# Presentations and Mermaid Diagrams

## Overview

Between April 10 and April 14, 2026, a multi-session effort established an end-to-end system for generating BayOne-branded HTML presentations and mermaid.js diagrams within the singularity skill. This system encompasses a design language specification, reusable components, gold standard reference decks, a comprehensive mermaid shape library, and codified visual standards for diagrams. Several prescriptive rules were introduced during the process and subsequently corrected through a B2 violation audit.

This document covers every aspect of the system: what exists, where it lives, how it works, what was corrected, and what remains to be done.

---

## The Presentation Design Language

### What It Is

The presentation design language (`references/presentation_design_language.md`) defines the visual foundation for generating BayOne-branded HTML slide decks. It was derived from 21 production slides created for the Cisco CI/CD engagement and refined through iterative correction during the first real deck generation (the Srinivas status update deck).

The design language is not a rigid template system. It defines a shared visual vocabulary (palette, typography, components, layout patterns) and expects slide generators to compose from these building blocks based on the content at hand. The spec explicitly states that a well-designed slide following the design language but not matching any example layout is better than content forced into a layout that does not fit.

### Design System Foundation

- **Font:** Inter (Google Fonts), weights 300-700
- **Icons:** Font Awesome 6.5.1 (CDN). No images or external media of any kind.
- **Aspect ratio:** 16:10 on the `.slide` container, max-width 1100px
- **Page background:** `#e6e8eb` with a centered slide card using a subtle shadow
- **Color palette:** A blue family from `#0c1929` (darkest) through `#3b82f6` (accent) to `#94a3b8` (steel). Defined as CSS custom properties.
- **Gradient progression:** When 3+ sequential peer elements (cards, icon badges) appear, they follow a dark-to-light gradient progression across the blue family for visual hierarchy.
- **Branding:** Logo reads "BayOne Solutions" with the word "Solutions" in blue accent. Light and dark variants exist for different slide backgrounds.

### Reusable Components

The spec defines these shared components that can be mixed freely across slides:

| Component | Purpose |
|-----------|---------|
| Standard Slide Header | Thin bar with logo left, context label right |
| Footer Bar | 3px gradient bar at the bottom of every slide |
| Card | Fundamental content unit: icon badge + title + bullet items |
| Definition Bar | Dark gradient strip at top of content area introducing a concept |
| Takeaway Bar | Dark gradient strip at bottom summarizing the slide key point |
| Connection Strip | Same visual as takeaway bar but used inside panels |
| Bullet Item Pattern | Default for all card bodies: bold lead phrase + description |
| Slide Navigation | Prev/next/home buttons, mandatory on all multi-slide decks |
| Question Block | Wrong (red, strikethrough) vs. Right (dark, white text) |
| Embedded Diagram | Inline mermaid + "Open full-screen" link to charts/ HTML |

### Example Layout Patterns

Seven example HTML files live in `assets/slide_examples/` and demonstrate proven layout patterns:

| File | Pattern |
|------|---------|
| `example_title.html` | Dark full-bleed title |
| `example_closing.html` | Dark full-bleed closing |
| `example_split_concept.html` | Two-column split (explanation + detail) |
| `example_profile.html` | Split panel with profile content |
| `example_three_column.html` | Full-width three-card grid |
| `example_grid_takeaway.html` | Card grid ending with takeaway bar |
| `example_agenda.html` | Horizontal row of section/chapter cards |

Three additional layout patterns are described in the spec text (definition bar + content area, evolution row, two-column) but were never created as example HTML files. This is tracked as path issues 5-7 in the path issues master document.

### Content and Process Rules

The spec includes rules in three categories: technical (self-contained HTML, 16:10 ratio, no images), content (bullet formatting default, specific details from source material, diplomatic framing, no em dashes), and process (mandatory pre-generation reading, propose slide list before generating, get user approval).

Several of these rules were found to contain prescriptive additions during the B2 violation audit. The corrections are detailed in the "Key Corrections" section below.

---

## The Diagram Pattern

### The Correct Pattern

Every diagram, regardless of size or complexity, follows the same two-file pattern:

1. **Inline embed** in the parent document (slide, knowledge transfer session, deliverable). The diagram is rendered inline within a `.diagram-container` so the viewer sees it in context.
2. **Standalone full-screen HTML file** in a `charts/` subfolder adjacent to the parent document. This file renders the diagram at full page size with a back button that uses `history.back()` to return to whatever opened it.
3. **"Open full-screen diagram" link** on the inline embed that opens the standalone chart file in a new tab.

