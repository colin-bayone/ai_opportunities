# 05 - Meeting: Cross-Engagement Insights

**Source:** /cisco/cicd/source/meeting_guhan_selva_2026-02-09.txt
**Source Date:** 2026-02-09 (Cisco campus meeting, primarily EPNM-focused)
**Document Set:** 05 (Guhan/Selva meeting -- light treatment for CICD)
**Pass:** Cisco culture, Colin positioning, and cross-engagement context relevant to CICD

---

## Cisco Culture: Consolidation Pressure and Competing Initiatives

Guhan describes an organizational challenge that is identical in nature to the problems the CICD engagement is meant to address at a smaller scale.

### The "Method to Madness" Problem

Guhan's teams are running multiple parallel AI and modernization experiments with no central coordination:

> "The teams are also trying multiple things so we're trying to see, consolidate into few things. Everyone trying... that's that's the area."

He is explicitly trying to impose structure:

> "I'm trying to build a catalog of things that are happening and have a structured way through Jira and other -- give visibility to what is happening because if they don't bring visibility then we can't help it. So trying to bring that kind of certain process... we have been trying to get some order, some method to madness."

He anticipates the human cost of delayed consolidation:

> "It's not there in the heated or demand stage, but I can envision given experience, six months down the line, we are just in a state where there are going to be more disappointments because they tried something that we chose something else. Even if the technical reasons don't hold good at that point, we are going to really disappoint some engineers which we don't want to be. So I would rather tell them now."

**Why this matters for CICD:** This is the same pattern Colin identified at Coherent (see below) and that BayOne is encountering in the CICD engagement with Anand/Srinivas. The CICD work -- standardizing pipelines, enforcing GitHub practices, creating deployment discipline -- is fundamentally a "method to madness" intervention. If BayOne can frame CICD success as solving this consolidation problem at the team level, the value proposition scales naturally to Guhan's broader organization.

### Prioritization Paralysis

Guhan describes a dysfunction that pervades the decision-making layer:

> "Everything at this point seems to be priority... We've got to have 10 priorities and run behind everything, all the 10. So we have to somewhere to make some tough calls."

He explicitly wants product management to enforce real prioritization before committing external resources:

> "We have to make a team with the product management. We will enforce some decisions on them that they have to prioritize properly. So based on that, we'll know which is more important."

**Why this matters for CICD:** The CICD engagement faces the same risk. Set 01 listed six use cases (A through F), of which only A, E, and F were named. The "everything is priority" dynamic that Guhan describes at the org level is the same dynamic that could diffuse the CICD engagement's focus if BayOne does not insist on sequenced delivery. Guhan's explicit desire to "enforce decisions" on product management validates Colin's approach of discovery-first, structured scope.

### Customer Resistance to Change

Guhan describes a tension between modernization and customer expectations that applies broadly across Cisco's product lines:

> "Some customers are major customers coming back and saying no, we want exactly the same ones. Because their higher -- their systems are integrated with it. Whatever their operators are used to, they don't want to change it."

He frames the solution as managed disruption:

> "Maybe we should look at one gently to the next one, rather than just trying to go to what they would like. We need to probably educate them about what's best for them... maybe they have to be disturbed a bit. They have to be a little bit shaken so that they are ready."

He also frames customer resistance as a timeline problem:

> "They are not even moving to 2025, they can't move to 2030, which we are having the conversation. So we have to make some choices."

**Why this matters for CICD:** While CICD improvements are internal (not customer-facing), the same resistance-to-change dynamic exists with Cisco's engineering teams. Set 02 documented developers pasting code in WebEx instead of using GitHub. Guhan's language about "educating" and "gently" moving people from what they are used to is the same change management challenge the CICD engagement will face with Srinivas's team.

---

## Cisco Culture: The CTO's AI Mandate

Guhan references Cisco's CTO as driving an AI-first direction:

> "As we see more in the next four years, it will also be AI which we are playing. GTO [CTO] has been very vocal everywhere. That's real. And that's what customers are telling us also."

He frames this as a real organizational mandate, not aspirational:

> "We have to use the best of what we have, but to your point modernize it in a way that agents can work with rather than just the humans can."

**Why this matters for CICD:** The CTO's AI mandate creates top-down pressure that justifies AI-enhanced approaches to CI/CD. If the CTO is "very vocal" about AI, then framing CI/CD improvements as AI-enabled pipeline optimization (not just process automation) aligns with organizational messaging and makes the engagement easier to fund and champion internally.

