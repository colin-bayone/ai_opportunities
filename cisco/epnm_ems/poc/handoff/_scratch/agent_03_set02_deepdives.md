# Agent 03: Set 02 Deep-Dive Extraction (2026-02-20)

Source files extracted:

1. 02_meeting_problem_definition_2026-02-20.md
2. 02_meeting_domain_gap_and_quality_assurance_2026-02-20.md
3. 02_meeting_engagement_model_and_constraints_2026-02-20.md
4. 02_meeting_poc_scope_and_success_criteria_2026-02-20.md
5. 02_meeting_next_steps_2026-02-20.md

Participants: Guhan (Cisco engineering leadership), Selva (Cisco technical lead on EMS), Colin Moore (BayOne, Director of AI).

---

## 1. Problem Definition (as of 2026-02-20)

Source file: 02_meeting_problem_definition_2026-02-20.md

### The Two Products

Guhan opened by defining both products:

> "We have two products, one is the legacy one, which is called EPNM, and a modern version of that, the microservices based, is called the Element Management System."

EPNM is the legacy product. Customers have used it for 15+ years:

> "Some key customers who still believe that they're used to this legacy UI, which they have used it for 15 years or whatnot, right? They want to keep the same UI for their operations."

EPNM domain: network management, network inventory, network topology, and the full customer lifecycle of automation that begins with element management. Guhan stated:

> "These are all basically managing the network inventory, network topology, the entire, the customer's life cycle of automation starts with this element management."

EMS is the modern replacement. Microservices-based. Cisco invested approximately two years building it with a new UI:

> "We have invested, spent, and then after two years we have built the [new] UI."

EMS is the direction Cisco still intends to go:

> "We had developed the product, the later version of product with the new UI, modern UI and everything we thought this is where we wanted to go and we're still moving in the direction."

EMS is what Cisco will pitch to newer customers. EPNM is intended to be retired:

> Guhan: "The idea is to move all the customers from EPNM into EMS. We need to move those guys here."
> Selva: "As a product, we are going to retire that."

Final product strategy (both UIs coexisting permanently vs. one replacing the other) has not been decided and is left to product managers.

### The Two Architectures

EPNM is monolithic. Selva:

> "It's tightly coupled to, like, as a model, it's not microservices. It's all, like, we really need to borrow things and bring it in."

The coupling is structural (monolith-level), not feature-to-feature. EMS is microservices.

### Technology Stacks

- Backend: Java in both products.
- EPNM frontend: primarily Dojo with minor Angular presence. Selva: "It's all JavaScript and Dojo kind of thing."
- EMS frontend: entirely Angular.

### Why Direct Code Porting Does Not Work

Guhan:

> "One approach is let's take all that [EPNM code] running here. It won't run directly because these two are two different architectures. One is microservices based, other is different and we have even done a lot of surgery on the older core, so they won't run as easily."

Three reasons:

1. Architectural mismatch (monolith vs. microservices, different deployment, communication, state, data access assumptions).
2. "Surgery" has already been performed on the EPNM core, so the legacy code is not in its original form.
3. If it were easy, it would already be done: "Otherwise, we would have solved it by now."

### The Vertical Nature of Functionality Gaps [SUPERSEDED BY SET 03]

This is the framing that was later reversed. Selva, in response to Colin's question about whether remaining work was primarily frontend or backend:

> "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

Reinforced:

> "It's not a UI alone. There is a, I mean, along with it comes the backend logic only then [it works]. This is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

And:

> "We can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new. And then make it work end-to-end, right? So that will be the goal for this exercise."

**SUPERSEDED BY SET 03:** Set 03 (2026-03-25) reversed this framing. The POC is now scoped as a frontend-only "classic view" toggle on two EMS screens (Inventory and Fault Management), with the backend unchanged.

### Already Done vs. Remaining [SUPERSEDED BY SET 03 in how it applies to the POC]

Some functionality has already been converted into EMS, with a redesigned UX:

> Selva: "There are some screens we have already brought in functionality with a new idea."
> "In some cases, we also went through a new UX design and the user experience. I mean, some areas it turned out to be [positive], some areas it's not."
> "I think the feedback in some cases was, can I get the same experience? So that's where we are looking into this one."

The Set 02 POC direction was to target remaining, not-yet-converted functionality (missing reports was the specific example). **SUPERSEDED BY SET 03:** the POC now targets adding a classic-view toggle to already-converted EMS screens, not net-new missing screens.

### Customer Demand for Identical Legacy Experience

Guhan:

> "They want to keep the same UI for their operations. Because otherwise, they have to learn. Network operators have to learn. They don't want to invest and go and do all those things."

Framed as multi-customer demand, not isolated: "This is something that many customers are asking for, going back to the, let's call it legacy UI."

Required fidelity:

> "From a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything, the way they would do, interact with the [EMS], same as what is there [in EPNM]."

Decomposed: same experience (workflow and interaction), same visualization (visual rendering), same operations (functional capabilities), backend transparency (customers do not know what runs behind).

### The Decision Already Made

> Guhan: "One decision that's made is the EPNM UI, the older UI needs to exist, that has to be given to the customers, customers need to, will be happy to use that."

The EPNM-style UI must be available in EMS. The question is how to deliver it, not whether to deliver it.

### Scale of the Conversion [PARTIALLY SUPERSEDED BY SET 03]

Guhan: "There are like 70, 80, 100 pages." (First meeting referenced ~200 screens; the relationship between counts is unresolved.)

Guhan: "We do not [expect] everything to be converted."

The real Set 02 deliverable was an estimation methodology: if 10 screens take X days, extrapolate. **SUPERSEDED BY SET 03:** POC is now two specific screens (Inventory, Fault Management), not a representative-sample estimation exercise.

### Code Health and Documentation

Feature-to-feature coupling may not be severe, but monolithic coupling is. Selva: "we really need to borrow things and bring it in."

Documentation, from Selva:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

Colin: "For the most part, especially with anything legacy, almost always is missing documentation... Because documentation doesn't always tell the truth."

### The Engineering Challenge (Guhan's Framing) [SUPERSEDED BY SET 03]

> "The challenge for you, that you can choose to accept, is basically can you take that [EPNM code], provide a working code, show us the demo, taking some of the [screens] on the backend of the EPNM, run it in the [EMS]. So from a customer point of view, they don't know what is running behind and everything."

Decomposed: take EPNM code, produce working code, show a demo, include backend, run it in EMS, customer cannot tell. **SUPERSEDED BY SET 03:** backend is no longer in scope; the POC is a frontend toggle.

### Justification for AI

Guhan: "I just [want to] use AI because this entire thing is a work that we didn't anticipate so but it's important for let's say product."

> "The team is also on critical [work] or a platform, if you think so, the team itself will not be able to [dedicate] time here."

Unanticipated work, engineering cannot be pulled off existing commitments, AI-assisted conversion is the mechanism.

### What "Conversion" Meant in Set 02 [SUPERSEDED BY SET 03]

Multi-layered: identify EPNM screen, trace the vertical slice (UI, API, backend, data), extract from the monolith, reimplement in EMS architecture (backend microservices, Angular UI, data flows), preserve the user experience, validate end-to-end. **SUPERSEDED BY SET 03:** the POC is a frontend-only toggle; no extraction, no backend reimplementation.

---

## 2. Domain Gap and Quality Assurance

Source file: 02_meeting_domain_gap_and_quality_assurance_2026-02-20.md

**This material still applies.**

### Guhan's Question

Guhan pressed on completeness in an unfamiliar specialized domain:

> "How do you try to [bridge] the [gap] for the domain level thing, right? So because, obviously, these projects are in various domains that you've taken up, right? And this one is in element management. And how do we ensure that there's no [gap] in what we bring over, right? I mean, this may not have the readily available prior [knowledge]."
> "How do you make sure that there's no domain gap or no functionality gap?"

Layered concerns embedded in the question:

