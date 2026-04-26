# 04 - Research: AV Sensor Data and Triage Workflows

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** AV sensor data characteristics and production triage workflow patterns

---

## Purpose

This document supports preparation for the 3:30 PM PST discovery call on 2026-04-23 with Travis Millet, Manager of Technical Operations Engineering at Woven by Toyota. The problem domain is data triaging for autonomous vehicle testing. The goal is to walk into the call with an accurate, current picture of what AV test data actually contains, what the triage function is responsible for in a modern AV development shop, where the common production bottlenecks sit, and what Woven by Toyota in particular has said publicly about its data platform.

Scope notes:

- All sources here are public web material. Prioritization was given to content from the last 24 months.
- Where an item is specific to a single developer (Waymo, Wayve, Mobileye, Zoox, Woven by Toyota) it is attributed. Where an item reflects a generic industry pattern it is flagged as such.
- No em dashes or contractions are used in analytical sections. Citations are inline URLs, aggregated at the end.

---

## 1. What AV sensor data actually looks like in production testing

### 1.1 Sensor modalities and typical configurations

Modern Level 2 through Level 4 test vehicles carry a layered suite of perception sensors, vehicle state sensors, and localization sensors. The rough shape of the sensor set is well known and consistent across Waymo, Cruise, Zoox, Motional, Aurora, and Mobileye.

| Modality | Typical count per test vehicle | Typical rate | Typical resolution or density | Primary role |
|---|---|---|---|---|
| RGB cameras (surround and forward) | 6 to 12 | 10 to 30 Hz, with most production stacks at 10 to 20 Hz | 1.2 MP to 8 MP per camera, with 2 MP (1080p-class) and 5 MP as common mid-range, and 8 MP appearing in newer stacks | Semantic perception, lane marking, traffic sign and light recognition, free-space estimation |
| Near-infrared or low-light cameras | 0 to 2 | 10 to 30 Hz | 1 to 2 MP | Night and tunnel perception |
| Mechanical spinning lidar | 1 to 5 | 10 Hz standard, 20 Hz on newer units | 64 to 128 channels, 1 to 2 million points per second per unit, with Valeo SCALA 3 at up to 12 million points per second and 2025 automotive norm at 128 to 256 channels at 200 to 300 m range | Precise 3D geometry, dense object localization |
| Solid-state or semi-solid-state lidar | 1 to 6 | 10 to 20 Hz | Variable, typically a few hundred thousand points per frame | Forward and side 3D perception, cheaper than spinning units |
| FMCW lidar (Aeva and others) | 0 to 2 | 10 Hz typical | Point cloud plus per-point radial velocity (Doppler) | 3D geometry with native velocity, helpful for motion segmentation |
| Short-range radar | 4 to 8 | 20 Hz | Lower angular resolution, strong range and radial velocity | Close-in object detection, blind spot, parking |
| Long-range radar (77 GHz) | 1 to 4 | 10 to 20 Hz | Traditional 3D (range, azimuth, radial velocity) | Highway forward perception |
| 4D imaging radar | 0 to 6 | 10 to 20 Hz | Elevation, azimuth, range, Doppler; tens of thousands of detections per frame | Elevation-aware object and free-space estimation; all-weather redundancy to lidar |
| IMU (inertial measurement unit) | 1 to 2 (often redundant) | 100 to 1000 Hz, commonly 400 Hz | 6-axis (accel and gyro), sometimes 9-axis | High-rate ego motion, dead reckoning |
| GNSS or GPS with RTK or PPP corrections | 1 to 2 | 1 to 20 Hz | Centimeter-class with RTK, meter-class raw | Global localization reference |
| Wheel odometry and wheel speed | 4 (one per wheel) | 50 to 100 Hz | Pulse counts per wheel | Short-horizon motion estimate, fusion with IMU and GNSS |
| Steering angle, throttle, brake pressure | From vehicle CAN bus | 50 to 200 Hz per signal | Scalar signals | Driver intent capture, model-in-the-loop reasoning, control ground truth |
| Vehicle CAN bus (full) | 1 to 4 CAN buses | Thousands of messages per second across all IDs | Many discrete signals (engine, powertrain, chassis, body, ADAS) | Full vehicle state, fault diagnostics, ADAS system status |

