# 05a - Discussion: Architecture Discussion and Credibility

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-06
**Document Set:** 05a (Technical Decomposition Discussion, supplementary to Set 05)
**Pass:** Assessment of architecture presentation and credibility milestones

---

## 1. Linear Funnel vs. Parallel (Lam's Prior Approach)

The core architectural contrast presented in the meeting. Lam ran three models in parallel and reconciled results. The proposed approach runs detection through a sequential funnel: deterministic first, then ML/NLP, then Gen AI. Each layer handles what it can and passes unresolved items to the next.

The practical implications are significant across multiple dimensions:

- **Cost:** The parallel approach runs every piece of content through every model. The linear approach lets the deterministic layer (essentially free in compute terms) resolve the majority of cases. Only a fraction reaches the ML layer, and a smaller fraction reaches the Gen AI layer (the most expensive per call). Total compute cost drops dramatically.
- **Accuracy:** Each layer is optimized for a specific problem class. Deterministic handles known patterns with zero false positives. ML handles pattern-adjacent cases. Gen AI handles truly contextual ambiguity. No layer is asked to be a generalist.
- **Debuggability:** In a parallel system, it is unclear which model caused an error and why reconciliation chose that result. In a linear system, the determination traces to a specific layer with a specific reason, making error correction targeted rather than systemic.
- **Scalability:** Adding new entity types or applications means updating the deterministic layer's dictionaries first (a configuration change, not a model retraining exercise). ML or Gen AI capability is only added when new entities introduce genuinely new contextual ambiguity.

The parallel approach was identified on the call as a modified mixture of experts, framed diplomatically as the architecture that was prominent 18 months ago when Mistral MOE was getting attention.

**Colin's assessment:** The distinction between the linear and parallel approaches may not have fully landed with the team in the moment, but the presentation was diplomatic and served its purpose. The team's takeaway was likely more general: the prior approach was not structured, and a structured approach exists that addresses the specific failure modes they experienced.

The broader message that came through clearly is the difference between trying AI models and actually engineering a detection system. The prior effort was exploratory: pick models, run them, compare outputs, hope for improvement. The proposed approach is architectural: define what each layer is responsible for, route problems to the appropriate layer, and only invoke expensive compute when cheaper methods cannot resolve the case. The meeting gave the Lam team a concrete demonstration of what it looks like when someone who has done this before approaches the same problem.

---

## 2. Purview for the Deterministic Layer

Microsoft Purview was positioned as the enterprise tooling for the first layer of the funnel. The specific capability is custom Sensitive Information Types (SITs), which allow organizations to define detection patterns beyond standard PII categories. For Lam, this would mean SITs for customer names, fab identifiers, and their known spelling variations.

The advantage over a custom regex script is not technical. A Python script with regex patterns detects the same things. The advantage is operational: Purview is managed through the Microsoft compliance center, integrates natively with the Azure ecosystem (Data Loss Prevention policies, sensitivity labels, Copilot guardrails), and can be maintained by compliance or IT administrators without engineering involvement. Detection rules are updated through a UI, not by deploying code. Adding a new customer name or fab identifier is a configuration change, not a release cycle.

This matters for Lam because of the CSBG/GIS dynamic. If the detection capability is a custom service maintained by Brad's team, it is another piece of shadow IT that the CIO's organization will eventually challenge. Built on Purview, it sits within enterprise compliance tooling that IT already manages and trusts. This bridges the gap between Brad's team owning the initiative and IT being comfortable with the implementation. When the project scales beyond Brad's domain, the infrastructure is already enterprise-compliant rather than requiring a rebuild.

The architecture section was compressed due to Brad's 2:30 hard stop, and the Purview positioning did not receive the full treatment it warranted. It was mentioned as the enterprise tooling for the deterministic layer, but the operational and political advantages were not elaborated.

**Colin's assessment:** This topic was not discussed in sufficient depth during the meeting due to time constraints, but the positioning is correct and should be captured. Purview is the bridge that can bring the GIS team into the fold. Instead of continuing down the path of shadow IT where Brad's team builds and maintains detection infrastructure independently, Purview places the capability within enterprise compliance tooling that IT professionals recognize, manage, and are accountable for. This transforms the engagement from Brad's team doing their own thing in parallel to Brad's team implementing a solution that IT can co-own and operate. That shift is significant for the long-term relationship between CSBG and GIS, and it positions BayOne as the partner that solved both the technical problem and the organizational one.

---

## 3. The "Accidental Hodgepodge" Recognition

After the layered architecture presentation, Mikhail connected the dots to the prior work on his own. His exact words: "So we just basically accidentally picked literally every single thing, one of each." He then confirmed: "So basically, Hugging Face, that's a small language model, and then Transformers, like in our case SpaCy, that's an NLP model? Okay, got it. So we just literally picked like a hodgepodge of stuff and then stuck a regex on top of that as well."

He followed with: "I wasn't the one picking it. I'm coming in from the business side of things. I'm just confirming what I just heard." This distanced himself from the model selection while acknowledging he now understands why the choices did not work.

**Colin's assessment:** This was the most important moment in the meeting from both a technical and a relationship standpoint. Mikhail arrived at the conclusion independently. He was not told the prior approach was wrong. He was shown a structured approach, looked at his own prior work through that lens, and recognized the gap himself. That distinction matters enormously. When someone owns an insight rather than defending against a criticism, the dynamic shifts from adversarial to collaborative.

Mikhail demonstrated genuine understanding in this moment, not performance. He was smart enough to see that whoever made the prior technical decisions selected models without any structured rationale and assembled them without understanding how they should work together. The prior partner or internal engineering team lost credibility in real time, and BayOne gained it, without a single negative word being said about anyone's work.

