# 05 — Technical Landscape

**Purpose of this document:** The technical context the execution session needs to understand before opening either repository. What EPNM looks like from a stack perspective, what EMS looks like, how they are architected, and what the 2026-04-06 walkthrough demonstrated about the actual product behavior. This document synthesizes the Set 07 walkthrough and the Set 08 technical research into a coherent picture.

For the deep conversion patterns reference (Dojo-to-Angular mapping tables, theme toggle architecture, folder structures, code examples), see `06_conversion_patterns_reference.md`.

---

## 1. EPNM — The Legacy Product

### 1.1 Product identity

EPNM stands for Evolved Programmable Network Manager. It is Cisco's long-standing network management product. Customers have been running EPNM operationally for approximately a decade.

### 1.2 Frontend

- **Framework:** Dojo Toolkit, version 1.x branch (the legacy branch). Dojo 2+ is a complete TypeScript rewrite with no meaningful relationship to 1.x. There is no automated migration path from Dojo 1.x to anything modern; the conversion is a full rewrite.
- **Module system:** AMD (Asynchronous Module Definition) via `define()` and `require()`. Older EPNM code may also use the pre-AMD synchronous `dojo.provide` / `dojo.require` format.
- **Component model:** Dijit widgets. Every UI element is a Dijit widget with a defined lifecycle (`constructor`, `postMixInProperties`, `buildRendering`, `postCreate`, `startup`, `destroy`). `postCreate` is where most widget logic lives; begin reading there for any widget.
- **Class system:** `dojo/_base/declare`. Single inheritance with C3-linearized mixin support (Python-style MRO). Custom mixins are conventionally prefixed with an underscore.
- **Templating:** HTML template strings using `data-dojo-attach-point` for DOM node references, `data-dojo-attach-event` for DOM-to-method wiring, and `${propertyName}` for one-time (non-reactive) property substitution. `_TemplatedMixin` turns templates into DOM during `buildRendering`. `_WidgetsInTemplateMixin` enables nested Dijit widgets within templates.
- **Declarative markup:** Widgets can also be instantiated from HTML via `data-dojo-type` and `dojo/parser`. The execution session must check both JavaScript code and HTML/JSP markup for widget creation.
- **Data stores:** `dojo/store` API. Common stores include `Memory` (in-memory), `JsonRest` (REST-backed), `Observable` (reactive wrapper), and `Cache` (caching wrapper). Store composition is typical: `Observable(Cache(JsonRest(...), Memory()))`. Store URL targets map directly to backend REST endpoints; cataloging JsonRest store targets yields the complete API contract.
- **Events:** Two systems. `dojo/on` for direct DOM events. `dojo/topic` for global pub/sub with `topic.publish()` and `topic.subscribe()`. Pub/sub creates implicit contracts between loosely-coupled widgets — cataloging all publish and subscribe calls is essential for mapping widget interactions.
- **Grids:** `dojox/grid/DataGrid` (older, monolithic, uses `dojo/data` API) and `dgrid` (newer since Dojo 1.7, lightweight, modular, built on `dojo/store`). Grids are likely the most important widget type in EPNM given the heavy use of tabular screens.
- **Theme:** Blue and white. The default EPNM visual language.

### 1.3 Backend

- **Language:** Java monolith.
- **Database:** Oracle.
- **Device images:** Historically stored in Oracle.
- **Device data collection:** SNMP polling and CLI polling. Device credentials are configured per device at add time. Collected information is parsed, normalized to an internal data model, and persisted to the database.

### 1.4 Data flow

Network devices → (SNMP, CLI polling) → Data Collection and Parsing Layer → (abstracted data model) → Oracle database → Application components (Inventory, Topology, Fault, Service Level, Performance Monitoring, Software Image Management) → UI rendering (Dojo).

Ramkrishna's description during the walkthrough: "After you add a device, you give the credentials. You tell how to collect this information by using SNMP, [and] CLI. You can [configure] those credentials aspect. So the information is collected, parsed, and there is a data model where the data is abstracted."

