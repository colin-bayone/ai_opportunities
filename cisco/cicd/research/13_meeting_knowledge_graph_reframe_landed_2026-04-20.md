# 13 - Meeting: Knowledge Graph Reframe Landed (Strategic Win)

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-20/srinivas_4-20-2026_formatted.txt
**Source Date:** 2026-04-20 (Monday afternoon Srinivas sync, first of 3x weekly cadence)
**Document Set:** 13 (Fourth Srinivas team meeting)
**Pass:** Focused deep dive on Colin's successful reframe of the Main Set 12 knowledge graph directive

---

## Why This File Matters

This file captures the single most consequential technical exchange of the engagement to date. On April 17 (Main Set 12), Srinivas delivered what amounted to an architectural directive: a knowledge graph should sit as Layer 0 underneath the build log analysis pipeline, providing a stateful, pre-computed representation of the code base that downstream classification layers could query. On the same day, internally, Colin and the BayOne team (Team Set 10 debrief) worked through the technical concerns with that directive and formulated a Monday strategy. The strategy was not to reject the knowledge graph outright, and it was not to cave to the directive either. It was to ask a single clarifying question, "call graph or knowledge graph", that would force Srinivas to engage with the distinction, and then to diplomatically surface the statefulness and computational cost concerns in the client-facing language of architectural caution rather than rebuttal.

