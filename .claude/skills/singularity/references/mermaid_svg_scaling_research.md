# Mermaid.js SVG Output Sizing and Scaling Research

**Date:** 2026-04-14
**Context:** Understanding how mermaid.js generates SVG output and how to control its sizing, particularly for making diagrams fill their containers or printed pages. Focused on mermaid v11 behavior.
**Related:** `mermaid_flowchart_learnings_2026-04-14.md` (same directory)

---

## 1. SVG Attributes Mermaid Sets on Generated Output

Mermaid's rendering pipeline uses an internal function called `configureSvgSize` (in `packages/mermaid/src/utils.ts`) that sets attributes on the root `<svg>` element after the diagram is rendered. The attributes set depend on the `useMaxWidth` configuration value.

### When `useMaxWidth: true` (the default)

```html
<svg xmlns="http://www.w3.org/2000/svg"
     id="mermaid-{unique-id}"
     width="100%"
     height="100%"
     style="max-width: {computed-width}px;"
     viewBox="{x} {y} {width} {height}"
     role="graphics-document document"
     aria-roledescription="flowchart">
```

Key observations:
- `width` is set to `"100%"` (percentage, not pixels)
- `height` is set to `"100%"` (percentage, not pixels)
- An inline `style` attribute is added with `max-width` set to the computed pixel width of the diagram content
- `viewBox` is set to the computed bounding box of the rendered diagram content (with padding)
- The `viewBox` origin (x, y) may be negative values due to padding calculations

### When `useMaxWidth: false`

```html
<svg xmlns="http://www.w3.org/2000/svg"
     id="mermaid-{unique-id}"
     width="{computed-width}"
     height="{computed-height}"
     viewBox="{x} {y} {width} {height}"
     role="graphics-document document"
     aria-roledescription="flowchart">
```

Key observations:
- `width` is set to an absolute pixel value (no units, interpreted as pixels by SVG spec)
- `height` is set to an absolute pixel value
- No `max-width` inline style is applied
- `viewBox` is set identically to the `true` case

### The `viewBox` Calculation

Mermaid calculates the viewBox through `calculateDimensionsWithPadding`, which calls `getBBox()` on the rendered SVG content to determine its actual dimensions. The viewBox is then constructed as:

```
viewBox = "{x - padding} {y - padding} {width + padding} {height + padding}"
```

