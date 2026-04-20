# 03 - Discussion: System Architecture and Design Principles

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-14 (Pre-proposal strategy discussion)
**Document Set:** 03 (Working Discussion)
**Pass:** Colin's architectural direction for the visual QA platform

---

## Core Framing Correction: Configurability, Not Separate Tools

The four consumer groups do not get four different tools, and no single group's needs should be positioned as cascading down to the others. The system is one platform with configurable settings. What varies across consumer groups is only the degree of specificity or customization, and that is a configuration choice, not a structural difference.

The framing in the document should be: common needs across all four groups, with the only variation being how specific or general the user wants the system to behave. Ultra hyper-specific (pixel-level thresholds for UI/UX)? Configurable. More general (exploratory testing for QE)? Also configurable. On demand. This is not four tools or four modules; it is one system with a settings layer.

## Standard Stack: Battle-Tested, Extensible, Maintainable

Colin's stack philosophy is to build with tools that are standard, extensible, maintainable, understandable by Sephora's teams, and based on scalable patterns. No exotic platforms, no vendor lock-in, no learning curves that create dependency on BayOne.

### Core Stack

| Layer | Technology | Role |
|-------|-----------|------|
| Model hosting | Microsoft Azure AI Foundry | LLM inference, visual understanding models, enterprise-grade hosting |
| Agent orchestration | LangGraph | Multi-agent workflows, state management, tool routing |
| Browser automation | Playwright | Visual testing, UI interaction, screenshot capture, cross-device/browser |
| Workflow orchestration | Apache Airflow | Scheduling and orchestrating test runs at scale |
| CI/CD integration | GitHub Actions | Triggering tests on code changes, developer-facing automation |
| Isolated execution | Docker containers | Running tests in isolated environments, reproducible test conditions |
| Web interface | Django or FastAPI (Python) | Control panel, user management, repository integration, SSO |

### Why Python Frameworks for the Web Layer

Colin specifically identified Python as the preferred backend language for the control panel. The reasoning is direct compatibility: the agentic libraries that power the system (LangGraph, LangChain, Playwright's Python bindings, Azure SDK) are all Python-native. Using a Python web framework means the backend, the agent orchestration, and the tool integrations all share a single language and runtime, making integration simple and reliable. There is no translation layer between the web application and the agent infrastructure.

If Sephora has a strong preference for a different platform, BayOne can adapt, but the Python recommendation is grounded in practical integration, not personal preference.

## Deterministic Playbook Concept

One of the most important design ideas: AI discovers effective testing workflows, and once they work, they are saved as deterministic, replayable playbooks. Colin compared this to recording an Excel macro.

### How It Works

1. **AI explores and discovers.** An agent is given a testing objective (e.g., "verify that new product items render correctly on the product detail page"). The agent uses its tools (Playwright for browser interaction, visual comparison for validation) to find a workflow that accomplishes the objective.

2. **Working workflows are saved.** Once a workflow succeeds and is validated (by the review agent layer and/or by a human), it is captured as a deterministic playbook. The playbook records the exact sequence of steps, assertions, and validation criteria.

3. **Playbooks are replayable.** A saved playbook can be run as many times as needed, on any schedule, against any environment. It does not need AI to execute. It is deterministic and repeatable, exactly like a recorded macro.

4. **Playbooks are tied to changes and releases.** This is the critical feature: playbooks are mapped to the code, features, and UI elements they validate. When a code change or new release happens, the system knows which playbooks are affected and runs them automatically. Tests do not break when features or UI changes unless that is the intended outcome of the change.

5. **Developers stay in full control.** Playbooks are owned by the teams, not by the AI. Teams can review, edit, extend, or retire playbooks. The AI generates them; the humans govern them. The system makes it easy so developers do not have to constantly configure and set everything up from scratch.

### Connection to Colin's Earlier Statements

This concept directly extends what Colin described in both meetings:
- Set 01: "We can go and build those kind of playbooks so that they are repeatable, reusable, deterministic, but they can still be agentic from the first part."
- Set 01: The state graph maps file changes to relevant tests, enabling change-aware test triggering.
- Set 02: Exploratory flows discover issues, structured playbooks codify successful patterns.

The playbook concept bridges the gap between AI's strength (exploration, discovery, adaptability) and engineering's requirement (repeatability, reliability, predictability).

## The System Is Not Purely Agentic

Colin emphasized this point: the platform combines agentic AI with deterministic engineering tools. The document should explain the system at a high level in a way that makes this clear.

What makes the system trustable:
- **Playwright** provides deterministic browser automation. When it clicks a button, it clicks the button. There is no AI interpretation layer on the action itself.
- **Docker containers** provide isolated, reproducible execution environments. Tests run in clean, known states, not against shared or contaminated environments.
- **Deterministic playbooks** provide repeatable, predictable test execution once workflows are validated.
- **AI** is layered on top for exploration, visual understanding, and intelligent routing. It augments the deterministic foundation but does not replace it.

This is Colin's deterministic-first philosophy from Set 01 applied to the visual QA platform: "The trick is to keep it deterministic as far as you can, and then agentic at the end."

## Human in the Loop

Human involvement is a design feature, not a limitation. From Set 01, Colin described how human-in-the-loop decreases over time as agent confidence builds through repeated validated successes. From Set 02, the review agent layer means humans only see results that pass an initial quality filter.

For this platform, human-in-the-loop applies at several points:
- Reviewing and approving newly discovered workflows before they become playbooks
- Configuring thresholds and baselines (the specificity/customization layer)
- Disposition decisions when visual discrepancies are flagged (approve, reject, update baseline)
- Periodic review of mature playbooks to ensure continued relevance

## Control Panel

The platform includes a web-based control panel. This is not a separate product but the user-facing interface to the system.

### Features Colin Described
- **Scoped to the user.** Each user sees their relevant tests, playbooks, and results, not the full universe.
- **Repository integration.** Connects to the team's code repositories so playbooks can be tied to code changes.
- **SSO integration.** Uses the organization's single sign-on for access control.
- **Built on Django or FastAPI** (or the client's preferred framework), with Python as the natural choice for agentic library compatibility.

## Trustability and Transparency

The document needs to explain how the system earns trust, not just claim it. Drawing from both meetings:

- **Traceability.** Every action the system takes is logged. Every test run records the exact steps, the environment state, and the code version (GitHub SHA). This is the standard Colin holds his human QA team to, applied to agents.
- **Review layer.** Agent output is reviewed by a secondary agent before surfacing to humans. "Smart but lazy" means humans spend time on real issues, not noise.
- **Deterministic foundations.** The base layer is not AI. It is Playwright and Docker and saved playbooks. AI augments; it does not operate unsupervised at the critical path.
- **Confidence scoring.** Agent track records are built through repeated human-validated successes. Trust is earned incrementally, not assumed. (Colin's reinforcement learning mechanism from Set 01.)
- **Observability.** The system provides visibility into what agents are doing and why, enabling the "executive chef" model: humans walk around tasting, not cooking.

---

*This is a blockchain-style document. It will not be edited after creation.*
