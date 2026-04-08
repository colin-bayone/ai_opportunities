# 02 - Meeting: What Was Tried (Deep Dive)

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on prior technical attempts and results

---

## 1. Overview of Prior Technical Attempts

Lam Research has made multiple attempts to solve the IP detection/redaction problem using machine learning approaches. Critically, they have **not** attempted any generative AI approaches. All work was done through MLOps infrastructure deployed on Azure cloud. The team tested three named models, attempted rule-based approaches, and explored a labeling exercise that was ultimately paused due to cost.

The overall trajectory: initial ML model training produced a 20% false positive rate per ticket, which fine-tuning reduced only to 17%. Rule-based models were attempted but abandoned due to the spelling variation problem in unstructured data. A 1,000+ hour labeling exercise was scoped but paused. The entire effort has stalled, which is why they are now seeking external help.

---

## 2. Models Tested

### 2.1 The Three Named Models

Mikhail identified the specific models that were trained and tested. When Colin asked "what specifically has been tried," Mikhail responded:

> "So first of all, we put MLOps in place, and we've tried training a few models. I can even name them. We tried Transformers model, SpaCy, and I don't remember the third. Oh, Azure AI model."

The three models tested were:
1. **Transformers** (likely a Hugging Face transformer-based NER model)
2. **SpaCy** (open-source NLP library, commonly used for Named Entity Recognition)
3. **Azure AI model** (likely Azure Cognitive Services or Azure AI Language entity recognition)

### 2.2 Infrastructure

Mikhail described the infrastructure as "cloud-based MLOps put on Azure cloud." When Colin pressed for specifics about Azure AI Foundry or Azure Purview, Mikhail was candid about the limits of his technical knowledge:

> "You're not talking to a technical audience here. But to an extent, I'm able to represent."

And later:

> "Again, I don't know what that even means. So again, it was a cloud-based MLOps put on Azure cloud, but the model was, like I said, Azure AI model, SpaCy and Transformers. That's as much as I can actually..."

**Note:** Mikhail is product leadership, not engineering. The technical team (Daniel and others) were not in this meeting. This is a significant gap -- the detailed technical decisions, hyperparameters, training data composition, and pipeline architecture are not represented in this conversation. Mikhail explicitly stated the follow-up meeting would bring in technical staff.

### 2.3 Training Data

Mikhail described that these models were "trained with global data as well, not just our data." This is a critical detail -- the models appear to have been general-purpose NER models, possibly pre-trained on public datasets and then fine-tuned on Lam's internal data. The "global data" phrasing suggests they did not train from scratch but used transfer learning or fine-tuning on top of publicly pre-trained model weights.

---

## 3. The 20% False Positive Rate

### 3.1 What 20% Means

Mikhail was specific about the metric:

> "We were hitting the rate of false positives of around 20% per ticket. Meaning 20% of tickets ended up with 20% false positive rate."

This means that for every ticket processed, approximately 20% of the entities flagged as confidential information were actually false positives -- not real violations.

### 3.2 Why 20% is Unacceptable

Mikhail was emphatic about why this rate kills the use case. He framed this in the context of the real-time detection use case (notifying users at entry time that they may be violating policy):

> "If every fifth thing I say, hey, you possibly have a violation, then you're like, no, I don't. People are just not going to trust it. And if you constantly give auditors notifications, say, a possible violation, they're also going to not trust your system. They're going to turn off these notifications."

Later, more directly:

> "In the way we wanted to do proactive notifications, in the way we want to prompt the user that they're violating policy, 20% is absolutely unacceptable number, right? We can't live with that."

### 3.3 The Target

Mikhail stated the end-state target:

> "We needed this number to be way below 1% end state."

So the gap is enormous: from 20% (or 17% after fine-tuning) down to below 1%. That is roughly a 17x improvement needed.

### 3.4 The Fine-Tuning Progression: 20% to 17%

The fine-tuning effort produced minimal improvement. This came out in the exchange between Colin and Mikhail:

Colin stated: "I'll be honest, when I heard 20% [...] that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

Mikhail confirmed: "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

