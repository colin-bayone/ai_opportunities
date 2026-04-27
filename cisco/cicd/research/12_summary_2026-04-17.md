# 12 - Meeting: Summary

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-13/day_2026-04-17/srinivas-and-team_4-17-2026_formatted.txt
**Source Date:** 2026-04-17 (Friday afternoon Srinivas meeting, approximately 60-70 minutes)
**Document Set:** 12 (Third Srinivas team meeting; first since the Apr 10 Srinivas guidance call)

---

## Overview

This is the third client-facing meeting with Srinivas and the first since the Apr 10 guidance call captured in Set 11. The meeting was the external delivery of work that the team had prepared internally in the morning session (Team Set 05), and it produced the single most consequential architectural decision of the engagement to date: Srinivas rejected the team's proposed chunking-first build log architecture and demanded a knowledge graph / call graph / build dependency tree approach first.

The meeting also formalized a three-times-weekly Monday-Wednesday-Friday sync cadence starting next week, revealed the substantive state of Justin's CI code review agent infrastructure (active build with agents behind the scenes, three to four weeks from production), and reframed BayOne's role on the functional-fix track as a build-failure analysis MCP endpoint that feeds Cisco's existing agent rather than a standalone triage system.

The meeting ended compressed due to Srinivas's next meeting starting and multiple WebEx screen-sharing failures during Namita's architecture section. Several Set 05 prep agenda items (scope alignment on Rui/Nexus T, Pulse/Scribble alignment, DeepSight access escalation, decisions requested) did not occur and carry forward as open items for next week.

## What is genuinely new in Set 12

### 1. Knowledge graph directive (architectural pivot)

Srinivas delivered a foundational redirect on the build log analysis architecture. The team had proposed an ingestion-parse-chunk-three-tier-cascade pipeline. Srinivas rejected that framing and demanded a knowledge graph (call graph, build dependency tree) as Layer 0. His reasoning: without a knowledge graph, log analysis is guesswork and becomes a year-long project. With a knowledge graph, a failure in one node localizes to a known subtree, the chunking problem becomes subgraph extraction, and root-cause attribution becomes a first-class output rather than an afterthought. Bazel already provides the raw material for the dependency graph; BayOne should consume and structure it rather than build it from scratch.

This redirect reshapes the engagement's build log deliverable from "log analysis" to "log-guided root-cause attribution within a known build graph." Monday deliverable: knowledge graph presentation plus a concrete chunking example.

### 2. Functional-fix agent infrastructure disclosure and MCP directive

Justin disclosed that his team is actively building a CI code review agent with agents running behind the scenes, a review UI with accept/reject/redo affordances, separate read-only mount for code review running parallel to the build, production target approximately three to four weeks out. Srinivas's directive to BayOne: do not build a separate agent; build a build-failure analysis MCP endpoint that feeds Cisco's existing agent. Seamless user experience across functional and build issues through a single dashboard. "Do not think in terms of agent. Think from an endpoint point of view. Context engineering, not agent building."

This is a major scope clarification. BayOne's deliverable shifts from a standalone triage system to an MCP endpoint consumed by Cisco's agent infrastructure. It also resolves the long-running Rui/Nexus T scope-overlap concern implicitly: if BayOne builds the build-failure MCP and Rui's Nexus T builds the functional-fix side, they are complementary not competing.

### 3. Three-times-weekly sync cadence

Srinivas formalized Mon-Wed-Fri 30-minute syncs starting next week, superseding the prior twice-weekly rhythm. Rationale: "we are moving little bit slow" and the next two to three weeks need close coordination. Feedback loop explicit: "the goal post will change based on the outcome." This elevates the engagement into a more intensive phase through the contract renewal window and requires weekly deliverable readiness from both tracks.

### 4. WebEx bot vision formalized

Srinivas articulated the WebEx bot vision in client-facing terms for the first time. Auto-reply to known questions with "at-bot" tagging, escalate unknowns to human with "at-human" tagging, estimated 80-90 percent noise reduction. Scope expansion: from passive Q&A to active action in the workflow itself. "If I move this is the response as AI assistant, then I can start taking the action or suggesting the action in real time to the user, not waiting for asking the question."

### 5. Bot deployment governance directive (non-negotiable)

Srinivas delivered the non-negotiable deployment rule directly: all bot and agent deployments must go through Cisco IDs, must be committed to Cisco repos (DeepSight repo acceptable; BayOne now has access), must pass through the CICD pipeline, no private deployments, no shortcuts. This applies to all deployments including bug fixes. This codifies the rule Cisco IT used to flag Saurav's Wall-E bot in Set 07.

### 6. Colin's three-levers automation framework articulated to Cisco

Colin introduced BayOne's operational framework for AI-applied automation decisions: impact (downstream consequences), complexity (likelihood a human is needed to verify), experience (historical confidence on this fix class). Srinivas validated the framework. This framework now informs the MCP endpoint design: the endpoint should return enough metadata for the automation layer to make impact/complexity/experience judgments.

### 7. Pain point volume reframe ("smaller than expected")

Colin observed that 4,200 messages over three years across dev/stage/test/prod is low relative to what he expected for a 750-person team on a 15-million-line codebase. Implication: either errors are not all being captured in WebEx or the real issue is elsewhere. Two error categories BayOne can address: extractable (build errors, auto-captured) and submitted (runtime errors, user-reported).

### 8. WebEx-to-GitHub traceability gap

Colin surfaced that WebEx messages are not traced back to GitHub resolution. Proposal: accompany new WebEx messages with auto-generated GitHub issues so the workflow stays traceable end-to-end. This links to the new time-to-resolution metric (measures end-to-end fix completion time, complements the first-response-time metric that the bot addresses).

