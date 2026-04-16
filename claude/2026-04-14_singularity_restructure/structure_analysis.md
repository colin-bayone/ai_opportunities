# Singularity Skill Structure Analysis

**Date:** 2026-04-14
**Purpose:** Observations from exploring the actual file system, with ideas for restructuring.

---

## What I Found

### 1. `assets/` is a grab-bag, not a category

`assets/` contains five unrelated things: templates (3 files), prompts (1 file), slide examples (7 files), mermaid shape library (8 files), and a `design/` subfolder. These have nothing in common except "not reference docs." The `assets/` directory adds a nesting level without providing organizational clarity.

### 2. `design/` is a wrapper around one file and one folder

`assets/design/` contains exactly `bayone_design_spec.md` and `gold_standards/`. It's an intermediate directory with no purpose. Everything under `assets/` is arguably design-related, so `design/` as a subcategory doesn't discriminate.

### 3. Gold standard deliverables are literal duplicates of worked example files

`problem_restatement.html`, `information_request.html`, and `preliminary_approach.html` in `assets/design/gold_standards/` are byte-for-byte identical (confirmed via md5) to the same files in `references/worked_example/deliverables/02_discovery_call_2026-03-12/`. Two copies of three files, no divergence.

### 4. Gold standards mix standalone examples with complete multi-file sets

The gold standards folder contains:
- 6 standalone deliverable examples (read one file, see one pattern)
- 1 complete presentation deck: 10 files + 1 chart (the Srinivas deck)
- 1 complete knowledge transfer session: 1 doc + 3 charts

These serve different purposes. Standalone examples answer "what does a good X look like?" Multi-file sets answer "how do the pieces fit together?" Right now they're thrown in the same bucket with inconsistent depth.

### 5. Three `charts/` directories exist because each gold standard has its own

- `gold_standards/charts/` (1 standalone ecosystem diagram)
- `gold_standards/knowledge_transfer/charts/` (3 chart files)
- `gold_standards/presentations/srinivas_status/charts/` (1 chart file)

This isn't really a naming conflict — it's a structural consequence of each example needing its own charts subfolder. But it makes the tree confusing to read.

### 6. `references/` is 22 flat files with no subcategorization

Everything from behavioral rules to methodology docs to integration guides to worked examples lives under one `references/` directory. Some of these are core to every invocation (hard_rules, blockchain_methodology, folder_structure). Others are loaded only for specific flows (mermaid_design_standards, presentation_design_language). Others are background context that might never be read (sales_forge_merger, reorganization_guide, skill_ecosystem).

### 7. The worked examples contain content that the skill never needs to read at runtime

`worked_example/planning/skill_spec/` has 14 frozen historical files — early drafts of what became the current reference docs. These are archival artifacts from the skill's own design history. They demonstrate what the planning process looked like, but no flow in SKILL.md ever reads them. That's 14 files occupying space in the skill directory with no runtime purpose.

### 8. Five empty directories exist as structural templates

`worked_example/decisions/`, `worked_example/progress/`, `worked_example_team/documents/`, `worked_example_team/planning/`, `worked_example_team/source/`. They show "here's what the folder structure looks like" but contain nothing. This is already communicated by `folder_structure.md`.

### 9. Deepest paths are 7 levels from skill root

`assets/design/gold_standards/presentations/srinivas_status/charts/build_log_ecosystem.html` = 7 directories deep. This is the worst case, but 5-6 level paths are common throughout `gold_standards/`.

### 10. SKILL.md and the stop hook hardcode deep paths

SKILL.md references `assets/design/gold_standards/presentations/srinivas_status/README.md` and `assets/slide_examples/` and `assets/design/bayone_design_spec.md`. The stop hook checks `assets/slide_examples` and `assets/design/gold_standards/presentations/srinivas_status`. Any restructure requires updating all of these.

---

## The Core Problem

The skill has three fundamentally different kinds of content mixed across two top-level directories:

| Kind | Purpose | Currently Lives In |
|------|---------|-------------------|
| **Instructions** — how to do things | Rules, methodology, workflows, standards | `references/` (flat, 22 files) |
| **Examples** — what good output looks like | Gold standard deliverables, worked engagement snapshots | Split between `references/worked_example*/` and `assets/design/gold_standards/` |
| **Resources** — tools used to produce output | Templates, prompts, design spec, shape library, slide examples | Scattered across `assets/` subfolders |

The `assets/` vs `references/` split doesn't map to these categories. Instructions and examples are both in `references/`. Resources and examples are both in `assets/`. The result is that finding "the gold standard for a problem restatement" requires knowing it's under `assets/design/gold_standards/` rather than `references/worked_example/deliverables/` (where the identical file also lives).

---

## Ideas

### Idea: Organize by purpose, not by file type

Three top-level directories under the skill root, one for each kind of content:

- **`references/`** — Instructions only. The 22 reference docs stay here, minus the worked examples which move out.
- **`gold_standards/`** — All example output in one place. Standalone deliverables, the Srinivas deck, the knowledge transfer session, the bridge document example. No duplicates with worked examples.
- **`worked_examples/`** — Full engagement snapshots. Renamed to be descriptive (`lam_research/`, `cisco_team/`). These show the full workflow, not just finished output.

Then the remaining resource files get direct top-level homes without intermediate wrappers:

- **`templates/`** — methodology template, xlsx, proposal template
- **`slide_examples/`** — the 7 example HTML slides
- **`mermaid_shape_library/`** — the 8 browsable HTML reference files
- **`prompts/`** — the excel prompt
- **`design_spec.md`** or keep it in a `design/` folder — the BayOne design spec

### What this solves

- Eliminates `assets/` and `assets/design/` wrappers (2 levels gone from deepest paths)
- Consolidates all gold standards in one location (currently split across two trees)
- Separates worked examples from gold standards (different purposes, currently tangled)
- Makes the reference docs directory cleaner (instructions only, no embedded multi-file examples)
- Deepest path drops from 7 levels to 4 (`gold_standards/srinivas_status/charts/build_log_ecosystem.html`)

### The duplication question

The three Lam Research deliverable HTMLs currently exist in both locations. After restructuring, the gold_standards copy would be canonical. The worked example's deliverables folder could either: (a) not include them and reference the gold_standards versions, or (b) keep them for completeness of the worked example. I lean toward (a) because duplicates create the exact confusion documented in B12, and the worked example's README can explain where to find the deliverables.

---

## What I'm Not Sure About

The knowledge transfer gold standard (`session_0_platform_overview.html` + 3 charts) — this came from the TalentAI project, not from a Singularity engagement. It's in the skill because it demonstrates the correct chart embed pattern. Should it live alongside the Srinivas deck as a gold standard, or does it belong somewhere else?
