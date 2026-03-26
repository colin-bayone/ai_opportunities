# Sephora Work Streams - Explorer Agent Findings

**Agent:** Sephora Explorer
**Date:** 2026-03-17
**Folders Scanned:** sephora/, sephora-related claude sessions

---

## SEPHORA WORK STREAMS CATALOG - COMPREHENSIVE EXPLORATION REPORT

Based on a very thorough exploration of `/home/cmoore/programming/cisco_projects/cicd/sephora/` and related Claude session folders, here is the complete catalog of Sephora work streams and initiatives:

---

### WORK STREAM 1: EDW MODERNIZATION (Primary Initiative)

**Description/Objective:**
Three-year enterprise data warehouse (EDW) re-engineering program to migrate from legacy SQL Server / IBM Cognos / IBM DataStage environment to Databricks lakehouse architecture. This is not a simple "lift and shift" migration but a complete re-engineering and re-architecting of data pipelines and reporting assets.

**Status:** In Progress (Started 2025, Active)

**Timeline:**
- Program duration: 2026-2028 (3 years planned)
- Target acceleration: Complete by 2027 or early 2028 (if AI-accelerated)
- Finance track: Nearly complete (~20-24 days remaining as of Feb 2026)

**Key Deliverables:**
- Report re-engineering: 6,000+ Cognos reports migrated and modernized
- SSAS Cube transition: 8 cubes → Databricks equivalent (major blocker)
- ETL pipeline conversion: Thousands of DataStage jobs → Databricks pipelines
- Semantic layer establishment: Unified data definitions across all BI tools
- Schema mapping: SQL Server EDW → Databricks (non-1:1 transformation)

**Technical Paths/Components:**
- Legacy stack: SQL Server (EDW), IBM Cognos (reporting), IBM DataStage (ETL), SSAS Cubes (OLAP)
- Target stack: Databricks (lakehouse), Tableau (future BI), ThoughtSpot (future BI), Azure cloud
- Current front-end: Cognos retained during transition (change management consideration)
- Semantic layer owners: Andrew Ho and Terti (co-leads)

**Scope Scale:**
- 6,000+ Cognos reports (15-20 years of accumulated logic)
- 8 SSAS cubes
- 800+ KPIs
- 300 dimensions
- 20+ source systems feeding the EDW
- ~20 years of legacy codebase
- Batch processing only (no real-time currently)

**Stakeholders:**
- **Mani Soundararajan** - VP, Executive sponsor, decision-maker (reports to Vlad, CIO)
- **Andrew Ho** - Sr. Director, Influencer/Media/Marketing AI; part of governance table; semantic layer co-owner (reports to Mani)
- **Grishi Chakraborty** - Director, Data Engineering/BI; execution lead (reports to Andrew)
- **Terti** - Semantic layer co-lead (with Andrew)
- **Databricks** - Platform partner at governance table
- **Microsoft** - Cloud platform (Azure at governance table)

**Known Pain Points / AI Opportunities:**
1. **SSAS Cube migration blocker** - Not technical (connector exists via ODBC/JDBC), but change management issue
2. **Report-by-report migration too slow** - Batch processing, pattern detection needed
3. **Embedded SQL complexity** - Queries buried in Cognos reports, business logic extraction needed
4. **Data mapping is slowest phase** - Manual validation creates bottleneck
5. **Tribal knowledge loss risk** - 20 years of logic undocumented
6. **SME bandwidth constraint** - Same experts need to keep production running AND validate migration

**AI Acceleration Needs (Explicitly Stated by Mani):**
- Batch report processing (process multiple reports simultaneously)
- Codebase analysis and pattern detection
- Business logic extraction and surfacing
- Dependency mapping and visualization
- KPI lineage tracing
- Consolidation detection (redundant reports)
- Documentation generation for legacy code
- Automated mapping with confidence scoring

