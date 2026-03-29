# BayOne AI Opportunities Catalog

## Current as of March 2026

---

## 1. Lam Research — Custom NER and Sensitive Data Redaction

**Client contacts:** Bradley Estes (Managing Director, Knowledge & Advanced Services), Mikhail Krivenko (Head of Product), Daniel (technical lead, not yet met)

**Problem statement:** Lam Research has pulled back all AI and GenAI usage organization-wide due to concerns about sensitive information leaking through these tools. Their customers are direct competitors with each other (TSMC, Samsung, Intel, Micron), so IP protection is existential. They need custom detection and redaction for semiconductor-specific sensitive entities at under 1% false positive rate for real-time use and high accuracy for batch redaction.

**Two distinct use cases surfaced in discovery:**

1. Self-help search: Users search knowledge bases for troubleshooting, but over-restriction blocks useful cross-customer solutions. A Samsung fix exists but an Intel user can't see it because it's customer-restricted. Goal is to surface solutions without leaking customer-specific IP.
2. Escalation and ticket intake: Users inadvertently include customer names, fab numbers, and sensitive details in unstructured text when opening tickets. Needs real-time detection (2-5 second response, under 1% false positive) and batch redaction before data enters the general knowledge pool.

**What they've tried and why it failed:** Custom transformer model hit ~20% false positive rate. SpaCy NER hit the same. Azure AI model improved to 17% but still far too high. Rule-based models failed due to spelling variations (Fab11, F11, fab-11). Over 1000 hours of manual labeling was started and then paused due to cost.

**Colin's assessment:** The prior approaches were fundamentally misguided. Customer names are a finite, known list, not an NER problem. This is better solved with fuzzy matching, normalization, and curated entity dictionaries than with ML classification. The real problem is that they treated a lookup and matching problem as a machine learning problem.

**Technical environment:** Azure stack (AI Foundry, Microsoft Sentinel). Extremely locked-down security posture with closed-loop machine ecosystem, dedicated routers, full encryption, and complete isolation.

**Status:** Discovery call completed 3/12. Follow-up meeting to include technical lead Daniel is the next step. BayOne needs to come back with a proposed approach.

**Colin's angle:** Deep prior experience building detection and redaction systems in a similar semiconductor environment (Coherent Corp, Aerospace and Defense with ITAR constraints). Caught an exfiltration attempt before it became a regulatory problem. Has a clear technical vision for how to solve this correctly.

**Potential friction note:** Amit and Pratik were on the original email thread from Brad Estes. Colin was not initially included and had to insert himself after recognizing the opportunity required AI expertise that others on the thread could not provide. Scheduling of the discovery call had coordination issues that were escalated to Surej.

---

## 2. Cisco — AI-Assisted Developer Tooling

**Client contacts:** Arun Arunkumar (VP, DC Switching), Anand Singh (Director), Siva Kailas (Director), Srinivas Pitta (Engineering), Imran Pasha (Engineering), Divakar Rayapureddy (CI Pipeline Lead)

**BayOne contacts:** Neha, Zahra (both have strong relationships with Cisco leadership including direct line to Jimin, their CPO)

**Problem statement:** Cisco wants targeted AI expertise to enhance their existing developer tooling, not a new product stack. They have invested heavily in modernizing their CI/CD environment over the past 12-18 months (VS Code at 80-90% adoption, merged toolchains across ACI/CME and NX-OS/Switching teams).

**Three focus areas from Anand:**

1. AI-based code review to improve effectiveness, quality, and speed
2. Agentic RCA workflow with multi-input reasoning across logs, topology, and tests for higher accuracy root cause detection
3. Test automation for network-level topologies, generating test code from test steps

**Additional thread from Surej (Transcript 2):** Cisco announced aggressive AI targets at Cisco Live, including Cloud Control for 2026 and AI Defense now GA. Internally, they are aiming for 70% AI-generated code but Colin assessed this as likely underperforming because they are probably just using GitHub Copilot without a structured approach. Colin's read is that public announcements will create internal crunch time and delivery pressure that benefits BayOne's positioning.

**AI adoption and upskilling angle:** Surej discussed positioning BayOne to help Cisco drive broader AI adoption within their engineering organization. Cisco's CPO has been asking about increasing AI-generated code percentages. Colin and Neha are aligned on using this as both a services opportunity and a credential for the broader upskilling initiative.

