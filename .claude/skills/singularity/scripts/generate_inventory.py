#!/usr/bin/env python3
"""
Generate inventory files for a Singularity engagement folder.

Produces markdown files in tree-view format documenting what exists in the engagement.
Output goes to <engagement>/inventory/ and overwrites on each run (snapshots).

Usage:
    python3 generate_inventory.py <engagement_path>

See references/inventory_design.md for design assumptions and maintenance notes.
"""

import argparse
import glob
import os
import sys
from datetime import datetime
from pathlib import Path

# Canonical folder descriptions from references/folder_structure.md.
# If folder purposes change there, update this table.
FOLDER_DESCRIPTIONS = {
    "source": "Raw input files (never modified)",
    "research": "Blockchain-style research decomposition (append-only)",
    "planning": "Approach planning, session handoffs, notes",
    "pricing": "Pricing specs, corrections, cost models",
    "deliverables": "Client-facing documents (markdown + HTML)",
    "presentations": "Slide decks, presentation materials",
    "decisions": "Open questions and agreed decisions",
    "progress": "Running status tracking",
    "inventory": "Auto-generated engagement inventory snapshots",
    "archive": "Pre-restructure historical files",
    "documents": "Reference documents and extracted materials",
    "tracking": "Living operational documents (action items, blockers, decisions)",
}

SKIP_FILES = {".gitkeep"}
SKIP_DIRS = {"inventory"}


def is_sub_singularity(dirpath):
    """Check if a directory is a sub-singularity (has research/00_methodology_*.md)."""
    return bool(glob.glob(os.path.join(dirpath, "research", "00_methodology_*.md")))


def get_last_updated(dirpath):
    """Get the most recent file modification date in a directory (non-recursive).

    Returns a date string (YYYY-MM-DD) or None if the folder is empty/only .gitkeep.
    """
    latest = None
    try:
        for entry in os.scandir(dirpath):
            if entry.is_file() and entry.name not in SKIP_FILES:
                mtime = entry.stat().st_mtime
                if latest is None or mtime > latest:
                    latest = mtime
    except PermissionError:
        return None
    if latest is None:
        return None
    return datetime.fromtimestamp(latest).strftime("%Y-%m-%d")


def walk_tree(root, filter_fn=None):
    """Walk a directory tree and return a nested structure.

    Args:
        root: Path to the root directory.
        filter_fn: Optional function(filepath) -> bool. If provided, only files
                   where filter_fn returns True are included. Directories are
                   included if they contain at least one matching file (recursively).

    Returns:
        List of (name, children_or_none) tuples. children_or_none is None for
        files and a list for directories.
    """
    entries = []
    try:
        items = sorted(os.scandir(root), key=lambda e: e.name)
    except PermissionError:
        return entries

    dirs = []
    files = []
    for item in items:
        if item.name in SKIP_FILES:
            continue
        if item.is_dir(follow_symlinks=False):
            if item.name in SKIP_DIRS:
                continue
            dirs.append(item)
        elif item.is_file():
            files.append(item)

    # Directories first, then files (both alphabetical)
    for d in dirs:
        children = walk_tree(d.path, filter_fn=filter_fn)
        if filter_fn is not None and not children:
            # Skip empty dirs when filtering
            continue
        entries.append((d.name, children))

    for f in files:
        if filter_fn is not None and not filter_fn(f.path):
            continue
        entries.append((f.name, None))

    return entries


def render_tree(entries, prefix=""):
    """Render a nested tree structure into lines with box-drawing characters.

    Args:
        entries: List of (name, children_or_none) from walk_tree.
        prefix: Current indentation prefix for nested levels.

    Returns:
        List of strings (lines), without trailing newlines.
    """
    lines = []
    for i, (name, children) in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        display = name + "/" if children is not None else name
        lines.append(f"{prefix}{connector}{display}")
        if children is not None:
            extension = "    " if is_last else "│   "
            lines.extend(render_tree(children, prefix + extension))
    return lines


def walk_folders_only(root, depth=0):
    """Walk directory tree collecting folder info for descriptions.

    Returns list of (name, depth, description, last_updated, children) tuples.
    """
    entries = []
    try:
        items = sorted(os.scandir(root), key=lambda e: e.name)
    except PermissionError:
        return entries

    for item in items:
        if not item.is_dir(follow_symlinks=False):
            continue
        if item.name in SKIP_FILES or item.name in SKIP_DIRS:
            continue

        desc = FOLDER_DESCRIPTIONS.get(item.name)
        if desc is None:
            if is_sub_singularity(item.path):
                desc = f"Sub-singularity: {item.name}"
            else:
                # Count non-gitkeep files
                try:
                    file_count = sum(
                        1
                        for e in os.scandir(item.path)
                        if e.is_file() and e.name not in SKIP_FILES
                    )
                except PermissionError:
                    file_count = 0
                desc = f"Contains {file_count} file{'s' if file_count != 1 else ''}"

        last_updated = get_last_updated(item.path)
        children = walk_folders_only(item.path, depth + 1)
        entries.append((item.name, depth, desc, last_updated, children))

    return entries


