# 05 - Discussion: What BayOne Wants from This Engagement

**Source:** Working discussion between Colin Moore and Claude, 2026-04-23
**Source Date:** 2026-04-23 (recorded before the 3:30 PM PST discovery call)
**Document Set:** 05 (Strategy discussion before the Travis Millet discovery call)
**Pass:** Opening topic on what shape of win BayOne is actually playing for

---

## Framing

Before the discovery call, the strategic question that needs alignment is what shape of win BayOne is playing for. This was one of the standard Flow 6 opening questions and it is now the most important one given what Set 04 revealed about Woven's maturity.

## Claude's Perspective

The picture that emerged from Set 04 changes the calculus of this engagement in a specific way. Going into Set 01 and Set 02, the mental model was roughly "Woven has a data triaging problem they have not figured out; BayOne has an AI-shaped solution; the question is whether BayOne can get in front of the right person to pitch it." That was wrong. Woven has largely figured out their data triaging problem at a platform level. They operate AutoTriage with GenAI and human-in-the-loop at reported 80 percent accuracy, they run Union.ai for orchestration on petabytes, they are an Encord annotation customer, they have a dedicated Data Annotation and Labeling Engineering team, and the day before this call they announced a major Woven City AI stack including a Data Fabric. The 3-4 person SOW is therefore not a green-field platform build. It is almost certainly some combination of capacity increment, quality or integration work, ontology-change-driven surge, or residual labeling that AutoTriage cannot absorb.

This reshapes what a win looks like, and there are at least three distinct shapes to pick from.

**Shape A: Pure solutions conversion, walk if it is not there.** Colin attends, listens to Travis frame the problem, identifies whether there is a solutions-shaped engagement hiding in what looks like a staffing ask, and either converts the conversation to that or steps back. If it is purely capacity augmentation, BayOne lets Jesse and Pratik run the staffing conversation without Colin's continued involvement. The win here is a properly scoped solutions engagement or no engagement. The risk is that Woven already has enough internal capability that even a solutions-shaped engagement is hard to carve out.

**Shape B: Accept the capacity increment as a foothold and work toward solutions over time.** Colin attends, helps convert this initial SOW into something more structured than undifferentiated T&M (for example, the hybrid model with BayOne staff embedded but working alongside a BayOne technical lead like Colin part-time), and treats this SOW as the relationship anchor while the senior procurement sponsor's introductions open additional doors. The win is multi-phase: the 3-4 person SOW lands now, then a second engagement six to nine months out is shaped around the real solutions work. The risk is that Colin's capacity constraint (documented in 01e) means he cannot sustain the ongoing involvement this shape requires.

**Shape C: Strategic partnership angle.** Colin attends, listens for the bigger picture (Arene shipping in production, Waymo partnership, Woven City AI stack, Toyota-scale data flow), and positions BayOne as a partner for the adjacent problems Travis is not yet solving. The 3-4 person SOW becomes incidental. The win is entry into Woven as a preferred AI partner with multiple workstreams. The risk is that this is aspirational and not something Travis has the authority or mandate to unlock on a discovery call.

These are not mutually exclusive in the long run, but on the call Colin has to pick a primary posture because the questions he asks, the framing he offers, and the decision he makes about whether to disengage all depend on which shape is the target.

## The Question

Of these three shapes, or something else you want to name, which one is BayOne actually playing for on this call? And specifically: if Travis frames this as pure capacity augmentation with no room to convert, is the answer walk (Shape A posture) or accept as a foothold (Shape B posture)?

---

## Colin's Response and Reset

Colin rejected the framing. The three shapes Claude offered conflated Colin's role with the sales team's role. Shape B (foothold for a bigger second engagement) and Shape C (strategic partnership across multiple workstreams) are decisions for Jesse Smith and Pratik Sharda. Those are sales concerns. Relationship plays, account expansion, and long-term commercial structuring are not in Colin's scope on this call.

Colin's scope is narrower and technical. He is the solutions voice in the room. His role is to assess whether there is something BayOne can build, propose, or architect for Woven in opposition to or in addition to staffing. If there is no such work, Colin disengages cleanly. If there is, Colin shapes the technical direction and helps scope what BayOne would deliver. The broader commercial question of whether a single capacity SOW becomes an anchor for later account expansion is Jesse and Pratik's to weigh, not Colin's.

This correction also surfaces a preference for how these discussions should be structured: lead with analysis, not questions. Claude should be bringing substantive technical perspective and only ending with a focused question when the question is something Colin specifically needs to weigh in on. Asking Colin to choose between abstract strategic shapes is interviewing, not brainstorming.

## Claude's Revised Analysis (Technical Solutions Scope Only)

