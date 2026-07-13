# Problem Statement: Order Supervisor System

## Overview
In high-volume e-commerce and logistics systems, tracking order fulfillment is complex. Orders frequently experience issues like payment failures, shipment delays, courier backlogs, and customer escalations. Standard static state-machine configurations struggle to adapt to these non-linear events, leading to either poor customer communication or excessive operational burden on support staff.

## The Goal
The objective is to build a smart **Order Supervisor**—a durable, agentic workflow that manages the end-to-end lifecycle of a customer order. The system handles updates, runs cheap rule-based filtering to decide whether to activate expensive LLM-based reasoning, triggers appropriate tools (activities), and retains a clean, summarized history of the order state to comply with system constraints.

## Core Pillars of the System

### 1. Durable Lifecycle (Workflows & Timers)
- The supervisor must track the order over its lifetime (which can span days or weeks).
- It receives external **Signals** (e.g., payment failures, shipment delays, customer inquiries).
- It must wake up automatically after set periods of inactivity (e.g., every 6 hours) via **Durable Timers** to audit the order status and follow up on unresolved issues.

### 2. Wake Policy
- To control computational costs and avoid spamming external services, the supervisor employs a two-bucket rule screen:
  - **Routine Events** (e.g., `payment_confirmed`, `shipment_created`) get logged directly to the timeline without waking the reasoning engine (`STAY_ASLEEP`).
  - **Exception Events** (e.g., `payment_failed`, `shipment_delayed`, `customer_message_received`) wake up the supervisor (`WAKE_NOW`).

### 3. Agentic Actions (Tool Executions)
- Once awake, the reasoning agent evaluates the order history and calls appropriate **Activities**:
  - `message_customer`: Sending SMS/Email/WhatsApp alerts.
  - `message_logistics_team`: Raising escalations to courier partners.
  - `create_internal_note`: Adding a log to the order record.
  - `escalate` / `mark_for_review`: Flagging anomalies for human-in-the-loop review.

### 4. Memory Management (Continue-as-New)
- To prevent the order timeline/event history from growing infinitely (which causes memory bloat and degraded replay performance in workflow engines like Temporal), older timeline details are periodically rolled up into a collapsed text summary (`memory_summary`), while keeping only the latest window of entries verbatim.

### 5. Deterministic Termination
- The workflow must terminate deterministically based on standard termination states (`delivered`, `refund_resolved`, `manual_termination`) rather than letting the AI agent decide when to stop.

## UI Objectives
Create an interactive, premium frontend application to visualize this entire process. Users should be able to:
- Run the simulation step-by-step or load arbitrary event chains.
- Inspect the agent's timeline and collapsed memory summary.
- Interact with Human-in-the-Loop review states.
- Preview messages across channels (WhatsApp, Email, Slack).
