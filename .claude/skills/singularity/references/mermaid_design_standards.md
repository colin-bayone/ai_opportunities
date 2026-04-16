# Mermaid Diagram Design Standards

## Purpose

Professional, polished diagrams for architecture, application workflows, data flows, decision trees, and ecosystem overviews. These standards ensure every mermaid diagram produced by the skill is visually consistent, readable, and presentation-ready.

## When These Standards Apply

Any time the skill generates a mermaid.js diagram, whether:
- Embedded in a presentation slide
- As a standalone chart file in `charts/`
- Embedded in a long-form deliverable document
- As part of a knowledge transfer session

---

## Theme Initialization

### Blue Palette (Presentations and Slide Decks)

Used for all presentation-context diagrams. Matches the slide design language.

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

### Purple Palette (Deliverable Documents and Proposals)

Used for diagrams embedded in BayOne design system documents (proposals, architecture docs).

```javascript
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  themeVariables: {
    primaryColor: '#ede9fe', primaryTextColor: '#1e1b4b', primaryBorderColor: '#7c3aed',
    lineColor: '#7c3aed', secondaryColor: '#e8f4fd', secondaryTextColor: '#0c4a6e',
    secondaryBorderColor: '#0078d4', edgeLabelBackground: '#ede9fe',
    clusterBkg: '#f8fafc', clusterBorder: '#94a3b8',
    fontSize: '13px', fontFamily: 'Inter, sans-serif'
  },
  flowchart: { curve: 'basis', nodeSpacing: 50, rankSpacing: 60, htmlLabels: false, useMaxWidth: false, padding: 16 }
});
```

### Compact Variant (Inline in Slides)

When a diagram is rendered inline within a slide (not a dedicated diagram slide), reduce font and spacing:

```javascript
fontSize: '11px',
flowchart: { curve: 'basis', nodeSpacing: 40, rankSpacing: 50, htmlLabels: false, useMaxWidth: false, padding: 12 }
```

---

## Color Palette for Subgraph Clusters and Nodes

Use semantic color coding to make diagrams self-explanatory. Colors indicate the category of each component.

### Cluster (Subgraph) Colors

| Category | Fill | Stroke | Text | When to Use |
|----------|------|--------|------|-------------|
| Code / Source | `#eff6ff` | `#2563eb` | `#1e3a5f` | Repositories, source code, version control |
| Build / Compute | `#dbeafe` | `#3b82f6` | `#1e3a5f` | Build systems, CI/CD, processing engines |
| Storage / Data | `#fef9c3` | `#ca8a04` | `#713f12` | Databases, file systems, blob storage, NFS |
| Existing / Legacy / POC | `#fef2f2` | `#f87171` | `#991b1b` | Current-state systems, POC work, things being replaced |
| Proposed / New | `#dcfce7` | `#16a34a` | `#14532d` | Proposed architecture, new components, improvements |
| AI / Intelligence | `#ede9fe` | `#7c3aed` | `#3b0764` | AI/ML models, language models, inference |
| External / Integration | `#ffedd5` | `#ea580c` | `#7c2d12` | Third-party services, external APIs, integrations |
| Observability / Monitoring | `#fef9c3` | `#ca8a04` | `#713f12` | Logging, metrics, tracing, dashboards |
| Deprecated / Inactive | `#e2e8f0` | `#94a3b8` | `#475569` | Phased-out components, deprecated systems |

### Node Colors Within Clusters

Nodes within a cluster use the same color family as their parent cluster but with `stroke-width: 1px` instead of the cluster's `2px` or `3px`. This creates visual hierarchy: cluster borders are prominent, node borders are subtle.

```
style CLUSTER fill:#eff6ff,stroke:#2563eb,stroke-width:2px,color:#1e3a5f
style NODE_IN_CLUSTER fill:#eff6ff,stroke:#2563eb,stroke-width:1px,color:#1e3a5f
```

---

## Node Formatting

### Multi-Line Nodes

Use markdown-style formatting within node labels for title + description:

```
NODE["`**Title**
Description text`"]
```

This produces a bold title on the first line and regular description below. Keeps nodes informative without being cluttered.

### Single-Line Nodes

```
NODE["Title"]
```

Both are valid options. Ask the user if unsure which is appropriate for the context.

---

## Line Style Conventions

| Style | Syntax | Meaning |
|-------|--------|---------|
| Solid arrow | `-->` | Current, confirmed flow |
| Dashed arrow | `-.->` | Proposed, future, or optional flow |
| Solid with label | `-->\|"Label"\|` | Flow with description |
| Thick solid | Use `stroke-width: 3px` on cluster | Primary grouping boundary |

