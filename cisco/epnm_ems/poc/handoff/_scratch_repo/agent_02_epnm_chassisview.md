# Agent 02 — EPNM `chassisview` Tree Report Absorption

Source: `/home/cmoore/programming/ai_opportunities/cisco/epnm_ems/poc/REPO/EPNM/tree-reports/chassisview_tree_report.md`
Repo root (in report): `/Users/cmoore/Documents/programming/EPNM/chassis/chassisview`

Report-declared counts:
- Included text-like files: 3,008
- Included directories: 559
- Total raw lines: 5,477,386
- Skipped binary files: 4
- Skipped ignored-extension files: 11

---

## 1. Repo Shape at a Glance

Top level of `chassisview/`:

- `chassisview/` (nested) — the core Maven multi-module with three submodules:
  - `chassisview-api/` — Java/Spring backend. REST DTOs, services, metadata handlers. Key classes: `ChassisViewServiceImpl.java` (2,897 lines), `ChassisViewV2RestServiceImpl.java` (1,191 lines), `ChassisViewImpl.java` (1,182 lines), `ChassisViewRestServiceImpl.java` (749 lines).
  - `chassisview-pid/` — "PID" (Product ID) support: a runtime registry of chassis and pluggable definitions consumed by the front-end widget, plus Ruby sanity-test scripts and a Python deploy toolchain. Houses the largest single JS in the repo, `ChassisWidget.js` (22,241 lines), and the `inventory/` tree of device/pluggable JSON per platform family.
  - `chassisview-ui/` — Dojo-based front-end. Ships the Device 360 chassis widget, popovers, toolbars, rack widgets, and the SVG/hotspot handlers. Secondary `ChassisWidget.js` here is 4,920 lines.
- `chassisview-mockdata/` — static captured REST responses and fixtures under `development/ncs2k/ncs2006-1/webacs/...` used to drive the widget without a live EPNM.
- `chassisview-parent/` — parent POM.
- `chassisview-resource/` — the asset library. One subdirectory per device family (asr1k, asr900, asr9k, cat6500, cbr, crs, me1200, ncs1k, ncs2k, ncs4k, ncs520, ncs540, ncs5500, ncs5k, ncs6k, rack), plus `chassisview/`, `jsonTest/`, `staticFiles/`. **This is where the overwhelming bulk of SVG and JSON volume lives.**
- `ems/` — A separate Maven pair (`ems-api`, `ems-ui`) that implements the *Device Details* / *NE Info* tabbed shell (Chassis, Interface, Inventory, Alarms, Circuits, Configuration, Performance, Image tabs). This looks like the Device Details page that hosts the chassis view on the left.
- Root build artifacts: `Jenkinsfile` (150 lines), `.gitignore`, `.project`.

Backing services (in `chassisview-api`) expose V1 and V2 REST surfaces over paths such as `/rs/chassis/chassisview/v2/device/{id}/chassisview/{moduleId}`, `/equipments/alarm`, `/ports/alarm`, `/equipments/state`, `/ports/state`, `getNeighbors/{ip}`, `devicespec/{id}`, `chassisexplorer`, `getConbinedSVGs` [sic], `metadata`, `supporteddevicetypes`. These URL shapes are recoverable from the mock-data tree and will be the contract the EMS backend must match for a transparent swap.

## 2. SVG Asset Organization

SVGs live almost entirely under `chassisview-resource/<family>/...`. Two axes of organization:

**(a) Per-device chassis (top-level of each family dir).** Directories named `Cisco_<Product>_Router/` or `Cisco_<Product>/` each hold `data/<name>.json` + `images/*.svg`. The chassis-level SVG shows the full faceplate and is typically large (hundreds to tens of thousands of lines).

