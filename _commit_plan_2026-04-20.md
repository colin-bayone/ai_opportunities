# Per-File Commit Plan — 2026-04-20

458 pending files enumerated. Reset HEAD ran; nothing is staged.

Prior decisions still apply:
- `image*.png` (anywhere) → SKIP (don't include, don't delete) [Q7/Q8]
- `scratchpad*.py`, `screenshot_chart.py` → SKIP [Q4]
- `excel_cisco_POC.png` → SKIP [Q9]

Action legend:
- **C2** = Cisco commit, **C3** = Lam commit, **C4** = Sephora commit, **C5** = Claude sessions commit, **C6** = misc/skills/cleanup commit
- **SKIP** = leave untracked; don't `git add`, don't delete
- **DELETE** = remove from disk (needs approval)
- **ASK** = Colin needs to decide

Commit 1 already landed (`5e40a31`): .gitignore + claude/SESSIONS consolidation + extract_pdf.py.

---

## Root-level single files (6)

| # | File | Action | Note |
|---|---|---|---|
| 1 | `.vscode/settings.json` | **ASK** | Editor settings. Gitignore (add `.vscode/` to .gitignore in C6)? |
| 2 | `_commit_plan_2026-04-20.md` | **SKIP** | This working file; delete after all commits land |
| 3 | `scratchpad.py` | **SKIP** | Per Q4 |
| 4 | `scratchpad_verify.py` | **SKIP** | Per Q4 |
| 5 | `screenshot_chart.py` | **SKIP** | Per Q4 |
| 6 | `singularity_skill_review_2026-04-20.md` | **ASK** | New root-level file. Purpose? Commit or move? |

## `.claude/skills/singularity/` modified files (3) — C6

| File | Action |
|---|---|
| `.claude/skills/singularity/references/sales_forge_merger.md` | **C6** |
| `.claude/skills/singularity/references/skill_ecosystem.md` | **C6** |
| `.claude/skills/singularity/scripts/html_to_pdf.py` | **C6** |

---

## Commit 2 — Cisco CI/CD (proposed)

### Modified (1)
| File | Action |
|---|---|
| `cisco/cicd/org_chart.md` | **C2** |

### `cisco/cicd/deliverables/` (9)
| File | Action | Note |
|---|---|---|
| `architecture_diagram.png` | **C2** | |
| `avg_response_time.png` | **C2** | |
| `category_distribution.png` | **C2** | |
| `image.png` | **SKIP** | Q7 rule |
| `proposed_architecture_mermaid_2026-04-16.html` | **C2** | |
| `proposed_architecture_mermaid_tb_2026-04-16.html` | **C2** | |
| `srinivas_primer_2026-04-16.html` | **C2** | |
| `srinivas_primer_2026-04-16.md` | **C2** | |
| `weekly_trend.png` | **C2** | |

### `cisco/cicd/documents/` (6) — all **C2**
- `b_CiscoCrossworkAdminGuide_7_1.pdf`
- `bk_cisco_epnm_7_0_0_user_and_administrator_guide_ga.pdf`
- `bk_cisco_epnm_7_0_0_user_and_administrator_guide_ga_PDF_extraction_2026-04-14_184002/bk_cisco_epnm_7_0_0_user_and_administrator_guide_ga.md`
- `…/bk_cisco_epnm_7_0_0_user_and_administrator_guide_ga.xhtml`
- `…/metadata.md`
- `…/tables.md`

### `cisco/cicd/inventory/` (5) — all **C2**
`folder_descriptions.md`, `markdown_inventory.md`, `master_map.md`, `non_markdown_inventory.md`, `sub_team.md`

### `cisco/cicd/planning/` (8)
| File | Action | Note |
|---|---|---|
| `pdf_border_debug_2026-04-20.md` | **ASK** | New 04-20 file — C2 or later? |
| `presentation_topic_assignments_2026-04-16.md` | **ASK** | Not in original plan |
| `proposed_architecture_review_2026-04-16.md` | **C2** | In plan |
| `srinivas_prep_outline_2026-04-16.md` | **C2** | In plan |
| `srinivas_slides_feedback_2026-04-17.md` | **ASK** | Not in original plan |
| `srinivas_slides_handoff_2026-04-16.md` | **C2** | In plan |
| `srinivas_slides_kickoff_2026-04-16.md` | **C2** | In plan |
| `srinivas_slides_outline_2026-04-17.md` | **ASK** | Not in original plan |

