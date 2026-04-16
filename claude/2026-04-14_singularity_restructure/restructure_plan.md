# Singularity Skill Folder Restructure Plan

**Date:** 2026-04-14
**Status:** DRAFT — awaiting Colin's review and approval
**Scope:** Reorganize the internal folder structure of `.claude/skills/singularity/`

---

## Guiding Principle

Organize by purpose. The skill contains three kinds of content that are currently tangled across `references/` and `assets/`:

1. **Reference docs** — Instructions for how the skill operates (methodology, rules, workflows)
2. **Gold standards** — Finished examples of what good output looks like, organized by output category
3. **Working resources** — Templates (fill-in starting points), visual reference libraries, and tool prompts

The current `assets/` directory mixes gold standards with templates, visual references, and prompts under layers of nesting (`assets/design/gold_standards/...`). The current `references/` directory mixes instructional docs with complete engagement snapshots containing 67+ files. This plan separates them.

---

## Proposed Folder Structure

```
.claude/skills/singularity/
│
├── SKILL.md                                    # Skill definition, all flows
│
├── scripts/                                    # Executable scripts
│   ├── singularity_stop.py                     # Stop hook (artifact checks)
│   ├── format_transcript.py                    # Raw transcript formatter
│   └── html_to_pdf.py                          # HTML to PDF conversion
│
├── references/                                 # INSTRUCTIONS — how the skill works
│   ├── hard_rules.md                           # B1-B16 behavioral rules (mandatory read)
│   ├── blockchain_methodology.md               # Core append-only methodology
│   ├── folder_structure.md                     # Engagement folder spec + sub-singularity layout
│   ├── document_processing.md                  # How to process each source type
│   ├── people_tracking.md                      # Dual system: per-set docs + org chart
│   ├── agent_architecture.md                   # Agent prompts, parallelization, permissions
│   ├── deliverables_pipeline.md                # Client-facing output rules and workflow
│   ├── pricing_workflow.md                     # Pricing questionnaire and Excel handoff
│   ├── session_continuity.md                   # Handoffs between sessions
│   ├── nested_singularity.md                   # Sub-singularity pattern and rules
│   ├── team_meeting_processing.md              # Team meeting standard passes methodology
│   ├── tracking_folder_pattern.md              # Living tracking docs pattern
│   ├── presentation_design_language.md         # Slide generation design system (21 rules)
│   ├── mermaid_design_standards.md             # Diagram visual standards and patterns
│   ├── mermaid_shape_library.md                # Quick-reference text menu of shapes/arrows/icons
│   ├── mermaid_flowchart_learnings.md          # Flowchart learnings (copied from sephora/qa_qe_playwright/planning/)
│   ├── mermaid_svg_scaling_research.md         # SVG sizing/scaling for print (copied from sephora/qa_qe_playwright/planning/)
│   ├── playwright_screenshot_research.md       # High-res chart capture for print (copied from sephora/qa_qe_playwright/planning/)
│   ├── enforcement_architecture.md             # Artifact-check enforcement pattern
│   ├── anti_patterns.md                        # AI writing anti-patterns
│   ├── professional_standards.md               # Big Four quality standards
│   ├── bayone_design_spec.md                   # BayOne CSS design system spec
│   ├── bayone_team.md                          # BayOne team directory (moved from .claude/context/)
│   ├── reorganization_guide.md                 # Reorganizing existing folders into Singularity format
│   ├── skill_ecosystem.md                      # Sibling skill integration
│   ├── sales_forge_merger.md                   # Sales-forge deprecation mapping
│   └── complete_structure.md                   # Skill file tree (regenerated LAST after restructure)
│
├── gold_standards/                             # Best available representations of each output format
│   │                                           # Each subfolder has a README explaining contents and usage
│   │
│   ├── deliverables/                           # Client-facing document examples
│   │   ├── README.md                           # What these deliverables demonstrate and how to use them
│   │   ├── problem_restatement.html            # From Lam Research engagement
│   │   ├── information_request.html            # From Lam Research engagement
│   │   ├── preliminary_approach.html           # From Lam Research engagement
│   │   ├── poc_proposal_v5.html                # Concise proposal format
│   │   ├── poc_proposal_v5_detailed.html       # Detailed proposal format
│   │   └── bridge_document_example.md          # Bridge document between sets
│   │
│   ├── presentations/                          # Presentation gold standards, categorized by purpose
│   │   │
│   │   ├── team_status_update/                 # Cisco CI/CD weekly status update (Srinivas deck)
│   │   │   ├── README.md                       # What this deck demonstrates and how to use it
│   │   │   ├── 00_title.html
│   │   │   ├── 01_assigned_items_status.html
│   │   │   ├── 02_discovery_findings_build.html
│   │   │   ├── 02a_build_ecosystem_diagram.html
│   │   │   ├── 03_discovery_findings_webex.html
│   │   │   ├── 04_items_for_discussion.html
│   │   │   ├── 05_access_status.html
│   │   │   ├── 06_next_steps.html
│   │   │   └── charts/
│   │   │       └── build_log_ecosystem.html
│   │   │
│   │   ├── ai_education/                       # AI fundamentals presentation (Masterminds deck)
│   │   │   ├── README.md                       # What this deck demonstrates and how to use it
│   │   │   ├── s0_00_title.html ... s6_01_closing.html  # 25 slides
│   │   │   └── resources/                      # Images referenced by slides
│   │   │
│   │   └── capabilities_pitch/                 # BayOne AI capabilities pitch (Ariat foundational)
│   │       ├── README.md                       # What this deck demonstrates and how to use it
│   │       ├── slide_01_ai_strategy_innovation.html
│   │       ├── slide_02_enterprise_ai_solutions.html
│   │       └── slide_03_quality_engineering.html
│   │
│   ├── charts/                                 # Standalone chart/diagram examples
│   │   ├── README.md                           # What these charts demonstrate and how to use them
│   │   └── ecosystem_diagram.html              # Mermaid ecosystem diagram pattern
│   │
│   └── knowledge_transfer/                     # Document-with-embedded-charts pattern
│       ├── README.md                           # What this example demonstrates and how to use it
│       ├── session_0_platform_overview.html     # Main doc with inline diagrams + full-screen links
│       └── charts/                             # Standalone full-screen chart files with back buttons
│           ├── architecture_overview.html
│           ├── candidate_data_flow.html
│           └── fishbone_apps.html
│
├── layout_examples/                            # VISUAL VOCABULARY — unique slide layout patterns
│   ├── README.md                               # Index: describes each layout with visual representation
│   ├── title.html                              # Dark full-bleed centered title (from Masterminds)
│   ├── agenda.html                             # Horizontal section card row (from Masterminds)
│   ├── profile.html                            # Split panel: photo left, highlights right (from Masterminds)
│   ├── split_concept.html                      # Split panel: explanation left, detail right (from Masterminds)
│   ├── three_column.html                       # Three-column card grid (from Masterminds)
│   ├── grid_takeaway.html                      # Card grid with dark takeaway bar (from Masterminds)
│   ├── closing.html                            # Dark full-bleed closing/Q&A (from Masterminds)
│   └── chevron_flow_detail.html                # Chevron process bar + detail card grid (from Ariat)
│
├── worked_examples/                            # COMPLETE ENGAGEMENT SNAPSHOTS
│   │
│   ├── lam_research/                           # Full engagement workflow (Lam Research IP Protection)
│   │   ├── org_chart.md
│   │   ├── source/                             # Raw transcripts (3 files)
│   │   ├── research/                           # Full blockchain chain (27 files across 3 sets + bridge)
│   │   ├── deliverables/                       # Kept intact including HTMLs that also appear in gold_standards
│   │   └── planning/                           # Session handoffs, skill notes, skill spec archive
│   │
│   └── cisco_team/                             # Team sub-singularity (Cisco CI/CD team meetings)
│       ├── README.md                           # What this example demonstrates
│       ├── cross_reference.md                  # Maps team sets to parent engagement sets
│       ├── research/                           # Independent blockchain chain (6 files)
│       └── tracking/                           # Living docs: action_items, blockers, decisions
│
├── templates/                                  # FILL-IN STARTING POINTS
│   ├── methodology_template.md                 # Template for 00_methodology docs (has <DATE>, <CLIENT> placeholders)
│   ├── ProjectCostingTemplate.xlsx             # Excel pricing workbook
│   └── excel_template_prompt.md                # Prompt for regenerating the xlsx from scratch
│
└── mermaid_shape_library/                      # BROWSABLE VISUAL REFERENCE (8 HTML files)
    ├── 01_classic_shapes.html
    ├── 02_v11_shapes.html
    ├── 03_arrows_and_edges.html
    ├── 04_text_formatting.html
    ├── 05_icons_reference.html
    ├── 06_classdef_styling.html
    ├── 07_subgraphs_and_layout.html
    └── 08_diagram_types_gallery.html
```

