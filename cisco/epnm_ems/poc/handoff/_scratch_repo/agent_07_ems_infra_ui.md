# Agent 07 - EMS `infra-ui` Tree Report Extract

Source: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/infra-ui_tree_report.md`

Repo root on origin machine: `/Users/cmoore/Documents/programming/EMS-CNC/frontend/infra-ui`

Topline counts from the report header: 4,439 text files, 339 directories, 541,682 raw lines, 1 skipped binary, 213 skipped ignored-extension files.

## 1. Repo shape at a glance

Top-level directories and root files (verbatim from the tree):

- `.ai/` — contains `HARBOR_DESIGN_SYSTEM_REFERENCE.md` (532 lines) and `coding-instructions.md` (248 lines). Direct evidence that **Harbor** is the design system this shell targets.
- `.github/instructions/` — 22 `codeguard-*.instructions.md` files (cryptography, auth, access control, XSS, session, supply chain, C-function safety, etc.). Plus `copilot-instructions.md`.
- `.husky/pre-commit` (91 lines) — git pre-commit hook.
- `.review/` — `ui-pr-review-rules.md` (821 lines), `ui-review-current-changes.md` (275 lines).
- `.windsurf/rules.md` (13 lines).
- `config/` — build/environment config: `environments/environment.js`, `environment.prod.js`, `environment.optims.js`, `environment.robot110.js`, `config.in`; plus `preprocess.js`, `preprocess.run.js`, `copy_json_attributes.py`, `tag-html-resources.js`, `tykConfigMap.json`.
- `custom-eslint-rules/` — custom rules: `hard-coded-string-ts.js`, `hard-coded-string.js`, `max-params.js`.
- `mock/cert-mgmt.ts`.
- `scripts/` — `run_test.sh`, `verifytools.sh`.
- `src/` — the Angular app (feature tree detailed below).
- `ui-backend-service/` — a **Go** backend service (see §9). Source under `src/backend/`, `src/controller/`, `src/service/journey/`, `src/service/tier/`, `src/database/`, `src/ui/httpserver/`; protobuf defs in `config/proto/`; `Makefile`, `go.mod`, `go.sum`.
- Root files: `.cursorrules`, `.eslintignore`, `.eslintrc.json`, `.gitignore`, `.npmrc`, `CODEOWNERS`, `Dockerfile`, `Dockerfile.dev`, `Jenkinsfile`, `PULL_REQUEST_TEMPLATE.md`, `README.md`, `angular.json`, `app.js`, `browserslist`, `build.sh`, `custom-webpack.config.js`, `dependency-repo-tree.txt`, `docker-compose.yml`, `i18n-verifier.js`, `karma.conf.js`, `mockup-code-conversion.md` (1046 lines — notable), `ng2-nvd3.ts`, `package-lock.json` (30,389 lines), `package.json` (177 lines), `package.prod.json`, `patch_version.js`, `readiness.sh`, `startup.sh`, `supervisor.conf`, `tsconfig.app.json`, `tsconfig.json`, `tsconfig.spec.json`, `tslint.json`, `webpack.config.js`.

## 2. Shell composition

The shell frame lives under `src/app/container/`:

- **Shell host:** `src/app/container/shell/`
  - `shell.component.ts` (148 lines), `shell.template.html` (35 lines), `shell.style.scss` (88 lines), `shell.service.ts` (78 lines), `shell.component.spec.ts` (223 lines), `shell.service.spec.ts` (81 lines), `index.ts`.
  - This is the primary layout frame — small (35-line template, 88-line SCSS) consistent with a shell that composes header + nav + router outlet.
- **Header:** `src/app/container/header/`
  - `header.component.ts` (1578 lines — large), `header.template.html` (159 lines), `header.style.scss` (337 lines), `header.module.ts` (44 lines), `header.component.spec.ts` (3141 lines), `index.ts`.
  - The 1578-line header is where a product-level classic-view global toggle would eventually plug in.
- **Top navigation:** `src/app/container/navigation/`
  - `navigation.component.ts` (703 lines), `navigation.template.html` (108 lines), `navigation.style.scss` (1197 lines — heaviest SCSS in the shell), `navigation.module.ts` (29 lines), `navigation.component.spec.ts` (840 lines), `index.ts`.
- **Home (landing/content outlet host):** `src/app/container/home/`
  - `home.component.ts` (240 lines), `home.component.html` (44 lines), `home.component.css` (20 lines), `home.module.ts` (36 lines), spec + e2e.
- **Robot shell (routing-level shell):** `src/app/container/robot-shell/`
  - `robot-shell.component.ts` (67 lines), `robot-shell.module.ts` (54 lines), `robot-shell.routes.ts` (**181 lines — primary route table**), `robot-shell.routes.spec.ts`, `robot-shell.component.html` (1 line — almost certainly `<router-outlet>`), `robot-shell.component.css` (0 lines).
  - The 181-line `robot-shell.routes.ts` is the feature-page mount point — where Infra UI registers lazy-loaded feature modules into the router outlet.
- **Loading overlay:** `src/app/container/loading/` — component + module, 237-line `loading.component.ts`.
- **Session expire:** `src/app/container/sessionExpire/` — `fusion-sessionExpire.component.ts`, `fusion-session.module.ts`.
- **Expiration error handler:** `src/app/container/expirationError/`.
- **Settings (in-shell):** `src/app/container/setting/`
  - `setting.component.ts` (730 lines), `setting.template.html` (171 lines), `setting.style.scss` (411 lines), `setting.module.ts` (23 lines), spec (883 lines), `image/key-solid.svg`. **Candidate mount for a product-level global classic-view toggle preference.**

Root bootstrap: `src/main.ts` (16 lines), `src/index.html` (50 lines), `src/polyfills.ts` (64 lines), `src/app/app.module.ts` (219 lines), `src/app/app.component.ts` (343 lines), `src/app/app.component.html` (1 line), `src/app/app-routing.module.ts` (10 lines — tiny, routing delegated to robot-shell), `src/app/app.component.scss` (8 lines), `src/app/app.variables.scss` (37 lines), `src/app/app.component.enum.ts`.

Cross-cutting interceptors at `src/app/`: `logging.interceptor.ts`, `session-expired.interceptor.ts`.

## 3. Top navigation menu

Primary evidence for a **dynamic / backend-driven** nav model:

- `src/app/container/navigation/navigation.component.ts` (703 lines) — nav component, sized like a consumer rather than a static config.
- `src/app/services/module.service.ts` (**401 lines**) — at `src/app/services/`, alongside `delay.service.ts`. A module service of this size is consistent with pulling available modules from backend and driving the nav tree.
- `src/app/models/module.model.ts` (15 lines) — module interface.
- `src/assets/modules.json` (300 lines, at `src/assets/modules.json`) — a static seed/manifest of modules (visible under `src/assets/` alongside `robot-admin.json`, `key-solid.svg`, etc.). This is a strong candidate for the static half of a hybrid static-config-plus-backend nav.
- `src/app/container/robot-shell/robot-shell.routes.ts` (181 lines) — route table that gates which features can be navigated to.
- `src/assets/app-icons/` — contains per-feature icon pairs (e.g., `epnm-bw-30px.svg`, `epnm-color-40px.svg`, `active-topology-bw-30px.svg`, `infrastructure_bw_30px.svg`, `health_insights_bw_30px.svg`, `change_automation_bw_30px.svg`, `opt_engine_bw_30px.svg`, `ztp_bw_30px.svg`, `workflow-manager-40px.svg`). The bw/color pair pattern suggests active/inactive states rendered against a module list — again consistent with data-driven nav.

Representative nav/feature paths surfaced in `src/app/`:
`advanced-export-jobs/`, `app-health/`, `backup-restore/`, `collection-jobs/`, `component-playground/`, `cw-init/` (very large — Crosswork init, management, health, NSO deployment, system management), `cw-startup/` (bootstrap/onboarding screens — welcome, help, support, getting-started, cluster-administration, scaling-deployment, ecosystem-partners, final-verification, bundle-installation), `entry/`, `geo-enrollment/`, `guards/`, `interface-filtering/`, `landing-page/`, `login/`, `metric-manager/`, `onboarding-main/` (wizard-main with credential-profile, data-gateway-connectivity, dg-list-onboarding-wrapper, onboard-device, providers, schedule, smart-licensing, tag-manager, add-destination), `robot-aaa/` (aaa-servers, aaa-settings, ldap, radius, sso, tacacs), `robot-admin/`, `robot-alarm/`, `robot-alarms-v2/` (alarm-notification, alarm-policy, device-alarms-and-events, shared, page-container — **central to POC Fault Management**), `robot-audit/`, `robot-certificates/`, `robot-users/` (active-session, data-subscription, role-management, user-management, web-socket), `smart-licensing/`.

Conclusion: nav is Angular lazy-loaded modules registered via `robot-shell.routes.ts`, with an accompanying `module.service.ts` + `modules.json` manifest driving visible menu items. Not a pure static config; not a runtime plugin/module-federation system (see §4).

## 4. Loading mechanism

Evidence points to **standard Angular lazy-loaded NgModules behind a single `robot-shell` router outlet**, not Webpack Module Federation:

- Each feature directory ships its own `*.module.ts` and (commonly) `*.routes.ts`, e.g. `advanced-export-jobs.module.ts`, `backup-restore.module.ts`, `collection-jobs.module.ts`, `component-playground.module.ts`, `cw-init.module.ts` + `cw-init.routes.ts`, `start-up.module.ts` + `start-up.routes.ts`, `geo-enrollment.module.ts`, `login.module.ts` + `login.routes.ts`, `metric-manager.module.ts`, `onboarding-main.*`, `robot-aaa.*`, `robot-admin.module.ts` + `robot-admin.routes.ts` (176 lines), `robot-alarm.module.ts`, `robot-alarms-v2.module.ts` + `robot-alarms-routes.ts`, `robot-audit.*`, `robot-certificates.module.ts` + `robot-certificates.routes.ts`, `robot-users.module.ts` + `robot-users.routes.ts`, `smart-licensing.module.ts`.
- The central wiring file is `src/app/container/robot-shell/robot-shell.routes.ts` (181 lines) — sized exactly for a route table of ~20+ lazy-loaded modules.
- Build config uses `custom-webpack.config.js` (13 lines — very short, an extension of Angular's builder) and `webpack.config.js` (5 lines — stub). No filenames evocative of Module Federation (`remote-entry.ts`, `mf.config.*`, `webpack.federation.*`) appear anywhere.
- `src/app/shared/foreign-service/` carries thin delegate services (`inventory-delegate.service.ts`, `provider-delegate.service.ts`, `cdg-inventory-delegate.service.ts`, `cdg-utils-delegate.service.ts`, `cdgAdmin-delegate.service.ts`, each 7 lines, plus `foreign-service.module.ts` at 54 lines). The "foreign-service" delegate pattern is how Infra UI calls out to services owned by other layers/apps — this is the integration seam for cross-app service calls, not runtime code loading.
- Root `app.js` (20 lines) and `supervisor.conf` (21 lines) + `startup.sh` / `readiness.sh` suggest a single-SPA served from a Node process under supervisord.

Conclusion: classic Angular lazy-load via `loadChildren` in `robot-shell.routes.ts`. Feature pages get mounted at the `<router-outlet>` inside `robot-shell.component.html`. A feature-layer repo (e.g. `unified-ems-ui`) would integrate either as additional lazy routes in this table, via delegate services, or by being built into the same bundle.

## 5. Theming foundations

- **Top-level styles:** `src/styles.scss` (**2,265 lines**) and `src/styles_ja.scss` (40 lines — Japanese locale overrides).
- **Harbor integration:** `src/harbor-global-styles-scope-fix.ts` (60 lines) and `src/harbor-global-styles-scope-fix.spec.ts` (68 lines). Plus `.ai/HARBOR_DESIGN_SYSTEM_REFERENCE.md` (532 lines). Harbor is first-class.
- **Magnetic tokens (present):** under `src/css/`:
  - `magnetic-tokens.scss` (90 lines)
  - `magnetic-light-classic.scss` (723 lines)
  - `magnetic-dark-classic.scss` (723 lines)
  - Critical: the filenames include the word **"classic"** — Magnetic light/dark classic are already in the repo. That is directly relevant to the classic-view POC. Whether "classic" here refers to the EPNM classic UI style or to a Magnetic design-system naming convention is an open question — flag for investigation.
- **AG Grid themes:** `src/css/ag-grid/styles/` — `ag-grid-themes.scss` (825 lines), `ag-grid.css` (885 lines), `theme-blue.css`, `theme-bootstrap.css`, `theme-dark.css` + `.scss`, `theme-fresh.css`, `theme-fresh-custom.css`, `theme-material.css`.
- **CUI (Cisco UI) legacy:** `src/assets/cisco-ui/` — very large. `build/css/cui-basic.css` (8328), `cui-standard.css` (13529), `cui-styleguide.css` (13558). `src/scss/` tree contains `base/`, `build/`, `components/`, `layout/` (including `_header.scss`, `_footer.scss`, `_grid.scss`, `_sidebar.scss` at 943 lines), `overrides/`, `primitives/`, `styleguide/`, `themes/_dark.scss` (98), `themes/_default.scss` (548), `utilities/`, `vendor/bootstrap/`, `_base.scss` (535), `_cui-font.scss` (14149 lines), `cui-basic.scss`, `cui-standard.scss`, `cui-styleguide.scss`. CUI is a second (legacy?) design system coexisting with Harbor/Magnetic.
- **Other style files:** `src/css/spicons.css` (612 lines), `src/css/styles.css` (5 lines — stub), `src/css/ng-bootstrap/popover.scss`, `src/css/tree/styles/tree-theme.css`.
- **Per-feature SCSS:** component-scoped `.scss` files everywhere (283 total per repo summary).
- **App-level vars:** `src/app/app.variables.scss` (37 lines).

Theming reality for the POC: three layers of design-system code already live in this shell (CUI legacy, Harbor, Magnetic light/dark-classic). A classic-view toggle would plausibly switch which of these token stacks applies to the feature outlet.

## 6. Login / auth

- **Login screen:** `src/app/login/`
  - `login.component.ts` (623 lines), `login.component.html` (122), `login.component.scss` (429), `login.module.ts` (20), `login.routes.ts` (16), `login.service.ts` (225), `login.service.spec.ts` (194), `login.component.spec.ts` (551 in `test/`), `login.component.e2e-spec.bak.ts`, `login.component.spec.bak.ts`, `loginDisclaimer.component.ts/html/scss/spec.bak.ts` (50/31/223/92). `index.ts`.
- **AAA and federation:** `src/app/robot-aaa/` — `aaa-servers/` (1209-line component, 3282-line spec), `aaa-settings/`, `ldap/`, `radius/`, `sso/` (service + component 745 lines), `tacacs/`, plus `robot-aaa-service.ts` (143 lines) and `robot-aaa.component.*`.
- **Certificates / CSR / cert-bind:** `src/app/robot-certificates/` — add-certificate, auto-renewal-settings, cert-bind (config-client-auth, upload-form), cert-details, cert-info, certificate-signing-request, csr-journey, external-destination, generate-csr, job-sets, select-devices, plus `robot-certificates.service.ts` (495 lines), `cert-state.service.ts`.
- **Users/roles/sessions:** `src/app/robot-users/` — active-session (688-line component), data-subscription, role-management (1728-line component, 2822-line spec), user-management (998-line component), user/change-password, user/new-password-hint-rule, web-socket (464-line component), `robot-user.service.ts`, `role.model.ts` (205), `user.model.ts`.
- **Audit:** `src/app/robot-audit/` — 731-line component, 1104-line spec, 291-line service.
- **Session expiry:** `src/app/container/sessionExpire/` (see §2). Plus `src/app/session-expired.interceptor.ts`.

A global classic-view toggle must coexist with: login page, session-expire modal, expiration-error handler, session-expired HTTP interceptor, and user/role-based preference storage (the active-session + user components and the settings module are the persistence surface).

## 7. Assets / icons

SVG asset organization (inside `src/assets/`):

- `app-icons/` — ~28 per-feature application icons with bw/color + size suffixes (e.g., `aa_bw_30px.svg`, `aa_color_40px.svg`, `active-topology-bw-30px.svg`, `active-topology-color-40px.svg`, `cards-cluster-bw-30px.svg`, `epnm-bw-30px.svg`, `epnm-color-40px.svg`, `geo-redundancy-icon.svg`, `health_insights_bw_30px.svg`, `infrastructure_bw_30px.svg`, `path-analytics-icon.svg`, `workflow-manager-40px.svg`, `ztp_bw_30px.svg`). Axis = feature × state(bw/color) × size.
- `cisco-ui/src/icons/` — hundreds of Cisco UI (CUI) icons, each duplicated as `<name>.svg` and `app-<name>.svg` (e.g., `add.svg` + `app-add.svg`, `cog.svg` + `app-cog.svg`). Axis = CUI icon name × plain/app-prefixed variant.
- `cisco-ui/build/fonts/cui-font.svg` (1464 lines) — CUI icon font.
- `customized-status-icons/` and `customized-status-icons-dark/` — ~18 status glyphs each (status-clock-countdown, status-degrade, status-eye, status-lock-close, status-lock-open, status-pause-circle, status-play-circle, status-question, status-queued, status-shield-check, status-shield-slash, status-shield-warning, status-wrench, status-x-square, status-nagative, status-positive, status-ai-assistant, icon-role-activepy). Axis = light/dark theme pair.
- `fonts/icomoon.svg`, `fonts/icon-font.svg`.
- `images/` (in `src/assets/images/`):
  - `ccp/` — 12 icons with active/default pairs (job-manager, licensing, live, network-design, network-models, collector).
  - `cdg/checkboxes_clear.svg`.
  - `checkboxes_assets/` — 17 checkbox state SVGs (off/on × normal/hover/pressed/disabled/focus).
  - `icons-svg/` — ~100 assorted icons (Alerts-blue-24, Filters-blue-24, Indicator-blue-24, Network-Switcher, Overview, Provisioning, Teleworker-Gateway — each with blue/grey 24-px variants; plus device card SVGs: `card_8800.svg`, `card_asr9000.svg`, `card_asr9900.svg`, `card_asr9k.svg`, `card_generic.svg`, `card_ncs1000.svg`, `card_ncs500.svg`, `card_ncs540.svg`, `card_ncs5500.svg`, `card_ncs560.svg`; plus status glyphs: critical, major, minor, warning, cleared, checking, reachable, unreachable, up, down, enabled, in-service, out-of-service, paused, maintenance, not-installed, null, queued, verified, waiting, etc.; plus navigation: `nav-tags.svg`, `nav-workflows.svg`; plus topo: `topo-optical-node.svg`; utility: `rocket-20.svg`, `lock-simple-20.svg`, `eye_16.svg`, `squares-four-20.svg`).
  - `kpi-icons/` — 30+ KPI-family icons (CPU, Memory, LLDP, BGP, OSPF, ISIS, QoS, ACL, CPP, IPSLA, LAG, Envmon, Layer1/2/3-* families, Platform-Errors).
  - `radio_assets/` — 9 radio-button state SVGs.
  - `states/` — 4 state icons (up/down/degraded/unknown).
  - Top-level per-feature nav pairs: `Administration-active(-dark).svg` + `Administration-default(-dark).svg`; same pattern for Alerts, Dashboard, Device-Management, Network-Automation, Performance-Alerts, Services-Traffic-Engineering, Topology, Workflow-Automation. Axis = nav feature × state(active/default) × theme(light/dark).
- `phosphor-icons/SVGs Flat/bold/` — the **Phosphor icon library (bold weight)**, ~1,500+ files (alphabet-exhaustive: acorn, address-book, airplane*, alarm, alien, align*, arrow*, battery*, book*, calendar*, caret*, chart*, chat*, cloud*, code*, currency*, cursor*, file*, folder*, gender*, globe*, hand*, lock*, map-pin*, person*, shield*, smiley*, text-*, user*, warning*, etc.). Axis = alphabetical Phosphor icon names. This is the dominant contributor to the ~2,861 SVG count.
- `svg/` — top-level operational glyphs (alarmBell, alarms, clear, cluster, critical/major/minor/warning, geo-guide-first-loc[-dark], geo-guide-second-loc[-dark], geo-inactive-state, step1-lhs-arbiter-completed[-dark], step2-rhs-arbiter-completed[-dark], step3-arbiter-completed[-dark], more, pencil, information).
- `fonts/spicons/spicons.svg` (155 lines) + `src/css/spicons.css` (612 lines) — small-icon (sp) set.
- Vendor assets: `src/assets/vendor/jsoneditor/img/jsoneditor-icons.svg` (893 lines).

Organization axes summarized: (a) design system family — CUI vs Phosphor vs Magnetic-spicons vs per-product custom; (b) state pair — active/default, on/off, hover/focus/disabled; (c) theme — light/dark; (d) size — 16/20/24/30/40 px variants; (e) feature/domain scoping — app-icons, kpi-icons, ccp, cdg, geo, states.

## 8. Settings / preferences surface

Two candidate locations for a post-POC product-level global classic-view toggle:

- `src/app/container/setting/` — in-shell settings module with `setting.component.ts` (730 lines), `setting.template.html` (171), `setting.style.scss` (411), `setting.module.ts` (23), `setting.component.spec.ts` (883), and own `image/key-solid.svg`. Sized like a real user-settings surface. Most likely home for the global toggle.
- `src/app/robot-users/` — per-user management (user-management, role-management, change-password, new-password-hint-rule, data-subscription, active-session, web-socket). Where per-user preferences would go if the toggle is user-scoped rather than tenant/session-scoped.

A secondary surface to be aware of: `src/app/robot-users/data-subscription/` (58 lines HTML, 554 lines TS) — this tracks per-user data subscriptions and may already persist user-level preferences.

## 9. Build and deployment config

Root-level build/deploy artifacts:

- `angular.json` (194 lines) — Angular workspace config.
- `package.json` (177 lines); `package-lock.json` (30,389 lines); `package.prod.json` (13 lines).
- `tsconfig.json` (32), `tsconfig.app.json` (28), `tsconfig.spec.json` (27), `tslint.json` (173).
- `webpack.config.js` (5 — stub) and `custom-webpack.config.js` (13 — small extension).
- `browserslist` (9).
- `karma.conf.js` (58) — unit-test runner.
- `build.sh` (286 lines), `patch_version.js` (18), `i18n-verifier.js` (54), `ng2-nvd3.ts` (211).
- `Dockerfile` (37), `Dockerfile.dev` (17), `docker-compose.yml` (83).
- `Jenkinsfile` (336) — CI pipeline.
- `supervisor.conf` (21), `startup.sh` (76), `readiness.sh` (14), `app.js` (20).
- `README.md` (49), `PULL_REQUEST_TEMPLATE.md` (92), `CODEOWNERS` (3), `.gitignore` (55), `.eslintrc.json` (97), `.eslintignore` (1), `.npmrc` (8), `.cursorrules` (13).
- Environment config files under `config/environments/`: `environment.js`, `environment.prod.js`, `environment.optims.js`, `environment.robot110.js`, `config.in`. Per-env frontend config switching happens here.
- Environment TS files under `src/environments/`: `environment.ts` (16), `environment.prod.ts` (3).
- `config/tykConfigMap.json` (52) — Tyk API gateway config (reverse-proxy for shell → backend calls).

Companion **Go** `ui-backend-service/` (hosted in the same repo) has its own `Makefile` (161), `go.mod` (101), `go.sum` (349). It exposes HTTP endpoints under `src/ui/httpserver/handler.go` (666 lines) + `server.go` (44 lines), with `src/controller/common/http_endpoint_defs.go` (48 lines) and protobuf message contracts in `config/proto/` (`ui_query.proto`, `ui_response.proto`, `error.proto`, `error_ui.proto`). Services include `service/journey/wizard_service.go` (345 lines) + `wizard_db_service.go` (119) and `service/tier/TierService.go` (553). This is the backend that powers the shell's wizard/onboarding journey + cluster-tier sizing — relevant context for how "shell" state is persisted but not a classic-view concern.

## 10. Integration touch points for the classic view

If classic EMS code lives as a feature subfolder (e.g. inside `unified-ems-ui`), Infra UI exposes the following integration surfaces, inferred from names and file sizes:

- **Route-mount contract:** `src/app/container/robot-shell/robot-shell.routes.ts` (181 lines) — the single entry point for registering additional lazy-loaded feature modules into the shell's `<router-outlet>`. A classic-view feature module would be added here (e.g., a new `{ path: 'classic-inventory', loadChildren: () => import(...) }` entry).
- **Layout slot / router outlet:** `src/app/container/robot-shell/robot-shell.component.html` (1 line — almost certainly just `<router-outlet>`), rendered inside `src/app/container/shell/shell.template.html` (35 lines) below `header` and alongside `navigation`.
- **Header injection surface:** `src/app/container/header/header.component.ts` (1578 lines) + `header.template.html` (159 lines). If a local toggle needs header-area UI, this is the component; a product-level global toggle would also land here.
- **Navigation registration:** feature must become visible in the nav tree either by: (a) inclusion in `src/assets/modules.json` (300 lines) or (b) dynamic registration through `src/app/services/module.service.ts` (401 lines) against `src/app/models/module.model.ts`. Icon assets under `src/assets/app-icons/` would need bw/color 30/40 px pairs matching existing convention.
- **Theme-variable contract:** global styles at `src/styles.scss` (2265 lines) plus Magnetic tokens at `src/css/magnetic-tokens.scss` (90), `magnetic-light-classic.scss` (723), `magnetic-dark-classic.scss` (723). The presence of Magnetic files already named `-classic` is the single most interesting finding — the theming surface for "classic" may already partially exist. The Harbor scope fix at `src/harbor-global-styles-scope-fix.ts` (60 lines) is the mechanism used to prevent Harbor-global CSS from bleeding across component boundaries; an analogous scope-fix may be needed if classic CSS coexists with Harbor in the same page.
- **Foreign-service delegate pattern:** `src/app/shared/foreign-service/` — delegate services (`inventory-delegate.service.ts`, `provider-delegate.service.ts`, `cdg-inventory-delegate.service.ts`, `cdg-utils-delegate.service.ts`, `cdgAdmin-delegate.service.ts`, each 7 lines) plus `foreign-service.module.ts` (54). This is the public service-API seam for features that need to call into Infra UI–owned services or vice versa.
- **i18n contract:** `src/assets/i18n/en.json` (4481 lines) is the central English string catalog; per-module i18n dirs (`src/assets/aa/i18n/en.json`, `src/assets/cdg/i18n/en.json`, `src/assets/cw-components/i18n/en.json` at 2985, plus `ja.json` at 2998) show the module-scoped pattern a classic-view module would follow.
- **Interceptor chain:** `src/app/session-expired.interceptor.ts` and `src/app/logging.interceptor.ts` wrap every HTTP call the feature layer makes through the shell. Any classic-view API traffic will run through these.
- **Cert-management mock:** `mock/cert-mgmt.ts` (114 lines) — example of how mocks are provided alongside the real module, useful pattern for POC dev.
- **Existing fault-management feature module:** `src/app/robot-alarms-v2/` is already the modern alarms/fault module in Infra UI (alarm-notification, alarm-policy, device-alarms-and-events, alarms-actions, alarms-base, alarms-header, page-container, plus services `alarm-notification.service.ts` at 676 lines, `alarm-policy.service.ts` at 621 lines, `device-alarms-and-events.service.ts` at 638 lines, and `robot-alarms-v2.service.ts` at 286 lines). There is also an older `src/app/robot-alarm/` (robot-alarm.component.ts at 1489 lines, robot-alarm.service.ts at 1007 lines). **For the POC Fault Management scope, classic-view fault pages would mount as a sibling route to robot-alarms-v2 and share the alarm data services.**

### Open questions / flags for the POC

1. The Magnetic files literally named `magnetic-light-classic.scss` / `magnetic-dark-classic.scss` need a confirmation pass: is "classic" here the EPNM classic UI concept, or a Magnetic design-system tier name (classic vs modern)? This is the single biggest ambiguity for theming.
2. `mockup-code-conversion.md` at repo root (1046 lines) is suggestive — may be an internal guide for converting mockups to code (possibly EPNM → EMS conversion notes). Worth a read beyond this tree report.
3. `CODEOWNERS` is only 3 lines — ownership routing is thin; the PR-review rules live in `.review/ui-pr-review-rules.md` (821 lines) instead.
4. No Module Federation evidence. A classic-view layer running inside `unified-ems-ui` must integrate at build time (monorepo build) or via Angular lazy route + npm dependency — not as a separately deployed remote. Confirm with the repo owner.
5. `src/app/entry/` (22 / 188 lines) is a small entry shell that sits alongside `container/` — its relationship to `robot-shell` is not clear from names alone and warrants inspection.
