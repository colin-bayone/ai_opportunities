# Agent 09 — EMS Inventory Backend (cw-inventory + cw-inventory-collector)

Combined extraction of the two EMS-side Inventory backend repositories, read from
`/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/cw-inventory_tree_report.md`
and `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/cw-inventory-collector_tree_report.md`.

Scope of the POC for these repos: Inventory (Network Devices, Device Details, Chassis View, Device 360, Interface 360) and Fault Management. Classic UI consumes REST APIs from these services; no backend modification is permitted beyond narrow API-level touchup with Selva's approval.

## 1. Shape of both repos

### cw-inventory (the service)

- Repository root reported as `/Users/cmoore/Documents/programming/cw-inventory`.
- 469 text-like files, 106 directories, 135,386 raw lines.
- Top-level directories:
  - `.claude/` — single stub `epnm_to_ems_conversion_2026-04-21/goals/README.md` (the conversion engagement marker).
  - `agentic/` — handoff docs, repo-analysis scripts, a copy of `skill-forge`. Not shipped code; appears to be Colin/BayOne working material the Cisco repo has absorbed.
  - `conf/` — very large runtime configuration tree: `ddlmetadata/`, `ifm/` (with an 8,309-line `mdfdata.xml`), `keys/` (PEMs, encryption keys), `notificationmetadata/`, `prunemetadata/`, `rfm/`, `schemacreate_listeners/`, and ~50 loose `.properties`/`.xml` config files (`inventory.properties`, `kafka.properties`, `topology.properties`, `persistence_config.properties`, `credentialdictionary.txt`, etc.).
  - `conf_cs/` — small "cs" variant override directory (`ifm_inventory.properties`, `inventory.properties`, `jdbc.properties`).
  - `config/platform/tyk/tykConfigmap.json` — Tyk API gateway configmap (169 lines).
  - `files/` — SQL bootstrap (`createQuartzSchedulerTable.sql`, `createSystemPref.sql`) and shell helpers (`executeSQLScript.sh`, `getUserAndPass.sh`, `verifyDbCreation.sh`).
  - `keyfiles/` — 40+ `.key` files for `xmp_*` modules (licensing/feature keys; mostly 0-line markers).
  - `nulltemp/inventory/ExportDevice.csv` — export scratch.
  - `scan-config/` — sonar / scanner config.
  - `src/main/java/com/cisco/` and `src/main/resources/` — the actual service code (see Section 2).
  - `src/test/` — mirror tree with 80+ test classes, some very large (`CwInventoryRestServiceTest.java` 5,708 lines; `InventoryParameterCollectionJobTest.java` 5,411 lines).
- Top-level files: `Dockerfile` (97 lines), `Jenkinsfile` (386), `pom.xml` (7,449), `pom.xml.bak` (2,339), `cw_inventory_start.sh` (354), `cw_inventory_liveness.sh`, `liveness.sh`, `readiness.sh`, `showtech.sh`, `generate_heap_dump.sh`, `mvnw` + `mvnw.cmd`, `settings.xml`, `sonar_scan.sh`, `CLAUDE.md` (36).

### cw-inventory-collector (the collector)

- Repository root reported as `/Users/cmoore/Documents/programming/cw-inventory-collector`.
- 159 text-like files, 32 directories, 20,070 raw lines — roughly one-seventh the size of `cw-inventory`.
- Top-level directories:
  - `.settings/` — Eclipse/m2e project metadata (`org.eclipse.core.resources.prefs`, `org.eclipse.jdt.core.prefs`, `org.eclipse.m2e.core.prefs`). Evidence of Eclipse IDE usage.
  - `conf/` — mirrors `cw-inventory/conf/` shape but smaller: `ddlmetadata/`, `keys/`, `notificationmetadata/`, `prunemetadata/`, `schemacreate_listeners/`, plus loose properties including a `featureExclusion_DISH.properties` (customer-specific variant hint).
  - `conf_cs/` — small variant (`ifm_inventory.properties`, `inventory.properties`).
  - `files/` — `getUserAndPass.sh`, `verifyDbCreation.sh`.
  - `scan-config/` — sonar / scanner config (same pattern).
  - `src/main/java/`, `src/main/proto/`, `src/main/resources/`, `src/test/java/`.
