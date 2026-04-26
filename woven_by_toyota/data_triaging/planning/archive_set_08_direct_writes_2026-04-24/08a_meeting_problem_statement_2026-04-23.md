# 08a - Meeting: Problem Statement Confirmed

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt
**Source Date:** 2026-04-23 (Travis Millet discovery call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** What the work actually is, the scale, and a technical critique of the architecture as described

---

## The Work, in Travis's Framing

Triage at Woven is described as dynamic root cause analysis, not static classification or annotation.

- Anywhere between 150 and 440 distinct bug categories at any given time.
- The categories are bugs, not broad categories. They are framed as root causes down to the sensor data or the LLM decision that produced the incorrect outcome.
- The categories change constantly. Travis referenced daily 30 to 60 minute team meetings to align on what was correct yesterday versus what is now considered wrong.
- 90 new tickets opened per month. 60 closed per month from the prior month's backlog.

This is the shape of the work. It is consistent with the root cause analysis language that appears verbatim in the HireArt job description analyzed separately in `08e_source_hireart_jd_analysis_2026-04-23.md`.

## Contrast with Other AV Developers

Travis contrasted Woven's triage model with that of Waymo, Cruise (now GM), and other AV shops that BayOne's conversations with those vendors touched on indirectly:

- Waymo, Cruise, and similar: static classification into broad categories. GM was referenced as using 14 categories. Categories do not change over time.
- Woven: 150 to 440 dynamic categories at root-cause depth, changing continuously.

The distinction is accurate insofar as it describes a harder technical problem than static classification. The distinction does not, however, justify the architectural approach currently in use, which is examined below.

## Scale and the 13x Growth Target

- Current throughput: 6,000 to 7,000 tickets per month across a team of 12.
- Target throughput: approximately 100,000 tickets per month by mid-July 2026.
- Implied growth: roughly 13x in three months.

The stated path to that growth is a combination of continued development of the in-house AI triage tool (AutoTriage) and expansion of the human buffer behind it. The composition of the human expansion (contractor vs vendor, how many, sourced from where) was described as still being figured out.

## The In-House AI Triage Tool

Travis described the in-house AI triage tool as operating at roughly 40 percent accuracy today and improving over time. The tool is framed as the primary solution, with the human triage workforce as the buffer behind it.

- Accuracy: approximately 40 percent.
- Posture toward the accuracy figure: described casually, with a pop-culture phrasing that signaled limited engineering urgency despite the accuracy level.
- Human buffer: positioned as Plan B or as a backup layer behind the AI.

The HireArt JD (see `08e`) states that the human triage workforce will also generate "expert level bug reports for use with our in-house AI triage tool." The human workforce is therefore both a buffer and a training signal generator for the AI tool.

## Technical Critique of the Architecture as Described

Travis's framing of the problem contains a claim that does not hold up under scrutiny. It is preserved here because it matters for assessing whether the current architecture is sound.

### The Claim

Travis stated that ground truth rules change every day. He framed this as an intrinsic property of the problem and a reason why many vendors cannot do the work. He also stated that his team holds a daily 30 to 60 minute meeting to re-align on what is correct versus incorrect.

### Why the Claim Does Not Hold

For a long-established autonomous driving development program at Toyota scale, fundamental ground truth rules should not change daily. Traffic physics do not change daily. Road geometry does not change daily. Vehicle sensor response does not change daily. Control system behavior does not change daily in a stable platform. Safety envelopes evolve at governance cadence, not at daily cadence.

If the team is genuinely re-aligning daily on what constitutes correct output, one of the following is likely:

1. **Overfitting to recent samples.** The AI model is absorbing short-term sample patterns and the team is correcting for regression. Daily re-alignment is then a symptom of an unstable model, not a property of the problem.
2. **Inconsistent human trainer output.** Different triagers are producing inconsistent labels. Daily re-alignment becomes necessary to paper over inter-rater drift rather than to track a legitimately shifting ground truth.
3. **Taxonomy churn, not ground truth churn.** The bug category definitions are being refined continuously. This is a process problem, not a ground truth problem.
4. **Overly granular root-cause decomposition.** Defining 150 to 440 root-cause bug categories creates category boundary ambiguity that requires constant re-arbitration. The alternative is a coarser category taxonomy with sub-tags for detail.

A mature platform should be trending toward stabilization. Travis's framing treats instability as the expected steady state, which is either inaccurate or symptomatic of a structural problem with the triage architecture or the training process. The accuracy figure (40 percent) is consistent with this critique.

## Why the Architecture as Described Matters

The architectural critique is not intended for surfacing externally. It is captured here for the following reasons:

- It informs the assessment that there is no solutions play in this engagement. The stakeholder does not perceive an architectural problem.
- It explains why BayOne's technical framing on the call (deterministic layers first, combined methods, progressive human-to-AI offload, track-record-based confidence scoring) did not produce commercial traction. The stakeholder does not appear to be looking for an architectural re-think.
- It documents a technical position that can be referenced later if the architecture fails to scale and the conversation returns.

## Open Questions After This File

- Whether the accuracy figure of 40 percent is cumulative across all 150 to 440 categories or specific to particular categories.
- Whether the daily re-alignment meetings are adjusting ground truth, adjusting taxonomy, or adjusting trainer calibration. The transcript did not distinguish.
- Whether any measurement exists of inter-rater reliability across the current 12-person team.
- What specific sensor data and signal types dominate the triage workload (a question raised on the pre-meeting sync and not definitively answered on the call).
