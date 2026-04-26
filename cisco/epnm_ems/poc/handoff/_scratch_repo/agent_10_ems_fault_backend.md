# Agent 10 — EMS Fault Backend Tree Report Extraction

**Inputs.**
- `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/cw-epnm-fault_tree_report.md` (7,087 lines; report states 5,762 text files, 833 dirs, 3.45M raw lines across `ROBOT/cw-epnm-fault` — EMS-era fault backend)
- `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EMS-CNC/tree-reports/ems-assurance_tree_report.md` (7,946 lines; report states 5,318 text files, 1,255 dirs, 1.99M raw lines across `ROBOT/ems-assurance` — EPNM-era fault backend)

**Scope.** POC: classic-view **Inventory** and **Fault Management** (alarms, events, syslogs, correlated alarms, clear-alarm). Backend is off-limits except narrow API touchup with Selva approval. Ownership: **Jenis Dharmadurai ("Janice")** per Akhil walkthrough.

---

## 1. Shape of both repos

### `cw-epnm-fault` (EMS-era, modern multi-service Maven reactor, `develop` branch)

Top-level module directories (all under `cw-epnm-fault/`):
- `alarm-forwarding/` — forwarding sub-reactor: `alarm-forwarding-service/`, `alarm-forwarding-config-cw-emf/`, `alarm-forwarding-config-cw-epnm/`, `docker/`, `scan-config/`, `pom.xml`.
- `alarm-processing/` — CEP/correlation sub-reactor: `alarm-processing-service/`, `alarm-processing-config-cw-emf/`, `alarm-processing-config-cw-epnm/`, `docker/`, `scan-config/`, `pom.xml`.
- `alarm-reconciling/` — alarm/inventory sync sub-reactor: `alarm-reconciling-service/`, `config/`, `docker/`, `pom.xml`.
- `alarm-rest/` — **the REST fronting service** for alarms/events/syslogs: `alarm-rest-service/`, `alarm-rest-config-cw-emf/`, `alarm-rest-config-cw-epnm/`, `docker/`, `scan-config/`, `pom.xml`, `settings.xml`.
- `data-retention/` — partition/retention job: sub-reactor with `data-retention-config-cw-emf/`, service module, Flyway scripts, `docker/`.
- `event-processing/` — raw event ingestion / normalization sub-reactor: `event-processing-service/`, `event-processing-config-cw-emf/`, `event-processing-config-cw-epnm/`, `config/`, `docker/`.
- `fault-api/` — protobuf contract module only (`src/main/proto/telemetry.proto`, 484 lines).
- `fault-dependency-manager/` — upgrade hook + SQL upgrade scripts, `dependencies.json`.
- `fault-purging/` — `fault-purging-service/`, `config/`, `docker/`.

Twin-config idiom: every service has both `*-config-cw-emf/` (multi-vendor lite "EMF" profile) and `*-config-cw-epnm/` (full EPNM event-type catalog) resource trees packaged as sibling modules. Per-service `decap/conf/` carries the HPOV-derived Attribute/Event/Correlation processing XMLs plus `HP_*.txt` tabular seed data.

### `ems-assurance` (EPNM-era, large Eclipse/Tigerstripe polyrepo, `cepnm8.1PI` branch)

Top-level directories (selected — there are ~70):
- Models / Tigerstripe: `AlarmSubscription/`, `ItutEventType/`, `NbAlertToEPMAlert/`, `ImpactAnalysis/`, `NextStep/`, `NextStep-nbi/`.
- Core service + config: `epnm-fault-service/` (Spring Boot-ish; `EventServiceApplication.java` 233 lines, `InventoryServiceImpl.java` 16,749 lines, `EventDispatcher.java` 2,510 lines), `epnm-fault-service-config/` (the massive MIB + event-type resource bundle).
- Correlation: `epnm-fault-correlation-service/` (standalone Spring Boot app with `Application.java`, `AlertCorrelator.java`, `AlertPublisher.java`), `correlation_faults/`, `correlation_rules/`, `cep/` (reactor with `cep_config/`, `cep_rest_ui/`, `correlation_documentation/`, `nms_cep/`).
- Messaging / NBI: `fault-messaging-service/` (JMS publisher + MessagingService), `fault-nbi/` (`ems-fault-nbi/` with `AlarmRestServiceImpl.java`, `ems-fault-nbi-model/` Tigerstripe DTOs), `NextStep-nbi/`, `PerformanceRest/`, `ifm_alarm_rest_provider_epnm/` (export handlers), `alarm_api_service/`.
- Inventory / topology: `NetworkInventory/`, `NetworkInventoryDashletUI/`, `NetworkInventoryTableUI/`, `network_impact_analysis/`, `ems-fault-alarmsync/` (the EPNM-side twin of EMS `alarm-reconciling`).
- Technology plugins (trap/syslog translations + calculators): `cbr8-faults/`, `cfm_faults/`, `common_faults/`, `ds1ds3_faults/`, `flex_lsp_faults/`, `l3vpn_faults/`, `nvedge_faults/`, `ptp_faults/`, `satellite-faults/`, `epnm_carrier_ethernet_faults/`, `epnm_sonet_faults/`, `topology_ce_alarm_processing_hooks/`, `trap_es_faults/`, `generic_trap_filter/`, `com.cisco.xmp.deviceprofile.L3VPN-fault/`.
- OAM tooling: `fault-oam/` with `cfm/`, `flexlsp/`, `l2vpn-pw/`, `mpls_lsp/`, `pingtrace/`, `sr_te/`, `vrf/` — each has a `*_rest_impl/` and a Tigerstripe `*_service/`.
- UI fragments: `fault_ui/` (`TopologyAlarmsTabTable.js`, 1,307 lines; `AddTrapEventMappingFormBora.html`), `oam_fault_ui/`, `NetworkInventoryDashletUI/`, `NetworkInventoryTableUI/`.
- Persistence / util: `rfm_fault/` (persistence framework — `PersistenceService.java` 1,473 lines, `PersistenceUtil.java` 1,426 lines, `PostgresSchemaUtil.java` 1,316 lines, `CreateIndexesUtil.java` 1,125 lines, plus `MonitorResources*.properties` localization bundles up to 10,138 lines).
- Pollers / jobs: `epnm-assurance-poller/`, `interface-status-poller/`, `schedule_collection_job/`, `standalone-poller/`, `distributed-tasks-executor/`, `ncs42xx_alarm_sync/`, `optical_reports/`, `qos_reports/`, `otdr/`, `otdr-wrapper/`, `performance/`.
- Reports / misc: `ems-assurance-reports/`, `optical_reports_data_scripts/`, `oam_fault_actions/`, `protection_group/`, `device_console/`, `port/`, `mcn_preference_service/`, `utils/`, `Test_Framework/` (contains an enormous `InventoryServiceImpl.java` of 14,995 lines, matching the tree doc), `base-faults/`, `base-ems-assurance/`, `build/`, `build-models/`, `build-release-ems-assurance/`, `buildsonar/`, `models-parent/`, `snmp4j-1.11.5/`, `snmp4j-2.8.0/` (vendored SNMP stacks), `synce-technology-overlay/`, `rfm_fault/`, `scan-config/`, `schedule_collection_job/`, `sonet_faults_build/`, `ems_assurance_traps_files_fragment/`, `epnm_tp/`, `groovy-shell-server/`, `localization_calculator/`, `oam_fault_actions/`.
- Root files: `CODEOWNERS`, `Jenkinsfile` (177 lines), `PULL_REQUEST_TEMPLATE.md`, `sonar_scan.sh`.

Overall contrast: `cw-epnm-fault` is a clean microservice reactor (9 top-level service areas, Docker-first, Flyway SQL). `ems-assurance` is a WAR-era modular monolith with ~70 Eclipse projects, Tigerstripe-generated models, Hibernate + hbm.xml persistence, and DDL expressed as XML view definitions.

