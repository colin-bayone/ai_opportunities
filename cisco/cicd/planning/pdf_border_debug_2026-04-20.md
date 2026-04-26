# PDF Border Debug Log

**Started:** 2026-04-20
**Context:** The Singularity `html_to_pdf.py` script with `--landscape` produces PDFs with thin asymmetric white borders around the colored slide content. The slide should fill the page edge to edge.

---

## Problem

When converting BayOne 16:10 slides to PDF via `html_to_pdf.py --landscape`, the colored slide does not fill the page. White margins of varying widths appear around the slide.

### Observed Measurements (Colin, 2026-04-20)

**Single slide rendered alone (`html_to_pdf.py 00_title.html out.pdf --landscape`):**
- Left border: ~2 px
- Right border: ~8 px
- Bottom border: ~5 px
- Top border: not yet measured

**Same slide rendered as part of merged deck (`html_to_pdf.py slides_dir/ deck.pdf --merge --landscape`):**
- Left border: ~2 px
- Right border: not visible (or much smaller)
- Bottom border: not visible (or much smaller)
- Top border: not visible

The asymmetry between sides AND the difference between single-slide and merged modes are both unexplained.

### Math That Should Apply

- `@page` size injected: 11.5in × 7.1875in = approximately 1104 × 690 px at 96 dpi
- Slide CSS: `max-width: 1100px; aspect-ratio: 16 / 10` → 1100 × 687.5 px
- Body wraps slide with `display: flex; align-items: center; justify-content: center;`
- With body padding zeroed, free horizontal space = 1104 − 1100 = 4 px → expected 2 px each side
- With body min-height zeroed, free vertical space = 690 − 687.5 = 2.5 px → expected ~1.25 px each side

**Observed left+right (2 + 8 = 10 px) exceeds the predicted 4 px total.** Something is adding margin beyond pure flex centering.

---

## Hypotheses (Pre-Diagnostic)

1. **Chrome `--print-to-pdf` is enforcing a default margin despite `@page { margin: 0 }`.** Some Chrome versions partially ignore @page margin and apply small browser-default page margins. Could explain the extra width.
2. **Chrome subpixel rounding asymmetry.** Print rendering can put leftover free-space pixels on whichever side rounding favors, varying by content and page size. Plausible explanation for left/right asymmetry within a small range.
3. **The slide's own `border: 1px solid rgba(0,0,0,0.08)` + `border-radius: 12px` + `box-shadow`.** These create soft edges that may render as white halos on a colored slide. Wouldn't explain the asymmetric WIDTH but could contribute to visibility.
4. **pypdf merge step rewrites page boxes.** When `--merge` is used, the merged PDF might have different effective dimensions than the per-slide PDF, explaining why merged-mode borders look different from single-slide mode.

---

## Tests Planned

### Test 1: Red Background Diagnostic (Run 2026-04-20)

**Goal:** Make the gap visible at exact pixel boundaries by changing the body print background from white to bright red. We will be able to see precisely where the red shows around the slide and measure each side.

**Method:** Temporarily change `background: #ffffff` to `background: #ff0000` in the script's `LANDSCAPE_PAGE_CSS` block. Render slide 00 only.

**Expected outcomes:**
- If borders are caused by flex centering / Chrome margin: red will frame the slide on whichever sides the gap exists.
- If borders are caused by the slide's border-radius / box-shadow halo: red will only show at the corners.

**Output path:** `cisco/cicd/presentations/srinivas_status_2026-04-17/00_title_debug_red.pdf`

**Result:** _to be filled in after Colin reviews_

---

## Test Results

### Test 1 Result (2026-04-20)

Red shows on three sides (left, right, bottom) and is flush at the top. Within the same PDF, when fully zoomed in the three bands appear roughly equal width; at lower zoom levels they appear asymmetric due to PDF viewer subpixel rendering. The earlier 2/5/8 px measurements were zoom-distorted readings of those three real gaps.

**Diagnosis:**

- Top is flush because the body has `display: flex; align-items: center` but `min-height: 0` (overridden in print). With min-height collapsed, the body shrinks to content height and the slide sits at the top of the body, which sits at the top of the page.
- Bottom shows red because page height (~690 px) is larger than slide height. With slide max-width 1100 px and aspect-ratio 16:10, slide height is 687.5 px. Difference is 2.5 px, all visible at the bottom.
- Left and right show red because the slide caps at `max-width: 1100px` but the page is approximately 1104 px wide. Flex centering splits the 4 px gap as 2 px on each side.

Hypothesis 1 (Chrome ignoring @page margin) and hypothesis 2 (subpixel asymmetry) and hypothesis 3 (border-radius halo) and hypothesis 4 (pypdf merge artifacts) are all not the actual cause. The real cause is the slide's own `max-width: 1100px` constraint relative to the slightly larger print page.

**Acceptance:** Colin is fine with the slide's `border-radius: 12px` exposing the page background at the four corners. Straight-edge bands on left, right, and bottom must go.

---

## Fix Plan (Run 2026-04-20)

Add a single rule to `LANDSCAPE_PAGE_CSS`: in print mode, force `.slide` to fill the page width.

```css
.slide { width: 100% !important; max-width: none !important; }
```

The slide's `aspect-ratio: 16 / 10` then makes the height fill the page exactly (11.5in / 1.6 = 7.1875in, which is the @page height). No additional rule needed for vertical sizing. Border-radius stays untouched.

Background reverts from `#ff0000` (debug) to `#ffffff` (production) in the same edit.

**Output path:** `cisco/cicd/presentations/srinivas_status_2026-04-17/00_title_debug_v2.pdf`

**Result:** _to be filled in after Colin reviews_

---

## Decisions and Next Tests

### Resolution (2026-04-20)

The fix shipped in the Singularity script's `LANDSCAPE_PAGE_CSS`:

```css
@page { size: 11.5in 7.1875in; margin: 0; }
@media print {
  body { padding: 0 !important; min-height: 0 !important; background: transparent !important; }
  .slide { width: 100% !important; max-width: none !important; }
  .slide-nav { display: none !important; }
}
```

What changed and why:

- `.slide { width: 100% !important; max-width: none !important; }` removes the screen-time 1100 px cap so the slide grows to the full page width (1104 px). This eliminates the left and right gaps.
- `body { background: transparent }` lets the PDF page color (white in every common viewer) show through naturally, instead of the CSS forcing a specific color. There is no truly "clear" PDF page; PDFs always have a default page color.
- The `aspect-ratio: 16/10` on the slide naturally produces 690 px height when given 1104 px width, which matches the page height. No explicit height override needed.
- A small thin band may remain at the bottom in some viewers due to subpixel rounding between slide aspect-ratio computation and Chrome's print engine. Colin accepted the current state on 2026-04-20.

Acceptable artifacts:
- The slide's `border-radius: 12px` exposes a tiny bit of page background at the four corners. This is intentional and accepted.

### Test 2 Result (2026-04-20)

After applying the fix and rendering with red background to verify: left and right gaps fully resolved. A small thin band remained at the bottom, traced to subpixel rounding between aspect-ratio and Chrome's print page math. Adding `height: 100vh; aspect-ratio: auto` to force vertical fill did not visibly change the result. Reverted to width-only override and switched background to transparent. Colin accepted.

Final production state of `LANDSCAPE_PAGE_CSS` is captured above.
