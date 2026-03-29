# Claude Session Migration Tracker

**Purpose:** Track migration of content from `claude/` session folders to root-level client directories.
**Approach:** Option C (reorganize by function) with date-prefixed subfolders. Session folders keep `_explorer_summary.md` and get `_MIGRATED.md` note.

## Migration Status

| # | Session Folder | Client | Target Dir | Status |
|---|---------------|--------|-----------|--------|
| 1 | `2025-02-25_big4_discovery_guide` | Sephora | `sephora/quality_reviews/` | **DONE** (2026-03-28) |
| 2 | `2025-02-25_big4_edw_framework` | Sephora | `sephora/quality_reviews/` | **DONE** (2026-03-28) |
| 3 | `2026-02-02_resource-planning` | Cisco | `cisco/cicd/planning/` | **DONE** (2026-03-28) |
| 4 | `2026-02-04_recruiter-guides` | Cisco | `cisco/cicd/planning/` | **DONE** (2026-03-28) |
| 5 | `2026-02-10_capabilities_deck` | BayOne | `bayone/positioning/` | **DONE** (2026-03-28) |
| 6 | `2026-02-11_skill-forge-creation` | Tooling | `claude/` (keep) | No migration needed |
| 7 | `2026-02-17_cisco-meeting-summaries` | Cisco | `cisco/cicd/meetings/` | **DONE** (2026-03-28) |
| 8 | `2026-02-17_discovery-call-prep` | Cisco | `cisco/cicd/meetings/` | **DONE** (2026-03-28) |
| 9 | `2026-02-20_mcgrath_rfp` | McGrath | `mcgrath/` | **DONE** (2026-03-28) |
| 10 | `2026-02-20_meeting-analyzer-hook-redesign` | Tooling | `claude/` (keep) | No migration needed |
| 11 | `2026-02-20_ui-conversion-discovery` | Cisco (EPNM) | `cisco/epnm_ems/` | **DONE** (2026-03-28) |
| 12 | `2026-02-23_rfp-questions-skill` | Tooling | `claude/` (keep) | No migration needed |
| 13 | `2026-02-26_sephora-hiring` | Sephora | `sephora/ravi/` | **DONE** (2026-03-28) |
| 14 | `2026-03-03_ariat_slides` | Ariat | `ariat/` | **DONE** (2026-03-28) |
| 15 | `2026-03-04_big4_slide1_review` | Ariat | `ariat/` | **DONE** (2026-03-28) |
| 16 | `2026-03-04_big4_slide_titles` | Ariat | `ariat/` | **DONE** (2026-03-28) |
| 17 | `2026-03-04_tailored-brands-prep` | Tailored Brands | `tailored_brands/` | **DONE** (2026-03-28) |
| 18 | `2026-03-05_big4_meeting4_html` | Sephora | SKIPPED (empty stub) | **DONE** (2026-03-28) |
| 19 | `2026-03-05_big4_neha_email` | Sephora | `sephora/meetings/04_*/neha_email/` | **DONE** (2026-03-28) |
| 20 | `2026-03-05_big4_sephora_technical_deep_dive` | Sephora | `sephora/quality_reviews/` | **DONE** (2026-03-28) |
| 21 | `2026-03-10_linkedin_anniversary` | BayOne | `bayone/personal/` | **DONE** (2026-03-28) |
| 22 | `2026-03-16_ai-manager-jd` | BayOne | `bayone/hiring/` | **DONE** (2026-03-28) |
| 23 | `2026-03-17_opportunity_catalog` | BayOne | `bayone/positioning/` | **DONE** (2026-03-28) |
| 24 | `2026-03-19_pptx_extractor_skill` | Tooling | `claude/` (keep) | No migration needed |
| 25 | `2026-03-20_big4_lam_problem_restatement` | Lam Research | `lam_research/` | **DONE** (2026-03-28) |
| 26 | `2026-03-20_lam-research` | Lam Research | `lam_research/` | **DONE** (2026-03-28) |
| 27 | `2026-03-23_mcgrath_slides` | McGrath + BayOne | Split: `mcgrath/` + `bayone/processes/` | **DONE** (2026-03-28) |
| 28 | `SESSIONS/` | Archive | `claude/` (keep) | No migration needed |
| 29 | `meeting-analyzer/` | Sephora | `sephora/meetings/` | **DONE** (2026-03-28) |
| 30 | `meetings/` | Cisco | `cisco/cicd/meetings/` | **DONE** (2026-03-28) |

## Summary

| Status | Count |
|--------|-------|
| **DONE** | 25 (Ariat 3, Lam Research 2, Tailored Brands 1, McGrath 3, Cisco 6, Sephora 7, BayOne 4) |
| **No migration needed** (tooling/archive stays in claude/) | 5 |
| **Pending** | 22 |

## Migration Notes

- **Ariat (done):** Content files copied to ariat/ organized by function. Session transcripts (.txt) left in claude/ as working history. _MIGRATED.md notes placed in each session folder.
- **Tooling folders stay:** skill-forge, meeting-analyzer-hook-redesign, rfp-questions-skill, pptx-extractor — these are Claude Code skill development, not client work.
- **SESSIONS/ stays:** Transcript archive, already well-organized.
- **Folder #18 (big4_meeting4_html):** Empty stub with only state.json — candidate for skip/delete.
