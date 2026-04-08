# 05a - Discussion: Prior Work Technical Assessment

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-06
**Document Set:** 05a (Technical Decomposition Discussion, supplementary to Set 05)
**Pass:** Assessment of Lam's prior technical approach

---

## 1. Presidio as the Starting Framework

Mikhail stated the team started with Microsoft Presidio, evaluated 12 models through its framework, narrowed to 5, then to 3. Presidio is Microsoft's open-source PII detection and anonymization library. It ships with pre-built recognizers for standard PII types -- social security numbers, credit card numbers, phone numbers, email addresses -- and allows custom recognizers to be added. It is commonly the first thing teams reach for when searching Microsoft documentation for "how to detect sensitive information."

Presidio is designed for generic PII detection across standard entity types. It is not designed for domain-specific entity detection like semiconductor customer names, fab identifiers, or the kinds of spelling variations Lam deals with (Fab 11, F11, Micro 11, FAP-11). The pre-built recognizers would have contributed nothing to Lam's actual problem.

The selection criteria Mikhail described was "accuracy and performance," meaning they were comparing how each model performed out of the box or with minimal configuration against their text fields. This is a bake-off of pre-trained models against a problem none of them were trained for.

**Colin's assessment:** Presidio is a capable tool for its intended purpose: standard PII redaction across well-defined entity types. Lam's problem is not standard PII. It is custom domain-specific text classification for entities that exist only within their own operational context: customer names with dozens of spelling variations, fab identifiers with no standardized format, and site-specific references that have no external analog. Applying Presidio to this problem is a category error, and even extensive customization on top of it does not change the fundamental mismatch. The right approach is to build the detection capability for the actual problem, not to extend a generic PII tool beyond its design boundaries.

The model evaluation process further confirms the gap. Evaluating 12 models and narrowing to 3 based on out-of-the-box performance indicates the team was searching for a model that already understood their problem rather than building the detection capability themselves. That is a fundamentally different approach, and it explains why they reached a ceiling they could not move past regardless of which model combination they tried.

---

## 2. The Three Final Models: Hugging Face Flair, SpaCy, Azure AI

The team narrowed to three models, each from a completely different category:

- **Hugging Face Flair:** Transformer-based NER framework. Pre-trained on standard NER categories (person names, organizations, locations, dates). Semiconductor fab identifiers and customer name variations are not in its training vocabulary. Would need fine-tuning with labeled domain data to be useful, and they had no golden set to fine-tune with.
- **SpaCy:** NLP library with built-in NER pipelines. Fast and lightweight (explains the performance cut), but out-of-the-box entity recognition has no concept of domain-sensitive entities like "Fab 11" or "TSMC." Same dependency on labeled training data for custom entity types.
- **Azure AI:** Almost certainly Azure AI Language or Azure Cognitive Services entity recognition. Cloud-hosted NER, handles standard PII types (same family as Presidio), no domain-specific knowledge of semiconductor IP.

Mikhail himself recognized the pattern in the meeting: "So we just basically accidentally picked literally every single thing, one of each." None were selected because they were suited to the problem. They were selected because they performed least badly in a bake-off against a problem none of them were designed for.

**Colin's assessment:** Without a golden set, fine-tuning any of these models to learn Lam's domain-specific entities was not possible. The selection process was inverted: the team evaluated model performance before defining what the models needed to learn. The 21% false positive rate is the predictable outcome of running generic NER against domain-specific text with no domain-specific training data to guide it.

The broader signal is that the effort was purely exploratory. There was no attempt to construct ground truth, no anti-set, no structured approach to teaching the models what Lam's sensitive entities actually look like. Models were given raw input and evaluated on their unguided output. As exploration, that is a reasonable first step. As a strategy for solving the problem, it explains exactly why progress stalled.

The 18-month timeline underscores the gap in internal AI expertise. A year and a half with no meaningful advancement on the same problem is not a reflection of problem difficulty. The problem is well-defined and tractable. It is a reflection of the team not having the specialized knowledge to move past the exploratory phase into structured model development.

---

## 3. The Parallel Reconciliation Algorithm

All three models ran in parallel on the same input. Mikhail described a "reconciliation algorithm" that compared results and made the final determination. The false positive rate moved from 21% to 17% with this approach.

