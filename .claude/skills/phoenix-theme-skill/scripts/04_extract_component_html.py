"""
Phoenix Component HTML Extractor

Extracts the actual HTML code for components from Phoenix documentation pages.
The Phoenix docs show both rendered previews AND the source code - this script
captures the source code so agents can copy it directly.

Output: data/components/ folder with HTML files organized by category

Usage:
    poetry run python .claude/skills/phoenix-theme-skill/scripts/04_extract_component_html.py
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from pathlib import Path
from html import unescape

# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DATA_DIR = SKILL_DIR / "data"
CATALOG_FILE = DATA_DIR / "phoenix_catalog.json"
COMPONENTS_DIR = DATA_DIR / "components"

# Key pages to extract (most useful for dashboard building)
KEY_PAGES = [
    "widgets.html",
    "modules/components/card.html",
    "modules/components/badge.html",
    "modules/components/list-group.html",
    "modules/components/progress-bar.html",
    "modules/components/avatar.html",
    "modules/components/alerts.html",
    "modules/tables/advance-tables.html",
    "modules/tables/basic-tables.html",
    "modules/echarts/bar-charts.html",
    "modules/echarts/line-charts.html",
    "modules/echarts/pie-charts.html",
    "modules/echarts/gauge-chart.html",
    "dashboard/default.html",
    "dashboard/crm.html",
    "dashboard/project-management.html",
    "dashboard/analytics.html",
    "apps/crm/analytics.html",
]


def get_page(url: str) -> BeautifulSoup:
    """Fetch a page and return BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None


def extract_code_blocks(soup: BeautifulSoup) -> list:
    """
    Extract code blocks from a Phoenix documentation page.

    Phoenix uses several patterns:
    1. <pre><code class="language-html">...</code></pre>
    2. <div class="highlight"><pre>...</pre></div>
    3. Code tabs with data-bs-target
    """
    components = []

    # Pattern 1: Standard code blocks with language-html class
    for code in soup.find_all('code', class_=re.compile(r'language-html|lang-html')):
        html_content = code.get_text()
        if html_content.strip():
            # Find the nearest heading for context
            heading = find_nearest_heading(code)
            components.append({
                'name': heading or 'Unnamed Component',
                'html': clean_html(html_content),
                'type': 'code_block'
            })

    # Pattern 2: Pre tags inside highlight divs
    for highlight in soup.find_all('div', class_='highlight'):
        pre = highlight.find('pre')
        if pre:
            html_content = pre.get_text()
            if html_content.strip() and '<' in html_content:
                heading = find_nearest_heading(highlight)
                components.append({
                    'name': heading or 'Unnamed Component',
                    'html': clean_html(html_content),
                    'type': 'highlight'
                })

    # Pattern 3: Tab panes with code content
    for tab_pane in soup.find_all('div', class_='tab-pane'):
        code = tab_pane.find('code') or tab_pane.find('pre')
        if code:
            html_content = code.get_text()
            if html_content.strip() and '<' in html_content:
                # Get tab name from aria-labelledby or nearby
                tab_id = tab_pane.get('id', '')
                heading = find_nearest_heading(tab_pane) or tab_id
                components.append({
                    'name': heading or 'Tab Component',
                    'html': clean_html(html_content),
                    'type': 'tab_pane'
                })

    # Pattern 4: Phoenix-specific code viewer pattern
    for viewer in soup.find_all('div', {'data-component': True}):
        component_name = viewer.get('data-component', 'Unknown')
        code = viewer.find('code') or viewer.find('pre')
        if code:
            html_content = code.get_text()
            if html_content.strip():
                components.append({
                    'name': component_name,
                    'html': clean_html(html_content),
                    'type': 'data_component'
                })

    return components


def extract_preview_html(soup: BeautifulSoup) -> list:
    """
    Extract the actual rendered preview HTML (not just code blocks).
    This captures the live components on the page.
    """
    components = []

    # Look for preview containers
    preview_selectors = [
        ('div', {'class': 'preview'}),
        ('div', {'class': 'component-preview'}),
        ('div', {'class': 'card-body'}),  # Many examples are in cards
    ]

    for tag, attrs in preview_selectors:
        for preview in soup.find_all(tag, attrs):
            # Skip if it's a code block container
            if preview.find('code') or preview.find('pre'):
                continue

            html_content = str(preview)
            if len(html_content) > 100:  # Skip tiny fragments
                heading = find_nearest_heading(preview)
                components.append({
                    'name': heading or 'Preview',
                    'html': html_content,
                    'type': 'preview'
                })

    return components


