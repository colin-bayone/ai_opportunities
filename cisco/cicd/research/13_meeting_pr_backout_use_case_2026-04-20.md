# 13 - Meeting: PR Backout Use Case (Release Lead Workflow)

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-20/srinivas_4-20-2026_formatted.txt
**Source Date:** 2026-04-20 (Monday afternoon Srinivas sync, first of 3x weekly cadence)
**Document Set:** 13 (Fourth Srinivas team meeting)
**Pass:** Focused deep dive on Srinivas's PR backout use case

---

## Purpose of This Decomposition

This document isolates a single load-bearing passage from the April 20 Srinivas meeting: the moment Srinivas moved the conversation from abstract architecture (call graph versus knowledge graph) into a concrete, named business workflow. That workflow is the release lead's nightly-build triage and pull request backout decision. Because Srinivas himself is a release lead, his description carries first-person authority about the tool's intended primary user, the pain the tool must relieve, and the decision the tool must support. Everything BayOne proposes to build downstream should trace back to this use case.

## The Nightly Build Scenario

Srinivas framed the problem with a concrete event. "Let us say there are 20 PRs that got merged in the nightly build and one PR cause an issue for us." The transcript here contains two artifacts, "got much" for "got merged" and "nightclub build" for "nightly build," both read through to the intended meaning. The scenario is that Cisco's nightly CI run integrates a batch of approximately twenty pull requests at once. When the batch fails, one pull request is the proximate cause, and the release lead's first responsibility is to identify it and remove it so the next nightly can proceed cleanly.

The twenty-pull-request figure is important for BayOne's sizing work. It establishes that the relevant graph is not the entire NX-OS codebase but the much smaller bounded set of pull requests in a particular nightly. The problem is naturally batched by the nightly cadence, and the analysis is naturally scoped to one batch at a time.

## Two Failure Categories

Srinivas then split the failure space into two categories: "the issue could be because of a Sanity issue or the issue could be build failure." A build failure is a compile or link failure, a clearly technical rupture where the build system itself refuses to produce an image. A sanity issue, by contrast, is a regression or smoke test failure. Sanity failures compile cleanly and produce an image, but that image fails one or more tests in the sanity suite. The two categories require different detection approaches, because the evidence surfaces differently. A build failure leaves a compiler or linker error pointing at a specific file or target. A sanity failure leaves a test failure pointing at functional behavior, which may or may not be attributable to any one file in the batch.

This bifurcation splits the attribution problem while leaving the backout problem unified. BayOne's endpoint must therefore handle both inputs (build log parsing and test log parsing) but can share a single backout path.

## Identifying Which Pull Request Caused a Build Failure

For the build failure branch, Srinivas described attribution as tractable. "If it is a build failure first of all we need to say okay, which PR cause that failure that is I am assuming straightforward number one." He qualified this with "I am assuming," signaling the common case is straightforward but not every case. The straightforward case is when a compiler error names a file or target changed by exactly one pull request in the batch. Less straightforward cases arise when multiple pull requests touched the same file or target, or when a pull request introduced a dependency visible only at link time against code from another pull request.

The release lead's tooling therefore needs, at minimum, a per-nightly-build map from failing build artifact to contributing pull requests. That map is computable from git history plus Bazel's dependency output, both of which Cisco already has available.

## The Pull Request Interleaving Complication

Srinivas then introduced the complication that motivates the entire dependency graph discussion. "But sometimes it is possible that people will commit one PR over the other PR. There will be two or three changes that gets merged. So even though you said that this PR caused the issue there will be dependent PRs that also need to be taken care." The insight here is that pull requests within a batch are not independent units. Developers commit against moving heads. Pull request two may be written against a base that already includes pull request one. Pull request three may be written against a base that includes both pull request one and pull request two. The relationships are not visible in a flat list of pull request identifiers; they are visible only when you look at the commit graph and the file and target touches for each pull request.

