# Proposed Plan: EPNM-EMS POC Handoff Package Preparation

**Author:** Claude (preparing handoff for a separate Claude session)
**Date:** 2026-04-20
**Status:** AWAITING FINAL APPROVAL — do not execute Phase A until Colin approves this revised plan.

---

## 1. Objective

Produce a complete, self-contained handoff package inside `cisco/epnm_ems/poc/handoff/` that gives a new Claude session everything it needs to walk into the EPNM → EMS/CNC UI conversion **POC** cold and be fully oriented. The new session will have unadulterated access to both the EPNM repository and the EMS/CNC repository. The handoff package is their "desert island supply pack."

### Scope Boundary

This is a **POC engagement covering exactly two screens** from the EPNM product. The handoff package must communicate the context and scope of this POC only. The larger engagement it sits within exists as a single-line contextual note; nothing more.

### Non-Objectives (Explicit Exclusions)

- NO timelines of any form.
- NO hour estimates.
- NO complexity or effort estimates.
- NO commercial detail whatsoever — no dollar figures, no rate structures, no margin language, no pricing strategy, no deliverable-timing commitments.
- NO prescriptive "how to" implementation guidance unless Colin has stated it personally.
- NO invented workstreams, modules, or decomposition the transcripts did not themselves establish.
- NO reading of `archive/` contents — duplicate material, confirmed to contain nothing unique of value.

---

## 2. Guiding Principles

- Chronological, blockchain-aware reading — the research library is structured as an append-only chain. Summaries, topic maps, and bridge (`NN-NN_changes`) documents give the arc; deep-dives give specifics. Read in order.
- Read every relevant file — no skimming, no pattern shortcuts.
- No pattern matching, regex heuristics, or grep during exploration. Reading only.
- Parallel general-purpose agents (not Explore agents — they cannot write) for deep-dive reads. Each agent writes its own scratch extraction file.
- Pilot-first agent spawning — one agent first, verify it can write files to the expected path, then scale the rest in parallel.
- Restate only what the transcripts established. When the source material leaves something undefined, the handoff documents leave it undefined and flag it as an open item. No extrapolation, no fabrication, no invented module names or workstream labels.

---

## 3. Decisions Locked (answers to the four open questions)

1. **Action plan granularity.** High-level work items at the granularity the transcripts themselves established. No invented tickets, no prescribed methodologies, no fabricated decomposition. The new session will fill in execution detail from the repositories.
2. **Commercial detail.** Strip entirely. No pricing, no margins, no commercial shape, no engagement-level timelines or deliverable commitments. Scope for the POC is two screens; that is the only commitment surface that enters the handoff.
3. **Final handoff location.** `cisco/epnm_ems/poc/handoff/`.
4. **Archive folder.** Excluded entirely at every phase. Confirmed duplicate-only, no unique ground truth.

---

## 4. Phase Breakdown

### Phase A — Foundational Narrative Read (I do this myself, sequential)

Goal: Absorb the complete engagement arc before any delegation.

Reading order (strict chronology):

1. `research/00_methodology_2026-02-09.md`
2. Set 01 anchors: `01_meeting_topic_map`, `01_meeting_summary`, `01_meeting_people`
3. `research/01-02_changes_2026-02-20.md`
4. Set 01a: `01a_call_prep_summary`, then `01a_call_prep_discovery_strategy`
5. Set 02 anchors: `02_meeting_topic_map`, `02_meeting_summary`, `02_meeting_people`
6. `research/02-03_changes_2026-03-25.md`
7. Set 03 anchors: `03_meeting_topic_map`, `03_meeting_summary`, `03_meeting_people`
8. `research/03-04_changes_2026-03-26.md`
9. Set 04 anchor: `04_discussion_summary` (read for scope-shaping content only; ignore pricing mechanics)
10. `research/04-05_changes_2026-03-30.md`
11. Set 05 anchors: `05_internal_call_summary`, `05_internal_call_people`, `05a_notes_summary` (scope-shaping content only; ignore pricing mechanics)
12. `research/05-06_changes_2026-04-02.md`
13. Set 06 anchor: `06_discussion_summary` (scope-shaping content only; ignore pricing mechanics)
14. `research/06-07_changes_2026-04-06.md`
15. Set 07 anchors: `07_meeting_topic_map`, `07_meeting_summary`, `07_meeting_people`
16. Set 08 anchor: `08_research_summary`
17. `planning/session_plan_2026-04-07.md`
18. `planning/session_handoff_2026-04-07.md`
19. `org_chart.md`

~19 files. Once read, I have the full engagement arc and can brief each Phase C agent precisely.

### Phase B — Pilot Agent (single, write-verification gate)

Spawn ONE general-purpose agent with Write permission. Assignment:

- Read the four most critical deep-dives from Set 07 (the 2026-04-06 technical meeting):
  - `07_meeting_architecture_and_repositories_2026-04-06.md`
  - `07_meeting_product_walkthrough_inventory_2026-04-06.md`
  - `07_meeting_product_walkthrough_faults_2026-04-06.md`
  - `07_meeting_ai_compliance_and_tooling_2026-04-06.md`
- Write a structured extraction to `cisco/epnm_ems/poc/handoff/_scratch/agent_01_set07_core.md` with sections: Architecture, Repositories, Inventory Walkthrough, Faults Walkthrough, AI Compliance Rules, Tooling Constraints, Verbatim Scope Commitments, Open Items.
- Report back with the path it wrote to and a brief summary.

Verification gate: confirm the scratch file exists at the expected path with substantive content before spawning Phase C.

### Phase C — Parallel Deep-Dive Agent Swarm

