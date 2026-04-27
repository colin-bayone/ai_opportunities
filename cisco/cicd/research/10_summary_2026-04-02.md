# 10 - Meeting: Summary

**Source:** /cisco/cicd/source/srini_team_meet_04-02-2026.txt
**Source Date:** 2026-04-02/03 (CI/CD Track Sync Up with Srinivas's extended team)
**Document Set:** 10 (First meeting with Srinivas's full CI/CD team)
**Pass:** Summary of all Set 10 documents

---

## Overview

Set 10 is the turning point from preparation to execution. After months of delays (procurement, hardware, access), this is the first meeting where actual work is assigned. Srinivas organized a CI/CD Track Sync Up with his extended team — introducing Colin to Anupma Sehgal (DevEx), Justin Joseph (build infrastructure), and establishing a recurring cadence.

This meeting is more technically detailed than any prior source. It reveals the MCP architecture, call graph strategy, database landscape, build log analysis requirements, and the user consumption model (self-serve + agentic) that will define the engagement's output.

## Files in This Set

| File | Focus |
|------|-------|
| `10_meeting_people_2026-04-02.md` | Anupma Sehgal (new, DevEx lead, co-owns pipeline, guarded about databases), Justin Joseph (new, build infra, MySQL, existing MCP), Srinivas in orchestration mode, Naga/Mazar/Tim referenced |
| `10_meeting_technical_architecture_and_mcp_2026-04-02.md` | Call graph from CLAM/LAM, MCP strategy (inventory→evaluate→create), dual consumption model (self-serve + agentic), database landscape (MySQL, Cassandra, NFS), build log analysis, inference cost warning |
| `10_meeting_first_tasks_and_roadmap_2026-04-02.md` | First tasks: WebEx scraper + Justin meetings. GitHub MFA still blocked. Four-phase roadmap emerging. Two on-site team members offered. Twice-weekly meetings. |
| `09-10_changes_2026-04-02.md` | Bridge: Rui handoff not mentioned, replaced by user pain point analysis as starting point. Anupma is new org boundary. Inference cost is hard constraint. |
| `10_meeting_summary_2026-04-02.md` | This file |

## Key Findings

1. **The engagement has shifted from preparation to execution.** First concrete tasks assigned. Recurring meeting cadence established. This is the inflection point.

2. **Two new people redefine the team structure.** Anupma Sehgal (DevEx) co-owns the CI pipeline and controls databases BayOne needs. Justin Joseph (build infrastructure) has existing tools and data. Both are technical counterparts, not just access gatekeepers.

3. **The CI pipeline is co-owned across two Cisco organizations.** Divakar's data center team and Anupma's DevEx team. This organizational boundary is a new risk — Anupma was visibly guarded about exposing databases.

4. **MCP architecture is the engagement's technical backbone.** Every data source needs an MCP. Tool calls must serve both self-serve and agentic modes. This is Srinivas's framework for how BayOne's work fits into DeepSight.

5. **Inference cost is a hard constraint.** 4X increase already. Srinivas screened Colin on this in their first meeting. Naive approaches (throwing full logs at LLMs) are explicitly rejected.

6. **The Rui handoff from Set 06 appears to be deprioritized.** Not mentioned at all. The engagement is starting from user pain point analysis (WebEx scraper) and build log understanding (Justin), not from an existing app.

7. **First deliverables are small, fast, and reusable.** WebEx chat scraper, recording transcriber, build log analysis. Srinivas: "these things are very simple things, they should be pretty fast." Colin: "we'll surprise you."

8. **Srinivas wants the full BayOne team engaged.** Requested profiles, wants in-office presence, will assign DeepSight work if CI/CD is blocked. "I don't want them to be idle."

## What We Still Don't Know

- Rui's CI/CD app status and whether the handoff is still planned
- Anupma's willingness to cooperate on database access
- Naga's existing code availability
- GitHub MFA resolution timeline
- Airflow SME identity
- Anand's current sentiment (invited but did not appear to actively participate)

## Engagement State After Set 10

- **First tasks assigned.** The engagement is no longer stalled.
- **Team recognized by Cisco.** Srinivas wants profiles, wants them in the office, will assign work directly.
- **Access still partially blocked.** GitHub MFA, DeepSight, code base access all outstanding. But work can begin on WebEx scraper and Justin meetings without full access.
- **Contract renewal is April 30.** Now 27 days away. The WebEx scraper and build log analysis are achievable quick wins to show before then.
