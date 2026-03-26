# Slide Build Feedback: Session 1 (Slides 1 and 3)

Builder: Claude session building slides 01 (title) and 03 (client logos).
Date: 2026-03-23
Reviewer: Colin Moore

---

## Slide 1: Title + About BayOne -- APPROVED

Colin said "slide 1 is fine."

### What worked
- **Split-screen layout** mirroring the Ariat 01 pattern (left text, right visual panel) landed well
- **Stats bar across the bottom** with 100+ customers, 1,000+ projects, 13 years, Global -- clean horizontal treatment
- **BayOne logo + #TheFutureWorksHere badge** in the brand row at the top of the left panel
- **McGrath logo/badge** prominently placed under the title
- **Elevator pitch** used verbatim from Ariat source
- **Purple gradient right panel** with frosted-glass icon grid was an acceptable substitute for the team photo (since we don't have image assets)
- **No standard slide-header** -- title slide got its own hero treatment, which felt appropriate

### Patterns to replicate
- Split-screen with bold purple gradient panel works for hero/intro slides
- Stats bars with gradient text numbers read well
- Putting the brand row inside the content area (instead of a standard header) gives title slides a distinct feel
- The #TheFutureWorksHere pill badge with gradient background is a nice reusable element

---

## Slide 3: Client Logos -- REJECTED ("atrocious")

Colin called this "atrocious." Screenshot comparison against the Ariat source reveals why.

### What went wrong

**1. Text-in-boxes looks like a spreadsheet, not a logo slide.**
The slide uses plain text company names in bordered white rectangles arranged in an 8-column grid. The result looks like an HTML table or a wireframe mockup, not a polished client showcase. The Ariat source has actual brand logos with their distinctive typography, colors, and marks -- Google in its multicolor font, Macy's red star, Cisco's bridge lines, GE's blue circle, Netflix in red, etc. Replacing logos with uniform gray text in identical white boxes strips away all visual richness and brand recognition. The slide communicates nothing -- you have to read each cell individually instead of recognizing logos at a glance.

**2. The grid is too rigid and clinical.**
8 columns of identically-sized boxes with thin borders creates a sterile, spreadsheet-like appearance. The Ariat version spaces logos organically -- they vary in size and visual weight, with natural breathing room. The rigid grid makes it look like a database output.

**3. The "tier" styling is invisible.**
The tier-1 vs tier-2 font weight distinction (700 vs 600, 11px vs 10px) is imperceptible at this scale. It accomplishes nothing.

**4. Three empty ghost cells in the last row.**
The last row has 5 logos and 3 transparent empty cells. This creates an awkward incomplete row that draws attention to itself.

**5. The overall impression is "placeholder wireframe."**
When you compare the screenshot to the Ariat source, our version looks like a low-fidelity mockup that a designer would use to block out spacing before adding actual logos. The Ariat version looks like a finished, professional slide.

### Root cause
The handoff doc warned: "The logos themselves will be represented as text names in styled boxes/cards (since we don't have actual logo image files). Make this look intentional and clean, not like a workaround." The builder's approach (uniform white rectangles with small text) is exactly what "a workaround" looks like. The instruction was to make it NOT look like one.

### What the Ariat source does right
- Real brand logos with distinctive colors, fonts, and marks create instant recognition
- Logos are spaced naturally on a white background -- no boxes, no borders, no grid cells
- Varying logo sizes create organic visual rhythm
- The referral bar at the bottom is a full-width dark gradient with colored keyword highlighting
- The overall impression is "these are our clients" not "here is a list of names"

### Possible fixes (for next builder)
1. **Use logo CDN images.** Services like Clearbit Logo API (`logo.clearbit.com/company.com`), SVGPorn, or Simple Icons could provide actual logos. This is by far the best fix.
2. **If text-only is unavoidable:** Remove all borders and boxes. Use the actual brand typography or at minimum vary font sizes and weights dramatically. Place names on a clean white background with generous spacing, more like a word cloud than a grid. Consider using brand colors for each name.
3. **Never use identical uniform boxes for a logo slide.** The uniformity is what makes it look like a data table.

---

## General Lessons for All Builders

### Do
- **Look at your output.** Run a Playwright screenshot and compare to the source. If the source has rich visual variety and yours has uniform rectangles, something is wrong.
- **Match the visual density and texture of the source**, not just the content. A logo slide's job is visual impression, not data transfer.
- **Slide 1 patterns work** -- split screens, gradient panels, stats bars, pill badges. Reuse them.

### Don't
- **Don't substitute visual richness with uniform containers.** A grid of identical boxes is never a substitute for logos, images, or visually distinct elements.
- **Don't rely on subtle CSS differences** (1px font weight changes, 1px size differences) to create visual hierarchy. If you can't see the difference in a screenshot, it doesn't exist.
- **Don't leave empty grid cells.** If the grid doesn't fill evenly, change the grid.
- **Don't build a slide that looks like a wireframe.** Every slide should look finished and intentional.
