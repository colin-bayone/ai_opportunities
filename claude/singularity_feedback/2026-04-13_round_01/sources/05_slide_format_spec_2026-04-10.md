# BayOne Solutions Presentation Design Language

**Created:** 2026-04-10
**Purpose:** Defines the visual design language, shared components, and example patterns for generating BayOne-branded HTML presentations within the singularity skill.
**Source:** Derived from 21 production slides in `claude/2026-03-31_masterminds/content/`.
**Branding:** BayOne Solutions. No images or external media. Font Awesome icons only.

---

## How to Use This Spec

This document defines a **design language**, not a rigid template system. The example layouts below are patterns that have been proven to work well. When generating presentations:

1. **Read this spec** for the shared foundation (palette, typography, components, rules).
2. **Read the example HTML files** in `.claude/skills/singularity/assets/slide_examples/` to see how the design language is applied in practice.
3. **Design slides that fit the content.** Use example layouts as inspiration, combine elements from different examples, or create new arrangements that follow the design language. The content determines the layout, not the other way around.

The examples are a vocabulary, not a grammar. A well-designed slide that does not match any example exactly but follows the design language is better than content forced into an ill-fitting example layout.

---

## Design System Foundation

### Shared Across All Slides

**Font:** Inter (Google Fonts), weights 300-700
**Icons:** Font Awesome 6.5.1 (CDN)
**Aspect ratio:** 16:10 (`aspect-ratio: 16 / 10` on `.slide`, max-width 1100px)
**Border radius:** 12px (slide), 10px (cards), 7-8px (icon badges)
**Page background:** `#e6e8eb` (the slide sits centered on this)
**Shadow:** `0 2px 8px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.08)`

### Color Palette

```css
:root {
  /* Dark blues (backgrounds, dark panels, definition bars) */
  --blue-darkest: #0c1929;
  --blue-dark: #15293e;
  --blue-mid: #1e3a5f;

  /* Bright blues (accents, highlights, active elements) */
  --blue-bright: #2563eb;
  --blue-accent: #3b82f6;

  /* Steel (secondary text, muted elements, inactive states) */
  --steel-light: #64748b;
  --steel-glow: #94a3b8;

  /* Light mode text and borders */
  --primary: #0f172a;
  --text: #334155;
  --text-light: #64748b;
  --border: #e2e8f0;
}
```

### Gradient Progression System

When multiple cards, icons, or accent elements appear in sequence, they follow a gradient progression that creates visual hierarchy while staying within the blue family:

| Position | Gradient | Feel |
|----------|----------|------|
| 1st | `#0c1929 -> #1e3a5f` | Darkest, anchoring |
| 2nd | `#1e3a5f -> #2563eb` | Dark to bright |
| 3rd | `#2563eb -> #3b82f6` | Bright to accent |
| 4th | `#3b82f6 -> #4f93f7` | Accent to light |
| 5th | `#4f93f7 -> #64748b` | Light to steel |

This is not required for every slide. Use it when there are 3+ sequential peer elements (cards in a grid, stacked items, icon badges) and visual differentiation adds clarity.

### Branding

**Logo text (light slides):**
```html
<div class="header-logo">BayOne <span>Solutions</span></div>
```
"BayOne" in `var(--primary)`, "Solutions" in `var(--blue-accent)`.

**Logo text (dark slides/full-bleed):**
"BayOne" in `#fff`, "Solutions" in `var(--blue-accent)`.

---

## Reusable Components

These components appear across many slides and can be mixed freely.

### Standard Slide Header

Thin bar at the top. Logo left, context label right.

```html
<div class="slide-header">
  <div class="header-logo">BayOne <span>Solutions</span></div>
  <div class="header-title">{{context_label}}</div>
</div>
```

Context label: date, client name, engagement name, or section label. 11px, muted.

### Footer Bar

3px gradient bar at the bottom of every slide. The visual signature.

```html
<div class="slide-footer">
  <div class="slide-footer-bar"></div>
  <div class="slide-number">01</div>  <!-- optional -->
</div>
```

Light slides: `linear-gradient(90deg, var(--blue-darkest), var(--blue-mid), var(--blue-accent), var(--steel-glow))`
Dark slides: `linear-gradient(90deg, rgba(255,255,255,0.1), var(--blue-accent), rgba(255,255,255,0.1))`

Slide number is two-digit zero-padded, bottom-right, blue accent, 11px.

### Card

The fundamental content unit. Icon badge + title + description. Appears stacked vertically or in grids.

**Accent options:**
- Left border (3px, gradient, vertical): used in stacked/list cards
- Top border (3px, gradient, horizontal): used in grid cards

