# 01 - Meeting: Topic Map

**Source:** `source/guhan_selva_3_25_2026.txt`
**Source Date:** 2026-03-25 (POC Proposal Discussion)
**Document Set:** 01 (Meeting Transcript)
**Pass:** Topic identification and file planning

---

## Topics Identified

### 1. Business Driver and Problem Restatement
Guhan opened with a full walkthrough of why this initiative exists. Key customers want the legacy EPNM UI they have used for 15+ years. The decision has been made: the old UI needs to exist in EMS. This is business-impacting and customer-driven, not a technical preference.

**Assigned file:** `01_meeting_business_driver_2026-03-25.md`

### 2. Technical Landscape and Conversion Challenge
Stack confirmed: Java backend on both sides, Dojo/JS frontend (EPNM), Angular frontend (EMS). The work is "vertical" - if UI is missing from EMS, the backend is missing too. Code health discussion, tight coupling in the monolith, prior "surgery" on the old core meaning code cannot be copied directly.

**Assigned file:** `01_meeting_technical_landscape_2026-03-25.md`

### 3. BayOne Methodology Presentation and Reception
Colin presented the approach: Claude Code for exploration, LangGraph agent swarm for deeper conversion work, Playwright for automated visual testing, blockchain-style documentation. Guhan's follow-up question about domain/functionality gaps and how Colin addressed it.

**Assigned file:** `01_meeting_methodology_reception_2026-03-25.md`

### 4. Security, Access, and Logistics
All work on Cisco hardware with Cisco-licensed AI tools. NDA already signed. Laptop expected within 1-2 weeks. Need access to both codebases. Running instances needed only when ready to test. Discussion of what can happen before hardware arrives.

**Assigned file:** `01_meeting_logistics_and_access_2026-03-25.md`

### 5. Stakeholder Expectations and Next Steps
Team cannot invest heavy time but will provide context. Colin expected to work independently with periodic checkpoints. POC output will be used by Guhan to justify additional resources. 4-week timeline. Colin to send POC proposal summary. Initial conversations can begin before hardware.

**Assigned file:** `01_meeting_expectations_and_next_steps_2026-03-25.md`

---

## File Plan

| File | Status |
|------|--------|
| `01_meeting_people_2026-03-25.md` | DONE |
| `01_meeting_topic_map_2026-03-25.md` | DONE (this file) |
| `01_meeting_business_driver_2026-03-25.md` | PENDING |
| `01_meeting_technical_landscape_2026-03-25.md` | PENDING |
| `01_meeting_methodology_reception_2026-03-25.md` | PENDING |
| `01_meeting_logistics_and_access_2026-03-25.md` | PENDING |
| `01_meeting_expectations_and_next_steps_2026-03-25.md` | PENDING |
| `01_meeting_summary_2026-03-25.md` | PENDING (always last) |