def render_folder_descriptions(entries, prefix=""):
    """Render folder descriptions with tree connectors.

    Returns list of strings (lines).
    """
    lines = []
    for i, (name, _depth, desc, last_updated, children) in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "

        date_part = f"(last updated: {last_updated})" if last_updated else "(empty)"
        line = f"{prefix}{connector}{name}/".ljust(40) + f"— {desc} {date_part}"
        lines.append(line)

        if children:
            extension = "    " if is_last else "│   "
            lines.extend(render_folder_descriptions(children, prefix + extension))

    return lines


def detect_sub_singularities(engagement_path):
    """Find sub-singularities at the engagement root level.

    Returns list of directory names that are sub-singularities.
    """
    subs = []
    standard_dirs = set(FOLDER_DESCRIPTIONS.keys()) | SKIP_DIRS
    try:
        for item in sorted(os.scandir(engagement_path), key=lambda e: e.name):
            if not item.is_dir(follow_symlinks=False):
                continue
            if item.name in standard_dirs:
                continue
            if is_sub_singularity(item.path):
                subs.append(item.name)
    except PermissionError:
        pass
    return subs


def engagement_label(engagement_path):
    """Extract a human-readable label like 'cisco/cicd' from the path."""
    parts = Path(engagement_path).resolve().parts
    if len(parts) >= 2:
        return f"{parts[-2]}/{parts[-1]}"
    return parts[-1] if parts else "engagement"


def write_inventory_file(filepath, title, label, lines):
    """Write an inventory file with standard header."""
    today = datetime.now().strftime("%Y-%m-%d")
    with open(filepath, "w") as f:
        f.write(f"# {title} — {label}\n\n")
        f.write(f"Generated: {today}\n\n")
        f.write(f"{label}/\n")
        for line in lines:
            f.write(line + "\n")


def generate_all(engagement_path):
    """Generate all inventory files for an engagement."""
    engagement_path = os.path.abspath(engagement_path)
    if not os.path.isdir(engagement_path):
        print(f"Error: {engagement_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    label = engagement_label(engagement_path)
    inv_dir = os.path.join(engagement_path, "inventory")
    os.makedirs(inv_dir, exist_ok=True)

    # 1. Master map — all files
    tree = walk_tree(engagement_path)
    lines = render_tree(tree)
    write_inventory_file(
        os.path.join(inv_dir, "master_map.md"), "Master Map", label, lines
    )
    print(f"  master_map.md ({len(lines)} lines)")

    # 2. Markdown inventory — .md files only
    md_tree = walk_tree(engagement_path, filter_fn=lambda p: p.endswith(".md"))
    md_lines = render_tree(md_tree)
    write_inventory_file(
        os.path.join(inv_dir, "markdown_inventory.md"),
        "Markdown Inventory",
        label,
        md_lines,
    )
    print(f"  markdown_inventory.md ({len(md_lines)} lines)")

    # 3. Non-markdown inventory — everything except .md
    non_md_tree = walk_tree(engagement_path, filter_fn=lambda p: not p.endswith(".md"))
    non_md_lines = render_tree(non_md_tree)
    write_inventory_file(
        os.path.join(inv_dir, "non_markdown_inventory.md"),
        "Non-Markdown Inventory",
        label,
        non_md_lines,
    )
    print(f"  non_markdown_inventory.md ({len(non_md_lines)} lines)")

    # 4. Folder descriptions
    folder_entries = walk_folders_only(engagement_path)
    desc_lines = render_folder_descriptions(folder_entries)
    write_inventory_file(
        os.path.join(inv_dir, "folder_descriptions.md"),
        "Folder Descriptions",
        label,
        desc_lines,
    )
    print(f"  folder_descriptions.md ({len(desc_lines)} lines)")

    # 5. Sub-singularity inventories
    subs = detect_sub_singularities(engagement_path)
    for sub_name in subs:
        sub_path = os.path.join(engagement_path, sub_name)
        sub_tree = walk_tree(sub_path)
        sub_lines = render_tree(sub_tree)
        sub_label = f"{label}/{sub_name}"
        filename = f"sub_{sub_name}.md"
        write_inventory_file(
            os.path.join(inv_dir, filename),
            f"Sub-Singularity: {sub_name}",
            sub_label,
            sub_lines,
        )
        print(f"  {filename} ({len(sub_lines)} lines)")

    total = 4 + len(subs)
    sub_msg = f" + {len(subs)} sub-singularity file{'s' if len(subs) != 1 else ''}" if subs else ""
    print(f"\nGenerated {total} inventory files{sub_msg} in {inv_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate inventory files for a Singularity engagement folder."
    )
    parser.add_argument(
        "engagement_path", help="Path to the engagement root folder"
    )
    args = parser.parse_args()
    generate_all(args.engagement_path)


if __name__ == "__main__":
    main()