This pattern applies uniformly. There are no thresholds based on node count, complexity, size, or diagram type. The inline embed shows the diagram in context. The full-screen link provides a way to examine detail. If the user determines a specific diagram is too large or too small for its context, they provide feedback and the layout is adjusted on a case-by-case basis.

### The Gold Standard Reference

The correct implementation of this pattern is demonstrated in the TalentAI knowledge transfer session 0 gold standard:

- **Parent document:** `assets/design/gold_standards/knowledge_transfer/session_0_platform_overview.html`
- **Charts folder:** `assets/design/gold_standards/knowledge_transfer/charts/`
  - `fishbone_apps.html`
  - `architecture_overview.html`
  - `candidate_data_flow.html`

This document contains three diagrams, all embedded inline within the long-form HTML with "Open full-screen diagram" links pointing to the `charts/` subfolder. Each chart file has a back button, title, subtitle, mermaid initialization, and the diagram source. This is the pattern to follow for any future diagram in any context.

The Srinivas status deck also demonstrates the pattern within presentations:
- Slide `02a_build_ecosystem_diagram.html` has an inline embed with a link to `charts/build_log_ecosystem.html`

### What Goes Wrong Without This Pattern

During the Srinivas deck generation, the first attempt produced a diagram crammed into a content slide without a full-screen alternative. The content area shrank and the diagram was unreadable. This was corrected by creating a dedicated diagram slide (02a) with the inline/charts pattern. However, the correction was then over-generalized into a rule banning all diagram embedding in content slides, which contradicted the knowledge transfer gold standard where diagrams are embedded directly in the document body. The B2 audit resolved this: the pattern is always inline embed plus charts/ full-screen, and there is no ban on where diagrams can appear.

---

## Mermaid Design Standards

### Two Theme Palettes

The mermaid design standards (`references/mermaid_design_standards.md`) define two color palettes:

- **Blue palette** for presentations and slide decks. Matches the slide design language. Primary color `#dbeafe`, borders `#2563eb`, lines `#2563eb`.
- **Purple palette** for deliverable documents and proposals. Matches the BayOne design system. Primary color `#ede9fe`, borders `#7c3aed`, lines `#7c3aed`.

Both use the same structural settings: Inter font, `basis` curve, `startOnLoad: false` (for the async rendering pattern), and `useMaxWidth: false`.

A compact variant reduces font size to 11px and tightens spacing for diagrams rendered inline within slides rather than on dedicated diagram slides or full-screen chart pages.

### Semantic Color Coding

Subgraph clusters and nodes use a semantic color system where colors indicate category rather than being arbitrary:

| Category | Fill | Stroke |
|----------|------|--------|
| Code / Source | `#eff6ff` | `#2563eb` |
| Build / Compute | `#dbeafe` | `#3b82f6` |
| Storage / Data | `#fef9c3` | `#ca8a04` |
| Existing / Legacy / POC | `#fef2f2` | `#f87171` |
| Proposed / New | `#dcfce7` | `#16a34a` |
| AI / Intelligence | `#ede9fe` | `#7c3aed` |
| External / Integration | `#ffedd5` | `#ea580c` |
| Observability / Monitoring | `#fef9c3` | `#ca8a04` |
| Deprecated / Inactive | `#e2e8f0` | `#94a3b8` |

Nodes within a cluster use the same color family as their parent but with `stroke-width: 1px` (vs. `2px` or `3px` for cluster borders) to create visual hierarchy.

### Line Style Conventions

- Solid arrows (`-->`) for current, confirmed flows
- Dashed arrows (`-.->`) for proposed, future, or optional flows
- Thick arrows (`==>`) for emphasis or primary paths
- Edge labels use `|"Label"|` pipe syntax

### Node Formatting

Multi-line nodes with bold titles and description text are one option. Single-line nodes with just a title are another. Neither is "preferred" over the other. The choice depends on the content. The B2 audit removed a prescriptive "preferred" label and a "fewer than 6 nodes" threshold that had been added without basis.

### CSS Overrides

Three CSS overrides are always included for consistent rendering:
1. `.mermaid { display: flex; justify-content: center; }` for centering
2. `.mermaid .node rect, .mermaid .node polygon { rx: 8 !important; ry: 8 !important; }` for rounded corners
3. `.mermaid .edgeLabel rect { fill: #dbeafe !important; }` (or `#ede9fe` for purple) for edge label backgrounds