- Top-level files: `Dockerfile` (63), `Jenkinsfile` (396), `pom.xml` (6,016), `cw_inventory_collector_start.sh` (313), `cw_inventory_collector_liveness.sh`, `readiness.sh`, `showtech.sh`, `settings.xml`, `sonar_scan.sh`, `.classpath`, `.project`.

## 2. Language split

Both repositories are **Java / Spring** — **not Go**. Ramkrishna's comment about Go services is not borne out here.

Evidence:

- Both have `pom.xml` (Maven), `mvnw`, `settings.xml`, `Jenkinsfile`, `.iml` / `.classpath` / `.project` (IntelliJ / Eclipse Java tooling). No `go.mod`, no `go.sum`, no `*.go` files.
- Both service trees live under `src/main/java/com/cisco/...` with `.java` extensions throughout.
- Spring evidence:
  - `cw-inventory/src/main/resources/` contains the full Spring bean XML stack (`xmp-persistence-context.xml`, `ifm_inventory_service_context.xml`, `distributed-cache-context.xml`, `ems-extension-app-beans.xml`, `cns-module-context.xml`, `ice-module-context.xml`, `presentation-root-context.xml`, `xmp-messaging-context.xml`, etc.), plus `bootstrap.properties` and `application.properties`.
  - `com/cisco/epnm/inventory/swagger/SwaggerConfig.java` (Springfox / OpenAPI).
  - Controller classes annotated by convention (HealthController, InventoryController, LoggerController) in both repos.
  - `ifm_inventory_service_context.xml` (326 lines) and `inventory-discovery-process-*-context.xml` bean wiring.
- Collector-specific:
  - `cw-inventory-collector/src/main/proto/inventory.proto` (23 lines) plus `grpcservice/DiagnosticCollectorGrpcService.java` (75 lines) = gRPC surface alongside Spring.
  - A vendored Hibernate class `org/hibernate/collection/internal/AbstractPersistentCollection.java` (1,356 lines) — local Hibernate override / patch.

**Conclusion.** Both repos are Spring Boot / Spring-XML Java services running on the JVM, Maven-built, Dockerized, orchestrated by Jenkins. No Go.

## 3. REST API surface — most important

Both services expose Spring MVC controllers; `cw-inventory` is by far the richer REST surface.

### cw-inventory controllers (classic UI primary targets)

- `src/main/java/com/cisco/epnm/inventory/controller/HealthController.java` (58 lines)
- `src/main/java/com/cisco/epnm/inventory/controller/InventoryController.java` (158 lines) — thin top-level inventory controller
- `src/main/java/com/cisco/epnm/inventory/controller/LoggerController.java` (66 lines)

### cw-inventory IFM Rest services — the heavyweight endpoints

- `src/main/java/com/cisco/ifm/inventoryrestservice/InventoryRestService.java` (**9,724 lines**) — the single largest REST surface in the repo.
- `src/main/java/com/cisco/ifm/inventoryrestservice/InventoryEMSRestService.java` (1,696 lines)
- `src/main/java/com/cisco/ifm/inventoryrestservice/InventoryEMSRestUtil.java` (833 lines)
- `src/main/java/com/cisco/ifm/inventoryrestservice/InventoryJobRestService.java` (903 lines)
- `src/main/java/com/cisco/ifm/inventoryrestservice/DiagnosticsRestService.java` (882 lines)
- `src/main/java/com/cisco/ifm/inventoryrestservice/SortCriteriaUtil.java` (80 lines)
- `src/main/java/com/cisco/ifm/jobscheduler/rest/JobSchedulerRestService.java` (**9,671 lines**) — job scheduler REST.
- `src/main/java/com/cisco/ifm/jobscheduler/rest/util/Utils.java` (100 lines)

### cw-inventory EMS / NetworkInventory REST services

- `src/main/java/com/cisco/ems/networkinventory/NetworkInventoryRestService.java` (323 lines)
- `src/main/java/com/cisco/ems/networkinventory/interfacedetails/EMSInterfaceRestService.java` (60 lines)

### cw-inventory NBI resource (RESTCONF / bulk import hint)

