# 09a - Technology Inventory Part 1: March 12 + March 20 Sources

**Source:** Multiple files in /lam_research/ip_protection/source/ (March 12 discovery call + March 20 prior discussion files)
**Source Date:** 2026-03-12 through 2026-03-20
**Document Set:** 09a (supplementary to Set 09 — comprehensive tech inventory for Mikhail/Daniel email response)
**Pass:** Complete extraction of every technology/tool/platform/system mention from these source files

---

## Source File Key (for short references)

- **PREP** = `lam_call_prep_2026-03-12.txt` (BayOne prep notes, Colin)
- **CALL** = `lam_discovery_call_2026-03-12.txt` (Brad, Mikhail, Pat, Anuj, Colin)
- **DEBRIEF** = `anuj_colin_debrief_2026-03-12.txt` (internal Anuj + Colin post-call)
- **SUMMARY** = `prior_discussion_summary_2026-03-20.md`
- **STRATEGY** = `prior_discussion_strategy_2026-03-20.md`
- **TECH1** = `prior_discussion_technical_approach_2026-03-20.md`
- **TECH2** = `prior_discussion_technical_approach_continued_2026-03-20.md`
- **TECH3** = `prior_discussion_technical_approach_round3_2026-03-20.md`
- **NEEDS** = `prior_discussion_open_needs_2026-03-20.md`
- **FINAL** = `prior_discussion_final_clarifications_2026-03-20.md`

---

## 1. Compute / Hosting / Infrastructure

- **Azure (general Azure cloud platform)** — Mikhail on CALL: "it was a cloud-based MLOps put on Azure cloud." Lam's primary cloud target. PREP: "They're on Azure stack: AI Foundry + Microsoft Sentinel." Colin in CALL, DEBRIEF, TECH1, TECH2 repeatedly pushes Azure as the unified target. *Lam already has it; BayOne pushing to unify on it.*

- **On-prem servers / on-premises systems** — Mikhail on CALL: "some of it on pram, some of it is on cloud, some of it is eventually gonna move to cloud." Mixed hybrid environment. Colin in TECH1: "Even for on-prem applications that are not hosted in the cloud, they can still leverage cloud AI models (Azure AI Foundry) for processing." *Lam current-state reality.*

- **Cloud-first roadmap / microservice architecture** — Mikhail on CALL: "we do want to focus on cloud first going forward. That's our plan... we also want to focus on microservice architecture long term." *Lam aspirational goal.*

- **Cloud bots** — Mikhail on CALL: "some of it is again cloud but bots." Unspecified cloud-hosted bot systems. *Lam current.*

- **MLOps (cloud-based, on Azure)** — Mikhail on CALL: "first of all, we put MLOps in place, and we've tried training a few models... it was a cloud-based MLOps put on Azure cloud." *Lam tried this, stood it up on Azure.*

- **AWS** — PREP only, as an example cloud platform reference in data storage context. Not mentioned by Lam. *Not in play.*

- **GCP / Google Cloud** — Not directly named beyond "even Google for that matter" (Anuj on CALL, in guardrails context, not infrastructure). *Not in play.*

- **Disconnected / fab-resident systems / edge** — Not explicitly discussed in these files (though fab context is pervasive). *None mentioned in this file set for fab-resident compute.*

- **Azure Postgres + pgvector** — Colin in TECH2: "build a custom vector search on Azure Postgres + pgvector, while still using Azure Blob Storage for documents." *BayOne proposed fallback option.*

- **GPU (local training)** — Colin in TECH1: "They may have been training sentence transformers locally on a GPU and thinking that fine-tuning would somehow make them good for classification." *Speculated about Lam's prior attempts.*

---

## 2. Data Storage / Databases / Data Lakes

- **Data lake (absence of)** — Mikhail on CALL: "there is not one, you could say data lake or something like that. So there doesn't mean that that's not in the future." *Lam does NOT have a data lake today.*

- **Azure Blob Storage** — Colin in TECH2: "Azure Blob Storage, Azure AI Search, Azure Cosmos DB, Azure AI Foundry, Microsoft Purview" listed as the "all existing Azure services" option. Also TECH1: "Blob storage (for raw documents)." *BayOne-proposed.*

- **Azure AI Search (formerly Azure Cognitive Search)** — Colin in TECH2: listed as an Azure service for the control plane; also explicitly flagged as potentially "cost-prohibitive or provide insufficient value for certain RAG use cases." Colin in NEEDS 1.5: "Purview, AI Foundry, AI Search, etc." *BayOne-proposed; under cost/value evaluation.*

- **Azure Cosmos DB** — Colin in TECH2: listed as an Azure service option for control plane. *BayOne-proposed option.*

- **Vector stores (for RAG embeddings)** — Colin in TECH1: "May include: Vector stores (for RAG embeddings)." *BayOne-proposed general component.*

