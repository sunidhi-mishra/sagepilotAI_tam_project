# Phase-wise Implementation Plan: Order Supervisor UI Dashboard

This document details the step-by-step phases for implementing the Order Supervisor simulation dashboard. Each phase focuses on building a distinct part of the application under the `order-supervisor-ui/` directory.

## Rationale for Porting Simulation to TypeScript
To run the simulation dashboard, we recommend porting the Python logic from `order_supervisor.py` into browser-native TypeScript:
1. **Zero Network Latency & Serverless Architecture:** Running the engine client-side allows instant state updates, step-by-step execution playback, and direct user interaction inside the browser.
2. **Simplified Vercel Hosting:** Avoids the overhead of managing backend Python runtime environments, serverless endpoints, CORS configurations, and API serialization.
3. **Low Maintenance:** The simulation logic is self-contained and rule-based (~300 lines of standard Python), making a TS translation highly straightforward and robust.

---

## Phase 1: Project Setup and Infrastructure
* **Objective:** Establish the TypeScript codebase, runtime configurations, and the basic HTML container.
* **Tasks:**
  * Configure `tsconfig.app.json` and `tsconfig.node.json` for proper React + TypeScript compilation.
  * Create `index.html` with a clean container and load a modern typography typeface (e.g., Inter or Plus Jakarta Sans).
  * Setup a clean directory structure:
    ```
    src/
    ├── app/               # Main entrypoints & global styles
    ├── components/        # Bento-grid cards, timelines, tabs, review controls
    └── simulator/         # Ported simulation logic in TypeScript
    ```
  * **Deliverables:** A compilable project boilerplate.

---

## Phase 2: Simulation Engine Porting (TS)
* **Objective:** Translate the logic from `order_supervisor.py` into browser-compatible TypeScript.
* **Tasks:**
  * Implement `Event` and `TimelineEntry` interfaces.
  * Port `WakePolicy` and custom wake rules.
  * Port `Agent` decision trees and mock tools mapping to browser callbacks.
  * Port `OrderState` structure, including the **Memory Management** timeline compression (`_collapse_if_needed`).
  * Port `OrderSupervisor` runner class to process a sequence of events.
  * **Deliverables:** A tested, pure-JS/TS simulator engine that can run in a browser environment.

---

## Phase 3: Global Styling (CSS)
* **Objective:** Establish a premium design system matching the aesthetic guidelines.
* **Tasks:**
  * Write `src/app/globals.css` with CSS variables for:
    * Primary background (Pure White `#FFFFFF`, muted neutrals `#F8F9FA` / `#F9FAFB`).
    * Accent brand color (Vibrant Mint Green `#10B981` / `#059669`).
    * Typography sizes and weights using sans-serif fonts.
  * Define card structures with subtle border rules, rounded corners (8px–12px), and smooth hover transitions.
  * **Deliverables:** A global stylesheet with core design system variables and layout utilities.

---

## Phase 4: Core Components & Bento-Grid Layout
* **Objective:** Create the modular UI layout.
* **Tasks:**
  * Assemble the dashboard shell utilizing a responsive Bento-grid layout.
  * Implement the following widgets:
    * **Simulated Timeline Stream:** Feed showing event items and actions with state tags (Amber, Green, Blue).
    * **Multi-Channel Tabs:** UI tab controls (`←` and `→` arrows or circular outlines) switching between simulated WhatsApp bubble logs, Emails, or Logistics logs.
    * **Human-in-the-Loop Review Cards:** Actionable panels showing approval states, diff displays, and action buttons.
  * **Deliverables:** A fully structured, styled dashboard populated with mock data.

---

## Phase 5: Live Simulation Integration
* **Objective:** Bind the TypeScript simulator state to the React UI.
* **Tasks:**
  * Hook up input sliders or sample event triggers to run the simulation engine step-by-step.
  * Render real-time progress, showing the agent waking up, logging events, updating the collapsed memory summary, and modifying the timeline.
  * Integrate approval buttons to directly affect simulated agent decisions (e.g. approving a $2,600 refund request).
  * **Deliverables:** A fully interactive local testing dashboard.

---

## Phase 6: Vercel Deployment & Verification
* **Objective:** Deploy and verify the final application.
* **Tasks:**
  * Verify the static build command compiles perfectly without errors (`npm run build`).
  * Setup standard Vercel configuration files.
  * **Deliverables:** Live URL hosted on Vercel.
