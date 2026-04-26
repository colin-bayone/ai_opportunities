# 06 - Call Prep: Technical Reference

**Source:** Engagement research library (Sets 01, 04, 05)
**Source Date:** 2026-04-23 (prepared immediately before discovery call)
**Document Set:** 06 (Call Prep for Travis Millet Discovery Call)
**Pass:** Technical context Colin walks in with

---

## Woven's Existing Technical Stack (What Colin Is Not Replacing)

Walking in, Colin should treat the following as given, not as gaps:

- **AutoTriage.** Woven's in-house GenAI plus human-in-the-loop system that absorbs approximately 50 percent of ADAS triage volume at 80 percent accuracy. Public face: Suigen Koide (Head of DevBoost, GenAI, MLOps). This is the ML platform system, owned by a different team than Travis's.
- **Union.ai.** Managed Flyte for orchestration across petabytes of sensor data. Public case study cites 20x faster ML iteration and $1M plus annual savings.
- **Encord.** Publicly disclosed annotation partner.
- **Internal tooling.** Dedicated Data Annotation and Labeling Engineering team per public job postings. Woven builds significant internal infrastructure.
- **Applied Intuition.** Simulation partner, lists Toyota as a customer.

The implication: walking in with a pitch that BayOne will set up labeling infrastructure misses the mark. Woven already has it. BayOne's credibility depends on understanding what they already have and offering something that layers on it or operates adjacent to it.

## AV Sensor Data and Production Triage Workflow (Reference)

Typical AV test and production vehicles collect:

- Cameras (RGB, near-IR, surround view) at high frame rates and resolutions
- LiDAR (mechanical spinning, solid state, or FMCW) with dense point clouds
- Radar (short range, long range, imaging radar)
- IMU, GPS, wheel odometry, steering angle, throttle and brake signals
- Vehicle CAN bus signals

Typical data volumes at Level 4 test fleet scale are roughly 4 to 8 TB per vehicle per hour. Production fleets (Arene-equipped RAV4s) change the shape of the problem because the number of vehicles and the data firehose multiply.

Triage activities typically include:

- Event identification and scenario tagging
- Edge case mining (finding rare or valuable situations in collected data)
- Anomaly detection (unusual sensor behavior, vehicle behavior, or traffic events)
- Disengagement review and safety-critical event analysis
- Routing to the correct engineering team (perception, prediction, planner, controls)
- Prioritizing which cases go to humans and which can be handled by automated systems

## The Acceleration vs Capacity Binary

This is the single most important framing for Colin on the call. It replaces prior speculation about labeling vs correlation vs root cause.

**Acceleration:** Travis wants to make his team's work faster through AI and automation. Volume is going up. His workforce cannot scale linearly. He wants tooling, instrumentation, or custom AI systems that let his existing team handle more throughput at the same or better quality. This is a Colin conversation. BayOne could propose custom engineering work.

**Capacity:** Travis wants more humans doing the work as it is done today. He has volume he cannot absorb. He wants more labelers, period. This is not a Colin conversation. Jesse and Pratik handle it through contingent workforce or staffing terms.

The signal distinguishing the two is in how Travis talks about the pain. If he talks about per-hour throughput, per-labeler SLAs, headcount math, the shape is capacity. If he talks about quality inconsistency, rework, slow onboarding, gaps between automated and human output, or feedback loops to the ML platform team, the shape leans acceleration.

## Candidate Acceleration Solutions (For Colin's Reference If Travis Volunteers Related Pain)

These are not problems BayOne introduces. They are shapes Colin can recognize if Travis surfaces related pain organically. Each is a legitimate custom engineering solution that would sit in Travis's operational mandate.

### Faster onboarding and consistency for new triagers

If Travis mentions long ramp times or inter-labeler drift during onboarding, the solution shape is training instrumentation, adaptive onboarding datasets, and consistency measurement across new hires.

### QA tooling across multiple workforces

If Travis uses a mix of internal labelers, Encord-provided labelers, and contractors, inter-rater reliability across groups is a real problem. Solution shape is golden-set QA, adjudication routing, measurement across vendors, and active quality monitoring.

### Feedback loops between workforce and AutoTriage

If Travis mentions cases where AutoTriage gets something wrong and his humans correct it, the feedback pathway to Suigen's team may be informal or slow. Solution shape is structured feedback instrumentation, correction capture, and error-pattern analysis that benefits both sides.

### Edit-distance telemetry on pre-labels

If his workforce reviews and edits AutoTriage pre-labels, measuring how often they accept as-is, minor-edit, or fully redo tells you both the model quality and the reviewer calibration. Solution shape is instrumentation layer over the existing pipeline.

### Ontology migration tooling

If Travis mentions taxonomy changes or schema updates, the cost of re-labeling historical data is large. Solution shape is migration tooling that identifies minimal re-work footprint and queues residuals to humans.