Colin asked whether the application reads from devices or from the database. Ramkrishna: "In most of the cases, it won't directly go to the [device]. It reads from the database, correct." The "in most of the cases" qualifier signals that some operations query devices directly. Which operations is an open item.

### 1.5 Repository inventory (EPNM)

Akhil walked through the EPNM repository layout in the walkthrough. The complete repository list is linked on the Confluence page the Cisco team prepared; the items below are what was called out in the meeting.

- **PI framework repository.** The core UI framework for EPNM. Dojo-based. "The Prime UI and the framework UI, Dojo based." PI likely stands for Prime Infrastructure (the broader product line EPNM descends from).
- **Wireless framework repository (Wireless Repos).** Wireless-specific UI and framework code. Referenced alongside PI framework as part of the EPNM frontend stack.
- **Assembly repository.** Contains the inventory UI screens. Also contains the fault management UI. Akhil: "Assembly is on the UI side"; for faults: "it's backend and frontend, and assembly is on the UI side."
- **ChassisView repository.** Contains the chassis visualization component — the physical device images and chassis layout seen on the Device Details screen.
- **Fault Management repositories.** Referenced as "EPA wireless repo" and "fold" (likely "fault" — speech-to-text artifact). Akhil indicated fault management spans both backend and frontend: "The fault is on the backend... it's backend and frontend, and assembly is on the UI side." Jenis appears to own the fault management backend.

---

## 2. EMS — The Next-Generation Product

### 2.1 Product identity

EMS stands for Element Management System. It is a component of CNC (Crosswork Network Controller), Cisco's next-generation platform. The Crosswork UI is the broader visual language under which EMS screens render.

EMS is not a migrated version of EPNM. The Cisco team was explicit: "It's not exactly migrated in a way. Things got reimplemented. Some of it, at least 80% of it, is there in the other product, as in the newer product." EMS was independently reimplemented with a modern stack. Selva's summary of EMS's functional scope: "EMS is the terminology you would keep hearing, element management system, where you have the inventory, the fault, the performance monitoring, topology links, software image management, the underlay configurations, so on and so forth. So that functionality is what we provide in EMS and a subset of what we have in EPNM."

The critical qualifier: EMS is "a subset of what we have in EPNM." Even with 80-90 percent reimplementation, EMS does not have full feature parity with EPNM.

### 2.2 Frontend

- **Framework:** Angular. Stated as "latest Angular 21" by Praveen and Akhil during the walkthrough.
- **Design system:** Harbor and Magnetic. Praveen's phrasing: "a design system called Harbor and Magnetic design system you're using." Harbor is likely the component library; Magnetic is likely the broader Cisco design language. The exact relationship between the two terms was not clarified and is an open item.
- **Visual branding:** Crosswork UI design language.
- **Architecture:** Three-layer shell-app model (see next section).

### 2.3 Shell-app architecture

The EMS frontend is organized into three nested layers [from the Set 07 walkthrough]:

1. **Infra UI (Shell App).** The outermost layer. Provides the application shell, header bar, top navigation menu, and infrastructure-level UI components (login, layout frame). This is the container that loads and hosts the other layers.

2. **Common UI.** The middle layer. A shared / reusable component library consumed across EMS. Akhil: "If you look at this card, right? These cards and the tables and these things are called common components. So this common component is part of this common UI." Contents include card components, table components, common widgets, and shared design patterns from Harbor / Magnetic.

3. **EMS UI.** The innermost layer. Feature-specific EMS pages. Akhil: "All these EMS related pages like Praveen mentioned about software image management and other things, other pages is part of this repo." Contents include software image management, inventory views, fault management views, device management pages, and the other EMS-specific feature screens.

Akhil also noted that the classic UI should follow this layered pattern and reuse Common UI: "We also use the underlying Crosswork Common UI, right, and that pattern should be picked up from the existing port."

