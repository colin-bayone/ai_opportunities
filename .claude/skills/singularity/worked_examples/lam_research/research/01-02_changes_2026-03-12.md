# Bridge Document: 01 -> 02 (Call Prep to Meeting)

**Set 01:** Call Prep (pre-meeting assumptions and strategy)
**Set 02:** Meeting Transcript (what actually happened on 2026-03-12)

---

This document captures what changed between BayOne's pre-call preparation and what was actually said and learned during the discovery call. It tracks which hypotheses were validated, invalidated, or remain open.

---

## Hypotheses: Validated, Invalidated, or Open

### Hypothesis 1: "Failing guardrails" likely means Purview DLP, not Sentinel
**Status: UNRESOLVED / REFRAMED**

The call prep assumed Lam might be confusing Sentinel (SIEM) with Purview (DLP). In the actual meeting, neither Sentinel nor Purview was mentioned by the Lam team. The problem was framed entirely differently: they described trying ML models (Transformers, SpaCy, Azure AI model) for detection/redaction and getting 20% false positive rates. When Colin asked about Azure AI Foundry and Purview, Mikhail said "I don't know what that even means." The "failing guardrails" narrative from the prep turned out to be the wrong frame entirely -- this is about ML model accuracy on a custom NER/classification problem, not about misconfigured Microsoft tools.

### Hypothesis 2: Microsoft's OOTB Sensitive Information Types don't cover semiconductor IP
**Status: VALIDATED (implicitly)**

