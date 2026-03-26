"""
Phoenix Theme Documentation Crawler v2

Crawls the Phoenix theme documentation site and builds a queryable
JSON catalog of all pages and components.

Output: phoenix_catalog.json with structured metadata

Usage:
    poetry run python claude/2025-12-16_phoenix-theme-skill/scripts/01_crawl_phoenix_site.py

Output saved to: claude/2025-12-16_phoenix-theme-skill/data/phoenix_catalog.json
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import time
import re
from datetime import datetime
from pathlib import Path
from collections import Counter

BASE_URL = "https://prium.github.io/phoenix/v1.23.0/"
VERSION = "1.23.0"

# Output directory (relative to this script's parent)
SCRIPT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SCRIPT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "phoenix_catalog.json"


def get_page(url: str):
    """Fetch a page and return BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None


def is_html_page(url: str) -> bool:
    """Check if URL is an HTML page (not an asset)."""
    parsed = urlparse(url)
    path = parsed.path.lower()

    # Skip asset files
    asset_extensions = (
        '.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico',
        '.mp4', '.webm', '.mp3', '.wav',
        '.pdf', '.zip', '.css', '.js',
        '.woff', '.woff2', '.ttf', '.eot'
    )
    if path.endswith(asset_extensions):
        return False

    # Skip query string variations of same page
    if '?' in url and 'theme-control' in url:
        return False

    return True


def extract_links(soup, current_url: str) -> set:
    """Extract all internal HTML page links from a page."""
    links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']

        # Skip anchors and javascript
        if href.startswith('#') or href.startswith('javascript:'):
            continue

        # Build full URL
        if href.startswith(('http://', 'https://')):
            full_url = href
        else:
            full_url = urljoin(current_url, href)

        # Only keep Phoenix v1.23.0 URLs
        if 'prium.github.io/phoenix/v1.23.0' not in full_url:
            continue

        # Remove anchor
        full_url = full_url.split('#')[0]

        # Only keep HTML pages
        if is_html_page(full_url):
            links.add(full_url)

    return links


def categorize_page(path: str) -> tuple:
    """
    Categorize a page based on its path.
    Returns (category, subcategory).
    """
    # Ensure path has leading slash for consistent matching
    path = path.lower()
    if not path.startswith('/'):
        path = '/' + path

    # Charts
    if '/modules/echarts/' in path:
        subcat = path.split('/modules/echarts/')[-1].replace('.html', '').replace('-', '_')
        return ('charts', subcat or 'overview')

    # Forms
    if '/modules/forms/' in path:
        if '/advance/' in path:
            subcat = path.split('/advance/')[-1].replace('.html', '')
            return ('forms', f'advanced_{subcat}')
        elif '/basic/' in path:
            subcat = path.split('/basic/')[-1].replace('.html', '')
            return ('forms', f'basic_{subcat}')
        else:
            subcat = path.split('/modules/forms/')[-1].replace('.html', '')
            return ('forms', subcat or 'overview')

    # Tables
    if '/modules/tables/' in path:
        subcat = path.split('/modules/tables/')[-1].replace('.html', '').replace('-', '_')
        return ('tables', subcat or 'overview')

    # Components
    if '/modules/components/' in path:
        subcat = path.split('/modules/components/')[-1].replace('.html', '').replace('-', '_')
        subcat = subcat.replace('/', '_').strip('_')
        return ('components', subcat or 'overview')

    # Utilities
    if '/modules/utilities/' in path:
        subcat = path.split('/modules/utilities/')[-1].replace('.html', '').replace('-', '_')
        return ('utilities', subcat or 'overview')

    # Icons
    if '/modules/icons/' in path:
        subcat = path.split('/modules/icons/')[-1].replace('.html', '')
        return ('icons', subcat or 'overview')

    # Dashboards
    if '/dashboard/' in path:
        subcat = path.split('/dashboard/')[-1].replace('.html', '').replace('-', '_')
        return ('dashboards', subcat or 'main')

    # Apps
    if '/apps/' in path:
        parts = path.split('/apps/')[-1].split('/')
        app_name = parts[0] if parts else 'misc'
        subcat = '_'.join(parts).replace('.html', '').replace('-', '_')
        return ('apps', subcat or app_name)

    # Pages
    if '/pages/' in path:
        if '/authentication/' in path:
            subcat = path.split('/authentication/')[-1].replace('.html', '').replace('/', '_')
            return ('pages', f'auth_{subcat}')
        elif '/errors/' in path:
            subcat = path.split('/errors/')[-1].replace('.html', '')
            return ('pages', f'error_{subcat}')
        elif '/landing/' in path:
            subcat = path.split('/landing/')[-1].replace('.html', '')
            return ('pages', f'landing_{subcat}')
        elif '/pricing/' in path:
            subcat = path.split('/pricing/')[-1].replace('.html', '')
            return ('pages', f'pricing_{subcat}')
        elif '/faq/' in path:
            subcat = path.split('/faq/')[-1].replace('.html', '')
            return ('pages', f'faq_{subcat}')
        else:
            subcat = path.split('/pages/')[-1].replace('.html', '').replace('-', '_')
            return ('pages', subcat or 'misc')

    # Documentation
    if '/documentation/' in path:
        subcat = path.split('/documentation/')[-1].replace('.html', '').replace('/', '_')
        return ('documentation', subcat or 'overview')

    # Widgets page
    if 'widgets.html' in path:
        return ('widgets', 'main')

    # Demo pages
    if '/demo/' in path:
        subcat = path.split('/demo/')[-1].replace('.html', '').replace('-', '_')
        return ('demos', subcat or 'misc')

    # Index/home
    if path.endswith('index.html') or path == '/' or path == '':
        return ('home', 'main')

    # Changelog
    if 'changelog' in path:
        return ('documentation', 'changelog')

    # Showcase
    if 'showcase' in path:
        return ('documentation', 'showcase')

    return ('other', 'misc')


