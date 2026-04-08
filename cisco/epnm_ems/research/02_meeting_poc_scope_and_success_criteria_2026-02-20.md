# 02 - Meeting: POC Scope and Success Criteria

**Source:** /cisco/epnm_ems/source/guhan_selva-2-20-2026.txt
**Source Date:** 2026-02-20 (Follow-Up Technical Meeting)
**Document Set:** 02 (Second meeting, deeper technical detail on EPNM-to-EMS conversion)
**Pass:** Focused deep dive on POC scope and success criteria

---

## Overview

This document decomposes every statement from the February 20, 2026 meeting that relates to what the proof of concept should accomplish, how its success should be measured, and how its results should feed into larger planning. The meeting participants were Guhan (Cisco engineering leadership), Selva (Cisco technical lead on EMS), and Colin Moore (BayOne, Director of AI). Guhan set the strategic framing. Selva provided the concrete starting example. Colin proposed the execution approach and timeline.

---

## The POC Objective: End-to-End Functional Conversion

### Guhan's Framing

Guhan opened the meeting by defining the POC as a challenge. His exact framing:

> "The challenge for you, that you can choose to accept, is basically can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS."

This is the single most important sentence in the meeting for understanding POC scope. It establishes five requirements in one statement:

1. **Working code** -- not analysis, not a plan, not documentation. Actual functional code.
2. **Show the demo** -- a visible, demonstrable result. Not a report on feasibility.
3. **Take screens from EPNM** -- the source is the legacy product's UI.
4. **Include the backend** -- not just the frontend; the backend logic behind those screens must also be ported.
5. **Run it in EMS** -- the target is the modern microservices-based product. The code must execute within EMS.

Guhan reinforced the customer-perspective test for success:

> "From a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything, the way they would do, interact with the EMS, same as what is there [in EPNM]."

This sets a high bar: functional equivalence from the user's perspective. The customer should not be able to distinguish whether they are interacting with original EPNM functionality or ported functionality running in EMS. Same visualization, same operations, same interaction patterns.

### Hands-On Coding, Not Just Analysis

Guhan was explicit that the POC must produce working artifacts, not just analysis. He returned to this point later in the meeting when discussing how the POC results would be used internally:

> "The POC would, so basically this is also about actually hands-on coding and showing the demo."

And the purpose of that hands-on work:

> "That way, if we have to also get the additional resources for this, which we will have to work through, this will help. Show it, even to make it, show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

This reveals a dual purpose for the POC:
1. **Technical validation** -- prove that the conversion approach works.
2. **Internal justification** -- provide Guhan with a tangible demonstration he can use to secure additional resources within Cisco. The POC is a tool for internal budget and resource approval.

### Colin's Acknowledgment

Colin understood and echoed this:

> "That's the investment I want to make for you, is to show that, because I know this is important, I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

This is a firm agreement that the POC deliverable is a working demonstration, not a document.

---

## The Estimation Methodology: The Core Analytical Outcome

### Guhan's Estimation Framework

Beyond the working demo, Guhan articulated a specific analytical outcome he wants from the POC. This is arguably the most strategically important deliverable:

> "One of the outcome I'm looking for, obviously there are like 70, 80, 100 pages, we are not expecting everything to be converted. We get a better idea of what it means to do that."

Breaking this down:

1. **70, 80, 100 pages** -- Guhan referenced a range of screen counts (where "pages" means screen pages/UI screens). The imprecision of the range (70 to 100) suggests the exact count has not been inventoried. This is a rough estimate of the total scope of screens that need conversion, not the POC scope.
2. **"We are not expecting everything to be converted"** -- explicit acknowledgment that the POC will only convert a subset.
3. **"We get a better idea of what it means to do that"** -- the POC's analytical purpose is to characterize the conversion effort: its complexity, its patterns, its cost.

Note: In the first meeting (Set 01), Guhan referenced approximately **200 UI screens**. The 70-80-100 figure here likely represents a subset -- possibly the screens that have not yet been brought into EMS, or a subset of the full 200 that are highest priority. This discrepancy is unresolved but may reflect that some screens have already been converted, reducing the remaining count.

### The Extrapolation Formula

Guhan then stated the specific estimation methodology he wants:

> "In case of like, for example, we are able to do 10 with this AI. I mean, whatever infra you will develop also, right? We are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this, right?"

