# 02 — Engagement History

**Purpose of this document:** Chronological narrative of how the POC came to be, from first contact through the final walkthrough. Scope commitments, major decisions, reversals, and who joined when. Commercial events (pricing discussions, financial model iterations) are deliberately excluded.

**Reading note.** Dates reflect when source material was produced, not when this document was written. Every claim traces back to a research file or meeting transcript in `cisco/epnm_ems/research/` or `cisco/epnm_ems/source/`.

---

## Before February 2026 — Pre-Engagement

BayOne's initial contact with Guhan came through an internal referral, referenced in Set 01 as a conversation Guhan had with someone called "Mecha" who suggested BayOne could help accelerate work in Guhan's area. No meetings preceded the February 9 first session.

---

## 2026-02-09 — First Discovery Meeting (Set 01)

In-person meeting at Cisco offices. Colin Moore (BayOne Director of AI) and an unnamed BayOne account representative meet with Guhan and Selva. The tone was exploratory and collegial; the group transitioned from casual conversation to the business problem organically.

**What Guhan introduced.** A legacy network management product (EPNM) has customers asking for the legacy UI experience back, because operators are trained on it and their systems integrate with it. Roughly 200 UI screens are involved. The traditional approach of staffing ten engineers for a year is rejected. Guhan wants an AI-accelerated approach and strategic guidance, not just implementation. Scale: 45-50 million lines of code across 6-8 products.

**What Colin presented.** BayOne's code modernization methodology: simplification first, then knowledge graphs, Claude Code as the backbone for exploration, a LangGraph agent swarm (architect, engineer, foreman, judge), automated UX testing with Playwright, gap analysis through peer-to-peer agent communication, blockchain-style documentation. Guhan interrupted the presentation mid-way to ask for a deeper session with his team lead later the same day.

**Key commitments from this meeting:** Colin would write a POC proposal. The POC would be done at cost to BayOne as an investment to prove capability. Colin would run the POC personally. Hardware (Cisco laptop, Cisco ID) to be provided; initial estimate 1-2 weeks. A 3:00 PM same-day deep-dive session with a team lead was scheduled.

**Security and access baseline established.** All code remains on Cisco hardware. Cisco-licensed AI tools only (no personal tool licenses). NDA signed. These constraints became immovable and persist through to today.

**Source file:** `source/guhan_selva-2-9-2026_formatted.txt`. Research files: `research/01_meeting_*.md`.

---

## 2026-02-18 (approximate) — Call Prep for Second Discovery (Set 01a)

BayOne prepared a structured question list for the Feb 20 meeting: 19 questions in five categories organized around a "please correct us" opening strategy. The prep underestimated the vertical nature of the backend gaps, which was revealed during the actual meeting. Most questions were answered organically once the meeting started; Colin observed in that meeting that his question list had been pre-answered by Guhan's and Selva's opening framing.

**Source file:** `source/discovery_questions_call_prep_2026-02-20.md`. Research files: `research/01a_call_prep_*.md`.

---

## 2026-02-20 — Second Discovery Meeting (Set 02)

Follow-up meeting with Guhan, Selva, and Colin. Eleven days after the first meeting. The tone shifted from exploratory to directive. Guhan framed the engagement explicitly as a challenge: "Can you take that experiment, provide a working code, show us the demo."

**Scope framing established in this meeting (later reversed).** The work was described as a full-stack vertical conversion. Selva stated "if something was not brought in the frontend, the corresponding backend is also not working." Missing reports were identified as a concrete starting point for the POC. Seventy to one hundred pages was cited (a revision down from the 200 of Set 01). Legacy code was described as having undergone "surgery," preventing direct porting. No design documentation existed for the legacy product.

**Enduring material from this meeting.**

