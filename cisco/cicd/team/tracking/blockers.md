# Blockers

Last updated after: Team Set 14 (2026-04-24 source, processed 2026-04-24)

## Active

| Blocker | Impact | Owner | Escalation | First Seen | Current Status |
|---------|--------|-------|------------|------------|---------------|
| DCN Switching tenant portal not reflecting | Mahaveer granted tenant but managecisco.com does not show it; also need CN-SJC-STANDALONE bundle | Namita | Srinivas | Team 01/02 | Partially resolved (grant exists) but two remaining gates before permanent ADS |
| Training course access via edcast.com | Correct link found but A2G_group membership required via oneaccess.cisco.com | Team | Cisco support | Team 01/02 | Justin provided correct URL 4/9; access enrollment pending |
| Pulse/Scribble repo access on DeepSight | Cannot evaluate Naga's existing WebEx tools; blocked on Naga sharing repo links | Srikar | Srinivas/Naga | Team 01/02 | ci-cd team access granted 4/15; Pulse/Scribble still inaccessible |
| WebEx API owner-only meeting access | Only meeting owners can extract recordings/transcripts via API; constrains Task 2 automation | Srikar | Architecture decision | Team 02 | Discovered 4/15; needs discussion with Srinivas |
| Saurav Cisco MacBook failure (INC10796337) | Device dead after macOS update 4/14. WebEx SDK research, Docker/Podman deployment, DCN tools repo docs lost. Working from BayOne machine only. | Saurav | Colin escalation to Srinivas + Anand (Team 08) | Team 02e | **Escalating 2026-04-15 (Team 08):** Cisco IT verdict is 1-2 month repair with loaner. Colin to forward Saurav's fact-driven email to Srinivas + Anand today; fallback plan is BayOne buys Mac under SAL if no resolution in one week. Expected outcome: new machine + old-hardware priority recovery for files only. |
| Refurbished-hardware policy applies to all red-badge contractors | Systemic risk: Saurav's failure may repeat for Namita, Srikar, Vaishali | All (team-level risk) | Colin / Cisco IT policy level | Team 08 | Saurav: "everyone should have same, so there might be some issues coming on your ends as well." Colin considering preemptive SAL purchases as contingency. |
| DeepSight platform access — 4 weeks, still none | Cannot access DeepSight despite Srinivas being the owner. Team has no access to the core platform they are building for. | Colin | Srinivas | Team 04 | Colin escalating to Anand. "4 weeks into the project and we still don't have access to the thing Srinivas himself owns." |
| Three separate GitHub Enterprise servers | Access must be requested separately on each GHE instance. Multiplies every access request by 3. | All | Cisco IT | Team 04 | Structural issue, not resolvable by one person. |
| Rui Guo / Nexus T scope conflict | Rui already built failure analysis agent with GPT 5.4 (auto-triage, topology views) that directly overlaps BayOne's Task 3. Three-way overlap with Justin's work. | Colin | Srinivas | Team 04 | Must clarify before committing architecture. "What are we doing here?" |
| No documentation in any Cisco repo | Zero repos have documentation. Every access grant requires code archaeology before work can begin. | All | Cisco teams | Team 04 | Compounds ramp-up time on every new access. |
| Divakar perceives conflict with BayOne scope | Could block collaboration on build log analysis if not resolved | Colin | Srinivas | Team 01 | Raising with Srinivas today, diplomatically |
| Naga's scope unclear for Pulse/Scribble | Cannot determine if we extend, replace, or parallel-build WebEx tools | Srikar/Colin | Srinivas | Team 01 | Raising with Srinivas today |
| Colin does not have Cisco laptop yet | Cannot access Cisco-internal resources directly | Colin | BayOne ops | Team 01 | In process |
| Cisco IT flagged Wall-E bot as non-compliant | Saurav's bot requires org registration; <100 user cap conflicts with 300-user NxOS group | Saurav | Cisco IT / Naga / Justin | Team 07 | Received email from Cisco IT Apr 13; team to clarify with Naga/Justin if they already have provisioned tokens |
| Codex/Copilot access pending | Team cannot use Cisco-sanctioned AI tools yet; forced to covert Claude Code use | All | Cisco IT | Team 07 | Requested via appstore.cisco.com Apr 13; waiting on provisioning |
| Docker Desktop IT approval pending | Team has Podman (auto) but Docker Desktop requires IT admin request | All | Cisco IT | Team 07 | Requested; unblocks POC flexibility |
| A2G granted but no GitHub visibility (Srikar, Saurav) | Access email received but repos not visible; requires Justin ping per Namita | Srikar, Saurav | Justin | Team 07 | Namita is only team member with successful access; she will teach the steps |
| BayOne-owned GitHub repo at Cisco not yet created | No shared team code/doc/deep-dive location | Colin | Srinivas + Anand | Team 07 | Colin will bug Srinivas this week |
| Vaishali waiting on Cisco hardware | Cannot request Codex/Copilot/Docker; log-side work gated until hardware arrives | Vaishali | BayOne ops | Team 07 | Async participation only via Namita handoff until resolved |
| Naga's Scribbler is not a production service | 50-line local Python script running Whisper, no backend/observer. BayOne cannot A/B test without Naga's help (no provisioned API keys) | Srikar | Naga | Team 07 | Diplomatic framing required: architecture-diagrams-first, "let smart people draw their own conclusions" |
| DCN Switching tenant ID portal not reflecting | Mahaveer approved tenant Apr 14 but still not reflecting in provisioning portal — now **3 weeks blocked** | Colin (direct) → Anand (EOD today) | Colin personally escalating today; Anand escalation if unresolved by EOD | Team 09 → Team 14 | **CRITICAL PATH.** Tuesday Apr 21 follow-up: Mahaveer shared docs only, took no action. Colin meeting Mahaveer today (Team 14). Without this, no DeepSight deployment by end of next week. |
| Internal pace / 24-hour delivery expectation | Team has been in background-research mode for 2 weeks; need to shift to delivery mode | All (enforcement: Colin) | N/A (internal) | Team 14 | Colin's firm warning; formal GitHub issues starting Monday; 24-hour update expectation |
| DCN tools retry-mechanism ambiguity | Disagreement whether tool runs build + applies fix + diff, or only generates diff for user. If diff-only, the "retry" loop is less robust than assumed | Namita (code dive) / Justin (verify) | Internal deep dive + Justin's next call | Team 09 | Saurav and Namita disagree; Srikar aligned with Namita; unresolved |
| DCN tools engineering hygiene gaps | No agent.md at repo root, no plugins, no prehooks, no skills, no README; only a build_error_analysis.md under prompt folder. Codex runs "bare bones" | BayOne (proposal) / Justin (approval) | Colin / Justin | Team 09 | Proposed BayOne contribution: add agent.md + skills + grep-based fallback scripts. "Low effort, high output" |
| CI vs CD code coverage mismatch | Justin's DCN tools auto-handles CD (nightly builds) but CI (Bazel dev builds) requires manual log path. Justin's "handles everything" claim is half-true. | Namita (discovery) | Justin | Team 09 | Reinforces Colin's 70/30 verbal-claim rule (Set 07) |
| Duplicate-scraping risk in current DeepSight model | If every user runs Pulse locally, same chat data scrapes into N separate DBs. For CICD team, 4+ duplicate DBs for identical data. | Architecture | N/A (architectural argument) | Team 09 | Core rationale for shared-service-layer pattern in Friday deliverable |

## Resolved

| Blocker | Resolution | Resolved Date |
|---------|-----------|---------------|
| ADS machine temporary access | Granted (4-week lease, RHEL8) | 2026-04-10 morning |
| GitHub repo access (A2G group) | Access email received, pending verification | 2026-04-10 morning |
| REALM bundle request (CN-SJC-ND) | Request raised and bundle in place | 2026-04-10 morning |
| ADS subdivision question (per-person vs shared) | Resolved: one shared Linux ADS supports concurrent access (Justin confirmed to Namita) | 2026-04-13 (Set 07) |
| Bazel vs Gmake scope question | Resolved on Apr 10 call: Bazel only, Gmake excluded. Reconfirmed 2026-04-13 in Set 07 | 2026-04-10 / reconfirmed 2026-04-13 |
| Pulse/Scribbler scope overlap with BayOne | Resolved 2026-04-15 (Set 09): Pulse and Scribbler are in GitHub on DeepSight org but NOT deployed anywhere, nothing in production. BayOne's architecture work does not displace any working Cisco tooling. | 2026-04-15 (Set 09) |
