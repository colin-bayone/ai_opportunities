# 03 - Discussion: Technical Approach

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Post-meeting analysis, informed by Sets 01, 02, and 02a

---

## 1. Discard Everything Lam Has Tried

Colin's assessment is unequivocal: everything Lam has attempted so far should be discarded as a starting point for the approach. Their prior work reflects a fundamental misunderstanding of the problem and the tools available.

**What they tried and why it's wrong:**

- **Custom Transformers model for semantic similarity between name variations** (e.g., Fab11 vs. F11). This is using a sledgehammer for a thumbtack. They have a finite list of customers with a finite set of naming variations. Training a custom ML model for this is the wrong tool entirely -- this is a deterministic lookup problem, not a semantic similarity problem.

- **SpaCy for NER.** Without a proper test set to work with, SpaCy NER is not going to do anything useful out of the box for domain-specific entities like semiconductor fab names.

- **Azure AI model.** They don't even know what Azure AI services they were using. The "Azure AI model" reference likely means they were using models hosted in Azure, not that they were leveraging any specific Azure AI service designed for this purpose. They may have been training sentence transformers locally on a GPU and thinking that fine-tuning would somehow make them good for classification.

- **Rule-based models abandoned due to spelling variations.** They gave up too early on what is actually part of the right approach. The variations are finite and enumerable -- Fab11, F11, Micro 11, FAP 11, FAP-11. A synonyms lookup table handles this. You don't need AI for this piece.

**Colin's core point:** These are intern-level AI projects. The team that attempted them has no technical depth in this area. The 1,000+ hour labeling exercise confirms this -- they don't know what the right approach looks like, so they're estimating effort for the wrong approach.

**Colin's confidence level:** "As a data scientist and AI engineer, I could probably get them to 95%+ with about a day's worth of effort if I had a representative sample with nothing more than regex." This is not bravado -- the problem, when correctly framed, is genuinely not that hard.

---

## 2. The Right Approach: Hybrid AI + Deterministic Logic

The approach should be a hybrid system, not pure AI and not pure rules:

**Deterministic components:**
- **Synonyms lookup table** for known customer names, fab identifiers, and their variations. This is a finite set that can be enumerated and maintained.
- **Regex patterns** for structured identifiers (fab numbers, customer codes, site identifiers) that follow predictable formats even with variation.
- **Keyword/entity lists** maintained as configuration, not model weights.

**AI components:**
- For **contextual sensitivity** -- determining whether a mention is sensitive in context (e.g., "TSMC" in a public discussion vs. "TSMC yield rate for Q4").
- For **unstructured text analysis** where deterministic patterns can't reach -- freeform descriptions, meeting transcripts, problem statements where the sensitive information is embedded in natural language.
- For **classification at the document level** -- is this document likely to contain customer-specific IP that needs review?

