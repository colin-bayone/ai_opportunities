# Lam Research: Problem Restatement

**Prepared by:** BayOne Solutions
**Date:** 2026-03-20
**Context:** Following Discovery Call on 2026-03-12

---

## Purpose

This document reflects BayOne's understanding of the problem as presented during the discovery session on March 12, 2026. The intent is to demonstrate a clear and accurate understanding of the challenge before any approaches or solutions are discussed.

---

## 1. The Business Context

Lam Research occupies a unique position in the semiconductor industry. As a provider of wafer fabrication equipment, Lam has direct visibility into the production environments of customers who are direct competitors with each other. TSMC, Samsung, Intel, Micron, and SK Hynix all rely on Lam's equipment and services, and in the course of that work, Lam employees interact with proprietary data belonging to each of these customers.

A leak of one customer's data to another would be catastrophic, both for the business relationship and potentially from a regulatory and antitrust standpoint. Protecting customer intellectual property is therefore existential to Lam's business model.

---

## 2. The Troubleshooting Workflow

The problem is anchored in a three-stage troubleshooting workflow that Lam's field and support teams follow:

1. **Self-Help:** The user searches knowledge bases, documentation, and AI tools to find an answer independently.
2. **Ask for Help:** The user reaches out to a community of experts or peers for guidance.
3. **Escalate:** A structured troubleshooting process involving more experts, deeper analysis, and formal coordination.

The goal is to maximize resolution at the self-help tier and minimize the volume of issues that reach escalation. Escalation is costly, time-consuming, and affects customer trust. The more problems that can be resolved through self-help, the lower the operational cost and the faster the resolution time.

A critical feedback loop connects these tiers: once a problem is solved through escalation, the solution should flow back into the self-help knowledge base so that the next person with the same problem finds the answer without escalating. This feedback loop is currently blocked, and unblocking it is at the core of what Lam is trying to achieve.

---

## 3. The Over-Restriction Problem

Today, Lam's default approach to protecting customer IP is blanket restriction. When there is uncertainty about whether a document or piece of data contains customer-identifiable information, the policy is to assume it does and restrict access.

This approach is understandable and defensible from a risk standpoint. However, it creates significant downstream problems:

- **Knowledge silos.** A field engineer working on a problem for one customer cannot access a solution that was documented in the context of another customer, even when the solution itself is entirely generic and non-proprietary. The answer exists within the organization but is inaccessible due to customer segmentation.

- **Fragmented search.** Over-restriction has driven the creation of multiple segmented search systems. There are currently six or more separate search tools, each covering a different knowledge pool with different access rules. This fragmentation compounds the problem rather than solving it.

- **Blocked AI training.** Restricted data cannot be used to train AI models for the general population. Because the organization cannot confirm whether a given data source is free of customer-identifiable content, that data source is excluded from model training entirely. This limits the effectiveness of any AI-powered search or assistance tools.

- **Blocked feedback loop.** The escalation-to-self-help feedback loop described above cannot function. Solutions generated during escalation often contain unstructured text, meeting transcripts, and attachments that may include customer names, fab identifiers, or other sensitive information. Until that content can be reliably cleaned, it cannot safely enter the general knowledge base.

The result: Lam is knowingly limiting productivity and knowledge-sharing capability in order to protect customer IP. The trade-off is acknowledged internally, and the goal of this initiative is to move from blanket restriction to targeted, intelligent protection.

---

## 4. Use Case 1: Self-Help Search Enablement

### The Problem

When users search for solutions across Lam's knowledge bases, relevant results may be locked behind customer-specific access restrictions. A solution that originated in a Samsung context may be entirely applicable to an Intel problem, but the customer segmentation prevents the Intel-assigned user from seeing it.

### The Goal

Process stored content (documents, procedures, historical solutions) to remove or mask customer-identifiable information so that the underlying technical knowledge can be surfaced to a broader audience. The aspiration is to take content that is currently restricted and make it searchable across customer boundaries by stripping the information that makes it customer-specific.

### Key Characteristics

