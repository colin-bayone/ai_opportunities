# An Agentic Platform for Quality Engineering

**Prepared For:** Sephora
**Prepared By:** BayOne Solutions
**Date:** April 2026
**Status:** Preliminary

---

## Contents

1. Problem Summary
2. Proposed Architecture
3. Technical Foundation
4. Engagement Models
5. Implementation Pathway
6. Preliminary Framing

---

## 01 — Problem Summary

As quality engineering organizations mature and accelerate their adoption of AI across the software development lifecycle, visual quality assurance consistently emerges as one of the most difficult capabilities to automate effectively. The challenge is common across industries: visual validation remains manual, time-intensive, and difficult to scale alongside the velocity of modern development practices.

The following represents BayOne's understanding based on conversations to date. This understanding may not yet reflect the full picture and will continue to be refined through deeper discussion with the team.

Sephora's QE organization has adopted an AI-first mandate across the SDLC and is transitioning to the Agentic Micro Pod (AMP) model: lean two-to-three person teams delivering small, frequent enhancements in a continuous development cycle. This model structurally eliminates the ability to batch or defer testing. Quality engineering must operate at the same pace as development, validating each increment as it ships rather than catching up after the fact. The organization has already demonstrated this velocity, delivering Q3 2026 roadmap objectives by March. Visual quality engineering is the next capability needed to sustain that pace.

A mid-2026 delivery target has been identified for addressing this gap, and four distinct teams have been identified as consumers of visual quality engineering, each with requirements that overlap significantly but differ in specificity and workflow integration.

### Quality Engineering

The QE team requires the broadest capability: exploratory testing to discover visual anomalies, structured regression testing, localization and translation verification, accessibility compliance validation, and content validation across the site.

The organization has completed proof-of-concept work on Playwright and is actively migrating from Selenium for new automation development. The gap is not in the team's understanding of what needs to be tested, but in the tooling and automation infrastructure to execute visual QE at the speed the AMP model demands.

This team's achievement in accelerating the 2026 roadmap establishes a strong foundation. Closing the visual QE gap is the next step in maintaining velocity parity with development across all testing dimensions.

### Development Teams

Development teams need visual validation during development, not after. The use case is comparing in-progress work against design specifications (Figma or equivalent UX design files) to verify that implementation tracks the intended design before the work reaches formal QE review.

This is a shift-left capability. Rather than discovering design drift during testing, development teams catch it during implementation. The integration point differs from QE: developers need something accessible within their existing workflow, triggered naturally through CI/CD on code changes.

### UI/UX Team

The UI/UX team requires the most granular level of visual control. This team partners closely with the business organization and needs the ability to configure pixel-level differential thresholds, define and maintain baseline component standards, and route visual discrepancies through an approval workflow when deviations exceed configured tolerances.

The UI/UX use case is governance-oriented. Where QE validates broadly and development self-checks, the UI/UX team defines and enforces the visual standards the organization holds itself to.

### Producers and Digital Content

The content production team creates and publishes product items, static content, images, and promotional materials. The current validation process is entirely manual, performed in the staging environment, with minimal validation in production after content is promoted.

This group has clear, well-defined validation needs and represents a strong candidate for demonstrating early platform value with relatively contained scope.

### Common Requirements Across All Four Groups

All teams need visual quality engineering that operates across two distinct environments with different purposes. The nonprod preview environment, where A/B testing is conducted, serves as the pre-release validation layer. The platform must account for the reality that pages in this environment may render different variants, and comparison logic must accommodate variant-aware validation to avoid false positives. The production environment serves a different function: autonomous anomaly detection after release, where agents monitor the live site for visual regressions, content errors, and unexpected changes without interfering with the production experience.

Cross-device and cross-browser testing is a requirement across the board, supported by a BrowserStack enterprise license currently being procured. Localization and translation testing was identified as a cross-cutting gap applicable to multiple consumer groups, and the platform architecture is designed to support it as a configurable testing dimension available to any team.

---

## 02 — Proposed Architecture

BayOne recommends an architecture that is deterministic at its foundation, agentic where judgment is required, and configurable across the teams that use it. The platform is a single ecosystem designed for long-term ownership and personalization, built from modular components that the organization can understand, maintain, and extend independently.

### Layered Architecture

The platform is organized in layers, each handling the part of the problem it is best suited for. The lower layers are deterministic and predictable. The upper layers introduce intelligence. This separation means the foundation operates reliably independent of AI performance, and the AI layer adds capability without introducing variability into the critical path. When performance plateaus, the constraint is typically in the framework and the deterministic foundation, not in the AI models. Investing in framework quality yields more than investing in better models.

