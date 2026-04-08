# 04 - Meeting: Detailed Agent Architecture Walkthrough

**Source:** /sephora/edw_modernization/source/meeting4-technical-deep-dive_formatted.txt
**Source Date:** 2026-03 (Technical Deep Dive)
**Document Set:** 04 (Technical Deep Dive)
**Pass:** Focused deep dive on Colin's agent architecture presentation

---

## 1. Session Context and Framing

This meeting was intended as a technical deep dive to gather requirements for a demo, not the demo itself. There was a disconnect at the start: the Sephora team (Andrew, Grishi/Andrew, Meher, Sergey) expected a demo, while Colin and the BayOne team (Neha, Gaurishi) expected a requirements-gathering session to inform the demo. After Neha clarified (lines 113-116) and Andrew reframed (lines 119-128), the session pivoted into Colin presenting the agent architecture methodology at a detailed technical level, followed by the Sephora architects asking questions and providing the technical constraints for the environment.

Andrew set the expectation clearly at line 120: "Whether you guys can or whether it's even possible to create all those different smaller agents and have a kind of an orchestrator agent to orchestrate all the smaller agents to do all the specific tasks throughout this modernization journey."

---

## 2. MCP Server Research: Cognos and DataStage Connectivity

Before presenting the architecture, Colin shared homework completed since the previous meeting on the feasibility of programmatic integration with Sephora's legacy tools.

### 2a. Cognos SDK Availability

**Key statement (lines 145-152):** "On Cognos and on DataStage both, very good news for you — beautiful, perfect, all-inclusive APIs or SDKs for both of them. These are old enough that they weren't APIs yet. They were just pure SDKs. They're available in both Java and .NET. That goes all the way back to even the earliest versions of Cognos. So as long as you're using a version that's after 2003, we're in good shape."

Findings:
- Complete SDKs exist for both IBM Cognos and IBM DataStage
- Available in Java and .NET
- Coverage extends back to post-2003 versions, meaning any Sephora version is covered
- Colin characterized access as unrestricted: "There's basically complete access to everything within Cognos with no restrictions that I could find" (line 160)
- This includes RBAC configurations, which matters for migration parity

### 2b. What an MCP Server for Cognos Does

**Key statement (lines 153-158):** "The way that we do this, we build what's called an MCP server. These don't typically already exist. So these are things that we build from scratch as part of what we do. This is not uncommon for us at all. We have to do this very often when it comes to legacy platforms, and essentially gives us a way to interact with that SDK programmatically with agents."

Colin described the MCP server as:
1. A custom-built component (not off-the-shelf) created for each legacy tool
2. A wrapper that defines available actions, controls, constraints, and parameters the agent can use to interact with the tool
3. The mechanism that transforms a legacy SDK into something an agent can use: "That basically gives you a mini-agent with the capability to take some action into Cognos" (line 158)

### 2c. Two Purposes for the Cognos MCP Server

Colin identified two specific use cases at lines 165-170:

1. **Report mapping without manual data entry** — Programmatic extraction of data sets, calculations, and other report components, eliminating the need to manually feed this information to the system. "Any of the data sets that are part of that report, any of the data, any of the other calculations or otherwise that might be a part of that report, rather than trying to access it through a human or even for the sake of verification, we can pull it out programmatically" (lines 166-167).

2. **Parity verification** — Deeper exploration of report nuances beyond what screenshots or human notes can capture. "If there's some nuance to it, we're able to more deeply explore that, rather than something that might just be a screenshot or some human notes that we're given" (line 169).

### 2d. MCP as the Universal Connector Pattern

Colin generalized MCP's role at lines 242-246: "Agents plus MCP is the way to go here, for sure. MCP is essentially a connector to all these tools. To prevent that human step from needing to... you'll always find a very good indication that you need MCP in the mix is if you find a human being copying and pasting or taking screenshots of something and passing it out to a language model."

