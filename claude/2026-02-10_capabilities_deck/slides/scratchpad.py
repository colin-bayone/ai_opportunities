#!/usr/bin/env python3
"""
Quick screenshot utility for reviewing HTML slides.
Usage: python scratchpad.py [slide_number or filename]
"""

import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

SLIDES_DIR = Path(__file__).parent

def screenshot_file(html_path: Path, output_path: Path = None):
    """Take a screenshot of an HTML file."""
    if output_path is None:
        output_path = Path(f"/tmp/{html_path.stem}.png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1200, "height": 900})
        page.goto(f"file://{html_path.absolute()}")
        page.screenshot(path=str(output_path), full_page=True)
        browser.close()

    print(f"Screenshot saved: {output_path}")
    return output_path

def screenshot_slides(*slide_nums):
    """Screenshot specific slides by number, or all if none specified."""
    html_files = sorted(SLIDES_DIR.glob("*.html"))

    if not slide_nums:
        # Screenshot all
        targets = html_files
    else:
        # Match by number prefix
        targets = []
        for num in slide_nums:
            prefix = f"{int(num):02d}_"
            matches = [f for f in html_files if f.name.startswith(prefix)]
            targets.extend(matches)

    for html_file in targets:
        screenshot_file(html_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Could be slide numbers or a filename
        args = sys.argv[1:]
        if args[0].endswith(".html"):
            screenshot_file(Path(args[0]))
        else:
            screenshot_slides(*args)
    else:
        # Default: screenshot slides 1-3 for current review
        screenshot_slides(1, 2, 3)