---

## What Each Top-Level Directory Is For

### `scripts/`
Executable Python scripts that the skill and stop hook use. Unchanged from current structure.

### `references/`
Instructional documents that tell the skill how to operate. Every file here answers a "how do I..." or "what are the rules for..." question. This is what the previous session's `references/` was meant to be, but it got cluttered with engagement snapshots. Under this plan, it contains only docs — no subdirectories with nested file trees.

Two additions: `bayone_design_spec.md` moves here from `assets/design/` (it's a specification, not example output), and `bayone_team.md` moves here from `.claude/context/` (self-contained principle trumps the speculative cross-skill sharing that never materialized). The original `.claude/context/bayone_team.md` gets deleted.

### `gold_standards/`
The best available representations of each output format, using real production-quality content. Gold standards can be complete decks, single HTML documents, individual slides, or any other format the skill produces. They are categorized by purpose — what situation calls for that output. Each subfolder has a README explaining what files are there and how they're meant to be used. The skill must update these READMEs if the files change.

- **`deliverables/`** — client-facing documents (proposals, information requests, problem restatements, bridge docs)
- **`presentations/`** — presentation gold standards categorized by purpose: `team_status_update/` (Cisco Srinivas deck), `ai_education/` (Masterminds deck, copied from `claude/2026-03-31_masterminds/content/`), `capabilities_pitch/` (Ariat foundational slides, copied from `ariat/deliverables/2026-03-03_slides/foundational/`)
- **`charts/`** — standalone mermaid diagram examples
- **`knowledge_transfer/`** — document-with-embedded-charts pattern (the TalentAI session showing inline diagrams with full-screen viewer links)

### `layout_examples/`
Individual slides extracted from across all decks, each showing a unique layout pattern exactly once. These are visual vocabulary for building new slides — when you need a split panel or a chevron flow, you browse these to find the right pattern. A README serves as an index describing each layout with enough detail to pick the right one without opening every file. Sources include the Masterminds deck and the Ariat foundational slides.

### `worked_examples/`
Complete engagement snapshots showing the full Singularity workflow end-to-end. Worked examples answer "what does an entire engagement's research library look like after processing 3 source documents?" Some files in worked examples may also appear in gold_standards — that's expected, since gold standards often originate from real engagement output.

Named descriptively (`lam_research/`, `cisco_team/`) instead of generically (`worked_example/`, `worked_example_team/`).

### `templates/`
Files with literal placeholders that the skill fills in when creating new content. There are currently two:
- **`methodology_template.md`** — Used for every new engagement's `00_methodology_<date>.md`. Contains `<DATE>`, `<CLIENT_NAME>`, `<OPPORTUNITY_DESCRIPTION>` placeholders plus the full methodology boilerplate.
- **`ProjectCostingTemplate.xlsx`** — Excel workbook for pricing engagements. Contains sample data that users replace with real project details.

The `excel_template_prompt.md` lives here too — it's the prompt for regenerating the xlsx from scratch if needed. `proposal_template.html` was deleted — the gold standard deliverables serve as better starting points because they show content structure, not just an empty CSS shell.

### `mermaid_shape_library/`
Eight browsable HTML files that render live mermaid.js examples — every shape, arrow, icon, styling option, and diagram type. This is reference material for understanding what's possible, not example output or a template. It's at the top level because it's a self-contained visual resource that doesn't fit cleanly under references (which are markdown docs) or gold standards (which are examples of skill output).

---

## What Gets Removed

| File | Reason |
|------|--------|
| `references/asshole.txt` | Not a skill file |
| `references/image.png` | Not a skill file |
| `assets/templates/proposal_template.html` | Obsolete — gold standards serve as better starting points |
| `.claude/context/bayone_team.md` | Moved into skill at `references/bayone_team.md` (self-contained principle) |
| Empty directories (`decisions/`, `progress/`, etc.) | See Decision Point 2 |

---

## Decision Points for Colin

### Decision Point 1: Duplicate Deliverables in Worked Example — RESOLVED

**Decision:** Keep both copies. It is natural that worked example deliverables also appear in gold standards — that's how gold standards originate. The worked example copy shows what a complete engagement looks like. The gold standards copy makes it findable by category. Both purposes are valid.

### Decision Point 2: Empty Directories in Worked Examples — RESOLVED

**Decision:** Keep them. They're part of the folder structure.

### Decision Point 3: Archival `planning/skill_spec/` in Lam Research Worked Example — RESOLVED

**Decision:** Keep them. They're part of the worked example.

### Decision Point 4: Layout Example File Naming — RESOLVED

**Decision:** Drop the `example_` prefix. `title.html`, `agenda.html`, `split_concept.html`, etc.

---

## Path Update Requirements

After the restructure, every file path reference in the skill must be updated. This is a complete list of files that contain internal skill paths:

| File | What It References |
|------|-------------------|
| `SKILL.md` | Gold standards, templates, slide examples, design spec, worked examples, mermaid shape library |
| `scripts/singularity_stop.py` | Slide examples dir, gold standard presentation dir, hard rules path |
| `references/presentation_design_language.md` | Gold standard presentations, slide examples, charts |
| `references/mermaid_design_standards.md` | Mermaid shape library path |
| `references/deliverables_pipeline.md` | Gold standard deliverables, design spec, templates |
| `references/skill_ecosystem.md` | Various skill paths |
| `references/complete_structure.md` | Entire tree (regenerate from scratch) |
| `references/nested_singularity.md` | Worked example team path |

The path audit will be the final step — after all moves are complete, before calling the restructure done.

---

## Execution Order

1. Get Colin's approval on this plan and remaining decision points
2. Create the new directory structure
3. Move existing files (gold standards, worked examples, templates, mermaid library)
4. Copy in new gold standards: Masterminds deck from `claude/2026-03-31_masterminds/content/`, Ariat slides from `ariat/deliverables/2026-03-03_slides/foundational/`
5. Create layout_examples/ with extracted patterns and README index
6. Copy mermaid/Playwright reference docs from `sephora/qa_qe_playwright/planning/` into `references/`
7. Move `bayone_team.md` from `.claude/context/` into `references/`
7. Delete `proposal_template.html`, `asshole.txt`, `image.png`, `.claude/context/bayone_team.md`
8. Remove `assets/` directory tree (now empty)
9. Handle remaining decision points (empty dirs, archive)
10. Write README files for each gold_standards subfolder
11. Update all path references in SKILL.md, stop hook, and reference docs
12. Regenerate `complete_structure.md` from actual file system
13. Full path audit: verify every path in every file resolves to a real file

---

## Depth Comparison

| Path | Current Depth | New Depth |
|------|--------------|-----------|
| Team status update chart | `assets/design/gold_standards/presentations/srinivas_status/charts/` (6) | `gold_standards/presentations/team_status_update/charts/` (4) |
| Knowledge transfer chart | `assets/design/gold_standards/knowledge_transfer/charts/` (5) | `gold_standards/knowledge_transfer/charts/` (3) |
| Layout example | `assets/slide_examples/` (2) | `layout_examples/` (1) |
| Standalone chart | `assets/design/gold_standards/charts/` (4) | `gold_standards/charts/` (2) |
| Design spec | `assets/design/bayone_design_spec.md` (2) | `references/bayone_design_spec.md` (1) |
| Mermaid shape library | `assets/mermaid_shape_library/` (2) | `mermaid_shape_library/` (1) |
| BayOne team | `.claude/context/bayone_team.md` (external) | `references/bayone_team.md` (1) |

Maximum depth drops from 6 to 4 (for the presentation deck charts, which inherently need: category > deck > charts). Most paths drop by 2-3 levels.
