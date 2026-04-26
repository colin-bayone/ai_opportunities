# 09 - Meeting: Topic Map

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Topic identification and proposed file breakdown

---

## Topics Identified

### T1. POC Conversion Status (Near-Complete)
Colin reported conversion is "ready, done." Final tests are in progress. The toggle is implemented as a simple UI switch that swaps the front end while pointing at the same backend. Implementation kept Angular in place and treated the classic UI as a "bolt-on seamless" parallel package set. EMS is now running on the BayOne side. Branches named `agentic UI conversion` exist on each repository's `develop` branch. Colin specifically architected the work to be auditable by the Cisco team (commits attributed, decisions documented inline with rationale).

**Why a dedicated file:** This is the headline status update and the primary client-facing deliverable preview. Captures what is built, how it is built, where it lives, and what state it is in.

### T2. Comprehensive 14-Repository System Mapping (Scope-Expanding Side Effect)
Colin disclosed that an unintended but consequential outcome of the work was a complete map of the EPNM and EMS systems across all 14 repositories. The mapping is bidirectional (EPNM-to-EMS and EMS-to-EPNM), covers UI components, backend, and data sources, and quantifies gaps. Specific number stated: 42 backend gaps identified. ~250 documentation files generated, mostly machine-readable but also human-readable on GitHub. Colin acknowledged the codebases "look really big at first" but his agentic process broke them down systematically (Java, SQL, XML quantified per repo).

**Why a dedicated file:** This is the most strategically significant content in the meeting. It is a free deliverable (not in scope) that materially changes the BayOne–Cisco conversation about full-scope conversion. Guhan responded by pivoting to product-management positioning. This shifts the engagement narrative.

### T3. Guhan's Scope and Validation Asks
Three distinct asks from Guhan, each significant:
1. **Memory and load review.** Guhan wants Cisco engineering to look under the code at what is generated vs. what runs on the system, to assess additional memory and load. Treating this as a gate.
2. **Performance Management (DPM) coverage.** Guhan asked whether DPM is in the gap analysis. Colin confirmed it is in the gap, just not in POC scope. Guhan signaled this matters for customer commitments.
3. **Promise-to-customers framing.** "Based on this, we are going to go to the product management and say, hey, we got this covered. You can go promise the customers that they will get this functionality." This is the engagement's positioning unlock.

**Why a dedicated file:** These three asks together define the next phase of the engagement. Memory/load is the technical gate; DPM is the scope expansion; product-management positioning is the commercial unlock.

### T4. Demo and Code-Review Planning
Demo originally targeted Wednesday next week. Selva proposed adding a code review with the India team as a precursor, which may push the demo to Thursday. Time-zone constraint: window must work for Colin (EST), Selva (PST), and India team (IST). Guhan's reasoning for code-review-before-demo: any team questions can route back through the team before the formal demo, "free to root" in the work. Selva to coordinate with the India team. Tuesday touch-base proposed.

**Why a dedicated file:** Logistics document with operational decisions and dates.

### T5. Access Status and Final Test Gating
The single remaining blocker: access to virtual machines running EPNM and EMS for live comparative testing. Colin's Playwright agent test suite is ready and waiting. Colin worked around the access gap during the week by using meeting-recording screenshots to seed the database (avoiding bothering the team). All other access items resolved. Selva confirmed access is a Monday agenda item.

**Why a dedicated file:** Operational status item with a clear gate. Worth capturing distinctly because it is the single remaining external dependency.

### T6. Architectural Debt Observations (Optional Future Work)
Colin disclosed he observed architectural debt during the mapping: same things done multiple ways in EMS (he gave the example of how columns are handled in tables). He held off making fixes during the POC but flagged that with the team involved, this kind of cleanup could "go a lot quicker" and "accelerate the timeline even further" for the broader scope. Bookmarks were given as an example of a deferred decision: behaves differently in EPNM vs. EMS, left as-is in EMS for POC because cross-screen impact is global.

**Why a dedicated file:** Captures Colin's discovery-by-doing observations that inform future engagement scoping. Distinct from the gap analysis (which is what is missing) — this is what is present but inconsistent.

---

## Proposed File List

| # | Filename | Topic |
|---|----------|-------|
| 1 | `09_meeting_people_2026-04-24.md` | Attendees (already written) |
| 2 | `09_meeting_topic_map_2026-04-24.md` | This file |
| 3 | `09_meeting_poc_status_and_toggle_implementation_2026-04-24.md` | T1: conversion done, toggle as bolt-on, code locations, branches |
| 4 | `09_meeting_full_system_mapping_2026-04-24.md` | T2: 14 repos, bidirectional gaps, 42 backend gaps, ~250 docs |
| 5 | `09_meeting_guhan_scope_signals_and_asks_2026-04-24.md` | T3: memory/load review, DPM coverage, product-management positioning |
| 6 | `09_meeting_demo_and_code_review_planning_2026-04-24.md` | T4: code review first, demo Wed→Thu, time-zone window, Tuesday touch base |
| 7 | `09_meeting_access_and_final_test_gating_2026-04-24.md` | T5: VM access pending, Playwright suite ready, Monday agenda item |
| 8 | `09_meeting_architectural_debt_observations_2026-04-24.md` | T6: debt observed during mapping, bookmarks example, future scope unlock |
| 9 | `09_meeting_guhan_selva_deep_dive_2026-04-24.md` | T7: focused profile of everything Guhan and Selva said, asked, requested |
| 10 | `08-09_changes_2026-04-24.md` | Bridge document |
| 11 | `09_meeting_summary_2026-04-24.md` | Summary |

That is 10 files total: 8 detail files (including people and topic map) + bridge + summary. Comparable density to Set 07.

---

## Rationale for the Cuts

- **T2 is split out from T1** (not merged into "POC status") because it is a fundamentally different artifact: T1 is the in-scope POC, T2 is an out-of-scope bonus that reshapes the engagement narrative. Keeping them separate makes the bridge document and future deliverables cleaner.
- **T3 is one file, not three** because Guhan's three asks cluster around the same theme: rigor before customer commitment. Splitting them would dilute the connective tissue.
- **T6 (architectural debt) gets its own file** because it is qualitatively different from the gap analysis. It is observation-based discovery that informs future-engagement positioning, not a deliverable.
- **T5 (access) gets its own file** because it is the only remaining operational gate. Easy to find later when the question is "what was unblocking us."
