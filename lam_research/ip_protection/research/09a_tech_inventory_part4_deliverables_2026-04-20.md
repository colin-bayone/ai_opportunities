# 09a - Technology Inventory Part 4: Client-Facing Deliverables

**Source:** All HTML and markdown files in /lam_research/ip_protection/deliverables/
**Source Date:** 2026-03-12 through 2026-04-09
**Document Set:** 09a (supplementary to Set 09)
**Pass:** Complete extraction of every technology/tool/platform/system mention from BayOne's deliverables to Lam

---

## Document Set Inventory

**Client-facing documents (shared or to be shared with Lam):**

1. `problem_restatement_2026-03-12.html`
2. `problem_restatement_2026-03-12.md`
3. `preliminary_approach_2026-03-12.html`
4. `preliminary_approach_2026-03-12.md`
5. `information_request_2026-03-12.html`
6. `information_request_2026-03-12.md`
7. `followup_email_draft_2026-03-12.md`
8. `discovery_followup_2026-04-06.html`
9. `engagement_pricing_2026-04-09.html`
10. `poc_proposal_2026-04-09.html`
11. `poc_proposal_2026-04-09.md`

**Internal-only documents (NOT shared with Lam, flagged):**

12. `internal_cost_breakdown_2026-04-09.html` — INTERNAL ONLY ("Internal Document - Do Not Share With Client")
13. `pricing_breakdown_2026-04-09.html` — Appears client-facing (letterhead says "Prepared for Lam Research") but may also be internal/companion to engagement_pricing. Flagged for clarification.

---

## 1. Compute / Hosting / Infrastructure

### Lam Research infrastructure / environment
- **Source:** engagement_pricing_2026-04-09.html, poc_proposal_2026-04-09.html/md
- **Context:** Option A (Recommended) execution environment; access requirements include "environment access (VM or equivalent) and access to Escalation Solver data and reference materials"
- **Quote:** "Option A (Recommended): All work is performed within the Lam Research environment. This approach ensures data never leaves Lam systems and aligns with existing confidentiality practices. BayOne will require environment access (such as a virtual machine) and access to Escalation Solver data and reference materials before the three-week timeline begins."

### BayOne infrastructure
- **Source:** engagement_pricing_2026-04-09.html, poc_proposal_2026-04-09.md, internal_cost_breakdown_2026-04-09.html
- **Context:** Option B execution environment
- **Quote:** "Option B: BayOne performs the work on its own infrastructure using data provided by Lam Research under the existing confidentiality agreement."
- **Quote (md):** "The POC runs on BayOne infrastructure unless there is a specific requirement to operate within the Lam Research environment"

### Virtual Machine (VM)
- **Source:** engagement_pricing_2026-04-09.html, poc_proposal_2026-04-09.html
- **Context:** Named as the presumed form of environment access under Option A
- **Quote:** "BayOne requires environment access (VM or equivalent) and access to Escalation Solver data and reference materials"
- **Quote:** "Execution environment provisioning (VM or equivalent for Option A, data export for Option B)"

### On-premises systems
- **Source:** problem_restatement (html/md), preliminary_approach.md, discovery_followup_2026-04-06.html
- **Context:** Infrastructure landscape description; Azure AI Foundry APIs decouple AI compute from on-premises application deployment
- **Quote:** "The technology environment is highly heterogeneous. There is a mix of on-premises systems, cloud-based systems, systems in the process of migrating to cloud..."
- **Quote:** "Even applications that are hosted on-premises can leverage Azure AI Foundry APIs for processing"

### Cloud-based systems / Cloud-first aspiration
- **Source:** problem_restatement, discovery_followup
- **Context:** Lam's infrastructure landscape and stated aspiration
- **Quote:** "The organization aspires to move cloud-first and has expressed interest in a microservice architecture long-term, though this is aspirational rather than committed."

### Microservice architecture
- **Source:** problem_restatement, discovery_followup
- **Context:** Lam's aspirational long-term architecture
- **Quote:** "expressed interest in a microservice architecture long-term"

### Hybrid deployment model
- **Source:** discovery_followup_2026-04-06.html
- **Context:** Alternative to Azure, noted as supportable
- **Quote:** "The same architecture can work on-premises or in a hybrid model if required."

### Asynchronous queue (processing architecture)
- **Source:** preliminary_approach (html/md)
- **Context:** AI classification layer processing architecture
- **Quote:** "The processing architecture would use an asynchronous queue for robustness and scalability, while delivering a synchronous user experience."

### Auto-scaling (Azure capability)
- **Source:** discovery_followup_2026-04-06.html
- **Context:** "Why Azure" table
- **Quote:** "Auto-scales with usage. The system grows with the organization without requiring infrastructure re-architecture."

---

## 2. Data Storage / Databases / Data Lakes

### Azure Blob Storage
- **Source:** preliminary_approach (html/md)
- **Context:** Recommended starting point for document storage in the unified data plane
- **Quote:** "The recommended starting point is Azure-native services (Blob Storage for documents, a vector database for search embeddings, Azure AI Foundry for AI model hosting)"

### Vector database (generic) for search embeddings
- **Source:** preliminary_approach (html/md)
- **Context:** Unified data plane component
- **Quote:** "a vector database for search embeddings"

