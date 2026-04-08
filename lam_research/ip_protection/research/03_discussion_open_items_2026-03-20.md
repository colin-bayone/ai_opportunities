# 03 - Discussion: Open Items and Information Needs

**Source:** /lam_research/ip_protection/source/prior_discussion_open_needs_2026-03-20.md (and 1 related file)
**Source Date:** 2026-03-20 (Working discussion between Colin Moore and Claude)
**Document Set:** 03 (Prior Working Discussion)
**Pass:** Consolidated open items and information needs from 2 source documents

---

## Critical Dependency Chain

Everything downstream depends on one piece of information: **the name of the first application**. Colin asked this directly on the March 12 discovery call and was told it was "too technical." It is not. It is a business question: which application should be the first to move to the new architecture?

Without naming the first application, BayOne cannot:
- Scope a POC
- Estimate costs
- Write a formal proposal
- Design a technical architecture
- Select the right processing pipeline
- Determine data volume or integration requirements

The dependency chain is linear:

```
Name the first application
  -> Scope POC around that application
    -> Estimate costs and timeline
      -> Write the proposal
        -> Request document samples and system access
          -> Build the POC
```

Every question below ultimately feeds into or flows from this single gate.

---

## Priority 1: What the Sales Team Can Get Without a Technical Call

These are questions Pat, Pradeep, and Anuj should be able to extract from Brad or Mikhail. None of these require Daniel or a technical deep-dive.

### 1.1 Name One Application (Critical Path)

- Name one specific RAG-like application -- the highest-impact one
- Describe what it does in business terms
- What documents or data sources feed it
- This was asked on the March 12 call and redirected as "too technical." It needs to be re-asked, framed as a business question: "Which of your search or knowledge applications would benefit most from going first?"

### 1.2 Data Volume Estimates

| Metric | Why It Matters |
|--------|----------------|
| Documents ingested per day or week | Architecture decisions, cost modeling |
| Support tickets created per day | Scale planning for Use Case 2 (real-time detection) |
| Search queries per day | Load estimation for the control plane |
| Number of users across all systems | Licensing, access control scope, user behavior analytics |

### 1.3 Verify Brad's Authority

Brad stated on the discovery call that he owns everything end-to-end: business, product, program, and technical. This is unusually consolidated authority for a $17 billion company. The following must be verified before BayOne invests in a proposal:

- Does Brad have IT decision-making authority, or does IT have veto power?
- How do cybersecurity and information security factor in? Do they approve cloud service procurement?
- Who controls infrastructure decisions (cloud services, data residency, new Azure service provisioning)?
- Who has final approval on spend for a project of this nature?

The risk: building a proposal that assumes Brad can greenlight everything, only to discover IT or security must approve and has different priorities.

### 1.4 Budget and Timeline

- What budget range is Lam working with for this initiative?
- The 1,000 man-hours comment from the discovery call (referring to the data labeling exercise that was paused) suggests they have no existing cost framework. BayOne needs to understand expectations before proposing.
- What is the timeline for a first pilot or POC?
- Who has final approval on spend?

### 1.5 Azure Environment

- What Azure services is Lam currently paying for?
- This determines whether key services (Azure Purview, AI Foundry, AI Search, Cognitive Services) are immediately available or require new procurement cycles
- Procurement lead time for new Azure services at a company of Lam's size could add weeks or months. Knowing the current footprint avoids surprises.

---

## Priority 2: What Requires the Daniel Technical Call

These questions require someone who understands the technical stack, can name specific Azure services, and can describe the prior work at an engineering level. Daniel is the identified technical lead.

### 2.1 Full Autopsy of Prior Technical Work

The discovery call established that models were tried and failed (20% false positive rate, fine-tuned to only 17%). The Daniel call needs to go deeper.

| Question | Why BayOne Needs This |
|----------|----------------------|
| What specific model architectures were tried? (Exact versions, configurations, not just "Transformers, SpaCy, Azure AI") | Determine whether the approach was fundamentally wrong or just poorly executed. If they used generic Named Entity Recognition (NER) out of the box, the failure was predictable. If they did substantial custom work and still failed, the problem is harder than it appears. |
| Who did the work? Internal team, Accenture, or both? | Assess the skill level that was applied. Internal data science team vs. Accenture consulting engagement implies very different baselines. |
| What was the golden standard or ground truth they tested against? | Understand if they even had a proper benchmark. Without a curated ground truth, the 20% false positive number may itself be unreliable. |
| What was the testing methodology? How were false positives calculated? | Determine if the 20% number is measured correctly. Were false positives calculated per-document, per-entity, per-field? |
| What was the test dataset -- size, composition, labeling quality? | Understand if the data was sufficient for the approach. Small or poorly labeled datasets produce unreliable results regardless of model quality. |
| How is the current system deployed? What infrastructure exists? | Understand what BayOne is replacing vs. building from scratch. Existing infrastructure may be reusable. |
| What does the end-to-end pipeline look like today? | Map the full flow from document ingestion to detection output. Identifies integration points and dependencies. |

