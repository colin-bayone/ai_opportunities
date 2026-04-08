# Cisco CI/CD Pipeline: Understanding of the Problem

Based on the discovery call held December 15, 2025.

---

## Overview

Cisco operates a multi-stage CI/CD pipeline for their NX-OS development. The pipeline spans from individual developer workstations through PR validation and into official builds for release. While the infrastructure is mature and has been running for years, several gaps exist in visibility, automation, and developer experience.

The core problem: **Engineers lack a unified, intelligent view of their work as it moves through the pipeline.** Status is fragmented across multiple tools, failures require manual investigation, and there is no conversational or AI-driven interface to help developers understand where things stand or what to do next.

---

## Current Pipeline Structure

The pipeline consists of three main zones:

### Developer Box (Blue)

Where individual developers write code, run local tests, and prepare PRs. This phase is currently a "black box" with no organizational visibility into what testing or validation occurs before code is submitted.

### GitHub PR Validation (Green)

Once a PR is submitted, it passes through 39 gates including build validation, static analysis, compiler warnings, sanities, bug severity checks, CDT (Context Driven Testing), diff checks, code review, and others. Short checks run via Jenkins; longer jobs run via Apache Airflow. A tool called CAT (Commit Approval Tool) manages gate enablement per branch.

### Official Build / CD (Red)

After PR merge, code enters the integrated "green build" process. QA picks up labeled builds, files bugs against specific versions, and the cycle continues until the build is release-ready. Release leads manage branch health at this stage.

---

## Key Pain Points

1. **No visibility into the Developer Box.** The organization cannot see what tests are run locally, whether code changes are covered, or what validation happened before a PR was submitted.

2. **Fragmented status across tools.** Information lives in CAT, DevX, Jenkins, Airflow, and Grafana. There is no single place for a developer to ask "Where is my PR?" and get a complete answer.

3. **Manual failure investigation.** When a gate fails, engineers must manually triage the cause. There is no automated diagnosis or suggested remediation.

4. **No self-healing or auto-resume.** Failures that don't require human judgment still require manual intervention to retry or fix.

5. **Incomplete coverage tracking.** While CDT exists for function-to-test mapping, there is no confirmation that specific code changes (at the condition level) were actually exercised by tests.

6. **Limited branch health visibility for release leads.** Release leads lack consolidated views to understand why things went wrong and who to follow up with.

---

## What Cisco is Looking For

Cisco described a desire for an "expert assistant" embedded in the pipeline that could:

- Provide real-time, persona-based views (developer vs. release lead)
- Answer natural language questions about PR status and pipeline health
- Diagnose failures and suggest fixes
- Take automated corrective action where appropriate
- Track test coverage end-to-end from Developer Box through CI

The stated goal is to improve developer productivity, with a target of reducing average PR merge time by 20-30%.

---

## Existing Assets

- **CDT (Context Driven Testing):** Live for 2+ years, provides function-to-test-case mapping
- **Grafana dashboards:** Analytics on gate performance, PR times, anomalies
- **pyATS:** Test automation framework with custom libraries for NX-OS
- **AI Code Review project:** Separate internal initiative going live soon (not in our scope)

---

## Open Questions

While the high-level problem is clear, significant details remain undefined:

- Scale (PRs/day, developers, repositories, branches)
- Technical specifics (APIs, data schemas, log formats, infrastructure hosting)
- MVP definition and timeline
- Boundary between Cisco's internal AI work and what they want from us
- Governance for automated actions

These should be clarified before we scope or estimate the engagement. See the Questions for Cisco document for the full list.
