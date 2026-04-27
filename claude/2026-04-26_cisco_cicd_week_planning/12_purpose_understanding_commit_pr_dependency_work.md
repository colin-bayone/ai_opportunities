# Purpose of the Build-Track Work and the Three Technical Artifacts

**Date prepared:** 2026-04-27 Monday morning
**Purpose:** Document my corrected understanding after Colin's call-out that I had been conflating three distinct artifacts. This file supersedes my prior version.

**Reading discipline note:** I had access to the distinction in the Friday Apr 24 transcript (Colin's own words: "get these call graph pieces, dependency graph pieces, completely moving both for the build as well as for the PR and commits") and read past it. The transcripts contain the precision; I have to consume that precision rather than collapse it.

---

## The product project goal

The product is a CI/CD AI Assistant for the NX-OS engineering team. It surfaces in two places that share one backend:

- A chat interface in the Cisco CI/CD application running on ADS.
- A WebEx bot on the NX-OS CI pipeline.

Engineers, release leads, and managers ask the assistant questions about builds, PRs, failures, and what to do next. The assistant answers via two paths: static FAQ entries for known recurring questions, and dynamic queries through MCPs (the CAT MCP first; others later) that pull live data from Cisco systems. Output is grounded in Cisco's actual CI/CD state, not in a generic LLM response.

## The release-lead workflow that drives the build-track work

Srinivas described this directly on the Friday Apr 24 call. The build runs with multiple PRs rolled in at once. For example, ten PRs in a single build. One PR is broken and the build fails. The release lead needs to keep the release moving. They cannot wait for the broken PR's author to fix it. So they want to back the broken PR out and rerun the build with the remaining nine.

The catch is that other PRs in the same build may depend on the broken one. Engineers commit on top of each other. PR 10 may have been written assuming PR 7's changes were already merged. If the release lead backs out PR 7, PR 10 also needs to be backed out, or it breaks for a different reason. The release lead needs visibility into the dependency chain before deciding what to remove.

In Srinivas's own words on the call: "PR 10 depends on PR logon, because he fixed on top of that. So we need to identify this dependency. So that knowledge graph we need to break. PR, dependency graph."

## The three technical artifacts (Cisco terminology is muddled — separating cleanly)

Cisco's vocabulary in this area is inconsistent. Different people on the Cisco side use "dependency graph," "call graph," and "knowledge graph" to mean different things in different conversations. The clean separation, per Colin:

### Artifact 1 — Bazel built-in dependency command

A terminal command that ships with Bazel itself. Not custom code, not built by anyone. Anyone running Bazel builds can use it. Same output every time because it is a feature of the tool, not a script.

What it produces: a dependency graph showing the relationships between build automation lines / build targets in a Bazel build. Useful for understanding which build targets depend on which other build targets within a single build run.

Concrete example from the joint chat (Apr 20, posted by Divakar/Justin):
```
bazel --output_user_root=../bazel_cache1 build //bzl-packages/core_64_n9000:compile_info_json_deps_graph
```
Output is a `.dot` file at `bazel-bin/bzl-packages/core_64_n9000/compile_info_json_deps_graph`.

Status: in hand. Built into Bazel. No work to do here other than knowing it exists and using its output as a substrate when relevant.

### Artifact 2 — Commit-to-PR attribution and dependency mapping (Namita's work this week)

Justin had been ideating on a custom script for this. He had not built it. Namita has taken it over.

What it does: given a failed build that contains multiple PRs, identify which PR caused the failure, and identify which other PRs in the same build depend on the failing PR (so the release lead knows the cascade if they back it out). This is the GitHub-level dependency graph that the release-lead workflow requires.

What happened with Justin last week: Namita and Justin worked together. Namita understood and documented Justin's current approach. The internal note that Colin flagged in his correction is that BayOne is not actually going to use Justin's approach — Namita is proposing a better one. The phrasing for Cisco-facing artifacts is "current approach understood and documented from Justin last week," not "approach finalized with Justin."

What happens this week: Namita finalizes and shares the new (better) approach. This is the "deeper mapping framework" being built this week. The output is the GitHub PR-to-PR dependency graph the release lead needs.

Status: in flight this week. Justin's prior ideation is the input context; Namita's new approach is the deliverable.

### Artifact 3 — Call graph for code interconnections within a repository

A separate piece of work that maps how files touch each other within a repository or commit: which functions call which other functions, which files import which other files, which libraries are accessed where. The terminology Cisco uses for this is unstable — "call graph" is one phrase, but it gets confused with "knowledge graph" (deferred separately) and sometimes with "dependency graph" (which usually means Artifact 2 in Cisco usage).

Justin has partial work on this. The transcript phrasing is "the call graph, I think, is partially done. There's been some work there. It's all good things. It just needs to be expanded a little bit bigger and build into a process."

Status: partial, longer-term. Not on the May 1 demo critical path. Tracked but not finalized this week.

## How the three artifacts relate to the release-lead workflow

The release-lead question is two-part: "Which PR broke the build, and if I back that PR out, what else breaks?"

- **Artifact 2** answers both halves of that question for the GitHub-PR-level workflow. This is the primary build-track deliverable for the engagement and the most direct input to the chat assistant.
- **Artifact 1** provides build-target-level dependency information that can be used as a substrate when needed (e.g., to disambiguate which build steps a given commit affects). It does not by itself answer the release-lead question.
- **Artifact 3** is longer-term value: code-level interconnection knowledge that supports deeper analyses such as predicted impact of a code change beyond build-target boundaries. Not on the critical path for May 1.

## Internal versus external phrasing rules (per Colin's correction)

- "Approach finalized with Justin" is wrong for any artifact. We are doing it a better way. The Cisco-facing phrasing is "current approach understood and documented from Justin last week."
- Drop "single-commit attribution." It was awkward and inaccurate.
- Drop Temp ADS qualifiers when describing scripts. Scripts run anywhere with the right network access; the dev environment is for deploying applications, not for scoping where a script can run.
- Do not say anything is "deployed" until an application is actually deployed. Scripts run; applications deploy.

## How Document A (Srinivas-facing) should phrase the build track this week

Section 1 — what the team is working on, build track line:

> Build dependency graph for commits and PRs. Current approach understood and documented from Justin last week. Deeper mapping framework being finalized and shared this week.

Section 3 — current status, build track row:

> Approach work with Justin completed last week. New mapping framework in flight this week.

Document A does not get into the three-artifact distinction. That precision is internal. Srinivas asked for a bird's-eye view, not a methodology breakdown. The chat assistant's release-lead use case is the implicit driver and does not need to be re-explained on the document.

## How Document B (internal companion) should classify the build track

Delivered cumulative inventory under the build / dependency-mapping track:

- Build log analysis PDF (Apr 10, Namita) — already in the catalog
- Log type mapping document — already in the catalog
- Star-schema architecture proposal for CI/CD traceability — already in the catalog
- Architecture and approach document for log processing — already in the catalog
- **Knowledge graph reframe presentation, Apr 20 Monday (Namita and Colin)** — already in the catalog; this is the moment Cisco accepted the existing-graph substrate over a custom-built knowledge graph
- **Bazel built-in dependency command identified and validated as substrate (Apr 20, joint with Justin/Divakar)** — this is the formal ingestion of Artifact 1 into the engagement's known-tools list, not a BayOne build artifact
- **Current approach for commit-to-PR attribution understood and documented from Justin (last week, Namita)** — input context for this week's new approach, not Justin's approach being adopted

Delivered does NOT include:
- A shipped commit-to-PR attribution script (Justin had not built one; Namita's new approach is in flight this week, not shipped)
- A PR-to-PR dependency graph (in flight this week as part of the new framework)
- A call graph (Artifact 3, longer-term, partial)

In Progress this week:
- Namita's new commit-to-PR attribution and dependency mapping framework — finalize and share

Planned to start this week or Future:
- Call graph expansion (Artifact 3) — not on May 1 critical path; tracked but not actively built this week unless main targets land early

## Open uncertainties I want to flag for the team meeting

These do not block drafting. They are precision points the team meeting can confirm.

- Whether Namita's new approach for Artifact 2 uses the SBOM extraction path mentioned in action_items.md item 140, or a different method she is proposing. The "parallel-agent research methodology" phrasing in item 140 suggests the methodology is parallel-agent-driven; the substantive technique is not specified.
- Whether the Bazel command output (Artifact 1) is being consumed as input to Artifact 2's mapping logic, or whether they remain separate streams.
- The exposure surface of the dependency graph: chat assistant only, or also a separate visualization (the "graph type theme" that came up as a longer-term direction in the Friday call).
- Whether "call graph" is the term BayOne wants to use externally for Artifact 3, or whether we settle on different terminology to avoid the muddled Cisco usage.

## Answer to Colin's comprehension check (corrected)

Yes — at the level above, I now have the right separation between the three artifacts and the right framing for what BayOne is delivering versus what Cisco is providing as substrate. Artifact 1 is a built-in Bazel command, not anyone's custom work. Artifact 2 is Namita's new approach to commit-to-PR attribution and dependency mapping, finalized and shared this week, replacing rather than adopting Justin's prior ideation. Artifact 3 is the call graph for code interconnections, partial and longer-term, not on the May 1 critical path. The chat assistant's release-lead use case is what makes Artifact 2 the most consequential of the three for this week.

If any part of this is still wrong, tell me before I touch Document A or B.