### Azure PostgreSQL with pgvector
- **Source:** preliminary_approach (html/md)
- **Context:** Custom component option when Azure-native services fall short; explicit alternative to Azure AI Search
- **Quote:** "custom components can be built on Azure infrastructure (for example, Azure PostgreSQL with pgvector for vector search, rather than Azure AI Search)"

### Azure AI Search
- **Source:** preliminary_approach.md
- **Context:** Named as the Azure-native vector search alternative that custom pgvector could replace
- **Quote:** "Azure PostgreSQL with pgvector for vector search, rather than Azure AI Search"

### Data lake (absence thereof)
- **Source:** problem_restatement, preliminary_approach, discovery_followup
- **Context:** Lam's current state has no unified data lake
- **Quote:** "No unified data lake. Data is fragmented across many systems with different segmentation and access models."

### Unified data plane
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Core architectural recommendation; central unified storage / ingestion / access layer
- **Quote:** "A unified data plane would provide a single standard interface that consolidates these capabilities."

### Knowledge base / knowledge bases
- **Source:** problem_restatement, preliminary_approach, discovery_followup
- **Context:** Target repositories for cleaned content
- **Quote:** "cleaned data can enter the self-help knowledge base"

### Six or more search tools / segmented search systems
- **Source:** problem_restatement, preliminary_approach, discovery_followup
- **Context:** Current state of fragmented search
- **Quote:** "There are currently six or more separate search tools, each covering a different knowledge pool with different access rules."

### Live data sources / databases / APIs
- **Source:** preliminary_approach (html/md), information_request
- **Context:** Categories of data handled by the pipeline
- **Quote:** "Live data sources (databases, APIs, active queries): For data accessed through live connections, the detection layer would operate at query time or through a scheduled scan of the data source"

### Ticketing system
- **Source:** problem_restatement
- **Context:** Lam internal system for customer segmentation
- **Quote:** "Customer segmentation in the ticketing system is enforced at the customer level"

---

## 3. Programming Languages / Runtimes

**None explicitly mentioned in the deliverable set.** No specific programming languages (Python, Java, JavaScript, etc.) are referenced by name in any client-facing deliverable.

---

## 4. NLP / NER Libraries / Frameworks

### spaCy
- **Source:** problem_restatement (html/md), preliminary_approach (html/md), information_request (html/md)
- **Context:** One of the three prior ML models tried by Lam
- **Quote:** "SpaCy (NLP library, likely NER-based) - ~20% false positive rate per ticket"
- **Quote:** "Prior attempts using custom ML models (Transformers, SpaCy, Azure AI) produced false positive rates around 20%"
- **Quote (info request):** "multiple ML-based approaches have been tried (Transformers, SpaCy, an Azure AI model)"

### Named Entity Recognition (NER)
- **Source:** problem_restatement, poc_proposal (html/md)
- **Context:** Technical category of Lam's prior 18-month effort
- **Quote:** "developed over a prior 18-month effort using multiple Named Entity Recognition (NER) models in parallel"
- **Quote:** "standard NER models are trained on generic entity types (person names, organizations, locations)"

### Natural Language Processing (NLP) layer
- **Source:** poc_proposal (html/md), engagement_pricing, pricing_breakdown
- **Context:** Middle layer of the proposed layered detection methodology
- **Quote:** "Machine learning and NLP layer: Addresses nuanced cases that deterministic matching cannot reach"
- **Quote:** "A machine learning and natural language processing layer addresses nuanced cases"

---

## 5. Machine Learning / Deep Learning Frameworks

### Transformers-based model / Transformers
- **Source:** problem_restatement (html/md), preliminary_approach (html/md), information_request (html/md)
- **Context:** One of the three prior ML models tried by Lam
- **Quote:** "Transformers-based model - Deep learning, fine-tuned on Lam data - ~20% false positive rate per ticket"

### Custom ML models (generic)
- **Source:** preliminary_approach (html/md), problem_restatement
- **Context:** Category label for prior Lam attempts
- **Quote:** "Prior attempts using custom ML models (Transformers, SpaCy, Azure AI) produced false positive rates around 20%"

### MLOps pipeline
- **Source:** problem_restatement (html/md)
- **Context:** Training infrastructure used by Lam
- **Quote:** "Three models were trained using an MLOps pipeline deployed on Azure Cloud."

### Machine Learning (ML) layer of the proposed methodology
- **Source:** poc_proposal (html/md), engagement_pricing, pricing_breakdown
- **Context:** Part of the layered detection approach
- **Quote:** "Machine learning and NLP detection layer: nuanced cases beyond deterministic matching"

### Fine-tuning
- **Source:** problem_restatement (html/md), preliminary_approach
- **Context:** Prior Lam approach that improved false positive rate marginally
- **Quote:** "Fine-tuning improved the false positive rate marginally, to approximately 17%."

---

## 6. Pre-trained Models / LLMs / Specific Model Names

