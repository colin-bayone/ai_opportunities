# Issue: Build the dynamic answer data path for the CAT issue responder skill

**Repository:** https://wwwin-github.cisco.com/DeepSight/ci-cd
**Branch:** `skills/webex`
**Working folder:** `cat-issue-responder/data_sources/` (create on the branch as part of this issue)
**Dependencies:** Read-only access to Justin Joseph's MongoDB (Justin to provide a generic user ID per Main Set 16 commitment); NX GitHub repository access

---

## Description

The WebEx bot answers two kinds of questions, static and dynamic. The dynamic answers depend on real-time PR data: where a PR is stuck, which checks failed, what the commit criteria results were, who submitted it, what branch it lives on. There are two candidate data sources, both reachable in production. The first is the CAT MCP, which you have been prototyping against locally and have a working schema view of. The second is Justin Joseph's MongoDB, deployed late last week, which captures GitHub events from the NX repository and contains overlapping content. The bot needs one canonical data path. This issue is the end-to-end work on the dynamic answer data path: the integration code, the source comparison, the coverage validation, the gap analysis, and the answer to which source becomes canonical and why.

The MCP is an access protocol, not a data source on its own. The data underneath could come from the CAT MCP backend, from Justin's MongoDB, or from both with the MCP layer as the access surface the bot reaches whichever the canonical store is. Anupma's PR Checks tab walkthrough in the Monday Cisco-side sync was a third view of related data through the GitHub UI, distinct from the MCP path you are using; it is useful as a sanity check but is not the implementation path. Your job is to build the integration in a way that lets BayOne and Cisco answer the canonical-source question with evidence.

The work you have been doing locally (the `cat_lookup`, `commit_criteria_json`, `raw_json` schema visible in the screenshots you shared) is not currently visible on the `skills/webex` branch. It needs to land there as part of this issue. The branch URL is https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex.

## Technical Approach

Build a Python module that fetches PR data from either source given a PR ID. The module exposes a clean abstraction so the bot caller does not care which source is currently canonical, and so a future fallback or migration is a configuration change rather than a code rewrite.

```
PR ID (from chat)
     |
     v
data_path.fetch(pr_id)        <-- single entry point for the bot
     |
     +---> CatMcpSource         (your existing local prototype, ported to skills/webex)
     +---> MongoDbSource        (read-only access via the generic user ID)
     |
     v
NormalizedPrRecord
  - pr_id, cat_id (resolved)
  - branch, submitter, sha
  - commit criteria results (per category)
  - state, last_seen_at
  - source_used (for telemetry)
```

Both sources should round-trip a representative set of recent PRs, including PRs that passed and PRs that failed. The visible filter on your local sample showed `branch=NULL` and `state="Criteria not met"` across a large window. That suggests either a filter you applied at extraction time or a gap in what your prototype is capturing. Resolve this as part of the integration, not as a separate document.

The gap analysis between the two sources lives alongside the code, captured as a markdown file inside `cat-issue-responder/data_sources/` named `source_comparison.md`. Update it as you discover differences. Treat that file as part of the deliverable.

## Tasks

1. **Port the existing CAT MCP work to `skills/webex`.** Create `cat-issue-responder/data_sources/` on the `skills/webex` branch. Move your existing local CAT MCP code into the folder structure. Commit and push directly to `skills/webex` and push daily as the work progresses.

2. **Wrap the CAT MCP path as a class and validate coverage.** Wrap your `cat_lookup`, `commit_criteria_json`, and `raw_json` shape into a `CatMcpSource` class with a `fetch(pr_id) -> NormalizedPrRecord` method. Validate against at least ten recent NX PRs, including at least three that passed all checks. Confirm the `branch` field populates correctly (the visible local sample showed `branch=NULL` across the window, which needs resolution). The current sample shows only "Criteria not met" rows; this validation step verifies the CAT MCP source reports passing PRs as well.

3. **Stand up `MongoDbSource` against the same interface.** Once Justin confirms the generic read-only user ID, write a `MongoDbSource` class with the same `fetch(pr_id) -> NormalizedPrRecord` interface. Inspect the actual MongoDB schema before writing the class; do not assume the fields are identical to the CAT MCP shape.

4. **Build the unified `data_path` module.** Add `data_path.py` that the bot's CAT issue responder calls. It takes a PR ID, dispatches to whichever source is currently configured as canonical, and returns the normalized record. Source selection is configurable so it can change without bot changes.

5. **Run the coverage comparison and recommend the canonical source.** For the same ten to twenty recent NX PRs, fetch from both sources and capture: which fields each source provides, where they agree, where they disagree, where one source is empty. Write findings to `cat-issue-responder/data_sources/source_comparison.md` in the same PR. State which source the bot should use canonically as of this week, why, and what conditions would change that recommendation later. Keep the recommendation grounded in evidence; do not pre-commit a position.

## Testing

**Set up:**
- Branch `skills/webex` checked out locally
- NX repository access confirmed (you can browse PRs)
- Read-only credentials for Justin's MongoDB in your local environment using a `.env.example` pattern

**Functional flow:**
1. Pick five recent NX PRs visible in the browser, mixing passed and failed checks
2. For each PR, run `python -m data_path.fetch <pr_id>` from both sources
3. Verify the normalized record contains: `pr_id`, `cat_id`, `branch`, `submitter`, `sha`, criteria results per category, `state`
4. Confirm the `branch` field is populated for all five (resolves the `branch=NULL` observation from your local sample)
5. Diff the two source outputs for the same PR and capture differences in the comparison markdown

