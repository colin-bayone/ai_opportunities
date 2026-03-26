"""Screenshot slide 03 and the Ariat source slide for side-by-side comparison."""
from playwright.sync_api import sync_playwright
from pathlib import Path

SLIDE_03 = Path(__file__).parent / "slide_03_client_logos.html"
ARIAT_02 = Path(__file__).parent.parent.parent / (
    "2026-03-19_pptx_extractor_skill/source/"
    "BayOne-Overview-Ariat- GCC - Feb-2026_COLIN_EDITS/"
    "slide_02/slide_02.png"
)
OUT_DIR = Path(__file__).parent

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 800})

    # Screenshot our slide 03
    page.goto(f"file://{SLIDE_03.resolve()}")
    page.wait_for_load_state("networkidle")
    out_path = OUT_DIR / "screenshot_slide_03.png"
    page.screenshot(path=str(out_path), full_page=True)
    print(f"Saved: {out_path}")

    browser.close()

print(f"\nAriat source PNG for comparison: {ARIAT_02}")
print(f"Exists: {ARIAT_02.exists()}")