This is an explicit request for a **linear extrapolation model**:
- Convert N screens during the POC.
- Measure the time it takes.
- Extrapolate: if 10 screens take X days, then Y screens will take (Y/10) * X days.

The numbers "10 days" and "17 days" appear to be Guhan's illustrative placeholders, not specific estimates. The point is the formula, not the numbers.

### Why This Matters: Customer Commitments

Guhan stated the business purpose of this estimation:

> "With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

This is a firm requirement, not an aspiration. The POC's estimation output will be used to make delivery commitments to Cisco's customers. The estimation methodology is therefore a critical deliverable, not a nice-to-have.

### Implications for POC Design

The estimation requirement shapes the POC in several ways:

1. **The POC must convert enough screens to produce a statistically meaningful sample.** Converting 1-2 screens would not establish a reliable per-screen rate. Guhan's mention of 10 screens suggests that is the rough target.
2. **The POC must track time per screen.** The methodology requires measuring effort, not just producing output.
3. **The infrastructure and tooling built during the POC must be reusable.** Guhan acknowledged this explicitly: "whatever infra you will develop also, right?" He understands that the first few screens will involve building tooling that accelerates subsequent screens.
4. **Complexity variance must be addressed.** Not all screens are the same complexity. The estimation model must account for this, or at minimum, the POC screens should be representative of the range of complexity.

---

## What to Convert: Focus on Missing Functionality

### Selva's Prioritization Principle

Selva provided the key prioritization criterion for selecting which screens to convert in the POC:

> "There are some screens we have already brought in functionality with a new UI. There are still some functionality that's remaining in the old. Maybe, I mean, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens, like Guhan has said."

This establishes a clear rule: **the POC should focus on functionality that has NOT yet been ported to EMS.** Screens that have already been brought over with a new UX design are excluded. The reason is practical -- converting already-converted screens proves nothing new. Converting screens that the team has not yet tackled demonstrates the approach on the actual remaining work.

### Vertical Functionality, Not Just UI

Selva reinforced that this is not a UI-only exercise:

> "And it's not a UI alone. There is a, I mean, along with it comes the backend logic. Only then this is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

This is critical. Each screen that gets converted must include its corresponding backend logic. The conversion is "vertical" -- from the UI layer down through the backend. This was reinforced by an earlier exchange where Colin asked about the backend work:

> **Colin:** "From the new interface to the old, you said there's still some backend work remaining. Is it major backend work that's also pending on it, or is that something that is familiar?"
>
> **Selva:** "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

This means the screens that still need conversion are not cases where the backend exists and only the UI is missing. The entire vertical slice -- UI, business logic, data access -- is absent from EMS. The POC must deliver the full stack for each screen it converts.

### The Concrete Starting Example: Missing Reports

Selva provided a specific, concrete example of functionality to target:

> "For example, I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new and then make it work end-to-end, right? So that will be the goal for this exercise."

This is the most specific guidance in the meeting about what to convert. "Missing reports" refers to report screens in EPNM that generate or display data but have not yet been implemented in EMS. This is a useful starting point because:

1. **Reports are typically well-defined** -- they have clear inputs, a data query, and a formatted output. This makes them easier to scope than highly interactive screens.
2. **Reports are visible deliverables** -- a working report can be demonstrated immediately.
3. **The user experience benchmark is clear** -- "keep the same user experience" means replicate the visual and functional behavior of the EPNM report in EMS.
4. **End-to-end means the full stack** -- the report must query data, process it, and display it, not just render a static layout.

### Who Selects the Screens

Both Guhan and Selva indicated that the Cisco team will identify and prioritize the specific screens for conversion:

> **Guhan:** "We can help prioritize few of the UI and also we will also basically, I mean basically we'll help you prioritize and we'll help you with which are the ones we want to try to begin with, right."
>
> **Selva:** "The team will help identify what those are and provide you with the overall thing."

BayOne does not choose the screens. Cisco's team identifies the target screens, provides context on them, and BayOne executes the conversion. This is a firm division of responsibility.

---

## The POC as a Confidence-Building Exercise

### Guhan's Internal Stakeholder Problem

Guhan stated explicitly that the POC serves an internal political purpose beyond its technical validation:

> "This is also about actually hands-on coding and showing the demo. That way, if we have to also get the additional resources for this, which we will have to work through, this will help."

