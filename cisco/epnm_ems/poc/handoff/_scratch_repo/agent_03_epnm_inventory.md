# Agent 03 — EPNM Inventory Repo Tree Extraction

**Source:** `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EPNM/tree-reports/inventory_tree_report.md`
**Report metadata (from header):** 2,561 text-like files, 636 directories, 1,420,340 total raw lines, 76 skipped binary, 33 skipped ignored-extension.
**Repo root per report:** `/Users/cmoore/Documents/programming/EPNM/inventory/inventory`
**Method:** Full linear read (4 segments covering lines 1–3802). No grep, regex, or shell shortcuts.

Names are evidence only. All likelihood judgments below are tagged (High / Medium / Low).

---

## H2 — 1. Repo shape at a glance

The top-level directory layout is narrow and highly regular:

- `comp/` — the bulk of the repo; all the functional Inventory backend components, one sub-module per directory. (High — naming + content volume)
- `model/` — `nbi_inventory_api/` northbound inventory API/DTO tree plus `.EMPTY_FOLDER_IN_SVN` marker.
- `scan-config/` — static scan / SonarQube-style config (application.properties, ignore_paths, sensitive_patterns). (High)
- `test-additions/` — two standalone test Java files (`NodeNotificationListenerUnreachabilityTest.java`, `NodeNotificationListenerUnreachableStateTest.java`). (High)
- `tests/` — integration/functional test aggregator with sub-trees `ifm-api-tests/`, `ifm-rest-tests/`, `ifm-ui-tests/` (empty), `xmp-api-tests/`.
- Root-level files: `.gitattributes`, `.gitignore`, `.gitmodules`, `.project`, `CODEOWNERS`, `CONFLICT_FILES.txt`, `Jenkinsfile` (194 lines), `jacoco-exclusions.properties`, `pom.xml` (243 lines), `sonar-project.properties`, `sonar_scan.sh`.

`comp/` subdirectories (Inventory component modules, in report order):

- `comp/ifm_devices_supported/`
- `comp/ifm_discovery_model/` (essentially empty — only `.project`)
- `comp/ifm_event_inventory_service/`
- `comp/ifm_inventory_rest_provider/`
- `comp/ifm_inventory_service/`
- `comp/ifm_inventory_service_package/`
- `comp/ifm_inventory_ui_metadata_impl/`
- `comp/ifm_inventory_xfn.xfn/`
- `comp/inventory_api/`
- `comp/xmp_existence_inventory/`
- `comp/xmp_grt/` (contains `xmp_grt_core/`, `xmp_grt_model/`)
- `comp/xmp_ice_job_adaptor/`
- `comp/xmp_inventory/` (contains `xmp_collector/`, `xmp_collector_intf/`, `xmp_inventory_error_parser/`, plus `ClearSessionCache/` XDE package)

The two tiers — `ifm_*` (IFM = Infrastructure / Integrated Fault Manager, the Prime Infrastructure-era upper layer) and `xmp_*` (the older XMP / "eXtensible Management Platform" inventory substrate) — strongly suggest a layered design where `ifm_*` sits above `xmp_*`. (Medium-High.)

---

## H2 — 2. Java backend surface

Java is organized per-module under the standard Maven layout `src/main/java/com/cisco/{ifm|xmp|nms}/...` and `src/test/java/...`. Package roots observed:

- `com/cisco/ifm/` — IFM layer (inventory service, event-based inventory, REST providers, metadata).
- `com/cisco/xmp/` — XMP/ICE collector layer, existence inventory, GRT (Global Reference Table), inventory model.
- `com/cisco/nms/` — NMS event correlation tangents (appears inside several modules; small footprint — e.g., `nms/ce/event/correlation/`, `nms/optical/event/correlation/`).
- `com/cisco/nm/xde/` — XDE (Extensible Device Engine) function helpers (`ifm_inventory_xfn.xfn` only).

Layering evidence (all High unless noted):

- **REST / API surface.** `comp/ifm_inventory_rest_provider/.../inventoryrestservice/` with:
  - `InventoryRestService.java` (8,770 lines — by far the largest file; the public REST facade). (High)
  - `InventoryDTOBuilder.java` (3,269 lines) — DTO assembly.
  - `InventoryRestUtil.java`, `ExportDeviceUtil.java` (1,899), `ExportDeviceDBUtil.java` (1,424), `PaginationUtil.java`, `SortCriteriaUtil.java`.
  - `dto/` sub-package with 50+ DTOs (Device, DeviceDTO 921 lines, InterfaceDTO, ModuleDTO, CDPNeighborDTO, LLDPNeighborDTO, VdcDetail*, VPC*, DevicesDTO, RootNodeDTO). (See section 3.)
  - `udfconfigrestservice/UdfRestService.java` — user-defined-fields REST.
  - `syncoffline/SyncOfflineDeviceRestService.java`.

- **Service layer.** `comp/ifm_inventory_service/.../inventoryserviceimpl/`:
  - `InventoryServiceImpl.java` (17,400 lines — the single largest file in the tree; likely the monolithic service implementation). (High)
  - `GetDevice.java` (2,140 lines) — device retrieval implementation.
  - `InventoryUtil.java` (1,310), `InventoryMessageListener.java` (694), `InventoryMessageHandler.java` (308), `MCNChangeNotificationPublisher.java` (513), `DeviceCredentialCheckCallBack.java` (796), `InventoryNotificationDispatcher.java`, `ScheduleDeviceMaintenance*`, `SmartLicensingComplianceReportJob.java`, `AssignDevicesToGroupJob.java`, `BulkDeviceEditJobTask.java`.
  - Enums: `InvEqpmtAdminStateEnum.java`, `InvEqpmtOperStateEnum.java`, `InvEquipmentTypeEnum.java`.

