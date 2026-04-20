# SVG Scaling in Browsers: Comprehensive Reference

**Date:** 2026-04-14
**Context:** Understanding SVG scaling mechanics for programmatically generated SVGs (mermaid.js, d3.js) embedded in HTML deliverables and captured via Playwright screenshots.

---

## 1. How `width`, `height`, and `viewBox` Interact

The SVG element has two distinct coordinate systems that interact to control rendering:

- **Viewport** (the display window): Defined by `width` and `height` attributes on the `<svg>` element. This is the physical space the SVG occupies on the page, measured in CSS pixels.
- **User coordinate system** (the drawing canvas): Defined by the `viewBox` attribute. This is the internal coordinate space that SVG content is drawn in.

The `viewBox` takes four parameters: `viewBox="min-x min-y width height"`:
- `min-x`, `min-y`: The origin point of the internal coordinate system
- `width`, `height`: The dimensions of the internal coordinate system in user units

### The Mapping

When both are present, the browser maps the viewBox coordinate system onto the viewport. This is where scaling occurs.

```html
<!-- Internal coordinates: 0-100 user units -->
<!-- Viewport: 400x200 CSS pixels -->
<!-- Result: each user unit = 4px horizontally, 2px vertically -->
<svg width="400" height="200" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

In this example, the 100x100 coordinate space is mapped to a 400x200 pixel viewport. Because the aspect ratios differ (1:1 vs 2:1), `preserveAspectRatio` determines the behavior (see Section 6).

### When Only `width` and `height` Are Set (No viewBox)

```html
<svg width="400" height="200">
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

The coordinate system is 1:1 with pixels. User unit values map directly to CSS pixels. The circle is drawn at (50px, 50px) with a 40px radius. The SVG viewport is 400x200 but the content only occupies a small portion of it. There is no scaling -- what you draw is what you get.

### When Only `viewBox` Is Set (No width/height)

```html
<svg viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

The SVG has an intrinsic aspect ratio (1:1 from the 100x100 viewBox) but no explicit size. The browser falls back to:
- In SVG2/HTML5: `width` and `height` default to `auto`, which resolves to `100%` of the containing block's width and uses the viewBox aspect ratio to calculate height.
- The SVG scales to fill its container width while maintaining aspect ratio.

This is the foundation of responsive SVG design.

### When All Three Are Present

```html
<svg width="800" height="400" viewBox="0 0 200 200">
  <rect width="200" height="200" fill="red"/>
</svg>
```

The 200x200 user coordinate space is mapped into an 800x400 viewport. The `preserveAspectRatio` attribute (default: `xMidYMid meet`) scales the content uniformly to fit, centering it with letterboxing as needed.

---

## 2. Specific Combinations and Their Behavior

### `width="100%"` with No viewBox

```html
<div style="width: 600px;">
  <svg width="100%" height="300">
    <circle cx="150" cy="150" r="100" fill="green"/>
  </svg>
</div>
```

**What happens:** The SVG viewport is 600px wide (100% of parent) and 300px tall. The coordinate system is 1:1 with pixels. The circle renders at its literal pixel coordinates (150, 150) with a 100px radius. If you resize the container, the viewport width changes but the content does not scale -- it just gets more or less viewport space around fixed-size content.

**Key problem:** Without a viewBox, the SVG has no intrinsic aspect ratio. Content does not scale. Browser behavior for height calculation varies:
- Chrome: May use the viewport height or default to 150px in some contexts
- Firefox: May use a 1:1 ratio to compute height if height is not explicit
- This inconsistency is a major reason to always include a viewBox.

### viewBox with No `width`/`height`

```html
<div style="width: 800px;">
  <svg viewBox="0 0 400 300">
    <rect width="400" height="300" fill="coral"/>
  </svg>
</div>
```

**What happens:** The SVG scales to fill the container (800px wide) and automatically calculates height from the viewBox aspect ratio (4:3), producing a 600px height. Content scales proportionally. This is the recommended responsive pattern.

### No viewBox, No `width`, No `height` (Bare SVG in HTML)

```html
<svg>
  <circle cx="50" cy="50" r="40" fill="blue"/>
