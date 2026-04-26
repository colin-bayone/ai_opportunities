# 08 — Repositories, Access, and Compliance

**Purpose of this document:** The operational boundary conditions the execution session operates inside. What repositories are in play, how access is gated, which tools are permitted, which tools are not, and what gets escalated. Every constraint in this document is sourced from the meetings; nothing is invented.

---

## 1. Repository Inventory

### EPNM repositories

Surfaced in the 2026-04-06 walkthrough. A complete list is on the Confluence page the Cisco team has prepared; the entries below are what was called out explicitly.

| Repository | Contents | Relevance to POC |
|---|---|---|
| PI framework | Core Cisco Prime Infrastructure framework. Dojo-based. EPNM's foundational UI framework layer. | Read-only reference. The base Dojo primitives and patterns live here. |
| Wireless framework (Wireless Repos) | Wireless-specific UI and framework code. Part of the EPNM frontend stack alongside PI framework. | Read-only reference where it intersects with in-scope screens. |
| Assembly | Inventory UI screens. Also the UI side of fault management ("assembly is on the UI side"). | Primary read-only reference for both POC Parts 1 and 2. |
| ChassisView | Chassis visualization component — the physical device rendering shown on Device Details. | Read-only reference for Chassis View reimplementation. |
| Fault Management (EPA wireless repo, and related) | Backend and frontend for fault management. Spans multiple repos. | Read-only reference for POC Part 2. |

Complete EPNM repository list is linked on the Confluence page. Akhil committed to emailing additional code pointers after the walkthrough.

### EMS repositories

| Repository | Contents | Relevance to POC |
|---|---|---|
| `ROBOT/infra-ui` | Angular application shell. Header bar, top navigation, infrastructure UI, login, layout frame. Outermost of the three-layer shell architecture. Existing alarms UI (`src/app/robot-alarms-v2/`) lives here. Navigation is data-driven from `src/assets/modules.json` + `module.service.ts`. Features lazy-load via `src/app/container/robot-shell/robot-shell.routes.ts`. | Classic view will almost certainly require edits here — route registration, nav config, theme wiring — regardless of which repo hosts the feature components. Local-run feasibility plausible (needs execution-session verification, open question 3.8). |
| `ROBOT/common-ui` | Shared Angular component library. Cards, tables (`cw-hbr-table` Harbor-themed, `ag-grid-table` theme-neutral with an existing pluggable theme stack under `scss/ag-grid/styles/`), `base360/` shell for device360 / interface360 / link360, form primitives (`cui-stepper`, `cui-input`, `cui-select`, `cui-datetime-select`, `cui-modal`), Harbor and Magnetic design patterns. Published to Cisco's internal npm registry. | Reuse where components are theme-neutral (the `cui-*` family appears to be). Wrap or extend where components are Harbor-coupled (the `cw-hbr-*` family). For ag-grid, adding a `theme-classic.css` alongside the existing `theme-blue/bootstrap/dark/fresh/material/` is the lowest-risk table path. |
| `ROBOT/unified-ems-ui` | Feature-page layer. Inventory feature pages (inventory-details, inventory-panel, device-management, shared/interface-list) live here. Fault Management is effectively absent — only a 21-line `node-alarms` skeleton, with the actual alarms UI living in `infra-ui/robot-alarms-v2/`. | See open framing on repo shape below. Candidate host for classic-view feature components once the shape is confirmed. |
| `ROBOT/cw-inventory` | Spring Boot / Java inventory REST. Primary REST services include `InventoryRestService.java` (9,724 lines), `JobSchedulerRestService.java` (9,671), `InventoryEMSRestService.java` (1,696). Tyk gateway route map at `config/platform/tyk/tykConfigmap.json`. `LocalProfileConfig` present — local-run plausible. | Read-only reference for API contract. Narrow API touchups routed through Selva. |
| `ROBOT/cw-inventory-collector` | Spring Boot / Java. gRPC contract (`inventory.proto`) with cw-inventory. `LocalProfileConfig` present. | Read-only reference. |
| `ROBOT/cw-epnm-fault` | Spring Boot / Java fault REST (EMS era). Main alarms surface: `AlarmRest.java` (2,622 lines). Write actions: `AlarmUpdateRestController.java` + `AlarmActionServiceImpl.java`. Advanced-filter grammar: `FilterCriteriaUtil.java` (797) + AlarmFilterDTO variants. Docker-first — container-runnable. | Read-only reference for API contract. |
| `ROBOT/ems-assurance` | Spring Boot / Java fault support. EPNM-era NBI at `fault-nbi/ems-fault-nbi/.../AlarmRestServiceImpl.java` (821). Contains capabilities (`NetworkImpactingAlarm`, `NextStep`) not ported to `cw-epnm-fault`. ADS-only — no Dockerfile for main service; `resources_from_server_to_local.sh` helper. | Read-only reference. If the classic UI needs ADS-only capabilities, ADS access (not Docker local) is required. |