---

## Mermaid v10 vs. v11 Differences

The diagram progression (v1 through v5) revealed significant differences between mermaid v10 and v11 that affect how diagrams are authored.

### The Core Trade-off in v10

In mermaid v10, you must choose between two mutually exclusive modes:

- **`htmlLabels: true`**: Enables FontAwesome icon rendering as actual glyphs via `fa:fa-icon-name`. However, bold text requires `<b>` HTML tags, and line breaks require `<br/>`. The markdown `**bold**` syntax does not work.
- **`htmlLabels: false`**: Enables markdown formatting (`**bold**`, literal newlines). However, FontAwesome icons render as literal text strings instead of glyphs.

The Srinivas deck gold standard was built with `htmlLabels: false` (markdown mode), which gave bold titles and multi-line nodes but no icons.

### What v11 Provides

Mermaid v11 with `htmlLabels: true` resolves the trade-off. You get icon rendering as actual Font Awesome glyphs AND formatted text, but all formatting must use HTML syntax:
- Bold via `<b>Title</b>` instead of `**Title**`
- Line breaks via `<br/>` instead of literal newlines
- Bullet characters (`&#9656;` for the triangle, or literal Unicode) work in both modes

### Other v11 Changes

- New `@{shape:}` syntax for 17 additional node shapes (document, multi-document, hourglass, lightning bolt, flag, etc.) requiring v11.3+
- The `architecture-beta` diagram type for system architecture with icons
- Additional diagram types: kanban, packet-beta, xychart-beta

### Rendering Approaches

Two rendering approaches were validated:

1. **`startOnLoad: true`**: Simpler. Used in the shape library HTML files. Mermaid automatically finds and renders `<pre class="mermaid">` elements on page load. Works well for pages with multiple diagrams.
2. **Async rendering with `startOnLoad: false`**: More control. Uses `mermaid.run()` followed by post-render JavaScript (such as the cluster label fix). The B2 audit corrected an "always use async" rule since both approaches are valid.

### Post-Render Cluster Label Fix

A known SVG rendering issue causes edge lines to paint on top of subgraph cluster labels because SVG renders elements in DOM order. The fix (implemented in v5) clones cluster labels to the end of the SVG after rendering, adding opaque background rectangles that match the parent cluster's border color. The complete working implementation is in `claude/2026-04-13_mermaid_research/diagrams/v5_mermaid11_icons.html`.

---

## The Shape Library

### What It Is

The shape library is a set of 8 interactive HTML files that serve as a visual reference for every mermaid.js shape, arrow, icon, formatting option, and diagram type. Each file renders live mermaid diagrams in the browser demonstrating the features it covers.

### Where It Lives

Two copies exist:
- **Working copy:** `claude/2026-04-13_mermaid_research/shape_library/` (where they were developed and audited)
- **Deployed copy:** `.claude/skills/singularity/assets/mermaid_shape_library/` (where the skill reads them)

### The 8 Files

| File | Content | Notable Details |
|------|---------|-----------------|
| `01_classic_shapes.html` | All 14 classic node shapes (rectangle, rounded, stadium, subroutine, cylinder, circle, diamond, hexagon, both parallelograms, both trapezoids, double circle, asymmetric) | Split into 4 diagram boxes (Basic, Geometric, Directional, Special). Each shape uses a distinct saturated color. |
| `02_v11_shapes.html` | 17 new `@{shape:}` syntax shapes plus icon and image node types (19 total) | Requires mermaid v11.3+. Includes a note explaining version dependency. |
| `03_arrows_and_edges.html` | All line styles, arrowhead variants, circle/cross terminators, bidirectional arrows, edge length control, labeled edges, invisible links | Multiple small diagrams, each demonstrating a category. |
| `04_text_formatting.html` | Bold via `<b>`, multi-line via `<br/>`, all 6 bullet characters, FontAwesome icons in labels, combined icon+bold+bullets pattern, htmlLabels true vs. false comparison | Documents the v10 vs. v11 trade-off visually. |
| `05_icons_reference.html` | All 25 common FontAwesome icons for architecture diagrams grouped by category (infrastructure, code, AI/ML, security, communication, status) | Each node renders the actual icon glyph with its `fa:fa-*` code. |
| `06_classdef_styling.html` | classDef definitions, `:::className` application, dashed borders, stroke widths, semantic color palette, `rx` corner radius progression, batch `class A,B,C` application, `linkStyle default` | Demonstrates the 9-category semantic color system from the design standards. |
| `07_subgraphs_and_layout.html` | Basic subgraphs, nested subgraphs (2 levels), direction overrides, subgraph styling, post-render cluster label fix JavaScript | Includes the full JavaScript code block for the label fix technique. |
| `08_diagram_types_gallery.html` | Examples of all 21 mermaid diagram types: flowchart, sequence, class, state, ER, gantt, pie, mindmap, timeline, git graph, user journey, quadrant chart, requirement, sankey-beta, xychart-beta, block-beta, architecture-beta, kanban, packet-beta, C4Context, plus ZenUML (plugin-required note) | 20 with live rendered examples, 1 with explanation of plugin requirement. |

