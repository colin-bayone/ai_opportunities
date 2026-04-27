# 07 - Standup: Summary

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/internal_team_meet_4-13-2026.txt
**Source Date:** 2026-04-13 (Monday team plan for the week)
**Document Set:** 07 (Internal BayOne team planning meeting following the April 10 Srinivas call)

---

## Overview

This was the first full-team working meeting after the April 10 Srinivas call. Colin ran a comprehensive debrief of Friday's session and used the meeting to set the shape of the week's work. Two parallel tracks were formalized: WebEx scraping and transcription (Srikar and Saurav) and build log analysis (Namita and Vaishali). The meeting ran for approximately 82 minutes.

The substance of the meeting was a blend of operational planning and architecture coaching. Colin used the transcript space to teach three technical frameworks that the team will apply across the engagement: how to reason about ADS infrastructure, how to structure the Scribbler-versus-WebEx transcription A/B test, and how to approach the build log data model using a star schema keyed on SHA hashes. Saurav brought a well-formed counter-proposal for WebEx scraping architecture (service layer plus database plus MCP plus app or bot on top), which Colin endorsed as exactly the level of thinking BayOne should bring that Cisco has not developed internally.

## What is genuinely new since prior sets

### Vaishali's first team meeting appearance

Vaishali Sonawane attended this meeting. The existing org chart marks her as added in the Apr 17 Friday Sync (Team Set 05 prep and related). This meeting moves her first-team-contact date to Apr 13. She was silent other than closing acknowledgment, so her engagement profile remains unread; she is gated on Cisco hardware.

### Two-track team structure formalized

Prior team sets described the team as one unit. Set 07 explicitly splits the team into a WebEx track (Srikar plus Saurav) and a build log track (Namita plus Vaishali), with Colin planning separate architecture meetings per track. This is the first time that split appears in writing as the operating model.

### Weekly deliverable cadence defined

Each track will now generate its own architecture documentation and Singularity-generated presentation each week. Colin will train both teams on the Singularity workflow. Presentation generation moves from Colin-owned to team-owned. This removes a bottleneck and creates a resilience plan for vacation or illness.

### Wednesday escalation cadence

Colin set a Wednesday-latest deadline for surfacing access blockers to Srinivas, grounded in Srinivas's explicit request on Apr 10 to hear about issues earlier in the week so he can help. Prior sets had no explicit cadence.

### Scribbler's actual state revealed

Srikar clarified mid-meeting that Scribbler is a local Python script running Whisper, not an integrated backend service. This is a material shift from prior assumed framing. It reframes the strategic opportunity: there is essentially nothing in production to replace, which means BayOne's proposal work can position current-state and proposed-state architecture without political friction.

### Namita as the de-facto onboarding resource

Namita is the only team member who successfully completed GitHub Enterprise access using the PDF she shared on Friday. Colin assigned her to teach the rest of the team the procedure. She also corrected the ADS acronym (Aurora Development Server, not Active Directory) and introduced the CI-versus-CD distinction, which created the observation-period workstream.

### Cisco IT flagged Saurav's Wall-E bot

Saurav received an email from Cisco IT stating his deployed bot is non-compliant: it must be registered with the organization, and bots are restricted to groups between 2 and 100 users. Cisco's own NXOS group has approximately 300 users, which violates the bot's own policy. This adds a compliance workstream that did not exist in prior sets.

## Status of the main workstreams

**WebEx scraping and transcription (Srikar and Saurav):**
- A/B testing framework defined: three tiers (raw quality, glossary-augmented quality, compute and scale cost).
- Next dependencies: access to Scribbler repo (blocked by DeepSight access), verbal understanding from Naga about existing WebEx work, and alignment on whether Cisco's current Pulse and Scribbler work overlaps with BayOne scope.
- Compliance blocker to resolve: bot registration and group-size policy conflict.
- Saurav proposed a decoupled architecture (scraper plus DB plus MCP plus app or bot) that Colin explicitly endorsed as the right direction.

**Build log analysis (Namita and Vaishali):**
- Bazel confirmed as the only relevant log type (Gmake ruled out by Srinivas on Apr 10).
- Namita has GitHub and temporary ADS access, has visibility into CI (Bazel dev builds), but lacks CD (nightly builds) visibility.
- Plan: observation period of past and future logs on the temporary ADS machine; structured storage by date, build, source, build type; automation script rather than manual downloads.
- Data model direction: star schema with SHA-hash keys, MCP tool for on-the-fly Git queries, persist only what cannot be regenerated from Git.
- Blocker: traceability gap (Justin told Colin that build-to-commit lineage is not currently captured, which Colin finds surprising since it is metadata).

**Cross-cutting infrastructure and tooling:**
- GitHub Enterprise access in various states across the team (Namita has it working, Srikar and Saurav show "granted" but no visible repos and need to ping Justin, Vaishali is gated on hardware).
- Codex and Copilot access requests submitted via appstore.cisco.com this week for everyone except Vaishali.
- Podman usable today; Docker Desktop request pending IT approval; Saurav has a working Podman-based Wall-E bot using a PG17 Postgres image from AWS's public container registry.
- Claude Code remains in covert use. Colin has it personally installed. Team is not to mention it in meetings with Srinivas. Codex and Copilot are the overt alternative once access is granted.

## Files in this set

- `07_standup_people_2026-04-13.md` — attendance, roles, dynamics, new people
- `07_standup_action_items_2026-04-13.md` — 35 new items plus carry-forward status on prior items
- `07_standup_blockers_2026-04-13.md` — access, compliance, knowledge, scope, hardware, tool-usage, political, and cadence blockers
- `07_standup_decisions_2026-04-13.md` — 17 decisions plus deferred items and cross-cutting themes
- `07_standup_technical_discussion_2026-04-13.md` — 12 sections covering WebEx architecture, transcription A/B testing, ADS internals, build log data modeling, and architectural critique of Cisco's current work
- `07_standup_summary_2026-04-13.md` — this file

## Bridge document

A separate bridge document at `06g-07_changes_2026-04-13.md` captures what this set validates, invalidates, or adds relative to the previously processed Sets 01 through 06g. This bridge is retroactive: Set 07's source date (Apr 13) predates most of the other team sets (which span Apr 10 through Apr 21), so the bridge frames Set 07 as a gap fill in the chronological record rather than the next step forward in time.

## What is next

- Colin to assign GitHub issues for A/B testing workstreams and log observation script
- Colin to train each team on Singularity presentation generation this week
- Separate architecture meetings for each track (WebEx and logs)
- Colin to escalate access blockers to Srinivas on Wednesday if still outstanding
- Team to connect with Naga and Justin to understand existing WebEx and Scribbler state and to unblock A2G provisioning
- Namita to teach the rest of the team GitHub Enterprise access using her Friday PDF
- Update parent org chart to reflect Vaishali's earlier first-team-contact date (Apr 13, not Apr 17)