</svg>
```

**What happens:** The browser uses a default size of 300x150 pixels (the CSS replaced element default). Content renders at 1:1 pixel coordinates. This is almost never what you want.

---

## 3. CSS `width`/`height` vs SVG Attributes

### Specificity and Override Rules

In SVG2, `width` and `height` on `<svg>` are classified as **geometry properties** (also called presentation attributes). They participate in the CSS cascade with specificity 0. This means:

1. Any CSS rule with specificity > 0 overrides the SVG attribute
2. An external stylesheet rule like `svg { width: 100%; }` overrides `<svg width="400">`
3. Inline styles (`style="width: 100%"`) override both

**Priority order (highest to lowest):**
```
1. inline style attribute (style="width: 500px")
2. CSS rules in <style> or external stylesheets (by specificity)
3. SVG presentation attributes (width="400")
4. Browser defaults
```

### Practical Example

```html
<style>
  .responsive-svg {
    width: 100%;
    height: auto;
  }
</style>

<!-- The CSS wins. SVG renders at 100% container width, not 400px. -->
<!-- Height is calculated from the viewBox aspect ratio. -->
<svg class="responsive-svg" width="400" height="400" viewBox="0 0 400 400">
  <rect width="400" height="400" fill="purple"/>
</svg>
```

### CSS `height: auto` Behavior

When CSS sets `height: auto` on an SVG:
- **With viewBox:** Height is calculated from the viewBox aspect ratio relative to the computed width. If the viewBox is `0 0 400 200` and the SVG renders at 800px wide, height becomes 400px.
- **Without viewBox:** Height defaults to 150px (CSS replaced element default) or may behave inconsistently across browsers.

### Important Caveat: `max-width` on SVG

```css
svg {
  max-width: 100%;
  height: auto;
}
```

This is the standard responsive image pattern and works well for SVGs with a viewBox. The SVG scales down to fit its container but never exceeds its intrinsic width.

---

## 4. Scaling to Fill Container While Maintaining Aspect Ratio

This is the most common requirement. There are three approaches depending on context.

### Approach A: viewBox + CSS (Recommended)

```html
<style>
  .chart-container {
    width: 100%;
    max-width: 1200px;
  }
  .chart-container svg {
    width: 100%;
    height: auto;
    display: block;
  }
</style>

<div class="chart-container">
  <svg viewBox="0 0 800 400">
    <!-- Content drawn in 800x400 coordinate space -->
    <!-- Scales to fill container width, height follows aspect ratio -->
  </svg>
</div>
```

**Requirements:**
- The SVG must have a `viewBox` attribute
- Remove or do not set explicit `width`/`height` attributes (or let CSS override them)
- `display: block` prevents inline spacing issues

### Approach B: viewBox + No Width/Height Attributes

```html
<svg viewBox="0 0 800 400">
  <!-- Scales to fill parent container width automatically -->
  <!-- Aspect ratio preserved by default (preserveAspectRatio="xMidYMid meet") -->
</svg>
```

This works because SVG2 defaults `width` and `height` to `auto` which resolves to 100% of the containing block. Simpler but less explicit.

### Approach C: The Padding-Bottom Hack (Legacy Browsers)

For older browsers that do not properly calculate height from viewBox aspect ratio:

```html
<style>
  .svg-wrapper {
    position: relative;
    width: 100%;
    padding-bottom: 50%; /* aspect ratio: height/width = 400/800 = 50% */
    height: 0;
    overflow: hidden;
  }
  .svg-wrapper svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
</style>

<div class="svg-wrapper">
  <svg viewBox="0 0 800 400" preserveAspectRatio="xMidYMid meet">
    <!-- Content here -->
  </svg>
</div>
```

The `padding-bottom` percentage is relative to the container's width, so `50%` creates a 2:1 aspect ratio container. The SVG fills it absolutely.

---

## 5. Scaling to Fill Container and Stretch (Ignoring Aspect Ratio)

Use `preserveAspectRatio="none"` combined with explicit sizing.

### Approach: Stretch to Fit

```html
<style>
  .stretch-container {
    width: 100%;
    height: 300px;
  }
  .stretch-container svg {
    width: 100%;
    height: 100%;
  }
</style>

<div class="stretch-container">
  <svg viewBox="0 0 800 400" preserveAspectRatio="none">
    <!-- Content stretches non-uniformly to fill the 100% x 300px container -->
    <rect width="800" height="400" fill="lightblue"/>
    <circle cx="400" cy="200" r="150" fill="orange"/>
    <!-- The circle will appear as an ellipse -->
  </svg>
