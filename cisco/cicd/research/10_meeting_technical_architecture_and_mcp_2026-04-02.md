# 10 - Meeting: Technical Architecture and MCP Strategy

**Source:** /cisco/cicd/source/srini_team_meet_04-02-2026.txt
**Source Date:** 2026-04-02/03 (CI/CD Track Sync Up)
**Document Set:** 10 (First meeting with Srinivas's full CI/CD team)
**Pass:** Technical architecture, MCP strategy, database landscape, and consumption model

---

## Overview

This is the first CI/CD Track Sync Up meeting with the full working team. Prior meetings (Sets 06, 06a) were discovery sessions with Anand, Srinivas, and Divakar. This meeting brings in **Justin** (build infrastructure, MySQL databases, existing AI fix-suggestion tools), **Anupma** (DevEx organization, CAT-related databases, Cassandra), and **Divakar** (infrastructure, NX-OS CI workflow WebEx space) alongside **Srinivas** (DeepSight platform lead, engagement technical authority) and **Colin** (BayOne).

The transcript is a speech-to-text capture with significant distortion. Key mappings: "Walker"/"the worker" = **Divakar**, "NCP" = **MCP** (Model Context Protocol), "cat"/"CAT" = a Cisco-internal CI tool, "CLAM"/"LAM" = code analysis tools for call graph generation, "CRFT" = a Cisco-internal instrumentation tool that runs on the switch, "Bazaar"/"Mazar" = **Mazar** (an engineer on the call graph team), "Pashini" = likely **Anupma** or another team member providing context to attendees unfamiliar with the engagement, "Naga"/"Nara" = a Cisco engineer who has (or should have) built WebEx scraping tools, "deep site"/"deep side" = **DeepSight** platform.

This document extracts the technical architecture discussion: call graph / impact analysis, MCP strategy framework, database landscape, build log analysis approach, user consumption model, and Airflow orchestration decisions.

---

## Call Graph and Impact Analysis

### What the Call Graph Is

Srinivas introduces the call graph as a function-level impact analysis capability. His requirement statement is direct: "If the function is changing, I want to know the impact. Who is the caller and calling?"

The call graph is generated from the **CLAM/LAM system** -- Cisco's code analysis tooling. Srinivas describes it as "a new option in the [compiler], when you compile a code." It is a compiler-level feature: when the NX-OS codebase is compiled, the CLAM/LAM system can optionally produce a graph of function-to-function call relationships. This is not runtime tracing. It is static analysis derived from the compilation process.

The call graph sits "on top of" the build system (referred to as "the puzzle" in the distorted transcript, likely Bazel). It is a compilation-time artifact, not an application-layer tool.

### Two Approaches to Call Graph Generation

Srinivas defines two distinct approaches, both of which are required:

**Approach 1: Baseline from Nightly Build (Static Database)**

The first approach generates a complete call graph from the nightly official build. Srinivas: "You can generate it as a nightly build, like a Cisco [build] generated. Equivalent of that, as a part of your [build] process, you can create a separate DB and keep it."

This produces a **baseline database** -- a snapshot of the entire function call graph as of the most recent nightly build. Think of it as a lookup table: given any function in the NX-OS codebase, you can query who calls it and what it calls.

Key characteristics:
- Generated as a parallel output of the nightly build process
- Stored in a **separate database** ("a look-up database")
- Does **not** go into the existing build image: "This is not going to be going into the existing image, but it's going to be something on top of that one"
- Runs **in parallel** to the existing build process: "I can run it in parallel to the existing build process to bring in the data"
- Requires APIs on top of it for consumption: "If you have any [way to] figure it out how to provide APIs on top of it and whatnot, that's a different problem"

**Approach 2: Dynamic Generation for New Code/Files**

The second approach addresses a gap in the baseline: new functions, new files, and new code that do not exist in the nightly build snapshot.

Srinivas: "The user may be touching new add-in, new files, new functions. For that, the baseline will not have it. It will not have it. Whatever the image is picking."

To cover this, Srinivas has asked Mazar to create a **run script equivalent** that dynamically builds the call graph for new code only: "We asked [Mazar] to create one more run [script] equivalent of a run script, which dynamically goes and builds the call graph with the new coding, for that change, for the new [modified] file."

This produces a supplemental call graph for the delta -- the new or changed code that the baseline does not cover. Combined with the baseline, it gives complete function-level impact visibility for any change, whether it touches existing functions or introduces new ones.

### Assignment and Ownership

Srinivas assigns this explicitly:
- **Justin and Mazar (with Tim):** Create the baseline database. "We need Justin and your help to say, and maybe work with Mazar, how do you create the database? What is needed?"
- **Mazar:** Dynamic call graph generation script for new code. "I'm hoping Mazar will give you something."
- **Justin:** May also need to be involved in the dynamic approach: "but [if] required you can be part of that, which is both ways."
- The database infrastructure for the baseline also needs Justin's involvement: "if we wanted to add the [build] infrastructure to create a database with the baseline related things, that also we need to be involved into."

### Distinction from CRFT

Someone on the call asks about the relationship between the call graph and CRFT. Srinivas draws a hard line: these are **two different independent things**.

- **CRFT** runs on the switch (the actual NX-OS hardware). It is a function-level counter -- it tells you which functions were invoked at runtime, which functions were hit, etc. This is runtime instrumentation.
- **Call graph** is generated at compile time from the CLAM/LAM system. It tells you the static call relationships between functions in the codebase. This is build-time static analysis.

The questioner probes for overlap: "I'm just trying to see if there is any common or typically risky." Srinivas confirms they are independent: "So that one and this one are two different independent things."

### Integration into the CI Pipeline

Srinivas places the call graph within a broader code review and CI pipeline architecture:

- **IDE level (VS Code):** Code review is "shallow" -- catching basic mistakes. Srinivas: "IDE code [review] will be a little bit shallow. Shallow meaning I don't want them to make mistakes, basic mistakes."
- **CI pipeline level:** Code review is deep and extensive, incorporating the knowledge graph, NX-OS domain knowledge, and the call graph as one element. Srinivas: "In the CI pipeline we do very extensive, very deep dive, with all the knowledge graph, NX-OS knowledge, so many other things. One of the elements is this [call graph]."

He clarifies the workflow boundary: "VS Code is in the developer workflow, IDE is code review, right? That's all in the developer workflow, whereas [the] CI pipeline falls in the PR workflow. So both will be done -- developer workflow as well as the CI workflow."

The XR team (Cisco's IOS-XR group, a sister organization) is also doing both IDE-level and CI-level code review, with "different metrics, dashboard, this and that."

---

## MCP Strategy Framework

### Srinivas's Decision Framework

Srinivas articulates a systematic framework for deciding when and how to build MCPs (Model Context Protocol servers). This is the most architecturally significant content in the meeting for the BayOne engagement, because it defines the methodology for connecting DeepSight to every backend data source.

The framework follows a decision tree:

1. **Inventory data sources.** Identify all databases and artifact stores in the CI/CD pipeline.
2. **Check: does an MCP already exist for this data source?**
   - **If yes:** Evaluate all tool calls the MCP supports. Map those tool calls against user requirements. Determine: "Is this tool call enough to solve the user [needs]? If not, what additional tool calls we need to do?"
   - **If no:** Take the database source as input and create an MCP with appropriate tool calls. "We need to go figure it out, take the database source as an input source and say now how do I create tool calls around [it]."

3. **Design tool calls for dual-mode consumption.** Every tool call must serve both the user-driven (self-serve) model and the agentic workflow model. Srinivas: "When we design these tool calls for the MCPs, we need to make sure that both these things are overlayed together."

4. **Static vs. AI-generated tool calls.** Two approaches to creating the tool calls: "One is we statically create these tool calls or use AI to basically create generic tools so that we enable agentic workflow." The choice depends on whether the use case is predictable (static tool calls) or requires flexibility (AI-generated generic tools).

### The Two Overlay Models

Srinivas repeatedly emphasizes that every MCP and every tool call must support **two models simultaneously**:

- **User-driven (self-serve):** The user explicitly goes to the DeepSight application, asks a question, and gets an answer. No automation, no proactive behavior. The user initiates.
- **Agentic workflow:** The system proactively takes action, guides the user, and chains steps together with approval. Srinivas: "System will guide him saying that, I'm taking this next step, is it OK?"

These are not sequential phases or either/or choices. They coexist: "It's both ways. Depending on the user behavior, they can pick one or the other way. Let the user figure it out what they want. We don't have to dictate. That system has to do both ways."

This is described as an **overlay functionality on top of the backend data services.** The MCPs provide the data layer. The overlay provides the interaction model. The same tool calls serve both modes.

### CAT Databases: The Organizational Blocker

Srinivas identifies a specific data source where MCP creation is blocked by organizational boundaries: the CAT-related databases controlled by Anupma's DevEx team.

When Srinivas asks Anupma about database access, her response is guarded: "We have the API but the database is not exposed, and I'll have to discuss. I can share more details offline."

Srinivas pushes: "Two ways. The [APIs] can help us, or if the [APIs] do not help, they need to expose the database and we'll create our own stuff. So that's the bottom line."

He acknowledges the friction: "I know there may be some people issues and organization issues and so many other things that may be there, but we need to figure it out a way. I mean, this way or that way. We need access to the [data]. Basically, the DB."

Anupma deflects to offline discussion. Srinivas accepts but does not relent: "I understand. I understand that maybe some reservations may be there, but yeah, we'll chat."

He also presses for understanding of the database type. Anupma volunteers: "I can tell [you] like it is a Cassandra." But for exposure, "I will discuss with you."

This is the clearest example in the transcript of what Srinivas means by "people issues and organization boundaries" -- the data exists, the databases exist, but organizational ownership creates friction around exposing them. Srinivas frames this as a blocker he intends to push through: "We need to unblock for the end of the [project]. We can take our own [approach] and we can have... whatever is needed, but we need to get the data exposed."

---

## Database Landscape

The meeting reveals a more complex database landscape than was documented in Set 06. Set 06 identified MySQL (structured data) and MongoDB (raw pipeline data). This meeting adds Cassandra and NFS as additional data stores, and clarifies Justin's MySQL scope.

### MySQL (Justin's Team -- Build Data)

Justin confirms: "We have it on MySQL." His MySQL database tracks official build data: "For all the official [builds], we keep track, you know, every time that it's triggered, status, like we pass, fail, all that."

Justin's team has also started building an **existing MCP** on top of this MySQL database. The MCP currently supports basic tool calls: "We have some basic things like we can call and get the latest QA [pass] rate, which build is the most recent. And we can also have some sanity results that also get posted to our databases as well."

This is the first confirmation in the research library that an MCP already exists within the CI/CD ecosystem. It is basic and limited to query-type operations (latest QA rate, most recent build, sanity results), but it exists and is functional.

### Cassandra (Anupma's Team -- CAT Data)

Anupma identifies Cassandra as the database type for the CAT-related data. This is the first mention of Cassandra in the engagement. No further technical details are provided in the meeting -- Anupma defers to offline discussion.

The significance: Cassandra is a wide-column NoSQL database optimized for high-write-throughput, time-series-like data. This makes sense for CI pipeline event data (check results, gate pass/fail, timestamps). However, Cassandra's query model is more constrained than relational databases -- you must know your access patterns in advance. Building an MCP on top of Cassandra requires careful partition key design and query planning.

### NFS (Build Logs)

Justin confirms that build logs are stored on NFS (Network File System), not in any database: "The logs and stuff all go to an NFS location, so the logs are not in a database or anything."

Key characteristics of the NFS log storage:
- **Retention:** 3-5 days. Srinivas: "That space is retained after three days, five days like that. We have policies."
- **Consumers:** Engineers and the sanity system. "Consumed by the engineers, and the sanity system, like the [testing systems]."
- **Not structured data.** These are raw log files, not queryable. They are files on a filesystem, consumed by humans and automated test systems, then purged.

Srinivas distinguishes the log data from the structured data: "The actual [build] status and other artifacts, other than the log, other artifacts [are] inside in the database for the state machine. But the logs are [only stored on NFS]."

### MongoDB (Previously Documented)

MongoDB was documented in Set 06 as the raw pipeline data store (on-prem, single location). It is not explicitly discussed in this meeting, suggesting it may fall under Anupma's DevEx domain or is already understood.

### Summary: Database Ownership Map

| Database | Type | Owner | Current Access | MCP Status |
|----------|------|-------|----------------|------------|
| MySQL | Relational | Justin's build team | Direct | Basic MCP exists (QA rate, build status, sanity results) |
| Cassandra | Wide-column NoSQL | Anupma's DevEx team | API exists, DB not exposed | No MCP; blocked by organizational boundaries |
| MongoDB | Document store | DevEx / shared | On-prem, single location (Set 06) | Unknown |
| NFS | Filesystem | Build infrastructure | Direct file access | N/A (logs, not a database) |

---

## Build Log Analysis

### Two Types of Builds, Same Log Format

Srinivas defines two build types that produce the same kind of log file but at different scales:

**Official Builds (Nightly):**
- Aggregate all commits from the entire day by **1,000+ engineers**
- "You're taking the commits that have been done for the entire day by 1,000 engineers and they're [combined]."
- Multiple PRs are accumulated and built together
- When a build failure occurs, the challenge is determining **which PR caused the failure** among many

**User Builds (Single PR):**
- A single engineer committing their own PR
- "The same build [log] can be generated when the user is committing his own PR."
- The engineer may also introduce a build failure
- Same log format as the official build, but the scope is narrower (one PR, one engineer)

Srinivas frames this as fundamentally a single problem: "One is more than one PR, same build. One [is a] single PR, same build, but log file is same."

### Two Failure Analysis Problems

From the build logs, Srinivas identifies two distinct problems to solve:

1. **Which PR caused the build failure?** This is the unsolved problem. Justin explicitly confirms: "I don't think we have anything for finding which commit [caused the] build [failure]. We haven't done that yet." For official builds with 1,000+ engineers' commits, this is the high-value analysis: isolate the offending PR from among many.

2. **How do we fix the build failure?** Justin's team has existing tools for this: "We have some things where we can even use AI and it comes up with like a decent fix basically." This is partially solved.

The downstream actions from failure identification are explicit:
- Alert the build team
- Identify which engineer caused the issue
- Send a message to that engineer
- Back out the PR if needed
- Srinivas: "Which PR [caused the] issue, can we know from the PR which engineer [caused the] issue, then alert the build guys to say, hey, can you undo this PR or whatever? Or put a [message] to the guy."

### Inference Cost Warning

Srinivas delivers an explicit warning about inference costs in the context of build log analysis. This is a design constraint, not a passing comment.

Srinivas: "Whatever we do, the inference costs are going higher. The [costs have] already increased by 4X."

He follows this with a direct prohibition: "I don't want to throw a [big] log and say, what is it?"

He then references that he screened Colin on this exact problem during their initial call: "One of my screening questions for these interviews for the team is exactly that. I screened you on the same question on the first day."

The message: brute-force approaches (feeding entire build logs to an LLM) are unacceptable. The solution must be engineered -- parsing, structuring, filtering -- before any LLM inference. Srinivas: "You can solve a problem in many ways, but the question is solve the problem in a right engineering way."

This aligns with the "two hats" principle from Set 06: solve the current need efficiently, and make it extensible for agentic infrastructure. Throwing raw logs at an LLM solves neither.

### Pre-Design Requirement: Understand the Log Structure

Srinivas is explicit that no design work should begin until the team understands the build log structure. He assigns this to Colin as a prerequisite:

- "You need to [meet with] Justin offline and understand what the build [log] will look like."
- "What is the structure and typical size of a full build and a user build?"
- "Understand what this log will look like. What is a typical log size."
- "Come up with a design on how do we [parse] it or how do you want to tackle it."
- "Understand [the engineer's life]. If I'm an engineer, how do I build it? Where do I see the log? What the build will look like? What a failure really means? Just understand the structure."
- "Even if you do a couple of meetings with Justin, it will not harm. Because you get the full view from him."

The instruction is: do not design before understanding. Meet with Justin one or two times, learn the log structure, learn the build process end-to-end, and then reconvene to design together: "Then after that, we'll step back and say what the design should look like and move forward."

### Real-Time Processing Requirement

Colin suggests extracting and preserving log content beyond the 3-5 day NFS retention window: "Even if they disappear after some time, and there's a constant refresh of them, essentially, we can still distill them down after we extract the content out, get it in structured format, preserve that for some time historically."

Srinivas confirms but adds a real-time constraint: "We will have to do it in the real time, right? They will fail, analyze, get the data." The analysis must happen when the failure occurs, not retroactively. Archiving is secondary to real-time detection and response.

---

## User Consumption Model

### The Vision: Single Landing Page, AI-Powered

Srinivas articulates the user consumption model as the central design target for the engagement. The current state is fragmented: users ask questions in WebEx spaces, email individuals, look in multiple places for pipeline status. The target state is unified:

"We need to look from user point of view to say how do we expose [the] system so that it is very easy for them as a single landing page, not like go multiple places for the same information or bits and pieces of information."

The user experience target: "If a user has a question, he should be [able to] leverage AI to ask a question and doesn't have to talk to any human being in the world. He should be only talking to the system."

Example user queries: "Where is my PR? How is it stuck? How do I unblock it? Can you unblock it?"

The consumption model is the **organizing principle** for the entire engagement. Backend systems (databases, MCPs, tool calls) exist to serve this model. Srinivas: "Once we know what is the user consumption model, now we need to go and find out what are the typical problems that the teams are facing today."

### Two Modes: Self-Serve and Agentic

The consumption model has two modes that coexist:

**Self-Serve Mode:**
- User goes to the DeepSight application
- Asks a natural-language question
- Gets an answer derived from backend data sources (via MCPs and tool calls)
- No automation beyond the query-response cycle
- Eliminates support burden: "So that way we eliminate support issues from the team"

**Agentic Mode:**
- System proactively identifies issues and takes action
- Guides the user through next steps with approval: "I'm taking this next step, is it OK?"
- Chains operations together (detect failure, identify cause, alert engineer, propose rollback)
- Operates with human-in-the-loop for complex actions

Srinivas is emphatic that both modes must coexist, and the choice belongs to the user: "Depending on the user behavior, they can pick one or the other way. Let the user figure it out what they want. We don't have to dictate."

### The Pipeline North Star

Srinivas frames the ultimate goal in terms of the developer experience: "If I raise a PR with minimum disruption, assuming the engineer has done the right job, the entire PR should get merged as fast as it can. And we will do whatever is needed to make that happen."

This is the success metric for the consumption model: time from PR submission to merge, with AI eliminating every friction point in between.

---

## WebEx Space Issue Mining: The Starting Point

Srinivas defines the first concrete task for BayOne: mining the NX-OS CI workflow WebEx space for user issues.

### What the WebEx Space Is

There is a WebEx space called the "NX-OS CI workflow" (or similar name) where engineers ask CI/CD-related questions and get support from Divakar's team and Anupma's team. Divakar confirms: "We have a WebEx space and people usually ask questions over there and we pick up that one. And we take it from there."

This space contains 6-8 months of accumulated user questions, issues, and support interactions: "This is a culmination of all the user requests putting there for the past, let's say, six to eight months."

### The Task

1. Get added to the WebEx space (Srinivas will add Colin)
2. Download the entire chat content using the WebEx API (Srinivas: "There's a WebEx [API]. It's a very simple thing. Within one hour you can get a plugin.")
3. Use AI to summarize the issues, rank them by severity and prioritization
4. Produce a categorized list of the top user pain points

Srinivas says this gives them "80% of the issues that the users are facing" as a starting point. Email-based requests are the remaining 20% and would be crunched separately.

### Naga's Existing Work

Srinivas mentions that an engineer named **Naga** may have already built a WebEx scraping tool: "I think Naga already has created, I think. You can reach out to him or I'll connect with you." He is uncertain whether the code was committed: "We already have it, but I don't know that we committed it because we did so many [iterations] in the last few months."

Colin should start with whatever Naga has, extend it if needed, and build from there rather than starting from scratch.

### Two WebEx Plugins Requested

Srinivas requests two reusable plugins (not single-use scripts):

1. **Meeting recording summarizer:** Given a WebEx recording, dump the recording, get the transcript, summarize it, and extract action items. Prompt-seeded so behavior changes based on the use case.

2. **WebEx space issue extractor:** Given a WebEx space, download all content and produce a categorized summary of issues. Also prompt-seeded.

Srinivas emphasizes reusability: "When we give a job to you, don't assume that it will be only used for CI/CD. It will take your help to create plugins in a way that can be consumed in other platforms."

### Colin's Upstream Extension

Colin offers something beyond what Srinivas described: automated GitHub issue creation from the extracted issues, connected to an agentic workflow where simple issues are resolved automatically and complex issues get human oversight.

Srinivas accepts the vision but defers the implementation: "You're thinking the same way what I'm thinking. But I want you to get started somewhere."

He does confirm the eventual need for a persistent, continuously monitored pipeline: "You need to have a way to continuously monitor it and extract it and put it in a separate database so that you de-[duplicate] also... So eventually, it'll become like a question and answer kind of thing, a FAQ equivalent."

The FAQ-equivalent system would have two tiers:
- **Static answers:** Some questions always have the same answer
- **Dynamic answers:** Some questions require probing a database with AI

---

## Airflow: Confirmed as Preferred Orchestration

### The Exchange

Colin suggests Airflow for the continuous monitoring pipeline: "My suggestion would be Airflow. If we can do things with Airflow, especially for things like this, where it's continuous monitoring."

Srinivas's response is immediate and enthusiastic: "Airflow, yeah, we are using Airflow. So, yeah, we love Airflow. Yeah, that is easy to manage and also easy to deploy in so many other ways."

### Existing Infrastructure vs. Standalone POC

Colin offers to stand up a standalone Airflow instance: "We can even do our own even POC like standalone Airflow instance just with Docker or Podman or something, or if there's an existing one that you want us to tack on to, we can do that too."

Srinivas rejects the standalone approach in favor of using existing infrastructure: "We have it already. Some of the Airflow [DAGs] already established. So I don't want to create yet another parallel and monitor that."

Colin agrees: "So we'll just leverage what we have."

This resolves an open question from Sets 06 and 09. Set 06 noted Airflow as controlled by a separate team with Divakar saying "I need to get in touch with another team." Set 09 identified finding the Airflow SME as an open discovery item. Now Srinivas confirms: Airflow is available, DAGs already exist, and BayOne should use the existing Airflow infrastructure rather than building a parallel instance.

### Implications for the Engagement

The Airflow confirmation means the continuous monitoring pipeline (WebEx space scraping, issue extraction, deduplication, categorization) can be implemented as Airflow DAGs deployed to Cisco's existing Airflow infrastructure. This avoids the infrastructure provisioning delay that a standalone instance would require, and it meets Srinivas's principle of not creating parallel infrastructure to monitor.

---

## Organizational Boundaries: DevEx and Data Center

### The Shared Ownership Model

Srinivas explains the organizational structure for the audience (particularly for the IT person helping with the Duo/MFA issue who needed context):

- **Divakar's team (Data Center / "the worker"):** Owns most of the CI pipeline. Srinivas: "The worker owns some part of it, or most part of it."
- **Anupma's team (DevEx):** "A sister organization" that provides build infrastructure and services for the business unit. Owns some CI pipeline components and the CAT-related databases.
- **Recent transfer:** Some functions recently moved from DevEx to Divakar's team: "Some of the functions got transferred to the worker's team from Anupma's organization."
- **Result:** Shared responsibility. "The CI pipeline, from the developer point of view, is co-owned by the worker, that means our team, data center team, and Anupma's team, which is the DevEx team."

### What This Means for MCP Access

The shared ownership creates a practical problem for MCP creation. The CAT-related databases live with Anupma's DevEx team. Srinivas can direct Justin's build team to expose their MySQL data and build MCPs directly. But for Anupma's data, there are "people issues and organization boundaries" that require negotiation.

Srinivas's approach: pull Anupma into the discussions, negotiate access, and if APIs are sufficient, use them; if not, get database access directly. Either way, the data must be exposed.

---

## BayOne Team Discussion

### Team Composition Shared

Colin describes the team structure to Srinivas:
- **Two onshore (San Jose):** Full-time on the project, available in the office any day, both live within 15 minutes of Cisco's campus. One specializes in large-scale agentic operations and Airflow. The other specializes in MCP, LangGraph, and integrations.
- **Two offshore (India):** Working PST hours.
- **Colin:** Director-level, based in Pittsburgh.

Srinivas asks Colin to share resumes for the two onshore engineers: "Just send me the resume and I want to understand their strengths."

### Srinivas's Utilization Expectation

Srinivas is explicit about not wanting idle time: "I don't want them to be idle. Either they do this project or some other project." He envisions cross-pollination -- when the CI/CD project is blocked waiting for another organization's input, he wants to redirect BayOne engineers to other DeepSight work: "A lot of work on the DeepSight also. So much stuff to be done. And probably we'll take your help there also."

Colin reciprocates: "Even for us, I won't let them be idle."

### Meeting Cadence

Srinivas proposes this sync-up meeting twice a week with the same audience, pulling in additional people as the project accelerates. He wants Colin's engineers to attend as well: "So that way we get to interact with them and build some rapport."

---

## GitHub Access Blocker: Duo MFA Issue

Colin demonstrates the GitHub access blocker by sharing his screen. The problem:

1. VPN is connected and working
2. Single sign-on (SSO) works and redirects to Duo
3. Duo authenticates via phone push notification
4. The system then requires adding a second authentication device
5. The only option offered is a **physical security key** (FIDO key, USB hardware token)
6. Colin does not have a physical security key
7. The system will not offer alternative MFA options (Touch ID, backup codes, etc.)
8. This creates an infinite loop: authenticate with Duo, get told to add a device, only option is physical key, no key available, start over

Srinivas and Anupma suggest:
- Raising an IT case ("raise an [IT] case")
- Calling IT support directly: "There's a number, they give you one and then you can [call]"
- The VPN is working, so IT should be able to resolve the downstream Duo configuration

This is the primary blocker for the entire BayOne engagement. Without GitHub Enterprise access, the team cannot access source code, DeepSight repositories, or any code-dependent workflows. Srinivas acknowledges this: Colin notes it is "the most gating factor for us right now. Because essentially, that is the [prerequisite for] everything."

---

## Srinivas's Engagement Philosophy (Reiterated and Expanded)

Several of Srinivas's operating principles from Set 06 are reinforced and expanded in this meeting:

### Outcomes First, Systems Second

Srinivas: "First I want to get the problem statement right, because when we go to Anand, I want to make sure that Anand is also comfortable on the problem that we are trying to solve. So first we want to get the outcomes. That's why I said I started with outcomes. I want to define what the outcome should be, high level, and then backend systems can change."

### Reusable Pieces, Not Pointed Solutions

Srinivas: "I want to develop these pieces that can be leveraged anywhere else. And we have a huge roadmap in mind. So I want to leverage your team to build some of these pieces of puzzles, so that we can automate the end-to-end [pipeline]."

This reiterates the Set 06 principle: do not build pointed solutions. Build reusable infrastructure components. The WebEx plugins, the Airflow pipeline, the MCPs -- all are intended to serve the CI/CD use case first but be deployable across other DeepSight applications.

### Understand Before Design

Srinivas: "Understanding is important before [you start], because if you don't understand [and] I say Colin let's do it, you don't know why we are doing this, it does not make sense. But if you also know the [build] artifacts, then we can do a better judgment."

He makes this a gating requirement: no design until Colin has met with Justin and understands the build log structure, the build process, and the engineer's daily workflow.

---

## Key Deltas from Prior Sets

| Topic | Prior Understanding | Updated Understanding |
|-------|--------------------|-----------------------|
| **Databases** | MySQL + MongoDB (Set 06) | MySQL (Justin, build data) + Cassandra (Anupma, CAT data) + MongoDB (raw pipeline) + NFS (build logs) |
| **Existing MCPs** | None known | Justin's team has a basic MCP on MySQL (QA rate, build status, sanity results) |
| **Call graph** | Not previously discussed | CLAM/LAM system generates function-level call graphs at compile time; two approaches (baseline + dynamic) being built |
| **CRFT** | Not previously discussed | Separate runtime instrumentation tool that runs on the NX-OS switch; independent from call graph |
| **Airflow** | Separate team controls it (Set 06); discovery needed (Set 09) | Confirmed available, existing DAGs, Srinivas enthusiastic; use existing infrastructure, not standalone |
| **Build logs** | Jenkins logs, no Splunk access (Set 06) | NFS storage, 3-5 day retention, two build types (official/user), same log format, real-time processing required |
| **Inference cost** | Not previously discussed | Explicit 4X cost increase flagged; brute-force log analysis explicitly prohibited |
| **DevEx boundary** | Not previously discussed in detail | Anupma's team controls CAT databases (Cassandra), APIs exist but DB not exposed, organizational friction acknowledged |
| **Justin** | Not previously identified | Build infrastructure engineer, owns MySQL database, has existing AI fix-suggestion tools, building MCPs |
| **Consumption model** | Self-serve mentioned (Set 06) | Formally defined: self-serve + agentic, single landing page, both modes coexist, user chooses |

---

## Open Questions After This Meeting

1. **What does the build log structure look like?** Srinivas explicitly says this must be answered before any design. Requires meetings with Justin.
2. **What is the typical log size** for an official build vs. a user build?
3. **What tool calls does Justin's existing MCP support?** Only high-level descriptions given (QA rate, build status, sanity results). Need the full tool call inventory.
4. **What APIs does Anupma's team expose for CAT data?** She deferred to offline discussion.
5. **What is the Cassandra schema for CAT data?** Type confirmed, structure unknown.
6. **Where is Naga's WebEx scraping code?** May or may not be committed. Colin needs to find Naga and assess.
7. **What does Mazar's dynamic call graph script look like?** Srinivas says Mazar is working on it, but no details on status or timeline.
8. **How do the existing Airflow DAGs work?** Confirmed as available, but no detail on what DAGs exist, where they run, or who manages them.
9. **What is the call graph baseline database schema?** Justin and Mazar are assigned to create it, but no design exists yet.

---

## Action Items Extracted from Meeting

| Owner | Action | Dependency |
|-------|--------|------------|
| **Colin** | Raise IT case for Duo/MFA issue blocking GitHub access | None |
| **Colin** | Send resumes of two onshore engineers to Srinivas | None |
| **Colin** | Contact Naga re: existing WebEx scraping tool | Srinivas to connect via email or WebEx |
| **Colin** | Build two WebEx plugins (recording summarizer, space issue extractor) | Access to WebEx space; Naga's existing code |
| **Colin** | Meet with Justin (1-2 sessions) to understand build log structure | GitHub access preferred but not strictly required |
| **Colin** | Download NX-OS CI workflow WebEx space content and produce categorized issue list | Access to WebEx space |
| **Justin + Mazar (+ Tim)** | Create baseline call graph database from nightly build | CLAM/LAM system access |
| **Mazar** | Create dynamic call graph generation script for new code/files | CLAM/LAM system access |
| **Anupma** | Discuss database exposure (Cassandra) with her team offline | Organizational approval |
| **Srinivas** | Add Colin to NX-OS CI workflow WebEx space | None |
| **Srinivas** | Connect Colin with Naga | None |
| **Divakar** | Put initial milestone/history document in the WebEx space | None |
