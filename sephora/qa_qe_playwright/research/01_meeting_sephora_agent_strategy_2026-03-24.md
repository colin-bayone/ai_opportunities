# 01 - Meeting: Sephora Agent Strategy

**Source:** /sephora/qa_qe_playwright/source/vabhav_3_24_2026.txt
**Source Date:** 2026-03-24 (Introductory meeting / discovery conversation)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on Sephora's agentic strategy, knowledge base, and trust framework

---

## 1. QE Agents Across Lifecycle Phases

### 1.1 Overall Agent Strategy

Vaibhav describes a phased agent deployment across the entire QE lifecycle. He frames this as "QE agents to cover for multiple phases in QE lifecycle." The phases, as he enumerates them:

1. **Validating acceptance criteria / understanding requirements** -- the earliest phase, where an agent reads and validates whether the acceptance criteria in stories are complete and testable.
2. **Generating test cases and other artifacts** -- Vaibhav notes that some of these artifacts (test plans, etc.) "maybe redundant in a short while," suggesting he views test plan documents as potentially unnecessary overhead once agents can generate and execute tests dynamically.
3. **Automating tests** -- Sephora is a "Selenium-based shop" currently migrating to Playwright. All POCs and new automation development are already using Playwright.
4. **CI/CD pipeline -- continuous testing** -- supporting continuous testing as part of the deployment pipeline.

### 1.2 Additional Coverage Gaps Being Addressed

Beyond the four-phase lifecycle, Vaibhav identifies specific coverage gaps that Sephora's QE function has been "not thrilled at" and is actively working to close:

- **Visual QA / visual testing**
- **Translations and localization testing**
- **ADA compliance testing**
- **Mobile testing** (setting up mobile farms)

He characterizes these as areas where "we were not thrilled at our coverage" and the team is now "getting our hands dirty in these areas."

### 1.3 MCP Integration Requirement

Vaibhav states a hard requirement: "Obviously, anything that we are touching needs to have an MCP server and all, so we can seamlessly integrate in our workflows." This is not positioned as aspirational -- it is a gate for any new tool or technology being adopted into Sephora's QE ecosystem.

### 1.4 QE Center of Excellence (CoE) Team

- Led by **Deepika**
- Team size: approximately **five people** currently
- Described as "conceptualized again a couple of years back"
- The CoE's roadmap aligns exactly with the lifecycle phases Vaibhav described: "their whole roadmap is exactly what I just narrated to you"

---

## 2. Agentic Micro-Pod (AMP) Structure

Vaibhav reveals a significant organizational shift: Sephora is "moving to a model from a regular pod structure to an AMP structure." AMP stands for **Agentic Micro-Pod**.

Key characteristics:
- "A very lean team working on very, very small enhancements, small and frequent enhancements"
- This model means "you're churning code on a very regular basis"
- This "demands equally stronger fast-paced testing as well"
- Vaibhav frames this as validating QE's early investment in AI: "since we started this journey two years back, we were already much ahead in the game and other functions. They've all caught up, yes."

**Open question:** How many people constitute an AMP? Vaibhav later mentions "two or three member people" who "will literally be locked in a room for the entire day" and "have to be co-located," but it is unclear if this describes the AMP structure specifically or a future resourcing model.

---

## 3. Platform Migration Path: DataIQ to Claude/Advent to Nova

### 3.1 DataIQ Phase

Vaibhav describes the initial tooling journey: "We established that using DataIQ after going through 1.11." (The "1.11" likely refers to iterating through multiple model versions or configurations.) DataIQ was the platform used to build the knowledge base and set context for testing.

### 3.2 Claude/Advent Phase

"Late last year DataIQ obviously became a lot more expensive. Sort of an enterprise model adopted Claude as a tool, but we moved to Advent as the platform."

Key detail: the cost pressure from DataIQ (likely Dataiku) drove the migration. Claude became the LLM of choice; Advent became the hosting/orchestration platform.

### 3.3 Nova Phase (Current/Upcoming)

