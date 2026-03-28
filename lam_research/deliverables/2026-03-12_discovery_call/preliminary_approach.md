# Lam Research: Preliminary Approach

**Prepared by:** BayOne Solutions
**Date:** 2026-03-20
**Context:** Following Discovery Call on 2026-03-12

---

## Purpose

This document presents BayOne's preliminary thinking on how to address the IP protection and knowledge enablement challenge described during the discovery session on March 12, 2026. These are initial ideas informed by BayOne's experience building similar solutions across multiple industries. They are intended as a starting point for discussion, not a final recommendation, and will require refinement through deeper discovery with the technical team.

---

## 1. Problem Summary

Lam Research needs to move from blanket over-restriction of customer-identifiable information to targeted, intelligent protection. The current approach blocks cross-customer knowledge sharing, fragments search across six or more systems, prevents AI model training on restricted data, and breaks the feedback loop that would allow escalation solutions to flow back into self-help.

Prior attempts using custom ML models (Transformers, SpaCy, Azure AI) produced false positive rates around 20%, consistent with general-purpose model baselines. Rule-based approaches were abandoned due to the maintenance burden of spelling variations. The organization is open to any approach and has expressed a preference for rapid, incremental proof over extended development cycles.

---

## 2. Observations on Prior Approaches

The approaches tried to date follow a common pattern: training custom classification models from scratch against domain-specific data. This pattern is well understood in the industry, and while it can be effective for certain problems, it tends to be brittle in environments where the target entities (customer names, fab identifiers, site codes) are finite and follow predictable variation patterns. Custom model training works best when the classification problem is open-ended and the entity set is unbounded. In this case, the entity set is known and enumerable.

Additionally, the separation between detection and redaction as distinct initiatives may be introducing unnecessary complexity. Detection is a prerequisite for any downstream action, whether that action is notification, redaction, quarantine, or rejection. A unified detection pipeline that supports multiple response modes would simplify the architecture and reduce duplication of effort.

BayOne has applied this same methodology at prior engagements across semiconductor, retail, and manufacturing environments, each with different technology stacks and compliance requirements. The underlying approach is consistent even when the implementation details differ.

---

## 3. Proposed Approach: Hybrid Architecture

BayOne recommends a hybrid approach that combines deterministic logic with AI-based classification. Each layer handles the part of the problem it is best suited for.

### Deterministic Layer

For known, enumerable entities, deterministic matching provides the fastest and most accurate detection with zero false positives on exact matches.

- **Entity lookup tables** for customer names, fab identifiers, and their known variations. These are maintained as configuration, not model weights, making them easy to update without retraining.
- **Pattern matching** for structured identifiers that follow predictable formats, even with variation (e.g., Fab 11, F11, Micro 11, FAP 11, FAP-11).
- **Keyword and entity lists** that can be expanded over time as new patterns are discovered.

This layer addresses the specific failure mode that caused the rule-based approach to be abandoned. The spelling variation problem is real, but the variations are finite and can be systematically enumerated and maintained as a configuration resource.

### AI-Based Classification Layer

For content where deterministic matching cannot reach, AI-based classification provides contextual analysis.

- **Contextual sensitivity analysis** to determine whether a mention is sensitive in its specific context. A customer name appearing in a public earnings discussion is different from the same name appearing alongside yield data or process parameters.
- **Unstructured text analysis** for freeform problem descriptions, meeting transcripts, and expert responses where sensitive information may be embedded in natural language rather than appearing as discrete identifiers.
- **Document-level classification** to assess whether a document as a whole is likely to contain customer-specific IP that requires review.

AI-based classification can operate within standard response times for uploaded content. The processing architecture would use an asynchronous queue for robustness and scalability, while delivering a synchronous user experience. The user would see an upload in progress, and results would return within seconds.

### Why Hybrid

Deterministic matching gives a false positive rate of zero on known patterns. AI classification handles the contextual gray areas. Together, the system achieves accuracy that neither layer can deliver independently, while keeping the overall false positive rate well within the sub-1% target.

---

## 4. Ingestion-First Architecture

Rather than detecting sensitive content after it has entered the system and then attempting to redact it, the recommended approach focuses on the point of ingestion.

### How It Works

1. Content is submitted (a document upload, a text entry, a transcript attachment, or any other data source).
2. The ingestion pipeline runs the submitted content through both the deterministic and AI classification layers.
3. If the content is clean, it enters the knowledge base and is immediately available.
4. If the content is flagged, the system responds with specifics: what was detected, where it was found, and what action is recommended. Depending on the content type, the system may offer automated cleaning for simple cases (text fields, transcripts) or flag the content for review.

### What This Means for the Two Use Cases

The detection and notification use case (real-time, at entry) and the batch redaction use case (on stored content) become two modes of the same pipeline rather than separate systems.

- **New content** is processed at ingestion. If the pipeline works correctly, new content entering the knowledge base is clean by construction.
- **Historical content** already in the system is processed through the same pipeline as a one-time cleanup effort, application by application.

