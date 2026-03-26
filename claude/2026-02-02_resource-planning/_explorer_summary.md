# Session Summary: 2026-02-02_resource-planning

## Client/Opportunity
**Cisco Systems** - NX-OS CI/CD Pipeline Improvement Initiative

This is a year-long consulting engagement between BayOne Solutions (minority-owned technology and talent solutions company) and Cisco to improve their CI/CD pipeline and developer productivity.

## Purpose
Resource planning and job description creation for a multi-quarter consulting engagement to address six key capability areas in Cisco's NX-OS development pipeline: Developer Box visibility, AI-driven failure diagnosis, unified pipeline interface, coverage tracking, self-healing/automated corrections, and branch health dashboards.

The session was specifically focused on creating resource plans, team structure recommendations, quarterly phasing, role definitions, and job descriptions for hiring.

## Files

### Planning Documents (planning/)
- `00_approach.md` - Overview of deliverable requirements, team structure, and document structure (4 sections: executive summary, team structure, job descriptions, quarterly phasing)
- `01_team_structure_draft.md` - OUTDATED - Initial brainstorming on roles (Senior Engineer, Backend Engineer, Frontend, AI/ML, Agentic AI Specialist)
- `02_quarterly_phasing_draft.md` - OUTDATED - Initial Q1-Q4 phasing breakdown with team composition by phase
- `03_q1_deliverables.md` - Q1 focus: Discovery phase + Item A (Developer Box) + Item F (Branch Health) with detailed requirements and milestones
- `04_q2_deliverables.md` - Q2 focus: Item C (Unified Interface) requiring integrations with CAT, DevX, Jenkins, Airflow, Grafana, GitHub
- `05_q3_deliverables.md` - Q3 focus: Item B (AI Diagnosis of gate failures) + Item D (Coverage Tracking)
- `06_q4_deliverables.md` - Q4 focus: Item E (Self-Healing/Autonomous Actions) with extensive governance framework discussion
- `07_resource_loading_summary.md` - Team roster by quarter with rates and cost breakdowns (all quarters under $100K/quarter budget)
- `handoff_to_next_session.md` - Detailed context handoff for follow-up work including project background, team structure changes, and next steps

### Role Planning Documents (planning/roles/)
- `01_senior_engineer_onshore.md` - Senior Engineer (Bay Area, on-site at Cisco) - technical leader, client interface, day-to-day team guidance
- `02_backend_integration_engineer.md` - Backend/Integration Engineer (Offshore) - data pipelines, API integrations, Airflow expertise (non-negotiable)
- `03_ui_application_developer.md` - UI/Application Developer (Offshore) - dashboards, chat interface, full-stack (React + Python)
- `04_ai_engineer.md` - AI Engineer (Offshore) - generative AI, NLP, LangChain/LangGraph, production AI features
- `05_agentic_ai_specialist.md` - Agentic AI Specialist (Offshore, Q2 start) - autonomous systems, governance frameworks, safety mechanisms

### Research Documents (research/)
- `00_rates_and_constraints.md` - Budget ($100K/quarter), rates ($12-16K offshore, $45-50K onshore), staffing model (1-1.5 FTE onshore + 4-5 offshore)
- `01_technical_stack.md` - Cisco's existing stack (Airflow, Jenkins, CAT, Grafana, pyATS, on-prem) and tech preferences for hiring (Airflow required, LangChain/LangGraph for AI, FastAPI, React or Django)
- `02_cost_estimates.md` - Quarterly billing rates and year-total cost projection ($370K under $100K/quarter budget by $30K)

### Decision Documents (decisions/)
- `00_open_questions.md` - Three open questions: Infrastructure ownership (Cisco vs BayOne), Agentic AI Specialist timing, and DevOps expertise allocation

### Source/Context (source/)
- `cisco-questions-for-clarification.md` - 31 discovery questions for Cisco covering general/cross-cutting, unified data layer, developer box instrumentation, AI diagnosis, coverage tracking, self-healing governance, branch health, AI infrastructure, and process requests

### Deliverables (deliverables/)

#### Main Planning Documents
- `resource_plan_for_rahul.md` - Markdown version of main deliverable for President (markdown format)
- `resource_plan_for_cisco.html` - HTML version of main deliverable for Cisco client-facing presentation (styled with BayOne design: Inter font, purple gradients, numbered sections)

#### Job Descriptions - Markdown Versions
- `jd_senior_engineer.md` - Senior Solutions Engineer (Onshore)
- `jd_backend_integration_engineer.md` - Backend/Integration Engineer
- `jd_devops_infrastructure_engineer.md` - DevOps/Infrastructure Engineer (newly added)
- `jd_ai_engineer.md` - AI Engineer
- `jd_ui_application_developer.md` - UI/Application Developer
- `jd_agentic_ai_specialist.md` - Agentic AI Specialist
- `jd_senior_ai_solutions_engineer.md` - Senior AI Solutions Engineer

#### Job Descriptions - HTML Versions
- `jd_senior_engineer.html` - Styled HTML version
- `jd_backend_integration_engineer.html` - Styled HTML version
- `jd_devops_infrastructure_engineer.html` - Styled HTML version
- `jd_ai_engineer.html` - Styled HTML version
- `jd_ui_application_developer.html` - Styled HTML version
- `jd_agentic_ai_specialist.html` - Styled HTML version
- `jd_senior_ai_solutions_engineer.html` - Styled HTML version

