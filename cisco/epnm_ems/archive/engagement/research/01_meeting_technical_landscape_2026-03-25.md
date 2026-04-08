# 01 - Meeting: Technical Landscape and Conversion Challenge

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Focused deep dive on technical architecture and conversion challenges

---

## 1. The Two Products: EPNM and EMS

Guhan opens the meeting by establishing the two-product landscape. His exact framing:

> "We have two products, one is the legacy one, which is called EPNM, and a modern version of that, the microservices based, is called the Element Management System. These are all basically managing the network inventory, network topology, the entire, the customer's life cycle of automation starts with this element management."

Key points from this opening:

- EPNM is explicitly called "the legacy one"
- EMS is explicitly called "a modern version of that"
- EMS is immediately described as "microservices based" - this is the first architectural descriptor offered
- Both products serve the same domain: network inventory, network topology, and customer automation lifecycle
- Element management is the foundational layer - "the customer's life cycle of automation starts with this element management"

### 1.1 EPNM Architecture

Colin asks directly: "So between EPNM, that's the older platform that is not microservice-based. Is that right?"

Guhan confirms: "No, it is not microservices based."

This is a clean confirmation: EPNM is monolithic.

### 1.2 EMS Architecture

Colin follows up: "And then EMS is the more modernized one, the newer one that we're trying to move to... And that would be microservice based."

Guhan confirms: "Yeah, it is microservices."

### 1.3 Summary of Architecture Split

| Attribute | EPNM | EMS |
|-----------|------|-----|
| Generation | Legacy | Modern |
| Architecture | Monolithic | Microservices |
| Status | Being retired (per Guhan) | Active development target |
| Customer base | Established, 15+ years | Newer customers, plus migrated customers |

---

## 2. Technology Stacks

Colin asks: "So from this, what is the stack for either of them? Is there like a primary language that they're in or are they using some framework?"

Guhan/Selva's response covers both backend and frontend:

### 2.1 Backend

> "The back-end is in Java, in both."

This is unambiguous. Both EPNM and EMS share Java as the backend language.

### 2.2 Frontend - EPNM

> "Front-end, the older thing, use Dojo, others like the technologies of those types. There will be some Angular, but you'll not see a lot of Angular. It's all JavaScript and Dojo kind of thing."

Breakdown:
- Primary framework: **Dojo** (a JavaScript toolkit, popular in enterprise applications roughly 2005-2015)
- Some Angular presence, but explicitly minimized: "you'll not see a lot of Angular"
- The characterization "JavaScript and Dojo kind of thing" suggests a mix of raw JavaScript and Dojo-specific patterns, not a clean single-framework application

### 2.3 Frontend - EMS

> "But in the microservices one, it's all Angular."

Clean, unambiguous: EMS frontend is entirely Angular.

### 2.4 Stack Summary

| Layer | EPNM | EMS |
|-------|------|-----|
| Backend | Java | Java |
| Frontend | Dojo + JavaScript, some Angular | All Angular |

---

## 3. The "Vertical Work" Concept

This is one of the most critical technical insights from the meeting. Colin asks about the nature of the remaining backend work:

> Colin: "From the new interface to the old, you said there's still some back-end work remaining. Is it major back-end work that's also pending on it, or is that something that is familiar?"

The response (from Selva, based on conversational flow):

> "It's usually vertical. If something was not brought in the front-end, the corresponding back-end is also not working. So it's more vertical. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."

This is a critical statement that reframes the entire scope of work. Key implications:

1. **This is not a UI-only conversion.** When a screen is missing from EMS, the entire functionality stack for that screen is missing - frontend, backend logic, data layer, everything.
2. **"Doesn't exist all the way down"** means there is no backend stub or partial implementation waiting for a frontend. The work was either done completely (full vertical slice) or not done at all.
3. **The word "vertical" is used twice** - this is deliberate terminology, not casual. It signals that the prior porting effort was done in vertical slices (complete features, top to bottom), and whatever was left behind was left behind entirely.
4. **Scope multiplier:** What might appear to be "just bring over 70-80 screens" is actually "bring over 70-80 complete feature stacks including their backend services, data models, and API integrations."

This has massive implications for the POC and for estimation. A screen count understates the work by potentially an order of magnitude.

---

## 4. "Surgery on the Older Core" - Conversion Feasibility

Guhan provides the most technically revealing statement about why this conversion is hard:

> "One approach is let's take all that running here. It won't run directly because these two are two different architectures. One is microservices based, other is different and we have even done a lot of surgery on the older core, so they won't run as easily. Otherwise, we would have solved it by now."

Unpacking this statement piece by piece:

### 4.1 "It won't run directly"

The naive approach of "copy the EPNM code into EMS" does not work. The code cannot simply be transplanted.

