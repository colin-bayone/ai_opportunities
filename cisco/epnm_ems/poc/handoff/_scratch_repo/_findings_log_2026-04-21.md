# Tree-Report Swarm — Running Findings Log
**Session 2, 2026-04-21**

Durable capture of findings from the 10-agent absorption pass. Each agent
returns a structured extraction into `agent_NN_*.md` in this folder. This log
is the running high-signal summary Colin reads. It will also seed the
cross-repo POC map synthesis once all ten agents are in.

Colin direction (2026-04-21): "We don't specifically know if all of this is
actually part of the task at hand. These libraries and stuff could be
relevant, or they could be completely irrelevant. Part of the job of the
other session is going to be to figure out what is actually needed versus
what is not." Session 2 surfaces what exists; the execution session is the
authority on what is in scope for the POC.

---

## Agent Status

| # | Target | Status | Extraction |
|---|---|---|---|
| 01 | EPNM assembly | complete | `agent_01_epnm_assembly.md` |
| 02 | EPNM chassisview | complete | `agent_02_epnm_chassisview.md` |
| 03 | EPNM inventory | complete | `agent_03_epnm_inventory.md` |
| 04 | EPNM fault | complete | `agent_04_epnm_fault.md` |
| 05 | EPNM pf-framework | complete | `agent_05_epnm_pf_framework.md` |
| 06 | EMS unified-ems-ui | complete | `agent_06_ems_unified_ems_ui.md` |
| 07 | EMS infra-ui | complete | `agent_07_ems_infra_ui.md` |
| 08 | EMS common-ui | complete | `agent_08_ems_common_ui.md` |
| 09 | EMS inventory backend pair | complete | `agent_09_ems_inventory_backend.md` |
| 10 | EMS fault backend pair | complete | `agent_10_ems_fault_backend.md` |

---

## Cross-Cutting Findings (so far)

### A. Where the POC code probably lives — concrete signal

- **`unified-ems-ui` is an Angular library** (`projects/ems-lib/`), not an app.
  It is consumed by the outer `infra-ui` shell. Bootstraps do not live here.
  Candidate classic-view placements inside the library: `src/app/classic/`
  as a sibling to existing domain dirs, or nested under existing feature
  directories.
- **Existing fault UI actually lives in `infra-ui`** at
  `src/app/robot-alarms-v2/` — not in `unified-ems-ui`. A classic fault
  surface would mount as a sibling in infra-ui or as a classic-themed
  parallel to robot-alarms-v2. This is contrary to what one might assume
  from the "unified-ems-ui is the primary working repo" framing in the
  handoff.
- **Inventory UI in unified-ems-ui** is richer: `inventory-details/`,
  `inventory-panel/`, `device-management/network-inventory/`,
  `shared/interface-list/` are all present and named.
- **infra-ui routes features via standard Angular lazy `loadChildren`**. No
  Module Federation evidence. `container/robot-shell/robot-shell.routes.ts`
  is the feature-mount route table.
- **Navigation is data-driven**: `src/assets/modules.json` + `module.service.ts`
  in infra-ui. Classic routes can be injected by extending that config.

### B. Shared component reuse policy gets sharper

- **Tables**: `cw-hbr-table` (Harbor-themed, 1,566-line component) is what
  alarms and network-devices tables use today. Two classic paths, both in
  common-ui precedent:
  1. Lower risk: a `theme-classic.css` added to the ag-grid theme pack
     alongside the existing `theme-blue/bootstrap/dark/fresh/material/`.
  2. Higher value: prove CSS-variable theming on `cw-hbr-table` itself.
     Requires reading `cw-hbr-table.component.scss` to decide.
- **Wizard primitives for the device-add flow exist and are likely theme-neutral**:
  `cui-stepper` (612 lines), `cui-input`, `cui-select` (983 lines),
  `cui-checkbox`, `cui-radio`, `cui-datetime-select` (968 lines),
  `cui-modal` (350 lines). `cui-*` prefix is a direct-reuse candidate;
  `cw-hbr-*` prefix needs wrappers.
- **360 shell exists**: `base360/` with `device360/`, `interface360/`,
  `link360/`, `generic-links/` — directly relevant to the Inventory
  nested-360 pattern.

### C. Naming collision — "classic" is ambiguous

- Infra-ui has `magnetic-light-classic.scss` and `magnetic-dark-classic.scss`
  already present. "Classic" is not unclaimed terminology inside this
  codebase. Strongly recommend prefixing our work distinctively —
  `epnm-classic-*` or similar — to avoid confusion with existing Magnetic
  tier naming.

### D. EPNM-side code — POC-critical paths

- **`InventoryListView.js`** confirmed at
  `ifm_platform_ui/src/main/webapp/applications/inventory/js/InventoryListView.js`
  (EPNM/assembly). 8,020 lines. The central inventory list widget.
