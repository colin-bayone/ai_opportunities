# 08d - Meeting: Travis Millet's Technical Presentation

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt
**Source Date:** 2026-04-23 (Travis Millet discovery call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** Assessment of Travis's technical framing on the call, what he said, and how it reads from an engineering perspective

---

## Purpose

This file documents what Travis Millet said about the technical architecture and how he presented technically on the call. It is captured as an internal factual record. The assessment matters because it shapes whether there is a viable solutions conversation at Woven through this stakeholder, and whether the technical framing presented by the BayOne technical lead landed against a peer evaluator or against a business stakeholder using technical language.

## Technical Claims Travis Made on the Call

The following technical claims were presented by Travis, in roughly the order they appeared.

### On the In-House AI Triage Tool (AutoTriage)

- The tool operates at approximately 40 percent accuracy.
- Framed the accuracy as "it works 40 percent of the time, it works every time." This is a pop-culture reference from a film comedy, used casually rather than as engineering commentary.
- Stated that the tool keeps getting better and the models keep getting better, without specifying which models, what fine-tuning approach, or what evaluation methodology is in use.
- Stated he is "one of the architects" of the tool.

### On the Problem Being Different from Other AV Developers

- Drew a contrast between Woven's triage approach and that of Waymo, Cruise (now GM), and other AV shops.
- Described the other developers as using static classification into 14 or so broad categories.
- Described Woven's approach as dynamic root-cause analysis across 150 to 440 categories that change continuously.
- Used this contrast to explain why the 20-plus product vendors Travis has talked to cannot do the work.

### On Ground Truth Changing Daily

- Stated that ground truth correctness shifts daily.
- Stated that the team meets daily for 30 to 60 minutes to align on what changed.
- Framed this as an intrinsic property of the problem.

As examined in `08a_meeting_problem_statement_2026-04-23.md`, this framing does not hold up technically. For a long-established AV program, fundamental ground truth rules should not shift daily. Daily re-alignment is more consistent with overfitting, inter-rater drift, taxonomy churn, or an overly granular category decomposition than with a genuinely shifting ground truth.

### On Vendor Evaluation

- Described conversations with 23 vendors.
- Described half of them as providing human labor pools and the other half as providing AI-only auto-labeling or auto-annotation.
- Noted that when confronted with the actual ticket open and close rates (90 opened per month, 60 closed from the prior month), the vendors recognized they could not meet the need.
- Did not describe any architectural evaluation criteria applied to the vendors.

### On Training Approach

When asked follow-up questions by the BayOne technical lead about training methodology:

- Responded with a question back: whether BayOne uses off-the-shelf models, fine-tuning, or custom training.
- Did not describe Woven's own training methodology in any detail beyond referencing that the models keep getting better.
- Did not describe evaluation or validation methodology for AutoTriage.
- Did not describe how training signal from human triagers feeds back to the model.

## Assessment of Technical Depth

Travis's technical depth, as presented on the call, is limited relative to the role he described ("one of the architects") and relative to the complexity of the problem. Specific observations supporting this assessment:

### Language Patterns

- Relied on surface-level technical vocabulary without depth probes. Referenced "models getting better" without specifying models or metrics.
- Used pop-culture phrasing for what should be an engineering concern (the 40 percent accuracy figure).
- Framed the problem difficulty in terms of what other vendors can or cannot do, rather than in terms of architectural properties or measurable technical characteristics.

### Missing Engineering Rigor

- No mention of evaluation methodology. How is the 40 percent measured? Across what test set? Is it the same test set over time or regenerated?
- No mention of inter-rater reliability among the current 12-person team. With 150 to 440 dynamic categories and daily re-alignment meetings, inter-rater reliability would be a core operational metric.
- No mention of confusion matrices, per-category accuracy breakdowns, or any signal that the team distinguishes which categories the model handles well from which it does not.
- No mention of how changes to taxonomy propagate through already-labeled data or already-trained model weights.

### Architectural Framing

- Travis's one-liner about ground truth changing daily is the kind of framing a business-side stakeholder uses to make a problem sound intractable. An engineering-side stakeholder would typically reach for causes (overfitting, inconsistent trainers, taxonomy instability) rather than framing the instability as a feature of the problem.
- The acceptance of 40 percent accuracy as adequate, paired with the plan to scale the human buffer 13x, suggests the architectural response to accuracy limitations is to throw headcount at the gap. A deeper engineering lens would treat the accuracy plateau as a signal to re-examine the architecture.

### Response to Technical Probing

- When the BayOne technical lead described deterministic-first layering, progressive offload, and track-record-based confidence scoring, Travis engaged at the level of follow-up questions about fine-tuning and off-the-shelf models. He did not engage on the deterministic-layering or confidence-scoring ideas, which are architectural rather than model-level.
- This pattern is consistent with someone who understands AI at the level of how people talk about AI publicly, rather than at the level of how AI systems are actually architected.

## Profile as Assessed from the Call

Travis presents as a tactical business operator who has absorbed the surface layer of AI discourse and who holds an architect-level title on an in-house AI project. The combination creates the appearance of technical depth, but the depth is not present in the content of what he said on the call.

The tactical sharpness is genuine. His management of the meeting (setting the cap, controlling topic flow, tactically accepting the head-to-head, recovering cleanly from the vendor disclosure slip) reflects business skill. The technical authority he claims is not visibly backed by the engineering discourse one would expect from an architect of an AI system at Woven's scale.

## Implications

### For BayOne's Engagement Posture

- There is no solutions conversation to have with this stakeholder. The stakeholder does not perceive an architectural problem and does not evaluate architecture at the depth required to recognize one.
- Any technical framing BayOne presents to this stakeholder will be received as interesting conversation, not as actionable input. The BayOne technical lead's time on this stakeholder has diminishing returns.
- The path back to a solutions conversation requires Travis to experience a failure of his current architecture that his current architecture cannot solve. That is not a timeline BayOne can accelerate or predict.

### For the Team Staffing This Head-to-Head

- Candidate evaluation for the backfill role should not over-index on AI depth. The role itself, as described by Travis and in the JD, is functionally a software QA role that uses AI tools (calling AI agents via API is a preferred, not a required, qualification). A candidate who can execute the tactical QA work reliably at the stated rate is more likely to succeed in this environment than an AI-forward candidate who may find the environment frustrating.
- The stakeholder responds to tactical commercial execution. Fast candidate turnaround, clean submission packaging, and reliable performance at interview will do more to win the head-to-head than technical differentiation narratives.

## Internal Note

This file is for internal reference only. Nothing in it should surface to Travis, to Naoki, to anyone at Woven, or to anyone at HireArt. It is a factual record to inform how BayOne's internal team allocates attention across this engagement.
