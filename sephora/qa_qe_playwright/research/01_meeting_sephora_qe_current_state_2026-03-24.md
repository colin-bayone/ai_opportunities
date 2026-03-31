# 01 - Meeting: Sephora QE Current State

**Source:** /sephora/qa_qe_playwright/source/vabhav_3_24_2026.txt
**Source Date:** 2026-03-24 (Introductory meeting / discovery conversation)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on Sephora's QE current state and transformation journey

---

## 1. Vaibhav's Background and Role Context

### 1.1 Professional History

Vaibhav joined Sephora from **Walmart Labs** in April (year not specified, likely ~2020-2021 based on the "couple of years" timelines he describes). He was hired with a specific mandate: **migrate Sephora from their old legacy APG e-commerce platform to a new microservices architecture**.

> "I joined Sephora from Walmart Labs back in April. [...] I was hired to migrate Sephora from old legacy APG e-commerce product to new microservices world."

That migration took "the next couple of years." After completing it, Vaibhav moved to **infrastructure**, specifically setting up Sephora's **Microsoft Cloud Platform in Azure**. That also took "another couple of years."

### 1.2 Current Role: Managing QE

After infrastructure, Vaibhav moved into managing **QE (Quality Engineering)**. He describes the state of QE when he took it over bluntly:

> "This was considered to be the slowest horse in the race. You're done with development, you're done with deployment, now testing is lagging behind."

This framing is critical -- QE was perceived as the bottleneck in Sephora's delivery pipeline. Vaibhav's charge has been to fix that perception and the reality behind it.

### 1.3 Current North Star

When asked directly about his North Star, Vaibhav deflected somewhat, saying the definition is evolving. But he offered this:

> "My north star would right now be stay ahead of the game and not be the roadblocker from a testing perspective because I don't want to be in a situation where they say we're churning code left and right and testing is slow. I want to stay ahead of the whatever means."

This reveals that the legacy perception of QE as a bottleneck is still a live concern. Vaibhav's primary mandate is velocity parity: QE must not be slower than development.

---

## 2. AI Journey and Mandate

### 2.1 Origin: Intern Project (~2024)

AI adoption at Sephora's QE started roughly two years before this conversation (so approximately early-to-mid 2024):

> "We started with AI, couple of years back again. It started with a small intern project, but obviously it evolved into bigger and bigger things."

### 2.2 The August 2025 Mandate

The AI trajectory changed fundamentally in **August 2025**. Before that date, AI was optional and exploratory. After, it became mandatory:

> "Until last August, it was a playground for everybody to explore, see what works for you, where you can introduce it. Since August, it's sort of a mandate now. There is no other option if you're working on anything new."

This is a hard organizational line. Everything new must incorporate AI. No exceptions.

### 2.3 SDLC "Agenticized"

Vaibhav describes the entire SDLC process as now "agenticized" (transcribed as "ancientized"):

> "So much so now the entire SDLC process is, I can use the word, agenticized. From the point of defining the requirements, creating stories, obviously developing, testing, deploying, everything else."

This is a sweeping claim: every phase of the software development lifecycle -- requirements, story creation, development, testing, deployment -- has agentic AI integrated into it.

---

## 3. AMP (Agentic Micro Pod) Model

### 3.1 Structural Shift

Sephora is transitioning from a **"regular pod structure"** to an **AMP (Agentic Micro Pod)** structure. Vaibhav asked if anyone had mentioned this:

> "We are moving to a model from a regular pod structure to an AMP structure. I don't know if anybody mentioned that. It's called Agentic Micro Pod."

### 3.2 How AMP Works

The AMP model has several defining characteristics:

- **Very lean teams** -- small headcount per port
- **Small and frequent enhancements** -- not large feature releases
- **Rapid code churn** -- "you're churning code on a very regular basis"
- **Demands equally fast testing** -- "that demands equally stronger fast-paced testing as well"

### 3.3 Implications for QE

The AMP model creates a forcing function for QE velocity. Small, frequent changes mean testing cannot be batched or deferred. QE must keep pace with a continuous stream of small releases, which is fundamentally different from testing large quarterly releases.

### 3.4 Staffing Implications

Vaibhav sees co-location as essential for AMP:

> "The way it's structured, we will need people to work together as two or three member people. It will literally be locked in a room for the entire day. They have to be co-located."

