# 04 - Research: Labeling vs Correlation vs Root Cause Analysis in AV Contexts

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** Technical framing of the three candidate problem modes and how to distinguish them

---

## Purpose

This document supports the 3:30 PM PST discovery call with Travis Millet at Woven by Toyota. The working hypothesis is that when an AV group says "data triaging and labeling," the actual request resolves into one of three structurally different engineering programs:

1. **Classical labeling** (production of supervised training signal)
2. **Correlation analysis** (relating conditions, inputs, or artifacts to outcomes across a fleet)
3. **Root cause analysis** (tracing a specific failure or disengagement back through the stack)

Each has a different technical shape, a different team composition, a different tool chain, and a different pricing and staffing profile. The goal of this research is to give Colin enough vocabulary and diagnostic prompts to localize which of the three Travis is actually describing within the first few minutes of the call.

---

## 1. Classical Labeling in AV Contexts

### 1.1 What the work actually is

Classical labeling in an AV context is the production of supervised ground truth that perception, prediction, and (increasingly) planning models are trained and evaluated against. The object of work is a single log segment, frame, or sweep, and the output is a structured annotation attached to that segment.

Typical annotation classes include:

- **2D bounding boxes** on camera frames for vehicles, pedestrians, cyclists, signs, and signals.
- **3D cuboids** on LiDAR point clouds encoding position, extent, heading, and class.
- **Semantic segmentation** at the pixel level for drivable surface, lane markings, curb, vegetation.
- **Instance and panoptic segmentation** where each instance of a class is individuated.
- **Polyline and polygon annotation** for lanes, crosswalks, stop lines, and free-space boundaries.
- **Object tracking / track association** linking the same object across frames and across sensors.
- **Scenario or event tagging** (e.g. "unprotected left", "construction zone", "jaywalker") applied at a clip or segment level.
- **Attribute labeling** such as pedestrian orientation, vehicle turn signal state, or occlusion level.