---

## 2. Relationship between the two

**Primary + auxiliary pair, with clear migration lineage.** Evidence from directory/path names:

- **Class duplication with EMS-era rewrite.** `cw-epnm-fault/alarm-reconciling/alarm-reconciling-service/.../inventory/alarmsync/` (e.g. `AbsoluteStateBasedAlarmServiceImpl.java` 1,405 lines, `AlarmInventorySyncServiceImpl.java` 2,264 lines, `InventorySyncHelper.java` 690 lines, handlers for `bgp/ isis/ ldp/ equipment/ mcn/ operationType/`) is a near-identical mirror of `ems-assurance/ems-fault-alarmsync/.../alarmsync/` (`AbsoluteStateBasedAlarmServiceImpl.java` 1,415 lines, `AlarmInventorySyncServiceImpl.java` 2,343 lines, same sub-package layout). The EMS version is the rewrite — same class names, higher line counts, additional `util/FaultManagedNECache.java`.
- **Correlator migration.** `ems-assurance/NbAlertToEPMAlert/src/main/java/com/cisco/nms/assurance/fault/nbi/NbAlertToEPMAlertCorrelator.java` (1,423 lines) reappears at `cw-epnm-fault/alarm-forwarding/alarm-forwarding-service/src/main/java/com/cisco/nms/assurance/fault/nbi/NbAlertToEPMAlertCorrelator.java` (1,731 lines) — EMS absorbed the EPNM north-bound correlator and extended it.
- **CEP engine migration.** `ems-assurance/cep/nms_cep/.../epnm/cep/esper/EsperCEPEngine.java` (277 lines) → `cw-epnm-fault/alarm-processing/alarm-processing-service/.../epnm/cep/esper/EsperCEPEngine.java` (328 lines). Same `esper/config/model/Correlation.java` JAXB class at 1,170 → 1,166 lines. Rule-handler package `epnm/cep/esper/rule/impl/` ships in both; EMS reactor drops some EPNM-only handlers (`HardwareAlarmHandler`, `SplitTreeRuleHandler`, `ServiceToAlarmRuleHandler`, `RandomRootCauseRuleHandler`, `SkipLevelRuleHandler`, `TimeDelayRuleHandler`, `MarkNonNetworkAlarmRuleHandler`) and keeps core EPNM-independent ones.
- **Configuration migration.** `cep_config/src/main/resources/conf/fault/cep/BGP.xml`, `ISIS.xml`, `L2VPN.xml`, `L3VPN.xml`, `MPLS_TE.xml`, `RSP.xml`, `SDH_CEP.xml`, `carrier_ethernet.xml`, `Cable_CEP.xml`, `DeviceRestart.xml`, `IM_Cardout.xml`, `SyncE.xml`, `SATop_CESoPSN.xml`, `SplitTree.xml`, `SIA.xml`, `NetworkAlarm.xml`, `esper.cfg.xml` are identical or nearly-identical under `cw-epnm-fault/alarm-processing/alarm-processing-config-cw-epnm/fault/conf/fault/cep/` (`*.xml`) and under the `cw-emf` profile of the same (`*.xml.deprecated` — EMS strips EPNM-only rules when running a non-EPNM-packaged device set).
- **Event/trap translation catalog.** The entire `eventTypes/`, `eventCategories/`, `trap/`, `syslog/`, `trapPlans/`, `correlationEngine/`, `syslogFormat/`, `localization/metadata/` tree appears verbatim in both repos: in `ems-assurance/epnm-fault-service-config/src/main/resources/opt/robot/{conf/fault,allmibs,mibs,trapPlans,...}` and in `cw-epnm-fault/event-processing/event-processing-config-cw-{emf,epnm}/src/main/resources/conf/fault/`.
- **Shared DTO + correlator copies.** `EPMAlarmModeEnum.java`, `EPMAlarmStatusEnum.java`, `EPMAlarmTypeEnum.java`, `InetAddressTypeEnum.java` appear in both under `com/cisco/nms/assurance/fault/nbi/common/`.
- **Not sibling services — primary + auxiliary.** `ems-assurance` is the EPNM-era primary that the EMS era (`cw-epnm-fault`) is being carved out of. Akhil's "EMS assurance is also back inside" = the EPNM codebase has been re-imported into the EMS repo structure as the reference/fallback. The classic UI talks to whichever is wired — Confluence branches `cepnm8.1PI` vs `develop` indicate EPNM-era classic-UI build vs EMS-era rewrite, with `cw-epnm-fault/develop` expected to be the POC target.

---

## 3. REST API surface (highest priority)

### `cw-epnm-fault/alarm-rest/alarm-rest-service/` — the main EMS alarms REST service

**Controllers (Spring `@RestController` by naming convention), all at `src/main/java/com/cisco/epnm/fault/alarmrest/`:**
- `AlarmRest.java` (**2,622 lines** — the primary entry point; classic-UI alarms/events endpoints)
- `AlarmSettingsController.java` (751 lines — alarm settings / preferences)
- `AlarmSettingsBean.java` (636 lines)
- `AlarmUpdateRestController.java` (308 lines — alarm acknowledge / clear / annotate)
- `CustomAlarmsController.java` (1,321 lines — custom trap/syslog/gNMI alarm CRUD)
- `CWRestController.java` (539 lines — CW-branded reads)
- `CWV2RestController.java` (434 lines — v2 reads)
- `CacheController.java` (156 lines)
- `UserPreferenceController.java` (247 lines)
- `View360AlarmController.java` (717 lines — device 360 view alarm panel)
- `AlarmRestApplication.java` (401 lines)
- Nested: `networkInventory/NetworkInventoryAlarmController.java` (180 lines)
- Nested: `controller/AlarmTestController.java` (655 lines), `controller/HealthController.java`, `controller/LoggerController.java`, `controller/TemplateController.java`
- `swagger/SwaggerConfig.java` (29 lines) — Swagger/OpenAPI is wired.

### Services behind the controllers
At `com/cisco/epnm/fault/alarmrest/services/`:
- `AlarmActionServiceImpl.java` (718 lines)
- `AlarmClassService.java` (650 lines)
- `CustomAlarmsServiceImpl.java` (2,023 lines)
- `DeviceSeverityService.java` (149 lines)
- `NextRestServiceImpl.java` (202 lines)
- `SeverityConfigRestService.java` (1,206 lines)

### Filter / criteria utilities
- `util/FilterCriteriaUtil.java` (797 lines)
- `util/CustomAlarmsDTOBuilder.java` (665 lines)
- `util/PaginationUtil.java` (92 lines)
- `nms/assurance/fault/cw/util/CriteriaUtil.java` (953 lines)
- `alarm-forwarding-service/.../subscription/filter/FilterParser.java` (623 lines)

### Spring contexts declaring the REST bean graph
- `alarm-rest-service/src/main/resources/ctx/cw-epnm/Alarm-context-restconf.xml` (142 lines)
- `alarm-rest-service/src/main/resources/ctx/cw-epnm/applicationContext.xml` (159 lines)
- `alarm-rest-service/src/main/resources/ctx/cw-epnm/ifm_proxy_alarm_rest_provider_epnm.xml` (37 lines)