He is "primarily looking at nearshore" and anticipates that "a lot more positions will probably move nearshore and on-site, the nearshore to start with." This is framed as a future shift -- currently the majority of their workforce is offshore, but the AMP model may force migration toward nearshore/onsite.

---

## 4. Platform Evolution: DataIQ to Claude/Advent to Nova

### 4.1 Phase 1: DataIQ

The first AI platform Sephora QE used was **DataIQ** (likely Dataiku or similar). Vaibhav describes going through iterations ("1.11" -- possibly version 1.11 or eleven iterations) to establish the right knowledge base and context for testing:

> "So we established that using DataIQ after going through 1.11."

### 4.2 Phase 2: Claude on Advent

Late in 2025, DataIQ became too expensive ("obviously became a lot more expensive, sort of an enterprise model"). Sephora adopted **Claude as a tool** but moved to **Advent as the platform**:

> "Then late last year DataIQ obviously became a lot more expensive. Sort of an enterprise model adopted Claude as a tool, but we moved to Advent as the platform."

Note: "Advent" is the transcription -- this could be a specific internal platform name, or a transcription artifact. Colin responded "Interesting" to this, suggesting it was new information.

### 4.3 Phase 3: Nova (Homegrown, LiteLLM-based)

A new initiative is underway, led by **Nikhil** (referenced as heading MCP and DevOps):

> "Now, there is an effort under Nikhil in our MCP and DevOps team. We are building our own interface, our own data models based on LiteLLM to a point that we will now, again, look at migrating what we have into our homegrown system. We call it Nova, you know, something next, something virtual assistant."

Key details:
- **Nova** = homegrown AI platform
- Built on **LiteLLM** (open-source model gateway/proxy)
- Includes custom **data models** and a custom **interface**
- Represents another migration -- from Advent/Claude to their own system
- Led by Nikhil's **MCP and DevOps team**

This is the third platform in roughly 18 months (DataIQ -> Advent/Claude -> Nova). The pace of platform churn is notable.

---

## 5. Selenium-to-Playwright Migration

### 5.1 Current State

Sephora is a **"Selenium-based shop"** and is migrating to Playwright:

> "We've been using, we are Selenium-based shop. So we are now looking at migrating to Playwright. So we've done all POCs and new automation development using Playwright."

Key details:
- **POCs are complete** -- Playwright has been proven out
- **New automation development** is already happening on Playwright
- The legacy Selenium suite presumably still exists and runs

### 5.2 Colin's Commentary on Playwright

Colin offered strong validation for this direction:

> "Moving from Selenium to Playwright. It'll be night and day. Playwright, not that Selenium was a bad framework, but Selenium days you're used to sticking long delays and things, essentially. Things take forever because you have to wait. There's some uncertainty there. Playwright is so much better, and it works so much better for AI as well."

Colin also noted that Sephora's Azure infrastructure is advantageous: "Playwright is from Microsoft anyway. So there's very, very good visual understanding tools within Azure."

---

## 6. QE COE Team

### 6.1 Structure

Sephora has a **QE Center of Excellence (COE)** team:

- **Led by Deepika**
- **~5 people** currently
- **Conceptualized ~2 years ago** (circa 2024)
- Their roadmap aligns with the QE agent strategy Vaibhav described

> "We have a QE COE team conceptualized again a couple of years back. Deepika is leading it, I don't know if you've had a chance to meet her yet but it's a very small team about five currently."

### 6.2 Deepika's Hiring

Deepika has been trying to fill an "agentic AI" role. BayOne has been sending candidates but faced challenges:
- **On-site requirement**: once per week in office
- **Budget constraints**: initial rate of ~$120/hour for onsite, described as "based on legacy preservation of QE" rate cards
- Vaibhav indicated there is "some flexibility" and he is "working with HR because this is a more niche area"
- Requirements for the role evolved -- "The roles evolved three different times." Initially titled "QE, AI and Gen AI," which attracted wrong candidates. Changed to "automation engineer" which yielded better results.

### 6.3 Broader QE Team

Beyond the COE, Vaibhav has a broader QE organization:

> "We have 10, 11, QE leads here. All of them are SMEs."

He describes limited room to hire onsite but willingness to argue for "a star player."

---

## 7. QE Agent Strategy

### 7.1 Agent Lifecycle Coverage

Vaibhav described a phased agent strategy covering the full QE lifecycle:

> "We are creating QE agents to cover for multiple phases in QE lifecycle."

