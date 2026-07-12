# Sagepilot AI - Technical Account Manager Assignment

This repository contains my submission for the Technical Account Manager assignment at Sagepilot AI. It covers all five parts of the assignment (Product and Market, The System You Will Support, Onboarding, Success/Retention/Upsell, and Judgment Under Pressure), along with the code deliverable for Part B2.

## Written answers

All written answers (Parts A, B1, B3, C, D, and E) are in this Google Doc:

**[Sagepilot Assignment Submission - Sunidhi Mishra](https://docs.google.com/document/d/1tYitF7L10nFSDp_GaL1b78NOMEYfk2yjYOy2s6_Zovw/edit?usp=sharing)**

The document is organized by part, with each question followed directly by its answer, matching the structure of the original assignment brief.

## Part B2: Order Supervisor Simulation

Part B2 asked for a small, in-memory simulation of the order supervisor system described in Part B, with no Temporal, database, cloud, or frontend involved. That code lives in the `order-supervisor-simulation` folder in this repo.

**Folder contents:**
- `order_supervisor.py`, the simulation itself
- `README.md`, with instructions on how to run it, sample output, a mapping of each part of the build to its Temporal equivalent (signal, timer, query, activity, continue-as-new), and notes on where an LLM could improve the decision step
- `sample_events.json`, example input covering every event type in the assignment
- `sample_output.txt`, the actual output produced by running the simulation on that sample input

To run it:

```bash
cd order-supervisor-simulation
python3 order_supervisor.py sample_events.json
```

Full details, including sample output and the Temporal mapping, are in that folder's own `README.md`.

## Repository structure

```
.
├── README.md                                    (this file)
├── Sagepilot Assignment Submission - Sunidhi Mishra   (exported copy of the written answers)
└── order-supervisor-simulation/
    ├── order_supervisor.py
    ├── README.md
    ├── sample_events.json
    └── sample_output.txt
```