### `ems-assurance` REST surfaces (EPNM-era)
- `fault-nbi/ems-fault-nbi/src/main/java/com/cisco/nms/ems/assurance/nbi/AlarmRestServiceImpl.java` (**821 lines**) + `AlarmRestService.java` (21 lines) — EPNM-era alarms NBI; accompanied by `fault-nbi/ems-fault-nbi-model/` Tigerstripe DTOs (`EmsAlarm.java` 531 lines, `FaultSessionFacade.java` 183 lines, `ServiceImpactingAlarmDTO.java` 322 lines).
- `fault-nbi/ems-fault-nbi/src/main/resources/nbi-sec/ems-assurance/ems-fault-nbi-sec.xml` (30 lines) — NBI security descriptor.
- `NextStep-nbi/src/main/java/.../NextRestServiceImpl.java` (204 lines).
- `alarm_api_service/.../AlarmAPIServiceImpl.java` (498 lines) plus DTOs (`DeviceDTO`, `LinkDTO`, `LinkEndpointDTO`, `DeviceLinkEndpointListDTO`, `InstanceIdClassNameDTO`).
- `ifm_alarm_rest_provider_epnm/.../AlarmRestProxy.java` (189 lines) + `export/` (`AlarmExport.java` 790 lines, `EventExport.java`, `SyslogExport.java`, `ExportBase.java`, `ExportBuilder.java`, `IExport.java`) + `handler/` (`CorrelationHandler.java` 242 lines, `ExportHandler.java` 571 lines, `SatelliteHandler.java`, `GenericHandler.java`). This is the EPNM alarm export pipeline (CSV/XML download).
- `PerformanceRest/nms-performance-rest-impl/.../PerformanceDataFacadeImpl.java` (90 lines) — performance REST (out of POC scope).
- OAM RestImpls: `fault-oam/*/oam_*_rest_impl/**/*RestImpl.java` — ping/trace/OAM action endpoints; `nbi-sec/ems-assurance/oam-*-nbi-sec.xml` for each. Out of POC scope but likely invoked from the Fault Management action menu.
- `device_console/device_console_rest/.../DeviceConsoleRestImpl.java` (49 lines) + `interactiveCliConsoleServiceImpl/.../InteractiveCLIConsoleServiceImpl.java` (408 lines).
- `services-fault-ia-view/` — `ddl/view_get_impacting_alarms_oracle.xml` (401 lines) + `nbi-sec/services-fault-ia/services-fault-ia-nbi-sec.xml` — impacting-alarms view/service.

**`nbi-sec/.../*-nbi-sec.xml` files are the canonical registry of what URLs exist** in the EPNM era; every NBI endpoint has one next to its impl. Inventory these first when mapping EPNM classic URLs.

---

## 4. Alarm model

### Primary EMS DTOs — `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/data/`
- `AlarmDTO.java` (126 lines), `CWAlarmDTO.java` (175 lines), `AlarmResponse.java` (65 lines), `AlarmFilterDTO.java` (188 lines), `AlarmRestRequestDTO.java`, `AlarmRestResponseDTO.java`, `AlarmSeverityByDevicesDTO.java`, `AlarmsByAlarmIdsDTO.java`, `AlarmsByDevicesDTO.java`, `AlarmActionParameter.java`
- `EventDTO.java` (118 lines), `CWEventDTO.java` (173 lines), `EventFilterDTO.java` (156 lines), `EventTypeFilterDTO.java`
- Custom event: `CustomEventConditionDTO`, `CustomEventDetailsDTO`, `CustomEventTypeDTO`, `CustomEventTypeFilterDTO`, `CustomGnmiDTO`, `CustomSyslogDTO`, `CustomSyslogRegexDetailsDTO`, `CustomSyslogTestDTO`, `CustomTrapDTO`, `CustomTrapTestDTO`, `CustomTrapAttributesDTO`, `CustomTrapAttributesTestDTO`
- `ErrorResponseDTO`, `RestRequestDTO`
- Subscription DTOs (`alarm-forwarding-service/.../subscription/model/`): `AlarmFilterDTO.java` (399 lines), `AlarmsRequestDTO`, `AlarmsNotificationsSubscriptionRequestDTO`, `AlarmsNotificationsSubscriptionResponseDTO`, `GetAlarmsResponseDTO`, `GetAlarmsSyncRequestDTO`, `GetAlarmsSyncResponseDTO`, `AlarmAdhocRequest`, `AlarmRequestCache`, `AlarmRequestStatus`, `AlarmSubscriptionOperation`, `AlarmSubscriptionWrapper`, `AlarmFilterConstants`, `NATSResponseType`

### Alarm cache tuple model — `cw-epnm-fault/alarm-rest/alarm-rest-service/.../ncs/eventAlarm/cache/`
- `alarm/AlarmCacheTuple.java` (217 lines), `alarm/SortedAlarmCache.java` (991 lines), `alarm/AlarmCountContainer.java` (205 lines), `alarm/AlarmSummaryCountCache.java` (482 lines), `alarm/AlarmAttributeNames.java`, `alarm/AlarmCacheDbInitializer.java` (115 lines), `alarm/AlarmSummaryCacheDbInitializer.java`
- `event/EventCacheTuple.java` (189 lines), `event/SortedEventCache.java` (889 lines), `event/EventAttributeNames.java`, `event/EventCacheDbInitializer.java`
- Base: `AlarmEventCacheBase.java` (189 lines), `AlarmEventCacheTupleBase.java`, `SortedCacheBase.java` (686 lines), `SortedCacheTupleBase.java`, `CacheTypeEnum.java`, `AlarmSystemSettings.java`, `ReloadCacheScheduler.java`
- Comparators: 14 `AlarmEventTuple*Comparer.java` under `comparers/`, 9 `AlarmTuple*Comparer.java` under `alarm/comparers/`, 4 `EventTuple*Comparer.java` under `event/comparers/`. Cover: Category, Condition, Description, DeviceTimestamp, FailureSource, InstanceId, InstanceUuid, RackId, Severity, Source, SrcObjectClassId, SrcObjectId, Timestamp, AlarmCreationTime, ChassisId, CorrelationType, Notes, Owner, ServiceAffecting, SrcObjectDisplayName, Status, UDFMap, Flagging.
- Filters: `CategoryFilter.java`, `ClearedFilter.java`, `CorrelatedFilter.java`, `FilterExpression.java` (139 lines), `NotificationDeliveryMechanismFilter.java`, `IFilterExpression.java`, `IAttributeValuePair.java`.

### Severity / type / enum
- `xmp/model/foundation/eventsAlarms/EventTypeEnum.java` (188–190 lines in each service module that includes it)
- `xmp/model/foundation/resourceManager/SnmpVersionEnum.java` (99 lines)
- `cep/esper/data/{Alarm.java (136 lines), Event.java (34 lines), Severity.java, EventType.java, Category.java}` — the CEP-internal POJOs

### EPNM Tigerstripe alarm model — `ems-assurance/`
- `AlarmSubscription/src/com/cisco/cw/common/alarmsubscription/AlarmSubscription.java` (139 lines)
- `fault-nbi/ems-fault-nbi-model/.../EmsAlarm.java` (531 lines) — the large EPNM alarm DTO
- `fault-messaging-service/.../message/objects/{Alarm.java (31 lines), AlarmUpdate.java (33 lines), Event.java (32 lines), FaultNotificationMessage.java (48 lines), Field.java (19 lines)}` — wire objects for JMS/notify
- `ItutEventType/src/com/cisco/nms/ituteventtype/ItutEventType.java` (61 lines) — ITU-T X.733 standard alarm type enum
- `ImpactAnalysis/services-fault-ia-view/src/com/cisco/nms/assurance/ia/views/{ImpactingAlarms.java (368 lines), ImpactingAlarmsHistory.java (368 lines), AlarmToServicesView.java (81 lines), ImpactedNetworkServices.java (256 lines)}` — view entities for the service-impact panel
- `common_faults/.../fault/cw/model/{CWAlarmDTO.java (163 lines), CWEventDTO.java (152 lines), CWAuditLogDTO.java (44 lines)}`
- `NbAlertToEPMAlert/src/main/java/.../common/{EPMAlarmModeEnum.java (73), EPMAlarmStatusEnum.java (83), EPMAlarmTypeEnum.java (83), EPMNotificationConstants.java (52), InetAddressTypeEnum.java (103)}`
- `NextStep/src/com/cisco/nms/countermeasures/{Countermeasure.java (175), NextstepDTO.java (131), PayloadDTO.java (82), ResponseDTO.java (50), CountermeasureSessionFacade.java (181)}` — "next step / recommended action" on an alarm.
- `oam_fault_ui/src/main/resources/data/OAM_EventList.json` — maps event types to OAM actions.