- **Quality assurance framework.** Guhan pressed Colin on how he would ensure no domain or functionality gap. Colin's four-layer answer — judge agent performing meta-analysis of test coverage, Playwright visual comparison workable without a running application, peer-to-peer agent gap analysis with autonomous sub-agent spawning, human categorical review as last line of defense — remains directly applicable to today's POC.
- **Engagement model.** Zero Cisco team bandwidth. BayOne works independently after receiving context. Periodic checkpoints for progress and clarification. Team is on critical platform work and cannot invest significant time. This model persists.
- **No design documentation.** The legacy codebase is the source of truth. Expect no architectural documentation covering EPNM.
- **Hardware delay became real.** Eleven days after the Feb 9 meeting, Cisco laptop and ID were still not available. Escalation in progress with an evening call scheduled.

**Source file:** `source/guhan_selva-2-20-2026_formatted.txt`. Research files: `research/02_meeting_*.md`.

---

## 2026-03-24 — Hardware Delivered

Colin received the Cisco laptop. Five weeks after the initial Feb 9 estimate of 1-2 weeks. The blocking dependency was finally resolved. Setup was partial on the day of delivery; Colin continued trainings and sign-in work into the following days.

---

## 2026-03-25 — Scope Reframe Meeting (Set 03)

The single most consequential meeting in the engagement history. Colin, Guhan, Selva on a WebEx call. Guhan had a hard stop at 11:25 and departed early; Selva took operational ownership from that point.

**The reframe.** Selva opened by acknowledging that the earlier meetings had been unclear. He then reversed the scope framing. "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI. But obviously, it's been redesigned to adopt a new workflow, a new UX and everything." The work is not a conversion of missing functionality. The work is a UX overlay on screens that already exist in EMS.

**What the new framing explicitly includes and excludes.**

- Included: a classic view toggle on existing EMS screens. Angular rebuild of the EPNM-style UX. Wiring the classic UI to the existing EMS backend.
- Excluded: backend reimplementation. "We don't want to rewrite the backend services," per Guhan, with reasons listed (effort, maintenance burden of two backends, staffing, engineering judgment, deployment footprint). "We are not trying to reboot the backend from older, right? That's not something what we want him to do." The only accepted backend exception is narrow API-level touchup for lens or filter differences.
- Excluded: missing functionality work. "We're not looking for missing functionalities, but we are looking for things that are there but gives us the same user experience."

**POC scope confirmed.**

- Target screens: Faults and Inventory. Selva: "It's inventory, yeah." Guhan: "So, these are very common applications that customer usually go to."
- Toggle approach for POC: local per screen. "We will do local toggle by that what I mean is let's say a fault screen for example... we'll just add a toggle to that very same page and say once you toggle it gives me the classic." Global toggle is product-level work that follows the POC.
- UX team explicitly not involved in POC. They will bless the final UX in product phase.
- Functional equivalence is the acceptance bar. Both views must produce the same results because they share the same backend.

**Colin's process framing.** Colin explained the exponential-decay nature of agent-driven work: first screens are slowest because the environment has to be set up and patterns established; subsequent screens benefit from compounding infrastructure. He warned against linear extrapolation: "Don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens." He also raised the Venn-diagram mental model for feature mapping (the overlap of EPNM functionality and EMS functionality is the target, with full parity only required for areas customers care about).

**Colin showed Azure Foundry** during the call as a concrete visual anchor for the toggle pattern. Guhan responded by synthesizing the reframe in one sentence: "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."

**New person introduced in this meeting.** Venkat, a Cisco leader above Guhan, was referenced as "direction from the top" pushing the team to think differently about staffing (away from the one-person-per-screen model). Venkat was not present. His explicit interest in a July delivery target was mentioned but framed as exploratory, not a hard deadline.

**Also in this meeting.** Rahul Bobbili (BayOne president) joined partway through. Selva committed to scheduling a walkthrough with the India-based domain experts the following week. Selva committed to creating a WebEx space for ongoing coordination between Selva, Colin, and Rahul. Selva offered to identify a local San Jose resource for Colin's first week so he had someone to "bounce off."

**Commitments from Colin coming out of this meeting.**

