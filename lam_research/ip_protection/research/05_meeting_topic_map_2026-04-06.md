# 05 - Meeting: Topic Map

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Pass 1 - High-level topic identification

---

## Major Topics Identified

### 1. The Application: Escalation Solver
The application is finally named. Homegrown escalation management platform. Field engineers create work orders and open escalation tickets when issues cannot be resolved within 8 hours. Contains structured and unstructured data, free text fields, attachments. Has built-in ASM (Application Security Manager) for profile/access management. Supports troubleshooting, closure reports, engineering design changes, procedure changes, tech articles.

Five free-text fields selected for the prior work. Two elements being detected: customer name and fab ID. Fields are 4,000-5,000 characters each. A definitive policy exists in the application prohibiting customer confidential information entry.

### 2. Prior Work Technical Details (Revealed by Mikhail)
Far more detail than any prior set. Started with Presidio models from Microsoft. Looked at 12 models, narrowed to 5, then to 3: Transformers (Hugging Face Flair), one other (name not recalled), and Azure AI. Built as a STANDALONE SERVICE, not integrated into the application. Designed as a redaction service any application could call. Deployed on-prem Kubernetes initially. Azure AI was the only cloud component.

Reconciliation algorithm ran all three models in parallel and reconciled results. False positive rate: 21% (corrected from prior 20% figure), reduced to 17% with reconciliation. 90% detection accuracy. No golden set was created. Used customer name list, fab/location list, and acronym exclusion list (~3,000 acronyms). The full labeling exercise was estimated at 1,000+ hours and not attempted.

Existing thumbs up/thumbs down UI with approximately 1,000 labeled examples already available.

### 3. Data Labeling and Ground Truth
Extended discussion about what "known good" and "known bad" means. Colin's three-tier labeling framework: Tier 1 (word level, no context), Tier 2 (word + document context, no human explanation), Tier 3 (word + document + human reasoning). Mikhail confirmed their prior approach jumped straight to Tier 3 requirements and stalled.

Brad asked for more technical detail here. Colin used the giraffe/car analogy for data separability. The 20,000 sample benchmark for highly similar data. Techniques to reduce labeling burden (auto-categorization, generating synthetic known-bad from existing bad examples). EDA (Exploratory Data Analysis) as the method to determine if existing labeled data is sufficient.

### 4. Colin's Layered Architecture Presentation
The hybrid approach presented as layers of a funnel. Deterministic layer (Purview, regex, rule-based) catches known patterns cheaply. ML/NLP layer handles more nuanced cases. Gen AI layer handles contextual edge cases. Linear/sequential approach, not parallel. Explicitly contrasted with Lam's prior parallel 3-model approach (which Colin identified as a modified mixture of experts that does not work for this use case).

Mikhail's recognition moment: "So we just basically accidentally picked literally every single thing, one of each."

Enterprise tooling (Purview) positioned for maintenance and scalability advantages over custom scripts.

### 5. Deployment Environment Discussion
Azure confirmed for POC. Prior environment still partially running (Azure AI infrastructure, data retrieval jobs). Daniel pushed hard on disconnected/air-gapped/edge AI environments for customer fabs. Brad's directive: cloud first for the primary use case, but keep future parity with disconnected environments in mind. Colin's position: SLMs only justified for true on-prem (healthcare production, ITAR/military), not recommended otherwise.

Three deployment modes clarified: cloud (Azure), on-prem (data center server), disconnected (air-gapped fab environments). Disconnected explicitly scoped out of current POC but flagged for future.

### 6. Next Steps and POC Scope
POC confirmed on Escalation Solver with the same data and goals. Proposal by Friday (this week). Brad reviews following week, thumbs up/down by following Friday. SOW/legal process approximately one week. POC approximately two weeks from data access. Dependencies: Orion (small team on critical COS project) for some data access. Brad asked Colin to redact customer names from all documents.

---

## Proposed Deep-Dive Files

| File | Focus | Rationale |
|------|-------|-----------|
| `05_meeting_application_and_prior_work_2026-04-06.md` | Escalation Solver details, the 5 fields / 2 elements, Presidio-to-3-model journey, standalone service architecture, false positive rates, existing thumbs up/down data | This is the core scoping information. Everything about what was tried, what it was tried on, and what exists to build from. |
| `05_meeting_labeling_and_ground_truth_2026-04-06.md` | The golden set discussion, 3 tiers of labeling, Brad's questions about known good/bad, EDA approach, the 1,000 existing labeled examples, techniques to reduce labeling burden | Critical for POC scoping. The labeling approach is the biggest potential bottleneck and the area where BayOne can add the most immediate value. |
| `05_meeting_architecture_and_deployment_2026-04-06.md` | Colin's layered funnel architecture, deterministic + ML + GenAI, Purview positioning, Daniel's edge AI / air-gapped concerns, Azure vs. on-prem vs. disconnected, the "accidental hodgepodge" recognition moment | The technical approach as presented and received. Includes Daniel's future-state concerns that will shape the architecture even if out of scope for POC. |
| `05_meeting_next_steps_2026-04-06.md` | POC confirmed, proposal timeline, dependencies (Orion), SOW process, Brad's document redaction request, data access requirements | Action items and commitments made. What needs to happen and by when. |