- The data involved is primarily unstructured: documents, procedures, meeting transcripts, problem descriptions.
- Some metadata exists in certain systems to identify customers, but coverage is not 100%.
- There is no single data lake. Multiple databases and search systems exist, each with different segmentation and access rules.
- The approach for this use case is accuracy-focused rather than speed-focused. Processing can take longer (up to an hour for batch operations) because it happens on stored data, not in real time.
- Over-redaction is acceptable as a starting point. If the system strips more than strictly necessary, that is still an improvement over blanket restriction. Success is defined as: "if we over-redact less than we currently restrict, we already have success."

### Sensitive Information in This Context

The primary concern is customer-identifiable information, including:

- **Customer names** (direct mentions in text)
- **Fab identifiers** with numerous spelling variations (Fab 11, F11, Micro 11, FAP 11, FAP-11, and others)
- **File names** that contain customer identifiers
- **Site-specific details** traceable to a particular customer
- **Customer-proprietary process information** embedded within troubleshooting documents

The initial target scope is narrow: customer name and file name. If detection and redaction cannot be made reliable for these two fields, there is no basis for expanding to harder cases.

---

## 5. Use Case 2: Escalation Entry Point Protection

### The Problem

When users create tickets, describe problems, or interact with experts during escalation, the way they communicate can itself expose customer IP. A field engineer typing a problem statement from a mobile device might write "I'm at Fab 11 and have an issue with this tool," inadvertently including customer-identifiable information in an unstructured text field.

Policy violations are common. When the team began examining actual ticket data, a policy violation was found within the first seven tickets reviewed. This is not a theoretical risk; it is a pervasive, everyday occurrence driven by convenience rather than malice.

### The Goal

Detect potential policy violations at the point of data entry and notify the user in real time. The intent is awareness and deterrence, not enforcement. The system should alert the user that their input may contain customer-confidential information and give them the opportunity to correct it, while leaving the final decision with the user.

### Key Characteristics

- This must operate in real time, within standard UI response times of two to five seconds.
- The system notifies rather than blocks. Because no detection system will be 100% accurate, hard blocking at entry would create unacceptable friction and false rejections.
- **False positive sensitivity is critical.** If every fifth notification is a false alarm, users will stop trusting the system and ignore all notifications. Auditors who receive constant false positive alerts will similarly lose confidence and disable notifications. The target false positive rate is well below 1%.
- Detection only, no redaction at this stage. The system identifies and flags; it does not modify content.

### Two Sub-Approaches Within Use Case 2

**Real-time detection at entry:** The "big brother" approach. Fast, lightweight, focused on minimizing false positives. Catches the obvious violations (customer names, fab identifiers in plain text) and notifies immediately.

**Batch processing after entry:** Once data has entered the system (problem statements, answers, transcripts, attachments), a heavier analysis runs to detect and handle customer-identifiable information before that data flows into the general knowledge base. This is more accuracy-focused than speed-focused and can take longer to process. Over-redaction is acceptable here. If content cannot be reliably redacted (for example, IP embedded in an image), the fallback is to keep the document restricted rather than releasing it with IP intact.

### The Connection Between Use Cases

Batch processing in Use Case 2 feeds Use Case 1. Once escalation data is cleaned through the heavier detection and redaction process, that cleaned data can enter the self-help knowledge base. This is the feedback loop: escalation solutions, once stripped of customer-identifiable information, become searchable for the general population, driving more problem resolution at the self-help tier and reducing future escalation volume.

The two use cases should be treated as separate tracks for MVP and development purposes, but they are connected through this feedback loop and should inform each other.

---

## 6. What Has Been Tried

Lam has made multiple attempts to solve the detection and redaction challenge. Each attempt has been paused or abandoned for specific, articulable reasons.

### Machine Learning Models

Three models were trained using an MLOps pipeline deployed on Azure Cloud:

1. **A Transformers-based model**
2. **SpaCy** (NLP library, likely NER-based)
3. **An Azure AI model**

These models were trained with Lam's own data on top of globally pre-trained foundations. The result across all three: a false positive rate of approximately 20% per ticket. Fine-tuning improved this marginally, to approximately 17%. At a target of well below 1%, this gap is an order of magnitude, and the effort was paused.

