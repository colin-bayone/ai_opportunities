# Cross-Repo POC Map
**Session 2, 2026-04-21. Synthesis of the 10-agent tree-report absorption.**

## How to Read This Document

- Left column is an area of POC scope (Inventory sub-surfaces, Fault sub-surfaces, cross-cutting concerns).
- Right columns identify EPNM-side code locations (source of the classic UX) and EMS-side code locations (where the classic rebuild consumes and integrates).
- All cited paths are verbatim from the tree reports. None of them have been opened in actual source. File names are evidence of purpose, not proof.
- **Scope discipline (Colin 2026-04-21):** Session 2 surfaces candidate paths; the execution session (on the Cisco Mac) decides what is actually needed for the POC. Do not treat anything below as committed-in-scope.

Agent extractions with full detail are in this same `_scratch_repo/` folder
as `agent_NN_*.md`. This document is the cross-cutting map.

---

## 1. The Big Picture in One Diagram

```
EPNM SIDE (what the classic UX must faithfully reproduce)
───────────────────────────────────────────────────────────
  pf-framework/ui/core/ui_components   ← framework widgets (xwt, dojo)
        ↑ depended on by
  assembly/ifm_platform_ui             ← Inventory UI + Fault UI (runtime)
  inventory/comp/ifm_inventory_*       ← Inventory backend (Java, Oracle)
  fault/{ifm_fault, xmp_correlation,   ← Fault backend (Java, Oracle)
         ncs_eventAlarm, ncs_syslog,      + policy mgmt UI (out of scope)
         xmp_syslog}
  chassisview                          ← Chassis visualization (SVG + JS + Java)

EMS SIDE (what the classic rebuild lives inside and talks to)
───────────────────────────────────────────────────────────
  infra-ui                   ← Angular app shell. Routes, nav, theme foundations.
        ↓ lazy-loads
  unified-ems-ui             ← Angular *library* (projects/ems-lib). Feature pages.
        ↑ uses
  common-ui                  ← Shared Angular components (cw-hbr-*, cui-*, base360).
         ───                 │
                             │  HTTP
                             ↓
  cw-inventory               ← Inventory REST (Spring Boot, 8 REST services).
  cw-inventory-collector     ← Collector service (Spring Boot + gRPC).
  cw-epnm-fault              ← Fault REST (Spring Boot, Docker-first).
  ems-assurance              ← Fault support (ADS-only, no Docker for main svc).
```

Both EPNM-side feature repos (assembly, inventory, fault) depend on the
framework repo (pf-framework). The EPNM side does not run locally; it needs
the EPNM VM once provisioned (action item A2 in handoff doc 09).

The EMS side is a classic Spring Boot + Angular shell-app shape. Local-run
is plausible for parts of it (cw-epnm-fault, both inventory services,
infra-ui). Open question 3.8 captures the specific investigation.

---

## 2. Inventory — POC Part 1

### 2.1 Network Devices (list + filters + toolbar actions)

| Aspect | EPNM source (reference / classic behavior) | EMS host (classic lives here, consumes these) |
|---|---|---|
| List widget | `assembly/ifm_platform_ui/.../inventory/js/InventoryListView.js` (8,020 lines) | `unified-ems-ui/projects/ems-lib/src/app/device-management/network-inventory/` |
| Table primitive (EPNM) | `pf-framework/ui/.../xwt/widget/table/Table.js` (5,146 lines) + `themes/prime/xwt/table/Table.css` | — |
| Table primitive (EMS) | — | `common-ui/.../cw-hbr-table/` (1,566 lines, Harbor-themed, needs classic wrapper) OR `common-ui/.../ag-grid-table/` (theme-neutral, with existing `theme-*` stack) |
| Device-add wizard primitive | `pf-framework/ui/.../xwt/widget/tasknavigator/TaskNavigator.js` (1,312) | `common-ui/.../cui-stepper/` (612 lines, theme-neutral) + `cui-input`, `cui-select`, `cui-datetime-select`, `cui-modal` |
| Bulk CSV import | Pattern lives in assembly; backend in `inventory` — needs source read | `cw-inventory/.../BulkImportRootResource.java1` (**NOTE: `.java1` extension — appears parked**) |
| REST contract | `inventory/comp/ifm_inventory_rest_provider/.../InventoryRestService.java` (8,770 lines) | `cw-inventory/.../InventoryRestService.java` (9,724 lines), `NetworkInventoryRestService.java` (323), `InventoryEMSRestService.java` (1,696) |
| Tyk gateway route map | — | `cw-inventory/config/platform/tyk/tykConfigmap.json` (read first for public API contract) |
| State scheduling (maintain/managed) | inventory repo (ifm_inventory_service_package) — needs source read | `cw-inventory/.../JobSchedulerRestService.java` (9,671 lines), `InventoryJobRestService.java` (903) |

