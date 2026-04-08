# 02 - Meeting: Topic Map

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Pass 1 - High-level topic identification

---

## Major Topics Identified

### 1. Technical Use Cases and Requirements
The core of Mikhail's whiteboard presentation. Two distinct business cases with different technical requirements:
- **Self-help search (redaction):** Batch processing, accuracy-focused, heavy-handed redaction to enable cross-customer knowledge sharing
- **Ask for help / escalation (detection):** Real-time, performance-focused (2-5 seconds), false-positive-sensitive, notification rather than blocking
- Detection vs. redaction distinction explained in detail
- False positive sensitivity differences between the two use cases
- Feedback loop concept (driving down escalations by feeding back to self-help)

### 2. What Was Tried and Results
Concrete data on prior technical attempts:
- Transformers, SpaCy, Azure AI model tested via MLOps on Azure cloud
- 20% false positive rate per ticket, fine-tuned down to 17%
- Rule-based models attempted but abandoned (spelling variations problem)
- 1,000+ hour labeling exercise paused
- GenAI explicitly NOT tried (unstructured output concern)
- Colin's diagnosis: 20% = out-of-the-box ChatGPT performance

### 3. Infrastructure and Access
System landscape and data architecture:
- Fragmented: on-prem + cloud, no unified data lake
- LamGPT (internal GPT deployment), Copilot, 6+ search systems
- Unstructured data is the primary challenge (documents, transcripts, procedures, problem statements)
- IAM program approximately 2 years in, not robust yet
- ASM governs access to some sensitive areas but not enterprise-wide
- Employee categories: blue badge, contractors, LSPs, trade-restricted, embargo country

### 4. Business Opportunity and Engagement Appetite
Deal signals, ownership structure, approach preferences:
- Brad owns everything end-to-end (business, product, program, technical)
- Open to "any and all approaches" with understanding of trade-offs
- Wants rapid prototyping, incremental, evolutionary not revolutionary
- Technology agnostic ("AI is a very sexy word, but it's also a meaningless word")
- Previous "pod" model was a pilot, not standard operating mode
- Follow-up meeting planned with broader team including Daniel
- ROI framing: productivity gains, cost reduction, customer trust
- Transcript cuts off mid-answer on "high value targets" question

### 5. Speaker Dynamics and Power Structure
How the meeting actually ran, who controlled what:
- Brad as room controller: set format, enforced boundaries, redirected when needed
- Mikhail as precise technical translator: led whiteboard, named specifics, admitted knowledge limits
- Colin's hits and misses: 20%/ChatGPT diagnosis landed, unified control plane resonated, got redirected on IAM
- Pat's contributions: ingestion questions, ecosystem knowledge, mostly positive
- Key tension: Brad's "Is that clear, Colin?" after IAM tangent

---

## Proposed Deep-Dive Files

| File | Focus | Rationale |
|------|-------|-----------|
| `02_meeting_technical_use_cases_2026-03-12.md` | The two use cases, detection vs. redaction, false positive requirements | This is the core problem statement. Needs exhaustive capture of every technical detail Mikhail presented. |
| `02_meeting_what_was_tried_2026-03-12.md` | Models tried, results, labeling exercise, why GenAI not used | Critical for solution design. Knowing exactly what failed and why prevents us from proposing something they already rejected. |
| `02_meeting_infrastructure_and_access_2026-03-12.md` | System landscape, data architecture, IAM/ASM, employee categories | Determines what is technically feasible. Fragmented infrastructure shapes the approach. |
| `02_meeting_business_opportunity_2026-03-12.md` | Brad's ownership, engagement appetite, ROI, next steps, deal signals | Shapes the commercial strategy. Brad's preferences directly determine how we position. |
| `02_meeting_speaker_dynamics_2026-03-12.md` | Power structure, key moments, tensions, alignments, unspoken signals | Informs how we engage in the follow-up. Who to address, what tone to take, what to avoid. |
