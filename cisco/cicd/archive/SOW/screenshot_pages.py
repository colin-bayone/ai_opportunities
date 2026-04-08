#!/usr/bin/env python3
"""Capture screenshots of each page of the SOW HTML document."""

from playwright.sync_api import sync_playwright
from pathlib import Path

HTML_FILE = Path(__file__).parent / "SOW-Building-Nexus-9000-switches.html"
OUTPUT_DIR = Path(__file__).parent / "screenshots"

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 900})

        # Load the HTML file
        page.goto(f"file://{HTML_FILE.resolve()}")
        page.wait_for_load_state("networkidle")

        # Find all page divs
        pages = page.locator("div.page").all()
        print(f"Found {len(pages)} pages")

        for i, page_div in enumerate(pages, 1):
            # Scroll to the page and screenshot it
            page_div.scroll_into_view_if_needed()
            page_div.screenshot(path=OUTPUT_DIR / f"page_{i:02d}.png")
            print(f"Captured page {i}")

        browser.close()

    print(f"\nScreenshots saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
