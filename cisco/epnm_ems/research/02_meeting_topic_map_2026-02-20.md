# 02 - Meeting: Topic Map

**Source:** /cisco/epnm_ems/source/guhan_selva-2-20-2026.txt
**Source Date:** 2026-02-20 (Follow-Up Technical Meeting)
**Document Set:** 02 (Second meeting, deeper technical detail on the EPNM-to-EMS conversion)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Problem Definition
- Two products: EPNM (legacy) and EMS (modern, microservices)
- Two architectures: monolithic vs microservices, different frontends
- Vertical functionality gaps: both UI and backend missing together
- Customers demanding identical experience from the legacy product
- Decision already made: EPNM UI must exist, customers must be able to use it
- "Surgery" already done on old core, so code won't port directly
- Some functionality already brought over with new UX, some still missing

**Proposed file:** `02_meeting_problem_definition_2026-02-20.md`

### 2. POC Scope and Success Criteria
- Convert select screens end-to-end (UI + backend)
- Show a working demo to build confidence
- Establish estimation methodology: if 10 screens take X days, extrapolate
- Focus on functionality NOT yet brought into EMS
- 70-80-100 pages mentioned (not expecting all converted)
- Missing reports as a concrete starting example
- Results help Guhan promise delivery timelines to customers

**Proposed file:** `02_meeting_poc_scope_and_success_criteria_2026-02-20.md`

### 3. Engagement Model and Constraints
- Engineering team on critical platform work, cannot invest significant time
- BayOne must work independently after receiving context
- Periodic checkpoints for progress and clarification
- Running systems needed for testing (provided when ready)
- Code access required, legacy product lacks design documentation
- Cisco laptop and ID still pending
- All work on Cisco infrastructure with Cisco-licensed tools

**Proposed file:** `02_meeting_engagement_model_and_constraints_2026-02-20.md`

### 4. Domain Gap and Quality Assurance
- Guhan's direct question: how do you ensure no domain or functionality gap?
- Element management is a specialized domain with no readily available prior knowledge
- Colin's response: judge agent pattern, Playwright automated UX testing
- Screen capture comparison, automated inspection
- Categorical gap analysis (if something is missed, it is usually a whole category)
- Human final review as last line of defense
- Agent peer-to-peer communication for self-correction

**Proposed file:** `02_meeting_domain_gap_and_quality_assurance_2026-02-20.md`

### 5. Next Steps
- Colin to write POC proposal based on both meetings
- Code access to be arranged
- Initial conversations with Varel's team for context transfer
- Cisco laptop hardware timeline to be confirmed
- 4-week decision window (from Set 01, reinforced here)
- Automated UX testing offered as additional value-add

**Proposed file:** `02_meeting_next_steps_2026-02-20.md`

---

## Processing Plan

1. Spawn 5 parallel agents, one per topic above
2. Each agent reads the full transcript with focus on their specific topic
3. After all agents complete, update org chart
4. Write bridge document (01-02)
5. Write summary document (last)