Colin's follow-up: "Yes, yes. And which is industry standard right now."

**Analysis of this exchange:** Colin's assessment landed well. Mikhail did not push back -- he confirmed the 20% to 17% number and agreed that this is why they paused. Colin's framing ("out-of-the-box ChatGPT performance") positioned the current results as baseline, not as a failed attempt, which reframed the narrative from "we tried and failed" to "the approach was never going to get there." This is a strategically important moment in the call -- it establishes that the problem is the approach, not the execution.

---

## 4. Rule-Based Models: Attempted and Abandoned

### 4.1 What Was Tried

Mikhail described the rule-based attempt:

> "We've started trying rule-based models, but we haven't gotten far because, again, something like a fab could be spelled many different ways, right?"

### 4.2 The Spelling Variations Problem

This is the core reason rule-based approaches were abandoned. Mikhail gave concrete examples:

> "Some people put a Micro 11, some put F11, some put Fab space 11, Fab dash 11."

He acknowledged the theoretical possibility but dismissed it as impractical:

> "Yes, we know that we can actually put all these permutations in a rule-based models, but now we're policing this non-stop every day as new things come up and so forth."

### 4.3 Summary of Rule-Based Assessment

Mikhail's assessment of rule-based models:

> "So in one case, rule-based models would be good enough and maybe fast enough. But the accuracy was fairly low due to different spellings and so forth."

The rule-based approach was abandoned because:
- The unstructured nature of the data meant infinite spelling variations
- Maintaining the rules would be a continuous, open-ended policing effort
- Accuracy was too low given the variation in how users express the same entity
- The approach does not scale -- every new customer name, fab name, or tool name introduces new permutations

---

## 5. The Labeling Exercise

### 5.1 Scope

Mikhail described the labeling effort that was assessed (and appears paused):

> "This is one of the things we looked at, for example, if it were to use ML models what it would take us to label, go through labeling exercise, it was over a thousand man hours just to get the labeling up and then continuous maintenance."

### 5.2 Cost Assessment

Mikhail described it as "fairly expensive activity" but did not fully close the door:

> "Doesn't mean we don't want to do it. All I'm saying is we looked at the labeling activity [...] but that's one of the reasons we're kind of limited to fields to see if we can prove out."

### 5.3 Conditional Logic

Mikhail framed the labeling investment as conditional on proving the concept works at a smaller scale first:

> "And if we say, yeah, this case is where all the things sit, maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up. So that's a possibility."

### 5.4 The 1,000 Hours Comes Up Again Later

In the context of the escalation/ticket use case, Mikhail referenced the labeling effort again:

> "And again, as we run up against 1,000 plus hours of labeling effort..."

This was mentioned alongside the detection approach attempt, suggesting the labeling effort was evaluated for both the redaction and detection use cases and was paused for both.

**Open question:** Were any labels actually created, or was this purely an estimation exercise? The transcript says "we looked at" the labeling activity and it was "over a thousand man hours," which reads more like a scoping estimate than a partially completed effort. However, the phrase "we run up against" suggests they may have started and hit the wall. Unclear from this transcript alone.

---

## 6. Why Generative AI Was Not Tried

### 6.1 Mikhail's Explicit Statement

This is one of the most important disclosures in the transcript. Mikhail proactively addressed this before anyone asked:

> "So one thing I don't want us to limit is to just LLMs and generative AI. So for example, I am jumping a little bit ahead. Some of the things we've actually tested was more with machine learning rather than generative AI. We actually have not used generative AI to prove any use cases."

### 6.2 The Reason: Unstructured Output

Mikhail's rationale was specific -- it was about output determinism, not about data concerns:

> "Not because of unstructured data, but because of unstructured output. [...] We decided to go with something more definitive that can tell us redact, don't redact. Rather than [the] unstructured output that LLMs typically produce."

### 6.3 Mikhail's Acknowledgment of the Counterargument

He acknowledged that prompt engineering can produce structured output but expressed skepticism:

> "I know it's prompt, you can make it structured, but there's limits to that as well."

### 6.4 Broader Skepticism of GenAI Guardrails

