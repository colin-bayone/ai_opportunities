# Kickoff: Build Singularity Engagement Inventory Scripts

You are picking up a task from a previous session that just completed a major restructure of the Singularity skill. Your job is to build Python scripts that generate inventory files for Singularity engagement folders.

## Step 1: Read the Handoff

Read `claude/2026-04-14_singularity_restructure/HANDOFF_INVENTORY_SCRIPTS.md` for full requirements, output format, test engagements, and behavioral rules.

## Step 2: Read the Skill Context

Read these files to understand the Singularity skill and engagement structure:
1. `.claude/skills/singularity/references/hard_rules.md` — Behavioral rules (mandatory)
2. `.claude/skills/singularity/references/folder_structure.md` — Canonical engagement folder structure
3. `.claude/skills/singularity/references/nested_singularity.md` — Sub-singularity pattern

## Step 3: Explore a Real Engagement

Before writing any code, explore at least one of the test engagements listed in the handoff. Look at the actual folder structure, file types, and naming conventions. This grounds your script design in reality.

## Step 4: Propose Before Building

Propose the script structure (single script vs module, function breakdown, output format details) and get approval before writing code. Show a sample of what the tree-view output would look like for one of the test engagements.

## Step 5: Build and Test

Build the script(s), run against all 3 test engagements, and verify output. Fix any issues.

## Step 6: Update Skill Docs

Add `inventory/` to `references/folder_structure.md` as part of the canonical engagement structure.

## Ground Rules

- One question at a time in discussion (B1)
- Do not invent requirements not in the handoff (B2)
- Read files before describing them (B4)
- Propose structure before producing (B7)
- Use the TODO at `claude/2026-04-14_singularity_restructure/TODO.md` to track your progress
