# Session Handoff – 2026-02-02

**Purpose:** Get a new Claude Code session up to speed quickly on the Cisco CI/CD engagement.

---

## Quick Context

BayOne Solutions (Colin Moore = Director of AI, your primary contact) is starting a consulting engagement with Cisco to improve their NX-OS CI/CD pipeline. This repository contains planning documents, not code.

## Read Order

1. **CLAUDE.md** – Working instructions, documentation system, formatting preferences
2. **project/engagement-status.md** – Current state (always start here)
3. **history/0001_2026-02-02_initial-state.md** – How we got here

## What Just Happened

Cisco confirmed they want to start with:
- **A – Developer Box** (visibility, insights, AI-assisted debugging)
- **F – Branch Health** (failure attribution, dashboards)

**Budget: $100K/quarter.** This is the confirmed amount. If more is needed, we must justify it. Plan the team to fit within $100K/quarter and only propose increases if truly necessary.

Discovery phase: 1-2 weeks. Previous phasing (C first) is obsolete. A+F is the new focus.

## Key People

**BayOne:** Colin Moore (you work with him), Rahul (President), Amit (Delivery), Zahra (Sales)

**Cisco:** Anand (Director, main contact), Arun (VP sponsor), Srini (Sr Eng Manager), Divakar (Eng Lead)

## Working With Colin

- Ask before creating/editing files
- Prefer markdown over long chat responses
- Never delete files – create new versions
- Ask questions incrementally, not in blocks
- Don't make assumptions – this is collaborative

## Formatting

- Slashes: space after, not before ("Unified interface/ single pane")
- Em dashes after bold: no space before ("**Bold**– text")
- Avoid em dashes in prose

## Immediate Task (for Rahul by Monday morning)

Rahul (President) needs a document with:

1. **Resource planning for A-F** – Team structure needed to deliver all six use cases over ~1 year
2. **Job descriptions** – For the key roles we need to hire
3. **Quarterly phasing** – What we do Q1 vs Q2 vs Q3 etc.
4. **Resource loading** – Which roles needed when, synchronized with phases

### Constraints
- Budget is **$100K/quarter** – plan within this, justify if more needed
- Staffing model: 1-1.5 FTE onshore (Bay Area), 4-5 offshore to scale
- Keep deliverables HIGH-LEVEL – avoid overpromising before discovery
- Skills needed: Agentic AI experience (system-level, not just prompts), Airflow experience
- Cisco requirements: startup mindset, build on their stack, no external products

### The Six Items (A-F)

| Item | Description | Complexity |
|------|-------------|------------|
| A | Developer Box – telemetry, coverage tracking, AI-assisted debugging | Phase 1 priority |
| B | Gate Failures – AI diagnosis, root cause analysis, suggested fixes | Medium |
| C | Cross Pipeline – Unified interface, single pane of glass | Was original Phase 1 |
| D | Coverage Tracking – Condition-level coverage confirmation for PRs | Needs Dev Box data |
| E | Self-Healing – Automated corrective actions, governance | Highest (350-500+ hrs) |
| F | Branch Health – Dashboards, failure attribution, follow-up | Phase 1 priority |

## Other Items (Lower Priority)

- Discovery plan details
- Updated estimates in `documents/cisco-dev-hours-estimate.md` (Phase 5/E is underestimated)
- Candidate sourcing

## Documents to Know About

| File | Purpose |
|------|---------|
| `documents/cisco-x-bayone.md` | Main client deliverable (may need A+F focus update) |
| `documents/cisco-dev-hours-estimate.md` | Estimates (Phase 5 underestimated, needs update) |
| `documents/cisco-questions-for-clarification.md` | 31 unanswered questions for Cisco |
| `specs/bayone-design-spec.md` | HTML document styling guide |

## Session Folder Structure

If you need working documents, ask Colin if he wants the standard structure:

```
claude/<date>_<topic>/
├── planning/
├── goals/
├── progress/
├── decisions/
├── research/
├── source/
└── issues_and_improvements/
```

File naming: `00_name.md`, `01_name.md`, etc.