In practice, what Mikhail calls a reconciliation algorithm is almost certainly a confidence-based comparison: whichever model returns the highest confidence score wins, or a majority vote where at least two of three models must agree. The term "algorithm" overstates the sophistication of what is happening. This is basic output comparison, not a structured reconciliation methodology.

Colin described this on the call as a modified take on mixture of experts, which was diplomatically generous. The fundamental issue is that this approach assumes all three models have an equal probability of being correct. When the models are three completely different types (a transformer, an NLP library, and a cloud API) with different architectures, training data, strengths, and failure modes, a voting mechanism does not produce a reliable signal. Two models agreeing does not validate the answer. It means two models that lack understanding of the problem happened to converge on the same output.

The 21% to 17% improvement (4 percentage points) for the complexity of orchestrating three models and building a comparison layer is marginal. If the parallel approach were adding meaningful value, combining three independent signals should produce a substantially larger improvement. The modest gain indicates correlated errors: the models fail on the same inputs because they share the same fundamental limitation. None of them have any concept of what Lam's sensitive entities actually are. Correlated inputs produce correlated outputs regardless of how many models are running.

**Colin's assessment:** The approach reveals that the team was trying three different things to see which worked best, which is characteristic of a first AI initiative where no one on the team has done this type of work before. The parallel design was not informed by an understanding of how ensemble methods work or when they add value. It was exploratory trial and error dressed up as architecture.

On the call, this was handled gracefully. The mixture-of-experts framing gave Mikhail a technical explanation for why the approach produced limited results without making the team feel incompetent. In reality, the approach is nonsensical to anyone with experience in applied AI. Running three uninformed models in parallel and comparing their outputs does not compensate for the absence of domain-specific training data. The linear funnel approach (deterministic first, escalating to progressively more capable systems) addresses the problem structurally rather than hoping that model consensus equals accuracy.

---

## 4. On-Prem Kubernetes Deployment

Flair and SpaCy were deployed on-prem Kubernetes. Azure AI was the only cloud component. Mikhail said they "didn't even put them anywhere, like we use anything in a cloud" and deployed on-prem while evaluating. Legal and security teams were still working through NDAs and cloud service approvals at that time (18 months ago).

**Colin's assessment:** The decision to deploy on Kubernetes for a lightweight POC evaluation is itself a red flag. Kubernetes is an orchestration platform designed for scaling containerized workloads. You move to Kubernetes from Docker when you need scaling potential, load balancing, and production-grade container management. None of that applies to a small-scale model evaluation. Running a POC on Kubernetes is overcomplicating a simple task, and it suggests the team was leaning on infrastructure choices they were familiar with from other projects rather than choosing the right tool for the job.

The on-prem decision also reveals the absence of coherent technical leadership. It is not clear that the team understands the distinction between on-prem, cloud, and hybrid deployment in any structured way, or that they have thought through what the right deployment model is for different stages of a project.

The operational burden of hosting models on-prem Kubernetes is substantial: infrastructure management, scaling, patching, monitoring, and security all fall on a team that is already stretched and lacks AI-specific operations expertise. Azure AI Foundry eliminates this overhead entirely, which is why it was positioned as the recommended path.

There is also a compliance dimension that the team has not yet confronted. The current on-prem setup exists outside of enterprise IT governance. As long as the project is an internal experiment, that is manageable. The moment it becomes a production system processing customer-identifiable information at scale, the lack of enterprise compliance integration (Identity and Access Management, Role-Based Access Control, audit logging, data governance) becomes a serious liability. Azure AI Foundry addresses this by placing the infrastructure within the enterprise compliance perimeter from the start, which also brings IT into the fold as a stakeholder rather than an adversary. The alternative is building a production system that eventually gets flagged by IT or security for operating outside of governance, which would set the project back significantly.

---

## 5. No Golden Set / No Ground Truth

Mikhail was direct: "We didn't have a golden set because we were told we have to do the labeling to create that set." Instead, the team worked with three reference lists: a customer name list, a fab/location identifier list, and an acronym exclusion list of approximately 3,000 entries.

