# 03 - Meeting: Agentic Architecture Discussion

**Source:** /sephora/edw_modernization/source/andrew-girishi-meeting1_formatted.txt
**Source Date:** 2026-03-05 (Andrew/Grishi Meeting)
**Document Set:** 03 (Andrew/Grishi Meeting)
**Pass:** Focused deep dive on the agentic architecture discussion between Andrew, Grishi, and Colin

---

## 1. Andrew's Vision: Multi-Agent Orchestration to Compress the Timeline

Andrew articulated the clearest statement of what Sephora is looking for from a prospective partner. His framing was strategic, not technical — he positioned the investment in agents as a reallocation of existing manual spend.

### 1a. The Core Vision Statement

**Key statement (lines 161-166):** "Can we, you know, is there a way we can create multiple agents, small little agents that can do all this little step by step for us? And they have a big orchestration kind of agent that orchestrates this entire flow, right? So then, rather than spending money on manual, you know, at the end of the day, we still need to spend the money, you know, in a contractor to do the manual work. Rather than spending that money there, I take the money and resources and spend it upfront to create all these agents so that it will then, once it's all done, then it can parallel run and do all the thing by itself."

Andrew's vision has four distinct components:

1. **Multiple small specialized agents** — not one monolithic agent but many small ones, each performing a discrete step
2. **A master orchestration agent** — a single coordinating agent that governs the entire flow across all the smaller agents
3. **Redirect manual contractor spend** — the investment in agent development is funded by reallocating the money that would otherwise go to manual contractor work
4. **Parallel execution at scale** — once built, the agents can run in parallel across the full scope of migration work simultaneously

### 1b. The Timeline Compression Argument

**Key statement (lines 169-170):** "If we can do that, then all of a sudden, you can parallel track a lot of this migration. And so then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half, or something like that, right?"

Andrew is framing agent investment as a timeline compression play — potentially cutting a three-year program to 12-18 months. He acknowledged QE validation would still be required (line 167: "Of course, at the end, you still need QE to validate your data"), but the core migration work would be parallelized through agents.

### 1c. Andrew's Market Assessment

**Key statement (lines 172-176):** "We have been talking this exact same conversation with a lot of different vendor right now. Because I know for a fact, right now outside there's no, no one has a pre, a package that we can just say, Hey, I will get, I want to buy your package or I want to pay something to get your package in so I can just run through this migration without any human involved or even a little human involved."

Andrew was transparent that:
- They are speaking with multiple vendors about this exact problem
- He knows no off-the-shelf package exists for this
- He is proactively searching for someone who can build the custom solution (line 176: "who out there can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing?")

This is a build engagement, not a buy engagement. Andrew understands that and is looking for a partner who can execute the custom development.

---

## 2. Colin's Response: The Palantir Ceiling

Before diving into architecture, Colin established the commercial landscape to calibrate expectations.

**Key statement (lines 187-197):** "Closest solution, which still would involve manual effort and still would be probably prohibitively expensive, to be honest, is Palantir. If you've ever gotten a demo from them, they'll come and say, you know, we can do these migrations. You don't even have to change anything. You can keep everything exactly where it is. And we'll be able to pipeline data. We'll do the ETL for you. We'll do the reports for you. We'll do everything. The problem is that's also going to come with six zeros attached to the price tag. And there is still always that manual effort that's involved."

Colin positioned Palantir as the commercial ceiling — the most capable off-the-shelf platform for this type of work — and then explained why it still falls short:
- Cost is prohibitive ("six zeros attached to the price tag")
- Manual effort is still required even with Palantir
- The human aspect of validating report necessity remains (line 198: "Someone actually has to do it, right?")

This framing served two purposes: it validated Andrew's assessment that no off-the-shelf package exists, and it established that even the most expensive commercial solution does not eliminate the need for the type of custom agent work Colin would propose.

---

## 3. Agent Swarm Architecture: Core Principles

Colin then laid out the foundational principles for how the agent system should be designed.

### 3a. Agent Specialization: Small, Specific Agents

**Key statement (lines 199-207):** "From agent's perspective, it's exactly the right thing to thought to it. It's an agent swarm, right? So it's an orchestrated cluster of agents that you have if you've spun off for a specific task. Agents in general work better if they're more specific. So if you try to have, you know, a small subset of agents that, this is my reports agent. No, no, no. Here's the reports validator agent. Here's the one that checks the past state and the present state, just as two small examples."

