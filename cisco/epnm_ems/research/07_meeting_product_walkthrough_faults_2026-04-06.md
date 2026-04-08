# 07 - Meeting: Product Walkthrough — Fault Management

**Source:** /cisco/epnm_ems/source/selva_and_team_4-6-2026.txt
**Source Date:** 2026-04-06 (EPNM Features Walkthrough)
**Document Set:** 07 (Team walkthrough meeting)
**Pass:** Focused deep dive on fault management screen walkthrough

---

## Overview

This document decomposes every statement, demonstration, and detail from the April 6, 2026 meeting that relates to fault management — the second of two functional areas identified for the POC. The meeting was a live walkthrough of EPNM conducted primarily by Akhil (Cisco tech lead), with contributions from Janice (fault management area), Praveen (engineering leadership), and Ramesh. Colin Moore (BayOne, Director of AI) was the primary audience. The fault management walkthrough was briefer than the inventory walkthrough, but the transcript captures specific UI elements, navigation paths, and features that define the conversion scope for Part 2 of the POC.

---

## Context: Fault Management as Part 2 of the POC

### Explicit Delineation from Inventory

Selva drew a clear boundary between the two POC parts during the meeting. After the inventory walkthrough concluded, he introduced the fault management section with an explicit framing statement to Colin:

> "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."

Colin confirmed understanding: "Makes sense. Yeah. Makes sense."

This is structurally important. The two parts are not sequential phases — they are distinct functional domains within the same POC scope. Part 1 (inventory) covers device management, network devices, device 360, device details, and chassis view. Part 2 (fault management) covers alarms, events, syslogs, and correlated alarms. They share common UI patterns (tables, filtering, expandable rows) but represent different backend data sources and domain logic.

### Where Fault Management Lives in EPNM Navigation

Akhil demonstrated the navigation path during the live walkthrough:

> "From monitor, you can go to the alarms and events. This is fault management."

The EPNM navigation hierarchy is: **Monitor** (top-level menu) > **Alarms and Events** (submenu item). This is the primary entry point for fault management. Unlike inventory (which lives under a "Device Management" category), fault management is grouped under "Monitor" — the operational monitoring section of the EPNM interface.

---

## Alarms Screen: Detailed Walkthrough

### Primary Alarms Table

Akhil opened the alarms screen and described what was visible:

> "So you can see the alarms here. And it's on the table actions similar to the network devices."

This establishes a critical architectural point: the alarms table uses the same table component pattern as the network devices table from Part 1. Both share common table infrastructure — column sorting, row selection, table actions toolbar, and data grid behavior. This means conversion work on the table component for inventory will directly benefit the fault management screens, and vice versa. The common table pattern is part of the "common UI" repository (the shared component library referenced later in the architecture discussion).

### Table Actions

The alarms table has a toolbar of actions. Janice contributed to this section:

> "Clear alarms."

Akhil prompted Janice to elaborate: "So Janice, you want to add anything here?" Janice's response identified "clear alarms" as a key action. In EPNM, clearing an alarm is an operational action — it marks the alarm as acknowledged/resolved without necessarily resolving the underlying condition. This is a write operation against the alarm management backend, not just a display operation.

Other table actions were described as "similar to the network devices," which in the inventory walkthrough included: edit, delete, bulk operations, export, and state management actions. For alarms, the equivalent set likely includes:
- Clear alarms (confirmed by Janice)
- Acknowledge alarms (standard fault management pattern)
- Filter/search operations
- Export functionality

### Correlated Alarms

Janice raised correlated alarms as a distinct concept:

> "Correlated alarms. I think that we showed the 360 view."

This is a reference to the fact that alarms can be correlated — multiple related alarms grouped under a root cause. Correlated alarms are a standard feature in network management systems where a single device failure can trigger cascading alarms across the network. In EPNM, correlated alarms appear to be viewable from at least two places:

1. **The alarms table itself** — where correlation relationships between alarms are represented (likely through parent-child groupings or a correlation ID column).
2. **The device 360 view** — the pop-up detail view for a device (demonstrated in the inventory section) includes an alarms tab that shows alarms associated with that specific device.