### Acknowledge / Clear / Annotate
- `cw-epnm-fault/alarm-rest/alarm-rest-service/.../nats/{CWAlarmAckHandler.java (76), CWAlarmClearHandler.java (94), CWAlarmNoteHandler.java (75), CWAlarmSubscriber.java (158)}` — NATS-bus counterparts.
- Controller routes for these actions live in `AlarmUpdateRestController.java` (308 lines) and `AlarmRest.java`.

---

## 5. Correlation engine

### Runtime — `cw-epnm-fault/alarm-processing/alarm-processing-service/.../epnm/cep/`
- Engine: `CEPService.java` (147), `CEPEngine.java` (39), `ConfigService.java` (127), `ConfigChangeListener.java` (24)
- Esper: `cep/esper/EsperCEPEngine.java` (328 lines), `cep/esper/config/CEPConfig.java` (197), `cep/esper/config/model/Correlation.java` (1,166 lines JAXB model), `cep/esper/config/model/ObjectFactory.java`
- Data facade: `cep/esper/data/{DefaultAlarmListener.java, DefaultEventListener.java, DataCollector.java, DataListener.java, Alarm.java, Event.java, Category.java, EventType.java, Severity.java}`
- Rule handlers: `cep/esper/rule/{CorrelationRuleHandler.java (34), impl/DefaultRuleHandler.java (120), impl/DefaultDBUpdateRuleHandler.java (142), impl/DefaultEventHandler.java (58), impl/EquipmentAlarmHandler.java (281), impl/ClearDyingGaspHandler.java (198), impl/ClearEntSensorHandler.java (200), impl/EventCountExceededDeviceHandler.java (64)}`
- Listeners: `cep/alarm/listener/{CEPAlarmListener.java (155), CorrelatedAlarm.java (60), CorrelationTree.java (32)}`, `cep/event/listener/CEPEventListener.java (138)`

### Rule definitions (per-technology XML)
- `cw-epnm-fault/alarm-processing/alarm-processing-config-cw-epnm/fault/conf/fault/cep/{BGP.xml (118), ISIS.xml (225), L2VPN.xml (313), L3VPN.xml (364), MPLS_TE.xml (399), RSP.xml (194), SDH_CEP.xml (311), SATop_CESoPSN.xml (164), carrier_ethernet.xml (157), Cable_CEP.xml (77), SyncE.xml (34), NetworkAlarm.xml (18), SIA.xml (18), SplitTree.xml (20), IM_Cardout.xml (536), DeviceRestart.xml (331), HardwareAlarmRules.xml (19), EquipmentAlarmRules.xml, EventRules.xml, EventThrottleRules.xml (24), AlarmInventorySyncHandler.xml (16), ClearDyingGasp.xml (16), ClearEntSensorHandler.xml (17), alarm_listener.xml, event_listener.xml, esper.cfg.xml (69)}`
- Correlation-engine catalog: `event-processing/event-processing-config-cw-*/.../conf/fault/correlationEngine/{AnyAlarmFlappingRules.xml (177), DuplicateEventRules.xml (178), FlexLSPEventRules.xml (58), GenericEventRules.xml (57), OspfEventRules.xml (58), RepeatedRestartRules.xml (131), TrapConstrainedIORules.xml (241)}`

### EPNM-era correlation (larger rule set)
- `ems-assurance/cep/nms_cep/.../epnm/cep/esper/rule/impl/` adds EPNM-specific handlers absent from EMS: `HardwareAlarmHandler.java` (581), `SplitTreeRuleHandler.java` (380), `ServiceToAlarmRuleHandler.java` (277), `SkipLevelRuleHandler.java` (238), `RandomRootCauseRuleHandler.java` (176), `TimeDelayRuleHandler.java` (195), `MarkNonNetworkAlarmRuleHandler.java` (81). Also `cep/esper/userdefined/impl/{HierarchyIdentificationHandler.java (215), HierarchyIdentificationUtil.java (163)}`.
- `ems-assurance/epnm-fault-correlation-service/` is a standalone Spring Boot correlator wrapping the rule engine: `AlertCorrelator.java` (147), `AlertPublisher.java` (113), `Application.java` (121), rules under `conf/rules/{AnyAlarmFlappingRules.xml, DuplicateEventRules.xml, RestartRules.xml}`.
- `correlation_faults/.../ncs/event/correlation/{LSPUpDownRuleAction.java (194), OSPFEventRuleAction.java (110)}` — custom rule actions.
- `correlation_rules/src/main/resources/conf/fault/correlationEngine/GenericEventRules.xml`.
- `ems-assurance/cep/cep_rest_ui/src/main/resources/webapp/applications/AlarmManagement/` — classic UI CorrelatedAlarms widget: `html/CorrelatedAlarmsDetails.html`, `html/CorrelatedAlarmsTree.html`, `js/AlarmCorrelatedView.js`, `js/CorrelatedAlarms.js` (**1,060 lines** — this is exactly the classic-UI "correlated alarms" tree view).
- Schema: `correlation.xsd` (87 lines) in both repos; Tigerstripe-generated `ems-assurance/epnm-fault-service/.../xsds/{decap-correlation-1.1.xsd (280), decap-correlation-1.2.xsd (631), decap-correlation-1.3.xsd (1191), decap-correlation-1.4.xsd (1201), decap-event-1.1.xsd (158), model-correlation-1.2.xsd (189)}`.
- `fault-oam/flexlsp/.../ifm_alarm_rest_provider_epnm/handler/CorrelationHandler.java` (242 lines).
- `network_impact_analysis/.../nia/{service/impl/NetworkImpactingAlarmServiceImpl.java (899), util/impl/NetworkImpactingAlarmManager.java (506), util/impl/NetworkImpactingAlarmHelperImpl.java (162), model/{AlarmNetworkLayerInfo.java, NetworkImpactingAlarmData.java}}`.
- `ImpactAnalysis/service_impact_analysis_plugin/.../sia/{transaction/impl/SiaTrxProcessorImpl.java (1,486), plugin/SIADBEventNotificationPlugin.java (673), alarm/AlarmManager.java (535), filters/FilterHandler.java (236), transaction/impl/{SiaDbReloadImpl.java (399), PluginTransactionScannerImpl.java (362), SiaOddEvenProcessImpl.java (175), DMMFaultSiaTransactionConsumer.java (124), DMMFaultSiaTransactionProcessThread.java (69), NotificationProcessThread.java (125)}}`.

---

## 6. Real-time update mechanism

The UI gets new alarms via a **multi-transport fan-out**: NATS + gRPC + JMS + Hazelcast, plus a Kafka/"external Kafka" fan-out for alarm forwarding. No WebSocket or SSE in the naming evidence.