</div>
```

**Critical:** `preserveAspectRatio="none"` must be on the SVG element, and a `viewBox` must be present for it to take effect.

### Without viewBox (Alternate Approach)

If you cannot add a viewBox but want content to stretch:

```html
<svg width="100%" height="100%" style="width: 100%; height: 100%;">
  <!-- Content is drawn at literal pixel coordinates -->
  <!-- No scaling occurs; content is clipped or has empty space -->
</svg>
```

This does not truly stretch content. Without a viewBox, there is no coordinate mapping to distort. The only way to get non-uniform scaling is with a viewBox + `preserveAspectRatio="none"`.

---

## 6. `preserveAspectRatio` Reference

### Syntax

```
preserveAspectRatio="<alignment> [<meet-or-slice>]"
```

**Default value:** `xMidYMid meet`

**Prerequisite:** A `viewBox` attribute must be present (except on `<image>` elements).

### Alignment Values

The alignment value has two components: X alignment and Y alignment.

| X Position | Y Position | Combined Value | Behavior |
|------------|------------|---------------|----------|
| xMin | YMin | `xMinYMin` | Align to top-left |
| xMid | YMin | `xMidYMin` | Center horizontally, align to top |
| xMax | YMin | `xMaxYMin` | Align to top-right |
| xMin | YMid | `xMinYMid` | Align to left, center vertically |
| xMid | YMid | `xMidYMid` | Center both (DEFAULT) |
| xMax | YMid | `xMaxYMid` | Align to right, center vertically |
| xMin | YMax | `xMinYMax` | Align to bottom-left |
| xMid | YMax | `xMidYMax` | Center horizontally, align to bottom |
| xMax | YMax | `xMaxYMax` | Align to bottom-right |
| (special) | (special) | `none` | Non-uniform scaling, stretches to fill |

### Meet vs Slice

**`meet` (default):** Scale the viewBox to fit entirely inside the viewport. The entire drawing is visible. Empty space (letterboxing) may appear. Analogous to CSS `background-size: contain` or `object-fit: contain`.

```html
<!-- 100x100 content in a 400x200 viewport -->
<!-- Content scales to 200x200 (limited by height), centered horizontally -->
<svg width="400" height="200" viewBox="0 0 100 100"
     preserveAspectRatio="xMidYMid meet">
  <rect width="100" height="100" fill="blue"/>
</svg>
```

**`slice`:** Scale the viewBox to cover the entire viewport. Content overflows and is clipped. No empty space. Analogous to CSS `background-size: cover` or `object-fit: cover`.

```html
<!-- 100x100 content in a 400x200 viewport -->
<!-- Content scales to 400x400 (fills width), top/bottom clipped -->
<svg width="400" height="200" viewBox="0 0 100 100"
     preserveAspectRatio="xMidYMid slice">
  <rect width="100" height="100" fill="blue"/>
</svg>
```

**`none`:** Non-uniform scaling. The viewBox is stretched or compressed to exactly fill the viewport dimensions. The `meet`/`slice` keyword is ignored when `none` is specified.

```html
<!-- 100x100 content stretched to fill 400x200 viewport -->
<!-- Horizontal scale: 4x, Vertical scale: 2x -->
<svg width="400" height="200" viewBox="0 0 100 100"
     preserveAspectRatio="none">
  <circle cx="50" cy="50" r="40" fill="blue"/>
  <!-- Circle becomes an ellipse: 320px wide, 160px tall -->
</svg>
```

### Common Usage Patterns

| Goal | Value |
|------|-------|
| Center and fit (default, most common) | `xMidYMid meet` |
| Pin to top-left while fitting | `xMinYMin meet` |
| Fill viewport, crop overflow from center | `xMidYMid slice` |
| Fill viewport, crop from bottom-right | `xMinYMin slice` |
| Stretch to exactly fill (distort) | `none` |

---

## 7. Playwright Screenshots of SVGs

### What Determines the Rendered Size

When Playwright takes a screenshot, the SVG is rendered by the browser's layout engine exactly as it would be in a real browser. The screenshot captures the rendered result. The factors that determine size are, in order of priority:

1. **CSS applied to the SVG element** (highest priority -- overrides attributes)
2. **SVG `width`/`height` attributes** (if no CSS overrides them)
3. **viewBox aspect ratio** (if width or height resolves to `auto`)
4. **Parent container dimensions** (if SVG uses percentage-based sizing)
5. **Playwright viewport size** (determines the available layout space)

### Viewport Configuration

```javascript
// Set viewport before navigation
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 }
});