- `src/main/java/com/cisco/nms/nbi/epnm/restconf/xmp/im/ext/restconf/resource/root/BulkImportRootResource.java1` (303 lines)
  - Filename ends in `.java1` — this is almost certainly a **renamed/disabled** source file, not compiled. Hint: classic bulk-import via RESTCONF NBI is present-but-parked.

### cw-inventory OpenAPI / Swagger

- `src/main/java/com/cisco/epnm/inventory/swagger/SwaggerConfig.java` (34 lines) — Swagger/Springfox config only. No committed `openapi.yaml` / `swagger.json` descriptor anywhere in the tree. UI devs will need to pull the live Swagger JSON from the running service.

### cw-inventory-collector controllers

- `src/main/java/com/cisco/epnm/inventory/controller/HealthController.java` (21)
- `src/main/java/com/cisco/epnm/inventory/controller/InventoryController.java` (38)
- `src/main/java/com/cisco/epnm/inventory/controller/LoggerController.java` (65)
- `src/main/java/com/cisco/epnm/inventory/grpcservice/DiagnosticCollectorGrpcService.java` (75) + `src/main/proto/inventory.proto` (23) — gRPC (not REST).

Collector REST surface is tiny; it is mostly health/logger plus a gRPC diagnostic channel. The classic UI should not be hitting the collector directly.

### Supporting Spring bean wiring with likely URL mappings

- `src/main/resources/ifm_inventory_service_context.xml` (326)
- `src/main/resources/presentation-root-context.xml` (105)
- `src/main/resources/presentation_base.xml` (270)
- `src/main/resources/presentation_marshalling.xml` (105)
- `src/main/resources/nbi-beans.xml` (88)
- `src/main/resources/rateLimiter.xml` (94)
- `config/platform/tyk/tykConfigmap.json` (169) — Tyk gateway routes. Likely the canonical source of URL prefixes.

## 4. Domain model (DTOs and entity-like classes)

### cw-inventory DTOs

- `src/main/java/com/cisco/ems/inventory/dto/`
  - `DeviceFeatureDTO.java` (23)
  - `DeviceNodeUUIdSummaryDTO.java` (27)
  - `GIRequestDTO.java` (28)
  - `InventoryReportJobDTO.java` (218)
  - `NodeDetailsSummaryDTO.java` (65)
  - `UUIDPerCollStatusRequestDTO.java` (35)
  - `featureExclusionDTO.java` (30)
- `src/main/java/com/cisco/ems/inventory/satellite/dto/`
  - `SatelliteDTO.java` (103)
  - `SatelliteErrorResponse.java` (38)
  - `SatelliteListResponse.java` (83)
- `src/main/java/com/cisco/ems/networkinventory/dto/` — most UI-relevant
  - `CoherentDetailsDTO.java` (54)
  - `DeviceColumnFilter.java` (27) — Device Filter Panel
  - `DeviceColumnFiltersDTO.java` (16)
  - `DevicesFilterDTO.java` (30)
  - `InterfaceDetailQuery.java` (49)
  - `InterfaceDetailsDTO.java` (91) — Interface 360
  - `InterfaceDetailsGetApiRequest.java` (95)
  - `OpticalDetailsDTO.java` (224)
- `src/main/java/com/cisco/ems/DBquery/dto/`
  - `DbqueryDto.java` (29)
  - `QueryResultDTO.java` (83)
- `src/main/java/com/cisco/epnm/inventory/dataexport/dto/ScpConfigDto.java` (59)
- `src/main/java/com/cisco/epnm/inventory/dataexport/`
  - `DeviceGroupDto.java` (15), `DeviceGroupListDto.java` (19), `ExportJobRequestDto.java` (78)

No classic `Device.java` / `Chassis.java` / `Module.java` / `Credentials.java` / `Location.java` / `Site.java` / `DeviceState.java` JPA entities are surfaced at this extraction level. Those are likely inside `InventoryRestService.java` (9,724 lines) or pulled from an external `xmp_*` model module (see `keyfiles/xmp_im_physical_resource_module.key`, `xmp_im_logical_resource_module.key`, `xmp_im_foundation_module.key`, `xmp_im_res_mgr_module.key` — module tokens suggesting the physical/logical/foundation inventory model lives in a separate internal library).