The phases, in order:
1. **Validating acceptance criteria / understanding requirements**
2. **Generating test cases** and other artifacts
3. **Creating test plans** (noted these "maybe redundant in a short while")
4. **Automating tests** (Playwright)
5. **CI/CD pipeline integration** for continuous testing

### 7.2 Non-Functional Agent Capabilities

Beyond functional testing, Vaibhav identified critical non-functional concerns:

- **Relevancy testing**: "Relevancy testing is a big deal right now just to measure the quality of agentic workflow outcomes. How do you know your agents are doing the right thing?"
- **Metrics generation and decision-support**: Supporting the transition of QE leads from individual contributors to decision-makers
- **Trust scoring**: Developing a "trust index" -- Vaibhav mentioned wanting to compute something like "4.8 out of 5" but acknowledged "How do you compute 4.8? I don't know."

### 7.3 The Role Transformation

Vaibhav is actively managing the human side of this transition:

> "More and more, all our leads are now getting converted into not an engineer, but a decision-maker. That's what I'm telling all my leads now, because everybody's worried about the job. Agents are doing everything, what are we doing? Hey, you wanted to be a manager, right? Now you have a team of agents. So you're still accountable. Just that you're accountable for a team, not for your individual contribution."

This is a significant organizational shift: QE leads transitioning from hands-on testing to managing/orchestrating agent teams.

---

## 8. Identified Gaps in QE Coverage

Vaibhav explicitly called out areas where Sephora's QE coverage is insufficient:

> "There have been few gaps in our QE in terms of supporting visual testing, for example, the visual QA, or translations and localization testing, or ADA compliance testing. We're also looking at setting up mobile farms."

### 8.1 Visual QA

Visual testing is a recognized gap. Colin responded to this with specific advice about using visual understanding models, noting that **Gemini tends to do a better job with visual understanding** than Claude:

> "Bringing that in with visual understanding models, that's where we usually have to mix from the grab bag a little bit with the models. So, for instance, it's not always Claude. We love Claude. We use Claude for about 90% of things. But, for instance, Gemini tends to do a lot better job with visual understanding."

### 8.2 Translations and Localization Testing

Listed as a gap but not elaborated on in this conversation.

### 8.3 ADA Compliance Testing

Listed as a gap. Colin noted this is well-suited to an agentic approach:

> "Even from the QA perspective, you can give an identity to an agent, even if you're doing ADA compliance testing. Here are the strict requirements for this specific compliance, and maybe there's also a persona that you give to an agent."

### 8.4 Mobile Farms

Sephora is looking at setting up mobile device farms for testing. Colin noted that Playwright can handle mobile testing: "Mobile testing, also it can be done with Playwright, so there's no difference there."

### 8.5 MCP Server Requirements

A cross-cutting requirement: any new tool or capability must have an **MCP server** for seamless integration into existing workflows:

> "Obviously, anything that we are touching needs to have an MCP server and all, so we can seamlessly integrate in our workflows."

---

## 9. Common Knowledge Base Initiative

### 9.1 The Problem

Vaibhav described a significant initiative to create a **shared knowledge base** across all functions:

> "One other big initiative that we're currently working is establishing a common knowledge base, which is something that every single function can work out."

The knowledge base would include:
- Business requirements and PRDs
- Entire code repository
- All test cases
- Meeting minutes, whiteboard drawings, design discussions

### 9.2 The "Aha" Moment

The need for this emerged from a concrete failure pattern. Different teams were maintaining separate knowledge bases, leading to misalignment:

> "We were capturing as part of QE and we were capturing meeting minutes or whiteboard drawings, making it part of the knowledge base, while other agent had no clue about some discussion that happened. So the development was not based on the newly created design, but we were testing out of that design."

Development agents and QE agents were working from different information. Tests were being written against updated designs while code was being written against older specifications (or vice versa).

### 9.3 The Vision

> "Think about if the dev agent knows how the QE agent is going to test the code, then that expectation will be built into the development itself. The testing improves and vice versa."

> "Instead of sharing, we said, you'll create a common knowledge base."

---

## 10. 2026 Roadmap Acceleration

### 10.1 Dramatic Acceleration

Vaibhav made a striking claim about their roadmap velocity:

> "We just created our 2026 roadmap in December, which had some deliverables in Q1, Q2, Q3. Everything that we were supposed to deliver in Q3, we were, we delivered it in March."

