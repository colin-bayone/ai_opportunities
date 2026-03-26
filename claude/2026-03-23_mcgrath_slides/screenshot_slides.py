"""Screenshot all exec summary slide versions for visual comparison."""
from playwright.sync_api import sync_playwright
from pathlib import Path

SLIDES_DIR = Path(__file__).parent / "slides_output"
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

slides = [
    "slide_02_exec_summary_version_a.html",
    "slide_02_exec_summary_version_b.html",
    "slide_02_exec_summary_version_c.html",
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 900})

    for slide_file in slides:
        path = SLIDES_DIR / slide_file
        if not path.exists():
            print(f"SKIP: {slide_file} not found")
            continue

        page.goto(f"file://{path.resolve()}")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(500)

        screenshot_name = slide_file.replace(".html", ".png")
        page.screenshot(path=str(SCREENSHOTS_DIR / screenshot_name), full_page=True)
        print(f"OK: {screenshot_name}")

    browser.close()

print(f"\nScreenshots saved to: {SCREENSHOTS_DIR}")
