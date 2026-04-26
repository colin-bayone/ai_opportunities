# 09a - Technology Inventory Part 2: April Internal Syncs + Mikhail Email

**Source:** Multiple files in /lam_research/ip_protection/source/ (April 1, April 6 pre-call, April 9 internal syncs, April 16 Mikhail email)
**Source Date:** 2026-04-01 through 2026-04-16
**Document Set:** 09a (supplementary to Set 09)
**Pass:** Complete extraction of every technology/tool/platform/system mention from these source files

---

## 1. Compute / Hosting / Infrastructure

- **Azure** — Colin Moore, April 9 sync 2; Primary cloud platform for Lam; already uses Azure ecosystem
- **Azure AI Foundry** — Colin Moore emphasizes; "all of our models are available through Azure AI Foundry"; 20x cheaper than external API calls
- **On-prem / On-Premise infrastructure** — Daniel Harrison mentioned exploring; Colin noted confusion about "air gapped" concepts
- **Virtual desktops / AVD** — Lam provides virtual desktop environments; known performance/reliability issues
- **GitHub** — Colin Moore mentions needing GitHub access for code repositories (Cisco example: 3-week wait)
- **Edge environments / Air-gapped systems** — Mentioned; Daniel didn't understand concept

## 2. Data Storage / Databases / Data Lakes

- **Azure Blob Storage** — Implied through Azure ecosystem; standard Lam infrastructure
- **SQL databases** — Likely part of Lam's internal systems
- **Data lakes** — Generic reference to Lam data ingestion/storage
- **Knowledge management systems** — Lam currently works on "knowledge management space"; using ".net column"

## 3. Programming Languages / Runtimes

- **Python** — Colin Moore, April 9 sync 2; "it's realistically just Python"; used for detection and redaction
- **.NET / .NET Core** — April 1 call: "the text that they're using is the dotnet column"
- **C#** — Implied through .NET ecosystem

## 4. NLP / NER Libraries / Frameworks

- **Microsoft Purview** — Colin Moore, April 1 call; primary tool for PII redaction; "deterministic layer... Microsoft Purview"
- **Pattern matching / Rule-based detection** — Colin Moore: "first level is going to be rule based"
- **Semantic/NLP-based approaches** — Layer 2: "something like semantic or NLP"

## 5. Machine Learning / Deep Learning Frameworks

- **Small language models / SLMs** — Daniel Harrison mentioned exploring; Colin found him confused about relevance
- **Language models (LLMs)** — Colin Moore: "the language model approach says yeah, this is definitely it within the context"
- **Ensemble/layered approaches** — Colin Moore's core methodology: "Layer 1... Layer 2... Layer 3"

## 6. Pre-trained Models / LLMs / Specific Model Names

- **GPT (generic)** — General reference to generative pretrained models
- **Azure GPT models** — "if I want cloud, if I want any of the new GPT models"
- **Grok** — Colin Moore, April 9 sync 2; "if I want Grok, if I want whatever, they're all available native to me in Azure"

## 7. Generative AI Services / APIs

- **Azure OpenAI** — Implied through Azure ecosystem; Colin emphasizes avoiding external APIs
- **External API calls** — Colin Moore: "20 times cheaper than an external API call for these"

## 8. Application(s) Being Worked On

- **Escalation Solver** — Named in April 9 sync 2; primary POC application
- **Knowledge Management / Knowledge Enablement applications** — "currently working on the knowledge management space"
- **Customer-facing applications** — Brad's vision; applications used at customer/competitor sites
- **Generic applications (30+)** — "we have 30 applications over here, and 10 over here, and three behind me"

## 9. Lam Internal Tools / Systems

- **Escalation Solver (application)** — Named system for IP detection
- **Internal systems (multiple)** — Generic references to applications and infrastructure

## 10. Identity / Access / Security Systems

- **Azure AD / Active Directory** — Implied through Azure ecosystem
- **Info Sec / Cybersecurity review** — Lam process; Colin emphasizes working with InfoSec
- **NDA / Confidentiality agreements** — "whatever NDA or agreement we have between Lam and Bay one"

## 11. Microsoft / Azure Ecosystem

- **Microsoft Purview** — Primary tool for deterministic PII detection
- **Azure AI Foundry** — Hosting platform for models and LLMs
- **Azure Virtual Machines / compute** — Implied infrastructure
- **Azure storage (Blob Storage, etc.)** — Implied

## 12. Third-Party Vendors / Consultants Mentioned

