# Agent 08 — EMS `common-ui` Tree Report Extraction

**Source file:** `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/common-ui_tree_report.md`
**Repo:** `common-ui` — 1,604 text files, 293 directories, 240,466 raw lines.
**POC scope:** Inventory and Fault Management (alarms table, network-devices table, Device 360, Interface 360, wizard-step form controls).

---

## 1. Repo Shape at a Glance

Top-level directories under `common-ui/`:

- `.github/` — CodeGuard instruction set (security/quality Copilot prompts) plus `copilot-instructions.md`.
- `.husky/` — `pre-commit` hook (91 lines).
- `custom-eslint-rules/` — in-repo ESLint rule package (`hard-coded-string`, `max-params`, `no-commented-code`, `no-deprecated-methods`).
- `projects/cw-lib/` — the Angular library itself (all shared components live here).
- `scripts/` — `run_test.sh`, `verifytools.sh`.

Root files of note: `angular.json`, `package.json` (128 lines), `package-lock.json` (24,487 lines), `rollup.config.js`, `tsconfig.json`, `Jenkinsfile` (244 lines), `build.sh` (216 lines), `common-component-creation-template.md` (161 lines — component-authoring template), `i18n-verifier.js`, `PULL_REQUEST_TEMPLATE.md`.

Inside `projects/cw-lib/`:
- `assets/` — i18n (`en.json` 2,985 lines, `ja.json` 2,998 lines) plus SVG icon sets (checkboxes, radios, status icons, device card SVGs, topology glyphs).
- `scss/` — `ag-grid/styles/` (ag-grid themes — see §3), `tree/styles/`, `spicons.css` (612 lines — icon font), `styles.css`.
- `src/core/` — auth, router, navigation-menu, license-info services.
- `src/cwcomponents/` — **the shared component catalog** (see §2).
- `src/shared/` — API services (v1/v2), directives, pipes, services, `shared.module.ts` (231 lines).
- `src/public-api.ts` (673 lines) — the library's exported barrel.
- Build/package files: `ng-package.json`, `package.json`, `public-api.ts`, `tsconfig.lib.json`, `tsconfig.spec.json`, `karma.conf.js`, `patch_version_cw.js`.

---

## 2. Component Catalog

The shared catalog lives under `projects/cw-lib/src/cwcomponents/`. Distinct component directories observed (grouped by apparent role):

**Fusion-era primitives** (legacy Fusion naming; pre-CUI baseline): `button/`, `checkbox/`, `dialog/`, `notification-toaster/`, `popover/`, `progressbar/`, `searchbar/`, `selectbox/`, `switch/`, `textbox/`, `tooltip/`, `validationbox/`.

**CUI family** (Cisco UI — the modern prefix, ~40 components): `cui/cui-ag-grid-action-item/`, `cui/cui-ag-grid-actions/`, `cui/cui-badge/`, `cui/cui-button/`, `cui/cui-carousel/`, `cui/cui-checkbox/`, `cui/cui-checkbox-group/`, `cui/cui-copytoclipboard/`, `cui/cui-datetime-select/`, `cui/cui-datetime-select-action/`, `cui/cui-days/`, `cui/cui-drawer/`, `cui/cui-empty-box/`, `cui/cui-gauge/`, `cui/cui-gear-dropdown/`, `cui/cui-import-progressbar/`, `cui/cui-info-icon/`, `cui/cui-input/`, `cui/cui-input-file/`, `cui/cui-modal/`, `cui/cui-notification/`, `cui/cui-popover/`, `cui/cui-popover-action/`, `cui/cui-popover-wrapper/`, `cui/cui-progressbar/`, `cui/cui-radio/`, `cui/cui-radio-group/`, `cui/cui-radio-switch/`, `cui/cui-select/`, `cui/cui-select-action/`, `cui/cui-select-hbr-vs/`, `cui/cui-splitter/`, `cui/cui-stepper/`, `cui/cui-success/`, `cui/cui-tag/`, `cui/cui-tag-filter/`, `cui/cui-tags-device/`, `cui/cui-text-link/`, `cui/cui-time-picker/`, `cui/cui-tooltip/`.