### 2.2 Accenture Involvement (Critical Context)

The debrief (Document Set 02a) identified Accenture as a prior vendor. Understanding what happened with Accenture is essential to avoid repeating the same failure.

| Question | Why BayOne Needs This |
|----------|----------------------|
| What deliverables did Accenture produce? | Understand what exists vs. what was abandoned. There may be reusable artifacts (labeled datasets, architecture documents, model artifacts). |
| How was the problem statement given to Accenture? Was it well-scoped or vague? | If the problem statement was vague, any vendor would struggle. BayOne needs to ensure it gets a clear, measurable problem statement before committing to a POC. |
| Did Lam provide Accenture enough information to succeed? | If the client side was the issue (insufficient context, unclear requirements, limited access to data), BayOne is at risk of the same outcome regardless of technical approach. |
| Why was the Accenture engagement ended? | Was it performance, budget, relationship, timeline, or strategic direction? Each reason implies different risk factors for BayOne. |

### 2.3 Top Applications at a Technical Level

The discovery call covered applications at a business level. The Daniel call needs to go deeper.

| Question | Why BayOne Needs This |
|----------|----------------------|
| Top 3 most important RAG-like applications, described technically | Scoping the control plane, prioritizing migration order |
| What systems does each application touch? (Databases, APIs, external services) | Architecture planning, integration scope |
| What data sources feed each application? | Understanding data overlap. Colin's hypothesis: these applications share data sources, which means the first migration is the hardest and each subsequent one is progressively easier. |
| Are the applications truly unique or variations of the same pattern? | Validates the "one project reused many times" theory from the technical approach discussion. If true, the control plane approach is strongly justified. |
| Which application has the highest business impact if the IP protection problem is solved for it? | POC selection. The first application should demonstrate maximum value to justify the platform investment. |

### 2.4 Organizational Reality Check

Brad's discovery call statements need technical-side verification.

| Question | Why BayOne Needs This |
|----------|----------------------|
| What is the actual technical governance structure? | Brad's version may not match reality. Daniel's perspective as a technical lead will reveal whether Brad's authority claims hold in practice. |
| Does IT or cybersecurity have veto power over new cloud services or data handling approaches? | Direct proposal risk. If IT must approve and has a 3-month review cycle, the timeline changes fundamentally. |
| Who controls infrastructure decisions? (Cloud provisioning, data residency, service selection) | Determines whether BayOne negotiates with Brad's org or with a separate IT function. |

### 2.5 The "2-5 Seconds" Clarification

Mikhail stated a 2-5 second performance requirement during the discovery call. This has at least two very different interpretations, and the architecture changes depending on which is correct.

| Interpretation | Architecture Implication |
|----------------|------------------------|
| 2-5 seconds for the upload to complete | No problem. Processing runs during the upload user experience. The user does not perceive a delay. Standard async queue with synchronous UX. |
| 2-5 seconds for the document to be RAG-ready (searchable, queryable) | Significantly harder constraint. Even ChatGPT takes more than 2 seconds between uploading a document and being ready for queries on it. Speed optimization is possible but changes the processing pipeline. |
| 2-5 seconds for a real-time detection notification | Different again. This is Use Case 2 (escalation detection), and the processing pipeline is shorter but the latency requirement is strict. |

The Daniel call must clarify which interpretation applies, or if different use cases have different latency requirements.

### 2.6 Infrastructure Details

| Question | Why BayOne Needs This |
|----------|----------------------|
| What Azure services are they actually paying for? | Determines available tooling without procurement. |
| What is on-premises vs. cloud today? | Architecture constraints, data movement considerations. |
| What is the data volume? (Documents per day, tickets per day, searches per day) | Validates or corrects the estimates from Priority 1. Technical leads typically have more accurate numbers than business owners. |

---

## Priority 3: What Requires Document Samples or Hands-On Access

These are needed for POC execution, not for proposal writing. They should be requested after a pilot or POC is greenlit.

### 3.1 Representative Documents

- A sample document of the type they are concerned about (even sanitized or synthetic)
- A sample support ticket with the kind of customer information that gets flagged
- Examples of the specific entities that need detection: customer names, fab identifiers (F11, Fab 11, FAB-11, etc.), site identifiers, process parameters
- These samples define the detection patterns and are essential for building the deterministic layer of the hybrid approach

### 3.2 Test Data for Validation

