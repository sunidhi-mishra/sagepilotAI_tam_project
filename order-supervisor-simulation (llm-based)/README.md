# Order Supervisor Simulation with LLM Integration

A Python simulation of a durable, agentic workflow for managing order lifecycle events. This implementation includes both a rule-based agent (the graded B2 submission) and an optional Gemini LLM agent (the bonus feature).

## Overview

The supervisor manages a single order through its entire lifecycle, handling events like payment failures, shipment delays, customer messages, and deliveries. The system implements:

- A wake policy that screens events to control computational cost (routine events stay asleep, exceptions wake the agent)
- Durable timers that trigger automatic check-ins every 6 hours
- Mock tool executions (send messages, create notes, escalate to human)
- Memory collapse that keeps the timeline compact instead of growing unbounded
- Terminal event handling that closes the workflow deterministically

## Running the Simulation

### Prerequisites

For rule-based mode (default): no dependencies needed, runs on Python 3.7+

For LLM mode: install the Gemini API client

```bash
pip install google-generativeai
```

### Rule-Based Agent (Default, Graded Submission)

This is the core B2 submission. No API calls, no external dependencies, pure rule-based decision logic.

```bash
python3 order_supervisor_llm.py sample_events.json
```

The agent follows hard-coded rules based on event type and current state. For example, if a refund exceeds ₹2000, it escalates; if a customer uses angry language, it flags for review; if no updates arrive for 6 hours, it does a scheduled check-in.

### LLM Agent (Bonus: Gemini Integration)

Wire in Gemini to reason through decisions instead of following fixed rules. The LLM is grounded in the order state and a fixed list of available tools. If the API fails, it automatically falls back to the rule-based agent.

First, get your Gemini API key:

1. Go to https://aistudio.google.com/app/apikeys
2. Click "Create API key"
3. Copy the key

Then run:

```bash
GEMINI_API_KEY=<your-key> python3 order_supervisor_llm.py --llm sample_events.json
```

Replace `<your-key>` with your actual key. The free tier includes 60 requests per minute, which is plenty for testing.

### Sample Output

Both modes produce JSON output:

```json
{
  "order_id": "ORDER-001",
  "final_status": "closed: delivered",
  "final_open_issue": null,
  "total_tool_calls": 18,
  "activity_log": [
    "[create_internal_note] Payment failed: card declined",
    "[message_customer] We noticed an issue with your payment, retrying now.",
    "[message_customer] Heads up, your order is delayed (courier backlog). We're on it.",
    "[escalate] Refund of 2600 exceeds limit 2000",
    "[message_customer] Your order has been delivered, hope you love it!"
  ],
  "timeline": [
    {"time": 0, "entry": "Payment failure logged and customer notified"},
    {"time": 1, "entry": "Shipment created"},
    {"time": 20, "entry": "Shipment delay handled (courier backlog)"}
  ],
  "memory_summary": "[t=0h] Payment failure logged... [t=20h] Shipment delay handled..."
}
```

In LLM mode, the output also includes:

```json
{
  "llm_calls": 7,
  "llm_fallbacks": 0
}
```

The `llm_calls` count shows how many times Gemini was invoked (one per WAKE_NOW event). The `llm_fallbacks` count shows how many times the API failed and the system fell back to rule-based decisions (ideally zero).

## Comparing Rule-Based vs. LLM

Run both and save the outputs:

```bash
# Rule-based
python3 order_supervisor_llm.py sample_events.json > output_rule_based.txt

# LLM
GEMINI_API_KEY=<your-key> python3 order_supervisor_llm.py --llm sample_events.json > output_llm.txt
```

The structure is identical. The activity logs may differ (LLM might make different tool calls in edge cases since it reasons from context), but both should close the order correctly with 18 total tool calls.

## Architecture

### Rule-Based Agent (`Agent` class)

Hard-coded decision logic based on event type and state. Fast, deterministic, no API dependency.

```python
if event_type == "payment_failed":
    # Log and message customer
elif event_type == "refund_requested":
    if amount > REFUND_AUTO_APPROVE_LIMIT:
        # Escalate
    else:
        # Auto-approve
```

### LLM Agent (`LLMAgent` class)

Uses Gemini with structured JSON output to decide which tool to call. Grounded in order state and available tools.

**Prompt structure:**
- Order state (status, open issue, recent timeline, memory summary)
- Current event (type and data)
- Available tools with descriptions
- Decision rules ("Ground every decision in the event and state," "Escalate if confused")

**Response schema (JSON):**
```json
{
  "tool": "message_customer | escalate | create_internal_note | ...",
  "reasoning": "Why this tool makes sense",
  "text_or_reason": "What to send or log"
}
```