Three dependency types are implied. First, textual dependency, where one pull request modifies code introduced by another. Second, semantic dependency, where one pull request uses an API or symbol introduced by another. Third, build dependency, where one pull request changes a Bazel target that another also changed. Bazel's existing dependency output speaks most directly to the third type, but the first two are derivable from git and Bazel together.

## The Backout Dependency Intelligence Requirement

Srinivas then stated the behavioral requirement for the tool. "If I say this is PR cause the issue and if the release lead says okay let's back out this PR then you cannot simply back out that PR because that has dependence on PR2, PR3." The naive backout, removing only the identified pull request, is not safe. Removing pull request one without also removing pull request two and pull request three will leave the repository in a state where pull request two references code that no longer exists or pull request three fails to build against a target that was mutated and then un-mutated inconsistently.

The tool's required intelligence is therefore: when the release lead asks to back out a given pull request, the tool must surface the full transitive closure of dependent pull requests that must be removed together. Srinivas made this explicit. "We have to tell the release lead that okay these three PRs need to be backed up together because of so and so reason." The "so and so reason" clause is important. The release lead needs to understand why the system is proposing to remove the dependents, because the release lead will be accountable to the pull request authors for that decision. The tool must surface the dependency edges and evidence for each, not just the resulting set.

The workflow implied is: release lead requests backout of one pull request, tool proposes a bundled backout of that pull request plus its dependents along with human-readable reasoning, release lead reviews and approves, then the tool executes the backout through the nightly build pipeline.

## The Sanity Failure Variant

Srinivas then pivoted to the sanity branch. "Same thing if the issue is because of let's say sanity meaning regression the smoke test." The sanity case carries an additional difficulty. With a build failure, the error message points at a file or target that narrows the attribution problem. With a sanity failure, the test failure points at behavior, and many files across many pull requests could have caused the behavioral change. Srinivas flagged this by saying that in the sanity case "he does not know what caused the issue," referring to the release lead's state of knowledge before the analysis is performed.

## Two Parts of the Sanity Part

Srinivas offered a clean decomposition of the sanity problem. "There are two parts of that sanity part. One is which PR cause the issue, that is a separate one. And given a PR how do I back out it that again falls into the same the build." This yields a two-part model that is useful across both failure types. Part one is attribution, meaning identifying the causing pull request. Part two is safe backout, meaning removing the causing pull request along with its dependents. Part two is common to both failure types. Part one differs. For build failures, part one is comparatively easy because the error message narrows the search. For sanity failures, part one requires correlation between test failures and pull request changes, which is a harder inference problem and probably requires either test-to-source mapping or bisection across the batch.

This decomposition gives BayOne's build-failure MCP endpoint a clean internal structure: an attribution subcomponent and a safe-backout subcomponent, with the safe-backout subcomponent shared between build-failure and potential future sanity-failure invocation paths.

## The Knowledge Graph Intelligence Required

Srinivas then tied the use case back to the architectural reframe Colin had opened earlier in the call. "With the knowledge graph that what we are creating should have intelligence to say how these PRs are interleaved and which PR has dependency on what." The word "knowledge graph" in this sentence is used loosely and should be read as "the graph we build for this use case." It is explicitly not a full call graph or a full semantic index of the codebase. Its contents are pull request nodes, pull request dependency edges, pull request to file mappings, and file to target mappings. It answers one question and only one question: if I revert this pull request, what else must I revert?

The intelligence is primarily structural, not natural language reasoning about code. It is graph traversal over a substrate already produced by git and Bazel.

## Release Lead User Experience Target

Srinivas returned to the user experience in closing. "When the user says I want to back out this particular PR which other dependent PR we need to tell the release leads." And then, on integration, "have a workflow on how to back out that change as a part of the nightly build." Two things stand out. First, the user experience is conversational or at least imperative. The release lead states an intent, and the tool responds with a qualified recommendation. Second, the backout must be executable inside the nightly build pipeline, not merely surfaced as advice on a pull request page. The release lead's workflow is centered on the nightly build, and the tool must fit that workflow end to end: identify, recommend, execute, verify in the next nightly.

This aligns with the single dashboard Srinivas has been describing across prior meetings, where build-related and functional-fix workflows appear together in one release-lead interface.