Colin's key design principle: **agents work better if they are more specific**. He explicitly corrected the instinct to build broad-purpose agents (a "reports agent") and instead advocated for narrow-scope agents (a "reports validator agent" and a "past state / present state checker" as two examples of granularity).

**Key statement (line 207):** "The more specific you go with agents without going overly specific, the better off you are."

There is a balance — over-specification is also a risk — but the bias should be toward specificity.

### 3b. Model After Real-Life Team Roles

**Key statement (lines 246-251):** "Agent swarms work best if you model them after real life things. So how does this work in real life? Imagine if AI wasn't a part of the picture. What would the team look like? That's how you can think of designing those agent swarms. So each role that a person plays or each primary function becomes part of the swarm."

This is the design methodology: take the human workflow, identify every distinct role or function a person would perform, and each one becomes an agent in the swarm. This maps the organizational structure of a migration team directly onto agent architecture.

Colin applied this principle to validation (lines 327-329): "So if you told a human being to go and do this mapping, what would be the next human in the process? Who would check them? That becomes another agent in the flow to actually go and validate that."

---

## 4. Orchestrator + Judge Pattern ("Grumpy Old Man Agent")

This is the most specific architectural pattern Colin described. It involves two coordinating agents — not one.

### 4a. The Two-Agent Control Layer

**Key statement (lines 312-317):** "What ends up happening is there is an agent that is the orchestrator. He's not the only one though. So there's an orchestrator agent there, but there's also a judge. And the judge and the orchestrator have to be in sync. The judge, I call him like the grumpy old man agent, kind of yells at everyone, stay on track, follow this workflow, do not deviate. If it deviates, it rejects immediately and lives back."

The pattern:

1. **Orchestrator agent** — manages the flow of work across the swarm, assigns tasks, tracks progress
2. **Judge agent** — enforces workflow compliance, rejects deviations immediately, forces the swarm to stay on track

The judge and orchestrator are separate agents that "have to be in sync." The judge is not a passive reviewer — it actively monitors all agent output and immediately rejects anything that deviates from the prescribed workflow. Colin's "grumpy old man" metaphor captures the intent: the judge is adversarial by design, intentionally strict, and intolerant of drift.

**Key statement (line 319):** "We can't do that quite with humans, but we can do that with AI."

Colin made the explicit point that this level of rigid enforcement is actually easier to achieve with agents than with human teams. A human reviewer might let things slide or apply inconsistent standards; the judge agent enforces the same standard every time.

### 4b. Human Reporting Without Black Box

**Key statement (lines 330-332):** "There still have to be there at the end, but they do get a little bit out of there for the early part. In addition, we can have reports generated during this to keep humans aware of what's going on instead of it just being a black box."

The orchestrator + judge pattern produces two outputs:
1. The actual migration work product
2. Progress reports for human stakeholders

This avoids the "black box" problem — the scenario where the system is running but no one knows what it is doing until it completes (or fails). Colin specifically flagged this as a design requirement: transparency during execution, not just at the end.

---

## 5. Schema Mapping Validation: The Three-Step Workflow

Grishi asked specifically about schema mapping automation (lines 254-276), and Colin walked through the detailed process. This is the most granular technical description in the meeting.

### 5a. Grishi's Question and Context

Grishi described the current state: they are already using Claude for schema mapping, feeding it schemas from two systems (EDW and Databricks Data Platform), and getting mappings back. The problems are:
- **Manual intervention required** — they have to manually feed schemas and retrieve results (line 268)
- **Not one-to-one** — three tables in EDW could map to one table in the data platform (line 272)
- **Not 100% accurate** — the AI mapping has errors that require human correction (line 273)

### 5b. Step 1: Non-AI Exploration and Crawling

**Key statement (lines 281-294):** "The first step in this, and this is kind of the trajectory that we follow, we actually stay away from AI until we have to. The reason for that is the higher up in the food chain AI gets implemented in, the more kind of telephone effect happens. So if you can wait to use AI until a little bit later in the process, it works better."

**Principle: Deterministic first, AI second.** Colin's rationale is that introducing AI early in the pipeline creates compounding errors — the "telephone effect" where each AI-processed step introduces small inaccuracies that cascade through subsequent steps.