Representative chassis-level paths:
- `chassisview-resource/asr1k/Cisco_ASR_1013_Router/images/ASR-1013-Front_Core.svg` (11,136 lines)
- `chassisview-resource/asr9k/Cisco_ASR_9904_Router/images/ASR-9904-Front.svg` (6,732 lines)
- `chassisview-resource/asr9k/Cisco_ASR_9910_Router/images/ASR-9910-Rear.svg` (6,069 lines)
- `chassisview-resource/ncs2k/Cisco_NCS_2015/images/NCS2015-SA.svg` (7,836 lines)
- `chassisview-resource/ncs540/Cisco_8212-48FH-M_Router/images/8212-48FH-M_front_core.svg` (22,272 lines)
- `chassisview-resource/ncs540/Cisco_8818_Router/images/8818-SYS_rear_core.svg` (18,836 lines)
- `chassisview-resource/cat6500/Cisco_Catalyst_6504-E_Switch/images/C6504-E_Rear_core.svg` (24,406 lines)
- `chassisview-resource/ncs6k/Cisco_NCS_6000/images/NCS-6008-Rear.svg` (26,480 lines)

**(b) Per-module / pluggable (`<family>/pluggables/images/`).** Split again into `horizontal/`, `vertical/`, and in some families `flip/` subdirectories — these likely correspond to display-orientation variants (front-panel portrait/landscape rendering modes). Each module (line card, RSP, fan, power supply, optic) has its own SVG, plus dedicated `_filler.svg` variants for empty slots.

Representative pluggable paths:
- `chassisview-resource/asr9k/pluggables/images/horizontal/A9K-MPA-20X10GE.svg` (930 lines)
- `chassisview-resource/asr9k/pluggables/images/vertical/A9K-RSP880-SE.svg` (3,244 lines)
- `chassisview-resource/asr9k/pluggables/images/flip/A9K-MPA-4X10GE.svg` (917 lines)
- `chassisview-resource/ncs2k/pluggables/images/horizontal/15454-M-TNC-K9.svg` (3,515 lines)
- `chassisview-resource/ncs5500/pluggables/images/horizontal/NC55-18H18F.svg` (19,310 lines)
- `chassisview-resource/ncs5500/pluggables/images/horizontal/NC55-5516-FAN.svg` (59,625 lines) — largest single SVG I saw
- `chassisview-resource/ncs540/pluggables/images/horizontal/88-LC1-12TH24EH-E.svg` (26,983 lines)

**(c) A separate, small generic SVG set in the UI module:** `chassisview/chassisview-ui/src/storm/chassisview/v2/svg/images/` — icons and alarm glyphs (`alertCritical.svg`, `alertMajor.svg`, `fi-admindown.svg`, `cir_led_light_active.svg`, `rec_led_light_active.svg`, `fiext_port_critical.svg`, etc.). These are the status-overlay icons drawn on top of module/port SVGs. Also here: `snapsvg/snap.svg.js` (6,925 lines) — Snap.svg library, likely the SVG DOM manipulation engine.

**Organization axis summary.** SVGs are organized by **device family → specific chassis**, with pluggables kept in a sibling `pluggables/images/{horizontal|vertical|flip}/` folder scoped to each family. There is heavy duplication (horizontal/vertical are essentially the same assets with different orientation metadata). A handful of common optics (`QSFP.svg`, `SFP.svg`, `CPAK.svg`, `GLC.svg`, `ONS-CFP2.svg`) are repeated inside nearly every family's pluggables directory.

## 3. JavaScript / Dojo Surface

Two front-end roots:

**(a) `chassisview/chassisview-ui/src/storm/chassisview/v2/` — the core chassis widget.** Top-level JS files (widget entry points):
- `ChassisWidget.js` (4,920 lines) — main widget
- `ChassisView.js` (2,011 lines) — view controller
- `utils.js` (1,285 lines)
- `rackWidget.js` (1,069 lines), `singleRackWidget.js` (153), `virtualRack.js` (935)
- `ChassisImage.js` (582), `ChassisDialogWidget.js` (244), `ChassisPopoverWidget.js` (253), `ChassisPopup.js` (126)
- `MultipleView.js` (216), `PreferenceWidget.js` (357), `ContextualToolbar.js` (47), `toolbar.js` (513)
- `chassisDataService.js` (538) — REST client
- `chassisPortPopover.js` (235), `deviceAlarmPopover.js` (191), `chassisSearchBox.js` (155)
- `pluggableZoomWidget.js` (654), `configFormBuilder.js` (78)
- `pid_assort.js` (183), `pid_os.js` (275)