### NATS (primary intra-service bus on EMS side)
- `cw-epnm-fault/alarm-rest/alarm-rest-service/.../nats/{CWAlarmAckHandler.java, CWAlarmClearHandler.java, CWAlarmNoteHandler.java, CWAlarmSubscriber.java}` — NATS-side alarm command handlers.
- `.../natsv2/{AlarmReadHandlerV2.java, EventReadHandlerV2.java, service/AlarmNatsReadV2Handler.java (190), service/EventNatsReadV2Handler.java (173)}`
- `.../natsv3/{AlarmReadHandlerV3.java, EventReadHandlerV3.java}`
- `alarm-forwarding-service/.../natsv3/{CWAddRestDestinationHandler, CWAddSyslogDestinationHandler, CWAddTrapDestinationHandler, CWDeleteRestDestinationHandler, CWDeleteSyslogDestinationHandler, CWDeleteTrapDestinationHandler, CWGetSyslogDestinationHandler, CWGetTrapDestinationHandler, CWAlarmForwardingSubscriber, AuditLogReadHandler, service/NatsReadV3Handler}`
- `alarm-forwarding-service/.../cw/events/messaging/{AlarmsSubscriptionRobotHandler (141), BulkAlarmNatsMessaging (27), BulkAlarmRobotHandler (116), FeaturesListener (443)}`
- `alarm-forwarding-service/.../subscription/messaging/{FaultNatsAlarmMessaging, FaultNatsBulkAlarmMessaging, FaultNatsSubscriptionMessaging, FaultAlarmRobotHandler, FaultBulkAlarmRobotHandler, FaultSubscriptionRobotHandler, FaultSyncAlarmRobotHandler}`
- `event-processing-service/.../cw/CWNatsSubscriber.java (106)` + `ManifestEventMessaging.java`, `CWSystemEventMessaging.java`, `NatsUtils.java`.
- `alarm-rest-service/.../messaging/AlarmUpdatePublisher.java (259)` — pushes real-time alarm updates.

### gRPC
- `alarm-forwarding-service/.../grpc/{AlarmsGrpcServiceImpl.java (121), FaultGrpcServiceImpl.java (69), GrpcServerInitializer.java (192)}`
- `alarm-processing-service/.../almprocess/grpc/OrchGrpcClientUtil.java (244)`
- `alarm-rest-service/.../grpc/{AlarmsGrpcServiceImpl.java (75), GRPCClientUtil.java (237), GrpcServerInitializer.java (185), OrchGrpcClientUtil.java (209)}`
- `event-processing-service/.../grpc/{AlarmsGrpcServiceImpl.java (155), GrpcClientUtil.java (237), GrpcServerInitializer.java (185), GrpcTestController.java (332), OrchGrpcClientUtil.java (274)}`
- Proto: `cw-epnm-fault/fault-api/src/main/proto/telemetry.proto` (484 lines) — the gRPC contract module.

### Kafka (alarm forwarding / external subscription fan-out)
- `alarm-forwarding-service/.../device/highest/severity/service/{DeviceHighestSeverityKafkaListener.java (81), DeviceHighestSeverityListener.java (192)}`
- `alarm-forwarding-service/.../listener/{ExternalKafkaDestinationDeleteSystemAlarmListener.java (248), ExternalKafkaSubscriptionInfoListener.java (104), PolicyAlarmEventListener.java (481)}`
- `alarm-forwarding-service/.../subscription/service/{ExternalKafkaDestinationDeletedSubscriptionCleanupService.java (248), ExternalKafkaOrphanSubscriptionService.java (155)}`

### JMS (EPNM-era, in `ems-assurance`)
- `fault-messaging-service/.../message/jms/FaultJMSPublisher.java (85)`
- `fault-messaging-service/.../message/notify/{listener/{FaultNotificationListener.java (93), NBIFaultListener.java (72), PolicyFaultAlertListener.java (86)}, NotificationService.java (92)}`
- `fault-messaging-service/.../messaging/{IMessagingService.java (255), MessagingService.java (1,031), MessagingPropertyPlaceholderConfigurer.java (95), GroupMembershipListener.java (16)}`
- `epnm-fault-service/.../server/events/EventDispatcher.java (2,510)` — the central EPNM event pump.

### Hazelcast (distributed in-memory cache, serving UI reads)
- `alarm-forwarding-service/.../cw/events/service/HazelcastMapInspectController.java (250)`
- `alarm-rest-service/resources/ctx/cw-epnm/modified_cache_context.xml` (162 lines)
- `SortedAlarmCache.java` / `SortedEventCache.java` are cache-backed.

### No WebSocket/SSE
Grep on file names shows no `.ws.`, `WebSocket`, `Sse`, `EventSource` hits. The classic UI must be polling `CWRestController` / `AlarmRest` — likely via `View360AlarmController` for widget refresh.

---

## 7. MIB / .my files

### `cw-epnm-fault/event-processing/event-processing-config-cw-{emf,epnm}/src/main/resources/mibs/`
Hundreds of `.my`, `.mib`, and extension-less MIB text files. Representative coverage (from file names):
- Standards: `ACCOUNTING-CONTROL-MIB`, `ADSL-*`, `ADSL2-*`, `AGENTX-MIB`, `ALARM-MIB`, `APM-MIB`, `APPC-MIB`, `APPLETALK-MIB`, `APPLICATION-MIB`, `APPN-*`, `APS-MIB`, `ATM-*`, `BGP4-MIB`, `BRIDGE-MIB`, `CHARACTER-MIB`, `CIRCUIT-IF-MIB`.
- Cisco Access/WLAN: `AIRESPACE-REF-MIB.my`, `AIRESPACE-SWITCHING-LATEST-MIB.my` (3,782 lines), `AIRESPACE-SWITCHING-MIB.my` (3,546), `AIRESPACE-WIRELESS-MIB.my` (14,845), `AWC-VLAN-CFG-MIB.my` (158), `AWCVX-MIB.my` (6,295).
- Aruba: `ARUBA-MIB.mib`, `ARUBA-TC.mib`, `ARUBA-TC.my`.
- CISCO MIBs (partial list from first page of MIB dir — hundreds more follow): `CISCO-ACCESS-ENVMON`, `CISCO-AUTH-FRAMEWORK`, `CISCO-BGP4`, `CISCO-CABLE-*` (5 MIBs), `CISCO-CCME`, `CISCO-CDP`, `CISCO-CONFIG-COPY`, `CISCO-CONFIG-MAN`, `CISCO-CONTENT-ENGINE`, `CISCO-DEVICE-EXCEPTION-REPORTING`, `CISCO-DOCS-EXT` (4,780), `CISCO-DOT11-*` (5 MIBs), `CISCO-DOT3-OAM-MIB.mib`, `CISCO-ENHANCED-MEMPOOL`, `CISCO-ENTITY-ALARM`, `CISCO-ENTITY-ASSET`, `CISCO-ENTITY-FRU-CONTROL`, `CISCO-ENTITY-SENSOR`, `CISCO-ENTITY-VENDORTYPE-OID` (4,840), `CISCO-ENVMON`, `CISCO-EPM-NOTIFICATION`, `CISCO-ETHER-CFM`, `CISCO-EVC` (4,285), `CISCO-FLASH` (3,469), `CISCO-GNSS`, `CISCO-IETF-BFD`, `CISCO-IETF-ISIS` (3,816), `CISCO-IETF-PW`, `CISCO-IMAGE`, `CISCO-ISDN`, `CISCO-LATEST-LWAPP-MOBILITY`, `CISCO-LICENSE-MGMT` (2,611), `CISCO-LOCAL-AUTH-USER`, `CISCO-LWAPP-*` (dozens — AAA, ACL, CCX-RM, CDP, CLIENT-ROAMING, CLOUD-SERVICES, DHCP, DOT11-*, DOWNLOAD, HA, IDS, INTERFACE, IPS, IPV6, LBS, LINKTEST, LOCAL-AUTH, MDNS, MESH-*, MFP, MOBILITY-*, NBAR, NETFLOW, ...).
- Structure. The MIB directory is flat under `event-processing-config-cw-*/...mibs/`. Additional `custom_mibs/` subfolders exist (e.g. `cbr8-faults/.../custom_mibs/{CLAB-DEF-MIB, CLAB-TOPO-MIB, DOCS-IF3-MIB, DOCS-RPHY-CTRL-MIB (699), DOCS-RPHY-MIB (7019), DOCS-RPHY-PTP-MIB, IANA-ENTITY-MIB, UUID-TC-MIB}`) — DOCSIS/cable family for CBR-8 CMTS.