#### Job Description Variations for Specific Needs
- `jd_ai_engineer_sephora.md` - AI Engineer job description customized for Sephora context
- `jd_ai_engineer_sephora.html` - HTML version for Sephora
- `jd_ai_engineer_offshore.md` - AI Engineer offshore variant
- `jd_ai_engineer_offshore.html` - HTML version

#### Recruiter Guides (deliverables/job_descriptions/recruiter_guides/)
- `recruiter_guide_senior_ai_solutions_engineer.html` - Detailed recruiter guidance for sourcing this role
- `recruiter_guide_ai_engineer.html` - Recruiter guide for AI Engineer
- `recruiter_guide_agentic_ai_engineer.html` - Recruiter guide for Agentic AI Engineer
- `recruiter_guide_automation_engineer.html` - Recruiter guide for Automation Engineer

#### Job Posting Variations (deliverables/job_descriptions/postings/)
- `jd_senior_ai_solutions_engineer.html` - Public-facing job posting
- `jd_ai_engineer_market_research_2026.md` - Market research on AI Engineer salaries and competition (40K lines)
- `jd_ai_engineer_sephora.html` - Public posting variant for Sephora
- `jd_agentic_ai_engineer.html` - Public posting for Agentic AI Engineer
- `jd_automation_engineer.html` - Public posting for Automation Engineer
- `jd_ai_engineer_offshore.html` - Public posting for offshore AI Engineer role

#### Supporting Artifacts
- `team_section_mockup.html` - HTML mockup of team section for presentations
- `resource_plan_for_cisco.html` - Main client-facing deliverable (HTML)
- `mockup_screenshot.png` (250K) - Screenshot of team/resource mockup
- `org_chart_screenshot.png` (11K) - Organizational chart visualization
- `screenshot.py` - Python script for generating screenshots
- `bad2.pdf` (3.2M) - PDF asset or reference document

## Key Deliverables

1. **Resource Plan Document** - Comprehensive plan for Cisco and Rahul covering team structure, quarterly roadmap, investment summary, and next steps

2. **Job Descriptions** - 7+ role definitions in both markdown and HTML formats:
   - Senior Engineer (Onshore)
   - Backend/Integration Engineer (Offshore)
   - DevOps/Infrastructure Engineer (Offshore)
   - AI Engineer (Offshore)
   - UI/Application Developer (Offshore)
   - Agentic AI Specialist (Offshore)
   - Senior AI Solutions Engineer

3. **Quarterly Phasing Plan** - Four quarters of detailed deliverables with dependencies:
   - Q1: Discovery + Developer Box + Branch Health
   - Q2: Unified Interface with chat capability
   - Q3: AI Diagnosis + Coverage Tracking
   - Q4: Self-Healing / Autonomous Actions

4. **Team Structure & Resource Loading** - 5-person team composition with start dates and cost projections, all under budget

5. **Role Planning Documents** - Detailed documentation for each role including responsibilities, skills, timing, and success criteria

6. **Recruiter Guides** - Hiring guidance for specialized roles (AI Engineer, Agentic AI Specialist, etc.)

7. **Technical Stack Documentation** - Cisco's existing infrastructure (Airflow, Jenkins, on-prem) and preferred technologies for implementation

## Cross-References

### Internal Cross-References within This Session
- Handoff document references other planning folders and role definitions
- Quarterly deliverables reference each other's dependencies (e.g., "Q2 depends on Q1 discovery")
- Job descriptions reference role planning documents
- Deliverables reference research documents for cost/rates/constraints

### References to Other Clients (in Job Descriptions)
- **Sephora** - Mentioned in `jd_ai_engineer_sephora.md` and `jd_ai_engineer_sephora.html` - appears to be a variant or alternate opportunity using the same role template

### Internal BayOne Context
- References to Colin Moore (Director of AI, BayOne)
- References to Rahul (President, BayOne)
- References to Amit (Delivery), Zahra (Sales)
- References to BayOne's design system (Inter font, purple gradients)
- References to minority-owned business status

### Cisco-Specific Context
- **VP Arun** - Executive sponsor
- **Srini/Srinivas** - Senior Engineering Manager
- **Anand** - Director
- **Divakar/Diwakar** - Engineering Lead
- Key systems: NX-OS, CAT, DevX, Jenkins, Airflow, Grafana, pyATS, GitHub
- 39 gates in PR validation process
- On-prem deployment requirement

## Suggested Home
**Parent Folder:** This should be organized under `/home/cmoore/programming/ai_opportunities/clients/cisco/` or similar Cisco-specific folder structure.

The content is entirely Cisco-focused - it contains resource planning, quarterly roadmaps, team structure, and job descriptions specifically for the NX-OS CI/CD Pipeline engagement. While some job descriptions (AI Engineer, Agentic AI Specialist, etc.) are generic enough to be reused for other clients (note: Sephora variant exists), the planning, deliverables, and context are all Cisco-specific.

### Alternative: If maintaining current structure
If keeping under claude/sessions, rename to clarify scope: `2026-02-02_cisco-resource-planning/` or `2026-02-02_cisco-nx-os-cicd/`

---

**Summary Statistics:**
- Total files: 47 files across 5 directories
- Job descriptions: 7 roles, 14+ file variants (markdown + HTML + variations)
- Planning documents: 11 core planning files
- Research/constraints: 3 research documents
- Quarterly deliverables: 4 detailed quarterly plans
- Largest file: Market research document (40K), PDF asset (3.2M)
- Budget: $370K/year, under $100K/quarter target by $30K annually

**Key Decision Point:** This session represents significant structural planning work for a major Cisco engagement. The handoff document indicates follow-up work needed to finalize team structure (onshore vs offshore allocation) and update the main deliverable document.