**Tools Currently in Use:**
- Databricks (platform, evaluating native AI tools)
- Lutra (AI/automation tool)
- Flow (AI/automation tool)
- Various partner accelerators (evaluated)

**Budget/Rates:**
- Staffing rates: $105-115/hr max (on-site preferred); $120+/hr only if on-site; >$120/hr not acceptable
- Solutions budget: Unknown (to be clarified in proposal)
- Proposal format: 3 options with cost ranges
- Location preference: Nearshore US (Oklahoma, Kansas, Utah at ~$75/hr); on-site SF acceptable

**Notes/Context:**
- Mani wants **proposal-led conversations**, not discovery
- **Not locked into Databricks** AI tools - still experimenting (opportunity for BayOne to influence)
- Pragmatic approach valued ("If semantic layer slows us down, skip it")
- Colin's Snowflake and BI migration experience directly relevant
- Integration with existing tools, not replacement, valued

---

### WORK STREAM 2: REPORTING DECENTRALIZATION (Organizational Restructuring)

**Description/Objective:**
Major 2026 organizational shift from centralized reporting under Mani's team to distributed domain-based operating models. Mani's team transitions from execution to lean governance/SME advisory role.

**Status:** In Progress / Planned (2026 onward)

**Key Operating Models Being Tested:**

| Model | Domain | Status | Lead | Timeline | Notes |
|-------|--------|--------|------|----------|-------|
| **Model 1** | Stores | In delivery | David/Natalia | ~1 year to stabilize | Delivery owned by Stores; Mani provides SME oversight |
| **Model 2** | E-commerce/Omni | Hiring in progress | Rajesh | May complete by June/July 2026 | Engineers hired through Grishi initially |
| **Model 3** | Supply Chain/Merchandising | Still centralized | Grishi (under Andrew) | Transitions later | Legacy tech prevents immediate decentralization |

**Stakeholders:**
- **Mani Soundararajan** - Transitioning from execution to governance/advisory
- **David/Natalia** - Stores domain leadership
- **Rajesh** - E-commerce/Omni leadership
- **Grishi Chakraborty** - Continuing on Supply Chain/Merchandising (Model 3)
- **Andrew Ho** - Oversee decentralization strategy

**Implications:**
- Multiple entry points for BayOne across domain teams
- Different teams at different maturity levels
- Coordination complexity increases
- Opportunity for standardization and framework development

---

### WORK STREAM 3: STAFFING/TALENT ACQUISITION (Ongoing)

**Description/Objective:**
Active hiring across multiple domains to support EDW modernization and AI/ML initiatives. Two distinct skill buckets: general full-stack developers and AI-enabled developers.

**Status:** Active Hiring (Ongoing)

**Active Hiring Managers:**
- **Ram Soundararajan** - Acquisition & Retention (actively hiring; nearshore + offshore interest)
- **Andrew Ho** - Influencer/Media/Marketing AI (actively hiring; SOW discussions with BayOne)
- **Grishi Chakraborty** - Data Engineering/BI (actively hiring; some positions on hold temporarily)
- **Rizwan Khan** - CRM & Personalization (Q1 2026 late; ramping down currently)

**Hiring Across Peer Organizations:**
- **David/Natalia** (Stores) - Grishi on interview panel
- **Rajesh** (E-commerce) - Engineers hired through Grishi initially, then transitions

**Skill Requirements:**
1. Full Stack (general development)
2. Full Stack + AI (development with AI tooling/acceleration)
3. Data Engineering + AI (data processing with AI skills)
4. Agentic AI (emerging future need)

**Rate Structure:**
- Nearshore US (OK, KS, UT, Canada PST): ~$75-100/hr (preferred)
- Bay Area in-office: <$100/hr seen acceptable
- $100-105/hr: Borderline, prefer on-site
- $105-115/hr: Senior level acceptable (prefer on-site)
- $120+/hr: **Must be on-site only**
- >$120/hr: **Not acceptable** ("not going anymore")