[Architecture Diagram: Five layers from Deterministic Automation through Observability, with a Configuration Layer spanning all]

#### Layer 1: Deterministic Automation

Playwright drives all browser interaction. When the platform clicks a button, navigates a page, captures a screenshot, or compares two visual states, it does so deterministically. There is no AI interpretation in the action itself. Playwright handles desktop and mobile viewports, integrates natively with cross-browser testing infrastructure, and is Microsoft-native, aligning with the existing Azure environment.

At this layer, the platform also maintains a deterministic map of the application under test: how different parts of the codebase relate to each other, which UI components depend on which code paths, and which visual tests are relevant to which changes. This mapping extends beyond surface-level file associations to recursive downstream dependencies, so that a change in one module triggers tests for everything that module affects, not just the module itself. This feeds directly into CI/CD integration: when code changes ship, the platform automatically identifies which tests to run rather than executing the entire suite or relying on manual test selection.

All test execution occurs in isolated environments. Docker containers provide clean, reproducible execution states for development and testing. In production, this translates to Azure Container Apps with compute allocated based on actual demand.

#### Layer 2: Saved Playbooks and Structured Testing

Once an effective testing workflow has been discovered and validated, it is saved as a deterministic playbook: an exact, repeatable sequence of steps, assertions, and validation criteria. Playbooks do not require AI to execute. They are the platform's equivalent of recorded automation workflows, except they are tied to the codebase and mapped to specific features, UI components, and code paths.

When a release ships or a code change merges, the platform knows which playbooks are affected and runs them automatically. If a feature changes intentionally, the associated playbooks can be updated or retired by the team. Tests do not break on deployment unless the underlying behavior genuinely changed.

Scheduled execution through a workflow orchestration layer (Apache Airflow) handles nightly regression suites, post-deploy validation sweeps, and periodic production monitoring. CI/CD integration through GitHub Actions handles event-driven test triggers on code changes, giving development teams a seamless experience within their existing workflow.

The accumulated playbook library grows over time and represents a compounding asset: each validated playbook is a testing workflow that no longer requires manual execution.

#### Layer 3: Agentic Exploration and Discovery

When the platform encounters a new feature, an unfamiliar application state, or a testing objective that no existing playbook covers, an agentic workflow takes over. The agent uses its tools (Playwright for browser interaction, visual comparison models for understanding what it sees, design file references for baseline comparison) to explore, discover anomalies, and construct new testing workflows.

Exploratory testing is the most visible agentic capability. An agent navigates the application as a user would: visiting pages, interacting with elements, identifying visual inconsistencies, broken layouts, content errors, or accessibility issues. Every action is logged, every screenshot is captured, and the results are traceable to the specific environment state and code version.

Visual understanding models distinguish between intentional design changes and genuine defects. A button that moved slightly due to a layout adjustment is not the same as a button that disappeared. This contextual judgment reduces false positives that would otherwise require human triage. At scale, automated visual consistency exceeds what human reviewers can maintain, particularly across large volumes of pages, variants, and devices where attention fatigue degrades accuracy.

When an agent discovers a workflow that successfully validates a testing objective, that workflow becomes a candidate for Layer 2. Once validated by a human reviewer, it is saved as a deterministic playbook. This cycle is what makes the platform self-improving: AI explores and discovers, validated discoveries become deterministic assets, the deterministic library grows, and the need for exploration decreases over time for known areas while remaining available for new features and changes.

**Guardrails and production safety:** Agents operating in production are restricted to non-destructive actions. They can observe, capture, compare, and report, but they cannot modify data, submit forms, or alter application state. This restriction is enforced at the tool access level, not through behavioral instructions. In sandbox environments, destructive actions can be explicitly enabled for testing scenarios that require interaction. The platform adapts its permission model based on the environment it is operating in.

#### Layer 4: Review and Confidence

Before any agent-generated result reaches a human, it passes through a review layer. A dedicated review agent evaluates the output for quality, relevance, and actionability. Results that are noise (false positives, known acceptable variations, duplicate findings) are filtered. Only findings that meet a quality threshold are surfaced to human reviewers.

Confidence scoring operates across the entire platform. Every agent maintains a track record built from human-validated outcomes. When a human approves an agent's finding, that approval reinforces the pattern and lowers the threshold for future human review of similar findings. When a human rejects a finding or corrects an agent, the correction feeds back to make the agent more cautious in that specific area, and the confidence threshold for that task type increases temporarily until the correction is validated through subsequent successful runs. This bidirectional feedback (approvals lower thresholds, corrections raise them) ensures the system calibrates itself to real-world accuracy standards.

