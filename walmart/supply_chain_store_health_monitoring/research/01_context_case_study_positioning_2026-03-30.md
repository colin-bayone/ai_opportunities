# 01 - Context Build: Case Study Positioning

**Source:** /walmart/supply_chain_store_health_monitoring/source/kanchan_claude.txt, kanchan_walmart_tracker.md, walmart_discovery_call_prep.md
**Source Date:** 2026-03-30 (Pre-engagement context build from Colin's working session)
**Document Set:** 01 (Pre-Engagement Context Build)
**Pass:** Focused deep dive on Coherent Multimodal SFT case study and positioning strategy

---

## 1. What the Case Study Is

### Origin and Ownership

The Multimodal SFT for Field-Support Visual Assistant is a real project that Colin Moore led and executed during his time at Coherent Corp (also known as Coherent/II-VI). It is not a BayOne Solutions product, deliverable, demo, or offering. It is a case study from Colin's prior professional work. This distinction is the single most important positioning constraint for this engagement and is addressed in detail throughout this document.

### The Business Problem

Coherent Corp operates a global field service organization supporting more than 8,000 complex industrial laser systems deployed across clients in 40+ countries. The operational pressures were severe:

- **Downtime cost approximately $12,000 per hour** for affected client operations
- On-site expert dispatches were expensive, slow, and introduced safety risks
- The global scale (40+ countries) meant language barriers, varying levels of local technician expertise, and logistics complexity for expert travel
- There was strong demand from the field for faster on-site fault diagnosis and guided resolution to maximize safety and minimize machine downtime

The core need was getting field technicians to the correct diagnosis and repair path faster, without requiring an expert dispatch for every complex fault.

### What Was Built

A supervised fine-tuning (SFT) pipeline applied to a vision-language model, trained on aligned image and text data consisting of fault photographs, system schematics, and repair step documentation. The system was designed for real-world field use by technicians who are not machine learning specialists.

**Data pipeline and infrastructure:**
- Azure AI data pipeline for ingestion, labeling, augmentation, model training, and secure model registry
- Multilingual output capability (English, German, Mandarin) via Azure Translator, integrated at both label creation and inference time
- PII and sensitive design redaction built into the pipeline
- Laser-classification safety tags applied to all outputs
- Full audit trail for regulatory compliance
- Post-deployment MLOps workflow with drift detection and periodic SFT refreshes from new field images every two weeks

**Model architecture and training:**
- 75,000 curated image-text pairs plus 25,000 augmented variants (100,000 total training samples)
- Data augmentation included rotation, occlusion, and brightness shifts to simulate real field conditions
- LoRA (Low-Rank Adaptation) adapters added on the text decoder head; vision backbone was frozen
- SFT strategy: freeze vision encoder, apply LoRA on text decoder, use mixed-language captions aligned with Azure Translator
- Weekly incremental SFT retrain cycles; model registry tracked full lineage, metrics, and rollback points
- Synthetic negative set (unrelated images) used to enforce a refusal policy when a technician submits an irrelevant photo
- 10,000 validation samples and 10,000 test samples held out from training

**The field workflow (tablet-based):**
1. Field technician encounters a fault and takes a photo using a tablet
2. The model returns the top-3 ranked fault diagnoses plus a safety-checked repair checklist for each
3. The technician reviews, selects the correct diagnosis, and follows the repair steps
4. Each confirmed repair pushes the annotated image-text pair back into the training set
5. An auto-curation bot scores label quality nightly on all new submissions

This feedback loop is a critical design feature. The system improves continuously from real field usage without requiring manual data curation for every new sample.

### Program Execution

- **Duration:** 15-week program
- **Team size:** 12-person squad aided by the Coherent client team
- This was not an experiment or a proof of concept. It was a production deployment with a defined timeline, a staffed team, and measurable deliverables.

---

## 2. Complete Results and Metrics

### Operational Impact

| Metric | Result |
|--------|--------|
| Ticket resolution time | 50-60% reduction |
| First-pass fix rate | Improved from 71% to 91% (+28 percentage points) |
| Expert call-outs and travel costs | 50% reduction |
| Safety-procedure deviations | 15% reduction (via checklist prompts) |
| Field technician CSAT | +6 points |
| SLA penalty reduction | Approximately $3.2 million annually |

### Technical Performance

| Metric | Result |
|--------|--------|
| Top-1 fault-classification accuracy | 93% on held-out test photos |
| SME blind review usefulness score | 4.7 out of 5 on generated repair guidance |
| Toxic/unsafe prompt check pass rate | Greater than 98% |
| p99 inference latency | Sub-2 seconds on standard F-series Azure GPUs |
| Offline capability | Edge-cache deployment for offline regions |
| Per-inference cost | $0.04 average |
| Cost recovery break-even | 3 months from deployment (build and labeling costs) |

The $3.2M SLA penalty reduction is the headline number for executive conversations. The first-pass fix rate improvement (71% to 91%) is the headline number for operational conversations. The sub-2s latency and $0.04 per-inference cost address the "is this practical at scale" question before it is asked.

---

## 3. Full Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Vision pre-processing | Azure AI Vision | Object detection, image quality checks on inbound photos |
| Model training and deployment | Azure Machine Learning | SFT runs, hyperparameter sweeps, managed inference endpoints |
| Data storage | Azure Blob Storage and Data Lake | Images, labels, model artifacts with RBAC/SAS security |
| CI/CD | Azure DevOps + GitHub Actions | Gated promotion pipeline (dev to QA/testing to production) |
| Monitoring and observability | Power BI dashboards | Live accuracy, latency, and drift alert dashboards |
| Translation | Azure Translator | Multilingual label creation and inference output |
| Compute | F-series Azure GPUs | Standard inference compute; edge-cache for offline regions |

The stack is entirely Azure-native, which matters for enterprise conversations. It signals that this was built within a governed cloud environment with proper security, RBAC, and compliance controls, not a research notebook running on a personal GPU.

---

## 4. How Kanchan Positioned It to Troy

### What She Said (Verbal Only)

Kanchan told Troy Ward verbally that BayOne has experience with multimodal AI and supervised fine-tuned models for predictive diagnostics. She connected his stated interest in proactive health monitoring of in-store systems to this case study context. She told him "we can talk more deeply about how we did all of this."

### What She Did NOT Do

- She did not send Troy any materials, decks, slides, or written descriptions
- She did not mention providing a demo
- She did not frame it as a product or an off-the-shelf solution
- She did not send the case study document itself

### Why This Matters

Kanchan's handling was actually correct. She positioned it as experience and offered a deeper conversation, which is exactly the right framing. Nothing needs to be walked back. Nothing was overpromised. Troy is likely expecting a conversation about BayOne's experience with predictive diagnostics, not a product demo or capability showcase. The misleading meeting title ("Showcasing BayOne's AI Capabilities") does not match what Kanchan actually communicated to Troy.

### The Echo Problem (Question 2)

There is one notable issue in how the information surfaced. Colin asked Kanchan five specific questions to prepare for the call. Question 2 was: "What conversations have already happened and what expectations have been set?" Kanchan's answer to this question was the Multimodal SFT case study that Colin himself had just mentioned to her moments earlier. She echoed his words back as if they were her prep work. This was not an answer to the question asked. It is unclear whether Kanchan relayed the case study to Troy in real time after Colin mentioned it, or whether she had any prior context about the case study before Colin brought it up.

This does not change the fact that her verbal positioning to Troy was appropriate. But it highlights that the depth of her understanding of the case study is likely shallow, having come from Colin's own mention of it rather than from independent study.

---

## 5. Colin's Guidance on Positioning

### The Core Constraint

Colin was explicit and direct: the Multimodal SFT case study is from his time at Coherent. It cannot be presented as a product that BayOne has or a solution that BayOne can demo. It is not a ready-made, off-the-shelf thing. Colin can talk about it deeply because he led the work. But it must be framed as relevant experience and expertise, not as something BayOne is coming in to demo or sell.

### What Colin Asked Kanchan to Confirm

After learning that Kanchan had mentioned the case study to Troy, Colin asked her directly: "How was that positioned to him? That's from my work at Coherent, so I can speak to it deeply, but it is not a product or solution that BayOne offers off the shelf. I just want to make sure it was framed as relevant experience and not something we're coming in to demo or sell."

This was not a correction. It was a confirmation request. Colin's tone was firm but not punitive. He wanted to know if there was a problem to fix before the call, not to chastise Kanchan.

### Kanchan's Confirmation

Kanchan confirmed that she did not send materials, did not mention a demo, and positioned it as experience with an offer for deeper conversation. This satisfied Colin's concern. No walkback was needed.

### Why the Positioning Constraint Exists

This is not a legal issue. It is a credibility issue. If BayOne presents Colin's Coherent work as a BayOne product and Troy (or anyone at Walmart) later discovers that it was built at a different company, BayOne's credibility is destroyed. The correct framing is: "Our Director of AI led exactly this type of work at his prior organization. He has deep hands-on experience building these systems. That expertise is what he brings to BayOne, and it is why we can credibly scope, architect, and deliver this kind of solution." This is the truth. It is also a stronger positioning than pretending BayOne has a product, because it signals that the person they would be working with has actually done this, not that a company has a slide deck about it.

### Context: The Amit Problem (Round 1)

The positioning constraint has additional weight because of what happened in Round 1 of Walmart engagement. Amit (VP of Delivery) had previously sent a deck to a different Walmart contact that positioned BayOne as having pre-built AI accelerators, chatbot demos, agent-based solutions, and a potential standalone product. None of this existed. Colin suspects Amit confused Colin's prior-org case studies with BayOne's actual capabilities. This Round 1 situation created misaligned expectations with Walmart that have never been formally walked back. Colin explicitly named this as the probable cause: "Amit may have confused case studies from real work that I have done at my prior org with demo-able work that BayOne can realistically claim."

The positioning discipline on the Multimodal SFT case study is therefore not just good practice. It is a direct response to a known pattern of capability misrepresentation that has already burned this client relationship once.

---

## 6. How the Case Study Maps to Walmart's Problem

### The Problem Statement from Troy (via Kanchan)

Troy Ward's primary challenge is establishing effective health checks and early diagnostic capabilities for in-store machines, allowing issues to be identified and resolved before they impact store performance. His team oversees:

- POS (checkout systems)
- Self-checkout machines
- Payment systems
- Store networks and connectivity
- Devices used by associates (handhelds, scanners)
- IoT and store infrastructure

His articulated AI interests are: predicting outages before they happen, and real-time monitoring of all store tech systems.

### Where the Analogy Holds

The core pattern is identical:

| Dimension | Coherent | Walmart |
|-----------|----------|---------|
| Environment | 8,000+ industrial laser systems across 40+ countries | Thousands of stores with POS, self-checkout, payment, network, IoT, and associate devices |
| Pain | Downtime at $12K/hr, slow expert dispatch, safety risk | Store tech failures impacting store performance, likely costing significant revenue per incident |
| Need | Faster on-site fault diagnosis and guided resolution | Health checks and early diagnostics before issues impact operations |
| User | Field service technician at the equipment | Likely a store tech or IT support person at the machine |
| Pattern | Tech encounters fault, needs diagnosis and repair path | Tech or system detects anomaly, needs diagnosis and resolution path |

The fundamental architecture is the same: ingest signals from equipment, detect or predict faults, surface actionable guidance to the person responsible for resolution, and measure impact on resolution time, first-pass fix rates, and cost.

### Where the Analogy Breaks Down or Needs Qualification

**Domain specificity.** Coherent was industrial laser systems. Walmart is retail store infrastructure. The machine types, failure modes, telemetry formats, resolution workflows, and regulatory environments are entirely different. Any solution for Walmart would need to be built on Walmart's data, trained on Walmart's failure patterns, and integrated into Walmart's operational workflows. Nothing from Coherent transfers directly at the implementation level.

**Visual vs. telemetry.** The Coherent solution was fundamentally visual: a technician snaps a photo of a fault and the model diagnoses from the image. Walmart's problem may or may not have a visual component. Store tech issues might be better diagnosed from telemetry data (logs, error codes, heartbeat signals, SNMP) rather than from photographs. Discovery needs to determine whether the visual assistant pattern applies at all, or whether this is more of an anomaly detection and predictive maintenance problem on structured data streams.

**Resolution path.** At Coherent, the field technician was physically present at the equipment and was the person resolving the issue. The model provided diagnosis and a repair checklist, and the tech executed it on the spot. At Walmart, the resolution path is unknown. If the system predicts that a self-checkout unit is going to fail, what happens next? Is there a tech in the store? Is someone dispatched from a regional hub? Is there a remote fix? Is there a parts replacement chain? Predicting an outage is only half the problem. If the prediction does not connect to a clear resolution action (dispatch a tech, trigger a remote restart, swap a part), the value proposition changes significantly. Colin specifically flagged this as a critical discovery question.

**Data maturity.** At Coherent, there was enough existing data (fault photos, schematics, repair documentation) to curate 75,000 image-text training pairs. Walmart's data environment is unknown. If Troy's team has rich telemetry and logs flowing from store systems, the AI conversation is real. If the environment is reactive and manual, with no telemetry until something breaks and a ticket gets filed, then the first problem is instrumentation and data infrastructure, not AI. Being honest about this distinction is critical to credibility.

**Scale and infrastructure.** Walmart's scale is orders of magnitude larger than a single manufacturer's field service org. The solution architecture, cost model, and operational considerations at Walmart's scale would be materially different even if the pattern is the same.

---

## 7. The Competitive Angle

Colin identified a key competitive concern: Troy's team manages store technology infrastructure, and there are massive vendors already in the POS, self-checkout, payment, network monitoring, and IoT space with turnkey solutions. Walmart almost certainly already has relationships with those vendors. The question is where BayOne adds value that an off-the-shelf vendor does not.

### Where Off-the-Shelf Falls Short

Predictive models for a specific environment like Walmart's store infrastructure would need to be trained on their data, their failure patterns, and their system configurations. That is not something you buy from a vendor. That is something you build. Generic monitoring platforms (Datadog, Splunk, etc.) can detect when something is already broken. Predicting failures before they happen, diagnosing root causes from multimodal signals, and surfacing actionable repair guidance requires custom model development on proprietary data.

### The Build Argument

This type of work, supervised fine-tuning on domain-specific data, custom data pipelines, MLOps workflows with continuous learning, requires someone who has actually done it. It is not something that can be purchased as a SaaS product. The Coherent case study demonstrates that Colin has built exactly this class of system end-to-end, from data curation through production deployment, with measurable results. That is the differentiator: not a product, but proven capability to build the right thing.

### What Discovery Needs to Determine

- Whether Troy is shopping for a turnkey platform or looking for help building something custom
- Whether there is an existing monitoring platform in place that is falling short, or whether they are starting from scratch
- Whether there is an internal data science or ML team involved, or whether this would be fully external
- What health data these machines already produce (telemetry, logs, error codes, heartbeat signals) or whether it is a reactive, ticket-based environment

If Troy is looking for a ready-made platform, BayOne is not the right fit, and it is better to know that early than to waste anyone's time. If Troy needs something built, BayOne's positioning through Colin's demonstrated experience is strong.

---

## 8. How to Use This Case Study on the Call

### The Opening (Colin's Planned Approach)

Colin planned to lead with the Coherent experience as a credibility builder in approximately 60 seconds. The framing from the discovery call prep document:

"My background is in AI and ML at the enterprise level. Before BayOne I led work at Coherent, a global manufacturing company, where we built AI solutions for field service and operations. One of the bigger ones was a predictive diagnostics system for industrial equipment across 40+ countries. Techs in the field could diagnose faults faster, we cut resolution time in half, and we significantly reduced unnecessary expert dispatches. I mention that because when I heard about your interest in health checks and early diagnostics for in-store machines, it felt like a very similar pattern. Different domain, but the same core problem."

This framing is precise. It says "before BayOne" (establishes it as prior work). It says "I led work" (personal credibility). It describes results without naming products. It draws the pattern connection explicitly. And it hands the conversation to Troy.

### When to Go Deeper

The discovery call prep identifies a specific trigger: "If the conversation naturally connects to the visual assistant / field support angle, then bring the Coherent case study into more detail. Tech snaps a photo, model diagnoses the issue, returns a repair checklist. If his techs are troubleshooting hardware in stores, this is directly relevant."

The case study should not be presented unprompted in full detail. It should be deepened only if Troy's description of his environment makes the connection obvious and natural.

### What NOT to Do

- Do not present it as a BayOne product or demo
- Do not offer to show Troy the system (it is Coherent's, not BayOne's)
- Do not claim BayOne has retail-specific experience (the pattern transfers, the domain does not)
- Do not lead with metrics unless Troy asks for specifics (save detailed numbers for a follow-up if the conversation warrants it)

---

## 9. Kanchan's Performance and Credit

Despite the communication gaps and the misleading meeting title (which was her doing), Kanchan was the only person from the sales side who responded to Colin's requests for information before the call. Colin also messaged Richa, who did not respond. Kanchan provided answers to all five of Colin's pre-call questions, clarified what she had said to Troy, and confirmed the positioning of the case study when asked.

Her instincts on connecting Troy's use case to the multimodal SFT experience were correct. Her verbal-only, experience-framed positioning to Troy was exactly right. Colin acknowledged this explicitly and directed that she be thanked warmly and given credit for stepping up.

Colin's message to Kanchan after her clarification was warm and encouraging, acknowledged that she was the only one who responded, validated that her instincts were right, and proactively flagged the capacity concern (that BayOne's team is currently stretched and cannot take on immediate new work) so she would not be caught off guard. He positioned the capacity issue as a leadership problem he has been pushing on, not as her fault.

---

## 10. Summary of Positioning Rules

For any future use of this case study in the Walmart engagement or any other context:

1. **Always attribute to Colin's prior work at Coherent.** Never imply it is BayOne's product or deliverable.
2. **Frame as experience and expertise.** "Colin built this" not "BayOne has this."
3. **Never offer a demo.** The system belongs to Coherent. There is nothing to demo.
4. **Never send the case study document to a prospect without Colin's review and approval.** The document exists for internal reference and credibility building, not for distribution.
5. **Draw the pattern, not the product.** The value is that the same class of problem (field diagnostics, predictive maintenance, multimodal AI for hardware troubleshooting) has been solved before at scale. The value is not a specific software system that can be redeployed.
6. **Be honest about domain differences.** The pattern transfers. The implementation does not. Any solution for Walmart would be built from scratch on Walmart's data and in Walmart's environment.
7. **Use results as proof of competence, not as promises.** The 50-60% reduction in resolution time at Coherent demonstrates what is possible, not what will happen at Walmart. Results at Walmart would depend entirely on Walmart's data, environment, and problem specifics.