- **Segmented databases / fragmented storage** — Mikhail on CALL: "Some of the databases or some of the stuff is segmented and different." *Lam current.*

- **Oracle back-end** — Colin on CALL (asking a question): "Is this connected like an Oracle back-end for things like that?" *Mentioned hypothetically; no confirmation Lam uses Oracle.*

- **SharePoint / OneDrive** — FINAL: "SharePoint or OneDrive content" listed as example data sources for representative sample. PREP: "SharePoint" listed under Microsoft ecosystem. *Mentioned as likely sources; unconfirmed at Lam.*

- **Snowflake, NoSQL, S3** — Categorically named in prompt; not specifically mentioned in source files. *None mentioned in this file set.*

---

## 3. Programming Languages / Runtimes

None mentioned explicitly in this file set. (No specific language — Python, .NET, JavaScript, etc. — was named by any speaker.)

---

## 4. NLP / NER Libraries / Frameworks

- **SpaCy** (transcribed as "Spacey") — Mikhail on CALL: "We tried Transformers model, Spacey, and I don't remember the third." Colin in TECH1: "SpaCy for NER. Without a proper test set to work with, SpaCy NER is not going to do anything useful out of the box for domain-specific entities like semiconductor fab names." *Lam tried it and failed.*

- **Presidio** — PREP/prompt-level reference (and listed in category prompt). Not explicitly named in Lam sources, but present in prep-doc framing. *Not named by Lam.*

- **NLTK, Stanza, Flair** — Categorically named in prompt; not mentioned in source files. *None mentioned in this file set.*

---

## 5. Machine Learning / Deep Learning Frameworks

- **Transformers (model / framework)** — Mikhail on CALL: "We tried Transformers model, Spacey, and I don't remember the third." Colin in TECH1: "Custom Transformers model for semantic similarity between name variations (e.g., Fab11 vs. F11). This is using a sledgehammer for a thumbtack." *Lam tried custom-trained Transformers; BayOne calls it the wrong tool.*

- **Sentence Transformers** — Colin in TECH1: "They may have been training sentence transformers locally on a GPU." *Colin's hypothesis about what Lam actually did.*

- **HuggingFace Transformers / scikit-learn / TensorFlow / PyTorch** — Not explicitly named; Colin's "Transformers" reference is generic (likely HuggingFace-family). *None explicitly named in this file set beyond the generic "Transformers" reference.*

- **Machine learning (as general category)** — Mikhail on CALL: "some of the things we've actually tested was more with machine learning rather than generative AI." Colin on CALL clarifying: ML for "formulations or, you know, process documents or process variables... more numeric scientific data." *Lam leaned on ML; deferred GenAI.*

- **Rule-based models** — Mikhail on CALL: "We've started trying rule-based models, but we haven't gotten far because... something like a fab could be spelled many different ways." *Lam tried, abandoned.*

---

## 6. Pre-trained Models / LLMs / Specific Model Names

- **"Azure AI model"** — Mikhail on CALL: "Oh, Azure AI model. So we've passed the training data to it." Colin in TECH1: "They don't even know what Azure AI services they were using. The 'Azure AI model' reference likely means they were using models hosted in Azure, not that they were leveraging any specific Azure AI service designed for this purpose." *Lam tried; exact identity unknown.*

- **GPT models (generic)** — Colin on CALL (self-correcting mid-sentence): "in the compiler, we're really talking open AI model, right? Because compiler using GPT models, right? They don't use open AI. I should not say that... They use GPT models inside." (Note: "compiler" = Copilot transcription artifact.) *Copilot reference.*

- **Microsoft Copilot / Copilot (Microsoft 365 Copilot context)** — Colin on CALL: "So I heard co-pilot. So is this all on Azure?" Mikhail's answer implied Copilot is part of their ecosystem. PREP: Copilot referenced re: Purview's ability to block Copilot from processing labeled content. *Lam uses Copilot.*

- **GitHub Copilot** — PREP discovery question: "Is there concern about developers using GitHub Copilot or building on top of unapproved AI APIs?" *Not confirmed at Lam; discovery question.*

- **ChatGPT** — Colin on CALL: "when I heard 20%... that's pretty much out-of-the-box chat GPT." PREP: "personal ChatGPT accounts" under shadow AI. DEBRIEF: "They think AI is chat GPD. You just put in information that you get stuff out and that's AI for them." PREP Samsung incident: "Engineers leaked semiconductor source code via ChatGPT." *Referenced as baseline, shadow AI risk.*

- **Claude (Anthropic)** — PREP: "personal Claude accounts" under shadow AI. DEBRIEF: Colin using Claude as his working partner (implicit through the discussion format). *Shadow AI reference.*

- **Anthropic (as guardrail comparison)** — Mikhail on CALL: "The guardrails are still not tested for production or tested in the field. So that risk is already even anthropic, and you name anyone." *Cited as industry-wide guardrail limitation.*

