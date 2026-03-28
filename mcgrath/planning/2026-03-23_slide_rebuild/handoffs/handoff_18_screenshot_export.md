# Handoff: Strip + Screenshot Export Pipeline

## Purpose

Build a pipeline that takes all completed HTML slides, strips the presentation chrome (borders, backgrounds, footers, headers), and produces high-resolution PNGs ready to drop into PowerPoint. Colin will assemble the final deck manually in PowerPoint, adding consistent headers/footers/slide numbers across all slides (both HTML-sourced and native PPTX slides).

**This is a tooling/scripting task, not a design task.**

## What to Build

### Step 1: Copy All HTML Slides
- Source: `claude/2026-03-23_mcgrath_slides/slides_output/`
- Destination: `claude/2026-03-23_mcgrath_slides/slides_export/`
- Copy only approved/final HTML files (skip prototypes, rejected versions, utility scripts)

### Step 2: Strip Presentation Chrome from Each Copy

Remove these elements from every copied HTML file:

**Body/Container:**
- Remove background gradient on `body` (make it white or transparent)
- Remove the `.slide` container's `border-radius`, `box-shadow`, `max-width` constraint
- Make the slide content fill the full viewport (no centered floating card look)

**Header:**
- Remove the `.slide-header` entirely (BayOne logo + context label). Colin will add headers in PowerPoint for consistency across HTML and PPTX slides.

**Footer:**
- Remove the `.slide-footer` entirely (gradient bar + slide number). Colin will add slide numbers in PowerPoint.

**What to KEEP:**
- All content within `.slide-content` -- this is the valuable part
- All CSS styling for the content (cards, grids, gradients, icons, typography)
- Font imports (Inter from Google Fonts CDN)
- Icon imports (Font Awesome CDN)
- Any internal gradients, accent bars, card styling within the content area

### Step 3: Playwright Screenshot Script

Write a simple Python script (`claude/2026-03-23_mcgrath_slides/slides_export/screenshot_all.py`) that:

1. Finds all `.html` files in `slides_export/`
2. Opens each in a Playwright Chromium browser
3. Sets viewport to **3840x2400** (16:10 aspect ratio at 4K -- this gives excellent print quality at 8.5x11)
4. Waits for fonts/icons to load (wait for network idle)
5. Takes a full-page screenshot as PNG
6. Saves to `slides_export/pngs/slide_name.png`
7. Prints progress as it goes

**Use `scratchpad.py` patterns -- simple, straightforward Python. No heredocs, no python -c.**

### Step 4: Test on 2-3 Slides First

Before running the full batch:
1. Pick 2-3 diverse slides (e.g., slide_01 title, slide_05 scope cards, slide_06b AI strategy)
2. Run the strip + screenshot on just those
3. Show Colin the results
4. Adjust if needed (viewport size, font loading wait, content padding)

### Step 5: Run Full Batch

Once Colin approves the test results, run on all slides.

## Important Notes

### Viewport Resolution
Colin wants HIGH resolution. Start at **3840x2400** (4K, 16:10). This produces PNGs large enough for print quality. PowerPoint can scale them down without losing clarity. If files are too large, Colin can decide to reduce.

### Slides That Stay in PowerPoint (Don't Screenshot)
- **Slide 3 (Client Logos):** Using Ariat PPTX directly -- skip this one
- Any other slides Colin decides to keep as native PPTX

### Content Padding
After removing the header and footer, the content area may need top/bottom padding adjustments so it doesn't feel cramped against the edges. Check this in the test run.

### Font Loading
Inter font loads from Google Fonts CDN. Font Awesome loads from CDN. The Playwright script MUST wait for these to load before screenshotting, otherwise you'll get fallback fonts. Use `page.wait_for_load_state('networkidle')` and optionally add a small delay.

## Output
- `slides_export/` -- Stripped HTML files
- `slides_export/pngs/` -- High-res PNG screenshots
- `slides_export/screenshot_all.py` -- The Playwright script

## Rules
- Use simple Python scripts. No heredocs or `python -c`.
- Test on 2-3 slides first, show Colin, then proceed.
- Do NOT modify the original files in `slides_output/` -- work on copies in `slides_export/`.
- Write a results handoff at `handoffs/handoff_18_results.md` when done.