// Or resize mid-test
await page.setViewportSize({ width: 1920, height: 1080 });
```

The viewport determines the available layout area. If an SVG has `width: 100%`, it will be 1920px wide in a 1920px viewport.

### Device Scale Factor

```javascript
const context = await browser.newContext({
  viewport: { width: 1920, height: 1080 },
  deviceScaleFactor: 2  // Retina: 2x pixel density
});
```

With `deviceScaleFactor: 2`, a 1920x1080 viewport produces a 3840x2160 pixel screenshot. The SVG renders at CSS dimensions but the screenshot captures at device pixel resolution. This is critical for high-quality SVG captures.

### Screenshot Approaches

**Full page screenshot:**
```javascript
await page.screenshot({ path: 'full.png', fullPage: true });
// Captures the entire scrollable page including off-viewport content
```

**Element screenshot (recommended for SVGs):**
```javascript
const svgElement = page.locator('svg.my-chart');
await svgElement.screenshot({ path: 'chart.png' });
// Captures exactly the bounding box of the SVG element
```

**Clip-based screenshot:**
```javascript
// Get the SVG's bounding box from the DOM
const bbox = await page.evaluate(() => {
  const svg = document.querySelector('svg.my-chart');
  const rect = svg.getBoundingClientRect();
  return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
});

await page.screenshot({ path: 'chart.png', clip: bbox });
```

### Controlling SVG Size for Screenshots

To capture an SVG at a specific size:

```javascript
// Approach 1: Set the container size before screenshot
await page.evaluate(() => {
  const container = document.querySelector('.chart-container');
  container.style.width = '1600px';
  container.style.height = '900px';
});
// Wait for reflow
await page.waitForTimeout(100);
await page.locator('.chart-container svg').screenshot({ path: 'chart.png' });

// Approach 2: Directly set SVG dimensions
await page.evaluate(() => {
  const svg = document.querySelector('svg');
  svg.style.width = '1600px';
  svg.style.height = '900px';
});
await page.locator('svg').screenshot({ path: 'chart.png' });
```

### Resolution Control (CSS vs Device Pixels)

```javascript
// "css" mode: 1 screenshot pixel per CSS pixel (smaller files)
await page.screenshot({ path: 'chart.png', scale: 'css' });

// "device" mode: 1 screenshot pixel per device pixel (larger, sharper on HiDPI)
await page.screenshot({ path: 'chart.png', scale: 'device' });
```

---

## 8. Making a Generated SVG Scale Up After Render

When you do not control the SVG source (e.g., mermaid.js or d3.js output), you need to manipulate the rendered SVG element in the DOM.

### What Mermaid.js Outputs

Mermaid generates SVGs with different attributes depending on the `useMaxWidth` config:

**`useMaxWidth: true` (default):**
```html
<svg id="mermaid-1" width="100%" xmlns="..." viewBox="0 0 843 562"
     style="max-width: 843px;">
  <!-- diagram content -->
</svg>
```

**`useMaxWidth: false`:**
```html
<svg id="mermaid-1" width="843" height="562" xmlns="..."
     viewBox="0 0 843 562">
  <!-- diagram content -->
</svg>
```

In both cases, a `viewBox` is present. This is the key to scaling.

### Strategy A: Remove Constraints and Let CSS Scale

The simplest approach when the SVG already has a viewBox:

```javascript
// After mermaid.run() completes
function scaleSvgToContainer(svgElement) {
  // Remove fixed dimensions that prevent scaling
  svgElement.removeAttribute('width');
  svgElement.removeAttribute('height');
  svgElement.style.removeProperty('max-width');
  svgElement.style.removeProperty('max-height');

  // Let CSS take over
  svgElement.style.width = '100%';
  svgElement.style.height = 'auto';

  // Ensure aspect ratio is preserved (already the default, but be explicit)
  if (!svgElement.getAttribute('preserveAspectRatio')) {
    svgElement.setAttribute('preserveAspectRatio', 'xMidYMid meet');
  }
}

