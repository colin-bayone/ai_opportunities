# 02 - Meeting: Technical Use Cases (Deep Dive)

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on technical use cases and requirements

---

## The Troubleshooting Workflow as Framework

Mikhail structures the entire discussion around the troubleshooting workflow used internally at Lam Research. He explicitly draws this on the whiteboard as a three-stage pipeline:

1. **Self-help** -- user searches using search tools or AI tools to find answers independently
2. **Ask for help** -- user asks a question to a specific community or group of experts
3. **Escalate** -- structured troubleshooting with more experts involved

Mikhail states directly: "So to set the premise, what I wanted to put on the board is our overall workflow that I'm going to use to represent some of the business cases. And that is our workflow in a troubleshooting."

He then maps two distinct business cases onto this workflow, each with fundamentally different technical requirements.

---

## Business Case 1: Self-Help Search (Redaction)

### The Problem

When a field service technician (or any user) searches the knowledge base, customer confidential information may be present in documents they should not have access to. The goal is to enable cross-customer knowledge sharing -- making solutions discoverable regardless of which customer engagement produced them -- without exposing customer IP.

Mikhail's example: "If document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."

Brad adds critical context about the current state: "Our current mode of operation is we over restrict." Mikhail confirms: "100%, right? And by doing that, we know that we're limiting because we're limiting the knowledge, the information, that kind of data, because when in doubt, we just restrict it."

Brad elaborates on the cost: "True, but we're also knowing that we're limiting the productivity, the capability, because we don't share that much."

### Technical Characteristics

- **Processing mode:** Batch / offline. This is not real-time. Mikhail explicitly contrasts it: "this could run an hour" (referring to the self-help redaction side) versus the ask-for-help side which "has to run within UI, whatever is UI standards, two to five seconds max."
- **Technique:** Redaction (heavy-handed). Mikhail: "a more heavy-handed reduction still happening once the data enters the flow to truly make sure things are not violating."
- **False positive tolerance:** High. Over-redaction is acceptable. Mikhail explicitly states: "this space we're right over-redacting. So if we over-redact less, we already have success." The bar for success is simply doing better than the current blanket restriction.
- **Data type:** Overwhelmingly unstructured. Mikhail: "Majority of the data that we're concerned with today for this discussion is unstructured data. So it lives inside documents. It could live inside the meeting transcripts. It could live in the procedures or a problem test."
- **No single search system:** Mikhail clarifies there are "six search formulas" -- not one unified search. He explicitly asks to discuss the problem conceptually rather than system-by-system: "That's why I want to talk conceptually, rather than specific systems, because we have, in some areas we have a single source, in some areas we have many, many different systems."

### What Success Looks Like

The current baseline is total restriction. Any improvement over blanket restriction is a win. Mikhail frames it as: "if we over-redact less, we already have success." This is a remarkably low bar -- the system does not need to be perfect, it just needs to be better than the binary restrict/allow approach currently in place.

---

## Business Case 2: Ask for Help / Escalation (Detection)

### The Problem

When a user enters a problem statement to ask for help or escalate an issue, they might inadvertently include customer confidential information. Mikhail's example: "the way you ask a question could present an IP risk if an Intel person asks the question in a way that exposes Intel's IP and a Samsung person [can see it]."

He clarifies what "Samsung person" means in this context: "what we say in Samsung, which really means in-lab employees, but that still, Samsung trusts us that it's not cross-shared, right? Because there could be like, oh, Samsung solved that problem, but that could be very proprietary."

### Technical Characteristics

