# 01 - Meeting: Business Driver and Problem Restatement

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on business driver and problem framing

---

## 1. Guhan's Opening: The Two-Product Landscape

Guhan opened the meeting by establishing context about the two products at the center of this initiative:

- **EPNM** -- the legacy product. Not microservices-based. Has been in use by customers for approximately 15 years.
- **EMS (Element Management System)** -- the modern replacement. Microservices-based. Built with a new UI (Angular front-end). Represents the strategic direction Cisco intended to move toward.

Both products serve the same domain: "managing the network inventory, network topology, the entire customer's life cycle of automation starts with this element management."

Guhan's framing was clear that Cisco had made a deliberate, forward-looking investment in EMS: "we had developed the product, the later version of product with the new UI, modern UI and everything -- we thought this is where we wanted to go and we're still moving in the direction."

The word "thought" is notable. It signals that the original plan has been disrupted by customer feedback.

---

## 2. The Customer Pressure: Why the Old UI Must Come Back

Guhan articulated the business driver with directness:

> "There are some key customers who still believe that they're used to this legacy UI, which they have used it for 15 years or whatnot, right? They want to keep the same UI for their operations, right? Because otherwise, they have to learn. Network operators have to learn. They don't want to invest and go and do all those things, right?"

Key elements of this pressure:

- **Habitual use over 15 years.** These are not casual users. Network operators have built their workflows, muscle memory, and operational procedures around the EPNM interface for over a decade.
- **Resistance to retraining.** Customers explicitly do not want to invest in retraining their network operators on a new UI. This is framed as a cost and disruption they refuse to absorb.
- **Multiple customers, not one.** Guhan said "many customers are asking for" a return to the legacy UI. This is not a single-customer accommodation -- it is a pattern of demand.
- **Business-impacting.** Guhan used the phrase "this is a business impacting for those customers" -- meaning Cisco risks losing customers or damaging relationships if this is not addressed.

The customer sentiment, as Guhan translated it, amounts to: we were using something that worked for us, you built something new, but we want the thing that worked for us. Give it back.

---

## 3. The Product Strategy: Coexistence Is on the Table

Guhan described a product strategy that is deliberately unresolved at this stage:

> "EPNM UI is where they want to go. The EMS UI is probably what we will pitch to the newer customers. We don't know yet how we are going to manage with respect to who they're going to have. Both the UI are just going to be -- only one day. That's, we will leave it to product managers to decide also."

Decomposing this:

- **EPNM UI for legacy customers.** The customers asking for the old UI will get it. This has been decided.
- **EMS UI for new customers.** The modern UI will continue to be the offering for customers without the legacy attachment.
- **Coexistence is possible.** Both UIs may exist simultaneously in the same product. The decision of whether both persist long-term, or whether one eventually wins, is deferred to product management.
- **Not Guhan's decision to make.** He is explicitly leaving the product direction question to PMs. His concern is the engineering execution: making the old UI available in the new system.

The strategic posture is pragmatic: the decision has been made that the EPNM UI must exist in EMS. Everything else (long-term coexistence, customer segmentation) is downstream.

---

## 4. The Operational Goal: Move All Customers from EPNM to EMS

Guhan stated the migration objective clearly:

> "The idea is to move all the customers from EPNM into EMS. We need to move those guys here."

This is the overarching operational goal. Cisco wants to consolidate onto a single platform (EMS) and retire EPNM as a product. But to do that, EMS must be able to offer the legacy UI experience that EPNM customers depend on. Otherwise, those customers will not migrate.

The implication is that EPNM is being retired as a standalone product. Cisco does not want to maintain two separate product lines indefinitely. The solution is to bring the EPNM experience into EMS so that all customers -- legacy and new -- are on one platform, even if they see different UIs.

---

## 5. The Decision That Has Been Made

Guhan stated the key decision with finality:

> "One decision that's made is the EPNM UI, the older UI, needs to exist. That has to be given to the customers. Customers need to -- will be happy to use that."

This is not a proposal or an option being evaluated. The decision is made. The old UI must be available in EMS. The only question is how to execute it.

---

## 6. The Engineering Problem as Guhan Translated It

Guhan transitioned from business context to engineering framing:

> "So the problem, the engineering problem translated, is: we have a bunch of that code existing in EPNM. We need to have the -- and it's not just UI, it's also the backend. We need to have all the same user experience we need to provide in EMS."

He then described why this is not trivial:

> "One approach is let's take all that running here. It won't run directly because these two are two different architectures. One is microservices-based, other is different, and we have even done a lot of surgery on the older core, so they won't run as easily. Otherwise, we would have solved it by now."

Key engineering realities Guhan surfaced:

- **It is not just a UI problem.** The backend must come along with it. This is a full-stack conversion challenge.
- **Architectural incompatibility.** EPNM is monolithic (or at least non-microservices). EMS is microservices-based. You cannot simply lift-and-shift.
- **The old codebase has been modified.** Cisco has done "a lot of surgery on the older core," meaning the EPNM codebase is not in its original clean state. It has been patched, refactored, or partially dismantled over time.
- **If it were easy, it would already be done.** Guhan's statement "otherwise, we would have solved it by now" signals that this has been a known problem for some time and previous attempts or assessments have found it difficult.