Subdirectories under the same `v2/`:
- `hotspot/` — interaction layer: `portState.js` (399), `cardDetails.js` (303), `addCard.js` (202), `cardConfig.js` (127), `equipmentAlarm.js` (142), `equipmentState.js` (140), `ledState.js` (109), `moduleAlarm.js` (106), `moduleState.js` (34), `portAlarm.js` (140), `hotspots.js` (31). **These are the exact files the classic-view port-click and module-click behavior lives in** (see §5).
- `lib/` — widgets and helpers: `expandableTree.js` (313), `ngcvToolbar.js` (466), `KeywordTokenField.js` (277), `zoomDetector.js` (198), `slideMenu.js` (133), `settingMenu.js` (116), `circuitPathFilter.js` (136), `configCardLayer.js` (157), `interfaceConfigRouter.js` (154), `chassisActionPopover.js` (94).
- `plugin/` — `circuitPathWidget.js` (1,125), `patchCordWidget.js` (749).
- `nls/` — i18n (en/ja/ko) strings.
- `templates/` — Dojo HTML templates (see §8).
- `widget/SampleExtendedIFWS.js` (312) — extension-point sample.
- `package.chassisview.profile.js` — Dojo build profile.

**(b) `chassisview/chassisview-pid/.../pidsupport/ChassisWidget.js` (22,241 lines).** This is the behemoth — the PID-support / runtime-registry version of the widget. Same directory also holds `NewSearch.js`, `pid_assort.js`, `pid_os.js`, `SampleExtendedIFWS.js`, and `piddescription.html` (545 lines).

**(c) Per-family `js/ChassisViewMetaDataV2.js`.** Every device-family directory under `chassisview-resource/<family>/js/` has one. These are metadata definitions: the list of supported PIDs and their rendering parameters. Line counts reflect family breadth:
- `asr9k` 1,065 lines, `asr1k` 1,014, `asr900` 627, `ncs5500` 1,112, `ncs540` 1,034, `ncs1k` 971, `cat6500` 791, `cbr` 489, `ncs2k` 483, `me1200` 474, `ncs4k` 665, `ncs5k` 671, `ncs6k` 639, `crs` 504, `ncs520` 520.

**Dojo evidence.** File naming (`*Widget.js` pattern, `nls/{en,ja,co}/` i18n layout, `templates/*.html` HTML-template-per-widget pattern, `package.*.profile.js` Dojo build profiles, `define([...], function(...){})` AMD-module style implied by the structure) is textbook Dojo 1.x. `snap.svg.js` is the rendering library.

Total JS files in the report are consistent with the ~186-file estimate; the bulk of behavior lives in the ~30 top-level files in `v2/`, the `hotspot/` dir (11 files), and the per-family `ChassisViewMetaDataV2.js` set (15 files).

## 4. JSON Metadata

Roughly four classes of JSON, by purpose:

**(a) Per-chassis data definitions (`<family>/Cisco_<Product>/data/Cisco_<Product>.json`).** These pair with each chassis SVG and describe slot layouts, supported modules, and hotspot coordinates. Sizes scale with chassis complexity. Examples:
- `chassisview-resource/asr9k/Cisco_ASR_9922_Router/data/Cisco_ASR_9922_Router.json` (439 lines)
- `chassisview-resource/ncs540/Cisco_8808_Router/data/Cisco_8808_Router.json` (520 lines)
- `chassisview-resource/ncs2k/Cisco_ONS_15454/data/Cisco_ONS_15454.json` (467 lines)
- `chassisview-resource/ncs5500/Cisco_NCS_5516/data/Cisco_NCS_5516.json` (416 lines)

**(b) Per-family `pluggables/data/pluggables.json`.** One giant registry per family enumerating all supported pluggables. These are huge:
- `asr9k/pluggables/data/pluggables.json` — 53,381 lines
- `ncs540/pluggables/data/pluggables.json` — 49,312 lines
- `ncs5500/pluggables/data/pluggables.json` — 50,334 lines
- `ncs2k/pluggables/data/pluggables.json` — 27,094 lines
- `asr900/pluggables/data/pluggables.json` — 17,815 lines
- `ncs1k/pluggables/data/pluggables.json` — 3,914 lines
- `ncs4k/pluggables/data/pluggables.json` — 5,053 lines
- `ncs6k/pluggables/data/pluggables.json` — 3,761 lines
- `ncs5k/pluggables/data/pluggables.json` — 6,350 lines
- `cbr/pluggables/data/pluggables.json` — 1,373 lines
- `cat6500/pluggables/data/pluggables.json` — 3,301 lines
- `crs/pluggables/data/pluggables.json` — 543 lines