### `cisco/cicd/presentations/srinivas_status_2026-04-10/` (9) — all **C2**
`00_title.html`, `01_assigned_items_status.html`, `02_discovery_findings_build.html`, `02a_build_ecosystem_diagram.html`, `03_discovery_findings_webex.html`, `04_items_for_discussion.html`, `05_access_status.html`, `06_next_steps.html`, `charts/build_log_ecosystem.html`

### `cisco/cicd/presentations/srinivas_status_2026-04-17/` (19) — **ASK (new, not in plan)**
12 HTML slides + 6 PNG images + 1 PDF. Commit with C2 or later? Note: includes `images/architecture_diagram.png`, `avg_response_time.png`, `category_distribution.png`, `reply_vs_original.png`, `unresolvable_response_time.png`, `weekly_trend.png` — named screenshots (not "image*.png"), probably keep.

### `cisco/cicd/research/` (3) — all **C2**
`11_meeting_people_2026-04-10.md`, `11_meeting_srinivas_guidance_2026-04-10.md`, `11_meeting_summary_2026-04-10.md`

### `cisco/cicd/source/` (5) — all **C2**
`internal_team_02-10-2026.txt`, `srinivas-and-team_4-7-2026.txt`, `srinivas-and-team_4-7-2026_formatted.txt`, `srinivas-and-team_4-10-2026.txt`, `srinivas-and-team_4-10-2026_formatted.txt`

### `cisco/cicd/team/` (top-level + tracking) (4) — all **C2**
`cross_reference.md`, `tracking/action_items.md`, `tracking/blockers.md`, `tracking/decisions.md`

### `cisco/cicd/team/documents/build_log_analysis_updates_2026-04-10_PDF_extraction/` (30) — all **C2**
Already moved here from skill folder. 1 index.md + 1 metadata.json + 6 page folders × (content.md, layout.md, page_0X.png, raw.md, visual_elements.md) = 30 files.

### `cisco/cicd/team/planning/` (2) — **ASK (new)**
| File | Action |
|---|---|
| `incident_prep_and_meeting_plan_2026-04-20.md` | **ASK** — 04-20, new |
| `namita_response_draft_2026-04-20.md` | **ASK** — 04-20, new |

### `cisco/cicd/team/research/` (59)
In-plan group (original standup + 02-04 chat/sync + 03 briefing + 04 sync + namita/srikar/saurav threads through 04-16): **C2**

Files dated 04-17 or 04-20 (05_prep_*, 05a_srikar, 06_incident_*, 06a_incident_*): **ASK** — new since plan.

Special:
| File | Action |
|---|---|
| `_test_write_permission.md` | **ASK / DELETE?** — looks like a probe file |

