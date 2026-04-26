# 06 — Conversion Patterns Reference

**Purpose of this document:** A working-desk reference for the Dojo-to-Angular conversion patterns the execution session will apply. Summarizes the critical patterns and points to the deep technical content that lives in the Set 08 research files. The research files are the source of truth for details; this document is the navigable overview.

**Primary source files:**
- `cisco/epnm_ems/research/08_research_epnm_legacy_stack_2026-04-07.md`
- `cisco/epnm_ems/research/08_research_ems_modern_stack_2026-04-07.md`
- `cisco/epnm_ems/research/08_research_conversion_patterns_2026-04-07.md`

Open these files directly when working on any of the patterns below. The execution session should treat them as the canonical reference.

---

## 1. The Big Picture

The work is a Dojo 1.x to Angular 21 presentation rewrite. The EMS backend stays untouched. Both the classic view and the existing modern EMS view will call the same Spring Boot and Go REST APIs against the same PostgreSQL database. Display differences are adapted on the Angular side.

Three pattern families matter most:

1. **Widget-to-component mapping.** Dojo Dijit widgets map to Angular Material components.
2. **Theme toggle architecture.** CSS custom properties plus a signal-based `ThemeService` plus a toggle component placed in the Infra UI shell header.
3. **Shared services with display adapters.** One service layer calls the EMS API; classic view components reformat the response through adapters.

Everything else flows from these three.

---

## 2. Widget Mapping (Dojo → Angular Material)

The complete 25-row mapping table is in `08_research_conversion_patterns_2026-04-07.md` Section 1.5. Summary of the mappings the execution session will use most often:

| Dojo Widget | Angular Equivalent |
|---|---|
| `dojox/grid/DataGrid` | `mat-table` + `MatSort` + `MatPaginator` |
| `dgrid/Grid` | `mat-table` |
| `dijit/Dialog` | `MatDialog.open()` |
| `dijit/TooltipDialog` | `MatMenu` or `cdkOverlayOrigin` |
| `dijit/Tree` | `MatTree` / `CdkTree` |
| `dijit/form/TextBox` | `<input matInput>` + `FormControl` |
| `dijit/form/ValidationTextBox` | `FormControl` + `Validators` |
| `dijit/form/FilteringSelect` | `<mat-select>` or `<mat-autocomplete>` |
| `dijit/form/ComboBox` | `<mat-autocomplete>` with free text |
| `dijit/form/Select` | `<mat-select>` |
| `dijit/form/CheckBox` | `<mat-checkbox>` |
| `dijit/form/RadioButton` | `<mat-radio-group>` + `<mat-radio-button>` |
| `dijit/form/NumberSpinner` | `<input matInput type="number">` |
| `dijit/form/DateTextBox` | `<mat-datepicker>` |
| `dijit/form/Button` | `<button mat-button>` or `<button mat-raised-button>` |
| `dijit/ProgressBar` | `<mat-progress-bar>` |
| `dijit/TabContainer` | `<mat-tab-group>` + `<mat-tab>` |
| `dijit/layout/ContentPane` | Angular component with `<ng-content>` |
| `dijit/layout/BorderContainer` | CSS Grid or Flexbox |
| `dijit/layout/AccordionContainer` | `<mat-accordion>` + `<mat-expansion-panel>` |
| `dijit/Toolbar` | `<mat-toolbar>` |
| `dijit/Menu` / `dijit/MenuItem` | `<mat-menu>` + `<mat-menu-item>` |
| `dijit/Tooltip` | `matTooltip` directive |
| `dojox/widget/Toaster` | `MatSnackBar` |

Full conversion examples for DataGrid, Dialog, Tree, and the form widget families are in Section 3 of `08_research_conversion_patterns_2026-04-07.md`.

---

## 3. AMD → ES6 Module Translation

Dojo uses AMD via `define()` and `require()`. Angular 21 uses ES6 modules with `import`/`export`. The mechanical transformation is straightforward:

- `define([deps], factory)` → `import { name } from 'path';` followed by class or function exports.
- `require([deps], callback)` → `import` plus direct invocation.
- `dojo/text!./templates/X.html` → move template to component `templateUrl` or inline `template`.
- Older `dojo.provide()` / `dojo.require()` code may also appear — same destination, different start.

An automated tool (`amd-to-es6`) handles the mechanical transformation but does not handle Dojo-specific patterns like `declare()`, `this.inherited()`, or the Dijit widget lifecycle. Plan on manual rewrite for anything that touches those.

Detail in Section 2 of the conversion patterns file.

---

## 4. Data Binding, Event Handling, Lifecycle

### Data binding

| Dojo | Angular |
|---|---|
| `dojo/aspect` `watch(prop, callback)` | Angular signals or `@Input()` change detection with `BehaviorSubject` |
| Dojo template `${property}` (one-time) | Angular `{{ expression }}` (reactive) |
| Dojo `set(prop, value)` / getter-setter | Signals (`sig.set(...)`) or two-way `[(ngModel)]` |

### Event handling

| Dojo | Angular |
|---|---|
| `dojo/on(node, "click", handler)` | `(click)="handler()"` template binding |
| `dojo/topic.publish("topic", data)` | RxJS `Subject.next(data)` via a shared event-bus service |
| `dojo/topic.subscribe("topic", handler)` | RxJS `Subject.subscribe()` |

The `dojo/topic` pub/sub is the invisible dependency web. There is no import chain, no compile-time coupling, and no structural signal that two widgets depend on each other. Every `topic.publish` and `topic.subscribe` call in the EPNM code should be cataloged during analysis so the implicit contract is reproduced explicitly in RxJS subjects on the Angular side.

### Widget lifecycle

| Dijit method | Angular hook | Notes |
|---|---|---|
| `constructor` | `constructor` | Property initialization |
| `postMixInProperties` | `constructor` (after super) | Pre-DOM property computation |
| `buildRendering` | (automatic; handled by template) | Template-driven rendering |
| `postCreate` | `ngOnInit` and `ngAfterViewInit` | **Most important.** Event binding, data loading, refs to child components. Start analysis here for any Dijit widget. |
| `startup` | `ngAfterViewInit` | Layout, child startup |
| `destroy` | `ngOnDestroy` | Cleanup, unsubscribe, disconnect |

Detail in Sections 3, 4, and 5 of the conversion patterns file.

---

## 5. State Management (Stores → Services)

Dojo `dojo/store` maps to Angular services using `HttpClient` for REST-backed data and `BehaviorSubject` for in-memory state. Concrete mappings:

| Dojo Store | Angular Equivalent |
|---|---|
| `dojo/store/Memory` | Service with `BehaviorSubject<T[]>` |
| `dojo/store/JsonRest` | Service with `HttpClient` |
| `dojo/store/Cache` | Service with `BehaviorSubject` + `HttpClient` + cache logic |
| `dojo/store/Observable` | `BehaviorSubject` (inherently observable) |

For the POC, the critical point is: **the Angular services call the EMS REST APIs, not any EPNM API.** Classic view code never talks to Oracle, never talks to the Java monolith. It reads from the same PostgreSQL-backed Spring Boot / Go services that the modern UX reads from. Any shape differences between what EPNM displays and what EMS returns are adapted on the Angular side, not resolved by calling different backends.

Detail in Section 6 of the conversion patterns file.

---

## 6. Theme Toggle Architecture (the Central POC Mechanism)

### Naming note (2026-04-21 update)

Internal code and CSS tokens use the prefix **`epnm-classic`** rather than bare `classic`, because `classic` is already a Magnetic tier name inside the EMS codebase (`infra-ui/src/css/magnetic-light-classic.scss`, `magnetic-dark-classic.scss`). The distinct prefix prevents collisions and makes it unambiguous that our reskin ties to EPNM.

User-facing toggle labels stay "Classic" and "Modern" per Akhil's walkthrough direction — the prefix affects code, CSS tokens, data attributes, and folder names only.

### Approach

