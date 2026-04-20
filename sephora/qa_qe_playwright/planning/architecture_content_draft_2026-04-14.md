# Architecture Section Content Draft

**Purpose:** Standalone content document for Section 02 (Proposed Architecture) of the preliminary approach deliverable.
**Status:** Draft for Colin's review before integration into the HTML.
**Last Updated:** 2026-04-14

---

## Sources Synthesized

This content draws from:
- Set 01 research: Colin's full QE methodology presentation (deterministic-first, state graph, CI/CD integration, agent evaluation, multi-model, confidence scoring, observability, recursive coverage, framework as bottleneck, "system autonomy")
- Set 02 research: Visual QA project scope, technical approach (exploratory flows, structured playbooks, review agent layer, guardrails, traceability, Figma MCP, unified backend), engagement model
- Set 03 discussion: Configurable specificity, ecosystem framing, deterministic playbooks, production architecture, standard stack, human-in-the-loop

---

## Section 02: Proposed Architecture

### Lead Paragraph

BayOne recommends an architecture that is deterministic at its foundation, agentic where judgment is required, and configurable across the teams that use it. The platform is a single ecosystem, not four separate tools. Every consumer group draws from the same set of modular components, and the only thing that varies is how those components are configured for each team's workflow.

### The Architecture in Layers

The platform is organized in layers, each handling the part of the problem it is best suited for. The lower layers are deterministic and predictable. The upper layers introduce intelligence. This separation is deliberate: it means the foundation is reliable independent of AI performance, and the AI adds value without introducing risk into the critical path.

#### Layer 1: Deterministic Automation

Playwright drives all browser interaction. When the platform clicks a button, navigates a page, captures a screenshot, or compares two visual states, it does so deterministically. There is no AI interpretation in the action itself. Playwright handles desktop and mobile viewports, integrates natively with cross-browser testing infrastructure (BrowserStack when available), and is Microsoft-native, aligning with Sephora's Azure environment.

At this layer, the platform also maintains a map of the application under test: how different parts of the codebase relate to each other, which UI components depend on which code paths, and which visual tests are relevant to which changes. This mapping feeds into CI/CD integration so that when code changes ship, the platform automatically identifies which tests need to run rather than executing the entire suite or relying on manual test selection.

Docker containers provide isolated, reproducible execution environments for all test runs. Every test executes in a clean, known state. In production, this translates to Azure Container Apps with compute allocated based on actual demand.

#### Layer 2: Saved Playbooks and Structured Testing

Once an effective testing workflow has been discovered and validated, it is saved as a deterministic playbook: an exact, repeatable sequence of steps, assertions, and validation criteria. Playbooks do not require AI to execute. They are the platform's equivalent of recorded macros, except they are tied to the codebase.

Playbooks are mapped to specific features, UI components, and code paths. When a release ships or a code change merges, the platform knows which playbooks are affected and runs them automatically. If a feature changes intentionally, the associated playbooks can be updated or retired by the team. If nothing changed, the playbooks continue to execute as they always have. Tests do not break on deployment unless the underlying behavior genuinely changed.

This layer is where the platform delivers the bulk of its day-to-day value for QE and development teams. The accumulated library of validated playbooks grows over time, and each playbook represents a testing workflow that a human no longer needs to perform manually. The library is a compounding asset: the more playbooks exist, the more coverage the team has without additional effort.

#### Layer 3: Agentic Exploration and Discovery

AI operates at this layer. When the platform encounters a new feature, an unfamiliar application state, or a testing objective that no existing playbook covers, an agentic workflow takes over. The agent uses its tools (Playwright for browser interaction, visual comparison models for understanding what it sees, design file references for baseline comparison) to explore, discover anomalies, and construct new testing workflows.

Exploratory testing is the most visible agentic capability. An agent can navigate an application the way a new user would: visiting pages, interacting with elements, looking for visual inconsistencies, broken layouts, content errors, or accessibility issues. Every action is logged, every screenshot is captured, and the results are traceable to the specific environment state and code version.

When an agent discovers a workflow that successfully validates a testing objective, that workflow becomes a candidate for Layer 2: it can be validated by a human and saved as a deterministic playbook. This is the cycle that makes the platform self-improving. AI explores and discovers; validated discoveries become deterministic assets; the deterministic library grows; the need for exploration decreases over time for known areas while remaining available for new features and changes.

This layer also handles visual understanding tasks that require judgment rather than exact pixel matching. A button that moved slightly due to a layout change is not the same as a button that disappeared. A visual understanding model can distinguish between intentional design changes and genuine defects, reducing false positives that would otherwise require human triage.

#### Layer 4: Review and Confidence

Before any agent-generated result reaches a human, it passes through a review layer. A dedicated review agent evaluates the output for quality, relevance, and actionability. Results that are noise (false positives, known acceptable variations, duplicate findings) are filtered. Only findings that meet a quality threshold are surfaced to human reviewers.

This review layer serves all four consumer groups. For QE, it filters exploratory test results. For development teams, it filters Figma-to-rendered comparison results. For UI/UX, it provides the first stage of the threshold-based approval workflow. For the content production team, it filters content validation results.

Confidence scoring operates across the entire platform. Every agent maintains a track record built from human-validated outcomes. When a human approves an agent's finding, that approval reinforces the pattern. When a human rejects a finding, the rejection refines future behavior. Over time, agents that consistently produce high-quality results earn higher confidence scores, and the frequency of human review decreases for those agents and task types. Human involvement shifts from reviewing every result to reviewing exceptions, similar to the transition from hands-on testing to overseeing an automated operation.

