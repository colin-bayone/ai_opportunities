# 02 - Meeting: What Was Tried (Deep Dive)

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on prior attempts

---

## 1. Overview of Prior Attempts

Lam Research has made multiple attempts to solve the detection and redaction problem using machine learning approaches. They have deliberately chosen NOT to try generative AI. All attempts to date have fallen short of acceptable thresholds, and the team has paused or abandoned each approach for specific, articulable reasons. The core takeaway: they have tried enough to know the problem is hard, but not so much that they are locked into any particular approach. They are explicitly open to new ideas.

---

## 2. ML Models Tried: Named Approaches and Results

### 2.1 Models Tried by Name

Mikhail lists the specific models they trained (noting he is not the technical person, but can represent to a degree):

> "We tried Transformers model, Spacey, and I don't remember the third. Oh, Azure AI model."

So the three named approaches are:
1. **Transformers model** (unspecified architecture beyond "Transformers")
2. **SpaCy** (the NLP library, likely used for NER-based detection)
3. **Azure AI model** (a model from Azure's AI services)

### 2.2 Training Approach

Mikhail describes the approach as follows:

> "We put MLOps in place, and we've tried training a few models."

And:

> "We've passed the training data to it. But because those models were trained with global data as well, not just our data, we were hitting the rate of false positives of around 20% per ticket."

Key details:
- They stood up MLOps infrastructure (on Azure cloud -- see Section 7 below)
- They passed their own training data to these models
- The models had been pre-trained on "global data" (i.e., general-purpose training corpora), and their domain-specific training data was applied on top
- The issue was not that the models missed detections entirely, but that they produced too many **false positives**

### 2.3 The 20% False Positive Rate

The central metric cited for the ML model attempts:

> "We were hitting the rate of false positives of around 20% per ticket. Meaning 20% of tickets ended up with 20% false positive rate."

This phrasing is somewhat ambiguous -- it could mean 20% of all tickets had at least one false positive, or that across all tickets the false positive rate was 20%. Regardless, the number was far above their threshold:

> "And we needed this number to be way below 1% end state, right?"

The gap between 20% and sub-1% is enormous. This is not a fine-tuning problem -- it is an order-of-magnitude gap.

### 2.4 Fine-Tuning Results: 20% Down to 17%

Fine-tuning was attempted and yielded marginal improvement:

> "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

So fine-tuning reduced the false positive rate by 3 percentage points (from 20% to 17%), which was insufficient to justify continued investment. Mikhail explicitly states this is why they paused.

### 2.5 Colin's Assessment of the 20% Figure

Colin (BayOne) provides a blunt external benchmark for the 20% result:

> "I'll be honest, when I heard 20%, you know... or 80% success rate, that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

This is a significant assessment: Colin is saying the trained models performed no better than a general-purpose LLM with zero customization. The implication is that the training/ fine-tuning effort did not meaningfully improve over baseline. Mikhail's response ("The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it.") confirms this -- the improvement was negligible.

---

## 3. Rule-Based Models: Started and Abandoned

### 3.1 What Was Tried

Mikhail describes a second approach:

> "We've started trying rule-based models, but we haven't gotten far."

This approach was started but not completed. The reason: the spelling variation problem.

### 3.2 The Spelling Variation Problem (Exhaustive Examples)

The core failure mode for rule-based approaches is the inconsistency in how people refer to the same entity. Mikhail provides specific examples for how a single fab (Fab 11) can be spelled:

> "Something like a fab could be spelled many different ways, right? So there were ones... Some people put a Micro 11, some put F11, some put FAP space 11, FAP dash 11."

The specific variations cited:
- **Fab11** (or Fab 11) -- the standard name
- **Micro 11** (an abbreviation or alternate name, likely referencing "Micron Fab 11")
- **F11** -- abbreviated
- **FAP space 11** (i.e., "FAP 11") -- an alternate abbreviation with a space
- **FAP dash 11** (i.e., "FAP-11") -- the same abbreviation with a hyphen

Mikhail then acknowledges the theoretical solution and its impracticality:

> "Yes, we know that we can actually put all these permutations in a rule-based models, but now we're policing this non-stop every day as new things come up and so forth."

So the problem is twofold:
1. **Combinatorial explosion** -- the number of permutations for even a single entity is large, and this multiplies across all customer names, fab names, tool names, etc.
2. **Ongoing maintenance burden** -- new variations appear continuously as new employees, new sites, new customers, and new shorthand emerge. The rules would need constant updating, making it an unsustainable operational burden.

### 3.3 Rule-Based Assessment Summary

Mikhail's summary of the rule-based approach:

> "So those were the two things we tried. So in one case, rule-based models would be good enough and maybe fast enough. But the accuracy was fairly low due to different spellings and so forth."

He acknowledges rule-based would be "fast enough" (performance is not the issue) and "good enough" in concept, but the accuracy was "fairly low" specifically because unstructured data from humans introduces too much spelling variation.

---

## 4. The Labeling Exercise: 1,000+ Hours, Paused

### 4.1 What the Labeling Exercise Was

The labeling exercise was an effort to annotate their unstructured data with metadata/ labels that could be used to train ML models or structure the data for detection/ redaction. This came up in the context of the broader question about structuring unstructured data:

> "And this is one of the things we looked at for example if it were to use ML models what it would take us to label go through labeling exercise it was over a thousand man hours just to get the labeling up and then continuous maintenance so that was fairly expensive activity."

### 4.2 Scale and Cost

- **Estimated effort:** Over 1,000 man-hours for the initial labeling pass
- **Ongoing cost:** "Continuous maintenance" required on top of the initial effort
- **Assessment:** "Fairly expensive activity"

### 4.3 Why It Was Paused (Not Abandoned)

Mikhail is careful to distinguish between pausing and abandoning:

> "Doesn't mean we don't want to do it all I'm saying is with looked at the labeling activity to do exactly what you're saying, but that's one of the reasons we're kind of limited to fields to see if we can prove out."

The logic: they could not justify 1,000+ hours upfront without first proving the concept works at a smaller scale. So they narrowed scope to just two data fields (customer name and file name, per Brad's earlier framing) to see if they could get those right first.

> "And if we say, yeah, this case is where all the things sit, maybe a thousand hours is just peanuts compared to the productivity gains we could gain by opening this up. So that's a possibility."

This is important: they have NOT ruled out the labeling exercise. If the ROI justification is strong enough (i.e., if opening up restricted knowledge delivers massive productivity gains), a thousand hours could be justified. But they need proof of concept first.

### 4.4 The Maintenance Burden

The maintenance burden is explicitly cited as a separate concern from the initial cost:

> "It was over a thousand man hours just to get the labeling up and then continuous maintenance so that was fairly expensive activity."

This mirrors the rule-based problem: even if you do the initial work, maintaining it is an ongoing operational cost. New data enters the system constantly (tickets, procedures, transcripts), and each would need labeling to keep the system current.

---

## 5. Why Generative AI Has NOT Been Tried

### 5.1 Deliberate Decision, Not Oversight

Mikhail explicitly states this was a conscious choice:

> "One thing I don't want us to limit is to just LLMs and generative AI. So for example, I am jumping a little bit ahead. Some of the things we've actually tested was more with machine learning rather than generative AI. We actually have not used generative AI to prove any use cases."

### 5.2 The Reasoning: Unstructured Output

The specific reason for avoiding generative AI:

> "Not because of unstructured data, but because of unstructured output. If it does mean we can't, all I'm saying is we decided to go with something more definitive that can tell us redact, don't redact. Rather than at a structured output that LLMs typically produce. I know it's prompt, you can make it structured, but there's limits to that as well."

Key reasoning unpacked:
- They wanted **deterministic, binary output**: "redact" or "don't redact"
- LLMs produce **unstructured/ probabilistic output** by nature
- They acknowledge that prompt engineering can make LLM output more structured, but believe "there's limits to that as well"
- They chose ML specifically because it can deliver more definitive classification decisions

### 5.3 Broader Guardrail Concerns

A separate but related concern about generative AI was raised:

> "Since last like 12-24 months, so much has happened in the generative AI field. The guardrails are still not tested for production or tested in the field. So that risk is already even Anthropic, and you name anyone. Even Google for that matter is not able to ensure they are still trying to do it as we speak today."

This reflects a broader industry skepticism: even the major AI providers (Anthropic, Google explicitly named) have not fully solved the guardrails problem. For a use case this sensitive (customer IP, cross-customer contamination), that is a real concern.

### 5.4 Not Ruling It Out

Despite the above, they are not dogmatically opposed:

> "I know AI is a very sexy word, but it's also a meaningless word... and not married to any specific AI technologies, LLM, machine learning, or anything like that, it doesn't have to be an AI."

And Brad adds:

> "We're open to any and all approaches by also understanding what are the trade offs."

The door is open, but they need to see how it addresses the false positive and determinism concerns.

---

## 6. What They Would Be Open To vs. What They've Ruled Out

### 6.1 Explicitly Open To

- **Any and all approaches**, per Brad: "We're open to any and everything as long as we understand kind of what those trade-offs are and how they get us to the outcomes that we're looking for."
- **Non-AI solutions**: "It doesn't have to be an AI. Preference on AI? Sure, because your kind of ceiling goes up with AI... But I just want to make sure that that message is clear, right? It doesn't have to be."
- **Hybrid approaches**: Brad mentions "you use AI with this other thing and that gets you what you need"
- **Evolutionary progress**: "We're not expecting to be revolutionary and right out of it. Evolutionary is absolutely fine."
- **Rapid prototyping**: "We want to get to some rapid prototyping. I mean, we don't want these things to take months and years, right? We want these things that we can chunk them down, prove these things."
- **The labeling exercise** if ROI justifies it

### 6.2 Not Explicitly Ruled Out

Nothing was explicitly ruled out. Even generative AI, which they chose not to try initially, is not forbidden -- they just need to understand the trade-offs.

### 6.3 Strong Preferences / Constraints

- **False positive rate must be "way below 1%"** for the detection use case
- **Real-time performance** required for the detection/ notification use case: "two to five seconds max" in the UI
- **Over-redaction is acceptable** for the bulk/ search use case (better to over-redact than under-redact)
- **False positives are the critical failure mode** for the detection/ notification use case (people will stop trusting the system)

---

## 7. MLOps Infrastructure

### 7.1 What Exists

Mikhail confirms MLOps infrastructure is in place:

> "We put MLOps in place, and we've tried training a few models."

### 7.2 Platform

The MLOps is on Azure cloud:

> "It was a cloud-based MLOps put on Azure cloud, but the model was, like I said, Azure AI model, SpaCy and Transformers."

When Colin asks about the specific Azure services (Azure Purview, Azure AI Foundry), Mikhail cannot answer:

> "You're not talking to a technical audience here."

And:

> "Again, I don't know what that even means. So again, it was a cloud-based MLOps put on Azure cloud."

### 7.3 Broader Infrastructure Landscape

The broader infrastructure is highly heterogeneous:

> "Oh my God. This is like ever like anything you can make up is because again, these are not free systems... Some of it on prem, some of it is on cloud, some of it is eventually gonna move to cloud, some of it is Lam GPT so we still have open and like the GPT models within Lam, some of it is again cloud... anything you can think of most likely this is a hazard."

But there is a stated aspiration:

> "We do want to focus on cloud first going forward. So that's our plan. And again, I don't want to dive into technical, but we also want to focus on microservice architecture long term."

---

## 8. Detection vs. Redaction: The Distinction

Mikhail draws a very clear line between detection and redaction as separate use cases with different requirements.

### 8.1 Detection (Real-Time, Entry Point)

- **Purpose:** Notify users in real time that they may be entering customer-confidential information
- **Where:** At the point of data entry (e.g., typing a ticket, entering a problem statement)
- **Performance requirement:** Must run within UI response times, "two to five seconds max"
- **Accuracy priority:** Low false positive rate is critical; false negatives are less dangerous
- **Action taken:** Notification only -- "We're not doing redaction. We're just doing detection and we're stopping there. We're letting users know that they might have issues and that we stop with the detection."
- **Does not need to be perfect:** "Does it have to be perfect in this case? No, because again, we have policies in these applications."
- **Analogy:** "Big brother approach" -- deterrence and awareness, not enforcement

> "How fast you can get to detect and notify the user that they would have possible violation of customer confidential information."

### 8.2 Redaction (Batch, Post-Entry)

- **Purpose:** Strip customer-identifiable information from data that has already been entered so it can be shared more broadly
- **Where:** After data has entered the system, on stored documents/ tickets/ transcripts
- **Performance requirement:** Can take longer -- "this could run an hour" (vs. the 2-5 second requirement for detection)
- **Accuracy priority:** Over-redaction is acceptable; under-redaction is dangerous
- **Action taken:** Actual removal or masking of information
- **Multiple techniques:** Could include text redaction, OCR-based detection in images, document-level restriction, or substitution

> "A more heavy-handed reduction still happening once the data enters the flow to truly make sure things are not violating."

### 8.3 Mikhail's Framing

> "What I've presented today is two separate business use cases. When we say small piece and MVP, I would expect them not being jumbled together, but they could be separate swim lanes."

---

## 9. Testing and Datasets

### 9.1 What Data Was Used for Testing

The testing was done against their own ticket data (the escalation flow). This is clear from:

> "We were hitting the rate of false positives of around 20% per ticket."

The unit of measurement is "per ticket," indicating the models were run against their actual support/ escalation tickets.

### 9.2 How Quickly Violations Were Found in Real Data

Brad provides a striking anecdote about the prevalence of violations in actual ticket data:

> "When we started this project, I'm like, how many tickets is gonna take me to find policy violation? Seven. Seven's ticket, there was a... already concept-renade."

This means in the first seven tickets examined, they found a policy violation. This establishes that the problem is pervasive -- not theoretical -- and that any solution needs to handle a high volume of actual violations.

### 9.3 Dataset Characteristics

- **Unstructured data:** Primarily text entered by humans -- problem statements, responses, procedures, meeting transcripts
- **Entry methods:** Manual typing (phone/ field, often informal), uploaded documents, auto-transcribed Microsoft Teams meetings
- **Language quality:** Variable -- the spelling variation problem (Section 3.2) demonstrates that field technicians use shorthand, abbreviations, and inconsistent naming

---

## 10. The Current State of Operations (Over-Restriction)

While not a "tried and failed" approach per se, over-restriction is the current fallback that exists because nothing else has worked:

> "Our current mode of operation is we over restrict... And by doing that, we know that we're limiting because we're limiting the knowledge, the information."

Brad describes the cost:

> "If document three has the path to solution, but you only can look at Intel documents and this sits in a Samsung space, you're not going to see that."

And it limits what data can be used for AI training:

> "This also limits to what data we can train our AI agents on, right? Or our AI mobs, not agents, but our models on because, hey, if this source is restricted and we cannot control whether this data could be trained for general public, we're not going to pass the source to the model to train them because we don't want to assume that additional risk."

Over-restriction is acknowledged as the safe but costly default. Every prior attempt to replace it with something smarter has failed to meet the accuracy bar.

---

## 11. Colin's Key Assessment: The Common Control Plane

Colin provides a structural recommendation based on his Coherent experience that reframes the problem:

> "There has to be commonality between these applications. The good thing with that is about 95% of a rack application is identical. The only thing that really changes is maybe some strategy for ingestion, maybe the end use case is a little bit different, but the actual architecture fundamentally is relatively the same."

And critically:

> "The whole problem is that whenever you make information known or available to AI, that's how information comes in. That ingestion part is so critical because even if information comes out, you shouldn't have to redact anything if this part actually worked. It's not possible. It can't create that from nothing."

His argument: if you get ingestion right (strip sensitive data before it enters the system), you don't need heavy downstream redaction. The more fragmented the ingestion landscape, the worse the problem gets over time. He advocates for a unified control plane across applications.

---

## 12. Summary: Attempt-by-Attempt Scorecard

| Approach | Status | Key Metric | Failure Mode |
|---|---|---|---|
| Transformers model | Paused | 20% false positive rate (reduced to 17% with fine-tuning) | False positives far above the sub-1% threshold; fine-tuning yielded only 3pp improvement |
| SpaCy | Paused | Same 20% rate (grouped with Transformers) | Same as above -- part of the same training exercise |
| Azure AI model | Paused | Same 20% rate (grouped with Transformers) | Same as above -- part of the same training exercise |
| Rule-based models | Abandoned early | Low accuracy due to spelling variations | Combinatorial explosion of entity name variations; unsustainable maintenance burden |
| Labeling exercise | Paused (not abandoned) | 1,000+ man-hours estimated | Cost and ongoing maintenance burden; could not justify without proof of concept first |
| Generative AI | Never tried | N/A | Deliberately avoided due to concerns about unstructured/ non-deterministic output |
| Over-restriction (current) | Active (default) | N/A | Known productivity loss; limits AI training data; limits cross-customer knowledge sharing |
