# Attachments — Where to Put Them

Colin asked where to upload attachments referenced in the WebEx chat exports. This guide gives target paths per attachment, following the existing source folder convention you already use.

---

## Convention in use

Looking at the existing source folders:

- **Main Singularity source** (`cisco/cicd/source/`) holds Cisco-side and joint Cisco+BayOne meeting material, plus reference documents shared by Cisco. Newer material organized as `week_YYYY-MM-DD/day_YYYY-MM-DD/`.
- **Team Singularity source** (`cisco/cicd/team/source/`) holds BayOne-internal team meeting material, internal artifacts, and team-side working documents. Newer material also organized as `week_YYYY-MM-DD/day_YYYY-MM-DD/`.
- Week folder is the **Monday** of the week. Day folder is the **actual date** of the source material.
- File names: descriptive, dated, lowercase, underscores. Match the existing convention in adjacent folders.

## Recommended placement, per attachment

The attachments to confirm and upload, with target paths:

### 1. Apr 6 Colin "PFA the overview of our upcoming tasks" (planning overview)

**Target:** `cisco/cicd/team/source/week_2026-04-06/day_2026-04-06/colin_upcoming_tasks_overview_2026-04-06.<ext>`

**Reasoning:** Colin's own internal artifact distributed to the team via internal chat. Pre-Set-07 planning material. Team Singularity. Week folder is Monday Apr 6 since Apr 6 is Monday itself. Create the week folder and day folder if not present.

### 2. Apr 9-10 Namita architecture screenshots / PDFs (multiple)

**Target:** `cisco/cicd/team/source/week_2026-04-06/day_2026-04-09/` and `day_2026-04-10/` as appropriate per actual posting date

**Reasoning:** Namita's internal architecture work shared in team chat. Set 07 source-adjacent material. Team Singularity. Use file names like `namita_architecture_diagram_2026-04-09.<ext>`.

### 3. Apr 15 Namita three architecture/log artifacts (current architecture, current architecture with limitations, log type mapping)

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-15/`

**Reasoning:** Already part of Set 08-09 working material. Team Singularity. Suggested names:
- `namita_current_architecture_2026-04-15.<ext>`
- `namita_current_architecture_with_limitations_2026-04-15.<ext>`
- `namita_log_type_mapping_2026-04-15.<ext>`

### 4. Apr 16 Namita "Initial draft of architecture"

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-16/namita_initial_architecture_draft_2026-04-16.<ext>`

**Reasoning:** Same week as #3. Team Singularity.

### 5. Apr 16 Mahaveer ADS onboarding PDF (`onboarding_ADS_20251201_updated.pdf`)

**Target:** `cisco/cicd/source/week_2026-04-13/day_2026-04-16/mahaveer_ads_onboarding_2026-04-16.pdf`

**Reasoning:** Cisco-side reference document shared by Mahaveer (a Cisco engineer). Goes in the **main Singularity source** (not team), since it is Cisco-originated content the team is consuming. Load-bearing for the temp ADS deployment work. **Highest-priority confirmation.**

You can also keep the original filename `onboarding_ADS_20251201_updated.pdf` if you prefer preserving the Cisco-side filename convention. Either works.

### 6. Apr 16 Srikar 4231-message NXOS-CI-Workflow CSV

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-16/srikar_nxos_ci_workflow_messages_2026-04-16.csv`

**Reasoning:** Srikar's scrape output, already processed into the 25-category taxonomy work. Team Singularity. Likely already in the chain via the issue-categorizer skill repo, but worth a copy in the source folder for chain integrity.

### 7. Apr 16 Srikar rule-based analysis charts and resolvable/unresolvable category outputs

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-16/srikar_rule_based_analysis_2026-04-16.<ext>` and `srikar_resolvable_categories_analysis_2026-04-16.<ext>`

**Reasoning:** Internal team analysis artifacts. Team Singularity.

### 8. Apr 16 Srikar "Update from Naga"

**Target:** Cannot recommend until content is known. **Highest-priority for content confirmation.** If the update is a Cisco-side artifact (Naga's repo update, scope clarification, or similar), goes to main source: `cisco/cicd/source/week_2026-04-13/day_2026-04-16/`. If it is Srikar's internal write-up of a Naga conversation, goes to team source.

Send the attachment to me and I will recommend the path with full confidence.

### 9. Apr 16 Srikar "brief overview of the CI-CD repository"

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-16/srikar_cicd_repo_overview_2026-04-16.<ext>`

**Reasoning:** Srikar's internal walkthrough of the newly-granted CI/CD repo access. Team Singularity.

### 10. Apr 17 Srikar charts and spreadsheets (resolvable/unresolvable)

**Target:** `cisco/cicd/team/source/week_2026-04-13/day_2026-04-17/srikar_pain_point_analysis_2026-04-17.<ext>`

**Reasoning:** Friday Apr 17 deliverable material. Team Singularity. Bridges into the Apr 17 Srinivas meeting (Main Set 12).

### 11. Apr 17 Srinivas "impact graph high level design" CD-build reference

**Target:** `cisco/cicd/source/week_2026-04-13/day_2026-04-17/srinivas_cd_impact_graph_high_level_design_2026-04-17.<ext>`

**Reasoning:** Cisco-side architectural reference shared by Srinivas in the joint chat. Main Singularity. **Load-bearing for build-track architectural direction.** **Second-highest-priority confirmation.**

### 12. Apr 24 Srikar "Update on the cat mcp and issue responder skills"

**Target:** `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srikar_cat_mcp_issue_responder_update_2026-04-24.<ext>`

**Reasoning:** Friday Apr 24 post-meeting work product. Team Singularity. The week folder for Apr 24 already exists.

### 13. Friday Apr 24 12:48 PM Colin "Got MCP running in under 5 minutes" (likely screenshot)

**Target:** `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/colin_mcp_running_screenshot_2026-04-24.<ext>`

**Reasoning:** Internal proof-of-life artifact. Team Singularity.

### 14. Friday Apr 24 1:56 PM Srikar "execute List all CATs in the nx_main branch" (likely screenshot)

**Target:** `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srikar_list_all_cats_nx_main_2026-04-24.<ext>`

**Reasoning:** Internal proof-of-life artifact. Team Singularity.

### 15. Apr 24 Namita 12:23 PM (unknown attachment)

**Target:** Cannot recommend until content is known. Default to team source folder for the date if internal: `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/`.

## Summary by priority

**Upload first (load-bearing for next-week plan):**
- #5 Mahaveer ADS onboarding PDF (main source, Apr 16)
- #11 Srinivas CD impact graph high-level design (main source, Apr 17)
- #8 Srikar "Update from Naga" — content needed before path can be confirmed

**Upload second (chain integrity, useful for cross-reference):**
- #1 Colin's Apr 6 task overview
- #2-#4 Namita architecture screenshots/PDFs
- #9 Srikar CI/CD repo overview

**Upload third (proof-of-life / supporting):**
- #6, #7, #10, #12, #13, #14, #15

## After upload

Once any of these land in their proper source paths, the chats in files 06 and 07 can be cross-referenced against them in future Singularity passes. The chats themselves stay in the session folder (per your earlier instruction); the attachments live where the rest of the source material lives.

For #5 and #11 specifically, a short Singularity backfill set may be warranted later this week (a 14c or 15b letter-suffixed addendum) to incorporate the content into the chain. Not urgent; flag once those two land.
