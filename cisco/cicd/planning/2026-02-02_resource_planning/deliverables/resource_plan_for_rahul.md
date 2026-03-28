# NX-OS CI/CD Pipeline Improvement Initiative

## Resource Plan and Quarterly Roadmap

**Prepared for:** Cisco Systems
**Prepared by:** BayOne Solutions
**Date:** February 2026

---

## 01 Executive Summary

BayOne proposes a year-long engagement to improve Cisco's NX-OS CI/CD pipeline through six integrated capability areas. The engagement addresses challenges across the development lifecycle: from lack of visibility into local developer testing, through fragmented cross-pipeline status information, to manual failure triage and limited automation for corrective actions.

The work is phased to build incrementally, with each quarter's deliverables providing the foundation for the next. A team of five resources will ramp in as deliverables require, starting with three in Q1 and growing to full capacity in Q2.

---

## 02 Team Structure

The team combines an on-site technical leader who interfaces with Cisco directly, with an offshore implementation team that brings specialized expertise in backend integration, application development, and AI.

| Role | Location | Quarterly Rate | Start |
|------|----------|----------------|-------|
| Senior Engineer | Onshore (Bay Area) | $47K | Q1 Week 1 |
| Backend/Integration Engineer | Offshore | $12K | Q1 Week 1 |
| AI Engineer | Offshore | $12.5K | Q1 Week 1 |
| UI/Application Developer | Offshore | $12K | End of Q1 |
| Agentic AI Specialist | Offshore | $16K | Early Q2 |

**Leadership Structure**

Colin Moore (Director of AI, BayOne) provides overall technical direction and final decision authority. The onshore Senior Engineer reports to Colin, leads the offshore team day-to-day, and serves as BayOne's primary interface with Cisco engineering teams. This is a hands-on technical leadership role, not a management-only position.

**Technical Requirements**

All team members are expected to be proficient with AI pair programming tools. At least one team member will have Apache Airflow experience, which is critical given Airflow's role in Cisco's orchestration layer. The onshore Senior Engineer will own DevOps best practices for the team, with the Backend Engineer providing secondary DevOps expertise.

---

## 03 Quarterly Roadmap

### Q1: Discovery + Developer Box + Branch Health

**Discovery Phase (3-4 Weeks)**

Before implementation begins, the team will conduct a structured discovery phase requiring approximately 8-12 hours of Cisco team involvement, spread as convenient. The remainder of discovery time is independent research into the codebase and existing systems. Discovery produces a confirmed scope document with refined estimates based on actual system understanding.

**Prerequisites:** System access to CAT, DevX, Jenkins, Airflow, Grafana, and relevant codebases. A designated Cisco contact who can unblock administrative hurdles and answer questions.

**A: Developer Box**

The local developer loop is currently a black box with no organizational visibility into what testing or validation happens before a PR is submitted.

Deliverables include a telemetry system to capture local test runs with pass/fail status, duration, and coverage metrics. A data pipeline will store and surface these results. Coverage tracking will operate at the condition level, not just function level, confirming that specific code changes were exercised by tests.

Tech stack is TBD pending Cisco input on how data should be collected (agent, hooks, pyATS integration) and deployment constraints.

**F: Branch Health**

Release leads lack consolidated views to understand why things went wrong and who to follow up with.

Deliverables include a branch health dashboard providing consolidated status, failure trends, and blockers. Failure attribution logic will surface which PRs or changes contributed to issues and identify who to follow up with. Automated follow-up triggers will send notifications or escalations based on specific conditions.

Grafana can serve as an initial starting point for viewing metrics. However, a real solution should be custom-built or use a suitable framework like FastAPI + React or Django to provide the full feature set desired by Cisco, including interactivity and action-taking workflows. Final platform decisions depend on Cisco preferences and on-prem deployment availability.

**Team Active:** Senior Engineer (Onshore), Backend/Integration Engineer, AI Engineer. UI/Application Developer joins late Q1 if dashboards are ready.

---

### Q2: Unified Interface / Cross-Pipeline Visibility

**C: Unified Interface**

Information is currently scattered across multiple systems with no unified view. Engineers submit PRs and have no easy way to monitor progress. There is no chat or conversational interface to query pipeline status.

This deliverable requires integration with six Cisco systems, each with its own APIs, data schemas, and access patterns:

| System | Purpose |
|--------|---------|
| CAT (Commit Approval Tool) | Gate configurations and status |
| DevX Platform | PR metadata and status |
| Jenkins | Short/quick CI checks |
| Apache Airflow | Longer-running jobs |
| Grafana | Analytics and metrics |
| GitHub | Source control and PR information |

Deliverables include an API integration layer connecting all relevant systems with unified authentication and data normalization. A unified data layer will consolidate PR status from all sources into a common model. The single pane of glass interface will show developers all their PRs across branches in one place with status, blockers, and next actions. A chat interface will enable natural language queries such as "Where is my PR?" or "Why did this fail?"

Each integration requires understanding the API or data access method, handling authentication, normalizing data into a common schema, and handling errors and edge cases. This is substantial backend work spanning multiple systems with different APIs.

**Team Active:** Full team. UI/Application Developer starts if they haven't already. Agentic AI Specialist joins early Q2 to learn systems and support AI work while preparing for Q4.

---

### Q3: AI Diagnosis + Coverage Tracking