### GPT models (deployed within Lam's infrastructure)
- **Source:** problem_restatement.md (note: only in the markdown version)
- **Context:** Lam's internally hosted AI tools
- **Quote:** "internally hosted AI tools (including GPT models deployed within Lam's own infrastructure)"
- **Flag:** Present in .md but the .html version says "internally hosted AI tools" without naming GPT. Check which version was actually sent to client.

### "Globally pre-trained foundations"
- **Source:** problem_restatement (html/md)
- **Context:** Reference to pre-trained base models used by Lam for fine-tuning
- **Quote:** "These models were trained with Lam's own data on top of globally pre-trained foundations."

### General-purpose language model baselines
- **Source:** problem_restatement, preliminary_approach
- **Context:** Benchmark comparison to Lam's prior work
- **Quote:** "A 20% false positive rate is consistent with general-purpose language model baselines"

**No specific foundation model names** (GPT-4, Claude, Llama, Mistral, Gemini, BERT, etc.) are named in the client-facing deliverables beyond the generic "GPT models" reference in the md file.

---

## 7. Generative AI Services / APIs

### Generative AI (category/layer)
- **Source:** problem_restatement, poc_proposal (html/md), engagement_pricing, pricing_breakdown
- **Context:** Third layer of the proposed layered detection methodology; also mentioned as a category Lam had not previously tried
- **Quote:** "Generative AI for contextual edge cases, applied sequentially" (engagement_pricing)
- **Quote:** "a generative AI layer provides contextual judgment on ambiguous cases" (poc_proposal)
- **Quote:** "Generative AI approaches have not been attempted. The decision was deliberate"

### Prompt engineering
- **Source:** problem_restatement (html/md)
- **Context:** Referenced as a possible technique to structure LLM output
- **Quote:** "There is awareness that prompt engineering can produce more structured output from language models"

### Cloud-based bot services / chatbots
- **Source:** problem_restatement (html/md), preliminary_approach (html/md)
- **Context:** Lam's existing AI/bot landscape; downstream consumers of the unified data plane
- **Quote:** "cloud-based bot services"
- **Quote:** "different applications (search tools, chatbots, Q&A systems) can connect"

### Q&A systems
- **Source:** preliminary_approach, information_request (html)
- **Context:** Class of downstream applications that would consume governed content
- **Quote:** "search tools, chatbots, Q&A systems, and other applications"

---

## 8. Application(s) Being Worked On

### Escalation Solver
- **Source:** engagement_pricing_2026-04-09.html, poc_proposal_2026-04-09.html/md, pricing_breakdown_2026-04-09.html, internal_cost_breakdown_2026-04-09.html
- **Context:** The specific Lam application that is the POC target
- **Quote:** "Demonstrate an improved detection methodology for customer-confidential information within Escalation Solver free-text fields."
- **Quote:** "Application: Escalation Solver (five free-text fields, 4,000 to 5,000 characters each)"
- **Quote:** "Entity Types: Customer name and fab identifier"
- **Quote:** "Additional applications beyond Escalation Solver" (listed as exclusion)
- **Quote:** "Production integration into Escalation Solver or any other application" (listed as exclusion)

### Escalation tickets / ticketing system
- **Source:** Multiple
- **Context:** Tickets created within Escalation Solver; data entry vehicle
- **Quote:** "free-text fields within escalation tickets"

---

## 9. Lam Internal Tools / Systems

### Access Security Manager (ASM)
- **Source:** problem_restatement (html/md)
- **Context:** Lam's existing access governance tool
- **Quote:** "Access Security Manager (ASM) governs access to certain sensitive areas (such as the escalation flow) but is not enterprise-wide and does not control individual entry fields within tickets."

### Multiple segmented search tools (six or more)
- **Source:** problem_restatement, preliminary_approach, discovery_followup
- **Context:** Current fragmented state of Lam's search landscape

### Internally hosted AI tools
- **Source:** problem_restatement (html/md)
- **Context:** Lam's existing AI systems
- **Quote:** "internally hosted AI tools (including GPT models deployed within Lam's own infrastructure)"

### Troubleshooting workflow (self-help / ask for help / escalate)
- **Source:** problem_restatement, discovery_followup
- **Context:** Lam's operational process model
- **Quote:** "three-stage troubleshooting workflow"

### Work center / role-based user identification
- **Source:** problem_restatement (html/md)
- **Context:** Lam's identity model
- **Quote:** "Users are identified by work center and role."

### Multiple search tools/systems/knowledge bases (unnamed)
- **Source:** Multiple
- **Context:** Lam's heterogeneous landscape

### Fab / customer-segmented ticketing
- **Source:** problem_restatement
- **Context:** Customer segmentation enforced in the ticketing system

---

## 10. Identity / Access / Security Systems

### Access Security Manager (ASM)
- See category 9.

### Identity and access management (IAM)
- **Source:** problem_restatement (html/md), discovery_followup
- **Context:** Lam's maturing program
- **Quote:** "Identity and access management is an active program of approximately two years but is not yet fully mature."
- **Quote (discovery_followup):** "credential and access management integrated with IAM and RBAC"

### Role-Based Access Control (RBAC)
- **Source:** discovery_followup_2026-04-06.html
- **Context:** Azure-native compliance capability cited as reason to use Azure
- **Quote:** "Native integration with identity and access management, role-based access control, and data governance capabilities out of the box."