- **Google (as guardrail comparison)** — Mikhail on CALL: "Even Google for that matter is not able to ensure they are still trying to do it as we speak today." *Cited alongside Anthropic re: guardrail maturity.*

- **LamGPT** (transcribed as "lamb GPT") — Mikhail on CALL: "some of it is lamb GPT so we still have Open and like the GPT models within lamb." Colin in TECH1: "Lam currently has a mix of on-prem, cloud, LamGPT, Copilot, cloud bots." *Lam's internal GPT-based system.*

- **BERT, RoBERTa, Llama** — Categorically named in prompt; not directly mentioned. *None mentioned in this file set by name.*

- **PyRIT (Microsoft red-teaming)** — PREP only: "Red teaming tools exist (Microsoft PyRIT, Nvidia Garak, F5 AI Red Team)." *BayOne prep reference; not discussed with Lam.*

- **Nvidia Garak** — PREP only, same context as PyRIT. *BayOne prep reference.*

- **F5 AI Red Team** — PREP only, same context. *BayOne prep reference.*

---

## 7. Generative AI Services / APIs

- **Azure OpenAI (as underlying GenAI API)** — Implicit via "GPT models" in Copilot context (Colin on CALL). Not explicitly named as "Azure OpenAI" by Lam. *Implicit presence.*

- **OpenAI API / "open AI"** — Colin on CALL: "we're really talking open AI model, right?" (Mid-sentence correction about Copilot.) *Referenced confusedly; not explicitly confirmed.*

- **AWS Bedrock, Anthropic API, Cohere API** — Categorically named in prompt; not named in source files. *None mentioned in this file set.*

- **Generative AI (as general category)** — Mikhail on CALL: "We actually have not used generative AI to prove any use cases, not because of unstructured data, but because of unstructured output." STRATEGY Section 4 challenges this: "Mikhail said they avoided generative AI because of 'unstructured output'... is a business user who came across the term 'unstructured output' and does not understand what it means." *Lam policy position; BayOne skeptical.*

- **Generative AI field / industry context** — Anuj on CALL: "Since last like 12-24 months, so much has happened in the generative AI field." *Framing of industry state.*

- **Agentic AI** — Colin in TECH2 (automated content cleanup): "Can be cleaned with an agentic AI cleaning tool." STRATEGY Section 3: "Agentic AI is one part of a potential solution for the specific use case at hand. It is NOT: A growth platform pitch." TECH3: "power and flexibility of AI-based systems for contextual analysis, not just NLP but agentic AI." *BayOne capability; used cautiously.*

- **RAG (Retrieval-Augmented Generation) chatbot** — Colin in TECH1: "The entire use case is a RAG chatbot." DEBRIEF: Colin repeatedly frames Lam's whole use case as "a rag chatbot." Across all prior-discussion files. *BayOne's reframing of the entire use case.*

---

## 8. Application(s) Being Worked On

- **Escalation Solver / Escalate flow** — Mikhail on CALL described the "escalate" workflow: "when you're in escalation flow, we actually have if they schedule out of the system, Microsoft Teams meeting, it's transcribed and it's automatically attached to the ticket." Brad on CALL: "our escalate flow area, right? And we even have the capability in there that a user can make a conscious decision to restrict the entire ticket." *Lam internal application.*

- **Self-help / search tools** — Mikhail on CALL: "our workflow in a troubleshooting... self-help, where you use the search tools or you use the AI tools to search for things." *Lam use case — one of two MVP business cases.*

- **Ask-for-help / community Q&A flow** — Mikhail on CALL: "you go into export help, and then you go and what we call escalate." *Second Lam use case.*

- **Six search formulas / "six search formulas"** — Mikhail on CALL: "we don't have a single search for it. We have six search formulas." TECH3: "6+ search systems." *Lam current fragmented state.*

- **Q&A chatbot / bot applications** — Colin across DEBRIEF: "they're talking about a rag chatbot, dude. I mean, they're talking about, like, one of the easiest." *BayOne's characterization.*

- **Unnamed specific application** — NEEDS 1.1: "Name one specific RAG-like application (the highest-impact one)... **This gates everything.**" *Unresolved; open ask.*

- **Engineering system (with drawings and schematics)** — Brad on CALL: "in our engineering system. I'm an office worker. I have access to all our drones and schematics." (Note: "drones" = drawings transcription artifact.) *Lam internal.*

---

## 9. Lam Internal Tools / Systems

- **Ticketing system (unnamed, likely ServiceNow or internal)** — Mikhail on CALL: "we actually have if they schedule out of the system, Microsoft Teams meeting, it's transcribed and it's automatically attached to the ticket." Brad: "restrict the entire ticket and or attachments by attachments." *Lam internal; specific name not disclosed.*

