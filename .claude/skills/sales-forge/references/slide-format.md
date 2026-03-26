# Slide Deck Format Guide

## Overview

BayOne slide decks are individual HTML files (one per slide), designed to be viewed in a browser and printed/exported to PDF.

**Reference implementation:** `/claude/2026-02-10_capabilities_deck/slides/`

---

## File Structure

```
slides/
├── 01_cover.html           # Title slide
├── 02_challenge.html       # Problem statement
├── 03_approach.html        # Our methodology
├── 04_solution.html        # Solution overview
├── 05_capability_1.html    # Capability details
├── 06_capability_2.html
├── ...
├── NN_next_steps.html      # Call to action / closing
└── logos/                  # Client and partner logos
    ├── client.png
    └── ...
```

**Naming Convention:** `NN_topic.html` where NN is zero-padded slide number.

---

## Slide Types

### Cover Slide

Full-page purple gradient with:
- Label (e.g., "AI Solutions Partner")
- Main title
- Subtitle
- Metadata (contact, date)
- BayOne logo (bottom right)

```html
<div class="cover">
  <div class="cover-content">
    <div class="cover-label">[Document Type]</div>
    <h1>[Title]</h1>
    <p class="cover-subtitle">[Subtitle]</p>
    <div class="cover-meta">
      <div class="cover-meta-item">
        <label>Contact</label>
        <span>[Name, Title]</span>
      </div>
      <div class="cover-meta-item">
        <label>Date</label>
        <span>[Month Year]</span>
      </div>
    </div>
  </div>
  <div class="logo">Bay<span>One</span> Solutions</div>
</div>
```

### Content Slides

White background with:
- Slide number (top left, subtle)
- Section title
- Content area (flexible layout)
- Footer with BayOne logo

**Layout Options:**
- Single column (full width content)
- Two column (side-by-side comparison)
- Icon grid (capabilities overview)
- Stat cards (metrics/numbers)

### Closing Slide

Similar to cover but with:
- Contact information
- Call to action
- "Let's Talk" or "Next Steps" messaging

---

## CSS Pattern

Each slide is self-contained with embedded styles:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Slide Title] - BayOne Solutions</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* Base reset */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      min-height: 100vh;
    }

    /* Slide container - full viewport */
    .slide {
      min-height: 100vh;
      padding: 60px;
      display: flex;
      flex-direction: column;
    }

    /* Slide number */
    .slide-number {
      position: absolute;
      top: 30px;
      left: 30px;
      font-size: 12px;
      font-weight: 600;
      color: #a855f7;
      letter-spacing: 2px;
    }

    /* Content area */
    .slide-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    /* Footer */
    .slide-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 20px;
      border-top: 1px solid #e2e8f0;
    }

    /* Print optimization */
    @media print {
      @page { size: 11in 8.5in; margin: 0; }  /* Landscape */
      .slide { height: 8.5in; }
    }
  </style>
</head>
<body>
  <div class="slide">
    <div class="slide-number">02</div>
    <div class="slide-content">
      <!-- Slide content here -->
    </div>
    <div class="slide-footer">
      <span class="footer-logo">Bay<span>One</span> Solutions</span>
    </div>
  </div>
</body>
</html>
```

---

## Design Guidelines

### Do:
- Keep each slide focused on ONE key message
- Use large, readable text (minimum 24px for body)
- Use whitespace generously
- Keep bullet points to 3-5 max per slide
- Use icons/visuals where possible
- Maintain consistent header placement

### Don't:
- Cram too much content on one slide
- Use small text that won't read in a room
- Use more than 3 font sizes per slide
- Use animations or interactive elements (they don't print)
- Mix horizontal and vertical slides in same deck

---

## Icon Patterns

For capability slides, use icon + title + description format:

```html
<div class="capability-card">
  <div class="capability-icon">
    <!-- SVG icon or emoji-free icon representation -->
    <svg>...</svg>
  </div>
  <h3 class="capability-title">Developer Productivity</h3>
  <p class="capability-desc">AI-assisted coding, testing, and documentation</p>
</div>
```

---

## Logo Guidelines

- BayOne logo always bottom-right on cover slides
- Smaller footer logo on content slides
- Client logos: Use high-quality PNGs with transparency
- Store in `logos/` subdirectory

---

## PDF Export

Use the `html_to_pdf.py` script to merge slides:

```bash
python scripts/html_to_pdf.py slides/ deck.pdf --merge --landscape
```

This converts all numbered HTML files and merges them in order.