**Known issue (GitHub #6146):** There is a race condition where `getBBox()` can return incorrect values if the SVG is not fully rendered when the calculation runs. This can produce incorrect viewBox heights (e.g., `2036` instead of the actual height). The recommended fix is wrapping the calculation in `requestAnimationFrame`:

```javascript
requestAnimationFrame(() => {
  const { width, height, x, y } = calculateDimensionsWithPadding(svg, padding);
  configureSvgSize(svg, height, width, useMaxWidth);
  const viewBox = createViewBox(x, y, width, height, padding);
  svg.attr('viewBox', viewBox);
});
```

### Other Attributes

Mermaid also sets:
- `role="graphics-document document"` (accessibility)
- `aria-roledescription` set to the diagram type (e.g., "flowchart", "class", "sequence")
- An embedded `<style>` element inside the SVG with scoped CSS rules using the unique SVG ID as a selector prefix
- `class` attribute set to the diagram type (e.g., "flowchart", "classDiagram")

### Inconsistencies Between Diagram Types

As documented in GitHub issue #1490, different diagram types historically set SVG attributes inconsistently. The proposal (now largely implemented) standardized on this pseudo-code:

```javascript
svg.attr('height', height);
if (conf.useMaxWidth) {
  svg.attr('width', '100%');
  svg.attr('style', `max-width: ${width}px;`);
} else {
  svg.attr('width', width);
}
```

However, some diagram types (Gantt, pie charts, ER diagrams) may still deviate from this pattern. Class diagrams in particular can produce extreme viewBox values (e.g., `viewBox="-820 -820 3116 2828"` with `style="max-width: 3116px;"`) as documented in GitHub issue #6471.

---

## 2. How `useMaxWidth` Actually Works

### The Mechanism

`useMaxWidth` is a per-diagram-type configuration option (available under `flowchart`, `sequence`, `class`, etc.) that defaults to `true`. It controls whether the SVG element uses responsive (percentage-based) or fixed (pixel-based) dimensions.

When `useMaxWidth: true`:
1. `width` attribute is set to `"100%"` -- the SVG will try to fill its container's width
2. `height` attribute is set to `"100%"` -- the SVG will try to fill its container's height
3. `style="max-width: {N}px;"` is added as an inline style -- this **caps** the SVG at its natural rendered width
4. The `viewBox` provides the coordinate system, so the browser can scale the diagram content proportionally

The net effect: **the diagram will shrink to fit a narrow container (responsive) but will never grow beyond its natural width.** The `max-width` inline style is the constraint that prevents upscaling.

When `useMaxWidth: false`:
1. `width` attribute is set to the computed pixel width (e.g., `"516"`)
2. `height` attribute is set to the computed pixel height (e.g., `"301"`)
3. No `max-width` style is applied
4. The SVG renders at exactly its computed size, regardless of container dimensions

### What It Does NOT Do

- It does **not** control individual node sizing within the diagram
- It does **not** make nodes expand to fill available width
- It does **not** affect text wrapping or content layout within nodes
- It does **not** provide a "scale up to fill container" mode

### The "Three Modes" Problem

As described by mermaid maintainer `knsv` in GitHub issue #5038, there are really three use cases that users need:

1. **No resize** -- diagram renders at its natural size regardless of container
2. **Fill container** -- diagram scales to use all available space (up AND down)
3. **Shrink to fit** -- diagram stays at natural size unless container is smaller (this is what `useMaxWidth: true` does)

Mermaid currently only supports modes 1 and 3. Mode 2 (fill container) is not natively supported. The maintainers proposed a future `scaling` config option with values `'none'`, `'fit-container'`, and `'shrink-to-fit-container'`, but this has not been implemented as of v11.

---

## 3. Making Mermaid SVGs Scale to Fill Their Container

Since mermaid does not natively support "scale up to fill container," you need post-render manipulation. Here are the techniques, ordered from simplest to most complete.

### Technique A: CSS Override of max-width (Simplest)

Override the inline `max-width` style that mermaid applies:

```css
.mermaid svg {
  max-width: none !important;   /* Remove the cap */
  width: 100% !important;       /* Fill container width */
  height: auto !important;      /* Maintain aspect ratio */
}
```

**How it works:** The `viewBox` attribute is still set, so the browser uses it to determine the aspect ratio. With `width: 100%` and `height: auto`, the SVG scales to fill its container's width while maintaining proportions.

**Limitation:** The `height: auto` depends on the browser correctly computing height from the viewBox aspect ratio. This works in modern browsers but may produce unexpected results if the viewBox has padding issues.

### Technique B: Post-Render JavaScript (More Control)

Remove the inline `max-width` style after mermaid renders:

```javascript
mermaid.initialize({ startOnLoad: false, /* ... */ });

async function renderAndScale() {
  await mermaid.run({ querySelector: '.mermaid' });
  
  document.querySelectorAll('.mermaid svg').forEach(svg => {
    // Remove the max-width constraint
    svg.style.maxWidth = 'none';
    
    // Set width to fill container
    svg.setAttribute('width', '100%');
    
    // Option 1: Let height auto-compute from viewBox
    svg.removeAttribute('height');
    
    // Option 2: Set explicit height based on container
    // svg.setAttribute('height', '100%');
  });
}

renderAndScale();
```

**When to use:** When you need to apply different scaling to different diagrams on the same page, or when you also need to modify other SVG attributes post-render (e.g., node styling).

### Technique C: ViewBox Manipulation for Precise Scaling

For maximum control, recalculate and override the viewBox:

```javascript
async function renderAndFit() {
  await mermaid.run({ querySelector: '.mermaid' });
  
  document.querySelectorAll('.mermaid svg').forEach(svg => {
    // Get the actual content bounds
    const bbox = svg.getBBox();
    const padding = 20;
    
    // Set a tight viewBox around the actual content
    svg.setAttribute('viewBox', 
      `${bbox.x - padding} ${bbox.y - padding} ${bbox.width + padding * 2} ${bbox.height + padding * 2}`
    );
    
    // Remove fixed dimensions, let CSS control size
    svg.style.maxWidth = 'none';
    svg.setAttribute('width', '100%');
    svg.removeAttribute('height');
    
    // Ensure proper scaling behavior
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
  });
}

renderAndFit();
```

**When to use:** When the default viewBox includes excessive padding or whitespace, or when the diagram content does not fill the viewBox properly.

### Technique D: Container-Based Responsive Scaling

Wrap the mermaid element in a sized container and let CSS handle scaling:

```html
<div class="diagram-container" style="width: 100%; max-height: 80vh;">
  <pre class="mermaid">
    graph TB
      A --> B --> C
  </pre>
</div>
```

```css
.diagram-container {
  width: 100%;
  overflow: visible;
}

.diagram-container svg {
  width: 100% !important;
  height: auto !important;
  max-width: none !important;
  display: block;
}
```

---

## 4. `useMaxWidth: true` vs `useMaxWidth: false` -- Detailed Comparison

| Aspect | `useMaxWidth: true` (default) | `useMaxWidth: false` |
|--------|-------------------------------|----------------------|
| SVG `width` attribute | `"100%"` | `"{computed}px"` (absolute) |
| SVG `height` attribute | `"100%"` | `"{computed}px"` (absolute) |
| Inline `style` | `max-width: {computed}px;` | None |
| `viewBox` | Set to computed bounds | Set to computed bounds (identical) |
| Shrinks in narrow container | Yes (responsive) | No (overflows or clips) |
| Grows in wide container | No (capped by max-width) | No (fixed size) |
| Whitespace in tall containers | Yes -- the height=100% causes large gaps above/below when width shrinks | No -- fixed dimensions, no gaps |
| Best for | Web pages with variable width | Fixed-size outputs (PDF, print) |
| Container overflow behavior | Diagram shrinks; container may have vertical whitespace | Diagram may overflow horizontally |

### The Height Gap Problem

When `useMaxWidth: true`, the SVG has `height="100%"`. As the browser window narrows, the `width` shrinks (bounded by `max-width`) and the viewBox scales down the content. But the `height="100%"` still tries to fill the parent container's height, creating large whitespace gaps above and below the diagram.

This was identified in GitHub issue #2160 and a fix was proposed in PR #2312 (making height auto-compute when useMaxWidth is true). That PR was merged but later reverted. The issue remains in current versions.

**Workaround for the height gap:**

```css
.mermaid svg {
  height: auto !important;  /* Override height="100%" */
}
```

Or post-render:

```javascript
svg.removeAttribute('height');
/* or */
svg.setAttribute('height', 'auto');
```

---

## 5. Known Issues and Workarounds

### Issue: Diagram will not scale UP to fill available space

**Root cause:** The inline `style="max-width: {N}px;"` caps the SVG at its natural width.

**Workaround:**
```css
.mermaid svg { max-width: none !important; }
```

Or post-render:
```javascript
document.querySelector('.mermaid svg').style.maxWidth = 'none';
```

### Issue: Large whitespace gaps above/below diagram

**Root cause:** `height="100%"` on the SVG combined with `useMaxWidth: true` means the SVG element fills the container height even when the content is scaled down.

**Workaround:**
```css
.mermaid svg { height: auto !important; }
```

### Issue: viewBox has incorrect dimensions (too tall, too wide)

**Root cause:** Race condition in `calculateDimensionsWithPadding` -- `getBBox()` returns incorrect values before SVG is fully rendered (GitHub #6146).

**Workaround:**
```javascript
// Delay viewBox recalculation
await mermaid.run({ querySelector: '.mermaid' });
requestAnimationFrame(() => {
  const svg = document.querySelector('.mermaid svg');
  const bbox = svg.getBBox();
  const pad = 20;
  svg.setAttribute('viewBox', 
    `${bbox.x - pad} ${bbox.y - pad} ${bbox.width + pad * 2} ${bbox.height + pad * 2}`
  );
});
```

### Issue: Class diagrams render with extreme viewBox values

**Root cause:** Some diagram types (class diagrams in particular) produce viewBox values like `-820 -820 3116 2828` with `max-width: 3116px;`, making content appear tiny (GitHub #6471).

**Workaround:** Use `getBBox()` post-render to recalculate a tight viewBox, as shown in Technique C above.

### Issue: Content clipped inside nodes (foreignObject overflow)

**Root cause:** Mermaid's foreignObject elements default to `overflow: hidden`, and their dimensions are calculated before any post-render styling.

**Workaround (from our existing learnings):**
```css
.mermaid .node foreignObject { overflow: visible !important; }
.mermaid .node foreignObject div { overflow: visible !important; }
```

### Issue: SVG content clipped by HTML container

**Root cause:** The HTML container (`.diagram-box`, `<pre>`, etc.) may have overflow hidden.

**Workaround:**
```css
.diagram-box { overflow: visible; }
.diagram-box svg { overflow: visible !important; }
```

---

## 6. How Other Projects Solve Mermaid SVG Scaling

### GitLab (Issue #199423, MR !25016)

GitLab needed mermaid diagrams to render at full container width in their markdown rendering. Their solution:

1. Created a CSS class `.gfm-mermaid` applied to the container
2. Set `max-width: 100% !important` on `.gfm-mermaid svg` to override mermaid's inline style
3. Used `useMaxWidth: true` in mermaid config to enable responsive behavior

```css
.gfm-mermaid svg {
  max-width: 100% !important;
  width: 100% !important;
}
```

### Obsidian -- mermaid-maestro Plugin

The mermaid-maestro plugin for Obsidian uses **SVG viewBox manipulation** to auto-fit diagrams:

1. After mermaid renders, the plugin reads the SVG's `getBBox()` 
2. Recalculates a tight viewBox around the actual content
3. Sets `width: 100%` and removes the max-width constraint
4. The diagram scales to fit the note's width while remaining crisp at any zoom level

### Obsidian -- mermaid-fit-center Plugin

Specifically for PDF export, this plugin:

1. Sets `max-width: 100%` for all diagrams during print/export
2. Shrinks large diagrams to fit page width (prevents right-side cutoff)
3. Leaves small diagrams at their original size (prevents forced stretching / pixelation)
4. Centers all diagrams on the page

### Joplin (Issue #6711)

Joplin had Gantt diagrams fixed to 640px width. Their solution was to use the parent container to control scaling:

```css
.mermaid svg {
  max-width: 100%;
  height: auto;
}
```

### ADW (Architecture Decision Workbench)

The ADW documentation system found that a previous mermaid version was inserting large blank spaces by setting `height="100%"`. Their fix was to remove the height attribute from the SVG after rendering, allowing the browser to compute height from the viewBox aspect ratio.

### reveal.js Presentations

For mermaid in slide decks, the common approach is:

1. Use the `r-stretch` class on the container to fill remaining slide space
2. Set `useMaxWidth: false` to get fixed dimensions
3. Apply CSS transforms to scale the fixed-size SVG to fit the slide

```css
.reveal .mermaid svg {
  max-width: 100% !important;
  max-height: 70vh;
  width: auto;
  height: auto;
}
```

### Quarto Documents (Issue #3973)

Quarto uses `fig-width` to control mermaid diagram sizing. Their approach:

1. Render mermaid with `useMaxWidth: false` for predictable sizing
2. Apply CSS transforms post-render to scale the SVG to the desired figure width

---

## 7. Recommended Approach for Our Use Case (BayOne Deliverables)

For standalone HTML deliverables that include mermaid diagrams and need to print on 8.5x11 portrait pages, the recommended approach combines several techniques:

### Configuration

```javascript
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  flowchart: {
    curve: 'basis',
    nodeSpacing: 30,
    rankSpacing: 70,
    htmlLabels: true,
    useMaxWidth: false,   // Use false for print -- we control sizing ourselves
    padding: 40,
    wrappingWidth: 600
  }
});
```

Using `useMaxWidth: false` gives us a fixed-size SVG that we can then scale precisely with CSS.

### CSS for Screen and Print

```css
/* Container */
.diagram-container {
  width: 100%;
  overflow: visible;
  text-align: center;
}

/* Screen: scale to container width */
.diagram-container svg {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

/* Print: scale to page width */
@media print {
  .diagram-container svg {
    max-width: 100% !important;
    width: 100% !important;
    height: auto !important;
    page-break-inside: avoid;
  }
}
```

### Post-Render JavaScript

```javascript
async function renderDiagram() {
  await mermaid.run({ querySelector: '.mermaid' });
  
  const svg = document.querySelector('.mermaid svg');
  if (!svg) return;
  
  // Recalculate viewBox from actual content bounds
  requestAnimationFrame(() => {
    const bbox = svg.getBBox();
    const pad = 20;
    svg.setAttribute('viewBox',
      `${bbox.x - pad} ${bbox.y - pad} ${bbox.width + pad * 2} ${bbox.height + pad * 2}`
    );
    
    // Ensure the SVG scales to fill container
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    
    // Remove any fixed dimensions so CSS controls sizing
    svg.style.maxWidth = 'none';
    svg.setAttribute('width', '100%');
    svg.removeAttribute('height');
  });
  
  // Apply node styling (title bars, padding fixes)
  svg.querySelectorAll('.node').forEach(n => {
    const fo = n.querySelector('foreignObject'), rect = n.querySelector('rect');
    if (!fo || !rect) return;
    let sc = rect.getAttribute('stroke') || '#94a3b8';
    fo.querySelectorAll('b').forEach(b => {
      b.style.display = 'block';
      b.style.background = 'rgba(255,255,255,0.85)';
      b.style.border = '1px solid ' + sc;
      b.style.borderRadius = '4px';
      b.style.padding = '4px 10px';
      b.style.marginBottom = '6px';
      b.style.fontSize = '13px';
      b.style.letterSpacing = '0.3px';
    });
    const h = parseFloat(rect.getAttribute('height'));
    rect.setAttribute('height', h + 12);
    fo.setAttribute('height', h + 12);
  });
}

renderDiagram();
```

### Alternative: `useMaxWidth: true` with CSS Override

If you prefer mermaid's responsive behavior with an override to allow upscaling:

```javascript
flowchart: { useMaxWidth: true, /* ... */ }
```

```css
.mermaid svg {
  max-width: none !important;  /* Override mermaid's inline max-width cap */
  width: 100% !important;
  height: auto !important;
}
```

This is simpler but gives less control over the exact sizing.

---

## 8. Quick Reference: SVG Scaling Fundamentals

For context, here is how SVG scaling works at the browser level (independent of mermaid):

### The Three Controls

1. **`viewBox`** -- defines the coordinate system of the SVG content (what the "camera" sees)
2. **`width` / `height`** -- defines the display size of the SVG element in the page
3. **`preserveAspectRatio`** -- controls how the viewBox content maps to the display size

### Making Any SVG Responsive

```html
<!-- Remove width/height, keep viewBox -->
<svg viewBox="0 0 800 600">
  <!-- content -->
</svg>
```

```css
svg {
  width: 100%;
  height: auto;
  display: block;
}
```

The browser computes height from the viewBox aspect ratio (600/800 = 0.75, so height = 75% of width).

### `preserveAspectRatio` Values

| Value | CSS Equivalent | Effect |
|-------|---------------|--------|
| `xMidYMid meet` (default) | `object-fit: contain` | Scale to fit, centered, may have empty space |
| `xMidYMid slice` | `object-fit: cover` | Scale to cover, centered, may crop |
| `none` | `object-fit: fill` | Stretch to fill, ignores aspect ratio |

### For Filling a Container Completely (Stretch)

```html
<svg viewBox="0 0 800 600" preserveAspectRatio="none" width="100%" height="100%">
```

This stretches the diagram to fill the container, distorting the aspect ratio. Rarely desirable for diagrams.

### For Filling Width, Auto Height (Most Common)

```html
<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid meet" width="100%">
```

```css
svg { width: 100%; height: auto; display: block; }
```

This scales the diagram to fill the container width while maintaining aspect ratio. The height adjusts automatically.

---

## Sources

### GitHub Issues
- [#5038 -- useMaxWidth flag doesn't really use the max width](https://github.com/mermaid-js/mermaid/issues/5038)
- [#1490 -- SVG width and height attributes inconsistencies between diagrams](https://github.com/mermaid-js/mermaid/issues/1490)
- [#2160 -- Svg fixed height causes gaps when fitting smaller window](https://github.com/mermaid-js/mermaid/issues/2160)
- [#3659 -- SVG height attribute absent with 9.1.7](https://github.com/mermaid-js/mermaid/issues/3659)
- [#6146 -- Race Condition in calculateDimensionsWithPadding Affecting ViewBox Calculation](https://github.com/mermaid-js/mermaid/issues/6146)
- [#6471 -- mermaid.render renders classDiagrams with extreme viewBox/max-width](https://github.com/mermaid-js/mermaid/issues/6471)
- [#838 -- Configure flowchart to auto-resize so that nodes are always the same size](https://github.com/mermaid-js/mermaid/issues/838)

### Pull Requests
- [#2312 -- configureSvgSize should make height 100% when useMaxWidth is true](https://github.com/mermaid-js/mermaid/pull/2312)

### Mermaid Documentation
- [Base Diagram Config Schema (useMaxWidth)](https://mermaid.js.org/config/schema-docs/config-defs-base-diagram-config.html)
- [Flowchart Diagram Config Schema](https://mermaid.js.org/config/schema-docs/config-defs-flowchart-diagram-config.html)
- [Mermaid Config Schema](https://mermaid.js.org/config/schema-docs/config.html)
- [Usage / Configuration](https://mermaid.js.org/config/usage.html)

### Source Code References
- [packages/mermaid/src/utils.ts (configureSvgSize, setupGraphViewbox)](https://github.com/mermaid-js/mermaid/blob/master/packages/mermaid/src/utils.ts)
- [packages/mermaid/src/rendering-util/render.ts](https://github.com/mermaid-js/mermaid/blob/master/packages/mermaid/src/rendering-util/render.ts)
- [packages/mermaid/src/defaultConfig.ts](https://github.com/mermaid-js/mermaid/blob/master/packages/mermaid/src/defaultConfig.ts)

### External Projects
- [GitLab -- Change mermaid rendering to width 100%](https://gitlab.com/gitlab-org/gitlab/-/issues/199423)
- [GitLab -- Fix Mermaid diagram scaling MR](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/25016)
- [Obsidian mermaid-maestro plugin](https://github.com/thetrustedadvisor/mermaid-maestro)
- [Obsidian mermaid-fit-center plugin](https://github.com/iE-zhi/obsidian-mermaid-fit-center)
- [ADW MermaidJS notes](https://cese.gitlab.io/adw/docs/devnotes/mermaid.html)

### SVG Scaling References
- [CSS-Tricks: How to Scale SVG](https://css-tricks.com/scale-svg/)
- [MDN: preserveAspectRatio](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/preserveAspectRatio)
- [MDN: viewBox](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
