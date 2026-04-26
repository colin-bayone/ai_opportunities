# 01b - Meeting: Problem Statement and Hypotheses

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-23/woven_internal_sync_2026-04-13.txt
**Source Date:** 2026-04-13 (Internal BayOne sync between Colin Moore, Jesse Smith, and Pratik Sharda)
**Document Set:** 01 (Internal sync meeting)
**Pass:** Focused deep dive on the data triaging problem statement and Colin's labeling-vs-correlation hypothesis

---

## 1. Context for the Conversation

The Woven by Toyota opportunity surfaced through an informal in-person lunch between Pratik Sharda and a senior leader on the Woven procurement and sourcing team. During that lunch, Pratik learned that a Statement of Work ("SOW") was inbound for a team responsible for data triaging in Woven's autonomous-vehicle testing program. The named internal stakeholder driving the need is Travis Millet. Pratik's internal sync with Colin Moore and Jesse Smith on 2026-04-13 was explicitly framed as a brainstorm: how should BayOne approach the upcoming discovery conversation with Travis, and what posture should BayOne take into the call?

Colin's stated goal for the meeting was to understand the shape of the data and the desired outcome before proposing any solution. This document captures the problem-statement discussion in detail, with emphasis on Colin's hypothesis that the underlying work may not be pure labeling.

## 2. What Pratik Was Told About the Data

Pratik's description of the data is drawn entirely from his recollection of the lunch conversation with the senior procurement leader. Because the conversation was in person and over a meal, Pratik was unable to take notes, and he explicitly framed what he relayed as "the assumption is what I could capture."

The data that Woven's test-operations team is working with, as Pratik described it, includes the following attributes:

- **Driving paths** taken by the autonomous vehicles during test runs.
- **Visuals** captured by the vehicles (implied camera footage from the autonomous driving stack).
- **Anomalies of the vehicle** observed during testing, meaning deviations in how the vehicle itself is behaving.
- **Telemetry** from the autonomous system, including sensor-derived signals tracking vehicle state.
- **Fringe cases** that emerge during test runs.
- **Manually added cases** that operators inject into the system.

The data is captured by the operations team that physically runs the test vehicles. Pratik described these operators as "the operations guy, right, who are running these cars, they take them out, a lot of data is captured, transferred, so a lot of ingestion happens there." The combination of driving paths, visuals, telemetry, vehicle anomalies, fringe cases, and manually added cases all sits with this operations team and flows into the team Travis Millet oversees.

Pratik also positioned Woven inside Toyota's broader strategic context. Toyota is, as of today, the world's largest automaker, and Woven is Toyota's vehicle for catching up with Tesla and other next-generation electric and autonomous competitors. Pratik described Woven as focused on autonomous driving, camera-based perception, Advanced Driver Assistance Systems ("ADAS"), and what he called "software-defined automotive architecture." He was explicit that Toyota has fallen behind on parts of this technology stack and that Woven is the push to close that gap.

## 3. Pratik's Explicitly Acknowledged Knowledge Gaps

A notable feature of the conversation is that Pratik was forthright about the limits of what he had actually learned. When Colin asked what kind of data needs to be labeled, whether it is logs, or whether it is something generated while the car or a system of the car is running, Pratik's direct reply was:

> "So the answer to that is I don't know, which is the honest answer."

Pratik then qualified further that he was working from memory of an in-person lunch conversation where note-taking was not possible, and that his description was "the assumption is what I could capture." He reiterated the knowledge gap a second time later in the same exchange:

> "The honest and straight answer is no, I don't know what all data they're capturing and they're trying to label. But that's something we can discover together on that call."

Taken together, the specific items Pratik explicitly acknowledges he does not know include:

- What specific sensors are involved. Pratik referenced telemetry "within the autonomous system" and then conceded "they could have much more sensors that I'm not aware of."
- What the data volumes look like.
- What attributes are actually being labeled.
- What the team does with the labeled output today.
- Whether the work should properly be framed as labeling at all, versus some adjacent problem such as correlation or root cause analysis.
- Whether the existing approach inside Woven is classical and potentially obsolete, or something more modern. Pratik states his belief that it is likely "classical, older, obsolete," but frames that as inference rather than direct knowledge.

Pratik also noted that the procurement contact never used the word "AI" during the lunch conversation: "they didn't even bring the AI word there. They were just talking about the problem statement they had." The AI framing is BayOne's inference, not a client ask.