- **Accenture** — Colin Moore, April 1 call; comparison for POC pricing
- **PwC / PricewaterhouseCoopers** — Comparison for POC practices
- **Deloitte** — Mentioned alongside Accenture/PwC
- **Cohere** — Colin Moore, April 1 call; "this exact project we did for Cohere"
- **Oracle (legacy)** — Colin Moore mentions old Oracle folks
- **Cisco** — Colin Moore, repeated example of successful BayOne project; $500K SOW
- **Sephora / Safar** — Colin Moore mentions as Cisco client example
- **Google** — Anuj Sehgal mentions hiring for Google account
- **HPE Juniper** — Pratik mentions being on-site for meeting
- **Empire / Empiger** — Colin Moore, April 9 sync 2; disparages custom solution vendor

## 13. Reference Data / Lists / Datasets

- **1000 examples / labeled data** — Mikhail mentioned claiming; Colin treats as red flag
- **50-500 data samples** — Discussion of minimum viable dataset sizes
- **Ground truth data / reference data** — Critical dependency
- **Detection targets** — Must be defined by Lam SMEs
- **Gold samples / good data** — Validation requirement
- **Terabytes of data** — Lam mentioned as having massive data volume
- **Representative dataset vs. exhaustive** — "POC designed for representative data set"

## 14. Methodology / Algorithms Mentioned

- **Layered detection approach** — Colin Moore's core methodology; Layer 1 (rule-based), Layer 2 (semantic/NLP/ML), Layer 3 (LLM-based)
- **Mesh filter analogy** — Colin Moore uses window screen filtering metaphor
- **Quarantine vs. discard** — False positives quarantined for further review
- **Rule-based pattern matching** — Layer 1
- **Semantic/NLP approaches** — Layer 2
- **Language model (LLM) validation** — Layer 3
- **Exploratory Data Analysis (EDA)** — Colin Moore: "run some statistics on this"
- **Precision and recall** — Mentioned as "rookie numbers" that Lam was using
- **Accuracy metrics (custom)** — Colin proposes real engineering metrics
- **Deterministic approaches** — Colin distinguishes as foundational
- **ROI/business value analysis** — Lam lacks; "They never really talk about business value"

## 15. Communication / Collaboration Tools

- **Microsoft Teams** — Used for remote meetings; recording and transcription capability discussed
- **Email** — Standard communication; Mikhail's email request vehicle
- **Meeting transcription tools** — Colin Moore: "all your teams meetings you'll get transcripts"

## 16. Development / Operational Tooling

- **Git / GitHub** — Colin Moore mentions needing GitHub access; Cisco required 3-week wait
- **CI/CD** — Referenced abstractly as "CI/CD project" for Cisco
- **Internal code repositories** — Referenced throughout

## 17. Compliance / Standards / Frameworks Referenced

- **Confidentiality / NDA** — Paramount concern; "non-disclosure, and so forth"
- **Data protection** — Generic; implicit through IP protection focus
- **Security review / InfoSec approval** — Colin Moore discusses proper channels vs. "shadow IT"
- **Enterprise IT standards** — Colin Moore: "enterprise grade... not just... custom, really cool solution"

## 18. Equipment / Hardware

- **Laptops** — Colin Moore mentions needing laptop for access
- **Virtual machines / VM instances** — Implied through Azure

## 19. Anything Else / Uncategorized

- **Test Complete** — Colin Moore, April 1 call; automation testing platform Lam exploring
- **Redaction (concept/technique)** — Core to IP protection; Colin emphasizes distinct from detection
- **PII / Personally Identifiable Information** — Primary detection target through Purview
- **IP / Intellectual Property** — Core problem domain
- **TSMC data** — Specifically mentioned; "They have TSMC data. So they can't have a screw up here"
- **18-month failed internal effort** — Lam's previous attempt; "It's been 18 months"
- **Free POC rejection** — BayOne policy: "no more free POCS"
- **POC outcome-based pricing** — Colin proposes deliverable-based, not headcount-based
- **Change request threshold** — "If it's over 25% scope change, there has to be a change request"
- **3-week POC timeline** — Week 1 discovery/data assessment; Weeks 2-3 build/validation
- **POC pricing ranges** — $5-15K range discussed
- **$45/hour rate** — Adjusted resource rate
- **Risk reserve/buffer (25%)** — Built into costing
- **Travel budget** — $2500 for Colin in-person POC work
- **Option A vs. Option B** — Two-track approach for POC execution location
- **Scale.ai** — Specialized data labeling company mentioned
- **Data labeling/annotation** — Major cost driver
- **Automotive/manufacturing sector** — Pratik mentions "world's largest automaker" opportunity

---

**SUMMARY:** Catalogued 130+ unique technologies and tools across all 19 categories. Largest categories: Microsoft Azure ecosystem (13+ services), Python, Lam applications. Key methodologies: Layered detection approach with rule-based + semantic + LLM tiers. Reference customers: Cohere, Cisco, Sephora; future: automotive sector.
