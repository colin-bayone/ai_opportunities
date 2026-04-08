# 03 - Meeting: Next Steps and Demo Demand

**Source:** /sephora/edw_modernization/source/andrew-girishi-meeting1_formatted.txt
**Source Date:** 2026-03-05 (Andrew/Grishi Meeting)
**Document Set:** 03 (Andrew/Grishi Meeting)
**Pass:** Focused deep dive on next steps, demo requirements, and engagement logistics

---

## 1. The Demo Demand: Two Independent Asks

The most consequential outcome of this meeting was that both Andrew and Grishi independently demanded a demo or proof-of-concept before committing to any engagement. This was not a coordinated request -- each came at it from a different angle and with different motivations, which makes the signal stronger.

### Andrew's Framing

Andrew framed his ask around validation that the agentic concept is feasible given Sephora's actual constraints. His concern was not theoretical -- he wanted proof that the concept works with old software versions, real connectivity challenges, and the end-to-end flow (not just SQL conversion).

**Key statement (line 512-513):** "I think we want to make sure that this concept of, you know, all those little multiple little agents and have an orchestrator kind of, you know, orchestrating the entire flow, is it possible?"

**Key statement (line 514-517):** "Why I'm asking that is because not just, I understand that everything is possible right now, right? With all this AI out there, but because of our version of the software, for example, Cognos that we have is a very, very old version... And it's super old version. Data Stage, it's not the latest version either."

**Key statement (line 518-522):** "What I don't know is whether... either this software has an open SQL Server... that you can just easily have the AI to go with, or it has an API endpoint or some sort. Otherwise, your agent... it can be as smart as you can be. It won't be able to connect to that software. Then it's moot point, right?"

Andrew's core question was whether agent integration with legacy on-premises software is even technically possible. He explicitly flagged Cognos (version 10.2 or 10.3) and DataStage as the systems of concern. He was not asking for a polished presentation -- he was asking for proof of connectivity.

**Key statement (line 528-529):** "I just want to make sure that the version and I feel comfortable that yes, the wild thinking is not wild, it's real, it can be done."

**Key statement (line 530-531):** "YouTube guys is absolutely capable of delivering that, knowing that our software version is old, knowing that, you know, understand the flow, it's not just converting the... making sure the report will work as is, but also the data behind the scene."

Andrew wanted two things validated: (1) that the concept of an orchestrated agent swarm for EDW migration is not aspirational fantasy, and (2) that BayOne specifically can execute it against Sephora's legacy stack. He was explicit that he did not care whether the demo used Sephora's data or synthetic data -- he just needed to see it working.

### Grishi's Framing

Grishi's ask was different in character. She was less concerned with theoretical feasibility and more concerned with demonstrated capability. She and her team had already been using Claude for SQL conversion and achieved approximately 30% efficiency gains, so she understood what AI could do in isolation. What she had not seen was an orchestrated multi-agent system performing the end-to-end flow.

**Key statement (line 488-491):** "For me, I loved what you presented today, right? But it would really help me if we could see some kind of a demo or, like, agents that you guys have created or, you know, that has done this kind of job, be ingestion automated this stuff, right? That will help us and give us the confidence that, oh, these guys have already done something like that, to see it actually working."

**Key statement (line 581-583):** "I just want to see before we go and spend a lot of time, I wanna see that you guys have done something like this, that done created agents that is capable of doing these kind of things, right? So I think that's something very selfishly, very important for me."

Grishi wanted to see agents in action. Not slides, not architecture diagrams, not case study documents -- a working demonstration. She was protecting her team's time: before investing in a deep technical engagement with BayOne, she needed evidence that BayOne had actually built agent systems of this type.

### The Difference Between the Two Asks

Andrew's ask was about **feasibility**: can this be done with our old systems? Grishi's ask was about **capability**: have you actually done this before? Both had to be answered before either would commit. This dual demand is what drove the demo/POC becoming the critical next gate.

