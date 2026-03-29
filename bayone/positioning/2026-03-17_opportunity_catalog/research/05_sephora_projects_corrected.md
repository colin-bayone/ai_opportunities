# Sephora Projects - Corrected Research (Auditable)

**Date:** 2026-03-17
**Research Method:** File-by-file reading (no keyword search)
**Files Reviewed:** 89 files in sephora/ folder + 3 Claude session folders

---

## SEPHORA CLIENT PROJECTS (BayOne Engagements)

### PROJECT 1: EDW Modernization Program

**Description:**
Three-year enterprise data warehouse re-engineering program (NOT migration) transitioning from SQL Server + IBM Cognos + IBM DataStage to Databricks while retaining Cognos front-end for change management. Re-engineering 6,000+ reports (15-20 years of legacy logic), 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20+ source systems, thousands of DataStage ETL pipelines. Finance track nearly complete, followed by Merchandising, Supply Chain, Stores, E-commerce/Omni.

**Team/Stakeholders:**
- **Sephora:** Vlad (CIO), Mani Soundararajan (VP Data & Analytics - decision maker), Andrew Ho (Sr. Director - semantic layer co-lead, internal champion for agent automation), Gariashi Chakraborty (Director Data Engineering/BI - technical gatekeeper), Maher Burhan (Enterprise Architect), Sergey Shtypuliak (IBM Tools SME), Terti (semantic layer co-lead)
- **BayOne:** Colin Moore (Director of AI, technical lead), Zahra Syed (Director Strategic Accounts), Neha Malhotra (Head of Recruiting)

**Technologies:**
- **Source:** SQL Server (EDW), IBM Cognos 10.2/10.3, IBM DataStage, SSAS cubes
- **Target:** Databricks (Azure), Cognos (retained front-end), future ThoughtSpot/Tableau
- **Approach:** Agent orchestration, MCP servers, Claude Code, Azure AI Foundry, knowledge graphs, confidence-based routing

**Budget/Timeline:**
- Timeline: 3-year program (2026-2028), started late 2025/Jan 2026, aspiration to compress to 1.5 years with AI acceleration
- Finance track: In progress through end of 2026 (~20-24 days remaining as of Feb 2026)
- Budget: Not disclosed; proposal requested with 3 options (limited scope pilot, co-delivery, larger partnership)
- Current efficiency: 30% gain with manual Claude usage
- Two tracks: Staffing (ongoing) + Solutions (proposal stage)

**Status:**
Active - Finance track in progress, Databricks migration just started (very early stages), proposal development underway for AI acceleration solutions

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani-transcript1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani_transcript2.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/andrew-girishi-meeting1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/00_project_overview.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/03_scope_and_scale.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/deliverables/03_edw_acceleration_framework.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-05_big4_sephora_technical_deep_dive/source/04_technical_deep_dive_framework.md

**Work Streams (Internal Detail):**
- Report re-engineering (6,000+ Cognos reports)
- SSAS cube transition (8 cubes to Databricks with Excel preservation)
- ETL pipeline conversion (DataStage → Databricks)
- Schema mapping (SQL Server EDW → Databricks)
- Semantic layer establishment (cross-tool consistency)
- Domain tracks (Finance, Merchandising, Supply Chain, Stores, E-commerce)

---

### PROJECT 2: Staffing / Talent Acquisition Engagement

**Description:**
Active staffing engagement across multiple hiring managers and domains to support EDW modernization and AI/ML initiatives. Two distinct skill buckets: (1) general full-stack developers, (2) AI-enabled developers. Multiple entry points across domain teams as Sephora transitions from centralized to decentralized reporting model.

**Team/Stakeholders:**
- **Sephora Hiring Managers:** Ram Soundararajan (Acquisition & Retention), Andrew Ho (Influencer/Media/Marketing AI), Gariashi Chakraborty (Data Engineering/BI), Rizwan Khan (CRM & Personalization - Q1 2026)
- **Peer Organizations:** David/Natalia (Stores), Rajesh (E-commerce/Omni)
- **BayOne:** Neha Malhotra (Head of Recruiting - staffing lead), Zahra Syed (relationship lead), Colin Moore (technical vetting)

**Technologies:**
Skills needed: Full Stack (general), Full Stack + AI (AI tooling/acceleration), Data Engineering + AI (data processing with AI), Agentic AI (emerging future need), Azure, Databricks, Python, Spark, MLOps

