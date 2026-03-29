# Cisco Work Streams - Explorer Agent Findings

**Agent:** Cisco-Root Explorer
**Date:** 2026-03-17
**Folders Scanned:** project/, history/, documents/, context/, new_context_2-2-2026/, SOW/, cisco-related claude sessions

---

## CISCO WORK STREAMS CATALOG

Based on extensive exploration of discovery documents, engagement status, development estimates, meeting summaries, and SOW materials, here is a comprehensive catalog of active work streams and initiatives for the Cisco NX-OS CI/CD Pipeline engagement:

---

### WORK STREAM A: Developer Box Instrumentation

**Description/Objective**
Provide visibility into local developer testing and validation. Currently a "black box" with no organizational oversight of what testing occurs before PR submission. Goals include capturing telemetry, tracking test execution, debugging support, and coverage confirmation at the condition level.

**Status**
In-progress (Phase 1 starting, discovery underway as of Feb 2026)

**Key Deliverables**
- Telemetry system to capture local test runs (pass/fail status, duration, coverage metrics)
- Data pipeline to store and surface test results
- Coverage tracking infrastructure (condition-level, not just function-level)
- AI-assisted debugging patterns and failure analysis
- Integration with pyATS test automation framework

**Technical Paths/Components**
- Developer Box (local environment)
- pyATS framework integration
- Telemetry collection agent or CI hooks
- Data storage (MongoDB on-prem)
- Coverage tracking system (building on CDT)
- MySQL-based relational services for test metadata

**Stakeholders**
- **BayOne:** Colin Moore (Director of AI, Technical Lead)
- **Cisco:** Srinivas/Srini (Senior Engineering Manager, AI strategy), Divakar (Engineering Lead)

**Notes/Context**
- Selected as Phase 1 starting point (with Branch Health F) for quick wins and early momentum
- May require custom agent development on developer machines or integration with existing CI hooks
- Depends on clarity about how data collection should work (agent vs. hooks vs. pyATS integration)
- Feeds into later phases (D - Coverage Tracking)

---

### WORK STREAM B: Gate Failures / AI-Driven Diagnosis

**Description/Objective**
Automate root cause analysis for failures in the 39-gate PR validation pipeline. Instead of manual triage, provide AI-driven diagnosis with suggested fixes and relevant log links. Target: reduce manual investigation time.

**Status**
Planned (Phase 3, deferred until Phases 1-2 complete)

**Key Deliverables**
- AI analysis engine for log/output patterns
- Root cause identification logic
- Suggested fixes and remediation recommendations
- Integration with failure log data from Jenkins/Airflow
- Automated triage summaries

**Technical Paths/Components**
- Jenkins (handles short/quick checks)
- Apache Airflow (handles longer-running jobs)
- Splunk or direct Jenkins log access
- LLM-powered analysis (via DeepSight platform)
- MongoDB (raw pipeline data storage)
- Log aggregation and pattern matching

**Stakeholders**
- **BayOne:** Colin Moore, Senior AI Engineer
- **Cisco:** Srinivas (AI platform coordination), Divakar (Jenkins access/infrastructure)
- **Cisco Internal:** DeepSight platform team (AI infrastructure)

**Notes/Context**
- Overlaps with Cisco's internal AI code review project (boundary to be clarified)
- Builds on unified data layer from Phase 2
- Requires access to failure patterns and common error types
- High-complexity work; depends on quality of log data available
- Development hours estimate: 100-150 hours

---

### WORK STREAM C: Cross-Pipeline / Unified Interface (Chat Interface)

**Description/Objective**
Consolidate fragmented data from CAT, DevX, Jenkins, Airflow, and Grafana into a single unified view. Provide natural language chat interface for queries like "Where is my PR?" "Why did this fail?" Surface status, blockers, and recommended actions in one place.

**Status**
Planned (Phase 2, foundational work before AI features)

**Key Deliverables**
- API integrations with CAT, DevX, Jenkins, Airflow, Grafana
- Data normalization layer across disparate systems
- Chat interface frontend with NLP capability
- Natural language query processing
- Unified PR/gate status dashboard
- Single pane of glass for pipeline visibility

**Technical Paths/Components**
- CAT (Commit Approval Tool, manages gate enablement per branch)
- DevX platform (owns deployment/integration data)
- Jenkins (handles quick validation checks)
- Apache Airflow (orchestrates longer-running jobs)
- Grafana (analytics on gate performance, PR times)
- MongoDB (raw pipeline data on-prem)
- Chat/NLP layer (Claude or similar via DeepSight)

