# Sagepilot AI - Technical Account Manager Assignment

This repository contains my submission for the Technical Account Manager assignment at Sagepilot AI. It covers all five parts of the assignment (Product and Market, The System You Will Support, Onboarding, Success/Retention/Upsell, and Judgment Under Pressure), along with the code deliverable for Part B2, submitted in two versions.

## Written answers

All written answers (Parts A, B1, B3, C, D, and E) are in this Google Doc:

**[Sagepilot Assignment Submission - Sunidhi Mishra](https://docs.google.com/document/d/1tYitF7L10nFSDp_GaL1b78NOMEYfk2yjYOy2s6_Zovw/edit?usp=sharing)**

The document is organized by part, with each question followed directly by its answer, matching the structure of the original assignment brief.

## Part B2: Order Supervisor Simulation

Part B2 asked for a small, in-memory simulation of the order supervisor system described in Part B, with no Temporal, database, cloud, or frontend involved. That's the graded requirement, and it's fully met by the rule-based version below. A second, LLM-based version is included as well, covering the BONUS item in the brief ("wire in a real LLM for the decision step").

### `order-supervisor-simulation (rule-based)`

This is the core graded submission. A fixed set of rules decides what to do at each wake-up, no external API calls, no dependencies beyond Python itself.

**Folder contents:**
- `order_supervisor.py`, the simulation itself
- `README.md`, with instructions on how to run it, sample output, a mapping of each part of the build to its Temporal equivalent (signal, timer, query, activity, continue-as-new), and notes on where an LLM could improve the decision step
- `sample_events.json`, example input covering every event type in the assignment
- `sample_output.txt`, the actual output produced by running the simulation on that sample input

To run it:

```bash
cd "order-supervisor-simulation (rule-based)"
python3 order_supervisor.py sample_events.json
```

### `order-supervisor-simulation (llm-based)`

Same simulation, same event handling, same wake policy and memory collapse logic, but the decision step at each wake-up is made by a real LLM instead of fixed rules, with an automatic fallback to the rule-based logic if the API call fails or returns something invalid.

**Folder contents:**
- The LLM-integrated simulation code
- `README.md`, with setup instructions, how to get an API key, how to run both modes side by side, and what a successful run looks like
- The same `sample_events.json` used by the rule-based version, so both can be tested against identical input
- Sample output showing the LLM-driven run, including call counts and fallback counts

To run it, see that folder's own `README.md` for exact setup steps (an API key is required).

### Why two folders instead of one

The assignment's base requirement is explicitly rule-based, in-memory, and dependency-free. Wiring in a real LLM is called out separately as a bonus. Keeping them in separate folders means the graded submission stands on its own, exactly as specified, while the bonus work is clearly additional rather than folded into (and potentially confused with) the required deliverable.

## Repository structure

```
.
├── README.md                                          (this file)
├── Sagepilot Assignment Submission - Sunidhi Mishra    (exported copy of the written answers)
├── order-supervisor-simulation (rule-based)/
│   ├── order_supervisor.py
│   ├── README.md
│   ├── sample_events.json
│   └── sample_output.txt
└── order-supervisor-simulation (llm-based)/
    ├── order_supervisor_llm.py
    ├── README.md
    ├── sample_events.json
    └── sample_output.txt (or equivalent LLM-run output)
```