1. Domain specificity: element management is niche, not generic web application work.
2. No readily available prior knowledge for BayOne or LLMs to draw on.
3. Completeness assurance against unknown unknowns (not "can you do it" but "how do you guarantee you haven't missed something").
4. Implicit vertical-code concern: missing functionality goes all the way down the stack.

### Colin's Four-Layer Response

**Layer 1: The Judge Agent**

> "The judge is the one that takes care of making sure that the actual conditions are met."

Key points:

- Judge functions as a quality enforcement personality within the agent swarm.
- Agents have "almost like personalities because that's almost how they function." The judge personality is adversarial to the work being produced.
- The judge does not merely rely on existing tests: "Rather than just relying on unit tests or any existing test scripts even, those are things that if they're identified as gaps, even if we already have tests written, maybe we need new tests. Maybe there's not some written that should have been written in the past."
- Meta-analysis of what should be tested, not just whether existing tests pass.
- Colin acknowledged architecture shift inherently creates testing gaps: "Especially with shift to new architecture, that's definitely going to be there, I know."

**Layer 2: Automated Visual Testing (Playwright)**

> "From a visuals perspective, we can definitely have that already, but that's what we have the automated inspection tools. So it uses Playwright for the most part."

Details:

- Screen capture comparison. Colin: "doing screen capture things, even as we're doing it." (Transcript renders as "screen graph" due to speech-to-text error.)
- Does not require a running application: "We don't even need to have the application running. We can just have certain screens loaded up with data, make sure that we can check the functionality there." Important because running instances were not immediately available.
- Automated even at small scale: "So even in a small way, we're able to do that automated, which is nice."
- Pre-offered as a precursor to formal testing: "If you want us to be able to test and guarantee the UI, part of this is also the testing of it to make sure that it has faithfully been converted. We can do the automated UX testing as well, even if it's a precursor to formal UX testing from your team, but that can save you some time too."

**Layer 3: Continuous Gap Analysis and Peer-to-Peer Agent Communication**

- "Other perspective with functionality, it's just a matter of going back and looking over and over and over again, both during development and at the end, to see if we missed anything."
- "There's kind of a constant gap analysis that goes on here."
- "That's why the agent swarms are great, because there's peer-to-peer communication between them."
- "If a gap is noticed, either another agent spawns to go and address that gap, or it informs something that's already running, but hey, you need to stop, pivot, and make sure you take care of this before anything else."
- "So they self-manage."

Reactive system: gaps discovered by one agent are communicated to others, which can spawn new agents or redirect existing work.

**Layer 4: Human Final Review**

> "But the final line of defense is us. So at the end of it, we still have to, as humans, go and review this, do it ourselves. That's where we can catch things that were missed."

### The Categorical Gap Insight

Colin's most important QA claim:

> "Usually what I found with this, if anything's missed, it's categorical. It's not like it's a little small thing that can slip through the cracks. It'll be a whole category of something that would get missed. So that's why we always do the final quality check."

Implications: AI agents do not tend to miss small individual details; they miss entire categories. Human review is tractable because reviewers check category-level coverage, not line-by-line. A domain-knowledge gap would manifest as an obviously missing section.

### The Documentation Position

Selva:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

Colin:

> "For the most part, especially with anything legacy, almost always is missing documentation. It's way easier to do it now, so we're kind of modern day cheating. It's much easier now."
> "Documentation doesn't always tell the truth."

Colin described append-only discovery documentation: "Documentation is actually a big part of the discovery so that we don't have to do the same work twice. So it's kind of like a... almost a blockchain documentation style. So as we continue to explore the code, we will find this knowledge, but we keep what we learned in the past."

### Agent Architecture Context (as described)

Phase 1 (Claude Code): initial exploration, "bringing one soldier to it," pattern understanding, game plan gathering.

Phase 2 (LangGraph multi-agent swarm): "bringing the army approach," models real-life teams. Roles:

1. Master Architect: strategic planner.
2. Engineer: translates architectural direction into implementation plans.
3. Foreman: manages execution, spawns sub-agent workers.
4. Judge: keeps everyone in line, validates output.