Mikhail also expressed a broader concern about the maturity of GenAI guardrails for production use:

> "Since last like 12-24 months, so much has happened in the generative AI field. The guardrails are still not tested for production or tested in the field. So that risk is already even Anthropic, and you name anyone. Even Google for that matter is not able to ensure they are still trying to do it as we speak today."

### 6.5 Analysis

Mikhail's reasoning has two layers:
1. **Technical concern:** LLMs produce probabilistic, unstructured output. For a binary redact/don't-redact decision, he wanted something deterministic.
2. **Industry trust concern:** He does not believe GenAI providers (including Anthropic and Google by name) have solved the guardrails problem for production use cases.

This is significant because it means Lam has not explored the most capable current approaches (LLM-based NER with structured output, few-shot prompting for entity extraction, RAG-based approaches for contextual understanding). The gap between what they tried (classical ML NER) and what is available (modern LLM-based approaches with structured output guarantees) is large.

---

## 7. Colin's "Out-of-the-Box ChatGPT" Assessment

### 7.1 The Statement

Colin's assessment of the 20% false positive rate:

> "I'll be honest, when I heard 20% [...] or 80% success rate, that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

### 7.2 How It Landed

Mikhail responded immediately with the precise numbers, confirming rather than defending:

> "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

Colin then framed 17% as expected: "Yes, yes. And which is industry standard right now."

Mikhail did not push back or express frustration. Instead, he redirected to why it matters:

> "Yeah, but for example, in the way we wanted to do proactive notifications, in the way we want to prompt the user that they're violating policy, 20% is absolutely unacceptable number, right? We can't live with that."

### 7.3 Strategic Significance

This exchange accomplished several things:
- **Validated Mikhail's decision to pause:** The fine-tuning was not going to get them where they needed to go.
- **Established Colin's technical credibility:** He immediately benchmarked their result against a known baseline (out-of-the-box ChatGPT).
- **Reframed the problem:** The issue was not bad execution but a fundamentally limited approach.
- **Opened the door for new approaches:** If the current results are just baseline performance, then modern techniques should be able to do dramatically better.

---

## 8. The Two Approaches Tried for the Escalation/Ticket Use Case

Mikhail described two specific things tried in the "ask for help and escalate" workflow:

> "Now, here we've tried two different things. One, we tried [the] redaction approach, meaning the same kind of bulk strategy on the machine learning side where you don't [protect] at the entry. But once it's entered, we have a bulk of data sitting there, it actually removes that, right?"

And:

> "So in here, we've tried two things. We've tried the redaction approach. And again, as we run up against 1,000 plus hours of labeling effort, and we've tried the detection approach."

The redaction approach: apply ML-based entity recognition to bulk data after entry, redact identified entities.
The detection approach: real-time notification to users at entry time that they may be violating policy.

Both hit the same walls: the redaction approach ran into the labeling cost barrier, and the detection approach ran into the 20% false positive rate.

---

## 9. Brad's Framing of the Current State

Brad (who owns the entire product/engineering/business organization) provided important framing around over-restriction as the current workaround:

> "Well, is it worth saying that our current mode of operation is we over restrict? [...] True, but we're also knowing that we're limiting the productivity, the capability, because we don't share that much."

And Mikhail's supporting example:

> "When we started this project, I'm like, how many tickets is gonna take me to find [a] policy violation? Seven. Seven tickets, there was already [a confidential violation]."

This means the problem is not theoretical -- within the first seven tickets Mikhail reviewed, he found an actual policy violation. The over-restriction policy exists because the alternative (open access) immediately produces real violations.

---

## 10. Copilot / LamGPT Context

The transcript contains a brief but important note about Lam's existing AI tooling. When discussing infrastructure:

Mikhail: "Some of it is on-prem, some of it is on cloud, some of it is eventually gonna move to cloud, some of it is LamGPT so we still have OpenAI [...] GPT models within Lam."

Brad also referenced Copilot (transcribed as "compiler"):

> "From an AI perspective, in [Copilot], we're really talking OpenAI model, right? Because [Copilot] using GPT models, right?"