Given Colin's scope is solutions, the real question is narrower: **given what the research shows about Woven's existing stack, what solutions could plausibly be on the table?** There are three candidate buckets tied to Colin's three-modes hypothesis from Set 01, and the research from Set 04 sharpens what each bucket would actually look like as BayOne work.

### Bucket 1: Labeling Surge (the likely default framing from Travis)

If Travis frames the problem as needing more labeling capacity, BayOne is walking straight into a space Woven is already strong in. AutoTriage runs at 80 percent accuracy with GenAI plus human-in-the-loop. Encord is the annotation platform. Union.ai orchestrates training pipelines. There is a dedicated Data Annotation and Labeling Engineering team. Adding three more labelers to that stack is T&M staffing, which Colin explicitly said is not his to pitch.

The solutions-shaped opportunities that would make this bucket worth Colin's time are layered around what is already there:

- **Active learning harness over Encord.** Woven has the platform but the decision logic about which samples to route to humans, how to calibrate uncertainty thresholds against model confidence, and how to feed corrections back into the next training cycle is non-trivial and often not where annotation platforms excel. A BayOne-built active learning control plane tied to Woven's specific model architectures is defensible work.

- **Edit-distance and label-quality telemetry.** Measuring how often model pre-labels are accepted as-is, minor-corrected, or fully redone tells you both the state of the model and the quality of the human reviewers. Instrumenting this across their pipeline as a monitoring and optimization layer is real engineering.

- **Multi-workforce quality assurance.** If Woven uses Encord plus an internal team plus possibly BSPs (business service providers) or contractors, measuring inter-rater reliability across groups, golden set performance, and adjudication routing is a systems problem. BayOne can build it.

- **Ontology migration tooling.** When a labeling taxonomy changes (new class, retired class, merged classes), the cost of re-labeling historical data is enormous. A tool that computes the minimal re-labeling footprint, auto-migrates where possible, and queues the residual for human review is substantial and bespoke.

- **Auto-labeling scaffolds for new modalities or new scenarios.** Foundation models (SAM 2, GroundingDINO, DINOv3, VLMs) applied to Woven's specific sensor fusion are a real engineering capability. Deploying, fine-tuning, and integrating them into Woven's pipeline is solution work.

### Bucket 2: Correlation Analysis (Colin's hypothesis from Set 01)

If Travis actually has a correlation problem (linking sensor conditions, weather, road geometry, or vehicle state to perception or planner failures), Woven's existing stack is less aligned. Their public material is about labeling and ML training infrastructure, not systematic correlation analysis. This is where BayOne could plausibly find bespoke work.

Candidate solutions:

- **ODD coverage mapping.** Measuring which operational design domain cells (weather, geometry, actor density, time of day) are well-represented in training and evaluation data and which have gaps. Statistical analysis tied to model performance per cell.

- **Disengagement correlation pipelines.** Systematic linking of disengagement events to sensor anomalies, planner decisions, and control outcomes. Often requires replay infrastructure and cross-stack traceability.

- **Failure-mode discovery.** Clustering failures by feature vectors to surface common upstream causes. Embedding-based scene retrieval tied to failure modes.

- **Regression analytics for model releases.** When Woven deploys a new model, which scenarios degraded? Which improved? Why? This is analysis infrastructure, not labeling.

### Bucket 3: Root Cause Analysis

If Travis has a root cause analysis problem (a specific disengagement or safety-critical event needs to be fully traced from symptom to source), this is the most bespoke engagement shape. Woven likely has internal tooling for this already given their aerospace-culture attention to safety, but the quality varies across AV developers.

Candidate solutions:

- **Replay and counterfactual simulation frameworks.** Re-run an event with modified conditions to isolate which factor caused the outcome.

- **Causal graph construction from telemetry.** Building directed acyclic graphs of cause and effect from event data.

- **Deep single-event investigation tools.** Structured workflows for investigators to trace an event through the full AV stack.

### The Observable Signal on the Call

Within the first few minutes of Travis framing, the signal about which bucket is in play is what Travis counts and what he says is broken. If he talks about frames per hour, annotations per week, label accuracy percentages, he is in Bucket 1. If he talks about event rates per condition cell, operational design domain gaps, or why certain scenarios underperform, he is in Bucket 2. If he talks about specific events that went wrong and why they went wrong, he is in Bucket 3. The mix is possible; the dominant framing usually is not.

### The Honest Risk

Bucket 1 is the likely default framing, and Bucket 1 is where Woven is strongest. If Travis is in Bucket 1, the solutions room is narrow and has to be carved out against a capable in-house team. BayOne would need to propose something specific enough that Travis cannot trivially dismiss it as something his team already does or could do. The items in the Bucket 1 list above are defensible but the bar is high.

Buckets 2 and 3 have more room but may not be Travis's mandate even if they are his problem. A triage operations manager may not own correlation analysis or root cause analysis infrastructure; that may sit with a different team or leader (possibly under Jack Yan in Cloud and AI, or under Dushyant Wadivkar in AD and ADAS).

