# 03 - Meeting: Scope Reframe — Classic View Toggle

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Focused deep dive on the scope reframe from full-stack conversion to classic view toggle

---

## Overview

This document captures the single most consequential development in the EPNM-to-EMS engagement to date: a fundamental reframe of the project scope. In Sets 01 and 02 (February 9 and February 20, 2026), the project was understood as converting **missing functionality** from EPNM into EMS — full-stack vertical work where both UI and backend were absent from EMS and needed to be built. The March 25 meeting revealed a completely different scope: the project is about adding a **"classic view" toggle** to screens that **already exist** in EMS. The backend stays the same. This is a UX overlay, not a full-stack conversion.

The reframe was initiated by Selva, confirmed and reinforced by Guhan, and recognized immediately by Colin as a material change to the engagement. Every statement related to this reframe is decomposed below.

---

## What Was Understood After Sets 01 and 02

Before documenting the reframe, it is essential to establish what the prior understanding was. The following statements were treated as confirmed after the first two meetings:

### From Set 01 (February 9, 2026)

Guhan framed the core problem as missing capabilities in EMS:

> "It is about, it's not an agentic product, it's a traditional network management product, but modernized product. With capabilities that were previously in the previous version is missing, the previous generation is missing, especially on the UI."

The engagement was understood as converting approximately **200 UI screens** from the legacy EPNM product to the modernized EMS product. The emphasis was on the UI layer, but the backend was implied to be included.

### From Set 02 (February 20, 2026)

The second meeting deepened this understanding significantly. Selva provided the key clarification that the missing functionality was **vertical** — not just UI, but the entire stack:

> "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

Selva reinforced this repeatedly:

> "It's not a UI alone. There is a, along with it comes the backend logic. Only then this is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

The POC scope was understood as focusing on **functionality not yet ported to EMS** — specifically, "missing reports" that had not been brought over from EPNM. Selva stated:

> "There are still some functionality that's remaining in the old. Maybe, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens."

Guhan set the POC challenge explicitly:

> "The challenge for you, that you can choose to accept, is basically can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS."

### The Established Understanding Going into March 25

Based on Sets 01 and 02, the project was understood as:

1. **Identifying EPNM functionality that does not exist in EMS** (screens, reports, operations)
2. **Converting that functionality vertically** — UI, API, backend logic, data access — into the EMS microservices architecture
3. **Rewriting the UI from Dojo/JavaScript to Angular** while preserving the legacy user experience
4. **Reimplementing the backend** within EMS's microservices framework
5. **Producing a fully functional end-to-end result** — not a UI shell, but operational code

This was a full-stack conversion engagement. The code did not exist in EMS. It had to be built.

---

## The Reframe: How It Was Introduced

### Selva's Opening Clarification

Selva introduced the reframe early in the meeting, approximately after initial pleasantries and a review of the POC proposal document Colin had shared. He prefaced it carefully:

> "I wanted to, what I wanted to clarify is that is one thing, right? So today we have EMS screens and then we have the EPNM which is the old product. What we wanted to — like maybe this didn't come out as clear in the first meeting..."

The phrase "maybe this didn't come out as clear in the first meeting" is significant. Selva acknowledged that the first two meetings left a different impression. He is not saying Colin misunderstood. He is saying the communication was unclear on Cisco's side.

### The Outlook/Banking App Analogy

Selva then introduced the analogy that defines the reframed scope:

> "We are looking at, you know, like how in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable. And then I want to switch to the new thing."

This analogy establishes the model precisely:
- A product ships a new UX
- Users are given the option to toggle back to the old experience
- Over time, users adopt the new experience
- Eventually, the old experience is deprecated

This is the exact pattern Cisco wants to implement. Users of EMS would be able to toggle between the new EMS UX and a "classic" view that replicates the EPNM experience.

### The Core Statement: Screens Already Exist

Selva then delivered the sentence that rewrites the engagement scope:

> "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI. But obviously, it's been redesigned to adopt a new workflow, a new UX and everything."

