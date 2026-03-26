"""
Phoenix Catalog Query Utility

Provides programmatic access to the Phoenix theme catalog.
Used by the skill to find relevant components and pages.

Usage:
    from scripts.query_catalog import PhoenixCatalog

    catalog = PhoenixCatalog()
    charts = catalog.by_category('charts')
    tables = catalog.search_tags('table', 'data')
    page = catalog.get_page_by_path('modules/echarts/bar-charts.html')
"""

import json
import re
from pathlib import Path
from typing import List, Optional


class PhoenixCatalog:
    """Query interface for the Phoenix theme catalog."""

    def __init__(self, catalog_path: str = None):
        """
        Initialize the catalog.

        Args:
            catalog_path: Path to phoenix_catalog.json.
                         Defaults to ../data/phoenix_catalog.json relative to this script.
        """
        if catalog_path is None:
            script_dir = Path(__file__).resolve().parent
            catalog_path = script_dir.parent / "data" / "phoenix_catalog.json"

        with open(catalog_path, 'r') as f:
            data = json.load(f)

        self.meta = data.get('meta', {})
        self.pages = data.get('pages', [])

        # Build indexes for fast lookup
        self._build_indexes()

    def _build_indexes(self):
        """Build internal indexes for fast lookups."""
        self._by_category = {}
        self._by_url = {}
        self._by_path = {}

        for page in self.pages:
            # Index by category
            cat = page['category']
            if cat not in self._by_category:
                self._by_category[cat] = []
            self._by_category[cat].append(page)

            # Index by URL and path
            self._by_url[page['url']] = page
            self._by_path[page['path']] = page

    # -------------------------------------------------------------------------
    # Category Queries
    # -------------------------------------------------------------------------

    def list_categories(self) -> List[str]:
        """List all available categories."""
        return sorted(self._by_category.keys())

    def by_category(self, category: str) -> List[dict]:
        """
        Get all pages in a category.

        Args:
            category: Category name (e.g., 'charts', 'forms', 'components')

        Returns:
            List of page dicts in that category
        """
        return self._by_category.get(category, [])

    def list_subcategories(self, category: str) -> List[str]:
        """List all subcategories within a category."""
        pages = self.by_category(category)
        subcats = set(p['subcategory'] for p in pages)
        return sorted(subcats)

    def by_subcategory(self, category: str, subcategory: str) -> List[dict]:
        """
        Get pages matching a specific subcategory.

        Args:
            category: Category name
            subcategory: Subcategory name

        Returns:
            List of matching page dicts
        """
        return [
            p for p in self.by_category(category)
            if p['subcategory'] == subcategory
        ]

    # -------------------------------------------------------------------------
    # Search Queries
    # -------------------------------------------------------------------------

    def search_tags(self, *tags: str) -> List[dict]:
        """
        Find pages matching ANY of the given tags.

        Args:
            tags: One or more tags to search for

        Returns:
            List of matching pages, sorted by number of matching tags (desc)
        """
        tags_lower = [t.lower() for t in tags]
        results = []

        for page in self.pages:
            page_tags = [t.lower() for t in page.get('tags', [])]
            matches = sum(1 for t in tags_lower if t in page_tags)
            if matches > 0:
                results.append((matches, page))

        # Sort by match count descending
        results.sort(key=lambda x: x[0], reverse=True)
        return [page for _, page in results]

    def search_components(self, term: str) -> List[dict]:
        """
        Search component_names for a term (case-insensitive).

        Args:
            term: Search term

        Returns:
            List of pages with matching component names
        """
        term_lower = term.lower()
        results = []

        for page in self.pages:
            for comp in page.get('component_names', []):
                if term_lower in comp.lower():
                    results.append(page)
                    break

        return results

    def search_text(self, term: str) -> List[dict]:
        """
        Search across title, description, component names, and tags.

        Args:
            term: Search term

        Returns:
            List of matching pages, scored by relevance
        """
        term_lower = term.lower()
        results = []

        for page in self.pages:
            score = 0

            # Title match (high weight)
            if term_lower in page.get('title', '').lower():
                score += 3

            # Description match
            if term_lower in page.get('description', '').lower():
                score += 2

            # Component name match
            for comp in page.get('component_names', []):
                if term_lower in comp.lower():
                    score += 2
                    break

            # Tag match
            if term_lower in [t.lower() for t in page.get('tags', [])]:
                score += 1

            # Path match
            if term_lower in page.get('path', '').lower():
                score += 1

            if score > 0:
                results.append((score, page))

        results.sort(key=lambda x: x[0], reverse=True)
        return [page for _, page in results]

    def by_path_pattern(self, pattern: str) -> List[dict]:
        """
        Find pages where path matches a regex pattern.

        Args:
            pattern: Regex pattern to match against path

        Returns:
            List of matching pages
        """
        regex = re.compile(pattern, re.IGNORECASE)
        return [p for p in self.pages if regex.search(p['path'])]

    # -------------------------------------------------------------------------
    # Direct Lookups
    # -------------------------------------------------------------------------

    def get_page_by_url(self, url: str) -> Optional[dict]:
        """Get a specific page by its full URL."""
        return self._by_url.get(url)

    def get_page_by_path(self, path: str) -> Optional[dict]:
        """Get a specific page by its relative path."""
        return self._by_path.get(path)

    # -------------------------------------------------------------------------
    # Utility Methods
    # -------------------------------------------------------------------------

    def summary(self) -> str:
        """Return a summary of the catalog."""
        lines = [
            f"Phoenix Theme Catalog v{self.meta.get('version', 'unknown')}",
            f"Crawled: {self.meta.get('crawl_date', 'unknown')}",
            f"Total pages: {self.meta.get('total_pages', len(self.pages))}",
            "",
            "Categories:"
        ]
        for cat in self.list_categories():
            count = len(self.by_category(cat))
            lines.append(f"  {cat}: {count} pages")

        return "\n".join(lines)

    def format_page(self, page: dict) -> str:
        """Format a page entry for display."""
        lines = [
            f"Title: {page.get('title', 'N/A')}",
            f"URL: {page.get('url', 'N/A')}",
            f"Category: {page.get('category', 'N/A')} / {page.get('subcategory', 'N/A')}",
        ]
        if page.get('description'):
            lines.append(f"Description: {page['description']}")
        if page.get('component_names'):
            lines.append(f"Components: {', '.join(page['component_names'])}")
        if page.get('tags'):
            lines.append(f"Tags: {', '.join(page['tags'])}")

        return "\n".join(lines)


