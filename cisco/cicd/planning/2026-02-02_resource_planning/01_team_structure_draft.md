# Team Structure – Draft

**Status:** OUTDATED - Kept for reference only
**Last Updated:** 2026-02-02

> **Note:** This document has been superseded by the individual role documents in `planning/roles/`. See those files for current role definitions.

---

## Leadership

| Role | Person | Responsibility |
|------|--------|----------------|
| Technical Lead (Director) | Colin Moore | Overall technical direction, final decisions, veto power |
| Senior Engineer (Onshore) | TBH | Day-to-day offshore management, Cisco interface, reports to Colin |

---

## Core Team Requirements

### All Team Members

- Proficient with AI pair programming tools (non-negotiable)
- Expected to be highly effective and efficient through AI-assisted development

### Technical Requirements

- At least one person with **Apache Airflow experience** (critical integration point)
- Front-end capability for chat interface (Item C)

---

## Proposed Roles

### 1. Senior Engineer (Onshore, Bay Area)

**Location:** On-site at Cisco campus (hybrid acceptable, on-site required)

**Responsibilities:**
- Primary interface with Cisco teams
- Day-to-day guidance and management of offshore team
- Unblock issues, coordinate across Cisco teams
- Hands-on technical contribution
- Reports to Colin

**Skills:**
- Strong communication, can navigate large org
- Technical breadth across backend, integrations
- CI/CD pipeline understanding
- Airflow experience (preferred)

---

### 2. Backend / Integration Engineer (Offshore)

**Responsibilities:**
- Data pipelines and telemetry (Item A)
- API integrations with CAT, DevX, Jenkins, Airflow, Grafana (Item C)
- Backend services

**Skills:**
- Python, data pipelines
- API integration experience
- **Airflow experience** (if onshore person doesn't have it)
- CI/CD familiarity

---

### 3. Front-end Engineer (Offshore)

**Responsibilities:**
- Dashboard development (Items A, F)
- Chat interface UI (Item C)
- Data visualization

**Skills:**
- Modern front-end (React, Vue, or similar)
- Dashboard/visualization experience
- Can work with design specs

**Timing:** Not needed Day 1, but required for Item C and dashboards

---

### 4. AI/ML Engineer (Offshore)

**Responsibilities:**
- LLM integration for chat interface (Item C)
- Failure diagnosis AI (Item B)
- AI-assisted debugging features (Item A)

**Skills:**
- LLM integration experience (not just prompt engineering)
- Python
- Can build production AI features, not just prototypes

---

### 5. Agentic AI Specialist (Offshore)

**Responsibilities:**
- Self-Healing system (Item E)
- Autonomous decision-making logic
- Governance framework implementation
- Safety mechanisms, rollback capabilities

**Skills:**
- System-level AI automation (agentic systems)
- Understanding of governance/safety for autonomous systems
- Experience building systems that take real actions

**Timing:** Primarily needed for Item E (later phases)

---

## Open Questions

1. Does the onshore person need Airflow experience, or can that be offshore?
2. When exactly do we need the front-end engineer? Q1 or Q2?
3. Can AI/ML Engineer and Agentic AI Specialist be the same person, or distinct?
4. What's the right offshore team size to start – 2, 3, or 4?

---

## Notes

- Phases can run in parallel (e.g., start C work while finishing A+F)
- Team ramps over time rather than all hired Day 1
- Specific skills matter more than generic "full-stack" label
