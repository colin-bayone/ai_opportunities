# 09a - Technology Inventory: Master Synthesis

**Source:** Synthesis of four Part files (09a_tech_inventory_part1 through part4) covering all source transcripts and deliverables from 2026-03-12 through 2026-04-16
**Source Date:** 2026-03-12 through 2026-04-16 (inclusive)
**Document Set:** 09a (supplementary to Set 09 — comprehensive tech inventory for Mikhail/Daniel email response and tech-access working session)
**Pass:** Consolidated, deduplicated master synthesis across all Part files

---

## Executive Summary

This document is the single authoritative inventory of every technology, system, library, model, platform, internal tool, reference dataset, methodology, vendor, and compliance framework referenced across the Lam Research IP Protection engagement from first contact (2026-03-12) through Mikhail Krivenko's tech-access question (2026-04-16). It is built by deduplicating and reconciling four prior Part files that each covered a different source corpus (March discovery materials, April internal syncs + Mikhail's email, the April 6 client meeting with Brad/Mikhail/Daniel, and BayOne's client-facing deliverables).

It serves two downstream purposes: (a) drafting an email response to Mikhail answering "what specific technologies would you need access to?" and (b) prepping a working session between Colin Moore (BayOne) and Daniel Harrison (Lam) to coordinate access provisioning. The structure reflects that: a full inventory for completeness, then a distilled Access Request List that maps directly onto the categories Lam IT will need to action.

**Total technologies catalogued:** approximately **175 distinct items** after deduplication (down from ~415 raw mentions across the four Part files).

**Top 5 categories by volume of mentions:**
1. Microsoft / Azure Ecosystem (~25 distinct items — Azure AI Foundry, Purview, Blob Storage, AI Search, Cosmos DB, PostgreSQL+pgvector, Sentinel, Teams, Copilot, Custom SITs, DLP, etc.)
2. Methodology / Algorithms (~22 items — layered detection, EDA, reconciliation, MoE, regex, deterministic, transfer learning, etc.)
3. Pre-trained Models / LLMs (~15 items — GPT-4.0, Claude, Gemini, IBM models, SLMs, Azure-hosted models, LamGPT, Flair, sentence transformers, etc.)
4. Lam Internal Tools / Systems (~15 items — Escalation Solver, ASM, MABC, Milux/Orion, COS, GSNO/GFSO, work-center identity, acronyms list, etc.)
5. Reference Data / Lists / Datasets (~14 items — acronyms list, customer list, fab list, exclusion list, thumbs-up/down labels, five free-text fields, etc.)

**Key callouts:**

- **What Lam already has:** Azure ecosystem (mixed on-prem + cloud, plus a partially-spun-down prior-project Azure environment still reachable), Microsoft Teams + auto-transcription attached to tickets, Microsoft Copilot, LamGPT (internal GPT-based system — referenced in Part 1 only; NOT confirmed in Part 3), Escalation Solver application (homegrown) with built-in thumbs-up/thumbs-down UI capturing ~1,000 existing feedback labels, ASM access control, in-progress IAM program (~2 years in), TRI-badge system, six-plus fragmented search systems, reference datasets (acronyms ~3,000 items, customer list, fab list, exclusion list), hourly data-retrieval ETL jobs from the prior effort.

- **What Lam tried and abandoned/paused in the 18-month prior effort:** Presidio (starting point, 12 candidate models narrowed to 3), spaCy NER, Hugging Face Transformers (Flair was the finalist pick), Azure AI model (swapped in late), rule-based matching, parallel-reconciliation algorithm (modified Mixture-of-Experts), fine-tuning on sentence transformers (probably), MLOps pipeline on Azure, on-prem Kubernetes deployment for non-Azure models. Achieved 21% → 17% false positive rate, ~90% accuracy — short of the sub-5% MVP target and sub-1% end-state target. ~1,000-person-hour labeling effort deemed cost-prohibitive; no true golden set was ever created.

- **What BayOne is bringing:** Layered Detection Methodology (deterministic → ML/NLP → Generative AI, sequential), Hybrid Architecture for Intelligent IP Protection (named in deliverable), Ingestion-First Architecture, Unified/Common Data Plane concept, Defined Repeatable Evaluation Protocol, Detection Target Map, Accuracy Ceiling determination, EDA methodology (20,000-sample benchmark, class separability analysis), tiered labeling taxonomy, asynchronous-queue-with-synchronous-UX pattern, BayOne V1 internal labeling tool (referenced by Pat), and Colin's reference architecture from Coherent Corp (40,000 users, 3 years in production, also deployed to aerospace/defense).

- **What Lam must provision for the POC:** environment access (VM or equivalent under Option A) + Escalation Solver data (five free-text fields, 4,000-5,000 chars each) + reference lists (customer names, fab/location identifiers, exclusion list including the ~3,000-item acronyms set) + access to the existing thumbs-up/down label set (~1,000 examples) + prior-effort documentation (baseline metrics, model selection history) + a Lam-sanctioned LLM endpoint (Azure AI Foundry is the named target) + LAM ID accounts for Colin + one BayOne engineer + Python/Jupyter/Git tooling + SME time for detection-target definition and validation.

- **Critical path:** **To start the POC on the week of 2026-05-04, Lam must provision (a) environment access (VM) with Python 3.10+ and standard NLP tooling, (b) the Escalation Solver five-free-text-field export plus the customer/fab/exclusion reference lists, and (c) LAM ID accounts with Azure AI Foundry endpoint access, by end of the week of 2026-04-27 — SLW paperwork (~1 week) and Lam account provisioning should be initiated immediately (this week).**

---

## 2. Consolidated Inventory

### 2.1 Compute / Hosting / Infrastructure

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Azure (general cloud) | Lam HAS; BayOne REFERENCES | Part 1 (Mikhail, Colin), Part 2, Part 3 (Mikhail), Part 4 | Lam's primary cloud target; BayOne's recommended unification platform. Access-critical. |
| Azure AI Foundry | Lam HAS (on paper per prep); Lam WANTS; BayOne COMMITTED; BayOne REFERENCES | Part 1 (PREP, CALL, TECH1-3), Part 2 (Colin), Part 3 (Colin, Mikhail as "Azure AI"), Part 4 (preliminary_approach, discovery_followup) | Recommended AI hosting/compute platform; named in client-facing deliverables. Access-critical for Layer 3. |
| On-prem servers / Lam data center | Lam HAS | Part 1 (Mikhail), Part 2 (Daniel), Part 3 (Mikhail line 155), Part 4 | Lam's definition: "running on the server at our data center." Out of POC scope as primary target; supportable by architecture. |
| Hybrid deployment model | Lam HAS; BayOne REFERENCES | Part 1, Part 3 (Colin line 147), Part 4 (discovery_followup) | Lam's current-state reality; BayOne can support. Informational. |
| Kubernetes (on-prem) | Lam TRIED | Part 3 (Mikhail line 75-76) | Deployment platform for the prior 18-month NER effort (non-Azure models). Informational — may hold deployed artifacts worth recovering. |
| Virtual Machine (VM) | COMMITTED (Option A) | Part 4 (engagement_pricing, poc_proposal) | Named execution environment under Option A. **Access-critical.** |
| Virtual desktops / AVD | Lam HAS | Part 2 | Known performance/reliability issues per Daniel. Informational. |
| MLOps pipeline (on Azure) | Lam TRIED | Part 1 (Mikhail), Part 4 (problem_restatement) | Used for training the prior three models. Artifacts potentially reusable. |
| Prior-project Azure environment (partially spun down) | Lam HAS | Part 3 (Mikhail line 148) | Still reachable; hourly retrieval jobs disabled but environment up. **Access-critical if we want prior artifacts.** |
| Cloud-first roadmap / microservice architecture | Lam WANTS | Part 1 (Mikhail), Part 4 | Aspirational. Informational. |
| Edge AI / Edge devices / Air-gapped customer fabs | Lam WANTS (future) | Part 2 (Daniel), Part 3 (Daniel line 150-157) | Out of POC scope. Daniel raised it; Colin pushed back (SLMs only justified on-prem). Informational. |
| Clean room / customer-resident environments | Lam HAS (operational) | Part 3 (Brad, Daniel) | Explicitly out of POC scope. Informational. |
| Hyperscalers (generic cloud) | BayOne REFERENCES | Part 3 (Colin line 161) | Generic reference. Informational. |
| Cloud bots | Lam HAS | Part 1 (Mikhail) | Unspecified cloud-hosted bot systems. Informational. |
| Auto-scaling (Azure capability) | BayOne REFERENCES | Part 4 (discovery_followup) | "Why Azure" talking point. Informational. |
| Asynchronous queue (processing architecture) | BayOne COMMITTED | Part 1, Part 4 (preliminary_approach) | Named processing pattern. Methodology. |
| GPU (local training) | Lam TRIED (speculated) | Part 1 (Colin TECH1) | Colin's hypothesis about prior work. Informational. |
| AWS / GCP | UNKNOWN / NEEDS CLARIFICATION | Part 1 (PREP only) | Not in play per all sources. Informational. |

