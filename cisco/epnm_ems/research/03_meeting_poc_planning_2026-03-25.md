# 03 - Meeting: POC Planning and Execution

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Focused deep dive on POC planning and execution approach

---

## Overview

This document decomposes every statement from the March 25, 2026 meeting that relates to how the POC will be planned, what screens will be targeted, how the toggle approach will work, how the work scales, and what automated verification will look like. The meeting participants were Guhan (Cisco engineering leadership), Selva (Cisco technical lead on EMS), and Colin Moore (BayOne, Director of AI). Guhan set the strategic framing and reframed the scope from missing-functionality conversion to classic-view overlay. Selva provided tactical details on screen selection and backend constraints. Colin explained the execution dynamics: front-loading, exponential decay in per-screen effort, parallelizable workflows, and automated QA/QE agents.

This is a significant evolution from Meeting 02 (February 20). The POC objective has shifted from "convert screens that do not exist in EMS" to "add a classic view toggle to screens that already exist in EMS." The backend remains largely untouched. The POC now demonstrates a UI overlay pattern, not a vertical conversion. The implications for planning and execution are substantial and are detailed below.

---

## Screen Selection for the POC

### Two to Three Screens, Specifically Faults and Inventory

Guhan and Selva identified the target screen count and the specific candidates. Guhan framed it first:

> "Right now just for demonstrating POC let's say we pick two to three screens we will say hey old way of doing this for example like faults right and then now you're doing new way of doing that and then switch and then say do some actions here, do some actions here and then final test will be to show the same thing comes up everywhere."

Selva confirmed the second candidate:

> **Guhan:** "Like the fault and I think, is it inventory or?"
> **Selva:** "It's inventory, yeah."

Guhan then explained the selection rationale:

> "So, these are very common applications that customer usually go to."

This establishes three things:

1. **The POC targets 2-3 screens** -- not the 10 screens discussed in Meeting 02. The scope has contracted, consistent with the shift from vertical conversion (which requires more screens to build a credible estimation model) to toggle overlay (which is a pattern demonstration).
2. **Faults and Inventory are the confirmed candidates.** These are two of the most-used screens in the product. The third screen, if there is one, was not named.
3. **Selection is driven by customer usage frequency**, not by technical complexity. Guhan chose screens that "customers usually go to" because the adoption problem is about these high-traffic screens. If customers can toggle to a classic view on the screens they use most, the adoption friction drops significantly.

### Contrast with Meeting 02 Screen Selection Logic

In Meeting 02, Selva said: "We will focus on the ones that we've not brought in yet." In Meeting 03, the logic has inverted: the POC targets screens that ALREADY exist in EMS. This is not a contradiction -- it reflects the scope reframe. The work is no longer about porting missing functionality; it is about adding a classic-view overlay to existing functionality.

### Colin's Point About Screen Diversity

Colin introduced a dimension to screen selection that went beyond simple priority ordering:

> "And the more diversity of the screens that we encounter, it's a good way for us to even plan what screens. Because there's the priority order, but there's also the diversity order. Diversity order helps us cover all the edge cases that we might miss with agents. So it can be more intelligent with this."

This is a methodological point about how to maximize the value of the POC for future scaling. Colin is distinguishing between two different criteria for choosing POC screens:

1. **Priority order** -- which screens matter most to customers. This is Guhan's criterion (faults, inventory).
2. **Diversity order** -- which screens cover the widest range of edge cases for agent-based conversion. This is Colin's criterion as the person who will build the automated conversion infrastructure.

The implication: if all three POC screens are structurally similar (e.g., all table-based data displays), the agents built during the POC will only handle that one pattern. If the screens include different UI patterns (e.g., a table view, a detail/form view, and a topology/graph view), the agents learn to handle a broader range of screen types. This makes the subsequent conversion of 200-250 screens more reliable because more edge cases were encountered early.

