# Mermaid.js Node Shapes, Arrow Types, and Edge Formatting -- Comprehensive Reference

**Source:** Official mermaid.js documentation + web research
**Date:** 2026-04-13
**Focus:** Every node shape, arrow type, and edge formatting option

---

## Table of Contents

1. [Flowchart Direction](#1-flowchart-direction)
2. [Classic Node Shapes (Bracket Syntax)](#2-classic-node-shapes-bracket-syntax)
3. [New Node Shapes -- v11.3+ @{shape:} Syntax](#3-new-node-shapes----v113-shape-syntax)
4. [Special Shapes: Icon and Image](#4-special-shapes-icon-and-image)
5. [Arrow / Edge Types](#5-arrow--edge-types)
6. [Edge Length Control](#6-edge-length-control)
7. [Edge Labels (Text on Arrows)](#7-edge-labels-text-on-arrows)
8. [Edge IDs and Animation](#8-edge-ids-and-animation)
9. [Markdown in Nodes](#9-markdown-in-nodes)
10. [Node Styling with classDef](#10-node-styling-with-classdef)
11. [Subgraph Syntax](#11-subgraph-syntax)
12. [Source URLs](#12-source-urls)

---

## 1. Flowchart Direction

Every mermaid flowchart begins with `flowchart` followed by a direction code:

| Code | Direction |
|------|-----------|
| `TB` or `TD` | Top to Bottom (default) |
| `BT` | Bottom to Top |
| `LR` | Left to Right |
| `RL` | Right to Left |

```
flowchart LR
    A --> B
```

---

## 2. Classic Node Shapes (Bracket Syntax)

These are the original shapes available since early mermaid versions. The bracket characters surrounding the label text determine the shape.

### 2.1 Rectangle (Process)

```
A[This is a rectangle]
```

- **Visual:** Standard rectangle with square corners
- **Use:** General process steps, actions, operations
- **Default shape** if no brackets specified (just `A` alone renders as rectangle with ID as label)

### 2.2 Rounded Rectangle (Event)

```
A(This is rounded)
```

- **Visual:** Rectangle with rounded corners
- **Use:** Events, alternate processes, softer visual for general steps

### 2.3 Stadium Shape (Terminal)

```
A([This is a stadium])
```

- **Visual:** Rectangle with fully rounded (semicircular) left and right edges, like a stadium or pill
- **Use:** Start/end terminals, entry/exit points

### 2.4 Subroutine Shape (Subprocess)

```
A[[This is a subroutine]]
```

- **Visual:** Rectangle with double vertical lines on left and right edges
- **Use:** Predefined processes, subroutines, function calls

### 2.5 Cylindrical Shape (Database)

```
A[(This is a database)]
```

- **Visual:** Cylinder (like a database drum)
- **Use:** Databases, data stores, persistent storage

### 2.6 Circle

```
A((This is a circle))
```

- **Visual:** Circle
- **Use:** Connectors, start/end points, junction points

### 2.7 Asymmetric Shape (Flag/Banner)

```
A>This is asymmetric]
```

- **Visual:** Rectangle with a pointed left edge (like a flag or banner pointing right)
- **Use:** Off-page connectors, signals, flags
- **Note:** Only one bracket style -- `>` on left, `]` on right

### 2.8 Rhombus / Diamond (Decision)

```
A{This is a decision}
```

- **Visual:** Diamond/rhombus rotated 45 degrees
- **Use:** Decision points, conditionals, branching logic (yes/no, true/false)

### 2.9 Hexagon (Preparation)

```
A{{This is a hexagon}}
```

- **Visual:** Regular hexagon (six sides)
- **Use:** Preparation steps, initialization, setup operations

### 2.10 Parallelogram (Data / Input-Output)

```
A[/This is a parallelogram/]
```

- **Visual:** Parallelogram leaning right
- **Use:** Input/output operations, data flow

### 2.11 Parallelogram Alternate (Data Alternate)

```
A[\This is a parallelogram alt\]
```

- **Visual:** Parallelogram leaning left (mirror of the standard parallelogram)
- **Use:** Alternate input/output representation

### 2.12 Trapezoid (Manual Operation)

```
A[/This is a trapezoid\]
```

- **Visual:** Trapezoid wider at the bottom, narrower at the top
- **Use:** Manual operations, manual processing steps

### 2.13 Trapezoid Alternate (Priority)

```
A[\This is a trapezoid alt/]
```

- **Visual:** Trapezoid wider at the top, narrower at the bottom (inverted)
- **Use:** Priority steps, alternate manual operations

### 2.14 Double Circle

```
A(((This is a double circle)))
```

- **Visual:** Circle with a second concentric circle around it
- **Use:** End states (especially in state diagrams), final/accept states

### Classic Shapes Quick Reference Table

| Shape | Syntax | Brackets |
|-------|--------|----------|
| Rectangle | `A[text]` | `[ ]` |
| Rounded rect | `A(text)` | `( )` |
| Stadium/Pill | `A([text])` | `([ ])` |
| Subroutine | `A[[text]]` | `[[ ]]` |
| Cylinder/DB | `A[(text)]` | `[( )]` |
| Circle | `A((text))` | `(( ))` |
| Asymmetric | `A>text]` | `> ]` |
| Diamond | `A{text}` | `{ }` |
| Hexagon | `A{{text}}` | `{{ }}` |
| Parallelogram | `A[/text/]` | `[/ /]` |
| Parallelogram alt | `A[\text\]` | `[\ \]` |
| Trapezoid | `A[/text\]` | `[/ \]` |
| Trapezoid alt | `A[\text/]` | `[\ /]` |
| Double circle | `A(((text)))` | `((( )))` |

---

## 3. New Node Shapes -- v11.3+ @{shape:} Syntax

Starting with mermaid v11.3.0 (released late 2024), a new general syntax was introduced to support the growing number of shapes. This uses a JavaScript-object-like notation:

```
ID@{ shape: shape-name, label: "Label text" }
```

If you omit the label, the node ID is used as the label. Example:

```
flowchart LR
    A@{ shape: rect, label: "Process Step" }
    B@{ shape: diam, label: "Decision?" }
    A --> B
```

### Complete Shape Reference Table (v11.3+)

Below is the comprehensive list of all shapes available via the `@{shape:}` syntax, including the 30 new shapes introduced alongside the existing ones. Each shape has a **semantic name** (its meaning in flowchart standards), a **short name** (used in `shape:` syntax), and may have **aliases**.

#### Existing Shapes (with new @{} syntax equivalents)

| Semantic Name | Short Name | Aliases | Classic Syntax | Visual Description |
|---------------|------------|---------|----------------|--------------------|
| Process | `rect` | `rectangle`, `process` | `A[text]` | Standard rectangle |
| Event | `rounded` | `event` | `A(text)` | Rounded rectangle |
| Terminal / Start-Stop | `stadium` | `terminal`, `pill` | `A([text])` | Stadium / pill shape |
| Subprocess | `subroutine` | `subprocess`, `fr-rect`, `framed-rectangle` | `A[[text]]` | Double-bordered rectangle |
| Database | `cyl` | `cylinder`, `db`, `database` | `A[(text)]` | Cylinder |
| Circle | `circle` | `circ` | `A((text))` | Circle |
| Asymmetric | `odd` | `asymmetric` | `A>text]` | Flag/banner shape |
| Decision | `diam` | `diamond`, `decision` | `A{text}` | Diamond / rhombus |
| Prepare | `hex` | `hexagon`, `prepare` | `A{{text}}` | Hexagon |
| Data (IO) | `lean-r` | `lean-right`, `in-out` | `A[/text/]` | Right-leaning parallelogram |
| Data (IO alt) | `lean-l` | `lean-left`, `out-in` | `A[\text\]` | Left-leaning parallelogram |
| Manual Operation | `trap-t` | `trapezoid-top`, `manual` | `A[/text\]` | Trapezoid (wider at bottom) |
| Priority | `trap-b` | `trapezoid-bottom`, `priority` | `A[\text/]` | Inverted trapezoid (wider at top) |
| Double Circle | `dbl-circ` | `double-circle` | `A(((text)))` | Double concentric circle |

#### New Shapes (v11.3+ only -- no classic bracket equivalent)

| Semantic Name | Short Name | Aliases | Visual Description | When to Use |
|---------------|------------|---------|--------------------|----|
| Card / Notched Rectangle | `notch-rect` | `card`, `notched-rectangle` | Rectangle with a notch (clipped corner) at top-left, like a punched card | Data cards, physical records, card-based input |
| Lined / Ruled Process | `lin-rect` | `lined-rectangle`, `lined-process`, `lin-proc` | Rectangle with a vertical line near the left edge (like a ruled margin) | Predefined or lined processes, documented steps |
| Start (Small Circle) | `sm-circ` | `small-circle`, `start` | Small filled or outlined circle | Start points, initial states |
| Stop (Framed Circle) | `fr-circ` | `framed-circle`, `stop` | Circle with a frame/border (bullseye style) | End points, final/stop states |
| Fork / Join | `fork` | `join` | Solid horizontal or vertical bar | Parallel process fork/join points (like UML activity diagrams) |
| Collate / Hourglass | `hourglass` | `collate` | Hourglass shape (two triangles meeting at points) | Collation, merging/sorting operations |
| Comment (Right Brace) | `brace-r` | `brace-right`, `comment` | Right curly brace `}` shape | Comments, annotations |
| Comment (Left Brace) | `brace-l` | `brace-left` | Left curly brace `{` shape | Comments, annotations (left side) |
| Braces | `braces` | -- | Both left and right curly braces `{ }` | Paired comments, grouping annotations |
| Communication Link / Lightning | `bolt` | `com-link`, `lightning-bolt` | Lightning bolt shape | Communication links, signals, electrical connections |
| Document | `doc` | `document` | Rectangle with a wavy bottom edge | Documents, reports, printouts |
| Multi-Document | `docs` | `documents`, `st-doc`, `stacked-document` | Stacked documents (document with shadow copies behind) | Multiple documents, file collections |
| Lined Document | `lin-doc` | `lined-document` | Document shape with a ruled line | Formal/lined documents |
| Tagged Document | `notch-pent` | `notched-pentagon`, `tag-doc`, `tagged-document` | Pentagon with a notch, like a document with a tag/bookmark | Tagged or categorized documents |
| Stored Data (Horizontal Cylinder) | `h-cyl` | `horizontal-cylinder`, `das`, `stored-data` | Cylinder on its side (horizontal) | Direct access storage, hard drives |
| Disk Storage (Lined Cylinder) | `lin-cyl` | `lined-cylinder`, `disk` | Cylinder with horizontal lines | Disk storage, sequential access |
| Display (Curved Trapezoid) | `curv-trap` | `curved-trapezoid`, `display` | Trapezoid with one curved side | Display output, screen/monitor |
| Divided Process / Divided Rectangle | `div-rect` | `divided-rectangle`, `div-proc`, `divided-process` | Rectangle divided horizontally into sections | Multi-part processes, divided operations |
| Extract / Triangle | `tri` | `triangle`, `extract` | Upward-pointing triangle | Extract operations, convergence points |
| Manual File / Inverted Triangle | `flip-tri` | `flipped-triangle`, `manual-file` | Downward-pointing triangle (inverted) | Manual file operations, manual sorting |
| Flag / Internal Storage | `flag` | -- | Flag shape (rectangle with triangular right edge) | Flags, signals, internal storage indicators |
| Internal Storage / Window Pane | `win-pane` | `window-pane`, `internal-storage` | Rectangle divided into four quadrants (like a window) | Internal storage, memory, registers |
| Junction / Filled Circle | `f-circ` | `filled-circle`, `junction` | Solid filled circle | Junction points, connection nodes |
| Delay (Half-Rounded Rectangle) | `delay` | `half-rounded-rectangle` | Rectangle with one rounded right side (D-shape) | Delays, wait states, buffers |
| Loop Limit / Notched Pentagon | `notch-pent` | `notched-pentagon`, `loop-limit` | Pentagon with a flat top and notch | Loop limits, iteration boundaries |
| Manual Input / Sloped Rectangle | `sl-rect` | `sloped-rectangle`, `manual-input` | Rectangle with a sloped top edge | Manual input, keyboard entry |
| Multi-Process / Stacked Rectangle | `st-rect` | `stacked-rectangle`, `multi-process`, `procs` | Rectangle with shadow/stacked copies behind | Multiple processes, batch operations |
| Odd Shape | `odd` | `asymmetric` | Flag/banner pointing right | Off-page references, connectors |
| Summary / Crossed Circle | `cross-circ` | `crossed-circle`, `summary` | Circle with an X through it | Summary points, cross-reference |
| Tagged Process / Braces around rect | `tag-rect` | `tagged-rectangle`, `tag-proc`, `tagged-process` | Rectangle with a tag indicator | Tagged or labeled process steps |
| Text Block | `text` | -- | Plain text with no border/shape | Annotations, free-floating labels |

> **Note on aliases:** Most shapes accept multiple name variants. For example, `shape: card` is equivalent to `shape: notch-rect`. Use whichever is most readable for your context.

### Example Using New Shapes

```
flowchart TD
    start@{ shape: sm-circ, label: "Begin" }
    input@{ shape: sl-rect, label: "Enter Data" }
    process@{ shape: lin-rect, label: "Process Record" }
    decision@{ shape: diam, label: "Valid?" }
    doc@{ shape: doc, label: "Generate Report" }
    db@{ shape: cyl, label: "Save to DB" }
    stop@{ shape: fr-circ, label: "End" }

    start --> input --> process --> decision
    decision -->|Yes| doc --> db --> stop
    decision -->|No| input
```

---

## 4. Special Shapes: Icon and Image

Mermaid v11.3+ also introduces two special non-geometric shapes:

### Icon Shape

```
A@{ shape: icon, icon: "fa:fa-database", label: "Database" }
```

- Renders a Font Awesome (or other supported icon set) icon as the node
- Useful for visual context without geometric shapes

### Image Shape

```
A@{ shape: image, img: "https://example.com/logo.png", label: "Logo", w: 60, h: 60 }
```

- Renders an image as the node
- Supports width (`w`) and height (`h`) parameters

---

## 5. Arrow / Edge Types

Mermaid supports a rich set of edge/arrow types. Edges are formed by combining three properties:
1. **Line style:** solid, dotted, or thick
2. **Arrowhead:** none, arrow (triangle), circle, or cross
3. **Direction:** one-way or bidirectional

### 5.1 Basic Link Types

#### Solid Lines

| Syntax | Description |
|--------|-------------|
| `A --- B` | Solid line, no arrowhead (open link) |
| `A --> B` | Solid line with arrow |
| `A --o B` | Solid line with circle end |
| `A --x B` | Solid line with cross end |

#### Dotted Lines

| Syntax | Description |
|--------|-------------|
| `A -.- B` | Dotted line, no arrowhead |
| `A -.-> B` | Dotted line with arrow |
| `A -.-o B` | Dotted line with circle end |
| `A -.-x B` | Dotted line with cross end |

#### Thick Lines

| Syntax | Description |
|--------|-------------|
| `A === B` | Thick line, no arrowhead |
| `A ==> B` | Thick line with arrow |
| `A ==o B` | Thick line with circle end |
| `A ==x B` | Thick line with cross end |

### 5.2 Bidirectional / Multi-Directional Arrows

Mermaid supports multidirectional arrows by placing arrowhead markers on both ends:

| Syntax | Description |
|--------|-------------|
| `A <--> B` | Solid bidirectional arrow |
| `A <-.-> B` | Dotted bidirectional arrow |
| `A <==> B` | Thick bidirectional arrow |
| `A o--o B` | Solid line with circles on both ends |
| `A x--x B` | Solid line with crosses on both ends |

### 5.3 Invisible Links

```
A ~~~ B
```

- Creates an invisible link (no visible line or arrow)
- Useful for controlling layout/spacing without visible connections

### 5.4 Complete Arrow Type Matrix

| Line Style | No Head | Arrow | Circle | Cross |
|------------|---------|-------|--------|-------|
| **Solid** | `---` | `-->` | `--o` | `--x` |
| **Dotted** | `-.-` | `-.->` | `-.-o` | `-.-x` |
| **Thick** | `===` | `==>` | `==o` | `==x` |

For bidirectional, mirror the marker on the left side:

| Line Style | Bi-Arrow | Bi-Circle | Bi-Cross |
|------------|----------|-----------|----------|
| **Solid** | `<-->` | `o--o` | `x--x` |
| **Dotted** | `<-.->` | `o-.-o` | `x-.-x` |
| **Thick** | `<==>` | `o==o` | `x==x` |

### 5.5 Important Note on `o` and `x`

If a node ID starts with `o` or `x`, mermaid may interpret it as a circle or cross marker. To avoid this:
- Add a space before the letter: `A --> o_node` should be `A --> oNode` (capitalize) or use quotes
- Or define the node first: `oNode[My Node]` then reference it

---

## 6. Edge Length Control

You can suggest longer edges by adding extra characters to the link syntax. Each extra dash/dot/equals adds approximately one rank of spacing.

### Solid Lines -- Length Control

| Length | Link | Arrow | Circle | Cross |
|--------|------|-------|--------|-------|
| Normal (1) | `---` | `-->` | `--o` | `--x` |
| Extended (2) | `----` | `--->` | `---o` | `---x` |
| Extended (3) | `-----` | `---->` | `----o` | `----x` |

### Dotted Lines -- Length Control

| Length | Link | Arrow | Circle | Cross |
|--------|------|-------|--------|-------|
| Normal (1) | `-.-` | `-.->` | `-.-o` | `-.-x` |
| Extended (2) | `-..-` | `-..->` | `-..-o` | `-..-x` |
| Extended (3) | `-...-` | `-...->` | `-...-o` | `-...-x` |

### Thick Lines -- Length Control

| Length | Link | Arrow | Circle | Cross |
|--------|------|-------|--------|-------|
| Normal (1) | `===` | `==>` | `==o` | `==x` |
| Extended (2) | `====` | `===>` | `===o` | `===x` |
| Extended (3) | `=====` | `====>` | `====o` | `====x` |

> **Important:** The rendering engine treats extra length as a *hint*, not a strict requirement. The actual rendered length may be adjusted to accommodate other layout constraints.

---

## 7. Edge Labels (Text on Arrows)

There are two syntaxes for adding text labels to edges:

### Pipe Syntax (preferred)

```
A -->|This is text| B
```

### Inline Syntax

```
A -- This is text --> B
```

Both produce the same result: centered text on the edge.

### Labels on Different Edge Types

```
A -->|solid arrow label| B
A -.->|dotted arrow label| C
A ==>|thick arrow label| D
A ---|open link label| E
```

### Labels with Extended Length

When using the label in the middle of the link, extra dashes go on the **right side**:

```
A -- text ---> B
```

(The extra dash is after "text", extending the link on the right.)

---

## 8. Edge IDs and Animation

### Edge IDs (v11+)

You can assign IDs to edges by prepending the edge syntax with the ID followed by `@`:

```
flowchart LR
    A e1@--> B
    B e2@-.-> C
    C e3@==> D
```

This creates edges with IDs `e1`, `e2`, and `e3`, which can then be targeted for styling and animation.

### Edge Animation with classDef

```
flowchart LR
    A e1@--> B
    B e2@--> C

    classDef animate stroke-dasharray: 9\,5,stroke-dashoffset: 900,animation: dash 25s linear infinite;
    class e1 animate
```

> **Important:** Commas within property values (like `stroke-dasharray: 9,5`) must be escaped with a backslash `\,` because commas are used as delimiters in mermaid classDef syntax.

### Built-in Animation Speeds

Mermaid supports shorthand animation speeds:

```
flowchart LR
    A e1@--> B
    class e1 fast
```

Two built-in speeds: `fast` and `slow`.

---

## 9. Markdown in Nodes

Mermaid supports **Markdown Strings** for rich text formatting inside node labels. To use markdown, wrap the label in double quotes and backticks:

### Syntax

```
A["`**Bold text** and *italic text*`"]
```

The pattern is: `"` + `` ` `` + markdown content + `` ` `` + `"`

### Supported Formatting

| Formatting | Syntax | Example |
|------------|--------|---------|
| Bold | `**text**` | `"`\``**Bold label**`\``"` |
| Italic | `*text*` | `"`\``*Italic label*`\``"` |
| Bold + Italic | `***text***` | `"`\``***Bold italic***`\``"` |
| Line break | Newline character | (literal newline in the string) |

### Full Example

```
flowchart TD
    A["`**Step 1**
    This is the first step
    with *automatic wrapping*`"]
    B["`**Step 2**
    - Item one
    - Item two
    - *Item three*`"]
    A --> B
```

### Key Features of Markdown Strings

- **Automatic text wrapping:** Text wraps when it becomes too long for the node
- **Newline support:** Use actual newline characters instead of `<br>` tags
- **Works in:** Node labels, edge labels, and subgraph labels
- **Limitation:** Only bold and italic are supported. Code blocks (backtick-enclosed code) within markdown strings are not supported in the standard way

---

## 10. Node Styling with classDef

Define reusable styles and apply them to nodes:

```
flowchart LR
    A[Process]:::highlight --> B[Decision]:::warning

    classDef highlight fill:#f9f,stroke:#333,stroke-width:2px
    classDef warning fill:#ff0,stroke:#f00,stroke-width:4px
```

### Inline Style

Apply styles directly to a node:

```
style A fill:#f9f,stroke:#333,stroke-width:2px
```

### Styling Edges by Index

Edges can be styled by their order of appearance (0-indexed):

```
flowchart LR
    A --> B --> C
    linkStyle 0 stroke:#ff3,stroke-width:4px
    linkStyle 1 stroke:#00f,stroke-width:2px,stroke-dasharray: 5 5
```

---

## 11. Subgraph Syntax

Subgraphs group nodes visually:

```
flowchart TB
    subgraph GroupName["Display Label"]
        direction LR
        A --> B
    end
    C --> A
```

- Subgraphs can be nested
- The `direction` keyword inside a subgraph overrides the parent flowchart direction
- Edges can connect to/from subgraphs themselves (not just nodes within them)

---

## 12. Source URLs

### Official Documentation
- [Mermaid.js Flowchart Syntax (Official)](https://mermaid.js.org/syntax/flowchart.html) -- Primary reference for all shapes, edges, and features
- [Mermaid Chart Documentation -- Flowcharts](https://docs.mermaidchart.com/mermaid-oss/syntax/flowchart.html) -- Mirror of official docs with additional examples
- [Mermaid Flowchart Shapes Page](https://docs.mermaidchart.com/mermaid/flowchart/shapes) -- Dedicated shapes reference
- [Mermaid Diagram Syntax Reference](https://mermaid.js.org/intro/syntax-reference.html) -- General syntax overview

### Blog and Announcements
- [Expanding the Horizons of Mermaid Flowcharts: Introducing 30 New Shapes!](https://docs.mermaidchart.com/blog/posts/expanding-the-horizons-of-mermaid-flowcharts-introducing-30-new-shapes) -- Announcement of the 30 new shapes
- [Adding Animations to Flowchart Edges (PR #6136)](https://github.com/mermaid-js/mermaid/pull/6136) -- Edge animation feature

### GitHub Source
- [Flowchart.md (source docs)](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/flowchart.md) -- Raw documentation source
- [Flowchart.md (built docs)](https://github.com/mermaid-js/mermaid/blob/develop/docs/syntax/flowchart.md) -- Built documentation
- [Custom SVG Shapes Library](https://mermaid.js.org/adding-new-shape.html) -- How to add custom shapes

### Community References
- [DeepWiki: Flowchart Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.1-flowchart-diagrams) -- Code-level analysis of flowchart implementation
- [Mastering Mermaid: Comprehensive Cheat Sheet (DEV Community)](https://dev.to/nagasuresh_dondapati_d5df/mastering-mermaid-a-comprehensive-cheat-sheet-45mi) -- Community cheat sheet
- [Mermaid Cheat Sheet (jojozhuang)](https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/) -- Quick reference
- [Mermaid.js Tutorial: Flowcharts, Sequence Diagrams & Syntax Guide (2026)](https://blog.starmorph.com/blog/mermaid-js-tutorial) -- Updated tutorial
- [FoggyBalrog MermaidDotNet Flowchart Docs](https://foggybalrog.github.io/MermaidDotNet/diagrams/flowchart.html) -- .NET wrapper with shape documentation
- [Mermaid Flowchart (ITOHI)](https://itohi.com/snippets/diagrams/mermaid-flowchart/) -- Practical snippet examples
- [FreeCodeCamp: How to Use Mermaid.js](https://www.freecodecamp.org/news/use-mermaid-javascript-library-to-create-flowcharts/) -- Introductory guide
- [Mermaid Live Editor](https://mermaid.live/) -- Interactive playground for testing syntax

---

## Appendix A: Quick Syntax Cheat Sheet

### Nodes at a Glance

```
%% Classic bracket syntax
A[Rectangle]
B(Rounded)
C([Stadium])
D[[Subroutine]]
E[(Cylinder)]
F((Circle))
G>Asymmetric]
H{Diamond}
I{{Hexagon}}
J[/Parallelogram/]
K[\Parallelogram Alt\]
L[/Trapezoid\]
M[\Trapezoid Alt/]
N(((Double Circle)))

%% New @{} syntax (v11.3+)
O@{ shape: notch-rect, label: "Card" }
P@{ shape: doc, label: "Document" }
Q@{ shape: docs, label: "Multi-Doc" }
R@{ shape: sm-circ, label: "Start" }
S@{ shape: fr-circ, label: "Stop" }
T@{ shape: fork, label: "Fork" }
U@{ shape: hourglass, label: "Collate" }
V@{ shape: bolt, label: "Signal" }
W@{ shape: delay, label: "Wait" }
X@{ shape: sl-rect, label: "Manual Input" }
Y@{ shape: win-pane, label: "Internal Storage" }
Z@{ shape: curv-trap, label: "Display" }
```

### Edges at a Glance

```
A --> B           %% Solid arrow
A --- B           %% Solid line (no arrow)
A -.-> B          %% Dotted arrow
A -.- B           %% Dotted line
A ==> B           %% Thick arrow
A === B           %% Thick line
A --o B           %% Circle end
A --x B           %% Cross end
A <--> B          %% Bidirectional
A o--o B          %% Circles both ends
A x--x B          %% Crosses both ends
A ~~~ B           %% Invisible link
A -->|label| B    %% Arrow with label
A -- text --> B   %% Alternative label syntax
A --->  B         %% Extended length (+1 rank)
A ----> B         %% Extended length (+2 ranks)
```