Notes on the above:

- The 10 Hz norm for lidar is a consequence of the 100 ms real-time processing budget that most perception stacks target. Sensor vendors offer 20 Hz modes, and some teams use them when downstream compute permits.
- Camera counts converged around 7 to 11 for L4 robotaxi platforms. Tesla famously uses an 8-camera vision-only stack for consumer Full Self-Driving. Dedicated test vehicles typically run more.
- The CAN bus is less glamorous than perception data but is load-bearing during triage because most ground truth for control, driver intent, and state machine behavior lives there. Powertrain, chassis, and body CANs carry throttle, brake, steering, gear, lights, wiper state, and ADAS system flags.

### 1.2 Data volumes per vehicle per hour of testing

Public estimates cluster around a wide range because they depend on retained resolution, number of cameras, whether raw or compressed frames are stored, and how much is dropped at the edge. Tuxera, Samsung Semiconductor, NI, Siemens Polarion, and Premio all publish figures in the same order of magnitude.

| Band | Per hour | Per 8-hour shift | Driver of band |
|---|---|---|---|
| Low (L2, modest camera count, compressed) | 1 to 2 TB | 10 to 15 TB | H.264 or H.265 camera, low-rate lidar, decimated radar |
| Mid (L4 test vehicle, typical) | 4 to 8 TB | 30 to 60 TB | Uncompressed or lightly compressed camera, full lidar, full CAN |
| High (full fidelity L4 test vehicle) | 19 to 40 TB | 150 to 300 TB | Raw multi-camera at full rate, multiple lidar, imaging radar, full auxiliary sensors |

A 10-vehicle test wave at the high end produces petabyte-per-day volumes. Tuxera cites 200 TB in an eight-hour shift as a realistic high-end number for a single test car. This is the physical reality that drives the need for on-vehicle filtering, tiered storage, and asynchronous triage.

### 1.3 On-vehicle log formats

Most AV developers converged on one of three container families for sensor logs:

- **MCAP.** Open-source, schema-embedded, append-only container optimized for timestamped multi-sensor data. Became the default rosbag2 storage format in ROS 2 starting with the Iron Irwini release in 2023. Widely adopted for robotics and AV logging because files remain self-describing, survive interrupted recording, and play back well in tools like Foxglove.
- **ASAM MDF4 (.mf4).** The ASAM standard for automotive measurement data. Common where CAN bus and AUTOSAR-oriented toolchains dominate.
- **Proprietary internal formats.** Waymo, Cruise, Tesla, Mobileye, and others historically built their own columnar or chunked formats for scale. AWS, NVIDIA, and other pipeline vendors now accept ingestion from ROS bag, MCAP, and MDF4 side by side.

A recent technical report on hierarchical AV storage (AVS, arXiv 2511.19453) argues that ROS bag and MCAP are append-oriented and optimized for offline replay, which creates query and ingestion bottlenecks at fleet scale. The same report describes modality-aware reduction and hot-cold tiering as standard practice in 2025-era production systems.

---

## 2. What "data triaging" means in AV development

Data triaging in AV development is the set of activities that take raw fleet logs and turn them into an ordered queue of events, clips, and scenarios that engineering teams actually work on. It is not a single job. It is a workflow that spans operations, data engineering, perception, planning, ML training, and safety review.

### 2.1 Core activities in an AV triage function

**Event and scenario identification.** Detecting and tagging interesting slices of a log. Examples: an unprotected left, a merge in heavy rain, a cyclist cutting across a roundabout. Tags are generated by a mix of rule-based heuristics on sensor channels, offline models applied to the logs, and natural language queries against embedding indexes.

