# Execution Session Handoff — EPNM-to-EMS Classic View POC

## Path and Transfer Disclaimer (read first)

Paths quoted in this document are illustrative. They describe the structure of the engagement folder as it exists on Colin's BayOne machine where Session 2 produced the handoff package. On your Cisco Mac the absolute prefix is different; the relative structure under the POC folder is what matters. If this document references a file by name and you cannot find it at the path implied, the file may be:

- At a different absolute prefix on your Cisco Mac (look for the same relative path under wherever Colin staged the engagement folder).
- Not yet transferred to your Cisco Mac. Colin moves files between machines through Cisco WebEx; some supporting files (the research library, source transcripts, the Saurav transcript extract, the Confluence context extract) may still be on the BayOne side when you start. Ask Colin.
- Present but under a slightly different folder name if staging required it.

Treat every path below as a pointer to a file by name, not a literal filesystem location. Ask Colin when you cannot find something. Do not assume the file does not exist.

## Read This First

You are the execution session for this POC. You run on Colin's Cisco-issued Mac with access to all the Cisco repositories this project touches. Your job is to build the classic-view toggle POC: Angular code, inside the existing EMS build, reproducing the EPNM user experience for two specific functional areas, against the existing EMS backend unchanged.

There is a second Claude session running on Colin's BayOne machine — Session 2 — that has been doing orchestration and synthesis for you: reading the handoff package, absorbing tree-report dumps, building maps, writing primers. Session 2 does not have repo access. You do. When Session 2's observations look wrong against actual source, trust what you see. Session 2 explicitly wrote its outputs as starting context, not conclusions. Route questions back through Colin to Session 2 when you want a second pair of eyes on something you can't act on from source alone.

Everything below is starting context. The actual investigation is yours.

---

## What the Engagement Is (one paragraph)

Cisco has two network-management products: EPNM (legacy, Dojo 1.x UI, Java monolith + Oracle, roughly a decade old) and EMS inside Crosswork Network Controller (Angular 21, Spring Boot + PostgreSQL). Customers trained on EPNM resist the EMS UX. BayOne (Colin Moore, Director of AI) is building a POC for Cisco that adds a classic-view toggle to two EMS screens — Inventory and Fault Management — so operators can flip between the EPNM-style UX and the modern EMS UX. Both views call the same EMS backend unchanged. Default on login is classic. POC is Colin solo. Full engagement scales after the POC lands. All work on Cisco hardware with Cisco-issued tooling.

---

## The Operating Model

- You are Colin's own Claude (or Codex) instance on his Cisco-issued Mac. Not a separate teammate's session.
- Tools are tool-agnostic in this document. Colin uses Claude and Codex interchangeably depending on what's practical. References to "Claude" in this document and in the handoff package apply equally to Codex. If Colin later decides to standardize on one, he will do a find-replace; do not assume one tool over the other in your own output.
- Session 2 is on Colin's BayOne machine, no repo access. You and Session 2 communicate through Colin.
- All AI-compliance rules from the handoff doc 08 apply. The only permitted tools for this work are the Cisco-issued Claude Code (or Cisco-issued Codex) for development and local LangGraph for orchestration. No external AI services, no personal accounts, no code outside Cisco hardware.

---

## Where Everything Lives