**Location Preferences:**
- Emerging nearshore talent hubs: Oklahoma, Kansas City, Utah
- San Francisco on-site (up to $120/hr)
- Canada PST (nearshore rates)
- India: Less preferred (concerns about "bodies vs. problem solvers," churn)

**Process:**
- Candidates go through Hacker Rank
- Interview panels include cross-functional participation
- Prefer quality talent commitment, no "double-dipping"
- Flexible engagement models (not all full-time wanted)

**Engagement Models:**
- Standard FTE
- Part-time/flexible hours ("couple of hours" engagements)
- Rotation model (ability to rotate specialists by expertise)

**Stakeholders:**
- **Mani Soundararajan** - Budget holder, hiring strategy owner
- Hiring managers (Ram, Andrew, Grishi, Rizwan)
- **Neha Malhotra** - BayOne Head of Recruiting (staffing lead)
- **Zahra Syed** - BayOne Director Strategic Accounts (relationship lead)

**Budget:**
- Rate pressure real across organization
- Prefer nearshore US for best talent/rate balance
- No India offshore unless absolutely necessary

**Notes/Context:**
- Past success: Sithara placement to Alan (referenced as success story)
- Current BayOne pipeline: Candidates in process with Grishi
- Multiple hiring managers = multiple entry points
- Staffing track separate from solutions track (different accountability)

---

### WORK STREAM 4: AI ACCELERATION & MODERNIZATION SOLUTIONS

**Description/Objective:**
Strategic partnership track for AI-assisted tooling and consulting to accelerate the EDW modernization program. This is distinct from staffing and involves methodology, tools, and implementation strategy.

**Status:** In Planning / Early Development (Proposal stage)

**Key Focus Areas (AI Acceleration Capabilities):**

| Capability | Description | Status | Potential Impact |
|------------|-------------|--------|------------------|
| **Report Similarity Clustering** | Analyze Cognos metadata to group similar reports for batch processing | Proposed | Very High |
| **Business Logic Extraction** | Parse reports/SQL to extract calculations, filters, business rules | Proposed | High |
| **Dependency Mapping** | Trace relationships between tables, views, reports, cubes | Proposed | High |
| **KPI Lineage Tracing** | Map 800+ KPIs to source calculations | Proposed | High |
| **Schema Mapping Validation** | Automate source-to-target column mapping with confidence scoring | Proposed | High |
| **Change Impact Analysis** | Simulate downstream effects before changes | Proposed | Medium |
| **Documentation Generation** | Generate docs for undocumented stored procedures, jobs | Proposed | Medium-High |
| **Consolidation Detection** | Identify redundant reports for elimination | Proposed | Medium |

**Technical Approach (Proposed):**
- Agent-assisted orchestration (not just generative AI)
- Hybrid deterministic + AI methodology
- Cognos SDK integration for programmatic report extraction
- DataStage dsjob/dsexport CLI integration
- Schema mapping with confidence-based routing
- Persistent knowledge graph across tracks
- Proof-of-concept approach first, then scale

**Implementation Model (Proposed Options):**

| Option | Description | Engagement Type |
|--------|-------------|------------------|
| **Option 1** | Small confidence-building pilot (Finance, Business Planning) | Limited scope, fixed price |
| **Option 2** | Co-delivery model (Sephora keeps architecture, BayOne supports) | T&M with caps, milestone-based |
| **Option 3** | Larger partnership (rotating specialists, flexibility) | Outcome-based components |

**Proposed Pilot Track:**
- **Finance - Business Planning reports** (already nearly complete; can validate approach)
- Alternative: Merchandising or Supply Chain (fresh tracks, prove value from beginning)

**Current State:**
- Finance track in progress (~20-24 days remaining)
- Established architectural patterns and methodology
- Already achieved ~30% efficiency gains with Claude for SQL transformation
- Current workflow manual; aspiration is orchestrated agent workflow