### cw-inventory-collector DTOs

- None in the tree — the collector does not appear to define its own DTO package. Domain model is consumed from shared libraries (`ifm_*`, `xmp_*`).

## 5. Data access (repositories, DAOs, migrations, queries)

### cw-inventory

- `src/main/java/com/cisco/epnm/inventory/constants/SQLQueryConstants.java` (**435 lines**) — SQL query strings live here. Primary place to look for inventory-side reads.
- No `repository/` or `dao/` package is present at the top-level extraction. Persistence is wired via Spring bean XML:
  - `src/main/resources/xmp-persistence-context.xml` (333)
  - `src/main/resources/xmp-persistence-init-context.xml` (80)
  - `src/main/resources/xmp-persistence-context-dbconn.xml` (31)
  - `conf/epnm_persistence_config.properties` (21), `conf/persistence-init.properties` (15), `conf/persistence_config.properties` (23)
- Bootstrap SQL: `files/createQuartzSchedulerTable.sql` (167), `files/createSystemPref.sql` (3). No Flyway/Liquibase migration directory.
- DB shell helpers: `files/executeSQLScript.sh`, `files/getUserAndPass.sh`, `files/verifyDbCreation.sh`.
- JDBC config: `conf_cs/jdbc.properties` (22), `conf/connection-inv.properties` (15), `conf/queries.properties` (5).
- Compliance / DB-query service layer: `src/main/java/com/cisco/ems/DBquery/service/impl/DBQueryServiceImpl.java` (293) — ad-hoc DB query capability.
- DB-retry util: `src/main/java/com/cisco/ems/networkinventory/util/DBQueryRetryUtil.java` (84).

### cw-inventory-collector

- Same persistence-context XML pattern (`inventory-discovery-process-xmp-*-context.xml` in `src/main/resources/inventory_discovery_process/`).
- `conf/jdbc.properties` (21), `conf_cs/` variants.
- Vendored Hibernate patch: `src/main/java/org/hibernate/collection/internal/AbstractPersistentCollection.java` (1,356).
- No repository / DAO / migration files in the tree.

**Conclusion.** Postgres is the backing store (per `jdbc.properties` + Spring persistence config), but migrations are not in-repo — they are handled by the shared `xmp` persistence layer or by external DBA tooling. There is **no Flyway/Liquibase migration directory** for new-UI devs to read.

## 6. Business services (service-layer classes called from controllers)

### cw-inventory

- `src/main/java/com/cisco/ems/DBquery/service/DBQueryService.java` (16) + `impl/DBQueryServiceImpl.java` (293)
- `src/main/java/com/cisco/ems/inventory/satellite/service/SatelliteService.java` (247)
- `src/main/java/com/cisco/ems/networkinventory/service/NetworkInventoryService.java` (27) + `impl/NetworkInventoryServiceImpl.java` (**1,977 lines**) — core network-inventory business logic
- `src/main/java/com/cisco/ems/networkinventory/service/impl/IntfAdminStatus.java` (51), `IntfOperStatus.java` (49)
- `src/main/java/com/cisco/epnm/inventory/EPNMInventoryService.java` (493)
- `src/main/java/com/cisco/epnm/inventory/maintenance/MaintenanceService.java` (57)
- `src/main/java/com/cisco/epnm/inventory/grouping/GroupDeviceInventoryService.java` (236), `GroupingClientHelper.java` (108)
- `src/main/java/com/cisco/epnm/inventory/dataexport/DataExportInventoryHandler.java` (17) + `DataExportInventoryHandlerImpl.java` (**1,055 lines**), `SwimDataExportService.java` (608), `InventoryCSVExportJob.java` (**1,652 lines**), `ExportJobListener.java` (106), `ExportJobPublisher.java` (193)
- `src/main/java/com/cisco/epnm/inventory/dlm/CredentialProfileOnboarder.java` (176), `XtractDlmNodeAndCred.java` (352), `InventoryAlarmClient.java` (66), `InvetoryAlarmClient.java` (45) — note typo "Invetory"; likely a duplicate class
- `src/main/java/com/cisco/ifm/jobscheduler/service/JobSchedulerServiceImpl.java` (**6,579 lines**)
- `src/main/java/com/cisco/xmp/ice/job/InventoryParameterCollectionJob.java` (**1,011 lines**)
- `src/main/java/com/cisco/xmp/jobmanager/postInit/JobManagerPostInitHookImpl.java` (456)
- `src/main/java/com/cisco/xmp/jobnotification/impl/JobNotificationManager.java` (137)