Engagement folder: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/`. On the Cisco Mac the path will differ; the structure is the same.

| Path | Contents |
|---|---|
| `poc/handoff/` | The 12-document handoff package. Start here. See next section. |
| `poc/handoff/_scratch_repo/` | Session 2's cross-repo POC map, findings log, and two primers. Starting context produced from tree reports. |
| `poc/REPO/` | Repository analysis bundle you produced on the Cisco Mac. Tree reports for every in-scope repo, plus consolidated and machine-readable summaries. |
| `poc/context.txt` | Confluence extract from Cisco: authoritative repository URLs, scope modules, EPNM wiki link. |
| `poc/` (working folder) | Where your new artifacts accumulate. Progress notes, decision logs, any output produced during the POC. |

### Available on request, not pre-staged

The research library (`cisco/epnm_ems/research/`, 57 files) and the raw / formatted source transcripts (`cisco/epnm_ems/source/`) live on Colin's BayOne machine. They are the engagement's historical substrate. The handoff package already distills the scope-material parts. If you encounter a specific question where you suspect the raw transcript or a specific research file holds the answer, ask Colin to send that one file. Do not assume these are on your machine.

---

## Starting Reading Order

This is a suggested sequence, not a prescription. You decide when you have enough context to start opening source.

1. **`poc/handoff/00_index.md`** — entry point for the 12-document handoff package. Points at everything else.
2. **`poc/handoff/01_project_overview.md`** — anchor explanation of the engagement.
3. **`poc/handoff/03_objectives_and_scope.md`** — the exact POC scope: two screens, what each covers, what's in, what's out, what defines done.
4. **`poc/handoff/06_conversion_patterns_reference.md`** — working-desk technical reference. Dojo-to-Angular widget mapping, theme toggle architecture, folder structure, per-screen migration checklist. See §6 naming note (2026-04-21 update: classic CSS tokens use the `epnm-classic` prefix, not bare `classic`, because Magnetic already uses `classic` as a tier name).
5. **`poc/handoff/08_repositories_access_and_compliance.md`** — repo inventory with Session 2's 2026-04-21 additions (named files inside each EMS repo), access-gating model, and the 10 AI-compliance rules.
6. **`poc/handoff/11_ways_of_working.md`** — escalation routing, decision authority, what to stop and ask about.
7. **Remaining handoff docs** (`02`, `04`, `05`, `07`, `09`, `10`) — history, strategic approach, technical landscape, stakeholders, work items, open questions and risks.
8. **`poc/REPO/README.md`** and the consolidated reports under `EPNM/`, `EMS-CNC/`, and `EPNM-EMS-CNC/`. These are machine-produced summaries of what is in each repository.
9. **`poc/handoff/_scratch_repo/cross_repo_poc_map_2026-04-21.md`** — Session 2's cross-repo map of POC-relevant paths. Starting context for where Inventory and Fault code appear to live on both sides. Not a commitment list.
10. **`poc/handoff/_scratch_repo/_findings_log_2026-04-21.md`** — Session 2's running findings ledger from the 10-agent tree-report absorption.
11. **`poc/handoff/_scratch_repo/java_multi_repo_primer.md`** — Colin flagged he is Django-brained on the Java side. This primer covers JARs, WARs, Maven multi-module builds, Spring Boot profile models, and how the EPNM and EMS stacks differ in runnability shape.
12. **`poc/handoff/_scratch_repo/xwt_primer.md`** — observed XWT widget toolkit inventory inside `pf-framework`. Doc 06's widget mapping table was built from raw Dojo research; XWT is not in that table. Factual catalog only, no proposed mappings.
13. **`poc/handoff/_kickoff_context_2026-04-21.md`** — running kickoff context updated through 2026-04-21 including the operating-model clarification, open question 3.8 (local runnability), and the scope-discipline posture.

---

## Standing Rules You Operate Under

### Scope

- Two screens: Inventory (Network Devices, Device Details with Chassis View, Device 360, Interface 360) and Fault Management (alarms table, events, syslogs, correlated alarms). Nothing else.
- Backend is untouched. The classic UI calls the same EMS REST APIs the modern EMS UX calls. No backend rewrite. Narrow API-level touchup (a filter parameter, a missing field) is allowed only after Selva signs off through Colin.
- Default on login is the classic view. Toggle flips to the modern EMS UX. Per-screen local toggle for the POC. Global toggle deferred.
- Production-quality code. Not a prototype. Selva framed this as "product of product" — it will ship.
- Functional equivalence is the acceptance bar: same action in either view produces the same result.

### AI compliance

- Cisco hardware only. Cisco-issued accounts only. Cisco-approved tools only (Cisco-issued Claude Code or Cisco-issued Codex for development, local LangGraph for orchestration).
- No external cloud AI. No pasting Cisco code into any external service. No downloading Cisco code to non-Cisco hardware.
- Library installs are gated. Route through Colin.
- Customers never see the AI. Commit messages, PR descriptions, code comments, and UI text read as standard Cisco engineering output.

### Branches and repositories

- The only branch you write to in any repository is `agentic-ui-conversion`. This branch has been created in every in-scope repo. All work happens on it. All pushes go only to it.
- Forking is disabled in `github3.cisco.com`. The branch was created by clone + new-branch + push, not by fork.
- Repo access is gated by Active Directory groups. Confluence page has the authoritative complete repo list; the 14 repos in `poc/REPO/` are what the classic UI directly interacts with.

### Exploration style

- Read files. Do not grep, regex, or shell-pattern-match during exploration unless Colin explicitly allows it for a specific task. Colin's standing rule; enforced across the engagement.
- Agent-driven exploration first, then targeted questions when code does not answer them. Batch questions rather than fragmenting.
- When a walkthrough transcript or handoff-doc paraphrase disagrees with source you can see, trust source. The walkthroughs are casual conversations transcribed from speech-to-text.

### Decision authority

- Implementation details inside committed scope (file organization within the proposed folder structure, component naming within the convention, Angular-idiomatic patterns, internal test design) are yours.
- Anything that would contradict the scope Guhan committed to in the 2026-03-25 reframe, any backend change, any new tool or library outside the approved set, any customer-visible artifact, or the code-organization proposal itself — raise to Colin before acting.
- No unilateral decisions when instructions can't be followed exactly. Stop and ask.

### Progress recording

- Research library is immutable. Do not edit anything under `research/`.
- POC work products go under `poc/` with date-prefixed folder names where useful. The handoff package `poc/handoff/` is living but tracked: if you update a handoff doc, add a dated note to its footer rather than silent rewrite.
- Session 2 will propagate relevant updates you report back through Colin.

---

## Starting-Context Flags (Session 2 observations — all unresolved)

These are items Session 2 surfaced from tree-report data and handoff-doc review that you have the source access to resolve. None of them are prescriptive. Each is presented with what the handoff says and what the tree suggests, both as equal-weight inputs for your own evaluation.

### Library vs. app on `unified-ems-ui`

- Handoff doc 05 §2.5 and doc 08 §1 have historically treated `ROBOT/unified-ems-ui` as the primary working EMS app. Framing originated from casual shorthand in the 2026-04-06 walkthrough transcript, which is speech-to-text and not architectural-spec language.
- Session 2's tree-report read found a `projects/ems-lib/` layout with `public-api.ts` and `root-ems.module.ts` as export surface, and no conventional-location `main.ts` / `index.html` / root `app.module.ts`. That is the standard shape of a publishable Angular library consumed by an outer Angular app. Under this read, `ROBOT/infra-ui` is the Angular app and `unified-ems-ui` is a library.
- Handoff docs 05 §2.5 and 08 §1 now present both readings as unresolved.
- Resolution belongs to you. `ng-package.json`, `angular.json`, `infra-ui/package.json`, and import patterns in `infra-ui/src/app/container/robot-shell/robot-shell.routes.ts` are the obvious source artifacts. Relevance: the code-organization proposal Akhil asked Colin for (action item B2) depends on how this resolves. Report back; Session 2 will help Colin propagate any doc updates.

### Where the existing alarms UI lives

- The handoff language implies alarms UI lives in `unified-ems-ui`.
- Session 2's tree read found the existing alarms UI at `infra-ui/src/app/robot-alarms-v2/`, with only a 21-line `node-alarms` skeleton in `unified-ems-ui`. Consistent with the library-vs-app read above.
- Worth confirming against source when you resolve the library question.

### The `epnm-classic` naming prefix (applied)

- Doc 06's earlier folder-and-theme convention was `classic/`, `data-theme="classic"`, `.classic`.
- Tree read found `infra-ui/src/css/magnetic-light-classic.scss` and `magnetic-dark-classic.scss` already in place — "classic" is already a Magnetic tier name, unrelated to EPNM.
- Doc 06 has been updated (2026-04-21 footer note) to use `epnm-classic` throughout: `data-theme="epnm-classic"`, `src/app/epnm-classic/` folder, theme CSS token names prefixed `--epnm-classic-*`. User-facing toggle labels stay "Classic" and "Modern" per the walkthrough direction.
- Acting on this is safe; naming is already applied in the handoff package. Flagged so you don't reintroduce the collision.

### Bulk CSV import in `cw-inventory`

- Handoff doc 03 §2.1 lists bulk CSV import as part of the Network Devices behavior Akhil demonstrated on 2026-04-06.
- Tree read found `cw-inventory/.../BulkImportRootResource.java1`. The `.java1` extension is non-compilable; that naming convention typically signals a parked file.
- Whether bulk import is replaced elsewhere, disabled intentionally, or pending reactivation is not visible from the tree. Source and `git log` resolve it.
- If bulk CSV is actually in POC scope once you read the source, and if there is no working replacement, that is an escalation through Colin to Selva.

### Chassis View interactivity

- Handoff doc 03 §2.1 and open question 1.8 (doc 10) flag that Chassis View interactivity in EMS was not confirmed during the walkthrough.
- Tree read of EPNM `chassisview` surfaced a `hotspot/` directory with files named `portState.js`, `moduleState.js`, `cardDetails.js` (~11 files), plus a `ChassisViewServiceImpl.java` at 2,897 lines on the EPNM backend side. Interactivity on the EPNM side is substantive, not trivial.
- Tree read of the four swept EMS backend repos did not surface a chassis-specific backend. That is absence-of-evidence, not evidence-of-absence — you have source access to verify whether chassis state endpoints exist elsewhere in `cw-inventory` under non-chassis-labeled names, or whether chassis rendering is entirely client-side in EMS.
- If the interactive chassis component does not exist in EMS, it is a gap candidate under handoff doc 10 risk 6.11. Praveen's guidance applies: add equivalent functionality to EMS rather than port from EPNM.

### XWT widget toolkit

- Handoff doc 06 §2 has a 25-row Dojo-to-Angular mapping table produced from the Set 08 research on raw Dojo primitives.
- Tree read of `pf-framework` surfaced a Cisco-internal widget toolkit, XWT, under `pf-framework/ui/core/ui_components/lib/xwt/`. Named widgets include `Table.js` (5,146 lines), `Header.js`, `SlideMenu.js` (2,394), `TaskNavigator.js` (1,312), `ObjectSelector.js` (6,929). Three grid generations coexist: `dojox/grid/DataGrid`, `EnhancedGridWrapper`, and XWT `Table.js`. Which generation `assembly/.../InventoryListView.js` and `assembly/.../AlarmListView.js` actually import is not visible from the tree.
- `_scratch_repo/xwt_primer.md` holds the factual inventory Session 2 observed, with no proposed Angular mappings.
- Resolution is yours once you open those files. If they import XWT, doc 06's mapping is incomplete for the POC screens and you decide whether to extend doc 06, write a separate XWT mapping, or handle translations ad hoc.

### `ems-assurance` is ADS-only; `cw-epnm-fault` is Docker-first

- `cw-epnm-fault` has Dockerfiles and appears container-runnable.
- `ems-assurance` has no Dockerfile for its main service and contains `resources_from_server_to_local.sh` plus start shell scripts that imply ADS provisioning. Cisco's ADS is the internal deployment infrastructure.
- Capabilities `NetworkImpactingAlarm` and `NextStep` exist in `ems-assurance` (the EPNM-era alarm NBI at `fault-nbi/ems-fault-nbi/.../AlarmRestServiceImpl.java`) but not in `cw-epnm-fault`. If the classic alarms UI consumes either, ADS access is required rather than pure local Docker. Source read confirms.

### Local runnability of EMS for POC testing

- Colin flagged in the 2026-04-21 Saurav conversation: nobody answered whether EMS runs locally for a developer without ADS access.
- `cw-inventory`, `cw-inventory-collector`, and `cw-epnm-fault` have `LocalProfileConfig` classes and/or Dockerfiles — consistent with local-run intention.
- `ems-assurance` is ADS-dependent (see above).
- `infra-ui` is an Angular app with a custom webpack config. Whether `ng serve` (or the custom-webpack equivalent) runs standalone or requires backend endpoints is unresolved.
- Answering this is a load-bearing question for the POC test plan. Colin's fallback from the Saurav transcript: start the first screen with mocked data (static JSON or screenshot-backed fixtures), wire the live backend once VM / ADS access is confirmed.
- Open question 3.8 in `_kickoff_context_2026-04-21.md` §9 captures this. Your first-days investigation is up to you.

### Resolution of open questions 1.2 and 1.15

- `DeviceDetailTabViewMetadata.json` in `EPNM/inventory` appears to hold the Device Details left-menu enumeration (open question 1.2).
- `View360AlarmController.java` in `cw-epnm-fault` appears to hold expandable-row alarm detail (open question 1.15).
- Both are strong signals, not resolutions. Source read closes them.

---

## How You Interact With Colin and Session 2

- Colin is your primary contact and the sole route to Cisco. You do not communicate directly with Selva, Guhan, Venkat, or the tech leads.
- When you have a question that code or the handoff docs genuinely do not answer, compile it concisely and raise to Colin. Batch where possible.
- Session 2 (on the BayOne machine) can answer questions about the handoff package, the research library, the tree-report observations, and prior session context. Route through Colin; Colin relays. Session 2 does not have your repo access.
- When you update a handoff doc, add a dated footer note and tell Colin what you changed so Session 2 can propagate.
- When Session 2 got something wrong (paths don't match, tree inference doesn't hold, a flag is a false alarm), tell Colin. The corrections feed back into the living handoff.

---

## Your First Response

When you start:

1. Confirm in a short message that you are the execution session on Colin's Cisco Mac for the EPNM-to-EMS classic-view POC, and that you understand the scope, the compliance rules, and the operating model above.
2. Read the handoff package and the supporting scratch files per the suggested sequence. Aim for narrative understanding; flag anything in the docs that does not match source you can see.
3. Decide your own first-days sequencing. The work items in handoff doc 09 (A through G) give the shape of what needs to happen; you order within that.
4. Start doing the work. Start with whichever of the two screens you judge most tractable to prove the toggle pattern end-to-end. Colin has said in informal conversation that he leans toward Inventory first because it is the larger, richer pattern family and will seed more reusable infrastructure. That is context, not instruction; decide for yourself after reading.

---

## One Last Thing

You have significant latitude. Session 2's job was to front-load context so your first days are spent on source reading and pattern establishment rather than orientation. The framing that has held across the engagement: scope is two screens, fidelity is the target, backend is off-limits, production-quality code, customers never see the AI, one person doing the POC. Everything else is judgment.

If anything in this kickoff, in the handoff package, or in the scratch materials looks wrong once you have source in front of you, trust the source. This document and the handoff docs are strong starting snapshots, not frozen specifications.

Good luck.
