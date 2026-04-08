# 03 - Discussion: Technical Approach

**Source:** /lam_research/ip_protection/source/prior_discussion_technical_approach_2026-03-20.md (and 3 related files)
**Source Date:** 2026-03-20 (Working discussion between Colin Moore and Claude)
**Document Set:** 03 (Prior Working Discussion)
**Pass:** Consolidated technical approach from 4 source documents

---

## 1. Why Every Prior Approach Was Wrong

Colin's assessment is unequivocal: everything Lam has attempted should be discarded as a starting point. Their prior work reflects a fundamental misunderstanding of the problem and the tools available.

### 1.1 Custom Transformers Model for Semantic Similarity

Lam trained a custom Transformers model to detect semantic similarity between name variations (e.g., Fab11 vs. F11). This is using a sledgehammer for a thumbtack. They have a finite list of customers with a finite set of naming variations. Training a custom ML model for this is the wrong tool entirely -- this is a deterministic lookup problem, not a semantic similarity problem.

### 1.2 SpaCy for NER

Without a proper test set, SpaCy NER does nothing useful out of the box for domain-specific entities like semiconductor fab names. Generic NER models do not know "Fab11" or "TSMC yield rate" as sensitive entities. This was never going to work without extensive domain-specific training data -- which they did not have.

### 1.3 "Azure AI Model"

Lam's team does not even know which Azure AI services they were using. The "Azure AI model" reference likely means they were using models hosted in Azure, not that they were leveraging any purpose-built Azure AI service designed for this type of problem. They may have been training sentence transformers locally on a GPU and thinking that fine-tuning would somehow make them good for classification.

### 1.4 Rule-Based Models Abandoned Prematurely

They gave up too early on what is actually part of the right approach. The variations are finite and enumerable -- Fab11, F11, Micro 11, FAP 11, FAP-11. A synonyms lookup table handles this. You do not need AI for this piece. The team's conclusion that spelling variations made rules impractical reveals they did not think through the problem correctly.

### 1.5 The 20% to 17% Fine-Tuning Trajectory

The fine-tuning progression from 20% to 17% false positive rate confirms the fundamental problem. A 3 percentage point improvement over baseline means the training data or approach was fundamentally flawed. As Colin diagnosed on the discovery call, 20% is out-of-the-box ChatGPT performance -- the fine-tuning added no value over baseline.

### 1.6 The 1,000+ Hour Labeling Exercise

The scoped labeling effort confirms the team does not know what the right approach looks like. When you estimate 1,000+ hours of labeling for a problem that is substantially solvable with deterministic matching, you are estimating effort for the wrong approach.

### 1.7 Colin's Confidence Assessment

"As a data scientist and AI engineer, I could probably get them to 95%+ with about a day's worth of effort if I had a representative sample with nothing more than regex."

**Critical caveat:** The "95% in a day" statement is hyperbole to illustrate that the problem is not as hard as Lam thinks. It is not a timeline commitment. It must never be referenced in proposals, discussions, or planning documents. The point is feasibility, not schedule.

---

## 2. The Right Approach: Hybrid Deterministic + AI Architecture

The approach is a hybrid system -- not pure AI and not pure rules. Each layer handles what it is best suited for, and the combination achieves accuracy that neither approach achieves alone.

### 2.1 Deterministic Components

- **Synonyms lookup table** for known customer names, fab identifiers, and their variations. This is a finite set that can be enumerated and maintained as configuration.
- **Regex patterns** for structured identifiers (fab numbers, customer codes, site identifiers) that follow predictable formats even with variation.
- **Keyword/entity lists** maintained as configuration, not model weights.

The deterministic pieces give a sub-1% false positive rate on known patterns -- zero false positives, actually, because it is exact matching. When a customer name is in the lookup table, the match is binary. There is no probability involved.

### 2.2 AI Components

- **Contextual sensitivity determination** -- whether a mention is sensitive in context. "TSMC" in a public discussion is different from "TSMC yield rate for Q4."
- **Unstructured text analysis** where deterministic patterns cannot reach -- freeform descriptions, meeting transcripts, problem statements where sensitive information is embedded in natural language.
- **Document-level classification** -- is this document likely to contain customer-specific IP that needs review?

The AI pieces handle the gray areas that cannot be enumerated. They address the contextual judgment that regex and keyword lists fundamentally cannot perform.

### 2.3 Why Hybrid

