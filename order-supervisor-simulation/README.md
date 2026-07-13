# Order Supervisor -- In-Memory Simulation

A small (~300-line) simulation of the order supervisor system described in
Part B of the assignment. No Temporal, no database, no cloud, no frontend --
a single Python file that reads an ordered list of order events and
replays the wake / reason / act / sleep loop in memory.

## How to run it

```bash
python3 order_supervisor.py sample_events.json
```

or via stdin:

```bash
cat sample_events.json | python3 order_supervisor.py
```

No dependencies beyond the Python 3 standard library.

### Sample output

Running `python3 order_supervisor.py sample_events.json` against the
included `sample_events.json` (a payment failure + retry, a shipment
delay, an angry customer message, an over-limit refund request, and a
delivery, with two multi-hour gaps to demonstrate scheduled wake-ups)
produces:

```
======================================================================
FINAL SUMMARY -- Order ORDER-DEMO-001
======================================================================
Status: closed:delivered

Actions taken (18 tool calls):
  - create_internal_note: {'order_id': 'ORDER-DEMO-001', 'note': 'Payment failed: card declined'}
  - message_customer: {'order_id': 'ORDER-DEMO-001', 'text': "We noticed an issue with your payment -- retrying now, we'll confirm shortly."}
  - create_internal_note: {'order_id': 'ORDER-DEMO-001', 'note': 'Scheduled check-in: nothing new, order on track'}
  - create_internal_note: {'order_id': 'ORDER-DEMO-001', 'note': 'Scheduled check-in: nothing new, order on track'}
  - create_internal_note: {'order_id': 'ORDER-DEMO-001', 'note': 'Scheduled check-in: nothing new, order on track'}
  - message_customer: {'order_id': 'ORDER-DEMO-001', 'text': "Heads up -- your order is delayed (courier backlog). We're on it and will update you."}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Delay reported (courier backlog) -- please confirm new ETA.'}
  - message_customer: {'order_id': 'ORDER-DEMO-001', 'text': 'Still tracking your delayed shipment -- latest update coming shortly.'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - mark_for_review: {'order_id': 'ORDER-DEMO-001', 'reason': "Escalation language detected: 'This is ridiculous, I want a refund or I'm filing a chargeback.'"}
  - message_customer: {'order_id': 'ORDER-DEMO-001', 'text': "I'm sorry for the frustration -- looping in a specialist to sort this out right away."}
  - escalate: {'order_id': 'ORDER-DEMO-001', 'reason': 'Refund of 2600 exceeds auto-approve limit of 2000.0'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - message_logistics_team: {'order_id': 'ORDER-DEMO-001', 'text': 'Checking in -- still no resolution on: shipment_delayed'}
  - message_customer: {'order_id': 'ORDER-DEMO-001', 'text': 'Your order has been delivered -- hope you love it!'}

Rolling memory summary (collapsed older detail):
  [t=0.0h] payment_failed -> WAKE_NOW [t=0.0h] Logged payment failure and reassured
  customer [t=0.5h] payment_confirmed -> STAY_ASLEEP [t=1.0h] shipment_created ->
  STAY_ASLEEP [t=7.0h] no_update_for_n_hours (scheduled) -> WAKE_NOW [t=7.0h] Scheduled
  check-in: no action needed [t=13.0h] no_update_for_n_hours (scheduled) -> WAKE_NOW
  [t=13.0h] Scheduled check-in: no action needed [t=19.0h] no_update_for_n_hours
  (scheduled) -> WAKE_NOW [t=19.0h] Scheduled check-in: no action needed [t=20.0h]
  shipment_delayed -> WAKE_NOW [t=20.0h] Notified customer of delay and pinged
  logistics for new ETA [t=22.0h] customer_message_received -> WAKE_NOW [t=22.0h]
  Replied to customer re: known open delay [t=28.0h] no_update_for_n_hours (scheduled)
  -> WAKE_NOW [t=28.0h] Scheduled check-in: chased unresolved issue (shipment_delayed)
  ... (continues, collapsing every entry older than the most recent 5)

Recent timeline (last 5 entries kept verbatim):
  [t=59.0h] (action) Scheduled check-in: chased unresolved issue (shipment_delayed)
  [t=65.0h] (event) no_update_for_n_hours (scheduled) -> WAKE_NOW
  [t=65.0h] (action) Scheduled check-in: chased unresolved issue (shipment_delayed)
  [t=70.0h] (event) delivered -> WAKE_NOW
  [t=70.0h] (action) Sent delivery confirmation to customer

Learnings:
  - No unresolved issues flagged at close.
  - 18 tool calls made across the run.
  - 1 escalation(s) to a human.
======================================================================
```

(Full untruncated output, exactly as produced, is in `sample_output.txt`.)

This single run exercises all five mock tools (`message_customer`,
`message_logistics_team`, `create_internal_note`, `escalate`,
`mark_for_review`), both wake-policy outcomes (`payment_confirmed` and
`shipment_created` are the only `STAY_ASLEEP` types), multiple
self-triggered scheduled wake-ups during the two multi-hour gaps in the
input, memory collapsing (the timeline holds 20+ entries by the end but
only the last 5 are kept verbatim -- everything older is folded into
`memory_summary`), and a terminal stop on `delivered`.

## Design decisions worth flagging

