# 05 - Meeting: Application and Prior Work

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Focused deep dive on the Escalation Solver application and prior technical work

---

## 1. The Application: Escalation Solver

### 1.1 Application Name and Nature

The application under discussion is called **Escalation Solver**. Colin explicitly asked for the application name, and it was confirmed directly:

> "Application name is escalation solver."

Escalation Solver is a homegrown platform -- built internally at Lam Research, not a commercial off-the-shelf product. Mikhail described its nature and lineage:

> "So we have an escalation system. It's a platform. It's homegrown built. There's got some security built into it and so forth -- ASM, which is Applications Security Manager, which manages some of the people in the profiles."

### 1.2 What the Application Does

Escalation Solver is the mandatory escalation tracking system for field service operations. Mikhail provided the operational context:

> "Anytime that a field engineer or someone in the field goes to do an installed maintenance upgrade, whatever it may be, they're required to create a work order. And if they run into an issue and they can't solve it within eight hours, they're required to open up and escalate petition."

The application drives an automatic process from that point forward. It contains both structured and unstructured data and information, and it has capabilities for troubleshooting, "fish phoning" (likely "siphoning" or a specialized term), and other workflow functions. Mikhail described the broader lifecycle:

> "It also does closure reports and so forth so you can capture the learning and then those can either be, they can generate follow-up actions which are either engineering design changes, procedure changes, it could be tech articles, it could drive ongoing actions."

### 1.3 Why This Application Was Selected

Mikhail was clear about the selection criteria. It was not primarily an ROI decision -- it was driven by data accessibility, variation in content, and being the natural first candidate for operationalizing the redaction/detection capability:

> "We were proving out the concept that was the easier to get data access to and the most variations where we could truly prove out the use case."

He added that consistency of the data was important for a meaningful proof of concept:

> "In order to provide a use case you need consistency of data itself, right? Or consistency of inconsistency, so to speak."

He also explicitly stated that if the concept could be proven on Escalation Solver, this would be the first application targeted for production deployment:

> "If we were able to prove out, this would be the first application also to start going after."

---

## 2. The Five Text Fields and Two Elements

### 2.1 Five Fields, Two Target Elements

The prior work focused on five specific text fields within Escalation Solver, searching for two specific identifiable elements. Mikhail carefully distinguished between the fields and the elements:

> "It's five data fields but the two -- what you call them -- elements. Customer name and fab ID. So we're looking for two specific identifiers within five free text fields."

Colin confirmed with a follow-up, and Mikhail reiterated that this was an intentional scoping decision:

> "But there's more than five data fields. I don't want to say there's five data fields. We just said, hey, let's pick these five, these two elements, and see if we can prove this use case. It starts small, right?"

### 2.2 Field Characteristics

The five fields are free text fields where users type problem statements and related information. They are substantial in size. Mikhail provided the character counts:

> "Five fields, somewhere between 5,000 and 4,000 characters."

This means each field is 4,000 to 5,000 characters of free text. These are not short-form entries -- they are lengthy narrative descriptions. Mikhail described what users enter:

> "What it doesn't populate is what's your problem statement. And these other things that you have to fill out. So if they typed in there, I'm having a plasma arcing issue at, and you start [describing] my customer site and start giving a lot of detail."

He further clarified the nature of the different fields later in the discussion:

> "One is problem statements. I mean, you know, they're all describing a problem. Yes, it's different problems, but they look very, very similar across the board. The other ones describe additional things like actions taken."

So the fields include things like problem statement, actions taken, and other narrative elements -- all similar in structure (free text describing technical situations), which Mikhail acknowledged makes the classification problem harder due to high similarity between classes.

### 2.3 Auto-Population vs. Free Text

Mikhail drew a clear distinction between the structured fields that auto-populate and the free text fields that are the problem. Using an analogy:

> "Think of it like you go in, you order Amazon or something, put in your zip code, it automatically populates your city and so forth. So based on the tool ID and so forth, because there's connections, it will all populate a bunch of fields, right? But what it doesn't populate is what's your problem statement."

The structured fields (tool ID, customer name as a structured field, fab ID as a structured field) are not the problem. The problem is the five free text fields where a field engineer may inadvertently type customer names, fab locations, or other sensitive identifiers into narrative text.