# -------------------------------------------------------------------------
# CLI for testing
# -------------------------------------------------------------------------

if __name__ == '__main__':
    import sys

    catalog = PhoenixCatalog()

    if len(sys.argv) < 2:
        print(catalog.summary())
        print("\nUsage:")
        print("  python query_catalog.py category <name>")
        print("  python query_catalog.py search <term>")
        print("  python query_catalog.py tags <tag1> [tag2] ...")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == 'category' and len(sys.argv) > 2:
        cat = sys.argv[2]
        pages = catalog.by_category(cat)
        print(f"Found {len(pages)} pages in '{cat}':\n")
        for p in pages:
            print(f"  - {p['title']}")
            print(f"    {p['url']}")

    elif cmd == 'search' and len(sys.argv) > 2:
        term = ' '.join(sys.argv[2:])
        pages = catalog.search_text(term)
        print(f"Found {len(pages)} pages matching '{term}':\n")
        for p in pages:
            print(catalog.format_page(p))
            print()

    elif cmd == 'tags' and len(sys.argv) > 2:
        tags = sys.argv[2:]
        pages = catalog.search_tags(*tags)
        print(f"Found {len(pages)} pages with tags {tags}:\n")
        for p in pages:
            print(f"  - {p['title']} ({p['category']})")
            print(f"    {p['url']}")

    else:
        print("Unknown command. Run without arguments for help.")
