# 05 - Meeting: Architecture and Deployment

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Focused deep dive on the layered architecture and deployment environment

---

## Context: Time Compression

Brad announced a hard stop at 2:30, which forced Colin to compress the architecture presentation significantly. At the moment Brad flagged the time constraint, Colin had just finished covering prior attempt analysis and golden set / labeling methodology, and was transitioning into the architecture recommendation. Colin had additional slides covering Azure-specific deployment details that he acknowledged were skipped: "I didn't go into the Azure part that's right down below this, but I'll pause here for questions on anything related."

The architecture presentation itself was delivered in a compressed form. Colin moved through the layered funnel concept quickly and did not get to elaborate on the Azure-specific deployment architecture, the full scaling discussion, or the detailed technical environment slides he had prepared. Despite the compression, the core architectural argument landed effectively, as evidenced by Mikhail's recognition moment (documented below).

---

## Colin's Layered Architecture Presentation

### The Core Argument: Not One Approach, All Three

Colin introduced the architecture by directly rejecting the idea of choosing a single technique. This was a deliberate reframing of how Lam had approached the problem previously:

> "The answer is not rejects or ML or GenAI. It is a tasteful combination of different things."

He framed the architecture as "layers of an onion" -- a metaphor he attributed to Brad's own earlier intuition: "Brad, you're 100% right. It's layers of an onion, is how I describe."

### Layer 1: The Deterministic Layer

Colin positioned the deterministic layer as the foundation -- the cheapest and fastest gate in the funnel:

> "The first layer of this is what I call is the deterministic layer. This is where things like any of the rule-based approaches, rejects approaches, this is where they fall into. The idea here is these are the least cost-heavy. And I say cost in terms of both resources, in terms of financial, and also in terms of compute."

The deterministic layer's function is flagging, not deciding:

> "That will flag things to you. That does not make a decision. That just simply says, this looks suspicious. Think of this like when you're at the airport, you're going through the scanner, something gets flagged in your bag. The machine doesn't say whether or not that's harmful or not unless it's a very obvious violation. It passes it to the human for a second round of judgment."

Colin explicitly called out the ceiling problem if you stop at this layer alone:

> "If I would stop here, you're going to hit that same wall you already hit. Which is to say, unless the data is very highly separable between the classes, you're still going to hit a ceiling for how accurate you can be. Because you're always going to be playing catch-up."

He used a lock-and-thief analogy: "The thief learns how to pick the lock, the lock maker makes a better lock. Thief learns to pick the lock, and so on we go forever. It's the same thing here. You're always going to have more examples to add on to this."

#### Enterprise Tooling: Microsoft Purview

Colin specifically positioned Microsoft Purview as the enterprise-grade implementation of the deterministic layer, and made a deliberate case for it over custom-built regex scripts:

> "If you are using something that has a Regex capability, absolutely you can do it with Regex. It's a simple Python script, right? But there's also enterprise tooling for that, like Microsoft Purview. There is a big advantage to this."

The advantage he articulated was maintenance and scalability over time:

> "Because if you can go the enterprise-type solution, what you are going to lose out on is the maintenance burden of this. And having a system that's connected from day one, that is a huge advantage, especially as you go forward."

Colin then told a story that resonated with the room -- the classic POC-to-production drift problem:

> "Usually, from an engineering perspective, I've lived it myself. We build a really cool thing. It's in POC mode. Suddenly, it's in production, as we like to call it. It's still the POC, but it's got a production stamp on it now. But then over time, the system starts to drift or fall apart or, you know, someone gets promoted because she did such a good job on this POC."

He described Purview as "essentially like imagine RegEx at scale and distributed across applications," emphasizing that it prevents duplicating effort across Lam's constellation of applications and frees the engineering team from ongoing maintenance.

### Layer 2: The ML/NLP Layer

The second layer handles what passes through the deterministic filter. Colin named specific techniques:

> "Pass it to the ML models or NLP models more specifically that you might want to have. In those cases, those are still cheaper, and those could be run on-prem. Those are easy to host, something like sentence transformers as well, or even just the techniques within NLP space. So things like TFIDF, for example."

The efficiency argument was explicit -- the deterministic layer cuts the problem space down before anything computationally expensive runs:

> "If you start out with the deterministic things that are very fast, very cheap, I already know I can ignore 80% here. So now my problem just got cut down by a very large amount."

