# Repository Tree Report: cw-inventory-collector

- Repository root: `/Users/cmoore/Documents/programming/cw-inventory-collector`
- Included text-like files: `159`
- Included directories: `32`
- Total raw lines: `20070`
- Skipped binary files: `4`
- Skipped ignored-extension files: `5`

```text
cw-inventory-collector/
├── .settings/
│   ├── org.eclipse.core.resources.prefs (5 lines)
│   ├── org.eclipse.jdt.core.prefs (7 lines)
│   └── org.eclipse.m2e.core.prefs (4 lines)
├── conf/
│   ├── ddlmetadata/
│   │   ├── GroupMemberRefPartitionIndex.xml (21 lines)
│   │   ├── ifm_ddlmetadata.xml (64 lines)
│   │   └── xmp_config_ddlmetadata.xml (14 lines)
│   ├── keys/
│   │   ├── encBootstrapKey.prop (2 lines)
│   │   ├── encBootstrapKey.prop.bkp (2 lines)
│   │   ├── enckey.prop (5 lines)
│   │   ├── enckey.prop.bkp (5 lines)
│   │   ├── enckey3.prop (0 lines)
│   │   ├── enckey3.prop.bkp (0 lines)
│   │   ├── server_crt_key.pem (63 lines)
│   │   └── serverkey.pem (34 lines)
│   ├── notificationmetadata/
│   │   ├── ce-notification-metadata.xml (85 lines)
│   │   ├── cem-notification-metadata.xml (95 lines)
│   │   ├── flex-notification-metadata.xml (89 lines)
│   │   ├── l3vpn-notification-metadata.xml (67 lines)
│   │   ├── optical-notifications-metadata.xml (105 lines)
│   │   └── serial-notification-metadata.xml (37 lines)
│   ├── prunemetadata/
│   │   └── pruneconfig.xml (25 lines)
│   ├── schemacreate_listeners/
│   │   └── listener_example.xml (19 lines)
│   ├── ComplianceEngine.properties (21 lines)
│   ├── ComplianceFeatures.properties (9 lines)
│   ├── CompliancePASFeatures.properties (12 lines)
│   ├── TqNotRequired.txt (38 lines)
│   ├── bootstrap.properties (120 lines)
│   ├── cli_preamble.properties (6 lines)
│   ├── credentialdictionary.txt (122 lines)
│   ├── epnm_persistence_config.properties (21 lines)
│   ├── existenceInventory.properties (6 lines)
│   ├── featureExclusion.properties (26 lines)
│   ├── featureExclusion_DISH.properties (27 lines)
│   ├── featureRunResultsCache.properties (17 lines)
│   ├── grouping.properties (9 lines)
│   ├── grt_config.properties (4 lines)
│   ├── ifm_inventory.properties (42 lines)
│   ├── ifm_inventory_cli_dp.properties (7 lines)
│   ├── inventory.properties (144 lines)
│   ├── jdbc.properties (21 lines)
│   ├── jobapprover.properties (10 lines)
│   ├── kafka.properties (13 lines)
│   ├── lockerscanlist.properties (4 lines)
│   ├── lockfilterorder.properties (7 lines)
│   ├── lockrequired.properties (4 lines)
│   ├── mcn.messaging.properties (19 lines)
│   ├── mdfdata.xml (311 lines)
│   ├── messaging.properties (15 lines)
│   ├── methodscanlist.properties (3 lines)
│   ├── modules.properties (1 lines)
│   ├── persistence-init.properties (15 lines)
│   ├── persistence_config.properties (23 lines)
│   ├── persistence_init_log4j2.xml (24 lines)
│   ├── scheduler.properties (12 lines)
│   ├── threadscanlist.properties (3 lines)
│   ├── topology.properties (48 lines)
│   ├── update.mdfid.properties (21 lines)
│   ├── update.properties (19 lines)
│   └── uuid.properties (3 lines)
├── conf_cs/
│   ├── ifm_inventory.properties (50 lines)
│   └── inventory.properties (144 lines)
├── files/
│   ├── getUserAndPass.sh (55 lines)
│   └── verifyDbCreation.sh (83 lines)
├── scan-config/
│   ├── application.properties (6 lines)
│   ├── ignore_paths.properties (8 lines)
│   ├── ignore_statements.properties (4 lines)
│   ├── ignore_variables.properties (3 lines)
│   ├── log_patterns.properties (2 lines)
│   ├── scan_file_types.properties (3 lines)
│   └── sensitive_patterns.properties (18 lines)
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── com/
│   │   │   │   └── cisco/
│   │   │   │       ├── epnm/
│   │   │   │       │   └── inventory/
│   │   │   │       │       ├── collector/
│   │   │   │       │       │   ├── geo/
│   │   │   │       │       │   │   └── InventoryGeoHAHook.java (141 lines)
│   │   │   │       │       │   ├── logger/
│   │   │   │       │       │   │   ├── InventoryCollectorLogger.java (197 lines)
│   │   │   │       │       │   │   └── InventoryCollectorLoggerInf.java (17 lines)
│   │   │   │       │       │   └── profile/
│   │   │   │       │       │       └── CWProfileConfig.java (26 lines)
│   │   │   │       │       ├── controller/
│   │   │   │       │       │   ├── HealthController.java (21 lines)
│   │   │   │       │       │   ├── InventoryController.java (38 lines)
│   │   │   │       │       │   └── LoggerController.java (65 lines)
│   │   │   │       │       ├── grpcservice/
│   │   │   │       │       │   └── DiagnosticCollectorGrpcService.java (75 lines)
│   │   │   │       │       ├── maintenance/
│   │   │   │       │       │   ├── InvCollectorMaintenanceModeTask.java (31 lines)
│   │   │   │       │       │   ├── MaintenanceService.java (50 lines)
│   │   │   │       │       │   └── NotInMaintenance.java (16 lines)
│   │   │   │       │       ├── AppManagementHandlerImpl.java (61 lines)
│   │   │   │       │       ├── ApplicationShowTechHandler.java (69 lines)
│   │   │   │       │       ├── EPNMInventoryBeanConfigImpl.java (30 lines)
│   │   │   │       │       ├── EPNMInventoryCollectorService.java (561 lines)
│   │   │   │       │       ├── HealthUpdater.java (75 lines)
│   │   │   │       │       ├── InvCollectorConductor.java (45 lines)
│   │   │   │       │       └── InventoryBackupRestoreHook.java (48 lines)
│   │   │   │       └── ifm/
│   │   │   │           └── inventory/
│   │   │   │               └── postprocessor/
│   │   │   │                   └── impl/
│   │   │   │                       ├── FaultInventoryCollectionCallbackPlugin.java (70 lines)
│   │   │   │                       └── IFMPostCollectionHook.java (1190 lines)
│   │   │   └── org/
│   │   │       └── hibernate/
│   │   │           └── collection/
│   │   │               └── internal/
│   │   │                   └── AbstractPersistentCollection.java (1356 lines)
│   │   ├── proto/
│   │   │   └── inventory.proto (23 lines)
│   │   └── resources/
│   │       ├── inventory_discovery_process/
│   │       │   ├── inventory-discovery-process-aems-aggregate-synchronizer-context.xml (26 lines)
│   │       │   ├── inventory-discovery-process-cns-module-context.xml (57 lines)
│   │       │   ├── inventory-discovery-process-collection_hooks_context.xml (30 lines)
│   │       │   ├── inventory-discovery-process-ems-extension-app-beans.xml (304 lines)
│   │       │   ├── inventory-discovery-process-ice-module-context.xml (299 lines)
│   │       │   ├── inventory-discovery-process-life_cycle_target_context.xml (53 lines)
│   │       │   ├── inventory-discovery-process-optical-inventory-context.xml (131 lines)
│   │       │   ├── inventory-discovery-process-utilities-module-context.xml (70 lines)
│   │       │   ├── inventory-discovery-process-xmp-common-function-beans.xml (73 lines)
│   │       │   ├── inventory-discovery-process-xmp-grouping-spring-context.xml (64 lines)
│   │       │   ├── inventory-discovery-process-xmp-grt-spring-context.xml (89 lines)
│   │       │   ├── inventory-discovery-process-xmp-jobmanager-context.xml (254 lines)
│   │       │   ├── inventory-discovery-process-xmp-lock-manager-context.xml (53 lines)
│   │       │   ├── inventory-discovery-process-xmp-platform-context.xml (71 lines)
│   │       │   ├── inventory-discovery-process-xmp-threadmanager-context.xml (52 lines)
│   │       │   └── inventory-discovery-process_ifm_ice_fragment_context.xml (84 lines)
│   │       ├── application.properties (27 lines)
│   │       ├── assoc_bean_name.conf (1 lines)
│   │       ├── banner.txt (8 lines)
│   │       ├── beans.xml (48 lines)
│   │       ├── bootstrap.properties (120 lines)
│   │       ├── cli_preamble.properties (6 lines)
│   │       ├── cw-inv-collector-categories.xml (120 lines)
│   │       ├── log4j2-offline.xml (19 lines)
│   │       ├── log4j2.xml (546 lines)
│   │       └── property_placeholder_context.xml (21 lines)
│   └── test/
│       └── java/
│           ├── com/
│           │   └── cisco/
│           │       ├── epnm/
│           │       │   └── inventory/
│           │       │       ├── collector/
│           │       │       │   ├── geo/
│           │       │       │   │   └── InventoryGeoHAHookTest.java (172 lines)
│           │       │       │   ├── logger/
│           │       │       │   │   └── InventoryCollectorLoggerTest.java (226 lines)
│           │       │       │   └── profile/
│           │       │       │       └── CWProfileConfigTest.java (25 lines)
│           │       │       ├── controller/
│           │       │       │   ├── HealthControllerTest.java (45 lines)
│           │       │       │   ├── InventoryControllerTest.java (44 lines)
│           │       │       │   └── LoggerControllerTest.java (100 lines)
│           │       │       ├── grpcservice/
│           │       │       │   └── DiagnosticCollectorGrpcServiceTest.java (198 lines)
│           │       │       ├── maintenance/
│           │       │       │   ├── InvCollectorMaintenanceModeTaskTest.java (45 lines)
│           │       │       │   └── MaintenanceServiceTest.java (67 lines)
│           │       │       ├── AppManagementHandlerImplTest.java (27 lines)
│           │       │       ├── ApplicationShowTechHandlerTest.java (86 lines)
│           │       │       ├── EPNMInventoryBeanConfigImplTest.java (47 lines)
│           │       │       ├── EPNMInventoryCollectorServiceTest.java (471 lines)
│           │       │       ├── HealthUpdaterTest.java (101 lines)
│           │       │       ├── InvCollectorConductorTest.java (42 lines)
│           │       │       ├── InventoryBackupRestoreHookTest.java (27 lines)
│           │       │       └── ifm_inventory.properties (33 lines)
│           │       └── ifm/
│           │           └── inventory/
│           │               └── postprocessor/
│           │                   └── impl/
│           │                       ├── FaultInventoryCollectionCallbackPluginTest.java (117 lines)
│           │                       └── IFMPostCollectionHookTest.java (246 lines)
│           └── org/
│               └── hibernate/
│                   └── collection/
│                       └── internal/
│                           └── AbstractPersistentCollectionTest.java (1472 lines)
├── .classpath (33 lines)
├── .gitignore (4 lines)
├── .project (23 lines)
├── CODEOWNERS (1 lines)
├── Dockerfile (63 lines)
├── Jenkinsfile (396 lines)
├── PULL_REQUEST_TEMPLATE.md (36 lines)
├── README.md (2 lines)
├── automation_version_list.py (56 lines)
├── automation_version_list.txt (40 lines)
├── cs_script.sh (5 lines)
├── cw_inventory_collector_liveness.sh (9 lines)
├── cw_inventory_collector_start.sh (313 lines)
├── exclude.txt (4 lines)
├── jacoco-exclusions.properties (0 lines)
├── pom.xml (6016 lines)
├── readiness.sh (9 lines)
├── settings.xml (229 lines)
├── showtech.sh (12 lines)
├── sonar_scan.sh (65 lines)
└── start_exporter.sh (1 lines)
```
