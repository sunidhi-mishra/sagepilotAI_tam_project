import React from "react";
import { OrderState } from "../simulator/orderSupervisor";

interface ReviewWidgetProps {
  state: OrderState;
  onApproveRefund: () => void;
  onRejectRefund: () => void;
  isEscalated: boolean;
}

export const ReviewWidget: React.FC<ReviewWidgetProps> = ({
  state,
  onApproveRefund,
  onRejectRefund,
  isEscalated,
}) => {
  // Check if we have an escalation in the activity log
  const hasEscalation = state.activityLog.some(log => log.tool === "escalate");
  const hasReview = state.activityLog.some(log => log.tool === "mark_for_review");

  return (
    <div className="card col-4">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h3>Policy Interventions</h3>
        <span className={`badge ${hasEscalation || isEscalated ? "badge-red" : hasReview ? "badge-amber" : "badge-green"}`}>
          {hasEscalation || isEscalated ? "Action Needed" : hasReview ? "Under Review" : "System Safe"}
        </span>
      </div>

      {hasEscalation || isEscalated ? (
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          <div className="diff-view">
            <div className="diff-line deletion">- "auto_approve": false</div>
            <div className="diff-line addition">+ "human_override": true</div>
            <div className="diff-line">  "refund_amount": 2600</div>
            <div className="diff-line">  "limit": {state.refundAutoApproveLimit}</div>
          </div>
          <div style={{ display: "flex", gap: "0.5rem" }}>
            <button className="btn btn-primary" style={{ flex: 1 }} onClick={onApproveRefund}>
              Approve Overlimit Refund
            </button>
            <button className="btn btn-secondary" style={{ flex: 1 }} onClick={onRejectRefund}>
              Decline & Escalate
            </button>
          </div>
        </div>
      ) : hasReview ? (
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          <div style={{ backgroundColor: "var(--status-amber-bg)", color: "var(--status-amber-text)", padding: "0.75rem", borderRadius: "6px", fontSize: "0.85rem", fontWeight: 600 }}>
            ⚠️ High frustration language detected. Escalated customer query logged.
          </div>
          <div className="diff-view">
            <div className="diff-line">  "customer_sentiment": "angry"</div>
            <div className="diff-line">  "chargeback_risk": "high"</div>
          </div>
          <button className="btn btn-secondary" disabled>
            Specialist Review Initiated
          </button>
        </div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: "150px", border: "1px dashed var(--border-dark)", borderRadius: "8px", gap: "0.5rem" }}>
          <span style={{ fontSize: "2rem" }}>✓</span>
          <div style={{ fontSize: "0.85rem", color: "var(--text-secondary)", fontWeight: 600 }}>
            All operations running autonomously
          </div>
          <div style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>
            Supervisor checks are within policy limits
          </div>
        </div>
      )}
    </div>
  );
};