**Step 1 detail (lines 285-293):** "Step one always for this is to build this mapping and hierarchy out. We kind of do a big exploration. That exploration is not done with AI. That exploration is literally tell me all the tables, tell me all the different schemas, tell me all of anything that you want us to factor into this. And let's go and map out those structures first, and let's preserve those. That's almost the same as if you were to just do an exploring SQL, and you were to just say, what is all the whole view of it? Usually people get worried when we say that, because they'll say, boil the ocean. It's not boiling the ocean, it's just a recursive, almost like we're crawling through a folder, just in a much more complex way of the SQL."

Step 1 is pure deterministic data collection:
- Enumerate all tables, schemas, and structures across both source and target
- Recursively crawl the database structures (compared to crawling a folder hierarchy)
- No AI in the loop — this is programmatic exploration
- Output: a flat, reliable picture of the full playing field
- Purpose: establish a trustworthy baseline that never drifts (line 295: "That way we have something reliable to go and trace back on")

### 5c. Step 2: Initial Non-AI Mapping (~30% Coverage)

**Key statement (lines 297-303):** "Step two is then to now try to do the initial mapping. The initial mapping, that's why I started to break it up into the AI and non-AI phases. We try to do that first without AI in the mix. We try to see what fields are common, which share a similar kind of route through this. So if it's one report here, but that same report is the source for three more reports over here, we can say with higher confidence that those fields are interrelated."

Step 2 is deterministic pattern matching — still no AI:
- Match fields by name, type, and structural position
- Trace report lineage: if report A feeds reports B, C, and D, the fields in all four are interrelated with high confidence
- Apply rule-based matching to find obvious correspondences

**Yield estimate (line 301):** "The first one did probably 30% of the work."

Colin estimated this deterministic phase resolves about 30% of the mapping. This 30% is high-confidence — things you can be certain about without AI judgment.

**Key statement (lines 302-303):** "It's not super useful by itself, but it is enough to give you certainty on things that you're actually 100% certain on. It's a good launch and off point, so that doesn't ever get confused later."

The 30% serves as the anchor: these mappings are locked in and will not be revisited or second-guessed by later AI processing. They form the foundation layer.

### 5d. Step 3: AI Mapping with Big-World/Small-World Consideration

**Key statement (lines 304-310):** "For the AI mapping, that's where you have to kind of play a big world, small world on it. Big world means I need to consider everything at once. If I do things in a vacuum, then I don't have the needed context to really understand what I'm talking about. And that's certainly true for AI agents. They can do a task, but are they doing the task with respect to the entire system or just with respect to that single report or file or circumstance? The small world part of it is that, unfortunately, AI is not that advanced that you can just throw the whole thing at it and say, figure it out."

The **big-world/small-world** framing describes the fundamental tension in AI-assisted mapping:

- **Big world:** The AI agent needs global context — awareness of the entire data estate — to make correct mapping decisions. Mapping in a vacuum produces errors because the agent does not know what else exists or how things relate across the broader system.
- **Small world:** AI cannot process the entire estate at once. Context windows have limits. Processing everything simultaneously is not technically feasible at the scale of 6,000+ reports.

**Resolution (lines 311-316):** The orchestrator + judge pattern resolves this tension. The orchestrator manages which small-world tasks the agents work on, while the knowledge graph (described in Section 6) accumulates the big-world context. The judge ensures agents do not deviate from the workflow or make decisions that conflict with already-established mappings.

---

## 6. Knowledge Graph and Flywheel Concept

Colin introduced the knowledge graph as a persistent, accumulating data structure that solves the "hot and cold" inconsistency problem.

### 6a. The Flywheel

**Key statement (lines 226-228):** "The difference is that this system would learn. So instead of doing that as kind of a one-off, this always feeds into a central knowledge graph. So that anything we learn in one report, any connections it has, any mapping that it has, that's preserved going forward. So that helps you kind of build this flywheel so things get better over time."

The knowledge graph is the mechanism that converts agent work from a series of independent one-off tasks into a compounding process:
- Every report analyzed, every mapping confirmed, every connection discovered is stored
- Subsequent reports benefit from everything already learned
- Performance improves over time as the graph grows richer

### 6b. Solving the "Hot and Cold" Problem