**Status:** Active engagement with existing BayOne contractors embedded at Cisco. MCP server cataloging work (Saurabh's project under Srini's team) was due in January but is still far from complete as of early February, confirming Colin's thesis about delivery pressure building.

**Partner dynamic note:** Sarang Dharmapurikar (CEO of DagKnows) is an external partner on this engagement. His platform addresses production SRE rather than the developer tooling Cisco is asking for, creating some misalignment between his product goals and the client's actual needs. Colin has flagged accountability concerns and established engagement model boundaries with BayOne leadership.

---

## 3. Sephora — Multiple AI Threads

### 3a. EDW Modernization with AI Acceleration

**Client contacts:** Mani Soundararajan (VP, Marketing Tech/Personalization/Data-AI/Enterprise Reporting/Analytics), Andrew Ho (Sr. Director, Enterprise Reporting), Gariashi Chakraborty (Director, Enterprise Reporting), Rizwan Khan (Sr. Manager, Data Warehouse)

**BayOne contacts:** Zahra (sales), Neha

**Problem statement:** Sephora is migrating thousands of Cognos and SQL Server reports to Databricks with Tableau and ThoughtSpot. Timeline extends through 2028. Mani wants to know how AI can accelerate this, specifically for grouping similar reports, analyzing complex SQL inside Cognos, identifying patterns and redundancies, and reducing manual review.

**Colin's assessment:** AI accelerates the analysis and triage phase significantly and assists with translation and documentation, but the rebuild still requires skilled humans. The honest pitch is compressing a 2028 timeline, not eliminating the work. First step should be report rationalization before migration. Mani explicitly wants a structured POV, not a blank-slate discovery call.

**Engagement model question still open:** Whether Sephora wants BayOne as an AI enablement partner for their internal teams, as an outcome-based delivery partner owning a portion of the migration, or a hybrid.

**Status:** Discovery brief created for Zahra to gather additional information before scheduling a meeting between Colin and Mani.

### 3b. Agentic QE Offering

**Origin:** Surej (Transcript 2) proposed an agentic AI-enabled quality engineering offering for Sephora, combining Priya's QE expertise with Colin's AI capabilities.

**Value proposition as described by Surej:** Discovery of what Sephora's ~200 test engineers are doing, followed by a to-be state using a combination of people and agents to deliver the same or higher quality QE at 40-50% cost reduction with higher speed.

**Colin's approach:** Transfer learning model where agents mimic existing human workflows, with staggered insertion of agents and gradual dial-down of human involvement as agents learn. Human-in-the-loop and human control aspects remain central throughout.

**Status:** Surej is working to schedule an initial listening session with Sephora's QE team. No pitch on the first call, just understanding what they're doing so BayOne can ask the right questions and come back with a proposal in one to two weeks. Surej indicated high confidence in landing this deal.

### 3c. Contractor Upskilling (Part of Broader Initiative)

**Context:** Sephora's leadership (specifically through Ravi Pandey) has asked about building a pipeline of engineers proficient in AI tools. Separately, the broader AI upskilling initiative that Colin and Surej discussed encompasses Sephora contractors as one of several populations to train.

**Colin's note:** This needs to be separated from the Ravi Pandey request for Claude Code-proficient engineers, which is a narrower skills pipeline ask versus a general AI upskilling initiative. These are different in scope and delivery.

**Status:** Neha is point of contact at Sephora and has provided a resource list. Open questions remain about access restrictions, Sephora-provided AI tools, and corporate policy on AI tool usage. Colin has proposed that this be folded into the unified upskilling initiative rather than treated as a standalone effort.

---

## 4. SiTime — Salesforce CRM Query Layer

**Client contacts:** Jyothi Gorti (EVP and Chief Digital Officer), Piyush Sevalia (EVP Marketing, introducer), Judy Ash (VP Digital CX Marketing)

**BayOne contacts:** Sangeeta (sales), Amit (on thread)

**Problem statement:** SiTime makes precision timing semiconductors with an extremely parametric product catalog. Their CDO wants an AI layer over Salesforce CRM that lets sales reps ask plain-language questions about product specs instead of navigating complex parametric tables manually. They already have an external-facing AI tool for semiconductor product queries on their website, so the concept is proven internally and Jyothi understands what this looks like.