Neither approach alone is sufficient:
- Deterministic alone fails on context and unstructured content (which is why Lam abandoned rules).
- AI alone produces the 20% false positive rate they already experienced (which is why they paused ML efforts).
- Combined, deterministic matching handles the known patterns with zero false positives, and AI handles the contextual and unstructured content where human judgment is needed.

### 2.4 Competitive Positioning of the Hybrid Approach

The prior approach is a known pattern with known limitations. Custom model training for classification is well-understood but fragile. It requires extensive training content, becomes very static, and cannot respond to dynamic, robust conditions. If it was to be successful, it would need the massive labeled dataset and continuous maintenance that their 1,000+ hour estimate revealed.

The hybrid approach offers:
- **Cost and speed advantage of deterministic systems** (known patterns match instantly, zero false positives on exact matches)
- **Power and flexibility of AI-based systems** for contextual analysis -- not just NLP but agentic AI and capabilities built into Azure AI Foundry
- **Enterprise tools from the start** because we are thinking strategically beyond one problem statement

**Positioning note:** Do not call out Accenture by name or throw shade at another company. Frame the prior approach as "our understanding of the prior approach" and position it as a common but brittle pattern. Say "from what we've heard, this approach addresses the specific failure modes described" -- not "your prior approach was wrong."

---

## 3. The RAG Chatbot Reframing

### 3.1 The Problem with Mikhail's Two Swim Lanes

Mikhail presented two "separate swim lanes" in the discovery call: (1) real-time detection at entry, and (2) batch redaction on stored content. This created the impression of a complex multi-system problem with two distinct product requirements.

Colin's reframe: the entire use case is a RAG chatbot. Everything Mikhail described -- people interacting with documents, uploading content, doing Q&A, searching across knowledge bases -- is a RAG system. The detection and redaction "swim lanes" are not separate products. They are features of a properly designed ingestion pipeline within a RAG architecture.

### 3.2 The Two Swim Lanes Are One Pipeline at Different Points in Time

- **"Real-time detection at entry"** = the ingestion pipeline validates content before storing it
- **"Batch redaction on stored content"** = reprocessing historical data through the same pipeline

These are the same system at different points in time. The code, the logic, the detection rules, the AI classification -- all identical. The only difference is whether the content is new (going through ingestion for the first time) or old (being re-ingested for cleanup).

### 3.3 The Technical Reality Lam Is Missing

Detection is a necessary step for redaction. You cannot redact something if you have not detected/identified it first. Redaction is simply an extra step after detection. They are separating things that are technically the same pipeline -- detect, then decide what to do (flag, reject, redact, quarantine). The fact that they frame these as separate business cases reveals they have no technical concept of how this actually works.

### 3.4 How to Handle the Reframing

We do not take them to school. We do not say "you are wrong." We reframe based on our experience, coming from a position of authority where we have done this before. The approach document should restate the problem using Mikhail's language and structure first (demonstrating we listened), then show our approach, which naturally corrects the framing. The unified pipeline where detection feeds into action makes the "two swim lanes" just become two modes of the same system.

---

## 4. Ingestion-First Philosophy

### 4.1 Core Principle

If ingestion is done right, you do not need downstream redaction.

### 4.2 Why "Real-Time Detection" Is the Wrong Framing

Mikhail described real-time detection as: notify the user in 2-5 seconds that they may be violating IP policy. Colin's counterpoint: why detect and notify when you can simply reject at ingestion?

If a user uploads a document riddled with customer IP, the system does not need to say "hey, you might have a problem." It should say: "Document rejected. It contains the following flagged content: [list]. Please upload a version with this information removed."

The polluted information never enters the knowledge base. No detection needed downstream because the contamination never happened.

### 4.3 The Pipeline

1. User submits a document (or text, or transcript, etc.)
2. Ingestion pipeline analyzes the content for customer-identifiable information
3. If flagged: reject back to user with specifics. "This document contains references to [Customer X] fab identifiers. Please remove and resubmit."
4. If clean: store in the knowledge base, available for RAG queries
5. Content in the knowledge base is guaranteed clean by construction

### 4.4 Impact on the Two Use Cases

- **Detection at entry** becomes **rejection at ingestion** -- a stronger, simpler mechanism
- **Batch redaction** becomes **historical data cleanup** -- a one-time project, not an ongoing operational burden

This eliminates the batch redaction problem almost entirely. If the ingestion pipeline works, new content entering the system is clean. The only batch work is a one-time cleanup of historical data already in the system.

### 4.5 Automated Content Entry