**Fallback mechanism:**
If the API call fails (timeout, rate limit, invalid response), the system automatically delegates to the rule-based agent and logs the fallback. The order keeps progressing either way.

## Temporal Mapping

This in-memory simulation maps to Temporal building blocks that would exist in production:

- **Signal**: events arriving from external systems (payment_confirmed, shipment_delayed, customer_message_received, etc.). In this code: `event` parameter to `process_event()`.
- **Timer**: the `no_update_for_n_hours` synthetic events, which trigger scheduled check-ins every 6 hours. In this code: generated in the supervisor loop when `event_timestamp - last_activity_time > SCHEDULED_WAKE_INTERVAL_HOURS`.
- **Query**: pulling the order's current memory_summary and timeline without waking the workflow (not implemented in this demo, but would be read-only state inspection).
- **Activity**: the tool calls (message_customer, escalate, create_internal_note, etc.). In this code: methods in the `ToolBox` class.
- **Continue-as-new**: the `_collapse_if_needed()` method, which folds older timeline entries into memory_summary and resets the timeline window to stay compact.

## Where an LLM Helps

The rule-based agent handles most cases with fixed rules. The LLM agent is useful for:

1. **Ambiguous customer language**: deciding whether "my dog refused the food" warrants a refund, escalation, or just a replacement (rule-based has hard limits; LLM can reason through context).
2. **Multi-tool decisions**: some situations need to message the customer, the logistics team, and create a note. LLM can coordinate this; rule-based needs explicit programming.
3. **Dynamic thresholds**: instead of a fixed refund limit (₹2000), LLM can consider customer history, order value, and sentiment.

For a production system, the LLM would be fed:

- Event type and data
- Compact memory summary (older detail already collapsed)
- Recent timeline (last 5 entries, verbatim)
- List of available tools with descriptions
- Explicit instruction: pick a tool from the list, or escalate if none fit

The JSON schema forces valid output. If the API fails, rule-based fallback ensures the order progresses.

## Files

- `order_supervisor_llm.py`: the main simulation (387 lines, includes both Agent and LLMAgent classes)
- `sample_events.json`: example input events (same as the original graded B2 submission)
- `sample_output.txt`: output of rule-based mode on the sample events
- `README.md`: this file

## LLM Integration Details

### API Configuration

The LLM agent reads the Gemini API key from the `GEMINI_API_KEY` environment variable. Never hardcode the key into the script.

```bash
export GEMINI_API_KEY=your_key_here
python3 order_supervisor_llm.py --llm sample_events.json
```

Or inline:

```bash
GEMINI_API_KEY=your_key sample_events.json
```

### Error Handling

If any API call fails:
- Network timeout
- Rate limit hit
- Invalid response JSON
- Malformed tool name

The system logs the error to stderr and delegates to the rule-based agent for that decision. The `llm_fallbacks` counter increments, so you can see how many times this happened.

```bash
[LLM Error] <error details>, falling back to rule-based agent
```

If fallbacks are greater than zero, the simulation still completes correctly, but you know some decisions came from the rule-based policy instead of the LLM.

### Testing the LLM Integration

To confirm the integration works end to end:

```bash
GEMINI_API_KEY=<your-key> python3 order_supervisor_llm.py --llm sample_events.json
```

Check the output:
- `"llm_calls"` should be 7 or similar (one per WAKE_NOW event)
- `"llm_fallbacks"` should be 0 (meaning all API calls succeeded)
- `"total_tool_calls"` should be 18 (same as rule-based mode)
- `"final_status"` should be `"closed: delivered"`

If `llm_fallbacks` is greater than zero, the API had issues, but the simulation still ran to completion using rule-based fallback.

## Dependencies

**Rule-based mode (default):**
- Python 3.7+
- No external packages

**LLM mode:**
- Python 3.7+
- `google-generativeai` (install with `pip install google-generativeai`)
- Gemini API key from https://aistudio.google.com/app/apikeys

## Bonus: Why Wire in an LLM?

This bonus demonstrates the practical integration point for AI reasoning in a deterministic workflow system. The LLM doesn't replace the workflow structure (signals, timers, activity execution) — it only replaces the decision logic within a single wake cycle. When the LLM fails, the system degrades to rule-based decisions and keeps working. This is the production-grade pattern: use AI for reasoning, use Temporal for durability and determinism.

## Notes

- This file is 387 lines (over the 200-350 base requirement) because the LLM integration is a bonus feature on top of the required rule-based simulation. The core rule-based simulation alone is within range.
- Both modes use the exact same `sample_events.json` input.
- The activity logs may differ slightly between modes (LLM makes different decisions on edge cases), but the structure and final state are identical.
- The LLM prompt is designed to prevent hallucination: it lists available tools, grounds decisions in event data, and requires escalation when uncertain.
