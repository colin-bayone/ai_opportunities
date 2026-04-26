# Repository Tree Report: chassisview

- Repository root: `/Users/cmoore/Documents/programming/EPNM/chassis/chassisview`
- Included text-like files: `3008`
- Included directories: `559`
- Total raw lines: `5477386`
- Skipped binary files: `4`
- Skipped ignored-extension files: `11`

```text
chassisview/
├── chassisview/
│   ├── chassisview-api/
│   │   ├── src/
│   │   │   └── main/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           └── nms/
│   │   │       │               ├── chassis/
│   │   │       │               │   ├── providers/
│   │   │       │               │   │   └── ChassisViewOpticalServiceProvider.java (16 lines)
│   │   │       │               │   └── ChassisViewMetadataHandler.java (264 lines)
│   │   │       │               └── chassisview/
│   │   │       │                   ├── model/
│   │   │       │                   │   ├── PortImpactState.java (33 lines)
│   │   │       │                   │   └── PortImpactStateEnum.java (25 lines)
│   │   │       │                   ├── rest/
│   │   │       │                   │   ├── dto/
│   │   │       │                   │   │   ├── AlarmDTO.java (84 lines)
│   │   │       │                   │   │   ├── AlarmListDTO.java (30 lines)
│   │   │       │                   │   │   ├── AlarmSummaryDTO.java (73 lines)
│   │   │       │                   │   │   ├── AlarmSummaryListDTO.java (23 lines)
│   │   │       │                   │   │   ├── ChassisExplorerDTO.java (155 lines)
│   │   │       │                   │   │   ├── ChassisFilterDTO.java (52 lines)
│   │   │       │                   │   │   ├── ChassisViewDTO.java (34 lines)
│   │   │       │                   │   │   ├── CircuitDTO.java (61 lines)
│   │   │       │                   │   │   ├── CircuitListDTO.java (25 lines)
│   │   │       │                   │   │   ├── DeviceSpecDTO.java (69 lines)
│   │   │       │                   │   │   ├── EquipmentBaseInfoDTO.java (108 lines)
│   │   │       │                   │   │   ├── EquipmentDTO.java (298 lines)
│   │   │       │                   │   │   ├── InterfaceDTO.java (75 lines)
│   │   │       │                   │   │   ├── InterfaceListDTO.java (33 lines)
│   │   │       │                   │   │   ├── LedDTO.java (51 lines)
│   │   │       │                   │   │   ├── NeighborDTO.java (88 lines)
│   │   │       │                   │   │   ├── NeighborListDTO.java (21 lines)
│   │   │       │                   │   │   ├── PathDTO.java (26 lines)
│   │   │       │                   │   │   ├── PathListDTO.java (36 lines)
│   │   │       │                   │   │   ├── PepDTO.java (38 lines)
│   │   │       │                   │   │   ├── PerformanceInfDTO.java (39 lines)
│   │   │       │                   │   │   ├── PerformanceInfListDTO.java (31 lines)
│   │   │       │                   │   │   ├── PhysicalConnectorDTO.java (44 lines)
│   │   │       │                   │   │   ├── PointDTO.java (122 lines)
│   │   │       │                   │   │   ├── StateDTO.java (65 lines)
│   │   │       │                   │   │   ├── StateListDTO.java (22 lines)
│   │   │       │                   │   │   ├── SupportedPIDDTO.java (58 lines)
│   │   │       │                   │   │   └── SupportedPIDListDTO.java (23 lines)
│   │   │       │                   │   ├── service/
│   │   │       │                   │   │   ├── ChassisViewRestService.java (69 lines)
│   │   │       │                   │   │   ├── ChassisViewRestServiceImpl.java (749 lines)
│   │   │       │                   │   │   └── ChassisViewV2RestServiceImpl.java (1191 lines)
│   │   │       │                   │   └── util/
│   │   │       │                   │       └── ChassisViewUtil.java (341 lines)
│   │   │       │                   ├── service/
│   │   │       │                   │   ├── ChassisView.java (30 lines)
│   │   │       │                   │   ├── ChassisViewImpl.java (1182 lines)
│   │   │       │                   │   ├── ChassisViewInventoryService.java (50 lines)
│   │   │       │                   │   ├── ChassisViewService.java (82 lines)
│   │   │       │                   │   ├── ChassisViewServiceImpl.java (2897 lines)
│   │   │       │                   │   ├── PortService.java (13 lines)
│   │   │       │                   │   └── PortServiceImpl.java (204 lines)
│   │   │       │                   └── ChassisViewSupportedDeviceTypes.java (69 lines)
│   │   │       └── resources/
│   │   │           └── META-INF/
│   │   │               └── spring/
│   │   │                   ├── chassis-rest-context.xml (22 lines)
│   │   │                   └── chassis_ui_wap_rs.xml (55 lines)
│   │   ├── .gitignore (2 lines)
│   │   └── pom.xml (134 lines)
│   ├── chassisview-pid/
│   │   ├── src/
│   │   │   ├── sanityscript/
│   │   │   │   ├── baseUI/
│   │   │   │   │   ├── Results/
│   │   │   │   │   │   └── Report-2017-7-28-1-38-41.html (28 lines)
│   │   │   │   │   ├── data/
│   │   │   │   │   │   └── baseUIMenuNavData.csv (149 lines)
│   │   │   │   │   ├── chassis.rb (275 lines)
│   │   │   │   │   ├── device360.rb (183 lines)
│   │   │   │   │   ├── nav-menu-automation.rb (204 lines)
│   │   │   │   │   └── testBaseUI.rb (370 lines)
│   │   │   │   ├── chassis.rb (273 lines)
│   │   │   │   ├── device360.rb (181 lines)
│   │   │   │   ├── nav-menu-automation.rb (205 lines)
│   │   │   │   └── testBaseUI.rb (372 lines)
│   │   │   ├── storm/
│   │   │   │   └── chassisview/
│   │   │   │       └── v2/
│   │   │   │           ├── css/
│   │   │   │           │   └── pid_style.css (132 lines)
│   │   │   │           └── pidsupport/
│   │   │   │               ├── deploy/
│   │   │   │               │   ├── one_time_scripts/
│   │   │   │               │   │   └── transform.py (67 lines)
│   │   │   │               │   ├── update/
│   │   │   │               │   │   ├── directory/
│   │   │   │               │   │   │   ├── mp4.py (31 lines)
│   │   │   │               │   │   │   └── nexus.py (40 lines)
│   │   │   │               │   │   └── rest_api/
│   │   │   │               │   │       ├── mp4.py (39 lines)
│   │   │   │               │   │       └── nexus.py (49 lines)
│   │   │   │               │   ├── common.py (7 lines)
│   │   │   │               │   ├── reg_pid.py (34 lines)
│   │   │   │               │   ├── replace_chassis_widget.py (56 lines)
│   │   │   │               │   └── update.sh (359 lines)
│   │   │   │               ├── inventory/
│   │   │   │               │   ├── ASR9K-IOSXR/
│   │   │   │               │   │   ├── Cisco_ASR_9001_Router/
│   │   │   │               │   │   │   ├── ASR-9001_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── ASR-9001_inventory.json (408 lines)
│   │   │   │               │   │   ├── Cisco_ASR_9006_Router/
│   │   │   │               │   │   │   ├── ASR-9006-AC_inventory.json (674 lines)
│   │   │   │               │   │   │   └── ASR9006-AC_chassisdata.json (15 lines)
│   │   │   │               │   │   ├── Cisco_ASR_9010_Router/
│   │   │   │               │   │   │   ├── ASR-9010_chassisdata.json (29 lines)
│   │   │   │               │   │   │   └── chassis ASR-9010-AC_inventory.json (1108 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── A9K-2T20GE-L.json (214 lines)
│   │   │   │               │   │       ├── A9K-3KW-AC.json (36 lines)
│   │   │   │               │   │       ├── A9K-4T-B.json (88 lines)
│   │   │   │               │   │       ├── A9K-8T-L.json (116 lines)
│   │   │   │               │   │       ├── A9K-MOD80-TR.json (124 lines)
│   │   │   │               │   │       ├── A9K-MODULEv.json (312 lines)
│   │   │   │               │   │       ├── A9K-MPA-20X1GE.json (312 lines)
│   │   │   │               │   │       ├── A9K-MPA-4X10GE.json (124 lines)
│   │   │   │               │   │       ├── A9K-RSP-8G.json (87 lines)
│   │   │   │               │   │       ├── A9K-RSP440-SE.json (157 lines)
│   │   │   │               │   │       ├── A9K-RSP440-TR.json (149 lines)
│   │   │   │               │   │       ├── ASR-9006-FAN.json (102 lines)
│   │   │   │               │   │       ├── ASR-9010-FAN.json (168 lines)
│   │   │   │               │   │       ├── ASR9001-LC.json (312 lines)
│   │   │   │               │   │       └── ASR9001-RP.json (71 lines)
│   │   │   │               │   ├── CBR8/
│   │   │   │               │   │   ├── Cisco_cBR-8_Converged_Broadband_Router/
│   │   │   │               │   │   │   ├── 1358869_inventory.json (13802 lines)
│   │   │   │               │   │   │   └── CBR-8-CCAP-CHASS_chassisdata.json (15 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── CBR-AC-PS.json (23 lines)
│   │   │   │               │   │       ├── CBR-CCAP-LC-40G.json (12749 lines)
│   │   │   │               │   │       ├── CBR-CCAP-SUP-160G.json (123 lines)
│   │   │   │               │   │       ├── CBR-DPIC-8X10G.json (195 lines)
│   │   │   │               │   │       ├── CBR-FAN-ASSEMBLY.json (45 lines)
│   │   │   │               │   │       ├── CBR-RF-PIC.json (195 lines)
│   │   │   │               │   │       ├── CBR-RF-PROT-PIC.json (195 lines)
│   │   │   │               │   │       ├── CBR-SUP-8X10G-PIC.json (346 lines)
│   │   │   │               │   │       └── PWR-3KW-AC-V2.json (23 lines)
│   │   │   │               │   ├── NCS1k/
│   │   │   │               │   │   ├── Cisco_NCS_1002/
│   │   │   │               │   │   │   ├── NCS1002_chassisdata.json (14 lines)
│   │   │   │               │   │   │   └── NCS1002_inventory.json (518 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── NCS1002.json (351 lines)
│   │   │   │               │   │       ├── NCS1K-AC-PSU.json (22 lines)
│   │   │   │               │   │       ├── NCS1K-CNTLR-K9.json (32 lines)
│   │   │   │               │   │       └── NCS1K-FTA.json (23 lines)
│   │   │   │               │   ├── NCS4k/
│   │   │   │               │   │   ├── Cisco_NCS_4009/
│   │   │   │               │   │   │   ├── NCS4009-SA-AC_inventory.json (4867 lines)
│   │   │   │               │   │   │   └── NCS4009-SA_chassisdata.json (14 lines)
│   │   │   │               │   │   ├── Cisco_NCS_4016/
│   │   │   │               │   │   │   ├── NCS4016-SA_chassisdata.json (14 lines)
│   │   │   │               │   │   │   └── NCS4016-SA_inventory.json (4831 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── CPAK-100G-LR4.json (33 lines)
│   │   │   │               │   │       ├── CPAK-100G-SR10.json (33 lines)
│   │   │   │               │   │       ├── NCS4009-FC-S.json (258 lines)
│   │   │   │               │   │       ├── NCS4016-FC2-M.json (633 lines)
│   │   │   │               │   │       ├── NCS4K-24LR-O-S.json (533 lines)
│   │   │   │               │   │       ├── NCS4K-2H-W.json (583 lines)
│   │   │   │               │   │       ├── NCS4K-2H10T-OP-KS.json (616 lines)
│   │   │   │               │   │       ├── NCS4K-AC-PEM.json (241 lines)
│   │   │   │               │   │       ├── NCS4K-AC-PSU.json (58 lines)
│   │   │   │               │   │       ├── NCS4K-CRAFT.json (36 lines)
│   │   │   │               │   │       ├── NCS4K-ECU.json (67 lines)
│   │   │   │               │   │       ├── NCS4K-FTA.json (47 lines)
│   │   │   │               │   │       ├── NCS4K-RP.json (949 lines)
│   │   │   │               │   │       ├── ONS-SC+-10G-LR.json (33 lines)
│   │   │   │               │   │       ├── ONS-SC+-10G-SR.json (33 lines)
│   │   │   │               │   │       └── SFP-10G-SR.json (32 lines)
│   │   │   │               │   ├── asr90xFamily/
│   │   │   │               │   │   ├── Cisco_ASR_901S-3SG-F-AH_Router/
│   │   │   │               │   │   │   ├── A901S-3SG-F-AH_chassisdata.json (14 lines)
│   │   │   │               │   │   │   └── A901S-3SG-F-AH_inventory.json (124 lines)
│   │   │   │               │   │   ├── Cisco_ASR_903_Router/
│   │   │   │               │   │   │   ├── ASR-903_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── ASR-903_inventory.json (768 lines)
│   │   │   │               │   │   ├── Cisco_ASR_907_Router/
│   │   │   │               │   │   │   ├── ASR-907_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── ASR-907_inventory.json (1308 lines)
│   │   │   │               │   │   ├── Cisco_ASR_920-12SZ-IM_Router/
│   │   │   │               │   │   │   ├── ASR-920-12SZ-IM_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── ASR-920-12SZ-IM_inventory.json (407 lines)
│   │   │   │               │   │   ├── Cisco_ASR_920_Router/
│   │   │   │               │   │   │   ├── ASR-920-24SZ-M_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── ASR-920-24SZ-M_inventory.json (974 lines)
│   │   │   │               │   │   ├── Cisco_NCS_4202/
│   │   │   │               │   │   │   ├── NCS-4202_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── NCS4202-SA_inventory.json (453 lines)
│   │   │   │               │   │   ├── Cisco_NCS_4206/
│   │   │   │               │   │   │   ├── NCS-4206_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── NCS4206-SA_inventory.json (1489 lines)
│   │   │   │               │   │   ├── Cisco_NCS_4216/
│   │   │   │               │   │   │   ├── NCS-4216_chassisdata.json (15 lines)
│   │   │   │               │   │   │   └── NCS4216-SA_inventory.json (1441 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── A900-IMA16D.json (155 lines)
│   │   │   │               │   │       ├── A900-IMA32D.json (23 lines)
│   │   │   │               │   │       ├── A900-IMA4OS.json (65 lines)
│   │   │   │               │   │       ├── A900-IMA8D.json (23 lines)
│   │   │   │               │   │       ├── A900-IMA8S.json (277 lines)
│   │   │   │               │   │       ├── A900-IMA8S1Z.json (23 lines)
│   │   │   │               │   │       ├── A900-IMA8T.json (91 lines)
│   │   │   │               │   │       ├── A900-IMA8T1Z.json (126 lines)
│   │   │   │               │   │       ├── A900-PWR1200-D.json (23 lines)
│   │   │   │               │   │       ├── A900-PWR550-A.json (23 lines)
│   │   │   │               │   │       ├── A900-RSP2A-128.json (80 lines)
│   │   │   │               │   │       ├── A900-RSP2A-54.json (70 lines)
│   │   │   │               │   │       ├── A900-RSP3C-400-W.json (62 lines)
│   │   │   │               │   │       ├── A903-FAN.json (145 lines)
│   │   │   │               │   │       ├── A903-RSP1A-55.json (80 lines)
│   │   │   │               │   │       ├── A907-FAN-E.json (135 lines)
│   │   │   │               │   │       ├── ASR-920-FAN-F.json (75 lines)
│   │   │   │               │   │       ├── ASR-920-PWR-A.json (23 lines)
│   │   │   │               │   │       ├── FTLF8519P2BCL-C4.json (38 lines)
│   │   │   │               │   │       ├── GLC-SX-MMD.json (33 lines)
│   │   │   │               │   │       ├── NCS4200-48T1E1-CE.json (23 lines)
│   │   │   │               │   │       ├── NCS4200-48T3E3-CE.json (363 lines)
│   │   │   │               │   │       ├── SFP-10G-SR.json (33 lines)
│   │   │   │               │   │       ├── SFP-GE-S.json (33 lines)
│   │   │   │               │   │       ├── SFP-GE-T.json (33 lines)
│   │   │   │               │   │       ├── SFP-OC3-IR1.json (33 lines)
│   │   │   │               │   │       └── SP7041-E .json (33 lines)
│   │   │   │               │   ├── optical-TL1/
│   │   │   │               │   │   ├── Cisco_NCS_2002/
│   │   │   │               │   │   │   ├── 15454-M2-SA_inventory.json (204 lines)
│   │   │   │               │   │   │   └── NCS2002-SA_chassisdata.json (13 lines)
│   │   │   │               │   │   ├── Cisco_NCS_2006/
│   │   │   │               │   │   │   ├── NCS2006-SA_chassisdata.json (1388 lines)
│   │   │   │               │   │   │   ├── SHELF-M6_SHELF-1_inventory.json (644 lines)
│   │   │   │               │   │   │   ├── SHELF-M6_SHELF-2_inventory.json (228 lines)
│   │   │   │               │   │   │   └── SHELF-M6_SHELF-3_inventory.json (158 lines)
│   │   │   │               │   │   ├── Cisco_NCS_2015/
│   │   │   │               │   │   │   ├── NCS2015-SA_chassisdata.json (50 lines)
│   │   │   │               │   │   │   ├── SHELF-M15_SHELF-1_inventory.json (331 lines)
│   │   │   │               │   │   │   └── SHELF-M15_SHELF-2_inventory.json (89 lines)
│   │   │   │               │   │   ├── Cisco_ONS_15454/
│   │   │   │               │   │   │   ├── 15454-M2-SA_chassisdata.json (13 lines)
│   │   │   │               │   │   │   ├── 15454-M2-SA_inventory.json (245 lines)
│   │   │   │               │   │   │   ├── 15454-M6-SA_chassisdata.json (1789 lines)
│   │   │   │               │   │   │   ├── 15454-SA-HD_chassisdata.json (1286 lines)
│   │   │   │               │   │   │   ├── SHELF-M6_SHELF-1_inventory.json (464 lines)
│   │   │   │               │   │   │   ├── SHELF-M6_SHELF-2_inventory.json (423 lines)
│   │   │   │               │   │   │   ├── SHELF-M6_SHELF-3_inventory.json (153 lines)
│   │   │   │               │   │   │   ├── SHELF_SHELF-1_inventory.json (1987 lines)
│   │   │   │               │   │   │   ├── SHELF_SHELF-2_inventory.json (1985 lines)
│   │   │   │               │   │   │   ├── SHELF_SHELF-3_inventory.json (473 lines)
│   │   │   │               │   │   │   └── SHELF_SHELF-4_inventory.json (1842 lines)
│   │   │   │               │   │   └── pluggables/
│   │   │   │               │   │       ├── 100G-CK-C.json (22 lines)
│   │   │   │               │   │       ├── 100G-LC-C.json (32 lines)
│   │   │   │               │   │       ├── 100GS-CK-LC.json (22 lines)
│   │   │   │               │   │       ├── 15454-10DME-C.json (137 lines)
│   │   │   │               │   │       ├── 15454-10E-L1.json (44 lines)
│   │   │   │               │   │       ├── 15454-10GE-XP.json (93 lines)
│   │   │   │               │   │       ├── 15454-10ME-L1-C.json (48 lines)
│   │   │   │               │   │       ├── 15454-32-DMX.json (312 lines)
│   │   │   │               │   │       ├── 15454-40-DMX-C.json (302 lines)
│   │   │   │               │   │       ├── 15454-40-MUX-C.json (302 lines)
│   │   │   │               │   │       ├── 15454-40-SMR1-C.json (99 lines)
│   │   │   │               │   │       ├── 15454-40-SMR2-C.json (99 lines)
│   │   │   │               │   │       ├── 15454-40-WSS-C.json (683 lines)
│   │   │   │               │   │       ├── 15454-40-WXC-C.json (123 lines)
│   │   │   │               │   │       ├── 15454-40E-TXP-C.json (31 lines)
│   │   │   │               │   │       ├── 15454-80-WXC-C.json (118 lines)
│   │   │   │               │   │       ├── 15454-AR-MXP.json (66 lines)
│   │   │   │               │   │       ├── 15454-AR-XP.json (175 lines)
│   │   │   │               │   │       ├── 15454-GE-XP.json (435 lines)
│   │   │   │               │   │       ├── 15454-M-10X10G-LC.json (194 lines)
│   │   │   │               │   │       ├── 15454-M-CFP-LC.json (55 lines)
│   │   │   │               │   │       ├── 15454-M-RAMAN-COP.json (21 lines)
│   │   │   │               │   │       ├── 15454-M-RAMAN-CTP=.json (91 lines)
│   │   │   │               │   │       ├── 15454-M-TNC-K9.json (51 lines)
│   │   │   │               │   │       ├── 15454-M-TSCE-K9.json (15 lines)
│   │   │   │               │   │       ├── 15454-M-WSE-K9.json (123 lines)
│   │   │   │               │   │       ├── 15454-OPT-AMP-17C.json (75 lines)
│   │   │   │               │   │       ├── 15454-OPT-AMP-C.json (75 lines)
│   │   │   │               │   │       ├── 15454-OPT-BST.json (67 lines)
│   │   │   │               │   │       ├── 15454-OPT-RAMP-C.json (85 lines)
│   │   │   │               │   │       ├── 15454-OPT-RAMP-CE.json (85 lines)
│   │   │   │               │   │       ├── 15454-OSC-CSM.json (64 lines)
│   │   │   │               │   │       ├── 15454-OSCM.json (43 lines)
│   │   │   │               │   │       ├── 15454-OTU2-XP.json (93 lines)
│   │   │   │               │   │       ├── 15454-SMR1-LIC.json (95 lines)
│   │   │   │               │   │       ├── 15454-TCC3-K9.json (15 lines)
│   │   │   │               │   │       ├── 15454E-TCC2-K9.json (15 lines)
│   │   │   │               │   │       ├── 15454E-TCCP-K9.json (15 lines)
│   │   │   │               │   │       ├── 15454W-TNCS-K9.json (34 lines)
│   │   │   │               │   │       ├── 200G-CK-LC.json (24 lines)
│   │   │   │               │   │       ├── 400G-XP-LC.json (84 lines)
│   │   │   │               │   │       ├── 40E-MXP-C.json (85 lines)
│   │   │   │               │   │       ├── 40ME-MXP-C.json (85 lines)
│   │   │   │               │   │       ├── AR-XPE.json (191 lines)
│   │   │   │               │   │       ├── EDRA-1-26.json (110 lines)
│   │   │   │               │   │       ├── EDRA-1-35.json (110 lines)
│   │   │   │               │   │       ├── EDRA-2-26.json (110 lines)
│   │   │   │               │   │       ├── EDRA-2-35.json (110 lines)
│   │   │   │               │   │       ├── NCS2K-100GS-CK-C.json (44 lines)
│   │   │   │               │   │       ├── NCS2K-12-AD-CCOFS.json (403 lines)
│   │   │   │               │   │       ├── NCS2K-16-AD-CCOFS.json (595 lines)
│   │   │   │               │   │       ├── NCS2K-16-WXC-FS.json (303 lines)
│   │   │   │               │   │       ├── NCS2K-9-SMR17FS.json (219 lines)
│   │   │   │               │   │       ├── NCS2K-MR-MXP.json (68 lines)
│   │   │   │               │   │       ├── NCS2K-SMR-20-FS.json (387 lines)
│   │   │   │               │   │       ├── NCS2K-TNCS-K9.json (15 lines)
│   │   │   │               │   │       ├── NCS2K-TNCS-O-K9.json (67 lines)
│   │   │   │               │   │       ├── OPT-EDFA-17.json (63 lines)
│   │   │   │               │   │       ├── OPT-EDFA-24.json (62 lines)
│   │   │   │               │   │       ├── SMR20-FS.json (383 lines)
│   │   │   │               │   │       ├── SMR9-24-FS.json (219 lines)
│   │   │   │               │   │       ├── SMR9-34-FS.json (215 lines)
│   │   │   │               │   │       └── TSC.json (11 lines)
│   │   │   │               │   ├── metadata_format.json (29 lines)
│   │   │   │               │   └── pidrelations.json (3509 lines)
│   │   │   │               ├── ChassisWidget.js (22241 lines)
│   │   │   │               ├── NewSearch.js (145 lines)
│   │   │   │               ├── SampleExtendedIFWS.js (312 lines)
│   │   │   │               ├── TableTestDetailsWidget.html (8 lines)
│   │   │   │               ├── emptymenu.json (13 lines)
│   │   │   │               ├── pid_assort.js (213 lines)
│   │   │   │               ├── pid_os.js (275 lines)
│   │   │   │               └── piddescription.html (545 lines)
│   │   │   ├── baseUITest.csv (7 lines)
│   │   │   ├── chassis.rb (275 lines)
│   │   │   ├── device360.rb (183 lines)
│   │   │   ├── nav-menu-automation.rb (204 lines)
│   │   │   └── testBaseUI.rb (370 lines)
│   │   ├── .gitignore (1 lines)
│   │   ├── assembly.xml (18 lines)
│   │   └── pom.xml (84 lines)
│   └── chassisview-ui/
│       ├── src/
│       │   ├── WEB-INF/
│       │   │   └── wro.xml (55 lines)
│       │   └── storm/
│       │       ├── chassisview/
│       │       │   └── v2/
│       │       │       ├── css/
│       │       │       │   ├── fonts/
│       │       │       │   │   └── chassis-view-iconfont.svg (22 lines)
│       │       │       │   ├── chassis.css (1572 lines)
│       │       │       │   ├── chassisToolbar.css (174 lines)
│       │       │       │   └── pid_style.css (132 lines)
│       │       │       ├── data/
│       │       │       │   ├── Cisco_ASR_903.json (529 lines)
│       │       │       │   ├── Cisco_NCS_4016.json (698 lines)
│       │       │       │   ├── FC1-PORT_SLOT_1_STATUS.json (1 lines)
│       │       │       │   ├── FC2-PORT_SLOT_0_STATUS.json (1 lines)
│       │       │       │   ├── FC2-PORT_SLOT_1_STATUS.json (1 lines)
│       │       │       │   ├── alarmConfig.json (16 lines)
│       │       │       │   ├── cevModuleNCS4KFCM_PORT_SLOT_0_STATUS.json (1 lines)
│       │       │       │   ├── chassisExplorer.json (472 lines)
│       │       │       │   ├── config.json (13 lines)
│       │       │       │   ├── configActionMappings.json (42 lines)
│       │       │       │   ├── deviceAlarms.json (62 lines)
│       │       │       │   ├── emptymenu.json (13 lines)
│       │       │       │   ├── hotSpots.json (25 lines)
│       │       │       │   ├── imageUrl.json (4 lines)
│       │       │       │   ├── interfaceData.json (37 lines)
│       │       │       │   ├── interfaceTypeList.json (25 lines)
│       │       │       │   ├── inventory.json (201 lines)
│       │       │       │   ├── pluggables.json (469 lines)
│       │       │       │   ├── power.json (35 lines)
│       │       │       │   ├── slot.json (41 lines)
│       │       │       │   ├── spanloss.json (29 lines)
│       │       │       │   ├── speed.json (11 lines)
│       │       │       │   ├── tagList.json (29 lines)
│       │       │       │   ├── treeTest.json (466 lines)
│       │       │       │   └── version.json (1 lines)
│       │       │       ├── hotspot/
│       │       │       │   ├── addCard.js (202 lines)
│       │       │       │   ├── cardConfig.js (127 lines)
│       │       │       │   ├── cardDetails.js (303 lines)
│       │       │       │   ├── equipmentAlarm.js (142 lines)
│       │       │       │   ├── equipmentState.js (140 lines)
│       │       │       │   ├── hotspots.js (31 lines)
│       │       │       │   ├── ledState.js (109 lines)
│       │       │       │   ├── moduleAlarm.js (106 lines)
│       │       │       │   ├── moduleState.js (34 lines)
│       │       │       │   ├── portAlarm.js (140 lines)
│       │       │       │   └── portState.js (399 lines)
│       │       │       ├── lib/
│       │       │       │   ├── KeywordTokenField.js (277 lines)
│       │       │       │   ├── _KeywordTokenField.js (392 lines)
│       │       │       │   ├── actionHandler.js (7 lines)
│       │       │       │   ├── chassisActionPopover.js (94 lines)
│       │       │       │   ├── circuitPathFilter.js (136 lines)
│       │       │       │   ├── configCardLayer.js (157 lines)
│       │       │       │   ├── configurationForm.js (125 lines)
│       │       │       │   ├── expandableTree.js (313 lines)
│       │       │       │   ├── expandableTreeNode.js (134 lines)
│       │       │       │   ├── interfaceConfigRouter.js (154 lines)
│       │       │       │   ├── ngcvToolbar.js (466 lines)
│       │       │       │   ├── settingMenu.js (116 lines)
│       │       │       │   ├── slideMenu.js (133 lines)
│       │       │       │   └── zoomDetector.js (198 lines)
│       │       │       ├── nls/
│       │       │       │   ├── en/
│       │       │       │   │   ├── ChassisWidget.js (139 lines)
│       │       │       │   │   ├── PreferenceWidget.js (13 lines)
│       │       │       │   │   └── pluggableZoomWidget.js (7 lines)
│       │       │       │   ├── ja/
│       │       │       │   │   ├── ChassisWidget.js (136 lines)
│       │       │       │   │   ├── PreferenceWidget.js (12 lines)
│       │       │       │   │   └── pluggableZoomWidget.js (3 lines)
│       │       │       │   ├── ko/
│       │       │       │   │   ├── ChassisWidget.js (138 lines)
│       │       │       │   │   ├── PreferenceWidget.js (15 lines)
│       │       │       │   │   └── pluggableZoomWidget.js (3 lines)
│       │       │       │   ├── ChassisWidget.js (142 lines)
│       │       │       │   ├── PreferenceWidget.js (18 lines)
│       │       │       │   └── pluggableZoomWidget.js (8 lines)
│       │       │       ├── plugin/
│       │       │       │   ├── circuitPathWidget.js (1125 lines)
│       │       │       │   └── patchCordWidget.js (749 lines)
│       │       │       ├── svg/
│       │       │       │   ├── images/
│       │       │       │   │   ├── RX.svg (22 lines)
│       │       │       │   │   ├── TX.svg (22 lines)
│       │       │       │   │   ├── alertCritical.svg (22 lines)
│       │       │       │   │   ├── alertCritical_disabled.svg (15 lines)
│       │       │       │   │   ├── alertMajor.svg (22 lines)
│       │       │       │   │   ├── alertMajor_disabled.svg (15 lines)
│       │       │       │   │   ├── alertMinor.svg (22 lines)
│       │       │       │   │   ├── alertMinor_disabled.svg (16 lines)
│       │       │       │   │   ├── arrow.svg (9 lines)
│       │       │       │   │   ├── atozArrow.svg (9 lines)
│       │       │       │   │   ├── auto-up.svg (15 lines)
│       │       │       │   │   ├── cir_led_light_active.svg (28 lines)
│       │       │       │   │   ├── cir_led_light_off.svg (28 lines)
│       │       │       │   │   ├── cir_led_light_standby.svg (28 lines)
│       │       │       │   │   ├── circuitPort.svg (6 lines)
│       │       │       │   │   ├── down.svg (15 lines)
│       │       │       │   │   ├── fi-admindown.svg (23 lines)
│       │       │       │   │   ├── fi-arrow.svg (9 lines)
│       │       │       │   │   ├── fi-brokenimage.svg (20 lines)
│       │       │       │   │   ├── fi-download.svg (13 lines)
│       │       │       │   │   ├── fi-info.svg (14 lines)
│       │       │       │   │   ├── fi-inprogress.svg (13 lines)
│       │       │       │   │   ├── fi-normal.svg (15 lines)
│       │       │       │   │   ├── fi-pin.svg (11 lines)
│       │       │       │   │   ├── fi-record-critical.svg (11 lines)
│       │       │       │   │   ├── fi-record-information.svg (11 lines)
│       │       │       │   │   ├── fi-record-major.svg (11 lines)
│       │       │       │   │   ├── fi-record-minor.svg (11 lines)
│       │       │       │   │   ├── fi-record-warning.svg (11 lines)
│       │       │       │   │   ├── fi-record.svg (11 lines)
│       │       │       │   │   ├── fi-warning.svg (17 lines)
│       │       │       │   │   ├── fiext-chassis-view.svg (464 lines)
│       │       │       │   │   ├── fiext-chassis.svg (45 lines)
│       │       │       │   │   ├── fiext-pinaz.svg (15 lines)
│       │       │       │   │   ├── fiext_port.svg (26 lines)
│       │       │       │   │   ├── fiext_port_critical.svg (26 lines)
│       │       │       │   │   ├── fiext_port_information.svg (26 lines)
│       │       │       │   │   ├── fiext_port_major.svg (26 lines)
│       │       │       │   │   ├── fiext_port_minor.svg (26 lines)
│       │       │       │   │   ├── fiext_port_warning.svg (26 lines)
│       │       │       │   │   ├── highlightPort_ie11.svg (49 lines)
│       │       │       │   │   ├── highlightPort_static.svg (13 lines)
│       │       │       │   │   ├── hightlightPort.svg (6 lines)
│       │       │       │   │   ├── icon_chassis_view_front.svg (1 lines)
│       │       │       │   │   ├── icon_chassis_view_rear.svg (1 lines)
│       │       │       │   │   ├── light_att.svg (42 lines)
│       │       │       │   │   ├── port_power.svg (13 lines)
│       │       │       │   │   ├── powerLevel.svg (14 lines)
│       │       │       │   │   ├── rec_led_light_active.svg (27 lines)
│       │       │       │   │   ├── rec_led_light_off.svg (27 lines)
│       │       │       │   │   ├── rec_led_light_standby.svg (27 lines)
│       │       │       │   │   ├── spanLoss.svg (11 lines)
│       │       │       │   │   ├── test.svg (27 lines)
│       │       │       │   │   ├── topo_a_pointer.svg (14 lines)
│       │       │       │   │   ├── topo_z_pointer.svg (12 lines)
│       │       │       │   │   ├── unknown.svg (18 lines)
│       │       │       │   │   ├── up.svg (15 lines)
│       │       │       │   │   └── ztoaArrow.svg (9 lines)
│       │       │       │   └── snapsvg/
│       │       │       │       ├── snap.js (20 lines)
│       │       │       │       └── snap.svg.js (6925 lines)
│       │       │       ├── templates/
│       │       │       │   ├── ContextualToolbar.html (37 lines)
│       │       │       │   ├── SDRTmpl.html (10 lines)
│       │       │       │   ├── alarmSummary.html (7 lines)
│       │       │       │   ├── chassis.html (2 lines)
│       │       │       │   ├── configForm.html (15 lines)
│       │       │       │   ├── deviceAlarmTemplate.html (19 lines)
│       │       │       │   ├── dialogHeader.html (5 lines)
│       │       │       │   ├── index.html (5 lines)
│       │       │       │   ├── keywordPlaceholder.html (7 lines)
│       │       │       │   ├── portPopoverTemplate.html (19 lines)
│       │       │       │   ├── settingMenuTemplate.html (1 lines)
│       │       │       │   ├── slideMenuTemplate.html (7 lines)
│       │       │       │   ├── slotView.html (89 lines)
│       │       │       │   ├── tabView.html (5 lines)
│       │       │       │   └── toolbar.html (38 lines)
│       │       │       ├── widget/
│       │       │       │   └── SampleExtendedIFWS.js (312 lines)
│       │       │       ├── ChassisDialogWidget.js (244 lines)
│       │       │       ├── ChassisImage.js (582 lines)
│       │       │       ├── ChassisPopoverWidget.js (253 lines)
│       │       │       ├── ChassisPopup.js (126 lines)
│       │       │       ├── ChassisView.js (2011 lines)
│       │       │       ├── ChassisWidget.js (4920 lines)
│       │       │       ├── ContextualToolbar.js (47 lines)
│       │       │       ├── MultipleView.js (216 lines)
│       │       │       ├── PreferenceWidget.js (357 lines)
│       │       │       ├── chassisDataService.js (538 lines)
│       │       │       ├── chassisDialogHeader.js (92 lines)
│       │       │       ├── chassisItemFileWriteStore.js (15 lines)
│       │       │       ├── chassisPortPopover.js (235 lines)
│       │       │       ├── chassisSearchBox.js (155 lines)
│       │       │       ├── configFormBuilder.js (78 lines)
│       │       │       ├── deviceAlarmPopover.js (191 lines)
│       │       │       ├── pid_assort.js (183 lines)
│       │       │       ├── pid_os.js (275 lines)
│       │       │       ├── pluggableZoomWidget.js (654 lines)
│       │       │       ├── rackWidget.js (1069 lines)
│       │       │       ├── singleRackWidget.js (153 lines)
│       │       │       ├── toolbar.js (513 lines)
│       │       │       ├── utils.js (1285 lines)
│       │       │       └── virtualRack.js (935 lines)
│       │       └── package.chassisview.profile.js (112 lines)
│       ├── .gitignore (1 lines)
│       ├── assembly.xml (74 lines)
│       └── pom.xml (243 lines)
├── chassisview-mockdata/
│   └── development/
│       ├── ncs2k/
│       │   └── ncs2006-1/
│       │       └── webacs/
│       │           ├── alarm-rest/
│       │           │   ├── AlarmStats (1 lines)
│       │           │   └── Alarms (1 lines)
│       │           ├── api/
│       │           │   ├── v1/
│       │           │   │   ├── data/
│       │           │   │   │   ├── Equipment (1 lines)
│       │           │   │   │   └── ServiceDetails (1 lines)
│       │           │   │   └── op/
│       │           │   │       └── action/
│       │           │   │           └── actions.json (1 lines)
│       │           │   └── v2/
│       │           │       └── op/
│       │           │           └── srrg/
│       │           │               └── resources/
│       │           │                   └── srrg/
│       │           │                       └── detailed.json (1 lines)
│       │           ├── inventoryRestService/
│       │           │   └── ifm/
│       │           │       └── inventory-rest/
│       │           │           ├── deviceLocations/
│       │           │           │   └── 10.49.228.63 (1 lines)
│       │           │           ├── auditData (1 lines)
│       │           │           ├── deviceData (1 lines)
│       │           │           ├── devices (1 lines)
│       │           │           ├── interfaceDataOptimized (1 lines)
│       │           │           └── moduleData (1 lines)
│       │           └── rs/
│       │               ├── chassis/
│       │               │   └── chassisview/
│       │               │       ├── device/
│       │               │       │   └── 223048102/
│       │               │       │       └── supported (1 lines)
│       │               │       ├── v2/
│       │               │       │   ├── device/
│       │               │       │   │   ├── 10.49.228.63/
│       │               │       │   │   │   ├── equipments/
│       │               │       │   │   │   │   └── alarm (1 lines)
│       │               │       │   │   │   └── ports/
│       │               │       │   │   │       └── alarm (1 lines)
│       │               │       │   │   ├── 223048102/
│       │               │       │   │   │   ├── chassisview/
│       │               │       │   │   │   │   ├── 0 (1 lines)
│       │               │       │   │   │   │   ├── 296260406 (1 lines)
│       │               │       │   │   │   │   ├── 296260407 (1 lines)
│       │               │       │   │   │   │   ├── 296260408 (1 lines)
│       │               │       │   │   │   │   ├── 296260409 (1 lines)
│       │               │       │   │   │   │   ├── 296260410 (1 lines)
│       │               │       │   │   │   │   ├── 296260411 (1 lines)
│       │               │       │   │   │   │   ├── 296260412 (1 lines)
│       │               │       │   │   │   │   ├── 296260413 (1 lines)
│       │               │       │   │   │   │   ├── 296260414 (1 lines)
│       │               │       │   │   │   │   ├── 296260416 (1 lines)
│       │               │       │   │   │   │   ├── 296260417 (1 lines)
│       │               │       │   │   │   │   ├── 296260418 (1 lines)
│       │               │       │   │   │   │   ├── 296260419 (1 lines)
│       │               │       │   │   │   │   ├── 296260420 (1 lines)
│       │               │       │   │   │   │   ├── 296260421 (1 lines)
│       │               │       │   │   │   │   ├── 296260422 (1 lines)
│       │               │       │   │   │   │   ├── 296260423 (1 lines)
│       │               │       │   │   │   │   ├── 296260424 (1 lines)
│       │               │       │   │   │   │   ├── 296260425 (1 lines)
│       │               │       │   │   │   │   ├── 296260426 (1 lines)
│       │               │       │   │   │   │   ├── 296260427 (1 lines)
│       │               │       │   │   │   │   ├── 296260428 (1 lines)
│       │               │       │   │   │   │   ├── 296260429 (1 lines)
│       │               │       │   │   │   │   ├── 296260430 (1 lines)
│       │               │       │   │   │   │   ├── 296260431 (1 lines)
│       │               │       │   │   │   │   ├── 296260432 (1 lines)
│       │               │       │   │   │   │   ├── 296260433 (1 lines)
│       │               │       │   │   │   │   ├── 296260434 (1 lines)
│       │               │       │   │   │   │   ├── 296260435 (1 lines)
│       │               │       │   │   │   │   ├── 296260436 (1 lines)
│       │               │       │   │   │   │   ├── 296260437 (1 lines)
│       │               │       │   │   │   │   ├── 296260438 (1 lines)
│       │               │       │   │   │   │   ├── 296260440 (1 lines)
│       │               │       │   │   │   │   ├── 296260441 (1 lines)
│       │               │       │   │   │   │   ├── 296260442 (1 lines)
│       │               │       │   │   │   │   ├── 296260443 (1 lines)
│       │               │       │   │   │   │   ├── 296260444 (1 lines)
│       │               │       │   │   │   │   └── 296260446 (1 lines)
│       │               │       │   │   │   ├── chassisexplorer (1 lines)
│       │               │       │   │   │   ├── getConbinedSVGs (1 lines)
│       │               │       │   │   │   └── metadata (25736 lines)
│       │               │       │   │   └── getNeighbors/
│       │               │       │   │       └── 10.49.228.63 (1 lines)
│       │               │       │   ├── devicespec/
│       │               │       │   │   └── 223048102 (1 lines)
│       │               │       │   ├── equipments/
│       │               │       │   │   └── state (1 lines)
│       │               │       │   └── ports/
│       │               │       │       └── state (1 lines)
│       │               │       └── supporteddevicetypes (1 lines)
│       │               └── wap/
│       │                   └── preference/
│       │                       └── value/
│       │                           └── @@me/
│       │                               ├── userpreferences_chassisAlarmBlink (0 lines)
│       │                               ├── userpreferences_chassisRacksDisplay.json (1 lines)
│       │                               └── userpreferences_chassisRefreshInterval.json (1 lines)
│       └── cv-mock-device-config.json (16 lines)
├── chassisview-parent/
│   ├── .gitignore (3 lines)
│   ├── .project (29 lines)
│   └── pom.xml (230 lines)
├── chassisview-resource/
│   ├── annotation/
│   │   ├── DeviceMetaData.annotation (47 lines)
│   │   ├── hotSpots.annotation (17 lines)
│   │   └── pluggables.annotation (46 lines)
│   ├── asr1k/
│   │   ├── Cisco_ASR_1013_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_1013_Router.json (194 lines)
│   │   │   └── images/
│   │   │       ├── ASR-1013-Front_Core.svg (11136 lines)
│   │   │       └── ASR-1013-Rear-Core.svg (1256 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (1014 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (2455 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── ASR1000-2T+20X1GE.svg (8577 lines)
│   │   │       │   ├── ASR1000-ESP200.svg (5131 lines)
│   │   │       │   ├── ASR1000-ESP40-Front.svg (2849 lines)
│   │   │       │   ├── ASR1000-MIP100.svg (936 lines)
│   │   │       │   ├── ASR1000-RP2-Front.svg (2891 lines)
│   │   │       │   ├── ASR1000-SIP40-Front_core.svg (1242 lines)
│   │   │       │   ├── ASR1013-FILLER-SIP.svg (92 lines)
│   │   │       │   ├── ASR1013-FILLER-SLC.svg (92 lines)
│   │   │       │   ├── ASR1013-FLC-FILLER.svg (79 lines)
│   │   │       │   ├── ASR1013-LC-FILLER.svg (74 lines)
│   │   │       │   ├── ASR1013-PWR-AC.svg (3607 lines)
│   │   │       │   ├── ASR1013-PWR-DC.svg (4495 lines)
│   │   │       │   ├── ASR1013-PWR-Filler.svg (93 lines)
│   │   │       │   ├── ASR1013-RP-FILLER.svg (79 lines)
│   │   │       │   ├── CFP-100G-ER4.svg (759 lines)
│   │   │       │   ├── CFP-100G-LR4.svg (684 lines)
│   │   │       │   ├── CFP-100G-SR10.svg (531 lines)
│   │   │       │   ├── CPAK.svg (137 lines)
│   │   │       │   ├── EPA-10x10GE.svg (3824 lines)
│   │   │       │   ├── EPA-18x1GE.svg (5223 lines)
│   │   │       │   ├── EPA-1x100GE.svg (3146 lines)
│   │   │       │   ├── EPA-CPAK-2x40GE.svg (3155 lines)
│   │   │       │   ├── GLC.svg (309 lines)
│   │   │       │   ├── ONS-CFP2.svg (47 lines)
│   │   │       │   ├── QSFP.svg (210 lines)
│   │   │       │   ├── SFP.svg (253 lines)
│   │   │       │   ├── SPA-1X10GE-L-V2.svg (944 lines)
│   │   │       │   ├── SPA-5X1GE-V2.svg (2078 lines)
│   │   │       │   └── SPA-8X1GE-V2.svg (2079 lines)
│   │   │       └── vertical/
│   │   │           ├── ASR1000-2T+20X1GE.svg (8600 lines)
│   │   │           ├── ASR1000-ESP200.svg (5131 lines)
│   │   │           ├── ASR1000-ESP40-Front.svg (2855 lines)
│   │   │           ├── ASR1000-MIP100.svg (936 lines)
│   │   │           ├── ASR1000-RP2-Front.svg (2892 lines)
│   │   │           ├── ASR1000-SIP40-Front_core.svg (1242 lines)
│   │   │           ├── ASR1013-FILLER-SIP.svg (93 lines)
│   │   │           ├── ASR1013-FILLER-SLC.svg (92 lines)
│   │   │           ├── ASR1013-FLC-FILLER.svg (79 lines)
│   │   │           ├── ASR1013-LC-FILLER.svg (79 lines)
│   │   │           ├── ASR1013-PWR-AC.svg (3609 lines)
│   │   │           ├── ASR1013-PWR-DC.svg (4551 lines)
│   │   │           ├── ASR1013-PWR-Filler.svg (93 lines)
│   │   │           ├── ASR1013-RP-FILLER.svg (79 lines)
│   │   │           ├── CFP-100G-ER4.svg (765 lines)
│   │   │           ├── CFP-100G-LR4.svg (690 lines)
│   │   │           ├── CFP-100G-SR10.svg (532 lines)
│   │   │           ├── CPAK.svg (139 lines)
│   │   │           ├── EPA-10x10GE.svg (3856 lines)
│   │   │           ├── EPA-18x1GE.svg (5266 lines)
│   │   │           ├── EPA-1x100GE.svg (3158 lines)
│   │   │           ├── EPA-CPAK-2x40GE.svg (3167 lines)
│   │   │           ├── GLC.svg (310 lines)
│   │   │           ├── ONS-CFP2.svg (47 lines)
│   │   │           ├── QSFP.svg (210 lines)
│   │   │           ├── SFP.svg (261 lines)
│   │   │           ├── SPA-1X10GE-L-V2.svg (957 lines)
│   │   │           ├── SPA-5X1GE-V2.svg (2089 lines)
│   │   │           └── SPA-8X1GE-V2.svg (2114 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (85 lines)
│   ├── asr900/
│   │   ├── Cisco_ASR-920-20SZ-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR-920-20SZ-M_Router.json (64 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-20SZ-M-Front-Core.svg (2910 lines)
│   │   ├── Cisco_ASR920-12SZ-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920-12SZ-A_Router.json (47 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12SZ-A_front_core.svg (6737 lines)
│   │   ├── Cisco_ASR920-12SZ-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920-12SZ-D_Router.json (47 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12SZ-D_front_core.svg (6539 lines)
│   │   ├── Cisco_ASR920_10S_ZPD___Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_10S_ZPD___Router.json (44 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-10SZ-PD-Front.svg (1265 lines)
│   │   ├── Cisco_ASR920_12_CZA_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_12_CZA_Router.json (56 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12CZ-A-Front.svg (2337 lines)
│   │   ├── Cisco_ASR920_12_CZ_D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_12_CZ_D_Router.json (55 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12CZ-D-Front.svg (2189 lines)
│   │   ├── Cisco_ASR920_12_SZ_IM_CC/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_12_SZ_IM_CC.json (64 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12SZ-IM-Front.svg (1141 lines)
│   │   ├── Cisco_ASR920_4S_ZA___Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_4S_ZA___Router.json (55 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-4SZ-A-Front.svg (2947 lines)
│   │   ├── Cisco_ASR920_4S_ZD_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR920_4S_ZD_Router.json (56 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-4SZ-D-Front.svg (2808 lines)
│   │   ├── Cisco_ASR_901S-2SG-F-AH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_901S-2SG-F-AH_Router.json (115 lines)
│   │   │   └── images/
│   │   │       ├── A901S-2SG-F-AH-Front.svg (597 lines)
│   │   │       └── A901S-2SG-F-AH-Rear.svg (255 lines)
│   │   ├── Cisco_ASR_901S-2SG-F-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_901S-2SG-F-D_Router.json (123 lines)
│   │   │   └── images/
│   │   │       ├── A901S-2SG-F-D-Front.svg (869 lines)
│   │   │       └── A901S-2SG-F-D-Rear.svg (255 lines)
│   │   ├── Cisco_ASR_901S-3SG-F-AH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_901S-3SG-F-AH_Router.json (123 lines)
│   │   │   └── images/
│   │   │       ├── A901S-3SG-F-AH-Rear.svg (255 lines)
│   │   │       └── A901S-3SG-F-AH_Front.svg (589 lines)
│   │   ├── Cisco_ASR_901S-3SG-F-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_901S-3SG-F-D_Router.json (129 lines)
│   │   │   └── images/
│   │   │       ├── A901S-3SG-F-D-Front.svg (881 lines)
│   │   │       └── A901S-3SG-F-D-Rear.svg (255 lines)
│   │   ├── Cisco_ASR_901S-4SG-F-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_901S-4SG-F-D_Router.json (137 lines)
│   │   │   └── images/
│   │   │       ├── A901S-4SG-F-D-Front.svg (898 lines)
│   │   │       └── A901S-4SG-F-D-Rear.svg (255 lines)
│   │   ├── Cisco_ASR_902U_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_902U_Router.json (88 lines)
│   │   │   └── images/
│   │   │       ├── ASR-902U-Front.svg (273 lines)
│   │   │       └── ASR-902U-Rear.svg (714 lines)
│   │   ├── Cisco_ASR_902_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_902_Router.json (88 lines)
│   │   │   └── images/
│   │   │       ├── ASR-902-Front.svg (273 lines)
│   │   │       └── ASR-902-Rear.svg (714 lines)
│   │   ├── Cisco_ASR_903U_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_903U_Router.json (108 lines)
│   │   │   └── images/
│   │   │       └── ASR-903U-Front.svg (1067 lines)
│   │   ├── Cisco_ASR_903_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_903_Router.json (109 lines)
│   │   │   └── images/
│   │   │       └── ASR-903-Front.svg (1067 lines)
│   │   ├── Cisco_ASR_907_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_907_Router.json (186 lines)
│   │   │   └── images/
│   │   │       └── ASR-907-Front.svg (571 lines)
│   │   ├── Cisco_ASR_920-12SZ-IM_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920-12SZ-IM_Router.json (64 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-12SZ-IM-Front.svg (1141 lines)
│   │   ├── Cisco_ASR_920-8S4Z-PD_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920-8S4Z-PD_Router.json (47 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-8S4Z-PD_core.svg (1159 lines)
│   │   ├── Cisco_ASR_920U-12SZ-IM_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920U-12SZ-IM_Router.json (64 lines)
│   │   │   └── images/
│   │   │       └── ASR-920U-12SZ-IM-Front.svg (1141 lines)
│   │   ├── Cisco_ASR_920_24SZIM_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920_24SZIM_Router.json (64 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-24SZ-IM-Front.svg (3626 lines)
│   │   ├── Cisco_ASR_920_24SZM_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920_24SZM_Router.json (57 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-24SZ-M-Front.svg (2005 lines)
│   │   ├── Cisco_ASR_920_24TZM_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_920_24TZM_Router.json (55 lines)
│   │   │   └── images/
│   │   │       └── ASR-920-24TZ-M-Front.svg (4385 lines)
│   │   ├── Cisco_NCS_4201/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4201.json (58 lines)
│   │   │   └── images/
│   │   │       └── NCS-4201-Front.svg (2022 lines)
│   │   ├── Cisco_NCS_4202/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4202.json (65 lines)
│   │   │   └── images/
│   │   │       └── NCS-4202-Front.svg (1141 lines)
│   │   ├── Cisco_NCS_4206/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4206.json (109 lines)
│   │   │   └── images/
│   │   │       └── NCS-4206-Front.svg (1067 lines)
│   │   ├── Cisco_NCS_4216/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4216.json (215 lines)
│   │   │   └── images/
│   │   │       ├── NCS-4216-Front.svg (571 lines)
│   │   │       └── NCS4216-Rear.svg (20207 lines)
│   │   ├── Cisco_NCS_4216_F2B/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4216_F2B.json (200 lines)
│   │   │   └── images/
│   │   │       └── NCS4216-F2B-SA-Front.svg (6176 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (627 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (17815 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── 10xGE-2x10GE-FIXED.svg (2256 lines)
│   │   │       │   ├── A900-FILLER-FT.svg (91 lines)
│   │   │       │   ├── A900-FILLER-LC.svg (117 lines)
│   │   │       │   ├── A900-FILLER-PT.svg (105 lines)
│   │   │       │   ├── A900-FILLER-RSP.svg (128 lines)
│   │   │       │   ├── A900-IMA16D.svg (570 lines)
│   │   │       │   ├── A900-IMA16D_T1PORT-16.svg (330 lines)
│   │   │       │   ├── A900-IMA1C.svg (1512 lines)
│   │   │       │   ├── A900-IMA1X.svg (1321 lines)
│   │   │       │   ├── A900-IMA1Z8S-C.svg (10420 lines)
│   │   │       │   ├── A900-IMA1Z8S-CX.svg (10420 lines)
│   │   │       │   ├── A900-IMA1Z8S-CXMS.svg (10533 lines)
│   │   │       │   ├── A900-IMA2F.svg (1846 lines)
│   │   │       │   ├── A900-IMA2Z.svg (4048 lines)
│   │   │       │   ├── A900-IMA32D.svg (908 lines)
│   │   │       │   ├── A900-IMA32D_T1PORT-16.svg (326 lines)
│   │   │       │   ├── A900-IMA3G-IMSG.svg (430 lines)
│   │   │       │   ├── A900-IMA48D-C.svg (1148 lines)
│   │   │       │   ├── A900-IMA48D-C_SPORT-16.svg (291 lines)
│   │   │       │   ├── A900-IMA48T-C.svg (1144 lines)
│   │   │       │   ├── A900-IMA48T-C_SPORT-16.svg (292 lines)
│   │   │       │   ├── A900-IMA4C3794.svg (537 lines)
│   │   │       │   ├── A900-IMA4OS.svg (9327 lines)
│   │   │       │   ├── A900-IMA6EM.svg (422 lines)
│   │   │       │   ├── A900-IMA8CS1Z-M-filler.svg (72 lines)
│   │   │       │   ├── A900-IMA8CS1Z-M.svg (709 lines)
│   │   │       │   ├── A900-IMA8D.svg (2561 lines)
│   │   │       │   ├── A900-IMA8S.svg (9176 lines)
│   │   │       │   ├── A900-IMA8S1Z.svg (10353 lines)
│   │   │       │   ├── A900-IMA8T.svg (2585 lines)
│   │   │       │   ├── A900-IMA8T1Z.svg (3558 lines)
│   │   │       │   ├── A900-IMA8Z-L.svg (1604 lines)
│   │   │       │   ├── A900-IMA8Z.svg (9281 lines)
│   │   │       │   ├── A900-IMASER14A-S.svg (939 lines)
│   │   │       │   ├── A900-IMASER14A-S_SPORT-4.svg (184 lines)
│   │   │       │   ├── A900-PWR1200-A.svg (1262 lines)
│   │   │       │   ├── A900-PWR1200-D.svg (1659 lines)
│   │   │       │   ├── A900-PWR550-A.svg (1293 lines)
│   │   │       │   ├── A900-PWR550-D-E.svg (1686 lines)
│   │   │       │   ├── A900-PWR550-D.svg (1556 lines)
│   │   │       │   ├── A900-PWR900-D2.svg (753 lines)
│   │   │       │   ├── A900-RSP2A-128.svg (3355 lines)
│   │   │       │   ├── A900-RSP2A-64.svg (3364 lines)
│   │   │       │   ├── A900-RSP3C-200-S.svg (3563 lines)
│   │   │       │   ├── A900-RSP3C-400-S.svg (3573 lines)
│   │   │       │   ├── A900-RSP3C-400-W.svg (3222 lines)
│   │   │       │   ├── A900U-RSP2A-128.svg (2157 lines)
│   │   │       │   ├── A900U-RSP2A-64.svg (2160 lines)
│   │   │       │   ├── A902-FAN-E.svg (816 lines)
│   │   │       │   ├── A902-FAN.svg (226 lines)
│   │   │       │   ├── A902-FILLER-FT.svg (100 lines)
│   │   │       │   ├── A903-FAN-E.svg (1093 lines)
│   │   │       │   ├── A903-FAN-H.svg (896 lines)
│   │   │       │   ├── A903-FAN.svg (802 lines)
│   │   │       │   ├── A903-FILLER-FT.svg (105 lines)
│   │   │       │   ├── A903-FILLER-LC.svg (786 lines)
│   │   │       │   ├── A903-FILLER-PWR.svg (484 lines)
│   │   │       │   ├── A903-FILLER-RSP.svg (509 lines)
│   │   │       │   ├── A903-RSP1A-55.svg (3181 lines)
│   │   │       │   ├── A903-RSP1B-55.svg (3182 lines)
│   │   │       │   ├── A907-FAN-E.svg (1246 lines)
│   │   │       │   ├── A907-FAN.svg (481 lines)
│   │   │       │   ├── A907-FILLER-FT.svg (203 lines)
│   │   │       │   ├── A907-FILLER-LC.svg (108 lines)
│   │   │       │   ├── A907-FILLER-PT.svg (114 lines)
│   │   │       │   ├── A907-FILLER-RSP.svg (122 lines)
│   │   │       │   ├── A920-24SZ-IM-FILLER-LC.svg (87 lines)
│   │   │       │   ├── A920-24SZ-IM-FILLER-PT.svg (65 lines)
│   │   │       │   ├── A9XX-2IMA-CARRIER.svg (384 lines)
│   │   │       │   ├── ASR-920-10SZ-PD-RSP.svg (327 lines)
│   │   │       │   ├── ASR-920-12CZ-A-PWR.svg (98 lines)
│   │   │       │   ├── ASR-920-12CZ-D-PWR.svg (146 lines)
│   │   │       │   ├── ASR-920-12CZ-LineCard.svg (1461 lines)
│   │   │       │   ├── ASR-920-12CZ-RSP.svg (129 lines)
│   │   │       │   ├── ASR-920-12SZ-A_front_Ports.svg (1308 lines)
│   │   │       │   ├── ASR-920-12SZ-A_front_rp.svg (221 lines)
│   │   │       │   ├── ASR-920-12SZ-LC.svg (1795 lines)
│   │   │       │   ├── ASR-920-12SZ-RSP.svg (191 lines)
│   │   │       │   ├── ASR-920-20SZ-Front-PowerSupply_Filler.svg (74 lines)
│   │   │       │   ├── ASR-920-20SZ-M-Front_linecard.svg (3968 lines)
│   │   │       │   ├── ASR-920-20SZ-M_slot_R0.svg (202 lines)
│   │   │       │   ├── ASR-920-24SZ-M-LC.svg (1784 lines)
│   │   │       │   ├── ASR-920-24SZ-M-RSP.svg (136 lines)
│   │   │       │   ├── ASR-920-24TZ-M-LC.svg (3059 lines)
│   │   │       │   ├── ASR-920-24TZ-M-RSP.svg (129 lines)
│   │   │       │   ├── ASR-920-4SZ-A-PWR.svg (125 lines)
│   │   │       │   ├── ASR-920-4SZ-D-PWR.svg (178 lines)
│   │   │       │   ├── ASR-920-4SZ-LC.svg (532 lines)
│   │   │       │   ├── ASR-920-4SZ-RSP.svg (129 lines)
│   │   │       │   ├── ASR-920-8S4Z-PD_mgmt.svg (330 lines)
│   │   │       │   ├── ASR-920-8S4Z-PD_ports.svg (1376 lines)
│   │   │       │   ├── ASR-920-PWR-A.svg (3107 lines)
│   │   │       │   ├── ASR-920-PWR-D.svg (756 lines)
│   │   │       │   ├── ASR-920-PWR-FILLER.svg (83 lines)
│   │   │       │   ├── ASR-920-PWR400-A.svg (276 lines)
│   │   │       │   ├── ASR-920-PWR400-D.svg (349 lines)
│   │   │       │   ├── CPAK.svg (92 lines)
│   │   │       │   ├── GLC.svg (190 lines)
│   │   │       │   ├── N560-IMA2C.svg (774 lines)
│   │   │       │   ├── NCS-4201-LC.svg (1784 lines)
│   │   │       │   ├── NCS-4201-PWR-A.svg (3107 lines)
│   │   │       │   ├── NCS-4201-RSP.svg (136 lines)
│   │   │       │   ├── NCS4200-1H-PK.svg (1512 lines)
│   │   │       │   ├── NCS4200-1T16G-PS.svg (1049 lines)
│   │   │       │   ├── NCS4200-1T8LR-PS.svg (10353 lines)
│   │   │       │   ├── NCS4200-1T8S-10CS.svg (10400 lines)
│   │   │       │   ├── NCS4200-1T8S-20CS.svg (1041 lines)
│   │   │       │   ├── NCS4200-2H-PQ.svg (784 lines)
│   │   │       │   ├── NCS4200-2Q-P.svg (1846 lines)
│   │   │       │   ├── NCS4200-3GMS.svg (716 lines)
│   │   │       │   ├── NCS4200-48T1E1-CE.svg (1130 lines)
│   │   │       │   ├── NCS4200-48T3E3-CE.svg (1097 lines)
│   │   │       │   ├── NCS4200-8E1T1-CE.svg (2579 lines)
│   │   │       │   ├── NCS4200-8T-PS.svg (9281 lines)
│   │   │       │   ├── NCS4201-FILLER-PT.svg (83 lines)
│   │   │       │   ├── NCS4202-12SZ-FILLER-LC.svg (1859 lines)
│   │   │       │   ├── NCS4202-12SZ-LC.svg (1795 lines)
│   │   │       │   ├── NCS4202-12SZ-RSP.svg (191 lines)
│   │   │       │   ├── NCS4202-FILLER-RSP.svg (83 lines)
│   │   │       │   ├── NCS4202-PWR400-A.svg (276 lines)
│   │   │       │   ├── NCS4202-PWR400-D.svg (349 lines)
│   │   │       │   ├── NCS420X-RSP.svg (3573 lines)
│   │   │       │   ├── NCS4216-F2B-FAN-F-Filler.svg (74 lines)
│   │   │       │   ├── NCS4216-F2B-FAN-F.svg (463 lines)
│   │   │       │   ├── NCS4216-F2B-FAN-Filler.svg (79 lines)
│   │   │       │   ├── NCS4216-F2B-FAN.svg (463 lines)
│   │   │       │   ├── NCS4216-PWR-FAN-Filler.svg (74 lines)
│   │   │       │   ├── NCS4216-PWR-FAN.svg (501 lines)
│   │   │       │   ├── NCS4216-RSP.svg (3222 lines)
│   │   │       │   ├── QSFP.svg (174 lines)
│   │   │       │   ├── SFP-1.svg (417 lines)
│   │   │       │   └── SFP.svg (173 lines)
│   │   │       └── vertical/
│   │   │           ├── 10xGE-2x10GE-FIXED.svg (2260 lines)
│   │   │           ├── A900-FILLER-FT.svg (91 lines)
│   │   │           ├── A900-FILLER-LC.svg (117 lines)
│   │   │           ├── A900-FILLER-PT.svg (105 lines)
│   │   │           ├── A900-FILLER-RSP.svg (128 lines)
│   │   │           ├── A900-IMA16D.svg (572 lines)
│   │   │           ├── A900-IMA16D_T1PORT-16.svg (331 lines)
│   │   │           ├── A900-IMA1C.svg (1513 lines)
│   │   │           ├── A900-IMA1X.svg (1374 lines)
│   │   │           ├── A900-IMA1Z8S-C.svg (10420 lines)
│   │   │           ├── A900-IMA1Z8S-CX.svg (10420 lines)
│   │   │           ├── A900-IMA1Z8S-CXMS.svg (6731 lines)
│   │   │           ├── A900-IMA2F.svg (1848 lines)
│   │   │           ├── A900-IMA2Z.svg (4044 lines)
│   │   │           ├── A900-IMA32D.svg (909 lines)
│   │   │           ├── A900-IMA32D_T1PORT-16.svg (327 lines)
│   │   │           ├── A900-IMA3G-IMSG.svg (510 lines)
│   │   │           ├── A900-IMA48D-C.svg (1149 lines)
│   │   │           ├── A900-IMA48D-C_SPORT-16.svg (292 lines)
│   │   │           ├── A900-IMA48T-C.svg (1146 lines)
│   │   │           ├── A900-IMA48T-C_SPORT-16.svg (293 lines)
│   │   │           ├── A900-IMA4C3794.svg (546 lines)
│   │   │           ├── A900-IMA4OS.svg (9335 lines)
│   │   │           ├── A900-IMA6EM.svg (422 lines)
│   │   │           ├── A900-IMA8CS1Z-M-filler.svg (67 lines)
│   │   │           ├── A900-IMA8CS1Z-M.svg (894 lines)
│   │   │           ├── A900-IMA8D.svg (2644 lines)
│   │   │           ├── A900-IMA8S.svg (9632 lines)
│   │   │           ├── A900-IMA8S1Z.svg (10362 lines)
│   │   │           ├── A900-IMA8T.svg (2676 lines)
│   │   │           ├── A900-IMA8T1Z.svg (3558 lines)
│   │   │           ├── A900-IMA8Z.svg (9281 lines)
│   │   │           ├── A900-IMASER14A-S.svg (935 lines)
│   │   │           ├── A900-IMASER14A-S_SPORT-4.svg (186 lines)
│   │   │           ├── A900-PWR1200-A.svg (1322 lines)
│   │   │           ├── A900-PWR1200-D.svg (1739 lines)
│   │   │           ├── A900-PWR550-A.svg (1370 lines)
│   │   │           ├── A900-PWR550-D-E.svg (1764 lines)
│   │   │           ├── A900-PWR550-D.svg (1636 lines)
│   │   │           ├── A900-PWR900-D2.svg (758 lines)
│   │   │           ├── A900-RSP2A-128.svg (3361 lines)
│   │   │           ├── A900-RSP2A-64.svg (3370 lines)
│   │   │           ├── A900-RSP3C-200-S.svg (3563 lines)
│   │   │           ├── A900-RSP3C-400-S.svg (3573 lines)
│   │   │           ├── A900-RSP3C-400-W.svg (3222 lines)
│   │   │           ├── A900U-RSP2A-128.svg (3354 lines)
│   │   │           ├── A900U-RSP2A-64.svg (3361 lines)
│   │   │           ├── A902-FAN-E.svg (1153 lines)
│   │   │           ├── A902-FAN.svg (226 lines)
│   │   │           ├── A902-FILLER-FT.svg (100 lines)
│   │   │           ├── A903-FAN-E.svg (1053 lines)
│   │   │           ├── A903-FAN-H.svg (895 lines)
│   │   │           ├── A903-FAN.svg (802 lines)
│   │   │           ├── A903-FILLER-FT.svg (105 lines)
│   │   │           ├── A903-FILLER-LC.svg (784 lines)
│   │   │           ├── A903-FILLER-PWR.svg (484 lines)
│   │   │           ├── A903-FILLER-RSP.svg (509 lines)
│   │   │           ├── A903-RSP1A-55.svg (3182 lines)
│   │   │           ├── A903-RSP1B-55.svg (3184 lines)
│   │   │           ├── A907-FAN-E.svg (1246 lines)
│   │   │           ├── A907-FAN.svg (481 lines)
│   │   │           ├── A907-FILLER-FT.svg (203 lines)
│   │   │           ├── A907-FILLER-LC.svg (109 lines)
│   │   │           ├── A907-FILLER-PT.svg (114 lines)
│   │   │           ├── A907-FILLER-RSP.svg (122 lines)
│   │   │           ├── A920-24SZ-IM-FILLER-LC.svg (87 lines)
│   │   │           ├── A920-24SZ-IM-FILLER-PT.svg (65 lines)
│   │   │           ├── A9XX-2IMA-CARRIER.svg (384 lines)
│   │   │           ├── ASR-920-10SZ-PD-RSP.svg (328 lines)
│   │   │           ├── ASR-920-12CZ-A-PWR.svg (114 lines)
│   │   │           ├── ASR-920-12CZ-D-PWR.svg (178 lines)
│   │   │           ├── ASR-920-12CZ-LineCard.svg (1920 lines)
│   │   │           ├── ASR-920-12CZ-RSP.svg (155 lines)
│   │   │           ├── ASR-920-12SZ-A_front_Ports.svg (1308 lines)
│   │   │           ├── ASR-920-12SZ-A_front_rp.svg (222 lines)
│   │   │           ├── ASR-920-12SZ-LC.svg (1796 lines)
│   │   │           ├── ASR-920-12SZ-RSP.svg (192 lines)
│   │   │           ├── ASR-920-20SZ-Front-PowerSupply_Filler.svg (79 lines)
│   │   │           ├── ASR-920-20SZ-M-Front_linecard.svg (3996 lines)
│   │   │           ├── ASR-920-20SZ-M_slot_R0.svg (203 lines)
│   │   │           ├── ASR-920-24SZ-M-LC.svg (1784 lines)
│   │   │           ├── ASR-920-24SZ-M-RSP.svg (136 lines)
│   │   │           ├── ASR-920-24TZ-M-LC.svg (2835 lines)
│   │   │           ├── ASR-920-24TZ-M-RSP.svg (154 lines)
│   │   │           ├── ASR-920-4SZ-A-PWR.svg (125 lines)
│   │   │           ├── ASR-920-4SZ-D-PWR.svg (178 lines)
│   │   │           ├── ASR-920-4SZ-LC.svg (532 lines)
│   │   │           ├── ASR-920-4SZ-RSP.svg (129 lines)
│   │   │           ├── ASR-920-PWR-A.svg (3108 lines)
│   │   │           ├── ASR-920-PWR-D.svg (756 lines)
│   │   │           ├── ASR-920-PWR-FILLER.svg (83 lines)
│   │   │           ├── ASR-920-PWR400-A.svg (277 lines)
│   │   │           ├── ASR-920-PWR400-D.svg (350 lines)
│   │   │           ├── CPAK.svg (108 lines)
│   │   │           ├── GLC.svg (191 lines)
│   │   │           ├── N560-IMA2C.svg (781 lines)
│   │   │           ├── NCS-4201-LC.svg (2345 lines)
│   │   │           ├── NCS-4201-PWR-A.svg (3108 lines)
│   │   │           ├── NCS-4201-RSP.svg (144 lines)
│   │   │           ├── NCS4200-1H-PK.svg (1513 lines)
│   │   │           ├── NCS4200-1T16G-PS.svg (1356 lines)
│   │   │           ├── NCS4200-1T8LR-PS.svg (10362 lines)
│   │   │           ├── NCS4200-1T8S-10CS.svg (10400 lines)
│   │   │           ├── NCS4200-1T8S-20CS.svg (1080 lines)
│   │   │           ├── NCS4200-2H-PQ.svg (793 lines)
│   │   │           ├── NCS4200-2Q-P.svg (1848 lines)
│   │   │           ├── NCS4200-3GMS.svg (756 lines)
│   │   │           ├── NCS4200-48T1E1-CE.svg (1102 lines)
│   │   │           ├── NCS4200-48T3E3-CE.svg (1095 lines)
│   │   │           ├── NCS4200-8E1T1-CE.svg (2608 lines)
│   │   │           ├── NCS4200-8T-PS.svg (9281 lines)
│   │   │           ├── NCS4201-FILLER-PT.svg (83 lines)
│   │   │           ├── NCS4202-12SZ-FILLER-LC.svg (1860 lines)
│   │   │           ├── NCS4202-12SZ-LC.svg (1796 lines)
│   │   │           ├── NCS4202-12SZ-RSP.svg (192 lines)
│   │   │           ├── NCS4202-FILLER-RSP.svg (82 lines)
│   │   │           ├── NCS4202-PWR400-A.svg (277 lines)
│   │   │           ├── NCS4202-PWR400-D.svg (350 lines)
│   │   │           ├── NCS420X-RSP.svg (3573 lines)
│   │   │           ├── NCS4216-F2B-FAN-F-Filler.svg (79 lines)
│   │   │           ├── NCS4216-F2B-FAN-F.svg (464 lines)
│   │   │           ├── NCS4216-F2B-FAN-Filler.svg (79 lines)
│   │   │           ├── NCS4216-F2B-FAN.svg (464 lines)
│   │   │           ├── NCS4216-PWR-FAN-Filler.svg (79 lines)
│   │   │           ├── NCS4216-PWR-FAN.svg (502 lines)
│   │   │           ├── NCS4216-RSP.svg (3222 lines)
│   │   │           ├── QSFP.svg (174 lines)
│   │   │           └── SFP.svg (261 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── asr9k/
│   │   ├── Cisco_ASR_9000_V_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9000_V_Router.json (284 lines)
│   │   │   └── images/
│   │   │       └── ASR-9000v.svg (18550 lines)
│   │   ├── Cisco_ASR_9001_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9001_Router.json (79 lines)
│   │   │   └── images/
│   │   │       └── ASR9001-Front.svg (213 lines)
│   │   ├── Cisco_ASR_9006_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9006_Router.json (235 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9006-AC-Front.svg (475 lines)
│   │   │       └── ASR-9006-AC-V2-Front.svg (464 lines)
│   │   ├── Cisco_ASR_9010_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9010_Router.json (425 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9010-AC-Front-V2.svg (877 lines)
│   │   │       └── ASR-9010-AC-Front.svg (898 lines)
│   │   ├── Cisco_ASR_9901_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9901_Router.json (126 lines)
│   │   │   └── images/
│   │   │       ├── asr9901-front_core.svg (7088 lines)
│   │   │       └── asr9901-rear_core.svg (869 lines)
│   │   ├── Cisco_ASR_9902_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9902_Router.json (128 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9902_front_core.svg (424 lines)
│   │   │       └── ASR-9902_rear_core.svg (421 lines)
│   │   ├── Cisco_ASR_9903_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9903_Router.json (155 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9903_front_core.svg (394 lines)
│   │   │       └── ASR-9903_rear_core.svg (628 lines)
│   │   ├── Cisco_ASR_9904_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9904_Router.json (120 lines)
│   │   │   └── images/
│   │   │       └── ASR-9904-Front.svg (6732 lines)
│   │   ├── Cisco_ASR_9906_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9906_Router.json (307 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9906-Front_core.svg (1666 lines)
│   │   │       ├── ASR-9906-Rear.svg (1253 lines)
│   │   │       └── ASR-9906_Front_core.svg (1869 lines)
│   │   ├── Cisco_ASR_9910_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9910_Router.json (297 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9910-Front.svg (2835 lines)
│   │   │       └── ASR-9910-Rear.svg (6069 lines)
│   │   ├── Cisco_ASR_9912_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9912_Router.json (371 lines)
│   │   │   └── images/
│   │   │       ├── ASR-9912-AC-Front.svg (3330 lines)
│   │   │       └── ASR-9912-Rear.svg (3357 lines)
│   │   ├── Cisco_ASR_9922_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ASR_9922_Router.json (439 lines)
│   │   │   └── images/
│   │   │       └── ASR-9922-Front.svg (3806 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (1065 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (53381 lines)
│   │   │   └── images/
│   │   │       ├── flip/
│   │   │       │   ├── A9K-FILLER-MPA.svg (88 lines)
│   │   │       │   ├── A9K-MPA-20X1GE.svg (1066 lines)
│   │   │       │   ├── A9K-MPA-2X10GE.svg (647 lines)
│   │   │       │   └── A9K-MPA-4X10GE.svg (917 lines)
│   │   │       ├── horizontal/
│   │   │       │   ├── 9922-FILLER-FAN.svg (74 lines)
│   │   │       │   ├── 9922-FILLER-LC.svg (90 lines)
│   │   │       │   ├── A9006-FILLER-PT.svg (92 lines)
│   │   │       │   ├── A9010-FAN-FILLER.svg (86 lines)
│   │   │       │   ├── A99-10X400GE-X.svg (4150 lines)
│   │   │       │   ├── A99-12X100GE-CM.svg (4734 lines)
│   │   │       │   ├── A99-12X100GE-CM_filler.svg (88 lines)
│   │   │       │   ├── A99-16X100GE-X.svg (9283 lines)
│   │   │       │   ├── A99-32X100GE-Filler.svg (25 lines)
│   │   │       │   ├── A99-32X100GE-X-SE.svg (6884 lines)
│   │   │       │   ├── A99-32X100GE-X-TR.svg (6886 lines)
│   │   │       │   ├── A99-32X100GE.svg (2640 lines)
│   │   │       │   ├── A99-48X10GE-1G.svg (3177 lines)
│   │   │       │   ├── A99-4HG-FLEX-X-SE.svg (7299 lines)
│   │   │       │   ├── A99-4HG-FLEX.svg (8005 lines)
│   │   │       │   ├── A99-8X100GE-SE.svg (2035 lines)
│   │   │       │   ├── A99-8X100GE-TR.svg (2042 lines)
│   │   │       │   ├── A99-RP-F.svg (1791 lines)
│   │   │       │   ├── A99-RP-F_filler.svg (189 lines)
│   │   │       │   ├── A99-RP2.svg (3160 lines)
│   │   │       │   ├── A99-RP3-SE.svg (1513 lines)
│   │   │       │   ├── A99-RP3-TR.svg (1515 lines)
│   │   │       │   ├── A99-RP3-X-SE.svg (2262 lines)
│   │   │       │   ├── A99-RP3-X-TR.svg (2256 lines)
│   │   │       │   ├── A99-RSP-SE-FILLER.svg (74 lines)
│   │   │       │   ├── A99-RSP-SE.svg (3169 lines)
│   │   │       │   ├── A99-RSP-TR-FILLER.svg (74 lines)
│   │   │       │   ├── A99-RSP-TR.svg (3159 lines)
│   │   │       │   ├── A99-SFC-S-FILLER.svg (74 lines)
│   │   │       │   ├── A99-SFC-S.svg (1764 lines)
│   │   │       │   ├── A99-SFC-T.svg (1775 lines)
│   │   │       │   ├── A99-SFC-T_Filler.svg (74 lines)
│   │   │       │   ├── A99-SFC2.svg (5176 lines)
│   │   │       │   ├── A99-SFC3.svg (1065 lines)
│   │   │       │   ├── A9903-20HG-PEC.svg (8518 lines)
│   │   │       │   ├── A9903-20HG-PEC_filler.svg (79 lines)
│   │   │       │   ├── A9903-8HG-PEC.svg (10569 lines)
│   │   │       │   ├── A9904-FAN-FILLER.svg (72 lines)
│   │   │       │   ├── A9904-FAN.svg (206 lines)
│   │   │       │   ├── A9904-FILLER-PT.svg (70 lines)
│   │   │       │   ├── A9912-FILLER-LC.svg (76 lines)
│   │   │       │   ├── A9K-16T-8-B.svg (884 lines)
│   │   │       │   ├── A9K-16X100GE-Filler.svg (25 lines)
│   │   │       │   ├── A9K-16X100GE.svg (5021 lines)
│   │   │       │   ├── A9K-1x100GE-SE.svg (2077 lines)
│   │   │       │   ├── A9K-1x100GE-TR.svg (2101 lines)
│   │   │       │   ├── A9K-20HG-FLEX-SE.svg (4403 lines)
│   │   │       │   ├── A9K-20HG-FLEX-TR.svg (4404 lines)
│   │   │       │   ├── A9K-24X10GE-1G-SE.svg (3759 lines)
│   │   │       │   ├── A9K-24X10GE-1G-TR.svg (3805 lines)
│   │   │       │   ├── A9K-24X10GE-1G-TR_Filler.svg (72 lines)
│   │   │       │   ├── A9K-24X10GE-SE.svg (1239 lines)
│   │   │       │   ├── A9K-2T20GE-B.svg (2095 lines)
│   │   │       │   ├── A9K-2T20GE-E.svg (2104 lines)
│   │   │       │   ├── A9K-2T20GE-L.svg (2095 lines)
│   │   │       │   ├── A9K-2X100GE-SE.svg (303 lines)
│   │   │       │   ├── A9K-2X100GE-TR.svg (526 lines)
│   │   │       │   ├── A9K-36X10GE-SE.svg (3672 lines)
│   │   │       │   ├── A9K-3KW-AC.svg (437 lines)
│   │   │       │   ├── A9K-400G-DWDM-TR.svg (2734 lines)
│   │   │       │   ├── A9K-40GE-B.svg (3269 lines)
│   │   │       │   ├── A9K-40GE-E.svg (3260 lines)
│   │   │       │   ├── A9K-40GE-L.svg (3302 lines)
│   │   │       │   ├── A9K-40GE-SE.svg (4926 lines)
│   │   │       │   ├── A9K-40GE-SE_Filler.svg (74 lines)
│   │   │       │   ├── A9K-40GE-TR.svg (4938 lines)
│   │   │       │   ├── A9K-48X10GE-1G-TR.svg (3174 lines)
│   │   │       │   ├── A9K-48X10GE-1G.svg (3168 lines)
│   │   │       │   ├── A9K-4HG-FLEX-X-SE.svg (7299 lines)
│   │   │       │   ├── A9K-4HG-FLEX.svg (8005 lines)
│   │   │       │   ├── A9K-4T-B.svg (360 lines)
│   │   │       │   ├── A9K-4T-E.svg (346 lines)
│   │   │       │   ├── A9K-4T-L.svg (360 lines)
│   │   │       │   ├── A9K-4T16GE-TR.svg (1913 lines)
│   │   │       │   ├── A9K-4X100GE-Filler.svg (63 lines)
│   │   │       │   ├── A9K-4X100GE-SE.svg (2325 lines)
│   │   │       │   ├── A9K-4X100GE-TR.svg (2302 lines)
│   │   │       │   ├── A9K-4X100GE.svg (1326 lines)
│   │   │       │   ├── A9K-750W-AC.svg (203 lines)
│   │   │       │   ├── A9K-750W-DC.svg (310 lines)
│   │   │       │   ├── A9K-8HG-FLEX-SE.svg (5948 lines)
│   │   │       │   ├── A9K-8HG-FLEX-TR.svg (5928 lines)
│   │   │       │   ├── A9K-8T-B.svg (457 lines)
│   │   │       │   ├── A9K-8T-E.svg (457 lines)
│   │   │       │   ├── A9K-8T-L.svg (484 lines)
│   │   │       │   ├── A9K-8T_4-B.svg (457 lines)
│   │   │       │   ├── A9K-8T_4-E.svg (470 lines)
│   │   │       │   ├── A9K-8T_4-L.svg (457 lines)
│   │   │       │   ├── A9K-8X100G-LB-SE.svg (2013 lines)
│   │   │       │   ├── A9K-8X100G-LB-TR.svg (2013 lines)
│   │   │       │   ├── A9K-8X100GE-CM.svg (2014 lines)
│   │   │       │   ├── A9K-8X100GE-L-SE.svg (2038 lines)
│   │   │       │   ├── A9K-8X100GE-SE.svg (2013 lines)
│   │   │       │   ├── A9K-8X100GE-TR.svg (2014 lines)
│   │   │       │   ├── A9K-8X100GE-X-Filler.svg (25 lines)
│   │   │       │   ├── A9K-8X100GE-X.svg (1480 lines)
│   │   │       │   ├── A9K-AC-PEM-V3_PWR.svg (470 lines)
│   │   │       │   ├── A9K-AC-PEM-V3_PWR_Filler.svg (79 lines)
│   │   │       │   ├── A9K-FILLER-LC.svg (130 lines)
│   │   │       │   ├── A9K-FILLER-MPA.svg (92 lines)
│   │   │       │   ├── A9K-FILLER-PT-V2.svg (1606 lines)
│   │   │       │   ├── A9K-FILLER-PT.svg (92 lines)
│   │   │       │   ├── A9K-MOD160-SE.svg (325 lines)
│   │   │       │   ├── A9K-MOD160-TR.svg (389 lines)
│   │   │       │   ├── A9K-MOD200-SE.svg (442 lines)
│   │   │       │   ├── A9K-MOD200-TR.svg (442 lines)
│   │   │       │   ├── A9K-MOD400-SE.svg (442 lines)
│   │   │       │   ├── A9K-MOD400-TR.svg (464 lines)
│   │   │       │   ├── A9K-MOD80-SE.svg (340 lines)
│   │   │       │   ├── A9K-MOD80-TR.svg (479 lines)
│   │   │       │   ├── A9K-MODULEv-FILLER.svg (60 lines)
│   │   │       │   ├── A9K-MODULEv.svg (458 lines)
│   │   │       │   ├── A9K-MPA-1X100GE.svg (554 lines)
│   │   │       │   ├── A9K-MPA-1X200GE.svg (669 lines)
│   │   │       │   ├── A9K-MPA-1X40GE.svg (288 lines)
│   │   │       │   ├── A9K-MPA-20X10GE.svg (930 lines)
│   │   │       │   ├── A9K-MPA-20X1GE.svg (910 lines)
│   │   │       │   ├── A9K-MPA-2X100GE.svg (787 lines)
│   │   │       │   ├── A9K-MPA-2X10GE.svg (501 lines)
│   │   │       │   ├── A9K-MPA-2X40GE.svg (493 lines)
│   │   │       │   ├── A9K-MPA-4X10GE.svg (901 lines)
│   │   │       │   ├── A9K-MPA-8X10GE.svg (392 lines)
│   │   │       │   ├── A9K-Power-Module-V2-Filler.svg (72 lines)
│   │   │       │   ├── A9K-Power-Module-V2.svg (581 lines)
│   │   │       │   ├── A9K-Power-Module.svg (1998 lines)
│   │   │       │   ├── A9K-Power-Tray.svg (483 lines)
│   │   │       │   ├── A9K-RSP-4G.svg (721 lines)
│   │   │       │   ├── A9K-RSP440-SE.svg (1038 lines)
│   │   │       │   ├── A9K-RSP440-TR.svg (1089 lines)
│   │   │       │   ├── A9K-RSP5-SE.svg (1500 lines)
│   │   │       │   ├── A9K-RSP5-TR.svg (1496 lines)
│   │   │       │   ├── A9K-RSP5-X-SE.svg (2524 lines)
│   │   │       │   ├── A9K-RSP5-X-TR.svg (2524 lines)
│   │   │       │   ├── A9K-RSP880-LT.svg (2909 lines)
│   │   │       │   ├── A9K-RSP880-SE.svg (3240 lines)
│   │   │       │   ├── A9K-RSP880-TR.svg (3231 lines)
│   │   │       │   ├── A9K-SIP-700.svg (897 lines)
│   │   │       │   ├── ASR-9000v-AC.svg (357 lines)
│   │   │       │   ├── ASR-9000v-DC.svg (186 lines)
│   │   │       │   ├── ASR-9000v-FT.svg (214 lines)
│   │   │       │   ├── ASR-9000v-LC.svg (2845 lines)
│   │   │       │   ├── ASR-9001-FAN.svg (110 lines)
│   │   │       │   ├── ASR-9006-FAN-V2.svg (500 lines)
│   │   │       │   ├── ASR-9010-FAN.svg (367 lines)
│   │   │       │   ├── ASR-9900-RP-SE.svg (1552 lines)
│   │   │       │   ├── ASR-9900-RP-TR.svg (1542 lines)
│   │   │       │   ├── ASR-9902_front_rspcard.svg (12379 lines)
│   │   │       │   ├── ASR-9902_rear_fan.svg (2500 lines)
│   │   │       │   ├── ASR-9902_rear_fan_filler.svg (84 lines)
│   │   │       │   ├── ASR-9903_LC.svg (9574 lines)
│   │   │       │   ├── ASR-9903_front_card.svg (13677 lines)
│   │   │       │   ├── ASR-9903_rear_fan.svg (2116 lines)
│   │   │       │   ├── ASR-9903_rear_fan_filler.svg (79 lines)
│   │   │       │   ├── ASR-9903_rear_power_module.svg (438 lines)
│   │   │       │   ├── ASR-9903_rear_power_module_filler.svg (73 lines)
│   │   │       │   ├── ASR-9906-FAN.svg (386 lines)
│   │   │       │   ├── ASR-9906-FAN_filler.svg (89 lines)
│   │   │       │   ├── ASR-9906-Front-fan-filler.svg (78 lines)
│   │   │       │   ├── ASR-9906-Front-fan1.svg (331 lines)
│   │   │       │   ├── ASR-9910-FAN.svg (323 lines)
│   │   │       │   ├── ASR-9912-FAN.svg (283 lines)
│   │   │       │   ├── ASR-9912-FILLER.svg (67 lines)
│   │   │       │   ├── ASR-9912-SFC110.svg (2967 lines)
│   │   │       │   ├── ASR-9922-FAN.svg (198 lines)
│   │   │       │   ├── ASR-9922-RP-SE.svg (1541 lines)
│   │   │       │   ├── ASR-9922-RP-TR.svg (2649 lines)
│   │   │       │   ├── ASR-9922-SFC110.svg (6308 lines)
│   │   │       │   ├── ASR9001-FILLER-PM.svg (76 lines)
│   │   │       │   ├── ASR9001-LC.svg (244 lines)
│   │   │       │   ├── ASR9001-RP.svg (1207 lines)
│   │   │       │   ├── ASR9910-FAN-FILLER.svg (75 lines)
│   │   │       │   ├── CFP-100G-ER4.svg (592 lines)
│   │   │       │   ├── CFP-100G-LR4.svg (556 lines)
│   │   │       │   ├── CFP-100G-SR10.svg (335 lines)
│   │   │       │   ├── CPAK.svg (92 lines)
│   │   │       │   ├── Cable-Manager.svg (3607 lines)
│   │   │       │   ├── GLC.svg (190 lines)
│   │   │       │   ├── ONS-CFP2.svg (47 lines)
│   │   │       │   ├── PWR-4.4KW-DC-V3.svg (561 lines)
│   │   │       │   ├── PWR-4.4KW-DC-V3_Filler.svg (93 lines)
│   │   │       │   ├── PWR-6KW-AC-V3-FILLER.svg (74 lines)
│   │   │       │   ├── PWR-6KW-AC-V3.svg (470 lines)
│   │   │       │   ├── PWR-6KW-AC-V3_Filler.svg (93 lines)
│   │   │       │   ├── QSFP.svg (174 lines)
│   │   │       │   ├── SFP.svg (173 lines)
│   │   │       │   ├── asr9000_powertray_v2.svg (399 lines)
│   │   │       │   ├── asr9901-front_mgnt.svg (533 lines)
│   │   │       │   ├── asr9901-front_ports.svg (6048 lines)
│   │   │       │   ├── asr9901-rear_fan.svg (249 lines)
│   │   │       │   └── asr9901-rear_powermodule.svg (256 lines)
│   │   │       └── vertical/
│   │   │           ├── 9922-FILLER-FAN.svg (74 lines)
│   │   │           ├── 9922-FILLER-LC.svg (92 lines)
│   │   │           ├── A9010-FAN-FILLER.svg (86 lines)
│   │   │           ├── A99-10X400GE-X.svg (4181 lines)
│   │   │           ├── A99-12X100GE-CM.svg (4746 lines)
│   │   │           ├── A99-12X100GE-CM_filler.svg (93 lines)
│   │   │           ├── A99-16X100GE-X.svg (10111 lines)
│   │   │           ├── A99-32X100GE-Filler.svg (74 lines)
│   │   │           ├── A99-32X100GE-X-SE.svg (8948 lines)
│   │   │           ├── A99-32X100GE-X-TR.svg (8950 lines)
│   │   │           ├── A99-32X100GE.svg (8950 lines)
│   │   │           ├── A99-48X10GE-1G.svg (4017 lines)
│   │   │           ├── A99-4HG-FLEX-X-SE.svg (7485 lines)
│   │   │           ├── A99-4HG-FLEX.svg (8793 lines)
│   │   │           ├── A99-8X100GE-SE.svg (2051 lines)
│   │   │           ├── A99-8X100GE-TR.svg (2058 lines)
│   │   │           ├── A99-RP-F.svg (1796 lines)
│   │   │           ├── A99-RP2.svg (3222 lines)
│   │   │           ├── A99-RP3-SE.svg (1837 lines)
│   │   │           ├── A99-RP3-TR.svg (1839 lines)
│   │   │           ├── A99-RP3-X-SE.svg (2347 lines)
│   │   │           ├── A99-RP3-X-TR.svg (2340 lines)
│   │   │           ├── A99-RSP-SE-FILLER.svg (75 lines)
│   │   │           ├── A99-RSP-SE.svg (3231 lines)
│   │   │           ├── A99-RSP-TR-FILLER.svg (75 lines)
│   │   │           ├── A99-RSP-TR.svg (3221 lines)
│   │   │           ├── A99-SFC-S-FILLER.svg (75 lines)
│   │   │           ├── A99-SFC-S.svg (1765 lines)
│   │   │           ├── A99-SFC-T.svg (1775 lines)
│   │   │           ├── A99-SFC-T_Filler.svg (79 lines)
│   │   │           ├── A99-SFC2.svg (5186 lines)
│   │   │           ├── A99-SFC3.svg (1358 lines)
│   │   │           ├── A9903-20HG-PEC.svg (8538 lines)
│   │   │           ├── A9904-FAN-FILLER.svg (72 lines)
│   │   │           ├── A9904-FAN.svg (274 lines)
│   │   │           ├── A9904-FILLER-PT.svg (72 lines)
│   │   │           ├── A9912-FILLER-LC.svg (94 lines)
│   │   │           ├── A9K-16T-8-B.svg (884 lines)
│   │   │           ├── A9K-16X100GE-Filler.svg (74 lines)
│   │   │           ├── A9K-16X100GE.svg (5021 lines)
│   │   │           ├── A9K-1x100GE-SE.svg (2089 lines)
│   │   │           ├── A9K-1x100GE-TR.svg (2101 lines)
│   │   │           ├── A9K-20HG-FLEX-SE.svg (4426 lines)
│   │   │           ├── A9K-20HG-FLEX-TR.svg (4427 lines)
│   │   │           ├── A9K-24X10GE-1G-SE.svg (3785 lines)
│   │   │           ├── A9K-24X10GE-1G-TR.svg (3807 lines)
│   │   │           ├── A9K-24X10GE-1G-TR_Filler.svg (79 lines)
│   │   │           ├── A9K-24X10GE-SE.svg (1403 lines)
│   │   │           ├── A9K-2T20GE-B.svg (2427 lines)
│   │   │           ├── A9K-2T20GE-E.svg (2435 lines)
│   │   │           ├── A9K-2T20GE-L.svg (2096 lines)
│   │   │           ├── A9K-2X100GE-SE.svg (303 lines)
│   │   │           ├── A9K-2X100GE-TR.svg (584 lines)
│   │   │           ├── A9K-36X10GE-SE.svg (4002 lines)
│   │   │           ├── A9K-3KW-AC.svg (447 lines)
│   │   │           ├── A9K-400G-DWDM-TR.svg (2711 lines)
│   │   │           ├── A9K-40GE-B.svg (3808 lines)
│   │   │           ├── A9K-40GE-E.svg (3796 lines)
│   │   │           ├── A9K-40GE-L.svg (3824 lines)
│   │   │           ├── A9K-40GE-SE.svg (4994 lines)
│   │   │           ├── A9K-40GE-SE_Filler.svg (79 lines)
│   │   │           ├── A9K-40GE-TR.svg (5004 lines)
│   │   │           ├── A9K-48X10GE-1G-TR.svg (4014 lines)
│   │   │           ├── A9K-48X10GE-1G.svg (4007 lines)
│   │   │           ├── A9K-4HG-FLEX-X-SE.svg (7485 lines)
│   │   │           ├── A9K-4HG-FLEX.svg (8793 lines)
│   │   │           ├── A9K-4T-B.svg (360 lines)
│   │   │           ├── A9K-4T-E.svg (346 lines)
│   │   │           ├── A9K-4T-L.svg (360 lines)
│   │   │           ├── A9K-4T16GE-TR.svg (1914 lines)
│   │   │           ├── A9K-4X100GE-Filler.svg (69 lines)
│   │   │           ├── A9K-4X100GE-SE.svg (2327 lines)
│   │   │           ├── A9K-4X100GE-TR.svg (2317 lines)
│   │   │           ├── A9K-4X100GE.svg (1675 lines)
│   │   │           ├── A9K-8HG-FLEX-SE.svg (6672 lines)
│   │   │           ├── A9K-8HG-FLEX-TR.svg (6677 lines)
│   │   │           ├── A9K-8T-B.svg (457 lines)
│   │   │           ├── A9K-8T-E.svg (457 lines)
│   │   │           ├── A9K-8T-L.svg (484 lines)
│   │   │           ├── A9K-8T_4-B.svg (457 lines)
│   │   │           ├── A9K-8T_4-E.svg (469 lines)
│   │   │           ├── A9K-8T_4-L.svg (457 lines)
│   │   │           ├── A9K-8X100G-LB-SE.svg (2030 lines)
│   │   │           ├── A9K-8X100G-LB-TR.svg (2030 lines)
│   │   │           ├── A9K-8X100GE-CM.svg (2030 lines)
│   │   │           ├── A9K-8X100GE-L-SE.svg (2054 lines)
│   │   │           ├── A9K-8X100GE-SE.svg (2030 lines)
│   │   │           ├── A9K-8X100GE-TR.svg (2030 lines)
│   │   │           ├── A9K-8X100GE-X-Filler.svg (74 lines)
│   │   │           ├── A9K-8X100GE-X.svg (3344 lines)
│   │   │           ├── A9K-AC-PEM-V3_PWR.svg (471 lines)
│   │   │           ├── A9K-AC-PEM-V3_PWR_Filler.svg (82 lines)
│   │   │           ├── A9K-FILLER-LC.svg (130 lines)
│   │   │           ├── A9K-FILLER-MPA.svg (94 lines)
│   │   │           ├── A9K-FILLER-PT-V2.svg (1606 lines)
│   │   │           ├── A9K-FILLER-PT.svg (81 lines)
│   │   │           ├── A9K-MOD160-SE.svg (340 lines)
│   │   │           ├── A9K-MOD160-TR.svg (389 lines)
│   │   │           ├── A9K-MOD200-SE.svg (443 lines)
│   │   │           ├── A9K-MOD200-TR.svg (443 lines)
│   │   │           ├── A9K-MOD400-SE.svg (443 lines)
│   │   │           ├── A9K-MOD400-TR.svg (486 lines)
│   │   │           ├── A9K-MOD80-SE.svg (340 lines)
│   │   │           ├── A9K-MOD80-TR.svg (452 lines)
│   │   │           ├── A9K-MPA-1X100GE.svg (567 lines)
│   │   │           ├── A9K-MPA-1X200GE.svg (679 lines)
│   │   │           ├── A9K-MPA-1X40GE.svg (288 lines)
│   │   │           ├── A9K-MPA-20X10GE.svg (1086 lines)
│   │   │           ├── A9K-MPA-20X1GE.svg (1066 lines)
│   │   │           ├── A9K-MPA-2X100GE.svg (787 lines)
│   │   │           ├── A9K-MPA-2X10GE.svg (495 lines)
│   │   │           ├── A9K-MPA-2X40GE.svg (493 lines)
│   │   │           ├── A9K-MPA-4X10GE.svg (901 lines)
│   │   │           ├── A9K-MPA-8X10GE.svg (438 lines)
│   │   │           ├── A9K-Power-Module-V2-Filler.svg (72 lines)
│   │   │           ├── A9K-Power-Module-V2.svg (581 lines)
│   │   │           ├── A9K-RSP-4G.svg (703 lines)
│   │   │           ├── A9K-RSP440-SE.svg (1038 lines)
│   │   │           ├── A9K-RSP440-TR.svg (1091 lines)
│   │   │           ├── A9K-RSP5-SE.svg (1824 lines)
│   │   │           ├── A9K-RSP5-TR.svg (1820 lines)
│   │   │           ├── A9K-RSP5-X-SE.svg (2622 lines)
│   │   │           ├── A9K-RSP5-X-TR.svg (2622 lines)
│   │   │           ├── A9K-RSP880-LT.svg (2968 lines)
│   │   │           ├── A9K-RSP880-SE.svg (3244 lines)
│   │   │           ├── A9K-RSP880-TR.svg (3235 lines)
│   │   │           ├── A9K-SIP-700.svg (1062 lines)
│   │   │           ├── ASR-9000v-LC.svg (3070 lines)
│   │   │           ├── ASR-9006-FAN-V2.svg (506 lines)
│   │   │           ├── ASR-9010-FAN.svg (367 lines)
│   │   │           ├── ASR-9900-RP-SE.svg (1484 lines)
│   │   │           ├── ASR-9900-RP-TR.svg (1491 lines)
│   │   │           ├── ASR-9903_front_card.svg (14144 lines)
│   │   │           ├── ASR-9903_rear_fan.svg (2116 lines)
│   │   │           ├── ASR-9903_rear_power_module.svg (438 lines)
│   │   │           ├── ASR-9906-FAN.svg (387 lines)
│   │   │           ├── ASR-9906-FAN_filler.svg (89 lines)
│   │   │           ├── ASR-9906-Front-fan-filler.svg (85 lines)
│   │   │           ├── ASR-9906-Front-fan1.svg (330 lines)
│   │   │           ├── ASR-9910-FAN.svg (324 lines)
│   │   │           ├── ASR-9912-FAN.svg (237 lines)
│   │   │           ├── ASR-9912-FILLER.svg (63 lines)
│   │   │           ├── ASR-9912-SFC110.svg (265 lines)
│   │   │           ├── ASR-9922-FAN.svg (198 lines)
│   │   │           ├── ASR-9922-RP-SE.svg (1177 lines)
│   │   │           ├── ASR-9922-RP-TR.svg (3040 lines)
│   │   │           ├── ASR-9922-SFC110.svg (6309 lines)
│   │   │           ├── ASR9001-FILLER-PM.svg (79 lines)
│   │   │           ├── ASR9001-LC.svg (252 lines)
│   │   │           ├── ASR9910-FAN-FILLER.svg (75 lines)
│   │   │           ├── CFP-100G-ER4.svg (593 lines)
│   │   │           ├── CFP-100G-LR4.svg (557 lines)
│   │   │           ├── CFP-100G-SR10.svg (420 lines)
│   │   │           ├── CPAK.svg (108 lines)
│   │   │           ├── GLC.svg (191 lines)
│   │   │           ├── ONS-CFP2.svg (47 lines)
│   │   │           ├── PWR-4.4KW-DC-V3.svg (566 lines)
│   │   │           ├── PWR-4.4KW-DC-V3_Filler.svg (93 lines)
│   │   │           ├── PWR-6KW-AC-V3-FILLER.svg (75 lines)
│   │   │           ├── PWR-6KW-AC-V3.svg (470 lines)
│   │   │           ├── PWR-6KW-AC-V3_Filler.svg (93 lines)
│   │   │           ├── QSFP.svg (184 lines)
│   │   │           ├── SFP.svg (261 lines)
│   │   │           ├── asr9901-front_mgnt.svg (534 lines)
│   │   │           ├── asr9901-front_ports.svg (6174 lines)
│   │   │           ├── asr9901-rear_fan.svg (292 lines)
│   │   │           └── asr9901-rear_powermodule.svg (304 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (85 lines)
│   ├── cat6500/
│   │   ├── Cisco_Catalyst_6500_Virtual_Switching_System/
│   │   │   ├── data/
│   │   │   │   └── Cisco_Catalyst_6500_Virtual_Switching_System.json (146 lines)
│   │   │   └── images/
│   │   │       ├── C6504-E_Rear_core.svg (24406 lines)
│   │   │       └── WS-C6504-E_Front.svg (475 lines)
│   │   ├── Cisco_Catalyst_6504-E_Switch/
│   │   │   ├── data/
│   │   │   │   └── Cisco_Catalyst_6504-E_Switch.json (110 lines)
│   │   │   └── images/
│   │   │       ├── C6504-E_Rear_core.svg (24406 lines)
│   │   │       └── WS-C6504-E_Front.svg (475 lines)
│   │   ├── Cisco_Catalyst_6509_Switch/
│   │   │   ├── data/
│   │   │   │   └── Cisco_Catalyst_6509_Switch.json (118 lines)
│   │   │   └── images/
│   │   │       └── WS-C6509-E-core.svg (1373 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (791 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (3301 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── C6504-E_PWR-2700-AC4.svg (1075 lines)
│   │   │       │   ├── C6504-E_PWR-2700-AC4_filler.svg (78 lines)
│   │   │       │   ├── C6509-E-FAN-filler.svg (90 lines)
│   │   │       │   ├── C6509-E-FAN.svg (9532 lines)
│   │   │       │   ├── FAN-MOD-4HS-FILLER.svg (73 lines)
│   │   │       │   ├── FAN-MOD-4HS.svg (3338 lines)
│   │   │       │   ├── VS-S720-10G-3CXL-filler.svg (85 lines)
│   │   │       │   ├── VS-S720-10G-3CXL.svg (5082 lines)
│   │   │       │   ├── VS-SUP2T-10G-Filler.svg (73 lines)
│   │   │       │   ├── VS-SUP2T-10G.svg (3524 lines)
│   │   │       │   ├── WS-CAC-6000W=.svg (3435 lines)
│   │   │       │   ├── WS-CAC-6000W=_filler.svg (85 lines)
│   │   │       │   ├── WS-SUP720-3BXL.svg (3701 lines)
│   │   │       │   ├── WS-SVC-FWM-1.svg (2422 lines)
│   │   │       │   ├── WS-SVC-WISM-1-K9.svg (3177 lines)
│   │   │       │   ├── WS-X6148E-GE-45AT.svg (6029 lines)
│   │   │       │   ├── WS-X6704-10GE.svg (2627 lines)
│   │   │       │   ├── WS-X6704-10GE_filler.svg (85 lines)
│   │   │       │   ├── WS-X6704-10GE_port_filler.svg (165 lines)
│   │   │       │   ├── WS-X6708-10G-3C-filler.svg (85 lines)
│   │   │       │   ├── WS-X6708-10G-3C.svg (3792 lines)
│   │   │       │   ├── WS-X6716-10GE.svg (3117 lines)
│   │   │       │   ├── WS-X6716-10GE_plug.svg (287 lines)
│   │   │       │   ├── WS-X6904-40G-2T-filler.svg (85 lines)
│   │   │       │   ├── WS-X6904-40G-2T.svg (9132 lines)
│   │   │       │   ├── WS-X6908-10G.svg (3732 lines)
│   │   │       │   └── X2.svg (287 lines)
│   │   │       └── vertical/
│   │   │           ├── C6509-E-FAN-filler.svg (85 lines)
│   │   │           ├── C6509-E-FAN.svg (9510 lines)
│   │   │           ├── FAN-MOD-4HS-FILLER.svg (73 lines)
│   │   │           ├── FAN-MOD-4HS.svg (3338 lines)
│   │   │           ├── VS-S720-10G-3CXL-filler.svg (90 lines)
│   │   │           ├── VS-S720-10G-3CXL.svg (5141 lines)
│   │   │           ├── VS-SUP2T-10G-Filler.svg (78 lines)
│   │   │           ├── VS-SUP2T-10G.svg (3547 lines)
│   │   │           ├── WS-SUP720-3BXL.svg (3712 lines)
│   │   │           ├── WS-SVC-FWM-1.svg (2439 lines)
│   │   │           ├── WS-SVC-WISM-1-K9.svg (3204 lines)
│   │   │           ├── WS-X6148E-GE-45AT.svg (6081 lines)
│   │   │           ├── WS-X6704-10GE.svg (2650 lines)
│   │   │           ├── WS-X6704-10GE_filler.svg (90 lines)
│   │   │           ├── WS-X6704-10GE_port_filler.svg (172 lines)
│   │   │           ├── WS-X6708-10G-3C-filler.svg (90 lines)
│   │   │           ├── WS-X6708-10G-3C.svg (3805 lines)
│   │   │           ├── WS-X6716-10GE.svg (3164 lines)
│   │   │           ├── WS-X6716-10GE_plug.svg (294 lines)
│   │   │           ├── WS-X6904-40G-2T-filler.svg (90 lines)
│   │   │           ├── WS-X6904-40G-2T.svg (9236 lines)
│   │   │           └── X2.svg (293 lines)
│   │   ├── assembly.xml (25 lines)
│   │   └── pom.xml (84 lines)
│   ├── cbr/
│   │   ├── Cisco_cBR-8_Converged_Broadband_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_cBR-8_Converged_Broadband_Router.json (285 lines)
│   │   │   └── images/
│   │   │       ├── CBR-8-CCAP-CHASS-Front.svg (1780 lines)
│   │   │       └── CBR-8-CCAP-CHASS-Rear.svg (603 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (489 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (1373 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── CBR-2X100G-PIC.svg (3112 lines)
│   │   │       │   ├── CBR-CCAP-LC-40G.svg (1360 lines)
│   │   │       │   ├── CBR-CCAP-LC-G2-R.svg (1477 lines)
│   │   │       │   ├── CBR-CCAP-SUP-160G.svg (2466 lines)
│   │   │       │   ├── CBR-DC-PS.svg (599 lines)
│   │   │       │   ├── CBR-DPIC-2X100G.svg (1941 lines)
│   │   │       │   ├── CBR-DPIC-8X10G.svg (1941 lines)
│   │   │       │   ├── CBR-FAN-ASSEMBLY-FILLER.svg (87 lines)
│   │   │       │   ├── CBR-FAN-ASSEMBLY.svg (2362 lines)
│   │   │       │   ├── CBR-LC-BLANK.svg (1177 lines)
│   │   │       │   ├── CBR-LC-PIC-BLANK.svg (183 lines)
│   │   │       │   ├── CBR-PEM-AC-6M.svg (18185 lines)
│   │   │       │   ├── CBR-PEM-DC-6M.svg (23227 lines)
│   │   │       │   ├── CBR-PS-BLANK.svg (82 lines)
│   │   │       │   ├── CBR-RF-PIC.svg (2854 lines)
│   │   │       │   ├── CBR-RF-PROT-PIC.svg (1266 lines)
│   │   │       │   ├── CBR-SUP-250G.svg (2447 lines)
│   │   │       │   ├── CBR-SUP-8X10G-PIC.svg (3005 lines)
│   │   │       │   ├── CBR-SUP-BLANK.svg (2109 lines)
│   │   │       │   ├── CBR-SUP-PIC-BLANK.svg (295 lines)
│   │   │       │   ├── QSFP-5.svg (201 lines)
│   │   │       │   ├── QSFP.svg (174 lines)
│   │   │       │   └── SFP.svg (173 lines)
│   │   │       └── vertical/
│   │   │           ├── CBR-2X100G-PIC.svg (3169 lines)
│   │   │           ├── CBR-CCAP-LC-40G.svg (1363 lines)
│   │   │           ├── CBR-CCAP-LC-G2-R.svg (2632 lines)
│   │   │           ├── CBR-CCAP-SUP-160G.svg (2490 lines)
│   │   │           ├── CBR-DC-PS.svg (604 lines)
│   │   │           ├── CBR-DPIC-2X100G.svg (1958 lines)
│   │   │           ├── CBR-DPIC-8X10G.svg (1958 lines)
│   │   │           ├── CBR-FAN-ASSEMBLY-FILLER.svg (90 lines)
│   │   │           ├── CBR-FAN-ASSEMBLY.svg (2365 lines)
│   │   │           ├── CBR-LC-BLANK.svg (1180 lines)
│   │   │           ├── CBR-LC-PIC-BLANK.svg (183 lines)
│   │   │           ├── CBR-PEM-AC-6M.svg (18368 lines)
│   │   │           ├── CBR-PEM-DC-6M.svg (23269 lines)
│   │   │           ├── CBR-PS-BLANK.svg (82 lines)
│   │   │           ├── CBR-RF-PIC.svg (2868 lines)
│   │   │           ├── CBR-RF-PROT-PIC.svg (1278 lines)
│   │   │           ├── CBR-SUP-250G.svg (2449 lines)
│   │   │           ├── CBR-SUP-8X10G-PIC.svg (3080 lines)
│   │   │           ├── CBR-SUP-BLANK.svg (2116 lines)
│   │   │           ├── CBR-SUP-PIC-BLANK.svg (295 lines)
│   │   │           ├── QSFP-5.svg (218 lines)
│   │   │           ├── QSFP.svg (174 lines)
│   │   │           └── SFP.svg (261 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (76 lines)
│   │   └── pom.xml (84 lines)
│   ├── chassisview/
│   │   ├── data/
│   │   │   ├── 172.25.123.219-bosshogg/
│   │   │   │   └── webacs/
│   │   │   │       └── rs/
│   │   │   │           └── chassis/
│   │   │   │               └── chassisview/
│   │   │   │                   └── v2/
│   │   │   │                       ├── device/
│   │   │   │                       │   ├── 10.58.235.69/
│   │   │   │                       │   │   ├── equipments/
│   │   │   │                       │   │   │   └── alarm (1 lines)
│   │   │   │                       │   │   └── ports/
│   │   │   │                       │   │       └── alarm (1 lines)
│   │   │   │                       │   ├── 8789803/
│   │   │   │                       │   │   ├── chassisview/
│   │   │   │                       │   │   │   ├── 0 (1 lines)
│   │   │   │                       │   │   │   ├── 336711399 (1 lines)
│   │   │   │                       │   │   │   ├── 336711421 (1 lines)
│   │   │   │                       │   │   │   ├── 336711428 (1 lines)
│   │   │   │                       │   │   │   ├── 336711430 (1 lines)
│   │   │   │                       │   │   │   ├── 336711432 (1 lines)
│   │   │   │                       │   │   │   ├── 336711445 (1 lines)
│   │   │   │                       │   │   │   ├── 336711455 (1 lines)
│   │   │   │                       │   │   │   ├── 336711456 (1 lines)
│   │   │   │                       │   │   │   ├── 336711461 (1 lines)
│   │   │   │                       │   │   │   ├── 336711477 (1 lines)
│   │   │   │                       │   │   │   ├── 336711479 (1 lines)
│   │   │   │                       │   │   │   ├── 336711485 (1 lines)
│   │   │   │                       │   │   │   ├── 336711492 (1 lines)
│   │   │   │                       │   │   │   └── 336711497 (1 lines)
│   │   │   │                       │   │   ├── chassisexplorer (1 lines)
│   │   │   │                       │   │   ├── getConbinedSVGs (1 lines)
│   │   │   │                       │   │   └── metadata (25735 lines)
│   │   │   │                       │   └── 8789804/
│   │   │   │                       │       ├── chassisview/
│   │   │   │                       │       │   ├── 0 (1 lines)
│   │   │   │                       │       │   └── 9036772 (1 lines)
│   │   │   │                       │       ├── chassisexplorer (1 lines)
│   │   │   │                       │       ├── getConbinedSVGs (1 lines)
│   │   │   │                       │       └── metadata (3007 lines)
│   │   │   │                       ├── equipments/
│   │   │   │                       │   └── state (1 lines)
│   │   │   │                       └── ports/
│   │   │   │                           └── state (1 lines)
│   │   │   └── cv-mock-device-config.json (9 lines)
│   │   ├── js/
│   │   │   ├── ChassisViewMetaData.js (67 lines)
│   │   │   └── ChassisViewMetaDataV2.js (22 lines)
│   │   ├── mockui/
│   │   │   ├── data/
│   │   │   │   └── sample.json (168 lines)
│   │   │   └── html/
│   │   │       └── DeviceList.html (762 lines)
│   │   ├── assembly.xml (22 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── crs/
│   │   ├── Cisco_CRS-1_16-Slot_Line_Card_Chassis/
│   │   │   ├── data/
│   │   │   │   └── Cisco_CRS-1_16-Slot_Line_Card_Chassis.json (533 lines)
│   │   │   └── images/
│   │   │       ├── CRS-16-Front_core.svg (6308 lines)
│   │   │       └── CRS-16-Rear_core.svg (13701 lines)
│   │   ├── Cisco_CRS-1_8-Slot_Single-Shelf_System/
│   │   │   ├── data/
│   │   │   │   └── Cisco_CRS-1_8-Slot_Single-Shelf_System.json (230 lines)
│   │   │   └── images/
│   │   │       ├── CRS-1_8-core.svg (6367 lines)
│   │   │       └── CRS-1_8-rear_core.svg (2815 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (504 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (543 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── 40X10GE-WLO.svg (11495 lines)
│   │   │       │   ├── 40X10GE-WLO_filler.svg (79 lines)
│   │   │       │   ├── CRS-16-ALARM-B.svg (2234 lines)
│   │   │       │   ├── CRS-16-ALARM-B_filler.svg (90 lines)
│   │   │       │   ├── CRS-16-FAN-CT.svg (3274 lines)
│   │   │       │   ├── CRS-16-FAN-CT_Filler.svg (93 lines)
│   │   │       │   ├── CRS-16-FANTRAY.svg (1690 lines)
│   │   │       │   ├── CRS-16-FANTRAY_filler.svg (89 lines)
│   │   │       │   ├── CRS-16-FC-S.svg (2829 lines)
│   │   │       │   ├── CRS-16-FC-S_Filler.svg (93 lines)
│   │   │       │   ├── CRS-16-FC400_M.svg (2829 lines)
│   │   │       │   ├── CRS-16-FC400_M_Filler.svg (93 lines)
│   │   │       │   ├── CRS-16-LCC-FAN-CT.svg (3286 lines)
│   │   │       │   ├── CRS-16-LCC-FAN-CT_Filler.svg (93 lines)
│   │   │       │   ├── CRS-16-LCC-FAN-TR.svg (1137 lines)
│   │   │       │   ├── CRS-16-LCC-FAN-TR_filler.svg (89 lines)
│   │   │       │   ├── CRS-16-PRP-12G.svg (4996 lines)
│   │   │       │   ├── CRS-1_8-front_AC.svg (3189 lines)
│   │   │       │   ├── CRS-1_8-front_powersystem.svg (631 lines)
│   │   │       │   ├── CRS-1_8-rear_dc.svg (5883 lines)
│   │   │       │   ├── CRS-8-FC.svg (2800 lines)
│   │   │       │   ├── CRS-8-RP.svg (6105 lines)
│   │   │       │   ├── CRS-CGSE-PLIM.svg (2739 lines)
│   │   │       │   ├── CRS-FP40.svg (2928 lines)
│   │   │       │   ├── CRS-MSC-X.svg (3006 lines)
│   │   │       │   ├── CRS-PM-AC.svg (765 lines)
│   │   │       │   └── CRS-PM-AC_filler.svg (89 lines)
│   │   │       └── vertical/
│   │   │           ├── 40X10GE-WLO.svg (11515 lines)
│   │   │           ├── 40X10GE-WLO_filler.svg (78 lines)
│   │   │           ├── CRS-16-ALARM-B.svg (2233 lines)
│   │   │           ├── CRS-16-ALARM-B_filler.svg (89 lines)
│   │   │           ├── CRS-16-FAN-CT.svg (3268 lines)
│   │   │           ├── CRS-16-FAN-CT_Filler.svg (92 lines)
│   │   │           ├── CRS-16-FANTRAY.svg (1690 lines)
│   │   │           ├── CRS-16-FANTRAY_filler.svg (90 lines)
│   │   │           ├── CRS-16-FC-S.svg (2815 lines)
│   │   │           ├── CRS-16-FC-S_Filler.svg (92 lines)
│   │   │           ├── CRS-16-FC400_M.svg (2815 lines)
│   │   │           ├── CRS-16-FC400_M_Filler.svg (92 lines)
│   │   │           ├── CRS-16-LCC-FAN-CT.svg (3278 lines)
│   │   │           ├── CRS-16-LCC-FAN-CT_Filler.svg (92 lines)
│   │   │           ├── CRS-16-LCC-FAN-TR.svg (1137 lines)
│   │   │           ├── CRS-16-LCC-FAN-TR_filler.svg (90 lines)
│   │   │           ├── CRS-16-LC_Filler.svg (93 lines)
│   │   │           ├── CRS-16-PRP-12G.svg (4968 lines)
│   │   │           ├── CRS-16-PRP-12G_filler.svg (78 lines)
│   │   │           ├── CRS-16-RP_Filler.svg (64 lines)
│   │   │           ├── CRS-16-Rear_Filler.svg (27 lines)
│   │   │           ├── CRS-1_8-front_AC.svg (3168 lines)
│   │   │           ├── CRS-1_8-front_powersystem.svg (616 lines)
│   │   │           ├── CRS-1_8-rear_dc.svg (5868 lines)
│   │   │           ├── CRS-8-FC.svg (2800 lines)
│   │   │           ├── CRS-8-FC_Filler.svg (94 lines)
│   │   │           ├── CRS-8-RP.svg (6061 lines)
│   │   │           ├── CRS-CGSE-PLIM.svg (2738 lines)
│   │   │           ├── CRS-FP40.svg (2927 lines)
│   │   │           ├── CRS-MSC-X.svg (3005 lines)
│   │   │           ├── CRS-MSC-X_vertical_Filler.svg (27 lines)
│   │   │           ├── CRS-PM-AC.svg (766 lines)
│   │   │           └── CRS-PM-AC_filler.svg (90 lines)
│   │   ├── assembly.xml (24 lines)
│   │   └── pom.xml (84 lines)
│   ├── jsonTest/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   └── java/
│   │   │   │       └── com/
│   │   │   │           └── cisco/
│   │   │   │               └── nms/
│   │   │   │                   └── resource/
│   │   │   │                       └── Utility.java (68 lines)
│   │   │   └── test/
│   │   │       └── java/
│   │   │           └── com/
│   │   │               └── cisco/
│   │   │                   └── nms/
│   │   │                       ├── TestFileName.java (81 lines)
│   │   │                       ├── TestJson.java (116 lines)
│   │   │                       └── Utility.java (122 lines)
│   │   ├── .classpath (22 lines)
│   │   ├── .project (23 lines)
│   │   └── pom.xml (64 lines)
│   ├── me1200/
│   │   ├── Cisco_ME_1200-4S-A_Ethernet_Access_Device/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ME_1200-4S-A_Ethernet_Access_Device.json (131 lines)
│   │   │   └── images/
│   │   │       ├── ME1200-4S-A.svg (1148 lines)
│   │   │       └── ME1200-4S-D.svg (1904 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (474 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (44 lines)
│   │   │   └── images/
│   │   │       └── horizontal/
│   │   │           └── ME1200-4S-A-ports.svg (1509 lines)
│   │   ├── assembly.xml (24 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs1k/
│   │   ├── Cisco_NCS_1001/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_1001.json (170 lines)
│   │   │   └── images/
│   │   │       ├── NCS1001-K9-Front-FILLER.svg (74 lines)
│   │   │       ├── NCS1001-K9-Front.svg (158 lines)
│   │   │       ├── NCS1001-K9-Rear-FILLER.svg (74 lines)
│   │   │       └── NCS1001-K9-Rear.svg (563 lines)
│   │   ├── Cisco_NCS_1002/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_1002.json (140 lines)
│   │   │   └── images/
│   │   │       ├── NCS1002-K9-Front.svg (13265 lines)
│   │   │       └── NCS1002-K9-Rear.svg (803 lines)
│   │   ├── Cisco_NCS_1004/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_1004.json (144 lines)
│   │   │   └── images/
│   │   │       ├── ncs1004_front_core.svg (328 lines)
│   │   │       └── ncs1004_rear_core.svg (123 lines)
│   │   ├── LS-2520/
│   │   │   ├── data/
│   │   │   │   └── LS-2520.json (0 lines)
│   │   │   └── images/
│   │   │       ├── LS-2520_Front.svg (8895 lines)
│   │   │       └── LS-2520_Rear.svg (1125 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (971 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (3914 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── NCS1001-K9-CNTLR.svg (1129 lines)
│   │   │       │   ├── NCS1001-K9-Rear-AC-FILLER.svg (74 lines)
│   │   │       │   ├── NCS1001-K9-Rear-AC.svg (454 lines)
│   │   │       │   ├── NCS1001-K9-Rear-FAN-FILLER.svg (74 lines)
│   │   │       │   ├── NCS1001-K9-Rear-FAN.svg (109 lines)
│   │   │       │   ├── NCS1002-K9-LC.svg (6104 lines)
│   │   │       │   ├── NCS1002-K9-RSP.svg (186 lines)
│   │   │       │   ├── NCS1002-K9-Rear-RSP.svg (409 lines)
│   │   │       │   ├── NCS1004_LINECARD_FILLER.svg (79 lines)
│   │   │       │   ├── NCS1004_REAR_FAN.svg (5293 lines)
│   │   │       │   ├── NCS1004_REAR_FAN_Filler.svg (77 lines)
│   │   │       │   ├── NCS1004_REAR_POWERMODULE.svg (227 lines)
│   │   │       │   ├── NCS1004_REAR_POWERMODULE_Filler.svg (79 lines)
│   │   │       │   ├── NCS1K-2KW-AC.svg (339 lines)
│   │   │       │   ├── NCS1K-2KW-DC.svg (411 lines)
│   │   │       │   ├── NCS1K-EDFA.svg (1906 lines)
│   │   │       │   ├── NCS1K-FTA-FILLER.svg (105 lines)
│   │   │       │   ├── NCS1K-FTA.svg (3087 lines)
│   │   │       │   ├── NCS1K-OTDR.svg (3378 lines)
│   │   │       │   ├── NCS1K-PSM-FILLER.svg (72 lines)
│   │   │       │   ├── NCS1K-PSM.svg (1283 lines)
│   │   │       │   ├── NCS1K-PWR-FILLER.svg (59 lines)
│   │   │       │   ├── NCS1K4-1.2T-K9.svg (1544 lines)
│   │   │       │   ├── NCS1K4-2-QDD-C.svg (3986 lines)
│   │   │       │   ├── NCS1K4-OTN-XP.svg (1897 lines)
│   │   │       │   ├── NCS1K4-OTN-XP_filler.svg (81 lines)
│   │   │       │   ├── NCS1K4-QXP-K9.svg (7942 lines)
│   │   │       │   ├── ONS-CFP2.svg (135 lines)
│   │   │       │   ├── QSFP.svg (190 lines)
│   │   │       │   ├── SFP.svg (173 lines)
│   │   │       │   └── ncs1004_RSP.svg (1475 lines)
│   │   │       └── vertical/
│   │   │           ├── NCS1001-K9-CNTLR.svg (1129 lines)
│   │   │           ├── NCS1001-K9-Rear-AC-FILLER.svg (75 lines)
│   │   │           ├── NCS1001-K9-Rear-AC.svg (455 lines)
│   │   │           ├── NCS1001-K9-Rear-FAN-FILLER.svg (75 lines)
│   │   │           ├── NCS1001-K9-Rear-FAN.svg (110 lines)
│   │   │           ├── NCS1002-K9-RSP.svg (187 lines)
│   │   │           ├── NCS1004_LINECARD_FILLER.svg (79 lines)
│   │   │           ├── NCS1004_REAR_FAN.svg (5317 lines)
│   │   │           ├── NCS1004_REAR_FAN_Filler.svg (79 lines)
│   │   │           ├── NCS1004_REAR_POWERMODULE.svg (227 lines)
│   │   │           ├── NCS1004_REAR_POWERMODULE_Filler.svg (79 lines)
│   │   │           ├── NCS1K-2KW-AC.svg (348 lines)
│   │   │           ├── NCS1K-2KW-DC.svg (418 lines)
│   │   │           ├── NCS1K-EDFA.svg (1900 lines)
│   │   │           ├── NCS1K-FTA-FILLER.svg (115 lines)
│   │   │           ├── NCS1K-FTA.svg (3088 lines)
│   │   │           ├── NCS1K-OTDR.svg (3385 lines)
│   │   │           ├── NCS1K-PSM-FILLER.svg (75 lines)
│   │   │           ├── NCS1K-PSM.svg (1278 lines)
│   │   │           ├── NCS1K-PWR-FILLER.svg (59 lines)
│   │   │           ├── SFP.svg (177 lines)
│   │   │           ├── ncs1004_RSP.svg (1418 lines)
│   │   │           └── ncs1004_RSP_filler.svg (75 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (76 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs2k/
│   │   ├── Cisco_NCS_2002/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_2002.json (68 lines)
│   │   │   └── images/
│   │   │       └── NCS2002-SA.svg (591 lines)
│   │   ├── Cisco_NCS_2006/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_2006.json (117 lines)
│   │   │   └── images/
│   │   │       └── NCS2006-SA.svg (2117 lines)
│   │   ├── Cisco_NCS_2015/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_2015.json (200 lines)
│   │   │   └── images/
│   │   │       └── NCS2015-SA.svg (7836 lines)
│   │   ├── Cisco_ONS_15454/
│   │   │   ├── data/
│   │   │   │   └── Cisco_ONS_15454.json (467 lines)
│   │   │   └── images/
│   │   │       ├── 15454-M2-Front.svg (709 lines)
│   │   │       ├── 15454-M6-Front.svg (568 lines)
│   │   │       ├── 15454-SA-ANSI-SA-HD.svg (814 lines)
│   │   │       └── 15454E-SA-ETSI.svg (921 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (483 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (27094 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── 15216-EF-40-EVEN.svg (9483 lines)
│   │   │       │   ├── 15216-EF-40-ODD.svg (9403 lines)
│   │   │       │   ├── 15216-FLD-OSC.svg (1501 lines)
│   │   │       │   ├── 15216-FLD4.svg (1269 lines)
│   │   │       │   ├── 15216-MD-40-EVEN.svg (10192 lines)
│   │   │       │   ├── 15216-MD-40-ODD.svg (6651 lines)
│   │   │       │   ├── 15216-MD-48-CM-FILLER.svg (130 lines)
│   │   │       │   ├── 15216-MD-48-CM.svg (563 lines)
│   │   │       │   ├── 15216-MD-48-EVEN.svg (10363 lines)
│   │   │       │   ├── 15216-MD-48-ODD.svg (10269 lines)
│   │   │       │   ├── 15454-10DME-C.svg (1119 lines)
│   │   │       │   ├── 15454-10E-L1.svg (877 lines)
│   │   │       │   ├── 15454-10GE-XP.svg (2849 lines)
│   │   │       │   ├── 15454-10ME-L1-C.svg (1340 lines)
│   │   │       │   ├── 15454-32-DMX.svg (1828 lines)
│   │   │       │   ├── 15454-32-MUX-O.svg (1977 lines)
│   │   │       │   ├── 15454-32-WSS.svg (2608 lines)
│   │   │       │   ├── 15454-40-DMX-C.svg (1972 lines)
│   │   │       │   ├── 15454-40-MUX-C.svg (2072 lines)
│   │   │       │   ├── 15454-40-SMR1-C.svg (3532 lines)
│   │   │       │   ├── 15454-40-SMR2-C.svg (3189 lines)
│   │   │       │   ├── 15454-40-WSS-C.svg (1280 lines)
│   │   │       │   ├── 15454-40-WXC-C.svg (2054 lines)
│   │   │       │   ├── 15454-40E-MXP-C.svg (2391 lines)
│   │   │       │   ├── 15454-40E-TXP-C.svg (676 lines)
│   │   │       │   ├── 15454-40EX-MXP-C.svg (2391 lines)
│   │   │       │   ├── 15454-40ME-MXP-C.svg (2391 lines)
│   │   │       │   ├── 15454-80-WXC-C.svg (4481 lines)
│   │   │       │   ├── 15454-AD-1C.svg (753 lines)
│   │   │       │   ├── 15454-AD-2C.svg (858 lines)
│   │   │       │   ├── 15454-AD-4C.svg (1104 lines)
│   │   │       │   ├── 15454-ADM-10G.svg (5391 lines)
│   │   │       │   ├── 15454-AR-XP.svg (2623 lines)
│   │   │       │   ├── 15454-BLANK.svg (357 lines)
│   │   │       │   ├── 15454-DM-L1-XX.svg (1441 lines)
│   │   │       │   ├── 15454-DMP-L1-XX.svg (1701 lines)
│   │   │       │   ├── 15454-FBR-STRG.svg (358 lines)
│   │   │       │   ├── 15454-FILLER-LCD.svg (106 lines)
│   │   │       │   ├── 15454-FTA-3T.svg (364 lines)
│   │   │       │   ├── 15454-FTA-3T_FILLER.svg (83 lines)
│   │   │       │   ├── 15454-GE-XP.svg (2265 lines)
│   │   │       │   ├── 15454-M-100G-LC-C.svg (652 lines)
│   │   │       │   ├── 15454-M-100G-ME-C.svg (585 lines)
│   │   │       │   ├── 15454-M-100ME-CK-C.svg (4905 lines)
│   │   │       │   ├── 15454-M-10X10G-LC.svg (1838 lines)
│   │   │       │   ├── 15454-M-CFP-LC.svg (829 lines)
│   │   │       │   ├── 15454-M-RAMAN-COP.svg (1123 lines)
│   │   │       │   ├── 15454-M-RAMAN-CTP.svg (2449 lines)
│   │   │       │   ├── 15454-M-TNC-K9.svg (3515 lines)
│   │   │       │   ├── 15454-M-TNCE-K9.svg (3469 lines)
│   │   │       │   ├── 15454-M-TSC-K9.svg (1408 lines)
│   │   │       │   ├── 15454-M-TSCE-K9.svg (1408 lines)
│   │   │       │   ├── 15454-M-WSE-K9.svg (3477 lines)
│   │   │       │   ├── 15454-M2-AC.svg (682 lines)
│   │   │       │   ├── 15454-M2-DC.svg (772 lines)
│   │   │       │   ├── 15454-M2-FILLER-FAN.svg (71 lines)
│   │   │       │   ├── 15454-M2-FTA.svg (308 lines)
│   │   │       │   ├── 15454-M2-Front.svg (570 lines)
│   │   │       │   ├── 15454-M6-AC.svg (824 lines)
│   │   │       │   ├── 15454-M6-AC2.svg (817 lines)
│   │   │       │   ├── 15454-M6-DC.svg (538 lines)
│   │   │       │   ├── 15454-M6-ECU-60.svg (1515 lines)
│   │   │       │   ├── 15454-M6-ECU-S.svg (3459 lines)
│   │   │       │   ├── 15454-M6-ECU.svg (1666 lines)
│   │   │       │   ├── 15454-M6-ECU2.svg (1699 lines)
│   │   │       │   ├── 15454-M6-FILLER-ECU.svg (157 lines)
│   │   │       │   ├── 15454-M6-FILLER-FTA.svg (70 lines)
│   │   │       │   ├── 15454-M6-FTA.svg (348 lines)
│   │   │       │   ├── 15454-M6-Front.svg (782 lines)
│   │   │       │   ├── 15454-M6-LCD.svg (401 lines)
│   │   │       │   ├── 15454-MR-L1.svg (673 lines)
│   │   │       │   ├── 15454-MRP-L1.svg (793 lines)
│   │   │       │   ├── 15454-OPT-AMP-17C.svg (1777 lines)
│   │   │       │   ├── 15454-OPT-AMP-C.svg (2662 lines)
│   │   │       │   ├── 15454-OPT-BST-E.svg (2311 lines)
│   │   │       │   ├── 15454-OPT-BST.svg (2303 lines)
│   │   │       │   ├── 15454-OPT-EDFA-17.svg (2423 lines)
│   │   │       │   ├── 15454-OPT-EDFA-24.svg (2408 lines)
│   │   │       │   ├── 15454-OPT-PRE.svg (1907 lines)
│   │   │       │   ├── 15454-OPT-RAMP-C.svg (952 lines)
│   │   │       │   ├── 15454-OPT-RAMP-CE.svg (930 lines)
│   │   │       │   ├── 15454-OSC-CSM.svg (779 lines)
│   │   │       │   ├── 15454-OSCM.svg (1391 lines)
│   │   │       │   ├── 15454-OTU2-XP.svg (1073 lines)
│   │   │       │   ├── 15454-PP-4-SMR.svg (4180 lines)
│   │   │       │   ├── 15454-PP-MESH-4.svg (4876 lines)
│   │   │       │   ├── 15454-PP-MESH-8.svg (7678 lines)
│   │   │       │   ├── 15454-PSM.svg (1673 lines)
│   │   │       │   ├── 15454-SA-ANSI-SA-HD.svg (458 lines)
│   │   │       │   ├── 15454-TDC-CC.svg (806 lines)
│   │   │       │   ├── 15454-TDC-FC.svg (747 lines)
│   │   │       │   ├── 15454-YCBL-LC.svg (206 lines)
│   │   │       │   ├── 15454E-SA-ETSI.svg (564 lines)
│   │   │       │   ├── 15454E-TCC2.svg (1283 lines)
│   │   │       │   ├── 15454E-TCC3-K9.svg (1326 lines)
│   │   │       │   ├── 15454E-TCCP.svg (1294 lines)
│   │   │       │   ├── 15454W-TNCS-K9.svg (3469 lines)
│   │   │       │   ├── CPAK.svg (126 lines)
│   │   │       │   ├── MF-6RU.svg (8151 lines)
│   │   │       │   ├── MF10-6RU.svg (1080 lines)
│   │   │       │   ├── MPO-16.svg (348 lines)
│   │   │       │   ├── MPO-16V.svg (350 lines)
│   │   │       │   ├── MPO-24.svg (478 lines)
│   │   │       │   ├── MPO-8.svg (222 lines)
│   │   │       │   ├── MPO-8V.svg (222 lines)
│   │   │       │   ├── NCS2002-AC.svg (1190 lines)
│   │   │       │   ├── NCS2002-DC.svg (1304 lines)
│   │   │       │   ├── NCS2002-DC2-Power_Module.svg (171 lines)
│   │   │       │   ├── NCS2002-DC2-Power_Module_Filler.svg (68 lines)
│   │   │       │   ├── NCS2002-DC2_Core.svg (618 lines)
│   │   │       │   ├── NCS2002-FILLER-FTA.svg (70 lines)
│   │   │       │   ├── NCS2002-FILLER-PSU.svg (70 lines)
│   │   │       │   ├── NCS2002-FTA.svg (679 lines)
│   │   │       │   ├── NCS2002-SA-DC.svg (1421 lines)
│   │   │       │   ├── NCS2002-SA.svg (921 lines)
│   │   │       │   ├── NCS2006-AC.svg (690 lines)
│   │   │       │   ├── NCS2006-DC.svg (689 lines)
│   │   │       │   ├── NCS2006-ECU-60.svg (1515 lines)
│   │   │       │   ├── NCS2006-ECU-S.svg (3211 lines)
│   │   │       │   ├── NCS2006-ECU.svg (1666 lines)
│   │   │       │   ├── NCS2006-FILLER-DC.svg (70 lines)
│   │   │       │   ├── NCS2006-FILLER-ECU.svg (157 lines)
│   │   │       │   ├── NCS2006-FILLER-FTA.svg (70 lines)
│   │   │       │   ├── NCS2006-FILLER-LCD.svg (106 lines)
│   │   │       │   ├── NCS2006-FILLER-PSU.svg (70 lines)
│   │   │       │   ├── NCS2006-FTA.svg (810 lines)
│   │   │       │   ├── NCS2006-LCD.svg (774 lines)
│   │   │       │   ├── NCS2006-SA.svg (2208 lines)
│   │   │       │   ├── NCS2015-ECU.svg (9338 lines)
│   │   │       │   ├── NCS2015-FILLER-FAN.svg (1208 lines)
│   │   │       │   ├── NCS2015-FTA.svg (2161 lines)
│   │   │       │   ├── NCS2015-SA.svg (6687 lines)
│   │   │       │   ├── NCS2K-100G-CK-C.svg (3502 lines)
│   │   │       │   ├── NCS2K-100GS-CK-C.svg (3445 lines)
│   │   │       │   ├── NCS2K-12-AD-CCOFS.svg (2833 lines)
│   │   │       │   ├── NCS2K-16-AD-CCOFS.svg (2520 lines)
│   │   │       │   ├── NCS2K-16-WXC-FS.svg (5119 lines)
│   │   │       │   ├── NCS2K-200G-CK-C=.svg (3436 lines)
│   │   │       │   ├── NCS2K-250G-2CK-LC.svg (2671 lines)
│   │   │       │   ├── NCS2K-400G-XP.svg (3691 lines)
│   │   │       │   ├── NCS2K-9-SMR17FS.svg (3921 lines)
│   │   │       │   ├── NCS2K-9-SMR24FS.svg (3923 lines)
│   │   │       │   ├── NCS2K-9-SMR34FS.svg (3923 lines)
│   │   │       │   ├── NCS2K-EDRAX-XX.svg (4891 lines)
│   │   │       │   ├── NCS2K-FILLER-LC.svg (135 lines)
│   │   │       │   ├── NCS2K-MF-10AD-CFS.svg (2437 lines)
│   │   │       │   ├── NCS2K-MF-16AD-CFS.svg (2955 lines)
│   │   │       │   ├── NCS2K-MF-16AE-CFS.svg (3472 lines)
│   │   │       │   ├── NCS2K-MF-1RU.svg (1051 lines)
│   │   │       │   ├── NCS2K-MF-2LC-ADP.svg (635 lines)
│   │   │       │   ├── NCS2K-MF-2MPO-ADP.svg (1245 lines)
│   │   │       │   ├── NCS2K-MF-4x4-COFS.svg (1277 lines)
│   │   │       │   ├── NCS2K-MF-6AD-CFS.svg (727 lines)
│   │   │       │   ├── NCS2K-MF-8X10G-FO.svg (1298 lines)
│   │   │       │   ├── NCS2K-MF-AST-EDFA.svg (1501 lines)
│   │   │       │   ├── NCS2K-MF-DEG-5.svg (1034 lines)
│   │   │       │   ├── NCS2K-MF-FILLER.svg (267 lines)
│   │   │       │   ├── NCS2K-MF-FILLER2.svg (516 lines)
│   │   │       │   ├── NCS2K-MF-MPO-16LC.svg (2043 lines)
│   │   │       │   ├── NCS2K-MF-MPO-20LC.svg (1303 lines)
│   │   │       │   ├── NCS2K-MF-MPO-8LC.svg (1285 lines)
│   │   │       │   ├── NCS2K-MF-UPG-4.svg (1322 lines)
│   │   │       │   ├── NCS2K-MR-MXP-LIC=.svg (5166 lines)
│   │   │       │   ├── NCS2K-MR-MXP.svg (4349 lines)
│   │   │       │   ├── NCS2K-OPT-EDFA-35.svg (2097 lines)
│   │   │       │   ├── NCS2K-OPT-EDFA-35_filler.svg (73 lines)
│   │   │       │   ├── NCS2K-PPMESH8-5AD.svg (3843 lines)
│   │   │       │   ├── NCS2K-SMR-20-FS-CV.svg (5107 lines)
│   │   │       │   ├── NCS2K-SMR-20-FS.svg (3654 lines)
│   │   │       │   ├── NCS2K-SMR-9-FS.svg (4153 lines)
│   │   │       │   ├── NCS2K-TNCS-O-K9.svg (1781 lines)
│   │   │       │   ├── NCS4K-DC-PSU-V1.svg (1385 lines)
│   │   │       │   ├── ONS-CFP2.svg (138 lines)
│   │   │       │   ├── PPM-1.svg (80 lines)
│   │   │       │   ├── QSFP-4.svg (208 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   ├── SFP.svg (172 lines)
│   │   │       │   ├── TNCS-2.svg (1275 lines)
│   │   │       │   └── TNCS-2O.svg (1730 lines)
│   │   │       └── vertical/
│   │   │           ├── 15216-EF-40-EVEN.svg (10335 lines)
│   │   │           ├── 15216-EF-40-ODD.svg (10326 lines)
│   │   │           ├── 15216-FLD-OSC.svg (1507 lines)
│   │   │           ├── 15216-FLD4.svg (1328 lines)
│   │   │           ├── 15216-MD-40-EVEN.svg (10458 lines)
│   │   │           ├── 15216-MD-40-ODD.svg (6475 lines)
│   │   │           ├── 15216-MD-48-CM-FILLER.svg (130 lines)
│   │   │           ├── 15216-MD-48-CM.svg (566 lines)
│   │   │           ├── 15216-MD-48-EVEN.svg (10363 lines)
│   │   │           ├── 15216-MD-48-ODD.svg (10269 lines)
│   │   │           ├── 15454-10DME-C.svg (1124 lines)
│   │   │           ├── 15454-10E-L1.svg (878 lines)
│   │   │           ├── 15454-10GE-XP.svg (3320 lines)
│   │   │           ├── 15454-10ME-L1-C.svg (1458 lines)
│   │   │           ├── 15454-32-DMX.svg (2045 lines)
│   │   │           ├── 15454-32-MUX-O.svg (1997 lines)
│   │   │           ├── 15454-32-WSS.svg (2643 lines)
│   │   │           ├── 15454-40-DMX-C.svg (1972 lines)
│   │   │           ├── 15454-40-MUX-C.svg (2068 lines)
│   │   │           ├── 15454-40-SMR1-C.svg (3532 lines)
│   │   │           ├── 15454-40-SMR2-C.svg (3195 lines)
│   │   │           ├── 15454-40-WSS-C.svg (1181 lines)
│   │   │           ├── 15454-40-WXC-C.svg (2050 lines)
│   │   │           ├── 15454-40E-MXP-C.svg (2390 lines)
│   │   │           ├── 15454-40E-TXP-C.svg (690 lines)
│   │   │           ├── 15454-40EX-MXP-C.svg (2390 lines)
│   │   │           ├── 15454-40ME-MXP-C.svg (2390 lines)
│   │   │           ├── 15454-80-WXC-C.svg (4481 lines)
│   │   │           ├── 15454-AD-1C.svg (753 lines)
│   │   │           ├── 15454-AD-2C.svg (862 lines)
│   │   │           ├── 15454-AD-4C.svg (1110 lines)
│   │   │           ├── 15454-ADM-10G.svg (5397 lines)
│   │   │           ├── 15454-AR-XP.svg (2575 lines)
│   │   │           ├── 15454-BLANK.svg (357 lines)
│   │   │           ├── 15454-DM-L1-XX.svg (1470 lines)
│   │   │           ├── 15454-DMP-L1-XX.svg (1730 lines)
│   │   │           ├── 15454-FBR-STRG.svg (359 lines)
│   │   │           ├── 15454-FILLER-LCD.svg (109 lines)
│   │   │           ├── 15454-FTA-3T.svg (364 lines)
│   │   │           ├── 15454-FTA-3T_FILLER.svg (83 lines)
│   │   │           ├── 15454-GE-XP.svg (2268 lines)
│   │   │           ├── 15454-M-100G-LC-C.svg (652 lines)
│   │   │           ├── 15454-M-100G-ME-C.svg (586 lines)
│   │   │           ├── 15454-M-100ME-CK-C.svg (4935 lines)
│   │   │           ├── 15454-M-10X10G-LC.svg (1874 lines)
│   │   │           ├── 15454-M-CFP-LC.svg (830 lines)
│   │   │           ├── 15454-M-RAMAN-COP.svg (1123 lines)
│   │   │           ├── 15454-M-RAMAN-CTP.svg (2449 lines)
│   │   │           ├── 15454-M-TNC-K9.svg (3467 lines)
│   │   │           ├── 15454-M-TNCE-K9.svg (3467 lines)
│   │   │           ├── 15454-M-TSC-K9.svg (1411 lines)
│   │   │           ├── 15454-M-TSCE-K9.svg (1411 lines)
│   │   │           ├── 15454-M-WSE-K9.svg (3490 lines)
│   │   │           ├── 15454-M2-AC.svg (682 lines)
│   │   │           ├── 15454-M2-DC.svg (785 lines)
│   │   │           ├── 15454-M2-FILLER-FAN.svg (71 lines)
│   │   │           ├── 15454-M2-FTA.svg (308 lines)
│   │   │           ├── 15454-M2-Front.svg (564 lines)
│   │   │           ├── 15454-M6-AC.svg (795 lines)
│   │   │           ├── 15454-M6-AC2.svg (911 lines)
│   │   │           ├── 15454-M6-DC.svg (592 lines)
│   │   │           ├── 15454-M6-ECU-60.svg (1515 lines)
│   │   │           ├── 15454-M6-ECU-S.svg (3458 lines)
│   │   │           ├── 15454-M6-ECU.svg (1666 lines)
│   │   │           ├── 15454-M6-ECU2.svg (1699 lines)
│   │   │           ├── 15454-M6-FILLER-ECU.svg (158 lines)
│   │   │           ├── 15454-M6-FILLER-FTA.svg (70 lines)
│   │   │           ├── 15454-M6-FTA.svg (355 lines)
│   │   │           ├── 15454-M6-Front.svg (787 lines)
│   │   │           ├── 15454-M6-LCD.svg (401 lines)
│   │   │           ├── 15454-MR-L1.svg (677 lines)
│   │   │           ├── 15454-MRP-L1.svg (839 lines)
│   │   │           ├── 15454-OPT-AMP-17C.svg (1778 lines)
│   │   │           ├── 15454-OPT-AMP-C.svg (2658 lines)
│   │   │           ├── 15454-OPT-BST-E.svg (2741 lines)
│   │   │           ├── 15454-OPT-BST.svg (2736 lines)
│   │   │           ├── 15454-OPT-EDFA-17.svg (2423 lines)
│   │   │           ├── 15454-OPT-EDFA-24.svg (2426 lines)
│   │   │           ├── 15454-OPT-PRE.svg (2282 lines)
│   │   │           ├── 15454-OPT-RAMP-C.svg (957 lines)
│   │   │           ├── 15454-OPT-RAMP-CE.svg (935 lines)
│   │   │           ├── 15454-OSC-CSM.svg (782 lines)
│   │   │           ├── 15454-OSCM.svg (1388 lines)
│   │   │           ├── 15454-OTU2-XP.svg (1073 lines)
│   │   │           ├── 15454-PP-4-SMR.svg (4195 lines)
│   │   │           ├── 15454-PP-MESH-4.svg (4858 lines)
│   │   │           ├── 15454-PP-MESH-8.svg (7678 lines)
│   │   │           ├── 15454-PSM.svg (1682 lines)
│   │   │           ├── 15454-SA-ANSI-SA-HD.svg (434 lines)
│   │   │           ├── 15454-TDC-CC.svg (808 lines)
│   │   │           ├── 15454-TDC-FC.svg (748 lines)
│   │   │           ├── 15454-YCBL-LC.svg (206 lines)
│   │   │           ├── 15454E-SA-ETSI.svg (551 lines)
│   │   │           ├── 15454E-TCC2.svg (1283 lines)
│   │   │           ├── 15454E-TCC3-K9.svg (1303 lines)
│   │   │           ├── 15454E-TCCP.svg (1228 lines)
│   │   │           ├── 15454W-TNCS-K9.svg (3486 lines)
│   │   │           ├── CPAK.svg (126 lines)
│   │   │           ├── MF-6RU.svg (8150 lines)
│   │   │           ├── MF10-6RU.svg (1078 lines)
│   │   │           ├── MPO-16.svg (350 lines)
│   │   │           ├── MPO-16V.svg (348 lines)
│   │   │           ├── MPO-24.svg (478 lines)
│   │   │           ├── MPO-8.svg (222 lines)
│   │   │           ├── MPO-8V.svg (222 lines)
│   │   │           ├── NCS2002-AC.svg (1190 lines)
│   │   │           ├── NCS2002-DC.svg (1304 lines)
│   │   │           ├── NCS2002-FILLER-FTA.svg (70 lines)
│   │   │           ├── NCS2002-FILLER-PSU.svg (70 lines)
│   │   │           ├── NCS2002-FTA.svg (679 lines)
│   │   │           ├── NCS2006-AC.svg (691 lines)
│   │   │           ├── NCS2006-DC.svg (690 lines)
│   │   │           ├── NCS2006-ECU-60.svg (1515 lines)
│   │   │           ├── NCS2006-ECU-S.svg (3211 lines)
│   │   │           ├── NCS2006-ECU.svg (1666 lines)
│   │   │           ├── NCS2006-FILLER-DC.svg (70 lines)
│   │   │           ├── NCS2006-FILLER-ECU.svg (158 lines)
│   │   │           ├── NCS2006-FILLER-FTA.svg (70 lines)
│   │   │           ├── NCS2006-FILLER-LCD.svg (109 lines)
│   │   │           ├── NCS2006-FILLER-PSU.svg (70 lines)
│   │   │           ├── NCS2006-FTA.svg (810 lines)
│   │   │           ├── NCS2006-LCD.svg (775 lines)
│   │   │           ├── NCS2006-SA.svg (1914 lines)
│   │   │           ├── NCS2015-ECU.svg (9158 lines)
│   │   │           ├── NCS2015-FILLER-FAN.svg (1208 lines)
│   │   │           ├── NCS2015-FTA.svg (2161 lines)
│   │   │           ├── NCS2015-SA.svg (8003 lines)
│   │   │           ├── NCS2K-100G-CK-C.svg (3502 lines)
│   │   │           ├── NCS2K-100GS-CK-C.svg (3447 lines)
│   │   │           ├── NCS2K-12-AD-CCOFS.svg (2833 lines)
│   │   │           ├── NCS2K-16-AD-CCOFS.svg (2520 lines)
│   │   │           ├── NCS2K-16-WXC-FS.svg (5118 lines)
│   │   │           ├── NCS2K-200G-CK-C=.svg (3436 lines)
│   │   │           ├── NCS2K-250G-2CK-LC.svg (2679 lines)
│   │   │           ├── NCS2K-400G-XP.svg (3781 lines)
│   │   │           ├── NCS2K-9-SMR17FS.svg (3923 lines)
│   │   │           ├── NCS2K-9-SMR24FS.svg (3923 lines)
│   │   │           ├── NCS2K-9-SMR34FS.svg (3923 lines)
│   │   │           ├── NCS2K-EDRAX-XX.svg (4875 lines)
│   │   │           ├── NCS2K-FILLER-LC.svg (135 lines)
│   │   │           ├── NCS2K-MF-10AD-CFS.svg (2437 lines)
│   │   │           ├── NCS2K-MF-16AD-CFS.svg (3305 lines)
│   │   │           ├── NCS2K-MF-16AE-CFS.svg (3472 lines)
│   │   │           ├── NCS2K-MF-1RU.svg (1283 lines)
│   │   │           ├── NCS2K-MF-2LC-ADP.svg (635 lines)
│   │   │           ├── NCS2K-MF-2MPO-ADP.svg (1245 lines)
│   │   │           ├── NCS2K-MF-4x4-COFS.svg (1329 lines)
│   │   │           ├── NCS2K-MF-6AD-CFS.svg (727 lines)
│   │   │           ├── NCS2K-MF-8X10G-FO.svg (1300 lines)
│   │   │           ├── NCS2K-MF-AST-EDFA.svg (1578 lines)
│   │   │           ├── NCS2K-MF-DEG-5.svg (1104 lines)
│   │   │           ├── NCS2K-MF-FILLER.svg (342 lines)
│   │   │           ├── NCS2K-MF-FILLER2.svg (516 lines)
│   │   │           ├── NCS2K-MF-MPO-16LC.svg (2043 lines)
│   │   │           ├── NCS2K-MF-MPO-20LC.svg (1302 lines)
│   │   │           ├── NCS2K-MF-MPO-8LC.svg (1337 lines)
│   │   │           ├── NCS2K-MF-UPG-4.svg (1444 lines)
│   │   │           ├── NCS2K-MR-MXP-LIC=.svg (5177 lines)
│   │   │           ├── NCS2K-MR-MXP.svg (4356 lines)
│   │   │           ├── NCS2K-OPT-EDFA-35.svg (2120 lines)
│   │   │           ├── NCS2K-OPT-EDFA-35_filler.svg (78 lines)
│   │   │           ├── NCS2K-PPMESH8-5AD.svg (3843 lines)
│   │   │           ├── NCS2K-SMR-20-FS-CV.svg (5110 lines)
│   │   │           ├── NCS2K-SMR-20-FS.svg (3678 lines)
│   │   │           ├── NCS2K-SMR-9-FS.svg (3923 lines)
│   │   │           ├── NCS2K-TNCS-O-K9.svg (1795 lines)
│   │   │           ├── NCS4K-DC-PSU-V1.svg (1385 lines)
│   │   │           ├── ONS-CFP2.svg (138 lines)
│   │   │           ├── PPM-1.svg (91 lines)
│   │   │           ├── QSFP-4.svg (177 lines)
│   │   │           ├── QSFP.svg (173 lines)
│   │   │           ├── SFP.svg (176 lines)
│   │   │           ├── TNCS-2.svg (1289 lines)
│   │   │           └── TNCS-2O.svg (1732 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs4k/
│   │   ├── Cisco_NCS_4009/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4009.json (188 lines)
│   │   │   └── images/
│   │   │       └── chassis_4009.svg (855 lines)
│   │   ├── Cisco_NCS_4016/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_4016.json (399 lines)
│   │   │   └── images/
│   │   │       ├── NCS4KF-core.svg (5933 lines)
│   │   │       ├── chassis.svg (5801 lines)
│   │   │       └── chassis24ru.svg (3054 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (665 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (5053 lines)
│   │   │   └── images/
│   │   │       ├── flip/
│   │   │       │   ├── 20x10OTN.svg (1860 lines)
│   │   │       │   ├── 24xOC48.svg (2184 lines)
│   │   │       │   ├── 2x100CPAK.svg (1016 lines)
│   │   │       │   ├── 2x100DWDM.svg (1204 lines)
│   │   │       │   ├── 4H-QDD-P.svg (1928 lines)
│   │   │       │   ├── CPAK.svg (126 lines)
│   │   │       │   ├── NCS4K-1H-W-LIC.svg (1206 lines)
│   │   │       │   ├── NCS4K-4H-OPW-QC2.svg (2538 lines)
│   │   │       │   ├── NCS4K-FILLER-LC.svg (74 lines)
│   │   │       │   ├── NCS4k-2H10T-OP-KS.svg (1563 lines)
│   │   │       │   ├── ONS-CFP2.svg (135 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   ├── SFP.svg (176 lines)
│   │   │       │   ├── fabric.svg (1004 lines)
│   │   │       │   ├── fabric_mc.svg (1161 lines)
│   │   │       │   └── rp.svg (1307 lines)
│   │   │       ├── horizontal/
│   │   │       │   ├── 20x10OTN.svg (2032 lines)
│   │   │       │   ├── 24xOC48.svg (2236 lines)
│   │   │       │   ├── 2x100CPAK.svg (1004 lines)
│   │   │       │   ├── 2x100DWDM.svg (1192 lines)
│   │   │       │   ├── 4H-QDD-P.svg (1919 lines)
│   │   │       │   ├── CPAK.svg (126 lines)
│   │   │       │   ├── NCS4K-1H-W-LIC.svg (1194 lines)
│   │   │       │   ├── NCS4K-4H-OPW-QC2.svg (2543 lines)
│   │   │       │   ├── NCS4K-DC-PSU-V1.svg (1385 lines)
│   │   │       │   ├── NCS4K-FILLER-PSU.svg (83 lines)
│   │   │       │   ├── NCS4K-FILLER-PT.svg (80 lines)
│   │   │       │   ├── NCS4KF-CRAFT-FILLER.svg (79 lines)
│   │   │       │   ├── NCS4KF-CRAFT.svg (235 lines)
│   │   │       │   ├── NCS4KF-DC-PSU-V1.svg (533 lines)
│   │   │       │   ├── NCS4KF-FC2-C-filler.svg (79 lines)
│   │   │       │   ├── NCS4KF-FC2-C.svg (3769 lines)
│   │   │       │   ├── NCS4KF-FILLER-PSU.svg (89 lines)
│   │   │       │   ├── NCS4KF-FTA-filler.svg (78 lines)
│   │   │       │   ├── NCS4KF-FTA.svg (2442 lines)
│   │   │       │   ├── NCS4KF-Power-Module-filler.svg (78 lines)
│   │   │       │   ├── NCS4KF-Power-Module.svg (374 lines)
│   │   │       │   ├── NCS4KF-RPMC-filler.svg (79 lines)
│   │   │       │   ├── NCS4KF-RPMC.svg (6113 lines)
│   │   │       │   ├── NCS4k-2H10T-OP-KS.svg (1553 lines)
│   │   │       │   ├── ONS-CFP2.svg (135 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   ├── SFP.svg (172 lines)
│   │   │       │   ├── ecu.svg (2506 lines)
│   │   │       │   ├── fabric_4009.svg (3725 lines)
│   │   │       │   ├── fabric_mc.svg (1149 lines)
│   │   │       │   ├── fan.svg (372 lines)
│   │   │       │   ├── pluggables.json (2806 lines)
│   │   │       │   ├── power_tray.svg (401 lines)
│   │   │       │   └── rp.svg (1289 lines)
│   │   │       └── vertical/
│   │   │           ├── 20x10OTN.svg (1899 lines)
│   │   │           ├── 24xOC48.svg (2159 lines)
│   │   │           ├── 2x100CPAK.svg (1002 lines)
│   │   │           ├── 2x100DWDM.svg (1187 lines)
│   │   │           ├── 4H-QDD-P.svg (1928 lines)
│   │   │           ├── CPAK.svg (126 lines)
│   │   │           ├── NCS4009-FILLER-FC.svg (80 lines)
│   │   │           ├── NCS4K-1H-W-LIC.svg (1189 lines)
│   │   │           ├── NCS4K-4H-OPW-QC2.svg (2548 lines)
│   │   │           ├── NCS4K-BLANK.svg (3199 lines)
│   │   │           ├── NCS4K-DC-PSU-V1.svg (1385 lines)
│   │   │           ├── NCS4K-FILLER-ECU.svg (71 lines)
│   │   │           ├── NCS4K-FILLER-FTA.svg (77 lines)
│   │   │           ├── NCS4K-FILLER-LC.svg (81 lines)
│   │   │           ├── NCS4K-FILLER-PSU.svg (83 lines)
│   │   │           ├── NCS4K-FILLER-PT.svg (80 lines)
│   │   │           ├── NCS4KF-DC-PSU-V1.svg (537 lines)
│   │   │           ├── NCS4KF-FC2-C-filler.svg (78 lines)
│   │   │           ├── NCS4KF-FC2-C.svg (3765 lines)
│   │   │           ├── NCS4KF-FILLER-PSU.svg (83 lines)
│   │   │           ├── NCS4KF-FTA-filler.svg (83 lines)
│   │   │           ├── NCS4KF-FTA.svg (2442 lines)
│   │   │           ├── NCS4KF-Power-Module-filler.svg (79 lines)
│   │   │           ├── NCS4KF-Power-Module.svg (378 lines)
│   │   │           ├── NCS4KF-RPMC-filler.svg (78 lines)
│   │   │           ├── NCS4KF-RPMC.svg (6111 lines)
│   │   │           ├── NCS4k-2H10T-OP-KS.svg (1556 lines)
│   │   │           ├── ONS-CFP2.svg (135 lines)
│   │   │           ├── QSFP.svg (173 lines)
│   │   │           ├── SFP.svg (176 lines)
│   │   │           ├── alertCritical.svg (19 lines)
│   │   │           ├── alertMajor.svg (11 lines)
│   │   │           ├── alertMinor.svg (11 lines)
│   │   │           ├── cpak_lr4.svg (213 lines)
│   │   │           ├── cpak_sr10.svg (206 lines)
│   │   │           ├── cxp.svg (119 lines)
│   │   │           ├── ecu.svg (2506 lines)
│   │   │           ├── fabric.svg (1023 lines)
│   │   │           ├── fabric_4009.svg (3725 lines)
│   │   │           ├── fabric_mc.svg (1134 lines)
│   │   │           ├── fan.svg (372 lines)
│   │   │           ├── pem24ru.svg (499 lines)
│   │   │           ├── power_tray.svg (401 lines)
│   │   │           └── rp.svg (1287 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs520/
│   │   ├── Cisco_NCS_520-4G4Z-A_Carrier_Ethernet_Access_Device/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_520-4G4Z-A_Carrier_Ethernet_Access_Device.json (48 lines)
│   │   │   └── images/
│   │   │       └── N520-X-4G4Z-A.svg (4284 lines)
│   │   ├── Cisco_NCS_520-X-4G4Z-A_Carrier_Ethernet_Access_Device/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_520-X-4G4Z-A_Carrier_Ethernet_Access_Device.json (48 lines)
│   │   │   └── images/
│   │   │       └── N520-X-4G4Z-A.svg (4284 lines)
│   │   ├── Cisco_NCS_520-X-4G4Z-D_Carrier_Ethernet_Access_Device/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_520-X-4G4Z-D_Carrier_Ethernet_Access_Device.json (48 lines)
│   │   │   └── images/
│   │   │       └── N520-X-4G4Z-D_core.svg (3210 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (520 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (332 lines)
│   │   │   └── images/
│   │   │       └── horizontal/
│   │   │           ├── 4xGE-4x10GE-FIXED.svg (2039 lines)
│   │   │           ├── N520-X-4G4Z-A_RP.svg (404 lines)
│   │   │           └── SFP.svg (253 lines)
│   │   ├── assembly.xml (24 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs540/
│   │   ├── Cisco_8011-12G12X4Y-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8011-12G12X4Y-A_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── 8011-12G12X4Y-A_front_core.svg (3287 lines)
│   │   ├── Cisco_8011-12G12X4Y-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8011-12G12X4Y-D_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── 8011-12G12X4Y-D_front_core.svg (3338 lines)
│   │   ├── Cisco_8011-2X2XP4L_Series_1RU_PLE_NID_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8011-2X2XP4L_Series_1RU_PLE_NID_Router.json (90 lines)
│   │   │   └── images/
│   │   │       ├── 8011-2X2XP4L_front_core.svg (3649 lines)
│   │   │       └── 8011-2X2XP4L_rear_core.svg (2662 lines)
│   │   ├── Cisco_8011-4G24Y4H-I_Series_1RU_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8011-4G24Y4H-I_Series_1RU_Router.json (90 lines)
│   │   │   └── images/
│   │   │       ├── 8011-4G24Y4H-I_front_core.svg (3377 lines)
│   │   │       └── 8011-4G24Y4H-I_rear_core.svg (2522 lines)
│   │   ├── Cisco_8101-32FH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8101-32FH_Router.json (149 lines)
│   │   │   └── images/
│   │   │       ├── 8101-32FH-front_core.svg (116 lines)
│   │   │       └── 8101-32FH-rear_core.svg (240 lines)
│   │   ├── Cisco_8111-32EH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8111-32EH_Router.json (139 lines)
│   │   │   └── images/
│   │   │       ├── 8111-32EH-front_core.svg (123 lines)
│   │   │       └── 8111-32EH-rear_core.svg (256 lines)
│   │   ├── Cisco_8201-24H8FH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8201-24H8FH_Router.json (140 lines)
│   │   │   └── images/
│   │   │       ├── 8201-24H8FH-front_core.svg (120 lines)
│   │   │       └── 8201-24H8FH-rear_core.svg (256 lines)
│   │   ├── Cisco_8201-32FH_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8201-32FH_Router.json (151 lines)
│   │   │   └── images/
│   │   │       ├── 8201-32FH-front_core.svg (116 lines)
│   │   │       └── 8201-32FH-rear_core.svg (240 lines)
│   │   ├── Cisco_8201_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8201_Router.json (147 lines)
│   │   │   └── images/
│   │   │       ├── Cisco-8201-SYS-front_core.svg (885 lines)
│   │   │       └── Cisco-8201-SYS-rear_core.svg (492 lines)
│   │   ├── Cisco_8202-32FH-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8202-32FH-M_Router.json (116 lines)
│   │   │   └── images/
│   │   │       ├── 8202-32FH-M_front_core.svg (15904 lines)
│   │   │       └── 8202-32FH-M_rear_core.svg (203 lines)
│   │   ├── Cisco_8202_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8202_Router.json (129 lines)
│   │   │   └── images/
│   │   │       ├── 8202-SYS_front_core.svg (3496 lines)
│   │   │       └── 8202-SYS_rear_core.svg (632 lines)
│   │   ├── Cisco_8212-48FH-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8212-48FH-M_Router.json (114 lines)
│   │   │   └── images/
│   │   │       ├── 8212-48FH-M_front_core.svg (22272 lines)
│   │   │       └── 8212-48FH-M_rear_core.svg (450 lines)
│   │   ├── Cisco_8608_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8608_Router.json (233 lines)
│   │   │   └── images/
│   │   │       ├── 8608-SYS_Front_Core.svg (662 lines)
│   │   │       └── 8608-SYS_Rear_Core.svg (1202 lines)
│   │   ├── Cisco_8711-32FH-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8711-32FH-M_Router.json (137 lines)
│   │   │   └── images/
│   │   │       ├── 8711-32FH-M-front_core.svg (137 lines)
│   │   │       └── 8711-32FH-M-rear_core.svg (305 lines)
│   │   ├── Cisco_8712-MOD-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8712-MOD-M_Router.json (141 lines)
│   │   │   └── images/
│   │   │       ├── 8712-MOD-M_front_core.svg (1147 lines)
│   │   │       └── 8712-MOD-M_rear_core.svg (337 lines)
│   │   ├── Cisco_8804_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8804_Router.json (386 lines)
│   │   │   └── images/
│   │   │       ├── 8804-SYS_front_core.svg (1473 lines)
│   │   │       └── 8804-SYS_rear_core.svg (2043 lines)
│   │   ├── Cisco_8808_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8808_Router.json (520 lines)
│   │   │   └── images/
│   │   │       ├── 8808-SYS_front_core.svg (2227 lines)
│   │   │       └── 8808-SYS_rear_core.svg (9978 lines)
│   │   ├── Cisco_8812_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8812_Router.json (368 lines)
│   │   │   └── images/
│   │   │       ├── 8812-SYS_front_core.svg (2336 lines)
│   │   │       └── 8812-SYS_rear_core.svg (9699 lines)
│   │   ├── Cisco_8818_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_8818_Router.json (487 lines)
│   │   │   └── images/
│   │   │       ├── 8818-SYS_front_core.svg (4007 lines)
│   │   │       └── 8818-SYS_rear_core.svg (18836 lines)
│   │   ├── Cisco_N540-24Q2C2DD-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_N540-24Q2C2DD-SYS_Router.json (90 lines)
│   │   │   └── images/
│   │   │       ├── N540-24Q2C2DD-SYS_front_core.svg (5892 lines)
│   │   │       └── N540-24Q2C2DD-SYS_rear_core.svg (1387 lines)
│   │   ├── Cisco_N540-8Z12G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_N540-8Z12G-SYS-D_Router.json (56 lines)
│   │   │   └── images/
│   │   │       └── N540-8Z12G-SYS-D_Core.svg (2279 lines)
│   │   ├── Cisco_NCS-57B1-5DSE-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57B1-5DSE-SYS_Router.json (139 lines)
│   │   │   └── images/
│   │   │       ├── NCS-57B1-5DSE-SYS_Front_core.svg (2398 lines)
│   │   │       └── NCS-57B1-5DSE-SYS_Rear_core.svg (164 lines)
│   │   ├── Cisco_NCS-57B1-6D24-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57B1-6D24-SYS_Router.json (139 lines)
│   │   │   └── images/
│   │   │       ├── NCS-57B1-6D24-SYS_Front_core.svg (2361 lines)
│   │   │       └── NCS-57B1-6D24-SYS_Rear_core.svg (164 lines)
│   │   ├── Cisco_NCS-57C1-48Q6-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57C1-48Q6-SYS_Router.json (122 lines)
│   │   │   └── images/
│   │   │       ├── NCS-57C1-48Q6-SYS_front_core.svg (1908 lines)
│   │   │       └── NCS-57C1-48Q6-SYS_rear_core.svg (598 lines)
│   │   ├── Cisco_NCS-57D2-18DD-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57D2-18DD-SYS_Router.json (116 lines)
│   │   │   └── images/
│   │   │       ├── NCS-57D2-18DD-SYS_front_core.svg (3593 lines)
│   │   │       └── NCS-57D2-18DD-SYS_rear_core.svg (337 lines)
│   │   ├── Cisco_NCS_540-12Z20G-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-12Z20G-SYS-A_Router.json (92 lines)
│   │   │   └── images/
│   │   │       ├── N540-12Z20G-SYS-A_Front_core.svg (3510 lines)
│   │   │       └── N540-12Z20G-SYS-A_rear_core.svg (422 lines)
│   │   ├── Cisco_NCS_540-12Z20G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-12Z20G-SYS-D_Router.json (101 lines)
│   │   │   └── images/
│   │   │       ├── N540-12Z20G-SYS-D_front_core.svg (3289 lines)
│   │   │       └── N540-12Z20G-SYS-D_rear_core.svg (422 lines)
│   │   ├── Cisco_NCS_540-24Q8L2DD-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-24Q8L2DD-SYS-A_Router.json (97 lines)
│   │   │   └── images/
│   │   │       ├── N540-24Q8L2DD-SYS_front_core.svg (2987 lines)
│   │   │       └── N540-24Q8L2DD-SYS_rear_core.svg (1117 lines)
│   │   ├── Cisco_NCS_540-28Z4C-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-28Z4C-SYS-A_Router.json (50 lines)
│   │   │   └── images/
│   │   │       └── N540-28Z4C-SYS-A_front_core.svg (4951 lines)
│   │   ├── Cisco_NCS_540-28Z4C-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-28Z4C-SYS-D_Router.json (50 lines)
│   │   │   └── images/
│   │   │       └── N540-28Z4C-SYS-D_front_core.svg (3869 lines)
│   │   ├── Cisco_NCS_540-6Z18G-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-6Z18G-SYS-A_Router.json (51 lines)
│   │   │   └── images/
│   │   │       └── N540-6Z18G-SYS-A_Core.svg (1082 lines)
│   │   ├── Cisco_NCS_540-6Z18G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-6Z18G-SYS-D_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── N540-6Z18G-SYS-D_Core.svg (1252 lines)
│   │   ├── Cisco_NCS_540-FH-AGG-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-FH-AGG-SYS_Router.json (121 lines)
│   │   │   └── images/
│   │   │       ├── N540-FH-AGG-SYS_Front_Core.svg (4828 lines)
│   │   │       └── N540-FH-AGG-SYS_Rear_Core.svg (205 lines)
│   │   ├── Cisco_NCS_540-FH-CSR-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-FH-CSR-SYS_Router.json (88 lines)
│   │   │   └── images/
│   │   │       ├── N540-FH-CSR-SYS_Front_Core.svg (2282 lines)
│   │   │       └── N540-FH-CSR-SYS_Rear_Core.svg (2003 lines)
│   │   ├── Cisco_NCS_540X-12Z16G-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-12Z16G-SYS-A_Router.json (51 lines)
│   │   │   └── images/
│   │   │       └── N540X-12Z16G-SYS-A_Front_core.svg (683 lines)
│   │   ├── Cisco_NCS_540X-12Z16G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-12Z16G-SYS-D_Router.json (51 lines)
│   │   │   └── images/
│   │   │       └── N540X-12Z16G-SYS-D_Front_core.svg (809 lines)
│   │   ├── Cisco_NCS_540X-16Z4G8Q2C-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-16Z4G8Q2C-A_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── N540X-16Z4G8Q2C-A_Front_core.svg (1371 lines)
│   │   ├── Cisco_NCS_540X-16Z4G8Q2C-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-16Z4G8Q2C-D_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── N540X-16Z4G8Q2C-D_Front_core.svg (1655 lines)
│   │   ├── Cisco_NCS_540X-16Z8Q2C-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-16Z8Q2C-D_Router.json (64 lines)
│   │   │   └── images/
│   │   │       └── N540X-16Z8Q2C-D_front_core.svg (1103 lines)
│   │   ├── Cisco_NCS_540X-4Z14G2Q-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-4Z14G2Q-A_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── N540X-4Z14G2Q-A_front_core.svg (2106 lines)
│   │   ├── Cisco_NCS_540X-4Z14G2Q-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-4Z14G2Q-D_Router.json (59 lines)
│   │   │   └── images/
│   │   │       └── N540X-4Z14G2Q-D_font_core.svg (2156 lines)
│   │   ├── Cisco_NCS_540X-6Z14S-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-6Z14S-SYS-D_Router.json (56 lines)
│   │   │   └── images/
│   │   │       └── N540-6Z14S-SYS-D_core.svg (1879 lines)
│   │   ├── Cisco_NCS_540X-6Z18G-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-6Z18G-SYS-A_Router.json (58 lines)
│   │   │   └── images/
│   │   │       └── N540-6Z18G-SYS-A_front_core.svg (1756 lines)
│   │   ├── Cisco_NCS_540X-6Z18G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-6Z18G-SYS-D_Router.json (58 lines)
│   │   │   └── images/
│   │   │       └── N540-6Z18G-SYS-D_front_core.svg (1048 lines)
│   │   ├── Cisco_NCS_540X-8Z16G-SYS-A_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-8Z16G-SYS-A_Router.json (58 lines)
│   │   │   └── images/
│   │   │       └── N540-8Z16G-SYS-A_front_core.svg (1663 lines)
│   │   ├── Cisco_NCS_540X-8Z16G-SYS-D_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-8Z16G-SYS-D_Router.json (58 lines)
│   │   │   └── images/
│   │   │       └── N540-8Z16G-SYS-D_front_core.svg (1910 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (1034 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (49312 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── 8011-12G12X4Y-A_PM_AC.svg (96 lines)
│   │   │       │   ├── 8011-12G12X4Y-A_PM_AC_Filler.svg (65 lines)
│   │   │       │   ├── 8011-12G12X4Y-A_front_ports.svg (2429 lines)
│   │   │       │   ├── 8011-12G12X4Y-D_front_ports.svg (2428 lines)
│   │   │       │   ├── 8011-24X-A_PM_DC.svg (523 lines)
│   │   │       │   ├── 8011-24X-A_PM_DC_Filler.svg (65 lines)
│   │   │       │   ├── 8011-2X2XP4L_front_ports.svg (781 lines)
│   │   │       │   ├── 8011-2X2XP4L_power_module.svg (1182 lines)
│   │   │       │   ├── 8011-2X2XP4L_power_module_filler.svg (83 lines)
│   │   │       │   ├── 8011-2X2XP4L_rear_fan.svg (140 lines)
│   │   │       │   ├── 8011-2X2XP4L_rear_fan_filler.svg (184 lines)
│   │   │       │   ├── 8011-4G24Y4H-I_front_ports.svg (4431 lines)
│   │   │       │   ├── 8011-4G24Y4H-I_rear_fan.svg (136 lines)
│   │   │       │   ├── 8011-4G24Y4H-I_rear_fan_filler.svg (170 lines)
│   │   │       │   ├── 8101-32FH-front.svg (13471 lines)
│   │   │       │   ├── 8111-32EH-front_ports.svg (13585 lines)
│   │   │       │   ├── 8201-24H8FH-front_ports.svg (13579 lines)
│   │   │       │   ├── 8201-24H8FH-rear_fan.svg (239 lines)
│   │   │       │   ├── 8201-24H8FH-rear_fan_filler.svg (87 lines)
│   │   │       │   ├── 8201-24H8FH-rear_powermodule.svg (361 lines)
│   │   │       │   ├── 8201-24H8FH-rear_powermodule_filler.svg (87 lines)
│   │   │       │   ├── 8201-32FH-front.svg (11646 lines)
│   │   │       │   ├── 8201-32FH-front_filler.svg (74 lines)
│   │   │       │   ├── 8201-SYS-RP.svg (2313 lines)
│   │   │       │   ├── 8201-SYS-rear_fan.svg (235 lines)
│   │   │       │   ├── 8201-SYS-rear_fan_filler.svg (64 lines)
│   │   │       │   ├── 8201-SYS-rear_rp.svg (165 lines)
│   │   │       │   ├── 8202-32FH-M_fan.svg (390 lines)
│   │   │       │   ├── 8202-32FH-M_fan_filler.svg (81 lines)
│   │   │       │   ├── 8202-32FH-M_front_port.svg (2566 lines)
│   │   │       │   ├── 8202-SYS_front_ports.svg (7843 lines)
│   │   │       │   ├── 8202-SYS_rear_fan.svg (2512 lines)
│   │   │       │   ├── 8202-SYS_rear_fan_filler.svg (77 lines)
│   │   │       │   ├── 8202-SYS_rear_rp.svg (164 lines)
│   │   │       │   ├── 8212-48FH-M_fan.svg (456 lines)
│   │   │       │   ├── 8212-48FH-M_front_ports.svg (3564 lines)
│   │   │       │   ├── 8212-48FH-M_power_module.svg (565 lines)
│   │   │       │   ├── 8212-48FH-M_power_module_filler.svg (80 lines)
│   │   │       │   ├── 8608-SYS_Front_86-MPA-14H2FH-M.svg (5236 lines)
│   │   │       │   ├── 8608-SYS_Front_86-MPA-24Z-M.svg (3877 lines)
│   │   │       │   ├── 8608-SYS_Front_86-MPA-4FH-M.svg (728 lines)
│   │   │       │   ├── 8608-SYS_MPA_Filler.svg (181 lines)
│   │   │       │   ├── 8608-SYS_RP.svg (742 lines)
│   │   │       │   ├── 8608-SYS_RP_Filler.svg (175 lines)
│   │   │       │   ├── 8608-SYS_Rear_Fan_Filler.svg (75 lines)
│   │   │       │   ├── 8608-SYS_Rear_PowerModule.svg (571 lines)
│   │   │       │   ├── 8608-SYS_Rear_PowerModule_DC.svg (997 lines)
│   │   │       │   ├── 8608-SYS_Rear_PowerModule_Filler.svg (85 lines)
│   │   │       │   ├── 8608-SYS_Rear_Single_Fan.svg (531 lines)
│   │   │       │   ├── 8711-32FH-M-front_ports.svg (20184 lines)
│   │   │       │   ├── 8712-MOD-M_fan.svg (456 lines)
│   │   │       │   ├── 8712-MOD-M_fan_filler.svg (81 lines)
│   │   │       │   ├── 88-LC0-34H14FH.svg (26436 lines)
│   │   │       │   ├── 88-LC1-12TH24EH-E.svg (26983 lines)
│   │   │       │   ├── 88-LC1-36EH.svg (19962 lines)
│   │   │       │   ├── 88-LC1-52Y8H4F-E.svg (17950 lines)
│   │   │       │   ├── 8800-LC-36FH.svg (12711 lines)
│   │   │       │   ├── 8800-LC-48H.svg (17814 lines)
│   │   │       │   ├── 8800-LC-48H_filler.svg (326 lines)
│   │   │       │   ├── 8800-RP.svg (3704 lines)
│   │   │       │   ├── 8800-RP2.svg (1582 lines)
│   │   │       │   ├── 8800-RP_filler.svg (329 lines)
│   │   │       │   ├── 8804-SYS_fabric_card.svg (302 lines)
│   │   │       │   ├── 8804-SYS_fabric_card_filler.svg (75 lines)
│   │   │       │   ├── 8804-SYS_rear_fan.svg (822 lines)
│   │   │       │   ├── 8804-SYS_rear_fan_filler.svg (79 lines)
│   │   │       │   ├── 8808-FC1-01.svg (480 lines)
│   │   │       │   ├── 8808-SYS-Fabric-Card.svg (88 lines)
│   │   │       │   ├── 8808-SYS-Fan-Tray.svg (1134 lines)
│   │   │       │   ├── 8812-Fabric-Card.svg (335 lines)
│   │   │       │   ├── 8812-Fan-Tray.svg (1094 lines)
│   │   │       │   ├── 8818-FC1.svg (380 lines)
│   │   │       │   ├── 8818-SYS-Fabric-Card.svg (88 lines)
│   │   │       │   ├── 8818-SYS-Fan-Tray.svg (1223 lines)
│   │   │       │   ├── 8K-MPA-16H.svg (7004 lines)
│   │   │       │   ├── 8K-MPA-16H_filler.svg (143 lines)
│   │   │       │   ├── 8K-MPA-16Z2D.svg (3220 lines)
│   │   │       │   ├── 8K-MPA-18Z1D.svg (4849 lines)
│   │   │       │   ├── 8K-MPA-4D.svg (757 lines)
│   │   │       │   ├── FAN-1RU-PI-V2_Filler.svg (63 lines)
│   │   │       │   ├── GLC.svg (190 lines)
│   │   │       │   ├── N540-12Z20G-SYS-A_Front_acpowersupply.svg (97 lines)
│   │   │       │   ├── N540-12Z20G-SYS-A_Front_acpowersupply_Filler.svg (79 lines)
│   │   │       │   ├── N540-12Z20G-SYS-D_front_RSP.svg (2323 lines)
│   │   │       │   ├── N540-12Z20G-SYS-D_front_dcpower.svg (237 lines)
│   │   │       │   ├── N540-24Q2C2DD-SYS_front_ports.svg (7214 lines)
│   │   │       │   ├── N540-24Q8L2DD-SYS_front_ports.svg (4832 lines)
│   │   │       │   ├── N540-24Q8L2DD-SYS_rear_fans.svg (167 lines)
│   │   │       │   ├── N540-24Z8Q2C-M-POWER-FILLERR.svg (94 lines)
│   │   │       │   ├── N540-28Z4C-SYS_frontports.svg (4304 lines)
│   │   │       │   ├── N540-6Z14S-SYS-D_port.svg (1090 lines)
│   │   │       │   ├── N540-6Z14S-SYS-D_power_module-dc_filler.svg (78 lines)
│   │   │       │   ├── N540-6Z18G-SYS-A_Ports.svg (2035 lines)
│   │   │       │   ├── N540-6Z18G-SYS-A_front_acpowersupply.svg (126 lines)
│   │   │       │   ├── N540-6Z18G-SYS-A_front_acpowersupply_filler.svg (74 lines)
│   │   │       │   ├── N540-6Z18G-SYS-A_front_ports.svg (3686 lines)
│   │   │       │   ├── N540-6Z18G-SYS-D_Ports.svg (2035 lines)
│   │   │       │   ├── N540-6Z18G-SYS-D_front_depowersupply.svg (658 lines)
│   │   │       │   ├── N540-6Z18G-SYS-D_front_depowersupply_filler.svg (78 lines)
│   │   │       │   ├── N540-6Z18G-SYS-D_front_ports.svg (3686 lines)
│   │   │       │   ├── N540-8Z12G-SYS-D_Ports.svg (1287 lines)
│   │   │       │   ├── N540-8Z16G-SYS_front_ports.svg (2592 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Fan.svg (203 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Fan_Filler.svg (89 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Front_Ports.svg (3442 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Power_Module-DC.svg (733 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Power_Module.svg (550 lines)
│   │   │       │   ├── N540-FH-AGG-SYS_Power_Module_Filler.svg (54 lines)
│   │   │       │   ├── N540-FH-CSR-SYS_Front_Port.svg (4937 lines)
│   │   │       │   ├── N540-PWR400-A-FILLER.svg (74 lines)
│   │   │       │   ├── N540-PWR400-A.svg (1100 lines)
│   │   │       │   ├── N540L-PSU-FIXED-D.svg (714 lines)
│   │   │       │   ├── N540L-PSU-FIXED-D_Filler.svg (78 lines)
│   │   │       │   ├── N540X-12Z16G-SYS-A_RSP.svg (4668 lines)
│   │   │       │   ├── N540X-12Z16G-SYS-D_Front_depowersupply.svg (658 lines)
│   │   │       │   ├── N540X-12Z16G-SYS-D_RSP.svg (4668 lines)
│   │   │       │   ├── N540X-16Z4G8Q2C-A-M-POWER-FILLER.svg (74 lines)
│   │   │       │   ├── N540X-16Z4G8Q2C-A_Front_Fan.svg (214 lines)
│   │   │       │   ├── N540X-16Z4G8Q2C-A_RSP.svg (6026 lines)
│   │   │       │   ├── N540X-16Z4G8Q2C-D_RSP.svg (6026 lines)
│   │   │       │   ├── N540X-16Z4G8Q2C-D_front_dcpowersupply.svg (406 lines)
│   │   │       │   ├── N540X-16Z8Q2C-D_front_RSP.svg (4914 lines)
│   │   │       │   ├── N540X-16Z8Q2C-D_front_dcpowersupply.svg (406 lines)
│   │   │       │   ├── N540X-16Z8Q2C-D_front_dcpowersupply_filler.svg (76 lines)
│   │   │       │   ├── N540X-4Z14G2Q_front_ports.svg (2251 lines)
│   │   │       │   ├── NC55-2KW-ACRV.svg (346 lines)
│   │   │       │   ├── NC55-2KW-ACRV_filler.svg (79 lines)
│   │   │       │   ├── NCS-57B1-5DSE-SYS_Front_ports.svg (8495 lines)
│   │   │       │   ├── NCS-57B1-5DSE-SYS_Rear_fan.svg (216 lines)
│   │   │       │   ├── NCS-57B1-5DSE-SYS_Rear_fan_filler.svg (79 lines)
│   │   │       │   ├── NCS-57B1-5DSE-SYS_Rear_powermodul_filler.svg (79 lines)
│   │   │       │   ├── NCS-57B1-5DSE-SYS_Rear_powermodule.svg (444 lines)
│   │   │       │   ├── NCS-57B1-6D24-SYS_Front_ports.svg (8768 lines)
│   │   │       │   ├── NCS-57C1-48Q6-SYS_front_port.svg (7837 lines)
│   │   │       │   ├── NCS-57C1-48Q6-SYS_power_module_filler.svg (75 lines)
│   │   │       │   ├── NCS-57D2-18DD-SYS_fan.svg (456 lines)
│   │   │       │   ├── NCS-57D2-18DD-SYS_fan_filler.svg (76 lines)
│   │   │       │   ├── NCS-57D2-18DD-SYS_front_ports.svg (23033 lines)
│   │   │       │   ├── ONS-CFP2.svg (135 lines)
│   │   │       │   ├── PSU1.4KW-ACPI_Filler.svg (63 lines)
│   │   │       │   ├── PSU2KW-DCPI.svg (517 lines)
│   │   │       │   ├── PSU4.8KW-DC100.svg (1832 lines)
│   │   │       │   ├── PSU4.8KW-DC100_Filler.svg (105 lines)
│   │   │       │   ├── PSU6.3KW-HV.svg (1551 lines)
│   │   │       │   ├── PSU6.3KW-HV_filler.svg (79 lines)
│   │   │       │   ├── QSFP-4.svg (209 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   └── SFP.svg (172 lines)
│   │   │       └── vertical/
│   │   │           ├── 8202-SYS_front_ports.svg (7915 lines)
│   │   │           ├── 8608-SYS_Front_86-MPA-14H2FH-M.svg (5323 lines)
│   │   │           ├── 8608-SYS_Front_86-MPA-24Z-M.svg (3826 lines)
│   │   │           ├── 8608-SYS_Front_86-MPA-4FH-M.svg (717 lines)
│   │   │           ├── 8608-SYS_MPA_Filler.svg (181 lines)
│   │   │           ├── 8608-SYS_RP.svg (719 lines)
│   │   │           ├── 8608-SYS_RP_Filler.svg (175 lines)
│   │   │           ├── 8800-LC-36FH.svg (12747 lines)
│   │   │           ├── 8800-LC-48H.svg (17863 lines)
│   │   │           ├── 8800-RP.svg (3709 lines)
│   │   │           ├── 8808-FC1-01.svg (480 lines)
│   │   │           ├── 8808-SYS-Fabric-Card.svg (88 lines)
│   │   │           ├── 8808-SYS-Fan-Tray.svg (1133 lines)
│   │   │           ├── 8808-SYS-Fan-Tray_filler.svg (78 lines)
│   │   │           ├── 8812-Fabric-Card.svg (335 lines)
│   │   │           ├── 8812-Fan-Tray.svg (1069 lines)
│   │   │           ├── 8812-Fan-Tray_filler.svg (78 lines)
│   │   │           ├── 8818-FC1.svg (379 lines)
│   │   │           ├── 8818-SYS-Fabric-Card.svg (88 lines)
│   │   │           ├── 8818-SYS-Fan-Tray.svg (1202 lines)
│   │   │           ├── 8818-SYS-Fan-Tray_filler.svg (78 lines)
│   │   │           ├── GLC.svg (191 lines)
│   │   │           ├── N540-12Z20G-SYS-A_Front_acpowersupply.svg (97 lines)
│   │   │           ├── N540-12Z20G-SYS-A_Front_acpowersupply_Filler.svg (79 lines)
│   │   │           ├── N540-12Z20G-SYS-D_front_RSP.svg (2323 lines)
│   │   │           ├── N540-12Z20G-SYS-D_front_dcpower.svg (237 lines)
│   │   │           ├── N540-24Z8Q2C-M-POWER-FILLERR.svg (94 lines)
│   │   │           ├── N540-6Z18G-SYS-A_front_acpowersupply.svg (126 lines)
│   │   │           ├── N540-6Z18G-SYS-A_front_ports.svg (3955 lines)
│   │   │           ├── N540-6Z18G-SYS-D_front_depowersupply.svg (659 lines)
│   │   │           ├── N540-6Z18G-SYS-D_front_ports.svg (3955 lines)
│   │   │           ├── NC55-2KW-ACRV.svg (370 lines)
│   │   │           ├── NC55-2KW-ACRV_filler.svg (90 lines)
│   │   │           ├── NCS-57B1-5DSE-SYS_Front_ports.svg (8921 lines)
│   │   │           ├── NCS-57B1-5DSE-SYS_Rear_fan.svg (216 lines)
│   │   │           ├── NCS-57B1-5DSE-SYS_Rear_powermodule.svg (454 lines)
│   │   │           ├── NCS-57B1-6D24-SYS_Front_ports.svg (9202 lines)
│   │   │           ├── ONS-CFP2.svg (135 lines)
│   │   │           ├── PSU2KW-DCPI.svg (518 lines)
│   │   │           ├── QSFP.svg (202 lines)
│   │   │           └── SFP.svg (199 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs5500/
│   │   ├── Cisco_NCS-57C3-MOD-HX_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57C3-MOD-HX_Router.json (158 lines)
│   │   │   └── images/
│   │   │       ├── NC57-C3-FAN2-FW_Rear_Core.svg (4016 lines)
│   │   │       └── NCS-57C3-MOD-SYS.svg (3899 lines)
│   │   ├── Cisco_NCS-57C3-MOD-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57C3-MOD-SYS_Router.json (158 lines)
│   │   │   └── images/
│   │   │       ├── NC57-C3-FAN2-FW_Rear_Core.svg (4016 lines)
│   │   │       └── NCS-57C3-MOD-S_Front_Core.svg (2775 lines)
│   │   ├── Cisco_NCS-57C3-MODS-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS-57C3-MODS-SYS_Router.json (158 lines)
│   │   │   └── images/
│   │   │       ├── NC57-C3-FAN2-FW_Rear_Core.svg (4016 lines)
│   │   │       └── NCS-57C3-MOD-S_Front_Core.svg (2775 lines)
│   │   ├── Cisco_NCS_540-24Z8Q2C-M_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-24Z8Q2C-M_Router.json (122 lines)
│   │   │   └── images/
│   │   │       ├── N540-24Z8Q2C-M_Front.svg (5558 lines)
│   │   │       └── N540-24Z8Q2C-M_Rear.svg (1804 lines)
│   │   ├── Cisco_NCS_540-ACC-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540-ACC-SYS_Router.json (114 lines)
│   │   │   └── images/
│   │   │       ├── N540-ACC-SYS_Front.svg (5576 lines)
│   │   │       └── N540-ACC-SYS_Rear.svg (1804 lines)
│   │   ├── Cisco_NCS_540X-ACC-SYS_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_540X-ACC-SYS_Router.json (114 lines)
│   │   │   └── images/
│   │   │       ├── N540X-ACC-SYS_Front.svg (5152 lines)
│   │   │       └── N540X-ACC-SYS_Rear.svg (1804 lines)
│   │   ├── Cisco_NCS_5501/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5501.json (108 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5501-Front-core.svg (2835 lines)
│   │   │       ├── NCS-5501-Front_filler.svg (79 lines)
│   │   │       └── NCS-5501_Rear_core.svg (353 lines)
│   │   ├── Cisco_NCS_5501-SE/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5501-SE.json (101 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5501-SE-Front-core.svg (2681 lines)
│   │   │       ├── NCS-5501-SE-Front-filler.svg (79 lines)
│   │   │       └── NCS-5501-SE-Rear.svg (1191 lines)
│   │   ├── Cisco_NCS_5502/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5502.json (128 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5502-Front-filler.svg (79 lines)
│   │   │       ├── NCS-5502-Rear-core.svg (322 lines)
│   │   │       └── NCS-5502_Front_core.svg (9389 lines)
│   │   ├── Cisco_NCS_5502-SE/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5502-SE.json (128 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5502-SE-Front-filler.svg (79 lines)
│   │   │       ├── NCS-5502-SE-Rear-core.svg (322 lines)
│   │   │       └── NCS-5502-SE_Front_core.svg (9400 lines)
│   │   ├── Cisco_NCS_5504/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5504.json (259 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5504-FRONT_CORE.svg (1542 lines)
│   │   │       └── NCS-5504-REAR_CORE.svg (1078 lines)
│   │   ├── Cisco_NCS_5508/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5508.json (349 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5508-Front_b.svg (634 lines)
│   │   │       └── NCS-5508-Rear_b.svg (1370 lines)
│   │   ├── Cisco_NCS_5516/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5516.json (416 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5516-Front-Core.svg (1409 lines)
│   │   │       └── ncs-5516-rear_core.svg (1222 lines)
│   │   ├── Cisco_NCS_55A1-24H/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-24H.json (112 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-24H_Front.svg (16387 lines)
│   │   │       └── NCS-55A1-24H_Rear_core.svg (454 lines)
│   │   ├── Cisco_NCS_55A1-24Q6H-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-24Q6H-S.json (110 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-24Q6H-S-Front_core.svg (3035 lines)
│   │   │       └── NCS-55A1-24Q6H-S-Rear_core.svg (1216 lines)
│   │   ├── Cisco_NCS_55A1-24Q6H-SS/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-24Q6H-SS.json (100 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-24Q6H-S-Rear_core.svg (1216 lines)
│   │   │       └── NCS-55A1-24Q6H-SS-Front_core.svg (4482 lines)
│   │   ├── Cisco_NCS_55A1-36H-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-36H-S.json (119 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-36H-S_Front.svg (20817 lines)
│   │   │       └── NCS-55A1-36H-S_Rear_core.svg (382 lines)
│   │   ├── Cisco_NCS_55A1-36H-SE-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-36H-SE-S.json (117 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-36H-SE_Front.svg (20817 lines)
│   │   │       └── NCS-55A1-36H-S_Rear_core.svg (382 lines)
│   │   ├── Cisco_NCS_55A1-48Q6H/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A1-48Q6H.json (110 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A1-48Q6H-Front_core.svg (3055 lines)
│   │   │       └── NCS-55A1-48Q6H-Rear_core.svg (1216 lines)
│   │   ├── Cisco_NCS_55A2-MOD-HD-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A2-MOD-HD-S.json (187 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A2-MOD-HD-S_Front_core.svg (5369 lines)
│   │   │       └── NCS-55A2-MOD-HD-S_Rear_core.svg (3488 lines)
│   │   ├── Cisco_NCS_55A2-MOD-HX-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A2-MOD-HX-S.json (179 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A2-MOD-HD-S_Front_core.svg (5369 lines)
│   │   │       └── NCS-55A2-MOD-HD-S_Rear_core.svg (3488 lines)
│   │   ├── Cisco_NCS_55A2-MOD-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A2-MOD-S.json (178 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A2-MOD-SE-S_Front_core.svg (5467 lines)
│   │   │       └── NCS-55A2-MOD-S_Rear_core.svg (3488 lines)
│   │   ├── Cisco_NCS_55A2-MOD-SE-H-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A2-MOD-SE-H-S.json (178 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A2-MOD-SE-S_Front_core.svg (5467 lines)
│   │   │       └── NCS-55A2-MOD-SE-S_Rear_core.svg (3488 lines)
│   │   ├── Cisco_NCS_55A2-MOD-SE-S/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_55A2-MOD-SE-S.json (178 lines)
│   │   │   └── images/
│   │   │       ├── NCS-55A2-MOD-SE-S_Front_core.svg (5467 lines)
│   │   │       └── NCS-55A2-MOD-SE-S_Rear_core.svg (3488 lines)
│   │   ├── Cisco_NCS_560-4_RSP4E_CC_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560-4_RSP4E_CC_Router.json (129 lines)
│   │   │   └── images/
│   │   │       └── NCS560-4-front_core.svg (910 lines)
│   │   ├── Cisco_NCS_560-4_RSP4_CC_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560-4_RSP4_CC_Router.json (129 lines)
│   │   │   └── images/
│   │   │       └── NCS560-4-front_core.svg (910 lines)
│   │   ├── Cisco_NCS_560-4_RSP4_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560-4_RSP4_Router.json (131 lines)
│   │   │   └── images/
│   │   │       ├── N560-Front.svg (1376 lines)
│   │   │       └── NCS560-4-front_core.svg (910 lines)
│   │   ├── Cisco_NCS_560-4_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560-4_Router.json (130 lines)
│   │   │   └── images/
│   │   │       └── NCS560-4-front_core.svg (910 lines)
│   │   ├── Cisco_NCS_560_Enhanced_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560_Enhanced_Router.json (185 lines)
│   │   │   └── images/
│   │   │       └── N560-Front.svg (1376 lines)
│   │   ├── Cisco_NCS_560_Router/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_560_Router.json (185 lines)
│   │   │   └── images/
│   │   │       └── N560-Front.svg (1376 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (1112 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (50334 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── A900-IMA8CS1Z-M.svg (1286 lines)
│   │   │       │   ├── A900-IMA8Z-L.svg (1604 lines)
│   │   │       │   ├── A900-IMA8Z.svg (7761 lines)
│   │   │       │   ├── A900-PWR1200-A.svg (1262 lines)
│   │   │       │   ├── A900-PWR1200-D.svg (1013 lines)
│   │   │       │   ├── A907-FAN.svg (664 lines)
│   │   │       │   ├── GLC.svg (190 lines)
│   │   │       │   ├── N540-24Z8Q2C-M-FAN-FILLER.svg (73 lines)
│   │   │       │   ├── N540-24Z8Q2C-M-Fan.svg (136 lines)
│   │   │       │   ├── N540-24Z8Q2C-M-POWER-FILLER.svg (74 lines)
│   │   │       │   ├── N540-24Z8Q2C-M_Front_power.svg (1100 lines)
│   │   │       │   ├── N540-24Z8Q2C-M_RP.svg (4619 lines)
│   │   │       │   ├── N540-ACC-SYS_RP.svg (4610 lines)
│   │   │       │   ├── N540-PWR400-D.svg (1092 lines)
│   │   │       │   ├── N540X-ACC-SYS_RP.svg (4590 lines)
│   │   │       │   ├── N560-4-FAN-H.svg (367 lines)
│   │   │       │   ├── N560-4-FAN-H_Filler.svg (74 lines)
│   │   │       │   ├── N560-4-PWR-FAN.svg (458 lines)
│   │   │       │   ├── N560-4-PWR-FAN_Filler.svg (74 lines)
│   │   │       │   ├── N560-4-RSP4.svg (1530 lines)
│   │   │       │   ├── N560-4-RSP4E.svg (1530 lines)
│   │   │       │   ├── N560-IMA-8Q4L.svg (2789 lines)
│   │   │       │   ├── N560-IMA1W.svg (1674 lines)
│   │   │       │   ├── N560-IMA2C-DD.svg (1639 lines)
│   │   │       │   ├── N560-IMA2C.svg (814 lines)
│   │   │       │   ├── N560-RSP4-E_Filler.svg (78 lines)
│   │   │       │   ├── N560-RSP4.svg (1612 lines)
│   │   │       │   ├── N9K-C9508-FAN.svg (39565 lines)
│   │   │       │   ├── N9K-PAC-3000W-B.svg (1084 lines)
│   │   │       │   ├── N9K-PUV-3000W-B.svg (1044 lines)
│   │   │       │   ├── NC55-1200W-ACFW-PWR-FILLER.svg (85 lines)
│   │   │       │   ├── NC55-1200W-ACFW.svg (483 lines)
│   │   │       │   ├── NC55-12X100GE-PROT.svg (5199 lines)
│   │   │       │   ├── NC55-18H18F-FILLER.svg (71 lines)
│   │   │       │   ├── NC55-18H18F.svg (19310 lines)
│   │   │       │   ├── NC55-24H12F-SE-FILLER.svg (74 lines)
│   │   │       │   ├── NC55-24H12F-SE.svg (19324 lines)
│   │   │       │   ├── NC55-24X100G-SE.svg (14275 lines)
│   │   │       │   ├── NC55-2KW-DCFW.svg (407 lines)
│   │   │       │   ├── NC55-32T16Q4H-A.svg (6164 lines)
│   │   │       │   ├── NC55-36X100G-FILLER.svg (74 lines)
│   │   │       │   ├── NC55-36X100G.svg (19022 lines)
│   │   │       │   ├── NC55-5504-FC.svg (1478 lines)
│   │   │       │   ├── NC55-5508-FC-Filler.svg (75 lines)
│   │   │       │   ├── NC55-5508-FC.svg (554 lines)
│   │   │       │   ├── NC55-5508-LC-Filler.svg (75 lines)
│   │   │       │   ├── NC55-5516-FAN.svg (59625 lines)
│   │   │       │   ├── NC55-6X200-DWDM-S.svg (5469 lines)
│   │   │       │   ├── NC55-A1-FAN-FW.svg (1691 lines)
│   │   │       │   ├── NC55-MOD-A-SE-S.svg (1993 lines)
│   │   │       │   ├── NC55-MPA-12T-S.svg (2543 lines)
│   │   │       │   ├── NC55-MPA-12T-S_filler.svg (73 lines)
│   │   │       │   ├── NC55-MPA-1TH2H-S.svg (2501 lines)
│   │   │       │   ├── NC55-MPA-1TH2H-S_filler.svg (85 lines)
│   │   │       │   ├── NC55-MPA-2TH-S.svg (1706 lines)
│   │   │       │   ├── NC55-MPA-4H-S.svg (3425 lines)
│   │   │       │   ├── NC55-OIP-02.svg (2441 lines)
│   │   │       │   ├── NC55-PS-FILLER.svg (75 lines)
│   │   │       │   ├── NC55-PSM-FILLER.svg (196 lines)
│   │   │       │   ├── NC55-PWR-3KW-2HV.svg (1824 lines)
│   │   │       │   ├── NC55-PWR-3KW-AC-FILLER.svg (75 lines)
│   │   │       │   ├── NC55-PWR-3KW-AC.svg (863 lines)
│   │   │       │   ├── NC55-PWR-3KW-DC.svg (1325 lines)
│   │   │       │   ├── NC55-RP-E.svg (916 lines)
│   │   │       │   ├── NC55-RP-E_filler.svg (72 lines)
│   │   │       │   ├── NC55-RP-FILLER.svg (72 lines)
│   │   │       │   ├── NC55-RP.svg (955 lines)
│   │   │       │   ├── NC55-RP2-E.svg (1006 lines)
│   │   │       │   ├── NC55-SC-FILLER.svg (71 lines)
│   │   │       │   ├── NC55-SC.svg (431 lines)
│   │   │       │   ├── NC57-18DD-SE.svg (9741 lines)
│   │   │       │   ├── NC57-24DD.svg (17405 lines)
│   │   │       │   ├── NC57-36H-SE.svg (12516 lines)
│   │   │       │   ├── NC57-36H6D-S.svg (8040 lines)
│   │   │       │   ├── NC57-48Q2D-S.svg (12644 lines)
│   │   │       │   ├── NC57-C3-FAN2-FW-Rear_Fan-Big-Filler.svg (94 lines)
│   │   │       │   ├── NC57-C3-FAN2-FW-Rear_Fan-Big.svg (4552 lines)
│   │   │       │   ├── NC57-C3-FAN2-FW-Rear_Fan-Small-Filler.svg (113 lines)
│   │   │       │   ├── NC57-C3-FAN2-FW-Rear_Fan-Small.svg (4529 lines)
│   │   │       │   ├── NC57-MOD-RP2-E-Filler.svg (94 lines)
│   │   │       │   ├── NC57-MOD-RP2-E.svg (1048 lines)
│   │   │       │   ├── NC57-MOD-S.svg (3826 lines)
│   │   │       │   ├── NC57-MPA-12L-S.svg (1116 lines)
│   │   │       │   ├── NC57-MPA-1FH1D-S.svg (1577 lines)
│   │   │       │   ├── NC57-MPA-2D4H-S-Filler.svg (94 lines)
│   │   │       │   ├── NC57-MPA-2D4H-S.svg (1268 lines)
│   │   │       │   ├── NCS-5501-Front-ports.svg (6925 lines)
│   │   │       │   ├── NCS-5501-RP.svg (124 lines)
│   │   │       │   ├── NCS-5501-SE-FAN.svg (484 lines)
│   │   │       │   ├── NCS-5501-SE-RP.svg (8647 lines)
│   │   │       │   ├── NCS-5501-SE-power.svg (977 lines)
│   │   │       │   ├── NCS-5501-SE_Front_ports.svg (6405 lines)
│   │   │       │   ├── NCS-5501_RP.svg (300 lines)
│   │   │       │   ├── NCS-5501_Rear_fan.svg (648 lines)
│   │   │       │   ├── NCS-5501_Rear_fan_filler.svg (79 lines)
│   │   │       │   ├── NCS-5501_Rear_powersupply.svg (384 lines)
│   │   │       │   ├── NCS-5501_Rear_powersupply_filler.svg (79 lines)
│   │   │       │   ├── NCS-5502-RP.svg (29283 lines)
│   │   │       │   ├── NCS-5502-Rear-fan-filler.svg (79 lines)
│   │   │       │   ├── NCS-5502-Rear-fan.svg (3805 lines)
│   │   │       │   ├── NCS-5502-Rear-powersupply-filler.svg (79 lines)
│   │   │       │   ├── NCS-5502-Rear-powersupply.svg (493 lines)
│   │   │       │   ├── NCS-5502-SE-RP.svg (29283 lines)
│   │   │       │   ├── NCS-5502_Rear_fan.svg (3807 lines)
│   │   │       │   ├── NCS-5516-FC.svg (433 lines)
│   │   │       │   ├── NCS-55A1-24H_Front_RP.svg (15951 lines)
│   │   │       │   ├── NCS-55A1-36H-S-PWR-Filler.svg (74 lines)
│   │   │       │   ├── NCS-55A1-36H-S-RP.svg (17299 lines)
│   │   │       │   ├── NCS-55A1-36H-SE-S-RP.svg (17299 lines)
│   │   │       │   ├── NCS-55A1-36H-S_Rear_FAN-Filler.svg (74 lines)
│   │   │       │   ├── NCS-55A2-MOD-S-RP.svg (5828 lines)
│   │   │       │   ├── NCS-55A2-MOD-S.svg (5827 lines)
│   │   │       │   ├── NCS-55A2-MOD-SE-S_RP.svg (8912 lines)
│   │   │       │   ├── NCS-55A2-MOD-S_Rear_Fan_filler.svg (97 lines)
│   │   │       │   ├── NCS-57C3-MOD-SE-S_Middle_Card.svg (10945 lines)
│   │   │       │   ├── NCS-57C3-MOD-S_Middle_Card.svg (11122 lines)
│   │   │       │   ├── NCS4200-1T16G-PS.svg (1596 lines)
│   │   │       │   ├── NCS4200-2H-PQ.svg (818 lines)
│   │   │       │   ├── NCS4200-8T-PS.svg (9281 lines)
│   │   │       │   ├── NCS55-5504-FAN.svg (25634 lines)
│   │   │       │   ├── NCS55-5504-FAN_Filler.svg (79 lines)
│   │   │       │   ├── NCS55-A2-FAN-FW.svg (122 lines)
│   │   │       │   ├── NCS55A2-FILLER-PWR.svg (85 lines)
│   │   │       │   ├── NCS560-4-FILLER-RSP.svg (71 lines)
│   │   │       │   ├── NCS560-FILLER-FT.svg (299 lines)
│   │   │       │   ├── NCS560-FILLER-LC.svg (131 lines)
│   │   │       │   ├── NCS560-FILLER-PT.svg (132 lines)
│   │   │       │   ├── NCS560-FILLER-RSP.svg (145 lines)
│   │   │       │   ├── NS55-5508-FAN-FILLER.svg (407 lines)
│   │   │       │   ├── NS55-5508-FAN.svg (39567 lines)
│   │   │       │   ├── ONS-CFP2.svg (135 lines)
│   │   │       │   ├── Power_Module-Filler.svg (113 lines)
│   │   │       │   ├── Power_Module.svg (379 lines)
│   │   │       │   ├── QSFP-4.svg (208 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   └── SFP.svg (172 lines)
│   │   │       └── vertical/
│   │   │           ├── A900-IMA8CS1Z-M.svg (1286 lines)
│   │   │           ├── A900-IMA8Z.svg (7761 lines)
│   │   │           ├── A900-PWR1200-A.svg (1322 lines)
│   │   │           ├── A900-PWR1200-D.svg (1014 lines)
│   │   │           ├── A907-FAN.svg (664 lines)
│   │   │           ├── GLC.svg (191 lines)
│   │   │           ├── N540-PWR400-D.svg (1103 lines)
│   │   │           ├── N560-4-FAN-H.svg (378 lines)
│   │   │           ├── N560-4-FAN-H_Filler.svg (79 lines)
│   │   │           ├── N560-4-PWR-FAN.svg (475 lines)
│   │   │           ├── N560-4-PWR-FAN_Filler.svg (79 lines)
│   │   │           ├── N560-4-RSP4.svg (1581 lines)
│   │   │           ├── N560-4-RSP4E.svg (1581 lines)
│   │   │           ├── N560-IMA-8Q4L.svg (2849 lines)
│   │   │           ├── N560-IMA1W.svg (1676 lines)
│   │   │           ├── N560-IMA2C.svg (821 lines)
│   │   │           ├── N560-RSP4.svg (1621 lines)
│   │   │           ├── N9K-C9508-FAN.svg (42027 lines)
│   │   │           ├── N9K-PAC-3000W-B.svg (949 lines)
│   │   │           ├── N9K-PUV-3000W-B.svg (1045 lines)
│   │   │           ├── NC55-1200W-ACFW-PWR-FILLER.svg (78 lines)
│   │   │           ├── NC55-1200W-ACFW.svg (484 lines)
│   │   │           ├── NC55-12X100GE-PROT.svg (5199 lines)
│   │   │           ├── NC55-18H18F-FILLER.svg (75 lines)
│   │   │           ├── NC55-18H18F.svg (19359 lines)
│   │   │           ├── NC55-24H12F-SE-FILLER.svg (75 lines)
│   │   │           ├── NC55-24H12F-SE.svg (19356 lines)
│   │   │           ├── NC55-24X100G-SE.svg (14292 lines)
│   │   │           ├── NC55-2KW-DCFW.svg (448 lines)
│   │   │           ├── NC55-32T16Q4H-A.svg (6234 lines)
│   │   │           ├── NC55-36X100G-FILLER.svg (75 lines)
│   │   │           ├── NC55-36X100G.svg (19023 lines)
│   │   │           ├── NC55-5504-FC.svg (1475 lines)
│   │   │           ├── NC55-5508-FC-FILLER.svg (74 lines)
│   │   │           ├── NC55-5508-FC.svg (553 lines)
│   │   │           ├── NC55-5516-FAN.svg (59624 lines)
│   │   │           ├── NC55-6X200-DWDM-S.svg (5470 lines)
│   │   │           ├── NC55-A1-FAN-FW.svg (1692 lines)
│   │   │           ├── NC55-MPA-12T-S.svg (2581 lines)
│   │   │           ├── NC55-MPA-12T-S_filler.svg (78 lines)
│   │   │           ├── NC55-MPA-1TH2H-S.svg (2518 lines)
│   │   │           ├── NC55-MPA-2TH-S.svg (1726 lines)
│   │   │           ├── NC55-MPA-4H-S.svg (3441 lines)
│   │   │           ├── NC55-PS-FILLER.svg (72 lines)
│   │   │           ├── NC55-PSM-FILLER.svg (196 lines)
│   │   │           ├── NC55-PWR-3KW-2HV.svg (1835 lines)
│   │   │           ├── NC55-PWR-3KW-AC-FILLER.svg (74 lines)
│   │   │           ├── NC55-PWR-3KW-AC.svg (862 lines)
│   │   │           ├── NC55-PWR-3KW-DC.svg (1324 lines)
│   │   │           ├── NC55-RP-E.svg (936 lines)
│   │   │           ├── NC55-RP-E_filler.svg (73 lines)
│   │   │           ├── NC55-RP-FILLER.svg (73 lines)
│   │   │           ├── NC55-RP.svg (956 lines)
│   │   │           ├── NC55-RP2-E.svg (1025 lines)
│   │   │           ├── NC55-SC-FILLER.svg (73 lines)
│   │   │           ├── NC55-SC.svg (449 lines)
│   │   │           ├── NC57-18DD-SE.svg (9763 lines)
│   │   │           ├── NC57-24DD.svg (17461 lines)
│   │   │           ├── NCS-5501-RP.svg (124 lines)
│   │   │           ├── NCS-5501-SE-FAN.svg (484 lines)
│   │   │           ├── NCS-5501-SE-RP.svg (8740 lines)
│   │   │           ├── NCS-5501-SE-power.svg (977 lines)
│   │   │           ├── NCS-5501-SE_Front_ports.svg (6451 lines)
│   │   │           ├── NCS-5501_Rear_fan.svg (648 lines)
│   │   │           ├── NCS-5501_Rear_fan_filler.svg (79 lines)
│   │   │           ├── NCS-5501_Rear_powersupply.svg (384 lines)
│   │   │           ├── NCS-5501_Rear_powersupply_filler.svg (79 lines)
│   │   │           ├── NCS-5502-RP.svg (29283 lines)
│   │   │           ├── NCS-5502-Rear-fan-filler.svg (79 lines)
│   │   │           ├── NCS-5502-Rear-fan.svg (3807 lines)
│   │   │           ├── NCS-5502-Rear-powersupply-filler.svg (79 lines)
│   │   │           ├── NCS-5502-Rear-powersupply.svg (493 lines)
│   │   │           ├── NCS-5502-SE-RP.svg (29283 lines)
│   │   │           ├── NCS-5502_Rear_fan.svg (3807 lines)
│   │   │           ├── NCS-5516-FC.svg (431 lines)
│   │   │           ├── NCS-55A1-24H_Front_RP.svg (15976 lines)
│   │   │           ├── NCS-55A1-36H-S-PWR-Filler.svg (79 lines)
│   │   │           ├── NCS-55A1-36H-S-RP.svg (17367 lines)
│   │   │           ├── NCS-55A1-36H-SE-S-RP.svg (17367 lines)
│   │   │           ├── NCS-55A1-36H-S_Rear_FAN-Filler.svg (79 lines)
│   │   │           ├── NCS-55A2-MOD-S-RP.svg (5874 lines)
│   │   │           ├── NCS-55A2-MOD-S.svg (5873 lines)
│   │   │           ├── NCS-55A2-MOD-S_Rear_Fan_filler.svg (98 lines)
│   │   │           ├── NCS4200-2H-PQ.svg (825 lines)
│   │   │           ├── NCS55-5504-FAN.svg (25633 lines)
│   │   │           ├── NCS55-5504-FAN_Filler.svg (74 lines)
│   │   │           ├── NCS55-A2-FAN-FW.svg (123 lines)
│   │   │           ├── NCS55A2-FILLER-PWR.svg (78 lines)
│   │   │           ├── NCS560-4-FILLER-RSP.svg (79 lines)
│   │   │           ├── NCS560-FILLER-FT.svg (300 lines)
│   │   │           ├── NCS560-FILLER-LC.svg (132 lines)
│   │   │           ├── NCS560-FILLER-PT.svg (123 lines)
│   │   │           ├── NCS560-FILLER-RSP.svg (145 lines)
│   │   │           ├── NS55-5508-FAN-FILLER.svg (406 lines)
│   │   │           ├── NS55-5508-FAN.svg (39567 lines)
│   │   │           └── ONS-CFP2.svg (135 lines)
│   │   ├── assembly.xml (25 lines)
│   │   ├── package.profile.js (78 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs5k/
│   │   ├── Cisco_NCS_5001/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5001.json (130 lines)
│   │   │   └── images/
│   │   │       ├── NCS5001-Front.svg (2677 lines)
│   │   │       └── NCS5001-Rear.svg (515 lines)
│   │   ├── Cisco_NCS_5002/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5002.json (129 lines)
│   │   │   └── images/
│   │   │       ├── NCS5002-Front.svg (6006 lines)
│   │   │       └── NCS5002-Rear.svg (690 lines)
│   │   ├── Cisco_NCS_5011/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_5011.json (129 lines)
│   │   │   └── images/
│   │   │       ├── NCS-5011_Rear.svg (261 lines)
│   │   │       └── NCS5011-Front-Core.svg (5427 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (671 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (6350 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── NC5K-PAC-650W-BK-FILLER.svg (74 lines)
│   │   │       │   ├── NC5K-PAC-650W-BK.svg (463 lines)
│   │   │       │   ├── NC5K-PAC-650W-FR-FILLER.svg (74 lines)
│   │   │       │   ├── NC5K-PAC-650W-FR.svg (458 lines)
│   │   │       │   ├── NCS-5002-FN-BK-FILLER.svg (74 lines)
│   │   │       │   ├── NCS-5002-FN-BK.svg (4035 lines)
│   │   │       │   ├── NCS-5011-FN-FR.svg (95 lines)
│   │   │       │   ├── NCS-5011-FN-FR_FILLER.svg (79 lines)
│   │   │       │   ├── NCS-5011-RP.svg (15866 lines)
│   │   │       │   ├── NCS-5011-Rear-RP.svg (306 lines)
│   │   │       │   ├── NCS-5011-Rear-rp-filler.svg (79 lines)
│   │   │       │   ├── NCS5001-FN-FR-FILLER.svg (74 lines)
│   │   │       │   ├── NCS5001-FN-FR.svg (1705 lines)
│   │   │       │   ├── NCS5001_Front_Ports.svg (8701 lines)
│   │   │       │   ├── NCS5002_Front_Ports.svg (15488 lines)
│   │   │       │   ├── QSFP.svg (173 lines)
│   │   │       │   └── SFP.svg (172 lines)
│   │   │       └── vertical/
│   │   │           ├── NC5K-PAC-650W-BK-FILLER.svg (79 lines)
│   │   │           ├── NC5K-PAC-650W-BK.svg (464 lines)
│   │   │           ├── NC5K-PAC-650W-FR-FILLER.svg (79 lines)
│   │   │           ├── NC5K-PAC-650W-FR.svg (462 lines)
│   │   │           ├── NCS-5002-FN-BK-FILLER.svg (79 lines)
│   │   │           ├── NCS-5002-FN-BK.svg (4069 lines)
│   │   │           ├── NCS-5011-FN-FR.svg (95 lines)
│   │   │           ├── NCS-5011-FN-FR_FILLER.svg (79 lines)
│   │   │           ├── NCS-5011-Rear-RP.svg (306 lines)
│   │   │           ├── NCS-5011-Rear-rp-filler.svg (79 lines)
│   │   │           ├── NCS5001-FN-FR-FILLER.svg (79 lines)
│   │   │           ├── NCS5001-FN-FR.svg (1706 lines)
│   │   │           ├── NCS5001_Front_Ports.svg (8502 lines)
│   │   │           └── NCS5002_Front_Ports.svg (15576 lines)
│   │   ├── assembly.xml (25 lines)
│   │   └── pom.xml (84 lines)
│   ├── ncs6k/
│   │   ├── Cisco_NCS_6000/
│   │   │   ├── data/
│   │   │   │   └── Cisco_NCS_6000.json (243 lines)
│   │   │   └── images/
│   │   │       ├── NCS-6008-Front.svg (6097 lines)
│   │   │       └── NCS-6008-Rear.svg (26480 lines)
│   │   ├── js/
│   │   │   └── ChassisViewMetaDataV2.js (639 lines)
│   │   ├── pluggables/
│   │   │   ├── data/
│   │   │   │   └── pluggables.json (3761 lines)
│   │   │   └── images/
│   │   │       ├── horizontal/
│   │   │       │   ├── CPAK.svg (170 lines)
│   │   │       │   ├── NC6-FC.svg (9386 lines)
│   │   │       │   ├── NC6-RP.svg (4291 lines)
│   │   │       │   ├── NC6-RP_filler.svg (90 lines)
│   │   │       │   ├── NCS-6008-FANTRAY.svg (331 lines)
│   │   │       │   ├── NCS-6008-Power-Tray.svg (701 lines)
│   │   │       │   ├── NCS6008-FAN-FILLER.svg (84 lines)
│   │   │       │   ├── NCS6008-LC-FILLER.svg (75 lines)
│   │   │       │   ├── NCS6008-PWR-FILLER.svg (84 lines)
│   │   │       │   ├── NCS6K-FC-FILLER.svg (89 lines)
│   │   │       │   ├── P-L-10X100G-F-K.svg (3196 lines)
│   │   │       │   ├── P-L-10X100G-F-P.svg (3189 lines)
│   │   │       │   ├── P-L-60X10G-F-P.svg (4139 lines)
│   │   │       │   ├── PWR-3KW-AC-V2.svg (1522 lines)
│   │   │       │   └── SFP.svg (172 lines)
│   │   │       └── vertical/
│   │   │           ├── CPAK.svg (170 lines)
│   │   │           ├── NC6-FC.svg (9353 lines)
│   │   │           ├── NC6-RP.svg (4280 lines)
│   │   │           ├── NC6-RP_filler.svg (85 lines)
│   │   │           ├── NCS-6008-FANTRAY.svg (331 lines)
│   │   │           ├── NCS-6008-Power-Tray.svg (701 lines)
│   │   │           ├── NCS6008-FAN-FILLER.svg (84 lines)
│   │   │           ├── NCS6008-LC-FILLER.svg (76 lines)
│   │   │           ├── NCS6008-PWR-FILLER.svg (84 lines)
│   │   │           ├── NCS6K-FC-FILLER.svg (90 lines)
│   │   │           ├── P-L-10X100G-F-K.svg (2865 lines)
│   │   │           ├── P-L-10X100G-F-P.svg (2866 lines)
│   │   │           ├── P-L-60X10G-F-P.svg (4138 lines)
│   │   │           ├── PWR-3KW-AC-V2.svg (1522 lines)
│   │   │           └── SFP.svg (176 lines)
│   │   ├── assembly.xml (25 lines)
│   │   └── pom.xml (84 lines)
│   ├── rack/
│   │   ├── Cisco_R42610/
│   │   │   ├── data/
│   │   │   │   └── Cisco_R42610.json (192 lines)
│   │   │   └── images/
│   │   │       ├── Cisco_R42610_Front.svg (1123 lines)
│   │   │       ├── RACK_Front.svg (1071 lines)
│   │   │       └── Virtual-Rack.svg (11 lines)
│   │   ├── RACK/
│   │   │   ├── data/
│   │   │   │   └── RACK.json (215 lines)
│   │   │   └── images/
│   │   │       ├── RACK_Front.svg (1071 lines)
│   │   │       ├── Virtual-Rack-CRS.svg (59 lines)
│   │   │       ├── Virtual-Rack.svg (11 lines)
│   │   │       └── virtualrack_asr9000.svg (31 lines)
│   │   ├── assembly.xml (19 lines)
│   │   └── pom.xml (83 lines)
│   ├── staticFiles/
│   │   ├── Temp/
│   │   │   ├── scripts/
│   │   │   │   ├── baseUINeighborView.sh (46 lines)
│   │   │   │   ├── baseUINeighborView.sql (34 lines)
│   │   │   │   ├── baseui_usergroup_upgrade.sh (46 lines)
│   │   │   │   ├── chassisview_rbac.sh (46 lines)
│   │   │   │   ├── chassisview_rbac.sql (257 lines)
│   │   │   │   ├── usergroup.sql (23 lines)
│   │   │   │   └── usergroup_update.sql (110 lines)
│   │   │   └── webacs/
│   │   │       └── WEB-INF/
│   │   │           └── classes/
│   │   │               ├── chassis_ui_wap_rs.xml (55 lines)
│   │   │               └── ems_wap_rs.xml (56 lines)
│   │   ├── conf/
│   │   │   ├── xmp_data/
│   │   │   │   ├── nms_chassisview_system_data.xml (124 lines)
│   │   │   │   └── nms_user_group_system_data.xml (1430 lines)
│   │   │   └── ems-context.xml (28 lines)
│   │   ├── jsp/
│   │   │   ├── buildNo.jsp (8 lines)
│   │   │   ├── version.jsp (8 lines)
│   │   │   └── versionData.jsp (9 lines)
│   │   ├── properties/
│   │   │   ├── OpticalDevices.properties (1 lines)
│   │   │   └── fileLocator.properties (1 lines)
│   │   ├── assembly.xml (71 lines)
│   │   └── pom.xml (41 lines)
│   ├── .gitignore (5 lines)
│   ├── .project (11 lines)
│   ├── assembly.xml (17 lines)
│   └── pom.xml (47 lines)
├── ems/
│   ├── ems-api/
│   │   ├── src/
│   │   │   └── main/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           └── nms/
│   │   │       │               ├── chassisview/
│   │   │       │               │   └── physicalroute/
│   │   │       │               │       ├── actions/
│   │   │       │               │       │   └── handlers/
│   │   │       │               │       │       └── LaunchPhysicalRouteActionHandler.java (95 lines)
│   │   │       │               │       ├── dto/
│   │   │       │               │       │   ├── PhysicalRouteConnectionDTO.java (44 lines)
│   │   │       │               │       │   ├── PhysicalRouteDTO.java (33 lines)
│   │   │       │               │       │   ├── PhysicalRouteDeviceRoleEnum.java (8 lines)
│   │   │       │               │       │   ├── PhysicalRouteLinkDTO.java (75 lines)
│   │   │       │               │       │   ├── PhysicalRoutePathDTO.java (53 lines)
│   │   │       │               │       │   ├── PhysicalRoutePortDTO.java (78 lines)
│   │   │       │               │       │   └── PhysicalRoutePortRoleEnum.java (7 lines)
│   │   │       │               │       └── service/
│   │   │       │               │           ├── BasePhysicalRouteProvider.java (23 lines)
│   │   │       │               │           ├── PhysicalRouteProvider.java (10 lines)
│   │   │       │               │           ├── PhysicalRouteRestService.java (12 lines)
│   │   │       │               │           └── PhysicalRouteRestServiceImpl.java (85 lines)
│   │   │       │               └── ems/
│   │   │       │                   └── rest/
│   │   │       │                       └── service/
│   │   │       │                           ├── BaseEmsRestServiceProvider.java (124 lines)
│   │   │       │                           ├── EmsRestService.java (28 lines)
│   │   │       │                           ├── EmsRestServiceImpl.java (137 lines)
│   │   │       │                           ├── EmsRestServiceProvider.java (15 lines)
│   │   │       │                           └── EmsRestUtil.java (11 lines)
│   │   │       └── resources/
│   │   │           └── META-INF/
│   │   │               └── spring/
│   │   │                   ├── ems-context.xml (28 lines)
│   │   │                   └── ems_wap_rs.xml (56 lines)
│   │   ├── .gitignore (2 lines)
│   │   └── pom.xml (141 lines)
│   └── ems-ui/
│       ├── src/
│       │   ├── WEB-INF/
│       │   │   └── wro.xml (31 lines)
│       │   └── storm/
│       │       ├── ems/
│       │       │   ├── config/
│       │       │   │   └── patchcord/
│       │       │   │       ├── nls/
│       │       │   │       │   ├── en/
│       │       │   │       │   │   └── patchcord.js (21 lines)
│       │       │   │       │   ├── ja/
│       │       │   │       │   │   └── patchcord.js (21 lines)
│       │       │   │       │   └── patchcord.js (25 lines)
│       │       │   │       └── patchcord.js (748 lines)
│       │       │   ├── metadata/
│       │       │   │   ├── cvEmsTabs.json (102 lines)
│       │       │   │   ├── cvSubTabs.json (136 lines)
│       │       │   │   ├── emsTabs.json (17 lines)
│       │       │   │   ├── interfaceTypeProperty.json (516 lines)
│       │       │   │   ├── neData.json (20 lines)
│       │       │   │   └── tabs.json (41 lines)
│       │       │   ├── neinfo/
│       │       │   │   ├── actiondelegations/
│       │       │   │   │   ├── addpatchcord/
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── AddPatchcord.js (15 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── AddPatchcord.js (15 lines)
│       │       │   │   │   │   │   └── AddPatchcord.js (19 lines)
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── index.html (88 lines)
│       │       │   │   │   │   └── AddPatchcord.js (421 lines)
│       │       │   │   │   └── provisioncard/
│       │       │   │   │       ├── data/
│       │       │   │   │       │   └── cards.json (23 lines)
│       │       │   │   │       ├── nls/
│       │       │   │   │       │   ├── en/
│       │       │   │   │       │   │   └── ProvisionCard.js (20 lines)
│       │       │   │   │       │   ├── ja/
│       │       │   │   │       │   │   └── ProvisionCard.js (19 lines)
│       │       │   │   │       │   └── ProvisionCard.js (22 lines)
│       │       │   │   │       ├── templates/
│       │       │   │   │       │   ├── AddCard.html (107 lines)
│       │       │   │   │       │   └── GridItemWidget.html (9 lines)
│       │       │   │   │       ├── AddCard.js (176 lines)
│       │       │   │   │       ├── CardConfigActions.js (67 lines)
│       │       │   │   │       ├── CardUtil.js (76 lines)
│       │       │   │   │       ├── GridItemWidget.js (95 lines)
│       │       │   │   │       └── TableWidget.js (151 lines)
│       │       │   │   ├── metadata/
│       │       │   │   │   ├── neData.json (20 lines)
│       │       │   │   │   └── tabs.json (21 lines)
│       │       │   │   ├── nls/
│       │       │   │   │   ├── en/
│       │       │   │   │   │   └── NEInfo.js (15 lines)
│       │       │   │   │   ├── ja/
│       │       │   │   │   │   └── NEInfo.js (18 lines)
│       │       │   │   │   ├── ko/
│       │       │   │   │   │   └── NEInfo.js (13 lines)
│       │       │   │   │   └── NEInfo.js (22 lines)
│       │       │   │   ├── tabs/
│       │       │   │   │   ├── alarmstab/
│       │       │   │   │   │   ├── data/
│       │       │   │   │   │   │   └── alarms.json (38 lines)
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── AlarmsTab.js (16 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── AlarmsTab.js (16 lines)
│       │       │   │   │   │   │   └── AlarmsTab.js (20 lines)
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   ├── alarmSeverity.html (83 lines)
│       │       │   │   │   │   │   ├── alarmsTab.html (4 lines)
│       │       │   │   │   │   │   └── donutChart.html (31 lines)
│       │       │   │   │   │   ├── AlarmSeverity.js (141 lines)
│       │       │   │   │   │   ├── AlarmsTab.js (338 lines)
│       │       │   │   │   │   └── donutChart.js (180 lines)
│       │       │   │   │   ├── circuitstab/
│       │       │   │   │   │   ├── data/
│       │       │   │   │   │   │   └── circuits.json (56 lines)
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── CircuitsTab.js (10 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── CircuitsTab.js (10 lines)
│       │       │   │   │   │   │   └── CircuitsTab.js (14 lines)
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── circuitsTab.html (3 lines)
│       │       │   │   │   │   └── CircuitsTab.js (355 lines)
│       │       │   │   │   ├── configurationArchivetab/
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── ConfigurationArchiveTabView.html (3 lines)
│       │       │   │   │   │   └── ConfigurationArchiveTab.js (30 lines)
│       │       │   │   │   ├── configurationtab/
│       │       │   │   │   │   ├── metadata/
│       │       │   │   │   │   │   ├── configlets.json (19 lines)
│       │       │   │   │   │   │   └── tabs.json (26 lines)
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── ConfigurationTab.js (3 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── ConfigurationTab.js (3 lines)
│       │       │   │   │   │   │   └── ConfigurationTab.js (7 lines)
│       │       │   │   │   │   ├── ConfigurationTab.js (131 lines)
│       │       │   │   │   │   └── Example.js (123 lines)
│       │       │   │   │   ├── imagetab/
│       │       │   │   │   │   └── ImageTab.js (76 lines)
│       │       │   │   │   ├── interfacetab/
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── InterfaceTab.js (22 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── InterfaceTab.js (22 lines)
│       │       │   │   │   │   │   └── InterfaceTab.js (26 lines)
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── interfaceTab.html (49 lines)
│       │       │   │   │   │   └── InterfaceTab.js (671 lines)
│       │       │   │   │   ├── inventorytab/
│       │       │   │   │   │   ├── data/
│       │       │   │   │   │   │   └── inventory.json (459 lines)
│       │       │   │   │   │   ├── nls/
│       │       │   │   │   │   │   ├── en/
│       │       │   │   │   │   │   │   └── InventoryTab.js (12 lines)
│       │       │   │   │   │   │   ├── ja/
│       │       │   │   │   │   │   │   └── InventoryTab.js (12 lines)
│       │       │   │   │   │   │   └── InventoryTab.js (16 lines)
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── inventoryTab.html (13 lines)
│       │       │   │   │   │   └── InventoryTab.js (548 lines)
│       │       │   │   │   ├── performancetab/
│       │       │   │   │   │   ├── templates/
│       │       │   │   │   │   │   └── performanceTab.html (71 lines)
│       │       │   │   │   │   └── PerformanceTab.js (425 lines)
│       │       │   │   │   └── performancetab_cBR8/
│       │       │   │   │       ├── nls/
│       │       │   │   │       │   ├── en/
│       │       │   │   │       │   │   └── performanceTab.js (31 lines)
│       │       │   │   │       │   ├── ja/
│       │       │   │   │       │   │   └── performanceTab.js (31 lines)
│       │       │   │   │       │   └── performanceTab.js (35 lines)
│       │       │   │   │       ├── CPEHistory.js (126 lines)
│       │       │   │   │       ├── CPEHistroy.js (133 lines)
│       │       │   │   │       ├── DSChannelUtilization.js (116 lines)
│       │       │   │   │       ├── FanStatus.js (122 lines)
│       │       │   │   │       ├── FiberNodeDSUtilization.js (124 lines)
│       │       │   │   │       ├── FiberNodeUSUtilization.js (124 lines)
│       │       │   │   │       ├── IPv6NeighborStatistics.js (48 lines)
│       │       │   │   │       ├── Ipv4ARPStatistics.js (48 lines)
│       │       │   │   │       ├── LCUtilizationDownstream.js (124 lines)
│       │       │   │   │       ├── LCUtilizationUpStream.js (124 lines)
│       │       │   │   │       ├── LineCardsInstalled.js (50 lines)
│       │       │   │   │       ├── MDDSSGUtilization.js (121 lines)
│       │       │   │   │       ├── MDUSSGUtilization.js (122 lines)
│       │       │   │   │       ├── ModemHistory.js (137 lines)
│       │       │   │   │       ├── PowerSupplyStatus.js (127 lines)
│       │       │   │   │       ├── SUP.js (159 lines)
│       │       │   │   │       ├── USChannelUtilization.js (115 lines)
│       │       │   │   │       └── Voice.js (125 lines)
│       │       │   │   ├── templates/
│       │       │   │   │   ├── EMSAccordionContainer.html (72 lines)
│       │       │   │   │   ├── EMSAccordionPane.html (9 lines)
│       │       │   │   │   └── index.html (154 lines)
│       │       │   │   ├── EMSAccordionContainer.js (129 lines)
│       │       │   │   ├── EMSAccordionPane.js (251 lines)
│       │       │   │   └── NEInfo.js (496 lines)
│       │       │   ├── nls/
│       │       │   │   ├── en/
│       │       │   │   │   └── EMSTabsView.js (164 lines)
│       │       │   │   ├── ja/
│       │       │   │   │   └── EMSTabsView.js (164 lines)
│       │       │   │   ├── ko/
│       │       │   │   │   └── EMSTabsView.js (166 lines)
│       │       │   │   └── EMSTabsView.js (169 lines)
│       │       │   ├── tabs/
│       │       │   │   ├── chassistab/
│       │       │   │   │   ├── nls/
│       │       │   │   │   │   ├── en/
│       │       │   │   │   │   │   └── ChassisTab.js (6 lines)
│       │       │   │   │   │   ├── ja/
│       │       │   │   │   │   │   └── ChassisTab.js (6 lines)
│       │       │   │   │   │   └── ChassisTab.js (10 lines)
│       │       │   │   │   ├── templates/
│       │       │   │   │   │   ├── index.html (180 lines)
│       │       │   │   │   │   └── notification.html (11 lines)
│       │       │   │   │   └── ChassisTab.js (379 lines)
│       │       │   │   ├── devicedetailtab/
│       │       │   │   │   └── DeviceDetailTab.js (272 lines)
│       │       │   │   └── logicaltab/
│       │       │   │       ├── templates/
│       │       │   │       │   └── LogicalTabView.html (10 lines)
│       │       │   │       └── LogicalTab.js (76 lines)
│       │       │   ├── EMSContentPane.js (89 lines)
│       │       │   ├── EMSRouter.js (102 lines)
│       │       │   ├── EMSTabContentPane.js (122 lines)
│       │       │   ├── EMSTabsView.js (241 lines)
│       │       │   ├── MessageCongress.js (191 lines)
│       │       │   └── _LoadingMixin.js (41 lines)
│       │       └── package.ems.profile.js (71 lines)
│       ├── .gitignore (1 lines)
│       ├── assembly.xml (25 lines)
│       └── pom.xml (228 lines)
├── .gitignore (7 lines)
├── .project (11 lines)
└── Jenkinsfile (150 lines)
```
