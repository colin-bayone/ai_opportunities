# 11 - Srinivas Team Meeting: Guidance and Operating Philosophy

**Source:** /cisco/cicd/source/srinivas-and-team_4-10-2026_formatted.txt
**Source Date:** 2026-04-10 (Srinivas team meeting)
**Document Set:** 11 (Second Srinivas team meeting)
**Pass:** Consolidated deep dive on Srinivas's guidance, problem framing, access items, and tool stack

**Transcript quality note:** This transcript has severe speech-to-text degradation. Many sections are unintelligible. Content below is reconstructed from recoverable portions only. Interpretations of garbled text are marked where confidence is lower.

---

## Srinivas's Operating Philosophy

Srinivas opened the meeting with a monologue on how he expects the team to work. Key principles extracted:

### 1. Fast Iteration Over Perfection
"I want to run as [fast] first. Meaning, I don't want to have a perfect solution, but I want a solution where I can test it out, and see how far it will take it, and forward to the next set of features."

He explicitly rejects waterfall-style design-then-build: "We change the architecture pretty fast... because unless you build, you don't know what are the challenges or the outcome that you are going to expect."

### 2. Uncharted Territory Acknowledged
"These are all uncharted [territory]. And we don't know how, and there are people [dependencies] also." Srinivas acknowledges that the team will encounter blockers from other Cisco teams and departments. The instruction: when blocked, escalate to him. "Call it Unblocked. Call it results."

### 3. Reusable Pieces as a Dual Goal
"Build the solution for the [CI/CD] department that we are looking for. At the same time build reusable pieces where we can leverage it for some of the other [teams/groups]."

This confirms what was captured in Set 10 and the team briefing (Set 03): Srinivas explicitly wants both the immediate CI/CD solution and generalizable components.

### 4. Scope Expansion for Good Performers
"If you guys prove yourself... you can take on additional things, you can [work on] other products or other [projects]." This is consistent with Colin's characterization in Set 03: "He's trying to build his kingdom."

### 5. Come with Suggestions and Innovations
"I support folks who come with the suggestions and innovations. Once you know what the problem you're trying to solve, you [don't] have to depend on me how to solve it." Srinivas explicitly delegates solution design to the team. He wants to define the problem, not the solution.

### 6. Existing Infrastructure is Ready
"It's not like you have to go [build everything from scratch]. You already have [an existing system] running with a basic set... All you have to do is just work with the business logic and figuring out what needs to happen." The DeepSight platform and surrounding infrastructure already exist. The team is extending, not building from zero.

---

## The Real Problem Statement: Beyond Scraping

Srinivas delivered a critical reframing of the WebEx scraping task that clarifies what he actually wants:

### Scraping Is Not the Problem
"Scraping is just a one day job... to identify the things." The scraper itself is trivial in Srinivas's view. It is not the deliverable — it is the data acquisition step.

### The Real Deliverable: Pain Point Analysis
"What I'm saying is that we need to first get the entire [data], do a quick analysis and say what are the top pain points that users are facing. And now to solve the pain point, what are the [data] sources that we have in the pipeline."

The sequence Srinivas wants:
1. Scrape the WebEx channel (one day)
2. Analyze the content to identify and rank user pain points
3. Map those pain points to data sources in the CI/CD pipeline
4. Build solutions that address the actual problems

### The CI/CD Pipeline Problem in Srinivas's Words
"The issue is that the engineer is raising the [PR]. The [PR] goes through [approximately 45 checks] today. And there are a bunch of systems... at the end, the [PR] gets [merged]... which gets loaded up to the router."

"Every day we have three, four... six, seven release groups are assigned, they [manage] that entire process."

"Now you want to take [it from manual to automated]. Meaning, let's say there is a [PR]. How do I know where that [PR] is? Can AI help me to unblock? Meaning, let's say, it says that I have some issue, something failed. What failed we don't know. Because it's going through this huge [pipeline]. So we need to look deep into the individual [PR] and say, okay, what is the issue, where [did] it start? What could be the issue? And how do we unblock? We have to reason that and suggest a solution. That's the problem."

