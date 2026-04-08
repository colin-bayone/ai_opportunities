# 01 - Meeting: Technical Landscape

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Focused deep dive on technical landscape

---

## Overview

This document captures every technical detail from the February 9, 2026 meeting between Guhan Selva (Cisco) and Colin Moore (BayOne). The meeting was exploratory and in-person. The technical landscape was discussed at a high level by Guhan to frame the problem, with specifics deferred to a follow-up session later that day with a technical team lead (likely Varel). As a result, some areas have incomplete detail that will need to be filled in from subsequent meetings.

---

## The Core Problem: UI Conversion at Scale

Guhan framed the central technical challenge as a UI conversion effort. Cisco rebuilt a product with a "different experience for customers," but major customers are pushing back, demanding the previous UI exactly as it was. Guhan's words:

> "We rebuilt it. Different experience for customers, but some customers are major customers are coming back and say no, we want exactly the same ones. Because their higher their systems are integrated with it. Their operators are used to, they don't want to change it."

This is not an aesthetic preference. The customers' downstream systems are integrated with the legacy UI. Their operational workflows depend on it. They are not requesting the new UI be styled differently; they are requesting functional equivalence with the prior product's interface.

### Scale of the UI Conversion

Guhan stated the scope is approximately **200 UI screens** (referred to as "200 sheen pages of UI" in the transcript, where "sheen" is a speech-to-text error for "screen"):

> "So we are trying to like almost like 200 sheen pages of UI."

### Timeline Pressure

Guhan stated that the traditional approach -- assigning a team to build it over a year -- is too slow:

> "Obviously the bill is about let's do it in one year. That's going to be too late."

He also stated that the traditional staffing model ("putting 10 people to it") is "kind of going away," and that he wants to "experiment something new."

### The Rebuild Is Not an Option

Guhan explicitly rejected the option of rebuilding the entire codebase as impractical:

> "We have easily 45-50 million lines of course [code], which are across like six or eight parts [products], and we can't go and rebuild... it's the fact that we can step in the direction with no return of investment for sure, right? That's not where we want to go."

This establishes two critical constraints:
1. The total codebase across the product portfolio is **45-50 million lines of code**.
2. That code spans **6-8 distinct products**.
3. A full rewrite is explicitly off the table due to the absence of return on investment.

---

## Product Architecture: EPNM vs. EMS

The transcript does not use the terms "EPNM" or "EMS" explicitly (these appear in the topic map and prior context, not in the transcript itself). However, Guhan describes the architecture in terms of a **previous product** (legacy) and a **rebuilt product** (current/new), and the relationship between them is clear from context.

### The Previous Product (EPNM)

