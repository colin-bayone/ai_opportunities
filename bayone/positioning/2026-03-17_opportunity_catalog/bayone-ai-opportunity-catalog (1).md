# BayOne AI Opportunity Catalog

**Prepared by:** Colin Moore, Director of AI
**Last Updated:** March 2026

---

## Active Engagements (Delivering)

### Cisco — CI/CD Log Triage & MDS Code Modernization

**Contact:** Gaurav (BayOne liaison), Cisco engineering team
**Status:** Active delivery, SAL approval cleared after prolonged procurement delay

Two distinct work streams under one client relationship. The first is CI/CD pipeline log triage, focused on automating the analysis and classification of build/deployment logs across Cisco's internal DevOps platforms. The second is a full code modernization of the MDS Element Manager (device management tool for SAN/Fibre Channel switches), migrating from a legacy Java Swing thick client (~1,432 Java files, ~242K lines of code, stuck on Java 1.8) to a React frontend with a Go backend.

Onboarding items including GitHub Enterprise training, VPN access, and DeepSight platform onboarding are in motion. Colin has Bay Area availability the week of 3/23 for in-person sessions. A detailed understanding-of-current-state document and approach proposal have been delivered. Timeline is approximately 2-3 quarters for the modernization, with Q3 as buffer. This engagement is the strongest current proof point for BayOne's AI and engineering capabilities.

**Capability areas:** Developer productivity, CI/CD automation, code modernization, agentic tooling

---

### Sephora — Data Warehouse Modernization

**Contact:** Neha (BayOne), Mani (VP, Sephora), Gariashi (Director of Report Engineering, Sephora)
**Status:** Active engagement, internal alignment in progress

Sephora is migrating a 20-year-old legacy enterprise data warehouse from SQL Server/Cognos to Databricks. The scope is massive: 6,000 reports, 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20+ source systems. Their 3-year timeline is ambitious, and there are open architectural questions around whether to preserve legacy SSAS cube connectivity (a change management problem, not a technical one) or fully modernize the semantic layer.

The engagement blends staffing (they want a senior embedded resource) and solutions (AI-assisted tooling for SQL extraction, lineage discovery, mapping automation). Colin has flagged internally that these need to be scoped as separate tracks with different accountability models. A Cognos MCP demo is in scope as a potential differentiator. Key risk: organizational politics at Sephora around who has authority to enforce architectural decisions.

**Capability areas:** Data/analytics modernization, AI-assisted migration tooling, enterprise data platforms

---

## Active Opportunities (Qualified, In Progress)

### LAM Research — AI Governance & Guardrails

**Contact:** Brad Estes (Managing Director, LAM), Mikhail Krivenko (LAM), Pratik (BayOne sales)
**Status:** Discovery call being scheduled by LAM. Client-driven structure.

LAM Research has pulled back usage of all AI and GenAI tools internally due to concerns about sensitive information leaking into these tools. They want a solution to flag inputs being fed into AI tools for proprietary content (client names, IP, production data, etc.). Brad explicitly laid out the engagement model: LAM presents problem statement, Q&A session, BayOne comes back with an approach. This is exactly the client-led discovery model that works best.

Colin's initial technical assessment: much of what LAM describes is typically addressed by enterprise-tier tools (Azure AI Foundry, Microsoft Sentinel) which already have built-in guardrails. LAM is using both Azure and AWS stacks and already has some guardrails deployed, but they're failing to meet LAM's more customized requirements around IP scrubbing and user prompting. The opportunity could range from a governance consulting engagement (helping them properly configure what they already have) to building a custom wrapper layer for more advanced data control needs.

LAM is an extremely IP-sensitive environment with dedicated routers, encrypted machines, and closed-loop ecosystems. Colin has prior experience in a very similar environment at Coherent (same industry, ITAR-grade protections). Strong natural fit.

**Capability areas:** AI governance, guardrails and compliance, enterprise security, consulting

---

### Salesforce / Kevin Bennett — Marketing Operations & Analytics

**Contact:** Kevin Bennett (VP Marketing Ops & Analytics, Salesforce), Han (BayOne sales)
**Status:** Exploratory conversation completed