This is the single most consequential technical gap in the entire prior effort. Everything downstream was compromised by this absence. Without ground truth, there is no way to train a model to recognize domain-specific entities (it has nothing to learn from), no way to evaluate whether a model is improving (there is no benchmark), no way to compare models meaningfully (all comparisons are against an undefined standard), and no way to fine-tune anything (there is no labeled data). The reference lists they used are configuration inputs for a deterministic system, not training data for machine learning. Feeding flat lookup tables to Flair, SpaCy, or Azure AI as the basis for evaluation is a category mismatch.

The team was told that creating a golden set required the full 1,000-hour labeling exercise, and they accepted that framing without challenge. The three-tier labeling framework presented in the meeting (Tier 1: word level, Tier 2: word + document context, Tier 3: word + document + human reasoning) was specifically designed to demonstrate that this assumption was wrong. Starting at Tier 2 produces a usable training set with dramatically less effort than the Tier 3 estimate.

**Colin's assessment:** This is the item that tells the entire story at once. Without ground truth, there is nothing the team could have done that makes logical sense. Every model evaluation, every comparison, every attempt at fine-tuning was fundamentally undermined from the start. Skipping ground truth because it is hard is not a technical decision. It is the equivalent of expecting a car to run without fuel because fuel is expensive. The prerequisite exists for a reason, and there is no shortcut around it.

The reference lists they do have are valuable, but not for what they were used for. Those lists are inputs for a rule-based deterministic system, and they will be useful for generating synthetic training data for the actual approach. They are a starting point, not a substitute for labeled examples.

The 1,000-hour labeling estimate was almost certainly provided by someone who did not understand the problem or the available approaches, and Mikhail accepted it as a trusted technical assessment. It was hand-waving that became gospel. The real effort to produce a functional Tier 2 data set is a fraction of that estimate, especially with auto-labeling techniques and the existing reference lists as seed data. The three-tier framework presented in the meeting was designed to break this misconception, and it clearly resonated with Mikhail. His immediate self-assessment ("We'd be definitely Tier 1 first") showed he understood both where the team currently sits and what the path forward looks like.

The characterization on the call that the data they had "probably only legitimately lends itself to being suitable for a rule-based approach" was diplomatically understated. The reality is that the entire ML effort was built on a foundation that could not support it, and no amount of model selection or reconciliation architecture could compensate for the absence of ground truth.

---

## 6. The 1,000-Hour Labeling Estimate

The full labeling exercise was estimated at over 1,000 person-hours for the initial pass, not including ongoing maintenance. This was deemed cost-prohibitive relative to expected value and became the justification for abandoning the ground truth pathway entirely. Mikhail said "we were told" without specifying who provided the estimate or what methodology produced it.

**Colin's assessment:** The estimate was not legitimate. It was hand-waving from someone who was likely overwhelmed by the scope, completed an initial POC, and did not want to do the remaining work. The number has no analytical basis. The team never scoped the actual data set, never determined what a statistically meaningful sample would look like, and never considered tiered or automated approaches to labeling. Quoting hours without understanding what you are actually doing is not estimation. It is avoidance dressed as analysis.

The deeper problem is that the team does not have a concept of automation in the labeling process. Their mental model is a human being sitting in front of every document and manually classifying it, which is the most expensive possible approach and is not required. The existing reference lists (customer names, fab identifiers, acronym exclusions) are seed data for auto-labeling. A rule-based pass using those lists can generate initial labels across the data set, and human reviewers then validate and correct rather than create from scratch. This reduces the effort by an order of magnitude compared to fully manual labeling.

There is an important nuance around auto-labeling that was discussed in the meeting: AI should never be used unilaterally to evaluate other AI's output. Auto-labeling is a tool to accelerate human review, not a replacement for it. Ground truth requires a human seal of approval. The auto-labeling step generates candidates; the human confirms or rejects. That distinction matters and was explicitly addressed during the meeting.

The scope question remains completely unanswered. How many tickets exist? How many text fields total? What is the distribution of content across those fields? None of this has been quantified. Without that baseline, any hour estimate is meaningless. The correct approach is exploratory data analysis to understand the actual data landscape before committing to a labeling methodology or quoting effort.