- The legacy product had a UI that customers are deeply integrated with.
- Customers' systems are integrated with it; operators are trained on it.
- The UI technology is legacy (Dojo/JavaScript, per the topic map; not explicitly named in this meeting's transcript).
- The product is part of a larger portfolio of network management products spanning 45-50 million lines of code.

### The New Product (EMS)

- Has been rebuilt with a "different experience for customers."
- Is a "traditional network management product, but modernized product."
- Guhan specifically described it as "not an agentic product."
- Has an **Azure HD platform** that is in the **GA (General Availability) phase**.
- Is currently staffed and being worked through a list of remaining items.

Guhan's description of the Azure HD platform:

> "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that. But that's, I think that's more like at this point staffed and we are continuing to review what is needed."

### The Gap Between Products

The core problem is that the new product (EMS) is missing capabilities that existed in the previous product (EPNM), particularly on the UI side. Guhan stated:

> "It is about, it's not an agentic product, it's a traditional network management product, but modernized product. With capabilities that were previously in the previous version is missing, the previous generation is missing, especially on the UI."

This confirms:
1. The new product is functionally incomplete relative to the legacy product.
2. The missing capabilities are concentrated in the UI layer.
3. The backend modernization is further along than the frontend.

---

## Code Base Scale and Complexity

### Quantitative Details

| Metric | Value | Source |
|--------|-------|--------|
| Total lines of code | 45-50 million | Guhan, stated directly |
| Number of products | 6-8 | Guhan, stated directly |
| UI screens needing conversion | ~200 | Guhan, stated directly |
| Target timeline for UI conversion | Less than 1 year (1 year is "too late") | Guhan, stated directly |
| Traditional staffing approach | "10 people" | Guhan, stated directly |

### Generational Modernization History

Guhan referenced that Cisco has been through multiple modernization generations:

> "We have been modernizing the Cisco multiple gens, right? We are moving from gen A to gen E to know. Next one, right?"

This is significant: the current effort is not the first modernization. The organization has been through this cycle multiple times, moving through product generations (A, B, C, etc.). Each generational shift brings the same demand: do not rebuild everything. This is a recurring organizational pattern, not a one-time event.

### The "Treadmill" Concern

Guhan raised a specific concern about the legacy technology not being a wise investment:

> "Other thing is we also don't want to go in the trout off [treadmill]. It's not scalable at this point with the way our objects and stuffs are going. I think I don't think there's something that that's a wise investment to go."

This suggests the legacy architecture has scalability issues with its data model ("objects"), and investing in extending the old platform further is not considered wise.

---

## Technology Stack

The transcript from this meeting does not explicitly name the specific technologies in the stack (Java, Dojo, Angular). Those details appear in the topic map, likely informed by context from other meetings or prior knowledge. What the transcript does establish:

### Frontend
- The legacy product has a UI built on an older technology stack.
- The new product has a UI built on a different, modern stack.
- Customers want the **legacy UI experience** replicated in the new product.
- There are approximately 200 screens that need to be converted.

### Backend
- Both products are network management systems.
- The new product is described as "modernized."
- The backend is apparently more mature than the frontend in the new product (Guhan's emphasis was entirely on UI gaps).

### AI Layer
- The new product is explicitly **not** an agentic product.
- AI is being considered as a means of accelerating development (code generation), not as a customer-facing feature.
- Guhan specifically stated: "So customers won't see the, maybe it's like AI generated code. So they won't see AI or anything in the frontend or even in the backend."

This is an important distinction: AI is being positioned as a **development accelerator**, not a product feature. The output would be conventional code; the customer would never know AI was involved.

---

## Parallel Efforts and Organizational Landscape

### Three Distinct Technical Efforts

Guhan described at least three parallel streams of work:

1. **UI Conversion (~200 screens)** -- The primary opportunity discussed in this meeting. Converting legacy UI screens to the new product. Guhan's highest-priority item.

2. **Agentic AI Platform (under Meryl)** -- A separate effort led by Meryl to build an agentic AI platform. Guhan checked with Meryl on whether she needed additional help and indicated she did not at that point:
   > "The agency platform is being built by Meryl. And I checked with her on what she needs something there at this point."

3. **Azure HD Platform (GA phase)** -- The infrastructure platform for the new product. Already staffed and in general availability. This effort is considered relatively stable ("at this point staffed and we are continuing to review what is needed. Each can take more and more people always, but we are working through the list of things to do there.").

### Team Ownership

- **Varel's team** -- Owns the UI conversion work. Guhan confirmed: "The one he said was the one that referred to the UI."
- **Meryl's team** -- Owns the agentic AI platform. Based in New York. Meryl was traveling the following week.
- **Azure HD team** -- Not explicitly attributed to a named leader in this meeting.

### Consolidation Challenge

Guhan identified a significant organizational challenge: multiple teams are independently pursuing AI-related initiatives, and those efforts need to be consolidated before they create technical debt and engineer disappointment.

> "The teams are also trying multiple things so we're trying to see consolidate into few things."

He elaborated on the human dimension of this problem:

> "It's not there in the heated or demand stage, but I can envision given experience, six months down line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be. So I would rather tell them now."

This reveals:
1. Multiple teams are experimenting with AI approaches independently.
2. Guhan anticipates that some of these efforts will need to be deprecated.
3. He prefers to make those decisions now rather than let teams invest further.
4. He is actively building a catalog of efforts and introducing structure via Jira: "I'm trying to build a catalog of things that are happening and have structured way through Jira."

### Visibility Problem

Guhan noted that a prerequisite for consolidation is visibility into what teams are doing:

> "Give visibility to what is happening because if they don't bring visibility then we can't help it."

This suggests the organization does not yet have a comprehensive inventory of all AI experiments and initiatives underway.

---

## Colin's Technical Context (BayOne Experience)

Colin provided technical context from his prior experience at Coherent that is directly relevant to the Cisco engagement:

### Code Modernization Experience

- **C# to Rust migration** -- Colin described this as "somehow worse than moving from Spring to Go," establishing that BayOne has handled extreme technology migrations.
- **Spring to Go** -- Referenced as a current Cisco CI/CD engagement: "This was a team that wanted to shift their stack entirely to something new, switch from Spring to actually they wanted to go to Go, which is a very big shift."
- **Thick client to web-based interface** -- Colin specifically called out experience with this migration pattern, which is relevant to UI modernization.

### Why Vanilla Code Modernization Fails at Scale

Colin articulated a specific technical argument about why naive AI-assisted code conversion does not work for large codebases:

> "You can go the vanilla way to do code-based modernization. And that's where usually people start, and it sounds really good whenever you start. It doesn't work at all as soon as you get above a certain size of code base."

He described the failure mode:

> "What ends up happening is you have developers saying, oh, ChatGPT can do this for me. I can copy and paste code. I can put in a file, get out a file, and it converts. The problem is that that's not how systems work. If you look at them as individual files, then what happens is, yes, you've done your job of converting, but now it can't talk to anything else. There's no meshing between the two."

And the nuance problem:

> "The other issue is the nuance between languages or even frameworks. What exists in one might not even have a concept in the other."

This was the beginning of Colin's methodology presentation, which was interrupted when Guhan stopped him and asked to schedule a deeper session:

> "Can we set up? Do you have some time in the afternoon?"

Guhan interrupted specifically at the mention of **knowledge graphs**:

> "I'm sorry to interrupt you, but this seems definitely interesting. I want to understand, are you going to add a knowledge graph? Yes. And all those things, right? Yes."

This is a signal that the knowledge graph approach resonated with Guhan's understanding of the problem.

---

## The Customer Dimension of the Technical Problem

### Why Customers Want the Old UI

Guhan provided two specific reasons customers demand the legacy UI:
1. **System integration:** "Their higher their systems are integrated with it." Customer systems have programmatic integrations with the legacy UI.
2. **Operator training:** "Their operators are used to, they don't want to change it." Operators are trained on the existing workflows and do not want retraining.

### The Strategic Tension

Guhan expressed a nuanced view on whether to simply give customers what they ask for:

> "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them."

And more pointedly:

> "Maybe they have to be disturbed a bit. They have to be a little bit shaken so that they are ready for pretty dirty [the future]. That's because they are not even moving to 2025, they can't move to 2030, which we are having the conversation."

This means some customers have not even upgraded to the current version. They are still on older versions, asking for the old UI to be brought to the new product. If they have not moved to 2025-era technology, they cannot skip to 2030-era technology. So there is a strategic question about whether to invest in recreating the old experience or pushing customers forward.

### ROI Calculus for UI Conversion

Guhan framed a specific decision framework around the conversion effort:

> "If it's six months and we go, we're able to convert all this, then it's not worth that, that kind of, that the dialogue can happen. In fact, it's going to take two, three years. Then by the time you're done, this could be probably already old or kind of redundant, so you need to go."

Translation: If the conversion can be done quickly (six months), it is worth doing because it satisfies customers without too much investment. If it takes two to three years, the effort is wasted because the technology will have moved on by the time it is complete. This creates a narrow window: the conversion must be achievable in significantly less than one year.

---

## AI as Development Accelerator (Not Product Feature)

A critical technical distinction emerged in this meeting. There are two completely separate uses of AI under discussion:

### AI Use #1: Accelerating UI Conversion (Development Tool)

This is the BayOne opportunity. Using AI to convert legacy UI screens to the new product faster than a traditional development team could. The AI output is conventional code. Customers do not see or interact with AI.

Guhan stated explicitly:

> "So how do we ensure we have that capability? So using AI, how do we deliver it? So customers won't see the, maybe it's like AI generated code. So they won't see AI or anything in the frontend or even in the backend. So that is one."

### AI Use #2: Agentic AI Platform (Product Feature)

This is Meryl's effort. A separate initiative to build an AI-powered product capability. This is distinct from the UI conversion work and has its own team and roadmap.

### AI Use #3: Teams Experimenting Independently

Multiple engineering teams are trying various AI approaches on their own. These are the efforts Guhan wants to consolidate.

---

## Cisco's Broader Technology Strategy

### GTO Direction

Guhan referenced Cisco's CTO (likely Chuck Robbins or a division CTO, referred to as "GTO" in the transcript, likely CTO):

> "GTO has been very vocal everywhere. That's real. And that's what customers are telling us also."

This suggests Cisco's technology leadership has been publicly advocating for AI adoption, and customers are echoing that direction.

### Agent-Ready Architecture

Guhan articulated a forward-looking architectural requirement:

> "We have to use the best of what we have, but to your point modernize it in a way that agents can work with rather than just the humans can, right?"

This is a significant statement. The modernization should produce code and architecture that AI agents can interact with, not just human developers. This goes beyond traditional modernization (making code maintainable by humans) to a new requirement (making code operable by AI agents).

### Customer Co-Development

Guhan mentioned MOUs (Memorandums of Understanding) with customers:

> "We have some MOUs with few of them to ensure that, and they are also talking to each other more than before, so they can leverage the best practices."

This indicates a collaborative approach to product evolution, not a purely internal effort.

---

## Open Questions and Gaps

### Technical Details Not Yet Available (from this meeting)

1. **Specific technology stack of the legacy product** -- Java backend, Dojo frontend is referenced in the topic map but not explicitly stated in this transcript. Needs confirmation from subsequent meetings.
2. **Specific technology stack of the new product** -- Angular frontend is referenced in the topic map but not explicitly stated. Needs confirmation.
3. **Architecture of the new product** -- Microservices architecture is referenced in the topic map but not explicitly stated in this transcript. Needs confirmation.
4. **Which of the 6-8 products is the focus** -- Guhan did not specify which product line this UI conversion applies to.
5. **Azure HD platform details** -- What "HD" stands for, what the platform's architecture looks like, what its relationship is to the UI conversion work.
6. **The 200 screens** -- No breakdown of complexity, categories, or priority among the 200 screens was provided in this meeting.
7. **Varel's team structure** -- Size, current capacity, technology expertise.
8. **What teams are experimenting with AI** -- Guhan mentioned multiple teams trying things but did not enumerate them.
9. **Meryl's agentic AI platform details** -- Architecture, technology choices, integration points with the network management product.

### Strategic Ambiguities

1. **Convert or leapfrog?** -- Guhan expressed two somewhat contradictory impulses: (a) convert the legacy UI to satisfy customers, and (b) "disturb" customers to push them forward. The resolution of this tension will determine the scope and nature of the work.
2. **Consolidation timing** -- Guhan said he wants to consolidate parallel AI efforts now, but also said priorities have not been decided yet ("We've got to have 10 priorities and run behind everything, all the 10"). How does BayOne's engagement interact with the broader consolidation?
3. **How does the CI/CD engagement relate?** -- Colin mentioned an existing Cisco CI/CD engagement. The relationship between that work and this EPNM/EMS effort is unclear. They are under the same corporate umbrella but appear to be separate product lines.

---

## Summary of Technical Landscape (as understood from this meeting)

Cisco has a portfolio of network management products spanning 45-50 million lines of code across 6-8 products. They have rebuilt a legacy product (EPNM) into a modernized product (EMS), but the new product is missing UI capabilities that major customers require. There are approximately 200 UI screens that need to be converted from the legacy product to the new one. The traditional approach (staffing a team, building for a year) is too slow, and Guhan wants to explore AI-accelerated conversion.

Three parallel technical efforts exist: (1) the UI conversion (Varel's team, the primary BayOne opportunity), (2) an agentic AI platform (Meryl's team, currently self-sufficient), and (3) the Azure HD platform (in GA, currently staffed). Additionally, multiple unnamed teams are independently experimenting with AI, creating a consolidation challenge that Guhan is actively trying to address.

The AI in this engagement would be a development tool, not a product feature. The output would be conventional code that customers never know was AI-generated. The strategic question is whether to faithfully replicate the legacy UI or push customers toward a modernized experience, with the answer depending on how quickly the conversion can be achieved.