**Stakeholders:**
- **Mani Soundararajan** - Decision-maker, budget holder
- **Andrew Ho** - Governance table input, semantic layer perspective
- **Grishi Chakraborty** - Execution feasibility, technical requirements
- **Colin Moore** - BayOne technical lead (Director of AI)
- **Zahra Syed** - BayOne sales/relationship lead
- **Neha Malhotra** - BayOne internal coordination

**Budget/Investment:**
- Staffing rates: $105-115/hr standard, $120+ only on-site
- Solutions budget: Unknown (Mani asked "What kind of investment?")
- Proposal must include cost ranges and assumptions
- ROI framing: Time saved, efficiency gains, acceleration value

**Competition:**
- Databricks (at governance table; native AI tools being evaluated)
- Various partner accelerators (already evaluated)
- BayOne differentiator: Experience + methodology, not better AI technology

**Timeline:**
- Proposal due: ~Feb 28, 2026 (or soon after)
- In-person proposal walk-through: Week after (Mani will attend)
- Pilot execution: Contingent on proposal approval
- Expanded engagement: Contingent on pilot success

**Notes/Context:**
- Mani: "If someone comes with groundwork done and a proposal — that would be very productive"
- Not locked into Databricks AI tools (opportunity for influence)
- Wants integration with, not replacement of, existing tools (Databricks, Lutra, Flow)
- Pragmatic approach valued; AI hype not wanted
- Evidence valued: case studies, proof points, relevant experience

---

### WORK STREAM 5: MARKETING AI INITIATIVES (Parallel but Related)

**Description/Objective:**
Broader marketing and personalization AI task force running in parallel with EDW modernization. Includes generative AI use cases, personalization, customer segmentation, and next-best-offer prediction.

**Status:** Active / In Development

**Key Initiatives:**
- Generative AI use cases for customer product discovery
- Personalized in-session product recommendation engine (in-store and online)
- Customer segmentation
- Next-best-offer prediction
- Agentic AI exploration
- Journey orchestration

**Stakeholders:**
- **Mani Soundararajan** - Oversees marketing tech and AI strategy
- **Andrew Ho** - Sr. Director, Influencer/Media/Marketing AI
- **Marketing AI task force** - Cross-functional team

**Connection to EDW Modernization:**
- EDW and data platform support these marketing AI initiatives
- Shared infrastructure needs
- Skills overlap (data engineering + AI)

**Notes/Context:**
- Sephora positioned similarly to BayOne with enterprise AI task force
- Agentic AI flagged as new required skill set
- EDW modernization AI should not create silos; should connect to broader strategy

---

### ADDITIONAL CONTEXT: ENGAGEMENT HISTORY & TIMELINE

**Key Engagement Milestones:**

| Date | Event | Participants | Outcome |
|------|-------|-------------|---------|
| Dec 11, 2025 | Initial opportunity intro | Zahra → Colin | Opportunity identified |
| Dec 14, 2025 | Colin's initial analysis | Colin → Zahra | Strong interest, noted Coherent experience |
| Jan 28, 2026 | Technical deep dive | Neha ↔ Grishi | Detailed scope received |
| Jan 30, 2026 | Strategic analysis | Colin → Neha | Key questions raised |
| Feb 4, 2026 | Two-track confirmation | Neha → Colin | Staffing + solutions both active |
| Feb (recent) | Zahra roadmap conversation | Zahra ↔ Mani | Critical: decentralization, proposal approach, not locked in |
| Feb 12, 2026 | VP meeting + engineer lunch | Colin ↔ Mani; Colin ↔ Ravi | Proposal-led conversation, ground truth gathering |

**Engagement Phases:**
- Phase 1: Discovery & Positioning (Nearing completion as of Feb 2026)
- Phase 2: Proposal Development (Starting; due ~Feb 28)
- Phase 3: Engagement (Target; pilot + expansion contingent on success)

---

### KEY STAKEHOLDERS SUMMARY