Agents do not assess themselves or each other. Confidence scores are derived from human-validated outcomes and defined performance indicators, not from agent self-evaluation. This is a deliberate design choice: agent self-assessment tends to oscillate between extreme optimism and extreme pessimism rather than producing calibrated judgments. Human expertise remains structurally necessary for course corrections.

#### Layer 5: Observability

The platform provides full visibility into what is happening across all layers. Every action is traceable: which agent performed it, what tools it used, what environment it operated in, what code version was being tested, and what the outcome was. This traceability is the same standard applied to human QE teams and provides the audit trail that enterprise quality engineering requires.

Beyond individual action tracing, the platform surfaces aggregate data: agent performance trends, test pass rates over time, edge case patterns, confidence score trajectories, and playbook coverage metrics. When the system is mature, the most interesting data is the edge cases. Are remaining failures because the system is too strict? Because the test criteria need updating? Because genuine defects are being found? This diagnostic capability helps the team continuously calibrate the platform against real-world quality standards.

When tests miss something, those edge cases are captured and fed back into the system as patterns to watch for in the future, even in situations that are not identical to the original miss. This learning loop expands the platform's awareness over time, complementing the confidence scoring mechanism that operates at the individual agent level.

This observability layer is designed for the organizational transition already underway: QE leadership moving from hands-on engineering to decision-making and oversight. The platform provides the evidence base needed to manage automated testing operations with confidence.

### Configuration Across Consumer Groups

The layered architecture is the same for all consumer groups. What differs is configuration across four dimensions: baseline reference, tolerance and precision, workflow integration, and tool connectors.

Tool connectors extend the platform's reach without modifying the core. Connectors for Figma, Canva, WordPress, and other tools are available via Model Context Protocol (MCP), and additional connectors can be built as needed. Each new connector expands what the platform can do for all teams.

### Unified Platform Hub

The platform provides a centralized interface where all teams and leadership have unified visibility into test status, playbook management, configuration settings, and performance metrics without navigating multiple applications. This hub consolidates what would otherwise require separate custom tools for each consumer group, reducing technical debt and ensuring that every team operates from the same data. The hub integrates with existing code repositories and single sign-on infrastructure, scoped to each user's role and responsibilities.

**System autonomy, not autonomous systems:** The platform is a system of coordinated components (deterministic processes, agentic capabilities, human oversight, and observability) that collectively achieves autonomous behavior while remaining fully traceable and governable. No single agent operates independently or without oversight. The autonomy is a property of the system's design, not of any individual component within it.

### Deterministic Playbook Engine

1. AI Exploration: An agent explores a testing objective using browser automation, visual comparison, and design file references.
2. Validation and Save: Once a workflow succeeds and is validated by a human reviewer, it is saved as a deterministic playbook.
3. Deterministic Replay: Saved playbooks run without AI, on any schedule, against any environment, mapped to code changes and releases.

Playbooks are assets owned by the teams. Teams can review, edit, extend, or retire playbooks. The platform makes testing more efficient without removing human governance.

### Human-in-the-Loop as a Design Feature

Human involvement is a design feature that makes the system trustworthy, not a limitation to be minimized. In the initial phase, human reviewers validate all agent-generated results and newly discovered workflows. Each validated success builds the agent's track record. As the record grows, the threshold for mandatory human review decreases for specific agent and task combinations that have proven reliable.

The result is a system where human effort decreases naturally as trust is earned. The human role transitions from reviewing every result to overseeing the system's overall health, intervening on exceptions, and making course corrections when agents drift.

---

## 03 — Technical Foundation

BayOne builds with the same tools it uses internally for its own quality engineering practice. The recommended stack is deliberately conservative: battle-tested frameworks that have reached production maturity, are extensible, and are maintainable by the team that will eventually own the system. Every component in the stack has crossed the threshold from experimental to production-grade.

### Core Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Browser automation | Playwright | Visual testing, UI interaction, screenshot capture, cross-device/browser. Microsoft-native. |
| Agent orchestration | LangGraph | Multi-agent workflows, state management, tool routing. |
| Model hosting | Azure AI Foundry | LLM inference and visual understanding, enterprise-grade. |
| Workflow orchestration | Apache Airflow | Scheduling test suites at scale. |
| CI/CD integration | GitHub Actions | Event-driven test triggering on code changes. |
| Web application | Django or FastAPI | Unified platform hub, SSO, reporting. Python-native. |