**(c) PID-support inventory snapshots (`chassisview-pid/.../pidsupport/inventory/<family>/Cisco_<Product>/*.json`).** Representative device-instance payloads used to bootstrap / unit-test the widget. Per device: `<Name>_chassisdata.json` (small, 13–50 lines) and `<Name>_inventory.json` (large, 124–13,802 lines). The `CBR-8-CCAP` inventory is 13,802 lines; an `ASR-9010-AC` inventory is 1,108. Per-pluggable JSONs (e.g., `ASR9001-LC.json` 312 lines, `NCS4K-RP.json` 949 lines) live in sibling `pluggables/` directories. Also here: `metadata_format.json` (29 lines, a schema definition) and `pidrelations.json` (3,509 lines, the PID-to-module compatibility graph).

**(d) UI-module runtime data (`chassisview-ui/src/storm/chassisview/v2/data/`).** Small configuration/test JSONs: `alarmConfig.json` (16), `chassisExplorer.json` (472), `config.json` (13), `configActionMappings.json` (42), `deviceAlarms.json` (62), `hotSpots.json` (25), `imageUrl.json` (4), `interfaceData.json` (37), `interfaceTypeList.json` (25), `inventory.json` (201), `pluggables.json` (469), `power.json` (35), `slot.json` (41), `spanloss.json` (29), `speed.json` (11), `tagList.json` (29), `treeTest.json` (466), `version.json` (1), `Cisco_ASR_903.json` (529), `Cisco_NCS_4016.json` (698). These appear to be fixtures / defaults.

**(e) EMS tab metadata (`ems/ems-ui/src/storm/ems/metadata/`):** `cvEmsTabs.json` (102), `cvSubTabs.json` (136), `emsTabs.json` (17), `interfaceTypeProperty.json` (516), `neData.json` (20), `tabs.json` (41). These drive the outer tabbed Device Details shell.

**(f) Annotations (`chassisview-resource/annotation/`):** `DeviceMetaData.annotation` (47), `hotSpots.annotation` (17), `pluggables.annotation` (46). Schema/annotation files — possibly Java-annotation-driven generation targets.

## 5. Interactive Component Indicators

Strong evidence that module-click and port-state interactivity is a first-class, extensible subsystem. The `chassisview-ui/src/storm/chassisview/v2/hotspot/` directory is purpose-built for exactly this:

- `hotspots.js` (31 lines) — likely a dispatcher/registry.
- `portState.js` (399 lines), `portAlarm.js` (140 lines) — port-level interactive state and alarm overlays.
- `moduleState.js` (34 lines), `moduleAlarm.js` (106 lines) — module-level.
- `equipmentState.js` (140 lines), `equipmentAlarm.js` (142 lines) — equipment (chassis) level.
- `ledState.js` (109 lines) — LED icon state rendering.
- `cardDetails.js` (303 lines), `addCard.js` (202 lines), `cardConfig.js` (127 lines) — slot interaction (click a slot → show card details, add card, configure).

Reinforcing files at the widget root:
- `chassisPortPopover.js` (235), `deviceAlarmPopover.js` (191), `ChassisPopoverWidget.js` (253), `ChassisPopup.js` (126), `chassisActionPopover.js` (94) — popover UX when a port/module/alarm is clicked.
- `pluggableZoomWidget.js` (654), `chassisview-ui/.../nls/.../pluggableZoomWidget.js` — zoom-into-a-module interaction.
- `templates/portPopoverTemplate.html` (19 lines), `deviceAlarmTemplate.html` (19 lines), `slotView.html` (89 lines).
- `data/hotSpots.json` (25 lines), `annotation/hotSpots.annotation` (17 lines) — hotspot schema.

The `rs/chassis/chassisview/v2/device/{id}/chassisview/<moduleId>` mock-data endpoints (many such numeric module IDs present) show that each module in a chassis has its own REST resource — the click handler almost certainly fetches per-module details on demand. Port/equipment alarm and state REST endpoints are separate siblings (`.../equipments/alarm`, `.../ports/alarm`, `.../equipments/state`, `.../ports/state`).