**Open question 1.5 (bulk-import CSV schema).** The `.java1` extension on the bulk import resource on the EMS side is a flag. If bulk import is in POC scope for the device-add flow, this needs Selva's direction.

### 2.2 Device Details (left menu + main view + chassis on left)

| Aspect | EPNM source | EMS host |
|---|---|---|
| Device Details runtime UI | `assembly/.../DeviceDetailsPage.js`, `VdcDetails.js`, `esChassisDetail.html` | `unified-ems-ui/projects/ems-lib/src/app/inventory-details/` + `inventory-panel/` (node-details, node-alarms, node-level-config) |
| Left-menu tab enumeration | `inventory/comp/ifm_inventory_ui_metadata_impl/.../DeviceDetailTabViewMetadata.json` + siblings (**highest-leverage artifact — likely resolves open question 1.2**) | — |
| Left-nav widget primitive | `pf-framework/ui/.../xwt/widget/navigation/SlideMenu.js` (2,394) | `infra-ui/src/app/container/navigation/` (703 + 1,197 SCSS) |
| Device-content assembly | — | `inventory/comp/ifm_inventory_rest_provider/.../InventoryDTOBuilder.java` (3,269) |

### 2.3 Chassis View (left side of Device Details)

| Aspect | EPNM source | EMS host |
|---|---|---|
| Chassis visualization | `chassisview/` — ~3,008 files dominated by SVG (2,124 files, ~5M lines), JS (186), JSON (396) | Not located in tree reports. Candidate: new component inside `unified-ems-ui/projects/ems-lib/src/app/inventory-details/`. |
| Interactive layer | `chassisview/.../hotspot/` (`portState.js`, `moduleState.js`, `cardDetails.js`, ~11 files) — **substantive, not trivial** | — |
| SVG asset organization | `chassisview/.../svg/<device-family>/chassis/{horizontal,vertical,flip}/...` (pluggables embed Nexus etc.) | — (execution session decides whether to port SVGs in-place, reference them by URL from a served asset store, or have an EMS-side SVG library) |
| Backend service | `chassisview/.../ChassisViewServiceImpl.java` (2,897 lines) | **NOT CONFIRMED present on EMS side.** Open question 1.8 says this may fall in the 10-20% gap. Agent sweep did not see a chassis-specific EMS backend. |

**Open question 1.8 (chassis interactivity reimplementation status on EMS) gets sharper.** The EPNM interactive layer is ~11 files with state semantics; a 2,897-line backend service sits behind it. If the EMS side has no equivalent (the tree reports did not surface one), this is a candidate gap item requiring Selva's direction. Flag for the execution session to verify by reading EMS inventory source before concluding.

### 2.4 Device 360 (popup) and Interface 360 (nested popup)