CSS custom properties on the document root plus a signal-based `ThemeService` plus a toggle component placed in the Infra UI shell header. Toggle flips a `data-theme` attribute on `document.documentElement`. All styled components read theme variables through `var(--theme-...)` and automatically re-render. No page reload.

### Default mode

`epnm-classic` is the default. The EPNM-style experience is what the user sees on login. The toggle flips to `magnetic` (the current EMS visual language).

### Key pieces

**1. CSS custom properties for each theme.** Two palettes defined as CSS variables on `:root[data-theme="epnm-classic"]` and `:root[data-theme="magnetic"]`. EPNM classic palette covers dark blue primary, blue/white surface colors, Segoe UI font family, 2px border radius. Magnetic palette covers the current Crosswork UI tokens (CiscoSans font, 8px border radius, darker surfaces).

**2. A `ThemeService` using Angular signals.** Provides a `currentTheme` signal, a `toggle()` method, reads and writes `localStorage` for persistence, and uses an `effect()` to write the `data-theme` attribute on `document.documentElement` whenever the signal changes.

**3. A `<app-theme-toggle>` component.** Placed in the Infra UI shell header. Binds to the `ThemeService` signal. Uses `<mat-slide-toggle>` with "Classic" and "Modern" labels.

**4. Conditional component rendering for screens with fundamentally different layouts.** Container component reads `ThemeService.currentTheme()` and renders `<app-network-devices-classic />` or `<app-network-devices-modern />` accordingly.

Full code (theme palettes, ThemeService implementation, toggle component, conditional rendering pattern, theming decision matrix) is in Section 7 of the conversion patterns file and preserved at length in `_scratch/agent_07_set08_research.md`.

### Toggle placement for the POC versus the product

The POC is local per-screen. Each POC screen (Inventory views + Fault Management views) has its own embedded toggle. The global header toggle is the product-level pattern, deferred post-POC. For the POC, keep the toggle component on each page rather than hoisting it to the shell. This aligns with Selva's explicit direction: "We will do local toggle... we'll just add a toggle to that very same page and say once you toggle it gives me the classic."

---

## 7. API Integration and Display Adapters

### The principle

One service layer. Both classic and modern views consume it. Classic view components apply formatting transformations through adapter classes to reshape EMS API responses into the EPNM-display format the classic UX expects.

### Pattern

```text
  EMS REST APIs (Spring Boot + Go, PostgreSQL)
        ↓
  Shared Angular service (HttpClient)
        ↓
        ├── Modern components (display as-is or via Magnetic conventions)
        └── Classic components (apply EpnmDisplayAdapter)
```

### Example adapter responsibilities

- EMS enum `"MANAGED"` → classic label `"Managed"` or `"In Maintenance"`.
- EMS enum `"CISCO_ASR_9000"` → classic label `"Cisco ASR 9000 Series"`.
- EMS ISO 8601 timestamp → classic format `"Mar 25, 2026 14:30:22 PDT"`.

Full adapter pattern with service implementation and usage in components is in Section 8 of the conversion patterns file.

### API gap table

Features to verify exist in EMS before building the classic UI around them:

| EPNM Feature | What EMS needs |
|---|---|
| Device count in left filter panel | Faceted counts by device type, location (check for aggregation endpoint) |
| Chassis view images | Application assets — confirmed available, low risk |
| Device 360 alarm count badge | Device endpoint returns alarm summary (check) |
| Export device (CSV) | Export endpoint or client-side generation |
| Bulk import (CSV) | Multipart file upload endpoint |
| OEM commands execution | Command dispatch endpoint — likely in the 20 percent gap, verify |
| Scheduling (maintain / managed state) | Scheduled state transition endpoints — may require new backend work |

Items that fall into the gap follow the two paths defined in Section 5 of `03_objectives_and_scope.md`: narrow API touchup if small, flag to Selva if broader.

---

## 8. Shell App Integration

### Current architecture