How the shell app loads the EMS UI feature pages (micro-frontend, lazy-loaded Angular modules, or monolithic Angular build) was not described in the walkthrough and is an open item. How Common UI is consumed (npm package, Git submodule, built together) is also open.

### 2.4 Backend

- **Primary framework:** Spring Boot (Java). Akhil when asked: "Mostly Spring Boot, yes."
- **Additional services:** Go services on the device management side specifically. Ramkrishna: "There are areas, at least on the device management side, and there are Go services running at the back end."
- **API layer:** REST APIs serve the Angular frontend.
- **Database:** PostgreSQL. "There's Postgres in the new product. We've gotten rid of Oracle dependency."
- **Device images:** Stored as application assets, not database BLOBs. "For the new UI, it is part of the application, not stored in Oracle and all."

The pattern of Spring Boot on most of the backend with Go carved out for device management is worth holding onto. If the execution session encounters a device-management API that looks different from the Spring Boot patterns seen elsewhere, it is probably a Go service.

### 2.5 Repository inventory (EMS)

**Frontend repos:**

- **Infra UI repository (`ROBOT/infra-ui`).** Shell app. Header, top navigation, infrastructure UI components. Hosts the existing modernized alarms UI at `src/app/robot-alarms-v2/`. Features lazy-load via `src/app/container/robot-shell/robot-shell.routes.ts`. Navigation is data-driven from `src/assets/modules.json` + `src/app/services/module.service.ts`.
- **Common UI repository (`ROBOT/common-ui`).** Shared Angular component library. Cards, tables (`cw-hbr-table`, `ag-grid-table`), 360 shell (`base360/device360/interface360/link360/generic-links`), form primitives (`cui-stepper`, `cui-input`, `cui-select`, `cui-datetime-select`, `cui-modal`), Harbor / Magnetic design patterns.
- **EMS UI repository (`ROBOT/unified-ems-ui`).** Where primary feature pages live (inventory-details, inventory-panel, device-management, interface-list).

> **Open on the EMS UI repo shape (flagged 2026-04-21).** Two readings are on the table, neither yet confirmed by source:
>
> **Reading A — casual walkthrough inference.** The 2026-04-06 walkthrough conversation suggested `unified-ems-ui` is a primary working EMS app where most feature development happens. This framing came from informal shorthand in a speech-to-text transcribed meeting, not from a repo-naming or architecture-spec statement, and should be weighted accordingly.
>
> **Reading B — tree-report inference.** The `poc/REPO/` tree-report swarm (Session 2, 2026-04-21) found the repo has a `projects/ems-lib/` layout with `public-api.ts` and `root-ems.module.ts` as the export surface, and no `main.ts` / `index.html` / root `app.module.ts` at conventional locations — the standard shape of an Angular library consumed by an outer Angular app. Under this reading, `infra-ui` is the app and `unified-ems-ui` is a publishable library the app depends on.
>
> Both readings are inferences. The execution session's first-days investigation (`ng-package.json`, `angular.json projectType`, `infra-ui/package.json` dependencies, import patterns in `robot-shell.routes.ts`) will resolve which reading holds. Doc edits will follow that resolution, not Session 2's tree read. See `_scratch_repo/flags_for_colin_2026-04-21.md` flag 8 for the full framing.

Where classic UI code lives is TBD (see `08_repositories_access_and_compliance.md` for the decision context). The code-organization proposal (action item B2) depends on the library-vs-app resolution above.

**Backend repos:** Corresponding backend repositories exist alongside the frontend repos, using PostgreSQL. **EMS Assurance** is referenced as the fault / alarm / event backend. The `poc/REPO/` bundle includes four EMS-side backend repos the classic UI will call: `cw-inventory`, `cw-inventory-collector`, `cw-epnm-fault`, `ems-assurance`. Any hardware-integration or device-management backend services are out of scope for this engagement — the POC is a UI reskin against existing EMS REST APIs, not a re-architecture of the backend stack.