The phrase "which we will have to work through" indicates that additional resources for a full-scale conversion are not yet approved. The POC is the evidence Guhan needs to make that case internally. Without a working demonstration, the request for resources is theoretical.

> "Show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

The word "confidence" is Guhan's. He needs to build confidence -- both his own and that of internal stakeholders -- that the conversion approach is viable. The POC is a confidence-building exercise.

### Colin's Response: Proof Over Case Studies

Colin understood and reinforced the confidence-building dimension:

> "I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

This was a deliberate choice by Colin to offer the POC at cost to BayOne as an investment:

> "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us. So we'll make sure that we're at least proving this out to you."

This confirms:
1. The POC is being offered as a cost-investment by BayOne (no charge to Cisco, or heavily discounted).
2. The scope must be kept reasonable precisely because BayOne is absorbing the cost.
3. The goal is to prove capability, not to do a substantial portion of the work.

---

## Timeline and Decision Window

### Guhan's Four-Week Target

Guhan set a specific timeline for the POC:

> "I think we were looking at discussing about like, let's do it in four weeks, so then we made some important decisions around this, right?"

Four weeks is the window within which the POC must produce results that enable "important decisions." This is a decision-forcing deadline, not just a project timeline. At the end of four weeks, Guhan needs to be able to decide whether to invest further in this approach.

Colin confirmed:

> "Let's do what we can in the four weeks, right? That's a good spread."

### The Hardware Dependency

A significant constraint on the timeline was the pending Cisco laptop and Cisco ID for Colin. Without these, he cannot access Cisco code repositories or systems. The meeting established:

1. Colin's Cisco hardware was expected within one to two weeks.
2. Guhan and his team were trying to accelerate the hardware delivery.
3. Once hardware arrived, code access could be provided immediately.

Guhan tried to problem-solve the gap:

> "It's possible to set up a program like this or something, what we can do to give this... you have a laptop that's not Cisco, but I can get them to the network, I'm not sure about that."

This was left unresolved -- Guhan was uncertain whether a non-Cisco laptop could be connected to Cisco's network.

### Colin's Two-Week Pre-Work Plan

Colin proposed using the hardware gap productively:

> "What I can do today, myself, to help this is I'll try to get a firm date on the hardware so that way we can plan around it."

He also suggested that context conversations could begin before hardware arrived:

> "Once we internally also will identify a few of the things for conversion, then maybe we can start those initial conversations... And by then, maybe your hardware arrives and then you can access to things right away."

This means the four-week clock effectively starts when hardware arrives and code access is granted, but context transfer can happen in advance.

### Colin's POC Timeline Estimate

Colin gave his own estimate for the POC duration:

> "I'm hoping something we can do in a couple of weeks for you at most."

This suggests Colin expected the POC execution (after context acquisition) to take approximately two weeks. Combined with the hardware wait, this fits within Guhan's four-week window: ~2 weeks waiting/context + ~2 weeks execution = ~4 weeks total.

---

## What the POC Is NOT

Several things were explicitly excluded or deferred:

### Not a Full Conversion

Guhan: "We are not expecting everything to be converted." The 70-80-100 screens are the total remaining scope. The POC converts a small subset, perhaps 10.

### Not a New UX Design Exercise

Selva: "For now, keep the same user experience and bring it to the new." The POC is not about reimagining the UX. It is about faithfully reproducing the EPNM experience in EMS. UX redesign happened for the screens that were already ported; the remaining screens should be ported as-is.

### Not Independent of Cisco's Team

Despite the emphasis on BayOne working independently, the POC requires Cisco's team for:
1. **Screen identification and prioritization** -- Cisco selects what to convert.
2. **Context transfer** -- explaining the domain, the codebase, and the architecture.
3. **Running systems** -- providing access to EPNM and EMS instances for reference and testing.
4. **Code access** -- granting repository access.

Guhan was clear that his team's time is limited:

> "At the moment the team is also on critical or a platform, if you think so, the team itself will not be able to invest time here. But of course, they need to give you the context and everything. They will provide you with that."

### Not Using External (Non-Cisco) Tools

Guhan required all work be done on Cisco infrastructure:

> "No, nothing on the laptop. No downloading of the code, those kind of things."
> "Also use the Cisco license or approved license for the [AI tools], rather than using their separate own license."

Colin agreed to use Cisco-licensed AI tools (Claude, Copilot) rather than external licenses. This is a security requirement, not a preference.

