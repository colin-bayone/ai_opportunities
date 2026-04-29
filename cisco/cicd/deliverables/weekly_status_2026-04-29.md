# Cisco CI/CD AI Engagement Weekly Status

**Week of April 27 to May 1, 2026**
**Last updated:** Wednesday April 29, 2026

---

## Accomplished this week

- **ADS machines provisioned by Divakar.** Two machines, `divvenka-qa-1` and `divvenka-qa-2`, 16 cores and 32 GB each, on the `CN-SJC-STANDALONE` bundle. Spec confirmed live during the Monday sync.
- **CAT MCP PR-mapping resolved end to end.** Anupma's walkthrough confirmed the cache request data path provides the full PR mapping plus rich metadata (branch, submitter, bug ID, SHA, sub-initiator, all checks). The mapping table BayOne expected to construct is not needed.
- **Skills repository destination confirmed.** Develop on the CI/CD repository `skills/webex` branch and promote to the master skills repository (SME KB) once production grade. Confirmed verbatim by Srinivas.
- **WebEx bot deployment identity resolved.** Bot will deploy under the existing `DSA Atlas` / `DSR Class` generic user ID. Anupma to fill the form on BayOne's behalf using BayOne's prior submission as the template.
- **Static FAQ source path agreed.** Bot will scrape the existing NX-OS wiki for static answers, with a chat-to-wiki feedback loop proposed and accepted for surfacing chat-resolved fixes back into the wiki.
- **Justin's GitHub-event MongoDB endpoint shared.** A working endpoint that returns PR status with all checks. Concrete data source for the dynamic answer path; either complementary to or substitutable for direct CAT MCP queries.
- **PR-to-commit mapping documentation, implementation, and rollback flow diagram delivered.** Generic documentation, working `pr_to_commit_mapping.py` against CI build logs and CD diffs with high-confidence mappings and evidence trails per commit, plus a 10-step rollback analysis flow diagram covering the release-lead PR backout use case.
- **`skills/webex` branch is the active working location for the team.** Skills on the branch include `nxos-issue-categorizer`, `cat-issue-responder`, `build-issue-responder`, `codenet-issue-responder`, `sanity-issue-responder`, `issue-response-router` (updated with static-vs-dynamic routing), `webex-bot-builder`, `webex-solution-architect`, and the new `wiki-issue-responder`.

---

## Current work

- **Friday May 1 integrated delivery: CI/CD application chat plus WebEx bot on the NX-OS CI pipeline**
  - Backend (Service Application Platform style, two pluggable frontends): backend feeds both the chat in the CI/CD application and the WebEx bot from one shared source. Architecture in flight.
  - Static FAQ wiring: NX-OS wiki as source of truth. Pending the wiki link from Divakar in the engagement chat.
  - CAT MCP integration (dynamic answer path): wiring this week using either the CAT MCP cache request data or Justin's MongoDB endpoint as the canonical source; comparison and selection in flight.
  - WebEx bot deployment on the NX-OS CI pipeline: bot backend built and validated locally. Awaiting WebEx bot compliance criteria from Cisco IT before resubmission under `DSA Atlas`.

- **Static-vs-dynamic intersection analysis (Srinivas request from Monday)**
  - Last six months of NX-OS chat unanswered questions classified as static (no DB lookup) versus dynamic (needs DB lookup).
  - Six-month toggle on the existing `nxos-issue-categorizer` dashboard.
  - In flight, landing today.

- **Skills on the main CI/CD repository**
  - Nine skills currently committed on `skills/webex` (see Skills currently committed below).
  - Documentation and `ds agent init` pattern validation this week. None blocking.

