# Cisco Engagement Context for Capabilities Deck

## Summary

The Cisco CI/CD engagement is a live project with BayOne, focused on NX-OS pipeline improvements. This provides a concrete, ongoing case study that demonstrates BayOne's capabilities in action.

---

## Engagement Overview

**Client:** Cisco (NX-OS division)
**Sponsor:** Arun (VP)
**Key Contacts:** Srini (Sr Engineering Manager), Anand (Director), Divakar (Engineering Lead)
**Budget:** $100K/quarter starting point
**Staffing Model:** 1-1.5 FTE onshore + 4-5 offshore

---

## Problem Statement

Cisco operates a multi-stage CI/CD pipeline for NX-OS with three zones:
1. Developer Box (local dev, "black box")
2. GitHub/DevX (39 gates via Jenkins + Airflow)
3. Official Build/DC BU (integrated builds, QA, release)

**Core Problem:** Engineers lack unified, intelligent view of work moving through pipeline. Status fragmented, failures require manual investigation, no AI-driven interface.

---

## Prioritized Work Items (Cisco Selected)

**Phase 1 (Active):**
- **A: Developer Box** - Telemetry, coverage tracking, AI-assisted debugging
- **F: Branch Health** - Dashboards, failure attribution, automated follow-up

**Deferred:**
- C: Unified interface / single pane of glass
- B: Gate failure diagnosis
- D: Coverage tracking
- E: Self-healing (most complex)

---

## Existing Cisco Assets

- CDT (Context Driven Testing) - 2+ years live
- Grafana dashboards
- pyATS test automation
- Jenkins + Apache Airflow orchestration
- CAT (Commit Approval Tool)

---

## Direct Alignment with BayOne Capabilities

| Cisco Need | BayOne Capability | Use Case # |
|------------|-------------------|------------|
| AI-assisted debugging | Agentic AI for DevOps | #2 |
| Failure diagnosis | Automated Code Review & QA | #2 |
| Self-healing systems | Intelligent Automation | #4 |
| Unified interface | Enterprise Tool Integrations | #5 |
| Branch health dashboards | Data Pipeline + BI Agents | #8, #9 |
| Coverage tracking | ML for observability | #17 |

---

## Mirel's Separate Opportunity (Cisco)

Mirel is a Director under Guhan at Cisco, leading "Coarse AI" (formerly Foresight):
- Next-gen agentic AI platform for CNC, NSO, future products
- SDK for custom agent development
- First release: December 2025

**Her Team's Skill Gaps:**
- No AI/ML engineers (all self-taught internally)
- Needs: RAG architecture, vector stores, agent orchestration, AI UX, knowledge graphs

**What She Wants from BayOne:**
- Flexible AI/ML + Agent Engineering Pod
- Multi-role team (AI, Data, Full-stack, UI)
- Long-term partnership

**Key Quote:** "If anything changes, you are my first call."

---

## Implications for Capabilities Deck

1. **Live Case Study:** Cisco CI/CD engagement can be referenced (with care about specifics) to show active enterprise work

2. **Demonstrates Technical Depth:**
   - Agentic AI for DevOps
   - CI/CD pipeline integration
   - Multi-system data consolidation
   - Self-healing capabilities

3. **Shows Operating Model:**
   - Onshore/offshore hybrid
   - Discovery-first approach
   - Build on client's existing stack
   - Startup mindset (Anand's requirement)

4. **Resonates with Cisco VP Audience:**
   - Deck will be shown to Arun (VP) or similar
   - CI/CD pain points are universal in large engineering orgs
   - Shows BayOne understands their world