Agents do not assess themselves or each other. Confidence scores are derived from human-validated outcomes and defined KPIs, not from agent self-evaluation. This is a deliberate design choice grounded in the observed behavior of agent self-assessment, which tends to oscillate between extreme optimism and extreme pessimism rather than producing calibrated judgments.

#### Layer 5: Observability

The platform provides full visibility into what is happening across all layers. Every action is traceable: which agent performed it, what tools it used, what environment it operated in, what code version was being tested, and what the outcome was. This traceability is the same standard applied to human QE teams.

Beyond individual action tracing, the platform surfaces aggregate data: agent performance trends, test pass rates over time, edge case patterns, confidence score trajectories, and playbook coverage metrics. This data is designed for QE leadership that is transitioning from hands-on execution to decision-making. The question shifts from "did the test pass?" to "is the testing system healthy, accurate, and improving?"

When the system is mature, the most interesting data is the edge cases. Are the remaining failures because the system is too strict? Because the test criteria are wrong? Because genuine defects are being found? This diagnostic capability helps the team continuously calibrate the platform to match real-world quality standards rather than theoretical ones.

### How Configuration Serves Four Consumer Groups

The layered architecture is the same for all consumer groups. What differs is configuration:

**Baseline reference.** QE compares current application state against prior state. Development teams compare rendered UI against design specifications (Figma or equivalent). UI/UX compares against defined component standards with configurable tolerance. Content production compares published content against expected content state. All four use the same visual comparison engine; the baseline input is the configuration variable.

**Tolerance and precision.** The UI/UX team may require pixel-level precision with explicit thresholds. QE exploratory testing operates with broader tolerance to focus on functional anomalies. Content validation focuses on whether the right content appears in the right place. Tolerance is a setting that can be adjusted per team, per test type, per component, or per page.

**Workflow integration.** QE receives test reports and anomaly logs integrated with their testing pipeline. Development teams receive feedback within their development workflow, triggered through CI/CD on code changes. UI/UX receives threshold-based alerts routed through an approval workflow for disposition decisions. Content production receives validation reports tied to their publishing pipeline. Each integration is a module on the shared backbone.

**Tool connectors.** Teams that work with Figma get a connector (via MCP) that allows the platform to reference design files as baselines. Teams that work with specific content management systems get connectors for their publishing tools. These connectors are additive: building one does not require rebuilding the core, and each new connector expands what the platform can do for all teams, not just the team that requested it.

### Deterministic Playbook Engine (Detail)

The playbook engine deserves specific attention because it is the mechanism through which the platform converts AI-discovered value into permanent, reliable automation.

**Discovery.** An agent is given a testing objective. It uses Playwright to interact with the application, visual comparison to validate what it sees, and design or content references as baselines. Through exploration, it finds a sequence of actions that validates the objective.

**Validation.** The discovered workflow is presented to a human reviewer. The reviewer can approve it as-is, modify it, or reject it. Approval converts the workflow into a saved playbook.

**Replay.** Saved playbooks execute deterministically. They do not require AI. They run the exact sequence of actions, capture the exact set of screenshots, and evaluate the exact assertions that were validated during discovery. They can run on any schedule (triggered by code changes, nightly, post-deploy, on-demand) and against any environment.

**Release mapping.** Playbooks are associated with the code, features, and UI components they validate. When a release ships, the platform identifies which playbooks are relevant and executes them. If a playbook fails because the underlying feature genuinely changed, the team can update the playbook or allow the agent to rediscover a new workflow. If a playbook fails for any other reason, that is a defect signal.

**Developer control.** Playbooks are assets owned by the teams, not by the AI. Teams can review the full sequence of actions in any playbook, edit steps, add assertions, adjust tolerances, or retire playbooks that are no longer relevant. The system makes testing easier without removing human governance over what is tested and how.

### Human-in-the-Loop as a Design Feature

Human involvement is not a limitation of the system. It is a feature that makes the system trustworthy. The reinforcement-based confidence model works as follows:

In the initial phase, humans validate all agent-generated results and all newly discovered workflows. This is the highest-effort phase. Each validated success builds the agent's track record. The track record accumulates over time. As the record grows, the threshold for mandatory human review decreases for specific agent/task combinations that have proven reliable.

The result is a system where human effort decreases naturally as trust is earned, not because a switch was flipped. The human role transitions from reviewing every result to overseeing the system's overall health, intervening on exceptions, and making course corrections when agents drift. This mirrors the broader organizational transition that QE leadership is already managing: from hands-on engineering to decision-making and oversight.

When a human does need to course-correct an agent, the correction is captured and feeds back into the system. The platform learns from corrections, not just from approvals. Agents that receive corrections in a specific area will be more cautious in that area going forward, and the confidence threshold for that task type may increase temporarily until the correction is validated.

---

## Notes for Integration

- This content replaces the entire "Proposed Architecture" section in the HTML
- The workflow-grid components from the draft (three-step playbook visual, three-step configuration visual) can be reused but should be redesigned to match this layered structure
- Consider whether the five layers should be visualized (stacked diagram, table, or sequential cards) or presented as prose with subheadings
- Progressive buildout content has been intentionally excluded; it belongs in Section 05 per the feedback
- Control panel content has been intentionally excluded; the web application is referenced in the stack table in Section 03
