# Agent 01 — EPNM `assembly` repo extraction

Source: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EPNM/tree-reports/assembly_tree_report.md`

Repo report header stats: 2,031 text-like files, 355 directories, 717,492 raw lines. Repo root observed in report: `/Users/cmoore/Documents/programming/EPNM/inventory/assembly`.

Note on naming: in the tree report path strings, filenames do not necessarily match the Confluence-cited path exactly. The Confluence extract referenced `assembly/blob/cepnm8.1PI_DPP3/ifm_platform_ui/src/main/webapp/applications/inventory/js/InventoryListView.js` — that exact file is present in this tree at `ifm_platform_ui/src/main/webapp/applications/inventory/js/InventoryListView.js` (8020 lines). Confirmed anchor.

## 1. Repo shape at a glance

The `assembly` repo is a multi-module Maven aggregate with roughly 12 top-level directories. The ones with substantive content are: `epnm_tp/` (contains the large `ifm_platform_ui/` submodule — the main Dojo-based Inventory and Fault UI webapp, plus `assembly/` XMLs), `ifm_rpm/` (RPM packaging — CLI template XML library, MIB files, schema SQL, shell scripts, system preferences — does not contain JS/UI code), `lumos_app_rpm/` (web-application RPM packaging with `war_overlay/` containing overlay JS for NetworkServices/TrustSec, XMPTopology, CUES widget library, XCT, XWT TreeGrid, and Dojo build tooling under `src/main/tools/dojo/`), `srtg_rpm/`, `xmp_assembly_installer/` (seven POM-only subprojects: base_services, datacenter, decap, helpers, inventory, model, platform), `xmp_assembly_static_files/` (Spring XML wiring for inventory-discovery-process), `xmp_assembly_third_party/`, `xmp_parent_pom/`, `xmp_parent_pom_epnm/`, `xmp_rpm/` (POM cleanup tooling, XMPIngeration), and `repackage_xwt_services_jar/`. Top-level files include `Jenkinsfile`, `settings-rel.xml`, `precheckforrpm.py`, and several `*_assembly.txt` manifest files. The UI source of truth for POC work is effectively confined to `epnm_tp/ifm_platform_ui/` plus overlay JS under `lumos_app_rpm/files/war_overlay/`.

## 2. Inventory UI file locations

Primary directory: `epnm_tp/ifm_platform_ui/src/main/webapp/applications/inventory/`

Subdirectories: `css/`, `data/`, `html/`, `i18n/nls/`, `js/` (with `details/`, `qv/`, `templates/`), `json/`.

Key files under `applications/inventory/js/`:
- `InventoryListView.js` (8020 lines) — the Confluence-cited anchor; likely the Network Devices list view.
- `DeviceDetailTabViewController.js` (420 lines)
- `DeviceDetailsObjectSelector.js` (91 lines)
- `DeviceDetailsPage.js` (650 lines) — likely the Device Details page controller.
- `DeviceSummaryTabView.js` (97 lines)
- `DeviceNotSupportedSummaryTabView.js` (41 lines)
- `SPTDeviceSummaryTabView.js` (97 lines)
- `DeviceTemplatesView.js` (12 lines)
- `AddEditDeviceWidget.js` (6849 lines) and `AddEditDeviceWidget_old_PI.js` (6263 lines)
- `AddDeviceToGroupWidget.js` (47 lines), `AddDeviceToSiteWidget.js` (404 lines)
- `BulkImportWidget.js` (295 lines), `bulkImportNetworkDevices.js` (63 lines)
- `CredentialProfileManager.js` (546 lines), `AddEditCredentialProfileWidget.js` (1181 lines)
- `EPNMFileMetadata.js` (752 lines), `FileMetadata.js` (704 lines), `MetadataMgr.js` (227 lines)
- `InventoryMultiQuickView.js` (131 lines)
- `VdcDetails.js` (862 lines) — chassis/VDC details (see §4).
- `QueryString.js`, `Utils.js`, `Utils_old_PI.js`, `deviceInventoryViewCommonJs.js` (518 lines), `commonInterfaces.js`, `app.profile.js`, `package.json`.

Quick-view JS under `applications/inventory/js/qv/`:
- `DeviceQuickView.js` (218 lines)
- `StatusQuickView.js` (310 lines)
- `ReachabilityQuickView.js` (127 lines)
- `CDAQuickView.js` (96 lines)

Details pane under `applications/inventory/js/details/`:
- `DeviceSummaryPane.js` (46 lines)

Metadata/data JSON under `applications/inventory/data/`:
- `InventoryListMetadata.json` (219 lines) plus family-specific metadata variants: `InventoryListMetadataForAutonomousAp.json`, `InventoryListMetadataForEdision.json`, `InventoryListMetadataForMerakiAccessPoint.json`, `InventoryListMetadataForMerakiDashboard.json`, `InventoryListMetadataForSwitches_and_Hubs.json`, `InventoryListMetadataForThirdpartyAp.json`, `InventoryListMetadataForThirdpartyWirelessController.json`, `InventoryListMetadataForUnifiedAp.json` (625 lines), `InventoryListMetadataForUnmanagedAp.json`, `InventoryListMetadataForWirelessController.json` (395 lines).
- `DeviceDetailTabViewMetadata.json` (487 lines)
- `DeviceTypes.json`, `ColumnMetaData.json`, `QuickViewMetadata.json`, `QuickView_DetailsMetadata.json`, `QuickView_StatusMetadata.json`.
- `vdc.json` (363 lines) — VDC/chassis data fixture.
- `InitDesignViewLHS.js` (3373 lines) — mis-placed as JS inside `data/`; likely the left-hand-side tree for the Design/Inventory view.

HTML templates under `applications/inventory/html/`:
- `InventoryList.html` (24 lines)
- `deviceInventoryDetails.html` (138 lines) — likely the Device Details page template.
- `cdpNeighborList.html` (183 lines)
- `DeviceVDCDetails.html` (18 lines)
- `esAllInterfaceDetails.html`, `esChassisDetail.html` (228 lines), `esEtherChannelDetail.html`, `esEthernetInterfacesDetail.html`, `esIpInterfaceDetails.html`, `esModuleDetail.html`, `esPhysicalPort.html`, `esUdfDetail.html`, `vssRedundantData.html`.
- `AssetList.html`, `smart.html`, `blankDesign.html`.
- JSP scheduler / job-result shells: `ApDeleteJobResults.jsp`, `BulkDeviceEditJobResults.jsp`, `CopyReplaceJobResults.jsp`, `EwlcDeployTaskServiceJobResults.jsp`, `ImportJobResults.jsp` (285 lines), `InventoryDeviceMaintenanceJobScheduler.html`, `InventoryDeviceManagedJobScheduler.html`, `ScheduledDeviceMaintenanceOrManagedJobResults.jsp`, `WLCConfigAction.jsp`, `WirelessConfigGroupTask.jsp`.

CSS under `applications/inventory/css/`: `inventory.css`, `networkDevices.css`, `vdcDetails.css` (plus `app.profile.js` and `package.json`).

i18n under `applications/inventory/i18n/nls/`: `InventoryProperties.js` in en (1814 lines), en-us (3 lines), ja (1814 lines), ko (1777 lines), plus root `InventoryProperties.js` (1835 lines).

Device-360 related files sit in a separate subtree under the Dojo lib, not under `applications/inventory/`:
- `epnm_tp/ifm_platform_ui/src/main/webapp/lib/ifm/_360/modules/cards/tables/IFM360VDCForm.js` (321 lines)
- `epnm_tp/ifm_platform_ui/src/main/webapp/lib/ifm/_360/modules/cards/tables/IFM360VDCTable.js` (222 lines)
- NLS bundle `epnm_tp/ifm_platform_ui/src/main/webapp/lib/ifm/nls/360Properties.js` (422 lines, plus en/ja/ko variants 415–422 lines).
- Dojo build layer `lumos_app_rpm/src/main/tools/dojo/layers/ifm_360.js` (48 lines) — suggests `ifm_360` is a separately built Dojo layer.

InterfaceLicense (adjacent to Inventory) under `applications/InterfaceLicense/`:
- `js/InventoryListViewInterfaceLicense.js` (756 lines), `js/FileMetadata.js`, `js/MetadataMgr.js`, `js/PropertySheetWidget.js`, `js/Utils.js`, `js/_QuickViewBasePane.js`.
- `html/InterfaceInventoryList.html`, `html/InterfaceUnLicensedList.html` (414 lines).
- `data/InterfaceLicenseListMetadata.json`, `data/InterfaceListForUnlicensedDiscoveredMetadata.json`.

Interface-360: no file explicitly named "Interface360" was found in the tree. The closest matches are: the Interface detail HTML templates above (`esAllInterfaceDetails.html`, `esEthernetInterfacesDetail.html`, `esIpInterfaceDetails.html`, `esPhysicalPort.html`), `IntfAvailability.jsp` / `IntfStatusSummary.jsp` / `IntfTxRxUtilization.jsp` / `IntfUtilSummary.jsp` / `InterfaceDetailsDashlet.jsp` (all under `applications/AlarmManagement/jsp/` — see §7), and `applications/common/js/ifm/widgets/IfmPortTreeTable.js` (188 lines). The named `_360` subtree only surfaces VDC. Interface 360 per se is likely rendered by the generic PropertySheet/_360 framework parameterized by context; this is an implication, not certain.

## 3. Fault Management UI file locations

Primary directory: `epnm_tp/ifm_platform_ui/src/main/webapp/applications/AlarmManagement/` (confirms Akhil's "assembly is on the UI side" for fault UI).

Subdirectories: `css/`, `data/`, `html/`, `i18n/nls/`, `js/` (with `components/`, `toolbar/`, `templates/`), `jsp/`, `nls/`.

Top-level JS under `applications/AlarmManagement/js/` (alarms table, events, syslogs, correlated alarms, and related):
- `AlarmListView.js` (536 lines) — the main alarms-table view.
- `AlarmEventListView.js` (655 lines), `AlarmLogView.js` (1232 lines)
- `EnhancedAlarmList.js` (607 lines)
- `AlarmCorrelatedView.js` (1269 lines) and `CorrelatedAlarms.js` (1086 lines) — correlated-alarms screens.
- `EventListView.js` (203 lines), `EventHistoryListView.js` (110 lines), `DerivedEventListView.js` (27 lines), `SystemEventsView.js` (341 lines).
- `SyslogListView.js` (469 lines), `SyslogListViewWebSocket.js` (647 lines) — syslogs.
- `AlarmActionHandler.js` (756 lines), `ActionHandlerOverride.js` (1279 lines), `AssuranceOverrides.js` (1201 lines).
- `AlarmDialogContent.js`, `AlarmEventBrowser.js` (512 lines), `EPNMAlarmEventBrowser.js` (202 lines), `AlarmEventObjSelFunctions.js` (827 lines).
- `AlarmQuickView.js` (227 lines), `DBHealthQuickView.js`, `ServiceAffectingAlarmView.js`, `SampleTroubleshootView.js`.
- `AlarmOAMHandler.js` (911 lines), `DeviceOAMHandler.js` (897 lines), `MplsLspOAMHandler.js` (868 lines), `MplsLspCircuitOAMHandler.js` (1453 lines), `PwOAMHandler.js` (1019 lines), `SRTEOAMHandler.js` (889 lines), `UniDirectionalOAMHandler.js` (924 lines), `VRFOAMHandler.js` (1132 lines), `L2vpnCfmOamHandler.js` (1240 lines), `OAMUtil.js`.
- `FaultExportDialog.js` (334 lines), `FileMetadataAlarms.js` (725 lines), `faultUtils.js` (359 lines), `conAlarm.js` (1210 lines).
- `DerivedAlarmListView.js`, `DeviceUnavailabilityListView.js` (218 lines), `SystemDBHealthTable.js`, `EventMetadataMgr.js` (531 lines), `UserDefinedEventMappingForm.js`, `SelectOwnerDialogForm.js`, `AddAnnotationForm.js`, `AlarmSummaryMetricView.js`, `MetricNavigator.js`, `MetricView.js`, `GenericAssuranceMetricView.js`.
- Store/infrastructure: `IfmJsonRestStore.js`, `l3vpnTableStore.js`, `lspOamTableStore.js`, `AlarmManagerEnablementTable.js` (268 lines).
- Misc: `customMsgPanel.js`, `RecommendedAction.js`, `ChartUtils.js`, `LineSpark.js`, `Panel.js`, `ProgressBar.js`, `SparkLineColumns.js`, `Tooltipoverride.js`, `_ItemWidget.js`, `_ExtendedAdvancedFilterPanel.js`, `_ExtendedContextualToolbar.js`, `_ExtendedFilterPopover.js`, `_ExtendedFilterWidget.js`, `TableLayoutUpdaterMixin.js`, `AlarmTableRefreshMixin.js`, `ABSAlarmListView.js`.
- Anomalies: `rashmi.js` (1 line) — stray dev file.

Table internals under `applications/AlarmManagement/js/components/table/`:
- `AlarmTable.js` (524 lines), `EventTable.js` (126 lines), `EventPageTable.js`, `SysLogTable.js` (91 lines), `_AlarmEventTable.js` (421 lines), `_GenericPageTable.js` (389 lines).
- Detail subtree (`components/table/detail/`) contains `AlarmDetailGrid.js`, `AlarmEventDetailGrid.js` (179 lines), `DetailUtil.js` (266 lines), `EventDetailGrid.js`, `op-center.js`, plus rich `cell/`, `titlePane/`, and `data/` trees with per-alarm-type metadata JSON (`Alarm_*.json`, `Event_*.json` — dozens of files covering BGP, ISIS, MPLS, MPLS-L3VPN, OSPF, OpticalNetworking, OpticalTransport, SONET, SwitchesandRouters, NexusVPCSwitch, plus rogue/wireless variants).

Toolbar actions under `applications/AlarmManagement/js/components/toolbar/button/`: `acknowledge`, `assign`, `annotation`, `changeStatus`, `customEvents/syslog`, `customEvents/trap` (with `UploadMibForm.js` 191 lines, `AddTrapEventMappingForm.js`, `MibFilteringSelect.js`), `policy`, `rogue`, `troubleshoot`, plus top-level `DeleteButton.js`, `EditButton.js` (350 lines), `EmailConfigurationButton.js`, `PauseAutoRefreshButton.js`, and mixins `_AsyncOperationMixin.js`, `_ConfirmAlarmActionMixin.js`, `_SelectionAwareMixin.js`. Aggregated toolbar files: `AlarmContextualToolbar.js` (286 lines), `AlarmEventGlobalToolbar.js` (159 lines), `EventContextualToolbar.js`, `_AlarmEventContextualToolbar.js` (248 lines).

EPNM-specific variants under `applications/AlarmManagement/js/components/EPNM/`: `EPNMAlarmEventGlobalToolbar.js`, `EPNMAlarmListView.js`, `EPNMAlarmTable.js`, `EPNMEnhancedAlarmListView.js`, `EPNMRealtimeAlarmTable.js`, `EPNMRefreshIntervalWidget.js` (236 lines).

Supporting components: `deviceGroupTree/` (selectors), `quickView/` (`AlarmQuickView.js`, `DeviceGroupAlarmSummary.js`), `tab/` (`AlarmTabButton.js`, `AlarmTabController.js`).

Data fixtures under `applications/AlarmManagement/data/`: `AlarmList.json` (269), `AlarmListMetadata.json` (167), `EventList.json`, `EventListMetadata.json` (141), `SyslogListMetadata.json` (111), `SystemEventsMetadata.json`, `SyslogSummaryTemplates.xml`, `SyslogWatchTemplates.xml`, family-specific metadata (`Alarm_BGP.json`, `Alarm_ISIS.json`, `Alarm_MPLS-L3VPN.json`, `Alarm_MPLS.json`, `Alarm_NexusVPCSwitch.json`, `Alarm_OSPF.json`, `Alarm_OpticalNetworking.json`, `Alarm_OpticalTransport.json` 1116 lines, `Alarm_SONET.json`, `Alarm_SwitchesandRouters.json`), plus wireless/derived variants and `DerivedEventListMetadata.*.json`, `EventListMetadata.*.json`, `alarmTabs.json`, `clusterAlarmTabs.json`, `epnmAlarmTabs.json`, `ifmAlarmMetadata.json`, `ifmalarms.json`, `FormatterData.json`, `devices.json` (1612 lines), `showCommands.json`, `FailureSourceDialogContent.json`.

HTML templates under `applications/AlarmManagement/html/`: `AlarmList.html` (48), `alarmEventList.html`, `alarmEventObjSel.html`, `SystemAlarm.html`, `Location_impactedAlarmsDetails.html`, `Location_impactedAlarmsTree.html`, `sliderAlarmStatGT.html` (117), `MetricView.html` (317), `MetricNavigator.html`, `Chart.html`, `SelectOwnerDialogForm.html`.

JSP shells under `applications/AlarmManagement/jsp/`: `AlarmSummaryDashlet.jsp`, `SystemAlarmsPortlet.jsp`, `SystemEventsPortlet.jsp`, `SyslogSummaryDashlet.jsp`, `SyslogWatchDashlet.jsp`, `TopNEvents.jsp`, `TopNSyslogSender.jsp`, plus Device/Interface/Sys summary dashlet JSPs (see §7).

Other fault-adjacent paths:
- `epnm_tp/ifm_platform_ui/src/main/webapp/applications/faultPolicy/util/event-types.js` (186 lines).
- `epnm_tp/ifm_platform_ui/src/main/webapp/applications/AlarmManagement/patches/FileMetadataAlarms.js` (729 lines).
- `epnm_tp/ifm_platform_ui/src/main/webapp/lib/ifm/Actions/Monitoring/PropertySheet/AlarmAndEventBrowserActionHandlers.js` (71 lines).
- `epnm_tp/ifm_platform_ui/src/main/webapp/ifmoverlay/ifm/widget/templates/AlarmEditWidget.html`, `.../EventEditWidget.html`, and JS `EventEditWidget.js` (143 lines) in the same `ifmoverlay/ifm/widget/` tree.
- `epnm_tp/ifm_platform_ui/src/main/webapp/lib/ifm/widget/AlarmEditWidget.js` (42 lines), `EventEditWidget.js` (121 lines), `RogueActionHandlers.js`.

## 4. Chassis View integration points inside assembly

No directory named `chassis/` exists, but chassis rendering appears embedded in the Inventory Device Details flow and VDC subtree:

- `applications/inventory/html/esChassisDetail.html` (228 lines) — likely the chassis detail HTML fragment used on Device Details.
- `applications/inventory/html/DeviceVDCDetails.html` (18 lines) and `applications/inventory/css/vdcDetails.css` (81 lines).
- `applications/inventory/js/VdcDetails.js` (862 lines) — VDC/chassis logic.
- `applications/inventory/data/vdc.json` (363 lines) — fixture.
- Device-360 VDC cards in `lib/ifm/_360/modules/cards/tables/IFM360VDCForm.js` and `IFM360VDCTable.js`.
- Accompanying module/port/interface detail HTML that sits alongside chassis: `esModuleDetail.html` (230), `esPhysicalPort.html` (170), `esEthernetInterfacesDetail.html` (227), `esAllInterfaceDetails.html` (318), `esEtherChannelDetail.html` (243), `esIpInterfaceDetails.html` (161), `esUdfDetail.html` (384).
- Likely data source for the chassis visual: `lib/cuecharts/cue_charts.js` (36 lines) and `applications/visualize/js/d3.js` (8811 lines) plus `Tree.js` (1454 lines) and `_D3Base.js` (647 lines). These are generic viz libs and the chassis could use them, though nothing in the filenames confirms chassis-specific rendering lives here. Implication only.

Note: the `assembly` tree does not contain any file with "Chassis" in the JS filename. The chassis experience is likely rendered via `esChassisDetail.html` populated by `DeviceDetailsPage.js` / `DeviceDetailTabViewController.js` against metadata keyed in `DeviceDetailTabViewMetadata.json`. Not proven by tree alone.

## 5. Dojo framework surface

The UI is Dojo 1.x, organized by Dojo package convention (`app.profile.js` + `package.json` pairs scattered through most UI directories). Build-time layer files consolidate packages.

Dojo build layers (`lumos_app_rpm/src/main/tools/dojo/layers/`): `app.js`, `app_wcs.js`, `assuranceDashboard.js`, `cues.js`, `dashboard.js`, `ifm.js` (72 lines), `ifm_360.js` (48 lines), `login.js`, `sam.js`, `smartLicenseDashboard.js`, `wapdashboard.js`, `wapfr.js` (90 lines), `wapfr_abs.js`. Dojo build profile: `lumos_app_rpm/src/main/tools/dojo/wcs.profile.js` (195 lines) and `epnm_wcs.profile.js` (160 lines). Build orchestration: `constructTree.xml` (349 lines), `preBuildConstructTree.xml`, `postBuildConstructTree.xml`, `wcs-build.xml`.

Dojo core/extension shipped in `epnm_tp/ifm_platform_ui/src/main/webapp/lib/`:
- `lib/dojo/io/iframe.js` (414), `lib/dojo/request/util.js` + `util.js.uncompressed.js`.
- `lib/dojox/form/FileUploader.js` (1437), `lib/dojox/grid/cells/_base.js` (plus `.uncompressed.js`), `lib/dojox/grid/_Builder.js` (plus `.uncompressed.js`), `lib/dojox/jq.js` (1289).
- `lib/cuecharts/cue_charts.js` + `swfobject.js` (Cisco CUE charting).

Widget / template conventions (Dojo `_TemplatedMixin` pattern — .js widget colocated with .html template):
- `applications/AlarmManagement/js/components/table/detail/cell/labelValue/field/` (Field.js, LinkField.js, AuditLinkField.js, …).
- `applications/AlarmManagement/js/components/toolbar/button/annotation/templates/AddAnnotationForm.html` paired with `AddAnnotationForm.js`.
- `applications/AlarmManagement/js/components/toolbar/button/customEvents/trap/templates/AddTrapEventMappingForm.html`, `UploadMibForm.html`, paired with JS siblings.
- `applications/AlarmManagement/js/components/quickView/templates/DeviceGroupAlarmSummary.html`.
- `applications/inventory/js/templates/AddDevice.html` (968), `AddCredentialProfile.html` (585), `bulkImportTemplate.html`, `credentialProfileManager.html`, `PropertySheetWidget.html`.
- `applications/common/js/ifm/widgets/templates/` with `IfmDeviceGridTemplate.html`, `IfmDeviceTreeTableLazyLoadedV2.html`, `_TagAssociationContent.html`, paired with `IfmDeviceTreeGridTable.js` (588), `IfmDeviceTreeTableLazyLoadedV2.js` (839), `DeviceSelectionWidget.js` (1534), `IfmPortTreeTable.js` (188).
- `ifmoverlay/ifm/widget/templates/` (AlarmEditWidget.html, EventEditWidget.html, IfmPaginationToolbar.html, PropertySheet.html, PropertySheetEditWidget.html, SliderPanelGT.html, SwitchPortTrace.html) — paired JS in same tree (`ActionHandlers.js` 1842, `DataGridHandlers.js`, `DataPropertySheet.js`, `PropertySheetColumn.js` 606, `TableHandlers.js`, `imageLoader.js`).
- `lib/ifm/widget/` — parallel widget library: templates directory + `ActionHandlers.js` (1876), `IFMTitlePane.js` (439), `IFMTitlePaneAlarmToplology.js` (411), `IfmPaginationToolbar.js` (369), `PropertySheet.js`, `PropertySheetColumn.js` (560), `PropertySheetEditWidget.js`, `PropertySheetItem.js`, `PIEChart.js`, `TableContainer.js`, `paginatedToolBar.js`, `sptDialog.js` (990).
- Dashboard filter widgets: `lib/ifm/dashboard/filter/templates/` (Advanced*Filter*.html, TimeFrame*, ApplicationSelector*, ClientFrame*, ObjectSelectorFilter, SiteLabel) paired with same-named JS.

i18n conventions: every UI module has `i18n/nls/en/`, `ja/`, `ko/` subdirectories with `*.js` resource bundles (Dojo standard layout). Notable bundles: `InventoryProperties.js` (1835 lines root, 1814 en/ja, 1777 ko), `AlarmEventProperties.js` (378 root, 374 en), `360Properties.js` (422 root, 415 en), `SmartLicenseProperties.js`, `AlarmPolicesProperties.js`, `NotificationPolicesProperties.js`, `Day1Properties.js` (628 en-us/root), `ApplicationProperties.js`.

Stores likely to be re-implemented as REST adapters in Angular:
- `applications/AlarmManagement/js/IfmJsonRestStore.js` (117)
- `applications/AlarmManagement/js/components/toolbar/button/customEvents/NbiJsonRestStore.js`
- `applications/common/js/JsonRestStore.js`, `applications/common/js/OrderSupportItemFileWriteStore.js`
- `applications/search/JsonRestStoreServiceProvider.js` (193)
- `applications/AlarmManagement/js/l3vpnTableStore.js`, `lspOamTableStore.js`
- `applications/inventory/js/EPNMFileMetadata.js`, `FileMetadata.js`
- `applications/InterfaceLicense/js/FileMetadata.js`
- `applications/UDF/js/UDFRestStore.js`

JSP views that render page shells or wrap Dojo content:
- `epnm_tp/ifm_platform_ui/src/main/webapp/index.html` (448)
- `login.jsp` (74), `logout.jsp` (16)
- Under `applications/AlarmManagement/jsp/` — dashlet JSPs listed in §3/§7.
- Under `applications/common/jsp/` — many `SystemPreferences_*`, `c_*`, and `sam*` JSPs used by dashboard editors.
- `applications/discovery/jsp/discoveryJobResults.jsp` (413).
- `applications/nbi/jsp/` — `CliTemplateDeployIOSDevicesJobResult.jsp` (320), `DeleteDevicesJobResult.jsp`, `DeployMacFilterJobResult.jsp`, `ModifyUnifiedApJobResult.jsp`, `WlanProvisioningJobResult.jsp`.
- `applications/inventory/html/*.jsp` — several job-result JSPs (ApDeleteJobResults, BulkDeviceEditJobResults, CopyReplaceJobResults, EwlcDeployTaskServiceJobResults, ImportJobResults, ScheduledDeviceMaintenanceOrManagedJobResults, WLCConfigAction, WirelessConfigGroupTask).
- `applications/search/jsp/` — advancedSearch.jsp, search.jsp, admin.jsp, include.jsp, updateConfigForm.jsp.
- `applications/softwareupdate/html/` — envelope.jsp (190), softwareUpdate.jsp (455), softwareUpdateContent.jsp, softwareUpdateStatuses.jsp, haCounterpartUpdates.jsp, haMinDowntimeMessage.jsp, getCsrfToken.jsp.

## 6. Build and packaging indicators

- Maven aggregate. POMs at: `epnm_tp/pom.xml` (1079), `epnm_tp/epnm_pom.xml` (806), `epnm_tp/ifm_platform_ui/` (no standalone pom in tree, but `docs/pom.xml` 57 lines), `epnm_tp/assembly/pom.xml` (171) with `assembly.xml` (1460) and `root_priv_assembly.xml` (63), `epnm_tp/release-pom.xml.save` (2201).
- `ifm_rpm/pom.xml` (3998), `ifm_rpm/epnm_pom.xml` (3424), `ifm_rpm/assembly-dependencies.xml`, `ifm_rpm/ifm_install_metadata.xml` (1011).
- `lumos_app_rpm/pom.xml` (1018), `lumos_app_rpm/pom_nogen.xml` (935), `lumos_app_rpm/epnm_pom.xml` (963), `lumos_app_rpm/lumosapp_install_metadata.xml`.
- `lumos_app_rpm/src/main/assembly/*.xml` — `assembly.xml`, `jsp_precompile-webapp.xml`, `unoptimized-webapp.xml`, `webacs-webapp.xml` (WAR-style overlay).
- `srtg_rpm/pom.xml` (616).
- `xmp_assembly_installer/pom.xml` (514) with 7 child modules each having their own pom.
- `xmp_assembly_static_files/pom.xml` (63), `xmp_assembly_third_party/pom.xml` (1184), `xmp_parent_pom/pom.xml` (3815), `xmp_parent_pom_epnm/pom.xml` (91), `xmp_rpm/pom.xml` (234), `repackage_xwt_services_jar/pom.xml` (175).
- CI: top-level `Jenkinsfile` (98 lines).
- Settings: `settings-rel.xml` (160), `lumos_app_rpm/settings.xml` (52).
- Assembly manifests at root: `ifm_assembly.txt`, `lumosapp_assembly.txt`, `srtg_assembly.txt`, `CONFLICT_FILES.txt`.
- Dojo build (not a gulp/webpack build): `lumos_app_rpm/src/main/tools/dojo/wcs-build.xml` (90), `constructTree.xml`, `preBuildConstructTree.xml`, `postBuildConstructTree.xml`, `wcs.profile.js`, `epnm_wcs.profile.js`.
- Deployment scripts: `lumos_app_rpm/mergewar_fromrpm.sh` (211), `buildanddeploymergewar.sh`, `installlumosapp.sh` (349), `deploy.sh`, `cpwar_tostaging.sh`, `updateapptopf.py` (132).
- WEB-INF: `epnm_tp/ifm_platform_ui/src/main/webapp/WEB-INF/web.xml` (69). META-INF Spring contexts at `epnm_tp/ifm_platform_ui/src/main/webapp/META-INF/spring/ifm_platform_ui_context.xml` (291), `admin-cxf-context.xml`, `osgi-context.xml`, plus `MANIFEST.MF` (3 lines — suggests OSGi bundle packaging).
- Registry / navigation XML: `epnm_tp/ifm_platform_ui/src/main/resources/wap/registry/xml/` — `actions.xml`, `application.xml`, `handlers.xml`, `navigation.xml` (456), `pageViews.xml` (392), `pages.xml` (317), `views.xml` (458). These drive the page/menu/view registration for the WAP (Web Application Platform) framework.
- Java backend slice in `ifm_platform_ui`: limited to search REST (`AdminRestService.java`, `QueryRestService.java` 261 lines, `TermsRestService.java`), security filters (`BufferOverflowFilter.java`, `IfmLogoutFilter.java`, `IfmXssFilter.java`, `IfmXssRequestWrapper.java` 349, `SQLInjectionFilter.java`), and `IfmXMLRegistryProvider.java` (207). Plus configuration XML under `src/main/resources/com/cisco/ifm/discovery/castor/` (`castor-mapping.xml`, `discovery-conf-mapping.xml` 756, `ifmDiscoverySchema.xsd` 474). The real device/alarm REST services are not in this webapp — they live in sibling XMP / inventory-discovery-process services configured via Spring XML (e.g., `xmp_assembly_static_files/src/main/resources/XMPInstaller/conf/inventory_discovery_process/inventory-discovery-process-ifm-inventory-service-context.xml` 200).

## 7. Other Inventory- or Fault-relevant files by name

Device-related (outside `applications/inventory/`):
- `applications/AlarmManagement/data/devices.json` (1612) — device fixture.
- `applications/AlarmManagement/js/DeviceOAMHandler.js` (897), `DeviceGroupTreeContainer.js` (181), `DeviceUnavailabilityListView.js` (218).
- `applications/AlarmManagement/js/components/table/detail/cell/DeviceEventsTableCell.js`, `titlePane/templates/DeviceEventsDropDown.html`, `titlePane/DeviceEventsDropDown.js`, `titlePane/RelatedHistoryDevicePicker.js`.
- `applications/AlarmManagement/js/components/deviceGroupTree/autoRefresh/_AutoRefreshControllerMixin.js`, `objectSelector/AlarmEventDeviceGroupSelector.js` (209), `ClusterAlarmEventDeviceGroupSelector.js`, `_AlarmEventDeviceGroupSelectorMixin.js` (228).
- `applications/AlarmManagement/jsp/DeviceAvailabilitySummary.jsp` (155), `DeviceHealthInfoDashlet.jsp`, `DeviceHealthSummary.jsp` (139), `DevicePortSummary.jsp` (165), `DeviceReachabilityStatus.jsp` (157), `DeviceUnavailabilitySummary.jsp`, `deviceAvailabilityTrend.jsp`, `deviceCPUUtilization.jsp`, `deviceCacheEntry.jsp`, `deviceMemoryUtilization.jsp`.
- `applications/common/js/ifm/widgets/DeviceSelectionWidget.js` (1534), `DeviceTreeTable.js`, `IfmDeviceSelector.js` (104), `IfmDeviceTreeGridTable.js` (588), `IfmDeviceTreeTable.js` (254), `IfmDeviceTreeTableLazyLoadedV2.js` (839), `IfmLazyLoadedDeviceTreeTable.js` (253).
- `applications/common/jsp/DeviceCredentialsSummary.jsp`, `DeviceSelector.jsp` (119), and many `c_device*Filter*.jsp` / `c_*Selection.jsp` helpers.
- `applications/common/js/ifm/widgets/TagAssociationPopOver.js` (281) and template — likely used by Device Details for tagging.
- `applications/common/js/ifm/widgets/IfmPortTreeTable.js` (188), `TableQuickView.js`, `IfmCustomTitlePane.js`.
- `applications/credentialProfile/js/AddEditCredentialProfileWidget.js` (2236 — larger copy than the one in inventory), `CredentialProfileManager.js` (1200), `deviceListTable.js` (204), plus its `html/`, `css/`, `data/bulk-import-profile-template.csv`.
- `applications/assurance/StormPropertySheetColumn.js` (1250 lines) — a large property-sheet column implementation.

Interface-related:
- `applications/AlarmManagement/data/Interfacedata.json`, `InterfaceChartdata.json`, `InterfaceReceivedata.json`, `InterfaceSummarydata.json`.
- `applications/AlarmManagement/jsp/InterfaceDetailsDashlet.jsp` (132), `IntfAvailability.jsp` (156), `IntfAvailibilitySummary.jsp` (152), `IntfInOutDiscards.jsp`, `IntfInOutErrors.jsp`, `IntfStatusSummary.jsp` (125), `IntfTxRxUtilization.jsp` (184), `IntfUtilSummary.jsp` (189), `topNIntfErrorsDiscards.jsp` (478), `topNIntfUtilization.jsp` (707), `topNWanIntfIssues.jsp`.
- `applications/InterfaceLicense/html/InterfaceInventoryList.html`, `InterfaceUnLicensedList.html` (414), `InventoryListViewInterfaceLicense.js` (756).

Alarm-related (supplementary):
- `applications/AlarmManagement/data/ifmalarms.json` (114), `ifmAlarmMetadata.json` (117), `alarmTabs.json`, `clusterAlarmTabs.json`, `epnmAlarmTabs.json`, `allMetrics.json`, `delimiter.json`, `AlarmNotes.json`.
- `applications/AlarmManagement/nls/AlarmEventProperties.js` (378; en 374, ja 390, ko 369).
- `applications/AlarmManagement/i18n/nls/` — `epnmAlarmManagementProperties.js` (215 root; 216 en; 212 en-us; 223 ja; 220 ko) and `epnmInventoryProperties.js` (40 root/en/en-us; 41 ja; 44 ko).
- `lib/ifm/tests/alarmStatGT/testAlarmStatGT.html` (92) and `alarmStatGT.json`.
- `lib/ifm/util/SliderAlarmMetadata.json`, `sliderAlarmStatUtilsView.js` (1169), `sliderAlarmStatusWrapper.js`, `SliderStats.js` (333).

Chassis / VDC:
- All covered in §4; also `applications/inventory/html/esChassisDetail.html` (228) is the only filename containing "Chassis" in the tree.

## 8. Out-of-scope observations

Clearly not POC-relevant (Inventory/Fault-only POC):

- `ifm_rpm/files/ootb/` — hundreds of CLI template XML files (Configure Interface, CoreLayer-IOS, CVD-DMVPN-*, Day-0/Day-1 variants, Guided_Workflow_WLAN, IOS_XE_Centralized_Wireless_Network.xml 2621, etc.), Composite Templates, Feature Templates/IWAN, NFV, Router Security (CWS, OpenDNS, Snort IPS, ZBFW). Configuration-deploy domain, not inventory/fault UI.
- `ifm_rpm/files/compliance/` — compliance policy engine (ComplianceMgr.xml 815, ComplianceMgrShowCommand.xml 1455, policy XML examples, XSLTs, SQL schema 7736 lines).
- `ifm_rpm/files/*.my` — dozens of MIB files (CISCO-ENTITY-VENDORTYPE-OID-MIB.my 11959, AIRESPACE-WIRELESS-MIB.my 17105, CISCO-RTTMON-MIB.my 10604, CISCO-STACK-MIB.my 13255, CISCO-UNIFIED-COMPUTING-TC-MIB.my 27419, etc.). MIB assets for SNMP polling — backend concern.
- `ifm_rpm/files/*.sql` — large SQL DDL/DML (ncs_oracle.sql 2797, compliance_engine_schema.sql 7736, licenseTokenInfo.sql 1863).
- `ifm_rpm/files/swim/` — software image management.
- `ifm_rpm/files/preferences/user/WCSUserPreference.xml` (3369) — legacy WCS user preferences.
- `ifm_rpm/files/grouping_MDFData.xml` (4007), `mdfdata.xml` (8492) — device type/family metadata definition (may be indirectly relevant for device-type rendering but not POC scope).
- `applications/softwareupdate/` — software update UI (3343-line `softwareUpdate.js`, dedicated templates). Not POC.
- `applications/discovery/` — device discovery wizard (`DiscoverySettings.js` 1565, `InitDiscoverySettingsView.js` 1406, `discoveryUtilVs.js` 1681, many `discovery*.html` pages including `discoveryMenuOnInventory.html` 2918). Discovery is adjacent but not in POC scope.
- `applications/Startup/` — startup wizard (`StartupWizard.js` 334).
- `applications/credentialProfile/` — credential profile management (large but standalone from the two POC screens, except where referenced from inventory add/edit).
- `applications/TacService/`, `applications/UDF/`, `applications/workflow/`, `applications/usermgmt/` (empty), `applications/visualize/` (d3/tree libs — potentially reused but generic).
- `applications/nbi/jsp/*` — NBI job-result shells (deploy CLI, delete devices, WLAN provisioning, mac filter, modify unified AP).
- `applications/search/` — full-text/Solr search admin and advanced search (`advancedSearch.js` 1463, `search.js` 971, Solr doc templates). Not POC.
- `applications/configure/jsp/rawconfig.jsp` — raw config view.
- `lumos_app_rpm/files/war_overlay/webapps/applications/NetworkServices/TrustSec/js/Readiness.js` (2094), `XMPTopology/css/XMPTopologyModule.css` (1174) — TrustSec and topology overlays.
- `lumos_app_rpm/files/war_overlay/webapps/lib/xct/`, `lib/xct_uncompressed/`, `lib/xwt/`, `lib/xwt_uncompressed/` — generic third-party widget libraries (XCT smart services including TAC contact, DeviceContractInformation, SupportSettings; XWT GlobalToolbar, QuickViewIntegration, TreeGrid 2822 lines). TreeGrid may be referenced by inventory lists — relevant only as a library dependency to map, not to rewrite.
- `lumos_app_rpm/files/war_overlay/webapps/lib/cues/` — CUE widget library (form, dialog, charting, wizard, layout). Library dependency.
- `lumos_app_rpm/xmp_patches/` — DB scripts, fault correlation rules (`EventBasedInventoryRules.xml` 234), datacenter event translations (VPC, Vcenter, Vm, Host, Cluster, Datastore). Backend fault-correlation config, not UI.
- `srtg_rpm/` — SRTG (segment routing / traffic engineering) bean contexts and install metadata. Out of POC scope.
- `xmp_assembly_installer/` — Maven aggregation poms only.
- `xmp_assembly_static_files/src/main/resources/XMPInstaller/` — Spring wiring for inventory-discovery-process, feature info, bootstrap. Server-side configuration, relevant only as REST-endpoint/backend context for the Angular rebuild.
- `xmp_rpm/`, `xmp_parent_pom*/`, `xmp_assembly_third_party/`, `repackage_xwt_services_jar/` — Maven infrastructure.
- Root-level misc: `buid_break.txt`, `test.txt`, `precheckforrpm.py`, `svninfo.sh`, `CONFLICT_FILES.txt` — admin/meta.

## Additional observations for the rebuild team

- The two Angular classic-rebuild screens map cleanly onto two Dojo roots: Inventory → `applications/inventory/` (driven by `InventoryListView.js`, `DeviceDetailsPage.js`, `DeviceDetailTabViewController.js`, with Chassis/VDC via `VdcDetails.js` + `esChassisDetail.html`, and Device 360 via `lib/ifm/_360/`). Fault Management → `applications/AlarmManagement/` (driven by `AlarmListView.js`, `EventListView.js`, `SyslogListView.js`/`SyslogListViewWebSocket.js`, `CorrelatedAlarms.js`/`AlarmCorrelatedView.js`).
- Column/table metadata is externalized in JSON (`InventoryListMetadata*.json`, `AlarmListMetadata.json`, `EventListMetadata.json`, `SyslogListMetadata.json`, per-type `Alarm_*.json` / `Event_*.json` in the detail cell data directory, `DeviceDetailTabViewMetadata.json`). This is a significant asset for the rebuild — most column definitions, labels, and type mappings can be lifted directly.
- i18n bundles are large and comprehensive (InventoryProperties en 1814 lines, AlarmEventProperties 374–390 per locale). Reuse opportunity.
- WebSocket support for syslog is already present (`SyslogListViewWebSocket.js` 647 lines). Alarms and events are likely polling-based in this codebase; AutoRefresh mixin exists (`_AutoRefreshControllerMixin.js` 103, `PauseAutoRefreshButton.js`, `EPNMRefreshIntervalWidget.js` 236).
- WAP registry XML (`navigation.xml`, `pageViews.xml`, `pages.xml`, `views.xml`, `actions.xml`) is the framework-level wiring for menus and page routing. The Angular app will need equivalent routing data and likely can reference these files to understand action-handler bindings.
- OSGi bundle indicator: `MANIFEST.MF` under webapp `META-INF/`, plus `osgi-context.xml`. Suggests the platform packages the webapp as an OSGi bundle within a larger EPNM runtime.
- Duplicate/legacy files in tree: `AddEditDeviceWidget_old_PI.js`, `Utils_old_PI.js`, `GroupTreePanelOld.js`, `sample_pom*`, `pom_nogen.xml`, `log4j.xml.junk`. Treat with caution — use current files, not `_old_PI` variants.
- Anomalies: `applications/AlarmManagement/js/rashmi.js` (1 line) and `xmp_rpm/.../XMPIngeration/rashmi` (70 lines) appear to be developer scratch. `buid_break.txt` (1 line) is a root-level marker of a prior build break.