**Key insight:** Srinivas is not asking for log parsing or error classification as standalone tools. He wants an AI system that can look at a stuck PR, determine where in the 45-check pipeline it failed, reason about why, and suggest how to unblock it. The log analysis is a component of that, not the end goal.

---

## Access and Tooling Guidance

### Copilot Access
- Go to `appstore.cisco.com`
- Search for "Copilot"
- Submit a request
- Reach out to Mahaveer (Cisco contact) to expedite
- Login uses User ID and support system credentials → EME group

### DeepSight Platform Access
- Go to `deepsight.cisco.com`
- Srinivas will provide direct access once the team is on the platform
- Initial look is expected "maybe this week" once access issues are resolved

### Naga's Existing Work
- Srinivas confirms Naga "developed something" for WebEx scraping
- But instructs: "You have to [build] this [as] an app... [for] any [WebEx] space"
- The team should build their own regardless of Naga's work
- Naga's code may or may not be usable: "It is not [ready] today"

### Airflow Timing
Colin asked about Airflow access. Srinivas's response: "Airflow is too early... So we have [a] lot to design, lot to figure out how things move. [Airflow] is the final stage where you want to create [a] pipeline."

This contradicts the Set 03 briefing where Colin described Airflow as the orchestration layer from the start. Srinivas sees Airflow as a later-stage concern, after the design and logic are proven. The team should focus on the business logic first, then productionalize with Airflow.

---

## Tool Stack Discussion

Colin asked directly: "For AI tools, do you want us to stick with Copilot? Do you want us to request Windsurf, Cursor? Do you support Claude Code?"

Srinivas's response:
- Cisco engineers primarily use **Cursor** (~85%) and **Copilot** (~15%)
- Copilot is used for a subset of use cases, not primary development
- Cisco engineers "don't write the Python code, they write the [system] code" (suggesting Cursor/Copilot are used for C/C++/system-level code, not Python)
- Srinivas mentioned **Codex** access and suggested the team get Codex login
- Colin's position: "Between Codex and Claude Code, all my needs are met. We don't even touch [the others] internally."
- Srinivas endorsed this: "We will tell you where to [use what] and we will figure it out."

---

## Meeting Cadence Established

Srinivas: "It has to be recurring... at least twice [a] week, otherwise things will [drift]."

Colin confirmed his availability: "Thursday, Fridays are totally good for me. I'm actually like the bridge between IST and PST... The only time that wouldn't work for me is after 5 PM PST. Any time before that."

Srinivas suggested the team use the WebEx space to catch him for ad-hoc questions between meetings.

---

## Srinivas on Justin and Log Analysis

Srinivas briefly addressed the log analysis work when someone mentioned researching "how to store [the] logs, how things look, how logs are created." His response indicated that existing work has been done: "I think just the one that we did... yeah, we did one more, a couple of them." This suggests Justin has shown Srinivas prior attempts at log analysis tooling, consistent with Set 01's characterization of Justin's Python+LLM workflow as a POC.

---

## Implications for the Srinivas Prep Document

From this meeting, the prep document should address:

1. **We understood the real problem.** Not just scraping or log parsing — the goal is an AI system that helps engineers understand where PRs are stuck in the 45-check pipeline and how to unblock them.

2. **We have been iterating fast.** Wall-E bot built and deployed in one week. Architecture diagrams produced. Log type mapping completed. WebEx recording extraction tool built.

3. **We built reusable pieces.** Wall-E is channel-agnostic. The WebEx recording extractor works for any meeting. The log type mapping applies across all Bazel builds.

4. **Airflow timing is acknowledged.** We are focusing on business logic and design first, as Srinivas directed. Airflow comes when the pipeline is ready to productionalize.

5. **Access blockers remain.** DCN Switching tenant, Pulse/Scribble repos, permanent ADS machine. These need Srinivas's help.
