# Singularity Skill Change Log — Round 01

**Purpose:** Lightweight summary of what we changed in the working copy of the Singularity skill at `.claude/skills/singularity/` during this round, with intent. Used when syncing to the master skill repository — a Claude session there can compare our skill folder to the master and reconcile, with this log providing context on why changes were made.

**Not in scope:** line-level diffs, before/after code, exhaustive patch descriptions. The receiving Claude session will handle diffing mechanically.

**Scope:** all edits to `.claude/skills/singularity/**` during Round 01 (started 2026-04-10, continuing through Phase 5 completion).

---

## Log Format

Each entry:

- **File** — path relative to `.claude/skills/singularity/`
- **Change type** — added / modified / removed / renamed
- **Intent** — one or two sentences on why
- **Source** — which synthesis section or todo item drove it

---

## Pre-Round 01 Changes (already made during 2026-04-10 session, before consolidation)

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `SKILL.md` | modified | Added Flow 7 (Present) to invocation menu and flow section | Synthesis §11, master todo Phase 1 pre-work |
| `SKILL.md` | modified | Replaced "Slide skill (TBD)" line in Sibling Skills table | Synthesis §11, pre-Phase-1 cleanup |
| `references/presentation_design_language.md` | added | New reference file defining the design language for presentations | Synthesis §11 |
| `assets/slide_examples/example_title.html` | added | Example slide: dark full-bleed title | Synthesis §11.6 |
| `assets/slide_examples/example_agenda.html` | added | Example slide: agenda / navigation row | Synthesis §11.6 |
| `assets/slide_examples/example_profile.html` | added | Example slide: split panel profile | Synthesis §11.6 |
| `assets/slide_examples/example_three_column.html` | added | Example slide: three-column card grid | Synthesis §11.6 |
| `assets/slide_examples/example_split_concept.html` | added | Example slide: split panel with concept cards | Synthesis §11.6 |
| `assets/slide_examples/example_grid_takeaway.html` | added | Example slide: grid + takeaway bar | Synthesis §11.6 |
| `assets/slide_examples/example_closing.html` | added | Example slide: dark full-bleed closing | Synthesis §11.6 |
| `scripts/singularity_stop.py` | modified | Added check that presentation design references exist if presentation HTML exists | Synthesis §14.1 |
| `references/presentation_design_language.md` | modified | Added embedded-diagram-with-full-screen-viewer pattern + back button | Synthesis §11.9 |
| `references/worked_example/planning/skill_notes.md` | modified | Added frozen-in-time header to disambiguate from authoritative current skill notes | Round 01 consolidation work |

## Phase 0 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `SKILL.md` | modified | Amended structural rule 5 with parenthetical clarifying max-5 applies to written follow-ups, not interactive discussion (see B1) | Synthesis §1.1, todo 0.2 |
| `SKILL.md` | modified | Expanded structural rule 10 (self-contained) to explicitly prohibit cross-referencing external paths as authoritative | Colin correction during Phase 0 |
| `SKILL.md` | modified | Added Behavioral Hard Rules subsection (B1-B15) under Hard Rules | Synthesis §1, todo 0.1-0.16 |
| `SKILL.md` | modified | Added Rule Violation Protocol (stop, re-read, acknowledge, correct) | Colin instruction during Phase 0 |
| `references/enforcement_architecture.md` | added | Documents the artifact-based enforcement pattern: every step produces an artifact, stop hook checks all artifacts exist, exit code 2 blocks on missing artifacts. References django-forge-v2. | Colin instruction to document as architecture reference |

| `references/hard_rules.md` | added | Behavioral hard rules B1-B16 plus Rule Violation Protocol, extracted from SKILL.md into standalone mandatory-read file | Synthesis §1, enforcement_architecture.md pattern |
| `SKILL.md` | modified | Removed inline B1-B15 + Rule Violation Protocol (moved to hard_rules.md). Added step 5-6 to Mandatory Startup: read hard_rules.md, stop if missing. | Enforcement architecture pattern |
| `scripts/singularity_stop.py` | modified | Added Check 3: verify hard_rules.md exists | Enforcement architecture pattern |

