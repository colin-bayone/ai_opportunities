# Orchestrator Briefing — Cisco EPNM-to-EMS POC

**Audience:** Claude orchestrator session running on the Cisco-issued machine, currently coordinating the actual build work for the EPNM-to-EMS POC.
**Author session:** Claude session running on Colin's BayOne laptop. Has full access to the engagement research library on that machine.
**Briefing date:** 2026-04-26 (Saturday)
**Briefing purpose:** Operational handoff. Captures everything from the April 24 status check-in with Guhan and Selva that affects how the build, test, commit, and demo phases should proceed. Read this fully before continuing work. Companion file: `09_meeting_guhan_scope_signals_and_asks_2026-04-24.md` (people-focused; this file is action-focused).

---

## Important: paths in this document are from the originating machine

Every absolute path in this briefing and in the `forge_pattern_for_cisco/` reference set was written from Colin's BayOne laptop, where the engagement files live at `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/`. When you receive these materials on the Cisco-issued machine, those exact paths will not exist.

**Before relying on any path in this briefing, ask Colin directly:**

- Where on the Cisco machine has he placed the `forge_pattern_for_cisco/` folder (files 01 through 07)?
- Where on the Cisco machine has he placed this orchestrator briefing?
- Which of the engagement files (research library, org chart, decisions log, progress log) are also on the Cisco machine, and at what paths?
- Which files are NOT on the Cisco machine — for those, this briefing's content is the substitute, and you should not chase the path.

Substitute the Cisco-machine paths for the BayOne-laptop paths throughout. The relative file relationships (e.g., "file 05 is in the same folder as file 06") still hold; only the absolute prefix changes.

The Singularity skill referenced as the structural template is at `/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/` on the BayOne laptop. Colin will let you know whether it is also on the Cisco machine and where; if it is not, file 05 in the forge_pattern_for_cisco/ folder is a complete enough extraction that the construction work can proceed without direct access to the original.

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

The conversion is in late-stage build. It is NOT done. Colin chose forward-leaning framing in the meeting deliberately (preserves Cisco confidence at a Friday-evening status check, multiple days of runway remain, on-track work).

### The workflow has changed: forge pattern is now active

Per Saurav's direction (relayed Friday), the remaining work shifts from monolithic-build mode to issue-driven forge-pattern mode. Concretely:

- Each remaining piece of build work is shaped as a GitHub issue on the relevant repository.
- Every in-scope issue carries the `agentic` label so the Cisco India team can filter to BayOne-driven work.
- A new skill — the EPNM forge skill — processes one issue at a time: sets up a worktree on the `agentic UI conversion` branch, runs an 8-phase implementation flow with hook-enforced compliance, opens a draft PR linked to the issue, and Colin reviews/merges.
- Issues are bite-sized with explicit dependency declarations. Smaller and more numerous beats larger and fewer — small issues are easier for the India team to review.

This is not optional and not provisional. The forge pattern is active. If it adds unnecessary burden once we are running it, we will revisit. For now, all remaining build work flows through this pattern.

The companion documentation set for constructing the skill lives at `cisco/epnm_ems/planning/forge_pattern_for_cisco/`. Files 01 through 07. The Singularity skill in this repository (`/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/`) is the canonical structural template for self-containment, frontmatter hooks, folder layout, and agent dispatch — see file 05.

### Demo timeline (unchanged)

- **Mon Apr 27:** Cisco-side VM access provisioned (per Selva). Comparative validation testing can begin against live instances.
- **Tue Apr 28:** Touch-base call between Colin and Selva. Demo slot locks. Code review window confirmed.
- **Wed Apr 29:** India team code review (developer-to-developer; Guhan not required).
- **Wed-Thu Apr 29-30:** Demo with Guhan, Selva, India team. Time-zone window: PST morning / EST midday / IST evening.

The build needs to be demonstrably done by end-of-day Monday. The India team will be reading the commits Tuesday-Wednesday — and now those commits will be coming through forge-skill-produced PRs, which is favorable for the review.

---

## Build priorities through Tuesday

The priority order changes with the forge-pattern shift. In order:

1. **Build the EPNM forge skill itself.** This is the highest-priority item this weekend. The downstream work (issue processing → PRs → review → merge) cannot start until the skill exists. Use SkillForge as the construction tool. Use the documentation set in `cisco/epnm_ems/planning/forge_pattern_for_cisco/` as the reference. Specifically:
   - File 06 is the skill specification — what to build.
   - File 05 is the structural template — how to shape it (Singularity pattern: frontmatter hooks, scripts/ folder, references/ folder, full self-containment).
   - File 07 is the design references guide — the substantive technical references for Java Swing / Dojo / Spring Boot / Angular that you author by reading the actual codebases.
   - Files 01-04 are the DjangoForge analytical reference set — mine as needed for workflow logic, scripts, and references patterns.
   - Bundle worktree creation as a script inside the skill folder. Do NOT depend on a separate worktree skill.

2. **Author the four design references** (per file 07) by walking the actual EPNM and EMS codebases. Source stack reference, target stack reference, conversion patterns reference, best practices and anti-patterns reference. These are substantive — plan for real depth, not boilerplate. The other Claude session does not have repository access and cannot author these.

3. **Create issues for the remaining conversion work** with the `agentic` label. Inventory screens (network devices, device 360, device details) and fault management screens (alarms, events, syslogs). Bite-sized; one screen or one cohesive sub-screen per issue. Explicit dependency declarations between issues where one screen's work depends on another's. Coordinate with Colin and Saurav on issue shape before locking the set.

4. **Run the forge skill on the first issue end-to-end.** The first run will surface deviations from the spec in file 06. Iterate on the skill based on what you learn. Once the first PR is merged, parallelize: run the skill on multiple independent issues concurrently if Anthropic credits and machine resources allow.

5. **Pre-empt the memory and load review concern as Phase 5.5 of the forge skill.** Guhan's gating ask is now baked into the workflow. Each PR's Phase 5.5 artifact is the evidence Colin can surface to the EMS team before they review. Specific checks: bundle-size delta, initial-load impact, toggle-state memory behavior, render thrashing on switch, backend load profile, memory leaks in long sessions, dependency footprint deltas. Document findings in the per-issue Phase 5.5 artifact and aggregate across issues at the end.

6. **Maintain the audit-ready commit pattern across all forge-produced commits.** This is now enforced by the skill itself (Phase 7.5 verifies it). The pattern: commit attribution conventions, in-line decision rationale (Colin's human-in-the-loop authorship), agent-generated content tagging distinct from human-authored content, branch consistency on `agentic UI conversion` off `develop`. The reference file inside the new skill (`audit_ready_commit_pattern.md`) is the spec.

7. **Update the 14-repo mapping documentation** if anything new is discovered during issue processing. Each `agentic UI conversion` branch carries the mapping artifacts; refine as you go.

### Local-staged comparative test harness (still valid)

The Playwright agentic test suite is built and waiting. Wire it against locally-staged data as a fallback in case Monday VM provisioning slips. The forge skill's Phase 7 (verification) integrates with this — when VMs are available, swap targets to live instances; if not, run against staged data.

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

The Cisco India team will review these commits. The pattern is part of the deliverable, and the forge skill enforces it (Phase 7.5). Apply consistently:

### Commit attribution
Commits should be authored such that the Cisco team has clear ownership semantics. Colin established this in earlier work — preserve it. Each commit author and committer field, message metadata, and any `Co-authored-by` lines should reflect the established pattern in the existing commit history on the `agentic UI conversion` branches. Read recent commits on those branches before adding new ones to match the pattern exactly. The forge skill's Phase 7.5 compliance script verifies the pattern is intact before the PR is moved from draft to ready.

### In-line decision rationale (human-in-the-loop)
Architectural and pattern decisions made during the conversion should be documented inline with explicit rationale, authored by Colin, and tagged distinctly from agent-generated content. The decision rationale is the human-in-the-loop part — it is not generated. It is Colin's judgment captured in commit messages or in adjacent markdown files within the branch.

When the forge skill encounters a decision point during issue processing (multiple valid implementation choices, ambiguity in the gap, behavioral differences requiring a call), the skill does NOT make the call silently. The decision and its rationale are surfaced explicitly during Phase 5 (plan-mode user-approval gate), attributable to Colin's stated direction, and committed with that rationale in plain prose.

### Agent-generated content tagging
Files produced by agentic processes (the ~250 mapping documentation files, generated code) should be distinguishable from human-authored content. The existing branch organization already separates these. Maintain that separation. Do not co-mingle generated documentation with human decision rationale.

### Branches and naming
Each of the 14 repositories has a branch named `agentic UI conversion` based on the repo's `develop` branch (per Akhil's note in the Confluence page from Set 07). Continue committing to that branch from each forge run's worktree. Do not create new branches. Do not rebase or squash without explicit instruction — the branch is the audit trail.

---

