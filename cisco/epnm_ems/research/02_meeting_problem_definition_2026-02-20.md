# 02 - Meeting: Problem Definition

**Source:** /cisco/epnm_ems/source/guhan_selva-2-20-2026.txt
**Source Date:** 2026-02-20 (Follow-Up Technical Meeting)
**Document Set:** 02 (Second meeting, deeper technical detail on EPNM-to-EMS conversion)
**Pass:** Focused deep dive on the precise problem definition

---

## Overview

This document captures the precise technical problem definition as articulated in the February 20, 2026 follow-up meeting. The meeting included Guhan (Cisco engineering leadership), Selva (Cisco technical lead), and Colin Moore (BayOne Director of AI). This was the second meeting, and the conversation immediately went deeper on the two-product architecture, the nature of the functionality gaps, and what "conversion" actually means in practice. Where the first meeting (2026-02-09) framed the problem at a strategic level, this meeting established the engineering reality.

---

## The Two Products

### EPNM (Legacy Product)

Guhan opened the meeting by defining both products. EPNM is the legacy product. His exact framing:

> "We have two products, one is the legacy one, which is called EPNM, and a modern version of that, the microservices based, is called the Element Management System."

EPNM is described as the established product that customers have used for **15+ years**. The significance of that tenure was stated directly:

> "Some key customers who still believe that they're used to this legacy UI, which they have used it for 15 years or whatnot, right? They want to keep the same UI for their operations."

The product's domain is network management: network inventory, network topology, and the full customer lifecycle of automation that begins with element management. Guhan framed this domain as foundational:

> "These are all basically managing the network inventory, network topology, the entire, the customer's life cycle of automation starts with this element management."

### EMS (Modern Product)

EMS is the modern replacement. It is microservices-based, and Cisco has invested approximately **two years** in building it with a new UI:

> "We have invested, spent, and then after two years we have built the [new] UI."

Guhan described the intent behind EMS as forward-looking -- this is the direction Cisco still wants to go:

> "We had developed the product, the later version of product with the new UI, modern UI and everything we thought this is where we wanted to go and we're still moving in the direction."

He also positioned EMS as the product for future customers:

> "The EMS UI is [what] we will probably pitch to the newer customers."

### The Unresolved Strategic Question

Guhan explicitly acknowledged that the final product strategy -- whether both UIs will coexist permanently or one will eventually replace the other -- has not been decided:

> "We don't know yet how we are going to manage with respect to who they're going to have. Both the UI are just going to be only one [product]. That's, we will leave it to product managers to decide."

This is a significant admission. The engineering work is proceeding before the product strategy is finalized. The reason is customer pressure: Guhan stated that "this is a business impacting for those customers."

---

## The Two Architectures

### EPNM: Monolithic

Colin confirmed directly:

> "Between EPNM, that's the older platform that is not microservice-based. Is that right?"

Guhan's answer was unambiguous:

> "No, it is not microservices based."

Selva further clarified the coupling characteristics:

> "It's tightly coupled to, like, as a model, it's not microservices. It's all, like, we really need to borrow things and bring it in."

This tight coupling is explicitly not between features (feature A to feature B) but structural -- the architecture itself is monolithic, so extracting any single capability requires disentangling it from the monolith:

> "Maybe not between the features, but yes, it's tightly coupled to, like, as a model."

### EMS: Microservices

Colin confirmed:

> "And then EMS is the more modernized one, the newer one that we're trying to move to... And that would be microservice based."

Guhan's confirmation:

> "Yeah, it is microservices."

### Technology Stacks (Confirmed in This Meeting)

Selva provided explicit technology details that were only inferred in the first meeting:

**Backend:**

> "The backend is in Java, in both."

Both products use Java on the backend. This is a significant detail -- the backend language itself is not the migration barrier.

**EPNM Frontend:**

> "The older thing, use Dojo, others like the technologies of those types. There will be some Angular, but you'll not see a lot of Angular. It's all JavaScript and Dojo kind of thing."

The EPNM frontend is primarily **Dojo** (a legacy JavaScript framework) with minor Angular presence. This is the first explicit confirmation of Dojo from a Cisco team member.

**EMS Frontend:**

> "But in the microservices one, it's all Angular."

The EMS frontend is entirely **Angular**.

---

## Why Direct Code Porting Does Not Work

This is the central engineering constraint. Guhan stated it explicitly:

> "One approach is let's take all that [EPNM code] running here. It won't run directly because these two are two different architectures. One is microservices based, other is different and we have even done a lot of surgery on the older core, so they won't run as easily."

There are **three distinct reasons** the code cannot be directly ported:

### Reason 1: Architectural Mismatch