---

## 2. Colin's Three Options for Building Confidence

When Grishi asked to see a demo, Colin immediately acknowledged the constraint that he could not show client work, then offered three distinct options. This was a well-structured response that gave Sephora choices rather than a single take-it-or-leave-it.

**Key statement (line 492-493):** "I'll give you three options for this one. Because this is tough."

**Key statement (line 496-497):** "I'm a graphic designer, but I can't show you what I worked on because it belongs to someone else. So we're still in that boat here."

### Option 1: Case Studies

**Key statement (line 498):** "Number one, case studies."

Written documentation of prior engagements where BayOne built similar agent systems. This is the lowest-risk option but also the lowest-impact for Sephora's decision-making, as it provides no live proof.

### Option 2: POC on Sephora's Actual Data

**Key statement (line 499-503):** "Number two, we can do a POC. So if we can have some representative sampling of something, we can just do it live for you on your own data as a POC. And that can actually feed into, if there's a scope of work or anything like an SOW, that can be a part of it. So you're not duplicating effort. There's nothing lost there. And if you don't like it at the end, well, you got something for free out of it."

This was Colin's preferred option because the POC work rolls directly into the engagement. Nothing is wasted. If Sephora provides representative data, BayOne builds agents against it, and whether or not the engagement closes, Sephora gets something tangible. Colin framed this as zero-risk for Sephora.

### Option 3: Demo on Synthetic Data

**Key statement (line 505-508):** "The third is we could show you with a representative sample from what we understand. So we could demo this on our own data, probably just some data that we put together, just to show you how it would work. That's the safest option, but there is kind of no value add. So there's like whatever time we sink into that doesn't directly contribute to the time that we would have to take to do it for real."

Colin was transparent that this option is the safest but least efficient: the demo effort does not translate into real engagement work. He flagged the trade-off explicitly rather than overselling the option.

### Outcome

The group effectively converged on a hybrid of Options 2 and 3. Andrew stated he did not care whether it used Sephora's data or synthetic data (line 528). Grishi said "it could be on your data, right?" (line 581), signaling she was open to synthetic data as long as she could see agents in action. The demo was planned with BayOne-constructed data showing agents performing the types of tasks Sephora needed.

---

## 3. Grishi's Databricks Preference

Grishi explicitly stated that her ideal environment for the POC was Databricks, the same platform Sephora is migrating to.

**Key statement (line 593-594):** "I do ideal would be like my ideal would be Databricks, right? I don't want to add too many things if you have it on Databricks, but again, like you will have your own tools I'm guessing."

Colin was honest that he could not guarantee Databricks for the POC specifically, but offered the equivalent.

**Key statement (line 595-598):** "So I can't promise that one. Not for POC, but I can at least give you the equivalent. Databricks wouldn't like me saying that it's similar to Snowflake, but in a lot of places it is. So we can at least show you with a simple version."

This exchange matters because it sets a baseline expectation: Grishi wants to see the agents working in an environment that is as close to Sephora's production stack as possible. The eventual demo or pilot would carry more weight if it ran on Databricks rather than a substitute.

---

## 4. The Deep Dive Technical Session Plan

Andrew proposed a follow-up technical session before the proposal, and laid out specifically what it should include.

**Key statement (line 570-574):** "We're going to put together, probably we have maybe one more just to kind of give that session in terms of architecture. And even, you know, Grishi has an enterprise architect working for her right now that have been laying out architecturally, in terms of the data migration, right? You know, how what Databricks tools that we're going to use, how it's going to work, how the whole mapping work, I think it would be good kind of a 30 minutes or not, like a conversation just to show what we have, how we plan to go about it. And then that will give you guys more information, right, then can go back and digest and then maybe then propose."

### Who Would Attend

Andrew referenced Grishi's enterprise architect. In the transcript, this person is rendered as "my hair" (line 619), which is almost certainly **Malika** -- the enterprise architect who becomes the primary technical contact in Set 04.

