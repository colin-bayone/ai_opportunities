# Session Plan: EPNM-to-EMS Singularity Reorganization

**Date:** 2026-04-07
**Objective:** Reorganize cisco/epnm_ems/ from scratch using Singularity, then process all source materials chronologically

---

## Current State

### Completed
- [x] Phase 0: Archived all old content to `archive/`
- [x] Phase 1: Created full Singularity folder structure, methodology doc, initial org chart
- [x] Phase 2: Processed Set 01 (Feb 9 meeting) — 8 research files
- [x] Phase 3: Processed Set 02 (Feb 20 meeting) — 8 research files + bridge doc
- [x] Phase 4: Compared archive content, identified gaps

### Research Library So Far
```
research/
├── 00_methodology_2026-02-09.md
├── 01_meeting_people_2026-02-09.md
├── 01_meeting_topic_map_2026-02-09.md
├── 01_meeting_business_drivers_2026-02-09.md
├── 01_meeting_technical_landscape_2026-02-09.md
├── 01_meeting_bayone_methodology_presentation_2026-02-09.md
├── 01_meeting_security_and_access_2026-02-09.md
├── 01_meeting_next_steps_and_expectations_2026-02-09.md
├── 01_meeting_summary_2026-02-09.md
├── 01-02_changes_2026-02-20.md
├── 02_meeting_people_2026-02-20.md
├── 02_meeting_topic_map_2026-02-20.md
├── 02_meeting_problem_definition_2026-02-20.md
├── 02_meeting_poc_scope_and_success_criteria_2026-02-20.md
├── 02_meeting_engagement_model_and_constraints_2026-02-20.md
├── 02_meeting_domain_gap_and_quality_assurance_2026-02-20.md
├── 02_meeting_next_steps_2026-02-20.md
└── 02_meeting_summary_2026-02-20.md
```

---

## Chronological Source Events (Full Timeline) — REVISED

| Set | Date | Type | Source File | Status |
|-----|------|------|-------------|--------|
| 01 | 2026-02-09 | Meeting | `guhan_selva-2-9-2026.txt` | DONE |
| 01a | ~2026-02-18 | Call Prep | `discovery_questions_call_prep_2026-02-20.md` | NEEDS PROCESSING |
| 02 | 2026-02-20 | Meeting | `guhan_selva-2-20-2026.txt` | DONE |
| 03 | 2026-03-25 | Meeting | `guhan_selva_3_25_2026.txt` | NEEDS PROCESSING |
| 04 | 2026-03-26 | Discussion | Pricing strategy (Colin + Claude) | NEEDS ADOPTION |
| 05 | 2026-03-30 | Internal Call | `ceo_rahul_call_2026-03-30.txt` | NEEDS PROCESSING |
| 05a | 2026-03-30 | Notes | `venkat_notes_2026-03-30.txt` | NEEDS PROCESSING |
| 06 | 2026-04-02 | Discussion | Pricing breakdown + gap analysis (4 files) | NEEDS ADOPTION |
| 07 | 2026-04-06 | Meeting | `selva_and_team_4-6-2026.txt` | NEEDS PROCESSING |

### Flag: Bridge Document Impact
- Bridge `01-02_changes_2026-02-20.md` was written before Set 01a existed. The bridge is still valid (it compares Set 01 to Set 02), but Set 01a may contain additional context not reflected in it. Per blockchain rules, we do NOT edit the bridge. Any new insights from 01a get noted in subsequent documents.
- New bridges needed: 02-03, 03-04, 04-05, 05-06, 06-07 (written after each set is processed)

---

## To-Do List

### Phase 5: Copy Missing Files
- [ ] Copy March 25 transcript from old repo to `source/`
- [ ] Format March 25 transcript with format_transcript.py
- [ ] Copy `ceo.txt` and `venkat.txt` from old repo to `source/`
- [ ] Copy `discovery_questions_v1.md` to `source/` (call prep)
- [ ] Copy POC proposal (v5 md + html + detailed html) to `deliverables/`
- [ ] Copy pricing deliverables to `deliverables/` (one-pager, breakdown, scope/milestone prototypes, email draft)
- [ ] Copy pricing planning files to `pricing/` (excel spec, model prototype, correction prompts, audit files)