- **`no_update_for_n_hours` is generated internally, not read from the
  input JSON.** Requirement 3 asks for a supervisor that "wakes on its
  own after a set interval," so the simulator injects this signal
  whenever the gap since the last processed event exceeds
  `SCHEDULED_WAKE_INTERVAL_HOURS` (6, configurable at the top of the
  file) -- it isn't something an external system pushes in.
- **If the order is still open after all input events are consumed**,
  the simulator fires a bounded number of additional scheduled wakes
  (`MAX_TRAILING_SCHEDULED_WAKES = 3`) so a finite demo run terminates
  cleanly. A real Temporal workflow would just keep sleeping and waking
  indefinitely; this cap exists only because this is a one-shot script,
  not a long-running process.
- **The wake policy is a two-bucket rule table**, not per-event scoring:
  `payment_confirmed` and `shipment_created` are routine, "as expected"
  events that get logged to the timeline but never wake the agent;
  everything else does. This is a deliberately simple, defensible rule
  set -- not a claim that it's the optimal policy for production.
- **Escalation / review triggers are keyword-based** (refund amount
  above a fixed limit; a short list of angry-language keywords in a
  customer message). This is explicitly a rule-based stand-in for the
  reasoning step -- see the LLM section below.

## Mapping to Temporal building blocks

| In this simulation | Temporal building block in production |
|---|---|
| `OrderSupervisor.run()`'s main loop, one instance per order | **Workflow** -- one long-running Workflow Execution per order, holding state for the life of the order |
| Items in `sample_events.json` fed into `_handle_event()` | **Signal** -- each external event (`payment_confirmed`, `shipment_delayed`, `customer_message_received`, etc.) arrives as a Signal to the running Workflow |
| The internally-generated `no_update_for_n_hours` event, fired when the gap since `last_activity_time` exceeds `SCHEDULED_WAKE_INTERVAL_HOURS` | **Timer** (durable sleep) -- `workflow.sleep()` / a Temporal Timer that survives worker restarts, firing the equivalent of `no_update_for_n_hours` |
| Nothing implemented in this script (see note below) | **Query** -- a read-only, synchronous way to inspect `OrderState` (current status, open issue, memory summary) from outside without sending a Signal or waking the agent. Not needed for a one-shot in-memory run, but a real Workflow would expose one so a support agent could pull up "what does the supervisor currently think is going on with order #4821" without disturbing it. |
| `ToolBox` methods (`message_customer`, `message_logistics_team`, `create_internal_note`, `escalate`, `mark_for_review`) | **Activity** -- each tool call is a Temporal Activity: executed outside the Workflow's deterministic code, independently retried on failure, with its own timeout policy |
| `OrderState._collapse_if_needed()` folding old timeline entries into `memory_summary` | **Continue-as-new** -- the in-memory analogue of the same problem: a Workflow's event history grows with every Signal/Timer/Activity and needs to be reset periodically (carrying forward only the compact summary) to avoid hitting history-size limits and degrading replay performance |
| `WakePolicy.decide()` | Logic inside the Workflow's Signal handler, run synchronously before deciding whether to invoke the (potentially expensive) reasoning step -- not a distinct Temporal primitive on its own, but the pattern of "cheap gate before expensive work" that keeps Activity/LLM-call volume down |
| The `TERMINAL_EVENT_TYPES` check inside `_handle_event()`, ending `run()` | The Workflow's own completion condition -- the Workflow function returning, not any tool or Activity deciding to stop (see B1.4: termination is never the agent's call) |

## Where an LLM would improve the decision, and what I'd feed it

The **only** piece of this simulation designed to be swapped for an LLM
is `Agent.decide_and_act()` -- the reasoning step that runs after
`WakePolicy` says `WAKE_NOW`. Everything else (the wake policy gate,
state/timeline management, timers, and especially termination) should
stay deterministic and rule-based even in production, consistent with
the B1.4 answer on why the workflow -- not the agent -- must decide when
a run ends.

Two places inside `decide_and_act()` are the clearest candidates:

1. **`customer_message_received` handling.** Right now this is a
   keyword list (`"angry"`, `"chargeback"`, `"lawyer"`, `"scam"`) --
   trivially bypassed by real customer language ("I'm really not happy
   about this" triggers nothing; "scammy" triggers a false positive).
   An LLM call here, given the customer's message, the order's current
   `memory_summary`, and the current `open_issue`, could produce a more
   reliable action decision (reply directly / escalate / mark for
   review) and a properly personalized reply, instead of a fixed
   canned string.

   *What I'd feed it:* the raw message text, the compact memory summary
   (not the full raw timeline -- that's the point of collapsing it),
   the current `open_issue` flag, and the brand's policy text (refund
   window, tone guidelines) as system context. Output: a structured
   decision (`action: reply | escalate | mark_for_review`, plus the
   reply text if applicable) -- not free-form prose, so the workflow
   code can still deterministically route the result to the right tool
   call.

2. **`refund_requested` handling.** The auto-approve threshold here is
   a flat number (`refund_auto_approve_limit`). A real policy usually
   has more nuance -- order age, whether the item was opened, prior
   refund history for this customer -- and an LLM could weigh those
   factors and produce a recommended action, while the hard
   auto-approve/escalate boundary (the actual money-movement gate)
   stays a deterministic check in the workflow, not something the LLM
   decides unilaterally. This mirrors Sagepilot's own tiered
   auto/read-only/needs-approval model from Part A.



## Files

- `order_supervisor.py` -- the simulation (~300 lines)
- `sample_events.json` -- example input covering every event type in the spec
- `sample_output.txt` -- full, unedited output from running the sample above
