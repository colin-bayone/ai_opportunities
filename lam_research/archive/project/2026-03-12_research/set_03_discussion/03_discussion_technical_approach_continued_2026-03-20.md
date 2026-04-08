# 03 - Discussion: Technical Approach (Continued)

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Follow-up Q&A on the initial technical approach document

---

## 1. Automated Content Entry and the Cleaning Pipeline

### The Problem
Some content enters the system automatically (e.g., Teams meeting transcripts auto-attached to tickets). There is no human in the loop to clean and resubmit when the system rejects.

### Colin's Position
This requires discovery with Lam's team -- we cannot prescribe the right solution without representative samples. However, the general approach:

- **Text-based content (transcripts, text fields, simple documents):** Can be cleaned with an agentic AI cleaning tool. A well-defined process where the system identifies flagged content, proposes cleaned versions, and resubmits automatically. This is feasible for simple content types.

- **Complex documents (PDFs, PowerPoints):** We are NOT in the business of trying to redact these in real-time. This is impractical on day one.

- **The evolutionary approach:** We don't need to say on day one that all document types can be cleaned across all topics. Start with a representative sample set of documents. Test on that. Verify it's good, traceable, and trackable. Then expand capability over time. This is the same approach you'd use for any AI project.

### Metrics as a Core Requirement

Colin emphasized: metrics are essential, not just having an AI system.

The system should track and report:
- Rejection rates (how often are documents being flagged?)
- Patterns in rejections (is it too strict? are specific users/groups consistently flagging?)
- User behavior insights (are people fundamentally misunderstanding compliance requirements?)
- Segmentation and demographics around rejection patterns

**Use case for metrics:** If users are constantly uploading and constantly getting flagged, the system should be intelligent enough to surface whether:
1. The detection rules are too strict (system problem)
2. People have a knowledge gap that could be resolved by compliance training (people problem)

These insights are derivable from the data if we store rejection events, flagged content types, user segments, and outcomes. This is a major value-add beyond just "we built a filter."

---

## 2. Unified Control Plane: Build vs. Configure

### Two Options for Lam

**Option 1: All existing Azure services**
- Azure Blob Storage, Azure AI Search, Azure Cosmos DB, Azure AI Foundry, Microsoft Purview
- Maximum compliance, maintainability, administrable by non-technical people
- Enterprise-grade from day one

**Option 2: Primarily Azure services with custom backend where needed**
- Core infrastructure on Azure (Blob Storage, Azure Postgres + pgvector, etc.)
- Custom components for things that don't work well or are cost-prohibitive in Azure
- Example: Azure AI Search may be cost-prohibitive or provide insufficient value for certain RAG use cases. In those cases, build a custom vector search on Azure Postgres + pgvector, while still using Azure Blob Storage for documents.

### Decision Framework

- **Always start with enterprise solutions first.** Compliance, maintainability, and enabling non-technical administration are the priorities.
- **Fall back to custom only when justified** -- cost-prohibitive, insufficient capability, or specific implementation needs that Azure services don't cover.
- **Cost is situational.** Just because something is on Azure doesn't make it expensive. Just because something is off Azure doesn't make it cheap. We need to know Lam's specific implementations and use cases before prescribing solutions or doing cost estimation.
- **We cannot prescribe without knowing the situation.** The right answer depends on what their specific applications look like, their data volumes, their query patterns, and their budget constraints.

### Clarification: "One Project Forked Many Times"

Colin clarified: Lam probably has a single RAG concept that was re-used across multiple applications (not literally a GitHub fork). The pattern is the same even if the implementations differ. The control plane would unify the common backend of this repeated pattern.

---

## 3. Historical Data Cleanup: Day Zero and Day One

### Terminology (Important)

- **Day Zero:** The day when everything is done and ready to be reprocessed. The system is built, the ingestion pipeline works, the detection rules are validated. Day zero is the starting gun, not the finish line.
- **Day One:** The first day after day zero where the application goes online with the new system after all historical data has been processed. This is NOT necessarily the calendar day after day zero -- it's a milestone, not a date.

### What Happens During Reprocessing (Between Day Zero and Day One)

1. Historical data is re-ingested through the new filter system
2. Flagged content is **quarantined** and surfaced for human review
3. Auto-cleanable content (text, transcripts -- per question 1) may be cleaned automatically
4. Content is **blocked from the RAG index** until addressed
5. AI classification and categorization assists so that humans are NOT reviewing each and every file individually

