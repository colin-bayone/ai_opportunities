# Cisco Projects - Corrected Research (Auditable)

**Date:** 2026-03-17
**Research Method:** File-by-file reading (no keyword search)
**Files Reviewed:** 62 files across meeting summaries, core documents, UI conversion, and SOW folders

---

## CISCO CLIENT PROJECTS (BayOne Engagements)

### PROJECT 1: NX-OS CI/CD Pipeline Improvement

**Description:**
Improving Cisco's NX-OS CI/CD pipeline with AI-driven tooling to provide developer visibility, reduce manual effort, and speed up PR merge time. Target: 20-30% reduction in average PR merge time. Multi-phase engagement covering Developer Box instrumentation (Item A), Branch Health dashboards (Item F), and future phases for unified interface, failure diagnosis, coverage tracking, and self-healing.

**Team/Stakeholders:**
- **Cisco:** Anand (Director), Srinivas/Srini (Senior Engineering Manager), Divakar/Diwakar (Engineering Lead), Arun (VP - sponsor)
- **BayOne:** Colin Moore (Director of AI, technical lead), Rahul (President), Amit (Delivery), Zahra (Sales)

**Technologies:**
Jenkins, Apache Airflow, CAT (Commit Approval Tool), DevX platform, Grafana, MongoDB, MySQL, Splunk, Bazel, Podman containers, pyATS (test automation), CDT (Context Driven Testing - 2+ years live), DeepSight Atlas AI platform

**Budget/Timeline:**
- Budget: $100K/quarter (starting baseline)
- Team: 1-1.5 FTE onshore (Bay Area), 4-5 offshore to scale
- Timeline: 6-8 months across 5 phases (810-1,230 dev hours estimated)
- Phase 1: A (Developer Box) + F (Branch Health) - 150-210 hours

**Status:**
Discovery phase started Feb 17, 2026. Awaiting access provisioning. Phase 1 (Items A+F) selected as starting point.

**Source Files:**
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

**Work Streams (Internal Detail):**
- A: Developer Box Instrumentation
- B: Gate Failures / AI-Driven Diagnosis
- C: Cross-Pipeline Unified Interface
- D: Coverage Tracking Enhancement
- E: Self-Healing / Automated Actions
- F: Branch Health / CD Health Dashboards

---

### PROJECT 2: UI Conversion (EPNM to EMS)

**Description:**
Converting legacy EPNM (Evolved Programmable Network Manager) UI screens to modern EMS (Element Management System) architecture. Not just UI skinning - requires extracting tightly-coupled functionality from 15+ year old monolithic system and re-implementing in microservices. Key customers demand old UI be retained because network operators trained on it for 15+ years. 70-100 screens potentially need conversion. POC: 2-3 screens in 4 weeks to demonstrate AI-accelerated conversion capability.

**Team/Stakeholders:**
- **Cisco:** Guhan (Decision maker), Selva (Technical contact)
- **BayOne:** Colin Moore (Director of AI, technical lead - solo for POC)

**Technologies:**
- Backend: Java (both EPNM and EMS)
- Frontend Old (EPNM): Dojo, JavaScript, some Angular
- Frontend New (EMS): Angular
- Architecture: Monolithic → Microservices
- Testing: Playwright (BayOne approach)
- AI Tools: Claude Code, LangGraph agent swarm

**Budget/Timeline:**
- POC: Free (4 weeks, Colin solo)
- Paid engagement: TBD based on POC success
- POC Timeline: ~March 18, 2026 start (waiting on hardware delivery)
- Phase 1 (2 weeks): Exploration, codebase analysis, screen selection
- Phase 2 (2 weeks): Conversion, testing, acceptance

**Status:**
POC proposal stage. NDA signed. Cisco laptop arriving 1-2 weeks from Feb 20, 2026. Waiting on code access and hardware.

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/source/guhan_selva-2-20-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/00_session_handoff.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/01_meeting_breakdown.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/01_session_understanding.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/planning/06_poc_proposal_v6.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/research/03_chronological_timeline.md
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/research/04_themes_and_decisions.md

**Key Constraint:**
All work must be done on Cisco hardware with Cisco-licensed AI tools. No code leaves Cisco infrastructure.

---

### PROJECT 3: Building Nexus 9000 Switches Product Line Testing