On April 20, that plan landed. Srinivas pivoted from the universal-Layer-0 framing to a concrete use case (PR backout dependency tracing), disclosed existing internal work (Justin's "what to build" tool extended via Bazel, with a .dot-format dependency graph already available on demand), and accepted on the record that the subgraph approach is "even better" than the full knowledge graph he had directed three days earlier. This document reconstructs that exchange, links each moment to the Set 10 prediction it validated, and captures the implications for the architecture going forward.

---

## 1. Colin's Opening Frame: The Distinction Question

After Srinivas closed out the open items review and asked whether there were any questions on the architecture he had sent earlier, Colin opened with a single, deliberately narrow clarifying question. "I think maybe just one. So just one distinction because I think there is two things that sound similar but could be the same thing depending upon how you want to think about them. So there is a call graph and then there is a knowledge graph. Just a clarification on which one you want." He immediately followed with, "We can do both. We can do either."

The framing matters. Colin did not push back on the knowledge graph. He did not suggest it was the wrong choice. He asked Srinivas to clarify which of two related but distinct structures he had in mind, offering to build either one or both. This is the Set 10 strategy playing out almost verbatim. The team had agreed internally that the worst move would be to appear to resist the directive, and the most productive move would be to surface the architectural decision as one requiring Srinivas's input rather than as one Srinivas had already made. By phrasing it as a clarification rather than a challenge, Colin kept the decision owned by Srinivas while opening the space for the trade-offs to surface.

## 2. Colin's Technical Definitions

Colin then defined the two terms in a way that made the cost differential visible without announcing it. The call graph he described as "the kind of waterfall almost of exactly what was called for what specific event or code change, all the files that it touches." The knowledge graph he described as "a stateful representation of the code base." He acknowledged that Main Set 12 had mentioned both concepts, saying, "I think last call we talked about both," which avoided the appearance of correcting Srinivas's earlier statement.

The definitions were chosen carefully. A call graph is event-scoped and episodic. A knowledge graph is code-base-scoped and continuously maintained. Stating it this way framed the knowledge graph not as a richer or more powerful option but as a broader and more expensive one, while leaving Srinivas free to say that was indeed what he wanted.

## 3. Colin's Diplomatic Statefulness Warning

With the definitions in place, Colin surfaced the cost concern, but he surfaced it as architectural caution rather than as an objection to the directive. "For a knowledge graph they can get a little bit computationally intensive as they need to be re-indexed whenever new files come in. So we would want to be careful there from an architecture standpoint not to do that on anything that would change frequently because that would create a burden on the computation side for an ADS machine."

He then offered a middle path. "We could still do it a little bit more lightly and you would still get the same impact of knowing exactly what files were touched, what libraries were called, etc. but we can do that a little bit differently." He closed by explicitly preserving Srinivas's optionality. "I just did not want to deviate from that if you really wanted to be a full knowledge graph for the code base."

This is the Set 10 rebuttal converted into client-facing language. The internal team analysis had identified three problems with a pre-computed knowledge graph: the statefulness problem (commits change the state, so any pre-computed graph has a race condition with active development), the cost inversion problem (maintaining an always-current graph would cost more computation than it saves in downstream LLM calls), and the scope problem (the NX-OS code base is large enough that full indexing is nontrivial). Colin expressed the first two as "computationally intensive" and "re-indexed whenever new files come in" and let the architectural implication speak for itself. He did not say the knowledge graph was wrong. He said it would be a burden on the ADS machine Srinivas was working to allocate.

## 4. Srinivas's Pivot to Justin's Existing Work

Srinivas's response was the first signal that the reframe was landing. Rather than reaffirming the full knowledge graph directive, he pivoted. "Before I make this way or that way, I have a chat with Justin and they had built an equivalent, I mean it is not a complete knowledge graph or a call graph, but an equivalent like what to build that way they had and they are also trying to do with the Bazel."

Two things happened in that sentence. First, Srinivas conceded on the record that Cisco does not currently have a complete knowledge graph or a complete call graph. This is significant because the Main Set 12 directive implied the knowledge graph was a relatively natural artifact to build. If Cisco's own engineering teams, operating with full repository access and domain expertise, have not built one, it is prima facie evidence that the full knowledge graph is not as cheap or natural as the directive implied. Second, Srinivas redirected to what Cisco does have: a dependency tool that answers "what to build" given a code change, being extended further via Bazel. That is, Cisco already has the lightweight, query-on-demand structure that Colin was about to propose.

Srinivas then handed off the integration path. "Once you have a deep dive probably you will understand and then after that we will chat. Okay, you can have a separate discussion with Justin." He explicitly asked Colin to talk to Justin.

## 5. Justin's Confirmation

Justin, who was on the call, confirmed the capability in plain terms. "Basically if you change a .c file or something, we can figure out which targets need to be built." This one sentence confirms everything Set 10 predicted. The Bazel dependency infrastructure returns, on demand and given a changed file, the set of build targets that depend on that file. This is precisely the substitute for a pre-computed knowledge graph that the internal analysis proposed: query Bazel at the moment you need the answer, rather than maintain a separate pre-computed structure that mirrors what Bazel already knows.

The change-to-targets query is, architecturally, a subgraph extraction. You enter the dependency graph at the changed file and walk outward to the build targets. You do not need the whole graph materialized; you need the walk result. That is the core of the Set 10 counter-proposal.

## 6. Srinivas's Reframe: PR Backout Use Case

Srinivas then did something important for the engagement. He shifted the knowledge graph conversation from architecture to a concrete use case. He described a scenario where twenty pull requests have been merged (transcribed as "much") in the nightly build and one of them has caused an issue, either a sanity regression or a build failure. As release lead, he needs to identify which PR caused the failure and then, critically, figure out which other PRs must be backed out alongside it because of merge-time dependencies between PRs. "If I say this is PR caused the issue and if the release lead says okay let us back out this PR, then you cannot simply back out that PR because that has dependence on PR2, PR3."

The PR backout use case is covered in detail in a separate file (`13_meeting_pr_backout_use_case_2026-04-20.md`). What matters here is that Srinivas has moved from framing the knowledge graph as a universal Layer 0 requirement to framing it as a capability driven by a specific, concrete operational need. That reframe shrinks the required scope of the dependency structure from "everything about the code base at all times" to "enough to trace PR interdependencies for a given nightly build." This is exactly the narrowing the Set 10 analysis anticipated. A use-case-driven dependency graph is a subgraph, and a subgraph is what BayOne can build pragmatically on top of Bazel.

## 7. The Critical Acceptance Moment

Colin responded to the PR backout framing with the line that closed the reframe. "What we can do from that is you will have, because that is good, because that means that the problem gets smaller."

Srinivas agreed, and the agreement was the strategic win. "That will be a full dependency graph. So similar to a knowledge graph, but does not need to encapsulate absolutely everything at all points in time. So that will make the computation for it significantly cheaper, which will make that much easier to do at some scale. So that is even better."

Every element of the Set 10 position is acknowledged in this reply. The structure is "similar to a knowledge graph" rather than a knowledge graph (terminology preserved, scope narrowed). It "does not need to encapsulate absolutely everything at all points in time" (the pre-computation requirement is dropped). The computation will be "significantly cheaper" (the cost concern is accepted). It will be "easier to do at some scale" (the practical constraint is accepted). And finally, "that is even better" (the narrower option is preferred to the original directive on Srinivas's own language).

For a client-facing architectural exchange, this is about as clean a landing as a reframe can get. Srinivas owns the conclusion. Colin did not reject the directive; he clarified it, and Srinivas chose the narrower path himself.

## 8. Bazel .dot Structure Disclosure

Srinivas then disclosed the substrate BayOne will actually be working against. "We do have a build grid dependency graph created and we have that commands available to look at what library binary how they are dependent and what image is getting created. All that dependency graph is already there in a .dot structure."

The .dot reference is to Graphviz's DOT format, which is the standard textual serialization of dependency graphs in the Bazel ecosystem. Bazel's `query` and `cquery` commands emit dependency information in .dot format natively. What Srinivas is saying is that Cisco's build system already maintains the dependency graph, that the graph can be queried via existing commands, and that the output format is already machine-readable. The "knowledge graph" Set 10 advocated for is not something BayOne has to build from scratch. It exists, it is queryable, and BayOne's job is to integrate its analysis pipeline on top of those queries rather than to construct a parallel structure.

This is the single most important technical finding from the meeting. It collapses a large piece of implementation risk from the engagement.

## 9. Justin-Colin Deep Dive Action Item

The operational consequence of the reframe is an action item. "Justin knows it like the worker so I am asking Colin to talk to Justin." Justin confirmed, "Yeah, I will pass on the command to him."

The Set 10 debrief had independently identified that Colin should reach out to Justin to understand the Bazel build infrastructure in depth. That outreach was going to need to happen through some combination of informal Bay Area coordination and a carefully timed ask. Srinivas introduced the meeting instead. Colin is now to have a dedicated deep dive with Justin, specifically on the Bazel dependency query commands, with Srinivas's explicit endorsement. Whatever the Set 10 plan for getting Justin on the phone was, it has been rendered unnecessary. The exact conversation the team wanted is now scheduled at Srinivas's instruction.

## 10. Statefulness Compromise

Colin then accepted a constrained form of statefulness, which closed the loop on the one element of the knowledge graph directive that had legitimate architectural value. "And there will be a statefulness to that, of course, too. So this is, you know, at this moment in time, this is what happened. This is the state of the repository. This is the state of that PR."

He then constrained it. "These things change maybe not as frequently if they are based on nightlies. But we will have a statefulness to it, too. So you can get the full kind of tracking history of it."

The compromise is historical statefulness rather than live statefulness. The architecture does not attempt to maintain a continuously re-indexed, always-current representation. Instead, it captures snapshots at nightly build boundaries. Each nightly build has an associated dependency graph state, an associated PR merge set, and an associated pass/fail outcome. The resulting structure is stateful in the sense that state is recorded over time, and it is queryable in the sense that any historical nightly build's state can be reconstructed. It avoids the race condition between indexing and active commits because the indexing boundary aligns with the build boundary.

This is consistent with the framing from Team Set 09 and Team Set 10: deterministic, on-demand, with historical snapshots at natural boundaries.

## 11. Implications for the Build Log Architecture

With the reframe accepted, the build log analysis architecture from Main Set 12 can proceed with targeted modifications. Layer 0 is no longer a pre-computed knowledge graph. It is an on-demand Bazel dependency query layer (returning .dot-format subgraphs for a given change or PR set) plus historical snapshots taken at each nightly build. The three-tier classification cascade (regex, then ML classifier, then LLM) described in Main Set 12 remains valid, but now operates on subgraph-extracted context from the on-demand query rather than on context pulled from a continuously maintained graph.

The MCP endpoint BayOne is building (per `12_meeting_functional_fix_and_build_mcp_2026-04-17.md`) returns subgraph-localized analysis. A build failure for a given PR is analyzed against the subgraph of targets that depend on that PR's changed files, not against the full code base. This keeps the context window small, keeps the LLM cost low, and keeps the analysis deterministic where Bazel's own dependency output is deterministic.

The PR backout use case that Srinivas raised becomes a first-class driver for the dependency graph component. The structure is not a general-purpose code-base index; it is a PR-interdependency tracer for release-lead workflows, with the Bazel dependency output as its substrate.

## 12. Contract with Set 10's Rebuttal

Set 10 predicted the landing almost exactly, and the Monday meeting validated the prediction point for point. Set 10 argued that BayOne should use Bazel's dependency output on demand rather than maintain a pre-computed knowledge graph. Srinivas agreed and disclosed that the Bazel dependency graph already exists in .dot format with queryable commands. Set 10 argued that a full knowledge graph would cost more in computation than the LLM usage it was intended to prevent. Srinivas acknowledged the computation cost directly, framing the narrower path as "significantly cheaper." Set 10 argued that continuous re-indexing creates a race condition against active commits. Srinivas accepted nightly-snapshot statefulness instead of live re-indexing. Set 10 argued that the subgraph problem is tractably smaller than the full graph problem. Srinivas said, in his own words, "the problem gets smaller."

The Set 10 analysis was, in effect, a prediction of what Srinivas would accept when the framing was presented diplomatically. It was validated by the actual exchange. This supports a broader pattern that has now played out across multiple Srinivas interactions: the team's approach of producing sharper internal analyses than the public posture allows, and then translating those analyses into gentle clarifying questions for the client conversation, produces better outcomes than either blunt pushback or pure acquiescence. The internal-analysis and public-diplomacy separation is now a documented, validated working mode for the engagement.

## 13. What the Reframe Does Not Do

The reframe is significant but not unlimited, and it is worth being clear about what it does not do. It does not eliminate the knowledge graph concept entirely. Srinivas has preserved the terminology ("similar to a knowledge graph") and may reinvoke the full version if future use cases demand it. It does not give BayOne free rein on the architecture. Srinivas still owns the directive, and the MCP structure, the classification cascade, and the overall Layer 0 through Layer 3 framing from Main Set 12 all remain in effect. The reframe narrowed Layer 0, not the stack.

It does not answer Srikar's scope question from Set 10, which asked whether the work is scoped to full NX-OS, to error-specific pipelines, or to CD-only. The on-demand framing makes that question less load-bearing because the dependency query scales naturally to whatever subset the analysis touches, but the question is still open and will need to be addressed as the use cases are finalized (Srinivas committed to having the user-related issue list defined by Wednesday).

It does not commit to a specific implementation. Colin and Justin need to work out the Bazel query integration in their deep dive, including which specific commands BayOne will shell out to or wrap, how the .dot output will be parsed and fed into the classification cascade, and how the historical snapshots will be persisted. Those details are the subject of the Justin deep dive action item.

---

## Summary

On April 17, Main Set 12 produced a directive that, if implemented as stated, would have committed BayOne to building a pre-computed, stateful, continuously re-indexed knowledge graph of the NX-OS code base. On April 17 evening, Team Set 10 produced an internal analysis identifying the statefulness, cost, and scope problems with that directive and proposed a subgraph-on-demand alternative built on Bazel's existing dependency output. The team designed a Monday framing: ask Srinivas to clarify "call graph or knowledge graph", surface the statefulness concern as architectural caution, and let Srinivas own the decision to narrow the scope. On April 20, Colin executed that framing. Srinivas pivoted to the PR backout use case, disclosed that Cisco already has a Bazel dependency graph in .dot format with queryable commands, said "the problem gets smaller," agreed that the on-demand dependency graph is "even better" than the original directive, and introduced Colin to Justin for a deep dive on the Bazel integration commands.

The Set 10 strategy landed. The knowledge graph directive from Main Set 12 has been reframed to a bounded, use-case-driven dependency graph built on existing Bazel infrastructure with historical snapshots at nightly build boundaries. The architectural cost risk for Layer 0 is substantially reduced. The implementation risk is substantially reduced because the substrate already exists. The client relationship is intact because Srinivas owns the conclusion on his own terms.
