# 03 - Meeting: Topic Map

**Source:** /cisco/epnm_ems/source/guhan_selva-3-25-2026.txt
**Source Date:** 2026-03-25 (POC Proposal Discussion and Scope Refinement)
**Document Set:** 03 (Third meeting, scope clarification and next steps)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Scope Reframe: Classic View Toggle, Not Missing Functionality
- Project is NOT about converting missing functionality (contradicts Sets 01/02 understanding)
- It is about adding a "classic view" toggle to screens that ALREADY EXIST in EMS
- Backend stays the same; this is a UX overlay using the existing EMS backend
- Outlook/banking app analogy: let users toggle between old and new experience
- Minor backend API changes may be needed for filtering/lens differences
- Driven by customer adoption: operators with 10+ years on EPNM need transition path
- Goal: accelerate customer migration from EPNM to EMS by reducing friction

**Proposed file:** `03_meeting_scope_reframe_2026-03-25.md`

### 2. POC Planning and Execution
- 2-3 screens for POC: faults and inventory identified as candidates
- Local toggle per screen for POC (global toggle comes later in product)
- Colin's exponential decay explanation: first screens are slowest due to front-loading
- Parallelizable workflow: multiple streams once foundation is established
- Automated QA/QE agents for verification: classic vs new UI matching
- Colin to amend POC document for the toggle/classic UI framing

**Proposed file:** `03_meeting_poc_planning_2026-03-25.md`

### 3. July Timeline and Costing Discussion
- Venkat mentioned July release as a possibility (exploring what is realistic, not a hard push)
- Full scope: 200-250 workflow screens
- Budget question acknowledged but no numbers discussed
- Colin suggested starting to look for India resources early to avoid lag
- Selva's concern: server-side changes risk the critical release path
- Second outcome of POC: cost estimation model for the full engagement

**Proposed file:** `03_meeting_july_timeline_and_costing_2026-03-25.md`

### 4. Next Steps and Logistics
- Cisco laptop received by Colin (day before meeting)
- Selva to schedule team session with India domain experts early next week
- WebEx space to be created (Selva, Colin, Rahul)
- Local San Jose resource to be identified for Colin
- Selva to confirm with Guhan on local contact
- Team walkthrough: which screens, what the outcome should be, code access for old and new

**Proposed file:** `03_meeting_next_steps_2026-03-25.md`

---

## Processing Plan

1. Spawn 4 parallel agents, one per topic above
2. Each agent reads the full transcript with focus on their specific topic
3. After all agents complete, update org chart
4. Write bridge document (02-03) — this will be significant given the scope reframe
5. Write summary document (last)