The two products have fundamentally different architectures. EPNM is monolithic; EMS is microservices. Code written for a monolithic runtime does not simply transplant into a microservices runtime. The assumptions about deployment, communication between components, state management, and data access are different at every layer.

### Reason 2: Surgery on the Legacy Core

Guhan used the word "surgery" specifically:

> "We have even done a lot of surgery on the older core."

This means the EPNM codebase is not in its original form. It has been modified -- presumably as part of the EMS migration effort or ongoing maintenance -- such that even the old code itself has changed. The implication: you cannot take the EPNM code as a clean starting point because it has already been altered.

### Reason 3: If It Were Easy, It Would Be Done

Guhan directly addressed why this problem still exists:

> "Otherwise, we would have solved it by now."

This is a critical statement. The Cisco engineering team has already attempted to bring this code over. They know the barriers firsthand. The problem is not a matter of will or staffing -- it is a genuine technical challenge that has resisted straightforward solutions.

---

## The Vertical Nature of Functionality Gaps

This is one of the most important technical details from the meeting. Colin asked whether the missing functionality was primarily frontend or backend:

> "From the new interface to the old, you said there's still some backend work remaining. Is it major backend work that's also pending on it, or is that something that is [familiar]?"

Selva's answer established the vertical nature of the gaps:

> "It's usually vertical. If something was not brought in the frontend, the corresponding backend is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

This is a fundamental framing. When functionality is missing from EMS, it is not a case where the backend exists but the UI was never built. The entire vertical slice -- UI, API layer, backend logic, data access -- is absent. Converting a screen is therefore not a frontend exercise alone. Each screen carries its own backend requirements.

Selva reinforced this repeatedly:

> "It's not a UI alone. There is a, I mean, along with it comes the backend logic only then [it works]. This is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

And further:

> "We can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new. And then make it work end-to-end, right? So that will be the goal for this exercise."

The key phrase here is **"end-to-end."** Each converted screen must be a fully functional vertical slice, not a UI shell over incomplete plumbing.

---

## What Has Already Been Done vs. What Remains

### Some Functionality Already Converted

Selva stated that some EPNM capabilities have already been brought into EMS, but with a redesigned user experience:

> "There are some screens we have already brought in functionality with a new idea."

For the capabilities that were brought over, the team did not simply replicate the EPNM UI -- they redesigned it:

> "In some cases, we also went through a new UX design and the user experience. I mean, some areas it turned out to be [positive], some areas it's not."

This redesign was not universally well-received. The customer feedback in some cases was that they wanted the original experience:

> "I think the feedback in some cases was, can I get the same experience? So that's where we are looking into this one."

### Remaining Functionality

Selva stated that the conversion effort for the POC should target what has **not** been brought over:

> "There are still some functionality that's remaining in the old. Maybe, I mean, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens."

He gave a concrete example of missing functionality:

> "I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new."

### Prioritization Responsibility

Both Guhan and Selva stated that Cisco's team will identify which screens to convert first:

Guhan: "We can help prioritize few of the UI and also we will also basically, I mean basically we'll help you prioritize and we'll help you with which which are the ones we want to try to begin with."

Selva: "The team will help identify what those are and provide you with the overall thing."

---

## Customer Demand for Identical Legacy Experience

### The Nature of the Demand

Guhan stated the customer requirement directly:

> "They want to keep the same UI for their operations. Because otherwise, they have to learn. Network operators have to learn. They don't want to invest and go and do all those things."

This is not an aesthetic preference. These are **network operators** -- people who manage production network infrastructure. They have learned the legacy interface over 15 years. Asking them to relearn is asking their employers to invest in retraining, accept productivity loss during transition, and risk operational errors during the learning curve.

Guhan framed it as a multi-customer demand, not isolated:

> "This is something that many customers are asking for, going back to the, let's call it legacy UI."

### The Required Fidelity

Guhan was specific about what "same experience" means:

> "From a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything, the way they would do, interact with the [EMS], same as what is there [in EPNM]."

The key requirements decomposed:
1. **Same experience** -- the workflow and interaction model must match
2. **Same visualization** -- the visual rendering must match
3. **Same operations** -- the functional capabilities must match
4. **Backend transparency** -- customers should not know or care what architecture runs behind the interface

---

## The Decision Already Made

Guhan stated one decision has been made with certainty, even while the broader product strategy remains open:

> "One decision that's made is the EPNM UI, the older UI needs to exist, that has to be given to the customers, customers need to, will be happy to use that."

This is a firm engineering commitment, not a suggestion. The EPNM-style UI must be available in EMS. The question is how to deliver it, not whether to deliver it.

The long-term coexistence question (one UI or both) remains with product management:

> "We will leave it to product managers to decide."

But the immediate engineering requirement is clear: make the legacy experience available.

---

## The Migration Direction

A subtle but important detail: the stated direction is to move **all** customers from EPNM to EMS:

> "The idea is to move all the customers from EPNM into EMS. We need to move those guys here."

This means EPNM is intended to be retired as a product. The legacy UI must exist within EMS, but it is EMS that will be the surviving product. Customers will not stay on EPNM; they will be migrated to EMS with the legacy UI available as an option within EMS.

Selva confirmed from a different angle that EPNM as a product is end-of-life:

> "As a product, we are going to retire that."

---

## Scale of the Conversion

### Screen Count

Guhan referenced the total scope:

> "There are like 70, 80, 100 pages."

This is lower than the "200 screens" mentioned in the first meeting (02-09). Whether this is a revised number, a different counting methodology, or a subset of the original 200, is unclear. It may be that 200 represents total EPNM screens while 70-100 represents screens not yet converted.

### Expectation Management

Guhan was explicit that the POC will not convert everything:

> "We do not [expect] everything to be converted."

The real deliverable from the POC is an estimation methodology:

> "We get a better idea of what it means to do that. In case of like, for example, we are able to do 10 [screens] with this AI... we are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this."

The downstream use of that estimation:

> "With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

This confirms the POC has a dual purpose:
1. **Prove the approach works** -- demonstrate that AI-assisted conversion produces functional results
2. **Establish a rate** -- create a per-screen estimation that can be extrapolated to the full scope and committed to customers

---

## Code Health and Documentation

### Code Organization

Colin asked about the health of the EPNM codebase. Selva's answer was nuanced:

> "When you say good health..."

He clarified that feature-to-feature coupling may not be severe, but the monolithic coupling is:

> "Maybe not between the features, but yes, it's tightly coupled to, like, as a model, it's not microservices."

The key phrase: **"we really need to borrow things and bring it in."** This implies a selective extraction process, not a wholesale migration. Each piece of functionality must be identified, extracted from the monolith, and transplanted into the microservices environment.

### Documentation

Selva explicitly stated that legacy product documentation is limited:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

This is a critical constraint. The primary source of truth for what EPNM does and how it does it is the code itself. There is no reliable design documentation to guide the conversion. This makes the code exploration phase essential -- understanding the system requires reading the system.

Colin acknowledged this is normal for legacy systems:

> "For the most part, especially with anything legacy, almost always is missing documentation... Because documentation doesn't always tell the truth."

---

## The Engineering Challenge (Guhan's Framing)

Guhan framed the challenge as a proposition:

> "The challenge for you, that you can choose to accept, is basically can you take that [EPNM code], provide a working code, show us the demo, taking some of the [screens] on the backend of the EPNM, run it in the [EMS]. So from a customer point of view, they don't know what is running behind and everything."

Decomposed, the challenge has these components:
1. **Take EPNM code** -- start with the existing legacy implementation
2. **Provide working code** -- produce functional output, not analysis or documentation
3. **Show a demo** -- the result must be demonstrable, not theoretical
4. **Backend included** -- it is not just UI; backend logic from EPNM must come along
5. **Run it in EMS** -- the converted code must operate within the EMS microservices architecture
6. **Customer transparency** -- the end result must be indistinguishable from the original EPNM experience

---

## The Justification for AI

Guhan framed the use of AI as a necessity driven by the unexpected nature of the work:

> "I just [want to] use AI because this entire thing is a work that we didn't anticipate so but it's important for let's say product."

This is telling. The EPNM-to-EMS conversion was not in the original plan. It emerged from customer demand after Cisco had already invested two years in building EMS with its new UI. Now they must add the old UI experience on top of the new architecture, and the engineering team is already committed to other critical platform work:

> "The team is also on critical [work] or a platform, if you think so, the team itself will not be able to [dedicate] time here."

So the situation is:
- Unanticipated work that must be done
- Engineering team cannot be pulled from existing commitments
- AI-assisted conversion is the mechanism to accomplish it without traditional staffing

---

## What "Conversion" Actually Means

Based on the meeting's discussion, "conversion" is not a single operation but a multi-layered process:

1. **Identify the EPNM screen and its functionality** -- what does this screen do, what data does it show, what operations does it support?
2. **Trace the vertical slice** -- identify the UI code (Dojo/JavaScript), the API calls, the backend Java logic, and the data access patterns
3. **Extract from the monolith** -- disentangle the functionality from EPNM's tightly coupled architecture
4. **Reimplement in EMS architecture** -- rebuild the backend as appropriate microservices, rewrite the UI in Angular, reconnect the data flows
5. **Preserve the user experience** -- the resulting screen must look and behave identically to the EPNM original
6. **Validate end-to-end** -- the converted screen must be fully functional, not just visually similar

This is not a code transpilation exercise. It is a full-stack reimplementation guided by the legacy code, operating within a fundamentally different architectural paradigm.

---