Brad's reference to 140-page legal-approved documents is also worth examining. Legal approval of a document does not constitute ground truth for an AI system. Legal reviews are based on representations from the technical team ("does this document contain restricted content?"), not on independent verification. Legal blesses a document based on information provided to them, not based on reading 140 pages and making entity-level judgments. A legal stamp says the process was followed, not that the content is accurately classified. If the underlying classification is wrong, the legal approval is built on a false premise. This is another area where the team has conflated a process checkpoint with actual data quality.

---

## 7. The Standalone Service Architecture

Mikhail corrected the assumption that the capability was built into Escalation Solver: "There's a big difference between application and application data. We've actually built this as a standalone service. We did not build it into the application. We use this application data because we wanted a standalone thing that any application could call it, a redaction service. You pass in and get detection, or you pass in and get redacted text back."

This is an intentional architectural decision: a decoupled service accepting text input via API and returning detection results or redacted text. It is the correct pattern for a capability that needs to scale across multiple applications over time.

**Colin's assessment:** The standalone service architecture is the one sound decision in the prior work, and notably it is pure software engineering, not AI. The API-based pattern is exactly what you would expect from a competent engineering team, and it is the part of the work that falls squarely within Daniel's domain of expertise.

This also further undermines Daniel's edge AI fixation. Air-gapped deployments are intrinsically tightly coupled components where the detection capability must be embedded within the application or device. A standalone API service is the opposite of that pattern. The architecture the team already built points toward cloud-hosted, network-accessible services, not disconnected edge deployments.

For the POC, the standalone service design is largely irrelevant. The POC is not building an application or integrating into one. The scope agreed upon in the meeting is straightforward: given real data from Escalation Solver, can the system perform accurate detection? That is a data-in, results-out exercise. Application integration, API patterns, and service architecture are all post-POC concerns that only become relevant when moving from validation to production deployment.

---

## 8. The 21% False Positive Rate and 90% Detection Accuracy

Mikhail corrected the false positive rate from the first meeting: 21%, not 20%. The reconciliation algorithm brought it to 17%. Detection accuracy was approximately 90%. MVP target was less than 5% false positives, ultimate goal less than 1%.

Mikhail separated detection accuracy from false positive rate and argued they serve different use cases differently. For detection (alerting users), 90% accuracy with a manageable false positive rate could be workable. For redaction (removing content before it enters the general knowledge base), 90% accuracy is insufficient.

**Colin's assessment:** These numbers should be treated with skepticism. It is unclear that any of them were derived through a scientifically viable testing methodology. Mikhail references AI evaluation terminology like precision and recall, but those terms do not carry meaning without a well-defined test set, clear class definitions, and a reproducible evaluation protocol. Given that the team could not construct a golden set and selected models based on out-of-the-box bake-offs, the likelihood that they had a rigorous evaluation framework is low.

The 90% accuracy and 21% false positive rate also do not reconcile cleanly. These metrics are related, and the combination suggests either the evaluation methodology was inconsistent across measurements or the definitions of what constitutes a true positive, false positive, and false negative were not stable. Without understanding exactly what was tested, how it was tested, and against what ground truth, these numbers are directional at best.

Mikhail's persistent distinction between detection and redaction also continues to be a source of confusion. Detection is inherently a prerequisite to redaction. You cannot redact something without first detecting it. They are not parallel capabilities or separate use cases in a technical sense. Detection identifies the target, and redaction acts on it. The action taken after detection (notify the user, mask the text, block the upload) is a policy decision, not a different technical system. The framing of these as fundamentally separate use cases with separate accuracy requirements conflates the policy layer with the technical layer.

The POC approach should reframe evaluation entirely. Rather than chasing a specific false positive target, the POC should demonstrate what proper evaluation looks like by introducing meaningful metrics beyond basic precision and recall, using actual labeled data with a defined evaluation protocol, and showing measurable progress across iterations. The Lam team are competent engineers who understand iterative improvement in their own domain. Presenting evaluation in engineering terms (baseline measurement, controlled changes, measurable deltas) translates the AI evaluation process into a framework they can reason about. The POC does not need to achieve perfection on the first iteration. It needs to demonstrate a credible methodology that shows progress and gives the team confidence that continued investment will produce continued improvement.

---

## 9. Globally Trained Models and the False Positive Problem

Mikhail identified what he believed was the root cause: "These models are globally trained, so a lot of things contextually they were redacting on our side which was not customer confidential, even, because they were trained." He noted the models "come in pre-trained, they come in blend," attributing the false positive problem to global training data conflicting with Lam-specific definitions of sensitivity.

