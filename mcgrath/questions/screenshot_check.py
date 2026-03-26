#!/usr/bin/env python3
"""Quick screenshot of the RFP questions HTML to verify styling."""

from playwright.sync_api import sync_playwright
import os

def main():
    html_path = os.path.abspath("rfp_questions_review.html")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 800})

        # Load the local HTML file
        page.goto(f"file://{html_path}")

        # Wait for content to load
        page.wait_for_load_state("networkidle")

        # Scroll past the cover page to get to the table
        page.evaluate("window.scrollTo(0, window.innerHeight + 200)")
        page.wait_for_timeout(500)

        # Screenshot
        page.screenshot(path="table_header_check.png", full_page=False)
        print(f"Screenshot saved to: {os.path.abspath('table_header_check.png')}")

        browser.close()

if __name__ == "__main__":
    main()