def find_nearest_heading(element) -> str:
    """Find the nearest heading element before this element."""
    # Look backwards through siblings
    for sibling in element.find_all_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text = sibling.get_text().strip()
        if text:
            return text[:100]  # Limit length
    return None


def clean_html(html: str) -> str:
    """Clean up HTML content."""
    # Unescape HTML entities
    html = unescape(html)
    # Remove excessive whitespace but preserve structure
    lines = html.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    return '\n'.join(cleaned_lines).strip()


def save_components(page_path: str, components: list):
    """Save extracted components to files."""
    if not components:
        return

    # Create directory structure
    page_name = page_path.replace('/', '_').replace('.html', '')
    page_dir = COMPONENTS_DIR / page_name
    page_dir.mkdir(parents=True, exist_ok=True)

    # Save individual components
    for i, comp in enumerate(components):
        filename = f"{i:02d}_{sanitize_filename(comp['name'])}.html"
        filepath = page_dir / filename

        # Write with metadata header
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"<!-- Component: {comp['name']} -->\n")
            f.write(f"<!-- Type: {comp['type']} -->\n")
            f.write(f"<!-- Source: {page_path} -->\n\n")
            f.write(comp['html'])

    # Save index for this page
    index_file = page_dir / "_index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump({
            'page': page_path,
            'components': [
                {'name': c['name'], 'type': c['type'], 'file': f"{i:02d}_{sanitize_filename(c['name'])}.html"}
                for i, c in enumerate(components)
            ]
        }, f, indent=2)

    return len(components)


def sanitize_filename(name: str) -> str:
    """Convert a name to a safe filename."""
    # Remove/replace invalid characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '_', name)
    name = name.lower()[:50]
    return name or 'component'


def extract_full_page_html(url: str) -> str:
    """Get the full page HTML for reference."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"  Error fetching full page {url}: {e}")
        return None


def main():
    print("=" * 60)
    print("Phoenix Component HTML Extractor")
    print("=" * 60)

    # Create output directory
    COMPONENTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load catalog to get full URLs
    with open(CATALOG_FILE, 'r') as f:
        catalog = json.load(f)

    base_url = catalog['meta']['base_url']
    pages = catalog['pages']

    # Create URL lookup
    url_lookup = {p['path']: p['url'] for p in pages}

    total_components = 0
    pages_processed = 0

    for page_path in KEY_PAGES:
        # Normalize path
        if page_path.startswith('/'):
            page_path = page_path[1:]

        url = url_lookup.get(page_path) or f"{base_url}{page_path}"
        print(f"\nProcessing: {page_path}")
        print(f"  URL: {url}")

        soup = get_page(url)
        if not soup:
            continue

        # Extract code blocks (the actual HTML source)
        code_components = extract_code_blocks(soup)
        print(f"  Found {len(code_components)} code blocks")

        # Save full page HTML for reference
        full_page_dir = COMPONENTS_DIR / "full_pages"
        full_page_dir.mkdir(exist_ok=True)
        full_page_file = full_page_dir / f"{page_path.replace('/', '_')}"
        with open(full_page_file, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

        # Save components
        if code_components:
            count = save_components(page_path, code_components)
            total_components += count
            pages_processed += 1

        # Be nice to the server
        time.sleep(0.5)

    # Create master index
    master_index = {
        'extracted_at': str(Path(__file__).stat().st_mtime),
        'pages_processed': pages_processed,
        'total_components': total_components,
        'pages': []
    }

    for page_dir in COMPONENTS_DIR.iterdir():
        if page_dir.is_dir() and page_dir.name != 'full_pages':
            index_file = page_dir / "_index.json"
            if index_file.exists():
                with open(index_file) as f:
                    page_index = json.load(f)
                    master_index['pages'].append(page_index)

    with open(COMPONENTS_DIR / "_master_index.json", 'w') as f:
        json.dump(master_index, f, indent=2)

    print("\n" + "=" * 60)
    print(f"Extraction complete!")
    print(f"  Pages processed: {pages_processed}")
    print(f"  Components extracted: {total_components}")
    print(f"  Output: {COMPONENTS_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