### Badge colors (trade-restricted individuals)
- **Source:** problem_restatement.md
- **Context:** Employee type differentiation at Lam
- **Quote:** "trade-restricted individuals (with distinct badge colors)"

### Employee types (full, contractor, licensed service providers, trade-restricted, embargo-country)
- **Source:** problem_restatement (html/md)
- **Context:** Lam's user taxonomy
- **Quote:** "Employee types include full employees, contractors, licensed service providers, trade-restricted individuals, and embargo-country employees."

### Credential and access management
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Capability of the proposed unified data plane
- **Quote:** "Centralized control over connected data sources, with role-based access aligned to existing identity infrastructure"

### NDA / confidentiality agreement (existing)
- **Source:** engagement_pricing_2026-04-09.html
- **Context:** Governing document for Option B data handling
- **Quote:** "Data provided to BayOne under existing NDA and confidentiality agreement"

---

## 11. Microsoft / Azure Ecosystem

### Azure Cloud (generic)
- **Source:** problem_restatement (html/md), preliminary_approach, discovery_followup
- **Context:** Lam's prior MLOps pipeline deployment platform; BayOne's recommended target environment
- **Quote:** "Three models were trained using an MLOps pipeline deployed on Azure Cloud."

### Azure AI (prior Lam model)
- **Source:** problem_restatement (html/md), preliminary_approach, information_request
- **Context:** Specifically "Azure AI model" — one of the three prior Lam attempts
- **Quote:** "Azure AI model - Cloud-based ML service - ~20% false positive rate per ticket"

### Azure-native services (generic)
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Recommended starting point for BayOne's proposed architecture
- **Quote:** "The recommended starting point is Azure-native services"

### Azure Blob Storage
- See category 2.

### Azure AI Search
- See category 2.

### Azure PostgreSQL (with pgvector)
- See category 2.

### Azure AI Foundry
- **Source:** preliminary_approach (html/md), discovery_followup_2026-04-06.html
- **Context:** Recommended AI hosting/compute platform
- **Quote:** "Azure AI Foundry for AI model hosting"
- **Quote:** "Azure AI Foundry provides the hosting and compute environment for the AI classification layer. Models can be deployed, managed, and scaled through a managed service, reducing the operational burden of maintaining custom ML infrastructure."
- **Quote:** "Even applications that are hosted on-premises can leverage Azure AI Foundry APIs for processing"
- **Quote (discovery_followup):** "Hosted on Azure AI Foundry for scalability, manageability, and integration with enterprise identity and compliance controls."

### Microsoft Purview
- **Source:** preliminary_approach (html/md), discovery_followup_2026-04-06.html
- **Context:** Recommended enterprise tool for the deterministic detection layer
- **Quote:** "Microsoft Purview - Foundation for the deterministic detection layer. Custom Sensitive Information Types for domain-specific entities (customer names, fab identifiers, and their variations)."
- **Quote:** "Purview provides the foundation for the deterministic detection layer. Custom Sensitive Information Types can be defined for domain-specific entities"

### Custom Sensitive Information Types (SITs)
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Purview feature being recommended
- **Quote:** "Custom Sensitive Information Types for domain-specific entities"

### Data Loss Prevention (DLP) policies
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Purview-based policy mechanism
- **Quote:** "Data Loss Prevention policies to enforce detection rules across connected systems"

### Microsoft Teams (meeting transcripts)
- **Source:** problem_restatement (html/md)
- **Context:** Data entry source referenced in Lam's infrastructure landscape
- **Quote:** "Microsoft Teams meeting transcripts automatically attached to escalation tickets"

### Microsoft platforms (generic)
- **Source:** preliminary_approach
- **Context:** Recommended tooling direction
- **Quote:** "Many of the capabilities required for this initiative are available through existing Azure services and Microsoft platforms."

---

## 12. Third-Party Vendors / Consultants Mentioned

### BayOne Solutions
- **Source:** All deliverables
- **Context:** Author / vendor

### Prior partners (Lam's)
- **Source:** information_request (html/md)
- **Context:** Information being requested from Lam; identifies the existence of prior third-party partner(s) without naming them
- **Quote:** "Any prior partner involvement in this work (what was delivered, how the problem was scoped for them, and what the outcome was)"
- **Quote (html):** "Prior Partners - What was delivered, how the problem was scoped, and what the outcome was"

### No other third-party vendors named by name in the client-facing deliverables.

---

## 13. Reference Data / Lists / Datasets

### Customer name list
- **Source:** engagement_pricing, poc_proposal (html/md), pricing_breakdown
- **Context:** Reference data Lam is expected to provide
- **Quote:** "reference lists (customer names, fab/location identifiers, exclusion lists)"

### Fab/location identifier list
- **Source:** engagement_pricing, poc_proposal (html/md), pricing_breakdown
- **Context:** Reference data Lam is expected to provide
- **Quote:** "fab/location identifier lists"

### Exclusion list
- **Source:** engagement_pricing, poc_proposal
- **Context:** Reference data Lam is expected to provide
- **Quote:** "exclusion lists"