**Edge cases:**
- A PR that exists in NX but has no CAT request yet (very fresh PR)
- A PR that passed all checks (the visible sample showed only failures)
- A PR that was closed without merging
- Malformed PR ID input (string vs integer, padding, branch-prefixed format)

## Acceptance Criteria

**Functionality:**
- [ ] `cat-issue-responder/data_sources/` exists on `skills/webex` with the CAT MCP source ported from local
- [ ] `data_path.fetch(pr_id)` returns a normalized record from the configured canonical source
- [ ] Both `CatMcpSource` and `MongoDbSource` implement the same `fetch` interface
- [ ] At least ten recent NX PRs round-trip through both sources with structured records
- [ ] At least three of those ten PRs passed all checks (confirms coverage is not failure-biased)
- [ ] `source_comparison.md` documents the comparison and recommends a canonical source with evidence

**Code quality:**
- [ ] Module structure is clean and the bot only imports `data_path`, not the underlying sources
- [ ] Configuration of the canonical source lives in one place
- [ ] No hard-coded credentials; secrets pattern follows the project's existing approach
- [ ] Commits land on `skills/webex` daily as the work progresses

**Visibility:**
- [ ] All work is on `skills/webex` and visible to Cisco
- [ ] The folder structure under `cat-issue-responder/data_sources/` is self-explanatory
- [ ] The engagement chat has the link to the latest commit and to `source_comparison.md` per the 24-hour update cadence

## Notes

### Working folder and branch

All code and analysis for this issue lands on https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex under `cat-issue-responder/data_sources/`. Commit and push early so progress is visible; push daily as the work progresses. Your existing local prototype is the starting point, not a do-over.

### Using Codex effectively

The prompt below is a starting point. You own your Codex sessions; expand, contract, or rewrite this prompt as you learn the actual shape of the MongoDB and refine the abstraction. The point is to move with velocity using Codex as your accelerator on the integration, the schema discovery, and the comparison work, not to follow a recipe. Treat this as guidance only.

```
Start here:

I am building the dynamic answer data path for a WebEx bot in the
DeepSight CI/CD repository, working on the skills/webex branch under
cat-issue-responder/data_sources/. The bot answers questions about
Cisco NX repo PRs (where my PR is stuck, which checks failed, who
submitted it, what the commit criteria results were).

There are two candidate data sources to integrate and compare:

1. The CAT MCP. I have a working local schema with these tables:
   - cat_lookup (cat_id, pr_num, pr_url, repo, branch, state)
   - commit_criteria_json (criteria categories: Branch Unit Test
     Enclosure, Merge Approval, NX Build, NX Code Review, NX
     Compiler Warnings, with criterion_detail_states,
     from_aggregate, passed, required)
   - raw_json
   The visible sample from my local prototype is filtered to
   branch=NULL and state="Criteria not met"; I need to confirm
   whether the source actually has passing PRs too and whether
   the branch field populates when the filter is removed.

2. A MongoDB instance owned by Justin Joseph that captures GitHub
   events from the NX repository, deployed late last week. I have
   read-only access pending a generic user ID from Justin.

Help me:
- Design a clean Python abstraction so the bot calls a single
  data_path.fetch(pr_id) and gets a normalized record
- Implement CatMcpSource using the schema above
- Inspect the MongoDB schema first, then implement MongoDbSource
  against the same interface
- Build a coverage comparison script that fetches the same 10 to 20
  recent NX PRs from both sources and reports differences
- Capture findings in source_comparison.md alongside the code

Use the skills/webex branch as the working location. Commit and push
early. Push daily. Keep secrets out of the repo using a .env.example
pattern.
```

Refine that prompt as you go. Switch to a more focused version once the abstraction shape is settled and you are iterating on schema discovery.

### Coordination

- **Justin Joseph (Cisco):** owns the MongoDB. Per Main Set 16 he committed to provide a generic read-only user ID. If credentials are not in hand by midweek, surface the gap to Colin so the escalation path can be used.
- **Anupma Sehgal (Cisco):** her PR Checks tab walkthrough showed a third view of related data through the GitHub UI. If you find yourself blocked on schema interpretation or on confirming whether two records describe the same underlying CAT request, she is a good Cisco-side check-in.
- **Colin (BayOne):** standing rule, surface blockers within 24 hours. The 24-hour update cadence on the engagement chat applies to this PR's progress as well.

### Common pitfalls

- Treating the CAT MCP as the data source itself rather than as the access protocol. The data may live in the CAT MCP backend, in Justin's MongoDB, or in both. Keep the abstraction honest about that distinction.
- Validating the local prototype against the same filter that produced your existing sample. Pull a broader window so the validation actually exercises passing PRs.
- Hard-coding the canonical source choice into the bot. The whole point of the abstraction is so a future migration is a configuration change.
- Letting `source_comparison.md` drift behind the code. Update it as you discover differences, not at the end.
- Doing schema discovery in your head rather than by reading the actual MongoDB. Inspect first, then code.

### What this issue does NOT cover

- Chat-side wiring of the bot to call `data_path.fetch`. Separate issue.
- The static FAQ path from the wiki. Separate workstream.
- Bot deployment, compliance, or registration. Separate workstream.

This issue is the data layer. Get this right and the rest is straightforward wiring.
