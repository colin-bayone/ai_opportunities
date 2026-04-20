# 02 - Meeting: Technical Approach and Tooling Alignment

**Source:** /sephora/qa_qe_playwright/source/vaibhav_colin_sync_4-9-2026.txt
**Source Date:** 2026-04-09 (Follow-up sync, project scoping conversation)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on technical approach and tooling alignment

---

## BayOne Internal QA/QE Practice as Social Proof

Colin used BayOne's own internal QA/QE practice as the primary technical credibility anchor. He introduced it with: "What we do internally even might be of some interest. I stand by what I said earlier. We kind of practice like we play. So even internally for our own QA QE, we have Playwright agents that go off" [00:05:19]. This framing was deliberate: rather than presenting an abstract capability deck, Colin showed that BayOne uses the same tooling for its own work, positioning the recommendation as battle-tested rather than theoretical.

### Core Stack: LangGraph + Custom Agents + Custom Tools

Colin stated the internal system is "all LangGraph based, so LangGraph plus custom agents with custom tools, usually MCP server in there as well" [00:05:21]. Key elements of this description:

- **LangGraph** is the orchestration layer. This is the framework that manages agent workflows, state transitions, and the flow between different agent steps.
- **Custom agents** -- not off-the-shelf agents. BayOne builds purpose-specific agents rather than relying on generic agent frameworks.
- **Custom tools** -- the agents are equipped with tools that BayOne has built or configured for specific tasks.
- **MCP server integration** -- Colin mentioned MCP servers as a standard component of the stack. He later elaborated that the MCP connects to external tools: "In the MCP I was talking about earlier, that connects to Figma. There's one for Canva. There's a couple of other tools that we can use too. Even for WordPress, we have one, which is pretty nice" [00:10:45]. This establishes that the MCP layer is the integration bridge between agents and external platforms.

### Playwright as Primary Automation Agent

Colin identified Playwright specifically as "the primary automation agent" [00:05:21]. This is the tool that actually drives browser interactions -- clicking, navigating, capturing screenshots, interacting with web elements. It sits underneath the LangGraph orchestration as the execution layer for browser-based testing.

### Desktop and Mobile Coverage

Colin confirmed the system "works for both desktop and mobile view, so that's no issue for the client that it's serving" [00:05:21]. This was stated matter-of-factly, not as a special capability, suggesting that the Playwright + LangGraph architecture handles viewport switching as a baseline feature.

### Visual Testing and UIUX Support via MCP

Colin specified that the MCP integration "helps with the visual testing for UIUX as well as user workflow, usability of product as well" [00:05:21]. This ties the MCP server specifically to the visual QA use case that Vaibhav described as the primary gap. The MCP is not just for content generation -- it is directly relevant to the visual testing pipeline.

## Agent Flow Architecture

Colin described two distinct agent flow patterns, establishing that the system supports both unstructured and structured testing approaches.

### Flow 1: Exploratory Flow

Colin described this as: "One flow could be an exploratory flow. Pretend you're a brand new user. Go to this application, click around, see what you can find. Note down any bugs. A typical QA task that is very time-consuming per person" [00:05:21]. Key characteristics:

- The agent impersonates a naive end user.
- The agent navigates without a predefined script.
- The agent identifies and records anomalies autonomously.
- This maps directly to one of Vaibhav's stated needs: "just exploratory testing" [00:02:47] and "run them loose in a production environment and try to isolate any anomalies on the site" [00:03:04].

### Flow 2: Structured Playbooks

Colin described the second flow as: "We can go and build those kind of playbooks so that they are repeatable, reusable, deterministic, but they can still be agentic from the first part" [00:05:21]. Key characteristics:

- Playbooks are predefined, scripted flows.
- They are repeatable and reusable across test cycles.
- They are deterministic in their execution path.
- They retain agentic behavior -- the agent can still make judgment calls within the structured flow, rather than being purely scripted automation.
- The phrase "from the first part" connects this back to the exploratory flow, suggesting that exploratory runs can be codified into playbooks once a useful testing pattern is discovered.

### Extensibility Beyond Visual QA

Colin explicitly stated the same strategy "even works for things like unit testing or the back end testing or integration testing that we have. So it's just a matter of getting the agents, getting the tools" [00:05:21]. This positions the architecture as a general-purpose agent framework, not limited to visual/browser testing. The modular design means the same orchestration layer can drive different types of testing by swapping tools.

## Traceability and Logging

Colin emphasized traceability as a core design requirement, drawing a parallel to what he expects from human QA engineers: "When those happen, we get what I always want from my human QA team, which is to say log exactly what you're doing all the time. Give me an exact record of every single thing that you're testing, the current state. Even look at the GitHub SHA tag, so that I can know what the state and the version was of that code base that you're testing on, so that I can have some good traceability in the future" [00:05:21].

