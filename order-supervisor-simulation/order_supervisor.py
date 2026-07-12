"""
order_supervisor.py -- in-memory simulation of an order supervisor.
No Temporal/DB/cloud. See README.md for the Temporal building-block mapping.

Run:
    python order_supervisor.py sample_events.json
    cat sample_events.json | python order_supervisor.py
"""

import json
import sys
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SCHEDULED_WAKE_INTERVAL_HOURS = 6  # durable timer interval -> see README
TIMELINE_WINDOW = 5                # entries kept verbatim before collapsing -> continue-as-new
MAX_TRAILING_SCHEDULED_WAKES = 3   # demo-only cap so a finite run terminates
TERMINAL_EVENT_TYPES = {"delivered", "refund_resolved", "manual_termination"}
STAY_ASLEEP_EVENT_TYPES = {"payment_confirmed", "shipment_created"}  # wake policy rule table


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Event:
    """One incoming signal for an order."""
    timestamp: float  # simulated hours since order start
    type: str
    data: dict = field(default_factory=dict)
    synthetic: bool = False  # True for scheduled wake-ups we inject ourselves

    @staticmethod
    def from_dict(d: dict) -> "Event":
        return Event(timestamp=float(d["timestamp"]), type=d["type"], data=d.get("data", {}))


@dataclass
class TimelineEntry:
    timestamp: float
    kind: str  # "event" or "action"
    description: str


# ---------------------------------------------------------------------------
# Wake policy -- maps to: the cheap synchronous check a signal handler
# runs BEFORE paying for a full agent reasoning step. See README.
# ---------------------------------------------------------------------------

class WakePolicy:
    """Rule-based screen: does this event wake the agent, or just get logged?"""

    @staticmethod
    def decide(event: Event) -> str:
        if event.type in STAY_ASLEEP_EVENT_TYPES:
            return "STAY_ASLEEP"
        return "WAKE_NOW"


# ---------------------------------------------------------------------------
# Mock tools -- maps to: Temporal Activities. Each call just appends a
# record to the activity log; nothing real is sent. See README.
# ---------------------------------------------------------------------------

class ToolBox:
    def __init__(self, activity_log: list):
        self.activity_log = activity_log

    def _log(self, tool: str, **kwargs):
        self.activity_log.append({"tool": tool, **kwargs})

    def message_customer(self, order_id: str, text: str):
        self._log("message_customer", order_id=order_id, text=text)

    def message_logistics_team(self, order_id: str, text: str):
        self._log("message_logistics_team", order_id=order_id, text=text)

    def create_internal_note(self, order_id: str, note: str):
        self._log("create_internal_note", order_id=order_id, note=note)

    def escalate(self, order_id: str, reason: str):
        self._log("escalate", order_id=order_id, reason=reason)

    def mark_for_review(self, order_id: str, reason: str):
        self._log("mark_for_review", order_id=order_id, reason=reason)


# ---------------------------------------------------------------------------
# Agent -- maps to: the reasoning step after WAKE_NOW. The ONE piece
# meant to be swapped for an LLM later -- see README. Termination stays
# workflow-owned regardless (per B1.4).
# ---------------------------------------------------------------------------