**The diagnostic rule for when MCP is needed:** Any time a human is copy-pasting or screenshotting to feed information to an AI, that is an integration gap that should be filled by an MCP server.

Colin confirmed MCP would be used for Databricks, SQL Server, and Cognos (lines 378-379).

---

## 3. The Three-Phase Mapping Methodology

This is the core technical architecture Colin presented for how the mapping between SQL Server (EDW) and Databricks would actually work. Colin introduced it by first explaining why a naive approach fails.

### 3a. Why Pure AI Mapping Fails

**Key statement (lines 295-299):** "What can happen if you have a language model dynamically look up, like let's say we talked to Claude and we say, go find me this table in Databricks that is equivalent to this table. That can work once. But if you try it over and over and over again, especially if things don't have clear naming conventions, or there might be some versioning, or there might be just some nuance to it, what you'll find is that it doesn't work reliably every time."

Colin was explicit that this lesson came from direct experience: "This is something we've definitely found through much pain in the past. It sounds like AI can do everything, this one not so much" (lines 298-299).

The failure mode: unreliable results at scale, particularly when naming conventions are inconsistent, versioning exists, or there are nuances in the data structures.

### 3b. Phase 1: Structural Discovery (No AI)

**Key statement (lines 300-308):** "What we do first is the structural discovery. This happens on both sides of the house, both in Databricks as well as in SQL. And this is actually no AI involved whatsoever. This is just essentially a recursive crawler script that goes out and can map the actual tables, databases, columns, relationships, data types that are on the tables that you have on-prem as well as in Databricks."

Technical specifics:
- **No AI involved** — purely deterministic
- **Recursive crawler** that maps both source (SQL Server) and target (Databricks) environments
- **Captures:** tables, databases, columns, relationships, data types
- **Runs on both sides** of the migration simultaneously
- **Purpose:** Enables a deterministic existence check before any AI processing begins

**Key benefit (lines 303-308):** "It saves us a lot of effort to do this later on because if a table doesn't exist in Databricks, I don't need to go try to find it. I can say deterministically, no, it doesn't exist before I ever get AI involved."

Colin described the failure mode this prevents as the "telephone game" (line 307) — an agent searching for a non-existent table, failing, and then fabricating an answer instead of cleanly exiting. With the structural discovery in place, the agent knows immediately that the table does not exist and can either flag it to a human or hand off to a migration agent to create it in Databricks (lines 308-310).

### 3c. Phase 2: Rule-Based Mapping (No AI)

**Key statement (lines 312-320):** "Phase two is the actual rule-based map. Again, no AI here. This is just making sure that there's matching. And it doesn't have to be a one-to-one map, because that still doesn't necessarily mean that the data is the same."

Technical specifics:
- **No AI involved** — pattern matching and rule-based logic only
- **Purpose:** Capture mappings that can be confirmed with 100% accuracy through deterministic rules
- **Handles:** Similarly named items, custom-named report items, items that may share names but come from different data sources
- **Captures both confirmed matches and confirmed non-matches:** "When we capture the things that we're wrong about, we capture the things that we're right about. That all kind of becomes the context as these agents go forward" (lines 319-320)

The critical nuance Colin flagged: even name matches do not guarantee data equivalence. "It happens very often in business intelligence reports, for sure, where there's a lot of similarly named things, or maybe custom named things within a report. But they might be a different data source altogether" (lines 316-317).

Both confirmed matches and confirmed mismatches are captured and fed forward as context for the AI phase.

### 3d. Phase 3: AI Semantic Mapping

**Key statement (lines 321-324):** "Phase three is where the AI system mapping comes into place. So we're looking at the column names, making sure that there's compatibility between the data types. This is essentially the pre-work that's needed before we do that shift over to Databricks from SQL Server."

Technical specifics:
- **AI is involved** — this is where language models enter the process
- **Checks:** Column name compatibility, data type compatibility
- **Purpose:** Fill in the gaps remaining after Phases 1 and 2
- **Input:** The confirmed matches, confirmed non-matches, and structural maps from the first two phases
- **Output:** The remaining mappings needed for migration