Full list:
- **C2 (in plan):** `00_methodology_2026-04-10.md`, `01-02_changes_2026-04-16.md`, `01_standup_action_items_2026-04-10.md`, `01_standup_blockers_2026-04-10.md`, `01_standup_people_2026-04-10.md`, `01_standup_summary_2026-04-10.md`, `01_standup_technical_discussion_2026-04-10.md`, `02-03_changes_2026-04-16.md`, `02_chat_access_training_saga_2026-04-16.md`, `02_chat_people_2026-04-16.md`, `02_chat_post_standup_progress_2026-04-16.md`, `02_chat_summary_2026-04-16.md`, `02_chat_wall_e_bot_demo_2026-04-16.md`, `02_sync_people_2026-04-16.md`, `02a_namita_build_log_analysis_updates_2026-04-10.md`, `02b_namita_log_type_mapping_2026-04-16.md`, `02c_namita_build_architecture_diagrams_2026-04-16.md`, `02d_srikar_webex_recording_extraction_2026-04-16.md`, `02e_saurav_hardware_failure_email_2026-04-15.md`, `03-04_changes_2026-04-16.md`, `03_briefing_engagement_rules_2026-04-07.md`, `03_briefing_people_2026-04-07.md`, `03_briefing_summary_2026-04-07.md`, `03_briefing_task_walkthrough_2026-04-07.md`, `03_sync_action_items_2026-04-16.md`, `03_sync_architecture_framework_2026-04-16.md`, `03_sync_blockers_and_access_status_2026-04-16.md`, `03_sync_colin_directives_2026-04-16.md`, `03_sync_people_2026-04-16.md`, `03_sync_rui_discovery_2026-04-16.md`, `03_sync_summary_2026-04-16.md`, `03_sync_team_continuation_2026-04-16.md`, `03_sync_tooling_and_skills_2026-04-16.md`, `03_sync_webex_scraping_progress_2026-04-16.md`, `04_sync_architecture_framework_2026-04-16.md`, `04_sync_blockers_and_access_2026-04-16.md`, `04_sync_nxos_chat_scraping_2026-04-16.md`, `04_sync_people_2026-04-16.md`, `04_sync_rui_guo_nexus_t_2026-04-16.md`, `04_sync_summary_2026-04-16.md`, `04_sync_team_architecture_discussion_2026-04-16.md`, `04d_srikar_nxos_chat_analysis_2026-04-16.md`, `04e_namita_proposed_architecture_2026-04-16.md`, `04f_saurav_webex_architecture_2026-04-16.md`
- **ASK (04-17 / 04-20 / test):** `04-05_changes_2026-04-17.md`, `05_prep_access_strategy_deepsight_line_in_sand_2026-04-17.md`, `05_prep_build_log_architecture_updates_2026-04-17.md`, `05_prep_contract_extension_and_scope_strategy_2026-04-17.md`, `05_prep_meeting_structure_and_presenters_2026-04-17.md`, `05_prep_nexus_t_rui_repo_contents_2026-04-17.md`, `05_prep_pain_point_deep_dive_2026-04-17.md`, `05_prep_people_2026-04-17.md`, `05_prep_pulse_scribble_naming_and_naga_stance_2026-04-17.md`, `05_prep_summary_2026-04-17.md`, `05a_srikar_updated_pain_point_charts_2026-04-17.md`, `06_incident_disclosure_facts_2026-04-20.md`, `06_incident_summary_2026-04-20.md`, `06a_incident_colin_response_to_namita_2026-04-20.md`, `_test_write_permission.md`

### `cisco/cicd/team/source/` (42)
- **C2 (in plan):** `build_log_analysis_updates_2026-04-10.pdf`, `internal_standup_2026-04-10.txt`, `internal_team_meet_4-13-2026.txt`, `2026-04-16/cisco-team-sync_01.txt`, `2026-04-16/cisco-team-sync_01.vtt`, `2026-04-16/cisco-team-sync_01_meta.json`, `week_2026-04-14/day_2026-04-16/internal_team_briefing_2026-04-07_formatted.txt`
- **ASK (04-20, new):** `2026-04-20/colin-response-to-namita-sent.md`, `2026-04-20/namita-incident-disclosure-exchange.md`
- **namita/ folder:**
  - `Build_log_analysis_upadtes_04102026.pdf` — **ASK** — typo-spelled duplicate of the main PDF? Keep as namita-source artifact or delete?
  - `Log Type Mapping.docx` — **C2**
  - `Proposed Build Log Analysis Architecture — Blocks 1–7.html` — **C2**
  - `build_architecture_with_limitations.html` — **C2**
  - `build_fix_architecture_light.html` — **C2**
  - `image.png` — **SKIP** (junk rule)
  - `namita.txt` — **C2**
- **saurav/ folder:** **C2** — `saurav_email.txt`, `webex_arch_clarifications.md`, `webex_architecture_light 1.html`
- **srikar/ folder (day_2026-04-16/srikar/):** **C2** — `WEBEX_REC_EXTRACTION.md`, `new/1_category_distribution.png`, `new/2_weekly_trend.png`, `new/5_reply_vs_original.png`, `new/6_avg_first_response_time.csv`, `new/6_avg_first_response_time.png`, `new/7_avg_first_response_time_unresolvable.csv`, `new/7_avg_first_response_time_unresolvable.png`, `new/listofcategories.txt`
  - **ASK:** `new/Screenshot 2026-04-16 at 1.50.00 PM.png` — Mac default-named screenshot. Junk or keep?
