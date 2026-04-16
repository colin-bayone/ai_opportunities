# Mermaid Shape and Feature Library

**Purpose:** Quick-reference menu of every shape, arrow, icon, and formatting option available in mermaid.js for use when designing diagrams. This is the "what can I use?" reference. For "how should I use it?" see `mermaid_design_standards.md`.

**Mermaid version:** v11+ (some shapes require v11.3+, noted below)

---

## Node Shapes

### Classic Shapes (All Versions)

| Shape | Syntax | Visual | Best For |
|-------|--------|--------|----------|
| Rectangle | `A["Text"]` | Square corners | General process steps, actions |
| Rounded | `A("Text")` | Rounded corners | Events, AI/ML components, soft processes |
| Stadium | `A(["Text"])` | Pill/capsule | Start/end terminals, entry/exit points |
| Subroutine | `A[["Text"]]` | Double vertical lines | Predefined processes, build tools, function calls |
| Cylinder | `A[("Text")]` | Database drum | Databases, data stores, storage, repositories |
| Circle | `A(("Text"))` | Circle | Connectors, junction points |
| Diamond | `A{"Text"}` | Diamond/rhombus | Decisions, verification, branching |
| Hexagon | `A{{"Text"}}` | Hexagon | Orchestrators, engines, central coordinators |
| Parallelogram | `A[/"Text"/]` | Slanted right | Input/output |
| Parallelogram reverse | `A[\"Text"\]` | Slanted left | Alternative input/output |
| Trapezoid | `A[/"Text"\]` | Wide top | Manual operations |
| Trapezoid reverse | `A[\"Text"/]` | Wide bottom | Alternative manual ops |
| Double circle | `A((("Text")))` | Double circle | Important connectors, emphasis |
| Asymmetric | `A>"Text"]` | Flag/banner | Flags, signals, events |

### New Shapes (v11.3+ — `@{shape:}` Syntax)

| Shape | Syntax | Visual | Best For |
|-------|--------|--------|----------|
| Document | `A@{ shape: doc, label: "Text" }` | Wavy bottom | Documents, reports |
| Multi-document | `A@{ shape: docs, label: "Text" }` | Stacked docs | Document collections |
| Card / Notched rect | `A@{ shape: notch-rect, label: "Text" }` | Notched corner | Cards, records |
| Lined rectangle | `A@{ shape: lin-rect, label: "Text" }` | Line on left | Annotated processes |
| Lined cylinder | `A@{ shape: lin-cyl, label: "Text" }` | Lined drum | Annotated storage |
| Small circle | `A@{ shape: sm-circ, label: "Text" }` | Small circle | Tiny connectors |
| Framed circle | `A@{ shape: fr-circ, label: "Text" }` | Framed circle | Important connectors |
| Fork/Join | `A@{ shape: fork, label: "Text" }` | Thick bar | Parallel fork/join points |
| Hourglass | `A@{ shape: hourglass, label: "Text" }` | Hourglass | Timing, collation |
| Lightning bolt | `A@{ shape: bolt, label: "Text" }` | Zigzag | Events, triggers, alerts |
| Triangle | `A@{ shape: tri, label: "Text" }` | Triangle up | Extract, merge |
| Flag | `A@{ shape: flag, label: "Text" }` | Flag | Milestones, markers |
| Delay | `A@{ shape: delay, label: "Text" }` | D-shape | Wait states, queues |
| Stacked rect | `A@{ shape: processes, label: "Text" }` | Stacked | Multi-process, batch ops |
| Window pane | `A@{ shape: win-pane, label: "Text" }` | 4-pane grid | Grouped items |
| Braces left | `A@{ shape: brace-l, label: "Text" }` | Left brace | Grouping marker |
| Braces right | `A@{ shape: brace-r, label: "Text" }` | Right brace | Grouping marker |
| Icon | `A@{ icon: "fa:fa-server", label: "Text" }` | Icon + label | Icon-prominent nodes |
| Image | `A@{ img: "url", label: "Text", w: 60, h: 60 }` | Image + label | Logo nodes |

---

## Arrow / Edge Types

### Line Styles

| Type | Syntax | Visual |
|------|--------|--------|
| Solid | `-->` | Standard arrow |
| Dotted | `-.->` | Dashed line arrow |
| Thick | `==>` | Bold arrow |
| Open (no arrow) | `---` | Line only |
| Dotted open | `-.-` | Dashed line only |
| Thick open | `===` | Bold line only |
| Invisible | `~~~` | No visible line (for spacing) |