**Description:**
Cisco's Cloud Networking Group (CN) Test team engagement for validating NX-OS releases for Nexus 9000 switches product line. Active SOW covering regression testing execution, test case automation, building AI solutions (data pipelines, AI models), testing and deployment in production, and infrastructure tools development. This is a DIFFERENT engagement from Project 1 (different team, different scope, different contract).

**Team/Stakeholders:**
- **Cisco:** Mahaveer Jinka (DCN-Switching-India)
- **BayOne:** Ashish Singh, BayOne Techno Advisors Private Limited

**Technologies:**
NX-OS testing, test automation, AI solutions, data pipelines, regression testing infrastructure

**Budget/Timeline:**
- Budget: Rs 4,393,740.00 INR (approx $100K USD equivalent)
- Timeline: Nov 5, 2025 - Apr 30, 2026 (6 monthly milestones)
- Status: Active contract, currently in execution

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches.md
- /home/cmoore/programming/cisco_projects/cicd/SOW/SESSION_HANDOFF.md
- /home/cmoore/programming/cisco_projects/cicd/SOW/SOW-conversion-notes.md

**Note:**
This project reference #33282. Different from NX-OS CI/CD Pipeline project (which is with Anand/Srinivas/Divakar on the development/pipeline side, not testing side).

---

### PROJECT 4: MDS Code Modernization

**Description:**
Full code modernization of the MDS Element Manager (device management tool for SAN/Fibre Channel switches), migrating from a legacy Java Swing thick client to a React frontend with a Go backend. Legacy codebase stuck on Java 1.8 with ~1,432 Java files and ~242K lines of code.

**Team/Stakeholders:**
- **Cisco:** Cisco engineering team
- **BayOne:** Colin Moore (Director of AI), Gaurav Kotiyal (BayOne liaison, Director Client Services India)

**Technologies:**
- **Source:** Java Swing thick client, Java 1.8, ~1,432 Java files, ~242K lines of code
- **Target:** React frontend, Go backend
- **Approach:** AI-driven code modernization, agentic tooling

**Budget/Timeline:**
- Timeline: 2-3 quarters for the modernization, with Q3 as buffer
- Status: Active delivery, SAL approval cleared after prolonged procurement delay

**Status:**
Active delivery. Onboarding items including GitHub Enterprise training, VPN access, and DeepSight platform onboarding are in motion. Colin has Bay Area availability the week of 3/23 for in-person sessions. A detailed understanding-of-current-state document and approach proposal have been delivered. This engagement is the strongest current proof point for BayOne's AI and engineering capabilities.

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-03-17_opportunity_catalog/source/bayone-ai-opportunity-catalog (1).md

**Note:**
Two distinct work streams under one client relationship: (1) CI/CD pipeline log triage (already documented in Project 1), (2) MDS code modernization (this project).

---

### PROJECT 5: Nexus Dashboard Regression Testing Automation

**Description:**
AI-driven automation for regression test analysis and UI testing for Nexus Dashboard (network controllers). Rama's Test Manager team faces a 3-4 hour/day bottleneck analyzing regression results. Seeking AI solutions to automate analysis and accelerate feedback loops. UI testing with Selenium, Python, Jenkins infrastructure.

**Team/Stakeholders:**
- **Cisco:** Rama (Test Manager), Milesh, Nilesha, Sonawee
- **BayOne:** Colin Moore (exploration discussion)

**Technologies:**
Jenkins, Selenium, Python, Cisco automation infrastructure layer, Cisco Circuit (AI), Nexus Dashboard

**Budget/Timeline:**
- Budget: Not established
- Status: Exploration/discussion phase

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting2_rama-2-17-2026.txt
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/meeting2_rama/00_meeting_breakdown.md

**Note:**
Early stage exploration. No formal engagement or proposal yet.

---

## CISCO INFRASTRUCTURE (Context Only - Not BayOne Projects)

These were mentioned in meetings but are Cisco internal infrastructure, not projects BayOne is working on:

### DeepSight Atlas AI Platform
- Cisco's internal AI platform providing infrastructure for AI applications
- Owned by Srinivas, used by Project 1 (NX-OS CI/CD)
- SDK provided, multiple apps launching
- **Not a BayOne project - it's the platform we'll build on**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting1_anand_srini_divakar-2-17-2026.txt