- **team_chat:** `day_2026-04-16/team_chat_1009AM.txt` — **C2**
- **day_2026-04-17/ (11):** **ASK — new since plan** — `cisco-cicd-friday-meet-and-sync_01.txt`, `_formatted.txt`, `srikar/1_category_distribution(1).png`, `srikar/1_category_distribution.csv`, `srikar/2_weekly_trend(1).png`, `srikar/2_weekly_trend.csv`, `srikar/5_reply_vs_original(1).png`, `srikar/5_reply_vs_original.csv`, `srikar/6_avg_first_response_time(1).csv`, `srikar/6_avg_first_response_time(1).png`, `srikar/7_avg_first_response_time_unresolvable(1).csv`, `srikar/7_avg_first_response_time_unresolvable(1).png`

### `cisco/epnm_to_ems/` (1)
| File | Action |
|---|---|
| `draft_message_2026-04-16.txt` | **C2** (in plan) |

---

## Commit 3 — Lam Research IP (proposed)

### Modified (3) — all **C3**
`lam_research/ip_protection/org_chart.md`, `planning/skill_notes.md`, `research/00_methodology_2026-04-06.md`

### `lam_research/ip_protection/deliverables/` (5) — all **C3**
`engagement_pricing_2026-04-09.html`, `internal_cost_breakdown_2026-04-09.html`, `poc_proposal_2026-04-09.html`, `poc_proposal_2026-04-09.md`, `pricing_breakdown_2026-04-09.html`

### `lam_research/ip_protection/inventory/` (4) — all **C3**
`folder_descriptions.md`, `markdown_inventory.md`, `master_map.md`, `non_markdown_inventory.md`

### `lam_research/ip_protection/planning/` (5)
| File | Action | Note |
|---|---|---|
| `remaining_actions_2026-04-09.md` | **C3** | In plan |
| `sow_filling_instructions_word_claude_2026-04-17.md` | **ASK** | 04-17, new |
| `sow_filling_instructions_word_claude_followup_2026-04-17.md` | **ASK** | 04-17, new |
| `sow_filling_instructions_word_claude_followup2_2026-04-17.md` | **ASK** | 04-17, new |
| `sow_filling_instructions_word_claude_followup3_2026-04-17.md` | **ASK** | 04-17, new |

### `lam_research/ip_protection/pricing/` (3) — all **C3**
`excel_corrections_prompt_v1_2026-04-09.md`, `excel_corrections_prompt_v2_2026-04-09.md`, `excel_poc_spec_2026-04-09.md`

### `lam_research/ip_protection/research/` (22)
- **C3 (in plan):** `05a-06_changes_2026-04-09.md`, `06_internal_pricing_access_and_expansion_2026-04-09.md`, `06_internal_pricing_action_items_2026-04-09.md`, `06_internal_pricing_people_2026-04-09.md`, `06_internal_pricing_poc_pricing_strategy_2026-04-09.md`, `06_internal_pricing_post_meeting_assessment_2026-04-09.md`, `06_internal_pricing_summary_2026-04-09.md`, `06_research_cisco_pricing_reference_2026-04-09.md`, `07-08_changes_2026-04-09.md`, `07_discussion_pricing_exercise_2026-04-09.md`, `07_discussion_pricing_scope_2026-04-09.md`, `07_discussion_summary_2026-04-09.md`, `08_internal_sync2_action_items_2026-04-09.md`, `08_internal_sync2_people_2026-04-09.md`, `08_internal_sync2_pricing_changes_2026-04-09.md`, `08_internal_sync2_summary_2026-04-09.md`, `08a_discussion_pricing_revision_2026-04-09.md`
- **ASK (04-17 / 04-20, new):** `08a-09_changes_2026-04-17.md`, `09_execution_kickoff_mikhail_signal_and_tech_access_2026-04-16.md`, `09_execution_kickoff_sow_filling_strategy_2026-04-17.md`, `09_execution_kickoff_sow_template_structure_2026-04-17.md`, `09_execution_kickoff_summary_2026-04-17.md`, `09a_tech_inventory_part1_march_2026-04-20.md`, `09a_tech_inventory_part2_internal_2026-04-20.md`

