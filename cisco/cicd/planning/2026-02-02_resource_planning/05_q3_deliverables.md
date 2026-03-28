# Q3 Deliverables

**Status:** Draft
**Last Updated:** 2026-02-02

---

## B – Gate Failures / AI Diagnosis

### Problem Being Solved

When a gate fails, engineers must manually investigate the cause. This is time-consuming and requires context that isn't always readily available. Divakar described the desired state: AI should "triage the build failure automatically and come back with some information or maybe a possible code diff" to help the engineer fix it.

There are 39 gates in the PR validation process, including build validation, static analysis, compiler warnings, sanities, bug severity, CDT, diff check, code review, and others. Failures at any of these gates currently require manual triage.

---

### Tech Stack (TBD)

AI/LLM approach depends on Cisco preferences, model availability, and on-prem deployment constraints. Specific frameworks and models TBD with Cisco. On-prem deployment required.

---

### Deliverables

1. **Log and Output Analysis Pipeline**
   - Ingest failure logs from Jenkins and Airflow
   - Parse and structure log data for AI analysis
   - Handle different log formats across different gate types

2. **AI-Driven Root Cause Identification**
   - Analyze failure patterns and logs
   - Identify likely root cause of failure
   - Leverage historical failure data where available

3. **Suggested Fixes**
   - Based on root cause analysis, suggest likely fixes (not automated fixes - suggestions for human review)
   - Requires understanding the codebase and the problem
   - Sources of issues for analysis: user-reported issues, application/system-reported errors
   - Link to relevant documentation, logs, or past resolutions
   - Scope is limited to diagnosis and suggestion; automated application of fixes is out of scope (that's E)

4. **Integration with Unified Interface (from Q2)**
   - Surface diagnosis results in the single pane of glass
   - When a developer asks "Why did this fail?", provide AI-generated diagnosis
   - Seamless experience from status view to diagnosis

---

### What's NOT in Q3 for B

- Automated application of fixes (that's E, Self-Healing, Q4)
- Governance framework for automated actions (that's E, Q4)

---

## D – Coverage Tracking

### Problem Being Solved

There's no way to verify that specific code changes were actually exercised by tests. Srini explained: "If I change a function foo... there is no easy way whether that particular condition has been touched through my validation."

CDT (Context Driven Testing) exists and provides function-to-test-case mapping, but it doesn't confirm that specific conditions within a function were actually hit. Cisco wants condition-level tracking, not just function-level.

---

### Tech Stack (TBD)

Coverage tracking approach depends on Cisco's existing tooling and how they collect coverage data. This deliverable builds on:

- Developer Box telemetry from A (Q1)
- Integration layer from C (Q2)
- CDT's existing function-to-test mapping

---

### Deliverables

1. **Condition-Level Coverage Tracking**
   - Go beyond function-level to track specific conditions (if statements, branches)
   - Confirm that code changes in a PR were actually exercised by tests
   - Integrate with existing coverage tooling where possible

2. **PR Coverage Confirmation**
   - For a given PR, show which changed lines/conditions were covered
   - Surface gaps before merge
   - Clear visualization of "this was tested" vs "this was not tested"

3. **Integration with Developer Box Data (from Q1)**
   - Leverage telemetry captured in A
   - Track coverage from local testing through CI
   - End-to-end visibility Srini requested

4. **Integration with Unified Interface (from Q2)**
   - Surface coverage information in the single pane of glass
   - Part of the PR status view

---

### What's NOT in Q3 for D

- Blocking PRs based on coverage (policy decision for Cisco)
- Automated test generation to fill coverage gaps (out of scope)

---

## Team Active in Q3

| Role | Focus |
|------|-------|
| Senior Engineer (Onshore) | Coordination, architecture decisions, Cisco interface |
| Backend/Integration Engineer | Coverage data integration, log pipelines for B |
| UI/Application Developer | Surfacing diagnosis and coverage in UI |
| AI Engineer | Heavy focus on B - diagnosis AI, log analysis, suggested fixes |
| Agentic AI Specialist | Supporting AI work, ramping up for E, may lead architecture for diagnosis |

---

## Dependencies

- Q2 unified interface and integration layer (B and D surface results through it)
- Q1 Developer Box telemetry (D builds on this data)
- Access to Jenkins/Airflow logs for failure analysis (B)
- Understanding of CDT and existing coverage tooling (D)

---

## Risks

1. **Log format variability** – Different gates may have different log formats, complicating analysis
2. **AI accuracy** – Diagnosis suggestions need to be useful, not just noise; requires tuning
3. **Coverage tooling gaps** – Condition-level coverage may require tooling Cisco doesn't have
4. **Scope creep on "suggested fixes"** – Easy to over-promise; need clear boundaries

---

## Milestone Summary

| Milestone | Target | Notes |
|-----------|--------|-------|
| Log ingestion pipeline working | Week 3 of Q3 | Foundation for B |
| AI diagnosis MVP (1-2 gate types) | Week 6 of Q3 | Prove the pattern |
| Coverage tracking MVP | Week 6 of Q3 | Basic condition-level working |
| B + D integrated into unified interface | Week 10 of Q3 | Seamless UX |
| B + D feature complete | End of Q3 | Polish and handoff |

**Note for final deliverable:** Do not include week-level targets in the Cisco-facing document. Use percentage-based progress milestones instead (e.g., "25% - foundation complete", "50% - MVP working", etc.) to avoid over-committing to specific timelines.
