import React, { useState } from "react";
import { ActivityLogEntry } from "../simulator/orderSupervisor";

interface ChannelTabsProps {
  activityLog: ActivityLogEntry[];
}

type Channel = "whatsapp" | "email" | "logistics";

export const ChannelTabs: React.FC<ChannelTabsProps> = ({ activityLog }) => {
  const [activeTab, setActiveTab] = useState<Channel>("whatsapp");

  // Filter communication events
  const customerMessages = activityLog.filter(
    (log) => log.tool === "message_customer"
  );
  const logisticsMessages = activityLog.filter(
    (log) => log.tool === "message_logistics_team"
  );

  return (
    <div className="card col-4">
      <div className="tabs-header">
        <button
          className={`tab-btn ${activeTab === "whatsapp" ? "active" : ""}`}
          onClick={() => setActiveTab("whatsapp")}
        >
          WhatsApp View
        </button>
        <button
          className={`tab-btn ${activeTab === "email" ? "active" : ""}`}
          onClick={() => setActiveTab("email")}
        >
          Customer Email
        </button>
        <button
          className={`tab-btn ${activeTab === "logistics" ? "active" : ""}`}
          onClick={() => setActiveTab("logistics")}
        >
          Logistics Slack
        </button>
      </div>

      <div className="chat-container">
        {activeTab === "whatsapp" && (
          <>
            <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textAlign: "center", marginBottom: "0.5rem" }}>
              WhatsApp chat with Customer
            </div>
            {customerMessages.length === 0 ? (
              <div style={{ margin: "auto", color: "var(--text-muted)", fontSize: "0.85rem" }}>
                No messages sent yet
              </div>
            ) : (
              customerMessages.map((msg, i) => (
                <div key={i} className="chat-bubble sent">
                  <div>{msg.text}</div>
                  <div className="chat-time">Agent • Delivered</div>
                </div>
              ))
            )}
          </>
        )}

        {activeTab === "email" && (
          <>
            <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textAlign: "center", marginBottom: "0.5rem" }}>
              Email Thread: Support Ticket
            </div>
            {customerMessages.length === 0 ? (
              <div style={{ margin: "auto", color: "var(--text-muted)", fontSize: "0.85rem" }}>
                No emails dispatched
              </div>
            ) : (
              customerMessages.map((msg, i) => (
                <div key={i} className="chat-bubble sent" style={{ alignSelf: "stretch", borderRadius: "8px", borderLeft: "4px solid var(--accent-mint)" }}>
                  <div style={{ fontWeight: 600, fontSize: "0.75rem", color: "var(--text-secondary)" }}>From: support@sagepilot.ai</div>
                  <div style={{ marginTop: "0.25rem" }}>{msg.text}</div>
                </div>
              ))
            )}
          </>
        )}

        {activeTab === "logistics" && (
          <>
            <div style={{ fontSize: "0.75rem", color: "var(--text-muted)", textAlign: "center", marginBottom: "0.5rem" }}>
              #ops-escalations (Slack)
            </div>
            {logisticsMessages.length === 0 ? (
              <div style={{ margin: "auto", color: "var(--text-muted)", fontSize: "0.85rem" }}>
                No log messages sent to courier operations team
              </div>
            ) : (
              logisticsMessages.map((msg, i) => (
                <div key={i} className="chat-bubble sent" style={{ backgroundColor: "#F1F3F5", border: "1px solid var(--border-dark)" }}>
                  <div style={{ fontWeight: 600, color: "var(--text-primary)", fontSize: "0.75rem" }}>[BOT] Order Supervisor</div>
                  <div>{msg.text}</div>
                  <div className="chat-time">Ops Channel</div>
                </div>
              ))
            )}
          </>
        )}
      </div>
    </div>
  );
};
