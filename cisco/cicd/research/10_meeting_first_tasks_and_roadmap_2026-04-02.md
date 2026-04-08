# 10 - Meeting: First Tasks and Emerging Roadmap

**Source:** /cisco/cicd/source/srini_team_meet_04-02-2026.txt
**Source Date:** 2026-04-02/03 (CI/CD Track Sync Up)
**Document Set:** 10 (First meeting with Srinivas's full CI/CD team)
**Pass:** Task assignments, access blockers, and roadmap

---

## Context: The Meeting That Changes the Engagement

This is the inflection point. Every prior set in this research library — from the Zahra summary email (Set 01) through Anand's "any update?" (Set 07) through the two internal team briefings where no work had started (Sets 08-09) — documented an engagement that existed entirely in planning, onboarding, and waiting. Set 09's cumulative state table said it plainly: "Deliverable work: Zero."

This meeting ends that. For the first time in the engagement's history, Srinivas assigns concrete tasks to Colin's team, names specific people to work with, and establishes a recurring meeting cadence with the operational team. Work is starting.

The meeting is a Friday team sync — Srinivas's CI/CD track team plus Colin. The first 15-20 minutes are the existing Cisco team discussing ongoing work (call graph generation, code review integration, PR validation) before Colin is brought into the conversation. Colin then demonstrates the GitHub Duo MFA problem on screen share, after which Srinivas provides context on the engagement for Anupma (a DevEx lead engineer who is new to the conversation), and then assigns the first two tasks. Justin provides a build infrastructure overview. The meeting closes with team deployment discussion and Srinivas's direct acknowledgment of the delay.

### Who Is Present

- **Srinivas** — AI platform owner, DeepSight, the engagement's technical sponsor. Runs the meeting.
- **Colin** — BayOne Director of AI. This is his first appearance in a Srinivas-led team meeting (prior meetings were one-on-one or with Anand).
- **Divakar** — CI/CD infrastructure engineer, Srinivas's team. Named as someone who "does a lot of support" on the NXOCI WebEx space. Previously the primary access provisioning contact (Sets 06-07).
- **Justin** — Build infrastructure engineer. Owns the official build database (MySQL), sanity results, and the MCP prototype for build queries. New name — first appearance in this research library.
- **Anupma** — Lead engineer from DevEx (Developer Experience), a Cisco sister organization. Co-owns the CI/CD pipeline with Srinivas's team. Controls some databases and services that the engagement will need access to. Described by Srinivas as someone whose organization "used to provide, even now they provide some services for us." New name — first appearance.
- **Ankit** and **"D"** (likely Deepak or another engineer) — Referenced at the start as asking about PR validation / code review. Part of Srinivas's technical team. Briefly visible but not major participants.
- **Naga** (also rendered as "Nara") — Not present but referenced multiple times. Has potentially existing WebEx scraping code. Srinivas will connect Colin with Naga via email or WebEx.

### Connection to Prior Sets

This meeting answers several open questions from earlier sets:

| Prior Set | Open Question | Answer in Set 10 |
|-----------|--------------|-------------------|
| Set 06 (Feb 17) | Who is the Airflow SME? | Not directly answered, but Srinivas says "we are using Airflow" and existing Airflow DAGs are established. Airflow infrastructure exists; the unknown has shifted from "does it exist?" to "how do we deploy on it?" |
| Set 06 (Feb 17) | What happened to Rui's existing CI/CD app? | Not mentioned. The focus has shifted entirely to the WebEx scraper and build log analysis as starting points. The Rui handoff appears to have been superseded or deferred. |
| Set 07 (Mar 31) | GitHub access still blocked? | Confirmed blocked. Colin demonstrates the Duo MFA infinite loop on screen share. Srinivas directs him to raise an IT case and call the support number. |
| Set 07 (Mar 31) | DeepSight access? | Still pending. Srinivas says "wait for this weekend" — a platform release is happening. Regroup needed. |
| Set 09 (Mar 30) | When will the team interact directly with Cisco engineers? | Now. This meeting is it. Srinivas establishes twice-weekly recurring meetings with the full team. |
| Set 09a (Mar 31) | What is the 2-week plan? | Srinivas defines it: WebEx scraper task, Justin meetings for build log understanding, then define the user consumption model. |

---

## Task 1: WebEx Space Scraper and Issue Extraction

### What Srinivas Wants

Download the entire content of the NXOCI workflow WebEx space, summarize the issues users have been reporting, and rank them by severity and priority. This is explicitly the **starting point** for the engagement — the first concrete task assigned.

Srinivas's exact framing:

> "One starting point, Colin, what you need to do is I will add you to there. What you can do is you can create a simple WebEx [plugin]. I think Naga already has created, I think. You can reach out to him or I'll connect with you. We have a plugin where you can download the entire content of this WebEx space once you are in and then you summarize the issues what the users have been facing so long and you can rank them in the order of severity, prioritization and whatnot."

### Why This Task First

The NXOCI workflow WebEx space is where engineers go when they have CI/CD pipeline problems. It is a running log of user pain points accumulated over the past six to eight months. By scraping and analyzing this content, the team will have a data-driven inventory of what is actually broken or frustrating for users — not what Cisco leadership thinks the problems are, but what engineers are actually complaining about.

Srinivas is explicit about the coverage:

> "This is a culmination of all the user requests putting there for the past, let's say, six to eight months. So email and all, if it is there, that will crunch it separately, but this piece will give us 80% of the issues that the users are facing."

### Technical Approach

- **WebEx API is public.** Srinivas states: "There's a WebEx space API. It's a very simple thing. Within one hour you can get a plugin. You don't have to even ask anyone also. There's a WebEx plugin that Cisco has already published."
- **Naga may have existing code.** Srinivas says Naga already created something similar but is unsure whether it was committed: "We already have it, but I don't know that we committed it because we did so many purposes in the last few months. It should be there, Naga should have it."
- **Srinivas will connect Colin to Naga** via email or WebEx to check whether existing code can be reused.
- **If Naga's code does not exist or is incomplete,** Colin's team builds it from scratch. Srinivas characterizes this as trivial: "These things are very simple things. They should be pretty fast."

### Reuse Requirement

Srinivas is emphatic that this must not be a one-off tool:

> "When we give a job to you, don't assume that it will be only used for CI/CD. It will take your help to create plugins in a way that can be consumed in other platforms."

And Colin confirms he already understands this pattern from Set 06's "two hats" framework:

> "That was the day when I was telling you also when we got started on this first meeting, if you remember."

The WebEx scraper must be designed as a general-purpose tool: given any WebEx space, download the content and run summarization/categorization against it. The prompt is the only thing that changes between use cases.

### Colin's Response: We Have This Already

Colin reveals that BayOne already has internal automation for a similar workflow:

> "My team will have meetings just like this. And it's kind of the equivalent of the issues chat like that. So we have the automation actually go and create even GitHub issues automatically. That goes downstream to a much more involved workflow that's agentic."

He describes their internal system: meetings generate transcripts, transcripts generate issues, simple issues get resolved automatically, complex ones require human oversight at the plan level. He asks whether Srinivas wants similar persistence and downstream processing.

Srinivas's answer is yes, but phased:

> "They'll be adding new questions, new set of issues, so many things, right? So you need to have a way to continuously monitor it and extract it and put it in a separate database so that you de-dupe also... eventually, we need to, it'll become like a question and answer kind of thing, a FAQ equivalent."

### The Full Vision Behind the Task

What starts as "scrape a WebEx space" evolves during the conversation into a continuous monitoring pipeline:

1. **Initial scrape:** Download all historical content, summarize issues, rank by severity/priority.
2. **Continuous monitoring:** Ongoing extraction of new issues as they are posted.
3. **De-duplication:** Same question asked multiple times by different users should collapse into a single issue.
4. **Categorization:** Issues categorized for downstream consumption by different pipeline components.
5. **FAQ generation:** Static answers for recurring questions. Dynamic answers (requiring database queries and AI) for others.
6. **Airflow orchestration:** Srinivas confirms they use Airflow and that this pipeline should use it. Colin suggests Airflow; Srinivas agrees: "We are using Airflow. So, yeah, we love Airflow."
7. **Existing Airflow infrastructure:** Srinivas confirms existing Airflow DAGs are already established: "We have it already, some of the Airflow DAGs already established. I don't want to create yet another parallel and monitor that."

Colin tells Srinivas: "We'll surprise you. That's my goal." Srinivas replies: "But yeah, that's what we have in mind. And we have created a bunch of pipelines like that behind the scenes right now. But you're right. You're thinking the same way what I'm thinking. But I want you to get started somewhere."

### Airflow Deployment Decision

The question of where to deploy the Airflow pipeline is resolved in the meeting:

- **Colin's offer:** "We can even do our own POC like standalone Airflow instance just with Docker or Podman or something, or if there's an existing one that you want us to tack on to."
- **Srinivas's answer:** Use the existing infrastructure. "I don't want to create yet another parallel and monitor that. We'll just leverage what we have."

This means the BayOne team will deploy their DAGs into Cisco's existing Airflow instance, not spin up an isolated environment. This requires Airflow access — another access item to track.

---

## Task 2: Meeting Recording Transcriber and Summarizer

### What Srinivas Wants

A second plugin that takes WebEx meeting recordings, downloads them, generates transcripts, summarizes the content, and extracts action items. This is the companion tool to the WebEx space scraper.

Srinivas's framing:

> "As a part of WebEx, we also have a plugin to take the recording, that is recording, and dump the notes and summarize it."

Then explicitly:

> "I'll first come up with you now. If it is, if [Naga] has committed the code, we'll take it up from there. Otherwise, we wanted to create two plugins. One is, given a [WebEx recording], I want you to be able to dump the recording, get the transcripts, summarize it, and extract the action items. Depending on the prompt, it will do the job."

### Prompt-Driven, Reusable

Both plugins are seeded with prompts that determine their behavior for each use case:

> "Both will be seeded with the prompt, and that prompt can be changed depending on what use case."

The prompt is the configuration layer. The infrastructure (download, transcribe, parse) is the reusable layer. This matches the "two hats" framework from Set 06: solve the current need (CI/CD meeting summarization) while building infrastructure that works for any meeting, any team, any platform.

### Colin's Response

Colin asks a targeted question about scope:

> "Is that something where you want to persist this so you can do Q&A on it, keep some track, even after the initial push?"

This is Colin probing whether the transcription should feed into a durable knowledge base (consistent with the agentic workflow he described from BayOne's internal tooling) or whether it is a fire-and-forget summarization. Srinivas's answer is the same continuous monitoring model he described for the WebEx scraper — persistent storage, de-duplication, and downstream consumption.

---

## Task 3: Build Log Structure Understanding (Justin Meetings)

### What Srinivas Assigns

Meet with Justin one to two times. Understand the complete build infrastructure: official builds versus user builds, log file format and structure, typical log size, failure types, existing tools, and how an engineer experiences a build failure.

Srinivas's directive:

> "Please have one call with Justin and have a report and say, you know exactly what the structure of a log will look like. And then you understand the pieces of it and how to invoke a build like that manually on your setup. Basically, understand [the engineer's] life. If I'm an engineer, how do I build it? Where do I see the log? What the build will look like? What a failure really means? Just understand the structure, some parts from Justin."

> "Even if you do a couple of meetings with Justin, it will not harm. Because you get the full view from him."

### Why This Is Prerequisite

Srinivas explicitly states that understanding must come before design:

> "Understanding is important before I [assign work] because if you don't understand... it does not make sense. But if you also know the actual artifacts then we can do a better judgment."

> "Then after that, we'll step back and say what the design should look like and move forward. So we'll be in line with you when you're designing so that we don't waste time and make the right decision."

This is Srinivas preventing a failure mode he clearly expects: an outside team jumping to implementation without understanding the domain. He wants Colin to have enough context to participate meaningfully in design discussions, not just execute instructions.

### What Justin Reveals About Build Infrastructure

Justin provides a compressed overview during the meeting:

**Databases:**
- **MySQL** for official builds. Tracks every trigger, status (pass/fail), and other metadata.
- Sanity results also go to databases and can be queried through the existing MCP.

**MCP Prototype:**
- Justin's team has an MCP that supports basic queries: latest QA-turning rate, most recent build, sanity results.
- This is the existing starting point that Colin's team may extend.

**Logs:**
- Build logs go to an **NFS location**, not a database.
- Logs are "huge" — Srinivas and Justin both flag this.
- Retention policy: 3-5 days, then the space is reclaimed.
- Logs are consumed by engineers and by the sanity system (integers/integrations).

**Existing Tooling:**
- Justin's team has parsing tools: "We already have like [something] where we parse, you know, the important [parts]. The logs are sometimes [very large]. So, figuring out and drilling down, so we have some tools."
- AI-assisted fix suggestions exist: "We have some things where we can even use AI and it comes up with like a decent fix basically."
- **Gap:** No existing tooling for identifying which commit caused a build failure. Justin states directly: "I don't think we have anything for finding which commit caused the build. We haven't done that yet."

**Two Problem Types:**
- **Official (nightly) builds:** Accumulate all commits from ~1000 engineers for the day. Build failures require identifying which PR(s) caused the break, then deciding whether to back out the PR or take other action.
- **User (PR) builds:** Individual engineer's PR triggers a build. Failures are caused by that specific PR's changes.
- Srinivas frames these as the same underlying problem: "It is a single problem. One is more than one PR, same build. One single PR, same build. But log file is same."

### Inference Cost Constraint

Justin raises a critical operational constraint:

> "Whatever we do, the inference costs are going higher. The products has already increased by 4X."

Srinivas reinforces this as a non-negotiable engineering requirement:

> "I don't want to throw a big log and say, what is it? One of my screening questions for these interviews for the team is exactly that. I screened you on the same question on the first day."

This is a direct callback to Colin's first conversation with Srinivas, where Srinivas tested Colin's approach to large-scale log analysis. The requirement is clear: do not naively feed entire build logs to an LLM (Large Language Model). The solution must be engineered to parse, filter, and structure logs before invoking AI, keeping inference costs manageable.

Colin confirms he understands: "So I'm telling you know my requirements are right, you can solve a problem in many ways but the question is solve the problem in a right engineering way."

### Colin's Approach

Colin proposes real-time processing with structured extraction:

> "Even from the logs, the moment we have something, we'll be able to immediately test out some things within probably a day. So we'll be able to give some early [results]."

And on the log retention problem:

> "Even if they disappear after some time, and there's a constant refresh of them, essentially, we can still distill them down after we extract the content out, get it in structured format, preserve that for some time historically."

Srinivas confirms real-time is the requirement: "We will have to do it in the real time, right? They will fail, analyze, get the data."

---

## Task 4: Colin to Share On-Site Team Profiles

Srinivas requests profiles/resumes for the two on-site BayOne team members:

> "Can you share their profiles of these two guys at San Jose?"

> "Just send me the resume and I want to understand their strengths and then probably, how do we pull them in?"

Colin describes the two on-site people:
- **Person 1:** Expert in large-scale agentic operations and Airflow.
- **Person 2:** Expert in MCP, LangGraph, and integrations.

Srinivas wants to understand their strengths before assigning work. This is the first time Srinivas has directly requested information about the broader team — in all prior meetings, the conversation was exclusively between Srinivas and Colin.

---

## Access Blockers: Updated Status

### Blocker 1: GitHub Duo MFA Infinite Loop

**Status:** Still blocked. Demonstrated on screen share in this meeting.

Colin demonstrated the problem live. The sequence:
1. Click the GitHub Enterprise link Divakar provided.
2. Single sign-on page appears. Click login.
3. Duo MFA screen appears.
4. Touch ID is set up on the laptop.
5. When trying to add a new MFA method, the only option offered is a physical security key (FIDO/USB device).
6. No option to add a different MFA method (phone push, Touch ID, etc.).
7. System loops infinitely between authentication and the "add a device" screen.

**Discussion during demo:**
- Another participant says they have a physical security key device that plugs into the laptop. Srinivas says he has one too. But both note that it works for them even without the key.
- Srinivas's resolution: "I think you should raise an IT case. You can call them. There's a number, they give you one and then you can use that one and they'll go and contact you all the way back because your [VPN] is working."

**Assessment:** This is the same blocker documented in Set 07 (Mar 25-31) and Set 09 (Mar 30). It has now been demonstrated visually to the Cisco team for the first time. The resolution path (IT case + phone call) is concrete but depends on Cisco IT responsiveness, which has historically been slow (Set 06: "no set procedure," "sometimes we wait some approval").

### Blocker 2: DeepSight Access

**Status:** Pending. Requires GitHub first, plus a platform release happening this weekend.

Srinivas says: "Wait for this weekend. We are releasing. I think we need to regroup one more time and define the milestones as well as what we want to achieve and what we want to automate."

DeepSight access is now explicitly deferred until after the current platform release. This is a soft block — the WebEx scraper and Justin meetings can proceed without it.

### Blocker 3: Code Base Access

**Status:** Pending. Anupma identified as the person who can help.

Srinivas at the close: "Talk to Anupma to get the next code base access. She's the one who helps us and then we'll take it from there."

Anupma's team (DevEx) co-owns the CI/CD pipeline. Her databases and services are currently "not exposed" — she states: "We have the API but the database is not exposed and I'll have to discuss." Srinivas acknowledges there may be "some people issues and organization issues" but insists access must happen: "We need access to the work. Basically, the DB."

This is a new dynamic not visible in earlier sets. The cross-organizational boundary between Srinivas's Data Center team and Anupma's DevEx team introduces a political dimension to database access. Srinivas handles it with a combination of directness and diplomacy: "I know there may be some reservations may be there, but we'll chat."

### Blocker 4: Anupma's Databases

**Status:** Discovery phase. Databases not yet cataloged.

Srinivas asks Anupma directly in the meeting: "How many databases are there behind the scene and what kind of database do we have?"

Anupma's response is guarded: "The database is not exposed and I'll have to discuss. I can share more details offline."

Srinivas identifies two paths: either use existing APIs that Anupma's team exposes, or get direct database access so BayOne can build their own integrations. He states the bottom line: "Two ways. The APIs can help us or if the APIs don't help, they need to expose the database and we'll create our own stuff."

Justin adds that his team uses MySQL for build data, and mentions Cassandra as another database in the ecosystem. Anupma says she will discuss exposure options offline.

---

## The Emerging Roadmap

### Srinivas's Method: Outcomes First

Srinivas is explicit that he does not want to jump to implementation:

> "First we need to define what we want to achieve. As we said, high level, one is from the user point of view, what we want to solve for the user, which is anything with respect to the pipeline, any question, they should have a single place where they go and it's like a self-service AI."

> "I'm not really worried. First I want to get the problem statement right, because when we go to Anand, I want to make sure that Anand is also comfortable on the problem that we are trying to solve. So first we want to get the outcomes. That's why I said I started with outcomes. I want to define what the outcome should be, high level, and then back end systems can change."

This is Srinivas managing the engagement relationship with Anand: he wants to present Anand with clearly defined outcomes that the team is pursuing, not a list of technologies being built. The outcomes justify the investment; the technology choices follow.

### Phase 1: Understand the Problem (Current)

Two parallel tracks:

**Track A — User Pain Points (WebEx Scraper)**
- Scrape the NXOCI workflow WebEx space.
- Summarize issues, rank by severity/priority.
- Identify patterns: what are users actually struggling with?
- This gives the team a data-driven starting point for defining the user-facing solution.

**Track B — Build Infrastructure Understanding (Justin Meetings)**
- Meet with Justin 1-2 times.
- Understand official vs. user builds, log structure, failure types, existing tools.
- Understand the MCP Justin's team already has.
- Produce a report on build log anatomy and existing capabilities.

### Phase 2: Define the User Consumption Model

Srinivas describes two modes:

> "We need to define what that consumption model should look like as a user point of view, both agentic and non-agentic mode."

**Self-serve mode:** User has a question, goes to the application, gets an answer. No human interaction needed. Example: "Where is my PR? How is it stuck? How do I unblock it? Can you unblock it?"

**Agentic mode:** The system proactively monitors, detects issues, and either resolves them automatically or presents a plan for approval. Example: build failure detected, AI identifies the problematic commit, sends a notification to the engineer, suggests a rollback.

> "Whether he go to the system, or system will guide him saying that, 'I'm taking this next step, is it OK?' Kind of thing. Both ways. Depending on the user behavior, they can pick one or the other. Let the user figure it out what they want. We don't have to dictate. That system has to do both ways."

### Phase 3: Map Tool Calls to User Needs

Once the user consumption model is defined and the existing data sources are cataloged:

1. **Inventory existing MCPs and tool calls.** Justin has a basic MCP. Anupma's team may have APIs. Others may exist.
2. **Evaluate existing tool calls against user needs.** Does what exists already solve any of the identified issues? Where are the gaps?
3. **Build missing MCPs or extend existing ones.** If an MCP exists, add tool calls. If not, create MCPs from the database sources.
4. **Design for both overlay modes.** Every MCP/tool call must support both user-driven (self-serve) and agentic workflows. Srinivas: "When we design these tool calls for the MCPs, we need to make sure that both these things are overlayed together. Because this is an overlay functionality on top of the backend data services."
5. **Choose static vs. AI-generated tool calls.** Srinivas identifies a design decision: "One is we statically create these tool calls or use AI to basically create generic tools so that we enable agentic workflow."

### Phase 4: Deployment and Integration

Not discussed in detail in this meeting, but implied:
- Deploy on DeepSight platform.
- Integrate with existing Airflow infrastructure.
- Follow DeepSight look-and-feel and SDK conventions (per Set 06).

---

## Team Deployment

### BayOne On-Site Resources

Colin offers two people based in San Jose, available full-time:

> "Two I'm sure that are accessible to you any time. The moment you tell them to be in the office, they're in the office. They're all based in San Jose, right near Cisco's campus. Both of them live within 15 minutes."

He also mentions two offshore team members working PST hours.

Srinivas asks pointed questions:

> "So these team members who are in San Jose, they are full-time for this project?"

Colin confirms: "Full-time for this project, yes."

> "Can they be with us in the office?"

Colin confirms: "Yes, yes. As soon as any days that you want them in the office, they can be there 40 hours a week in the office if you want them. Or if you want them like every Tuesday, I know everyone's in the office on Tuesdays."

Srinivas then asks for profiles:

> "Can you share their profiles of these two guys at San Jose? I also want to understand their strengths and weaknesses."

Colin describes their specialties:
- **Person 1:** "Expert for large-scale agentic operations and Airflow."
- **Person 2:** "MCP, LangGraph, any kind of integrations."

These map to the two named on-site team members from Set 09: Srikar (Bay Area, AI engineer) and Namita (expected week of April 6, Airflow expert). The descriptions align — Namita's Airflow expertise and Srikar's AI/integration background.

### Srinivas Wants Rapport with the Full Team

> "If you are required, you can get your other engineers also. So that way we get to interact with them and build some rapport."

This is Srinivas implementing the "colleague" model from Set 06. He does not want Colin as a single intermediary — he wants direct relationships with the engineers who will do the work.

### The Idle Prevention Clause

Srinivas is direct about utilization:

> "I don't want them to be idle. Either they do this project or some other project. I don't want them to be idle because, yeah, you know, I mean, we run very fast. So sometimes we may be waiting for some information on some project. Let's say we have waiting on some other organization to bring some information. I don't want to lose a day or two, right? I mean, just waiting. So if you can assign, if they are working with us in line, then we'll say, 'Hey, can you do this job?' Something like that."

This is significant for the engagement economics. If BayOne's team is blocked on CI/CD items (access, database exposure, dependencies on other organizations), Srinivas will redirect them to DeepSight work rather than let them sit idle. He makes this explicit:

> "A lot of work on the DeepSight side also. So much stuff to be done. And probably we'll take your help there also."

Colin agrees: "Even for us where I won't let them be idle, I'll say that."

This means the BayOne team's utilization is protected regardless of CI/CD blockers. If access issues stall the CI/CD work, the hours still get billed against DeepSight tasks. This is operationally ideal for BayOne and resolves the idle-time risk that has been implicit since Set 08 (when the team was briefed but had nothing to do).

---

## Srinivas's Stance on the Delay

Srinivas addresses the elephant in the room:

> "I felt bad. I'll be honest with you. I know it's April now."

Colin responds: "I want you to know we're eager to make up for any missed time that we had from the procurement side."

Srinivas:

> "I mean, we were hoping that you guys will come onboard months early, but it's OK. It is what it is. But I think we should move fast now that you guys have [hardware]. Just work with the IT team, get the laptop, other issues resolved. Then talk to Anupma to get the next code base access. She's the one who helps us and then we'll take it from there."

### Tone Assessment

Srinivas is **understanding but firm**:

- **Understanding:** "It is what it is." He does not assign blame for the procurement delay, the hardware delays, or the access blockers. He accepts the situation.
- **Firm:** "We should move fast now." The grace period is over. Hardware is in hand. The team is on the call. There are no more structural excuses.
- **Honest about disappointment:** "I felt bad" and "months early" reveal that this delay has cost the team. The existing CI/CD team (Divakar, Justin) has been working without the AI augmentation that was supposed to arrive in Q1.

This matches the pattern from Set 07 — Anand's March 31 "any update on this?" was the executive version of the same sentiment. The Cisco side has been patient but the patience has a limit, and that limit is now.

---

## Meeting Cadence Established

Srinivas establishes a recurring structure:

> "I want to have all of us to be there. I'll make it a recorded meeting maybe twice, I mean two times in a week. Same set of audience."

**Twice-weekly recurring meetings** with the full CI/CD track team (Srinivas, Divakar, Justin, Anupma, Colin, and BayOne engineers as they are introduced). Additional people to be pulled in as work advances.

This is a dramatic escalation from the prior meeting cadence. Before this meeting, the only recurring touchpoint was whatever Colin could arrange with individual Cisco contacts. Now there is a standing, recorded, twice-weekly meeting with the operational team. This is the structural change that makes sustained progress possible.

---

## Pre-Meeting Discussion: Existing Cisco Work (Not Assigned to BayOne)

The first 15-20 minutes of the meeting, before Colin's access demonstration, cover work already underway within Srinivas's team. This is not assigned to BayOne but provides important context for what the team will eventually integrate with.

### Call Graph Generation

Srinivas describes a project to generate call graphs for the NX-OS codebase:

- **Purpose:** Given a function change in a PR, determine the impact — who calls it, who it calls, what breaks.
- **Source:** The CLAM system can generate call graphs from compiled code. This is a compile-time option, not a runtime analysis.
- **Two baselines needed:**
  1. **Static baseline:** Generated from nightly builds. Equivalent of a "Cisco DB" — a precomputed call graph of the full codebase.
  2. **Dynamic baseline:** For new files/functions not in the nightly build, a separate script dynamically generates the call graph for just the new code.
- **Justin's role:** Work with Mazar and Tim to create the call graph database from the CLAM system.
- **Relationship to CRFT:** CRFT runs on the switch itself and tracks which functions are invoked at runtime. Call graphs are static analysis (compile-time). They are independent but complementary.

### Code Review Integration

Srinivas describes a two-tier code review approach:
- **IDE level (VS Code):** "Shallow" review. Catches basic mistakes. Runs in the developer workflow.
- **CI pipeline level:** "Very extensive, very deep dive" with knowledge graph, NX-OS domain knowledge, and other context. Runs in the PR workflow.

Both are in the developer workflow and CI workflow respectively. Even XR (another Cisco platform) is doing both. Each has different metrics and dashboards.

This maps to what Colin discussed in Set 09 — the copilot quality concern and the competing internal AI code review team. The "shallow" IDE review is the Copilot-equivalent. The deep CI pipeline review is what BayOne may eventually own or extend.

---

## Anupma's Introduction and the DevEx Relationship

Srinivas provides the most complete explanation of the DevEx organizational relationship in the engagement to date. This is context he delivers for Anupma's benefit, but it is the clearest articulation of the cross-org dynamic.

### DevEx's Role

> "Anupma is a lead engineer from the DevEx side of the story. DevEx is an organization which actually used to provide, even now they provide some services for us. Think of it like our Cisco sister organization and they provide all the build and what are the infrastructure needs for the business unit."

DevEx provides build infrastructure services to Srinivas's Data Center team. Some functions have been transferred from DevEx to Srinivas's team, but ownership is shared:

> "Divakar and Anupma worked closely and now some of the functions got transferred to Divakar's team from Anupma's organization. So Divakar owns some part of it, or most part of it, and Anupma's team owns some part of it. It's like a shared responsibility."

### The CI/CD Pipeline Is Co-Owned

> "The CI pipeline, from the developer point of view, is co-owned by Divakar, that means our team, Data Center team, and Anupma's team, which is the DevEx team."

This means any work BayOne does on the CI/CD pipeline will touch systems owned by two different Cisco organizations. Access, database exposure, and MCP creation will require cooperation from both. Srinivas is positioning this meeting as the venue where both organizations coordinate.

### Anupma's Databases Are the Unknown

When Srinivas asks about databases, Anupma is cautious:

> "The database is not exposed and I'll have to discuss. I can share more details offline."

Justin offers more specifics about his side (MySQL for builds, NFS for logs), but the DevEx-controlled databases remain opaque. Srinivas pushes:

> "We need to unblock for the end of the [engagement]. We can take our own [approach] and we can have... whatever is needed, but we need to get the data exposed."

He acknowledges the political dimension but does not back down: "I know there have been people issues, coordination boundaries, so many things, but we'll chat."

---

## Action Items From This Meeting

| # | Action | Owner | Deadline/Urgency |
|---|--------|-------|-----------------|
| 1 | Raise IT case for GitHub Duo MFA infinite loop; call support number | Colin | Immediate |
| 2 | Connect Colin with Naga re: existing WebEx scraper code | Srinivas | Immediate (email/WebEx) |
| 3 | Add Colin to the NXOCI workflow WebEx space | Srinivas/Divakar | Immediate |
| 4 | Build WebEx space scraper plugin: download content, summarize issues, rank by severity/priority | Colin's team | First task — "should be pretty fast" |
| 5 | Build meeting recording transcriber plugin: download recordings, get transcripts, summarize, extract action items | Colin's team | Concurrent with #4 |
| 6 | Design both plugins for reuse across platforms (not CI/CD specific) | Colin's team | Built into #4 and #5 |
| 7 | Schedule 1-2 meetings with Justin to understand build log structure, official vs. user builds, existing tools | Colin + Justin | This week / next week |
| 8 | Send on-site team profiles/resumes to Srinivas | Colin | Immediate |
| 9 | Put historical CI/CD issue context into the WebEx space | Divakar | Near-term |
| 10 | Discuss database exposure options offline | Anupma + Srinivas | Next meeting cycle |
| 11 | Talk to Anupma for code base access | Colin | After GitHub is resolved |
| 12 | Set up twice-weekly recurring meeting with full team | Srinivas | Immediate |

---

## What This Meeting Changes

### Before This Meeting (Set 09 State)

| Dimension | Status |
|-----------|--------|
| Deliverable work | Zero |
| Access | No GitHub, no DeepSight, no Airflow, no code base |
| Meeting cadence with Cisco ops team | None |
| Task assignments | None |
| Cisco team's knowledge of BayOne team | Colin only |

### After This Meeting (Set 10 State)

| Dimension | Status |
|-----------|--------|
| Deliverable work | Two plugins assigned (WebEx scraper, recording transcriber). Justin meetings scheduled. |
| Access | GitHub still blocked (IT case path identified). DeepSight deferred to post-release weekend. Code base access path through Anupma identified. |
| Meeting cadence with Cisco ops team | Twice-weekly recurring, recorded, full team |
| Task assignments | Four concrete tasks with clear ownership |
| Cisco team's knowledge of BayOne team | Profiles requested; Srinivas wants direct rapport with engineers |

The engagement has moved from **planning** to **execution** — constrained execution (access is still partial), but execution nonetheless. The WebEx scraper and recording transcriber require no Cisco access beyond being added to the WebEx space. The Justin meetings require only a calendar invitation. These tasks were chosen deliberately to be achievable while the access blockers are being resolved.

---

## Genuinely New Information in This Set

| Item | Detail |
|------|--------|
| **Justin** | First appearance. Build infrastructure engineer. Owns MySQL database for official builds, NFS for logs, and an MCP prototype. |
| **Anupma** | First appearance. Lead engineer, DevEx organization. Co-owns CI/CD pipeline with Divakar's team. Controls databases that are currently unexposed. |
| **Naga has (possibly) existing WebEx scraper code** | Srinivas says Naga built it but is unsure if it was committed. Colin to follow up. |
| **NXOCI workflow WebEx space** | The primary support channel for CI/CD pipeline issues. Contains 6-8 months of user complaints. This is the data source for the first task. |
| **Twice-weekly recurring meeting established** | First structured meeting cadence with the operational team. |
| **Airflow infrastructure already exists at Cisco** | DAGs established. BayOne to deploy on existing infrastructure, not spin up their own. |
| **Inference cost is a hard constraint** | Justin reports 4X cost increase. Srinivas screened Colin on this in their first conversation. No naive log-to-LLM approaches allowed. |
| **No tooling for commit-to-failure mapping** | Justin confirms this gap explicitly. Existing tools handle fix suggestions but not root cause commit identification. |
| **DevEx organizational boundary** | Anupma's DevEx team co-owns the pipeline. Database access requires cross-org negotiation. Srinivas acknowledges "people issues and organization issues." |
| **Srinivas will redirect idle BayOne resources to DeepSight** | If CI/CD work is blocked, BayOne team will be assigned other DeepSight tasks. Utilization is protected. |
| **Srinivas acknowledges the delay explicitly** | "I felt bad... months early... it's OK. We should move fast now." |
| **Colin describes two on-site people by specialty** | Person 1: agentic operations + Airflow. Person 2: MCP + LangGraph + integrations. |
| **Cassandra** | Mentioned by Anupma as a database in the ecosystem (in addition to Justin's MySQL). |
| **Build log retention: 3-5 days** | Logs on NFS are purged after 3-5 days per retention policy. Real-time processing is required. |

---

## Open Questions After This Set

1. **Does Naga's WebEx scraper code exist?** If so, in what state? If not, the team builds from scratch.
2. **What are the specific databases Anupma's DevEx team controls?** Cassandra was named. What else? What data do they hold?
3. **When will GitHub Duo MFA be resolved?** Depends on Cisco IT case turnaround time.
4. **When does the DeepSight platform release finish?** Srinivas said "this weekend" — the next meeting should confirm whether it shipped.
5. **What happened to Rui's existing CI/CD app on DeepSight?** Not mentioned in this meeting at all. From Set 06, Rui was supposed to have the current app live on DeepSight within 2-3 weeks (from Feb 17). Status unknown.
6. **What is the content volume in the NXOCI WebEx space?** 6-8 months of messages from ~1000 engineers — could be substantial.
7. **Will Namita be available this week?** Set 09 expected her week of April 6. Her Airflow expertise maps directly to the Airflow deployment work.
8. **How will the twice-weekly meetings be scheduled?** Days/times not specified in this transcript.