---

## POC Success Criteria: Summary

Based on the meeting, POC success requires ALL of the following:

| Criterion | Source | Type |
|-----------|--------|------|
| Working code, not just analysis or documentation | Guhan | Firm requirement |
| A demonstrable, visual demo of converted screens | Guhan | Firm requirement |
| End-to-end vertical conversion (UI + backend) | Selva | Firm requirement |
| Focus on functionality not yet ported to EMS | Selva | Firm requirement |
| Missing reports as a concrete starting point | Selva | Firm requirement (specific example) |
| Estimation methodology: per-screen effort extrapolation | Guhan | Firm requirement |
| Customer-facing delivery timeline estimates | Guhan | Firm requirement (derived from estimation) |
| Confidence-building demo for internal resource approval | Guhan | Firm requirement (strategic purpose) |
| Completed within approximately four weeks | Guhan | Firm requirement (decision window) |
| Faithful reproduction of EPNM user experience | Guhan, Selva | Firm requirement |
| All work on Cisco hardware with Cisco-licensed tools | Guhan | Firm requirement (security) |

---

## Open Questions and Unresolved Points

1. **How many screens will the POC target?** Guhan mentioned 10 as an illustrative example. The actual number has not been agreed upon. Cisco's team must identify the specific screens.

2. **Which "missing reports" specifically?** Selva referenced missing reports as a starting point but did not name specific reports. This requires follow-up with Selva's team.

3. **What is the relationship between the 70-80-100 figure and the 200 from the first meeting?** Guhan said 200 screens in the February 9 meeting and 70-80-100 in this meeting. It is unclear whether the difference represents screens already ported (200 total minus ~100-130 already done = ~70-100 remaining) or whether these are different counting methods. This ambiguity affects the total conversion scope and therefore the extrapolation target.

4. **What does "estimation methodology" mean in practice?** Guhan wants to be able to say "we will deliver in X time." But screens vary in complexity. Will the estimation be a simple average (total screens / screens per day), or will it account for complexity tiers? The POC design should anticipate this question.

5. **How will the POC screens be selected for representativeness?** If the POC converts only simple screens, the per-screen rate will be optimistic. If it converts only complex screens, the rate will be pessimistic. The selection of POC screens must balance this to produce a credible extrapolation.

6. **When does the four-week clock start?** Guhan said "let's do it in four weeks." Colin's hardware may take one to two weeks. If the four weeks starts from the meeting date (February 20), the execution window is only two to three weeks. If it starts when hardware arrives, there is more room. This is ambiguous.

7. **What constitutes a "working demo" for sign-off?** There is no formal acceptance criteria defined. "Same experience, same visualization, everything, operations, everything" is the stated standard, but whether there is a formal review process (and who attends it) was not discussed.

8. **Will automated UX testing be part of the POC deliverable?** Colin offered automated UX testing (using Playwright) as a value-add. Guhan responded with "when we get to that stage, we guess we will provide the system to try this out." It is unclear whether this is in-scope for the POC or deferred.

---

## Key Quotes Index

For reference, the most important verbatim quotes from the transcript, organized by speaker and topic:

**Guhan on POC objective:**
- "Can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS."
- "From a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything."

**Guhan on estimation:**
- "Obviously there are like 70, 80, 100 pages, we are not expecting everything to be converted. We get a better idea of what it means to do that."
- "We are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this."
- "With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

**Guhan on internal justification:**
- "This is also about actually hands-on coding and showing the demo."
- "If we have to also get the additional resources for this, which we will have to work through, this will help."
- "Show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

**Guhan on timeline:**
- "Let's do it in four weeks, so then we made some important decisions around this."

**Selva on prioritization:**
- "There are some screens we have already brought in functionality with a new UI. There are still some functionality that's remaining in the old."
- "We will focus on the ones that we've not brought in yet and identify a few screens."

**Selva on vertical scope:**
- "It's not a UI alone. There is a, along with it comes the backend logic. Only then this is more EMS element management domain."
- "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working."

**Selva on missing reports:**
- "I have some missing reports that I've not brought in from the old thing. So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new and then make it work end-to-end."

**Colin on cost investment:**
- "We'll have to make sure that the scope is kept reasonable, because we'll do this one at cost to us."
- "I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding."

**Colin on timeline:**
- "I'm hoping something we can do in a couple of weeks for you at most."
