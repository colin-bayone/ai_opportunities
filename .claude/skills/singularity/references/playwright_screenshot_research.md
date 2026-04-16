# Playwright Screenshot Research: High-Resolution Chart Capture for Print

**Date:** 2026-04-14
**Context:** Capturing mermaid diagrams rendered in HTML as high-resolution PNG images for embedding in printed consulting deliverables (8.5x11 portrait, BayOne design system).

---

## Table of Contents

1. [Core Concepts: How Playwright Screenshots Work](#1-core-concepts)
2. [device_scale_factor and Output Resolution](#2-device_scale_factor)
3. [Viewport Size and What Gets Captured](#3-viewport-size)
4. [full_page: True Behavior](#4-full_page)
5. [Element-Level Screenshots](#5-element-screenshots)
6. [The screenshot scale Parameter: "css" vs "device"](#6-scale-parameter)
7. [Rendering at a Specific Physical Size for Print](#7-physical-size-for-print)
8. [Forcing Content to Fill the Viewport](#8-forcing-content-fill)
9. [Waiting for Mermaid Render Completion](#9-waiting-for-mermaid)
10. [The style Parameter: Injecting CSS at Screenshot Time](#10-style-parameter)
11. [Transparent Backgrounds with omit_background](#11-transparent-backgrounds)
12. [How mermaid-cli (mmdc) Handles Rendering](#12-mermaid-cli)
13. [Best Practices for Print-Quality Chart Screenshots](#13-best-practices)
14. [Complete Working Script: Print-Quality Mermaid Chart Capture](#14-complete-script)
15. [Quick Reference: DPI/Pixel Calculations](#15-dpi-calculations)
16. [Current Project State](#16-current-project-state)

---

## 1. Core Concepts: How Playwright Screenshots Work <a name="1-core-concepts"></a>

Playwright screenshots are rasterizations of the browser's rendered page. The output PNG dimensions are determined by a combination of three factors:

1. **Viewport size** (CSS pixels): The logical width and height of the browser window.
2. **device_scale_factor** (DPR): A multiplier that determines how many physical pixels map to each CSS pixel.
3. **screenshot scale parameter**: Whether the output uses CSS pixel dimensions or device pixel dimensions.

The relationship:

```
Output pixel width  = viewport_width  x device_scale_factor  (when scale="device")
Output pixel height = viewport_height x device_scale_factor  (when scale="device")

Output pixel width  = viewport_width   (when scale="css")
Output pixel height = viewport_height  (when scale="css")
```

This means there are two independent levers for controlling output resolution:
- Make the viewport larger (content reflows to fill more CSS pixels)
- Increase device_scale_factor (content renders at higher pixel density without reflowing)

---

## 2. device_scale_factor and Output Resolution <a name="2-device_scale_factor"></a>

### What It Does

`device_scale_factor` emulates a high-DPI display. It is set when creating a browser context and cannot be changed after context creation (there is no `page.setDeviceScaleFactor()`).

- **device_scale_factor=1**: Standard display. 1 CSS pixel = 1 device pixel.
- **device_scale_factor=2**: Retina/HiDPI. 1 CSS pixel = 4 device pixels (2x2). Screenshot output is 2x the viewport dimensions.
- **device_scale_factor=3**: Super HiDPI (iPhone Pro-class). Screenshot output is 3x viewport.

### How It Affects Rendering

The browser renders text, SVG paths, CSS borders, and all vector content at the higher pixel density. This means:
- Text is sharper (subpixel-level rendering at the higher resolution)
- SVG diagrams render with smoother curves and lines
- CSS borders and shadows render at full fidelity
- Raster images (if any) do NOT benefit unless they have `srcset` or are SVG

### Code Example

```python
from playwright.async_api import async_playwright

async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)

    # Standard resolution: 1400x2000 viewport -> 1400x2000 PNG
    context_1x = await browser.new_context(
        viewport={"width": 1400, "height": 2000},
        device_scale_factor=1
    )

    # High resolution: 1400x2000 viewport -> 2800x4000 PNG
    context_2x = await browser.new_context(
        viewport={"width": 1400, "height": 2000},
        device_scale_factor=2
    )

    # Ultra resolution: 1400x2000 viewport -> 4200x6000 PNG
    context_3x = await browser.new_context(
        viewport={"width": 1400, "height": 2000},
        device_scale_factor=3
    )
```

### Key Constraint

`device_scale_factor` must be set at context creation. You cannot change it per-page or per-screenshot. If you need different scale factors for different captures, create separate contexts.

---

## 3. Viewport Size and What Gets Captured <a name="3-viewport-size"></a>

### Default Screenshot (full_page=False)

When `full_page` is not set (or set to False), the screenshot captures exactly the viewport rectangle:
- Width = viewport width
- Height = viewport height
- Content below the fold is not captured
- Content that overflows horizontally is not captured

### How Viewport Affects Layout

The viewport width determines CSS layout. A wider viewport means:
- Responsive layouts shift to wider breakpoints
- Elements with `width: 100%` stretch wider
- Mermaid diagrams with `useMaxWidth: true` expand to fill the container

The viewport height affects:
- What portion of the page is visible in a non-full-page screenshot
- Where `100vh` CSS units resolve to
- Whether `min-height: 100vh` centered content appears centered

### Setting Viewport

Two approaches:

```python
# At context creation (preferred for screenshot scripts)
context = await browser.new_context(
    viewport={"width": 1400, "height": 2000}
)

# After page creation (can be changed dynamically)
page = await context.new_page()
await page.set_viewport_size({"width": 1400, "height": 2000})
```

### Important: Viewport Width is Always Respected

Even with `full_page=True`, the viewport width determines the screenshot width. Only the height is overridden to capture the full document. This means you must set the viewport width to match your desired output width (in CSS pixels, before device_scale_factor multiplication).

---

## 4. full_page: True Behavior <a name="4-full_page"></a>

### What It Does

`full_page=True` captures the entire scrollable document, not just the visible viewport.

```python
await page.screenshot(path="output.png", full_page=True)
```

### What Determines the Captured Area

- **Width**: Always the viewport width. Not affected by `full_page`.
- **Height**: The `document.body.scrollHeight` -- the total scrollable height of the page.

### When to Use It

Use `full_page=True` when:
- Your HTML content extends beyond the viewport height
- You want to capture an entire document without calculating exact height
- The content height varies between charts

### When NOT to Use It

Avoid `full_page=True` when:
- You want a fixed output size (use a fixed viewport instead)
- You need to capture a specific element (use locator screenshot instead)
- The page has a `body { min-height: 100vh }` and the content is shorter than the viewport -- `full_page` may still capture only the viewport height if there is no scrollable overflow

### Known Limitation

`full_page=True` depends on the scrollable content being on the `<body>` element. If your page uses a scrollable `<div>` container with `overflow: auto`, the full_page option may capture only the viewport, not the full scrollable content inside that div.

### Workaround for Fixed Capture Size

If you want a specific pixel output regardless of content size, set the viewport to the exact CSS pixel dimensions you want and do NOT use `full_page`:

```python
# Capture exactly 1400x2000 CSS pixels (2800x4000 at 2x)
context = await browser.new_context(
    viewport={"width": 1400, "height": 2000},
    device_scale_factor=2
)
page = await context.new_page()
await page.goto(url)
await page.screenshot(path="output.png")  # No full_page
```

---

## 5. Element-Level Screenshots <a name="5-element-screenshots"></a>

### Locator Screenshot

Playwright can screenshot a single element, clipped to that element's bounding box:

```python
# Screenshot a specific element
await page.locator("svg").screenshot(path="chart.png")

# Screenshot by CSS selector
await page.locator(".mermaid svg").screenshot(path="diagram.png")

# Screenshot by ID
await page.locator("#my-chart").screenshot(path="chart.png")
```

### How It Works

1. Playwright waits for the element to be actionable (visible, stable)
2. Scrolls the element into view if needed
3. Calculates the element's bounding box via `getBoundingClientRect()`
4. Captures a screenshot clipped to that bounding box

### Resolution with device_scale_factor

The element screenshot respects `device_scale_factor`. If the SVG renders at 800x600 CSS pixels with `device_scale_factor=2`, the output PNG is 1600x1200 pixels.

### Capturing SVG at Maximum Resolution

For a mermaid SVG that needs to be as large as possible:

```python
async with async_playwright() as p:
    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(
        viewport={"width": 1400, "height": 2000},
        device_scale_factor=3  # 3x resolution
    )
    page = await context.new_page()
    await page.goto(f"file://{html_path}")
    await page.wait_for_load_state('networkidle')

    # Wait for mermaid to render
    await page.wait_for_selector('.mermaid svg')
    await asyncio.sleep(2)  # Allow post-render JS to complete

    # Capture just the SVG element
    svg = page.locator('.mermaid svg')
    await svg.screenshot(path="chart_highres.png")
```

### Bounding Box Access

You can also get the bounding box programmatically:

```python
box = await page.locator('.mermaid svg').bounding_box()
# box = {"x": 50, "y": 100, "width": 800, "height": 1200}
```

This is useful for debugging sizing issues or for using the `clip` parameter on `page.screenshot()`.

---

## 6. The screenshot scale Parameter: "css" vs "device" <a name="6-scale-parameter"></a>

### What It Controls

The `scale` parameter on `page.screenshot()` determines whether the output image dimensions reflect CSS pixels or device pixels.

```python
# Default behavior: output = viewport * device_scale_factor
await page.screenshot(path="device.png", scale="device")

# CSS mode: output = viewport dimensions (ignores device_scale_factor for sizing)
await page.screenshot(path="css.png", scale="css")
```

### Comparison Table

| Setting | Viewport | device_scale_factor | Output PNG Size |
|---------|----------|-------------------|-----------------|
| scale="device" (default) | 1400x2000 | 1 | 1400x2000 |
| scale="device" (default) | 1400x2000 | 2 | 2800x4000 |
| scale="device" (default) | 1400x2000 | 3 | 4200x6000 |
| scale="css" | 1400x2000 | 1 | 1400x2000 |
| scale="css" | 1400x2000 | 2 | 1400x2000 |
| scale="css" | 1400x2000 | 3 | 1400x2000 |

### When to Use "css"

Use `scale="css"` when you need consistent output dimensions regardless of the device emulation context. This is rare for print-quality capture; you almost always want `scale="device"` (the default) to take advantage of higher `device_scale_factor`.

### For Print-Quality Charts

Always use the default `scale="device"` with an appropriate `device_scale_factor`. The "css" mode discards the extra resolution from high DPI emulation.

---

## 7. Rendering at a Specific Physical Size for Print <a name="7-physical-size-for-print"></a>

### The Problem

Playwright works in CSS pixels and device pixels. There is no built-in "render at 7.5 inches by 9 inches at 300 DPI" option. You must calculate the required pixel dimensions yourself.

### The Formula

```
pixels = inches x DPI
```

### Example: Chart for an 8.5x11 Document with 0.5-inch Margins

Print area: 7.5 inches wide x 10 inches tall (after margins)

| Target DPI | Viewport (CSS px) | device_scale_factor | Output PNG Size |
|-----------|-------------------|-------------------|-----------------|
| 150 DPI | 1125 x 1500 | 1 | 1125 x 1500 |
| 150 DPI | 563 x 750 | 2 | 1125 x 1500 |
| 300 DPI | 2250 x 3000 | 1 | 2250 x 3000 |
| 300 DPI | 1125 x 1500 | 2 | 2250 x 3000 |
| 300 DPI | 750 x 1000 | 3 | 2250 x 3000 |

### Recommended Approach for Print

Use a viewport that matches the layout you want (reasonable CSS pixel width for the content to reflow properly) and a device_scale_factor that gets you to the target pixel count.

For a chart that fills 7.5 inches wide at 300 DPI:
- Target output: 2250 pixels wide
- Best approach: viewport width=1125, device_scale_factor=2 (output: 2250px)
- Alternative: viewport width=750, device_scale_factor=3 (output: 2250px)

The first approach (1125px viewport) is better because mermaid diagrams have reasonable room to lay out at 1125px. At 750px the viewport may be too narrow for complex diagrams.

### Complete Example

```python
import asyncio
from playwright.async_api import async_playwright

# Target: 7.5" x 5" chart area at 300 DPI
TARGET_WIDTH_INCHES = 7.5
TARGET_HEIGHT_INCHES = 5.0
TARGET_DPI = 300
DEVICE_SCALE = 2

# Calculate viewport
viewport_width = int((TARGET_WIDTH_INCHES * TARGET_DPI) / DEVICE_SCALE)   # 1125
viewport_height = int((TARGET_HEIGHT_INCHES * TARGET_DPI) / DEVICE_SCALE)  # 750

# Output will be: 2250 x 1500 pixels (7.5" x 5" at 300 DPI)

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": viewport_width, "height": viewport_height},
            device_scale_factor=DEVICE_SCALE
        )
        page = await context.new_page()
        await page.goto(f"file:///path/to/chart.html")
        await page.wait_for_load_state('networkidle')
        await asyncio.sleep(3)  # Wait for mermaid render

        await page.screenshot(path="chart_300dpi.png")
        await browser.close()

asyncio.run(capture())
```

### Using page.pdf() for True Physical Dimensions

Playwright's `page.pdf()` accepts physical units directly, but only generates PDF output (not PNG):

```python
await page.pdf(
    path="output.pdf",
    width="7.5in",
    height="10in",
    margin={"top": "0in", "bottom": "0in", "left": "0in", "right": "0in"},
    print_background=True
)
```

Supported units: `px`, `in`, `cm`, `mm`. This is useful if the final deliverable is PDF, but not for generating PNG images for HTML embedding.

### Emulating Print Media

If your CSS has `@media print` rules, emulate print media before capturing:

```python
await page.emulate_media(media="print")
await page.screenshot(path="print_view.png")
```

This does NOT change physical dimensions -- it only activates print-specific CSS rules.

---

## 8. Forcing Content to Fill the Viewport <a name="8-forcing-content-fill"></a>

### The Problem

Mermaid diagrams render at their natural size, which may be smaller than the viewport. When captured, the chart may appear small within a large white rectangle.

### Technique 1: CSS Transform Scale (Before Screenshot)

Inject CSS via `add_style_tag()` to scale the content up:

```python
await page.add_style_tag(content="""
    .mermaid svg {
        width: 100% !important;
        max-width: 100% !important;
    }
""")
```

### Technique 2: JavaScript Evaluation to Resize SVG

Use `page.evaluate()` to modify the SVG's `width` and `height` attributes after mermaid renders:

```python
await page.evaluate("""
    () => {
        const svg = document.querySelector('.mermaid svg');
        if (!svg) return;
        const viewBox = svg.getAttribute('viewBox');
        if (viewBox) {
            // Keep the viewBox but stretch to fill container
            svg.style.width = '100%';
            svg.style.height = '100%';
            svg.removeAttribute('width');
            svg.removeAttribute('height');
        }
    }
""")
```

### Technique 3: Measure-Then-Resize Viewport

Measure the SVG's natural size and resize the viewport to match:

```python
# Let mermaid render first
await page.wait_for_selector('.mermaid svg')
await asyncio.sleep(2)

# Get the SVG's natural bounding box
bbox = await page.evaluate("""
    () => {
        const svg = document.querySelector('.mermaid svg');
        if (!svg) return null;
        const rect = svg.getBoundingClientRect();
        return { width: Math.ceil(rect.width), height: Math.ceil(rect.height) };
    }
""")

if bbox:
    # Resize viewport to exactly fit the SVG
    await page.set_viewport_size({
        "width": bbox["width"] + 40,   # Add padding
        "height": bbox["height"] + 40
    })

    await page.screenshot(path="tight_fit.png")
```

### Technique 4: Use the style Parameter at Screenshot Time

The `style` parameter applies CSS only during the screenshot capture:

```python
await page.screenshot(
    path="chart.png",
    style="""
        body { margin: 0; padding: 0; }
        .mermaid svg { width: 100vw !important; }
    """
)
```

This is cleaner than `add_style_tag()` because it does not permanently modify the page.

### Technique 5: Design the HTML to Fill the Viewport

The most reliable approach is to design the chart HTML so the content naturally fills its container. The existing chart HTML files in this project already do this with:

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
}
```

Combined with mermaid's `useMaxWidth: true`, the diagram expands to fill the available width.

---

## 9. Waiting for Mermaid Render Completion <a name="9-waiting-for-mermaid"></a>

### The Problem

Mermaid renders asynchronously. Taking a screenshot too early captures a blank page or partially rendered diagram.

### Approach 1: Hard Wait (Current Project Approach)

```python
await page.wait_for_load_state('networkidle')
await asyncio.sleep(6)  # Wait for mermaid
```

This works but wastes time and is fragile (may not be long enough on slow systems).

### Approach 2: Wait for SVG Element (Better)

```python
await page.wait_for_selector('.mermaid svg', state='attached', timeout=15000)
```

This returns as soon as mermaid creates the SVG element in the DOM.

### Approach 3: Wait for JavaScript Condition (Best)

Use `wait_for_function` to wait for a custom condition:

```python
# Wait for mermaid SVG to have child elements (fully rendered)
await page.wait_for_function("""
    () => {
        const svg = document.querySelector('.mermaid svg');
        return svg && svg.querySelectorAll('.node').length > 0;
    }
""", timeout=15000)
```

### Approach 4: Signal from the Page

Modify the chart HTML to set a flag when rendering is complete:

```javascript
// In the chart HTML
async function render() {
    await mermaid.run({ querySelector: '.mermaid' });
    // Post-render fixes...
    window.__MERMAID_READY = true;  // Signal to Playwright
}
render();
```

Then in Python:

```python
await page.wait_for_function("() => window.__MERMAID_READY === true", timeout=15000)
```

### Recommended Approach

Combine selector wait + short sleep for post-render JavaScript:

```python
await page.wait_for_load_state('networkidle')
await page.wait_for_selector('.mermaid svg', state='attached', timeout=15000)
await asyncio.sleep(1)  # Allow post-render JS (title bar styling, padding fixes)
```

Or, if the chart HTML sets `window.__MERMAID_READY`, use approach 4 for deterministic waiting.

---

## 10. The style Parameter: Injecting CSS at Screenshot Time <a name="10-style-parameter"></a>

### What It Does

The `style` parameter on `page.screenshot()` injects a temporary stylesheet that applies only during the screenshot capture. It pierces Shadow DOM and applies to inner frames.

```python
await page.screenshot(
    path="output.png",
    style="""
        .animated-element { animation: none !important; }
        .tooltip { display: none !important; }
    """
)
```

### Use Cases for Chart Capture

1. **Remove background for compositing**: Make the background transparent while keeping diagram visible
2. **Hide UI elements**: Remove browser-like chrome or interactive controls
3. **Force sizing**: Apply `width: 100%` to SVG during capture only
4. **Disable animations**: Freeze any CSS transitions that might cause inconsistent captures

### Comparison with add_style_tag()

| Feature | style parameter | add_style_tag() |
|---------|----------------|-----------------|
| Scope | Screenshot only | Permanent on page |
| Shadow DOM | Pierces | Does not pierce |
| Reversible | Automatic | Must remove manually |
| Use case | Screenshot-specific overrides | Persistent layout changes |

---

## 11. Transparent Backgrounds with omit_background <a name="11-transparent-backgrounds"></a>

### What It Does

Setting `omit_background=True` produces a PNG with a transparent background instead of white:

```python
await page.screenshot(
    path="chart_transparent.png",
    omit_background=True
)
```

### Requirements

- Output must be PNG (not JPEG -- JPEG does not support transparency)
- The page's `<body>` and `<html>` must not have an opaque background color set, or the transparency will be covered by CSS backgrounds

### When to Use for Charts

Useful when embedding a chart PNG into an HTML document that has its own background color scheme. The chart floats over the document background without a white rectangle.

### Caveat

If your chart HTML sets `background: white` on the body (as the current chart files do), you need to override this:

```python
await page.screenshot(
    path="chart_transparent.png",
    omit_background=True,
    style="body { background: transparent !important; }"
)
```

---

## 12. How mermaid-cli (mmdc) Handles Rendering <a name="12-mermaid-cli"></a>

### Overview

mermaid-cli (`mmdc`) is a Node.js tool that uses Puppeteer (not Playwright) under the hood. Understanding its approach is useful for comparison.

### Key Parameters

```bash
mmdc -i input.mmd -o output.png --width 1400 --height 2000 --scale 2
```

- `--width` (default: 800): Puppeteer viewport width in CSS pixels
- `--height` (default: 600): Puppeteer viewport height in CSS pixels
- `--scale` (default: 1): Passed to Puppeteer as `deviceScaleFactor`
- `--cssFile`: Custom CSS injected into the rendered page
- `--configFile`: Mermaid configuration JSON
- `--puppeteerConfigFile`: Puppeteer launch/viewport configuration JSON

### How Scale Maps to deviceScaleFactor

The `--scale` parameter is directly passed to Puppeteer's viewport as `deviceScaleFactor`. So `--scale 2` with `--width 800` produces a 1600-pixel-wide PNG.

### Puppeteer Config File Example

```json
{
    "headless": true,
    "args": ["--no-sandbox"],
    "defaultViewport": {
        "width": 1400,
        "height": 2000,
        "deviceScaleFactor": 2
    }
}
```

### Comparison: mmdc vs Custom Playwright Script

| Feature | mmdc | Custom Playwright Script |
|---------|------|------------------------|
| Ease of use | One-line command | Full script needed |
| Input | .mmd file (raw mermaid) | HTML file with mermaid |
| Post-render JS | Not supported | Full control |
| CSS customization | --cssFile only | Full page CSS control |
| Title bar styling | Not possible | Yes (post-render JS) |
| Wait strategy | Internal timing | Configurable |
| Scale control | --scale flag | device_scale_factor |
| Browser | Puppeteer (Chromium) | Playwright (Chromium/Firefox/WebKit) |

For this project, the custom Playwright approach is required because we use post-render JavaScript to style title bars, adjust node heights, and apply FontAwesome icons -- none of which mmdc supports.

---

## 13. Best Practices for Print-Quality Chart Screenshots <a name="13-best-practices"></a>

### Resolution Guidelines

| Print Context | Minimum DPI | Recommended DPI | Notes |
|---------------|-------------|-----------------|-------|
| Professional print (close viewing) | 300 | 300 | Business cards, proposals, reports |
| Magazine/standard print | 150 | 200-300 | Acceptable for diagrams with large text |
| Large format (posters, banners) | 100 | 150 | Viewed from distance |
| Screen/PDF embedding | 72-96 | 150 | Retina screens benefit from 2x |
| Consulting deliverable (our case) | 150 | 200-300 | 8.5x11 viewed at arm's length |

### Chart Area Calculations for 8.5x11 Document

Typical BayOne deliverable layout:
- Page: 8.5" x 11"
- Margins: 0.5" each side
- Usable area: 7.5" x 10"
- Chart typically occupies about 60-80% of a page: approximately 7.5" x 6-8"

For a chart area of 7.5" x 9" at 300 DPI:
- Output needed: 2250 x 2700 pixels
- Configuration: viewport 1125x1350, device_scale_factor=2

### Checklist for High-Quality Chart Capture

1. **Set viewport to match content layout needs** -- 1100-1400px wide is typical for mermaid diagrams
2. **Use device_scale_factor=2 minimum** for print-quality output
3. **Use scale="device"** (the default) -- never use "css" for print capture
4. **Wait deterministically** for mermaid render (selector wait + signal flag, not hard sleep)
5. **Use PNG format** (lossless) -- never JPEG for charts with text and lines
6. **Design HTML to fill viewport** -- `body { display: flex; justify-content: center; min-height: 100vh; }` with `useMaxWidth: true`
7. **Apply overflow: visible** CSS fixes on mermaid foreignObject elements
8. **Test the output** -- open the PNG at 100% zoom to verify text readability
9. **Disable animations** if any CSS transitions exist: use `animations="disabled"` parameter
10. **Use headless=True** -- headed mode can introduce OS-specific rendering differences

### File Size Considerations

A 2800x4000 PNG (the current output) at 8-bit RGB is approximately 1-4 MB depending on diagram complexity. This is acceptable for embedded deliverables but large for web. For web use, consider:
- Generating a separate lower-resolution version
- Using SVG export instead (mermaid diagrams are inherently vector)

---

## 14. Complete Working Script: Print-Quality Mermaid Chart Capture <a name="14-complete-script"></a>

### Basic Version (Matches Current Project Pattern)

```python
#!/usr/bin/env python3
"""Capture a mermaid chart HTML as a high-resolution PNG for print embedding."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML_FILE = Path("/path/to/chart.html")
OUTPUT_PATH = Path("/path/to/chart.png")

# Print target: 7.5" wide at 300 DPI = 2250px output width
VIEWPORT_WIDTH = 1400
VIEWPORT_HEIGHT = 2000
DEVICE_SCALE = 2  # Output: 2800x4000 px

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            device_scale_factor=DEVICE_SCALE
        )
        page = await context.new_page()

        await page.goto(f"file://{HTML_FILE.resolve()}")
        await page.wait_for_load_state('networkidle')

        # Wait for mermaid SVG to render with actual content
        await page.wait_for_selector('.mermaid svg .node', timeout=15000)
        await asyncio.sleep(1)  # Post-render JS (title bars, padding)

        await page.screenshot(path=str(OUTPUT_PATH), full_page=True)
        print(f"Saved: {OUTPUT_PATH} ({VIEWPORT_WIDTH * DEVICE_SCALE}x px)")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

### Advanced Version (Signal-Based Wait, Element Capture, Flexible)

```python
#!/usr/bin/env python3
"""
Advanced chart capture script with:
- Signal-based mermaid wait (no hard sleep)
- Optional element-level capture
- Configurable DPI targeting
- Print area specification in inches
"""
import asyncio
import argparse
from pathlib import Path
from playwright.async_api import async_playwright


def calc_viewport(width_inches, height_inches, dpi, scale_factor):
    """Calculate viewport CSS pixels from physical print dimensions."""
    return {
        "width": int((width_inches * dpi) / scale_factor),
        "height": int((height_inches * dpi) / scale_factor),
    }


async def capture_chart(
    html_path: Path,
    output_path: Path,
    width_inches: float = 7.5,
    height_inches: float = 10.0,
    dpi: int = 300,
    device_scale: int = 2,
    element_selector: str = None,
    transparent: bool = False,
    use_signal: bool = False,
):
    viewport = calc_viewport(width_inches, height_inches, dpi, device_scale)
    output_w = viewport["width"] * device_scale
    output_h = viewport["height"] * device_scale

    print(f"Viewport: {viewport['width']}x{viewport['height']} CSS px")
    print(f"Output:   {output_w}x{output_h} px ({dpi} DPI at {width_inches}\"x{height_inches}\")")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport=viewport,
            device_scale_factor=device_scale,
        )
        page = await context.new_page()

        await page.goto(f"file://{html_path.resolve()}")
        await page.wait_for_load_state("networkidle")

        # Wait for mermaid render
        if use_signal:
            # Requires chart HTML to set window.__MERMAID_READY = true
            await page.wait_for_function(
                "() => window.__MERMAID_READY === true", timeout=15000
            )
        else:
            await page.wait_for_selector(".mermaid svg", timeout=15000)
            await asyncio.sleep(2)  # Post-render JS settling

        # Capture
        screenshot_opts = {
            "path": str(output_path),
            "type": "png",
        }

        if transparent:
            screenshot_opts["omit_background"] = True
            screenshot_opts["style"] = "body { background: transparent !important; }"

        if element_selector:
            await page.locator(element_selector).screenshot(**screenshot_opts)
        else:
            screenshot_opts["full_page"] = True
            await page.screenshot(**screenshot_opts)

        print(f"Saved: {output_path}")
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture chart HTML as print-quality PNG")
    parser.add_argument("html_file", type=Path, help="Input HTML file")
    parser.add_argument("output_file", type=Path, help="Output PNG file")
    parser.add_argument("--width", type=float, default=7.5, help="Print width in inches")
    parser.add_argument("--height", type=float, default=10.0, help="Print height in inches")
    parser.add_argument("--dpi", type=int, default=300, help="Target DPI")
    parser.add_argument("--scale", type=int, default=2, help="Device scale factor")
    parser.add_argument("--element", type=str, help="CSS selector to capture (instead of full page)")
    parser.add_argument("--transparent", action="store_true", help="Transparent background")
    parser.add_argument("--signal", action="store_true", help="Use window.__MERMAID_READY signal")

    args = parser.parse_args()
    asyncio.run(capture_chart(
        args.html_file, args.output_file,
        width_inches=args.width, height_inches=args.height,
        dpi=args.dpi, device_scale=args.scale,
        element_selector=args.element,
        transparent=args.transparent,
        use_signal=args.signal,
    ))
```

### Batch Capture Script

```python
#!/usr/bin/env python3
"""Batch capture all chart HTML files in a directory."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

CHART_DIR = Path("/path/to/charts")
VIEWPORT_WIDTH = 1400
VIEWPORT_HEIGHT = 2000
DEVICE_SCALE = 2

async def main():
    html_files = sorted(CHART_DIR.glob("*.html"))
    if not html_files:
        print("No HTML files found")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            device_scale_factor=DEVICE_SCALE,
        )

        for html_file in html_files:
            output = html_file.with_suffix(".png")
            page = await context.new_page()

            await page.goto(f"file://{html_file.resolve()}")
            await page.wait_for_load_state("networkidle")
            await page.wait_for_selector(".mermaid svg", timeout=15000)
            await asyncio.sleep(2)

            await page.screenshot(path=str(output), full_page=True)
            print(f"  {html_file.name} -> {output.name}")

            await page.close()

        await browser.close()
    print(f"Captured {len(html_files)} charts.")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 15. Quick Reference: DPI/Pixel Calculations <a name="15-dpi-calculations"></a>

### Formula

```
output_pixels = inches x DPI
viewport_css_px = output_pixels / device_scale_factor
```

### Common Print Sizes (300 DPI, device_scale_factor=2)

| Print Area | Output Pixels | Viewport (CSS px) |
|-----------|--------------|-------------------|
| 7.5" x 10" (Letter, margins) | 2250 x 3000 | 1125 x 1500 |
| 7.5" x 5" (half page) | 2250 x 1500 | 1125 x 750 |
| 7.5" x 9" (chart + caption) | 2250 x 2700 | 1125 x 1350 |
| 6" x 4" (inline figure) | 1800 x 1200 | 900 x 600 |
| 10" x 7.5" (landscape) | 3000 x 2250 | 1500 x 1125 |

### Common Print Sizes (200 DPI, device_scale_factor=2)

| Print Area | Output Pixels | Viewport (CSS px) |
|-----------|--------------|-------------------|
| 7.5" x 10" | 1500 x 2000 | 750 x 1000 |
| 7.5" x 5" | 1500 x 1000 | 750 x 500 |
| 7.5" x 9" | 1500 x 1800 | 750 x 900 |

### Reverse Calculation: What DPI Are My Current PNGs?

Current project output: 2800 x 4000 pixels (viewport 1400x2000, device_scale_factor=2)

| Print Width (inches) | Effective DPI (horizontal) |
|----------------------|---------------------------|
| 7.5" | 373 DPI |
| 8.5" | 329 DPI |
| 6.0" | 467 DPI |

At 7.5 inches print width, the current 2800px output provides 373 DPI, which exceeds the 300 DPI threshold for professional print quality.

---

## 16. Current Project State <a name="16-current-project-state"></a>

### Existing Screenshot Scripts

Two capture scripts exist in the `sephora/edw_modernization/planning/` directory:

1. **`capture_screenshot.py`**: viewport 1600x1080, no device_scale_factor (defaults to 1), 6-second hard wait
2. **`screenshot_arch.py`**: viewport 1600x900, no device_scale_factor (defaults to 1), 8-second hard wait

Both use `full_page=True` and do not set `device_scale_factor`, meaning output is 1x resolution (1600px wide). For print, these would yield approximately 213 DPI at 7.5 inches -- below the 300 DPI threshold.

### Current Chart PNGs

The files in `sephora/qa_qe_playwright/deliverables/charts/` are all 2800x4000 pixels, suggesting they were captured with viewport=1400x2000 and device_scale_factor=2. At 7.5" print width, this provides 373 DPI -- well above the professional print threshold.

### Improvement Opportunities

1. **Replace hard sleep with deterministic wait**: Use `wait_for_selector('.mermaid svg .node')` plus `wait_for_function` for the signal flag pattern
2. **Add `window.__MERMAID_READY` signal** to chart HTML files after the `render()` function completes
3. **Parameterize the capture script** so chart dimensions can be configured per-chart (some charts are shorter than others)
4. **Consider element-level capture** for charts that do not fill the full viewport, to avoid excess whitespace in the output

---

## Sources

- [Playwright Screenshots Documentation](https://playwright.dev/docs/screenshots)
- [Playwright Python Emulation Documentation](https://playwright.dev/python/docs/emulation)
- [Playwright Python Page API](https://playwright.dev/python/docs/api/class-page)
- [Playwright Python Locator API](https://playwright.dev/python/docs/api/class-locator)
- [Playwright GitHub Issue #1468: How to make screenshot more sharp?](https://github.com/microsoft/playwright-python/issues/1468)
- [Playwright GitHub Issue #2134: page.setDeviceScaleFactor](https://github.com/microsoft/playwright/issues/2134)
- [Playwright GitHub Issue #13339: Unable to set viewport width and capture fullpage screenshot](https://github.com/microsoft/playwright/issues/13339)
- [Playwright GitHub Issue #12962: fullPage screenshot does not work with non-body scroll](https://github.com/microsoft/playwright/issues/12962)
- [Playwright GitHub Issue #16255: element screenshot with omitBackground](https://github.com/microsoft/playwright/issues/16255)
- [Puppeteer GitHub Issue #1329: How do I take a high resolution screenshot?](https://github.com/puppeteer/puppeteer/issues/1329)
- [mermaid-cli npm package](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
- [mermaid-cli DeepWiki: Command-Line Usage](https://deepwiki.com/mermaid-js/mermaid-cli/2.2-command-line-usage)
- [mermaid-cli DeepWiki: Configuration Options](https://deepwiki.com/mermaid-js/mermaid-cli/2.4-configuration-options)
- [Screenshot Settings in Playwright](https://www.programmablebrowser.com/posts/screenshot-settings-playwright/)
- [Checkly: Playwright Screenshots Guide](https://www.checklyhq.com/docs/learn/playwright/taking-screenshots/)
- [Liran Tal: Advanced Playwright Screenshot Patterns](https://lirantal.com/blog/advanced-usage-patterns-for-taking-page-element-screenshots-with-playwright)
- [PrintingForLess: Standard DPI & Image Resolution](https://www.printingforless.com/resources/image-resolution-for-printing/)
