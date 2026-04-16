# BayOne Solutions Presentation Design Language

**Created:** 2026-04-10
**Purpose:** Defines the visual design language, shared components, and example patterns for generating BayOne-branded HTML presentations within the singularity skill.
**Source:** Derived from 21 production slides in `claude/2026-03-31_masterminds/content/`.
**Branding:** BayOne Solutions. No images or external media. Font Awesome icons only.

---

## Gold Standard Reference

Before generating a new presentation, read the gold standard deck at `.claude/skills/singularity/gold_standards/presentations/team_status_update/`. The README in that folder explains what each slide demonstrates. This is a real engagement deck that was used in a client meeting and represents the target quality level.

## How to Use This Spec

This document defines a **design language**, not a rigid template system. The example layouts below are patterns that have been proven to work well. When generating presentations:

1. **Read this spec** for the shared foundation (palette, typography, components, rules).
2. **Read the example HTML files** in `.claude/skills/singularity/layout_examples/` to see how the design language is applied in practice.
3. **Read the gold standard deck** at `gold_standards/presentations/team_status_update/` to see the design language applied end-to-end in a real deck.
4. **Design slides that fit the content.** Use example layouts as inspiration, combine elements from different examples, or create new arrangements that follow the design language. The content determines the layout, not the other way around.

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

### Embedded Diagram with Full-Screen Viewer

Mermaid.js diagrams can be embedded in slides with a link to open a full-screen version in a new tab. This uses two files: the slide itself (with a compact inline render) and a standalone chart file in a `charts/` subfolder.

**In the slide:**
```html
<div class="diagram-container">
  <div class="diagram-title">Diagram Title</div>
  <div class="mermaid"><pre class="mermaid-src">graph TB ...</pre></div>
  <a class="diagram-link" href="charts/diagram_name.html" target="_blank">Open full-screen diagram</a>
</div>
```

**CSS for the slide:**
```css
.diagram-container {
  background: var(--bg-subtle, #f8fafc);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  margin: 8px 0;
  overflow: hidden;
}
.diagram-container .diagram-title {
  font-size: 11px; font-weight: 600; color: var(--text-light);
  letter-spacing: 1px; text-transform: uppercase; margin-bottom: 12px; text-align: center;
}
.diagram-link {
  display: block; text-align: center; margin-top: 10px;
  font-size: 11px; color: var(--blue-accent); text-decoration: none;
}
.diagram-link:hover { text-decoration: underline; }
```

**In `charts/` subfolder:** A standalone HTML file with the diagram rendered full-page. Includes a title, subtitle, the mermaid source, the mermaid JS initialization, and a **back button** in the top-left corner. The back button uses `history.back()` so it returns to whatever slide opened it.

**Back button (required on all chart pages):**
```html
<a class="back-btn" onclick="history.back(); return false;" href="#"><i class="fa-solid fa-arrow-left"></i> Back to slides</a>
```

```css
.back-btn {
  position: fixed; top: 20px; left: 20px;
  display: flex; align-items: center; gap: 8px;
  padding: 8px 16px;
  background: rgba(12, 25, 41, 0.85); color: rgba(255,255,255,0.8);
  border: 1px solid rgba(255,255,255,0.15); border-radius: 8px;
  font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 500;
  text-decoration: none; cursor: pointer;
  transition: background 0.2s, color 0.2s; z-index: 100;
}
.back-btn:hover { background: rgba(37, 99, 235, 0.9); color: #fff; }
```

**Mermaid initialization (blue palette for slides):**
```javascript
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  themeVariables: {
    primaryColor: '#dbeafe', primaryTextColor: '#0f172a', primaryBorderColor: '#2563eb',
    lineColor: '#2563eb', secondaryColor: '#eff6ff', secondaryTextColor: '#1e3a5f',
    secondaryBorderColor: '#3b82f6', edgeLabelBackground: '#dbeafe',
    clusterBkg: '#f8fafc', clusterBorder: '#94a3b8',
    fontSize: '13px', fontFamily: 'Inter, sans-serif'
  },
  flowchart: { curve: 'basis', nodeSpacing: 50, rankSpacing: 60, htmlLabels: false, useMaxWidth: false, padding: 16 }
});
```

**Reference implementation:** See `gold_standards/charts/example_ecosystem_diagram.html` for the standalone chart pattern, and `gold_standards/presentations/team_status_update/02a_build_ecosystem_diagram.html` for the dedicated diagram slide.

**For mermaid visual standards (color palettes, node formatting, line styles, diagram types):** See `references/mermaid_design_standards.md`.

### Bullet Item Pattern (Default for All Card Bodies)

**This is the default content format for all cards.** Paragraph text in card bodies is a failure mode. Use bullet items instead.

