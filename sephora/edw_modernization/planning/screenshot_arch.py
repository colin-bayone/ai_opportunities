#!/usr/bin/env python3
"""Quick screenshot - architecture diagram HTML file"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = "/home/cmoore/programming/ai_opportunities/sephora/edw_modernization/deliverables/architecture_diagram_2026-04-02.html"
OUTPUT_PATH = "/home/cmoore/programming/ai_opportunities/sephora/edw_modernization/planning/architecture_screenshot_v2.png"

async def main():
    file_url = f"file://{HTML_FILE}"
    print(f"Opening: {file_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1600, "height": 900})
        page = await ctx.new_page()

        await page.goto(file_url)
        await page.wait_for_load_state('networkidle')

        print("Waiting 8 seconds for fonts and Mermaid.js to fully render...")
        await asyncio.sleep(8)

        # Full page screenshot
        await page.screenshot(path=OUTPUT_PATH, full_page=True)
        print(f"Screenshot saved to: {OUTPUT_PATH}")

        await browser.close()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(main())