// Usage after render
await mermaid.run({ querySelector: '.mermaid' });
document.querySelectorAll('.mermaid svg').forEach(scaleSvgToContainer);
```

### Strategy B: Read getBBox and Set viewBox Dynamically

When the SVG does not have a viewBox (rare for mermaid, common for some d3 output):

```javascript
function fitSvgToContents(svgElement) {
  // getBBox returns the tight bounding box of all SVG content
  const bbox = svgElement.getBBox();

  // Add padding
  const padding = 20;
  const viewBoxX = bbox.x - padding;
  const viewBoxY = bbox.y - padding;
  const viewBoxW = bbox.width + padding * 2;
  const viewBoxH = bbox.height + padding * 2;

  // Set the viewBox to tightly wrap the content
  svgElement.setAttribute('viewBox', `${viewBoxX} ${viewBoxY} ${viewBoxW} ${viewBoxH}`);

  // Remove fixed dimensions so the SVG scales with its container
  svgElement.removeAttribute('width');
  svgElement.removeAttribute('height');

  // Apply responsive CSS
  svgElement.style.width = '100%';
  svgElement.style.height = 'auto';
  svgElement.style.display = 'block';
}
```

**Critical timing note:** `getBBox()` can return incorrect values if the SVG is not yet fully rendered. Use `requestAnimationFrame` or wait for the render cycle to complete:

```javascript
// Correct: wait for render before measuring
requestAnimationFrame(() => {
  requestAnimationFrame(() => {
    // Double rAF ensures layout is complete
    fitSvgToContents(document.querySelector('svg'));
  });
});
```

### Strategy C: Scale to a Specific Target Size

When you need the SVG at exact dimensions (e.g., for screenshot capture):

```javascript
function scaleSvgToSize(svgElement, targetWidth, targetHeight) {
  // Read the existing viewBox or calculate one from getBBox
  let viewBox = svgElement.getAttribute('viewBox');
  if (!viewBox) {
    const bbox = svgElement.getBBox();
    viewBox = `${bbox.x} ${bbox.y} ${bbox.width} ${bbox.height}`;
    svgElement.setAttribute('viewBox', viewBox);
  }

  // Set explicit target dimensions
  svgElement.setAttribute('width', targetWidth);
  svgElement.setAttribute('height', targetHeight);

  // Also set via CSS to override any existing styles
  svgElement.style.width = targetWidth + 'px';
  svgElement.style.height = targetHeight + 'px';
  svgElement.style.maxWidth = 'none';
  svgElement.style.maxHeight = 'none';

  // Choose scaling behavior:
  // 'xMidYMid meet' = fit inside, maintain aspect ratio (may have empty space)
  // 'xMidYMid slice' = fill completely, maintain aspect ratio (may crop)
  // 'none' = stretch to fill exactly (distorts content)
  svgElement.setAttribute('preserveAspectRatio', 'xMidYMid meet');
}

// Example: scale a mermaid diagram to fill an A4-width container
scaleSvgToSize(document.querySelector('svg'), 1600, 900);
```

### Strategy D: Scale Up with Container Resizing

Force the container to a target size and let the SVG follow:

```javascript
function scaleByContainer(containerSelector, targetWidth) {
  const container = document.querySelector(containerSelector);
  const svg = container.querySelector('svg');

  // Set container to target width
  container.style.width = targetWidth + 'px';

  // Ensure SVG fills container
  svg.style.width = '100%';
  svg.style.height = 'auto';
  svg.style.maxWidth = 'none';
  svg.removeAttribute('width');
  svg.removeAttribute('height');

  // viewBox must exist for scaling to work
  if (!svg.getAttribute('viewBox')) {
    const bbox = svg.getBBox();
    svg.setAttribute('viewBox',
      `${bbox.x} ${bbox.y} ${bbox.width} ${bbox.height}`);
  }
}
```

### Complete Mermaid + Playwright Example

Putting it all together for capturing a mermaid diagram at a specific size:

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { margin: 0; padding: 20px; background: white; }
    .diagram-container {
      width: 1400px;  /* Target capture width */
      margin: 0 auto;
    }
    .diagram-container svg {
      width: 100% !important;
      height: auto !important;
      max-width: none !important;
      display: block;
    }
  </style>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
</head>
<body>
  <div class="diagram-container">
    <pre class="mermaid">
      graph TB
        A[Start] --> B[Process]
        B --> C[End]
    </pre>
  </div>
  <script>
    mermaid.initialize({
      startOnLoad: false,
      flowchart: { useMaxWidth: true, htmlLabels: true }
    });

    async function renderAndScale() {
      await mermaid.run({ querySelector: '.mermaid' });

      // Post-render: remove mermaid's max-width constraint
      document.querySelectorAll('.diagram-container svg').forEach(svg => {
        svg.style.maxWidth = 'none';
        svg.style.width = '100%';
        svg.style.height = 'auto';
      });
    }

    renderAndScale();
  </script>
</body>
</html>
```