All files use mermaid v11 CDN, `htmlLabels: true`, the blue palette theme, `startOnLoad: true`, and cross-navigation links to all 8 pages.

### Development and Audit

The shape library was developed via a separate Claude Code session using a detailed prompt (`claude/2026-04-13_mermaid_research/prompt_for_shape_library_html.md`). After initial generation, every file was audited against the `mermaid_shape_library.md` reference for completeness. The audit and fix log (`claude/2026-04-13_mermaid_research/shape_library/TODO.md`) documents all corrections made:
- `01_classic_shapes.html`: Recolored with saturated fills, split from 1 monolithic diagram into 4, removed HTML entities from labels, added overflow:visible fix
- `02_v11_shapes.html`: Added icon and image shape sections
- `03_arrows_and_edges.html`: Fixed syntax error
- `06_classdef_styling.html`: Added linkStyle default, batch class, and rx corner radius examples
- `08_diagram_types_gallery.html`: Added 12 new diagram type examples, expanded reference table to all 21 types

---

## The 5 Research Documents

The mermaid research session produced 5 exhaustive reference documents from web research on mermaid.js capabilities. These live in `claude/2026-04-13_mermaid_research/references/`:

| File | Content | Size |
|------|---------|------|
| `01_diagram_types_2026-04-13.md` | All 21 mermaid diagram types with syntax, capabilities, and use cases | 53K |
| `02_styling_and_theming_2026-04-13.md` | Theme configuration, themeVariables, CSS overrides, custom themes | 40K |
| `03_node_shapes_and_arrows_2026-04-13.md` | Every node shape (classic + v11) and every arrow/edge type with syntax | 25K |
| `04_advanced_features_2026-04-13.md` | Icons, click events, accessibility, configuration options, integrations | 31K |
| `05_professional_examples_and_patterns_2026-04-13.md` | Design patterns, anti-patterns, real-world diagram examples | 26K |

These documents are raw research materials. The distilled, actionable versions are the three skill reference files: `mermaid_design_standards.md`, `mermaid_shape_library.md`, and the relevant sections of `presentation_design_language.md`.

---

## The v1-v5 Diagram Progression

The diagram progression used the Cisco CI/CD Build Log Ecosystem as a test subject, iterating through 5 versions to develop and validate the mermaid standards. All versions are in `claude/2026-04-13_mermaid_research/diagrams/`.

### v1: Baseline

- Mermaid v10 with `htmlLabels: false` (markdown mode)
- Basic flowchart with subgraph clusters
- Multi-line nodes using markdown `**bold**` and literal newlines
- No semantic shape differentiation (all rectangles)
- No icons (rendered as literal text in markdown mode)
- Established the basic structure: code repos, build system, storage, existing automation, proposed approach

### v2: Semantic Shapes

- Added shape differentiation: cylinders for databases, hexagons for orchestrators, subroutines for build tools, diamonds for verification, rounded rectangles for AI components
- Shapes now communicate node type visually
- Still no icons, still markdown mode

### v3: ClassDef Polish

- Added classDef classes matching the semantic color palette (codeRepo blue, buildTool blue, deprecated gray dashed, storage yellow, existingPoc red, proposed green, aiComponent purple)
- Dashed stroke for deprecated components (`stroke-dasharray: 5 5`)
- Added detail text to every node (line counts, retention periods, specific capabilities)
- This version established the visual quality target

### v4: Icons Attempt (v10)

- Attempted to add FontAwesome icons with `htmlLabels: false`
- Icons rendered as literal `fa:fa-server` text instead of glyphs
- Demonstrated the v10 trade-off: you get markdown formatting OR icons, not both
- Bold text and multi-line formatting still worked via markdown syntax

