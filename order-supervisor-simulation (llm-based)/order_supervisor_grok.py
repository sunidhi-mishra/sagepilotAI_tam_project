#!/usr/bin/env python3
"""
Order Supervisor Simulation with optional Grok LLM integration.

Run with rule-based policy (default):
  python3 order_supervisor_grok.py sample_events.json

Run with Grok LLM agent:
  GROK_API_KEY=<your-key> python3 order_supervisor_grok.py --llm sample_events.json

The LLM mode uses Grok to decide which tool to call on each wake-up,
grounded in the order's state. If the API fails or returns invalid output,
it falls back to the rule-based agent.
"""

import json
import sys
import os
import argparse
from dataclasses import dataclass, field
from typing import Optional, Set
from datetime import datetime

try:
    import requests
except ImportError:
    requests = None


@dataclass
class OrderState:
    """Tracks the order's current state."""
    order_id: str
    status: str = "active"
    open_issue: Optional[str] = None
    timeline: list = field(default_factory=list)
    memory_summary: str = ""
    last_activity_time: float = 0.0
    activity_log: list = field(default_factory=list)

    def _collapse_if_needed(self) -> None:
        """Fold older timeline entries into memory_summary if timeline exceeds TIMELINE_WINDOW."""
        if len(self.timeline) > CONFIG["TIMELINE_WINDOW"]:
            overflow = self.timeline[: len(self.timeline) - CONFIG["TIMELINE_WINDOW"]]
            self.timeline = self.timeline[len(self.timeline) - CONFIG["TIMELINE_WINDOW"] :]
            folded = " ".join([f"[t={e['time']}h] {e['entry']}" for e in overflow])
            self.memory_summary = (self.memory_summary + " " + folded).strip()

    def add_timeline_entry(self, time: float, entry: str) -> None:
        """Add an entry to the timeline and collapse if needed."""
        self.timeline.append({"time": time, "entry": entry})
        self._collapse_if_needed()


CONFIG = {
    "SCHEDULED_WAKE_INTERVAL_HOURS": 6,
    "TIMELINE_WINDOW": 5,
    "REFUND_AUTO_APPROVE_LIMIT": 2000,
    "TERMINAL_EVENT_TYPES": {"delivered", "refund_resolved", "manual_termination"},
    "STAY_ASLEEP_EVENT_TYPES": {"payment_confirmed", "shipment_created"},
}

TOOLS = {
    "message_customer": "Send a message to the customer via WhatsApp/Email/SMS.",
    "message_logistics_team": "Send a message to the logistics/courier team.",
    "create_internal_note": "Create an internal note in the order record.",
    "escalate": "Escalate to a human for immediate review.",
    "mark_for_review": "Flag the order for human review.",
}


class ToolBox:
    """Mock tool implementations."""

    def __init__(self, activity_log: list):
        self.activity_log = activity_log

    def message_customer(self, text: str) -> None:
        self.activity_log.append(f"[message_customer] {text}")

    def message_logistics_team(self, text: str) -> None:
        self.activity_log.append(f"[message_logistics_team] {text}")

    def create_internal_note(self, text: str) -> None:
        self.activity_log.append(f"[create_internal_note] {text}")

    def escalate(self, reason: str) -> None:
        self.activity_log.append(f"[escalate] {reason}")

    def mark_for_review(self, reason: str) -> None:
        self.activity_log.append(f"[mark_for_review] {reason}")

    def call_tool(self, tool_name: str, **kwargs) -> None:
        """Generic tool dispatcher."""
        if tool_name not in TOOLS:
            self.activity_log.append(f"[unknown_tool] {tool_name}")
            return
        method = getattr(self, tool_name, None)
        if method:
            text = kwargs.get("text") or kwargs.get("reason") or str(kwargs)
            method(text)