**Why hybrid:** The deterministic pieces give you the sub-1% false positive rate on known patterns (zero false positives, actually, because it's exact matching). The AI pieces handle the gray areas that can't be enumerated. Together, you get accuracy that neither approach achieves alone.

---

## 3. Reframing: The Entire Use Case Is a RAG Chatbot

**Critical correction to Set 02's framing:**

Mikhail's two "separate swim lanes" (real-time detection at entry, batch redaction on stored content) created the impression that this is a complex multi-system problem. Colin's reframe: the entire use case is a RAG chatbot. Everything Mikhail described -- people interacting with documents, uploading content, doing Q&A, searching across knowledge bases -- is a RAG system.

The detection and redaction "swim lanes" are not separate products. They are features of a properly designed ingestion pipeline within a RAG architecture:

- **"Real-time detection at entry"** = the ingestion pipeline validates content before storing it
- **"Batch redaction on stored content"** = reprocessing historical data through the same pipeline

These are the same system at different points in time.

**Why "real-time detection" is the wrong framing:**

Mikhail described real-time detection as: notify the user in 2-5 seconds that they may be violating IP policy. Colin's counterpoint: why detect and notify when you can simply reject at ingestion?

If a user uploads a document riddled with customer IP, the system doesn't need to say "hey, you might have a problem." It should say: "Document rejected. It contains the following flagged content: [list]. Please upload a version with this information removed."

The polluted information never enters the knowledge base. No detection needed downstream because the contamination never happened.

**This eliminates the batch redaction problem almost entirely.** If the ingestion pipeline works, new content entering the system is clean. The only batch work is a one-time cleanup of historical data already in the system.

---

## 4. Ingestion-First Architecture

Colin's philosophy: if ingestion is done right, you don't need downstream redaction.

**The pipeline:**
1. User submits a document (or text, or transcript, etc.)
2. Ingestion pipeline analyzes the content for customer-identifiable information
3. If flagged: reject back to user with specifics. "This document contains references to [Customer X] fab identifiers. Please remove and resubmit."
4. If clean: store in the knowledge base, available for RAG queries
5. Content in the knowledge base is guaranteed clean by construction

**What this means for the two "swim lanes":**
- **Detection at entry** becomes **rejection at ingestion** -- a stronger, simpler mechanism
- **Batch redaction** becomes **historical data cleanup** -- a one-time project, not an ongoing operational burden

---

## 5. Historical Data Cleanup Strategy

Once the ingestion pipeline works, existing contaminated data needs to be addressed. Colin identifies two types:

### Type A: Live Data Sources (Databases, APIs)

Data that comes from a live, queryable source -- not a static snapshot. For these:
- Identify the patterns in the data (customer names, fab IDs, etc.)
- Determine the redaction strategy (mask, replace, flag)
- This is a live query to a live source, so the approach is different from document processing
- The redaction may need to happen at query time rather than at storage time

### Type B: Static Snapshots (Documents, Procedures, Transcripts)

Data that exists as a point-in-time artifact -- uploaded docs, historical procedures, meeting transcripts. For these:
- Re-ingest through the new filter system for flagging
- Transition one RAG application at a time to the new system
- Each application gets a "day zero" where everything in its knowledge base has been re-identified
- Clean as you go, application by application -- don't try to do it all at once

**Sequencing:** Build the ingestion pipeline first (handles all new content). Then use it to clean historical data, one application at a time. This is evolutionary, exactly what Brad asked for.

---

## 6. Unified Control Plane Architecture

**What it is:** A middleware platform layer that unifies:
- Document storage
- Knowledge bases
- Credentials and access for knowledge bases
- Ingestion pipelines (including the detection/rejection logic)
- Standard interface from which different RAG applications connect

**May include:**
- Vector stores (for RAG embeddings)
- Blob storage (for raw documents)
- Built on enterprise software (Azure services, not custom infrastructure)

**Why it must be cloud-unified:**

Lam currently has a mix of on-prem, cloud, LamGPT, Copilot, cloud bots, and "anything you can think of." Colin's position: they need to unify. Building a separate control plane for each application is completely non-scalable and provides no central governance.

Even for on-prem applications that are not hosted in the cloud, they can still leverage cloud AI models (Azure AI Foundry) for processing. The compute doesn't have to be local just because the application is.

**Unknown:** We still don't know what specific applications Lam has. They keep saying they have "a bunch of tools" but have not named a single one beyond generic descriptions. What is most likely: they have a project that was reused/forked multiple times. They keep saying "a ton" but we don't have a count, and they have yet to provide a single specific use case.

---

## 7. Why Their ML Approaches Failed

The team that presented to us was non-technical. The ML failure is almost certainly because:

1. **They were training custom models from scratch** for a problem that doesn't require custom models. Training a sentence transformers model to recognize "Fab11" vs. "F11" is the wrong abstraction entirely.

2. **They had no proper test set.** SpaCy NER requires labeled training data. Without it, you get generic entity recognition that doesn't know domain-specific entities.

3. **"Azure AI model" was likely just a model hosted on Azure**, not a purpose-built Azure AI service. They may not have been using any of the enterprise tools designed for this type of problem.

4. **20% false positive = out-of-the-box ChatGPT** means their "training" added no value over baseline. The fine-tuning from 20% to 17% confirms this -- negligible improvement means the training data or approach was fundamentally flawed.

5. **The approach itself was wrong.** You don't solve "is this text mentioning a customer?" with semantic similarity. For known entities (customer names, fab IDs), you use deterministic matching. For contextual sensitivity, you use a well-prompted LLM, not a custom-trained classifier.

---

## 8. Enterprise Tools Strategy

**Core philosophy:** Push Lam toward enterprise tools that are manageable and maintainable, rather than reinventing the wheel. These are largely solved problems.

### Microsoft Purview

Relevant for:
- Data classification and sensitivity labeling
- DLP (Data Loss Prevention) policies
- Content detection for sensitive information types
- Can define custom Sensitive Information Types for domain-specific entities

**Caveat:** Only works if they move things to the cloud. If everything stays on-prem with fragmented systems, Purview can't see it.

### Azure AI Foundry

Relevant for:
- Hosting and deploying AI models for the RAG system
- Providing the compute layer for document processing
- Even on-prem applications can call Azure AI Foundry APIs for processing

**The push should always be:** Move to enterprise tools. Unify on Azure. Use purpose-built services instead of training custom models. These tools exist precisely because the problems Lam is facing are common, and they are designed to solve them at enterprise scale.

### Research Needed

Both Azure AI Foundry and Microsoft Purview should be thoroughly researched in the context of:
- RAG chatbot architectures with sensitivity controls
- Custom Sensitive Information Types for domain-specific entities
- DLP integration with AI ingestion pipelines
- How Purview handles the kind of entity variation Lam faces (Fab11, F11, etc.)
