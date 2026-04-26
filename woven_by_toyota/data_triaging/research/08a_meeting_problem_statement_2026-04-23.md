# 08a - Meeting: Problem Statement and Architectural Critique

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-24/travis_millet_discovery_2026-04-23_formatted.txt
**Source Date:** 2026-04-23 (Travis Millet discovery call)
**Document Set:** 08 (Discovery call with Travis Millet)
**Pass:** Focused deep dive on the problem statement and a technical critique of the architectural claims

---

## 1. Overview

This document decomposes Travis Millet's framing of the triage problem at Woven by Toyota as delivered during the 2026-04-23 discovery call, and attaches a technical critique of the architectural claims he made. Travis is responsible for the triage function at Woven and also serves as counterpart for the Japan-based team. He described himself as one of the architects of the in-house AI-based triage tool that the team is currently developing. The decomposition below captures specific statements, numbers, and technical claims from the call. The engineering critique that follows is for internal BayOne reference only and is not intended for external surfacing.

---

## 2. Problem Statement as Described by Travis

### 2.1 Team Scope and Current Volume

Travis confirmed that he runs the triage function at Woven and coordinates with the equivalent Japan counterpart. The current team consists of twelve people. The current throughput sits at approximately 6,000 to 7,000 tickets per month. In Travis's framing, the team's role is to work alongside an in-house AI-based auto triage tool that is "almost ready" but still maturing.

### 2.2 Target Scale and Timeline

Travis stated that the team is targeted to support a 13-times increase in volume, moving to approximately 100,000 tickets per month by mid-July 2026. This represents roughly a 13x step change in approximately three months from the date of the call. Travis described the uplift as a known commitment, not a speculative scenario, and framed the human workforce expansion as a contingency and buffer around the AI-based solution rather than as the primary path.

### 2.3 Inflow and Backlog Dynamics

Travis described the current dynamics of ticket flow in concrete terms: roughly 90 new tickets open per month and roughly 60 close from the previous month's backlog. He used this specific ratio to illustrate why some of the external vendor pitches he has heard fall apart under questioning. In his words, when he presents that inflow and closure rate to vendors who claim they can handle the problem, the response shifts from confidence to concern about feasibility.

### 2.4 In-House AI Auto Triage Tool

Travis confirmed that Woven has an in-house AI-based auto triage tool under active development. He stated that the tool is "working 40 percent of the time, it works every time," delivering the observation with a deliberately casual pop-culture framing. He followed this by saying the tool is improving as the underlying models improve and that the team has "a lot of hope" in it, while acknowledging meaningful uncertainty. He positioned the tool as the primary strategy and the human workforce as a buffer around it, with the explicit caveat that using an AI fallback behind an AI primary would be stacking risks.

Travis later identified himself as one of the architects of this tool and noted that he enjoys talking with other AI companies to compare approaches and see where Woven's tool stands.

### 2.5 Contrast with Waymo and Cruise

Travis drew an explicit architectural contrast between Woven's triage approach and that of Waymo and Cruise (noted as now part of GM). He framed those organizations as performing static analysis or static classification. In his description, their systems continuously classify incoming issues into a small set of broad categories such as hardware issue, sensor issue, perception, or planner. He stated that GM was using approximately 14 categories, and that those categories are static and do not change.

Travis contrasted this with Woven's approach, where the triage output is framed as specific bugs rather than broad categories. He stated that Woven operates with "anywhere between 150 and 440 bugs," explicitly characterized as bugs rather than categories, and further characterized as root causes pushed down to the sensor data level or down to the LLM that made the specific choice or decision. He emphasized that these root-cause bug definitions are not static but change constantly.

### 2.6 Vendor Landscape as Described by Travis

Travis stated that Woven has been evaluating approximately 23 vendors. He characterized the vendor pool as splitting roughly in half. One half relies on large human labor pools, often offshore. The other half claims an AI-based automated approach, which he identified as largely auto-labeling or auto-annotation vendors. Travis was explicit that triage as Woven defines it is distinct from auto-labeling or auto-annotation work, and that vendors in the AI half of the pool tend to retract their claims once confronted with the dynamic and granular nature of Woven's ticket flow.

### 2.7 Daily Re-Alignment Cadence

