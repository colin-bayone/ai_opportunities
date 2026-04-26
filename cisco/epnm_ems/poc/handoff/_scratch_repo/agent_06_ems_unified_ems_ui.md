# Agent 06: unified-ems-ui Tree Report Extract

- Source: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/unified-ems-ui_tree_report.md`
- Repo root (as recorded): `/Users/cmoore/Documents/programming/unified-ems-ui`
- Included text-like files: `935`
- Included directories: `207`
- Total raw lines: `211036`
- POC scope filter: Inventory + Fault Management

---

## 1. Repo shape at a glance

Top-level entries directly under `unified-ems-ui/`:

- `.github/` — contains `instructions/` (22 codeguard `.instructions.md` files covering crypto, API, auth, client-side web security, cloud/k8s, data storage, DevOps/CI-CD, file handling, frameworks, IaC, input validation, logging, mobile, privacy, sessions/cookies, supply chain, XML/serialization, crypto algos, digital certs, hardcoded creds, safe C functions) plus `copilot-instructions.md` (131 lines).
- `.husky/pre-commit` (69 lines)
- `.vscode/` (`extensions.json`, `launch.json`, `tasks.json`)
- `custom-eslint-rules/` — in-repo custom ESLint plugin with rules `hard-coded-string-ts.js`, `hard-coded-string.js`, `max-params.js`, `no-commented-code.js`, `no-deprecated-methods.js`; plus `index.js`, `package.json`.
- `projects/ems-lib/` — **the entire Angular code lives here; this is a library project, not a standalone app shell.**
- `scripts/` — `run_test.sh` (175 lines), `verifytools.sh` (29 lines).
- Root-level files: `.editorconfig`, `.eslintrc.json`, `.gitignore`, `.npmrc`, `CODEOWNERS`, `Jenkinsfile` (245), `PULL_REQUEST_TEMPLATE.md` (100), `README.md` (27), `angular.json` (43), `build.sh` (213), `i18n-verifier.js` (54), `mockup-code-conversion.md` (1286 lines — notable large doc), `modify_ng_package.js` (30), `package-lock.json` (28678), `package.json` (156), `patch-navigation.js` (28), `rollup.config.mjs` (78), `serve-install.sh` (4), `serve.sh` (3), `tsconfig.json` (46).

**Key shape observation:** this repo is an Angular **library** (`projects/ems-lib/`), not an app. No `src/app/app.module.ts`, no `main.ts`, no `index.html` at repo root, no environments folder seen. The library is consumed by an outer shell (Infra UI). The `ng-package.json`, `tsconfig.lib.json`, `tsconfig.lib.prod.json`, `rollup.config.mjs`, and `modify_ng_package.js` confirm this is packaged for distribution.

## 2. Feature-page organization

All code sits under `projects/ems-lib/src/app/`. Features are grouped by **functional domain**, each as a sibling directory under `src/app/`:

- `device-management/`
- `device-monitoring/`
- `group-management/`
- `inventory-details/`
- `inventory-panel/`
- `network-debugger/`
- `satellites/`
- `shared/`

Under `device-management/`, sub-domains: `config-management/`, `constants/`, `helpers/`, `network-inventory/`, `services/`, `shared/`, `software-images/`, `styles/`, `swim-settings/`.

Under `device-monitoring/`: `constants/`, `network-summary/`, `performance-policies/`, `pipe/`.

Each domain owns its own `*.module.ts`, `*.routes.ts`, sometimes `*.service.ts`/`*.constants.ts`/`*.interface.ts`. Every leaf feature is a component triad (`*.component.html` + `*.component.scss` (or `.css`) + `*.component.ts`) with a `*.component.spec.ts`. No global `src/app/features/` collector — the domain directories *are* the features.

## 3. Inventory feature area

Directories and files that map to Inventory / Network Devices / Device 360 / Interface 360 / Chassis View equivalents:

- `projects/ems-lib/src/app/device-management/network-inventory/` — the Network Devices table area.
  - `network-inventory.component.html` (119), `.scss` (44), `.spec.ts` (796), `.ts` (642)
  - `constants/network-inventory.constants.ts` (158)
- `projects/ems-lib/src/app/inventory-details/` — the Device 360 / device-detail area.
  - `inventory-details.component.html` (40), `.scss` (122), `.spec.ts` (1099), `.ts` (486)
  - `inventory-details.module.ts` (22), `inventory-details.routes.ts` (9), `inventory-details.service.ts` (164)
  - `inventory-details-device360/` — explicitly named Device 360 subcomponent: `inventory-details-device360.component.{html,scss,spec.ts,ts}`
  - `inventory-details-panel-header/` — panel header for the details view
  - `equipment-types-show-hide/` — controls visibility of equipment types (chassis/card/port filtering)
- `projects/ems-lib/src/app/inventory-panel/` — the side/right-panel expanded view on inventory items.
  - `inventory-panel.component.{html,scss,spec.ts,ts}`, `inventory-panel.constants.ts` (94), `inventory-panel.module.ts` (48)
  - `inventory-panel.api.service.ts` (25), `inventory-panel-events.service.ts` (32)
  - `metric-chart/` — metric charts on the device panel
  - `node-alarms/` — alarms for a node (inventory ↔ fault cross-cut)
  - `node-details/` — node-level detail view, 245-line html, 180-line ts
  - `node-history/` — node history (373-line ts)
  - `node-level-config/` — config-details + template-selection (large: `node-level-config.component.ts` 374 lines, `config-details.component.ts` 704 lines)
- `projects/ems-lib/src/app/shared/interface-list/` — Interface 360 equivalent.
  - `interface-list.component.{html,scss,spec.ts,ts}` (ts 366), `interface-list.module.ts` (25)
  - `constants/interface-list.constant.ts` (79)
  - `services/interface-list.service.ts` (115) + spec (156)
- `projects/ems-lib/src/app/shared/inventory-list/` — reusable inventory list component.
  - `inventory-list.component.{html,scss,spec.ts,ts}` (ts 405), `inventory-list.module.ts` (23)
  - `constant/inventory-list.constant.ts` (122), `services/inventory-list.service.ts` (122) + spec
- `projects/ems-lib/src/app/satellites/` — satellites view (inventory-adjacent; chassis-family domain).
  - `satellites.component.*`, `satellites.module.ts` (51)
  - `satellite-pane/`, `satellites-table/` (with `satellites-table-api.service.ts` 128 + spec 207, and 138-line constants)

Chassis / card / port iconography present in assets:

- `projects/ems-lib/assets/images/inventory_details/map/devices/` — SVGs named `ET_CHASSIS`, `ET_CARDSLOT`, `ET_LINECARD`, `ET_MODULE`, `ET_PORT`, `ET_PORTSLOT`, `ET_SLOT`, `ET_RACK`, `ET_ROUTER`, `ET_FAN`, `ET_POWERSUPPLY`, `ET_PLUGGABLE`, `NODE_TYPE_ROUTER` (each with `-dark` variant). This is the icon set a Chassis View would render against. No explicit `chassis-view/` component directory appears in the tree — the chassis rendering is likely consumed externally or rendered via the device-map images.

## 4. Fault Management feature area

No top-level directory explicitly named `alarms/`, `events/`, `syslogs/`, `correlation/`, or `monitor/` was found. The fault surfaces in this repo are limited to:

- `projects/ems-lib/src/app/inventory-panel/node-alarms/` — per-node alarms in the inventory panel.
  - `node-alarms.component.{html,scss,spec.ts,ts}` (ts 21, html 5, scss 3, spec 29) — thin wrapper component.
- `projects/ems-lib/assets/images/inventory_details/map/glyphs/` — severity glyphs: `critical.svg`, `major.svg`, `minor.svg`, `warning.svg`, `information.svg`, `unknown.svg`, `up.svg` (plus collapse/expand).
- `projects/ems-lib/src/app/device-monitoring/network-summary/trend/severity/severity.component.{html,scss,spec.ts,ts}` (ts 283 lines, scss 126) — severity-driven trend visualization inside network-summary.
- `projects/ems-lib/src/app/shared/metrics-history/metric-events-chart/` — events overlay on a metrics chart.

i18n: `projects/ems-lib/assets/i18n/en.json` (3772 lines) and `ja.json` (3772 lines) are the translation stores that presumably hold alarm/event labels but are not decomposable from names alone.

**Finding (evidence gap):** Fault Management (alarms list, events list, syslogs, correlation, monitor menu) is effectively **absent** from `unified-ems-ui`. The only fault-related code is the skeletal `node-alarms` panel component and severity-glyph/severity-component assets. This suggests Fault Management pages live in a different repo (likely another feature-layer repo or the OSS-fault-manager backend-consuming layer).

## 5. Routing and navigation

No `app-routing.module.ts` or root router module — consistent with this being a library. Routing files are per-domain:

- `projects/ems-lib/src/app/ems.routes.ts` (26 lines) — top-level route aggregator for the library.
- `projects/ems-lib/src/app/device-management/device-manager.routes.ts` (15)
- `projects/ems-lib/src/app/device-management/config-management/config-management.routes.ts` (100)
- `projects/ems-lib/src/app/device-management/software-images/software-images.routes.ts` (19)
- `projects/ems-lib/src/app/device-management/swim-settings/swim-settings.routes.ts` (9)
- `projects/ems-lib/src/app/device-monitoring/device-monitoring.routes.ts` (9)
- `projects/ems-lib/src/app/device-monitoring/network-summary/network-summary.routes.ts` (9)
- `projects/ems-lib/src/app/device-monitoring/performance-policies/performance-policies.routes.ts` (23)
- `projects/ems-lib/src/app/group-management/port-groups/port-groups-manager.routes.ts` (53)
- `projects/ems-lib/src/app/inventory-details/inventory-details.routes.ts` (9)
- `projects/ems-lib/src/app/network-debugger/network-debugger.routes.ts` (55)
- `projects/ems-lib/src/app/shared/data-retention/device-performance/device-performance.routes.ts` (9)
- `projects/ems-lib/src/app/shared/metric-health-settings/metric-health-setting.routes.ts` (9)

Navigation config (menu data): `projects/ems-lib/assets/config/navigation.json` (71 lines) + `navigation-ja.json` (71 lines). Root-level helper: `patch-navigation.js` (28 lines) — suggests the navigation JSON is patched during build/install.

Root library module: `projects/ems-lib/src/app/root-ems.module.ts` (44 lines). Public API barrel: `projects/ems-lib/src/app/public-api.ts` (26 lines). Lib entry: `projects/ems-lib/src/lib/ems-lib.module.ts` (16), `ems-lib.component.ts` (21), `ems-lib.service.ts` (9).

## 6. Services layer

No single `services/` directory. Services are co-located with each feature. Key service files:

- Root lib facade/glue:
  - `projects/ems-lib/src/app/shared/service/ems-api.service.ts` (121) + spec (19)
  - `projects/ems-lib/src/app/shared/service/api.external.service.ts` (58)
  - `projects/ems-lib/src/app/shared/service/app-facade.service.ts` (85) + spec (84)
  - `projects/ems-lib/src/app/shared/service/mock-facade.service.ts` (31)
  - `projects/ems-lib/src/app/shared/service/ems-validator.service.ts` (107) + spec (79)
  - `projects/ems-lib/src/app/shared/service/file.manager.service.ts` (50)
  - `projects/ems-lib/src/app/shared/service/mock-icon-renderer-service.ts` (542)
  - `projects/ems-lib/src/app/shared/ems-helper/ems-api.helper.ts` (203), `ems-error.helper.ts` (93)
- Device management:
  - `device-management/device-manager-api.service.ts` (25), `device-manager.service.ts` (63) + spec (105)
  - `device-management/services/table-utils.service.ts` (74) + spec (135)
  - `device-management/config-management/api.deviceConfig.service.ts` (267) + spec (806)
  - `device-management/config-management/config-management.service.spec.ts` (605)
  - `device-management/config-management/stepper.service.ts` (31) + spec (108)
  - `device-management/config-management/config-backup-restore/config-backup-restore.service.ts` (726) + spec (675)
  - `device-management/config-management/config-jobs/config-jobs.api.service.ts` (256) + spec (481)
  - `device-management/config-management/config-jobs/config-br-job/backup-restore-jobs.service.ts` (168), `config-br-jobs.service.ts` (840) + spec (1250)
  - `device-management/config-management/config-jobs/deploy-template-job/deploy-template-job.service.ts` (161) + spec (226)
  - `device-management/config-management/config-templates/config-template.service.ts` (411) + spec (395)
  - `device-management/config-management/config-templates/create-template/create-template.service.ts` (97) + spec (385)
  - `device-management/config-management/config-templates/deploy-template/deploy-template.service.ts` (115) + spec (301)
  - `device-management/config-management/config-settings/config-settings.service.ts` (8) + spec (16)
  - `device-management/software-images/software-images.service.ts` (512) + spec (880)
  - `device-management/software-images/activate-flow/activate-flow.service.ts` (53) + spec (44), `activate-helper.service.ts` (52) + spec (71)
  - `device-management/software-images/add-image-flow/add-image-flow.service.ts` (9)
  - `device-management/software-images/stepper-service.ts` (35) + spec (277)
  - `device-management/software-images/common/base-settings/base-settings.service.ts` (9) + spec (51)
  - `device-management/software-images/distribute-flow/distribute-flow.service.ts` (16)
  - `device-management/software-images/main-page/tables/tables.service.ts` (27)
  - `device-management/swim-settings/swim-settings.service.ts` (33) + spec (92)
- Device monitoring:
  - `device-monitoring/network-summary/network-summary.service.ts` (175) + spec (264), `network-summary.utils.ts` (147) + spec (290)
  - `device-monitoring/network-summary/common/data.service.ts` (14) + spec (32)
  - `device-monitoring/network-summary/dpm-dashlet/dpm-dashlet.service.ts` (37) + spec (47)
  - `device-monitoring/network-summary/dpm-dashlet/main/histogram/histogram.service.ts` (125) + spec (398)
  - `device-monitoring/performance-policies/performance-policies.service.ts` (400) + spec (564)
- Group management: `group-management/port-groups/port-groups-manager.service.ts` (175) + spec (249)
- Inventory:
  - `inventory-details/inventory-details.service.ts` (164)
  - `inventory-panel/inventory-panel.api.service.ts` (25) + spec (51)
  - `inventory-panel/inventory-panel-events.service.ts` (32) + spec (63)
  - `inventory-panel/node-level-config/node-level-config.service.ts` (85) + spec (133)
- Network debugger: `network-debugger/services/network-debugger-api.service.ts` (125), `services/utility.service.ts` (122)
- Satellites: `satellites/satellites-table/satellites-table-api.service.ts` (128) + spec (207)
- Shared domain services:
  - `shared/data-retention/device-performance/device-performance.service.ts` (99) + spec (100)
  - `shared/devicemetrics/device-metrics.service.ts` (62) + spec (92)
  - `shared/interface-list/services/interface-list.service.ts` (115) + spec (156)
  - `shared/inventory-list/services/inventory-list.service.ts` (122) + spec (166)
  - `shared/metric-health-settings/metric-health-setting.service.ts` (101) + spec (154)
  - `shared/metrics-history/metrics-history.service.ts` (74) + spec (86)

The central HTTP wrapper is `shared/service/ems-api.service.ts` (121 lines) plus the `ems-api.helper.ts` (203) — these are the primary REST integration points feature services call into.

## 7. Models / interfaces

TypeScript interfaces and enums live alongside their features. Inventory + fault relevant:

- `projects/ems-lib/src/app/device-management/constants/device-manager.interface.ts` (51)
- `projects/ems-lib/src/app/inventory-panel/metric-chart/metric-chart.interface.ts` (40)
- `projects/ems-lib/src/app/device-management/software-images/software-images.interface.ts` (16)
- `projects/ems-lib/src/app/device-management/software-images/activate-flow/activate-flow.interface.ts` (91)
- `projects/ems-lib/src/app/device-management/software-images/add-image-flow/add-image-flow.interface.ts` (5)
- `projects/ems-lib/src/app/device-management/software-images/common/common.interface.ts` (60)
- `projects/ems-lib/src/app/device-management/software-images/distribute-flow/distribute-flow.interface.ts` (223)
- `projects/ems-lib/src/app/device-management/software-images/main-page/tables/jobs-table/job-details/job-details.interface.ts` (14)
- `projects/ems-lib/src/app/device-management/config-management/config-jobs/config-br-job/backup-restore-jobs.interface.ts` (33)
- `projects/ems-lib/src/app/device-monitoring/network-summary/network-summary.interface.ts` (239)
- `projects/ems-lib/src/app/shared/metrics-history/metrics-history.interface.ts` (182), `metrics-history.ts` (152)

Enums of note:

- `device-management/config-management/config-backup-restore/device-configuration.enum.ts` (95)
- `device-management/config-management/config-jobs/config-br-job/api-config-br-job.enum.ts` (20), `config-br-jobs.enum.ts` (126)
- `device-management/config-management/config-jobs/config-jobs.enum.ts` (28)
- `device-management/config-management/api.deviceConfig.enum.ts` (76)
- `device-management/software-images/software-images.api.enum.ts` (42), `software-images.enum.ts` (61), `main-page/main-page.enum.ts` (11), `add-image-flow/add-image-flow.enum.ts` (32)
- `device-management/software-images/main-page/tables/tables.enum.ts` (51)
- `device-management/software-images/main-page/tables/jobs-table/job-details/device-details.enum.ts` (79)
- `device-monitoring/network-summary/network-summary.enum.ts` (118)
- `shared/constants/ems.constant.ts` (30)

**No explicit `Device`, `Alarm`, `Event`, `Interface`, `Module`, `Chassis` interface files** appear by name. Device/Alarm/Event/Interface types are almost certainly imported from an upstream shared-types package (likely `ems-cnc-ui-lib` or an ncnc/api-clients layer in the outer shell) rather than declared here. This is consistent with this repo being the feature-layer and inheriting domain types.

## 8. Where the classic-view subfolder would most naturally fit

Based strictly on observed structure (no `features/`, `pages/`, or `views/` folder exists), candidate placements:

1. **`projects/ems-lib/src/app/classic/`** — as a peer to existing domain directories (`device-management/`, `device-monitoring/`, `inventory-details/`, `inventory-panel/`, `satellites/`, etc.). This matches the repo's single dominant pattern: each feature domain is a top-level sibling under `src/app/`. It would register itself via its own `classic.module.ts` + `classic.routes.ts`, following the pattern of `device-monitoring.module.ts` + `device-monitoring.routes.ts`, and be wired into `projects/ems-lib/src/app/ems.routes.ts` (26 lines) — the single aggregator file.

2. **`projects/ems-lib/src/app/inventory-panel/classic/`** or **`projects/ems-lib/src/app/inventory-details/classic/`** — if the classic view is scoped specifically as an alternate render of the inventory details/panel. Precedent: `inventory-details/inventory-details-device360/` already exists as a subcomponent of inventory-details. A `classic/` subfolder here would mirror that nesting.

Option 1 is the cleaner structural fit if classic covers multiple domains (inventory + fault). Option 2 fits only if classic view remains a drop-in alternate of Device 360.

Evidence for both: `src/app/ems.routes.ts` as the central route aggregator, plus the per-domain `*.module.ts` + `*.routes.ts` convention repeated uniformly across all eight domain folders.

## 9. Build and Angular version indicators

Root config files:

- `angular.json` (43 lines) — Angular CLI workspace definition.
- `package.json` (156 lines) — dependencies (not expanded in tree report; version numbers not visible from names alone).
- `package-lock.json` (28678 lines).
- `tsconfig.json` (46 lines) — root TS config.
- Library TS configs: `projects/ems-lib/tsconfig.lib.json` (30), `tsconfig.lib.prod.json` (10), `tsconfig.spec.json` (17).
- `projects/ems-lib/ng-package.json` (1 line) — ng-packagr config.
- `projects/ems-lib/package.json` (13 lines) — library's own package manifest.
- `projects/ems-lib/karma.conf.js` (53) — Karma for unit tests.
- `rollup.config.mjs` (78) — Rollup bundling (library output).
- `build.sh` (213), `serve.sh` (3), `serve-install.sh` (4), `modify_ng_package.js` (30), `patch-navigation.js` (28), `i18n-verifier.js` (54).
- `Jenkinsfile` (245) — CI pipeline.
- `.husky/pre-commit` (69) — git hook.
- `.eslintrc.json` (109) + in-repo `custom-eslint-rules/` plugin.
- `CODEOWNERS` (1 line).

The tree report does not expose `package.json` contents, so exact Angular major version (21 per briefing) cannot be confirmed from tree names alone.

## 10. Shell integration signals

Evidence that this library is loaded by an outer shell (Infra UI):

- Library packaging artifacts: `projects/ems-lib/ng-package.json`, `tsconfig.lib.json/prod.json`, `rollup.config.mjs`, `modify_ng_package.js` — all indicate this is compiled as a distributable Angular library.
- Public API barrel: `projects/ems-lib/src/app/public-api.ts` (26 lines) — the exported surface that consumers import.
- Root modules: `projects/ems-lib/src/app/root-ems.module.ts` (44), `projects/ems-lib/src/lib/ems-lib.module.ts` (16), `ems-lib.component.ts` (21), `ems-lib.service.ts` (9) — the component/service/module a shell mounts.
- Top-level route aggregator consumed by the shell: `projects/ems-lib/src/app/ems.routes.ts` (26).
- Navigation descriptor the shell merges into its menu: `projects/ems-lib/assets/config/navigation.json` (71) + `navigation-ja.json` (71), with build-time patcher `patch-navigation.js` (28).
- No `main.ts`, no `index.html`, no `environments/` folder, no `app.module.ts`, no bootstrap entry — confirms library-only, expected to be bootstrapped by Infra UI.
- `CODEOWNERS`, `Jenkinsfile`, `build.sh` at root suggest the library is published as part of a multi-repo pipeline (consistent with the three-layer shell model).

No cross-repo federation config (e.g., Module Federation webpack config) is visible in the tree by name. Integration is almost certainly via package consumption (ng-packagr output imported by the outer shell) rather than runtime microfrontend federation.

---

## Summary of critical paths for the POC

- `projects/ems-lib/src/app/ems.routes.ts` — central route injection point for any classic-view module.
- `projects/ems-lib/src/app/root-ems.module.ts` — module registration.
- `projects/ems-lib/src/app/public-api.ts` — export surface for shell consumption.
- `projects/ems-lib/src/app/inventory-details/` (incl. `inventory-details-device360/`) — Device 360 equivalent home.
- `projects/ems-lib/src/app/inventory-panel/` (incl. `node-details/`, `node-alarms/`, `metric-chart/`, `node-level-config/`) — side-panel detail surface.
- `projects/ems-lib/src/app/device-management/network-inventory/` — Network Devices list.
- `projects/ems-lib/src/app/shared/interface-list/` — Interface 360 equivalent.
- `projects/ems-lib/src/app/satellites/` — satellites/chassis-adjacent inventory.
- `projects/ems-lib/src/app/shared/service/ems-api.service.ts` + `ems-api.helper.ts` — central REST wrapper.
- `projects/ems-lib/assets/config/navigation.json` + `patch-navigation.js` — menu wiring for any new classic routes.
- `projects/ems-lib/assets/images/inventory_details/map/devices/` — chassis/card/port SVG iconography for any Chassis View render.

## Gaps / issues flagged

- **Fault Management is largely missing from this repo.** Only `inventory-panel/node-alarms/` (21-line component) and severity glyph/component fragments exist. No alarms list, events list, syslogs, correlation, or monitor-menu components are present. Classic-view Fault scope likely needs code either sourced from a sibling repo or built new here.
- **No explicit Device / Alarm / Event / Interface / Chassis interface files by name.** Domain types are likely imported from an upstream shared-types package not visible in this tree.
- **No Chassis View component directory** named as such; the chassis rendering assets exist (SVGs in `assets/images/inventory_details/map/devices/`) but the renderer consuming them is not locatable by name — may be in an outer layer or rendered via the inventory-details/inventory-panel components.
- **Angular version not confirmable from tree** — `package.json` contents not exposed; briefing states Angular 21.
- **`mockup-code-conversion.md` (1286 lines)** at root is an unusually large in-repo doc — worth reading directly (not in this agent's scope).