- **Fault UI is in the `assembly` repo**, not the `fault` repo. `assembly`
  contains `AlarmListView`, `EventListView`, `SyslogListViewWebSocket`,
  `CorrelatedAlarms`, `AlarmCorrelatedView`. Matches Akhil's
  "assembly is on the UI side" in the walkthrough.
- **`SyslogListViewWebSocket`** file name hints **WebSocket** is the
  real-time update mechanism for syslogs at least — partial answer to
  open question 1.14 in handoff doc 10. The alarms real-time mechanism
  may be similar; needs agent 04 (EPNM fault) to confirm by seeing whether
  alarms view has a parallel WebSocket-named file.
- **`DeviceDetailTabViewMetadata.json`** flagged as likely the single
  highest-leverage artifact for Device Details left-menu enumeration —
  partial answer to open question 1.2.
- **`InventoryRestService.java`** (EPNM/inventory) is 8,770 lines. The
  EPNM side's main REST entry; 50+ DTOs in the package including `*360`
  neighbor DTOs and VDC/VPC DTOs.
- **Bridge code already exists**: `EMSInterfaceInfoBuilder.java` and
  `EMSInterfaceInventoryRequestHandler.java` inside EPNM/inventory.
  Names imply EMS-compatibility hooks that predate this POC. Worth
  reading to understand what's already in place before building new
  adapters.
- **Chassis view interactivity is substantive**: EPNM/chassisview has a
  dedicated `hotspot/` interaction layer (`portState.js`, `moduleState.js`,
  `cardDetails.js`, 11 files total). `ChassisViewServiceImpl.java` alone
  is 2,897 lines. Chassis interactivity is not a trivial reimplementation.
  Reinforces open question 1.8 (interactive chassis reimplementation status
  on EMS side).

### E. EMS backend — findings

- **Both `cw-inventory` and `cw-inventory-collector` are Spring Boot / Java.**
- **Bulk import looks parked**: `BulkImportRootResource.java1` — the `.java1`
  extension is not Java-compilable. Likely backend gap for the Inventory
  device-add bulk-CSV flow. Might need Selva's direction if this is a POC
  requirement.
- **No committed OpenAPI / Swagger descriptor**: only `SwaggerConfig.java`
  exists. The classic UI will need to pull the live API contract from a
  running instance to map endpoints — another dependency on local-run or
  VM access.
- **Primary REST services in cw-inventory (Java):**
  - `InventoryRestService.java` (9,724 lines)
  - `JobSchedulerRestService.java` (9,671 lines)
  - `InventoryEMSRestService.java` (1,696 lines)
  - `InventoryJobRestService.java` (903 lines)
  - `DiagnosticsRestService.java` (882 lines)
  - `NetworkInventoryRestService.java` (323 lines)
  - `EMSInterfaceRestService.java` (60 lines)
- **Controllers exposed:** `InventoryController`, `HealthController`, `LoggerController`.
- **Tyk gateway map** at `config/platform/tyk/tykConfigmap.json` — the
  execution session should read this for the public-facing API contract.
- **gRPC**: `inventory.proto` exists — inter-service contract between
  cw-inventory and cw-inventory-collector likely.
- **`LocalProfileConfig`** class present in both inventory repos. Suggests
  local-run is possible; needs the execution session to verify end-to-end.
  Partial answer to open question 3.8.

### F. Scope-discipline reminder (Colin)

Session 2 surfaces candidate paths. The execution session (Colin on the
Cisco Mac) is the authority on what is actually needed. Everything above
is evidence, not commitment.

---

### G. EPNM fault repo (agent 04) — findings

- **The fault repo does NOT contain the runtime alarms-table UI.** Only the
  policy-management UI and a trap-notification widget live under this
  repo's `webapp/`. The runtime alarms list UI is in `assembly` (agent 01
  confirmed `AlarmListView.js` there) or server-rendered via JSP against
  the 7,969-line `AlarmRest.java` in this repo.
- **`AlarmRest.java` is 7,969 lines** — the EPNM fault REST service. Where
  the classic UI's alarm-data contract originates.
- **`NotificationWebSocket` pipeline** exists in the fault repo. Likely
  the alarm real-time delivery mechanism (parallel to
  `SyslogListViewWebSocket` in assembly). Partial answer to open question
  1.14 (alarm real-time update mechanism): WebSocket is the probable
  pattern.
