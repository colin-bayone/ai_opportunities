# 08d - Meeting: Travis Millet Technical Presentation (INTERNAL ONLY)

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt
**Source Date:** 2026-04-23 (Travis Millet discovery call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** Internal-only assessment of Travis's technical depth as presented on the call

---

**FLAG: INTERNAL ONLY.** This document is for BayOne internal use only. It must not be referenced in any client-facing communication, shared with Travis, Naoki, John Lim, or anyone at Woven or HireArt, or surfaced in any external material. It exists to inform internal resource allocation decisions.

---

## Purpose

This document records a focused internal assessment of how Travis Millet presented technically on the 2026-04-23 discovery call, based strictly on what he said on the call. The purpose is to inform BayOne's engagement posture, technical-lead time allocation, and staffing approach for the head-to-head candidate submission. It is not a judgment of Travis as an operator. His tactical strengths are real and relevant to how BayOne should engage. The narrow scope of this assessment is the technical authority he claimed and the engineering substance behind it.

---

## Travis's Technical Claims on the Call, Organized by Topic

### AutoTriage accuracy and model improvement

Travis stated that the in-house AutoTriage tool is "working 40 percent of the time, it works every time." The phrasing is a pop-culture reference to the film Anchorman. It was delivered as the primary characterization of the tool's current performance. He followed with the statement that the team is "trying to get that performance up" and that "the models just keep getting better, and the tool keeps getting better." He did not identify which models, did not identify a baseline performance measurement approach, did not describe an evaluation set, and did not name a target accuracy or a time horizon.

### Architect-level role

Travis stated directly: "We're the one building the AI-based solution. I'm one of the architects of it." He returned to this framing later in the call when describing his interest in comparing notes with other AI practitioners: "I love talking to AI companies because I can pick your brains and see how it compares to where we're at." The claim to architect-level involvement was made twice and was framed as authoritative.

### Taxonomy contrast with Waymo and Cruise

Travis positioned Woven's triage taxonomy against what he described as the industry norm: "Those are what we call static analysis or static classification, where they're just constantly kind of categorizing it to the top ... there are very broad categories, and there's only a few of them. I think GM was using 14 categories. And they're static. They don't change." He contrasted this with Woven's approach: "We have close to anywhere between 150 and 440 bugs. And they are bugs. They're not categories. They're like root cause down to the sensor data or down to the LLM that made the choice and the decision. And so they are a lot more in-depth root cause. And they're changing constantly." He framed the dynamic, expansive taxonomy as the distinguishing difficulty of Woven's problem.

### Daily ground-truth drift

Travis stated that each morning the team meets for 30 to 60 minutes to "talk to the changes from yesterday. What was correct yesterday is now wrong. Please use this process and this method instead." He presented this as an intrinsic property of Woven's problem space and as the reason outside vendors struggle with it. He did not discuss whether the drift represents taxonomy instability, inconsistent labeler calibration, underlying system change, or all three.

### Vendor landscape framing

Travis stated Woven has evaluated roughly 23 vendors, split approximately in half between "mass amounts of people, mostly in other countries" and vendors that claim they "can do this with AI." He positioned AutoTriage plus human triager buffer as necessary because the AI-only vendors cannot handle the dynamic taxonomy, and described the human buffer as avoiding the risk of stacking AI on AI.

### Response to the BayOne technical lead's framing

When the BayOne technical lead described a deterministic-first layered approach, combined methods to avoid compounded probabilistic error, track-record-based confidence scoring analogous to human assignment, and progressive offload with sampling, Travis did not engage at the architectural level. His follow-up questions were: "So is this fine tuning of existing models? Are you guys doing any training of models? Are you using commercial off the shelf?" These are questions about tooling selection, not about the proposed architectural pattern. He did not respond to the deterministic-first point, the layered combination point, the track-record-based confidence point, or the progressive offload with sampling point. He closed his engagement on the topic by acknowledging he was off on a tangent: "I sometimes get sidetracked on that because that's where I spend a lot of my day."

---

## Engineering Concerns Absent from Travis's Framing

The following concerns are first-class for any practitioner architecting a production AI classification system at the scale Travis described. None of them were raised by Travis, either in his opening framing or in his response to the BayOne technical lead.

- **Evaluation methodology.** No mention of how the 40 percent figure is measured, what the evaluation set looks like, how often it is refreshed, or how model updates are validated before promotion. "Keeps getting better" is an unquantified claim in the absence of an evaluation harness.
- **Inter-rater reliability.** No mention of how the triager team calibrates against itself. Given the claimed daily drift in ground truth and the 13x planned headcount scaling, inter-rater reliability is the primary risk to training-signal quality and is usually the first question an AI architect asks about a labeling pipeline.
- **Per-category accuracy breakdown.** No mention of whether the 40 percent is a flat average across 150 to 440 categories, whether accuracy is bimodal, whether head categories dominate performance, or whether long-tail categories are effectively at zero. A single aggregate accuracy figure across a taxonomy of this size obscures nearly all of the useful signal for architectural decisions.
- **Confusion matrix or error-mode analysis.** No mention of where the tool fails, what categories it confuses, or what the dominant error modes are. These are the artifacts that drive architectural decisions about layering, routing, and deterministic pre-filtering.
- **Taxonomy propagation procedure.** When the taxonomy changes daily, there has to be a mechanism for propagating the change to the model, to the human triager training material, and to the evaluation harness. Travis referenced the morning team meeting as the propagation mechanism for humans. He did not reference a model-side or evaluation-side propagation mechanism.
- **Model update and retraining cadence.** No mention of how the model is retrained, how often, on what signal, with what review gate, or how regressions are caught.
- **Training signal from human triagers.** No mention of how the corrections and overrides produced by the human team feed back into the model. This is the core feedback loop for a human-in-the-loop AI system. Its absence from the framing is notable.
- **Architectural alternatives to throwing headcount at the accuracy gap.** The stated plan is to hold AutoTriage at its current performance, scale the human buffer 13x to absorb the 60 percent of tickets the tool cannot handle, and hope that "models keep getting better." There was no articulation of architectural alternatives such as deterministic pre-classification for the head categories, taxonomy collapse for the long tail, specialist sub-models per category cluster, or confidence-based routing. The BayOne technical lead offered several of these and they did not land.

---

## Assessment Angles

### Language patterns

Travis's technical vocabulary on the call was consistent with surface-level AI discourse rather than with an engineering practitioner's vocabulary. The cues:

- Pop-culture phrasing for an accuracy figure that would concern any engineer. Forty percent accuracy on the core task of a tool the organization plans to bet its scaling plan on is not a figure that gets wrapped in a movie reference by someone who is architecting the system and lives with its failure modes.
- "Models keep getting better" used as a forward-looking assertion without specifying which models, on what evaluation, against what baseline, with what confidence interval, or by what mechanism.
- Difficulty framed in terms of vendor inability ("they're like, well, crap, how am I supposed to succeed at this") rather than in terms of architectural properties of the problem that would inform a solution.
- Absence of the vocabulary an AI architect uses when describing a production system under pressure: eval harness, regression, calibration, drift detection, error analysis, feature attribution, confidence calibration, fallback policy.

### Missing engineering rigor

The concerns enumerated in the prior section are not advanced concerns. They are the standard vocabulary of anyone architecting an AI classification system at production scale. Their complete absence from Travis's framing, across both his opening description and his response to the BayOne technical lead's probes, is the strongest single signal in the transcript. An architect who lives with the system day to day would reach for at least some of these concepts when describing it to a potential partner, particularly when the stated goal of the conversation is to "pick your brains."

### Architectural framing: "ground truth changes daily"

The claim that what is true today is false tomorrow is presented as an intrinsic and immutable property of the problem. An engineering-side stakeholder would parse the same observation differently. The likely causes, none of which were named, include:

- Taxonomy churn imposed by upstream process changes rather than by the problem itself. A taxonomy that changes daily is usually a taxonomy that lacks a stable definitional layer, not a taxonomy reflecting genuine daily change in the underlying system.
- Inconsistent labeler calibration across the 12-person team, producing the appearance of drift when the underlying phenomenon is variance between triagers.
- Overfitting to recent examples in whatever retraining mechanism exists, producing the appearance that yesterday's correct answer is today's wrong answer when the actual phenomenon is model-side instability.
- Genuine dynamic behavior in the upstream autonomous driving stack, which would be architecturally handleable with taxonomy versioning, time-windowed evaluation, and per-version model checkpoints.

Presenting the property as intrinsic and presenting it as the reason external vendors fail is a business-side framing. It makes the problem sound intractable in a way that justifies the current plan. It does not sound like a framing from someone actively looking for architectural leverage on the problem.

The accompanying business decision reinforces this reading: AutoTriage is held at 40 percent and the human buffer is scaled 13x to cover the gap. The stated rationale for keeping the human buffer is risk management around stacking AI on AI, which is a defensible position on its own. The absence of any discussion of attacking the accuracy gap architecturally, combined with the scale of the headcount commitment, suggests that the organization has implicitly accepted throwing people at the gap rather than re-examining the architecture.

### Response to technical probing

The BayOne technical lead presented four distinct architectural concepts within a single turn: deterministic-first layering, combined methods to avoid compounded probabilistic error, track-record-based confidence scoring with an explicit analogy to how humans build trust in assignments, and progressive offload from human to AI with ongoing sampling. Each of these is a concept that an AI architect would either recognize immediately and respond to on its own terms, or push back on specifically.

Travis's response was to ask whether BayOne is fine-tuning models, whether BayOne is training models, and whether BayOne is using off-the-shelf commercial models. These are tooling questions appropriate to someone who encounters AI systems at the level of how people talk about them publicly. They are not responses to the architectural content of what was just said. The pattern is consistent with a stakeholder who has absorbed the surface discourse of AI but does not operate in the architectural layer of it.

---

## Profile Conclusion

Travis presents as a tactical business operator who has absorbed surface AI discourse and who holds an architect-level title on an in-house AI project. The combination produces the appearance of technical depth. The depth is not present in the substance of what he said on the call.

The tactical competence is genuine and should not be discounted. Specifically:

- He opened the meeting efficiently, set the scaling problem cleanly, and placed AutoTriage and the human buffer in their correct strategic positions within his sourcing plan.
- He handled the accidental supplier-name disclosure from a Woven colleague with a clean, low-temperature recovery.
- He accepted the head-to-head framing quickly, without defensiveness, and moved the conversation to next steps.
- He kept the meeting on time and exited cleanly.

The technical authority is not visibly backed by the engineering discourse that would be expected from an architect of an AI system at Woven's scale. His value on the account is as the decision-maker on sourcing. His value is not as an architectural counterpart for BayOne's technical lead.

---

## Implications for BayOne's Engagement Posture

### Solutions-track engagement is not available through this stakeholder now

Travis does not perceive an architectural problem with AutoTriage. He perceives a scaling problem with the human buffer and a market-fit problem with AI-only vendors. From his vantage, the architecture is fine and will continue to improve on its own trajectory. A solutions conversation with BayOne technical leadership will not land on him as actionable input. It will land as interesting conversation with a vendor he enjoys talking to, and will be absorbed into his general appetite for picking the brains of AI practitioners.

### The BayOne technical lead's time on this stakeholder has diminishing returns

Further technical framing from BayOne will not change the posture of the account. The highest-leverage use of technical-lead time on this engagement is to support the head-to-head candidate evaluation and the submission packaging, not to continue engaging Travis at the architectural level. Technical-lead presence on further Travis calls should be deliberate rather than default. Attend when the agenda includes a technical evaluation component or when a specific architectural question is on the table. Do not attend purely to maintain relationship presence.

### Path back to a solutions conversation

A solutions conversation becomes available when Travis experiences a failure of his current architecture that his current approach cannot solve. Likely failure modes include an accuracy plateau that outlasts his internal credibility window, a scaling failure in the human buffer driven by inter-rater reliability collapse at 100-plus headcount, or a taxonomy-drift failure that makes retraining uneconomic. None of these are events BayOne can accelerate. The correct posture is to land the head-to-head cleanly, establish delivery credibility through the staffing motion, and remain positioned for a later conversation that may or may not arrive.

### Implications for the staffing team on the head-to-head

The head-to-head will not be won on AI differentiation. The stakeholder does not evaluate AI depth at the level that would allow technical differentiation to register. The head-to-head will be won on tactical commercial execution. Specifically:

- **Fast candidate turnaround.** Travis accepted the head-to-head with no hesitation and emphasized that the role is a backfill with immediate need. Speed of first qualified submission will be disproportionately weighted.
- **Clean submission packaging.** Resume formatting, clarity of the technical summary, and alignment to the job description will register more than candidate technical depth beyond what the role requires.
- **Reliable interview performance.** The role is a system QA position without programming requirements. Candidates who present reliably and communicate clearly in the interview loop will outperform candidates with stronger raw technical profiles who are less consistent in delivery.
- **Do not over-index on AI depth in candidate selection.** AI-adjacent background is not the differentiator on this role and will not be the differentiator in Travis's evaluation. The role requires JIRA, JQL, and some SQL. Select for those skills and for interview reliability.

---

## Open Questions

- Who on the Woven engineering side actually owns the AutoTriage architecture, evaluation harness, and retraining pipeline, and is that person reachable through any path BayOne has? If there is a real architect behind AutoTriage, that is a different stakeholder from Travis.
- What is the actual evaluation methodology behind the 40 percent figure? Is it an aggregate over all categories, is it measured against a held-out set, and is it refreshed when the taxonomy changes?
- Is the 40 percent figure directionally accurate, or is it a casual internal characterization that could be higher or lower than the measured number?
- What is the real shape of the per-category accuracy distribution, and are there category clusters where a deterministic classifier or specialist model would outperform the current general approach?
- Does Woven have any written architectural artifact for AutoTriage, and if so who holds it?
- What is the decision path inside Woven when AutoTriage does not meet the 13x scaling requirement by mid-July? Is there a point at which architecture becomes reviewable, and who reviews it?
- Does Naoki's view of AutoTriage match Travis's view, or does Naoki see the accuracy gap as an architectural issue rather than a buffer-sizing issue?
- Is there an internal Woven stakeholder whose incentives are aligned with architectural improvement rather than with headcount scaling, and is that stakeholder a better relationship target for BayOne's technical lead than Travis?