### `ems-assurance/epnm-fault-service-config/src/main/resources/opt/robot/allmibs/`
Same catalog (verbatim overlap). Size on disk ~576K lines of MIBs per Confluence. Laid out beneath `opt/robot/allmibs/` which is the runtime deployment path (ADS) — the EPNM-era service expected MIBs pre-deployed at `/opt/robot/allmibs/`.

### `ems-assurance/{technology}_faults/src/main/resources/decap/conf/mibs/` (per-technology)
- `cbr8-faults/` — cable/DOCSIS.
- `cfm_faults/` — `CISCO-IETF-PW-MIB.my`, `CISCO-IETF-PW-TC-MIB.my` (CFM / pseudowire).
- `common_faults/` — `CISCO-ENTITY-ALARM`, `CISCO-ENTITY-SENSOR`, `CISCO-NTP`, `CISCO-PRODUCTS` (1,999), `CISCO-SYSTEM-EXT`, `CISCO-SYSTEM-MIB`.
- `nvedge_faults/` — `CISCO-RF-MIB.my` (1,554) — nV edge chassis.
- Similar per-tech MIB bundles under `satellite-faults/`, `ds1ds3_faults/`, `flex_lsp_faults/`, `l3vpn_faults/`, `ptp_faults/`, `generic_trap_filter/`.

### Device-family coverage summary (from file names)
ASR 9K, NCS (4K, 5xx, 540), CBR-8, ME1200, ASR901/903, ONS TL1, NxOS (Nexus), nV edge, Cisco WLC (Airespace), Aruba, optical / SONET / SDH, satellite, DOCSIS (CMTS), carrier ethernet (CFM/EVC/LAG), MPLS-TE, L2VPN, L3VPN (BGP/LDP/RIP/OSPF/ISIS), FlexLSP, PTP/SyncE, DS1/DS3, DSX, entSensor, storm-control.

### MIB processing metadata (parallel tree with MIBs)
- `parsingProperties/*.xml` per MIB (e.g. `CISCO-ETHER-CFM-MIB_ParsingProperties.xml`, `CISCO-RF-MIB_ParsingProperties.xml`, `CISCO-IETF-PW-MIB_ParsingProperties.xml`) — MIB attribute → alarm mapping.
- `trapPlans/*.xml` per MIB (~40 files at `epnm-fault-service/src/main/resources/trapPlans/`) — trap-to-event plans.

---

## 8. Data access

### PostgreSQL migrations (Flyway) — `cw-epnm-fault/data-retention/data-retention-config-cw-*/...`
Versioned SQL scripts (filenames encode version order `V7_0_0_1__...` style):
- `V7_0_0__baseline.sql` (1,497 lines at `-cw-epnm`, 925 lines at `-cw-emf`)
- `V7_0_0_1__create_hypertable.sql` (105 / 74)
- `V7_0_0_2__fixstuckjobs_fault.sql` (34 / 34)
- `V7_0_0_3__nbi_views.sql` (3 / 3)
- `V7_1_0_1__retention.sql` (84 / 39)
- `V7_1_0_2__fixstuckjobs_fault.sql` (49 / 49)
- `V7_1_0_3__alarm_index.sql` (1 / 1)
- `V7_1_0_4__fault_customalarm.sql` (5 / —)
- `V7_2_0_1__retention.sql` (48 / 48)
- `V7_2_0_2__snmpv3.sql` (— / 5)
- `V8_0_0_1__alarmsubscription.sql` (2)
- `V8_0_0__baseline.sql` (246)
- Migration helper SQLs: `alarms_migration.sql` (5), `alms_migration.sql` (80), `sysalarm_migration.sql` (273).
Hypertable naming indicates **TimescaleDB** on top of PostgreSQL for time-series alarms/events.

### DAO / repository layer
- `cw-epnm-fault/alarm-forwarding-service/.../subscription/service/AlarmSubscriptionDbQueryService.java` (124)
- `cw-epnm-fault/alarm-forwarding-service/.../service/PersistenceService.java` (EPNM-legacy — 1,439 lines at `com/cisco/server/services/`)
- `cw-epnm-fault/alarm-rest-service/src/main/resources/mapping/hibernate/com/cisco/epnm/fault/alarmrest/entity/{EventCondition.hbm.xml, EventType.hbm.xml, SyslogManifest.hbm.xml, TrapAttributes.hbm.xml, TrapManifest.hbm.xml, TrapVarbindValue.hbm.xml}` — Hibernate entity mappings for custom event/syslog/trap persistence.
- Event-type persistence: `event-processing-service/.../cw/events/EventsManifestCacheFromDB.java` (347), `EventsManifestCacheV3FromDB.java` (353), `EventsManifestPersistence.java` (225), `ReconcileManifestCache.java` (72).
- Custom-event persistence: `event-processing-service/.../customevent/{CustomEventCacheInitalizer.java (640), CustomEventCacheListener.java (308), CustomEventUtil.java (375), CustomSyslogEventProcessor.java (382), CustomTrapProcessor.java (468), RegexParserUtil.java (61)}`.
- Raw SQL: `event-processing-service/.../common/util/DirectSQLQuery.java` (906).

### `ems-assurance` persistence (EPNM era — Hibernate-centric, no Flyway)
- `rfm_fault/src/main/java/com/cisco/server/persistence/{hibernate/{query/CriteriaBuilder.java (223), query/CriteriaExpressionHelper.java (349), query/CriteriaPropertyResultSetter.java (110), query/CriteriaResultTypeHelper.java (156), query/ReGexLikeExpression.java, query/MaskMatchesExpression.java (75), query/EnhancedLikeExpression.java}, query/{SQLBuilder.java (387), SQLExpressionHelper.java (269), SQLResultTypeHelper.java (121), ...}, transaction/{LockDebugInterceptor.java, SQLStatement.java (196), StatementCache.java}, util/{PersistenceUtil.java (1,426), PostgresSchemaUtil.java (1,316), CreateIndexesUtil.java (1,125), SchemaUtil.java (717), SetColumnsUtil.java (538), DatabaseCredentials.java (271), DeduplicationUtil.java (389), IdentityMigrationUtil.java, VendorSchemaUtil.java (128), VendorMigrationUtil.java, BlobType.java, DMMErrorCode.java, DMMException.java (281), TableChunkInfo.java, TransactionQueryCache.java (214)}}`
- `server/services/PersistenceService.java` (1,473 lines) — the EPNM persistence facade.
- `server/persistence/hibernate/conf/dtd/hibernate-mapping-3.0.dtd` (1,036 lines) — Hibernate 3 DTD bundled.
- Oracle + Postgres side-by-side: `PerformanceRest/nms-performance-rest-model/ddl/cepm_views_oracle.xml` (151), `ImpactAnalysis/services-fault-ia-view/ddl/view_get_impacting_alarms_oracle.xml` (401) — SQL views defined as XML for both DBs.
- `ImpactAnalysis/fault_sia_model/.../fa/sia/{DMM_FAULT_SIA_TRANSACTIONS.java (180), DMM_FAULT_SIA_TXNSCANNER.java (142), SIADBReloadFacade.java (122), SIAREFEMS.java (145), SIA_RFS_EMSIDS.java (128)}` — SIA (service impact) persistence entities (likely Tigerstripe-generated POJOs).

Database name for fault (from `DBNames.java` references in multiple services): expect single name emitted across services.

---

## 9. Config and build