**Stakeholders**
- **BayOne:** Colin Moore, Web developers, Senior AI Engineer
- **Cisco:** Divakar (Jenkins/CAT owner), Srinivas (AI platform), other team leads for DevX/Airflow/Grafana

**Notes/Context**
- Described as foundational—everything else depends on this unified data layer
- Originally proposed as Phase 1 but deprioritized to Phase 2 to start with A+F for quicker wins
- High impact on developer experience
- API documentation quality will significantly affect timeline (add 30-50% if APIs poorly documented)
- Development hours estimate: 180-250 hours

---

### WORK STREAM D: Coverage Tracking Enhancement

**Description/Objective**
Confirm that specific code changes in a PR (at the condition level, not just function level) were actually exercised by tests before merge. Close gaps in existing CDT (Context Driven Testing) coverage confirmation.

**Status**
Planned (Phase 4, depends on Phases 1 and 2)

**Key Deliverables**
- Condition-level coverage confirmation system
- Integration with CDT (2+ years live, provides function→test mapping)
- PR-level coverage gap identification
- Developer feedback on untested code changes
- Coverage dashboard/reporting

**Technical Paths/Components**
- CDT (Context Driven Testing) system (already live, 2+ years)
- Developer Box instrumentation (Phase 1 output)
- Unified data layer (Phase 2 output)
- Test execution data from Developer Box
- Code change analysis (diff comparison)

**Stakeholders**
- **BayOne:** Colin Moore, Web developers, Junior AI Engineers
- **Cisco:** Srinivas (strategy), Divakar (access to code/test systems)

**Notes/Context**
- CDT already provides function→test mapping, but gap exists in tracking whether specific conditions are exercised
- Described by Cisco as "mostly solved" but they cannot confirm if specific code changes were tested
- Requires clarification: what does CDT lack that they need?
- Depends on Phase 1 (Developer Box data) and Phase 2 (unified access)
- Development hours estimate: 80-120 hours

---

### WORK STREAM E: Self-Healing / Automated Corrective Actions

**Description/Objective**
For failures that don't require human judgment (e.g., transient errors, copyright check fixes), allow the system to automatically retry or apply simple corrections. Requires governance framework to define what actions are allowed and safety mechanisms for rollback.

**Status**
Planned/Deferred (Phase 5, most complex, addressed after deeper environment understanding)

**Key Deliverables**
- Governance framework defining auto-correctable failures
- Automated retry logic for transient failures
- Simple auto-fix implementations (e.g., copyright headers, formatting)
- Action triggers in Jenkins/Airflow
- Safety mechanisms and rollback capabilities
- Testing and validation framework for autonomous actions

**Technical Paths/Components**
- Jenkins (executes actions)
- Apache Airflow (orchestrates workflow changes)
- Safety/governance rules engine
- Rollback system with state tracking
- Logging and audit trail for autonomous actions
- Possibly agentic AI system for decision-making

**Stakeholders**
- **BayOne:** Colin Moore, Senior AI Engineer, Agentic AI specialist
- **Cisco:** Anand (Director, governance sign-off), Srinivas (AI strategy), Divakar (pipeline execution)

**Notes/Context**
- Highest complexity and risk—essentially building an agentic AI system that takes real actions in production
- Was originally Phase 3 but deferred due to complexity
- Overlaps significantly with Cisco's internal AI code review project (boundary unclear)
- Estimate likely understated: 300-500 hours (up from original 150-250 hours)
- Governance framework definition must happen with Cisco before implementation
- Risk assessment and safety testing requirements will be substantial

---

### WORK STREAM F: Branch Health / CD Health Dashboards

**Description/Objective**
Provide release leads with consolidated visibility into branch health, failure trends, and blockers. Identify which PRs/changes contributed to issues and automatically trigger follow-up notifications or assignments based on failure conditions.

**Status**
In-progress (Phase 1 starting, with Developer Box A)

**Key Deliverables**
- Branch health consolidated dashboard
- Build status and failure trend visualization
- PR/change attribution for failures
- Automated follow-up triggers (notifications, assignments, escalations)
- Release lead operational dashboards
- Historical trend analysis

**Technical Paths/Components**
- Grafana (analytics already exist, leverage for visualization)
- MongoDB (raw build/branch data)
- MySQL-based services (aggregated metrics)
- Build/integration data from Official Build/DC BU zone
- Attribution system (which PR caused failure)
- Notification/assignment system (Jira integration or custom)