Colin did not push this point over Guhan's priority-based selection. He raised it as a factor for planning, not as a challenge to the faults-and-inventory decision.

---

## The Toggle Approach: Local vs. Global

### The Core Concept

Guhan laid out the toggle concept clearly:

> "How in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable. And then I want to switch to the new thing."

And then applied it to the EMS context:

> "So basically, I mean, the areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI. But obviously, it's been redesigned to adopt a new workflow, a new UX and everything. So how do you make our customers more comfortable to adopt this is by bringing the similar workflow that you have for the same functionality from EPNM, right? And then giving them like a toggle and then saying, hey, do you want to go to the old workflow?"

This is the clearest articulation of the project's purpose in any of the three meetings. Breaking it down:

1. The target screens **already exist in EMS** with a backend, a UI, and a redesigned workflow.
2. The problem is that **customers are uncomfortable** with the redesigned workflow because they are accustomed to EPNM's 10-year-old interface.
3. The solution is to **overlay a classic-view option** that reproduces the EPNM workflow/UX on top of the existing EMS backend.
4. The toggle lets customers **choose their comfort level** -- use the classic view until they are ready, then switch to the new UI.

### Local Toggle for POC

Selva specified that the POC will use a per-screen toggle, not a global one:

> "For the toggle, as I said, let's not worry too much about the UX. Finally, of course, we'll take the blessing of the UX. There is a separate UX team. We didn't want to involve them here so this is like we can keep it simple and say we will do local toggle by that what I mean is let's say a faults screen for example right that's the one I want to give you want to take in this new product and you want to give an equivalent classic experience we'll just add a toggle to that very same page and say once you toggle it gives me the classic."

This is Selva explicitly scoping down the toggle implementation for the POC:

1. **Local toggle** = a toggle button on each individual screen page that switches between new and classic views.
2. **No UX team involvement** for the POC. The UX team exists separately and would bless the final product design, but involving them at the POC stage would slow things down and add complexity that is not needed for a demonstration.
3. **Keep it simple** -- the toggle just needs to illustrate the concept.

### Global Toggle Comes Later

Selva continued:

> "But when we finally do the product, we may do it somewhere globally in the user setting or somewhere where they say, and then the whole experience is going to be classic. So that we'll worry about later."

And reinforced:

> "So now, let's say we're going to pick three screens. We're going to have a local toggle one, each one another to keep it simple. Because you're just illustrating the idea."

This establishes a clear phasing:

| Phase | Toggle Type | Scope | Purpose |
|-------|-------------|-------|---------|
| POC (now) | Local, per-screen | 2-3 screens | Illustrate the concept |
| Product (later) | Global, user settings | All screens | Full customer-facing feature |

The global toggle would allow a user to set their preference once (e.g., "classic mode") and have every screen in EMS render in the classic EPNM style. This is architecturally more complex because it requires a user preference system and every screen must check that preference. The POC deliberately avoids this complexity.

### Colin's Azure Foundry Example