## Scope Focus: Small Graph, Not Full Knowledge Graph

Srinivas summed up the architectural implication directly. "This small edge graph, when you think you need to take this use case and say that how this use case will work, what are the data structures that we are building behind the scene?" The phrase "small edge graph" is his own, and it confirms the reframe Colin had introduced earlier. What is needed is a per-failure, per-backout graph, not an omniscient always-up-to-date representation of every symbol in the codebase. The data structures should be cheap to compute on demand and should not require continuous background re-indexing. Justin confirmed in the meeting that a full dependency graph scoped this way would be computationally cheap and easy to run at scale.

## Connection to the Knowledge Graph Reframe

This use case validates the reframe captured in document set twelve and the companion document thirteen on the knowledge graph reframe landing. A pre-computed knowledge graph of the entire NX-OS codebase is not required for pull request backout analysis. What is required is a dependency analysis scoped to a specific set of pull requests in a specific nightly build. The substrate already exists. Bazel emits dependency output in a dot-format structure, which Srinivas confirmed when he said, "we do have a build grid dependency graph created and we have that commands available to look at what library binary how they are dependent and what image is getting created all that dependency graph is already there in a dot structure." Git emits the commit chain and the file diffs per pull request. The MCP endpoint BayOne builds takes these two inputs and computes, for one nightly build at a time, the pull request level dependency graph that answers the release lead's backout question.

## Implications for BayOne's Deliverable

The pull request backout use case is now the primary business driver for the build-failure MCP endpoint. The endpoint's scope, stated in terms grounded in this meeting, is: given a build failure, identify the contributing commits and pull requests; given a pull request, identify the dependent pull requests that must be backed out with it; return a reasoned bundle for release lead review; integrate with Justin's functional-fix agent so that any micro-fixes (for example, a missing semicolon or a condition tweak) can be applied in-line without a full revert where appropriate. This is materially more concrete than "build log analysis" as a deliverable framing. It is pull request attribution and dependency-aware backout. The endpoint's value proposition to Cisco is time saved per nightly failure by the release lead, measured against the current manual process of inspecting twenty pull requests one by one.

## Release Lead Persona Implications

Srinivas self-identifies as a release lead in this passage. "I need to be able to figure it out" is spoken in the first person. This reinforces that the release lead is the primary user of the BayOne tooling, not the individual pull request author, not the test engineer, not the build infrastructure engineer. The release lead's needs are: quick attribution when a nightly fails, clear surfacing of dependency edges, confidence that the tool's recommendations are safe, and integration into the nightly cadence. The single-dashboard interface described in Main Set twelve is the logical entry point.

## The Small Dependency Graph Architecture

The data structures implied by this use case are compact. Per nightly build: the list of roughly twenty pull requests integrated in that run; pull request to pull request dependency edges computed from commit chain analysis and Bazel target overlap; pull request to file mapping from git; file to Bazel target mapping from Bazel's dependency output. This graph is computable on demand per nightly build, producible, queryable, and discardable per failure, or cached per nightly snapshot if historical query is needed.

## Statefulness as Historical Tracking

Colin commented on statefulness during this passage. "There will be a statefulness to that, of course, too. So this is, you know, at this moment in time, this is what happened. This is the state of the repository." The statefulness here is scoped to nightly build snapshots, not to continuous live re-indexing. Each nightly build produces a snapshot of the pull request dependency graph for that batch, and those snapshots are queryable after the fact for audit or pattern analysis. This is consistent with Cisco's nightly build cadence. Builds are naturally snapshot events. The statefulness requirement is therefore modest and does not push the architecture back toward the expensive continuous knowledge graph Colin had flagged earlier in the call.

## Closing Observation

This passage is the hinge between the architectural reframe and the concrete engagement deliverable. Before it, the team was debating whether to build a call graph or a knowledge graph. After it, the team has a specific business use case, a specific primary user, a decomposition of the analysis problem, a defined set of data structures, and an endpoint scope. The rest of the engagement's technical design should be driven from here.