### 2.4 The Definitive Policy

There is a stated, explicit policy within the Escalation Solver application that users should not enter customer confidential information. Mikhail noted this as relevant context:

> "And there is a definitive policy in that application not to enter customer confidential information."

This is significant: the policy exists, but users violate it routinely in practice by including customer names, fab IDs, and other identifiers in their free text problem descriptions. The detection/redaction system is needed precisely because the policy alone is insufficient to prevent the behavior.

---

## 3. Prior Technical Work: The Presidio Starting Point

### 3.1 Attribution: Mikhail Drove the Technical Discussion

A critical observation about this meeting: **Mikhail provided virtually all of the technical detail about the prior work.** Daniel, the director of engineering, explicitly stated at the outset that he was in an information-gathering role:

> "I think I'm more on the information gathering side today as opposed to being in contribution just unless I see anything egregious."

Despite being director of engineering for the GFSO area covering the products Mikhail manages, Daniel did not drive the technical discussion about what was tried. When Brad asked about the technical implementation, Mikhail stepped in:

> "If you need me to speak on this, I can totally because I was enrolled from day one."

This is notable: the product management lead (Mikhail), not the engineering lead (Daniel), was the person most knowledgeable about the technical implementation of the prior attempt. This aligns with observations from the first discovery call where Mikhail was the primary source for technical details despite being in a product role.

### 3.2 Starting with Presidio: 12 Models Evaluated

The work started with **Microsoft Presidio**, the open-source PII detection and anonymization framework. Mikhail described the progression:

> "So we started first -- now going back to your answer -- we started with Presidio models. We took about 12 models on Microsoft. We've looked at them. We narrowed down to three. We narrowed down to five and then to three. Yeah, we narrowed down to five and then to three."

The sequence was: 12 candidate models within the Presidio ecosystem were evaluated, narrowed to 5, then narrowed to 3. The narrowing criteria combined accuracy and performance:

> "We were trying to start with getting us a little bit of accuracy as well as performance was important, right? So we ran through a large, you know, 4,000 characters. If it passes, does it take a minute? Does it take 20 seconds and so forth? So we kind of balanced it out."

### 3.3 The Three Selected Models

Mikhail identified the three models that were ultimately selected. The identification was somewhat halting due to speech-to-text artifacts, but the three are:

1. **Transformers / Hugging Face Flair** -- Mikhail stated: "So transformers, which one from Hugging Face -- Flair." Later in the meeting he confirmed: "So we did pick one of the Hugging Face, right? I remember Flair was the one that we picked."
2. **SpaCy** -- An NLP model. Brad later helped clarify the categorization: "So when you said Hugging Face, and that's a small language model, and then Transformers, like in our case, SpaCy, that's an NLP model?" Colin confirmed: "That's correct."
3. **Azure AI** -- One of Microsoft's cloud-based AI models. Mikhail described this as a substitution: "We actually narrowed it down to three, then removed one and added Azure AI. That's one of the Azure models."

So the final three were not simply the top three from the initial evaluation. They removed one of the original three and substituted Azure AI, arriving at: Hugging Face Flair (transformer-based), SpaCy (NLP), and Azure AI (cloud LLM).

Brad's characterization of the selection, which Mikhail confirmed, was revealing:

> Brad: "So we just basically accidentally picked literally every single thing, one of each."
> Mikhail confirmed: "It's everyone does it."

Colin also noted that in addition to these three, a rule-based component was layered on: "We've also later introduced rule-based one as well, just to see if we can get the accuracy out."

### 3.4 Why These Models and Not Larger LLMs

Colin asked directly why larger models (like GPT-4.0, which would have been available 18 months ago) were not used. This was a key diagnostic question. Mikhail's answer was candid:

> "Thinking about the context 18 months ago, we were still going through NDAs and security evaluations of [cloud] models and what services we were going to allow within our ecosystem. And we were still in major discovery things."

Daniel reinforced this:

> "Between the legal and technical constraints and the discovery that was going on, I don't think there's going to be anything that we can definitively say we chose these over another explicitly for their capabilities."