### Previously labeled examples
- **Source:** engagement_pricing, poc_proposal (html/md)
- **Context:** Reference data Lam is expected to provide
- **Quote:** "previously labeled examples that informed the prior detection effort"

### Ground truth
- **Source:** information_request, poc_proposal, engagement_pricing
- **Context:** Evaluation methodology concept; also listed as a POC exclusion ("ground truth remediation at scale")
- **Quote:** "how was ground truth established"
- **Quote:** "Ground truth remediation at scale (BayOne documents findings and recommends a remediation path)"

### Labeled datasets / training data
- **Source:** information_request
- **Context:** Referenced in prior-work context
- **Quote:** "Whether any prior work produced trained models, labeled datasets, or evaluation scripts"

### Labeling exercise (1,000+ person-hours)
- **Source:** problem_restatement, information_request
- **Context:** Prior Lam effort, paused due to cost
- **Quote:** "A labeling exercise to create structured training data was evaluated and estimated at over 1,000 person-hours"

### Customer-identifiable information
- **Source:** All deliverables
- **Context:** The target data category for detection

### Specific customer names referenced
- **Source:** problem_restatement (html/md), discovery_followup
- **Context:** Named examples of Lam's customers
- **Names:** TSMC, Samsung, Intel, Micron, SK Hynix
- **Quote:** "TSMC, Samsung, Intel, Micron, and SK Hynix all rely on Lam's equipment and services"

### Specific fab identifier variations referenced
- **Source:** problem_restatement, preliminary_approach, information_request
- **Context:** Named examples of spelling variation problem
- **Variations:** Fab 11, F11, Micro 11, FAP 11, FAP-11, Fab11
- **Quote:** "a single entity like 'Fab 11' can appear as Fab11, F11, Micro 11, FAP 11, FAP-11, and other variations"

### Five free-text fields of Escalation Solver (4,000-5,000 chars each)
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown
- **Context:** Target data in POC
- **Quote:** "Escalation Solver (five free-text fields, 4,000 to 5,000 characters each)"

### Entity types targeted
- **Source:** All pricing/proposal docs
- **Entities:** Customer name, fab identifier
- **Quote:** "Entity types: Customer name and fab identifier"

### Representative data samples / sanitized examples / synthetic representations
- **Source:** information_request (html/md), discovery_followup
- **Context:** Data BayOne is requesting
- **Quote:** "sanitized examples or synthetic representations that preserve the structure and patterns of real content"

### Data export (Option B)
- **Source:** engagement_pricing
- **Context:** Mechanism for BayOne to receive data under Option B
- **Quote:** "Lam Research provides data export and reference materials to BayOne"

### Sensitive information categories
- **Source:** problem_restatement (html/md)
- **Categories:** Customer names, Fab identifiers, File names, Site-specific details, Proprietary process data / Customer-proprietary process information

---

## 14. Methodology / Algorithms Mentioned

### BayOne's Layered Detection Methodology (core IP)
- **Source:** engagement_pricing, poc_proposal (html/md), pricing_breakdown
- **Context:** Central named methodology
- **Quote:** "Layered detection approach: deterministic pattern matching, machine learning and NLP, and generative AI for contextual edge cases, applied sequentially"

### Layer 1: Deterministic Layer / Deterministic pattern matching
- **Source:** preliminary_approach, discovery_followup, poc_proposal, engagement_pricing, pricing_breakdown
- **Context:** First layer of the proposed approach
- **Components:** Entity lookup tables, pattern matching, keyword and entity lists
- **Quote:** "A deterministic layer handles known patterns with high confidence and low computational cost"

### Layer 2: Machine Learning / NLP Layer
- **Source:** Same as above
- **Context:** Second layer for nuanced cases

### Layer 3: Generative AI Layer
- **Source:** Same as above
- **Context:** Third layer for ambiguous/contextual cases
- **Quote:** "Where required, a generative AI layer provides contextual judgment on ambiguous cases"

### Hybrid Architecture
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Named architectural approach
- **Quote:** "A Hybrid Architecture for Intelligent IP Protection"

### Contextual sensitivity analysis
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** AI classification capability
- **Quote:** "Contextual sensitivity analysis to determine whether a mention is sensitive in its specific context"

### Unstructured text analysis
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** AI classification capability

### Document-level classification
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** AI classification capability

### Ingestion-First Architecture
- **Source:** preliminary_approach (html/md)
- **Context:** Named architectural pattern
- **Quote:** "Ingestion-First Architecture"

### Application-by-application migration
- **Source:** preliminary_approach (html/md)
- **Context:** Named rollout strategy

### Exploratory Data Analysis (EDA)
- **Source:** engagement_pricing, poc_proposal (html/md), pricing_breakdown
- **Context:** Phase 1 methodology
- **Quote:** "Exploratory Data Analysis (EDA) - Using statistical analysis, BayOne will assess data separability between entity classes, evaluate the distribution and volume of content across the target fields, and determine the sample sufficiency of existing labeled data."

### Statistical analysis / Class separability / Distribution assessment / Sample sufficiency
- **Source:** pricing_breakdown, poc_proposal
- **Context:** EDA components
- **Quote:** "class separability, distribution assessment, sample sufficiency determination"

