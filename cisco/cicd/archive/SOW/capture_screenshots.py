#!/usr/bin/env python3
"""
Screenshot capture script for SOW HTML document
Captures full document and individual pages/sections
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

# Configuration
HTML_FILE = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches-v2.html")
SCREENSHOTS_DIR = Path("/home/cmoore/programming/cisco_projects/cicd/SOW/screenshots")
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

async def main():
    """Capture screenshots of the SOW document"""

    # Verify HTML file exists
    if not HTML_FILE.exists():
        print(f"ERROR: HTML file not found at {HTML_FILE}")
        return

    file_url = f"file://{HTML_FILE.absolute()}"
    print(f"Opening: {file_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        # Use exact dimensions for 8.5" x 11" at 96 DPI
        # 8.5" x 96 = 816px width
        # 11" x 96 = 1056px height
        # Using higher resolution for better quality
        viewport_width = 1632  # 8.5" at 192 DPI
        viewport_height = 2112  # 11" at 192 DPI

        context = await browser.new_context(
            viewport={"width": viewport_width, "height": viewport_height},
            device_scale_factor=2  # High DPI for print quality
        )
        page = await context.new_page()

        # Load the HTML document
        await page.goto(file_url)
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(2)  # Give time for all styles to render

        print("Page loaded successfully")

        # 1. Full document screenshot
        print("\n1. Capturing full document screenshot...")
        await page.screenshot(
            path=str(SCREENSHOTS_DIR / "00_full_document.png"),
            full_page=True
        )
        print(f"   Saved: {SCREENSHOTS_DIR}/00_full_document.png")

        # 2. Individual page screenshots
        # Get all page elements
        pages = await page.query_selector_all('.page')
        total_pages = len(pages)
        print(f"\nFound {total_pages} pages in document")

        print("\n2. Capturing individual page screenshots...")
        for i, page_element in enumerate(pages, 1):
            screenshot_path = SCREENSHOTS_DIR / f"page_{i:02d}_of_{total_pages:02d}.png"
            await page_element.screenshot(path=str(screenshot_path))
            print(f"   Page {i}/{total_pages}: {screenshot_path}")

        # 3. Specific sections requested
        print("\n3. Capturing specific sections...")

        # Page 1: Cover page (already captured above as page_01)
        print("   Cover page: page_01_of_12.png")

        # Page 2: General Information, Timeline
        print("   General Info/Timeline: page_02_of_12.png")

        # Pages 4-5: SLA tables - capture combined view
        if total_pages >= 5:
            print("   Capturing SLA tables (pages 4-5)...")
            # Get page 4 and 5 elements
            page_4 = pages[3]  # Index 3 = page 4
            page_5 = pages[4]  # Index 4 = page 5

            # Individual page screenshots already captured
            # Also capture the SLA table section specifically
            sla_tables = await page.query_selector_all('table.sla-table')
            for idx, table in enumerate(sla_tables, 1):
                table_path = SCREENSHOTS_DIR / f"section_sla_table_{idx}.png"
                await table.screenshot(path=str(table_path))
                print(f"   SLA Table {idx}: {table_path}")

        # Page 6: Required Personnel/Other Resources tables
        if total_pages >= 6:
            print("   Personnel/Resources tables: page_06_of_12.png")

            # Capture the specific tables
            personnel_tables = await page.query_selector_all('table.data-table.empty-table')
            if len(personnel_tables) >= 2:
                await personnel_tables[0].screenshot(
                    path=str(SCREENSHOTS_DIR / "section_required_personnel_table.png")
                )
                print(f"   Required Personnel table: section_required_personnel_table.png")

                await personnel_tables[1].screenshot(
                    path=str(SCREENSHOTS_DIR / "section_other_resources_table.png")
                )
                print(f"   Other Resources table: section_other_resources_table.png")

        # Pages 7-8: Milestone tables
        if total_pages >= 8:
            print("   Milestone tables: page_07_of_12.png and page_08_of_12.png")

            # Capture milestone tables
            milestone_headers = await page.query_selector_all('table.milestone-header')
            for idx, table in enumerate(milestone_headers, 1):
                table_path = SCREENSHOTS_DIR / f"section_milestone_{idx}_header.png"
                await table.screenshot(path=str(table_path))
                print(f"   Milestone {idx} header: {table_path}")

        # Page 12: Signature block
        if total_pages >= 12:
            print("   Signature block: page_12_of_12.png")

            # Capture signature block specifically
            signature_block = await page.query_selector('.signature-block')
            if signature_block:
                await signature_block.screenshot(
                    path=str(SCREENSHOTS_DIR / "section_signature_block.png")
                )
                print(f"   Signature block: section_signature_block.png")

        await browser.close()

        print("\n" + "="*60)
        print("Screenshot capture complete!")
        print(f"All screenshots saved to: {SCREENSHOTS_DIR}")
        print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