**CW family** (Crosswork-specific composites, Harbor-themed): `cui/cw-button-group/`, `cui/cw-date-picker/`, `cui/cw-footer/`, `cui/cw-hbr-card/`, `cui/cw-hbr-dropdown/`, `cui/cw-hbr-icon/`, `cui/cw-hbr-stepper/`, `cui/cw-menu-hbr/`, `cui/cw-select/`, `cui/cw-sticky-action-bar/`, `cui/cw-timeline/`, `cui/hbr-dropdown-cascading-menu/`, `cui/hbr-select-add/`.

**Domain composites** (inventory/fault-relevant): `alarms/`, `base360/` (with `device360/`, `interface360/`, `link360/`, `generic-links/`), `breadcrumb/`, `cards/`, `carousel/`, `clear-filter/`, `custom-monaco-editor/`, `custom-views/` (saved-custom-views, save-custom-view, custom-views-notifications), `cw-card-page-layout/`, `cw-dashboard/` (add-dashboard, add-dashlet-drawer, dashlet), `cw-date-range-picker/`, `cw-empty-state/`, `cw-filter-form/`, `cw-global-search/`, `cw-hbr-bar-chart/`, `cw-hbr-donut/`, `cw-hbr-line-chart/`, `cw-hbr-progress-ring/`, `cw-hbr-select-tags/`, `cw-hbr-table/`, `cw-heat-map/`, `cw-history-timestamp/`, `cw-inline-notification/`, `cw-menu-divider/`, `cw-notifications/`, `cw-pagination/`, `cw-sankey-chart/`, `cw-spinner/`, `cw-tree/`, `generic-topology-map/`, `groups-manager/`, `groups-tree/`, `infinite-scroller/`, `key-value/`, `modal-dialog/`, `nav-tabs/`, `ngx-nestable-comp/`, `notification-destination/`, `onboarding/steps-panel/`, `orderable-list/`, `panel/`, `panel-toggle/`, `panel-toggle-device/`, `pendingChangesGuard/`, `select-virtualscroll/`, `settings/`, `side-panel/`, `status-card/`, `tabs-container/`, `tag-filter/`, `topology/`, `topology-dashlet/`, `topology-metrics-links-dashlet/`, `unified/`, `unitfied-topology/` (sic), `virtual-domain/`, `virtual-domain-tree/`.

**Ag-grid plumbing:** `ag-grid-custom-filters/` (datetime, multi-select, multi-select-icon, select, select-icon), `ag-grid-custom-header/`, `ag-grid-custom-header-select-all/`, `ag-grid-custom-header-select-all-3-icon/`, `ag-grid-table/`.

**Advanced export wizard family** (alarm/inventory/performance-policy export): `advanced-export/` with sub-forms `alarm-export-form/`, `generic-export-form/`, `inventory-export-form/`, `performance-policy-export-form/`, plus shared `adv-export-file-selector/`, `adv-export-scheduling/`, `cui-device-group-picker/`.

**Dropdown legacy:** `angular2-multiselect-dropdown/`.

---

## 3. Table / Data-Grid Components (highest-value reuse candidates)

The walkthrough called out alarms table + network-devices table as common-UI-based. Cite-worthy paths:

- **`projects/cw-lib/src/cwcomponents/cw-hbr-table/`** — the Harbor-branded workhorse table. Size is the tell: `cw-hbr-table.component.ts` (1,566 lines), `cw-hbr-table.component.spec.ts` (2,906 lines), `cw-hbr-table.component.html` (224 lines), `cw-hbr-table.component.scss` (232 lines), `cw-hbr-table-config.interface.ts` (151 lines), `cw-hbr-table.module.ts` (43 lines). Subfolders: `cw-table-filter/`, `helper/cw-hbr-helper.service.ts`, `table-loading-skeleton/`, plus `ActionMenuComponent.ts`. **This is the component that `alarms/alarms.component.ts` (760 lines) and the topology device-table use.**
- **`projects/cw-lib/src/cwcomponents/ag-grid-table/ag-grid-table.component.ts`** (453 lines) — the alternate ag-grid-based shared table. `ag-grid-table.component.html` (232 lines), `.scss` (122 lines).
- **Ag-grid ecosystem** (filter chrome + headers used by both tables):
  - `ag-grid-custom-filters/ag-grid-datetime-custom-filter/`
  - `ag-grid-custom-filters/multi-select/`
  - `ag-grid-custom-filters/multi-select-icon/`
  - `ag-grid-custom-filters/select/`
  - `ag-grid-custom-filters/select-icon/`
  - `ag-grid-custom-filters/ag-grid-disabled-filter.ts`
  - `ag-grid-custom-header/ag-grid-custom-header.component.ts`
  - `ag-grid-custom-header-select-all/`
  - `ag-grid-custom-header-select-all-3-icon/`