- Amend the POC proposal to reflect the classic view toggle framing.
- Continue application-specific trainings and sign-in on the new Cisco laptop.

**Source file:** `source/guhan_selva-3-25-2026_formatted.txt`. Research files: `research/03_meeting_*.md`. Bridge: `research/02-03_changes_2026-03-25.md`.

---

## 2026-03-26 through 2026-04-02 — Internal BayOne Period

A series of internal BayOne discussions and client-facing pricing artifacts were produced during this window. These are commercial in nature and outside the scope of this handoff. One item from this period is worth noting for scope purposes only: the Cisco team (Guhan specifically) reached out asking for a breakdown of the engagement structure. This was a buying signal and resulted in a four-phase engagement structure being documented for Cisco. The four-phase structure covers discovery, tooling, conversion, and QE; this affects how the larger engagement is framed but does not affect the two-screen POC scope.

Also noted in this period: the 05a Venkat positioning notes referenced the engagement as "Legacy product EPNM, Migrating UI from EPNM -> CNC platform, AI generating code for modernization" — confirming the CNC framing of the target platform and the AI-generated-code narrative that Venkat champions broadly.

**Source files (informational only):** `source/ceo_rahul_call_2026-03-30_formatted.txt`, `source/venkat_notes_2026-03-30.txt`.

---

## 2026-04-06 — First Technical Walkthrough (Set 07)

The first meeting with the full Cisco engineering team. Twelve attendees: eight Cisco (Selva, Praveen, Akhil, Ramesh, Aadit, Jenis, Ramkrishna, Senthilkumar) and four BayOne (Colin, Rahul Bobbili, Neha, Zahra). Selva introduced the team and context, then the tech leads presented the EPNM product live and walked through the repository structures for both products. Colin was seeing EPNM and EMS running for the first time.

**What got confirmed.**

- POC Part 1 scope: Network Devices list, Device Details (with Chassis View on the left and a left-menu of system summary / device details / chassis / enrollment), Device 360 (tabs: alarms, modules, interfaces, location, recent changes; launchable from multiple places), Interface 360 (nested 360 launched from the interfaces tab).
- POC Part 2 scope: Alarms and Events (alarms table with columns / quick filter / advanced filter / expandable rows / clear-alarm action / correlated alarms / 360 view link), a most-recent-events popup, a full events page with a default past-8-hours window, and syslogs as a third data type.
- EPNM stack: Dojo legacy framework with a blue-and-white theme; repository layout includes PI framework (the core Dojo-based Prime framework), wireless framework, assembly (inventory UI), ChassisView, and fault management (EPA wireless repo and related).
- EMS stack: Angular 21 (latest), Harbor and Magnetic design system, Spring Boot primary backend with Go services on the device-management side, PostgreSQL. Three-layer shell app model (Infra UI → Common UI → EMS UI).
- Backend status: "at least 80 percent" of EPNM backend functionality has been reimplemented in EMS. The remaining 10-20 percent gap will be surfaced during Colin's deep dive; gap analysis is part of the POC. Oracle has been fully eliminated from EMS; device images are stored as application assets, not database BLOBs.
- Default login view should be the EPNM classic theme; toggle flips to Magnetic. Confirmed by Akhil.
- The classic UI code must build as part of the new EMS build. Location is Colin's call: a folder inside the EMS UI repository or a separate repository. Colin owes a plan.

**What AI-compliance discussion settled.**

- Cisco hardware only. Cisco-issued accounts only.
- Two tools only: Cisco-issued Claude Code for development, LangGraph running locally on the Cisco laptop for orchestration. No external third-party or cloud-based AI tools.
- Library installation is gated; Colin is the single gatekeeper.
- Repository access via Active Directory groups.
- Precedent: the concurrent NX-OS CI/CD engagement (Colin plus four others, working with Srinivas Pita and Anand Singh) as the operational model. DeepSite (or DeepSeek, transcript phonetics are unclear) was referenced as another Cisco-context tool Colin has worked with.

