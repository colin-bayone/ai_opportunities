# Mermaid.js Diagram Types — Comprehensive Reference

**Source:** Official mermaid.js documentation + web research
**Date:** 2026-04-13
**Focus:** All supported diagram types with syntax, examples, and capabilities

---

## Table of Contents

1. [Flowchart](#1-flowchart)
2. [Sequence Diagram](#2-sequence-diagram)
3. [Class Diagram](#3-class-diagram)
4. [State Diagram](#4-state-diagram)
5. [Entity Relationship (ER) Diagram](#5-entity-relationship-er-diagram)
6. [User Journey Diagram](#6-user-journey-diagram)
7. [Gantt Chart](#7-gantt-chart)
8. [Pie Chart](#8-pie-chart)
9. [Quadrant Chart](#9-quadrant-chart)
10. [Requirement Diagram](#10-requirement-diagram)
11. [GitGraph Diagram](#11-gitgraph-diagram)
12. [Mindmap](#12-mindmap)
13. [Timeline](#13-timeline)
14. [Sankey Diagram](#14-sankey-diagram)
15. [XY Chart](#15-xy-chart)
16. [Block Diagram](#16-block-diagram)
17. [Architecture Diagram](#17-architecture-diagram)
18. [Kanban Diagram](#18-kanban-diagram)
19. [Packet Diagram](#19-packet-diagram)
20. [C4 Diagram](#20-c4-diagram)
21. [ZenUML (Alternative Sequence Diagram)](#21-zenuml-alternative-sequence-diagram)

---

## Version History Summary

| Diagram Type | Version Introduced | Status |
|---|---|---|
| Flowchart | v0.x (2014, original) | Stable |
| Sequence Diagram | v0.x (2014, original) | Stable |
| Class Diagram | Early versions | Stable |
| State Diagram | Early versions | Stable |
| ER Diagram | Early versions | Stable |
| User Journey | Early versions | Stable |
| Gantt Chart | Early versions | Stable |
| Pie Chart | Early versions | Stable |
| Requirement Diagram | v8.x | Stable |
| GitGraph | v8.x | Stable |
| Mindmap | v9.3.0 | Stable |
| Timeline | v9.3.0 | Stable |
| Quadrant Chart | v10.x | Stable |
| Sankey | v10.3.0+ | Beta (`sankey-beta`) |
| ZenUML | v10.x | Stable (external plugin) |
| XY Chart | v10.x / v11.0.0 | Stable |
| Block Diagram | v11.0.0+ | Beta (`block-beta`) |
| Packet Diagram | v11.0.0+ | Beta (`packet-beta`) |
| Architecture | v11.1.0+ | Beta (`architecture-beta`) |
| Kanban | v11.4.0+ | Beta (`kanban`) |
| C4 Diagram | v9.x | Experimental |

**Sources:**
- [Mermaid Releases on GitHub](https://github.com/mermaid-js/mermaid/releases)
- [Mermaid v10.0.0 Release](https://github.com/mermaid-js/mermaid/releases/tag/v10.0.0)
- [Mermaid v11.0.0 Release](https://github.com/mermaid-js/mermaid/releases/tag/v11.0.0)
- [Mermaid 11.4 Kanban Release](https://docs.mermaidchart.com/blog/posts/mermaid-11-4-is-out-new-features-and-kanban-diagramming)
- [History of Mermaid.js (Taskade)](https://www.taskade.com/blog/history-of-mermaid)

---

## 1. Flowchart

**Keyword:** `flowchart` or `graph`
**When to use:** Process flows, decision trees, workflows, system logic, any box-and-arrow diagram.
**Documentation:** https://mermaid.js.org/syntax/flowchart.html

### Direction Options

| Keyword | Direction |
|---|---|
| `TB` or `TD` | Top to Bottom (default) |
| `BT` | Bottom to Top |
| `LR` | Left to Right |
| `RL` | Right to Left |

```
flowchart LR
    A --> B --> C
```

### Classic Node Shapes

| Shape | Syntax | Description |
|---|---|---|
| Rectangle | `A[Text]` | Standard process |
| Round edges | `A(Text)` | Rounded rectangle |
| Stadium | `A([Text])` | Pill/stadium shape |
| Subroutine | `A[[Text]]` | Subroutine/predefined process |
| Cylindrical | `A[(Text)]` | Database/cylinder |
| Circle | `A((Text))` | Circle |
| Asymmetric / Flag | `A>Text]` | Flag shape |
| Rhombus / Diamond | `A{Text}` | Decision |
| Hexagon | `A{{Text}}` | Preparation |
| Parallelogram | `A[/Text/]` | Input/Output |
| Parallelogram alt | `A[\Text\]` | Alternate parallelogram |
| Trapezoid | `A[/Text\]` | Manual operation |
| Trapezoid alt | `A[\Text/]` | Alternate trapezoid |
| Double Circle | `A(((Text)))` | Double circle |

### New General Shape Syntax (v11.3.0+, 30 New Shapes)

Mermaid v11.3.0 introduced a general syntax for defining shape types using `@{ shape: <shapeName> }`. This allows access to 30+ additional shapes with semantic meanings:

```
flowchart LR
    A@{ shape: notch-rect, label: "Notched Rectangle" }
    B@{ shape: lined-cylinder, label: "Lined Cylinder" }
    C@{ shape: sm-circ, label: "Small Circle" }
```

Key new shapes include (representative, not exhaustive):

| Shape Name | Semantic Meaning |
|---|---|
| `rect` | Rectangle / Process |
| `rounded` | Rounded rectangle / Event |
| `stadium` | Terminal point |
| `subproc` | Subprocess |
| `cyl` | Cylinder / Database |
| `diam` | Diamond / Decision |
| `hex` | Hexagon / Preparation |
| `lean-r` | Lean right / Input |
| `lean-l` | Lean left / Output |
| `trap-b` | Trapezoid bottom / Manual operation |
| `trap-t` | Trapezoid top |
| `dbl-circ` | Double circle |
| `notch-rect` | Notched rectangle |
| `lined-rect` | Lined rectangle |
| `sm-circ` | Small circle |
| `framed-circle` | Framed circle |
| `fork` | Fork / Join |
| `hourglass` | Hourglass / Collate |
| `bolt` | Lightning bolt |
| `com` | Communication link |
| `brace` | Brace notation |
| `brace-r` | Right brace |
| `braces` | Double braces |
| `lined-cyl` | Lined cylinder |
| `notch-pent` | Notched pentagon |
| `flag` | Flag shape |
| `bow-rect` | Bow-tie rectangle |
| `cross-circ` | Cross in circle |
| `tag-rect` | Tagged rectangle |
| `tag-doc` | Tagged document |
| `docs` | Multi-document |
| `win-pane` | Window pane |
| `tri` | Triangle |
| `curv-trap` | Curved trapezoid |
| `doc` | Document |
| `odd` | Odd shape |

**Source:** [Expanding the Horizons of Mermaid Flowcharts: Introducing 30 New Shapes](https://docs.mermaidchart.com/blog/posts/expanding-the-horizons-of-mermaid-flowcharts-introducing-30-new-shapes)

### Arrow / Edge Types

| Syntax | Description |
|---|---|
| `A --> B` | Arrow (solid line, arrowhead) |
| `A --- B` | Link (solid line, no arrowhead) |
| `A -.- B` | Dotted link (no arrowhead) |
| `A -.-> B` | Dotted arrow |
| `A ==> B` | Thick arrow |
| `A === B` | Thick link (no arrowhead) |
| `A --o B` | Circle endpoint |
| `A --x B` | Cross endpoint |
| `A o--o B` | Circle on both ends |
| `A x--x B` | Cross on both ends |
| `A <--> B` | Bidirectional arrow |

### Edge Labels

```
A -->|text| B
A -- text --> B
A -.->|text| B
A ==>|text| B
```

### Edge IDs (v11+)

Prepend the edge with an ID followed by `@`:

```
flowchart LR
    myEdge@A --> B
```

### Subgraphs

```
flowchart TB
    subgraph sub1 [Title for subgraph]
        direction LR
        A --> B
    end
    subgraph sub2 [Another subgraph]
        C --> D
    end
    sub1 --> sub2
```

- Subgraphs can set their own `direction`
- Subgraphs can be linked to/from other subgraphs or nodes
- If a subgraph's nodes link to external nodes, the subgraph inherits the parent direction

### Styling

```
flowchart LR
    A:::myClass --> B
    classDef myClass fill:#f9f,stroke:#333,stroke-width:2px
    classDef default fill:#fff,stroke:#333
    style A fill:#bbf,stroke:#f66,stroke-width:2px
```

### Click Interactions

```
flowchart LR
    A --> B
    click A "https://example.com" "Tooltip" _blank
    click B callback "Tooltip"
```

### Renderer Options

- **dagre** (default) -- standard renderer
- **elk** (v9.4+) -- better for larger/more complex diagrams

```
%%{init: {"flowchart": {"defaultRenderer": "elk"}} }%%
flowchart LR
    A --> B
```

### Special Syntax Notes

- The word `end` in all lowercase breaks flowcharts; capitalize it (`End`, `END`)
- `o` or `x` as the first letter after `---` creates circle/cross edges; add a space or capitalize

**Sources:**
- [Flowcharts Syntax | Mermaid](https://mermaid.js.org/syntax/flowchart.html)
- [Flowchart Shapes (test-docs)](https://test-docs.mermaidchart.com/mermaid/flowchart/shapes)
- [Flowchart Edges (test-docs)](https://test-docs.mermaidchart.com/mermaid/flowchart/edges)
- [DeepWiki: Flowchart Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.1-flowchart-diagrams)

---

## 2. Sequence Diagram

**Keyword:** `sequenceDiagram`
**When to use:** API interactions, protocol exchanges, system-to-system communication, method call sequences, any time-ordered interaction between actors.
**Documentation:** https://mermaid.js.org/syntax/sequenceDiagram.html

### Participants and Actors

```
sequenceDiagram
    participant A as Alice
    actor B as Bob
```

- `participant` renders as a box
- `actor` renders as a stick figure
- Participants appear in declaration order (or order of first appearance)

### Actor Grouping (Box)

```
sequenceDiagram
    box Purple Team Alpha
        participant A
        participant B
    end
    box rgb(100, 200, 150) Team Beta
        participant C
    end
```

### Message / Arrow Types

| Syntax | Line Style | Endpoint |
|---|---|---|
| `->` | Solid | No arrowhead (open) |
| `-->` | Dotted | No arrowhead (open) |
| `->>` | Solid | Arrowhead (filled) |
| `-->>` | Dotted | Arrowhead (filled) |
| `-x` | Solid | Cross (async/lost) |
| `--x` | Dotted | Cross |
| `-)` | Solid | Open arrow (async) |
| `--)` | Dotted | Open arrow (async) |

### Activation / Deactivation

```
sequenceDiagram
    Alice->>+John: Hello
    John-->>-Alice: Hi
```

- `+` after `>>` activates the target
- `-` after `>>` deactivates the target
- Explicit: `activate John` / `deactivate John`

### Create and Destroy

```
sequenceDiagram
    Alice->>Bob: Hello
    create participant Carl
    Alice->>Carl: Hi
    destroy Carl
    Carl->>Alice: Bye
```

### Notes

```
Note right of Alice: A note
Note left of Bob: Another note
Note over Alice,Bob: A note spanning both
```

### Control Flow Blocks

**Loop:**
```
loop Every minute
    Alice->>Bob: Ping
end
```

**Alt (If/Else):**
```
alt Condition A
    Alice->>Bob: Path A
else Condition B
    Alice->>Bob: Path B
else
    Alice->>Bob: Default
end
```

**Opt (Optional):**
```
opt Extra response
    Bob->>Alice: Thanks
end
```

**Par (Parallel):**
```
par Alice to Bob
    Alice->>Bob: Hello
and Alice to John
    Alice->>John: Hello
end
```

**Critical (Must succeed):**
```
critical Establish connection
    Service->>DB: Connect
option Network timeout
    Service->>Service: Retry
end
```

**Break (Exception):**
```
break When error occurs
    Service->>Client: Error
end
```

**Rect (Highlight):**
```
rect rgb(200, 220, 255)
    Alice->>Bob: Important flow
    Bob->>Alice: Response
end
```

### Sequence Numbers

```
sequenceDiagram
    autonumber
    Alice->>Bob: Step 1
    Bob->>Alice: Step 2
```

### Actor Links and Menus

```
sequenceDiagram
    participant A as Alice
    link A: Dashboard @ https://dashboard.example.com
    link A: Wiki @ https://wiki.example.com
```

### Character Escaping

Use HTML character names or numeric codes. Semicolons require `#59;`.

**Sources:**
- [Sequence Diagrams | Mermaid](https://mermaid.js.org/syntax/sequenceDiagram.html)
- [DeepWiki: Sequence Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.2-sequence-diagrams)
- [Mermaid Cheat Sheet](https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/)

---

## 3. Class Diagram

**Keyword:** `classDiagram`
**When to use:** Object-oriented design, UML modeling, data structures, API contracts, any system where you need to show classes with attributes/methods and their relationships.
**Documentation:** https://mermaid.js.org/syntax/classDiagram.html

### Class Definition

**Method 1: Colon notation (one member at a time):**
```
classDiagram
    class BankAccount
    BankAccount : +String owner
    BankAccount : +BigDecimal balance
    BankAccount : +deposit(amount) bool
    BankAccount : +withdraw(amount) int
```

**Method 2: Curly braces (grouped):**
```
classDiagram
    class BankAccount {
        +String owner
        +BigDecimal balance
        +deposit(amount) bool
        +withdraw(amount) int
    }
```

### Visibility Markers

| Symbol | Meaning |
|---|---|
| `+` | Public |
| `-` | Private |
| `#` | Protected |
| `~` | Package/Internal |

### Method Classifiers

| Suffix | Meaning |
|---|---|
| `*` | Abstract |
| `$` | Static |

Example: `+someAbstractMethod()* int` or `+someStaticMethod()$ String`

### Relationship Types

| Syntax | Relationship | Description |
|---|---|---|
| `<\|--` | Inheritance | "is-a" |
| `*--` | Composition | Strong "has-a" (part cannot exist without whole) |
| `o--` | Aggregation | Weak "has-a" (part can exist independently) |
| `-->` | Association | General relationship |
| `--` | Link (Solid) | Unspecified solid connection |
| `..>` | Dependency | "uses" |
| `..\|>` | Realization | Implements interface |
| `..` | Link (Dashed) | Unspecified dashed connection |

All arrows can be reversed (e.g., `--\|>` becomes `<\|--`).

### Cardinality / Multiplicity

```
classDiagram
    Customer "1" --> "*" Order : places
    Order "1" *-- "1..*" LineItem : contains
```

Common cardinality values: `1`, `0..1`, `1..*`, `*`, `n`, `0..n`, `1..n`

### Annotations

```
classDiagram
    class Shape {
        <<interface>>
        +draw()
    }
    class Color {
        <<enumeration>>
        RED
        GREEN
        BLUE
    }
```

Supported annotations: `<<interface>>`, `<<abstract>>`, `<<service>>`, `<<enumeration>>`, `<<sealed>>`, `<<static>>`

### Generics

```
classDiagram
    class Square~Shape~ {
        int id
        List~int~ position
        setPoints(List~int~ points)
    }
```

### Namespaces

```
classDiagram
    namespace BaseShapes {
        class Triangle
        class Rectangle
    }
```

### Notes

```
classDiagram
    note "This is a general note"
    note for MyClass "This is specific to MyClass"
```

### Direction

```
classDiagram
    direction RL
```

Options: `TB`, `BT`, `LR`, `RL`

### Styling

```
classDiagram
    class Animal:::styleClass
    classDef styleClass fill:#f9f,stroke:#333
    style Animal fill:#bbf
```

**Sources:**
- [Class Diagrams | Mermaid](https://mermaid.js.org/syntax/classDiagram.html)
- [Creating Class Diagrams with Mermaid.js](https://newdevsguide.com/2023/04/08/mermaid-class-diagrams/)
- [PBS 141: Generating UML Class Diagrams with Mermaid](https://pbs.bartificer.net/pbs141)

---

## 4. State Diagram

**Keyword:** `stateDiagram-v2` (recommended) or `stateDiagram`
**When to use:** State machines, workflow states, lifecycle management, protocol states, UI state management.
**Documentation:** https://mermaid.js.org/syntax/stateDiagram.html

### Basic Syntax

```
stateDiagram-v2
    [*] --> Still
    Still --> [*]
    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

- `[*]` represents start state (when transitioned FROM) or end state (when transitioned TO)
- `-->` defines transitions
- Transition labels: `Moving --> Crash : Collision detected`

### State Descriptions

```
stateDiagram-v2
    state "This is a long state name" as s1
    s1 --> s2: Event
```

### Composite (Nested) States

```
stateDiagram-v2
    [*] --> First
    state First {
        [*] --> Second
        Second --> [*]
    }
```

### Choice Nodes

```
stateDiagram-v2
    state if_state <<choice>>
    [*] --> IsPositive
    IsPositive --> if_state
    if_state --> False: if n < 0
    if_state --> True: if n >= 0
```

### Forks and Joins

```
stateDiagram-v2
    state fork_state <<fork>>
    state join_state <<join>>
    [*] --> fork_state
    fork_state --> State2
    fork_state --> State3
    State2 --> join_state
    State3 --> join_state
    join_state --> State4
```

### Concurrency

```
stateDiagram-v2
    [*] --> Active
    state Active {
        [*] --> NumLockOff
        NumLockOff --> NumLockOn : EvNumLockPressed
        --
        [*] --> CapsLockOff
        CapsLockOff --> CapsLockOn : EvCapsLockPressed
        --
        [*] --> ScrollLockOff
        ScrollLockOff --> ScrollLockOn : EvScrollLockPressed
    }
```

The `--` separator divides concurrent regions.

### Notes

```
stateDiagram-v2
    State1: The state with a note
    note right of State1
        Important information
        about this state
    end note
    note left of State2 : Short note
```

### Direction

```
stateDiagram-v2
    direction LR
```

Options: `TB`, `BT`, `LR`, `RL`

### Styling with classDef

```
stateDiagram-v2
    classDef badEvent fill:#f00,color:white
    classDef movement font-style:italic
    State1:::movement --> Crash:::badEvent
```

The `:::` operator applies a classDef style inline.

**Sources:**
- [State Diagrams | Mermaid](https://mermaid.js.org/syntax/stateDiagram.html)
- [DeepWiki: State Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.4-state-diagrams)
- [State Diagram Mermaid Tutorial](https://www.iodraw.com/codechart/tutorial/en/stateDiagram.html)

---

## 5. Entity Relationship (ER) Diagram

**Keyword:** `erDiagram`
**When to use:** Database schema design, data modeling, showing relationships between data entities.
**Documentation:** https://mermaid.js.org/syntax/entityRelationshipDiagram.html

### Basic Syntax

```
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

Each statement: `<first-entity> <relationship> <second-entity> : <label>`

### Cardinality Markers

The notation uses two characters per side. The outermost character = maximum, innermost = minimum.

| Syntax | Meaning |
|---|---|
| `\|\|` | Exactly one |
| `o\|` | Zero or one |
| `\|{` or `}|` | One or more |
| `o{` or `}o` | Zero or more |

### Relationship Line Types

| Syntax | Meaning |
|---|---|
| `--` | Identifying (solid line) |
| `..` | Non-identifying (dashed line) |

### Full Relationship Notation Examples

| Syntax | Reading |
|---|---|
| `\|\|--\|\|` | Exactly one to exactly one (identifying) |
| `\|\|--o{` | Exactly one to zero or more (identifying) |
| `}o..\|{` | Zero or more to one or more (non-identifying) |
| `o\|--\|\|` | Zero or one to exactly one (identifying) |

### Entity Attributes

```
erDiagram
    CUSTOMER {
        string name PK
        string email
        int age
    }
    ORDER {
        int id PK
        date created
        string status
    }
    CUSTOMER ||--o{ ORDER : places
```

Attribute format: `type name [PK|FK|UK] "comment"`

### Aliases

```
erDiagram
    p[Person] {
        string firstName
        string lastName
    }
```

**Sources:**
- [Entity Relationship Diagrams | Mermaid](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
- [ER Diagram Mermaid Viewer](https://docs.mermaidviewer.com/diagrams/er.html)
- [ER Diagram - Mermaid Chart Docs](https://docs.mermaidchart.com/mermaid-oss/syntax/entityRelationshipDiagram.html)

---

## 6. User Journey Diagram

**Keyword:** `journey`
**When to use:** Customer experience mapping, user experience flows, satisfaction tracking across touchpoints.
**Documentation:** https://mermaid.js.org/syntax/userJourney.html

### Syntax

```
journey
    title My Working Day
    section Go to Work
        Make tea: 5: Me
        Go upstairs: 3: Me
        Do work: 1: Me, Cat
    section Go Home
        Go downstairs: 5: Me
        Sit down: 5: Me
```

### Components

| Component | Syntax | Description |
|---|---|---|
| Title | `title My Journey` | Overall journey title |
| Section | `section Section Name` | Groups related tasks |
| Task | `Task name: score: actor1, actor2` | Individual step |

### Task Scoring

- Score range: **1** (negative experience) to **5** (positive experience)
- Multiple actors can be listed, separated by commas

### Notes

- Each section gets its own color grouping
- Actors are listed and color-coded in the diagram
- No edge/arrow customization -- this is a fixed-layout diagram

**Sources:**
- [User Journey Diagram | Mermaid](https://mermaid.js.org/syntax/userJourney.html)
- [User Journey Syntax | Mermaid Chart](https://docs.mermaidchart.com/mermaid/user-journey/syntax)
- [Mapping User Journeys with Mermaid.js](https://newdevsguide.com/2023/04/12/user-journey-maps-mermaid/)

---

## 7. Gantt Chart

**Keyword:** `gantt`
**When to use:** Project scheduling, timeline planning, task dependencies, milestone tracking.
**Documentation:** https://mermaid.js.org/syntax/gantt.html

### Basic Syntax

```
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    axisFormat %Y-%m-%d
    todayMarker stroke-dasharray: 5 5
    excludes weekends

    section Section A
        Completed task    :done,    des1, 2024-01-06, 2024-01-08
        Active task        :active,  des2, 2024-01-09, 3d
        Future task        :         des3, after des2, 5d
        Future task 2      :         des4, after des3, 5d

    section Critical Path
        Critical task      :crit, done, 2024-01-06, 24h
        Create tests       :crit, active, 3d
        Milestone          :milestone, 2024-01-25, 0d
```

### Configuration Directives

| Directive | Description | Example |
|---|---|---|
| `title` | Chart title | `title Project Plan` |
| `dateFormat` | Input date format | `dateFormat YYYY-MM-DD` |
| `axisFormat` | Output axis date format | `axisFormat %Y-%m-%d` |
| `todayMarker` | Style or hide today marker | `todayMarker off` |
| `excludes` | Dates to exclude from duration | `excludes weekends` or `excludes 2024-01-01` |
| `tickInterval` | Axis tick interval | `tickInterval 1week` |
| `weekday` | Start day of week | `weekday monday` |

### Task Tags

| Tag | Description |
|---|---|
| `done` | Completed task (grayed out) |
| `active` | Currently active task (highlighted) |
| `crit` | Critical path task (red) |
| `milestone` | Single point in time |

Tags are optional, but if used, must appear before the task ID.

### Task Metadata Format

```
Task title : [tags], [taskId], [startDate or 'after otherId'], [endDate or duration]
```

### Duration Formats

`1d`, `5d`, `2w`, `24h`, `1w`, etc.

### Dependencies

Use `after taskId` to set a task's start date based on another task's end date:
```
Task B : taskB, after taskA, 3d
```

### Milestones

Milestones represent a single instant in time. Their position is `initial date + duration/2`.

### Comments

```
%% This is a comment
```

**Sources:**
- [Gantt Diagrams | Mermaid](https://mermaid.js.org/syntax/gantt.html)
- [Gantt Diagram Config Schema](https://mermaid.js.org/config/schema-docs/config-defs-gantt-diagram-config.html)
- [DeepWiki: Gantt Charts](https://deepwiki.com/elastic/mermaid/3.6-gantt-charts)

---

## 8. Pie Chart

**Keyword:** `pie`
**When to use:** Proportional data, budget breakdowns, survey results, market share.
**Documentation:** https://mermaid.js.org/syntax/pie.html

### Syntax

```
pie showData
    title Budget Allocation
    "Development" : 40
    "Marketing" : 20
    "Operations" : 30
    "Admin" : 10
```

### Components

| Component | Syntax | Required |
|---|---|---|
| Keyword | `pie` | Yes |
| Show values | `showData` | No (displays values after legend) |
| Title | `title Chart Title` | No |
| Data entry | `"Label" : value` | Yes (at least one) |

### Rules

- Values must be positive numbers greater than zero
- Supports up to two decimal places
- Labels must be in double quotes
- Slices are ordered clockwise in declaration order
- No edge/arrow types -- this is a data visualization diagram
- No subgraph/grouping support

**Sources:**
- [Pie Chart Diagrams | Mermaid](https://mermaid.js.org/syntax/pie.html)
- [Making Pie Charts out of Mermaid.js](https://newdevsguide.com/2023/04/13/mermaid-pie/)

---

## 9. Quadrant Chart

**Keyword:** `quadrantChart`
**When to use:** Priority matrices, effort-vs-impact analysis, competitive positioning, risk assessment, feature prioritization.
**Documentation:** https://mermaid.js.org/syntax/quadrantChart.html

### Syntax

```
quadrantChart
    title Reach and Engagement of Campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```

### Components

| Component | Syntax | Description |
|---|---|---|
| Title | `title Text` | Chart title |
| X-axis | `x-axis Left Label --> Right Label` | Horizontal axis (both labels optional, arrow optional) |
| Y-axis | `y-axis Bottom Label --> Top Label` | Vertical axis |
| Quadrant labels | `quadrant-1` through `quadrant-4` | Text inside each quadrant |
| Points | `Point Name: [x, y]` | Data point; x, y in range 0-1 |

### Quadrant Numbering

| Quadrant | Position |
|---|---|
| `quadrant-1` | Top right |
| `quadrant-2` | Top left |
| `quadrant-3` | Bottom left |
| `quadrant-4` | Bottom right |

### Customization

Quadrant charts support theme variables for colors and styling via configuration directives.

**Sources:**
- [Quadrant Chart | Mermaid](https://mermaid.js.org/syntax/quadrantChart.html)
- [Quadrant Syntax | Mermaid Chart](https://docs.mermaidchart.com/mermaid/quadrant/syntax)
- [Quadrant Examples | Mermaid Chart](https://docs.mermaidchart.com/mermaid/quadrant/examples)

---

## 10. Requirement Diagram

**Keyword:** `requirementDiagram`
**When to use:** Systems engineering, SysML requirements tracing, compliance tracking, verification planning.
**Documentation:** https://mermaid.js.org/syntax/requirementDiagram.html

### Syntax

```
requirementDiagram

    requirement test_req {
        id: 1
        text: the test text.
        risk: high
        verifymethod: test
    }

    functionalRequirement test_req2 {
        id: 1.1
        text: the second test text.
        risk: low
        verifymethod: inspection
    }

    performanceRequirement test_req3 {
        id: 1.2
        text: the third test text.
        risk: medium
        verifymethod: demonstration
    }

    element test_entity {
        type: simulation
        docRef: reqs/test_entity
    }

    element test_entity2 {
        type: word doc
        docRef: reqs/test_entity2
    }

    test_entity - satisfies -> test_req2
    test_req - traces -> test_req2
    test_req - contains -> test_req3
    test_entity2 - verifies -> test_req3
```

### Requirement Types

| Type | Description |
|---|---|
| `requirement` | Generic requirement |
| `functionalRequirement` | Functional requirement |
| `interfaceRequirement` | Interface requirement |
| `performanceRequirement` | Performance requirement |
| `physicalRequirement` | Physical requirement |
| `designConstraint` | Design constraint |

### Requirement Properties

| Property | Values |
|---|---|
| `id` | User-defined string |
| `text` | User-defined description |
| `risk` | `low`, `medium`, `high` |
| `verifymethod` | `test`, `inspection`, `demonstration`, `analysis` |

### Element Properties

| Property | Description |
|---|---|
| `type` | User-defined type string |
| `docRef` | User-defined document reference |

### Relationship Types

| Relationship | Syntax | Description |
|---|---|---|
| Contains | `- contains ->` | Parent contains child |
| Copies | `- copies ->` | Copies from source |
| Derives | `- derives ->` | Derived from source |
| Satisfies | `- satisfies ->` | Element satisfies requirement |
| Verifies | `- verifies ->` | Element verifies requirement |
| Refines | `- refines ->` | Refines a requirement |
| Traces | `- traces ->` | Traceability link |

**Sources:**
- [Requirement Diagram | Mermaid](https://mermaid.js.org/syntax/requirementDiagram.html)
- [Creating SysML Requirement Diagrams in Mermaid.js](https://newdevsguide.com/2023/04/17/mermaid-requirement-diagrams/)

---

## 11. GitGraph Diagram

**Keyword:** `gitGraph`
**When to use:** Git branching strategies, release workflows, merge visualizations, CI/CD pipeline flows.
**Documentation:** https://mermaid.js.org/syntax/gitgraph.html

### Basic Syntax

```
gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    commit
```

### Operations

| Operation | Syntax | Description |
|---|---|---|
| Commit | `commit` | Add a commit to current branch |
| Commit with ID | `commit id: "abc123"` | Named commit |
| Commit with tag | `commit tag: "v1.0.0"` | Tagged commit |
| Commit with type | `commit type: HIGHLIGHT` | Styled commit |
| Branch | `branch branchName` | Create a new branch |
| Checkout | `checkout branchName` | Switch to branch |
| Switch | `switch branchName` | Same as checkout |
| Merge | `merge branchName` | Merge into current branch |
| Cherry-pick | `cherry-pick id: "abc123"` | Cherry-pick a commit |

### Commit Types

| Type | Description |
|---|---|
| `NORMAL` | Default commit style |
| `REVERSE` | Reverse-highlighted commit |
| `HIGHLIGHT` | Emphasized commit |

### Orientation

```
gitGraph LR:
    commit
```

| Keyword | Direction |
|---|---|
| (default) | Left-to-Right |
| `LR:` | Left-to-Right |
| `TB:` | Top-to-Bottom |
| `BT:` | Bottom-to-Top |

### Configuration Options

| Option | Type | Default | Description |
|---|---|---|---|
| `showBranches` | Boolean | `true` | Show/hide branch labels |
| `showCommitLabel` | Boolean | `true` | Show/hide commit labels |
| `mainBranchName` | String | `"main"` | Name of root branch |
| `mainBranchOrder` | Integer | `0` | Display order of main branch |
| `rotateCommitLabel` | Boolean | `true` | Rotate commit labels (TB mode) |

### Theme Support

Mermaid gitgraph supports all built-in themes: `default`, `forest`, `dark`, `neutral`, `base`.

**Sources:**
- [GitGraph Diagrams | Mermaid](https://mermaid.js.org/syntax/gitgraph.html)
- [DeepWiki: Git Graph Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.6-git-graph-diagrams)
- [How to Make a Git Graph with Mermaid Chart](https://docs.mermaidchart.com/blog/posts/how-to-make-a-git-graph-with-mermaid-chart)

---

## 12. Mindmap

**Keyword:** `mindmap`
**When to use:** Brainstorming, hierarchical idea organization, topic decomposition, knowledge mapping.
**Documentation:** https://mermaid.js.org/syntax/mindmap.html

### Basic Syntax

Hierarchy is defined by **indentation** (spaces or tabs):

```
mindmap
    root((Central Topic))
        Topic A
            Subtopic A1
            Subtopic A2
        Topic B
            Subtopic B1
        Topic C
```

### Node Shapes

| Shape | Syntax | Description |
|---|---|---|
| Default | `id` | No delimiters, default shape |
| Square | `id[Text]` | Square/rectangle |
| Rounded | `id(Text)` | Rounded rectangle |
| Circle | `id((Text))` | Circle |
| Cloud | `id)Text(` | Cloud shape |
| Bang | `id))Text((` | Explosion/bang |
| Hexagon | `id{{Text}}` | Hexagon |

### Icons

```
mindmap
    root
        A
        ::icon(fa fa-book)
        B
```

Uses Font Awesome or other icon class libraries via `::icon()` syntax.

### Markdown Strings

Supports bold (`**text**`) and italic (`*text*`) within node labels using Markdown Strings feature.

### Unique Features

- No arrows or edges -- hierarchy is entirely indentation-based
- No subgraph concept -- nesting is via indentation levels
- Automatic layout and coloring by level
- Where possible, shapes match flowchart shapes

**Sources:**
- [Mindmap | Mermaid](https://mermaid.js.org/syntax/mindmap.html)
- [Mind Maps in Markdown with Mermaid.js](https://newdevsguide.com/2023/04/14/mermaid-mind-maps/)
- [Create a Mindmap from Text with Mermaid (draw.io)](https://www.drawio.com/blog/mindmaps-from-text)

---

## 13. Timeline

**Keyword:** `timeline`
**When to use:** Historical events, project milestones over time, product roadmaps, company history, process phases.
**Documentation:** https://mermaid.js.org/syntax/timeline.html

### Basic Syntax

```
timeline
    title History of Social Media Platform
    2002 : LinkedIn
    2004 : Facebook
         : Google
    2005 : YouTube
    2006 : Twitter
```

### With Sections

```
timeline
    title Product Development Phases
    section Research
        2025-Q1 : Market Analysis
                : User Research
    section Design
        2025-Q2 : Wireframes
                : Prototypes
    section Development
        2025-Q3 : MVP Build
                : Testing
```

### Components

| Component | Syntax | Description |
|---|---|---|
| Title | `title Text` | Timeline title |
| Section | `section Name` | Group related periods |
| Time period | `2024 : Event` | Date/period with event |
| Multiple events | Indent additional `: Event` lines | Multiple events in one period |

### Styling

- Each section gets its own color scheme automatically
- Color customization via theme variables `cScale0` through `cScale11`
- `disableMultiColor` option makes all sections use the same color

### Notes

- No arrow/edge types -- this is a fixed-layout visualization
- No node shapes -- events are rendered as cards
- Date format is flexible (years, quarters, specific dates)

**Sources:**
- [Timeline Diagram | Mermaid](https://mermaid.js.org/syntax/timeline.html)
- [Creating Timeline Charts with Mermaid.js](https://newdevsguide.com/2023/04/16/mermaid-timeline-charts/)

---

## 14. Sankey Diagram

**Keyword:** `sankey-beta`
**When to use:** Flow quantities between nodes, energy/resource flows, budget allocation visualization, data pipeline throughput, migration tracking.
**Documentation:** https://mermaid.js.org/syntax/sankey.html
**Introduced:** v10.3.0+

### Basic Syntax

Uses CSV-like format with three columns: source, target, value.

```
sankey-beta

Agricultural 'waste',Bio-energy,124.729
Bio-energy,Electricity grid,289.366
Bio-energy,Losses,13.597
Coal imports,Coal,40.719
Coal,Electricity grid,35.889
```

### CSV Rules

- Three columns required: source, target, value
- Comma-separated
- Empty lines allowed for readability (without commas)
- Wrap values containing commas in double quotes

### Configuration Options

| Option | Description | Example |
|---|---|---|
| `width` | Diagram width | `800` |
| `height` | Diagram height | `400` |
| `linkColor` | Color of flows | `'source'`, `'target'`, `'gradient'`, or hex color |
| `nodeAlignment` | Node positioning | `'left'`, `'right'`, `'center'`, `'justify'` |

### Terminology

- **Nodes:** The entities being connected (displayed as rectangles)
- **Links:** The connections/flows between nodes (displayed as curved bands)

### Unique Features

- No traditional node shapes -- nodes are rectangles whose height corresponds to total flow
- No subgraph/grouping -- layout is automatic based on flow direction
- Flow width is proportional to quantity

**Sources:**
- [Sankey Diagram | Mermaid](https://mermaid.js.org/syntax/sankey.html)
- [Sankey Diagrams (Unmesh Gundecha)](https://unmesh.dev/post/mermaid_sankey/)
- [Present Flow Data Using Sankey Diagrams](https://mermaid.ai/docs/blog/posts/present-flow-data-using-sankey-diagrams)

---

## 15. XY Chart

**Keyword:** `xychart-beta`
**When to use:** Bar charts, line charts, trend data, comparisons, any x-y axis data visualization.
**Documentation:** https://mermaid.js.org/syntax/xyChart.html

### Basic Syntax

```
xychart-beta
    title "Sales Revenue"
    x-axis [jan, feb, mar, apr, may, jun]
    y-axis "Revenue (in $)" 4000 --> 11000
    bar [5000, 6000, 7500, 8200, 9800, 10500]
    line [5000, 6000, 7000, 8000, 9000, 10000]
```

### Components

| Component | Syntax | Description |
|---|---|---|
| Title | `title "Chart Title"` | Chart title (optional) |
| X-axis (categorical) | `x-axis [cat1, cat2, cat3]` | Category labels |
| X-axis (numeric) | `x-axis "Label" min --> max` | Numeric range |
| Y-axis | `y-axis "Label" min --> max` | Numeric range |
| Bar data | `bar [1, 2, 3, 4]` | Bar chart series |
| Line data | `line [1, 2, 3, 4]` | Line chart series |

### Orientation

```
xychart-beta horizontal
    ...
```

Options: `vertical` (default), `horizontal`

### Rules

- Only two things required: the chart keyword and one data set
- Text with spaces must be enclosed in quotes
- Multiple `bar` and `line` series can be combined
- X-axis can be categorical or numeric, Y-axis is always numeric

**Sources:**
- [XY Chart | Mermaid](https://mermaid.js.org/syntax/xyChart.html)
- [XY Chart on GitHub (source)](https://github.com/mermaid-js/mermaid/blob/develop/packages/mermaid/src/docs/syntax/xyChart.md)

---

## 16. Block Diagram

**Keyword:** `block-beta`
**When to use:** System architecture, component layouts, any diagram where you need precise positional control over blocks, layered architectures.
**Documentation:** https://mermaid.js.org/syntax/block.html

### Basic Syntax

```
block-beta
    columns 3
    A["Frontend"] B["API Gateway"] C["Backend"]
    space D["Database"] space
    A --> B --> C
    C --> D
```

### Columns

Define the grid layout with `columns N`:

```
block-beta
    columns 4
    A B C D
    E F G H
```

### Block Shapes

| Shape | Syntax | Description |
|---|---|---|
| Rectangle | `A["Text"]` | Default rectangle |
| Rounded | `A("Text")` | Rounded rectangle |
| Circle | `A(("Text"))` | Circle |
| Cylinder | `db[("Database")]` | Database/cylinder |
| Stadium | `A(["Text"])` | Pill shape |
| Rhombus | `A{"Text"}` | Diamond |
| Hexagon | `A{{"Text"}}` | Hexagon |

### Width Control

Blocks can span multiple columns:

```
block-beta
    columns 3
    A["Wide Block"]:3
    B C D
```

The `:N` suffix makes a block span N columns.

### Space Blocks

```
block-beta
    columns 3
    space A space
    space:2 B
```

`space` occupies one column; `space:N` occupies N columns.

### Nested Blocks

```
block-beta
    columns 2
    block:groupA:2
        columns 2
        A B
    end
    C D
```

### Arrows / Links

```
A --> B
A --- B
A -- "label" --> B
```

Similar to flowchart edge syntax.

### Styling

```
block-beta
    A["Styled"]
    style A fill:#969,stroke:#333,stroke-width:4px
    classDef highlight fill:#f9f,stroke:#333
    B["Also Styled"]:::highlight
```

**Sources:**
- [Block Diagram Syntax | Mermaid](https://mermaid.js.org/syntax/block.html)
- [Block Diagrams Documentation (Paradime)](https://docs.paradime.io/app-help/documentation/integrations/code-ide/mermaid-js/block-diagrams-documentation)

---

## 17. Architecture Diagram

**Keyword:** `architecture-beta`
**When to use:** Cloud infrastructure, CI/CD deployments, microservice topology, network architecture, system deployment diagrams.
**Documentation:** https://mermaid.js.org/syntax/architecture.html
**Introduced:** v11.1.0+

### Basic Syntax

```
architecture-beta
    group api(cloud)[API]

    service db(database)[Database] in api
    service disk1(disk)[Storage] in api
    service server(server)[Server] in api

    db:L -- R:server
    disk1:T -- B:server
```

### Components

**Groups:**
```
group groupId(icon)[Label]
```

Contain related services.

**Services:**
```
service serviceId(icon)[Label] in groupId
```

Services are the nodes of the diagram.

**Junctions:**
```
junction junctionId in groupId
```

4-way split points for edges.

**Edges:**
```
serviceA:side -- side:serviceB
serviceA:side --> side:serviceB
```

### Edge Direction Syntax

Sides are specified with `L`, `R`, `T`, `B` (Left, Right, Top, Bottom):

```
db:R --> L:server     %% Right of db to Left of server
disk1:T -- B:server   %% Top of disk1 to Bottom of server
```

- `<` before the direction on the left adds an arrow pointing left
- `>` after the direction on the right adds an arrow pointing right
- `--` = no arrows, `-->` = arrow on right, `<--` = arrow on left, `<-->` = bidirectional

### Group-to-Group Edges

Use `{group}` modifier:

```
server{group}:B --> T:subnet{group}
```

### Built-in Icons

Default icons: `cloud`, `database`, `disk`, `internet`, `server`

Supports 200,000+ icons from [iconify.design](https://iconify.design) by registering icon packs.

### Unique Features

- Positional edge attachment (L/R/T/B) gives precise control
- Junction nodes for splitting/merging edges
- Icon-first design with built-in and extensible icon support
- No traditional node shapes -- services use icons

**Sources:**
- [Architecture Diagrams Documentation | Mermaid](https://mermaid.js.org/syntax/architecture.html)
- [Introducing Architecture Diagrams in Mermaid](https://docs.mermaidchart.com/blog/posts/mermaid-supports-architecture-diagrams)
- [DeepWiki: Architecture Diagrams](https://deepwiki.com/mermaid-js/mermaid/3.5-architecture-diagrams)

---

## 18. Kanban Diagram

**Keyword:** `kanban`
**When to use:** Task boards, agile workflow visualization, project status tracking, team workload views.
**Documentation:** https://mermaid.js.org/syntax/kanban.html
**Introduced:** v11.4.0+

### Basic Syntax

```
kanban
    Todo
        task1[Design new feature]
            @{ ticket: PROJ-001, priority: 'High', assigned: 'Alice' }
        task2[Write documentation]
            @{ ticket: PROJ-002, priority: 'Low', assigned: 'Bob' }
    In Progress
        task3[Implement API]
            @{ ticket: PROJ-003, priority: 'Very High', assigned: 'Charlie' }
    Done
        task4[Setup CI/CD]
            @{ ticket: PROJ-004, assigned: 'Alice' }
```

### Column Definition

```
columnId[Column Title]
```

Each column uses a unique identifier with a title in square brackets.

### Task/Item Definition

Tasks are indented under their column:

```
taskId[Task Description]
    @{ metadata }
```

### Metadata Fields

| Field | Description | Values |
|---|---|---|
| `assigned` | Person responsible | Free text |
| `ticket` | Ticket/issue number | Free text (linkable) |
| `priority` | Task urgency | `'Very High'`, `'High'`, `'Low'`, `'Very Low'` |

### Configuration

| Option | Description |
|---|---|
| `ticketBaseUrl` | Base URL for ticket links (e.g., `https://jira.example.com/browse/`) |

### Unique Features

- Column-based layout (no arrows or edges)
- Metadata support for tickets, priority, and assignment
- Ticket numbers can become clickable links with `ticketBaseUrl`

**Sources:**
- [Mermaid Kanban Diagram Documentation](https://mermaid.js.org/syntax/kanban.html)
- [Mermaid 11.4: New Features and Kanban Diagramming](https://docs.mermaidchart.com/blog/posts/mermaid-11-4-is-out-new-features-and-kanban-diagramming)

---

## 19. Packet Diagram

**Keyword:** `packet-beta`
**When to use:** Network protocol headers, packet structure visualization, bit-level data format documentation, protocol analysis.
**Documentation:** https://mermaid.js.org/syntax/packet.html
**Introduced:** v11.0.0+

### Basic Syntax

```
packet-beta
    0-15: "Source Port"
    16-31: "Destination Port"
    32-63: "Sequence Number"
    64-95: "Acknowledgment Number"
    96-99: "Data Offset"
    100-105: "Reserved"
    106: "URG"
    107: "ACK"
    108: "PSH"
    109: "RST"
    110: "SYN"
    111: "FIN"
    112-127: "Window Size"
    128-143: "Checksum"
    144-159: "Urgent Pointer"
```

### Field Definition Formats

**Bit range format:**
```
start-end: "Field Name"
```

**Single bit:**
```
position: "Field Name"
```

**Bit count format (alternative):**
```
+1: "Single bit field"
+8: "Eight bit field"
+16: "Sixteen bit field"
```

Bit range and bit count formats can be mixed.

### Title (via frontmatter)

```
---
title: "TCP Packet Header"
---
packet-beta
    0-15: "Source Port"
    ...
```

### Unique Features

- Bit-level precision for field definitions
- Automatic row wrapping based on configured bits per row
- No arrows, edges, or grouping -- purely structural representation
- Two field definition methods (range and count) can be mixed

**Sources:**
- [Packet Diagram | Mermaid](https://mermaid.js.org/syntax/packet.html)
- [Mermaid Packet Diagrams (ITOHI)](https://itohi.com/snippets/diagrams/mermaid-packet/)

---

## 20. C4 Diagram

**Keyword:** `C4Context`, `C4Container`, `C4Component`, `C4Dynamic`, `C4Deployment`
**When to use:** Software architecture documentation using the C4 model (Context, Containers, Components, Code), system landscape visualization.
**Documentation:** https://mermaid.js.org/syntax/c4.html
**Status:** Experimental

### Context Diagram

```
C4Context
    title System Context Diagram for Internet Banking System

    Enterprise_Boundary(b0, "BankBoundary") {
        Person(customer, "Banking Customer", "A customer of the bank")
        System(banking_system, "Internet Banking System", "Allows customers to manage accounts")
    }

    System_Ext(mail_system, "E-mail System", "Microsoft Exchange")
    System_Ext(mainframe, "Mainframe Banking System", "Core banking")

    Rel(customer, banking_system, "Uses")
    Rel(banking_system, mail_system, "Sends e-mails", "SMTP")
    Rel(banking_system, mainframe, "Gets account info", "XML/HTTPS")
```

### Container Diagram

```
C4Container
    title Container Diagram for Internet Banking System

    Person(customer, "Customer", "A banking customer")

    Container_Boundary(c1, "Internet Banking") {
        Container(web_app, "Web Application", "Java, Spring MVC", "Delivers static content")
        Container(spa, "Single-Page App", "JavaScript, Angular", "Provides banking functionality")
        ContainerDb(database, "Database", "SQL Database", "Stores user data")
        Container(api, "API Application", "Java, Docker", "Provides banking API")
    }

    Rel(customer, web_app, "Uses", "HTTPS")
    Rel(web_app, spa, "Delivers")
    Rel(spa, api, "Uses", "JSON/HTTPS")
    Rel(api, database, "Reads/Writes", "JDBC")
```

### Component Diagram

```
C4Component
    title Component Diagram for API Application

    Container_Boundary(api, "API Application") {
        Component(sign_in, "Sign In Controller", "Spring MVC Rest Controller", "Allows users to sign in")
        Component(accounts, "Accounts Summary Controller", "Spring MVC Rest Controller", "Provides account summaries")
        Component(security, "Security Component", "Spring Bean", "Handles authentication")
        ComponentDb(db, "Database", "Oracle", "Stores data")
    }

    Rel(sign_in, security, "Uses")
    Rel(accounts, db, "Reads from")
```

### Core Elements

| Function | Description |
|---|---|
| `Person(id, label, description)` | A person/user |
| `Person_Ext(id, label, description)` | External person |
| `System(id, label, description)` | Internal system |
| `System_Ext(id, label, description)` | External system |
| `Container(id, label, technology, description)` | Container/service |
| `ContainerDb(id, label, technology, description)` | Database container |
| `ContainerQueue(id, label, technology, description)` | Message queue |
| `Component(id, label, technology, description)` | Component |
| `ComponentDb(id, label, technology, description)` | Database component |

### Boundary Types

| Function | Description |
|---|---|
| `Enterprise_Boundary(id, label)` | Enterprise boundary |
| `System_Boundary(id, label)` | System boundary |
| `Container_Boundary(id, label)` | Container boundary |
| `Deployment_Node(id, label)` | Deployment node |

### Relationships

```
Rel(source, target, label)
Rel(source, target, label, technology)
Rel_D(source, target, label)    %% Down
Rel_U(source, target, label)    %% Up
Rel_L(source, target, label)    %% Left
Rel_R(source, target, label)    %% Right
Rel_Back(source, target, label) %% Reverse
BiRel(source, target, label)    %% Bidirectional
```

### Notes

- C4 diagram support is experimental -- syntax may change in future releases
- Compatible with PlantUML C4 syntax
- Supports `UpdateLayoutConfig`, `UpdateElementStyle`, `UpdateRelStyle` for customization

**Sources:**
- [C4 Diagrams | Mermaid](https://mermaid.js.org/syntax/c4.html)
- [Building C4 Diagrams in Mermaid](https://lukemerrett.com/building-c4-diagrams-in-mermaid/)
- [C4 Diagram - Mermaid Chart](https://content.mermaidchart.com/diagram-syntax/c4-diagram/)

---

## 21. ZenUML (Alternative Sequence Diagram)

**Keyword:** `zenuml`
**When to use:** Same use cases as sequence diagrams, but with a code-like syntax that may feel more natural to developers.
**Documentation:** https://mermaid.js.org/syntax/zenuml.html

### Basic Syntax

```
zenuml
    Alice->Bob: Hello
    Bob->Alice: Hi

    if(condition) {
        Alice->Bob: Do this
    } else {
        Alice->Bob: Do that
    }
```

### Key Differences from Standard Sequence Diagram

| Feature | Standard Sequence | ZenUML |
|---|---|---|
| Conditionals | `alt`/`else`/`end` | `if()`/`else`/`{}` |
| Loops | `loop`/`end` | `while()`/`{}` or `for()`/`{}` |
| Optional | `opt`/`end` | `opt`/`{}` |
| Parallel | `par`/`and`/`end` | `par`/`{}` |
| Exception | `break`/`end` | `try`/`catch`/`{}` |
| Comments | `%%` | `//` |

### Supported Features

- Conditional logic: `if`/`else if`/`else`
- Loops
- Optional fragments
- Parallel actions
- Exception handling (try/catch)
- Comments (`//`)
- Implicit participant declaration

### Unique Features

- Code-like syntax (curly braces, if/else, try/catch)
- Model-first philosophy
- Available as an external plugin (`@mermaid-js/mermaid-zenuml`)

**Sources:**
- [ZenUML | Mermaid](https://mermaid.js.org/syntax/zenuml.html)
- [ZenUML npm package](https://www.npmjs.com/package/@mermaid-js/mermaid-zenuml)
- [Best Mermaid Alternatives for Sequence Diagrams | ZenUML](https://zenuml.com/best-mermaid-alternative-for-sequence-diagrams/)

---

## Global Features (Applicable Across Diagram Types)

### Directives

Configure diagram behavior inline:

```
%%{init: {"theme": "dark", "flowchart": {"curve": "basis"}} }%%
flowchart LR
    A --> B
```

### Themes

Available themes: `default`, `forest`, `dark`, `neutral`, `base`

```
%%{init: {"theme": "forest"} }%%
```

### Comments

All diagram types support comments with `%%`:

```
%% This is a comment
```

### Markdown Strings

Many diagram types support Markdown-formatted text in labels using backtick delimiters:

```
flowchart LR
    A["`**Bold** and *italic*`"] --> B["`Line 1
    Line 2`"]
```

### Frontmatter

YAML frontmatter can be used for configuration:

```
---
title: My Diagram
config:
    theme: dark
---
flowchart LR
    A --> B
```

### Security Levels

| Level | Description |
|---|---|
| `strict` | Tags stripped, click disabled |
| `loose` | Tags allowed, click enabled |
| `antiscript` | Script tags stripped, other HTML allowed |
| `sandbox` | Renders in sandboxed iframe |

**Sources:**
- [Diagram Syntax Reference | Mermaid](https://mermaid.js.org/intro/syntax-reference.html)
- [Directives | Mermaid](https://mermaid.js.org/config/directives.html)
- [About Mermaid](https://mermaid.js.org/intro/)
- [Mermaid Homepage](https://mermaid.js.org/)

---

## Quick Reference: Diagram Type Keywords

| Keyword | Diagram Type |
|---|---|
| `flowchart` or `graph` | Flowchart |
| `sequenceDiagram` | Sequence Diagram |
| `classDiagram` | Class Diagram |
| `stateDiagram-v2` | State Diagram |
| `erDiagram` | Entity Relationship |
| `journey` | User Journey |
| `gantt` | Gantt Chart |
| `pie` | Pie Chart |
| `quadrantChart` | Quadrant Chart |
| `requirementDiagram` | Requirement Diagram |
| `gitGraph` | Git Graph |
| `mindmap` | Mindmap |
| `timeline` | Timeline |
| `sankey-beta` | Sankey Diagram |
| `xychart-beta` | XY Chart |
| `block-beta` | Block Diagram |
| `architecture-beta` | Architecture Diagram |
| `kanban` | Kanban Board |
| `packet-beta` | Packet Diagram |
| `C4Context` | C4 Context Diagram |
| `C4Container` | C4 Container Diagram |
| `C4Component` | C4 Component Diagram |
| `C4Dynamic` | C4 Dynamic Diagram |
| `C4Deployment` | C4 Deployment Diagram |
| `zenuml` | ZenUML Sequence Diagram |

---

## Master Source List

- [Mermaid.js Official Site](https://mermaid.js.org/)
- [Mermaid GitHub Repository](https://github.com/mermaid-js/mermaid)
- [Mermaid Syntax Reference](https://mermaid.js.org/intro/syntax-reference.html)
- [Mermaid Examples](https://mermaid.js.org/syntax/examples.html)
- [Mermaid Releases](https://github.com/mermaid-js/mermaid/releases)
- [Mermaid Chart Documentation](https://docs.mermaidchart.com/)
- [Mermaid Live Editor](https://mermaid.live/)
- [Flowchart Syntax](https://mermaid.js.org/syntax/flowchart.html)
- [Sequence Diagram Syntax](https://mermaid.js.org/syntax/sequenceDiagram.html)
- [Class Diagram Syntax](https://mermaid.js.org/syntax/classDiagram.html)
- [State Diagram Syntax](https://mermaid.js.org/syntax/stateDiagram.html)
- [ER Diagram Syntax](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)
- [User Journey Syntax](https://mermaid.js.org/syntax/userJourney.html)
- [Gantt Syntax](https://mermaid.js.org/syntax/gantt.html)
- [Pie Chart Syntax](https://mermaid.js.org/syntax/pie.html)
- [Quadrant Chart Syntax](https://mermaid.js.org/syntax/quadrantChart.html)
- [Requirement Diagram Syntax](https://mermaid.js.org/syntax/requirementDiagram.html)
- [GitGraph Syntax](https://mermaid.js.org/syntax/gitgraph.html)
- [Mindmap Syntax](https://mermaid.js.org/syntax/mindmap.html)
- [Timeline Syntax](https://mermaid.js.org/syntax/timeline.html)
- [Sankey Syntax](https://mermaid.js.org/syntax/sankey.html)
- [XY Chart Syntax](https://mermaid.js.org/syntax/xyChart.html)
- [Block Diagram Syntax](https://mermaid.js.org/syntax/block.html)
- [Architecture Diagram Syntax](https://mermaid.js.org/syntax/architecture.html)
- [Kanban Syntax](https://mermaid.js.org/syntax/kanban.html)
- [Packet Diagram Syntax](https://mermaid.js.org/syntax/packet.html)
- [C4 Diagram Syntax](https://mermaid.js.org/syntax/c4.html)
- [ZenUML Syntax](https://mermaid.js.org/syntax/zenuml.html)
- [30 New Flowchart Shapes Blog Post](https://docs.mermaidchart.com/blog/posts/expanding-the-horizons-of-mermaid-flowcharts-introducing-30-new-shapes)
- [History of Mermaid.js (Taskade)](https://www.taskade.com/blog/history-of-mermaid)
- [DeepWiki: Mermaid Diagram Types](https://deepwiki.com/mermaid-js/mermaid/3-diagram-types)
- [Mermaid Cheat Sheet](https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/)
