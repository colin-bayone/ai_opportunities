"""
Take 4K screenshots of HTML slides using Playwright.
Viewport: 1100x688 at 4x DPI = 4400x2752 output. Output: pngs/<slide_name>.png
"""
import glob
import os
import sys
from playwright.sync_api import sync_playwright

EXPORT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_DIR = os.path.join(EXPORT_DIR, "pngs")


def screenshot_slides(file_filter=None):
    os.makedirs(PNG_DIR, exist_ok=True)

    if file_filter:
        html_files = [os.path.join(EXPORT_DIR, f) for f in file_filter if os.path.exists(os.path.join(EXPORT_DIR, f))]
    else:
        html_files = sorted(glob.glob(os.path.join(EXPORT_DIR, "slide_*.html")))

    print(f"Screenshotting {len(html_files)} slides at 3840x2400...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1100, "height": 688}, device_scale_factor=4)

        for path in html_files:
            name = os.path.basename(path)
            png_name = name.replace(".html", ".png")
            png_path = os.path.join(PNG_DIR, png_name)

            page.goto("file://" + os.path.abspath(path))
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(500)
            page.screenshot(path=png_path, full_page=False)

            size_kb = os.path.getsize(png_path) / 1024
            print(f"  {png_name} ({size_kb:.0f} KB)")

        browser.close()
    print("Done.")


if __name__ == "__main__":
    screenshot_slides(sys.argv[1:] if len(sys.argv) > 1 else None)
