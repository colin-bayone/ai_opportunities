"""
Visual verification of SOW HTML conversion using Playwright.
Takes screenshots of each page for comparison with original PDF.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_PATH = Path(__file__).parent / "SOW-Building-Nexus-9000-switches.html"
OUTPUT_DIR = Path(__file__).parent / "screenshots"


async def capture_pages():
    OUTPUT_DIR.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Set viewport to approximate letter size at 96 DPI
        await page.set_viewport_size({"width": 816, "height": 1056})

        # Load the HTML file
        await page.goto(f"file://{HTML_PATH.absolute()}")
        await page.wait_for_load_state("networkidle")

        # Get all page divs
        pages = await page.query_selector_all(".page")
        print(f"Found {len(pages)} pages")

        # Screenshot each page
        for i, page_div in enumerate(pages, 1):
            screenshot_path = OUTPUT_DIR / f"page_{i:02d}.png"
            await page_div.screenshot(path=str(screenshot_path))
            print(f"Captured page {i} -> {screenshot_path.name}")

        # Also capture full document
        await page.screenshot(
            path=str(OUTPUT_DIR / "full_document.png"),
            full_page=True
        )
        print("Captured full document")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(capture_pages())