"There is an effort under Nikhil in our MCP and DevOps team. We are building our own interface, our own data models based on LiteLLM to a point that we will now, again, look at migrating what we have into our homegrown system. We call it Nova -- you know, something next, something virtual assistant."

Key details about Nova:
- **Built by:** Nikhil's MCP and DevOps team
- **Foundation:** LiteLLM (model routing/abstraction layer)
- **Nature:** Homegrown platform -- own interface, own data models
- **Name meaning:** Vaibhav glosses it as "something next, something virtual assistant"
- **Status:** Under active development; Sephora is "again, look at migrating" existing capabilities into it

This represents the third platform migration in roughly two years: DataIQ -> Claude/Advent -> Nova.

---

## 4. The SDLC Agenticization Mandate

### 4.1 Timeline and Trajectory

Vaibhav provides a clear timeline:
- **"A couple of years back"** -- AI exploration began, started with "a small intern project"
- **Until August 2025** -- "a playground for everybody to explore, see what works for you, where you can introduce it"
- **Since August 2025** -- "it's sort of a mandate now. There is no other option if you're working on anything new"
- **Current state** -- "the entire SDLC process is agenticized. From the point of defining the requirements, creating stories, obviously developing, testing, deploying, everything else."

### 4.2 Scope of Agenticization

Vaibhav explicitly lists every SDLC phase as now agenticized:
- Defining requirements
- Creating stories
- Development
- Testing
- Deployment
- "Everything else"

This is not aspirational; he frames it as current state.

---

## 5. Trust and Confidence Scoring -- "A Big Hurdle"

### 5.1 Vaibhav's Framing of the Problem

Vaibhav identifies trust and confidence as the central unsolved challenge. His exact framing:

"It's very difficult to gauge at this point of time because it is a lot of human in the loop in order to even increase that trust confidence from 60 to 80 percent. It's a big step initially. Yeah, you'll say 40-50 percent, agents are doing great work, but that 50 to 60 jump will come after you've thoroughly reviewed what your agents are doing and slowly you develop more trust and this is a big hurdle that we have to cross together."

Key nuances in his statement:
- He places current trust confidence in the **40-50% range** ("agents are doing great work" at that level)
- The jump from **50 to 60%** requires "thorough review" of agent outputs
- He describes the progression from **60 to 80%** as "a big step"
- He explicitly calls this "a big hurdle that we have to cross together"
- He acknowledges: "It doesn't matter how good your agents are doing or as far as they're churning code, to develop that trust, it will take time"

### 5.2 The Production Risk Concern

Vaibhav articulates a core anxiety: "You put your guardrails and you put your left and right, but ultimately it will show up in production and that is too late for us."

This is the fundamental fear driving the trust question -- that agent failures will only surface in production, which for Sephora (a major e-commerce retailer) is unacceptable.

### 5.3 Vaibhav's Aspiration for a Trust Index

He describes wanting to produce a composite score: "Incorporate that together and then come up with a trust index and yeah, look, we are good 4.8 out of 5. How do you compute 4.8? I don't know."

This is a candid admission that the methodology for computing composite trust scores does not yet exist at Sephora.

### 5.4 The Expanding Scope of Quality

Vaibhav describes how his quality mandate has expanded beyond traditional testing:

"Quality is not -- I mean, it's no longer output driven, right? Quality is there in every different realm of SDLC. Quality of the stories that are created, quality of the code, not the bugs and all, but just the quality, testing, quality of testing, and quality of deployment, everything is understood to me in terms of quality umbrella."

He summarizes the impact on his role: "My job is becoming tougher because I was just testing code. Now I'm being asked to test every single outcome of every single phase."

---

## 6. Colin's Response: Agent Evaluation Framework

### 6.1 Core Philosophy -- "Just Like People"

Colin's central thesis on agent evaluation: "The best way, even whenever you're trying to think of like what an agent should do... the answer is just like people. And that's the core, I think, for all of it. Even with scoring or evaluating AI, how do we as people look at other people, and how do we assess if I trust you to do this? And it's the same thing."