For reference, a 20% false positive rate is consistent with general-purpose language model baselines, suggesting that the fine-tuning approach did not produce meaningful gains over default model performance.

### Rule-Based Models

Rule-based approaches were explored but abandoned early. The core challenge is the spelling variation problem: a single entity like "Fab 11" can appear as Fab11, F11, Micro 11, FAP 11, FAP-11, and other variations. Enumerating all permutations is theoretically possible but creates an unsustainable maintenance burden, as new variations appear continuously with new employees, sites, and shorthand.

### Labeling Exercise

A labeling exercise to create structured training data was evaluated and estimated at over 1,000 person-hours for the initial pass, with continuous maintenance required thereafter. This was paused (not abandoned) due to cost, with the reasoning that the investment could not be justified without first proving the concept works at a smaller scale. If the use case proves valuable enough, the labeling effort may become justifiable.

### Generative AI

Generative AI approaches have not been attempted. The decision was deliberate: the team preferred deterministic, binary output (redact / don't redact) over the probabilistic, unstructured output that language models typically produce. There is awareness that prompt engineering can produce more structured output from language models, but concerns remain about reliability and guardrails.

### Current State

The current operational mode remains blanket over-restriction. Every prior attempt to replace it with something more targeted has failed to meet the accuracy bar. The organization is open to any and all approaches, including AI, non-AI, or hybrid methods, with a preference for understanding trade-offs before committing to a direction.

---

## 7. The Infrastructure Landscape

The technology environment is highly heterogeneous. There is a mix of on-premises systems, cloud-based systems, systems in the process of migrating to cloud, internally hosted AI tools (including GPT models deployed within Lam's own infrastructure), and cloud-based bot services.

The organization aspires to move cloud-first and has expressed interest in a microservice architecture long-term, though this is aspirational rather than committed.

Key characteristics of the current landscape:

- **No unified data lake.** Data is fragmented across many systems with different segmentation and access models.
- **Six or more search tools** covering different knowledge pools.
- **Multiple data entry paths:** user-entered problem statements, expert responses, uploaded documents, Microsoft Teams meeting transcripts automatically attached to escalation tickets, and images/OCR content.
- **Identity and access management** is an active program of approximately two years but is not yet fully mature. Users are identified by work center and role. Employee types include full employees, contractors, licensed service providers, trade-restricted individuals (with distinct badge colors), and embargo-country employees.
- **Access Security Manager (ASM)** governs access to certain sensitive areas (such as the escalation flow) but is not enterprise-wide and does not control individual entry fields within tickets.
- **Customer segmentation** in the ticketing system is enforced at the customer level: Lam employees assigned to Micron see Micron tickets; those assigned to Samsung see Samsung tickets. Cross-visibility is blocked.

---

## 8. The Desired Outcome

Lam Research is looking for a path from blanket over-restriction to targeted, intelligent IP protection that:

- Enables cross-customer knowledge sharing for non-proprietary technical solutions
- Detects and flags customer-identifiable information at the point of data entry with a false positive rate well below 1%
- Processes stored content to remove customer-identifiable information so it can be surfaced more broadly
- Unblocks the escalation-to-self-help feedback loop, driving down costly escalations over time
- Starts small, proves incrementally, and scales based on demonstrated results
- Is technology-agnostic, with a willingness to evaluate any approach based on trade-offs and outcomes
- Does not require a revolutionary overhaul; evolutionary, incremental progress is expected and preferred

The initial proof of concept scope is narrow: demonstrate reliable detection and handling of customer names and file names. If these two fields cannot be solved reliably, there is no foundation for tackling the harder cases. If they can, the path to broader capability becomes clear.

---

## 9. Summary

Lam Research has a well-defined problem with clear business impact. The over-restriction of customer-identifiable information is blocking knowledge sharing, limiting AI model training, fragmenting search across multiple systems, and preventing the feedback loop that would drive down escalation costs. Multiple technical approaches have been tried and have not met the required accuracy thresholds. The organization is open to new approaches and is looking for a partner that demonstrates deep understanding of the problem before proposing solutions.

BayOne believes this document reflects that understanding. We welcome feedback, corrections, and refinements to ensure we are fully aligned before discussing approaches.