| Aspect | EPNM source | EMS host |
|---|---|---|
| 360 popups (EPNM) | `assembly/.../_360/` templates + metadata JSON; renders via generic `PropertySheet`/_360 framework (not a dedicated Interface360.js) | — |
| Device picker | `pf-framework/ui/.../xwt/widget/objectselector/ObjectSelector.js` (6,929 lines) | — |
| 360 shell (EMS) | — | `common-ui/.../base360/` with `device360/`, `interface360/`, `link360/`, `generic-links/` — **this is the host for the nested 360 pattern** |
| Device 360 feature | — | `unified-ems-ui/projects/ems-lib/src/app/inventory-details/inventory-details-device360/` |
| Interface 360 candidate | — | `unified-ems-ui/projects/ems-lib/src/app/shared/interface-list/` |

### 2.5 Inventory — EMS service-layer entry points

| Purpose | Path |
|---|---|
| Primary inventory REST | `cw-inventory/.../InventoryRestService.java` (9,724) |
| EMS-flavored inventory | `cw-inventory/.../InventoryEMSRestService.java` (1,696) |
| Job scheduling | `cw-inventory/.../JobSchedulerRestService.java` (9,671), `InventoryJobRestService.java` (903) |
| Diagnostics | `cw-inventory/.../DiagnosticsRestService.java` (882) |
| Interface (for 360) | `cw-inventory/.../EMSInterfaceRestService.java` (60) — tiny file, worth reading |
| Controllers | `InventoryController`, `HealthController`, `LoggerController` |
| gRPC contract (inventory ↔ collector) | `inventory.proto` |
| Local profile | `LocalProfileConfig.java` in both `cw-inventory` and `cw-inventory-collector` |

**Note:** Both inventory repos are Spring Boot / Java. Any hardware-integration or device-management backend services (which might be implemented in other languages) are out of scope — the POC is a UI reskin against existing EMS REST APIs.

---

## 3. Fault Management — POC Part 2

### 3.1 Alarms table

| Aspect | EPNM source | EMS host |
|---|---|---|
| Alarms runtime UI | `assembly/.../AlarmListView.js` (**runtime UI is in assembly, not fault repo**) | Existing UI at `infra-ui/src/app/robot-alarms-v2/`. Classic mounts as sibling or via theme. |
| Table primitive | `pf-framework/ui/.../xwt/widget/table/Table.js` (5,146) + `AlarmsFormatter.js` (103, framework-level severity formatting) | `common-ui/.../cw-hbr-table/` (alarms table today) or ag-grid with a new `theme-classic.css` |
| Correlated alarms | `assembly/.../CorrelatedAlarms.js`, `AlarmCorrelatedView.js`; correlation engine at `fault/xmp_correlation/` | TBD — probably `cw-epnm-fault/.../CWRestController.java` (needs confirmation) |
| REST contract (EPNM) | `fault/.../AlarmRest.java` (7,969 lines) | — |
| REST contract (EMS) | — | `cw-epnm-fault/alarm-rest/alarm-rest-service/AlarmRest.java` (2,622) + `AlarmUpdateRestController.java` + `AlarmActionServiceImpl.java` |
| Expandable-row detail candidate | EPNM fault service layer | `cw-epnm-fault/.../View360AlarmController.java` (717) |
| Custom alarms | — | `cw-epnm-fault/.../CustomAlarmsController.java` (1,321) |
| Advanced filter grammar | EPNM fault service layer — needs source read | `cw-epnm-fault/.../FilterCriteriaUtil.java` (797) + two `AlarmFilterDTO` variants (188 / 399 lines). Disambiguate in source. |
| Inventory-side bridge (alarms inside Device 360) | — | `cw-epnm-fault/.../NetworkInventoryAlarmController.java` (180) |
| Public route inventory | — | `cw-epnm-fault/alarm-rest-config-cw-emf/platform/tyk/tykConfigmap.json` (386 — read first) |
| EPNM-twin reference | — | `ems-assurance/fault-nbi/ems-fault-nbi/.../AlarmRestServiceImpl.java` (821) |