### 6.2 Agent-to-Agent Assessment Warning

Colin explicitly warns against having agents evaluate themselves or each other:

"The trick is to not let an agent ever assess itself. And it's also true to not have an agent assess another agent. They have this very oscillating behavior where they either go very, very, very overwhelmingly positive, everything's perfect all the time, or polar opposite, everything's awful all the time. It's not good."

He advocates instead for "clear KPIs almost like you would for a person."

### 6.3 The Reliability Score Analogy

Colin uses a workplace analogy: "I know this person, I assign them a task, I assign them every time on Friday. They say they'll have it done for me next Wednesday. It has never been done on next Wednesday. It's always the next week, maybe. Well, what would you give them in terms of a reliability score? It's the same kind of question to ask an agent."

### 6.4 Confidence Through Reinforcement Learning (Simplified)

Colin describes his specific approach to building agent confidence:

"At first, humans have to be in the loop a lot. But humans, this is essentially reinforcement learning in a much simpler way. When we say confidence, all that really means is that the agent has done a good thing repeatedly, consistently, a number of times. And the human is given a green light for those number of times."

The process:
1. **Initial phase:** Heavy human-in-the-loop review
2. **Threshold setting:** "We can set a threshold as to whatever you'd like"
3. **Positive reinforcement:** Agent accumulates a track record of human-approved outputs, giving it "reference to those patterns, so it's kind of how it can look back at its notes before it goes and approaches a new problem"
4. **Negative reinforcement:** "Same works for negative direction"
5. **Graduated autonomy:** "At a certain point, human doesn't need to be in the loop anymore"
6. **Exception handling:** "The human only needs to come into the loop whenever that agent makes a mistake again to say, why was this?"

### 6.5 Why Humans Must Stay in the Correction Loop

Colin argues against fully automated self-correction:

"That's something that technically, yes, you could have an agent resolve within itself, but should you? Probably not, because it's not going to be able to course correct. They tend to simplify. They tend to go off-road. You still want a human expertise and insight to say, that wasn't right. Here's what we should be doing instead."

### 6.6 The Chef Analogy for Human Roles

Colin offers a vision for what human roles look like in an agentic world: "You almost transition from a sous chef or a line chef to the master executive chef for the kitchen. You're walking around tasting everyone else's stuff. You're not actually cooking yourself."

### 6.7 Framework vs. Model as the Bottleneck

Colin asserts that performance caps come from the framework, not the models: "If you ever see a cap forming, that's because of the framework, not because of the models. It's just like us with people."

### 6.8 The Guardrails Critique

Colin offers a pointed critique of guardrails as commonly implemented: "I'm 100% with you on the guardrails. It's a lot of hand waving, frankly. It's glorified regex pattern matching, and maybe some AI to AI communication that helps it."

---

## 7. Relevancy Testing for Agentic Workflow Outcomes

Vaibhav names "relevancy testing" as a distinct concern: "Relevancy testing is a big deal right now just to measure the quality of agentic workflow outcomes. How do you know your agents are doing the right thing?"

This is positioned as a non-functional requirement -- separate from the functional agent phases (test generation, automation, etc.) but critical to the overall system's reliability.

**Open question:** Vaibhav does not describe what "relevancy testing" looks like in practice at Sephora. He names it as a priority but does not detail the methodology.

---

## 8. Metrics and Decision-Making Support

### 8.1 Leads Becoming Decision-Makers

Vaibhav describes a role transformation: "More and more, all our leads are now getting converted into not an engineer, but a decision-maker. That's what I'm telling all my leads now, because everybody's worried about the job. Agents are doing everything, what are we doing? Hey, you wanted to be a manager, right? Now you have a team of agents."

He frames accountability as unchanged but redirected: "You're still accountable. Just that you're accountable for a team output, not your individual output."

### 8.2 Metrics as Support for This Transition