Janice's mention of the 360 view in context of correlated alarms suggests that the 360 pop-up can display alarm correlation chains specific to a device — showing not just the alarms on that device, but how they relate to alarms on connected devices.

### Columns and Data Fields

Akhil noted that the alarms table has extensive column options:

> "And there are different columns here in the right hand side also."

This indicates that the alarms table supports column configuration — users can select which columns to display, likely through a column picker control on the right side of the table. Standard alarm table columns in a network management system would include:

- Severity (critical, major, minor, warning, info)
- Alarm source (device name/IP)
- Alarm type/category
- Timestamp (when the alarm was raised)
- Status (active, cleared, acknowledged)
- Description/message text
- Correlation ID or root cause reference

The exact column set was not enumerated during the walkthrough, but the mention of "different columns" and a right-hand configuration area indicates that column configurability is part of the UI that must be replicated.

---

## Events Screen: Detailed Walkthrough

### Events as a Separate View from Alarms

Akhil demonstrated that events are accessible from the alarms screen but constitute a distinct data set:

> "From here there is a different pop-up most recent events and then there is all events eight hours past eight hours then there is an events page a secondary table."

This single sentence describes a multi-layered events interface:

1. **Most recent events pop-up** — a pop-up window (modal or panel) accessible from the alarms screen that shows the most recent events. This is a quick-access view, not a full-page navigation. It likely appears when clicking a button or link within the alarms view.

2. **Time-based filtering** — the events view has a time-based filter with at least one preset: "past eight hours." This is a standard pattern for operational monitoring — showing events within a recent time window. The "all events" option likely removes the time filter to show the full event history.

3. **Events page (secondary table)** — beyond the pop-up, there is a full-page events table. Akhil described this as a "secondary table," meaning it is a separate data grid from the alarms table, rendered on its own page or panel. This is the comprehensive events view for detailed investigation.

### Relationship Between Alarms and Events

The transcript does not explicitly state the relationship, but standard EPNM architecture follows this pattern: **events are the raw occurrences** (traps, syslogs, notifications received from devices), while **alarms are the processed, deduplicated, correlated state** derived from those events. An alarm may be created from one or more events, and an alarm persists until cleared, while events are immutable log entries. The fact that events are accessible from the alarms screen supports this — operators investigating an alarm can drill into the underlying events that triggered it.

---

## Syslogs

### Syslogs as a Distinct Data Source

Akhil mentioned syslogs as a separate element within the fault management screens:

> "And then we have syslogs."

This was stated in sequence after events, indicating that syslogs are a third data type within the fault management area, alongside alarms and events. Syslogs are device-generated log messages (RFC 5424 format) that provide detailed operational information. In EPNM, syslogs likely have their own view or tab within the fault management section, with their own table, filtering, and column configuration.

The mention is brief, with no additional detail about the syslog UI layout. This is an area where further investigation of the actual EPNM interface will be needed during the POC to understand the syslog viewing, filtering, and search capabilities.

---

## Filtering Capabilities

### Quick Filter

Akhil described two levels of filtering available across the fault management tables:

> "All the table we have a quick filter and advance filter."

**Quick filter** is a text-based search that operates across visible table columns. In EPNM's Dojo-based table implementation, this is typically a text input field at the top of the table that performs client-side or server-side filtering as the user types. Quick filter provides immediate narrowing of results without configuring specific column/value criteria.

### Advanced Filter

**Advanced filter** provides structured, multi-criteria filtering. In EPNM, advanced filters typically allow:
- Column-specific criteria (e.g., severity = Critical AND source contains "router")
- Logical operators (AND, OR, NOT)
- Date/time range selection
- Saved filter presets
- Complex compound conditions

The distinction between quick filter and advanced filter is important for the POC because:
1. Quick filter is relatively straightforward to implement — it is a text search across visible data.
2. Advanced filter requires a filter builder UI with condition rows, operator selectors, and field type-specific input controls (dropdowns for enum fields, date pickers for timestamps, text inputs for strings). This is significantly more complex to build.