### Phase 6: Process Set 03 (March 25 Meeting)
- [ ] Read prior context (Set 02 summary + org chart)
- [ ] Pass 1: People file
- [ ] Pass 1: Topic map — present to user for approval
- [ ] Spawn parallel deep-dive agents
- [ ] Update org chart
- [ ] Bridge document (02-03)
- [ ] Summary (last)

### Phase 7: Process Set 04 (March 26 Pricing Discussion)
- [ ] Review existing archived pricing discussion doc
- [ ] Determine if it can be adopted with header reformatting or needs reprocessing
- [ ] Write/adopt into research library with proper singularity headers
- [ ] Bridge document (03-04)
- [ ] Summary

### Phase 8: Process Set 05 (April 2 Pricing Breakdown)
- [ ] Review existing archived docs (03_discussion, 03a_refinement, 03b_gap_analysis, 03c_gap_resolution)
- [ ] Renumber from old 03/03a/03b/03c to 05/05a/05b/05c
- [ ] Reformat headers to match singularity standard
- [ ] Bridge document (04-05)
- [ ] Summary

### Phase 9: Process Set 06 (April 6 Team Meeting)
- [ ] Read prior context (latest summary + org chart)
- [ ] Pass 1: People file (big meeting — 12 attendees, 8 Cisco, 4 BayOne)
- [ ] Pass 1: Topic map — present to user for approval
- [ ] Spawn parallel deep-dive agents
- [ ] Update org chart (major update — many new Cisco team members)
- [ ] Bridge document (05-06)
- [ ] Summary (last)

### Phase 10: Web Research (Optional)
- [ ] Offer to spawn research agents for Dojo Toolkit and Angular+Java integration
- [ ] If approved, write to research library with appropriate set numbers

### Phase 11: Final Review
- [ ] Compare final research library against all archived content
- [ ] Flag any remaining gaps
- [ ] Write session handoff document to `planning/session_handoff_2026-04-07.md`

---

## Attendees — April 6 Meeting (from screenshots)

**Meeting title:** EPNM Features Walkthrough
**Date:** Monday, April 6, 2026, 12:00 PM - 1:00 PM

### Cisco (8 people)
- Praveen Kumar Vangala (pvangala@cisco.com) — Organizer
- Selva Subramanian (selva@cisco.com)
- Aadit Vaidyanathan (aadvaidy@cisco.com)
- Akhil Francis (akfranci@cisco.com)
- Jenis Dharmadurai (jdharmad@cisco.com)
- Ramesh Dhashnamoorthy (dramesh@cisco.com)
- Ramkrishna Galla (ragalla@cisco.com)
- Senthilkumar Palaniyandi (spalaniy@cisco.com)

### BayOne (4 people)
- Colin Moore (colmoore@cisco.com — using Cisco email)
- Rahul Bobbili (rabobbil@cisco.com)
- Neha Malhotra (nehamalh@cisco.com)
- Zahra Syed (zahsyed@cisco.com)

---

## Flags / Decisions Needed

1. **CEO and Venkat source files:** Need to review to determine which set they belong to (supplementary to Set 03? Set 04? Their own set?).
2. **Discovery questions:** Source doc or its own set (01a call prep)?
3. **Existing pricing/deliverable files from old repo:** Copy verbatim into pricing/ and deliverables/, or review first?
4. **Set numbering for adopted docs:** Sets 04 and 05 are discussions, not transcripts. Adoption (reformat headers) vs reprocessing (full multi-pass)?

---

## Key Rules (Reminders)

- NEVER modify existing research files (blockchain rule)
- Present topic maps to user before spawning agents
- Flag chronological issues rather than fixing autonomously
- Process strictly in chronological order
- All modifications to existing files require explicit user approval