---

## 7. The POC Challenge

Guhan framed the POC request:

> "The challenge for you, that you can choose to accept, is basically: can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS. So from a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything, the way they would do, interact with the EMS, same as what is there in EPNM."

The success criterion for the POC is clear: **customer-transparent equivalence.** The customer should not be able to tell whether they are using EPNM or EMS. The experience must be identical -- same visualization, same operations, same interaction patterns.

Guhan also noted that the team would help prioritize which screens to tackle first: "We can help prioritize a few of the UI and also we will also basically help you with which are the ones we want to try to begin with."

---

## 8. Why AI: An Unanticipated Workload

Guhan provided an important justification for using AI in this effort:

> "I just use AI because this entire thing is a work that we didn't anticipate, but it's important for -- let's say -- product."

This reveals several things:

- **This was not on the roadmap.** The conversion work was not planned. It emerged from customer pressure after Cisco had already invested in the new UI.
- **Budget and headcount were not allocated for it.** Since it was unanticipated, there is no existing team or budget carved out. AI-assisted conversion is being explored because it could make the work feasible without the full engineering investment that a manual conversion would require.
- **It is nonetheless critical.** Despite being unplanned, it is "important for product" -- meaning it is a business necessity that cannot be deferred indefinitely.

---

## 9. The Estimation Goal: POC as a Scoping Instrument

Guhan articulated what may be the most strategically important outcome of the POC -- not the demo itself, but the estimation data it produces:

> "There are like 70, 80, 100 pages -- we do not expect everything to be converted. We get a better idea of what it means to do that. In case of, like, for example, we are able to do 10 with this AI -- I mean, whatever infra you will develop also, right? We are able to do that in 10 screens, we can do it in, let's say, 10 days, we can do 17, 17 days -- some sort of estimation we can do based on this, right? With this, we can go back to the customer and promise that, okay, we will deliver this in this time."

Decomposing the estimation goal:

- **Total screen count: 70-80-100.** The full legacy UI surface is large. Guhan gave a range, not an exact number, suggesting the inventory has not been precisely catalogued.
- **Not all screens will be converted.** There is no expectation of 100% coverage. This will be a prioritized subset.
- **The POC should produce a conversion rate.** If 10 screens take X days, Cisco can extrapolate. This is the data they need.
- **The data feeds customer commitments.** Guhan explicitly stated that with this estimation, they can "go back to the customer and promise" delivery timelines. The POC is not just a technical proof -- it is a sales and customer management tool.
- **Infrastructure reusability matters.** Guhan referenced "whatever infra you will develop" -- indicating that the tooling, patterns, and processes created during the POC are expected to be reusable for the full conversion effort.

---

## 10. Selva's Refinement: Focus on Missing Functionality

Selva added a critical refinement to Guhan's framing:

> "There are some screens we have already brought in functionality with a new UI. There are still some functionality that's remaining in the old. Maybe, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens."

And further:

> "It's not a UI alone. There is a -- along with it comes the backend logic. Only then -- this is more EMS element management domain, right? So along with that, it needs to have a fully functional thing."

Selva then gave a concrete example:

> "For example, I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one, and bring -- for now, keep the same user experience -- and bring it to the new, and then make it work end-to-end."

Key points from Selva's refinement:

- **Do not re-do work that already exists.** Some EPNM functionality has already been brought into EMS (with a new UX design in some cases). The POC should not waste effort on those.
- **Focus on the gaps.** The highest-value work is converting functionality that exists only in EPNM and has no equivalent in EMS yet. These are the true blockers to customer migration.
- **Full vertical slices.** Each conversion must be end-to-end: UI plus backend logic. A front-end-only conversion is not useful.
- **Reports as a concrete example.** Selva identified missing reports as a specific category of unconverted functionality. This suggests reporting screens may be a natural candidate for the POC.
- **"Keep the same user experience."** Selva echoed Guhan's requirement -- the converted screens should preserve the EPNM user experience, not redesign it.

---

## 11. Team Availability and Independent Work Expectation

Guhan set expectations about team availability:

> "The team is also on critical or a platform -- the team itself will not be able to invest time here. But of course, they need to give you the context and everything. They will provide you with that. And then if you can take that independently and come back with your analysis and put that up with what you've come up with, that would be good."

And:

> "We'll have periodic checkpoints to help clarify anything more and also keep the rest of the folks aware of the progress."

This establishes the operating model:

- **The Cisco team is resource-constrained.** They are working on critical platform work and cannot dedicate sustained time to this effort.
- **Context transfer, then independence.** The team will provide initial context (code access, domain knowledge, screen prioritization) but then BayOne is expected to work independently.
- **Periodic checkpoints.** There will be recurring sync points, but not embedded collaboration.
- **Results must be demonstrable.** "Come back with your analysis and put that up with what you've come up with" -- meaning deliverables, not status updates.