Specific traceability artifacts mentioned:
- **Complete action logs** -- every action the agent takes is logged.
- **State capture** -- the current state of the application at each step.
- **GitHub SHA tags** -- version tracking tied to the specific code commit being tested. This enables correlation between test results and code versions.
- **Screenshots** -- Colin later mentioned "screenshots, QA artifacts" [00:07:44] as outputs of the process.
- **Progression tracking** -- Colin referenced "some sense of progression of this 'cause this can be, it can have a feedback loop" [00:07:44].

This traceability design directly addresses audit trail requirements that enterprise QA teams typically need.

## Review Agent Layer

Colin described a filtering layer between agent output and human review: "I always say if AI is giving me something, I want to do as little work as possible. Smart but lazy. So I want to have this only shown back to me after the agents are done, if and only if it looks good. So there's still even a review agent that has to pass it first to make sure it's worth the human being's time to review" [00:07:44].

This establishes a multi-layer architecture:
1. **Execution agents** -- run the tests, capture artifacts, log everything.
2. **Review agent** -- evaluates the output of execution agents before any human sees it.
3. **Human review** -- only triggered when the review agent determines the results warrant human attention.

The philosophy Colin articulated -- "smart but lazy" -- is a design principle, not a throwaway comment. It means the system is built to minimize human effort per review cycle, which directly affects the ROI calculation for the tool.

## Guardrails Approach

Colin described the guardrail strategy in terms of tool access control and destructive action prevention: "Guardrails for us are kind of in that sense of making sure that only the needed tools have some access. And that even within that access, we are restricting it down to what we consider as non-destructive actions unless it is specifically within a sandbox environment. And if it is in the sandbox, we can work with that too and we can turn on the destructive mode where AIs love to do all the things we read about on Twitter" [00:05:21].

Decomposition of the guardrail model:
- **Tool-level access control** -- agents only have access to the tools they need for their specific task. No universal access.
- **Non-destructive by default** -- outside of sandbox environments, agents are restricted to read-only or observation-only actions. They cannot modify data, submit forms, or alter state.
- **Sandbox escalation** -- in sandbox environments, destructive actions can be enabled. This is a deliberate opt-in, not a default.
- **Environment-aware behavior** -- the agent adapts its permissions based on which environment it is operating in (production vs. nonprod vs. sandbox).

This is directly relevant to Vaibhav's stated use case of testing in both nonprod preview environments (where AB testing occurs) and production environments. The guardrail model addresses the risk of agents interfering with live production state.

## Recommended Stack: Playwright, LangGraph, Azure AI Foundry

Colin made his stack recommendation explicit: "If I had anything right now today, if I said Playwright, LangGraph, and probably model hosting on Azure AI Foundry, it's typically what we do" [00:18:55].

**Vaibhav's response was immediate and unqualified: "Yes, all three. I'll give thumbs up to" [00:19:04].** Deepika's response was "Mhm" [00:19:11] and "Yep" [00:19:11], indicating agreement.

This is a significant alignment moment. All three core technologies were accepted without pushback, negotiation, or questions. There is no tooling gap to bridge in the proposal.

### "Boring is Good" Philosophy

Colin framed his approach as deliberately conservative: "I'm not someone to come in and bring in a very strange external platform, even though it has all this promises to it. I'm a boring engineer. Boring is good. Boring is reliable" [00:18:45]. This is a positioning statement with two functions:

1. **Technical credibility** -- it signals that Colin will not over-engineer or introduce unnecessary complexity.
2. **Risk mitigation** -- it addresses Vaibhav's stated concern about "not expanding into too many tech that we need to then kind of manage" [00:17:40].

### Fallback Strategy: Build or Microsoft

Colin described the strategy for when something is needed beyond the core three: "If we do, we build it or if we don't, we find something on Microsoft. That way someone in IT can help to administrate things, which is great. So there's good business continuity as well" [00:19:11].

This establishes three principles:
1. **Core stack first** -- Playwright, LangGraph, Azure AI Foundry handle the bulk of the work.
2. **Custom build second** -- if something is not covered, BayOne builds it rather than introducing another vendor.
3. **Microsoft ecosystem third** -- if a pre-built solution is needed, it comes from the Microsoft ecosystem, ensuring IT administrability and business continuity.

The business continuity argument is notable. It means Sephora's IT team can manage infrastructure through familiar Microsoft tooling rather than needing specialized knowledge of niche platforms.

## Sephora's Existing Tooling Context

### BrowserStack Enterprise License