- **Ag-grid theming:** `projects/cw-lib/scss/ag-grid/styles/ag-grid-themes.scss` (657 lines), `ag-grid.css` (885 lines), plus `theme-blue.css`, `theme-bootstrap.css`, `theme-dark.css`, `theme-fresh.css`, `theme-fresh-custom.css` (631 lines), `theme-material.css`. **Multiple themes already exist — precedent for adding a classic theme.**
- **Ag-grid support services:** `projects/cw-lib/src/shared/services/aggrid-accessibility.services.ts` (559 lines), `aggrid-floating-filter.service.ts`, `cell-renderer-utils.ts`, `hbr-table.service.ts`, `icon-render.service.ts` (1,279 lines).
- **Alarms table composite:** `projects/cw-lib/src/cwcomponents/alarms/alarms.component.ts` (760 lines), `.html` (48 lines), `.scss` (187 lines), `alarms.service.ts` (196 lines), `alarms.constants.ts` (152 lines).
- **Network-devices table (topology panel):** `projects/cw-lib/src/cwcomponents/topology/topology-unified-view/topology-panel/device-table/topology-device-table.component.ts` (1,050 lines).
- **Groups device table:** `projects/cw-lib/src/cwcomponents/groups-manager/groups-device-table/groups-device-table.component.ts` (720 lines).
- **Links table:** `projects/cw-lib/src/cwcomponents/topology/topology-unified-view/links-table/links-table.component.ts` (96 lines).

---

## 4. Card Components

- `projects/cw-lib/src/cwcomponents/cards/` — the primitive card: `card.compoent.ts` (sic — typo in filename, 36 lines), `card.component.spec.ts` (96 lines), `card.css` (176 lines), `card.html` (47 lines), `card.module.ts` (23 lines).
- `projects/cw-lib/src/cwcomponents/cui/cw-hbr-card/` — Harbor-themed card: `cw-hbr-card.component.ts` (100 lines), `.html` (107 lines), `.scss` (101 lines), `.module.ts`.
- `projects/cw-lib/src/cwcomponents/status-card/` — status-display card (`status-card.component.ts` 29 lines, `.html` 27, `.scss` 55).
- `projects/cw-lib/src/cwcomponents/cw-card-page-layout/` — page layout built around cards (`cw-card-page-layout.component.ts` 19 lines).
- Dashboard cards: `projects/cw-lib/src/cwcomponents/cw-dashboard/dashlet/dashlet.component.ts` (409 lines) — the tile/card used in the dashboard grid.

---

## 5. Form Controls (wizard-step building blocks)

Inputs:
- `cui/cui-input/cui-input.component.ts` (369 lines), `.html` (209), `.scss` (254), `.spec.ts` (498).
- `cui/cui-input-file/cui-input-file.component.ts` (168 lines).
- `textbox/fusion-textbox.component.ts` (94 lines) — legacy Fusion textbox.

Selects / dropdowns:
- `cui/cui-select/cui-select.component.ts` (983 lines), `.html` (231), `.scss` (364), `.spec.ts` (1,081) — the flagship dropdown; includes key-control and paginator directives.
- `cui/cui-select-action/cui-select-action.component.ts` (181 lines).
- `cui/cui-select-hbr-vs/cui-select-hbr-vs.component.ts` (975 lines) — Harbor/virtual-scroll variant; `.html` (212), `.scss` (443), `.spec.ts` (1,498).
- `cui/cw-select/cw-select.component.ts` (925 lines), `.spec.ts` (1,200).
- `select-virtualscroll/cui-select-virtualscroll.component.ts` (170 lines).
- `selectbox/fusion-selectbox.component.ts` (43 lines) — legacy.
- `cui/cw-hbr-dropdown/cw-hbr-dropdown.component.ts` (100 lines).
- `cui/hbr-dropdown-cascading-menu/hbr-dropdown-cascading-menu.component.ts` (71 lines).
- `cui/hbr-select-add/hbr-select-add.component.ts` (233 lines).