---

## 3. What the 2026-04-06 Walkthrough Demonstrated

Akhil ran live product demos during the walkthrough. What follows is what the execution session should expect to encounter when it first opens the EPNM codebase and looks at the screens in scope. All entries are from the research files on the Set 07 walkthrough; details that were not enumerated are flagged as open.

### 3.1 Navigation patterns

- EPNM: Left-side navigation tree. Inventory → Network Devices and Monitor → Alarms and Events are the two primary navigation paths for the POC.
- EMS: Header bar and top menu served from Infra UI. EMS UI feature pages are reached through this top-level navigation. Exact navigation tree to reach the equivalent Inventory and Fault Management screens in EMS is something the execution session will map during its code deep dive.

### 3.2 Inventory screens

What Akhil demonstrated on EPNM:

- **Network Devices:** A table listing devices. Left filter panel (All devices, by device type, by locations, by group and sites). Toolbar with a device-add wizard (IP address first, then a step-forward flow requesting protocol credentials — SNMP, Telnet, HTTP, HTTPS, and others). Bulk import via downloadable CSV template and upload. Basic table actions (edit, delete). Device state operations (set to admin state, maintain state, manage state, schedule maintain state, schedule managed state, disable handler inventory). Additional actions: export device, new box certificate, OEM commands.
- **Device Details:** Opened by clicking a device name (hyperlinked in the Network Devices table). Chassis View on the left. Main area shows the view selected from a left-side menu. Left-menu views included system summary view, device details, chassis and enrollment, and others that were not fully enumerated.
- **Chassis View:** Visual representation of the device hardware — modules, ports, layout. In EPNM, device images are Oracle-stored. In EMS, they are bundled with the application.
- **Device 360:** A popup launched from an info icon in the Network Devices table. Also launchable from other screens (alarms, other windows). Tabs include Alarms, Modules, Interfaces, Location, Recent changes. Actions menu includes Device console.
- **Interface 360:** A second-level popup launched from the Interfaces tab of Device 360. A 360 view inside a 360 view. The nesting pattern must be preserved in the Angular rebuild.

### 3.3 Fault Management screens

What Akhil demonstrated:

- **Alarms table:** Reached via Monitor → Alarms and Events. Same table pattern as Network Devices. Column picker on the right. Quick filter and advanced filter. Row-expandable — every row can open inline to show general information and additional detail. Clear-alarm action (confirmed by Jenis). Other actions described as "similar to the network devices."
- **Correlated alarms:** Multiple related alarms grouped under a root cause. Viewable from the alarms table itself and within the Device 360 alarms tab. The visual representation (tree, grouped rows, correlation panel) was not detailed in the walkthrough.
- **Events:** A most-recent-events popup accessible from the alarms screen. Time-based presets including "past 8 hours" and "all events." A full events page as a secondary table, distinct from the alarms table.
- **Syslogs:** A third data type alongside alarms and events. No UI detail was provided in the walkthrough; this is genuinely under-documented.

### 3.4 Toggle behavior

Akhil on the default behavior:

- Default on login: EPNM theme (blue and white, Dojo-style layout).
- After toggling: Magnetic design system (current EMS visual language).
- Toggle switches the entire visual experience for that screen, not individual components.

### 3.5 What the walkthrough did not enumerate

Open items the execution session will need to resolve (full list in `10_open_questions_and_risks.md`):

- Complete Device Details left-menu enumeration.
- Complete Device 360 action set (beyond Device Console).
- Interface 360 structure (same tabs as Device 360, or different).
- Bulk-import CSV schema.
- Device-add wizard step-by-step field breakdown.
- State-management scheduling UI (time picker, scheduling controls for "schedule maintain state").
- Chassis View interactivity (whether the interactive component — module clicks, port state interactions — is in the 80 percent reimplemented or part of the gap).
- Complete alarms table column set.
- Alarms advanced filter criteria, operators, saved filter capabilities.
- Severity-based row coloring in the alarms table.
- Cross-navigation between alarms, events, and syslogs.
- Alarm real-time update mechanism (auto-refresh, polling, push).
- Full alarm action set beyond clear-alarm (acknowledge, annotate, assign, suppress, create trouble ticket).
- Syslog UI layout and filtering.