---

## Cisco Culture: Build Speed as a Competitive Advantage

When Colin suggests starting with CI/CD-adjacent improvements even before EPNM work is formally scoped, he frames it as a universal benefit:

> "If you can build faster, even if your application isn't, let's say, AI facing or having AI features, if you can build faster, that definitely is a huge boost to everyone."

Guhan agrees with this framing. The implication is that build speed, deployment velocity, and pipeline efficiency are valued across Cisco's engineering org -- not just within the CICD engagement's specific team.

**Why this matters for CICD:** This validates the CICD engagement's value proposition at the organizational level. CI/CD improvements are not niche -- they are universally valued. If BayOne can demonstrate measurable build speed improvements for Anand/Srinivas, the case for expanding that work to Guhan's broader organization makes itself.

---

## Colin's Positioning: Consulting, Not Just Solutions

Colin delivers a positioning statement in this meeting that he will reuse across all Cisco engagements:

> "It's as much for me a solution as it is consulting in a way. Because our job can't just be to do solutions. Because if I do that, I'm not really being a good partner to you. I have to help you think about what comes next."

This is not the first time this positioning appears, but it is the first time it is delivered directly to a Cisco budget holder ($7M R&D). Guhan's response is immediate and positive -- he interrupts to schedule a deeper session. The positioning works.

**Why this matters for CICD:** This same consulting-not-just-delivery framing is what differentiates BayOne from the staff augmentation vendors (Zorian, Persistent) that Guhan already uses. For the CICD engagement, this means Colin should lead with strategic recommendations (what to build, what to skip, how to sequence), not just implementation plans. The consulting posture is what creates expansion opportunities -- implementation alone gets commoditized.

---

## Colin's Positioning: High Reliability and Determinism

Colin introduces himself with a specific technical identity:

> "My focus has always been high reliability systems. Determinism in AI, things that you can actually trust and are transparent, so engineers don't get this great solution built, and then completely reject it, because I'm not sure where any of the information or decisions are coming from."

**Why this matters for CICD:** This framing directly addresses a known risk in the CICD engagement. Set 02 documented Cisco engineers with non-standard workflows who would resist tooling changes. Colin's emphasis on "transparency" and "engineers don't reject it" is not just a personal brand statement -- it is a delivery philosophy that informs how CICD improvements should be introduced at Cisco. Changes must be explainable and trustworthy, not imposed.

---

## Colin's Positioning: The Coherent Parallel

Colin draws on his Coherent experience to validate the consolidation conversation with Guhan:

> "There were a lot of really amazing siloed teams, and they were all kind of going in a similar direction. But no one was talking. And then what ends up happening is you build this massive mountain of technical debt, and you can't do anything about it. And you end up having these really heated, at times, engineering discussions that are like, this platform versus this one, or this framework versus that. And it's not the right conversation. It's a conversation that should have happened a year prior before anyone started their work."

**Why this matters for CICD:** This is the exact narrative for the CICD engagement's long-term value. If BayOne can position CICD standardization as "the conversation that should have happened a year ago," the work becomes foundational rather than tactical. It also creates a role for Colin as the person who has seen this pattern before and knows how to resolve it -- which is exactly the consulting premium Guhan is willing to pay for.

---

## Colin's Positioning: CICD as Existing Credential

Colin mentions the CICD engagement unprompted during his self-introduction:

> "We had a couple of things at Cisco. One that we have right now that we're, I think, about to start this work is on CI-CD side."

He then immediately pivots to the code modernization topic as more relevant to Guhan. But the mention is strategic: it establishes that BayOne already has active work at Cisco, which gives Guhan confidence that BayOne is not an untested vendor. BayOne has already cleared procurement, already has a sponsor, and is already embedded.

**Why this matters for CICD:** The CICD engagement -- even before it delivers results -- is a credential. Its existence reduces the "first engagement penalty" (Set 03) for any expansion into Guhan's organization. This is a bidirectional value loop: CICD success validates BayOne for Guhan's work, and Guhan's interest validates BayOne as a multi-engagement partner for Anand.

---

## The Agentic AI Bolt-On Risk

Colin makes a sharp observation about how organizations typically adopt agentic AI:

> "Agentic AI specifically. That one is the toughest because people tend to bolt things on. It always ends up being, hey, I wrote this plugin for this tool integration. Great. That's one more thing that we have to worry about."

He connects this to modernization:

> "Even when you're modernizing, what you choose and how you choose to build it. Even if the UI is the same, the backend and the things that the customer doesn't see could be different. And it can allow you to have better capabilities that are going to be more future proof."

**Why this matters for CICD:** The "bolt-on" anti-pattern is the same risk the CICD engagement faces. If Cisco teams adopt AI tools piecemeal (a ChatGPT plugin here, a code assistant there), the result is more fragmentation, not less. The CICD engagement's pipeline standardization work can include governance for how AI tools are integrated -- preventing the bolt-on pattern rather than just automating existing workflows.

---

## The ChatGPT Misconception

Colin identifies a specific misconception about AI-assisted code modernization:

> "What ends up happening is you have developers saying, oh, ChatGPT can do this for me. I can copy and paste code. I can put in a file, get out a file, and it converts. The problem is that that's not how systems work. If you look at them as individual files, then what happens is, yes, you've done your job of converting, but now it can't talk to anything else."

He elaborates:

> "The nuance between languages or even frameworks. What exists in one might not even have a concept in the other. For instance, JavaScript versus Rust. These are two entirely different paradigms. So you have to know those nuances and capture those before you just start planning converting, because anything can convert."

**Why this matters for CICD:** This is Colin establishing himself as someone who understands AI's limitations, not just its capabilities. For the CICD engagement, this credibility is important: when Colin recommends specific AI-enhanced pipeline tools or approaches, Cisco engineers will trust that he has thought through the integration challenges, not just reached for the trendiest tool. It also reinforces the "determinism in AI" positioning.

---

## Scale: 45-50 Million Lines of Code

Guhan states the scale of Cisco's codebase:

> "We have easily 45-50 million lines of code which are across like six or eight parts and we can't go and rebuild."

This is the broader codebase context that the CICD work sits within. Any CI/CD improvements must account for the fact that they are operating on a small portion of an enormous, multi-generational codebase. The pipeline changes cannot assume clean architecture, consistent coding standards, or modern dependency management.

Guhan also frames the economics:

> "We can't step in the direction with no return of investment for sure. That's not where we want to go."

**Why this matters for CICD:** The CICD engagement must deliver measurable ROI on a subset of this 45-50M line codebase, not try to boil the ocean. The "A+F use case first" approach (Set 01) is the right strategy for this scale. Success means proving that pipeline improvements work on a specific segment, then replicating the pattern across additional segments.

---

## Guhan's Azure AI Platform (Not CICD, But Context)

Guhan references an existing AI platform initiative:

> "We have an Azure-based platform, we are building a team, and we did it last year and we are into the GA phase of this, we are working through that. But that's, I think, more like at this point staffed and we are continuing to review what is needed."

He clarifies that this platform is "not an agentic product, it's a traditional network management product, but modernized product."

**Why this matters for CICD:** This tells us Guhan's organization already has an Azure-based deployment pipeline for at least one product. If the CICD engagement's work for Anand/Srinivas produces pipeline templates or automation patterns, there may be reusability with Guhan's Azure-based platform. This is speculative but worth noting as a potential convergence point.

---

## Fact vs. Interpretation

| Item | Fact (stated in transcript) | Interpretation (inferred) |
|------|---------------------------|--------------------------|
| 45-50M lines of code across 6-8 parts | Guhan states directly | This is the total codebase, not just the CICD-relevant portion. CICD work operates on a subset. |
| CTO is "very vocal" about AI | Guhan states directly | Top-down AI mandate creates favorable conditions for AI-enhanced CICD framing |
| Meryl said CICD is "somewhat relevant" | Colin relays this in conversation | Weak connection -- Meryl acknowledges awareness but does not express strong interest |
| Guhan wants strategic consulting | Guhan states: "it's not just about implementing" | Colin's consulting posture is the correct positioning for this buyer |
| Teams running competing experiments | Guhan states: "everyone trying" | Same consolidation problem as CICD environment; pipeline standardization is the answer |
| Azure platform is staffed, in GA | Guhan states directly | Not an immediate opportunity for BayOne, but a potential convergence point for CICD pipeline work |
| Colin mentions CICD as existing Cisco work | Colin states in self-introduction | Strategic: establishes BayOne as already embedded, reducing first-engagement risk |