The model selection was constrained by the organizational and legal environment 18 months ago, not by a deliberate technical evaluation of model capabilities. This is architecturally significant: the team did not have access to the models that would have been most effective for this use case due to the enterprise's security evaluation process still being underway.

---

## 4. The Standalone Service Architecture

### 4.1 A Redaction Service, Not an Application Feature

This is one of the most architecturally significant details from the meeting. Mikhail made a sharp correction when the discussion implied the detection/redaction work was built into Escalation Solver:

> "So there's a big difference between application and application data. We've actually built this as a standalone service. We did not build it into the application when we're proving this out. We use this application data because we wanted a standalone thing [that] any application [could call]."

He then described its interface pattern:

> "Call it a redaction service. You can just pass in and get detection, or you pass in and you get redacted text back as well. So that was the key."

This means the team designed the system from day one as a **reusable microservice** with a pass-in/pass-out API pattern. Any application at Lam could call this service, submit text, and receive either detection results (flags for potential PII/IP violations) or redacted text with the violations removed. They were not building a feature inside Escalation Solver -- they were building an enterprise capability that was merely being tested against Escalation Solver data.

### 4.2 Significance for Future Scope

This design decision has major implications. It means:

- The architecture already supports the multi-application future that Lam envisions (the "constellation" of tools Colin referenced from the first discovery call).
- The POC or engagement work does not need to re-architect the integration pattern -- the service boundary already exists.
- Any improvements to the detection/redaction models benefit all consuming applications simultaneously.
- The deployment topology (cloud, on-prem, hybrid) is a decision about where the service runs, not about how it integrates with each application.

---

## 5. On-Prem Kubernetes Deployment

### 5.1 Initial Deployment Environment

The models were not deployed to Azure initially. Mikhail described the infrastructure:

> "We initially launched them on the Kubernetes. We didn't even put them anywhere, like we use anything in a cloud, so to speak, right? We deployed them on prem and Kubernetes and so forth, while we're evaluating."

The one exception was Azure AI, which by nature runs on Azure:

> "Azure AI, I think that was the only one we didn't, obviously, do that."

So the deployment architecture during the prior work was: Hugging Face Flair and SpaCy running on on-premises Kubernetes, with Azure AI running in Azure cloud. The reconciliation algorithm (described below) would have been calling across these environments.

### 5.2 Current State of the Environment

The environment has not been fully decommissioned. Mikhail indicated it could be reused:

> "From the last project, we've only partially spun down the old environment, so we still have access to it. Some of, I don't know if we [spun down the] full envelope side of things, but [the Azure AI] stuff is all up and running where actually we just disabled the hourly jobs and that's it. So that environment is [fully] out. So we already have kind of the environments we could even use for this."

---

## 6. The Reconciliation Algorithm

### 6.1 Three Models in Parallel with Reconciliation

The architecture ran all three models simultaneously against the same input, then used a reconciliation algorithm to determine the final result. Mikhail described this:

> "The way we've done this, because we're still evaluating them, you could see what each model returned. And then we had a reconciliation algorithm, which would actually not call one versus the other. It would call all three in parallel and then reconcile between the two."

The "reconcile between the two" phrasing likely refers to reconciling the results pairwise or reaching consensus -- the algorithm was looking for agreement among the models. This is essentially a voting or ensemble approach.

### 6.2 Colin's Diagnosis of the Approach

Colin identified this as a variant of **mixture of experts (MOE)**, which he noted was the hot architecture approximately 18 months ago (associated with Mistral MOE). He explained why it did not produce the expected results:

> "The problem with, I think, what might have been tried earlier, which is give it the same thing to three models and see if they agree. That's a modified take on mixture of experts. But the reason why that doesn't work is because you're essentially saying that all three of these have an equal chance of being right. So if they're not all equal, well then that's a biased group that you're having judged."

Colin's recommended alternative was a **linear, layered approach** (deterministic first, then ML/NLP, then GenAI) rather than the parallel consensus approach. This is the core architectural recommendation that emerged from the discussion.

---

## 7. False Positive and Accuracy Numbers

### 7.1 The 21% False Positive Rate

Mikhail provided the initial false positive rate with specificity:

> "The false positive rate was super high, like on the magnitude of -- I think we were at 21%."

This is the rate from the individual models or the initial evaluation before reconciliation was applied.

### 7.2 Reduction to 17% with Reconciliation

After the reconciliation algorithm was applied (running all three models in parallel and having them vote), the false positive rate dropped, but not enough:

> "The false positive rate didn't decrease significantly when we start doing that. It went from 21% to 17%. So it was still, all of them were consistently, at least two models would agree that [it] would still need to be redacted."

The improvement was only 4 percentage points (21% to 17%), which Mikhail characterized as insufficient. The consensus approach consistently over-flagged because "at least two models would agree" on false positives -- the models shared similar biases.

### 7.3 The 90% Detection Accuracy

Mikhail provided a separate accuracy figure:

> "Accuracy, I think we were close to 90% accuracy rate."

He then immediately qualified this number based on use case:

> "If you're looking just at a detection use case, that's probably a great number. If you're looking for redaction where you need to be able to open up, 90% confidence is nowhere near [what] you can use."

This is a critical distinction: 90% accuracy may be acceptable for detection (flagging things for human review), but it is completely unacceptable for automated redaction (where incorrect redaction destroys usable information).

### 7.4 Target Metrics

The target false positive rates were stated in two tiers:

- **MVP target:** Less than 5% false positives. Mikhail: "Less than 5% false positives. Well, that was for MVP. Saying okay to support temporarily."
- **Ultimate target:** Under 1% false positives. Mikhail: "So our ultimate was under 1% false positives. That was the agreement."

For the MVP target, the operational stakeholder (referred to as "his team") was willing to tolerate 5% temporarily. For accuracy, Mikhail acknowledged it depends heavily on the use case:

> "If I get false positive under 1% and 75% accuracy, is detection okay? Probably. Redaction, we're not even going to start that conversation."

---

## 8. The Root Cause: Globally Trained Models and No Golden Set

### 8.1 Globally Trained Models Producing Contextual Mismatches

Mikhail identified what he understood to be a core problem. The models came pre-trained on global data and did not understand Lam-specific context:

> "One of the problems we ran into pretty quickly was these models are globally trained so a lot of things contextually they were redacting on our side which was not customer confidential even because they were trained -- because these are not our models that come in blend, right? They come in pre-trained."

The models were flagging terms as sensitive that were perfectly fine in Lam's context because they had been trained on general-purpose PII patterns, not semiconductor industry patterns.

### 8.2 The Lack of a Golden Set

When Colin asked about the training data and golden set, Mikhail was direct:

> "So there's three answers to that. So we didn't have a golden set because we were told -- or at least I was told -- that we have to do the labeling to create that set. Right, wrong, and different. I'm just telling you that."

This is a significant admission: the team was advised that creating a golden set required a full labeling exercise, and that advice effectively blocked them from doing it. Mikhail did not necessarily agree with that framing ("right, wrong, and different") but reported it as what happened.

Colin's assessment was that the lack of a golden set was "probably where you hit most of the wall":

> "The output limit of your model is limited to the accuracy of whatever you gave it, and if that's a small set, or if it's not labeled, you're proportionally limited as to what the accuracy of that system can be."

### 8.3 The Labeling Cost Barrier

The labeling effort was scoped and found to be cost-prohibitive:

> "We did not train those models. We trained them with our acronym, we trained them with exclusion list. What we haven't done was the labeling effort. Because our estimates was over a thousand hours, man hours, to [do it]. Just straight up labeling effort, and that was cost prohibited from the value we're going to receive. And that is initial effort, that's not ongoing effort."

Mikhail explicitly said this estimate was for the initial effort only -- ongoing labeling to maintain the system would add further cost on top of the 1,000+ hour initial investment.

---

## 9. The Three Reference Lists

### 9.1 What Was Used Instead of a Golden Set

In the absence of a properly labeled golden set, the team used three reference lists for the models:

1. **Customer name list** -- A list of customer names loaded into the system so the models could detect them. Mikhail: "We loaded the list of customers."

2. **Fab list** -- A list of fab IDs / fab locations. Mikhail: "We loaded the list of fabs, you know, whatever we had from a location."