### Time-Based Filtering on Events

As noted above, the events view includes time-based presets:

> "Most recent events and then there is all events eight hours past eight hours."

This is a specialized filter control specific to event data — offering time window presets (e.g., "Past 8 hours," "Past 24 hours," "All") rather than requiring users to enter explicit date ranges. This is separate from the generic quick/advanced filter and likely appears as a toggle or dropdown control near the events table.

---

## Expandable Row Data

### Row Expansion Pattern

Akhil described an expandable row feature present in the fault management tables:

> "And also there is expandable in the PC every day row has expandable data as information, general information, things like that."

Despite the speech-to-text distortion ("PC every day" likely intended as "basically every"), the meaning is clear: **every row in the alarms/events table can be expanded inline to reveal additional detail.** This is a standard data grid pattern where clicking an expand icon on a row reveals a sub-panel below the row containing additional fields that are not shown in the table columns.

The expandable row data includes:
- **General information** — basic alarm/event metadata not shown in the compact table row
- **"Things like that"** — additional detail fields (alarm history, correlated event chain, device context, recommended actions, etc.)

This is an important UI element to replicate because:
1. It requires a specific table rendering behavior (row expansion with animated reveal)
2. The expanded content may be fetched on-demand (lazy loaded when the user expands a row) rather than pre-loaded with the table data
3. The layout within the expanded section is a nested detail view, not another table — it likely uses a key-value pair layout or a multi-section panel

---

## Repository and Backend Context for Fault Management

### Fault Management Code Location

During the architecture discussion later in the meeting, Akhil described where fault management code lives in the EPNM repository structure:

> "Fault management EPA wireless repo and fault and this is I think Janice's backend right the fault is on the backend it's backend and assembly is in the UI side."

Parsing through the speech-to-text distortion, this establishes:
1. **EPNM fault management UI code** lives in the **assembly repo** — the same repository that contains the inventory screen UI code.
2. **EPNM fault management backend code** lives in a separate backend repository. Janice appears to be the tech lead responsible for the fault management backend ("Janice's backend").
3. There is also a reference to "EPA wireless repo" which suggests that some fault management logic may also exist in the wireless-specific repository, potentially for wireless-specific alarm types.

### EMS Backend Counterpart

For the new EMS side:

> "EMS assurance is also back inside."

"EMS assurance" likely refers to the assurance module within EMS — the component responsible for fault/alarm/event management in the new product. The backend for fault management in EMS already exists (this is part of the ~80% of functionality that has been reimplemented), which means the POC's fault management work is primarily a UI conversion exercise that maps the EPNM visual experience to the existing EMS assurance backend APIs.

---

## How Fault Management Differs from Inventory in Complexity

### Shared Table Infrastructure

Both inventory and fault management use the same common table components. This is explicitly stated: "table actions similar to the network devices." This means that table rendering, column sorting, pagination, row selection, and basic CRUD toolbar actions share a common implementation. Work on one area directly reduces effort on the other.

### Unique Complexity Factors in Fault Management

Despite the shared table infrastructure, fault management introduces complexity not present in inventory:

1. **Time-sensitive, streaming data.** Alarms and events are continuously generated. Unlike the network devices table (which shows a relatively static inventory that changes infrequently), the alarms table must handle real-time or near-real-time data updates. New alarms appear, existing alarms change state (from active to acknowledged to cleared), and the table must reflect these changes. This may involve WebSocket connections, polling, or server-sent events for live updates.

2. **Correlation logic.** Correlated alarms add a dimension not present in inventory. The UI must represent parent-child or root-cause-to-symptom relationships between alarms. This could manifest as tree structures within the table, grouped rows, or drill-down navigation between related alarms.

3. **Multiple data types in one area.** Fault management spans three distinct data types: alarms, events, and syslogs. Each has its own table, its own schema, and its own filtering needs. Inventory is primarily one data type (network devices) with detail views. Fault management is three interlocking data types with cross-references between them.

4. **Advanced filtering complexity.** The advanced filter in fault management must handle severity levels, time ranges, alarm states, correlation IDs, device references, and alarm type categories. This is a richer filter domain than inventory, where filtering is primarily by device type and location.