This establishes that Lam does have GPT/OpenAI models deployed internally (through Copilot and LamGPT), but these were not applied to the IP detection/redaction problem. The GenAI tools they already have in-house were not part of the attempts described.

---

## 11. What Was NOT Tried (Explicit and Implicit Gaps)

Based on the transcript, the following approaches were **not** attempted:

| Approach | Status | Evidence |
|----------|--------|----------|
| Generative AI / LLM-based NER | Explicitly not tried | Mikhail: "We actually have not used generative AI to prove any use cases" |
| Few-shot or zero-shot prompting | Not mentioned | No evidence of prompt-based approaches |
| RAG (Retrieval Augmented Generation) | Not mentioned | No evidence |
| Azure AI Foundry | Unknown to Mikhail | "I don't know what that even means" |
| Azure Purview (data governance) | Not confirmed | Colin asked; no clear answer |
| Hybrid approach (ML + rules + LLM) | Not mentioned | Each approach tried in isolation |
| Pre-trained NER with domain adaptation | Unclear | The "fine-tuning" may have been this, but results suggest minimal domain adaptation |
| Custom training from scratch | Unlikely | "Models were trained with global data as well, not just our data" suggests pre-trained models |

---

## 12. Open Questions and Unresolved Points

1. **Who did the technical work?** Mikhail referenced that the prior pilot was done "for the pod working because that was a pilot." Was this Capgemini? An internal team? Another vendor? The transcript does not clarify who executed the MLOps/model training work.

2. **What was the training data composition?** Mikhail said models were "trained with global data as well, not just our data." What was the ratio? How much Lam-specific data was used? What entities were they training to detect?

3. **Were labels actually created or just estimated?** The 1,000+ hour figure could be an estimate or a partially completed effort.

4. **What does "per ticket" mean precisely?** When Mikhail says "20% false positive rate per ticket," does he mean 20% of flagged items per ticket are false positives, or that 20% of all tickets contain at least one false positive? The former is an entity-level metric; the latter is a ticket-level metric. The distinction matters for benchmarking.

5. **What two fields were they focusing on?** Brad mentioned "two attributes or two data fields" as the initial focus: "just really about two attributes or two data fields, right? Because if you can't get those correct, and you can't redact or do whatever we're trying to do with those, you can't escape." These appear to be customer name and fab/site name based on later discussion, but this was not explicitly confirmed.

6. **What happened to the Capgemini engagement?** The transcript references prior work that was described as "a pilot" and "not a standard mode of operation." Was Capgemini the vendor that did the initial MLOps/model training? This needs clarification in the technical follow-up.

7. **Timeline of attempts:** When did the ML model testing occur? When was the rule-based approach tried? When was the labeling exercise scoped? The transcript does not establish a clear chronology beyond "we tried" and "we paused."

---

## 13. Summary: Progression of Technical Attempts

```
Rule-based models
  -> Attempted for entity detection
  -> Abandoned: spelling variations in unstructured data made accuracy too low
  -> Maintenance burden deemed unsustainable ("policing this non-stop every day")

ML Models (Transformers, SpaCy, Azure AI)
  -> Deployed via MLOps on Azure cloud
  -> Trained on global + Lam data
  -> Initial result: ~20% false positive rate per ticket
  -> Fine-tuning applied: reduced to ~17%
  -> 3 percentage point improvement deemed insufficient
  -> Paused

Labeling Exercise
  -> Scoped at 1,000+ man hours for initial labeling
  -> Continuous maintenance on top of that
  -> Deemed "fairly expensive"
  -> Paused pending proof of concept at smaller scale

Generative AI
  -> Explicitly NOT tried
  -> Reason: concern about unstructured/non-deterministic output
  -> Secondary reason: distrust of GenAI guardrails in production
  -> Despite having GPT models deployed internally (Copilot, LamGPT)

Current State
  -> All technical approaches paused
  -> Operating in over-restriction mode (restrict by default)
  -> Target: below 1% false positive rate
  -> Current best: 17% false positive rate
  -> Gap: ~17x improvement needed
  -> Seeking external perspective and new approaches
```