**Colin's assessment:** The Salesforce CRM query layer is the only legitimate AI engagement thread from the SiTime meeting. Technically feasible via RAG over product data, Salesforce-native Einstein AI integration, or external LLM with API access to Salesforce product objects. Viability depends heavily on what data actually lives in their Salesforce and how it's structured. Requires a no-strings-attached technical discovery before any scoping or proposal.

**Other items from the meeting (not AI):** Renesas acquisition integration work (M&A, not AI, and BayOne has no semiconductor integration track record to Colin's knowledge), SharePoint intranet buildout (basic IT/staffing work), and Judy Ash's website vendor selection (99% done, not an opportunity).

**Status:** Colin sent a calibrated response establishing that he will engage on the Salesforce use case once there is a concrete discovery conversation, and flagged that his time should not be committed without prior coordination. Needs to connect with Surej on bandwidth and priority.

---

## 5. Taylor Brand — AI Adoption in Engineering and Platform Migration

**Client contacts:** Shiva (engineering leader), Kalyan (new Director of AI at Taylor Brand)

**BayOne contacts:** Yogesh (met with Shiva socially), Surej

**Problem statement (two threads from Surej Transcript 1):**

1. AI adoption in engineering: Taylor Brand wants help driving AI adoption within their engineering department. This includes structured training, best practices sharing, and hands-on enablement showing teams the right way to use AI tools in their actual workflows. Colin's interest is that inserting himself into their engineering organization with the intent to drive AI adoption will surface additional opportunities over time.

2. Platform migration with AI-enabled development: Taylor Brand has a legacy platform integrated into their enterprise with multiple API integration points, data connections, and wrappers. They need to replace the old platform with a new one while maintaining all integration touchpoints. They have hundreds of wrappers to replace. Colin assessed this as a strong fit for an agentic approach using autonomous discovery, purpose-built agents for specific integration types, rule-based architecture for reliability, and automated validation agents.

**Colin's assets for this:** Already has the agentic migration approach documented from the Sephora code modernization work (monolithic thick client to microservices plus API endpoints). Same architecture applies. Also building a demo using the Sephora use case that will serve as a reusable showcase for exactly this type of engagement.

**Kalyan angle:** Surej noted that Kalyan, as the new Director of AI at Taylor Brand, has a lot to prove. Helping him pick a couple of smaller wins to build credibility is a low-risk, high-reward way to create a long-term partner.

**Status:** Yogesh met with Shiva socially. Next step is for Yogesh to raise the AI adoption and migration capabilities in conversation with Shiva to gauge interest and get a starting point. Colin is preparing the demo and documentation that would support a follow-up conversation.

---

## 6. AI Upskilling Initiative — Cross-Client and Internal

**Sponsor:** Surej (CEO)

**Ownership proposed:** Colin (technical lead), Neha (business owner)

**Scope as discussed with Surej:** A unified, reusable AI training capability for BayOne that applies across clients (Sephora, Cisco, Taylor Brand) and internally for both existing employees and new hires. Uses early client engagements as proof points and credentials. Builds reusable training assets, frameworks, and potentially credentialing. Not a one-off pilot at a single client.

**Connected threads:**

- Sephora contractor training (Ravi Pandey request plus general upskilling)
- Cisco AI adoption in engineering (70% AI-generated code target, CPO-level ask)
- Taylor Brand AI adoption in engineering
- Internal BayOne employee development

**Neha's qualifications:** Already POC at both Sephora and Cisco. Leads Make Tech Purple (workforce development and women's empowerment program). Has direct relationships with client leadership. Already in tight coordination with Colin on active deliverables. High-output producer who can own business and delivery components independently.

**Status:** Colin has messaged Surej to align on ownership structure. Surej confirmed alignment and agreed to manage expectations with others who had been involved. Discussion forthcoming to formalize the initiative.

---

## 7. Reusable Demo — Agentic Code Modernization

**Not a client opportunity but a strategic asset under development.**

Colin's team is building a demo using the Sephora use case (monolithic thick client migration to microservices plus API endpoints) that will serve as a reusable, non-client-specific showcase. This demo will be the first tangible thing BayOne can show when someone asks to see AI capabilities in action.

**Applies to:** Taylor Brand (platform migration), Cisco (developer tooling and code modernization), future client conversations requiring proof of capability.

**Timeline:** Team expected to have demo ready within two weeks (as of Transcript 2 conversation with Surej).

**Status:** Team has started work. Colin also plans to provide a written summary of the approach as a faster deliverable while the demo is being built.