### 9. Justin's collaboration posture

Justin's participation in this meeting (he joined mid-meeting) read as collaborative rather than turf-protective. His disclosure of the functional-fix agent scope and his affirmation that BayOne should build the build-failure MCP endpoint to feed his existing agent is the exact integration-not-replacement posture Colin coached the team toward in Sets 07 and 08.

### 10. Meeting ended compressed, not clean

Set 05 prep had planned eight sections. Four sections were either truncated or did not occur:
- Scope alignment (Rui/Nexus T, Pulse/Scribble) — did not occur
- Access items (DeepSight, tenant ID portal) — did not occur
- Decisions requested (alternative-deployment forcing function) — did not occur
- WebEx meeting recording extraction — did not occur

Cause: Srinivas's next meeting starting plus multiple WebEx screen-sharing failures during Namita's architecture section.

## Status of the Main Workstreams After Set 12

**Build log analysis track:**
- Architecture redirect to knowledge graph as Layer 0
- Monday deliverable: knowledge graph presentation plus concrete chunking example
- Bazel dependency output to be consumed as raw material
- BayOne builds the MCP endpoint for build-failure analysis
- Justin's functional-fix agent provides the downstream consumer (three to four weeks from production)
- Chunking logic demoted from solution to subgraph extraction detail
- Three-tier classification cascade remains valid, operates on subgraph-extracted context

**WebEx / pain point track:**
- Srikar's 4,200-message 25-category dataset landed well
- Monday deliverable: top-5 category deep-dive with sub-error classes and CI pipeline stage context
- Bazel as its own category (one-time migration issue)
- Live dashboard drill-down capability offered (set aside, may surface Monday)
- Bot partnership with Justin confirmed; Saurav's Wall-E work continues on loaner laptop
- Bot deployment governance codified
- Time-to-resolution metric added as a new workstream; requires GitHub access

**Infrastructure and access:**
- DeepSight access still pending (not raised in meeting but remains a blocker)
- GitHub access for time-to-resolution metric (new ask)
- Tenant ID portal (Set 09) not raised
- Alternative-deployment forcing function (Set 05 prep) not raised

**Open items carried forward (did not occur in meeting):**
- Rui/Nexus T scope alignment
- Pulse/Scribble scope question
- DeepSight 4-week escalation
- Decisions Requested slide items
- Saurav's laptop escalation (Set 08)
- WebEx meeting recording extraction owner-only constraint

## Files in this set

- `12_meeting_people_2026-04-17.md` — attendees, dynamics, Justin joining mid-meeting, Vaishali/Tanuja observers, Anand background
- `12_meeting_pain_point_and_bot_strategy_2026-04-17.md` — Srikar's presentation, Srinivas's bot vision, deployment governance, time-to-resolution metric
- `12_meeting_build_log_architecture_proposal_2026-04-17.md` — Namita's proposed architecture (pre-redirect): ingestion, parse, chunking, three-tier cascade, simple first
- `12_meeting_knowledge_graph_redirect_2026-04-17.md` — Srinivas's architectural pivot; the most consequential file in the set
- `12_meeting_functional_fix_and_build_mcp_2026-04-17.md` — Justin's agent infrastructure, Srinivas's MCP endpoint directive, scope division
- `12_meeting_automation_levers_and_verification_2026-04-17.md` — Colin's three-levers framework, surgery metaphor, topic-branch model
- `12_meeting_cadence_and_next_steps_2026-04-17.md` — 3x weekly cadence, Monday deliverables, skipped sections carried forward
- `12_meeting_summary_2026-04-17.md` — this file

## Bridge document

`11-12_changes_2026-04-17.md` at the same location covers the progression from the Apr 10 Srinivas guidance meeting (Set 11) to this meeting. Focus on architectural evolution, scope clarifications, cadence progression, and the team maturity signals between the two sets.

## Significance for the Engagement

Set 12 is a redirect point. The engagement's build log track now has a new foundational requirement (knowledge graph) that was not on the Set 05 prep agenda. The WebEx/bot track has clearer governance (deployment rules) and clearer scope (bot partnership with Justin). The functional-fix track has clearer scope division (BayOne does MCP endpoint, Cisco does agent). The cadence change (3x weekly) means this pace of decisions continues through the next two to three weeks.

The Monday meeting (Apr 20) will be the first test of whether BayOne can deliver against the redirect in three days. The knowledge graph plus chunking example plus top-5 category deep-dive is a substantial ask on compressed timeline, with Saurav still on a loaner laptop and several Cisco-side access items still outstanding.

## What Happened After Set 12

The engagement was hit by the Apr 20 incident (Namita data-handling violations, CSIRT investigation) documented in Sets 06 through 06g. The knowledge graph deliverable and the Monday category deep-dive were subsumed by the incident response. Colin escalated the laptop blocker from Set 08 concurrently with incident damage control. The next non-incident Srinivas meeting is Set 13 (Apr 20 tech review with Justin and Anupma, pending processing).

## What is next (from Set 12 perspective)

- Monday Apr 20 sync: knowledge graph presentation, top-5 category deep-dive, concrete chunking example (actual outcome: preempted by incident)
- Wednesday Apr 22 sync: progress check (actual outcome: Apr 22 Wed Standup captured for team processing)
- Friday Apr 24 sync: week outcomes (actual outcome: no transcript yet per session tracker)
- Bazel dependency output access for knowledge graph construction
- GitHub access for time-to-resolution metric
- MCP endpoint design work (3-4 weeks runway to Justin's infrastructure production)
- Revisit the skipped sections (Rui scope, Pulse/Scribble, DeepSight escalation) in subsequent syncs or email follow-up
