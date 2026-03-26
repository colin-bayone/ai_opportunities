"""
Generate Markdown Summaries per Category

Reads the phoenix_catalog.json and generates markdown summary files
for each category. These files are useful for LLM context when working
in a specific category.

Usage:
    poetry run python claude/2025-12-16_phoenix-theme-skill/scripts/03_generate_markdown_summaries.py

Output: One markdown file per category in data/summaries/
"""

import json
from pathlib import Path
from collections import defaultdict

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SCRIPT_DIR / "data"
CATALOG_FILE = DATA_DIR / "phoenix_catalog.json"
SUMMARIES_DIR = DATA_DIR / "summaries"


def load_catalog():
    """Load the catalog JSON."""
    with open(CATALOG_FILE, 'r') as f:
        return json.load(f)


def group_by_category(pages):
    """Group pages by category."""
    groups = defaultdict(list)
    for page in pages:
        groups[page['category']].append(page)
    return dict(groups)


def generate_category_summary(category: str, pages: list, meta: dict) -> str:
    """Generate markdown content for a category."""
    lines = [
        f"# Phoenix Theme: {category.title()}",
        "",
        f"**Version:** {meta.get('version', 'unknown')}",
        f"**Base URL:** {meta.get('base_url', '')}",
        f"**Total Pages in Category:** {len(pages)}",
        "",
        "---",
        "",
    ]

    # Group by subcategory
    by_subcat = defaultdict(list)
    for page in pages:
        by_subcat[page.get('subcategory', 'misc')].append(page)

    for subcat in sorted(by_subcat.keys()):
        subcat_pages = by_subcat[subcat]
        lines.append(f"## {subcat.replace('_', ' ').title()}")
        lines.append("")

        for page in subcat_pages:
            title = page.get('title', 'Untitled')
            url = page.get('url', '')
            description = page.get('description', '')
            components = page.get('component_names', [])

            lines.append(f"### [{title}]({url})")
            lines.append("")

            if description:
                lines.append(f"**Description:** {description}")
                lines.append("")

            if components:
                lines.append(f"**Components:** {', '.join(components)}")
                lines.append("")

            lines.append(f"**Path:** `{page.get('path', '')}`")
            lines.append("")

            if page.get('tags'):
                lines.append(f"**Tags:** {', '.join(page['tags'])}")
                lines.append("")

            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main():
    print("=" * 60)
    print("Phoenix Markdown Summary Generator")
    print(f"Input: {CATALOG_FILE}")
    print(f"Output: {SUMMARIES_DIR}/")
    print("=" * 60)

    # Load catalog
    catalog = load_catalog()
    meta = catalog.get('meta', {})
    pages = catalog.get('pages', [])

    print(f"\nLoaded {len(pages)} pages")

    # Group by category
    by_category = group_by_category(pages)
    print(f"Found {len(by_category)} categories")

    # Ensure output directory exists
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)

    # Generate summaries
    for category, cat_pages in sorted(by_category.items()):
        filename = f"phoenix_{category}.md"
        filepath = SUMMARIES_DIR / filename

        content = generate_category_summary(category, cat_pages, meta)

        with open(filepath, 'w') as f:
            f.write(content)

        print(f"  {filename}: {len(cat_pages)} pages")

    print(f"\nGenerated {len(by_category)} markdown files in {SUMMARIES_DIR}")

    # Also generate a quick reference index
    index_lines = [
        "# Phoenix Theme v1.23.0 - Quick Reference Index",
        "",
        f"**Total Pages:** {len(pages)}",
        f"**Base URL:** {meta.get('base_url', '')}",
        "",
        "## Categories",
        "",
    ]

    for category in sorted(by_category.keys()):
        count = len(by_category[category])
        index_lines.append(f"- **{category.title()}**: {count} pages - [phoenix_{category}.md](phoenix_{category}.md)")

    index_lines.extend([
        "",
        "## High-Value Starting Points",
        "",
        "| URL | Purpose |",
        "|-----|---------|",
        f"| {meta.get('base_url', '')}index.html | Home/Overview |",
        f"| {meta.get('base_url', '')}widgets.html | Single most helpful - various widgets |",
        f"| {meta.get('base_url', '')}modules/echarts/ | Apache ECharts (built into theme) |",
        f"| {meta.get('base_url', '')}modules/components/ | UI Components |",
        f"| {meta.get('base_url', '')}modules/forms/ | Form Components |",
        "",
    ])

    index_file = SUMMARIES_DIR / "00_index.md"
    with open(index_file, 'w') as f:
        f.write("\n".join(index_lines))

    print(f"  00_index.md: Quick reference index")


if __name__ == '__main__':
    main()