Capabilities mentioned: automated regex pattern finding (transcript renders "rejects"), prototyping, documentation generation, peer-to-peer communication, dynamic sub-agent spawning, autonomous gap detection and redirection.

### Open Items Flagged in Source

- Colin did not explicitly answer how agents or team would acquire domain knowledge itself; implicit answer is that code is the domain knowledge.
- Categorical gap detection depends on knowing all categories; who defines the complete category list was not addressed.
- Mechanics of Playwright testing without a running application were left vague.
- Full QA framework is a property of LangGraph swarm; during initial Claude Code exploration the full system is not available.
- Guhan did not push back or ask for clarification; his level of comfort is ambiguous.

---

## 3. Engagement Model and Constraints

Source file: 02_meeting_engagement_model_and_constraints_2026-02-20.md

**Much of this still binds.**

### Engineering Team Bandwidth: Zero

Guhan:

> "At the moment the team is also on critical or a platform, if you think so, the team itself will not be able to miss time here. But of course, they need to give you the context and everything. They will provide you with that."

Three parts:

1. Team is on "critical platform" work (core EMS microservices platform).
2. Team cannot invest time on EPNM conversion. Not willingness; committed elsewhere.
3. Team WILL provide context. Context transfer is obligation; execution is BayOne's.

Practical: no engineering pairing, no embedded collaboration, no ongoing Q&A. Model is: receive context dump, go away, return with results.

### Independent Execution After Context Transfer

Guhan: "And then if you can take that independently and come back with your analysis and put that up with what you've come up with, that would be good."

Selva (paraphrased): "Hopefully, you'll be able to, once we get the context right, you'll be able to move ahead on your own to do this analysis and come back."

Colin: "We don't need too much of their time, I promise. I think this is straightforward as soon as we can get our eyes on the code."

### Periodic Checkpoints

Guhan: "We'll have periodic checkpoints to help clarify anything more and also keep the rest of the folks average with the progress."

("Average" is speech-to-text for "apprised.") Two purposes: clarification and visibility. Cadence, format, and attendees were not defined.

### Code Access

Confirmed. Colin asked, Guhan confirmed: "Yeah, we need to provide you with access to things."

Entails: EPNM codebase (Java + Dojo/JavaScript), EMS codebase (Java + Angular), via Cisco's internal VCS, on Cisco hardware through Cisco infrastructure. Blocked at the time on Cisco laptop and Cisco ID.

### No Design Documentation for Legacy

Guhan:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view. Most of it. That will be the bulk of the challenge here."

Implication: no design documentation. Code IS the documentation. Navigating the code is "the bulk of the challenge." Initial context transfer must be verbal, architectural walkthrough, or engineer-guided code tour.

### Security Constraints: All Work on Cisco Infrastructure

Guhan:

> "Because this is a Cisco code, so we don't want this code to get out of Cisco."
> "No downloading of the code, those kind of things."
> "Also use the Cisco license or approval license for the... and others, rather than using their separate own license."

Guhan referenced that Cisco engineers already use "Claude" and "Copilot Enterprise" (or similar) internally.

Colin: "I'll have Cisco hardware that I'll do all Cisco work on. So that won't ever leave your hardware. And likewise with AI tools, definitely. We'll use those from day one if we can, and that way we can keep that kind of security bubble intact."

Constraint stack:

1. No code leaves Cisco infrastructure.
2. No downloading to personal machines.
3. AI tools must be Cisco-licensed.
4. Personal AI tool licenses cannot be used on Cisco code.
5. All work on Cisco-provisioned hardware.

Open: whether Cisco's enterprise license for Claude (if referenced) provides API access or only web/IDE. LangGraph agent swarm requires API-level access.

### Hardware Posture

As of 2026-02-20, Colin did not have a Cisco laptop or Cisco ID. Both had been pending since 2026-02-09 (11 days). Colin estimated one to two weeks for delivery. A BayOne representative noted an evening call that same day to get a firm date.

Guhan's response to delay: "I'm trying to figure out what we can do in the next two weeks to get you going." He suggested Cisco could identify screens and begin initial context-transfer conversations during the wait.