## 4. Colin's Three-Item Framework

Midway through the meeting, Colin signaled that he needed to lay out a coherent structure before the group reacted piecewise. He said:

> "One thing that we can do, let me get through, I have three items, let me get through them, because they'll be important together. On their own, they won't make sense, but together they don't make sense."

The three items, as Colin presented them, are as follows.

### Item One: Colin Should Be on the Travis Discovery Call

Colin believes it will be valuable for him to be present on the first discovery call with Travis Millet rather than having BayOne meet the client and then bring Colin in later. His reasoning is that he can ask the domain-specific engineering questions required to understand what the data actually looks like and what the team wants to do with it.

### Item Two: Understand the Data and Desired Outcome Before Pitching

Before BayOne goes into "show and tell mode," Colin wants to understand what the Woven team is trying to accomplish with the data. He hypothesizes that the team is a traditional engineering and operations group that has data flowing in and is looking at it in a conventional way. In Colin's own words:

> "If I'm going to hazard a guess, it's probably a traditional, you know, engineering. kind of ops team that's here, that's got this data coming. They're probably looking at it in a more traditional sense. There's probably like what they would call as like a root cause analysis or other things like different conditions relating to some outcome. So in that case, maybe not labeling. Labeling is a word you could use for it, but maybe it's more of a correlation."

This is the core hypothesis: that the underlying problem is not pure labeling but rather a correlation or root cause analysis task in which the team is attempting to tie different conditions to specific outcomes observed in the vehicles. Colin continues:

> "kind of map that they want, which we can do. I mean, it's still labeling at the end of the day. It's just a subclass of labeling."

Colin explicitly qualifies that labeling is still a valid framing even if the underlying work is correlation or root cause analysis. The point is not that labeling is wrong, but that labeling is the broader umbrella under which the more specific task sits. Correlation and root cause analysis are, in Colin's framing, a subclass of the broader labeling or categorization problem. If BayOne understands which subclass is actually in scope, the proposal can be targeted. If BayOne does not understand which subclass is in scope, the proposal risks being generic labeling when the client actually needs something sharper.

Colin then states the risk of mis-framing directly:

> "what would be a bad thing is if we think it's labeling and we go with a different kind of labeling and we missed the mark with them."

This sentence captures the core risk driving the discovery-first posture. If BayOne walks in positioning a generic labeling solution and Travis's team actually needs correlation or root cause mapping, the pitch misses. Colin's remedy is to extract enough detail on the call to give Woven "something very focused back," rather than a generic pitch.

### Item Three: Internal Staffing Capacity

Colin's third item is the hardest. If the work turns out to be labeling-labeling in the pure sense, BayOne's current AI team is capacity-constrained. Colin describes having spent five months pushing leadership ("the powers that be") for additional headcount without result. This item is relevant to the problem-statement discussion only insofar as it reinforces why Colin wants to understand the problem shape before committing: the solution shape determines the staffing shape, and BayOne's ability to deliver varies depending on which shape is required.

## 5. The Risk of Mis-Framing the Problem

Colin's hypothesis carries a specific downside risk that is worth stating plainly. If BayOne approaches Woven with a labeling-centric pitch (for example, human plus AI annotation of camera frames or telemetry events), and Travis's team actually needs a system that correlates driving conditions, telemetry signals, and vehicle anomalies to identify root causes for observed test outcomes, the pitch will be perceived as a mismatch. The solution shapes are genuinely different:

- **Labeling as classification or annotation** implies a workflow of data, annotators, label schemas, quality assurance, and tooling such as label management platforms. The deliverable is labeled data.
- **Correlation or root cause analysis** implies a workflow of feature extraction across multi-modal data, statistical or model-based correlation, and engineering review of candidate root causes. The deliverable is an explanation or a ranked causal map.

Labeling can be a component of the correlation workflow (for example, labeling anomaly types so that correlation models have targets), which is why Colin allows that labeling is "still a valid framing" and calls correlation a "subclass of labeling." But a proposal that stops at labeling leaves the higher-value analytic layer on the table, and a proposal that leans heavily on annotation workforce when the client actually needs analytic modeling will misread the client's intent.

This drives BayOne's discovery-first posture for the Travis call: gather enough detail on data shape and desired outcome to choose the right solution framing, then propose.

## 6. Classical-vs-AI-Hybrid Framing of the Eventual Proposal

Pratik's working hypothesis, which Colin did not contest, is that Woven's current approach to the problem is likely classical and potentially obsolete. In Pratik's words:

> "they might be going in a path which is much more... like classical, older, obsolete, but we can do a hybrid where we are not saying just do it with AI, we are saying do it together. You can give us this piece as well while we work on this AI part of it and which could be a longer term solution for them."

The proposed BayOne framing therefore has two tracks:

1. **Immediate SOW support.** Woven has an inbound SOW calling for three to four people to work on the data triaging project. BayOne intends to support that staffing need in the near term. Jesse framed this as "the immediate part of it to fill those positions while simultaneously understanding what the long-term piece of it is."
2. **Longer-term hybrid solution.** Parallel to filling the SOW, BayOne positions a hybrid human plus AI approach as the longer-term solution, displacing or augmenting the classical path the team appears to be on today. Pratik was emphatic that this longer-term play is the larger opportunity: "here the play is even bigger and longer term is what I'm saying."

The hybrid framing preserves optionality. It supports the immediate SOW (which is already budgeted and moving through procurement) while opening the door for a more substantial AI-led engagement once BayOne has earned the right to that conversation by demonstrating competence on the SOW work.

## 7. Concrete Data Questions to Answer on the Travis Discovery Call

Before BayOne can propose a solution shape, the following questions need answers on the Travis Millet discovery call. These are derived directly from the hypotheses Colin raised and the knowledge gaps Pratik acknowledged.

**Data shape questions**

- What specific sensor modalities are in scope (camera, LiDAR, radar, Inertial Measurement Unit, Global Navigation Satellite System, Controller Area Network bus, others)?
- What is the format of the captured data (time-series logs, video, structured event records, a mix)?
- What are the data volumes per test run, per vehicle, per day?
- What is the current ingestion and storage path for the data once operators bring the vehicles in?
- Are the driving paths, telemetry, visuals, and anomaly records linked to a common identifier (for example, run identifier, vehicle identifier, timestamp), or are they currently siloed?

**Problem-framing questions**

- What does the team actually do with the data today? What is the current workflow end-to-end?
- Is the team attempting to classify events, label frames or segments, identify anomalies, or correlate conditions to outcomes? If it is more than one of these, which is the primary pain point?
- Are fringe cases and manually added cases being flagged for a downstream model training loop, for engineering review, or for regulatory or safety documentation?
- What does a successful output look like? A labeled dataset, a root cause report, a triaged ticket queue, a model, or something else?

**Scale and throughput questions**

- How many test vehicles are in operation, and what is the cadence of test runs?
- How many cases (fringe or manually added) flow into the team per week? What is the current backlog?
- How many people are on the team today, and how is work allocated among them?

**Current-state and tooling questions**

- What tools or platforms does the team use today for triage, labeling, or analysis?
- Is there any existing machine-learning infrastructure (for example, a labeling platform, a feature store, a model training pipeline)?
- Has the team previously attempted an AI-assisted approach, and if so, what was the outcome?

**Outcome and success-criteria questions**

- What would "faster" or "better" triaging actually look like in terms of measurable outcomes (throughput, accuracy, time-to-root-cause, engineer hours saved)?
- What decisions downstream of the triaging team depend on the output (safety certification, engineering change requests, software releases, other)?
- Is there a budget frame or timeline frame already attached to the SOW that constrains the solution shape?

## 8. Open Questions Specific to This Topic

The following questions are raised but not resolved by the 2026-04-13 sync and remain open pending the discovery call or further internal discussion.

- Whether Woven's existing approach is in fact classical and obsolete, or whether the team already has a non-trivial AI or modeling component that Pratik simply did not hear about over lunch.
- Whether the three to four people called for in the inbound SOW are intended to perform labeling-style annotation work, analyst or engineering work, or a mix, and therefore what skill profiles BayOne should line up for the staffing portion of the engagement.
- Whether Travis Millet himself views the problem as labeling, as correlation or root cause analysis, or as something else entirely. Pratik's description is filtered through a procurement intermediary, not through Travis.
- Whether the procurement sponsor will in fact secure a meeting with Travis, given Jesse's observation that historically "we have not got a lot of traction from him."
- Whether BayOne can cleanly separate the immediate SOW staffing conversation from the longer-term AI hybrid conversation, or whether the procurement channel will force both into a single commercial vehicle.
- Whether any portion of the problem is regulated (for example, safety-critical data governance around autonomous-vehicle test records) in a way that would constrain solution design before discovery even begins.
