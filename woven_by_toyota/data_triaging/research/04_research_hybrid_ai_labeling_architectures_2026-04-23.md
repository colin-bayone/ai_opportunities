# 04 - Research: Hybrid AI Labeling Architectures in 2026

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** Current state of human-plus-AI labeling and triage architectures

---

## Purpose

This document synthesizes the publicly disclosed state of hybrid human-plus-AI labeling and data triage architectures as of April 2026, oriented to the question of what BayOne could credibly build for Woven by Toyota. It is written for a technical reader. Citations point to primary source URLs; where a specific claim depends on a vendor blog or interview, the source is named inline.

Woven by Toyota's own public writing on labeling infrastructure (the 2021 Arene DGP post) focuses on format governance and vendor orchestration rather than on algorithmic automation. Their engineering job posts from 2025-2026 describe a Data Annotation and Labeling Engineering team building "both human-assisted and automated data labeling services" and an Enterprise AI platform using Union.ai for orchestration across petabytes of sensor data. This is a team already thinking in pipeline terms, so a pitch that reduces to "we can add an AI step" will not land. The pitch that can land is "here is the specific loop architecture, here are the failure modes, and here is the team shape that will install it without breaking your governance model."

---

## 1. Active Learning Loops in Production AV Labeling

### 1.1 The canonical loop

The production pattern that has been publicly documented (NVIDIA, Waymo, Wayve, and by proxy Tesla through AI Day) is pool-based active learning with an acquisition function that scores unlabeled frames on model uncertainty, model disagreement, or planning relevance. The loop has five stages:

1. **Candidate pool construction.** Fleet or drive logs are ingested to an unlabeled frame or clip pool. At fleet scale this is billions of frames, so the pool itself is partitioned and sharded before any scoring happens.
2. **Scoring.** One or more trained models run inference over the pool and produce per-frame scores reflecting informativeness.
3. **Query selection.** A query budget (for example, the 19k frames per iteration in NVIDIA's published A/B test) is drawn from the top of the distribution, usually with a diversity constraint so the selected batch is not redundant.
4. **Human labeling.** Selected frames are routed to annotators, optionally with pre-filled labels (see Section 2).
5. **Model retraining.** New labels are merged into the training set, the model is retrained, and the loop repeats.

### 1.2 Acquisition functions that actually get used

Four families are reported in production or near-production settings:

- **Least-confidence / margin / entropy sampling.** The simplest uncertainty heuristics. Least confidence flags frames where the top class probability is below a threshold. Margin sampling scores on the gap between top-1 and top-2 classes. Entropy sums over all class probabilities. Digital Divide Data and CloudFactory both document these as the baseline, and they remain the default starting point because they are cheap and require only one model.
- **Bayesian ensemble disagreement (NVIDIA).** NVIDIA's published implementation trains an ensemble of eight detectors from different random initializations and computes mutual information between ensemble member predictions. The acquisition score is disagreement: frames where the ensemble members disagree are the most informative. In their A/B test on 2M nighttime frames with a query budget of 19k, this produced a 3x precision improvement on pedestrian detection and 4.4x on bicycle detection relative to manual curation. Each training run used 8 GPUs for about two days, so the infrastructure cost is nontrivial. Source: [Scalable Active Learning for Autonomous Driving](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f).
- **Inconsistency-based sampling for LiDAR.** A 2025 arXiv paper proposes scoring LiDAR frames based on spatial-temporal inconsistency between successive frames rather than single-frame uncertainty, which is more robust for 3D detection because well-calibrated 3D classification uncertainty is notoriously hard to estimate. Source: [Inconsistency-based Active Learning for LiDAR](https://arxiv.org/html/2505.00511).
- **Planning-oriented (ActiveAD, CVPR 2026).** Rather than scoring on detection uncertainty, ActiveAD scores on how much a frame would change the planned trajectory of an end-to-end driving model. This is the direction end-to-end teams (Wayve, Tesla) are heading because detection uncertainty does not always correlate with driving risk. Source: [ActiveAD OpenReview](https://openreview.net/forum?id=7Zppme1swQ) and [Thinklab-SJTU/ActiveAD](https://github.com/Thinklab-SJTU/ActiveAD).

### 1.3 Query budget and feedback cadence

NVIDIA's disclosed cadence was 19k frames per iteration against a 2M pool and an 850k labeled training set. Wayve has publicly noted that in 1.45M km of driving logs, only about 0.1% of miles contained long-tail events that justified labeling. This ratio (0.1% to 1% of raw data worth labeling) is consistent across reports and is the economic argument for active learning: without it, you either label uninformative frames or throw them away. Iteration cadence in published systems ranges from weekly to monthly depending on compute.

### 1.4 How human labels feed back

Labels do not go straight to the training set. The pattern across all mature pipelines is:

- Annotators produce labels on queried frames.
- Labels pass through a quality layer (golden-set calibration, consensus among multiple annotators, adjudication for disagreement; Section 5).
- Clean labels are versioned into a dataset snapshot.
- The next training run uses the snapshot, not live labels, so training is reproducible.
- Model performance on a held-out benchmark is tracked per iteration, which is what lets teams decide when active learning has saturated and the loop can be paused for that particular failure mode.

---

## 2. Model-Assisted Labeling and Pre-Labeling

### 2.1 The state of the art in 2026

Pre-labeling has moved from "run a production detector and have humans fix it" to "run a foundation model prompted with text or points and have humans validate." The foundation models in active production or near-production use for AV pre-labeling are:

- **SAM 2 / SAM 2.1 (Meta).** The segmentation workhorse. SAM 2 handles images and video in one model, tracks objects through occlusion, and is reported to be ~8.4x faster than per-frame manual segmentation in CVAT's integration. Encord, V7, and CVAT all ship SAM 2 integrations as a default. Source: [CVAT SAM 2 integration](https://www.cvat.ai/resources/changelog/video-annotation-sam-2); [Encord on SAM 2.1](https://encord.com/blog/sam-2.1-explained/). Ultralytics quotes SAM 2 as "8.4x faster than manual per-frame annotation."
- **SAM 3 (Meta, late 2025).** "Segment Anything with Concepts." Text-promptable segmentation without needing a click, which closes the gap with GroundingDINO for pre-labeling rare categories. Source: [Roboflow on SAM 3](https://blog.roboflow.com/what-is-sam3/).
- **GroundingDINO 1.5 / GroundingDINO-B.** Open-vocabulary detection prompted with free-text category names. Used in corner case discovery pipelines for AV to annotate classes that were not in the original taxonomy. Source: [Grounding DINO 1.5 arXiv](https://arxiv.org/html/2405.10300v1); [OpenAD benchmark](https://arxiv.org/html/2411.17761v1).
- **OWLv2 (OWL-ViT v2).** Used as the open-vocabulary detection baseline in the OpenAD autonomous driving benchmark alongside GroundingDINO-B. Differences are primarily in text-encoder architecture and training data; both work for AV pre-labeling of unusual objects.
- **DINOv2 / DINOv3.** Self-supervised ViT backbones that produce strong dense features without any labels. Used less for pre-labeling directly and more as a feature extractor for similarity search and clustering (Section 6). Source: [Encord DINOv3 explainer](https://encord.com/blog/dinov3-explained-scaling-self-supervised-vision-tr/).
- **Multimodal large language models (MLLMs) for attribute labeling.** LLaVA-class models are used to generate scene descriptions, attribute labels (weather, lighting, road type), and caption-level metadata that feeds retrieval and scenario mining. Not accurate enough for geometric labels, good enough for categorical metadata.

### 2.2 Speedup factors that are defensible to quote

The reliable numbers from vendor case studies and benchmarks:

- SAM 2 segmentation vs manual per-frame: ~8.4x (Ultralytics / CVAT).
- AI-assisted labeling platforms vs manual: 4-5x throughput improvement is the most commonly reported figure (Encord, Labellerr case studies).
- Hybrid workflow case study (Pickle Robot, via Encord): 30% accuracy improvement and 60% faster iteration.
- Setup/configuration time reduction with templated workflows: 70-80% (vendor-reported, less verifiable).

The honest caveat: all of these numbers come from vendors selling the tools. The actual speedup for a new client depends heavily on the class taxonomy, the base rate of errors the foundation model makes on the client's domain, and how much time is spent on review versus creation. A useful frame for Travis: "vendor numbers are ceiling, your observed speedup will be 40-70% of ceiling in year one, and we size the engagement around what we measure on your data."

### 2.3 Pre-labeling architecture pattern

Foundation-model pre-labeling in 2026 looks like:

1. Orchestrator pulls a batch of frames from the queue.
2. For each frame, a router decides which foundation models to run (SAM 2 for instance masks, GroundingDINO for novel categories, a domain detector for known classes).
3. Pre-labels are written to the labeling tool as draft annotations.
4. Human annotator sees the frame with draft labels and either accepts, adjusts, rejects, or adds.
5. Time on task, edit distance from pre-label to final, and acceptance rate are tracked per model per class, which is the basis for deciding when the foundation model should be replaced or fine-tuned.

The "edit distance" tracking is underused and is a credible BayOne differentiator. It is how you answer "is the pre-labeler actually saving time or are humans just correcting a lot?"

---

## 3. Auto-Labeling and Semi-Supervised Pipelines

### 3.1 Where auto-labeling actually works

Auto-labeling in AV is not "run a model and trust the output." It works in three specific configurations:

- **Offline perception (Motional, Waymo, Tesla).** Use a model that has access to the full temporal window (including future frames) to label past frames. The offline model is much more accurate than the online model because it can use motion and future context. Labels from the offline model train the online model. Motional's public writing on this is explicit. Source: [Motional auto-labeling](https://motional.com/news/technically-speaking-auto-labeling-offline-perception). Waymo's published "Pseudo-labeling for Scalable 3D Object Detection" paper shows performance gains across architectures and dataset sizes. Source: [Waymo pseudo-labeling research](https://waymo.com/research/pseudo-labeling-for-scalable-3d-object-detection/).
- **Tesla's three-step pipeline (AI Day 2022).** Clip capture, offline neural network bundle, robotics and algorithmic reconciliation to produce final labels. Scale: 10,000 clips auto-labeled in one week, versus months of human labor. Tesla characterizes this as "semi-auto labeling" because humans sample and verify. Tesla also shut down ~200 data-labeling roles in 2024 partly on the back of this pipeline scaling, which is the public indicator that it works.
- **Teacher-student pseudo-labeling.** Train a teacher on labeled data, use the teacher to pseudo-label unlabeled data, train a student on both, optionally iterate. ST3D, ST3D++, and the "Proficient Teachers" paper show this works for LiDAR 3D detection on Waymo and can match or beat fully-supervised performance with half the labels. Recent work (ASFG, 2025) reports 19.2% improvement with only 1% labeled data on KITTI and Waymo. Source: [Waymo Pseudo-labeling](https://waymo.com/research/pseudo-labeling-for-scalable-3d-object-detection/); [Semi-supervised 3D detection](https://link.springer.com/chapter/10.1007/978-3-031-19839-7_42); [ST3D++](https://www.researchgate.net/publication/364716469_ST3D_Denoised_Self-Training_for_Unsupervised_Domain_Adaptation_on_3D_Object_Detection).

### 3.2 Where auto-labeling fails

The honest failure modes to know for the Travis conversation:

- **Long-tail classes.** Auto-labelers systematically under-label rare classes because the teacher model under-detects them. If you feed the student pseudo-labels from the teacher, you reinforce the teacher's blind spots. This is one reason the Tesla and Waymo approaches emphasize human sampling of pseudo-labels for rare classes.
- **Domain shift.** A teacher trained on California data will produce unreliable pseudo-labels on Tokyo data (different road markings, different vehicle classes, right-hand drive). Cross-domain self-training without adaptation collapses quality.
- **Calibration drift.** Pseudo-label confidence is not calibrated to accuracy. Fixed thresholds leak wrong labels into the training set. Adaptive thresholding (ASFG and similar) is a partial fix.
- **Occluded and amodal 3D boxes.** Auto-labeling amodal 3D extent under heavy occlusion is still an open problem. Waymo's "multi-modal auto labeling pipeline" paper is framed around this.
- **Ground truth contamination.** If auto-labels get recycled into the training set unlabeled as auto-labels, you lose the ability to diagnose whether a model failure is a model failure or a label failure.

### 3.3 What this means for a BayOne engagement

Auto-labeling is not a "turn on and walk away" capability. A responsible auto-labeling pipeline for a Woven-class client is always guarded by (a) a human sampling rate, (b) per-class acceptance thresholds derived from measurement, not intuition, and (c) a clear provenance chain that keeps auto-labels distinguishable from human labels in the data warehouse. Any pitch that implies "we will auto-label everything" is a red flag; the credible pitch is "we will identify which slices can be auto-labeled with measured quality guarantees and we will triage the rest."

---

## 4. Foundation Models for AV Scene Understanding and Triage

### 4.1 What the foundation models give you beyond labeling

Beyond pre-labeling (Section 2), foundation models enable a different class of triage workflow:

- **Text-queried retrieval.** Given a fleet log, ask "find all clips where a cyclist is in a crosswalk at night." CLIP, GroundingDINO, and OWLv2 can score clips for this without any prior labeling. The retrieval is noisy; humans validate the top-k. This replaces the older pattern of pre-labeling every clip with a fixed taxonomy and then querying a structured database.
- **Scene graph and attribute extraction.** MLLMs generate captions and attribute tags (time of day, weather, road type, presence of emergency vehicles). These become filterable metadata across the corpus.
- **Open-vocabulary detection for edge cases.** When a safety driver reports "there was a weird object in the road," open-vocabulary detection lets you search for that object in other clips without first building a labeled training set for it. This is the shortest path from "we saw a new thing" to "how often does this new thing occur in our fleet."
- **Unsupervised 3D perception with 2D VLM distillation (Waymo).** Waymo's published work distills CLIP-style 2D features into 3D perception without 3D human labels, specifically for open-set categories. Source: [Waymo unsupervised 3D perception](https://waymo.com/research/unsupervised-3d-perception-with-2d-vision-language-distillation-for/).

### 4.2 Clustering and edge case mining with foundation-model embeddings

The operational pattern, sometimes called "scenario intelligence" (Wayve's term):

1. Run a frozen backbone (DINOv2/v3, CLIP, or a domain-adapted ViT) on every clip or frame.
2. Store embeddings in a vector index (FAISS, pgvector, Milvus).
3. For any seed clip of interest (a failure, a near-miss, a safety driver flag), retrieve the top-k most similar clips by cosine similarity.
4. Cluster the corpus (k-means, HDBSCAN) to expose naturally occurring scenario groups.
5. Label one exemplar per cluster and propagate, or use the clusters to prioritize active learning queries toward under-represented clusters.

Wayve explicitly describes using emergent concepts from their model for dataset introspection and coverage analysis. Source: [Wayve long-tail post](https://wayve.ai/thinking/e2e-embodied-ai-solves-the-long-tail/).

### 4.3 Honest limitations

- Foundation model embeddings are not AV-aware out of the box. A DINOv2 embedding will cluster "sunny highway" and "rainy highway" apart but may not cluster "cut-in from the left at 30mph" distinctly from "cut-in from the left at 50mph." Domain-adaptive fine-tuning or supervised contrastive learning on a small labeled subset substantially improves the signal.
- Vocabulary drift. An open-vocabulary detector prompted with "fire hydrant" will find things that look like fire hydrants, not things that Woven's taxonomy defines as fire hydrants. Bridging vocabulary to client taxonomy requires a translation layer.
- Compute cost at fleet scale. Embedding a petabyte of video is not free. The design question is always "which frames do we embed and at what resolution," and the answer is usually "one keyframe per N seconds at 224x224," which is lossy.

---

## 5. Human-in-the-Loop Quality Assurance

### 5.1 Mechanisms

The mature QA stack in 2026 combines several mechanisms that operate at different time scales:

- **Golden sets.** A curated set of labeled examples whose correctness is adjudicated and treated as ground truth. Used to measure annotator accuracy in real time. If an annotator's accuracy on golden items drops, they are flagged for retraining or review. Golden sets themselves must be re-adjudicated periodically; "gold" that still has disagreement is not gold. Source: [Twine golden sets](https://www.twine.net/blog/rubric-vs-guidelines-vs-golden-set/).
- **Redundant labeling with consensus.** For contested or high-risk classes, two or three annotators label independently. Consensus is taken by majority vote, skill-weighted vote, or adjudication escalation. Per-annotator skill scores feed the weighting.
- **Inter-annotator agreement (Cohen's kappa, Fleiss' kappa, or task-specific metrics like IoU agreement for boxes).** Used to identify ambiguous classes where the taxonomy itself is the problem, not the annotators.
- **Adjudication queues.** Disagreements above a threshold route to a senior annotator or ML engineer. Adjudication outcomes feed back into annotator training and sometimes into guideline revision.
- **Model-vs-human disagreement as a QA signal.** When a trained model strongly disagrees with a human label, route for review. Catches both model errors and human errors.
- **Calibration tests.** Periodic blind tests of annotator agreement with the golden set, done often enough to catch drift but rarely enough not to exhaust the team. Weekly is common.

### 5.2 Architectural implication

QA is not a pass at the end; it is a continuous layer that wraps every label event and emits a quality score. The data warehouse schema should record, per label: who labeled it, when, how long it took, what was the pre-label, what was the edit distance, what was the consensus state, and what is the current quality score. This is where most annotation platforms fall short and where a custom-integrated pipeline can win.

Source: [Kinde HITL evals at scale](https://www.kinde.com/learn/ai-for-software-engineering/ai-devops/human-in-the-loop-evals-at-scale-golden-sets-review-queues-drift-watch/); [SuperAnnotate HITL](https://www.superannotate.com/blog/human-in-the-loop-hitl).

---

## 6. Edge Case Mining

### 6.1 Techniques in use

- **Embedding similarity retrieval.** As in Section 4.2. Seed a query with a known edge case, retrieve similar examples. FiftyOne Brain, Voxel51, and Wayve's scenario intelligence tools all implement this pattern. Source: [FiftyOne Brain](https://docs.voxel51.com/brain.html).
- **Anomaly detection on embeddings.** Fit a density model (GMM, normalizing flow, isolation forest) on the embedding distribution. Low-density points are anomalies worth labeling. This finds "novelty" but also finds sensor artifacts, so output requires human triage.
- **Disagreement-based mining.** Frames where an ensemble disagrees (NVIDIA approach) or where auto-label and online model disagree are edge cases by construction.
- **Model-residual mining.** Run a model, collect frames with high loss or high error on a held-out evaluation set, retrieve similar frames from the unlabeled pool. Targets specific failure modes rather than generic "weirdness."
- **Behavioral criticality metrics.** For planning and prediction models, mine for scenarios where the model's plan diverges from the human driver's action or where the cost function spikes. The "Mining the Long Tail" paper (2025) describes this explicitly. Source: [Mining the Long Tail arXiv](https://arxiv.org/html/2508.18397).
- **Synthetic scenario generation for coverage.** Wayve's Ghost Gym generates photorealistic 4D scenarios to fill gaps in real data. Source: [Wayve Ghost Gym](https://wayve.ai/thinking/ghost-gym-neural-simulator/). Real-world coupling is still a research problem; generated data helps train but does not yet fully replace on-road data for safety cases.

### 6.2 The 2026 operational frame

The organizing metaphor across Wayve, Waymo, and the newer academic literature is "scenario coverage." The question is not "how many frames do we have" but "what fraction of the operational design domain is densely covered by labeled examples?" Edge case mining is how you move from the first question to the second. Tools that treat the dataset as an indexed, introspectable artifact (FiftyOne, Encord, Scale Nucleus, internal Wayve tooling) are what operationalize this.

---

## 7. Existing Tools and Frameworks

A pragmatic categorization, with a note on trade-offs:

**Annotation platforms with integrated AI assistance**

- **Encord.** Strong on multimodal (2D, 3D, LiDAR, radar, video), SAM 2 integrated, workflow agents, SOC 2 and GDPR. Called out in 2025-2026 comparisons as the leader for AV specifically. Their "Physical AI suite" unifies 3D, camera, and radar in one workflow. Source: [Encord AV platforms](https://encord.com/blog/ai-data-labeling-platforms-for-autonomous-vehicle-development/).
- **Scale AI.** Deep AV heritage. Combines tooling with managed workforce. Scale Nucleus for dataset exploration. Strong on large managed programs, less flexible for custom pipelines.
- **Labelbox.** Strong on collaboration and MAL (model-assisted labeling). More general-purpose than AV-specific.
- **V7.** AI-assisted annotation with workflow automation. Tends to be lighter weight.
- **CVAT (open-source).** Community-maintained, SAM 2 integration, can be self-hosted. The default starting point for teams that want to own their stack.
- **Label Studio (open-source, Heartex).** Similar positioning to CVAT. Flexible, less AV-specialized.
- **SuperAnnotate, BasicAI, Kili.** Regional or niche players with specific strengths.

**Dataset curation and mining**

- **Voxel51 FiftyOne.** De facto standard for embedding-based dataset exploration in CV. FiftyOne Brain for similarity, uniqueness, hardness, and near-duplicate detection. Open-source core with Enterprise tier. Frequently used adjacent to an annotation platform, not as a replacement. Source: [Voxel51 FiftyOne](https://github.com/voxel51/fiftyone).
- **Scale Nucleus.** Scale's dataset exploration and curation layer. Tightly integrated with Scale's annotation services.

**Foundation model runtimes**

- SAM 2.1 / SAM 3 via Meta / Hugging Face.
- GroundingDINO via IDEA-Research.
- DINOv2 / DINOv3 via Meta.
- OWLv2 via Google.
- Open-source orchestration via Ray, Flyte, or Union.ai (Woven is already on Union.ai).

**Active learning frameworks**

- modAL, baal (Bayesian active learning), NVIDIA's open research code.
- Most production AL is custom because the acquisition function is domain-specific.

**Trade-offs framing for Travis**

- Buy (Encord, Scale): fast time-to-value, vendor lock, and the platform's taxonomy of "what a label looks like" is not always the same as the client's internal data model.
- Build: owns the data model and cost curve, but requires the engineering team that Woven is already hiring for.
- Hybrid (common): buy the annotation UI, build the orchestration, active learning, and data lake. This is the most common shape and is where BayOne can land.

---

## 8. A Realistic BayOne Engagement Shape

This section is the one that matters for the Travis conversation. The goal is to have a concrete answer if Travis asks "what would you actually do?"

### 8.1 Engagement shape

A credible hybrid AI labeling engagement for a Woven-scale client is a phased program, not a pilot-to-production single arc. Three phases:

**Phase 1: Instrumentation and baseline (6-8 weeks)**

Deliverables:
- Audit of current labeling pipeline: per-class throughput, cost per label, current model-assist usage, annotator-level quality distribution, and identified bottleneck classes.
- A labeled baseline for speedup measurement: a held-out set of N frames labeled with current workflow and with timing data, so Phase 2 improvements are measurable against a real baseline, not a vendor benchmark.
- A target architecture document covering active learning loop, pre-labeling model routing, QA mechanisms, and data governance.
- One or two foundation-model pre-labeling prototypes on actual client data, with measured edit distance and time saved.

Team: 1 Principal (Colin or equivalent), 1 Senior ML Engineer, 1 Data Engineer. Part-time PM.

**Phase 2: Loop installation (12-16 weeks)**

Deliverables:
- A production active learning loop with one acquisition function (ensemble disagreement or inconsistency-based, chosen based on Phase 1 findings) running on an agreed target class set.
- A pre-labeling service wrapping SAM 2 and GroundingDINO (or domain-equivalent) with an edit-distance telemetry layer.
- Integration with the client's labeling UI (Encord/Scale/CVAT, whichever is in use).
- A golden set and consensus workflow for the target classes.
- Weekly metric reporting on labels-per-hour, per-class accuracy against golden set, and model benchmark on held-out eval.

Team: 1 Principal part-time, 2 Senior ML Engineers, 1 Data Engineer, 1 MLOps Engineer. Client-side product owner required.

**Phase 3: Scale and handoff (8-12 weeks)**

Deliverables:
- Extension of the loop to additional class sets or modalities.
- Edge case mining pipeline (embedding index, similarity retrieval, anomaly detection) wired to the labeling queue.
- Teacher-student auto-labeling where measurement supports it, with guardrails (human sampling rate, per-class acceptance thresholds, provenance tracking).
- Runbooks, training for the client team, and a handoff period where BayOne is on call but not driving.

Team: 1 Principal part-time, 1 Senior ML Engineer, 1 MLOps Engineer. Client team takes over day-to-day.

Total: 26-36 weeks end to end. Total BayOne team over the life of the engagement: 3-5 named people with surge capacity.

### 8.2 Technical components

- Orchestration: Union.ai or Flyte (Woven is already on Union.ai, so this is the safe default).
- Foundation model inference: Triton, vLLM, or SageMaker / Vertex endpoints depending on client cloud.
- Embedding store: FAISS or pgvector for smaller corpora; Milvus or a managed service for fleet-scale.
- Dataset curation: FiftyOne (open-source), upgraded to Enterprise if needed.
- Annotation UI: Whatever the client is on. BayOne is UI-agnostic and integrates.
- Data lake: Client's existing (Databricks, Snowflake, S3/Iceberg).
- Governance: Versioned datasets with per-label provenance, auto-label vs human-label distinction preserved end to end.

### 8.3 What differentiates this from a typical labeling consultancy pitch

Three things, all of which should come up in the Travis conversation:

1. **Edit-distance telemetry.** Most vendors report speedup; few measure it. BayOne installs the measurement layer from day one, which means year-two value is defensible.
2. **Honest failure-mode framing.** Auto-labeling is guarded, not blind. Foundation models are bounded, not magical. This is the credibility test with a technical buyer at Woven.
3. **Loop ownership, not tool ownership.** BayOne does not sell Encord or Scale or CVAT. BayOne builds the loop around whatever tooling the client already has. That positioning de-risks the engagement for Travis because it avoids a platform-swap conversation.

### 8.4 Pricing frame (not a commitment, an order of magnitude)

Phase 1 is a 6-8 week fixed-price engagement in the low-mid six figures, scoped by class set and baseline work. Phase 2 and Phase 3 are T&M or milestone-based, scaling with team size. Total program cost over 26-36 weeks for a team averaging 3 FTEs is in the range of a mid-seven-figure multi-year program if Phase 3 extends into ongoing operation. Do not volunteer these numbers in the discovery call; they are for Colin's internal calibration.

---

## 9. Open Questions

Questions to either answer before the 3:30 PM call or hold for the call itself, depending on how the opening goes:

1. **What annotation tooling is Woven currently on?** Encord, Scale, CVAT, or internal? The integration shape of Phase 2 depends on this.
2. **What is the current split between human labeling and any automated pre-labeling they already run?** Woven's 2021 DGP post and 2025 job descriptions suggest the Data Annotation and Labeling Engineering team already has internal tooling; the opportunity may be augmenting rather than replacing.
3. **Which modalities are the current pain?** Camera, LiDAR, radar, or fusion? Each has different foundation-model options and different auto-labeling track records.
4. **What classes are the current cost drivers?** Pedestrians, vehicles, and lane markings are usually well-solved; rare classes (construction zones, emergency vehicles, unusual cargo) are where active learning and open-vocabulary detection pay off most.
5. **Is the work for Woven's own AV program or for Toyota-group partners using Arene?** The governance and data-sharing constraints are very different and the engagement shape changes.
6. **Where is the quality bar set?** Safety-critical perception for L4 has a much higher bar than research datasets. This determines the golden-set investment.
7. **What does the existing offline-perception / pseudo-labeling pipeline look like, if any?** Motional-style offline perception is public; Woven's approach is not. If they already have this, BayOne's value is in the active learning loop and edge case mining layer, not in auto-labeling itself.
8. **How does Travis define "success" for the data triage problem he is trying to solve?** Throughput, cost, quality, coverage, or time-to-resolve on edge cases? These drive which metrics the engagement commits to.

---

## 10. Sources

Primary references used:

- NVIDIA: [Scalable Active Learning for Autonomous Driving](https://medium.com/nvidia-ai/scalable-active-learning-for-autonomous-driving-a-practical-implementation-and-a-b-test-4d315ed04b5f)
- ActiveAD (CVPR 2026): [OpenReview](https://openreview.net/forum?id=7Zppme1swQ), [GitHub](https://github.com/Thinklab-SJTU/ActiveAD)
- Inconsistency-based LiDAR AL: [arXiv 2505.00511](https://arxiv.org/html/2505.00511)
- Digital Divide Data: [Active Learning in AV Pipelines](https://www.digitaldividedata.com/blog/active-learning-in-autonomous-vehicle-pipelines)
- CloudFactory: [Under the Hood: Active Learning](https://www.cloudfactory.com/blog/active-learning-and-autonomous-vehicles)
- Meta SAM 2.1: [Encord on SAM 2.1](https://encord.com/blog/sam-2.1-explained/)
- CVAT SAM 2: [Video Annotation with SAM 2](https://www.cvat.ai/resources/changelog/video-annotation-sam-2)
- Roboflow on SAM 3: [What is SAM 3](https://blog.roboflow.com/what-is-sam3/)
- Grounding DINO 1.5: [arXiv 2405.10300](https://arxiv.org/html/2405.10300v1)
- OpenAD benchmark: [arXiv 2411.17761](https://arxiv.org/html/2411.17761v1)
- DINOv3: [Encord explainer](https://encord.com/blog/dinov3-explained-scaling-self-supervised-vision-tr/)
- Tesla auto-labeling: [Saneryee deep dive](https://saneryee-studio.medium.com/deep-understanding-tesla-fsd-part-4-auto-labeling-simulation-60c9bfd3bcb5), [Kargar AL/auto-labeling series](https://kargarisaac.medium.com/active-learning-data-selection-data-auto-labeling-and-simulation-in-autonomous-driving-part-4-dc985e2c83f9)
- Motional offline perception: [Motional: Auto-labeling With Offline Perception](https://motional.com/news/technically-speaking-auto-labeling-offline-perception)
- Waymo research: [Pseudo-labeling for 3D Object Detection](https://waymo.com/research/pseudo-labeling-for-scalable-3d-object-detection/), [Unsupervised 3D Perception via 2D VL Distillation](https://waymo.com/research/unsupervised-3d-perception-with-2d-vision-language-distillation-for/), [Motion Inspired Unsupervised Perception](https://waymo.com/research/motion-inspired-unsupervised-perception-and-prediction-in-autonomous-driving/)
- Semi-supervised 3D detection (Proficient Teachers): [Springer](https://link.springer.com/chapter/10.1007/978-3-031-19839-7_42)
- ST3D++: [ResearchGate](https://www.researchgate.net/publication/364716469_ST3D_Denoised_Self-Training_for_Unsupervised_Domain_Adaptation_on_3D_Object_Detection)
- Wayve: [Long-tail with e2e AI](https://wayve.ai/thinking/e2e-embodied-ai-solves-the-long-tail/), [Ghost Gym](https://wayve.ai/thinking/ghost-gym-neural-simulator/), [Safety framework](https://wayve.ai/technology/safety-framework/)
- Long-tail mining: [arXiv 2508.18397](https://arxiv.org/html/2508.18397)
- WOD-E2E: [arXiv 2510.26125](https://arxiv.org/html/2510.26125v1)
- Voxel51 FiftyOne: [GitHub](https://github.com/voxel51/fiftyone), [Brain docs](https://docs.voxel51.com/brain.html), [Self-driving guide](https://docs.voxel51.com/getting_started_guides/self_driving/index.html)
- Platform comparisons: [Encord on AV platforms](https://encord.com/blog/ai-data-labeling-platforms-for-autonomous-vehicle-development/), [Encord on Physical AI 2026](https://encord.com/blog/data-labeling-platforms-for-physical-ai/), [Label Your Data on Scale alternatives](https://labelyourdata.com/articles/scale-ai-competitors)
- QA and golden sets: [Twine rubrics/guidelines/golden sets](https://www.twine.net/blog/rubric-vs-guidelines-vs-golden-set/), [Kinde HITL evals at scale](https://www.kinde.com/learn/ai-for-software-engineering/ai-devops/human-in-the-loop-evals-at-scale-golden-sets-review-queues-drift-watch/), [SuperAnnotate HITL](https://www.superannotate.com/blog/human-in-the-loop-hitl)
- HITL survey (2024): [arXiv 2408.12548](https://arxiv.org/html/2408.12548v2)
- Woven by Toyota: [Arene DGP post](https://woven.toyota/en/our-latest/20210927/), [Union.ai case study](https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai), [Enterprise AI Data Platform SSE JD](https://jobs.lever.co/woven-by-toyota/28fbe931-ed43-4dba-a52b-1a0c155d161c)