### 4.2 "Two different architectures"

The monolith-to-microservices gap is explicitly called out as the reason for incompatibility. Even though both backends are Java, the architectural patterns (service boundaries, communication patterns, deployment models, dependency injection, configuration management) are fundamentally different.

### 4.3 "Done a lot of surgery on the older core"

This is the most loaded phrase. "Surgery on the older core" means the EPNM codebase was modified - possibly extensively - during the process of building EMS. This could mean:
- Shared libraries were extracted and modified for EMS, leaving the EPNM versions incompatible
- Core abstractions were refactored, so EPNM code references interfaces or classes that no longer exist in their original form in EMS
- Database schemas diverged
- The "surgery" may have been done to enable parts of EPNM to work with EMS during the initial migration, breaking EPNM's internal consistency

### 4.4 "Otherwise, we would have solved it by now"

This is an admission that the team has already considered and rejected the simple transplant approach. They know from experience (not just theory) that the code cannot be moved over trivially. This is not a hypothetical concern - it's a known, validated obstacle.

### 4.5 Feasibility Framing

Guhan frames the POC challenge explicitly around this:

> "So the challenge for you, that you can choose to accept, is basically can you take that experiment, provide a working code, show us the demo, taking some of the [screens] on the backend of the EPNM, run it in the [EMS]."

The word "experiment" is notable. Guhan is not asking for a guaranteed deliverable - he is asking for an experimental proof that this kind of conversion can work at all.

---

## 5. Code Organization and Coupling

Colin probes code health, and the exchange reveals important details:

> Colin: "From the way that it sounds, even on the old system, I was going to ask about the general code health. Because sometimes that's one of the drivers to move to a new framework or just new architecture for the system. But it sounds like actually, if it's a vertical, it probably is already fairly good health, the old code base."

> Guhan: "I mean, as a product, we are going to retire that. So when you say good health..."

> Colin: "So good organization of the code. It's not kind of tightly coupled between all the different features."

> Guhan: "Maybe not between the features, but yes, it's tightly coupled to, like, as a monolith, it's not microservices. It's all, like, we really need to borrow things and bring it in."

### 5.1 Coupling Analysis

This exchange reveals a nuanced coupling situation:

- **Feature-to-feature coupling:** Relatively low. Individual features may be reasonably self-contained in terms of their business logic. Colin's intuition that vertical slicing implies decent feature isolation has some validity.
- **Feature-to-monolith coupling:** High. Features are tightly coupled to the monolithic infrastructure - shared services, common frameworks, the monolith's runtime environment, shared data access patterns, etc.

The practical implication: you can identify a feature's code, but you cannot extract it without also bringing along (or replacing) a large number of monolith-level dependencies. The features are like organs in a body - each has a distinct function, but they share the circulatory system, nervous system, and skeletal structure of the monolith.

### 5.2 "Borrow Things and Bring It In"

Guhan's phrase "we really need to borrow things and bring it in" describes the prior approach the team used. This was not a lift-and-shift. It was a selective extraction ("borrow") followed by adaptation ("bring it in"). This is confirmed by the next statement about the team's prior work.

---

## 6. Prior Porting Work: What Has Been Done

Selva provides critical context about the previous migration effort:

> "There are some screens we have already brought in functionality with a new idea. There are still some functionality that's remaining in the old."

And Guhan elaborates:

> "That's kind of the exercise the team did for previous ones. And in some cases, we also went through a new UX design and the user experience."

### 6.1 What Was Done

- Some screens/features were migrated from EPNM to EMS
- The migration included both frontend and backend (consistent with the "vertical" nature)
- During migration, a **new UX design** was applied - the screens were not ported as-is but redesigned
- The team "borrowed" code from EPNM and adapted it for EMS's microservices architecture

### 6.2 What Was Not Done

- A significant number of screens/features remain in EPNM only
- Guhan estimates "70, 80, 100 pages" of screens exist in total (though he clarifies not all are expected to be converted in the POC)
- Selva specifically calls out **reports** as a concrete example of missing functionality:

> "For example, I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new."

### 6.3 POC Strategy: Focus on Unported Screens

Selva explicitly directs the POC toward screens that have NOT yet been brought to EMS:

> "Maybe, I mean, just to add more value to this exercise, we will focus on the ones that we've not brought in yet and identify a few screens, like Guhan has said."

This means the POC is not re-doing work that was already done. It is tackling the backlog of screens that the internal team has not yet migrated.

---

## 7. The UX Redesign Situation

This is one of the more complex dynamics in the meeting. The EMS migration was not just a technical port - it included a UX overhaul. This created a new problem.

### 7.1 What Happened

Guhan's opening frames it:

> "We had developed the product, the later version of product with the new UI, modern UI and everything we thought this is where we wanted to go and we're still moving in the direction."

So EMS was built with a modern UI, presumably following current UX design principles (Angular-based, responsive, etc.).

### 7.2 Customer Pushback

> "But there are some key customers who still believe that they're used to this legacy UI, which they have used it for 15 years or whatnot, right? They want to keep the same UI for their operations, right? Because otherwise, they have to learn. Network operators have to learn. They don't want to invest and go and do all those things, right?"

Key details:
- The pushback is from "key customers" (i.e., important, likely large accounts)
- Customers have used the EPNM UI for "15 years or whatnot" - deeply ingrained operational muscle memory
- The concern is about operational disruption: network operators would need retraining
- Multiple customers are involved: "this is something that many customers are asking for"

### 7.3 The Ask: Legacy UI on Modern Architecture

> "So this is something that many customers are asking for, going back to the, let's call it legacy UI."

And later:

> "So from a customer point of view, they don't know what is running behind and everything. They have the same experience, same visualization, everything, operations, everything, the way they would do, interact with the [EMS], same as what is there [in EPNM]."

The goal is explicit: the customer should have the EPNM visual experience running on EMS infrastructure. The backend can be modern; the frontend must feel legacy.

### 7.4 Mixed Results of UX Redesign

Guhan acknowledges the UX redesign had mixed results:

> "In some cases, we also went through a new UX design and the user experience. I mean, some areas it turned out to be plus some areas it's not."

This is a candid admission: the UX redesign was beneficial in some areas but not others. For screens where the new UX was not well received, the customer demand is to revert to the legacy experience.

### 7.5 Current Strategic Position

> "EPNM UI is where they want to go. The EMS UI is [what] we will probably pitch to the newer customers."

This suggests a potential dual-UI strategy:
- Legacy EPNM-style UI for existing/migrating customers
- Modern EMS-style UI for new customers

But Guhan notes the final decision is unresolved:

> "We don't know yet how we are going to manage with respect to who they're going to have. Both the UI are just going to be only one [day]. That's, we will leave it to product managers to [decide]."

### 7.6 Implication for POC

Selva reframes the POC focus in light of this:

> "Rather than first focusing on reworking some of that, there are missing functionalities too. So then it will be probably useful to look at that."

Translation: instead of re-doing screens that were already ported with new UX (and potentially reverting the UX), focus the POC on screens that haven't been ported at all. This is more immediately valuable and avoids the UX debate.

---

## 8. Documentation State

Colin asks about documentation. The response is revealing:

> "I mean, there is like some cases... This is also a legacy product. You wouldn't have a solid design documentation to that level. So it will be trying to find the way around the code and trying to bring that into the view, right? Most of it. That will be the bulk of the challenge here."

### 8.1 Key Phrases

- **"You wouldn't have a solid design documentation to that level"** - Design documentation is explicitly acknowledged as insufficient or absent for the legacy EPNM product.
- **"Trying to find the way around the code"** - The primary method of understanding EPNM functionality is code exploration, not documentation review.
- **"That will be the bulk of the challenge here"** - Code comprehension, not conversion, is identified as the biggest challenge. Understanding what the code does is harder than the actual porting work.

### 8.2 Colin's Response

Colin normalizes this:

> "For the most part, especially with anything legacy, almost always is missing documentation. It's way easier to do it now, so we're kind of modern day cheating."

And adds a pragmatic note:

> "But the only reason why I ask is just to help inform the context whenever we do it to save us some time. But if it doesn't exist, it's no problem. We still do the same exploration. Because documentation doesn't always tell the truth."

---

## 9. Streaming / Real-Time Question

Colin asks about whether the EMS migration introduced new technical patterns:

> Colin: "From the screens, are they, especially from the new version, are they doing different things? Like, for instance, with new, maybe students in streaming or real-time integrations, were those types of changes moved to, or did that already exist in the old?"

The question is about whether EMS introduced fundamentally new UI interaction patterns (streaming data, real-time updates, WebSocket connections, etc.) that would need to be replicated when porting legacy screens.

Guhan's response redirects:

> "Oh, no, it was not just UI focused. There was also reorganization into microservices, and even UI had a new makeover."

He then clarifies what changed:

> "For the things that we've already done, it needs to blend in with the current products. Those kind of things were done, yes. It's not a different ship as is for the most part."

### 9.1 Interpretation

Guhan does not directly address streaming or real-time patterns. His answer focuses on:
- The reorganization from monolith to microservices (backend change)
- UI makeover (visual/UX change)
- The ported screens were adapted to "blend in" with EMS's product design

