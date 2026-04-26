# Repository Tree Report: cw-inventory

- Repository root: `/Users/cmoore/Documents/programming/cw-inventory`
- Included text-like files: `469`
- Included directories: `106`
- Total raw lines: `135386`
- Skipped binary files: `7`
- Skipped ignored-extension files: `13`

```text
cw-inventory/
├── .claude/
│   └── epnm_to_ems_conversion_2026-04-21/
│       └── goals/
│           └── README.md (11 lines)
├── agentic/
│   ├── init_handoff/
│   │   ├── 00_index.md (142 lines)
│   │   ├── 01_project_overview.md (131 lines)
│   │   ├── 02_engagement_history.md (171 lines)
│   │   ├── 03_objectives_and_scope.md (191 lines)
│   │   ├── 04_strategic_approach.md (185 lines)
│   │   ├── 05_technical_landscape.md (204 lines)
│   │   ├── 06_conversion_patterns_reference.md (366 lines)
│   │   ├── 07_stakeholders_and_organization.md (242 lines)
│   │   ├── 08_repositories_access_and_compliance.md (233 lines)
│   │   ├── 09_work_items.md (425 lines)
│   │   ├── 10_open_questions_and_risks.md (309 lines)
│   │   ├── 11_ways_of_working.md (194 lines)
│   │   ├── _proposed_plan_2026-04-20.md (155 lines)
│   │   └── _tree_snapshot_2026-04-20.md (142 lines)
│   ├── repo-inventory/
│   │   ├── repository_inventory.json (142 lines)
│   │   └── repository_inventory.md (60 lines)
│   ├── scripts/
│   │   ├── repo_analysis/
│   │   │   ├── README.md (38 lines)
│   │   │   ├── count_java_lines.py (188 lines)
│   │   │   ├── count_raw_lines_by_extension.py (226 lines)
│   │   │   ├── generate_repo_tree_report.py (213 lines)
│   │   │   ├── inventory_file_extensions.py (100 lines)
│   │   │   ├── run_ems_cnc_repo_analysis.py (176 lines)
│   │   │   └── run_inventory_defined_analysis.py (353 lines)
│   │   ├── README.md (17 lines)
│   │   └── extract_pdf.py (724 lines)
│   ├── skills/
│   │   └── skill-forge/
│   │       ├── kickoff-prompts/
│   │       │   ├── 01_i_know_what_i_want.md (32 lines)
│   │       │   ├── 02_help_me_understand.md (31 lines)
│   │       │   ├── 03_multi_agent_workflow.md (40 lines)
│   │       │   └── 04_compliance_enforcement.md (39 lines)
│   │       ├── references/
│   │       │   ├── 2026-02-11_agents_subagents.md (663 lines)
│   │       │   ├── 2026-02-11_cross_cutting_patterns.md (553 lines)
│   │       │   ├── 2026-02-11_django_forge_patterns.md (739 lines)
│   │       │   ├── 2026-02-11_hooks_system.md (1204 lines)
│   │       │   ├── 2026-02-11_new_features.md (108 lines)
│   │       │   ├── 2026-02-11_phoenix_patterns.md (671 lines)
│   │       │   ├── 2026-02-11_pr_review_patterns.md (546 lines)
│   │       │   ├── 2026-02-11_scripts_context.md (1007 lines)
│   │       │   ├── 2026-02-11_skill_structure.md (699 lines)
│   │       │   └── 2026-03-28_new_features_update.md (236 lines)
│   │       ├── scripts/
│   │       │   ├── check_agent_write_permissions.py (147 lines)
│   │       │   ├── check_staleness.py (119 lines)
│   │       │   ├── estimate_tokens.py (63 lines)
│   │       │   ├── scaffold.py (461 lines)
│   │       │   └── validate.py (143 lines)
│   │       ├── SKILL.md (530 lines)
│   │       └── VERSION.md (67 lines)
│   └── repo-overview.txt (69 lines)
├── conf/
│   ├── ddlmetadata/
│   │   ├── GroupMemberRefPartitionIndex.xml (21 lines)
│   │   ├── ifm_ddlmetadata.xml (64 lines)
│   │   └── xmp_config_ddlmetadata.xml (14 lines)
│   ├── ifm/
│   │   ├── jobmanager/
│   │   │   └── job_settings.xml (16 lines)
│   │   ├── UserPreference.properties (18 lines)
│   │   ├── ifm_common.properties (13 lines)
│   │   ├── ifm_inventory.properties (31 lines)
│   │   ├── mdfdata.xml (8309 lines)
│   │   ├── portColumnMap.xml (14 lines)
│   │   ├── portTypesList.xml (295 lines)
│   │   └── xmp_default_dynamic_group.xml (52 lines)
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
│   ├── rfm/
│   │   └── classes/
│   │       └── hibernate.properties (4 lines)
│   ├── schemacreate_listeners/
│   │   └── listener_example.xml (19 lines)
│   ├── ClassesToAudit.xml (56 lines)
│   ├── ComplianceEngine.properties (21 lines)
│   ├── ComplianceFeatures.properties (9 lines)
│   ├── CompliancePASFeatures.properties (12 lines)
│   ├── TqNotRequired.txt (38 lines)
│   ├── application.properties (18 lines)
│   ├── assoc_bean_name.conf (1 lines)
│   ├── connection-inv.properties (15 lines)
│   ├── credentialdictionary.txt (123 lines)
│   ├── deviceOnboarding.properties (1 lines)
│   ├── emsNotificationConfig.properties (1 lines)
│   ├── epnm_persistence_config.properties (21 lines)
│   ├── existenceInventory.properties (6 lines)
│   ├── featureExclusion.properties (26 lines)
│   ├── grouping.properties (9 lines)
│   ├── grt_config.properties (4 lines)
│   ├── ifm_inventory.properties (51 lines)
│   ├── inventory.properties (160 lines)
│   ├── jobapprover.properties (10 lines)
│   ├── kafka.properties (16 lines)
│   ├── lockerscanlist.properties (4 lines)
│   ├── lockfilterorder.properties (7 lines)
│   ├── lockrequired.properties (4 lines)
│   ├── mcn.messaging.properties (19 lines)
│   ├── mdfdata.xml (271 lines)
│   ├── messaging.properties (15 lines)
│   ├── methodscanlist.properties (3 lines)
│   ├── modules.properties (1 lines)
│   ├── nbi.properties (3 lines)
│   ├── persistence-init.properties (15 lines)
│   ├── persistence_config.properties (23 lines)
│   ├── persistence_init_log4j2.xml (29 lines)
│   ├── queries.properties (5 lines)
│   ├── scheduler.properties (12 lines)
│   ├── threadscanlist.properties (3 lines)
│   ├── topology.properties (48 lines)
│   ├── update.mdfid.properties (21 lines)
│   ├── update.properties (19 lines)
│   └── uuid.properties (3 lines)
├── conf_cs/
│   ├── ifm_inventory.properties (59 lines)
│   ├── inventory.prop_CS (5 lines)
│   ├── inventory.properties (160 lines)
│   └── jdbc.properties (22 lines)
├── config/
│   └── platform/
│       └── tyk/
│           └── tykConfigmap.json (169 lines)
├── files/
│   ├── createQuartzSchedulerTable.sql (167 lines)
│   ├── createSystemPref.sql (3 lines)
│   ├── executeSQLScript.sh (39 lines)
│   ├── getUserAndPass.sh (55 lines)
│   └── verifyDbCreation.sh (83 lines)
├── keyfiles/
│   ├── UCS_deviceprofile.key (0 lines)
│   ├── xmp_ana_integrator.key (0 lines)
│   ├── xmp_ciscolog.key (1 lines)
│   ├── xmp_ciscolog_log4j.key (0 lines)
│   ├── xmp_collector.key (0 lines)
│   ├── xmp_credential_mgmt.key (0 lines)
│   ├── xmp_dar_device_base_ios.key (0 lines)
│   ├── xmp_datacenter_customization.key (0 lines)
│   ├── xmp_datacenter_pal_handler.key (0 lines)
│   ├── xmp_datasource.key (0 lines)
│   ├── xmp_dbCredential_mgmt.key (0 lines)
│   ├── xmp_decap_linux.key (0 lines)
│   ├── xmp_decap_remote_client.key (0 lines)
│   ├── xmp_existence_inventory.key (0 lines)
│   ├── xmp_grouping_impl.key (0 lines)
│   ├── xmp_grouping_intf.key (0 lines)
│   ├── xmp_grouping_model.key (0 lines)
│   ├── xmp_grouping_spring.key (0 lines)
│   ├── xmp_i18nl10n_exception.key (0 lines)
│   ├── xmp_i18nl10n_exception_handler.key (0 lines)
│   ├── xmp_im_foundation_module.key (0 lines)
│   ├── xmp_im_logical_resource_module.key (0 lines)
│   ├── xmp_im_physical_resource_module.key (0 lines)
│   ├── xmp_im_res_mgr_module.key (0 lines)
│   ├── xmp_jobmodel.key (0 lines)
│   ├── xmp_jobscheduler.key (0 lines)
│   ├── xmp_log4j_dynamic.key (0 lines)
│   ├── xmp_log4j_dynamic_ciscolog.key (0 lines)
│   ├── xmp_log4j_dynamic_slf4j.key (0 lines)
│   ├── xmp_log4j_improved.key (0 lines)
│   ├── xmp_log4j_manager.key (0 lines)
│   ├── xmp_mdf_hook.key (0 lines)
│   ├── xmp_modelFramework.key (0 lines)
│   ├── xmp_nbi_fw_war.key (0 lines)
│   ├── xmp_pal.key (0 lines)
│   ├── xmp_persistence_impl.key (0 lines)
│   ├── xmp_persistence_init.key (0 lines)
│   ├── xmp_persistence_intf.key (0 lines)
│   ├── xmp_persistence_spring.key (0 lines)
│   ├── xmp_usermgmt.key (0 lines)
│   ├── xmp_usermgmt_model.key (0 lines)
│   └── xmp_xde_engine.key (0 lines)
├── nulltemp/
│   └── inventory/
│       └── ExportDevice.csv (0 lines)
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
│   │   │   └── com/
│   │   │       └── cisco/
│   │   │           ├── ems/
│   │   │           │   ├── DBquery/
│   │   │           │   │   ├── Util/
│   │   │           │   │   │   ├── CSVConverter.java (42 lines)
│   │   │           │   │   │   └── QueryValidatorUtil.java (38 lines)
│   │   │           │   │   ├── dto/
│   │   │           │   │   │   ├── DbqueryDto.java (29 lines)
│   │   │           │   │   │   └── QueryResultDTO.java (83 lines)
│   │   │           │   │   └── service/
│   │   │           │   │       ├── impl/
│   │   │           │   │       │   └── DBQueryServiceImpl.java (293 lines)
│   │   │           │   │       └── DBQueryService.java (16 lines)
│   │   │           │   ├── inventory/
│   │   │           │   │   ├── dto/
│   │   │           │   │   │   ├── DeviceFeatureDTO.java (23 lines)
│   │   │           │   │   │   ├── DeviceNodeUUIdSummaryDTO.java (27 lines)
│   │   │           │   │   │   ├── GIRequestDTO.java (28 lines)
│   │   │           │   │   │   ├── InventoryReportJobDTO.java (218 lines)
│   │   │           │   │   │   ├── NodeDetailsSummaryDTO.java (65 lines)
│   │   │           │   │   │   ├── UUIDPerCollStatusRequestDTO.java (35 lines)
│   │   │           │   │   │   └── featureExclusionDTO.java (30 lines)
│   │   │           │   │   ├── reports/
│   │   │           │   │   │   └── ReportResponseDispatcher.java (295 lines)
│   │   │           │   │   └── satellite/
│   │   │           │   │       ├── dto/
│   │   │           │   │       │   ├── SatelliteDTO.java (103 lines)
│   │   │           │   │       │   ├── SatelliteErrorResponse.java (38 lines)
│   │   │           │   │       │   └── SatelliteListResponse.java (83 lines)
│   │   │           │   │       └── service/
│   │   │           │   │           └── SatelliteService.java (247 lines)
│   │   │           │   └── networkinventory/
│   │   │           │       ├── dto/
│   │   │           │       │   ├── CoherentDetailsDTO.java (54 lines)
│   │   │           │       │   ├── DeviceColumnFilter.java (27 lines)
│   │   │           │       │   ├── DeviceColumnFiltersDTO.java (16 lines)
│   │   │           │       │   ├── DevicesFilterDTO.java (30 lines)
│   │   │           │       │   ├── InterfaceDetailQuery.java (49 lines)
│   │   │           │       │   ├── InterfaceDetailsDTO.java (91 lines)
│   │   │           │       │   ├── InterfaceDetailsGetApiRequest.java (95 lines)
│   │   │           │       │   └── OpticalDetailsDTO.java (224 lines)
│   │   │           │       ├── interfacedetails/
│   │   │           │       │   └── EMSInterfaceRestService.java (60 lines)
│   │   │           │       ├── service/
│   │   │           │       │   ├── impl/
│   │   │           │       │   │   ├── IntfAdminStatus.java (51 lines)
│   │   │           │       │   │   ├── IntfOperStatus.java (49 lines)
│   │   │           │       │   │   └── NetworkInventoryServiceImpl.java (1977 lines)
│   │   │           │       │   └── NetworkInventoryService.java (27 lines)
│   │   │           │       ├── util/
│   │   │           │       │   ├── DBQueryRetryUtil.java (84 lines)
│   │   │           │       │   ├── EMSInterfaceInventoryAdaptor.java (185 lines)
│   │   │           │       │   ├── NetworkInventoryAuditUtil.java (137 lines)
│   │   │           │       │   └── NetworkInventoryUtil.java (33 lines)
│   │   │           │       └── NetworkInventoryRestService.java (323 lines)
│   │   │           ├── epnm/
│   │   │           │   ├── LeaderElectorImpl/
│   │   │           │   │   ├── DeviceSyncDistrCacheProcessor.java (137 lines)
│   │   │           │   │   ├── InventoryLeaderElector.java (196 lines)
│   │   │           │   │   └── InventoryLeaderHook.java (175 lines)
│   │   │           │   └── inventory/
│   │   │           │       ├── constants/
│   │   │           │       │   ├── InventoryCacheConstants.java (36 lines)
│   │   │           │       │   └── SQLQueryConstants.java (435 lines)
│   │   │           │       ├── controller/
│   │   │           │       │   ├── HealthController.java (58 lines)
│   │   │           │       │   ├── InventoryController.java (158 lines)
│   │   │           │       │   └── LoggerController.java (66 lines)
│   │   │           │       ├── dataexport/
│   │   │           │       │   ├── dto/
│   │   │           │       │   │   └── ScpConfigDto.java (59 lines)
│   │   │           │       │   ├── AppId.java (48 lines)
│   │   │           │       │   ├── DataExportAsyncConfig.java (29 lines)
│   │   │           │       │   ├── DataExportInventoryHandler.java (17 lines)
│   │   │           │       │   ├── DataExportInventoryHandlerImpl.java (1055 lines)
│   │   │           │       │   ├── DataExportInventoryListener.java (107 lines)
│   │   │           │       │   ├── DataExportInventoryPublisher.java (55 lines)
│   │   │           │       │   ├── DeviceGroupDto.java (15 lines)
│   │   │           │       │   ├── DeviceGroupListDto.java (19 lines)
│   │   │           │       │   ├── ExportJobListener.java (106 lines)
│   │   │           │       │   ├── ExportJobPublisher.java (193 lines)
│   │   │           │       │   ├── ExportJobRequestDto.java (78 lines)
│   │   │           │       │   ├── InventoryCSVExportJob.java (1652 lines)
│   │   │           │       │   └── SwimDataExportService.java (608 lines)
│   │   │           │       ├── dlm/
│   │   │           │       │   ├── Constants.java (14 lines)
│   │   │           │       │   ├── CredentialProfileOnboarder.java (176 lines)
│   │   │           │       │   ├── InventoryAlarmClient.java (66 lines)
│   │   │           │       │   ├── InvetoryAlarmClient.java (45 lines)
│   │   │           │       │   └── XtractDlmNodeAndCred.java (352 lines)
│   │   │           │       ├── geo/
│   │   │           │       │   └── InventoryGeoHAHook.java (115 lines)
│   │   │           │       ├── grouping/
│   │   │           │       │   ├── EXPORT_README.md (538 lines)
│   │   │           │       │   ├── GroupDeviceInventoryService.java (236 lines)
│   │   │           │       │   ├── GroupingClientHelper.java (108 lines)
│   │   │           │       │   └── README.md (358 lines)
│   │   │           │       ├── listener/
│   │   │           │       │   └── Lag8023admemberportsettingsListener.java (174 lines)
│   │   │           │       ├── logger/
│   │   │           │       │   ├── InventoryLogger.java (198 lines)
│   │   │           │       │   └── InventoryLoggerInf.java (17 lines)
│   │   │           │       ├── maintenance/
│   │   │           │       │   ├── InventoryMaintenanceModeTask.java (31 lines)
│   │   │           │       │   ├── MaintenanceService.java (57 lines)
│   │   │           │       │   └── NotInMaintenance.java (16 lines)
│   │   │           │       ├── profile/
│   │   │           │       │   ├── CWProfileConfig.java (34 lines)
│   │   │           │       │   └── LocalProfileConfig.java (33 lines)
│   │   │           │       ├── swagger/
│   │   │           │       │   └── SwaggerConfig.java (34 lines)
│   │   │           │       ├── util/
│   │   │           │       │   ├── CSVWriterUtil.java (410 lines)
│   │   │           │       │   ├── InventoryDecryptionUtil.java (56 lines)
│   │   │           │       │   ├── InventoryRemoteFileUploader.java (257 lines)
│   │   │           │       │   ├── InventorySSHClient.java (245 lines)
│   │   │           │       │   └── ZipCompressionUtil.java (371 lines)
│   │   │           │       ├── xde/
│   │   │           │       │   └── XdeInitInv.java (35 lines)
│   │   │           │       ├── AppManagementHandlerImpl.java (52 lines)
│   │   │           │       ├── ApplicationShowTechHandler.java (71 lines)
│   │   │           │       ├── EPNMInventoryService.java (493 lines)
│   │   │           │       ├── HealthUpdater.java (75 lines)
│   │   │           │       ├── InventoryBackupRestoreHook.java (48 lines)
│   │   │           │       └── InventoryCrossworkPostInit.java (146 lines)
│   │   │           ├── ifm/
│   │   │           │   ├── inventoryrestservice/
│   │   │           │   │   ├── DiagnosticsRestService.java (882 lines)
│   │   │           │   │   ├── InventoryEMSRestService.java (1696 lines)
│   │   │           │   │   ├── InventoryEMSRestUtil.java (833 lines)
│   │   │           │   │   ├── InventoryJobRestService.java (903 lines)
│   │   │           │   │   ├── InventoryRestService.java (9724 lines)
│   │   │           │   │   └── SortCriteriaUtil.java (80 lines)
│   │   │           │   ├── inventoryserviceplugin/
│   │   │           │   │   ├── EBSCaller.java (247 lines)
│   │   │           │   │   └── LocationUpdateCallBackImpl.java (142 lines)
│   │   │           │   └── jobscheduler/
│   │   │           │       ├── rest/
│   │   │           │       │   ├── util/
│   │   │           │       │   │   └── Utils.java (100 lines)
│   │   │           │       │   └── JobSchedulerRestService.java (9671 lines)
│   │   │           │       └── service/
│   │   │           │           └── JobSchedulerServiceImpl.java (6579 lines)
│   │   │           ├── nms/
│   │   │           │   └── nbi/
│   │   │           │       └── epnm/
│   │   │           │           └── restconf/
│   │   │           │               └── xmp/
│   │   │           │                   └── im/
│   │   │           │                       └── ext/
│   │   │           │                           └── restconf/
│   │   │           │                               └── resource/
│   │   │           │                                   └── root/
│   │   │           │                                       └── BulkImportRootResource.java1 (303 lines)
│   │   │           └── xmp/
│   │   │               ├── ice/
│   │   │               │   └── job/
│   │   │               │       └── InventoryParameterCollectionJob.java (1011 lines)
│   │   │               ├── jobmanager/
│   │   │               │   └── postInit/
│   │   │               │       └── JobManagerPostInitHookImpl.java (456 lines)
│   │   │               └── jobnotification/
│   │   │                   └── impl/
│   │   │                       └── JobNotificationManager.java (137 lines)
│   │   └── resources/
│   │       ├── com/
│   │       │   └── cisco/
│   │       │       └── ifm/
│   │       │           └── castor/
│   │       │               └── helper/
│   │       │                   └── ifm-common-castor-mapping-for-inv-service.xml (84 lines)
│   │       ├── ifm/
│   │       │   └── ifm_inventory.properties (31 lines)
│   │       ├── inventory_discovery_process/
│   │       │   ├── inventory-discovery-process-aems-aggregate-synchronizer-context.xml (26 lines)
│   │       │   ├── inventory-discovery-process-collection_hooks_context.xml (28 lines)
│   │       │   ├── inventory-discovery-process-context.xml (33 lines)
│   │       │   ├── inventory-discovery-process-epnm-backend-base-context.xml (11 lines)
│   │       │   ├── inventory-discovery-process-ifm-bean-context.xml (47 lines)
│   │       │   ├── inventory-discovery-process-ifm-grouping-service-context.xml (430 lines)
│   │       │   ├── inventory-discovery-process-ifm-inventory-service-context.xml (204 lines)
│   │       │   ├── inventory-discovery-process-ifm-jobmanager-serv-rest-context.xml (71 lines)
│   │       │   ├── inventory-discovery-process-life_cycle_target_context.xml (51 lines)
│   │       │   ├── inventory-discovery-process-optical-inventory-context.xml (131 lines)
│   │       │   ├── inventory-discovery-process-xmp-common-function-beans.xml (75 lines)
│   │       │   ├── inventory-discovery-process-xmp-grouping-spring-context.xml (62 lines)
│   │       │   ├── inventory-discovery-process-xmp-grt-spring-context.xml (89 lines)
│   │       │   ├── inventory-discovery-process-xmp-jobmanager-context.xml (379 lines)
│   │       │   ├── inventory-discovery-process-xmp-platform-context.xml (66 lines)
│   │       │   ├── inventory-discovery-process_ems-extension-app-beans.xml (298 lines)
│   │       │   ├── inventory-discovery-process_ifm_ice_fragment_context.xml (67 lines)
│   │       │   ├── inventory-discovery-process_ifm_template_rest_context.xml (34 lines)
│   │       │   ├── inventory-discovery-process_ifm_template_service_impl_context.xml (52 lines)
│   │       │   ├── inventory-discovery-process_xmp-audit-components-context.xml (107 lines)
│   │       │   └── xmp-xde-init-context.xml (37 lines)
│   │       ├── TaskCategoryMapping.xml (119 lines)
│   │       ├── ThreadManagerConfig.xml (43 lines)
│   │       ├── application.properties (39 lines)
│   │       ├── assoc_bean_name.conf (1 lines)
│   │       ├── banner.txt (8 lines)
│   │       ├── beans.xml (71 lines)
│   │       ├── bootstrap.properties (120 lines)
│   │       ├── cli_preamble.properties (6 lines)
│   │       ├── cns-module-context.xml (57 lines)
│   │       ├── config-module-context.xml (191 lines)
│   │       ├── config-module-plugin-context.xml (25 lines)
│   │       ├── cw-inventory-categories.xml (152 lines)
│   │       ├── dbcreation-context.xml (66 lines)
│   │       ├── deviceOnboarding.properties (1 lines)
│   │       ├── distributed-cache-context.xml (21 lines)
│   │       ├── ems-extension-app-beans.xml (273 lines)
│   │       ├── epnm-mcn-service-context.xml (54 lines)
│   │       ├── ha_hooks_context.xml (28 lines)
│   │       ├── ice-module-context.xml (264 lines)
│   │       ├── ice-module-context_lockProxy.xml (243 lines)
│   │       ├── ifm_common_context.xml (77 lines)
│   │       ├── ifm_grouping_service_context.xml (466 lines)
│   │       ├── ifm_inventory_service_context.xml (326 lines)
│   │       ├── log4j2-offline.xml (19 lines)
│   │       ├── log4j2.xml (642 lines)
│   │       ├── mbc.globalobject_types.properties (11 lines)
│   │       ├── mbc_config.properties (9 lines)
│   │       ├── mbc_customtags.properties (1 lines)
│   │       ├── mbc_globalobject_types.properties (11 lines)
│   │       ├── mcn.messaging.properties (19 lines)
│   │       ├── messaging.properties (15 lines)
│   │       ├── nbi-beans.xml (88 lines)
│   │       ├── nbi.properties (3 lines)
│   │       ├── optical_inventory_context.xml (72 lines)
│   │       ├── persistence-init.properties (16 lines)
│   │       ├── persistence_config.properties (23 lines)
│   │       ├── presentation-root-context.xml (105 lines)
│   │       ├── presentation_base.xml (270 lines)
│   │       ├── presentation_marshalling.xml (105 lines)
│   │       ├── rateLimiter.xml (94 lines)
│   │       ├── utilities-module-context.xml (66 lines)
│   │       ├── xmp-existence-inventory-context.xml (112 lines)
│   │       ├── xmp-grouping-spring-context.xml (67 lines)
│   │       ├── xmp-grt-spring-context.xml (89 lines)
│   │       ├── xmp-lock-manager-context.xml (53 lines)
│   │       ├── xmp-messaging-context.xml (71 lines)
│   │       ├── xmp-persistence-context-dbconn.xml (31 lines)
│   │       ├── xmp-persistence-context.xml (333 lines)
│   │       ├── xmp-persistence-init-context.xml (80 lines)
│   │       └── xmp-xde-init-context.xml (28 lines)
│   └── test/
│       ├── com/
│       │   └── cisco/
│       │       └── ems/
│       │           └── DBquery/
│       │               └── dto/
│       │                   └── DbqueryDtoTest.java (46 lines)
│       └── java/
│           └── com/
│               └── cisco/
│                   ├── ems/
│                   │   ├── DBquery/
│                   │   │   ├── Util/
│                   │   │   │   ├── CSVConverterTest.java (103 lines)
│                   │   │   │   └── QueryValidatorUtilTest.java (82 lines)
│                   │   │   ├── dto/
│                   │   │   │   └── QueryResultDTOTest.java (120 lines)
│                   │   │   └── service/
│                   │   │       ├── impl/
│                   │   │       │   └── DBQueryServiceImplTest.java (341 lines)
│                   │   │       └── DBQueryServiceTest.java (80 lines)
│                   │   ├── inventory/
│                   │   │   ├── dto/
│                   │   │   │   ├── DeviceNodeUUIdSummaryDTOTest.java (23 lines)
│                   │   │   │   ├── GIRequestDTOTest.java (59 lines)
│                   │   │   │   ├── NodeDetailsSummaryDTOTest.java (127 lines)
│                   │   │   │   ├── ReportResponseDispatcherTest.java (1178 lines)
│                   │   │   │   ├── UUIDPerCollStatusRequestDTOTest.java (63 lines)
│                   │   │   │   └── featureExclusionDTOTest.java (30 lines)
│                   │   │   └── satellite/
│                   │   │       ├── dto/
│                   │   │       │   ├── SatelliteDTOTest.java (259 lines)
│                   │   │       │   ├── SatelliteErrorResponseTest.java (321 lines)
│                   │   │       │   └── SatelliteListResponseTest.java (325 lines)
│                   │   │       └── service/
│                   │   │           └── SatelliteServiceTest.java (520 lines)
│                   │   └── networkinventory/
│                   │       ├── dto/
│                   │       │   ├── CoherentDetailsDTOTest.java (32 lines)
│                   │       │   ├── InterfaceDetailQueryTest.java (31 lines)
│                   │       │   ├── InterfaceDetailsDTOTest.java (159 lines)
│                   │       │   ├── InterfaceDetailsGetApiRequestTest.java (44 lines)
│                   │       │   └── OpticalDetailsDTOTest.java (41 lines)
│                   │       ├── interfacedetails/
│                   │       │   └── EMSInterfaceRestServiceTest.java (95 lines)
│                   │       ├── service/
│                   │       │   └── impl/
│                   │       │       ├── IntfAdminStatusTest.java (18 lines)
│                   │       │       ├── IntfOperStatusTest.java (20 lines)
│                   │       │       └── NetworkInventoryServiceImplTest.java (1632 lines)
│                   │       ├── util/
│                   │       │   ├── EMSInterfaceInventoryAdaptorTest.java (109 lines)
│                   │       │   └── NetworkInventoryUtilTest.java (14 lines)
│                   │       └── NetworkInventoryRestServiceTest.java (355 lines)
│                   ├── epnm/
│                   │   ├── LeaderElectorImpl/
│                   │   │   ├── DeviceSyncDistrCacheProcessorTest.java (86 lines)
│                   │   │   ├── InventoryLeaderElectorTest.java (133 lines)
│                   │   │   └── InventoryLeaderHookTest.java (89 lines)
│                   │   └── inventory/
│                   │       ├── controller/
│                   │       │   ├── HealthControllerTest.java (38 lines)
│                   │       │   ├── InventoryControllerTest.java (169 lines)
│                   │       │   └── LoggerControllerTest.java (41 lines)
│                   │       ├── dataexport/
│                   │       │   ├── dto/
│                   │       │   │   └── ScpConfigDtoTest.java (325 lines)
│                   │       │   ├── AppIdTest.java (168 lines)
│                   │       │   ├── DataExportAsyncConfigTest.java (167 lines)
│                   │       │   ├── DataExportInventoryHandlerImplTest.java (552 lines)
│                   │       │   ├── DataExportInventoryListenerTest.java (452 lines)
│                   │       │   ├── DataExportInventoryPublisherTest.java (451 lines)
│                   │       │   ├── DeviceGroupDtoTest.java (209 lines)
│                   │       │   ├── DeviceGroupListDtoTest.java (344 lines)
│                   │       │   ├── ExportJobListenerTest.java (172 lines)
│                   │       │   ├── ExportJobPublisherTest.java (308 lines)
│                   │       │   ├── ExportJobRequestDtoTest.java (280 lines)
│                   │       │   ├── InventoryCSVExportJobTest.java (1990 lines)
│                   │       │   └── SwimDataExportServiceTest.java (316 lines)
│                   │       ├── dlm/
│                   │       │   ├── CredentialProfileOnboarderTest.java (180 lines)
│                   │       │   ├── InventoryAlarmClientTest.java (82 lines)
│                   │       │   ├── InvetoryAlarmClientTest.java (64 lines)
│                   │       │   └── XtractDlmNodeAndCredTest.java (400 lines)
│                   │       ├── geo/
│                   │       │   └── InventoryGeoHAHookTest.java (168 lines)
│                   │       ├── grouping/
│                   │       │   ├── GroupDeviceInventoryServiceTest.java (854 lines)
│                   │       │   └── GroupingClientHelperTest.java (216 lines)
│                   │       ├── listener/
│                   │       │   └── Lag8023admemberportsettingsListenerTest.java (144 lines)
│                   │       ├── logger/
│                   │       │   └── InventoryLoggerTest.java (256 lines)
│                   │       ├── maintenance/
│                   │       │   ├── InventoryMaintenanceModeTaskTest.java (53 lines)
│                   │       │   └── MaintenanceServiceTest.java (94 lines)
│                   │       ├── profile/
│                   │       │   ├── CWProfileConfigTest.java (23 lines)
│                   │       │   └── LocalProfileConfigTest.java (23 lines)
│                   │       ├── swagger/
│                   │       │   └── SwaggerConfigTest.java (27 lines)
│                   │       ├── util/
│                   │       │   ├── CSVWriterUtilTest.java (429 lines)
│                   │       │   ├── InventoryDecryptionUtilTest.java (99 lines)
│                   │       │   ├── InventoryRemoteFileUploaderTest.java (279 lines)
│                   │       │   ├── InventorySSHClientTest.java (233 lines)
│                   │       │   └── ZipCompressionUtilTest.java (229 lines)
│                   │       ├── xde/
│                   │       │   └── XdeInitInvTest.java (31 lines)
│                   │       ├── AppManagementHandlerImplTest.java (57 lines)
│                   │       ├── ApplicationShowTechHandlerTest.java (39 lines)
│                   │       ├── EPNMInventoryServiceTest.java (332 lines)
│                   │       ├── HealthUpdaterTest.java (118 lines)
│                   │       ├── InventoryBackupRestoreHookTest.java (25 lines)
│                   │       └── InventoryCrossworkPostInitTest.java (63 lines)
│                   ├── ifm/
│                   │   ├── inventory/
│                   │   │   └── rest/
│                   │   │       └── CwInventoryRestServiceTest.java (5708 lines)
│                   │   ├── inventoryrestservice/
│                   │   │   ├── DiagnosticsRestServiceTest.java (886 lines)
│                   │   │   ├── InventoryEMSRestServiceTest.java (1451 lines)
│                   │   │   ├── InventoryEMSRestUtilTest.java (130 lines)
│                   │   │   ├── InventoryJobRestServiceTest.java (2441 lines)
│                   │   │   ├── InventoryRestServiceTest.java (188 lines)
│                   │   │   └── SortCriteriaUtilTest.java (89 lines)
│                   │   ├── inventoryserviceplugin/
│                   │   │   └── LocationUpdateCallBackImplTest.java (234 lines)
│                   │   └── jobscheduler/
│                   │       ├── rest/
│                   │       │   ├── util/
│                   │       │   │   └── UtilsTest.java (190 lines)
│                   │       │   └── JobSchedulerRestServiceTest.java (4007 lines)
│                   │       └── service/
│                   │           └── JobSchedulerServiceImplTest.java (4516 lines)
│                   └── xmp/
│                       ├── ice/
│                       │   └── job/
│                       │       └── InventoryParameterCollectionJobTest.java (5411 lines)
│                       ├── jobmanager/
│                       │   └── postInit/
│                       │       └── JobManagerPostInitHookImplTest.java (751 lines)
│                       └── jobnotification/
│                           └── impl/
│                               └── JobNotificationManagerTest.java (132 lines)
├── .gitignore (6 lines)
├── CLAUDE.md (36 lines)
├── CODEOWNERS (1 lines)
├── Dockerfile (97 lines)
├── ExportDevice.csv (0 lines)
├── Jenkinsfile (386 lines)
├── PULL_REQUEST_TEMPLATE.md (36 lines)
├── README.md (2 lines)
├── TestFile.csv (0 lines)
├── automation_version_list.py (56 lines)
├── automation_version_list.txt (67 lines)
├── cs_script.sh (5 lines)
├── cw_inventory.iml (8 lines)
├── cw_inventory_liveness.sh (9 lines)
├── cw_inventory_start.sh (354 lines)
├── election.conf (19 lines)
├── exclude.txt (4 lines)
├── generate_heap_dump.sh (5 lines)
├── jacoco-exclusions.properties (2 lines)
├── liveness.sh (99 lines)
├── mvnw (233 lines)
├── mvnw.cmd (145 lines)
├── patch.txt (24 lines)
├── pom.xml (7449 lines)
├── pom.xml.bak (2339 lines)
├── readiness.sh (5 lines)
├── settings.xml (229 lines)
├── showtech.sh (12 lines)
├── sonar_scan.sh (60 lines)
└── start_exporter.sh (1 lines)
```