Q3 deliverables completed by March -- roughly 6 months ahead of schedule. This is presented not as a humble brag but almost as a problem:

> "Things are changing so rapidly, and my objectives for 2026 is already done, kind of. That's the next thing now. North Star, that definition of North Star is changing."

### 10.2 Implications

This acceleration creates a planning vacuum. Vaibhav cannot define a clear North Star because the pace of change outstrips planning cycles. The roadmap created in December 2025 was obsolete by March 2026.

---

## 11. Trust and Confidence Framework

### 11.1 Vaibhav's Framing of the Trust Problem

Vaibhav articulated the trust challenge as a major hurdle:

> "It's very difficult to gauge at this point of time because it is a lot of human in the loop in order to even increase that trust confidence from 60 to 80 percent. It's a big step initially. Yeah, you'll say 40-50 percent, agents are doing great work, but that 50 to 60 jump will come after you've thoroughly reviewed what your agents are doing and slowly you develop more trust and this is a big hurdle that we have to cross together."

He described a progression: 40-50% confidence is easy, getting to 60% requires thorough review, and 60-80% is "a big step."

### 11.2 Production Risk

> "You put your guardrails and you put your left and right, but ultimately it will show up in production and that is too late for us."

The fear is that agent mistakes will manifest in production, where the cost is highest.

### 11.3 Expanding Quality Scope

Vaibhav's quality mandate is expanding beyond traditional testing:

> "Quality is there in every different realm of SDLC. Quality of the stories that are created, quality of the code, not the bugs and all, but just the quality, testing, quality of testing, and quality of deployment, everything is understood to me in terms of quality umbrella."

> "Now I'm being asked to test every single outcome of every single phase."

This is scope expansion: from testing code to testing the entire agentic SDLC output at every phase.

### 11.4 Colin's Response: Reinforcement-Based Confidence

Colin proposed a practical confidence framework:

> "When we say confidence, all that really means is that the agent has done a good thing repeatedly, consistently, a number of times. And the human is given a green light for those number of times."

The model:
1. **Heavy human-in-the-loop initially** -- humans review everything
2. **Positive reinforcement** -- agent builds a record of correct outcomes
3. **Threshold-based autonomy** -- after enough positive confirmations, human steps back
4. **Exception-based re-engagement** -- human re-enters only when agent makes mistakes
5. **Human expertise for course correction** -- agents should never self-assess or assess each other ("They have this very oscillating behavior where they either go very, very overwhelmingly positive [...] or polar opposite, everything's awful")

---

## 12. Upskilling Challenge

### 12.1 The Problem

Vaibhav flagged upskilling as a separate challenge beyond the COE platform work:

> "Speaking of upskilling too, that's another problem. [...] We need talented people across the board, not just creating or working on the platform, which is from pure user perspective, how to use this technology to deliver business commitments."

Two dimensions:
1. **Building the platform** -- creating agents, infrastructure (COE team)
2. **Using the platform** -- enabling all QE staff to effectively orchestrate agents

> "You are not just creating agents. You have to be solid enough to be able to use and orchestrate between these agents to deliver the right outcome."

### 12.2 Offshore vs. Nearshore Gap

> "I have these two facts that are very true today. [Offshore is] not upskilling at the same speed as the nearshore."

Vaibhav sees offshore talent lagging in AI upskilling, creating a potential nearshore opportunity for BayOne.

---

## 13. Staffing and Talent Signals

### 13.1 Current Budget Holders

Vaibhav named several people with budget authority or project needs:
- **Deepika** -- COE team, actively hiring
- **Ashweta** -- mentioned as having staffing needs
- **Lakshmi** -- mentioned as having staffing needs
- **Priyanka** -- mentioned as having staffing needs
- **CDW project** -- would require entirely different team composition ("It's not going to be our existing credit card team doing it")

### 13.2 What Vaibhav Looks For in Candidates

His hiring philosophy is strongly anti-resume, pro-conversation:

> "It's the communication that we'll have. Anybody can create a catchy resume. A lot of these resumes, we've just started conversing and said, yeah, thank you. You can tell."

> "I always put them on the whiteboard. Simple problem. It's actually nothing related to Java or anything. I'm not testing that. This is a common problem. Tell me what you're thinking. That's it. [...] I don't care whether you solve it or not. [...] I just want your mental attitude. Your approach to the problem. That's all."

### 13.3 Geographic Preferences