The key design principle: AI only handles the ambiguous cases after deterministic methods have handled everything they can. The first two phases reduce the problem space so that AI is applied only where it is actually needed.

---

## 4. Confidence via Human Reinforcement Learning

Colin dedicated significant time to explaining why AI-reported confidence is unreliable and how the system builds real confidence through human reinforcement.

### 4a. Why Language Model Confidence Is Meaningless

**Key statement (lines 328-333):** "How do you know that confidence is high? What does that really mean? That's where AI, I think especially with language models, suffers quite a bit because it can say I'm 100% confident in something. A lot of the times we call that a hallucination. I disagree with that determination because it's usually that either we haven't given enough context or the ground truth is wrong. But confidence is one where it can't be coming from a language model. A language model doesn't even have a concept of confidence."

Colin made two distinct claims:
1. A language model cannot meaningfully report its own confidence level
2. What people label "hallucinations" are more accurately attributed to insufficient context or incorrect ground truth — but regardless of the cause, self-reported confidence from a model is unreliable

### 4b. How Real Confidence Is Built

**Key statement (lines 335-347):** "Whenever a human goes and reinforces a decision made by AI, that is confidence. So if you say yes, you are correct or no, you are wrong, that is what determines confidence. And even when it's wrong, now it knows what's wrong about it, so confidence still increases."

The mechanism:
1. The AI makes a mapping decision
2. A human reviews and says "yes, correct" or "no, wrong — and here's why"
3. Both positive and negative feedback increase system confidence because both expand the known-correct context
4. This feedback is stored and referenced in future decisions

### 4c. The Threshold Model: Graduated Autonomy

**Key statement (lines 339-347):** "It starts slow. It starts with a lot more human interaction to go and say, am I doing this right? Am I doing this right? But as soon as that gets OK'd a couple of times, confidence gets high enough that it goes and says, OK, if the situation is the same, if everything is the same here, should I do this myself?"

The autonomy progression:
- **Early stage:** High human interaction, frequent check-ins from the agent
- **Middle stage:** Confidence accumulates from repeated human confirmations
- **Mature stage:** The agent proceeds autonomously for situations it has seen confirmed before

**The five-times rule (lines 346-347):** "In simple terms, if I've said, yes, you can do this five times in a row, and time number six, you don't need to ask me to do it. You can just go and do it as long as you're tracking and keep remaining traceable with the actions taken."

Key constraints on autonomous action:
- The situation must match previously confirmed patterns ("if everything is the same here")
- All actions must remain traceable even when autonomous
- The threshold for moving from human-in-the-loop to autonomous is configurable per team preference (lines 344-345)

### 4d. Protection Against Unsupervised Drift

**Key statement (lines 348):** "So it's a good way to build some momentum with the agents while also making sure they don't go to work for 20 hours and then come back and it's complete junk that you can use."

The reinforcement model prevents the scenario where agents run for extended periods without check-ins and produce unusable output. The feedback loop ensures corrections happen incrementally rather than after a large batch of potentially wrong work.

---

## 5. The Knowledge Graph Component

### 5a. What the Knowledge Graph Does

**Key statement (lines 352-358):** "There is a Knowledge Graph component to this. And this is, I think, what makes the biggest difference compared to something like just using Claude natively. Because you're remembering the state of the system."

The Knowledge Graph serves as persistent memory for the entire agent system. Colin identified four specific functions:

1. **System state tracking:** "If a new table gets added into Databricks, now we're aware of that change occurring" (line 355)
2. **Opportunity detection:** "We can now say, look, now these other avenues for the reports are available to us" (lines 355-356)
3. **Error recovery:** "If there was some mistake made" (line 356) — the Knowledge Graph records the mistake so it is not repeated
4. **Infinity loop prevention:** "Or some rabbit hole that we went down and we went into this kind of infinity loop of agents talking to agents and never really reaching an answer. Knowledge Graph helps to keep everything grounded" (lines 356-357)