Some content enters the system automatically (e.g., Teams meeting transcripts auto-attached to tickets). There is no human in the loop to clean and resubmit when the system rejects.

This requires discovery with Lam's team -- we cannot prescribe the right solution without representative samples. However, the general approach:

- **Text-based content (transcripts, text fields, simple documents):** Can be cleaned with an agentic AI cleaning tool. A well-defined process where the system identifies flagged content, proposes cleaned versions, and resubmits automatically. This is feasible for simple content types.
- **Complex documents (PDFs, PowerPoints):** We are NOT in the business of trying to redact these in real-time. This is impractical on day one.
- **The evolutionary approach:** We do not need to say on day one that all document types can be cleaned across all topics. Start with a representative sample set of documents. Test on that. Verify it is good, traceable, and trackable. Then expand capability over time.

---

## 5. The Layered Architecture: Purview + AI + Control Plane

### 5.1 Layer 1: Deterministic (Microsoft Purview)

- Custom Sensitive Information Types for known entities (customer names, fab IDs, variations)
- Regex and keyword matching
- Always on, regardless of what systems are using it
- Zero false positives on known patterns

### 5.2 Layer 2: AI / Contextual Classification

- Handles the gray areas Purview cannot: "Is 'TSMC' sensitive in this specific context?"
- Document-level classification
- Natural language analysis for unstructured content
- Faster than expected -- not a 20-minute wait. AI classification can run quickly, even on uploaded documents.

### 5.3 Layer 3: Unified Control Plane

- Wraps Layer 1 and Layer 2 into a single standard interface
- An end user or application makes one call to the data plane
- The data plane already has Purview built in, already has the AI layer built in
- The layers are **indistinguishable to the end user** -- they just see "clean/not clean"

### 5.4 The Key Selling Point

The end user (or the RAG application) does not know or care whether a detection came from a regex rule in Purview or an AI classification model. They make one API call to the control plane. The control plane handles the routing, the detection, the classification, and the decision. This is the unified experience.

---

## 6. Unified Control Plane Architecture

### 6.1 What It Is

A middleware platform layer that unifies:
- Document storage
- Knowledge bases
- Credentials and access for knowledge bases
- Ingestion pipelines (including the detection/rejection logic)
- Standard interface from which different RAG applications connect

### 6.2 What It May Include

- Vector stores (for RAG embeddings)
- Blob storage (for raw documents)
- Built on enterprise software (Azure services, not custom infrastructure)

### 6.3 Why It Must Be Cloud-Unified

Lam currently has a mix of on-prem, cloud, LamGPT, Copilot, cloud bots, and "anything you can think of." They need to unify. Building a separate control plane for each application is completely non-scalable and provides no central governance.

Even for on-prem applications that are not hosted in the cloud, they can still leverage cloud AI models (Azure AI Foundry) for processing. The compute does not have to be local just because the application is.

### 6.4 Build vs. Configure: Two Options

**Option 1: All existing Azure services**
- Azure Blob Storage, Azure AI Search, Azure Cosmos DB, Azure AI Foundry, Microsoft Purview
- Maximum compliance, maintainability, administrable by non-technical people
- Enterprise-grade from day one

**Option 2: Primarily Azure services with custom backend where needed**
- Core infrastructure on Azure (Blob Storage, Azure Postgres + pgvector, etc.)
- Custom components for things that do not work well or are cost-prohibitive in Azure
- Example: Azure AI Search may be cost-prohibitive or provide insufficient value for certain RAG use cases. In those cases, build a custom vector search on Azure Postgres + pgvector, while still using Azure Blob Storage for documents.

### 6.5 Decision Framework

- Always start with enterprise solutions first. Compliance, maintainability, and enabling non-technical administration are the priorities.
- Fall back to custom only when justified -- cost-prohibitive, insufficient capability, or specific implementation needs that Azure services do not cover.
- Cost is situational. Just because something is on Azure does not make it expensive. Just because something is off Azure does not make it cheap.
- We cannot prescribe without knowing the situation. The right answer depends on what their specific applications look like, their data volumes, their query patterns, and their budget constraints.

### 6.6 The "One Project Forked Many Times" Clarification

Lam probably has a single RAG concept that was re-used across multiple applications (not literally a GitHub fork). The pattern is the same even if the implementations differ. The control plane would unify the common backend of this repeated pattern.

### 6.7 The Control Plane Is a Project, Not a Product

