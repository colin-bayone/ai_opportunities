# 01 - Meeting: Topic Map

**Source:** /cisco/epnm_ems/source/guhan_selva-2-9-2026.txt
**Source Date:** 2026-02-09 (Initial Discovery Meeting, In-Person)
**Document Set:** 01 (First meeting between BayOne and Guhan Selva regarding EPNM-to-EMS)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Business Drivers and Strategic Context
- Why this work matters now: customers demanding legacy UI, business pressure, can't staff 10 people the old way
- Guhan's framing of the modernization challenge across multiple generations
- Product management tensions around prioritization ("everything is priority")
- Customer relationship dynamics: MOUs, education vs accommodation
- The broader organizational challenge of consolidating parallel AI efforts

**Proposed file:** `01_meeting_business_drivers_2026-02-09.md`

### 2. Technical Landscape
- EPNM (legacy, monolithic) vs EMS (microservices) architecture
- 45-50 million lines of code across 6-8 products
- ~200 UI screens needing conversion
- Technology stack: Java backend (both), Dojo/JavaScript frontend (old), Angular (new)
- Agentic AI platform under Meryl (separate effort)
- Azure HD platform in GA phase
- Consolidation of multiple parallel team efforts

**Proposed file:** `01_meeting_technical_landscape_2026-02-09.md`

### 3. BayOne Methodology Presentation
- Colin's code modernization approach: simplification first, then knowledge graphs
- Claude Code as backbone for exploration
- LangGraph agent swarm: architect, engineer, foreman, judge pattern
- Blockchain-style documentation approach
- Automated UX testing with Playwright
- Gap analysis through peer-to-peer agent communication
- Guhan's reaction: interrupted presentation to schedule deeper session

**Proposed file:** `01_meeting_bayone_methodology_presentation_2026-02-09.md`

### 4. Security, Access, and Logistics
- All code must remain on Cisco hardware
- Cisco-licensed AI tools required (not personal licenses)
- NDA signed
- Cisco laptop pending (expected 1-2 weeks)
- Cisco ID pending (expected same day or shortly after)
- Wi-Fi and WebEx connectivity challenges during meeting
- Team also has same NDA/hardware setup

**Proposed file:** `01_meeting_security_and_access_2026-02-09.md`

### 5. Next Steps and Expectations
- Colin to write POC proposal
- 4-week timeline mentioned by Guhan for making decisions
- Hardware timeline to be confirmed same day
- Priority screens to be identified by Guhan's team
- Deeper technical session at 3:00 PM same day with team lead
- Periodic checkpoints agreed
- POC at cost to BayOne (investment approach)
- Team beyond POC already available

**Proposed file:** `01_meeting_next_steps_and_expectations_2026-02-09.md`

---

## Processing Plan

1. Spawn 5 parallel agents, one per topic above
2. Each agent reads the full transcript with focus on their specific topic
3. After all agents complete, update org chart
4. Write summary document (last)