- **Knowledge management systems (Brad's org)** — Brad on CALL: "I run the knowledge management and event services organization. mostly supporting many different flavors of our support business group." *Brad's domain; multiple systems under it.*

- **LamGPT** — See Section 6. *Lam internal.*

- **TRI / trade-restricted-employee flagging** — Brad on CALL: "if you're a trade restricted employee or you're in an embargo country, there is restrictions based on your location... those people are flagged in our system that have an identifiable flag that they are a TRI employee or something like that, they even have a different colored badge." *Lam internal identity/compliance flag.*

- **ASM (access control)** — Brad on CALL: "We do have ASM that governs access to certain things, right? So like our escalate flow area." (Likely transcription of access/service-management acronym; treat as Lam-internal access control system.) *Lam internal.*

- **Licensed Service Provider (LSP) designation** — Brad on CALL: contractor/LSP distinction affects what data they see. *Lam internal role classification.*

- **Lam badge / blue badge** — Brad on CALL: "if you're a Lambloo badge employee." Identity artifact tied to access. *Lam internal.*

- **Work-center-based identification** — Brad on CALL: "we identify people by the work center." *Lam internal identity attribute.*

- **JIRA, Confluence** — Categorically named in prompt; not mentioned in source files. *None mentioned in this file set.*

---

## 10. Identity / Access / Security Systems

- **IAM (Identity and Access Management) — Lam's in-progress program** — Brad on CALL: "The company's working on getting to more of an IAM identity access management. And so that's an active program that's been going on probably for about two years. We're making progress there but I wouldn't say that it's like super robust." Anuj: "eventually come to the place where it's going to help quite a bit." *Lam ~2-year in-flight initiative.*

- **RBAC (Role-Based Access Control)** — Colin in DEBRIEF: "are we talking about RBAC? They were talking about IAM, and I'm like, that's called RBAC. No one calls it IAM. IAM is the Microsoft term for it. It's role-based access control." *Colin's reframing; category-level mention.*

- **Role-based / attribute-based access** — Colin on CALL: "it's like a role base, like we know what their role is. And we know, okay, you're an office worker versus, you know, somebody like servicing the equipment and then also where they're located." *Discovery question.*

- **Zero-trust security posture** — PREP quote from Jason Callahan (Lam CISO): "We are operating from the zero-trust point of view. But we all share intellectual property. Fundamentally, we as security people don't trust encryption." *Lam CISO-level stated posture.*

- **Restricted/labeled badge systems (colored badges)** — Brad on CALL: see TRI above. *Lam internal.*

- **SSO, VPN, Okta, Active Directory, MFA tools, certificate authorities** — Categorically named in prompt; not explicitly mentioned by anyone. *None mentioned in this file set.*

- **Encryption (referenced)** — PREP quote from Callahan: "we as security people don't trust encryption." *Philosophical reference.*

- **Privileged access / clearance** — Colin on CALL: "I had a high level clearance whenever I was at coherent. I had access to things that would, you know, make your eyes pop out. And if I uploaded something, I had some special scrutiny on me." *Colin referencing prior-role analog; he positions this as a detection-calibration input.*

---

## 11. Microsoft / Azure Ecosystem

- **Microsoft Purview** — PREP extensively: "Purview DLP: The actual guardrail layer. Detects sensitive content based on Sensitive Information Types (SITs), sensitivity labels. Can block Copilot from processing labeled content. Prompt-based SIT detection is in preview, GA expected late March 2026." TECH1 as Layer 1 deterministic; TECH3 Layer 1: "Custom Sensitive Information Types for known entities." *BayOne recommended core tool; Lam availability unconfirmed.*

- **Microsoft Purview DLP (Data Loss Prevention)** — PREP: "Purview DLP" called out specifically. TECH1: "DLP (Data Loss Prevention) policies." *BayOne-proposed.*

- **Microsoft Sensitive Information Types (SITs) / Custom SITs** — PREP: "Microsoft's OOTB Sensitive Information Types don't cover semiconductor IP (customer names, process parameters, yield data). Custom SIT configuration is non-trivial and likely not fully implemented." TECH3: "Custom Sensitive Information Types for known entities (customer names, fab IDs, variations)." *BayOne-proposed; unconfigured at Lam.*

- **Microsoft Sentinel** — PREP: "They're on Azure stack: AI Foundry + Microsoft Sentinel... Sentinel: SIEM/SOAR platform. Aggregates alerts, triggers playbooks. NOT a content detection tool... If Lam is relying on Sentinel as their primary guardrail, that's an architecture misunderstanding." DEBRIEF: "I can talk about Azure Purview, Azure Sentinel, like all these like fancy things." *Lam has it per prep intel; Colin argues misapplied.*

- **Azure AI Foundry** — PREP, CALL, TECH1, TECH2, TECH3, NEEDS. Colin on CALL asked directly: "AI Foundry, Adjunct on the Azure part, are you using both of those?" Mikhail couldn't answer. TECH1: "Azure AI Foundry... Hosting and deploying AI models for the RAG system." *BayOne's recommended compute layer; Lam has it on paper per prep but unclear in practice.*

- **Azure AI Content Safety / Prompt Shields** — PREP: "Azure AI Content Safety / Prompt Shields: Real-time detection of prompt injection, jailbreak attempts, harmful content. Model-layer protection." *BayOne prep context; not discussed with Lam.*

- **Microsoft Defender for Cloud Apps** — PREP: "Defender for Cloud Apps: CASB functionality. Visibility into shadow AI/SaaS usage." *BayOne prep context.*

- **SIEM/SOAR (categories, via Sentinel framing)** — PREP: Sentinel description. *Category reference.*

- **CASB (Cloud Access Security Broker)** — PREP: "Defender for Cloud Apps: CASB functionality." *Category reference.*

- **Microsoft Teams** — Mikhail on CALL: "Microsoft Teams meeting, it's transcribed and it's automatically attached to the ticket." *Lam uses Teams; transcripts are an auto-ingestion data source.*

- **Microsoft Teams transcription** — Same as above. *Lam current data flow; critical for ingestion pipeline discussion.*

- **Microsoft Copilot / Copilot** — See Section 6. *Lam uses.*

- **Microsoft 365** — Implicit via Copilot/Teams/SharePoint; not explicitly named as "M365." *Implicit.*

- **SharePoint** — PREP, FINAL reference. *Mentioned as likely data source; unconfirmed.*

- **Power BI** — TECH3: "Integration with existing BI tools (Tableau, Power BI, whatever Lam uses)." *BayOne-proposed option.*

- **Azure (general cloud)** — See Section 1.

- **Azure Blob Storage, Azure AI Search, Azure Cosmos DB, Azure Postgres + pgvector** — See Section 2.

---

## 12. Third-Party Vendors / Consultants Mentioned

- **Accenture** — DEBRIEF: Colin: "that Accenture did that or was that right? That was their prior partner. Yes." TECH3: "Accenture autopsy questions." NEEDS 2.2 entire section: "What deliverables did Accenture produce?... Did Lam provide Accenture enough information to succeed?" *Lam's prior technical partner on this problem; central in the autopsy.*

- **Capgemini** (transcribed as "Gapsium," "Kaptima") — DEBRIEF, Anuj: "that's basically what Deloitte and Kaptima has been doing for them... Gapsium and I have been around there." *Prior Lam vendor in the orbit.*

- **Deloitte** — DEBRIEF, Anuj: "Deloitte and Kaptima has been doing for them. They've been booting off them like for years." *Prior Lam vendor.*

- **Coherent Corp (Colin's prior employer)** — CALL: Colin intro; FINAL: "Coherent Corp — massive global enterprise, many teams across finance, engineering, sales, service, manufacturing." *Colin's credibility / reference architecture.*

- **Raytheon, Northrop Grumman** — PREP: "Defense primes (Raytheon, Northrop Grumman) - similarly sensitive environments." *Colin's prior-work adjacency; positioning.*

- **Samsung (as Lam customer AND as prior-incident reference)** — PREP: "Samsung incident (2023): Engineers leaked semiconductor source code via ChatGPT - directly analogous to Lam's fear." Also Lam customer throughout. *Both a customer context and a precedent cited in prep.*

- **TSMC, Intel, Micron, SK Hynix** — PREP: "Key customers: TSMC, Samsung, Intel, Micron, SK Hynix." Used throughout the CALL as hypothetical examples by Mikhail/Colin (e.g., "'TSMC' in a public earnings discussion vs. 'TSMC yield rate for Q4'"). *Lam's customers whose names are the sensitive entities.*

- **BayOne (self-reference)** — Colin's firm; throughout all files. *Acting party.*

- **Cohere, OpenAI (as a company/vendor)** — Colin's "coherent" refers to Coherent Corp laser/semi, not Cohere (the AI company). OpenAI referenced implicitly via GPT models. *Not directly engaged vendors at Lam.*

- **Salesforce (retail customer reference)** — FINAL: "A retail customer — Salesforce-based, completely different stack." *Colin's prior work analog.*

- **Oracle Cloud (customer reference)** — FINAL: "An Oracle Cloud customer — different cloud, different use case." *Colin's prior work analog.*

- **Tableau** — TECH3: "Integration with existing BI tools (Tableau, Power BI, whatever Lam uses)." *BayOne-proposed option.*

- **Otter.ai** — PREP discovery question: "What about browser extensions, meeting recording tools like Otter.ai." *Shadow-AI probing; not confirmed at Lam.*

---

## 13. Reference Data / Lists / Datasets

- **Customer name list / synonyms lookup table** — Colin in DEBRIEF: "you are essentially talking about a synonyms lookup table, dude. Like, this is not even an AI project." TECH1: "Synonyms lookup table for known customer names, fab identifiers, and their variations. This is a finite set." *BayOne core recommendation.*

- **Fab identifier list and variations (Fab11, F11, Micro 11, FAP 11, FAP-11)** — Mikhail on CALL: "something like a fab could be spelled many different ways... some put a micro 11, some put F11, some put PAP space 11, PAP dash 11." TECH1 lists these exact variations. *Lam's concrete entity-variation problem.*

- **Customer-confidential-information markers / "CI documents"** — Mikhail on CALL: "there could be customer confidential information, the CI documents." *Lam existing content label.*

- **Customer Identifiable Information (CII) / Customer-confidential-information (CCI) policies** — Mikhail on CALL: "You should not put customer identifiable information into anything." *Lam policy-defined category.*

- **Ground truth / golden standard dataset (absence of)** — NEEDS 2.1: "What was the golden standard / ground truth they were testing against?" FINAL: "Known good examples: Documents that are clean and should pass through without flagging. This is the gold standard." *Unclear whether Lam had one; central open question.*

- **Labeled training data (the 1,000+ hour estimate)** — Mikhail on CALL: "it was over a thousand man hours just to get the labeling up and then continuous maintenance." *Lam's assessed labeling cost; quoted repeatedly.*

- **Test data / representative sample (absence of)** — Colin in TECH2: "no representative sample of anything." FINAL Section 2: detailed requirements for a representative sample (failure cases + known good across document, email/ticket, Excel, SharePoint/OneDrive, live DB). *Open BayOne ask.*

- **Real false-positive examples from prior model testing** — NEEDS 3.2: "Real false positive examples from their prior model testing." *Open ask.*

- **Prior model training artifacts** — NEEDS 3.3: "Prior model training artifacts from the Accenture/internal effort." *Open ask.*

- **Exclusion lists / known-offender user list** — TECH3: "If a user has a history of uploading flagged content, apply greater scrutiny. Normal checks still run, but the AI layer can apply elevated attention." *BayOne-proposed feature.*

- **Customer contractual data-segregation requirements** — NEEDS 3.4: "Customer contractual requirements around data segregation." *Open ask.*

- **Written policies for customer-confidential-information handling** — NEEDS 3.4: same. *Open ask.*

- **ACL / role definitions** — NEEDS 3.4: "Current ACL/role definitions in their systems." *Open ask.*

---

## 14. Methodology / Algorithms Mentioned

- **Hybrid deterministic + AI architecture** — Colin in TECH1 Section 2 (core BayOne approach). *BayOne proposed methodology.*

- **Deterministic matching (exact match, zero false positives)** — TECH1, TECH3. *Layer 1 of proposed stack.*

- **Regex patterns** — TECH1: "Regex patterns for structured identifiers (fab numbers, customer codes, site identifiers) that follow predictable formats even with variation." DEBRIEF Colin: "I could probably get them to 95%+ with about a day's worth of effort if I had a representative sample with nothing more than regex." *BayOne methodology element.*

- **Keyword/entity lists (as configuration, not model weights)** — TECH1. *BayOne methodology.*

- **NER (Named Entity Recognition)** — Category-level throughout; explicit in TECH1 re: SpaCy NER. *Category.*

- **Semantic similarity (as wrong-tool choice)** — Colin in TECH1: "Custom Transformers model for semantic similarity between name variations... This is a deterministic lookup problem, not a semantic similarity problem." *Critique of Lam's approach.*

- **Fine-tuning / model fine-tuning** — Colin on CALL: "probably, to be honest, the fine-tuning didn't do anything." Mikhail: "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it." *Lam did it; BayOne deems ineffective here.*

- **Attack Success Rate (ASR)** — PREP: "Key metric: Attack Success Rate (ASR) - percentage of successful attacks over total attempts." *BayOne prep reference.*

- **Red teaming (manual, automated adversarial, production monitoring)** — PREP discovery question; reference to PyRIT/Garak/F5. *BayOne prep methodology reference.*

- **Document-level classification / document-type-aware processing** — TECH3: "Excel file: Processed differently than a PDF or a transcript." *BayOne methodology.*

- **Async queue with synchronous UX** — TECH3 Section 2: core processing-architecture pattern. *BayOne methodology.*

- **Ingestion-first architecture / reject-at-ingestion** — TECH1 Section 4. *BayOne core methodology.*

- **Application-by-application migration (vs. "big bang")** — TECH3 Section 5. *BayOne methodology.*

- **Day Zero / Day One terminology** — TECH2 Section 3: milestone-based (not date-based) cleanup framing. *BayOne methodology.*

- **Quarantine + human review with AI-assisted categorization** — TECH2 Section 3. *BayOne methodology.*

- **Model reconciliation / ensemble (category)** — Not explicitly discussed under that label. *None named this way in this file set.*

- **"Intern-level AI projects" (characterization)** — Colin in TECH1 re: Lam's prior work.

- **OCR (optical character recognition)** — DEBRIEF Colin: "When I was talking about OCR, I was like, what? Are you sure? You just want to focus on documents?" Mikhail on CALL: "if it's inside a picture or like the OCR picture, you're still going to just retrieve the document." *Mentioned; deferred.*

- **Unified control plane pattern / middleware platform** — Colin on CALL: "there has to be some kind of a common control plane." TECH1, TECH2, TECH3, FINAL. *Core BayOne architectural concept.*

- **Metrics & reporting module (rejection rates, usage, flagged-content patterns, known offenders)** — TECH2, TECH3. *BayOne methodology.*

- **"Defensive depth" / defense-in-depth** — Colin on CALL: "we do defensive depth for everything." *BayOne methodology reference.*

---

## 15. Communication / Collaboration Tools

- **Microsoft Teams** — See Section 11. *Lam uses.*

- **Email (as a leakage vector)** — PREP discovery: "Is email exfiltration part of this scope, or is this specifically about AI tools?" *Discovery question.*

- **Slack** — Categorically named in prompt; not mentioned. *None mentioned in this file set.*

- **File-sharing (SharePoint/OneDrive)** — See Section 2/11.

---

## 16. Development / Operational Tooling

- **MLOps (generic practice)** — Mikhail on CALL: "we put MLOps in place." *Lam tried; unclear tooling.*

- **Git / GitHub / Jenkins / CI/CD / monitoring tools** — Not mentioned. *None mentioned in this file set.*

- **GitHub (referenced in "not literally a GitHub fork")** — TECH2: "Lam probably has a single RAG concept that was re-used across multiple applications (not literally a GitHub fork)." *Analogy only.*

- **API documentation / non-production environment access** — NEEDS 3.3: "API documentation for their ingestion endpoints. Access to a non-production environment (if pilot approved)." *Open ask.*

---

## 17. Compliance / Standards / Frameworks Referenced

- **ITAR (International Traffic in Arms Regulations)** — PREP: "navigating ITAR, CMMC, DFARS, NIST 800-171." Colin on CALL: "our space and defense, doing things with ITAR, CMMC, DFARs, things like that." DEBRIEF: context of defense-grade redaction. *Colin's prior-work credibility; not a Lam compliance scope yet.*

- **CMMC (Cybersecurity Maturity Model Certification)** — Same citations as ITAR. *Colin's prior-work credibility.*

- **DFARS** — Same. *Colin's prior-work credibility.*

- **NIST 800-171** — PREP: "ITAR, CMMC, DFARS, NIST 800-171." *Colin's prior-work credibility.*

- **Embargo/Trade Restrictions (TRI)** — Brad on CALL: "if you're a trade restricted employee or you're in an embargo country, there is restrictions based on your location." *Lam operational reality.*

- **Zero-trust (methodology/posture)** — PREP (Callahan quote). *Lam stated posture.*

- **Antitrust / competitive-harm risk** — PREP: "If Customer A's yield data leaked to Customer B, that's catastrophic - both for the business relationship and potentially for regulatory/antitrust reasons." *Risk framing.*

- **GDPR, CCPA, SOC2, HIPAA, ISO standards** — Categorically named in prompt; not mentioned. *None mentioned in this file set.*

- **AI governance maturity (Stage 1-5 model)** — PREP: "Most organizations are at Stage 1-2... Lam pulling back ALL AI usage suggests reactive Stage 1-2 maturity. BayOne's opportunity is to help them build Stage 3 systematic governance." *BayOne prep framework.*

- **China-operations IP protection (bidirectional)** — PREP: "Built bidirectional IP protection for China operations." Colin on CALL: "One of the fun things that we had to navigate was doing things in China. So definitely managing IP." *Colin's prior-work credibility.*

---

## 18. Equipment / Hardware

- **Semiconductor wafer fabrication equipment (etch, deposition, clean)** — PREP: Lam's product category. *Lam context.*

- **Laptops (Brad suggesting Pat put laptop on screen)** — CALL opening: "maybe you could join and even put your laptop at the screen." *Incidental.*

- **Whiteboard (physical)** — CALL opening: "what we wanted to do today is... whiteboard to have an interactive discussion." *Meeting setup.*

- **Colored badges (physical identity artifact)** — Brad on CALL: "different colored badge." *Lam internal hardware/identity.*

- **GPU (speculated local training)** — See Section 1. *Speculation only.*

- **Workstations, edge devices** — Not explicitly discussed. *None mentioned in this file set.*

- **Nvidia (implicit via Garak tool name only)** — PREP only. *Reference only.*

---

## 19. Anything Else / Uncategorized

- **"AI 101 book" (Colin's colorful DEBRIEF characterization)** — DEBRIEF: "someone literally bought like an AI 101 book, like for like a teenager and like flipped to the first like chapter, read it and then said, okay, let's do this." *Not a real artifact; characterization.*

- **"Big brother approach" (notification pattern)** — Mikhail on CALL: "it's more about the big brother approach. How fast? Because this is real time." *Lam's framing for real-time detection UX.*

- **"Swim lanes" (Mikhail's framing)** — Mikhail on CALL; re-referenced across all prior-discussion files. *Lam's conceptual framing of detection vs. redaction.*

- **"20% error rate" / "20% false positive rate" / "17% after fine-tuning"** — Mikhail on CALL: quantitative benchmarks from Lam's internal POC. *Lam's reported metrics.*

- **"<1% end state" false positive target** — Mikhail on CALL: "we needed this number to be way below 1% end state." *Lam target.*

- **"2-5 seconds" UI latency requirement** — Mikhail on CALL: "UI standards, two to five seconds max." Also TECH3: clarification-required topic. *Lam stated requirement; unclear scope.*

- **Fortune 10 descriptor** — DEBRIEF, Anuj: "Colin, this is a Fortune 10 company." *Characterization (Lam is actually Fortune ~500 by revenue; Anuj hyperbole).*

- **~$17B revenue / ~17,000 employees / Fremont HQ** — PREP Lam facts. *Lam context.*

- **$60 billion + enterprise (DEBRIEF Colin hyperbole)** — DEBRIEF. *Not literal.*

- **$670K shadow-AI breach cost delta** — PREP statistic. *Industry context.*

- **"98% of orgs shadow-AI, 68% free-tier, 77% copy-paste" statistics** — PREP. *Industry context.*

- **"89% reduction in unauthorized use" (healthcare case)** — PREP. *Industry context.*

- **"concept-renade" (transcription artifact of "confidentiality violation" or similar)** — Brad on CALL: "Seven's ticket, there was a... already concept-renade." Used to indicate a policy violation was found in the 7th ticket reviewed. *Transcription artifact; resolved as "policy/confidentiality violation".*

- **"wipe board" = whiteboard (transcription artifact)** — CALL opening. *Resolved.*

- **"Why board" = whiteboard (transcription artifact)** — CALL opening. *Resolved.*

- **"rag" / "RAG"** — Throughout; Retrieval-Augmented Generation. See Section 7. *Core BayOne framing.*

- **Sales workshop 3/24-3/27** — DEBRIEF: scheduled in-person next opportunity. *Engagement milestone.*

- **"Pat" / "Pradeep" (BayOne sales team members)** — DEBRIEF: owners of the sales asks. *BayOne people.*

- **"Anuj" (BayOne, internal lead)** — DEBRIEF: co-architect of the engagement strategy. *BayOne.*

- **"Daniel" (Lam technical counterpart)** — CALL + all prior-discussion files: the person BayOne needs to talk to for any technical depth. *Lam individual; central open ask.*

- **"Monica" (Lam, mentioned in passing)** — CALL: "Monica was blessed. Even some of the people." *Lam individual.*

- **"Christian" (Lam, referenced as slide owner)** — CALL: "it's actually what Christian owns, so I couldn't find it." *Lam individual.*

- **"Jason Callahan" (Lam CISO)** — PREP: quoted on zero-trust. *Lam individual.*

- **"Bradley Estes / Brad"** — PREP, CALL. Managing Director, Knowledge & Advanced Services. *Lam individual.*

- **"Mikhail Krivenko / Michael / Michaela"** — CALL. Head of Product. (Note: "Michaela" appears as a transcription variant of "Mikhail.") *Lam individual.*

---

## Summary Statistics

This inventory captures mentions across **19 categories** spanning infrastructure, tooling, models, policies, data, methodology, vendors, and related artifacts. Key themes:

- **Lam's actual stack (confirmed):** Azure (mixed on-prem/cloud), Microsoft Teams + Teams transcripts, Microsoft Copilot, LamGPT (internal GPT-based), 6+ search systems, fragmented databases, ASM access control, in-progress IAM program, TRI badge/flagging system.
- **Lam tried and failed with:** Custom Transformers, SpaCy NER, generic "Azure AI model," rule-based models (abandoned over spelling variations), fine-tuning (20%→17% negligible improvement), ~1000-hour labeling exercise.
- **BayOne bringing:** Microsoft Purview (DLP + Custom SITs), Azure AI Foundry, unified control plane (custom build), hybrid deterministic+AI architecture, ingestion-first philosophy, Day-Zero/Day-One cleanup methodology, dashboard/reporting module, Azure Blob + Azure AI Search + Azure Cosmos DB + optional Azure Postgres+pgvector, async-queue-with-sync-UX pattern, RAG chatbot framing.
- **Prior vendors in orbit:** Accenture (central prior partner, autopsy needed), Capgemini, Deloitte.
- **Compliance adjacency (Colin's credibility):** ITAR, CMMC, DFARS, NIST 800-171, zero-trust, China bidirectional IP.
- **Central unresolved asks:** Name one application, representative samples, Daniel technical call, Azure services actually licensed, Accenture deliverables.