**Budget/Timeline:**
- Staffing rates: $105-115/hr acceptable range; $120+/hr only if on-site; >$120/hr not acceptable
- Location preference: Nearshore US (Oklahoma, Kansas, Utah at ~$75-100/hr); Bay Area on-site acceptable
- Timeline: Ongoing hiring (2026+)
- Multiple hiring managers = multiple entry points and parallel hiring tracks

**Status:**
Active hiring - candidates in process with Gariashi, Ram actively hiring, Andrew hiring with SOW discussions, Rizwan ramping late Q1 2026

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani-transcript1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/08_staffing_details.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/05_budget_rates_financials.md

**Note:**
This is a SEPARATE project from EDW Modernization - different accountability track (staffing vs. solutions), different budgets, different ownership (Neha vs. Colin/Zahra)

---

### PROJECT 3: ML Production Initiatives (Ravi's Team)

**Description:**
Four active production ML initiatives driving customer experience: (1) Generative AI for product discovery, (2) Personalized in-session recommendation engine (in-store and online), (3) Customer segmentation, (4) Next-best offer prediction. Requires ML data infrastructure build-out to support these production systems at scale.

**Team/Stakeholders:**
- **Sephora:** Ravi (hiring manager, ML team lead), Product teams, Engineering teams, Data Scientists, Business teams
- **BayOne:** Hiring for Data Engineer, ML Engineer, ML Platform Engineer, AI Engineer roles to support

**Technologies:**
- **ML Stack:** PyTorch/TensorFlow/Keras, Azure ML, MLOps, feature stores, batch and real-time ML systems, A/B testing
- **Data Infrastructure:** Azure, Spark, Kafka, Hadoop, Databricks, SQL/NoSQL databases, Docker
- **AI Tools:** LLMs, LLMOps, Azure AI, Python

**Budget/Timeline:**
- Status: In action (active production initiatives)
- Budget: Not disclosed
- Timeline: Ongoing 2026+
- Hiring: Active recruitment for multiple roles to support

**Status:**
Active production - these are live ML systems driving business outcomes, hiring to expand team capacity

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/ravi-ml-jd.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ml_engineer/jd_ml_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/data_engineer/jd_data_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ml_platform_engineer/jd_ml_platform_engineer_sephora.md

**Note:**
This is distinct from the EDW Modernization project - different team (Ravi vs. Mani/Andrew/Gariashi), different focus (ML production systems vs. data warehouse re-engineering), though both fall under Sephora's broader data & AI transformation

---

### PROJECT 4: AI-Assisted Development Tooling Initiative

**Description:**
Building AI-powered automation for engineering/QA/QE teams, developing Claude Code skills and agents, introducing new AI tools and workflows to accelerate development velocity. High-visibility engagement to transform how Sephora's engineering teams work with AI tooling.

**Team/Stakeholders:**
- **Sephora:** Engineering teams, QA teams, QE teams
- **BayOne:** Hiring AI Engineer role to lead implementation, Colin Moore (oversight)

**Technologies:**
Claude Code, Cursor, Windsurf, Python, Claude Agent SDK, LangChain, LangGraph, AI-powered automation, skills/agents development

**Budget/Timeline:**
- Status: Hiring for implementation
- Budget: Not disclosed
- Timeline: Immediate start required (active hiring)

**Status:**
Pre-implementation - hiring stage

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ai_engineer/jd_ai_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-26_sephora-hiring/

**Note:**
Distinct initiative focused on engineering productivity and tooling, separate from EDW and ML production projects

---

### PROJECT 5: EDW Modernization POC/Demo Projects

**Description:**
Three interconnected proof-of-concept demonstrations to validate AI-driven agent orchestration capabilities before larger EDW engagement: (1) Cognos MCP Demo - automated report extraction and conversion, (2) DataStage YAML Demo - ETL job parsing and configuration generation, (3) Enhanced Agent Orchestration Demo - end-to-end workflow automation across multiple tools.

**Team/Stakeholders:**
- **Sephora:** Mani, Andrew Ho, Gariashi, Maher Burhan, Sergey Shtypuliak, Malika
- **BayOne:** Colin Moore (solo for POC), Zahra, Neha

**Technologies:**
- **Cognos Track:** MCP server, Cognos SDK, Content Store, multi-agent orchestration, XML parsing, SQL transformation, Databricks schema mapping
- **DataStage Track:** DataStage XML parsing, stored procedure analysis, YAML generation, existing Databricks framework integration
- **Overall:** Agent orchestration, automated extraction, tool communication, task sequencing, dependency handling