Travis described a daily operational practice in which the full triage team meets each morning for 30 to 60 minutes to align on the changes from the prior day. He framed the content of these meetings as items that were considered correct yesterday but are now considered wrong, with guidance to the team to instead apply a different process or method. He presented this cadence as a baseline property of the problem that any workforce partner or vendor would need to absorb.

### 2.8 Engagement Shape

Travis described the near-term engagement shape as a single backfill requisition for a team member who recently left. He acknowledged that the broader 13-times increase will require additional headcount, additional vendor commitments, or both, and that Woven has not yet finalized the mix between contractor, vendor, and in-house growth. He mentioned existing use of a vendor described in the transcript as "higher" (understood as HireArt) and flagged the interest in a head-to-head comparison subject to the existing disclosure constraints around the incumbent supplier. Travis noted that a mutual NDA is already in place.

### 2.9 Role Profile

Travis described the role as very much a software QA or system QA role, sometimes titled QA engineer or software QA. He clarified that the role does not require programming (no Java or C++) but does rely heavily on JIRA, JQL, and SQL where candidates have those skills. He observed that at the target pay rate of approximately 53 to 62 dollars per hour, finding engineering-degreed candidates is difficult, and that the current team holds degrees in fields such as anthropology, psychology, and sports medicine. He confirmed that the work is presently remote-friendly at his discretion, but that a future return-to-office mandate is plausible, so Woven prefers candidates physically located near the Palo Alto or Ann Arbor offices.

---

## 3. Key Quotations and Close Paraphrases

The following are the most load-bearing statements made by Travis during the call, preserved as verbatim or near-verbatim text for reference in later analysis.

- On scale: "We do something close to 6,000 to 7,000 tickets a month with this team of 12. We're supposed to 13x increase ... close to 100,000 tickets a month by mid-July."
- On the in-house AI tool: "We have been developing and testing an AI-based auto triage tool. It's working 40 percent of the time, it works every time."
- On the Waymo and Cruise contrast: "The problem with triage is, at least the way we do triage, it's a little different than Waymo, Cruise, which is now GM ... Those are what we call static analysis or static classification ... I think GM was using 14 categories. And they're static. They don't change."
- On Woven's approach: "We have close to anywhere between 150 and 440 bugs. And they are bugs. They're not categories. They're like root cause down to the sensor data or down to the LLM that made the choice and the decision."
- On inflow and backlog: "We opened 90 new tickets this month and we close 60 from last month."
- On daily re-alignment: "Each morning we meet for 30 to 60 minutes and talk to the changes from yesterday. What was correct yesterday is now wrong. Please use this process and this method instead."
- On his role with the tool: "We're the one building the AI-based solution. I'm one of the architects of it."

---

## 4. Technical Critique of the Architectural Claims (Internal Only)

The following section is an engineering assessment of Travis's framing. It is intended as internal reference for the BayOne AI practice. It is not to be surfaced to Travis or to anyone at Woven. The goal is to separate what Travis observes on the ground from what his framing implies about the underlying architecture, and to capture alternate hypotheses that better explain the observations.

### 4.1 Ground Truth Does Not Change Daily

Travis's core framing is that the ground truth of correct triage outputs changes daily, and that this is a property of the problem space rather than of the implementation. For a long-established autonomous driving development program operating at Toyota scale, this framing does not hold up under scrutiny. Specifically:

- Traffic physics do not change daily.
- Road geometry does not change daily.
- Vehicle sensor response characteristics do not change daily.
- Control system behavior does not change daily in a stable platform.
- Safety envelopes evolve at governance cadence, not at daily cadence.

A mature autonomous driving development platform should trend toward stabilization of its fundamental correctness criteria over time. The claim that correct outputs flip daily implies either an immature platform, an unstable process layered on top of a stable platform, or a conflation of different kinds of change. Treating instability as the expected steady state is either inaccurate or symptomatic of a structural problem in the triage architecture or training process.

### 4.2 More Likely Root Causes of the Daily Re-Alignment Cadence

If the team is genuinely re-aligning daily on correctness, the following hypotheses better explain the observation than "ground truth itself changes daily."

**Hypothesis 1: Overfitting to recent samples.** The in-house model is absorbing short-term sample patterns and the team is correcting for the resulting regressions. Under this hypothesis, the daily re-alignment is a symptom of an unstable model rather than a property of the problem space. This is consistent with a model that is being continually retrained on fresh examples without sufficient guardrails against distributional drift.