- **Processing mode:** Real-time. Mikhail is explicit about the performance constraint: "How fast? Because this is real time, right? How fast you can get to detect and notify the user that they would have possible violation of customer confidential information." And later: "this has to run within UI, whatever is UI standards, two to five seconds max."
- **Technique:** Detection only, not redaction. Mikhail draws this distinction sharply: "In this case, we're not doing redaction. We're just doing detection and we're stopping there. We're letting users know that they might have issues and that we stop with the detection."
- **Action on detection:** Notification, not blocking. The business case explicitly calls for a warning approach: "let's start not enforcing the policy, but let's notify you to potentially could be violating. Still leave it up to the users to say, yes, I am. No, I'm not. Because we're never going to get it accurate enough, or we can 100% block it from entry."
- **False positive tolerance:** Extremely low. This is the critical differentiator. Mikhail: "The problem we ran into this approach... was not the accuracy of detection, but the accuracy around the false positives. Because this particular space is super sensitive to false positives. If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it."
- **Auditor trust problem:** The false positive issue extends beyond end users. Mikhail: "And if you constantly give auditors notifications, say, a possible violation, they're also going to not trust your system. They're going to turn off these notifications."

### What Success Looks Like

The system must provide real-time detection with a false positive rate well below 1%. Mikhail states the target directly: "we needed this number to be way below 1% end state." The 20% false positive rate achieved with their initial ML models was "absolutely unacceptable."

---

## The Detection vs. Redaction Distinction (Mikhail's Explicit Framing)

Mikhail draws this distinction repeatedly and with great precision. Key statements:

1. **Both are detection, but different kinds:** "And you made a great point, because in both cases, in this case, in this case, it's detection. It's just one is not performance focused. One is more accuracy focused. The other one is good enough, less false positive, performance focus."

2. **Redaction is what happens after detection in the self-help case:** "In this case [ask-for-help], we're not doing redaction. We're just doing detection and we're stopping there." Versus: "In this case [self-help], there is nobody to ask. We can't audit every document. So you are relying on this to, in some instances, either say, I can't redact and I'm going to redact, or no, I can't redact even though I detect this. So you're still going to restrict the document."

3. **Redaction is "heavy-handed" because of the variety of data formats:** Brad explains: "Redaction is a technique. Because in some cases, if it's inside a picture or like the OCR picture, you're still going to just retrieve the document rather than..." -- suggesting that in some cases the system would suppress the entire document rather than attempt fine-grained redaction within images.

4. **These are separate swim lanes:** Mikhail insists: "When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes." He later reinforces: "I want to caution against" combining use cases -- each entry point should be treated as a separate business case.

### Summary Table (derived from Mikhail's framing)

| Dimension | Self-Help Search | Ask for Help / Escalation |
|---|---|---|
| Technique | Detection + Redaction | Detection only |
| Processing | Batch (can run for an hour) | Real-time (2-5 seconds max) |
| Primary concern | Accuracy of redaction | False positive rate |
| False positive tolerance | High (over-redact is OK) | Very low (must be well below 1%) |
| Action on detection | Redact or restrict document | Notify user of possible violation |
| Current baseline | Blanket restriction | Blanket restriction |
| Success threshold | Any improvement over blanket restriction | User and auditor trust in notifications |

---

## False Positive Requirements: The Core Technical Challenge

### The Numbers

- **Current ML model performance:** 20% false positive rate per ticket. Mikhail: "we were hitting the rate of false positives of around 20% per ticket. Meaning 20% of tickets ended up with 20% false positive rate."
- **After fine-tuning:** Improved from 20% to 17%. Mikhail: "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."
- **Target:** "Way below 1% end state."
- **Colin's assessment of the 20% number:** "when I heard 20%... that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

### Why False Positives Are Devastating in the Ask-for-Help Case

Mikhail lays out two distinct failure modes from false positives:

1. **End user trust erosion:** "If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it."
2. **Auditor trust erosion:** "And if you constantly give auditors notifications, say, a possible violation, they're also going to not trust your system. They're going to turn off these notifications."

Both lead to the same outcome: the system gets ignored, which is worse than not having it at all because it creates a false sense of security.

### Why False Positives Are Tolerable in the Self-Help Case

Mikhail: "this space we're right over-redacting. So if we over-redact less, we already have success." The current state is 100% restriction for any document that might contain customer information. Even a system that incorrectly redacts 30% of content is a massive improvement over suppressing the entire document. The direction of failure matters -- over-redacting is safe, under-redacting is dangerous.

---

## The Feedback Loop Concept

### The Architecture

Mikhail describes a feedback loop that connects the ask-for-help/escalation flow back to the self-help search:

"There is the feedback loop, because we want to actually drive down the usage of these systems by doing what? Once the problem statement and the answer is identified, we feed this always back so next time people come in, they self-help and they don't have to ask the question."

### The Blocking Problem

This feedback loop is currently broken because of the IP risk in the escalation data. Mikhail: "until we have confidence, we can't fool and build this feedback loop and take unstructured data that we know is restricted, or potentially could be restricted, and feed it into the general training area."

The chain of dependency:
1. Escalation tickets contain unstructured data with potential customer IP
2. That data cannot be fed into the general knowledge base without redaction
3. Without feeding it back, the self-help layer stays thin
4. With a thin self-help layer, more people escalate
5. More escalations mean more cost, slower resolution, and more IP exposure risk

### The ROI Framing

Brad frames the business case explicitly in terms of driving volume from expensive escalation toward cheap self-help:

"When you're over here [escalation], this is very very costly... So the goal is to drive this down and drive this up [self-help]. Even ask questions, so theoretically, right, you will never get here [escalation]. The goal is to get here [self-help] and drive it and drive this down, drive that up because we want to -- again, it's productivity, but it's cost, it's customer cost, it's other things."

Pat (BayOne) adds the predictive analytics angle: "that's actually the ROI on the ML, AI, all of that is predictive analysis. Because once the root cause analysis of, let's say, 10, 100,000, the data points come in, then it predicts it in the very first layer itself."

### The Virtuous Cycle

The implied architecture is:
1. Solve detection in the ask-for-help flow (real-time, low false positive)
2. Solve redaction in the self-help/search flow (batch, heavy-handed)
3. Use redacted escalation data to feed back into the self-help knowledge base
4. As self-help improves, escalation volume drops
5. Lower escalation volume means lower cost, faster resolution, and less IP exposure

Mikhail makes this chain explicit: "heavy-handed detection and redaction so we can safely feed this into the general with the ultimate goal of dragging this [escalation volume] down. And the only way we can do it is with this feedback flow."

---

## What Has Been Tried

### Models Tested

Mikhail names three approaches they tested:
1. **Transformers model** (unspecified which one)
2. **SpaCy** (Named Entity Recognition library)
3. **Azure AI model** (cloud-based, likely Azure Cognitive Services or Azure AI Language)

All were trained/fine-tuned on Lam's data via an MLOps pipeline on Azure cloud.

### Results

- False positive rate: ~20% per ticket with initial models
- After fine-tuning: improved to 17%, at which point the effort was paused
- Colin's assessment: 80% accuracy is equivalent to out-of-the-box, untuned model performance; the fine-tuning effectively did nothing meaningful

### Rule-Based Approaches

They also started exploring rule-based models but hit accuracy problems due to the diversity of unstructured data entry. Mikhail's example: "something like a fab could be spelled many different ways, right? So there were ones, they're the accuracy basically created because the data is unstructured. Some people put a Micro 11, some put F11, some put FAB space 11, FAB dash 11."

The maintenance burden was also a concern: "we can actually put all these permutations in a rule-based models, but now we're policing this non-stop every day as new things come up."

### Labeling Effort

They investigated a formal data labeling approach: "it was over a thousand man hours just to get the labeling up and then continuous maintenance, so that was fairly expensive activity."

Mikhail does not dismiss it entirely: "doesn't mean we don't want to do it. All I'm saying is we looked at the labeling activity." He frames the potential ROI: "if we say, yeah, this case is where all the things sit, maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up."

### Why Generative AI Was Not Tried

Mikhail explicitly states: "We actually have not used generative AI to prove any use cases, not because of unstructured data, but because of unstructured output. If it does mean we can't, all I'm saying is we decided to go with something more definitive that can tell us redact, don't redact, rather than unstructured output that LLMs typically produce."

He acknowledges the capability: "I know it's prompt, you can make it structured, but there's limits to that as well."

---

## MVP Scope

### Two Fields Only

Brad and Mikhail are emphatic that the MVP focuses on just two data fields:

1. **Customer name** (e.g., Intel, Samsung, Micron)
2. **File name** (which can contain customer-identifying information)