**Colin's assessment:** Mikhail's observation is directionally correct but misplaced. The issue is not that the models came pre-trained with conflicting global knowledge. Presidio models, Flair, and SpaCy NER are not trained to recognize "Samsung" as a semiconductor customer in a field service context. They are not even trained on that type of content. The models are generic NER tools that recognize standard entity categories (person, organization, location). The false positives were not caused by the models knowing too much from global training. They were caused by the models knowing nothing about Lam's domain and applying generic pattern matching to text they had no basis for understanding.

The real issue is simpler: the models were never re-trained. The team provided no comparative content, no labeled examples, no domain-specific signal of any kind. Without that, the models were operating purely out of the box, and the 21% false positive rate is exactly what you would expect from unguided generic NER applied to domain-specific text. It is not a pre-training problem. It is a complete absence of any training for the actual task.

Mikhail also did not consider that the detection approach itself was fundamentally wrong for a significant portion of the problem. Known entities (customer names, fab identifiers) do not require probabilistic classification. A deterministic lookup against a curated dictionary handles them with zero false positives because it is exact matching. The models were being asked to solve a problem that a much simpler system handles perfectly. The AI layer should only be invoked for contextual cases where deterministic matching cannot reach. This connects directly to the layered architecture presented in the meeting, where the deterministic layer eliminates false positives on known patterns entirely and the AI layer operates on a much smaller, more tractable set of ambiguous cases.

Mikhail's thinking was modified by the meeting discussion, but his understanding is still incomplete. He continues to default to a structured versus unstructured data distinction that was explicitly addressed in the meeting as irrelevant. At one point in the call he agreed that structured versus unstructured does not matter because the first step with any unstructured input is to convert it to a structured representation. Despite agreeing in the moment, he reverted to the distinction multiple times afterward, which suggests the conceptual shift has not fully taken hold. This is worth monitoring in future conversations, as it may resurface when scoping expands beyond the initial five text fields into documents and attachments.

---

## 10. The Existing Thumbs Up / Thumbs Down UI

Mikhail mentioned that a UI exists allowing users to give thumbs up or thumbs down on whether the system's detection was correct. Approximately 1,000 examples have been labeled through this mechanism. He described it as a continuous feedback loop. The UI appears to be specific to the Escalation Solver application, not a general-purpose tool across all of Lam's systems.

**Colin's assessment:** The thumbs up/down data is potentially useful but requires significant qualification before any weight is placed on it. The critical unknowns are who is providing the feedback and what criteria they are following. If the reviewers are field service engineers with domain knowledge and a written rule set defining what constitutes sensitive content, the labels may be reliable. If the feedback is based on individual intuition without documented criteria, the labels are subjective and potentially inconsistent across reviewers. A data set where reviewers apply different standards contains contradictions that will degrade any model trained on it.

The quality of the labels also has a bidirectional trust problem. If the system is wrong 21% of the time, users lose confidence and stop providing meaningful feedback. But even if the system were perfectly accurate, users who do not have clear criteria for what constitutes sensitive content will introduce their own error rate. If the human reviewers are wrong 20% of the time based on gut feeling rather than defined rules, the feedback loop degrades the system rather than improving it. Ground truth requires defined, documented criteria that reviewers can apply consistently, not blind intuition-based assessment.

One thousand examples is also a suspiciously round number. Mikhail has now used "a thousand" three times across different contexts: a thousand hours for labeling, a thousand examples in the thumbs up/down UI, and other references to scale. This pattern suggests the number is approximate and possibly inflated. Until the actual data is examined, the count and the quality are both unverified.

For the POC, this data should be treated as a starting point for exploratory data analysis, not as a validated training set. The Exploratory Data Analysis (EDA) step will determine the distribution (almost certainly heavily skewed toward one class), the consistency of labeling, and whether the volume is sufficient for meaningful model training. For rule-based approaches and basic ML classifiers, a thousand labeled examples may have some utility if the quality holds up. For Large Language Model (LLM) fine-tuning, a thousand examples is negligible and there is no point attempting retraining or fine-tuning at that scale. The parameters of a modern LLM number in the billions, and a thousand training examples would produce no statistically meaningful shift in model behavior.

