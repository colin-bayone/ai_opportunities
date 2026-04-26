# 04 - Research: Travis Millet Public Footprint

**Source:** Web research
**Source Date:** 2026-04-23
**Document Set:** 04 (Pre-call web research)
**Pass:** Travis Millet public footprint

---

## Executive Summary

Travis Millet maintains a minimal public-facing professional footprint. He has a LinkedIn profile, is indexed on contact-intelligence databases (ZoomInfo, SignalHire, RocketReach) and appears in a third-party org-chart site (The Org). Beyond these structural traces, there is no evidence of public writing, conference talks, podcast appearances, panel participation, patents, or academic publications under his name in the autonomous vehicle, machine learning, or data operations domains. The most substantive public signal about his current role comes indirectly: a Woven by Toyota Triage Manager job description at Lever, published Woven by Toyota engineering blog posts and customer case studies from Weights and Biases, Union.ai, and Microsoft, and The Org's extracted reporting structure. These sources describe the technical and organizational environment Travis operates in rather than his own positions.

For a first discovery call, the practical consequence is that Colin should not walk in with quotes or talks to reference back to Travis. The material for rapport-building is the team and the problem space, not Travis's personal brand.

---

## 1. LinkedIn Profile and Career Arc

### 1.1 Profile Exists but Is Not Publicly Scrapeable

Travis Millet has a LinkedIn profile at `https://www.linkedin.com/in/travis-millet-b405a64/`. LinkedIn returned a 999 status code when this research attempted a direct fetch, which is consistent with LinkedIn's standard anti-scraping posture. The profile is publicly listed in search engine results but its detailed contents are not accessible through unauthenticated web fetch.

Public third-party aggregators surface the following career arc, which aligns with the internal BayOne notes:

- **Current:** Manager, Technical Operations Engineering at Woven by Toyota
- **Previous:** Senior Triage Operations Lead at Toyota Research Institute
- **Prior:** F-16 Flight Dynamics Lead, Air Force Test Center (out of scope per Colin)
- **Education:** Master of Science, Brigham Young University

Sources: ZoomInfo profile listing (blocked from direct fetch, but LinkedIn search snippet and ZoomInfo snippet both confirm), The Org profile via Steve Lauziere's direct reports page.

### 1.2 Reporting Line (Directly Confirmed)

The Org's organizational chart for Woven Planet Holdings lists Travis Millet as a direct report of **Steve Lauziere**, titled Director of Engineering (current title Senior Manager, per Lauziere's public profile, promoted March 2023). Lauziere's background is Argo AI (Senior Manager, Engineering for embedded software on self-driving vehicles), Amazon (Manager, Software Development), and Ford (Product Development Engineer through Supervisor, Hardware Architecture and Acceleration, Autonomous Vehicles). This is directly stated on The Org.

Other engineers and managers listed alongside Travis under Lauziere include Paul Ozog (Engineering Manager), Jan Falkowski (Director of Engineering, Geo), Anastasia D. (Senior Engineering Manager), Jorge de Castro (Engineering Manager), Paul Sastrasinh (Senior Engineering Manager), Richard Higgins (Engineering Manager, Japan Blue Team), Miho Kusaka (Senior Engineering Manager), Michael Bell (Tech Lead / Engineering Manager), and Harsh Mehta (Senior Engineering Manager). The Org labels this cluster as an Engineering department of seven with zero open positions listed at time of crawl.

Inferred, not directly stated: the range of titles under Lauziere (Geo, Japan Blue Team, infrastructure-flavored senior managers) suggests Lauziere sits over a broad AD/ADAS engineering function, and Travis is the Technical Operations Engineering leader within that function. This is consistent with Travis owning triage operations as an internal-facing engineering capability rather than a product team.

Sources:
- `https://theorg.com/org/woven-planet-holdings/org-chart/steve-lauziere`
- `https://www.linkedin.com/in/steve-lauziere` (confirmed Lauziere current title via search snippet)

### 1.3 Career Arc Interpretation

Travis's visible arc goes from aerospace flight test to Toyota Research Institute triage operations to Woven by Toyota technical operations engineering. This is a consistent trajectory through **safety-critical operational engineering roles**, not a research or individual-contributor ML trajectory. That shape matters for Colin: Travis is likely to approach vendor discussions as an operations owner who cares about throughput, SLAs, quality consistency, and headcount economics, rather than as a research collaborator evaluating algorithmic novelty.

