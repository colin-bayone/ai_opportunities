# 04 - Research: Woven by Toyota Company Profile

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** Woven company profile

---

## Purpose

This document consolidates publicly available research on Woven by Toyota in preparation for a discovery call with Travis Millet (Manager of Technical Operations Engineering) on 2026-04-23 at 3:30 PM PST. It focuses on the company's strategic positioning, organizational structure, AV data pipeline posture, Toyota Research Institute (TRI) relationship, hiring signals, tooling partnerships, and competitive context. Inferences from limited sources are flagged explicitly. Open questions are captured at the end.

---

## 1. Company Overview and Corporate History

Woven by Toyota, Inc. is the mobility technology subsidiary of Toyota Motor Corporation, positioned as the 18th member of the Toyota Group. The company is headquartered in Tokyo (Nihonbashi Muromachi Mitsui Tower) with a significant United States presence in Palo Alto, California at 900 Arastradero Road.

Corporate lineage:

- **2018:** Founded as Toyota Research Institute - Advanced Development (TRI-AD), a joint venture among Toyota, Denso, and Aisin.
- **January 2021:** Reorganized and renamed Woven Planet Holdings, Inc., with two operating companies (Woven Core, Woven Alpha) and Woven Capital as an $800M investment fund.
- **April 2021:** Announced acquisition of Lyft's Level 5 self-driving division for approximately $550M, closed July 2021. The acquisition brought over 300 engineers, research scientists, and mobility specialists.
- **July 2021:** Announced acquisition of CARMERA, Inc. (road mapping).
- **September 2021:** Acquired Renovo Motors (vehicle operating systems).
- **April 2023:** Renamed Woven by Toyota, Inc. Software development by Woven was reorganized to be outsourced from Toyota, and Toyota took 100% ownership, making Woven a wholly owned subsidiary.
- **October 2023:** James Kuffner departed as CEO; Hajime Kumabe appointed CEO.

Sources: Wikipedia - Woven by Toyota; global.toyota newsroom (33786527, 35244091, 35682170, 35589999, 39070846).

---

## 2. The Arene Platform and Public Positioning

Arene is Woven by Toyota's unified vehicle software development platform and is positioned as Toyota's first step toward fully software-defined vehicles. The platform made its production debut in the all-new 2026 Toyota RAV4, announced May 21, 2025. This is the first Toyota vehicle delivered to customers with features powered by Arene.

Arene is composed of three primary packages:

- **Arene SDK:** Provides building blocks for developing vehicle software consistently across systems and vehicle programs, with shared APIs and frameworks that allow software to be integrated once and reused across vehicles.
- **Arene Tools:** Collaborative workflows and virtual environments for testing, validating, and managing software. Includes integrated simulation and verification in automated workflows.
- **Arene Data:** Secure data infrastructure with privacy-first pipelines and standardized data models that enable fleet-level understanding and improvements across vehicle lines.

Public positioning emphasizes:

- End-to-end testing that combines simulation with fleet validation.
- Automated traceability linking requirements, development, and testing.
- Hardware flexibility across ECU generations and vehicle architectures.
- Global deployment across diverse regulatory environments.
- Over-the-air (OTA) update capability so vehicles stay current after purchase.

Capabilities in the 2026 RAV4 include smarter infotainment, advanced safety systems, customizable digital displays, and future OTA updates. Arene targets global automakers beyond Toyota as well, consistent with Woven's stated ambition to set an industry standard.

Sources: woven.toyota/en/technology/arene/; woven.toyota/en/our-latest/20250521/; autonews.com Toyota Arene coverage.

---

## 3. Woven City and Its Role in Data Collection and AV Testing

Woven City is a real-world test bed in Susono, Shizuoka Prefecture, first unveiled at CES 2020 and officially launched in September 2025. The first phase accommodates approximately 300 to 360 residents (called "Weavers," primarily Toyota Group employees and families). Public opening to a target population of 2,000 residents is planned for fiscal year 2026.

Key physical design features:

- Three ground-level road classifications: pedestrian-exclusive, pedestrian and personal mobility shared, and vehicle-dedicated.
- A fourth underground road that enables testing unaffected by weather or temperature.
- Use of autonomous shuttles such as the e-Palette.

On April 22, 2026 (one day before the discovery call), Toyota and Woven by Toyota unveiled a significant package of new AI technologies at Woven City:

- **Woven City AI Vision Engine:** A large-scale AI foundation model that enables the city to understand and respond to real-world conditions in real time. Described in Automotive News coverage as "one of the world's top AI vision engines."
- **Woven City Integrated ANZEN System:** Combines the AI Vision Engine with Woven City Behavior AI and Woven City Drive Sync Assist to understand movement, anticipate behavior, and surface information to pedestrians and drivers. ("Anzen" is Japanese for "safety.")
- **Woven City Infra Hub:** An integrated data platform that unifies data across the city.
- **Woven City Data Fabric:** A data management framework that facilitates data utilization while respecting individual preferences and privacy.
- **Inventor Garage:** A co-creation hub with prototyping, testing areas, and accommodations for Inventors.

The Kakezan concept (Japanese for "multiplication") is Woven by Toyota's stated framing for combining Toyota's mass-production experience, Woven's software expertise, and the unique capabilities of Inventors and partners.

Inferred relevance to data collection and AV testing: Woven City provides a controlled multimodal sensing environment with fleet activity, pedestrian behavior, and infrastructure telemetry that feeds Woven's foundation models and AV data pipelines. The Data Fabric and Infra Hub announcements suggest active investment in the data plumbing that sits underneath ML training, triage, and evaluation workflows. (This specific framing is inferred from adjacent public statements; the sources do not directly label these as AV training feeds.)

Sources: global.toyota newsroom 43347785, 44256155; woven-city.global; woven.toyota/en/news/20260422/; autonews.com Woven City vision AI coverage.

---

## 4. Organizational Structure

### 4.1 Executive Leadership

From the Woven by Toyota leadership page:

| Name | Title |
|---|---|
| Hajime Kumabe | CEO, Representative Director |
| John Absmeier | CTO, Director |
| Hiroaki Okuchi | CCO |
| Daisuke Toyoda | Woven City Lead, SVP (founding member; son of Akio Toyoda) |
| Nancy Ji | HR Lead |
| Jean-Francois Campeau | Arene Lead |
| Dushyant Wadivkar | AD/ADAS Lead |
| Jack Yan | Cloud and AI Lead |
| Ro Gupta | Investments and Acquisitions Lead (also Managing Director, Woven Capital, since December 2025) |
| Kishore Kondragunta | Enterprise Technology Lead |

Board members also include Masahiro Yamamoto and Holly Walters (Directors) and Koji Kobayashi (Audit and Supervisory). Yumi Otsuka is listed as Corporate Adviser.

### 4.2 Functional Pillars

The public leadership list maps to five visible functional pillars relevant to engineering delivery:

1. **Arene** (vehicle OS and software platform) - under Campeau.
2. **AD/ADAS** (automated driving, advanced driver assistance) - under Wadivkar.
3. **Cloud and AI** (foundational ML infrastructure, multi-tenant workspaces, auto-labeling, AV data pipelines) - under Yan.
4. **Woven City** - under Daisuke Toyoda.
5. **Enterprise Technology** (internal IT platforms) - under Kondragunta.

Investments and Acquisitions (Gupta) is a separate strategic function; Woven Capital's own leadership refreshed in April 2026 with Michiko Kato (CIO/CEO of Toyota Invention Partners) and Mia Panzer (COO) reporting to Gupta.

### 4.3 Where a Technical Operations Engineering Team Likely Sits

**This is an inference, not a directly stated fact.** Public materials do not publish an organization chart below the pillar-lead layer. Based on the scope of Travis Millet's title ("Manager of Technical Operations Engineering") and the publicly stated responsibilities of the AD/ADAS and Cloud and AI pillars, the team most plausibly sits in one of:

- **AD/ADAS pillar (Wadivkar):** If the team operates the AV data triage, labeling QA, scenario curation, or fleet data intake workloads. The Active Learning Loop, evaluation framework, and simulation workflows described in Woven's public blog posts are AD/ADAS functions.
- **Cloud and AI pillar (Yan):** If the team operates shared ML infrastructure, auto-labeling pipelines, multi-tenant data workspaces, or compute/storage platforms that serve AD/ADAS as an internal customer. Woven's public description of the Cloud and AI team explicitly covers "auto-labeling and automated driving data pipelines."
- **Arene pillar (Campeau):** If the team operates the production-vehicle data pipelines feeding back into Arene Data from the deployed RAV4 fleet.

Woven's internship program postings confirm the existence of a **Vehicle Data team** and a **Software Data team**, which suggests the "data operations" work is distributed rather than centralized in a single org. The Vehicle Data team is described as "responsible for ingesting, processing, and providing actual and simulated vehicle data to internal and external customers within the Toyota group."

