# 05a - Discussion: Stakeholder Technical Gaps

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-06
**Document Set:** 05a (Technical Decomposition Discussion, supplementary to Set 05)
**Pass:** Assessment of individual stakeholder technical understanding

---

**WARNING: Internal only. Candid assessments. None of this should appear in client-facing materials.**

---

## 1. Daniel's Edge AI / Small Language Model Fixation

Daniel pushed on this topic repeatedly throughout the meeting. His first substantive intervention asked whether the architecture was "only focused on the enterprise implementation or are we considering offline or small language models." He subsequently raised clean room environments, customer fab deployments, the MABC project, E10 data extraction, and Small Language Model (SLM) parity with enterprise Large Language Models (LLMs). Brad scope-managed him multiple times, ultimately directing: "Focus on the cloud for the primary use case, but discussions in future thinking about how to achieve parity between those air-gapped files as well."

Daniel's framing: data gets captured in customer clean rooms and needs cleansing before flowing back into the enterprise. He wants to know if detection can run inside the fab on a disconnected device before data ever leaves the customer site. He repeatedly used "parity between models" to ask whether an SLM on an edge device could replicate enterprise LLM results.

**Colin's assessment:** Daniel does not understand how model deployment works. His mental model appears to be that running small language models locally at a customer site is the answer for data cleansing at the edge. In reality, the data sensitivity question at customer sites is a legal and contractual matter, not a model deployment problem. What data can leave a customer fab, under what conditions, and with what protections is governed by customer agreements and data-out policies, not by where a language model is hosted. Processing data locally using an SLM does not change the legal or contractual obligations around that data.

The edge AI discussion also completely contradicts the Azure-based architecture that the rest of the meeting aligned on. If there is a specific business requirement from Brad to run detection offline at customer sites, that is a legitimate future-state conversation. That requirement has not been stated. Daniel introduced it independently without a corresponding business case from the decision maker.

The model parity concept Daniel kept referencing is not meaningful. A model with 3 billion parameters and one with 300 billion parameters are fundamentally different classes of capability. They differ in parameter count, context window, reasoning depth, and generalization ability. Comparing their outputs and calling the comparison "parity" implies an equivalence that does not exist. You can evaluate both against the same test set and measure the performance gap, but the expectation that they will produce equivalent results is technically uninformed.

Daniel also conflated deployment topology (where a model runs) with model architecture (what a model can do). Running a model on Azure versus on-prem versus on an edge device is an infrastructure decision that does not change the model's capabilities within its own class. His questions suggested he believed that choosing Azure would lock them out of edge deployment, which reflects a misunderstanding of how models are packaged, deployed, and served across different environments.

The broader concern is one of priorities. The team has not solved the enterprise use case. A basic text classifier on cloud infrastructure with full compute resources is not working at acceptable accuracy. Worrying about whether that same capability can run on a disconnected edge device is premature to the point of irrelevance. The enterprise problem must be solved first, and the architecture that solves it will inform what is and is not feasible at the edge. Addressing it in the other direction produces nothing actionable.

---

## 2. Daniel's Enterprise vs. Offline Architecture Question

Daniel's first substantive contribution, asked before any discussion of the actual problem, prior work, or POC scope: "Are we only focused on the enterprise implementation or are we considering offline or small language models? Do we need to ensure that the possibility for supporting that, or are we going to architect our solution ourselves into an enterprise-owned model?"

Brad and Mikhail both redirected him. Brad: prove the use case first, then determine deployment modes. Mikhail: in a disconnected environment, the security posture is already different because data is manually controlled. Both responses indicated this is a familiar tangent from Daniel that they have already decided is not a current priority.

Daniel's response to being redirected was to continue pressing: "If we're not bringing it up as, hey, this is where we see ourselves five, 10 years from now..."

**Colin's assessment:** The question did not add value to the meeting, and the room did not receive it as valuable. Brad and Mikhail's repeated redirection made that clear. The concern about architectural decisions constraining future deployment options is a legitimate engineering consideration in the abstract, but the timing was premature. The question was asked before the target application was named, before the prior work was discussed, and before any architecture was presented. Asking about the ceiling before the foundation exists is not strategic thinking. It is jumping the gun.

Daniel's framing of "where we see ourselves five to ten years from now" is particularly disconnected from the reality of the engagement. Eighteen months ago, the team was at the same starting point they are at today. The prior effort produced no meaningful advancement. Speculating about a five-to-ten-year technology vision when the team has not yet demonstrated the ability to execute on the immediate problem is not a useful contribution. The five-year vision becomes relevant after the first use case is solved, not before.

---

## 3. Stakeholder Technical Understanding: Individual Assessments

### 3.1 Brad (Economic Buying Influence, Business Leader)

Brad is not a technical person and does not position himself as one. His role is executive sponsorship and business decision-making. Despite this, he demonstrated a better intuitive grasp of the fundamental engineering concept behind the layered architecture than the technical people on the call.