```html
<div class="items">
  <div class="item"><i class="fa-solid fa-circle"></i><span><strong>Bold lead phrase</strong> elaboration and detail text</span></div>
  <div class="item"><i class="fa-solid fa-circle"></i><span><strong>Another lead</strong> with its description</span></div>
</div>
```

```css
.items { display: flex; flex-direction: column; gap: 5px; flex: 1; }
.item { display: flex; align-items: flex-start; gap: 8px; font-size: 11px; color: var(--text-light); line-height: 1.45; }
.item i { font-size: 5px; color: var(--blue-accent); margin-top: 5px; flex-shrink: 0; }
.item strong { color: var(--primary); font-weight: 600; }
```

**Pattern:** Bold lead phrase sets the key fact. Description text after the bold elaborates. Each item is scannable independently. 4-6 items per card is the sweet spot.

**When paragraph text IS acceptable:** Short lead paragraphs below a slide title (1-2 sentences), takeaway bar content, connection strip content. These are framing elements, not card bodies.

### Slide Navigation (Mandatory on All Multi-Slide Decks)

Every slide in a multi-slide deck must include prev/next/home navigation at the bottom-left.

```html
<div class="slide-nav">
  <a href="prev_slide.html"><i class="fa-solid fa-chevron-left"></i></a>
  <a href="next_slide.html"><i class="fa-solid fa-chevron-right"></i></a>
  <a href="00_title.html" style="margin-left: 6px;"><i class="fa-solid fa-house"></i></a>
</div>
```

```css
.slide-nav { position: fixed; bottom: 18px; left: 18px; display: flex; gap: 6px; z-index: 100; }
.slide-nav a { display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; border-radius: 8px; background: rgba(12,25,41,0.75); color: rgba(255,255,255,0.7); text-decoration: none; font-size: 14px; transition: background 0.2s, color 0.2s; border: 1px solid rgba(255,255,255,0.1); cursor: pointer; }
.slide-nav a:hover { background: rgba(37,99,235,0.9); color: #fff; }
.slide-nav a.disabled { opacity: 0.25; pointer-events: none; }
```

**Link chain rules:**
- First slide: prev is `class="disabled"` (no href)
- Last slide: next is `class="disabled"` (no href)
- Home: always points to `00_title.html`
- Every other slide: prev and next link to adjacent slides in sequence

### Question Block

Used for argument or reframing slides. Two variants:
- **Wrong:** Red-tinted background, strikethrough text (the bad approach)
- **Right:** Dark gradient background, white text (the better approach)

---

## Example Layout Patterns

The following patterns are demonstrated in the example HTML files. They are starting points for inspiration, not a closed set.

### Dark Full-Bleed (Title / Closing)

Full dark gradient background. Centered content. No header bar (or dark-themed header). Used for deck openers and closers.

**Examples:** `title.html`, `closing.html`
**Good for:** First slide, last slide, section dividers, high-impact single statements

### Split Panel (Left Explanation + Right Detail)

Two-column layout. Left panel (35-45%) provides context, framing, or a narrative. Right panel (55-65%) provides structured detail (cards, steps, examples). Left panel often has a subtle gray background or dark gradient background.

**Examples:** `split_concept.html`, `profile.html`
**Good for:** Deep dives, profiles, topic explorations, argument slides (wrong vs. right)

### Definition Bar + Content Area

Dark definition bar at the top establishes the concept. Light content area below breaks it down with cards, columns, or grids. Optionally ends with a takeaway bar.

**Good for:** New concept introductions, frameworks, comparisons, progression/evolution

### Card Grid (Full Width)

Standard header + lead text + grid of cards filling the content area. Cards can be in any grid arrangement (3-across, 3+2 staggered, 2x2, etc.). Often ends with a takeaway bar.

**Examples:** `three_column.html`, `grid_takeaway.html`
**Good for:** Overviews, enumerations, side-by-side comparisons, category breakdowns

### Agenda / Navigation

Horizontal row of section cards, each acting as a chapter summary. Card top borders use gradient progression.

**Examples:** `agenda.html`
**Good for:** Table of contents, roadmap, multi-track overview

### Diagram Pattern

Every diagram gets a standalone full-screen HTML file in a `charts/` subfolder. On the slide or document where the diagram appears, it is embedded inline with an "Open full-screen diagram" link that opens the standalone chart file in a new tab. The chart file has a back button to return to the prior view.

This pattern is the same regardless of diagram size or complexity. The inline embed lets the viewer see the diagram in context. The full-screen link lets them view it at full size when needed.

**Gold standard (correct pattern):** `gold_standards/charts/session_0_platform_overview.html` with `gold_standards/charts/charts/` — shows 3 diagrams embedded inline in a document, each with "Open full-screen diagram" links to standalone chart files.