Checkboxes / radios / switches:
- `cui/cui-checkbox/cui-checkbox.component.ts` (211 lines).
- `cui/cui-checkbox-group/cui-checkbox-group.component.ts` (118 lines).
- `cui/cui-radio/cui-radio.component.ts` (201 lines).
- `cui/cui-radio-group/cui-radio-group.component.ts` (162 lines).
- `cui/cui-radio-switch/cui-radio-switch.component.ts` (80 lines).
- `checkbox/fusion-checkbox.component.ts` (38 lines).
- `switch/fusion-switch.component.ts` (181 lines).

Date/time:
- `cui/cui-datetime-select/cui-datetime-select.component.ts` (968 lines), `.spec.ts` (1,284), `.scss` (152).
- `cui/cui-datetime-select-action/cui-datetime-select-action.component.ts` (39 lines).
- `cui/cw-date-picker/cw-date-picker/cw-date-picker.component.ts` (62 lines).
- `cui/cui-time-picker/cui-time-picker.component.ts` (49 lines).
- `cw-date-range-picker/cw-date-range-picker.component.ts` (112 lines) with `custom-date-time-range-picker/`.
- `cui/cui-days/cui-days.component.ts` (53 lines).

Buttons / button groups:
- `cui/cui-button/cui-button.component.ts` (116 lines), `.html` (99), `.scss` (48).
- `button/fusion-button.component.ts` (29 lines).
- `cui/cw-button-group/cw-button-group-hbr.component.ts` (34 lines).

Stepper / wizard frame:
- `cui/cui-stepper/cui-stepper.component.ts` (612 lines), `.scss` (772), `.spec.ts` (777) — **the multi-step wizard host.**
- `cui/cui-stepper/cui-stepper-section.component.ts` (13 lines).
- `cui/cw-hbr-stepper/cw-hbr-stepper.component.ts` (186 lines).

Form composite:
- `cw-filter-form/cw-filter-form.component.ts` (333 lines).

Tags:
- `cui/cui-tag/cui-tag.component.ts` (74 lines).
- `cui/cui-tag-filter/cui-tag-filter.component.ts` (302 lines) with sub `cui-multiselect/` and `cui-tag-selection-dialog/`.
- `cui/cui-tags-device/cui-tags-device.component.ts` (279 lines).
- `tag-filter/tag-filter.component.ts` (139 lines) with `multiselect/` and `tag-selection-dialog/`.

Validation:
- `validationbox/fusion-validationbox.component.ts` (111 lines).

---

## 6. Dialog / Popup Components (Device 360, Interface 360, confirmation modals)

- **`cui/cui-modal/cui-modal.component.ts`** (350 lines), `.html` (99), `.scss` (456), `.spec.ts` (408), plus `trap-focus.directive.ts` (41 lines). The primary modal.
- **`modal-dialog/modal-dialog.component.ts`** (263 lines), `.html` (66), `.scss` (147), `.module.ts` (26).
- **`dialog/`** (Fusion-era): `fusion-dialog.component.ts` (131 lines), `dialog.style.css` (68), `dialog.template.html` (26).
- **`cui/cui-popover/cui-popover.component.ts`** (26 lines) — thin popover.
- **`cui/cui-popover-action/cui-popover-action.component.ts`** (271 lines), `.scss` (175) — action popover (menu/tooltip-like).
- **`cui/cui-popover-wrapper/cui-popover-wrapper.component.ts`** (25 lines).
- **`popover/`** (Fusion-era): `fusion-popover.component.ts` (401 lines), `popover.style.css` (277).
- **`cui/cui-drawer/cui-drawer.component.ts`** (190 lines) — side drawer.
- **`side-panel/side-panel.component.ts`** (453 lines), `.scss` (169), `.spec.ts` (436), plus `README.txt` (87 lines).
- **`cui/cui-notification/cui-notification.component.ts`** (224 lines) and `cw-inline-notification/cw-inline-notification.component.ts` (85 lines); toaster stack: `notification-toaster/fusion-notification-toaster.component.ts` (73 lines) and `cw-notifications/cw-notifications.component.ts` (106 lines) with `cw-notifications.service.ts`.
- **`cui/cui-tooltip/cui-tooltip.component.ts`** (52 lines) and `tooltip/fusion-tooltip.component.ts` (90 lines).
- **360 family (Device / Interface / Link):**
  - `base360/base360.component.ts` (193 lines), `.service.ts` (675 lines), `.module.ts`, plus `base360Actions/`.
  - `base360/device360/device360.component.ts` (187 lines), `.module.ts` (49), with `tabs/summary/device360Summary.component.ts` (196) and `tabs/links/device360Links.component.ts` (30), `inventoryActionButton.component.ts` (23).
  - `base360/interface360/interface360.component.ts` (35 lines), `.module.ts`, with `tabs/summary/interface360Summary.component.ts` (45 lines).
  - `base360/link360/link360.component.ts` (89 lines) with `tabs/` (historical-data, lag, summary) and `link360Actions/`.
  - `base360/generic-links/genericLinks.component.ts` (1,120 lines) with `thresholds-filter/threshold-filter.component.ts` (255 lines).