### v5: Mermaid v11 with Icons

- Upgraded CDN from mermaid v10 to v11
- Switched to `htmlLabels: true`
- Converted all formatting from markdown to HTML: `<b>` for bold, `<br/>` for line breaks
- FontAwesome icons now render as actual glyphs on every node
- Added the post-render cluster label fix (JavaScript to move labels on top of edges)
- Final result: full semantic shapes, full color coding, full icons, full detail text, cluster labels not obscured by edges

### What Was Learned

1. The v10/v11 `htmlLabels` trade-off is the single most important technical decision when authoring mermaid diagrams. It determines the entire formatting approach.
2. Semantic shapes add substantial readability even without colors or icons.
3. The classDef color palette makes diagrams self-documenting when categories are consistent.
4. The cluster label fix is necessary for any diagram with subgraphs and inter-cluster edges.
5. Detail text in nodes (specific numbers, retention periods, tool names) makes diagrams genuinely informative rather than just structural.

---

## Key Corrections: B2 Violations

The B2 violation review (`claude/2026-04-13_mermaid_research/b2_violation_review_2026-04-14.md`) identified 11 instances where specific, situational feedback was generalized into rigid universal rules with criteria that were never specified. This is the B2 violation pattern applied to rule-writing: taking a narrow correction and expanding it into an absolute ban or an invented threshold.

### Diagram-Related Corrections

**Absolute ban on embedding diagrams in content slides (Items 1, 11):** One specific diagram on one specific slide was too large. This was turned into a universal rule "Do not embed large diagrams inside content slides" and added to the failure modes table as "Diagram embedded in content slide." The correction: the diagram pattern is always inline embed plus charts/ full-screen link, applied uniformly regardless of context. There is no ban on where diagrams can appear. The knowledge transfer gold standard has three diagrams embedded inline in a long-form document. If a specific diagram does not work in a specific context, the user provides feedback.

**Invented node count threshold (Item 2):** A "4+ nodes" threshold was added for when a diagram should get its own slide. No such threshold was ever specified. The correction: remove the threshold entirely. Whether a diagram gets its own slide or is embedded in a content slide is situational, and the user decides.

**Invented slide density threshold (Item 3):** A "4+ substantive points" rule was added for when a section needs its own slide. This was based on one instance where one section should have been its own slide. The correction: remove the number. Whether content needs splitting is situational.

### Formatting-Related Corrections

**Paragraph exception enumeration (Item 4):** Bullet formatting was correctly established as the default for card bodies, but then an explicit list of where paragraphs ARE acceptable ("only for lead text, takeaway bars, and connection strips") was added. The user said bullets are the default for cards. If there is ambiguity about paragraph usage in a given context, ask. Do not enumerate the exceptions.

**"At least N" minimums for pre-generation reading (Items 5, 10):** Rules said "at least 3 example HTML files" or "at least 2 shape library files." The actual instruction was to read ALL the example files and ALL the shape library files. The correction: the pre-generation reading requirement is to read all example HTML files, all mermaid shape library files (when diagrams are involved), and a full worked gold standard.

### Mermaid Standards Corrections

**"Preferred" label on multi-line nodes (Item 6):** Multi-line nodes with bold titles were labeled as "Preferred for Complex Diagrams." No preference was stated. Both single-line and multi-line are valid options depending on the content.

**Node count threshold for single-line nodes (Item 7):** A "fewer than 6 nodes" criterion was added for when to use single-line vs. multi-line formatting. No such threshold was ever given. When in doubt, ask.

**"Always use async rendering" (Item 8):** The standards said to always use the async rendering pattern and never `startOnLoad: true`. The shape library files all use `startOnLoad: true` successfully. Both approaches are valid.

### The Pattern

The common thread across all these violations is the same: Claude took specific, situational feedback (one diagram was too big for one slide, one section needed its own slide, read all the files) and generalized it into rigid universal rules with invented thresholds and absolute language ("always," "never," "4+ nodes," "fewer than 6"). This is the B2 violation pattern applied to rule-writing itself. The fix in every case is the same: remove the invented threshold or absolute ban, state what was actually specified, and defer to the user for situational judgment.

---

## Gold Standard Assets

### Presentations Gold Standard

`assets/design/gold_standards/presentations/srinivas_status/`