Brad: "we want to promote those couple of fields, right? Let's say customer name, file name. Sometimes those are just enough."

Mikhail reinforces the reasoning: "if you can't get those correct, and you can't redact or do whatever we're trying to do with those, you can't escape, right? We want to start small."

### The Incremental Philosophy

Brad articulates the approach clearly: "The message is we want to start small and prove incrementally that we can solve certain things." And: "we want these things that we can chunk them down, prove these things, and then kind of determine, because not everything may work."

Mikhail adds: "when we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes."

---

## The Current Mode of Operation: Over-Restriction

This is a central theme that underpins the entire business case. Key statements:

- **Brad:** "Our current mode of operation is we over restrict."
- **Mikhail:** "what we're doing, we're putting policies in place, which basically creates hard barriers. Because we're saying, OK, we don't know if this document contains IP. We're just going to, by default, assume that it does."
- **Mikhail on AI training data:** "This also limits what data we can train our AI agents on... if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."
- **Brad on the reality of policy violations:** "when we started this project, I'm like, how many tickets is gonna take me to find policy violation? Seven. Seven tickets, there was a confidential violation already."

The over-restriction creates a cascading effect:
1. Knowledge is siloed by customer
2. Self-help search returns limited results
3. Users escalate more frequently
4. Escalations are costly and slow
5. Resolved escalation knowledge cannot be fed back due to IP risk
6. The self-help layer remains thin (cycle repeats)

---

## Infrastructure and Platform Context

### Current State (Heterogeneous)

Mikhail describes the infrastructure bluntly: "Oh my God. This is like ever, like anything you can make up, is because again, these are not free systems. Some of it on-prem, some of it is on cloud, some of it is eventually gonna move to cloud. Some of it is LamGPT, so we still have Open[AI] and like the GPT models within Lam. Some of it is again cloud but both, so anything you can think of, most likely this is a hazard."

He emphasizes these are not isolated systems: "I'm not describing a single system or three systems. These are flows."

### Strategic Direction

Despite the current fragmentation:
- **Cloud-first going forward:** Mikhail: "we do want to focus on cloud first going forward. So that's our plan."
- **Microservice architecture (aspirational):** "we also want to focus on microservice architecture long term. Whether we do or not, let's say these solutions, that's a different thing, but that's our kind of aspirational goal."

### Colin's Observation on Unified Control Plane

Colin (BayOne) makes the case for a unified ingestion layer: "if you want to put your lasso around a lot of things at the org... overall, you don't want to keep things so fragmented because you're going to end up trying to play whack-a-mole with this."

He elaborates: "making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure. It's easier than you would think if you can have that common control plane."

Brad's response indicates openness: "we are open to any and all approaches by also understanding what are the trade offs."

---

## Technology Stance

Mikhail makes a deliberate statement about not being locked into AI: "I know AI is a very sexy word, but it's also a meaningless word. And not married to any specific AI technologies, LLM, machine learning, or anything like that, it doesn't have to be an AI."

He then qualifies: "Preference on AI? Sure, because your kind of ceiling goes up with AI, what you can do afterwards, because other solutions are very important solutions."

Brad reinforces: "anything and everything... is on the table. We think and we believe that we can... pilot, POC, whatever fancy word you want to use, right? And prove that that is the right approach."

---

## Existing Access Control and Identity

### What Exists Today

- Users are identified by **work center** and **role**
- The escalation tool has access controls: tickets are visible only to users associated with the same customer (e.g., Micron employees can see Micron tickets, Samsung employees cannot)
- Users can manually **restrict entire tickets or specific attachments**
- Some identity attributes exist (employee vs. contractor vs. Licensed Service Provider; trade-restricted employees have flags and different colored badges)
- Embargo country restrictions are enforced

### What Does Not Exist

- Enterprise-wide Identity Access Management (IAM) -- a program has been underway for ~2 years but is "not super robust" yet
- Field-level restriction within tickets (users can restrict the whole ticket or attachments, "but not by all the different entry fields")
- Automated content-level detection/redaction within documents

### Mikhail's Position on IAM as a Separate Use Case