**Open question 1.14 (real-time alarm update mechanism).** EPNM side: `NotificationWebSocket` pipeline in the fault repo. WebSocket is the probable pattern (and the name `SyslogListViewWebSocket` in assembly confirms the style for at least one channel). EMS side: NATS, gRPC, Kafka, and JMS are all present in the tree — which of them drives UI live updates is open and requires a source read.

**Gap risk (from agent 10).** `NetworkImpactingAlarm` and `NextStep` exist only in `ems-assurance` (EPNM-era fault NBI), not in `cw-epnm-fault` (EMS-era). If the classic UI consumes either, that's a backend gap — applies risk 6.11 in handoff doc 10. Needs a source read to confirm usage.

### 3.2 Events

| Aspect | EPNM source | EMS host |
|---|---|---|
| Events table UI | `assembly/.../EventListView.js` | TBD — probably handled inside `cw-epnm-fault/.../AlarmRest.java` with an event-type filter. Likely no dedicated EventsRestController. |
| Events domain | `fault/ncs_eventAlarm/`, `fault/xmp_syslog/`, `fault/xmp_correlation/` (server side) | `cw-epnm-fault/*` (no dedicated events controller surfaced) |

**Open question 1.17 (time-based filtering on events) and 1.18 (popup vs. full page relationship).** Both are source-read items — the tree reports don't resolve them.

### 3.3 Syslogs

| Aspect | EPNM source | EMS host |
|---|---|---|
| Syslog UI | `assembly/.../SyslogListViewWebSocket.js` (name implies WebSocket stream) | TBD — agent 10 did not find a dedicated syslog REST controller on EMS side |
| Syslog backend | `fault/ncs_syslog/`, `fault/xmp_syslog/` | Needs confirmation from Jenis / source read in `cw-epnm-fault` and `ems-assurance` |

**Highest under-documented area.** Syslogs are the single least-resolved corner of POC scope. If Fault Management is ranked ahead of Inventory for first-screen work, the syslog piece is the main risk.

---

## 4. Cross-Cutting — Where the Classic View Mounts

### 4.1 Classic-view code placement candidates

Based on evidence:

1. **Inside `unified-ems-ui`'s library at `projects/ems-lib/src/app/classic/`** — most likely. Sibling to existing feature directories (`inventory-details/`, `inventory-panel/`, `device-management/`, `shared/`). Builds as part of the library; consumed by `infra-ui`'s lazy routes. This matches Akhil's "part of the new EMS build" constraint.

2. **Inside `infra-ui` at `src/app/classic/`** — plausible for fault screens since the runtime alarms UI (`robot-alarms-v2/`) lives in infra-ui already. Less clean because infra-ui is the shell app, not the feature layer.

3. **New standalone repo** — Akhil's alternate. Requires more coordination and is not the natural shape given the Angular library pattern.

Recommendation for Colin's `B2` code-organization proposal: option 1 for Inventory screens, with a decision about fault placement pending confirmation of where `robot-alarms-v2` actually lives architecturally.

### 4.2 Route / navigation integration points

- `infra-ui/src/app/container/robot-shell/robot-shell.routes.ts` (181 lines) — the feature-mount route table. Classic routes register here.
- `infra-ui/src/assets/modules.json` (300 lines) + `module.service.ts` (401 lines) — data-driven navigation. Classic menu entries added via modules.json.
- `unified-ems-ui/projects/ems-lib/src/app/ems.routes.ts` — the library's internal route aggregator.
- `unified-ems-ui/projects/ems-lib/src/app/root-ems.module.ts` + `public-api.ts` — how the library exposes itself to the shell.

### 4.3 Theming plumbing