**Also demonstrated in:** `gold_standards/presentations/team_status_update/02a_build_ecosystem_diagram.html` with `charts/build_log_ecosystem.html`

**Good for:** Any diagram in any context — architecture, data flow, ecosystem, workflow, or anything else.

### Status Grid (Colored Indicators)

Multi-column layout with status indicators using colored icons. Green (fa-check-circle, `#22c55e`) for granted/complete, amber (fa-clock, `#f59e0b`) for in-progress/pending, blue (fa-circle-exclamation, blue-accent) for needs-assistance/action-required.

**Gold standard:** `gold_standards/presentations/team_status_update/05_access_status.html`
**Good for:** Access status, environment readiness, checklist progress, approval status

---

## Rules for Generating Slides

### Technical Rules

1. **No images or external media.** Font Awesome icons only. No `<img>` tags.
2. **Self-contained HTML.** Each slide is a complete HTML document with inline `<style>`. CDN links for fonts and icons only.
3. **BayOne Solutions branding.** Logo reads "BayOne Solutions." Blue palette throughout.
4. **Aspect ratio 16:10.** All slides use `aspect-ratio: 16 / 10` on the `.slide` container. Max-width 1100px.
5. **Content must fit without scrolling.** If content overflows, split into multiple slides or reduce text.
6. **Date or context in header-title.** Every content slide shows context in the header.

### Content Rules

7. **Bullet formatting is the default for all card bodies.** Use the `.items` / `.item` pattern, not paragraph text. If unsure whether paragraphs are appropriate in a given context, ask the user. See the Bullet Item Pattern component above.
8. **Navigation is mandatory on every slide in a multi-slide deck.** First slide has prev disabled, last slide has next disabled, home always points to 00_title.html. See the Slide Navigation component above.
9. **Content must use specific details from the source material.** Vague corporate language is a failure mode. If the research library says "300K-500K lines per log file," the slide says that, not "substantial log files."
10. **Dense slides reduce readability.** If in doubt, split content across multiple slides. If the user says a section needs its own slide, give it its own slide.
13. **No individual names in slide content.** Presenter credit is allowed only on the title and closing slides. Content slides reference "the team," "the infrastructure team," etc.
14. **No direct quotes from any person.** Paraphrase all information as organizational knowledge.
15. **Diplomatic framing for any issue.** Problems are "alignment needed" or "items for discussion," not conflicts or criticisms. Existing work is called "prototypes" or "existing automation," not failures.
16. **Architectural ideas framed as preliminary.** Unless explicitly confirmed by the client, all architecture is "initial thinking" or "exploratory," not "the plan."
17. **No em dashes.** Consistent with singularity deliverable rules. Use commas, periods, or "and."
18. **Professional tone.** No contractions, no emojis, no colloquialisms.

### Process Rules

19. **Mandatory pre-generation reading.** Before generating any presentation slide, the skill (or its agents) must read this spec, ALL of the example HTML files from `.claude/skills/singularity/layout_examples/`, ALL of the mermaid shape library HTML files from `.claude/skills/singularity/mermaid_shape_library/` if diagrams are involved, AND a full worked gold standard (e.g., `gold_standards/presentations/team_status_update/` or `gold_standards/charts/`). This is enforced by the stop hook.
20. **Propose the slide list before generating.** Describe what each slide covers and the layout approach in plain language. Get user approval. Then generate.
21. **If a diagram is needed, propose a chart file in `charts/` and a dedicated diagram slide.** Do not embed diagrams in content slides.

### Common Failure Modes

These are patterns that were produced during the first real deck generation and had to be corrected. They are listed here so they are not repeated.

| Failure | What Went Wrong | Correct Approach |
|---------|----------------|-----------------|
| Paragraph text in cards | Cards had wall-of-text descriptions | Use bullet items (`.items`/`.item`) in every card |
| Missing navigation | Slides had no prev/next/home buttons | Navigation is mandatory on every slide |
| Vague content | Slides said "existing automation" instead of specific details | Draw from the research library: "Python script extracts subset of errors, passes to LLM" |
| Dense slides | 5 topics crammed into one slide | Split content across slides when density reduces readability |
| Missing back button on chart | Full-screen diagram had no way to return | Back button is mandatory on all chart pages |

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
2. Read at least 3 example HTML files from `layout_examples/`
3. Determine content from the research library
4. Propose a slide list with layout descriptions (not rigid IDs)
5. Get user approval
6. Generate slides using the design language
7. Output to the presentations folder

**This replaces the "Slide skill (TBD)" placeholder** in the singularity skill ecosystem. Presentation generation is a native singularity capability.
