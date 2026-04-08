# Handoff: Fix Mermaid Edge Label Double Border

**Date:** 2026-04-02
**File:** `/home/cmoore/programming/ai_opportunities/sephora/edw_modernization/deliverables/architecture_diagram_2026-04-02.html`
**Priority:** This needs to be fixed before the demo today.

---

## The Problem

The Mermaid.js diagrams in the architecture HTML document have two types of boxes:

1. **Node labels** (e.g., "Azure Blob Storage", "Claude Opus 4.6", "FastAPI Application Server") - These render correctly with solid colored backgrounds, proper borders, and text that fits inside the boxes.

2. **Edge labels** (e.g., "Exported XML", "Deploy configs", "Opus calls", "Source files") - These have a DOUBLE BORDER problem. There is an inner border and an outer border visible, making them look broken compared to the node labels.

The node labels work perfectly. The edge labels need to look exactly the same way: single solid fill, single border, no double border, no transparency.

## What Has Been Tried (And Failed)

- Adding CSS `.mermaid .edgeLabel rect` overrides with `!important` flags - causes double border
- Adding the same CSS without `!important` - still causes double border
- Removing all CSS and relying only on `edgeLabelBackground` in the Mermaid theme config - makes the labels semi-transparent with no border
- Adding `opacity: 1` to the CSS rule - still double border

The root cause appears to be that Mermaid renders edge labels with TWO nested rect elements (or a rect plus a background), and any CSS targeting `.edgeLabel rect` styles both of them, producing the double border effect.

## What Works (Node Labels)

Node labels use the markdown string syntax in the Mermaid diagram definition:

```
BLOB["`**Azure Blob Storage**
Source Artifacts + Pipeline Outputs`"]
```

They are then styled with inline Mermaid `style` declarations at the bottom of the diagram:

```
style BLOB fill:#ccfbf1,stroke:#0d9488,stroke-width:2px,color:#134e4a
```

This produces a single solid box with one border. No CSS overrides needed.

## What Needs to Happen

Figure out how Mermaid renders edge label boxes internally (inspect the SVG output in browser dev tools) and apply styling that produces a single solid box with a single border, matching the appearance of the node labels. The edge labels currently use markdown string syntax:

```
DS -.->|"`Exported XML`"| BLOB
```

The desired appearance:
- Solid `#ede9fe` background (no transparency)
- Single `#7c3aed` border at 1.5px
- Rounded corners (rx 6)
- Text fits inside the box with proper padding
- No double border

## Current Mermaid Config

```javascript
mermaid.initialize({
  startOnLoad: false,
  theme: 'base',
  themeVariables: {
    edgeLabelBackground: '#ede9fe',
    fontSize: '14px',
    fontFamily: 'Inter, sans-serif'
    // ... other theme vars
  },
  flowchart: {
    htmlLabels: false,
    useMaxWidth: false,
    padding: 20
  }
});
```

## Approach Suggestion

Open the rendered page in a browser, inspect one of the working node label boxes in dev tools, then inspect one of the broken edge label boxes. Compare the SVG structure. The node labels likely have a single `<rect>` element. The edge labels likely have two overlapping elements. Once you see the actual SVG structure, you can write CSS that targets only the correct element, or find a different approach entirely.

**DO NOT make changes without the user's explicit approval.** Ask first, explain what you plan to do, and wait for "yes" before editing.

## Context

This is a client-facing architecture diagram for a Sephora demo happening today. The rest of the document (cover page, component cards, model allocation table, security section, portability section) is done and looks good. Only the Mermaid diagram edge labels need fixing.

The full session context is in:
- `sephora/edw_modernization/planning/master_plan_2026-04-02.md`
- `sephora/edw_modernization/planning/session_handoff_2026-04-02.md`
- `sephora/edw_modernization/planning/demo_prep_audience_alignment_2026-04-02.html`
- `sephora/edw_modernization/planning/demo_gap_analysis_2026-04-02.md`
- `sephora/edw_modernization/planning/post_demo_next_steps_strategy_2026-04-02.html`
- `sephora/edw_modernization/planning/demo_prep_maher_assessment_2026-04-02.html`
