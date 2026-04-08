# Q1 Deliverables

**Status:** Draft
**Last Updated:** 2026-02-02

---

## Discovery Phase (Weeks 1-4)

### Prerequisites (Must be in place before Discovery starts)

1. **System access** – Team must have access to CAT, DevX, Jenkins, Airflow, Grafana, and relevant codebases
2. **Designated Cisco contact** – A person at Cisco who can unblock administrative hurdles and answer questions
3. **Environment access** – Ability to view logs, APIs, and data sources we'll be integrating with

### Cisco Involvement

- **8-12 hours total** of Cisco team time during Discovery
- Spread however works for their schedule (e.g., 2-3 sessions per week)
- Used for: architecture walkthroughs, answering questions, access provisioning, clarifying requirements

### Independent Research (Majority of Discovery time)

- Codebase exploration
- Understanding existing systems and data flows
- Identifying integration points
- Documenting findings
- Preparing detailed scope and approach

### Discovery Deliverable

At end of Discovery (Week 4):
- Confirmed scope and approach document
- Detailed technical plan for A and F
- Identified risks and dependencies
- Refined estimates based on actual system understanding

---

## A – Developer Box (Weeks 5-13)

### Problem Being Solved

The local developer loop is a "black box" with no organizational visibility into what testing or validation happens before a PR is submitted.

### Tech Stack (TBD)

Tech stack and platform for telemetry collection and data pipeline is TBD. We can suggest approaches, but final decisions depend on Cisco's existing infrastructure, how they want data collected (agent, hooks, pyATS integration, etc.), and deployment constraints.

### Deliverables

1. **Telemetry/Instrumentation**
   - System to capture local test runs
   - Track pass/fail status, duration, coverage metrics
   - Make visible what is currently invisible

2. **Data Pipeline**
   - Store telemetry data
   - Surface results in a usable format
   - Foundation for later AI features

3. **Coverage Tracking**
   - Condition-level tracking (not just function-level)
   - Confirm specific code changes were exercised by tests

### What's NOT in Q1 for A

- AI-assisted debugging (requires data foundation first; likely Q2+)

---

## F – Branch Health (Weeks 5-13)

### Problem Being Solved

Release leads lack consolidated views to understand why things went wrong and who to follow up with.

### Tech Stack (TBD)

Grafana can be used as an initial starting point for viewing metrics. However, a real solution should be custom-built or use a suitable framework like FastAPI + React or Django in order to have the full feature set desired by Cisco (interactivity, action-taking, failure attribution with follow-up workflows). This is provided that hosting on-prem is available. Final platform decisions depend on Cisco preferences and deployment constraints.

### Deliverables

1. **Branch Health Dashboard**
   - Consolidated view for release leads
   - Build status, failure trends, blockers

2. **Failure Attribution**
   - Identify which PRs or changes contributed to issues
   - Surface "who to follow up with" automatically

3. **Automated Follow-up Triggers**
   - Notifications, assignments, or escalations
   - Triggered by specific conditions (repeated failures, severity thresholds)

---

## Q1 Team

| Role | Start | Notes |
|------|-------|-------|
| Senior Engineer (Onshore) | Week 1 | Leads Discovery, primary Cisco interface |
| Backend/Integration Engineer | Week 1 | Data pipelines, telemetry, integrations |
| AI Engineer | Week 1 | Foundation work, learns systems, prepares for Q2 |
| UI/Application Developer | End of Q1 | Dashboards for F |
| Agentic AI Specialist | Not Q1 | Joins Q2 |

---

## Risks and Dependencies

1. **Access delays** – If system access is delayed, Discovery extends and downstream work shifts
2. **Cisco availability** – If Cisco contact is unavailable, team gets blocked
3. **Undocumented systems** – If APIs or data sources are poorly documented, integration takes longer

---

## Milestone Summary

| Milestone | Target | Dependency |
|-----------|--------|------------|
| System access granted | Week 1 | Cisco |
| Cisco contact identified | Week 1 | Cisco |
| Discovery complete | Week 4 | Access + Cisco involvement |
| A - Telemetry MVP | Week 8 | Discovery complete |
| F - Dashboard MVP | Week 10 | Discovery complete |
| A + F feature complete | Week 13 | Ongoing Cisco collaboration |

**Note for final deliverable:** Do not include week-level targets in the Cisco-facing document. Use percentage-based progress milestones instead to avoid over-committing to specific timelines.
