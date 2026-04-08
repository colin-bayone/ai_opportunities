# 03 - Meeting: Summary

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Summary of all Set 03 documents

---

## Overview

Third meeting between Colin (BayOne), Guhan (Cisco), and Selva (Cisco), five weeks after the Feb 20 follow-up. Colin had just received his Cisco laptop the day before. This meeting fundamentally reframed the project scope from what was understood in Sets 01 and 02.

## Key Takeaway

The project is NOT about converting missing functionality from EPNM into EMS. It is about adding a "classic view" toggle to screens that already exist in EMS, allowing operators to switch between the new UX and the familiar EPNM experience. The EMS backend stays unchanged (minor API adjustments excepted). This is a UX overlay problem, not a full-stack conversion. The business driver is customer adoption: operators with 10+ years on EPNM resist the new UX, and Cisco needs them to migrate to EMS for renewal revenue.

## Documents in This Set

| File | Focus |
|------|-------|
| `03_meeting_people_2026-03-25.md` | Guhan set strategic frame then departed; Selva took operational ownership; Venkat referenced as exploring July timeline; Rahul joined from BayOne. |
| `03_meeting_topic_map_2026-03-25.md` | Topics identified, proposed file breakdown. |
| `03_meeting_scope_reframe_2026-03-25.md` | **The most important document.** Full-stack conversion to classic view toggle. Four direct contradictions with Sets 01/02 documented. Toggle lifecycle (local for POC, global for product). Business rationale: adoption, not missing features. |
| `03_meeting_poc_planning_2026-03-25.md` | Faults and inventory as POC screens. Local toggle approach. Exponential decay explanation. Parallelizable workflow. QA/QE agents. Venn diagram mapping. Azure Foundry shown as reference. |
| `03_meeting_july_timeline_and_costing_2026-03-25.md` | Venkat exploring July as a possibility (not pushing). 200-250 total screens. Budget acknowledged but not discussed. Early India resource search suggested. Server-side release risk flagged. |
| `03_meeting_next_steps_2026-03-25.md` | Cisco laptop received. Selva scheduling India team session next week. WebEx space. Local San Jose resource. POC document to be amended. |

## Bridge Document

| File | Focus |
|------|-------|
| `02-03_changes_2026-03-25.md` | **Critical bridge.** Three core hypotheses from Set 02 invalidated: full-stack vertical work, missing functionality focus, and backend reimplementation. Scope entirely reframed. |

## Critical Facts Established (New in Set 03)

1. **Scope reframe:** Classic view toggle on existing EMS screens, not conversion of missing functionality.
2. **Backend stays:** No backend reimplementation. Minor API adjustments only.
3. **POC screens:** Faults and inventory (not missing reports as in Set 02).
4. **Total scope:** 200-250 workflow screens.
5. **Toggle lifecycle:** Local per-screen for POC, global user setting for product.
6. **Business driver:** Customer adoption and renewal revenue, not filling functionality gaps.
7. **Venkat:** Senior leader exploring whether this could fit in the July release (not a deadline).
8. **Hardware resolved:** Cisco laptop received March 24.
9. **Selva as operational lead:** Scheduling team sessions, creating WebEx space, identifying local resources.
10. **India team:** Domain experts are India-based; walkthroughs cross-timezone.

## Open Questions After Set 03

1. What happened to the "missing functionality" scope from Set 02? Was there an internal Cisco decision?
2. Which specific faults and inventory screens will be selected?
3. What is the boundary between "minor API adjustment" and backend change?
4. What budget is available for the full engagement beyond the POC?
5. Who is the local San Jose resource Selva is identifying?
6. "Cerny" sent a message about another team working on this area — what does that mean?
7. Does Venkat's July interest align with the reframed toggle scope?