Critical path blocker: without laptop and ID, no hands-on work possible.

### Running Systems

Colin asked about running instances of both EPNM and EMS. Selva agreed to provide "when ready." Not needed immediately, only after initial code exploration. Not formally accepted for POC scope: "When we get to that stage, we guess we will provide the system to try this out."

Unresolved: dedicated vs. shared, access level, data pre-population, timing.

### Four-Week Decision Window

Guhan: "I think we were looking at discussing about like, let's do it in four weeks, so then we made some important decisions around this."

Colin had initially proposed "a couple of weeks at most." Guhan extended to four weeks. Unclear whether clock starts from meeting date, hardware arrival, or code access.

### Two-Week Pre-Work Gap

Guhan: "You have signed NDA and everything. That's right. I'm trying to figure out what we can do in the next two weeks to get you going."

Productive use: Colin writes POC proposal, Cisco identifies target screens, initial context conversations begin, hardware escalation.

Sequencing:

- Weeks 1-2: No hardware, context transfer and planning only.
- Weeks 3-6 (approx): Hardware arrives, code access, hands-on POC work.
- Week 6: Four-week decision deadline (if counted from hardware arrival).

### Shared Hardware Pipeline with Anand's CI/CD Engagement

Colin: "I'm already working on Anand's project for the CICD board. I'll have my Cisco laptop probably within a week or two."

Same laptop serves both engagements. Any slip affects both.

### BayOne Bench Already NDA/Hardware Cleared

Colin disclosed: "Everyone else has the same NDA signage, the same everything."

Guhan: "So you need access to more than you?" Colin: "I don't think I will. I think, especially for the POC, I'll just handle this. But then when we go beyond the POC, I just know I already have an asset of people ready to go."

### Cloud Instances

Oblique reference. Cisco has cloud infrastructure (Azure-based, per Set 01). Colin: "Even probably for access to the cloud instance. I'm guessing that would be preferable if it's using the Cisco ID." Connection to this engagement not clarified.

### Division of Responsibilities

**Cisco provides:** initial context, screen identification and prioritization, running systems (when ready), code access, checkpoint availability, domain clarification at checkpoints, hardware and ID provisioning.

**Cisco does NOT provide:** ongoing engineering pairing, dedicated engineer time, design documentation, immediate hardware/access.

**BayOne provides:** independent code exploration, AI-assisted conversion, working demos, estimation methodology, POC proposal, all work on Cisco hardware with Cisco tools.

### POC at BayOne's Cost

Colin: "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us."

> "I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

Guhan: "So basically this is also about actually hands-on coding and showing the credit. That way, if we have to also get the additional resources for this, which we will have to work through, this will help."

POC absorbed by BayOne as investment; proof for Guhan to secure additional internal resources; scope must be reasonable.

---

## 4. POC Scope and Success Criteria (as of 2026-02-20)

Source file: 02_meeting_poc_scope_and_success_criteria_2026-02-20.md

**FRAMING FLAG:** This entire section reflects the Set 02 "missing functionality / missing reports / vertical end-to-end conversion" framing. **SUPERSEDED BY SET 03** for scope. The QA expectations, customer-experience fidelity standard, and "working demo not analysis" requirement survive in modified form.

### POC Objective [SUPERSEDED BY SET 03]

Guhan:

> "The challenge for you, that you can choose to accept, is basically can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS."

Five requirements in Set 02 framing:

1. Working code, not analysis or documentation.
2. Show the demo, visible and demonstrable.
3. Take screens from EPNM (legacy UI).
4. Include the backend, not just the frontend.
5. Run it in EMS (modern microservices target).

Customer test: "From a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything."

**SUPERSEDED BY SET 03:** backend porting is no longer in scope. POC is a classic-view toggle on two specific EMS screens. Working-demo requirement and customer-experience fidelity survive.

### Hands-On Coding, Not Analysis

Guhan: "The POC would, so basically this is also about actually hands-on coding and showing the demo."

Purpose: "That way, if we have to also get the additional resources for this, which we will have to work through, this will help. Show it, even to make it, show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