Colin showed a live example of the toggle concept during the meeting. He navigated to Azure Foundry (Microsoft's AI/ML platform) in his browser:

> "Like, for instance, this is Azure Foundry. This has a toggle to show the old version versus the new version. New version, you can see a completely different UI flow. But old version, let me search back, continue that feedback. You'll see that old version looks much different."

Guhan responded:

> "Thank you. So it's the same thing. It's essentially forking the UI. So back-end is kind of consistent between the two. It's just the look and feel."

This example served two purposes:

1. **Visual communication** -- rather than describing the toggle concept abstractly, Colin showed a real-world implementation from a major platform (Microsoft Azure), making it concrete.
2. **Architectural confirmation** -- Guhan immediately understood the pattern and stated its defining characteristic: "forking the UI" while the "backend is consistent." This confirmed alignment between Colin's understanding and Guhan's expectation.

### Backend Implications of the Toggle

Guhan was firm that the backend should not be rewritten:

> "And we don't want to rewrite the back-end services. So that can keep me honest. Because that's a lot of work. If we write all the back-end again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."

However, Selva introduced a nuance -- minor backend adjustments may be needed:

> "One thing is, for example, in the older UI, we might have given him ability to look at things with a different lens. And we sometimes may or may not have that. Let's say that I am... A crude example is I'm showing a certain functionality with a broader lens. I'm showing everything. Whereas the newer thing is like filtering things out and showing it with a certain lens. The converse may be true too. We may be doing the filtering in the older one. Now we are doing like a broader lens. So this means that there may be slight touch up to the back end to do that filtering. That's the kind of thing we expect."

This is a critical clarification. The rule is: **no backend rewrite**, but **minor API-level adjustments** (adding a filter parameter, changing a query scope) are expected and acceptable. The classic view may need data presented differently than the new view (broader vs. narrower lens), and the backend may need to accommodate both lenses.

Selva also raised a risk associated with any backend changes:

> "Any changes to the current server, because the current server is also getting updated. Next three months of coding is going to happen. With that... any service change we have, we are in the critical release path which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."

This is a significant constraint. The EMS backend is actively under development with a release path. Backend changes made for the classic view toggle could introduce regressions in either the new UI or the classic UI. If both break, there is no fallback. This is why backend changes must be minimized -- not just for effort reasons, but for risk reasons.

---

## Colin's Exponential Decay Explanation

### The Front-Loading Concept

Colin explained why the initial POC screens will take disproportionately longer than subsequent screens:

> "On Vscoping, because I know that is very important for this. So to say, here's how much time it took us to do the first part, here's how much time it'll take us to do the full tick of things. This does grow exponentially. So when it starts out, I think we'd said it would just be me working on this for the POC, but it's still fine. That is the slowest it will ever be."

Note: "Vscoping" is likely a speech-to-text artifact. In context, Colin is talking about "the scoping" or possibly "V-scoping" as in V-shaped scoping (broad to narrow). The key substance is the exponential growth claim: the per-screen rate improves exponentially over time.

Colin continued:

> "So it takes time to, there's that initial inertia just to get everything set up, learn the initial quirks of the system. Everything after that is kind of a multiplier for the speed. We'll still be able to scope that up perfectly, but don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just... kind of that initial front loading of getting everything set up, understanding everything, discoveries wrapped in there too."

Breaking this down into specific claims:

1. **Initial inertia** -- the first screens require setup work that is never repeated: environment configuration, codebase understanding, architecture mapping, agent development, pattern establishment.
2. **Multiplier effect** -- each subsequent screen benefits from the infrastructure and patterns built during earlier screens. The speed multiplies.
3. **Three weeks for the POC does not mean one week per screen.** Colin explicitly warned against this linear extrapolation. The three weeks include the one-time front-loading. The actual per-screen rate, once established, is much faster.
4. **Discovery is embedded in the timeline.** The first phase includes exploration and discovery, not just execution. This is the "understanding everything" phase.

### Selva's Clarifying Question

Selva asked Colin to confirm this dynamic later in the meeting:

> "On your earlier comment, I didn't quite catch, are you saying that initially it takes more time and then the subsequent ones will be even faster?"

Colin confirmed:

> "Yes, yes, by far. So typically what we see, and this is the first, it's almost like this exponential decay cycle truly, even the time-wise, the first time is us, first of all, understanding the problem. So there's that kind of onboarding period for us."

Colin used the term "exponential decay" deliberately. This is a mathematical metaphor: the time per screen decays exponentially as more screens are completed. The first screen takes the longest. The second takes less. The third takes even less. The curve flattens as it approaches a steady-state per-screen rate.

### How the Efficiency Gains Accumulate

Colin described the specific mechanisms that drive the exponential decay:

> "We're very good at that. So we won't need much hand holding once we have access to the code base. We go and have exploration happen. Even on this, I said we kind of build our own kind of map of the application. So we understand a lot more without having to ask SMEs. So we try to make that as painless as it can be. The only time we'll ask questions is if things contradict each other or things aren't in alignment or logically speaking."

The efficiency mechanisms, in order:

1. **Self-directed codebase exploration** -- BayOne builds its own understanding of the application without requiring constant SME access. This reduces the burden on Cisco's team.
2. **Application mapping** -- Colin's team creates their own map of the application architecture. This map accelerates every subsequent screen because the team already understands the system's patterns.
3. **Minimal SME interaction** -- questions are reserved for contradictions or misalignments, not for basic understanding. This is an explicit promise about how BayOne operates.
4. **Agent maturation** -- though not stated here, implied from the broader discussion: the conversion agents get better with each screen they process because they accumulate pattern knowledge.

### Implications for Estimation

This exponential decay dynamic has a critical implication for the estimation methodology discussed in Meeting 02. Guhan wanted a linear extrapolation: if 10 screens take X days, then Y screens take (Y/10) * X days. Colin is signaling that this model would be **overly pessimistic** because it treats the front-loaded first screens as representative of steady-state throughput.

The correct model, per Colin's explanation, would be:
- First N screens (with front-loading): X days
- Remaining screens (at steady-state rate): much less than (X/N) * remaining_count days

Colin did not push back on Guhan's linear model in Meeting 02, but in this meeting he is proactively setting the expectation that the POC's per-screen rate should not be linearly extrapolated.

---

## The Venn Diagram Approach to Feature Mapping

### Colin's Method for Mapping Old vs. New Functionality

Selva asked how Colin would identify functionality differences between EPNM and EMS:

> "How will you figure out things like, I mean, I'm able to do a certain functionality in this new UI, and then that functionality is not even, it was there or not even there in the previous one, you'd be able to figure out and analyze between how?"

Colin answered:

> "So that's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about, as you said. But for the start out, we would essentially not know. So we'd have to map that out."

Breaking this down:

1. **Venn diagram** -- the classic visualization of two overlapping sets. One circle is EPNM functionality; the other is EMS functionality. The overlap is functionality that exists in both. The non-overlapping portions are functionality unique to one product.
2. **Perfect circle overlap as the goal** -- for the screens being converted, the classic view in EMS should reproduce all the EPNM functionality that customers care about. A perfect circle means zero gaps -- every EPNM capability on that screen also works in EMS's classic view.
3. **"At least for the areas that the customers care about"** -- Colin is acknowledging that 100% functional parity may not be needed. If EPNM has capabilities that no customer uses, they need not be reproduced. The target is functional parity for customer-relevant features.
4. **"We would essentially not know"** -- at the start, the feature mapping does not exist. Neither BayOne nor Cisco has a comprehensive mapping of what is in EPNM vs. what is in EMS for any given screen. This mapping is a discovery deliverable.

### Agent-Driven Exploration Replaces Calendar Meetings

Colin then explained how this mapping would happen:

> "We like to do that because it actually makes our life easier. So rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore. And that helps us ask the right questions, so it's a lot more efficient."

This is a specific methodological claim: BayOne uses AI agents to explore codebases and build feature maps autonomously, rather than scheduling meetings with domain experts to manually walk through functionality. The agents generate the questions, not the people. This:

1. Reduces the time burden on Cisco's team (no hour-long walkthrough meetings for every screen).
2. Produces higher-quality questions (agents can be thorough; humans forget things).
3. Is faster (agents can explore 24/7; meetings require calendar coordination across time zones).

---

## Parallelizable Workflow

### Colin's Scaling Model

Colin described the total scope and the scaling approach:

> "So in terms of that, I think from a resource perspective, if we said, but there's I think in total 200, 250 screens, or workflow screens that will have you going, something like that. Now, I'll say this is a very parallelizable workflow."

Note: Colin is citing Cisco's own figures here -- 200-250 total workflow screens that need the classic view treatment. This is the first time a specific range has been stated for the full scope under the new toggle-based framing (as opposed to the earlier "missing functionality" framing).

Colin continued:

> "So once the foundation is there, once those agents are there, it's really just a matter of having people on our side to continue to run this and be the quality checkers."

This describes the post-POC execution model:

1. **Foundation** = the agents, tooling, patterns, and infrastructure built during the POC.
2. **Agents do the conversion work** -- generating the classic view UI code for each screen.
3. **People serve as quality checkers** -- humans review agent output rather than writing code from scratch.
4. **Multiple streams can run in parallel** -- because the agents are the bottleneck, not the humans, and agents can be replicated.

Colin elaborated on what parallel resourcing looks like:

> "For instance, for me it's like I would have a person dedicated to just the QA/QE agents, you know, and I would have a person doing this subset of screens, doing that batch, moving on to the next. I can get more done with more people in parallel."

The parallel streams Colin described:

| Stream | Focus | Personnel |
|--------|-------|-----------|
| QA/QE agents | Building and running automated verification agents | 1 dedicated person |
| Screen batch A | Converting a subset of screens using established patterns | 1 person |
| Screen batch B | Converting another subset of screens | 1 person |
| (Additional batches as needed) | Further screen subsets | Additional people |

Colin acknowledged the cost tradeoff:

> "Yes, that increases the shorter-term cost, but that gets you where you want to be faster. And it gets you there comfortably, so it's not like we're delivering on June 31st or June 30th for a July 1st deadline."

This is a direct pitch for investing in parallel resources: higher upfront cost, but faster delivery with comfortable margins. The June 30 / July 1 reference is tied to Guhan's interest in hitting the July release (discussed elsewhere in the meeting).

### Early Resource Mobilization

Colin also raised the lead-time concern for staffing:

> "Just think about it because that way we can start looking for people early on our side. So if we want to get some India resources to help accelerate this, if we do want to shoot for July, we can get a head start so we don't have a lag period after this initial deliverable is done."

This is a specific request for an early signal from Cisco on their appetite for the full engagement. If Cisco wants July delivery, BayOne needs to start recruiting and onboarding India-based resources now, not after the POC is complete. There is a lag period between deciding to scale and having the people ready. Colin is asking Cisco to make a directional decision -- even without final numbers -- so BayOne can prepare.

---

## Automated QA/QE Agents

### Colin's Vision for Automated Verification

Colin described a specific approach to automated quality assurance that extends the agent-based methodology:

> "There are going to be extra steps that we can throw into after the POC is done, which is kind of automated QA/QE for it. That doesn't have to replace, but instead to complement the existing QA/QE process."

Key framing:

1. **Post-POC enhancement** -- the automated QA/QE is not part of the initial POC deliverable. It is a follow-on capability.
2. **Complement, not replace** -- Colin is careful to position this as additive to Cisco's existing quality processes, not a replacement. This is politically important because suggesting replacement of Cisco's QA team would be threatening.

### User Persona Agents

Colin described the agent architecture:

> "So for instance, even if we wanted to set up like a user persona, train an agent to go and know the old interface and then say, you know, try this on the new interface, make sure that everything is matching. We can do that."

This describes a specific type of testing agent:

1. **User persona agent** -- an agent that embodies a particular user type (e.g., a network operator who primarily uses the faults screen).
2. **Trained on the old interface** -- the agent knows what the EPNM experience looks like and how workflows proceed in the legacy product.
3. **Tests the new interface** -- the agent then exercises the classic view in EMS and verifies that "everything is matching."
4. **Automated matching verification** -- the agent compares the classic view output to the expected EPNM behavior, flagging discrepancies.

Selva confirmed interest:

> "That would be great too."

Colin expanded:

> "We can even have an agent try this out on a classic content and then say this is matching with what was the experience. And we can do that from a number of different echos too."

Note: "echos" is likely a speech-to-text error. In context, Colin probably said "angles" or "vectors" -- meaning the testing can be done from multiple perspectives. For example:

- Different user roles (operator, administrator, read-only user)
- Different data states (empty system, system with thousands of faults, system under load)
- Different workflows (viewing faults, filtering faults, acknowledging faults, drilling into fault details)

### Customer-Specific Workflow Testing

Colin added a customer-specific dimension:

> "So like even for instance if there's a customer that uses a certain subset of screens or does a workflow..."

This suggests the automated QA/QE agents could be configured per customer: if Customer X primarily uses screens A, B, and C in a specific workflow sequence, an agent could be trained to replicate that specific workflow and verify it works in the classic view. This is a more sophisticated testing approach than generic screen-by-screen verification.

### Playwright for Test Automation

Colin mentioned the specific test automation tool:

> "...we use Playwright."

This is a brief but specific technical detail. Playwright is a browser automation framework (developed by Microsoft) that can programmatically interact with web applications -- clicking buttons, filling forms, navigating pages, and capturing screenshots. In this context, Playwright would be used to:

1. Automate the toggle interaction (switch between classic and new views).
2. Capture the rendered state of each view.
3. Compare the classic view rendering against expected EPNM behavior.
4. Execute workflow sequences (click fault, view details, acknowledge, return to list).

This is consistent with Colin's broader approach: agents generate the code, agents also verify the code, Playwright is the execution engine for the verification agents.

---

## Colin's Confidence Level

### Selva's Direct Question

Selva asked Colin a direct question about confidence:

> "What is your confidence level with respect to this quote-unquote, the same experience for customer, what they want? Without bugs and maybe we still have to release it with quality and it's going to be product of product. It's not a prototype. Eventually it will be product, right?"

This is a pressure-test question. Selva is clarifying that the POC output, while it is a proof of concept, must be production-quality. The phrase "product of product" (likely "part of the product") means the classic view toggle will ship to customers. It is not throwaway prototype code.

Colin's response:

> "Very high. Very high."

Colin then qualified the initial period:

> "I think one of the goals that I would have for this depends upon how comfortable everyone is. I know there's other initiatives at Cisco to go to what we'd say is like 100% AI generated code. This is a very good one where maybe not at first can we say that because at first we're going to need to pass a manual oversight of this."

Breaking this down:

1. **Very high confidence** in the overall approach.
2. **Manual oversight needed initially** -- the first screens will require human review of agent-generated code. This is the honest caveat.
3. **100% AI generated code as a trajectory** -- Colin is aware of other Cisco initiatives targeting fully AI-generated code. He positions this project as a candidate for that goal, but not from day one.

Colin continued:

> "Once we have a pattern established, this starts to take off. And that's the momentum that comes with these agentic workflows. Once you get those early kinks worked out, I won't be the guy that sits here and tells you it's going to be perfect on day one. It never is. But every iteration of this, it's a very iterative process, gets better."

This is a calibrated confidence statement:

1. Not perfect on day one -- explicitly stated.
2. Iterative improvement -- each cycle produces better results.
3. Pattern establishment is the inflection point -- once the pattern is locked in, the agents produce increasingly reliable output.

---

## POC Document Amendment

### Selva's Request

Selva asked Colin to update the existing POC proposal document to reflect the scope reframe:

> "And if you want to amend this document for that UI thing, you can do that."

"That UI thing" refers to the entire scope reframe: toggle-based classic view overlay instead of missing-functionality conversion. Colin agreed. This means the POC document shared in earlier meetings needs to be revised to reflect:

1. The classic view toggle concept (not missing functionality porting).
2. Local toggle per screen for the POC.
3. Faults and inventory as the target screens.
4. Backend remains untouched (with minor API adjustments as exceptions).
5. The parallelizable post-POC scaling model.

### The Existing POC Document

Colin had shared a POC document prior to this meeting (referenced at the start of the meeting: "This was the document I shared"). The document was screen-shared during the meeting. Guhan had reviewed it:

> "Overall, whatever you've given at this time, right, you've given multiple details and I mean intent is to do a few pages or a few areas like screens you said, right?"

Colin confirmed:

> "Yes, two or three representative screens are fully covered, converted."

The document as-written described a conversion approach. It now needs to be amended to describe a classic-view overlay approach. The core methodology (agents, Playwright, estimation model) likely remains, but the framing and scope description must change.

---

## The Acceptance Test Framework

### Guhan's End-to-End Verification Concept

Guhan described what the POC demonstration should look like:

> "We will say hey old way of doing this for example like faults right and then now you're doing new way of doing that and then switch and then say do some actions here, do some actions here and then final test will be to show the same thing comes up everywhere."

This describes a specific acceptance test scenario:

1. Start on a screen (e.g., faults) in the **new EMS view**.
2. Perform some actions (view faults, filter, interact).
3. **Toggle** to the classic view.
4. Perform the **same actions** in the classic view.
5. **Verify** that the results, data, and behavior are consistent -- "the same thing comes up everywhere."

This is functional equivalence testing. The toggle is not just cosmetic; the same operations must produce the same outcomes regardless of which view is active. This is the POC's acceptance criterion.

---

## The Repeatable Pattern Aspiration

### Guhan's Scale Concern

Guhan framed the repeatable pattern requirement:

> "Taking those inventory and other screens, converting that into auto-generate the classic UI based on that. And it's kind of a repeatable way to do that. Because you can always see where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently. And I think we have to."

This reveals an important organizational context:

1. **"Direction from the top"** -- Cisco leadership is pushing for efficiency. "10 screens, now there are 10 people" is a reference to the current state where each screen requires dedicated engineering effort. Leadership is asking for a more efficient model.
2. **"Think differently"** -- Guhan is explicitly acknowledging that the old model (one person per screen) is unsustainable. This is the opening for BayOne's agentic approach.
3. **"Repeatable way"** -- the POC must not just convert 2-3 screens but must establish a pattern that can be repeated at scale without proportional headcount.

Guhan continued:

> "How do we repeat this so we can probably generate more and more right I mean basically about all the screens and I like the way how it can be tested also verified that it is matching what the expectations with the classic customer view right with no changes to the back end preferably because any service change we have we are in the critical release path."

This statement bundles several requirements:

1. **Repeatable generation** -- the conversion process must be repeatable and scalable.
2. **Built-in verification** -- the testing/verification is as important as the generation. Guhan likes that the agent approach includes automated verification.
3. **No backend changes** -- reiterated as a strong preference, grounded in the practical constraint of the active release path.

---

## Open Questions and Unresolved Points

1. **What is the third POC screen?** Faults and inventory are confirmed. A possible third screen was implied ("two to three") but not named. This will likely be determined during the upcoming session with India domain experts.

2. **How will the local toggle be implemented technically?** The concept is clear (a toggle button on each screen page), but the technical implementation is unspecified. Options include: conditional rendering within the existing component, a parallel component that swaps in, a route-based switch with shared state. This is an implementation detail for Colin to propose.

3. **What constitutes "minor backend adjustment" vs. "backend rewrite"?** Selva acknowledged that some API-level changes may be needed for filtering/lens differences. The boundary between acceptable minor adjustments and unacceptable rewrites has not been defined. This could become a source of scope disagreement.

4. **How will the Venn diagram mapping be delivered?** Colin described the approach (agent-driven exploration, mapping EPNM vs. EMS functionality) but did not specify the deliverable format. Will it be a document? A spreadsheet? An automated report? This matters for Cisco's ability to use the mapping independently.

5. **When does automated QA/QE become available?** Colin positioned it as "after the POC is done." But the POC screens themselves need verification. Will the POC use manual QA, or will Colin build basic automated verification as part of the POC? The acceptance test framework (toggle, perform actions, verify matching) suggests at least some automation during the POC.

6. **What is the exact screen count under the new framing?** Colin mentioned "200, 250 screens, or workflow screens." This is the total scope for the full engagement, but it is unclear whether all 200-250 screens need a classic view toggle, or whether some are low-priority and can be excluded.

7. **How will Cisco's concurrent backend development affect the classic view?** Selva noted that "next three months of coding is going to happen" on the backend. If the backend APIs change during the period when classic views are being built, the classic views could break. There is no stated plan for coordination between the two streams.

8. **Who reviews and approves the amended POC document?** Selva asked Colin to amend the document, but it is unclear whether Guhan needs to approve it, whether Venkat (mentioned in the context of July timeline) needs to see it, or whether product management has a role.

---

## Key Quotes Index

For reference, the most important verbatim or closely paraphrased quotes from the transcript, organized by speaker and topic:

**Guhan on the toggle concept:**
- "How in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable."
- "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI."
- "We don't want to rewrite the back-end services. So that can keep me honest. Because that's a lot of work."

**Guhan on screen selection:**
- "Right now just for demonstrating POC let's say we pick two to three screens... for example like faults."
- "These are very common applications that customer usually go to."

**Guhan on the customer adoption driver:**
- "Our customers are asking that the operators are very used to a 10-year-old product. They can't just like that one thing, they don't want to learn everything."
- "We want the customers to go to this new product and the new thing. We don't want them to stick around with the older one."
- "This is going to push them in the right direction, is what we think."

**Guhan on the repeatable pattern:**
- "Where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently."

**Selva on the local toggle:**
- "We will do local toggle by that what I mean is let's say a faults screen... we'll just add a toggle to that very same page and say once you toggle it gives me the classic."
- "When we finally do the product, we may do it somewhere globally in the user setting."
- "We're going to pick three screens. We're going to have a local toggle one, each one another to keep it simple. Because you're just illustrating the idea."

**Selva on backend constraints:**
- "There may be slight touch up to the back end to do that filtering. That's the kind of thing we expect."
- "Any service change we have, we are in the critical release path which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI."

**Selva on amending the POC document:**
- "And if you want to amend this document for that UI thing, you can do that."

**Colin on exponential decay / front-loading:**
- "This does grow exponentially. So when it starts out, I think we'd said it would just be me working on this for the POC, but it's still fine. That is the slowest it will ever be."
- "It takes time to, there's that initial inertia just to get everything set up, learn the initial quirks of the system. Everything after that is kind of a multiplier for the speed."
- "Don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just kind of that initial front loading."
- "It's almost like this exponential decay cycle truly, even the time-wise."

**Colin on the Venn diagram:**
- "That's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about."
- "Rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore."

**Colin on screen diversity:**
- "There's the priority order, but there's also the diversity order. Diversity order helps us cover all the edge cases that we might miss with agents."

**Colin on parallelizable workflow:**
- "This is a very parallelizable workflow. So once the foundation is there, once those agents are there, it's really just a matter of having people on our side to continue to run this and be the quality checkers."
- "I would have a person dedicated to just the QA/QE agents... and I would have a person doing this subset of screens, doing that batch, moving on to the next."

**Colin on automated QA/QE:**
- "Automated QA/QE for it. That doesn't have to replace, but instead to complement the existing QA/QE process."
- "Set up like a user persona, train an agent to go and know the old interface and then say, try this on the new interface, make sure that everything is matching."
- "We use Playwright."

**Colin on confidence:**
- "Very high. Very high."
- "I won't be the guy that sits here and tells you it's going to be perfect on day one. It never is. But every iteration of this, it's a very iterative process, gets better."

**Colin on the Azure Foundry example:**
- "This is Azure Foundry. This has a toggle to show the old version versus the new version."