This directly contradicts the Set 02 understanding. In Set 02, Selva stated that missing functionality "doesn't exist like all the way down." In this meeting, Selva is saying the screens they will target **do exist** in EMS — both backend and UI are present. The issue is not absence but redesign: the EMS versions have a new UX that customers find unfamiliar.

### The Marriage Metaphor

Selva described the goal using a specific metaphor:

> "Take that UX and that experience, marry it with the backend that's already there in the system."

Decomposed:
1. **"That UX and that experience"** — the EPNM-style user experience (the classic, familiar workflow)
2. **"The backend that's already there"** — the EMS backend, which is operational and does not need to be rebuilt
3. **"Marry it"** — create a connection between the old UX design and the existing EMS backend

This is not a conversion. It is a UX overlay. The backend is a given. The work is to create an alternative UI presentation that uses the same backend services.

### Selva's Explicit Negation of Missing Functionality

Selva then explicitly stated what the project is NOT:

> "So in a sense, it's along the lines of what you've said, and we're not looking for missing functionalities, but we are looking for things that are there but gives us the same user [experience]."

The phrase "we're not looking for missing functionalities" is a direct negation of the Set 02 framing. In Set 02, the entire discussion was organized around what was missing from EMS and needed to be brought over. Here, Selva is saying the functionality is already present — the task is to present it differently.

---

## Guhan's Reinforcement of the Reframe

### The Customer Adoption Driver

Guhan reinforced the reframe from the business perspective. He explained why this matters:

> "Our customers are asking that the operators are very used to a 10-year-old product. They can't just like that — one thing, they don't want to learn everything. They're asking us two or three, two releases or something, like a year, like a couple of releases or two or three. So we keep classic and the new."

Decomposed:
1. **Operators are used to a 10-year-old product** — the EPNM interface has been in use for at least a decade
2. **They don't want to learn everything** — the objection is not to specific missing features but to the entire new user experience
3. **Two or three releases** — customers are asking for a transition period of roughly two to three release cycles (approximately one year)
4. **"Keep classic and the new"** — the word "classic" is the label for the EPNM-style experience; it coexists with the new EMS experience

The word "classic" is introduced here as the working name for the legacy-style view. This is the "classic view toggle" concept.

### The UI Fork

Guhan used a different, more technical framing:

> "So it's the same thing. It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."

The word "forking" is significant. In engineering terms, a fork creates two parallel versions from a common base. Here, the common base is the EMS backend. The fork produces two UI presentations: the current EMS UX and the classic EPNM-style UX. Both share the same backend services.

Guhan stated this as a one-sentence summary: **"It's just the look and feel."**

### The Explicit Backend Prohibition

Guhan was emphatic about not touching the backend:

> "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work. If we write all the backend again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."

This is a firm constraint, not a guideline. Guhan gave three reasons for the prohibition:

1. **Effort:** "That's a lot of work" — rewriting backend services would multiply the scope
2. **Maintenance burden:** "We have to maintain two different versions" — dual backends create ongoing operational cost
3. **Staffing reality:** "We're not staffed" — the team does not have the people to support two backends
4. **Engineering judgment:** "It's not the right way to do it" — even if they had the resources, it would be architecturally wrong

### Guhan's Most Definitive Statement

The single most important statement from Guhan on the scope reframe:

> "We are not trying to reboot the backend from older, right? That's not something what we want him to do."

"Him" refers to Colin. Guhan is telling Selva (and Colin) that the engagement does not include backend work from the old system. The word "reboot" implies starting the backend over from the EPNM version — that is off the table.

---

## The Nuance: Minor Backend Changes May Be Needed

### Selva's Lens/Filter Explanation

While the reframe eliminates full-stack backend conversion, Selva acknowledged that minor backend adjustments may be necessary:

> "One thing is, for example, in the older UI, we might have given him ability to look at things with a different lens. And we sometimes may or may not have that. Let's say that I am... A crude example is I'm showing a certain functionality with a broader lens. I'm showing everything. Whereas the newer thing is like filtering things out and showing it with a certain way. The converse may be true too. We may be doing the filtering in the older one. Now we are doing like a broader lens. So this means that there may be slight touchup to the backend to do that filtering."

