# BayOne AI Opportunities Catalog

*Last updated: March 17, 2026*

---

## 1. Cisco — AI-Assisted Developer Tooling

**Status:** Active engagement, in-person meetings completed

**Contacts:**
- Arun Arunkumar (VP, DC Switching)
- Anand Singh (Director)
- Siva Kailas (Director)
- Srinivas Pitta / Srini (Engineering)
- Imran Pasha (Engineering)
- Divakar Rayapureddy (CI Pipeline Lead)

**BayOne Team:** Colin Moore, Zahra Syed, Rahul Sharma
**External Partner:** Sarang Dharmapurikar (DagKnows)

**Problem Statement:**
Cisco's DC Switching org has modernized their development environment (VS Code at 80-90%, unified ACI/NX-OS toolchain, established CI/CD with Bazel and Jenkins). They are not looking to replace anything. They want targeted AI expertise to enhance what they already built.

**Three Focus Areas (from Anand Singh):**
1. AI-based code review to improve effectiveness, quality, and speed
2. Agentic RCA workflow with multi-input reasoning across logs, topology, and test results for higher accuracy root cause detection
3. Test automation for complex network topologies, converting test steps into executable test code

**Key Context:**
- Cisco announced major AI initiatives at Cisco Live (Feb 2026) including AI Defense (now GA), Cloud Control (later 2026), and agentic network management tools
- Public announcements create delivery pressure on internal teams
- Srini's team was set to deliver MCP server cataloging work before Q1 and is still well behind schedule
- The gap between executive ambition and engineering reality is the ongoing opportunity for BayOne
- Must work at scale for 500+ engineers, not just POC for 10
- Colin has direct engagement history with the technical teams

**Engagement Model:** BayOne provides AI expertise and augmentation. DagKnows (Sarang) involvement has required careful boundary-setting around accountability and ownership. Clear engagement model established with BayOne president Rahul.

**Opportunity Size:** Substantial. Ongoing augmentation and potential multi-workstream engagement across all three focus areas.

---

## 2. Lam Research — Custom NER/Redaction for IP Protection

**Status:** Discovery call completed 3/12/2026. Follow-up with technical lead Daniel expected.

**Contacts:**
- Bradley Estes (Managing Director, Knowledge & Advanced Services)
- Mikhail Krivenko (Head of Product)
- Daniel (Technical Lead, expected on follow-up)

**BayOne Team:** Colin Moore, Pratik Sharda, Surej KP, Amit Grover

**Problem Statement:**
Lam pulled back all AI/GenAI usage organization-wide due to IP concerns. They need a custom detection and redaction layer to protect sensitive information before it can safely re-enable AI tools for their workforce.

**The actual problem (clarified on 3/12 discovery call) differs from the initial framing.** This is not about Azure guardrails failing. It is a custom NER problem with two distinct use cases:

**Use Case 1 — Self-Help Search:**
Users search knowledge bases for troubleshooting. Over-restriction blocks useful cross-customer solutions. A Samsung solution exists but an Intel user can't see it because it's restricted. Goal is to surface solutions without leaking customer-specific IP.

**Use Case 2 — Escalation / Ask for Help:**
Users open tickets, describe problems, and attach transcripts. They inadvertently include customer names, fab numbers, and sensitive details in unstructured text. This breaks into two sub-problems:
- Real-time detection at input (must be fast, 2-5 seconds, under 1% false positive rate)
- Batch redaction before data enters the general knowledge pool (accuracy matters more than speed)

**What They've Tried:**
- Transformer models, SpaCy, Azure AI models, rule-based models
- Best result was 17% false positive rate (Azure AI model), far from the under 1% target
- 1000+ hours of labeling paused due to cost and maintenance burden
- Core difficulty is spelling variations and Lam-specific patterns (Fab11, F11, fab-11, FAP space 11, etc.)

**Why This Is Hard:**
Lam's IP environment is extremely locked down. Dedicated routers per machine globally, everything through VPN, machines fully encrypted and isolated. Their customers (TSMC, Samsung, Intel, Micron, SK Hynix) are competitors with each other, and Lam sees production data from all of them. A leak between customers would be catastrophic.

**Colin's Assessment:**
Lam's prior attempts were fundamentally misapproached. This is a solvable NER/classification problem that requires Lam-specific entity training, not generic off-the-shelf models. The real-time detection requirement at under 1% false positive is the hard constraint. Colin has direct relevant experience from Coherent Corp in the same industry.

**Opportunity Size:** Potentially significant. Real technical problem with a well-defined success metric. Client is sophisticated and driving the engagement structure properly.

**Process Note:** Communication and scheduling around this opportunity have had friction. The discovery call and follow-up meetings have not been well-coordinated internally, which Colin has raised with leadership.

---

## 3. Sephora — EDW Modernization with AI Acceleration

**Status:** Pre-engagement. Zahra (sales) gathering information for Colin to build a POV before meeting with Mani.