---

## Phase 0 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `SKILL.md` | modified | Amended structural rule 5 with parenthetical clarifying that max-5 applies to written follow-ups, not interactive discussion (see B1) | Synthesis §1.1, todo 0.2 |
| `SKILL.md` | modified | Expanded structural rule 10 (self-contained skill) to explicitly prohibit cross-referencing session/engagement folders as authoritative sources from within the skill definition | Colin correction during Phase 0 work |
| `SKILL.md` | modified | Added "Behavioral Hard Rules" subsection (B1-B15) under Hard Rules, covering all 15 documented failure patterns with rule statement, rationale, and correction date for each | Synthesis §1, todo 0.1-0.16 |
| `SKILL.md` | modified | Added "Rule Violation Protocol" — when user indicates a rule is violated, Claude must stop, re-read Hard Rules, acknowledge the specific rule, and correct course | Colin instruction during Phase 0 work, todo 0.17 |

---

## Phase 1 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `assets/design/gold_standards/presentations/srinivas_status/` | added (directory + 8 slides + charts/) | Full Srinivas status deck as the presentation gold standard. 8 slides + 1 chart file. | Todo 1.1 |
| `assets/design/gold_standards/presentations/srinivas_status/README.md` | added | Documents what each slide demonstrates, key design rules, and the nav chain | Todo 1.1 |
| `references/worked_example_team/` | added (directory + 10 files) | Team sub-singularity worked example: methodology, 5 research files, 3 tracking files, cross_reference.md. Source folder empty (transcript redacted). | Todo 1.2 |
| `references/worked_example_team/README.md` | added | Documents what the example demonstrates, folder structure, differences from parent worked example | Todo 1.2 |
| `assets/design/gold_standards/charts/example_ecosystem_diagram.html` | added | Standalone chart gold standard: mermaid ecosystem diagram with back button and blue theme | Todo 1.3 |

---

## Phase 2 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `references/nested_singularity.md` | added | Full sub-singularity pattern: concept, when to use, folder template, 12 rules (structural, relationship, naming), cross-reference format, how to add, org chart handling, worked example reference | Todo 2.1 |
| `references/team_meeting_processing.md` | added | Team meeting methodology: when to use, 6 standard passes (people, action items, blockers, decisions, technical, summary), differences from client meetings, tracking doc update rules, agent architecture, worked example reference | Todo 2.2 |
| `references/tracking_folder_pattern.md` | added | Tracking folder dual model: concept, 3 standard files (action_items, blockers, decisions) with templates, column specs, update rules, worked example reference | Todo 2.3 |
| `references/folder_structure.md` | modified | Added sub-singularity folder structure section with template, folder purposes table, key distinctions (deliverables vs presentations vs planning vs documents) | Todo 2.4 |
| `references/complete_structure.md` | modified | Updated skill file structure tree (added 8 new references, slide_examples, gold_standards/presentations, gold_standards/charts, 3 scripts). Updated engagement output structure (added team/ and other sub-singularity). Updated "What Lives Where" decision guide with sub-singularity rows. | Todo 2.5 |
| `references/blockchain_methodology.md` | modified | Added rule 7 (tracking files are living, exception to append-only). Added "Application to Sub-Singularities" section explaining same rules apply within sub-singularities plus tracking folder. | Todo 2.6 |

---

## Phase 3 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `references/presentation_design_language.md` | modified | Added Gold Standard Reference section pointing to `gold_standards/presentations/srinivas_status/` with instruction to read before generating | Todo 3.5 |
| `references/presentation_design_language.md` | modified | Added Bullet Item Pattern component (`.items`/`.item` CSS + HTML + usage rules, flagged as default for all card bodies) | Todo 3.2 |
| `references/presentation_design_language.md` | modified | Added Slide Navigation component (CSS + HTML + link chain rules, flagged as mandatory) | Todo 3.3 |
| `references/presentation_design_language.md` | modified | Added Dedicated Diagram Slide pattern and Status Grid pattern to Example Layout Patterns section | Todo 3.4 |
| `references/presentation_design_language.md` | modified | Expanded Rules section from 9 rules to 21 rules organized as Technical (6), Content (12), Process (3). Added Common Failure Modes table with 6 named failures and corrections. | Todo 3.1 |

