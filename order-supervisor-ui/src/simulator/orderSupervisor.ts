// Configuration constants matching the python implementation
export const SCHEDULED_WAKE_INTERVAL_HOURS = 6;
export const TIMELINE_WINDOW = 5;
export const MAX_TRAILING_SCHEDULED_WAKES = 3;
export const TERMINAL_EVENT_TYPES = new Set(["delivered", "refund_resolved", "manual_termination"]);
export const STAY_ASLEEP_EVENT_TYPES = new Set(["payment_confirmed", "shipment_created"]);

export interface Event {
  timestamp: number; // simulated hours since order start
  type: string;
  data?: Record<string, any>;
  synthetic?: boolean; // True for scheduled wake-ups injected by supervisor
}

export interface TimelineEntry {
  timestamp: number;
  kind: "event" | "action";
  description: string;
}

export interface ActivityLogEntry {
  tool: string;
  order_id: string;
  [key: string]: any;
}

export class WakePolicy {
  static decide(event: Event): "WAKE_NOW" | "STAY_ASLEEP" {
    if (STAY_ASLEEP_EVENT_TYPES.has(event.type)) {
      return "STAY_ASLEEP";
    }
    return "WAKE_NOW";
  }
}

export class ToolBox {
  constructor(private activityLog: ActivityLogEntry[]) {}

  private log(tool: string, order_id: string, extra: Record<string, any>) {
    this.activityLog.push({ tool, order_id, ...extra });
  }

  message_customer(orderId: string, text: string) {
    this.log("message_customer", orderId, { text });
  }

  message_logistics_team(orderId: string, text: string) {
    this.log("message_logistics_team", orderId, { text });
  }

  create_internal_note(orderId: string, note: string) {
    this.log("create_internal_note", orderId, { note });
  }

  escalate(orderId: string, reason: string) {
    this.log("escalate", orderId, { reason });
  }

  mark_for_review(orderId: string, reason: string) {
    this.log("mark_for_review", orderId, { reason });
  }
}

export class Agent {
  constructor(private tools: ToolBox) {}

  decideAndAct(orderId: string, event: Event, state: OrderState): string {
    const data = event.data || {};

    if (event.type === "payment_failed") {
      const reason = data.reason || "unknown reason";
      this.tools.create_internal_note(orderId, `Payment failed: ${reason}`);
      this.tools.message_customer(
        orderId,
        "We noticed an issue with your payment -- retrying now, we'll confirm shortly."
      );
      return "Logged payment failure and reassured customer";
    }

    if (event.type === "shipment_delayed") {
      const reason = data.reason || "a logistics delay";
      this.tools.message_customer(
        orderId,
        `Heads up -- your order is delayed (${reason}). We're on it and will update you.`
      );
      this.tools.message_logistics_team(
        orderId,
        `Delay reported (${reason}) -- please confirm new ETA.`
      );
      state.openIssue = "shipment_delayed";
      return "Notified customer of delay and pinged logistics for new ETA";
    }

    if (event.type === "refund_requested") {
      const amount = data.amount || 0;
      if (amount > state.refundAutoApproveLimit) {
        this.tools.escalate(
          orderId,
          `Refund of ${amount} exceeds auto-approve limit of ${state.refundAutoApproveLimit}`
        );
        return `Escalated refund request of ${amount} (over auto-approve limit)`;
      }
      this.tools.create_internal_note(orderId, `Refund of ${amount} approved within policy`);
      this.tools.message_customer(
        orderId,
        "Your refund has been approved and is on its way -- 3-5 business days."
      );
      return `Auto-approved refund of ${amount} within policy limit`;
    }

    if (event.type === "customer_message_received") {
      const text = data.text || "";
      const lowerText = text.toLowerCase();
      const triggerWords = ["angry", "chargeback", "lawyer", "scam"];
      
      if (triggerWords.some(word => lowerText.includes(word))) {
        this.tools.mark_for_review(orderId, `Escalation language detected: '${text}'`);
        this.tools.message_customer(
          orderId,
          "I'm sorry for the frustration -- looping in a specialist to sort this out right away."
        );
        return "Flagged escalation-language message for human review";
      }
      
      if (state.openIssue === "shipment_delayed") {
        this.tools.message_customer(
          orderId,
          "Still tracking your delayed shipment -- latest update coming shortly."
        );
        return "Replied to customer re: known open delay";
      }
      
      this.tools.message_customer(orderId, "Thanks for reaching out -- checking on this now.");
      return "Acknowledged customer message";
    }

    if (event.type === "delivered") {
      this.tools.message_customer(orderId, "Your order has been delivered -- hope you love it!");
      return "Sent delivery confirmation to customer";
    }

    if (event.type === "refund_resolved") {
      this.tools.create_internal_note(orderId, "Refund confirmed processed by payment provider");
      return "Confirmed refund completion";
    }

    if (event.type === "manual_termination") {
      this.tools.create_internal_note(orderId, `Manually terminated: ${data.reason || "n/a"}`);
      return "Recorded manual termination";
    }

    if (event.type === "no_update_for_n_hours") {
      if (state.openIssue) {
        this.tools.message_logistics_team(
          orderId,
          `Checking in -- still no resolution on: ${state.openIssue}`
        );
        return `Scheduled check-in: chased unresolved issue (${state.openIssue})`;
      }
      this.tools.create_internal_note(orderId, "Scheduled check-in: nothing new, order on track");
      return "Scheduled check-in: no action needed";
    }

    this.tools.create_internal_note(orderId, `Unhandled event type: ${event.type}`);
    return `Logged unhandled event type: ${event.type}`;
  }
}

