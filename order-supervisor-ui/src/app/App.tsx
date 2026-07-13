import React, { useState } from "react";
import { OrderSupervisor, Event, OrderState } from "../simulator/orderSupervisor";
import { TimelineStream } from "../components/TimelineStream";
import { ChannelTabs } from "../components/ChannelTabs";
import { ReviewWidget } from "../components/ReviewWidget";

// Load sample events matching e:\SideProjects\sagepilotAI_tam_project\order-supervisor-simulation\sample_events.json
const SAMPLE_EVENTS: Event[] = [
  { timestamp: 0, type: "payment_failed", data: { reason: "card declined" } },
  { timestamp: 0.5, type: "payment_confirmed", data: {} },
  { timestamp: 1, type: "shipment_created", data: { tracking_id: "TRK-4821" } },
  { timestamp: 20, type: "shipment_delayed", data: { reason: "courier backlog" } },
  { timestamp: 22, type: "customer_message_received", data: { text: "Hey, where is my order? It's been a while." } },
  { timestamp: 40, type: "customer_message_received", data: { text: "This is ridiculous, I want a refund or I'm filing a chargeback." } },
  { timestamp: 41, type: "refund_requested", data: { amount: 2600 } },
  { timestamp: 70, type: "delivered", data: {} },
];

const App: React.FC = () => {
  const [events] = useState<Event[]>(SAMPLE_EVENTS);
  const [currentStep, setCurrentStep] = useState<number>(0);
  const [supervisor, setSupervisor] = useState<OrderSupervisor>(new OrderSupervisor("ORDER-DEMO-001"));
  const [snapshots, setSnapshots] = useState<{ stateSnapshot: OrderState; eventHandled: Event }[]>([]);
  const [limitInput, setLimitInput] = useState<number>(2000);
  const [isEscalatedOverride, setIsEscalatedOverride] = useState<boolean>(false);

  // Initialize and run full simulation
  const runFullSimulation = () => {
    const freshSupervisor = new OrderSupervisor("ORDER-DEMO-001");
    freshSupervisor.state.refundAutoApproveLimit = limitInput;
    const history = freshSupervisor.runSimulation(events);
    setSupervisor(freshSupervisor);
    setSnapshots(history);
    setCurrentStep(history.length);
    setIsEscalatedOverride(false);
  };

  // Step-by-step controller
  const stepForward = () => {
    if (snapshots.length === 0) {
      // Calculate snapshots first
      const freshSupervisor = new OrderSupervisor("ORDER-DEMO-001");
      freshSupervisor.state.refundAutoApproveLimit = limitInput;
      const history = freshSupervisor.runSimulation(events);
      setSnapshots(history);
      if (history.length > 0) {
        setSupervisor(freshSupervisor);
        setCurrentStep(1);
      }
    } else if (currentStep < snapshots.length) {
      setCurrentStep(prev => prev + 1);
    }
  };

  const resetSimulation = () => {
    setSupervisor(new OrderSupervisor("ORDER-DEMO-001"));
    setSnapshots([]);
    setCurrentStep(0);
    setIsEscalatedOverride(false);
  };

  // Human-in-the-loop triggers
  const handleApproveRefund = () => {
    // Add manual override logs to state
    const currentState = getActiveState();
    currentState.activityLog.push({
      tool: "create_internal_note",
      order_id: currentState.orderId,
      note: "Human Override: Approved refund of $2,600 manually."
    });
    currentState.activityLog.push({
      tool: "message_customer",
      order_id: currentState.orderId,
      text: "We have reviewed your request and approved a refund of $2,600 manually."
    });
    currentState.addTimelineEntry(
      currentState.timeline[currentState.timeline.length - 1]?.timestamp || 41,
      "action",
      "Human Override: Approved overlimit refund"
    );
    setIsEscalatedOverride(false);
    // Force React re-render
    setSnapshots([...snapshots]);
  };

  const handleRejectRefund = () => {
    const currentState = getActiveState();
    currentState.activityLog.push({
      tool: "create_internal_note",
      order_id: currentState.orderId,
      note: "Human Action: Declined refund. Ticket sent to finance desk."
    });
    currentState.addTimelineEntry(
      currentState.timeline[currentState.timeline.length - 1]?.timestamp || 41,
      "action",
      "Human Action: Declined refund and escalated to finance desk"
    );
    setIsEscalatedOverride(false);
    setSnapshots([...snapshots]);
  };

  // Get active state representation
  const getActiveState = (): OrderState => {
    if (snapshots.length > 0 && currentStep > 0) {
      return snapshots[Math.min(currentStep - 1, snapshots.length - 1)].stateSnapshot;
    }
    return supervisor.state;
  };

  const getActiveEvent = (): Event | null => {
    if (snapshots.length > 0 && currentStep > 0) {
      return snapshots[Math.min(currentStep - 1, snapshots.length - 1)].eventHandled;
    }
    return null;
  };

  const activeState = getActiveState();
  const activeEvent = getActiveEvent();

  return (
    <div className="app-container">

      {/* Compact Title */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", borderBottom: "1px solid var(--border-light)", paddingBottom: "1rem" }}>
        <div>
          <h2 style={{ fontSize: "1.6rem", fontWeight: 800 }}>Order Supervisor Simulator</h2>
          <p style={{ fontSize: "0.85rem", color: "var(--text-secondary)", marginTop: "0.25rem" }}>
            <span className="badge badge-blue" style={{ marginRight: "0.5rem", textTransform: "none", verticalAlign: "middle" }}>Rule-Based</span>
            Replays order lifecycles and handles delays, failures, and overrides in memory.
          </p>
        </div>
        <span style={{ fontSize: "0.85rem", color: "var(--text-secondary)", fontWeight: 600 }}>ORDER-DEMO-001</span>
      </div>

      {/* Main Bento Grid */}
      <main className="bento-grid">
        
        {/* Simulation Controls */}
        <div className="card col-6">
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <h3>Control Center</h3>
            <span className="badge badge-blue">Interactive</span>
          </div>
          
          <div style={{ display: "flex", flexDirection: "column", gap: "1rem", marginTop: "0.5rem" }}>
            <div>
              <div style={{ display: "flex", justifyContent: "space-between", fontSize: "0.85rem", fontWeight: 600, color: "var(--text-secondary)" }}>
                <span>Auto-Approve Threshold</span>
                <span style={{ fontWeight: 700 }}>${limitInput}</span>
              </div>
              <div style={{ display: "flex", gap: "1rem", alignItems: "center", marginTop: "0.25rem" }}>
                <input 
                  type="range" 
                  min="500" 
                  max="5000" 
                  step="100" 
                  value={limitInput}
                  onChange={(e) => {
                    setLimitInput(Number(e.target.value));
                    resetSimulation();
                  }}
                  style={{ flex: 1, accentColor: "var(--accent-mint)" }}
                />
              </div>
            </div>

            <div style={{ display: "flex", gap: "0.5rem", marginTop: "0.25rem" }}>
              <button className="btn btn-primary" onClick={runFullSimulation}>
                Run All
              </button>
              <button className="btn btn-secondary" onClick={stepForward} disabled={snapshots.length > 0 && currentStep >= snapshots.length}>
                Step Forward {snapshots.length > 0 ? `(${currentStep}/${snapshots.length})` : ""}
              </button>
              <button className="btn btn-secondary" onClick={resetSimulation}>
                Reset
              </button>
            </div>

            {activeEvent && (
              <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", backgroundColor: "var(--bg-secondary)", padding: "0.5rem 0.75rem", borderRadius: "8px", border: "1px solid var(--border-light)", fontSize: "0.8rem" }}>
                <span>Event: <code style={{ color: "var(--accent-mint-hover)", fontWeight: 700 }}>{activeEvent.type}</code></span>
                <span>Time: <strong>{activeEvent.timestamp}h</strong></span>
              </div>
            )}
          </div>
        </div>

        {/* Supervisor State Overview */}
        <div className="card col-6">
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <h3>System Status</h3>
            <span className={`badge ${activeState.status.includes("closed") ? "badge-green" : "badge-amber"}`}>
              {activeState.status.toUpperCase()}
            </span>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1rem", marginTop: "0.5rem" }}>
            <div style={{ borderLeft: "3px solid var(--accent-mint)", paddingLeft: "0.75rem" }}>
              <div style={{ fontSize: "0.7rem", color: "var(--text-muted)", fontWeight: 600 }}>ACTIVE FLAG</div>
              <div style={{ fontSize: "0.95rem", fontWeight: 700 }}>{activeState.openIssue || "None"}</div>
            </div>
            <div style={{ borderLeft: "3px solid var(--status-blue-text)", paddingLeft: "0.75rem" }}>
              <div style={{ fontSize: "0.7rem", color: "var(--text-muted)", fontWeight: 600 }}>ACTIVITIES</div>
              <div style={{ fontSize: "0.95rem", fontWeight: 700 }}>{activeState.activityLog.length} calls</div>
            </div>
          </div>

          <div style={{ marginTop: "0.5rem" }}>
            <div style={{ fontSize: "0.7rem", color: "var(--text-muted)", fontWeight: 600, marginBottom: "0.25rem" }}>
              STATE MEMORY
            </div>
            <div style={{ backgroundColor: "var(--bg-secondary)", padding: "0.5rem 0.75rem", borderRadius: "8px", border: "1px solid var(--border-light)", fontSize: "0.75rem", color: "var(--text-secondary)", minHeight: "50px", maxHeight: "80px", overflowY: "auto", lineHeight: "1.4" }}>
              {activeState.memorySummary || "(Timeline under 5 items)"}
            </div>
          </div>
        </div>

        {/* Bento Grid Row 2: Live Stream, Communications, HITL widget */}
        <TimelineStream timeline={activeState.timeline} />
        
        <ChannelTabs activityLog={activeState.activityLog} />
        
        <ReviewWidget 
          state={activeState}
          onApproveRefund={handleApproveRefund}
          onRejectRefund={handleRejectRefund}
          isEscalated={isEscalatedOverride}
        />

      </main>

      <footer style={{ marginTop: "auto", padding: "2rem 0 1rem 0", borderTop: "1px solid var(--border-light)", textAlign: "center", color: "var(--text-muted)", fontSize: "0.8rem" }}>
        © 2026 Sagepilot Inc. All rights reserved. Order Supervisor Simulation & Analytics.
      </footer>
    </div>
  );
};

export default App;