class Agent:
    """Rule-based decision agent (default)."""

    def decide_and_act(self, event: dict, state: OrderState, tools: ToolBox) -> None:
        """Make a decision based on event type and current state."""
        event_type = event["type"]
        data = event.get("data", {})

        if event_type == "payment_failed":
            tools.create_internal_note(f"Payment failed: {data.get('reason', 'unknown')}")
            tools.message_customer("We noticed an issue with your payment, retrying now.")
            state.add_timeline_entry(event["timestamp"], "Payment failure logged and customer notified")

        elif event_type == "shipment_delayed":
            reason = data.get("reason", "a logistics delay")
            tools.message_customer(f"Heads up, your order is delayed ({reason}). We're on it.")
            tools.message_logistics_team(f"Delay reported ({reason}), please confirm new ETA.")
            state.add_timeline_entry(event["timestamp"], f"Shipment delay handled ({reason})")
            state.open_issue = "shipment_delayed"

        elif event_type == "refund_requested":
            amount = data.get("amount", 0)
            if amount > CONFIG["REFUND_AUTO_APPROVE_LIMIT"]:
                tools.escalate(f"Refund of {amount} exceeds limit {CONFIG['REFUND_AUTO_APPROVE_LIMIT']}")
                state.add_timeline_entry(event["timestamp"], f"Refund of {amount} escalated (over limit)")
            else:
                tools.create_internal_note(f"Refund of {amount} approved within policy")
                tools.message_customer("Your refund has been approved, on its way, 3-5 business days.")
                state.add_timeline_entry(event["timestamp"], f"Refund of {amount} auto-approved")

        elif event_type == "customer_message_received":
            text = data.get("text", "").lower()
            if any(word in text for word in ["angry", "chargeback", "lawyer", "scam"]):
                tools.mark_for_review(f"Escalation language detected: {data.get('text', '')}")
                tools.message_customer("I'm sorry for the frustration, looping in a specialist right away.")
                state.add_timeline_entry(event["timestamp"], "Angry customer message flagged for review")
            elif state.open_issue == "shipment_delayed":
                tools.message_customer("Still tracking your delayed shipment, latest update coming shortly.")
                state.add_timeline_entry(event["timestamp"], "Replied to customer about delay")
            else:
                tools.message_customer("Thanks for reaching out, checking on this now.")
                state.add_timeline_entry(event["timestamp"], "Acknowledged customer message")

        elif event_type == "delivered":
            tools.message_customer("Your order has been delivered, hope you love it!")
            state.add_timeline_entry(event["timestamp"], "Delivery confirmed to customer")

        elif event_type == "refund_resolved":
            tools.create_internal_note("Refund confirmed processed by payment provider")
            state.add_timeline_entry(event["timestamp"], "Refund settlement confirmed")
            state.open_issue = None

        elif event_type == "manual_termination":
            tools.create_internal_note(f"Manually terminated: {data.get('reason', 'n/a')}")
            state.add_timeline_entry(event["timestamp"], "Manual termination recorded")

        elif event_type == "no_update_for_n_hours":
            if state.open_issue:
                tools.message_logistics_team(f"Checking in, still no resolution on: {state.open_issue}")
                state.add_timeline_entry(event["timestamp"], f"Scheduled check-in on {state.open_issue}")
            else:
                tools.create_internal_note("Scheduled check-in: nothing new, order on track")
                state.add_timeline_entry(event["timestamp"], "Scheduled check-in: no action needed")

        else:
            tools.create_internal_note(f"Unhandled event type: {event_type}")
            state.add_timeline_entry(event["timestamp"], f"Logged unhandled event: {event_type}")