```
Infra UI (Shell App — outermost)
  └── Header bar, top navigation, login, layout frame
  └── Common UI (shared component library, Harbor/Magnetic)
        └── Cards, tables, design system widgets
  └── EMS UI (feature pages loaded into shell content area)
        └── Inventory views
        └── Fault management views
        └── Other feature pages
```

### Where classic view code lives

Location decision is open. Akhil's two options: a subfolder inside the EMS UI repository or a dedicated new repository. The firm constraint: must build as part of the EMS build. Colin owes a proposal on this. Whichever choice is made, the folder structure laid out below is proposed for the content itself.

### Proposed folder structure (inside EMS UI repo or a new repo)

Updated 2026-04-21 to use the `epnm-classic` prefix (see §6 naming note).

```
ems-ui/
  src/
    app/
      epnm-classic/
        components/
          network-devices-classic/
          device-360-classic/
          device-details-classic/
          chassis-view-classic/
          alarm-list-classic/
        adapters/
          epnm-display.adapter.ts
        styles/
          _epnm-classic.scss
          _epnm-components.scss
          _epnm-layout.scss
        shared/
          epnm-left-nav/
          epnm-toolbar/
          epnm-filter-panel/
      modern/
        components/
          (existing Magnetic/Harbor components)
      shared/
        services/
          inventory.service.ts
          alarm.service.ts
          theme.service.ts
          event-bus.service.ts
        models/
          network-device.model.ts
          alarm.model.ts
          device-360.model.ts
        containers/
          inventory-view.component.ts
          fault-view.component.ts
```

The `epnm-classic/` folder is the entire POC surface. Component files inside keep the `-classic` suffix because they are already namespaced by the folder (no collision risk once inside `epnm-classic/`). Shared infrastructure (services, models, containers) lives under `shared/` so both classic and modern views consume the same service layer.

### Routing strategy

Two options laid out in Section 9.3 of the conversion patterns file:

- **Option A (recommended for POC).** Dual routes with container component. URL stays the same regardless of theme. Container component reads `ThemeService.currentTheme()` and renders the classic or modern inner component. Simpler. No route re-evaluation on toggle.
- **Option B.** Route guards with theme-aware loading using `canMatch` functions that check theme state. Fits better if the team already uses `canMatch` patterns.

### Common UI reuse policy

1. Reuse Common UI structural components where they can be themed via CSS custom properties (card containers, layout grids).
2. Do NOT reuse Common UI components tightly coupled to Magnetic (Magnetic-specific buttons, Harbor typography).
3. Create classic-specific wrapper components that use the same data patterns but render with EPNM styling.

### Build integration

The constraint from Set 07 is firm: "It has to be part of the new EMS build." Classic code ships in the same build artifact as modern EMS UI. No separate deployment. Lazy-loading the classic module is advised to keep the initial bundle size reasonable.

Detail in Section 9 of the conversion patterns file.

---

## 9. Per-Screen Migration Checklist

Preserved verbatim from Section 10 of `08_research_conversion_patterns_2026-04-07.md`. Apply this checklist to each screen in scope.

### Step 1: Analyze the EPNM screen

- [ ] Identify all Dojo widgets used (DataGrid, Dialog, Tree, form widgets)
- [ ] Document the data flow (what API or store does it call?)
- [ ] Map the layout structure (BorderContainer, ContentPane, TabContainer)
- [ ] Note all user interactions (click handlers, context menus, keyboard shortcuts)
- [ ] Capture the visual design (colors, fonts, spacing, borders)

### Step 2: Identify the EMS API endpoints

- [ ] Find the equivalent EMS REST API for each data source
- [ ] Compare the EPNM data fields with EMS API response fields
- [ ] Document any gaps (fields present in EPNM but absent from EMS API)
- [ ] Note any data format differences requiring adapter transformation

### Step 3: Create the Angular component

- [ ] Map Dojo widgets to Angular Material components (Section 2 above)
- [ ] Convert AMD modules to ES6 imports (Section 3 above)
- [ ] Replace Dojo data binding with Angular binding patterns (Section 4 above)
- [ ] Replace Dojo event handling with Angular patterns (Section 4 above)
- [ ] Map lifecycle methods (Section 4 above)
- [ ] Create or reuse Angular services for state management (Section 5 above)