### `cw-epnm-fault`
- **Maven reactor**: root `pom.xml` (not seen directly, but each top-level module has one: `alarm-forwarding/pom.xml` (424), `alarm-processing/pom.xml` (253), `alarm-reconciling/pom.xml` (279), `alarm-rest/pom.xml` (306), `fault-api/pom.xml` (183), `fault-dependency-manager/pom.xml` (192), `fault-purging/pom.xml` (311)). Service pom.xmls are big (`alarm-rest-service/pom.xml` 2,422 lines; `alarm-processing-service/pom.xml` 2,002; `fault-purging-service/pom.xml` 2,180; `alarm-forwarding-service/pom.xml` 1,694).
- **Spring Boot / profile-driven config**: each service has `application-cw-emf.properties` (~107–134 lines) and `application-cw-epnm.properties` (~64–77 lines) in `src/main/resources/`. Profile switch selects EMF vs EPNM event-type catalog.
- **Logging**: `log4j2.xml` (~256–401 lines per service), `log4j2-offline.xml` for dev.
- **Spring contexts**: per-service `ctx/cw-emf/` and `ctx/cw-epnm/` trees with `applicationContext.xml`, `base-xmp-context.xml`, `alarm-notification.xml`, `modified-eventTypes.xml` (5,863–5,926 lines), `modified-eventAlarmCategories.xml`, `modified-rfm-application-context.xml`, `modified-xmp-jobmanager-context.xml`, `modified-cep-context.xml`, `modified-sia.xml`.
- **Docker**: every service has a `docker/` with `Dockerfile` (45–119 lines), `start.sh` (21–279 lines), `startup.sh`, `readiness.sh`, `showtech.sh`, `getUserAndPass.sh`, `verifyDbCreation.sh`, `start_exporter.sh`, `election.conf` (alarm-processing only — leader election).
- **Tyk (API gateway)**: `config/platform/tyk/tykConfigmap.json` per service — gateway route registration, sizes 8–386 lines (alarm-rest is the largest at 386 — contains the public REST route table).
- **Jenkinsfile** at repo root (259 lines), `CODEOWNERS` (1 line), `README.md` (27 lines), `PULL_REQUEST_TEMPLATE.md` (36 lines).
- **Scan-config**: per-service `scan-config/*.properties` — security / sensitive-data scanner config (tracks hard-coded secrets).

### `ems-assurance`
- **Maven + Tigerstripe**: root `pom.xml` (not shown), `buildsonar/pom.xml` (435), `build/pom.xml` (211), `build-models/pom.xml` (55), `build-release-ems-assurance/pom.xml` (307), `base-ems-assurance/pom.xml` (324), `base-faults/pom.xml` (455). Many modules carry `tigerstripe.target` and `tigerstripe.xml` — model-driven code gen.
- **Per-module poms** are extensive: `epnm-fault-service/pom.xml` (2,273), `schedule_collection_job/pom.xml` (1,173), `ems-fault-alarmsync/pom.xml` (1,052), `common_faults/pom.xml` (706), `correlation_faults/pom.xml` (387), `epnm-fault-correlation-service/pom.xml` (452), `cep/nms_cep/pom.xml` (453), etc.
- **Spring XML contexts**: per-module `src/main/resources/META-INF/spring/*.xml`. Not Spring Boot — looks like Spring 3.x/4.x OSGi-ish deployment with `beanRefContext*.xml`.
- **Properties**: `application.properties` (small — 2–17 lines, indicating main config externalized). `epnm-fault-service/src/main/resources/application.properties` (17), `epnm-fault-correlation-service/.../application.properties` (13). `epnm-assurance-poller/src/main/resources/application.yml` (30 lines — only `.yml` seen repo-wide).
- **Logging**: per-module `*_log4j.xml` (older log4j 1.x).
- **Maven wrapper**: `epnm-fault-service/mvnw`, `epnm-fault-correlation-service/mvnw` (310 each), `epnm-assurance-poller/mvnw` (233), `.mvn/wrapper/maven-wrapper.properties`.
- **Docker**: only `epnm-assurance-poller/Dockerfile` (5 lines — trivial) — **no Dockerfiles for the main fault service**. Consistent with ADS-only deployment for the EPNM era.
- **Startup scripts**: `epnm-fault-service/start-epnm-fault-service.sh` (253), `epnm-fault-correlation-service/start-epnm-fault-correlation-service.sh` (193), `epnm-fault-service/resources_from_server_to_local.sh` (106) — explicit "copy resources from server" helper suggests devs pull prod files to local (ADS-only). `Test_Framework/src/main/resources/run_test_fault.sh` (357).
- **NBI security** is declared in XML: `*nbi-sec/*.xml` files define URL → role mappings per REST impl module.
- **CEP/Esper config**: `cep/cep_config/.../conf/fault/cep/*.xml`, `cep/nms_cep/src/main/resources/META-INF/spring/cep-context.xml` (64).
- **Jenkinsfile** (177), `PULL_REQUEST_TEMPLATE.md` (36), `sonar_scan.sh` (60), `CODEOWNERS` (4).
- **Vendored SNMP**: `snmp4j-1.11.5/` (legacy) and `snmp4j-2.8.0/` side by side.

**Local-run vs ADS-only.** `cw-epnm-fault` is Docker-first and clearly runnable as containers locally. `ems-assurance` has no Dockerfiles for the main service, uses `start-epnm-fault-service.sh` + a `resources_from_server_to_local.sh` pull script — consistent with ADS-only deployment as noted in walkthrough.

---

## 10. API gap hotspots (open questions for handoff)

Evidence by file name of what is and is not present.

### Advanced-filter structure
**Present** (EMS side):
- `alarm-rest-service/.../util/FilterCriteriaUtil.java` (797 lines) — server-side filter parser.
- `nms/assurance/fault/cw/util/CriteriaUtil.java` (953) — EMS criteria utilities.
- `alarm-forwarding-service/.../subscription/filter/{FilterParser.java (623), ParameterizedQuery.java (40)}` — subscription filter expression parser.
- `AlarmFilterDTO.java` exists in two versions (`alarmrest/data/AlarmFilterDTO.java` 188 lines, `subscription/model/AlarmFilterDTO.java` 399 lines) — different filter grammars for REST vs subscription.
- `ncs/eventAlarm/cache/alarm/filters/FilterExpression.java` (139) — cache-layer filter AST.
**Open question.** Two different filter shapes ship. Classic UI's advanced-filter builder must map to one of them — likely the REST `AlarmFilterDTO`; but subscription-side 399-line variant has more operators. Worth confirming with Jenis which DTO the UI POSTs.

### Expandable-row detail source
**Present.**
- `alarm-rest-service/.../View360AlarmController.java` (717) — the device-360 alarm detail controller; likely what the expandable row fetches.
- `alarm-rest-service/.../AlarmRest.java` (2,622) contains per-alarm detail routes.
- `event-processing-service/.../cw/events/model/{DocInfo.java, EventCaseInfo.java, EventInfo.java, EventsManifest.java}` + `cw/events/EventsManifestCacheFromDB.java` — event documentation/case-info back-end (matches the expanded-row "Doc" / "Case" tabs in classic UI).
- `event-processing-service/.../cw/showtech/model/{CaseInfo.java (58), Documentation.java (44), Events.java, Manifest.java, Tca.java}` — same shape surfaced via show-tech.
**Open question.** Which REST URL aggregates `EventCaseInfo + EventDocInfo + EventTcaInfo + Manifest` for a single alarm? Likely served by `AlarmRest.java` or `View360AlarmController` — needs confirmation.