- Real false positive examples from their prior model testing (what was incorrectly flagged?)
- A small labeled dataset to benchmark BayOne's approach against the prior 20% false positive rate
- The specific "7th ticket with a violation" that Brad mentioned during the discovery call -- what did that actually look like? This is a concrete example that illustrates the detection challenge.

### 3.3 System Access

- API documentation for their ingestion endpoints
- Access to a non-production environment (if pilot is approved)
- Prior model training artifacts from the Accenture and/or internal effort (labeled data, model weights, configuration files)
- Architecture diagrams for the current pipeline

### 3.4 Governance Documentation

- Written policies for customer confidential information handling
- Customer contractual requirements around data segregation
- Current access control list (ACL) and role definitions in their systems
- Any compliance frameworks they must adhere to (export control, International Traffic in Arms Regulations (ITAR), etc.)

---

## Sequencing Table

| Step | Action | Owner | Gate | Notes |
|------|--------|-------|------|-------|
| 1 | Email Pat with Priority 1 questions (especially 1.1: name one application) | Anuj + Colin | None | Frame 1.1 as a business question, not a technical one. "Which application would benefit most from going first?" |
| 2 | Get Priority 1 responses from Lam | Pat / Anuj | Lam responsiveness | If 1.1 is again deflected as "too technical," escalate: this gates everything. |
| 3 | Schedule Daniel technical call | Anuj / Pat | Priority 1 answered (especially 1.1) | Do not schedule the Daniel call until the first application is named. The call is more productive with that context. |
| 4 | Conduct Daniel call: extract Priority 2 answers | Colin | Call scheduled | Colin leads the technical discussion. Bring the autopsy questions, the 2-5 second clarification, and the application deep-dive. |
| 5 | Assess findings and decide go/no-go on proposal | Colin | Daniel call completed | If the autopsy reveals the problem is client-side (insufficient data, vague requirements), BayOne must decide whether to proceed or not. |
| 6 | Write formal proposal and POC scope | Colin | Go decision from Step 5 | Informed by all priority levels. |
| 7 | Request Priority 3 items (samples, access, governance docs) | Colin via Pat | Pilot or POC greenlit | These are needed for execution, not for the proposal. |
| 8 | Build POC | Colin | Priority 3 items received | First application on the new architecture. |

---

## Questions for the Daniel Technical Call

### Autopsy Questions (What Happened Before)

These should be asked first. Understanding the prior work prevents BayOne from repeating the same mistakes.

1. **Models and approach:** What specific models were tried? We heard "Transformers, SpaCy, Azure AI" on the discovery call. What were the exact architectures, versions, and configurations? Were these out-of-the-box or custom-trained?

2. **Who did the work:** Was this done by an internal data science team, by Accenture, or by both in sequence? What was the team composition and skill level?

3. **Ground truth:** What was the golden standard dataset? How was it created? How many examples? Was it manually labeled, and if so, by whom?

4. **Testing methodology:** How was the 20% false positive rate calculated? Per-document, per-entity, or per-field? What was the test set size and composition? Was there a held-out validation set?

5. **The fine-tuning gap:** The rate went from 20% to 17% with fine-tuning. What kind of fine-tuning was attempted? How much labeled data was used? Why did it plateau?

6. **Rule-based attempt:** Rule-based models were abandoned due to spelling variations (F11, Fab 11, FAB-11, etc.). How comprehensive was the rule set? Was fuzzy matching attempted? Were regular expressions used?

7. **Current state:** What exists today? Is anything deployed, or was everything shelved? Is there a pipeline still running, or is it completely dormant?

8. **The 1,000-hour estimate:** Brad mentioned 1,000+ man-hours for the labeling exercise. Who made that estimate? Was it for labeling alone or for labeling plus model retraining?

### Forward-Looking Questions (What Comes Next)

These questions inform the proposal and POC design.

9. **First application:** Which application is the highest priority for the IP protection capability? What does it do, technically? What data sources feed it?

10. **Application overlap:** How much overlap exists between the data sources for different applications? If Application A and Application B both pull from the same document repository, protecting that repository protects both.

11. **Architecture vision:** Does Lam want a centralized platform (control plane model) or per-application solutions? The discovery call suggested evolutionary, not revolutionary -- does Daniel agree?

12. **The 2-5 second requirement:** Is this upload completion time, RAG readiness time, or real-time detection notification time? Which use case does it apply to?

13. **Document types:** What are the most common document types flowing through these systems? PDFs, Excel files, Word documents, plain text, code files, engineering drawings?

14. **Entity catalog:** Beyond customer names and fab identifiers, what other entity types need detection? Process parameters, yield data, equipment configurations, pricing information?

15. **Integration points:** What are the ingestion endpoints? REST APIs, file drops, SharePoint, email? Where do documents enter the system?