Dual purpose: technical validation AND internal justification for Guhan to secure resources.

Colin: "That's the investment I want to make for you, is to show that, because I know this is important, I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding."

### Estimation Methodology [SUPERSEDED BY SET 03]

Guhan: "One of the outcome I'm looking for, obviously there are like 70, 80, 100 pages, we are not expecting everything to be converted. We get a better idea of what it means to do that."

Extrapolation formula:

> "In case of like, for example, we are able to do 10 with this AI. I mean, whatever infra you will develop also, right? We are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this, right?"

Business purpose: "With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

Shaped POC design: enough screens for statistically meaningful sample (~10), time-per-screen tracking, reusable infrastructure, complexity variance addressed.

**SUPERSEDED BY SET 03:** two specific screens only; not a per-screen extrapolation exercise.

### What to Convert: Missing Functionality [SUPERSEDED BY SET 03]

Selva: "There are some screens we have already brought in functionality with a new UI. There are still some functionality that's remaining in the old. Maybe, I mean, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens, like Guhan has said."

Rule: focus on functionality NOT yet ported to EMS. Already-converted screens excluded.

**SUPERSEDED BY SET 03:** the POC now targets already-converted EMS screens (Inventory and Fault Management) by adding a classic-view toggle, not net-new missing functionality.

### Vertical Functionality [SUPERSEDED BY SET 03]

Selva: "It's not a UI alone. There is a, I mean, along with it comes the backend logic. Only then this is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

Colin: "From the new interface to the old, you said there's still some backend work remaining. Is it major backend work that's also pending on it, or is that something that is familiar?"

Selva: "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

**SUPERSEDED BY SET 03:** backend unchanged; POC is frontend-only.

### Concrete Example: Missing Reports [SUPERSEDED BY SET 03]

Selva: "I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new and then make it work end-to-end, right? So that will be the goal for this exercise."

**SUPERSEDED BY SET 03:** Inventory and Fault Management, not missing reports.

### Who Selects Screens [SUPERSEDED BY SET 03 for which screens]

Guhan: "We can help prioritize few of the UI and also we will also basically, I mean basically we'll help you prioritize and we'll help you with which are the ones we want to try to begin with, right."

Selva: "The team will help identify what those are and provide you with the overall thing."

Cisco selects; BayOne does not choose.

### POC as Confidence-Building

Guhan: "This is also about actually hands-on coding and showing the demo. That way, if we have to also get the additional resources for this, which we will have to work through, this will help."

"Which we will have to work through" indicates additional resources are not yet approved. POC is evidence for internal case. This survives as a purpose.

### Timeline

Guhan: "I think we were looking at discussing about like, let's do it in four weeks, so then we made some important decisions around this, right?"

Colin: "Let's do what we can in the four weeks, right? That's a good spread."

Colin's own estimate: "I'm hoping something we can do in a couple of weeks for you at most."

Hardware dependency: ~1-2 weeks, so effective execution window was approximately 2 weeks after hardware arrival.

### What POC Is Not

- Not a full conversion (70-80-100 total; POC a subset).
- Not a new UX design exercise: "For now, keep the same user experience and bring it to the new."
- Not independent of Cisco team: still needs screen identification, context transfer, running systems, code access.
- Not using external (non-Cisco) tools.

### Set 02 POC Success Criteria [FRAMING FLAG]

The following were Set 02's success criteria. Items marked [S] are superseded by Set 03; items marked [B] still bind.

- [S] Working code for vertical conversions from EPNM backend into EMS.
- [B] Demonstrable, visual demo of converted screens.
- [S] End-to-end vertical conversion (UI + backend).
- [S] Focus on functionality not yet ported.
- [S] Missing reports as concrete starting point.
- [S] Per-screen effort estimation methodology.
- [S] Customer-facing delivery timeline estimates derived from estimation.
- [B] Confidence-building demo for internal resource approval.
- [B] Approximately four-week window for decision.
- [B] Faithful reproduction of EPNM user experience.
- [B] All work on Cisco hardware with Cisco-licensed tools.

---

## 5. Next Steps Committed in This Meeting

