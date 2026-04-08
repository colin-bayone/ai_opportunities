# 01 - Meeting: Business Drivers and Strategic Context

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Focused deep dive on business drivers and strategic context

---

## 1. Why This Engagement Matters Now

### 1.1 Customer Demand for Legacy UI Parity

The immediate business driver is that major customers are rejecting the modernized product's UI and demanding exact replicas of the legacy (EPNM) interface. Guhan framed this directly:

> "We rebuilt it. Different experience for customers, but some customers are major customers are coming back and say no, we want exactly the same ones. Because their higher their systems are integrated with it. Whatever their operators are used to, they don't want to change it."

Two distinct customer objections are embedded here:

1. **System integration dependency.** Customer systems (likely OSS/BSS stacks, NOC dashboards, or automation tooling) are integrated with the legacy UI. Changing the UI breaks those integrations. This is not a preference issue; it is an operational dependency.
2. **Operator familiarity.** Network operators who use these tools daily are trained on the legacy interface. Retraining costs and workflow disruption are unacceptable to these customers.

The scale of the problem is approximately **200 UI screens** that need conversion from the legacy product to the modernized one:

> "So we are trying to like almost like 200 screen pages of UI."

### 1.2 The Staffing Model Is Broken

Guhan explicitly stated that the traditional approach of throwing bodies at the problem is no longer viable:

> "I think the usual way of delivering through, putting 10 people to it, that's kind of going away. So you want to experiment something new."

This is a significant admission. It signals that:
- The old staffing model (assign 10 engineers to manually rebuild screens) is recognized as unsustainable.
- Leadership is actively seeking an AI-accelerated alternative.
- This is framed as an "experiment" -- Guhan is open to new approaches but wants to see proof before committing.

### 1.3 Timeline Pressure

Guhan identified a critical timeline constraint. The conventional timeline (one year) is unacceptable:

> "Obviously the bill is about let's do it in one year. That's going to be too late."

At the same time, he acknowledged the risk of overinvesting in the wrong direction:

> "Other thing is we also don't want to go in the trout off. It's not scalable at this point with the way our objects and stuffs are going."

The "trout off" (likely "trough" -- as in a trough of diminishing returns, or possibly "trade-off") suggests he has considered and rejected a brute-force rebuild because the architecture itself is evolving. Investing heavily in converting screens for the current-generation product may be wasted if the underlying object model changes.

---

## 2. The Multi-Generational Modernization Challenge

### 2.1 Guhan's Framing of Serial Modernization

Guhan described Cisco's network management products as going through multiple generational leaps:

> "We have been modernizing the Cisco multiple gens, right? We are moving from gen A to gen E to... next one, right? And then when we do that, obviously there's always a demand for not rebuilding everything."

This is a critical piece of context. The EPNM-to-EMS transition is not a one-time migration. It is the latest in a series of generational product transitions ("gen A to gen E"), and each transition carries the same fundamental tension: customers want continuity while the engineering organization needs to evolve.

### 2.2 The Scale That Makes Rebuilding Impractical

Guhan quantified the total codebase size that makes wholesale rebuilding untenable:

> "We have easily 45-50 million lines of code, which are across like six or eight products, and we can't go and rebuild. And they've been... it's the fact that we can step in the direction with no return of investment for sure, right? That's not where we want to go."

Key data points:
- **45-50 million lines of code** across **6-8 products**
- Rebuilding from scratch is explicitly ruled out as having no ROI
- This code has accumulated across multiple product generations

### 2.3 The AI Inflection Point

Guhan connected the modernization challenge to the broader AI transformation happening across Cisco:

> "And again, it comes down to the evolving means. As we see more in the next four years, it will also be AI, which we are playing. You know, GTO has been very vocal everywhere. That's real. And that's what customers are telling us also."

"GTO" refers to Cisco's CTO (likely referring to the broader executive messaging around AI). Guhan is saying:
- Cisco's CTO has been publicly committed to AI transformation.
- Customers are echoing this -- they are also telling Cisco they expect AI capabilities.
- The next four years will see significant AI integration into these products.

This creates a directional tension: the immediate need is UI parity (looking backward), but the strategic direction is AI-native capabilities (looking forward).

### 2.4 Modernization Must Enable Agents, Not Just Humans

Guhan made a forward-looking statement that reframes the modernization objective:

> "So we have to use the best of what we have, but to your point, modernize it in a way that agents can work with rather than just the humans can, right?"

This is strategically significant. He is not asking for a simple UI port. He is asking for modernization that:
1. Preserves what exists ("best of what we have")
2. Makes the system accessible to AI agents, not just human operators
3. Prepares the product for an agentic future

---

## 3. Customer Relationship Dynamics

### 3.1 Education vs. Accommodation

Guhan articulated a nuanced position on how to handle customer demands for legacy UI parity. He does not simply want to give customers what they ask for:

> "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them. Make them move in that direction. It's easy, easy workflow is to stick to what they're used to. But I think it's maybe they have to be disturbed a bit. They have to be a little bit shaken so that they are ready for pretty dirty."