3. **Acronym exclusion list (~3,000 acronyms)** -- A list of approximately 3,000 Lam-internal acronyms that were explicitly marked as safe (not customer confidential) so the models would not flag them. Mikhail: "Lam has a list of acronyms. We went through exercise to create a list of acronyms, and then from close to 3,000 -- we love acronyms -- where we removed things that were customers and basically said, this is an exclusion list, this is totally fine."

Colin's assessment was that this data set "probably only legitimately lends itself to being suitable for a rule-based approach." The lists are lookup tables, not labeled training data -- they tell a system what to look for or what to ignore, but they do not teach a model how to make contextual judgments about when an entity's presence constitutes a violation.

---

## 10. The Existing Thumbs Up / Thumbs Down UI

### 10.1 Existing Feedback Mechanism

The team has already built a user-facing feedback mechanism into the system. Mikhail revealed this during the discussion about labeling and ground truth:

> "We actually still do have already a UI, which actually gives you a thumbs up, thumbs down if the system is doing it properly or not. So the extension of is it true or not, it's already built in."

### 10.2 Approximately 1,000 Labeled Examples

When Colin asked about volume, Mikhail estimated the amount of feedback data collected:

> "I think we have about a thousand."

Colin asked if this would suffice as training data. Mikhail clarified it was across the five text fields:

> "A thousand -- which is a thumbs up, thumbs down."

Brad (from BayOne) framed this correctly as ongoing training data, not a one-time exercise:

> "It's not a [one-time]. It's a continuous loop. It's just the more you have, the better your data is."

Mikhail confirmed: "That's right. That's right."

Colin stated that the adequacy of this data could be determined through **exploratory data analysis (EDA)** -- specifically, examining how similar the data is among classes and how consistent it is within each class -- before committing to whether additional labeling would be needed.

### 10.3 Relevance to the Engagement

This existing feedback data is potentially valuable. It represents approximately 1,000 human judgments on whether the system correctly identified (or failed to identify) sensitive content. Brad (BayOne) noted that this aligns with modern training approaches:

> "These trainings have improved in the last few years. They are now, earlier it used to be just training of data, labeling and all. Now they're calling it pre-training, post-training. So for example, this thumbs up and down, which is already there that you mentioned in your UI, it's kind of an aspect of the post-training where you can improve on it."

---

## 11. The 18-Month Timeline

### 11.1 Age of the Prior Work

When Brad asked how old the prior effort was, Mikhail's answer was specific:

> "18 months old."

This places the start of the prior work at approximately October 2024 -- early in the current generative AI adoption cycle for enterprises. Mikhail acknowledged this context:

> "Remember, this is our first kind of dive into that space."

He explicitly characterized it as setting up a baseline rather than a benchmarking exercise:

> "It wasn't really a benchmarking that we're looking for. It's setting up a baseline, more than anything. Because again, at that time, we went for a reduction use case. As part of the learnings, the detection use case evolved out of that. It wasn't our primary use case."

This is an important detail: the team originally pursued **redaction** (automatically removing sensitive content) and only through the process of failing at redaction did they realize that **detection** (flagging sensitive content for human review) was a viable and valuable intermediate use case.

### 11.2 What Changed in 18 Months

Colin noted the significance of the timing gap:

> "18 months ago, it was still an early adoption. [Things have] improved quite a bit and a lot of them have changed in the landscape."

Mikhail also acknowledged this: the models available, the legal/security frameworks allowing their use, and the enterprise tooling have all evolved significantly since the prior attempt.

---

## 12. Existing Data Retrieval Jobs

### 12.1 Reusable Infrastructure

A detail that surfaced when discussing the current state of the partially decommissioned environment: there are existing data retrieval jobs that extract data from the Escalation Solver system. Mikhail stated:

> "And they have data, hourly data retrieval jobs that could get data out of the system that we use for [the prior work]."

These jobs are currently disabled but not deleted:

> "We just disabled the hourly jobs and that's it. So that environment is [fully intact]."

This means the data pipeline from Escalation Solver to the analysis/model environment already exists, was previously running on an hourly schedule, and could be re-enabled. This significantly reduces the time-to-data for any new engagement -- one of the most common bottlenecks Colin identified for enterprise AI projects.