**Hypothesis 2: Inconsistent human trainer output.** Different triagers produce inconsistent labels for substantively similar tickets. The daily re-alignment papers over inter-rater drift rather than tracking a legitimately shifting external ground truth. Under this hypothesis, the underlying disagreement is between humans on the team and not between yesterday's world state and today's world state.

**Hypothesis 3: Taxonomy churn, not ground truth churn.** The bug category definitions themselves are being refined continuously. What Travis frames as yesterday-correct-now-wrong is actually yesterday-labeled-A-now-relabeled-B because the meaning of A has shifted. This is a process problem, not a ground truth problem. A stabilization pass on the taxonomy itself would substantially reduce the apparent churn.

**Hypothesis 4: Overly granular root-cause decomposition.** Defining 150 to 440 distinct root-cause bug categories creates category boundary ambiguity at scale. Many real tickets will sit on or near the boundary between multiple categories, and which side of the boundary they fall on becomes a negotiated judgment rather than an objective call. A coarser top-level taxonomy with sub-tags for the granular root-cause detail would preserve the detail while stabilizing the primary classification.

### 4.3 The 40 Percent Accuracy Figure

The reported 40 percent accuracy of the in-house tool is consistent with the above critique. An overfit model against an unstable label set produced by an inconsistent human trainer pool is expected to land in that range. That figure should be read as a signal, not as a baseline capability of the underlying model. Before an external partner can make credible claims about lifting accuracy, it is important to understand whether the 40 percent is a cumulative accuracy across all bug categories, a per-category average, or an accuracy weighted by volume. It is also important to understand whether accuracy is measured against a frozen gold-standard set or against the drifting daily-adjusted labels.

### 4.4 Implications for BayOne Positioning

The BayOne technical lead's framing on the call emphasized keeping the pipeline deterministic for as long as possible, layering methods rather than stacking probabilistic decisions, and reserving generative AI for fringe cases at the end of the pipeline. That framing maps directly onto the hypotheses in 4.2. Specifically, the deterministic-first approach stabilizes the upstream classification surface, which reduces the surface area where daily re-alignment is needed. The layered-methods approach reduces error multiplication, which is a likely contributor to the 40 percent figure. The late-stage generative AI approach contains model non-determinism to the places where it actually adds value.

This positioning should be held as an internal reference while the engagement matures. The critique itself should not be surfaced to Travis. Travis is the architect of the tool that the critique targets, and surfacing it during the sales motion would damage the relationship without producing useful reflection.

---

## 5. Open Questions

The following open questions are specific to the problem statement and architectural claims captured above. These should be answered, ideally through further discovery conversations, before any architectural recommendations are made.

1. Is the 40 percent accuracy figure measured cumulatively across all 150 to 440 bug categories, or is it an average of per-category accuracies, or is it weighted by ticket volume per category?
2. Is accuracy measured against a frozen gold-standard labeled set, or against the drifting daily-adjusted labels produced by the team?
3. What specifically changes during the daily 30 to 60 minute re-alignment meetings? Is the team adjusting ground truth labels, refining taxonomy definitions, recalibrating trainers against each other, or some combination of the three?
4. Does Woven measure inter-rater reliability among its twelve triagers? If so, what is the current figure, and how has it trended over the last six months?
5. How is the 150 to 440 bug category list curated? Is there an owner of the taxonomy, a versioning process, and a formal change-control mechanism?
6. How are new bug categories introduced, merged, or retired, and at what cadence?
7. What is the split between tickets driven by sensor data anomalies, perception or planner errors, and generative AI decision points? This split shapes the extent to which the pipeline can be stabilized with deterministic methods upstream.
8. What is the actual target accuracy for the in-house AI tool at mid-July 2026 given the 13-times volume increase? A 40 percent tool against 100,000 tickets per month implies 60,000 monthly tickets falling to human review, which is ten times the team's current total throughput.
9. What governance process exists, if any, for stabilizing the correctness criteria on which both the AI tool and the human team are trained?
10. To what extent does the Japan counterpart team apply the same taxonomy and the same daily re-alignment practice, and how is taxonomy divergence reconciled across sites?