---

## 7. Harbor / Magnetic Theming

Evidence of theme-variable wiring (promising for classic-theme reuse):

- **`cw-hbr-*` naming** throughout the catalog — `hbr` = Harbor design system prefix. Components exist in two parallel lines: generic CUI (`cui-*`) and Harbor-specific (`cw-hbr-*`, `hbr-*`). Examples: `cw-hbr-card/`, `cw-hbr-dropdown/`, `cw-hbr-icon/`, `cw-hbr-stepper/`, `cw-hbr-table/`, `cw-hbr-bar-chart/`, `cw-hbr-donut/`, `cw-hbr-line-chart/`, `cw-hbr-progress-ring/`, `cw-hbr-select-tags/`, `cw-menu-hbr/`, `hbr-dropdown-cascading-menu/`, `hbr-select-add/`, `cw-button-group-hbr.component.ts`, `panel-toggle-hbr.component.ts`. **Implication:** Harbor is a skin applied on top of a generic base — reuse path is to keep the base and re-skin.
- **Ag-grid themes (strong precedent for classic-theme wrapping):** `projects/cw-lib/scss/ag-grid/styles/ag-grid-themes.scss` (657 lines), `ag-grid.css` (885), `theme-blue.css`, `theme-bootstrap.css`, `theme-dark.css`, `theme-fresh.css`, `theme-fresh-custom.css` (631), `theme-material.css`.
- **Tree theme file:** `projects/cw-lib/scss/tree/styles/tree-theme.css` (34 lines).
- **Nestable theme:** `cwcomponents/ngx-nestable-comp/_nestable-theme.scss` (43 lines).
- **Icon font:** `projects/cw-lib/scss/spicons.css` (612 lines) — brand icon set.
- **Global stylesheet:** `projects/cw-lib/scss/styles.css` (5 lines — very thin — real styles live per-component in `.scss` partials).
- **i18n strings present** (`en.json` 2,985 lines, `ja.json` 2,998) — themeable visible strings.

No single top-level `_theme.scss` or `_variables.scss` visible in the tree — styling is distributed across per-component `.scss`. Classic-view reuse depends on whether those component SCSS files consume CSS custom properties (likely, given the Harbor/Magnetic separation pattern) vs. hard-coded hex colors (would require forking).

---

## 8. Utilities

Pipes (`projects/cw-lib/src/shared/pipes/`):
- `count.pipe.ts`, `keys.ts`, `map-values.pipe.ts`, `safe.pipe.ts`, `safe-pipe.module.ts`, `search-by-key.pipe.ts`.
- In-component: `cw-tree.pipe.ts`, `tag-filter/multiselect/filter.pipe.ts`, `highlight.pipe.ts`, `tag-selection-dialog/equal.pipe.ts`, `generic-topology-map/global-search/highlighter.pipe.ts`, `advanced-export/shared/adv-export-scheduling/day-abbreviation.pipe.ts`, `cui-datetime-select/cui-datetime-filter-pipe.ts`.