### `lam_research/ip_protection/source/` (22)
| File | Action | Note |
|---|---|---|
| `anuj_amit_pratik_colin_internal_4-9-2026.txt` | **C3** | In plan |
| `anuj_amit_pratik_colin_internalsync2_4-9-2026.txt` | **C3** | In plan |
| `excel_cisco_POC.png` | **SKIP** | Q9 |
| `BAYON-MAS-0013142 Sarthak Gupta Mar26.docx` | **ASK** | New |
| `lam_sow.pdf` | **ASK** | New |
| `lam_sow/` (18 files: index.md, metadata.json, 3 page folders × 5 files) | **ASK** | New SOW extraction |
| `mikhail_email_execution_tech_access_2026-04-16.txt` | **ASK** | New |

---

## Commit 4 — Sephora QA (proposed)

### Modified (2) — all **C4**
`sephora/qa_qe_playwright/org_chart.md`, `planning/glossary_2026-03-24.md`

### `sephora/qa_qe_playwright/deliverables/` (22)
**C4:**
- `architecture_detail_2026-04-14.html`
- `architecture_detail_v2_2026-04-14.html`
- `architecture_diagram_experiments/01_mindmap.html` through `05_gitgraph.html` (5)
- `architecture_diagram_exploration_2026-04-14.html`
- `charts/figure_1_platform_architecture.html` + `.png`
- `charts/figure_2_discovery_cycle.html` + `.png`
- `charts/figure_3_playbook_lifecycle.html` + `.png`
- `charts/figure_4_confidence_scoring.html` + `.png`
- `email_draft_vaibhav_2026-04-15.md` + `.txt`
- `preliminary_approach_2026-04-14.html` + `.md`
- `preliminary_approach_concise_2026-04-14.html`
- `technical_foundation_2026-04-14.html`

**SKIP (Q7/Q8):** `imagea.png`, `imageb.png`, `imagec.png`, `imaged.png`, `imagee.png`, `imagef.png`, `imageg.png`, `imageh.png`

### `sephora/qa_qe_playwright/inventory/` (4) — all **C4**
`folder_descriptions.md`, `markdown_inventory.md`, `master_map.md`, `non_markdown_inventory.md`

### `sephora/qa_qe_playwright/planning/` (11) — all **C4**
`architecture_content_draft_2026-04-14.md`, `architecture_diagram_draft_2026-04-14.md`, `deliverable_completion_plan_2026-04-14.md`, `deliverable_outline_preliminary_approach_2026-04-14.md`, `gap_analysis_preliminary_approach_2026-04-14.md`, `mermaid_flowchart_learnings_2026-04-14.md`, `mermaid_svg_scaling_research_2026-04-14.md`, `playwright_screenshot_research_2026-04-14.md`, `session_handoff_2026-04-14.md`, `svg_scaling_browser_research_2026-04-14.md`, `vaibhav_meeting_refresher_2026-04-09.html`

### `sephora/qa_qe_playwright/research/` (18) — all **C4**
`01-02_changes_2026-04-09.md`, `02_meeting_budget_timeline_2026-04-09.md`, `02_meeting_engagement_model_2026-04-09.md`, `02_meeting_people_2026-04-09.md`, `02_meeting_summary_2026-04-09.md`, `02_meeting_technical_approach_2026-04-09.md`, `02_meeting_topic_map_2026-04-09.md`, `02_meeting_visual_qa_scope_2026-04-09.md`, `03_discussion_control_panel_and_open_webui_correction_2026-04-14.md`, `03_discussion_deliverable_feedback_round_1_2026-04-14.md`, `03_discussion_document_outline_and_depth_calibration_2026-04-14.md`, `03_discussion_document_structure_and_ecosystem_approach_2026-04-14.md`, `03_discussion_engagement_models_and_deliverable_framing_2026-04-14.md`, `03_discussion_gap_analysis_decisions_2026-04-14.md`, `03_discussion_infrastructure_and_production_architecture_2026-04-14.md`, `03_discussion_sequencing_and_qe_framing_2026-04-14.md`, `03_discussion_system_architecture_and_design_principles_2026-04-14.md`, `03_research_open_webui_2026-04-14.md`