Colin noted sentence transformers and TFIDF specifically as cost-effective middle-tier tools that can provide meaningful accuracy gains without the expense of a full generative AI model.

### Layer 3: The Gen AI Layer

The Gen AI layer sits at the narrow end of the funnel, handling contextual edge cases:

> "My rule-based approach flagged this. My ML approach does agree or maybe it disagrees, but it's not quite certain. Let's give it to the gen AI model next for the final one."

Colin was clear that Gen AI should not be the first resort:

> "Heavy hitter would be send everything to a language model. You can't do that. It doesn't scale. The costing doesn't make sense, and performance isn't great."

He also noted that in many deployments, the full three-tier stack is not always necessary:

> "It's not to say you always need all three. In most cases, it's generally enough to have rule-based plus gen AI for those edge cases."

### The Linear Funnel vs. Lam's Prior Parallel Approach

This was a critical moment in the presentation. Colin directly contrasted his linear/funnel architecture against what Lam had tried previously -- running multiple models in parallel and reconciling their outputs:

> "The reason why this is different is that this is intentionally linear. So the problem with, I think, what might have been tried earlier, which is give it the same thing to three models and see if they agree. That's a modified take on mixture of experts, which is probably if it's 18 months ago, that was the hot architecture of that time with Mistral MOE."

Colin identified the fundamental flaw in the parallel approach:

> "The reason why that doesn't work is because you're essentially saying that all three of these have an equal chance of being right. So if they're not all equal, well then that's a biased group that you're having judged and it does matter as the content as well."

He then articulated why the linear approach outperforms:

> "This type of an approach where it's linear, each gate results in a higher accuracy as a result and it also is more efficient than any one of those on its own."

### Production Proof Points

Colin closed the architecture section with a direct credential statement, citing Coherent Corporation:

> "For myself, at Coherent, this was something that 40,000 people are using every day. And that's something that also got deployed to aerospace and defense. It works on-prem. It works in the cloud. It works even on air gap devices, too. So this is a very proven type of approach to this problem."

---

## The "Accidental Hodgepodge" Recognition Moment

This exchange is a credibility milestone. After Colin presented the layered architecture explaining the deterministic, ML/NLP, and Gen AI tiers, Mikhail connected the dots to what Lam had previously built. The exchange proceeded as follows:

**Mikhail:** "So basically, and this is just from my understanding, so when you said hugging face, and that's a small language model, and then transformers, like in our case, spaCy, that's an NLP model?"

**Colin:** "That's correct, that's correct."

**Mikhail:** "So we just literally picked like a hodgepodge of stuff and then stuck a reject on top of that as well."

Colin did not pile on. He validated the approach gently:

> "Yeah, okay. But yes, so and that's the reason so if you do one of those it probably has some level of accuracy. It's really like if you were to multiply probabilities together. That's essentially what you would get if you combine those without a structured approach to it."

Mikhail then added the Azure AI layer to his own self-diagnosis:

**Mikhail:** "And again Azure AI on top of that. That's now LLM. So we just basically accidentally pick literally every single thing, one of each."

**Colin's response was deliberately generous:** "It's everyone does it. So yeah, it's okay."

**Mikhail then clarified his position:** "I wasn't the one picking it. I'm coming in from the business side of things. I'm just confirming what I just heard like Colin talked about and I like picked up on some of the acronyms and I was like, okay, that makes sense."

Colin then provided additional technical precision about transformers as an architecture:

> "Even for Transformers, so Transformers is the architecture that is the backbone for pretty much everything except for the IBM models. So probably what you tried was sentence Transformers, if I had to guess."

**Mikhail confirmed:** "It was spaCy."

**Why this moment matters:** Mikhail, coming from the business/product management side, independently recognized that Lam's prior attempt had assembled one tool from each tier (regex, NLP/spaCy, Hugging Face model, Azure AI/LLM) but ran them in an unstructured parallel configuration rather than a linear funnel. Colin's architecture presentation gave Mikhail the vocabulary and framework to diagnose what went wrong. This is a trust-building moment -- Colin did not criticize the prior work; he provided the framework that let the client arrive at the diagnosis themselves.

---

## Deployment Environment Discussion

### Daniel's Early Intervention on Edge AI / SLMs