**What testing and QA discussion surfaced.**

- Cisco's existing test infrastructure spans seven categories (functional, scale, end-to-end, UI, API, migration, upgrade) with thousands of test cases, data-driven coverage across device types and configurations, and existing automation for regression.
- The existing UI tests will not transfer to the classic UI. The DOM is different under Angular; the selectors and Dojo-specific patterns will not match. Jenis and Praveen asked directly whether a replica of existing test cases would be built for the new classic UI. Colin confirmed yes — but scoped the replica work to the full engagement, not the POC.
- POC testing scope is narrow: enough testing to guarantee functional equivalence for the two screens, plus internal unit testing before declaring the POC complete. Full agentic QA, dashboard visibility, and coverage gap analysis are deferred.

**Twelve action items came out of this meeting.** They span AD group access, WebEx team space creation, VM provisioning (one EPNM read-only, one EMS development), Confluence page review, code deep dive and UI mapping, code organization proposal, regression suite identification, and a recurring sync cadence. All twelve are marked pending in the research files; none have been confirmed complete as of the time this handoff is being prepared.

**Source file:** `source/selva_and_team_4-6-2026_formatted.txt`. Research files: `research/07_meeting_*.md`. Screenshots: `source/selva_and_team_4-6-2026__1.png` and `__2.png` (the authoritative attendee list for the meeting).

---

## 2026-04-07 — Technical Research Set (Set 08)

The day after the walkthrough, three technical research documents were produced to give the team a working reference for the POC:

- `research/08_research_epnm_legacy_stack_2026-04-07.md` — Dojo 1.x core concepts, Dijit widget lifecycle, AMD module system, dojo/store API, pub/sub patterns, templating, grids, and the other Dojo primitives the execution session will encounter in EPNM code.
- `research/08_research_ems_modern_stack_2026-04-07.md` — Angular 21 features (signals, standalone components, Material), the Harbor and Magnetic design system, Spring Boot REST patterns, Go services on device management, PostgreSQL migration context, microservices and shell-app patterns.
- `research/08_research_conversion_patterns_2026-04-07.md` — the 25-row Dojo-to-Angular widget mapping, AMD-to-ES6 module mapping, data binding translation (dojo watch to signals or observables), event handling translation (pub/sub to RxJS), lifecycle hook mapping, state management translation (stores to services), the theme toggle architecture using CSS custom properties and a ThemeService, shared service and display adapter patterns, and a proposed folder structure under `ems-ui/src/app/classic/`.

This research material is the immediately actionable technical reference. It is preserved as an integrated working reference in `06_conversion_patterns_reference.md`.

---

## 2026-04-07 Onward — Quiet Period

The research library has no new source events between 2026-04-07 and the 2026-04-20 date of this handoff preparation. During this period, access provisioning (AD groups, VMs) is the primary external blocker — outstanding at the time of the Set 07 walkthrough, with no completion evidence since.

---

## Summary of What Each Meeting Contributed

| Date | Event | What it settled |
|------|-------|-----------------|
| 2026-02-09 | First discovery | BayOne engaged. POC model agreed. Security baseline set. |
| 2026-02-20 | Second discovery | QA framework articulated. Engagement model constraints set. Scope assumed full-stack (later reversed). |
| 2026-03-24 | Hardware delivery | Cisco laptop received. Blocking dependency cleared. |
| 2026-03-25 | Scope reframe | Classic view toggle scope locked. Two-screen POC confirmed (Faults + Inventory). Backend off-limits. |
| 2026-04-06 | Technical walkthrough | Product demonstrated live. Repositories mapped. AI compliance ratified. Access provisioning requested. Testing expectations set. |
| 2026-04-07 | Technical research | Dojo, Angular, and conversion patterns documented as a working reference. |

Every one of these events is preserved in full in the research library. Nothing in this document is a primary source; everything is distilled from the underlying research files.