Source file: 02_meeting_next_steps_2026-02-20.md

| # | Action Item | Owner | Timeline | Dependency |
|---|-------------|-------|----------|------------|
| 1 | Send meeting summary from Feb 20 call | Colin | Same day (Feb 20) | None |
| 2 | Confirm Cisco laptop delivery date | Colin + BayOne ops | Same day evening call | None |
| 3 | Write POC proposal based on Feb 9 and Feb 20 meetings | Colin | Within days of Feb 20 | None |
| 4 | Resolve Cisco ID provisioning | Cisco onboarding / BayOne ops | Expected ~Feb 20 | None |
| 5 | Identify priority screens/functionality for conversion | Selva + Cisco engineering team | During 2-week waiting period | None |
| 6 | Arrange code access | Guhan / Selva | After laptop delivery | Cisco laptop + ID |
| 7 | Set up Cisco-licensed AI tools | Guhan / Cisco IT | After laptop delivery | Cisco laptop |
| 8 | Initial context transfer conversations | Selva's team + Colin | During or after waiting period | Priority screen identification |
| 9 | Provide running systems (EPNM and EMS instances) | Selva's team | When POC reaches testing stage | POC progress |
| 10 | Deliver POC results (working demo + estimation methodology) | Colin | Within 4-week window (~Mar 9) | Items 4-8 |
| 11 | Establish periodic checkpoint cadence | Both parties | After POC work begins | POC kickoff |
| 12 | Deliver Cisco laptop hardware | Cisco IT / procurement | ~1-2 weeks from Feb 20 | None |

Firm commitments distinguished from aspirational statements:

**Firm:**

- Colin sends same-day summary.
- Colin writes POC proposal.
- Colin confirms hardware date via evening call.
- Cisco provides code access once hardware is in place.
- Selva's team identifies priority screens.
- Selva's team provides initial context.
- All work on Cisco hardware with Cisco-licensed tools.
- Colin handles POC solo.
- Periodic checkpoints will occur.

**Aspirational / conditional:**