### Data Quality Assessment
- **Source:** poc_proposal, pricing_breakdown
- **Context:** Phase 1 deliverable
- **Quote:** "Assessment of reference data completeness, consistency, and contradictions with impact on achievable accuracy"

### Maximum achievable accuracy determination
- **Source:** All POC deliverables
- **Context:** Phase 1 outcome

### Detection Target Map
- **Source:** poc_proposal, pricing_breakdown
- **Context:** Phase 1 deliverable
- **Quote:** "Documented entity types, known variations, authoritative sources, and validation criteria"

### Defined, repeatable evaluation protocol
- **Source:** engagement_pricing, poc_proposal (html/md), pricing_breakdown
- **Context:** Phase 2 deliverable
- **Quote:** "Defined, repeatable evaluation protocol that carries forward to subsequent phases"

### Benchmarking against prior effort baseline
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown
- **Context:** Phase 2 activity
- **Quote:** "Detection performance benchmarked against prior effort baseline as documented by Lam Research"

### Scaling path documentation
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown
- **Context:** Phase 2 deliverable
- **Quote:** "Scaling path documenting how the approach extends to additional entity types, fields, and applications"

### Testing methodology / False positive rate calculation
- **Source:** information_request, problem_restatement
- **Context:** Technical concepts in play

### Rule-based models / Pattern matching
- **Source:** problem_restatement, preliminary_approach
- **Context:** Prior approach Lam abandoned; component of proposed deterministic layer

### Entity lookup tables
- **Source:** preliminary_approach (html/md), discovery_followup
- **Context:** Deterministic layer component
- **Quote:** "Entity lookup tables for customer names, fab identifiers, and their known variations, maintained as configuration rather than model weights"

### Keyword and entity lists
- **Source:** preliminary_approach (html/md)
- **Context:** Deterministic layer component

### OCR (Optical Character Recognition)
- **Source:** problem_restatement (html/md)
- **Context:** Referenced as a data entry/content path at Lam
- **Quote:** "user-entered problem statements, expert responses, uploaded documents, Microsoft Teams meeting transcripts automatically attached to escalation tickets, and images/OCR content"

### Feedback loop (escalation-to-self-help)
- **Source:** problem_restatement, discovery_followup
- **Context:** Methodological concept in the business process

### Outcome-based / Fixed-price pricing model
- **Source:** engagement_pricing, pricing_breakdown, poc_proposal
- **Context:** Commercial methodology
- **Quote:** "The pricing reflects a fixed-price, outcome-based model."

---

## 15. Communication / Collaboration Tools

### Microsoft Teams (transcripts)
- See category 11.
- **Context:** Specifically named data entry source for Lam

### "Working session" (meeting format)
- **Source:** information_request, preliminary_approach
- **Context:** Proposed discovery format with technical team

### Email / email draft
- **Source:** followup_email_draft_2026-03-12.md
- **Context:** Communication medium to Lam contacts

---

## 16. Development / Operational Tooling

### MLOps pipeline
- See category 5.

### Evaluation scripts
- **Source:** information_request
- **Context:** Reusable artifacts being inquired about
- **Quote:** "Whether any of this prior work produced reusable artifacts (trained models, labeled datasets, evaluation scripts)"

### Data pipelines / ingestion frameworks / middleware
- **Source:** information_request (html/md)
- **Context:** Technical context being requested from Lam
- **Quote:** "Any existing data pipelines, ingestion frameworks, or middleware that are already in place"

### Centralized ingestion pipeline
- **Source:** preliminary_approach, discovery_followup
- **Context:** Unified data plane component

### Dashboards / business intelligence tools
- **Source:** preliminary_approach (html/md)
- **Context:** Governance visibility surfaces
- **Quote:** "surfaced through dashboards or integrated with existing business intelligence tools"

### Scheduled scan (of data sources)
- **Source:** preliminary_approach
- **Context:** Detection mode for live data

### Asynchronous queue
- See category 1.

### "Standard tooling" (for updating detection rules/entity dictionaries/classification models)
- **Source:** discovery_followup
- **Quote:** "Detection rules, entity dictionaries, and classification models are updated through standard tooling."

### Change request process
- **Source:** engagement_pricing, poc_proposal
- **Context:** Commercial mechanism

---

## 17. Compliance / Standards / Frameworks Referenced

### Antitrust / regulatory standpoint
- **Source:** problem_restatement
- **Context:** Business-risk framing
- **Quote:** "both for the business relationship and potentially from a regulatory and antitrust standpoint"

### Export control constraints
- **Source:** discovery_followup_2026-04-06.html
- **Context:** Referenced as context for BayOne's prior work in semiconductor sector
- **Quote:** "BayOne has built detection and IP protection systems in similar environments, including semiconductor equipment companies with defense and export control constraints."

### Trade-restricted / embargo-country employees
- **Source:** problem_restatement
- **Context:** Employee types at Lam with compliance implications

### Defense / financial services (comparison industries)
- **Source:** preliminary_approach (html/md)
- **Context:** Named as industries where Microsoft Purview is used
- **Quote:** "used extensively in defense, financial services, and other regulated industries"

### Data governance capabilities (Azure)
- **Source:** discovery_followup
- **Context:** Azure advantage cited