The streaming/real-time question goes unanswered, which may mean:
- It's not a significant concern (no major streaming patterns were introduced)
- Guhan didn't fully parse the question (speech-to-text meeting, cross-talk likely)
- It's something to follow up on during technical deep-dives with the engineering team

---

## 10. Reports as Concrete Missing Functionality

Selva provides the only concrete example of missing functionality in the entire meeting:

> "For example, I have some missing reports that I've not brought in from the old thing, right? So we can look at how it looks in the old one and bring, for now, keep the same user experience and bring it to the new."

### 10.1 Significance

- Reports are a tangible, scoped feature category
- Selva says "I have some missing reports" - using first person, suggesting this is directly within his area of responsibility
- The approach Selva describes is exactly the POC model: look at the old, keep the same UX, bring it to the new
- Reports may be a strong candidate for the POC because:
  - They are often relatively self-contained (data query + rendering)
  - They have clear visual output (easy to verify conversion fidelity)
  - They represent real missing functionality customers are asking for

### 10.2 End-to-End Requirement

Selva emphasizes this is not surface-level:

> "And it's not a UI alone. There is a, I mean, along with it comes the backend logic only then... it needs to have a fully functional thing."

And:

> "Make it work end-to-end, right? So that will be the goal for this exercise."

---

## 11. Scale and Estimation Goal

Guhan frames the expected outcome in terms of estimation:

> "There are like 70, 80, 100 pages we do not expecting everything to be converted. We get a better idea of what it means to do that."

And then the estimation model:

> "In case of like, for example, we are able to do 10 with this AI... We are able to do that in 10 screens, we can do it in let's say 10 days, we can do 17, 17 days, some sort of estimation we can do based on this, right? With this, we can go back to the customer and promise that, okay, we will do, we will deliver this in this time."

### 11.1 What This Reveals

- **Total screen count:** 70-100 screens in EPNM that need conversion (approximate)
- **POC is not about converting everything** - it's about proving the method and establishing a conversion velocity
- **The deliverable is dual:** working converted screens AND a per-screen time estimate
- **Customer-facing commitments** depend on this estimation - this is not academic, it drives delivery promises
- The AI-assisted approach is explicitly tied to the value proposition: can AI make this conversion fast enough to be viable?

---

## 12. Team Availability Constraint

Guhan sets clear expectations about internal team availability:

> "At the moment the team is also on critical or a platform, if you think so, the team itself will not be able to [invest] time here. But of course, they need to give you the context and everything. They will provide you with that."

And:

> "If you can take that independently and come back with your analysis and put that up with what you've come up with, that would be good. We'll have periodic checkpoints to help clarify anything more."

### 12.1 Operating Model

- Cisco team provides context and access, then steps back
- BayOne (Colin) works independently on analysis and conversion
- Periodic checkpoints for clarification, not ongoing collaboration
- The team is on "critical" work (likely the EPNM platform itself or other priorities)

This reinforces why documentation absence is such a significant challenge - the people who know the code are too busy to provide sustained guidance.

---

## 13. Domain Gap Concern

Guhan raises an important concern about domain knowledge:

> "How do you try to reach the [capability] for the domain level thing, right? So because, obviously, these projects are in various domains that you've taken up, right? And this one is in element management. And how do we ensure that there's no [gap] in what we bring over, right?"

And more pointedly:

> "This may not have the readily available [tests] for you to go rerun them on the new one? How do you make sure that there's no domain gap or no functionality gap?"

### 13.1 What This Reveals

- Guhan is concerned about domain-specific correctness, not just visual fidelity
- Element management has domain-specific logic that could be subtly wrong if not understood
- Existing test coverage may be insufficient - "this may not have the readily available [tests]"
- The concern is about functional completeness, not just UI appearance

---

## 14. Conversion Challenge Summary

Synthesizing all technical details from the meeting, the conversion challenge has these dimensions:

1. **Architecture gap:** Monolith (EPNM) to microservices (EMS) - fundamentally different runtime models
2. **Frontend framework gap:** Dojo/JavaScript to Angular - different component models, data binding, routing, state management
3. **Vertical scope:** Each screen requires full-stack conversion, not just frontend work
4. **Code surgery:** The original codebase was modified during EMS development, so EPNM code cannot be used as-is even as reference
5. **Missing documentation:** Code comprehension must be done through exploration, identified as "the bulk of the challenge"
6. **Domain complexity:** Element management domain has specialized logic that must be preserved precisely
7. **UX constraint:** Converted screens must reproduce the legacy EPNM experience, not adopt the new EMS UX
8. **Scale:** 70-100 screens total, with an unknown subset prioritized for conversion
9. **Test gap:** Existing automated tests may not cover the functionality being ported
10. **Team bandwidth:** Internal engineering team cannot dedicate significant time to support the effort