Implication for POC. The interactive chassis is not merely a static SVG — it is a Dojo widget system with a REST-backed hotspot layer, per-module drill-down, popover templates, and per-alarm overlay logic. Reproducing this on the EMS side will almost certainly require rebuilding the hotspot dispatch, popover, and state-overlay systems in Angular. The SVG assets themselves can likely be reused as-is, but the behavior around them cannot.

## 6. Device-Type / Device-Family Coverage

Explicit top-level device-family directories in `chassisview-resource/`:

- `asr1k/` — ASR 1000 series (e.g. ASR 1013). Classic IOS-XE platform.
- `asr900/` — ASR 900 series: ASR 901S, 902, 902U, 903, 903U, 907, 920 variants, NCS 4201/4202/4206/4216 (the 4200 series lives here). Primarily IOS-XE access/aggregation.
- `asr9k/` — ASR 9000 series: 9001, 9006, 9010, 9901, 9902, 9903, 9904, 9906, 9910, 9912, 9922, plus ASR 9000v satellite. IOS-XR.
- `cat6500/` — Catalyst 6504-E, 6509, VSS. IOS (classic).
- `cbr/` — Cisco cBR-8 converged broadband router.
- `crs/` — CRS-1 8-slot and 16-slot. IOS-XR.
- `me1200/` — ME 1200 Ethernet access device.
- `ncs1k/` — NCS 1001, 1002, 1004, LS-2520. Optical.
- `ncs2k/` — NCS 2002, 2006, 2015, and legacy ONS 15454. DWDM optical (TL1-managed; see §8).
- `ncs4k/` — NCS 4009, 4016. OTN.
- `ncs520/` — NCS 520-X variants.
- `ncs540/` — very broad: NCS 540 variants, NCS 57B1/57C1/57D2, Cisco 8000 series (8011, 8101, 8111, 8201, 8202, 8212, 8608, 8711, 8712, 8804, 8808, 8812, 8818). Modern IOS-XR.
- `ncs5500/` — NCS 5500 / 55A1 / 55A2 / 57C3 / 5501 / 5502 / 5504 / 5508 / 5516, NCS 560 series. IOS-XR.
- `ncs5k/` — NCS 5001, 5002, 5011.
- `ncs6k/` — NCS 6000 / 6008.
- `rack/` — Cisco R42610 rack rendering + generic virtual racks.

**NX-OS / Nexus observation.** There is **no dedicated `nexus/` or `n9k/` family directory**. However, Nexus assets do appear *inside* other families: `chassisview-resource/ncs5500/pluggables/images/horizontal/N9K-C9508-FAN.svg` (39,565 lines), `N9K-PAC-3000W-B.svg`, `N9K-PUV-3000W-B.svg` — Nexus 9508 fan and Nexus power supplies are bundled with NCS 5500. This suggests either (a) limited Nexus chassis coverage via shared hardware rather than full chassis rendering, or (b) the Nexus chassis view is implemented outside the chassisview module entirely. Likely Nexus/NX-OS is out of primary EPNM scope — which aligns with the Cisco CI/CD engagement being an NX-OS pipeline separate from EPNM.

Likely categorization (to be validated, not proven):
- **IOS-XR families:** asr9k, crs, ncs1k, ncs4k, ncs520, ncs540 (including 8000 series), ncs5k, ncs5500, ncs6k.
- **IOS-XE families:** asr1k, asr900.
- **IOS classic:** cat6500.
- **Optical / TL1:** ncs2k, ncs1k (partial).
- **DOCSIS / cable:** cbr.
- **NX-OS:** no dedicated support.

The `chassisview-pid/.../pidsupport/inventory/` tree is further organized with explicit labels `ASR9K-IOSXR/`, `optical-TL1/`, `asr90xFamily/`, `CBR8/`, `NCS1k/`, `NCS4k/`, which corroborates the family mapping above.

## 7. Build / Packaging Indicators