- **Naming collision alert.** `infra-ui/src/css/magnetic-light-classic.scss` and `magnetic-dark-classic.scss` already exist (723 lines each). The word "classic" is not unclaimed in this codebase — "classic" inside Magnetic is a tier, not the EPNM reskin. Use a distinct prefix for our work: `epnm-classic-*` or similar.
- **CSS custom-property approach** remains the right strategy (handoff doc 06 §6). Add a new `:root[data-theme="epnm-classic"]` variable set in infra-ui's global SCSS.
- **EPNM blue-and-white palette is distributed across pf-framework.** No single palette file. Extraction into tokens will require the execution session to survey `xwt/themes/prime/*.css` and pick representative values.

### 4.4 Shared-service + display-adapter pattern

- `unified-ems-ui/projects/ems-lib/src/app/shared/service/ems-api.service.ts` — the central REST wrapper. Classic components call into this, same as modern components. No parallel service layer.
- `infra-ui/src/app/shared/foreign-service/` — delegate pattern for cross-app service calls. Relevant if classic code needs to talk to shell-provided services.
- Adapters go in a new `classic/adapters/` directory with `epnm-display.adapter.ts` per the pattern in handoff doc 06 §7.

### 4.5 Component reuse catalog (high-level)

| Reuse category | Examples from common-ui | Disposition for classic |
|---|---|---|
| Direct reuse (theme-neutral) | `cui-stepper`, `cui-input`, `cui-select`, `cui-checkbox`, `cui-radio`, `cui-datetime-select`, `cui-modal` | Use as-is; theme via CSS variables |
| Wrap with classic variant | `cw-hbr-table`, `cw-hbr-*` (Harbor-themed) | Wrap — classic table variant reads theme variables and renders EPNM-style |
| Theme extension | ag-grid (existing `theme-blue/bootstrap/dark/fresh/material`) | Add new `theme-classic.css` — lowest-risk table path |
| Reuse shell | `base360/` (device360, interface360, link360, generic-links) | Use the shell; apply classic content components inside |

---

## 5. Open Questions Resolved or Refined by the Tree-Report Pass

These map back to items in handoff doc 10 (`10_open_questions_and_risks.md`).

| Open Q | Status after tree reports |
|---|---|
| 1.2 Device Details left-menu enumeration | Likely resolved in source by `inventory/comp/ifm_inventory_ui_metadata_impl/.../DeviceDetailTabViewMetadata.json`. Execution session reads this first. |
| 1.8 Chassis interactivity reimplementation | Still open. EPNM side is substantive (`hotspot/` interactions, 2,897-line `ChassisViewServiceImpl.java`). EMS side: no dedicated chassis backend surfaced. High-probability gap candidate. |
| 1.14 Alarm real-time update | Partial. EPNM side: WebSocket (`NotificationWebSocket`, `SyslogListViewWebSocket`). EMS side: NATS / gRPC / Kafka / JMS all present — exact UI subscription pipe needs source read. |
| 1.15 Expandable-row content | Likely `cw-epnm-fault/.../View360AlarmController.java` (717 lines). Source read confirms. |
| 1.11 Advanced filter structure | `cw-epnm-fault/.../FilterCriteriaUtil.java` (797) + two AlarmFilterDTO variants. Ambiguity to disambiguate in source. |
| 2.2 Shell loading mechanism | Resolved: standard Angular lazy `loadChildren` via `robot-shell.routes.ts`. No Module Federation. |
| 2.3 Common UI consumption | Library pattern: `unified-ems-ui` is itself a library; `common-ui` is a library consumed via the internal npm registry (`.npmrc`). |
| 2.6 Go services on EMS backend | Not relevant to the POC. This is a UI reskin against existing EMS REST APIs; any hardware-integration or device-management service language choice is out of scope. Keeping in the open-questions list for completeness but not pursuing. |
| 2.7 10-20% backend gap for POC screens | Concrete gap candidates: bulk-CSV import (`.java1` extension), chassis interactivity backend, `NetworkImpactingAlarm`, `NextStep`. |
| 3.8 Local runnability (NEW) | Partial. `cw-inventory`, `cw-inventory-collector`, `cw-epnm-fault` have Dockerfiles and/or LocalProfileConfig. `ems-assurance` is ADS-only. Infra-ui should run standalone with `ng serve` or the custom-webpack variant — needs verification. End-to-end local-run status remains open; specific investigation steps in `_kickoff_context_2026-04-21.md` §9. |