"Ready for pretty dirty" is likely a transcription error for something like "ready for the future" or "ready for productivity" -- the intent is clear: customers need to be moved forward, not simply accommodated.

He then made the business case for this approach:

> "That's because they are not even moving to 2025, they can't move to 2030, which we are having the conversation. So we have to make some choices around what are... if you have the immediate need, and again, we have to look at what does it take to do it."

The logic chain:
1. Some customers have not even adopted the current (2025-era) product.
2. They cannot leap to a 2030-era product without intermediate steps.
3. Simply building what they want (legacy UI clone) may be wasted effort if it takes too long.
4. The time horizon of the conversion determines whether it is worth doing at all.

### 3.2 The Time-Value Calculation

Guhan laid out an explicit decision framework around the conversion timeline:

> "Let's say if it's six months and we go, we're able to convert all this, then it's not worth that, that kind of, that the dialogue can happen. In fact, it's going to take two, three years. Then by the time you're done, this could be probably already old or kind of redundant, so you need to go."

This is the core business calculus:
- **If conversion takes ~6 months:** Worth doing. Customers get what they need quickly, and the investment pays off during the product's remaining lifecycle.
- **If conversion takes 2-3 years:** Not worth doing. By completion, the product generation will be obsolete and the effort is wasted.
- **The AI-accelerated approach is attractive precisely because it might compress the timeline into the "worth doing" window.**

### 3.3 MOUs with Major Customers

Guhan mentioned formal agreements with key customers:

> "So we have some MOUs with few of them to ensure that, and they are also talking to each other more than before, so they can leverage the best practices and things."

This indicates:
- Memoranda of Understanding exist with specific major customers around the modernization transition.
- Customers are coordinating with each other (sharing best practices).
- There is formal structure around managing customer expectations during the transition.

### 3.4 Customer-First Culture vs. Strategic Discipline

Guhan identified a tension between Cisco's customer-first culture and the need for strategic discipline:

> "And aligned with PLM too, because there's always usual stuff. Often some big customers when they want, we don't think twice. We just want to go. You are a customer-first company. You want to go take care of it. Maybe try to step back and look at, is this right?"

"PLM" likely refers to Product Lifecycle Management or the product management organization. The tension:
- Cisco's instinct is to immediately fulfill major customer requests.
- Guhan wants to pause and evaluate whether fulfilling those requests is strategically correct.
- He is seeking external support (from BayOne) to provide that strategic counterweight.

---

## 4. Product Management Tensions and Prioritization

### 4.1 "Everything Is Priority"

Guhan described a dysfunctional prioritization dynamic with product management:

> "The product has prioritized, which is important. Because everything at this point seems to be priority, which I've just come out of the meeting. We've got to have everything as a priority. We've got to have 10 priorities and run behind everything, all the 10."

This is a direct and candid admission of organizational dysfunction:
- Product management treats everything as equally important.
- Engineering is expected to pursue all 10 priorities simultaneously.
- Guhan has just come from a meeting where this dynamic played out.
- He recognizes this is unsustainable.

### 4.2 Forcing Prioritization Decisions

Guhan stated his intent to force product management into real prioritization:

> "So we have to somewhere to make some tough calls. We have to make a team with the product management. We will enforce some decisions to them that they have to prioritize to be proper."

He sees this as a prerequisite for the BayOne engagement:

> "So based on that, we'll know which is more important than that. And that's when we can have the solid, honest, true discussion about it."

The implication: Guhan cannot commit to a specific scope for BayOne until product management has made real prioritization decisions. The engagement scope depends on which of the multiple possible work streams is selected.

### 4.3 Two or Three Items in the Pipeline

Guhan mentioned that beyond the UI conversion work, there are additional candidate projects:

> "But there are, as I said, there are two or three in the lab."

And earlier:

> "There is something we have other areas anyway to look at if at all we get some additional."

The UI conversion (200 screens) is the most clearly defined, but there are 2-3 other potential work streams that could also benefit from BayOne's approach. These are not yet clearly scoped or prioritized.

---

## 5. Consolidating Parallel AI Efforts

### 5.1 The Consolidation Problem

Guhan described multiple teams independently experimenting with AI:

> "The teams are also trying multiple things, so we're trying to see consolidate into few things. Everyone trying... that's the area."

This mirrors a common pattern in large engineering organizations: decentralized AI experimentation leading to fragmentation.

### 5.2 The Engineer Morale Risk

Guhan articulated a specific concern about what happens when parallel efforts are eventually consolidated:

> "It's not there in the heated or demand stage, but I can envision given experience, six months down line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be. So I would rather tell them now."

This is a sophisticated management concern:
- Multiple teams are currently experimenting with different AI tools and approaches.
- Eventually, the organization will standardize on a subset of these.
- Teams whose chosen tools/approaches are not selected will feel their work was wasted.
- Even if the technical rationale for choosing one approach over another is sound, the human cost of disappointment remains.
- Guhan wants to make consolidation decisions early ("tell them now") rather than let teams invest further in approaches that will ultimately be abandoned.

### 5.3 Building Visibility Through Process

Guhan described his efforts to create organizational visibility:

> "So that's why I'm trying to build a catalog of things that are happening and have structured way through Jira and other. Give visibility to what is happening because if they don't bring visibility then we can't help it. So trying to bring that kind of certain process."

He then acknowledged the difficulty:

> "We have been trying to get some order to some method to madness, right? So that's a separate one, adding that more... which of course is a management leadership thing that we are working on."

This reveals:
- The catalog/visibility effort is ongoing but incomplete.
- It is a Jira-based approach to tracking what teams are doing.
- Guhan frames it explicitly as a management and leadership challenge, separate from the technical work.
- He distinguishes this organizational work from the technical assistance he wants from BayOne.

### 5.4 Colin's Resonance with the Consolidation Challenge

Colin validated this concern by sharing his experience at Coherent:

> "There were a lot of really amazing siloed teams, and they were all kind of going in a similar direction. But no one was talking. And then what ends up happening is you build this massive mountain of technical debt, and you can't do anything about it. And you end up having these really heated, at times, engineering discussions that are like, this platform versus this one, or this framework versus that. And it's not the right conversation. It's a conversation that should have happened a year prior before anyone started their work."

This exchange established a shared understanding between Colin and Guhan about the organizational risk of uncoordinated AI experimentation.

---

## 6. What Guhan Wants from BayOne

### 6.1 Strategic Guidance, Not Just Implementation

Guhan explicitly asked for more than just execution:

> "Given your title and your experience, I think it's not just about implementing. What is the right direction? What is the right way to go about it? I think those kind of things will also really help. Strategic. Strategic. Right."

He repeated the word "strategic" for emphasis. He wants:
- Directional advice on the right approach to modernization.
- Assessment of whether specific investments are worthwhile.
- External perspective to challenge internal assumptions.

### 6.2 Alignment with Product Management

Guhan wants any BayOne engagement to be aligned with PLM (product lifecycle management / product management):

> "And aligned with PLM too, because there's always usual stuff."

This means whatever BayOne recommends needs to be defensible in the context of product management priorities, not just engineering preferences.

### 6.3 Practical Alongside Strategic

While wanting strategic input, Guhan also grounded the conversation:

> "At the same time, something practical. Yes, I don't want to shoot ourselves by overcommitting something."

He wants actionable work, not just consulting advice. The engagement needs to produce tangible results within the prioritized scope.

---

## 7. The Two Defined Work Streams

### 7.1 UI Conversion (Varel's Team)

The primary work stream discussed in this meeting:
- **Owner:** Varel (team lead under Guhan)
- **Scope:** Converting approximately 200 UI screens from legacy (EPNM) to modern (EMS) product
- **Driver:** Major customer demands for UI parity
- **Constraint:** Cannot take a year; must be accelerated through AI
- **Status:** Identified as a need but not yet formally scoped for BayOne

### 7.2 Agentic AI Platform (Meryl's Team)

A separate, parallel effort:
- **Owner:** Meryl
- **Scope:** Building an agentic AI platform
- **Status:** "Staffed and we are continuing to review what is needed"
- **Guhan's assessment:** "I checked with her on what she needs something there at this point" -- implying Meryl may not currently need external help
- **Location:** Meryl is based in New York, was available that week but traveling the following weekend

Colin noted that Meryl had expressed interest in what BayOne was doing with CI/CD, calling it "somewhat relevant" to her work.

### 7.3 The Azure HD Platform

Guhan briefly mentioned a third platform:

> "We have an Azure HD platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that."

This appears to be a separate product/platform that has reached General Availability. Guhan described it as:
- Currently staffed
- In the GA phase
- Capable of absorbing more people ("each can take more and more people always") but being managed within the existing team
- Not the primary focus for BayOne involvement

---

## 8. Open Questions and Unresolved Points

1. **Which of the 2-3 pipeline items will be prioritized?** Guhan explicitly deferred this to product management decisions that had not yet been made.

2. **What does "200 screens" actually mean in technical terms?** Are these full application views, dialog boxes, configuration panels, reports? The scope could vary enormously depending on screen complexity.

3. **What are the MOUs with major customers?** How binding are these commitments? Do they specify timelines or UI parity requirements?

4. **Who are the "major customers" demanding legacy UI?** Their identity and market importance would shape prioritization.

5. **What is the relationship between the UI conversion work and the agentic platform?** Could the agentic platform eventually make the legacy UI conversion moot if customers move to agent-driven interactions?

6. **What AI tools are the various teams currently experimenting with?** Guhan mentioned wanting to "consolidate into few things" but did not specify what is currently in play.

7. **What is the actual product management prioritization timeline?** Guhan said he would "enforce some decisions" but did not specify when.

8. **What does the four-year AI vision look like internally?** Guhan referenced "as we see more in the next four years, it will also be AI" -- is there an internal roadmap?

9. **How does Meryl's agentic platform relate to the UI conversion need?** If the platform is building agent capabilities, does that change the calculus on screen-by-screen UI parity?

10. **What is the nature of the "experiment" Guhan wants?** He framed BayOne's involvement as wanting to "experiment something new." How does success get measured? What would cause Cisco to scale up or abandon the approach?