class Agent:
    """Rule-based stand-in for the reasoning step. Picks ONE action per wake."""

    def __init__(self, tools: ToolBox):
        self.tools = tools

    def decide_and_act(self, order_id: str, event: Event, state: "OrderState") -> str:
        """Returns a short description of the action taken, for the timeline."""

        if event.type == "payment_failed":
            self.tools.create_internal_note(
                order_id, f"Payment failed: {event.data.get('reason', 'unknown reason')}"
            )
            self.tools.message_customer(
                order_id,
                "We noticed an issue with your payment -- retrying now, we'll confirm shortly.",
            )
            return "Logged payment failure and reassured customer"

        if event.type == "shipment_delayed":
            reason = event.data.get("reason", "a logistics delay")
            self.tools.message_customer(
                order_id,
                f"Heads up -- your order is delayed ({reason}). We're on it and will update you.",
            )
            self.tools.message_logistics_team(
                order_id, f"Delay reported ({reason}) -- please confirm new ETA."
            )
            state.open_issue = "shipment_delayed"
            return "Notified customer of delay and pinged logistics for new ETA"

        if event.type == "refund_requested":
            amount = event.data.get("amount", 0)
            if amount > state.refund_auto_approve_limit:
                self.tools.escalate(
                    order_id,
                    f"Refund of {amount} exceeds auto-approve limit of {state.refund_auto_approve_limit}",
                )
                return f"Escalated refund request of {amount} (over auto-approve limit)"
            self.tools.create_internal_note(order_id, f"Refund of {amount} approved within policy")
            self.tools.message_customer(
                order_id, "Your refund has been approved and is on its way -- 3-5 business days."
            )
            return f"Auto-approved refund of {amount} within policy limit"

        if event.type == "customer_message_received":
            text = event.data.get("text", "")
            if any(w in text.lower() for w in ["angry", "chargeback", "lawyer", "scam"]):
                self.tools.mark_for_review(order_id, f"Escalation language detected: '{text}'")
                self.tools.message_customer(
                    order_id,
                    "I'm sorry for the frustration -- looping in a specialist to sort this out right away.",
                )
                return "Flagged escalation-language message for human review"
            if state.open_issue == "shipment_delayed":
                self.tools.message_customer(
                    order_id, "Still tracking your delayed shipment -- latest update coming shortly."
                )
                return "Replied to customer re: known open delay"
            self.tools.message_customer(order_id, "Thanks for reaching out -- checking on this now.")
            return "Acknowledged customer message"

        if event.type == "delivered":
            self.tools.message_customer(order_id, "Your order has been delivered -- hope you love it!")
            return "Sent delivery confirmation to customer"

        if event.type == "refund_resolved":
            self.tools.create_internal_note(order_id, "Refund confirmed processed by payment provider")
            return "Confirmed refund completion"

        if event.type == "manual_termination":
            self.tools.create_internal_note(order_id, f"Manually terminated: {event.data.get('reason', 'n/a')}")
            return "Recorded manual termination"

        if event.type == "no_update_for_n_hours":
            # Scheduled wake-up. Only takes action if something is unresolved --
            # otherwise it's a silent check-in, same as a human wouldn't ping
            # logistics about an order that's on track.
            if state.open_issue:
                self.tools.message_logistics_team(
                    order_id, f"Checking in -- still no resolution on: {state.open_issue}"
                )
                return f"Scheduled check-in: chased unresolved issue ({state.open_issue})"
            self.tools.create_internal_note(order_id, "Scheduled check-in: nothing new, order on track")
            return "Scheduled check-in: no action needed"

        # Fallback for any signal type not explicitly handled above.
        self.tools.create_internal_note(order_id, f"Unhandled event type: {event.type}")
        return f"Logged unhandled event type: {event.type}"


# ---------------------------------------------------------------------------
# Order state -- timeline/memory_summary maps to: the compact memory
# summary + timeline the agent refreshes before each sleep.
# ---------------------------------------------------------------------------

@dataclass
class OrderState:
    order_id: str
    status: str = "active"
    open_issue: Optional[str] = None
    refund_auto_approve_limit: float = 2000.0
    timeline: list = field(default_factory=list)        # list[TimelineEntry], recent detail
    memory_summary: str = ""                             # collapsed older detail
    activity_log: list = field(default_factory=list)     # every tool call, ever (full audit trail)

    def add_timeline_entry(self, timestamp: float, kind: str, description: str):
        self.timeline.append(TimelineEntry(timestamp, kind, description))
        self._collapse_if_needed()

    def _collapse_if_needed(self):
        """Keep last TIMELINE_WINDOW entries verbatim; fold older ones into
        the rolling summary instead of growing without bound (continue-as-new
        analogue -- see README)."""
        if len(self.timeline) <= TIMELINE_WINDOW:
            return
        overflow = self.timeline[: len(self.timeline) - TIMELINE_WINDOW]
        self.timeline = self.timeline[len(self.timeline) - TIMELINE_WINDOW :]
        folded = "; ".join(f"[t={e.timestamp}h] {e.description}" for e in overflow)
        self.memory_summary = (self.memory_summary + " " + folded).strip() if self.memory_summary else folded


# ---------------------------------------------------------------------------
# Supervisor loop -- maps to: the Temporal Workflow function itself, the
# durable "one workflow per order" loop owning state, signals, timers,
# and the (never agent-owned) termination decision. See README.
# ---------------------------------------------------------------------------