The feedback loop concept is sound for long-term system improvement, but it is a post-deployment mechanism that depends on having a system accurate enough to earn user trust. It is not a bootstrapping mechanism for a system that does not yet work.

---

## 11. Five Fields, Two Elements

Mikhail was specific about the scope: five free-text fields within Escalation Solver tickets, each between 4,000 and 5,000 characters. Two elements are being detected: customer name and fab identifier. He drew an explicit distinction: "It's not the two data fields. It's five data fields but the two elements. Customer name and fab ID. So we're looking for two specific identifiers within five text fields." Document redaction is not in scope: "Right now we're just trying to see how we can open up text."

The fields are where field engineers describe problems conversationally. Mikhail's example: "I'm having a plasma arcing issue at [customer site] and start giving a lot of detail." Sensitive information is embedded naturally in problem descriptions, not in structured metadata fields.

**Colin's assessment:** The scope is fine as a constraint for the POC. The data volumes are trivial: 4,500 words per ticket across five fields is not even close to a processing challenge for any modern system.

The more fundamental question is what Mikhail actually means by "two elements within five text fields." If the task is literally detecting the presence of known customer names and known fab identifiers in free text, that is a regex problem. A deterministic script matching against the customer name list and fab identifier list they already have could be written in a day and would produce zero false positives on exact matches. The fact that they deployed three ML models, a reconciliation algorithm, and an on-prem Kubernetes cluster to solve what may be a pattern matching problem is the clearest indication of how far the approach diverged from the actual requirements.

The complication that justifies going beyond regex is spelling variation and contextual ambiguity: abbreviated names, informal shorthand, and cases where a term could be sensitive in one context but innocuous in another. Those edge cases are real and require more than exact matching. But the base case of known entities with known variations is deterministic, and the layered architecture addresses this by handling the easy cases cheaply and only escalating the ambiguous ones. The scope as defined is the right starting point. The approach Lam applied to it was dramatically overcomplicated for what the task actually requires.

---

## 12. Detection vs. Redaction as Separate Use Cases

Mikhail has maintained the detection versus redaction distinction across every meeting. He frames detection as real-time notification at data entry (lightweight, speed-focused, false-positive-sensitive) and redaction as batch processing on stored content (heavier, accuracy-focused, over-redaction acceptable). Brad added that the prior effort started as redaction only, and detection evolved as a secondary outcome. Mikhail has stated multiple times that redaction is more valuable than detection.

**Colin's assessment:** The detection versus redaction distinction is a false dichotomy that creates dual work for no reason. This needs to be addressed separately with Mikhail in a focused conversation, but the reasoning is straightforward on two levels.

First, redaction as a standalone concept does not make sense if the ingestion pipeline works correctly. If content is properly detected at the point of entry and prevented from entering the knowledge base when it contains sensitive information, then the source content in the system is clean. There is nothing to redact because the polluted information never made it in. The redaction use case Mikhail describes (cleaning up stored content in batch) is the historical cleanup problem, which is a bounded, one-time effort, not an ongoing operational mode. Going forward, if detection at ingestion works, the redaction workload approaches zero. Additionally, output monitoring (through something like Microsoft Purview on the language model response layer) provides a second line of defense without requiring source file modification.

Second, redaction is technically nothing more than detection with a different downstream action. Detection identifies the sensitive entity. Redaction replaces those characters with asterisks or masks or removes them. The AI and NLP work is identical. The only difference is what happens after the entity is found: notify the user (detection) or modify the text (redaction). There is no AI capability that separates the two. Building them as separate systems duplicates the detection engine, the evaluation pipeline, and the maintenance burden for no technical benefit.

Mikhail may be using "redaction" to mean editing source files that are already in the system, which would be the historical cleanup use case. If so, the framing makes more business sense but the technical point still holds: detection is the engine, and redaction is one of several possible actions the engine can trigger. The distinction belongs in the policy layer, not the architecture.

The current situation is workable because the POC is focused on detection only, and Lam is not forcing a parallel redaction effort. The conversation with Mikhail about collapsing these into a single pipeline with multiple action handlers should happen after the POC demonstrates the detection capability, at which point the argument becomes concrete rather than theoretical.