## Memory and load self-review (Phase 5.5 of the forge skill)

This is the highest-priority pre-emption ahead of the demo. Guhan's words: "What is getting generated? I mean, this is generated, but what is running on the system? Right? Let's look under the code with somebody in the EMS team and see because we want to be conscious of how much additional memory this is taking, how much additional load is putting on the system."

In the forge workflow, this becomes Phase 5.5 — runs after the plan is approved (Phase 5) and before implementation (Phase 6). Each issue's PR carries its Phase 5.5 artifact in the branch. Across issues, an aggregator script (`memory_load_aggregate.py` in the skill's `scripts/`) rolls up findings.

The Phase 5.5 checklist for each issue:

1. **Bundle size impact.** What is the byte-size delta in the EMS UI bundle from adding the classic-view packages this issue introduces? If the toggle ships parallel packages, each adds bundle weight. Measure it. Note it.

2. **Initial-load impact.** Does the classic UI lazy-load on toggle, or is it loaded up-front with the modern UI? Lazy is better. If up-front, justify or change.

3. **Toggle-state memory.** When a user toggles between modern and classic view, what stays in memory? Both component trees? One unmounted? Toggle frequency could compound this. Aim for cleanup-on-unmount, not retention.

4. **Render thrashing on toggle.** Does switching modes trigger excessive re-renders, layout recalculations, or DOM churn? Time the toggle. If it stutters, surface it.

5. **Backend load.** Same backend serves both UIs (per the architectural commitment). Does the classic UI make more requests, larger requests, or more frequent requests than the modern UI for the same screens? Compare network panels. Match the modern UI's request profile or justify the delta.

6. **Memory leaks in long sessions.** Toggle 10x in a row. Does memory grow? If yes, flag.

7. **Dependency footprint.** What did the conversion add to the dependency tree? Are any dependencies redundant with what EMS already has? Deduplicate where possible.

The skill's `references/memory_load_self_review.md` is the bundled spec for this checklist. The Stop hook verifies the Phase 5.5 artifact exists before allowing Phase 6 (implementation) to begin. Even a short artifact that says "no significant findings" is valuable — it tells Colin he can answer the EMS team's review with confidence.

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

The paths shown below are the originating-machine (BayOne laptop) paths. Ask Colin where the equivalents live on the Cisco machine before using any of them. The relative relationships (e.g., "files 01-07 are siblings in the forge_pattern_for_cisco/ folder") hold; only the absolute prefix changes.

### Engagement state (origin paths)
- Engagement root: `cisco/epnm_ems/`
- Research library: `cisco/epnm_ems/research/`
- Latest summary: `cisco/epnm_ems/research/09_meeting_summary_2026-04-24.md`
- Org chart: `cisco/epnm_ems/org_chart.md`
- Decisions log: `cisco/epnm_ems/decisions/decisions_2026-04-24.md`
- Progress (actual state): `cisco/epnm_ems/progress/progress_2026-04-24.md`
- This briefing: `cisco/epnm_ems/planning/orchestrator_briefing_2026-04-26.md`

If any of these files are not on the Cisco machine, do not chase them. The summaries, decisions, and progress notes that matter for the forge construction are quoted or paraphrased in this briefing and in files 01-07. The originals are reference, not blocking.

### Forge skill construction reference set (origin path)
- Folder: `cisco/epnm_ems/planning/forge_pattern_for_cisco/`
- File 01: DjangoForge anatomy and self-containment audit
- File 02: DjangoForge workflow phases and orchestration
- File 03: DjangoForge scripts and hooks deep-dive
- File 04: DjangoForge references and standards
- File 05: Singularity self-containment and structural pattern (the structural template)
- File 06: EPNM forge skill specification (the build target)
- File 07: Design references to author (Java Swing, Spring Boot, Angular, conversion patterns, best practices)

This is the most important folder to locate on the Cisco machine. Ask Colin first.

### Structural template skill (origin path)
- Singularity skill: `/home/cmoore/programming/ai_opportunities/.claude/skills/singularity/`
- Frontmatter hook pattern, folder layout, mandatory startup pattern, agent prompt template — model after this.
- File 05 in the forge construction folder extracts the relevant patterns; if the original Singularity skill is not on the Cisco machine, file 05 is sufficient.

### Codebases (Cisco machine — these you have)
The 14 EPNM and EMS repositories live on the Cisco machine. You have direct access. Their paths and clone structure are something Colin will confirm if not already in the engagement records you receive. Walking these is part of the design-references authoring work in file 07.