### Confidentiality requirements / confidentiality practices (existing NDA)
- **Source:** engagement_pricing, poc_proposal
- **Context:** Governing constraints on data handling

### Regulatory or contractual requirements (referenced)
- **Source:** information_request (html/md)
- **Context:** Discovery inquiry
- **Quote:** "Any regulatory or contractual requirements that constrain how customer data is handled"

### Semiconductor industry / semiconductor equipment industry
- **Source:** problem_restatement, preliminary_approach, discovery_followup
- **Context:** Industry framing

### Retail, manufacturing (comparison industries)
- **Source:** preliminary_approach (html/md)
- **Context:** BayOne's prior engagement sectors
- **Quote:** "BayOne has applied this same methodology at prior engagements across semiconductor, retail, and manufacturing environments"

---

## 18. Equipment / Hardware

### Wafer fabrication equipment
- **Source:** problem_restatement (html/md)
- **Context:** Lam's core business identity; not a specific piece of equipment named
- **Quote:** "As a provider of wafer fabrication equipment, Lam has direct visibility into the production environments of customers"

### Mobile device (as data entry source)
- **Source:** problem_restatement (html/md)
- **Context:** Illustrative data entry scenario
- **Quote:** "A field engineer typing a problem statement from a mobile device might inadvertently include customer-identifiable information"

### Tool (as in semiconductor tool)
- **Source:** problem_restatement.md
- **Context:** Example ticket content
- **Quote:** "'I'm at Fab 11 and have an issue with this tool'"

**No specific hardware SKUs or product lines (Kiyo, Sense.i, etc.) are named in the deliverable set.**

---

## 19. BayOne Methodology IP / Frameworks Named

### "Layered Detection Methodology" / "Layered detection approach"
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown
- **Context:** Named BayOne methodology (3 sequential layers)
- **Quote:** "Layered detection approach: deterministic pattern matching, machine learning and NLP, and generative AI for contextual edge cases, applied sequentially"

### "Hybrid Architecture for Intelligent IP Protection"
- **Source:** preliminary_approach (title)
- **Context:** Named BayOne architectural framework

### "Hybrid Detection Architecture"
- **Source:** discovery_followup
- **Context:** Named section

### "Ingestion-First Architecture"
- **Source:** preliminary_approach
- **Context:** Named BayOne architectural principle

### "Unified Data Plane" / "Common Data Plane"
- **Source:** preliminary_approach, discovery_followup
- **Context:** Named BayOne architectural concept

### "Enterprise Tools Strategy"
- **Source:** preliminary_approach
- **Context:** Named section/principle

### "Application-by-Application Migration"
- **Source:** preliminary_approach
- **Context:** Named rollout strategy

### BayOne Solutions "Office of AI Strategy and Innovation"
- **Source:** engagement_pricing, pricing_breakdown (letterhead)
- **Context:** BayOne org unit identified on client-facing pricing documents
- **Quote:** "Office of AI Strategy and Innovation"

### Director of AI (Colin Moore)
- **Source:** engagement_pricing, internal_cost_breakdown
- **Context:** Project leadership role
- **Quote:** "Project Leadership - Director of AI, BayOne Solutions"

### Defined, Repeatable Evaluation Protocol (BayOne artifact)
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown
- **Context:** BayOne deliverable that "carries forward to subsequent phases"

### Detection Target Map (BayOne artifact)
- **Source:** poc_proposal, pricing_breakdown

### Accuracy Ceiling determination (BayOne artifact)
- **Source:** poc_proposal

### Data Quality Report (BayOne artifact)
- **Source:** poc_proposal, pricing_breakdown

### EDA Report (as engineering documentation) (BayOne artifact)
- **Source:** pricing_breakdown
- **Quote:** "Formal EDA report delivered as engineering documentation"

### Scaling Path documentation (BayOne artifact)
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown

### Methodology documentation (layer contribution to accuracy) (BayOne artifact)
- **Source:** engagement_pricing, poc_proposal, pricing_breakdown

### Internal references (not client-facing, flagged):
- **Risk Reserve (25%)** - internal_cost_breakdown: costing/pricing methodology
- **"Embed and expand" strategy** - internal_cost_breakdown: sales/account methodology
- **"BayOne costing workbook"** - internal_cost_breakdown: internal tool
- **20% load factor** - internal_cost_breakdown: costing convention

---

## 20. Anything Else / Uncategorized

### Gold standard (evaluation concept)
- **Source:** information_request, discovery_followup
- **Context:** Definition of clean content
- **Quote:** "This is the gold standard for what 'good' looks like."

### Subject Matter Expert (SME)
- **Source:** engagement_pricing, poc_proposal, information_request
- **Context:** Lam resource role required during POC

### Milestone-based payment structure (40/60 split)
- **Source:** engagement_pricing, pricing_breakdown
- **Context:** Commercial structure
- **Quote:** "40% - Kickoff and discovery phase complete; 60% - Detection build complete"

### $15,000 fixed price
- **Source:** engagement_pricing, pricing_breakdown, internal_cost_breakdown
- **Context:** Client-facing POC price