- **Maven.** Every submodule has `pom.xml`. A `chassisview-parent/pom.xml` (230 lines) drives the reactor; the top-level `chassisview/pom.xml` (47 lines) is the aggregator. `chassisview-ui/pom.xml` is the largest (243 lines) — presumably invokes Dojo build and WRO packaging. Each resource-family submodule has its own `pom.xml` (84–85 lines) and an `assembly.xml` (19–25 lines) for packaging family-specific JARs/ZIPs.
- **Dojo build profiles.** `package.chassisview.profile.js` (112 lines) at the UI root, `package.ems.profile.js` (71 lines) in ems-ui, and per-family `package.profile.js` (76–78 lines) — standard Dojo `profile.js` layer definitions.
- **WRO4J.** `src/WEB-INF/wro.xml` in both `chassisview-ui` (55 lines) and `ems-ui` (31 lines) — WRO4J web-resource-optimizer config (JS/CSS bundling and minification). Classic early-2010s Java-webapp front-end pipeline.
- **Spring.** `META-INF/spring/chassis-rest-context.xml`, `chassis_ui_wap_rs.xml`, `ems-context.xml`, `ems_wap_rs.xml` — Spring DI + Apache CXF JAX-RS ("wap-rs" suggests Web Application Portal REST service) service publication.
- **Jenkins.** Root `Jenkinsfile` (150 lines) — CI declarative pipeline.
- **Deploy / ops scripts.** `chassisview-pid/.../pidsupport/deploy/` contains Python scripts (`transform.py`, `mp4.py`, `nexus.py` — ironically named files under directory/ and rest_api/), `common.py`, `reg_pid.py`, `replace_chassis_widget.py`, and `update.sh` (359 lines). These look like the mechanism for hot-loading new PIDs (new device models) into a running EPNM without a full re-release.
- **Ruby sanity tests.** `chassis.rb`, `device360.rb`, `nav-menu-automation.rb`, `testBaseUI.rb` — older browser automation, likely Watir/Selenium-Ruby.
- **DB bootstrap / RBAC.** `staticFiles/Temp/scripts/chassisview_rbac.sql` (257 lines), `usergroup_update.sql` (110), `baseUINeighborView.sql` (34), plus accompanying `.sh` wrappers.

## 8. Anything Else POC-Relevant

**HTML templates the Angular rebuild must cover (chassisview-ui):**
- `chassis.html` (2 lines — probably a minimal Dojo mount point)
- `index.html` (5), `tabView.html` (5), `slotView.html` (89), `toolbar.html` (38)
- `ContextualToolbar.html` (37), `alarmSummary.html` (7), `configForm.html` (15)
- `dialogHeader.html` (5), `keywordPlaceholder.html` (7), `portPopoverTemplate.html` (19)
- `settingMenuTemplate.html` (1), `slideMenuTemplate.html` (7), `deviceAlarmTemplate.html` (19)
- `SDRTmpl.html` (10)

**HTML templates on the EMS (outer-shell) side — `ems/ems-ui/.../tabs/`:**
- `chassistab/templates/index.html` (180), `chassistab/templates/notification.html` (11)
- `alarmstab/templates/alarmsTab.html` (4), `alarmSeverity.html` (83), `donutChart.html` (31)
- `circuitstab/templates/circuitsTab.html` (3)
- `configurationArchivetab/templates/ConfigurationArchiveTabView.html` (3)
- `interfacetab/templates/interfaceTab.html` (49)
- `inventorytab/templates/inventoryTab.html` (13)
- `logicaltab/templates/LogicalTabView.html` (10)
- `performancetab/templates/performanceTab.html` (71)
- `neinfo/templates/EMSAccordionContainer.html` (72), `EMSAccordionPane.html` (9), `index.html` (154)
- `neinfo/actiondelegations/addpatchcord/templates/index.html` (88)
- `neinfo/actiondelegations/provisioncard/templates/AddCard.html` (107), `GridItemWidget.html` (9)

The `ems-ui` tree reveals the **Device Details tab structure** explicitly: Alarms, Circuits, ConfigurationArchive, Configuration, Image, Interface, Inventory, Performance, Performance (cBR8-specific), plus Chassis, DeviceDetail, and Logical tabs. The cBR8 performance tab has 17 separate chart JS files (DSChannelUtilization, USChannelUtilization, FanStatus, PowerSupplyStatus, ModemHistory, etc.) — a meaningful per-device-type customization point that future POC phases may hit.

**CSS assets:**
- `chassisview-ui/src/storm/chassisview/v2/css/chassis.css` (1,572 lines) — main chassis stylesheet
- `chassisToolbar.css` (174 lines)
- `pid_style.css` (132 lines) — present in both `chassisview-pid` and `chassisview-ui` copies
- `css/fonts/chassis-view-iconfont.svg` (22 lines) — icon font

