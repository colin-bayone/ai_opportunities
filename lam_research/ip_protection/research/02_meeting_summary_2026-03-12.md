# 02 - Meeting: Summary

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Summary

---

## Overview

Document Set 02 decomposes the discovery call between BayOne (Colin Moore, Pratik/Pat) and Lam Research (Bradley Estes, Mikhail Krivenko) on March 12, 2026. Mikhail led a whiteboard presentation of the problem statement while Brad controlled the room and enforced boundaries. The call covered two distinct business cases, prior technical attempts, infrastructure landscape, and engagement appetite.

## Files in This Set

1. **02_meeting_people_2026-03-12.md** - Brad (Managing Director, room controller, owns everything end-to-end), Mikhail (Head of Product, technical problem presenter), Pat (active participant, ingestion/ecosystem questions), Colin (technical lead, strong moments and one redirect). Daniel, Christian, and Monica referenced but not present.

2. **02_meeting_topic_map_2026-03-12.md** - Five major topics identified from Pass 1, with proposed deep-dive files and rationale for each.

3. **02_meeting_technical_use_cases_2026-03-12.md** - Two distinct business cases mapped to Mikhail's troubleshooting workflow. Use Case 1: Self-help search redaction (batch, accuracy-focused, heavy-handed, over-redaction acceptable). Use Case 2: Ask-for-help/escalation detection (real-time, 2-5 second performance constraint, false positive rate must be well below 1%, notification not blocking). Detection vs. redaction distinction. Feedback loop driving down escalations. MVP scope: two fields only (customer name, file name).

4. **02_meeting_what_was_tried_2026-03-12.md** - Three models tested (Transformers, SpaCy, Azure AI) via MLOps on Azure cloud. 20% false positive rate, fine-tuned to only 17%. Rule-based models abandoned due to spelling variations (F11, Fab 11, FAB-11, etc.). 1,000+ hour labeling exercise paused. GenAI explicitly not tried due to unstructured output concern. Colin's "out-of-the-box ChatGPT" diagnosis reframed Lam's failure as a fundamentally limited approach, not failed execution.

5. **02_meeting_infrastructure_and_access_2026-03-12.md** - Extreme fragmentation: on-prem + cloud, LamGPT, Copilot, cloud bots, 6+ search systems, no unified data lake. "Flows not systems" framing from Mikhail. IAM approximately 2 years in, not robust. ASM governs some sensitive areas but not enterprise-wide. Employee categories: blue badge, contractors, LSPs, trade-restricted, embargo country. Over-restriction creates a self-reinforcing cycle: no detection leads to blanket restriction leads to siloed data leads to no training data leads to no detection.

6. **02_meeting_business_opportunity_2026-03-12.md** - Brad owns everything end-to-end (business, product, program, technical), unusually consolidated authority for a $17B company. Open to "any and all approaches" with trade-offs understood. Wants rapid prototyping, incremental, evolutionary. Technology agnostic. Previous "pod" pilot was not standard operating mode. Follow-up meeting planned with broader team including Daniel. Transcript cuts off mid-answer on "high value targets" question, the most critical missing data point.

7. **02_meeting_speaker_dynamics_2026-03-12.md** - Brad's meeting: set the format (whiteboard, not slides), controlled pace, redirected speakers. Mikhail as precise technical translator. Colin's best moment: 20%/ChatGPT diagnosis (confirmed by Mikhail revealing the 17% number). Colin's worst moment: IAM tangent earning Brad's "Is that clear, Colin?" Brad's vendor scar tissue: "we've heard it before." BayOne team performance solid but uneven.

## Key Findings from the Discovery Call

### The Problem Is Well-Defined
Mikhail presented two clear, distinct business cases with different technical requirements. This is not a vague "help us with AI" request. They know exactly what they need: (1) batch redaction to open up cross-customer knowledge, and (2) real-time detection to notify users of potential policy violations.

### Prior Approaches Were Fundamentally Wrong
The 20% false positive rate from Transformers/SpaCy/Azure AI models represents generic NER applied to a domain-specific problem. Semiconductor IP (customer names, fab identifiers, process parameters) is not in any model's training data. Colin correctly diagnosed this as out-of-the-box performance with no real fine-tuning benefit.

### The Infrastructure Is a Challenge but Not a Blocker
Extreme fragmentation means any solution must work across diverse systems. But Brad scoped the MVP to "within our systems," avoiding cross-org complexity. The unified control plane concept resonated but needs to be positioned carefully.

### Brad Controls Everything and Has Been Burned Before
Consolidated decision authority means fast deal velocity if we pass the credibility gate. The credibility gate is: demonstrate understanding of the problem before proposing solutions. "We've heard it before" is the warning signal.

### The Transcript Cut Off at a Critical Moment
Brad was naming his "high value targets" (which platforms to tackle first) when the recording ended. This is the most important missing data point for scoping.

## Open Questions After Set 02

1. What are Brad's high value targets? (Lost to transcript cutoff)
2. Who executed the prior ML work? Internal team or external vendor?
3. What is the training data composition for the models that achieved 20%?
4. What are the exact two fields for MVP scope? (Customer name confirmed, file name confirmed)
5. What does Daniel (technical lead) think about the problem and prior approaches?
6. What other systems exist beyond what Brad's org owns?
7. What is the timeline pressure? (Not directly answered on this call)