- **Request handlers.** `comp/ifm_inventory_service/.../deviceinventory/`:
  - `DeviceInventoryRequestHandler.java` (1,145), `EMSInterfaceInventoryRequestHandler.java` (305), `SQLQueryConstants.java` (193 — inline SQL constants, High confidence this is a DAO-ish surface).

- **Persistence helpers / DAO-ish.** 
  - `comp/ifm_inventory_service/.../inventoryservice/util/InventoryPersistenceHelper.java` (861).
  - `comp/ifm_inventory_service/.../invhelper/` — `InventoryDBUtil.java`, `InventoryMCNHelper.java`, `InventoryCommonHelper.java`, `SwitchHelper.java` (350), `RowCountUtil.java`.
  - `comp/xmp_grt/xmp_grt_core/.../impl/FaultCorrelationHelperDAO.java` (124) — explicit DAO naming.
  - `comp/xmp_inventory/xmp_collector/.../persistence/ICEDao.java` (458), `ICEDaoIntf.java` (151), `PersistenceFactoryBean.java` (84).

- **Service API / model package** (the interface module): `comp/ifm_inventory_service_package/.../inventoryservice/`:
  - `InventoryService.java` (2,044 lines — looks like the service interface / API contract).
  - `Device.java` (1,159), `DeviceRetrievalCriteria.java` (505), `RetrievalCriteria.java` (207), `UCSInventoryService.java`, `FunctionalCapabilityEnum.java`, `IDeviceDeleteHandler.java`.

- **Aspects / AOP.** `comp/ifm_inventory_service/.../aspects/` — `AuditInventoryAfterAspect.java`, `AuditInventoryAroundAspect.java` (478), `AuditInventoryAspect.java` (298). Also `invcache/impl/InvCacheAspect.java`. Spring AOP is clearly in use. (High)

- **Callback plugins / hooks.** `comp/ifm_inventory_service/.../inventoryserviceplugin/` — 13 Callback/Hook classes (ChassisCallBackImpl, NECallbackImpl, NRCallbackImpl, MEICallbackImpl, PepCallBackImpl, LocationUpdateCallBackImpl, etc.). Strongly suggests a pluggable post-collection hook system. (High)

- **gRPC surface.** `comp/ifm_inventory_service/.../inventory/grpcService/` — `DeviceInventoryApiService.java`, `DeviceSyncApiService.java`, `GroupingGrpcApiService.java`, `GrpcServerManager.java`. Plus `comp/xmp_inventory/xmp_collector/.../grpc/` — `InventoryGrpcClient.java` (253), `InventoryGrpcServer.java` (173), `GrpcUtil.java`, `GrpcConstants.java`, `GRPCConnectivityException.java`, `GrpcLeaderElectorHooks.java`. (High — gRPC is a real wire format here.)

- **Kafka / messaging.** `comp/ifm_inventory_service/.../kafka/dlmnotification/listener/` — `NodeNotificationListener.java` (1,063), `CredentialNotificationListener.java` (678), `DLMNotificationListener.java`. And `kafka/ems/notification/handler/GeoDestinationManagerHandler.java` (802). (High)

Proto definitions (non-Java but Java-adjacent): `comp/inventory_api/src/main/proto/Inventory.proto` (112), `InventoryCollectionNotification.proto` (31). (High — this is the protobuf wire schema for the gRPC layer.)

---

## H2 — 3. Device-model / inventory-data structures

Packages and files whose names strongly indicate device / inventory entity definitions (the "data shape" that matters for the EMS adapter work):

- **Canonical Device service interface + types** — `comp/ifm_inventory_service_package/src/main/java/com/cisco/ifm/inventoryservice/`:
  - `Device.java` (1,159 lines) — almost certainly the central Device domain class. (High)
  - `InventoryService.java` (2,044) — service interface.
  - `DeviceRetrievalCriteria.java`, `RetrievalCriteria.java`, `UCSInventoryService.java`.
  - `dto/InvEquipmentDTO.java`, `dto/InterfaceDTO.java`, `dto/InventoryDeviceItemDTO.java`, `dto/InventoryDeviceSyncTaskDTO.java`, `dto/VPCDetailsDTO.java`, `dto/VDCAllocatedCPUDTO.java`, `dto/LagLinkDTO.java`, `dto/VirtualDomainDTO360.java`, `dto/PortChannelDTO.java`, `dto/MemberInterfaceDTO.java`, `dto/NewPortChannelDetailsDTO.java`, `dto/ScheduleDeviceMaintenanceManagedStateDTO.java`, `dto/LineChartItems*DTO.java`, `dto/CollectionStatusCountDTOList.java`.