### $10,000 price (contradiction in poc_proposal.md)
- **Source:** poc_proposal_2026-04-09.md ONLY
- **Context:** The markdown version lists $10,000 while all other deliverables say $15,000. Flagged as discrepancy.
- **Quote (md):** "Proof-of-Concept (This Proposal) | $10,000"

### Two named Lam contacts
- **Source:** followup_email_draft_2026-03-12.md
- **Names:** Bradley Estes (Brad), Mikhail Krivenko
- **Context:** Lam addressees of follow-up email
- **Quote (internal):** "Brad (Managing Director, decision-maker)"

### Named internal BayOne contacts
- **Source:** internal_cost_breakdown (not client-facing)
- **Names:** Colin Moore (Director of AI), Anuj (referenced re: in-person recommendation)
- **Context:** Internal staffing/strategy references

### "India Resource (Mid-Level)" ($45/hr loaded rate)
- **Source:** internal_cost_breakdown_2026-04-09.html (INTERNAL ONLY)
- **Context:** BayOne internal staffing and rate
- **Flag:** Not disclosed to client

### Three-week POC timeline
- **Source:** All proposal docs
- **Context:** Engagement duration
- **Quote:** "Three weeks from data access"

### 18-month prior effort (Lam)
- **Source:** poc_proposal (html/md)
- **Context:** Reference to Lam's failed prior work
- **Quote:** "prior 18-month effort using multiple Named Entity Recognition (NER) models in parallel"

### Sub-1% false positive target
- **Source:** problem_restatement, preliminary_approach
- **Context:** Performance target

### 2-to-5-second response time requirement
- **Source:** problem_restatement, information_request
- **Context:** Real-time UI performance requirement being clarified

### One in-person trip
- **Source:** internal_cost_breakdown (INTERNAL)
- **Context:** Travel planning for POC demo/execution
- **Quote:** "One in-person trip for POC demo/execution"

### Generic technical terminology (entity types)
- **Source:** poc_proposal
- **Generic NER entity types:** person names, organizations, locations
- **Quote:** "standard NER models are trained on generic entity types (person names, organizations, locations)"

### PDF (attachment format)
- **Source:** followup_email_draft_2026-03-12.md
- **Context:** Attachment format of deliverables sent to Lam
- **Quote:** "Attachments: Balancing IP Protection with Productivity at Scale (PDF), Next Steps and Discovery (PDF)"

### Excel files (content type)
- **Source:** information_request (html/md)
- **Context:** One of the content types BayOne is asking about
- **Quote:** "If the selected application ingests multiple content types (text documents, Excel files, transcripts, images, database records)"

---

## Flags and Discrepancies Worth Highlighting

1. **GPT models mention only in .md of problem_restatement** — the .md version states "internally hosted AI tools (including GPT models deployed within Lam's own infrastructure)" but the .html version omits the parenthetical. Check which version was actually sent to the client.

2. **Pricing discrepancy in poc_proposal.md** — the markdown version shows $10,000 while all other documents (html version, engagement_pricing, pricing_breakdown, internal_cost_breakdown) show $15,000. Confirm final version sent.

3. **internal_cost_breakdown_2026-04-09.html** — explicitly marked "Internal Document - Do Not Share With Client." References India resource rate, Colin's hourly allocation, risk reserve %, margin analysis, strategic "embed and expand" notes, and names Anuj and Brad. MUST NOT appear in access request or in anything sent to Lam.

4. **pricing_breakdown_2026-04-09.html** — letterhead says "Prepared for Lam Research - April 2026 - Confidential" — appears client-facing. Contents match what would be appropriate to share.

5. **Azure AI Foundry vs. Azure Machine Learning / Azure OpenAI** — BayOne has committed to "Azure AI Foundry" specifically. Access request should reflect this exact service, not the older Azure ML or Azure OpenAI naming.

6. **Microsoft Purview with Custom Sensitive Information Types + DLP policies** — specifically promised in preliminary_approach and discovery_followup. Access request should explicitly reference Purview admin access and ability to create Custom SITs and DLP policies.

7. **Azure PostgreSQL + pgvector** — explicitly named as an alternative/fallback. If selected, access request would need PostgreSQL provisioning rights.

8. **Azure Blob Storage** — specifically named for document storage.

9. **Azure AI Search** — named as the implied default vector search (and the thing pgvector would replace). Access request should allow for either.

10. **VM (virtual machine)** — explicitly named as the form of environment access BayOne expects under Option A.

11. **Escalation Solver data access + five free-text fields** — the specific application and specific fields that need to be accessible.

12. **Reference lists from Lam** — customer names list, fab/location identifier list, exclusion list, previously labeled examples — all specifically called out as required inputs.

13. **Prior-effort baseline documentation** — Lam commits to providing "documentation of prior detection effort results and target performance aims to serve as a benchmark."

14. **Microsoft Teams transcripts** — referenced but not part of POC scope (document/attachment scanning is explicitly excluded). Noted here for completeness.

15. **BayOne methodology IP to protect** — Layered Detection Methodology, Hybrid Architecture, Ingestion-First Architecture, Unified Data Plane, Application-by-Application Migration, Defined Repeatable Evaluation Protocol, Detection Target Map, Accuracy Ceiling determination.
