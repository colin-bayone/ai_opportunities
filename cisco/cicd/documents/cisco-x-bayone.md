# Current State and Potential Enhancements

## For Cisco CI/CD Pipeline

---

## Overview

Cisco operates a multi-stage CI/CD pipeline for their NX-OS development. The pipeline spans from individual developer workstations through PR validation and into official builds for release. While the infrastructure is mature and has been running for years, several gaps exist in visibility, automation, and developer experience.

The core problem: **Engineers lack a unified, intelligent view of their work as it moves through the pipeline.** Status is fragmented across multiple tools, failures require manual investigation, and there is no conversational or AI-driven interface to help developers understand where things stand or what to do next.

---

## Current Pipeline Structure

The pipeline consists of three main zones:

### Developers (Blue Box)

Where individual developers write code, run local tests, and prepare PRs. This phase is currently a "black box" with no organizational visibility into what testing or validation occurs before code is submitted.

### Github/ DevX (Green Box)

Once a PR is submitted, it passes through 39 gates including build validation, static analysis, compiler warnings, sanities, bug severity checks, CDT (Context Driven Testing), diff checks, code review, and others. Short checks run via Jenkins; longer jobs run via Apache Airflow. A tool called CAT (Commit Approval Tool) manages gate enablement per branch.

### Official Build/ DC BU (Red Box)

After PR merge, code enters the integrated "green build" process. QA picks up labeled builds, files bugs against specific versions, and the cycle continues until the build is release-ready. Release leads manage branch health at this stage.

---

## Existing Assets

- **CDT (Context Driven Testing):** Live for 2+ years, provides function-to-test-case mapping
- **Grafana dashboards:** Analytics on gate performance, PR times, anomalies
- **pyATS:** Test automation framework with custom libraries for NX-OS
- **AI Code Review project:** Separate internal initiative going live soon (not in our scope)

---

## Potential Enhancements

### Developers (Blue Box)

**Current State:** Developers write code, run local tests, and prepare PRs. This phase is a "black box" with no organizational visibility into what testing or validation occurs before code is submitted. Tests and coverage are untracked. Failures are debugged manually without tooling assistance.

**Potential Enhancements:**

- **Telemetry and instrumentation**– Capture local test runs, pass/fail status, duration, and coverage metrics. Make visible what is currently invisible.
- **Coverage tracking**– Confirm that specific code changes (at the condition level, not just function level) were exercised by tests before PR submission.
- **AI-assisted debugging**– Surface patterns in test failures, suggest likely causes, reduce time spent investigating.

---

### Github/ DevX (Green Box)

**Current State:** PRs pass through 39 gates (build validation, static analysis, sanities, CDT, code review, etc.) orchestrated by Jenkins and Apache Airflow. Status is fragmented across CAT, DevX, Jenkins, Airflow, and Grafana. Engineers often don't know where a PR is stuck or why. Gate failures require manual triage. No automated retry or correction.

**Potential Enhancements:**

- **Unified interface/ single pane of glass**– Consolidate data from all systems into one view. Allow natural language queries like "Where is my PR?" or "Why did this fail?" Surface status, blockers, and recommended actions in one place.
- **AI-driven failure diagnosis**– Analyze logs and outputs to identify root cause. Provide summaries, link to relevant logs, suggest likely fixes. Reduce manual investigation time.
- **Automated corrective actions**– For failures that don't require human judgment (e.g., transient errors, copyright check fixes), allow the system to retry or apply simple corrections automatically. Requires governance framework to define what's allowed.
- **Coverage confirmation**– Track whether the specific diff in a PR was exercised by tests during CI. Surface gaps before merge.

---

### Official Build/ DC BU (Red Box)

**Current State:** After PR merge, code enters the integrated "green build" process. QA picks up labeled builds and files bugs against specific versions. Release leads manage branch health but lack consolidated views to understand failures and accountability.

**Potential Enhancements:**

- **Branch health dashboard**– Consolidated view for release leads showing build status, failure trends, and blockers across the branch.
- **Failure attribution**– Identify which PRs or changes contributed to issues. Surface "who to follow up with" automatically.
- **Automated follow-up**– Notifications, assignments, or escalations triggered by specific conditions (e.g., repeated failures, severity thresholds).

---

## Open Questions

While the high-level problem is clear, several key details remain undefined:

- Scale (PRs/day, developers, repositories, branches)
- Technical specifics (APIs, data schemas, log formats, infrastructure hosting)
- MVP definition and timeline
- Boundary between ongoing internal AI Projects @ Cisco and the scope of this engagement
- Governance framework for automated actions

These should be clarified before we scope or estimate the engagement.

---

## Summary Table

| Item | Space              | Current State                              | Potential Enhancement                                                  |
| ---- | ------------------ | ------------------------------------------ | ---------------------------------------------------------------------- |
| A    | Developer Box      | Black box, no tracking                     | Telemetry, coverage tracking, AI-assisted debugging                    |
| B    | Gate Failures      | Manual triage                              | AI diagnosis, root cause analysis, suggested fixes                     |
| C    | Cross Pipeline     | Siloed tools (CAT, DevX, Jenkins, Airflow) | Unified chat interface, single pane of glass, natural language queries |
| D    | Coverage Tracking  | Incomplete/ CDT gaps                       | Condition-level coverage confirmation for PRs                          |
| E    | Self-Healing       | Manual resume/ intervention                | Automated corrective actions, governance framework                     |
| F    | Branch Health (CD) | Limited visibility for release leads       | Dashboards, failure attribution, automated follow-up                   |

**Please rank these A-F in order of priority for your team.**
