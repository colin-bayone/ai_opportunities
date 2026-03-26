"""Screenshot slide 16 capacity distribution for visual review."""
from playwright.sync_api import sync_playwright
from pathlib import Path

SLIDES_DIR = Path(__file__).parent / "slides_output"
SCREENSHOTS_DIR = Path(__file__).parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

slide_file = "slide_16_capacity_distribution.html"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1400, "height": 900})

    path = SLIDES_DIR / slide_file
    page.goto(f"file://{path.resolve()}")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(500)

    screenshot_name = slide_file.replace(".html", ".png")
    page.screenshot(path=str(SCREENSHOTS_DIR / screenshot_name), full_page=True)
    print(f"OK: {screenshot_name}")

    browser.close()

print(f"\nScreenshot saved to: {SCREENSHOTS_DIR / screenshot_name}")