This approach significantly reduces the ongoing operational burden. Once the ingestion pipeline is validated, the batch redaction workload is bounded and decreasing rather than continuous.

---

## 5. Unified Data Plane

The current environment includes multiple search systems, knowledge bases, and AI tools, each with different access controls, data segmentation, and ingestion paths. A unified data plane would provide a single standard interface that consolidates these capabilities.

### What the Data Plane Provides

- **Unified document storage and knowledge base management** across applications
- **Centralized ingestion pipeline** with the detection and classification layers built in
- **Credential and access management** for connected data sources
- **A standard interface** from which different applications (search tools, chatbots, Q&A systems) can connect
- **Governance visibility** including usage metrics, rejection rates, flagging patterns, and adoption data

The data plane would be built on enterprise infrastructure. The recommended starting point is Azure-native services (Blob Storage for documents, a vector database for search embeddings, Azure AI Foundry for AI model hosting), with the flexibility to incorporate custom components where Azure services may not meet specific requirements or cost thresholds.

### Governance and Visibility

As a natural result of centralizing data ingestion and access, the data plane generates operational data that would otherwise be unavailable across fragmented systems. This includes tool usage patterns, document volumes, rejection and flagging rates, and user behavior insights. This data can be surfaced through a built-in dashboard or integrated with existing business intelligence tools.

These insights support ongoing optimization of the detection rules (are they too strict? too lenient?), identification of user training opportunities (are certain groups consistently uploading flagged content?), and business-level reporting on the value and adoption of knowledge tools.

---

## 6. Historical Data Cleanup

Once the ingestion pipeline is operational, existing content in the knowledge bases would need to be processed through the same pipeline.

### Two Categories of Historical Data

**Stored documents and snapshots** (procedures, historical solutions, uploaded files, archived transcripts): These would be re-ingested through the pipeline. Content that passes cleanly re-enters the knowledge base. Content that is flagged is quarantined and surfaced for review, with AI-assisted categorization to minimize the manual review burden.

**Live data sources** (databases, APIs, active queries): For data accessed through live connections, the detection layer would operate at query time or through a scheduled scan of the data source, with flagged records handled according to policies defined during discovery.

### Application-by-Application Migration

Historical cleanup would proceed one application at a time. Each application receives a transition point where its historical data has been processed, its ingestion pipeline is active, and it is operating on the new platform.

This approach is evolutionary by design. The first application is the most effort-intensive, as the pipeline itself is being built and validated. Subsequent applications benefit from shared data sources and an established detection configuration, making each migration progressively faster.

Applications not yet migrated continue to operate as they do today. This does not introduce new governance risk, as the current governance posture is already acknowledged as a gap. Each migration closes a portion of that gap without requiring a coordinated, organization-wide transition.

---

## 7. Enterprise Tools Strategy

BayOne recommends building on enterprise-grade tools from the start. Many of the capabilities required for this initiative are available through existing Azure services and Microsoft platforms. Using these tools provides compliance, maintainability, and the ability for non-technical administrators to manage ongoing operations.

### Microsoft Purview

Purview provides the foundation for the deterministic detection layer. Custom Sensitive Information Types can be defined for domain-specific entities (customer names, fab identifiers, and their variations), and Data Loss Prevention policies can enforce detection rules across connected systems. This is a mature, enterprise-supported capability used extensively in defense, financial services, and other regulated industries.

### Azure AI Foundry

Azure AI Foundry provides the hosting and compute environment for the AI classification layer. Models can be deployed, managed, and scaled through a managed service, reducing the operational burden of maintaining custom ML infrastructure. Even applications that are hosted on-premises can leverage Azure AI Foundry APIs for processing, decoupling the AI compute from the application deployment model.

### Flexibility for Custom Components

In cases where Azure-native services do not meet specific requirements, whether due to cost, capability gaps, or integration constraints, custom components can be built on Azure infrastructure (for example, Azure PostgreSQL with pgvector for vector search, rather than Azure AI Search). The principle is to start with enterprise tools and fall back to custom only when justified.

---

## 8. Preliminary Framing

This document represents BayOne's initial thinking based on the discovery session. Several areas require deeper exploration before these ideas can be refined into a concrete proposal.

### What We Need Next

- Identification of the first target application for the proof of concept
- Representative data samples (both flagged and clean examples)
- A working session with the technical team to understand the infrastructure in detail
- Clarification on performance requirements and their underlying use cases

These items are outlined in the accompanying Next Steps and Discovery document.

### What This Approach Enables

If validated through a targeted proof of concept, this architecture provides a foundation for progressively expanding IP protection across Lam's knowledge systems, one application at a time, without requiring a disruptive organization-wide transition. The same architecture that solves the immediate detection and knowledge-sharing challenge can naturally support additional initiatives as business needs evolve.

BayOne welcomes the opportunity to discuss these ideas and refine them with the Lam Research team.