- Four-week window as a hard deadline (Guhan said "let's do what we can").
- Running systems "when we get to that stage."
- Automated UX testing "when we get to that stage."
- Context transfer "maybe we can start those initial conversations."
- Hardware arriving within "a week or two" (Colin's estimate).
- Non-code activities during two-week waiting period (no clear path beyond proposal writing).

[SUPERSEDED BY SET 03 NOTE:] Action items 5, 8, 10 were framed around Set 02's vertical-conversion POC. Their underlying mechanics (context transfer, screen selection by Cisco, working-demo delivery in the four-week window) continue, but the screens selected and the nature of the "working demo" shifted in Set 03.

---

## 6. What Still Binds from Set 02

The following items from Set 02 remain applicable to the POC today.

### Binding: Quality Assurance Approach

Source: 02_meeting_domain_gap_and_quality_assurance_2026-02-20.md

Colin's four-layer QA framework was presented as how BayOne handles the domain-gap risk. That framework binds regardless of whether the POC is a vertical conversion or a classic-view toggle, because Guhan's underlying concern (completeness in an unfamiliar specialized domain) applies equally to frontend-only work. Specifically:

- Judge agent in the swarm doing meta-analysis of test coverage, not just test execution.
- Playwright screen-capture comparison for visual fidelity, workable without a running application.
- Peer-to-peer agent gap analysis with autonomous sub-agent spawning and redirection.
- Human final review as last line of defense.
- Categorical-miss insight: when things are missed, entire categories are missed, so human review at the category level is tractable.

The automated UX testing offer (Playwright-based, precursor to Cisco's formal testing) was made by Colin and received positively by Selva ("when we get to that stage, we guess we will provide the system to try this out"). It remains on the table.

### Binding: Independent-Work Engagement Model

Source: 02_meeting_engagement_model_and_constraints_2026-02-20.md

- Engineering team bandwidth is zero. Team provides context; BayOne executes.
- BayOne works independently after context transfer.
- Periodic checkpoints (cadence still undefined; weekly is a reasonable default).
- No engineering pairing, no embedded collaboration, no ongoing Q&A.

### Binding: No Design Documentation Reality

Source: 02_meeting_engagement_model_and_constraints_2026-02-20.md; 02_meeting_domain_gap_and_quality_assurance_2026-02-20.md

- Legacy product lacks solid design documentation.
- Code IS the documentation.
- Navigating the code is the bulk of the challenge.
- Context transfer is verbal, architectural walkthrough, or code tour, not document handoff.
- Colin's "blockchain documentation" discovery approach applies: append-only knowledge accumulation as the agents explore.

### Binding: Security and Infrastructure Constraints

Source: 02_meeting_engagement_model_and_constraints_2026-02-20.md

- All work on Cisco infrastructure.
- No code leaves Cisco.
- No downloading to personal machines.
- AI tools must be Cisco-licensed (Claude, Copilot Enterprise referenced as available internally).
- Personal AI tool licenses cannot be used on Cisco code.
- All work on Cisco-provisioned hardware.

### Binding: Hardware Posture (Historical Context Still Relevant)

Source: 02_meeting_engagement_model_and_constraints_2026-02-20.md

- Cisco laptop and Cisco ID required.
- Same hardware serves both Cisco engagements (EPNM-to-EMS and Anand's CI/CD).
- BayOne bench is already NDA-cleared and in the same hardware pipeline for any post-POC scaling.

### Binding: Customer-Experience Fidelity Standard

Source: 02_meeting_problem_definition_2026-02-20.md; 02_meeting_poc_scope_and_success_criteria_2026-02-20.md

- Same experience, same visualization, same operations as EPNM.
- Backend transparency: customers do not know or care what runs behind.
- Faithful reproduction of the EPNM user experience is the bar, regardless of whether delivery is vertical conversion or a classic-view toggle.

### Binding: Working Demo, Not Analysis

Source: 02_meeting_poc_scope_and_success_criteria_2026-02-20.md

- Guhan wants hands-on coding and a demonstrable result, not a plan or report.
- POC is a confidence-building exercise for Guhan's internal case for additional resources.
- The demo, not the analysis, is the deliverable.

### Binding: Screen Selection by Cisco

Source: 02_meeting_poc_scope_and_success_criteria_2026-02-20.md; 02_meeting_next_steps_2026-02-20.md

- Cisco identifies and prioritizes screens. BayOne does not choose.
- In Set 03, Cisco selected Inventory and Fault Management. The selection-by-Cisco principle remains.

### Binding: Four-Week Decision Window

Source: 02_meeting_poc_scope_and_success_criteria_2026-02-20.md; 02_meeting_next_steps_2026-02-20.md

- "Let's do it in four weeks" remains the framing, subject to hardware and access timing.

### Binding: POC at BayOne's Cost

Source: 02_meeting_engagement_model_and_constraints_2026-02-20.md; 02_meeting_poc_scope_and_success_criteria_2026-02-20.md

- POC is a BayOne investment.
- Scope must remain reasonable.
- Purpose is capability demonstration for downstream engagement.

---

## Summary of What Still Binds vs. What Was Superseded

**Still binds:** the four-layer QA approach (judge agent, Playwright, peer-to-peer agent gap analysis, human review), the categorical-miss insight, the automated UX testing offer, the independent-work engagement model with zero engineering bandwidth and periodic checkpoints, the no-documentation reality (code is the source of truth), all security and Cisco-infrastructure constraints, the Cisco-selects-screens principle, the customer-experience fidelity standard, the working-demo-not-analysis deliverable model, the four-week decision window, and POC-at-BayOne's-cost.

**Superseded by Set 03:** the vertical full-stack conversion framing, the missing-functionality / missing-reports scope, the backend porting requirement, the 70-80-100-screen estimation extrapolation methodology, the EPNM-code-to-EMS-runtime challenge, the "end-to-end vertical" success criterion, and the "take EPNM code and run it in EMS" formulation. The POC now scopes to a classic-view toggle on two specific EMS screens (Inventory, Fault Management) with backend unchanged.