## Focused Technical Question

The one thing worth your weigh-in: **of the Bucket 1 opportunities listed above (active learning harness, edit-distance telemetry, multi-workforce QA, ontology migration tooling, auto-labeling scaffolds), which ones do you consider credible BayOne work given what we can actually staff and build, and which should be off the table because they are too tool-vendor-shaped or too platform-team-shaped?** That calibration shapes what Colin listens for and what he is willing to propose on the call if Travis ends up in Bucket 1.

---

## Colin's Response to the Revised Question

Colin rejected the revised framing as well. The problem with Claude's Bucket 1 / 2 / 3 decomposition was not just the list of specific solutions but the fact that Claude was naming what Travis's underlying problem might be. Colin's position: BayOne should not guess at whether Travis has a quality problem, a discovery problem, an ontology problem, or any other specific problem. Travis will say what the problem is. BayOne listens.

The correct framing is narrower than the three modes or the three buckets. The binary Colin cares about is simpler: **is Travis interested in making the work faster through AI and automation, or does he want additional human capacity doing the work as it is done today?** The first is a Colin conversation (solutions). The second is not (staffing).

Colin also flagged a structural issue: the entire "AI acceleration" framing for this opportunity originated with Pratik at an in-person lunch with a procurement contact. It has not been confirmed with Travis directly. Pratik presented the framing to Travis via Naoki, but explicit confirmation that Travis shares the AI openness Pratik assumed is not documented anywhere in the research chain. Colin's Condition 4 from Set 02 required that confirmation before the call. Its status remains unverified.

Colin then asked a direct question that is worth answering honestly: if Woven already has AutoTriage, Union.ai, Encord, and a dedicated labeling engineering team, what is the SOW actually for?

## Claude's Answer on the SOW

The most defensible read is that Travis and the AutoTriage team are not the same team. AutoTriage is publicly associated with Suigen Koide (Head of DevBoost, GenAI and MLOps). That is the ML platform function. It builds the automated system that absorbs approximately 50 percent of ADAS triage volume. Travis runs Technical Operations Engineering. That is the operational triage workforce function. It runs the humans who handle everything AutoTriage does not. Staffing, SLAs, throughput, quality of the human-in-the-loop portion.

If that reading is correct, the SOW makes sense even against Woven's mature platform. AutoTriage takes half the load. The other half is humans doing real work. That volume just stepped up significantly because Arene shipped in the 2026 RAV4 in May 2025, which means Woven now has production fleet data flowing in alongside test fleet data. Travis's workforce needs to keep up with a materially larger firehose than it was sized for.

The uncomfortable corollary that follows from this reading is that if Travis's mandate is operational triage rather than ML platform work, AI acceleration is not naturally in his swim lane. The AI acceleration story is something Suigen's team owns, or possibly Jack Yan's Cloud and AI pillar. Pratik's AI framing came from a procurement lunch, not from Travis. The risk scenario, which Colin already named, is that Colin joins a call where Travis does not know why a Director of AI is on the line and proceeds to describe a purely staffing need, at which point Colin's presence has no value and he disengages clean.

## The Narrow Salvage Shape

If Travis does have latitude to drive internal improvements to his operational triage workforce, there is a small set of operational solutions that sit legitimately in his role and would benefit from Colin's involvement rather than undifferentiated staffing. These are not new problems BayOne introduces; they are things Travis may surface organically if he is at all frustrated with how his team currently operates. Examples of what this could look like if Travis describes it: faster onboarding tooling for new triagers, better QA tooling for his workforce, better feedback loops when AutoTriage produces wrong outputs that his workforce has to correct, or improved throughput instrumentation for SLA management. None of these are for Colin to propose first. They are shapes to listen for if Travis volunteers operational pain.

## Current Working Conclusion for the Call

- Listen to how Travis frames the problem in his own words.
- Probe whether what he describes is an acceleration-through-AI-and-automation opportunity or a capacity augmentation opportunity. This is the binary that matters.
- Do not introduce problem shapes on BayOne's behalf. Do not guess at quality, discovery, correlation, root cause, or anything else.
- If Travis signals acceleration interest, Colin has a conversation worth having and can probe into the operational realities of his workforce to see where solutions fit.
- If Travis signals staffing only, Colin disengages cleanly. The hour will not have been pleasant to give up but the decision is clean.

## Outstanding Conversational Threads Before the Call

- Confirmation of Condition 4 (Travis's AI openness, confirmed via Naoki) is still not in evidence.
- Whether Colin wants to prepare explicit language for the clean disengagement scenario inside the prep document.
- Whether Colin wants to frame the prep document around the binary listen-for (acceleration vs capacity) as the primary structural element.