**Key statement (line 618-619):** "And then for the deep dive, who is the architect that you wanted to include in that? My hair, and I'll send that person's name as well."

Grishi committed to sending the architect's name and contact information for scheduling.

### Purpose of the Deep Dive

The deep dive was designed to serve both sides:
- **For Sephora:** Show BayOne the actual architecture, the Databricks tooling decisions, the mapping methodology, and the migration plan so that BayOne would have enough context to build a credible proposal.
- **For BayOne:** Get the technical depth needed to scope realistically, understand the integration challenges (especially the legacy Cognos and DataStage versions), and identify which tracks or domains would be best suited for a pilot.

Colin added one more request for the deep dive (line 577-578): "If there's a priority ranking of things that would be, even from our concerns perspective, or things that we'd like to be done as pain points or deliverables perspective, that'd be super helpful. Because we could take this in a lot of different directions, but I want to make sure whatever we're doing is definitely aligned with what you want to see."

This request was for a prioritized list of pain points so BayOne could target the proposal precisely rather than covering everything broadly.

---

## 5. The Three-Tier Engagement Model

Colin restated Mani's previously requested three-tier proposal structure, framing each tier clearly for Andrew and Grishi. This ensured all stakeholders had the same understanding of the options that would be proposed.

### Type 1: Full Outsource

**Key statement (line 455-456):** "One, where you're pretty much doing this ourselves. We give you a big chunk of work, we give you requirements, you deliver on it, and that's that."

BayOne takes ownership of an entire track or workstream. Sephora provides requirements and acceptance criteria; BayOne delivers independently. This is a turnkey model.

### Type 2: Partner Model (Colin's Preference)

**Key statement (line 457-462):** "Type two, which to me is the best type, and I think the healthiest type, even from an org standpoint, is kind of a partner. Where we're doing a lot of the work, we're taking care of that AI load, but we're also at the same time kind of working alongside your team to help them understand what we're doing. So we're not doing this in a vacuum, there's not secret sauce to this. It's you're kind of getting people that are now upskilled as a result."

Colin was explicit that this was his preferred model. The reasoning: BayOne does the heavy AI work, but Sephora's team gains knowledge transfer. BayOne benefits because they have embedded collaborators who understand the business context. Sephora benefits because they are not left dependent on BayOne after the engagement ends.

**Key statement (line 461-462):** "It's not meant to be something that takes up 50% of people's time, but it's just in general, it's not in isolation from us."

### Type 3: Pure Staffing (Colin's Least Preferred)

**Key statement (line 463-464):** "In type three would be pure staffing, where we just hand you off people that we know can do the work. That one is my least favorite because I can't control that."

Colin used a sports analogy to illustrate the risk (line 465-469): even the best team can fail without clear direction. He was candid that once BayOne hands off staff, the outcome depends on Sephora's management of those individuals, and that introduces risk BayOne cannot mitigate.

### Why This Matters

By restating the three tiers in this meeting, Colin ensured that Andrew and Grishi heard the options directly from him, not filtered through Mani. This also allowed Andrew and Grishi to start forming their own preference before seeing the formal proposal.

---

## 6. Andrew's Vendor Transparency and Competitive Context

Andrew was unusually transparent about Sephora's vendor evaluation process. He stated plainly that BayOne was not the only party in the conversation.

**Key statement (line 172-173):** "Again, I'm just going to be very transparent, right? We have been talking this exact same conversation with a lot of different vendors right now."

**Key statement (line 174-176):** "Because I know for a fact, right now outside there's no, no one has a pre, a package that we can just say, hey, I want to buy your package... so I can just run through this migration without any human involved or even a little human involved."

**Key statement (line 176-177):** "So now I'm just kind of poking a hole and saying, who out there can help us to create this potential package with multiple agents and with a master agent orchestrating the whole thing?"

### What This Signals