> **Open on the EMS UI repo shape (flagged 2026-04-21).** Two readings of `ROBOT/unified-ems-ui` are on the table, neither yet confirmed by source:
>
> **Reading A — casual walkthrough inference.** The 2026-04-06 walkthrough conversation suggested `unified-ems-ui` is the primary working EMS app where most feature development happens. This framing came from informal shorthand in a speech-to-text transcribed meeting, not from a repo-naming or architecture-spec statement.
>
> **Reading B — tree-report inference.** The Session 2 tree-report swarm (2026-04-21) found a `projects/ems-lib/` layout with `public-api.ts` and `root-ems.module.ts` as the export surface, and no conventional-location `main.ts` / `index.html` / root `app.module.ts` — the standard shape of an Angular library consumed by an outer Angular app. Under this reading, `infra-ui` is the Angular app and `unified-ems-ui` is a publishable library.
>
> Both readings are inferences. The execution session's first-days investigation resolves which holds, via source reads of `ng-package.json`, `angular.json projectType`, `infra-ui/package.json` dependencies, and import patterns in `robot-shell.routes.ts`. Handoff doc edits follow that resolution, not Session 2's tree-only read. See `_scratch_repo/flags_for_colin_2026-04-21.md` flag 8 for the full framing.

Additional EMS backend repositories beyond these four may exist (for example, device-management or hardware-integration services). Those are out of scope for this engagement — the POC is a UI reskin against existing EMS REST APIs. The four repos above are the ones the classic UI is expected to call.

### Classic UI code location (undecided)

Akhil offered two options: a subfolder inside the EMS UI repository or a dedicated new repository. Colin owes a proposal. Action item 10 in the Set 07 list. The firm constraint is that the code builds as part of the EMS build regardless of which option is chosen: "It has to be part of the new EMS build."

A proposed folder structure (if the decision is "subfolder in EMS UI repo") is in `06_conversion_patterns_reference.md` Section 8.

---

## 2. Access Provisioning

### The gate: Active Directory groups

Repository access is gated by Active Directory group membership. Akhil: "It is basically controlled through [Cisco] groups, so when we can get that activated to that item and a few groups we have to enable this access. So once after that, he can seamlessly access all the repos."

The specific AD groups Colin needs were not enumerated in the 2026-04-06 meeting. Akhil said "a few groups." This is an open item.

Colin already has a Cisco ID (`colmoore@cisco.com`) issued for the concurrent NX-OS CI/CD engagement, so the provisioning is about adding his existing ID to new groups rather than creating new accounts. Action item 1 in the Set 07 list assigns this to Akhil or the Cisco team.

### VM requirements

Two separate VMs need to be provisioned:

| VM | Purpose | Access level |
|---|---|---|
| EPNM VM | Reference environment for observing classic UI behavior, understanding screen layouts, data flows, and functional behavior. | Read-only. No development, no code deployment. |
| EMS / CNC VM | Development environment. Initial read-only access for exploration, then deployment access when code is ready to patch and verify. | Read-only to start, then development. |

Ramkrishna's framing: "Read only access to an EPNM system... Read only access to a CNC and then when he's ready with the new code and everything, we need to help him patch it. It's only for patching the artifact binaries and then verifying, swapping. Because definitely you might need a setup for the EPNM and one setup for CNC."

**Important: the NX-OS VMs are not reusable.** Colin noted that the NX-OS CI/CD project VMs were provisioned by Divakar for that engagement and are NX-OS-specific. This POC needs its own dedicated VMs. "Technically supposed to be separate."

Ramesh (US-based) was flagged as the best facilitator for VM provisioning because of his time zone overlap. The specific US person or team actually provisioning the VMs was not named. Action items 6 and 7 in the Set 07 list.

### Confluence page access

The Cisco team prepared a Confluence page before the 2026-04-06 walkthrough. Contents:

- User guides for EPNM and EMS.
- API documentation for both products.
- Recordings of EPNM device onboarding and network device workflows.
- Recordings of EMS inventory and detailed views.
- Complete repository list with links to both EPNM and EMS repositories.
- Code pointers to key repositories.

Whether Colin currently has Confluence access, or whether that also requires separate provisioning, was not confirmed in the meeting. Open item.

### Email-based supplementary pointers

Akhil committed to emailing specific repository links and code navigation pointers as a supplement to the Confluence page. Action item 2 in the Set 07 list.

### Neha's access status

Whether Neha (BayOne engagement management) also needs Cisco accounts and repository access was not explicitly discussed. Open item.

---

## 3. AI Compliance Rules