The need for metrics is tied directly to this role shift. If leads are managing agent teams rather than doing engineering themselves, they need metrics to:
- Understand agent performance
- Make decisions about when to intervene
- Report on team output quality
- Justify trust levels to leadership

---

## 9. Unified Knowledge Base Initiative

### 9.1 The Problem: Siloed Knowledge

Vaibhav describes the original failure mode: "Each one of our functions were working out of our own knowledge base, creating a separate knowledge. Yeah, we have this, you have that."

Specific example of the problem: "We were capturing as part of QE -- and we were capturing meeting minutes or whiteboard drawings, making it part of the knowledge base, while other agent had no clue about some discussion that happened. So the development was not based on the newly created design, but we were testing out of that design."

### 9.2 The Solution: Single Shared Knowledge Base

"One other big initiative that we're currently working is establishing a common knowledge base, which is something that every single function can work out of."

What feeds into the unified knowledge base:
- **Business requirements and PRDs** -- "creating or translating business requirements and PRDs"
- **Code repositories** -- "the entire code repository"
- **Test cases** -- "the entire test cases"
- **Meeting minutes and whiteboard drawings** -- captured artifacts from discussions
- **Design artifacts** -- design decisions that inform testing

### 9.3 The Cross-Functional Vision

Vaibhav articulates the specific benefit: "Think about if the dev agent knows how the QE agent is going to test the code, then that expectation will be built into the development itself. The testing improves and vice versa."

He frames this as mutual learning: agents that "learn from each other, basically."

### 9.4 Resolution

The teams moved from "you need to share" to "let's create a common knowledge base" -- a single source rather than shared access to multiple separate stores.

Vaibhav's current status: "Let's see how things pan out, but a lot of things are evolving and evolving very fast."

Colin's response: "Definitely on the right track with that, for sure."

---

## 10. Colin's Technical Approach (BayOne Methodology)

### 10.1 Deterministic-First Philosophy

Colin states his core principle: "For anything that I do, you'll find that the approach is first deterministic as much as I can. Bring in AI last as a rule because it's kind of like the telephone game. There's a certain amount of reliability that you can and cannot get out of AI systems. And I don't like seeing numbers that are 80 percent. I like 97 plus."

### 10.2 State Graph Approach

Colin describes an autonomous process that maps the codebase:
- Deterministically explores the codebase
- Creates "essentially a state graph of what's going on"
- Covers dependency mapping, CVE identification, library usage, module communication
- Also identifies dead code
- Plugs into CI/CD pipelines so that "whenever new things happen or change, now I can adjust my tests accordingly"

### 10.3 Coverage Philosophy

Colin redefines coverage: "When we say coverage for a unit test, does that just mean that it's testing out all the functions or should it also test the things that it touches that could be downstream dependencies recursively? It has to be that."

### 10.4 Multi-Model Strategy

"Playwright is the secret sauce for the actual testing, even from the UI testing angle. Bringing that in with visual understanding models, that's where we usually have to mix from the grab bag a little bit with the models."

Model allocation:
- **Claude:** ~90% of tasks
- **Gemini:** Visual understanding tasks ("Gemini tends to do a lot better job with visual understanding")
- **OpenAI:** Very few use cases ("that's a different story")

### 10.5 Agents Checking Agents

Colin describes a specific use case: "You can have agents check on other agents, too. So even when the agents are messing up, you don't have to waste a human's time to go and look at this and say, that was junk."

Example: "Those days where you're doing some UI testing and a button position moves, then the test fails. It was just because it relocated. We should visually understand that enough."

### 10.6 The Human Accuracy Benchmark

Colin provides a calibrating statistic: "Professional PhD researchers given computer vision task to label, is this a giraffe or is this a car? The best of the best is 92%. Giraffe versus a car. Why? Because they're given 10,000 images to label and people get lazy."

He uses this to argue that agent consistency can exceed human consistency for repetitive tasks.

### 10.7 Observability and Transparency