The platform's modular architecture natively supports Model Context Protocol (MCP) integration, consistent with the organizational requirement that all new tooling integrates seamlessly into existing workflows through MCP servers.

### Deterministic-First Design

The platform follows a deterministic-first design principle. Deterministic processes handle everything they can handle reliably. AI is layered on top for work that requires judgment. This layering keeps the reliability floor high.

**Multi-model strategy:** Visual quality engineering benefits from selecting models based on what each does best. General reasoning and test orchestration use one model family; visual understanding and pixel-level comparison may use another. This flexibility is managed within the platform and is transparent to end users.

### Traceability and Observability

Every action the platform takes is logged with full traceability. Observability extends to the agent layer, surfacing performance data that supports decision-making and oversight.

### Production Infrastructure

| Component | Service | Characteristics |
|-----------|---------|----------------|
| Application hosting | Azure Container Apps | Pay-by-usage, automatic scaling |
| Database | Azure PostgreSQL | Flexible to accommodate alternatives |
| Model inference | Azure AI Foundry | Managed hosting, enterprise security |
| Caching | Azure Redis | Available as needed |

**Cost management:** Pay-by-usage model. Containers scale automatically based on demand. No fixed infrastructure commitment. Production-grade from day one.

---

## 04 — Engagement Models

BayOne offers three engagement models. The first two are structured around outcomes, milestones, and deliverables.

### Fully Managed Delivery (Recommended)

BayOne receives a defined scope and delivers the solution end-to-end. The team works closely with stakeholders for requirements, feedback, and validation, but BayOne owns the execution, the methodology, and the quality of the deliverables. Pricing is tied to defined deliverables and milestones.

### Variable Collaborative Delivery (Recommended)

BayOne leads the engagement while the internal team participates at a level that matches organizational goals: reducing cost through shared effort, building internal capability, or accelerating delivery. The split is flexible and adjustable. Pricing adjusts accordingly.

This model is well-suited to the structure discussed with the QE Center of Excellence team: BayOne builds the solution while the COE team shadows the work, provides governance and integration input, receives hands-on training, and builds the expertise to own maintenance and future extensions after the engagement concludes.

### Staff Augmentation

BayOne provides qualified personnel who work under the organization's direction. BayOne does not recommend this model for this engagement. It is available if staffing support is needed for other initiatives.

---

## 05 — Implementation Pathway

The unified platform architecture supports multiple sequencing strategies and does not require a single large-scale deployment. The backbone is built once and extended incrementally.

### Progressive Buildout

The platform can start with one consumer group, validate the approach, and expand to the remaining three on the same foundation. The first phase is the most effort-intensive because the foundation is being built. Subsequent phases benefit from shared infrastructure, established patterns, and a growing playbook library.

### Starting Points

**Rapid Validation:** Content production (entirely manual today, well-understood workflow, contained scope).

**Broadest Value:** QE or UI/UX (widest foundation, may make more chronological sense as other groups depend on capabilities introduced here). A firm recommendation requires deeper discussion with the team.

### Parallel Execution

Feasible but carries trade-offs in complexity, focus, and resources. Recommended only with a well-defined plan and clear requirements for each group.

### Future Considerations

The platform's architecture is extensible beyond visual quality engineering. The same framework could support broader quality initiatives across the SDLC. The knowledge generated (codebase maps, playbook libraries, traceability data) could complement the organization's initiative to establish a unified knowledge base across functions.

---

## 06 — Preliminary Framing

This document represents BayOne's initial thinking based on the conversations to date. The architecture and recommendations are informed by experience building similar solutions across multiple industries and by BayOne's own internal use of these same tools and methodologies.

These ideas are intended as a starting point for discussion, not a specification. They will require refinement through deeper discovery with the technical team.

### Requirements for Refinement

- A working session with the QE Center of Excellence team
- Specific requirements for each consumer group
- Access to representative environments, including A/B test variant behavior
- Clarity on BrowserStack enterprise license timeline
- Preferences on engagement model and sequencing

### Continued Partnership

BayOne is prepared to move into a detailed requirements session at the team's convenience and welcomes the opportunity to refine this approach into a comprehensive engagement plan. The platform described in this document is designed as a long-term asset that grows with the organization.

---

### Organizational AI Portal

BayOne has experience building internal AI platforms and is available to collaborate on the organization's AI portal initiative if there is interest. This is a separate offering from the quality engineering platform and can be discussed independently.

---

**BayOne Solutions**
Confidential, Prepared for Sephora
