# BayOne Active Opportunities - Internal Catalog

**Date:** 2026-03-17
**Purpose:** Comprehensive internal reference of all active client engagements, projects, and work streams
**Audience:** Internal BayOne team reference
**Status:** Cisco and Sephora complete; Tailored Brands and Zeblok pending

---

## TABLE OF CONTENTS

1. [Executive Summary](#executive-summary)
2. [Cisco](#cisco)
3. [Sephora](#sephora)
4. [Research Methodology](#research-methodology)
5. [Document Index](#document-index)

---

## EXECUTIVE SUMMARY

**Total Clients Cataloged:** 2 (Cisco, Sephora)
**Total Projects Identified:** 9
**Files Reviewed:** 151 files (62 Cisco + 89 Sephora)
**Research Method:** Complete file-by-file reading (no keyword search)
**Date Range:** Documents from late 2025 through March 2026

### Breakdown by Client

| Client | Projects | Status | Budget Range | Timeline |
|--------|----------|--------|--------------|----------|
| **Cisco** | 4 | 2 Active, 1 POC, 1 Exploration | $100K-200K/quarter | Varies by project |
| **Sephora** | 5 | 2 Active, 1 Hiring, 1 Pre-impl, 1 POC | $105-115/hr + TBD | 2026-2028 |
| **TOTAL** | **9** | **Multiple stages** | **Multi-million** | **2026-2028** |

---

## CISCO

**Client Overview:**
Enterprise networking and technology company. Multiple engagements across different teams and products (NX-OS, EPNM/EMS, Nexus switches, testing infrastructure).

**Key Contacts:**
- **Anand** (Director) - NX-OS CI/CD Pipeline project lead
- **Srinivas/Srini** (Senior Engineering Manager) - AI strategy, DeepSight platform owner
- **Divakar/Diwakar** (Engineering Lead) - Day-to-day technical contact, Jenkins/build systems
- **Arun** (VP) - Executive sponsor, budget authority
- **Guhan** (Decision maker) - UI Conversion project
- **Selva** (Technical contact) - UI Conversion project
- **Mahaveer Jinka** (DCN-Switching-India) - Nexus 9000 Testing SOW
- **Rama** (Test Manager) - Nexus Dashboard Testing exploration

**BayOne Team:**
- **Colin Moore** (Director of AI, Technical Lead) - All projects
- **Rahul** (President) - Budget/resourcing authority
- **Amit** (Delivery) - SOW/estimation
- **Zahra** (Sales) - Scheduling/relationship
- **Ashish Singh** - Nexus 9000 Testing execution

---

### PROJECT 1: NX-OS CI/CD Pipeline Improvement

**Type:** Software development / AI integration
**Status:** Active - Discovery phase (started Feb 17, 2026)

#### Description
Multi-phase engagement to improve Cisco's NX-OS CI/CD pipeline with AI-driven tooling. Goal: 20-30% reduction in average PR merge time. Focus on developer visibility (Developer Box instrumentation), branch health dashboards, unified interface, AI-driven failure diagnosis, coverage tracking, and future self-healing capabilities.

#### Scope & Scale
- **Pipeline zones:** 3 (Developer Box/Blue, GitHub-DevX/Green, Official Build-DC BU/Red)
- **Gates:** 39 validation gates via Jenkins and Apache Airflow
- **Phases:** 5 phases (A-F work items)
- **Total estimated effort:** 810-1,230 dev hours over 6-8 months

#### Work Streams (6 total)

**Phase 1 (In Progress):**
- **Item A: Developer Box Instrumentation** - Visibility into local testing, telemetry capture, debugging support (Part of 150-210 hours)
- **Item F: Branch Health / CD Health Dashboards** - Consolidated visibility, failure trends, PR attribution, automated notifications (Part of 150-210 hours)

**Phase 2 (Planned):**
- **Item C: Cross-Pipeline Unified Interface (Chat Interface)** - Consolidate CAT, DevX, Jenkins, Airflow, Grafana data; natural language query interface (180-250 hours)

**Phase 3 (Planned):**
- **Item B: Gate Failures / AI-Driven Diagnosis** - Automate root cause analysis, suggest fixes, reduce manual triage (100-150 hours)

**Phase 4 (Planned):**
- **Item D: Coverage Tracking Enhancement** - Condition-level coverage confirmation, integration with CDT (80-120 hours)

**Phase 5 (Planned/Deferred):**
- **Item E: Self-Healing / Automated Corrective Actions** - Auto-retry transient failures, simple auto-fixes with governance framework (300-500 hours; originally 150-250, revised up due to complexity)

#### Technologies & Platforms
- **Existing:** Jenkins (short checks), Apache Airflow (longer jobs), CAT (Commit Approval Tool), DevX platform, Grafana (analytics), MongoDB (on-prem raw data), MySQL (aggregated metrics), Splunk (security team), CDT (Context Driven Testing - 2+ years live), pyATS (test automation), Bazel (recently rolled out), Podman containers, ADS machines (Linux on-prem)
- **New/Internal:** DeepSight Atlas AI platform (launching Feb/March 2026), DeepSight CI/CD application (Rui leading)
- **BayOne approach:** AI-assisted development with ~2x speedup assumption

#### Team & Stakeholders
- **Cisco:**
  - Arun (VP) - Sponsor, budget authority
  - Anand (Director) - Project coordination, escalation, governance decisions
  - Srinivas (Senior Engineering Manager) - AI strategy, DeepSight platform owner
  - Divakar (Engineering Lead) - Day-to-day access, Jenkins/build owner
  - Rui (on Arun's team) - Leads existing CI/CD app on DeepSight (coordination point)
- **BayOne:**
  - Colin Moore (Director of AI, Technical Lead) - Onsite starting mid-Feb
  - Rahul (President) - Budget/resourcing
  - Amit (Delivery) - SOW/estimation
  - Zahra (Sales) - Scheduling

#### Budget & Resourcing
- **Budget:** $100K per quarter (starting baseline; increases justify as needed)
- **Initial team:** 1-1.5 FTE onshore (Bay Area), 4-5 offshore to scale
- **Discovery:** 1-2 weeks (40-80 hours)
- **Skills needed:** Agentic AI experience (Phase 5), Airflow expertise (single biggest integration point), Web development (frontend/backend/Docker), Senior AI Engineer, Platform/integration engineers

#### Timeline
- **Discovery phase:** 1-2 weeks (started Feb 17, 2026)
- **Phase 1:** 4-5 weeks
- **Total program:** 6-8 months (20-31 weeks sequential)
- **Jan 16, 2026 decision:** Selected A+F as Phase 1 (changed from original C priority)

#### Key Unknowns / Open Questions
1. API documentation quality for CAT, DevX, Jenkins, Airflow?
2. Exact data schema/format from each system
3. Data retention policies (historical analysis depth?)
4. Governance framework scope for self-healing actions
5. Boundary between BayOne work and Cisco's internal AI code review project
6. Development environment repository/code commit workflow
7. Specific failure patterns that dominate (diagnosis prioritization)
8. Complete roster of 39 gates and classification (transient vs. structural)
9. User research: "What questions should chat interface answer?"
10. Infrastructure provisioning model (self-service vs. IT-provisioned)

#### Infrastructure Context (Not BayOne projects)
- **DeepSight Atlas Platform** - Cisco's internal AI platform providing SDK, models, UI framework for AI apps (Srinivas owner)
- **DeepSight CI/CD App** - Existing app launching on DeepSight that BayOne will extend (Rui leading, 90% complete as of Feb 17)
- **Bazel Rollout** - Google's build system just rolled to production (context for build issues)

#### Related Cisco Work (NOT in BayOne scope)
- **AI Code Review project** - Cisco internal, going live soon (boundary to be clarified)
- **Code refactoring/modernization** - Explicitly NOT coming to BayOne

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/project/engagement-status.md
- /home/cmoore/programming/cisco_projects/cicd/history/0001_2026-02-02_initial-state.md
- /home/cmoore/programming/cisco_projects/cicd/documents/cisco-understanding-of-problem.md
- /home/cmoore/programming/cisco_projects/cicd/documents/cisco-problem-areas-by-bucket.md
- /home/cmoore/programming/cisco_projects/cicd/documents/cisco-dev-hours-estimate.md
- /home/cmoore/programming/cisco_projects/cicd/documents/cisco-x-bayone.md
- /home/cmoore/programming/cisco_projects/cicd/new_context_2-2-2026/meetings/email-1-16-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/new_context_2-2-2026/meetings/rahul1.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting1_anand_srini_divakar-2-17-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/meeting1_anand_srini_divakar/00_meeting_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/session-kickoff.md

---

### PROJECT 2: UI Conversion (EPNM to EMS)

**Type:** Software modernization / AI-accelerated code conversion
**Status:** POC Stage - Waiting on hardware/access (~March 18, 2026 start)

#### Description
Convert legacy EPNM (Evolved Programmable Network Manager) UI screens to modern EMS (Element Management System) architecture. NOT just UI skinning - requires extracting tightly-coupled functionality from 15+ year old monolithic system and re-implementing in microservices. Key customers demand old UI be retained because network operators trained on it for 15+ years. 70-100 screens potentially need conversion; POC focuses on 2-3 screens in 4 weeks.

#### Scope & Scale
- **Total screens:** 70-100 potential
- **POC scope:** 2-3 screens (Cisco initially suggested 10; too much for free work)
- **Timeline:** 4 weeks POC (2 weeks exploration/screen selection, 2 weeks conversion/testing)
- **Products:** EPNM (legacy, 15+ years) vs. EMS (modern microservices)

#### Technologies
- **Backend:** Java (both systems)
- **Frontend Old (EPNM):** Dojo, JavaScript, some Angular
- **Frontend New (EMS):** Angular
- **Architecture:** Monolithic → Microservices ("vertical work" - if frontend doesn't exist, backend doesn't either)
- **Testing:** Playwright (BayOne's approach)
- **AI Tools:** Claude Code, LangGraph agent swarm
- **Constraint:** All work must be done on Cisco hardware with Cisco-licensed AI tools; no code leaves Cisco infrastructure

#### Team & Stakeholders
- **Cisco:**
  - Guhan (Decision maker)
  - Selva (Technical contact)
  - Team availability: Limited ("on critical platform work")
- **BayOne:**
  - Colin Moore (Director of AI, solo for POC; team for paid engagement)

#### Budget & Timeline
- **POC:** Free (4 weeks, Colin solo)
- **Paid engagement:** TBD based on POC success
- **POC start:** ~March 18, 2026 (waiting on Cisco laptop delivery 1-2 weeks from Feb 20)
- **Security:** NDA signed, Cisco laptop arriving, code access needed

#### Technical Approach
- **"Flywheel Effect"** - POC is front-loaded with one-time investment:
  - Codebase exploration and knowledge graph
  - Pattern identification and conversion library
  - Custom agent development
  - Workflow design and validation
  - Playwright testing infrastructure
- **Result:** 2-3 screens in 4 weeks doesn't extrapolate linearly to 200 screens (multiplicative speedup after initial investment)

#### Phases
1. **Phase 1 (2 weeks):** Exploration and onboarding - codebase analysis, screen selection (collaborative with Cisco SMEs)
2. **Phase 2 (2 weeks):** Conversion, testing, and acceptance

#### Key Distinction
This UI conversion work is SEPARATE from Project 1 (NX-OS CI/CD). Different product (EPNM/EMS vs. NX-OS), different scope, different team (Guhan/Selva vs. Anand/Srinivas/Divakar).

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/source/guhan_selva-2-20-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/00_session_handoff.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/01_meeting_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/01_session_understanding.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/06_poc_proposal_v6.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/research/03_chronological_timeline.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/research/04_themes_and_decisions.md

---

### PROJECT 3: Building Nexus 9000 Switches Product Line Testing

**Type:** Test automation / AI solutions / Regression testing
**Status:** Active Contract (Nov 5, 2025 - Apr 30, 2026)

#### Description
Cisco's Cloud Networking Group (CN) Test team engagement for validating NX-OS releases for Nexus 9000 switches product line. Active SOW covering regression testing execution, test case automation, building AI solutions (data pipelines, AI models), testing and deployment in production, and infrastructure tools development.

#### Scope & Scale
- **Product line:** Nexus 9000 switches
- **Focus:** NX-OS release validation
- **Contract reference:** #33282
- **Deliverables:** Regression testing, test automation, AI solutions, data pipelines, production deployment, infrastructure tools

#### Technologies
- NX-OS testing
- Test automation
- AI solutions
- Data pipelines
- Regression testing infrastructure

#### Team & Stakeholders
- **Cisco:**
  - Mahaveer Jinka (DCN-Switching-India) - SOW owner
- **BayOne:**
  - Ashish Singh - Execution lead
  - BayOne Techno Advisors Private Limited (vendor entity)

#### Budget & Timeline
- **Budget:** Rs 4,393,740.00 INR (approx $100K USD equivalent)
- **Timeline:** Nov 5, 2025 - Apr 30, 2026 (6 monthly milestones)
- **Status:** Active contract, currently in execution

#### Key Distinction
This is DIFFERENT from Project 1 (NX-OS CI/CD Pipeline). Both involve NX-OS, but:
- **Project 1:** Development pipeline improvement (Anand/Srinivas/Divakar team)
- **Project 3:** Testing/validation for product releases (Mahaveer team)
- Different teams, different scope, different contracts

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches.md
- /home/cmoore/programming/cisco_projects/cicd/SOW/SESSION_HANDOFF.md
- /home/cmoore/programming/cisco_projects/cicd/SOW/SOW-conversion-notes.md

---

### PROJECT 4: Nexus Dashboard Regression Testing Automation

**Type:** AI-driven test analysis automation
**Status:** Exploration Phase

#### Description
AI-driven automation for regression test analysis and UI testing for Nexus Dashboard (network controllers). Rama's Test Manager team faces a 3-4 hour/day bottleneck analyzing regression results. Seeking AI solutions to automate analysis and accelerate feedback loops.

#### Scope & Scale
- **Product:** Nexus Dashboard (network controllers)
- **Pain point:** 3-4 hours/day manual analysis bottleneck
- **Goal:** Automate analysis, accelerate feedback

#### Technologies
- Jenkins
- Selenium (UI testing)
- Python
- Cisco automation infrastructure layer
- Cisco Circuit (AI tool)

#### Team & Stakeholders
- **Cisco:**
  - Rama (Test Manager) - Pain point owner
  - Milesh, Nilesha, Sonawee (team members)
- **BayOne:**
  - Colin Moore (exploration discussion)

#### Budget & Timeline
- **Budget:** Not established
- **Timeline:** TBD
- **Status:** Exploration/discussion phase only (no formal engagement or proposal yet)

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting2_rama-2-17-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/meeting2_rama/00_meeting_breakdown.md

---

## SEPHORA

**Client Overview:**
Fortune 500 beauty retailer. Multiple engagements across data engineering, ML/AI, staffing, and enterprise data warehouse modernization.

**Key Contacts:**
- **Vlad** (CIO) - Top executive sponsor
- **Mani Soundararajan** (VP, Marketing Tech/Personalization/Data-AI/Reporting) - Decision maker for EDW, budget holder
- **Andrew Ho** (Sr. Director, Influencer/Media/Marketing AI) - Internal champion for agent automation, semantic layer co-lead
- **Gariashi Chakraborty** (Director, Data Engineering/BI) - Technical gatekeeper, execution lead
- **Maher Burhan** (Enterprise Architect) - Pragmatic solutions focus
- **Sergey Shtypuliak** (IBM Tools SME) - Deep technical expertise
- **Terti** (Role unknown) - Semantic layer co-lead with Andrew
- **Ram Soundararajan** (VP, Acquisition & Retention) - Hiring manager (active)
- **Rizwan Khan** (Director, CRM & Personalization) - Hiring manager (Q1 2026)
- **Ravi** (Hiring Manager) - ML initiatives lead
- **David/Natalia** (Stores domain leadership) - Testing Model 1 decentralization
- **Rajesh** (E-commerce/Omni leadership) - Testing Model 2 decentralization

**BayOne Team:**
- **Colin Moore** (Director of AI, Technical Lead) - All technical projects
- **Zahra Syed** (Director Strategic Accounts) - Sales/relationship lead
- **Neha Malhotra** (Head of Recruiting) - Staffing coordination
- **Rahul** (President) - Executive level
- **Amit** (Delivery) - Execution

---

### PROJECT 1: EDW Modernization Program

**Type:** Enterprise data warehouse re-engineering / AI acceleration
**Status:** Active - Finance track in progress, proposal development underway

#### Description
Three-year enterprise data warehouse re-engineering program (NOT migration) transitioning from SQL Server + IBM Cognos + IBM DataStage to Databricks while retaining Cognos front-end for change management. Re-engineering 6,000+ reports (15-20 years of legacy logic), 8 SSAS cubes, 800+ KPIs, 300 dimensions, 20+ source systems, thousands of DataStage ETL pipelines. Finance track nearly complete, followed by Merchandising, Supply Chain, Stores, E-commerce/Omni.

**Two Tracks:**
1. **Solutions Track:** AI acceleration for migration (proposal stage)
2. **Staffing Track:** Separate project (see Project 2 below)

#### Scope & Scale
- **Reports:** 6,000+ Cognos reports (15-20 years of accumulated logic)
- **SSAS Cubes:** 8 cubes
- **KPIs:** 800+
- **Dimensions:** 300
- **Source Systems:** 20+
- **ETL Pipelines:** Thousands of DataStage jobs
- **Legacy age:** ~20 years
- **Processing:** Batch only (no real-time currently)

#### Work Streams (Domain Tracks)
1. **Finance** - In progress through end of 2026 (~20-24 days remaining as of Feb 2026), architectural patterns established
2. **Merchandising** - Next candidate
3. **Supply Chain** - Next candidate
4. **Stores** - Later phase
5. **E-commerce/Omni** - Later phase

#### Work Streams (Technical Components)
- **Report re-engineering** - 6,000+ Cognos reports conversion
- **SSAS cube transition** - 8 cubes to Databricks with Excel preservation (major blocker/challenge)
- **ETL pipeline conversion** - DataStage → Databricks
- **Schema mapping** - SQL Server EDW → Databricks (non-1:1 transformation)
- **Semantic layer establishment** - Cross-tool consistency (Cognos, ThoughtSpot, future BI tools)
- **Business logic extraction** - Queries buried in reports, tribal knowledge capture

#### Technologies & Platforms
**Source Stack:**
- SQL Server (EDW)
- IBM Cognos 10.2/10.3 (reporting front-end, RETAINED during transition)
- IBM DataStage (ETL)
- SSAS cubes (OLAP)

**Target Stack:**
- Databricks (Azure) - lakehouse architecture
- Cognos (retained front-end - change management consideration)
- Future: Tableau, ThoughtSpot (BI tools)
- Azure cloud infrastructure

**AI Acceleration Approach (Proposed):**
- Agent-assisted orchestration (not just generative AI)
- Hybrid deterministic + AI methodology
- Cognos SDK integration for programmatic report extraction
- DataStage dsjob/dsexport CLI integration
- Schema mapping with confidence-based routing
- Persistent knowledge graph across tracks
- MCP (Model Context Protocol) servers
- Claude Code, Azure AI Foundry
- Proof-of-concept first, then scale

**Current State:**
- Finance track in progress (~20-24 days remaining as of Feb 2026)
- Databricks migration started Jan 2026 (very early stages - "very less progress," few tables out of ~1,000 in EDW)
- Databricks environment itself is "very mature" (thousands of jobs, P1 applications)
- Already achieved ~30% efficiency gains with manual Claude usage for SQL transformation
- Current workflow manual; aspiration is orchestrated agent workflow

#### Team & Stakeholders
- **Sephora:**
  - Vlad (CIO) - Top executive sponsor
  - Mani Soundararajan (VP) - Decision maker, budget holder (reports to Vlad)
  - Andrew Ho (Sr. Director) - Governance table, semantic layer co-owner, internal champion for automation
  - Gariashi Chakraborty (Director) - Execution lead, technical gatekeeper
  - Terti - Semantic layer co-lead (with Andrew)
  - Maher Burhan (Enterprise Architect, Consultant) - Practical solutions, security workarounds
  - Sergey Shtypuliak (SME IBM Tools, Consultant) - Deep technical expertise, YAML requirements for DataStage
  - Malika - Demo requirements clarification (email correspondent)
  - **Governance table partners:** Databricks, Microsoft (Azure)

- **BayOne:**
  - Colin Moore (Director of AI, Technical Lead)
  - Zahra Syed (Director Strategic Accounts, Sales/relationship)
  - Neha Malhotra (Head of Recruiting, Internal coordination)

#### Budget & Timeline
- **Timeline:** 3-year program (2026-2028), started late 2025/Jan 2026
- **Acceleration target:** Complete by 2027 or early 2028 (if AI-accelerated; aspiration to compress to 1.5 years)
- **Finance track:** In progress through end of 2026
- **Budget (Solutions):** Unknown specific budget; Mani asked "What kind of investment?"; proposal requested with 3 options and cost ranges
- **Budget (Staffing):** See Project 2 (separate track)
- **ROI framing:** Time saved, efficiency gains, acceleration value
- **Current efficiency:** 30% gain with manual Claude usage
- **Andrew's preference:** Invest upfront in agents vs. long-term manual contractors

#### Known Pain Points / AI Opportunities
1. **SSAS Cube migration blocker** - Not technical (ODBC/JDBC connector exists), but change management issue; business users demand Excel drag-and-drop experience
2. **Report-by-report migration too slow** - Batch processing, pattern detection needed
3. **Embedded SQL complexity** - Queries buried in Cognos reports, business logic extraction required
4. **Data mapping is slowest phase** - Manual validation creates bottleneck
5. **Tribal knowledge loss risk** - 20 years of logic undocumented
6. **SME bandwidth constraint** - Same experts keep production running AND validate migration

#### AI Acceleration Capabilities (Explicitly Stated by Mani)
- Batch report processing (process multiple reports simultaneously)
- Codebase analysis and pattern detection
- Business logic extraction and surfacing
- Dependency mapping and visualization
- KPI lineage tracing (800+ KPIs)
- Consolidation detection (redundant reports)
- Documentation generation for legacy code
- Automated mapping with confidence scoring

#### Proposal Approach (Three Options Requested)
| Option | Description | Engagement Type |
|--------|-------------|------------------|
| **Option 1** | Small confidence-building pilot (Finance, Business Planning) | Limited scope, fixed price |
| **Option 2** | Co-delivery model (Sephora keeps architecture, BayOne supports) | T&M with caps, milestone-based |
| **Option 3** | Larger partnership (rotating specialists, flexibility) | Outcome-based components |

#### Proposed Pilot Track
- **Finance - Business Planning reports** (already nearly complete; can validate approach retrospectively)
- **Alternative:** Merchandising or Supply Chain (fresh tracks, prove value from beginning)

#### Competition / Positioning
- **Databricks** - At governance table; native AI tools being evaluated
- **Various partner accelerators** - Already evaluated by Sephora
- **BayOne differentiator:** Experience + methodology, not better AI technology
- **Key insight:** Mani wants **proposal-led conversations**, not discovery
- **Not locked into Databricks** AI tools (opportunity for BayOne to influence)
- **Integration valued:** Work with existing tools (Databricks, Lutra, Flow), not replacement

#### Current Tools in Use
- Databricks (platform, evaluating native AI tools)
- Lutra (AI/automation tool)
- Flow (AI/automation tool)
- Various partner accelerators (evaluated)

#### Timeline / Next Steps (As of Feb 2026)
1. Proposal due: ~Feb 28, 2026 (or soon after)
2. In-person proposal walk-through: Week after (Mani will attend)
3. Send case studies (Patter, Evaluator) to Mani immediately
4. Obtain sample reports from Gariashi (if available)
5. Define pilot scope recommendation (Finance vs. Merchandising vs. Supply Chain)
6. Confirm meeting dates for in-person proposal walk-through
7. Prepare for travel (Colin on-site)

#### Related Sephora Initiatives (Context Only - NOT BayOne Projects)
- **Reporting Democratization** - 2026 organizational shift from centralized reporting to embedded domain teams (Mani transitions from execution to governance/advisory)
- **Marketing AI Task Force** - Marketing-focused AI initiatives (journey orchestration, CRM personalization, influencer marketing, agentic AI exploration)
- **Semantic Layer Architecture** - Common semantic layer across all reporting tools (Andrew Ho and Terti co-leads; pragmatic approach, don't let it slow progress)

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani-transcript1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani_transcript2.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/andrew-girishi-meeting1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/00_project_overview.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/02_pain_points.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/project/03_scope_and_scale.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/deliverables/03_edw_acceleration_framework.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-05_big4_sephora_technical_deep_dive/source/04_technical_deep_dive_framework.md

---

### PROJECT 2: Staffing / Talent Acquisition Engagement

**Type:** Staffing / Managed services
**Status:** Active Hiring - Candidates in process

#### Description
Active staffing engagement across multiple hiring managers and domains to support EDW modernization and AI/ML initiatives. Two distinct skill buckets: (1) general full-stack developers, (2) AI-enabled developers. Multiple entry points across domain teams as Sephora transitions from centralized to decentralized reporting model (2026 organizational transformation).

#### Hiring Managers (Active)
1. **Ram Soundararajan** (VP, Acquisition & Retention) - Actively hiring; nearshore + offshore interest; two major 2026 projects
2. **Andrew Ho** (Sr. Director, Influencer/Media/Marketing AI) - Actively hiring; SOW discussions with BayOne
3. **Gariashi Chakraborty** (Director, Data Engineering/BI) - Actively hiring; some positions on hold temporarily
4. **Rizwan Khan** (Director, CRM & Personalization) - Q1 2026 late; ramping down currently

#### Hiring Across Peer Organizations
- **David/Natalia** (Stores) - Gariashi on interview panel
- **Rajesh** (E-commerce/Omni) - Engineers hired through Gariashi initially, then transition

#### Skill Requirements
1. **Full Stack** (general development)
2. **Full Stack + AI** (development with AI tooling/acceleration)
3. **Data Engineering + AI** (data processing with AI skills)
4. **Agentic AI** (emerging future need)

#### Technologies
Azure, Databricks, Python, Spark, MLOps, Machine Learning, Data Engineering, Full Stack Development, AI tooling integration

#### Rate Structure & Location Preferences
- **Nearshore US** (OK, KS, UT, Canada PST): ~$75-100/hr (preferred)
- **Bay Area in-office:** <$100/hr acceptable
- **$100-105/hr:** Borderline, prefer on-site
- **$105-115/hr:** Senior level acceptable (prefer on-site)
- **$120+/hr:** **Must be on-site only**
- **>$120/hr:** **Not acceptable** ("not going anymore")
- **India offshore:** Less preferred (concerns about "bodies vs. problem solvers," churn)

#### Engagement Models
- Standard FTE
- Part-time/flexible hours ("couple of hours" engagements)
- Rotation model (ability to rotate specialists by expertise)

#### Process
- Candidates go through Hacker Rank
- Interview panels include cross-functional participation
- Prefer quality talent commitment, no "double-dipping"
- Flexible engagement models (not all full-time wanted)

#### Team & Stakeholders
- **Sephora:** Multiple hiring managers (Ram, Andrew, Gariashi, Rizwan), Domain leaders (David, Natalia, Rajesh)
- **BayOne:** Neha Malhotra (Head of Recruiting - staffing lead), Zahra Syed (Director Strategic Accounts - relationship lead), Colin Moore (technical vetting)

#### Budget & Timeline
- **Rates:** $105-115/hr standard (prefer nearshore US at $75-100/hr)
- **Timeline:** Ongoing 2026+
- **Current pipeline:** Candidates in process with Gariashi
- **Past success:** Sithara placement to Alan (referenced as success story)

#### Key Distinction
This is a SEPARATE PROJECT from Project 1 (EDW Modernization Solutions Track):
- **Different ownership:** Staffing (Neha) vs. Solutions (Colin/Zahra)
- **Different accountability:** Staff augmentation vs. outcomes/deliverables
- **Different budgets:** Hourly rates vs. project-based
- **Multiple hiring managers:** Ram, Andrew, Gariashi, Rizwan (not just Mani)

#### Organizational Context (2026 Transformation)
Sephora is testing three operating models for reporting decentralization:
- **Model 1 (Stores):** David/Natalia own delivery, Mani provides SME oversight (~1 year to stabilize)
- **Model 2 (E-commerce/Omni):** Rajesh owns, Gariashi hires initially, engineers transition by June/July 2026
- **Model 3 (Supply Chain/Merchandising):** Stays centralized under Gariashi (legacy tech prevents immediate decentralization)

**Implication:** Multiple entry points for BayOne across domain teams; different teams at different maturity levels; coordination complexity increases; opportunity for standardization and framework development

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/mani-transcript1.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/08_staffing_details.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/05_budget_rates_financials.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/2025-02-25_andrew-meeting-prep/topics/02_organizational_map.md

---

### PROJECT 3: ML Production Initiatives (Ravi's Team)

**Type:** Machine learning / Production AI systems
**Status:** Active Production + Hiring for Infrastructure

#### Description
Four active production ML initiatives driving customer experience: (1) Generative AI for product discovery, (2) Personalized in-session recommendation engine (in-store and online), (3) Customer segmentation, (4) Next-best offer prediction. Requires ML data infrastructure build-out to support these production systems at scale.

#### Four Active Production Systems

**1. Generative AI Product Discovery**
- Description: Generative AI use cases helping customers discover products
- Technologies: LLMs, LLMOps, Azure ML, Python
- Status: In action (active production)

**2. Personalized In-Session Product Recommendation Engine**
- Description: Personalized recommendation engine for both in-store and online experiences
- Technologies: PyTorch/TensorFlow/Keras, Azure ML, MLOps, feature stores, batch and real-time ML systems
- Status: In action (active production)
- Impact: Production ML system driving customer experience

**3. Customer Segmentation**
- Description: ML-driven customer segmentation initiative
- Technologies: ML model development, Azure ML, Databricks
- Status: In action (active production)

**4. Next-Best Offer Prediction**
- Description: Predictive modeling for next-best offer recommendations
- Technologies: ML models, A/B testing, MLOps
- Status: In action (active production)
- Impact: Revenue optimization initiative

#### ML Data Infrastructure (Supporting Initiative)
- Description: Building data pipelines, ETL processes, and infrastructure powering production ML systems
- Technologies: Azure, Spark, Kafka, Hadoop, Databricks, SQL/NoSQL databases, feature stores, Docker
- Status: Build-out in progress, hiring for capacity

#### Team & Stakeholders
- **Sephora:**
  - Ravi (Hiring Manager, ML team lead)
  - Product teams
  - Engineering teams
  - Data Scientists
  - Business teams
- **BayOne:**
  - Hiring: Data Engineer, ML Engineer, ML Platform Engineer, AI Engineer roles

#### Technologies
- **ML Stack:** PyTorch, TensorFlow, Keras, Azure ML, MLOps, feature stores, batch ML systems, real-time ML systems, A/B testing
- **Data Infrastructure:** Azure, Spark, Kafka, Hadoop, Databricks, SQL databases, NoSQL databases, Docker
- **AI Tools:** LLMs, LLMOps, Azure AI, Python

#### Budget & Timeline
- **Budget:** Not disclosed
- **Timeline:** Ongoing 2026+
- **Status:** Active production systems, hiring to expand team capacity
- **Hiring:** Active recruitment for multiple roles

#### Key Distinction
This is DISTINCT from Project 1 (EDW Modernization):
- **Different team:** Ravi vs. Mani/Andrew/Gariashi
- **Different focus:** ML production systems vs. data warehouse re-engineering
- **Different domain:** Real-time customer-facing ML vs. batch reporting/analytics
- **Connection:** Both fall under Sephora's broader data & AI transformation

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/ravi-ml-jd.txt
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ml_engineer/jd_ml_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/data_engineer/jd_data_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ml_platform_engineer/jd_ml_platform_engineer_sephora.md

---

### PROJECT 4: AI-Assisted Development Tooling Initiative

**Type:** Engineering productivity / Developer tooling
**Status:** Pre-Implementation (Hiring Stage)

#### Description
Building AI-powered automation for engineering/QA/QE teams, developing Claude Code skills and agents, introducing new AI tools and workflows to accelerate development velocity. High-visibility engagement to transform how Sephora's engineering teams work with AI tooling.

#### Scope
- AI-powered automation development
- Claude Code skills and agents creation
- New AI tools introduction
- Workflow transformation for engineering/QA/QE teams
- Accelerate development velocity across organization

#### Technologies
- Claude Code
- Cursor
- Windsurf
- Python
- Claude Agent SDK
- LangChain
- LangGraph
- AI-powered automation frameworks

#### Team & Stakeholders
- **Sephora:**
  - Engineering teams (target users)
  - QA teams (target users)
  - QE teams (target users)
- **BayOne:**
  - Hiring: AI Engineer role to lead implementation
  - Colin Moore (oversight)

#### Budget & Timeline
- **Budget:** Not disclosed
- **Timeline:** Immediate start required (active hiring)
- **Status:** Pre-implementation, hiring stage

#### Key Distinction
Distinct initiative focused on engineering productivity and tooling, separate from:
- **Project 1:** EDW modernization (different domain)
- **Project 3:** ML production systems (different domain)
- **Focus:** Internal developer experience and velocity, not customer-facing or data engineering

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/sephora/ravi/job_descriptions/ai_engineer/jd_ai_engineer_sephora.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-26_sephora-hiring/

---

### PROJECT 5: EDW Modernization POC/Demo Projects

**Type:** Proof-of-concept / Pre-sales demonstrations
**Status:** Materials Gathering Phase (ETL received, Cognos pending)

#### Description
Three interconnected proof-of-concept demonstrations to validate AI-driven agent orchestration capabilities before larger EDW engagement commitment. Designed to prove BayOne's ability to automate complex migration workflows that Sephora cannot do internally (they already do code translation; want to see coordination/orchestration).

#### Three Demo Tracks

**Track A: Cognos MCP Demo**
- Description: Build MCP connector and agent orchestration for Cognos report conversion demonstration
- Workflow: Multi-agent system extracts report from Cognos, parses structure, interprets SQL, converts syntax, remaps to Databricks schema, generates output
- Technologies: MCP server, Cognos SDK, Content Store, agent orchestration, multiple specialized agents, XML parsing, SQL transformation
- Status: Scoped in Meeting 4, awaiting Cognos report XML and Databricks schema from Sephora

**Track B: DataStage YAML Configuration Demo**
- Description: Build agents to parse DataStage job XML, interpret SQL logic, generate YAML configuration files that work with Sephora's existing AggregationApplication Databricks framework (NOT new Scala code - specific YAML requirement from Sergey)
- Technologies: DataStage XML parsing, stored procedure analysis, YAML generation, existing Databricks framework integration
- Status: Agreed in Meeting 4 as optional additional demo scope; materials received

**Track C: Enhanced Agent Orchestration Demo (Revised Scope)**
- Description: Malika's email significantly expanded demo scope beyond Meeting 4 - demonstrate end-to-end workflow automation, how agents manage tool communication, task sequencing, and dependency handling
- Requirements: MCP server for Cognos, automated extraction of report metadata, agent orchestration across multiple tools
- Technologies: MCP integration, multi-agent orchestration, automated extraction, Spark SQL/Scala generation, YAML configs, deployment artifacts
- Context: Sephora already does code translation internally; wants to see coordination/orchestration capabilities they can't do
- Status: Requirements expanded post-Meeting 4 via email

#### Team & Stakeholders
- **Sephora:**
  - Mani Soundararajan (VP - decision maker)
  - Andrew Ho (Sr. Director - internal champion, technical evaluation)
  - Gariashi Chakraborty (Director - technical gatekeeper, will evaluate feasibility)
  - Maher Burhan (Enterprise Architect - practical solutions focus)
  - Sergey Shtypuliak (SME IBM Tools - specified YAML output requirement for DataStage)
  - Malika (email correspondent - expanded scope requirements)
- **BayOne:**
  - Colin Moore (Director of AI - solo for POC)
  - Zahra Syed (relationship)
  - Neha Malhotra (internal coordination)

#### Technologies
- **Cognos Track:** MCP server, Cognos SDK (Integration Layer, Content Store, Dispatcher), XML parsing, SQL transformation, Databricks schema mapping, multi-agent orchestration
- **DataStage Track:** DataStage XML parsing (dsjob/dsexport CLI), stored procedure analysis, YAML generation, existing Databricks framework integration (AggregationApplication)
- **Overall Orchestration:** Agent coordination, automated extraction, tool communication, task sequencing, dependency handling, end-to-end workflow automation

#### Budget & Timeline
- **Budget:** Proof-of-concept scope (investment in sales process, not charged to Sephora)
- **Timeline:** Demo session after materials received
  - ETL materials: Received
  - Cognos materials: Pending
- **Status:** Scoped in Meeting 4 (early March 2026), expanded via Malika's email, demo session TBD

#### Key Purpose
These are PRE-SALES demonstrations to prove capability before Project 1 (EDW Modernization) solutions engagement. Success of POC determines:
1. Sephora's confidence in BayOne's agent orchestration approach
2. Paid engagement scope and budget
3. Which proposal option (1, 2, or 3) Sephora selects

#### Source Files
- /home/cmoore/programming/cisco_projects/cicd/sephora/context/meeting4-technical-deep-dive.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/01_meeting_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/scoping/track_a_cognos_mcp_demo.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/scoping/track_b_etl_datastage_demo.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/research/06_malika_email_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/research/09_complete_materials_inventory.md

---

## RESEARCH METHODOLOGY

This catalog was created using a rigorous file-by-file reading methodology developed specifically for this engagement. Key principles:

1. **Read Everything First** - Complete file-by-file reading, no keyword search
2. **Understand Hierarchy** - Client → Projects → Work Streams
3. **Make It Auditable** - Always cite source files
4. **Separate Discovery from Synthesis** - Find everything, then organize
5. **Parallel Exploration** - 3 Explorer agents reading files concurrently
6. **No Search-Based Discovery** - Can't find what you don't know to search for

**Files Reviewed:**
- **Cisco:** 62 files (meeting summaries, core documents, UI conversion, SOW)
- **Sephora:** 89 files (sephora/ folder + 3 Claude session folders)
- **Total:** 151 files

**Methodology Documentation:**
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/planning/01_methodology_lessons_learned.md`

---

## DOCUMENT INDEX

### Research Outputs
1. **Cisco Projects (Corrected):** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/research/04_cisco_projects_corrected.md`
2. **Sephora Projects (Corrected):** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/research/05_sephora_projects_corrected.md`
3. **Initial Phase 1 Summary:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/progress/00_phase1_summary.md`

### Planning & Methodology
1. **Execution Plan:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/planning/00_execution_plan.md`
2. **Methodology Lessons Learned:** `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/planning/01_methodology_lessons_learned.md`

### Session Folder
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/`

---

**End of Internal Catalog**
**Last Updated:** 2026-03-17
**Status:** Cisco and Sephora Complete; Tailored Brands and Zeblok Pending