Decomposed:
1. **Different lens** — the EPNM UI and EMS UI may present the same data differently. One might show all data unfiltered; the other might apply filters.
2. **Converse may be true** — the filtering difference could go either direction. EPNM might have shown everything while EMS filters, or vice versa.
3. **"Slight touchup to the backend"** — minor API changes to support different filtering or data presentation, not full backend reimplementation.
4. **"That's the kind of thing we expect"** — this is the boundary of acceptable backend work. It is additive (adding a filter or removing one) rather than constructive (building new backend services from scratch).

### Selva's Characterization of Backend Touch

Selva then connected this to the reframe:

> "Guhan is absolutely right. We're not trying to reboot the backend from older, right? That's not something what we want him to do."

And then:

> "So basically here you're saying I'm bringing in something vertically which does not exist. So we also weighed in all of this..."

The phrase "here you're saying I'm bringing in something vertically which does not exist" is Selva referencing Colin's POC proposal document, which was written based on the Set 01/02 understanding. Selva is acknowledging that the document described a vertical, full-stack conversion — and then implicitly saying that is not what the project actually is.

---

## Selva's Warning: Server-Side Changes Are Dangerous

Later in the meeting, after Guhan had departed, Selva issued a specific warning about backend changes:

> "Any changes to the current server, because the current server is also getting updated. With no changes to the backend preferably, because any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."

This is a risk assessment, not just a preference:

1. **The server is actively being updated** — the EMS backend is under active development by Cisco's team for the upcoming release
2. **Critical release path** — the July release is a firm target with real customer commitments
3. **Risk of breakage** — if BayOne's work introduces server-side bugs, it could break both the new UI and the classic UI simultaneously
4. **"No way to go either way"** — a server-side regression could leave Cisco with neither a working new UI nor a working classic UI

This dramatically elevates the importance of the backend constraint. It is not just about scope control — it is about risk management for a production release.

---

## Colin's Immediate Recognition of the Change

Colin recognized the scope change immediately and stated it directly:

> "This is actually in a good way. It changes the scope. It reduces it a little bit. Because I was thinking we were going to have to do the whole backend."

This is Colin acknowledging that the Sets 01/02 understanding included backend work, and that this reframe eliminates that backend work from the engagement.

### Selva's Partial Pushback

Selva gently pushed back on the idea that the scope is reduced:

> "To me, I don't think it changes the scope that much. Whatever you have here still applies. For example, I told you this. Sometimes you may need to go touch the backend to do this particular API. Since we are not presenting a certain information in a certain way, I'm not having a corresponding backend API. So you may need to do that corresponding thing to make it happen. So which is similar to what you have mentioned here."

Selva's argument: the work described in Colin's POC document (exploring the codebase, understanding the screens, building conversion tooling) still applies. The difference is that instead of building something from nothing, you are building an alternative presentation of something that already exists. But the exploration, understanding, and tooling work is comparable.

This is a nuanced point. The scope has fundamentally changed in nature (from full-stack conversion to UX overlay), but the effort for the POC phase may not change as dramatically because much of the POC effort is front-loaded with exploration and tooling, regardless of whether the output is a full-stack build or a UX toggle.

---

## The Business Rationale: Customer Renewal and Migration

### Selva's Revenue and Renewal Framing

Selva placed the classic view toggle squarely in a business context:

> "This is one of the things, at least it's been in our minds, and then it's been top of my mind also, to improve the customer adoption. This is one of the challenges we are having. See, when it comes to renewal, we want the customers to go to this new product and the new thing. We don't want them to stick around with the older one."

Decomposed:
1. **Customer adoption is a challenge** — customers are not voluntarily moving from EPNM to EMS
2. **Renewal pressure** — Cisco wants customers to renew on EMS, not EPNM
3. **Revenue fungibility** — "Either one of them will give us the revenue" — Cisco gets revenue whether customers are on EPNM or EMS, but they want them on EMS for strategic reasons

### The Phase-Out Strategy

Selva continued:

> "We really want to phase out the old one and then go on the new one. That's where we're doing all the new things, cool things. We're not planning to sustain the old thing forever."

This establishes the classic view toggle as a **transitional mechanism**, not a permanent feature:
1. The old product (EPNM) will be retired
2. All new development is happening on EMS
3. The classic view exists to ease the transition, not to preserve the old product indefinitely
4. Eventually, the classic view itself will be removed ("over time we say okay we're going to take away your old view")

### Guhan's Phase-Out Vision

Guhan articulated the end state:

> "And then over time we say okay we're going to take away your old view. This is the only view right now."

The lifecycle is:
1. **Phase 1:** EMS has only the new UX (current state — causing customer resistance)
2. **Phase 2:** EMS gets a classic view toggle (the project being discussed)
3. **Phase 3:** Customers use classic view as a comfort bridge while learning the new UX
4. **Phase 4:** Classic view is deprecated and removed; new UX is the only option

This is explicitly modeled on the Outlook and banking application pattern that Selva referenced.

---

## The Azure Foundry Example

Colin demonstrated a real-world example of the toggle pattern during the meeting:

> "Like, for instance, this is Azure Foundry. This has a toggle to show the old version versus the new version. New version, you can see a completely different UI flow. But old version... you'll see that old version looks much different."

This was shown via screen share. It served as a concrete visual reference for what the classic view toggle would look like in practice. The Azure Foundry example demonstrates:
1. A product with a new and old version toggle
2. The old version has a visually distinct UI
3. The toggle is accessible from within the product
4. Both versions are fully functional

---

## Scope of the Toggle: Local vs. Global

### POC: Local Toggle Per Screen

Selva described the toggle implementation for the POC:

> "For the toggle, as I said, let's not worry too much about the UX. There is a separate UX team. We didn't want to involve them here. So this is like we can keep it simple and say we will do local toggle. By that what I mean is, let's say a fault screen for example, right? That's the one I want to give you. You want to take in this new product and you want to give an equivalent classic experience. We'll just add a toggle to that very same page and say once you toggle it gives me the classic."

Decomposed:
1. **Local toggle** — the toggle is per-screen, not application-wide
2. **Simple implementation** — no need to involve the UX team for the POC; this is a functional demonstration, not a polished UX deliverable
3. **On the same page** — the toggle is embedded in the existing EMS screen, switching between the new view and the classic view

### Product: Global Toggle

Selva then described the eventual product vision:

> "But when we finally do the product, we may do it somewhere globally in the user setting or somewhere where they say, and then the whole experience is going to be classic."

The product version would have a global user preference: set your entire experience to classic or new, and all screens follow that preference.

### POC Simplification

Selva explicitly scoped the POC toggle as simple:

> "Now, let's say we're going to pick three screens. We're going to have a local toggle on each one — one, each one, another — to keep it simple. Because you're just illustrating the idea."

Three screens, each with its own local toggle. The goal is to demonstrate the concept, not to deliver a production-ready toggle system.

---

## Target Screens for the POC

Selva and Guhan identified the initial screens:

> "So, we also prioritized — like because there are multiple screens, there are screens that we want to first start. Like the fault, and I think, is it inventory or?"
>
> Guhan: "It's inventory, yeah."

The two confirmed POC screen candidates are:
1. **Faults** — fault management screens (alarm/event monitoring)
2. **Inventory** — network inventory screens (device/element tracking)

Selva explained why these were selected:

> "These are very common applications that customer usually go to."

These are high-traffic, high-visibility screens that operators use daily. Demonstrating the classic view toggle on these screens would have the highest impact on customer adoption.

### The Full Scale

Colin referenced the total scope of screens that would eventually need classic view toggles:

> "There's, I think in total 200, 250 screens, or workflow screens that will have you going."

This is a significant number. The POC covers 2-3 screens. The full engagement would cover 200-250. This is the gap that the POC estimation methodology must bridge.

---

## How This Contradicts Sets 01 and 02

The scope reframe creates several direct contradictions with the understanding established in the first two meetings.

### Contradiction 1: Missing Functionality vs. Existing Functionality