export class OrderState {
  orderId: string;
  status: string = "active";
  openIssue: string | null = null;
  refundAutoApproveLimit: number = 2000.0;
  timeline: TimelineEntry[] = [];
  memorySummary: string = "";
  activityLog: ActivityLogEntry[] = [];

  constructor(orderId: string) {
    this.orderId = orderId;
  }

  addTimelineEntry(timestamp: number, kind: "event" | "action", description: string) {
    this.timeline.push({ timestamp, kind, description });
    this.collapseIfNeeded();
  }

  private collapseIfNeeded() {
    if (this.timeline.length <= TIMELINE_WINDOW) {
      return;
    }
    const overflow = this.timeline.slice(0, this.timeline.length - TIMELINE_WINDOW);
    this.timeline = this.timeline.slice(this.timeline.length - TIMELINE_WINDOW);
    
    const folded = overflow.map(e => `[t=${e.timestamp}h] ${e.description}`).join("; ");
    this.memorySummary = this.memorySummary 
      ? (this.memorySummary + " " + folded).trim()
      : folded;
  }
}

export class OrderSupervisor {
  state: OrderState;
  tools: ToolBox;
  agent: Agent;
  lastActivityTime: number = 0.0;

  constructor(orderId: string) {
    this.state = new OrderState(orderId);
    this.tools = new ToolBox(this.state.activityLog);
    this.agent = new Agent(this.tools);
  }

  // Handle a single event
  handleEvent(event: Event) {
    this.lastActivityTime = event.timestamp;
    const decision = WakePolicy.decide(event);
    const label = event.type + (event.synthetic ? " (scheduled)" : "");
    
    this.state.addTimelineEntry(event.timestamp, "event", `${label} -> ${decision}`);
    
    if (decision === "STAY_ASLEEP") {
      return;
    }

    const actionDesc = this.agent.decideAndAct(this.state.orderId, event, this.state);
    this.state.addTimelineEntry(event.timestamp, "action", actionDesc);

    if (TERMINAL_EVENT_TYPES.has(event.type)) {
      this.state.status = `closed:${event.type}`;
      this.state.openIssue = null;
    }
  }

  // Run whole simulation and return historical states for animation/step playback
  runSimulation(events: Event[]): { stateSnapshot: OrderState; eventHandled: Event }[] {
    const snapshots: { stateSnapshot: OrderState; eventHandled: Event }[] = [];
    const sortedEvents = [...events].sort((a, b) => a.timestamp - b.timestamp);
    
    let i = 0;
    while (i < sortedEvents.length) {
      const event = sortedEvents[i];

      // Insert scheduled timer wake ups
      while (event.timestamp - this.lastActivityTime > SCHEDULED_WAKE_INTERVAL_HOURS) {
        const scheduledTime = this.lastActivityTime + SCHEDULED_WAKE_INTERVAL_HOURS;
        const syntheticEvent: Event = {
          timestamp: scheduledTime,
          type: "no_update_for_n_hours",
          synthetic: true
        };
        this.handleEvent(syntheticEvent);
        snapshots.push({
          stateSnapshot: this.cloneState(this.state),
          eventHandled: syntheticEvent
        });
        
        if (this.state.status !== "active") {
          return snapshots;
        }
      }

      this.handleEvent(event);
      snapshots.push({
        stateSnapshot: this.cloneState(this.state),
        eventHandled: event
      });
      
      i++;
      if (this.state.status !== "active") {
        return snapshots;
      }
    }

    // Trailing check-ins
    let trailing = 0;
    while (this.state.status === "active" && trailing < MAX_TRAILING_SCHEDULED_WAKES) {
      const scheduledTime = this.lastActivityTime + SCHEDULED_WAKE_INTERVAL_HOURS;
      const syntheticEvent: Event = {
        timestamp: scheduledTime,
        type: "no_update_for_n_hours",
        synthetic: true
      };
      this.handleEvent(syntheticEvent);
      snapshots.push({
        stateSnapshot: this.cloneState(this.state),
        eventHandled: syntheticEvent
      });
      trailing++;
    }

    return snapshots;
  }

  private cloneState(state: OrderState): OrderState {
    const clone = new OrderState(state.orderId);
    clone.status = state.status;
    clone.openIssue = state.openIssue;
    clone.refundAutoApproveLimit = state.refundAutoApproveLimit;
    clone.timeline = [...state.timeline];
    clone.memorySummary = state.memorySummary;
    clone.activityLog = [...state.activityLog];
    return clone;
  }
}