### Step 4: Apply EPNM theming

- [ ] Use CSS custom properties for theme-responsive styling (Section 6 above)
- [ ] Apply EPNM-specific class names for structural differences
- [ ] Test that the component renders correctly in both classic and modern themes

### Step 5: Integrate with shell app

- [ ] Add component to the appropriate routing configuration
- [ ] Wire up the theme-switching container component (Section 8 above)
- [ ] Verify component renders within the Infra UI shell
- [ ] Test toggle between classic and modern views

---

## 10. Named Conversion Risks

Curated from all three Set 08 research files. These are the failure modes the research flagged. The execution session should anticipate them.

### From the EPNM legacy stack

1. **Undocumented behavior in a 15+ year monolith.** Quirks in sorting, filtering, data transformation buried in widget code, service layer, or Oracle stored procedures. No design documentation exists (confirmed by Selva in Set 02).
2. **Custom widget complexity.** EPNM custom Dijit widgets have accumulated conditional rendering, device-type special cases, browser workarounds. Plan for these to be non-trivial.
3. **Pub/sub dependency web.** `dojo/topic` creates invisible coupling between widgets. Must be mapped manually; there is no compile-time signal.
4. **Data shape mismatches.** EPNM API and EMS API almost certainly return different JSON structures (field names, nesting, pagination, error formats).
5. **Oracle-to-PostgreSQL data gaps.** The 10-20 percent backend gap may touch POC screens.
6. **Device-type-specific logic.** IOS vs IOS-XR vs NX-OS parsing, chassis layout differences, interface naming conventions.

### From the EMS modern stack

- **Harbor / Magnetic relationship is ambiguous.** Open question from Set 07 whether they are two layers of one system or distinct systems. Affects whether classic view can reuse Common UI components.
- **Go service integration is not fully characterized.** Which endpoints are Go versus Spring Boot; whether the frontend calls Go directly or only through Spring Boot.
- **PostgreSQL timezone behavior differs from Oracle SYSDATE.** UTC storage with display-time conversion. Adapters must handle this.
- **PostgreSQL NULL handling differs from Oracle.** Postgres distinguishes empty string from NULL where Oracle treats them equivalently. Ported query behavior may shift.

### From the conversion patterns research

- **Toggle state persistence decision affects cross-device and cross-session UX.** Local storage, user preference API, or URL parameter — each has tradeoffs. Open for POC.
- **Bundle size.** Classic view adds to the EMS UI bundle. Lazy-load the classic module so it only loads when selected.
- **AMD-to-ES6 automated tooling is mechanical only.** Handles imports but not `declare()`, `this.inherited()`, or Dijit lifecycle. Plan for manual work.

---

## 11. What to Read in Order

If the execution session is starting on a specific screen, the read order that maximizes signal:

1. The EPNM source of that screen in the assembly repo (for Inventory) or EPA wireless repo / fault repos (for Fault Management).
2. Corresponding EMS screen in the EMS UI repo — how the modern version is built.
3. Section 1 of `08_research_epnm_legacy_stack_2026-04-07.md` for Dojo primitives encountered.
4. Section 2 of `08_research_ems_modern_stack_2026-04-07.md` for Angular 21 primitives used in EMS.
5. `08_research_conversion_patterns_2026-04-07.md` Sections 1 through 10 — the per-screen checklist and mapping material.
6. This handoff document as the connective tissue between research detail and POC scope.

Keep research files open while working. Do not try to remember the mapping tables from memory; reference them.

---

## Footer — Update Log

- **2026-04-21 (Session 2).** Updated §6 and §8 to use the prefix `epnm-classic` instead of bare `classic`, because the word `classic` is already used as a tier name inside the existing Magnetic design system (`infra-ui/src/css/magnetic-light-classic.scss`). Distinct prefix avoids collision. User-facing toggle labels unchanged ("Classic" / "Modern"). No other sections affected.