Daniel raised the deployment environment question very early in the meeting, before Colin had reached his architecture slides. This set up a recurring thread throughout the conversation.

**Daniel's initial question** (delivered as Colin was setting up the problem statement):

> "Are we only focused on the enterprise implementation or are we considering offline or small language models?"

**Brad's immediate response** was to scope it down:

> "We're going to prove the use case first. The first thing when we were describing the business case is the cam flow. Self-help escalate. As it relates to enterprise products."

**Daniel pushed back**, arguing for future-proofing:

> "100% agree, but if we're not bringing it up as, hey, this is where we see ourselves five, 10 years from now... I'm trying to piece together is that when we talk about large language model to small language model parity or collaboration and what parameters exist within each of them, if we have the ability of saying, hey, the LLM that we're potentially using to support this business case enables this other possibility as opposed to we're not going to solve for it now, but having a conversation around, hey, we'll be able to jump to this area later on based on the technology we use."

**Brad then added a critical clarification** that reframed the entire technology selection:

> "You're already saying LLM is a solution. Machine learning is still on the table. We don't have to use LLM."

**Daniel acknowledged this** and restated his concern as an architecture risk:

> "Because if we don't bring that up as, hey, there's a potential, but we're focused on enterprise, we don't want to architect ourselves into all of us."

This exchange established Daniel's consistent concern throughout the meeting: ensuring that whatever is built for the cloud POC does not preclude future deployment to disconnected/air-gapped fab environments.

### Daniel's Definition of On-Prem vs. Mikhail's Definition

A notable terminology clarification occurred. When Colin asked about Azure vs. on-prem for the POC, Daniel interjected:

> "I have a different definition for that when I think about our customer fabs and Edge AI and small language models. So that's what I think of as on-premises. I know that AI Foundry has compatibility with Edge AI and these small language models. So if we're moving forward with this recommendation, again, try to communicate compatibility or incompatibility with that type of model, just so we know what we're getting into."

**Mikhail clarified the internal terminology:**

> "To me, on-prem is not a disconnect, and it's rather running on the server at our data center versus being on cloud."

And further:

> "That is not on-prem versus Azure. That's to me disconnected environment, right? That's fab-specific deployments."

This established three distinct deployment modes in Lam's vocabulary:

1. **Cloud** -- Azure-hosted (hyperscaler)
2. **On-prem** -- Lam's own data center, network-connected
3. **Disconnected** -- Customer fab-specific, air-gapped environments

### Colin's Position on SLMs

Colin gave a direct, opinionated answer on when small language models make sense:

> "On-prem, the only time I'm ever going to recommend on-prem is in two scenarios exclusively. One, if you're in healthcare or manufacturing and this is critical to production and you need this to run 100% of the time. That's the only real motivation for on-prem on one side."

> "The second is from a security compliance, if there's anything ITAR or military related where you have a specific thing. For instance, when we were doing FedRAMP, it had to be on-prem, it couldn't not be."

On SLMs specifically:

> "There's no actual reason to use small language models unless you're doing on-prem. They're actually more expensive to run on cloud infrastructure, to be honest with you, and the performance is way lower than normal models."

> "I love them. I'm a big proponent of hugging face. I contribute all the time on hugging face. But in reality, unless there's a real business reason that you guys tell us, hey, we need to use SLMs and we have to do it on prem, then I'm probably not going to even look at them in their direction."

### Daniel's Fab Data Cleansing Use Case

Daniel articulated a specific use case for SLMs in disconnected environments:

> "If at any point we want to cleanse the data before it's making its way back into the enterprise, and we still want to run cleansing within the enterprise as well. Depending on how that data is getting captured in the customer clean room, we can actually go through an approval process with the customer in their data out policy prior to ingestion getting into the enterprise."

He pressed for clarity:

> "We need to be very clear around whether we're supporting SLMs or not."

### Brad's Directive: Cloud First, Future Parity

Brad gave the definitive scope directive for the engagement:

> "Focus on the cloud for the primary use case, but discussions in future thinking about how to achieve parity between those air gapped files as well."

The group then agreed on terminology to avoid confusion going forward:

> "Which we can call disconnected for the future so that there is no confusion. We call disconnected and then on-prem and then [cloud]."

### Colin's Three Deployment Modes Summary

Colin synthesized the discussion into three modes:

> "I think we have really three, because we're not talking about on-prem versus this. So Michael, I agree. So one case, you're talking about air-gapped. Anytime Edge device is written, you're talking about air-gapped. Then you're talking about true on-prem, which is there's a server running that's hosting the models on-premise, which, to be honest, that doesn't usually make sense in terms of cost or maintenance. And then you have cloud-based, which is going to use one of the hyperscalers."

He then clarified the POC scope:

> "For the POC's sake, so if we're talking about architecture that has to be air gapped, that's a totally different conversation than this. Even for cleansing, that's still totally different. All I would ask is just tell me what you want me to shoot for here."

---

## Existing Azure Environment Details

Mikhail revealed that the prior project's Azure infrastructure is still partially operational:

> "From the last project, we've only partially spun down the old environment, so we still have access to it."

On the specific state of the environment:

> "Some of, I don't know if we stand on full envelope side of things, but audit aid stuff is all up and running where actually we just disabled the hourly jobs and that's it. So that environment is full out."

He further detailed the data pipeline infrastructure:

> "So we already have kind of the environments we could even use for this. And they have data, hourly data retrieval jobs that could get data out of the system that we use for."

This is significant for POC planning: the Azure environment does not need to be built from scratch. The infrastructure exists, the data pipelines exist (though the scheduled jobs are currently disabled), and the audit aid components are still running. The primary action would be re-enabling the data retrieval jobs and deploying the new architecture into the existing environment.

---

## What Was Skipped Due to Time Constraints

Colin explicitly noted he had additional Azure-specific content prepared but not presented:

> "I didn't go into the Azure part that's right down below this, but I'll pause here for questions on anything related."

Based on the flow of the presentation, the following topics were prepared but not covered in depth:

- **Azure-specific deployment architecture** -- Colin had slides below the architecture diagram covering Azure implementation details
- **Scaling discussion** -- Colin mentioned volume and scale considerations ("getting a general idea of how much information is flowing through the system") but deferred detailed discussion
- **Full technical environment deep dive** -- The group agreed this would need a separate session: "the technical environment specifically itself is a very elaborate so I think this would need a much more deeper scenario"
- **Detailed cost comparison** across deployment modes (cloud vs. on-prem vs. disconnected)
- **Purview integration specifics** -- Mentioned as a concept but not elaborated

---

## Additional Context: Mikhail's Structured vs. Unstructured Data Distinction

During the deployment discussion, Mikhail made an important scoping clarification about what requires AI vs. what does not:

> "You're talking about structured data because rest of the data today could be easily segregated out of the data you don't need machine learning. This is for unstructured data."

He elaborated:

> "If it's structured inside of let's say tool file, that's what we will call the structured data that is easily segregateable elements that we could just remove before grabbing."

Daniel acknowledged but noted the unstructured data case:

> "If there are escalations that are captured in the fab and we need to be able to get documentation or [use AI]."

This distinction is important for architecture planning: structured data from tool files can be handled with simple field-level removal (no AI needed), while unstructured text from escalations, problem statements, and free-text fields is where the layered architecture applies.

---

## Key Takeaways for Architecture and Deployment Planning

1. **Architecture is validated conceptually.** The layered funnel approach (deterministic -> ML/NLP -> Gen AI) landed well with the room. Mikhail's self-diagnosis of the "accidental hodgepodge" confirms understanding.

2. **POC deployment target is Azure cloud.** Brad's directive is unambiguous. The existing partially-active Azure environment with data retrieval pipelines provides a head start.

3. **Disconnected/air-gapped is a future requirement, not a POC requirement.** Daniel's concerns are acknowledged and the group agreed to keep architectural compatibility in mind without solving for it now.

4. **SLMs are off the table for the POC.** Colin's position is clear and was not contested. SLMs only become relevant if/when the engagement extends to disconnected fab environments.

5. **Purview is positioned as the enterprise-grade deterministic layer.** This has implications for long-term maintainability and reduces engineering burden versus custom regex scripts.

6. **The prior parallel approach (modified mixture of experts) is understood as flawed.** The room now has shared vocabulary for why running three models in parallel with reconciliation produced 17-21% false positive rates.

7. **The Azure-specific architecture and technical environment deep dive are outstanding items** that need to be covered in a subsequent session or in the proposal document.