These rules were confirmed in the 2026-04-06 meeting after Ramesh raised the question about AI tool identity, compliance status, and whether Cisco code could be exposed to external services. Selva reiterated the policy on behalf of Cisco. Colin's commitments were accepted by the room.

### Rule 1: Cisco hardware only

All work for this POC is performed on Cisco hardware. No personal laptops, no BayOne hardware outside of Cisco infrastructure. Colin explicitly: "Every single thing we do for this will be done number one on Cisco hardware..."

### Rule 2: Cisco-issued accounts only

All accounts used for this work are Cisco-issued. Colin's `colmoore@cisco.com` is the Cisco ID. "...and number two with Cisco-issued accounts."

### Rule 3: Exactly two AI tools are permitted

1. **Claude Code (Cisco-issued).** Cisco has procured and authorized Claude Code at the enterprise level. BayOne uses it through Cisco's provisioning, not through any BayOne or personal license. "For us, what that looks like from an architecture perspective is Claude Code — we use for development. We'll use the Cisco-issued Claude Code."

2. **LangGraph (local execution).** Runs on Colin's Cisco-issued laptop. No external cloud dependency. "For the actual deployment, that is LangGraph, and that is local. So that is also living and breathing on, for the moment, my Cisco-issued laptop." The phrase "for the moment" signals possible future migration to a Cisco server or VM, but local-to-Cisco-infrastructure execution would remain the property.

**No other tools.** Colin was explicit: "We won't bring in any kind of external third-party or cloud-based tools aside from the Cisco-provided Claude Code for this."

### Rule 4: Code never leaves approved tools

Selva's restatement of Cisco policy: "It's part of any engagement here. We're not allowed to use Cisco code on anything that's outside of our... I mean, the approved AI tools that we get access to is the only thing that we use on our code."

In practice: no pasting Cisco code into external AI chatbots, no uploading Cisco code to external repositories, no running Cisco code through external analysis services, no transit through non-Cisco-approved infrastructure.

### Rule 5: Library installation is gated

Colin: "Even the libraries that are used — those are not able to be touched unless we get those approved first." Python libraries, npm packages, and any other dependencies require approval before installation. For the POC (one person, one laptop), Colin is the gatekeeper. "I'm kind of the master gatekeeper."

How the approval process actually works at Cisco (formal change management versus BayOne-internal control, time-to-response) is not specified in the transcripts. If the execution session needs to install a new library, route through Colin for the decision.

### Rule 6: Network and cloud restrictions

- No external third-party cloud-based tools are permitted.
- LangGraph must run locally on the Cisco laptop, not on external cloud infrastructure.
- Claude Code is permitted only via Cisco's enterprise provisioning.

### Rule 7: Transparency

Colin: "We'll be very transparent about what we're using and how we're using it." Any new tool usage or approach change should be communicable to Cisco if asked. Nothing gets used silently.

### Rule 8: NDA and code residency

NDA was signed prior to the 2026-02-09 discovery meeting. All code remains on Cisco hardware — no downloads to personal machines under any circumstances.

### Rule 9: Precedent

The NX-OS CI/CD engagement with Srinivas Pita and Anand Singh is the operational precedent. Colin cited it in the 2026-04-06 meeting: "We are currently active. Me and about four other people are active on a different project for Cisco. That's the NX-OS CI/CD pipeline work." That engagement is the model for AI-compliance posture at Cisco.

DeepSite (or DeepSeek — phonetics are ambiguous, both are real tools) was mentioned by Colin as another Cisco-context AI tool he has helped with. Its formal status at Cisco (approved, restricted, under evaluation) was not specified and is an open item.

### Rule 10: Gatekeeper model scales with the team

For the POC, Colin is the only BayOne person on the engagement. For the full engagement (Colin plus approximately three additional engineers), every team member gets the same treatment: Cisco hardware, Cisco-issued accounts, Cisco-approved tools only, NDAs signed. The compliance model does not relax as the team grows.

---

## 4. What the Execution Session Must Never Do

These are the lines. Cross any of them and it is a trust event with Cisco.

1. **Do not use any AI tool other than Cisco-issued Claude Code and the locally-running LangGraph.** No ChatGPT, Gemini, Copilot, Cursor, any cloud-hosted LLM, any code assistant other than Cisco-issued Claude Code. If an exception is ever required, it routes through Colin, who routes it through Selva.

2. **Do not install any library without approval.** If a library is not already in the environment, the install is a decision point. Route through Colin.

3. **Do not download Cisco code to non-Cisco hardware.** All work stays on the Cisco-issued laptop.

4. **Do not paste Cisco code into any external service.** No external search, external review, external analysis. If the Cisco-issued Claude Code does not answer it, the answer comes from reading the code directly.