Colin emphasizes the need for system-level observability: "How is my team doing? And not just how's my team doing, but how are my agents doing?"

He describes the value of mature system diagnostics: "After the system's mature enough, it's really, really interesting to see what those edge cases are. Is this because it's being too strict? Is this because we're wrong?"

He connects observability to upstream accountability: "If some error occurs over here and it should have been caught upstream, why didn't we catch that? And that kind of a loop to have those two things in sync with each other is all part of this kind of system autonomy."

---

## 11. Selenium to Playwright Migration

### 11.1 Current State

Sephora is a "Selenium-based shop" that has completed POCs and is doing all new automation development in Playwright.

### 11.2 Colin's Assessment

Colin: "Moving from Selenium to Playwright. It'll be night and day. Playwright, not that Selenium was a bad framework, but Selenium days you're used to sticking long delays and things, essentially. Things take forever because you have to wait. There's some uncertainty there. Playwright is so much better, and it works so much better for AI as well."

He also notes Playwright's alignment with Azure: "Playwright is from Microsoft anyway. So there's very, very good visual understanding tools within Azure. So everything gets hosted there."

---

## 12. Sephora's Execution Velocity

### 12.1 Roadmap Acceleration

Vaibhav provides a striking detail about pace: "We just created our 2026 roadmap in December, which had some deliverables in Q1, Q2, Q3, everything that we were supposed to deliver in Q3, we were -- we delivered it in March."

He continues: "My objectives for 2026 is already done, kind of. That's the next thing now."

### 12.2 No Fixed North Star

When asked about a North Star, Vaibhav responds: "There is no North Star that you have to be on. There is no target that I'm trying to achieve. I'm taking it day by day... North Star, that definition of North Star is changing. Sorry, I can't answer your question, but it's not defined. It's an evolving target now."

He later refines this to a general principle: "My north star would right now be stay ahead of the game and not be the roadblocker from a testing perspective because I don't want to be in a situation where they say we're churning code left and right and testing is slow."

---

## 13. Upskilling and Team Transformation

### 13.1 Vaibhav on Upskilling Needs

"We need talented people across the board, not just creating or working on the platform, which is from pure user perspective, how to use this technology to deliver business commitments."

He draws a distinction: "You are not just creating agents. You have to be solid enough to be able to use and orchestrate between these agents to deliver the right outcome."

### 13.2 Colin's Upskilling Offer

Colin describes two initiatives:
1. **Mandatory training for new hires:** "Anyone new that's coming in for Sephora will have some kind of training" -- all BayOne staffing hires will receive AI upskilling.
2. **Team upskilling offering:** Available for existing Sephora teams wanting to get effective with AI tools.

Colin also describes an incubation model: "What if it is a we incubate the person, they're working on your project for you, we incubate them while they're with us, we're teaching them what they need to know."

---

## 14. Staffing and Resourcing Details

### 14.1 Vaibhav's Team Structure

- **10-11 QE leads** on-site, all described as SMEs
- **Majority of workforce** is offshore
- Named leads: **Ashweta, Lakshmi, Priyanka**
- Deepika leads the CoE team (~5 people)

### 14.2 Geographic and Staffing Trajectory

Vaibhav forecasts a geographic shift:
- **Current:** Majority offshore
- **Near-term (6 months to 1 year):** "A lot more positions will probably move nearshore and on-site, nearshore to start with"
- **Rationale:** Offshore talent is "not upskaling at the same speed as nearshore"
- **AMP model implications:** Co-location requirements for 2-3 person pods
- **Nearshore targets:** South America, Canada
- **On-site:** "Always a premium" with limited room, but "if there is a star player, then I can argue"

### 14.3 Rate Discussion

- Deepika's open role: on-site at **$120/hr**
- Vaibhav: "I'll have to take it up to my boss. But if it has a value behind it, then yes."
- Vaibhav also says there's "some flexibility" around the $95 rate: "I'm working with HR because this is a more niche area and these rates are still based on legacy preservation of QE."

### 14.4 Hiring Philosophy