---

## 4. The 80 Percent Backend Coverage and the Gap

Ramkrishna's statement is the anchor: "Some of it, at least 80% of it, is there in the other product, as in the newer product." The "at least" is deliberate — the team believes coverage is higher than 80 percent but prefers a conservative figure.

Colin's commitment on the gap: "There will be a gap analysis. So we'll look for, you know, if there's anything critical that's missing and then those things that maybe, you know, that 10% that's remaining that might not be migrated or might not be compatibly migrated, we'll be able to flag that."

Praveen's guidance on handling gaps when they are found: "In the instance where potentially the new backend is not there, then... We need to consider adding equivalent functionality in the new [product] rather than just bringing over the whole old thing. That's too bulky to bring here and that's not the approach we're taking."

For the POC, gap analysis applies only to the two screens in scope. The execution session should be prepared to find that some EPNM features do not have direct EMS equivalents. When that happens:
- If the gap is narrow (API shape difference, missing filter parameter, response field adjustment), the narrow API touchup exception applies and the execution session can proceed.
- If the gap is broader (entire backend capability not present in EMS), the guidance is to flag to Selva rather than reimplement the old backend. Per Praveen and Selva, the direction is to add equivalent functionality to the new product (EMS backend) over time, not bring EPNM's backend forward.

---

## 5. Data Flow in EMS Versus EPNM

Both products follow the same basic pattern — device polling into a data collection layer, persisted to a database, read by applications, rendered by UI — but with different implementations:

| Step | EPNM | EMS |
|------|------|-----|
| Device polling | SNMP, CLI | SNMP, CLI |
| Data collection / parsing | Java monolith | Spring Boot services, Go services (device management) |
| Persistence | Oracle | PostgreSQL |
| Application consumption | Java backend components → internal data access | REST APIs → backend services → database |
| UI rendering | Dojo / Dijit | Angular 21 + Harbor / Magnetic |
| Device images | Oracle | Application assets |

Because the backend is untouched in the POC, the EMS data flow is inherited unchanged. The POC's scope is entirely in the Angular frontend layer, calling the existing EMS REST APIs.

---

## 6. What the Execution Session Should Read Before Writing Code

In approximate priority order:

1. The Confluence page the Cisco team has prepared — links to repos, user guides, recordings of EPNM device onboarding and the Inventory / Device Details walkthrough, API documentation for both products.
2. The EPNM code for the Inventory screens (Assembly repo, ChassisView repo, PI framework) and Fault Management (EPA wireless repo and the backend counterparts).
3. The EMS code for the equivalent screens in the EMS UI repo, plus the Common UI and Infra UI repos to understand the shell integration.
4. The Set 08 research files in `cisco/epnm_ems/research/`: `08_research_epnm_legacy_stack_2026-04-07.md`, `08_research_ems_modern_stack_2026-04-07.md`, and `08_research_conversion_patterns_2026-04-07.md`. Their content is restated as a reference in `06_conversion_patterns_reference.md` in this handoff.
5. Existing Cisco regression test suites for Inventory and Fault Management (relevant files or specifications) — to understand what functional coverage the classic UI needs to preserve. Acquisition of these is pending and is an action item.

---

## Footer — Update Log

- **2026-04-21 (Session 2).** §2.5 EMS repo inventory: added the library-vs-app ambiguity on `unified-ems-ui`. Both walkthrough-inference and tree-report-inference readings are now presented as equal-weight, unresolved. Resolution goes to the execution session's first-days source read. Added named evidence for `infra-ui` feature-loading pattern and `common-ui` primitive catalog from the 2026-04-21 tree-report swarm.