### Clear-alarm API
**Present.**
- `alarm-rest-service/.../AlarmUpdateRestController.java` (308) — REST path.
- `alarm-rest-service/.../services/AlarmActionServiceImpl.java` (718) — action implementation.
- `alarm-rest-service/.../nats/CWAlarmClearHandler.java` (94) — NATS handler.
- `alarm-rest-service/.../messaging/AlarmUpdatePublisher.java` (259) — publishes clear-event downstream.
- `alarm-processing-service/.../alarmupdate/{AlarmUpdateHelper.java (377), AlarmUpdateNotifier.java (99), AlarmUpdateProcessorImpl.java (1,042), AlarmUpdateNotificationType.java, AlarmUpdateNotificationWrapper.java}`.
**Gap check.** No doubt clear-alarm exists; the question is whether a single POST clears multi-selected alarms in one call or requires per-alarm calls. `AlarmUpdateProcessorImpl` at 1,042 lines likely supports bulk — confirm via the controller route.

### Events time-window filters
**Present (likely via FilterCriteriaUtil):**
- No dedicated "events-by-time-window" controller file, but `FilterCriteriaUtil.java` (797) + `EventFilterDTO.java` (156) imply time fields exist.
- Timescale `create_hypertable.sql` is present, so time-range queries are DB-efficient.
- `CWEventDTO.java` (173) has event-time fields.
**Open question.** Does the events endpoint paginate time ranges correctly? The classic UI typically wants "last N minutes/hours" convenience params — may require querystring alias mapping or a wrapper endpoint.

### Syslogs endpoint
**Partially present.**
- `alarm-forwarding-service/.../subscription/` has syslog destination handlers (**outbound** — sending syslogs to external collectors), not an inbound syslog-read REST surface.
- `alarm-rest-service/.../data/{CustomSyslogDTO.java, CustomSyslogRegexDetailsDTO.java, CustomSyslogTestDTO.java}` — custom-syslog CRUD DTOs.
- `event-processing-service/.../messaging/SyslogListener.java` (197) — ingests incoming syslogs.
- `event-processing-service/.../metrics/{SyslogHandlerMetrics.java, SyslogHandlerMetricsImpl.java (551)}` — metrics only.
- `ems-assurance/ifm_alarm_rest_provider_epnm/.../export/SyslogExport.java` (212) — syslog export for download.
**Potential gap.** No obvious dedicated syslog-list REST controller in `cw-epnm-fault`. The classic-UI syslog tab may have been served by `AlarmRest.java` (unified query) or a method on `CustomAlarmsController` that filters to syslog-type events. **Confirm with Jenis which URL the classic syslogs table POSTs.**

### Correlated-alarms tree endpoint
**Present.**
- Frontend: `ems-assurance/cep/cep_rest_ui/.../AlarmManagement/js/CorrelatedAlarms.js` (1,060 lines) + `AlarmCorrelatedView.js` + `CorrelatedAlarmsDetails.html` + `CorrelatedAlarmsTree.html`.
- Backend: `CEPAlarmListener.java`, `CorrelatedAlarm.java`, `CorrelationTree.java`, `FilterExpression` with `CorrelatedFilter.java`.
- `ifm_alarm_rest_provider_epnm/handler/CorrelationHandler.java` (242) — correlation export.
**Open question.** The EMS side has the filter `CorrelatedFilter.java` but the **tree rendering** endpoint (flat vs nested JSON) is not obvious from names. `CWRestController.java` (539) is the likely candidate — ask Jenis for the route name.

### Network-impact / impacting-alarms
**Present (EPNM era only — `ems-assurance`).**
- `network_impact_analysis/.../service/impl/NetworkImpactingAlarmServiceImpl.java` (899)
- `ImpactAnalysis/services-fault-ia-view/` — view entities + oracle DDL
- `ImpactAnalysis/service_impact_analysis_plugin/.../sia/alarm/AlarmManager.java` (535)
**Not found** in `cw-epnm-fault` tree — open question whether impact-analysis classic-UI widgets work against EMS.

### Custom alarms / user preferences
**Present.**
- `alarm-rest-service/.../CustomAlarmsController.java` (1,321), `AlarmSettingsController.java` (751), `UserPreferenceController.java` (247), `UserPreferencesBean.java` (224), `SeverityConfigRestService.java` (1,206), `preferences/{AlarmManagerPreferences.java (291), GnmiPreferences.java (267)}`.

### Next-step / recommended action
**EPNM-era only** — `ems-assurance/NextStep/`, `NextStep-nbi/` + `oam_fault_actions/`. **Not found** in `cw-epnm-fault`. If the classic Inventory/Alarms panel includes a "recommended action" link it will fail on EMS-only deployments.

---

## 11. Top paths for the execution session

Most useful files/dirs to open first when mapping EMS fault endpoints to classic UI screen needs. All absolute under their repo root.

1. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/AlarmRest.java` (2,622 lines) — **the single biggest classic-UI alarms REST surface**.
2. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/CustomAlarmsController.java` (1,321) — custom trap/syslog/gNMI CRUD.
3. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/AlarmUpdateRestController.java` (308) + `services/AlarmActionServiceImpl.java` (718) — clear / ack / annotate.
4. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/util/FilterCriteriaUtil.java` (797) + `data/AlarmFilterDTO.java` (188) + `data/EventFilterDTO.java` (156) — advanced filter grammar.
5. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/View360AlarmController.java` (717) — expandable-row/detail-panel candidate.
6. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/CWRestController.java` (539) + `CWV2RestController.java` (434) — CW branded read APIs.
7. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/resources/ctx/cw-epnm/Alarm-context-restconf.xml` (142) + `applicationContext.xml` (159) — Spring wiring for the REST service.
8. `cw-epnm-fault/alarm-rest/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/networkInventory/NetworkInventoryAlarmController.java` (180) — inventory-side alarm bridge.
9. `cw-epnm-fault/event-processing/event-processing-service/src/main/java/com/cisco/epnm/fault/cw/events/EventsManifestCacheFromDB.java` (347) + `.../cw/showtech/AlarmsShowtechHandler.java` (251) — event documentation + manifest retrieval for the expandable-row detail.
10. `cw-epnm-fault/data-retention/.../db/migration/V8_0_0__baseline.sql` (246) + `V7_0_0__baseline.sql` (1,497) + `V7_0_0_1__create_hypertable.sql` (105) — actual schema of the alarms/events tables the UI reads.
11. `cw-epnm-fault/alarm-rest-service/src/main/java/com/cisco/epnm/fault/alarmrest/swagger/SwaggerConfig.java` (29) + `config/platform/tyk/tykConfigmap.json` (386 at `alarm-rest-config-cw-emf/`) — generated OpenAPI + the Tyk-gateway public route table. **Open both: the Tyk configmap at 386 lines is the definitive public route inventory.**
12. `ems-assurance/cep/cep_rest_ui/src/main/resources/webapp/applications/AlarmManagement/js/CorrelatedAlarms.js` (1,060) — classic-UI correlated-alarms tree reference (tells you the shape the UI expects back).
13. `ems-assurance/fault-nbi/ems-fault-nbi/src/main/java/com/cisco/nms/ems/ems/assurance/nbi/AlarmRestServiceImpl.java` (actually at `com/cisco/nms/ems/assurance/nbi/AlarmRestServiceImpl.java`, 821 lines) — EPNM-era counterpart to `AlarmRest.java`; use to confirm per-route parity.
14. `ems-assurance/fault_ui/src/TopologyAlarmsTabTable.js` (1,307) + `oam_fault_ui/src/main/resources/i18n/nls/en/epnmAlarmManagementProperties.js` (216) — classic-UI column/i18n inventory for the Alarms tab.

---

**Cross-referencing hint for the execution session.** When Jenis joins, the fastest concrete question list is: (a) which `AlarmRest.java` routes back the alarms-table main query; (b) which route serves the expanded-row JSON; (c) clear / ack / annotate route shape; (d) whether there is a separate "syslogs" endpoint or whether syslogs surface via event-filter; (e) Tyk-gateway URL prefix for the classic UI to target; (f) what changed between the `cepnm8.1PI` branch and `develop` in each repo that affects these routes.
