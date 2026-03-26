# BayOne Active Work Streams - Executive Summary

**Date:** March 17, 2026
**Prepared for:** CEO
**Purpose:** High-level overview of active client engagements and project status

---

## CISCO

### NX-OS CI/CD Pipeline Improvement

**Type:** Software Development / AI Integration
**Budget:** $100K/quarter
**SOW Status:** Signed, renewal date end of April 2026

**Overview:**
Multi-phase engagement to improve Cisco's NX-OS CI/CD pipeline with AI-driven tooling.

**Phases:**
- **Current:** Discovery + Phase 1 - Developer Box instrumentation (local testing visibility) and Branch Health dashboards (failure trends and attribution)
- **Phase 2:** Unified Interface - Consolidate data from multiple tools into single chat-based interface
- **Phase 3:** AI-Driven Failure Diagnosis - Automate root cause analysis and suggest fixes for pipeline failures
- **Phase 4:** Coverage Tracking - Confirm code changes are tested at the condition level before merge
- **Phase 5:** Self-Healing - Automated retry and correction for transient failures with governance framework

**Client Stakeholders:**
- Arun Kumar (VP, Sponsor)
- Venkat Krishnamurthy (VP)
- Anand Singh (Director)
- Srinivas Pitta (Sr. Engineering Manager, Internal AI Lead)
- Divakar Rayapureddy (Engineering Manager)

**Team:**
- **BayOne Lead:** Colin Moore (Director of AI)
- **Onshore:** Namita Mane (H1 pending, temporary backfill identified), Srikar Madarapu (starts next week)
- **Offshore:** Saurav Mishra (onboarded), Askari Sayed (onboarded)

**Effort:** High but distributed among the team

**Project Status:** On track

**Current Status:**
Team onboarding in progress. Askari and Saurav have completed onboarding and received Cisco hardware. Srikar starts next week. Namita's H1 status has been challenging for over a month; temporary backfill recommended. Communication with Anand and Srinivas is strong. Most onboarding steps complete on BayOne's side; remaining items pending on Cisco's side with Anand Singh assisting. Discovery phase to begin soon pending final Cisco onboarding activities.

---

---

### UI Conversion (EPNM to EMS)

**Type:** Software Modernization / AI-Accelerated Code Conversion
**Budget:** POC (free), paid engagement TBD based on success
**SOW Status:** POC stage

**Overview:**
Converting 250+ legacy EPNM (Evolved Programmable Network Manager) UI screens to modern EMS (Element Management System) microservices architecture. Cisco's key customers demand the familiar EPNM UI be retained because network operators have been trained on it for 15+ years and resist retraining. This requires extracting tightly-coupled functionality from a monolithic system and re-implementing it in a modern microservices architecture. Highly reusable project with significant scope and strong interest from multiple parties. Team is very enthusiastic about this opportunity.

**Client Stakeholders:**
- Guhan Raman (Director)
- Selva Subramanian (Engineering Manager and Lead)

**Technical Approach:**
AI-accelerated code conversion using Claude Code and LangGraph agent swarm. Build knowledge graph of codebase, pattern identification and conversion library (reusable across screens), custom agent development for parsing/converting, Playwright for automated testing. "Flywheel effect" - initial investment in infrastructure (POC: 2-3 screens in 4 weeks), then multiplicative speedup for remaining 250+ screens using established patterns.

**Effort:** Medium-low

**Current Status:** Firm opportunity, POC in progress. Waiting on Cisco hardware and code access. NDA signed.

---

### Nexus Dashboard Regression Testing Automation

**Type:** Hardware Automation / Regression Testing / AI-Driven Analysis
**SOW Status:** Not started, in discussion

**Overview:**
Regression testing automation for Nexus Dashboard controllers testing Nexus switches. 30K-40K test cases running daily with 3-4 hour/day manual analysis bottleneck. UI automation challenges with Selenium-based testing that breaks when themes change. Highly reusable project with alignment across two different Cisco teams in India without duplicating resources - same solution applicable to multiple teams.

**Client Stakeholders:** (In-person meetings; will need last names from Neha and Zahra)
- Rama (Test Manager)
- Milesh
- Nilesha
- Sonawee

**Alignment:** Gaurav Kotiyal (Director Client Services, India) and Priya Kalyanasundaram (CTO)

**Technical Approach:**
Build graph topology of codebase (multi-dimensional, state-aware) showing relationships between files, tests, and dependencies. Updates as code changes for efficient impact analysis. Identifies primary vs. secondary failures hierarchically to avoid noise. Same approach being used for Arun's NX-OS CI/CD team, creating natural alignment and reusability.

**Effort:** Medium to high depending on scope, would require larger team

**Current Status:** Need and interest confirmed. Cisco engineers are extremely forthcoming and proactive, providing content and materials without being asked - strong signal of trust and commitment. Not pressing at the moment; recommendation is to address after current Cisco POCs are delivered as team is at capacity. Real opportunity to pursue once team scales. Highly reusable for other companies and clients.

