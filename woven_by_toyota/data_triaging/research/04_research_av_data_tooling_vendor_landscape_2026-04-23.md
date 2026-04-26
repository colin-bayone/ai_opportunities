# 04 - Research: AV Data Tooling and Vendor Landscape

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** Competitive tooling landscape for AV data triaging and labeling

---

## Executive Summary

The autonomous vehicle data tooling market is mid-consolidation. Three structural dynamics matter most for a Woven discovery call:

1. **Woven already appears to have significant off-the-shelf tooling in place.** Encord publicly names Woven by Toyota as a customer on its platform and in its AV marketing. Woven also migrated its ML orchestration to Union.ai (managed Flyte) by 2023, and maintains internal labeling-suite backend engineering teams. Colin should assume Travis is evaluating tools against an already-layered stack, not starting from zero.
2. **The vendor landscape is shrinking via acquisition.** Aquarium Learning was acquired by Notion in October 2024 and is no longer positioned for AV. Segments.ai was acquired by Uber in October 2025. Applied Intuition continues to expand into data management and log-based workflows, and Scale AI had a customer-trust disruption after Meta took a 49 percent stake in June 2025 that drove Google, OpenAI, and xAI to reduce engagements. Automotive buyers are watching these moves carefully because of data-confidentiality implications.
3. **Tools are converging on a similar feature set** (multimodal ingest, model-assisted labeling, data curation, embedding search, active learning loops). The differentiation has moved to 3D and multi-sensor depth, QA workflows, on-prem and air-gapped deployment, and service-inclusive delivery models. This is where custom engagement oxygen still exists.

Colin's posture for the call: BayOne does not need to displace any vendor. The question is what Woven still does not get from its existing stack, and where bespoke engineering, integration, or ML engineering capacity is the remaining gap.

---

## 1. Scale AI

### Offering for AV

Scale runs three primary offerings relevant to AV: the **Data Engine** (service-inclusive labeling of camera, LiDAR, and radar), **Scale Rapid** (self-serve labeling via Scale's workforce), **Scale Studio** (bring-your-own workforce on Scale's platform), and **Scale Nucleus** (dataset management, visualization, curation, and model-prediction diffing, originally launched August 2020). The **Automotive Foundation Model (AFM-1)**, introduced December 2023, runs inside Nucleus and produces pre-labels and autolabels for 2D image tasks across detection, semantic segmentation, instance segmentation, and panoptic segmentation. Scale acquired SiaSearch in 2021 to add Tesla-style data engine search capabilities.

### Public AV References

Cruise (GM, now wound down), Zoox, Nuro, and Toyota are on Scale's public automotive customer list. Scale's automotive site emphasizes OEM and tier-one partnerships.

### Pricing Posture

Custom enterprise contracts only, with no published price list. Per Vendr aggregation, average annual spend is approximately 93,000 dollars with deals exceeding 400,000 dollars. Per-annotation ranges cited publicly: approximately 0.03 to 1.00 dollars per 2D bounding box, and 0.05 to 3.00 dollars per semantic mask, with 3D and sensor fusion higher. These are benchmarks from secondary sources, not official Scale pricing.

### Build vs Buy Positioning

Scale positions as a full-service data engine that replaces in-house labeling infrastructure. The pitch is scale of workforce plus platform plus foundation models.

### Known Gaps and Sensitivities

The Meta investment in June 2025 introduced a data-confidentiality concern for customers who view Meta as a competitor or risk. Google, OpenAI, and xAI publicly reduced spend. Automotive OEMs with proprietary driving data may share this concern. Scale also laid off 14 percent of staff and cut 500 contractors shortly after the deal. AFM-1 is 2D image only; 3D LiDAR autolabeling is not the headline capability.

