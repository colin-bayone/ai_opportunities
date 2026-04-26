# 09 - Meeting: Summary

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting between BayOne lead and Cisco leadership)
**Pass:** Summary of all Set 09 documents

---

## Overview

Late-Friday status check-in. Five attendees: Guhan, Selva (Cisco) and Colin, Neha, Zahra (BayOne). Selva opened with extended rapport-building; Guhan joined late after a back-to-back with Zahra earlier in the day. Colin reported that the POC conversion is done, that final tests are the only remaining work (gated on VM access), and disclosed that an unplanned side-effect of the work is a complete 14-repository system mapping with bidirectional gap analysis. Guhan responded with three significant asks (memory/load review, DPM coverage, code review before demo) and stated the engagement's commercial unlock out loud.

## Key Takeaway

**Two parallel narratives now exist.** The POC narrative — toggle conversion of inventory and fault management screens — is essentially complete and ready for demo. The full-scope narrative — converting the entire EPNM-to-EMS surface area — has been substantially de-risked by the comprehensive mapping Colin produced as a side effect. The two narratives are now decoupled: the POC can be demoed and validated on its own terms, while the mapping work positions BayOne for the full-scope conversation that Guhan signaled is coming ("you can go promise the customers").

## Documents in This Set

| File | Focus |
|------|-------|
| `09_meeting_people_2026-04-24.md` | 5 attendees confirmed. Transcription artifacts identified ("Anu" not real, "Aya" = Neha, "Zara" = Zahra). Guhan and Selva profiled at high level. |
| `09_meeting_topic_map_2026-04-24.md` | 6 topics + Guhan/Selva deep-dive request from Colin. File-list rationale documented. |
| `09_meeting_poc_status_and_toggle_implementation_2026-04-24.md` | Conversion done. Toggle as bolt-on parallel packages. Code on GitHub branches `agentic UI conversion` off `develop`. Auditability designed in: commit attribution, in-line decision rationale. |
| `09_meeting_full_system_mapping_2026-04-24.md` | 14 repos mapped, bidirectional, UI + backend + data. 42 backend gaps. ~250 docs. The strategic centerpiece of the set. |
| `09_meeting_guhan_scope_signals_and_asks_2026-04-24.md` | Three asks: memory/load review, DPM coverage, product-management positioning. The commercial unlock quote captured verbatim. |
| `09_meeting_demo_and_code_review_planning_2026-04-24.md` | Demo Wed → possibly Thu. Code review with India team inserted before demo. Time-zone window. Tuesday touch-base. |
| `09_meeting_access_and_final_test_gating_2026-04-24.md` | VM access is the only remaining external dependency. Playwright agentic test suite ready. Database seed workaround via meeting-recording screenshots. |
| `09_meeting_architectural_debt_observations_2026-04-24.md` | Debt observed during mapping (columns example, bookmarks example). Distinct value lever from gap analysis. Future-engagement positioning. |
| `09_meeting_guhan_selva_deep_dive_2026-04-24.md` | Comprehensive profiles: what each said, asked, requested. Engagement styles, recommendations for working with each. |

## Bridge Document

| File | Focus |
|------|-------|
| `08-09_changes_2026-04-24.md` | Set 07 → Set 09 (Set 08 was research). Full-system mapping retired the largest unknown for the future-scope engagement. Three new Guhan asks. Commercial unlock surfaced. |

## Critical Facts Established (New in Set 09)

1. **POC conversion is complete.** Inventory and fault management screens converted with toggle implementation. Final tests pending VM access.
2. **14-repository system mapping exists.** Bidirectional gap analysis covering UI, backend, data sources. 42 backend gaps quantified. ~250 documentation files. Available on GitHub on `agentic UI conversion` branches.
3. **Toggle hits same backend.** Confirmed by Selva on the record with Guhan present. No backend forking. Angular preserved in EMS.
4. **Memory and load review is a gate.** Guhan wants the EMS team to assess generated-code resource consumption before demo.
5. **DPM (Device Performance Management) is in the gap analysis** but not in POC scope. Guhan flagged it as customer-critical.
6. **Commercial unlock stated out loud.** Guhan will take the work to product management for customer commitment authorization.
7. **Code review before demo.** Demo possibly slips to Thursday to accommodate code review with India team first.
8. **Architectural debt is a distinct value lever.** Same things done multiple ways in EMS; observed but deliberately not fixed during POC.
9. **Access narrowed to one item.** Only VMs remain; everything else self-resolved by Colin during the week.
10. **BayOne's repo inventory exceeds Cisco's central documentation.** Colin's agentic process picked up implicit dependencies the Confluence page did not list.
11. **Cost transparency.** Colin maxed out his Cisco Claude Code subscription daily through the conversion week.
12. **Selva and Guhan profiled in depth.** Engagement styles, validation patterns, asks, recommendations for future interactions captured in dedicated reference document.

## Open Questions After Set 09

1. What does Cisco need to take to product management? (Format, audience, depth)
2. Who in the EMS team conducts the memory/load review?
3. What is Guhan's exact title and reporting line? (Still TBD from Set 07)
4. Should BayOne pre-build a DPM gap brief for the demo?
5. Will the demo include the full mapping reveal, or stay scoped to the POC?
6. What is the "good vs. great" answer Selva will ask for again?
7. When does pricing get revisited given the de-risked full-scope?
8. Tuesday touch-base agenda with Selva.
