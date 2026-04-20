# Prompt: Generate Mermaid Shape Library HTML Files

**Give this prompt to a new Claude Code session in the ai_opportunities repository.**

---

## Context

We are building a visual shape library for the Singularity skill's mermaid diagram capabilities. The goal is a set of individual HTML files, each showing a specific category of mermaid features with live rendered examples that you can open in a browser and see.

A comprehensive reference document already exists at `.claude/skills/singularity/references/mermaid_shape_library.md` that lists every shape, arrow, icon, and formatting option. Your job is to turn each section of that reference into a standalone HTML file with live mermaid diagrams demonstrating every item.

## What to Read First

1. **`.claude/skills/singularity/references/mermaid_shape_library.md`** — The complete reference. Each major section becomes one HTML file.
2. **`.claude/skills/singularity/references/mermaid_design_standards.md`** — The visual standards (color palettes, theme variables, CSS overrides). Use these for consistent styling across all files.
3. **`claude/2026-04-13_mermaid_research/references/`** — Five exhaustive research documents on mermaid.js capabilities. Consult these if you need more detail on any feature:
   - `01_diagram_types_2026-04-13.md` — All 21 diagram types
   - `02_styling_and_theming_2026-04-13.md` — All styling and theming options
   - `03_node_shapes_and_arrows_2026-04-13.md` — Every node shape and arrow type
   - `04_advanced_features_2026-04-13.md` — Icons, click events, accessibility, config
   - `05_professional_examples_and_patterns_2026-04-13.md` — Design patterns and anti-patterns
4. **`claude/2026-04-13_mermaid_research/diagrams/v5_mermaid11_icons.html`** — The current best version of a polished diagram. Use this as the HTML template reference for page structure, back button, mermaid initialization, and the post-render cluster label fix.

## Output Location

Create all files in: `claude/2026-04-13_mermaid_research/shape_library/`

## Files to Create

Each file is a standalone HTML page with live mermaid diagrams. Use mermaid v11 CDN (`https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js`), `htmlLabels: true`, and the blue palette theme from the design standards.

### 1. `01_classic_shapes.html`

**Title:** Classic Node Shapes
**Content:** One mermaid diagram showing ALL 14 classic shapes side by side (rectangle, rounded, stadium, subroutine, cylinder, circle, diamond, hexagon, both parallelograms, both trapezoids, double circle, asymmetric). Each node should be labeled with both its name and its syntax. Arrange in a grid-like layout using subgraphs or careful LR/TB positioning. Color each shape with a different shade from the blue palette so they are visually distinct.

### 2. `02_v11_shapes.html`

**Title:** New Shapes (Mermaid v11.3+)
**Content:** One or more mermaid diagrams showing the `@{shape:}` syntax shapes: document, multi-document, card/notch-rect, lined rectangle, lined cylinder, small circle, framed circle, fork/join, hourglass, lightning bolt, triangle, flag, delay, stacked rect, window pane, braces. Each labeled with name and syntax. Note: these require mermaid v11.3+ and may not all render depending on the CDN version available. Include a note at the top explaining this.

### 3. `03_arrows_and_edges.html`

**Title:** Arrow and Edge Types
**Content:** Multiple small mermaid diagrams demonstrating:
- All line styles (solid, dotted, thick) with arrows
- Open links (no arrowhead)
- Circle and cross terminators
- Bidirectional arrows
- Edge length control (normal, long, extra long)
- Labeled edges (both pipe syntax and inline)
- Invisible links for spacing

Each example should be its own small diagram with a descriptive title above it.

### 4. `04_text_formatting.html`

**Title:** Text Formatting in Nodes
**Content:** Side-by-side examples showing:
- Bold text with `<b>` tags (htmlLabels: true mode)
- Multi-line text with `<br/>`
- Bullet characters (▸, •, ◦, →, ‣, –) in node labels
- FontAwesome icons in labels (`fa:fa-server`, `fa:fa-database`, etc.)
- Combined: icon + bold title + bullet detail lines (the pattern from v5)

### 5. `05_icons_reference.html`

**Title:** FontAwesome Icons for Architecture Diagrams
**Content:** A mermaid diagram (or multiple) showing all 25 common FA icons from the shape library rendered as actual icons in nodes. Group by category: infrastructure (server, database, hard-drive, cloud, network-wired), code (code-branch, file-code, hammer, gears), AI/ML (brain, microchip, robot), security (shield-halved, lock), communication (envelope, users, globe), status (circle-check, list-check, chart-line, clock, eye, bolt, plug). Each node shows the icon rendering with its `fa:fa-*` code as the label.

### 6. `06_classdef_styling.html`