**Key statement (lines 229-234):** "Because typically when you do the one-off, I'm sure the team's probably found this. Even with the help of things like Claude to do the conversion, you'll find that it's kind of like hot and cold sometimes. Sometimes it works really, really well. Other times it completely doesn't work. And the manual effort to go and copy code here, paste it into this, check the report, go back and do that iteration, it's faster for sure than doing it all manually, but it's still a process."

Colin directly acknowledged the inconsistency problem that Grishi's team has been experiencing with their current Claude-based approach. The knowledge graph addresses this by providing accumulated context that reduces the variability of AI outputs. Each agent invocation benefits from what was learned in prior invocations, rather than starting from scratch each time.

### 6c. Scalability Through the Knowledge Graph

**Key statement (lines 474-478):** "The great thing about these is they scale independent of people. So once we have the agents going, that's one of the strongest parts about them. We still need people to do the work. But the more and more we scale the agents, the less and less we need. So the work to take on 100 tables or 100 different reports is about the same as if we were to do 1,000. Because once we have that initial structure in place, this scales naturally."

The knowledge graph is what enables this non-linear scaling claim. Without it, processing 1,000 reports would be roughly 10 times the effort of processing 100. With a knowledge graph accumulating learnings, the marginal cost of each additional report decreases as the graph becomes more complete.

---

## 7. MCP vs. Raw Agent Tool Calls

Colin drew a specific distinction between how agents interact with external tools.

**Key statement (lines 335-339):** "On the actual tool integration part of it, that's a fun one. That actually becomes more of an MCP problem than an agent problem, because you want to get all these different tools connected. Agents can definitely do that. But agents combined with MCP to actually interact with those utilities and tools is much better because it's more reliable. So you can make sure that an agent is testing something the exact same way each and every time instead of just telling it, go figure this out."

The distinction:
- **Raw agent tool calls:** The agent is told to interact with an external system and figures out how on its own. This is unreliable because the agent may approach the interaction differently each time.
- **MCP (Model Context Protocol) integration:** Provides structured, deterministic interfaces for agents to interact with external tools. The agent calls the same interface the same way every time, ensuring consistency.

Colin framed MCP as solving the reliability problem for tool integration. The agents handle the intelligence (what to do), while MCP handles the mechanics (how to interact with the tool) in a repeatable way.

**Key statement (lines 339-340):** "So having structure to it is kind of the secret sauce, I would say. Having that planning there."

---

## 8. LangGraph for Custom Orchestration

Colin named LangGraph as the framework for building the orchestration layer.

**Key statement (lines 345-349):** "Even for us, that would be LangGraph. We do something custom with LangGraph, something that scales. That's much better than just trying to do it in Claude Code. Claude Code can get you pretty far, but with 6,000-odd reports. That's pretty tough to do and tough to do consistently."

The rationale for LangGraph over Claude Code:
- **Scale:** Claude Code works well for smaller scope but breaks down at the scale of 6,000+ reports
- **Consistency:** LangGraph provides custom orchestration logic that maintains consistency across thousands of invocations
- **Control:** LangGraph allows building the orchestrator + judge pattern with deterministic workflow enforcement, whereas Claude Code would rely on the model to self-govern

Colin acknowledged Claude Code's utility (lines 347-352): it "can get you pretty far," and team members who become proficient with it get faster over time. But the problem is that individual workflows evolve and drift — people start using Claude skills, their approach changes, and consistency across the team degrades. LangGraph provides the structured framework that prevents this drift at scale.

---

## 9. Token Cost and Infrastructure Discussion

### 9a. Token Cost Dynamics

**Key statement (lines 320-325):** "Token cost for these actually isn't too bad. It's just token cost is directly proportional to speed when you're talking about agent swarms. So if you want it to happen faster, more tokens are being consumed, it'll take a little bit longer if that's a worry. The reality for it is that if you're using something like Claude Code and you have, for instance, the Max license, it's very tough to exhaust that. If you're paying by API, it gets expensive."

Colin established the cost/speed tradeoff:
- **Speed and token consumption are proportional:** Faster execution means more parallel agents, which means more tokens consumed simultaneously
- **Enterprise/Max licenses:** Make agent swarms economically feasible because they are not billed per-token
- **API billing:** Gets expensive quickly for agent swarms due to the volume of tokens processed

### 9b. Azure AI Foundry as Cost Optimization

