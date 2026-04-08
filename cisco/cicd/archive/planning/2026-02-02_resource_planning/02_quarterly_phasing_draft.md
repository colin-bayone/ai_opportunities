# Quarterly Phasing – Draft

**Status:** OUTDATED - Kept for reference only
**Last Updated:** 2026-02-02

> **Note:** This document has been superseded by the quarterly deliverable documents (`03_q1_deliverables.md` through `06_q4_deliverables.md`). See those files for current quarterly plans.

---

## Overview

| Quarter | Primary Work | Secondary / Parallel |
|---------|--------------|----------------------|
| Q1 | Discovery + A (Developer Box) + F (Branch Health) | – |
| Q2 | C (Unified Interface / Chat) | Possibly start B |
| Q3 | B (AI Diagnosis) + D (Coverage) | Possibly start E |
| Q4 | E (Self-Healing) | Maintenance / iteration |

**Note:** Phases can overlap. Q2 work can start in Q1 if capacity allows. Not strictly sequential.

---

## Q1: Discovery + A + F

### Work

**Discovery (Weeks 1-2):**
- Access, walkthroughs, architecture review
- Understand CAT, DevX, Jenkins, Airflow, Grafana
- Identify integration points and data sources
- Colin can lead this; team learns alongside

**A – Developer Box:**
- Telemetry system to capture local test runs
- Data pipeline to store and surface results
- Pass/fail, duration, coverage metrics
- Some AI-assisted debugging features

**F – Branch Health:**
- Release lead dashboards
- Failure attribution logic
- Automated follow-up triggers
- Can leverage existing Grafana initially

### Team Active

| Role | Active? | Notes |
|------|---------|-------|
| Senior Engineer (Onshore) | Yes | Primary Cisco interface, hands-on |
| Backend/Integration Engineer | Yes | Data pipelines, telemetry |
| Front-end Engineer | Maybe | Dashboards for F, or defer to Q2 |
| AI/ML Engineer | Light | Learning systems, minor AI features in A |
| Agentic AI Specialist | No | Not needed yet |

### Nature of Work

Primarily **platform/integration** – building data pipelines, telemetry, dashboards. Light AI involvement.

---

## Q2: C (Unified Interface / Chat)

### Work

**C – Cross Pipeline / Unified Interface:**
- API integrations with CAT, DevX, Jenkins, Airflow, Grafana
- Data normalization across systems
- Chat interface with natural language queries
- "Where is my PR?" type functionality

### Team Active

| Role | Active? | Notes |
|------|---------|-------|
| Senior Engineer (Onshore) | Yes | Coordination, API work |
| Backend/Integration Engineer | Yes | Heavy API integration, Airflow |
| Front-end Engineer | Yes | Chat interface UI |
| AI/ML Engineer | Yes | NLP for chat, query understanding |
| Agentic AI Specialist | No | Not needed yet |

### Nature of Work

**Platform + AI** – API integrations are foundational, chat interface brings in AI/NLP.

---

## Q3: B + D

### Work

**B – Gate Failures / AI Diagnosis:**
- AI-driven failure analysis from logs
- Root cause identification
- Suggested fixes

**D – Coverage Tracking:**
- Condition-level coverage confirmation for PRs
- Integration with CDT and Developer Box data

### Team Active

| Role | Active? | Notes |
|------|---------|-------|
| Senior Engineer (Onshore) | Yes | Coordination |
| Backend/Integration Engineer | Yes | Coverage integration, data work |
| Front-end Engineer | Moderate | Surfacing results in UI |
| AI/ML Engineer | Heavy | Failure diagnosis is core AI work |
| Agentic AI Specialist | Ramp | Starting to prepare for E |

### Nature of Work

**AI-heavy** – This is where AI diagnosis features really come online.

---

## Q4: E (Self-Healing)

### Work

**E – Self-Healing:**
- Automated corrective actions for qualifying failures
- Governance framework (what can be auto-corrected)
- Action triggers in Jenkins/Airflow
- Safety mechanisms, rollback capabilities

### Team Active

| Role | Active? | Notes |
|------|---------|-------|
| Senior Engineer (Onshore) | Yes | Governance discussions with Cisco |
| Backend/Integration Engineer | Yes | Triggers, Airflow integration |
| Front-end Engineer | Light | UI for governance/visibility |
| AI/ML Engineer | Moderate | Supporting agentic work |
| Agentic AI Specialist | Heavy | Core focus |

### Nature of Work

**Agentic AI + Platform** – Most complex. Building systems that take real actions autonomously.

---

## Phasing Notes

1. **E (Self-Healing) is highest risk** – May extend into Year 2. Governance framework must be defined with Cisco before implementation.

2. **Parallel work possible** – Can start next phase before current phase fully complete.

3. **Team ramps gradually** – Not all roles needed Day 1. Front-end and Agentic specialist join as needed.

4. **Dependencies:**
   - C depends on understanding from A+F
   - B depends on unified data layer from C
   - D depends on Developer Box data from A
   - E depends on all prior phases

---

## Open Questions

1. When does front-end engineer actually need to start? Q1 for dashboards or Q2 for chat?
2. Can Agentic AI work start earlier (Q2-Q3) in parallel?
3. What's realistic for Q4 E scope vs. pushing into Year 2?