5. **Expandable row detail.** While inventory has device 360 as a separate pop-up, fault management has inline expandable rows that show detail without leaving the table context. This is a different interaction pattern that requires the table component to support nested content rendering.

6. **Events pop-up with time presets.** The "most recent events" pop-up with its time-based filtering presets is a UI element with no direct counterpart in the inventory screens.

### Shared Complexity Factors

Some complexity is shared between both areas:
- 360 views (device 360 in inventory, and correlated alarm 360 views in faults)
- Pop-up modal dialogs for detail views
- Quick filter and advanced filter on tables
- Column configuration/picker

---

## What Colin Observed and Confirmed

Colin did not ask detailed follow-up questions during the fault management walkthrough section specifically, but his summary statement at the end of the meeting encompasses both areas:

> "On my side, I think the two cases here are clear. The code is clear."

And regarding the UX conversion approach:

> "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend. So that's very clear for me."

This confirms that fault management, like inventory, will be a faithful visual reproduction of the EPNM experience connected to the new EMS backend. No UX redesign, no simplification — pixel-accurate reproduction of the classic EPNM fault management screens.

Colin also noted the quality of Cisco's preparation:

> "Even that confluence page where it was showing, here are the specific links to everything. Here's where this information is. Usually we have to go digging for that. So actually my life is a lot easier because this is really organized."

This is relevant to fault management because the Confluence page included recordings, user guides, and API documentation that cover fault management functionality.

---

## The Toggle Mechanism and Fault Management

### How the Toggle Applies

Akhil described the toggle concept that applies across both POC areas:

> "Basically what I think you can come up with your own design, but the idea is like the default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be the EPNM current feel should be shown instead of Magnetic."

And:

> "Once I suppose I have a toggle button somewhere in the UI once I toggle it to EMS UI then the current design should be shown."

For fault management, this means:
1. **Default state (EPNM theme active):** The Monitor > Alarms and Events screens render with the EPNM classic look and feel — blue and white color scheme, Dojo-style table components, classic EPNM navigation patterns.
2. **Toggled state (EMS theme active):** The same screens render with the Magnetic design system (Angular, Harbor/Magnetic components), the current EMS visual language.

Both states connect to the same EMS backend (assurance module). Only the presentation layer changes. The fault management data (alarms, events, syslogs) comes from the same EMS backend APIs regardless of which theme is active.

---

## EPNM Design System Context

Akhil described the visual characteristics of the two design systems:

> "EPNM UI is a Dojo based framework. And if you look at the theming is kind of a blue and white kind of thing. And if you look at the Crosswork UI, we have a Magnetic design system. So it's a design system called Harbor and Magnetic design system."

For fault management conversion:
- **Source (EPNM):** Blue and white theme, Dojo-based components, classic enterprise table styling
- **Target rendering (classic mode):** Replicate the blue and white EPNM visual language using Angular components
- **Alternative rendering (EMS mode):** Harbor/Magnetic design system (already exists in current EMS)

The conversion challenge is not just functional but visual: the Angular components used in the classic mode must faithfully reproduce the visual density, spacing, color palette, and interaction patterns of the Dojo-based EPNM tables. Fault management tables in enterprise NMS products are typically very dense, with many columns, color-coded severity indicators, and compact row heights to maximize the number of visible alarms.

---

## Open Questions Specific to Fault Management

1. **What are the exact columns in the alarms table?** The walkthrough mentioned "different columns" but did not enumerate them. The column set determines the data model that the classic UI must consume from the EMS assurance APIs.

2. **What does the correlated alarms view actually look like?** Janice mentioned correlated alarms and referenced the 360 view, but the visual representation of correlation (tree hierarchy, grouped rows, separate correlation panel) was not demonstrated in detail.

3. **What is the syslog UI?** Syslogs were mentioned as a single word. The syslog viewer's layout, filtering capabilities, and relationship to the alarms/events views were not described. This needs investigation during POC setup.