- **Inventory model (NIO wrappers)** — `comp/ifm_inventory_service_package/src/main/java/com/cisco/ifm/inventorymodel/`:
  - `NetworkDeviceNioWrapper.java` (678), `InterfaceServiceNioWrapper.java` (295), `LinkNIOWrapper.java` (180), `LocationNioWrapper.java` (145). (High — "NIO wrapper" suggests a façade over native inventory objects. The term "NIO" here is probably Cisco's internal abbreviation, not java.nio.)

- **REST-side DTOs (what the client/UI sees)** — `comp/ifm_inventory_rest_provider/.../inventoryrestservice/dto/`:
  - **Device DTOs:** `Device.java` (211), `DeviceDTO.java` (921), `DeviceDetailsDTO.java` (205), `DeviceInventory.java` (154), `DeviceList.java`, `DeviceLocationDTO.java`, `DeviceCollectionState.java` (311), `DeviceMaintenanceStateDTO.java`, `DevicesAttributesDTO.java`, `DevicesDTO.java`, `DevicesNodeDTO.java`, `DevicesRootDTO.java`, `DeviceExceptionDTO.java`, `DeviceExceptionGridDTO.java`.
  - **Interface / physical:** `InterfaceDTO.java` (336), `ModuleDTO.java` (576).
  - **Neighbors:** `CDPNeighborDTO.java` (427), `CDPNeighborDTO360.java`, `LLDPNeighborDTO.java` (427), `LLDPNeighborDTO360.java`.
  - **VDC / VPC (Nexus data center):** `VdcDetailDTO.java`, `VdcDetailManagedDTO.java`, `VdcDetailResourceSummaryDTO.java`, `VdcDetailResourcesDTO.java`, `VdcDetailSummaryDTO.java`, `VPCConsistencyDTO.java`, `VPCConsistencyViewDTO.java`, `VPCFullDuplex.java`, `VPCHalfDuplex.java`.
  - **Services / config bits:** `Erspan.java`, `Rspan.java`, `Span.java`, `Nbar.java`, `Netflow.java`, `Versions.java`.
  - **Location hierarchy:** `LocationDTO.java` (208), `LocationNmspDTO.java` (516), `SubLocationNodeDTO.java`, `SubLocationsDTO.java`, `RootNodeDTO.java`.
  - **Other:** `VirtualDomainDTO360.java`, `VrfListDTO.java`, `VrfNameDTO.java`, `udfDTO.java`, `passPromptDTO.java`, `passPromptListDTO.java`, `SearchResultsDTO.java`, `UserHeaderDTO.java`, `ManagedNetworkElementsChild.java`, `ScheduleDeviceMaintenanceJobDTO.java`, `ScheduledDevicesMaintenanceManagedJobDTO.java`, `ScheduledDevicesMaintenanceManagedJobList.java`.
  - `ObjectFactory.java` — JAXB-generated factory marker (High). `jaxb.index` present at `resources/com/cisco/ifm/inventoryrestservice/dto/`.

- **UDF (User-Defined Fields) DTOs** — `comp/ifm_inventory_rest_provider/.../udfconf/dto/`: `BulkImportDTO.java`, `BulkImportListDTO.java`, `DeviceOperationStatusDTO.java`, `UdfDTO.java`.

- **Device-support / catalog model** — `comp/ifm_devices_supported/.../devpkg/model/`: `DeviceDetails.java` (261), `DeviceSeriesDetails.java`, `Family.java`, `Series.java`, `DevicesPaging.java`, `FilterParameter.java`, `TreeTable.java` (301), `ObjectSelector.java`. Plus `DeviceSupportService.java` (2,172) and `DevicePackageCoverageService.java` (934). (High — device package / supported-device catalog.)

- **XMP collector model** — `comp/xmp_inventory/xmp_collector/.../model/`:
  - `Interface.java` (621), `ACL.java` (286), `IP.java`, `Equipment.java`.
  - `model/dto/ACLDTO.java`, `model/dto/InterfaceDTO.java` (469).
  - `model/metadata/ACLMetadata.java` (376), `model/metadata/InterfaceMetadata.java` (848) — metadata-driven model. (High)
  - Note: this is inside `src/test/java/` per the tree path — but the classes look like real model classes used as test fixtures or kept alongside tests. (Flagged: check if these are production or test-only before relying on them.)

- **GRT (Global Reference Table) model** — `comp/xmp_grt/xmp_grt_model/.../grt/model/`:
  - `GlobalReference.java` (168), `GlobalRefAltKeys.java` (114).
  - Hibernate mappings: `GlobalRefAltKeys.hbm.xml` (60), `GlobalReference.hbm.xml` (41), `grt_named_queries.hbm.xml` (275). (High — Hibernate-mapped persistence entity. See section 4.)

- **Oracle / persistence signals.** Hibernate `.hbm.xml` files exist (`GlobalRefAltKeys.hbm.xml`, `GlobalReference.hbm.xml`, `ACL.hbm.xml`, `Iterface.hbm.xml` (sic) in `xmp_collector` test resources). `persistence.properties` appears at `comp/xmp_existence_inventory/src/test/resources/persistence.properties` and `comp/xmp_inventory/xmp_collector/.../resources/persistence.properties`. The tree does not name a specific DB vendor; "Oracle" does not appear literally in file paths. (Medium — Hibernate is definitely used; DB vendor inference is not supported by this report alone.)

- **Northbound API DTOs (separate model project)** — `model/nbi_inventory_api/.../com/cisco/ifm/nbi/inventory/`:
  - 40+ `Cluster*DTO.java` files for data center / UCS-style reporting: `ClusterDeviceChassisDTO.java`, `ClusterDeviceLocationDTO.java` (637), `ClusterDeviceModuleDTO.java`, `ClusterDeviceSensorDTO.java`, `ClusterDeviceUDIDTO.java`, `ClusterEnvironmentDTO.java`, `ClusterEtherChannelDTO.java`, `ClusterEthernetInterfaceDTO.java`, `ClusterFEXDTO.java`, `ClusterFanDTO.java`, `ClusterInventoryDetailsDTO.java`, `ClusterInventoryDetailsService.java` (762), `ClusterInventoryInterfaceDTO.java`, `ClusterIpInterfaceDTO.java`, `ClusterPowerSupplyDTO.java`, `ClusterSpanningTreeDTO.java`, `ClusterVlanInterfaceDTO.java`, `ClusterVpc*DTO.java`, `ClusterVtpDTO.java`, etc.
  - Subdirectories for `cdpneighbors/`, `clients/`, `ethernet/`, `lldpneighbors/`, `location/`, `memory/`, `physicalports/`, `stacks/`, `summary/`, `udf/`, `vlan/`, `vpc/`, `vtp/`.
  - Uses Tigerstripe (`tigerstripe.target`, `tigerstripe.xml` at module root) — this is a model-driven code-generation framework from Cisco. (High — this means these DTOs are generated from a model spec, not hand-written. That's relevant: the schema of record is the Tigerstripe model, not the generated .java files.)

---

## H2 — 4. XML configuration

XML is plentiful and serves multiple distinct purposes in this repo:

- **Spring application context files** (primary DI / wiring). Dozens of them under `src/main/resources/META-INF/spring/`, e.g.:
  - `ifm-devicessupported-context.xml` (41), `ifm_event_inventory_service_context.xml` (90), `ifm_inventory_service_context.xml` (266), `ifm_inventory_service_context_apic.xml` (120), `module-context.xml`, `osgi-context.xml`, `xmp-existence-inventory-context.xml` (93), `xmp-grt-spring-context.xml` (89), `ice-module-context.xml` (264), `ice-osgi-context.xml`, `xmp-inventory-context.xml`, `assembly-module-context.xml`, `assembly-osgi-context.xml`, `das-module-context.xml`, `das-osgi-context.xml`, `device-scheduling-context.xml` (121), `xmp-ice-job-adaptor-context.xml`, `ice-job-module-context.xml` (155), `ice-job-osgi-context.xml`, `collector-context.xml`.
  - Presence of both `module-context.xml` and `osgi-context.xml` in the same module is the Spring-DM / OSGi pattern. This codebase is OSGi-bundle-based. (High)

- **AOP / aspect config.** `aop.xml` at `comp/ifm_devices_supported/.../META-INF/`, `comp/ifm_event_inventory_service/.../META-INF/`, `comp/ifm_inventory_service/.../META-INF/` (paired with `ifm_inventory_service_aop.xml`).

- **Hibernate mapping (`.hbm.xml`).** `GlobalRefAltKeys.hbm.xml`, `GlobalReference.hbm.xml`, `grt_named_queries.hbm.xml`, `ACL.hbm.xml`, `Iterface.hbm.xml`. (High)

- **MIB definitions** — `comp/xmp_inventory/xmp_collector/src/main/resources/xdeRuntime/mibs/` and `comp/xmp_inventory/xmp_collector/xde-home/mibs/`:
  - `CISCO-CDP-MIB.my` (828), `CISCO-ENTITY-ASSET-MIB.my`, `CISCO-PRODUCTS-MIB.my` (1,095 / 1,669 in the two copies), `CISCO-SMI.my`, `CISCO-TC.my` (1,654), `CISCO-VTP-MIB.my` (4,986), `AIRESPACE-REF-MIB.my`, `AIRESPACE-SWITCHING-MIB.my` (3,606), `IANAifType-MIB.my`, `INET-ADDRESS-MIB.my`, `MERAKI-CLOUD-CONTROLLER-MIB.mib`, `Q-BRIDGE-MIB.my`, `SNMPv2-TC.my`. (High — these are SNMP MIB source files used by the XDE engine at runtime.)

- **ICE metadata / device model XMLs** — `comp/xmp_inventory/xmp_collector/src/test/resources/ice_metadata/`:
  - `rfm-im-module.xml`, `xmp-im-logical-resource-module.xml`, `xmp-im-physical-resource-module.xml`, `xmp-im-vlan-module-ice-metadata.xml`. (High — ICE = Inventory Collection Engine; these are the inventory metadata modules.)
  - Model XSDs: `ACLSamplePalOutput.xsd`, `InterfaceSamplePalOutput.xsd`, `xmp-im-physical-resource-module.xsd`.
  - PAL XML samples (big): `20kEthernetProtocolEndpoints.xml` (320,002 lines), `20kInterfaceProtocolEndpoints.xml` (300,002 lines), `pal_physical_resources_out.xml`, `xmp-im-connectivity-module_out.xml` (907), `xmp-im-vlan-module-output.xml`. The two 300K-line files alone account for a large fraction of the XML line count.

- **Device catalog / MDF data.** `mdfdata.xml` (6,543 lines) at `comp/xmp_inventory/xmp_collector/src/test/resources/`. MDF = Cisco's Master Device Feature reference. (High.)

- **Inventory-collection-states catalogs.** `InventoryCollectionStates.xml` appears twice: `comp/ifm_inventory_service/.../xml/InventoryCollectionStates.xml` (211), `comp/ifm_inventory_rest_provider/.../dto/InventoryCollectionStates.xml` (148). Likely the enumeration of collection lifecycle states exposed over REST. (High — relevant for POC: Device 360 likely shows these states.)

- **Security / privilege contribution.** `comp/ifm_inventory_rest_provider/src/main/resources/nbi-sec/DeviceDetailPrivileges/DeviceDetailPrivileges.xml` (678) and `SecurityContribution.xsd` (75). (High — REST endpoint privilege map.)

- **UI metadata (tab/dashlet metadata consumed by the classic UI).** `comp/ifm_inventory_ui_metadata_impl/src/main/resources/`:
  - `TabViewMetadata.json` (377), `DeviceDetailTabViewMetadata.json` (386), `DWCViewMetadata.json`, `dwcMetadata.json`, `storm/TabViewMetadata.json`.
  - Handlers: `DWCHandler.java`, `DWCMetadata.java` (228), `UIMetadataHandler.java` (305), `UIMetadataProcessor.java`, `UIdataServiceImpl.java`, `IMetadataHandler.java`.
  - **Relevance to POC — HIGH.** These JSON metadata files likely describe the tab structure of Device Details / Device 360 in the classic UI. If so, they are a concrete source-of-truth for "what tabs/fields the classic view renders."

- **Build / assembly XML.** `pom.xml` everywhere (see section 7). `xmpxde.xml`, `packageDescriptor.xml`, `.xde`, `.par`, `.xsd`, `.rpl`, `.xpa`, `.xft` files in the XDE package directories (`comp/ifm_inventory_xfn.xfn/`, `comp/xmp_inventory/ClearSessionCache/`, `comp/xmp_inventory/xmp_inventory_error_parser/`).

- **Log4j config.** `log4j.xml`, `log4j.properties`, `*-categories.xml` (e.g., `dps-categories.xml`, `ifm_inventory_categories.xml`, `collector_categories.xml`, `xde_categories.xml`, `existence-inventory-categories.xml`, `grt-log4j-categories.xml`).

- **Feature / product mapping properties.** `comp/ifm_devices_supported/.../features/`: `featureMapping.properties` (149), `hiddenMapping.properties` (162), `protocolMapping.properties` (56), `SoftwareCustomMapping.properties`.

- **Test data XML.** Very extensive; under `tests/` see `discoveryTestXMLFiles/` (100+ device-discovery scenario XMLs), `datasets/com.cisco.*/*.xml`, `testbeds/*.xml`. Not directly relevant for the POC but accounts for much of the XML line count.

---

## H2 — 5. Data collection and polling (SNMP / CLI / parsers / scheduled jobs)

Strong presence. These packages and files are the collection substrate:

- **ICE — Inventory Collection Engine** — `comp/xmp_inventory/xmp_collector/src/main/java/com/cisco/xmp/inventory/ice/`:
  - Core engines (largest files in the xmp layer):
    - `InventoryCollectorEngineServiceImpl.java` (3,233), `InventoryCollectorEngineXdeImpl.java` (6,062) — two engine implementations. (High — the XDE-backed engine is the primary production path.)
    - `IceTaskImpl.java` (1,218), `IceCollectorTaskImpl.java` (776), `IceCollectorTaskScheduler.java` (136).
  - Collector tasks (state-machine / workflow steps under `collectortask/`):
    - `CollectorTask.java`, `CollectorTaskStart.java`, `CollectorTaskAcquireLock.java`, `CollectorTaskBootstrapConnectivity.java`, `CollectorTaskBootstrapExecute.java`, `CollectorTaskConnectivityCheck.java` (512), `CollectorTaskExecuteDevicePackages.java` (989), `CollectorTaskCDGExecuteDevicePackages.java` (860), `CollectorTaskManageabilityConfig.java`, `CollectorTaskPostAcquireDeviceLock*.java`, `CollectorTaskPreDPExecute.java`, `CollectorTaskPostDPExecute.java`, `CollectorTaskPostCollection.java`, `CollectorTaskPunctualUpdate.java`, `CollectorTaskUpdateCollectionContext.java`, `CollectorFeatureTask.java` (874), `CollectorFeatureHookTask.java`, `CollectorCDGFeatureTask.java` (427), `LirRigiHelper.java` (452). (High — canonical collector-workflow state machine.)
  - Feature / criteria: `feature/FeatureCheck.java`, `feature/AttributeBasedCriteria.java`, `feature/ObjectBasedCriteria.java`, `feature/HookBasedCriteria.java`, `feature/FeatureRunResult.java`.
  - CDG (Cisco Device Gateway) — `ice/cdg/`:
    - `service/CDGCollectionService.java` (850), `service/CDGConstants.java`, `service/CDGRequestData.java`, `service/CDGResponseData.java`, `dispatcher/CDGResponseDispatcher.java` (372), `handler/GNMIResponseParser.java` (1,042), `handler/SatelliteResponseParser.java` (457), `handler/HeliosNotificationListener.java`, `handler/CollectionJobResultListener.java` (418). (High — gNMI/CDG is a modern southbound collection path.)
  - Polling: `InventoryFeaturePollerTask.java` (557) — explicit poller. (High)

- **Device access / business processor** — `comp/xmp_inventory/xmp_collector/.../deviceaccess/`:
  - `impl/DeviceAccessServiceImpl.java` (331), `impl/PalAdaptorImpl.java` (58), `businessProcessor/BusinessProcessManager.java` (182), `businessProcessor/BusinessProcessorRegistry.java` (158), exceptions (`DeviceInteractionException`, `ActionNotFoundException`, `NonUniqueResponseException`, `NotSupportedException`, `UnexpectedResponseException`).
  - Interfaces in `xmp_collector_intf/.../deviceaccess/`: `DeviceAccessService.java`, `PalAdaptor.java`, `BusinessProcessor.java`, `ActionRegistry.java`, `DuplicateDetector.java`, `datapopulator/ExternalAttributePopulator.java`.
  - "PAL" appears to be Cisco's **Protocol Abstraction Layer** wrapping SNMP/CLI device interactions. (High — PAL is the direct-device channel.)

- **XDE engine packages and PAL actions** — `comp/xmp_inventory/xmp_collector/src/main/resources/BaseInventoryActions/`:
  - SNMP-style parametrized actions (`.par`) and output schemas (`.xsd`):
    - `BaseInterface/getifTable.par`, `getifTableOutput.xsd` (303), `getifXTable.par`, `getifXTableOutput.xsd` (297).
    - `GlobalDeviceInformation/getsysContact.par`, `getsysDescr.par`, `getsysLocation.par`, `getsysName.par`, `getsysObjectID.par` (all with corresponding `*Output.xsd`).
    - `InterfaceBinding/getifStackEntry.par`.
    - `PhysicalStructure/getentPhysicalTable.par`, `getentPhysicalTableOutput.xsd` (394).
  - These are plainly SNMP GET / GET-TABLE definitions driving inventory collection. (High)
  - `xdeRuntime/mibs/` and `xde-home/mibs/` — MIB source files (see section 4).
  - `xde-home/inventoryDefaults/`: 17 `.def` files — `XdeCommonExt.def`, `XdeGenericExt.def`, `XdeIOSExt.def`, `XdeIOSXR.def`, `XdeIOS_ngwc.def`, `XdeMeraki.def`, `XdeSGxExt.def`, `ncsCIMC.def`, `ncsNX-OS.def`, `ncsWAAS.def`, `netconf.def`, `xdeASA_FirePOWER.def`, `xdeAdaptiveSecurityAppliances.def`, `xdeApplicationControlEngine.def`, `xdeIndustrialSecurityAppliance.def`, `xdeME1200.def`. Per-family device definitions. (High)
  - `comp/xmp_inventory/ClearSessionCache/`: per-family `clearCacheParser_xde*.rpl` files for ACSW, ASASW, ASR5K, CATOS, IOS, IOS_EXR, IOS_XR, ME1200, NAM, NX-OS, NX-OS-UCSM, ONS, SCOS, SG500, UCOS, UNIX, WAAS, WLC. (High — confirms breadth of supported device families.)

- **Scheduled jobs.** 
  - `comp/ifm_inventory_service/.../inventoryserviceimpl/`: `ScheduleDeviceMaintenanceJobTask.java` (199), `ScheduleDeviceManagedJobTask.java` (202), `SmartLicensingComplianceReportJob.java` (178), `BulkDeviceEditJobTask.java` (206), `AssignDevicesToGroupJob.java` (310).
  - `comp/xmp_inventory/xmp_collector/.../ice/startup/SchedulingStartupHook.java` (181), `CheckCollectorSyncStateHook.java` (204), `CheckLifeCycleStatePostInitHook.java` (484). (High)

- **Event-based inventory (syslog-driven).** `comp/ifm_event_inventory_service/.../eventbasedinventory/` and `comp/ifm_inventory_service/.../eventbasedinventory/` (two parallel copies):
  - `InventorySyslogProcessor.java` (907 / 773), `InventorySyslogRuleAction.java` (576 / 558), `InterfaceConfigChangeProcessor.java` (740 / 417), `InventoryConfigChangeProcessor.java`, `DeviceReachabilityRuleAction.java`, `GranularInventoryAdapter.java`, `GranularInventoryQueue.java`, `GranularInventoryQueueExecutor.java` (301 / 276), `GranularInventoryRuleAction.java`, `ExpediteInventoryProcessor.java`, `ArchivelogExecutor.java` (475 / 442), `BaseOpticalConfigChangeProcessor.java`, `PhysicalPepChangeProcessor.java`, `StaticRouteConfigChangeProcessor.java`, `EventBasedArchiveIdCache.java`, `EventBasedAdminSettingsListener.java`, `CustomizedGranularInventoryPolicy.java` (751 / 719). (High — event-driven, syslog-triggered partial re-collection.)

- **Flow controllers for event throughput** — `comp/ifm_event_inventory_service/.../eventactions/` and similar:
  - `BurstEventsFlowController.java` (1,128), `ContinousEventsFlowController.java` (612), `CompositeEventsFlowController.java`, `FeatureSyncEventsFlowController.java`, `DuplicateEventsFlowController.java`, `PrioritizedEventsFlowController.java`, `ThresholdEventFlowController.java`, `FlappingEventsFlowController.java`, `FilterPatternFlowController.java` (761). Plus action holders (`BurstEventHolder`, `ContinuousHolderMonitor`, `EventRateDetectionHolder`, `GIDisabledStatusMonitor.java` — 700 lines). (High)

- **Parsers.** `GNMIResponseParser.java` (1,042), `SatelliteResponseParser.java` (457), `PalXMLToPOJOConvertor.java` (891), `ICEMetadataParser.java` (457), `InventoryParserUtilImpl.java` (299), `handlerCodeParser.rpl`, `ruleErrorParser.rpl`, plus `comp/xmp_inventory/xmp_inventory_error_parser/` XDE package. (High)

- **Credential / DLM notification listeners** (Kafka, as noted in section 2).

---

## H2 — 6. Direct device-query paths (bypassing DB)

Ramkrishna noted that "in most cases" the app reads from DB; some paths reach directly. Files whose names suggest direct-device channels:

- **PAL (Protocol Abstraction Layer) direct-device API.** 
  - `comp/xmp_inventory/xmp_collector_intf/.../deviceaccess/PalAdaptor.java` (interface), `DeviceAccessService.java` (104), `BusinessProcessor.java`.
  - `comp/xmp_inventory/xmp_collector/.../deviceaccess/impl/PalAdaptorImpl.java`, `DeviceAccessServiceImpl.java`.
  - Exception types (`DeviceInteractionException`, `UnexpectedResponseException`, `NonUniqueResponseException`, `NotSupportedException`) are device-interaction-specific, strongly implying a runtime path to the device. (High)

- **CDG / gNMI southbound.** `CDGCollectionService.java`, `InventoryGrpcClient.java`, `GNMIResponseParser.java`. These are collection-time paths, not necessarily on-demand user reads, but they're the wire path to the device. (High)

- **Credential check callback.** `comp/ifm_inventory_service/.../inventoryserviceimpl/DeviceCredentialCheckCallBack.java` (796) — "check credentials" is often an on-demand device ping. (Medium-High)

- **Feature poller / punctual update.** `InventoryFeaturePollerTask.java` (557), `CollectorTaskPunctualUpdate.java`, `PunctualUpdateEventHandlerTL1TestImpl.java`. "Punctual update" in Cisco parlance = single-feature, on-demand re-collection. (Medium-High — these are collection triggers that may run synchronously from user actions.)

- **Force-sync / reactive inventory.** Tests named `ReactiveInventoryTest.java` (991), `InventorySyncTest.java` (398), `force-sync.sh`. Indicates a "sync now" path. (Medium)

- **Device manageability check.** `DeviceManageability.java` (109), `DeviceManageabilityCheckFunction.java` (86 — XDE function). (Medium)

- **HTTP/REST southbound to device or to other EPNM microservices?** `InventoryHttpClient.java` (118), `HttpUtil.java`. Purpose ambiguous from name. (Low-Medium)

- **Bootstrap connectivity.** `CollectorTaskBootstrapConnectivity.java`, `BootstrapConnectivityCheckFailureNotification.java`. (High — this is a direct device-reach test.)

None of this is proof of user-facing, bypass-the-DB read paths — it's just the presence of direct-device code. The actual "bypass" Ramkrishna describes would need to be confirmed by tracing what the REST endpoints in `InventoryRestService.java` call into for specific views like Device 360 / Interface 360.

---

## H2 — 7. Build / packaging indicators

- **Root build.** Top-level `pom.xml` (243 lines), `Jenkinsfile` (194 lines), `sonar-project.properties`, `sonar_scan.sh`, `jacoco-exclusions.properties`, `scan-config/` SonarQube-style directory. (High — Maven multi-module with Jenkins CI and SonarQube.)

- **Per-module Maven POMs.** Every `comp/*/` module has its own `pom.xml`; most also have `release-pom.xml.save` (the largest being `comp/ifm_inventory_rest_provider/release-pom.xml.save` at 3,221 lines and `comp/ifm_inventory_service/release-pom.xml.save` at 3,399 lines). Representative main POMs by size:
  - `comp/ifm_inventory_service/pom.xml` (2,373 lines).
  - `comp/ifm_event_inventory_service/pom.xml` (1,786).
  - `comp/ifm_inventory_rest_provider/pom.xml` (1,568).
  - `comp/xmp_existence_inventory/pom.xml` (1,247).
  - `comp/xmp_inventory/pom.xml` (1,230).
  - `comp/xmp_ice_job_adaptor/pom.xml` (1,058).
  - `comp/ifm_inventory_service_package/pom.xml` (1,019).
  - `comp/xmp_inventory/xmp_collector/pom.xml` (752).
  - `comp/xmp_grt/pom.xml` (554).
  - `comp/ifm_inventory_ui_metadata_impl/pom.xml` (528).
  - `comp/inventory_api/pom.xml` (471).
  - `comp/xmp_grt/xmp_grt_core/pom.xml` (389).
  - `comp/ifm_devices_supported/pom.xml` (369).
  - `comp/ifm_inventory_xfn.xfn/pom.xml` (321).
  - `comp/xmp_grt/xmp_grt_model/pom.xml` (184).
  - `comp/xmp_inventory/xmp_collector_intf/pom.xml` (162).
- Plus release-time `settings.xml` / `settings-rel.xml` at module roots.

- **Ant-era build holdovers.** `build.xml` (45 lines) at `comp/ifm_inventory_rest_provider/` and `comp/ifm_inventory_service/`. (Low functional relevance; historical.)

- **Eclipse project metadata.** `.classpath`, `.project`, `.settings/org.eclipse.*.prefs` everywhere — IDE artifacts; not consequential.

- **OSGi.** `MANIFEST.MF` files under `META-INF/` in most modules, plus `osgi-context.xml` files. Confirms OSGi bundle packaging. (High)

- **Tigerstripe.** `tigerstripe.target`, `tigerstripe.xml`, `.visualstate` at `model/nbi_inventory_api/` and `tests/xmp-api-tests/functional_tests/xmp-nice-model-test/`. Model-driven development via Tigerstripe. (High)

- **XDE packaging.** `packageDescriptor.xml`, `xmpxde.xml`, `build.properties`, `.xpa/`, `.xpa.xml`, `.xde`, `.par`, `.rpl`, `.xft` files in `comp/ifm_inventory_xfn.xfn/`, `comp/xmp_inventory/ClearSessionCache/`, `comp/xmp_inventory/xmp_inventory_error_parser/`.

- **Test harness.** `test_suite.xml`, `suite.xml`, `DeviceTestSuite.xml`, `jtestsettings.properties`. Heavy TestNG + JUnit use (inferred from naming).

---

## H2 — 8. Relevance to POC

POC scope is **Inventory (Network Devices, Device Details, Chassis View, Device 360, Interface 360) + Fault Management**, delivered as a classic-view EMS-side UI against EPNM data. The EPNM backend is not modified, but the EMS-side adapter needs to consume the same inventory data shape.

**Primary source-of-truth files for the POC adapter's device / interface data model — HIGH relevance:**

- `comp/ifm_inventory_rest_provider/src/main/java/com/cisco/ifm/inventoryrestservice/InventoryRestService.java` (8,770 lines) — the REST facade the classic UI calls. This defines the contract the EMS-side UI would have to match / replicate.
- `comp/ifm_inventory_rest_provider/src/main/java/com/cisco/ifm/inventoryrestservice/InventoryDTOBuilder.java` (3,269 lines) — how DB/service objects become REST DTOs. This is the mapping the adapter most needs to understand.
- `comp/ifm_inventory_rest_provider/src/main/java/com/cisco/ifm/inventoryrestservice/dto/` — the full set of REST DTOs the classic UI renders. Most-relevant names for each POC view:
  - **Network Devices list:** `Device.java`, `DeviceDTO.java` (921), `DeviceInventory.java`, `DeviceList.java`, `DevicesDTO.java`, `DevicesAttributesDTO.java`, `DevicesNodeDTO.java`, `DevicesRootDTO.java`, `DeviceCollectionState.java`.
  - **Device Details / Device 360:** `DeviceDetailsDTO.java` (205), `DeviceLocationDTO.java`, `DeviceMaintenanceStateDTO.java`, `LocationDTO.java`, `LocationNmspDTO.java`, `ModuleDTO.java` (576), `VdcDetailSummaryDTO.java`, `VdcDetailResourceSummaryDTO.java`, `VdcDetailResourcesDTO.java`.
  - **Chassis View:** `ModuleDTO.java` and `DeviceDetailsDTO.java` likely carry the chassis module structure. Also `comp/ifm_inventory_service/.../inventoryserviceplugin/ChassisCallBackImpl.java` for chassis data population.
  - **Interface 360:** `InterfaceDTO.java` (336), neighbor DTOs `CDPNeighborDTO.java` / `CDPNeighborDTO360.java`, `LLDPNeighborDTO.java` / `LLDPNeighborDTO360.java`, `VirtualDomainDTO360.java`. Note the "360" suffix pattern — these are explicitly the 360-view variants.
- `comp/ifm_inventory_rest_provider/src/main/resources/nbi-sec/DeviceDetailPrivileges/DeviceDetailPrivileges.xml` (678) — the privilege map for Device Details endpoints. Any adapter must respect or re-implement this.
- `comp/ifm_inventory_ui_metadata_impl/src/main/resources/DeviceDetailTabViewMetadata.json` (386), `TabViewMetadata.json` (377), `DWCViewMetadata.json`, `dwcMetadata.json` — **likely the concrete tab structure definitions for Device Details / Device 360 in the classic UI.** This may be the single highest-leverage artifact in the whole repo for POC UI layout work. **Recommend: read these four files end-to-end.**
- `comp/ifm_inventory_service_package/src/main/java/com/cisco/ifm/inventoryservice/Device.java` (1,159) and `InventoryService.java` (2,044) — the service-package (API-contract) view of the domain. A cleaner, higher-level schema than the REST DTOs.

**Secondary relevance — MEDIUM:**

- `model/nbi_inventory_api/` — northbound API DTOs (Tigerstripe-generated). If the POC adapter needs to hit a different API surface than the internal REST, this is the alternate schema.
- `comp/ifm_inventory_service/.../inventoryservice/xml/InventoryCollectionStates.xml` (211) and `.../dto/InventoryCollectionStates.xml` (148) — the enumeration of collection states the UI displays.
- `comp/inventory_api/src/main/proto/Inventory.proto` (112) — gRPC schema; if the EMS adapter uses gRPC rather than REST, this is the contract.
- `comp/ifm_inventory_service/.../deviceinventory/SQLQueryConstants.java` (193) — inline SQL strings reveal the DB-level schema the service reads from.
- `comp/ifm_inventory_service/.../inventoryserviceimpl/GetDevice.java` (2,140) — device retrieval. A good file to trace for "which device attributes come from DB vs. direct query".
- `comp/ifm_inventory_service/.../inventoryservice/util/EMSInterfaceInfoBuilder.java` (710) and `.../deviceinventory/EMSInterfaceInventoryRequestHandler.java` (305) — files explicitly named "EMS" on the EPNM backend side. **Suggestive** that there is already an EMS-facing inventory request path inside EPNM. Worth investigation — the "EMS" here might be the exact integration surface the POC wants to stand on. (Medium-High — flag for follow-up.)

**Lower relevance for this specific POC — LOW:**

- Everything under `tests/` (test harness, scale scripts, testbeds).
- `comp/xmp_grt/` (Global Reference Table — cross-subsystem ID reconciliation; probably not user-facing).
- `comp/xmp_existence_inventory/` (device existence / lifecycle — foundational but not rendered).
- `comp/ifm_inventory_xfn.xfn/` (XDE functions — tiny utility).
- The PAL / collector / XDE layer (`comp/xmp_inventory/xmp_collector/`) — the POC does not re-implement collection.

**Flags / unknowns:**

- The tree report is a faithful inventory of filenames and line counts only. All content-level claims above are inferences from naming. Read the highlighted files before committing to any schema assumption.
- The two copies of `eventbasedinventory/` (in `comp/ifm_event_inventory_service/` and in `comp/ifm_inventory_service/`) may be historical duplication or an intentional split. Not resolvable from tree alone.
- The literal string "Oracle" does not appear in any path in this report. Hibernate is in use (`.hbm.xml`, `persistence.properties`) but the vendor is not declared in filenames. Do not state "Oracle" as fact based on this report.
- Files inside `src/test/java/` that look like production classes (e.g., the `model/` package under `xmp_collector` tests) should be confirmed as test-only before being cited as runtime schema.
