# 13 - Meeting: Summary

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-20/srinivas_4-20-2026_formatted.txt
**Source Date:** 2026-04-20 (Monday afternoon Srinivas sync, approximately 30 minutes)
**Document Set:** 13 (Fourth Srinivas team meeting; first of the Mon-Wed-Fri 3x weekly cadence)

---

## Overview

This is the first Srinivas meeting on the new three-times-weekly cadence established in Main Set 12 three days prior. It is also the first Srinivas meeting after the Apr 20 Cisco IT Security incident involving Namita's data-handling violations. The meeting was compressed to approximately 30 minutes and attended by Srinivas, Justin, Anupma, and Colin. Srikar was absent due to travel disruption from a landslide affecting his return; Namita was not present (CSIRT investigation active, access suspended).

The meeting is the single most consequential strategic win in the engagement chain to date. Team Set 10's knowledge graph rebuttal strategy landed cleanly: Colin raised the call-graph versus knowledge-graph distinction as a clarifying question, and Srinivas accepted the pragmatic subgraph approach without friction. Srinivas's own framing at the pivot — "that is good, because that means the problem gets smaller... similar to a knowledge graph, but does not need to encapsulate absolutely everything at all points in time. So that is even better" — reversed Main Set 12's foundational Layer 0 directive within three days.

The meeting also featured a compact incident-acknowledgment exchange. Srinivas asked about Namita's email; Colin gave a diplomatic summary emphasizing process failure (wrong channel) rather than intent or scope; Srinivas accepted the framing and moved on. The engagement's forward trajectory is intact.

Secondary developments: the NX-OS CI bot request was formalized with Singularity skill factory acceptance, the Pulse/Scribbler scope was explicitly deferred, the Wednesday Apr 22 spreadsheet deadline was set for user-issue definition, and the CAT MCP availability via DeepSight marketplace was disclosed with an MCP viewer app releasing in approximately two days.

## What is genuinely new in Set 13

### 1. Knowledge graph directive reframed to on-demand dependency graph

Main Set 12's knowledge graph demand was pre-computed, stateful, and foundational. Set 13 accepted the call-graph-vs-knowledge-graph distinction, confirmed Bazel already provides a dependency graph in .dot structure, and agreed that a full dependency graph "does not need to encapsulate absolutely everything at all points in time." This validates Team Set 10's technical rebuttal and shifts the build log architecture's Layer 0 from pre-computed omniscient graph to on-demand dependency query plus historical snapshots at nightly builds.

### 2. PR backout use case disclosed

Srinivas grounded the abstract architecture in a specific, concrete use case: release lead identifying which PR caused a nightly build failure and safely backing it out with its dependent PRs. The use case has two parts (attribution and safe backout), applies to both build failures and sanity regressions, and requires intelligence about PR interdependencies (including which PRs must be backed out together). This is the primary business driver for BayOne's build-failure analysis MCP endpoint.

### 3. Pulse/Scribbler scope explicitly deferred

Srinivas said directly: "you guys are not part of that technique right now. I think NAGA misunderstood the original thing." Later in the meeting: "for now, hold on. We will bring you guys, but for now, hold on to that." This closes the long-open Pulse scope overlap and the Scribbler A/B testing workstream. BayOne focus narrows to PR analysis, common-issues categorizer, WebEx bot, and the build-failure MCP endpoint.

### 4. WebEx bot request formalized with Singularity skill factory acceptance

Srinivas asked BayOne to build an NX-OS CI bot for curated Q&A auto-reply. Colin pitched the Singularity skill pattern as a "factory to do that and generate that" with a 45-minute repeatable workflow. Srinivas accepted: "create a skill which can create a new bot, right, as required." First client-facing endorsement of the Singularity-as-factory pattern in the engagement chain.

### 5. Bazel MCP directive with on-premander Wit MCP context

Srinivas confirmed a Bazel MCP is needed: "We need to do that." The existing Wit MCP from the on-premander team provides a reference pattern. Initial build ownership is Cisco internal, with Colin as fallback. Scope: per-branch build validation integrated into the code review infrastructure.

### 6. CAT MCP disclosure and MCP viewer app preview

Anupma confirmed the CAT MCP is on the DeepSight marketplace IDE with automatic DeepSight integration. An MCP viewer app releases in "another two days" (roughly Wednesday Apr 22). Colin can use the viewer as a playground to invoke the CAT MCP. This is the first time a Cisco-internal MCP has been disclosed as available to BayOne without deep access negotiation.

### 7. Incident acknowledged at technical director level with diplomatic summary

Srinivas: "I saw email from Namita, access logger or some escalation. Anything, any concern there or are we good right now?" Colin's summary emphasized: team member offboarded for not meeting internal standards, replacement onboarded with full NDA and documents, some files shared via wrong channel, CyberSec flagged due to scraping context misunderstanding, "we are good right now." Colin offered BayOne-ID backup plan if CyberSec disallows third-party contractor scraping. Srinivas accepted and moved on. The incident is now acknowledged at the technical-director level; the full CSIRT record (documented in Team Sets 06 through 06g) is not surfaced.

### 8. Modular/pluggable principle reinforced again

Srinivas: "Please remember that anything you guys are doing should be modular and pluggable to other workflows." Consistent with Main Set 11's operating philosophy and Team Sets 07-10's decoupled service-layer pattern.

### 9. Wednesday deadline for user issue definition