### Arrowhead Variants

| Type | Syntax | Visual |
|------|--------|--------|
| Arrow | `-->` | Standard pointed |
| Circle end | `--o` | Circle terminator |
| Cross end | `--x` | X terminator |
| Bidirectional | `<-->` | Arrows both ends |
| Bi circle | `o--o` | Circles both ends |
| Bi cross | `x--x` | X's both ends |

### With Labels

| Syntax | Example |
|--------|---------|
| Pipe syntax | `A -->\|Label text\| B` |
| Inline | `A -- Label text --> B` |

### Edge Length Control

Extra dashes = longer edges:

| Length | Solid | Dotted | Thick |
|--------|-------|--------|-------|
| Normal | `-->` | `-.->` | `==>` |
| Long | `--->` | `-..->` | `===>` |
| Extra long | `---->` | `-...->` | `====>` |

---

## Text Formatting in Nodes

### With `htmlLabels: true` (Recommended for icons)

```
A["<b>Bold Title</b><br/>▸ Detail line 1<br/>▸ Detail line 2"]
```

- `<b>` for bold
- `<br/>` for line breaks
- HTML entities like `▸` `•` `◦` `→` for bullets
- `fa:fa-icon-name` for FontAwesome icons (renders as glyphs)

### With `htmlLabels: false` (Markdown mode)

```
A["`**Bold Title**
Detail line 1
Detail line 2`"]
```

- `**text**` for bold
- `_text_` for italic
- Literal newlines for line breaks
- Icons render as literal text (no glyph rendering)

**Trade-off:** You get icons OR markdown bold, not both in mermaid v10. Mermaid v11 with `htmlLabels: true` gives both via HTML `<b>` tags + `fa:` icons.

---

## Bullet Characters for Detail Lines

| Character | Code | Look | Best For |
|-----------|------|------|----------|
| ▸ | `▸` | Small right triangle | Clean, modern |
| • | `•` | Round bullet | Traditional |
| ◦ | `◦` | Open circle | Secondary items |
| → | `→` | Arrow | Flow/sequence items |
| ‣ | `‣` | Triangular bullet | Alternative to ▸ |
| – | `–` | En dash | Subtle separator |

---

## FontAwesome Icons (Require FA CSS Loaded)

### Common Icons for Architecture Diagrams

| Icon | Code | Use For |
|------|------|---------|
| fa:fa-server | `fa:fa-server` | Servers, hosts |
| fa:fa-database | `fa:fa-database` | Databases |
| fa:fa-hard-drive | `fa:fa-hard-drive` | Storage, NFS, disk |
| fa:fa-code-branch | `fa:fa-code-branch` | Repositories, version control |
| fa:fa-gears | `fa:fa-gears` | Orchestration, automation, CI/CD |
| fa:fa-hammer | `fa:fa-hammer` | Build tools |
| fa:fa-brain | `fa:fa-brain` | AI/ML, language models |
| fa:fa-microchip | `fa:fa-microchip` | ML models, processing |
| fa:fa-robot | `fa:fa-robot` | Automation, bots |
| fa:fa-file-code | `fa:fa-file-code` | Scripts, code files |
| fa:fa-circle-check | `fa:fa-circle-check` | Verification, approval |
| fa:fa-list-check | `fa:fa-list-check` | Checklists, rule-based |
| fa:fa-shield-halved | `fa:fa-shield-halved` | Security, governance |
| fa:fa-cloud | `fa:fa-cloud` | Cloud services |
| fa:fa-lock | `fa:fa-lock` | Security, encryption |
| fa:fa-chart-line | `fa:fa-chart-line` | Metrics, monitoring |
| fa:fa-bolt | `fa:fa-bolt` | Events, triggers |
| fa:fa-users | `fa:fa-users` | Teams, users |
| fa:fa-envelope | `fa:fa-envelope` | Email, notifications |
| fa:fa-plug | `fa:fa-plug` | Integrations, connectors |
| fa:fa-eye | `fa:fa-eye` | Observability, monitoring |
| fa:fa-clock | `fa:fa-clock` | Scheduling, timers |
| fa:fa-network-wired | `fa:fa-network-wired` | Networks, infrastructure |
| fa:fa-docker | `fab:fa-docker` | Docker containers |
| fa:fa-globe | `fa:fa-globe` | Web, external services |