5. **Do not attempt to access Cisco systems using non-Cisco credentials.** Colin's `colmoore@cisco.com` is the identity. No personal accounts.

6. **Do not make backend changes beyond narrow API-level touchups without Selva's explicit agreement.** The backend is in the critical release path. A regression breaks both views simultaneously.

7. **Do not introduce customer-visible references to AI tooling or agent workflow.** Customers never see the AI. Commit messages, documentation, code comments, and UI text read as standard Cisco engineering output.

---

## 5. What Happens When Something Is Blocked

### Access is blocked

If AD group provisioning is delayed, VM availability slips, or Confluence access is missing, the primary route is:

1. Flag to Colin.
2. Colin coordinates with Selva and Neha.
3. Selva engages Akhil, Aadit, or Ramesh depending on what is needed.

The execution session does not chase Cisco engineers directly for access issues. Colin owns the coordination.

### A library is needed

1. Check if the library is already in the environment (run the relevant package manager commands).
2. If not, flag to Colin with a specific ask (what library, what version, what for).
3. Colin makes the call or escalates if needed.
4. Do not install until explicit approval.

### A backend change seems necessary

1. Verify whether the classic view can solve the problem in Angular alone (adapter, service layer, component-level adjustment).
2. If only a backend change works, size it:
   - Narrow API touchup (filter parameter, field addition, query scope): raise to Colin, who raises to Selva, who decides.
   - Anything larger: raise to Colin, who raises to Selva. Per Praveen, the direction is to add equivalent functionality to the new product, not port the old backend.

### A tooling question

Route through Colin. Any new tool, even internally to BayOne's development, goes through the approval frame described in Rules 3 through 7 above.

### A scope question

1. If the answer is in the transcripts, in the research library, in the handoff docs, or derivable from the code — use that.
2. If the answer is genuinely not in any of the above, raise to Colin.
3. Colin raises to Selva if the question is scope-material.

---

## 6. The Twelve Set 07 Action Items (status)

For completeness. All were pending as of the 2026-04-06 meeting. No completion evidence is in the research library through 2026-04-07 (the most recent research date).

| # | Action Item | Owner | Status |
|---|---|---|---|
| 1 | Add Colin's Cisco ID to AD groups for EPNM and EMS repositories | Akhil / Cisco team | Pending |
| 2 | Reply to meeting invite email with code pointers and repository links | Akhil | Pending |
| 3 | Create WebEx team space for the engagement | Aadit or Praveen | Pending |
| 4 | Provide list of BayOne team members to add to team space | Neha | Pending |
| 5 | Set up recurring sync meeting (approximately 12 participants) | Selva / Aadit | Pending |
| 6 | Provision EPNM read-only VM access for Colin | Ramesh (US) / Cisco team | Pending |
| 7 | Provision EMS/CNC development VM for Colin | Ramesh (US) / Cisco team | Pending |
| 8 | Review Confluence page materials (user guides, recordings, API documentation) | Colin | Pending |
| 9 | Complete code deep dive / UI mapping of target POC screens | Colin | Pending |
| 10 | Propose code organization plan (folder in EMS UI repo vs. new repo) | Colin | Pending |
| 11 | Ask Srinivas for permission to share NX-OS CI/CD testing approach with the EPNM team | Colin | Pending |
| 12 | Identify regression test suites applicable to POC scope areas | Cisco engineering team | Pending |

The execution session should assume these remain pending on arrival and confirm status with Colin before relying on any of them as complete.

---

## Footer — Update Log

- **2026-04-21 (Session 2).** §1 Repository Inventory: added the library-vs-app ambiguity on `ROBOT/unified-ems-ui` and enumerated the EMS backend repos with concrete details from the 2026-04-21 tree-report swarm (`cw-inventory`, `cw-inventory-collector`, `cw-epnm-fault`, `ems-assurance`). Named `ROBOT/infra-ui`'s data-driven navigation and lazy-loading pattern, and `ROBOT/common-ui`'s primitive catalog (`cui-*` theme-neutral vs. `cw-hbr-*` Harbor-themed). Flagged `ems-assurance` as ADS-only vs. `cw-epnm-fault` as Docker-first, which shapes local-run feasibility (open question 3.8).

---

## 7. Summary

The execution session works inside a Cisco infrastructure boundary. The laptop is Cisco-issued. The account is Cisco-issued. The AI tools are Cisco-approved (Claude Code via Cisco provisioning; LangGraph local). Library installations are gated. Repository access is gated by AD groups. VMs are provisioned per-engagement. Customer-visible artifacts never reference AI.

Every boundary has a reason. Every boundary has a precedent in the concurrent NX-OS CI/CD engagement. The execution session should treat compliance as a feature of the work, not an overhead on it — the compliance posture is part of what Cisco is buying.
