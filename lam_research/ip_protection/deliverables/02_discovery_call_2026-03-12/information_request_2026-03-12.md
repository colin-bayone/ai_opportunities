# Lam Research: Information Request

**Prepared by:** BayOne Solutions
**Date:** 2026-03-20
**Context:** Following Discovery Call on 2026-03-12

---

## Purpose

During the discovery session, we gained a strong understanding of the problem space (captured in the accompanying Problem Restatement). To move forward with a preliminary approach, we need additional specifics that will allow us to scope an initial proof of concept and prepare meaningful recommendations with trade-offs for the follow-up meeting.

This document outlines the information we are requesting from the Lam Research team. We have organized the items by priority and have noted which items could be addressed by the business team versus those that may require involvement from the technical team.

---

## Priority 1: Selecting the Starting Point

These items are essential for scoping the initial proof of concept and do not require deep technical knowledge to answer.

### 1.1 Identify One Application

We need to start with one specific application or system from Lam's environment. During the discovery session, the team described a broad landscape of tools and knowledge systems. To build something meaningful rather than generic, we need to focus on a single, high-impact starting point.

**What we are asking for:**

- The name of one application or system that is considered the highest-impact candidate for this initiative
- A description of what that application does (what problem it solves for its users, how they interact with it)
- What data sources feed into it (documents, databases, APIs, user-entered text, transcripts, or other inputs)
- What types of content within that application are most likely to contain customer-identifiable information

This is a business-level question about which tool matters most, not a technical deep dive into architecture.

---

## Priority 2: Technical Context

These items require involvement from the technical team and will inform the architecture of our proposed approach.

### 2.1 Representative Data Samples

To validate any approach, we need to see examples of the actual content the system would process. We need both positive and negative examples.

**What we are asking for:**

- **Examples of content that should be flagged:** Documents, tickets, or data entries that contain customer-identifiable information and represent the types of violations the system needs to catch. These are the failure cases, the things that the current approach misses or that policy violations look like in practice.
- **Examples of content that is clean:** Documents or entries that are free of customer-identifiable information and should pass through without flagging. This is the gold standard for what "good" looks like.
- **Coverage across data types:** If the selected application ingests multiple content types (text documents, Excel files, transcripts, images, database records), we would benefit from seeing examples of each type that is in scope.

If security or IP concerns prevent sharing actual documents, sanitized examples or synthetic representations that preserve the structure and patterns of real content would also be valuable.

For live data sources (databases, APIs), we would need either an export of representative data tagged by the team as "should be flagged" or "is clean," or access to the data source along with a subject matter expert who can walk us through what should and should not be caught.

### 2.2 What "Sensitive" Looks Like in Practice

During the discovery session, the team described customer names and file names as the initial target fields. To calibrate detection accurately, we need concrete examples of what customer-identifiable information looks like in the wild.

**What we are asking for:**

- A list of the specific customer names, abbreviations, and identifiers that the system should recognize
- Known spelling variations for key identifiers (the discovery session surfaced examples like Fab 11, F11, Micro 11, FAP 11, FAP-11, and we expect there are many more)
- Any other categories of information beyond customer names and file names that should be flagged, even if those are lower priority for the initial scope
- Examples of borderline cases: content that is ambiguous or context-dependent, where a human reviewer would need to make a judgment call

### 2.3 Prior Technical Work

We understand that multiple ML-based approaches have been tried (Transformers, SpaCy, an Azure AI model) with results around 20% false positive rate, fine-tuned to 17%. To avoid repeating prior work and to understand what has already been learned, we would benefit from the following:

- The specific model architectures and configurations that were used
- The training data: what was it, how large was it, how was it labeled
- The testing methodology: how was the false positive rate calculated, what was the test set, and how was ground truth established
- The labeling exercise that was assessed at 1,000+ person-hours: what was the intended scope, and what was the methodology
- Any prior partner involvement in this work (what was delivered, how the problem was scoped for them, and what the outcome was)
- Whether any of this prior work produced reusable artifacts (trained models, labeled datasets, evaluation scripts)

### 2.4 Infrastructure and Systems

During the discovery session, the infrastructure landscape was described at a high level. To recommend an approach that fits Lam's environment, we need more specifics:

- What Azure services are currently in use (and licensed) across the organization
- Which systems involved in this initiative are on-premises versus cloud-hosted
- The architecture of the selected application from Priority 1.1 (how data enters, how it is stored, how it is served to users)
- Data volume estimates: how many documents are ingested per day or week, how many tickets are created, how many search queries are performed
- Any existing data pipelines, ingestion frameworks, or middleware that are already in place

### 2.5 Organizational and Governance Context

Understanding the decision-making structure and existing governance will help us propose an approach that is operationally realistic.

- The governance structure for AI and data initiatives: who approves new tools, who manages compliance, and how IT and cybersecurity are involved in decisions of this nature
- Any regulatory or contractual requirements that constrain how customer data is handled (beyond the general principle of customer IP protection)
- The scope of systems that fall within the initiative owner's direct authority versus systems that require coordination with other teams or departments

### 2.6 The "2-5 Seconds" Requirement

The discovery session referenced a two-to-five-second performance requirement for the detection use case. To architect appropriately, we need to understand what this requirement is measuring:

- Is this the time from document upload to confirmation that the upload was accepted?
- Is this the time from data entry to a detection notification appearing in the UI?
- Is this the time from upload to the content being available for search or Q&A?

The architecture differs depending on which of these the requirement applies to.

---

## Priority 3: Follow-Up Discussion

These items are best addressed in a working session with the technical team rather than asynchronously.

### 3.1 Technical Working Session

We would like to schedule a working session with the technical lead and relevant team members to walk through the items in Priority 2 in a conversational format. This would allow us to ask follow-up questions in real time and ensure we have the depth needed to prepare a well-grounded preliminary approach.

### 3.2 Application Inventory (Lightweight)

We do not need an exhaustive inventory of every application in the environment. However, a lightweight view of the top three to five most important applications or knowledge systems that are candidates for this initiative would help us understand the broader landscape and plan for incremental expansion beyond the initial proof of concept.

---

## Next Steps

Once we receive the information outlined in Priority 1, we will be in a position to prepare a preliminary approach document with specific recommendations, trade-offs, and a proposed scope for the initial proof of concept.

We are targeting the follow-up meeting as the venue to present this approach, and we want to ensure that what we bring is grounded in Lam's actual environment rather than generic recommendations.

We appreciate the team's time and openness during the discovery session and look forward to continuing this conversation.