When Colin probes on user identity and role-based access as part of the solution, Mikhail explicitly cautions against scope creep: "I want to make sure we're not introducing noise in our business case... what we're describing is actually a completely different use case that I didn't present, which is, yeah, when it's restricted, how do you solve that? I don't know if we need to focus on that."

He draws a clear boundary: the two business cases he presented are about (1) scrubbing content so it can enter the general knowledge base, and (2) detecting potential violations at entry points. Access control for who sees what is a third, separate concern.

---

## Open Questions and Unresolved Points

1. **Which specific systems/platforms to target first for the MVP?** Colin asks directly: "From your perspective, let's talk like high value targets for this." Mikhail begins to answer ("Two things. Number one, one of the things we wanted to...") but the transcript appears to cut off before the answer is complete.

2. **Structured vs. unstructured data scope:** Colin asks whether machine learning on structured/numeric data (formulations, process variables) is a current concern. Mikhail redirects to unstructured as the initial focus: "Our MVP, customer name, companies... I'm going to say unstructured is probably the initial." This leaves structured data as a future consideration.

3. **The 1,000+ hours labeling effort:** Mikhail frames it as expensive but not ruled out. The question of whether to invest in labeling remains open, contingent on proving the value of the overall approach: "maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up."

4. **OCR and image-based documents:** Brad raises that redaction within images (OCR-extracted text in pictures, micrographs) is a qualitatively different problem than text redaction. The approach there may be to suppress the entire document rather than attempt in-image redaction. No resolution reached.

5. **Data lake / unified repository:** Colin asks about a single data lake. Mikhail confirms there is not one today: "there is not one, you could say data lake or something like that. So there doesn't mean that that's not in the future." The fragmentation across six-plus search systems and multiple platforms is a known constraint.

6. **Copilot / LamGPT implications:** Mikhail mentions both Copilot (using GPT models) and LamGPT as part of the ecosystem. The implications for those tools -- which also consume potentially restricted data -- are not explored in detail.

7. **The "big brother" framing for detection:** Mikhail uses the phrase "it's more about the big brother approach" for the ask-for-help detection use case. The political sensitivity of monitoring employee inputs is acknowledged but not deeply discussed.

8. **Rule-based model maintenance:** The permutation problem for fab names (F11, FAB 11, FAB-11, Micro 11, etc.) is identified but no resolution is proposed. This is implicitly a challenge for any approach.

---

## Key Quotes Index

**On the two business cases being separate:**
> "When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes." -- Mikhail

**On detection vs. redaction:**
> "In both cases, in this case, in this case, it's detection. It's just one is not performance focused. One is more accuracy focused. The other one is good enough, less false positive, performance focus." -- Mikhail

**On false positive sensitivity:**
> "This particular space is super sensitive to false positives. If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it." -- Mikhail

**On over-restriction as the baseline:**
> "Our current mode of operation is we over restrict." -- Brad
> "If we over-redact less, we already have success." -- Mikhail

**On the feedback loop:**
> "Until we have confidence, we can't build this feedback loop and take unstructured data that we know is restricted, or potentially could be restricted, and feed it into the general training area." -- Mikhail

**On performance requirements:**
> "This has to run within UI, whatever is UI standards, two to five seconds max." -- Mikhail (on the ask-for-help detection use case)
> "This could run an hour." -- Mikhail (on the self-help redaction use case)

**On the target false positive rate:**
> "We needed this number to be way below 1% end state." -- Mikhail

**On what was tried:**
> "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it." -- Mikhail

**On Colin's assessment of the 20% baseline:**
> "When I heard 20%... that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything." -- Colin

**On technology openness:**
> "I know AI is a very sexy word, but it's also a meaningless word. And not married to any specific AI technologies." -- Mikhail

**On the speed of policy violations surfacing:**
> "When we started this project, I'm like, how many tickets is gonna take me to find policy violation? Seven. Seven tickets, there was a confidential violation already." -- Brad

**On why Gen AI was not tested:**
> "We decided to go with something more definitive that can tell us redact, don't redact, rather than unstructured output that LLMs typically produce." -- Mikhail
