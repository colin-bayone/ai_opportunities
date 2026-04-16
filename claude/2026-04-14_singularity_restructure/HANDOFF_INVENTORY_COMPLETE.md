# Handoff: Inventory Scripts — Complete

**From:** Session that built the inventory scripts (2026-04-16)
**To:** Future Singularity skill sessions
**Status:** Complete and tested

---

## What Was Built

A Python script that generates inventory snapshots of any Singularity engagement folder. The script walks the engagement directory tree and produces markdown files in tree-view format (`├──`/`└──` style) documenting everything that exists.

### Files Created

| File | Location | Purpose |
|------|----------|---------|
| `generate_inventory.py` | `.claude/skills/singularity/scripts/` | The inventory script itself |
| `inventory_design.md` | `.claude/skills/singularity/references/` | Design doc with all assumptions the skill must maintain — **read this** |

### Files Updated

| File | What Changed |
|------|-------------|
| `references/folder_structure.md` | Added `inventory/` to the canonical engagement tree diagram and folder purposes table |

---

## How the Script Works

### Usage

```bash
python3 .claude/skills/singularity/scripts/generate_inventory.py <engagement_path>
```

Takes an absolute or relative path to an engagement root (e.g., `cisco/cicd/`). Creates `<engagement>/inventory/` if it doesn't exist. Overwrites all output files on each run — these are snapshots, not append-only.

### Output Files

The script produces these files in `<engagement>/inventory/`:

| File | Contents |
|------|----------|
| `master_map.md` | Complete tree of every file in the engagement |
| `markdown_inventory.md` | Tree of all `.md` files only |
| `non_markdown_inventory.md` | Tree of all non-`.md` files (HTML, py, xlsx, images, etc.) |
| `folder_descriptions.md` | Tree of folders only, each with a brief description and last-updated date |
| `sub_<name>.md` | One per sub-singularity (e.g., `sub_team.md`). Only created when sub-singularities exist. |

### Script Structure

Single file, no external dependencies. Key functions:

| Function | What It Does |
|----------|-------------|
| `walk_tree(root, filter_fn)` | Recursively walks directory, returns nested structure. Optional filter for md/non-md splits. |
| `render_tree(entries, prefix)` | Converts nested structure into `├──`/`└──` formatted lines |
| `detect_sub_singularities(path)` | Finds folders at engagement root containing `research/00_methodology_*.md` |
| `walk_folders_only(root)` | Like `walk_tree` but folders only, with descriptions and last-updated dates |
| `describe_folder(name)` | Looks up canonical description from `FOLDER_DESCRIPTIONS` constant |
| `generate_all(path)` | Orchestrator: creates inventory dir, calls all generators, writes all files |

### Sub-Singularity Detection

A folder is a sub-singularity if it:
1. Lives at the engagement root level (sibling of `source/`, `research/`, etc.)
2. Contains `research/00_methodology_*.md`

This is derived from `references/nested_singularity.md` — every sub-singularity must have a methodology doc. When detected, the folder gets labeled "Sub-singularity: <name>" in folder descriptions, and a separate `sub_<name>.md` focused inventory is generated.

### What Gets Excluded

- `.gitkeep` files — invisible in all output
- `inventory/` folder — excluded from its own output (no self-reference)
- Nothing else — the script inventories everything, including `archive/`

---

## What Was Tested

Ran against all 3 test engagements specified in the original handoff:

### 1. Lam Research IP Protection (`lam_research/ip_protection/`)

- Full engagement with source, research (8 sets + bridge docs), deliverables (HTML + md), presentations, planning, pricing, archive
- No sub-singularity
- **Result:** 4 inventory files generated. 185-line master map. All folders described correctly with canonical descriptions. Archive contents fully enumerated.

### 2. Cisco CI/CD (`cisco/cicd/`)

- Engagement with a `team/` sub-singularity
- Has source, research (10 sets), deliverables, presentations (srinivas status deck with charts subfolder), documents (PDF extractions), and the team sub-singularity with its own research chain, tracking docs, and week/day/person source organization
- **Result:** 5 inventory files generated (4 standard + `sub_team.md`). Sub-singularity auto-detected. `team/` labeled as "Sub-singularity: team" in folder descriptions. Week/day/person source folder structure renders correctly in trees. 411-line master map.

### 3. Sephora QA/QE Playwright (`sephora/qa_qe_playwright/`)

- Engagement with deliverables (including architecture diagram experiments subfolder and charts subfolder), planning, research
- No sub-singularity
- **Result:** 4 inventory files generated. 87-line master map. Empty folders (decisions, pricing, progress, presentations) correctly show `(empty)` in folder descriptions.

### Edge Cases Verified

- Empty folders containing only `.gitkeep` → shown as empty, `.gitkeep` not listed
- Nested subfolders within deliverables (charts/, architecture_diagram_experiments/) → correctly rendered
- Week/day/person source folder structure → correctly rendered with all nesting levels
- Folders not in the canonical description table → fall back to "Contains N files" description
- Sub-singularities in folder descriptions → labeled as such, not just "Contains N files"

---

## Assumptions the Skill Must Maintain

Full details in `references/inventory_design.md`. The critical ones:

1. **Folder descriptions stay in sync.** The script has a `FOLDER_DESCRIPTIONS` constant derived from `references/folder_structure.md`. If folder purposes change in that doc, the constant must be updated too.

2. **Methodology file naming.** Sub-singularity detection depends on `research/00_methodology_*.md`. If the naming convention changes, the glob in `detect_sub_singularities()` must be updated.

3. **`inventory/` is in `SKIP_DIRS`.** The script excludes itself. If other directories should be excluded in the future, add them to the `SKIP_DIRS` set.

---

## TODO Updates

This work completes **Phase 8** from `TODO.md`:

- [x] Discuss and agree on exact requirements (done in previous session)
- [x] Create handoff document with full context (HANDOFF_INVENTORY_SCRIPTS.md)
- [x] Create kickoff prompt for the new session (KICKOFF_INVENTORY_SCRIPTS.md)
- [x] Build and test the scripts (this session)
- [x] Document assumptions for the skill (references/inventory_design.md)
- [x] Update folder_structure.md with inventory/ folder
