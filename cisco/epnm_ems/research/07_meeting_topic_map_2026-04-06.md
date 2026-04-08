# 07 - Meeting: Topic Map

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting — first meeting with Cisco engineering team)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Product Walkthrough: Inventory
- Live demo of EPNM network devices screen, device 360, device details, chassis view
- Data flow: SNMP/CLI queries -> Oracle DB -> application layers
- Device add (single + bulk CSV import), admin state, managed state
- Oracle in EPNM, Postgres in EMS (Oracle dependency removed)
- Images stored in application, not database
- ~80% of backend functionality already reimplemented in EMS
- First time BayOne has actually seen the product in action

**Proposed file:** `07_meeting_product_walkthrough_inventory_2026-04-06.md`

### 2. Product Walkthrough: Fault Management
- Alarms and events screens, correlated alarms, syslogs
- Table actions, expandable row data, filtering (quick filter + advanced filter)
- Events page with time-based filtering (past 8 hours)
- Part 2 of the POC scope, distinct functional area from inventory

**Proposed file:** `07_meeting_product_walkthrough_faults_2026-04-06.md`

### 3. Architecture and Repository Structure
- EPNM repos: PI framework (Dojo core), wireless framework, assembly repo (inventory UI), ChassisView repo, fold management
- EMS repos: Infra UI (shell app with header/top menu), common UI (shared components like cards/tables), EMS UI (feature pages)
- Backend: Spring Boot primarily, some Go services for device management
- Frontend: Angular 21, Harbor/Magnetic design system
- Code organization: where classic UI code should live (EMS UI repo or new repo — to be decided)

**Proposed file:** `07_meeting_architecture_and_repositories_2026-04-06.md`

### 4. AI Compliance and Tooling
- Ramesh's questions about AI tool compliance and code exposure
- Colin's response: Cisco hardware only, Cisco-issued Claude Code, LangGraph local
- Existing CICD engagement as precedent (working with Srinivas Pita and Anand)
- Library installation gating, no external cloud tools
- DeepSeek also being used in other Cisco contexts

**Proposed file:** `07_meeting_ai_compliance_and_tooling_2026-04-06.md`

### 5. Testing and QA Approach
- Ramesh and Praveen's detailed questions about validation
- Existing test lifecycle: functional, scale, end-to-end, UI, API, migration, upgrade
- Thousands of test cases across different devices
- Data-driven testing: device configurations drive test coverage
- Colin's Playwright agent approach for automated UI testing
- Existing UI tests won't work (UI is changing) — need new classic UI test equivalents
- POC: enough testing to guarantee equivalency; full agentic QA for post-POC

**Proposed file:** `07_meeting_testing_and_qa_approach_2026-04-06.md`

### 6. Access and Next Steps
- AD group access for EPNM and EMS repos
- VM requirements: EPNM read-only access, EMS development setup
- Team space creation (WebEx)
- Confluence page with links, user guides, recordings, API docs already prepared
- Time zone coordination: India (IST) for most team, EST for Colin, PST for Zahra

**Proposed file:** `07_meeting_access_and_next_steps_2026-04-06.md`

---

## Processing Plan

1. Spawn 6 parallel agents, one per topic above
2. After all agents complete, update org chart (major update — many new people)
3. Write bridge document (06-07)
4. Write summary document (last)