**i18n coverage.** English, Japanese, and Korean translation bundles are present throughout (`nls/en/`, `nls/ja/`, `nls/ko/`). If EMS scope targets English-only first, translation parity is a documented deferral.

**Mock data fixtures.** `chassisview-mockdata/development/ncs2k/ncs2006-1/webacs/...` provides a full captured REST response set for an NCS 2006 device (IP 10.49.228.63, device ID 223048102). Also `chassisview-resource/chassisview/data/172.25.123.219-bosshogg/...` for a second device. These are invaluable for POC: they let you drive the existing widget offline, and they document the exact REST URL shapes the Angular rebuild must emit or consume.

**Notable oddities:**
- Inventory JSON contains an entry `chassis ASR-9010-AC_inventory.json` (1,108 lines) — leading "chassis " with a space in the filename. Real filename, not a tree-report artifact.
- `LS-2520` appears under `ncs1k/` with an empty `data/LS-2520.json` (0 lines) but populated SVGs — incomplete entry.
- `chassisview-pid` holds the 22k-line `ChassisWidget.js`, which is ~4.5x larger than the one in `chassisview-ui`. Likely the source-of-truth with build-time transformations producing the smaller UI copy — worth verifying in a follow-up.
- The `getConbinedSVGs` endpoint is spelled with a typo ("Conbined" vs "Combined") in the mock-data tree. This is a real REST path and must be matched verbatim by any compatibility shim.

**POC-critical paths (short list).** These are the ones the POC authoring team should pre-load into the handoff:

1. `chassisview/chassisview-ui/src/storm/chassisview/v2/ChassisWidget.js` — entry point
2. `chassisview/chassisview-ui/src/storm/chassisview/v2/ChassisView.js` — view controller
3. `chassisview/chassisview-ui/src/storm/chassisview/v2/hotspot/*.js` — 11 files, the interaction core
4. `chassisview/chassisview-ui/src/storm/chassisview/v2/chassisDataService.js` — REST contract
5. `chassisview/chassisview-ui/src/storm/chassisview/v2/css/chassis.css` — styling
6. `chassisview/chassisview-pid/.../pidsupport/ChassisWidget.js` — full 22k-line reference
7. `chassisview/chassisview-pid/.../pidsupport/inventory/metadata_format.json` — schema
8. `chassisview/chassisview-pid/.../pidsupport/inventory/pidrelations.json` — PID relationships
9. `chassisview/chassisview-api/src/main/java/com/cisco/nms/chassisview/service/ChassisViewServiceImpl.java` — backend core (2,897 lines)
10. `chassisview/chassisview-api/src/main/java/com/cisco/nms/chassisview/rest/service/ChassisViewV2RestServiceImpl.java` — REST V2 (1,191 lines)
11. `chassisview-resource/<family>/js/ChassisViewMetaDataV2.js` — per-family metadata (15 files)
12. `chassisview-resource/annotation/*.annotation` — 3 schema-like files
13. `ems/ems-ui/src/storm/ems/neinfo/NEInfo.js` (496 lines) — Device Details shell
14. `ems/ems-ui/src/storm/ems/tabs/chassistab/ChassisTab.js` (379 lines) — chassis-tab wrapper that hosts the widget
15. `chassisview-mockdata/development/ncs2k/ncs2006-1/webacs/...` — end-to-end REST fixture for one device
16. Representative full-chassis SVG: `chassisview-resource/ncs540/Cisco_8202_Router/images/8202-SYS_front_core.svg` (3,496 lines) — mid-complexity example for POC rendering test

---

**Open question for planning (not answered by tree alone).** The chassisview widget is deeply integrated with EPNM's REST backend (DTOs, alarm state, port state, neighbor lookup, device spec, combined SVG bundling). The 10–20% backend-gap figure from prior POC framing is plausible *if* the EMS backend can serve the same V2 REST contract — but the contract surface is non-trivial (dozens of endpoints implied by `ChassisViewRestService*`). A targeted read of `ChassisViewV2RestServiceImpl.java` (1,191 lines) and `ChassisViewServiceImpl.java` (2,897 lines) would quantify this precisely.