Directives (`projects/cw-lib/src/shared/directives/`):
- `cadence.directive.ts`, `click-outside-event.directive.ts`, `dropdown-keycontrol.directive.ts` (163 lines), `popover-keycontrol.directive.ts` (183 lines), `security-check.directive.ts`.
- In-component: `cui-modal/trap-focus.directive.ts`, `cui-datetime-select/cui-datetime-key-control.directive.ts` (178), `cui-datetime-paginator.directive.ts`, `cui-select/cui-select-key-control.directive.ts` (191), `cui-select-paginator.directive.ts`, `cw-tree/cw-tree-key-control.directive.ts` (175), `ag-grid-table/clickEventOutside.ts`, `angular2-multiselect-dropdown/clickOutside.ts`, `carousel/carousel.directive.ts`, `clear-filter/clear-filter-keycontrol.directive.ts` (157), `cw-notifications/cw-notifications.directive.ts`, `cw-notifications/cw-route-transform.directive.ts`, `notification-toaster/toasteranchor.directive.ts`, `tag-filter/dom-change.directive.ts`, `ngx-nestable-comp/nestable-drag-handle/` and `nestable-expand-collapse-handle/`.

Services (`projects/cw-lib/src/shared/services/`):
- `aggrid-accessibility.services.ts` (559), `aggrid-floating-filter.service.ts`, `availability.service.ts`, `cdg-jobs.service.ts`, `cell-renderer-utils.ts`, `config.service.ts` (694 lines), `hbr-table.service.ts`, `icon-render.service.ts` (1,279 lines — likely the theme-aware icon lookup), `links-bandwidth.service.ts`, `message-handler.service.ts`, `message-retry-handler.service.ts`, `node-map-filter.service.ts`, `shell.service.ts` (256 lines).

Core (`projects/cw-lib/src/core/`):
- `auth.service.ts` (216), `auth-guard.service.ts`, `cas.service.ts`, `sharedauth.service.ts`, `core.module.ts`, and under `services/`: `license-info-cache.service.ts`, `module.model.ts`, `navigation-menu.service.ts` (553), `navigation.service.ts` (307), `router.service.ts` (311).

API layer (`projects/cw-lib/src/shared/api/`):
- `api.base.service.ts` (471), `api.interface.ts` (741), `api.service.ts` (563), `api.module.ts`, `data.model.ts`, `sse.d.ts`.
- `v1/` with 26 per-domain services: `api.alarms.v1.service.ts` (50), `api.alarmsEvent.v1.service.ts` (126), `api.base360.v1.service.ts` (114), `api.topology.v1.service.ts` (235), `api.groups.v1.service.ts` (254), `api.customViews.v1.service.ts` (57), `api.v1.service.ts` (2,023), plus cable, cdg, imagemgmt, mop, open.bmp, optima, poweron, pulse, report, smartLicense, unprovisioned.device, websocket, ztp.configs, ztp.profile, appHealth, admin, actionfw, common.
- `v2/` mostly 1-line stubs (v2 migration in progress); meaty ones: `api.v2.service.ts` (2,102), `api.mop.api.v2.service.ts` (267), `api.pulse.v2.service.ts` (105).

Dynamic component host: `projects/cw-lib/src/cwcomponents/shared/dynamic/dynamic-component/dynamic-component.service.ts` (161) — could be useful for shell-integrated classic views.

---

## 9. Package Publishing