### 12.2 Team Dependencies

Mikhail identified that the data infrastructure involves a specific team:

> "The majority of this outside of [Mikhail's work] is Orion, so just FYI. They're working on COS, so it's not that the team is not capable, it's a small team working on a supercritical project."

Mikhail indicated he could handle some of the data access himself, but certain elements would require Orion's team:

> "I should be able to do some of it, but some things will require Orion's attention from a data side."

---

## 13. Daniel's Role and Contributions

### 13.1 Director of Engineering Introduction

Daniel introduced himself at the start of the meeting:

> "Just a little bit of background. I'm director of engineering in our GFSO area, which covers all of the products that [Mikhail] is product managing, basically. Well, except for service on the services side."

His background: "Software development for about three decades and focus on test automation, quality assurance, software architecture, everything on software development teams except for UX."

### 13.2 Daniel's Focus Areas

Daniel's primary contributions during the meeting were not about the prior technical work but about **future architecture considerations**, specifically:

- **Edge AI and small language models:** Daniel repeatedly raised the question of whether the architecture needed to support disconnected/air-gapped environments at customer fabs. He wanted to ensure that whatever was built for the enterprise use case would not preclude future extension to edge deployments.

- **Model parity across environments:** Daniel asked: "If we're not bringing it up as, hey, this is where we see ourselves five, 10 years from now... I'm trying to piece together that when we talk about large language model to small language model parity or collaboration."

- **Definition precision:** Daniel pushed for clear definitions of "on-prem" versus "disconnected" versus "cloud," noting that he has a different definition of on-premises that relates to customer fabs and edge AI.

Brad (Mikhail's counterpart at BayOne) clarified the scoping decision: "We are going to prove the use case first. And we can prove the use case, then we'll determine, okay, can we do this in [on-prem]? Can we do this in a semi-connected mode and an offline mode?"

---

## 14. Colin's Architectural Recommendation (Summary)

While the focus of this document is the application and prior work, Colin's architectural recommendation emerged directly from diagnosing what was tried. The core insight: the prior team selected one model from each category (transformer/Hugging Face, NLP/SpaCy, cloud LLM/Azure AI) and ran them in parallel with a consensus algorithm. Brad's characterization was memorable:

> "So we just basically accidentally picked literally every single thing, one of each."

Colin's recommended approach is a **linear, layered architecture** instead of a parallel consensus architecture:

1. **Deterministic layer** (rule-based, regex, lookup tables, enterprise tooling like Microsoft Purview) -- fast, cheap, catches the obvious cases, filters out ~80% of the problem space.
2. **ML/NLP layer** (sentence transformers, SpaCy, TFIDF, etc.) -- catches patterns the rule-based layer misses, still relatively cheap and can run on-prem.
3. **GenAI layer** (large language model) -- final arbiter for edge cases where the first two layers disagree or are uncertain.

Colin drew from his direct experience:

> "For myself, at Coherent, this was something that 40,000 people are using every day. And that's something that also got deployed to aerospace and defense. It works on-prem. It works in the cloud. It works even on air gap devices, too."

---

## 15. Key Gaps and Open Items

Several items were identified but not resolved in this meeting:

1. **Specific model versions and configurations** -- Mikhail could not recall the exact third model before the Azure AI substitution. He stated: "I'm just not going to come to me right now for whatever reason."

2. **Detailed performance metrics beyond false positives** -- Mikhail mentioned using "recall, precision" and "many different criteria" but did not provide specific numbers for these metrics. The only hard numbers are: 21% initial false positive rate, 17% after reconciliation, and approximately 90% detection accuracy.

3. **The reconciliation algorithm specifics** -- How exactly the three-model consensus was calculated (majority vote, weighted, threshold-based) was not detailed.

4. **The Orion team's availability** -- Identified as a potential bottleneck for data access, with the team described as "small" and "working on a supercritical project."

5. **Full inventory of data fields** -- Mikhail stated there are more than five data fields in Escalation Solver; only five were selected for the prior work. The total number and nature of additional fields were not discussed.