See CVAT's and Label Your Data's annotation taxonomies for representative lists of these primitives ([CVAT AV annotation](https://www.cvat.ai/resources/blog/data-annotation-for-autonomous-vehicles), [Label Your Data 2026](https://labelyourdata.com/industries/data-labeling-for-autonomous-vehicles)).

### 1.2 Tools and workflow

The dominant pattern in 2026 is **model-assisted labeling (MAL)** inside a closed workflow:

1. An **offline / auto-labeling** perception stack runs over raw logs in the cloud. This stack is larger, slower, and more accurate than the onboard stack; it is not bound by real-time constraints and can use bidirectional temporal context. NVIDIA and Motional both document this pattern explicitly ([NVIDIA auto-labeling pipeline](https://developer.nvidia.com/blog/developing-an-end-to-end-auto-labeling-pipeline-for-autonomous-vehicle-perception/), [Motional auto-labeling](https://motional.com/news/technically-speaking-auto-labeling-offline-perception)).
2. Auto-labels are pushed to a labeling platform (CVAT, Scale, Encord, or internal tooling) where human annotators **correct** rather than **create** annotations.
3. A quality assurance layer applies honeypots, ground-truth spot checks, consensus scoring, and reviewer workflows ([Label Your Data bounding box 2026](https://labelyourdata.com/articles/data-annotation/bounding-box-annotation)).
4. Labels are versioned, attached to an ontology, and emitted to a training data store.

NVIDIA reports 65% reduction in manual effort from properly implemented auto-labeling ([NVIDIA](https://developer.nvidia.com/blog/developing-an-end-to-end-auto-labeling-pipeline-for-autonomous-vehicle-perception/)).

### 1.3 Team structure

Labeling programs at AV-grade companies typically involve:

- A **perception engineering** group owning the ontology and the auto-label stack.
- A **data labeling operations** team (often offshore or vendor-managed) doing correction and QA at scale.
- An **ontology** team or function arbitrating class definitions, edge-case rules, and schema evolution.
- A **tooling / platform** team running the annotation platform, data store, and pipelines.

Nuro, Zoox, and Motional job descriptions describe this split explicitly; perception engineers are positioned as the bridge between the stack, the labeling operation, and the ML model trainers ([Nuro Perception Data Infrastructure JD](https://www.builtinsf.com/job/sr-software-engineer-perception-data-infrastructure/8968727), [Zoox Perception Attributes JD](https://jobs.lever.co/zoox/f44d1c41-2d41-457b-94af-85692176347f)).

### 1.4 Where AI assists and where human judgment is irreducible

AI assists strongly in:

- First-pass geometry (box, cuboid, mask placement).
- Propagation across frames (tracking, temporal smoothing).
- Easy-class classification (clearly visible cars in open lanes).
- Pre-filtering obvious negatives.

Human judgment remains irreducible for:

- **Ontology edge cases:** is a scooter a pedestrian or a vehicle? Is a person pushing a shopping cart a pedestrian plus an object, or a single instance?
- **Heavy occlusion and partial visibility:** how much of a cuboid do you extrapolate through a truck.
- **Intent and scenario tags:** "driver is about to cut in" is not reliably inferable from geometry.
- **Arbitration between conflicting auto-labels** across offline passes.
- **Long-tail events** that the auto-labeler was not trained on.

### 1.5 Engagement shape

If Travis's need is classical labeling, the BayOne engagement looks like:

- A **managed services** or **labeling operations** engagement.
- Headcount-heavy, low-per-head cost, scales with data volume.
- Deliverable is labeled data in a contractually defined ontology at a contractually defined quality bar.
- Value proposition is throughput, SLA, and cost-per-label, not insight.

This is the engagement Ariat-style managed services teams sell. It is the shape BayOne is most likely to try to force-fit onto the conversation if we do not explicitly guard against it.

---

## 2. Correlation Analysis in AV Data

### 2.1 What the work actually is

Correlation analysis operates on a fleet or log aggregate, not a single frame. The unit of work is a **population of events** (disengagements, hard-brakes, near-misses, perception misdetections, planner stalls) cross-referenced against **conditions** (weather, road class, time of day, sensor configuration, map region, software version, ODD).

The output is a quantified relationship: "Planner disengagements occur 3.4x more often on wet pavement at night between 10pm and 2am in the Palo Alto ODD on software version X." It is statistical inference over fleet data, not per-event annotation.

### 2.2 Representative questions this mode answers

From academic and industry literature, the recurring questions are:

- Which road geometries and cross-sections correlate with disengagements? ([IJMO disengagement analysis](https://www.ijmo.org/vol15/IJMO-V15N1-865.pdf))
- Which weather or visibility conditions degrade specific sensor modalities, and by how much? ([ScienceDirect adverse-weather perception survey](https://www.sciencedirect.com/science/article/pii/S0924271622003367))
- Which infrastructure features (horizontal / vertical alignment, pavement condition, markings) co-occur with system takeovers?
- Which ODD cells are overrepresented in crash and disengagement data? ([Nature Scientific Data California AV crash/disengagement](https://www.nature.com/articles/s41597-021-01083-7))
- Which software versions or model revisions changed the distribution of downstream failures?

### 2.3 Techniques

- **Descriptive statistics and contingency tables** over tagged event populations.
- **Classification trees and generalized linear models** on structured features to identify predictors of disengagement ([ScienceDirect causes and effects via classification tree](https://www.sciencedirect.com/science/article/abs/pii/S0001457519300016)).
- **Mixed-effects models** when hierarchy matters (vehicle, region, software version).
- **Scenario mining** over embedded log data: natural language or structured queries produce populations for comparison ([Applied Intuition Data Explorer](https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets), [Motional Omnitag](https://motional.com/news/technical-speaking-omnitag-ml-powered-multimodal-data-mining-framework)).
- **Online/offline perception disagreement** as a signal: when the offline stack disagrees with the online stack, that is a correlation feature in its own right and is routinely mined ([Motional scenario mining](https://motional.com/news/technically-speaking-mining-scenarios-help-better-train-our-avs)).
- **Uncertainty-based and embedding-similarity selection** to pull comparable populations for like-for-like comparison ([NVIDIA active learning A/B test](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f)).

### 2.4 How this differs structurally from labeling

- Labeling produces **one annotation per segment**. Correlation produces **one statistic per condition cell**.
- Labeling is primarily human-in-the-loop. Correlation is primarily pipeline plus analyst.
- Labeling scales with annotator headcount. Correlation scales with data engineering and statistical depth, and is strongly limited by the **completeness and cleanliness of prior labels and tags**. A correlation engagement silently depends on the labeling engagement having already happened well.
- Labeling's deliverable is a dataset. Correlation's deliverable is a **finding, chart, or dashboard**.

### 2.5 Engagement shape

A correlation engagement is smaller-headcount, higher-per-head, and much more senior. It is a data science and ML engineering engagement. The deliverable is insights, not volume. Time-to-value is weeks, not months. BayOne can do this credibly but the staffing is fundamentally different from a labeling operation.

---

## 3. Root Cause Analysis in AV Data

### 3.1 What the work actually is

Root cause analysis (RCA) operates on a **single event** and answers the question: "Why did this specific disengagement / near-miss / crash / takeover happen, and which component in which layer of the stack originated the fault?"

The unit of work is a log of one drive around one event, and the output is a causal chain traced through sensor, perception, prediction, planning, and control.

### 3.2 Standard workflow

The Applied Intuition articles describe the now-canonical workflow ([open-loop vs closed-loop replay](https://www.appliedintuition.com/blog/closed-loop-log-replay), [Log Sim](https://www.appliedintuition.com/blog/logstream), [four triage essentials](https://www.appliedintuition.com/blog/av-development-4-triage-considerations)):

1. **Triage and surfacing:** the event is flagged by fleet telemetry (disengagement marker, safety-driver intervention, onboard monitor).
2. **Open-loop log replay:** the original sensor data is fed back through the current autonomy stack. This tells the engineer what the perception and localization stacks produced, frame by frame. It is sufficient to diagnose perception and localization defects.
3. **Closed-loop log re-simulation:** the scenario is recreated in a simulator and the planner and control stack are allowed to run against it. This answers whether the disengagement was *necessary*, i.e. whether the ego would have actually collided or violated a constraint if the safety driver had not intervened. It localizes planning and control defects.
4. **Counterfactual / perturbation analysis:** the scenario is varied (remove an agent, change the weather, change the software version) and the stack is re-run to isolate which input changes the outcome. This is how one attributes root cause.
5. **Fault localization** at module, message, and code level per the ADS debugging mapping study ([arXiv systematic mapping](https://arxiv.org/html/2601.04293v1)).
6. **Scenario simplification** where irrelevant traffic participants or frames are stripped to produce a minimal failing case ([arXiv](https://arxiv.org/html/2601.04293v1)).

### 3.3 Additional techniques

- **Fault tree analysis (FTA)**, sometimes combined with SOTIF (safety of the intended functionality), to enumerate how a top-level failure could be produced from component faults ([Sage fault tree AV](https://journals.sagepub.com/doi/abs/10.1177/15553434221116254), [ACM FTA + SOTIF survey](https://dl.acm.org/doi/10.1145/3787221)).
- **Causal analysis tools** that derive which specification clause was violated and which upstream events contributed ([arXiv debugging study](https://arxiv.org/html/2601.04293v1)).
- **Counterfactual re-execution** where engineers identify the first module output that deviates from a reference run ([arXiv debugging study](https://arxiv.org/html/2601.04293v1)).
- **Six-way taxonomy of disengagements** used as a standard framing: control discrepancy, environmental / other road users, hardware / software discrepancy, perception discrepancy, planning discrepancy, operator takeover ([IJMO](https://www.ijmo.org/vol15/IJMO-V15N1-865.pdf)).

### 3.4 How this differs structurally from labeling and correlation

- RCA is **narrow and deep**. Labeling is wide and shallow; correlation is wide and statistical. RCA is single-event and layered.
- RCA depends on **log fidelity, replay infrastructure, and simulator integration**. Labeling has no such dependency. Correlation has a partial dependency (mining, not replay).
- RCA requires **stack-level knowledge** (perception, prediction, planner, control, vehicle dynamics). It is not plausibly performed by an annotation workforce.
- RCA's output is a **defect disposition**, not a dataset or a statistic.

### 3.5 Engagement shape

RCA is the most senior and most specialized engagement of the three. It requires engineers who can read and reason about the client's autonomy stack, or at minimum work next to client engineers who can. It is typically sold as augmentation of a client's own safety or debug function. BayOne can staff this, but only with carefully selected senior people, and the margin profile is very different from a labeling operation.

---

## 4. Comparative View

| Dimension | Classical Labeling | Correlation Analysis | Root Cause Analysis |
|---|---|---|---|
| Unit of work | One frame / segment | Population of events | One event |
| Primary output | Annotated dataset | Statistical finding | Causal chain / defect disposition |
| Dominant skill | Annotation ops + ontology | Data science / ML engineering | Autonomy stack engineering |
| Human headcount scaling | Linear in data volume | Sublinear | Constant, senior |
| Dependency on prior work | Needs ontology | Needs labels and tags | Needs logs, replay, simulator |
| Tooling | CVAT / Scale / Encord, offline perception | Data warehouse, scenario mining, notebooks | Log replay, simulator, counterfactual harness |
| Time to first value | Weeks for throughput ramp | 1-2 weeks for first chart | Days per event |
| Failure mode if misbuilt | Slow, inconsistent labels | Wrong conclusions, noisy baseline | Wrong blame assigned to wrong layer |
| BayOne engagement model | Managed services | Project-based data science | Senior augmentation |

### 4.1 Where the three overlap

- All three sit on top of the same fleet log store.
- All three benefit from a shared **ontology and attribute schema** ([Motional Omnitag](https://motional.com/news/technical-speaking-omnitag-ml-powered-multimodal-data-mining-framework)).
- All three benefit from **auto-labeling**: labeling consumes auto-labels directly, correlation consumes them as features, RCA consumes them as a reference when comparing replay outputs to ground truth.
- **Scenario mining** is the connective tissue. It is how one pulls populations for correlation, how one finds candidate RCA events, and how one selects data to send to labelers ([Applied Intuition](https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets)).

### 4.2 Where they are genuinely different engagements

- **Team composition** is not interchangeable. Annotation workforce does not do RCA. Senior perception engineers are not a labeling operation. A data-science-oriented team will not produce labeling throughput.
- **Contract structure** diverges. Labeling is SLA-and-throughput. Correlation is deliverable-and-milestone. RCA is time-and-materials senior augmentation.
- **Tooling investment** is different. A labeling engagement needs annotation platform and QA. A correlation engagement needs a data warehouse, scenario mining, and an analyst seat. An RCA engagement needs log replay and simulation infrastructure, which the client almost always owns and does not let an outside vendor touch lightly.

### 4.3 What breaks if BayOne sells one and the real need is another

- **Sell labeling, need correlation:** BayOne delivers volume, client gets no answers. Client churns in three months citing "they do not understand our stack." Downstream referenceability is damaged.
- **Sell labeling, need RCA:** same, worse. Safety-critical questions go unanswered; the client concludes BayOne is an annotation shop and will never re-engage for technical work.
- **Sell correlation, need labeling:** BayOne staffs senior data scientists who cannot move the primary bottleneck (annotation throughput). Burn is high, output is low, the engagement stalls.
- **Sell correlation, need RCA:** BayOne produces fleet-wide charts when the client needed a per-event postmortem. The client perceives BayOne as missing the point.
- **Sell RCA, need labeling:** senior engineers sit idle or get pulled into ontology arguments they cannot win without scale.
- **Sell RCA, need correlation:** senior engineers produce over-deep postmortems when the client wanted a trend.

The highest-risk misalignment is **selling labeling when the actual need is RCA or correlation**, because BayOne's default positioning and default staffing archetype is the labeling shape.

---

## 5. Diagnostic: Telling Them Apart from Travis's Verbal Framing

The goal in the first five to ten minutes of the call is to localize which of the three modes Travis is describing. Listen for **what Travis names as the output**, **what he names as the input**, and **who on his side owns it today**.

### 5.1 Verbal tells

**Classical labeling tells:**
- "We have a queue of data we need annotated."
- "Our vendor is not keeping up."
- "Our ontology has evolved and we need to relabel."
- "We need 3D cuboids / semantic seg / scenario tags."
- Mentions of Scale, CVAT, Labelbox, Encord, Appen, iMerit.
- Output described as **datasets** or **labels**.
- Volume metrics: hours, miles, frames, clips per week.

**Correlation tells:**
- "We have a lot of data and we need to understand what is happening."
- "We are seeing X behavior in these conditions and not those."
- "We do not know why the disengagement rate went up last quarter."
- "We want to compare software version A to version B."
- Output described as **dashboards, reports, findings**.
- Volume metrics: events, cells, ODDs.
- Mentions of fleet telemetry, Looker / Tableau / internal BI.

**RCA tells:**
- "We had an event last week and we cannot explain it."
- "We need to understand why the planner did X in this specific situation."
- "Our safety team is backlogged on disengagement reviews."
- "We need someone who can sit with our stack and trace through it."
- Output described as **postmortems, tickets, defect dispositions**.
- Volume metrics: events per week, events per engineer per week.
- Mentions of log replay, simulation, Applied Intuition, Foretellix, internal re-sim tools.

### 5.2 Follow-up questions that force the mode to reveal itself

If Travis opens with something ambiguous like "we have a lot of data and we need to make sense of it," the following questions collapse the ambiguity fast:

1. **"What is the deliverable?"** Labels? A chart? A postmortem? The answer maps directly to one of the three modes.
2. **"Who consumes the output today, and what do they do with it?"** ML training pipeline implies labeling. A program manager or safety lead implies correlation or RCA. A specific autonomy engineer implies RCA.
3. **"Is the bottleneck at the per-event level, the per-population level, or the per-frame level?"** Per-frame is labeling. Per-population is correlation. Per-event is RCA.
4. **"How is the data surfaced to you today? Do you query it, do you get it handed to you, or do you start from a single incident?"** Query means correlation. Incident means RCA. Queue means labeling.
5. **"What tooling is already in place?"** CVAT / Scale / Labelbox means labeling. Applied Intuition / Foretellix / internal sim means RCA. Data warehouse and BI means correlation.
6. **"What does success look like in six months?"** A bigger labeled dataset, a report and decision made, or a backlog of events cleared? Each answer maps to a mode.
7. **"Who on your side owns this problem?"** Annotation ops lead means labeling. Data science / ML lead means correlation. Safety / autonomy / debug engineer means RCA.
8. **"What is the unit you count?"** Frames / hours means labeling. ODD cells / conditions means correlation. Events / tickets means RCA.

### 5.3 Mode-indifferent questions to avoid

"What data do you have?" and "how much data is there?" do not discriminate between the three modes. Every AV team has petabytes of sensor data. The volume is not the tell. The **unit of work** and the **unit of deliverable** are the tells.

---

## 6. Public Evidence on How AV Teams Structure This Work

### 6.1 Team-level patterns

- **Perception engineers** sit between the stack, the labeling operation, and the ML training team. They own the ontology and the auto-label stack ([Nuro JD](https://www.builtinsf.com/job/sr-software-engineer-perception-data-infrastructure/8968727), [Zoox JD](https://jobs.lever.co/zoox/f44d1c41-2d41-457b-94af-85692176347f)).
- **Offline / auto-label teams** are a distinct function from the onboard perception team ([NVIDIA](https://developer.nvidia.com/blog/developing-an-end-to-end-auto-labeling-pipeline-for-autonomous-vehicle-perception/), [Motional auto-labeling](https://motional.com/news/technically-speaking-auto-labeling-offline-perception)).
- **Scenario mining / data mining** is an increasingly separate function with its own tooling; Motional's Omnitag is a dedicated platform staffed by ML engineers ([Motional Omnitag](https://motional.com/news/technical-speaking-omnitag-ml-powered-multimodal-data-mining-framework)).
- **Safety / debug / RCA** is often inside the safety organization or a dedicated debugging group, not inside the perception group.
- **Platform and infrastructure** teams (data warehouse, pipeline orchestration) are a distinct function. Woven by Toyota publicly describes using Union.ai at the scale of petabytes and hundreds of thousands of node-hours for this layer ([Union.ai case study](https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai)).

### 6.2 Tooling patterns

- **Labeling platforms:** CVAT, Scale, Labelbox, Encord, internal tools. Model-assisted labeling is standard.
- **Scenario mining:** natural-language retrieval over embedded logs. Applied Intuition Data Explorer uses a two-tower retrieval architecture over foundation models ([Applied Intuition](https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets)). Motional uses multimodal foundation models adapted via few-shot RAG loops ([Motional Omnitag](https://motional.com/news/technical-speaking-omnitag-ml-powered-multimodal-data-mining-framework)).
- **Log replay and re-simulation:** Applied Intuition Log Sim, Foretellix, and internal tooling. Open-loop replay for perception / localization faults, closed-loop re-sim for planner / control faults ([Applied Intuition closed-loop](https://www.appliedintuition.com/blog/closed-loop-log-replay), [Foretellix](https://www.foretellix.com/)).
- **Active learning / data selection:** Tesla's Data Engine is the best-known public pattern; Waymo runs data-mining and active-learning pipelines over fleet data to surface uncertainty and inconsistency cases ([Think Autonomous Tesla vs Waymo](https://www.thinkautonomous.ai/blog/tesla-vs-waymo-two-opposite-visions/), [NVIDIA active learning](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f)).
- **Woven by Toyota specifically:** publicly documents an ML-first approach, camera-only collection devices at 90% lower cost, an ML Planner deployed in San Francisco and Palo Alto, and model introspection tooling used across all models trained daily ([Woven camera data](https://woven.toyota/en/our-latest/20220407/), [Woven ML Planner](https://woven.toyota/en/our-latest/20211105/), [Woven model improvement](https://woven.toyota/en/our-latest/20220127/)).

### 6.3 What this implies for the Woven call

Woven by Toyota is publicly visible as a sophisticated ML-first shop with in-house data infrastructure, an ML Planner in production, auto-labeling capability, and a functioning model improvement loop. They are not a client that needs basic labeling capacity introduced to them. If Travis is reaching outside for "data triaging and labeling," it is worth treating as evidence that the real need is **correlation** or **RCA-adjacent scenario mining**, or a **surge on a specific labeling ontology change**, rather than net-new labeling operations.

This is a hypothesis, not a conclusion. The call's job is to test it.

---

## 7. Open Questions for the Call

1. What is the specific event or dataset Travis is looking at that made this a question this quarter? An existing vendor falling behind, a new model launch, a safety program review, or a product decision?
2. What does Travis mean by "triaging"? Is the word pointing at disengagement triage (RCA), at data selection for training (mining), or at labeling queue prioritization?
3. Who at Woven owns the ontology? If the engagement touches labels, who arbitrates schema?
4. What does Woven's existing labeling operation look like, and is this engagement additive, displacing, or surge?
5. What simulation and replay infrastructure does Woven already have in place? Are they on Applied Intuition, Foretellix, or internal tooling? This determines whether RCA is even a BayOne-executable engagement or purely a client-side activity.
6. What is the expected output? Labeled data, a report, a dashboard, a backlog of events closed, or a capability handoff?
7. What is the target team size and seniority mix? This is the clearest single signal of which of the three modes Travis has in mind, even if he does not yet call it that.
8. What are the constraints on where the work happens? US-only, Japan, India GCC, hybrid? Labeling tolerates offshore cheaply; RCA does not.

---

## Sources

- [CVAT - Data Annotation for Autonomous Vehicles](https://www.cvat.ai/resources/blog/data-annotation-for-autonomous-vehicles)
- [Label Your Data - AV Data Labeling 2026](https://labelyourdata.com/industries/data-labeling-for-autonomous-vehicles)
- [Label Your Data - Bounding Box Annotation 2026](https://labelyourdata.com/articles/data-annotation/bounding-box-annotation)
- [NVIDIA - End-to-End Auto Labeling Pipeline for AV Perception](https://developer.nvidia.com/blog/developing-an-end-to-end-auto-labeling-pipeline-for-autonomous-vehicle-perception/)
- [Motional - Auto-labeling With Offline Perception](https://motional.com/news/technically-speaking-auto-labeling-offline-perception)
- [Motional - Mining Scenarios to Train AVs](https://motional.com/news/technically-speaking-mining-scenarios-help-better-train-our-avs)
- [Motional - Omnitag Multimodal Data Mining Framework](https://motional.com/news/technical-speaking-omnitag-ml-powered-multimodal-data-mining-framework)
- [Applied Intuition - AI for Mining Massive Autonomy Datasets](https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets)
- [Applied Intuition - Closed-Loop Log Replay](https://www.appliedintuition.com/blog/closed-loop-log-replay)
- [Applied Intuition - Log Sim Re-simulation](https://www.appliedintuition.com/blog/logstream)
- [Applied Intuition - 4 Triage Essentials for AV Development](https://www.appliedintuition.com/blog/av-development-4-triage-considerations)
- [Applied Intuition - Log Visualization and Triage](https://www.appliedintuition.com/use-cases/log-visualization-and-triage)
- [Foretellix - Physical AI Toolchain](https://www.foretellix.com/)
- [IJMO - Analysis of Disengagements in Autonomous Vehicles](https://www.ijmo.org/vol15/IJMO-V15N1-865.pdf)
- [ScienceDirect - Causes and Effects of AV Disengagement (Classification Tree)](https://www.sciencedirect.com/science/article/abs/pii/S0001457519300016)
- [ScienceDirect - Perception Under Adverse Weather Survey](https://www.sciencedirect.com/science/article/pii/S0924271622003367)
- [Nature Scientific Data - California AV Crash and Disengagement Data](https://www.nature.com/articles/s41597-021-01083-7)
- [Sage - Where Failures May Occur in Automated Driving (FTA)](https://journals.sagepub.com/doi/abs/10.1177/15553434221116254)
- [ACM - FTA and SOTIF Integration Survey](https://dl.acm.org/doi/10.1145/3787221)
- [arXiv - Systematic Mapping Study on Debugging of ADS](https://arxiv.org/html/2601.04293v1)
- [NVIDIA AI - Scalable Active Learning for Autonomous Driving](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f)
- [Think Autonomous - Tesla vs Waymo](https://www.thinkautonomous.ai/blog/tesla-vs-waymo-two-opposite-visions/)
- [Woven by Toyota - Powering Data-Driven Autonomy at Scale with Camera Data](https://woven.toyota/en/our-latest/20220407/)
- [Woven by Toyota - Deploying an ML Planner in San Francisco](https://woven.toyota/en/our-latest/20211105/)
- [Woven by Toyota - Improving ML Models for AVs](https://woven.toyota/en/our-latest/20220127/)
- [Union.ai - Woven by Toyota Case Study](https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai)
- [Nuro - Sr. Software Engineer, Perception Data Infrastructure JD](https://www.builtinsf.com/job/sr-software-engineer-perception-data-infrastructure/8968727)
- [Zoox - Machine Learning Engineer, Perception Attributes JD](https://jobs.lever.co/zoox/f44d1c41-2d41-457b-94af-85692176347f)
- [Encord - ADAS Data Annotation Pipelines](https://encord.com/blog/adas-data-annotation-pipelines/)