**Edge case mining.** Finding rare or novel situations in collected data. Applied Intuition, Foxglove, and the Wayve and AWS-NVIDIA AV 3.0 architectures all describe this as a retrieval problem against a vector index of clip embeddings. Production methods cluster into four families: active learning on model uncertainty, similarity search on embeddings, out-of-distribution detection, and rule-based scenario filters (Kognic, arXiv 2410.08491).

**Anomaly detection.** Spotting unusual sensor behavior (dropped frames, timestamp skew, calibration drift), unusual vehicle behavior (hard brakes, unexpected steering corrections, throttle oscillation), or unusual traffic events (a pedestrian entering the roadway, a construction zone layout that differs from the map).

**Disengagement analysis and safety-critical event review.** Every disengagement (either operator-initiated or system-initiated) is reviewed. California DMV data and PLOS ONE analysis put reaction times around 0.83 seconds. A non-trivial fraction of disengagements are classified as safety-critical, and a subset of those would have led to collisions. Over 90 percent of takeover root causes are software Safety of the Intended Functionality (SOTIF) issues rather than hardware functional safety faults (ScienceDirect survey on SOTIF, 2024). Triage for these events is typically higher priority, faster SLA, and often has a dedicated on-call rotation.

**Log classification and routing.** Once a clip is tagged with what went wrong (perception miss, tracker ID switch, prediction error, planner hesitation, control overshoot, localization drift), it is routed to the team that owns that component. Applied Intuition calls this "tagging and filtering" and notes that specialized groups (perception, fusion, localization, planning) each need different slices of the same log.