16. **Azure footprint:** What Azure services are currently provisioned and in use? Specifically: is Azure AI Foundry, AI Search, Purview, or Cognitive Services already available?

---

## Accenture Autopsy Questions

These are a subset of the Daniel call questions, separated here because they require particular care. The goal is to understand what happened without appearing to attack a prior vendor or make Lam feel defensive about their choice.

### Direct Questions for Daniel

1. **Scope:** What was Accenture brought in to do? Was it a defined project with clear deliverables, or an exploration?

2. **Deliverables:** What did Accenture actually produce? Models, code, architecture documents, labeled datasets, recommendations?

3. **Problem definition:** How was the problem statement given to Accenture? Was it the same level of specificity that Mikhail presented on the discovery call, or was it broader or vaguer?

4. **Data access:** Did Accenture have access to representative data? Could they work with real documents, or were they limited to synthetic or sanitized samples?

5. **Timeline and team:** How long was the engagement? How many people were on the Accenture team? What were their roles?

6. **Outcome:** Why did the engagement end? Was it a planned conclusion, a performance issue, a budget decision, or a strategic pivot?

7. **Reusable artifacts:** Is anything from the Accenture engagement still in use or available? Labeled datasets, model artifacts, architecture documents, or lessons learned documentation?

### Why These Questions Matter for BayOne

Every answer maps to a risk factor:

| Answer Pattern | Risk Implication |
|----------------|------------------|
| Vague problem statement given to Accenture | BayOne must insist on precise scoping before committing. Same vagueness leads to same outcome. |
| Limited data access for Accenture | BayOne must secure data access as a precondition for the POC, not an afterthought. |
| Short engagement with large scope | BayOne must right-size the POC scope and set expectations for what is achievable in a pilot. |
| Engagement ended due to poor results | Validates that the prior technical approach was wrong, not that the problem is unsolvable. Good signal for BayOne's hybrid approach. |
| Engagement ended due to client-side issues | Red flag. If Lam could not provide sufficient support for Accenture to succeed, BayOne faces the same risk. |

---

## Competitive Positioning Questions (Diplomatic Framing)

These questions are designed to extract information about the prior vendor engagement without naming Accenture directly. Use these framings in conversations with Brad or Mikhail (non-technical stakeholders) rather than the direct questions above (which are for Daniel).

1. **"What did you learn from the prior engagement that should inform our approach?"** -- Invites Lam to share lessons without putting them on the defensive about a vendor choice.

2. **"Were there organizational barriers that made the prior effort harder than it needed to be?"** -- Surfaces client-side issues (data access, governance, stakeholder alignment) without blaming anyone.

3. **"Is there prior work product we should review before starting, to avoid duplicating effort?"** -- Gets access to Accenture deliverables without implying they were inadequate.

4. **"What would success look like this time that is different from what was attempted before?"** -- Establishes new success criteria and implicitly asks what went wrong.

5. **"If we get to the same point the prior effort reached, what would you want us to do differently from there?"** -- Acknowledges prior work was not worthless, but asks for the specific gap.

6. **"Were there constraints in the prior effort -- timeline, data access, team composition -- that you would change if you could?"** -- Extracts root cause without blame.

---

## Summary of Information Gaps by Category

| Category | What We Know | What We Need |
|----------|-------------|-------------|
| **First application** | Multiple RAG-like applications exist, at least 6 search systems, fragmented landscape | The name and description of one specific application to target first |
| **Prior technical work** | Models tried (Transformers, SpaCy, Azure AI), 20% false positive rate, fine-tuned to 17%, rule-based abandoned, 1,000-hour labeling estimate | Exact architectures, who did the work, ground truth quality, testing methodology, current deployment state |
| **Accenture** | They were involved (confirmed in debrief) | Scope, deliverables, problem definition quality, data access, outcome, reusable artifacts |
| **Data volumes** | "Tons of data," multiple systems, heavy ticket volume implied | Documents per day, tickets per day, queries per day, user count |
| **Authority** | Brad claims end-to-end ownership | Verification from technical side, IT/security veto power, infrastructure decision authority |
| **Budget** | No framework exists (1,000 man-hours comment implies ad hoc thinking) | Budget range, timeline, approval authority |
| **Azure environment** | Azure cloud is in use, MLOps on Azure mentioned | Specific services provisioned, what is available vs. what requires procurement |
| **Performance requirements** | 2-5 seconds stated by Mikhail | Clarification of what the 2-5 seconds applies to (upload, RAG readiness, or detection notification) |
| **Document types** | Support tickets, customer data, fab identifiers mentioned | Representative samples, entity catalog, document type distribution |
| **Governance** | Over-restriction is the current approach, ACLs exist but IAM is immature (~2 years in) | Written policies, contractual requirements, compliance frameworks |