Sources: woven.toyota/en/company/leadership; techcrunch.com (Woven Capital March 2026); jobs.lever.co/woven-by-toyota internship postings.

---

## 5. AV Data Pipeline, Labeling, Triaging Operations, and ML Infrastructure

This is the area where Woven publishes most openly. The following public signals are particularly relevant to a data-triaging engagement conversation.

### 5.1 Active Learning Loop (stated framework)

Woven describes its AD/ADAS data strategy as a proprietary **Active Learning Loop** with eight stages:

1. Vehicle data collection via sensors.
2. Issue and scenario identification.
3. Database updates with new scenarios.
4. Retrieval of related historical scenarios.
5. Expert-guided training selection.
6. AI model training and evaluation.
7. Over-the-air model updates.
8. Real-world deployment.

High-volume pipelines process fleet data from vehicles across regions and model years, with stated emphasis on strict privacy and data-handling governance standards. Stages 2, 3, 4, and 5 are the heart of what most practitioners would call triage and curation.

### 5.2 ML Training Infrastructure (Flyte to Union.ai migration)

Woven publicly migrated from self-managed Flyte to Union.ai in 2023. Per the Union.ai case study:

- Pipeline manages **petabytes of sensor data**.
- Workloads include **hundreds of thousands of node hours** and **thousands of parallel workers**.
- Covers data annotation, perception labeling, dynamic scene processing, and GPU-accelerated model training.
- Reported outcomes: **20x faster ML iteration cycles**, **$1M+ annual savings** on compute and scheduling.
- Quoted from Alborz Alavian, Senior Engineering Manager: Union.ai support was "critical" when Woven needed to "significantly scale up our data processing needs to meet major milestones."

### 5.3 Evaluation Framework and Model Introspection

Public blog posts describe:

- A **three-fold evaluation framework:** granular metrics for targeted scenarios plus general metrics for large-scale datasets.
- A **visualization and introspection framework** enabling rapid inspection of simulation experiments, aggregation, and drilldown into individual metrics and scenarios.
- A **model introspection** capability that allows ML engineers to "sort through all inference samples in under a minute and quickly identify failure cases." Inference data is gathered and published to the cloud within minutes.

### 5.4 Camera Data and ML Planner

Woven developed an in-house stereo camera collection device that is **90% cheaper** than the sensor suites previously used. After nine months of iteration, the ML Planner demonstrated comparable performance on camera-only data as on high-cost lidar/radar data, with a 42% improvement on the "stop behind lead" scenario and 5% across all scenarios.

### 5.5 Data Annotation Pipeline (Arene AI / DGP)

A 2021 Woven post describes a scalable annotation pipeline built by the Arene AI team at Woven Alpha with three phases: receiving targeted data, requesting annotations from vendors, delivering results. Three standardized parameter types decouple dependencies (customer project, vendor process, delivery format). The team adopted **Dataset Governance Policy (DGP)**, a unified dataset management format developed collaboratively with Toyota Research Institute and released as open source. Reported outcomes included up to 90% reduction in human errors.

Sources: union.ai case study; woven.toyota/en/our-latest/20211105/, 20220127/, 20220407/, 20210927/; woven.toyota/en/technology/automated-driving/; woven.toyota/en/technology/cloud_ai.

---

## 6. Relationship to Toyota Research Institute (TRI) and Toyota Motor Corporation

### 6.1 Corporate Relationship

Woven by Toyota is a **wholly owned subsidiary** of Toyota Motor Corporation as of 2023. Software development performed by Woven is contractually outsourced from Toyota. Kenta Kon (Toyota CFO, becoming President and CEO of Toyota Motor Corporation in April 2026) has explicit cross-functional management experience at Woven by Toyota.

### 6.2 TRI Is a Separate Entity

Toyota Research Institute, Inc. (TRI) and Woven by Toyota are distinct. TRI, based in Los Altos, California (with additional presence in Cambridge, Massachusetts and Ann Arbor, Michigan), focuses on fundamental research in AI, robotics, human-amplifying mobility, and materials science. Woven is the production-oriented software development arm.

TRI-AD (the 2018 joint venture) was the predecessor to Woven Planet Holdings and then Woven by Toyota. TRI (without "-AD") is a separate US-based research entity that continues to exist and collaborate with Woven.

### 6.3 Team Moves from TRI to Woven

Public sources confirm at least one major wave of transfers: **TRI "graduated" approximately 150 researchers out of research into development,** and those researchers are now at Woven by Toyota working on production vehicle development. Additionally, the 2021 Level 5 acquisition brought engineers who were already working jointly with TRI into Woven. The Dataset Governance Policy was developed collaboratively between Woven and TRI, indicating continuing technical exchange.