---

## Subgraph / Cluster Options

```
subgraph ID["Label Text"]
    direction TB
    %% nodes go here
end
```

- `direction TB` or `direction LR` can override the parent graph direction within a subgraph
- Subgraphs can be nested (2-3 levels max recommended)
- Style with `style ID fill:#color,stroke:#color,stroke-width:2px,color:#textcolor`
- Labels support HTML when `htmlLabels: true` (e.g., `"<b>TITLE</b>"`)

---

## Styling with classDef

```
classDef className fill:#hex,stroke:#hex,stroke-width:1px,color:#hex
classDef dashed fill:#hex,stroke:#hex,stroke-width:1px,color:#hex,stroke-dasharray:5 5

%% Apply to node
A["Text"]:::className

%% Apply to multiple nodes
class A,B,C className
```

### Supported CSS Properties in classDef

| Property | Example | Effect |
|----------|---------|--------|
| fill | `fill:#eff6ff` | Node background color |
| stroke | `stroke:#2563eb` | Border color |
| stroke-width | `stroke-width:2px` | Border thickness |
| stroke-dasharray | `stroke-dasharray:5 5` | Dashed border |
| color | `color:#1e3a5f` | Text color |
| rx | `rx:8` | Corner radius (rounded corners) |

---

## Edge Styling

```
%% Style by link index (0-based)
linkStyle 0 stroke:#ff0000,stroke-width:2px

%% Style default links
linkStyle default stroke:#2563eb,stroke-width:1px
```

---

## Diagram Types Beyond Flowcharts

| Type | Keyword | Best For |
|------|---------|----------|
| Sequence | `sequenceDiagram` | API calls, message flows, protocol exchanges |
| Class | `classDiagram` | Object models, class hierarchies |
| State | `stateDiagram-v2` | State machines, lifecycle workflows |
| ER | `erDiagram` | Database schemas, entity relationships |
| Gantt | `gantt` | Timelines, project schedules |
| Pie | `pie` | Proportional breakdowns |
| Mindmap | `mindmap` | Brainstorming, topic hierarchies |
| Timeline | `timeline` | Historical progression, milestones |
| Architecture | `architecture-beta` | System architecture with icons (v11.1+) |
| Kanban | `kanban` | Task boards, workflow stages |
| Git graph | `gitGraph` | Branch/merge visualization |
| Block | `block-beta` | Block diagrams, column layouts |
| C4 | `C4Context` | C4 architecture model |

---

## Post-Render Techniques (JavaScript)

### Move Cluster Labels on Top of Edges

SVG renders in DOM order. Cluster labels render before edges, so arrows cut through titles. Fix: clone labels to end of SVG after rendering.

```javascript
// After mermaid.run(), move cluster labels to end of SVG
const svg = document.querySelector('.mermaid svg');
document.querySelectorAll('.cluster-label').forEach(label => {
    const fo = label.querySelector('foreignObject');
    if (fo) {
        const g = document.createElementNS('http://www.w3.org/2000/svg', 'g');
        // Add opaque background rect matching parent cluster border color
        // Clone foreignObject into new group
        // Append group to end of SVG
        // Hide original label
    }
});
```

See `v5_mermaid11_icons.html` in `claude/2026-04-13_mermaid_research/diagrams/` for the complete working implementation.

---

## Quick Decision Guide

| I want to... | Use... |
|-------------|--------|
| Show a database | Cylinder: `A[("Label")]` |
| Show a decision point | Diamond: `A{"Label"}` |
| Show an orchestrator/engine | Hexagon: `A{{"Label"}}` |
| Show a build tool or subprocess | Subroutine: `A[["Label"]]` |
| Show an AI/ML component | Rounded: `A("Label")` with purple classDef |
| Show something deprecated | Any shape + classDef with `stroke-dasharray:5 5` |
| Show a proposed/future flow | Dashed arrow: `-.->` |
| Show the primary path | Thick arrow: `==>` |
| Add an icon | `fa:fa-icon-name` in label text (requires `htmlLabels: true`) |
| Add bullet points | `▸` character before each detail line |
| Make title bold | `<b>Title</b>` with `htmlLabels: true` |
| Group related nodes | `subgraph ID["Label"]...end` |
| Color-code by category | `classDef` with semantic colors from `mermaid_design_standards.md` |