Only after Phase B succeeds. Each agent writes to `cisco/epnm_ems/poc/handoff/_scratch/agent_NN_<label>.md`. All agents spawned in a single message for true parallelism.

| Agent | Scope | Files to Read |
|-------|-------|---------------|
| 02 | Set 01 deep-dives | `01_meeting_business_drivers`, `01_meeting_technical_landscape`, `01_meeting_bayone_methodology_presentation`, `01_meeting_security_and_access`, `01_meeting_next_steps_and_expectations` |
| 03 | Set 02 deep-dives | `02_meeting_problem_definition`, `02_meeting_domain_gap_and_quality_assurance`, `02_meeting_engagement_model_and_constraints`, `02_meeting_poc_scope_and_success_criteria`, `02_meeting_next_steps` |
| 04 | Set 03 deep-dives | `03_meeting_scope_reframe`, `03_meeting_poc_planning`, `03_meeting_next_steps` (NOT `03_meeting_july_timeline_and_costing` — commercial-only) |
| 05 | Scope-only extraction from pricing-heavy sets | `04_discussion_pricing_strategy`, `05_internal_call_pricing_decisions`, `05a_notes_venkat_positioning`, `06_discussion_pricing_breakdown`, `06a_discussion_pricing_refinement_language`, `06b_gap_analysis_breakdown_vs_transcripts`, `06c_gap_resolution_decisions`. Agent is explicitly instructed to IGNORE all commercial detail and extract ONLY scope-shaping decisions, POC boundary changes, or positioning language that affects what the two screens need to be. Expected output may be short. |
| 06 | Set 07 remaining deep-dives | `07_meeting_testing_and_qa_approach`, `07_meeting_access_and_next_steps` |
| 07 | Set 08 research | `08_research_epnm_legacy_stack`, `08_research_ems_modern_stack`, `08_research_conversion_patterns` |
| 08 | Source ground-truth pass | `source/ceo_rahul_call_2026-03-30_formatted.txt`, `source/venkat_notes_2026-03-30.txt`, `source/selva_and_team_4-6-2026_formatted.txt`, and the two PNG screenshots from 4-6. Extract only what is NOT captured in research and is scope/technical-relevant (explicitly ignore pricing and internal commercial color). |

No agent is assigned to the `deliverables/` or `pricing/` folders. Their contents are either commercial (excluded) or formally-committed scope that is already restated in the research library. If Phase A reveals a scope commitment that only lives in a deliverable file, I will read that single file myself.

Agents 02–08 spawn concurrently after pilot verification. Seven agents total in the swarm.

### Phase D — Synthesis Into Final Handoff Documents

I read every scratch extraction, integrate with Phase A narrative, and write the final handoff package. All documents under `cisco/epnm_ems/poc/handoff/`:

| # | Filename | Purpose |
|---|----------|---------|
| 00 | `00_index.md` | Navigation entry point. What each doc contains, reading order, quickest-start path. |
| 01 | `01_project_overview.md` | The "why we're here" document — deep, narrative, in detail. What EPNM is, what EMS/CNC is, the conversion mission, the Cisco organizational context, the two-screen POC scope, why this matters. Master anchor document. |
| 02 | `02_engagement_history.md` | Chronological arc of how the POC scope came to be, from 2026-02-09 through 2026-04-06. Scope evolution, key scope decisions, major shifts. No commercial events. |
| 03 | `03_objectives_and_scope.md` | What success looks like for the POC. The two screens (names, what they do, why selected). Success criteria as established by Cisco. Explicit scope boundaries. |
| 04 | `04_strategic_approach.md` | The conversion approach as articulated in the transcripts — to the level of detail the transcripts established. No inventions. |
| 05 | `05_technical_landscape.md` | EPNM legacy stack and EMS/CNC modern stack as captured in research. Known surface area. Walkthrough findings. |
| 06 | `06_conversion_patterns_reference.md` | The Set 08 conversion pattern research, presented as a working reference. |
| 07 | `07_stakeholders_and_organization.md` | Cisco-side people and roles, BayOne-side people and roles, decision authority, relationship dynamics and sentiments. |
| 08 | `08_repositories_access_and_compliance.md` | EPNM repo context, EMS/CNC repo context, access path, AI compliance rules, tooling constraints, secrets handling. |
| 09 | `09_work_items.md` | High-level work items at the granularity the transcripts established. No invented tickets, no prescribed decomposition, no timelines, no estimates. The new session fills in execution detail from the repositories. |
| 10 | `10_open_questions_and_risks.md` | Known unknowns, items awaiting Cisco response, risks flagged during discovery, anything the new session should raise rather than guess about. |
| 11 | `11_ways_of_working.md` | How BayOne operates in this engagement, what to escalate to Colin, what to decide autonomously, how to document progress going forward. |

12 documents. Doc formerly numbered #09 (prior_client_commitments) was dropped per decision #2 — scope lives in doc 03; there is no separate commercial commitments doc.

### Phase E — Cleanup and Final Review

- Verify every final handoff doc cites its research-file source where applicable.
- Verify `00_index.md` references all final docs.
- Present final package location to Colin. Delete `_scratch/` only after Colin confirms nothing to preserve.

---

## 5. Delegation Boundaries

**Delegated to agents:** bulk reading and structured extraction of individual document sets.

**Not delegated (mine alone):** synthesis into final handoff documents; every judgment call about what to include, exclude, emphasize, or characterize.

---

## 6. Approval Gate

Upon Colin's approval of this revised plan, I will:

1. Begin Phase A.
2. Execute Phase B (pilot agent).
3. Await pilot verification before Phase C.
4. Execute Phase C swarm, then Phase D synthesis, then Phase E cleanup.