**Key statement (lines 413-416):** "If you're on Azure, for instance, you have Azure AI Foundry. So then you even have another level of sophistication there because everything with Azure AI Foundry is just as secure as when you use Outlook as one example. So using Azure AI Foundry models are way cheaper as well than their commercial API counterparts. So you can do a lot of cost optimization just by using infrastructure."

Colin positioned Azure AI Foundry as a significant cost lever:
- Models deployed through Azure AI Foundry are cheaper than their commercial API equivalents
- Security is enterprise-grade (same as other Azure services)
- This is a "hidden bonus that a lot of people kind of miss on" (line 417)

### 9c. Platform-Agnostic Approach

**Key statement (lines 418-422):** "If you go directly, like let's say the Claude API, super expensive. I would never use that as a standalone API. OpenAI's API much better than Claude in terms of performance versus cost, but you're still at the mercy of that API and especially any agent swarms. You're going to hit a limit very quickly. Versus whenever you deploy it on Azure, you have absolute control. And this same paradigm is true for Azure, afraid of us for GCP. It's just whatever flavor they want. So for instance Vertex for Google, you know AWS is Bedrock, but you can do any of these on any of those platforms."

Colin named three enterprise AI platforms:
1. **Azure AI Foundry** — for Azure/Microsoft environments
2. **Vertex AI** — for Google Cloud Platform
3. **Bedrock** — for AWS

His recommendation was clear: deploy on the enterprise platform rather than using commercial APIs directly. The benefits are cost control, rate limit avoidance, and security compliance. He was platform-agnostic in the proposal — whatever Sephora already runs on is what should be used.

---

## 10. Build on Sephora's Infrastructure vs. BayOne's

Andrew asked directly whether BayOne would build agents in Sephora's ecosystem or bring their own tools (line 383-384).

### 10a. Colin's Preference: Build on Client Infrastructure

**Key statement (lines 388-403):** "My first instinct is always just build it. If it's a custom situation, we need to build it. But also, my language, I like to say, I'll meet you at your home. So we don't want to force you into using another tool. You're already getting another tool. So I add more to that. The other thing is that, for better or for worse, it's hopefully a temporary effort. You know, once that three year period is done, you want to be done with it. You don't want to have this debt that you have an additional tool in the stack that's adding technical debt to everyone on the team. Just one more baby to babysit. So for us, it would be built on your infrastructure if that is desired."

Colin's rationale for building on Sephora's infrastructure:
- No additional tool to manage after the engagement ends
- No technical debt left behind
- The agent system is purpose-built for the migration and should be retired when the migration is complete
- BayOne follows the client's organizational rules, approved tooling, and even uses client-issued hardware when required

### 10b. Andrew's Confirmation

**Key statement (lines 408-411):** Andrew confirmed this made sense: "I'm assuming, you can use our account infrastructure. Because as you run through those agents, like you mentioned, it's going to use tokens. And we have enterprise account or whatnot, right, with Claude and with all those stuff, even Google Vertex AI."

This confirmed that Sephora has enterprise accounts with both Claude (likely Anthropic enterprise) and Google Vertex AI. This gives BayOne multiple platform options for deploying the agent system on Sephora's own infrastructure and token budgets.

---

## 11. Grishi's Current State: AI Already in Use, Seeking Automation

Grishi provided important context about where the team already is with AI adoption before the agentic discussion.

### 11a. Current AI Usage

**Key statement (lines 141-146):** "We are using Claude, Lakebridge, and we are experimenting with all these tools... but at this point we are not finding something like we want to ideally have an agent that would integrate with, let's say, Cognos, all these reports, and it would re-engineer the metadata queries and it can automatically point to our semantic layer that's sitting on Databricks."

Grishi's team is already using:
- Claude — for code conversion and mapping
- Other experimental tools (referenced as "Lakebridge" and others)

But they have not found a solution that can:
1. Integrate directly with Cognos
2. Automatically re-engineer metadata and queries
3. Point output to the Databricks semantic layer without manual intervention

### 11b. Current Manual Workflow

**Key statement (lines 146-147):** "We have Data Stage tool, which is the ETL tool that grabs data from different sources and dumps it into our SQL data warehouse. So we would want an agent to go integrate with Data Stage, read all that and re-engineer code automatically on Databricks."

The current process for Data Stage migration (lines 146-147): going to each job individually, extracting the XML, feeding it to AI, reviewing the re-engineered code, and manually deploying to Databricks. This is the manual, job-by-job process that Andrew wants to replace with orchestrated agents.