The lateral move from TRI (Senior Triage Operations Lead) to Woven by Toyota (Manager, Technical Operations Engineering) is the main visible career event. It tracks the broader 2020 to 2021 corporate reshuffle in which Toyota Research Institute - Advanced Development, Inc. (TRI-AD) formed Woven Planet Holdings, Woven Core, and Woven Alpha, later rebranded as Woven by Toyota in April 2023. Travis's two Toyota-family roles are best understood as the continuation of a single triage mission through an organizational transition, not a change of discipline.

---

## 2. Public Writing, Speaking, and Other Published Work

### 2.1 Search Results

Targeted searches across the following axes returned no results authored by this Travis Millet:

- Conference talks and speaker bureau listings
- Podcast interviews
- Medium, GitHub, and YouTube (professional)
- Patents (Justia patent database)
- Academic publications and BYU thesis archives
- Toyota, Woven by Toyota, and TRI press releases

The search for "Travis Millet" author or researcher returned unrelated individuals (Travis Mills the motivational speaker, Travis Lowdermilk at Microsoft Research, Dylan B. Millet in environmental sciences). A YouTube channel exists at the handle `UCB0uer5_yWNPV7q58I8mITQ` under the name "Travis Millet" but the channel page would not render substantive content through web fetch. There is no indication this channel is professional or related to Toyota.

### 2.2 Interpretation

Travis has a low-signal public footprint on purpose or by disposition. This is common for operations leaders in automotive OEM settings, where engineering managers are generally not incentivized to build public profiles the way ML research leads are. Colin should not interpret the absence of publications as evidence of low technical depth. In fact, the triage operations role at scale in AD/ADAS is technically demanding but not publication-producing.

---

## 3. Publicly Visible Positions on Data Operations, Labeling, HITL, ML Training Data Quality

### 3.1 No Direct Positions Are Public

Travis has made no public statements this research could identify on AV data operations, labeling workflows, human-in-the-loop systems, or ML training data quality. There are no blog posts, talks, or quoted statements from him in any of the Woven by Toyota, Weights and Biases, Union.ai, or Microsoft customer stories that document the AutoTriage and adjacent systems he presumably touches.

### 3.2 Inferred Positions from the Technical Environment He Operates In

What can be reliably inferred from published Woven by Toyota material is the **technical environment** Travis's team supports. These positions are not Travis's own, but they define the assumptions he almost certainly brings to the call:

