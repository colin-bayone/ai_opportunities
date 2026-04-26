"""
Chart Screenshot Tool

Takes high-resolution screenshots of mermaid chart HTML files using Playwright.
Captures the SVG element directly at 2x device scale for print-quality output.

Usage:
    python3 screenshot_chart.py <html_file> [output_png]
"""

import sys
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

DEVICE_SCALE = 2


async def screenshot_chart(html_path: str, output_path: str = None) -> str:
    html_path = Path(html_path).resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    if output_path is None:
        output_path = html_path.with_suffix('.png')
    else:
        output_path = Path(output_path).resolve()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(
            viewport={'width': 1400, 'height': 2000},
            device_scale_factor=DEVICE_SCALE
        )

        await page.goto(f"file://{html_path}", wait_until='networkidle')
        await page.wait_for_timeout(3000)

        # Get the SVG's full rendered bounds including any overflow from post-render JS
        bounds = await page.evaluate('''() => {
            const svg = document.querySelector('.mermaid svg');
            if (!svg) return null;
            const bbox = svg.getBBox();
            const ctm = svg.getScreenCTM();
            return {
                x: bbox.x * ctm.a + ctm.e,
                y: bbox.y * ctm.d + ctm.f,
                width: bbox.width * ctm.a,
                height: bbox.height * ctm.d
            };
        }''')

        if not bounds:
            raise RuntimeError("No SVG found in the page")

        pad = 20
        await page.screenshot(
            path=str(output_path),
            type='png',
            clip={
                'x': max(0, bounds['x'] - pad),
                'y': max(0, bounds['y'] - pad),
                'width': bounds['width'] + pad * 2,
                'height': bounds['height'] + pad * 2,
            }
        )

        await browser.close()

    return str(output_path)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    html_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Capturing chart: {html_path}")

    try:
        result = asyncio.run(screenshot_chart(html_path, output_path))
        print(f"  Saved to: {result}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