---

## Layout Conventions

| Direction | Syntax | When to Use |
|-----------|--------|-------------|
| Top to bottom | `graph TB` | Hierarchies, architectures, layered systems |
| Left to right | `graph LR` | Sequential processes, pipelines, data flows |

### Spacing

- `nodeSpacing: 50` for standard diagrams
- `nodeSpacing: 40` for compact/inline diagrams
- `rankSpacing: 60` for standard
- `rankSpacing: 50` for compact

---

## CSS Overrides

Always include these CSS overrides for consistent rendering:

```css
.mermaid { display: flex; justify-content: center; }
.mermaid .node rect, .mermaid .node polygon { rx: 8 !important; ry: 8 !important; }
.mermaid .edgeLabel rect { fill: #dbeafe !important; fill-opacity: 1 !important; stroke: none !important; }
```

For purple palette, change the edge label fill:
```css
.mermaid .edgeLabel rect { fill: #ede9fe !important; fill-opacity: 1 !important; stroke: none !important; }
```

---

## Mermaid Rendering Pattern

Two rendering approaches are available. Both are valid:

```javascript
document.querySelectorAll('.mermaid-src').forEach(async (el) => {
  const src = el.textContent.trim();
  const container = el.parentElement;
  try {
    const { svg } = await mermaid.render('mermaid-' + Math.random().toString(36).slice(2), src);
    container.innerHTML = svg;
  } catch (e) {
    container.innerHTML = '<p style="text-align:center;color:#64748b;">Diagram rendering failed. Open in a browser with JavaScript enabled.</p>';
  }
});
```

The `<pre class="mermaid-src">` pattern keeps the source separate from the rendered output, and the random ID prevents collisions when multiple diagrams exist on one page.

---

## Standalone Chart File Pattern

Every standalone chart file in a `charts/` subfolder must include:

1. Title (h1) and subtitle (p) centered above the diagram
2. Back button (fixed position, top-left) — see `presentation_design_language.md` for the CSS
3. Mermaid initialization with the appropriate theme
4. The async rendering pattern
5. A `<noscript>` fallback message

See `gold_standards/charts/example_ecosystem_diagram.html` for the reference implementation.

---

## Diagram Types and Their Patterns

### Architecture Diagram

- Direction: `graph TB` (top to bottom)
- Use subgraph clusters for logical groupings (e.g., "Azure Cloud," "On-Prem," "Observability")
- Color-code clusters by category
- Show data flow between clusters with labeled arrows
- Good for: system architecture, deployment topology, infrastructure overview

### Workflow / Pipeline Diagram

- Direction: `graph LR` (left to right)
- Linear flow with decision points (rhombus nodes)
- Use dashed lines for retry/error paths
- Label edges with conditions ("Pass," "Fail," "Retry")
- Good for: CI/CD pipelines, agent workflows, data processing pipelines

### Ecosystem Diagram

- Direction: `graph LR` or `graph TB` depending on flow
- Separate clusters for current state vs. proposed state
- Red for existing/POC, green for proposed
- Dashed arrows for proposed flows, solid for current
- Good for: showing what exists today alongside what you plan to build

### Data Flow Diagram

- Direction: `graph LR`
- Emphasize storage nodes (yellow/amber family)
- Show transformations as process nodes (blue family)
- Label edges with what data moves between nodes
- Good for: ETL flows, data pipeline architecture, integration maps

### Decision Tree

- Direction: `graph TB`
- Rhombus nodes for decision points
- Label edges with yes/no or condition text
- Terminal nodes in green (positive outcome) or red (negative outcome)
- Good for: decision workflows, triage logic, classification trees

---

## Gold Standard Charts

See `gold_standards/charts/` for reference implementations. Each demonstrates the standards above applied to a specific diagram type.

| File | Type | Theme |
|------|------|-------|
| `example_ecosystem_diagram.html` | Ecosystem (current + proposed) | Blue |

Additional gold standards for other diagram types will be added as real engagement work produces them. The ecosystem diagram is the first and currently the only gold standard.

---

## Quality Checklist

Before finalizing any diagram:

- [ ] Color coding is semantic (not arbitrary)
- [ ] Subgraph clusters have descriptive titles
- [ ] Multi-line nodes have bold titles and regular descriptions
- [ ] Solid lines for current flows, dashed for proposed
- [ ] Font is Inter, appropriate size for context (13px standard, 11px compact)
- [ ] CSS overrides for rounded corners and edge label backgrounds are included
- [ ] Async rendering pattern is used (not startOnLoad)
- [ ] If standalone chart file: has back button, title, subtitle, and noscript fallback