**Budget/Timeline:**
- Budget: Proof-of-concept scope (investment in sales process, not charged)
- Timeline: Demo session after materials received (ETL materials received, awaiting Cognos materials)
- Status: Scoped in Meeting 4, expanded requirements via Malika's email

**Status:**
Materials gathering phase - ETL track materials received, Cognos track materials pending, demo session to be scheduled

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/01_meeting_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/scoping/track_a_cognos_mcp_demo.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/scoping/track_b_etl_datastage_demo.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/research/06_malika_email_breakdown.md

**Note:**
These are PRE-SALES demonstrations to prove capability before Project 1 (EDW Modernization) solutions engagement. Success of POC determines paid engagement scope.

---

## SEPHORA ORGANIZATIONAL INITIATIVES (Context Only - Not BayOne Projects)

These were mentioned in documentation but are Sephora internal initiatives, not projects BayOne is working on:

### Reporting Democratization (2026 Organizational Transformation)
- Description: Shift from centralized reporting under Mani to embedded domain teams
- Three operating models being tested (Stores, E-commerce/Omni, Supply Chain/Merchandising)
- Timeline: 2026 transition year
- **Not a BayOne project - it's organizational change management context**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/02_organizational_map.md

### Marketing AI Task Force
- Description: Marketing-focused AI initiatives (journey orchestration, CRM personalization, influencer marketing, agentic AI exploration)
- Owner: Mani's organization
- **Not a BayOne project - it's internal Sephora initiative that may create future opportunities**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani-transcript1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/04_ai_opportunities.md

### Ram's 2026 Acquisition & Retention Projects
- Description: Two major 2026 projects (unnamed) in acquisition & retention domain
- Domain: Digital billboards, TV ads, social media, retention/post-purchase
- **Not a BayOne project yet - potential future opportunity, Ram is active hiring manager**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/02_organizational_map.md

---

## BAYONE PAST PROJECTS (Referenced as Case Studies/Experience)

These were mentioned as BayOne experience examples during Sephora discussions:

### Wayfinder (Lamo/Lampo)
- Description: AI employee portal showing available AI tools to employees
- Timeline: ~3 months to complete
- Led by Colin Moore
- **Referenced as case study during Sephora conversations**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani_transcript2.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/email1.txt

### Patter
- Description: Architecture-focused project with high degree of freedom
- **Referenced as BayOne case study example**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt

### Evaluator
- Description: Custom Databricks connectors project
- **Referenced as BayOne case study example**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt

---

## COLIN'S PRIOR EXPERIENCE (Not BayOne Projects)