### cw-inventory-collector

- `src/main/java/com/cisco/epnm/inventory/EPNMInventoryCollectorService.java` (561) — top-level collector service
- `src/main/java/com/cisco/epnm/inventory/InvCollectorConductor.java` (45)
- `src/main/java/com/cisco/epnm/inventory/maintenance/MaintenanceService.java` (50)
- `src/main/java/com/cisco/epnm/inventory/AppManagementHandlerImpl.java` (61), `ApplicationShowTechHandler.java` (69), `EPNMInventoryBeanConfigImpl.java` (30), `HealthUpdater.java` (75), `InventoryBackupRestoreHook.java` (48)
- `src/main/java/com/cisco/ifm/inventory/postprocessor/impl/IFMPostCollectionHook.java` (**1,190 lines**) — the biggest thing in the collector; post-collection processing pipeline
- `src/main/java/com/cisco/ifm/inventory/postprocessor/impl/FaultInventoryCollectionCallbackPlugin.java` (70) — collector-side fault linkage

## 7. Collector service specifics (what `cw-inventory-collector` does differently)

- Dedicated gRPC surface via `src/main/proto/inventory.proto` + `DiagnosticCollectorGrpcService.java`. UI should not talk to this; other services do.
- `IFMPostCollectionHook.java` (1,190) is the heart of the collector: post-collection processing after device poll completes.
- `FaultInventoryCollectionCallbackPlugin.java` (70) — inventory-collection ↔ fault system linkage (relevant to Fault Management POC scope: collector is where fault-inventory correlation is wired).
- No controller-defined REST business endpoints (only Health, Inventory placeholder, Logger).
- No DTO packages, no business-level REST output. Collector does not surface device data directly to UI — it writes collected data into the shared persistence layer which `cw-inventory` then exposes.
- Expected but not seen in the tree: SNMP/CLI driver classes and device parsers. These are imported from external libraries (the `xmp_*` / `ifm_*` keyfiles in `cw-inventory`'s `keyfiles/` reference `xmp_collector`, `xmp_decap_linux`, `xmp_decap_remote_client`, `xmp_dar_device_base_ios` — shared driver modules). Actual SNMP/CLI transport code is not in-repo.
- Bean wiring for collection is extensive: `src/main/resources/inventory_discovery_process/inventory-discovery-process-ice-module-context.xml` (299), `inventory-discovery-process-ems-extension-app-beans.xml` (304), `inventory-discovery-process-xmp-jobmanager-context.xml` (254) — ICE = Inventory Collection Engine.
- HA hook: `src/main/java/com/cisco/epnm/inventory/collector/geo/InventoryGeoHAHook.java` (141).
- Vendored Hibernate patch at `src/main/java/org/hibernate/collection/internal/AbstractPersistentCollection.java` (1,356).

## 8. Config and build

### cw-inventory

- `pom.xml` (7,449 lines) + `pom.xml.bak` (2,339) — Maven. `.bak` means an earlier pom kept on disk; worth spot-checking for parent/BOM changes.
- `mvnw` / `mvnw.cmd` present → Maven wrapper available for local builds.
- `settings.xml` (229) — Maven settings (internal Cisco Artifactory almost certainly).
- `Dockerfile` (97).
- `Jenkinsfile` (386).
- `cw_inventory_start.sh` (354) — entry point; shows JVM flags, profile activation, local-vs-cluster.
- `cw_inventory_liveness.sh` (9), `liveness.sh` (99), `readiness.sh` (5) — K8s probes.
- `showtech.sh` (12), `generate_heap_dump.sh` (5), `start_exporter.sh` (1), `cs_script.sh` (5), `sonar_scan.sh` (60).
- Spring profile configs: `src/main/java/com/cisco/epnm/inventory/profile/CWProfileConfig.java` (34), `LocalProfileConfig.java` (33) — explicit "local" profile → supports local-run, contradicting an "ADS only" assumption.
- `src/main/resources/application.properties` (39), `bootstrap.properties` (120), `banner.txt` (8).
- Gateway / rate limiter: `config/platform/tyk/tykConfigmap.json` (169), `src/main/resources/rateLimiter.xml` (94).
- Election / HA: `election.conf` (19), `InventoryLeaderElector.java` (196), `InventoryLeaderHook.java` (175), `InventoryGeoHAHook.java` (115).
- No `application.yml` — properties-based.
- `CLAUDE.md` (36) at repo root.

### cw-inventory-collector

- `pom.xml` (6,016) — Maven.
- `Dockerfile` (63).
- `Jenkinsfile` (396).
- `cw_inventory_collector_start.sh` (313).
- `cw_inventory_collector_liveness.sh` (9), `readiness.sh` (9), `showtech.sh` (12).
- `settings.xml` (229), `sonar_scan.sh` (65).
- `.classpath`, `.project`, `.settings/` — Eclipse project.
- `src/main/resources/application.properties` (27), `bootstrap.properties` (120).
- Local profile: `src/main/java/com/cisco/epnm/inventory/collector/profile/CWProfileConfig.java` (26).
- **No `pom.xml.bak`, no `CLAUDE.md` here.** The `agentic/` / `.claude/` conversion-engagement footprint exists only in `cw-inventory`.

**Deployment signal.** Both have Dockerfiles, Jenkins pipelines, K8s probes, start-scripts, and `LocalProfileConfig` classes. Local-run is feasible; ADS-only is not a hard constraint the code imposes. Tyk configmap + Jenkinsfile are the ADS production posture.

## 9. API gap hotspots — open questions from the handoff

Mapped against filenames (presence ≠ fit; absence ≠ missing).

- **Device count in Inventory filter panel.**
  - Likely candidates: `DeviceColumnFilter.java`, `DeviceColumnFiltersDTO.java`, `DevicesFilterDTO.java` in `com/cisco/ems/networkinventory/dto/`; logic in `NetworkInventoryServiceImpl.java` (1,977) and `InventoryRestService.java` (9,724).
  - No file named like `FilterCount` / `DeviceCountSummary`. Either the count is embedded in an existing filter response or missing — **investigation needed**.

- **Alarm summary on device endpoint.**
  - `InventoryAlarmClient.java` (66) and `InvetoryAlarmClient.java` (45) — note the typo duplicate; both live in `com/cisco/epnm/inventory/dlm/`. These suggest an inventory→alarm client exists. Whether a device-detail response embeds alarm summary is a question for `NetworkInventoryServiceImpl.java` and `InventoryEMSRestService.java`.
  - Collector side: `FaultInventoryCollectionCallbackPlugin.java` (70) wires fault/inventory correlation during collection.

- **Bulk-import CSV endpoint.**
  - `BulkImportRootResource.java1` — **filename ends with `.java1`**, so this class is not compiled. Strong signal the classic RESTCONF bulk-import is **disabled/parked** in this build.
  - Other CSV touch: `InventoryCSVExportJob.java` (1,652), `CSVWriterUtil.java` (410), `CSVConverter.java` (42). These are export-oriented, not import.
  - **Gap likely.** Bulk-import as a REST endpoint is probably not live; needs an API touchup with Selva's approval if UI requires it.

- **Export endpoint.**
  - Well-represented: `com/cisco/epnm/inventory/dataexport/` package (14 files), `DataExportInventoryHandlerImpl.java` (1,055), `InventoryCSVExportJob.java` (1,652), `SwimDataExportService.java` (608), `ExportJobPublisher.java` (193), `ExportJobListener.java` (106), `ExportJobRequestDto.java` (78), `ScpConfigDto.java` (59).
  - Also `nulltemp/inventory/ExportDevice.csv` and `ExportDevice.csv` at root (both 0 lines — runtime output targets).
  - Export pipeline is async / job-based (publisher + listener + SCP config). Classic UI must invoke via the export job API, not a synchronous GET.

- **OEM commands / OEM device support.**
  - No file surfaces with `OEM` in its name in either tree.
  - Closest: `credentialdictionary.txt` (123) and `xmp_dar_device_base_ios.key` (keyfile). OEM/third-party device command surface is not visibly present — **likely gap**.

- **State scheduling / DeviceState.**
  - `com/cisco/ifm/jobscheduler/` package: `JobSchedulerRestService.java` (9,671), `JobSchedulerServiceImpl.java` (6,579). Job scheduler is present and substantial.
  - `com/cisco/xmp/ice/job/InventoryParameterCollectionJob.java` (1,011) handles collection-job scheduling.
  - `conf/scheduler.properties` (12), `conf/ifm/jobmanager/job_settings.xml` (16).
  - Device-state scheduling as a distinct endpoint is not visibly named — state scheduling likely flows through the generic job scheduler REST (`/jobs`-style), not a purpose-built `DeviceState` endpoint. **Needs confirmation via Swagger.**

- **Device 360 / Interface 360 / Chassis View.**
  - Interface 360 has a direct home: `EMSInterfaceRestService.java` (60) + `InterfaceDetailsDTO.java` (91) + `InterfaceDetailsGetApiRequest.java` (95) + `InterfaceDetailQuery.java` (49) + `IntfAdminStatus.java`/`IntfOperStatus.java`.
  - Device 360 / Chassis View likely fed by `InventoryRestService.java` (9,724) + `NetworkInventoryServiceImpl.java` (1,977). No class named `Chassis*` or `Device360*` surfaces — aggregated views are assembled from the monolithic REST class.

## 10. Top paths to open first (execution session)

These map EMS backend endpoints to EPNM classic-UI inventory needs. All paths are inside `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/` once the repos are cloned in place; currently only the tree reports are present.

1. `cw-inventory/src/main/java/com/cisco/ifm/inventoryrestservice/InventoryRestService.java` — 9,724 lines, largest REST surface; almost every Device / Chassis / Module / Inventory endpoint.
2. `cw-inventory/src/main/java/com/cisco/ifm/inventoryrestservice/InventoryEMSRestService.java` — 1,696 lines, EMS-specific endpoints.
3. `cw-inventory/src/main/java/com/cisco/ems/networkinventory/NetworkInventoryRestService.java` + `service/impl/NetworkInventoryServiceImpl.java` — 323 + 1,977 lines; Network Devices / Device Details / filters.
4. `cw-inventory/src/main/java/com/cisco/ems/networkinventory/interfacedetails/EMSInterfaceRestService.java` + `dto/InterfaceDetailsDTO.java` + `dto/InterfaceDetailsGetApiRequest.java` — Interface 360.
5. `cw-inventory/src/main/java/com/cisco/epnm/inventory/controller/InventoryController.java` — 158 lines; top-level controller entry.
6. `cw-inventory/src/main/java/com/cisco/ifm/jobscheduler/rest/JobSchedulerRestService.java` — 9,671 lines; state scheduling, collection jobs.
7. `cw-inventory/src/main/java/com/cisco/epnm/inventory/dataexport/DataExportInventoryHandlerImpl.java` + `InventoryCSVExportJob.java` — export pipeline.
8. `cw-inventory/src/main/java/com/cisco/epnm/inventory/dlm/InventoryAlarmClient.java` (and the typo duplicate `InvetoryAlarmClient.java`) — fault-summary linkage for device endpoints.
9. `cw-inventory/src/main/java/com/cisco/epnm/inventory/swagger/SwaggerConfig.java` — pull the live Swagger/OpenAPI JSON from a running instance; there is no committed descriptor.
10. `cw-inventory/config/platform/tyk/tykConfigmap.json` + `cw-inventory/src/main/resources/ifm_inventory_service_context.xml` + `cw-inventory/src/main/resources/presentation-root-context.xml` — authoritative URL prefix / route wiring for the classic UI to target.

Collector secondary reads (fault-inventory correlation only):

- `cw-inventory-collector/src/main/java/com/cisco/ifm/inventory/postprocessor/impl/IFMPostCollectionHook.java` (1,190)
- `cw-inventory-collector/src/main/java/com/cisco/ifm/inventory/postprocessor/impl/FaultInventoryCollectionCallbackPlugin.java` (70)
- `cw-inventory-collector/src/main/proto/inventory.proto` — non-REST, for awareness only.