---

## Phase 4 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `SKILL.md` | modified | Flow 6 (Discussion): replaced "max 5 questions" with "ONE question per turn" for interactive discussions, with reference to B1 in hard_rules.md | Todo 4.5 (moved from Phase 0) |
| `SKILL.md` | modified | Flow 7 (Present): expanded mandatory reading to include gold standard README, added bullet/nav requirements to process steps, added diagram-as-own-slide step, referenced design language spec for full 21 rules | Todo 4.3 |
| `SKILL.md` | modified | Added Sub-Singularities section between Flow 7 and Sibling Skills: overview, when to create, load references, key rules, worked example pointer | Todo 4.1 |
| `SKILL.md` | modified | Flow 3 (Process Source): added question 3 routing team meetings to sub-singularity, added team meeting reference loading | Todo 4.2 |
| `SKILL.md` | modified | Flow 1 (New Engagement): added step 4 offering team sub-singularity creation at engagement start | Todo 4.4 |
| `scripts/singularity_stop.py` | modified | Added Check 5: gold standard deck exists if presentations exist. Added Check 6: nested_singularity.md exists if sub-singularity folders exist. Added Check 7: back button verification on chart files. | Todo 4.6 |

---

## Phase 5 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `references/mermaid_design_standards.md` | added | Complete mermaid visual standards: two theme palettes (blue for slides, purple for deliverables), 9-category semantic color palette for clusters/nodes, multi-line node formatting, line style conventions, layout conventions, CSS overrides, async rendering pattern, standalone chart file pattern, 5 diagram type patterns (architecture, workflow, ecosystem, data flow, decision tree), quality checklist | Todo 5.1, 5.3, 5.4 |
| `references/presentation_design_language.md` | modified | Updated mermaid reference implementation pointers to gold standards and added cross-reference to mermaid_design_standards.md | Todo 5.3 |
| `SKILL.md` | modified | Flow 7 step 5: added instruction to read mermaid_design_standards.md when diagrams are needed | Todo 5.5 |
| `references/complete_structure.md` | modified | Added mermaid_design_standards.md to skill file structure tree | Completeness |

**Note on gold standard charts (Todo 5.2):** The master to-do called for 5 diagram type gold standards. Currently only `example_ecosystem_diagram.html` exists. Additional types will become gold standards when produced from real engagement work.

## Phase 6 Changes

| File | Change | Intent | Source |
|------|--------|--------|--------|
| `references/mermaid_shape_library.md` | added | Quick-reference menu: 14 classic shapes, 18+ v11 shapes, all arrow types, text formatting, bullet characters, 25 FA icons for architecture diagrams, classDef properties, edge styling, diagram types, post-render techniques, decision guide | Phase 6 visual polish |
| `references/mermaid_design_standards.md` | existing | Already created in Phase 5 — color palettes, theme init, layout conventions, quality checklist | Phase 5 |
| `assets/design/gold_standards/charts/example_ecosystem_diagram.html` | replaced | Updated gold standard chart with v5 (mermaid v11, FA icons, bullets, bordered cluster labels, semantic shapes, classDef) replacing the v1 baseline | Phase 6 |
| `references/complete_structure.md` | modified | Added mermaid_shape_library.md to the skill file tree | Phase 6 |

---

## For the Receiving Session (Master Skill Repo)

When syncing this round's changes to the master repository:

1. Read this change log to understand scope and intent.
2. Read the synthesis document at `00_synthesis.md` for the underlying rules and patterns.
3. Read the master to-do list at `sources/07_master_todo_list_2026-04-13.md` for the phased plan.
4. Diff the working-copy skill at `.claude/skills/singularity/` in this repo against the master repo's version.
5. Apply changes as appropriate, preserving master repo conventions.
6. Validate that no master repo features were accidentally removed (this working copy has only seen the additions, not any unrelated master changes).