### Coherent BI Migration
- Organization: Coherent (Colin's previous employer, 40,000 employees, $16B revenue)
- Description: Enterprise BI reporting and migration from SSAS/SSRS to Snowflake + Tableau/Power BI
- Colin's Role: Led BI reporting and migration
- **Direct parallel experience to Sephora EDW modernization**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/02_pain_points.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt

### Hyperion Excel Connector (at Coherent)
- Description: Custom Excel connector for Hyperion financial system
- Challenge: Complex data structure mapping for BI tools
- **Relevant to SSAS-to-Databricks Excel preservation challenge at Sephora**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt

---

## CANDIDATE PRIOR WORK (Interview Context)

### Enterprise Security Analysis System with MCP
- Description: Full enterprise security analysis system with three coordinating AI agents, MCP for structured data, RAG for unstructured security advisories
- Built by: Anushree Joshi (candidate for AI Engineer role)
- **Referenced during interview as relevant experience, not a Sephora project**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-26_sephora-hiring/candidate_guide/anushree_joshi_recruiter_feedback.md

---

### PROJECT 6: Agentic QE Offering

**Description:**
Agentic AI-enabled quality engineering offering for Sephora, combining Priya's QE expertise with Colin's AI capabilities. Discovery of what Sephora's ~200 test engineers are doing, followed by a to-be state using a combination of people and agents to deliver the same or higher quality QE at 40-50% cost reduction with higher speed.

**Team/Stakeholders:**
- **Sephora:** QE team (~200 test engineers)
- **BayOne:** Surej (CEO - sponsor), Colin Moore (AI lead), Priya Kalyanasundaram (CTO - QE expertise)

**Technical Approach:**
Transfer learning model where agents mimic existing human workflows, with staggered insertion of agents and gradual dial-down of human involvement as agents learn. Human-in-the-loop and human control aspects remain central throughout.

**Budget/Timeline:**
- Budget: Not disclosed
- Timeline: TBD
- Status: Surej working to schedule initial listening session

**Status:**
Proposal stage. Surej is working to schedule an initial listening session with Sephora's QE team. No pitch on the first call, just understanding what they're doing so BayOne can ask the right questions and come back with a proposal in one to two weeks. Surej indicated high confidence in landing this deal.

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/source/bayone_ai_opportunities_catalog.md

**Note:**
This is a SEPARATE project from EDW Modernization, focused on quality engineering rather than data/analytics.

---

### PROJECT 7: Contractor Upskilling

**Description:**
Building a pipeline of engineers proficient in AI tools. Sephora's leadership (specifically through Ravi Pandey) has asked about this. Broader AI upskilling initiative discussed with Surej encompasses Sephora contractors as one of several populations to train.

**Team/Stakeholders:**
- **Sephora:** Ravi Pandey (requesting Claude Code-proficient engineers), Neha (point of contact at Sephora)
- **BayOne:** Colin Moore (technical lead), Neha Malhotra (business owner - already POC at Sephora)

**Scope:**
Two distinct components:
1. Ravi Pandey request: Claude Code-proficient engineers (narrower skills pipeline ask)
2. General AI upskilling initiative (broader scope)

**Budget/Timeline:**
- Budget: Not disclosed
- Timeline: TBD
- Status: In discussion

**Status:**
Neha is point of contact at Sephora and has provided a resource list. Open questions remain about access restrictions, Sephora-provided AI tools, and corporate policy on AI tool usage. Colin has proposed that this be folded into the unified upskilling initiative rather than treated as a standalone effort.

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/source/bayone_ai_opportunities_catalog.md

**Note:**
Colin's note: This needs to be separated from the Ravi Pandey request for Claude Code-proficient engineers, which is a narrower skills pipeline ask versus a general AI upskilling initiative. These are different in scope and delivery.

---

## SUMMARY TABLE

| # | Project Name | Team/Domain | Status | Budget | Timeline |
|---|--------------|-------------|--------|--------|----------|
| 1 | EDW Modernization Program | Mani/Andrew/Gariashi | Active | TBD (proposal stage) | 2026-2028 (3 years) |
| 2 | Staffing / Talent Acquisition | Multiple hiring managers | Active hiring | $105-115/hr | Ongoing 2026+ |
| 3 | ML Production Initiatives | Ravi's team | Active production | TBD | Ongoing 2026+ |
| 4 | AI-Assisted Development Tooling | Engineering/QA teams | Hiring stage | TBD | Immediate start |
| 5 | EDW Modernization POC/Demo | Mani/Andrew/Gariashi | Materials gathering | POC (free) | Demo after materials |

**Total Confirmed Sephora Projects: 7**
- 2 Active (Projects 1 and 3)
- 1 Active Hiring (Project 2)
- 1 Pre-Implementation (Project 4)
- 1 POC Stage (Project 5)
- 1 Proposal Stage (Project 6)
- 1 In Discussion (Project 7)

---

## KEY DISTINCTIONS

**What are NOT separate projects:**
- "Reporting democratization" - Organizational transformation, not a project
- "Marketing AI task force" - Internal initiative/working group
- "Supply Chain reporting," "Merchandising reporting," "Stores reporting" - Domain tracks within EDW Modernization (Project 1), not separate projects
- "Cognos automation," "DataStage migration," "SSAS transition," "Schema mapping," "Semantic layer" - Work streams within EDW Modernization (Project 1), not separate projects
- "Journey orchestration," "CRM personalization," "Influencer marketing" - Functional areas under Marketing AI task force, not projects

**Two-Track Structure:**
Project 1 (EDW Modernization) has two distinct tracks that are often confused:
- **Staffing track** - Handled by Project 2 (separate ownership, separate budget)
- **Solutions track** - Project 1 proper (AI acceleration, proposal stage)

---

## METHODOLOGY NOTE

This research was conducted using complete file-by-file reading (no keyword search) across 89 files in sephora/ folder plus 3 Claude session folders. All source files are cited for auditability. Projects are distinct initiatives with their own scope, stakeholders, and budgets - NOT work streams within a single project.