Mikhail's political move to distance himself from the design decisions was self-aware and deliberate. He is signaling that the technical choices were made by others and that he now has a framework for evaluating whether future technical decisions are sound. Going forward, this changes the working relationship. Mikhail is likely to view his own internal teams and prior partners with more scrutiny and to give BayOne's technical recommendations more weight. He is the person on the Lam side who will champion the approach internally, and this moment is the foundation of that trust.

---

## 4. Brad's Intuitive Grasp of the Layered Architecture

Colin used the "layers of an onion" phrasing during the meeting to describe the layered architecture, but the concept itself was something Brad had arrived at independently. Brad intuitively grasped that the answer was a combination of approaches where simpler methods handle simple cases and more sophisticated methods handle the harder ones, before the formal architecture was presented. Colin put a name and a structure to what Brad was already thinking.

**Colin's assessment:** Brad, as the economic buying influence and a non-technical business leader, ended up demonstrating a better intuitive grasp of the fundamental engineering concept than the technical people on the call. He understood that you do not send everything to the most expensive tool when a cheaper tool resolves most cases. That is a basic engineering principle, and Brad arrived at it through business logic rather than technical training.

This is significant for two reasons. First, it is validating to Brad. Having the technical approach confirm his own thinking builds rapport and confidence. He is not being taught something foreign. He is being shown a structured version of something he already understood, which positions BayOne as a partner that thinks the way he thinks. Second, it should be noted that a non-technical executive understood this concept more quickly and clearly than a self-described 30-year engineering leader (Daniel) who spent the meeting fixated on edge AI instead of engaging with the actual architecture.

For the proposal, the layered approach should be presented in business terms that Brad already resonates with. He does not need to be convinced of the concept. He needs to see it scoped, costed, and mapped to his specific environment. The heavy technical justification is unnecessary for him because the intuition is already there.

---

## 5. The Three-Tier Labeling Framework

Colin introduced three tiers of labeling to demonstrate that creating ground truth does not require the 1,000-hour all-or-nothing exercise the team had been told was necessary:

- **Tier 1:** The flagged word or entity on its own. Binary classification, no document context, no human explanation. The existing thumbs up/thumbs down data is Tier 1.
- **Tier 2:** The flagged word plus the document or text field it appeared in. The model gets context but no human reasoning about why it was flagged. Significantly more useful than Tier 1 because context enables the model to learn patterns about when and where sensitive entities appear.
- **Tier 3:** The flagged word, plus the document, plus a human explanation of why it is or is not sensitive. The richest training signal but the most expensive to produce. This is what the team was told they needed for the entire data set, which caused the 1,000-hour estimate.

Mikhail's immediate response: "We'd be definitely Tier 1 first." He understood where the team sits and implicitly accepted that the path forward is incremental. Colin clarified that you start at Tier 2 and subset to Tier 3 for the hardest cases, not the other way around.

**Colin's assessment:** The framework accomplished two things simultaneously. It broke the mental barrier of the 1,000-hour estimate by demonstrating that useful training data can be produced at a fraction of that cost through a tiered approach. And it gave the team a vocabulary for discussing data quality that is more nuanced than the binary of "we need labeling" versus "labeling is too expensive."

Mikhail's immediate self-placement at Tier 1 showed genuine comprehension of both where the team currently stands and what the incremental path forward looks like. This reframes the labeling conversation for the POC from a prohibitive upfront cost to a manageable, progressive investment that starts producing value at each tier.

The existing 1,000 thumbs up/thumbs down examples are already Tier 1 data that could be promoted to Tier 2 by linking them to their source documents. This provides a concrete starting point for the POC's data work rather than requiring the team to begin from zero.

---

## 6. Exploratory Data Analysis (EDA) to Determine Sample Sufficiency

Mikhail asked the direct question: how many labeled examples would they need? ("A thousand five fields, so like five thousand total fields, or we talk in tens of thousands?") Colin introduced Exploratory Data Analysis as the method to answer with precision rather than guesswork.

The core point was that sample sufficiency is not a fixed number. It depends on data separability. Colin used the giraffe/car analogy: distinguishing two things that look nothing alike requires very few examples; distinguishing two things that are nearly identical (front and back of a quarter) requires many more. For Lam's five text fields, which are all problem descriptions written in similar style, the content is likely highly similar within classes. Colin cited 20,000 samples as a general benchmark for highly similar data but immediately qualified it as not meaningful without understanding the actual data distribution.

EDA answers this before any labeling commitment is made. By examining the existing data, EDA measures similarity within and between classes, label consistency, and minimum sample size for statistically meaningful training. The team gets a data-driven answer instead of guessing or accepting hand-waved estimates.

**Colin's assessment:** This was the right move and it resonated, particularly with Mikhail. The giraffe/car analogy was effective and well received. The Lam team has likely been given flat numbers by both internal teams and other vendors: generic estimates produced without examining the actual data, driven by sales positioning or general rules of thumb rather than analysis. The EDA approach is different because it comes from someone who has actually done this work at scale and knows that the answer is always "it depends on what the data looks like."

That distinction between a data-driven answer and a hand-waved number is what builds credibility with an engineering team. Engineers respect methodology. They do not respect guesses dressed up as estimates. The EDA step in the POC serves a dual purpose: it produces the technical answer needed for planning, and it demonstrates to the Lam team that BayOne's approach is grounded in analysis rather than assertion. Both outcomes strengthen the engagement.