**Title:** ClassDef Styling Examples
**Content:** One diagram demonstrating:
- 7+ classDef definitions with different colors
- Application via `:::className` syntax
- Dashed borders (`stroke-dasharray`)
- Different stroke widths
- The semantic color palette from the design standards (code=blue, storage=yellow, POC=red, proposed=green, AI=purple, deprecated=gray dashed, external=orange)
- Side-by-side comparison of styled vs unstyled nodes

### 7. `07_subgraphs_and_layout.html`

**Title:** Subgraphs, Nesting, and Layout
**Content:** Examples showing:
- Basic subgraph with title
- Nested subgraphs (2 levels)
- Direction override within subgraphs (`direction LR` inside a `TB` graph)
- Subgraph styling (colored backgrounds, borders)
- The post-render cluster label fix technique (include the JavaScript)

### 8. `08_diagram_types_gallery.html`

**Title:** Diagram Types Gallery
**Content:** Small example of each major diagram type beyond flowchart: sequence diagram, class diagram, state diagram, ER diagram, gantt chart, pie chart, mindmap, timeline, git graph. Each as its own small mermaid block with a heading above it. This is a visual gallery so the user can see what each type looks like and decide when to use it.

## HTML Template

Use this structure for every file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Page Title] — Mermaid Shape Library</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: #f8fafc; padding: 40px; color: #0f172a; }
        h1 { text-align: center; font-size: 28px; font-weight: 700; margin-bottom: 8px; }
        .subtitle { text-align: center; font-size: 14px; color: #64748b; margin-bottom: 32px; }
        .section { max-width: 1200px; margin: 0 auto 40px; }
        .section h2 { font-size: 18px; font-weight: 600; color: #1e3a5f; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 2px solid #dbeafe; }
        .section p { font-size: 13px; color: #64748b; margin-bottom: 16px; line-height: 1.6; }
        .section code { background: #eff6ff; padding: 2px 6px; border-radius: 4px; font-size: 12px; color: #1e40af; }
        .diagram-box { background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; margin-bottom: 24px; }
        .mermaid { display: flex; justify-content: center; }
        .nav { max-width: 1200px; margin: 0 auto 32px; display: flex; gap: 8px; flex-wrap: wrap; }
        .nav a { font-size: 12px; padding: 6px 12px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 6px; color: #1e40af; text-decoration: none; }
        .nav a:hover { background: #dbeafe; }
    </style>
</head>
<body>
    <h1>[Page Title]</h1>
    <p class="subtitle">Mermaid Shape Library — Visual Reference</p>

    <!-- Navigation to other pages in the library -->
    <div class="nav">
        <a href="01_classic_shapes.html">Classic Shapes</a>
        <a href="02_v11_shapes.html">v11 Shapes</a>
        <a href="03_arrows_and_edges.html">Arrows</a>
        <a href="04_text_formatting.html">Text Formatting</a>
        <a href="05_icons_reference.html">Icons</a>
        <a href="06_classdef_styling.html">ClassDef</a>
        <a href="07_subgraphs_and_layout.html">Subgraphs</a>
        <a href="08_diagram_types_gallery.html">Diagram Types</a>
    </div>

    <!-- Sections with diagrams go here -->

    <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
    <script>
        mermaid.initialize({
            startOnLoad: true,
            theme: 'base',
            themeVariables: {
                primaryColor: '#dbeafe', primaryTextColor: '#0f172a', primaryBorderColor: '#2563eb',
                lineColor: '#2563eb', secondaryColor: '#eff6ff', secondaryTextColor: '#1e3a5f',
                secondaryBorderColor: '#3b82f6', edgeLabelBackground: '#dbeafe',
                clusterBkg: '#f8fafc', clusterBorder: '#94a3b8',
                fontSize: '13px', fontFamily: 'Inter, sans-serif'
            },
            flowchart: { curve: 'basis', nodeSpacing: 50, rankSpacing: 60, htmlLabels: true, useMaxWidth: false, padding: 20 }
        });
    </script>
</body>
</html>
```

## Rules

- Each file must be fully self-contained (inline CSS, CDN links only)
- Use `startOnLoad: true` for simplicity (multiple diagrams per page)
- Each diagram goes inside a `.diagram-box` div for visual separation
- Every shape/arrow/feature shown must have its syntax displayed as a label or in a description paragraph above the diagram
- Navigation links at the top of every page link to all 8 pages
- Use the blue palette theme consistently
- No images — everything is mermaid rendered
- Test that diagrams actually render by ensuring syntax is correct for mermaid v11

## What Success Looks Like

A user opens `01_classic_shapes.html` in a browser and sees every classic node shape rendered as a live mermaid diagram with labels showing the syntax. They can click to `05_icons_reference.html` and see all 25 FontAwesome icons rendered as actual icons in nodes. The entire library is browsable as 8 interconnected pages.