Vaibhav on what matters: "It's the communication that we'll have. Anybody can create a catchy resume... It's all based on your intuition. You like the guy, you don't like the guy."

His whiteboard test: "Simple problem. It's actually nothing related to Java or anything. I'm not testing that. This is a common problem. Tell me what you're thinking. That's it... I just want your mental attitude, attitude. How you are relating to your problem."

---

## 15. Unresolved Questions and Open Items

1. **How will relevancy testing for agentic workflow outcomes be implemented?** Vaibhav names it as a priority but provides no methodology.
2. **How will the trust index be computed?** Vaibhav candidly says "I don't know" when asked how to compute a 4.8/5 trust score.
3. **What is the timeline for Nova platform readiness?** The migration from Advent to Nova is described as in-progress but no delivery date is given.
4. **How will the unified knowledge base be architecturally implemented?** The concept is clear but the technical approach (RAG, vector store, document management system, etc.) is not discussed.
5. **What is the relationship between the AMP model and QE agent deployment?** It is unclear how the AMP (Agentic Micro-Pod) structure interacts with the QE lifecycle agents -- are QE agents embedded in AMPs or centrally managed by the CoE?
6. **Deepika's open role status:** Vaibhav is uncertain whether the agentic QE role has been filled. Colin/BayOne have sent candidates but outcomes are unclear.
7. **What does "quality of deployment" testing look like in an agentic context?** Vaibhav expands his mandate to cover deployment quality but does not describe what that means operationally.
8. **How does the MCP server requirement interact with the Nova platform?** Both are mentioned but their architectural relationship is not explained.

---

## 16. Key Quotes Index

| Speaker | Quote | Context |
|---------|-------|---------|
| Vaibhav | "This was considered to be the slowest horse in the race. You're done with development, you're done with deployment, now testing is lagging behind." | On QE's historical perception at Sephora |
| Vaibhav | "Since August, it's sort of a mandate now. There is no other option if you're working on anything new." | On the AI mandate |
| Vaibhav | "Anything that we are touching needs to have an MCP server and all, so we can seamlessly integrate in our workflows." | On MCP requirement |
| Vaibhav | "It's very difficult to gauge at this point of time because it is a lot of human in the loop in order to even increase that trust confidence from 60 to 80 percent. It's a big step." | On the trust challenge |
| Vaibhav | "This is a big hurdle that we have to cross together." | On building agent trust |
| Vaibhav | "You put your guardrails and you put your left and right, but ultimately it will show up in production and that is too late for us." | On production risk |
| Vaibhav | "How do you compute 4.8? I don't know." | On trust index methodology |
| Vaibhav | "My job is becoming tougher because I was just testing code. Now I'm being asked to test every single outcome of every single phase." | On expanding quality mandate |
| Vaibhav | "Hey, you wanted to be a manager, right? Now you have a team of agents." | On role transformation for leads |
| Vaibhav | "Think about if the dev agent knows how the QE agent is going to test the code, then that expectation will be built into the development itself." | On unified knowledge base value |
| Vaibhav | "Everything that we were supposed to deliver in Q3, we delivered it in March." | On execution velocity |
| Colin | "For anything that I do, the approach is first deterministic as much as I can. Bring in AI last." | On methodology |
| Colin | "I don't like seeing numbers that are 80 percent. I like 97 plus." | On quality threshold |
| Colin | "The trick is to not let an agent ever assess itself. And it's also true to not have an agent assess another agent." | On evaluation methodology |
| Colin | "When we say confidence, all that really means is that the agent has done a good thing repeatedly, consistently, a number of times. And the human has given a green light." | On confidence scoring |
| Colin | "If you ever see a cap forming, that's because of the framework, not because of the models." | On performance limitations |
| Colin | "It's a lot of hand waving, frankly. It's glorified regex pattern matching." | On guardrails as commonly implemented |
| Colin | "You almost transition from a sous chef or a line chef to the master executive chef for the kitchen." | On human roles in agentic world |
