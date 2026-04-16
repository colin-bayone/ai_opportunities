# Inventory Script Design and Assumptions

**Script:** `scripts/generate_inventory.py`
**Purpose:** Generates current-state inventory snapshots of any Singularity engagement folder.

---

## What It Produces

All output goes to `<engagement>/inventory/`. Files are overwritten on each run (snapshots, not append-only).

| File | Contents |
|------|----------|
| `master_map.md` | Complete tree of every file in the engagement |
| `markdown_inventory.md` | Tree of `.md` files only |
| `non_markdown_inventory.md` | Tree of all non-`.md` files (HTML, py, xlsx, txt, images, etc.) |
| `folder_descriptions.md` | Tree of folders only, each with a description and last-updated date |
| `sub_<name>.md` | One per sub-singularity (e.g., `sub_team.md`). Only created when sub-singularities exist. |

## Usage

```bash
python3 .claude/skills/singularity/scripts/generate_inventory.py <engagement_path>
```

Accepts absolute or relative paths. Creates `inventory/` if it doesn't exist.

---

## Assumptions the Skill Must Maintain

### 1. Canonical folder descriptions come from `references/folder_structure.md`

The script contains a lookup table of folder descriptions derived from the "Folder Purposes" tables in `folder_structure.md`. **If a folder's purpose changes in `folder_structure.md`, the corresponding entry in `generate_inventory.py` must also be updated.** The lookup table lives in the `FOLDER_DESCRIPTIONS` constant near the top of the script.

Current canonical descriptions:

| Folder | Description |
|--------|-------------|
| `source/` | Raw input files (never modified) |
| `research/` | Blockchain-style research decomposition (append-only) |
| `planning/` | Approach planning, session handoffs, notes |
| `pricing/` | Pricing specs, corrections, cost models |
| `deliverables/` | Client-facing documents (markdown + HTML) |
| `presentations/` | Slide decks, presentation materials |
| `decisions/` | Open questions and agreed decisions |
| `progress/` | Running status tracking |
| `inventory/` | Auto-generated engagement inventory snapshots |
| `archive/` | Pre-restructure historical files |
| `documents/` | Reference documents and extracted materials |
| `tracking/` | Living operational documents (action items, blockers, decisions) |

Folders not in this table get a generic description based on file count.

### 2. Sub-singularity detection relies on `research/00_methodology_*.md`

A folder is identified as a sub-singularity if:
- It is a direct child of the engagement root (sibling of `source/`, `research/`, etc.)
- It contains a `research/` subfolder with at least one file matching `00_methodology_*.md`

This matches the rule from `nested_singularity.md`: every sub-singularity starts with a methodology document. **If the naming convention for methodology files changes, the detection glob in the script must be updated.**

The `inventory/` folder itself is always excluded from sub-singularity consideration.

### 3. `.gitkeep` files are invisible

`.gitkeep` files are excluded from all inventories. They exist only to preserve empty directories in git and carry no information. A folder containing only `.gitkeep` is treated as empty.

### 4. Sort order is alphabetical

Directories and files within each level are sorted alphabetically. Directories are listed before files at each level. This is a display convention — it has no semantic meaning.

### 5. Empty folders are explicitly noted

In `folder_descriptions.md`, empty folders (or folders with only `.gitkeep`) show `(empty)` instead of a last-updated date. In tree views, empty folders appear with no children.

### 6. Last-updated dates are non-recursive

In `folder_descriptions.md`, the "last updated" date for a folder is the most recent file modification timestamp **in that folder only**, not recursively into subfolders. This means a parent folder can show an older date than its children — that is correct and intentional. It tells you when files in *that specific folder* were last touched.

### 7. The `inventory/` folder excludes itself

When generating inventories, the script skips the `inventory/` directory to avoid self-referential output. The inventory documents what exists in the engagement — not the inventory itself.

---

## When to Regenerate

Run the script after any of these events:
- New source material added
- New research set completed
- Deliverables created or updated
- Sub-singularity created
- Any file moves or reorganization

The script is idempotent — safe to run at any time. Output is always a fresh snapshot.