1. **Sephora is actively shopping.** This is not a courtesy conversation -- they are evaluating multiple vendors for the same work.
2. **No one has a pre-built solution.** Andrew acknowledged that a commercial off-the-shelf agent orchestration package for EDW migration does not exist. This levels the playing field: every vendor will have to build custom.
3. **The selection criterion is capability to build.** Since no package exists, the vendor who wins is the one who most convincingly demonstrates they can build the agent swarm. This is why the demo/POC demand is the critical gate.
4. **Andrew is giving BayOne a fair shot.** His transparency was a courtesy -- he could have kept the competitive landscape private. By sharing it, he was also implicitly saying: impress me and you have a real chance.

### Colin's Response to the Competitive Pressure

Colin did not react defensively to the multi-vendor disclosure. Instead, he leaned into flexibility.

**Key statement (line 437-439):** "No, I'm not going to force us to you guys. I know, like you said, you're talking to multiple people. What we can do is we can kind of grow with your appetite."

**Key statement (line 447-450):** "We could start out small because I think with a project this big, there's enough room at the table. So even if you want to continue exploring other vendors, that's fine, and we could do a small-scope thing for you to start with. And if you like that, we continue. If you don't, it's less of an investment for you."

This was a deliberate de-risking pitch: BayOne does not need to win the whole engagement at once. They can earn their way in with a small-scope proof point. This directly addresses the competitive pressure because it asks Sephora for minimal commitment while other vendors are likely pitching large engagements.

---

## 7. Scheduling and Logistics

### Demo Timeline

The demo was targeted for the following Thursday. Zahra drove the scheduling.

**Key statement (line 603-604):** "We're going to put together a demo for you. Colin, do you think, how much time do you think you'll need?"

**Key statement (line 605-606):** "I will need, so I'm traveling this week. I'm going to leave tonight. I will be back next week."

**Key statement (line 612-613):** Andrew confirmed availability: "Wednesday could work, Wednesdays, Thursdays."

**Key statement (line 617):** "Let's aim for next Thursday, share your availability, so we'll get that on the calendar."

### Deep Dive Session Timeline

The deep dive with Grishi's enterprise architect (Malika) was also scheduled for the following week, as a separate session from the demo.

**Key statement (line 620-621):** "We'll schedule that sometime next week as well, so leave the coordination up to us."

### Coordination Owner

Zahra took ownership of all scheduling coordination.

**Key statement (line 621-623):** "We have a timeline now, so we'll act upon that. You'll have access to Colin as well in case anything else comes to mind."

---

## 8. Colin's Framing of Scalability

A critical selling point Colin made during the next-steps discussion was about the economics of the agent approach at scale.

**Key statement (line 474-479):** "The great thing about these is they scale independent of people. So once we have the agents going, that's one of the strongest parts about them. We still need people to do the work. But the more and more we scale the agents, the less and less we need. So the work to take on 100 tables or 100 different reports is about the same as if we were to do 1,000. Because once we have that initial structure in place, this scales naturally."

This directly addressed Andrew's vision of shrinking the three-year program timeline. Andrew had earlier articulated the hope (line 169-170): "Then this program can potentially shrink from, I don't know, three years, all the way to maybe a year or a year and a half, or something like that." Colin's scalability argument reinforced that this was achievable once the agent infrastructure was built.

---

## 9. Colin's Response to the Legacy Software Concern

Andrew's concern about whether agents could even connect to old Cognos and DataStage was a potential deal-breaker. Colin addressed it directly.

**Key statement (line 534-536):** "The good news with older software, to be honest with you, is the same reason why it gets old is because I shouldn't say it like this, but I will. It's easier to get into older software. That's the most professional way I can say that."

**Key statement (line 537-538):** "So the reason why we go to a different version, yes, new features, but primarily because there's also a lot more security built in."