A complete 8-slide status update deck from the Cisco CI/CD engagement. Demonstrates bullet formatting in all cards, slide navigation on every slide, diplomatic framing, specific details from source material, a dedicated diagram slide with charts/ subfolder, status grid with colored indicators, and every reusable component in the design language. A README in the directory explains what each slide demonstrates.

Slide chain: 00 (title) -> 01 (assigned items) -> 02 (build findings) -> 02a (ecosystem diagram) -> 03 (webex findings) -> 04 (discussion) -> 05 (access status) -> 06 (next steps)

### Knowledge Transfer Gold Standard

`assets/design/gold_standards/knowledge_transfer/session_0_platform_overview.html`

A long-form knowledge transfer document from the TalentAI engagement using the BayOne purple palette. Contains three embedded mermaid diagrams (fishbone app ecosystem, platform architecture, candidate data flow), each with an "Open full-screen diagram" link to a standalone chart in the adjacent `charts/` folder. This is the canonical reference for the diagram embed pattern in non-presentation contexts.

### Charts Gold Standard

`assets/design/gold_standards/charts/example_ecosystem_diagram.html`

A standalone full-screen ecosystem diagram using the blue palette theme. Demonstrates the chart file pattern: title, subtitle, back button, mermaid initialization, async rendering, and noscript fallback.

---

## What Still Needs to Happen

### Path and Structure Issues

The path issues master document (`claude/2026-04-13_mermaid_research/path_issues_master.md`) identified 10 issues from a verification pass across all skill files. The most relevant to presentations and diagrams:

- **Issues 5-7:** Three example layout patterns referenced in the presentation design language (`example_definition_bar.html`, `example_two_column.html`, `example_evolution_row.html`) were never created as HTML files. They need to be created or the references removed.
- **Issue 8:** Inconsistent path prefixes in the presentation design language. Some references use the short form (`gold_standards/presentations/`) and others use the full form (`assets/design/gold_standards/presentations/`). These should be made consistent.
- **Issue 4:** The `complete_structure.md` tree does not include the `assets/mermaid_shape_library/` directory (8 files) or several other assets added during these sessions. The tree needs a full refresh.

### Folder Restructure

A planned folder restructure for the singularity skill will affect where all these assets live. When this restructure happens, every path reference in the presentation design language, mermaid design standards, mermaid shape library reference, SKILL.md, and the gold standard README will need to be updated. This is a known coordination cost.

### B2 Corrections Not Yet Applied to Files

The B2 violation review document identifies all the prescriptive rules and their corrections, but notes that the actual file edits for several items were deferred for the user's decision. The presentation design language and mermaid design standards files may still contain some of the prescriptive language identified in the audit. A follow-up pass should verify each flagged item has been corrected in the actual reference files.

---

## File Inventory

### Skill Reference Files (`.claude/skills/singularity/references/`)

| File | Purpose |
|------|---------|
| `presentation_design_language.md` | Full design language spec: palette, components, layout patterns, rules |
| `mermaid_design_standards.md` | Theme palettes, semantic colors, line conventions, diagram types, quality checklist |
| `mermaid_shape_library.md` | Text reference of every shape, arrow, icon, formatting option |

### Skill Assets (`.claude/skills/singularity/assets/`)

| Directory | Contents |
|-----------|----------|
| `slide_examples/` | 7 example HTML files demonstrating layout patterns |
| `mermaid_shape_library/` | 8 interactive HTML files with live mermaid demos |
| `design/gold_standards/presentations/srinivas_status/` | Complete gold standard presentation deck (8 slides + charts/) |
| `design/gold_standards/knowledge_transfer/` | Gold standard knowledge transfer doc with 3 embedded diagrams + charts/ |
| `design/gold_standards/charts/` | Standalone ecosystem diagram gold standard |

### Session Working Files (`claude/2026-04-13_mermaid_research/`)

| Path | Contents |
|------|----------|
| `references/` | 5 exhaustive research documents on mermaid.js (175K total) |
| `diagrams/` | v1-v5 diagram progression (5 HTML files) |
| `shape_library/` | Working copy of the 8 shape library HTML files + audit TODO |
| `prompt_for_shape_library_html.md` | Prompt used to generate the shape library in a separate session |
| `b2_violation_review_2026-04-14.md` | Full prescriptive rules audit with 11 flagged items |
| `path_issues_master.md` | 10 path/reference issues identified across skill files |