| Name | Title | Role | Reports To | Active? |
|------|-------|------|-----------|---------|
| **Mani Soundararajan** | VP, Marketing Tech/Personalization/Data-AI/Reporting | Executive sponsor, decision-maker | Vlad (CIO) | Yes |
| **Andrew Ho** | Sr. Director, Influencer/Media/Marketing AI | Governance table; semantic layer co-lead | Mani | Yes |
| **Grishi Chakraborty** | Director, Data Engineering/BI | Execution lead; hiring manager | Andrew | Yes |
| **Ram Soundararajan** | VP, Acquisition & Retention | Hiring manager | Mani | Yes |
| **Rizwan Khan** | CRM & Personalization | Hiring manager (Q1 2026) | Mani | Q1 2026 |
| **Terti** | (Title unknown) | Semantic layer co-lead | (Unknown) | Yes |
| **David/Natalia** | Domain leadership | Stores team leads | (Unknown) | Yes |
| **Rajesh** | Domain leadership | E-commerce/Omni lead | (Unknown) | Yes |
| **Ravi** | Engineer | Engineer (technical credibility check) | (Unknown) | Yes |
| **Vlad** | CIO | Executive sponsor (above Mani) | (Unknown) | Yes |

**BayOne Team:**
- **Colin Moore** - Director of AI (technical lead, meeting with Mani)
- **Zahra Syed** - Director, Strategic Accounts (sales/relationship lead)
- **Neha Malhotra** - Head of Recruiting (staffing coordination)

---

### OPEN QUESTIONS & NEXT STEPS

**Critical Questions to Answer:**
1. What AI POCs have Sephora already attempted?
2. What exactly is Databricks proposing for AI acceleration?
3. What is the solutions engagement budget authority/threshold?
4. Can sample Cognos reports be obtained for proposal refinement?
5. What success criteria would Grishi/Andrew use for pilot evaluation?
6. What is Databricks' positioning on the semantic layer?
7. Timeline pressure - any hard deadline for first phase?

**Action Items (As of Feb 2026):**
1. Send case studies (Patter, Evaluator) to Mani immediately
2. Develop 3-option proposal with cost ranges and assumptions
3. Obtain sample reports from Grishi (if available)
4. Define pilot scope recommendation (Finance vs. Merchandising vs. Supply Chain)
5. Follow-up with Ram on staffing (Zahra assigned)
6. Re-engage Andrew on SOW (solutions track)
7. Confirm meeting dates for in-person proposal walk-through
8. Prepare for travel (Colin on-site)

**Proposal Checklist:**
- [ ] Three clearly defined options
- [ ] Cost ranges for each
- [ ] Explicit assumptions stated
- [ ] Pilot track recommendations (2-3 options)
- [ ] Integration approach with existing tools explained
- [ ] Flexibility model described
- [ ] Differentiation from Databricks clear
- [ ] Case studies included/referenced
- [ ] Staffing track separation acknowledged

---

### DOCUMENT LOCATIONS

All documentation located in: `/home/cmoore/programming/cisco_projects/cicd/sephora/`

Key folders:
- `/project/` - Current state documents
- `/planning/` - Strategy and approach
- `/stakeholders/` - People directory
- `/context/` - Source materials (emails, transcripts)
- `/2025-02-25_andrew-meeting-prep/` - Meeting prep materials (33 files)
- `/ravi/` - Job descriptions for hiring
- `/sephora/2025-02-25_andrew-meeting-prep/` - Detailed topic files

Related Claude session folders:
- `/claude/2026-03-05_big4_sephora_technical_deep_dive/` - Technical deep dive framework
- `/claude/2026-02-26_sephora-hiring/` - Hiring coordination session
- `/claude/meeting-analyzer/meeting_sephora_technical_deep_dive_2026-03/` - Meeting analysis

---

This comprehensive catalog represents very thorough exploration of 89 markdown and text files across the Sephora engagement documentation, capturing active work streams, deliverables, stakeholders, technical focus areas, and strategic context for BayOne's engagement.