### 11c. The 30% Efficiency Gain

**Key statement (lines 158):** Andrew noted that "the efficiency gain that Grishi and the team had figured out was about 30%."

The team's current AI-assisted approach (manual Claude usage for SQL conversion) has yielded approximately 30% efficiency improvement over fully manual work. Andrew's vision is to move well beyond 30% through full agent orchestration.

---

## 12. Andrew's Validation Requirements

Andrew articulated specific criteria for moving forward with any vendor.

### 12a. Feasibility Given Legacy Software Versions

**Key statement (lines 514-523):** "Because of our version of the software, for example, Cognos that we have is a very, very old version. We actually, I think it's like a 10.3 or 10.2, something like that. And it's super old version. Data Stage, it's not the latest version either. And so what I don't know is whether because even in order for the AI agent to be able to go in and read stuff out of the software or this metadata, either this software has an open SQL server for some of that kind of database that you can just easily have the AI to go with, or it has an API endpoint or some sort. Otherwise, your agent it can be as smart as you can be. It won't be able to connect to that software."

Andrew's concern: the software versions are old (Cognos 10.2 or 10.3, older Data Stage), and agents need a way to actually connect to them — either through a SQL interface, API endpoint, or some other mechanism. If no connectivity path exists, the agent system is "moot point."

Colin's response (lines 534-537) was that older software is actually easier to integrate with: "The good news with older software, to be honest with you, is the same reason why it gets old... It's easier to get into older software." He noted that newer software versions add security layers that make integration harder, while on-prem legacy systems are often more accessible.

### 12b. Proof That Agents Will Actually Shorten the Timeline

**Key statement (lines 525-529):** "Is it even possible that at the end of the day, having those agents created will definitely shorten our time in terms of the flow, right? So before we really committed to deep dive and create those agents... I just want to make sure that the vision and I feel comfortable that yes, the wild thinking is not wild, it's real, it can be done."

Andrew wants two forms of confidence before committing:
1. **Technical feasibility** — that agents can actually connect to and interact with their legacy systems
2. **Timeline benefit** — that the investment in building agents will demonstrably compress the migration timeline

He was explicit that he does not care whether the proof comes from a POC on BayOne's own data, a demo with mock data, or something else (line 528). He just needs to see it working.

---

## 13. Summary: The Complete Architecture as Described

Assembling all of Colin's statements into one coherent picture, the proposed agentic architecture for Sephora's EDW modernization consists of:

**Control Layer:**
- **Orchestrator agent** — manages task assignment, sequencing, and progress tracking across the swarm
- **Judge agent** ("grumpy old man") — enforces workflow compliance, rejects deviations, keeps all agents on the prescribed path

**Worker Agents (modeled after human team roles):**
- Each distinct function in the migration workflow becomes a specialized agent
- Examples mentioned: reports validator, past-state/present-state checker, schema mapper, business logic extractor
- Bias toward specificity — many narrow agents rather than few broad ones

**Infrastructure:**
- **LangGraph** — custom orchestration framework (preferred over Claude Code for 6,000+ report scale)
- **MCP** — structured tool integration layer (preferred over raw agent tool calls for reliability)
- **Knowledge graph** — persistent, accumulating data structure that stores all learnings across reports and feeds the flywheel

**Workflow for Schema Mapping:**
1. **Step 1 (No AI):** Deterministic crawling and enumeration of all tables, schemas, and structures across source and target systems
2. **Step 2 (No AI):** Rule-based initial mapping using field names, types, and lineage tracing (~30% of mappings resolved with high confidence)
3. **Step 3 (AI):** Agent-powered mapping with big-world context (full system awareness via knowledge graph) applied through small-world tasks (individual report/table scope managed by the orchestrator)

**Deployment:**
- Built on Sephora's enterprise infrastructure (Azure AI Foundry, Vertex AI, or Bedrock depending on their platform)
- Uses Sephora's enterprise token accounts rather than commercial API billing
- No new tools left behind after the engagement — agents are purpose-built and retired when migration completes

**Economics:**
- Token cost proportional to execution speed
- Enterprise/Max licenses make swarms economically viable
- Azure AI Foundry models significantly cheaper than commercial API equivalents
- Commercial Claude API explicitly called out as too expensive for agent swarms at this scale
