#!/usr/bin/env python3
"""Capture screenshots of all 12 pages from SOW-Building-Nexus-9000-switches-v2.html"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches-v2.html")
OUTPUT_DIR = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/screenshots/v2_current")

async def main():
    if not HTML_FILE.exists():
        print(f"ERROR: HTML file not found at {HTML_FILE}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # 850px width, 1x DPI (not device_scale_factor=2)
        context = await browser.new_context(
            viewport={"width": 850, "height": 1100},
            device_scale_factor=1
        )
        page = await context.new_page()

        # Load the HTML file
        file_url = f"file://{HTML_FILE.absolute()}"
        print(f"Loading {file_url}")
        await page.goto(file_url)
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(1)  # Extra time for any dynamic content

        # Capture 12 pages
        for page_num in range(1, 13):
            screenshot_path = OUTPUT_DIR / f"page_{page_num:02d}.png"

            # Use JavaScript to scroll to the correct page
            # Each page is 11 inches tall at 96 DPI = 1056px
            # Add small offset to center on page
            scroll_position = (page_num - 1) * 1056

            await page.evaluate(f"window.scrollTo(0, {scroll_position})")
            await asyncio.sleep(0.5)  # Wait for scroll to complete

            # Take screenshot of viewport (which should be showing one page)
            await page.screenshot(path=str(screenshot_path))
            print(f"✓ Captured page {page_num:02d} -> {screenshot_path}")

        await browser.close()
        print(f"\n✓ All 12 pages captured to {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
