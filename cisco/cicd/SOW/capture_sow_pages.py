#!/usr/bin/env python3
"""Capture screenshots of all 12 pages of the SOW HTML document"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches-v2.html")
SCREENSHOTS = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/screenshots")
SCREENSHOTS.mkdir(parents=True, exist_ok=True)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use A4 page dimensions (8.5" x 11" at 96 DPI)
        context = await browser.new_context(
            viewport={"width": 816, "height": 1056},  # 8.5" x 11" at 96 DPI
            device_scale_factor=2  # Higher resolution for print quality
        )
        page = await context.new_page()

        # Load the HTML file
        print(f"Loading {HTML_FILE}...")
        await page.goto(f"file://{HTML_FILE}")
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(2)  # Give time for any rendering

        # The document uses CSS page breaks for print layout
        # We'll capture the entire scrollable page and then extract page regions

        # First, get the total height
        total_height = await page.evaluate("document.documentElement.scrollHeight")
        print(f"Total document height: {total_height}px")

        # For a print layout document, we'll capture it at print dimensions
        # Set viewport to standard letter size and capture each "page" region

        # Capture 12 pages by scrolling and screenshotting page-sized regions
        page_height = 1056  # 11" at 96 DPI

        for page_num in range(1, 13):
            print(f"Capturing page {page_num}...")

            # Scroll to the page position
            scroll_y = (page_num - 1) * page_height
            await page.evaluate(f"window.scrollTo(0, {scroll_y})")
            await asyncio.sleep(0.5)  # Brief pause for rendering

            # Take screenshot of current viewport
            screenshot_path = SCREENSHOTS / f"v2_page_{page_num:02d}.png"
            await page.screenshot(path=str(screenshot_path))
            print(f"✓ Saved {screenshot_path}")

        await browser.close()
        print("\n✓ All 12 pages captured successfully")

if __name__ == "__main__":
    asyncio.run(main())
