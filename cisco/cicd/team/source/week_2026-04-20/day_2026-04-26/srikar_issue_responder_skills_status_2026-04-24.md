# Issue Responder Skills Status

## Summary

Created a small skill family for MCP-backed issue replies:

- `issue-response-router`
- `cat-issue-responder`
- `build-issue-responder`
- `sanity-issue-responder`
- `codenet-issue-responder`

The current working implementation is the CAT path. The other responder skills are scaffolded so future MCPs can follow the same pattern.

## What Is Done

### Issue Response Router

- Added `SKILL.md` with routing rules for CAT, Codenet, sanity, and build issues.
- Added `scripts/route_message.py` for deterministic routing smoke tests.
- Router output now includes `secondary_routes` so a CAT-visible problem can still show possible Codenet/build/sanity follow-up routes.
- Tested routing:
  - CAT/catbot/xFlow message routes to `cat-issue-responder`.
  - Build failure message is classified for `build-issue-responder`, but that responder is still a scaffold and does not produce live build replies yet.

### CAT Issue Responder

- Added full `SKILL.md` workflow.
- Added references:
  - `references/cat_mcp.md`
  - `references/issue_db_schema.md`
  - `references/reply_policy.md`
  - `references/known_gaps.md`
- Added scripts:
  - `parse_message.py` extracts PR URLs, PR numbers, CAT IDs, branch names, and criteria.
  - `sync_cat_lookup.py` loads saved CAT MCP exports into `output/cat_lookup.db`.
  - `cat_reply_context.py` builds structured reply context from the CAT lookup DB and issue DB.
  - `draft_reply.py` creates a draft support response.
  - `live_cat_mcp.py` handles live CAT MCP OAuth, tool calls, and live branch sync.
- Live CAT MCP was tested successfully:
  - OAuth login completed through Cisco SSO/Duo.
  - `whoami` returned `srmadara`.
  - `get_cat_details(cat_id=932668)` succeeded.
  - `sync-lookup --branch nx_main` synced 194 live CAT records into `output/cat_lookup.db`.
- Draft reply generation now uses live cache data.
- The draft highlights mentioned criteria, for example `NX Build: passed` when a user message says it is not met but live CAT data says it passed.
- Draft replies now separate live CAT facts and recommended next action from historical issue-pattern suggestions, so historical patterns are not presented as confirmed root cause.

### Build Issue Responder

- Added scaffold `SKILL.md`.
- Added `references/mcp_contract.md` describing the expected build MCP/tool contract.
- Router can identify build-related messages and point to this responder.
- Not yet connected to a live build MCP or log API.
- No build log parser, lookup table, or draft reply generator has been implemented yet.

### Sanity Issue Responder

- Added scaffold `SKILL.md`.
- Added `references/mcp_contract.md` describing the expected sanity/test MCP contract.
- Not yet connected to a live sanity MCP or result API.

### Codenet Issue Responder

- Added scaffold `SKILL.md`.
- Added `references/mcp_contract.md` describing the expected Codenet/xFlow MCP contract.
- Not yet connected to a live Codenet/xFlow MCP or workflow API.

## Current Working Flow

```text
incoming message
-> issue-response-router
-> cat-issue-responder
-> parse PR/CAT/criterion
-> lookup PR in output/cat_lookup.db
-> fetch/sync live CAT MCP data when needed
-> read CAT commit_criteria
-> optionally enrich with issue DB solution pattern
-> produce draft reply
```

## CAT MCP Tools And Data

Available CAT MCP tools used or inspected:

| Tool | What It Does | Current Use |
| --- | --- | --- |
| `cat_help_for_llm()` | Returns CAT usage guidance and status interpretation rules. | Session/reference guidance. |
| `whoami()` | Returns the authenticated username. | Verified auth/session; returned `srmadara` in live testing. |
| `get_cat_details(...)` | Lists CAT/throttle requests by `cat_id`, `branch`, `org`, `initiator`, or `requiring_approval`. | Primary live data source for the responder. |
| `get_criterion_details(cat_id, criterion)` | Intended to return detail for one CAT criterion. | Tested, but returned all-null details for `CAT 932668 / NX Build`; not reliable as primary source. |

Information available from `get_cat_details`:

- CAT ID
- PR URL and PR number
- branch/project, such as `nx_main`
- CAT state, such as `Criteria not met`
- initiator
- bug ID
- checksum
- project state
- commit criteria map
- per-criterion `passed`, `required`, `from_aggregate`, and `criterion_detail_states`