- **Build dependency graph and PR-to-commit mapping (Namita's track)**
  - Documentation: generic PR-to-commit mapping documentation committed at `build-issue-responder/PR_to_commit_mapping_generic/`.
  - Implementation: `pr_to_commit_mapping.py` reads CI build logs and CD diffs and produces structured JSON with high-confidence mappings.
  - Rollback flow: 10-step incident-analysis-to-rollback diagram delivered, capturing the release-lead PR backout use case.

---

## Open items and access

- **ADS host access for the team**
  - Machines provisioned and reachable from the network.
  - Access to the hosts is gated by REALM user-group membership in `oneaccess.cisco.com` (`CN-ACI-HOSTBUNDLE-GROUP-ACCESS`) or `myid-groups.cisco.com` (`DEVXADS-GROUP`, `NGDEVX-DEV`, `WIT-REALM-GROUP`).
  - Realm Request Access submitted; "email sent to bundle owners" returned. The actual approval path is user-group membership rather than the host-bundle queue. Owner of the user groups not yet identified to BayOne.

- **NX-OS wiki link for static FAQ extraction**
  - Pending Divakar to share the link in the engagement WebEx space.

- **WebEx bot compliance criteria**
  - The non-compliance flag from Cisco IT did not include the criteria. Resubmission under `DSA Atlas` is ready when the criteria arrive.

- **Asynchronous unblocking via the engagement chat**
  - Active. Either side may post blockers between meetings.

The major blockers (ADS user-group access, wiki link, bot compliance criteria) are tracked in Critical path blockers and clarifications needed below.

---

## Critical path blockers and clarifications needed

The items below are on the critical path for Friday's first deployment. Each needs clarification or unblocking from the Cisco side so the team can complete the work in the available window.

1. **ADS user-group access ownership.** The team has been blocked from logging into the provisioned hosts since Tuesday morning despite submitting Realm requests.
   - **Who owns the user groups `CN-ACI-HOSTBUNDLE-GROUP-ACCESS`, `DEVXADS-GROUP`, `NGDEVX-DEV`, and `WIT-REALM-GROUP`?**
   - **Can those memberships be approved today so the team can use the ADS provisioned Monday?**
2. **NX-OS wiki link.** The static FAQ wiring is the source-of-truth pivot from chat scraping to wiki scraping. The work is queued; the link unblocks it.
   - **Can Divakar share the wiki link in the engagement chat?**
3. **WebEx bot compliance criteria.** Resubmission under `DSA Atlas` is ready; the criteria are not.
   - **Can Cisco IT share the compliance criteria so the rebuild can meet them on resubmission?**
4. **PR Apollo and Builder Triaging scope alignment.** Justin's existing MongoDB and the Builder Triaging tool overlap with parts of BayOne's planned work.
   - **Confirm BayOne builds the dynamic answer path on top of Justin's MongoDB plus the CAT MCP, rather than constructing a parallel system.**

---

## Skills currently committed

The following skills are currently committed on the `skills/webex` branch of the DeepSight CI/CD repository. Final repository destination per Skills repository destination decision: develop here, promote to the master skills repository (SME KB) once production grade.

| Skill |
|---|
| build-issue-responder |
| cat-issue-responder |
| codenet-issue-responder |
| issue-response-router (updated this week with static-vs-dynamic routing) |
| nxos-issue-categorizer |
| sanity-issue-responder |
| webex-bot-builder |
| webex-solution-architect |
| wiki-issue-responder (new this week) |

---

## Friday May 1 deployment target

This is the first deployment of the chat-based assistance in the CI/CD application, with a paired WebEx bot on the NX-OS CI pipeline. The initial release is a static and dynamic FAQ. Static entries come from the NX-OS wiki via scrape and indexing. Dynamic answers come through the CAT MCP cache request data or Justin's MongoDB at request time. Both surfaces share the same backend so users can ask the same questions from either the chat in the application or the WebEx bot.

This is a first pass, with incremental improvement to follow as the team uses it and as feedback from team usage and internal testing comes in.

Pre-deployment internal testing is gated on ADS user-group access landing this week.

---

## Architecture overview

```mermaid
flowchart LR
    User1[User in CI/CD App Chat]
    User2[User in NX-OS CI WebEx]
    Backend[Shared Backend]
    Router{Routing}
    Static[Static FAQ from NX-OS Wiki]
    Dynamic[Dynamic via CAT MCP / Justin MongoDB]
    LLM[LLM]

    User1 --> Backend
    User2 --> Backend
    Backend --> Router
    Router --> Static
    Router --> Dynamic
    Static --> LLM
    Dynamic --> LLM
```

---

## Recent closures

Items resolved between the Monday April 27 sync and this update.

- ~~ADS machines provisioned with the agreed 16 core / 32 GB spec~~
- ~~CAT MCP PR-mapping path identified via cache request structure (no mapping table needed)~~
- ~~Skills repository destination confirmed (CI/CD `skills/webex` to SME KB)~~
- ~~WebEx bot deployment identity resolved (DSA Atlas / DSR Class)~~
- ~~Static FAQ source path pivoted to NX-OS wiki~~
- ~~Justin's GitHub-event MongoDB endpoint shared~~
- ~~PR-to-commit mapping documentation, implementation, and rollback flow diagram landed on `skills/webex`~~
- ~~`wiki-issue-responder` skill added; `issue-response-router` extended with static-vs-dynamic routing~~