### 5b. Why It Matters for Long-Running Processes

**Key statement (lines 357-358):** "Especially when these things are more than just a one-shot, which certainly we are in the back of the boat over here. If it's more than just a one-shot attempt, Knowledge Graph is definitely needed to keep things aligned and on track."

Colin distinguished between one-shot AI tasks (where the Knowledge Graph is less critical) and multi-phase, long-running processes (where it is essential). The Sephora EDW migration is firmly in the latter category.

### 5c. What the Knowledge Graph Tracks

Based on Colin's description, the Knowledge Graph maintains:
- Current state of both Databricks and SQL Server/Cognos environments
- Which tables exist where (updated as the Databricks environment evolves)
- Which mappings have been confirmed or rejected by humans
- Paths that have been explored and their outcomes (preventing repeated failures)
- The current status across the full scope of migration work

---

## 6. How Agents Become Stateful: Blockchain-Style Context Management

### 6a. The Statefulness Mechanism

**Key statement (lines 252-262):** "Agents can be stateful as well. And what I mean by that is they can learn over time. And are they really learning? Learning, a lot of people think that means we're retraining models. We're certainly not doing that. It's that we're building up the business context that the agents are working within in a kind of a blockchain format."

Colin explicitly clarified:
- **"Learning" does not mean model retraining** — no fine-tuning or model modification is occurring
- **"Learning" means accumulating business context** that is passed to agents as they work
- The context is managed in a **blockchain-style format** — an append-only, immutable chain of decisions and outcomes

### 6b. The Behavioral Analogy

Colin compared it to "a perfectly behaved school kid — you tell them not to do something once, they know not to do that ever again. You tell them, hey, this was the right mapping and it's a reinforcement model to help with them" (lines 258-261).

The key characteristic: corrections and confirmations are permanent. Unlike a standard LLM conversation where context is lost between sessions, the blockchain-style context ensures that a correction given once persists across all future agent interactions.

### 6c. Why This Requires a Framework, Not Just Claude

**Key statement (lines 263-266):** "It's all through well-managed context, which is possible if you have a framework. It's not super possible to do that if it's just Claude. So even with Claude skills, Claude agents within Claude Code, it's still too big of a problem for Claude to do by itself. That's where frameworks come in and are a lot more powerful because they're still using Claude behind the scenes. It's just that they're doing it in a more orchestrated way with a lot more moving parts to keep things on track."

Colin drew a clear line between:
- **Claude natively** (including Claude skills and Claude agents within Claude Code) — insufficient for this problem due to context management limitations
- **Framework-based orchestration** — uses Claude as the underlying model but wraps it in persistent state management, routing, and coordination

This is the clearest articulation of why "just using Claude" is not the proposed approach: the problem requires persistent context across many agent interactions, which a framework provides but a standalone LLM session does not.

---

## 7. Guardrails

### 7a. Types of Guardrails

**Key statement (lines 359-366):** "There are always guardrails. These are the basic ones that we can have, but we can always add in more. It really depends upon what's the most important to you."

Colin identified two specific guardrail types:

1. **Static number checks (lines 362-363):** "Sometimes guardrails are actually just checking static numbers, almost like what a human would do to say that this work is actually done. How do I know that this conversion is actually a bit successful?" — Numeric validation that a transformation produced expected results, analogous to a human spot-checking output values.

2. **Convention following (line 364):** "Other things could just be, are we following conventions? Basic things with guardrails to make sure that we didn't randomly take a different approach." — Ensuring agents adhere to established patterns and do not deviate into novel approaches unprompted.

### 7b. Why Guardrails Are Critical for Autonomous Agents

**Key statement (lines 365-366):** "Guardrails are important here because since agents are working autonomously, you don't want them to just work and work and work completely in their own direction. So kind of this way of guidance is very important to these being successful."

The guardrails serve as drift prevention — without them, agents operating autonomously over extended periods can gradually deviate from the intended approach, compounding errors over time.