- **Correlation engine** under `xmp_correlation/`. Root-cause correlation
  (Jenis's "correlated alarms") likely runs here.
- **Event / alarm / syslog domain subtrees** are each their own directory:
  `ncs_eventAlarm`, `ncs_syslog`, `xmp_syslog`, `xmp_correlation`, plus
  `ifm_fault/` with adapter / rest_provider / service / base_dto subdirs
  reflecting standard Cisco IFM layering.
- **Policy management UI** is the main in-repo UI and is out of POC scope.

### H. EPNM pf-framework repo (agent 05) — findings

- **Most of `pf-framework` is the provisioning engine, not UI.** Only the
  `ui/` subtree matters for the POC. The repo name is misleading for a
  Django-brained reader: "framework" here covers both provisioning runtime
  and UI framework.
- **Table primitive both Network Devices and Alarms likely use:**
  `ui/core/ui_components/lib/xwt/widget/table/Table.js` (5,146 lines) +
  `themes/prime/xwt/table/Table.css` (1,748 lines) + `Toolbar.css`
  (1,580). Under the "xwt" namespace — a Cisco internal widget toolkit
  layered on top of Dojo.
- **Branded chrome:** `xwt/widget/uishell/Header.js` (524 lines) + its
  template + `themes/prime/xwt/uishell/Header.css` (392). Where EPNM's top
  bar visually originates.
- **Left nav:** `xwt/widget/navigation/SlideMenu.js` (2,394 lines) +
  `slidemenu.css` (630).
- **Device-add wizard primitive:** `xwt/widget/tasknavigator/TaskNavigator.js`
  (1,312 lines). Very likely the Dojo wizard used by the Inventory
  device-add flow.
- **Device picker:** `xwt/widget/objectselector/ObjectSelector.js`
  (6,929 lines) — a large widget almost certainly used by the network-
  devices table and by Device 360 launch flows.
- **Three grid generations coexist**: dojox DataGrid, EnhancedGridWrapper,
  and the XWT `Table.js`. The execution session must confirm which
  generation Inventory and Alarms actually use. Likely XWT `Table.js` —
  newest and biggest — but needs confirmation.
- **Blue-and-white theme is distributed, not centralized.** No single
  palette file; color values are spread across per-component CSS files
  under `xwt/themes/prime/`. Classic-theme adoption on the Angular side
  will require either extracting tokens from the distributed CSS or
  picking a representative palette to reproduce.
- **Pub/sub plumbing:** `dojo/topic.js` (38 lines). Framework-level. Topic
  names used by Inventory and Fault widgets are not visible from the
  tree — embedded in individual widget source. The execution session
  catalogs these when reading actual source.
- **`AlarmsFormatter.js`** (103 lines) is the only named "Alarms" artifact
  in the framework layer. Suggests fault-specific rendering hooks
  (severity icons, color rules) exist in the framework.

---

### I. EMS fault backend pair (agent 10) — findings

- **Main classic-UI alarms surface:** `cw-epnm-fault/alarm-rest/alarm-rest-service/AlarmRest.java` (2,622 lines).
- **Write actions (clear / acknowledge / annotate):** `AlarmUpdateRestController.java` + `AlarmActionServiceImpl.java`.
- **Custom alarms CRUD:** `CustomAlarmsController.java` (1,321 lines).
- **Expandable-row detail candidate:** `View360AlarmController.java` (717 lines) — likely resolves open question 1.15 (expandable-row content source) once read.
- **Advanced-filter grammar:** `FilterCriteriaUtil.java` (797 lines) + two `AlarmFilterDTO` variants (188-line REST shape vs. 399-line subscription shape). Ambiguity: the advanced-filter builder's target DTO is unclear from names alone.
- **Inventory-side bridge:** `NetworkInventoryAlarmController.java` (180 lines) — how alarms appear inside Device 360.
- **Public route inventory:** Tyk configmap `alarm-rest-config-cw-emf/platform/tyk/tykConfigmap.json` (386 lines). Execution session should read this first to see the actual external API contract.
- **EPNM twin in ems-assurance:** `fault-nbi/ems-fault-nbi/.../AlarmRestServiceImpl.java` (821 lines).
- **Syslog REST absent as a dedicated controller.** Likely surfaces via `AlarmRest.java` event filter. Needs Jenis to confirm. Reinforces that syslogs are the least-documented corner of POC scope.
- **Correlated-alarms tree JSON shape** not derivable from file names — probably delivered by `CWRestController.java`. Needs a real-source read.
- **Capabilities present only in EPNM ems-assurance, NOT ported to cw-epnm-fault:** `NetworkImpactingAlarm` and `NextStep`. If the classic alarms UI depends on either, they are a backend gap — falls into handoff doc 10 risk 6.11 territory.
- **Deployment shape differences between the two repos:**
  - `cw-epnm-fault` is Docker-first (Dockerfiles present, container-runnable).
  - `ems-assurance` is **ADS-only**: no Dockerfile for the main service, and contains a `resources_from_server_to_local.sh` helper plus start shell scripts that imply ADS provisioning. Reinforces open question 3.8 (local runnability): fault side is partially local-runnable (`cw-epnm-fault`) but not end-to-end (`ems-assurance` is ADS-dependent).
- **Real-time delivery primitives observed:** NATS, gRPC, Kafka, and JMS references in the tree. Exact delivery path to the UI (which of these the classic UI subscribes to) is open.

---

## Swarm Complete

All ten agents returned. Synthesis document:
`_scratch_repo/cross_repo_poc_map_2026-04-21.md`
