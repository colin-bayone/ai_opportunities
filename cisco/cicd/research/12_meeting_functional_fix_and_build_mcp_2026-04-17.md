# 12 - Meeting: Functional Fix Infrastructure and Build MCP Endpoint

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-13/day_2026-04-17/srinivas-and-team_4-17-2026_formatted.txt
**Source Date:** 2026-04-17 (Friday afternoon Srinivas meeting)
**Document Set:** 12 (Third Srinivas team meeting)
**Pass:** Focused deep dive on Cisco's functional-fix agent and BayOne's MCP endpoint role

---

## Overview

The April 17 Friday sync with Srinivas produced a scope-defining moment that meaningfully changes the deliverable contour of the BayOne Cisco CI/CD engagement. Justin Joseph joined the meeting partway through, and in response to a question about how a build-failure auto-fix workflow would function from a user perspective, Justin disclosed that his team at Cisco is actively building exactly that kind of system already. His disclosure, combined with Srinivas's immediate reframing of BayOne's role, converts what BayOne thought it was building (a triage and auto-fix capability with its own agent logic and its own user interface) into something narrower and more integrationally disciplined (a build-failure analysis Model Context Protocol endpoint that plugs into the agent infrastructure Justin's team is already constructing).

This section captures that scope-defining exchange in full detail. It is the paired companion to the knowledge graph redirect captured elsewhere in the research stream, because the two directives together define what BayOne is actually being asked to build: a knowledge-graph-grounded context engineering service, exposed as an MCP endpoint, consumed by an agent BayOne does not own.

## The Functional Fix Agent Disclosure

The disclosure came when the team was discussing how a user would interact with a build-failure auto-fix. Colin had been walking through the idea of a user comment triggering a Codex session that would attempt a fix. Srinivas was building out his vision of placing that capability on the build page itself rather than forcing the user back into their workspace. At that point, when the conversation turned to how the user accepts or rejects suggested changes, Justin stepped in and revealed that Cisco already has a working infrastructure for this pattern on the functional-issue side.

Justin's own words, delivered to the group without ambiguity: "what we are doing is as a part of the CI pipeline code review what we are doing is we have agents behind the scenes running where it can actually fix the functional issues meaning I have a functional failure and I want to fix it." He continued to describe the user interaction model: "the agents will be providing a UI for the engineer to interact to say I accept the comment I reject it, but can I redo it basically the functional issue." The mechanism for applying an accepted fix is automated: "the agent behind the scene will take the user comment and actually automatically do it." He summarized the state of the infrastructure with a simple declarative: "we have this infrastructure we have this UI everything is there already."

The implications of this disclosure are substantial. Cisco is not waiting on BayOne to build a review user interface. Cisco is not waiting on BayOne to build the agent orchestration layer that accepts or rejects comments. Cisco is not waiting on BayOne to build the infrastructure that applies an accepted fix back to the GitHub pull request. All of those components already exist in some form, being maintained by Justin's team and a broader group of engineers on Cisco's side.

## The Parallel Execution Model

Justin also clarified, in response to a timing question from Srinivas about when code review engages relative to the build, that the two processes run concurrently rather than sequentially. His explanation: "basically we create a workspace we in parallel we start the code review and the build starts because we do a separate read-only mount for the code review." The key engineering detail is the read-only mount, which allows the code review workflow to operate on a snapshot of the workspace without interfering with the active build compilation happening in the same workspace area.

Colin's follow-up observation captured the consequence neatly: "so then technically we are our CI agent is anyway helping the engineer fix the issue." The CI pipeline, in Justin's current implementation, is already an agentic helper for the engineer. It is not a passive report generator. It is an interactive collaborator that the engineer can guide through accept, reject, and redo commands on the functional issues it raises.

This detail is important to BayOne because it establishes that the delivery model of the overall system has already been chosen by Cisco. The model is concurrent, read-only-mount, agent-in-the-background, user-interactive. BayOne's contribution must fit into that established delivery model rather than propose a different one.

## Srinivas's Directive: Build the MCP Endpoint, Not the Agent

The pivotal redirect came immediately after Justin described what his team had built. Srinivas turned to the BayOne team and issued a directive that cleanly separated what Cisco owns from what BayOne should build. His exact framing: "what I want you guys to do is you we can if you can build the log failure build failure as an MCP endpoint we can take the same agent and hit the build mcp, build server mcp and say where is the issue for the specific PR, right?"

He elaborated on why this scope division made sense. The functional-fix agent that Justin's team had built could be reused, unchanged, for build failures, provided BayOne exposed the build analysis as an MCP endpoint. "And then we can use the same agent to suggest the fix even for the build failures, not just the functional issues. Because if functional issues is the critical thing that's happening, right? If I can do the functional issue fix directly, we should be able to do the build issue as well, right? But the only thing what we are not building the knowledge is we are not looking from the from the build lens point of view, right, the PR."

In other words, Cisco's existing agent infrastructure has functional-issue context, but it does not yet have build-failure context. The content gap is the MCP endpoint that BayOne would build. The agent itself does not need to change. The user interface does not need to change. What needs to be added is a new MCP endpoint that returns build-failure analysis in a form the existing agent can consume.

Srinivas summarized the user experience outcome this integration would produce: "from the user point of view you have a single dashboard, single feedback mechanism, single way of interacting for his PR which says that oh, I have functional issue This is all fix it. I have a build issue. I have this all fix it." The user cannot tell which MCP endpoint the agent consulted. The agent routes between functional and build issues transparently.

## The "Do Not Think in Terms of Agent" Coaching

After issuing the directive, Srinivas went further and coached the BayOne team on how to approach the analysis work itself. This was a deliberate reorientation of the team's mental model, and it deserves close attention because it changes the shape of the engineering problem BayOne is solving.

His words: "when you guys do the analysis, don't think in terms of agent. Think of from an endpoint point of view. Like, what is the endpoint, what that API should look like. Then, we'll bring you guys on board, and you can do the integration." The sequencing he proposed is clear: design the endpoint contract first, let Cisco's team integrate the endpoint into the agent infrastructure later, and do not let the BayOne design be contaminated by assumptions about how the agent will behave.

Srinivas then broadened the coaching to explain why the agent itself was not the interesting part of the problem: "I'm not worried about the agent because agent can be codec, co-pilot, cursor. There are so many 10 other things that we are planning to support. don't worry about that piece just let's look at the context engineering and how do we expose this as an end point." The agent is commodity. Codex, Copilot, Cursor, and potentially many other agents are all candidates. What is not commodity, and what Cisco needs BayOne to produce, is the context engineering that turns a build log into structured, actionable information the agent can reason about.

Srinivas framed this redefinition of the work explicitly: "agent is just a prompt and a actual context right? So please adjust it in the menu I mean I'll be there too but when we work we need to think in terms of context engineering right and that context engineering can be opened as an endpoint or one or two endpoints depending on what problems that we are trying to solve and then just give to the agent that is there." The engineering principle embedded in this framing is that the hard part of agentic systems is not the agent. The hard part is the context assembly, the narrowing of the search space, the categorization of what the failure is and why it happened. Once that context exists and is exposed cleanly, any agent can consume it.

## The Endpoint Design Target

Srinivas then described what the BayOne-built endpoint should actually return. The functional requirements he articulated are concrete and specific. Given a build failure, the endpoint should analyze it and output a statement about cause. In his words: "we should look at, you have the build failure, you do the analysis, and you say that, okay, this failure caused because of this reason, right?"

The endpoint should support multiple failures per build, since a single build can fail in more than one place. "And there may be more than one failure, that's fine, but at least if you can categorize that and expose it as an endpoint." Categorization is the minimum bar. Not just raw failure data, but classified and labeled failures that an agent can reason over.

The consumption pattern is agent-initiated pull: "Then the agent that is running here will pick up that NCP and say oh, this is an issue Let me suggest a fix." The agent does not wait for a push notification. When it needs build context for a pull request, it hits the MCP endpoint. (Note: Srinivas said "NCP" in the transcript, which is almost certainly a dictation artifact for MCP, Model Context Protocol. Elsewhere in the same exchange he says "MCP" clearly.)

## Justin's Timing Commitment: Three to Four Weeks

A critical scheduling detail emerged when Colin asked who was working on the functional fix infrastructure. Justin's answer provided both team scale and a timeline: "There's a big team actually, there's a huge team working behind the scene and yeah on the CI pipeline like ID code review you know we are making it mandatory like a CI we have a huge pipeline a lot of folks are working behind the scene so mostly another three four weeks It will be ready. But by that time, if you guys do the context engineering, you can just put it there."

The three-to-four-week window matters for planning. It means that BayOne's work can proceed in parallel with Cisco's internal work on the agent side, and that the integration moment is expected to happen at the end of that window. If BayOne delivers the MCP endpoint on that same timeline, the two pieces come together naturally. If BayOne takes longer, the Cisco-side agent goes to production without a build failure integration initially, and BayOne plugs in afterward. Either way, the timeline is a tractable few weeks, not a multi-quarter effort.

## Execution Runtime on the Build Host

Colin asked a clarifying question about where the agent actually runs: "so this agent should run on the build host?" Justin confirmed: "Yeah, it will be running on the build host."

The architectural implication is that the agent lives inside Cisco infrastructure, on machines that have direct access to the build workspace, the build logs, and the GitHub enterprise environment. BayOne's MCP endpoint needs to be reachable from the build host, which likely means it needs to run inside the Cisco environment as well, or it needs to be exposed through whatever network ingress Cisco makes available for its internal services. The MCP endpoint does not need to run on the build host itself, but it does need to be callable from there.

This also clarifies a deployment question. The BayOne-built service is not a SaaS product reached over the public internet. It is an internal Cisco service, subject to Cisco's network policies, its authentication controls, and its operational practices.

## GitHub Enterprise Versus Cloud Constraint

Colin asked whether Cisco might simply use GitHub's built-in agent features, citing Codex integration that exists out of the box in GitHub Cloud. Srinivas's response closed that door firmly: "Guys, we use the enterprise version of the Git. This is not the cloud version. We need to build all the pipeline searching houses."

He reinforced the constraint when Colin pushed back on whether the enterprise version supported those features: "Enterprise does not have that support only. You have open, you have a cloud-based or whatever the Microsoft support, they have that thing. Enterprise does not have that support. They are tied guardrails on the enterprise version, on-prem version."

The practical consequence is that cloud-hosted GitHub agent features are not available. BayOne cannot point at a GitHub Cloud feature and say "use this." Everything logical, everything that needs to reason about the pull request, must be built inside the enterprise perimeter. This constraint is a first-order driver of the overall architecture, because it is why the MCP endpoint model exists in the first place. If Cisco could use cloud Codex integration, it would not need a custom MCP-based agent pipeline at all. Because it cannot, the entire integration surface must be constructed inside Cisco's on-premises environment.

## The Reframe: Who Builds What

Pulling the directives together produces a clear scope division that reshapes the engagement boundary.

Cisco, specifically Justin Joseph's team along with the broader group he described as a "huge team working behind the scene," is building the functional-fix agent infrastructure. They are building the review user interface that the engineer interacts with to accept, reject, or redo suggestions. They are building the build host integration, the workspace creation logic, and the read-only mount plumbing that lets code review run concurrently with the build. They are building the plumbing that patches accepted changes back into the GitHub pull request. They own the agent, whatever agent that ends up being. Srinivas explicitly listed Codex, Copilot, and Cursor as candidate agents, and he indicated that many others might be supported over time.

BayOne is building the build-failure analysis MCP endpoint. This includes the categorization logic that identifies what kind of failure each error represents. It includes the context engineering that assembles the relevant code fragments, commit history, and dependency information into a form the agent can reason about. It includes the knowledge graph integration described in the companion knowledge graph decomposition, since the knowledge graph is the substrate that makes the MCP endpoint's output useful rather than just raw log data.

The agent itself is not owned by BayOne. Srinivas was explicit on this point. The agent is commodity and interchangeable.

The integration point between the two scopes is the MCP endpoint. Cisco's agent pulls from it. BayOne serves it. Over the wire, the contract is MCP.

This is, structurally, a classic microservice integration pattern. BayOne provides a service with a well-defined contract. Cisco consumes the service through an already-built orchestration layer. The two sides are coupled through the contract, not through shared implementation details.

## Srinivas's Infrastructure Sequencing Comment

Before Srinivas closed the scope discussion, he offered a sentence that underscored how much Cisco-internal investment already exists in this space: "There is a big team actually, there is a huge team working behind the scene and yeah on the CI pipeline like ID code review you know we are making it mandatory like a CI we have a huge pipeline a lot of folks are working behind the scene."

Two things follow from this comment. First, BayOne is not the only contributor on this pipeline. There are many internal Cisco engineers building adjacent and overlapping capabilities, and BayOne's deliverable must fit into their work without disrupting it. Second, the code review mandate is a business driver, not a research experiment. Cisco is making agent-assisted code review mandatory as part of its CI pipeline. The investment is large enough, and the policy commitment is serious enough, that integration discipline matters. A BayOne MCP endpoint that does not integrate cleanly, or that assumes a different agent behavior than what Cisco's internal team is actually building, will be a problem.

## Implications for the Engagement's Deliverable Framing

The April 17 meeting changes the shape of what BayOne delivers. Before this meeting, a reasonable reading of the engagement was that BayOne would build a triage system that included its own agent behavior and its own user interface for developers to consume the triage output. The Set 05 prep materials had begun to surface the scope overlap concern with Rui's team and the Nexus T repository, and Set 07 through Set 09 had been working through a decoupled service layer pattern that tried to separate BayOne's contribution from Cisco's existing infrastructure. Set 10 and Set 11 had established that Justin Joseph had working infrastructure that BayOne would need to integrate with.

This meeting completes that scope narrowing. After this meeting, BayOne's deliverable is most accurately described as an MCP endpoint that plugs into Cisco's existing agent infrastructure, with context engineering as the core engineering problem. BayOne is not building a triage user interface. BayOne is not building a custom agent. BayOne is not building a WebEx bot as part of this specific workstream, though there is a separate WebEx bot conversation running elsewhere in the engagement.

The deliverable contract becomes more specific as a result. BayOne needs to produce an MCP endpoint specification that defines, at minimum, the input (some reference to a specific pull request and build, though the exact identifier format is [unclear in transcript]), the output schema (a list of categorized failures, each with a cause statement and presumably supporting evidence), and the behavior under multiple-failure conditions. The quality of the endpoint is measured by the quality of the context it returns, not by the sophistication of any agent behavior.

Context engineering, in this framing, is the central engineering discipline of the engagement. What information does the endpoint include? How is it narrowed? How is it ranked? How is it structured so that an agent consuming it can reliably propose fixes? These are the questions that matter, and they are the questions Srinivas was pointing at when he said "agent is just a prompt and a actual context."

## Connection to the Knowledge Graph Redirect

The MCP endpoint directive from April 17 is complementary to the knowledge graph directive that Srinivas issued later in the same meeting and that is captured in a separate decomposition. The two directives must be read together.

The knowledge graph is the foundational context that makes the MCP endpoint useful. Without a knowledge graph of the build structure, the MCP endpoint cannot localize a failure to a subgraph. It would be reduced to returning raw log chunks with generic summaries, which is exactly the kind of junk output Srinivas warned the team against when he said "without a knowledge graph you go to AI you get junk and this project will be another year project."

With a knowledge graph in place, the MCP endpoint can return something genuinely useful. Given a build failure, it can identify the affected node in the build tree, walk the upstream and downstream dependencies to determine blast radius, correlate the failure against the commit chain on that node to identify the likely causal commit, and return a structured response that says, in effect: "this failure was caused in this subtree by this change, here is the narrowed log extract, and here is the relevant code context." That output is then what the Cisco agent consumes and uses to propose a fix.

In the absence of either piece, the system falls apart. Without the knowledge graph, the endpoint returns shallow content. Without the MCP endpoint, the knowledge graph has no consumer in the pull request review flow. Both pieces are needed, and together they define the totality of what BayOne is building on this workstream.

## Summary

The April 17 exchange with Justin and Srinivas produced three durable outcomes for the engagement. First, the existence of Justin's functional-fix agent infrastructure is now confirmed and documented, including the read-only mount concurrent execution model, the accept-reject-redo user interface, and the three-to-four-week production timeline. Second, Srinivas's directive reshaped BayOne's scope from "build a triage system" to "build an MCP endpoint that plugs into the existing agent infrastructure," with context engineering as the central engineering discipline and the agent itself explicitly declared to be commodity. Third, the GitHub enterprise constraint fixes the architecture to on-premises integration, ruling out the cloud-hosted agent features that would otherwise simplify the problem.

The next steps for BayOne are to design the MCP endpoint contract explicitly (input schema, output schema, failure categorization taxonomy), to align on the knowledge graph foundation that feeds it, and to deliver the first version of the endpoint in time to be available when Justin's agent infrastructure reaches production in the three-to-four-week window Justin described.