---

## 12. Timeline Indicators and Urgency Signals

Several timeline data points emerged:

- **Four-week window.** Guhan stated: "We were looking at discussing about -- let's do it in four weeks, so then we made some important decisions around this." The four-week mark appears to be a decision point where results from the POC feed into broader strategic decisions.
- **Two-week hardware gap.** Colin's Cisco laptop is expected within one to two weeks. Guhan tried to figure out what work could happen in the interim: "I'm trying to figure out what we can do in the next two weeks to get you going."
- **Guhan wants estimation data to take to customers.** The urgency is not abstract -- there are customer conversations waiting on this data.
- **"Important decisions" hinge on this.** Guhan's phrasing ("we made some important decisions around this") suggests that the POC outcome will directly influence product strategy and resource allocation decisions.

---

## 13. The POC as a Confidence-Builder

Colin framed the POC's purpose from BayOne's perspective:

> "That's the investment I want to make for you, is to show that -- because I know this is important -- I know I can send you a million case studies saying we can do it, but sometimes the proof is in the pudding, and it's better to really show the capability, so you can have that confidence as well."

And Guhan confirmed the dual purpose of the POC:

> "If we have to also get the additional resources for this, which we will have to work through, this will help. Show it, even to make it -- show the demo and showing that this is how we have done it, this is what is working, and then it will help you get more confidence."

The POC serves multiple audiences:

- **Guhan and Selva** need estimation data and proof that the approach works.
- **Customer-facing teams** need timelines to commit to.
- **Internal stakeholders** (likely Arun, Anand) need confidence to approve additional resources for the full conversion effort. The POC demo becomes the justification for budget and headcount.

---

## 14. Selva's Domain Gap Concern

Selva raised a substantive concern about domain fidelity:

> "How do you try to bridge the gap for the domain level thing, right? Because, obviously, these projects are in various domains that you've taken up, and this one is in element management. And how do we ensure that there's no gap in what we bring over? This may not have the readily available prior -- asks for you to go rerun them on the new one. How do you make sure that there's no domain gap or no functionality gap?"

This question reveals Selva's concern: AI-assisted conversion might produce code that looks right but misses domain-specific behavior that only someone with deep element management knowledge would catch. It is a concern about functional fidelity, not just visual fidelity.

---

## 15. Code and Documentation Reality

Guhan acknowledged the documentation situation:

> "This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

And on code health, when asked whether the EPNM codebase is well-organized:

> "As a product, we are going to retire that. So when you say good health... maybe not between the features, but yes, it's tightly coupled to -- like, as a monolith, it's not microservices. It's all -- like, we really need to borrow things and bring it in."

Key realities:

- **No reliable design documentation.** The legacy system's behavior must be understood from the code itself.
- **Tight coupling within the monolith.** Extracting specific functionality from EPNM is not as simple as pulling out a module. Things are intertwined.
- **The team has done this extraction before.** Selva noted: "that's kind of the exercise the team did for previous ones" -- meaning there is institutional experience with this type of extraction, but it is labor-intensive.
- **Some prior conversions involved UX redesign.** "In some cases, we also went through a new UX design and the user experience. Some areas it turned out to be plus, some areas it's not." The mixed reception of the redesigned UX is part of what drove the demand for the legacy UI.

---

## 16. Security and Access Model

Guhan established firm security requirements:

> "This is Cisco code, so we don't want this code to get out of Cisco."

Requirements stated:
- All work must happen on Cisco hardware.
- Cisco-licensed AI tools must be used (not external licenses).
- No code downloaded to personal laptops.
- Use of Cisco protocols within Cisco infrastructure.

Colin confirmed compliance and noted that the team working on Anand's CI/CD project has the same NDA coverage and will receive Cisco hardware.

---

## Summary: The Problem as Stated

The business problem, as articulated across both Guhan and Selva's statements, can be decomposed into these layers:

1. **Customer demand:** Key customers with 15+ years on EPNM refuse to adopt the new EMS UI and want their familiar interface back.
2. **Strategic decision:** Cisco has decided the EPNM UI must exist within EMS. This is not optional.
3. **Migration goal:** All customers must eventually move from EPNM (as a standalone product) to EMS. The legacy UI in EMS makes this possible for resistant customers.
4. **Engineering challenge:** The two systems have fundamentally different architectures (monolith vs. microservices). The old code is tightly coupled and has been surgically modified. Conversion is a full-stack problem (UI + backend).
5. **Resource constraint:** This work was not anticipated and no team is allocated to it. The existing team is occupied with critical platform work.
6. **POC objective:** Produce working converted screens AND estimation data. The estimation data is arguably more valuable than the demo itself, because it enables customer commitments.
7. **Scope refinement:** Focus on functionality that has NOT yet been brought into EMS, not on re-doing what already exists.
8. **Timeline pressure:** Four weeks to produce results that feed into "important decisions." Customer commitments are waiting on this data.
