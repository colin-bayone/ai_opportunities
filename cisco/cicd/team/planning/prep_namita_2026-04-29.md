# Prep recap: Namita's status going into the Wednesday Srinivas meeting

**For:** Wednesday 2026-04-29 Srinivas meeting
**Source folder:** `/cisco/cicd/team/source/week_2026-04-27/day_2026-04-29/namita/`
**Files captured:**
- `github.txt` — GitHub comments from issues 17 and 18
- `ROLLBACK_FLOW_DIAGRAM.html` — a polished HTML rollback analysis flow diagram (10 steps, designed and styled)

---

## What Namita reports

**Issue 17 (PR-to-commit mapping generic documentation):** Namita committed the documentation to `https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex/build-issue-responder/PR_to_commit_mapping_generic` under the `skills/webex` branch. Colin reviewed: "the documents look good from my side." Colin requested a diagram via Mermaid (the GitHub-rendered Mermaid, not Mermaid.js) so the readers can visualize the GitHub, Git, and API call interaction. Namita delivered the diagram at `https://wwwin-github.cisco.com/DeepSight/ci-cd/blob/skills/webex/build-issue-responder/PR_to_commit_mapping_generic/PR_TO_COMMIT_MAPPING_PYTHON_DIAGRAM.html` (HTML rather than Mermaid; see below).

**Issue 18 (PR-to-commit mapping implementation):** Namita committed `pr_to_commit_mapping.py`. The script reads either a CI build log or a CD diff directory and produces a JSON file that maps pull requests to the commits associated with them.

For a CI log: looks for structured build payloads with fields like `pr_id`, `sha`, `user_id`, `branch`, `label`, `github_url`, `start_time`.

For a CD diff directory: scans `.diff` and `.txt` files, extracts PR URLs, commit SHAs, authors, branches, labels, and timestamps from diff headers and `git show` blocks.

The output schema groups data into `pull_requests` (each with `pr_id`, `repo`, `branch`, `commits[]`) plus an `unmapped_commits` list for commits found without a PR URL. Each commit record includes `commit_sha`, `author`, `relationship_type`, an `evidence` array showing the source file and line of every extracted field, and a `confidence` rating.

The sample output Namita provided is from a real CD diff range (`COV_10_7_0_IDV9_0_200-COV_10_7_0_IDV9_0_201`) on the `nx/nx` repository, `nx_dev` branch, with five mapped PRs (86527, 86738, 86647, 86274, 85468) all at high confidence and one unmapped commit (`5efb3c5...` by `nxbld`) at low confidence flagged as `uncertain_association`. The evidence trail per commit includes line-numbered citations into the source diff files, which is solid output design.

## The rollback flow diagram

The HTML file in the source folder (`ROLLBACK_FLOW_DIAGRAM.html`) is a separate, more ambitious artifact. It walks through the full incident-analysis-to-rollback flow in 10 numbered steps:

1. Read PR commits from `diff`
2. Read build data from `fullbuild`
3. Normalize into one model (`commit -> PR`, `PR -> integrated commit`, `build -> change set`)
4. Map PRs to integrated commits (classify as source, merge, squash, rebased, or promotion)
5. Parse failed build logs to identify the first reliable failure signal
6. Map the failing commit back to its root PR
7. Build the dependency graph (hard, soft, promotion)
8. Choose the rollback boundary (single PR, PR cluster, or last good build boundary)
9. Create the rollback recommendation
10. Execute the rollback and validate

Three side panels reinforce the framing: a decision rule ("Do not rollback only by timestamp"), the key output shape ("Rollback Candidate Set"), and the goal ("Safe Rollback Goal: smallest safe revert set that restores a coherent branch state").

The diagram is well-designed (warm earth-tone palette, clear typography, decision-vs-output color coding via left borders). It is not Mermaid; it is hand-coded HTML/CSS. Colin's request was specifically for GitHub-rendered Mermaid for ease of inline display in the repo. The rollback diagram is a separate, more elaborate artifact than what Colin asked for.

## Read for today's meeting

Namita is in materially better shape than Srikar going into this meeting:

- Documentation issue: closed-quality. Colin reviewed and approved. The diagram followed.
- Implementation issue: working code with real output against the actual NX repo. The evidence-trail design and the high-confidence ratings on five mapped PRs is the kind of output that travels well to Srinivas.
- The rollback flow diagram is bonus scope: Namita is thinking ahead to the use case (PR backout for failing builds), not just the immediate deliverable. This is the release-lead PR backout use case from Main Set 13 made concrete.

The Mermaid-vs-HTML mismatch is worth noting but not urgent. Colin asked for Mermaid; she produced HTML. The HTML rollback diagram is excellent work; the question is whether to also produce a Mermaid version for inline GitHub rendering, or treat the HTML as the canonical artifact.

## Concrete asks for the team meeting

- Acknowledge the implementation working against the live NX repo with the sample output as evidence
- Decide whether the rollback flow diagram is in scope for today's Srinivas conversation (it directly addresses the PR backout use case Srinivas grounded the architecture in)
- Resolve the Mermaid versus HTML question for the diagram artifact (one canonical version, not both)
- Confirm whether the issues are ready to close or have remaining work