How the responder uses this data:

- Resolve PR number to CAT ID through `output/cat_lookup.db`.
- Read live CAT state from `state`.
- Read blocking criteria from `commit_criteria`.
- Correct stale user assumptions, for example when a message says `NX Build` is not met but live CAT says `NX Build: passed`.
- Generate a draft reply based on CAT-facing facts first.

CAT MCP limitations observed:

- It does not accept PR URL or PR number directly, so the local lookup table is required.
- It does not explain deeper Codenet/xFlow backend state.
- It does not explain sanity root cause beyond showing `NX Sanity` as passed or unmet.
- `get_criterion_details` may return all-null data, so use `get_cat_details(...).commit_criteria` as the reliable criterion source.
- Auth is OAuth/SSO based. The current prototype stores a local token at `output/cat_mcp_oauth.json`; that file is sensitive.

## Expected CAT Reply Format

For CAT-specific messages, the response should be based on live CAT facts first:

```text
Detected PR:
Matched CAT:
Current CAT state:
Blocking criteria:
Mentioned criterion status:
Recommended reply:
Confidence:
Evidence:
```

For the actual user-facing reply, keep it short:

```text
I checked CAT <cat_id> for PR <pr>. CAT is currently <state>.
The current blockers are: <criteria>.
<Specific correction if user mentioned a criterion>.
Recommended next action: <action based on live criteria>.
```

## CAT Reply Examples

The examples below were checked against live CAT MCP using `get_cat_details`.

### Example 1: NX Build Really Is Blocking

User message:

```text
CAT issue: my PR https://gh-nx.scm.engit.cisco.com/nx/nx/pull/88551 is showing NX Build not met.
```

Expected reply:

```text
I checked CAT 932692 for PR 88551. CAT is currently `Criteria not met`.

Current blockers include NX Build, NX Code Review, NX Compiler Warnings, NX Sanity, NX Static Analysis, Merge Approval, Severity <= 3, Unit Test Complete, and unit-test enclosure criteria.

NX Build is currently unmet, so the next step is to check the NX Build result/log and rerun only if it looks transient. The PR also needs the remaining CAT criteria cleared before merge.
```

### Example 2: User Mentions NX Build, But Live CAT Says It Passed

User message:

```text
CAT/catbot says my PR is stuck: https://gh-nx.scm.engit.cisco.com/nx/nx/pull/88549. Is NX Build still blocking?
```

Expected reply:

```text
I checked CAT 932686 for PR 88549. CAT is still `Criteria not met`, but NX Build is now passed.

The remaining blockers are Branch Unit Test Enclosure, Merge Approval, NX Code Review, NX IDE Code Review Analysis, and NX Sanity.

Recommended next action: confirm merge approval, check the NX Sanity result, and complete or refresh the pending review/enclosure criteria.
```

### Example 3: Merge Approval Issue

User message:

```text
Can someone check CAT for https://gh-nx.scm.engit.cisco.com/nx/nx/pull/88309? Looks like merge approval is blocking.
```

Expected reply:

```text
I checked CAT 930985 for PR 88309. CAT is currently `Criteria not met`.

Merge Approval is unmet. The other current blockers are Branch Unit Test Enclosure and NX IDE Code Review Analysis.

Recommended next action: request or confirm merge approval from the required approver/release lead, and check the remaining enclosure/review criteria.
```

### Example 4: Not Enough Info

User message:

```text
CAT issue: catbot says criteria not met but I do not have the PR link handy.
```

Expected reply:

```text
I could not find a PR URL, PR number, or CAT ID in the message. Please share the PR link, CAT ID, or branch, and I can check the live CAT state.
```

## Known Gaps

- CAT OAuth token is stored at `output/cat_mcp_oauth.json`; this file is sensitive and should not be committed.
- CAT MCP does not accept PR URL/PR number directly. The current implementation addresses this with `output/cat_lookup.db`, a local PR-to-CAT lookup table populated by live branch sync.
- `get_criterion_details` returned all-null data in live testing; use `get_cat_details(...).commit_criteria` as the reliable criterion source.
- CAT MCP does not expose true Codenet/xFlow backend state or sanity root cause. Those should be handled by separate responders (`codenet-issue-responder`, `sanity-issue-responder`, and `build-issue-responder`) once their MCPs/APIs are connected.