---

## 8. Failure Handling: Two Approaches

**Key statement (lines 367-377):** "If things fail, what happens? Well, it depends. Again, on whatever the appetite is."

Colin presented failure handling as a spectrum with two endpoints:

### 8a. Agent Self-Resolution

"On one hand, you can tell agents to go and resolve themselves. And that's something where you can have a decider agent in the loop to say, here's what you do when something goes bad" (lines 370-371).

This approach introduces a specialized **decider agent** whose role is specifically to handle failure cases and determine the correct recovery action.

### 8b. Human Escalation

"On the other hand, you could always have a human in the loop and continue to build that flywheel" (line 372).

Human escalation on failures feeds back into the reinforcement learning system, building the knowledge base for future failure handling.

### 8c. Factors That Determine the Right Approach

Colin identified two factors:
1. **Team appetite for involvement** (line 373)
2. **Report complexity and consistency** (lines 374-377): "If reports are all over the place and done completely differently, and there's a million of them with a million different formats — yes, it's going to need to be more human in the loop because there will be so many edge cases. But in other cases where it's more simple and you have 80% of reports follow the same conventions, which usually is true if they were developed by the same team, well then we can go and do this a lot quicker because there's less patterns for us to uncover along the way."

The practical implication: consistent report conventions (which are likely if the same team built them) dramatically reduce the need for human-in-the-loop failure handling.

---

## 9. Agent Playbooks: Two Creation Methods

Colin introduced the playbook concept in response to Sergey's question about how agents would know to generate YAML configuration files for the existing Databricks framework rather than writing new code.

### 9a. Method 1: Documented Playbook

**Key statement (lines 612-614):** "There is a concept, we call it as a playbook. So if there's like a well-defined task that humans already have known and documented, that is a good set of instructions for the agent. And this is kind of the iterative refinement that happens whenever we first create an agent to make sure it's actually doing what it's supposed to be doing, and it's robust enough that it can not just work once, but work broadly in that area."

A documented playbook is:
- An existing written process or procedure
- Translated directly into agent instructions
- Iteratively refined to ensure the agent performs correctly not just once but across the full range of cases it will encounter

### 9b. Method 2: Transcript-Based Playbook (Recorded Walkthrough)

**Key statement (lines 616-624):** "Another, even though it's going to sound a little bit silly, is actually very, very easy and kind of pain free for everyone. It's been very effective. All that we do is we get on a call, we hit the record button on the call to enable the transcript, and essentially someone walked through the exact process calling out those details. That's it. And then I have one of our team on just asking some questions along the way. It's usually something that's like 30 minutes to 45 minutes, depending on how complicated it is. At the end of that, that transcript itself becomes distilled as the first input to the agent."

The transcript-based approach:
- A subject matter expert performs the task live on a recorded call
- A BayOne team member asks clarifying questions during the walkthrough
- Duration: 30-45 minutes per process
- The call transcript is distilled into the initial agent instructions

Colin explained why this works better than written documentation in many cases (lines 622-623): "Usually I find that we're better as humans at showing what we're doing, rather than we are sitting down and writing it, because sometimes we miss out on details, or it's a little bit painful to do that."

### 9c. Playbooks as Repeatable Task Associations

**Key statement (lines 624-626):** "What happens at the outset is what we call the playbook, these repeatable, well-known, well-defined tasks. So if you do want to generate YAML files, any time that I give you this... if you want those things to be created every time, that's essentially us making an association between this set of actions corresponds to this kind of a request."

The playbook creates a binding between a type of request and a set of agent actions. For Sergey's specific scenario (generating YAML configuration files for the existing Databricks framework), the playbook would define: when someone requests a migration of a DataStage job, the agent generates the appropriate YAML configuration files rather than writing new Python or Scala code.

---

## 10. Agent Composition: Specialized Agents Combined with MCP and Orchestration

### 10a. Individual Agents Are Not Useful Alone