It is a **custom build for Lam**, tailored to their environment, their data sources, and their specific needs. It is a consulting engagement: "we will come in, get this set up for you, and we are more than happy to provide long-term support and build off of this."

It is NOT:
- A product sitting in BayOne's back pocket ready to deploy
- An out-of-the-box solution
- A one-size-fits-all platform
- Something that already exists that magically solves any problem

**How to describe it:** Always call it a "solution," never a "product." "A tailor-made solution using the same methodology and blueprint as has been applied at previous customers." Every client's environment is drastically different -- the methodology is reusable, the implementation is custom.

Colin has built similar architectures for Coherent Corp (massive global enterprise, many teams across finance, engineering, sales, service, manufacturing), a retail customer (Salesforce-based, completely different stack), and an Oracle Cloud customer (different cloud, different use case). Each was custom. The pattern and expertise transfer; the code does not.

---

## 7. Historical Data Cleanup Strategy

### 7.1 Day Zero and Day One Terminology

- **Day Zero:** The day when everything is done and ready to be reprocessed. The system is built, the ingestion pipeline works, the detection rules are validated. Day zero is the starting gun, not the finish line.
- **Day One:** The first day after day zero where the application goes online with the new system after all historical data has been processed. This is NOT necessarily the calendar day after day zero -- it is a milestone, not a date.

### 7.2 Two Types of Historical Data

**Type A: Live Data Sources (Databases, APIs)**

Data that comes from a live, queryable source -- not a static snapshot. For these:
- Identify the patterns in the data (customer names, fab IDs, etc.)
- Determine the redaction strategy (mask, replace, flag)
- This is a live query to a live source, so the approach differs from document processing
- The redaction may need to happen at query time rather than at storage time

**Type B: Static Snapshots (Documents, Procedures, Transcripts)**

Data that exists as a point-in-time artifact -- uploaded docs, historical procedures, meeting transcripts. For these:
- Re-ingest through the new filter system for flagging
- Transition one RAG application at a time to the new system
- Each application gets a "day zero" where everything in its knowledge base has been re-identified
- Clean as you go, application by application -- do not try to do it all at once

### 7.3 What Happens During Reprocessing (Between Day Zero and Day One)

1. Historical data is re-ingested through the new filter system
2. Flagged content is **quarantined** and surfaced for human review
3. Auto-cleanable content (text, transcripts) may be cleaned automatically by the agentic AI cleaning tool
4. Content is **blocked from the RAG index** until addressed
5. AI classification and categorization assists so that humans are NOT reviewing each and every file individually

### 7.4 Business Decision, Not Technical Decision

Whether flagged content is quarantined, auto-redacted, or blocked is ultimately Lam's call. BayOne provides guidance and recommendations, but Lam controls this decision. Recommendation: block from RAG index until resolved, with AI-assisted categorization to minimize human review burden.

### 7.5 Sequencing

Build the ingestion pipeline first (handles all new content). Then use it to clean historical data, one application at a time. This is evolutionary, exactly what Brad asked for.

### 7.6 Framing for the Proposal

This needs to sound achievable and AI-enabled:
- "AI-enabled with minimal human intervention except where needed"
- Not a massive manual review project
- The system does the classification and categorization work
- Humans only intervene for edge cases and business judgment calls
- One application at a time, clean as you go

---

## 8. Application-by-Application Migration

### 8.1 The Governance Gap Objection

During migration, some applications are on the new platform and some are not. This creates a governance gap. But the governance gap already exists today. Lam has 6+ search systems, no unified data lake, no unified governance, and over-restriction as a blunt instrument. Moving one application to the new system does not make the gap worse -- it makes one piece of it better.

### 8.2 Why Not Big Bang

A massive all-at-once transition would:
- Unnecessarily delay everything
- Prevent early testing and validation
- Require coordinating across all applications simultaneously
- Be the "revolutionary" approach that Brad explicitly rejected