**Icon badge:** Small rounded square (28-38px), gradient background, white Font Awesome icon.

### Definition Bar

Full-width dark gradient strip at the top of the content area. Sets up a concept before the detail below.

```
Label (uppercase, small, blue accent)
Title (22px, white, bold)
Description (13-14px, white ~80% opacity)
```

Best for: section openers, concept introductions, framing statements.

### Takeaway Bar

Dark gradient strip with a single bold insight. Used at the bottom of the content area, above the footer. Summarizes the slide's key point.

```
Single paragraph, 14px, white ~85% opacity. Key phrase bolded in full white.
```

### Connection Strip

Same visual treatment as takeaway bar but used inside a panel (typically the left panel in split layouts). Smaller padding. Delivers a bridging insight.

### Question Block

Used for argument or reframing slides. Two variants:
- **Wrong:** Red-tinted background, strikethrough text (the bad approach)
- **Right:** Dark gradient background, white text (the better approach)

---

## Example Layout Patterns

The following patterns are demonstrated in the example HTML files. They are starting points for inspiration, not a closed set.

### Dark Full-Bleed (Title / Closing)

Full dark gradient background. Centered content. No header bar (or dark-themed header). Used for deck openers and closers.

**Examples:** `example_title.html`, `example_closing.html`
**Good for:** First slide, last slide, section dividers, high-impact single statements

### Split Panel (Left Explanation + Right Detail)

Two-column layout. Left panel (35-45%) provides context, framing, or a narrative. Right panel (55-65%) provides structured detail (cards, steps, examples). Left panel often has a subtle gray background or dark gradient background.

**Examples:** `example_split_concept.html`, `example_profile.html`
**Good for:** Deep dives, profiles, topic explorations, argument slides (wrong vs. right)

### Definition Bar + Content Area

Dark definition bar at the top establishes the concept. Light content area below breaks it down with cards, columns, or grids. Optionally ends with a takeaway bar.

**Examples:** `example_definition_bar.html`, `example_two_column.html`, `example_evolution_row.html`
**Good for:** New concept introductions, frameworks, comparisons, progression/evolution

### Card Grid (Full Width)

Standard header + lead text + grid of cards filling the content area. Cards can be in any grid arrangement (3-across, 3+2 staggered, 2x2, etc.). Often ends with a takeaway bar.

**Examples:** `example_three_column.html`, `example_grid_takeaway.html`
**Good for:** Overviews, enumerations, side-by-side comparisons, category breakdowns

### Agenda / Navigation

Horizontal row of section cards, each acting as a chapter summary. Card top borders use gradient progression.

**Examples:** `example_agenda.html`
**Good for:** Table of contents, roadmap, multi-track overview

---

## Rules for Generating Slides

1. **No images or external media.** Font Awesome icons only. No `<img>` tags.
2. **Self-contained HTML.** Each slide is a complete HTML document with inline `<style>`. CDN links for fonts and icons only.
3. **BayOne Solutions branding.** Logo reads "BayOne Solutions." Blue palette throughout.
4. **Aspect ratio 16:10.** All slides use `aspect-ratio: 16 / 10` on the `.slide` container. Max-width 1100px.
5. **Content must fit without scrolling.** If content overflows, split into multiple slides or reduce text.
6. **No em dashes.** Consistent with singularity deliverable rules.
7. **Professional tone.** No contractions, no emojis, no colloquialisms.
8. **Date or context in header-title.** Every content slide shows context in the header.
9. **Mandatory pre-generation reading.** Before generating any presentation slide, the skill (or its agents) must read this spec AND at least 3 of the example HTML files from `.claude/skills/singularity/assets/slide_examples/` to internalize the design language. This is enforced by the stop hook.

---

## Slide File Naming

For multi-slide decks within a dated subdirectory of `presentations/`:

```
/<client_name>/<opportunity_name>/presentations/<deck_name>_<date>/
├── 00_title.html
├── 01_<descriptive_name>.html
├── 02_<descriptive_name>.html
├── ...
└── NN_closing.html
```

For standalone slides: `<descriptive_name>_<date>.html` in `presentations/`.

---

## Integration with Singularity Skill

**Output location:** `/<client_name>/<opportunity_name>/presentations/`

**Invocation:** When the user requests a presentation:
1. Read this spec (`presentation_design_language.md`)
2. Read at least 3 example HTML files from `slide_examples/`
3. Determine content from the research library
4. Propose a slide list with layout descriptions (not rigid IDs)
5. Get user approval
6. Generate slides using the design language
7. Output to the presentations folder

**This replaces the "Slide skill (TBD)" placeholder** in the singularity skill ecosystem. Presentation generation is a native singularity capability.