Playwright capture script:

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 2  // 2x for sharp output
  });
  const page = await context.newPage();

  await page.goto('file:///path/to/diagram.html');

  // Wait for mermaid to finish rendering
  await page.waitForSelector('.diagram-container svg');
  await page.waitForTimeout(500); // Allow post-render JS to complete

  // Screenshot the SVG element directly
  const svg = page.locator('.diagram-container svg');
  await svg.screenshot({ path: 'diagram.png' });

  // Or screenshot with specific clip dimensions
  const bbox = await page.evaluate(() => {
    const el = document.querySelector('.diagram-container svg');
    const rect = el.getBoundingClientRect();
    return { x: rect.x, y: rect.y, width: rect.width, height: rect.height };
  });
  await page.screenshot({ path: 'diagram-clipped.png', clip: bbox });

  await browser.close();
})();
```

---

## Quick Reference: Decision Matrix

| Situation | Solution |
|-----------|----------|
| SVG has viewBox, need it responsive | CSS: `width: 100%; height: auto;` |
| SVG has no viewBox, need it responsive | JS: calculate `getBBox()`, set `viewBox`, then CSS `width: 100%; height: auto;` |
| Need exact pixel dimensions | Set `viewBox` + `width`/`height` attributes + CSS to match |
| Need to stretch/distort to fill | `viewBox` + `preserveAspectRatio="none"` + CSS `width: 100%; height: 100%;` |
| Need to fill and crop (cover) | `viewBox` + `preserveAspectRatio="xMidYMid slice"` |
| Need to fit inside (contain) | `viewBox` + `preserveAspectRatio="xMidYMid meet"` (default) |
| Mermaid output too small | Remove `max-width` style, set CSS `width: 100%` on the SVG |
| Mermaid output for screenshot | Set container to target size, CSS override on SVG, `deviceScaleFactor: 2` in Playwright |
| d3 output without viewBox | `getBBox()` after double `requestAnimationFrame`, then set `viewBox` |

---

## Sources

- [MDN: viewBox attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/viewBox)
- [MDN: preserveAspectRatio](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/preserveAspectRatio)
- [MDN: SVG width attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/width)
- [MDN: SVG Tutorial - Positions](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Positions)
- [CSS-Tricks: How to Scale SVG](https://css-tricks.com/scale-svg/)
- [Sara Soueidan: SVG Coordinate Systems and Transformations](https://www.sarasoueidan.com/blog/svg-coordinate-systems/)
- [TypeOfNaN: How to Perfectly Fit an SVG to its Contents](https://typeofnan.dev/how-to-perfectly-fit-an-svg-to-its-contents-using-javascript/)
- [Playwright: Screenshots documentation](https://playwright.dev/docs/screenshots)
- [Playwright: Locator API](https://playwright.dev/docs/api/class-locator)
- [Mermaid.js: SVG width/height inconsistencies (Issue #1490)](https://github.com/mermaid-js/mermaid/issues/1490)
- [Mermaid.js: useMaxWidth flag behavior (Issue #5038)](https://github.com/mermaid-js/mermaid/issues/5038)
- [Mermaid.js: getBBox race condition (Issue #6146)](https://github.com/mermaid-js/mermaid/issues/6146)
- [W3C SVG WG: Intrinsic Sizing](https://www.w3.org/Graphics/SVG/WG/wiki/Intrinsic_Sizing)
- [W3C SVG2 Draft: Styling](https://w3c.github.io/svgwg/svg2-draft/styling.html)