### Business Decision, Not Technical Decision

Whether flagged content is quarantined, auto-redacted, or blocked is ultimately **Lam's call**. BayOne provides guidance and recommendations, but Lam controls this decision. Our recommendation: block from RAG index until resolved, with AI-assisted categorization to minimize human review burden.

### Framing for the Proposal

This needs to sound achievable and AI-enabled:
- "AI-enabled with minimal human intervention except where needed"
- Not a massive manual review project
- The system does the classification and categorization work
- Humans only intervene for edge cases and business judgment calls
- One application at a time, clean as you go

---

## 4. The Layered Architecture: Purview + AI + Control Plane

### How the Layers Work Together

**Layer 1: Deterministic (Microsoft Purview)**
- Custom Sensitive Information Types for known entities (customer names, fab IDs, variations)
- Regex and keyword matching
- Always on, regardless of what systems are using it
- Zero false positives on known patterns

**Layer 2: AI / Contextual Classification**
- Handles the gray areas Purview can't: "Is 'TSMC' sensitive in this specific context?"
- Document-level classification
- Natural language analysis for unstructured content
- Faster than expected -- not a 20-minute wait. AI classification can run quickly, even on uploaded documents.

**Layer 3: Unified Control Plane**
- Wraps Layer 1 and Layer 2 into a single standard interface
- An end user or application makes one call to the data plane
- The data plane already has Purview built in, already has the AI layer built in
- The layers are **indistinguishable to the end user** -- they just see "clean/not clean"
- This is what we pitch to Lam: one interface, not a patchwork of tools

### The Key Selling Point

The end user (or the RAG application) doesn't know or care whether a detection came from a regex rule in Purview or an AI classification model. They make one API call to the control plane. The control plane handles the routing, the detection, the classification, and the decision. This is the unified experience.

---

## 5. What's Missing: The POC Problem

### We Have Nothing to Demo

Colin is blunt: there is nothing to go off of right now for a POC. The Lam team has provided:
- No specific document examples
- No specific application names
- No specific problem statement beyond hand-waving
- No representative sample of anything

### What We Need from Lam (via the Sales Team)

At minimum:
1. **One specific application** -- name it, describe what it does, what documents feed it
2. **One specific document** or a representative sample of the type of content they're worried about
3. **One specific situation** where they were not successful with their current approach

### The "Too Technical" Pushback Was Wrong

Colin pushed for this on the call and was told he was "getting too technical." His position: this was not a technical question. He was asking "name one specific application that you use for document Q&A and tell me which one is highest impact." That is a business question. Any non-technical person should be able to answer it.

### What Lam Cannot Do

They cannot sit here and expect BayOne to guess what their starting point should be. They introduced the concept of "many tools and applications" in the meeting. They need to pick one. The sales team must formally request this information.

### If Lam Provides It

We can build a compelling demo: the document goes in, flagged entities come out, the system shows what would be rejected/cleaned. This could be done in a day.

### If Lam Won't Provide It

We could do a generic demo with Microsoft Purview and a data plane concept using synthetic documents, but it won't be as compelling. Colin prefers real data because "it's more factual if they themselves have that."

---

## 6. What the Sales Team Must Get

### From the Anuj Debrief (Set 02a) -- Already Identified

1. Name one specific tool (the biggest one)
2. Describe what that tool does
3. What documents feed it

### Additional Items (Identified from This Discussion)

4. **A representative sample document** (or at minimum, a description of what one looks like -- even a sanitized example)
5. **A specific situation where their current approach failed** -- not "20% false positive rate" in the abstract, but "this specific ticket had this specific violation and here's what happened"
6. **Their application inventory** -- how many RAG-like applications do they actually have? They keep saying "a ton" but have never given a number or a list
7. **Their Azure environment details** -- what Azure services are they actually paying for? This gates whether Purview is immediately available or requires new procurement
8. **Daniel's availability for a technical call** -- Brad confirmed Daniel is the technical counterpart. We need to talk to someone who can answer "what Azure services are you using" without saying "I don't know what that means"
9. **Their data volume** -- how many documents, how many tickets per day, how many searches? This gates architecture decisions and cost estimation
10. **Their budget expectations** -- the 1,000 man-hours comment suggests they have no real cost framework. We need to understand what they think this costs vs. what it actually costs