def generate_tags(path: str, title: str, component_names: list) -> list:
    """Generate search tags from path, title, and component names."""
    tags = set()

    # Tags from path segments
    path_parts = path.lower().replace('.html', '').replace('-', ' ').replace('_', ' ').split('/')
    for part in path_parts:
        words = part.split()
        for word in words:
            if len(word) > 2:
                tags.add(word)

    # Tags from title
    title_words = re.findall(r'\b\w+\b', title.lower())
    for word in title_words:
        if len(word) > 2 and word not in ('phoenix', 'the', 'and', 'for'):
            tags.add(word)

    # Tags from component names
    for comp in component_names:
        comp_words = re.findall(r'\b\w+\b', comp.lower())
        for word in comp_words:
            if len(word) > 2:
                tags.add(word)

    return sorted(list(tags))


def extract_page_info(soup, url: str) -> dict:
    """Extract structured metadata from a page."""
    path = url.replace(BASE_URL, '')
    category, subcategory = categorize_page(path)

    # Get title
    title = ''
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.strip()

    # Get description from h1
    description = ''
    h1 = soup.find('h1')
    if h1:
        description = h1.get_text(strip=True)

    # Extract component names
    component_names = []

    for el in soup.find_all(class_=['card-title', 'card-header']):
        text = el.get_text(strip=True)
        if text and 5 < len(text) < 60 and not any(x in text.lower() for x in ['sign in', 'sign out', 'notification']):
            component_names.append(text)

    for el in soup.find_all(['h2', 'h3', 'h4'], id=True):
        text = el.get_text(strip=True)
        if text and 3 < len(text) < 50:
            component_names.append(text)

    component_names = list(dict.fromkeys(component_names))

    # Extract nav breadcrumb
    parent_nav = ''
    breadcrumb = soup.find(class_='breadcrumb')
    if breadcrumb:
        items = breadcrumb.find_all('li')
        parent_nav = ' > '.join([li.get_text(strip=True) for li in items])

    # Generate tags
    tags = generate_tags(path, title, component_names)

    return {
        'url': url,
        'path': path,
        'title': title,
        'category': category,
        'subcategory': subcategory,
        'description': description,
        'component_names': component_names,
        'tags': tags,
        'parent_nav': parent_nav
    }


def crawl(start_url: str, max_pages: int = 500) -> list:
    """Crawl the site starting from start_url."""
    visited = set()
    to_visit = {start_url}
    pages = []

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()

        if url in visited:
            continue

        visited.add(url)
        print(f"[{len(visited):3d}] {url.replace(BASE_URL, '')}")

        soup = get_page(url)
        if not soup:
            continue

        page_info = extract_page_info(soup, url)
        pages.append(page_info)

        links = extract_links(soup, url)
        for link in links:
            if link not in visited:
                to_visit.add(link)

        time.sleep(0.15)

    return pages


def main():
    print("=" * 60)
    print("Phoenix Theme Crawler v2")
    print(f"Base URL: {BASE_URL}")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 60)

    # Ensure output directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Start crawl
    pages = crawl(BASE_URL)

    # Build catalog with metadata
    catalog = {
        'meta': {
            'version': VERSION,
            'base_url': BASE_URL,
            'crawl_date': datetime.now().isoformat()[:10],
            'total_pages': len(pages)
        },
        'pages': sorted(pages, key=lambda p: (p['category'], p['subcategory'], p['path']))
    }

    # Print summary
    print("\n" + "=" * 60)
    print(f"Crawled {len(pages)} HTML pages")
    print("\nPages by category:")

    cat_counts = Counter(p['category'] for p in pages)
    for cat, count in sorted(cat_counts.items()):
        print(f"  {cat}: {count}")

    # Save to JSON
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(catalog, f, indent=2)
    print(f"\nSaved catalog to: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