---

## 6. New Risks or Flags from the Tree-Report Pass

1. **"Classic" is an overloaded term in this codebase.** `magnetic-*-classic.scss` already exists. Use a distinct prefix for our work.
2. **Bulk CSV import on EMS inventory is in a parked state.** `.java1` file extension. If in POC scope, raise to Selva.
3. **Chassis interactivity may be an EMS gap.** EPNM side is substantive; no EMS equivalent surfaced in the tree.
4. **`ems-assurance` is ADS-only.** If POC needs the EPNM-era alarm NBI (`AlarmRestServiceImpl.java`, NetworkImpactingAlarm, NextStep), ADS access is required.
6. **The XWT widget layer is distinct from base Dojo.** Cisco layered its own widget toolkit on Dojo (`xwt/*`). The conversion patterns in handoff doc 06 target Dojo primitives; XWT-specific patterns will need to be added once the execution session surveys actual source.
7. **Three grid generations in EPNM** (dojox DataGrid, EnhancedGridWrapper, XWT Table.js). Which one Inventory and Alarms actually use is unconfirmed. Widget mapping in handoff doc 06 §2 may need a fourth row for the XWT Table.js case.

---

## 7. Read-Order Recommendation for the Execution Session

When the execution session opens actual source (on the Cisco Mac), suggested order to build the first internal map fastest:

1. `unified-ems-ui/projects/ems-lib/src/app/ems.routes.ts` and `root-ems.module.ts` — library entry / exports.
2. `infra-ui/src/app/container/robot-shell/robot-shell.routes.ts`, `modules.json`, `module.service.ts` — how features mount.
3. `infra-ui/src/app/robot-alarms-v2/` — existing alarms UI. Classic fault reskin baseline.
4. `unified-ems-ui/projects/ems-lib/src/app/device-management/network-inventory/`, `inventory-details/`, `inventory-panel/` — existing inventory UI.
5. `cw-inventory/config/platform/tyk/tykConfigmap.json` — the public API contract for inventory.
6. `cw-epnm-fault/alarm-rest-config-cw-emf/platform/tyk/tykConfigmap.json` — the public API contract for alarms.
7. `cw-inventory/.../InventoryRestService.java` (entry points only — do not read the full 9,724 lines at once).
8. `cw-epnm-fault/alarm-rest/alarm-rest-service/AlarmRest.java` (entry points only).
9. `inventory/comp/ifm_inventory_ui_metadata_impl/.../DeviceDetailTabViewMetadata.json` — the Device Details left-menu truth.
10. `assembly/ifm_platform_ui/.../inventory/js/InventoryListView.js` — the EPNM Inventory list. Start with its `postCreate` lifecycle method.
11. `assembly/.../AlarmListView.js`, `EventListView.js`, `SyslogListViewWebSocket.js` — the EPNM Fault surface.
12. `pf-framework/ui/.../xwt/widget/table/Table.js` — the XWT table primitive (if Inventory and Alarms use it, which is likely).
13. `common-ui/.../cw-hbr-table/` + `ag-grid-table/` — decide table path.

All subsequent reading flows from these.

---

## 8. What This Synthesis Does Not Cover

- **Actual topic names in the Dojo pub/sub web.** Only visible in source, not in the tree.
- **Actual route names in the Tyk configmap.** Needs source read.
- **Angular service implementations.** The tree shows which files exist, not how they call the backend.
- **Shell-to-library mount details.** How infra-ui actually loads ems-lib features — needs source read.
- **Harbor vs. Magnetic relationship** (open question 2.4). Names surfaced but relationship not clarified by the tree alone.

All of these are execution-session tasks. Session 2's role stops at the map.
