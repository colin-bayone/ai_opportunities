# BayOne AI Opportunities Catalog

**Maintained by:** Colin Moore, Director of AI
**Last Updated:** March 17, 2026

---

## Lam Research

**Opportunity:** Custom NER and Redaction System for AI IP Protection

**Contacts:**
- Bradley Estes, Managing Director, Knowledge & Advanced Services
- Mikhail Krivenko, Head of Product
- Daniel (technical lead, not yet met)

**Problem Statement:**
Lam has pulled back all AI and GenAI usage across the organization due to IP leakage concerns. Their customers (TSMC, Samsung, Intel, Micron) are direct competitors with each other, and Lam sees production data from all of them. Leaking one customer's data to another would be catastrophic.

They need two capabilities. The first is real-time detection at entry points when users type problem statements, ticket descriptions, or search queries containing customer-confidential information such as customer names, fab identifiers, and production details. This needs to run in 2-5 seconds with under 1% false positives. The second is batch redaction of stored documents and tickets so they can be fed into general knowledge bases without exposing sensitive data.

**What They've Tried:**
Custom Transformers model (20% false positive rate), SpaCy NER (20% false positive rate), Azure AI model (improved to 17%), rule-based matching (low accuracy due to spelling variations), and 1000+ hours of manual labeling (paused due to cost). All approaches fundamentally misapproached the problem. This is not a machine learning classification problem. It is a domain-specific entity recognition problem solvable through curated dictionaries, fuzzy matching, and normalization layers.

**Colin's Assessment:**
The prior approaches were junior-level. Customer names are a finite, known list. Fab identifiers follow predictable patterns. The right approach is a layered system combining curated entity dictionaries with fuzzy matching and normalization, not training general-purpose models on global data and hoping they learn Lam-specific patterns. Real-time detection at the entry point is the highest-value target because if that works well, the need for heavy batch redaction drops significantly.

**Status:** Discovery call completed March 12, 2026. Follow-up meeting being scheduled to include Daniel (technical lead). BayOne to come back with an approach and proposal.

**Tech Stack at Lam:** Azure (AI Foundry, Microsoft Sentinel). Extremely locked-down security environment with closed-loop machine ecosystems, dedicated routers, full encryption, and VPN-only access.

**Qualification:**
- Decision maker with authority: Yes (Brad owns the full lifecycle from business case to execution)
- Confirmed problem statement: Yes (specific, articulated, with measurable failure criteria)
- Budget: Not yet confirmed, but Brad indicated he has latitude
- Revenue potential: Medium to large depending on scope
- Colin's domain fit: Strong. Direct experience building similar systems at Coherent in the same industry

---

## Cisco

**Opportunity:** AI-Assisted Developer Tooling (Code Review, Agentic RCA, Test Automation)

**Contacts:**
- Arun Arunkumar, VP, DC Switching
- Anand Singh, Director
- Siva Kailas, Director
- Srinivas Pitta (Srini), Engineering
- Imran Pasha, Engineering
- Divakar Rayapureddy, CI Pipeline Lead

**Problem Statement:**
Cisco's DC Switching group (NX-OS) wants targeted AI expertise to enhance their existing CI/CD infrastructure. They are not looking for a new toolchain or product stack. They want to make their current systems more intelligent across three focus areas. First, AI-based code review to improve effectiveness, quality, and speed. Second, agentic RCA workflows for multi-input reasoning across logs, topology, and test results with higher accuracy root cause detection. Third, test automation generation from test steps for network topology validation.

**Colin's Assessment:**
Cisco's engineering teams are highly capable and already deep into AI/ML internally. They explicitly said "this team is expert, we can build it." What they need is augmentation with specialized AI expertise, not a team that comes in and starts from scratch. The engagement model is constrained (budget for roughly 1-5 contractors) and requires significant ongoing collaboration from Cisco engineers to transfer context.

**Complicating Factor:**
Sarang Dharmapurikar (CEO of DagKnows, BayOne partner) was brought in by Rahul (BayOne founder). Sarang's motivations center on positioning DagKnows for VC metrics, and his preferred engagement models place architecture control with DagKnows while BayOne assumes implementation and accountability risk. Colin established clear boundaries with Rahul: either DagKnows owns it end-to-end or BayOne owns it end-to-end. The middle ground where DagKnows designs and BayOne is accountable is not acceptable.