Sources: global.toyota newsroom 33786527, 35244091; tri.global/about-us; woven.toyota/en/our-latest/20210927/.

---

## 7. Hiring and SOW Signals

### 7.1 Scale of Hiring

As of April 2026, external job aggregators indicate approximately **195 open positions** at Woven by Toyota globally across Tokyo and Palo Alto (and smaller sites). The careers portal runs on Lever (jobs.lever.co/woven-by-toyota).

### 7.2 Roles Directly Relevant to Data Triaging and Operations

Public role titles and descriptions include:

- **Senior Machine Learning Engineer, Behavior Data:** Designs and implements data strategies for "collecting, sampling, labeling, and using large scale datasets to enhance machine learning model performance."
- **Data and Machine Learning Engineer (Internship):** Placements across "Vehicle Data" and "Software Data" teams. Vehicle Data is described as responsible for "ingesting, processing, and providing actual and simulated vehicle data to internal and external customers within the Toyota group."
- **Data Platform, Senior Software Engineer, Enterprise AI:** Cloud and AI team role.
- **Senior Machine Learning Engineer, World Foundation Model:** Suggests ongoing investment in foundation-model-scale perception or behavior modeling.
- Multiple postings describe building and maintaining "ML pipelines that produce training and evaluation data for behavior and prediction models, including ETL, feature extraction, augmentation, and labeling workflows."

### 7.3 Interpretation

The hiring pattern suggests Woven is scaling data pipeline, labeling, and evaluation infrastructure in parallel with AD/ADAS modeling roles. This is consistent with the public narrative that a large fleet data volume (RAV4 production fleet plus test fleets) is feeding back into a retraining loop, and with Union.ai case-study language about needing to "significantly scale up data processing needs to meet major milestones." (Inference: the throughput growth on the operational side of this pipeline is a plausible source of demand for external managed-services capacity.)

### 7.4 Restructuring Signals

Employee discussion forums (Blind, LinkedIn posts) reference 2023-era layoffs, particularly following the April 2023 reorganization when software work was formally outsourced from Toyota and Woven became wholly owned. No specific 2024-2025 large layoff events surfaced in the search results. The broader trajectory appears to be restructuring and sharpening of scope rather than workforce contraction.

Sources: jobs.lever.co/woven-by-toyota; builtin.com/company/woven-toyota/jobs; startup.jobs/company/woven-by-toyota; teamblind.com discussions.

---

## 8. Known Technology Partners and Vendors

Based on public sources:

| Partner | Role |
|---|---|
| **Union.ai** | Managed AI workflow orchestration platform (successor to internal Flyte). Manages petabytes of sensor data and GPU training workloads. |
| **Applied Intuition** | Simulation tooling. Used for end-to-end perception verification, sensor modeling (including Toyota's proprietary cameras), synthetic data generation (weather, fog, time of day variations), and CI environments. |
| **Encord** | Multimodal data management and annotation platform. Woven listed as one of Encord's customers. |
| **AWS** | Referenced in the Union.ai / Amazon EKS integration for Woven's AI workloads (via public AWS blog and Union marketplace listing). |
| **Waymo** | Strategic partnership announced April 2025 to develop next-generation personally owned vehicles combining Waymo's AV stack with Toyota's Arene platform. |
| **Denso, Aisin** | Historical joint-venture partners from TRI-AD days; continuing collaboration in the broader Toyota/Denso/Woven software-centered mobility restructuring. |
| **Toyota Research Institute** | Co-developer of Dataset Governance Policy and source of ~150 transferred researchers. |

Scale AI was searched but no public Woven-Scale relationship surfaced in the sources reviewed. Absence of a search hit is not conclusive.

Sources: union.ai case study; appliedintuition.com/case-studies/toyota; encord.com; aws.amazon.com/blogs (Union.ai on EKS); waymo.com/blog 2025-04; global.toyota newsroom 42703368.

---

## 9. Competitive Context

### 9.1 Stated and Implied Competitive Set

Public framing positions Woven and Toyota in three overlapping competitions:

1. **Software-defined vehicle platform leadership** (Arene vs Tesla's vertically integrated stack, vs other OEM platforms such as Mercedes MB.OS, Volkswagen CARIAD, Rivian's in-house stack, and increasingly Chinese OEMs). The Automotive News coverage of Woven City specifically frames the AI Vision Engine announcement as part of "the race with China heats[ing] up."
2. **Personally owned autonomous vehicles (POVs)** via the Waymo partnership, explicitly framed in press coverage as going after Tesla. Tesla is described as the current market leader in personally owned self-driving vehicles; Waymo plus Toyota offers a lidar-plus-radar-plus-camera counterweight to Tesla's camera-only approach.
3. **Foundation models for physical AI** (vision-language-action models, world models). Woven's "World Foundation Model" job posting and the Woven City AI Vision Engine announcement both signal direct engagement in this frontier.

### 9.2 Public Narrative

Woven's public narrative emphasizes:

- A full-stack approach that pairs AI decision-making with Toyota's safety principles.
- Fleet-scale, OEM-grade data advantage over smaller AV-only startups.
- Global regulatory reach across many regions and road types.
- A production-first posture (Arene is in the 2026 RAV4 now) rather than a pure R&D posture.

Toyota historically lagged in perceived software-defined vehicle narrative. Woven is the vehicle through which that perception is being corrected. The April 22, 2026 Kakezan announcement and the Waymo partnership are both visible attempts to close that gap.

Sources: autonews.com Woven City vision AI coverage; electrek.co Waymo/Toyota coverage; wardsauto.com Toyota-Waymo JV analysis; theautopian.com.

---

## 10. Open Questions the Web Research Could Not Answer

The following questions materially affect engagement shaping but were not answerable from public sources. These should be asked or confirmed on the call or through Colin's existing BayOne relationships.

1. **Exact reporting line for Travis Millet's Technical Operations Engineering team.** Is it inside AD/ADAS (Wadivkar), Cloud and AI (Yan), Arene (Campeau), or a platform function that spans them?
2. **Specific scope of "Technical Operations Engineering."** Does it own data intake, triage and curation, labeling QA, or production ML infrastructure operations? Or is it broader (hardware operations, fleet operations, lab operations)?
3. **Fleet composition behind the pipeline.** Which sources feed the triage workload: production RAV4 OTA data, AV test fleet data, Woven City data, or partner data (including Waymo joint work)?
4. **Current labeling vendor mix and volumes.** Encord is publicly disclosed but may not be the only vendor. What is the in-house-vs-outsourced split?
5. **Relationship between Arene Data, Cloud and AI auto-labeling pipelines, and AD/ADAS-specific pipelines.** Are these one stack, or three parallel stacks with varying maturity?
6. **State of the Active Learning Loop in 2026.** Public descriptions date from 2022. What has changed with foundation models, the World Foundation Model role, and the Woven City Data Fabric announcement?
7. **Where the pain is.** Public materials celebrate the Union.ai migration. What is now the binding constraint: human labeling throughput, scenario curation quality, evaluation coverage, edge case discovery, or cross-team data contract governance?
8. **Geographic distribution of the team.** Palo Alto has a substantial AV-focused group (former Level 5); Tokyo is the corporate and Arene center. Where does Travis's team sit and how is the work split across sites?
9. **Managed services precedent.** Has Woven previously engaged external managed-services providers for data triage, labeling QA, or ML ops support, and at what scale?
10. **Confidentiality and IP posture.** The public materials emphasize strict privacy and data-handling governance. What does this mean in practice for an external managed-services partner handling labeled driving data?

---

## 11. Source Index

Primary sources consulted:

- en.wikipedia.org/wiki/Woven_by_Toyota,_Inc.
- woven.toyota/en/arene/ and woven.toyota/en/technology/arene/
- woven.toyota/en/technology/automated-driving/
- woven.toyota/en/technology/cloud_ai
- woven.toyota/en/company/leadership
- woven.toyota/en/company/profile/
- woven.toyota/en/careers/ and jobs.lever.co/woven-by-toyota
- woven.toyota/en/our-latest/ posts dated 20210927, 20211105, 20220127, 20220407, 20250521, 20260422, 20251218
- global.toyota newsroom 33786527, 33751885, 35244091, 35682170, 35589999, 39070846, 39828555, 42703368, 43347785, 43359087, 43951723, 44256155
- union.ai case study on Woven by Toyota
- appliedintuition.com/case-studies/toyota
- encord.com customer list
- waymo.com/blog/2025/04 Waymo-Toyota partnership
- autonews.com Woven City vision AI coverage; Toyota Arene coverage
- techcrunch.com Woven Capital March 2026 leadership
- electrek.co, wardsauto.com, theautopian.com on Toyota-Waymo competitive context
- woven-city.global
- aws.amazon.com/blogs (Union.ai on EKS reference)

---

*End of research document.*