Srinivas: "I am hoping by Wednesday, we will, we would have defined all the user related issues that we want to focus and solve it." Deliverable: Excel spreadsheet or similar listing typical questions to solve. Feeds the common-issues categorizer (Team chain: Srikar's 4,200-message analysis).

### 10. Anupma as collegial technical counterpart

First substantive Anupma contribution in the main research chain. CAT MCP marketplace disclosure is cooperative, not guarded. Closing side-bar with Colin ("I wanted to know the code review what happened") signals a developing working relationship. Parent org chart update warranted.

### 11. Justin direct collaboration pattern

Srinivas: "Justin knows it like the worker so I am asking Colin to talk to Justin." Justin: "I will pass on the command to him." Direct Colin-Justin conversation now sanctioned by Srinivas. Informal in-person Bay Area meeting plan added. The Team Set 10 Justin outreach plan is now operationalized from two directions.

### 12. Point-fix agent vision reaffirmed

Srinivas reaffirmed the code-review-agent-extended-to-build-failures pattern from Main Set 12. "We will use the same infrastructure, we will use it here." Timeline unchanged (approximately 3-4 weeks to production per Justin's Main Set 12 disclosure).

## Status of the Main Workstreams After Set 13

**Build log / PR backout track:**
- Layer 0 is on-demand Bazel dependency query, not pre-computed knowledge graph
- Primary business driver: release-lead PR backout use case (attribution + safe backout with dependencies)
- BayOne deliverable: build-failure analysis MCP endpoint feeding Cisco's code review agent
- Justin 1-on-1 on Bazel dependency commands scheduled informally
- Historical snapshots at nightly builds provide statefulness without live re-indexing

**WebEx / pain point / bot track:**
- Common-issues categorizer in progress; Srikar working on it Apr 20
- Spreadsheet deliverable due Wednesday Apr 22
- NX-OS CI bot request formalized with Singularity skill factory acceptance
- Pulse/Scribbler explicitly deferred; no longer BayOne's concern for this phase
- Bot deployment still subject to Main Set 12 governance (Cisco IDs, repos, CICD pipeline)

**MCP ecosystem:**
- BayOne builds build-failure analysis MCP endpoint
- Cisco builds Bazel MCP (BayOne as fallback)
- Wit MCP already exists (on-premander team)
- CAT MCP available via DeepSight marketplace (Anupma sending link)
- MCP viewer app releasing ~Wednesday Apr 22 as BayOne playground

**Access and infrastructure:**
- DeepSight read-level access achieved (Colin can reference reports in conversation)
- Permanent ADS routing to Mahaveer Jinka explicitly (Srinivas defers ownership)
- CAT MCP available without deep access negotiation
- MCP viewer app provides access to the MCP ecosystem without full platform integration

**Incident response (tracked in Team Sets 06-06g):**
- Acknowledged at Srinivas level with diplomatic summary
- No surface damage to engagement trajectory
- GPS findings pending (timeline unchanged)
- Anand's Apr 16 contract extension (Team Set 06d) remains the commercial floor

**Carried forward (not yet addressed):**
- WebEx meeting recording extraction (owner-only API constraint) — not raised
- Alternative-deployment forcing function — not raised
- Decisions Requested slide items — not raised
- Full Rui/Nexus T scope alignment — not fully raised (Pulse scope closed)

## Files in this set

- `13_meeting_people_2026-04-20.md` — attendees, dynamics, absences (Srikar landslide, Namita CSIRT)
- `13_meeting_open_items_and_scope_updates_2026-04-20.md` — ADS routing, Pulse/Scribbler deferral, common-issues progress
- `13_meeting_knowledge_graph_reframe_landed_2026-04-20.md` — the Set 10 strategy validated, Srinivas acceptance captured
- `13_meeting_pr_backout_use_case_2026-04-20.md` — release lead workflow, PR dependencies, small edge graph scope
- `13_meeting_bot_creation_and_mcp_ecosystem_2026-04-20.md` — NX-OS CI bot, Singularity factory, Bazel MCP, CAT MCP, MCP viewer
- `13_meeting_incident_acknowledgment_2026-04-20.md` — diplomatic disclosure, what was surfaced and what was omitted
- `13_meeting_cadence_and_wednesday_deadline_2026-04-20.md` — Mon-Wed-Fri active, Wednesday spreadsheet deadline, forward items
- `13_meeting_summary_2026-04-20.md` — this file

## Bridge document

`12-13_changes_2026-04-20.md` covers the three-day progression from Main Set 12 (Apr 17 redirect-heavy meeting) to Main Set 13 (Apr 20 reframe-accepted meeting). Focus on the Set 10 rebuttal's predictive accuracy, Srinivas's sentiment stability through the incident, and the scope crystallization that emerged.

## Significance for the Engagement

Set 13 is the first meeting in the engagement chain where BayOne's internal strategy (from Team Set 10) directly produced a client-meeting outcome (Srinivas acceptance of the on-demand dependency approach). The internal-analysis-plus-public-diplomacy pattern is validated. The engagement is stable through the incident. The scope is clearer than at any prior point. The Mon-Wed-Fri cadence enables the weekly deliverable rhythm through the contract renewal window.

The next Srinivas sync is Wednesday Apr 22; the Friday Apr 24 sync follows. The Wednesday spreadsheet deliverable is the immediate next milestone. The Justin 1-on-1 on Bazel dependency commands is the next structural move. The Apr 22 MCP viewer app release is the next Cisco-side milestone that affects BayOne's work directly.

## What is next (from Set 13 perspective)

- Tuesday (Apr 21): Srikar works on pain point deep-dive; Namita status contingent on CSIRT
- Wednesday (Apr 22): User-issue spreadsheet deliverable to Srinivas, MCP viewer app release, next Srinivas sync
- Friday (Apr 24): Week outcomes sync
- Informal: Colin-Justin 1-on-1 on Bazel dependency query commands
- Informal: Colin next Bay Area visit, in-person with Justin
- Incident: GPS findings pending, contract renewal floor intact
- Next phase: MCP endpoint design for build-failure analysis, 3-4 week runway to align with Justin's code review infrastructure production