Current state and trajectory:
- **Majority of workforce is offshore** today
- **Near-term opportunity** exists on the offshore side
- **Medium-term (6-12 months)**: positions likely migrating to nearshore (South America, Canada)
- **Longer-term**: onsite presence likely to increase
- **Onsite is "always a premium"** -- limited room, only for exceptional candidates
- Remote onshore (non-Bay-Area, Central/Eastern time) is viable at nearshore-competitive rates

---

## 14. Key Technical Details and Requirements

### 14.1 Infrastructure Stack
- **Microsoft Azure** -- cloud platform (Vaibhav set this up himself)
- **Selenium** -- current automation framework (legacy)
- **Playwright** -- target automation framework (POCs done, new work happening here)
- **LiteLLM** -- foundation for Nova platform
- **MCP servers** -- required integration pattern for all new tooling

### 14.2 AI Models in Use
- **Claude** -- adopted as primary AI tool (post-DataIQ)
- Platform progression: DataIQ -> Advent (with Claude) -> Nova (homegrown)

### 14.3 Organizational AI Infrastructure
- **Nikhil** -- leads MCP and DevOps team, building Nova
- **Deepika** -- leads QE COE (~5 people)
- **Vaibhav** -- oversees QE broadly, 10-11 QE leads

---

## 15. Open Questions and Unresolved Points

1. **What exactly is Advent?** -- Vaibhav mentioned it as the platform they moved to after DataIQ. Could be a transcription artifact. Needs clarification.

2. **DataIQ identity** -- Is this Dataiku, or another platform? The name appears clearly in the transcript but no further detail provided.

3. **Nova timeline** -- When will the migration from Advent/Claude to Nova happen? Vaibhav says "we will now, again, look at migrating" but no dates given.

4. **AMP model status** -- Is AMP already deployed, or in transition? Vaibhav says "we are moving to" suggesting it's in progress, not complete.

5. **Selenium migration scope** -- How large is the existing Selenium test suite? What is the migration timeline? Only "POCs complete and new development on Playwright" was stated.

6. **Mobile farm specifics** -- "Looking at setting up mobile farms" but no details on scope, tooling, or timeline.

7. **Deepika's hiring status** -- Multiple candidates sent, none confirmed hired. Vaibhav uncertain: "Filled them or not, I don't know yet."

8. **CDW project** -- Mentioned briefly as requiring a "completely different" team. No elaboration on what CDW is or its timeline.

9. **Trust index methodology** -- Vaibhav acknowledged wanting to compute a trust score ("4.8 out of 5") but admitted "How do you compute 4.8? I don't know." This is an unsolved problem for him.

10. **"1.11" reference** -- When describing DataIQ, Vaibhav said "after going through 1.11." Unclear if this is a version number, iteration count, or transcription artifact.

11. **Common knowledge base implementation** -- The vision is clear (shared knowledge across dev/QE/other functions) but implementation details are absent. What platform? How does it integrate with Nova?

---

## 16. Relationship Dynamics and Sales Context

### 16.1 BayOne's Position

BayOne already has multiple active relationships at Sephora:
- **Mani's team** -- PWA modernization conversation
- **Ravi Pandey** -- active engagement, found a "purple squirrel" candidate
- **Andrea with Girishi** -- active engagement
- **Deepika** -- candidate pipeline for COE roles

### 16.2 Colin's Pitch Points

Colin positioned BayOne's QE capabilities around several themes:
- **Deterministic-first, AI-last philosophy** -- "Bring in AI last as a rule"
- **State graph approach** -- autonomous mapping of codebase for dependency/coverage analysis
- **CI/CD integration** -- state graph plugs into pipelines for change-aware testing
- **Multi-model flexibility** -- Claude 90%, Gemini for visual, OpenAI rarely
- **Observability and transparency** -- agent monitoring, traceability
- **Upskilling training** -- both for new BayOne hires and client teams

### 16.3 Vaibhav's Receptivity

Vaibhav was receptive but non-committal on specific engagements. His stance:

> "I'm open, hey, give me a good... if you're talking about just a resource, give me a good resource, I'll find the right role for that guy."

He is talent-first, role-second: "If there is a star performer, you'll find the place for them."

### 16.4 Outcome-Based Work

Colin pushed for outcome-based work (project-based, not just staffing). Vaibhav's response was that there is no defined North Star target, making it hard to scope an outcome-based engagement. The door remains open but undefined.