**Key statement (lines 267-272):** "For instance, something to extract report metadata or something to go and parse SQL and figure out what the equivalent would be in Databricks. And maybe this isn't even one agent, maybe it's two. Maybe there's one that's a Databricks agent, one that's SQL Server and one that takes both of their inputs and then figures out what the rehashing of the SQL might be in order to keep that report working."

Colin described a three-agent pattern for SQL conversion:
1. **Databricks agent** — knows the Databricks environment and structures
2. **SQL Server agent** — knows the source SQL Server environment
3. **Conversion agent** — takes inputs from both and produces the translated SQL

### 10b. The Power Comes from Combination

**Key statement (lines 267-269):** "I brought up a couple of specific agents that we could make, which by themselves don't do anything. But if you combine them with MCP and you combine them with an orchestrator, now you have something powerful."

The formula: **specialized agents + MCP connectors + orchestrator = functional system**. No single component is useful in isolation.

### 10c. The Human Role in Agent Workflows

**Key statement (lines 284-288):** "The general way that this goes for agents: agents do all of the boring stuff. As humans, we do things like edge case decisions, we look at the business logic, we give the final approval, and if there's anything that goes wrong, which there always is with any kind of agent workflow, there's almost nothing that'll work perfect out of the box. There's always that one weird edge case that we didn't handle. Humans need to see those, flag them up so that either a new agent can be brought in or some agent can be refined."

The division of labor:
- **Agents handle:** repetitive, well-defined, high-volume work
- **Humans handle:** edge case decisions, business logic judgment, final approval, and identifying gaps that require new agents or agent refinement

### 10d. Deployment Strategy: Non-Destructive Cloning

**Key statement (lines 277-283):** "Imagine you have a Cognos report that's currently pointing to your SQL servers. You want to point it to Databricks. Well, let's keep that existing Cognos report in place as is. Let's not touch it. But let's build a copy of it, a clone of it, that is connected up to Databricks. That way we're not messing with anything that's working today, but we're able to still connect into it and show that data works."

The approach: never modify the working production report. Instead, clone it, point the clone to Databricks, and validate the clone independently. This eliminates risk to existing production workflows during migration.

Colin also mentioned agent-driven validation: "Even an agent that can go and take screenshots of the reports or do pointwise validation on certain key values within a report" (line 282).

---

## 11. Infrastructure and Deployment Approach

### 11a. Build on the Client's Platform

**Key statement (lines 380-386):** "From an infrastructure perspective... this is where it gets tough from a demo perspective, because I can show it working on our side of the house. I can't show how it'll work on yours without getting it set up for you."

**Key statement (lines 384-386):** "If you are on Azure and you want us to use all Azure services and any of the AI subscriptions that you have, it's definitely better to go that way, especially from a cost perspective."

The infrastructure principle: the agent system is built on the client's existing cloud platform using their existing AI subscriptions. This is both a cost optimization (no duplicate subscription spend) and a security advantage (data stays within the client's environment).

### 11b. Security Positioning

Colin addressed the security concern directly after Meher mentioned that Sephora's security team had previously blocked an MCP server attempt (lines 474-477).

**Key statement (lines 646-666):** "We do this all the time, so we're used to talking to IT and security teams to kind of tell them, no, we're not crazy. No, we're not going to hurt anything. We know how to talk to them about this to kind of unblock things."

Colin's approach to security objections:
1. **Primary argument (80% of objections):** "As soon as people understand, hey, we're doing this with your own tools within your own environment, literally no information goes beyond that" (lines 663-664)
2. **Secondary argument (remaining 20%):** "Any guardrails you want, we can put in the system" (line 666)

The fact that Sephora's security team had already blocked a previous MCP server attempt was flagged as a known risk that BayOne would need to help navigate.

---

## 12. What This Architecture Is Not

### 12a. Not Model Retraining

Colin explicitly stated (lines 255-257): "Learning, a lot of people think that means we're retraining models. We're certainly not doing that." The system uses context accumulation, not model fine-tuning.

