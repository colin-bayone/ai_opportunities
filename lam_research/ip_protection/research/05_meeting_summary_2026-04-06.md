# 05 - Meeting: Summary

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Summary

---

## Overview

Document Set 05 decomposes the follow-up discovery meeting on April 6, 2026, between BayOne (Colin Moore remote, Pratik Sharda, Anuj Sehgal, Amit Grover in person) and Lam Research (Bradley Estes, Mikhail Krivenko, Daniel Harrison in person). This was the first meeting with Daniel Harrison. The meeting ran approximately 90 minutes with a hard stop at 2:30 PM.

## Files in This Set

1. **05_meeting_people_2026-04-06.md** - Daniel Harrison's first meeting with Colin. Director of Engineering, GFSO, 30 years software development. Self-described as information gathering, not contributing. His actual contribution centered on edge AI and disconnected environment questions. Mikhail revealed as the actual technical driver of the prior ML work. Brad less dominant than the first meeting, let the technical discussion flow. Colin's strongest moment was the golden set explanation. Pat performed his wingman role.

2. **05_meeting_topic_map_2026-04-06.md** - Six major topics identified: the application (Escalation Solver), prior work technical details, data labeling and ground truth, Colin's layered architecture, deployment environment, and next steps.

3. **05_meeting_application_and_prior_work_2026-04-06.md** - The application is Escalation Solver, a homegrown escalation management platform. Five free-text fields (4,000-5,000 characters each), two elements being detected (customer name, fab ID). Prior work started with Presidio models from Microsoft, narrowed 12 models to 5 to 3 (Hugging Face Flair, SpaCy, Azure AI). Built as a standalone redaction service, not integrated into the application. Deployed on-prem Kubernetes. Reconciliation algorithm ran all 3 in parallel. 21% false positive rate reduced to 17%. 90% detection accuracy. No golden set created. Used customer name list, fab list, and ~3,000 acronym exclusion list. Existing thumbs up/thumbs down UI with ~1,000 labeled examples. Work was 18 months old.

4. **05_meeting_labeling_and_ground_truth_2026-04-06.md** - Extended discussion. Mikhail admitted no golden set existed ("we were told we have to do the labeling to create that set"). Colin explained this fundamentally limited their ceiling. Three-tier labeling framework: Tier 1 (word level), Tier 2 (word + document context), Tier 3 (word + document + human reasoning). Mikhail confirmed they jumped to Tier 3 requirements and stalled. Brad engaged deeply, asked about sample sizes and whether AI can help create the set. Colin's giraffe/car analogy for data separability. 20,000 sample benchmark for highly similar data. EDA as the method to determine sufficiency. Existing ~1,000 examples as a starting point.

5. **05_meeting_architecture_and_deployment_2026-04-06.md** - Colin presented the layered funnel: deterministic (Purview, regex) for known patterns, ML/NLP for nuanced cases, Gen AI for contextual edge cases. Linear approach, not parallel. Explicitly contrasted with Lam's prior parallel approach (identified as a modified mixture of experts). Mikhail's recognition: "So we just basically accidentally picked literally every single thing, one of each." Azure confirmed for POC, existing environment still partially running. Daniel pushed on disconnected/air-gapped environments. Brad's directive: cloud first, future parity with disconnected. Three deployment modes clarified: cloud, on-prem, disconnected. Architecture presentation compressed by Brad's hard stop.

6. **05_meeting_technical_understanding_gaps_2026-04-06.md** - Internal assessment. Daniel was the least useful person on the call, fixated on edge AI without understanding model hosting. Pat word-vomited on model training topics he does not grasp but remains valuable as relationship manager. Mikhail had a genuine turning point, recognized the prior approaches were fundamentally wrong, engaged substantively on labeling, gained credibility with BayOne. Brad showed surprisingly good technical intuition ("layers of an onion" was his phrase). Colin's golden set explanation was the strongest credibility moment.

7. **05_meeting_next_steps_2026-04-06.md** - POC confirmed on Escalation Solver with the same data and goals. Proposal by Friday (April 10). Brad reviews following week, decision by approximately April 17. SOW/legal approximately one week. POC approximately two weeks from data access. Dependencies: Orion (small team on critical COS project). Brad requested customer name redaction from all BayOne documents. Existing Azure environment and data retrieval jobs can be reused.

## Key Outcomes

### The Application Is Named
Escalation Solver. After four meetings, the entry point application is finally identified. Homegrown, accessible data, existing infrastructure, and a clear business case.

### The Prior Work Is Fully Understood
The 12-to-3 model selection, the standalone service architecture, the parallel reconciliation approach, the lack of a golden set, the 21%/17% false positive rates, the 90% detection accuracy, the 1,000 labeled examples. The prior work's fundamental limitation was the absence of ground truth, not the choice of models.

### Credibility Was Established
Colin's golden set explanation and layered architecture presentation landed. Mikhail's "accidental hodgepodge" moment was genuine recognition. Brad engaged technically for the first time. The Coherent experience as proof of production deployment resonated.

### The POC Path Is Clear
Proposal this week. SOW next week. Data access after legal. POC two weeks from access. The Orion dependency is the primary risk to timeline.

### Daniel Is Not What Was Expected
His contribution was limited to edge AI and disconnected environment concerns, which are future-state, not POC-relevant. He is a software engineering leader, not an AI/ML resource. Communication with his team should be calibrated accordingly.