**Set 02 understanding:** "There are still some functionality that's remaining in the old. We will focus on the ones that we've not brought in yet." (Selva, February 20)

**Set 03 reality:** "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI." (Selva, March 25)

These are opposite statements. In February, the POC was to target functionality that had **not** been brought into EMS. In March, the POC targets functionality that **already exists** in EMS.

### Contradiction 2: Vertical Full-Stack vs. UX Overlay

**Set 02 understanding:** "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down." (Selva, February 20)

**Set 03 reality:** "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel." (Guhan, March 25)

In February, the work was described as building complete vertical slices from nothing. In March, the backend is explicitly off-limits and the work is UI-only.

### Contradiction 3: Backend Reimplementation vs. Backend Preservation

**Set 02 understanding:** "It's not a UI alone. There is a, along with it comes the backend logic. Only then this is more EMS element management domain." (Selva, February 20)

**Set 03 reality:** "And we don't want to rewrite the backend services. We're not trying to reboot the backend from older." (Guhan, March 25)

In February, backend logic was a core part of the deliverable. In March, touching the backend is prohibited except for minor API adjustments.

### Contradiction 4: Missing Reports vs. Faults and Inventory

**Set 02 understanding:** "I have some missing reports that I've not brought in from the old thing. So we can look at how it looks in the old one and bring it to the new." (Selva, February 20)

**Set 03 reality:** The POC screens are faults and inventory — both of which already exist in EMS with full backend and UI. Reports are not mentioned.

The starting example changed entirely. Missing reports (something that does not exist in EMS) were replaced by faults and inventory (things that already exist in EMS).

### Possible Explanation for the Contradictions

These contradictions may be explained by one of the following:
1. **The scope genuinely evolved between meetings.** Between February 20 and March 25, Cisco's internal discussions (possibly driven by Venkat or product management) may have shifted the priority from filling functional gaps to accelerating customer adoption.
2. **The first two meetings were exploring multiple problems.** Sets 01 and 02 may have touched on several aspects of the EPNM-to-EMS transition, and what was described as "the project" was actually one of several possible engagement scopes. The March 25 meeting narrowed to a specific, different scope.
3. **Selva's acknowledgment:** His statement "maybe this didn't come out as clear in the first meeting" suggests Cisco may have always had the classic view toggle in mind but failed to communicate it clearly, leading BayOne to understand a broader full-stack conversion scope.

Regardless of the explanation, the March 25 meeting establishes the **operative scope** going forward. Sets 01 and 02 understanding is superseded.

---

## What Stays the Same Despite the Reframe

Not everything changed. Several elements from Sets 01 and 02 carry forward:

1. **The customer pressure is the same driver.** Operators want the familiar experience. This was stated in all three meetings.
2. **The POC serves a dual purpose.** It must demonstrate capability and produce an estimation methodology. This was stated by Guhan in Set 02 and reaffirmed in Set 03.
3. **The AI-accelerated approach is still the value proposition.** Using agents to generate and verify the classic views at scale.
4. **The working demo requirement is unchanged.** Guhan still wants working code and a demonstrable result.
5. **Cisco selects the screens.** BayOne executes; Cisco prioritizes. Same division of responsibility.
6. **The codebase exploration effort is comparable.** Colin still needs to understand both codebases (EPNM for the classic UX patterns, EMS for the target platform). The exploration work described in the POC proposal still applies.
7. **The estimation methodology is still a key deliverable.** How long per screen, extrapolated to the full set.
8. **All work on Cisco hardware with Cisco tools.** Security constraints unchanged.

---

## The Footprint Argument

Guhan raised an additional technical argument against dual backends:

> "If you write, if you have two different backup, multiple backup services, it will also increase your footprint. You have to be cautious about it."

"Footprint" here refers to the deployment footprint — the amount of compute, memory, and infrastructure required to run EMS. Running two separate backend service stacks would double the operational footprint. In network management products deployed in customer environments (not just cloud), footprint is a real constraint.

---

## Guhan's Banking Application Elaboration