---

### MDS Code Modernization

**Type:** Software Modernization / Code Modernization
**SOW Status:** Active delivery, SOW approved after prolonged procurement delay

**Overview:**
Modernizing MDS Element Manager (device management tool for SAN/Fibre Channel switches) from legacy Java Swing thick client to React frontend with Go backend. Related to UI Conversion project - both are element management system modernization efforts but separate SOWs. Legacy codebase stuck on Java 1.8 with 1,432 Java files and 242K lines of code.

**Client Stakeholders:**
- Guhan Raman (Director)
- Selva Subramanian (Engineering Manager and Lead)

**BayOne Liaison:** Gaurav Kotiyal (Director Client Services, India)
**Should Also Involve:** Priya Kalyanasundaram (CTO)

**Technical Approach:**
AI-driven code modernization using agentic tooling. Autonomous discovery, purpose-built agents for specific migration tasks, rule-based architecture for reliability, automated validation. Understanding-of-current-state document and approach proposal have been delivered.

**Effort:** Medium-high, as we do not have much here

**Current Status:** Active delivery. Onboarding items including GitHub Enterprise training, VPN access, and DeepSight platform onboarding are in motion. Colin has Bay Area availability week of 3/23 for in-person sessions. Strongest current proof point for BayOne's AI and engineering capabilities.

---

## SEPHORA

### EDW Modernization Program

**Type:** Enterprise Data Warehouse Re-engineering / AI Acceleration
**Budget:** Multi-million dollar potential (TBD based on POC results)
**SOW Status:** POC delivery March 31st, formal SOW to follow

**Overview:**
Three-year enterprise data warehouse re-engineering program transitioning from SQL Server + IBM Cognos + IBM DataStage to Databricks. Re-engineering 6,000+ reports (15-20 years of legacy logic), 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20+ source systems. Huge scope opportunity with potential to reduce timeline from 3 years to 1.5 years minimum, possibly 9 months or less with AI acceleration. Easy to get deeply embedded with high visibility to CIO. Team has significant budget ready.

**Domain Tracks:**
- **Current:** Finance (leadership believes nearly complete; actual status ~5% due to slow progress)
- **Future:** Merchandising, Supply Chain, Stores, E-commerce/Omni

**Engagement Models (Three Options):**
1. **Full Handoff:** Complete project accountability on BayOne
2. **70/30 Collaboration:** Work with their teams, upskilling while delivering (ideal scenario)
3. **Pure Staffing:** No ownership/accountability (least preferable, not currently entertained)

**Client Stakeholders:**
- Vlad Kuznetsov (CIO)
- Mani Soundararajan (VP, Decision Maker)
- Andrew Ho (Sr. Director)
- Gariashi Chakraborty (Director)
- Maher Burhan (Enterprise Architect)
- Sergey Shtypuliak (IBM Tools SME)
- Terti (Semantic Layer Co-lead)
- Malika Seth (Demo Requirements Coordination)

**Team:**
- **BayOne Lead:** Colin Moore (Director of AI)
- **Support:** Zahra Syed (Strategic Accounts), Neha Malhotra (Recruiting)

**Technical Approach:**
Agent-assisted orchestration using hybrid deterministic + AI methodology. Cognos SDK integration for programmatic report extraction, DataStage CLI integration, schema mapping with confidence-based routing, persistent knowledge graph across tracks. Scaling with agents more than people.

**Effort:** POC is medium-low (team addressed); full scope is medium-to-high

**Current Status:** POC on track for March 31st delivery. No promises yet on time savings until POC demonstrates full complexity. After POC, will explore formal SOW creation with three engagement model options.

---

### Staffing / Talent Acquisition Engagement

**Type:** Staffing / AI Talent Acquisition
**SOW Status:** Active placements

**Overview:**
Building internal AI team for Ravi Pandey at Sephora. Pure staffing engagement with focus on upselling quality remote US talent and in-person placements over lower-quality nearshore options. Strong relationship with Ravi established. High visibility to CIO, representing two-pronged approach with Sephora across multiple projects, building BayOne as household name.

**Client Stakeholders:**
- Ravi Pandey (Building Internal AI Team)

**Team:**
- **Business Owner:** Zahra Syed (Strategic Accounts)
- **Interviews:** Colin Moore (Director of AI, conducting all interviews)
- **Sourcing Support:** Vinayak's team (Colin assisting)

**Active Placement:**
- Abhinav Gupta (placed at higher pay rate)

**Effort:** Medium (takes substantial Colin time, but dual benefit: same people Ravi needs = same Colin needs for internal team; sourcing for one leads to sourcing for both)

**Current Status:** Great relationship with Ravi forged through quality and trust. Team acceptance rate improved from under 15% (before Colin training) to 80% first-time acceptance rate with Colin. With Sephora specifically: 100% acceptance rate due to high scrutiny in process. This quality focus has built strong trust with Ravi and his team. Highly effective for both internal hiring and general AI hiring.