**AutoTriage (Woven by Toyota's published triage automation product).** Per the Weights and Biases customer story, Woven by Toyota operates a human-triage workflow in which engineers review driving log videos to identify root causes of perception or planning failures. AutoTriage is their GenAI-powered automation layer that cut ADAS triage workload by approximately 50 percent using two multimodal LLMs with human-in-the-loop, achieving over 80 percent classification accuracy and saving roughly 34,000 engineer-hours and $2.2 million. The project is publicly led by **Suigen Koide**, Head of DevBoost (Generative AI and MLOps), ADAS, not by Travis. Inferred: Travis's Technical Operations Engineering function is one of the internal customers or downstream operators of AutoTriage, since "triage operations" is the domain AutoTriage automates. The scope of his incoming SOW for three to four people should be read in that context. Woven has already absorbed roughly half the ADAS triage workload into GenAI; the human work that remains is either the harder residual or the labeling and quality layer that feeds the GenAI system.

**Triage Manager role as published.** A Lever-hosted job description for a Woven by Toyota Triage Manager establishes these team parameters publicly: approximately seven Core Triagers, reporting to a Senior Manager, Triage Operations, partnering with Release Operations and Vehicle Operations, operating on triage SLAs and a quality bar. Responsibilities include bug hygiene (deduplication, linking incidents to issues, validating countermeasures), cross-functional prioritization (release blockers versus milestone blockers, technical bug scrubs, KPI reviews), people management, and process metrics (time to triage, accuracy, reoccurrence rates). Tooling referenced is Python-based in-house tooling, re-simulation workflows, incident-to-issue linking, and auto-triage prototypes. Required qualifications: five plus years in AD/ADAS, robotics, or safety-critical software operations; two plus years of leadership; expert root-cause analysis using structured methods (fishbone, 5 Whys). This JD is probably for a role **adjacent to Travis** or reporting into him. Flagged as inferred. The Triage Manager JD was crawled through a search snippet since the direct Lever page returned 403.

**Dataset Governance Policy (DGP) and annotation pipeline.** Woven Alpha engineers Akira Wakatsuki, Takaaki Tagawa, Yusuke Yachide, and Yuta Tsuzuki published a 2021 Medium post describing a three-phase annotation pipeline (receive target data, request annotations from vendors, deliver results) that reduced manual operations by approximately 90 percent. The Dataset Governance Policy was jointly developed with TRI and is open source. Inferred: if Travis's TRI role as Senior Triage Operations Lead overlapped this period (2020 to 2022), he was likely adjacent to or downstream of DGP. This is inference based on timing and the explicit TRI and Woven Alpha co-development statement, not a direct claim.

**W&B Weave, Union.ai, and Azure OpenAI.** Woven by Toyota's public stack for AI development includes Weights and Biases Weave (experiment tracking and evaluation for AutoTriage), Union.ai (workflow orchestration, migrated from open-source Flyte in 2023, spanning annotation through training), and Azure OpenAI (automating approximately 80 percent of software code safety fixes, per a Microsoft customer story). These are the vendor sets Travis's team interoperates with.

### 3.3 Relevance to BayOne's Positioning

Colin should assume Travis works in an environment where:

- Human-in-the-loop with LLM pre-classification is the explicit strategic direction, not an experiment. Travis is not a skeptic of GenAI-in-the-loop; he is operating under leadership that has published on it.
- Throughput and cost economics are measured and reported (34,000 hours, $2.2 million, 80 percent accuracy, 50 percent workload reduction are all public numbers). A BayOne proposal should speak in the same units.
- The platform layer is already built: Union.ai, W&B Weave, in-house Python tooling. BayOne is unlikely to be asked to build platform. The incoming SOW for three to four people almost certainly covers **human triage capacity, quality, or residual labeling work** rather than tooling.
- TRI collaboration is a real organizational thread. Travis's prior title at TRI suggests he still has cross-organization relationships.

---

## 4. Signals About His Team at Woven

### 4.1 Directly Stated

- Reporting up: Travis reports to Steve Lauziere (The Org).
- Peer engineering managers under Lauziere: at least nine named peers (see Section 1.2).
- Triage function sizing: a peer Triage Manager role manages approximately seven Core Triagers reporting to a Senior Manager, Triage Operations (Lever JD snippet). Flagged: this is for a role adjacent to Travis, not necessarily his own team.
- Published Woven by Toyota triage practitioners visible publicly include Trisha Acuna (Triage Operations Specialist), Bharjoban Sandhu (Triage Operations Lead), Kenta Kumazaki (Lead of Product Triage), and Kimlyn Huynh (Technical Operations Manager).

### 4.2 Inferred

Travis's own team size and composition are not publicly stated. The Lever job posting for Triage Manager with seven Core Triagers gives a plausible anchor for one sub-team in the function, but Technical Operations Engineering is likely broader than a single triage squad. If Travis is the Manager of Technical Operations Engineering for AD/ADAS in the US, and a Senior Manager Triage Operations role also exists per the Triage Manager JD, then there are at least two management layers in the triage and technical operations function. The incoming SOW for three to four people is most plausibly an augmentation or backfill inside his existing function rather than a net-new capability stand-up.

### 4.3 Openings, Hires, Departures

No named personnel departures or recent hires into Travis's direct team were identifiable through this research. Woven by Toyota underwent layoffs in summer 2023 (per Blind and LinkedIn farewell posts from affected employees such as Richard Wimmer), and the broader Toyota and Woven by Toyota organization announced a joint restructuring to accelerate software implementation in 2023. These are background conditions, not specific to Travis's team.

The Lever job board lists multiple current Woven by Toyota openings relevant to the AD/ADAS triage and data platform stack, including Triage Manager, Senior Site Reliability Engineer (Data Infrastructure, AD/ADAS), Senior Data Scientist (ADAS Strategy), Data Platform Senior Software Engineer (Enterprise AI), Senior Engineering Manager (Tools Engineering), and Senior Technical Project Manager (ADAS/Autonomy, Ann Arbor). Hiring posture is consistent with continued investment in the AD/ADAS operations and tooling stack.

---

## 5. Public Commentary on BayOne-Comparable Vendors

No public commentary from Travis on any vendor, staffing firm, managed services provider, BPO, or labeling services vendor could be identified. The Woven by Toyota engineering blog and customer stories name their tool vendors (Weights and Biases, Union.ai, Microsoft Azure OpenAI, Applied Intuition in adjacent industry coverage) but do not name labor-side partners.

For Colin: this is an information gap worth asking about in discovery. Whether Woven currently uses a staffing partner, a BPO for triage labor, or a managed testing vendor, and what they think of them, is probably the most important unknown this research cannot close from public sources.

---

## 6. How Travis Thinks and Decides (Inferred)

There is not enough direct public material to profile Travis's decision style. The following are structural inferences based on his career shape and context, not direct claims:

- **Safety-critical operations disposition.** Twelve-plus years across F-16 flight test, TRI triage, and Woven technical operations reflects a consistent orientation toward operational rigor in safety-critical systems. Colin should expect Travis to value process discipline, repeatability, documentation, and evidence-based reasoning over speed or novelty.
- **Triage as a discipline, not a chore.** The TRI title "Senior Triage Operations Lead" is specific. Triage is Travis's identified professional discipline, not a general operations background he happens to have. He will likely be conversant with industry triage frameworks (the published Woven material references structured root-cause methods such as fishbone diagrams and 5 Whys).
- **Manager rather than IC.** The move from "Lead" to "Manager" title indicates a deliberate management track. He is likely to evaluate a vendor partnership on team-scaling, capacity, and reliability terms rather than on specific technical approach.
- **Connected to TRI research culture but not in it.** His TRI tenure puts him adjacent to Dataset Governance Policy development, ML Recognition, and other TRI-ML research directions, but his title places him on the operations side of that boundary. He likely has strong working relationships with ML research engineers without being one.

No public material supports or contradicts a position on build-versus-buy, onshore-versus-offshore staffing, or proprietary-versus-open-source tooling. These remain open.

---

## 7. Open Questions Web Research Could Not Answer

1. What is the actual size and composition of Travis's direct team at Woven by Toyota today?
2. Is the incoming SOW for three to four people an augmentation of an existing triage squad, backfill for departures or layoffs, or a new capability?
3. Does Woven currently use a staffing partner, BPO, or managed services provider for any triage, labeling, or annotation work, and if so who?
4. How does Travis's function interact with AutoTriage day to day? Is his team a consumer, an evaluator, or a data source?
5. Where geographically does Travis want this SOW staffed (Palo Alto, Ann Arbor, remote, offshore)?
6. What is the relationship between Travis's Technical Operations Engineering function and the Senior Manager, Triage Operations role referenced in the Lever JD?
7. What triage metrics does Travis's team already track and target? Public material mentions time to triage, accuracy, reoccurrence or validation rates, but not his specific KPIs.
8. How has his team been affected by the 2023 to 2024 Woven and Toyota restructuring?
9. Does he have a stated preference for on-call and operational coverage models (follow-the-sun, regional, surge)?
10. What is the evaluation process and timeline for the incoming SOW, and who else is involved in the decision (Lauziere, the Senior Manager Triage Operations, procurement)?

These are the questions the discovery call should prioritize.

---

## Sources

- Travis Millet LinkedIn profile (URL confirmed via search, direct fetch blocked by LinkedIn): `https://www.linkedin.com/in/travis-millet-b405a64/`
- ZoomInfo profile for Travis Millet (role, title, biography snippet): `https://www.zoominfo.com/p/Travis-Millet/-2040443710`
- The Org, Steve Lauziere org chart page listing Travis Millet as direct report: `https://theorg.com/org/woven-planet-holdings/org-chart/steve-lauziere`
- The Org, top-level Woven Planet Holdings org chart: `https://theorg.com/org/woven-planet-holdings/org-chart`
- Woven by Toyota Triage Manager job description (text via search snippet; direct Lever URL returned 403): `https://jobs.lever.co/woven-by-toyota/dda9dec1-a170-421d-994a-17fc3a09ec4d`
- Woven by Toyota Medium post on large-scale data annotation pipeline and Dataset Governance Policy: `https://woven.toyota/en/our-latest/20210927/` and `https://medium.com/@WovenbyToyota/large-scale-data-annotation-pipeline-with-global-data-governance-policy-in-arene-85af91474842`
- Weights and Biases customer story on Woven by Toyota AutoTriage: `https://wandb.ai/site/customers-new/toyota/` and `https://wandb.ai/site/customers/toyota-agents/`
- Union.ai case study on Woven by Toyota: `https://www.union.ai/case-study/how-woven-by-toyota-saved-millions-with-scaled-autonomous-driving-from-union-ai`
- Microsoft customer story on Woven by Toyota and Azure OpenAI: `https://www.microsoft.com/en/customers/story/24108-woven-by-toyota-inc-azure-openai`
- Toyota global newsroom on Woven Planet formation (2020 to 2021): `https://global.toyota/en/newsroom/corporate/33786527.html`
- Woven by Toyota careers portal: `https://www.woven.toyota/en/careers/` and Lever jobs index `https://jobs.lever.co/woven-by-toyota`
- Suigen Koide LinkedIn (Head of DevBoost, AutoTriage project lead): `https://www.linkedin.com/in/suigen-koide/`
- Peer triage personnel profiles referenced for team context: Trisha Acuna (LinkedIn), Bharjoban Sandhu (ZoomInfo), Kenta Kumazaki (LinkedIn), Kimlyn Huynh (LinkedIn)