Kevin is a 25-year marketing operations veteran who built Informatica's entire GTM analytics stack, including proprietary predictive models and multi-touch attribution. Following Salesforce's $8B acquisition of Informatica (closed November 2025), he is navigating platform integration, Agentforce rollout, and the tension between his custom-built tools and Salesforce's native ecosystem.

Detailed meeting prep was completed including Kevin's background, career trajectory, Salesforce/Informatica acquisition context, industry talking points on Agentforce and marketing AI in 2026, and signal mapping for potential opportunity areas. The approach was purely discovery-oriented: get Kevin talking, show expertise through conversation, follow up with something tailored.

**Capability areas:** Marketing analytics, AI/ML operations, data infrastructure, platform integration

---

### Ariat — GCC AI Capabilities & Offshoring Support

**Contact:** Ariat leadership (CEO attended initial meetings)
**Status:** Presentation delivered, relationship building

Ariat is offshoring internal functions for the first time and establishing a Global Capability Center (GCC) in India. They are concerned about maintaining company culture and standards across geographies, and interested in how AI can facilitate this transition. A capabilities presentation was delivered covering four areas: AI strategy and innovation, enterprise AI solutions, next-generation quality engineering, and bridging culture across geographies through AI.

Their CEO specifically asked about growing skills and building AI-ready culture during GCC scaling. Potential opportunity areas include AI for software development acceleration, AI-driven quality engineering (addressing their interest in QA testing), analytics and insights, and using AI as a driver to bring distributed teams together.

**Capability areas:** Enterprise AI solutions, quality engineering, developer productivity, organizational AI enablement

---

### JPMC — Direct Vendor Onboarding

**Contact:** Lasandra James (Executive Director, Commercial Banking, JPMC), BayOne sales team
**Status:** Building capabilities deck for procurement meeting

JPMC engagement centers on getting BayOne onboarded as a direct vendor (previously supported through a preferred vendor). BayOne has strong internal relationships and history filling roles in cloud engineering, SRE, Java backend, and database engineering supporting projects in Observability, OpenTelemetry, and database infrastructure.

The meeting with Lasandra's boss required a capabilities deck incorporating AI-driven solutions. Colin was asked to contribute AI positioning aligned with JPMC's strategic priorities (informed by 10-K and 5-K filings). Primarily a staffing relationship with potential to expand into solutions.

**Capability areas:** Cloud infrastructure, DevOps, AI-enhanced development, enterprise platforms

---

## Early-Stage Opportunities (Needs Further Qualification)

### Tailored Brands — Internal AI Initiatives

**Contact:** Kalyan (Director of AI, Tailored Brands), Kishore (UI/UX lead), Kiran (Senior Director), Rima (BayOne sales), Anuj (BayOne VP Sales)
**Status:** Very early. No concrete problem statement from client.

Tailored Brands has a new Director of AI (Kalyan) who is non-technical but a strong domain SME. He is still figuring out the roadmap. When discussed with Surej, the agreed angle was around known internal initiatives: code modernization, QA testing, analytics/dashboards, customer intelligence, DevOps/cloud native, and enterprise platforms.

The initial client meeting did not produce any concrete problem statements or initiatives. The client's Director of AI explicitly stated he was not ready to discuss AI topics yet. There has been recurring misalignment between what the sales team positioned and what the client was actually ready for. Colin has stepped back until there are concrete discussion topics on the client's side.

Potential areas of interest (once ready): code modernization, AI-assisted QA testing, analytics and dashboards, customer segmentation and intelligence, DevOps and cloud native platforms.

**Capability areas:** TBD pending client readiness

---

### Walmart — AI Capabilities Interest (via Kanchan)

**Contact:** Kanchan (BayOne sales), Amit (BayOne VP Delivery)
**Status:** Needs reset. Misaligned expectations.

A lead at Walmart expressed interest in BayOne's AI capabilities after receiving a deck (which Colin did not see or approve). The client asked about AI accelerators, chatbot and agent-based solutions, standalone product positioning, and a feature/functionality list. None of these things exist at BayOne.

