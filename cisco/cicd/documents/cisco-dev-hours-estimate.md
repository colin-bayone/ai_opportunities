# Cisco CI/CD Engagement: Development Hours Estimate

Internal document for BayOne team.

---

## Summary

| Phase | Item(s) | Dev Hours | Dev Weeks |
|-------|---------|-----------|-----------|
| 1 | A - Developer Box Instrumentation + F - Branch Health | 150–210 | 4–5 |
| 2 | C - Cross Pipeline / Unified Interface | 180–250 | 4.5–6 |
| 3 | B - Gate Failures / AI Diagnosis | 100–150 | 2.5–4 |
| 4 | D - Coverage Tracking | 80–120 | 2–3 |
| 5 | E - Self-Healing | 300–500 | 7.5–13 |
| **Total** | | **810–1,230** | **20–31** |

*Dev weeks assumes 40 hours/week.*

---

## Assumptions

- All estimates assume AI-assisted development (Claude Code, pair programming with AI tools)
- Internal efforts show approximately 2x speedup with AI tooling; estimates below reflect this
- Estimates are ranges due to unknowns around scale, API availability, and documentation quality
- Team composition: 1 Senior AI Engineer, 2 Junior AI Engineers, 3 Web Developers, 1 Agentic AI hire (pending)
- Phases are sequential; some parallel work possible within phases

---

## Phase 1: Developer Box Instrumentation (Item A) + Branch Health (Item F)

**Scope:** 
- A: Telemetry system to capture local test runs, pass/fail, duration, coverage. Data pipeline to store and surface results.
- F: Release lead dashboards, failure attribution, automated follow-up triggers using existing data sources.

**Team:** Web developers (telemetry pipeline, dashboards, data storage)

**Dev Hours:** 150–210 hours

**Notes:** Quick wins that deliver value early while building familiarity with Cisco's ecosystem. A depends on how Cisco wants data collected (agent, hooks, pyATS integration). F can leverage existing Grafana/data access initially; full integration with unified data layer comes later. This phase sets us up well for Phase 2 by giving hands-on experience with their systems.

---

## Phase 2: Cross Pipeline / Unified Interface (Item C)

**Scope:** API integrations with CAT, DevX, Jenkins, Airflow, Grafana. Data normalization across systems. Chat interface frontend with natural language query capability.

**Team:** Web developers (integrations, frontend), Senior AI Engineer (NLP/chat layer)

**Dev Hours:** 180–250 hours

**Notes:** Foundational for AI features. Quality of Cisco's API documentation and access will significantly impact timeline. Phase 1 experience will inform this work significantly. If APIs are poorly documented or require custom work, add 30-50%.

---

## Phase 3: Gate Failures / AI Diagnosis (Item B)

**Scope:** AI-driven failure analysis, root cause identification, suggested fixes.

**Team:** Senior AI Engineer + Agentic AI hire (diagnosis)

**Dev Hours:** 100–150 hours

**Notes:** Requires access to logs and failure patterns. Builds on unified data layer from Phase 2. Overlaps with Cisco's internal AI code review project—boundary must be clarified.

---

## Phase 4: Coverage Tracking (Item D)

**Scope:** Condition-level coverage confirmation for PRs. Integration with CDT and Developer Box instrumentation.

**Team:** Web developers, Junior AI Engineers (analysis logic)

**Dev Hours:** 80–120 hours

**Notes:** Builds on Phase 1 (Developer Box data) and Phase 2 (unified data access). Scope depends on what gaps exist in CDT.

---

## Phase 5: Self-Healing (Item E)

**Scope:** Automated corrective actions for qualifying failures. Governance framework definition. Action triggers in Jenkins/Airflow. Safety mechanisms. Rollback capabilities.

**Team:** Senior AI Engineer, Agentic AI hire, Web developers (triggers/integrations)

**Dev Hours:** 300–500 hours

**Notes:** Highest complexity and risk. This is essentially building an agentic AI system that takes real actions in production. Estimate is highly dependent on scope—specifically what types of failures are "allowed" to be auto-corrected and how extensive the governance framework needs to be. Requires governance framework to be defined with Cisco before implementation. May expand significantly based on safety/testing requirements.

---

## Considerations

- **Discovery period:** Amit suggested an initial month for deep dive on environments and architecture. This is not included in the above estimates but is recommended before Phase 1 begins. Estimate 40-80 hours for discovery.

- **Unknowns that could expand scope:**
  - Poor or missing API documentation
  - On-prem infrastructure with access constraints
  - Custom agent development for Developer Box
  - Governance framework complexity for Self-Healing
  - Scale (if PRs/day is very high, infrastructure needs change)

- **Overlap with Cisco internal AI work:** Boundary with their AI code review project remains unclear. If they want us to integrate with or extend their internal project, scope changes significantly.

---

## Phasing Rationale

1. **Phase 1 (A + F) first** for quick wins and low initial cost. Builds familiarity with Cisco's ecosystem and sets up well for Phase 2.
2. **Phase 2 (C) second** because it's foundational for AI features, and Phase 1 experience will inform the integration work.
3. **Phase 3 (B) third** because AI diagnosis builds on the unified data layer from Phase 2.
4. **Phase 4 (D) fourth** because coverage tracking needs both Developer Box data (Phase 1) and unified data access (Phase 2).
5. **Phase 5 (E) last** because it's highest risk, requires governance, and benefits from lessons learned in earlier phases.