After the initial reframe, Guhan provided an extended analogy using banking applications:

> "So, a typical thing is your banking applications, right? Like, everyone does it. Those are all cloud applications. So they say, I'm used to doing this transfer here. I'm used to looking at a summary, and even Outlook. I'm used to doing certain things like layout. So when Outlook rolled out, I remember myself doing this. When I upgraded, I said, OK, I'm not going to use the new UI because I have 10 things to handle. I don't have time to handle your new UI thing right now. But gradually, when I got the time, I switched it and then saw, oh, this looks much nicer. And then over time I said this is my default view. That's what we want to do with the users."

This is Guhan speaking from personal experience. The progression he describes:
1. Upgrade forces new UI on the user
2. User resists because they are busy and cannot afford the productivity hit of learning
3. User toggles back to the old view
4. Eventually, at their own pace, the user tries the new view
5. The user recognizes the new view is better
6. The new view becomes the default

This is the adoption curve Cisco is trying to engineer for their network operator customers. The classic view toggle is the mechanism that enables this gradual transition.

---

## The Document Amendment

Colin had prepared a POC proposal document (shared and reviewed during the meeting). Based on the reframe, Selva asked Colin to update it:

> "And if you want to amend this document for that UI thing, you can do that."

Colin acknowledged this. The POC document, which was written based on the Set 01/02 understanding of full-stack vertical conversion, needs to be updated to reflect the classic view toggle scope.

Selva described what the updated document should reflect:

> "This document, that's the running thread you want to be, because in a sense it's bringing in screens and tying it with the backend thread. It doesn't change. But the slight twist to that is, it's an existing thing. And then we'll also show you how it exists in the old product. And then by that you have your UX and everything there from the old product. And then you get to see what is here. And then you bring that screen here."

The "slight twist" is the reframe itself: the screens exist, the backend exists, and the work is to bring the old UX to the existing new product, not to build something from scratch.

---

## The Toggle Lifecycle in Detail

Selva described how the toggle would work in the POC:

> "Right now we will do a local toggle, because eventually when everything is done we want to say global toggle saying that you want to do the old one or the new one. Right now just for demonstrating POC, let's say we pick two to three screens. We will say, hey, old way of doing this — for example like faults, right? — and then now you're doing new way of doing that. And then switch. And then say do some actions here, do some actions here. And then final test will be to show the same thing comes up everywhere."

The POC demonstration sequence:
1. Show the faults screen in its current EMS UX
2. Toggle to the classic view
3. Perform operations in the classic view
4. Perform the same operations in the new view
5. Verify that the results are consistent across both views ("the same thing comes up everywhere")

This last point is critical — the verification test is that both views produce identical results because they share the same backend. The views are different; the data and operations are the same.

---

## The "Direction from the Top" Statement

Selva made a reference to executive pressure that further contextualizes the reframe:

> "Because you can always see where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently. And I think we have to. So that's why the AI, your expertise needed."

Decomposed:
1. **"Direction from the top"** — executive leadership (likely Venkat or above) is pushing this
2. **"10 screens, now there are 10 people"** — the traditional approach of one person per screen is being challenged
3. **"We are being asked to think differently"** — this is not organic; it is a directive
4. **"That's why the AI, your expertise needed"** — AI-accelerated development is the "think differently" approach

This connects to Venkat's push for the July release timeline (referenced elsewhere in the meeting). The executive pressure is to deliver more screens faster with fewer people, using AI acceleration.

---

## Colin's Confidence Assessment

Guhan directly asked Colin about his confidence level:

> "What is your confidence level that we can do this automated AI way without having to burn lots of resources?"

Colin's response:

> "Very high."

Colin then elaborated on the pattern-based acceleration:

> "Once we have a pattern established, this starts to take off. And that's the momentum that comes with these agentic workflows. Once you get those early kinks worked out, I won't be the guy that sits here and tells you it's going to be perfect on day one. It never is. But every iteration of this, it's a very iterative process, gets better. And the more diversity of the screens that we encounter, it's a good way for us to even plan what screens. Because there's the priority order, but there's also the diversity order. Diversity order helps us cover all the edge cases that we might miss with agents."