The Lam team never mentioned SITs, Purview, or any Microsoft content detection tools. Their entire effort was focused on training their own models. The fact that they went straight to custom ML (not Microsoft's built-in detection) confirms that OOTB patterns were never considered adequate for their domain-specific IP (customer names, fab identifiers, process parameters).

### Hypothesis 3: Custom SIT configuration is non-trivial and likely not fully implemented
**Status: SUPERSEDED**

This hypothesis assumed Lam was trying to use Microsoft's tooling and struggling. In reality, they bypassed Microsoft's content detection entirely and built their own ML pipeline. The hypothesis was asking the wrong question -- it's not about SIT configuration, it's about custom model training for domain-specific entities.

### Hypothesis 4: Shadow AI may be a bigger factor than admitted
**Status: OPEN / NOT DISCUSSED**

Shadow AI was not meaningfully discussed in the meeting. Brad and Mikhail focused entirely on their two use cases (search redaction, entry-point detection). The shadow AI concern from the call prep -- that banning all AI drives usage underground -- was never raised or explored. This remains an open question for future conversation, but it was explicitly not part of what Lam wanted to discuss.

---

## What We Got Wrong (or Didn't Anticipate)

### 1. The problem framing was different than expected
The call prep framed this as a "guardrails failing" problem -- implying misconfigured enterprise tools. The meeting revealed it's a **custom NER/classification problem**: how to detect customer-identifiable information in unstructured text with a false positive rate below 1%, when all ML approaches tried so far produce ~20%.

### 2. Two distinct use cases, not one
The call prep treated the problem as a single "detection and redaction" challenge. Mikhail explicitly separated it into two business cases with different requirements:
- **Self-help search** (batch redaction, accuracy-focused, over-redacting OK)
- **Escalation entry** (real-time detection, performance-sensitive, false positives unacceptable)

These are "separate swim lanes" per Mikhail.

### 3. They've tried more than expected
The prep suggested Lam might not have fully implemented custom detection. In reality, they've tried three ML models, set up MLOps on Azure, attempted rule-based approaches, and evaluated a 1,000+ hour labeling exercise. They are further along than the prep assumed -- they've hit real technical walls, not configuration gaps.

### 4. Generative AI was deliberately avoided
The prep didn't anticipate that Lam would have a philosophical objection to LLMs for this use case. Mikhail explicitly stated they chose ML over generative AI because they want deterministic "redact/don't redact" binary output, not unstructured LLM output. This shapes what BayOne can propose.

### 5. The infrastructure is far more fragmented than assumed
The prep mentioned "Azure stack: AI Foundry + Microsoft Sentinel." The reality is dramatically more complex: on-prem, cloud, LamGPT, Copilot, cloud bots, 6+ search systems, no unified data lake, and "anything you can think of" per Mikhail. The call prep was far too optimistic about infrastructure coherence.

### 6. Brad's "we've heard it before" posture
The prep suggested Brad was a structured, organized contact. The meeting revealed he is also deeply skeptical of vendors who jump to solutions. He explicitly set a gate: BayOne must demonstrate problem understanding ("repeat back") before any solution discussion is permitted. This was the defining dynamic of the meeting and was not anticipated in the prep.

---

## What We Got Right

### 1. IP protection is existential
The call prep correctly identified that cross-customer data contamination is catastrophic for Lam. The meeting confirmed this in detail: customer segmentation is enforced at the ticket level, employees are physically identified by colored badges based on trade restriction status, and violations are found immediately when you look (7th ticket).

### 2. Lam is security-sophisticated
The CISO quote in the prep about zero-trust was validated by the meeting's operational details: IAM program, TRI flags, embargo country restrictions, ASM for sensitive areas, and deliberate over-restriction as the default philosophy.

### 3. The spelling variation problem is real
The prep mentioned "Fab11, F11, fab-11, FAP space 11" as examples. The meeting confirmed this exact problem and added "Micro 11" to the list. This remains the core technical challenge for any detection approach.

### 4. Colin's experience is directly relevant
The Coherent Corp experience, ITAR/CMMC background, and AI governance at scale all resonated. Colin's best moment (the 20%/ChatGPT diagnosis) directly leveraged this experience.

### 5. Brad is the decision maker
The prep identified Brad as the gatekeeper. The meeting confirmed he owns the full vertical: business case, product definition, ideation, and execution.

---

## New Information Not in the Prep

### People
- **Christian** exists (part of Brad's team, owns a slide)
- **Monica** exists (part of the broader team)
- **Daniel** confirmed as the technical lead, explicitly paired with Mikhail (Daniel = program/technical, Mikhail = product)
- **Mikhail** is far more central than the prep suggested -- he ran the meeting's substance, not just "likely to present"

### Technical
- **LamGPT** exists (GPT models hosted within Lam)
- **Teams meetings** are auto-transcribed and attached to tickets -- a significant unstructured data entry point
- **ASM** (Access Security Manager) governs access to some areas but is not enterprise-wide
- **Employee taxonomy** is more detailed than expected: blue badge, contractors, LSPs, TRI, embargo country
- **MLOps pipeline** exists on Azure cloud and is functional
- **The 20%->17% fine-tuning result** is a specific data point we didn't have

### Business
- **Brad will not write user stories** -- his team handles that, changing the engagement model
- **Previous "pod" working model** was a one-time pilot, not standard going forward
- **Evolutionary, not revolutionary** is an explicit requirement
- **Rapid prototyping** is demanded -- "we don't want these things to take months and years"
- **The ROI argument** centers on the feedback loop: solve escalations -> feed answers back -> reduce future escalations
- **The transcript cuts off** mid-answer on the "high value targets" question -- critical information is missing

### Dynamics
- **Brad redirects Colin directly** ("Is that clear, Colin?") -- a managerial move not anticipated
- **Mikhail is a scope guardian** -- he actively protects the two business cases from scope creep
- **"We've heard it before"** is the central trust dynamic -- BayOne must pass the "repeat back" test

---

## Questions Answered from the Prep's Question Bank

| Prep Question | Answered? | What We Learned |
|---|---|---|
| Walk through a specific failure example | Partially | 20% false positive rate on ML models; 7th ticket had a violation |
| False negatives vs false positives? | Yes | False positives are the critical concern for detection; over-redaction OK for batch |
| How are you testing? | Partially | Against actual ticket data; no mention of red teaming tools |
| What does 20% error rate measure? | Yes | False positive rate per ticket across ML model testing |
| Which tools are failing? | Reframed | Not about tools failing -- about custom ML models not meeting thresholds |
| Content detection today? | Yes | Custom ML (Transformers, SpaCy, Azure AI) + over-restriction as fallback |
| Custom SITs configured? | N/A | They bypassed Microsoft's content detection entirely |
| Categories of content most concerning? | Yes | Customer names, fab identifiers, file names -- starting with just two fields |
| Examples of "sensitive"? | Yes | Fab11, F11, Micro 11, FAP-11, customer name in problem statements |
| Shadow AI visibility? | No | Not discussed |
| Who owns AI governance? | Partially | Brad owns the initiative; enterprise IAM is a separate 2-year program |
| What's been tried? | Yes | Three ML models, rule-based, labeling exercise evaluation |
| Timeline pressure? | No | Not discussed beyond "don't want months and years" |
| Success at 6/12 months? | No | Not discussed |
| Best format for response? | Partially | Follow-up meeting with broader team, approaches with trade-offs |