- **`projects/cw-lib/ng-package.json`** (12 lines) — Angular library packaging manifest (Angular's `ng-packagr` convention).
- **`projects/cw-lib/package.json`** (19 lines) — the inner library's name/version/peerDeps; consumed as an npm package by EMS UI.
- **`projects/cw-lib/public-api.ts`** (634 lines) **and duplicate `projects/cw-lib/src/public-api.ts`** (673 lines) — the public export barrel. Anything not re-exported from `public-api.ts` is not consumable downstream.
- **`projects/cw-lib/patch_version_cw.js`** (21 lines) — version-bump helper.
- **`projects/cw-lib/tsconfig.lib.json`** (30), **`tsconfig.spec.json`** (21), **`.eslintrc.json`** (88), **`eslint.config.mjs`** (9), **`karma.conf.js`** (52), **`README.md`** (24).
- Root-level build: **`angular.json`** (47), **`package.json`** (128), **`rollup.config.js`** (25), **`build.sh`** (216), **`Jenkinsfile`** (244), **`.npmrc`** (5). Library builds as an Angular package; Rollup suggests a bundled artifact. `.npmrc` presence suggests publishing to an internal Cisco npm registry (standard for cross-team consumption).
- **`common-component-creation-template.md`** (161 lines) at repo root — contribution template; worth reading if we plan to upstream a classic wrapper component.

---

## 10. Reuse Policy Summary (vs. classic-view handoff doc 06)

Handoff policy: reuse structural components themable via CSS custom properties; do **not** reuse Magnetic-coupled components directly.

**Likely reusable under a classic theme (structural, theme-neutral by design):**
- `cui-*` primitives: `cui-input`, `cui-select`, `cui-checkbox`, `cui-checkbox-group`, `cui-radio`, `cui-radio-group`, `cui-radio-switch`, `cui-modal`, `cui-drawer`, `cui-popover`, `cui-popover-action`, `cui-tooltip`, `cui-tag`, `cui-stepper`, `cui-stepper-section`, `cui-datetime-select`, `cui-time-picker`, `cui-progressbar`, `cui-import-progressbar`, `cui-empty-box`, `cui-info-icon`, `cui-splitter`, `cui-notification`.
- Ag-grid table stack: `ag-grid-table/`, `ag-grid-custom-filters/*`, `ag-grid-custom-header/`, `ag-grid-custom-header-select-all/`, plus the ag-grid themes as precedent. Adding a `theme-classic.css` alongside the existing six themes is the idiomatic path.
- Utilities: entire `src/shared/pipes/`, `src/shared/directives/`, `src/shared/services/` (icon-render, aggrid-accessibility, cell-renderer-utils, message-handler, config), and the entire `src/shared/api/` layer (backend contract, no UI coupling).
- Structural layout: `panel/`, `side-panel/`, `tabs-container/`, `nav-tabs/`, `breadcrumb/`, `cw-card-page-layout/`, `pendingChangesGuard/`, `onboarding/steps-panel/`, `infinite-scroller/`, `orderable-list/`, `key-value/`, `cards/` (primitive — minimal styling), `status-card/`.
- 360-shell frame: `base360/base360.component.ts` and module (sub-components are heavier — audit case-by-case).

**Need `*-classic` wrapper (Harbor/Magnetic-coupled naming or heavy domain styling):**
- Entire `cw-hbr-*` family: `cw-hbr-card`, `cw-hbr-dropdown`, `cw-hbr-icon`, `cw-hbr-stepper`, `cw-hbr-table` (the big one — 1,566-line component), `cw-hbr-bar-chart`, `cw-hbr-donut`, `cw-hbr-line-chart`, `cw-hbr-progress-ring`, `cw-hbr-select-tags`.
- `hbr-*` additions: `hbr-dropdown-cascading-menu`, `hbr-select-add`, `cw-menu-hbr`, `cw-button-group-hbr`, `panel-toggle-hbr`, `cui-select-hbr-vs` (Harbor virtual-scroll select).
- Chart/topology visualization: `cw-heat-map`, `cw-sankey-chart`, `generic-topology-map` (2,587-line component), `unitfied-topology/` (sic), `topology/`, `topology-dashlet/`, `topology-metrics-links-dashlet/` — likely Magnetic-coupled; out of POC scope anyway.
- Dashboard: `cw-dashboard/` (1,030-line component) — heavy Harbor styling; likely wrap.
- `alarms/` composite — needs audit: the component itself is domain-scoped to fault management and reads from `cw-hbr-table`. A classic alarms table may need to re-bind the same service to an `ag-grid-table` instance under classic theme.
- **Fusion-era legacy** (`button/`, `checkbox/`, `dialog/`, `popover/`, `textbox/`, `selectbox/`, `switch/`, `validationbox/`, `notification-toaster/`, `tooltip/`, `progressbar/`, `searchbar/`) — pre-CUI; treat as deprecated, do not build POC on top.

**Key decision point for the POC:** whether the alarms table and network-devices table should reuse `cw-hbr-table` (the Harbor-themed path — then the POC proves CSS-variable theming is enough) or `ag-grid-table` (the theme-neutral path — then we add a classic ag-grid theme alongside `theme-blue/bootstrap/dark/fresh/material`). The ag-grid theme precedent is the lower-risk choice.

**Open question:** whether `cw-hbr-table.component.scss` reads CSS custom properties or hard-codes Harbor colors — can only be answered by reading the SCSS, not the tree. Recommend that be the next agent's target.