### `sephora/qa_qe_playwright/source/` (3) — all **C4**
`vabhav_3_24_2026_formatted.txt`, `vaibhav_colin_sync_4-9-2026.txt`, `vaibhav_colin_sync_4-9-2026_formatted.txt`

---

## Commit 5 — Claude session archives (proposed)

All **C5** unless noted. 102 files across 10 dated folders.

### `claude/2026-04-10_singularity_nested_design/` (14)
5 MDs + 1 TXT transcript + 8 example HTML slides.

### `claude/2026-04-13_cisco_cicd_team_issues/` (11)
1 agent output + 9 issue MDs + 1 source transcript.

### `claude/2026-04-13_mermaid_research/` (28)
`b2_violation_review_2026-04-14.md`, 5 diagrams/*.html, 6 path_verification/issues MDs, 1 prompt MD, 5 references/*.md, 9 shape_library/*.html + 1 TODO.md.

### `claude/2026-04-13_singularity_reorganization_session/` (1)
`skill_issues.md`

### `claude/2026-04-14_pdf_extraction_test/` (10)
Rivian RFP PDF + two extraction output folders + 3 working MDs + 1 test.txt. **ASK** for `test.txt` (delete?).

### `claude/2026-04-14_sephora_proposal_handoff/` (2)
`HANDOFF.md`, `KICKOFF.md`

### `claude/2026-04-15_cisco_cicd_scoping_brainstorm/` (23)
6 draft/brainstorm MDs + 10 source TXTs + 2 strategy files + 7 transcript analysis MDs.

### `claude/2026-04-16_big4_srinivas_primer/` (3)
`research/source_analysis.md`, `source/srinivas_primer_2026-04-16.html`, `state.json`

### `claude/2026-04-16_cisco_architecture_mermaid_rebuild/` (1)
`HANDOFF.md`

### `claude/singularity_feedback/2026-04-13_round_01/` (11)
1 index + 1 synthesis + 1 change log + 8 sources MDs.

---

## Totals

| Bucket | Count |
|---|---|
| C2 (Cisco, defined) | ~140 |
| C3 (Lam, defined) | ~37 |
| C4 (Sephora, defined) | ~58 |
| C5 (Claude sessions) | ~102 |
| C6 (skills) | 3 |
| SKIP | ~16 (image*.png + scratchpads + excel_POC + _commit_plan + singularity_skill_review ASK) |
| ASK | ~55 (new 04-17/04-20 files, new dirs, namita PDF, _test_write_permission, Screenshot PNG) |
| **Total** | **458** |

---

## Decisions needed from Colin (5 real questions)

### Q-REMAINING-1. New 04-17 / 04-20 work across Cisco and Lam

About 85 of the 115 pending files are work that happened AFTER the original plan was written. Cisco got new planning files, a new srinivas_status presentation for 04-17, team incident files from 04-20, and another week of team source material. Lam got new SOW-filling instructions, execution-kickoff research, a new SOW PDF extraction, and a couple more source transcripts.

Options:
- (a) Just extend Cisco and Lam commits — one catch-up commit per client with everything new
- (b) Group by semantic topic instead (e.g., "Cisco Srinivas 04-17 meeting package", "Lam SOW execution kickoff")
- (c) One big "catch-up" commit across both

### Q-REMAINING-2. Skill modifications

3 modified files under `.claude/skills/singularity/`. Own commit, or bundled into the catch-up?

### Q-REMAINING-3. `.vscode/settings.json`

Gitignore (recommended — keeps IDE prefs personal) or commit?

### Q-REMAINING-4. `singularity_skill_review_2026-04-20.md`

New root-level file, unknown purpose. You tell me what it is.

### Q-REMAINING-5. Junk candidates (batch)

Four suspicious files — all keep, all drop, or mixed:
- `cisco/cicd/team/research/_test_write_permission.md` (probe file)
- `cisco/cicd/team/source/…/namita/Build_log_analysis_upadtes_04102026.pdf` (typo-named duplicate of already-committed PDF)
- `cisco/cicd/team/source/…/srikar/new/Screenshot 2026-04-16 at 1.50.00 PM.png` (default Mac screenshot name)
- `claude/2026-04-14_pdf_extraction_test/test.txt` (test file in test folder)