**B: Gate Failures / AI Diagnosis**

When a gate fails, engineers must manually investigate the cause. This is time-consuming and requires context that isn't always readily available. There are 39 gates in the PR validation process, including build validation, static analysis, compiler warnings, sanities, bug severity, CDT, diff check, code review, and others.

Deliverables include a log and output analysis pipeline that ingests failure logs from Jenkins and Airflow, parses and structures log data for AI analysis, and handles different log formats across different gate types. AI-driven root cause identification will analyze failure patterns and logs to identify likely causes, leveraging historical failure data where available.

Suggested fixes will provide recommendations for human review based on root cause analysis. This requires understanding the codebase and the problem. Sources of issues for analysis include user-reported issues and application/system-reported errors. Scope is limited to diagnosis and suggestion; automated application of fixes is E (Q4), not B.

**D: Coverage Tracking**

There is no way to verify that specific code changes were actually exercised by tests. CDT exists and provides function-to-test-case mapping, but it doesn't confirm that specific conditions within a function were actually hit.

Deliverables include condition-level coverage tracking that goes beyond function-level to track specific conditions and branches. PR coverage confirmation will show which changed lines and conditions were covered before merge, with clear visualization of what was tested versus what was not. This integrates with Developer Box telemetry from Q1 for end-to-end visibility.

**Team Active:** Full team. AI Engineer has heavy focus on B. Agentic AI Specialist supports AI work and ramps up for E.

---

### Q4: Self-Healing / Automated Corrective Actions

**E: Self-Healing**

For failures that don't require human judgment, engineers still have to manually intervene to retry or fix. Self-healing means automated retry for transient failures such as network timeouts or flaky tests, and automated simple corrections for well-defined issues such as copyright check failures or formatting issues. All actions are taken within a defined governance framework and are logged, auditable, and reversible where possible.

Self-healing does not mean AI making arbitrary code changes without human review, bypassing code review or approval processes, or taking actions outside defined governance boundaries.

**Governance Framework**

Before any automated actions can be implemented, a governance framework must be defined collaboratively with Cisco. This includes determining what types of failures can be auto-corrected, what actions the system can take, who defines and approves the rules, and how audit and accountability work.

Deliverables include automated action triggers integrated with Jenkins and Airflow, decision logic for which action to take based on failure type and governance rules, safety mechanisms including limits on automated actions and circuit breakers, rollback capabilities where possible, and audit visibility with all actions logged and surfaced in the unified interface.

**Timeline Considerations**

E is unique among the deliverables because it requires organizational alignment beyond technical implementation. The governance framework involves policy decisions, stakeholder buy-in, and risk acceptance that extend beyond development work.

We recommend beginning governance conversations in Q2-Q3 in parallel with other work. This allows time for Cisco stakeholders to align on policy questions before technical implementation begins.

| Scenario | Governance | Technical | Completion |
|----------|------------|-----------|------------|
| Optimistic | Q2-Q3 (parallel) | Q4 | End of Q4 |
| Realistic | Q3-Q4 | Q4 + Year 2 | Q1-Q2 Year 2 |
| Extended | Q4+ | Year 2 | Mid Year 2 |

The scope of automated actions that Cisco wants to enable is a key driver of the timeline. Cisco needs to establish the scope they are requiring for success to accurately estimate this deliverable. BayOne can propose our view on what's achievable and appropriate, but Cisco must accept and define the boundaries.

BayOne will be technically ready to implement in Q4. The Agentic AI Specialist joins early Q2 specifically to prepare for this work. We can support governance discussions as early as Cisco is ready to have them.

**Team Active:** Full team. Agentic AI Specialist leads decision logic, safety mechanisms, and governance implementation.

---

## 04 Investment Summary

| Quarter | Team Size | Cost | vs $100K Budget |
|---------|-----------|------|-----------------|
| Q1 | 3-4 | $71.5K | Under by $28.5K |
| Q2 | 5 | $99.5K | Under by $0.5K |
| Q3 | 5 | $99.5K | Under by $0.5K |
| Q4 | 5 | $99.5K | Under by $0.5K |
| **Year Total** | | **$370K** | **Under by $30K** |

All quarters are under the $100K/quarter budget. Q1 has significant buffer due to the phased team ramp. The $30K annual buffer provides flexibility for scope adjustments or unexpected needs.

---

## 05 Next Steps

**From Cisco (Before Start)**

1. **System Access:** Provide team access to CAT, DevX, Jenkins, Airflow, Grafana, and relevant repositories.

2. **Designated Contact:** Identify a primary engineering contact for discovery sessions. Estimated Cisco involvement is 8-12 hours during the first 3-4 weeks, spread as convenient.

3. **Infrastructure Discussion:** Clarify infrastructure ownership and deployment environment constraints. Does Cisco's infra team own deployment, or does BayOne need to include infrastructure responsibility?

**From BayOne (Immediate)**

1. **Hiring:** Begin recruitment for Senior Engineer (Onshore), Backend/Integration Engineer, and AI Engineer immediately. UI/Application Developer hiring follows in Q1. Agentic AI Specialist is specialized and hard to source; search begins early.

2. **Technical Readiness:** Prepare for discovery phase pending access.

**Target Start:** Upon access grant and contact designation.

---

*Confidential — Prepared for Cisco Systems*