Sources: [Scale Automotive](https://scale.com/automotive), [AFM-1 introduction](https://scale.com/blog/afm1) (marketing), [Vendr pricing](https://www.vendr.com/buyer-guides/scale-ai) (independent), [Scale on customer trust after Meta](https://scale.com/blog/customer-trust-scale-meta-deal) (marketing), [Just Think AI on Meta-Scale cracks](https://www.justthink.ai/blog/meta-scale-ai-cracks-emerge-in-their-partnership) (independent commentary), [TechCrunch on SiaSearch acquisition](https://techcrunch.com/2021/11/03/scale-ai-acquires-siasearch-to-give-companies-the-same-data-engine-superpowers-that-tesla-has/).

---

## 2. Labelbox

### Offering for AV

General-purpose multimodal annotation platform with a growing 3D toolkit. Strengths are dataset management, workflow automation, and Model Foundry for model-assisted labeling and evaluation. Supports LiDAR 3D bounding boxes, but independent reviewers characterize the 3D engine as less specialized than Encord's.

### Public AV References

Labelbox lists general enterprise customers but does not foreground AV references the way Scale and Encord do. Automotive use tends to be 2D camera workloads and teams that are expanding into light 3D.

### Pricing Posture

Free, Starter, and Enterprise tiers. Usage-based via Labelbox Units (LBUs) approximately 0.10 dollars per LBU at entry level; enterprise is custom negotiated by volume and feature.

### Build vs Buy Positioning

Buy the platform, bring your own labelers, and extend via API. Labelbox explicitly positions as good for teams with strong in-house engineering that want extension points rather than turnkey service.

### Known Gaps

Weaker in dedicated LiDAR and sensor fusion workflows. Less automotive-industry-specific than Scale, Encord, or Applied Intuition.

Sources: [Labelbox pricing](https://labelbox.com/pricing/) (marketing), [Vendr Labelbox marketplace](https://www.vendr.com/marketplace/labelbox) (independent), [Encord AV ranking blog](https://encord.com/blog/ai-data-labeling-platforms-for-autonomous-vehicle-development/) (competitor-published, treat as biased but directionally useful).

---

## 3. Voxel51 (FiftyOne)

### Offering for AV

FiftyOne is the open-source dataset curation and model evaluation toolkit. **FiftyOne Enterprise** (formerly FiftyOne Teams) adds collaboration, access control, on-prem or private cloud deployment via Helm, user-based licensing, SLA, and Slack-channel support. Voxel51 integrated FiftyOne with NVIDIA Omniverse for AV synthetic data workflows and published a Porsche Research case study on synthetic data augmentation pipelines. Strong capability: side-by-side visualization of images, videos, and 3D sensor data with labels, predictions, and metadata in one interactive view. Data Quality Workflow added in 2025.

### Public AV References

Porsche Research (synthetic data pipeline); general automotive vertical. Not typically the sole labeling tool; it complements labeling platforms by handling curation, review, and evaluation.

### Pricing Posture

Open-source core is free. Enterprise is user-based licensing; pricing not public, direct sales only. Deployment inside customer infrastructure is standard.

### Build vs Buy Positioning

Voxel51 positions as the data-curation layer, not as a labeling platform. It is often paired with a separate labeling vendor or internal labeling ops.

### Known Gaps

Not a labeler. Annotation is delegated to plugins or integrations with CVAT, Labelbox, Scale, and others. Teams buying FiftyOne still need a labeling solution and an active-learning story.

Sources: [FiftyOne docs](https://docs.voxel51.com/), [FiftyOne pricing](https://voxel51.com/pricing) (marketing), [Voxel51 blog on synthetic data for Porsche](https://voxel51.com/blog/powering-physical-ai-synthetic-data-generation-pipeline) (marketing), [PRNewswire on NVIDIA Omniverse integration](https://www.prnewswire.com/news-releases/voxel51-accelerates-autonomous-vehicle-development-with-nvidia-omniverse-integration-302091979.html) (press release).

---

## 4. Applied Intuition

### Offering for AV

Applied Intuition is the closest thing to a category-defining vertical for AV development infrastructure. Products relevant to data work:

- **Data Explorer**: log-data search engine using a contrastive foundation model trained on over five billion text-image pairs for scenario mining across fleet logs.
- **Log Sim**: log-based resimulation, regression testing, and synthetic scenario extraction from real-world events.
- **Object Sim**: perception and planning simulation.
- **Applied Intuition Copilot**: AI chatbot over engineering data.

Applied Intuition raised a 600 million dollar Series F and now lists Volkswagen, Toyota, Nissan, Porsche, and Stellantis among customers. Toyota is named in Applied Intuition case studies.

### Public AV References

Volkswagen, Toyota, Porsche, Nissan, Stellantis, and construction and mining OEMs.

### Pricing Posture

Enterprise-only, custom multi-year contracts. Typically packaged across simulation, data management, validation, and services. Not a per-annotation model.

### Build vs Buy Positioning

Applied Intuition is positioning to be the operating system for AV and ADAS development. Buy the stack, reduce internal platform engineering burden.

### Known Gaps

Applied Intuition is strong on simulation, scenario mining, and validation. It is less of a dedicated labeling tool. Teams still need a primary annotation platform and a labeling ops function. Also note the relationship to Toyota: if Woven already has Applied Intuition under contract at a parent level, Travis may frame any new vendor conversation through the lens of what Applied Intuition does not cover.

Sources: [AI for mining autonomy datasets](https://www.appliedintuition.com/blog/ai-for-mining-massive-autonomy-datasets) (marketing), [Log Sim](https://www.appliedintuition.com/products/log-sim) (marketing), [2024 year in review](https://www.appliedintuition.com/blog/2024-year-in-review) (marketing), [Toyota case study page](https://www.appliedintuition.com/case-studies/toyota) (marketing), [Transport Topics on 600M Series F](https://www.ttnews.com/articles/applied-intuition-series-f) (independent).

---

## 5. Snorkel AI

### Offering for AV

**Snorkel Flow** is a programmatic labeling platform built on weak supervision research from Stanford. Users write labeling functions (heuristics) that generate noisy labels at scale; Snorkel models label-function accuracy and correlations to produce probabilistic training labels. The platform has expanded into foundation-model supervision and data-centric AI workflows. Public revenue figures cite approximately 148 million dollars in 2025, up from 36.8 million in 2024.

### Public AV References

Snorkel's public customer base skews to enterprise, government, and defense (intelligence community), finance, and healthcare. AV is mentioned as a vertical where weak supervision applies, but Snorkel does not have the public AV references that Scale, Encord, and Applied Intuition have.

### Pricing Posture

Enterprise platform license, custom pricing.

### Build vs Buy Positioning

Snorkel positions as a programmatic-labeling accelerator, not a full annotation platform. It fits best where rule-expressible heuristics can reduce the volume of human-labeled data required. For AV, that often means NLP-adjacent tasks (event tagging, metadata enrichment, behavioral label generation) rather than pixel-level 3D segmentation.

### Known Gaps

Does not replace human-in-the-loop 3D or sensor-fusion labeling. Limited AV-specific tooling compared with dedicated platforms. Works best alongside a primary labeling stack.

Sources: [Snorkel weak supervision guide](https://snorkel.ai/data-centric-ai/weak-supervision/) (marketing), [Getlatka revenue summary](https://getlatka.com/companies/snorkel-ai) (independent aggregator; treat figures as rough), [Snorkel paper on VLDB](https://link.springer.com/article/10.1007/s00778-019-00552-1) (academic).

---

## 6. Aquarium Learning

### Current Status

**Acquired by Notion on October 15, 2024.** No longer marketed as a standalone AV tool. The team and technology were absorbed into Notion's AI search capability, particularly for cross-platform retrieval across Slack, Google Drive, and GitHub.

### Historical Offering

Aquarium was a model-performance debugging and edge-case mining platform. It used embedding-based search over a customer's data and model predictions to surface failure modes and prioritize what to label next. Customers included AV teams during its independent years.

### Implication for Woven

If Travis evaluated Aquarium in prior years, that capability is no longer purchasable as a standalone product. The functional category (embedding-based failure mining, active learning loop closure) has been absorbed into FiftyOne, Encord, Applied Intuition Data Explorer, and Scale Nucleus.

Sources: [Aquarium landing page announcement](https://www.aquariumlearning.com/) (primary), [Peter Gao LinkedIn announcement](https://www.linkedin.com/posts/pgaooo_aquarium-is-joining-notion-activity-7251984217205551104-reFP) (primary).

---

## 7. Encord

### Offering for AV

Encord is the most AV-specialized labeling platform in this list and explicitly names **Woven by Toyota as a customer**. Key capabilities:

- Full multimodal support: 2D camera, 3D, LiDAR, radar, video.
- Native ingest of raw sensor data including MCAP, the common ROS 2 sensor-log container.
- AI-assisted automation with SAM2 integration for segmentation.
- Workflow agents and automated QA.
- Physical AI suite launched 2025 for robotic perception, Vision-Language-Action models, AV, and ADAS.
- 60 million dollar Series C closed February 2026 for AI-native data infrastructure.

### Public AV References

**Woven by Toyota** (publicly cited by Encord), plus over 300 AI teams. Encord aggressively markets AV as a primary vertical.

### Pricing Posture

Enterprise, custom pricing, typically annual platform subscription with volume tiers. Not public.

### Build vs Buy Positioning

Buy the platform; self-serve or combine with Encord-managed services.

### Implication for Woven Discovery

Encord is already in the Woven stack according to Encord's own marketing. That means Travis is either happy, mid-migration, or evaluating alternatives. The call should probe which scenario applies. If Encord is in, a BayOne engagement likely sits around Encord (integration, workflow automation, custom model assist, QA instrumentation, throughput analytics) rather than replacing it.

Sources: [Encord AV development blog](https://encord.com/blog/ai-data-labeling-platforms-for-autonomous-vehicle-development/) (marketing, self-cites Woven), [Encord Physical AI suite](https://encord.com/blog/physical-ai-suite/) (marketing), [Pulse2 on Series C](https://pulse2.com/encord-60-million-series-c-raised-to-scale-ai-native-data-infrastructure/) (independent). **Flag:** Encord publications mentioning Woven are marketing; treat the claim as directionally credible but confirm with Travis.

---

## 8. Roboflow

### Offering for AV

Roboflow is a developer-focused computer vision platform: data ingest, annotation, augmentation, training, deployment, and inference. Roboflow Universe hosts publicly available datasets including AV-adjacent ones (traffic lights, potholes, driver-assist classifiers). Over one million developers, half of the Fortune 100.

### Public AV References

Primarily the long tail of ADAS and perception projects. Not typically the platform for a full-AV-program like Woven. Strongly positioned for ADAS subcomponents, smaller perception teams, and rapid prototyping.

### Pricing Posture

Tiered SaaS with a free tier, credit-based usage, and enterprise plans. More accessible than Scale or Encord.

### Build vs Buy Positioning

Buy for speed and developer ergonomics. Good fit for narrow CV problems; not a full sensor-fusion AV platform.

### Known Gaps

Limited 3D and LiDAR depth. Less suited to petabyte-scale fleet data than Woven's requirements.

Sources: [Roboflow platform](https://roboflow.com/) (marketing), [Best data annotation platforms 2025](https://blog.roboflow.com/data-annotation-platforms/) (vendor-published comparison).

---

## 9. Open Source Stacks

### CVAT

Self-hostable via Docker; over one million prebuilt-image pulls. Strong at large-scale projects in autonomous driving. Handles dense urban scenes with 50+ objects per frame, supports video interpolation, exports to YOLO and COCO. SAM integration for automatic segmentation. Used broadly in research and teams that need data sovereignty.

### Label Studio

More multimodal than CVAT (text, audio, image, video, time series). Works with AWS, GCP, and self-hosted. Widely used for mixed-domain teams.

### FiftyOne (open source)

Already covered under Voxel51. The open-source core is a legitimate option for curation and evaluation without enterprise spend.

### Labelme, LabelImg, and smaller tools

Still present in research contexts, rarely used at AV-program scale.

### Market Signal

Per Data Insight Markets, the open-source data-labeling market is approximately 500 million dollars in 2025, projected to grow at 25 percent CAGR to 2.7 billion by 2033. This growth reflects teams that want control, customization, or cost containment and have the engineering capacity to own deployment.

### Implication

Teams like Woven typically run a hybrid: an enterprise labeling platform for the bulk of production annotation, plus open-source tools for experimental workflows, research labeling, or modalities the enterprise platform does not cover well. The open-source layer is often where in-house engineering time is spent.

Sources: [CVAT blog](https://www.cvat.ai/resources/blog/best-open-source-data-annotation-tools) (vendor blog, useful as reference), [CVAT GitHub](https://github.com/cvat-ai/cvat) (primary), [CVAT vs Label Studio](https://www.cvat.ai/resources/blog/cvat-or-label-studio-which-one-to-choose) (vendor-published).

---

## 10. Cloud-Native Options

### AWS SageMaker Ground Truth

Mature labeling service with active learning, integration with Amazon Mechanical Turk, vendor workforces, or private workforces. Tight S3, Lambda, and CloudWatch integration. Good fit for teams already deep in AWS. Depth of SageMaker across the full ML workflow is a real advantage for MLOps teams.

### Azure ML Data Labeling

Basic image labeling interface embedded in Azure ML. Less differentiated than SageMaker Ground Truth or Vertex AI. Appropriate for Azure-native shops.

### Google Vertex AI Data Labeling

Basic web-based annotation for Vertex models. BigQuery and Dataflow integration. Strong AutoML story for teams that want less hand-written training code.

### Implication for AV

Cloud-native labeling services are practical for non-safety-critical CV workloads and for teams that want a default annotator tightly coupled to their training stack. For production AV perception, teams routinely move beyond these to specialized tools because of 3D and sensor fusion needs, QA sophistication, and workforce quality.

Sources: [SageMaker Ground Truth docs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) (primary), [Cloudoptimo cross-comparison](https://www.cloudoptimo.com/blog/sagemaker-vs-azure-ml-vs-google-ai-platform-a-comprehensive-comparison/) (independent), [AWS Physical AI data pipeline blog](https://aws.amazon.com/blogs/industries/building-an-end-to-end-physical-ai-data-pipeline-for-autonomous-vehicle-3-0-on-aws-with-nvidia/) (AWS marketing).

---

## 11. Internal Tooling at Major AV Developers

### Waymo

Published the **Waymo Open Dataset** starting 2019, with 12 million 3D labels and 1.2 million 2D annotations. The labeling specifications are public on GitHub. Waymo has not open-sourced its internal labeling platform; what is public is the dataset and labeling specs, not the pipeline code.

### Cruise

Was a Scale AI customer publicly. Cruise was wound down by GM in late 2024.

### Zoox

Public Scale AI customer. No significant open-source labeling tooling of its own.

### Tesla

Operates an in-house data engine, approximately 1,000-person labeling team, heavy automated labeling pipelines (often called "offline auto-labeling"), shadow-mode data collection from fleet, and a closed-loop active-learning pipeline. Famous for vertical integration and rarely using external labeling vendors. None of the tooling is open source.

### Woven by Toyota (self-reporting via job descriptions and public blogs)

- Runs internal labeling-suite backend engineering (data platform team) that supports multiple ML training data formats and on-the-fly conversions.
- Operates model-introspection frameworks for statistical aggregation of recorded samples.
- Uses **Union.ai (managed Flyte)** for pipeline orchestration, managing petabytes of sensor data, hundreds of thousands of node hours, thousands of parallel workers; reported 20x faster iteration and over 1 million dollars annual cost savings.
- Published content on camera-data-driven autonomy at scale.
- Confirmed as an **Encord** customer per Encord marketing.
- Applied Intuition counts Toyota as a customer; unclear whether this touches Woven specifically or other Toyota business units.

### Pattern

Every major AV developer runs a hybrid: proprietary data engine plus one or more commercial labeling platforms plus workforce partners. The proprietary part is usually the data orchestration layer, edge-case mining logic, and internal tooling for the specific perception stack and sensor configuration. The commercial part is the annotation UI and workforce at scale.

Sources: [Waymo Open Dataset GitHub](https://github.com/waymo-research/waymo-open-dataset) (primary), [Waymo labeling specs](https://github.com/waymo-research/waymo-open-dataset/blob/master/docs/labeling_specifications.md) (primary), [Tesla data engine overview on LinkedIn Pulse](https://www.linkedin.com/pulse/teslas-data-engine-road-full-self-driving-taivo-pungas) (independent), [Towards Data Science on Tesla AI Day](https://towardsdatascience.com/tesla-ai-day-2021-review-part-2-training-data-how-does-a-car-learn-e8863ba3f5b0/) (independent), [Union.ai Woven by Toyota case study](https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai) (vendor-published), [Woven Enterprise AI blog](https://woven.toyota/en/our-latest/20220407/) (primary).

---

## 12. Recent Market Moves Worth Noting

- **Scale AI and Meta (June 2025):** Meta 14.3 billion dollar investment for approximately 49 percent of Scale; founder Alexandr Wang moved to Meta. Google, OpenAI, xAI reduced engagement over data-confidentiality concerns. Scale cut 200 staff and 500 contractors shortly after.
- **Aquarium to Notion (October 2024):** Exit from AV category.
- **Segments.ai to Uber (October 2025):** Uber absorbed a strong multi-sensor labeling platform primarily to serve Uber's autonomy and delivery ambitions.
- **Encord Series C (February 2026):** 60 million dollars for AI-native data infrastructure, aggressive expansion into Physical AI.
- **Applied Intuition Series F:** 600 million dollars, major commercial momentum with OEMs.
- **Kognic, Deepen, Dataloop, Superb AI, Mindkosh, Kili, BasicAI:** Smaller specialized vendors still active, often ranked in AV-specific comparisons. Most have specific niches (Kognic on 3D fusion, Superb AI on dataset lifecycle, Dataloop on mid-market).

---

## Comparative Matrix

| Vendor | Core Capability for AV | AV Focus | Pricing Posture | Notable AV Customers |
|---|---|---|---|---|
| Scale AI | Full-service Data Engine, AFM-1 2D autolabel, Nucleus curation, Rapid, Studio | High | Custom enterprise; 90k to 400k+ typical annual contracts; per-annotation pricing varies widely | Cruise (historical), Zoox, Nuro, Toyota, GM |
| Labelbox | General multimodal labeling, Model Foundry, light 3D | Medium | LBU usage model, enterprise custom | Enterprise customers broadly; less AV-branded |
| Voxel51 FiftyOne | Dataset curation, model eval, Omniverse integration for synthetic data | Medium-high for curation, low for labeling | Open-source core free; Enterprise user-based license | Porsche Research, automotive vertical |
| Applied Intuition | Simulation, Log Sim, Data Explorer scenario mining, Copilot | High, vertical | Enterprise multi-year contracts | VW, Toyota, Porsche, Nissan, Stellantis |
| Snorkel AI | Programmatic labeling via weak supervision; labeling functions | Low for AV specifically | Enterprise platform license | Primarily enterprise, defense, financial, healthcare |
| Aquarium Learning | Model debugging, edge-case mining (historical) | N/A - acquired | N/A - absorbed by Notion October 2024 | N/A |
| Encord | LiDAR, radar, 3D, video multimodal labeling; SAM2; Physical AI suite | Very high, actively positioned | Enterprise custom | **Woven by Toyota** (publicly cited), 300+ AI teams |
| Roboflow | Developer CV platform; broad, accessible | Medium for ADAS, low for full-AV | Tiered SaaS with free tier | Long tail; Fortune 100 breadth |
| CVAT (OSS) | Self-hosted labeling; SAM integration; 3D and video | High for those who self-host | Free OSS; paid cloud available | Unlisted; used broadly in research and production |
| Label Studio (OSS) | Multi-modal self-hosted labeling | Medium | Free OSS; Heartex enterprise | Unlisted; broad enterprise use |
| AWS SageMaker GT | Labeling inside AWS ML stack; active learning; workforce options | Medium | Pay-per-use, workforce costs added | Many AWS-native teams |
| Azure ML Labeling | Basic image labeling inside Azure ML | Low | Azure consumption | Azure-native teams |
| Vertex AI Labeling | Basic annotation inside Vertex AI | Low | GCP consumption | GCP-native teams |
| Segments.ai | Multi-sensor labeling (acquired by Uber October 2025) | Was high, now Uber-internal | N/A for new buyers | Uber, prior AV customers |
| Applied Intuition Toyota ref | Cross-referenced | High | Enterprise | Toyota (scope unclear to Woven) |

---

## Where Custom Engagements Still Have Room

BayOne does not need to compete with these vendors. It needs to sit in the integration and engineering gaps they leave open. Based on the landscape above, the durable custom-work categories for AV-scale teams like Woven are:

### 1. Integration and Orchestration Between Tools

No single vendor does everything. Woven runs Union.ai for orchestration, Encord for labeling, internal backend services for format conversion, and some combination of FiftyOne, custom analytics, or internal tooling for curation. The glue between these systems, especially at petabyte scale with sensor fusion, remains bespoke. Every change in one vendor's API or data model creates integration work.

### 2. Custom Active-Learning and Edge-Case-Mining Logic

Vendors provide generic active-learning hooks. The logic that decides which scenarios are most valuable for a specific perception or planning model depends on the model architecture, the sensor configuration, and the operational design domain. This is where the most model-impacting engineering happens, and it rarely maps cleanly to a vendor feature. BayOne can build scenario-specific miners, bespoke embedding indexes, and failure-mode detectors tied to the customer's model.

### 3. Labeling QA and Throughput Instrumentation

Every AV team needs labeling quality metrics, labeler productivity, inter-annotator agreement, drift detection on labeler performance, and SLA tracking against vendors and internal workforces. Vendors report their own numbers, but cross-vendor QA dashboards, reconciliation logic, and independent QA workflows remain custom work.

### 4. Custom Model-Assisted Labeling Pipelines

AFM-1 and SAM2 and similar foundation models produce pre-labels. Stitching those pre-labels into a customer-specific taxonomy, confidence thresholding, automatic escalation to humans, and calibration against the customer's own held-out set is not shipped out of the box. This is a straightforward BayOne engagement pattern.

### 5. Sensor-Fusion and Format Conversion Backends

Woven's own job descriptions indicate the data platform team builds backends that support multiple ML training data formats with on-the-fly conversions and sinks. This is an ongoing engineering load that scales with sensor and format proliferation. An outsourced engineering team can own specific conversion pipelines, MCAP integrations, or format normalizers.

### 6. Synthetic Data Integration and Closed-Loop Workflows

NVIDIA Omniverse, Applied Intuition, Applied Intuition Log Sim, FiftyOne for synthetic augmentation, internal simulators. Tying synthetic generation into the data curation and labeling loop with reproducible experiments is custom work. Every team does it slightly differently.

### 7. On-Prem, Air-Gapped, or Data-Sovereign Deployments

If Woven Japan has data-locality or sovereignty requirements for certain datasets, the vendor SaaS path does not always satisfy them. Deploying FiftyOne Enterprise, CVAT, Label Studio, or hybrid architectures inside a customer boundary is real engineering work.

### 8. ML Engineering Capacity Augmentation

Sometimes the need is not platform choice but staff. BayOne's managed engineering model can absorb backlog in labeling ops engineering, dataset pipeline development, curation tooling, and evaluation infrastructure without Woven hiring headcount.

### Meta Answer to the Meta Question

What is Woven most likely to still need custom engagement for? Not labeling UI. Not storage. Not generic workforce management. The custom work is in the seams: integration between best-of-breed vendors, model-specific active learning and edge-case mining, QA instrumentation across multiple workforces and tools, and ML engineering capacity for the backlog of glue code that no vendor ships. That is a consulting and custom-engineering conversation, not a tool-displacement conversation.

---

## Sources Flagged by Type

**Marketing material (primary vendor content), treat directionally:**

- Scale AI: scale.com/automotive, scale.com/blog/afm1, scale.com/blog/customer-trust-scale-meta-deal
- Labelbox: labelbox.com/pricing
- Voxel51: voxel51.com/pricing, voxel51.com/blog/powering-physical-ai-synthetic-data-generation-pipeline
- Applied Intuition: appliedintuition.com product and blog pages
- Encord: encord.com AV development blog, Physical AI suite blog (self-references Woven)
- Roboflow: roboflow.com, blog.roboflow.com
- CVAT: cvat.ai resources blog

**Independent or third-party, more reliable for posture and pricing:**

- Vendr: vendr.com/buyer-guides/scale-ai, vendr.com/marketplace/labelbox (enterprise deal aggregators)
- Pulse2, TechCrunch, TransportTopics, EU-Startups (funding and corporate moves)
- Just Think AI, Everest Group, Public Citizen (independent commentary on Scale-Meta)
- Cloudoptimo, Leanware, getdeveloper.net (cloud platform comparisons)
- Getlatka (revenue aggregator; treat as rough)
- GDSOnline, iMerit, Keylabs, Label Your Data, Mindkosh (industry blogs; most are themselves vendor-adjacent; cross-reference)

**Primary or academic:**

- Waymo GitHub and labeling specs
- Snorkel VLDB paper
- GitHub repositories for CVAT and FiftyOne
- AWS, Azure, Google Cloud documentation

**Press releases and announcements:**

- Aquarium to Notion (founder LinkedIn, company page)
- Segments.ai to Uber (Uber, CIO, PYMNTS)
- Scale-Meta June 2025 (multiple outlets)
- Encord Series C February 2026 (Morningstar, Pulse2)
- Applied Intuition Series F (Transport Topics)

---

## Key Facts to Carry Into the 3:30 PM Call

1. Woven by Toyota is a named Encord customer in Encord's own marketing. Probe this. Is Encord the primary labeling platform today? At what scale? Any pain points?
2. Woven uses Union.ai for orchestration and has an internal labeling-suite backend engineering team. There is already significant custom work happening inside Woven.
3. Applied Intuition lists Toyota as a customer. Scope within Woven specifically is unclear. Worth asking.
4. The Meta-Scale deal in June 2025 is a live concern for any OEM worried about data confidentiality. Travis may or may not share this view; the topic is legitimate to raise if Scale comes up.
5. Segments.ai was absorbed by Uber in October 2025 and is not available to new buyers.
6. Aquarium Learning was absorbed by Notion in October 2024 and is not available to new buyers.
7. The custom engagement space for BayOne is the integration seams, active-learning logic, QA instrumentation, and ML engineering capacity. Not tool replacement.