## Guhan's Domain Gap Concern

Guhan raised a pointed question about domain expertise:

> "How do you try to [bridge] the [gap] for the domain level thing, right? So because, obviously, these projects are in various domains that you've taken up, right? And this one is in element management. And how do we ensure that there's no [gap] in what we bring over, right? I mean, this may not have the readily available prior [knowledge]."

This question reveals Guhan's awareness that element management (network inventory, topology, automation lifecycle) is a specialized domain. Generic code conversion tools or approaches may miss domain-specific semantics. A report that shows network topology data is not just a table of values -- it has domain meaning that must be preserved.

He further pressed:

> "How do you make sure that there's no domain gap or no functionality gap?"

This concern was directed specifically at whether AI-assisted conversion can handle domain-specific logic without prior exposure to the element management domain. It is a legitimate engineering concern and one that the POC will need to address directly.

---

## Open Questions and Unresolved Points

### From This Meeting

1. **Screen count discrepancy** -- The first meeting referenced ~200 screens. This meeting referenced 70-100 pages. Whether these are different counts of the same thing, or whether 70-100 is the unconverted subset of 200, is not clarified.

2. **Which screens will be selected for the POC** -- Cisco's team will identify and prioritize, but no specific screens were named in this meeting beyond "missing reports."

3. **The "surgery" on EPNM** -- Guhan mentioned surgery on the old core but did not specify what was changed, when, or why. Understanding what was modified would help assess how much the current EPNM code diverges from its original state.

4. **Product coexistence strategy** -- Will both UIs permanently coexist in EMS, or will the legacy UI be a transitional bridge? This is deferred to product management.

5. **Backend decomposition complexity** -- Selva confirmed the gaps are vertical, but the complexity of extracting backend logic from a monolith into microservices was not quantified. Some vertical slices may be simple (a report that queries a database), others may be deeply entangled (an operation that touches multiple subsystems).

6. **Data model compatibility** -- Both products use Java backends, but whether they share the same data model, database schema, or data access patterns was not discussed. If the data models differ, the backend conversion is significantly more complex.

7. **Running instances for testing** -- Colin asked about access to running instances of both products. Guhan indicated these would be provided "when ready" but no timeline was set. Without running instances, end-to-end validation is not possible.

8. **The relationship between "new UX design" screens and "legacy UI" screens** -- Some functionality was brought into EMS with a new UX design. Customers rejected some of those redesigns and want the old experience. Does the POC need to address screens that were already converted with new UX but need to revert to legacy UX, or only screens that were never converted at all?

---

## Key Terminology Established in This Meeting

| Term | Meaning |
|------|---------|
| **EPNM** | Evolved Programmable Network Manager -- the legacy, monolithic network management product |
| **EMS** | Element Management System -- the modern, microservices-based replacement product |
| **Vertical** | A full-stack slice of functionality (UI + API + backend + data), not just a single layer |
| **Surgery** | Modifications already made to the EPNM core codebase, complicating direct code extraction |
| **Same experience** | Functional and visual equivalence with the legacy EPNM UI, as perceived by network operators |
| **End-to-end** | A converted screen must be fully operational, not just visually rendered |
| **Dojo** | The JavaScript UI framework used in the EPNM frontend |
| **Angular** | The JavaScript UI framework used in the EMS frontend |
| **Missing reports** | A specific example Selva gave of functionality not yet brought from EPNM to EMS |

---

## Comparison: What Was Known After Meeting 01 vs. Meeting 02

| Topic | After Meeting 01 (02-09) | After Meeting 02 (02-20) |
|-------|--------------------------|--------------------------|
| Product names | Inferred from context, not explicitly stated in transcript | Explicitly stated: EPNM and EMS |
| Architecture | Inferred (legacy vs. modern) | Confirmed: monolithic vs. microservices |
| Frontend tech | Referenced in topic map only | Confirmed by Selva: Dojo vs. Angular |
| Backend tech | Not stated | Confirmed: Java in both products |
| Nature of gaps | Described as "UI gaps" | Clarified as vertical (UI + backend together) |
| Screen count | ~200 screens | 70-100 pages (possible subset or revised count) |
| Why porting fails | Not discussed at this level | Three reasons: architecture mismatch, surgery on core, proven difficulty |
| Customer demand | "Major customers" want old UI | "Many customers" want it; 15+ years of usage cited |
| Decision status | Strategic tension between convert vs. leapfrog | Decision made: legacy UI must exist in EMS |
| Documentation | Not discussed | Confirmed: minimal, code is the primary source of truth |
| Code coupling | Not discussed | Confirmed: tightly coupled monolith, not between features |
| Investment in EMS | Not quantified | Two years of development |
| EPNM end-of-life | Not stated | Confirmed: "as a product, we are going to retire that" |