Key points:
1. **High confidence** — Colin is confident in the AI approach
2. **Pattern-based** — the first screens establish patterns; subsequent screens leverage those patterns
3. **Not perfect on day one** — honest about iterative improvement
4. **Diversity matters** — screen variety is important for building robust agents, not just business priority
5. **Priority order vs. diversity order** — two different sequencing strategies that need to be balanced

---

## Open Questions and Unresolved Points

### 1. What Happened to the "Missing Functionality" Scope?

In Set 02, Selva described missing reports and vertical functionality gaps. In Set 03, the scope is about existing functionality. Are the missing reports still a concern? Will they be addressed separately? Or was that scope absorbed into the classic view toggle project? This is unresolved.

### 2. How Different Are the EPNM and EMS UX Patterns?

The reframe assumes that the EPNM UX can be overlaid on the EMS backend. But if the EMS backend APIs return data in a different structure or granularity than what the EPNM UI expected, the "slight touchup" to the backend could become more substantial. The actual complexity is unknown until specific screens are examined.

### 3. What Is the Boundary Between "Slight Touchup" and "Backend Rewrite"?

Selva acknowledged that minor backend API changes may be needed for filtering/lens differences. But there is no defined threshold for what constitutes a minor change versus a scope-violating backend modification. This boundary will need to be negotiated on a screen-by-screen basis.

### 4. Will the Classic View Be Pixel-Perfect or Functionally Equivalent?

The meeting uses phrases like "same experience" and "same user experience." But the classic view is running on a different backend (EMS, not EPNM). If there are data differences, timing differences, or behavioral differences between the two backends, the classic view may not perfectly replicate the EPNM experience. The fidelity standard has not been precisely defined.

### 5. What Is the UX Team's Role?

Selva mentioned not wanting to involve the UX team for the POC ("We didn't want to involve them here"). But the UX team will presumably need to be involved for the product version. At what point does the UX team engage? What is their authority over the classic view design?

### 6. Does the Reframe Affect the 200-250 Screen Count?

In Sets 01 and 02, the screen count reflected missing functionality. If the scope is now about existing screens that need a classic view toggle, is the 200-250 number the same? It may be larger (every EMS screen could theoretically need a classic view) or smaller (only screens where customers have complained about the new UX).

### 7. How Does the Classic View Handle EMS-Only Features?

If EMS has features or data views that did not exist in EPNM, what happens to those in classic view? Are they hidden? Shown but styled differently? This edge case was not discussed.

### 8. Does Venkat Know About the Scope Reframe?

Selva referenced Venkat pushing for July delivery, but it is unclear whether Venkat's expectation is aligned with the classic view toggle scope or the original full-stack conversion scope from Sets 01 and 02. If Venkat expects full-stack conversion by July, the reframe may create a disconnect.

---

## Key Quotes Index

**Selva on the reframe:**
- "Maybe this didn't come out as clear in the first meeting."
- "We are looking at, you know, like how in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle."
- "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI."
- "Take that UX and that experience, marry it with the backend that's already there in the system."
- "We're not looking for missing functionalities, but we are looking for things that are there but gives us the same user [experience]."
- "Any changes to the current server... we are in the critical release path."

**Guhan on the reframe:**
- "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."
- "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work."
- "We are not trying to reboot the backend from older, right? That's not something what we want him to do."
- "That's what we want to do with the users. We want to give them and then over time we say okay we're going to take away your old view."

**Colin on recognizing the change:**
- "This is actually in a good way. It changes the scope. It reduces it a little bit. Because I was thinking we were going to have to do the whole backend."

**Selva on the business rationale:**
- "This is one of the challenges we are having. See, when it comes to renewal, we want the customers to go to this new product."
- "We really want to phase out the old one and then go on the new one."
- "We are being asked to think differently. And I think we have to. So that's why the AI, your expertise needed."

**Selva's pushback on scope reduction:**
- "To me, I don't think it changes the scope that much. Whatever you have here still applies."

**Selva's server-side warning:**
- "Any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."