Colin has communicated that BayOne does not have pre-built AI accelerators, demos, or standalone products, and that any deck sent without his involvement would need to be walked back by whoever sent it. He offered to walk Kanchan through what BayOne actually offers so she can have a grounded conversation with her Walmart contact. Requires re-engagement on realistic terms once expectations are reset.

**Capability areas:** TBD pending honest realignment

---

### HPE — Prasanjit Shome / AI-SRE

**Contact:** Prasanjit Shome (Sr. Engineering Manager, HPE)
**Status:** Not a qualified opportunity. Requires outreach and qualification.

Identified via a LinkedIn post where Prasanjit shared completion of a GenAI mastermind program and expressed interest in experimenting with AI for incident reviews, documentation, and developer workflows. No conversation has occurred with the prospect. No confirmed interest, problem statement, budget, or decision-making authority established.

Pratik (BayOne sales) has been directed to reach out, have a real conversation, and determine if there's an actual need before escalating. If something concrete surfaces, Colin will engage.

**Capability areas:** Potentially SRE automation, incident review, developer workflows (unconfirmed)

---

## Partnership Opportunities

### Zeblok Computational — Air-Gapped AI Platform Partnership

**Contact:** Mouli Narayanan (CEO, Zeblok)
**Status:** Discovery call completed

Zeblok offers the Ai-MicroCloud platform, an on-prem AI/ML lifecycle management platform targeting organizations that cannot use cloud services due to sensitivity requirements. Primary target market is U.S. defense and A&D. They need a partner who can bring AI talent, enterprise delivery capability, and experience navigating ITAR/FedRAMP compliance requirements.

Colin brings direct experience from Coherent working in ITAR-regulated and FedRAMP-authorized environments. BayOne's Azure expertise could bridge both worlds if customers want Ai-MicroCloud running on Azure Local infrastructure. Key questions around Zeblok's CMMC 2.0 readiness and NIST 800-171 compliance posture were identified for further discussion.

**Capability areas:** On-prem AI deployment, ITAR/FedRAMP compliance, defense sector AI, governance

---

### Workday / Adam Godson — Recruiting AI Partnership

**Contact:** Adam Godson (VP Talent Acquisition, Workday, former CEO of Paradox)
**Status:** Outreach in preparation via Sangeeta (BayOne)

Adam Godson is the former CEO of Paradox (conversational AI recruiting platform, acquired by Workday for ~$1B, closed October 2025). He is now integrating Paradox into Workday's core platform alongside HiredScore (AI talent matching). Workday is actively shifting engineering capacity offshore to India and has been through two rounds of layoffs.

The outreach angle is as a partner who can provide engineering teams in India with recruiting AI domain familiarity, given BayOne's own internal experience building TalentAI. This is not a "help you build something" pitch but a "we have teams who can be productive in this space without a long ramp-up" conversation. Adam is deeply technical and allergic to generic vendor pitches. Approach must be respectful of his expertise.

**Capability areas:** Recruiting AI, conversational AI, offshore engineering capacity, platform integration

---

## Internal Products

### TalentAI

**Status:** Active, ongoing development and support

BayOne's internal Django-based recruiting platform, evolved from a project called Recruitment 2.0. Scaled from roughly 8 to 45 applications, transitioned from React/Node.js/MongoDB to Django. Ownership and long-term support model is currently under discussion with leadership. Significant portion of Colin's team's weekly capacity is consumed by TalentAI work, which competes with client-facing delivery and sales enablement efforts.

### TechScore

**Status:** Active internal tool

Internal scoring and assessment platform. Part of BayOne's AI product portfolio.

---

## Capability Areas Summary

Based on active work and qualified opportunities, BayOne's demonstrable AI capability areas are:

**Currently delivering and defensible:** CI/CD automation and log triage, code modernization (Java to modern stacks), agentic AI development, data/analytics modernization, AI-assisted migration tooling, enterprise DevOps platforms, recruiting AI (internal)

**Strong positioning based on Colin's background:** AI governance and compliance, ITAR/FedRAMP environments, enterprise security and guardrails, on-prem and air-gapped AI deployment

**Emerging based on active opportunities:** AI-driven quality engineering, marketing operations and analytics AI, customer intelligence and segmentation