4. **How are alarms updated in real-time?** Does the EPNM alarm table auto-refresh, use polling, or receive push updates? The EMS equivalent must match this behavior for the classic view.

5. **What does the expandable row content look like?** The expandable row was described as containing "general information, things like that." The exact fields, layout, and data sources for the expanded content need to be mapped.

6. **What are the advanced filter fields for fault management?** The advanced filter was mentioned but not demonstrated. The specific filter criteria, operators, and saved filter capabilities need to be catalogued.

7. **How do the three data types (alarms, events, syslogs) cross-reference?** Can a user navigate from an alarm to its underlying events? From an event to the generating syslog? The navigation paths between these three views were not fully described.

8. **What is the events time-based filtering granularity?** "Past 8 hours" was mentioned as one preset. What other presets exist? Can users specify custom time ranges? Is there a calendar-picker control?

9. **Does the alarms table support severity-based row coloring?** In most NMS products, alarm rows are color-coded by severity (red for critical, orange for major, yellow for minor). This visual treatment was not explicitly mentioned but is almost certainly present in EPNM.

10. **What actions exist beyond "clear alarms"?** Janice mentioned clearing alarms. Are there other alarm-specific actions such as acknowledge, annotate/add notes, assign to operator, suppress, or create trouble ticket?

11. **What is the relationship between the "most recent events" pop-up and the full events page?** Are they showing the same data with different filters, or are they different views with different data sources?

12. **Which backend APIs in EMS assurance correspond to each fault management view?** The alarms table, events table, syslog view, correlated alarms, and expandable row detail each likely call different API endpoints. These need to be mapped during the POC.

---

## Transcript Coverage Assessment

The fault management section of the walkthrough was significantly shorter than the inventory section. Akhil spent more time on device management, device 360, and device details, with the fault management walkthrough compressed into a relatively brief segment. Janice, who appears to be the fault management domain expert, contributed only two short statements (correlated alarms and clear alarms). This brevity means that the POC will require additional investigation of the EPNM fault management screens — through the user guide, the recordings that Cisco's team added to Confluence, and direct access to a running EPNM instance — to fully catalogue the UI elements that need conversion.

The brevity may also reflect that Akhil was primarily an inventory/device management engineer, and fault management is Janice's domain. A follow-up session focused specifically on fault management with Janice leading the walkthrough would likely yield substantially more detail.

---

## Key Quotes Index

**Selva on delineation between POC parts:**
- "Just to put some delineation, Colin, whatever we covered earlier is part one of the POC, like the inventory device, like that's target for the POC. This is part two, and this is a different area."

**Akhil on fault management navigation:**
- "From monitor, you can go to the alarms and events. This is fault management."

**Akhil on alarms table:**
- "So you can see the alarms here. And it's on the table actions similar to the network devices."

**Janice on alarm actions:**
- "Clear alarms."

**Janice on correlated alarms:**
- "Correlated alarms. I think that we showed the 360 view."

**Akhil on events:**
- "From here there is a different pop-up most recent events and then there is all events eight hours past eight hours then there is an events page a secondary table."

**Akhil on filtering:**
- "All the table we have a quick filter and advance filter."

**Akhil on syslogs:**
- "And then we have syslogs."

**Akhil on expandable rows:**
- "And also there is expandable in the [table] every row has expandable data as information, general information, things like that."

**Akhil on columns:**
- "And there are different columns here in the right hand side also."

**Akhil on EPNM design:**
- "EPNM UI is a Dojo based framework. And if you look at the theming is kind of a blue and white kind of thing."

**Akhil on toggle concept:**
- "The idea is like the default, once I log into the Crosswork UI, the default will be showing the EPNM theme."

**Colin on clarity of both cases:**
- "On my side, I think the two cases here are clear. The code is clear."

**Colin on visual fidelity:**
- "So really we'll keep it exactly, visually speaking, and UX speaking identical to this EPNM use case. But Selva, as you said, map everything to the new backend."

**Akhil on fault management code location:**
- "Fault management [is in the] wireless repo and fault and this is Janice's backend... the fault is on the backend... and assembly is in the UI side."
