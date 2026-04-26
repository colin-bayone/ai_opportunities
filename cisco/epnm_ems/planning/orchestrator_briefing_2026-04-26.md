# Orchestrator Briefing — Cisco EPNM-to-EMS POC

**Audience:** Claude orchestrator session running on the Cisco-issued machine, currently coordinating the actual build work for the EPNM-to-EMS POC.
**Author session:** Claude session running on Colin's BayOne laptop. Has full access to the engagement research library at `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/`.
**Briefing date:** 2026-04-26 (Saturday)
**Briefing purpose:** Operational handoff. Captures everything from the April 24 status check-in with Guhan and Selva that affects how the build, test, commit, and demo phases should proceed. Read this fully before continuing work. Companion file: `09_meeting_guhan_scope_signals_and_asks_2026-04-24.md` (people-focused; this file is action-focused).

---

## Read these files before continuing

If anything below is unclear or contradicts something in the broader engagement record, the research library is authoritative. Read in this order:

1. `cisco/epnm_ems/research/09_meeting_summary_2026-04-24.md` — Set 09 set-level summary
2. `cisco/epnm_ems/research/09_meeting_guhan_selva_deep_dive_2026-04-24.md` — full profiles of the two Cisco stakeholders
3. `cisco/epnm_ems/research/09_meeting_guhan_scope_signals_and_asks_2026-04-24.md` — Guhan's three asks decomposed
4. `cisco/epnm_ems/research/08-09_changes_2026-04-24.md` — bridge document
5. `cisco/epnm_ems/research/07_meeting_summary_2026-04-06.md` — prior meeting context (architecture, repos, team)
6. `cisco/epnm_ems/org_chart.md` — current people state

This briefing pulls the operationally relevant subset from those, but they are the source of truth.

---

## Engagement state, honestly

### What was communicated to Cisco on April 24

Colin told Guhan and Selva that the POC is "ready, conversion is done; we are just doing our final tests" and that the only remaining gate is access to virtual machines for live comparative testing. This positioning is on the record and is the bar the work needs to land at.

### Actual state as of the start of the weekend

The conversion is in late-stage build. It is NOT done. Colin chose forward-leaning framing in the meeting deliberately (preserves Cisco confidence at a Friday-evening status check, multiple days of runway remain, on-track work). The orchestrator's job for the weekend and through Tuesday is to close the gap so the communicated state and the actual state align.

This gap is the most important context for prioritization. Treat the Friday framing as a commitment to land by Tuesday, not as a description of current state.

### Demo timeline

- **Mon Apr 27:** Cisco-side VM access provisioned (per Selva). Comparative validation testing can begin.
- **Tue Apr 28:** Touch-base call between Colin and Selva. Demo slot locks. Code review window confirmed.
- **Wed Apr 29:** India team code review (developer-to-developer; Guhan not required).
- **Wed-Thu Apr 29-30:** Demo with Guhan, Selva, India team. Time-zone window: PST morning / EST midday / IST evening.

The build needs to be demonstrably done by end-of-day Monday. The India team will be reading the commits Tuesday-Wednesday.

---

## Build priorities through Tuesday

In order:

1. **Close out remaining conversion work on inventory and fault management screens.** Inventory: network devices, device 360, device details. Fault management: alarms, events, syslogs. Toggle behavior on each. Match EMS visual and behavioral parity in the toggle's classic-view mode.

2. **Wire a local-staged comparative test harness.** The Playwright agentic test suite is built and waiting. Instead of waiting strictly on Monday VM provisioning, wire the tests against locally-staged data so testing is not gated on Cisco-side VMs. If Monday VMs are delayed, work continues. If they land on time, swap targets and run against live instances.

3. **Self-review the generated output for memory and system load.** Guhan asked for an explicit code review with the Cisco EMS team that evaluates how much memory the converted UI consumes and how much additional load it puts on the system. Pre-empt this review. Walk through the generated code with resource impact in mind. Look for: bundle-size inflation, unnecessary runtime dependencies, redundant DOM traversal, memory leaks in toggle-state management, render-thrashing on switch. Document any findings in a short markdown note in `cisco/epnm_ems/planning/` so Colin can surface anything notable on his terms before the EMS team finds it.

4. **Maintain the audit-ready commit pattern across all remaining commits.** See "Audit-ready commit pattern" below for specifics. The India team is reviewing these commits, and the integrity of the audit pattern is itself part of the deliverable.

5. **Update the gap analysis documentation if anything new is discovered during the close-out.** The 14-repo mapping is the strategic centerpiece of this engagement. Any discoveries during build close-out that refine the gap picture should be reflected in the mapping docs on the corresponding `agentic UI conversion` branches.