The application-by-application approach is:
- Evolutionary (Brad's word)
- Enables early testing
- Reduces risk
- Each migration reduces the remaining workload proportionally

### 8.3 Shared Data Sources Reduce Marginal Effort

These RAG applications likely do NOT have truly unique data sources. As more applications come online in the new system, the workload decreases proportionally because the data sources are shared. The first application is the hardest. Each subsequent one is easier.

### 8.4 Reject Ad-Hoc Per-App Customization

Colin explicitly rejects trying to build custom solutions for each individual Q&A bot. That is duplication of effort and not worth our time. The whole point of the control plane is that it is a unified architecture. New applications get pulled into the existing platform, not given bespoke treatment.

We can help Lam plan new system integrations to pull additional applications into the architecture, but the architecture itself does not change per app.

---

## 9. Async Queue Architecture with Synchronous UX

### 9.1 Queue for Robustness, Not for Batching

The processing architecture is an async queue, but the user experience is effectively synchronous:
- The queue exists for robustness (scalability, retry logic, fault tolerance)
- In practice, the queue never actually forms -- documents process in seconds
- Leverages Azure for scale

### 9.2 User Experience

- User clicks upload
- Upload screen appears ("uploading...")
- While the upload screen is showing, all processing runs (deterministic checks, AI classification)
- If clean: document enters the knowledge base, user proceeds
- If rejected: user gets a message back with specifics -- in the UI, via notification, whatever the system supports

### 9.3 The "2-5 Seconds" Requirement Needs Clarification

Colin wants to understand the actual motivation behind Mikhail's 2-5 second requirement:
- **If it is 2-5 seconds for the upload itself:** No problem. The processing happens during the upload UX. User does not even perceive a delay.
- **If it is 2-5 seconds to start doing RAG on the document:** That is a different constraint entirely. Even ChatGPT takes more than 2 seconds between uploading a document and being ready for RAG queries on it. Speed optimization is possible but we need to understand the actual use case.

---

## 10. Document-Type-Aware Processing

The best approaches are NOT one-size-fits-all. The system should be aware of document types:

- **Excel file:** Processed differently than a PDF or a transcript. Different patterns, different extraction logic.
- **Known offender users:** If a user has a history of uploading flagged content, apply greater scrutiny. Normal checks still run, but the AI layer can apply elevated attention.
- **Content type routing:** Different document types route to different processing pipelines within the same queue.

Text pattern matching does not change between file types, but if the context or structure of documents is drastically different, the system needs to see what the things that should be caught look like in each context.

---

## 11. Enterprise Tools Strategy

### 11.1 Core Philosophy

Push Lam toward enterprise tools that are manageable and maintainable, rather than reinventing the wheel. These are largely solved problems.

### 11.2 Microsoft Purview

Relevant for:
- Data classification and sensitivity labeling
- DLP (Data Loss Prevention) policies
- Content detection for sensitive information types
- Can define custom Sensitive Information Types for domain-specific entities

**Caveat:** Only works if they move things to the cloud. If everything stays on-prem with fragmented systems, Purview cannot see it.

### 11.3 Azure AI Foundry

Relevant for:
- Hosting and deploying AI models for the RAG system
- Providing the compute layer for document processing
- Even on-prem applications can call Azure AI Foundry APIs for processing

### 11.4 The Push

The push should always be: move to enterprise tools. Unify on Azure. Use purpose-built services instead of training custom models. These tools exist precisely because the problems Lam is facing are common, and they are designed to solve them at enterprise scale.

### 11.5 Research Still Needed

Both Azure AI Foundry and Microsoft Purview need thorough research in the context of:
- RAG chatbot architectures with sensitivity controls
- Custom Sensitive Information Types for domain-specific entities
- DLP integration with AI ingestion pipelines
- How Purview handles the kind of entity variation Lam faces (Fab11, F11, etc.)

---

## 12. Dashboard, Reporting, and Governance as Control Plane Features

### 12.1 Architecture Decision

The metrics/insights layer is a dashboard and reporting module built directly into the control plane, not a separate system. This gives leadership visibility into:

- **Governance metrics:** Rejection rates, flagged content patterns, compliance trends
- **Usage metrics:** How much people are actually using the tools -- super valuable to leadership because right now, with fragmented systems, there is no possible way they are tracking usage and understanding actual business value
- **User behavior insights:** Known offenders, repeat flagging, training gap identification
- **Business value demonstration:** The tools' actual impact, not just a guess with leadership support

### 12.2 Metrics as a Core Requirement

The system should track and report:
- Rejection rates (how often are documents being flagged?)
- Patterns in rejections (is it too strict? Are specific users/groups consistently flagging?)
- User behavior insights (are people fundamentally misunderstanding compliance requirements?)
- Segmentation and demographics around rejection patterns

If users are constantly uploading and constantly getting flagged, the system should be intelligent enough to surface whether: (1) the detection rules are too strict (system problem), or (2) people have a knowledge gap that could be resolved by compliance training (people problem). These insights are derivable from the data if we store rejection events, flagged content types, user segments, and outcomes. This is a major value-add beyond just "we built a filter."

### 12.3 Data Layer, Not Dashboard Lock-In

The underlying data is stored regardless of how it is consumed. Multiple consumption options:
- BayOne-built dashboard within the control plane (default offering)
- Integration with existing BI tools (Tableau, Power BI, whatever Lam uses) -- completely fine
- BayOne builds the dashboard using their tools -- also fine

Colin's philosophy: "It's just data. If we store it, it doesn't really matter if we're building the dashboard or if they are, or if we are for them with their tools. It's all the same."

### 12.4 The Selling Point

This goes beyond governance into business intelligence about AI tool adoption. Leadership currently has no visibility into whether their RAG applications are actually delivering value. The control plane solves this as a side effect of existing there. This is a cohesive, holistic solution -- not just a filter bolted onto a chatbot.

---

## 13. Representative Sample Requirements

### 13.1 What "Representative Sample" Means

A selection of documents (not one file type, not one file) that give us a view into what people are using the system for day-to-day. Must include:

- **Failure cases:** Documents that contain the kind of content that should be caught. We cannot detect things if we do not have examples of what to catch.
- **Known good examples:** Documents that are clean and should pass through without flagging. This is the gold standard.
- **Both are required.** We need the good and the bad to calibrate.

### 13.2 Not Just Documents

The sample needs to reflect the actual data sources feeding the system:
- Documents (PDFs, Word docs, procedures)
- Emails or tickets
- Excel files
- SharePoint or OneDrive content
- Live queries to a database
- Anything else that could be a data source for the RAG system

### 13.3 If It Is a Live Connection

For live data sources (databases, APIs), we either need:
1. An export of representative data, tagged by the Lam team as "this should be flagged" / "this is clean"
2. OR direct access to the data source plus access to an SME who can explain what should and should not be flagged

### 13.4 The Dependency Chain

The answer to "what samples do we need" depends on which use case / application is selected as the first one. The samples must come from that specific application's data sources. This is why naming the first application gates everything else.

---

## 14. Scope Discipline

### 14.1 What We Focus On

Solely the problem statement within Brad's team:
- Customer IP detection and protection across their document/knowledge systems
- The two use cases Mikhail presented (even though we will reframe the approach)
- The ingestion pipeline, control plane, and historical data cleanup

### 14.2 What We Mention Only in Passing

- "This architecture can naturally enable other AI activities once the immediate issue is solved"
- "If that is of interest strategically, we can discuss when the team is ready"
- Stop there. Do not elaborate. Do not list examples. Do not pitch growth.

### 14.3 Why This Discipline Matters

Mikhail was dismissive of anything beyond the stated use cases. Brad explicitly said "we don't want to introduce noise in our business case." Colin got redirected on the call for exactly this kind of scope expansion. The proposal must not repeat that mistake. The future potential is real and massive, but the presentation must be laser-focused on what was asked. Earn the right to expand later by delivering on the immediate ask first.

---

## 15. What We Still Do Not Know

### 15.1 Application Inventory

We still do not know what specific applications Lam has. They keep saying they have "a bunch of tools" but have not named a single one beyond generic descriptions. What is most likely: they have a project that was reused/forked multiple times. They keep saying "a ton" but we do not have a count, and they have yet to provide a single specific use case.

### 15.2 Technical Infrastructure Details

No specific Azure service inventory, no data volume numbers, no query pattern data, no budget framework.

### 15.3 Minimum Information Needed to Proceed

1. One specific application -- name it, describe what it does, what documents feed it
2. One specific document or representative sample of the type of content they are worried about
3. One specific situation where they were not successful with their current approach
4. A representative sample with both failure cases and known good examples
5. Their Azure environment details (what services they are paying for)
6. Daniel's availability for a technical call
7. Their data volume (documents, tickets per day, searches)
8. Their budget expectations

### 15.4 The "Too Technical" Pushback Was Wrong

Colin pushed for this on the call and was told he was "getting too technical." His position: this was not a technical question. He was asking "name one specific application that you use for document Q&A and tell me which one is highest impact." That is a business question. Any non-technical person should be able to answer it.

### 15.5 If Lam Provides It

We can build a compelling demo: the document goes in, flagged entities come out, the system shows what would be rejected/cleaned. This could be done rapidly.

### 15.6 If Lam Will Not Provide It

We could do a generic demo with Microsoft Purview and a data plane concept using synthetic documents, but it will not be as compelling. Colin prefers real data because "it's more factual if they themselves have that."
