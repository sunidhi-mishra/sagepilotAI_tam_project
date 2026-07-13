import React from "react";
import { TimelineEntry } from "../simulator/orderSupervisor";

interface TimelineStreamProps {
  timeline: TimelineEntry[];
}

export const TimelineStream: React.FC<TimelineStreamProps> = ({ timeline }) => {
  return (
    <div className="card col-4">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h3>Timeline</h3>
        <span className="demo-badge">{timeline.length} Steps</span>
      </div>
      
      <div className="timeline-list">
        {timeline.length === 0 ? (
          <div style={{ textAlign: "center", padding: "2rem", color: "var(--text-muted)", fontSize: "0.8rem" }}>
            No steps executed yet. Click "Step Forward" or "Run All" to start.
          </div>
        ) : (
          [...timeline].reverse().map((entry, index) => {
            const isEvent = entry.kind === "event";
            const badgeClass = isEvent
              ? entry.description.includes("WAKE_NOW")
                ? "badge-amber"
                : "badge-blue"
              : "badge-green";

            const badgeLabel = isEvent
              ? entry.description.includes("WAKE_NOW")
                ? "WOKE UP"
                : "ASLEEP"
              : "ACTION";

            return (
              <div key={index} className={`timeline-item kind-${entry.kind}`}>
                <div className="timeline-header">
                  <span>t = {entry.timestamp.toFixed(1)}h</span>
                  <span className={`badge ${badgeClass}`}>{badgeLabel}</span>
                </div>
                <div className="timeline-desc">{entry.description}</div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