### 12b. Not "Just Claude"

Colin drew a direct comparison (lines 263-266): even Claude Code with skills and agents is "still too big of a problem for Claude to do by itself." The framework provides the persistent state, routing, and orchestration that a standalone Claude session cannot.

### 12c. Not a Pre-Built Package

Consistent with Andrew's observation from the previous meeting, this is a custom-built solution. The MCP servers are built from scratch (line 154), the agents are composed for the specific environment, and the playbooks are derived from Sephora's own processes.

---

## 13. Sergey's Framework Constraint: Configuration Over Code

Sergey provided a critical technical constraint for agent design at lines 585-610.

**Key statement (lines 585-605):** "On Databricks, we develop frameworks, config-based, where you don't need to do, let's say, Python development or something. So you just need to do configuration. And we have, let's say, thousands of jobs running in production today, support team aware how to support them and so on. So basically, no need to create, let's say, new framework by using some Python or something."

Sergey's constraints:
1. **Existing config-based framework on Databricks** — already running thousands of production jobs
2. **No new code required** — agents should generate YAML configuration files, not Python or Scala code
3. **Must fit existing support model** — the production support team already knows how to support the current framework; introducing a new one adds cost
4. **DataStage stored procedures should convert to SQL** (preferably Spark SQL) — not to Scala or Python, because stored procedures are already SQL-based and the conversion is more natural
5. **Anti-pattern: Databricks notebooks with hundreds of cells** — Sergey explicitly called this out as a maintenance nightmare (line 598: "When you have Databricks notebook with hundreds of cells inside this notebook and how to maintain it, I don't know, it will be nightmare to debug it")

The agent implication: agents must be designed to output YAML configuration files that fit the existing Databricks framework, not to generate new code. This is the exact scenario Colin's playbook concept addresses.

---

## 14. Current State of AI Usage at Sephora

Meher provided the clearest picture of where Sephora is currently using AI in this process (lines 224-228):

1. **Claude for XML extraction** — They are using Claude to extract joins, source tables, and other metadata from exported Cognos report XML files
2. **Claude for SQL code translation** — Using Claude to help convert SQL Server code to Databricks-oriented code
3. **XML export is still manual** — "Getting that XML, that is still manual effort, we have to log into Cognos, go to report studio, download the XML" (lines 226-227)
4. **No end-to-end agent workflow exists** — "We haven't really come up with any agent yet that can do this process end to end" (line 228)

This establishes the baseline: Sephora is using Claude as a point tool for individual steps but has not connected the steps into an automated pipeline. The MCP-based approach would eliminate the manual XML export step and connect the individual Claude interactions into a coordinated agent workflow.

---

## 15. Frameworks Mentioned

Colin did not name a specific agent framework (such as LangGraph, CrewAI, or AutoGen) in this meeting. He referred to "frameworks" generically at lines 262-266 when distinguishing between standalone Claude usage and framework-orchestrated agents. The specific framework selection was not discussed, likely because it is an implementation detail that would be determined during engagement rather than during pre-sales technical discussion.

---

## 16. Agreed Next Steps for Demo

The session concluded with agreement on a demo approach at lines 632-640:

1. Sephora will provide a Cognos report (full XML) from the finance subject area
2. Sephora will provide the corresponding Databricks table/schema definitions
3. BayOne will build the MCP server for Cognos and demonstrate:
   - Programmatic connection to and dissection of the Cognos report
   - Remapping the report to point to Databricks
4. First demo will be a lift-and-shift scenario (same structure assumed in Databricks)
5. Second demo may cover the remapping scenario (different structure in Databricks requiring mapping agents)
6. Validation against live Databricks is deferred due to security access constraints — the demo will operate disconnected from Sephora's live environment

Meher also suggested a secondary demo track: a DataStage job conversion to Databricks, noting they had previously attempted this with Lakebridge with approximately 85% requiring manual rework (lines 579-582).