### 2.2 Data Storage / Databases / Data Lakes

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Data lake (absence of) | Lam does NOT HAVE | Part 1 (Mikhail), Part 4 | Current state gap. Informational. |
| Azure Blob Storage | BayOne COMMITTED; BayOne REFERENCES | Part 1 (Colin TECH1-2), Part 2, Part 4 (preliminary_approach) | Named for document storage in unified data plane. Access-critical if storage architecture falls to POC scope. |
| Azure AI Search (formerly Cognitive Search) | BayOne REFERENCES | Part 1 (Colin TECH2), Part 4 (preliminary_approach) | Default vector search; pgvector named as alternative. Access-critical if selected. |
| Azure Cosmos DB | BayOne REFERENCES | Part 1 (Colin TECH2) | Control-plane option. Informational for POC. |
| Azure PostgreSQL + pgvector | BayOne REFERENCES (fallback option) | Part 1 (Colin TECH2), Part 4 (preliminary_approach) | Custom alternative to Azure AI Search. Access-critical if chosen. |
| Vector databases / vector stores (generic) | BayOne REFERENCES | Part 1, Part 4 | General RAG embedding component. Methodology. |
| Escalation Solver data — structured + unstructured | Lam HAS (target data) | Part 3 (Mikhail line 40), Part 4 | Application data including free-text fields and attachments. **Access-critical.** |
| Escalation Solver attachments | Lam HAS | Part 3 (Mikhail line 44) | Future capability; not POC scope. Informational. |
| Hourly data retrieval jobs (ETL from source systems) | Lam HAS (disabled) | Part 3 (Mikhail line 149) | Prior-project batch jobs; currently paused but environment up. Informational / potentially reusable. |
| SharePoint / OneDrive | Lam HAS (likely) | Part 1 (PREP, FINAL) | Likely data sources; unconfirmed at Lam. Informational. |
| SQL databases (generic) | Lam HAS | Part 2 | Implied internal systems. Informational. |
| Knowledge management systems (Brad's org) | Lam HAS | Part 1, Part 2 | Brad's domain includes multiple KM systems. Informational. |
| Knowledge bases (target repositories) | Lam HAS / WANTS | Part 4 | Downstream consumers of cleaned content. Informational. |
| Six-plus search systems / segmented search tools | Lam HAS | Part 1 (Mikhail, TECH3), Part 4 | Fragmented current state. Informational. |
| Live data sources / databases / APIs | Lam HAS | Part 4 (preliminary_approach) | Detection targets at query time. Informational for future scope. |
| Tool data / recipe / yield data (fab-resident) | Lam HAS | Part 3 (Daniel line 158) | Sensitive fab IP categories. Out of POC scope. |
| Tool file (structured fab data) | Lam HAS | Part 3 (Daniel line 160) | Easily segregated. Out of POC scope. |
| Segmented / fragmented databases | Lam HAS | Part 1 (Mikhail) | Current state. Informational. |
| Oracle back-end | UNKNOWN / NEEDS CLARIFICATION | Part 1 (Colin hypothetical question) | Not confirmed. Informational. |
| Unified / Common Data Plane | BayOne COMMITTED | Part 1 (Colin TECH1-3, FINAL), Part 4 | Named BayOne architectural concept. Methodology. |

### 2.3 Programming Languages / Runtimes

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Python | BayOne REFERENCES; BayOne BRINGS | Part 2 (Colin), Part 3 (Colin line 174) | Core POC language. **Access-critical** (need Python 3.10+ on POC VM). |
| .NET / .NET Core | Lam HAS | Part 2 (April 1 call) | "Text that they're using is the dotnet column" — Lam knowledge-management stack. Informational. |
| C# | Lam HAS (implied) | Part 2 | Implied via .NET. Informational. |

### 2.4 NLP / NER Libraries / Frameworks

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| spaCy | Lam TRIED; BayOne REFERENCES for POC | Part 1 (Mikhail), Part 3 (Mikhail, Colin line 185-188), Part 4 | Failed out of the box in prior effort; still a useful building block. **Access-critical** (must be installable on POC VM). |
| Presidio (Microsoft PII framework) | Lam TRIED; BayOne REFERENCES | Part 1 (PREP), Part 3 (Mikhail line 51) | Starting point for prior effort (12 models narrowed to 3). **Access-critical** (BayOne will reuse; must be installable). |
| Flair (NLP library) | Lam TRIED | Part 3 (Mikhail line 52, 155) | One of three finalists in prior effort; the Hugging Face pick. **Access-critical** if benchmarking against prior baseline. |
| Hugging Face Transformers library | Lam TRIED; BayOne REFERENCES | Part 1, Part 3 (Mikhail, Colin line 153) | Model source for prior effort; Colin is an active contributor. **Access-critical** (must be installable; pre-downloaded weights if air-gapped). |
| Sentence Transformers | Lam TRIED (Colin hypothesis); BayOne REFERENCES | Part 1 (Colin TECH1), Part 3 (Colin line 181, 188) | On-prem-hostable NLP option. **Access-critical** (installable on POC VM). |
| Transformers architecture (generic) | BayOne REFERENCES | Part 1, Part 3 (Colin line 188), Part 4 | Architectural backbone of most models. Methodology. |
| TF-IDF | BayOne REFERENCES | Part 3 (Colin line 181) | Classic NLP baseline; on-prem friendly. Methodology. |
| Regex / rule-based pattern matching | BayOne COMMITTED (Layer 1) | Part 1, Part 2, Part 3 (Colin line 174), Part 4 | Deterministic-layer component. Methodology; must run in Python. |
| Named Entity Recognition (NER) — generic | Lam TRIED; BayOne REFERENCES | Part 1, Part 3, Part 4 | Category. Methodology. |
| NLTK, Stanza, Stanford NER | Not mentioned | — | Not in play. |

### 2.5 Machine Learning / Deep Learning Frameworks

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Transformers (model / architecture) | Lam TRIED; BayOne REFERENCES | Part 1 (Mikhail), Part 3, Part 4 | One of three prior finalists; also the "wrong tool for deterministic lookup" per Colin. **Access-critical** (installable). |
| Hugging Face (platform) | Lam TRIED; BayOne REFERENCES | Part 3 (Mikhail line 52, Colin line 153) | Model registry source. Informational / access-critical if pulling models. |
| Mixture of Experts (MoE) — Mistral MoE reference | Lam TRIED (modified take); BayOne REFERENCES | Part 3 (Colin line 182) | Prior parallel-reconciliation pattern. Informational. |
| Custom ML models (generic) | Lam TRIED | Part 1, Part 4 | Category. Informational. |
| Small Language Models (SLMs) | Lam WANTS (Daniel); BayOne REFERENCES | Part 2, Part 3 (Daniel, Colin line 152-153) | Daniel pushed; Colin pushed back (cloud-more-expensive argument). Informational. |
| Rule-based models | Lam TRIED | Part 1 (Mikhail), Part 2 | Abandoned over spelling variations. Informational. |
| scikit-learn | BayOne REFERENCES | (Category prompt / Colin's toolkit) | Standard Python ML. **Access-critical** (installable). |
| pandas, numpy | BayOne REFERENCES | (Standard Python ML toolkit) | **Access-critical** (installable). |
| PyTorch, TensorFlow | Not explicitly mentioned | — | Likely underlying Transformers; installable. Informational. |
| Machine Learning (as general category) | Lam HAS experience with | Part 1 (Mikhail), Part 4 | Policy preference was ML over Gen AI. Informational. |

### 2.6 Pre-trained Models / LLMs / Specific Model Names

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| GPT-4.0 / GPT models (generic) | Lam HAS (via Copilot); BayOne REFERENCES | Part 1 (Colin, Mikhail), Part 2, Part 3 (Colin line 71), Part 4 (problem_restatement.md) | Via Copilot/LamGPT. Access-critical for Layer 3 methodology — requires endpoint access. |
| ChatGPT (as product reference) | BayOne REFERENCES | Part 1 (Colin, PREP Samsung incident), Part 3 (Colin) | Industry baseline & shadow-AI risk reference. Informational. |
| Claude (Anthropic) | BayOne REFERENCES | Part 1 (PREP, shadow AI), Part 3 (Colin line 62, 71) | Enterprise LLM option accessible via Azure AI Foundry. Informational / alternative Layer 3 endpoint. |
| Anthropic (as vendor/API) | BayOne REFERENCES | Part 1 (Mikhail), Part 3 (Colin line 62) | Named enterprise LLM option. Informational. |
| OpenAI (as vendor/API) | BayOne REFERENCES | Part 1, Part 3 (Colin line 62) | Named enterprise LLM option. Informational. |
| Gemini (Google) | BayOne REFERENCES (excluded) | Part 3 (Colin line 71, 100) | Explicitly NOT in Azure AI Foundry; Colin aware of Gemini training. Informational. |
| Grok | Lam HAS (Azure-native availability) | Part 2 (Colin) | Available via Azure. Informational. |
| LamGPT | Lam HAS (per Part 1); UNKNOWN / NEEDS CLARIFICATION (Part 3 silent) | Part 1 (Mikhail, Colin TECH1) — **NOT confirmed in Part 3** | Internal GPT-based system — mentioned only in Part 1. Flag for confirmation with Daniel. |
| Microsoft Copilot / Microsoft 365 Copilot | Lam HAS | Part 1 (Mikhail, Colin, PREP) | Lam ecosystem; Purview can block Copilot from labeled content. Informational. |
| GitHub Copilot | UNKNOWN / NEEDS CLARIFICATION | Part 1 (PREP discovery question) | Not confirmed. Informational. |
| IBM models | BayOne REFERENCES | Part 3 (Colin line 188) | Exception to Transformers-backbone. Informational. |
| "Azure AI model" (unspecified) | Lam TRIED | Part 1 (Mikhail), Part 3 (Mikhail line 53), Part 4 | One of prior three finalists; Lam unclear on exact identity. Needs clarification. |
| "Globally pre-trained foundations" (generic) | Lam TRIED (as base for fine-tuning) | Part 4 (problem_restatement) | Generic reference to pre-trained bases. Informational. |
| 12 Presidio-family candidate models (narrowed to 5, then to 3) | Lam TRIED | Part 3 (Mikhail line 51) | Prior model down-selection. Informational. |
| BERT, RoBERTa, Llama, Mistral | Not explicitly named | — | Mistral named only via MoE reference. Informational. |
| PyRIT (Microsoft red-teaming), Nvidia Garak, F5 AI Red Team | BayOne REFERENCES | Part 1 (PREP only) | Prep-doc references; not discussed with Lam. Informational. |

### 2.7 Generative AI Services / APIs

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Azure OpenAI (old name for Azure AI Foundry) | BayOne REFERENCES | Part 1, Part 2, Part 3 (Colin line 70) | Former name; now Azure AI Foundry. Informational. |
| Azure AI Foundry | See 2.1. **Access-critical for Layer 3.** | | |
| Anthropic API | BayOne REFERENCES | Part 1, Part 3 (Colin line 62) | Named option. Alternative Layer 3 endpoint. |
| OpenAI API | BayOne REFERENCES | Part 1, Part 3 (Colin line 62) | Named option. Alternative Layer 3 endpoint. |
| External API calls (generic) | BayOne REFERENCES (avoid) | Part 2 (Colin) | 20x more expensive than Azure-native; Colin's preference is Azure AI Foundry. Informational. |
| Generative AI (category/layer) | Lam has NOT used; BayOne COMMITTED (Layer 3) | Part 1 (Mikhail), Part 4 (all pricing/proposal docs) | Named in deliverables as Layer 3. **Access-critical methodology component.** |
| Prompt engineering | BayOne REFERENCES | Part 4 (problem_restatement) | Technique. Methodology. |
| RAG chatbot / Retrieval-Augmented Generation | BayOne REFERENCES | Part 1 (Colin TECH1, DEBRIEF) | Colin's reframing of Lam's use case. Methodology. |
| Agentic AI | BayOne REFERENCES | Part 1 (Colin TECH2, TECH3, STRATEGY) | Cleaning/tooling capability. Methodology. |
| Cloud-based bot services / Q&A systems | Lam HAS (landscape) | Part 4 | Downstream consumers of unified data plane. Informational. |
| AWS Bedrock, Google Vertex AI, Cohere API | Not mentioned | — | Not in play. |

### 2.8 Applications (Lam Internal — POC targets and context)

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| **Escalation Solver** (homegrown escalation mgmt app) | Lam HAS (POC TARGET) | Part 1 (Mikhail, Brad), Part 2, Part 3 (Mikhail line 40-48), Part 4 (all pricing/proposal) | Primary POC target. Five free-text fields, 4,000-5,000 chars each. Entity targets: customer name + fab identifier. **Access-critical.** |
| Redaction Service (standalone from prior effort) | Lam HAS | Part 3 (Mikhail line 50-51) | Standalone service built independent of any app; accepts text and returns detection or redacted text. **Access-critical if benchmarking.** |
| Thumbs-up/thumbs-down labeling UI | Lam HAS | Part 3 (Mikhail line 105, 166), Part 2 | Existing UI capturing human validation; ~1,000 label points. **Access-critical** — this is the closest thing Lam has to a labeled dataset. |
| Self-help search / Q&A application | Lam HAS / WANTS | Part 1 (Mikhail), Part 3 (Colin line 18-19) | One of the two use-case families. Future scope; informational for POC. |
| Ask-for-help / community Q&A flow | Lam HAS | Part 1 (Mikhail), Part 3 (Colin line 19) | Second use-case family. Future scope. |
| Six search formulas / six-plus search systems | Lam HAS | Part 1 (Mikhail), Part 4 | Fragmented current state. Informational. |
| Engineering system (drawings and schematics) | Lam HAS | Part 1 (Brad) | Brad's context. Informational. |
| Field engineer work-order system / installed-maintenance-upgrade workflow | Lam HAS | Part 3 (Mikhail line 42) | Upstream feeder for escalations (8-hour SLA → escalation petition). Informational. |
| Engineering design change system / procedure change system / tech articles | Lam HAS | Part 3 (Mikhail line 41) | Downstream actions from escalation closure reports. Informational. |
| Knowledge management / Knowledge Enablement applications | Lam HAS | Part 2 | Brad's org. Informational. |
| Generic applications (30+) | Lam HAS | Part 2 | Landscape reference. Informational. |

### 2.9 Lam Internal Tools / Systems

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| **ASM — Application Security Manager** (Escalation Solver security stack) | Lam HAS | Part 1 (Brad), Part 3 (Mikhail line 40), Part 4 | Access control in Escalation Solver profiles. **Informational but access-critical if POC needs role provisioning inside Escalation Solver.** |
| Ticketing system (unnamed, not ServiceNow per Part 3) | Lam HAS | Part 1, Part 4 | Customer segmentation enforced at customer level. Informational. |
| Knowledge management systems (Brad's org) | Lam HAS | Part 1 (Brad) | Multiple systems under Brad's domain. Informational. |
| TRI / trade-restricted-employee flagging | Lam HAS | Part 1 (Brad), Part 4 | Colored-badge system. Informational. |
| Licensed Service Provider (LSP) designation | Lam HAS | Part 1 (Brad) | Contractor/role classification. Informational. |
| Lam "blue badge" employee artifact | Lam HAS | Part 1 (Brad) | Identity artifact. Informational. |
| Work-center-based identification | Lam HAS | Part 1 (Brad), Part 4 | Identity attribute. Informational. |
| **LAM ID** (Lam identity/credential) | Lam HAS (needs provisioning for BayOne) | Part 3 (Colin line 192) | Everyone on the call had a LAM ID except Colin. **Access-critical — BayOne needs ~2 LAM IDs provisioned.** |
| **Lam acronym list (~3,000 items)** | Lam HAS | Part 3 (Mikhail line 80), Part 2 | Loaded into prior NER pipeline. **Access-critical — reference data for POC.** |
| **Customer name list** | Lam HAS | Part 1 (Colin recommendation), Part 3 (Mikhail line 80-81), Part 4 | Reference data. **Access-critical.** |
| **Fab / location identifier list** | Lam HAS | Part 1, Part 3 (Mikhail line 81), Part 4 | Reference data. **Access-critical.** |
| **Exclusion list** (customers removed from acronyms) | Lam HAS | Part 3 (Mikhail line 80), Part 4 | Content approved for general sharing. **Access-critical.** |
| MABC / MA Data Center / E10 data / "big EI project" | Lam HAS | Part 3 (Mikhail line 157-158) | Existing fab-data-out initiative. Informational. |
| Milux / Orion (internal teams) | Lam HAS | Part 3 (Daniel line 202) | Internal teams with IT capacity; currently committed to COS. Informational. |
| COS (Orion's current project) | Lam HAS | Part 3 (Daniel line 202) | Supercritical project consuming Orion capacity. Informational. |
| GSNO / GFSO (Brad's org) | Lam HAS | Part 1 (Brad), Part 3 (Brad line 11, Mikhail line 76-77) | Organizational unit. Informational. |
| Knowledge and Advanced Services teams | Lam HAS | Part 1 (Brad), Part 3 (Mikhail line 77) | Prior-project team. Informational. |
| JIRA / Confluence / ServiceNow | NOT explicitly mentioned / UNKNOWN | — | Likely present; not confirmed. |
| Internally hosted AI tools (generic) | Lam HAS | Part 4 (problem_restatement) | Category reference including GPT-models-in-Lam-infra. Informational. |

### 2.10 Identity / Access / Security Systems

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| IAM (Lam's in-progress program, ~2 years in) | Lam HAS (in progress) | Part 1 (Brad, Anuj), Part 4 | Not yet enterprise-wide. Informational. |
| RBAC (Role-Based Access Control) | Lam HAS (via IAM); BayOne REFERENCES | Part 1 (Colin DEBRIEF), Part 4 (discovery_followup) | Azure-native. Informational. |
| Zero-trust posture (Jason Callahan, Lam CISO) | Lam HAS | Part 1 (PREP) | Stated CISO posture. Informational. |
| Restricted / colored badges | Lam HAS | Part 1, Part 4 | Identity artifact. Informational. |
| NDA / confidentiality agreements (existing between BayOne and Lam) | Lam HAS | Part 2, Part 3 (Mikhail line 73), Part 4 (engagement_pricing) | Governs Option B data handling. **Access-critical — confirm existing NDA covers POC scope.** |
| SLW / Statement of Work paperwork | Lam HAS (process) | Part 3 (Brad line 197-198) | ~1 week turnaround. **Access-critical — start immediately.** |
| SSO / VPN / Okta / Active Directory / MFA | UNKNOWN / NEEDS CLARIFICATION | Part 2 (Azure AD implied) | Implied via Azure ecosystem; not named explicitly. Access-critical. |
| Azure AD / Active Directory | Lam HAS (implied) | Part 2 | Implied. Informational. |
| InfoSec / Cybersecurity review | Lam HAS (process) | Part 2 | Required approval channel. **Access-critical — identify InfoSec approval path for Azure AI Foundry LLM usage.** |
| Encryption (philosophical reference) | — | Part 1 (Callahan) | Informational. |
| Customer data-out policy (Lam/customer governance) | Lam HAS | Part 3 (Daniel line 154) | Approval process for fab-side data. Out of POC scope. |
| Clean room policies | Lam HAS | Part 3 (Brad) | Out of POC scope. |
| "No customer confidential information in Escalation Solver" policy | Lam HAS | Part 3 (Mikhail line 48) | The policy the POC enforces. Informational foundation. |

### 2.11 Microsoft / Azure Ecosystem (consolidated — see also 2.1, 2.2, 2.6, 2.7)

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| **Microsoft Purview** | BayOne COMMITTED | Part 1 (PREP, TECH1, TECH3), Part 2 (Colin), Part 3 (Colin line 174-176), Part 4 (preliminary_approach, discovery_followup) | Named in client-facing deliverables as foundation for deterministic layer. **Access-critical if method to be implemented as-promised.** |
| Microsoft Purview DLP | BayOne COMMITTED | Part 1 (PREP, TECH1), Part 4 (preliminary_approach) | DLP policies for detection enforcement. Access-critical. |
| Microsoft Sensitive Information Types (SITs) / Custom SITs | BayOne COMMITTED | Part 1 (PREP, TECH3), Part 4 (preliminary_approach, discovery_followup) | Custom SITs for customer names, fab IDs, variations. Access-critical. |
| Microsoft Sentinel | Lam HAS (per prep) | Part 1 (PREP, DEBRIEF) | SIEM/SOAR; Colin argues misapplied as content detection. Informational. |
| Azure AI Content Safety / Prompt Shields | BayOne REFERENCES | Part 1 (PREP only) | Real-time prompt-injection detection. Informational. |
| Microsoft Defender for Cloud Apps | BayOne REFERENCES | Part 1 (PREP only) | CASB / shadow-AI visibility. Informational. |
| Microsoft Teams | Lam HAS | Part 1 (Mikhail), Part 2, Part 4 (problem_restatement) | **Access-critical for collaboration.** |
| Microsoft Teams meeting transcription | Lam HAS | Part 1, Part 4 | Auto-attached to Escalation Solver tickets. Informational data source. |
| Microsoft Copilot | Lam HAS | Part 1 | Informational. |
| Microsoft 365 | Lam HAS (implied) | Part 1 | Implicit. Informational. |
| SharePoint | Lam HAS (likely) | Part 1 (PREP, FINAL) | Unconfirmed. Informational. |
| Power BI | BayOne REFERENCES (option) | Part 1 (TECH3) | BI integration option. Informational. |
| Azure DevOps | Not explicitly mentioned | — | — |

### 2.12 Third-Party Vendors / Consultants Mentioned

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Accenture | Lam's prior partner | Part 1 (DEBRIEF, TECH3, NEEDS 2.2), Part 2 | Central in the prior-effort autopsy. Informational. |
| Capgemini (transcribed "Gapsium"/"Kaptima") | Lam's prior vendor | Part 1 (DEBRIEF, Anuj) | Prior vendor. Informational. |
| Deloitte | Lam's prior vendor | Part 1 (DEBRIEF, Anuj), Part 2 | Prior vendor. Informational. |
| PwC | BayOne REFERENCES (pricing comparison) | Part 2 | Informational. |
| BayOne Solutions | (Self) | All | Acting vendor. |
| Coherent Corp (Colin's prior employer) | BayOne REFERENCES | Part 1, Part 3 (Colin line 8-10, 184) | Colin's reference architecture (40K users, 3 years in prod, also aerospace/defense). Informational. |
| Raytheon, Northrop Grumman | BayOne REFERENCES (prior-work adjacency) | Part 1 (PREP) | Informational. |
| Samsung (customer + prior incident reference) | Lam customer / Industry reference | Part 1 (PREP), Part 3 (Colin line 90), Part 4 | Named in deliverables as a Lam customer. Informational. |
| TSMC, Intel, Micron, SK Hynix | Lam customers | Part 1 (PREP), Part 2, Part 4 | Named in client-facing deliverables. Informational. |
| Oracle Cloud (customer reference) | BayOne REFERENCES | Part 1 (FINAL) | Colin's prior work analog. Informational. |
| Salesforce (retail customer reference) | BayOne REFERENCES | Part 1 (FINAL) | Colin's prior work analog. Informational. |
| Tableau | BayOne REFERENCES (option) | Part 1 (TECH3) | BI integration option. Informational. |
| Otter.ai | UNKNOWN / NEEDS CLARIFICATION | Part 1 (PREP discovery question) | Shadow-AI probe; unconfirmed. Informational. |
| Cohere (BayOne past engagement) | BayOne REFERENCES | Part 2 (Colin) | "This exact project we did for Cohere." Informational. |
| Cisco (BayOne past engagement) | BayOne REFERENCES | Part 2 (Colin) | $500K SOW example; 3-week GitHub access wait. Informational. |
| Sephora / "Safar" (BayOne past engagement) | BayOne REFERENCES | Part 2 (Colin) | Cisco-client example. Informational. |
| Google (hiring context) | BayOne REFERENCES | Part 2 (Anuj) | Informational. |
| HPE Juniper | BayOne REFERENCES | Part 2 (Pratik) | Informational. |
| Empire / "Empiger" | BayOne REFERENCES (disparaged) | Part 2 (Colin) | Custom-solution vendor. Informational. |
| Oracle (legacy) | BayOne REFERENCES | Part 2 (Colin) | Informational. |
| RoboFlow | BayOne REFERENCES | Part 3 (Colin line 144) | Commercial labeling tool — only for computer vision. Informational. |
| FedRAMP | BayOne REFERENCES | Part 3 (Colin line 152) | Prior on-prem context. Informational. |
| Scale.ai | BayOne REFERENCES | Part 2 | Data labeling company. Informational. |
| "World's largest automaker" | BayOne REFERENCES (future opportunity) | Part 2 (Pratik) | Informational. |
| Prior partner(s) (unnamed in client deliverables) | Lam HAS | Part 4 (information_request) | Deliverable explicitly asks about prior partner without naming them. Informational. |

### 2.13 Reference Data / Lists / Datasets

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Customer name list / synonyms lookup table | Lam HAS | Part 1, Part 3 (Mikhail line 80-81), Part 4 | **Access-critical.** |
| Fab identifier list (Fab11, F11, Micro 11, FAP 11, FAP-11) | Lam HAS | Part 1, Part 3 (Mikhail line 81), Part 4 | **Access-critical.** |
| Lam acronym list (~3,000 items) | Lam HAS | Part 3 (Mikhail line 80) | **Access-critical.** |
| Exclusion list (acronyms minus customer names) | Lam HAS | Part 3 (Mikhail line 80), Part 4 | **Access-critical.** |
| ~1,000 thumbs-up/down label set | Lam HAS | Part 2 (Mikhail), Part 3 (Mikhail line 166) | **Access-critical — closest to labeled dataset.** |
| Five free-text fields (Escalation Solver) — 4,000-5,000 chars each | Lam HAS | Part 3 (Mikhail line 43-48), Part 4 | **Access-critical — POC test corpus.** |
| Customer-confidential-information markers / CI documents | Lam HAS | Part 1 (Mikhail) | Content label. Informational. |
| Customer Identifiable Information (CII) category | Lam HAS (policy) | Part 1 (Mikhail) | Informational. |
| Ground truth / golden-standard dataset (ABSENCE) | Lam does NOT HAVE | Part 1 (NEEDS 2.1, FINAL), Part 3 (Mikhail line 69), Part 4 | Labeling was deemed cost-prohibitive. **Critical gap for POC.** |
| Labeled training data (1,000+ person-hour estimate, abandoned) | Lam TRIED / abandoned | Part 1 (Mikhail), Part 3 (Mikhail line 69), Part 4 | Informational — explains why existing labels matter. |
| Representative data sample (absence of) | Lam does NOT HAVE | Part 1 (Colin TECH2, FINAL), Part 4 (information_request) | Open BayOne ask. **Access-critical for Phase 1.** |
| Sanitized / synthetic representations | BayOne REFERENCES (as alternative) | Part 4 (information_request) | Fallback if real data can't leave. Access-critical alternative. |
| 20,000-sample benchmark (BayOne rule of thumb) | BayOne REFERENCES | Part 3 (Colin line 109) | Methodology. Informational. |
| Problem statement field (one of the five) | Lam HAS | Part 3 (Mikhail line 44-45) | Informational. |
| Acronyms loaded (not labels) in prior training | Lam HAS | Part 3 (Mikhail line 69) | Informational. |
| Real false-positive examples from prior testing | Lam may HAVE | Part 1 (NEEDS 3.2) | Open ask. Access-critical if available. |
| Prior model training artifacts | Lam may HAVE | Part 1 (NEEDS 3.3) | Open ask. Access-critical if available. |
| Customer contractual data-segregation requirements | Lam HAS | Part 1 (NEEDS 3.4) | Open ask. Informational. |
| Written policies for CII handling | Lam HAS | Part 1 (NEEDS 3.4) | Open ask. Informational. |
| ACL / role definitions | Lam HAS | Part 1 (NEEDS 3.4) | Open ask. Informational. |
| Known-offender / user-history list | BayOne REFERENCES (proposed) | Part 1 (TECH3) | Future feature. Informational. |
| Specific entity variations (Fab11, F11, etc.) | Lam HAS | Part 4 | Reference data. Access-critical. |
| Terabytes of data (scale) | Lam HAS | Part 2 | Scale context. Informational. |

### 2.14 Methodology / Algorithms

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Hybrid deterministic + AI architecture | BayOne COMMITTED | Part 1, Part 2, Part 3 (Colin line 176-184), Part 4 | Core BayOne approach. |
| Layered Detection Methodology (3 sequential layers) | BayOne COMMITTED | All Parts | Named in client-facing deliverables. **Core IP.** |
| Deterministic matching (Layer 1) | BayOne COMMITTED | All Parts | Layer 1. |
| ML / NLP layer (Layer 2) | BayOne COMMITTED | All Parts | Layer 2. |
| Generative AI layer (Layer 3) | BayOne COMMITTED | All Parts | Layer 3; requires LLM endpoint. |
| Regex patterns | BayOne COMMITTED (Layer 1 component) | Part 1, Part 2, Part 3 | Methodology. |
| Keyword / entity lookup tables | BayOne COMMITTED | Part 1, Part 4 | Methodology. |
| NER (Named Entity Recognition) | Lam TRIED; BayOne REFERENCES | All Parts | Category. |
| Semantic similarity | BayOne critiques as wrong-tool | Part 1 (Colin TECH1) | Informational. |
| Fine-tuning | Lam TRIED (abandoned); BayOne cautions | Part 1, Part 3 (Colin line 121), Part 4 | 20% → 17% FPR; marginal. |
| Attack Success Rate (ASR) | BayOne REFERENCES | Part 1 (PREP) | Red-team metric. Informational. |
| Red teaming (manual/automated/production monitoring) | BayOne REFERENCES | Part 1 (PREP) | Methodology. Informational. |
| Document-level classification | BayOne COMMITTED | Part 1 (TECH3), Part 4 | Methodology. |
| Async queue with synchronous UX | BayOne COMMITTED | Part 1 (TECH3), Part 4 | Methodology. |
| Ingestion-first architecture / reject-at-ingestion | BayOne COMMITTED | Part 1 (TECH1), Part 4 | Methodology. |
| Application-by-application migration | BayOne COMMITTED | Part 1 (TECH3), Part 4 | Methodology. |
| Day Zero / Day One (milestone-based cleanup) | BayOne REFERENCES | Part 1 (TECH2) | Methodology. |
| Quarantine + human review | BayOne COMMITTED | Part 1 (TECH2), Part 2 | Methodology. |
| Unified control plane pattern / middleware | BayOne COMMITTED | Part 1 (All), Part 4 | Methodology. |
| Metrics & reporting module | BayOne COMMITTED | Part 1 (TECH2-3) | Methodology. |
| Defense in depth / "defensive depth" | BayOne REFERENCES | Part 1 (Colin) | Methodology. |
| OCR (optical character recognition) | Lam HAS (at entry); deferred | Part 1 (Mikhail, Colin DEBRIEF), Part 4 | Out of POC scope. |
| Parallel model reconciliation algorithm | Lam TRIED | Part 3 (Mikhail line 63) | 21% → 17% FPR via reconciliation. Informational. |
| Mixture of Experts (MoE) | BayOne REFERENCES (historical) | Part 3 (Colin line 182) | Informational. |
| Transfer learning | BayOne REFERENCES | Part 3 (Colin line 123-124) | Methodology. Informational. |
| Binary classifier | BayOne REFERENCES | Part 3 (Colin line 107) | Methodology. |
| Exploratory Data Analysis (EDA) | BayOne COMMITTED (Phase 1) | Part 2, Part 3 (Colin line 108, 168), Part 4 | Named in pricing/proposal. **Core Phase 1 activity.** |
| Pre-training / post-training | BayOne REFERENCES | Part 3 (Pat line 114) | Methodology terminology. |
| Ground truth (concept) | BayOne REFERENCES | Part 1, Part 3 (Colin line 98-99), Part 4 | Evaluation concept. |
| ML metrics: F1, accuracy, recall, precision | BayOne REFERENCES | Part 1, Part 2, Part 3 (line 55-56, 130) | Methodology. |
| Data augmentation ("generate known bad from the bad") | BayOne REFERENCES | Part 3 (Colin line 110) | Methodology. |
| Human-in-the-loop / auto-categorization tooling | BayOne COMMITTED | Part 3 (Colin line 143, 164) | BayOne-built. Methodology. |
| Tiered labeling taxonomy (Tier 1 word, Tier 2 word+doc, Tier 3 word+doc+reason) | BayOne COMMITTED | Part 3 (Colin line 169-172) | Methodology. |
| Target metrics (≤5% MVP FPR; ≤1% ultimate FPR; achieved 17% + 90% acc) | Lam / baseline | Part 1, Part 3 (line 61-66), Part 4 | Benchmark. |
| Contextual sensitivity analysis | BayOne COMMITTED | Part 4 (preliminary_approach) | Methodology. |
| Entity lookup tables (config not weights) | BayOne COMMITTED | Part 1, Part 4 | Methodology. |
| Defined Repeatable Evaluation Protocol | BayOne COMMITTED | Part 4 (engagement_pricing, poc_proposal) | Named deliverable. |
| Benchmarking vs prior-effort baseline | BayOne COMMITTED | Part 4 | Phase 2 activity. |
| Scaling path documentation | BayOne COMMITTED | Part 4 | Phase 2 deliverable. |
| Detection Target Map | BayOne COMMITTED | Part 4 (poc_proposal, pricing_breakdown) | Phase 1 deliverable. |
| Accuracy Ceiling determination | BayOne COMMITTED | Part 4 (poc_proposal) | Phase 1 deliverable. |
| Data Quality Report / Assessment | BayOne COMMITTED | Part 4 | Phase 1 deliverable. |
| Outcome-based / fixed-price pricing | BayOne COMMITTED (commercial) | Part 4 | Commercial methodology. |
| Lock-maker-and-thief / baggage-scanner / giraffe-vs-car analogies | BayOne REFERENCES | Part 3 | Explanatory devices. |

### 2.15 Communication / Collaboration Tools

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Microsoft Teams | Lam HAS | Part 1, Part 2, Part 4 | **Access-critical for collaboration + meetings.** |
| Microsoft Teams transcription | Lam HAS | Part 1, Part 4 | Informational. |
| Email | Lam HAS | Part 2, Part 4 | Standard. |
| Meeting transcription tools (generic) | Lam HAS | Part 2 | Informational. |
| Slack | Not explicitly mentioned | — | BayOne-internal alternative possibility. |
| SharePoint / OneDrive file-sharing | Lam HAS (likely) | Part 1, Part 2 | File-sharing mechanism. **Access-critical for non-sensitive doc sharing.** |
| Working session (format) | BayOne REFERENCES | Part 4 (information_request) | Proposed meeting format. |

### 2.16 Development / Operational Tooling

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Git / GitHub | BayOne REFERENCES | Part 2 (Colin; Cisco 3-week wait) | **Access-critical for POC version control.** |
| CI/CD (generic) | BayOne REFERENCES | Part 2 | Informational. |
| MLOps pipeline (as generic practice) | Lam HAS (prior) | Part 1, Part 4 | Informational. |
| Jupyter / equivalent IDE | BayOne REFERENCES | (Standard Python toolchain) | **Access-critical for POC.** |
| pip / package manager | BayOne REFERENCES | (Standard Python) | **Access-critical — Lam-approved repo or air-gapped wheel-file approach.** |
| Evaluation scripts | Lam may HAVE | Part 4 (information_request) | Reusable artifacts being inquired about. |
| Data pipelines / ingestion frameworks / middleware | Lam HAS | Part 4 (information_request) | Open ask. Informational. |
| Centralized ingestion pipeline | BayOne COMMITTED | Part 4 | Methodology. |
| Dashboards / BI tools | BayOne REFERENCES | Part 4 | Governance surfaces. Informational. |
| Scheduled scan (data sources) | BayOne REFERENCES | Part 4 | Methodology. Informational. |
| Standard tooling (entity dict updates) | BayOne COMMITTED | Part 4 (discovery_followup) | Methodology. |
| Change request process | BayOne COMMITTED (commercial) | Part 4 | Commercial. |
| BayOne V1 internal labeling tool | BayOne BRINGS | Part 3 (Pat line 129) | BayOne-internal. Informational. |
| Test Complete (automation testing) | Lam HAS (exploring) | Part 2 | Informational. |
| API documentation / non-prod environment access | Open ask | Part 1 (NEEDS 3.3) | Informational. |

### 2.17 Compliance / Standards / Frameworks

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| ITAR | BayOne REFERENCES | Part 1, Part 3 (Colin line 152) | Colin's prior-work credibility. Informational. |
| CMMC | BayOne REFERENCES | Part 1 | Colin's prior-work credibility. Informational. |
| DFARS | BayOne REFERENCES | Part 1 | Colin's prior-work credibility. Informational. |
| NIST 800-171 | BayOne REFERENCES | Part 1 | Colin's prior-work credibility. Informational. |
| FedRAMP | BayOne REFERENCES | Part 3 | Colin's prior-work credibility. Informational. |
| Healthcare / HIPAA-adjacent | BayOne REFERENCES | Part 3 | Colin's prior-work credibility. Informational. |
| Embargo / Trade Restrictions (TRI) | Lam HAS (operational) | Part 1 (Brad), Part 4 | Lam compliance context. Informational. |
| Zero-trust (Lam posture) | Lam HAS | Part 1 (Callahan PREP) | Posture. Informational. |
| Antitrust / competitive-harm risk | BayOne REFERENCES (framing) | Part 1 (PREP), Part 4 | Risk framing. Informational. |
| China-operations IP protection (bidirectional) | BayOne REFERENCES | Part 1 (PREP, Colin CALL) | Colin's prior-work credibility. Informational. |
| AI governance maturity Stage 1-5 model | BayOne REFERENCES | Part 1 (PREP) | Framework. Informational. |
| Export control constraints | BayOne REFERENCES | Part 4 (discovery_followup) | Industry framing. Informational. |
| Semiconductor industry context | Lam IS | Part 4 | Informational. |
| Customer data-out policy (Lam/customer governance) | Lam HAS | Part 3 (Daniel) | Out of POC scope. |
| Clean room policies | Lam HAS | Part 3 (Brad) | Out of POC scope. |
| "No customer confidential information in Escalation Solver" policy | Lam HAS | Part 3 (Mikhail line 48) | The policy the POC enforces. |
| Regulatory or contractual requirements on data | Lam HAS | Part 4 (information_request) | Open ask. Informational. |
| Confidentiality practices (existing NDA) | Lam HAS | Part 4 | Governing. Access-critical. |
| GDPR, CCPA, SOC2, HIPAA, ISO | Not explicitly mentioned | — | — |

### 2.18 Equipment / Hardware

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Semiconductor wafer fabrication equipment | Lam's product | Part 1, Part 4 | Lam context. Informational. |
| Customer fab equipment | Lam HAS (context) | Part 3 | Informational. |
| Servers at Lam data center | Lam HAS | Part 3 (Mikhail line 155) | On-prem. Informational. |
| Colored badges | Lam HAS | Part 1, Part 4 | Identity. Informational. |
| Laptops | — | Part 1, Part 2 | Incidental. |
| Whiteboard | — | Part 1 | Meeting context. |
| GPU (speculated local training) | Lam TRIED (per Colin) | Part 1 | Speculation. Informational. |
| Mobile device (as data entry source) | Lam HAS (context) | Part 4 | Illustrative. Informational. |
| Tool (semiconductor tool) | Lam HAS | Part 4 | Example context. Informational. |
| Nvidia (via Garak tool name) | — | Part 1 (PREP) | Reference only. |

### 2.19 BayOne Methodology IP / Frameworks Named (from Part 4)

| Technology / System | Status | Source Attribution | Context & Relevance to POC |
|---|---|---|---|
| Layered Detection Methodology | BayOne COMMITTED | engagement_pricing, poc_proposal, pricing_breakdown | Named; "deterministic → ML/NLP → Gen AI, sequentially." **Core IP.** |
| Hybrid Architecture for Intelligent IP Protection | BayOne COMMITTED | preliminary_approach (title) | Named architectural framework. |
| Hybrid Detection Architecture | BayOne COMMITTED | discovery_followup | Named section. |
| Ingestion-First Architecture | BayOne COMMITTED | preliminary_approach | Named principle. |
| Unified Data Plane / Common Data Plane | BayOne COMMITTED | preliminary_approach, discovery_followup | Named concept. |
| Enterprise Tools Strategy | BayOne COMMITTED | preliminary_approach | Named principle. |
| Application-by-Application Migration | BayOne COMMITTED | preliminary_approach | Named rollout strategy. |
| Office of AI Strategy and Innovation (BayOne org unit) | BayOne COMMITTED | engagement_pricing letterhead | Branding. |
| Director of AI (Colin Moore) | — | engagement_pricing | Leadership. |
| Defined Repeatable Evaluation Protocol | BayOne COMMITTED | engagement_pricing, poc_proposal, pricing_breakdown | Artifact. |
| Detection Target Map | BayOne COMMITTED | poc_proposal, pricing_breakdown | Artifact. |
| Accuracy Ceiling determination | BayOne COMMITTED | poc_proposal | Artifact. |
| Data Quality Report | BayOne COMMITTED | poc_proposal, pricing_breakdown | Artifact. |
| EDA Report (engineering doc) | BayOne COMMITTED | pricing_breakdown | Artifact. |
| Scaling Path documentation | BayOne COMMITTED | engagement_pricing, poc_proposal, pricing_breakdown | Artifact. |
| Methodology documentation (layer contribution to accuracy) | BayOne COMMITTED | engagement_pricing, poc_proposal, pricing_breakdown | Artifact. |

---

## 3. Access Request List

This section distills the above inventory into exactly what Lam must provision for the POC to begin and proceed. Each item includes a WHY note — what breaks if Lam does not provision it.

### 3.1 Environment Access

| Item | Baseline Spec / Requirement | Why Access-Critical |
|---|---|---|
| Virtual machine or workspace on Lam infrastructure (Option A) | Linux preferred; 8 cores / 32 GB RAM / 200 GB disk baseline (scale up if embeddings to be cached locally) | Named in deliverables; data "never leaves Lam systems." Without this, we cannot proceed under Option A. |
| OS | Linux (Ubuntu 22.04 LTS or RHEL 9 preferred). Acceptable alternatives: any supported Linux distro with Python 3.10+ | NLP tooling (spaCy, Presidio, HuggingFace) best supported on Linux; Windows workable but slower. |
| Internet egress policy | **CLARIFICATION NEEDED** — fully open egress OR curated allow-list (pypi.org, huggingface.co, github.com, relevant Azure endpoints) OR fully air-gapped with pre-loaded wheels/models | Without egress or wheel-file approach, cannot install NLP libraries or pull model weights. This directly gates Phase 1. |
| Persistent storage for POC artifacts | ~50 GB mapped to the POC VM; separate location for exported data; POC-artifact retention policy aligned with NDA | Required for checkpointing models, storing intermediate embeddings, and holding evaluation outputs. |
| Confirmed access to the partially-spun-down prior-project Azure environment | Read access to hourly-retrieval-job outputs and any retained artifacts | Prior-effort environment still up per Mikhail (Part 3); potential baseline artifacts and historical data save us 3-5 days of Phase 1 work. |

### 3.2 Data Access

| Item | Specifics | Why Access-Critical |
|---|---|---|
| Escalation Solver — five free-text fields export | 4,000-5,000 chars each; representative sample across ticket types; minimum ~1,000 tickets (ideal 20,000 per BayOne EDA benchmark) | THE POC test corpus. Without this, zero phases of the POC proceed. |
| Customer name reference list | Authoritative list of Lam customer names + known variations | Deterministic Layer 1 lookup. Without it, Layer 1 cannot flag known entities. |
| Fab / location identifier reference list | Including known variations (Fab 11, F11, Micro 11, FAP 11, FAP-11, etc.) | Second target entity type. Same reason as above. |
| Exclusion list | Content / acronyms approved for general sharing (derived from the 3,000-item acronyms list minus customer names) | Prevents false positives on benign terms. |
| Lam acronyms list (~3,000 items) | Authoritative source | Source of truth for exclusions and also potential Layer 1 dictionary. |
| ~1,000 thumbs-up/thumbs-down label set | Existing UI feedback data | Closest thing Lam has to a labeled evaluation dataset. Without it, we cannot benchmark rigorously. |
| Prior-effort code, notebooks, artifacts | Documentation of prior detection effort results, model selection history, baseline metrics (21%/17% FPR, 90% accuracy), any reusable scripts | Named as reference benchmark in client-facing deliverables. Without it, "benchmarked against prior effort" commitment cannot be met. |
| Prior trained models / labeled datasets / evaluation scripts | Any reusable artifacts from the 18-month effort | Referenced in information_request. Major time-saver if available. |
| Real false-positive examples from prior testing | Any captured FP cases | Directly feeds Layer 2 tuning. Major Phase 1 accelerator. |
| Any contractual / regulatory constraints on data handling | Written policies for CII handling; customer contractual data-segregation requirements | Informs what sanitization or sampling approach is acceptable. Can unblock Option A vs. Option B decision. |

### 3.3 Tooling Access

| Item | Specifics | Why Access-Critical |
|---|---|---|
| Python runtime | Python 3.10 or later | Core POC language. Cannot run any of BayOne's code without it. |
| Package manager | pip with access to a Lam-approved PyPI mirror **OR** air-gapped install via pre-loaded wheel files | Without this, cannot install spaCy, Presidio, scikit-learn, pandas, numpy, HuggingFace Transformers. This is the single biggest potential blocker. |
| Jupyter (or equivalent IDE) | JupyterLab, VS Code, or similar | EDA and iterative model work. |
| Git / GitHub (or internal Git server) | Repo provisioning for the POC codebase | Version control. Cisco took 3 weeks (Part 2); start now to avoid being the critical path. |
| Ability to install and run: spaCy (+ en_core_web_lg model), Microsoft Presidio, scikit-learn, pandas, numpy, HuggingFace Transformers, sentence-transformers, TF-IDF (via scikit-learn) | Standard NLP stack | Core Layer 1/Layer 2 components. Without these, methodology cannot be implemented. |
| Ability to download Hugging Face model weights (or pre-stage them on VM) | Model cache, e.g., sentence-transformers/all-MiniLM-L6-v2 and comparable | Layer 2. Without weights, no ML layer. |
| Data-sharing location for reference lists | SharePoint / OneDrive / secure S3-equivalent for non-sensitive docs | Exchange of methodology documents, sanitized outputs, reports. |

### 3.4 Generative AI Layer Access (methodology-critical)

| Item | Specifics | Why Access-Critical |
|---|---|---|
| Lam-sanctioned LLM endpoint for Layer 3 | Azure AI Foundry endpoint is the named target per all client-facing deliverables; alternative acceptable if Lam has a different sanctioned path | Layer 3 of the committed methodology depends on Gen AI. Without an endpoint, the third layer is a documentation exercise only — contradicting what Lam has already seen in writing. |
| Acceptable model family | GPT-4.0 (or newer GPT), Claude, or any Lam-sanctioned equivalent. Azure AI Foundry reportedly has "everything except Gemini" per Colin | Drives both accuracy and cost. |
| Rate limits / quotas | Documented tokens-per-minute and requests-per-minute | We need to pace load tests and batch eval runs; hitting a silent quota mid-Phase-2 would be a Week-3 blocker. |
| InfoSec approval path for BayOne to call the endpoint | Named approver + typical lead time | Without this, cannot write a single Gen-AI line even with environment access. |
| Documented fallback | If no sanctioned endpoint exists in time: (a) proceed with Layers 1-2 only and document Layer 3 in abstract, OR (b) run Layer 3 against BayOne-internal endpoint under Option B with sanitized data | So Mikhail / Daniel know the contingency before we hit it. |

### 3.5 Identity / Account Provisioning

| Item | Specifics | Why Access-Critical |
|---|---|---|
| LAM ID accounts for BayOne consultants | **2 accounts** — Colin Moore (Director of AI) + 1 onshore BayOne engineer. Include email, VPN, SSO, MFA enrollment | Colin does not currently have a LAM ID (Part 3, line 192). Without LAM IDs, no access to anything else. |
| NDA scope confirmation | Confirm existing NDA covers POC scope (Escalation Solver data, reference lists, POC outputs) OR issue supplemental | Without NDA coverage, Lam legal blocks Phase 1 start. |
| MFA provisioning | Standard Lam MFA (Microsoft Authenticator or equivalent) | Required by zero-trust posture. |
| Account provisioning lead time | Typical Lam turnaround (1-3 weeks?) | Confirms whether 2026-05-04 POC start is feasible. If lead time is >2 weeks, start TODAY. |
| SLW / Statement of Work paperwork | Brad flagged ~1 week turnaround (Part 3, line 197-198) | Must be initiated in parallel with account provisioning. |

### 3.6 Subject Matter Expert / Validation Support

| Item | Specifics | Why Access-Critical |
|---|---|---|
| Designated Lam SME (named) | One person, ~2-4 hours/week across Phase 1-2 | Defines detection targets, validates results, confirms true positives vs false positives. Without an SME, we cannot produce a credible Detection Target Map (a committed deliverable). |
| Prior-effort documentation | Results, model selection history, target performance aims, baseline metrics | Named in client-facing deliverables as the benchmark. |
| Authoritative source for acronyms list | Who owns the 3,000-item list; how is it kept current | Determines whether we work from a snapshot or a live feed. |
| Access to the thumbs-up/down feedback data (~1,000 examples per Mikhail) | Export of labels + associated text | Near-ground-truth for Phase 2 evaluation. |

### 3.7 Communication / Collaboration

| Item | Specifics | Why Access-Critical |
|---|---|---|
| Slack or Teams channel for the engagement | One shared channel across Brad, Mikhail, Daniel, Colin, BayOne eng | Lower-friction comms than email. Speeds daily unblocks. |
| Preferred meeting cadence | Weekly 30-min sync + ad-hoc for blockers | Mikhail and Daniel alignment. |
| File-sharing mechanism for non-sensitive documents | SharePoint, OneDrive, or Box location accessible to BayOne LAM IDs | Exchanging methodology documents, sanitized outputs, reports. |

---

## 4. Open Questions for Daniel Harrison

### Blockers for POC Start (MUST be resolved before POC can begin)

1. **What is Lam's sanctioned LLM endpoint for internal use, and what is the approval process for BayOne to call it?** Specifically: is Azure AI Foundry provisioned and accessible in a Lam tenancy that BayOne consultants can reach via LAM IDs? If not, what is the path (LamGPT endpoint? Another Azure subscription? InfoSec exception)?
2. **What is the account provisioning lead time for BayOne consultants to receive LAM IDs (email, VPN, SSO, MFA)?** If >2 weeks, we need to start TODAY to hit a 2026-05-04 POC start.
3. **Does the existing BayOne-Lam NDA cover the POC scope, or is a supplemental needed?** Who signs on each side?
4. **Option A vs Option B: can we export Escalation Solver five-free-text-field data to BayOne infrastructure, or must all work happen inside a Lam VM?** This gates the environment request entirely.
5. **What is the internet egress policy on a provisioned Lam POC VM?** Fully open / curated allow-list / fully air-gapped. If air-gapped, we need a pre-loaded wheel approach for pip packages and pre-downloaded Hugging Face model weights.
6. **Can we reach the partially-spun-down prior-project Azure environment, and what artifacts (code, data, models, evaluation scripts) does it still contain?** Mikhail confirmed the environment is still up (Part 3, line 148). If we can pull from it, we save 3-5 days of Phase 1 work.
7. **What is the Detection Target Map validation authority?** Who on Lam's side owns the SME review for "is this a true positive or a false positive?" Is that Mikhail, a dedicated Escalation Solver ops person, or a Knowledge and Advanced Services engineer?

### Week 1 Items (can be sorted in parallel with data provisioning)

8. What Python version and package-install approach does Lam prefer on POC VMs (Python 3.10 vs 3.11; pip + allow-list vs wheel-files)?
9. Is there a Lam-approved PyPI mirror, or do we pre-load wheel files? If wheels, what's the delivery mechanism?
10. Git access: is there a Lam-internal Git server (Bitbucket/GitLab/ADO) we should use, or can we use a private GitHub repo?
11. How do we exchange sanitized methodology documents and reports — SharePoint, OneDrive, Teams file-sharing, or Box?
12. What is the standing Slack/Teams channel for the engagement? Who to include?
13. What is the authoritative format for the three reference lists (acronyms, customer names, fab identifiers)? Excel? JSON? Database export?
14. Are there any Microsoft Purview admin roles we'd need to exercise Custom SITs and DLP policies inside Lam's tenant — or is that Phase 2-scoped only (documentation, not implementation)?

### Informational / Nice-to-Have

15. Can we get Daniel's full team org chart for the prior 18-month effort? (Identifies who else might hold knowledge of Presidio 12-to-3 narrowing, the Flair choice, reconciliation-algorithm implementation details.)
16. Is LamGPT actually provisioned and what models does it front? (Referenced in Part 1 only; not confirmed in Part 3.)
17. What ticketing system underlies Escalation Solver (ServiceNow, Jira, something homegrown atop .NET)?
18. Is Microsoft Sentinel being asked to do any content-detection work today? (Per prep doc, Colin suspects it's miscast as a guardrail.)
19. Is there a Lam-sanctioned labeling tool we should use for any Phase 1 annotation work, or should we use BayOne's V1 internal labeling tool?
20. What is the GitHub-like wait time Lam typically has for vendor repo access? (Cisco example was 3 weeks.)

---

## 5. Items BayOne Has Committed to in Writing (from Part 4)

This section lists specific technologies and methodologies BayOne has named in client-facing deliverables that Lam has received. We must be ready to deliver on these — or, if we plan to substitute, signal it explicitly in any Mikhail response.

| Committed Item | Source Deliverable(s) |
|---|---|
| **Azure AI Foundry** as AI hosting/compute platform | preliminary_approach (html/md), discovery_followup_2026-04-06.html |
| **Microsoft Purview** as foundation for the deterministic detection layer | preliminary_approach, discovery_followup |
| **Microsoft Purview Custom Sensitive Information Types (SITs)** for domain-specific entities (customer names, fab identifiers, variations) | preliminary_approach, discovery_followup |
| **Microsoft Purview DLP policies** to enforce detection rules across connected systems | preliminary_approach, discovery_followup |
| **Azure Blob Storage** for document storage in the unified data plane | preliminary_approach |
| **Vector database (generic) for search embeddings** in the unified data plane | preliminary_approach |
| **Azure PostgreSQL with pgvector** named as alternative custom component when Azure AI Search falls short | preliminary_approach |
| **Azure AI Search** named as the default vector search alternative | preliminary_approach |
| **Three-layer sequential Layered Detection Methodology** (deterministic → ML/NLP → Generative AI) | engagement_pricing, poc_proposal (html/md), pricing_breakdown |
| **Generative AI for contextual edge cases, applied sequentially** (Layer 3) | engagement_pricing, poc_proposal, pricing_breakdown |
| **Hybrid Architecture for Intelligent IP Protection** (named architectural framework) | preliminary_approach (title) |
| **Ingestion-First Architecture** (named principle) | preliminary_approach |
| **Unified / Common Data Plane** (named concept) | preliminary_approach, discovery_followup |
| **Application-by-Application Migration** (named rollout strategy) | preliminary_approach |
| **Defined Repeatable Evaluation Protocol** (named deliverable) | engagement_pricing, poc_proposal, pricing_breakdown |
| **Detection Target Map** (named deliverable) | poc_proposal, pricing_breakdown |
| **Accuracy Ceiling determination** (named deliverable) | poc_proposal |
| **Data Quality Report / Assessment** (named deliverable) | poc_proposal, pricing_breakdown |
| **EDA Report (engineering documentation)** | pricing_breakdown |
| **Scaling Path documentation** | engagement_pricing, poc_proposal, pricing_breakdown |
| **Methodology documentation (layer contribution to accuracy)** | engagement_pricing, poc_proposal, pricing_breakdown |
| **Asynchronous queue with synchronous user experience** (processing architecture) | preliminary_approach |
| **Auto-scaling (Azure capability)** (talking point for why Azure) | discovery_followup |
| **RBAC native integration (Azure)** (talking point) | discovery_followup |
| **Hybrid deployment model** (named as supportable alternative to pure Azure) | discovery_followup |
| **Option A (inside Lam environment) + Option B (BayOne infra under existing NDA)** as explicit commercial options | engagement_pricing, poc_proposal |
| **VM or equivalent as the form of environment access under Option A** | engagement_pricing, poc_proposal |
| **Three-week POC timeline from data access** | engagement_pricing, poc_proposal, pricing_breakdown |
| **Sub-1% false positive target** (performance aim) | problem_restatement, preliminary_approach |
| **Entity types: Customer name + Fab identifier** (POC scope) | engagement_pricing, poc_proposal, pricing_breakdown |
| **Five free-text fields of Escalation Solver (4,000-5,000 chars each)** | engagement_pricing, poc_proposal, pricing_breakdown |

---

## 6. Flags and Inconsistencies

1. **LamGPT confirmation gap.** LamGPT is referenced explicitly in Part 1 (Mikhail on the discovery call said "some of it is lamb GPT so we still have Open and like the GPT models within lamb") and Colin restated it in TECH1. However, Part 3 (the April 6 client meeting, which was much more technical) has NO "LamGPT" mention. Part 3's Notable Absences section explicitly calls this out. **Action:** ask Daniel/Mikhail to confirm whether LamGPT is a provisioned internal system, a marketing name for their Copilot deployment, or a misheard reference.

2. **GPT models mention only in the markdown version of problem_restatement.** Part 4 flags that the `.md` says "internally hosted AI tools (including GPT models deployed within Lam's own infrastructure)" but the `.html` omits the parenthetical. **Action:** confirm which version was sent to Lam so we don't inadvertently introduce or retract the claim.

3. **Pricing discrepancy in `poc_proposal.md` ($10,000) vs all other pricing docs ($15,000).** Flagged in Part 4. **Action:** confirm the final price before Mikhail response references pricing.

4. **"Azure AI model" in the prior three-model finalists is unspecified.** Part 3 confirms Lam dropped one Presidio-family model and added an "Azure AI" model late in the down-selection; Part 1 confirms neither Mikhail nor the team could identify the exact model. **Action:** ask Mikhail to dig through JIRA / email for the specific model name; this matters for the "benchmark against prior baseline" commitment.

5. **Microsoft Sentinel's role.** Part 1 PREP says Lam has it as part of their Azure stack. Colin (DEBRIEF) argues it is being miscast as a content-detection tool when it is a SIEM/SOAR. Not discussed at all in Part 3. **Action:** clarify with Daniel whether Sentinel is actually in the detection path today.

6. **Microsoft Purview adoption gap.** BayOne has committed Purview as the foundation for Layer 1 across all client-facing deliverables (preliminary_approach, discovery_followup). But Purview has never been confirmed as provisioned at Lam in any transcript — Mikhail did not mention it in Part 3 despite a dense technical discussion. **Action:** confirm Purview licensing and admin access availability. Without it, we have a gap between what Lam has seen in writing and what we can actually implement.

7. **Methodology commitment vs. plan.** Client-facing deliverables commit to a Microsoft Purview + Azure AI Foundry-centric Layered Detection Methodology. Part 3 transcripts show Colin describing the same three-layer methodology but primarily in terms of regex, spaCy/Flair/sentence-transformers (for Layer 2), and a generic "Gen AI for edge cases" (Layer 3). The POC as we are actually planning to execute it appears to be lighter on Purview specifics than the deliverables imply. **Action:** reconcile with Mikhail explicitly — are we implementing Purview Custom SITs and DLP policies in the POC, or are we building a Python-based prototype of the same concept that could later be wired into Purview?

8. **Part 1 "they don't know what Azure AI service they were using" vs Part 3 "we used Azure AI as the primary."** Not necessarily contradictory but worth confirming. Part 3's "Azure AI" reference probably means Azure OpenAI / Azure AI Foundry as of 18 months ago. **Action:** confirm.

9. **SLMs / Edge AI ambiguity.** Daniel raised SLMs and Edge AI in Part 3; Colin pushed back. Daniel may come back to this. **Action:** Colin should be ready with the "when SLMs are justified" argument and confirm Edge is strictly future scope, not POC.

10. **Acronyms: 3,000 items per Part 3 (Mikhail line 80); "close to 3,000" is an approximation.** **Action:** confirm exact count when Lam provides the list.

11. **Accenture vs. unnamed "prior partners" in client-facing deliverables.** Part 1 confirms Accenture was Lam's prior technical partner on this problem. Part 4 client-facing deliverables (information_request) ask about "prior partners" without naming Accenture. Part 3 does not mention Accenture at all. This is deliberate — BayOne has not surfaced Accenture by name to Lam in writing. **Action:** maintain this separation in the Mikhail response.

12. **"Transcription errors that might still be ambiguous":** "Gapsium"/"Kaptima" = Capgemini; "Spacey" = spaCy; "Michaela" = Mikhail; "drones" = drawings; "concept-renade" = confidentiality violation; "wipe board" / "Why board" = whiteboard; "lamb GPT" = LamGPT; "Asher" = Azure; "SLW" = SOW; "flare" = Flair; "GPD 4.0" = GPT-4.0; "FAP" = fab. All resolved in the Parts, but a fresh reader could re-encounter these.

13. **Not a contradiction but a gap: Python version.** Not named in any source. BayOne should specify 3.10+ proactively in the Mikhail response.

14. **Rate/model availability for Azure AI Foundry in Lam's tenancy.** Colin claims Azure AI Foundry has "everything except Gemini" (Part 3). This is true at the Azure level but Lam may have restricted it further via their own governance. **Action:** ask what specific models are approved inside Lam's Azure tenancy.
