# 01 - Discovery Meeting: Summary

**Source:** cisco/cicd/communications/source/meeting1_anand_srini_divakar-2-17-2026.txt
**Source Date:** 2026-02-17 (In-person discovery at Cisco office)
**Document Set:** 01 (Feb 17 Discovery Meeting)
**Pass:** Summary of all Set 01 documents

---

## What This Set Contains

- **01_discovery_key_findings_2026-02-17.md** -- Technical findings, infrastructure decisions, DeepSight Atlas platform discovery, onboarding requirements, and Srinivas's philosophy for the engagement
- **01_discovery_commitments_2026-02-17.md** -- All commitments made by both sides (12 from Cisco, 7 from BayOne), 18 tracked action items, unanswered discovery questions, and the dependency chain for onboarding

## Top 5 Findings

1. **DeepSight Atlas changes the entire engagement model.** Cisco has a live, production AI platform with SDK, UI framework, and AI stack already built. BayOne is not building from scratch -- the work is to build a CI/CD application on top of this existing infrastructure using MCP integrations and prompt queries.

2. **The existing CI/CD app built by Rui is the starting point.** Srinivas's team already has a CI/CD application that was scheduled to launch on DeepSight Atlas within 2-3 weeks of the meeting. BayOne's role is to take over from Rui's work and extend it based on new requirements.

3. **The infrastructure stack is Cisco-standard, not BayOne's preference.** MySQL (not Postgres), Podman (not Docker), on-premises ADS machines (not cloud), and Splunk access likely restricted. BayOne agreed to align with Cisco's existing standards across the board.

4. **Onboarding has a six-step dependency chain.** Background check, NDA, Cisco hardware, VPN access, GitHub Enterprise training (3-4 hours mandatory), and ADS machine provisioning must all complete before substantive work can begin. ADS provisioning was flagged during the meeting as historically slow with no set procedure.

5. **Srinivas expects extensibility beyond the immediate CI/CD scope.** Every deliverable should solve the current need while simultaneously building reusable infrastructure pieces for what Srinivas called "agentic infrastructure." This is the long-term vision, not a bolt-on.

## Key Decisions Made

| Decision | Implication |
|---|---|
| Build on DeepSight Atlas, not from scratch | BayOne's architecture, UI, and AI stack decisions are constrained by the platform |
| MySQL, Podman, Jenkins as core stack | BayOne aligns to Cisco tooling; no technology selection discussions needed |
| Read-only repository access initially | Development happens in local workspaces; BayOne cannot push code until access is expanded |
| Record all knowledge-transfer sessions | Engineers ramp asynchronously; reduces dependency on live meetings |
| "Quarter starts when access granted" | Engagement clock starts at access, not at SOW signing or fiscal quarter start -- de-risks timeline pressure |

## Critical Open Items

- **31 discovery questions were prepared; approximately 14 were partially answered.** The meeting was compressed due to the Bazel production rollout. A continuation session was scheduled for February 18, and roughly 17 questions (covering developer box instrumentation, coverage tracking, release lead needs, AI governance, and auto-correct boundaries) remain fully open.
- **Five new questions emerged from the meeting itself**, including DeepSight Atlas architecture details, Rui's CI/CD app handoff plan, and the Jira replacement situation.
- **No commitments were marked complete at meeting end.** All 18 action items were in "pending" or "in progress" status. The key dependency chain runs: NDA (BayOne) unblocks DeepSight recording (Cisco) unblocks platform understanding (BayOne), in parallel with GitHub training (BayOne) unblocking repo access and ADS provisioning (Cisco) unblocking code access.

## What This Means for the Engagement Going Forward

The February 17 discovery meeting established that BayOne's technical scope is narrower and more focused than originally assumed -- building an application layer on a mature platform rather than designing infrastructure from the ground up. This is favorable: the AI stack, deployment pipeline, and UI framework are provided. The risk is entirely in onboarding speed. Every path to productive work runs through Cisco's provisioning processes (hardware, VPN, ADS machines, repository access), and the meeting itself surfaced that these processes are known to be slow. The two-week follow-up meeting (~March 3) was the agreed checkpoint to verify that onboarding was on track and substantive work could begin.