### DeepSight CI/CD Application
- Existing CI/CD application being launched on DeepSight platform
- Led by Rui on Arun's team
- BayOne will extend this (part of Project 1), not build from scratch
- **Not a separate project - it's infrastructure for Project 1**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting1_anand_srini_divakar-2-17-2026.txt

### Bazel Production Rollout
- Cisco rolling out Bazel (Google's build system) to production
- Mentioned as context for Project 1 (dealing with build issues)
- **Not a BayOne project - it's environmental context**

**Source Files:**
- /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/meeting1_anand_srini_divakar-2-17-2026.txt

---

## PROPOSED BUT NOT CONFIRMED PROJECTS

### Code-Based Modernization (Nilesha's team)
- Description: Converting legacy codebase, potentially Spring to Go, thick client to web UI
- Stakeholders: Guhan, Selva, Nilesha, Colin Moore
- Status: Discussion phase, no formal proposal or engagement
- **Source:** /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/guhan_selva-2-9-2026.txt

### Agentic AI Platform (Varel's team)
- Description: Platform being built to support agentic workflows
- Stakeholders: Varel (team lead)
- Status: Mentioned in conversation, no BayOne involvement
- **Source:** /home/cmoore/programming/cisco_projects/cicd/claude/2026-02-17_cisco-meeting-summaries/source/guhan_selva-2-9-2026.txt

---

## NOT BAYONE SCOPE (Explicitly Excluded)

### AI Code Review Project
- Cisco internal project going live soon
- **NOT in BayOne scope** (boundary to be clarified with Project 1)
- **Source:** /home/cmoore/programming/cisco_projects/cicd/documents/cisco-understanding-of-problem.md

### Code Refactoring/Modernization
- Explicitly stated as **NOT coming to BayOne**
- **Source:** /home/cmoore/programming/cisco_projects/cicd/history/0001_2026-02-02_initial-state.md

### Gaurav Contractor Engagement
- Prior failed contractor engagement (no GitHub access, no US responses)
- **Source:** /home/cmoore/programming/cisco_projects/cicd/new_context_2-2-2026/meetings/rahul1.txt

---

## OTHER CLIENTS FOUND IN FILES (Not Cisco)

These were discovered in the Cisco folder files (primarily in Rahul meeting transcripts) but are SEPARATE client engagements, not Cisco projects:

1. **Coherent** - QA/Testing Managed Services (16-person team, 2+ years active)
2. **Coherent** - CMS Development
3. **Coherent** - Performance Testing (Super Bowl)
4. **Bases** - Loyalty Program Modernization
5. **Walmart** - Test Automation Managed Services (lead stage)
6. **BayOne Talent AI** - Internal recruiting tool
7. **Palantir Project** - Colin mentioned working on it
8. **Adobe** - Migration activity mentioned

**Source:** /home/cmoore/programming/cisco_projects/cicd/new_context_2-2-2026/meetings/rahul2.txt

---

## INTERNAL BAYONE PROJECTS (Not Client Work)

### SOW Template Development
- Creating reusable SOW generation workflow using AI
- Colin Moore leading
- Golden version complete, templating workflow next
- **Source:** /home/cmoore/programming/cisco_projects/cicd/SOW/SESSION_HANDOFF.md

---

## SUMMARY TABLE

| # | Project Name | Team | Status | Budget | Timeline |
|---|--------------|------|--------|--------|----------|
| 1 | NX-OS CI/CD Pipeline Improvement | Anand/Srinivas/Divakar | Discovery | $100K/qtr | 6-8 months |
| 2 | UI Conversion (EPNM→EMS) | Guhan/Selva | POC Stage | Free POC | 4 weeks POC |
| 3 | Nexus 9000 Switches Testing | Mahaveer Jinka | Active SOW | Rs 4.4M INR | Nov 2025 - Apr 2026 |
| 4 | Nexus Dashboard Regression Testing | Rama | Exploration | TBD | TBD |

**Total Confirmed Cisco Projects: 4**
- 2 Active (Projects 1 and 3)
- 1 POC Stage (Project 2)
- 1 Exploration (Project 4)

---

## METHODOLOGY NOTE

This research was conducted using complete file-by-file reading (no keyword search) across 62 markdown and text files. All source files are cited for auditability. Projects are distinct initiatives with their own scope, stakeholders, and budgets - NOT work streams within a single project.