**Contacts:**
- Mani Soundararajan (VP, Marketing Tech / Personalization / Data-AI / Enterprise Reporting / Analytics)
- Andrew Ho (Sr. Director, Enterprise Reporting)
- Gariashi Chakraborty (Director, Enterprise Reporting)
- Rizwan Khan (Sr. Manager, Data Warehouse)

**BayOne Team:** Colin Moore, Zahra Syed, Neha

**Problem Statement:**
Sephora is kicking off a large EDW modernization program. Thousands of Cognos/SQL Server reports need to be re-engineered and migrated to Databricks with Tableau/ThoughtSpot as the front end. Timeline extends through 2028, but Mani wants AI to accelerate it.

**AI Acceleration Angles:**
- Grouping similar reports to identify consolidation targets
- Analyzing complex SQL inside Cognos for migration planning
- Identifying patterns, redundancies, and dead reports
- Reducing manual review burden across the catalog

**Key Context:**
- Mani explicitly said he does not want a blank-slate discovery call. He wants Colin to come in with a structured POV or one-pager anchored in what his teams are actually experiencing.
- BayOne already has consultants embedded under Andrew, Ram, and Gariashi, which provides an existing intelligence channel
- Zahra's approach to this opportunity (gathering info proactively, asking Colin what he needs, proposing a prep sync) has been a model for how the sales-to-AI handoff should work

**Opportunity Size:** Large. Multi-year migration program with clear AI use cases. Existing BayOne presence at the account.

---

## 4. SiTime — Salesforce CRM Query Layer

**Status:** Early. Meeting held 3/12/2026 by sales team. Colin evaluating whether there is a real AI engagement thread.

**Contacts:**
- Jyothi Gorti (EVP & Chief Digital Officer)
- Judy Ash (VP, Digital CX Marketing)
- Piyush Sevalia (EVP Marketing, introducer)

**BayOne Team:** Colin Moore, Sangeeta (sales), Anuj (VP Sales), Amit (VP Delivery)

**Problem Statement:**
SiTime is scaling to $1B revenue and integrating the timing division acquired from Renesas. Jyothi is interested in AI but strictly use-case driven. Multiple items surfaced in the initial meeting, but only one has a clear AI thread.

**The One Real AI Use Case — Salesforce CRM Query Layer:**
SiTime's product catalog is extremely parametric (frequency, jitter, phase noise, voltage, package, temp range, etc.). Sales reps currently have to navigate complex product tables or ask applications engineers for help matching customer specs to SKUs. Jyothi wants an AI layer on top of Salesforce CRM that lets reps ask natural language questions and get matching products back. They already have a version of this working on their external website for customer-facing product queries, so the concept is proven internally.

**Viability depends on:** What data actually lives in their Salesforce and how it's structured. Requires a technical discovery conversation before any scoping.

**Other Items Discussed (not AI, not Colin's scope):**
- Renesas acquisition integration (M&A platform migration, not AI)
- SharePoint intranet / "Dashboarding" (basic IT/staffing work)
- Judy Ash's website vendor selection and PIM question (99% done, no engagement there)

**Colin's Assessment:**
The Salesforce query layer is the only legitimate AI engagement thread. Everything else is either not AI work or already decided. Colin flagged this clearly to the group and requested a no-strings-attached discovery before any commitments. Bandwidth and priority need to be confirmed with Surej first.

**Opportunity Size:** Moderate if the Salesforce data is in good shape. Single focused use case with a clear business driver.

---

## 5. Salesforce (Kevin Bennett) — Relationship Building / Monitoring

**Status:** Introductory call completed. No concrete AI opportunity identified yet.

**Contact:**
- Kevin Bennett (VP, Marketing Operations & Analytics, Salesforce via Informatica acquisition Nov 2025)

**BayOne Team:** Colin Moore, Han (sales)

**Problem Statement:**
Kevin is navigating the post-acquisition integration of Informatica into Salesforce. He has several pain points including IT engineering support disappearing as resources get pulled into integration work, a massive Marketo migration on the horizon, and an executive mandate to demonstrate Agentforce use cases.

**Potential AI Thread:**
Kevin needs to show Agentforce adoption to Salesforce leadership. He is realistic about what that requires (data readiness, context engines, guardrails) versus the hand-waving at the executive level. A targeted POC helping him stand out in the new org could be a way in.

**Key Constraints:**
- No operational budget currently allocated for new initiatives
- Kevin's authority at Salesforce is still being defined post-acquisition
- Timeline for everything is uncertain pending M&A decisions
- IT engineering gap hits in 6-8 weeks but that's augmentation work, not AI-specific

**Colin's Assessment:**
Strong relationship signal from Kevin (stayed past time, proactively offered to protect vendor status), but no concrete AI opportunity to pursue right now. Agreed to share the Sephora use case as reference material. Worth monitoring but not worth investing significant time until something specific surfaces.

**Opportunity Size:** TBD. Watching brief for now.