**Labeling prioritization.** Triage decides what subset of filtered data is worth paying to label. This is where auto-labeling pipelines (such as Waymo's 3D Auto Labeling, described in arXiv 2103.05073) and human-in-the-loop review converge. The interesting tension is that the clips most worth labeling are usually the ones where auto-labelers are least confident.

### 2.2 How triage ops teams typically work with data science and ML training teams

The standard shape of the collaboration, across Waymo blog posts, Wayve's AV2.0 writeups, Applied Intuition's and Foxglove's product pages, and the AWS-NVIDIA AV 3.0 reference architecture, is:

- **Triage ops** owns first-pass filtering and routing. They run the platform, write heuristics and queries, maintain tags, handle the on-call for safety-critical events, and produce the curated queues that feed downstream teams.
- **Data science and ML training** consume those queues. They build and retrain models, run active learning loops that feed new uncertainty-based queries back into triage, and request targeted additional data collection.
- **Perception, planning, prediction, and control teams** own their respective slices of the stack and consume triage output specific to their component. They often maintain their own scenario suites for regression.
- **Safety and validation** sits across the top, owning the overall scenario catalog, ODD coverage, and release gating.

The active learning loop is the primary integration point between triage ops and ML training. Ops produces labeled edge cases. ML trains on them and emits a new model with new uncertainty fingerprints. Ops uses those fingerprints to mine the next batch. Wayve explicitly describes this as a rapid, continuous fleet-learning loop for AV2.0.

---

## 3. A typical AV data pipeline from collection to training

The most detailed recent public reference is the AWS plus NVIDIA AV 3.0 architecture. It matches in shape with what Wayve, Waymo, Applied Intuition, and Foxglove describe, and it is consistent with what Woven by Toyota has published about its own platform. The pipeline has roughly eight stages in four phases.

| Phase | Stage | What happens | Typical tools |
|---|---|---|---|
| Ingest | 1. On-vehicle capture and buffering | Sensor drivers write to MCAP, ROS bag, or MDF4. Some early filtering and lossless compression happens at the edge. Interesting-event triggers can prioritize retention. | Custom loggers, rosbag2 with MCAP plugin, AUTOSAR recorders |
| Ingest | 2. Upload and ingestion | Physical media transfer on return to depot (AWS Data Transfer Terminal, Snowball) or network upload over private fiber or dedicated interconnects. Quality validation checks for missing channels, timestamp skew, corruption. Raw material lands in S3 or equivalent object storage. | AWS Data Transfer Terminal, direct upload, AWS Batch validators |
| Data Processing | 3. Indexing and metadata extraction | Per-log metadata catalog is populated: ODD attributes (map, weather, time of day), event markers, disengagement flags, CAN-derived driver and system state. Woven by Toyota explicitly built this decoupling between metadata catalog and full image extraction. | Custom metadata catalogs, OpenSearch, NVIDIA Cosmos Dataset Search |
| Data Processing | 4. Triage, curation, and mining | Embedding generation on camera frames and clips, vector search, natural language queries, scenario tagging, active learning queries. Applied Intuition's Data Explorer, Foxglove's data platform, and NVIDIA Cosmos Curator all sit at this stage. | Multimodal foundation models, two-tower retrieval, Apache Spark, vector databases |
| Data Processing | 5. Labeling | Human-in-the-loop annotation of the curated subset, plus auto-labeling for tasks where a larger offline model can out-perform real-time models. 3D bounding boxes, semantic segmentation, tracklets, behavior labels. Quality gates use inter-rater agreement (Cohen's kappa > 0.75 is a common benchmark). | Scale AI, iMerit, Kognic, Encord, plus internal tools |
| Train | 6. Dataset curation and versioning | Curated clips plus labels plus synthetic variants get packaged into versioned training sets. Synthetic augmentation is increasingly important (NVIDIA Cosmos Transfer, weather and lighting variants). | Internal data lake, DVC-like versioning, data catalogs |
| Train | 7. Model training and evaluation | GPU-accelerated training, often petabyte-scale. Wayve trains foundation models end-to-end on petabyte datasets. Woven by Toyota reports hundreds of thousands of node hours on Union.ai. | PyTorch, JAX, Ray, Flyte, Union.ai, SageMaker HyperPod |
| Validate | 8. Regression testing, simulation, release gating | Open-loop log replay, closed-loop simulation on reconstructed scenes (NVIDIA NuRec, Zoox scenario diffusion), KPI tracking, safety case updates. | Applied Intuition Log Sim, NVIDIA AlpaSim, internal sim |

A few characteristic patterns across this pipeline:

- **Metadata first, pixels later.** Woven by Toyota's platform, Wayve's foundation-model-based indexing, and the AWS-NVIDIA reference all decouple "find what you want" from "materialize the pixels you want." This is the single biggest design shift in AV data platforms over the last three years.
- **Retrieval-driven training.** The AWS AV 3.0 post says this explicitly. Datasets are not fixed. They are continuously reshaped based on model weaknesses. Embeddings are the index. Vector search plus natural language search are the query interface.
- **Simulation as a first-class consumer of triaged data.** Reconstructed real-world scenes are replayed in sim for regression, and triaged edge cases become the seeds for generative scenario variation (Zoox scenario diffusion, NVIDIA Cosmos Transfer).

---

## 4. Common failure modes and bottlenecks in AV triage operations

This is the part that is most relevant to the Travis conversation, because "triaging" as a stated engagement topic implies there is operational pain somewhere in this list.

### 4.1 Volume versus quality tradeoff

The fundamental tension. A 10-vehicle fleet at 8 TB per vehicle per hour produces 80 TB per hour of sensor data. Not all of that is worth keeping at full fidelity. Deciding what to drop at the edge, what to retain compressed, what to index in metadata, and what to keep pixel-accurate for labeling is a recurring policy decision. Applied Intuition markets this explicitly as a cost-savings driver, claiming that efficient selection reduces infrastructure costs by millions for large programs.

### 4.2 Ingestion and upload bandwidth

NI, DXC, and NetApp writeups, plus the AVS arXiv report, all call out that ingestion pipelines are frequently the actual bottleneck, not storage capacity. The limit is not SSD or disk. It is the path between vehicle and cloud (physical media shipping plus finite interconnect bandwidth), combined with append-oriented log formats that do not support online querying while files are being written. A 100 Gbps cloud link theoretically moves 1 PB in 24 hours, but in practice closer to half that, and a single-day 10-car wave can produce 2 PB.

### 4.3 Inter-rater disagreement and labeling quality

Labeling is expensive and inconsistent. Benchmarks such as Cohen's kappa > 0.75 are used, but in practice pedestrian edge precision, occluded object consistency, and ambiguous scene tags generate inter-rater drift. Low agreement produces noisy labels, which produce worse models, which produce more ambiguous downstream triage. This is a recognized loop, covered in Springer's "Attribute annotation and bias evaluation in visual datasets for autonomous driving" and in the broader ML annotation QA literature.

### 4.4 Missed edge cases

Edge case detection is a known-hard problem. The survey in arXiv 2410.08491 describes the taxonomy, and the consistent message across production vendors is that no single method catches everything. The bottlenecks are data sparsity, sim-to-real gap on synthetic edges, interpretability of neural detectors, threshold selection, and poor cross-scenario generalization. Operationally, this shows up as a long tail of "we should have caught that" post-incident reviews.

### 4.5 Slow ingestion and slow indexing pipelines

Indexing a week of fleet data is an asynchronous batch job in most shops. If that batch falls behind, the time from a real-world drive to a queryable, triageable clip stretches out. Engineers cannot run follow-up queries against data that is still in flight through the pipeline. This directly degrades the feedback loop between ML training and ops.

### 4.6 Lost signal between ops and ML teams

A recurring organizational pattern. Ops teams tag clips with their taxonomy. ML teams need a different taxonomy for training. The mapping between the two is maintained manually or not at all. Triage outputs decay into stale queues. ML teams build shadow pipelines. Applied Intuition's "4 triage essentials" post leans hard on this, and it is consistent with what Wayve describes as the motivation for its single unified fleet-learning loop.

### 4.7 Tagging taxonomy drift

Related to the previous point. The scenario and event taxonomy is a living artifact. New ODD additions, new sensors, and new behaviors drive taxonomy changes. Without disciplined versioning, historical tags become unreliable, which breaks longitudinal analysis and regression queries.

### 4.8 Safety-critical event SLA pressure

Disengagement review and safety-critical event triage often have a tight SLA (for example, within 24 hours of ingestion). When the upstream pipeline slips, the SLA slips, which creates pressure to keep everything at high retention, which makes the upstream pipeline worse. This is a known vicious cycle.

---

## 5. What Woven by Toyota has said publicly about its data stack

This is worth pulling out separately because Travis Millet sits inside Technical Operations Engineering at Woven by Toyota, and the contents of public Woven material are useful for context.

- **First-generation platform.** The November 2021 Woven blog ("The Evolution of Our Data Platform") says the first platform ingested double-digit petabytes of data across two years. The original pipeline pre-extracted lossy image frames from fleet video at low sampling rates. Only a small fraction of those frames were ever used.
- **Shift to metadata-first.** The same post describes a shift to a metadata catalog indexed by map attributes, weather, and time of day, with on-demand extraction of pixels for the clips that users actually want. This is the pattern the broader industry has since converged on.
- **Stereo camera fleet device.** An April 2022 Woven post describes an in-house roof-pod stereo camera that is roughly 90 percent cheaper than prior sensors and is designed for large-scale deployment across Toyota passenger vehicles. They explicitly mention mining camera data to find examples of specific scenario types (for example, following a lead vehicle to a stop) for targeted training.
- **Union.ai migration.** In 2023 Woven by Toyota migrated from self-managed Flyte to Union.ai as the foundation of its AI development infrastructure. The Union.ai case study reports 20 times faster ML iteration cycles, more than 1 million dollars in annual savings, petabyte-scale sensor data, hundreds of thousands of node hours, and thousands of parallel workers. Union.ai sits across annotation, perception labeling, dynamic scene processing, and GPU-accelerated training.
- **Arene vehicle OS.** Woven's Arene software platform debuted in the 2026 Toyota RAV4. It is positioned as a long-horizon vehicle operating system and software development platform for Toyota and Lexus vehicles, including automated driving features. Data collection from Arene-equipped vehicles is potentially enormous if and when it reaches Toyota-scale production volumes.
- **Woven City.** Woven City officially launched in September 2025 in Susono, Shizuoka as a real-world testing ground for mobility, robotics, and smart infrastructure. This is an additional source of test data beyond the on-road fleet.

What public material does not disclose: specific per-vehicle data rates, number of test vehicles, the internal taxonomy for triage, the SLA targets for disengagement review, the team structure inside Technical Operations Engineering, or the specific commercial tools (Applied Intuition, Foxglove, Scale, and so on) that may or may not be in the stack.

---

## 6. Public material from other AV developers worth referencing

- **Waymo.** Open dataset documentation and labeling specifications (GitHub waymo-research). "Offboard 3D Object Detection from Point Cloud Sequences" (arXiv 2103.05073) describes their 3D auto-labeling pipeline. Multiple blog posts on active learning, automated augmentation, and scalable ML for the Waymo Driver. WOD-E2E (arXiv 2510.26125) focuses on end-to-end driving in challenging long-tail scenarios.
- **Wayve.** "AV2.0" technology page, "Scaling Embodied AI for Autonomous Driving with Microsoft Azure" and "Measuring autonomy performance" blog series. Describes retrieval-driven dataset curation, foundation models for scenario classification, and fleet-learning loops. GAIA-1 and GAIA-3 generative world models for safety and evaluation.
- **Mobileye.** Road Experience Management (REM) crowdsourced mapping approach. Less than 10 KB per kilometer, centimeter accuracy, anonymized ingestion. Mobileye blog on next-generation active sensors (radar, lidar). AWS Graviton post on REM ML inference optimization.
- **Zoox.** Amazon Science post "Scenario Diffusion helps Zoox vehicles navigate safety-critical situations." Focus on synthetic scenario generation for rare events.
- **Cruise, Aurora, Motional.** Less public technical material in the last 24 months, partially because of Cruise's 2023-2024 operational difficulties and post-acquisition integrations at Motional and elsewhere. Useful mostly as reference points for disengagement event handling and safety case structure.
- **Tesla.** Public material is limited to Autonomy Day and AI Day talks, plus third-party analysis. Referenced here mostly because Tesla's vision-only, fleet-scale shadow-mode data collection is philosophically very different from a Waymo-style sensor-heavy L4 fleet. Useful framing for Woven's Toyota-scale production fleet opportunity.

Academic and vendor references worth citing in conversation:

- "A Survey on Autonomous Driving Datasets" (arXiv 2401.01454).
- "A Systematic Review of Edge Case Detection in Automated Driving" (arXiv 2410.08491).
- "Mining the Long Tail" on criticality metrics for offline RL in motion planning (arXiv 2508.18397).
- AWS and NVIDIA "Building an End-to-End Physical AI Data Pipeline for Autonomous Vehicle 3.0" reference architecture.
- Applied Intuition blog: "AI for mining massive autonomy datasets" and "4 triage essentials for AV development."
- Foxglove product and data management tools pages, including the April 2026 unified data platform launch.

---

## 7. Open questions that matter for the Travis call

These are the questions where the public material runs out and where Travis is the actual source of truth.

1. **What are Woven's current ingestion volumes per day from the on-road fleet, and how is that split between Tokyo or Japan operations, Woven City, and any North American or European fleet?** The public number is double-digit petabytes over two years, circa 2021. The current number is almost certainly much larger but unconfirmed.

2. **What does Technical Operations Engineering own inside Woven?** Specifically, does it own the on-vehicle logger and uplink, the ingestion and indexing pipeline, the triage workflow and tooling, the labeling operations vendor relationship, all of the above, or some subset? The scope of the function drives what a BayOne engagement can usefully touch.

3. **Which parts of the pipeline use commercial tooling (Applied Intuition, Foxglove, Scale AI, Kognic, Encord, Union.ai, NVIDIA Cosmos) and which parts are fully internal?** This is load-bearing for any proposal.

4. **What is the current triage taxonomy, and how is it versioned?** If there is taxonomy drift pain, it is a concrete intervention point. If the taxonomy is well maintained, the pain is probably elsewhere (retrieval quality, labeling throughput, ML feedback loop).

5. **Where is the bottleneck right now?** Candidates: upload and ingestion latency, indexing turnaround, retrieval quality on long-tail queries, labeling throughput, inter-rater quality, ML feedback loop, safety-critical event SLA. Travis likely has a strong opinion on which one is acute.

6. **How does the triage function relate to disengagement and incident review?** Some shops run these as separate workflows with separate tooling. Others unify them.

7. **What is the relationship between fleet data and Arene-equipped production vehicle data?** If Arene is starting to flow data from consumer RAV4 and successor vehicles, the scale and governance questions change dramatically.

8. **What is the model-development feedback loop cadence?** How long from a real-world event to a retrained model deployed on fleet. This frames where in the pipeline the pain is felt.

9. **What are the known failure modes in the current triage operation?** Volume versus quality, inter-rater drift, missed edge cases, ingestion slippage, ops-ML signal loss. Travis will likely frame these in his own language, and mapping his framing to this document's taxonomy is useful prep.

10. **Where does Technical Operations Engineering want outside help?** Which of these are Woven-internal engineering builds versus candidates for BayOne-style managed services or consulting engagement. This is ultimately the discovery question.

---

## Sources

Sensor data and volumes:

- https://www.tuxera.com/blog/autonomous-and-adas-test-cars-produce-over-11-tb-of-data-per-day/
- https://www.tuxera.com/blog/autonomous-cars-300-tb-of-data-per-year/
- https://medium.com/@autodriveai/autonomous-cars-will-collect-approximately-4-tb-of-data-every-hour-of-driving-3819aba33204
- https://blogs.sw.siemens.com/polarion/the-data-deluge-what-do-we-do-with-the-data-generated-by-avs/
- https://www.ni.com/en/solutions/transportation/adas-and-autonomous-driving-testing/adas-and-autonomous-driving-validation/adas-datalogger.html
- https://premioinc.com/pages/autonomous-vehicle-data-storage
- https://semiconductor.samsung.com/news-events/tech-blog/autonomous-driving-and-the-modern-data-center/
- https://labelyourdata.com/articles/autonomous-vehicle-data-collection
- https://roboticsandautomationnews.com/2026/01/29/the-sensor-suite-for-autonomous-vehicles-lidar-radar-cameras-and-sensor-fusion/98371/
- https://www.mobileye.com/blog/radar-lidar-next-generation-active-sensors/
- https://www.valeo.com/en/valeo-scala-lidar/
- https://www.asapdrew.com/p/lidar-2025-level-4-autonomous-vehicles-analysis
- https://www.cepton.com/driving-lidar/reading-lidar-specs-part-ii-why-they-matter-for-lidar-applications
- https://www.aeva.com/
- https://www.thinkautonomous.ai/blog/fmcw-lidars-vs-imaging-radars/
- https://www.mdpi.com/1424-8220/24/10/3185
- https://insidegnss.com/synchronizing-mems-imus-with-gps-in-autonomous-vehicles/
- https://arxiv.org/html/2510.08880
- https://www.csselectronics.com/pages/can-bus-simple-intro-tutorial
- https://industrial.panasonic.com/ww/ds/ss/technical/ap2

Log formats and ingestion:

- https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format
- https://mcap.dev/guides/getting-started/ros-2
- https://arxiv.org/html/2511.19453v1
- https://www.netapp.com/blog/how-to-build-a-data-pipeline-for-autonomous-driving/
- https://dxc.com/us/en/insights/perspectives/blogs/ensuring-effective-autonomous-vehicle-data-ingestion

Triage, curation, edge case mining:

- https://www.appliedintuition.com/use-cases/log-visualization-and-triage
- https://www.appliedintuition.com/blog/av-development-4-triage-considerations
- https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets
- https://foxglove.dev/product
- https://foxglove.dev/robotics/data-management-tools-for-robotics-a-2025-guide-comparison
- https://roboticsandautomationnews.com/2026/04/22/foxglove-launches-unified-data-platform-to-accelerate-physical-ai-development/100847/
- https://aws.amazon.com/blogs/industries/building-an-end-to-end-physical-ai-data-pipeline-for-autonomous-vehicle-3-0-on-aws-with-nvidia/
- https://aws.amazon.com/blogs/industries/multi-agent-ai-solution-for-vehicle-fleet-data-discovery-and-edge-case-classification/
- https://arxiv.org/html/2410.08491v1
- https://www.kognic.com/articles/edge-case-detection-for-autonomous-driving-methods-and-workflowsedge-case-detection-autonomous-driving
- https://www.kognic.com/articles/edge-cases-autonomous-driving
- https://www.mdpi.com/1424-8220/24/1/108
- https://imerit.net/resources/blog/autonomous-vehicle-edge-cases-avi-sol/
- https://www.techbrew.com/stories/2026/02/05/autonomous-vehicles-edge-cases
- https://arxiv.org/html/2403.17373v1
- https://arxiv.org/html/2508.18397v2
- https://encord.com/blog/human-in-the-loop-autonomous-vehicles/
- https://objectways.com/blog/improving-inter-rater-reliability-for-data-annotation-and-labeling/
- https://www.ultralytics.com/blog/inter-rater-reliability
- https://link.springer.com/article/10.1186/s40537-024-00976-9
- https://arxiv.org/html/2401.01454v2

Disengagement and safety:

- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0168054
- https://www.nature.com/articles/s41597-021-01083-7
- https://www.sciencedirect.com/science/article/pii/S2095809924000274
- https://arxiv.org/pdf/2305.12665
- https://www.transportation.gov/sites/dot.gov/files/2024-08/HASS_COE_Understanding_Safety_Challenges_of_Vehicles_Equipped_with_ADS_Aug2024.pdf

AV developer material:

- https://waymo.com/open/
- https://waymo.com/blog/2020/04/using-automated-data-augmentation-to/
- https://github.com/waymo-research/waymo-open-dataset/blob/master/docs/labeling_specifications.md
- https://arxiv.org/pdf/2103.05073
- https://arxiv.org/html/2510.26125v1
- https://exchange.scale.com/public/blogs/how-ml-waymo-building-scalable-autonomous-driver-dmitri-dolgov
- https://wayve.ai/technology/
- https://wayve.ai/technology/av2-0/
- https://wayve.ai/thinking/gaia-3/
- https://wayve.ai/thinking/scaling-gaia-1/
- https://wayve.ai/thinking/scaling-embodied-ai-for-autonomous-driving-with-microsoft-azure/
- https://www.zenml.io/llmops-database/end-to-end-foundation-models-for-self-driving-vehicles-at-scale
- https://www.mobileye.com/technology/rem/
- https://www.mobileye.com/blog/rem-mapping-avs/
- https://aws.amazon.com/blogs/machine-learning/optimizing-mobileyes-rem-with-aws-graviton-a-focus-on-ml-inference-and-triton-integration/
- https://www.amazon.science/blog/scenario-diffusion-helps-zoox-vehicles-navigate-safety-critical-situations

Woven by Toyota specific:

- https://www.woven.toyota/en/
- https://woven.toyota/en/technology/automated-driving/
- https://woven.toyota/en/our-latest/20220407/
- https://www.woven.toyota/en/news/20211119/
- https://woven.toyota/en/our-latest/20211119/
- https://woven.toyota/en/our-latest/20220927/
- https://woven.toyota/en/our-latest/20220127/
- https://woven.toyota/en/arene/
- https://www.woven.toyota/en/technology/arene/
- https://woven.toyota/en/our-latest/20250521/
- https://global.toyota/en/newsroom/corporate/39070846.html
- https://en.wikipedia.org/wiki/Woven_by_Toyota,_Inc.
- https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai
- https://www.microsoft.com/en/customers/story/24108-woven-by-toyota-inc-azure-openai
- https://woven.vc/