**Key statement (line 547-551):** "The more time passes and the more people use that. You have tools, they might be legacy, but they're not out of the ordinary. They're a fairly normal stack. Maybe they've dated a little bit now in their versions, but the more normal things are, the more support there is, the more likely it is that someone already has made a connector or that we can go back and get an existing connector."

He also drew a distinction (line 552-553): the scenario would be different "if you said we had an on-prem thing that our in-house team developed themselves and then didn't look at for 15 years." Cognos and DataStage are commercial products with known interfaces -- that is fundamentally easier to integrate with than custom-built systems.

His one caveat was around production impact (line 554-557): "My only concern would be on speed. And if those things are in production or if they're kind of a staging server, because I also wouldn't want to kill the server if it's production and you need that data to do some business function. And I'm querying it a million times with an agent."

---

## 10. Complete Action Item Summary

### Immediate Actions (Week of 2026-03-05)

| # | Action Item | Owner | Timeline | Source |
|---|-------------|-------|----------|--------|
| 1 | Prepare demo showing agent orchestration capability | Colin / BayOne | By next Thursday (~2026-03-12) | Lines 603-617 |
| 2 | Send email with availability for demo and deep dive | Zahra | Immediate | Lines 615-617 |
| 3 | Send enterprise architect's name and contact info | Grishi | Immediate | Line 619 |
| 4 | Schedule demo session (target: Thursday next week) | Zahra | Within days | Lines 613-617 |
| 5 | Schedule deep dive technical session with Malika | Zahra | Next week | Lines 618-621 |

### Deep Dive Session Requirements

| # | Item | Owner | Source |
|---|------|-------|--------|
| 1 | Present current architecture and Databricks tooling decisions | Grishi / Malika | Lines 570-574 |
| 2 | Show how the migration mapping currently works | Grishi / Malika | Lines 572-573 |
| 3 | Provide priority ranking of pain points or desired deliverables | Andrew / Grishi | Lines 577-578 |

### Post-Demo / Post-Deep-Dive Actions

| # | Action Item | Owner | Source |
|---|-------------|-------|--------|
| 1 | Digest technical information from deep dive | Colin / BayOne | Lines 573-574 |
| 2 | Develop proposal with three engagement tiers | Colin | Lines 454-472 |
| 3 | Scope the proposal appropriately (can start small) | Colin | Lines 447-450 |
| 4 | Include POC or demo results as confidence evidence | Colin | Lines 499-504 |

---

## 11. What This Meeting Set in Motion

This meeting was the pivot point between introductory conversations (Sets 01-02 with Mani) and the technical engagement phase (Set 04). Specifically:

1. **The demo demand created urgency.** Both Andrew and Grishi required a working demonstration before proceeding. This forced BayOne to move from conversation to construction within one week.

2. **The deep dive session with Malika was agreed upon.** This directly produced the technical deep dive captured in Set 04, where BayOne would see Sephora's actual architecture, tooling, and migration methodology for the first time.

3. **The competitive landscape was revealed.** Andrew's transparency about multiple vendors meant BayOne knew they were in a competitive evaluation. The demo was not just a confidence-builder -- it was an audition.

4. **The engagement model was pre-socialized.** By restating the three-tier model (full outsource, partner, staffing) in front of Andrew and Grishi, Colin ensured the eventual proposal would not be a surprise. All decision-makers had heard the options.

5. **The "start small" offer was planted.** Colin's willingness to begin with a limited scope, even while Sephora continued evaluating other vendors, reduced the decision risk for Sephora. This made it easier for Andrew and Grishi to say yes to a next step without committing to a large engagement.

6. **The infrastructure question was answered.** Colin committed to building on Sephora's infrastructure (Databricks, their cloud accounts, their enterprise AI licenses), which removed the concern about introducing additional tools or vendor lock-in.

The sequence this meeting initiated: demo (prove capability) followed by deep dive (understand the real architecture) followed by proposal (scoped to what was learned). Each step was designed to build incrementally on the prior one, with Sephora able to exit at any point without sunk cost.
