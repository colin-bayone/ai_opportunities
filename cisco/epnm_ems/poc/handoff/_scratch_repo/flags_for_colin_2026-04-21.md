# Flags for Colin — Consolidated Discussion Document
**Session 2, 2026-04-21.**

Merges Session 2's tree-report findings with Session 1's pressure-test review. Each flag has:

- A short name.
- Classification: **SAFE TO ACT ON** / **NEEDS VALIDATION** / **COLIN DECIDES** / **EXECUTION-SESSION WORK**.
- Evidence for.
- Counter-evidence or uncertainty.
- What decision (if any) is being asked, and of whom.

Scope discipline from Colin (2026-04-21): if we don't know something, we don't guess. We give the execution session (Colin's own Claude instance on the Cisco Mac) enough context to figure it out.

---

## Flag 1. "classic" is a naming collision in the existing codebase

**Classification:** SAFE TO ACT ON. Session 1 concurs: safe to act on.

**Evidence for.** `infra-ui/src/css/magnetic-light-classic.scss` and `magnetic-dark-classic.scss` already exist (723 lines each). These are tier names inside the Magnetic design system — not about EPNM. Handoff doc 06 proposes a `.classic` CSS class convention for our work, which would collide.

**Recommended adjustment.** Use a distinct prefix for our reskin work. Candidates:
- `epnm-classic-*` (clearly ties to EPNM product identity)
- `classic-ui-*`
- `legacy-view-*`

Recommendation leans `epnm-classic-*` because it mirrors the product branding the customers recognize.

**Decision requested:** Confirm the prefix choice so Session 2 can update handoff doc 06 §6 (theme toggle architecture) and the proposed folder structure in §8 consistently.

**Who decides:** Colin.

---

## Flag 2. Bulk CSV import on `cw-inventory` is in a parked state

**Classification:** COLIN DECIDES (scope question).

**Evidence for.** The file is at `cw-inventory/.../BulkImportRootResource.java1`. The `.java1` extension is not compilable; standard Maven / Java build tooling does not pick it up. This is the pattern developers use to retire a file without deleting it, keeping it on disk for reference while excluding it from the build.

**Counter-evidence / uncertainty.** The rename could be recent — the execution session can confirm by looking at `git log --all -- BulkImportRootResource.java1` once on the Cisco Mac. Whether a replacement exists (a different bulk-import mechanism, or a different endpoint in the same service) is not determinable from file names alone.

**What's at stake for the POC.** Network Devices Inventory in EPNM supports bulk device add via downloadable CSV template + upload. If bulk import is a required POC capability, and the EMS backend has parked that feature without a replacement, then either:
1. We escalate to Selva as a narrow API-level gap (implement or reactivate the endpoint), or
2. We defer bulk import from POC scope, or
3. The execution session discovers a replacement mechanism during source read.

Handoff doc 03 (Objectives and Scope) §2.1 lists bulk import as part of Network Devices behavior. It was demonstrated by Akhil in the 2026-04-06 walkthrough.

**Decision requested:** How do you want Session 2 to treat this? Three options:
- (A) Flag immediately to Selva through the WebEx team space when it's created.
- (B) Wait for the execution session to do a source read on `cw-inventory` and confirm whether a replacement exists before raising.
- (C) Defer from POC scope now; bulk import goes to the full engagement.

**Who decides:** Colin.

---

## Flag 3. Chassis interactivity may be an EMS backend gap

**Classification:** NEEDS VALIDATION FIRST. Possible Selva escalation downstream.

**Evidence for.** EPNM's chassis repo has a substantive interactive layer:
- `chassisview/.../hotspot/` directory with `portState.js`, `moduleState.js`, `cardDetails.js` and related files — ~11 files total.
- `chassisview/.../ChassisViewServiceImpl.java` at 2,897 lines on the EPNM backend side.
- Supporting SVG asset library organized by device family with horizontal / vertical / flip orientation variants.

The tree-report swarm did not surface an EMS-side equivalent. There is no chassis-specific backend repo in the 14-repo swept set. The `cw-inventory` service does not appear to host chassis rendering endpoints by name.

**Counter-evidence / uncertainty.**
- The swarm read tree reports, not source. It is possible chassis functionality is embedded inside `cw-inventory` under non-obvious names.
- It is possible chassis rendering is handled entirely client-side in EMS (SVGs delivered as application assets, with interaction state managed in Angular). Handoff doc 05 §2.4 notes "device images are stored as application assets, not Oracle BLOBs" in EMS — consistent with client-side rendering.
- Handoff doc 10 open question 1.8 already flags this as unresolved.

**What's at stake for the POC.** Inventory Part 1 scope includes Chassis View rendered on the left of Device Details. If the interactive chassis (module clicks, port state) is substantive in EPNM and has no EMS-side counterpart, the classic UI either:
1. Builds the interactivity client-side in Angular against EMS inventory endpoints (if data is available but no chassis service exists), or
2. Requires a new EMS backend capability (broader gap — Praveen's guidance says add to EMS, don't port from EPNM), or
3. Gets a scope scaledown — classic view ships with static chassis rendering for the POC.

**What the execution session should do first (before this escalates to Selva).**

1. Open `chassisview/.../ChassisViewServiceImpl.java` entry points only — what operations does it actually expose?
2. Open `cw-inventory` Tyk configmap (`config/platform/tyk/tykConfigmap.json`) and `InventoryRestService.java` entry points — is there a chassis endpoint masquerading under an inventory or interface name?
3. Open EMS `unified-ems-ui` inventory-details area — is there a chassis component that's calling something?
4. Report findings in a short note. Only after that does the question go to Selva.

**Decision requested:** Confirm Session 2 should add the investigation steps above to the execution session's task list for its first days, and hold the Selva escalation until those reads are done.

**Who decides:** Colin.

---

## Flag 4. [WITHDRAWN 2026-04-21]

Retracted by Colin. The POC is a UI reskin against existing EMS REST APIs. Hardware-integration or device-management backend services are out of scope regardless of their implementation language. Go services, if they exist, do not touch this project. Removed from kickoff and from the handoff doc footers. Session 2 error: conflated handoff-doc reference to a walkthrough quote with something the project actually cares about.

---

## Flag 5. `ems-assurance` is ADS-only; `cw-epnm-fault` is Docker-first

**Classification:** FACTUAL OBSERVATION. Affects the local-run plan (open question 3.8).

**Evidence for.**
- `cw-epnm-fault` has Dockerfiles and appears Docker-first (container-runnable).
- `ems-assurance` has no Dockerfile for its main service, but contains `resources_from_server_to_local.sh` (helper script that copies resources from an ADS server into a local dev environment) plus start shell scripts that imply ADS provisioning is expected.
- `cw-inventory` and `cw-inventory-collector` both have `LocalProfileConfig` classes — suggesting local-profile Spring Boot configuration is available.

**Counter-evidence / uncertainty.** None observed. The shape differences are consistent with Cisco migrating newer services to Docker-first and leaving legacy services ADS-dependent.

**Implication for the POC.** End-to-end local-run is **partially** feasible:
- `cw-inventory`, `cw-inventory-collector`, `cw-epnm-fault` — plausibly local-runnable. Needs verification.
- `ems-assurance` — not local-runnable without ADS access. If POC classic fault UI consumes any `ems-assurance`-only endpoints (the EPNM-era `AlarmRestServiceImpl.java`, `NetworkImpactingAlarm`, `NextStep` capabilities), then either ADS access is required or the classic view is tested against `cw-epnm-fault`-only endpoints.

Colin's fallback plan from the Saurav transcript (mocked data first, live wiring once VMs land) remains applicable.

**Decision requested:** None immediately — this is a factual observation. But it feeds the execution session's first-days investigation of local runnability (open question 3.8 in `_kickoff_context_2026-04-21.md` §9). Confirm that's the right handling.

**Who decides:** Colin confirms the handling.

---

## Flag 6. XWT widget layer is distinct from Dojo; handoff doc 06 widget table is incomplete

**Classification:** COLIN DECIDES (do we update doc 06 now or later).

**Evidence for.** The pf-framework repo's `ui/core/ui_components/lib/xwt/` subtree is a Cisco internal widget toolkit layered on top of Dojo. Distinct file paths, distinct widget prefixes, distinct theme files. Examples:
- `xwt/widget/table/Table.js` (5,146 lines)
- `xwt/widget/uishell/Header.js`
- `xwt/widget/navigation/SlideMenu.js`
- `xwt/widget/tasknavigator/TaskNavigator.js`
- `xwt/widget/objectselector/ObjectSelector.js`
- Theme under `xwt/themes/prime/`

**The handoff package's widget-mapping table (handoff doc 06 §2, 25 rows)** was built from the Set 08 research on **Dojo primitives** (`dijit/*`, `dojox/*`). XWT is not in that mapping. The 25-row table is incomplete for actually converting EPNM Inventory and Fault UIs, because those UIs are built on XWT, not raw Dojo.

**Counter-evidence / uncertainty.** The execution session needs to confirm, from actual source reads in `assembly/InventoryListView.js` and `assembly/AlarmListView.js`, whether those views actually instantiate XWT widgets vs. base Dojo widgets. File names in the tree suggest XWT, but the usage could be mixed.

**Options.**
- **(A)** Session 2 updates handoff doc 06 §2 now: add an XWT-to-Angular mapping section alongside the Dojo table, even before the execution session confirms. Document what we see.
- **(B)** Session 2 leaves doc 06 as-is; the execution session reports on actual widget usage during the first-screen deep dive, and doc 06 is updated on the next handoff-update pass.
- **(C)** Session 2 writes a small XWT primer into `_scratch_repo/` now and folds it into doc 06 after the execution session's confirmation.

**Decision requested:** Which of (A), (B), (C)?

**Who decides:** Colin.

---

## Flag 7. Three grid generations coexist in EPNM pf-framework

**Classification:** EXECUTION-SESSION WORK. Session 2 notes it; source read resolves it.

**Evidence for.** The tree report surfaces three generations of grid / table widget in pf-framework:
1. `dojox/grid/DataGrid` — oldest, the legacy Dojo grid.
2. `EnhancedGridWrapper` — middle generation, a Cisco wrapper on top of DataGrid.
3. `xwt/widget/table/Table.js` (5,146 lines) — newest, the XWT table.

Which one the Network Devices table and the Alarms table actually use in `InventoryListView.js` / `AlarmListView.js` is not derivable from the tree. Best guess (by volume and recency) is XWT Table.js, but it is a guess.

**Counter-evidence / uncertainty.** Cisco codebases commonly leave older grid generations in place for legacy screens while newer screens use the newest generation. The POC-scoped screens may or may not use the newest.

**Implication for the POC.** The widget-mapping table in handoff doc 06 targets only one grid pattern (`dojox/grid/DataGrid` → `mat-table`). If the actual usage is the XWT table, the conversion target, ARIA semantics, and feature set differ.

**What the execution session should do.**
1. Open `assembly/.../InventoryListView.js` and `AlarmListView.js`. Check which grid generation is imported at the top.
2. Note in the first-screen deep-dive report which generation is actually in play.
3. If it's XWT Table.js, ask Session 2 (or update doc 06 directly) to add an XWT row to the widget mapping.

**Decision requested:** None — just confirming this is execution-session work, not a Colin decision point. Session 2 captures it in the kickoff message as a first-day task.

**Who decides:** Colin confirms the handling.

---

## Flag 8. `unified-ems-ui` is a library, not an app — reshapes where classic-view code plugs in

**Classification:** NEEDS VALIDATION. Possibly updates handoff doc 08 + doc 05.

**Evidence for.** Agent 06 (unified-ems-ui tree extract) found:
- The repo is an Angular library at `projects/ems-lib/`, not an app.
- No `main.ts`, `index.html`, or root `app.module.ts` at the conventional locations.
- `public-api.ts` and `root-ems.module.ts` are the library's export surface.
- It is consumed by an outer shell — by evidence of tree layout, the outer shell is `infra-ui`.

Further evidence from agent 07 (infra-ui tree extract): existing alarms UI lives at `infra-ui/src/app/robot-alarms-v2/`, not in `unified-ems-ui`. Consistent with `unified-ems-ui` being a feature library that exports pages the shell consumes, while some features (including the existing alarms v2) live directly in the shell.

**Counter-evidence / uncertainty.** Praveen in the 2026-04-06 walkthrough: "Mostly I think you have to work on this [EMS] UI." That was said pointing at `unified-ems-ui`. Session 1's pressure-test flags this as a reshape that affects handoff doc 08 (Repositories, Access, and Compliance) §1 and handoff doc 05 (Technical Landscape) §2.5 — both currently describe `unified-ems-ui` as the primary working repository without qualifying that it's a library.

It is possible that:
- Praveen was imprecise and meant "work on the EMS UI feature layer, which is unified-ems-ui the library."
- Praveen was correct and most of the work does happen in `unified-ems-ui` because it's where inventory feature pages live, even though shell integration happens in `infra-ui`.
- Both repos require substantial work because the classic view has to add new pages to unified-ems-ui AND mount them via infra-ui's routes and nav.

**What the execution session should do** to confirm before handoff doc edits:
1. Open `unified-ems-ui/projects/ems-lib/ng-package.json`, `package.json`, and `public-api.ts` — confirm it's actually a library that gets published.
2. Open `infra-ui/package.json` — confirm it depends on `unified-ems-ui` (or its published name).
3. Open `infra-ui/src/app/container/robot-shell/robot-shell.routes.ts` — confirm routes import from the library.
4. Report whether the library-vs-app split is as Session 2 sees it. Flag to Session 2 if not.

**What changes if the library interpretation holds.**
- Handoff doc 05 §2.5 adds a qualifier: "EMS UI repository (`unified-ems-ui`) is an Angular library consumed by Infra UI, not a standalone app."
- Handoff doc 08 §1 Repository Inventory adds the same qualifier.
- Handoff doc 06 §8 proposed folder structure stays valid: classic-view code can live inside the library at `projects/ems-lib/src/app/classic/`. But a coordinating change is also needed in `infra-ui` to mount the classic routes and register the classic module in `modules.json`.
- Colin's code-organization proposal (action item B2) now needs to cover two repos: `unified-ems-ui` (where classic feature components live) and `infra-ui` (where mount points register).

**Decision requested:** Two-part:
- **(A)** Confirm Session 2 flags this in the execution-session kickoff message as a first-days verification task.
- **(B)** Decide whether to update handoff doc 05 §2.5 and doc 08 §1 now (based on Session 2's read of the tree) or wait for the execution-session confirmation.

**Who decides:** Colin.

---

## Flag 9. Open questions 1.2 and 1.15 are strong-signal, not resolved

**Classification:** HOUSEKEEPING. Just record correctly.

**Session 2's original framing** (cross-repo POC map §5) marked open questions 1.2 and 1.15 as "resolved" based on the tree-report evidence:
- 1.2 (Device Details left-menu enumeration): Said resolved by `DeviceDetailTabViewMetadata.json`.
- 1.15 (Expandable-row content): Said resolved by `View360AlarmController.java`.

**Session 1's correction** (valid): The file name is evidence of where the answer lives, not the answer itself. Until actual source is read and the menu / fields are enumerated, these are **strong-signal-source-read-needed**, not resolved.

**Adjustment.** Session 2 will update the cross-repo POC map §5 to downgrade 1.2 and 1.15 from "resolved" to "strong-signal, needs source read." Handoff doc 10 (Open Questions and Risks) continues to list them as open until the execution session closes them.

**Decision requested:** None — just confirming the correction gets applied.

**Who decides:** Session 2 applies the correction unprompted. Colin acknowledges.

---

## Flag 10. Handoff doc 05 §2.5 and doc 08 §1 assume `unified-ems-ui` is the primary working app

**Classification:** DEPENDS ON FLAG 8.

**Evidence for.** See Flag 8. If the library interpretation holds, these paragraphs need targeted corrections.

**Session 1's observation.** "The only operational cleanup I would do on our side: doc 08 and doc 05 both assume unified-ems-ui is the primary working app. If Session 2's 'library not app' reading holds, those paragraphs need a targeted correction when we next touch the handoff package."

**Decision requested:** Rolls up into Flag 8. If Colin approves updating now (Flag 8 option B), Session 2 edits doc 05 §2.5 and doc 08 §1 with dated footer notes. If Colin wants to wait for execution-session confirmation, no action yet.

**Who decides:** Colin, via the Flag 8 decision.

---

## Summary Table

| # | Flag | Classification | Asks Colin? |
|---|---|---|---|
| 1 | "classic" naming collision | SAFE TO ACT ON | Yes — pick prefix |
| 2 | Bulk CSV parked (`.java1`) | COLIN DECIDES | Yes — scope call |
| 3 | Chassis interactivity EMS gap | NEEDS VALIDATION FIRST | Yes — confirm handling |
| 4 | Go services in swept repos | NEEDS VALIDATION FIRST | Yes — confirm handling |
| 5 | `ems-assurance` ADS-only vs. Docker-first | FACTUAL | Confirmation only |
| 6 | XWT layer distinct from Dojo | COLIN DECIDES | Yes — update doc 06 now or later |
| 7 | Three grid generations in pf-framework | EXECUTION-SESSION WORK | Confirmation only |
| 8 | `unified-ems-ui` is library, not app | NEEDS VALIDATION | Yes — update doc 05/08 now or later |
| 9 | Open Qs 1.2 and 1.15 downgrade | HOUSEKEEPING | Acknowledgement |
| 10 | Doc 05/08 corrections | DEPENDS ON 8 | Rolls up into 8 |

---

## Order of Discussion

Session 2 will walk Colin through these one at a time, in this order (decision-blocking ones first, then the rest):

1. Flag 1 (classic prefix) — fast decision, unblocks doc 06 edits.
2. Flag 8 (library-vs-app) — gates doc 05 + doc 08 updates and affects the code-organization proposal.
3. Flag 6 (XWT vs Dojo in doc 06) — gates completeness of the widget-mapping table.
4. Flag 2 (bulk CSV scope).
5. Flag 3 (chassis gap handling).
6. Flag 4 (Go services verification plan).
7. Flags 5, 7, 9, 10 — confirmations only, batch at the end.