---

### AI-Assisted Development Tooling Initiative

**Type:** Engineering Productivity / Developer Tooling
**SOW Status:** In discussion, no SOW

**Overview:**
Building AI-powered automation for engineering/QA/QE teams, developing Claude Code skills and agents, introducing new AI tools and workflows. Well aligned with other initiatives ongoing at Cisco and beyond.

**Client Stakeholders:**
- Ravi Pandey

**Technical Approach:**
Claude Code, Cursor, Windsurf, Python, Claude Agent SDK, LangChain, LangGraph for AI-powered automation and skills/agents development.

**Effort:** TBD

**Current Status:** In discussion. Nothing firm, no SOW. Relationship has evolved from Ravi wanting to keep us at arm's length as a pure staffing partner to being open to technical partnership for solutions.


## LAM RESEARCH

### Custom NER/Redaction for IP Protection

**Type:** Custom AI / NLP / IP Protection / Data Governance
**SOW Status:** Discovery completed, follow-up pending

**Overview:**
Lam Research suspended all AI/GenAI usage organization-wide due to IP protection concerns. Their customers (TSMC, Samsung, Intel, Micron, SK Hynix) are direct competitors, and Lam manages production data from all parties. They need custom detection and redaction capabilities to safely re-enable AI tools across the organization. Two use cases: self-help knowledge search and ticket escalation system, both requiring high accuracy (under 1% false positive for real-time detection).

**Client Stakeholders:**
- Bradley Estes (Managing Director, Knowledge & Advanced Services)
- Mikhail Krivenko (Head of Product)
- Daniel (Technical Lead)

**Technical Approach:**
Enterprise-grade tooling approach leveraging Microsoft Purview and Azure AI stack. Colin has direct experience building similar detection and redaction systems at Coherent Corp in the semiconductor industry.

**Effort:** TBD pending technical discovery

**Current Status:** Discovery call completed 3/12/2026. Mildly-defined technical problem with abstract success criteria, but easy to formalize. Client driving engagement structure appropriately. Follow-up meeting with technical lead Daniel expected. Note: Internal coordination challenges have been addressed with leadership.

---

## SITIME

### Salesforce CRM Query Layer

**Type:** AI / NLP / Salesforce Integration
**SOW Status:** Early stage, evaluating viability

**Overview:**
SiTime scaling to $1B revenue and integrating Renesas timing division acquisition. Product catalog is extremely parametric (frequency, jitter, phase noise, voltage, package, temp range, etc.). Sales reps need AI layer on Salesforce CRM for natural language product matching to help match customer specs to SKUs. Similar system already working on external website for customer-facing product queries.

**Client Stakeholders:**
- Jyothi Gorti (EVP & Chief Digital Officer)
- Judy Ash (VP, Digital CX Marketing)
- Piyush Sevalia (EVP Marketing, Introducer)

**Technical Approach:**
AI layer on top of Salesforce CRM enabling natural language queries. Viability depends on Salesforce data structure and requires technical discovery before scoping. Investigating partnership with Impinger AI (suggested by Priya Kalyanasundaram, CTO) since this is low-value work comparatively speaking to other projects.

**Effort:** TBD pending technical discovery

**Current Status:** Early stage. Meeting held 3/12/2026. Colin evaluating if real AI engagement exists. Only Salesforce query layer is legitimate AI thread; other items discussed (M&A integration, SharePoint intranet, website vendor selection) are not AI work or already decided. Requires no-strings discovery before commitments. Must confirm bandwidth and priority with Surej first.


---

## TAILORED BRANDS

### AI Adoption in Engineering

**Type:** AI Training / Enablement
**SOW Status:** Exploratory, no concrete engagement

**Overview:**
Structured training, best practices, and enablement for development teams to drive AI adoption in engineering workflows. Identified by Surej as potential entry point. This has not been an articulated need from the client - it is something BayOne is prescribing, though they are likely to want it. Client is very early in their AI journey.

**Client Stakeholders:**
- Kalyan (Director of AI)
- Shiva (Engineering Leader)

**Effort:** TBD

**Current Status:** Very early stage. No concrete problem statements from client. Monitoring for when client readiness matures.

---

### Platform Migration with AI-Enabled Development

**Type:** Platform Modernization / Code Migration
**SOW Status:** Exploratory, no concrete engagement

**Overview:**
Legacy platform replacement with hundreds of integration wrappers to migrate while maintaining all integration touchpoints. Investigating partnership with Impinger AI to support delivery given early stage and lower strategic priority.

**Client Stakeholders:**
- Kalyan (Director of AI)
- Shiva (Engineering Leader)

**Technical Approach:**
Agentic approach with autonomous discovery and purpose-built agents. Leveraging reusable demo from Sephora work.

**Effort:** TBD

**Current Status:** Very early stage. No concrete problem statements from client. Potential partnership with Impinger AI for execution. Monitoring for when client readiness matures.