class OrderSupervisor:
    def __init__(self, order_id: str):
        self.state = OrderState(order_id=order_id)
        self.tools = ToolBox(self.state.activity_log)
        self.agent = Agent(self.tools)
        self.last_activity_time = 0.0

    def run(self, events: list) -> OrderState:
        events = sorted(events, key=lambda e: e.timestamp)
        i = 0
        while i < len(events):
            event = events[i]

            # Fire any scheduled wake-ups that fall due before this event.
            # This is the durable timer: the supervisor wakes itself even
            # if nothing external happened.
            while event.timestamp - self.last_activity_time > SCHEDULED_WAKE_INTERVAL_HOURS:
                scheduled_time = self.last_activity_time + SCHEDULED_WAKE_INTERVAL_HOURS
                self._handle_event(Event(scheduled_time, "no_update_for_n_hours", synthetic=True))
                if self.state.status != "active":
                    return self._finalize()

            self._handle_event(event)
            i += 1
            if self.state.status != "active":
                return self._finalize()

        # Input exhausted but order still open: simulate a bounded number
        # of trailing scheduled wakes (production would keep sleeping/
        # waking indefinitely; this cap only exists so the demo halts).
        trailing = 0
        while self.state.status == "active" and trailing < MAX_TRAILING_SCHEDULED_WAKES:
            scheduled_time = self.last_activity_time + SCHEDULED_WAKE_INTERVAL_HOURS
            self._handle_event(Event(scheduled_time, "no_update_for_n_hours", synthetic=True))
            trailing += 1
            if self.state.status != "active":
                return self._finalize()

        return self._finalize(still_open=True)

    def _handle_event(self, event: Event):
        self.last_activity_time = event.timestamp
        decision = WakePolicy.decide(event)

        label = event.type + (" (scheduled)" if event.synthetic else "")
        self.state.add_timeline_entry(event.timestamp, "event", f"{label} -> {decision}")

        if decision == "STAY_ASLEEP":
            return  # logged only -- no reasoning, no tool calls, agent stays asleep

        action_desc = self.agent.decide_and_act(self.state.order_id, event, self.state)
        self.state.add_timeline_entry(event.timestamp, "action", action_desc)

        if event.type in TERMINAL_EVENT_TYPES:
            self.state.status = f"closed:{event.type}"
            self.state.open_issue = None  # order closed -- nothing left to chase

    def _finalize(self, still_open: bool = False) -> OrderState:
        print_final_summary(self.state, still_open)
        return self.state


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_final_summary(state: OrderState, still_open: bool):
    print("\n" + "=" * 70)
    print(f"FINAL SUMMARY -- Order {state.order_id}")
    print("=" * 70)
    print(f"Status: {'STILL OPEN (demo cap reached)' if still_open else state.status}")

    print(f"\nActions taken ({len(state.activity_log)} tool calls):")
    for a in state.activity_log:
        extra = {k: v for k, v in a.items() if k != "tool"}
        print(f"  - {a['tool']}: {extra}")

    print("\nRolling memory summary (collapsed older detail):")
    print(f"  {state.memory_summary or '(nothing collapsed yet -- fewer than ' + str(TIMELINE_WINDOW) + ' entries so far)'}")

    print(f"\nRecent timeline (last {len(state.timeline)} entries kept verbatim):")
    for e in state.timeline:
        print(f"  [t={e.timestamp}h] ({e.kind}) {e.description}")

    print("\nLearnings:")
    if state.open_issue:
        print(f"  - Run ended with an unresolved issue flag still set: {state.open_issue}")
    else:
        print("  - No unresolved issues flagged at close.")
    print(f"  - {len(state.activity_log)} tool calls made across the run.")
    print(f"  - {len([1 for e in state.activity_log if e['tool'] == 'escalate'])} escalation(s) to a human.")
    print("=" * 70 + "\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def load_events(path: Optional[str]) -> list:
    raw = json.load(open(path)) if path else json.load(sys.stdin)
    return [Event.from_dict(d) for d in raw]


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    events = load_events(path)
    supervisor = OrderSupervisor("ORDER-DEMO-001")
    supervisor.run(events)


if __name__ == "__main__":
    main()
