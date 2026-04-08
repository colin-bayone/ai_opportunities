#!/usr/bin/env python3
"""Capture full-page screenshot of architecture diagram HTML with Mermaid.js rendering."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path("/home/cmoore/programming/ai_opportunities/sephora/edw_modernization/deliverables/architecture_diagram_2026-04-02.html")
OUTPUT_PATH = Path("/home/cmoore/programming/ai_opportunities/sephora/edw_modernization/planning/architecture_screenshot.png")

async def main():
    file_url = f"file://{HTML_FILE.resolve()}"
    print(f"Loading: {file_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1600, "height": 1080})
        page = await context.new_page()

        await page.goto(file_url)
        await page.wait_for_load_state('networkidle')

        # Wait at least 5 seconds for Mermaid.js to render diagrams
        print("Waiting 6 seconds for Mermaid.js diagrams to render...")
        await asyncio.sleep(6)

        # Check if Mermaid rendered successfully
        mermaid_svgs = await page.query_selector_all('svg')
        print(f"Found {len(mermaid_svgs)} SVG element(s) on page")

        # Take full-page screenshot
        await page.screenshot(path=str(OUTPUT_PATH), full_page=True)
        print(f"Screenshot saved to: {OUTPUT_PATH}")

        await browser.close()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
