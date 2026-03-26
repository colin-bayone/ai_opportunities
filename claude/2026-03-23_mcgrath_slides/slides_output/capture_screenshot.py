#!/usr/bin/env python3
"""Capture screenshot of slide HTML file."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path("/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_profile_oracle_scm.html")
OUTPUT = Path("/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/screenshot_profile_oracle_scm.png")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        ctx = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await ctx.new_page()

        await page.goto(f"file://{HTML_FILE}")
        await page.wait_for_load_state('networkidle')

        await page.screenshot(path=str(OUTPUT), full_page=False)
        print(f"Screenshot saved to: {OUTPUT}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