**Stakeholders**
- **BayOne:** Colin Moore, Web developers
- **Cisco:** Anand (Director, release strategy), Srinivas (strategy), Divakar (build systems)

**Notes/Context**
- Selected as Phase 1 starting point (with Developer Box A) for quick wins
- Initially uses existing Grafana dashboards as foundation, full integration with unified data layer comes later
- Can deliver value early while building familiarity with Cisco systems
- Less complex than unified interface (C) but high impact for release leads
- Development hours estimate: Part of Phase 1 (150-210 combined with A)

---

## CROSS-CUTTING CONTEXT

### Pipeline Infrastructure (Three Zones)

1. **Developer Box (Blue Box):** Local development environment, currently opaque to organization
2. **GitHub/DevX (Green Box):** PR validation through 39 gates via Jenkins/Airflow, orchestrated by CAT
3. **Official Build/DC BU (Red Box):** Integrated builds, QA, release management

### Key Technical Platforms

- **Existing:** CDT (Context Driven Testing, 2+ years live), pyATS (test automation), Grafana (analytics), CAT (gate enablement), Jenkins, Apache Airflow, MongoDB (on-prem), MySQL, Splunk (security team)
- **New/Internal:** DeepSight AI platform (live in 2-3 weeks as of Feb 17), CICD application (Rui leading on Arun's team)
- **Infrastructure:** Podman containers (Red Hat), ADS machines (Linux, on-prem), Bazel (recently rolled out to production)

### Phasing Strategy (Jan 16 Decision)

**Phase 1:** A (Developer Box) + F (Branch Health) → 150-210 dev hours
**Phase 2:** C (Unified Interface) → 180-250 dev hours
**Phase 3:** B (Gate Failures/AI Diagnosis) → 100-150 dev hours
**Phase 4:** D (Coverage Tracking) → 80-120 hours
**Phase 5:** E (Self-Healing) → 300-500 dev hours
**Total:** 810-1,230 dev hours over ~6-8 months (sequential phases)

### Budget & Resourcing

- **Budget:** $100K per quarter (starting baseline, increases justify needed)
- **Initial Team:** 1-1.5 FTE onshore (Bay Area), 4-5 offshore resources to scale
- **Discovery Phase:** 1-2 weeks (40-80 hours)
- **Skills Needed (per Rahul/Colin discussion):**
  - Agentic AI experience (especially for Phase 5)
  - Airflow expertise (single biggest integration point)
  - Web development (frontend, backend, Docker experience)
  - Senior AI Engineer
  - Platform/integration engineers

### Key Unknowns / Open Questions

1. What API documentation quality exists for CAT, DevX, Jenkins, Airflow?
2. Exact data schema/format from each system
3. Data retention policies (how far back can historical analysis go?)
4. Governance framework scope for self-healing actions
5. Boundary between BayOne work and Cisco's internal AI code review project
6. Development environment repository/code commit workflow for BayOne code
7. Specific failure patterns that dominate (for diagnosis prioritization)
8. Complete roster of the 39 gates and their classification (transient vs. structural failures)
9. User research on "what questions should the chat interface answer?"
10. Infrastructure provisioning model (self-service vs. IT-provisioned)

### Key Stakeholders & Roles

**BayOne Leadership:**
- **Colin Moore** – Director of AI, Technical Lead (onsite starting mid-Feb)
- **Rahul** – President, budget/resourcing authority
- **Amit** – Delivery lead, SOW/estimation
- **Zahra** – Sales, scheduling

**Cisco Leadership:**
- **Arun** – VP, sponsor level, budget authority
- **Anand** – Director, project coordination, escalation path, governance decisions
- **Srinivas/Srini** – Senior Engineering Manager, AI strategy, DeepSight platform owner
- **Divakar/Diwakar** – Engineering Lead, day-to-day access, Jenkins/build owner
- **Rui** – Arun's team, leads existing CICD app on DeepSight (coordinate with)

### Related Initiatives (SOW Document Work)

A separate SOW document (for Nexus 9000 switches, refs #33282) is being formatted and standardized ($4.39M INR, Nov 2025-Apr 2026). This is parallel infrastructure work for Cisco, not part of the CI/CD engagement but shows BayOne's SOW delivery process maturity.

---

**Report Compiled:** March 17, 2026
**Source Documents Reviewed:** 15+ files including engagement status, development estimates, discovery call notes, meeting summaries, historical records, SOW context, and stakeholder instructions.
