# 02 - Meeting: Topic Map (Pass 1 - High-Level Overview)

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** 1 of N (high-level topic identification)

---

This document captures the major topics discussed in the meeting, identified from a first full read of the transcript. Each topic below will be the subject of a focused deep-dive pass.

## Topics Identified

### 1. The Two Use Cases (Core Problem Statement)
Mikhail presented two distinct business cases using a troubleshooting workflow as the frame:
- **Use Case 1: Self-Help Search** - How to surface knowledge across customer boundaries without leaking IP. Currently over-restricting, which kills productivity.
- **Use Case 2: Ask for Help / Escalation** - How to handle IP in ticket creation, problem descriptions, and expert Q&A. Splits into two sub-problems: real-time detection at entry and batch redaction after entry.

These are explicitly separate swim lanes, not to be jumbled together.

### 2. Detection vs. Redaction (Technical Distinction)
A critical conceptual distinction that ran through the entire meeting:
- **Detection:** Real-time, performance-sensitive, focused on false positive avoidance. Notify the user, don't block. 2-5 second response requirement.
- **Redaction:** Batch/heavy, accuracy-focused, multiple techniques depending on content type. Can take longer. Over-redacting is acceptable as a starting point.

Different tolerances for each: detection must have <1% false positive rate. Redaction can afford to over-redact as long as it's better than current blanket restriction.

### 3. What They've Tried (and Why It Failed)
- Transformers model, SpaCy, Azure AI model - 20% false positive rate per ticket, improved to 17% with fine-tuning (effectively useless)
- Rule-based models - started but abandoned due to spelling variation problem (Fab11, F11, FAP space 11, FAP-11, etc.)
- 1,000+ hours estimated for labeling exercise - paused due to cost and maintenance burden
- Have NOT tried generative AI for this - deliberately chose ML for deterministic output
- MLOps infrastructure is in place on Azure cloud

### 4. The Over-Restriction Problem
Current mode of operation: when in doubt, restrict everything. This is causing:
- Knowledge silos (6+ search systems)
- Blocked cross-customer learning (Samsung solution invisible to Intel users)
- Can't feed unstructured data back into general training pool
- Can't build the feedback loop that would drive down escalation costs
- Policy violations are trivially easy to find (7 tickets to find first one)

### 5. Infrastructure Landscape
- No unified data lake - fragmented across many systems
- Mix of on-prem and cloud, with aspiration to move cloud-first
- "LamGPT" exists (GPT models hosted within Lam)
- Copilot in use (GPT models)
- Many legacy systems that are "not two or three systems" but "flows"
- Aspirational goal: microservice architecture long-term
- Teams meetings auto-transcribed and attached to tickets

### 6. Identity and Access Management (IAM)
- Active IAM program for ~2 years, making progress but "not super robust"
- Currently identify users by work center and role
- Trade-restricted employees (TRI) flagged with different badges
- Embargo country restrictions exist
- ASM (Access Security Manager?) governs some areas (escalation flow) but not enterprise-wide
- Customers segmented: Micron people can see Micron tickets, can't see Samsung tickets
- Blanket access philosophy being questioned internally

### 7. The Feedback Loop Vision
Brad and Mikhail described a virtuous cycle they want to enable:
- Solve problems at self-help level -> feed answers back into knowledge base -> reduce escalations
- Currently blocked because unstructured data in escalations may contain IP
- Can't safely feed restricted data into general training until detection/redaction is solved
- This is the real ROI argument: driving down costly escalations by enriching self-help

### 8. Engagement Structure and Next Steps
- Follow-up meeting to bring in Daniel and broader team
- Brad will NOT be writing user stories - his team handles that
- Previous "pod" work was a pilot, not standard operating procedure
- Open to any approach (AI or not), but want to understand trade-offs
- Want rapid prototyping / incremental proof, not months-long projects
- Evolutionary, not revolutionary
- Brad asked Colin for "high value targets" - where to focus first
- The transcript appears to cut off mid-answer on this question

### 9. Colin's Key Interventions
- Pushed the "unified control plane" concept for ingestion across systems
- Pointed out 20% false positive = out-of-the-box ChatGPT (fine-tuning was effectively useless)
- Emphasized ingestion-side protection as biggest bang for buck
- Shared Coherent Corp analogy about privileged access scrutiny
- Got redirected by Mikhail on access management (valid but out of scope per Mikhail)

## Proposed Deep-Dive Files

Based on this topic map, I recommend these focused-pass files:

| File | Focus | Why It Needs Its Own File |
|------|-------|-------------------------|
| `02_meeting_technical_use_cases` | Deep dive on the two use cases with all technical details | This is the core of the engagement - needs exhaustive detail |
| `02_meeting_what_was_tried` | Everything attempted, results, why it failed, what wasn't tried | Critical for avoiding duplication and informing approach |
| `02_meeting_infrastructure_and_access` | System landscape, IAM state, data flows, over-restriction mechanics | Needed to understand what's possible technically |
| `02_meeting_business_opportunity` | Engagement structure, appetite, next steps, ROI framing | Separate from technical - this is about the deal |
| `02_meeting_speaker_dynamics` | Who said what, how they interacted, what it means for the engagement | Important signals in how people communicated |

All will have `_2026-03-12` date suffix.
