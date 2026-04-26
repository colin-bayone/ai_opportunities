# Agent 04 — EPNM `fault` Repo Tree Extraction

Source tree: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EPNM/tree-reports/fault_tree_report.md`

Repo root (as recorded in the tree): `/Users/cmoore/Documents/programming/EPNM/fault/fault`
- Included text-like files: 9,090
- Included directories: 1,609
- Total raw lines: 2,487,994
- Skipped binary: 19; Skipped ignored-ext: 33

## 1. Repo Shape at a Glance

The `fault/` repo is a monolithic multi-module Maven build (top-level `pom.xml`, `pom_parent.xml`, `pom_testing.xml`, `Jenkinsfile`, `buildAndPatch.sh`, `master_components.txt`). It mixes C++ collection daemons, Java event/alarm processing, a Dojo-based web UI, MIB libraries, and functional test harnesses. Top-level modules roughly split into four tiers:

**Collection tier (C++ + Java receivers).**
- `CPP/` — C/C++ native "Decap" subsystem (trap, syslog, netflow, trace receivers/forwarders, Oracle/file DBs, circular-buffer IPC to Java). Sub-projects: `Decap_core`, `Decap_main`, `Decap_trap`, `Decap_trap_rcv`, `Decap_syslog`, `Decap_netflow`, `Decap_oracle`, `Decap_file`, `Decap_trace`, `Decap_trace_core`, `Decap_cbapi`, `Decap_aggregator`, `Decap_perf_lib`, `Decap_example`, `LogGc`, `NetflowGen`, `SyslogGen`, plus `TestDecap*` projects.
- `Decap_build/` — top-level C++ build config: MIBs under `conf/mibs/` (~160 `.my` files), `conf/syslog/*.xml` Java syslog templates, `conf/AttributeTypes.xml` (18,489 lines), trap processing plans, `log4j.xml`, `xmp_start_scripts/`.
- `decap.processor/` — Java trap/syslog processors (`SyslogProcessorImpl`, `TrapProcessorImpl`, tokenizers, attribute parsers, `CiscoSyslogFormatTokenizer`, MIB file monitor, trap plans).
- `decap.event/` — Java "event" service: alarm cache, event chaining, normalization, physical correlation, persistence.
- `decap_core_java/` — Java core: circular buffer, field collection, filter/forwarder, config parsing, queues, subsystem launcher.
- `decap_codegen/` — MIB-to-XML code generator (trap parsing properties to plan XML).

**Fault semantics & policy tier (Java).**
- `fault_policy/` (umbrella) containing: `fault_policy_impl`, `fault_policy_rest`, `fault_policy_ce` (Correlation-Engine binding), `fault_policy_notification`, `fault_policy_srp` (simple-rule processor framework), `fault_policy_syslog`, `fault_policy_audit_logging`, `fault_policy_dto`, `fault_policy_api`, `fault_policy_testutils`.
- `fault_policy_ui/` — Dojo-based policy management UI (alarm/syslog policies, notification contacts, notification policies).
- `model/fault_policy_model/` — Tigerstripe data-model for fault policy entities.

**Platform / integration tier (NCS + IFM).**
- `ncs_common/` — shared NCS fault utilities (event translation, alarm sync, resource identifiers, impacted-entity modeling, device life cycle).
- `ncs_eventAlarm/` + `ncs_eventAlarm_ext/` — the core alarm/event/syslog sorted caches, dedupe, PI rule engine (percentage/flapping/suppress), group state management.
- `ncs_syslog/` + `ncs_syslog_ext/` — syslog dispatch/filter/translation, syslog-policy action runtime.
- `ncs_tl1/` — TL1 protocol support.
- `ifm_ext/`, `ifm_fault/` (umbrella over `ifm_alarm_adapter/`, `ifm_alarm_rest_provider/`, `ifm_alarm_service/`, `ifm_base_dto/`), `ifm_fault_message/`, `ifm_snmptrap_rest/`, `ifm_trapnotification_ui/`, `ifm_pces_server/` — IFM (Infrastructure Fault Manager) integration layer: REST adapters/services, DTOs, alarm-service engine (`AlarmServiceImpl.java` at 5,075 lines), the master `AlarmRest.java` (7,969 lines).

**Correlation & XMP engines (Java).**
- `xmp_correlation/` + `xmp_correlation_extensions/` — the Java correlation engine: rule parsing, rule contexts, macros, groups-condition, percentage/area rules, phone/collab and network-device rules.
- `xmp_poller/` — SNMP polling algorithm engine (not strictly fault but lives here).
- `xmp_syslog/` — lighter-weight syslog receiver/parser/persister using Hibernate (separate from `Decap_syslog`).

**Test and build scaffolding.**
- `faultComponentTest/`, `faultDevTools/`, `ncsFunctionalTests/`, `nb_trap_receiver/`, `epnm_tp/` (assembly), `buildsonar/`, `design/`, `PMDRules_Selected.xml` everywhere.

**Top-level miscellaneous.** `Jenkinsfile` (127 lines), `buildAndPatch.sh` (314 lines), `README.md` (100 lines), `components.txt`, `master_components.txt`.

## 2. Alarms Subsystem

**Core alarm cache and storage (Java, in `decap.event/`).**
- `decap.event/src/main/java/com/cisco/xmp/decap/event/alarmCache/impl/AlarmCacheImpl.java` (1,359 lines) — central in-memory alarm cache.
- `decap.event/.../alarmCache/impl/AlarmCacheMetricsImpl.java`, `AlarmCacheService.java`, `AlarmLockHandlerImpl.java`, `AlarmWriteBehindThread.java`, `CorrelationAlarmStorageHandler.java`.
- `decap.event/.../alarmCache/AlarmCache.java`, `AlarmCacheMetricsBean.java`, `AlarmCacheCollectedMetrics.java`, `AlarmLockHandler.java`.
- `decap.event/.../model/alarm/xmp/XMPAlarmStorageHandler.java`, `XMPInMemoryAlarmStorageHandler.java`, `EventAlarmHelper.java`, `CSDemoAlarmListener.java`.
- `decap.event/.../model/alarm/AlarmStorageHandler.java`.
- `decap.event/.../bean/impl/DefaultAlarmSeverityUpdatorImpl.java`, `AlarmInfo.java`, `EventChainerImpl.java`, `EventChainer.java` (alarm-creation chaining logic).
- `decap.event/.../impl/LocalAlarmCacheView.java`, `BusinessKeyHelper.java`, `CannedFaultCorrelationHelper.java`.

**Sorted/count caches and comparers (`ncs_eventAlarm/`).** These are the structures the UI most directly reads from for the alarms table.
- `ncs_eventAlarm/src/main/java/com/cisco/ncs/eventAlarm/cache/alarm/SortedAlarmCache.java` (1,057 lines) — primary sorted alarm cache used by list/table queries.
- `ncs_eventAlarm/.../cache/alarm/AlarmCountCache.java` (453 lines), `AlarmCountCacheInitializer.java`, `AlarmCountTuple.java`, `AlarmCacheTuple.java` (182 lines), `AlarmCacheDbInitializer.java`, `AlarmAttributeNames.java`, `AdditionalAlarmAttributesLoader.java`, `GroupSourceListConverter.java` (409 lines).
- `ncs_eventAlarm/.../cache/alarm/comparers/AlarmTupleAlarmCreationTimeComparer.java`, `AlarmTupleOwnerComparer.java`, `AlarmTupleStatusComparer.java`, `AlarmTupleUDFMapComparer.java`.
- `ncs_eventAlarm/.../cache/alarm/filters/CategoryFilter.java`, `ClearedFilter.java`, `CorrelatedFilter.java`, `FilterExpression.java`, `IAttributeValuePair.java`, `IFilterExpression.java`.
- `ncs_eventAlarm/.../cache/comparers/AlarmEventTupleSeverityComparer.java`, `AlarmEventTupleCategoryComparer.java`, `AlarmEventTupleConditionComparer.java`, `AlarmEventTupleDescriptionComparer.java`, `AlarmEventTupleDeviceTimestampComparer.java`, `AlarmEventTupleFailureSourceComparer.java`, `AlarmEventTupleInstanceIdComparer.java`, `AlarmEventTupleRackIdComparer.java`, `AlarmEventTupleSrcObjectClassIdComparer.java`, `AlarmEventTupleSrcObjectIdComparer.java`, `AlarmEventTupleTimestampComparer.java`.
- `ncs_eventAlarm/.../AlarmCountContainer.java`, `AlarmSummaryCacheDbInitializer.java`, `AlarmSummaryCountCache.java`, `AlarmSummaryCountMetrics.java`, `AlarmSummaryCounter.java`.
- `ncs_eventAlarm/.../suppression/AlarmSuppressionQueryService.java`, `AlarmSuppressionQueryServiceImpl.java`, `SustainedIssueTimerTask.java`.

**Interfaces (contracts).**
- `ifm_ext/src/main/java/com/cisco/ncs/eventAlarm/cache/alarm/IAlarmCountCache.java`, `ISortedAlarmCache.java`.
- `ifm_ext/.../cache/IAlarmEventCache.java`, `ISortedCache.java`.
- `ncs_eventAlarm_ext/src/main/java/com/cisco/ncs/eventAlarm/cache/IAlarmCountCacheInitializer.java`, `IAlarmEventCacheInitializer.java`, `IGroupSourceListConverter.java`, `ISortedCacheInitializer.java`, `IVirtualDomainFilter.java`, `IAlarmCountContainer.java`, `IAlarmSummaryCacheInitializer.java`, `IAlarmSummaryCountCache.java`.

**Alarm service (IFM — this is the main business-logic entry point).**
- `ifm_fault/ifm_alarm_service/src/main/java/com/cisco/ifm/alarmservice/impl/AlarmServiceImpl.java` (5,075 lines) — the master alarm service implementation.
- `ifm_fault/ifm_alarm_service/.../impl/AlarmServiceUtilImpl.java` (1,524 lines), `AlarmSummaryUtil.java`, `AlarmNoteDbUtil.java`, `AlarmGroupBadgeIconImpl.java` (555 lines), `AlarmQuickViewUtil.java` (745 lines), `AlarmDashletUtil.java` (526 lines), `CallbackManagerImpl.java`, `CommonDashletDTOComparator.java`, `EventSeverityComparator.java`, `LegacyDeviceCriteria.java`, `DMPreferenceUtil.java`, `DataFormatUtil.java`, `IndexValidationUpgradeHook.java`, `SyslogDataUtil.java`.
- `ifm_fault/ifm_alarm_service/.../AlarmService.java` (564 lines), `AlarmCallback.java`, `AlarmCallbackManager.java`, `EventCallbackHandler.java`.
- `ifm_fault/ifm_alarm_service/.../services/alarm/AlarmQueryService.java`, `AlarmQueryServiceImpl.java`.
- `ifm_fault/ifm_alarm_service/.../services/queries/alarm/*` — `AlarmListQuery.java`, `AlarmSummaryQuery.java`, `AlarmCountsByCategoryQuery.java`, `AlarmCountsByDeviceQuery.java`, `AlarmCountsBySeverityQuery.java`, `AlarmCountsByTypeQuery.java`, `AlarmTabSummaryQuery.java`, `AlarmQueries.java`, `MostRecentNotesForAlarmsQuery.java`, `AbstractAlarmAggregateQuery.java`.
- `ifm_fault/ifm_alarm_service/.../services/queries/data/AnnotatedAlarm.java`, `AlarmTabSummary.java` (likely the annotated/note-attached shape rendered in the expandable rows).

**REST exposure / endpoints (Java DTOs and services).**
- `ifm_fault/ifm_alarm_rest_provider/src/main/java/com/cisco/ifm/alarmrest/AlarmRest.java` (**7,969 lines** — by far the largest REST entry; likely hosts most /webacs alarm endpoints).
- `ifm_fault/ifm_alarm_rest_provider/.../services/AlarmRestService.java` (763 lines), `AlarmEventRestService.java` (350 lines), `AlarmClassService.java`, `DashletRestService.java`, `EventRestService.java` (605 lines), `SeverityConfigRestService.java` (1,521 lines), `SyslogRestService.java` (429 lines).
- `ifm_fault/ifm_alarm_rest_provider/.../AlarmSettingsBean.java`, `AlarmStatsKey.java`, `AlarmStatsUtil.java`, `AlarmActionUtil.java`, `AlarmMapping.java`, `FilterCriteriaUtil.java` (705 lines), `PaginationUtil.java`, `UserPreferencesBean.java`.
- `ifm_fault/ifm_alarm_rest_provider/.../dao/AlarmSettingsDao.java`, `MailConfigDao.java`, `UserPreferncesDao.java` [sic].
- `ifm_fault/ifm_alarm_adapter/src/main/java/com/cisco/ifm/rest/adapter/AlarmRestAdapterImpl.java` (489 lines), `IAlarmRestAdapter.java` (219 lines), `DTOConversionUtil.java`, `AlarmRestAdapterException.java`.
- `ifm_fault/ifm_alarm_adapter/.../dtobuilder/AlarmDtoBuilder.java` (568 lines), `WiredWirelessAlarmDtoBuilder.java`, `WiredWirelessAlarmUdfDTO.java`.

**DTOs (shared JAXB types, probably serialized to the UI).**
- `ifm_fault/ifm_base_dto/src/main/java/com/cisco/ifm/base/dto/alarm/AlarmDTO.java` (547 lines), `EventDTO.java` (388 lines), `SyslogDTO.java` (221 lines), `AlarmCountDTO.java`, `AlarmNoteDTO.java`, `AlarmCommandDTO.java`, `AlarmCommandListDTO.java`, `AlarmRelatedHistoryDTO.java`, `AlarmSeverityStatsDTO.java` (217 lines), `AlarmStatsDTO.java`, `AlarmSummaryDTO.java`, `AlarmSummaryDashletDTO.java`, `AlarmTabDecoratorDTO.java`, `AlarmDeviceEventListDTO.java`, `GeneralInformationEventDTO.java` (372 lines), `DeviceDetailsListDTO.java`, `GroupListDTO.java`, `jaxb.index`.
- `ifm_fault/ifm_alarm_rest_provider/.../services/dto/GroupedAlarmDTO.java`, `GroupedAlarmEventDTO.java`, `GroupedEventDTO.java`, `RecentClearedAlarmDTO.java`, `SeverityCountsDTO.java`, `EventTypeDTO.java`.

**Alarm annotation / notes.** `ifm_fault/ifm_alarm_service/.../impl/AlarmNoteDbUtil.java`, queries `MostRecentNotesForAlarmsQuery.java`, DTO `AlarmNoteDTO.java`.

## 3. Events Subsystem

**Event persistence and services (`decap.event/`).**
- `decap.event/src/main/java/com/cisco/xmp/decap/event/EventChain.java`, `EventService.java` (392 lines), `EventProcessingManager.java`, `EventRecord.java`, `EventServiceException.java`, `FaultProperties.java`, `Literals.java`, `DecapModelEnum.java`, `EventInfo.java`.
- `decap.event/.../bean/impl/EventServiceImpl.java` (854 lines), `EventChainerImpl.java` (742 lines), `EventCorrelationKeyEvaluatorImpl.java`, `EventEnhancementImpl.java`, `ConfigurationBasedEventNormalization.java` (478 lines), `MultiThreadedTimeWindowEventHandler.java`, `TimeWindowEventHandler.java`, `AbstractTimeWindowEventHandler.java` (769 lines), `WriteBehindThread.java`, `ShowFieldCollectionEventPreProcessor.java`, `IntraDevicePhysicalHierarchyEvaluator.java` (769 lines), `IntraDevicePhysicalHierarchyProviderImpl.java`.
- `decap.event/.../impl/EventProcessingManagerImpl.java` (361 lines), `EventProcessor.java`, `EventRecordImpl.java`, `EventServicesMBean.java`, `FaultPerformanceMetricsBean.java`, `GenericLookupEnumPopulator.java`, `TimeWindowEventHandlerMetrics.java`, `TimeWindowEventHandlerMetricsBean.java`, `LocalLogger.java`, `EventAttributeTypes.java`, `EventChainImpl.java`.
- `decap.event/.../eventType/EventType.java`, `EventTypeDoc.java` (363 lines), `IEventTypeManager.java`, `impl/EventTypeManager.java` (570 lines), `impl/EventTypeContextFileManager.java`, `PolicyType.java`, `Use.java`, `Visibility.java`.
- `decap.event/.../category/EventAlarmCategory.java`, `impl/EventAlarmCategoryManager.java` (358 lines), `impl/CategoryContextFileManager.java`, `IEventAlarmCategoryManager.java`, `CategoryLicenseType.java`, `CategoryQueryMode.java`.
- `decap.event/.../config/impl/EventTemplate.java` (270 lines), `SourceSpec.java` (288 lines), `EventNormalizationSpecification.java`, `ConfigTrapSyslogList.java`, `PhysicalEventCauseHierarchyEvaluatorSpecification.java`, `EventChainingSpecification.java`.
- `decap.event/.../parser/EventConfigHandler.java`, `persist/impl/EventAlarmDMMPersistenceInitBean.java`, `persist/impl/EventAlarmStorageAccessor.java`, `persist/impl/HibernateServices.java`, `persist/impl/PersistenceCommon.java`.
- `decap.event/.../model/event/xmp/XMPEventObjectHandler.java`, `XMPEventStorageHandler.java`, `XMPInMemoryEventStorageHandler.java` (226 lines), `XMPTemplateBasedEventPopulator.java`, `fw/XMPEventToAlarmPopulator.java`, `fw/XMPEventToAlarmPopulatorImpl.java`, `fw/EventToAlarmSpecification.java`, `fw/AuthEntityHandler.java`, `fw/ConfigurationBasedEventUtil.java`, `fw/EventCommon.java`.
- `decap.event/.../model/event/fc/FieldCollectionEventObjectHandler.java`, `FieldCollectionEventStorageHandler.java`, `FieldCollectionTemplateBasedEventPopulator.java`.
- `decap.event/.../normalizer/configBased/bean/impl/SourceCalculator.java` (341 lines), `SeverityCalculator.java`, `NotificationTimestampCalculator.java`, `NotificationDeliveryMechanismCalculator.java`, `ReportingEntityAddressCalculator.java`, `ConcatCalculator.java`, `FieldCalculator.java`, `InterfaceNameLookupFromIfIndex.java`, `CSDemoSourceCalculator.java`.

**Sorted event cache, time-windowed query (`ncs_eventAlarm/`).**
- `ncs_eventAlarm/.../cache/event/SortedEventCache.java` (579 lines) — this is the prime place to look for time-windowed "events in the last N hours" queries backing the events popup and events full page.
- `ncs_eventAlarm/.../cache/event/EventCacheDbInitializer.java` (295 lines), `EventCacheTuple.java` (115 lines), `EventAttributeNames.java`, `AdditionalEventAttributesLoader.java`, `DataPruningStatusPoller.java`.
- `ncs_eventAlarm/.../cache/SortedCacheBase.java` (761 lines) — shared base across alarm/event/syslog sorted caches.
- `ncs_eventAlarm/.../cache/comparers/...` (see Alarms section — tuple comparers shared).
- `ifm_ext/.../cache/event/ISortedEventCache.java`.
- `ifm_fault/ifm_alarm_service/.../services/queries/event/EventListQuery.java`, `EventCountsBySeverityQuery.java`, `EventCountsByTypeQuery.java`, `AbstractEventAggregateQuery.java`.
- `ifm_fault/ifm_alarm_service/.../services/event/EventQueryService.java`, `EventQueryServiceImpl.java`.
- `ncs_eventAlarm/.../EventCreator.java`, `EventImporterPostInitHook.java`, `EventImporterRunnable.java`.

**Event type metadata (very large — used by UI dropdowns and policies).**
- `ncs_eventAlarm/src/main/resources/META-INF/spring/eventTypes.xml` (**5,925 lines**), `eventTypesDoc.xml` (5,467 lines), `eventTypes.bkp_251` (5,930 lines), `eventTypes_EPNM.xml`, `eventTypes_Inventory.xml`, `eventTypes_Unused.xml`, `eventTypes_UsedAsTrigger.xml`, `eventTypes_UsedForMessage.xml`, `eventTypes_UsedForSeverity.xml`, `eventAlarmCategories.xml` (359 lines).
- `ncs_eventAlarm/.../eventTypeApp/EventTypeCSVToXML.java`, `EventTypeXMLToCSV.java`, `UpdateExplanationFromDoc.java`, `EventTypeRow.java`, `BeanTag.java`, `BeansTag.java`, `PropertyTag.java`, `Tag.java`.

**Event translation (NCS → common).**
- `ncs_common/.../event/impl/EventTranslationTemplate.java` (780 lines), `AbstractCustomerEventMapping.java`, `AbstractEventMappingMonitor.java`, `AbstractEventTranslationService.java`, `GenericAlarmSynchronization.java`, `SyslogTranslate.java`, `NCS42xxAlarmSynchronization.java`, `NCS42xxDeviceLifeCycle.java`, `NCS42xxInventoryHooks.java`, `ScapaAlarmManagerSync.java`, `ScapaDeviceLifeCycle.java`, `ScapaInventoryHooks.java`.
- `ncs_common/.../event/EventFormatterUtilImpl.java` (1,327 lines), `EventDisplayNameHelper.java`, `EventSynchServiceImpl.java` (632 lines), `DeviceSynch.java`, `DeviceSynchMonitorTask.java`, `EventProcessorConfigs.java`, `EventResourceLookup.java`.
- `ncs_eventAlarm/.../NCSEventTranslator.java`.

## 4. Syslog Subsystem

**Receivers / collectors (C++).**
- `CPP/Decap_syslog/` — includes/src split into `config/` (AttributeParser, SyslogType, SyslogTypeCriteria, SyslogFormat, all with Cfg-Tmpl managers), `processor/` (`SyslogProcessorThread.cpp` 336 lines, `SyslogFormatTokenizer.cpp`, `TokenizerAV.cpp` 1,584 lines, `TrapProcessor.cpp`), `forwarder/` (`SyslogForwarder.cpp` 411 lines, `SyslogForwardingRecord.cpp`, `SyslogFilter.cpp`, `HpSyslogDBTranslator.cpp`, `ClaytonSyslogDBTranslator.cpp`, `RawSyslogMsgTranslator.cpp`), `project/DecapSyslogProject.cpp`.
- `CPP/SyslogGen/` — test syslog generator with sample files `syslog_acs1.txt`, `syslog_event.txt`, `syslog_wcs.txt`, `syslogs_basic.txt` etc.

**Parsers and tokenizers (Java, `decap.processor/`).**
- `decap.processor/.../processor/impl/SyslogProcessorImpl.java` (660 lines), `SyslogProcessorBean.java`, `SyslogMetricsBean.java`.
- `decap.processor/.../syslog/impl/SyslogContextImpl.java`, `SyslogContext.java`, `Tokenizer.java`, `ExtractField.java`, `ISyslogTemplate.java`.
- `decap.processor/.../tokenizer/impl/CiscoSyslogFormatTokenizer.java` (1,206 lines), `BasicWordTokenizer.java`, `AbstractTokenizer.java`, `AcsTokenizer.java`, `RegexTokenizer.java`, `FormatTokenizerFactory.java`, `MessageTokenizerFactory.java`, `ArrayListRecordWriter.java`, `AttrValueParserResult.java` (544 lines), `SyslogSeverityCharacters.java`, `Token.java`, `TokenArrayList.java`.
- `decap.processor/.../tokenizer/attributeParser/impl/` — many specialized parsers: `AcsNameValuePairAttributeParser.java`, `BSDIPAddressAttributeParser.java`, `CiscoFormatTypeAttributeParser.java`, `CiscoSyslogKeyAttributeParser.java`, `CollabNameValuePairAttributeParser.java`, `EventNotificationTimestampAttributeParser.java`, `IndexBetween*`, `IndexTo*`, `NodeIdAttributeParser.java`, `ProxyIPAttributeParser.java`, `RawRcvSecAttributeParser.java`, `RcvSourceIpAttributeParser.java`, `RegexAttributeParser.java`, `SimpleConstStringAttributeParser.java`, `SingleAttributeParser.java`, `AttributeParserFactory.java`, `AttributeParserHelper.java` (402 lines).
- `decap.processor/.../tokenizer/subfunction/impl/` — `BsdFacilitySubFunction.java`, `BsdPrioritySubFunction.java`, `BsdSeveritySubFunction.java`, `AsciiBsdFacilitySubFunction.java`, `RemovePercentSubFunction.java`, `StringSplitSubFunction.java`, `SubFunctionFactory.java`, `SyslogKeyToIdSubFunction.java`.
- `decap.processor/.../processor/config/impl/SyslogFormatSpecification.java`, `SyslogFormatTemplate.java`, `SyslogFormatTemplateFile.java` (348 lines), `SyslogFormatTemplates.java`, `SyslogSeverityEnum.java`, `SyslogTemplate.java` (216 lines), `SyslogTemplateFile.java` (349 lines), `SyslogTemplates.java`, `TabSeparatedInputFile.java`.
- `decap.processor/.../relay/impl/SyslogRelay.java`, `SyslogRelayBean.java`, `SyslogTranslatorImpl.java`.
- `decap.processor/src/main/resources/syslog/*.xml` — multiple template XMLs: `ACSSyslogTemplatesJava.xml`, `CorrelationSyslogTemplatesJava.xml`, `DynAttrSyslogTemplatesJava.xml`, `FanSyslogTemplatesJava.xml`, `IOSXESyslogTemplatesJava.xml`, `InventorySyslogTemplatesJava.xml`, `NAMSyslogTemplatesJava.xml`, `NVEdgeSyslogTemplatesJava.xml`, `StormSyslogTemplatesJava.xml`, `SyslogTemplatesJava.xml` (361 lines), `WCSSyslogTemplatesJava.xml`.

**Syslog dedupe, live cache, UI-facing (`ncs_eventAlarm/`).**
- `ncs_eventAlarm/.../cache/syslog/SortedSyslogCache.java` (577 lines) — the sorted cache behind the syslog list UI.
- `ncs_eventAlarm/.../cache/syslog/SyslogCacheDbInitializer.java`, `SyslogCacheTuple.java`, `SyslogAttributeNames.java`.
- `ncs_eventAlarm/.../cache/syslog/comparers/SyslogTupleDescriptionComparer.java`, `SyslogTupleDeviceNameComparer.java`, `SyslogTupleDeviceTimestampComparer.java`, `SyslogTupleFacilityComparer.java`, `SyslogTupleMnemonicComparer.java`, `SyslogTupleProxyIpComparer.java`, `SyslogTupleSeverityComparer.java`, `SyslogTupleSourceComparer.java`, `SyslogTupleTimeComparer.java`.
- `ncs_eventAlarm/.../cache/syslog/dedupe/LiveSyslogCache.java` (214 lines) + `LiveSyslogSender.java`, `DeduplicatingSyslogQueue.java`, `DoublyLinkedList.java`, `Node.java`, `SyslogNodeMap.java`, `SyslogTuple.java`.
- `ifm_ext/.../cache/syslog/ISortedSyslogCache.java`.

**Syslog dispatch/filter/translation (`ncs_syslog/`).**
- `ncs_syslog/.../SyslogHandler.java` (762 lines), `SyslogDispatcher.java`, `SyslogDispatcherFactoryImpl.java`, `SyslogFilterRepository.java`, `SyslogConfigurationMonitor.java`, `SyslogConfigurationRequestApplication.java`, `SyslogHandlerMetricsImpl.java`.
- `ncs_syslog/.../AuthmgrSyslogFilter.java` (482 lines), `GenericSyslogFilter.java`, `NAMSyslogFilter.java`, `TranslationSyslogFilter.java`, `LinkDownSyslogDescriptionCalculator.java` (322 lines), `NCSSyslogDeviceTimestampCalculator.java`, `StringSetWCSPreference.java`.
- `ncs_syslog/.../event/SyslogCustomerEventMapping.java`, `SyslogEventMappingMonitor.java`, `SyslogEventTranslationService.java`, `SyslogEventTranslationTemplate.java`.
- `ncs_syslog/.../rest/SyslogEventMapping.java`, `SyslogEventMappingOutput.java`, `UserDefinedSyslogTranslationService.java`, `metadata/SyslogEventMappingMetadata.java`, `metadata/SyslogEventMappingOutputMetadata.java`, `ObjectFactory.java`.
- `ncs_syslog/src/main/resources/deploy/conf/fault/syslog/*.xml` — translation rules by category (`AuthmgrSyslogFilterContext.xml`, `BGPSyslogTranslation.xml`, `CESyslogFilterContext.xml`, `CFMSyslogTranslation.xml` (291 lines), `CustomerSyslogFilterContext.xml`, `EIGRPSyslogTranslation.xml`, `ErrorDisableSyslogTranslation.xml`, `FanSyslogTranslation.xml` (333 lines), `FijiSyslogFilterContext.xml`, `GenericSyslogFilterContext.xml`, `IOSXESyslogTranslation.xml`, `OpticalSyslogFilterContext.xml`, `SyslogTranslation.xml` (746 lines)).
- `ncs_syslog_ext/.../ISyslogDispatcher.java`, `SyslogBeanNames.java`, `SyslogDispatcherFactory.java`.

**Lightweight syslog receiver (`xmp_syslog/`).**
- `xmp_syslog/.../impl/SyslogReceiver.java` (321 lines), `SyslogParser.java`, `DeviceTimestampExtractor.java`, `SyslogStore.java`, `SyslogPropertyPlaceholderConfigurer.java`.
- `xmp_syslog/.../db/FieldCollectionDBFactory.java`, `FieldCollectionOracleDB.java` (470 lines), `FieldCollectionMongoDB.java`.
- `xmp_syslog/.../model/XmpSyslog.java` (333 lines), `intf/FieldCollectionDB.java`, `intf/ISyslogConstant.java`, `intf/SyslogListener.java`, `intf/FacilitySeverityMnemonicSelector.java`, `intf/FieldCollectionIdMapping.java`.
- `xmp_syslog/.../log/SyslogLoggingHelper.java` (465 lines).
- `xmp_syslog/src/main/resources/mapping/hibernate/model/xmpSyslog.hbm.xml`, `deploy/bin/db_scripts/oracle/xmp_syslog_ddl.sql`.

**REST / service layer for syslogs.**
- `ifm_fault/ifm_alarm_service/.../services/syslog/SyslogQueryService.java`, `SyslogQueryServiceImpl.java`.
- `ifm_fault/ifm_alarm_service/.../services/queries/syslog/SyslogListQuery.java` (310 lines), `SyslogCountsBySeverityQuery.java`, `SyslogsByPatternQuery.java`, `TopSyslogSendersQuery.java`, `AbstractSyslogQuery.java`.
- `ifm_fault/ifm_alarm_rest_provider/.../services/SyslogRestService.java` (429 lines).

## 5. Correlation Engine

**Core correlation engine (`xmp_correlation/` and `xmp_correlation_extensions/`).** Rule engine framework — the 10,000-line region of the tree holds rule XML configuration (`spring/rules/`, `spring/countRules/`, `spring/simplifiedRules/`, `spring/collab/`, `spring/batchRules/`) plus the parsing/evaluation code. Notable:
- `xmp_correlation_extensions/.../group/GroupStateManager.java` (417 lines), `AbstractGroupsCondition.java` (388 lines), `GroupsCondition.java`, `GroupsInstance.java`, `GroupsInstanceImpl.java`, `PercentageAreaGroupsCondition.java`, `PercentageGroupRuleAction.java`, `PercentageGroupsCondition.java`, `GroupState.java`, `GroupMemberState.java`, `GroupImpactState.java`, `GroupStateChanged.java`, `AreasToLeaves.java`, `AlarmStateService.java`, `AlarmStateServiceImpl.java`, `ClassTranslation.java`, `ClassTranslationModelMetaData.java`.
- `xmp_correlation_extensions/.../CorrelationExtensionsDependencyServiceProviderImpl.java`, `GRTDependencyService.java`, `PersistenceInitBean.java`.
- `xmp_correlation/` — rule XML in `src/test/resources/spring/rules/` (e.g., `FlappingRules.xml`, `RestartRules.xml`, `CpuMemRules.xml`, `ConstrainedIORules.xml` 194 lines, `PICpuThresholdRules.xml` 157 lines, `PhoneDependencyDelayedRules.xml`, `UCCERules.xml`, `SerialRules.xml`, `EventFilterRules.xml`, `ModuleInterfaceDependencyRules.xml` 157 lines under `forNCS/`), plus `CorrelationEngineContext.xml`, `corrEngine.xsd`. Translation resources `EventTranslate.xml` (497 lines), `TrapAsFCTranslation.xml`.

**Policy-engine binding to correlation (`fault_policy/fault_policy_ce/`).**
- `fault_policy/fault_policy_ce/.../ce/CorrEngPolicyEngine.java` (281 lines), `RuleBuilder.java` (682 lines), `RuleExpressionMethods.java`, `RuleConstants.java`.
- `fault_policy/fault_policy_impl/.../correng/TCorrelationEngine.java`, `CERule.java`, `SLRule.java`, `CEAction.java`, `CECriteria.java`, `ActionSequence.java`, `EvalResult.java`, `FluentFuture.java`, `StateKeySelector.java`, `StatefulAction.java`, `StatelessAction.java`, `StatefulCriteria.java`, `StatelessCriteria.java`, `EmptyAction.java`.
- `fault_policy/fault_policy_impl/.../impl/CEPolicyEngine.java`.
- `fault_policy/fault_policy_srp/.../rp/base/impl/*` — simple rule-processor skeleton: `RuleImpl.java`, `RuleManagerImpl.java`, `ProcessorImpl.java`, `ContextImpl.java`, `AndCriteria.java`, `ActionResultImpl.java`, `CriteriaResultImpl.java`, `WrappedSimpleAccAction.java`, `WrappedSimpleCriteria.java`. Item/key abstractions: `ItemManagerImpl.java`, `ItemNodeImpl.java` (483 lines), `KeyImpl.java`, `ValueKey.java`, `NameValueKey.java`, `KeyHolderFactory.java`.

**NCS-level alarm-to-alarm correlation.**
- `ncs_eventAlarm/.../impl/NmsEventToNmsAlertCorrelator.java` (462 lines) — core event→alert correlator.
- `ncs_common/.../event/impl/ImpactedAndReportingHelperImpl.java` (298 lines), `ImpactedAndReportingHelper.java`, the whole `ncs_common/.../event/impacted/` package (`ImpactedAp.java`, `ImpactedLradIf.java`, `ImpactedManagedNetworkElement.java`, `ImpactedNgwcPort.java`, `ImpactedPort.java`, `ImpactedWlanController.java`, `ImpactedInterfaceProtocolEndpoint.java`, `Impacted.java`, `AbstractImpactedInterfaceGroupable.java`, `AbstractImpactedMNEGroupable.java`, plus AP-wrapper subtypes).
- `ncs_eventAlarm/.../impacted/ImpactedCreationHelper.java`, `ImpactedCreationHelperImpl.java` (276 lines), `ImpactedQueryHelper.java`, `ImpactedQueryHelperImpl.java`.

**Physical-hierarchy / "GRT" correlation.**
- `decap.event/.../physicalCorrelation/PopulateGRTBean.java` (398 lines), `PartialGRTCache.java`.
- `decap.event/.../impl/CannedGRTEntry.java`, `CannedFaultCorrelationHelper.java` (338 lines).
- `Decap_build/conf/GRTEntries.xml` (1,221 lines), `GRTEntries.xsd`.

**Correlation config (what rules to run).**
- `Decap_build/conf/CorrelationEventPopulate.xml`, `CorrelationEventProcessing.xml`, `CorrelationRules.xml`.
- `Decap_build/conf/EventPopulate.xml` (477 lines), `EventProcessing.xml`, `EventPopulateCSDemo.xml`, `FieldCollectionEventPopulate.xml` (418 lines), `EventAttributeTypes.xml`, `EventAlarmDMMApplicationConfig.xml`.

**Correlation functional tests.** `ncsFunctionalTests/src/test/resources/eventSenders/rootCause/sameInterval/*.xml`, `rootCause/twoIntervals/condition/`, `rootCause/twoIntervals/interfaceDown/`, `rootCause/twoIntervals/interfaceUp/` (with 20+ `SendCond*Rules.xml`, `SendIntDown_*Rules.xml` and paired up/down scenarios — these document the exact correlation scenarios the system ships with). Plus `flapping/`, `repeatedRestart/`, and `SendModuleLinkBaseRules.xml` (291 lines).

## 6. Frontend Surface

There are two clearly distinct UI layers in this repo. Both are Dojo/Dijit-flavored (AMD modules, `_WizardPaneMixin`, `DG.html`, etc.) — not React.

**Alarm/Syslog Policy management UI (`fault_policy_ui/`).**
Not the alarms table itself; this is the policy-configuration UI. Located at `fault_policy_ui/src/main/webapp/applications/`.
- `fault_policy_ui/.../applications/AlarmPolicies/js/AlarmPolicyWizardCommons.js` (**4,115 lines**), `AlarmPolicyDetailsCommons.js` (1,025 lines), `AlarmPolicyConstants.js`, `PolicyTypes.js`, `auth.js`, `wizard/contextual/ContextualAlarmPolicyWizard.js`.
- `fault_policy_ui/.../applications/AlarmPolicies/html/AlarmPolicies.html`, `AlarmPolicyDetails.html`, `AlarmPolicyDetailsDG.html` (DG = DataGrid), `AlarmPolicyWizard.html`.
- `fault_policy_ui/.../applications/AlarmPolicies/css/alarmPolicies.css`, `alarmPolicyDetails.css`, `alarmPolicyWizard.css` and SVG icons (`sustain_time_icon.svg`, `threshold_icon.svg`).
- `fault_policy_ui/.../applications/AlarmPolicies/data/*.json` — seed JSON for policy wizards (`AccessPointAlarms.json`, `ControllerAlarms.json`, `InterfaceAlarms.json`, `Layer2SwitchAlarms.json`, `WiredInfrastructureAlarms.json`, `FaultPolicy*EventsList.json`, `policies.json`).
- `fault_policy_ui/.../applications/NotificationContact/*` — HTML templates and JS for notification-contact configuration (email, trap receiver v2/v3, REST-conf).
- `fault_policy_ui/.../applications/NotificationPolicies/*` — `AlarmNotificationWizard.js` (620 lines), `AlarmNotificationListView.js` (766 lines), `EventTypeWizardPane.js` (1,618 lines), `ActionListWizardPane.js` (1,222 lines), many wizard panes for email, trap, web-socket, and virtual-domain destinations.
- `fault_policy_ui/.../applications/faultPolicy/` — generic policy framework used by both alarm and syslog policies: `listView/PolicyListView.js` (543 lines), `listView/alarm/AlarmPolicyListView.js`, `listView/syslog/SyslogPolicyListView.js`, `wizard/PolicyWizard.js` (1,253 lines), `wizard/alarm/panes/EventTypePane.js` (802 lines), `wizard/alarm/panes/SuppressionTypePane.js`, `wizard/syslog/panes/email/EmailPane.js`, `wizard/syslog/panes/script/ScriptPane.js`, `wizard/syslog/panes/url/URLPane.js`, `wizard/syslog/panes/syslogType/SyslogMessagePane.js`, `util/transform/alarm/alarm-policy-transform.js`, plus sprawling NLS (`en/`, `ja/`, `ko/`) trees.

**Trap notification UI (`ifm_trapnotification_ui/`).**
- `ifm_trapnotification_ui/src/main/webapp/applications/trapnotification/js/TrapNotificationWidget.js` (409 lines) + `html/trapNotification.jsp`, `templates/TrapNotificationWidget.html`, `css/TrapNotification.css`, `data/trapTableColumnStructure.json` (82 lines — column schema), and i18n `nls/en,ja,ko/trapNotificationProperties.js`.
- Also `sysmonsettings/html/trapNotification.jsp` (167 lines) variant.

**Gap: core Alarms/Events/Syslogs "browser" UI.** The runtime alarms table itself (expandable rows, correlated alarms, clear action, notes, events popup, syslogs page) is **not** in this repo under a `webapp/` the way the policy UI is. Candidate locations for where that UI actually lives:
1. In the `assembly/` repo (Akhil's "assembly is on the UI side").
2. As a separate UI module outside this repo.
3. Generated/served from JSP templates paired with the REST endpoints in `AlarmRest.java` (7,969 lines) and `AlarmRestService.java`, `AlarmEventRestService.java`, `EventRestService.java`, `SyslogRestService.java` under `ifm_fault/ifm_alarm_rest_provider/`.

What's definitely HERE on the UI side that the execution session should ingest:
- The column-structure JSON for trap-notification (template for alarm-table column schema): `ifm_trapnotification_ui/.../data/trapTableColumnStructure.json`.
- DTO shapes (`AlarmDTO.java`, `EventDTO.java`, `SyslogDTO.java`) as the wire contract the new UI must serialize/consume.
- Policy-wizard `EventTypePane.js` / `_EventTypeColumns.js` as column-model precedent.

## 7. MIB / .my files

MIB libraries appear in three places and are the authoritative device-definition source:

1. **`Decap_build/conf/mibs/`** (top-level, primary) — ~160 MIB files. Wireless-heavy: `AIRESPACE-*`, `ARUBA-*`, `CISCO-LWAPP-*` (~50 LWAPP MIBs covering WLAN, AP, mesh, RRM, mobility, rogue, IPS, IDS, WebAuth, CDP, QoS, DHCP, DOT11, etc.), `bsnwras.my` (14,822 lines), `ORiNOCO-MIB.my` (9,176 lines), `AIRESPACE-WIRELESS-MIB.my` (14,845 lines). Wired/common: `CISCO-STACK-MIB.my` (13,053 lines), `CISCO-RTTMON-MIB.my` (12,392 lines), `CISCO-RHINO-MIB`, `CISCO-VTP-MIB`, `CISCO-VPDN-MGMT-MIB`, `CISCO-PAE-MIB`, `CISCO-ENTITY-FRU-CONTROL-MIB`, `CISCO-ENTITY-SENSOR-MIB`, `CISCO-ENTITY-VENDORTYPE-OID-MIB` (4,840 lines), `CISCO-FLASH-MIB`, `CISCO-IMAGE-MIB`, `CISCO-CONFIG-COPY/MAN-MIB`, `CISCO-LICENSE-MGMT-MIB`, `CISCO-RF-MIB`, `CISCO-MAC-NOTIFICATION-MIB`, `CISCO-STACKWISE-MIB`, `CISCO-SYSLOG-MIB`, `CISCO-TC.my`, `CISCO-ST-TC.my`. Standard: `IF-MIB.my` (1,996), `BRIDGE-MIB`, `ENTITY-MIB`, `IP-MIB` (5,171), `LAG-MIB`, `LLDP-MIB`, `MAU-MIB`, `P-BRIDGE`/`Q-BRIDGE`, `RFC1213-MIB`, `RFC1271-MIB`, `RMON-MIB`, `RMON2-MIB`, `SNMPv2-*`, `TOKEN-RING-RMON-MIB`, `IEEE8021-CFM-MIB`, `IEEE8021-PAE-MIB`, `IEEE802dot11-MIB`, `FDDI-SMT73-MIB`, `INET-ADDRESS-MIB`, `IANAifType-MIB`, `ISDN-MIB`. Third-party: Aruba (`.mib`), WLSX-*, Cognio, Orinoco.
2. **`CPP/Decap_build/conf/mibs/`** — essentially a duplicate set for the C++ build. Same filenames, sometimes slightly different line counts (e.g., `CISCO-LWAPP-AP-MIB.my` is 3,941 lines here vs 4,788 at top level).
3. **`decap_codegen/src/main/mibs/`** — inputs to the codegen that produces `TrapAttributeTypes.xml` / `TrapParsingPlan.xml` (~110 MIBs; subset of 1).
4. **`decap.processor/src/test/resources/MIBsForTest/CISCO-VSAN-MIB.my`** — single MIB shipped for processor tests.
5. **`faultComponentTest/src/main/resources/conf/da/mibs/userprovided/EVNTAGENT-MIB.mib`** — user-provided sample for component tests.

Device-family coverage inferred from MIB names: LWAPP/CAPWAP wireless (APs, controllers, clients, mobility, mesh, rogue, IPS), wired switching (Catalyst stack, VTP, VLAN, MAC notification), routing (RTTMon, VPDN, ISDN, FDDI, Token Ring), environment monitoring (FRU, sensors, power, fans, voltage, temperature), WAN (Aruba, UCS `CISCO-UNIFIED-COMPUTING-MIB`).

Supporting XML (not MIB but closely coupled) at `Decap_build/conf/`:
- `AttributeTypes.xml` (18,489 lines), `DefaultTrapAttributeTypes.xml` (400–409 lines depending on version), `DefaultTrapProcessingPlan.xml` (621–636 lines), `TrapVarbindParser.xml`, `EventAttributeTypes.xml`, `GRTEntries.xml`.
- Sandbox larger captures: `sandbox/AttributeTypes_05_24.xml` (18,379 lines), `sandbox/SyslogTemplates_05_20.xml` (39,495 lines), `sandbox/SyslogTemplatesJava_05_20.xml` (39,519 lines).
- Hidden as `.txt`: `HP_ATTRIBUTETYPE.txt` (18,441 lines), `HP_EXPLANATION.txt` (7,893), `HP_RECACTION.txt` (3,452), `HP_SYSLOGTYPE.txt`, `HP_SYSLOGTYPECRITERIA.txt`, `HP_SYSLOGTYPECRITERIALIST.txt` — HP OpenView-format dumps, appears to be heritage data.

## 8. Real-Time Update Mechanism

The repo has **three** plausible mechanisms for live UI updates. No single WebSocket endpoint screams "alarms table stream" by name, but the pieces are:

**WebSocket-based notifications (policy-driven, likely server-push for subscribed destinations).**
- `model/fault_policy_model/.../NotificationWebSocket.java` (113 lines) — model class for WebSocket notification-contact destinations.
- `fault_policy/fault_policy_impl/.../NotificationWebSocketConfigServiceImpl.java` (145 lines).
- `fault_policy/fault_policy_rest/.../NotificationWebSocketResource.java` (241 lines).
- `fault_policy/fault_policy_notification/.../AlarmPolicyBuiltinsForWebSocketContacts.java` (149 lines).
- `fault_policy_ui/.../applications/NotificationPolicies/WebSocketDestinationForm.html` + `WebSocketDestinationForm.js`.
- Note: this is the "send alarms to a registered WebSocket subscriber" feature. Whether the classic UI alarms table uses the same plumbing is not discoverable from the tree alone.

**JMS / topic-based in-process messaging.**
- `ifm_fault_message/src/main/java/com/cisco/ifm/fault/message/IfmFaultMessageSubscriber.java`, `IfmFaultTopicListener.java` — Spring/JMS subscriber pattern.
- `ifm_fault_message/src/main/java/com/cisco/ifm/fault/syslog/SyslogPersistor.java` (196 lines), `SyslogQueue.java`, `PersistSyslogHelper.java`, `BatchPersistenceHelper.java`.

**Listener / observable registry (in-JVM push).**
- `ncs_common/.../listener/BaseQueuingListener.java` (182 lines), `QueuingAlarmNEventListener.java`, `QueuingAlertListener.java`.
- `decap.event/.../alarmCache/impl/AlarmWriteBehindThread.java` — async write-behind; implies a queue-driven update pathway.
- `ncs_eventAlarm/.../cache/syslog/dedupe/LiveSyslogSender.java` + `LiveSyslogCache.java` — live/streaming syslog path.
- `ncs_eventAlarm/.../group/GroupChangeListener.java`, `GroupChangeManager.java`, `GroupChangedTask.java`, `GroupChangedTaskCallback.java`.

**Polling infrastructure (SNMP, not UI).** `xmp_poller/` is heavy SNMP polling code (`AsyncPoll.java`, `AsyncPollTask.java` 660 lines, `AsyncPollUnit.java`, `DeviceImpl.java`, `Macro.java`) — serves performance management, not the alarm table.

**Circular-buffer IPC (C++ → Java event feed).** `decap_core_java/` contains a heavy `circularBuffer/` package with `SegCircularBuffer`, `ProxyRegistry`, `CircularBufferMonitorThread`, `ThreadSafeCircularBufferOutputObjectReader/Writer`, `VPerfCircularBufferOutputObjectReader/Writer`. The C++ daemon writes records; Java readers mmap-read them. `Decap_core/include/util/AbstractCircularBuffer.h` (1,135 lines) / `.cpp` (3,086 lines) is the native side. This is the raw ingest pipeline (traps/syslogs enter Java through this) — not the UI-push mechanism per se.

## 9. Build / Packaging Indicators

- Top-level: `pom.xml` (147 lines), `pom_parent.xml`, `pom_testing.xml`, `Jenkinsfile` (127 lines), `buildAndPatch.sh` (314 lines), `components.txt` (17 lines), `master_components.txt` (12 lines), `sonar-project.properties`, `sonar_scan.sh` (62 lines), `settings-lumos-group.xml`, `settings-rel.xml`, `xmpcomp-settings-rel.xml`, `xmpcomp-settings.xml`, `MVN_ENFORCER_SKIP.txt`, `.gitignore` (12 lines), `README.md` (100 lines).
- Module-level: every module has `pom.xml` + `PMDRules_Selected.xml` + usually `suite.xml` (TestNG) and `settings-rel.xml`. Many have `MVN_ENFORCER_SKIP.txt`.
- Assembly: `epnm_tp/assembly/assembly.xml` (474 lines), `epnm_tp/pom.xml`, `fault_policy_ui/assembly.xml`, `ifm_fault_message/assembly.xml`, `ifm_trapnotification_ui/assembly.xml`.
- C++ builds: per-subproject `.cproject` files (Eclipse CDT), `cproject-linux`, `cproject-solaris`, `makefile`, `objects.mk`, `sources.mk`, `subdir.mk` in `Debug-linux/` and `Debug-solaris/` dirs. Shell build scripts under `CPP/Decap_build/`: `buildDecap-common.bash`, `buildDecap-linux.bash`, `buildDecap-solaris.bash`, `SourceCommonBuildEnvBase.bash`, `SourceLinux64BuildEnv.bash`, etc. Dual-platform (Linux and Solaris) is baked in.
- Release poms: many subprojects carry `release-pom.xml.save` and `pom_epnm_old.xml` as historical artifacts (indicates merge history).
- OSGi: several modules declare `MANIFEST.MF` + `osgi-context.xml` (e.g., `ifm_alarm_adapter/`, `ifm_alarm_service/`), implying Karaf/OSGi deployment for the service tier.

## 10. POC-Critical Paths Summary

These are the paths the execution session will most want to open first when recreating the alarms table, its correlated-alarm group expansion, clear-action, events popup, and syslog page:

1. **`fault/ifm_fault/ifm_alarm_rest_provider/src/main/java/com/cisco/ifm/alarmrest/AlarmRest.java`** — 7,969 lines. The master REST layer. Almost certainly contains the endpoint(s) the classic alarms table calls (list, detail, correlated, clear, annotate).
2. **`fault/ifm_fault/ifm_alarm_service/src/main/java/com/cisco/ifm/alarmservice/impl/AlarmServiceImpl.java`** — 5,075 lines. Core alarm business logic behind the REST layer.
3. **`fault/ifm_fault/ifm_base_dto/src/main/java/com/cisco/ifm/base/dto/alarm/AlarmDTO.java`** — 547 lines. The wire shape for a single alarm row. Plus `EventDTO.java`, `SyslogDTO.java`, `AlarmNoteDTO.java`, `AlarmRelatedHistoryDTO.java`, `GroupedAlarmDTO.java`, `GroupedAlarmEventDTO.java`, `AlarmSeverityStatsDTO.java` in the same package.
4. **`fault/ncs_eventAlarm/src/main/java/com/cisco/ncs/eventAlarm/cache/alarm/SortedAlarmCache.java`** — 1,057 lines. The in-memory, sorted, filtered cache that backs the alarms-list table and its correlation grouping. Plus siblings `AlarmCountCache.java`, `SortedCacheBase.java`, `filters/CorrelatedFilter.java`, `filters/ClearedFilter.java`, `filters/CategoryFilter.java`.
5. **`fault/ncs_eventAlarm/src/main/java/com/cisco/ncs/eventAlarm/cache/event/SortedEventCache.java`** — 579 lines. Backs the events list and the past-N-hours popup.
6. **`fault/ncs_eventAlarm/src/main/java/com/cisco/ncs/eventAlarm/cache/syslog/SortedSyslogCache.java`** — 577 lines. Backs the syslogs page.
7. **`fault/ifm_fault/ifm_alarm_service/src/main/java/com/cisco/ifm/alarmservice/services/queries/alarm/`** (directory) — the query abstractions (`AlarmListQuery`, `AlarmSummaryQuery`, `AlarmCountsBy*Query`, `MostRecentNotesForAlarmsQuery`) the session will want to map to new endpoints. Plus the sibling `filter/` package (`SimpleFilterExpression`, `LogicalFilterExpression`, `Between`, `Contains`, `StartsWith`, `Range`, etc.) which is the classic-table's filter-expression contract.
8. **`fault/ifm_fault/ifm_alarm_adapter/src/main/java/com/cisco/ifm/rest/adapter/AlarmRestAdapterImpl.java`** — 489 lines. Adapter between REST and alarm service, plus `IAlarmRestAdapter.java` (219 lines) and `dtobuilder/AlarmDtoBuilder.java` (568 lines) / `WiredWirelessAlarmDtoBuilder.java`.
9. **`fault/decap.event/src/main/java/com/cisco/xmp/decap/event/alarmCache/impl/AlarmCacheImpl.java`** — 1,359 lines. The deeper in-process alarm cache, correlation-alarm storage handler, lock handler. Needed for understanding how correlation updates back-propagate.
10. **`fault/ncs_eventAlarm/src/main/java/com/cisco/ncs/eventAlarm/impl/NmsEventToNmsAlertCorrelator.java`** — 462 lines. How an incoming event becomes an alarm / updates an existing one — the core of "correlated alarm groupings" behavior.

Secondary-but-high-value (real-time and UI contract):
- **`fault/fault_policy/fault_policy_rest/src/main/java/com/cisco/xmp/fault/policy/rest/NotificationWebSocketResource.java`** + `fault/model/fault_policy_model/src/com/cisco/xmp/fault/policy/model/NotificationWebSocket.java` — WebSocket plumbing.
- **`fault/ifm_trapnotification_ui/src/main/webapp/applications/trapnotification/data/trapTableColumnStructure.json`** — a concrete Dojo column-schema template the new UI can mirror.
- **`fault/ifm_fault/ifm_alarm_service/src/main/java/com/cisco/ifm/alarmservice/services/queries/syslog/SyslogListQuery.java`** — 310 lines. Syslog list backing query.
- **`fault/ifm_fault/ifm_alarm_rest_provider/src/main/java/com/cisco/ifm/alarmrest/services/EventRestService.java`** (605 lines) and `SyslogRestService.java` (429 lines) — events/syslog REST endpoints.