Vaibhav disclosed: "We are hoping to get BrowserStack enterprise license so that would give us the ability to run them across these combinations [of devices and browsers]. So that would be something that'll be hopefully very soon available to us" [00:11:01].

Key details:
- The license is not yet in place -- "hoping to get" and "hopefully very soon."
- It is intended to provide cross-device and cross-browser testing capability.
- The BayOne solution should be designed to integrate with BrowserStack once available, but cannot depend on it being present from day one.

### In-House Open WebUI Equivalent Portal

Vaibhav mentioned: "We are building an in-house Open WebUI equivalent portal" [00:18:19]. He then connected this to the portability discussion: "Once we have the boilerplate solution in place, it won't be too difficult to port it over to what we have" [00:18:19].

This means:
- Sephora is building their own AI portal, modeled on Open WebUI.
- The expectation is that the BayOne-built solution will eventually be integrated into or ported to this portal.
- The solution should be architecturally portable -- modular enough that the core logic can move into Sephora's own hosting and UI layer.

### Tool Proliferation Concern

Vaibhav stated: "From tools and technology perspective, we are fairly flexible, but we are also cautious about not expanding into too many tech that we need to then kind of manage" [00:17:40]. This is a governance constraint, not a technical one. Sephora does not want to accumulate tools that create maintenance burden. The proposal must show that the stack is minimal and integrates with what Sephora already has.

## Unified Backend Approach

Colin proposed: "One kind of unified backend approach to all four cases. It'll eliminate a lot of the work. You'll have reusable modular components even beyond those four areas. If you want to do something even beyond that in the future, you'll have something extensible for yourself" [00:10:28].

He reinforced this with a concrete example: "The same tool we built internally for our QE team is the same one our marketing team uses for new content generation" [00:10:45]. This demonstrates that a single backend can serve fundamentally different use cases (testing vs. content creation) without being rebuilt.

Vaibhav agreed with this approach. His statement about 80% commonality -- "irrespective of what tech Colin suggests in this proposal, I'm very sure there will be like he said 80% common commonality and whatever is not, I think it shouldn't be too much of an effort to move it to something else that we currently use" [00:17:40] -- indicates he already sees the four consumer groups as variants of the same core platform, not four separate tools.

## Cross-Team Reuse: QE and Marketing Sharing the Same Tool

Colin's disclosure that BayOne's QE tool and marketing tool are the same system is a significant data point. He specified the MCP integrations that make this possible: Figma, Canva, WordPress [00:10:45]. This means:

- The same LangGraph orchestration layer drives both testing workflows and content generation workflows.
- The MCP server is the abstraction layer that makes this possible -- different MCP connectors enable different capabilities without changing the core agent architecture.
- For Sephora, this implies their fourth consumer group (Producers / Digital Content team) can be served by the same backend as the QE consumer groups, with different MCP configurations rather than a separate tool.

## Open Questions and Unresolved Points

1. **BrowserStack integration timeline:** Vaibhav said "hoping" and "hopefully very soon" but gave no firm date. The proposal needs to handle the scenario where BrowserStack is not available at project start.

2. **In-house portal architecture:** No details were shared about what Sephora's Open WebUI equivalent is built on, what its API surface looks like, or what integration pattern it supports. This will matter when designing for portability.

3. **Deepika's technical evaluation criteria:** Vaibhav warned that Deepika "scrutinizes everything with very heavy lens" [00:15:05], but no specific technical requirements or evaluation criteria were shared by Deepika herself. Her questions and standards will emerge in the requirements deep dive.

4. **Existing AI solutions in Deepika's COE:** Vaibhav mentioned Deepika's team has "already been working on this for the last couple of years" and has been "very successful in creating multiple agentic solutions across the board in QE lifecycle" [00:04:13]. No details were shared about what these existing solutions are, what they are built on, or how the new visual QA tool would coexist with them. This is a critical integration question for the proposal.

5. **Model selection within Azure AI Foundry:** Colin recommended Azure AI Foundry as the model hosting layer but did not specify which models would be used (GPT-4o, GPT-4V for visual analysis, etc.). This will need to be addressed in the technical proposal.

6. **Nonprod preview environment access:** Vaibhav mentioned that "most of the AB testing is conducted" in nonprod preview [00:03:04]. No details were shared about how agents would access this environment, what authentication is required, or what restrictions exist on automated access.

7. **Pixel-level differential thresholds:** Vaibhav mentioned that the UIUX team should be able to "define some pixel level differential thresholds or certain baseline components or even some sort of an approval routing" [00:08:33]. No specific threshold values or baseline component definitions were discussed. This feature is noted as a requirement but is entirely unspecified.

---

*This is a blockchain-style document. It will not be edited after creation.*
