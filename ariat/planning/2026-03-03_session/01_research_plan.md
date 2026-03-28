# Research Plan: Content Discovery for Ariat Slides

**Created:** 2026-03-03
**Objective:** Systematically explore codebase to find viable content for Ariat presentation slides

---

## Folders to IGNORE (Per User Instruction)

- `claude/2025-02-25_big4_discovery_guide`
- `claude/2026-02-04_recruiter-guides`
- `claude/2026-02-11_skill-forge-creation`
- `claude/2026-02-20_mcgrath_rfp`
- `claude/2026-02-20_meeting-analyzer-hook-redesign`
- `claude/2026-02-23_rfp-questions-skill`
- `claude/2026-02-26_sephora-hiring`
- `claude/meeting-analyzer`

---

## Exploration Waves (Max 4 Parallel Agents Each)

### Wave 1: Primary Content Sources
| Agent | Target Folder | Rationale |
|-------|--------------|-----------|
| 1 | `sephora/` | User specifically mentioned as having real use cases |
| 2 | `claude/2026-02-17_cisco-meeting-summaries` | Recent meeting context, potential patterns |
| 3 | `claude/2026-02-10_capabilities_deck` | Template slides - understand existing structure |
| 4 | `claude/2025-02-25_big4_edw_framework` | Potentially relevant AI/data content |

### Wave 2: Project and Client Folders
| Agent | Target Folder | Rationale |
|-------|--------------|-----------|
| 1 | `SOW/` | Statements of work - service descriptions |
| 2 | `mcgrath/` | Separate project, may have reusable patterns |
| 3 | `zeblock/` | Recent project folder |
| 4 | `project/` | Current state documents |

### Wave 3: Context and Supporting Materials
| Agent | Target Folder | Rationale |
|-------|--------------|-----------|
| 1 | `context/` | Internal context files |
| 2 | `documents/` | Legacy client-facing and internal documents |
| 3 | `new_context_2-2-2026/` | Meeting transcripts and emails |
| 4 | `specs/` | Design specifications |

### Wave 4: Remaining Claude Sessions
| Agent | Target Folder | Rationale |
|-------|--------------|-----------|
| 1 | `claude/2026-02-02_resource-planning` | Resource planning content |
| 2 | `claude/2026-02-17_discovery-call-prep` | Discovery call preparation |
| 3 | `claude/2026-02-20_ui-conversion-discovery` | UI/UX related content |
| 4 | `claude/meetings` | Meeting-related materials |

### Wave 5: Top-Level Transcripts (If Needed)
- Review `.txt` files at root level for relevant content
- These are session transcripts that may contain useful discussions

---

## Output Structure

For each wave, create:
- `research/wave_N_findings.md` - Raw findings from that wave
- After all waves: consolidate into topic-focused documents

---

## Progress Tracking

| Wave | Status | Findings File |
|------|--------|---------------|
| Wave 1 | **COMPLETE** | `research/wave_1_findings.md` |
| Wave 2 | **COMPLETE** | `research/wave_2_findings.md` |
| Wave 3 | **COMPLETE** | `research/wave_3_findings.md` |
| Wave 4 | **COMPLETE** | `research/wave_4_findings.md` |
| Wave 5 | **SKIPPED** | Not needed - comprehensive coverage achieved |
| Consolidation | Pending | Topic-specific documents |
