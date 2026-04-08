# 07 - Meeting: Summary

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting — first meeting with Cisco engineering team)
**Pass:** Summary of all Set 07 documents

---

## Overview

First meeting with the Cisco engineering team. 12 attendees (8 Cisco, 4 BayOne). Selva introduced the team and context, then tech leads demonstrated the EPNM product live and walked through the repository structure. Colin saw the product for the first time. Ramesh asked detailed questions about AI compliance and testing. The meeting was operationally substantive and moved the engagement from planning to execution.

## Key Takeaway

The POC scope is now fully concrete. Two functional areas are confirmed: inventory (network devices, device 360, device details) and fault management (alarms, events, syslogs). The backend is ~80% reimplemented in EMS already, validating the classic view toggle approach. The EMS stack is Angular 21 with Spring Boot/Go backend and Postgres. Code lives across specific repositories now known by name. AI compliance was addressed satisfactorily. The next steps are access provisioning, VM setup, and Colin beginning code exploration.

## Documents in This Set

| File | Focus |
|------|-------|
| `07_meeting_people_2026-04-06.md` | 12 attendees. 7 new Cisco tech leads identified by name, email, role. Praveen likely = "Varel" from earlier sets. Neha (BayOne) first appearance. |
| `07_meeting_topic_map_2026-04-06.md` | 6 topics identified and file plan. |
| `07_meeting_product_walkthrough_inventory_2026-04-06.md` | Live demo: network devices, device 360, device details, chassis view. Data flow (SNMP/CLI -> Oracle/Postgres -> app). First product visibility for BayOne. |
| `07_meeting_product_walkthrough_faults_2026-04-06.md` | Alarms, events, syslogs. Correlated alarms. Expandable rows. Quick and advanced filtering. Part 2 of POC. |
| `07_meeting_architecture_and_repositories_2026-04-06.md` | 5 EPNM repos, 3 EMS repos. Shell app architecture. Angular 21, Harbor/Magnetic design system. Spring Boot + Go backend. Classic UI code location TBD. |
| `07_meeting_ai_compliance_and_tooling_2026-04-06.md` | Ramesh's compliance questions. Colin: Cisco hardware, Cisco Claude Code, local LangGraph. CICD engagement precedent. Library gating. |
| `07_meeting_testing_and_qa_approach_2026-04-06.md` | Existing test infra: 7 categories, thousands of cases, data-driven. Existing UI tests won't work for classic UI. Playwright agents for automated UI testing. POC vs full engagement QA scope. |
| `07_meeting_access_and_next_steps_2026-04-06.md` | AD group access, VM setup, team space, Confluence page, time zone coordination. 12 action items. |

## Bridge Document

| File | Focus |
|------|-------|
| `06-07_changes_2026-04-06.md` | Strategy to execution. First product visibility. Architecture confirmed. ~80% backend reimplemented. Pricing "full-stack" language now clearly inconsistent with reality. 7 new people. |

## Critical Facts Established (New in Set 07)

1. **First product visibility:** Colin saw EPNM running for the first time.
2. **~80% backend reimplemented** in EMS already.
3. **POC screens confirmed:** Inventory (network devices, device 360, device details) + Fault management (alarms, events, syslogs).
4. **Repository structure known:** 5 EPNM repos, 3 EMS repos, by name and purpose.
5. **EMS stack:** Angular 21, Spring Boot + Go, Postgres, Harbor/Magnetic design system.
6. **Oracle eliminated:** Postgres in EMS.
7. **Shell app architecture:** Infra UI -> Common UI -> EMS UI (nested layers).
8. **AI compliance satisfied:** Cisco hardware, Cisco Claude Code, local LangGraph.
9. **Existing UI tests won't work:** New test replicas needed for classic UI.
10. **Praveen Kumar Vangala** likely = "Varel" from earlier sets.
11. **Confluence page prepared** with user guides, API docs, recordings, repo lists.
12. **Team is India-based** (IST) except Ramesh and Selva (US).

## Open Questions After Set 07

1. When will AD group access and VMs be provisioned?
2. Where should classic UI code live? (Colin to propose)
3. What does the remaining ~20% backend gap look like?
4. What are the exact test suite formats?
5. What is the recurring meeting cadence?
6. Does the pricing model need recalibration given the lighter scope?
7. What happened to the "Cerny" message from Set 03 about another team working on this?