---

## Out of scope (do not touch)

The orchestrator should not, under any circumstance, expand scope into these areas:

1. **Bookmarks behavior change.** Bookmarks have a different conceptual model in EPNM vs. EMS. The decision is on record: port them as-is from EMS for the POC. Cross-screen impact makes it incompatible with POC scope. If the temptation arises to "fix" bookmarks behavior to match EPNM during a screen conversion, do not. Note the inconsistency in the gap analysis if it is not already there.

2. **Architectural debt fixes.** During the mapping, Colin observed that the same things are done multiple ways in EMS (column handling in tables given as the canonical example). These are real opportunities, but they require team involvement and are explicitly held back from the POC. Do not silently fix architectural patterns. Log them in a debt register if discovered, but do not modify production code to address them.

3. **Device Performance Management (DPM).** DPM is a separate functional area beyond inventory and fault management. It is in the gap analysis but NOT in POC scope. Do not start converting DPM screens. Do not extend the toggle to DPM. If working on shared infrastructure that DPM also uses, make changes that are POC-screen-scoped only.

4. **Additional screens beyond inventory and fault management.** The POC scope is explicitly the two functional areas: inventory (network devices, device 360, device details) and fault management (alarms, events, syslogs). Do not convert additional screens "for completeness." If a screen is needed to support the toggle infrastructure, do the minimum.

5. **EMS Angular code modification.** The toggle ships as parallel packages alongside existing EMS Angular code. The committed architecture is "we kept everything exactly as it is in EMS. We weren't trying to reinvent the wheel too much in the POC." Do not refactor existing EMS code. Do not add abstractions in EMS to support the toggle. Bolt-on, not invasive.

6. **Backend changes.** The toggle hits the same backend as the modern UI. Selva validated this on the record with Guhan present: "Identically the same." Do not modify backend services, controllers, or contracts. If a backend change appears necessary, that is a sign the front-end conversion has gone off course — stop and have Colin look.

---

## Audit-ready commit pattern

The Cisco India team will review these commits. The pattern is part of the deliverable. Apply consistently:

### Commit attribution
Commits should be authored such that the Cisco team has clear ownership semantics. Colin established this in earlier work — preserve it. Each commit author and committer field, message metadata, and any `Co-authored-by` lines should reflect the established pattern in the existing commit history on the `agentic UI conversion` branches. Read recent commits on those branches before adding new ones to match the pattern exactly.

### In-line decision rationale (human-in-the-loop)
Architectural and pattern decisions made during the conversion should be documented inline with explicit rationale, authored by Colin, and tagged distinctly from agent-generated content. The decision rationale is the human-in-the-loop part — it is not generated. It is Colin's judgment captured in commit messages or in adjacent markdown files within the branch.

When the orchestrator encounters a decision point during the build (multiple valid implementation choices, ambiguity in the gap, behavioral differences requiring a call), the orchestrator does NOT make the call silently. The decision and its rationale are surfaced explicitly, attributable to Colin's stated direction, and committed with that rationale in plain prose.

### Agent-generated content tagging
Files produced by agentic processes (the ~250 mapping documentation files, generated code) should be distinguishable from human-authored content. The existing branch organization already separates these. Maintain that separation. Do not co-mingle generated documentation with human decision rationale.

### Branches and naming
Each of the 14 repositories has a branch named `agentic UI conversion` based on the repo's `develop` branch (per Akhil's note in the Confluence page from Set 07). Continue committing to that branch. Do not create new branches. Do not rebase or squash without explicit instruction — the branch is the audit trail.

---

## Memory and load self-review (concrete steps)

This is the highest-priority pre-emption ahead of the demo. Guhan's words: "What is getting generated? I mean, this is generated, but what is running on the system? Right? Let's look under the code with somebody in the EMS team and see because we want to be conscious of how much additional memory this is taking, how much additional load is putting on the system."

Walk through the generated/converted code for each of inventory and fault management with these specific concerns:

1. **Bundle size impact.** What is the byte-size delta in the EMS UI bundle from adding the classic-view packages? If the toggle ships parallel packages, each adds bundle weight. Measure it. Note it.

2. **Initial-load impact.** Does the classic UI lazy-load on toggle, or is it loaded up-front with the modern UI? Lazy is better. If up-front, justify or change.

3. **Toggle-state memory.** When a user toggles between modern and classic view, what stays in memory? Both component trees? One unmounted? Toggle frequency could compound this. Aim for cleanup-on-unmount, not retention.

4. **Render thrashing on toggle.** Does switching modes trigger excessive re-renders, layout recalculations, or DOM churn? Time the toggle. If it stutters, surface it.