class GrokAgent:
    """Grok-based decision agent with fallback."""

    def __init__(self, api_key: str):
        """Initialize Grok client."""
        if not requests:
            raise ImportError("requests not installed. Run: pip install requests")
        self.api_key = api_key
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.fallback_agent = Agent()
        self.call_count = 0
        self.fallback_count = 0

    def decide_and_act(self, event: dict, state: OrderState, tools: ToolBox) -> None:
        """Use Groq to decide which tool to call, with fallback to rule-based agent."""
        self.call_count += 1
        try:
            decision = self._query_grok(event, state)
            if decision:
                self._execute_decision(decision, event, state, tools)
            else:
                self._fallback(event, state, tools)
        except Exception as e:
            print(f"[Groq Error] {str(e)}, falling back to rule-based agent", file=sys.stderr)
            self.fallback_count += 1
            self.fallback_agent.decide_and_act(event, state, tools)

    def _query_grok(self, event: dict, state: OrderState) -> Optional[dict]:
        """Call Groq API and return parsed decision."""
        prompt = self._build_prompt(event, state)
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500,
        }

        try:
            response = requests.post(self.base_url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            result = response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            decision = self._parse_response(content)
            return decision
        except requests.exceptions.RequestException as e:
            print(f"[Grok API Error] {str(e)}", file=sys.stderr)
            return None
        except (json.JSONDecodeError, KeyError, AttributeError) as e:
            print(f"[Grok Parse Error] {str(e)}", file=sys.stderr)
            return None

    def _build_prompt(self, event: dict, state: OrderState) -> str:
        """Build the prompt with full context."""
        timeline_str = "\n".join([f"  [t={e['time']}h] {e['entry']}" for e in state.timeline[-3:]])
        tools_list = "\n".join([f"  - {tool}: {desc}" for tool, desc in TOOLS.items()])

        return f"""You are an order supervisor agent. Your job is to decide which tool to call based on the current event and order state.

Order State:
- ID: {state.order_id}
- Status: {state.status}
- Open Issue: {state.open_issue or "none"}
- Last Activity: t={state.last_activity_time}h

Recent Timeline:
{timeline_str or "  (no entries yet)"}

Memory Summary:
{state.memory_summary or "(no collapsed history yet)"}

Current Event:
- Type: {event['type']}
- Data: {json.dumps(event.get('data', {}))}
- Timestamp: t={event['timestamp']}h

Available Tools:
{tools_list}
  - escalate_to_human: if the situation requires human judgment and none of the above tools fit

Decision Rules:
1. Ground every decision in the event and state. Do not invent facts.
2. If no tool clearly applies, respond with "escalate_to_human".
3. Never call a tool without a concrete reason tied to the event data or state.
4. For refunds over 2000, always escalate.
5. For angry customer language, escalate.

Respond in this exact JSON format (no markdown, no code blocks, just raw JSON):
{{"tool": "<tool_name>", "reasoning": "<why this tool>", "text_or_reason": "<what to send/log>"}}

For example:
{{"tool": "message_customer", "reasoning": "Customer reported delay, needs reassurance", "text_or_reason": "We're tracking your delayed shipment..."}}

Now decide:
"""

    def _parse_response(self, content: str) -> Optional[dict]:
        """Parse Grok's response as JSON."""
        content = content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()
        result = json.loads(content)
        return result

    def _execute_decision(self, decision: dict, event: dict, state: OrderState, tools: ToolBox) -> None:
        """Execute the Grok decision."""
        tool_name = decision.get("tool", "escalate_to_human")
        text_or_reason = decision.get("text_or_reason", "No details provided")
        reasoning = decision.get("reasoning", "")

        if tool_name == "escalate_to_human":
            tools.escalate(text_or_reason)
            state.add_timeline_entry(event["timestamp"], f"Escalated to human: {reasoning}")
        elif tool_name in TOOLS:
            tools.call_tool(tool_name, text=text_or_reason)
            state.add_timeline_entry(event["timestamp"], f"Called {tool_name}: {reasoning}")
        else:
            tools.create_internal_note(f"Invalid tool from Grok: {tool_name}")
            state.add_timeline_entry(event["timestamp"], f"Invalid Grok tool: {tool_name}, logged")

        if event["type"] == "shipment_delayed":
            state.open_issue = "shipment_delayed"
        elif event["type"] == "refund_resolved":
            state.open_issue = None
        elif event["type"] == "delivered":
            state.open_issue = None

    def _fallback(self, event: dict, state: OrderState, tools: ToolBox) -> None:
        """Fallback to rule-based agent."""
        self.fallback_count += 1
        self.fallback_agent.decide_and_act(event, state, tools)


def wake_policy(event: dict) -> str:
    """Determine whether to wake the agent based on event type."""
    return "STAY_ASLEEP" if event["type"] in CONFIG["STAY_ASLEEP_EVENT_TYPES"] else "WAKE_NOW"


class OrderSupervisor:
    """Main supervisor orchestrator."""

    def __init__(self, use_llm: bool = False, api_key: Optional[str] = None, llm_provider: str = "grok"):
        self.use_llm = use_llm
        self.llm_provider = llm_provider
        if use_llm:
            if not api_key:
                api_key = os.environ.get("GROK_API_KEY")
            if not api_key:
                raise ValueError("GROK_API_KEY environment variable not set")
            self.agent = GrokAgent(api_key)
        else:
            self.agent = Agent()

    def run(self, events: list) -> dict:
        """Run the supervisor through all events."""
        sorted_events = sorted(events, key=lambda e: e["timestamp"])
        state = OrderState(order_id="ORDER-001")
        tools = ToolBox(state.activity_log)
        last_activity_time = 0.0
        trailing_scheduled_wakes = 0
        max_trailing = 3

        def process_event(event: dict) -> bool:
            nonlocal last_activity_time, trailing_scheduled_wakes
            last_activity_time = event["timestamp"]
            decision = wake_policy(event)

            if decision == "WAKE_NOW":
                self.agent.decide_and_act(event, state, tools)
                if CONFIG["TERMINAL_EVENT_TYPES"].intersection({event["type"]}):
                    state.status = f"closed: {event['type']}"
                    state.open_issue = None
                    return True
            return False

        i = 0
        while i < len(sorted_events) and state.status == "active":
            current_event = sorted_events[i]
            while current_event["timestamp"] - last_activity_time > CONFIG["SCHEDULED_WAKE_INTERVAL_HOURS"] and state.status == "active":
                scheduled_time = last_activity_time + CONFIG["SCHEDULED_WAKE_INTERVAL_HOURS"]
                synthetic_event = {"timestamp": scheduled_time, "type": "no_update_for_n_hours", "data": {}, "synthetic": True}
                if process_event(synthetic_event):
                    return self._build_summary(state)
            if state.status != "active":
                break
            if process_event(current_event):
                return self._build_summary(state)
            i += 1

        while state.status == "active" and trailing_scheduled_wakes < max_trailing:
            scheduled_time = last_activity_time + CONFIG["SCHEDULED_WAKE_INTERVAL_HOURS"]
            synthetic_event = {"timestamp": scheduled_time, "type": "no_update_for_n_hours", "data": {}, "synthetic": True}
            if process_event(synthetic_event):
                return self._build_summary(state)
            trailing_scheduled_wakes += 1

        return self._build_summary(state)

    def _build_summary(self, state: OrderState) -> dict:
        """Build the final run summary."""
        summary = {
            "order_id": state.order_id,
            "final_status": state.status,
            "final_open_issue": state.open_issue,
            "total_tool_calls": len(state.activity_log),
            "activity_log": state.activity_log,
            "timeline": state.timeline,
            "memory_summary": state.memory_summary,
        }
        if self.use_llm and isinstance(self.agent, GrokAgent):
            summary["llm_calls"] = self.agent.call_count
            summary["llm_fallbacks"] = self.agent.fallback_count
        return summary


def main():
    parser = argparse.ArgumentParser(description="Order Supervisor Simulation")
    parser.add_argument("events_file", help="JSON file with order events")
    parser.add_argument("--llm", action="store_true", help="Use Grok LLM agent (requires GROK_API_KEY)")
    args = parser.parse_args()

    with open(args.events_file) as f:
        events = json.load(f)

    supervisor = OrderSupervisor(use_llm=args.llm, api_key=os.environ.get("GROK_API_KEY"))
    result = supervisor.run(events)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