### Active learning control plane

If Travis talks about deciding what to label next or prioritizing work against a finite human budget, there is a real engineering problem in the decision logic. Solution shape is an active learning harness tied to Woven's specific models that selects samples for human review based on model uncertainty, disagreement, and strategic data gaps.

## Foundation Model and Auto-Labeling Context (2026 State)

In 2026, model-assisted labeling is standard practice. The relevant tools and approaches:

- **SAM 2 and SAM 2.1.** Segment Anything Model 2, widely adopted for pre-labeling with reported speedup factors around 8x.
- **GroundingDINO 1.5 and OWLv2.** Open-vocabulary detection models usable for pre-detection in novel taxonomies.
- **DINOv2 and DINOv3.** Self-supervised vision foundation models for embedding-based scene retrieval and edge case mining.
- **Multimodal large language models (MLLMs).** Applied to scene understanding, attribute extraction, and caption-driven retrieval.
- **Active learning.** Least-confidence, entropy, margin sampling, Bayesian ensemble disagreement. NVIDIA has published A/B results showing 3x to 4.4x efficiency gains with well-designed acquisition functions.
- **Semi-supervised and auto-labeling.** Tesla, Waymo, and Motional have publicly described self-training and pseudo-labeling pipelines. Fails in specific ways on long-tail, domain shift, calibration drift, and amodal 3D.

Colin does not need to lecture Travis on any of this. It is reference material for speaking credibly if Travis probes on what BayOne knows.

## BayOne Engagement Shapes (Reference, Not to Pitch)

The three BayOne models Colin introduced in Set 01 and Pratik extended:

- **Model 1. Full managed solutions.** 100 percent BayOne execution. Outcome-based pricing. Client does not see headcount. Analog: Lam Research.
- **Model 2. Hybrid collaboration.** Variable split (commonly 70/30, but client-selectable: 100/0, 75/25, 50/50, 25/75, 0/100). Team may be BayOne staffing placements or existing client engineers. Daily direction from the client, intermingling with BayOne.
- **Model 3. Pure staffing.** Time and materials. BayOne not in the loop on execution. Appropriate when the client has strong internal AI leadership.

These are not for Colin to pitch on the call. They are for when a second conversation happens after discovery.

## AV Data Tooling Landscape Context

- **Scale AI.** Under regulatory and confidentiality pressure after Meta took approximately 49 percent stake for $14.3B in June 2025. Major AV customers (Google, OpenAI, xAI) reduced engagement. Scale cut 200 staff and 500 contractors. Woven may have reasons to be cautious about Scale.
- **Encord.** Closed $60M Series C February 2026. Publicly lists Woven as a customer.
- **Applied Intuition.** $600M Series F. Lists Toyota as a customer.
- **Aquarium Learning.** Acquired by Notion October 2024, exited the AV category.
- **Segments.ai.** Acquired by Uber October 2025.

Colin does not need to raise competitor vendors. This is context for understanding what Travis may be evaluating or has evaluated.

## Diagnostic Questions for the Call

These are questions Colin can ask after Travis frames the problem. Not to use opening a pitch. Used to probe into whether acceleration or capacity is the shape.

### On the workforce

- Walk me through what a typical week looks like for the people on this team. What are they actually spending time on?
- Where does your existing team spend time that feels like rework or wasted effort?
- What is the hardest part of getting a new person productive on this work?
- How do you measure quality on the output of this team today?

### On the interface with AutoTriage (if Travis references it)

- How does work flow between your team and the AutoTriage team today?
- When AutoTriage misses something or gets something wrong, how does that feedback get back?
- Where does your team add value that AutoTriage cannot?

### On the nature of the work

- What is the deliverable at the end of a typical case that your team handles?
- What do you count? Frames labeled, cases closed, hours billed?
- What would make your team twice as productive, if you could choose one thing?

### On the SOW

- What specifically are the three to four people going to do?
- Is this replacing capacity you have lost, handling new volume, or doing something different?
- Is the work tied to a specific release, a specific model, or a specific operational goal?

## What Not to Do

- Do not open with BayOne capabilities.
- Do not bring up specific vendor names or tools unless Travis does first.
- Do not describe the five-point AI-generated playbook from the pre-call prep email. None of it.
- Do not cite "modeling road event distributions, developing evaluation frameworks for AD and ADAS deployment readiness, and assessing ML training data strategy." That framing was generated, not researched against this conversation, and it will sound hollow.
- Do not attempt to correct John Lim's employer on the call if it comes up. Hold internally.
- Do not pitch the three engagement models framework on the call. Not this call. Not yet.
- Do not bring up Arene, Woven City, or the April 22 announcement unless Travis does first. If Travis references them, Colin can engage with minimal technical depth and pivot back to the problem Travis is framing.