5. **Backend load.** Same backend serves both UIs (per the architectural commitment). Does the classic UI make more requests, larger requests, or more frequent requests than the modern UI for the same screens? Compare network panels. Match the modern UI's request profile or justify the delta.

6. **Memory leaks in long sessions.** Toggle 10x in a row. Does memory grow? If yes, flag.

7. **Dependency footprint.** What did the conversion add to the dependency tree? Are any dependencies redundant with what EMS already has? Deduplicate where possible.

Document findings in `cisco/epnm_ems/planning/memory_load_self_review_2026-04-26.md` (or similar dated filename). Even a short note that says "no significant findings" is valuable — it tells Colin he can answer the EMS team's review with confidence.

---

## Demo content scope

The demo will cover the POC: toggle behavior on inventory and fault management screens, comparative parity with EPNM behavior. Keep the demo build clean for that scope.

Two open scope decisions that have NOT been made yet (do not pre-build for them, but be aware they may land):

1. **Mapping reveal.** Whether to include a reveal of the 14-repository system mapping during the demo. If included, Colin will lead it. The mapping artifacts are already in place on GitHub — no orchestrator action needed unless Colin specifically asks.

2. **DPM brief.** Whether BayOne pre-builds a brief showing DPM coverage in the gap analysis. If pursued, the mapping docs already cover DPM as a future-implementation item; the brief would be a curation pass, not new work.

If Colin updates these decisions during the weekend, the orchestrator will be told.

---

## Reference: Stakeholders

For the orchestrator, the relevant stakeholder context is condensed:

**Guhan** — Senior Cisco engineering leader, primary decision-maker. Reads the work product, not the slides. Treats the deliverable as input to a Cisco product-management conversation about customer commitments. His three asks (memory/load review, DPM coverage confirmation, code review before demo) are gates, not curiosity. The orchestrator's contribution to satisfying those gates: pre-empt the memory/load review (above), maintain DPM coverage in the mapping docs, keep commits review-ready.

**Selva** — Cisco engineering/product lead, US-based, operationally hands-on. Validates technical assumptions on the record (toggle hits same backend, etc.). Coordinates demo logistics, time-zone slots, India team scheduling. The orchestrator does not interact with Selva directly; Colin does.

**Cisco India team** (Praveen, Akhil, Ramesh, Ramkrishna, Aadit, Jenis, Senthilkumar) — These are the engineers who will read the commits during the Wednesday code review. Ramkrishna confirmed Postgres in EMS. Akhil led the live product demo on April 6 and described the repo structure. Ramesh is the most technically detail-oriented and will likely surface the sharpest questions during the code review. Audit-ready commits are aimed at this audience.

For the full profiles, read `09_meeting_guhan_selva_deep_dive_2026-04-24.md` and the Set 07 people file.

---

## Reference: Repository inventory

Per the Set 09 mapping work, all 14 repositories are accounted for. The branch `agentic UI conversion` exists on each, off `develop`. The Confluence page from Set 07 is the source of the canonical list, with implicit references discovered during the mapping completing the inventory.

EMS stack: Angular 21, Spring Boot + Go (device management), PostgreSQL, Harbor/Magnetic design system, shell app architecture (Infra UI → Common UI → EMS UI nested).

EPNM stack: Dojo 1.x (Dijit widgets, AMD modules, pub/sub, stores), Java monolith, Oracle DB, SNMP/CLI device integration.

For full technical research see `08_research_*.md` files. Conversion patterns research at `08_research_conversion_patterns_2026-04-07.md` is the most actionable reference if pattern questions come up during build close-out.

---

## What this briefing is not

- It is not a status request to the orchestrator. The orchestrator already has work in progress; this briefing reinforces priorities and adds context.
- It is not a re-scope. POC scope is unchanged.
- It is not a critique. The orchestrator's existing work pattern is good; this is supplementary context from the meeting Colin had on Friday that the orchestrator was not in.

---

## Anchor file paths for the orchestrator

If the orchestrator needs to reference engagement state during the weekend:

- Engagement root: `cisco/epnm_ems/`
- Research library: `cisco/epnm_ems/research/`
- Latest summary: `cisco/epnm_ems/research/09_meeting_summary_2026-04-24.md`
- Org chart: `cisco/epnm_ems/org_chart.md`
- Decisions log: `cisco/epnm_ems/decisions/decisions_2026-04-24.md`
- Progress (actual state): `cisco/epnm_ems/progress/progress_2026-04-24.md`
- This briefing: `cisco/epnm_ems/planning/orchestrator_briefing_2026-04-26.md`

If the orchestrator is on the Cisco machine and these paths are not accessible there directly, they will be transferred or referenced via the means Colin sets up.