Brad intuitively understood that you do not send everything to the most expensive tool when a cheaper tool resolves most cases. He arrived at this through business logic rather than technical training. Colin's "layers of an onion" phrasing gave structure to a concept Brad had already formed independently. This is significant: a non-technical executive who likely spends most of his time in organizational management understood the layered approach more quickly and clearly than a self-described 30-year engineering leader who spent the meeting fixated on edge AI.

Brad's scope management of Daniel was consistent and deliberate. He redirected Daniel multiple times toward the immediate problem, indicating that the edge AI tangent is a known pattern from Daniel, not a novel concern. Brad's instinct to prove the use case first and worry about deployment later reflects sound engineering prioritization even if it comes from business intuition rather than technical training.

Brad is the person who will approve the engagement. The proposal should be presented in business terms he already resonates with. He does not need to be convinced of the layered concept. He needs to see it scoped, costed, and mapped to his specific environment.

### 3.2 Mikhail (Technical Lead, Business-Side)

Mikhail is the most technically engaged stakeholder and the one whose understanding shifted the most during the meeting. He came in with a frame of reference built around the prior work (Presidio, three models, reconciliation algorithm) and left with a substantially different understanding of why that approach produced limited results and what a structured approach looks like.

Key indicators of genuine comprehension:

- **The "accidental hodgepodge" recognition.** After the layered architecture presentation, Mikhail connected the dots independently: "So we just basically accidentally picked literally every single thing, one of each." He arrived at the conclusion without being told the prior approach was wrong. He was shown a structured approach, looked at his own prior work through that lens, and recognized the gap himself.
- **Immediate self-placement on the labeling framework.** When the three-tier labeling framework was presented, Mikhail's response was "We'd be definitely Tier 1 first." This showed he understood both where the team currently stands and what the incremental path forward looks like.
- **Political self-awareness.** His statement "I wasn't the one picking it. I'm coming in from the business side of things. I'm just confirming what I just heard" distanced himself from the prior model selection while acknowledging he now understands why those choices did not work. This was deliberate.

Mikhail's understanding is incomplete in one important area: he continues to default to a structured versus unstructured data distinction that was explicitly addressed in the meeting as irrelevant. He agreed in the moment that structured versus unstructured does not matter because the first step with any unstructured input is to convert it to a structured representation. Despite agreeing, he reverted to the distinction multiple times afterward. The conceptual shift has not fully taken hold and is worth monitoring in future conversations.

Mikhail will be the person on the Lam side who champions the approach internally. The "accidental hodgepodge" moment is the foundation of that trust. He is likely to view his own internal teams and prior partners with more scrutiny going forward and to give BayOne's technical recommendations more weight.

### 3.3 Daniel (Engineering Leader, 30+ Years)

Daniel is the most problematic stakeholder from a technical credibility standpoint. He self-identifies as a veteran engineering leader, but his contributions in the meeting reveal fundamental gaps in AI and modern deployment understanding.

Key indicators:

- **Edge AI fixation without business justification.** Daniel introduced edge deployment, air-gapped environments, clean room processing, and SLM parity as concerns before the target application was even named. None of these were supported by a business requirement from Brad. They were Daniel's personal technical interests projected onto the engagement.
- **Model parity misconception.** His repeated references to "parity between models" -- comparing a 3-billion-parameter SLM to a 300-billion-parameter LLM as though they should produce equivalent results -- is not a serious technical position. These are fundamentally different classes of capability, and treating them as interchangeable reflects a surface-level understanding of how language models work.
- **Deployment topology confused with model capability.** Daniel's questions suggested he believed choosing Azure would lock the team out of edge deployment. Running a model on Azure versus on-prem versus on an edge device is an infrastructure decision that does not change the model's capabilities. This conflation indicates he does not understand how models are packaged, deployed, and served across different environments.
- **Contradiction with existing architecture.** The standalone API service architecture the team already built points toward cloud-hosted, network-accessible services. Air-gapped edge deployments are intrinsically tightly coupled components. Daniel's preferred direction contradicts the architecture his own team built.
- **Aspiration without foundation.** The team has not solved the enterprise use case with full cloud compute resources. Aspirations around edge deployment are premature when the core problem remains unsolved. Without a concrete plan for what would be deployed, how it would be trained, or what architecture would support it, edge discussions are speculative rather than actionable.

Daniel was scope-managed by both Brad and Mikhail multiple times, which indicates this is a known pattern. His contributions stood in sharp contrast to the team's inability to discuss basic NLP fundamentals. The gap between his self-positioning as a senior technical leader and his actual contributions in the meeting is significant.

For the engagement, Daniel should be managed carefully. His instinct to expand scope toward edge AI and disconnected environments could create distraction if not channeled. The approach should acknowledge his concerns as legitimate future-state considerations while keeping the immediate work focused on the enterprise use case. Brad has already established this framing and it should be reinforced rather than challenged.