**Status:** Initial meetings completed in December 2025. Cisco publicly announced aggressive agentic AI goals at Cisco Live (February 2026), creating delivery pressure and urgency. Saurabh (BayOne contractor on Srini's team) reported in early February that the MCP server cataloging work originally due before Q1 is still far from ready. The public announcement timeline versus actual readiness gap represents an ongoing opportunity.

**Qualification:**
- Decision maker with authority: Yes (Arun, VP level)
- Confirmed problem statement: Yes (three specific focus areas articulated by Anand)
- Budget: Constrained (1-5 contractors)
- Revenue potential: Small to medium initially, with expansion potential as Cisco's delivery pressure increases
- Colin's domain fit: Strong on AI/ML architecture and agentic systems

---

## Sephora

**Opportunity:** AI-Accelerated EDW Modernization (Cognos to Databricks Migration)

**Contacts:**
- Mani Soundararajan, VP (Marketing Tech, Personalization, Data/AI, Enterprise Reporting, Analytics)
- Andrew Ho, Sr. Director, Enterprise Reporting
- Gariashi Chakraborty, Director, Enterprise Reporting
- Rizwan Khan, Sr. Manager, Data Warehouse

**BayOne Sales:** Zahra (salesperson), Neha

**Problem Statement:**
Sephora is migrating thousands of Cognos/SQL Server reports to Databricks with Tableau/ThoughtSpot as the visualization layer. Current timeline extends to 2028. Mani wants AI to accelerate the process across several areas: grouping similar reports, analyzing complex SQL inside Cognos, identifying patterns and redundancies, and reducing manual review. He explicitly requested that any meeting with Colin come with a structured POV, not a blank-slate discovery call.

**Colin's Assessment:**
This is a real opportunity with a well-qualified buyer. Mani has clear authority, a defined problem, and a timeline. The AI angle is genuine, as report rationalization, complexity scoring, and migration planning are all areas where AI adds measurable value. Key open questions include whether Sephora wants enablement (AI tools for their team), outcome-based delivery (BayOne owns migration of a report subset), or a hybrid model. Also unknown: the actual complexity distribution of those "thousands" of reports, whether rationalization has been done, and who currently owns the re-engineering work.

**Status:** Zahra gathered initial context from her meeting with Mani. Colin provided a detailed set of qualifying questions for Zahra to bring back before scheduling the direct meeting with Mani. A discovery brief and set of information-gathering questions were prepared. Waiting on Zahra to collect answers from the team before Colin's direct engagement.

**Qualification:**
- Decision maker with authority: Yes (Mani, VP level)
- Confirmed problem statement: Yes (specific, with named use cases for AI)
- Budget: Implied (large program with 2028 timeline suggests funded initiative)
- Revenue potential: Medium to large depending on engagement model
- Colin's domain fit: Strong on AI-accelerated data migration and report analysis

---

## SiTime

**Opportunity:** Salesforce CRM AI Query Layer for Sales Teams

**Contacts:**
- Jyothi Gorti, EVP & Chief Digital Officer
- Judy Ash, VP, Digital CX Marketing
- Piyush Sevalia, EVP Marketing (introducer)

**BayOne Sales:** Sangeeta, with Anuj (VP of Sales) and Amit (VP of Delivery) looped in

**Problem Statement:**
Jyothi wants an AI layer over Salesforce CRM that lets SiTime's sales team query complex semiconductor product specifications in natural language instead of navigating parametric tables manually. SiTime's product catalog is highly parametric (frequency range, jitter, phase noise, supply voltage, package size, operating temperature, etc.), and sales reps currently need deep product knowledge or applications engineer support to match customer requirements to the right SKU. They already have an AI-powered product query tool on their external website for customers, and this would be the internal-facing equivalent for sales teams.

**Colin's Assessment:**
The use case is legitimate and Jyothi is a use-case-driven buyer, which is the best kind. However, viability depends entirely on what product data actually lives in their Salesforce instance, how it's structured, and how clean it is. A discovery conversation with Jyothi's technical team is needed before anything can be scoped. Jyothi's team appears technical enough to walk through their data model.

The meeting also surfaced several non-AI threads (Renesas M&A integration, SharePoint intranet, website vendor selection) that are not in scope for Colin. The Renesas acquisition integration is a post-acquisition M&A systems integration involving data migration, platform consolidation, and personnel onboarding, and BayOne has not done that type of work. The SharePoint intranet is basic IT consulting. Judy Ash's website vendor is 99% selected.

**Process Friction:** Sangeeta told Jyothi she would bring "tech folks" to the next call without checking with Colin first. The scope also expanded in replies from "Salesforce use case" to "AI use cases broadly," which Colin pushed back on. Anuj responded to Colin's detailed qualification breakdown by saying "all of these look interesting, let's chase everything," bypassing the qualification Colin laid out.

**Status:** Initial meeting completed. Colin responded with qualification of each thread. Waiting on Sangeeta to collect specific problem statements from Jyothi before discovery. Colin connecting with Surej on bandwidth and priority.

**Qualification:**
- Decision maker with authority: Yes (Jyothi, CDO/EVP level)
- Confirmed problem statement: Directionally yes, but needs technical discovery to validate feasibility
- Budget: Unknown
- Revenue potential: Medium, depending on Salesforce data readiness
- Colin's domain fit: Strong on AI/NLP query interfaces and RAG systems

---

## Salesforce (Kevin Bennett / Informatica)

**Opportunity:** No active AI opportunity. Relationship building and monitoring.

**Contacts:**
- Kevin Bennett, VP, Marketing Operations and Analytics (formerly Informatica, now Salesforce post-acquisition)

**BayOne Sales:** Han

**Summary:**
Introductory discovery call where Kevin shared challenges from the Informatica-to-Salesforce acquisition. He was highly engaged and proactive about maintaining BayOne as a vendor through the Salesforce procurement transition. Pain points surfaced included IT engineering support disappearing in 6-8 weeks, a massive Marketo migration if leadership accelerates it, and an Agentforce mandate from Salesforce leadership.

However, none of the surfaced items are AI-specific. Salesforce has Agentforce as their own agentic AI platform, which requires internal employees to implement. The IT support gap and Marketo migration are staffing and platform work, not AI engagements.

**Status:** Colin recommended Han follow up with Kevin directly to get him talking about what he specifically wants to speed up internally. Colin's qualifying criteria (client interest, budget/authority, specific use case) currently show one of three met (interest). On hold for Colin's direct involvement until a concrete AI-relevant use case surfaces.

**Qualification:**
- Decision maker with authority: Partial (Kevin can write proposals, but post-M&A authority is unclear)
- Confirmed problem statement: Directional pain points, nothing concrete or AI-specific
- Budget: None currently; all operational budget allocated to campaign spend
- Revenue potential: Unknown, possibly small to medium if something surfaces
- Colin's domain fit: Low for current threads

---

*End of catalog. Opportunities listed in order of current qualification strength and AI relevance.*
