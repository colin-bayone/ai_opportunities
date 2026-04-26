# Repository Tree Report: inventory

- Repository root: `/Users/cmoore/Documents/programming/EPNM/inventory/inventory`
- Included text-like files: `2561`
- Included directories: `636`
- Total raw lines: `1420340`
- Skipped binary files: `76`
- Skipped ignored-extension files: `33`

```text
inventory/
├── comp/
│   ├── ifm_devices_supported/
│   │   ├── .settings/
│   │   │   ├── org.eclipse.core.resources.prefs (5 lines)
│   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           └── ifm/
│   │   │   │   │               └── devpkg/
│   │   │   │   │                   ├── model/
│   │   │   │   │                   │   ├── AdvancedFilterOperation.java (74 lines)
│   │   │   │   │                   │   ├── DeviceDetails.java (261 lines)
│   │   │   │   │                   │   ├── DeviceSeriesDetails.java (153 lines)
│   │   │   │   │                   │   ├── DevicesPaging.java (80 lines)
│   │   │   │   │                   │   ├── Family.java (127 lines)
│   │   │   │   │                   │   ├── FilterParameter.java (137 lines)
│   │   │   │   │                   │   ├── NameValuePair.java (49 lines)
│   │   │   │   │                   │   ├── NameValuePairListPaging.java (76 lines)
│   │   │   │   │                   │   ├── ObjectFactory.java (35 lines)
│   │   │   │   │                   │   ├── ObjectSelector.java (150 lines)
│   │   │   │   │                   │   ├── Series.java (160 lines)
│   │   │   │   │                   │   └── TreeTable.java (301 lines)
│   │   │   │   │                   ├── rest/
│   │   │   │   │                   │   ├── DPRestService.java (915 lines)
│   │   │   │   │                   │   └── IDPRestService.java (151 lines)
│   │   │   │   │                   ├── DPSLogService.java (22 lines)
│   │   │   │   │                   ├── DevicePackageCoverageService.java (934 lines)
│   │   │   │   │                   └── DeviceSupportService.java (2172 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   ├── spring/
│   │   │   │       │   │   └── ifm-devicessupported-context.xml (41 lines)
│   │   │   │       │   └── aop.xml (19 lines)
│   │   │   │       ├── com/
│   │   │   │       │   └── cisco/
│   │   │   │       │       └── ifm/
│   │   │   │       │           ├── features/
│   │   │   │       │           │   ├── SoftwareCustomMapping.properties (1 lines)
│   │   │   │       │           │   ├── featureMapping.properties (149 lines)
│   │   │   │       │           │   ├── hiddenMapping.properties (162 lines)
│   │   │   │       │           │   └── protocolMapping.properties (56 lines)
│   │   │   │       │           └── mesg/
│   │   │   │       │               ├── messages.properties (2 lines)
│   │   │   │       │               └── messages.xml (36 lines)
│   │   │   │       └── log4j/
│   │   │   │           ├── dps-categories.xml (13 lines)
│   │   │   │           └── dps_log4j.xml (28 lines)
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   ├── com/
│   │   │       │   │   └── cisco/
│   │   │       │   │       └── ifm/
│   │   │       │   │           └── devpkg/
│   │   │       │   │               ├── model/
│   │   │       │   │               │   └── UnitTest.java (393 lines)
│   │   │       │   │               ├── rest/
│   │   │       │   │               │   └── DPRestServiceTest.java (605 lines)
│   │   │       │   │               ├── DevicePackageCoverageServiceTest.java (469 lines)
│   │   │       │   │               ├── DeviceSupportServiceTest.java (1366 lines)
│   │   │       │   │               └── UnitTest.java (83 lines)
│   │   │       │   └── ifm_devices_supported/
│   │   │       │       └── UnitTest.java (126 lines)
│   │   │       └── resources/
│   │   │           └── conf/
│   │   │               └── ifm/
│   │   │                   └── DevicePackageCoverage.html (4 lines)
│   │   ├── .classpath (31 lines)
│   │   ├── .project (23 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── merge_0210_2014.txt (11 lines)
│   │   ├── merge_12_08.txt (90 lines)
│   │   ├── pom.xml (369 lines)
│   │   └── release-pom.xml.save (1346 lines)
│   ├── ifm_discovery_model/
│   │   └── .project (36 lines)
│   ├── ifm_event_inventory_service/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           ├── ifm/
│   │   │   │   │           │   ├── eventactions/
│   │   │   │   │           │   │   ├── action/
│   │   │   │   │           │   │   │   ├── BurstEventHolder.java (47 lines)
│   │   │   │   │           │   │   │   ├── ContiniousEventHolder.java (97 lines)
│   │   │   │   │           │   │   │   ├── ContinuousHolderMonitor.java (493 lines)
│   │   │   │   │           │   │   │   ├── EventRateDetectionHolder.java (95 lines)
│   │   │   │   │           │   │   │   ├── EventRateHolderInterface.java (5 lines)
│   │   │   │   │           │   │   │   ├── EventRateHolderType.java (5 lines)
│   │   │   │   │           │   │   │   └── GIDisabledStatusMonitor.java (700 lines)
│   │   │   │   │           │   │   ├── metadata/
│   │   │   │   │           │   │   │   └── EventRateFCMetaData.java (118 lines)
│   │   │   │   │           │   │   ├── util/
│   │   │   │   │           │   │   │   ├── EventRateActionType.java (10 lines)
│   │   │   │   │           │   │   │   ├── FlowControllerUtil.java (380 lines)
│   │   │   │   │           │   │   │   └── SystemEventPublisher.java (158 lines)
│   │   │   │   │           │   │   ├── BurstEventsFlowController.java (1128 lines)
│   │   │   │   │           │   │   ├── CompositeEventsFlowController.java (206 lines)
│   │   │   │   │           │   │   ├── ContinousEventsFlowController.java (612 lines)
│   │   │   │   │           │   │   └── FeatureSyncEventsFlowController.java (248 lines)
│   │   │   │   │           │   ├── eventbasedinventory/
│   │   │   │   │           │   │   ├── AbstractInventoryRuleAction.java (189 lines)
│   │   │   │   │           │   │   ├── ArchivelogExecutor.java (475 lines)
│   │   │   │   │           │   │   ├── BaseOpticalConfigChangeProcessor.java (315 lines)
│   │   │   │   │           │   │   ├── BeanUtility.java (26 lines)
│   │   │   │   │           │   │   ├── CustomizedGranularInventoryPolicy.java (751 lines)
│   │   │   │   │           │   │   ├── DeviceReachabilityRuleAction.java (304 lines)
│   │   │   │   │           │   │   ├── EventBasedAdminSettingsListener.java (250 lines)
│   │   │   │   │           │   │   ├── EventBasedArchiveIdCache.java (136 lines)
│   │   │   │   │           │   │   ├── ExpediteInventoryProcessor.java (119 lines)
│   │   │   │   │           │   │   ├── GranularInventoryAdapter.java (145 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueue.java (133 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueueExecutor.java (301 lines)
│   │   │   │   │           │   │   ├── GranularInventoryRuleAction.java (262 lines)
│   │   │   │   │           │   │   ├── InterfaceConfigChangeProcessor.java (740 lines)
│   │   │   │   │           │   │   ├── InvCollectionNotifierQueueImpl.java (44 lines)
│   │   │   │   │           │   │   ├── InventoryConfigChangeProcessor.java (279 lines)
│   │   │   │   │           │   │   ├── InventorySyslogProcessor.java (907 lines)
│   │   │   │   │           │   │   ├── InventorySyslogRuleAction.java (576 lines)
│   │   │   │   │           │   │   ├── OpticalConfigChangePostProcessor.java (19 lines)
│   │   │   │   │           │   │   ├── PhysicalPepChangeProcessor.java (143 lines)
│   │   │   │   │           │   │   └── StaticRouteConfigChangeProcessor.java (110 lines)
│   │   │   │   │           │   ├── invhelper/
│   │   │   │   │           │   │   ├── InventoryDBUtil.java (206 lines)
│   │   │   │   │           │   │   ├── InventoryMCNHelper.java (110 lines)
│   │   │   │   │           │   │   └── InventoryServiceHelper.java (1029 lines)
│   │   │   │   │           │   ├── postInitHook/
│   │   │   │   │           │   │   ├── IFMPostInitHookImpl.java (67 lines)
│   │   │   │   │           │   │   └── OpticalInvModelObjectExtractor.java (230 lines)
│   │   │   │   │           │   └── syncofflineprefimpl/
│   │   │   │   │           │       └── SyncOfflineDevicePrefImpl.java (150 lines)
│   │   │   │   │           └── nms/
│   │   │   │   │               ├── ce/
│   │   │   │   │               │   └── event/
│   │   │   │   │               │       └── correlation/
│   │   │   │   │               │           └── DuplicateEventsFlowController.java (91 lines)
│   │   │   │   │               └── optical/
│   │   │   │   │                   └── event/
│   │   │   │   │                       └── correlation/
│   │   │   │   │                           └── PrioritizedEventsFlowController.java (114 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   ├── spring/
│   │   │   │       │   │   └── ifm_event_inventory_service_context.xml (90 lines)
│   │   │   │       │   └── MANIFEST.MF (70 lines)
│   │   │   │       └── com/
│   │   │   │           └── cisco/
│   │   │   │               └── ifm/
│   │   │   │                   └── inventoryservice/
│   │   │   │                       └── logging/
│   │   │   │                           ├── InventoryServiceMessages.properties (157 lines)
│   │   │   │                           └── InventoryServiceMessages.xml (842 lines)
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           ├── ifm/
│   │   │       │           │   ├── eventactions/
│   │   │       │           │   │   ├── action/
│   │   │       │           │   │   │   ├── BurstEventHolderTest.java (41 lines)
│   │   │       │           │   │   │   ├── ContinuousHolderMonitorTest.java (276 lines)
│   │   │       │           │   │   │   └── EventRateDetectionHolderTest.java (73 lines)
│   │   │       │           │   │   ├── metadata/
│   │   │       │           │   │   │   └── EventRateFCMetaDataTest.java (96 lines)
│   │   │       │           │   │   ├── util/
│   │   │       │           │   │   │   ├── FlowControllerUtilTest.java (485 lines)
│   │   │       │           │   │   │   └── SystemEventPublisherTest.java (123 lines)
│   │   │       │           │   │   ├── BurstEventsFlowControllerTest.java (839 lines)
│   │   │       │           │   │   ├── CompositeEventsFlowControllerTest.java (207 lines)
│   │   │       │           │   │   ├── ContinousEventsFlowControllerTest.java (384 lines)
│   │   │       │           │   │   └── FeatureSyncEventsFlowControllerTest.java (209 lines)
│   │   │       │           │   ├── eventbasedinventory/
│   │   │       │           │   │   ├── AbstractInventoryRuleActionTest.java (205 lines)
│   │   │       │           │   │   ├── ArchivelogExecutorTest.java (497 lines)
│   │   │       │           │   │   ├── BaseOpticalConfigChangeProcessorTest.java (365 lines)
│   │   │       │           │   │   ├── BurstEventsFlowControllerTest.java (798 lines)
│   │   │       │           │   │   ├── CustomizedGranularInventoryPolicyTest.java (410 lines)
│   │   │       │           │   │   ├── DeviceReachabilityRuleActionTest.java (434 lines)
│   │   │       │           │   │   ├── EventBasedAdminSettingsListenerTest.java (111 lines)
│   │   │       │           │   │   ├── EventBasedArchiveIdCacheTest.java (271 lines)
│   │   │       │           │   │   ├── GranularInventoryQueueExecutorTest.java (111 lines)
│   │   │       │           │   │   ├── GranularInventoryQueueTest.java (582 lines)
│   │   │       │           │   │   ├── GranularInventoryRuleActionTest.java (501 lines)
│   │   │       │           │   │   ├── InterfaceConfigChangeProcessorTest.java (697 lines)
│   │   │       │           │   │   ├── InventoryConfigChangeProcessorTest.java (137 lines)
│   │   │       │           │   │   ├── InventorySyslogProcessorJTest.java (716 lines)
│   │   │       │           │   │   ├── InventorySyslogProcessorTest.java (305 lines)
│   │   │       │           │   │   ├── InventorySyslogRuleActionTest.java (863 lines)
│   │   │       │           │   │   └── PhysicalPepChangeProcessorTest.java (110 lines)
│   │   │       │           │   ├── invhelper/
│   │   │       │           │   │   ├── InventoryDBUtilTest.java (238 lines)
│   │   │       │           │   │   ├── InventoryMCNHelperTest.java (139 lines)
│   │   │       │           │   │   └── InventoryServiceHelperTest.java (1297 lines)
│   │   │       │           │   ├── postInitHook/
│   │   │       │           │   │   ├── IFMPostInitHookImplTest.java (78 lines)
│   │   │       │           │   │   └── OpticalInvModelObjectExtractorTest.java (452 lines)
│   │   │       │           │   ├── syncofflineprefimpl/
│   │   │       │           │   │   └── SyncOfflineDevicePrefImplTest.java (43 lines)
│   │   │       │           │   └── util/
│   │   │       │           │       ├── MessageSourceMock.java (31 lines)
│   │   │       │           │       └── TempLogger.java (2305 lines)
│   │   │       │           └── nms/
│   │   │       │               ├── ce/
│   │   │       │               │   └── event/
│   │   │       │               │       └── correlation/
│   │   │       │               │           └── DuplicateEventsFlowControllerTest.java (130 lines)
│   │   │       │               └── optical/
│   │   │       │                   └── event/
│   │   │       │                       └── correlation/
│   │   │       │                           └── PrioritizedEventsFlowControllerTest.java (161 lines)
│   │   │       └── resources/
│   │   │           ├── META-INF/
│   │   │           │   └── spring/
│   │   │           │       └── LoggerTest-context.xml (23 lines)
│   │   │           ├── testdatafiles/
│   │   │           │   └── inventory_devices.xml (58 lines)
│   │   │           ├── DeviceTestSuite.xml (22 lines)
│   │   │           ├── EventPatternExample.xml (45 lines)
│   │   │           └── testbed.xml (15 lines)
│   │   ├── .gitignore (5 lines)
│   │   └── pom.xml (1786 lines)
│   ├── ifm_inventory_rest_provider/
│   │   ├── .settings/
│   │   │   └── org.eclipse.jdt.core.prefs (5 lines)
│   │   ├── logs/
│   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           └── ifm/
│   │   │   │   │               ├── inventoryrestservice/
│   │   │   │   │               │   ├── dto/
│   │   │   │   │               │   │   ├── CDPNeighborDTO.java (427 lines)
│   │   │   │   │               │   │   ├── CDPNeighborDTO360.java (117 lines)
│   │   │   │   │               │   │   ├── Device.java (211 lines)
│   │   │   │   │               │   │   ├── DeviceCollectionState.java (311 lines)
│   │   │   │   │               │   │   ├── DeviceDTO.java (921 lines)
│   │   │   │   │               │   │   ├── DeviceDetailsDTO.java (205 lines)
│   │   │   │   │               │   │   ├── DeviceExceptionDTO.java (64 lines)
│   │   │   │   │               │   │   ├── DeviceExceptionGridDTO.java (114 lines)
│   │   │   │   │               │   │   ├── DeviceInventory.java (154 lines)
│   │   │   │   │               │   │   ├── DeviceList.java (83 lines)
│   │   │   │   │               │   │   ├── DeviceLocationDTO.java (151 lines)
│   │   │   │   │               │   │   ├── DeviceMaintenanceStateDTO.java (69 lines)
│   │   │   │   │               │   │   ├── DevicesAttributesDTO.java (144 lines)
│   │   │   │   │               │   │   ├── DevicesDTO.java (71 lines)
│   │   │   │   │               │   │   ├── DevicesNodeDTO.java (122 lines)
│   │   │   │   │               │   │   ├── DevicesRootDTO.java (60 lines)
│   │   │   │   │               │   │   ├── Erspan.java (72 lines)
│   │   │   │   │               │   │   ├── InterfaceDTO.java (336 lines)
│   │   │   │   │               │   │   ├── LLDPNeighborDTO.java (427 lines)
│   │   │   │   │               │   │   ├── LLDPNeighborDTO360.java (107 lines)
│   │   │   │   │               │   │   ├── LocationDTO.java (208 lines)
│   │   │   │   │               │   │   ├── LocationNmspDTO.java (516 lines)
│   │   │   │   │               │   │   ├── ManagedNetworkElementsChild.java (25 lines)
│   │   │   │   │               │   │   ├── ModuleDTO.java (576 lines)
│   │   │   │   │               │   │   ├── Nbar.java (72 lines)
│   │   │   │   │               │   │   ├── Netflow.java (97 lines)
│   │   │   │   │               │   │   ├── ObjectFactory.java (146 lines)
│   │   │   │   │               │   │   ├── RootNodeDTO.java (61 lines)
│   │   │   │   │               │   │   ├── Rspan.java (72 lines)
│   │   │   │   │               │   │   ├── ScheduleDeviceMaintenanceJobDTO.java (55 lines)
│   │   │   │   │               │   │   ├── ScheduledDevicesMaintenanceManagedJobDTO.java (26 lines)
│   │   │   │   │               │   │   ├── ScheduledDevicesMaintenanceManagedJobList.java (134 lines)
│   │   │   │   │               │   │   ├── SearchResultsDTO.java (37 lines)
│   │   │   │   │               │   │   ├── Span.java (72 lines)
│   │   │   │   │               │   │   ├── SubLocationNodeDTO.java (156 lines)
│   │   │   │   │               │   │   ├── SubLocationsDTO.java (70 lines)
│   │   │   │   │               │   │   ├── UserHeaderDTO.java (93 lines)
│   │   │   │   │               │   │   ├── VPCConsistencyDTO.java (83 lines)
│   │   │   │   │               │   │   ├── VPCConsistencyViewDTO.java (136 lines)
│   │   │   │   │               │   │   ├── VPCFullDuplex.java (135 lines)
│   │   │   │   │               │   │   ├── VPCHalfDuplex.java (107 lines)
│   │   │   │   │               │   │   ├── VdcDetailDTO.java (105 lines)
│   │   │   │   │               │   │   ├── VdcDetailManagedDTO.java (137 lines)
│   │   │   │   │               │   │   ├── VdcDetailResourceSummaryDTO.java (121 lines)
│   │   │   │   │               │   │   ├── VdcDetailResourcesDTO.java (91 lines)
│   │   │   │   │               │   │   ├── VdcDetailSummaryDTO.java (237 lines)
│   │   │   │   │               │   │   ├── Versions.java (83 lines)
│   │   │   │   │               │   │   ├── VirtualDomainDTO360.java (27 lines)
│   │   │   │   │               │   │   ├── VrfListDTO.java (24 lines)
│   │   │   │   │               │   │   ├── VrfNameDTO.java (19 lines)
│   │   │   │   │               │   │   ├── passPromptDTO.java (45 lines)
│   │   │   │   │               │   │   ├── passPromptListDTO.java (25 lines)
│   │   │   │   │               │   │   └── udfDTO.java (40 lines)
│   │   │   │   │               │   ├── ExportDeviceDBUtil.java (1424 lines)
│   │   │   │   │               │   ├── ExportDeviceUtil.java (1899 lines)
│   │   │   │   │               │   ├── InventoryDTOBuilder.java (3269 lines)
│   │   │   │   │               │   ├── InventoryRestService.java (8770 lines)
│   │   │   │   │               │   ├── InventoryRestUtil.java (584 lines)
│   │   │   │   │               │   ├── PaginationUtil.java (183 lines)
│   │   │   │   │               │   └── SortCriteriaUtil.java (93 lines)
│   │   │   │   │               ├── inventoryservice/
│   │   │   │   │               │   ├── dnac/
│   │   │   │   │               │   │   ├── DeviceAndActionToBeTaken.java (52 lines)
│   │   │   │   │               │   │   ├── SAXHandler.java (60 lines)
│   │   │   │   │               │   │   └── SpecialDevice.java (45 lines)
│   │   │   │   │               │   └── util/
│   │   │   │   │               │       ├── VDCDetailConstants.java (46 lines)
│   │   │   │   │               │       └── VPCConstants.java (33 lines)
│   │   │   │   │               ├── service/
│   │   │   │   │               │   └── rest/
│   │   │   │   │               │       └── syncoffline/
│   │   │   │   │               │           ├── SyncOfflineDeviceDTO.java (62 lines)
│   │   │   │   │               │           └── SyncOfflineDeviceRestService.java (181 lines)
│   │   │   │   │               ├── udfconf/
│   │   │   │   │               │   └── dto/
│   │   │   │   │               │       ├── BulkImportDTO.java (94 lines)
│   │   │   │   │               │       ├── BulkImportListDTO.java (150 lines)
│   │   │   │   │               │       ├── DeviceOperationStatusDTO.java (54 lines)
│   │   │   │   │               │       └── UdfDTO.java (127 lines)
│   │   │   │   │               └── udfconfigrestservice/
│   │   │   │   │                   ├── UdfDTOBuilder.java (76 lines)
│   │   │   │   │                   └── UdfRestService.java (596 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── com/
│   │   │   │       │   └── cisco/
│   │   │   │       │       └── ifm/
│   │   │   │       │           └── inventoryrestservice/
│   │   │   │       │               ├── dnacDeviceFilter/
│   │   │   │       │               │   └── SpecialDevices.xml (13 lines)
│   │   │   │       │               └── dto/
│   │   │   │       │                   ├── InventoryCollectionStates.xml (148 lines)
│   │   │   │       │                   └── jaxb.index (15 lines)
│   │   │   │       └── nbi-sec/
│   │   │   │           └── DeviceDetailPrivileges/
│   │   │   │               ├── DeviceDetailPrivileges.xml (678 lines)
│   │   │   │               └── SecurityContribution.xsd (75 lines)
│   │   │   ├── site/
│   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           ├── ifm/
│   │   │       │           │   ├── inventoryrestservice/
│   │   │       │           │   │   ├── dto/
│   │   │       │           │   │   │   ├── DeviceCollectionStateTest.java (153 lines)
│   │   │       │           │   │   │   └── DeviceDtoTest.java (108 lines)
│   │   │       │           │   │   ├── ExportDeviceDBUtilTest.java (837 lines)
│   │   │       │           │   │   ├── ExportDeviceUtilTest.java (513 lines)
│   │   │       │           │   │   ├── ExportDeviceUtilTestExisting.java (590 lines)
│   │   │       │           │   │   ├── InventoryDTOBuilderJTest.java (2466 lines)
│   │   │       │           │   │   ├── InventoryDTOBuilderTest.java (360 lines)
│   │   │       │           │   │   ├── InventoryRestServiceTest.java (6801 lines)
│   │   │       │           │   │   ├── InventoryRestServiceTestExisting.java (5482 lines)
│   │   │       │           │   │   ├── InventoryRestUtilTest.java (466 lines)
│   │   │       │           │   │   ├── InventoryRestUtilTestExisting.java (87 lines)
│   │   │       │           │   │   ├── PaginationUtilTest.java (79 lines)
│   │   │       │           │   │   ├── SortCriteriaUtilTest.java (30 lines)
│   │   │       │           │   │   ├── TestInventoryRestDto.java (162 lines)
│   │   │       │           │   │   └── TestInventoryService.java (1446 lines)
│   │   │       │           │   ├── inventoryservice/
│   │   │       │           │   │   └── dnac/
│   │   │       │           │   │       └── DeviceAndActionToBeTakenTest.java (117 lines)
│   │   │       │           │   ├── service/
│   │   │       │           │   │   └── rest/
│   │   │       │           │   │       └── syncoffline/
│   │   │       │           │   │           ├── SyncOfflineDeviceDTOTest.java (24 lines)
│   │   │       │           │   │           └── SyncOfflineDeviceRestServiceTest.java (239 lines)
│   │   │       │           │   └── udfconfigrestservice/
│   │   │       │           │       ├── UdfDTOBuilderTest.java (43 lines)
│   │   │       │           │       ├── UdfRestServiceTest.java (443 lines)
│   │   │       │           │       └── UdfRestServiceTestExisting.java (140 lines)
│   │   │       │           └── randoop/
│   │   │       │               └── gen/
│   │   │       │                   └── tests/
│   │   │       │                       ├── RegressionTest.java (9 lines)
│   │   │       │                       ├── RegressionTest0.java (7954 lines)
│   │   │       │                       ├── RegressionTest1.java (8693 lines)
│   │   │       │                       └── RegressionTest2.java (5120 lines)
│   │   │       └── resources/
│   │   │           ├── dnacDeviceFilter/
│   │   │           │   └── SpecialDevices.xml (30 lines)
│   │   │           └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   ├── test-output/
│   │   │   └── ifm_inventory_rest_provider/
│   │   │       ├── classes.html (32 lines)
│   │   │       ├── com.cisco.ifm.inventoryrestservice.InventoryRestServiceTest.html (116 lines)
│   │   │       ├── com.cisco.ifm.inventoryrestservice.InventoryRestServiceTest.properties (1 lines)
│   │   │       ├── com.cisco.ifm.inventoryrestservice.InventoryRestServiceTest.xml (11 lines)
│   │   │       ├── groups.html (1 lines)
│   │   │       ├── index.html (6 lines)
│   │   │       ├── main.html (2 lines)
│   │   │       ├── methods-alphabetical.html (10 lines)
│   │   │       ├── methods-not-run.html (2 lines)
│   │   │       ├── methods.html (10 lines)
│   │   │       ├── reporter-output.html (1 lines)
│   │   │       ├── testng-failed.xml (14 lines)
│   │   │       ├── testng.xml.html (1 lines)
│   │   │       └── toc.html (30 lines)
│   │   ├── .classpath (40 lines)
│   │   ├── .gitignore (3 lines)
│   │   ├── .project (25 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── build.xml (45 lines)
│   │   ├── jtestsettings.properties (43 lines)
│   │   ├── merge_0210_2014.txt (29 lines)
│   │   ├── merge_12_08.txt (7 lines)
│   │   ├── pom.xml (1568 lines)
│   │   └── release-pom.xml.save (3221 lines)
│   ├── ifm_inventory_service/
│   │   ├── docs/
│   │   │   ├── src/
│   │   │   │   └── docbkx/
│   │   │   │       ├── Inventory_service.xpr (15 lines)
│   │   │   │       ├── book-ifm-inventory-service-ug.xml (23 lines)
│   │   │   │       ├── chapter-getting-started.xml (13 lines)
│   │   │   │       ├── chapter-inventory.xml (823 lines)
│   │   │   │       ├── chapter-overview.xml (14 lines)
│   │   │   │       └── chapter-references.xml (14 lines)
│   │   │   └── pom.xml (71 lines)
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           ├── ifm/
│   │   │   │   │           │   ├── aspects/
│   │   │   │   │           │   │   ├── AuditInventoryAfterAspect.java (160 lines)
│   │   │   │   │           │   │   ├── AuditInventoryAroundAspect.java (478 lines)
│   │   │   │   │           │   │   └── AuditInventoryAspect.java (298 lines)
│   │   │   │   │           │   ├── converter/
│   │   │   │   │           │   │   ├── AddressToLocationNioWrapperConverter.java (23 lines)
│   │   │   │   │           │   │   └── DeviceToNetworkDeviceNioWrapperConverter.java (118 lines)
│   │   │   │   │           │   ├── deletehandler/
│   │   │   │   │           │   │   └── dto/
│   │   │   │   │           │   │       └── DeviceServicesCount.java (82 lines)
│   │   │   │   │           │   ├── deviceinventory/
│   │   │   │   │           │   │   ├── DeviceInventoryRequestHandler.java (1145 lines)
│   │   │   │   │           │   │   ├── EMSInterfaceInventoryRequestHandler.java (305 lines)
│   │   │   │   │           │   │   └── SQLQueryConstants.java (193 lines)
│   │   │   │   │           │   ├── dlm/
│   │   │   │   │           │   │   ├── DlmDataServiceImpl.java (1266 lines)
│   │   │   │   │           │   │   └── DlmDataServiceValidator.java (300 lines)
│   │   │   │   │           │   ├── eventbasedinventory/
│   │   │   │   │           │   │   ├── ArchivelogExecutor.java (442 lines)
│   │   │   │   │           │   │   ├── BeanUtility.java (43 lines)
│   │   │   │   │           │   │   ├── CustomizedGranularInventoryPolicy.java (719 lines)
│   │   │   │   │           │   │   ├── DeviceReachabilityRuleAction.java (376 lines)
│   │   │   │   │           │   │   ├── EventBasedAdminSettingsListener.java (245 lines)
│   │   │   │   │           │   │   ├── EventBasedArchiveIdCache.java (136 lines)
│   │   │   │   │           │   │   ├── ExpediteInventoryProcessor.java (110 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueue.java (72 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueueExecutor.java (276 lines)
│   │   │   │   │           │   │   ├── GranularInventoryRuleAction.java (262 lines)
│   │   │   │   │           │   │   ├── InterfaceConfigChangeProcessor.java (417 lines)
│   │   │   │   │           │   │   ├── InvCollectionNotifierQueueImpl.java (34 lines)
│   │   │   │   │           │   │   ├── InventoryConfigChangeProcessor.java (278 lines)
│   │   │   │   │           │   │   ├── InventorySyslogProcessor.java (773 lines)
│   │   │   │   │           │   │   ├── InventorySyslogRuleAction.java (558 lines)
│   │   │   │   │           │   │   ├── PhysicalPepChangeProcessor.java (143 lines)
│   │   │   │   │           │   │   └── StaticRouteConfigChangeProcessor.java (109 lines)
│   │   │   │   │           │   ├── invcache/
│   │   │   │   │           │   │   ├── impl/
│   │   │   │   │           │   │   │   ├── InvCacheAspect.java (261 lines)
│   │   │   │   │           │   │   │   ├── InvCacheAspectUtil.java (298 lines)
│   │   │   │   │           │   │   │   ├── InvCacheICENotifierImpl.java (81 lines)
│   │   │   │   │           │   │   │   └── InventoryServiceCacheImpl.java (258 lines)
│   │   │   │   │           │   │   └── InventoryServiceCache.java (58 lines)
│   │   │   │   │           │   ├── inventory/
│   │   │   │   │           │   │   ├── emscn/
│   │   │   │   │           │   │   │   └── dto/
│   │   │   │   │           │   │   │       ├── InterfaceCountPojo.java (51 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigDTO.java (40 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigDetails.java (18 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigInfo.java (27 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigOperation.java (29 lines)
│   │   │   │   │           │   │   │       └── NotificationConfigType.java (27 lines)
│   │   │   │   │           │   │   ├── grpcService/
│   │   │   │   │           │   │   │   ├── DeviceInventoryApiService.java (87 lines)
│   │   │   │   │           │   │   │   ├── DeviceSyncApiService.java (174 lines)
│   │   │   │   │           │   │   │   ├── GroupingGrpcApiService.java (170 lines)
│   │   │   │   │           │   │   │   └── GrpcServerManager.java (68 lines)
│   │   │   │   │           │   │   ├── listeners/
│   │   │   │   │           │   │   │   ├── CDGGlobalParameterChangeListener.java (207 lines)
│   │   │   │   │           │   │   │   ├── DeviceDeleteListener.java (178 lines)
│   │   │   │   │           │   │   │   ├── GenericDevicePostCollListener.java (136 lines)
│   │   │   │   │           │   │   │   ├── GenericDevicePreCollListener.java (85 lines)
│   │   │   │   │           │   │   │   ├── PostCollectionTopicListener.java (110 lines)
│   │   │   │   │           │   │   │   ├── SyslogSnmpHostConfigProcessor.java (436 lines)
│   │   │   │   │           │   │   │   └── ThirdPartySDUUploadListener.java (180 lines)
│   │   │   │   │           │   │   ├── message/
│   │   │   │   │           │   │   │   ├── CollectionPolicyContextWrapper.java (271 lines)
│   │   │   │   │           │   │   │   ├── InventoryErrorMessage.java (11 lines)
│   │   │   │   │           │   │   │   ├── InventoryNotificationMessage.java (28 lines)
│   │   │   │   │           │   │   │   ├── InventoryRequestMessage.java (15 lines)
│   │   │   │   │           │   │   │   └── InventoryResponseMessage.java (8 lines)
│   │   │   │   │           │   │   ├── portgroup/
│   │   │   │   │           │   │   │   ├── PortColumnInfo.java (45 lines)
│   │   │   │   │           │   │   │   ├── PortGroupRequestHandlerUtil.java (1179 lines)
│   │   │   │   │           │   │   │   ├── PortGroupUtil.java (216 lines)
│   │   │   │   │           │   │   │   ├── PortGroupValidationException.java (14 lines)
│   │   │   │   │           │   │   │   └── PortType.java (38 lines)
│   │   │   │   │           │   │   └── vrf/
│   │   │   │   │           │   │       ├── VRFConstants.java (29 lines)
│   │   │   │   │           │   │       └── VRFUtility.java (209 lines)
│   │   │   │   │           │   ├── inventoryservice/
│   │   │   │   │           │   │   ├── adaptor/
│   │   │   │   │           │   │   │   ├── EMSChangeNotificationPublisherAdapter.java (133 lines)
│   │   │   │   │           │   │   │   └── InventoryAdaptor.java (74 lines)
│   │   │   │   │           │   │   ├── dnac/
│   │   │   │   │           │   │   │   ├── CSVGenerator.java (276 lines)
│   │   │   │   │           │   │   │   └── DNACJsonUtil.java (40 lines)
│   │   │   │   │           │   │   ├── hook/
│   │   │   │   │           │   │   │   ├── DisplayNameUpdateGraphEventHook.java (30 lines)
│   │   │   │   │           │   │   │   ├── InsertBCProvider.java (25 lines)
│   │   │   │   │           │   │   │   └── PEPCallbackImpl.java (148 lines)
│   │   │   │   │           │   │   └── util/
│   │   │   │   │           │   │       ├── EMSChangeNotificationCacheUtil.java (51 lines)
│   │   │   │   │           │   │       ├── EMSChangeNotificationUtil.java (848 lines)
│   │   │   │   │           │   │       ├── EMSInterfaceInfoBuilder.java (710 lines)
│   │   │   │   │           │   │       ├── InventoryPersistenceHelper.java (861 lines)
│   │   │   │   │           │   │       ├── LinkDetails.java (49 lines)
│   │   │   │   │           │   │       ├── ScheduleDeviceMaintenanceManagedStateDTO.java (36 lines)
│   │   │   │   │           │   │       └── VPCDetailsHelper.java (47 lines)
│   │   │   │   │           │   ├── inventoryserviceimpl/
│   │   │   │   │           │   │   ├── AssignDevicesToGroupJob.java (310 lines)
│   │   │   │   │           │   │   ├── BulkDeviceEditJobTask.java (206 lines)
│   │   │   │   │           │   │   ├── Condition.java (28 lines)
│   │   │   │   │           │   │   ├── ControlParameters.java (162 lines)
│   │   │   │   │           │   │   ├── DataFormatUtil.java (67 lines)
│   │   │   │   │           │   │   ├── DeviceCollectionState.java (334 lines)
│   │   │   │   │           │   │   ├── DeviceCredentialCheckCallBack.java (796 lines)
│   │   │   │   │           │   │   ├── DeviceManageability.java (109 lines)
│   │   │   │   │           │   │   ├── DeviceStatusUpdateHook.java (170 lines)
│   │   │   │   │           │   │   ├── EMSAppSettingsInterfaceFilterListener.java (145 lines)
│   │   │   │   │           │   │   ├── EMSInterfaceInventoryMessageListener.java (471 lines)
│   │   │   │   │           │   │   ├── Filter.java (24 lines)
│   │   │   │   │           │   │   ├── GetDevice.java (2140 lines)
│   │   │   │   │           │   │   ├── IfmCredentialProvider.java (129 lines)
│   │   │   │   │           │   │   ├── IfmCredentialValues.java (13 lines)
│   │   │   │   │           │   │   ├── InvEqpmtAdminStateEnum.java (52 lines)
│   │   │   │   │           │   │   ├── InvEqpmtOperStateEnum.java (53 lines)
│   │   │   │   │           │   │   ├── InvEquipmentTypeEnum.java (55 lines)
│   │   │   │   │           │   │   ├── InventoryMessageHandler.java (308 lines)
│   │   │   │   │           │   │   ├── InventoryMessageListener.java (694 lines)
│   │   │   │   │           │   │   ├── InventoryNotificationDispatcher.java (175 lines)
│   │   │   │   │           │   │   ├── InventoryQueryString.java (296 lines)
│   │   │   │   │           │   │   ├── InventoryServiceImpl.java (17400 lines)
│   │   │   │   │           │   │   ├── InventoryThreadLocal.java (40 lines)
│   │   │   │   │           │   │   ├── InventoryUtil.java (1310 lines)
│   │   │   │   │           │   │   ├── MCNChangeNotificationPublisher.java (513 lines)
│   │   │   │   │           │   │   ├── MCNDeleteNotificationPublisher.java (154 lines)
│   │   │   │   │           │   │   ├── ScheduleDeviceMaintenanceJobTask.java (199 lines)
│   │   │   │   │           │   │   ├── ScheduleDeviceManagedJobTask.java (202 lines)
│   │   │   │   │           │   │   ├── SmartLicensingComplianceReportJob.java (178 lines)
│   │   │   │   │           │   │   ├── UCSInventoryQueryConstants.java (84 lines)
│   │   │   │   │           │   │   └── XdeInitInv.java (48 lines)
│   │   │   │   │           │   ├── inventoryserviceplugin/
│   │   │   │   │           │   │   ├── AuthEntityIdSetterCallbackImpl.java (106 lines)
│   │   │   │   │           │   │   ├── ChassisCallBackImpl.java (50 lines)
│   │   │   │   │           │   │   ├── DeleteSNMPEngineIdHook.java (86 lines)
│   │   │   │   │           │   │   ├── FaultInventoryCollectionCallbackPlugin.java (69 lines)
│   │   │   │   │           │   │   ├── IPEPInSTPCallBackImpl.java (84 lines)
│   │   │   │   │           │   │   ├── InventoryStatusPopulateCallbackImpl.java (257 lines)
│   │   │   │   │           │   │   ├── IpAddressToDnsMappingCallbackImpl.java (66 lines)
│   │   │   │   │           │   │   ├── LocationUpdateCallBackImpl.java (131 lines)
│   │   │   │   │           │   │   ├── MEICallbackImpl.java (34 lines)
│   │   │   │   │           │   │   ├── MNELocationGraphHook.java (100 lines)
│   │   │   │   │           │   │   ├── NECallbackImpl.java (277 lines)
│   │   │   │   │           │   │   ├── NRCallbackImpl.java (159 lines)
│   │   │   │   │           │   │   └── PepCallBackImpl.java (45 lines)
│   │   │   │   │           │   ├── inventorystatistics/
│   │   │   │   │           │   │   ├── ExcelInventoryStatisticsFileWriter.java (653 lines)
│   │   │   │   │           │   │   ├── InventoryStatisticsFileWriter.java (12 lines)
│   │   │   │   │           │   │   ├── InventoryStatisticsHelper.java (59 lines)
│   │   │   │   │           │   │   ├── InventoryStatisticsStatus.java (33 lines)
│   │   │   │   │           │   │   └── InventoryStatisticsSummary.java (14 lines)
│   │   │   │   │           │   ├── invhelper/
│   │   │   │   │           │   │   ├── InventoryCommonHelper.java (105 lines)
│   │   │   │   │           │   │   ├── InventoryDBUtil.java (206 lines)
│   │   │   │   │           │   │   ├── InventoryMCNHelper.java (133 lines)
│   │   │   │   │           │   │   ├── RowCountUtil.java (32 lines)
│   │   │   │   │           │   │   ├── SwitchHelper.java (350 lines)
│   │   │   │   │           │   │   └── SwitchHelperIfc.java (17 lines)
│   │   │   │   │           │   ├── ipsec/
│   │   │   │   │           │   │   └── IPSecConfigManager.java (581 lines)
│   │   │   │   │           │   ├── kafka/
│   │   │   │   │           │   │   ├── dlmnotification/
│   │   │   │   │           │   │   │   ├── handler/
│   │   │   │   │           │   │   │   │   ├── DLMNotificationHandler.java (386 lines)
│   │   │   │   │           │   │   │   │   └── FailedNotificationHandler.java (12 lines)
│   │   │   │   │           │   │   │   ├── listener/
│   │   │   │   │           │   │   │   │   ├── pojo/
│   │   │   │   │           │   │   │   │   │   └── GrpcFailureContextAttributes.java (40 lines)
│   │   │   │   │           │   │   │   │   ├── CredentialNotificationListener.java (678 lines)
│   │   │   │   │           │   │   │   │   ├── DLMNotificationListener.java (34 lines)
│   │   │   │   │           │   │   │   │   └── NodeNotificationListener.java (1063 lines)
│   │   │   │   │           │   │   │   ├── processor/
│   │   │   │   │           │   │   │   │   └── UpdateCredThread.java (79 lines)
│   │   │   │   │           │   │   │   └── RobotNodeDataAttribute.java (29 lines)
│   │   │   │   │           │   │   └── ems/
│   │   │   │   │           │   │       └── notification/
│   │   │   │   │           │   │           ├── dto/
│   │   │   │   │           │   │           │   ├── DestDetails.java (94 lines)
│   │   │   │   │           │   │           │   └── Destination.java (45 lines)
│   │   │   │   │           │   │           ├── handler/
│   │   │   │   │           │   │           │   └── GeoDestinationManagerHandler.java (802 lines)
│   │   │   │   │           │   │           └── util/
│   │   │   │   │           │   │               ├── CertService.java (234 lines)
│   │   │   │   │           │   │               ├── DestinationFileReader.java (126 lines)
│   │   │   │   │           │   │               ├── EMSNotificationLogger.java (99 lines)
│   │   │   │   │           │   │               ├── GeoModeFileReader.java (62 lines)
│   │   │   │   │           │   │               └── KafkaDestinationUtils.java (81 lines)
│   │   │   │   │           │   ├── logger/
│   │   │   │   │           │   │   └── AuditLogger.java (56 lines)
│   │   │   │   │           │   ├── postInitHook/
│   │   │   │   │           │   │   ├── IFMPostInitHookImpl.java (106 lines)
│   │   │   │   │           │   │   ├── SmartLicensingServiceImpl.java (164 lines)
│   │   │   │   │           │   │   └── SyncOfflineDevicesImpl.java (288 lines)
│   │   │   │   │           │   ├── postUpgradeHook/
│   │   │   │   │           │   │   ├── CLIAddressUpdateHook.java (109 lines)
│   │   │   │   │           │   │   ├── CredentialPropsUpgradeHandler.java (188 lines)
│   │   │   │   │           │   │   ├── IFMMainPostUpgradeHook.java (403 lines)
│   │   │   │   │           │   │   ├── MDFToDBSyncHandler.java (176 lines)
│   │   │   │   │           │   │   └── SnmpTransportUpdateHook.java (149 lines)
│   │   │   │   │           │   ├── syncofflineprefimpl/
│   │   │   │   │           │   │   └── SyncOfflineDevicePrefImpl.java (150 lines)
│   │   │   │   │           │   ├── ucsinventory/
│   │   │   │   │           │   │   └── dto/
│   │   │   │   │           │   │       ├── DCServiceProfileDTO.java (143 lines)
│   │   │   │   │           │   │       ├── ServiceProfileHierarchyDTO.java (182 lines)
│   │   │   │   │           │   │       ├── ServiceProfileHierarchyListDTO.java (41 lines)
│   │   │   │   │           │   │       └── UCSSectionDTO.java (72 lines)
│   │   │   │   │           │   ├── udfconfigserviceimpl/
│   │   │   │   │           │   │   ├── UDFData.java (60 lines)
│   │   │   │   │           │   │   ├── UdfConfigServiceImpl.java (1224 lines)
│   │   │   │   │           │   │   └── UdfConstants.java (7 lines)
│   │   │   │   │           │   └── wrapper/
│   │   │   │   │           │       ├── CdgDataWrapper.java (131 lines)
│   │   │   │   │           │       └── IfmBCWrapperProvider.java (32 lines)
│   │   │   │   │           └── nms/
│   │   │   │   │               ├── ce/
│   │   │   │   │               │   └── event/
│   │   │   │   │               │       └── correlation/
│   │   │   │   │               │           └── DuplicateEventsFlowController.java (87 lines)
│   │   │   │   │               └── optical/
│   │   │   │   │                   └── event/
│   │   │   │   │                       └── correlation/
│   │   │   │   │                           └── PrioritizedEventsFlowController.java (138 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   ├── spring/
│   │   │   │       │   │   ├── ifm_inventory_service_aop.xml (19 lines)
│   │   │   │       │   │   ├── ifm_inventory_service_context.xml (266 lines)
│   │   │   │       │   │   ├── ifm_inventory_service_context_apic.xml (120 lines)
│   │   │   │       │   │   ├── module-context.xml (38 lines)
│   │   │   │       │   │   └── osgi-context.xml (22 lines)
│   │   │   │       │   ├── MANIFEST.MF (70 lines)
│   │   │   │       │   └── aop.xml (21 lines)
│   │   │   │       ├── com/
│   │   │   │       │   └── cisco/
│   │   │   │       │       └── ifm/
│   │   │   │       │           └── inventoryservice/
│   │   │   │       │               ├── logging/
│   │   │   │       │               │   ├── InventoryServiceMessages.properties (169 lines)
│   │   │   │       │               │   └── InventoryServiceMessages.xml (882 lines)
│   │   │   │       │               ├── status/
│   │   │   │       │               │   └── lastcollectionstatusgroups.xml (26 lines)
│   │   │   │       │               ├── template/
│   │   │   │       │               │   └── pi-ipsec.template (86 lines)
│   │   │   │       │               └── xml/
│   │   │   │       │                   └── InventoryCollectionStates.xml (211 lines)
│   │   │   │       └── ifm_inventory_categories.xml (13 lines)
│   │   │   ├── site/
│   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── test/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           ├── ifm/
│   │   │   │   │           │   ├── aspects/
│   │   │   │   │           │   │   ├── AuditInventoryAfterAspectTest.java (123 lines)
│   │   │   │   │           │   │   └── AuditInventoryAroundAspectTest.java (445 lines)
│   │   │   │   │           │   ├── converter/
│   │   │   │   │           │   │   ├── AddressToLocationNioWrapperConverterTest.java (30 lines)
│   │   │   │   │           │   │   └── DeviceToNetworkDeviceNioWrapperConverterTest.java (152 lines)
│   │   │   │   │           │   ├── deviceinventory/
│   │   │   │   │           │   │   ├── DeviceInventoryRequestHandlerTest.java (1286 lines)
│   │   │   │   │           │   │   └── EMSInterfaceInventoryRequestHandlerTest.java (397 lines)
│   │   │   │   │           │   ├── dlm/
│   │   │   │   │           │   │   ├── DlmDataServiceImplTest.java (1571 lines)
│   │   │   │   │           │   │   └── DlmDataServiceValidatorTest.java (288 lines)
│   │   │   │   │           │   ├── eventbasedinventory/
│   │   │   │   │           │   │   ├── ArchivelogExecutorTest.java (537 lines)
│   │   │   │   │           │   │   ├── BeanUtilityTest.java (43 lines)
│   │   │   │   │           │   │   ├── CE-EventBasedInventoryRules.xml (1465 lines)
│   │   │   │   │           │   │   ├── CorrelationRuleActionTest.java (48 lines)
│   │   │   │   │           │   │   ├── CustomizedGranularInventoryPolicyTest.java (639 lines)
│   │   │   │   │           │   │   ├── DevicePackageLoaderTestStub.java (270 lines)
│   │   │   │   │           │   │   ├── DevicePackageLoaderTestStubEmpty.java (262 lines)
│   │   │   │   │           │   │   ├── DeviceReachabilityRuleActionTest.java (336 lines)
│   │   │   │   │           │   │   ├── EventBasedAdminSettingsListenerTest.java (145 lines)
│   │   │   │   │           │   │   ├── EventBasedArchiveIdCacheTest.java (101 lines)
│   │   │   │   │           │   │   ├── ExpediteInventoryProcessorTest.java (229 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueueExecutorTest.java (246 lines)
│   │   │   │   │           │   │   ├── GranularInventoryQueueTest.java (79 lines)
│   │   │   │   │           │   │   ├── GranularInventoryRuleActionTest.java (167 lines)
│   │   │   │   │           │   │   ├── InterfaceConfigChangeProcessorTest.java (405 lines)
│   │   │   │   │           │   │   ├── InventoryConfigChangeProcessorTest.java (83 lines)
│   │   │   │   │           │   │   ├── InventorySyslogProcessorTest.java (1030 lines)
│   │   │   │   │           │   │   ├── InventorySyslogRuleActionTest.java (845 lines)
│   │   │   │   │           │   │   ├── PackageQualifiedIdStub.java (30 lines)
│   │   │   │   │           │   │   ├── PhysicalPepChangeProcessorTest.java (110 lines)
│   │   │   │   │           │   │   ├── RefreshInventoryObjectsWrapperTest.java (67 lines)
│   │   │   │   │           │   │   └── StaticRouteConfigChangeProcessorTest.java (93 lines)
│   │   │   │   │           │   ├── invcache/
│   │   │   │   │           │   │   └── impl/
│   │   │   │   │           │   │       ├── InvCacheAspectTest.java (197 lines)
│   │   │   │   │           │   │       ├── InvCacheAspectUtilTest.java (196 lines)
│   │   │   │   │           │   │       ├── InvCacheICENotifierImplTest.java (77 lines)
│   │   │   │   │           │   │       └── InventoryServiceCacheImplTest.java (266 lines)
│   │   │   │   │           │   ├── inventory/
│   │   │   │   │           │   │   ├── emscn/
│   │   │   │   │           │   │   │   └── dto/
│   │   │   │   │           │   │   │       ├── NotificationConfigDTOTest.java (45 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigDetailsTest.java (26 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigInfoTest.java (32 lines)
│   │   │   │   │           │   │   │       ├── NotificationConfigOperationTest.java (24 lines)
│   │   │   │   │           │   │   │       └── NotificationConfigTypeTest.java (23 lines)
│   │   │   │   │           │   │   ├── grpcService/
│   │   │   │   │           │   │   │   ├── DeviceInventoryApiServiceTest.java (81 lines)
│   │   │   │   │           │   │   │   ├── DeviceSyncApiServiceTest.java (162 lines)
│   │   │   │   │           │   │   │   ├── GroupingGrpcApiServiceTest.java (134 lines)
│   │   │   │   │           │   │   │   └── GrpcServerManagerTest.java (109 lines)
│   │   │   │   │           │   │   ├── listeners/
│   │   │   │   │           │   │   │   ├── CDGGlobalParameterChangeListenerTest.java (146 lines)
│   │   │   │   │           │   │   │   ├── DeviceDeleteListenerTest.java (184 lines)
│   │   │   │   │           │   │   │   ├── GenericDevicePostCollListenerTest.java (206 lines)
│   │   │   │   │           │   │   │   ├── GenericDevicePreCollListenerTest.java (116 lines)
│   │   │   │   │           │   │   │   ├── PostCollectionTopicListenerTest.java (131 lines)
│   │   │   │   │           │   │   │   ├── SyslogSnmpHostConfigProcessorTest.java (455 lines)
│   │   │   │   │           │   │   │   └── ThirdPartySDUUploadListenerTest.java (137 lines)
│   │   │   │   │           │   │   ├── message/
│   │   │   │   │           │   │   │   └── CollectionPolicyContextWrapperTest.java (154 lines)
│   │   │   │   │           │   │   ├── portgroup/
│   │   │   │   │           │   │   │   ├── PortColumnInfoTest.java (42 lines)
│   │   │   │   │           │   │   │   ├── PortGroupRequestHandlerUtilTest.java (987 lines)
│   │   │   │   │           │   │   │   └── PortGroupUtilTest.java (143 lines)
│   │   │   │   │           │   │   └── vrf/
│   │   │   │   │           │   │       ├── VRFConstantsTest.java (36 lines)
│   │   │   │   │           │   │       └── VRFUtilityTest.java (247 lines)
│   │   │   │   │           │   ├── inventoryservice/
│   │   │   │   │           │   │   ├── adaptor/
│   │   │   │   │           │   │   │   ├── EMSChangeNotificationPublisherAdapterTest.java (203 lines)
│   │   │   │   │           │   │   │   └── InventoryAdaptorTest.java (104 lines)
│   │   │   │   │           │   │   ├── dnac/
│   │   │   │   │           │   │   │   └── CSVGeneratorTest.java (166 lines)
│   │   │   │   │           │   │   ├── hook/
│   │   │   │   │           │   │   │   └── PEPCallbackImplTest.java (197 lines)
│   │   │   │   │           │   │   └── util/
│   │   │   │   │           │   │       ├── EMSChangeNotificationUtilTest.java (1611 lines)
│   │   │   │   │           │   │       ├── EMSInterfaceInfoBuilderTest.java (534 lines)
│   │   │   │   │           │   │       └── InventoryPersistenceHelperTest.java (857 lines)
│   │   │   │   │           │   ├── inventoryserviceimpl/
│   │   │   │   │           │   │   ├── AssignDevicesToGroupJobTest.java (183 lines)
│   │   │   │   │           │   │   ├── BulkDeviceEditJobTaskTest.java (423 lines)
│   │   │   │   │           │   │   ├── ConditionTest.java (41 lines)
│   │   │   │   │           │   │   ├── ControlParametersTest.java (150 lines)
│   │   │   │   │           │   │   ├── DataFormatUtilTest.java (65 lines)
│   │   │   │   │           │   │   ├── DeviceCollectionStateTest.java (74 lines)
│   │   │   │   │           │   │   ├── DeviceCredentialCheckCallBackTest.java (566 lines)
│   │   │   │   │           │   │   ├── DeviceManageabilityTest.java (99 lines)
│   │   │   │   │           │   │   ├── EMSAppSettingsInterfaceFilterListenerTest.java (495 lines)
│   │   │   │   │           │   │   ├── EMSInterfaceInventoryMessageListenerTest.java (410 lines)
│   │   │   │   │           │   │   ├── FilterTest.java (29 lines)
│   │   │   │   │           │   │   ├── GetDeviceTest.java (5338 lines)
│   │   │   │   │           │   │   ├── IfmCredentialProviderTest.java (113 lines)
│   │   │   │   │           │   │   ├── InventoryMessageHandlerTest.java (415 lines)
│   │   │   │   │           │   │   ├── InventoryMessageListenerTest.java (1084 lines)
│   │   │   │   │           │   │   ├── InventoryNotificationDispatcherTest.java (232 lines)
│   │   │   │   │           │   │   ├── InventoryQueryStringTest.java (64 lines)
│   │   │   │   │           │   │   ├── InventoryServiceImplTest.java (10947 lines)
│   │   │   │   │           │   │   ├── InventoryUtilTest.java (700 lines)
│   │   │   │   │           │   │   ├── MCNChangeNotificationPublisherTest.java (297 lines)
│   │   │   │   │           │   │   ├── MCNDeleteNotificationPublisherTest.java (349 lines)
│   │   │   │   │           │   │   ├── ScheduleDeviceMaintenanceJobTaskTest.java (279 lines)
│   │   │   │   │           │   │   ├── ScheduleDeviceManagedJobTaskTest.java (279 lines)
│   │   │   │   │           │   │   └── SmartLicensingComplianceReportJobTest.java (121 lines)
│   │   │   │   │           │   ├── inventoryserviceplugin/
│   │   │   │   │           │   │   ├── AuthEntityIdSetterCallbackImplTest.java (31 lines)
│   │   │   │   │           │   │   ├── ChassisCallBackImplTest.java (78 lines)
│   │   │   │   │           │   │   ├── DeleteSNMPEngineIdHookTest.java (117 lines)
│   │   │   │   │           │   │   ├── FaultInventoryCollectionCallbackPluginTest.java (113 lines)
│   │   │   │   │           │   │   ├── InventoryStatusPopulateCallbackImplTest.java (165 lines)
│   │   │   │   │           │   │   ├── IpAddressToDnsMappingCallbackImplTest.java (142 lines)
│   │   │   │   │           │   │   ├── LocationUpdateCallBackImplTest.java (276 lines)
│   │   │   │   │           │   │   ├── MEICallbackImplTest.java (51 lines)
│   │   │   │   │           │   │   ├── MNELocationGraphHookTest.java (312 lines)
│   │   │   │   │           │   │   ├── NECallbackImplTest.java (285 lines)
│   │   │   │   │           │   │   ├── NRCallbackImplTest.java (68 lines)
│   │   │   │   │           │   │   └── PepCallBackImplTest.java (73 lines)
│   │   │   │   │           │   ├── inventorystatistics/
│   │   │   │   │           │   │   ├── ExcelInventoryStatisticsFileWriterTest.java (141 lines)
│   │   │   │   │           │   │   ├── InventoryStatisticsHelperTest.java (87 lines)
│   │   │   │   │           │   │   ├── InventoryStatisticsStatusTest.java (42 lines)
│   │   │   │   │           │   │   └── InventoryStatisticsSummaryTest.java (48 lines)
│   │   │   │   │           │   ├── invhelper/
│   │   │   │   │           │   │   ├── InventoryCommonHelperTest.java (70 lines)
│   │   │   │   │           │   │   ├── InventoryDBUtilTest.java (194 lines)
│   │   │   │   │           │   │   ├── InventoryMCNHelperTest.java (184 lines)
│   │   │   │   │           │   │   └── SwitchHelperTest.java (695 lines)
│   │   │   │   │           │   ├── ipsec/
│   │   │   │   │           │   │   └── IPSecConfigManagerTest.java (543 lines)
│   │   │   │   │           │   ├── kafka/
│   │   │   │   │           │   │   ├── dlmnotification/
│   │   │   │   │           │   │   │   ├── handler/
│   │   │   │   │           │   │   │   │   └── DLMNotificationHandlerTest.java (441 lines)
│   │   │   │   │           │   │   │   └── listener/
│   │   │   │   │           │   │   │       ├── CredentialNotificationListenerTest.java (1763 lines)
│   │   │   │   │           │   │   │       └── NodeNotificationListenerTest.java (4280 lines)
│   │   │   │   │           │   │   └── ems/
│   │   │   │   │           │   │       └── notification/
│   │   │   │   │           │   │           ├── dto/
│   │   │   │   │           │   │           │   ├── DestDetailsTest.java (73 lines)
│   │   │   │   │           │   │           │   └── DestinationTest.java (41 lines)
│   │   │   │   │           │   │           ├── handler/
│   │   │   │   │           │   │           │   └── GeoDestinationManagerHandlerTest.java (89 lines)
│   │   │   │   │           │   │           └── util/
│   │   │   │   │           │   │               ├── CertServiceTest.java (302 lines)
│   │   │   │   │           │   │               ├── DestinationFileReaderTest.java (65 lines)
│   │   │   │   │           │   │               ├── GeoModeFileReaderTest.java (60 lines)
│   │   │   │   │           │   │               └── KafkaDestinationUtilsTest.java (79 lines)
│   │   │   │   │           │   ├── logger/
│   │   │   │   │           │   │   └── AuditLoggerTest.java (74 lines)
│   │   │   │   │           │   ├── postInitHook/
│   │   │   │   │           │   │   ├── SmartLicensingServiceImplTest.java (66 lines)
│   │   │   │   │           │   │   └── SyncOfflineDevicesImplTest.java (230 lines)
│   │   │   │   │           │   ├── postUpgradeHook/
│   │   │   │   │           │   │   ├── CLIAddressUpdateHookTest.java (117 lines)
│   │   │   │   │           │   │   ├── CredentialPropsUpgradeHandlerTest.java (114 lines)
│   │   │   │   │           │   │   ├── IFMMainPostUpgradeHookTest.java (338 lines)
│   │   │   │   │           │   │   ├── MDFToDBSyncHandlerTest.java (243 lines)
│   │   │   │   │           │   │   └── SnmpTransportUpdateHookTest.java (131 lines)
│   │   │   │   │           │   ├── randoop/
│   │   │   │   │           │   │   └── gen/
│   │   │   │   │           │   │       └── tests/
│   │   │   │   │           │   │           ├── RegressionTest.java (9 lines)
│   │   │   │   │           │   │           ├── RegressionTest0.java (1187 lines)
│   │   │   │   │           │   │           └── RegressionTest1.java (6037 lines)
│   │   │   │   │           │   ├── syncofflineprefimpl/
│   │   │   │   │           │   │   └── SyncOfflineDevicePrefImplTest.java (162 lines)
│   │   │   │   │           │   ├── ucsinventory/
│   │   │   │   │           │   │   └── dto/
│   │   │   │   │           │   │       ├── DCServiceProfileDTOTest.java (45 lines)
│   │   │   │   │           │   │       ├── ServiceProfileHierarchyDTOTest.java (50 lines)
│   │   │   │   │           │   │       ├── ServiceProfileHierarchyListDTOTest.java (31 lines)
│   │   │   │   │           │   │       └── UCSSectionDTOTest.java (35 lines)
│   │   │   │   │           │   ├── udfconfigserviceimpl/
│   │   │   │   │           │   │   ├── UDFDataTest.java (110 lines)
│   │   │   │   │           │   │   ├── UdfConfigServiceImplTest.java (713 lines)
│   │   │   │   │           │   │   └── UdfConstantsTest.java (31 lines)
│   │   │   │   │           │   └── wrapper/
│   │   │   │   │           │       ├── CdgDataWrapperTest.java (163 lines)
│   │   │   │   │           │       └── IfmBCWrapperProviderTest.java (14 lines)
│   │   │   │   │           └── nms/
│   │   │   │   │               └── optical/
│   │   │   │   │                   └── event/
│   │   │   │   │                       └── correlation/
│   │   │   │   │                           └── PrioritizedEventsFlowControllerTest.java (143 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   └── spring/
│   │   │   │       │       └── LoggerTest-context.xml (23 lines)
│   │   │   │       ├── conf/
│   │   │   │       │   ├── ifm/
│   │   │   │       │   │   ├── portColumnMap.xml (14 lines)
│   │   │   │       │   │   └── portTypesList.xml (299 lines)
│   │   │   │       │   ├── ifm_inventory.properties (7 lines)
│   │   │   │       │   └── log4j.xml (89 lines)
│   │   │   │       ├── testdatafiles/
│   │   │   │       │   └── inventory_devices.xml (58 lines)
│   │   │   │       ├── DeviceTestSuite.xml (19 lines)
│   │   │   │       ├── EventPatternExample.xml (45 lines)
│   │   │   │       └── testbed.xml (15 lines)
│   │   │   └── test-Excluded/
│   │   │       └── java/
│   │   │           └── com/
│   │   │               └── cisco/
│   │   │                   ├── ifm/
│   │   │                   │   ├── aspects/
│   │   │                   │   │   └── AuditInventoryAroundAspectTest.java (425 lines)
│   │   │                   │   ├── eventbasedinventory/
│   │   │                   │   │   ├── ArchivelogExecutorTest.java (200 lines)
│   │   │                   │   │   ├── GranularInventoryQueueExecutorTest.java (52 lines)
│   │   │                   │   │   └── SyslogMsgInfoTests.java (149 lines)
│   │   │                   │   ├── invcache/
│   │   │                   │   │   └── impl/
│   │   │                   │   │       └── InvCacheAspectUtilTest.java (112 lines)
│   │   │                   │   ├── inventory/
│   │   │                   │   │   ├── listeners/
│   │   │                   │   │   │   └── SyslogSnmpHostConfigProcessorTest.java (250 lines)
│   │   │                   │   │   └── portgroup/
│   │   │                   │   │       └── PortGroupAPITest.java (2280 lines)
│   │   │                   │   ├── inventoryservice/
│   │   │                   │   │   ├── hook/
│   │   │                   │   │   │   └── VDCHookTest.java (39 lines)
│   │   │                   │   │   ├── InventoryServiceImplTest.java (3203 lines)
│   │   │                   │   │   ├── TestCredential.java (43 lines)
│   │   │                   │   │   ├── TestCredentialMgr.java (306 lines)
│   │   │                   │   │   ├── TestDeviceCredentialCheckCallBack.java (139 lines)
│   │   │                   │   │   ├── TestDisplayText.java (43 lines)
│   │   │                   │   │   ├── TestEventBasedAdminSettingsListener.java (123 lines)
│   │   │                   │   │   ├── TestEventBasedArchiveIdCache.java (102 lines)
│   │   │                   │   │   ├── TestExpediteInventoryProcessor.java (161 lines)
│   │   │                   │   │   ├── TestGranularConfigChangeProcessorImpl.java (33 lines)
│   │   │                   │   │   ├── TestHibernateCriteria.java (276 lines)
│   │   │                   │   │   ├── TestInvConfigChangeProcessor.java (80 lines)
│   │   │                   │   │   ├── TestInventoryDBUtil.java (788 lines)
│   │   │                   │   │   ├── TestInventorySyslogProcessor.java (197 lines)
│   │   │                   │   │   ├── TestInventorySyslogRuleAction.java (119 lines)
│   │   │                   │   │   ├── TestPersistenceFactory.java (149 lines)
│   │   │                   │   │   ├── TestPersistenceService.java (1081 lines)
│   │   │                   │   │   ├── TestProcessorToFeatureList.java (59 lines)
│   │   │                   │   │   ├── TestQuery.java (841 lines)
│   │   │                   │   │   ├── TestSession.java (1063 lines)
│   │   │                   │   │   ├── TestSessionFactory.java (309 lines)
│   │   │                   │   │   ├── UCSInventoryServiceImplTest.java (2060 lines)
│   │   │                   │   │   └── VRFUtilityTest.java (234 lines)
│   │   │                   │   ├── inventoryserviceimpl/
│   │   │                   │   │   └── TestHelper.java (10 lines)
│   │   │                   │   ├── inventoryserviceplugin/
│   │   │                   │   │   └── NECallbackImplTest.java (916 lines)
│   │   │                   │   ├── ipsec/
│   │   │                   │   │   └── IPSecConfigManagerTest.java (49 lines)
│   │   │                   │   ├── postInitHook/
│   │   │                   │   │   └── SmartLicensingServiceImplTest.java (63 lines)
│   │   │                   │   ├── postUpgradeHook/
│   │   │                   │   │   ├── CredentialPropsUpgradeHandlerTest.java (69 lines)
│   │   │                   │   │   └── IFMMainPostUpgradeHookTest.java (32 lines)
│   │   │                   │   └── ucsinventory/
│   │   │                   │       └── util/
│   │   │                   │           └── UCSRestInventoryUtilTest.java (1991 lines)
│   │   │                   └── nms/
│   │   │                       └── optical/
│   │   │                           └── event/
│   │   │                               └── correlation/
│   │   │                                   ├── EventMatcher.java (43 lines)
│   │   │                                   ├── EventSequence.java (50 lines)
│   │   │                                   ├── EventsFactory.java (67 lines)
│   │   │                                   ├── FSMTest.java (442 lines)
│   │   │                                   ├── FilterPatternFlowControllerTest.java (505 lines)
│   │   │                                   ├── PrioritizedEventsFlowControllerTest.java (207 lines)
│   │   │                                   └── PunctualUpdateEventHandlerTL1TestImpl.java (21 lines)
│   │   ├── .gitignore (5 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── build.xml (45 lines)
│   │   ├── fileName (0 lines)
│   │   ├── jtestsettings.properties (60 lines)
│   │   ├── merge_0210_2014.txt (26 lines)
│   │   ├── merge_12_08.txt (1915 lines)
│   │   ├── pom.xml (2373 lines)
│   │   └── release-pom.xml.save (3399 lines)
│   ├── ifm_inventory_service_package/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           ├── ifm/
│   │   │   │   │           │   ├── dlm/
│   │   │   │   │           │   │   ├── DlmConstants.java (44 lines)
│   │   │   │   │           │   │   └── DlmDataService.java (287 lines)
│   │   │   │   │           │   ├── eventbasedinventory/
│   │   │   │   │           │   │   ├── CompositeEventFlowController.java (222 lines)
│   │   │   │   │           │   │   ├── EventFlowController.java (16 lines)
│   │   │   │   │           │   │   ├── EventInfo.java (38 lines)
│   │   │   │   │           │   │   ├── GranularInvResnCommitInfo.java (53 lines)
│   │   │   │   │           │   │   ├── GranularInventoryConfigChangeProcessor.java (16 lines)
│   │   │   │   │           │   │   ├── GranularInventoryEventActionTypeEnum.java (19 lines)
│   │   │   │   │           │   │   ├── GranularInventoryEventHandler.java (23 lines)
│   │   │   │   │           │   │   ├── GranularInventoryEventResult.java (139 lines)
│   │   │   │   │           │   │   ├── LinkStatusGranularInventoryEventHandler.java (227 lines)
│   │   │   │   │           │   │   ├── ProcessorToFeatureList.java (83 lines)
│   │   │   │   │           │   │   ├── RefreshInventoryObjectsWrapper.java (85 lines)
│   │   │   │   │           │   │   ├── SyslogMsgInfo.java (267 lines)
│   │   │   │   │           │   │   └── ThresholdEventFlowController.java (26 lines)
│   │   │   │   │           │   ├── inventorymodel/
│   │   │   │   │           │   │   ├── InterfaceServiceNioWrapper.java (295 lines)
│   │   │   │   │           │   │   ├── LinkNIOWrapper.java (180 lines)
│   │   │   │   │           │   │   ├── LocationNioWrapper.java (145 lines)
│   │   │   │   │           │   │   └── NetworkDeviceNioWrapper.java (678 lines)
│   │   │   │   │           │   ├── inventoryservice/
│   │   │   │   │           │   │   ├── dto/
│   │   │   │   │           │   │   │   ├── CollectionStatusCountDTOList.java (42 lines)
│   │   │   │   │           │   │   │   ├── InterfaceDTO.java (49 lines)
│   │   │   │   │           │   │   │   ├── InvEquipmentDTO.java (127 lines)
│   │   │   │   │           │   │   │   ├── InventoryDeviceItemDTO.java (36 lines)
│   │   │   │   │           │   │   │   ├── InventoryDeviceSyncTaskDTO.java (108 lines)
│   │   │   │   │           │   │   │   ├── InventoryDeviceSyncTaskDTOList.java (143 lines)
│   │   │   │   │           │   │   │   ├── LagLinkDTO.java (65 lines)
│   │   │   │   │           │   │   │   ├── LineChartItemsDTO.java (32 lines)
│   │   │   │   │           │   │   │   ├── LineChartItemsListDTO.java (41 lines)
│   │   │   │   │           │   │   │   ├── LineChartLabelsDTO.java (32 lines)
│   │   │   │   │           │   │   │   ├── LoggerLevelDTO.java (77 lines)
│   │   │   │   │           │   │   │   ├── MemberInterfaceDTO.java (73 lines)
│   │   │   │   │           │   │   │   ├── MemberLinkDetailsDTO.java (68 lines)
│   │   │   │   │           │   │   │   ├── NewPortChannelDetailsDTO.java (88 lines)
│   │   │   │   │           │   │   │   ├── NewPortChannelEndDTO.java (47 lines)
│   │   │   │   │           │   │   │   ├── PortChannelDTO.java (26 lines)
│   │   │   │   │           │   │   │   ├── ScheduleDeviceMaintenanceManagedStateDTO.java (34 lines)
│   │   │   │   │           │   │   │   ├── VDCAllocatedCPUDTO.java (16 lines)
│   │   │   │   │           │   │   │   ├── VPCDetailsDTO.java (100 lines)
│   │   │   │   │           │   │   │   └── VirtualDomainDTO360.java (54 lines)
│   │   │   │   │           │   │   ├── Device.java (1159 lines)
│   │   │   │   │           │   │   ├── DeviceRetrievalCriteria.java (505 lines)
│   │   │   │   │           │   │   ├── DistributedHealthUtil.java (30 lines)
│   │   │   │   │           │   │   ├── FunctionalCapabilityEnum.java (16 lines)
│   │   │   │   │           │   │   ├── IDeviceDeleteHandler.java (32 lines)
│   │   │   │   │           │   │   ├── InventoryDiagnosticUtil.java (101 lines)
│   │   │   │   │           │   │   ├── InventoryService.java (2044 lines)
│   │   │   │   │           │   │   ├── LeadershipService.java (5 lines)
│   │   │   │   │           │   │   ├── RetrievalCriteria.java (207 lines)
│   │   │   │   │           │   │   └── UCSInventoryService.java (338 lines)
│   │   │   │   │           │   ├── inventoryserviceexception/
│   │   │   │   │           │   │   ├── InventoryException.java (43 lines)
│   │   │   │   │           │   │   └── InventoryUncheckedException.java (59 lines)
│   │   │   │   │           │   └── logger/
│   │   │   │   │           │       └── IFMInventoryLogger.java (56 lines)
│   │   │   │   │           └── nms/
│   │   │   │   │               ├── ce/
│   │   │   │   │               │   └── event/
│   │   │   │   │               │       └── correlation/
│   │   │   │   │               │           └── FlappingEventsFlowController.java (84 lines)
│   │   │   │   │               └── optical/
│   │   │   │   │                   └── event/
│   │   │   │   │                       └── correlation/
│   │   │   │   │                           ├── CompositeEvent.java (61 lines)
│   │   │   │   │                           ├── FilterPatternAction.java (343 lines)
│   │   │   │   │                           ├── FilterPatternFlowController.java (761 lines)
│   │   │   │   │                           └── SubstringParser.java (62 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   ├── spring/
│   │   │   │       │   │   ├── ifm_inventory_service_package_context.xml (15 lines)
│   │   │   │       │   │   ├── module-context.xml (15 lines)
│   │   │   │       │   │   └── osgi-context.xml (11 lines)
│   │   │   │       │   └── MANIFEST.MF (56 lines)
│   │   │   │       └── com/
│   │   │   │           └── cisco/
│   │   │   │               └── ifm/
│   │   │   │                   └── inventoryservice/
│   │   │   │                       └── InventoryService.properties (139 lines)
│   │   │   ├── site/
│   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   └── test/
│   │   │       └── java/
│   │   │           └── com/
│   │   │               └── cisco/
│   │   │                   ├── ifm/
│   │   │                   │   ├── eventbasedinventory/
│   │   │                   │   │   ├── CompositeEventFlowControllerTest.java (313 lines)
│   │   │                   │   │   ├── EventInfoTest.java (68 lines)
│   │   │                   │   │   ├── GranularInvResnCommitInfoTest.java (34 lines)
│   │   │                   │   │   ├── GranularInventoryEventActionTypeEnumTest.java (22 lines)
│   │   │                   │   │   ├── GranularInventoryEventResultTest.java (49 lines)
│   │   │                   │   │   ├── LinkStatusGranularInventoryEventHandlerTest.java (307 lines)
│   │   │                   │   │   ├── ProcessorToFeatureListTest.java (84 lines)
│   │   │                   │   │   ├── RefreshInventoryObjectsWrapperTest.java (67 lines)
│   │   │                   │   │   ├── SyslogMsgInfoTest.java (84 lines)
│   │   │                   │   │   └── ThresholdEventFlowControllerTest.java (48 lines)
│   │   │                   │   ├── inventorymodel/
│   │   │                   │   │   ├── InterfaceServiceNioWrapperTest.java (780 lines)
│   │   │                   │   │   ├── LinkNIOWrapperTest.java (127 lines)
│   │   │                   │   │   ├── LocationNioWrapperTest.java (115 lines)
│   │   │                   │   │   └── NetworkDeviceNioWrapperTest.java (2619 lines)
│   │   │                   │   ├── inventoryservice/
│   │   │                   │   │   ├── dto/
│   │   │                   │   │   │   ├── CollectionStatusCountDTOListTest.java (27 lines)
│   │   │                   │   │   │   ├── InterfaceDTOTest.java (47 lines)
│   │   │                   │   │   │   ├── InvEquipmentDTOTest.java (45 lines)
│   │   │                   │   │   │   ├── InventoryDeviceItemDTOTest.java (24 lines)
│   │   │                   │   │   │   ├── InventoryDeviceSyncTaskDTOListTest.java (35 lines)
│   │   │                   │   │   │   ├── InventoryDeviceSyncTaskDTOTest.java (82 lines)
│   │   │                   │   │   │   ├── LagLinkDTOTest.java (47 lines)
│   │   │                   │   │   │   ├── LineChartItemsDTOTest.java (25 lines)
│   │   │                   │   │   │   ├── LineChartItemsListDTOTest.java (27 lines)
│   │   │                   │   │   │   ├── LineChartLabelsDTOTest.java (22 lines)
│   │   │                   │   │   │   ├── MemberInterfaceDTOTest.java (37 lines)
│   │   │                   │   │   │   ├── MemberLinkDetailsDTOTest.java (35 lines)
│   │   │                   │   │   │   ├── NewPortChannelDetailsDTOTest.java (55 lines)
│   │   │                   │   │   │   ├── NewPortChannelEndDTOTest.java (29 lines)
│   │   │                   │   │   │   ├── PortChannelDTOTest.java (24 lines)
│   │   │                   │   │   │   ├── ScheduleDeviceMaintenanceManagedStateDTOTest.java (28 lines)
│   │   │                   │   │   │   ├── VDCAllocatedCPUDTOTest.java (30 lines)
│   │   │                   │   │   │   ├── VPCDetailsDTOTest.java (45 lines)
│   │   │                   │   │   │   └── VirtualDomainDTO360Test.java (35 lines)
│   │   │                   │   │   ├── DeviceRetrievalCriteriaTest.java (58 lines)
│   │   │                   │   │   ├── DeviceTest.java (133 lines)
│   │   │                   │   │   ├── DistributedHealthUtilTest.java (71 lines)
│   │   │                   │   │   ├── FunctionalCapabilityEnumTest.java (19 lines)
│   │   │                   │   │   └── RetrievalCriteriaTest.java (46 lines)
│   │   │                   │   └── logger/
│   │   │                   │       └── IFMInventoryLoggerTest.java (74 lines)
│   │   │                   └── nms/
│   │   │                       ├── ce/
│   │   │                       │   └── event/
│   │   │                       │       └── correlation/
│   │   │                       │           └── FlappingEventsFlowControllerTest.java (130 lines)
│   │   │                       └── optical/
│   │   │                           └── event/
│   │   │                               └── correlation/
│   │   │                                   ├── BaseSubstringParserTest.java (22 lines)
│   │   │                                   ├── BurstEventFilterActionTest.java (50 lines)
│   │   │                                   ├── ComposeAndCompressPunctualEventFilterActionTest.java (192 lines)
│   │   │                                   ├── ComposeEventFilterActionTest.java (57 lines)
│   │   │                                   ├── ComposePunctualEventFilterActionTest.java (74 lines)
│   │   │                                   ├── CompositeEventTest.java (55 lines)
│   │   │                                   ├── CompressEventTypeFilterActionTest.java (56 lines)
│   │   │                                   ├── CompressPunctualEventTypeFilterActionTest.java (147 lines)
│   │   │                                   ├── DropEventFilterActionTest.java (50 lines)
│   │   │                                   ├── EventPatternConfigTest.java (13 lines)
│   │   │                                   ├── FSMElementTest.java (115 lines)
│   │   │                                   ├── FSMReportTest.java (21 lines)
│   │   │                                   ├── FSMTest.java (307 lines)
│   │   │                                   ├── FilterPatternFlowControllerTest.java (269 lines)
│   │   │                                   ├── IndexedEventInfoTest.java (93 lines)
│   │   │                                   ├── KeepOneFilterActionTest.java (53 lines)
│   │   │                                   ├── QueueObjectTest.java (38 lines)
│   │   │                                   └── SubstringParserFactoryTest.java (57 lines)
│   │   ├── .gitignore (4 lines)
│   │   ├── .project (23 lines)
│   │   ├── 1 (177 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── merge_0210_2014.txt (14 lines)
│   │   ├── merge_12_08.txt (9 lines)
│   │   ├── pom.xml (1019 lines)
│   │   └── release-pom.xml.save (2482 lines)
│   ├── ifm_inventory_ui_metadata_impl/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           └── ifm/
│   │   │   │   │               └── inventory/
│   │   │   │   │                   └── metadata/
│   │   │   │   │                       ├── devicePartHandler/
│   │   │   │   │                       │   ├── DWCMetadata.java (228 lines)
│   │   │   │   │                       │   ├── UIMetadataHandler.java (305 lines)
│   │   │   │   │                       │   └── UIMetadataProcessor.java (36 lines)
│   │   │   │   │                       ├── impl/
│   │   │   │   │                       │   ├── DWCHandler.java (179 lines)
│   │   │   │   │                       │   └── UIdataServiceImpl.java (78 lines)
│   │   │   │   │                       └── IMetadataHandler.java (23 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   └── spring/
│   │   │   │       │       └── inventory_op_context.xml (35 lines)
│   │   │   │       ├── storm/
│   │   │   │       │   └── TabViewMetadata.json (21 lines)
│   │   │   │       ├── DWCViewMetadata.json (46 lines)
│   │   │   │       ├── DeviceDetailTabViewMetadata.json (386 lines)
│   │   │   │       ├── TabViewMetadata.json (377 lines)
│   │   │   │       └── dwcMetadata.json (1 lines)
│   │   │   └── test/
│   │   │       └── java/
│   │   │           └── com/
│   │   │               └── cisco/
│   │   │                   └── ifm/
│   │   │                       └── inventory/
│   │   │                           └── metadata/
│   │   │                               ├── devicePartHandler/
│   │   │                               │   ├── DWCMetadataTest.java (229 lines)
│   │   │                               │   ├── UIMetadataHandlerTest.java (126 lines)
│   │   │                               │   ├── UIMetadataProcessorTest.java (64 lines)
│   │   │                               │   └── ifm_ui_metadata.xml (27 lines)
│   │   │                               └── impl/
│   │   │                                   ├── DWCHandlerTest.java (459 lines)
│   │   │                                   └── UIdataServiceImplTest.java (98 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   └── pom.xml (528 lines)
│   ├── ifm_inventory_xfn.xfn/
│   │   ├── src/
│   │   │   ├── META-INF/
│   │   │   │   └── MANIFEST.MF (2 lines)
│   │   │   └── com/
│   │   │       └── cisco/
│   │   │           └── nm/
│   │   │               └── xde/
│   │   │                   └── functions/
│   │   │                       ├── AuditLogFunction.java (169 lines)
│   │   │                       ├── DeviceManageabilityCheckFunction.java (86 lines)
│   │   │                       └── TemplateIdentifierFunction.java (202 lines)
│   │   ├── .project (29 lines)
│   │   ├── 1 (154 lines)
│   │   ├── addAuditLog.xde (19 lines)
│   │   ├── build.properties (4 lines)
│   │   ├── identifyConfiglet.xde (17 lines)
│   │   ├── isDeviceManageabilityEnabled.xde (13 lines)
│   │   ├── packageDescriptor.xml (11 lines)
│   │   ├── pom.xml (321 lines)
│   │   └── xmpxde.xml (274 lines)
│   ├── inventory_api/
│   │   ├── src/
│   │   │   └── main/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           └── xmp/
│   │   │       │               └── inventory/
│   │   │       │                   └── InventoryConstants.java (25 lines)
│   │   │       └── proto/
│   │   │           ├── Inventory.proto (112 lines)
│   │   │           └── InventoryCollectionNotification.proto (31 lines)
│   │   ├── .classpath (32 lines)
│   │   ├── .gitignore (1 lines)
│   │   ├── .project (23 lines)
│   │   └── pom.xml (471 lines)
│   ├── xmp_existence_inventory/
│   │   ├── .settings/
│   │   │   ├── org.eclipse.core.resources.prefs (6 lines)
│   │   │   ├── org.eclipse.jdt.core.prefs (8 lines)
│   │   │   ├── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   └── org.sonar.ide.eclipse.core.prefs (5 lines)
│   │   ├── EiTest/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.jdt.core.prefs (6 lines)
│   │   │   │   └── org.maven.ide.eclipse.prefs (9 lines)
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       ├── java/
│   │   │   │       │   └── com/
│   │   │   │       │       └── cisco/
│   │   │   │       │           └── xmp/
│   │   │   │       │               └── test/
│   │   │   │       │                   └── TestEI.java (71 lines)
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── spring/
│   │   │   │                   ├── module-context.xml (28 lines)
│   │   │   │                   └── osgi-context.xml (24 lines)
│   │   │   ├── .classpath (10 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── pom.xml (103 lines)
│   │   ├── src/
│   │   │   ├── docbkx/
│   │   │   │   ├── behavioral_view.xml (706 lines)
│   │   │   │   ├── book-existence-inventory-spec.xml (28 lines)
│   │   │   │   ├── index.xml (444 lines)
│   │   │   │   ├── packaging_implementation_view.xml (24 lines)
│   │   │   │   └── structural_view.xml (122 lines)
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           └── xmp/
│   │   │   │   │               └── existence/
│   │   │   │   │                   └── inventory/
│   │   │   │   │                       ├── credentials/
│   │   │   │   │                       │   └── CredentialsBridge.java (351 lines)
│   │   │   │   │                       ├── engine/
│   │   │   │   │                       │   ├── AbortCollectionManagerImpl.java (37 lines)
│   │   │   │   │                       │   ├── EITransactionSynchronizationHook.java (118 lines)
│   │   │   │   │                       │   ├── ExistenceInventoryImpl.java (1765 lines)
│   │   │   │   │                       │   ├── LifecycleManagerImpl.java (135 lines)
│   │   │   │   │                       │   └── ParallelInventoryDeleter.java (142 lines)
│   │   │   │   │                       ├── util/
│   │   │   │   │                       │   ├── DeleteNECallable.java (8 lines)
│   │   │   │   │                       │   ├── DeleteNETask.java (49 lines)
│   │   │   │   │                       │   ├── IpAddressUtil.java (97 lines)
│   │   │   │   │                       │   └── PersistenceUtil.java (87 lines)
│   │   │   │   │                       ├── AbortCollectionCallback.java (10 lines)
│   │   │   │   │                       ├── AbortCollectionManager.java (32 lines)
│   │   │   │   │                       ├── AddressException.java (48 lines)
│   │   │   │   │                       ├── Credentials.java (104 lines)
│   │   │   │   │                       ├── CredentialsException.java (50 lines)
│   │   │   │   │                       ├── EILogger.java (250 lines)
│   │   │   │   │                       ├── ExistenceInventory.java (707 lines)
│   │   │   │   │                       ├── ExistenceInventoryException.java (52 lines)
│   │   │   │   │                       ├── InvalidIdException.java (38 lines)
│   │   │   │   │                       ├── LifecycleCallback.java (68 lines)
│   │   │   │   │                       ├── LifecycleCallbackEnhanced.java (22 lines)
│   │   │   │   │                       ├── LifecycleManager.java (62 lines)
│   │   │   │   │                       ├── PersistenceException.java (36 lines)
│   │   │   │   │                       └── XmpCredentialProperties.java (376 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   └── spring/
│   │   │   │       │       ├── osgi-application-context.xml (30 lines)
│   │   │   │       │       └── xmp-existence-inventory-context.xml (93 lines)
│   │   │   │       ├── com/
│   │   │   │       │   └── cisco/
│   │   │   │       │       └── xmp/
│   │   │   │       │           └── logging/
│   │   │   │       │               └── inventory/
│   │   │   │       │                   └── msgs/
│   │   │   │       │                       ├── messages.properties (49 lines)
│   │   │   │       │                       └── messages.xml (530 lines)
│   │   │   │       ├── dcTest.txt (4 lines)
│   │   │   │       ├── existence-inventory-categories.xml (13 lines)
│   │   │   │       └── existence.properties (16 lines)
│   │   │   ├── site/
│   │   │   │   ├── apt.bak/
│   │   │   │   │   ├── behavioral_view.apt (448 lines)
│   │   │   │   │   ├── overview.apt (355 lines)
│   │   │   │   │   ├── packaging_implementation_view.apt (45 lines)
│   │   │   │   │   ├── rel-notes.apt (34 lines)
│   │   │   │   │   └── structural_view.apt (117 lines)
│   │   │   │   └── site.xml.bak (58 lines)
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           ├── randoop/
│   │   │       │           │   └── gen/
│   │   │       │           │       └── tests/
│   │   │       │           │           └── RegressionTest0.java (9187 lines)
│   │   │       │           └── xmp/
│   │   │       │               └── existence/
│   │   │       │                   └── inventory/
│   │   │       │                       ├── credentials/
│   │   │       │                       │   └── CredentialsBridgeTest.java (390 lines)
│   │   │       │                       ├── engine/
│   │   │       │                       │   ├── EITransactionSynchronizationHookTest.java (97 lines)
│   │   │       │                       │   ├── ExistenceInventoryImplTest.java (1599 lines)
│   │   │       │                       │   ├── LifecycleManagerImplTest.java (110 lines)
│   │   │       │                       │   ├── MockSemaphoreManager.java (93 lines)
│   │   │       │                       │   ├── ParallelInventoryDeleterTest.java (87 lines)
│   │   │       │                       │   ├── TestAbortCollectionManagerImpl.java (34 lines)
│   │   │       │                       │   └── TestParallelInventoryDeleter.java (40 lines)
│   │   │       │                       ├── util/
│   │   │       │                       │   ├── DeleteNETaskTest.java (57 lines)
│   │   │       │                       │   ├── IpAddressUtilTest.java (19 lines)
│   │   │       │                       │   └── PersistenceUtilTest.java (65 lines)
│   │   │       │                       ├── TestEILogger.java (79 lines)
│   │   │       │                       ├── TestExistenceInventory.java (744 lines)
│   │   │       │                       ├── TestIpAddressUtil.java (21 lines)
│   │   │       │                       ├── TestLifecycleManager.java (78 lines)
│   │   │       │                       ├── TestTransactionManager.java (30 lines)
│   │   │       │                       └── TestTransactionStatus.java (58 lines)
│   │   │       └── resources/
│   │   │           ├── conf/
│   │   │           │   └── credentialdictionary.txt (39 lines)
│   │   │           ├── props/
│   │   │           │   └── DMMException.properties (7 lines)
│   │   │           ├── DCMException.properties (6 lines)
│   │   │           └── persistence.properties (24 lines)
│   │   ├── .classpath (38 lines)
│   │   ├── .project (25 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── pom.xml (1247 lines)
│   │   ├── settings-rel.xml (111 lines)
│   │   ├── settings.xml (118 lines)
│   │   └── test_suite.xml (25 lines)
│   ├── xmp_grt/
│   │   ├── src/
│   │   │   ├── docbkx/
│   │   │   │   ├── spec/
│   │   │   │   │   └── META-INF/
│   │   │   │   │       └── MANIFEST.MF (7 lines)
│   │   │   │   ├── behavioral_view.xml (46 lines)
│   │   │   │   ├── book-grt-spec.xml (27 lines)
│   │   │   │   ├── index.xml (119 lines)
│   │   │   │   ├── packaging_implementation_view.xml (25 lines)
│   │   │   │   └── structural_view.xml (236 lines)
│   │   │   └── site/
│   │   │       └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   ├── xmp_grt_core/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.core.resources.prefs (6 lines)
│   │   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   ├── src/
│   │   │   │   ├── main/
│   │   │   │   │   ├── java/
│   │   │   │   │   │   └── com/
│   │   │   │   │   │       └── cisco/
│   │   │   │   │   │           └── xmp/
│   │   │   │   │   │               └── grt/
│   │   │   │   │   │                   ├── config/
│   │   │   │   │   │                   │   ├── GRTConfig.java (33 lines)
│   │   │   │   │   │                   │   ├── GRTConfigBean.java (32 lines)
│   │   │   │   │   │                   │   └── GRTConfigurationLoader.java (44 lines)
│   │   │   │   │   │                   ├── exception/
│   │   │   │   │   │                   │   ├── GRTErrorCode.java (35 lines)
│   │   │   │   │   │                   │   ├── GRTException.java (175 lines)
│   │   │   │   │   │                   │   ├── MessageCatalogue.java (139 lines)
│   │   │   │   │   │                   │   └── MessageException.java (75 lines)
│   │   │   │   │   │                   ├── impl/
│   │   │   │   │   │                   │   ├── FaultCorrelationHelperDAO.java (124 lines)
│   │   │   │   │   │                   │   ├── FaultCorrelationHelperImpl.java (178 lines)
│   │   │   │   │   │                   │   ├── FingerprintUtilityImpl.java (244 lines)
│   │   │   │   │   │                   │   ├── GRTFilterForTQEntries.java (58 lines)
│   │   │   │   │   │                   │   └── GRTServiceImpl.java (525 lines)
│   │   │   │   │   │                   ├── log/
│   │   │   │   │   │                   │   └── GRTLogger.java (149 lines)
│   │   │   │   │   │                   ├── timer/
│   │   │   │   │   │                   │   ├── GRTTimer.java (116 lines)
│   │   │   │   │   │                   │   ├── IGRTTimer.java (18 lines)
│   │   │   │   │   │                   │   ├── TransactionQueueGRTProcessor.java (34 lines)
│   │   │   │   │   │                   │   └── TransactionQueueGRTProcessorImpl.java (366 lines)
│   │   │   │   │   │                   ├── IFaultCorrelationHelper.java (43 lines)
│   │   │   │   │   │                   ├── IFingerprintUtility.java (138 lines)
│   │   │   │   │   │                   └── IGRTService.java (297 lines)
│   │   │   │   │   └── resources/
│   │   │   │   │       ├── META-INF/
│   │   │   │   │       │   └── spring/
│   │   │   │   │       │       └── xmp-grt-spring-context.xml (89 lines)
│   │   │   │   │       ├── com/
│   │   │   │   │       │   └── cisco/
│   │   │   │   │       │       └── xmp/
│   │   │   │   │       │           └── grt/
│   │   │   │   │       │               └── logging/
│   │   │   │   │       │                   └── config/
│   │   │   │   │       │                       ├── GRTLogMsgs.properties (6 lines)
│   │   │   │   │       │                       └── GRTLogMsgs.xml (48 lines)
│   │   │   │   │       ├── GRTException.properties (15 lines)
│   │   │   │   │       ├── GRTLog4jConfig.xml (44 lines)
│   │   │   │   │       └── grt-log4j-categories.xml (13 lines)
│   │   │   │   ├── site/
│   │   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │   └── test/
│   │   │   │       ├── java/
│   │   │   │       │   └── com/
│   │   │   │       │       └── cisco/
│   │   │   │       │           └── xmp/
│   │   │   │       │               └── grt/
│   │   │   │       │                   ├── config/
│   │   │   │       │                   │   └── GRTConfigurationLoaderTest.java (121 lines)
│   │   │   │       │                   ├── exception/
│   │   │   │       │                   │   └── ExceptionTest.java (120 lines)
│   │   │   │       │                   ├── impl/
│   │   │   │       │                   │   ├── FaultCorrelationHelperDAOTest.java (145 lines)
│   │   │   │       │                   │   ├── FaultCorrelationHelperImplTest.java (141 lines)
│   │   │   │       │                   │   ├── FingerprintUtilityImplTest.java (261 lines)
│   │   │   │       │                   │   ├── GRTFilterForTQEntriesTest.java (56 lines)
│   │   │   │       │                   │   └── GRTServiceImplTest.java (384 lines)
│   │   │   │       │                   ├── log/
│   │   │   │       │                   │   └── GRTLoggerTest.java (88 lines)
│   │   │   │       │                   ├── timer/
│   │   │   │       │                   │   ├── GRTTimerTest.java (179 lines)
│   │   │   │       │                   │   └── TransactionQueueGRTProcessorImplTest.java (335 lines)
│   │   │   │       │                   ├── FaultCorrelationTests.java (199 lines)
│   │   │   │       │                   └── GRTServiceTests.java (1477 lines)
│   │   │   │       └── resources/
│   │   │   │           └── suites/
│   │   │   │               └── GRTTestSuite.xml (23 lines)
│   │   │   ├── .classpath (36 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── pom.xml (389 lines)
│   │   ├── xmp_grt_model/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.core.resources.prefs (4 lines)
│   │   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   ├── mapping/
│   │   │   │   └── hibernate/
│   │   │   │       └── com/
│   │   │   │           └── cisco/
│   │   │   │               └── xmp/
│   │   │   │                   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── src/
│   │   │   │   ├── main/
│   │   │   │   │   ├── java/
│   │   │   │   │   │   └── com/
│   │   │   │   │   │       └── cisco/
│   │   │   │   │   │           └── xmp/
│   │   │   │   │   │               └── grt/
│   │   │   │   │   │                   └── model/
│   │   │   │   │   │                       ├── GlobalRefAltKeys.java (114 lines)
│   │   │   │   │   │                       └── GlobalReference.java (168 lines)
│   │   │   │   │   └── resources/
│   │   │   │   │       └── mapping/
│   │   │   │   │           └── hibernate/
│   │   │   │   │               └── xmp_grt_model/
│   │   │   │   │                   ├── GlobalRefAltKeys.hbm.xml (60 lines)
│   │   │   │   │                   ├── GlobalReference.hbm.xml (41 lines)
│   │   │   │   │                   └── grt_named_queries.hbm.xml (275 lines)
│   │   │   │   ├── site/
│   │   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │   └── test/
│   │   │   │       ├── java/
│   │   │   │       │   └── com/
│   │   │   │       │       └── cisco/
│   │   │   │       │           └── xmp/
│   │   │   │       │               └── grt/
│   │   │   │       │                   └── model/
│   │   │   │       │                       ├── GlobalRefAltKeysTest.java (73 lines)
│   │   │   │       │                       └── GlobalReferenceTest.java (136 lines)
│   │   │   │       ├── resources/
│   │   │   │       │   └── suites/
│   │   │   │       │       └── GRTModelTestSuite.xml (15 lines)
│   │   │   │       └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (24 lines)
│   │   │   ├── pom.xml (184 lines)
│   │   │   └── suite.xml (19 lines)
│   │   ├── .project (17 lines)
│   │   ├── README-SVN-to-GIT (3 lines)
│   │   ├── pom.xml (554 lines)
│   │   ├── settings-rel.xml (111 lines)
│   │   └── settings.xml (118 lines)
│   ├── xmp_ice_job_adaptor/
│   │   ├── .settings/
│   │   │   ├── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── org.eclipse.core.resources.prefs (4 lines)
│   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           └── xmp/
│   │   │   │   │               └── inventory/
│   │   │   │   │                   ├── adaptors/
│   │   │   │   │                   │   ├── InventoryCollectorJobServiceImpl.java (667 lines)
│   │   │   │   │                   │   ├── InventoryCollectorJobServiceInf.java (100 lines)
│   │   │   │   │                   │   └── JobManagementLifecycleAdaptor.java (83 lines)
│   │   │   │   │                   ├── ice/
│   │   │   │   │                   │   ├── job/
│   │   │   │   │                   │   │   ├── InventoryCollectionJob.java (1140 lines)
│   │   │   │   │                   │   │   └── InventoryFailedFeatureCollector.java (466 lines)
│   │   │   │   │                   │   └── MEIPreDeleteHandler.java (78 lines)
│   │   │   │   │                   └── postStart/
│   │   │   │   │                       └── IcePostInitHookImpl.java (152 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── META-INF/
│   │   │   │       │   └── spring/
│   │   │   │       │       ├── ice-job-module-context.xml (155 lines)
│   │   │   │       │       ├── ice-job-osgi-context.xml (33 lines)
│   │   │   │       │       └── xmp-ice-job-adaptor-context.xml (21 lines)
│   │   │   │       ├── collector_categories.xml (14 lines)
│   │   │   │       └── collector_log4j.xml (19 lines)
│   │   │   ├── site/
│   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   └── test/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           └── xmp/
│   │   │       │               └── inventory/
│   │   │       │                   ├── adaptors/
│   │   │       │                   │   ├── InventoryCollectorJobServiceImplTest.java (252 lines)
│   │   │       │                   │   └── JobManagementLifecycleAdaptorTest.java (75 lines)
│   │   │       │                   ├── ice/
│   │   │       │                   │   ├── job/
│   │   │       │                   │   │   └── InventoryFailedFeatureCollectorTest.java (414 lines)
│   │   │       │                   │   └── MEIPreDeleteHandlerTest.java (100 lines)
│   │   │       │                   ├── job/
│   │   │       │                   │   ├── InventoryCollectionJobTest.java (927 lines)
│   │   │       │                   │   └── SessionStub.java (889 lines)
│   │   │       │                   └── postStart/
│   │   │       │                       └── IcePostInitHookImplTest.java (143 lines)
│   │   │       └── resources/
│   │   │           ├── ifm_inventory.properties (31 lines)
│   │   │           └── queries.properties (5 lines)
│   │   ├── .classpath (31 lines)
│   │   ├── .project (24 lines)
│   │   ├── README-SVN-to-GIT (1 lines)
│   │   ├── pom.xml (1058 lines)
│   │   ├── settings-rel.xml (111 lines)
│   │   ├── settings.xml (118 lines)
│   │   └── test_suite.xml (23 lines)
│   ├── xmp_inventory/
│   │   ├── .settings/
│   │   │   ├── org.eclipse.core.resources.prefs (2 lines)
│   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   ├── ClearSessionCache/
│   │   │   ├── clearCache/
│   │   │   │   ├── clearCache.par (352 lines)
│   │   │   │   ├── clearCacheParserOutput.xsd (6 lines)
│   │   │   │   ├── clearCacheParser_xdeACSW.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeASASW.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeASR5K.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeCATOS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeDEFAULT.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeIOS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeIOS_EXR.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeIOS_XR.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeME1200_OS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeNAM.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeNX-OS-UCSM.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeNX-OS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeONS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeSCOS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeSG500_OS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeUCOS.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeUNIX.rpl (3 lines)
│   │   │   │   ├── clearCacheParser_xdeWAAS.rpl (3 lines)
│   │   │   │   └── clearCacheParser_xdeWLC.rpl (3 lines)
│   │   │   ├── test/
│   │   │   │   ├── emptyParamTest.xft (22 lines)
│   │   │   │   ├── oneParamTest.xft (29 lines)
│   │   │   │   └── preProcedureTest.xft (33 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── postProcedure.xde (31 lines)
│   │   │   ├── preProcedure.xde (62 lines)
│   │   │   ├── procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (32 lines)
│   │   ├── src/
│   │   │   └── site/
│   │   │       └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   ├── xmp_collector/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.core.resources.prefs (7 lines)
│   │   │   │   ├── org.eclipse.jdt.core.prefs (14 lines)
│   │   │   │   ├── org.eclipse.m2e.core.prefs (5 lines)
│   │   │   │   └── org.sonar.ide.eclipse.core.prefs (5 lines)
│   │   │   ├── pal-home/
│   │   │   │   ├── conf/
│   │   │   │   │   ├── inventory.properties (1 lines)
│   │   │   │   │   ├── log4j.properties (7 lines)
│   │   │   │   │   └── pal.properties (6 lines)
│   │   │   │   └── packages/
│   │   │   │       └── site/
│   │   │   │           └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── src/
│   │   │   │   ├── main/
│   │   │   │   │   ├── java/
│   │   │   │   │   │   └── com/
│   │   │   │   │   │       └── cisco/
│   │   │   │   │   │           └── xmp/
│   │   │   │   │   │               ├── device/
│   │   │   │   │   │               │   └── tools/
│   │   │   │   │   │               │       ├── DatabaseDiagnosticsImpl.java (1018 lines)
│   │   │   │   │   │               │       ├── FingerprintCacheNoSingleton.java (1529 lines)
│   │   │   │   │   │               │       ├── GeneratedPojoCacheNoSingleton.java (1530 lines)
│   │   │   │   │   │               │       └── ModelApiAssociationBuilderNoCache.java (1127 lines)
│   │   │   │   │   │               ├── deviceaccess/
│   │   │   │   │   │               │   ├── businessProcessor/
│   │   │   │   │   │               │   │   ├── BusinessProcessManager.java (182 lines)
│   │   │   │   │   │               │   │   └── BusinessProcessorRegistry.java (158 lines)
│   │   │   │   │   │               │   ├── impl/
│   │   │   │   │   │               │   │   ├── ActionRegistryImpl.java (57 lines)
│   │   │   │   │   │               │   │   ├── DeviceAccessServiceImpl.java (331 lines)
│   │   │   │   │   │               │   │   └── PalAdaptorImpl.java (58 lines)
│   │   │   │   │   │               │   ├── ActionNotFoundException.java (37 lines)
│   │   │   │   │   │               │   ├── DeviceInteractionException.java (38 lines)
│   │   │   │   │   │               │   ├── NonUniqueResponseException.java (39 lines)
│   │   │   │   │   │               │   ├── NotSupportedException.java (35 lines)
│   │   │   │   │   │               │   └── UnexpectedResponseException.java (57 lines)
│   │   │   │   │   │               └── inventory/
│   │   │   │   │   │                   ├── adaptors/
│   │   │   │   │   │                   │   ├── InventoryCollectionLifecycleAdaptor.java (390 lines)
│   │   │   │   │   │                   │   └── InventoryCollectionSyncronization.java (62 lines)
│   │   │   │   │   │                   ├── appContext/
│   │   │   │   │   │                   │   └── ICEApplicationContext.java (58 lines)
│   │   │   │   │   │                   ├── associationBuilder/
│   │   │   │   │   │                   │   ├── AbstractAssociationBuilder.java (27 lines)
│   │   │   │   │   │                   │   ├── AssociationBuilderTesterUtil.java (227 lines)
│   │   │   │   │   │                   │   ├── AssociationBuilderUtil.java (1262 lines)
│   │   │   │   │   │                   │   ├── CacheLookupBasedAssociationBuilder.java (524 lines)
│   │   │   │   │   │                   │   ├── ModelAPIBasedAssociationBuilder.java (1314 lines)
│   │   │   │   │   │                   │   └── SortByObjectCreationOrder.java (31 lines)
│   │   │   │   │   │                   ├── cache/
│   │   │   │   │   │                   │   └── ICESmartCacheImpl.java (804 lines)
│   │   │   │   │   │                   ├── credentials/
│   │   │   │   │   │                   │   ├── CredentialManagerFactory.java (51 lines)
│   │   │   │   │   │                   │   └── DCMInventoryProvider.java (468 lines)
│   │   │   │   │   │                   ├── cw/
│   │   │   │   │   │                   │   └── connector/
│   │   │   │   │   │                   │       └── InvKafkaConnectorManager.java (21 lines)
│   │   │   │   │   │                   ├── diffEngine/
│   │   │   │   │   │                   │   ├── DifferenceEngineImpl.java (402 lines)
│   │   │   │   │   │                   │   ├── FingerprintCache.java (1895 lines)
│   │   │   │   │   │                   │   └── FingerprintUtilityImpl.java (194 lines)
│   │   │   │   │   │                   ├── events/
│   │   │   │   │   │                   │   ├── AlterObjectGraphCallback.java (106 lines)
│   │   │   │   │   │                   │   ├── GraphObjectsCollectedCallback.java (140 lines)
│   │   │   │   │   │                   │   ├── IceEvent.java (46 lines)
│   │   │   │   │   │                   │   ├── IceObjectGraphEvent.java (155 lines)
│   │   │   │   │   │                   │   ├── IceObjectGraphListener.java (36 lines)
│   │   │   │   │   │                   │   └── UnmodifiableGraphException.java (38 lines)
│   │   │   │   │   │                   ├── exception/
│   │   │   │   │   │                   │   └── IceSparseException.java (27 lines)
│   │   │   │   │   │                   ├── grpc/
│   │   │   │   │   │                   │   ├── GRPCConnectivityException.java (24 lines)
│   │   │   │   │   │                   │   ├── GrpcConstants.java (34 lines)
│   │   │   │   │   │                   │   ├── GrpcLeaderElectorHooks.java (35 lines)
│   │   │   │   │   │                   │   ├── GrpcUtil.java (242 lines)
│   │   │   │   │   │                   │   ├── InventoryGrpcClient.java (253 lines)
│   │   │   │   │   │                   │   └── InventoryGrpcServer.java (173 lines)
│   │   │   │   │   │                   ├── http/
│   │   │   │   │   │                   │   ├── HttpConstants.java (22 lines)
│   │   │   │   │   │                   │   ├── HttpUtil.java (35 lines)
│   │   │   │   │   │                   │   └── InventoryHttpClient.java (118 lines)
│   │   │   │   │   │                   ├── ice/
│   │   │   │   │   │                   │   ├── cdg/
│   │   │   │   │   │                   │   │   ├── dispatcher/
│   │   │   │   │   │                   │   │   │   └── CDGResponseDispatcher.java (372 lines)
│   │   │   │   │   │                   │   │   ├── handler/
│   │   │   │   │   │                   │   │   │   ├── CollectionJobControlStatusHandler.java (45 lines)
│   │   │   │   │   │                   │   │   │   ├── CollectionJobResultListener.java (418 lines)
│   │   │   │   │   │                   │   │   │   ├── CollectionJobStatusHandler.java (57 lines)
│   │   │   │   │   │                   │   │   │   ├── GNMIResponseParser.java (1042 lines)
│   │   │   │   │   │                   │   │   │   ├── HeliosNotificationListener.java (167 lines)
│   │   │   │   │   │                   │   │   │   └── SatelliteResponseParser.java (457 lines)
│   │   │   │   │   │                   │   │   └── service/
│   │   │   │   │   │                   │   │       ├── CDGCollectionCallBackService.java (33 lines)
│   │   │   │   │   │                   │   │       ├── CDGCollectionJobCallback.java (14 lines)
│   │   │   │   │   │                   │   │       ├── CDGCollectionService.java (850 lines)
│   │   │   │   │   │                   │   │       ├── CDGConstants.java (144 lines)
│   │   │   │   │   │                   │   │       ├── CDGMultiCollectionJobCallback.java (13 lines)
│   │   │   │   │   │                   │   │       ├── CDGRequestData.java (62 lines)
│   │   │   │   │   │                   │   │       └── CDGResponseData.java (64 lines)
│   │   │   │   │   │                   │   ├── collectortask/
│   │   │   │   │   │                   │   │   ├── CollectorCDGFeatureTask.java (427 lines)
│   │   │   │   │   │                   │   │   ├── CollectorFeatureHookTask.java (233 lines)
│   │   │   │   │   │                   │   │   ├── CollectorFeatureTask.java (874 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTask.java (218 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskAcquireLock.java (79 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskBootstrapConnectivity.java (180 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskBootstrapExecute.java (397 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskCDGExecuteDevicePackages.java (860 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskCallback.java (12 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskConnectivityCheck.java (512 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskExecuteDevicePackages.java (989 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskManageabilityConfig.java (72 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPostAcquireDeviceLock.java (162 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPostAcquireDeviceLockFailed.java (20 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPostCollection.java (19 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPostDPExecute.java (87 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPreDPExecute.java (95 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskPunctualUpdate.java (23 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskStart.java (15 lines)
│   │   │   │   │   │                   │   │   ├── CollectorTaskUpdateCollectionContext.java (63 lines)
│   │   │   │   │   │                   │   │   └── LirRigiHelper.java (452 lines)
│   │   │   │   │   │                   │   ├── dlm/
│   │   │   │   │   │                   │   │   └── handler/
│   │   │   │   │   │                   │   │       └── DlmInvMgrRequestHandler.java (108 lines)
│   │   │   │   │   │                   │   ├── feature/
│   │   │   │   │   │                   │   │   ├── AttributeBasedCriteria.java (167 lines)
│   │   │   │   │   │                   │   │   ├── Criteria.java (27 lines)
│   │   │   │   │   │                   │   │   ├── CriteriaObject.java (48 lines)
│   │   │   │   │   │                   │   │   ├── FeatureCheck.java (167 lines)
│   │   │   │   │   │                   │   │   ├── FeatureRunResult.java (157 lines)
│   │   │   │   │   │                   │   │   ├── HookBasedCriteria.java (46 lines)
│   │   │   │   │   │                   │   │   └── ObjectBasedCriteria.java (135 lines)
│   │   │   │   │   │                   │   ├── results/
│   │   │   │   │   │                   │   │   └── CollectionResultsHelper.java (86 lines)
│   │   │   │   │   │                   │   ├── startup/
│   │   │   │   │   │                   │   │   ├── CheckCollectorSyncStateHook.java (204 lines)
│   │   │   │   │   │                   │   │   ├── CheckLifeCycleStatePostInitHook.java (484 lines)
│   │   │   │   │   │                   │   │   └── SchedulingStartupHook.java (181 lines)
│   │   │   │   │   │                   │   ├── AbortException.java (33 lines)
│   │   │   │   │   │                   │   ├── AlarmClientConstants.java (35 lines)
│   │   │   │   │   │                   │   ├── AuditLoggingUtil.java (72 lines)
│   │   │   │   │   │                   │   ├── CollectionContext.java (23 lines)
│   │   │   │   │   │                   │   ├── CollectionPolicyContextWrapper.java (294 lines)
│   │   │   │   │   │                   │   ├── CollectionPolicyWrapper.java (42 lines)
│   │   │   │   │   │                   │   ├── CollectionRequest.java (182 lines)
│   │   │   │   │   │                   │   ├── CollectionResponse.java (124 lines)
│   │   │   │   │   │                   │   ├── DeviceSchedulingHookImpl.java (584 lines)
│   │   │   │   │   │                   │   ├── DeviceSyncRequestDistrCache.java (536 lines)
│   │   │   │   │   │                   │   ├── DummyInventoryCollectorStatsLogger.java (35 lines)
│   │   │   │   │   │                   │   ├── ICETransactionSynchronizationHook.java (534 lines)
│   │   │   │   │   │                   │   ├── IceCollectorTaskImpl.java (776 lines)
│   │   │   │   │   │                   │   ├── IceCollectorTaskScheduler.java (136 lines)
│   │   │   │   │   │                   │   ├── IceExternalApplicationSampleImpl.java (57 lines)
│   │   │   │   │   │                   │   ├── IcePojoGenerationException.java (92 lines)
│   │   │   │   │   │                   │   ├── IceTaskImpl.java (1218 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectionAbortService.java (11 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectionAbortServiceImpl.java (132 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorAbortMessageHandler.java (87 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorEngineServiceImpl.java (3233 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorEngineXdeImpl.java (6062 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorExecutorCustom.java (37 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorExecutorImpl.java (573 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorExecutorPool.java (117 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorFactory.java (119 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorLoggingUtil.java (205 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorStatsLoggerImpl.java (87 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorSyncMessageHandler.java (132 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorUtil.java (60 lines)
│   │   │   │   │   │                   │   ├── InventoryFeaturePollerTask.java (557 lines)
│   │   │   │   │   │                   │   ├── InventoryMessageHandler.java (459 lines)
│   │   │   │   │   │                   │   └── Utilities.java (246 lines)
│   │   │   │   │   │                   ├── persistence/
│   │   │   │   │   │                   │   ├── ICEDao.java (458 lines)
│   │   │   │   │   │                   │   ├── ICEDaoIntf.java (151 lines)
│   │   │   │   │   │                   │   └── PersistenceFactoryBean.java (84 lines)
│   │   │   │   │   │                   ├── pojogen/
│   │   │   │   │   │                   │   ├── GeneratedPojoCache.java (2239 lines)
│   │   │   │   │   │                   │   ├── ICEMetadataParser.java (457 lines)
│   │   │   │   │   │                   │   ├── ObjectDefinitionCache.java (188 lines)
│   │   │   │   │   │                   │   └── PalXMLToPOJOConvertor.java (891 lines)
│   │   │   │   │   │                   ├── profile/
│   │   │   │   │   │                   │   └── DeviceProfileUtilities.java (630 lines)
│   │   │   │   │   │                   └── util/
│   │   │   │   │   │                       ├── CollectorCacheUtil.java (87 lines)
│   │   │   │   │   │                       ├── CollectorConstants.java (57 lines)
│   │   │   │   │   │                       ├── CommandStatisticsCollectorImpl.java (127 lines)
│   │   │   │   │   │                       ├── CommandStatisticsImpl.java (158 lines)
│   │   │   │   │   │                       ├── DistributedCacheRWUtil.java (46 lines)
│   │   │   │   │   │                       ├── GNMIResponseLogger.java (73 lines)
│   │   │   │   │   │                       ├── GlobalFilterUtil.java (815 lines)
│   │   │   │   │   │                       ├── IOSXRVersionChecker.java (80 lines)
│   │   │   │   │   │                       ├── InventoryParserUtilImpl.java (299 lines)
│   │   │   │   │   │                       ├── InventoryStatisticsCollectorImpl.java (345 lines)
│   │   │   │   │   │                       ├── InventoryStatisticsImpl.java (434 lines)
│   │   │   │   │   │                       ├── InventoryStatisticsSummary.java (12 lines)
│   │   │   │   │   │                       ├── InventoryUtilImpl.java (145 lines)
│   │   │   │   │   │                       ├── MCEPreDeleteHandler.java (66 lines)
│   │   │   │   │   │                       ├── ServerHostKeyVerifierProviderImpl.java (178 lines)
│   │   │   │   │   │                       ├── SystemPreferenceUtil.java (122 lines)
│   │   │   │   │   │                       ├── XMPInventoryConstantsUtil.java (181 lines)
│   │   │   │   │   │                       └── XMPInventoryMEICallBackHook.java (69 lines)
│   │   │   │   │   └── resources/
│   │   │   │   │       ├── BaseInventoryActions/
│   │   │   │   │       │   ├── BaseInterface/
│   │   │   │   │       │   │   ├── getifTable.par (27 lines)
│   │   │   │   │       │   │   ├── getifTableOutput.xsd (303 lines)
│   │   │   │   │       │   │   ├── getifXTable.par (25 lines)
│   │   │   │   │       │   │   └── getifXTableOutput.xsd (297 lines)
│   │   │   │   │       │   ├── GlobalDeviceInformation/
│   │   │   │   │       │   │   ├── getsysContact.par (27 lines)
│   │   │   │   │       │   │   ├── getsysContactOutput.xsd (20 lines)
│   │   │   │   │       │   │   ├── getsysDescr.par (27 lines)
│   │   │   │   │       │   │   ├── getsysDescrOutput.xsd (20 lines)
│   │   │   │   │       │   │   ├── getsysLocation.par (27 lines)
│   │   │   │   │       │   │   ├── getsysLocationOutput.xsd (19 lines)
│   │   │   │   │       │   │   ├── getsysName.par (27 lines)
│   │   │   │   │       │   │   ├── getsysNameOutput.xsd (20 lines)
│   │   │   │   │       │   │   ├── getsysObjectID.par (27 lines)
│   │   │   │   │       │   │   └── getsysObjectIDOutput.xsd (25 lines)
│   │   │   │   │       │   ├── InterfaceBinding/
│   │   │   │   │       │   │   ├── getifStackEntry.par (30 lines)
│   │   │   │   │       │   │   └── getifStackEntryOutput.xsd (54 lines)
│   │   │   │   │       │   ├── PhysicalStructure/
│   │   │   │   │       │   │   ├── getentPhysicalTable.par (25 lines)
│   │   │   │   │       │   │   └── getentPhysicalTableOutput.xsd (394 lines)
│   │   │   │   │       │   └── .project (12 lines)
│   │   │   │   │       ├── META-INF/
│   │   │   │   │       │   └── spring/
│   │   │   │   │       │       ├── assembly-module-context.xml (21 lines)
│   │   │   │   │       │       ├── assembly-osgi-context.xml (26 lines)
│   │   │   │   │       │       ├── das-module-context.xml (26 lines)
│   │   │   │   │       │       ├── das-osgi-context.xml (23 lines)
│   │   │   │   │       │       ├── device-scheduling-context.xml (121 lines)
│   │   │   │   │       │       ├── ice-module-context.xml (264 lines)
│   │   │   │   │       │       ├── ice-osgi-context.xml (33 lines)
│   │   │   │   │       │       └── xmp-inventory-context.xml (23 lines)
│   │   │   │   │       ├── com/
│   │   │   │   │       │   └── cisco/
│   │   │   │   │       │       └── xmp/
│   │   │   │   │       │           ├── deviceaccess/
│   │   │   │   │       │           │   ├── exception.properties (17 lines)
│   │   │   │   │       │           │   ├── messages.properties (13 lines)
│   │   │   │   │       │           │   └── messages.xml (50 lines)
│   │   │   │   │       │           └── inventory/
│   │   │   │   │       │               └── ice/
│   │   │   │   │       │                   └── msg/
│   │   │   │   │       │                       ├── errors_en_US.properties (39 lines)
│   │   │   │   │       │                       ├── messages.properties (48 lines)
│   │   │   │   │       │                       ├── messages.xml (272 lines)
│   │   │   │   │       │                       └── messages_en_US.properties (47 lines)
│   │   │   │   │       ├── collector_categories.xml (20 lines)
│   │   │   │   │       └── xde_categories.xml (23 lines)
│   │   │   │   ├── site/
│   │   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │   └── test/
│   │   │   │       ├── java/
│   │   │   │       │   └── com/
│   │   │   │       │       └── cisco/
│   │   │   │       │           └── xmp/
│   │   │   │       │               ├── device/
│   │   │   │       │               │   └── tools/
│   │   │   │       │               │       ├── DatabaseDiagnosticsImplTest.java (1286 lines)
│   │   │   │       │               │       ├── FingerprintCacheNoSingletonTest.java (1224 lines)
│   │   │   │       │               │       ├── GeneratedPojoCacheNoSingletonTest.java (1338 lines)
│   │   │   │       │               │       └── ModelApiAssociationBuilderNoCacheTest.java (1044 lines)
│   │   │   │       │               ├── deviceaccess/
│   │   │   │       │               │   ├── businessProcessor/
│   │   │   │       │               │   │   ├── BusinessProcessHookIntfTestStub.java (15 lines)
│   │   │   │       │               │   │   ├── BusinessProcessManagerTest.java (107 lines)
│   │   │   │       │               │   │   └── BusinessProcessorRegistryTest.java (98 lines)
│   │   │   │       │               │   ├── impl/
│   │   │   │       │               │   │   ├── ActionRegistryImplTest.java (28 lines)
│   │   │   │       │               │   │   ├── DeviceAccessServiceImplTest.java (444 lines)
│   │   │   │       │               │   │   └── PalAdaptorImplTest.java (56 lines)
│   │   │   │       │               │   ├── ActionNotFoundExceptionTest.java (16 lines)
│   │   │   │       │               │   ├── DeviceInteractionExceptionTest.java (16 lines)
│   │   │   │       │               │   ├── NonUniqueResponseExceptionTest.java (17 lines)
│   │   │   │       │               │   ├── NotSupportedExceptionTest.java (17 lines)
│   │   │   │       │               │   ├── TestDeviceAccess.java (350 lines)
│   │   │   │       │               │   └── UnexpectedResponseExceptionTest.java (17 lines)
│   │   │   │       │               └── inventory/
│   │   │   │       │                   ├── adaptors/
│   │   │   │       │                   │   ├── InventoryCollectionLifecycleAdaptorTest.java (522 lines)
│   │   │   │       │                   │   └── InventoryCollectionSyncronizationTest.java (96 lines)
│   │   │   │       │                   ├── associationBuilder/
│   │   │   │       │                   │   ├── test/
│   │   │   │       │                   │   │   ├── AssociationBuilderTest.java (457 lines)
│   │   │   │       │                   │   │   └── ICETester.java (805 lines)
│   │   │   │       │                   │   ├── AbstractAssociationBuilderTest.java (89 lines)
│   │   │   │       │                   │   ├── AssociationBuilderTesterUtilTest.java (130 lines)
│   │   │   │       │                   │   ├── AssociationBuilderUtilTest.java (964 lines)
│   │   │   │       │                   │   ├── CacheLookupBasedAssociationBuilderTest.java (630 lines)
│   │   │   │       │                   │   ├── ModelAPIBasedAssociationBuilderTest.java (1268 lines)
│   │   │   │       │                   │   ├── PostCollectionPersistHookStubTest.java (19 lines)
│   │   │   │       │                   │   ├── PostCollectionPersistHookStubTest2.java (19 lines)
│   │   │   │       │                   │   ├── SortByObjectCreationOrderTest.java (34 lines)
│   │   │   │       │                   │   ├── ValueObjectBaseImpl.java (46 lines)
│   │   │   │       │                   │   └── populateFieldsImplTest.java (103 lines)
│   │   │   │       │                   ├── cache/
│   │   │   │       │                   │   └── ICESmartCacheImplTest.java (821 lines)
│   │   │   │       │                   ├── connectivity/
│   │   │   │       │                   │   └── sample/
│   │   │   │       │                   │       ├── BootstrapConnectivityCheckFailureNotification.java (39 lines)
│   │   │   │       │                   │       └── DevicePackageConnectivityCheckFailureNotification.java (40 lines)
│   │   │   │       │                   ├── credentials/
│   │   │   │       │                   │   ├── CredentialMgrFactoryTest.java (33 lines)
│   │   │   │       │                   │   ├── DCMInventoryProviderTest.java (305 lines)
│   │   │   │       │                   │   ├── DCMPALIntegrationTest.java (242 lines)
│   │   │   │       │                   │   └── StubCredentialManager.java (58 lines)
│   │   │   │       │                   ├── device/
│   │   │   │       │                   │   └── pal/
│   │   │   │       │                   │       └── PALCommand.java (93 lines)
│   │   │   │       │                   ├── diffEngine/
│   │   │   │       │                   │   ├── test/
│   │   │   │       │                   │   │   └── FingerprintCacheTest.java (181 lines)
│   │   │   │       │                   │   ├── DifferenceEngineImplTest.java (405 lines)
│   │   │   │       │                   │   ├── DifferenceEngineTest.java (94 lines)
│   │   │   │       │                   │   ├── FingerprintCacheIntfDummyImpl.java (289 lines)
│   │   │   │       │                   │   ├── FingerprintCacheTest.java (1390 lines)
│   │   │   │       │                   │   ├── FingerprintUtilityImplTest.java (351 lines)
│   │   │   │       │                   │   ├── MockNativeQuery.java (788 lines)
│   │   │   │       │                   │   ├── MockPersistenceFactory.java (128 lines)
│   │   │   │       │                   │   ├── MockSQLQuery.java (959 lines)
│   │   │   │       │                   │   ├── MockSession.java (923 lines)
│   │   │   │       │                   │   └── MockSessionFactory.java (257 lines)
│   │   │   │       │                   ├── events/
│   │   │   │       │                   │   ├── GraphObjectsCollectedCallbackTest.java (97 lines)
│   │   │   │       │                   │   ├── IceEventTest.java (21 lines)
│   │   │   │       │                   │   └── IceObjectGraphEventTest.java (57 lines)
│   │   │   │       │                   ├── exception/
│   │   │   │       │                   │   └── IceSparseExceptionTest.java (20 lines)
│   │   │   │       │                   ├── grpc/
│   │   │   │       │                   │   ├── GrpcConstantsTest.java (98 lines)
│   │   │   │       │                   │   ├── GrpcLeaderElectorHooksTest.java (169 lines)
│   │   │   │       │                   │   ├── GrpcUtilTest.java (533 lines)
│   │   │   │       │                   │   ├── InventoryGrpcClientTest.java (461 lines)
│   │   │   │       │                   │   └── InventoryGrpcServerTest.java (325 lines)
│   │   │   │       │                   ├── hooks/
│   │   │   │       │                   │   └── NetworkNotificationHook.java (34 lines)
│   │   │   │       │                   ├── http/
│   │   │   │       │                   │   ├── HttpUtilTest.java (79 lines)
│   │   │   │       │                   │   └── InventoryHttpClientTest.java (131 lines)
│   │   │   │       │                   ├── ice/
│   │   │   │       │                   │   ├── cdg/
│   │   │   │       │                   │   │   ├── dispatcher/
│   │   │   │       │                   │   │   │   └── CDGResponseDispatcherTest.java (182 lines)
│   │   │   │       │                   │   │   ├── handler/
│   │   │   │       │                   │   │   │   ├── CollectionJobControlStatusHandlerTest.java (88 lines)
│   │   │   │       │                   │   │   │   ├── CollectionJobResultListenerTest.java (473 lines)
│   │   │   │       │                   │   │   │   ├── CollectionJobStatusHandlerTest.java (101 lines)
│   │   │   │       │                   │   │   │   ├── GNMIResponseParserTest.java (928 lines)
│   │   │   │       │                   │   │   │   ├── HeliosNotificationListenerTest.java (113 lines)
│   │   │   │       │                   │   │   │   └── SatelliteResponseParserTest.java (872 lines)
│   │   │   │       │                   │   │   └── service/
│   │   │   │       │                   │   │       ├── CDGCollectionCallBackServiceTest.java (62 lines)
│   │   │   │       │                   │   │       ├── CDGCollectionServiceTest.java (1497 lines)
│   │   │   │       │                   │   │       ├── CDGConstantsTest.java (21 lines)
│   │   │   │       │                   │   │       ├── CDGRequestDataTest.java (39 lines)
│   │   │   │       │                   │   │       └── CDGResponseDataTest.java (51 lines)
│   │   │   │       │                   │   ├── collectortask/
│   │   │   │       │                   │   │   ├── CollectorCDGFeatureTaskTest.java (586 lines)
│   │   │   │       │                   │   │   ├── CollectorFeatureHookTaskTest.java (925 lines)
│   │   │   │       │                   │   │   ├── CollectorFeatureTaskTest.java (1525 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskAcquireLockTest.java (274 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskBootstrapConnectivityTest.java (396 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskBootstrapExecuteTest.java (929 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskCDGExecuteDevicePackagesTest.java (1978 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskConnectivityCheckTest.java (235 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskExecuteDevicePackagesTest.java (2180 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskManageabilityConfigTest.java (168 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPostAcquireDeviceLockFailedTest.java (190 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPostAcquireDeviceLockFinishedExecDevicePackagesTest.java (119 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPostAcquireDeviceLockTest.java (221 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPostCollectionTest.java (78 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPostDPExecuteTest.java (159 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPreDPExecuteTest.java (178 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskPunctualUpdateTest.java (82 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskTest.java (261 lines)
│   │   │   │       │                   │   │   ├── CollectorTaskUpdateCollectionContextTest.java (114 lines)
│   │   │   │       │                   │   │   └── LirRigiHelperTest.java (768 lines)
│   │   │   │       │                   │   ├── dlm/
│   │   │   │       │                   │   │   └── handler/
│   │   │   │       │                   │   │       └── DlmInvMgrRequestHandlerTest.java (96 lines)
│   │   │   │       │                   │   ├── feature/
│   │   │   │       │                   │   │   ├── AttributeBasedCriteriaTest.java (241 lines)
│   │   │   │       │                   │   │   ├── FeatureCheckTest.java (220 lines)
│   │   │   │       │                   │   │   ├── FeatureRunResultTest.java (90 lines)
│   │   │   │       │                   │   │   └── ObjectBasedCriteriaTest.java (159 lines)
│   │   │   │       │                   │   ├── results/
│   │   │   │       │                   │   │   └── CollectionResultsHelperTest.java (98 lines)
│   │   │   │       │                   │   ├── startup/
│   │   │   │       │                   │   │   ├── CheckCollectorSyncStateHookTest.java (343 lines)
│   │   │   │       │                   │   │   ├── CheckLifeCycleStatePostInitHookTest.java (392 lines)
│   │   │   │       │                   │   │   └── SchedulingStartupHookTest.java (133 lines)
│   │   │   │       │                   │   ├── AbortExceptionTest.java (16 lines)
│   │   │   │       │                   │   ├── AlarmClientConstantsTest.java (30 lines)
│   │   │   │       │                   │   ├── AuditLoggingUtilTest.java (60 lines)
│   │   │   │       │                   │   ├── CollectionContextTest.java (20 lines)
│   │   │   │       │                   │   ├── CollectionPolicyContextWrapperTest.java (106 lines)
│   │   │   │       │                   │   ├── CollectionPolicyWrapperTest.java (92 lines)
│   │   │   │       │                   │   ├── CollectionRequestFullCoverageTest.java (104 lines)
│   │   │   │       │                   │   ├── CollectionRequestTest.java (135 lines)
│   │   │   │       │                   │   ├── CollectionResponseTest.java (83 lines)
│   │   │   │       │                   │   ├── DeviceSchedulingHookImplTest.java (580 lines)
│   │   │   │       │                   │   ├── DeviceSyncRequestDistrCacheTest.java (348 lines)
│   │   │   │       │                   │   ├── DummyInventoryCollectorStatsLoggerTest.java (45 lines)
│   │   │   │       │                   │   ├── ICETransactionSynchronizationHookTest.java (543 lines)
│   │   │   │       │                   │   ├── IceCollectorTaskImplKafkaPopulateTest.java (80 lines)
│   │   │   │       │                   │   ├── IceCollectorTaskImplTest.java (787 lines)
│   │   │   │       │                   │   ├── IceCollectorTaskSchedulerTest.java (227 lines)
│   │   │   │       │                   │   ├── IceExternalApplicationSampleImplTest.java (32 lines)
│   │   │   │       │                   │   ├── IcePojoGenerationExceptionTest.java (60 lines)
│   │   │   │       │                   │   ├── IceSrvTest.java (81 lines)
│   │   │   │       │                   │   ├── IceTaskImplTest.java (885 lines)
│   │   │   │       │                   │   ├── IceXdeEngineTest.java (99 lines)
│   │   │   │       │                   │   ├── InventoryCollectionAbortServiceImplTest.java (92 lines)
│   │   │   │       │                   │   ├── InventoryCollectorAbortMessageHandlerTest.java (102 lines)
│   │   │   │       │                   │   ├── InventoryCollectorEngineServiceImplDummy_Test.java (48 lines)
│   │   │   │       │                   │   ├── InventoryCollectorEngineServiceImplTest.java (3141 lines)
│   │   │   │       │                   │   ├── InventoryCollectorEngineXdeImplTest.java (5822 lines)
│   │   │   │       │                   │   ├── InventoryCollectorExecutorCustomTest.java (51 lines)
│   │   │   │       │                   │   ├── InventoryCollectorExecutorImplTest.java (439 lines)
│   │   │   │       │                   │   ├── InventoryCollectorFactoryTest.java (107 lines)
│   │   │   │       │                   │   ├── InventoryCollectorLoggingUtilTest.java (173 lines)
│   │   │   │       │                   │   ├── InventoryCollectorStatsLoggerImplTest.java (74 lines)
│   │   │   │       │                   │   ├── InventoryCollectorSyncMessageHandlerTest.java (181 lines)
│   │   │   │       │                   │   ├── InventoryCollectorUtilTest.java (82 lines)
│   │   │   │       │                   │   ├── InventoryFeaturePollerTaskTest.java (835 lines)
│   │   │   │       │                   │   ├── InventoryMessageHandlerTest.java (647 lines)
│   │   │   │       │                   │   ├── MockFeatureRunner.java (165 lines)
│   │   │   │       │                   │   ├── MockInventoryCollector.java (202 lines)
│   │   │   │       │                   │   ├── MockJobService.java (244 lines)
│   │   │   │       │                   │   ├── MockModelService.java (54 lines)
│   │   │   │       │                   │   ├── MockPersistence.java (811 lines)
│   │   │   │       │                   │   ├── MockTransactionStatus.java (114 lines)
│   │   │   │       │                   │   ├── MockTransactionmgr.java (27 lines)
│   │   │   │       │                   │   └── UtilitiesTest.java (151 lines)
│   │   │   │       │                   ├── model/
│   │   │   │       │                   │   ├── dto/
│   │   │   │       │                   │   │   ├── ACLDTO.java (169 lines)
│   │   │   │       │                   │   │   └── InterfaceDTO.java (469 lines)
│   │   │   │       │                   │   ├── metadata/
│   │   │   │       │                   │   │   ├── ACLMetadata.java (376 lines)
│   │   │   │       │                   │   │   └── InterfaceMetadata.java (848 lines)
│   │   │   │       │                   │   ├── ACL.java (286 lines)
│   │   │   │       │                   │   ├── Equipment.java (42 lines)
│   │   │   │       │                   │   ├── IP.java (61 lines)
│   │   │   │       │                   │   └── Interface.java (621 lines)
│   │   │   │       │                   ├── persistence/
│   │   │   │       │                   │   ├── tests/
│   │   │   │       │                   │   │   ├── CRUDTestBean.java (108 lines)
│   │   │   │       │                   │   │   ├── CRUDTestCase.java (251 lines)
│   │   │   │       │                   │   │   ├── DMMInitHelper.java (90 lines)
│   │   │   │       │                   │   │   ├── ModelObjectPersisterTester.java (164 lines)
│   │   │   │       │                   │   │   └── PersistenceInit.java (52 lines)
│   │   │   │       │                   │   ├── ICEDaoTest.java (364 lines)
│   │   │   │       │                   │   └── PersistenceFactoryBeanTest.java (88 lines)
│   │   │   │       │                   ├── pojogen/
│   │   │   │       │                   │   ├── test/
│   │   │   │       │                   │   │   ├── GeneratedPojoCacheTest.java (1799 lines)
│   │   │   │       │                   │   │   ├── PALXMLToPojoTester.java (489 lines)
│   │   │   │       │                   │   │   ├── SampleBusinessProcessWithFalseResponseHook.java (53 lines)
│   │   │   │       │                   │   │   └── SampleBusinessProcessWithTrueResponseHook.java (53 lines)
│   │   │   │       │                   │   ├── DocumentImpl.java (345 lines)
│   │   │   │       │                   │   ├── ElementImpl.java (290 lines)
│   │   │   │       │                   │   ├── GeneratedPojoCacheTest.java (4281 lines)
│   │   │   │       │                   │   ├── ICEMetadataParserTest.java (354 lines)
│   │   │   │       │                   │   ├── NodeImpl.java (190 lines)
│   │   │   │       │                   │   ├── ObjectDefinitionCacheTest.java (132 lines)
│   │   │   │       │                   │   └── PalXMLToPOJOConvertorTest.java (1016 lines)
│   │   │   │       │                   ├── profile/
│   │   │   │       │                   │   ├── DeviceProfileUtilitiesTest.java (401 lines)
│   │   │   │       │                   │   ├── FeatureRunnerTest.java (190 lines)
│   │   │   │       │                   │   └── XDEFeatureRunner.java (183 lines)
│   │   │   │       │                   ├── test/
│   │   │   │       │                   │   ├── stubs/
│   │   │   │       │                   │   │   ├── CredentialMgrTestStub.java (227 lines)
│   │   │   │       │                   │   │   ├── DevicePackageLoaderTestStub.java (418 lines)
│   │   │   │       │                   │   │   └── LifecycleManagerTestStub.java (77 lines)
│   │   │   │       │                   │   ├── util/
│   │   │   │       │                   │   │   ├── ACPMTestUtils.java (443 lines)
│   │   │   │       │                   │   │   └── ServerHostKeyVerifierProviderTest.java (178 lines)
│   │   │   │       │                   │   └── RootTester.java (26 lines)
│   │   │   │       │                   └── util/
│   │   │   │       │                       ├── ApplicationContextTestStub.java (183 lines)
│   │   │   │       │                       ├── CollectorCacheUtilTest.java (113 lines)
│   │   │   │       │                       ├── CollectorConstantsTest.java (27 lines)
│   │   │   │       │                       ├── CommandStatisticsCollectorImplTest.java (57 lines)
│   │   │   │       │                       ├── CommandStatisticsImplTest.java (41 lines)
│   │   │   │       │                       ├── DistributedCacheServiceTestStub.java (41 lines)
│   │   │   │       │                       ├── GlobalFilterUtilTest.java (1360 lines)
│   │   │   │       │                       ├── IOSXRVersionCheckerTest.java (51 lines)
│   │   │   │       │                       ├── InventoryParserUtilImplTest.java (408 lines)
│   │   │   │       │                       ├── InventoryStatisticsCollectorImplTest.java (157 lines)
│   │   │   │       │                       ├── InventoryStatisticsImplTest.java (252 lines)
│   │   │   │       │                       ├── InventoryStatisticsSummaryTest.java (18 lines)
│   │   │   │       │                       ├── InventoryUtilImplTest.java (139 lines)
│   │   │   │       │                       ├── MCEPreDeleteHandlerTest.java (70 lines)
│   │   │   │       │                       ├── PersistenceFactoryStubTest.java (104 lines)
│   │   │   │       │                       ├── PersistenceServiceStubTest.java (596 lines)
│   │   │   │       │                       ├── ServerHostKeyVerifierProviderImplTest.java (228 lines)
│   │   │   │       │                       ├── SystemPreferenceUtilTest.java (200 lines)
│   │   │   │       │                       ├── XMPInventoryConstantsUtilTest.java (315 lines)
│   │   │   │       │                       └── XMPInventoryMEICallBackHookTest.java (80 lines)
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── spring/
│   │   │   │           │       ├── collector-context.xml (16 lines)
│   │   │   │           │       ├── device-scheduling-context.xml (117 lines)
│   │   │   │           │       ├── module-context.xml (45 lines)
│   │   │   │           │       └── osgi-context.xml (14 lines)
│   │   │   │           ├── com/
│   │   │   │           │   └── cisco/
│   │   │   │           │       └── xmp/
│   │   │   │           │           ├── deviceaccess/
│   │   │   │           │           │   ├── equipment.xml (1476 lines)
│   │   │   │           │           │   └── single-equipment.xml (29 lines)
│   │   │   │           │           └── inventory/
│   │   │   │           │               ├── credentials/
│   │   │   │           │               │   ├── credentialdictionary.txt (15 lines)
│   │   │   │           │               │   └── inventory.properties (11 lines)
│   │   │   │           │               └── model/
│   │   │   │           │                   ├── ACL.hbm.xml (33 lines)
│   │   │   │           │                   └── Iterface.hbm.xml (46 lines)
│   │   │   │           ├── conf/
│   │   │   │           │   ├── FeatureInfo.xml (25 lines)
│   │   │   │           │   └── ifm_inventory.properties (0 lines)
│   │   │   │           ├── gnmi/
│   │   │   │           │   ├── 10.104.120.236/
│   │   │   │           │   │   └── LWR_236_8k_UNBundled_CDG_Response.log (37467 lines)
│   │   │   │           │   └── 10.104.120.57/
│   │   │   │           │       └── 57_response170725.log (237 lines)
│   │   │   │           ├── ice_metadata/
│   │   │   │           │   ├── rfm-im-module.xml (182 lines)
│   │   │   │           │   ├── xmp-im-logical-resource-module.xml (47 lines)
│   │   │   │           │   ├── xmp-im-physical-resource-module.xml (42 lines)
│   │   │   │           │   ├── xmp-im-physical-resource-module_corrupted_for_testing.xml (39 lines)
│   │   │   │           │   └── xmp-im-vlan-module-ice-metadata.xml (169 lines)
│   │   │   │           ├── model_xsd/
│   │   │   │           │   ├── ACLSamplePalOutput.xsd (22 lines)
│   │   │   │           │   ├── InterfaceSamplePalOutput.xsd (33 lines)
│   │   │   │           │   ├── InterfaceSamplePalOutput_Corrupted.xsd (31 lines)
│   │   │   │           │   └── xmp-im-physical-resource-module.xsd (220 lines)
│   │   │   │           ├── packagesDir/
│   │   │   │           │   └── customized-feature-parts/
│   │   │   │           │       └── INVENTORY/
│   │   │   │           │           └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │           ├── pal_xml_out/
│   │   │   │           │   ├── perf/
│   │   │   │           │   │   ├── 20kEthernetProtocolEndpoints.xml (320002 lines)
│   │   │   │           │   │   └── 20kInterfaceProtocolEndpoints.xml (300002 lines)
│   │   │   │           │   ├── ACLSamplePalOutput.xml (30 lines)
│   │   │   │           │   ├── InterfaceSamplePalOutput.xml (38 lines)
│   │   │   │           │   ├── InterfaceSamplePalOutput_Corrupted.xml (34 lines)
│   │   │   │           │   ├── InterfaceSamplePalOutput_Empty.xml (4 lines)
│   │   │   │           │   ├── pal_NE_out.xml (21 lines)
│   │   │   │           │   ├── pal_mne_out.xml (20 lines)
│   │   │   │           │   ├── pal_physical_resources_out.xml (1428 lines)
│   │   │   │           │   ├── pal_physical_resources_out_corrupted.xml (34 lines)
│   │   │   │           │   ├── pal_physical_resources_out_empty.xml (7 lines)
│   │   │   │           │   ├── pal_physical_resources_out_for_business_process_hook_false_test.xml (123 lines)
│   │   │   │           │   ├── pal_physical_resources_out_for_business_process_hook_true_test.xml (123 lines)
│   │   │   │           │   ├── pal_physical_resources_out_multiple_objects.xml (330 lines)
│   │   │   │           │   ├── pal_physical_resources_uuid_out.xml (84 lines)
│   │   │   │           │   ├── pal_software_out.xml (14 lines)
│   │   │   │           │   ├── xmp-im-connectivity-module_out.xml (907 lines)
│   │   │   │           │   └── xmp-im-vlan-module-output.xml (106 lines)
│   │   │   │           ├── xdeRuntime/
│   │   │   │           │   ├── conf/
│   │   │   │           │   │   ├── inventory.properties (20 lines)
│   │   │   │           │   │   ├── log4j.properties (8 lines)
│   │   │   │           │   │   └── xdeEngine.properties (6 lines)
│   │   │   │           │   └── mibs/
│   │   │   │           │       ├── CISCO-CDP-MIB.my (828 lines)
│   │   │   │           │       ├── CISCO-ENTITY-ASSET-MIB.my (526 lines)
│   │   │   │           │       ├── CISCO-PRODUCTS-MIB.my (1095 lines)
│   │   │   │           │       ├── CISCO-SMI.my (542 lines)
│   │   │   │           │       ├── CISCO-TC.my (1654 lines)
│   │   │   │           │       └── CISCO-VTP-MIB.my (4986 lines)
│   │   │   │           ├── bootstrap.properties (59 lines)
│   │   │   │           ├── cli_preamble.properties (4 lines)
│   │   │   │           ├── exclusion.properties (5 lines)
│   │   │   │           ├── ifm_inventory.properties (179 lines)
│   │   │   │           ├── ifm_inventory_cli_dp.properties (1 lines)
│   │   │   │           ├── log4j.properties (22 lines)
│   │   │   │           ├── log4j.xml (30 lines)
│   │   │   │           ├── mdfdata.xml (6543 lines)
│   │   │   │           ├── persistence.properties (56 lines)
│   │   │   │           ├── test-ice.xml (83 lines)
│   │   │   │           ├── test-iceSrv.xml (16 lines)
│   │   │   │           └── testbed.xml (12 lines)
│   │   │   ├── xde-home/
│   │   │   │   ├── conf/
│   │   │   │   │   ├── inventory.properties (7 lines)
│   │   │   │   │   └── xdeEngine.properties (17 lines)
│   │   │   │   ├── inventoryDefaults/
│   │   │   │   │   ├── XdeCommonExt.def (8 lines)
│   │   │   │   │   ├── XdeGenericExt.def (13 lines)
│   │   │   │   │   ├── XdeIOSExt.def (16 lines)
│   │   │   │   │   ├── XdeIOSXR.def (23 lines)
│   │   │   │   │   ├── XdeIOS_ngwc.def (18 lines)
│   │   │   │   │   ├── XdeMeraki.def (7 lines)
│   │   │   │   │   ├── XdeSGxExt.def (23 lines)
│   │   │   │   │   ├── ncsCIMC.def (20 lines)
│   │   │   │   │   ├── ncsNX-OS.def (22 lines)
│   │   │   │   │   ├── ncsWAAS.def (22 lines)
│   │   │   │   │   ├── netconf.def (19 lines)
│   │   │   │   │   ├── xdeASA_FirePOWER.def (36 lines)
│   │   │   │   │   ├── xdeAdaptiveSecurityAppliances.def (24 lines)
│   │   │   │   │   ├── xdeApplicationControlEngine.def (18 lines)
│   │   │   │   │   ├── xdeIndustrialSecurityAppliance.def (13 lines)
│   │   │   │   │   └── xdeME1200.def (20 lines)
│   │   │   │   ├── mibs/
│   │   │   │   │   ├── AIRESPACE-REF-MIB.my (11 lines)
│   │   │   │   │   ├── AIRESPACE-SWITCHING-MIB.my (3606 lines)
│   │   │   │   │   ├── CISCO-CDP-MIB.my (828 lines)
│   │   │   │   │   ├── CISCO-ENTITY-ASSET-MIB.my (526 lines)
│   │   │   │   │   ├── CISCO-PRODUCTS-MIB.my (1669 lines)
│   │   │   │   │   ├── CISCO-SMI.my (542 lines)
│   │   │   │   │   ├── CISCO-TC.my (1654 lines)
│   │   │   │   │   ├── CISCO-VTP-MIB.my (4986 lines)
│   │   │   │   │   ├── IANAifType-MIB.my (518 lines)
│   │   │   │   │   ├── INET-ADDRESS-MIB.my (425 lines)
│   │   │   │   │   ├── MERAKI-CLOUD-CONTROLLER-MIB.mib (373 lines)
│   │   │   │   │   ├── Q-BRIDGE-MIB.my (1867 lines)
│   │   │   │   │   └── SNMPv2-TC.my (714 lines)
│   │   │   │   ├── packages/
│   │   │   │   │   ├── site/
│   │   │   │   │   │   └── README (1 lines)
│   │   │   │   │   └── standard/
│   │   │   │   │       └── README (1 lines)
│   │   │   │   ├── tmp/
│   │   │   │   │   └── README (1 lines)
│   │   │   │   └── tmp_inv/
│   │   │   │       └── README (1 lines)
│   │   │   ├── .classpath (37 lines)
│   │   │   ├── .project (24 lines)
│   │   │   ├── pom.xml (752 lines)
│   │   │   ├── suite.xml (50 lines)
│   │   │   └── test_suite.xml (50 lines)
│   │   ├── xmp_collector_intf/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.core.resources.prefs (7 lines)
│   │   │   │   ├── org.eclipse.jdt.core.prefs (14 lines)
│   │   │   │   └── org.eclipse.m2e.core.prefs (5 lines)
│   │   │   ├── src/
│   │   │   │   ├── main/
│   │   │   │   │   ├── java/
│   │   │   │   │   │   └── com/
│   │   │   │   │   │       └── cisco/
│   │   │   │   │   │           └── xmp/
│   │   │   │   │   │               ├── device/
│   │   │   │   │   │               │   └── tools/
│   │   │   │   │   │               │       ├── DatabaseDiagnostics.java (107 lines)
│   │   │   │   │   │               │       ├── DeviceDiagnosticException.java (31 lines)
│   │   │   │   │   │               │       └── ModelDiagnostic.java (171 lines)
│   │   │   │   │   │               ├── deviceaccess/
│   │   │   │   │   │               │   ├── businessProcessor/
│   │   │   │   │   │               │   │   ├── BusinessProcessHookException.java (151 lines)
│   │   │   │   │   │               │   │   ├── BusinessProcessHookIntf.java (43 lines)
│   │   │   │   │   │               │   │   ├── BusinessProcessManagerIntf.java (53 lines)
│   │   │   │   │   │               │   │   ├── BusinessProcessWithResponseHookIntf.java (32 lines)
│   │   │   │   │   │               │   │   └── BusinessProcessorRegistryIntf.java (50 lines)
│   │   │   │   │   │               │   ├── datapopulator/
│   │   │   │   │   │               │   │   └── ExternalAttributePopulator.java (32 lines)
│   │   │   │   │   │               │   ├── ActionRegistry.java (37 lines)
│   │   │   │   │   │               │   ├── BusinessProcessor.java (30 lines)
│   │   │   │   │   │               │   ├── DeviceAccessException.java (39 lines)
│   │   │   │   │   │               │   ├── DeviceAccessService.java (104 lines)
│   │   │   │   │   │               │   ├── DuplicateDetector.java (74 lines)
│   │   │   │   │   │               │   └── PalAdaptor.java (35 lines)
│   │   │   │   │   │               └── inventory/
│   │   │   │   │   │                   ├── adaptors/
│   │   │   │   │   │                   │   └── InventoryCollectorJobService.java (121 lines)
│   │   │   │   │   │                   ├── associationBuilder/
│   │   │   │   │   │                   │   ├── AssociationBuilderIntf.java (86 lines)
│   │   │   │   │   │                   │   └── PostCollectionPersistHook.java (41 lines)
│   │   │   │   │   │                   ├── cache/
│   │   │   │   │   │                   │   └── ICESmartCache.java (87 lines)
│   │   │   │   │   │                   ├── connectivity/
│   │   │   │   │   │                   │   ├── BootstrapConnectivityFailureIntf.java (50 lines)
│   │   │   │   │   │                   │   └── DevicePackageConnectivityFailureIntf.java (50 lines)
│   │   │   │   │   │                   ├── diffEngine/
│   │   │   │   │   │                   │   ├── DifferenceEngine.java (145 lines)
│   │   │   │   │   │                   │   ├── DifferenceState.java (33 lines)
│   │   │   │   │   │                   │   ├── FingerprintCacheIntf.java (475 lines)
│   │   │   │   │   │                   │   └── FingerprintUtility.java (140 lines)
│   │   │   │   │   │                   ├── ice/
│   │   │   │   │   │                   │   ├── cdg/
│   │   │   │   │   │                   │   │   └── dispatcher/
│   │   │   │   │   │                   │   │       └── CDGResponseLocalListener.java (15 lines)
│   │   │   │   │   │                   │   ├── feature/
│   │   │   │   │   │                   │   │   ├── IFeatureRunResult.java (100 lines)
│   │   │   │   │   │                   │   │   └── RunResultEnum.java (20 lines)
│   │   │   │   │   │                   │   ├── results/
│   │   │   │   │   │                   │   │   └── ICollectionResultsHelper.java (53 lines)
│   │   │   │   │   │                   │   ├── AbstractCollectionNotifierIntf.java (38 lines)
│   │   │   │   │   │                   │   ├── ChangedObjectOfTypeNotifierIntf.java (42 lines)
│   │   │   │   │   │                   │   ├── CollectionLifecycleNotifierIntf.java (28 lines)
│   │   │   │   │   │                   │   ├── CollectionNotifierAsyncCallback.java (15 lines)
│   │   │   │   │   │                   │   ├── CollectionNotifierAsyncIntf.java (68 lines)
│   │   │   │   │   │                   │   ├── CollectionNotifierEnhancedIntf.java (53 lines)
│   │   │   │   │   │                   │   ├── CollectionNotifierIntf.java (64 lines)
│   │   │   │   │   │                   │   ├── DeviceSchedulingHook.java (157 lines)
│   │   │   │   │   │                   │   ├── DoesNotExistException.java (94 lines)
│   │   │   │   │   │                   │   ├── ExecutionStatus.java (89 lines)
│   │   │   │   │   │                   │   ├── FeatureAndParams.java (39 lines)
│   │   │   │   │   │                   │   ├── ICEWorkFlowIntf.java (29 lines)
│   │   │   │   │   │                   │   ├── ICollectionContext.java (8 lines)
│   │   │   │   │   │                   │   ├── IceCallback.java (26 lines)
│   │   │   │   │   │                   │   ├── IceExternalApplicationHookWithSameMarker.java (9 lines)
│   │   │   │   │   │                   │   ├── IceExternalApplicationIntf.java (63 lines)
│   │   │   │   │   │                   │   ├── IceMediation.java (65 lines)
│   │   │   │   │   │                   │   ├── IceStatus.java (45 lines)
│   │   │   │   │   │                   │   ├── IceTask.java (168 lines)
│   │   │   │   │   │                   │   ├── IceTaskCallback.java (5 lines)
│   │   │   │   │   │                   │   ├── IceTaskRunnable.java (7 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectionTypeEnum.java (14 lines)
│   │   │   │   │   │                   │   ├── InventoryCollector.java (203 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorCallback.java (5 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorEngine.java (916 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorEngineWithOverride.java (65 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorExecutor.java (11 lines)
│   │   │   │   │   │                   │   ├── InventoryCollectorStatsLogger.java (9 lines)
│   │   │   │   │   │                   │   ├── InventoryException.java (143 lines)
│   │   │   │   │   │                   │   ├── InventorySyncingException.java (42 lines)
│   │   │   │   │   │                   │   ├── NetworkNotificationIntf.java (68 lines)
│   │   │   │   │   │                   │   ├── PostCollectionHookException.java (135 lines)
│   │   │   │   │   │                   │   ├── PreCollectionCheck.java (49 lines)
│   │   │   │   │   │                   │   ├── PreCollectionCheckEnhanced.java (51 lines)
│   │   │   │   │   │                   │   └── WorkflowEnum.java (11 lines)
│   │   │   │   │   │                   ├── policybase/
│   │   │   │   │   │                   │   ├── CollectionPolicy.java (74 lines)
│   │   │   │   │   │                   │   ├── CollectionPolicyContext.java (469 lines)
│   │   │   │   │   │                   │   └── PolicyBasedInventoryCollectorEngine.java (39 lines)
│   │   │   │   │   │                   ├── profile/
│   │   │   │   │   │                   │   └── FeatureRunner.java (73 lines)
│   │   │   │   │   │                   └── util/
│   │   │   │   │   │                       ├── FeatureDetailsWrapper.java (96 lines)
│   │   │   │   │   │                       ├── InventoryCollectionQueueNotifier.java (26 lines)
│   │   │   │   │   │                       ├── InventoryStatistics.java (780 lines)
│   │   │   │   │   │                       ├── InventoryStatisticsCollector.java (91 lines)
│   │   │   │   │   │                       ├── InventoryUtil.java (36 lines)
│   │   │   │   │   │                       ├── NLOInfo.java (79 lines)
│   │   │   │   │   │                       └── NetworkObjectData.java (65 lines)
│   │   │   │   │   └── resources/
│   │   │   │   │       └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │   ├── site/
│   │   │   │   │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │   └── test/
│   │   │   │       ├── java/
│   │   │   │       │   ├── com/
│   │   │   │       │   │   └── cisco/
│   │   │   │       │   │       └── xmp/
│   │   │   │       │   │           ├── device/
│   │   │   │       │   │           │   └── tools/
│   │   │   │       │   │           │       └── ModelDiagnosticTest.java (73 lines)
│   │   │   │       │   │           ├── deviceaccess/
│   │   │   │       │   │           │   ├── businessProcessor/
│   │   │   │       │   │           │   │   └── BusinessProcessHookExceptionTest.java (67 lines)
│   │   │   │       │   │           │   └── DeviceAccessExceptionTest.java (17 lines)
│   │   │   │       │   │           └── inventory/
│   │   │   │       │   │               ├── diffEngine/
│   │   │   │       │   │               │   └── DifferenceStateTest.java (18 lines)
│   │   │   │       │   │               ├── ice/
│   │   │   │       │   │               │   ├── AbstractCollectionNotifierIntfTest.java (28 lines)
│   │   │   │       │   │               │   ├── IceStatusTest.java (18 lines)
│   │   │   │       │   │               │   ├── IceTaskAdditionalTest.java (102 lines)
│   │   │   │       │   │               │   ├── IceTaskTest.java (289 lines)
│   │   │   │       │   │               │   ├── InventoryCollectionTypeEnumTest.java (14 lines)
│   │   │   │       │   │               │   ├── InventoryExceptionTest.java (115 lines)
│   │   │   │       │   │               │   ├── PostCollectionHookExceptionTest.java (92 lines)
│   │   │   │       │   │               │   └── WorkflowEnumTest.java (14 lines)
│   │   │   │       │   │               ├── policybase/
│   │   │   │       │   │               │   └── CollectionPolicyContextTest.java (125 lines)
│   │   │   │       │   │               └── util/
│   │   │   │       │   │                   ├── InventoryStatisticsTest.java (96 lines)
│   │   │   │       │   │                   └── NLOInfoTest.java (100 lines)
│   │   │   │       │   └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   │       └── resources/
│   │   │   │           └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── pom.xml (162 lines)
│   │   │   └── suite.xml (7 lines)
│   │   ├── xmp_inventory_error_parser/
│   │   │   ├── .settings/
│   │   │   │   └── org.eclipse.core.resources.prefs (2 lines)
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.xmp.config.xde/
│   │   │   │   │       └── xmp_inventory_error_parser/
│   │   │   │   │           ├── pom.properties (5 lines)
│   │   │   │   │           └── pom.xml (41 lines)
│   │   │   │   └── MANIFEST.MF (8 lines)
│   │   │   ├── errorCodeInfo.xpa/
│   │   │   │   └── errorCodeInfo/
│   │   │   │       ├── ErrorCodeInfo.xml (368 lines)
│   │   │   │       └── errorCodeInfo.par (37 lines)
│   │   │   ├── handlerCodeParser/
│   │   │   │   ├── errorMessage.txt (18 lines)
│   │   │   │   ├── gnmiError.txt (1 lines)
│   │   │   │   ├── handlerCodeParser.par (40 lines)
│   │   │   │   ├── handlerCodeParser.rpl (212 lines)
│   │   │   │   ├── handlerCodeParserParserOutput.xsd (17 lines)
│   │   │   │   ├── internalError.txt (1 lines)
│   │   │   │   ├── netconfError.txt (5 lines)
│   │   │   │   ├── svo_rpc_error.txt (10 lines)
│   │   │   │   └── tl1Error.txt (2 lines)
│   │   │   ├── inventoryErrorMessageParser.xpa/
│   │   │   │   └── inventoryErrorMessageParser/
│   │   │   │       ├── newRuleParserOutput.xsd (36 lines)
│   │   │   │       ├── parseMessage.par (46 lines)
│   │   │   │       ├── ruleErrorParser.rpl (110 lines)
│   │   │   │       └── ruleErrorParser_Sample_Input (4 lines)
│   │   │   ├── src/
│   │   │   │   └── site/
│   │   │   │       └── .EMPTY_FOLDER_IN_SVN (0 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── handlerCodeProcedure.xde (20 lines)
│   │   │   ├── inventoryErrorMessageParser.xde (103 lines)
│   │   │   ├── inventoryRestCallParser.xde (44 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (38 lines)
│   │   ├── .project (17 lines)
│   │   ├── pom.xml (1230 lines)
│   │   ├── settings-rel.xml (106 lines)
│   │   └── settings.xml (118 lines)
│   ├── .classpath (6 lines)
│   ├── .gitignore (2 lines)
│   ├── .project (23 lines)
│   ├── components.txt (12 lines)
│   ├── components.txt.save (13 lines)
│   ├── settings-rel.xml (153 lines)
│   └── settings.xml (127 lines)
├── model/
│   ├── nbi_inventory_api/
│   │   ├── src/
│   │   │   └── com/
│   │   │       ├── cisco/
│   │   │       │   ├── ifm/
│   │   │       │   │   ├── nbi/
│   │   │       │   │   │   ├── inventory/
│   │   │       │   │   │   │   ├── cdpneighbors/
│   │   │       │   │   │   │   │   ├── .package (29 lines)
│   │   │       │   │   │   │   │   ├── CdpNeighborsDTO.java (239 lines)
│   │   │       │   │   │   │   │   └── CdpNeighborsService.java (97 lines)
│   │   │       │   │   │   │   ├── clients/
│   │   │       │   │   │   │   │   ├── .package (29 lines)
│   │   │       │   │   │   │   │   ├── ClusterInventoryClientDTO.java (621 lines)
│   │   │       │   │   │   │   │   └── ClusterInventoryClientService.java (110 lines)
│   │   │       │   │   │   │   ├── ethernet/
│   │   │       │   │   │   │   │   ├── EthernetEnablementSummaryService.java (89 lines)
│   │   │       │   │   │   │   │   ├── EthernetSummaryDTO.java (351 lines)
│   │   │       │   │   │   │   │   └── EthernetUdiDetailsDTO.java (142 lines)
│   │   │       │   │   │   │   ├── lldpneighbors/
│   │   │       │   │   │   │   │   ├── LldpNeighborsDTO.java (194 lines)
│   │   │       │   │   │   │   │   └── LldpNeighborsService.java (97 lines)
│   │   │       │   │   │   │   ├── location/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── AdvancedCivicAddressDTO.java (402 lines)
│   │   │       │   │   │   │   │   ├── BasicCivicAddressDTO.java (162 lines)
│   │   │       │   │   │   │   │   ├── ClusterCivicLocationDTO.java (258 lines)
│   │   │       │   │   │   │   │   ├── InventoryLocationService.java (88 lines)
│   │   │       │   │   │   │   │   └── UserDefinedAddressDTO.java (226 lines)
│   │   │       │   │   │   │   ├── memory/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterMemoryPoolDTO.java (129 lines)
│   │   │       │   │   │   │   │   └── InventoryMemoryService.java (88 lines)
│   │   │       │   │   │   │   ├── physicalports/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterPhysicalPortDTO.java (158 lines)
│   │   │       │   │   │   │   │   └── InventoryPhysicalPortsService.java (88 lines)
│   │   │       │   │   │   │   ├── stacks/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterInventoryStackDTO.java (146 lines)
│   │   │       │   │   │   │   │   └── InventoryStacksService.java (88 lines)
│   │   │       │   │   │   │   ├── summary/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   └── InventorySummaryService.java (195 lines)
│   │   │       │   │   │   │   ├── udf/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterInventoryUdfDTO.java (98 lines)
│   │   │       │   │   │   │   │   └── InventoryUdfService.java (356 lines)
│   │   │       │   │   │   │   ├── vlan/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterVlanDTO.java (94 lines)
│   │   │       │   │   │   │   │   └── VlanService.java (88 lines)
│   │   │       │   │   │   │   ├── vpc/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterVpcDetailsDTO.java (130 lines)
│   │   │       │   │   │   │   │   ├── ClusterVpcPeerLinkStatusDTO.java (146 lines)
│   │   │       │   │   │   │   │   ├── ClusterVpcPeerSettingsDTO.java (258 lines)
│   │   │       │   │   │   │   │   ├── ClusterVpcStatusDTO.java (178 lines)
│   │   │       │   │   │   │   │   └── EthernetVpcDetailsService.java (241 lines)
│   │   │       │   │   │   │   ├── vtp/
│   │   │       │   │   │   │   │   ├── .package (31 lines)
│   │   │       │   │   │   │   │   ├── ClusterVtpDTO.java (98 lines)
│   │   │       │   │   │   │   │   └── InventoryVtpService.java (88 lines)
│   │   │       │   │   │   │   ├── .package (29 lines)
│   │   │       │   │   │   │   ├── ClusterDeviceChassisDTO.java (194 lines)
│   │   │       │   │   │   │   ├── ClusterDeviceLocationDTO.java (637 lines)
│   │   │       │   │   │   │   ├── ClusterDeviceModuleDTO.java (194 lines)
│   │   │       │   │   │   │   ├── ClusterDeviceSensorDTO.java (148 lines)
│   │   │       │   │   │   │   ├── ClusterDeviceUDIDTO.java (114 lines)
│   │   │       │   │   │   │   ├── ClusterEnvironmentDTO.java (72 lines)
│   │   │       │   │   │   │   ├── ClusterEtherChannelDTO.java (158 lines)
│   │   │       │   │   │   │   ├── ClusterEtherChannelMemberPortsDTO.java (78 lines)
│   │   │       │   │   │   │   ├── ClusterEthernetInterfaceDTO.java (275 lines)
│   │   │       │   │   │   │   ├── ClusterFEXDTO.java (114 lines)
│   │   │       │   │   │   │   ├── ClusterFEXInterfacesDTO.java (98 lines)
│   │   │       │   │   │   │   ├── ClusterFanDTO.java (114 lines)
│   │   │       │   │   │   │   ├── ClusterInventoryDetailsDTO.java (129 lines)
│   │   │       │   │   │   │   ├── ClusterInventoryDetailsService.java (762 lines)
│   │   │       │   │   │   │   ├── ClusterInventoryInterfaceDTO.java (111 lines)
│   │   │       │   │   │   │   ├── ClusterIpInterfaceDTO.java (63 lines)
│   │   │       │   │   │   │   ├── ClusterPowerSupplyDTO.java (130 lines)
│   │   │       │   │   │   │   ├── ClusterSpanningTreeDTO.java (194 lines)
│   │   │       │   │   │   │   ├── ClusterSpanningTreeDetailsDTO.java (146 lines)
│   │   │       │   │   │   │   ├── ClusterVlanInterfaceDTO.java (132 lines)
│   │   │       │   │   │   │   └── InventoryServiceException.java (34 lines)
│   │   │       │   │   │   └── .package (29 lines)
│   │   │       │   │   ├── syncoffline/
│   │   │       │   │   │   ├── model/
│   │   │       │   │   │   │   ├── .package (29 lines)
│   │   │       │   │   │   │   └── SyncOfflineDevicePrefSettings.java (81 lines)
│   │   │       │   │   │   └── .package (29 lines)
│   │   │       │   │   └── .package (29 lines)
│   │   │       │   └── .package (29 lines)
│   │   │       └── .package (28 lines)
│   │   ├── .gitignore (1 lines)
│   │   ├── .project (38 lines)
│   │   ├── pom.xml (240 lines)
│   │   ├── tigerstripe.target (19 lines)
│   │   └── tigerstripe.xml (81 lines)
│   └── .EMPTY_FOLDER_IN_SVN (0 lines)
├── scan-config/
│   ├── application.properties (6 lines)
│   ├── ignore_paths.properties (7 lines)
│   ├── ignore_statements.properties (4 lines)
│   ├── ignore_variables.properties (2 lines)
│   ├── log_patterns.properties (1 lines)
│   ├── scan_file_types.properties (2 lines)
│   └── sensitive_patterns.properties (17 lines)
├── test-additions/
│   ├── NodeNotificationListenerUnreachabilityTest.java (288 lines)
│   └── NodeNotificationListenerUnreachableStateTest.java (240 lines)
├── tests/
│   ├── ifm-api-tests/
│   │   ├── functional_tests/
│   │   │   ├── 360/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── test/
│   │   │   │   │       │               └── pi/
│   │   │   │   │       │                   └── deviceview/
│   │   │   │   │       │                       ├── DeviceFullViewBasicTest.java (516 lines)
│   │   │   │   │       │                       └── DeviceFullViewModulesTest.java (326 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── com/
│   │   │   │   │           │   └── cisco/
│   │   │   │   │           │       └── test/
│   │   │   │   │           │           └── pi/
│   │   │   │   │           │               └── deviceview/
│   │   │   │   │           │                   └── i18n/
│   │   │   │   │           │                       └── framework.properties (28 lines)
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.test.pi.deviceview/
│   │   │   │   │           │       ├── DeviceFullViewBasicTest.xml (256 lines)
│   │   │   │   │           │       └── DeviceFullViewModulesTest.xml (129 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── 360PreCommitTestSuiteStaging.xml (22 lines)
│   │   │   │   │           │   ├── 360TestSuite.xml (19 lines)
│   │   │   │   │           │   └── Sanity_360TestSuite.xml (22 lines)
│   │   │   │   │           ├── testbeds/
│   │   │   │   │           │   └── localtestbed.xml (223 lines)
│   │   │   │   │           └── pi-360-test-case-context.xml (35 lines)
│   │   │   │   └── pom.xml (352 lines)
│   │   │   ├── credentialProfile/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── test/
│   │   │   │   │       │               └── pi/
│   │   │   │   │       │                   └── cp/
│   │   │   │   │       │                       ├── util/
│   │   │   │   │       │                       │   └── CredentialProfileUtil.java (791 lines)
│   │   │   │   │       │                       ├── CredentialProfileAddTest.java (234 lines)
│   │   │   │   │       │                       ├── CredentialProfileCopyTest.java (171 lines)
│   │   │   │   │       │                       ├── CredentialProfileDisplayTest.java (1078 lines)
│   │   │   │   │       │                       ├── CredentialProfileUpdateTest.java (346 lines)
│   │   │   │   │       │                       └── DeleteCredentialProfileTest.java (175 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.test.pi.cp/
│   │   │   │   │           │       ├── CredentialProfileAddTest.xml (333 lines)
│   │   │   │   │           │       ├── CredentialProfileCopyTest.xml (40 lines)
│   │   │   │   │           │       ├── CredentialProfileDisplayTest.xml (323 lines)
│   │   │   │   │           │       ├── CredentialProfileUpdateTest.xml (74 lines)
│   │   │   │   │           │       └── DeleteCredentialProfileTest.xml (44 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── CPSanityTestSuite.xml (27 lines)
│   │   │   │   │           │   ├── CPTestSuite.xml (22 lines)
│   │   │   │   │           │   └── CredentialProfilePreCommitTestSuiteStaging.xml (27 lines)
│   │   │   │   │           ├── testbeds/
│   │   │   │   │           │   └── localtestbed.xml (156 lines)
│   │   │   │   │           └── pi-cp-test-context.xml (34 lines)
│   │   │   │   └── pom.xml (239 lines)
│   │   │   ├── device-credential/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── test/
│   │   │   │   │       │               └── pi/
│   │   │   │   │       │                   └── ifm/
│   │   │   │   │       │                       └── cda/
│   │   │   │   │       │                           ├── impl/
│   │   │   │   │       │                           │   ├── CDARunnerTest.java (174 lines)
│   │   │   │   │       │                           │   └── CheckMNECredentialsTest.java (203 lines)
│   │   │   │   │       │                           ├── rest/
│   │   │   │   │       │                           │   └── CheckCredentialsTest.java (94 lines)
│   │   │   │   │       │                           └── util/
│   │   │   │   │       │                               ├── CDAHelper.java (95 lines)
│   │   │   │   │       │                               ├── CDAUtilTest.java (321 lines)
│   │   │   │   │       │                               └── DeviceProfileUtilTest.java (127 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   ├── com.cisco.test.pi.ifm.cda.impl/
│   │   │   │   │           │   │   ├── CDARunnerTest.xml (12 lines)
│   │   │   │   │           │   │   └── CheckMNECredentialsTest.xml (37 lines)
│   │   │   │   │           │   ├── com.cisco.test.pi.ifm.cda.rest/
│   │   │   │   │           │   │   └── CheckCredentialsTest.xml (12 lines)
│   │   │   │   │           │   └── com.cisco.test.pi.ifm.cda.util/
│   │   │   │   │           │       ├── CDAUtilTest.xml (60 lines)
│   │   │   │   │           │       └── DeviceProfileUtilTest.xml (21 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── CDAPreCommitTestSuiteStaging.xml (26 lines)
│   │   │   │   │           │   ├── CDA_Dev_TestSuite.xml (21 lines)
│   │   │   │   │           │   └── Sanity_CDA_Dev_TestSuite.xml (26 lines)
│   │   │   │   │           ├── testbeds/
│   │   │   │   │           │   └── localtestbed.xml (357 lines)
│   │   │   │   │           ├── pi-cda-test-case-context.xml (27 lines)
│   │   │   │   │           ├── pi-cda-test-context.xml (21 lines)
│   │   │   │   │           └── pi_cda.properties (3 lines)
│   │   │   │   └── pom.xml (151 lines)
│   │   │   ├── discovery/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── discovery/
│   │   │   │   │       │                       ├── util/
│   │   │   │   │       │                       │   └── DiscoveryTestUtil.java (1703 lines)
│   │   │   │   │       │                       └── DiscoveryTest.java (1394 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.discovery/
│   │   │   │   │           │       └── DiscoveryTest.xml (2231 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── DiscoveryPreCommitTestSuiteStaging.xml (22 lines)
│   │   │   │   │           │   ├── DiscoveryTestSuite.xml (17 lines)
│   │   │   │   │           │   └── Sanity_DiscoveryTestSuite.xml (22 lines)
│   │   │   │   │           ├── testbeds/
│   │   │   │   │           │   └── testbed.xml (480 lines)
│   │   │   │   │           ├── discovery-test-case-context.xml (29 lines)
│   │   │   │   │           └── discovery-test-context.xml (20 lines)
│   │   │   │   └── pom.xml (850 lines)
│   │   │   └── inventory/
│   │   │       ├── src/
│   │   │       │   └── test/
│   │   │       │       ├── java/
│   │   │       │       │   └── com/
│   │   │       │       │       └── cisco/
│   │   │       │       │           └── test/
│   │   │       │       │               └── pi/
│   │   │       │       │                   └── inv/
│   │   │       │       │                       ├── util/
│   │   │       │       │                       │   └── InventoryAppHelper.java (1775 lines)
│   │   │       │       │                       ├── EventBasedInventoryAdminListenerTest.java (45 lines)
│   │   │       │       │                       ├── InventoryAPIsTest.java (296 lines)
│   │   │       │       │                       ├── InventoryAddProfileTest.java (137 lines)
│   │   │       │       │                       ├── InventoryConfigTest.java (620 lines)
│   │   │       │       │                       ├── InventoryDeleteAllDevicesTest.java (90 lines)
│   │   │       │       │                       ├── InventoryDeleteTest.java (227 lines)
│   │   │       │       │                       ├── InventoryDeviceAttrTest.java (457 lines)
│   │   │       │       │                       ├── InventoryDeviceUniqueTest.java (109 lines)
│   │   │       │       │                       ├── InventoryEventBasedTest.java (205 lines)
│   │   │       │       │                       ├── InventoryImportTest.java (760 lines)
│   │   │       │       │                       ├── InventoryLocationTest.java (208 lines)
│   │   │       │       │                       ├── InventoryProfileTest.java (99 lines)
│   │   │       │       │                       ├── InventorySyncTest.java (398 lines)
│   │   │       │       │                       ├── InventoryUDFTest.java (790 lines)
│   │   │       │       │                       ├── InventoryUpdateProfileTest.java (241 lines)
│   │   │       │       │                       └── InventoryUpdateTest.java (528 lines)
│   │   │       │       └── resources/
│   │   │       │           ├── datasets/
│   │   │       │           │   └── com.cisco.test.pi.inv/
│   │   │       │           │       ├── EventBasedInventoryAdminListenerTest.xml (11 lines)
│   │   │       │           │       ├── InventoryAPIsTest.xml (66 lines)
│   │   │       │           │       ├── InventoryAddProfileTest.xml (202 lines)
│   │   │       │           │       ├── InventoryConfigTest.xml (355 lines)
│   │   │       │           │       ├── InventoryDeleteAllDevicesTest.xml (11 lines)
│   │   │       │           │       ├── InventoryDeleteTest.xml (53 lines)
│   │   │       │           │       ├── InventoryDeviceAttrTest.xml (34 lines)
│   │   │       │           │       ├── InventoryDeviceUniqueTest.xml (19 lines)
│   │   │       │           │       ├── InventoryEventBasedTest.xml (68 lines)
│   │   │       │           │       ├── InventoryImportTest.xml (49 lines)
│   │   │       │           │       ├── InventoryLocationTest.xml (80 lines)
│   │   │       │           │       ├── InventoryProfileTest.xml (80 lines)
│   │   │       │           │       ├── InventorySyncTest.xml (49 lines)
│   │   │       │           │       ├── InventoryUDFTest.xml (129 lines)
│   │   │       │           │       ├── InventoryUpdateProfileTest.xml (102 lines)
│   │   │       │           │       └── InventoryUpdateTest.xml (616 lines)
│   │   │       │           ├── suites/
│   │   │       │           │   ├── InventoryAddSmokeTestSuite.xml (25 lines)
│   │   │       │           │   ├── InventoryPreCommitTestSuite.xml (25 lines)
│   │   │       │           │   ├── InventoryPreCommitTestSuiteStaging.xml (25 lines)
│   │   │       │           │   ├── InventoryPreCommitTestSuite_Staging.xml (25 lines)
│   │   │       │           │   ├── InventoryProductionRunSuite_1.xml (87 lines)
│   │   │       │           │   ├── InventoryProductionRunSuite_2.xml (99 lines)
│   │   │       │           │   ├── InventoryProductionRunSuite_3.xml (18 lines)
│   │   │       │           │   ├── InventorySmokeTestSuite.xml (25 lines)
│   │   │       │           │   ├── InventoryUpdateTestSuite.xml (21 lines)
│   │   │       │           │   └── Sanity_InventoryUpdateTestSuite.xml (26 lines)
│   │   │       │           ├── testbeds/
│   │   │       │           │   └── localtestbed.xml (688 lines)
│   │   │       │           ├── pi-inventory-test-case-context.xml (41 lines)
│   │   │       │           ├── pi-inventory-test-context.xml (20 lines)
│   │   │       │           └── pi_inventory.properties (3 lines)
│   │   │       ├── .project (11 lines)
│   │   │       └── pom.xml (585 lines)
│   │   ├── helper/
│   │   │   ├── 360/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── test/
│   │   │   │   │       │               └── pi/
│   │   │   │   │       │                   └── deviceview/
│   │   │   │   │       │                       └── helper/
│   │   │   │   │       │                           ├── DeviceViewHelper.java (192 lines)
│   │   │   │   │       │                           └── DeviceViewImpl.java (1649 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           └── pi-360-helper-test-context.xml (22 lines)
│   │   │   │   └── pom.xml (918 lines)
│   │   │   ├── credentialprofile/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── test/
│   │   │   │   │       │               └── pi/
│   │   │   │   │       │                   └── credentialprofile/
│   │   │   │   │       │                       └── helper/
│   │   │   │   │       │                           ├── CredentialProfileHelperImpl.java (900 lines)
│   │   │   │   │       │                           └── CredentialProfileHelperIntf.java (143 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           └── pi-credentialprofile-helper-test-context.xml (21 lines)
│   │   │   │   └── pom.xml (177 lines)
│   │   │   ├── discovery/
│   │   │   │   ├── src/
│   │   │   │   │   └── test/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── discovery/
│   │   │   │   │       │                       └── helper/
│   │   │   │   │       │                           ├── DiscoveryTestHelper.java (235 lines)
│   │   │   │   │       │                           └── DiscoveryTestHelperImpl.java (1617 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           └── pi-discovery-helper-context.xml (25 lines)
│   │   │   │   └── pom.xml (619 lines)
│   │   │   └── inventory/
│   │   │       ├── src/
│   │   │       │   └── test/
│   │   │       │       ├── java/
│   │   │       │       │   └── com/
│   │   │       │       │       └── cisco/
│   │   │       │       │           └── test/
│   │   │       │       │               └── pi/
│   │   │       │       │                   ├── inv/
│   │   │       │       │                   │   └── helper/
│   │   │       │       │                   │       ├── CredentialEnum.java (119 lines)
│   │   │       │       │                   │       ├── DbQueriesUtilityImpl.java (355 lines)
│   │   │       │       │                   │       ├── DbQueriesUtilityIntf.java (86 lines)
│   │   │       │       │                   │       ├── DeviceMaxSyncTimeEnum.java (55 lines)
│   │   │       │       │                   │       ├── InventoryHelperImpl.java (2179 lines)
│   │   │       │       │                   │       ├── InventoryHelperIntf.java (713 lines)
│   │   │       │       │                   │       ├── InventoryProfileHelperImpl.java (308 lines)
│   │   │       │       │                   │       └── InventoryProfileHelperIntf.java (169 lines)
│   │   │       │       │                   └── inventory/
│   │   │       │       │                       └── helper/
│   │   │       │       │                           ├── CredentialEnum.java (118 lines)
│   │   │       │       │                           ├── DbQueriesUtility.java (297 lines)
│   │   │       │       │                           ├── DeviceMaxSyncTimeEnum.java (51 lines)
│   │   │       │       │                           ├── InventoryHelper.java (696 lines)
│   │   │       │       │                           ├── InventoryHelperImpl.java (1988 lines)
│   │   │       │       │                           ├── InventoryProfileHelper.java (161 lines)
│   │   │       │       │                           └── InventoryProfileHelperImpl.java (327 lines)
│   │   │       │       └── resources/
│   │   │       │           └── pi-inventory-helper-test-context.xml (33 lines)
│   │   │       ├── .project (11 lines)
│   │   │       └── pom.xml (703 lines)
│   │   └── .EMPTY_FOLDER (0 lines)
│   ├── ifm-rest-tests/
│   │   ├── functional_tests/
│   │   │   ├── 360/
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       ├── payload/
│   │   │   │   │       │                       │   ├── 360module.json (36 lines)
│   │   │   │   │       │                       │   └── wirelessControllerPolicy.txt (55 lines)
│   │   │   │   │       │                       ├── CDPNeighborDTO.java (418 lines)
│   │   │   │   │       │                       ├── Device360Constant.java (25 lines)
│   │   │   │   │       │                       ├── Device360Helper.java (340 lines)
│   │   │   │   │       │                       ├── Device360ViewTest.java (304 lines)
│   │   │   │   │       │                       └── DeviceDTO.java (808 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.rest/
│   │   │   │   │           │       └── Device360ViewTest.xml (30 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── BATS_360TestSuite.xml (23 lines)
│   │   │   │   │           │   ├── Device360ViewCFDTestSuite.xml (23 lines)
│   │   │   │   │           │   └── Device360ViewTestSuit.xml (23 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               └── testbed.xml (37 lines)
│   │   │   │   └── pom.xml (177 lines)
│   │   │   ├── credentialprofile/
│   │   │   │   ├── bin/
│   │   │   │   │   └── src/
│   │   │   │   │       └── main/
│   │   │   │   │           ├── java/
│   │   │   │   │           │   └── com/
│   │   │   │   │           │       └── cisco/
│   │   │   │   │           │           └── ifm/
│   │   │   │   │           │               └── test/
│   │   │   │   │           │                   └── rest/
│   │   │   │   │           │                       └── credentialprofile/
│   │   │   │   │           │                           └── payload/
│   │   │   │   │           │                               ├── credential-rest.json (151 lines)
│   │   │   │   │           │                               └── discoverysetting-rest.json (134 lines)
│   │   │   │   │           └── resources/
│   │   │   │   │               ├── datasets/
│   │   │   │   │               │   └── com.cisco.ifm.test.rest.credentialprofile/
│   │   │   │   │               │       ├── CredentialProfileRestTest.xml (54 lines)
│   │   │   │   │               │       └── DiscoverySettingsRestTest.xml (36 lines)
│   │   │   │   │               └── suites/
│   │   │   │   │                   ├── CFD_CredentialProfileTestSuite.xml (23 lines)
│   │   │   │   │                   └── credentialProfileTestSuite.xml (13 lines)
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   ├── config/
│   │   │   │   │       │                   │   └── credentialprofile/
│   │   │   │   │       │                   │       ├── payload/
│   │   │   │   │       │                   │       │   └── credential-rest.json (89 lines)
│   │   │   │   │       │                   │       ├── CredentialProfileConstants.java (7 lines)
│   │   │   │   │       │                   │       ├── CredentialProfileRestTest.java (265 lines)
│   │   │   │   │       │                   │       └── CredentialProfileRestTestHelper.java (161 lines)
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       └── credentialprofile/
│   │   │   │   │       │                           ├── payload/
│   │   │   │   │       │                           │   ├── credential-rest.json (602 lines)
│   │   │   │   │       │                           │   └── discoverysetting-rest.json (231 lines)
│   │   │   │   │       │                           ├── CredentialProfileConstants.java (31 lines)
│   │   │   │   │       │                           ├── CredentialProfileRestTest.java (856 lines)
│   │   │   │   │       │                           ├── CredentialProfileRestTestHelper.java (584 lines)
│   │   │   │   │       │                           └── DiscoverySettingsRestTest.java (445 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   ├── com.cisco.ifm.test.config.credentialprofile/
│   │   │   │   │           │   │   └── CredentialProfileRestTest.xml (33 lines)
│   │   │   │   │           │   └── com.cisco.ifm.test.rest.credentialprofile/
│   │   │   │   │           │       ├── CredentialProfileRestTest.xml (154 lines)
│   │   │   │   │           │       └── DiscoverySettingsRestTest.xml (69 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── BATSCredentialProfileTestSuite.xml (24 lines)
│   │   │   │   │           │   ├── CFD_CredentialProfileTestSuite.xml (23 lines)
│   │   │   │   │           │   └── credentialProfileTestSuite.xml (19 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               └── testbed.xml (18 lines)
│   │   │   │   └── pom.xml (149 lines)
│   │   │   ├── discovery/
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       └── Discovery/
│   │   │   │   │       │                           ├── payload/
│   │   │   │   │       │                           │   └── discovery-rest.json (2977 lines)
│   │   │   │   │       │                           ├── DiscoveryDiffrentProtocolHelper.java (138 lines)
│   │   │   │   │       │                           ├── DiscoveryHelper.java (495 lines)
│   │   │   │   │       │                           └── DiscoveryRestTest.java (3478 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.rest.Discovery/
│   │   │   │   │           │       └── DiscoveryRestTest.xml (864 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── BATSDiscoveryTestSuite.xml (25 lines)
│   │   │   │   │           │   ├── CFD_DiscoveryTestSuite.xml (23 lines)
│   │   │   │   │           │   └── DiscoveryTestSuite.xml (27 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               └── testbed.xml (18 lines)
│   │   │   │   └── pom.xml (166 lines)
│   │   │   ├── inventory/
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       └── inventory/
│   │   │   │   │       │                           ├── payload/
│   │   │   │   │       │                           │   ├── addMnTpolicy.txt (114 lines)
│   │   │   │   │       │                           │   ├── cliTempate.txt (1 lines)
│   │   │   │   │       │                           │   ├── inventory.json (6293 lines)
│   │   │   │   │       │                           │   └── inventoryscrum.json (582 lines)
│   │   │   │   │       │                           ├── CredentialProfileConstants.java (31 lines)
│   │   │   │   │       │                           ├── InvenotyConstants.java (60 lines)
│   │   │   │   │       │                           ├── InventoryHelper.java (1771 lines)
│   │   │   │   │       │                           ├── InventoryScrumRestTest.java (1030 lines)
│   │   │   │   │       │                           └── InventoryTests.java (13092 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.rest.inventory/
│   │   │   │   │           │       ├── InventoryScrumRestTest.xml (291 lines)
│   │   │   │   │           │       └── InventoryTests.xml (3038 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   ├── BATS_InventoryTestSuite.xml (22 lines)
│   │   │   │   │           │   ├── CFD_BR_Upgrade_InventoryTestSuite.xml (23 lines)
│   │   │   │   │           │   ├── CFD_InventoryAlarmTestSuite.xml (22 lines)
│   │   │   │   │           │   ├── CFD_InventoryTestSuite.xml (22 lines)
│   │   │   │   │           │   ├── InventoryDNACMigration.xml (24 lines)
│   │   │   │   │           │   ├── InventoryScrumRestSuite.xml (22 lines)
│   │   │   │   │           │   └── InventoryTestSuite.xml (24 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               ├── inventoryscrumtestbed.xml (17 lines)
│   │   │   │   │               └── testbed.xml (17 lines)
│   │   │   │   └── pom.xml (300 lines)
│   │   │   ├── inventory-dashlets/
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       └── inventory/
│   │   │   │   │       │                           └── dashlets/
│   │   │   │   │       │                               ├── payload/
│   │   │   │   │       │                               │   └── DashletsPayload.json (19 lines)
│   │   │   │   │       │                               └── InventoryDashletsTests.java (148 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.rest.inventory.dashlets/
│   │   │   │   │           │       └── InventoryDashletsTests.xml (13 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   └── InventoryDashletsTestSuite.xml (17 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               └── testbed.xml (27 lines)
│   │   │   │   └── pom.xml (140 lines)
│   │   │   ├── ipsla/
│   │   │   │   ├── .settings/
│   │   │   │   │   ├── org.eclipse.core.resources.prefs (4 lines)
│   │   │   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   │   ├── src/
│   │   │   │   │   └── main/
│   │   │   │   │       ├── java/
│   │   │   │   │       │   └── com/
│   │   │   │   │       │       └── cisco/
│   │   │   │   │       │           └── ifm/
│   │   │   │   │       │               └── test/
│   │   │   │   │       │                   └── rest/
│   │   │   │   │       │                       └── ipsla/
│   │   │   │   │       │                           ├── payload/
│   │   │   │   │       │                           │   └── ipsla.json (129 lines)
│   │   │   │   │       │                           ├── IpSlaConstants.java (20 lines)
│   │   │   │   │       │                           ├── IpSlaHelper.java (153 lines)
│   │   │   │   │       │                           └── IpSlaTests.java (996 lines)
│   │   │   │   │       └── resources/
│   │   │   │   │           ├── datasets/
│   │   │   │   │           │   └── com.cisco.ifm.test.rest.ipsla/
│   │   │   │   │           │       └── IpSlaTests.xml (276 lines)
│   │   │   │   │           ├── suites/
│   │   │   │   │           │   └── IpSlaTestSuite.xml (24 lines)
│   │   │   │   │           └── testbeds/
│   │   │   │   │               └── testbed.xml (16 lines)
│   │   │   │   ├── .classpath (25 lines)
│   │   │   │   ├── .project (23 lines)
│   │   │   │   └── pom.xml (128 lines)
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       ├── java/
│   │   │   │       │   └── com/
│   │   │   │       │       └── cisco/
│   │   │   │       │           └── ifm/
│   │   │   │       │               └── test/
│   │   │   │       │                   └── rest/
│   │   │   │       │                       └── inventory/
│   │   │   │       │                           ├── payload/
│   │   │   │       │                           │   └── inventory.json (202 lines)
│   │   │   │       │                           ├── InvenotyConstants.java (26 lines)
│   │   │   │       │                           ├── InventoryHelper.java (282 lines)
│   │   │   │       │                           └── InventoryTests.java (619 lines)
│   │   │   │       └── resources/
│   │   │   │           ├── datasets/
│   │   │   │           │   └── com.cisco.ifm.test.rest.inventory/
│   │   │   │           │       └── InventoryTests.xml (150 lines)
│   │   │   │           ├── suites/
│   │   │   │           │   └── InventoryTestSuite.xml (17 lines)
│   │   │   │           └── testbeds/
│   │   │   │               └── testbed.xml (17 lines)
│   │   │   └── pom.xml (137 lines)
│   │   └── .EMPTY_FOLDER (0 lines)
│   ├── ifm-ui-tests/
│   │   └── .EMPTY_FOLDER (0 lines)
│   └── xmp-api-tests/
│       ├── functional_tests/
│       │   ├── xmp-credential-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── test/
│       │   │   │       │                   └── credential/
│       │   │   │       │                       ├── CredentialProfileTest.java (907 lines)
│       │   │   │       │                       ├── DBCredTest.java (189 lines)
│       │   │   │       │                       ├── DictionaryEntryTest.java (412 lines)
│       │   │   │       │                       ├── DictionaryEntryTestInContainer.java (421 lines)
│       │   │   │       │                       ├── ISNMP_V3.java (24 lines)
│       │   │   │       │                       ├── ITelnetSSH.java (20 lines)
│       │   │   │       │                       ├── MgrSetupNegativeTest.java (81 lines)
│       │   │   │       │                       ├── SCMGetAttributesForSNMPProtocolTest.java (235 lines)
│       │   │   │       │                       ├── SCMGetAttributesForSNMPProtocolTestInContainer.java (253 lines)
│       │   │   │       │                       ├── SCMGetAttributesForTelnetProtocolTest.java (161 lines)
│       │   │   │       │                       ├── SCMGetAttributesForTelnetProtocolTestInContainer.java (175 lines)
│       │   │   │       │                       ├── SCMNegativeTestInContainer.java (254 lines)
│       │   │   │       │                       ├── SCMNegativeUnitTest.java (224 lines)
│       │   │   │       │                       ├── SCMProtocolTest.java (494 lines)
│       │   │   │       │                       ├── SCMProtocolTestInContainer.java (503 lines)
│       │   │   │       │                       ├── SCMUnitTest.java (325 lines)
│       │   │   │       │                       ├── SCMUnitTestInContainer.java (401 lines)
│       │   │   │       │                       ├── SCMUnitTestInContainerWithMessaging.java (195 lines)
│       │   │   │       │                       ├── TestSetUpMgrWithDatabaseDictionary.java (85 lines)
│       │   │   │       │                       ├── TransactionHelperBean.java (113 lines)
│       │   │   │       │                       ├── TransactionTest.java (77 lines)
│       │   │   │       │                       └── TransactionTestHelper.java (39 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── datasets/
│       │   │   │           │   └── com.cisco.xmp.test.credential/
│       │   │   │           │       ├── CredentialProfileTest.xml (169 lines)
│       │   │   │           │       ├── MgrSetupNegativeTest.xml (25 lines)
│       │   │   │           │       ├── SCMNegativeTestInContainer.xml (48 lines)
│       │   │   │           │       ├── SCMNegativeUnitTest.xml (44 lines)
│       │   │   │           │       ├── SCMUnitTest.xml (88 lines)
│       │   │   │           │       ├── SCMUnitTestInContainer.xml (78 lines)
│       │   │   │           │       └── SCMUnitTestInContainerWithMessaging.xml (21 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   ├── XmpCredentialDataCenterTestSuite.xml (22 lines)
│       │   │   │           │   ├── XmpCredentialSmokeTestSuite.xml (27 lines)
│       │   │   │           │   └── XmpCredentialTestSuite.xml (59 lines)
│       │   │   │           ├── tea-properties/
│       │   │   │           │   └── springdm.test.properties (5 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   └── xmp-credential-testbed.xml (40 lines)
│       │   │   │           ├── dcTest-credential-test.txt (59 lines)
│       │   │   │           ├── log4j.xml (32 lines)
│       │   │   │           ├── xmp-credential-data-center-test-context.xml (91 lines)
│       │   │   │           └── xmp-credential-test-context.xml (93 lines)
│       │   │   └── pom.xml (156 lines)
│       │   ├── xmp-discovery-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── test/
│       │   │   │       │                   └── discovery/
│       │   │   │       │                       ├── CallDiscovery.java (708 lines)
│       │   │   │       │                       ├── DiscoveryIntegrationTest.java (679 lines)
│       │   │   │       │                       ├── DiscoveryInvokerTest.java (1167 lines)
│       │   │   │       │                       ├── DiscoveryModuleTest.java (547 lines)
│       │   │   │       │                       ├── EnvironmentTest.java (73 lines)
│       │   │   │       │                       ├── NGDFilterTest.java (333 lines)
│       │   │   │       │                       ├── NGDNegativeTest.java (526 lines)
│       │   │   │       │                       ├── NGDProtocolTest.java (855 lines)
│       │   │   │       │                       └── PathProvider.java (189 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── META-INF/
│       │   │   │           │   └── spring/
│       │   │   │           │       ├── ICE_expected-results-context.xml (552 lines)
│       │   │   │           │       ├── discovery_expected-results-context.xml (142 lines)
│       │   │   │           │       ├── expected-results-context.out.xml (11 lines)
│       │   │   │           │       ├── expected-results-context.xml (2109 lines)
│       │   │   │           │       └── osgi-context.xml (25 lines)
│       │   │   │           ├── datasets/
│       │   │   │           │   └── com.cisco.xmp.test.discovery/
│       │   │   │           │       ├── DiscoveryIntegrationTest.xml (33 lines)
│       │   │   │           │       ├── DiscoveryInvokerTest.xml (139 lines)
│       │   │   │           │       ├── DiscoveryModuleTest.xml (223 lines)
│       │   │   │           │       ├── NGDFilterTest.xml (125 lines)
│       │   │   │           │       ├── NGDNegativeTest.xml (110 lines)
│       │   │   │           │       └── NGDProtocolTest.xml (384 lines)
│       │   │   │           ├── discoveryTestXMLFiles/
│       │   │   │           │   ├── CDP_AP_Skip_user-config.xml (56 lines)
│       │   │   │           │   ├── ClusterModule.xml (330 lines)
│       │   │   │           │   ├── ClusterModule_DSBUSwitch.xml (328 lines)
│       │   │   │           │   ├── DiffFilterPatternconfig.xml (361 lines)
│       │   │   │           │   ├── DiffFilterRangeconfig.xml (358 lines)
│       │   │   │           │   ├── DiffIPAddressfilterconfig.xml (360 lines)
│       │   │   │           │   ├── DiffIPfilterconfig.xml (358 lines)
│       │   │   │           │   ├── DiffSysLocfilterconfig.xml (358 lines)
│       │   │   │           │   ├── HighestIPV6PrefMultipleGlobalAddPingSweepDiscovery.xml (251 lines)
│       │   │   │           │   ├── HopCountfilterconfig.xml (358 lines)
│       │   │   │           │   ├── IPAddressfilterconfig.xml (353 lines)
│       │   │   │           │   ├── IPIncludefilterconfig.xml (353 lines)
│       │   │   │           │   ├── IPRangefilterconfig.xml (356 lines)
│       │   │   │           │   ├── IPV4PrefPingSweepDiscovery.xml (252 lines)
│       │   │   │           │   ├── IPV4_V6CDPDiscovery.xml (246 lines)
│       │   │   │           │   ├── IPV4_V6PingDiscovery.xml (250 lines)
│       │   │   │           │   ├── IPV6CDPPingDiscovery.xml (328 lines)
│       │   │   │           │   ├── IPV6ExcFilterDiscovery.xml (318 lines)
│       │   │   │           │   ├── IPV6IncFilterDiscovery.xml (318 lines)
│       │   │   │           │   ├── IPV6PrefARPDiscovery.xml (254 lines)
│       │   │   │           │   ├── IPV6PrefCDPDiscovery.xml (252 lines)
│       │   │   │           │   ├── IPV6PrefPingSweepDiscovery.xml (250 lines)
│       │   │   │           │   ├── IPV6PrefPingWithHopDiscovery.xml (253 lines)
│       │   │   │           │   ├── IPV6PrefRTDiscovery.xml (251 lines)
│       │   │   │           │   ├── IPV6SNMPV3Discovery.xml (326 lines)
│       │   │   │           │   ├── Interfacefilterconfig.xml (358 lines)
│       │   │   │           │   ├── InvalidIpAddress_ExcludeIPFilter.xml (347 lines)
│       │   │   │           │   ├── LoopbackIPIncludefilterconfig.xml (356 lines)
│       │   │   │           │   ├── NoIPAddressfilterconfig.xml (352 lines)
│       │   │   │           │   ├── PingSweepDiscoveryModule.xml (324 lines)
│       │   │   │           │   ├── PingSweep_invalidNetmask.xml (328 lines)
│       │   │   │           │   ├── SnmpCredentials_wrongconfig.xml (339 lines)
│       │   │   │           │   ├── Snmpv3AuthNoPriv_userconfig.xml (352 lines)
│       │   │   │           │   ├── Snmpv3NoAuthNoPriv_userconfig.xml (355 lines)
│       │   │   │           │   ├── arpdiscoveryCSCuh25581.xml (374 lines)
│       │   │   │           │   ├── arpdiscoveryconf.xml (351 lines)
│       │   │   │           │   ├── arpdiscoveryv3credconf.xml (360 lines)
│       │   │   │           │   ├── ausdiscoveryconf.xml (353 lines)
│       │   │   │           │   ├── bgpdiscoveryCSCuh25581.xml (375 lines)
│       │   │   │           │   ├── bgpdiscoveryconf.xml (352 lines)
│       │   │   │           │   ├── bgpdiscoveryv3credconf.xml (347 lines)
│       │   │   │           │   ├── cdp_duplicate_config.xml (346 lines)
│       │   │   │           │   ├── cdp_module_userconfig.xml (346 lines)
│       │   │   │           │   ├── cdp_myconfig.xml (346 lines)
│       │   │   │           │   ├── cdpdiscCSCuh25581.xml (350 lines)
│       │   │   │           │   ├── cdpneighborlist.xml (346 lines)
│       │   │   │           │   ├── cdpwithIPv6disabled.xml (329 lines)
│       │   │   │           │   ├── cluster_config.xml (346 lines)
│       │   │   │           │   ├── credential_snmp.xml (339 lines)
│       │   │   │           │   ├── credential_ssh1.xml (325 lines)
│       │   │   │           │   ├── credential_ssh2.xml (324 lines)
│       │   │   │           │   ├── credential_telnet.xml (343 lines)
│       │   │   │           │   ├── credential_telnet_catOs.xml (344 lines)
│       │   │   │           │   ├── device_sysoid.xml (359 lines)
│       │   │   │           │   ├── devices.txt (18 lines)
│       │   │   │           │   ├── devices_v6.txt (3 lines)
│       │   │   │           │   ├── discoveryAssemblySNMPV2.xml (358 lines)
│       │   │   │           │   ├── discoveryAssemblySNMPV3AuthNoPriv.xml (359 lines)
│       │   │   │           │   ├── discoveryfallback_cdp.xml (249 lines)
│       │   │   │           │   ├── discoveryfallback_order.xml (249 lines)
│       │   │   │           │   ├── discoveryfallback_rt.xml (249 lines)
│       │   │   │           │   ├── discoveryv3apcredconf.xml (349 lines)
│       │   │   │           │   ├── discoveryv3apcredconf_3DES.xml (349 lines)
│       │   │   │           │   ├── dns_filter_userconfig.xml (346 lines)
│       │   │   │           │   ├── dnsfilterconfig.xml (359 lines)
│       │   │   │           │   ├── duplicate_device_config.xml (344 lines)
│       │   │   │           │   ├── eboc_interface.xml (347 lines)
│       │   │   │           │   ├── elmidiscoveryconf.xml (354 lines)
│       │   │   │           │   ├── ftestReady.sh (90 lines)
│       │   │   │           │   ├── hsrpdiscoveryCSCuh25581.xml (380 lines)
│       │   │   │           │   ├── hsrpdiscoveryconf.xml (355 lines)
│       │   │   │           │   ├── hsrpdiscoveryv3credconf.xml (353 lines)
│       │   │   │           │   ├── ilmidiscoveryconf.xml (355 lines)
│       │   │   │           │   ├── invalid_config.xml (11 lines)
│       │   │   │           │   ├── invalidhostconf.xml (357 lines)
│       │   │   │           │   ├── iou_cdp_config.xml (346 lines)
│       │   │   │           │   ├── ipv4v6discoveryconf.xml (11 lines)
│       │   │   │           │   ├── ipv6_rtdiscovery.xml (247 lines)
│       │   │   │           │   ├── ipv6discoveryconf.xml (11 lines)
│       │   │   │           │   ├── junk_conf.xml (348 lines)
│       │   │   │           │   ├── layer3moduleNeighbors.xml (354 lines)
│       │   │   │           │   ├── module_cdp_config.xml (337 lines)
│       │   │   │           │   ├── multiple_module_config.xml (348 lines)
│       │   │   │           │   ├── multiple_seed_config.xml (351 lines)
│       │   │   │           │   ├── myconfig.xml (346 lines)
│       │   │   │           │   ├── mysysconfig.xml (247 lines)
│       │   │   │           │   ├── ospfcdpdiscoveryv2credconf.xml (351 lines)
│       │   │   │           │   ├── ospfcdpdiscoveryv3credconf.xml (349 lines)
│       │   │   │           │   ├── ospfdiscoveryCSCuh25581.xml (377 lines)
│       │   │   │           │   ├── ospfdiscoveryconf.xml (354 lines)
│       │   │   │           │   ├── pingSweep_V3_config.xml (347 lines)
│       │   │   │           │   ├── pingSweep_cidr.xml (329 lines)
│       │   │   │           │   ├── pingSweep_cidrmask.xml (248 lines)
│       │   │   │           │   ├── pingSweep_hop_V3_config.xml (347 lines)
│       │   │   │           │   ├── pingSweep_hop_config.xml (64 lines)
│       │   │   │           │   ├── pingSweep_invalidcidr.xml (248 lines)
│       │   │   │           │   ├── pingSweep_seed_config.xml (346 lines)
│       │   │   │           │   ├── pingSweep_unreachable_device_config.xml (346 lines)
│       │   │   │           │   ├── pingSweep_wrong_snmp_cred_config.xml (346 lines)
│       │   │   │           │   ├── pingoutput (17 lines)
│       │   │   │           │   ├── pingsweepdiscCSCuh25581.xml (267 lines)
│       │   │   │           │   ├── pingsweepwithIPv6disabled.xml (248 lines)
│       │   │   │           │   ├── pingsweepwithunreachabledevice.xml (248 lines)
│       │   │   │           │   ├── postIPfilterconfig.xml (343 lines)
│       │   │   │           │   ├── postSysOidfilterconfig.xml (357 lines)
│       │   │   │           │   ├── postsyslocationconfig.xml (358 lines)
│       │   │   │           │   ├── resnamedualstack.xml (330 lines)
│       │   │   │           │   ├── resolvbyname.xml (330 lines)
│       │   │   │           │   ├── resolvbynone.xml (330 lines)
│       │   │   │           │   ├── resolveipaddressconf.xml (359 lines)
│       │   │   │           │   ├── resolvesysname.xml (330 lines)
│       │   │   │           │   ├── routerboundaryfilterconfig.xml (356 lines)
│       │   │   │           │   ├── rtdiscoveryCSCuh25581.xml (379 lines)
│       │   │   │           │   ├── rtdiscoveryconf.xml (357 lines)
│       │   │   │           │   ├── rtwithIPv6disabled.xml (251 lines)
│       │   │   │           │   ├── rtwithIPv6enabled.xml (253 lines)
│       │   │   │           │   ├── sysoidexcfilter.xml (287 lines)
│       │   │   │           │   ├── sysoidincfilter.xml (356 lines)
│       │   │   │           │   ├── system-config-template.xml (246 lines)
│       │   │   │           │   ├── system-config.xml (246 lines)
│       │   │   │           │   ├── system-config1.xml (244 lines)
│       │   │   │           │   ├── system-config_old.xml (244 lines)
│       │   │   │           │   ├── telnetcredential_nullusername.xml (164 lines)
│       │   │   │           │   ├── updatedevice.xml (346 lines)
│       │   │   │           │   ├── user-config-template.xml (349 lines)
│       │   │   │           │   ├── user-config.xml (349 lines)
│       │   │   │           │   ├── userconfig_invaliddependentfile.xml (347 lines)
│       │   │   │           │   ├── userconfig_removedfilter.xml (259 lines)
│       │   │   │           │   ├── userconfig_wrongseedtag.xml (355 lines)
│       │   │   │           │   ├── vpn_config.xml (346 lines)
│       │   │   │           │   ├── vpn_discovery_config.xml (348 lines)
│       │   │   │           │   └── wrongv3credconf.xml (359 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   ├── CIDiscoveryTestSuite.xml (33 lines)
│       │   │   │           │   ├── DiscoveryTestSuite.xml (33 lines)
│       │   │   │           │   ├── XmpDiscoverySmokeTestSuite.xml (35 lines)
│       │   │   │           │   ├── XmpDiscoveryTestSuite.xml (34 lines)
│       │   │   │           │   └── lmsDiscoveryTestSuite.xml (34 lines)
│       │   │   │           ├── tea-properties/
│       │   │   │           │   └── springdm.test.properties (9 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   ├── CI_testbed.xml (57 lines)
│       │   │   │           │   ├── production-testbed.xml (37 lines)
│       │   │   │           │   ├── testbed.xml (57 lines)
│       │   │   │           │   └── xmp-discovery-testbed.xml (54 lines)
│       │   │   │           ├── ICE_expected-results-context.xml (552 lines)
│       │   │   │           ├── discovery_expected-results-context.xml (139 lines)
│       │   │   │           ├── discoveryschema.xsd (492 lines)
│       │   │   │           ├── lms-discovery-test-context.xml (59 lines)
│       │   │   │           ├── log4j.xml (32 lines)
│       │   │   │           ├── xmp-discovery-expected-results-test-context.xml (3196 lines)
│       │   │   │           └── xmp-discovery-test-context.xml (59 lines)
│       │   │   └── pom.xml (357 lines)
│       │   ├── xmp-existence-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── test/
│       │   │   │       │                   └── existence/
│       │   │   │       │                       └── EIEngineTest.java (1550 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── datasets/
│       │   │   │           │   └── com.cisco.xmp.test.existence/
│       │   │   │           │       └── EIEngineTest.xml (622 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   ├── XmpExistenceDataCenterTestSuite.xml (15 lines)
│       │   │   │           │   ├── XmpExistenceSmokeTestSuite.xml (20 lines)
│       │   │   │           │   └── XmpExistenceTestSuite.xml (15 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   └── existence-testbed.xml (50 lines)
│       │   │   │           ├── log4j.xml (32 lines)
│       │   │   │           ├── xmp-existence-datacenter-test-context.xml (30 lines)
│       │   │   │           ├── xmp-existence-expected-results-test-context.xml (176 lines)
│       │   │   │           ├── xmp-existence-module-test-context.xml (25 lines)
│       │   │   │           └── xmp-existence-test-context.xml (30 lines)
│       │   │   └── pom.xml (303 lines)
│       │   ├── xmp-grt-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── grt/
│       │   │   │       │                   └── tests/
│       │   │   │       │                       ├── FaultCorrelationHelperTests.java (123 lines)
│       │   │   │       │                       ├── GRTTestHelper.java (623 lines)
│       │   │   │       │                       ├── GRTTests.java (674 lines)
│       │   │   │       │                       └── GRTUpdateTests.java (122 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── datasets/
│       │   │   │           │   └── com.cisco.xmp.grt.tests/
│       │   │   │           │       └── GRTTests.xml (34 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   └── XmpGRTTestSuite.xml (20 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   ├── xmp-grt-testbed-CI.xml (60 lines)
│       │   │   │           │   └── xmp-grt-testbed.xml (57 lines)
│       │   │   │           ├── log4j.xml (32 lines)
│       │   │   │           └── xmp-grt-test-context.xml (35 lines)
│       │   │   └── pom.xml (228 lines)
│       │   ├── xmp-inventory-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── inventory/
│       │   │   │       │                   └── ice/
│       │   │   │       │                       ├── dc/
│       │   │   │       │                       │   ├── DataCenterBusinessProcessHookTester.java (369 lines)
│       │   │   │       │                       │   ├── DataCenterIceEngineTests.java (1686 lines)
│       │   │   │       │                       │   ├── DataCenterIceEngineTestsMultipleCredentials.java (323 lines)
│       │   │   │       │                       │   ├── DataCenterVidsAnaApiIntegrationTests.java (1458 lines)
│       │   │   │       │                       │   ├── DataCenterVidsAssociationDeleteTests.java (356 lines)
│       │   │   │       │                       │   ├── DataCenterVidsAssociationTests.java (2081 lines)
│       │   │   │       │                       │   ├── DataCenterVidsClusterTests.java (793 lines)
│       │   │   │       │                       │   ├── DataCenterVidsDVSEventTests.java (5 lines)
│       │   │   │       │                       │   ├── DataCenterVidsDVSPortGroupTests.java (5 lines)
│       │   │   │       │                       │   ├── DataCenterVidsDVSPortTests.java (5 lines)
│       │   │   │       │                       │   ├── DataCenterVidsDVSTests.java (5 lines)
│       │   │   │       │                       │   ├── DataCenterVidsDataStoreTestCases.java (898 lines)
│       │   │   │       │                       │   ├── DataCenterVidsEventBasedResourceCounterTestCases.java (1199 lines)
│       │   │   │       │                       │   ├── DataCenterVidsEventWorkflowTests.java (3688 lines)
│       │   │   │       │                       │   ├── DataCenterVidsHostTestCases.java (1441 lines)
│       │   │   │       │                       │   ├── DataCenterVidsHttpCredentialTest.java (1396 lines)
│       │   │   │       │                       │   ├── DataCenterVidsHypervisorTestCases.java (462 lines)
│       │   │   │       │                       │   ├── DataCenterVidsLifeCycleHookTests.java (460 lines)
│       │   │   │       │                       │   ├── DataCenterVidsRefreshAPITests.java (743 lines)
│       │   │   │       │                       │   ├── DataCenterVidsResourceCountersTestCases.java (795 lines)
│       │   │   │       │                       │   ├── DataCenterVidsSupportApiTestCases.java (483 lines)
│       │   │   │       │                       │   ├── DataCenterVidsVmTestCases.java (962 lines)
│       │   │   │       │                       │   ├── DiscoverySourceTestHelper.java (258 lines)
│       │   │   │       │                       │   ├── EventTester.java (3253 lines)
│       │   │   │       │                       │   ├── VIDSTestCases.java (323 lines)
│       │   │   │       │                       │   └── VIDSVManagerApiTestCases.java (1160 lines)
│       │   │   │       │                       └── ft/
│       │   │   │       │                           ├── BusinessProcessHookTester.java (378 lines)
│       │   │   │       │                           ├── CommunicationStateTester.java (516 lines)
│       │   │   │       │                           ├── DuplicateDeviceCheckTests.java (723 lines)
│       │   │   │       │                           ├── DynamicDPLoadTest.java (320 lines)
│       │   │   │       │                           ├── ICEEngineTest.java (5054 lines)
│       │   │   │       │                           ├── ICEEngineTestLocal.java (439 lines)
│       │   │   │       │                           ├── ICEEngineXmpTest.java (440 lines)
│       │   │   │       │                           ├── ICEFragmentBundleTester.java (223 lines)
│       │   │   │       │                           ├── InventoryChangesTest.java (1405 lines)
│       │   │   │       │                           ├── InventoryTesterUtility.java (68 lines)
│       │   │   │       │                           ├── JobManagerTest.java (268 lines)
│       │   │   │       │                           ├── LifeCycleStateTester.java (901 lines)
│       │   │   │       │                           ├── MessagesTest.java (695 lines)
│       │   │   │       │                           ├── PreAndPostCollectionHookTester.java (339 lines)
│       │   │   │       │                           ├── PreCollectionCheckTester.java (200 lines)
│       │   │   │       │                           ├── ReactiveInventoryTest.java (991 lines)
│       │   │   │       │                           ├── SNMPv3AndSSHTest.java (661 lines)
│       │   │   │       │                           └── VerifyCollectedData.java (18 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── datasets/
│       │   │   │           │   ├── com.cisco.xmp.inventory.ice.dc/
│       │   │   │           │   │   ├── DataCenterBusinessProcessHookTester.xml (37 lines)
│       │   │   │           │   │   ├── DataCenterIceEngineTests.xml (468 lines)
│       │   │   │           │   │   ├── DataCenterIceEngineTestsMultipleCredentials.xml (137 lines)
│       │   │   │           │   │   ├── DataCenterVidsAnaApiIntegrationTests.xml (140 lines)
│       │   │   │           │   │   ├── DataCenterVidsAssociationDeleteTests.xml (62 lines)
│       │   │   │           │   │   ├── DataCenterVidsAssociationTests.xml (315 lines)
│       │   │   │           │   │   ├── DataCenterVidsClusterTests.xml (196 lines)
│       │   │   │           │   │   ├── DataCenterVidsDVSEventTests.xml (6 lines)
│       │   │   │           │   │   ├── DataCenterVidsDVSPortGroupTests.xml (6 lines)
│       │   │   │           │   │   ├── DataCenterVidsDVSPortTests.xml (6 lines)
│       │   │   │           │   │   ├── DataCenterVidsDVSTests.xml (6 lines)
│       │   │   │           │   │   ├── DataCenterVidsDataStoreTestCases.xml (187 lines)
│       │   │   │           │   │   ├── DataCenterVidsEventBasedResourceCounterTestCases.xml (117 lines)
│       │   │   │           │   │   ├── DataCenterVidsEventTests.xml (153 lines)
│       │   │   │           │   │   ├── DataCenterVidsEventWorkflowTests.xml (389 lines)
│       │   │   │           │   │   ├── DataCenterVidsHostTestCases.xml (347 lines)
│       │   │   │           │   │   ├── DataCenterVidsHttpCredentialTest.xml (173 lines)
│       │   │   │           │   │   ├── DataCenterVidsHypervisorTestCases.xml (128 lines)
│       │   │   │           │   │   ├── DataCenterVidsLifeCycleHookTests.xml (125 lines)
│       │   │   │           │   │   ├── DataCenterVidsRefreshAPITests.xml (56 lines)
│       │   │   │           │   │   ├── DataCenterVidsResourceCountersTestCases.xml (112 lines)
│       │   │   │           │   │   ├── DataCenterVidsSupportApiTestCases.xml (113 lines)
│       │   │   │           │   │   ├── DataCenterVidsVmTestCases.xml (313 lines)
│       │   │   │           │   │   ├── EventTester.xml (554 lines)
│       │   │   │           │   │   ├── VIDSTestCases.xml (44 lines)
│       │   │   │           │   │   └── VIDSVManagerApiTestCases.xml (301 lines)
│       │   │   │           │   └── com.cisco.xmp.inventory.ice.ft/
│       │   │   │           │       ├── BusinessProcessHookTester.xml (61 lines)
│       │   │   │           │       ├── CommunicationStateTester.xml (77 lines)
│       │   │   │           │       ├── DuplicateDeviceCheckTests.xml (134 lines)
│       │   │   │           │       ├── DynamicDPLoadTest.xml (45 lines)
│       │   │   │           │       ├── EventTester.xml (554 lines)
│       │   │   │           │       ├── ICEEngineTest.xml (836 lines)
│       │   │   │           │       ├── ICEEngineXmpTest.xml (51 lines)
│       │   │   │           │       ├── ICEFragmentBundleTester.xml (28 lines)
│       │   │   │           │       ├── InventoryChangesTest.xml (218 lines)
│       │   │   │           │       ├── JobManagerTest.xml (29 lines)
│       │   │   │           │       ├── LifeCycleStateTester.xml (122 lines)
│       │   │   │           │       ├── MessagesTest.xml (165 lines)
│       │   │   │           │       ├── PreAndPostCollectionHookTester.xml (67 lines)
│       │   │   │           │       ├── PreCollectionCheckTester.xml (39 lines)
│       │   │   │           │       ├── ReactiveInventoryTest.xml (102 lines)
│       │   │   │           │       └── SNMPv3AndSSHTest.xml (189 lines)
│       │   │   │           ├── scale-scripts/
│       │   │   │           │   ├── TC7457.sh (17 lines)
│       │   │   │           │   ├── TC7459.sh (43 lines)
│       │   │   │           │   ├── TC7460.sh (106 lines)
│       │   │   │           │   ├── TC7461.sh (194 lines)
│       │   │   │           │   ├── TC7462.sh (26 lines)
│       │   │   │           │   ├── TC7467.sh (99 lines)
│       │   │   │           │   ├── forcesync.sh (12 lines)
│       │   │   │           │   └── migration.sh (17 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   ├── DataCenterIceTestSuite.xml (19 lines)
│       │   │   │           │   ├── DataCenterPIEventsTestSuite.xml (21 lines)
│       │   │   │           │   ├── DataCenterPITestSuite.xml (20 lines)
│       │   │   │           │   ├── IAC_IceTestSuite.xml (19 lines)
│       │   │   │           │   ├── IA_IceTestSuite.xml (20 lines)
│       │   │   │           │   ├── IceLumosSmokeTestSuite.xml (24 lines)
│       │   │   │           │   ├── IceSmokeTestSuite.xml (23 lines)
│       │   │   │           │   └── IceTestSuite.xml (20 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   ├── XmpInventoryTestBed.xml (171 lines)
│       │   │   │           │   ├── ice-testbed.xml (243 lines)
│       │   │   │           │   └── testbed.xml (50 lines)
│       │   │   │           ├── 7609-entity-mibs-modules.txt (7 lines)
│       │   │   │           ├── 7609-entity-mibs.txt (162 lines)
│       │   │   │           ├── association-results-context.xml (41 lines)
│       │   │   │           ├── crs-mibs-modules.txt (7 lines)
│       │   │   │           ├── expected-results-context.xml (566 lines)
│       │   │   │           ├── ia-ice-test-case-context.xml (71 lines)
│       │   │   │           ├── ia-ice-test-context.xml (23 lines)
│       │   │   │           ├── log4j.xml (78 lines)
│       │   │   │           ├── xmp-iac-ice-test-context.xml (23 lines)
│       │   │   │           ├── xmp-ice-data-center-test-context.xml (116 lines)
│       │   │   │           ├── xmp-ice-test-case-context.xml (93 lines)
│       │   │   │           └── xmp-ice-test-context.xml (23 lines)
│       │   │   ├── pom.xml (449 lines)
│       │   │   ├── settings-rel.xml (111 lines)
│       │   │   └── settings.xml (118 lines)
│       │   ├── xmp-nice-model-test/
│       │   │   ├── facets/
│       │   │   │   └── default.wfc (10 lines)
│       │   │   ├── src/
│       │   │   │   └── com/
│       │   │   │       ├── cisco/
│       │   │   │       │   ├── xmp/
│       │   │   │       │   │   ├── model/
│       │   │   │       │   │   │   ├── nice/
│       │   │   │       │   │   │   │   ├── test/
│       │   │   │       │   │   │   │   │   ├── college/
│       │   │   │       │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   ├── College.java (148 lines)
│       │   │   │       │   │   │   │   │   │   ├── CollegeHasCourse.java (59 lines)
│       │   │   │       │   │   │   │   │   │   ├── Course.java (131 lines)
│       │   │   │       │   │   │   │   │   │   ├── University.java (113 lines)
│       │   │   │       │   │   │   │   │   │   └── UniversityHasColleges.java (59 lines)
│       │   │   │       │   │   │   │   │   ├── company/
│       │   │   │       │   │   │   │   │   │   ├── manytomany/
│       │   │   │       │   │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyOrderedHasClientUniDirJoinEndCompany.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyTransportHasTransportVendorsBiDirJoinEndTransportVendor.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasBenefitsBiDirJoinEndBenefitsBothOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasProjectOrderedBiDirJoinEndProject.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasTrainingUniDirJoinEndEngineerOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerOrderedHasGoalBiDirJoinEndGoal.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerSubscribesMailerUniDirJoinEndEngineerBothOrdered.java (61 lines)
│       │   │   │       │   │   │   │   │   │   │   └── FoodCourtHasFoodVendorsUniDirJoinEndFoodCourt.java (57 lines)
│       │   │   │       │   │   │   │   │   │   ├── onetomany/
│       │   │   │       │   │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasAssetUniDirJoinEndAsset.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasBUBiDirJoinEndBU.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasCampusBiDirJoinEndCampusOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasCompanyTransportsBiDirJoinEndCompanyTransport.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasDistributerBiDIrJoinEndCompany.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasEngineerUniDirJoinEndEngineerOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasHealthInsuranceBiDirJoinEndHealthInsurance.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CompanyHasSupplierBiDirJoinEndCompanyOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasAssetUniDirJoinEndEngineer.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── GradeLevelHasEngineerUniDirJoinEndGradeLevelOrdered.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── HealthInsuranceHasHospitalUniDirJoinEndHospital.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── ManagerHasEmployees.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   └── RecruitmentDriveHasRecruitersBiDirJoinEndRecruiter.java (57 lines)
│       │   │   │       │   │   │   │   │   │   ├── onetoone/
│       │   │   │       │   │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── CampusHasAuditoriumBiDirJoinEndAuditorium.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasParkingspaceBiDirJoinEndParkingSpace.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── EngineerHasWorkspaceUniDirJoinEndEngineer.java (59 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── ManagerGivesPerformanceEvaluation.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   ├── TrainingHasMailerUniDirJoinEndTraining.java (57 lines)
│       │   │   │       │   │   │   │   │   │   │   └── WorkerGivesPerformanceEvaluation.java (57 lines)
│       │   │   │       │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   ├── Asset.java (135 lines)
│       │   │   │       │   │   │   │   │   │   ├── Auditorium.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Benefit.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── BusinessUnit.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── Campus.java (120 lines)
│       │   │   │       │   │   │   │   │   │   ├── Client.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── Company.java (118 lines)
│       │   │   │       │   │   │   │   │   │   ├── CompanyTransport.java (154 lines)
│       │   │   │       │   │   │   │   │   │   ├── Distributer.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── Engineer.java (220 lines)
│       │   │   │       │   │   │   │   │   │   ├── FoodCourt.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── FoodVendor.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Goal.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── GradeLevel.java (98 lines)
│       │   │   │       │   │   │   │   │   │   ├── HealthInsurance.java (120 lines)
│       │   │   │       │   │   │   │   │   │   ├── Hospital.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Mailer.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Parkingspace.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── PerformanceEvaluation.java (239 lines)
│       │   │   │       │   │   │   │   │   │   ├── Project.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── Recruiter.java (134 lines)
│       │   │   │       │   │   │   │   │   │   ├── RecruitmentDrive.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Supplier.java (115 lines)
│       │   │   │       │   │   │   │   │   │   ├── Training.java (137 lines)
│       │   │   │       │   │   │   │   │   │   ├── TransportVendor.java (117 lines)
│       │   │   │       │   │   │   │   │   │   ├── Worker.java (135 lines)
│       │   │   │       │   │   │   │   │   │   └── Workspace.java (115 lines)
│       │   │   │       │   │   │   │   │   ├── movies/
│       │   │   │       │   │   │   │   │   │   ├── .package (31 lines)
│       │   │   │       │   │   │   │   │   │   ├── Movie.java (131 lines)
│       │   │   │       │   │   │   │   │   │   ├── Theatre.java (145 lines)
│       │   │   │       │   │   │   │   │   │   └── TheatreHasMovies.java (59 lines)
│       │   │   │       │   │   │   │   │   └── .package (31 lines)
│       │   │   │       │   │   │   │   └── .package (31 lines)
│       │   │   │       │   │   │   └── .package (31 lines)
│       │   │   │       │   │   ├── nice/
│       │   │   │       │   │   │   ├── model/
│       │   │   │       │   │   │   │   ├── company/
│       │   │   │       │   │   │   │   │   └── .package (31 lines)
│       │   │   │       │   │   │   │   └── .package (31 lines)
│       │   │   │       │   │   │   └── .package (31 lines)
│       │   │   │       │   │   └── .package (31 lines)
│       │   │   │       │   └── .package (31 lines)
│       │   │   │       └── .package (30 lines)
│       │   │   ├── tigerstripe/
│       │   │   │   └── velocity.log.1 (835 lines)
│       │   │   ├── .classpath (8 lines)
│       │   │   ├── .project (40 lines)
│       │   │   ├── .visualstate (13 lines)
│       │   │   ├── pom.xml (266 lines)
│       │   │   ├── tigerstripe.target (15 lines)
│       │   │   └── tigerstripe.xml (66 lines)
│       │   ├── xmp-nice-test/
│       │   │   ├── src/
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── test/
│       │   │   │       │                   └── nice/
│       │   │   │       │                       ├── helper/
│       │   │   │       │                       │   └── NiceTestHelper.java (196 lines)
│       │   │   │       │                       ├── DLOToDLOAssociationsTest.java (846 lines)
│       │   │   │       │                       ├── NICEAssociationsTest.java (983 lines)
│       │   │   │       │                       ├── NICECacheTest.java (560 lines)
│       │   │   │       │                       ├── NICEEngineTest.java (1162 lines)
│       │   │   │       │                       ├── NiceCommonModelAssociationsWithScopeAttributesTests.java (1872 lines)
│       │   │   │       │                       ├── NiceCommonModelDLOToNLOAssociationTests.java (722 lines)
│       │   │   │       │                       ├── NiceCommonModelNLOToNLOAssociationTests.java (603 lines)
│       │   │   │       │                       ├── NiceCommonModelSmartCacheAssociationsTests.java (1040 lines)
│       │   │   │       │                       ├── NiceCommonModelTests.java (1941 lines)
│       │   │   │       │                       ├── TestNICECacheAfterRestart.java (227 lines)
│       │   │   │       │                       └── XMPLoadNICECacheBeforeShutdown.java (343 lines)
│       │   │   │       └── resources/
│       │   │   │           ├── datasets/
│       │   │   │           │   └── com.cisco.xmp.test.nice/
│       │   │   │           │       ├── DLOToDLOAssociationsTest.xml (94 lines)
│       │   │   │           │       ├── NICEAssociationsTest.xml (177 lines)
│       │   │   │           │       ├── NICECacheTest.xml (198 lines)
│       │   │   │           │       ├── NICEEngineTest.xml (197 lines)
│       │   │   │           │       ├── NiceCommonModelAssociationsWithScopeAttributesTests.xml (229 lines)
│       │   │   │           │       ├── NiceCommonModelDLOToNLOAssociationTests.xml (55 lines)
│       │   │   │           │       ├── NiceCommonModelNLOToNLOAssociationTests.xml (57 lines)
│       │   │   │           │       ├── NiceCommonModelSmartCacheAssociationsTests.xml (146 lines)
│       │   │   │           │       ├── NiceCommonModelTests.xml (150 lines)
│       │   │   │           │       ├── TestNICECacheAfterRestart.xml (24 lines)
│       │   │   │           │       └── XMPLoadNICECacheBeforeShutdown.xml (38 lines)
│       │   │   │           ├── suites/
│       │   │   │           │   ├── NiceTestSuite.xml (20 lines)
│       │   │   │           │   └── TestNiceCacheAfterRestart.xml (19 lines)
│       │   │   │           ├── testbeds/
│       │   │   │           │   └── xmp-nice-testbed.xml (33 lines)
│       │   │   │           └── xmp-nice-test-context.xml (41 lines)
│       │   │   └── pom.xml (298 lines)
│       │   └── xmp-test-parent/
│       │       └── pom.xml (825 lines)
│       ├── helper/
│       │   ├── xmp-credential-helper-test/
│       │   │   ├── src/
│       │   │   │   ├── main/
│       │   │   │   │   ├── java/
│       │   │   │   │   │   └── com/
│       │   │   │   │   │       └── cisco/
│       │   │   │   │   │           └── xmp/
│       │   │   │   │   │               └── test/
│       │   │   │   │   │                   └── credential/
│       │   │   │   │   │                       └── helper/
│       │   │   │   │   │                           ├── CredentialItem.java (45 lines)
│       │   │   │   │   │                           ├── DCMHelper.java (689 lines)
│       │   │   │   │   │                           ├── GroupCredential.java (36 lines)
│       │   │   │   │   │                           ├── JMSListener.java (45 lines)
│       │   │   │   │   │                           └── NotificationListener.java (50 lines)
│       │   │   │   │   └── resources/
│       │   │   │   │       └── xmp-credential-test-helper-context.xml (23 lines)
│       │   │   │   └── site/
│       │   │   │       ├── apt/
│       │   │   │       │   ├── behavioral_view.apt (168 lines)
│       │   │   │       │   ├── front_page.apt (81 lines)
│       │   │   │       │   ├── index.apt (139 lines)
│       │   │   │       │   ├── infrastructure_environment_view.apt (168 lines)
│       │   │   │       │   ├── packaging_implementation_view.apt (102 lines)
│       │   │   │       │   ├── rel-notes.apt (32 lines)
│       │   │   │       │   ├── review_action_items.apt (20 lines)
│       │   │   │       │   └── structural_view.apt (95 lines)
│       │   │   │       ├── site.xml (82 lines)
│       │   │   │       └── specification.xml (68 lines)
│       │   │   └── pom.xml (117 lines)
│       │   ├── xmp-discovery-helper-test/
│       │   │   ├── src/
│       │   │   │   ├── main/
│       │   │   │   │   ├── java/
│       │   │   │   │   │   └── com/
│       │   │   │   │   │       └── cisco/
│       │   │   │   │   │           └── xmp/
│       │   │   │   │   │               └── test/
│       │   │   │   │   │                   └── discovery/
│       │   │   │   │   │                       └── helper/
│       │   │   │   │   │                           ├── DeviceInfo.java (146 lines)
│       │   │   │   │   │                           ├── DiscoveryData.java (30 lines)
│       │   │   │   │   │                           └── NGDTestHelper.java (975 lines)
│       │   │   │   │   └── resources/
│       │   │   │   │       ├── dns_filter_userconfig.xml (352 lines)
│       │   │   │   │       ├── helper.artifact.properties (0 lines)
│       │   │   │   │       ├── mapping.xml (35 lines)
│       │   │   │   │       └── xmp-discovery-test-helper-context.xml (23 lines)
│       │   │   │   └── test/
│       │   │   │       ├── java/
│       │   │   │       │   └── com/
│       │   │   │       │       └── cisco/
│       │   │   │       │           └── xmp/
│       │   │   │       │               └── existencediscovery/
│       │   │   │       │                   └── HelperTests.java (16 lines)
│       │   │   │       └── resources/
│       │   │   │           └── HelperTestSuite.xml (9 lines)
│       │   │   └── pom.xml (199 lines)
│       │   ├── xmp-existence-helper-test/
│       │   │   ├── src/
│       │   │   │   ├── main/
│       │   │   │   │   └── java/
│       │   │   │   │       └── com/
│       │   │   │   │           └── cisco/
│       │   │   │   │               └── xmp/
│       │   │   │   │                   └── test/
│       │   │   │   │                       └── existence/
│       │   │   │   │                           └── helper/
│       │   │   │   │                               ├── Association.java (89 lines)
│       │   │   │   │                               ├── Equipment.java (438 lines)
│       │   │   │   │                               ├── EquipmentHolder.java (559 lines)
│       │   │   │   │                               ├── ExistenceInventoryHelper.java (390 lines)
│       │   │   │   │                               ├── ICEVerification.java (104 lines)
│       │   │   │   │                               ├── Join.java (44 lines)
│       │   │   │   │                               ├── ManagedDeviceUtility.java (346 lines)
│       │   │   │   │                               ├── ManagedElementIntf.java (205 lines)
│       │   │   │   │                               ├── ManagedNetworkElem.java (181 lines)
│       │   │   │   │                               └── ManagedNetworkUtility.java (273 lines)
│       │   │   │   └── test/
│       │   │   │       └── java/
│       │   │   │           └── com/
│       │   │   │               └── cisco/
│       │   │   │                   └── xmp/
│       │   │   │                       └── test/
│       │   │   │                           └── existence/
│       │   │   │                               └── helper/
│       │   │   │                                   └── AppTest.java (38 lines)
│       │   │   └── pom.xml (191 lines)
│       │   └── xmp-inventory-helper-test/
│       │       ├── src/
│       │       │   ├── main/
│       │       │   │   ├── java/
│       │       │   │   │   └── com/
│       │       │   │   │       └── cisco/
│       │       │   │   │           └── xmp/
│       │       │   │   │               ├── inventory/
│       │       │   │   │               │   └── helper/
│       │       │   │   │               │       ├── Association.java (87 lines)
│       │       │   │   │               │       ├── AssociationTests.java (105 lines)
│       │       │   │   │               │       ├── DataCenterServiceConnectionUtilities.java (249 lines)
│       │       │   │   │               │       ├── DataCenterUtilities.java (1653 lines)
│       │       │   │   │               │       ├── HelperUtility.java (1146 lines)
│       │       │   │   │               │       ├── HelperUtilityIntf.java (146 lines)
│       │       │   │   │               │       ├── Join.java (43 lines)
│       │       │   │   │               │       ├── LoadEntityMibs.java (812 lines)
│       │       │   │   │               │       ├── Node.java (1766 lines)
│       │       │   │   │               │       ├── RecordFinder.java (139 lines)
│       │       │   │   │               │       ├── TestCollectionNotifierEnhancedImplHook.java (118 lines)
│       │       │   │   │               │       ├── TestCollectionNotifierHook.java (94 lines)
│       │       │   │   │               │       ├── TestCustomDuplicateDetector.java (27 lines)
│       │       │   │   │               │       ├── TestDevicePackageConnectivityCheckFailure.java (18 lines)
│       │       │   │   │               │       ├── TestFeatureExecutionCriteriaHook.java (21 lines)
│       │       │   │   │               │       ├── TestNetworkNotificationIntfHook.java (87 lines)
│       │       │   │   │               │       ├── TestVIDSLifecycleCallback.java (74 lines)
│       │       │   │   │               │       ├── TestVirtualDiscoveryCompletionNotifierHook.java (80 lines)
│       │       │   │   │               │       ├── TestVirtualInventoryDiscoveryNotifierHook.java (45 lines)
│       │       │   │   │               │       └── Utilities.java (307 lines)
│       │       │   │   │               └── test/
│       │       │   │   │                   └── inventory/
│       │       │   │   │                       └── cns/
│       │       │   │   │                           ├── TestCNSInventoryInitializer.java (46 lines)
│       │       │   │   │                           ├── TestCNSInventoryMessageListener.java (46 lines)
│       │       │   │   │                           ├── TestCNSInventoryMessageProcessor.java (247 lines)
│       │       │   │   │                           └── TestCNSInventoryMessagePublisher.java (35 lines)
│       │       │   │   └── resources/
│       │       │   │       ├── xmp-data-center-test-helper-hook-context.xml (28 lines)
│       │       │   │       ├── xmp-ice-cns-test-helper-context.xml (45 lines)
│       │       │   │       ├── xmp-ice-data-center-test-helper-context.xml (33 lines)
│       │       │   │       ├── xmp-ice-test-helper-context.xml (30 lines)
│       │       │   │       └── xmp-ice-test-helper-hook-context.xml (33 lines)
│       │       │   └── test/
│       │       │       └── java/
│       │       │           └── com/
│       │       │               └── cisco/
│       │       │                   └── xmp/
│       │       │                       └── inventory/
│       │       │                           └── helper/
│       │       │                               └── test/
│       │       │                                   └── UtilitiesTester.java (78 lines)
│       │       └── pom.xml (245 lines)
│       └── .EMPTY_FOLDER (0 lines)
├── .gitattributes (55 lines)
├── .gitignore (25 lines)
├── .gitmodules (3 lines)
├── .project (11 lines)
├── CODEOWNERS (3 lines)
├── CONFLICT_FILES.txt (1 lines)
├── Jenkinsfile (194 lines)
├── jacoco-exclusions.properties (15 lines)
├── pom.xml (243 lines)
├── sonar-project.properties (6 lines)
└── sonar_scan.sh (59 lines)
```
