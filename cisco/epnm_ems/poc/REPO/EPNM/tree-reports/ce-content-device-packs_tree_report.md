# Repository Tree Report: ce-content-device-packs

- Repository root: `/Users/cmoore/Documents/programming/EPNM/inventory/ce-content-device-packs`
- Included text-like files: `6445`
- Included directories: `1427`
- Total raw lines: `4494138`
- Skipped binary files: `2`
- Skipped ignored-extension files: `6`

```text
ce-content-device-packs/
├── config/
│   ├── block_root_user.sh (50 lines)
│   ├── build.properties (65 lines)
│   ├── settings.xml (70 lines)
│   ├── settings_rel.xml (54 lines)
│   └── settings_release.xml (54 lines)
├── deviceTools/
│   ├── DeviceComm/
│   │   ├── src/
│   │   │   └── main/
│   │   │       ├── java/
│   │   │       │   └── com/
│   │   │       │       └── cisco/
│   │   │       │           ├── cliClient/
│   │   │       │           │   └── CommProducer.java (96 lines)
│   │   │       │           ├── commLayers/
│   │   │       │           │   └── cli/
│   │   │       │           │       ├── SSHCommExecution.java (154 lines)
│   │   │       │           │       └── TelnetCommExecution.java (344 lines)
│   │   │       │           ├── commThreadPool/
│   │   │       │           │   ├── SSHTask.java (77 lines)
│   │   │       │           │   ├── TelnetTask.java (84 lines)
│   │   │       │           │   └── ThreadPoolService.java (41 lines)
│   │   │       │           ├── domain/
│   │   │       │           │   ├── Device.java (68 lines)
│   │   │       │           │   └── Task.java (100 lines)
│   │   │       │           └── propertyFileHandling/
│   │   │       │               └── LoadPropertFile.java (58 lines)
│   │   │       └── resources/
│   │   │           ├── config.properties (7 lines)
│   │   │           └── log4j.properties (18 lines)
│   │   ├── .classpath (37 lines)
│   │   ├── .project (29 lines)
│   │   └── pom.xml (54 lines)
│   ├── DeviceCommWS/
│   │   ├── WebContent/
│   │   │   ├── META-INF/
│   │   │   │   └── MANIFEST.MF (3 lines)
│   │   │   └── WEB-INF/
│   │   │       ├── dispatcher-servlet.xml (15 lines)
│   │   │       └── web.xml (31 lines)
│   │   ├── src/
│   │   │   └── com/
│   │   │       └── cisco/
│   │   │           └── deviceService/
│   │   │               ├── DeviceController.java (89 lines)
│   │   │               ├── DeviceImpl.java (38 lines)
│   │   │               └── DeviceInterface.java (14 lines)
│   │   ├── .classpath (20 lines)
│   │   ├── .project (42 lines)
│   │   └── pom.xml (169 lines)
│   ├── DeviceManagerGui/
│   │   ├── css/
│   │   │   ├── bootstrap.min.css (8044 lines)
│   │   │   ├── cytoscape-context-menus.css (51 lines)
│   │   │   ├── deviceWS.css (169 lines)
│   │   │   └── jquery.qtip.css (623 lines)
│   │   ├── images/
│   │   │   └── RouterPic.svg (71 lines)
│   │   ├── imports/
│   │   │   ├── angular.min.js (318 lines)
│   │   │   ├── bootstrap.min.js (7 lines)
│   │   │   ├── cytoscape-context-menus.js (422 lines)
│   │   │   ├── cytoscape-qtip.js (398 lines)
│   │   │   ├── cytoscape.min.js (63 lines)
│   │   │   ├── jquery.min.js (5 lines)
│   │   │   ├── jquery.qtip.js (3440 lines)
│   │   │   └── xml2json.min.js (1 lines)
│   │   ├── js/
│   │   │   ├── ajaxloader.js (39 lines)
│   │   │   ├── base.js (420 lines)
│   │   │   ├── directive.js (18 lines)
│   │   │   └── topology.js (416 lines)
│   │   ├── .classpath (20 lines)
│   │   ├── .project (42 lines)
│   │   ├── Device-Manager.html (344 lines)
│   │   ├── inputUserData.xml (270 lines)
│   │   └── pom.xml (71 lines)
│   ├── DevicePersistency/
│   │   ├── src/
│   │   │   ├── main/
│   │   │   │   ├── java/
│   │   │   │   │   └── com/
│   │   │   │   │       └── cisco/
│   │   │   │   │           ├── common/
│   │   │   │   │           │   ├── App.java (32 lines)
│   │   │   │   │           │   └── Device.java (80 lines)
│   │   │   │   │           └── persistence/
│   │   │   │   │               └── HibernateUtil.java (36 lines)
│   │   │   │   └── resources/
│   │   │   │       ├── com/
│   │   │   │       │   └── cisco/
│   │   │   │       │       └── common/
│   │   │   │       │           └── Device.hbm.xml (24 lines)
│   │   │   │       └── hibernate.cfg.xml (18 lines)
│   │   │   └── test/
│   │   │       └── java/
│   │   │           └── com/
│   │   │               └── cisco/
│   │   │                   └── common/
│   │   │                       └── AppTest.java (38 lines)
│   │   ├── .classpath (32 lines)
│   │   └── pom.xml (50 lines)
│   └── pom.xml (54 lines)
├── emsDevicePackages/
│   ├── deviceProfile/
│   │   ├── com.cisco.prime.deviceprofile.ASR1000/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (6 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (1 lines)
│   │   │   │           └── .orderedFeatures (206 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (297 lines)
│   │   ├── com.cisco.prime.deviceprofile.ASR9K-64CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (11 lines)
│   │   │   │           └── .orderedFeatures (288 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (399 lines)
│   │   ├── com.cisco.prime.deviceprofile.CAT8K_CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (4 lines)
│   │   │   │           └── .orderedFeatures (79 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (151 lines)
│   │   ├── com.cisco.prime.deviceprofile.CAT9K_STACK_CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (4 lines)
│   │   │   │           └── .orderedFeatures (77 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpdevice.xml (179 lines)
│   │   ├── com.cisco.prime.deviceprofile.CBR8/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (1 lines)
│   │   │   │           └── .orderedFeatures (64 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpdevice.xml (100 lines)
│   │   ├── com.cisco.prime.deviceprofile.CRS16SB/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (1 lines)
│   │   │   │           └── .orderedFeatures (223 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (338 lines)
│   │   ├── com.cisco.prime.deviceprofile.GenericDeviceCE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (17 lines)
│   │   │   │           └── .orderedFeatures (13 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (62 lines)
│   │   ├── com.cisco.prime.deviceprofile.ME-36x38x/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (3 lines)
│   │   │   │           └── .orderedFeatures (131 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (168 lines)
│   │   ├── com.cisco.prime.deviceprofile.ME1200CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (1 lines)
│   │   │   │           └── .orderedFeatures (107 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (177 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS42XXFamily/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (17 lines)
│   │   │   │           └── .orderedFeatures (413 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (477 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS4K/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (4 lines)
│   │   │   │           └── .orderedFeatures (240 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (290 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS520CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (3 lines)
│   │   │   │           └── .orderedFeatures (38 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (107 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS540L_CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (6 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (46 lines)
│   │   │   │           └── .orderedFeatures (270 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (395 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS55XX_CE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (34 lines)
│   │   │   │           └── .orderedFeatures (287 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpdevice.xml (434 lines)
│   │   ├── com.cisco.prime.deviceprofile.NCS5K/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (3 lines)
│   │   │   │           └── .orderedFeatures (232 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   └── xmpdevice.xml (350 lines)
│   │   ├── com.cisco.prime.deviceprofile.NEXUS3KCE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (17 lines)
│   │   │   │           └── .orderedFeatures (6 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (67 lines)
│   │   ├── com.cisco.prime.deviceprofile.NEXUS9KCE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (17 lines)
│   │   │   │           └── .orderedFeatures (9 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (56 lines)
│   │   ├── com.cisco.prime.deviceprofile.ThirdPartyDeviceProfileCE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (3 lines)
│   │   │   │           └── .orderedFeatures (6 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (31 lines)
│   │   ├── com.cisco.prime.deviceprofile.asr901Family/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (26 lines)
│   │   │   │           └── .orderedFeatures (356 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (441 lines)
│   │   ├── com.cisco.prime.deviceprofile.asr901sFamily/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (6 lines)
│   │   │   │           └── .orderedFeatures (342 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (36 lines)
│   │   │   └── xmpdevice.xml (431 lines)
│   │   ├── com.cisco.prime.deviceprofile.asr90xFamily/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (26 lines)
│   │   │   │           └── .orderedFeatures (361 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (465 lines)
│   │   ├── com.cisco.prime.deviceprofile.cat6500/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (5 lines)
│   │   │   │           └── .orderedFeatures (42 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpdevice.xml (148 lines)
│   │   ├── com.cisco.prime.deviceprofile.ncs6008/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (1 lines)
│   │   │   │           └── .orderedFeatures (272 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (333 lines)
│   │   ├── com.cisco.prime.deviceprofile.uiMetadata.UI_Metadata_Cisco_Catalyst_6500_Virtual_Switching_System/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.uiMetadata/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── ifm_ui_metadata.xml (27 lines)
│   │   │   │           └── .orderedFeatures (6 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpdevice.xml (35 lines)
│   │   ├── com.cisco.xmp.deviceprofile.ASR9K-IOSXR/
│   │   │   ├── .settings/
│   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           ├── cdp/
│   │   │   │           │   └── com.cisco.xmp.sdk.contrib.chassisView/
│   │   │   │           │       ├── META-INF/
│   │   │   │           │       │   └── services/
│   │   │   │           │       │       └── com.cisco.xmp.acdr.acpm.device.IDevicePartAccess (1 lines)
│   │   │   │           │       └── supportedDevices.properties (9 lines)
│   │   │   │           └── .orderedFeatures (274 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpdevice.xml (399 lines)
│   │   └── pom.xml (177 lines)
│   ├── feature/
│   │   ├── com.cisco.prime.feature.cardProtection/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (8 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.carrier-ethernet-pbb/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (13 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.prime.feature.device-capability/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.prime.feature.ethernet-oam/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.ethernet-oam-cfm/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.ethernet-oam-elmi/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.ethernet-oam-pm/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.ethernetflowpoint_me1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (14 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.prime.feature.feature-LLDP-ME1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-LLDP_topology-ME1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-ains/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (33 lines)
│   │   ├── com.cisco.prime.feature.feature-ains-port/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (33 lines)
│   │   ├── com.cisco.prime.feature.feature-bdi/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.feature-eowyn5g/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (17 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.feature-ipinterworking/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (7 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (29 lines)
│   │   ├── com.cisco.prime.feature.feature-l3link-bgp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-l3link-flowpoint/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (35 lines)
│   │   ├── com.cisco.prime.feature.feature-l3link-isis/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-l3link-ospf-delete/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (41 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.prime.feature.feature-l3vpn-config-change/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (32 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (62 lines)
│   │   ├── com.cisco.prime.feature.feature-l3vpn-routepolicy-inventory/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.prime.feature.feature-lag/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (34 lines)
│   │   ├── com.cisco.prime.feature.feature-lag-ME1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-lag-me3x00/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.prime.feature.feature-port-mirroring/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (27 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.feature-powersupply_generic/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-ptp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (34 lines)
│   │   ├── com.cisco.prime.feature.feature-sdr/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature-serial/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.prime.feature.feature_ChassisView-admin-config/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (7 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.feature_IPinterface/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (4 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (68 lines)
│   │   ├── com.cisco.prime.feature.feature_MPLS_TE_FRR/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (11 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (33 lines)
│   │   ├── com.cisco.prime.feature.feature_QOS_ME1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.feature_SFP/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.prime.feature.feature_SegmentRouting/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (17 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.prime.feature.feature_SegmentRoutingDummy/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   └── xmpfeature.xml (18 lines)
│   │   ├── com.cisco.prime.feature.feature_VSS/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (30 lines)
│   │   ├── com.cisco.prime.feature.feature_cem/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (35 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_NCS520CE/
│   │   │   └── xmpfeature.xml (35 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_NCS5508/
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_NCS5K/
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_asr901s/
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_asr90x/
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.feature_compliance_prime_show_commands_ncs42xx/
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.feature_config_interface/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (17 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (73 lines)
│   │   ├── com.cisco.prime.feature.feature_eoam_y1731/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (27 lines)
│   │   ├── com.cisco.prime.feature.feature_ethernet_Interfaces_me1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.prime.feature.feature_isis/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (26 lines)
│   │   │   └── xmpfeature.xml (43 lines)
│   │   ├── com.cisco.prime.feature.feature_mplste/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (19 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (43 lines)
│   │   ├── com.cisco.prime.feature.feature_mplste_bfd/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.prime.feature.feature_mplste_lspAttrList/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (14 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.feature_ospf_te/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (14 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.prime.feature.feature_packet_device_Menus/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (5 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (18 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base1_envtemp_extended_asr901Family/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── ENVTEMP/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (30 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base1_envtemp_extended_asr90xFamily/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── ENVTEMP/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (30 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base1_envtemp_extended_asr9k-iosxr/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── ENVTEMP/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (30 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base1_envtemp_extended_ncs42xxFamily/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── ENVTEMP/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (30 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base1_envtemp_extended_ncs4k/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── ENVTEMP/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (30 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base_deviceavailability_extended/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── DVAVAILABILITY/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (16 lines)
│   │   │   └── xmpfeature.xml (27 lines)
│   │   ├── com.cisco.prime.feature.feature_performance_base_memory_ME1200_extended/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (8 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── MEMORY/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (25 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (29 lines)
│   │   ├── com.cisco.prime.feature.feature_protectiongroup/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (27 lines)
│   │   ├── com.cisco.prime.feature.feature_srte/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (39 lines)
│   │   ├── com.cisco.prime.feature.ldpResources/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (21 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (26 lines)
│   │   │   └── xmpfeature.xml (51 lines)
│   │   ├── com.cisco.prime.feature.performance_me1200_cpu/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           ├── META-INF/
│   │   │   │           │   └── MANIFEST.MF (7 lines)
│   │   │   │           └── cfp/
│   │   │   │               └── com.cisco.xmp.sdk.contrib.pm.mapping/
│   │   │   │                   └── CPU/
│   │   │   │                       ├── META-INF/
│   │   │   │                       │   └── services/
│   │   │   │                       │       └── com.cisco.xmp.acdr.acpm.featurepart.configuration.IFeaturePartConfigurationAccess (1 lines)
│   │   │   │                       └── pmMapping.xml (12 lines)
│   │   │   └── xmpfeature.xml (28 lines)
│   │   ├── com.cisco.prime.feature.serial-config/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.prime.feature.synce/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.prime.feature.vcop/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.prime.feature.vlan_me1200/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (25 lines)
│   │   ├── com.cisco.prime.feature.xmp-im-ethernet-oam-module/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (17 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (42 lines)
│   │   ├── com.cisco.xmp.feature.auth-key-chain/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.xmp.feature.bfd-template/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (11 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.xmp.feature.cem-config/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.cem-config-recovered-clock/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.ethernet-oam-cfm-domain/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-ce-config-iosxe/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (85 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (151 lines)
│   │   ├── com.cisco.xmp.feature.feature-ce-config-iosxr/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (77 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (115 lines)
│   │   ├── com.cisco.xmp.feature.feature-device-logs/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (8 lines)
│   │   │   └── xmpfeature.xml (30 lines)
│   │   ├── com.cisco.xmp.feature.feature-eoam-ipsla/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (22 lines)
│   │   │   └── xmpfeature.xml (42 lines)
│   │   ├── com.cisco.xmp.feature.feature-erps-g8032/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-hsrp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.xmp.feature.feature-iccp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.feature-ip-prefixlist/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (53 lines)
│   │   ├── com.cisco.xmp.feature.feature-ipsla-twamp-light/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (16 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-l2vpn-pbb-evpn/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (62 lines)
│   │   ├── com.cisco.xmp.feature.feature-l2vpn-pseudowire-headend/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (13 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (66 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3link-ospf/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (52 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-bgp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-interface/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-ip-pep/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (11 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-ipsla/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-mpbgp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (44 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-ospf/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (32 lines)
│   │   ├── com.cisco.xmp.feature.feature-l3vpn-vrf/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature-lacplag-link/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (36 lines)
│   │   ├── com.cisco.xmp.feature.feature-mlacp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.feature-ospf/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (15 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (43 lines)
│   │   ├── com.cisco.xmp.feature.feature-ospf-XE/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── com.cisco.xmp.feature.feature_l3link_te/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (12 lines)
│   │   │   ├── .classpath (31 lines)
│   │   │   ├── .project (40 lines)
│   │   │   └── xmpfeature.xml (37 lines)
│   │   ├── com.cisco.xmp.feature.feature_rpd/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (9 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   └── xmpfeature.xml (36 lines)
│   │   ├── com.cisco.xmp.feature.l3vpn-qos-applyQosPolicy/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (26 lines)
│   │   ├── com.cisco.xmp.feature.mef-qos-applyQosPolicy/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.xmp.feature.mef-qos-classMap/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.xmp.feature.mef-qos-inventory/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.xmp.feature.mef-qos-policyMap/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (10 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (24 lines)
│   │   │   └── xmpfeature.xml (38 lines)
│   │   ├── com.cisco.xmp.feature.prime-ethernet-resource-model/
│   │   │   ├── .settings/
│   │   │   │   ├── org.eclipse.jdt.core.prefs (5 lines)
│   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (13 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (44 lines)
│   │   ├── com.cisco.xmp.feature.prime-resource-model-PwSegment/
│   │   │   ├── .settings/
│   │   │   │   └── org.eclipse.m2e.core.prefs (4 lines)
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (13 lines)
│   │   │   ├── .project (25 lines)
│   │   │   └── xmpfeature.xml (44 lines)
│   │   ├── com.cisco.xmp.feature.rsvp/
│   │   │   ├── src/
│   │   │   │   └── main/
│   │   │   │       └── resources/
│   │   │   │           └── META-INF/
│   │   │   │               └── MANIFEST.MF (7 lines)
│   │   │   ├── .classpath (26 lines)
│   │   │   ├── .project (23 lines)
│   │   │   └── xmpfeature.xml (31 lines)
│   │   ├── .project (11 lines)
│   │   └── pom.xml (219 lines)
│   ├── featureParts/
│   │   ├── ChassisView_admin_config_xde/
│   │   │   ├── sendCommandAdminConfigMode/
│   │   │   │   └── sendCommandAdminConfigMode.par (109 lines)
│   │   │   ├── sendCommandAdminMode/
│   │   │   │   └── sendCommandAdminMode.par (97 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (33 lines)
│   │   │   └── xmpxde.xml (35 lines)
│   │   ├── DeviceCapability_ICE/
│   │   │   ├── getCemModuleSpec.xpa/
│   │   │   │   ├── getPriorityForIMs/
│   │   │   │   │   └── getPriorityForIMs.par (315 lines)
│   │   │   │   ├── getPriorityForNewVersionIMs/
│   │   │   │   │   └── getPriorityForNewVersionIMs.par (269 lines)
│   │   │   │   └── getSupportedServices/
│   │   │   │       └── getSupportedServices.par (996 lines)
│   │   │   ├── getCemSpec.xpa/
│   │   │   │   └── getMinPayload/
│   │   │   │       └── getMinPayload.par (146 lines)
│   │   │   ├── getGeneralSpec/
│   │   │   │   └── getDeviceType/
│   │   │   │       └── getDeviceType.par (141 lines)
│   │   │   ├── getL2TransportSpec.xpa/
│   │   │   │   ├── getEncapsulationDot1ad/
│   │   │   │   │   └── getEncapsulationDot1ad.par (185 lines)
│   │   │   │   ├── getEtherType/
│   │   │   │   │   └── getEtherType.par (143 lines)
│   │   │   │   ├── getEvpnSupported/
│   │   │   │   │   └── getEvpnSupported.par (201 lines)
│   │   │   │   ├── getExact/
│   │   │   │   │   └── getExact.par (95 lines)
│   │   │   │   ├── getInnerVlanAlloWhenOuterIsRange/
│   │   │   │   │   └── getInnerVlanAlloWhenOuterIsRange.par (233 lines)
│   │   │   │   ├── getPortEncapsulation/
│   │   │   │   │   └── getPortEncapsulation.par (230 lines)
│   │   │   │   ├── getPrioTagOnlyAloneOrAnyUntagged/
│   │   │   │   │   └── getPrioTagOnlyAloneOrAnyUntagged.par (191 lines)
│   │   │   │   ├── getPrioTagOnlyWithDot1qOrDot1ad/
│   │   │   │   │   └── getPrioTagOnlyWithDot1qOrDot1ad.par (95 lines)
│   │   │   │   ├── getPriorityTagged/
│   │   │   │   │   └── getPriorityTagged.par (144 lines)
│   │   │   │   ├── getPushDot1ad/
│   │   │   │   │   └── getPushDot1ad.par (319 lines)
│   │   │   │   ├── getPushDot1q/
│   │   │   │   │   └── getPushDot1q.par (143 lines)
│   │   │   │   ├── getSpeedDuplexNegotiation/
│   │   │   │   │   └── getSpeedDuplexNegotiation.par (446 lines)
│   │   │   │   ├── getTranslate/
│   │   │   │   │   └── getTranslate.par (148 lines)
│   │   │   │   ├── getUniqueDefaultEncapsulation/
│   │   │   │   │   └── getUniqueDefaultEncapsulation.par (143 lines)
│   │   │   │   ├── getUntaggedOnlyAlone/
│   │   │   │   │   └── getUntaggedOnlyAlone.par (95 lines)
│   │   │   │   ├── getVfiCreation/
│   │   │   │   │   └── getVfiCreation.par (143 lines)
│   │   │   │   ├── getVlanCos/
│   │   │   │   │   └── getVlanCos.par (144 lines)
│   │   │   │   └── getVlanCosOnlyWithPrioTag/
│   │   │   │       └── getVlanCosOnlyWithPrioTag.par (144 lines)
│   │   │   ├── getL3VPNSpec.xpa/
│   │   │   │   ├── getBviBdiSupport/
│   │   │   │   │   └── getBviBdiSupport.par (95 lines)
│   │   │   │   └── getMTURange/
│   │   │   │       └── getMTURange.par (252 lines)
│   │   │   ├── getNamesNormalizationSpec.xpa/
│   │   │   │   ├── getBridgeDomainNameLength/
│   │   │   │   │   └── getBridgeDomainNameLength.par (95 lines)
│   │   │   │   ├── getBridgeGroupNameLength/
│   │   │   │   │   └── getBridgeGroupNameLength.par (95 lines)
│   │   │   │   ├── getEthMaintEntityGroupNameLength/
│   │   │   │   │   └── getEthMaintEntityGroupNameLength.par (95 lines)
│   │   │   │   ├── getLocalConnectNameLength/
│   │   │   │   │   └── getLocalConnectNameLength.par (95 lines)
│   │   │   │   ├── getShortMaintenanceNameLength/
│   │   │   │   │   └── getShortMaintenanceNameLength.par (95 lines)
│   │   │   │   ├── getVfiNameLength/
│   │   │   │   │   └── getVfiNameLength.par (95 lines)
│   │   │   │   ├── getXconnectGroupNameLength/
│   │   │   │   │   └── getXconnectGroupNameLength.par (95 lines)
│   │   │   │   └── getXconnectNameLength/
│   │   │   │       └── getXconnectNameLength.par (95 lines)
│   │   │   ├── getTETunnelSpec.xpa/
│   │   │   │   ├── getAffinityBits/
│   │   │   │   │   └── getAffinityBits.par (144 lines)
│   │   │   │   ├── getAffinityMask/
│   │   │   │   │   └── getAffinityMask.par (144 lines)
│   │   │   │   ├── getAutoRouteAnnounce/
│   │   │   │   │   └── getAutoRouteAnnounce.par (144 lines)
│   │   │   │   ├── getCoRouted/
│   │   │   │   │   └── getCoRouted.par (144 lines)
│   │   │   │   ├── getEncapMode/
│   │   │   │   │   └── getEncapMode.par (144 lines)
│   │   │   │   ├── getFastDetectEnabled/
│   │   │   │   │   └── getFastDetectEnabled.par (144 lines)
│   │   │   │   ├── getHoldPriority/
│   │   │   │   │   └── getHoldPriority.par (144 lines)
│   │   │   │   ├── getLockDown/
│   │   │   │   │   └── getLockDown.par (144 lines)
│   │   │   │   ├── getLoopBack/
│   │   │   │   │   └── getLoopBack.par (144 lines)
│   │   │   │   └── getSetupPriority/
│   │   │   │       └── getSetupPriority.par (144 lines)
│   │   │   ├── resources/
│   │   │   │   ├── device-capability-model.xsd (819 lines)
│   │   │   │   └── device-capability-model.xslt (20 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getDeviceCapability.xde (136 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── Device_logs/
│   │   │   ├── bootFlash/
│   │   │   │   ├── bootFlash.par (61 lines)
│   │   │   │   ├── bootFlash.txt (2 lines)
│   │   │   │   ├── bootFlash.xjs (43 lines)
│   │   │   │   ├── bootFlashParser_xdeIOS.rpl (42 lines)
│   │   │   │   └── bootFlashParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── bootFlashTraceLogs/
│   │   │   │   ├── bootFlashTraceLogs.par (54 lines)
│   │   │   │   ├── bootFlashTraceLogs.xjs (32 lines)
│   │   │   │   ├── bootFlashTraceLogsParserOutput.xsd (6 lines)
│   │   │   │   └── bootFlashTraceLogsParser_xdeIOS.rpl (3 lines)
│   │   │   ├── copyFileWithSCPEx/
│   │   │   │   ├── copyFileWithSCPEx.par (43 lines)
│   │   │   │   └── copyFileWithSCPEx.xde (82 lines)
│   │   │   ├── copyStbyBFlashToBFlash/
│   │   │   │   ├── copyStatus.txt (2 lines)
│   │   │   │   ├── copyStbyBFlashToBFlash.par (57 lines)
│   │   │   │   ├── copyStbyBFlashToBFlashParserOutput.xsd (6 lines)
│   │   │   │   ├── copyStbyBFlashToBFlashParser_xdeIOS.rpl (43 lines)
│   │   │   │   └── copyStbyBFlashToBFlashParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── deleteBootflash/
│   │   │   │   ├── deleteBootflash.par (54 lines)
│   │   │   │   ├── deleteBootflashParserOutput.xsd (6 lines)
│   │   │   │   └── deleteBootflashParser_xdeIOS.rpl (3 lines)
│   │   │   ├── deleteStandByBootflash/
│   │   │   │   ├── deleteStandByBootflash.par (57 lines)
│   │   │   │   ├── deleteStandByBootflashParserOutput.xsd (6 lines)
│   │   │   │   └── deleteStandByBootflashParser_xdeIOS.rpl (3 lines)
│   │   │   ├── deviceConfAct/
│   │   │   │   ├── deviceConfAct.par (66 lines)
│   │   │   │   ├── deviceConfActParserOutput.xsd (6 lines)
│   │   │   │   └── deviceConfActParser_xdeIOS.rpl (3 lines)
│   │   │   ├── dirBootFlash/
│   │   │   │   ├── dirBootFlash.par (54 lines)
│   │   │   │   ├── dirBootFlash.txt (9 lines)
│   │   │   │   ├── dirBootFlashParser_xdeIOS.rpl (110 lines)
│   │   │   │   └── dirBootFlashParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── dirStandByBootFlash/
│   │   │   │   ├── dirStandByBootFlash.par (54 lines)
│   │   │   │   ├── dirStandByBootFlash.txt (97 lines)
│   │   │   │   ├── dirStandByBootFlashParserOutput.xsd (6 lines)
│   │   │   │   ├── dirStandByBootFlashParser_xdeIOS.rpl (52 lines)
│   │   │   │   └── dirStandByBootFlashParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── directoryCheck/
│   │   │   │   ├── directoryCheck.par (54 lines)
│   │   │   │   ├── directoryCheck.txt (1 lines)
│   │   │   │   ├── directoryCheckParserOutput.xsd (6 lines)
│   │   │   │   ├── directoryCheckParser_xdeIOS.rpl (43 lines)
│   │   │   │   └── directoryCheckParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── mkdirInDevice/
│   │   │   │   ├── mkdirInDevice.par (54 lines)
│   │   │   │   ├── mkdirInDeviceParserOutput.xsd (6 lines)
│   │   │   │   └── mkdirInDeviceParser_xdeIOS.rpl (3 lines)
│   │   │   ├── showPlatform/
│   │   │   │   ├── deviceTypeCheck_4202 (7 lines)
│   │   │   │   ├── dualRp (2 lines)
│   │   │   │   ├── showPlatform.par (54 lines)
│   │   │   │   ├── showPlatformParserOutput.xsd (6 lines)
│   │   │   │   ├── showPlatformParser_xdeIOS.rpl (71 lines)
│   │   │   │   ├── showPlatformParser_xdeIOSOutput.xsd (18 lines)
│   │   │   │   └── singleRP (1 lines)
│   │   │   ├── showTechLogs/
│   │   │   │   ├── showTechLogs.par (55 lines)
│   │   │   │   ├── showTechLogs.xjs (32 lines)
│   │   │   │   ├── showTechLogsParserOutput.xsd (6 lines)
│   │   │   │   └── showTechLogsParser_xdeIOS.rpl (3 lines)
│   │   │   ├── standbyBootFlashTraceLogs/
│   │   │   │   ├── standbyBootFlashTraceLogs.par (54 lines)
│   │   │   │   ├── standbyBootFlashTraceLogs.xjs (33 lines)
│   │   │   │   ├── standbyBootFlashTraceLogsParserOutput.xsd (6 lines)
│   │   │   │   └── standbyBootFlashTraceLogsParser_xdeIOS.rpl (3 lines)
│   │   │   ├── stbyBootFlash/
│   │   │   │   ├── stbyBootFlash.par (54 lines)
│   │   │   │   ├── stbyBootFlash.txt (2 lines)
│   │   │   │   ├── stbyBootFlash.xjs (50 lines)
│   │   │   │   ├── stbyBootFlashParserOutput.xsd (6 lines)
│   │   │   │   ├── stbyBootFlashParser_xdeIOS.rpl (42 lines)
│   │   │   │   └── stbyBootFlashParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── test/
│   │   │   │   ├── bootFlash.xft (26 lines)
│   │   │   │   ├── bootFlashTraceLogs.xft (763 lines)
│   │   │   │   ├── copyFileWithSCPEx.xft (25 lines)
│   │   │   │   ├── copyStbyBFlashToBFlash.xft (25 lines)
│   │   │   │   ├── deleteBootflash.xft (23 lines)
│   │   │   │   ├── deleteStandByBootflash.xft (24 lines)
│   │   │   │   ├── deviceConfAct.xft (33 lines)
│   │   │   │   ├── dirBootFlash.xft (27 lines)
│   │   │   │   ├── dirStandByBootFlash.xft (201 lines)
│   │   │   │   ├── directoryCheck.xft (23 lines)
│   │   │   │   ├── mkdirInDevice.xft (25 lines)
│   │   │   │   ├── showPlatform.xft (24 lines)
│   │   │   │   ├── showTechLogs.xft (73926 lines)
│   │   │   │   ├── standbyBootFlashTraceLogs.xft (751 lines)
│   │   │   │   └── stbyBootFlash.xft (27 lines)
│   │   │   ├── .project (17 lines)
│   │   │   ├── copiedDataDetails.xjs (23 lines)
│   │   │   ├── deleteLogOnDevice.xde (17 lines)
│   │   │   ├── deleteLogs.xjs (29 lines)
│   │   │   ├── deviceLogs.xde (137 lines)
│   │   │   ├── dirBootFlashFileDetalis.xjs (13 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── scpDeviceLogs.xde (152 lines)
│   │   │   ├── showPlatform.xjs (43 lines)
│   │   │   ├── showPlatformParser.xjs (15 lines)
│   │   │   ├── totalLogFileSize.xjs (36 lines)
│   │   │   └── xmpxde.xml (26 lines)
│   │   ├── IPInterface_CE/
│   │   │   ├── Ipv6_Xe.xpa/
│   │   │   │   └── getIpv6_Xe/
│   │   │   │       ├── 903_ipv6.txt (40 lines)
│   │   │   │       ├── 907_ipv6.txt (23 lines)
│   │   │   │       ├── getIpv6_Xe.par (63 lines)
│   │   │   │       ├── getIpv6_XeParserOutput.xsd (6 lines)
│   │   │   │       ├── getIpv6_XeParser_xdeIOS.rpl (357 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (1145 lines)
│   │   │   ├── getIfIndexCli.xpa/
│   │   │   │   └── getIfIndexCli/
│   │   │   │       ├── IOS.txt (1 lines)
│   │   │   │       ├── XR.txt (1 lines)
│   │   │   │       ├── getIfIndexCli.par (111 lines)
│   │   │   │       ├── getIfIndexCliParserOutput.xsd (6 lines)
│   │   │   │       ├── getIfIndexCli_IOS.rpl (69 lines)
│   │   │   │       ├── getIfIndexCli_XR.rpl (69 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (18 lines)
│   │   │   ├── getIfSnmpCli.xpa/
│   │   │   │   └── getIfSnmpCli/
│   │   │   │       ├── getIfSnmpCli.par (103 lines)
│   │   │   │       ├── getIfSnmpXe.rpl (78 lines)
│   │   │   │       ├── getIfSnmpXr.rpl (78 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (18 lines)
│   │   │   ├── getInterfaceName.xpa/
│   │   │   │   └── getInterfaceName/
│   │   │   │       ├── getInterfaceName.par (26 lines)
│   │   │   │       └── getInterfaceNameOutput.xsd (41 lines)
│   │   │   ├── getIpMtuCli.xpa/
│   │   │   │   └── getIpMtuCli/
│   │   │   │       ├── XE.txt (12 lines)
│   │   │   │       ├── XR.txt (6 lines)
│   │   │   │       ├── getIpMtuCli.par (109 lines)
│   │   │   │       ├── getIpMtuXe.rpl (129 lines)
│   │   │   │       ├── getIpMtuXr.rpl (138 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (20 lines)
│   │   │   ├── getIpMtuCliGi.xpa/
│   │   │   │   └── getIpMtuCliGi/
│   │   │   │       ├── XR.txt (6 lines)
│   │   │   │       ├── getIpMtuCliGi.par (109 lines)
│   │   │   │       ├── getIpMtuXeGi.rpl (107 lines)
│   │   │   │       ├── getIpMtuXrGi.rpl (130 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (20 lines)
│   │   │   ├── ipAddr.xpa/
│   │   │   │   └── IP-MIB/
│   │   │   │       ├── getipAddrTable.par (29 lines)
│   │   │   │       ├── ipAddrTableMapping.map (16 lines)
│   │   │   │       ├── output.txt (17 lines)
│   │   │   │       ├── snmpOutput.txt (14 lines)
│   │   │   │       ├── snmpOutput1.txt (44 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (470 lines)
│   │   │   ├── ipv4Address_cli.xpa/
│   │   │   │   └── getIPV4Address/
│   │   │   │       ├── 10.126.165.17.txt (763 lines)
│   │   │   │       ├── 10.126.165.19.txt (749 lines)
│   │   │   │       ├── 903_88.txt (808 lines)
│   │   │   │       ├── 903_ipv4.txt (428 lines)
│   │   │   │       ├── getIPV4Address.par (122 lines)
│   │   │   │       ├── getIPV4AddressParser_xdeIOS.rpl (618 lines)
│   │   │   │       ├── getIPV4AddressParser_xdeIOS_XR.rpl (646 lines)
│   │   │   │       ├── output-XR-GI.txt (16 lines)
│   │   │   │       ├── outputIOS_10_126_165_20.txt (84 lines)
│   │   │   │       ├── output_IOS_10_104_120_37.txt (18 lines)
│   │   │   │       ├── output_IOS_ASR903_10_126_165_24.txt (122 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v1.txt (39 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v2.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v2.txt (122 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v3.txt (159 lines)
│   │   │   │       ├── showvrfdetail-output-17.XR52.txt (54 lines)
│   │   │   │       ├── showvrfdetail-output-173-ASR903-15.4.2S.txt (67 lines)
│   │   │   │       ├── showvrfdetail-output-178-ASR903-15.3.3S3.txt (196 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S-v2.txt (49 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-24-ASR903-15.4.3.S.txt (122 lines)
│   │   │   │       ├── xmp-im-connectivity-module.xsd (1145 lines)
│   │   │   │       └── xmp-im-vrf-module.xsd (89 lines)
│   │   │   ├── ipv6Address_cli.xpa/
│   │   │   │   └── getIPV6Address/
│   │   │   │       ├── 10.126.165.17-ipv6.txt (628 lines)
│   │   │   │       ├── 10.126.165.17.txt (763 lines)
│   │   │   │       ├── 10.126.165.19.txt (636 lines)
│   │   │   │       ├── getIPV6Address.par (124 lines)
│   │   │   │       ├── getIPV6AddressParser_xdeIOS.rpl (819 lines)
│   │   │   │       ├── getIPV6AddressParser_xdeIOS_XR.rpl (365 lines)
│   │   │   │       ├── outputIOS_10_126_165_20.txt (84 lines)
│   │   │   │       ├── output_IOS_10_104_120_37.txt (18 lines)
│   │   │   │       ├── output_IOS_ASR903_10_126_165_24.txt (122 lines)
│   │   │   │       ├── output_XR_17.txt (159 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v1.txt (39 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v2.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v2.txt (122 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v3.txt (159 lines)
│   │   │   │       ├── showvrfdetail-output-17.XR52.txt (54 lines)
│   │   │   │       ├── showvrfdetail-output-173-ASR903-15.4.2S.txt (67 lines)
│   │   │   │       ├── showvrfdetail-output-178-ASR903-15.3.3S3.txt (196 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S-v2.txt (49 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-24-ASR903-15.4.3.S.txt (122 lines)
│   │   │   │       ├── xmp-im-connectivity-module.xsd (46 lines)
│   │   │   │       └── xmp-im-vrf-module.xsd (89 lines)
│   │   │   ├── tests/
│   │   │   │   ├── IPInterface.xft (262 lines)
│   │   │   │   ├── IpInterface-EMS-ASR9K.xft (3824 lines)
│   │   │   │   └── cannedData.xml (3285 lines)
│   │   │   ├── .project (17 lines)
│   │   │   ├── IPInterface.xde (989 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── L2TransportIntSettings_ICE/
│   │   │   ├── L2TransportIntSettings.xpa/
│   │   │   │   ├── getIntPEPSettings/
│   │   │   │   │   ├── IOS-XR-With-Service-ACL-Used.txt (1031 lines)
│   │   │   │   │   ├── IOS-XR-With-Service-ACLs.txt (40 lines)
│   │   │   │   │   ├── asr903-15-4-PortChan.txt (327 lines)
│   │   │   │   │   ├── ethernet_resource_endpoint.xslt (390 lines)
│   │   │   │   │   ├── ethernet_resource_endpointCat8k9k.xslt (287 lines)
│   │   │   │   │   ├── ethernet_resource_endpointXR.xslt (246 lines)
│   │   │   │   │   ├── getIntPEPSettings.par (313 lines)
│   │   │   │   │   ├── getIntPEPSettingsParser_xdeIOS_Cat8k_9k.rpl (749 lines)
│   │   │   │   │   ├── getIntPEPSettingsParser_xdeIOS_VSS6500.rpl (668 lines)
│   │   │   │   │   ├── getIntPEPSettingsParser_xdeIOS_XR.rpl (668 lines)
│   │   │   │   │   ├── getIntSettings_ICE_IOSParser_xdeCat8k9k.xsd (70 lines)
│   │   │   │   │   ├── getIntSettings_ICE_IOSParser_xdeIOS.rpl (800 lines)
│   │   │   │   │   ├── getIntSettings_ICE_IOSParser_xdeIOSOutput.xsd (70 lines)
│   │   │   │   │   ├── interface_serviceInstance_IOSXR_output.txt (229 lines)
│   │   │   │   │   ├── interface_serviceInstance_IOS_outputs.txt (235 lines)
│   │   │   │   │   ├── output-903.txt (267 lines)
│   │   │   │   │   ├── output-VSS6500.txt (448 lines)
│   │   │   │   │   ├── output2-XR.txt (1820 lines)
│   │   │   │   │   ├── output3-XR+ACLs.txt (1071 lines)
│   │   │   │   │   ├── prime-ethernet-resource-model.xsd (406 lines)
│   │   │   │   │   ├── sampleOuputIOS.txt (481 lines)
│   │   │   │   │   └── sampleOutput.txt (53 lines)
│   │   │   │   └── getSplitHorizonGroup/
│   │   │   │       ├── asr903-multi.txt (107 lines)
│   │   │   │       ├── emptyResponse (0 lines)
│   │   │   │       ├── getSplitHorizonGroup.par (47 lines)
│   │   │   │       ├── getSplitHorizonGroupParser_xdeIOS.rpl (303 lines)
│   │   │   │       └── prime-ethernet-resource-model.xsd (339 lines)
│   │   │   ├── getBridgeInformation.xpa/
│   │   │   │   ├── getEVCMap/
│   │   │   │   │   ├── getEVCMap.par (188 lines)
│   │   │   │   │   ├── getEVCMapParserOutput.xsd (36 lines)
│   │   │   │   │   ├── getEVCMapParser_xdeIOS.rpl (269 lines)
│   │   │   │   │   ├── getEVCMap_IOS.xslt (77 lines)
│   │   │   │   │   ├── iosOutputASR903.txt (1262 lines)
│   │   │   │   │   └── iosOutputNCS4206.txt (4738 lines)
│   │   │   │   ├── getEvpnInfo/
│   │   │   │   │   ├── evpnSampleOutput_IOS.txt (483 lines)
│   │   │   │   │   ├── getEvpnInfo.par (137 lines)
│   │   │   │   │   ├── getEvpnInfoParser_xde_IOS.rpl (484 lines)
│   │   │   │   │   ├── getEvpnInfo_IOS.xslt (130 lines)
│   │   │   │   │   └── prime-ethernet-resource-model.xsd (1460 lines)
│   │   │   │   ├── getVfiBridgeInfo/
│   │   │   │   │   ├── 173_interfaces.txt (1334 lines)
│   │   │   │   │   ├── IOS-XR-5-1-Vfi-Name-hypen.txt (567 lines)
│   │   │   │   │   ├── Local_Switching_IOS.txt (263 lines)
│   │   │   │   │   ├── asr901.txt (491 lines)
│   │   │   │   │   ├── asr903-15-3-PortChan.txt (89 lines)
│   │   │   │   │   ├── asr903-multi.txt (107 lines)
│   │   │   │   │   ├── asr_1k.txt (135 lines)
│   │   │   │   │   ├── bvi_xr.txt (61 lines)
│   │   │   │   │   ├── getVfiBridgeInfo.par (186 lines)
│   │   │   │   │   ├── getVfiBridgeInfoParser_xdeIOS.rpl (418 lines)
│   │   │   │   │   ├── getVfiBridgeInfoParser_xdeIOS_ASR1k.rpl (377 lines)
│   │   │   │   │   ├── getVfiBridgeInfoParser_xdeIOS_XR.rpl (348 lines)
│   │   │   │   │   ├── me3800-ios15-4.txt (40 lines)
│   │   │   │   │   ├── output-Asr-9006kIOS-XR5-1.txt (333 lines)
│   │   │   │   │   ├── prime-ethernet-resource-model.xsd (645 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS (979 lines)
│   │   │   │   │   ├── show_bridge-domain_10.81.80.37_IOS_15.6(S)2.txt (48 lines)
│   │   │   │   │   └── show_l2vpn_bridge-domain_detail_output_XR_leonid.txt (14945 lines)
│   │   │   │   └── getXConnectInfo/
│   │   │   │       ├── ASR097_ios.txt (216 lines)
│   │   │   │       ├── LocalSwitching_IOSXR.txt (758 lines)
│   │   │   │       ├── Output_ShowL2VPNXConnectDetail_XR_Leonid.txt (4477 lines)
│   │   │   │       ├── SamplewithIOSEVC.txt (309 lines)
│   │   │   │       ├── asr901-localXC-MixSI.txt (2083 lines)
│   │   │   │       ├── asr903-15-3-WithPwBackup.txt (135 lines)
│   │   │   │       ├── asr903-15-4-NoEvc.txt (977 lines)
│   │   │   │       ├── getXConnectInfo.par (192 lines)
│   │   │   │       ├── getXConnectInfoParser_xdeIOS.rpl (1626 lines)
│   │   │   │       ├── getXConnectInfoParser_xdeIOS_XR.rpl (388 lines)
│   │   │   │       ├── getXConnectInfo_ios.xslt (682 lines)
│   │   │   │       ├── getXConnectInfo_ios_2.xslt (161 lines)
│   │   │   │       ├── me3800.txt (1500 lines)
│   │   │   │       ├── ncs42xx_pwInterfaceId.txt (649 lines)
│   │   │   │       ├── prime-ethernet-resource-model.xsd (460 lines)
│   │   │   │       ├── sample-descconfig-IOS-XR.txt (442 lines)
│   │   │   │       ├── sampleDeviceOutput.txt (136 lines)
│   │   │   │       ├── show_l2vpn_xconnect_detail_Output_XR_10.65.205.28.txt (85 lines)
│   │   │   │       └── show_l2vpn_xconnect_detail_Output_XR_Leonid.txt (4477 lines)
│   │   │   ├── getEthernetPWConnectionPEP.xpa/
│   │   │   │   ├── getEthernetPWConnectionPEP/
│   │   │   │   │   ├── getEthernetPWConnectionPEP.par (117 lines)
│   │   │   │   │   ├── getEthernetPWConnectionPEPParser_xdeIOS_XR.rpl (191 lines)
│   │   │   │   │   ├── getEthernetPWConnectionPEP_iosxr.xslt (62 lines)
│   │   │   │   │   ├── prime-ethernet-resource-model.xsd (438 lines)
│   │   │   │   │   └── sampleDeviceOutput.txt (9668 lines)
│   │   │   │   ├── getEviProtocolEndpoint/
│   │   │   │   │   ├── getEthernetBridgeModel.xsd (32 lines)
│   │   │   │   │   ├── getEviProtocolEndpoint.par (284 lines)
│   │   │   │   │   ├── getEviProtocolEndpoint.xslt (87 lines)
│   │   │   │   │   ├── getEviProtocolEndpointParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getEviProtocolEndpointParser_xdeIOS.rpl (336 lines)
│   │   │   │   │   ├── getEviProtocolEndpointParser_xdeIOS_XR.rpl (295 lines)
│   │   │   │   │   ├── getEviProtocolEndpointParser_xdeIOS_XROutput.xsd (23 lines)
│   │   │   │   │   ├── prime-ethernet-resource-model.xsd (1485 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS-GI.txt (57 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (204 lines)
│   │   │   │   │   └── sampleDeviceOutputIOS_XR.txt (1210 lines)
│   │   │   │   └── getVfiPWConnectionEP/
│   │   │   │       ├── IOS-XR-5-1-SHG.txt (1164 lines)
│   │   │   │       ├── IOS-XR-5-1-Vfi-Name-Caps.txt (659 lines)
│   │   │   │       ├── VfiConnectionProtocolEP-model.xsd (108 lines)
│   │   │   │       ├── VfiConnectionProtocolEP_ios.xslt (81 lines)
│   │   │   │       ├── asr-903.txt (38 lines)
│   │   │   │       ├── asr-903_1.txt (56 lines)
│   │   │   │       ├── asr903-multi-evc.txt (25 lines)
│   │   │   │       ├── asr903-multi.txt (45 lines)
│   │   │   │       ├── evpn-sample.txt (200 lines)
│   │   │   │       ├── getVfiPWConnectionEP.par (149 lines)
│   │   │   │       ├── getVfiPWConnectionEPParser_xdeIOS.rpl (344 lines)
│   │   │   │       ├── getVfiPWConnectionEPParser_xdeIOS_XR.rpl (692 lines)
│   │   │   │       ├── moo (665 lines)
│   │   │   │       ├── output-Asr-9006kIOS-XR5-1.txt (333 lines)
│   │   │   │       ├── output-IOSXR-vpnid.txt (155 lines)
│   │   │   │       ├── output-asr-9006kIOS-XR-MultiPWnoInt.txt (574 lines)
│   │   │   │       └── prime-ethernet-resource-model.xsd (1115 lines)
│   │   │   ├── getEthernetSegmentIdentifier.xpa/
│   │   │   │   └── getEthernetSegmentIdentifier/
│   │   │   │       ├── getESId.xsd (27 lines)
│   │   │   │       ├── getEthernetSegmentIdentifier.par (114 lines)
│   │   │   │       ├── getEthernetSegmentIdentifierParser_IOS_XR.xslt (119 lines)
│   │   │   │       ├── getEthernetSegmentIdentifier_xdeIOS_XR.rpl (383 lines)
│   │   │   │       ├── prime-ethernet-resource-model.xsd (1641 lines)
│   │   │   │       ├── sampleOutput1_IOSXR.txt (275 lines)
│   │   │   │       ├── sampleOutput2_IOSXR.txt (439 lines)
│   │   │   │       ├── sampleOutput_IOSXR.txt (177 lines)
│   │   │   │       └── sampleOutput_IOSXR_73IL.txt (250 lines)
│   │   │   ├── getEviNeighborSettings.xpa/
│   │   │   │   └── getEviNeighborSettings/
│   │   │   │       ├── SampleDeviceOutput_IOS.txt (37 lines)
│   │   │   │       ├── SampleDeviceOutput_IOSXR.txt (59 lines)
│   │   │   │       ├── SampleDeviceOutput_IOS_GI.txt (99 lines)
│   │   │   │       ├── getEviNeighborSettings.par (283 lines)
│   │   │   │       ├── getEviNeighborSettingsParser_IOSXR.xslt (51 lines)
│   │   │   │       ├── getEviNeighborSettingsParser_xdeIOS.rpl (130 lines)
│   │   │   │       ├── getEviNeighborSettingsParser_xdeIOS_XR.rpl (155 lines)
│   │   │   │       ├── getEvpnEvi.xsd (20 lines)
│   │   │   │       └── prime-ethernet-resource-model.xsd (1490 lines)
│   │   │   ├── getEviTunnelMap.xpa/
│   │   │   │   └── getEviTunnelMap/
│   │   │   │       ├── SampleDeviceOutput_IOSXR.txt (1640 lines)
│   │   │   │       ├── getEviTunnelMap.par (120 lines)
│   │   │   │       ├── getEviTunnelMap.xsd (28 lines)
│   │   │   │       ├── getEviTunnelMap_IOSXR.xslt (56 lines)
│   │   │   │       └── getEviTunnelMap_xdeIOS_XR.rpl (237 lines)
│   │   │   ├── test cases/
│   │   │   │   ├── localswitching_ASR901_IOS15.4(2)S1_getVfiBridgeInfoParser_bridgedomainremoved.xft (150 lines)
│   │   │   │   ├── localswitching_ASR901_IOS15.4(2)S1_getVfiBridgeInfoParser_difflinecard.xft (117 lines)
│   │   │   │   └── localswitching_ASR901_IOS15.5(2)S1_getVfiBridgeInfo_sameinstance.xft (162 lines)
│   │   │   ├── tests/
│   │   │   │   ├── ASR903-getXConnectInfo-CE-auto.xft (309 lines)
│   │   │   │   ├── ASR903-getXConnectInfo-PAN5.xft (11504 lines)
│   │   │   │   ├── ASR903-getXConnectInfo-Test.xft (177 lines)
│   │   │   │   ├── ASR903-getXConnectInfo-Test2.xft (1651 lines)
│   │   │   │   ├── ASR903-getXConnectInfo-Test3.xft (13008 lines)
│   │   │   │   ├── ASR903-getXConnectInfo-Test4.xft (39595 lines)
│   │   │   │   ├── ASR903_ModifiedName_EVC.xft (5369 lines)
│   │   │   │   ├── ASR9K712-getEthernetSegmentInfo-Test.xft (578 lines)
│   │   │   │   ├── IOS-getEvpnInfo-GITest.xft (110 lines)
│   │   │   │   ├── IOS-getEvpnInfo-Test.xft (1447 lines)
│   │   │   │   ├── asr901-15-3-getXCInfo.xft (305 lines)
│   │   │   │   ├── asr903-15-4-getXCInfo-mixedSIformat.xft (579 lines)
│   │   │   │   ├── asr903-15-4-getXCInfo.xft (479 lines)
│   │   │   │   ├── asr903-IOS-VfiBridge.xft (157 lines)
│   │   │   │   ├── asr903-IOS-VfiPwCPEP.xft (197 lines)
│   │   │   │   ├── asr903Eth-MultiVfiCPEP.xft (1353 lines)
│   │   │   │   ├── asr903EthPWCPEPSuccess.xft (578 lines)
│   │   │   │   ├── asr903Success.xft (67 lines)
│   │   │   │   ├── asr903_3-3_getSHGIntDetails.xft (237 lines)
│   │   │   │   ├── asr9k-TransBridgeHypen.xft (1239 lines)
│   │   │   │   ├── asr9k-capture-description-1.xft (85 lines)
│   │   │   │   ├── asr9k-capture-description.xft (873 lines)
│   │   │   │   ├── asr9k_BridgeVFI.xft (890 lines)
│   │   │   │   ├── asr9k_EthPWConnectionPEP.xft (21100 lines)
│   │   │   │   ├── asr9k_L2TransportIntSettings.xft (492 lines)
│   │   │   │   ├── asr9k_L2Transport_preconfigure.xft (2944 lines)
│   │   │   │   ├── asr9k_P2PXC.xft (359 lines)
│   │   │   │   ├── asr9k_VfiPWPep.xft (1357 lines)
│   │   │   │   ├── asr9k_iosxr_vlanlistrange_L2TransportIntSettings.xft (898 lines)
│   │   │   │   ├── asr9k_vfi_with_SHG.xft (1288 lines)
│   │   │   │   ├── asr9k_vficonnpep_nopw.xft (115 lines)
│   │   │   │   ├── asr9k_withServiceACLs.xft (5402 lines)
│   │   │   │   ├── cat8k_fullInventory.xft (1573 lines)
│   │   │   │   ├── cat9k_fullInventory.xft (1422 lines)
│   │   │   │   ├── ios-getEviNeighborSettings.xft (536 lines)
│   │   │   │   ├── ios3600_L2TransportIntSettings.xft (812 lines)
│   │   │   │   ├── ios3600_L2TransportIntSettings_2.xft (1228 lines)
│   │   │   │   ├── ios3800_L2TransportIntSettings.xft (945 lines)
│   │   │   │   ├── ios901-l2vpnXC-localconnect.xft (562 lines)
│   │   │   │   ├── ios901_L2TransportIntSettings.xft (1989 lines)
│   │   │   │   ├── ios903_L2TransportIntSettings.xft (1646 lines)
│   │   │   │   ├── ios903_L2TransportIntSettings2.xft (22233 lines)
│   │   │   │   ├── ios903_ios_vlanlistrange_L2TransportIntSettings.xft (1013 lines)
│   │   │   │   ├── ios90x_getXConnectLC_GI.xft (113 lines)
│   │   │   │   ├── ios90x_getXConnectLC_HP_GI.xft (142 lines)
│   │   │   │   ├── iosME3800FullXdeProcRun.xft (27234 lines)
│   │   │   │   ├── iosXR_fullInventory.xft (8214 lines)
│   │   │   │   ├── ios_XConnect_EthPWConnPEP.xft (943 lines)
│   │   │   │   ├── ios_getEviProtocolEndpoint.xft (1134 lines)
│   │   │   │   ├── ios_getSHGDetailsEmpty.xft (21 lines)
│   │   │   │   ├── iosme3800_getxconnect1.xft (5010 lines)
│   │   │   │   ├── iosxr-getEviNeighborSettings.xft (303 lines)
│   │   │   │   ├── iosxr_.getSHGIntDetails.xft (25 lines)
│   │   │   │   ├── iosxr_getEviProtocolEndpoint.xft (11058 lines)
│   │   │   │   ├── iosxr_getEviTunnelMap.xft (3422 lines)
│   │   │   │   ├── ioxr-getEthernetSegmentIdentifier.xft (407 lines)
│   │   │   │   ├── me3600_getXConnectInfo_LC.xft (3908 lines)
│   │   │   │   ├── me3800-getXCInfo.xft (2898 lines)
│   │   │   │   ├── me3800EthernetBridgeIOS.xft (171 lines)
│   │   │   │   ├── ncs42xx-getXCInfo.xft (1424 lines)
│   │   │   │   └── ncs42xx-getXConnectInfo.xft (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getL2TransportIntSettings.xde (523 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── PseudowireSegmentEP_ICE/
│   │   │   ├── PW_Endpoint_Inventory.xpa/
│   │   │   │   ├── EvpnL2vpnRouteSettings/
│   │   │   │   │   ├── EvpnL2vonRouteSettingsOutputWithRoutePolicy_IOSXR.txt (52 lines)
│   │   │   │   │   ├── EvpnL2vpnRouteSettings.xsd (26 lines)
│   │   │   │   │   ├── EvpnL2vpnRouteSettingsParser_xdeIOS.rpl (202 lines)
│   │   │   │   │   ├── EvpnL2vpnRouteSettingsParser_xdeIOS_XR.rpl (274 lines)
│   │   │   │   │   ├── EvpnL2vpnRouteSettings_IOS.xslt (167 lines)
│   │   │   │   │   ├── EvpnL2vpnRouteSettings_IOSXR.xslt (82 lines)
│   │   │   │   │   ├── EvpnVpnIdOutput_IOS.txt (719 lines)
│   │   │   │   │   ├── EvpnVpnIdOutput_IOSXR.txt (225 lines)
│   │   │   │   │   ├── getEvpnL2vpnRouteSettings.par (208 lines)
│   │   │   │   │   └── prime-resource-model.xsd (810 lines)
│   │   │   │   ├── EvpnVpwsPWEndpoint/
│   │   │   │   │   ├── EvpnVpwsOutput_IOS.txt (362 lines)
│   │   │   │   │   ├── EvpnVpwsOutput_IOSXR.txt (665 lines)
│   │   │   │   │   ├── EvpnVpwsOutput_IOSXR_1.txt (193 lines)
│   │   │   │   │   ├── EvpnVpwsPWEndpoint.xslt (123 lines)
│   │   │   │   │   ├── EvpnVpwsPWEndpointParser_xdeIOS.rpl (339 lines)
│   │   │   │   │   ├── EvpnVpwsPWEndpointParser_xdeIOS_XR.rpl (787 lines)
│   │   │   │   │   ├── EvpnVpwsPwEndpoint_XR.xsd (37 lines)
│   │   │   │   │   ├── getEvpnVpwsPWEndpoint.par (219 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (236 lines)
│   │   │   │   │   └── prime-resource-model_XR.xsd (40 lines)
│   │   │   │   ├── getEVPNRemoteRouterIPs/
│   │   │   │   │   ├── evpnRemoteRouterIPs.xsd (25 lines)
│   │   │   │   │   ├── getEVPNRemoteRouterIPs.par (100 lines)
│   │   │   │   │   ├── getEVPNRemoteRouterIPs_IOS_XR.rpl (123 lines)
│   │   │   │   │   └── sampleOutput_IOSXR.txt (619 lines)
│   │   │   │   ├── getPWEndpoint/
│   │   │   │   │   ├── DeviceOutputIOS.txt (198 lines)
│   │   │   │   │   ├── IOSXRoutput.txt (9668 lines)
│   │   │   │   │   ├── IOS_XR_Routed (94 lines)
│   │   │   │   │   ├── PwProtocolEndpointParser_xdeIOS.rpl (795 lines)
│   │   │   │   │   ├── PwProtocolEndpoint_ios.xsd (64 lines)
│   │   │   │   │   ├── PwProtocolEndpoint_ios.xslt (303 lines)
│   │   │   │   │   ├── PwProtocolEndpoint_ios_xr.xslt (40 lines)
│   │   │   │   │   ├── getPWEndpoint.par (174 lines)
│   │   │   │   │   ├── getPWEndpointParser_xdeIOS_XR.rpl (937 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (255 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS-901.txt (552 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (306 lines)
│   │   │   │   │   ├── sampleOutput_IOS.txt (566 lines)
│   │   │   │   │   └── show_l2vpn_service_xconnect_all_detail.txt (2111 lines)
│   │   │   │   └── getVfiPWEndpoints/
│   │   │   │       ├── IOS-XR-5-1-SHG.txt (1250 lines)
│   │   │   │       ├── asr903-multiVfi.txt (70 lines)
│   │   │   │       ├── asr903ShowLdp.txt (25 lines)
│   │   │   │       ├── asr920_pwendpoints.txt (128 lines)
│   │   │   │       ├── getVfiPWEndpoints.par (161 lines)
│   │   │   │       ├── getVfiPWEndpoints.xslt (115 lines)
│   │   │   │       ├── getVfiPWEndpointsParser_xdeIOS.rpl (484 lines)
│   │   │   │       ├── getVfiPWEndpointsParser_xdeIOS_XR.rpl (1280 lines)
│   │   │   │       ├── output-Asr-9006kIOS-XR5-1.txt (333 lines)
│   │   │   │       ├── output-asr-9001kIOS-XR-MultiPInterworking.txt (122 lines)
│   │   │   │       ├── output-asr-9006kIOS-XR-MultiPWnoInt.txt (574 lines)
│   │   │   │       └── prime-resource-model.xsd (604 lines)
│   │   │   ├── PseudowireSegmentEP.xpa/
│   │   │   │   ├── getPWBandwidthNew/
│   │   │   │   │   ├── getPWBandwidthNew.par (91 lines)
│   │   │   │   │   ├── getPWBandwidthNewParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getPWBandwidthNewParser_xdeIOS.rpl (231 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (23 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS-NCS.txt (1697 lines)
│   │   │   │   │   └── sampleDeviceOutputIOS.txt (94 lines)
│   │   │   │   ├── getPWClassDetails/
│   │   │   │   │   ├── PWClassDetails.xslt (73 lines)
│   │   │   │   │   ├── getPWClassDetails.par (90 lines)
│   │   │   │   │   ├── getPWClassDetailsParser_xdeIOS.rpl (441 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (103 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (204 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS1.txt (508 lines)
│   │   │   │   │   └── sampleDeviceOutputIOS2.txt (158 lines)
│   │   │   │   ├── getPWOutInt/
│   │   │   │   │   ├── getPWOutInt.par (94 lines)
│   │   │   │   │   ├── getPWOutIntParser_xdeIOS_XR.rpl (149 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (19 lines)
│   │   │   │   │   └── sampleDeviceoutputXR.txt (69 lines)
│   │   │   │   ├── getPseudowireSegments/
│   │   │   │   │   ├── getPseudowireSegments.par (144 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (604 lines)
│   │   │   │   │   ├── pseudowireSegmentParser_IOS.rpl (399 lines)
│   │   │   │   │   ├── pseudowireSegmentParser_IOSXR.rpl (699 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (2355 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOSXR.txt (273 lines)
│   │   │   │   │   ├── sampleDeviceOutputNCS4K_XR.txt (816 lines)
│   │   │   │   │   └── sampleDeviceOutput_interworking_IOSXR.txt (44 lines)
│   │   │   │   ├── getVfiPWSplitHorizon/
│   │   │   │   │   ├── asr903-XE3.3.txt (194 lines)
│   │   │   │   │   ├── emptyResponse (0 lines)
│   │   │   │   │   ├── getVfiPWSplitHorizon.par (49 lines)
│   │   │   │   │   ├── getVfiPWSplitHorizonParser_xdeIOS.rpl (138 lines)
│   │   │   │   │   └── prime-resource-model.xsd (224 lines)
│   │   │   │   └── getcpwVcIndex/
│   │   │   │       ├── getcpwVcIndex.par (135 lines)
│   │   │   │       ├── getcpwVcIndexOutput.xsd (19 lines)
│   │   │   │       ├── getcpwVcIndexParser_xdeIOS.rpl (43 lines)
│   │   │   │       ├── getcpwVcIndexParser_xdeIOS_XR.rpl (208 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (5 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (45 lines)
│   │   │   │       └── sampleDeviceOutputIOS_XR_Multi.txt (95 lines)
│   │   │   ├── PwP2PForwarder.xpa/
│   │   │   │   └── getPwP2PForwarder/
│   │   │   │       ├── SampleDeviceOutput_XR.txt (86 lines)
│   │   │   │       ├── getPwP2PForwarder.par (111 lines)
│   │   │   │       ├── getPwP2PForwarderParserOutput.xsd (28 lines)
│   │   │   │       ├── getPwP2PForwarderParser_iosxr.rpl (369 lines)
│   │   │   │       ├── getPwP2PForwarder_iosxr.xslt (47 lines)
│   │   │   │       └── prime-resource-model.xsd (913 lines)
│   │   │   ├── tests/
│   │   │   │   ├── IOS-GetPWBandwidthNew.xft (1039 lines)
│   │   │   │   ├── IOS-GetPWClassDetails-Vfi-PWClassName.xft (207 lines)
│   │   │   │   ├── IOS-GetPWClassDetails.xft (4287 lines)
│   │   │   │   ├── IOS-SourceInterfaceName.xft (4577 lines)
│   │   │   │   ├── ME3600-GetPWClassDetails-Vfi-PWClassName.xft (717 lines)
│   │   │   │   ├── NCS42K-getBandwidthNew.xft (1036 lines)
│   │   │   │   ├── NCS42K-getPWClassDetails.xft (2535 lines)
│   │   │   │   ├── NSC4K-GetPWEndpoint-UP-DN-AD.xft (1782 lines)
│   │   │   │   ├── asr903-XE-33-VfiPwShg.xft (411 lines)
│   │   │   │   ├── asr920-getVfiPwEndpoints.xft (556 lines)
│   │   │   │   ├── asr9k-5-1-getVfiPwEndpoints.xft (494 lines)
│   │   │   │   ├── asr9k-getEVPNRemoteRouterIPs.xft (679 lines)
│   │   │   │   ├── asr9k_PWProtocolEP.xft (21931 lines)
│   │   │   │   ├── asrk9k-vfiPwEpsSHG.xft (2559 lines)
│   │   │   │   ├── cat8k-fullInventory.xft (1443 lines)
│   │   │   │   ├── cat9k-fullInventory.xft (1516 lines)
│   │   │   │   ├── ios-VfiPwShgEmpty.xft (21 lines)
│   │   │   │   ├── ios-fullInventory.xft (11543 lines)
│   │   │   │   ├── ios901_PwProtocolEndpoint.xft (1273 lines)
│   │   │   │   ├── ios901_PwProtocolEndpoint_RemoteAddress.xft (2064 lines)
│   │   │   │   ├── iosXR_fullInventory.xft (24679 lines)
│   │   │   │   ├── iosXR_fullInventory2.xft (19556 lines)
│   │   │   │   ├── ios_EvpnL2vpnRouteSettings.xft (194 lines)
│   │   │   │   ├── ios_EvpnVpwsProtocolEndpoint.xft (957 lines)
│   │   │   │   ├── ios_PwProtocolEndpoint.xft (1174 lines)
│   │   │   │   ├── ios_PwProtocolEndpoint2_ncs42xx.xft (18971 lines)
│   │   │   │   ├── ios_PwProtocolEndpoint_ncs42xx.xft (1555 lines)
│   │   │   │   ├── ios_XR_EvpnL2vpnRouteSettings.xft (1541 lines)
│   │   │   │   ├── ios_XR_EvpnVpwsProtocolEndpoint.xft (1178 lines)
│   │   │   │   ├── ios_XR_getPwP2PForwarder.xft (15416 lines)
│   │   │   │   ├── ios_XR_getPwP2PForwarder_GI.xft (218 lines)
│   │   │   │   ├── ios_asr-getVfiPwEndpoints.xft (293 lines)
│   │   │   │   ├── ios_getPseudowireSegments_ncs42xx.xft (2945 lines)
│   │   │   │   ├── iosxr-VfiPwShgEmpty.xft (27 lines)
│   │   │   │   ├── iosxr-getPWOutInt.xft (88 lines)
│   │   │   │   ├── iosxr-getPseudowireSegments-asr9k.xft (4413 lines)
│   │   │   │   └── priorityTagged_ios.xft (421 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getPseudowireSegmentEP.xde (540 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── bfdTemplate_config_change/
│   │   │   ├── get_BfdTemplate_ConfigChange.xpa/
│   │   │   │   └── get_BfdTemplate_ConfigChange_details/
│   │   │   │       ├── get_BfdTemplate_ConfigChange_details.par (49 lines)
│   │   │   │       ├── get_BfdTemplate_ConfigChange_details.xsd (23 lines)
│   │   │   │       ├── get_BfdTemplate_ConfigChange_details_IOS.rpl (63 lines)
│   │   │   │       └── output.txt (9 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (22 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_ethernet_oam_module/
│   │   │   ├── getEthernetOAM.xpa/
│   │   │   │   └── getOAMDetails/
│   │   │   │       ├── getOAMDetails.par (89 lines)
│   │   │   │       ├── getOAMDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getOAMDetailsParser_xdeIOS.rpl (1140 lines)
│   │   │   │       ├── getOAMDetailsParser_xdeIOSOutput.xsd (114 lines)
│   │   │   │       ├── getOAMDetailsParser_xdeIOS_XR.rpl (1211 lines)
│   │   │   │       ├── getOAMDetailsParser_xdeIOS_XROutput.xsd (131 lines)
│   │   │   │       ├── sample_ethmaintdomain_IOS.txt (88 lines)
│   │   │   │       └── sample_ethmaintdomain_IOSXR.txt (87 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_ios_CEM_xde/
│   │   │   ├── getConfigChangeCEMDetails.xpa/
│   │   │   │   └── getConfigChangeCEMDetails/
│   │   │   │       ├── D41.txt (118 lines)
│   │   │   │       ├── GCofig1 (94 lines)
│   │   │   │       ├── GCofig2 (12 lines)
│   │   │   │       ├── STS3C.txt (23 lines)
│   │   │   │       ├── getConfigChangeCEMDetails.par (24 lines)
│   │   │   │       ├── getConfigChangeCEMDetailsParser_xdeIOS.rpl (3159 lines)
│   │   │   │       ├── getConfigChangeCEMDetailsParser_xdeIOSOutput.xsd (230 lines)
│   │   │   │       ├── sonet.txt (139 lines)
│   │   │   │       └── tdmandpep (33 lines)
│   │   │   ├── getPwPepDetails/
│   │   │   │   ├── getPwPepDetails.par (57 lines)
│   │   │   │   ├── getPwPepDetails.xjs (21 lines)
│   │   │   │   ├── getPwPepDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getPwPepDetailsParser_xdeIOS.rpl (129 lines)
│   │   │   │   ├── getPwPepDetailsParser_xdeIOSOutput.xsd (21 lines)
│   │   │   │   └── pse119.txt (9 lines)
│   │   │   ├── test/
│   │   │   │   └── getPwPepDetails.xft (31 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (35 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_ios_IPInterworking_xde/
│   │   │   ├── getConfigChangeIPIntworkingDetails.xpa/
│   │   │   │   └── getConfigChangeIPInterworkingDetails/
│   │   │   │       ├── CircuitCreation_IP (29 lines)
│   │   │   │       ├── CircuitDeletion_IP (7 lines)
│   │   │   │       ├── D41.txt (118 lines)
│   │   │   │       ├── GCofig1 (94 lines)
│   │   │   │       ├── IP_SDH (42 lines)
│   │   │   │       ├── IP_Sonet (18 lines)
│   │   │   │       ├── IP_Xconnect (20 lines)
│   │   │   │       ├── STS3C.txt (23 lines)
│   │   │   │       ├── getConfigChangeIPInterworkingDetails.par (50 lines)
│   │   │   │       ├── getConfigChangeIPInterworkingDetails.rpl (1776 lines)
│   │   │   │       ├── getConfigChangeIPInterworkingDetailsParser_xdeIOSOutput.xsd (136 lines)
│   │   │   │       ├── sonet.txt (139 lines)
│   │   │   │       └── tdmandpep (33 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (29 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_ios_LAG_xde/
│   │   │   ├── getConfigChangeLAGDetails.xpa/
│   │   │   │   └── getConfigChangeLAGDetails/
│   │   │   │       ├── getConfigChangeLAGDetails.par (50 lines)
│   │   │   │       ├── getConfigChangeLAGDetailsParser_xdeIOS.rpl (290 lines)
│   │   │   │       ├── getConfigChangeLAGDetailsParser_xdeIOSOutput.xsd (28 lines)
│   │   │   │       └── lag.txt (24 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (28 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_ios_SERIAL_xde/
│   │   │   ├── getConfigChangeSerialDetails.xpa/
│   │   │   │   └── getConfigChangeSerialDetails/
│   │   │   │       ├── D41.txt (175 lines)
│   │   │   │       ├── GCofig1 (94 lines)
│   │   │   │       ├── getConfigChangeSerialDetails.par (50 lines)
│   │   │   │       ├── getConfigChangeSerialDetailsParser_xdeIOS.rpl (1014 lines)
│   │   │   │       ├── getConfigChangeSerialDetailsParser_xdeIOSOutput.xsd (73 lines)
│   │   │   │       └── tdmandpep (33 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (27 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_ios_ipsla_twamp_xde/
│   │   │   ├── getIpSlaTwampConfigChanges.xpa/
│   │   │   │   └── getIpSlaTwampChanges/
│   │   │   │       ├── Output_InactiveTime.txt (10 lines)
│   │   │   │       ├── Output_InactiveTimeout_ServerInactiveTimeout_Port.txt (12 lines)
│   │   │   │       ├── Output_Port.txt (7 lines)
│   │   │   │       ├── Output_ServerInactiveTimeout.txt (2 lines)
│   │   │   │       ├── Output_ServerInactiveTimeout_Port.txt (8 lines)
│   │   │   │       ├── Output_XE_InactiveTime.txt (10 lines)
│   │   │   │       ├── Output_XR.txt (16 lines)
│   │   │   │       ├── getIpSlaTwampChanges.par (50 lines)
│   │   │   │       ├── getIpSlaTwampChangesParser_xdeIOS.rpl (135 lines)
│   │   │   │       └── getIpSlaTwampChangesParser_xdeIOSOutput.xsd (21 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (32 lines)
│   │   │   └── xmpxde.xml (46 lines)
│   │   ├── ce_config_change_ios_xe_VCOP_xde/
│   │   │   ├── getVCOPConfigDetails.xpa/
│   │   │   │   └── getVCOPConfigDeatails/
│   │   │   │       ├── VCOP_Granular_Output (6 lines)
│   │   │   │       ├── getVCOPConfigDeatails.par (23 lines)
│   │   │   │       ├── getVCOPConfigDeatailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getVCOPConfigDeatailsParser_xdeIOS.rpl (103 lines)
│   │   │   │       └── getVCOPConfigDeatailsParser_xdeIOSOutput.xsd (25 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── ce_config_change_ios_xe_g8032_ethernet_ring/
│   │   │   ├── getRingNameInstance.xpa/
│   │   │   │   └── getRingNameInstanceName/
│   │   │   │       ├── getRingNameInstanceName.par (23 lines)
│   │   │   │       ├── getRingNameInstanceNameParser_xdeIOSOutput.xsd (47 lines)
│   │   │   │       ├── getRingName_InstanceName_xdeIOS_XE.rpl (655 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE.txt (18 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE5.txt (28 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE6.txt (21 lines)
│   │   │   │       └── sampleDeviceOutputIOS_XE7.txt (27 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_ios_xe_ipprefixlist/
│   │   │   ├── getPrefixlistChanges.xpa/
│   │   │   │   └── getPrefixlistChanges/
│   │   │   │       ├── getPrefixlistChanges.par (50 lines)
│   │   │   │       ├── getPrefixlistChangesParserOutput.xsd (6 lines)
│   │   │   │       ├── getPrefixlistChangesParser_xdeIOS.rpl (206 lines)
│   │   │   │       ├── getPrefixlistChangesParser_xdeIOSOutput.xsd (32 lines)
│   │   │   │       ├── output_delete_name.txt (103 lines)
│   │   │   │       ├── output_description.txt (33 lines)
│   │   │   │       └── output_no_yes.txt (103 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (46 lines)
│   │   ├── ce_config_change_ios_xe_synceth_xde/
│   │   │   ├── getSynceGlobalDetails.xpa/
│   │   │   │   └── getSynceGlobalConfigDetails/
│   │   │   │       ├── OutputIOS_XE.txt (7 lines)
│   │   │   │       ├── OutputInterFaceHold.txt (6 lines)
│   │   │   │       ├── OutputInterFacePrirty.txt (7 lines)
│   │   │   │       ├── OutputInterFaceWait.txt (5 lines)
│   │   │   │       ├── OutputInterPriority.txt (3 lines)
│   │   │   │       ├── OutputNoInterFacePrirty.txt (7 lines)
│   │   │   │       ├── getSynceGlobalConfigDetails.out.xml (0 lines)
│   │   │   │       ├── getSynceGlobalConfigDetails.par (23 lines)
│   │   │   │       ├── getSynceGlobalConfigDetailsParser_xdeIOS.rpl (317 lines)
│   │   │   │       ├── getSynceGlobalConfigDetailsParser_xdeIOSOutput.xsd (26 lines)
│   │   │   │       ├── outputExternalR0.txt (7 lines)
│   │   │   │       ├── outputExternalR0E1CRC4.txt (4 lines)
│   │   │   │       ├── outputGlbEsmc.txt (3 lines)
│   │   │   │       ├── outputGlbHold.txt (5 lines)
│   │   │   │       ├── outputGlbNoEsmc.txt (3 lines)
│   │   │   │       ├── outputGlbNoRetrive.txt (3 lines)
│   │   │   │       ├── outputGlbQlModeDisable.txt (7 lines)
│   │   │   │       ├── outputGlbQlModeEnable.txt (4 lines)
│   │   │   │       ├── outputGlbRetrive.txt (4 lines)
│   │   │   │       ├── outputGlbWait.txt (5 lines)
│   │   │   │       ├── outputGlobal.txt (5 lines)
│   │   │   │       ├── outputGlobal1.txt (5 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE.txt (7 lines)
│   │   │   │       └── sampleDeviceOutputIOS_XE1.txt (24 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_ios_xr_synceth_xde/
│   │   │   ├── getSynceGlobalDetails.xpa/
│   │   │   │   ├── getSynceGlobalConfigDetails/
│   │   │   │   │   ├── getSynceGlobalConfigDetails.par (23 lines)
│   │   │   │   │   ├── getSynceGlobalConfigDetailsParser_xdeIOS.rpl (289 lines)
│   │   │   │   │   └── getSynceGlobalConfigDetailsParser_xdeIOSOutput.xsd (31 lines)
│   │   │   │   ├── xr-granular-delete-interface.txt (8 lines)
│   │   │   │   └── xr-granular-inputs (37 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_IMOpMode_xde/
│   │   │   ├── getConfigChangeIMOpModeDetails.xpa/
│   │   │   │   └── getConfigChangeIMOpModeDetails/
│   │   │   │       ├── 10.104.120.184_4_Port_Only_Config (21 lines)
│   │   │   │       ├── 10.104.120.41_10G-Config.txt (12 lines)
│   │   │   │       ├── 10.104.120.41_5G-Config.txt (7 lines)
│   │   │   │       ├── 10.104.120.41_5G_Config.txt (75 lines)
│   │   │   │       ├── 10.104.120.41_default_10G.txt (89 lines)
│   │   │   │       ├── celebornBandwidth_Config.txt (18 lines)
│   │   │   │       ├── celeborn_Input.txt (494 lines)
│   │   │   │       ├── getConfigChangeIMOpModeDetails.par (50 lines)
│   │   │   │       ├── getConfigChangeIMOpModeDetailsParserOutput.xsd (30 lines)
│   │   │   │       ├── getConfigChangeIMOpModeDetailsParser_xdeIOS.rpl (388 lines)
│   │   │   │       └── getConfigChangeIMOpModeDetailsParser_xdeIOSOutput.xsd (34 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── ce_config_change_iosxe_PsudowireEndpoint/
│   │   │   ├── getPseudowireendpoint.xpa/
│   │   │   │   └── getPseudowireendpoint/
│   │   │   │       ├── EM_Output.txt (27 lines)
│   │   │   │       ├── SampleOutput2_CSCva87820.txt (25 lines)
│   │   │   │       ├── SampleOutput_CSCva87820.txt (19 lines)
│   │   │   │       ├── SampleOutput_CSCva87820_Derecho.txt (20 lines)
│   │   │   │       ├── SampleOutput_CSCva87820_Derecho_FromIfmInventoryLogs.txt (22 lines)
│   │   │   │       ├── getPseudowireEnpoint_IOSOutput.xsd (198 lines)
│   │   │   │       ├── getPseudowireendpointInstanceName.par (23 lines)
│   │   │   │       ├── getPseudowireendpoint_InstanceName_IOS_XE.rpl (2003 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_EVPN.txt (75 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE.txt (60 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE1.txt (5 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE5.txt (6 lines)
│   │   │   │       ├── sampleoutput (6 lines)
│   │   │   │       └── sampleoutput_xconnect_context (5 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (26 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxe_ains/
│   │   │   ├── getAins.xpa/
│   │   │   │   ├── getAinsDetails/
│   │   │   │   │   ├── getAinsDetails.par (50 lines)
│   │   │   │   │   ├── getAinsDetailsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getAinsDetailsParser_xdeIOS.rpl (83 lines)
│   │   │   │   │   ├── getAinsDetailsParser_xdeIOSOutput.xsd (30 lines)
│   │   │   │   │   └── output.txt (101 lines)
│   │   │   │   └── getBkDetails/
│   │   │   │       ├── getBkDetails.map (7 lines)
│   │   │   │       ├── getBkDetails.par (55 lines)
│   │   │   │       ├── getBkDetailsOutput.xsd (27 lines)
│   │   │   │       └── xmp-im-physical-resource-module.xsd (1005 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (76 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_bgp_xde/
│   │   │   ├── getBgpConfChange.xpa/
│   │   │   │   └── getConfChangeBgpNeighborDetails/
│   │   │   │       ├── BGP (6 lines)
│   │   │   │       ├── BGPInput (15 lines)
│   │   │   │       ├── af_167 (108 lines)
│   │   │   │       ├── getConfChangeBgpNeighborDetails.par (23 lines)
│   │   │   │       ├── getConfChangeBgpNeighborDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getConfChangeBgpNeighborDetailsParser_xdeIOS.rpl (2673 lines)
│   │   │   │       └── getConfChangeBgpNeighborDetailsParser_xdeIOSOutput.xsd (30 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (28 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxe_ethernetFlowPoint/
│   │   │   ├── getEthernetFlowPoint.xpa/
│   │   │   │   └── getEthernetFlowPointinstanceName/
│   │   │   │       ├── SampleDeviceOutputIOS_XE_EVPN_MULTIPOINT.txt (36 lines)
│   │   │   │       ├── getEthernetFlowPointParser_xdeIOSOutput.xsd (178 lines)
│   │   │   │       ├── getEthernetFlowPointinstanceName.par (23 lines)
│   │   │   │       ├── getEthernetFlowPointinstanceName_IOS_XE.rpl (2835 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_EVPN.txt (39 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE.txt (60 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE1.txt (5 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE5.txt (6 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE6.txt (9 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE_EVPLAN.txt (24 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE_EVPLAN_EVPN.txt (18 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XE_EVPLAN_EVPN_Order1.txt (24 lines)
│   │   │   │       ├── sampleoutput (6 lines)
│   │   │   │       └── sampleoutput_xconnect_context (5 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (26 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxe_isis_xde/
│   │   │   ├── getConfigChangeIsisDetails.xpa/
│   │   │   │   └── getConfigChangeIsisDetails/
│   │   │   │       ├── getConfigChangeIsisDetails.par (49 lines)
│   │   │   │       ├── getConfigChangeIsisDetails.rpl (141 lines)
│   │   │   │       ├── getConfigChangeIsisDetailsOutput.xsd (30 lines)
│   │   │   │       ├── output.txt (1 lines)
│   │   │   │       ├── output_iosxe_pep.txt (13 lines)
│   │   │   │       ├── output_neighbor_interface.txt (16 lines)
│   │   │   │       └── output_net.txt (4 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_mplstefrr/
│   │   │   ├── getMplsTeFrr.xpa/
│   │   │   │   └── getMplsTeFrr/
│   │   │   │       ├── NCS42XX_AutoBackup (103 lines)
│   │   │   │       ├── NCS42XX_Bandwidth (103 lines)
│   │   │   │       ├── getMplsTeFrrName.par (49 lines)
│   │   │   │       └── getMplsTeFrr_InstanceName_IOS_XE.rpl (46 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (27 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_ospf_xde/
│   │   │   ├── getInterfaceName.xpa/
│   │   │   │   └── getInterfaceName/
│   │   │   │       ├── Xoutput_conf.txt (90 lines)
│   │   │   │       ├── getInterfaceName.out.xml (0 lines)
│   │   │   │       ├── getInterfaceName.par (23 lines)
│   │   │   │       ├── getInterfaceNameParser_xdeIOS.rpl (741 lines)
│   │   │   │       ├── getInterfaceNameParser_xdeIOSOutput.xsd (91 lines)
│   │   │   │       ├── output_conf.txt (126 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (48 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxe_port_ains/
│   │   │   ├── getAins.xpa/
│   │   │   │   └── getAinsDetails/
│   │   │   │       ├── getAinsDetails.par (50 lines)
│   │   │   │       ├── getAinsDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getAinsDetailsParser_xdeIOS.rpl (211 lines)
│   │   │   │       ├── getAinsDetailsParser_xdeIOSOutput.xsd (25 lines)
│   │   │   │       ├── output.txt (28 lines)
│   │   │   │       ├── output1.txt (14 lines)
│   │   │   │       ├── output2.txt (19 lines)
│   │   │   │       ├── output_ains_card.txt (11 lines)
│   │   │   │       ├── output_ains_card_no.txt (10 lines)
│   │   │   │       ├── output_ains_chasis.txt (17 lines)
│   │   │   │       └── output_ains_chasis_no.txt (8 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (185 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxe_portmirroring_xde/
│   │   │   ├── getPortMirroringConfigChangeDetails.xpa/
│   │   │   │   └── getPortMirroringConfigChangeDetails/
│   │   │   │       ├── archieve for NCS4200.txt (80 lines)
│   │   │   │       ├── archive for ASR903.txt (70 lines)
│   │   │   │       ├── getPortMirroringConfigChangeDetails.par (50 lines)
│   │   │   │       ├── getPortMirroringConfigChangeDetailsParser_xdeIOS.rpl (428 lines)
│   │   │   │       └── getPortMirroringConfigChangeDetailsParser_xdeIOSOutput.xsd (42 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (33 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxe_ptp_xde/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.xmp.config.xde/
│   │   │   │   │       └── ce_config_change_iosxe_ptp_xde/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (19 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── getConfigChangePTPDetails.xpa/
│   │   │   │   └── getConfigChangePTPDetails/
│   │   │   │       ├── getConfigChangePTPDetails.par (50 lines)
│   │   │   │       ├── getConfigChangePTPDetailsParser_xdeIOS.rpl (159 lines)
│   │   │   │       └── getConfigChangePTPDetailsParser_xdeIOSOutput.xsd (25 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_qos_xde/
│   │   │   ├── getQOSConfigChangeDetails.xpa/
│   │   │   │   └── getQOSConfigChangeDetails/
│   │   │   │       ├── 22_out.txt (88 lines)
│   │   │   │       ├── Xoutput_conf.txt (90 lines)
│   │   │   │       ├── getQOSConfigChangeDetails.par (49 lines)
│   │   │   │       ├── getQOSConfigChangeDetailsParser_xdeIOS.rpl (515 lines)
│   │   │   │       ├── getQOSConfigChangeDetailsParser_xdeIOSOutput.xsd (53 lines)
│   │   │   │       └── output_conf.txt (126 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (45 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── ce_config_change_iosxe_sdr/
│   │   │   ├── getSdr.xpa/
│   │   │   │   └── getSdrName/
│   │   │   │       ├── getSdrName.par (51 lines)
│   │   │   │       ├── getSdrNameParser_xdeIOS_XR.rpl (107 lines)
│   │   │   │       └── getSdrNameParser_xdeIOS_XROutput.xsd (31 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxe_segRouting_xde/
│   │   │   ├── getSegmenRoutingConfChange.xpa/
│   │   │   │   └── getSegmenRoutingDetails/
│   │   │   │       ├── Input (20 lines)
│   │   │   │       ├── getSegmenRoutingDetails.par (49 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParserOutput.xsd (64 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParser_xdeIOS.rpl (926 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParser_xdeIOSOutput.xsd (0 lines)
│   │   │   │       └── isis_output (34 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (29 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxr_LAG_xde/
│   │   │   ├── getConfigChangeLAGDetails.xpa/
│   │   │   │   └── getConfigChangeLAGDetails/
│   │   │   │       ├── getConfigChangeLAGDetails.par (51 lines)
│   │   │   │       ├── getConfigChangeLAGDetailsParser_xdeIOS.rpl (228 lines)
│   │   │   │       ├── getConfigChangeLAGDetailsParser_xdeIOSOutput.xsd (28 lines)
│   │   │   │       └── lag.txt (45 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (29 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxr_PsudowireEndpoint_xde/
│   │   │   ├── getConfChangePsudowireEndpointDetails.xpa/
│   │   │   │   └── getConfChangePsudowireEndpointDetails/
│   │   │   │       ├── getConfChangePsudowireEndpointDetails.par (24 lines)
│   │   │   │       ├── getConfChangePsudowireEndpointDetailsParser_xdeIOS_XR.rpl (1055 lines)
│   │   │   │       ├── getConfChangePsudowireEndpointDetailsParser_xdeIOS_XROutput.xsd (125 lines)
│   │   │   │       ├── sampleDeviceOutput_EVPN.txt (67 lines)
│   │   │   │       └── sampledeletepwwp.txt (17 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (22 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxr_bgp_xde/
│   │   │   ├── getBgpNeighborInfo.xpa/
│   │   │   │   └── getBgpNeighborInfo/
│   │   │   │       ├── getBgpNeighborInfo.par (24 lines)
│   │   │   │       ├── getBgpNeighborInfoParserOutput.xsd (6 lines)
│   │   │   │       ├── getBgpNeighborInfoParser_xdeIOS_XR.rpl (10069 lines)
│   │   │   │       ├── getBgpNeighborInfoParser_xdeIOS_XROutput.xsd (85 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (52 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (48 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (27 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxr_ethernetFlowPoint/
│   │   │   ├── getConfChangeEthernetFlowPointDetails.xpa/
│   │   │   │   └── getConfChangeEthernetFlowPointDetails/
│   │   │   │       ├── getConfChangeEthernetFlowPointDetails.par (24 lines)
│   │   │   │       ├── getConfChangeEthernetFlowPointDetailsParser_xdeIOS_XR.rpl (1216 lines)
│   │   │   │       ├── getConfChangeethernetFlowPointDetailsParser_xdeIOS_XROutput.xsd (124 lines)
│   │   │   │       ├── sample-ethernet-segment-identifier.txt (17 lines)
│   │   │   │       ├── sample-multipoint-create (26 lines)
│   │   │   │       ├── sampleDeviceOutput_EVPN.txt (22 lines)
│   │   │   │       ├── sampleInnerVlanChange.txt (6 lines)
│   │   │   │       ├── sampleMultipointDelete (4 lines)
│   │   │   │       └── sampledeletepwwp.txt (57 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (21 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxr_g8032_ethernet_ring/
│   │   │   ├── getRingNameInstance.xpa/
│   │   │   │   └── getRingNameInstanceName/
│   │   │   │       ├── Deletion_sampleDeviceOutputIOS_XR4.txt (16 lines)
│   │   │   │       ├── getRingNameInstanceName.par (24 lines)
│   │   │   │       ├── getRingNameInstanceNameParser_xdeIOSOutput.xsd (47 lines)
│   │   │   │       ├── getRingNameInstanceNameParser_xdeIOX.rpl (436 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (37 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR3.txt (88 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR4.txt (166 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR5.txt (29 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR6.txt (176 lines)
│   │   │   │       └── sampleDeviceOutputIOS_XR7.txt (15 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxr_iccp_xde/
│   │   │   ├── getIccpGrupDetails/
│   │   │   │   ├── cliOutput.txt (17 lines)
│   │   │   │   ├── cliOutput1.txt (41 lines)
│   │   │   │   ├── getIccpGrupDetails.par (50 lines)
│   │   │   │   ├── getIccpGrupDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getIccpGrupDetailsParser_xdeIOS_XR.rpl (304 lines)
│   │   │   │   └── getIccpGrupDetailsParser_xdeIOS_XROutput.xsd (34 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (20 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxr_ipsla_twamp_xde/
│   │   │   ├── getIpslatwampConfigChangeInfo.xpa/
│   │   │   │   └── getIpslatwampConfigChangeInfo/
│   │   │   │       ├── Output_Inactivity_ServerInactivity_Port.txt (14 lines)
│   │   │   │       ├── Output_XR_Port.txt (9 lines)
│   │   │   │       ├── Output_XR_ServerTimerInactivity.txt (8 lines)
│   │   │   │       ├── Output_XR_Timeout.txt (10 lines)
│   │   │   │       ├── Output_XR_TimerInactivity.txt (16 lines)
│   │   │   │       ├── getIpslatwampConfigChangeInfo.par (50 lines)
│   │   │   │       ├── getIpslatwampConfigChangeInfo_xdeIOS_XR.rpl (135 lines)
│   │   │   │       └── getIpslatwampConfigChangeInfo_xdeIOS_XROutput.xsd (21 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (27 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxr_ipsla_twamplight_xde/
│   │   │   ├── getIpslatwamplightConfigChangeInfo.xpa/
│   │   │   │   └── getIpslatwamplightConfigChangeInfo/
│   │   │   │       ├── Output_Inactivity_ServerInactivity_Port.txt (14 lines)
│   │   │   │       ├── Output_XR_Port.txt (9 lines)
│   │   │   │       ├── Output_XR_ServerTimerInactivity.txt (8 lines)
│   │   │   │       ├── Output_XR_Timeout.txt (10 lines)
│   │   │   │       ├── Output_XR_TimerInactivity.txt (16 lines)
│   │   │   │       ├── getIpslatwamplightConfigChangeInfo.par (50 lines)
│   │   │   │       ├── getIpslatwamplightConfigChangeInfo_xdeIOS_XR.rpl (305 lines)
│   │   │   │       ├── getIpslatwamplightConfigChangeInfo_xdeIOS_XROutput.xsd (42 lines)
│   │   │   │       └── getSessionTrial.txt (12 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (27 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxr_isis_xde/
│   │   │   ├── getConfigChangeIsisDetails.xpa/
│   │   │   │   └── getConfigChangeIsisDetails/
│   │   │   │       ├── getConfigChangeIsisDetails.par (50 lines)
│   │   │   │       ├── getConfigChangeIsisDetails.rpl (102 lines)
│   │   │   │       ├── getConfigChangeIsisDetailsOutput.xsd (31 lines)
│   │   │   │       └── output_neighbor_interface.txt (6 lines)
│   │   │   ├── javascript/
│   │   │   │   ├── getInterfaceFullNames.xjs (31 lines)
│   │   │   │   └── getIsisPep.xjs (41 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxr_mplstefrr/
│   │   │   ├── getMplsTeFrr.xpa/
│   │   │   │   └── getMplsTeFrr/
│   │   │   │       ├── getMplsTeFrrName.par (49 lines)
│   │   │   │       ├── getMplsTeFrr_InstanceName_IOS_XR.rpl (49 lines)
│   │   │   │       └── output.txt (8 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (25 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── ce_config_change_iosxr_ospf_xde/
│   │   │   ├── getConfigChangeOspfDetails.xpa/
│   │   │   │   └── getConfigChangeOspfDetails/
│   │   │   │       ├── getConfigChangeOspfDetails.par (24 lines)
│   │   │   │       ├── getConfigChangeOspfDetails.rpl (1375 lines)
│   │   │   │       ├── getConfigChangeOspfDetailsOutput.xsd (6 lines)
│   │   │   │       ├── outpu_neighbor.txt (23 lines)
│   │   │   │       ├── output_global.txt (49 lines)
│   │   │   │       └── output_v3.txt (106 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (23 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ce_config_change_iosxr_qos_xde/
│   │   │   ├── getQOSConfigChangeDetails.xpa/
│   │   │   │   └── getQOSConfigChangeDetails/
│   │   │   │       ├── getQOSConfigChangeDetails.par (50 lines)
│   │   │   │       ├── getQOSConfigChangeDetailsOutput.xsd (44 lines)
│   │   │   │       ├── getQOSConfigChangeDetailsParser_xdeXR.rpl (391 lines)
│   │   │   │       ├── output.txt (33 lines)
│   │   │   │       ├── output_pm_cm.txt (38 lines)
│   │   │   │       └── output_update.txt (30 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (24 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ce_config_change_iosxr_segRouting_xde/
│   │   │   ├── getSegmenRoutingConfChange.xpa/
│   │   │   │   └── getSegmenRoutingDetails/
│   │   │   │       ├── Input (107 lines)
│   │   │   │       ├── Output (64 lines)
│   │   │   │       ├── PCE_SR_Output_XR.txt (88 lines)
│   │   │   │       ├── getSegmenRoutingDetails.par (50 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParserOutput.xsd (141 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParser_xdeIOS.rpl (2134 lines)
│   │   │   │       ├── getSegmenRoutingDetailsParser_xdeIOSOutput.xsd (0 lines)
│   │   │   │       └── isis_output (33 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (26 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-NCS520CE-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (72 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-NCS5508-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (86 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-NCS5K-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (85 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-asr901s-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (76 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-asr90x-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (79 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.complaince.xde.compliance-prime-show-commands-ncs42xx-inventory/
│   │   │   ├── SH_COMMANDS.xpa/
│   │   │   │   └── collectPrimeShowCommands/
│   │   │   │       ├── collectPrimeShowCommands.par (52 lines)
│   │   │   │       ├── collectPrimeShowCommandsParser.rpl (3 lines)
│   │   │   │       └── collectPrimeShowCommandsParserOutput.xsd (6 lines)
│   │   │   ├── collectPrimeIOSShowCommands.xde (78 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (34 lines)
│   │   ├── com.cisco.prime.config.xde.BDI_config/
│   │   │   ├── createBDIInterface.xpa/
│   │   │   │   ├── bdiCreateAndUpdateWriter/
│   │   │   │   │   ├── bdiCreateAndUpdateWriter.par (75 lines)
│   │   │   │   │   ├── ios.vtl (13 lines)
│   │   │   │   │   └── iosxr.vtl (14 lines)
│   │   │   │   ├── bdiDeleteWriter/
│   │   │   │   │   ├── bdiDeleteWriter.par (79 lines)
│   │   │   │   │   ├── ios.vtl (18 lines)
│   │   │   │   │   └── iosxr.vtl (30 lines)
│   │   │   │   ├── testBDI/
│   │   │   │   │   ├── create_bdi.xft (60 lines)
│   │   │   │   │   ├── create_bdiXR.xft (61 lines)
│   │   │   │   │   ├── delete_bdi.xft (57 lines)
│   │   │   │   │   └── delete_bdiXR.xft (61 lines)
│   │   │   │   └── updateAction/
│   │   │   │       ├── updateAction.par (21 lines)
│   │   │   │       └── updateAction.vtl (19 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── bdiCreateProcedure.xde (14 lines)
│   │   │   ├── bdiDeleteProcedure.xde (14 lines)
│   │   │   ├── bdiUpdateProcedure.xde (31 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.ains-config/
│   │   │   ├── ains.xpa/
│   │   │   │   ├── ainsCreateAndUpdateWriter/
│   │   │   │   │   ├── ainsCreateAndUpdateWriter.par (40 lines)
│   │   │   │   │   └── ios.vtl (66 lines)
│   │   │   │   └── ainsDeleteWriter/
│   │   │   │       ├── ainsDeleteWriter.par (37 lines)
│   │   │   │       └── ios.vtl (0 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ainsCreateProcedure.xde (23 lines)
│   │   │   ├── ainsDeleteProcedure.xde (22 lines)
│   │   │   ├── ainsUpdateProcedure.xde (59 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.ains-port-config/
│   │   │   ├── ains.xpa/
│   │   │   │   ├── ainsCreateAndUpdateWriter/
│   │   │   │   │   ├── ainsCreateAndUpdateWriter.par (40 lines)
│   │   │   │   │   └── ios.vtl (167 lines)
│   │   │   │   └── ainsDeleteWriter/
│   │   │   │       ├── ainsDeleteWriter.par (37 lines)
│   │   │   │       └── ios.vtl (0 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ainsCreateProcedure.xde (23 lines)
│   │   │   ├── ainsDeleteProcedure.xde (22 lines)
│   │   │   ├── ainsUpdateProcedure.xde (70 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.config.xde.card-protection-config/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.config.xde/
│   │   │   │   │       └── card-protection-config/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (18 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── cardProtection.xpa/
│   │   │   │   ├── cardProtectionCreateAndUpdateWriter/
│   │   │   │   │   ├── cardProtectionConfigCreateAndUpdateWriter.par (52 lines)
│   │   │   │   │   └── config.vtl (66 lines)
│   │   │   │   └── cardProtectionDeleteWriter/
│   │   │   │       ├── cardProtectionDelete.vtl (11 lines)
│   │   │   │       └── cardProtectionDeleteWriter.par (40 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── cardProtectionCreateProcedure.xde (27 lines)
│   │   │   ├── cardProtectionDeleteProcedure.xde (25 lines)
│   │   │   ├── cardProtectionUpdateProcedure.xde (138 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── error.xml (7 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.carrier-ethernet-pbb/
│   │   │   ├── cisco-carrier-ethernet-pbb.xpa/
│   │   │   │   ├── CreateAndUpdateWriter/
│   │   │   │   │   ├── CreateAndUpdateWriter.par (19 lines)
│   │   │   │   │   └── pbb_evpn.vtl (99 lines)
│   │   │   │   ├── DeleteWriter/
│   │   │   │   │   ├── DeleteWriter.par (19 lines)
│   │   │   │   │   └── pbb_evpn.vtl (82 lines)
│   │   │   │   ├── testForEMS/
│   │   │   │   │   └── ASR9K/
│   │   │   │   │       ├── Activate_bgpRouteTarget_asr9k.xft (32 lines)
│   │   │   │   │       ├── Activate_evpnEthernetSegment_asr9k.xft (36 lines)
│   │   │   │   │       ├── Activate_globalEvpnTimers_asr9K.xft (34 lines)
│   │   │   │   │       ├── Activate_pbbCoreBridgeDomain_asr9k.xft (36 lines)
│   │   │   │   │       ├── Activate_pbbEdgeBridgeDomain_asr9K.xft (37 lines)
│   │   │   │   │       ├── Delete_bgpRouteTarget_asr9k.xft (30 lines)
│   │   │   │   │       ├── Delete_evpnEthernetSegment_asr9k.xft (36 lines)
│   │   │   │   │       ├── Delete_globalEvpnTimers.xft (35 lines)
│   │   │   │   │       ├── Delete_pbbCoreBridgeDomain_asr9k.xft (32 lines)
│   │   │   │   │       └── Delete_pbbEdgeBridgeDomain_asr9k.xft (34 lines)
│   │   │   │   ├── prime-carrier-ethernet-pbb-model.xml (80 lines)
│   │   │   │   └── prime-carrier-ethernet-pbb-model.xsd (424 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── CreateProcedure.xde (23 lines)
│   │   │   ├── DeleteProcedure.xde (23 lines)
│   │   │   ├── UpdateProcedure.xde (31 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.cem-config/
│   │   │   ├── cem-config.xpa/
│   │   │   │   ├── cemCreateAndUpdateWriter/
│   │   │   │   │   ├── cemCreateAndUpdateWriter.par (48 lines)
│   │   │   │   │   └── iosXR.vtl (1556 lines)
│   │   │   │   ├── cemDeleteWriter/
│   │   │   │   │   ├── cemDeleteWriter.par (44 lines)
│   │   │   │   │   └── iosXR.vtl (1743 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── cemCreateLocalWithTimeslotAndRecoverdClock.xft (571 lines)
│   │   │   │   │       ├── cemCreateWithTransportSettingsLocalconnect.xft (448 lines)
│   │   │   │   │       ├── cemCreateWithTransportSettingsXconnect.xft (326 lines)
│   │   │   │   │       ├── cemCreateWithoutTransportSettingXconn.xft (312 lines)
│   │   │   │   │       ├── cemCreateWithoutTransportSettingsLocalConn.xft (420 lines)
│   │   │   │   │       ├── cemDeleteLocalconn.xft (440 lines)
│   │   │   │   │       ├── cemDeleteXconnect.xft (320 lines)
│   │   │   │   │       ├── createCem.xft (80 lines)
│   │   │   │   │       ├── createCemLocalWithTimeslot.xft (561 lines)
│   │   │   │   │       ├── createCemT3LocalWithSTS1E.xft (495 lines)
│   │   │   │   │       ├── createCemUPSRProtectionLocalConnect.xft (598 lines)
│   │   │   │   │       ├── createCemUPSRProtectionXconnect.xft (54 lines)
│   │   │   │   │       ├── deleteCEMUPSRProtectionXconnect.xft (51 lines)
│   │   │   │   │       └── deleteCemUPSRProtectionLocalConnect.xft (600 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── cemCreateProcedure.xde (66 lines)
│   │   │   ├── cemDeleteProcedure.xde (50 lines)
│   │   │   ├── cemUpdateProcedure.xde (16 lines)
│   │   │   ├── conf.xml (7 lines)
│   │   │   ├── customTags.xde (22 lines)
│   │   │   ├── error.xml (12 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── packageDescriptor.xml (27 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.cem-config-recovered-clock/
│   │   │   ├── cem-config.xpa/
│   │   │   │   ├── cemRecoveredClockCreateAndUpdateWriter/
│   │   │   │   │   ├── cemRecoveredClockCreateAndUpdateWriter.par (18 lines)
│   │   │   │   │   └── iosXR.vtl (64 lines)
│   │   │   │   ├── cemRecoveredClockDeleteWriter/
│   │   │   │   │   ├── cemRecoveredClockDeleteWriter.par (18 lines)
│   │   │   │   │   └── iosXR.vtl (64 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── cemRecoveredClockCreateProcedure.xde (24 lines)
│   │   │   ├── cemRecoveredClockDeleteProcedure.xde (20 lines)
│   │   │   ├── cemRecoveredClockUpdateProcedure.xde (18 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.eoam-ipSla-config/
│   │   │   ├── ipSla-config.xpa/
│   │   │   │   ├── ipSlaConfigCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXE.vtl (120 lines)
│   │   │   │   │   ├── iosXR.vtl (79 lines)
│   │   │   │   │   └── ipSlaConfigCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── ipSlaConfigDeleteWriter/
│   │   │   │   │   ├── iosXE.vtl (0 lines)
│   │   │   │   │   ├── iosXR.vtl (53 lines)
│   │   │   │   │   └── ipSlaConfigDeleteWriter.par (28 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ipSlaConfigCreateProcedure.xde (19 lines)
│   │   │   ├── ipSlaConfigDeleteProcedure.xde (14 lines)
│   │   │   ├── ipSlaConfigUpdateProcedure.xde (33 lines)
│   │   │   ├── packageDescriptor.xml (19 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.eowyn5g-config/
│   │   │   ├── eowyn5g.xpa/
│   │   │   │   ├── eowyn5gCreateAndUpdateWriter/
│   │   │   │   │   ├── eowyn5gCreateAndUpdateWriter.par (18 lines)
│   │   │   │   │   └── ios.vtl (35 lines)
│   │   │   │   ├── eowyn5gDeleteWriter/
│   │   │   │   │   ├── eowyn5gDeleteWriter.par (18 lines)
│   │   │   │   │   └── ios.vtl (11 lines)
│   │   │   │   └── testFromEMS/
│   │   │   │       └── iosXE/
│   │   │   │           ├── Output_IOS_XE.xml (14 lines)
│   │   │   │           ├── createEowyn5gSettings.xft (30 lines)
│   │   │   │           └── updateEowyn5gSettings.xft (44 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── eowyn5gCreateProcedure.xde (21 lines)
│   │   │   ├── eowyn5gDeleteProcedure.xde (21 lines)
│   │   │   ├── eowyn5gUpdateProcedure.xde (262 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.ethernet-oam/
│   │   │   ├── ethernet-oam.xpa/
│   │   │   │   ├── ethernet_OAMCreateAndUpdateWriter/
│   │   │   │   │   ├── ethernet_OAMCreateAndUpdateWriter.par (42 lines)
│   │   │   │   │   ├── ios.vtl (14 lines)
│   │   │   │   │   ├── iosXR.vtl (22 lines)
│   │   │   │   │   └── iosasr901.vtl (11 lines)
│   │   │   │   ├── ethernet_OAMDeleteWriter/
│   │   │   │   │   ├── ethernet_OAMDeleteWriter.par (106 lines)
│   │   │   │   │   ├── ios.vtl (9 lines)
│   │   │   │   │   ├── iosasr901.vtl (10 lines)
│   │   │   │   │   └── iosxr.vtl (9 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   └── Activate_EthOAM_asr903.xft (59 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       └── Activate_EthOAM_asr9k.xft (61 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ethernet_OAMCreateProcedure.xde (11 lines)
│   │   │   ├── ethernet_OAMDeleteProcedure.xde (11 lines)
│   │   │   ├── ethernet_OAMUpdateProcedure.xde (28 lines)
│   │   │   ├── excludeAssociations.xml (27 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.ethernet-oam-cfm/
│   │   │   ├── ethernet-oam-cfm.xpa/
│   │   │   │   ├── ethernetOAMCFMCreateAndUpdateWriter/
│   │   │   │   │   ├── ethernetOAMCFMCreateAndUpdateWriter.par (64 lines)
│   │   │   │   │   ├── ios.vtl (292 lines)
│   │   │   │   │   ├── iosME1200.vtl (163 lines)
│   │   │   │   │   ├── iosXR.vtl (413 lines)
│   │   │   │   │   └── iosasr901.vtl (199 lines)
│   │   │   │   ├── ethernetOAMCFMDeleteWriter/
│   │   │   │   │   ├── ME1200.vtl (14 lines)
│   │   │   │   │   ├── ethernetOAMCFMDeleteWriter.par (50 lines)
│   │   │   │   │   ├── ios.vtl (163 lines)
│   │   │   │   │   ├── iosasr901.vtl (111 lines)
│   │   │   │   │   └── iosxr.vtl (181 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── Activate_EthCFM_ELAN_asr901.xft (128 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_ELAN_asr903.xft (134 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_EVPLAN_asr901.xft (271 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_EVPLAN_asr903.xft (279 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_IOS_RX.xft (253 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_Multiple_asr901.xft (272 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_asr901.xft (273 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_asr903.xft (275 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_ncs42xx.xft (284 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_ELAN_asr901.xft (121 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_ELAN_asr903.xft (127 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_EVPLAN_asr901.xft (256 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_EVPLAN_asr903.xft (263 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_IOS_RX.xft (291 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_asr901.xft (256 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_asr903.xft (262 lines)
│   │   │   │   │   │   └── Cease_EthCFM_ncs42xx.xft (267 lines)
│   │   │   │   │   ├── asr9k/
│   │   │   │   │   │   ├── Activate_EthCFM_ELAN_asr9k.xft (129 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_Multi_asr9k.xft (558 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_asr9k.xft (290 lines)
│   │   │   │   │   │   ├── Activate_EthCFM_ncs4k.xft (298 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_ELAN_asr9k.xft (126 lines)
│   │   │   │   │   │   ├── Cease_EthCFM_asr9k.xft (193 lines)
│   │   │   │   │   │   └── Cease_EthCFM_ncs4k.xft (194 lines)
│   │   │   │   │   └── me1200/
│   │   │   │   │       ├── Activate_EthCFM_ME1200_PM1.xft (228 lines)
│   │   │   │   │       ├── Activate_EthCFM_ME1200_PM1withRangedVlan.xft (227 lines)
│   │   │   │   │       ├── Activate_EthCFM_ME1200_PM2.xft (292 lines)
│   │   │   │   │       ├── Activate_EthCFM_ME1200_PM3.xft (289 lines)
│   │   │   │   │       ├── Activate_EthCFM_ME1200_PM4.xft (291 lines)
│   │   │   │   │       ├── Activate_EthCFM_ME1200_WithoutOAM.xft (164 lines)
│   │   │   │   │       └── Deactivate_EthCFM_ME1200.xft (269 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── ethernetOAMCFMCreateProcedure.xde (14 lines)
│   │   │   ├── ethernetOAMCFMDeleteProcedure.xde (14 lines)
│   │   │   ├── ethernetOAMCFMUpdateProcedure.xde (28 lines)
│   │   │   ├── excludeAssociations.xml (27 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.prime.config.xde.ethernet-oam-elmi/
│   │   │   ├── ethernet-oam-ELMI.xpa/
│   │   │   │   ├── ethernetOAMELMICreateAndUpdateWriter/
│   │   │   │   │   ├── ethernetOAMELMICreateAndUpdateWriter.par (140 lines)
│   │   │   │   │   ├── ios.vtl (117 lines)
│   │   │   │   │   └── iosXR.vtl (78 lines)
│   │   │   │   ├── ethernetOAMELMIDeleteWriter/
│   │   │   │   │   ├── ethernetOAMELMIDeleteWriter.par (32 lines)
│   │   │   │   │   ├── ios.vtl (33 lines)
│   │   │   │   │   └── iosxr.vtl (27 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── Activate_EthELMI_asr903.xft (102 lines)
│   │   │   │   │   │   ├── Activate_EthELMI_ceVlan_Default_asr903.xft (101 lines)
│   │   │   │   │   │   └── Activate_EthELMI_noCevlan_asr903.xft (73 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       └── Activate_EthELMI_asr9k.xft (99 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ethernetOAMELMICreateProcedure.xde (11 lines)
│   │   │   ├── ethernetOAMELMIDeleteProcedure.xde (11 lines)
│   │   │   ├── ethernetOAMELMIUpdateProcedure.xde (28 lines)
│   │   │   ├── excludeAssociations.xml (27 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.prime.config.xde.ethernet-oam-pm/
│   │   │   ├── ethernet-oam-pm.xpa/
│   │   │   │   ├── ethernetOAMPMCreateAndUpdateWriter/
│   │   │   │   │   ├── ethernetOAMPMCreateAndUpdateWriter.par (28 lines)
│   │   │   │   │   ├── ios.vtl (36 lines)
│   │   │   │   │   └── iosXR.vtl (82 lines)
│   │   │   │   ├── ethernetOAMPMDeleteWriter/
│   │   │   │   │   ├── ethernetOAMPMDeleteWriter.par (28 lines)
│   │   │   │   │   ├── ios.vtl (31 lines)
│   │   │   │   │   └── iosxr.vtl (47 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   └── Activate_EthDelayMeast_asr903.xft (211 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       └── Activate_EthDelayMeast_asr9k.xft (248 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ethernetOAMPMCreateProcedure.xde (14 lines)
│   │   │   ├── ethernetOAMPMDeleteProcedure.xde (14 lines)
│   │   │   ├── ethernetOAMPMUpdateProcedure.xde (28 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.prime.config.xde.feature-ip-prefixlist-config/
│   │   │   ├── feature-ip-prefixlist-config.xpa/
│   │   │   │   ├── ipPrefixListCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (12 lines)
│   │   │   │   │   ├── iosXR.vtl (11 lines)
│   │   │   │   │   └── ipPrefixListCreateAndUpdateWriter.par (74 lines)
│   │   │   │   └── ipPrefixListDeleteWriter/
│   │   │   │       ├── ios.vtl (12 lines)
│   │   │   │       ├── iosxr.vtl (10 lines)
│   │   │   │       └── ipPrefixListDeleteWriter.par (74 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (25 lines)
│   │   │   ├── ipPrefixListCreateProcedure.xde (16 lines)
│   │   │   ├── ipPrefixListDeleteProcedure.xde (16 lines)
│   │   │   ├── ipPrefixListUpdateProcedure.xde (30 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.l3link-flowpoint-config/
│   │   │   ├── l3link_flowpoint_config.xpa/
│   │   │   │   ├── l3linkFlowPointCreateAndUpdate/
│   │   │   │   │   ├── ios.vtl (104 lines)
│   │   │   │   │   ├── iosxr.vtl (21 lines)
│   │   │   │   │   ├── l3linkFlowPointCreateAndUpdate.par (71 lines)
│   │   │   │   │   └── velocity_macros.vm (210 lines)
│   │   │   │   ├── l3linkFlowPointDelete/
│   │   │   │   │   ├── ios.vtl (35 lines)
│   │   │   │   │   ├── iosxr.vtl (8 lines)
│   │   │   │   │   └── l3linkFlowPointDelete.par (71 lines)
│   │   │   │   └── testl3linkFlowPoint/
│   │   │   │       ├── testEmsl3linkFlowPointCreateXR.xft (112 lines)
│   │   │   │       └── testEmsl3linkFlowPointDeleteXR.xft (77 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3linkFlowPointCreateProcedure.xde (14 lines)
│   │   │   ├── l3linkFlowPointDeleteProcedure.xde (14 lines)
│   │   │   ├── l3linkFlowPointUpdateProcedure.xde (28 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3link-ospf-delete-config/
│   │   │   ├── l3link_ospf_delete.xpa/
│   │   │   │   ├── l3linkOspfDelete/
│   │   │   │   │   ├── ios.vtl (95 lines)
│   │   │   │   │   ├── iosxr.vtl (60 lines)
│   │   │   │   │   └── l3linkOspfDelete.par (79 lines)
│   │   │   │   └── testl3linkOspfDelete/
│   │   │   │       ├── testEmsl3linkOspfDelete.xft (97 lines)
│   │   │   │       └── testEmsl3linkOspfDeleteXR.xft (95 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getDeviceType.xde (28 lines)
│   │   │   ├── l3linkOspfCreateProcedure.xde (28 lines)
│   │   │   ├── l3linkOspfDeleteProcedure.xde (28 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3link-te-config/
│   │   │   ├── l3link_te_config.xpa/
│   │   │   │   ├── createTrafficEng/
│   │   │   │   │   ├── createTrafficEng.par (71 lines)
│   │   │   │   │   ├── ios.vtl (25 lines)
│   │   │   │   │   └── iosxr.vtl (36 lines)
│   │   │   │   ├── deleteTrafficEng/
│   │   │   │   │   ├── deleteTrafficEng.par (71 lines)
│   │   │   │   │   ├── ios.vtl (21 lines)
│   │   │   │   │   └── iosxr.vtl (40 lines)
│   │   │   │   └── testTrafficEngineering/
│   │   │   │       ├── testcreateTrafficEngIOS.xft (27 lines)
│   │   │   │       ├── testcreateTrafficEngIOSXR.xft (25 lines)
│   │   │   │       ├── testdeleteTrafficEngIOS.xft (16 lines)
│   │   │   │       └── testdeleteTrafficEngIOSXR.xft (28 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3linkTeCreateProcedure.xde (14 lines)
│   │   │   ├── l3linkTeDeleteProcedure.xde (14 lines)
│   │   │   ├── packageDescriptor.xml (13 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-Ospf-config/
│   │   │   ├── l3vpn-Ospf-config.xpa/
│   │   │   │   ├── l3vpnOspfCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXE.vtl (89 lines)
│   │   │   │   │   ├── iosXR.vtl (119 lines)
│   │   │   │   │   └── l3vpnOspfCreateAndUpdateWriter.par (74 lines)
│   │   │   │   ├── l3vpnOspfDeleteWriter/
│   │   │   │   │   ├── iosXE.vtl (115 lines)
│   │   │   │   │   ├── iosXR.vtl (75 lines)
│   │   │   │   │   └── l3vpnOspfDeleteWriter.par (71 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── ASR903/
│   │   │   │   │   │   ├── Create_XE_Ospf_config-Redistribute.xft_old (127 lines)
│   │   │   │   │   │   ├── Create_XE_Ospf_config.xft_old (127 lines)
│   │   │   │   │   │   └── Delete_XE_Ospf_config.xft_old (123 lines)
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── Create_XR_Ospf_config-Auth-IpSecMD5-Clear.xft (359 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config-Auth-IpSecMD5-Encrypted.xft (359 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config-Auth-IpSecSHA1-Clear.xft (359 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config-Auth-IpSecSHA1-Encrypted.xft (359 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config-DomainType.xft (129 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config.xft (129 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config_No-Bfd.xft (127 lines)
│   │   │   │   │       ├── Create_XR_Ospf_config_fast_detect_disable.xft (129 lines)
│   │   │   │   │       └── Delete_XR_Ospf_config.xft (119 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── OSPF-FeatureDoc.xml (99 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpnOspfCreateProcedure.xde (45 lines)
│   │   │   ├── l3vpnOspfDeleteProcedure.xde (14 lines)
│   │   │   ├── l3vpnOspfUpdateProcedure.xde (31 lines)
│   │   │   ├── packageDescriptor.xml (17 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-bgp-config/
│   │   │   ├── l3vpn-Bgp-config.xpa/
│   │   │   │   ├── l3vpnBgpCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXE.vtl (177 lines)
│   │   │   │   │   ├── iosXR.vtl (289 lines)
│   │   │   │   │   └── l3vpnBgpCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── l3vpnBgpDeleteWriter/
│   │   │   │   │   ├── iosXE.vtl (117 lines)
│   │   │   │   │   ├── iosXR.vtl (118 lines)
│   │   │   │   │   └── l3vpnBgpDeleteWriter.par (28 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── ASR903/
│   │   │   │   │   │   ├── create-NeighborSetting-with-local-as-no-prepend-replace-as-dual-as.xft (178 lines)
│   │   │   │   │   │   ├── create-NeighborSetting-with-local-as-no-prepend-replace-as.xft (178 lines)
│   │   │   │   │   │   ├── create-NeighborSetting-with-local-as-no-prepend.xft (178 lines)
│   │   │   │   │   │   ├── create-NeighborSetting-with-local-as.xft (298 lines)
│   │   │   │   │   │   ├── createBgpProcess-Auth-Encrypted.xft (426 lines)
│   │   │   │   │   │   ├── createBgpProcess-Auth.xft (426 lines)
│   │   │   │   │   │   ├── createBgpProcess-IPv4-AddressFamily.xft (170 lines)
│   │   │   │   │   │   ├── createBgpProcess-IPv6-AddressFamily.xft (170 lines)
│   │   │   │   │   │   ├── createBgpProcess-NeighborSetting-with-IPv4-AddressFamily.xft (170 lines)
│   │   │   │   │   │   ├── createBgpProcess-NeighborSetting-with-IPv4-and-IPv6AddressFamily.xft (209 lines)
│   │   │   │   │   │   ├── createBgpProcess-ospf-Redistribute-match-internal.xft (105 lines)
│   │   │   │   │   │   ├── createBgpProcess-ospf-Redistribute-match-nssa.xft (137 lines)
│   │   │   │   │   │   ├── createBgpProcess-ospf-Redistribute.xft (91 lines)
│   │   │   │   │   │   ├── deleteBgpAfSettings-redistrubuteOspf.xft (118 lines)
│   │   │   │   │   │   ├── deleteBgpAfSettings-redistrubuteOspf2_enterna1_enternal2.xft (108 lines)
│   │   │   │   │   │   ├── deleteBgpAfSettings-redistrubuteOspf2_internal.xft (119 lines)
│   │   │   │   │   │   ├── deleteBgpAfSettings-redistrubuteOspf2_nssa-ext1_nssa-ext2.xft (119 lines)
│   │   │   │   │   │   ├── deleteBgpAfSettings.xft (59 lines)
│   │   │   │   │   │   ├── deleteBgpNeighborSettings-Auth.xft (284 lines)
│   │   │   │   │   │   ├── deleteBgpNeighborSettings.xft (144 lines)
│   │   │   │   │   │   └── deleteBgpProcessSettings.xft (332 lines)
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── create-NeighborSetting-with-local-as-no-prepend-replace-as-dual-as.xft (300 lines)
│   │   │   │   │       ├── create-NeighborSetting-with-local-as-no-prepend-replace-as.xft (301 lines)
│   │   │   │   │       ├── create-NeighborSetting-with-local-as-no-prepend.xft (301 lines)
│   │   │   │   │       ├── create-NeighborSetting-with-local-as.xft (298 lines)
│   │   │   │   │       ├── createBgpProcess-Auth-Both-AddressFamily.xft (518 lines)
│   │   │   │   │       ├── createBgpProcess-Auth.xft (412 lines)
│   │   │   │   │       ├── createBgpProcess-NeighborSetting-with-IPv4AddressFamily.xft (293 lines)
│   │   │   │   │       ├── createBgpProcess-NeighborSetting-with-IPv6AddressFamily.xft (252 lines)
│   │   │   │   │       ├── createBgpProcess-NeighborSetting.xft (293 lines)
│   │   │   │   │       ├── createBgpProcess-VRF-NAME.xft (206 lines)
│   │   │   │   │       ├── createBgpProcess-ospf-Redistribute-match-internal.xft (263 lines)
│   │   │   │   │       ├── createBgpProcess-ospf-Redistribute-match-nssa.xft (294 lines)
│   │   │   │   │       ├── createBgpProcess-ospf-Redistribute.xft (249 lines)
│   │   │   │   │       ├── createBgpProcess-ospfv3-Ipv4-Redistribute.xft (263 lines)
│   │   │   │   │       ├── createBgpProcessSettings.xft (293 lines)
│   │   │   │   │       ├── deleteBgpNeighborSettings.xft (143 lines)
│   │   │   │   │       ├── deleteBgpProcess-NeighborSetting-with-IPv4AddressFamily.xft (60 lines)
│   │   │   │   │       ├── deleteBgpProcess-NeighborSetting-with-IPv6AddressFamily.xft (93 lines)
│   │   │   │   │       ├── deleteBgpProcess-NeighborSetting.xft (131 lines)
│   │   │   │   │       ├── deleteBgpProcess-VRF-NAME.xft (53 lines)
│   │   │   │   │       ├── deleteBgpProcess-XR-Auth.xft (258 lines)
│   │   │   │   │       └── deleteBgpProcessSettings.xft (327 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (6 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpnBgpCreateProcedure.xde (19 lines)
│   │   │   ├── l3vpnBgpDeleteProcedure.xde (14 lines)
│   │   │   ├── l3vpnBgpUpdateProcedure.xde (31 lines)
│   │   │   ├── packageDescriptor.xml (17 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-hsrp/
│   │   │   ├── l3vpn-hsrp.xpa/
│   │   │   │   ├── l3vpnHsrpCreateAndUpdateWriter/
│   │   │   │   │   ├── cisco-iosxe-l3vpn-hsrp-ConfigCmds.vtl (50 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-hsrp-ConfigCmds.vtl (53 lines)
│   │   │   │   │   └── l3vpnHsrpCreateAndUpdateWriter.par (71 lines)
│   │   │   │   ├── l3vpnHsrpDeleteWriter/
│   │   │   │   │   ├── cisco-iosxe-l3vpn-hsrp-delete-ConfigCmds.vtl (37 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-hsrp-delete-ConfigCmds.vtl (49 lines)
│   │   │   │   │   └── l3vpnHsrpDeleteWriter.par (71 lines)
│   │   │   │   └── tests/
│   │   │   │       ├── IOS-XE/
│   │   │   │       │   ├── CreateL3vpnHsrpGroupPepSettingsXE.xft (154 lines)
│   │   │   │       │   ├── DeleteL3vpnHsrpGroupPepSettings.xft (151 lines)
│   │   │   │       │   └── DeleteL3vpnHsrpPepSettings.xft (131 lines)
│   │   │   │       └── IOS-XR/
│   │   │   │           ├── CreateL3vpnHsrpGroupPepSettings.xft (172 lines)
│   │   │   │           ├── CreateL3vpnHsrpGroupPepSettings2.xft (170 lines)
│   │   │   │           ├── DeleteL3vpnHsrpGroupPepSettings.xft (222 lines)
│   │   │   │           └── DeleteL3vpnHsrpPepSettings.xft (202 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpnHsrpCreateProcedure.xde (24 lines)
│   │   │   ├── l3vpnHsrpDeleteProcedure.xde (23 lines)
│   │   │   ├── l3vpnHsrpUpdateProcedure.xde (29 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-interface/
│   │   │   ├── l3vpn-interface.xpa/
│   │   │   │   ├── l3vpnInterfaceCreateAndUpdateWriter/
│   │   │   │   │   ├── cisco-cat6500-l3vpn-interface-ConfigCmds.vtl (69 lines)
│   │   │   │   │   ├── cisco-iosxe-l3vpn-interface-ConfigCmds.vtl (30 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-interface-ConfigCmds.vtl (28 lines)
│   │   │   │   │   ├── l3vpnVrfCreateAndUpdateWriter.par (102 lines)
│   │   │   │   │   └── velocity_macros.vm (260 lines)
│   │   │   │   ├── l3vpnInterfaceDeleteWriter/
│   │   │   │   │   ├── cisco-cat6500-l3vpn-interface-delete-ConfigCmds.vtl (76 lines)
│   │   │   │   │   ├── cisco-iosxe-l3vpn-interface-delete-ConfigCmds.vtl (14 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-interface-delete-ConfigCmds.vtl (57 lines)
│   │   │   │   │   ├── l3vpnInterfaceDeleteWriter.par (106 lines)
│   │   │   │   │   └── velocity_macros.vm (35 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── cease_l3vpn_vrf_iosxe_asr903.xft (65 lines)
│   │   │   │   │   │   ├── create_l3vpn_interface-EthernetSubInterface-ASR903-Inactive-State.xft (64 lines)
│   │   │   │   │   │   ├── create_l3vpn_interface-EthernetSubInterface-ASR903.xft (64 lines)
│   │   │   │   │   │   └── create_l3vpn_interface-encapsulation-ASR903.xft (72 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       ├── cease_l3vpn_interface-EthernetSubInterface-ASR9K.xft (63 lines)
│   │   │   │   │       └── create_l3vpn_interface-EthernetSubInterface-ASR9K.xft (64 lines)
│   │   │   │   ├── prime-ethernet-resource-model.xml (58 lines)
│   │   │   │   └── prime-ethernet-resource-model.xsd (210 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpnInterfaceCreateProcedure.xde (15 lines)
│   │   │   ├── l3vpnInterfaceDeleteProcedure.xde (19 lines)
│   │   │   ├── l3vpnInterfaceUpdateProcedure.xde (28 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-ipSla-config/
│   │   │   ├── ipSla-config.xpa/
│   │   │   │   ├── ipSlaConfigCreateAndUpdateWriter/
│   │   │   │   │   ├── cat6500.vtl (182 lines)
│   │   │   │   │   ├── iosXE.vtl (182 lines)
│   │   │   │   │   ├── iosXR.vtl (242 lines)
│   │   │   │   │   └── ipSlaConfigCreateAndUpdateWriter.par (38 lines)
│   │   │   │   ├── ipSlaConfigDeleteWriter/
│   │   │   │   │   ├── deleteIpSlaCat6500.vtl (177 lines)
│   │   │   │   │   ├── deleteIpSlaIosXE.vtl (177 lines)
│   │   │   │   │   ├── deleteIpSlaIosXR.vtl (243 lines)
│   │   │   │   │   └── ipSlaConfigDeleteWriter.par (101 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── ASR903/
│   │   │   │   │   │   ├── Delete_icmpPath_Echo.xft (266 lines)
│   │   │   │   │   │   ├── Delete_icmpPath_Echo_StartTime_Now.xft (266 lines)
│   │   │   │   │   │   ├── Delete_icmpPath_Echo_starttime-01.xft (266 lines)
│   │   │   │   │   │   ├── icmpPath_Echo_AverageType.xft (132 lines)
│   │   │   │   │   │   ├── icmpPath_Jitter.xft (122 lines)
│   │   │   │   │   │   ├── icmpPath_Jitter_Average.xft (121 lines)
│   │   │   │   │   │   ├── icmpPath_Jitter_ConsecutiveType.xft (123 lines)
│   │   │   │   │   │   ├── icmpPath_Jitter_XofY.xft (123 lines)
│   │   │   │   │   │   ├── udp_Echo.xft (130 lines)
│   │   │   │   │   │   ├── udp_Echo_ControlDisabled.xft (131 lines)
│   │   │   │   │   │   ├── udp_Echo_ControlEnabled.xft (131 lines)
│   │   │   │   │   │   ├── udp_Echo_NoControlenabled.xft (131 lines)
│   │   │   │   │   │   └── udp_Jitter_ControlDisabled.xft (129 lines)
│   │   │   │   │   └── ASR9K/
│   │   │   │   │       ├── IosXR-icmpPath_Echo_ActionType-trigger.xft (139 lines)
│   │   │   │   │       ├── IosXR-icmpPath_Echo_AverageType.xft (139 lines)
│   │   │   │   │       ├── IosXR-icmpPath_Echo_Variable-connection-loss.xft (138 lines)
│   │   │   │   │       ├── IosXR-icmpPath_Echo_Variable-verify-error.xft (138 lines)
│   │   │   │   │       ├── delete-Ipsla-Reaction-XR.xft (132 lines)
│   │   │   │   │       └── delete-Ipsla-XR.xft (132 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── ipSlaConfigCreateProcedure.xde (19 lines)
│   │   │   ├── ipSlaConfigDeleteProcedure.xde (14 lines)
│   │   │   ├── ipSlaConfigUpdateProcedure.xde (33 lines)
│   │   │   ├── packageDescriptor.xml (19 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.l3vpn-vrf/
│   │   │   ├── l3vpn-vrf.xpa/
│   │   │   │   ├── l3vpnVrfCreateAndUpdateWriter/
│   │   │   │   │   ├── cisco-cat-6500-l3vpn-vrf-ConfigCmds.vtl (137 lines)
│   │   │   │   │   ├── cisco-cat-6500-l3vpn-vrf-ConfigCmds_V2.vtl (142 lines)
│   │   │   │   │   ├── cisco-iosxe-901s-l3vpn-vrf-ConfigCmds.vtl (147 lines)
│   │   │   │   │   ├── cisco-iosxe-l3vpn-vrf-ConfigCmds.vtl (147 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-vrf-ConfigCmds.vtl (142 lines)
│   │   │   │   │   ├── cisco-iosxr-ncs5k-l3vpn-vrf-ConfigCmds.vtl (139 lines)
│   │   │   │   │   └── l3vpnVrfCreateAndUpdateWriter.par (199 lines)
│   │   │   │   ├── l3vpnVrfDeleteWriter/
│   │   │   │   │   ├── cisco-cat6500-l3vpn-vrf-delete-ConfigCmds.vtl (84 lines)
│   │   │   │   │   ├── cisco-iosxe-901s-l3vpn-vrf-delete-ConfigCmds.vtl (91 lines)
│   │   │   │   │   ├── cisco-iosxe-l3vpn-vrf-delete-ConfigCmds.vtl (96 lines)
│   │   │   │   │   ├── cisco-iosxr-l3vpn-vrf-delete-ConfigCmds.vtl (110 lines)
│   │   │   │   │   └── l3vpnVrfDeleteWriter.par (142 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── asr901/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxe_asr901.xft (193 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxe_asr901.xft (135 lines)
│   │   │   │   │   ├── asr902/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxe_asr902.xft (193 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxe_asr902.xft (135 lines)
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxe_asr903.xft (217 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxe_asr903.xft (135 lines)
│   │   │   │   │   ├── asr920/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxe_asr920.xft (194 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxe_asr920.xft (135 lines)
│   │   │   │   │   ├── asr9k/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxr_asr9k.xft (185 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxr_asr9k.xft (136 lines)
│   │   │   │   │   ├── me3600x/
│   │   │   │   │   │   ├── activate_l3vpn_vrf_iosxe_me3600x.xft (193 lines)
│   │   │   │   │   │   └── cease_l3vpn_vrf_iosxe_me3600x.xft (135 lines)
│   │   │   │   │   └── me3800x/
│   │   │   │   │       ├── activate_l3vpn_vrf_iosxe_me3800x.xft (193 lines)
│   │   │   │   │       └── cease_l3vpn_vrf_iosxe_me3800x.xft (135 lines)
│   │   │   │   └── xmp-im-vrf-module.xsd (109 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpnVrfCreateProcedure.xde (95 lines)
│   │   │   ├── l3vpnVrfDeleteProcedure.xde (19 lines)
│   │   │   ├── l3vpnVrfUpdateProcedure.xde (34 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.ldp-config/
│   │   │   ├── ldpConfig.xpa/
│   │   │   │   ├── ldpConfigCreateAndUpdateWriter/
│   │   │   │   │   ├── config.vtl (68 lines)
│   │   │   │   │   ├── config_XR.vtl (60 lines)
│   │   │   │   │   └── ldpConfigCreateAndUpdateWriter.par (74 lines)
│   │   │   │   └── ldpDeleteWriter/
│   │   │   │       ├── ldpDelete.vtl (55 lines)
│   │   │   │       ├── ldpDeleteWriter.par (71 lines)
│   │   │   │       └── ldpDelete_XR.vtl (5 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── ldpCreateProcedure.xde (19 lines)
│   │   │   ├── ldpDeleteProcedure.xde (18 lines)
│   │   │   ├── ldpUpdateProcedure.xde (72 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.config.xde.ldpResources-Inventory/
│   │   │   ├── ldpResources-Inventory.xpa/
│   │   │   │   ├── entropy/
│   │   │   │   │   ├── entropy.par (103 lines)
│   │   │   │   │   ├── entropyParserOutput.xsd (6 lines)
│   │   │   │   │   ├── entropyParser_xdeIOS.rpl (49 lines)
│   │   │   │   │   └── entropyXRParser_xdeIOS_XR.rpl (49 lines)
│   │   │   │   ├── explicit_null/
│   │   │   │   │   ├── explicit_null.par (55 lines)
│   │   │   │   │   ├── explicit_nullParserOutput.xsd (6 lines)
│   │   │   │   │   └── explicit_nullParser_xdeIOS.rpl (61 lines)
│   │   │   │   ├── getIntefaceName/
│   │   │   │   │   ├── getIntefaceName.par (99 lines)
│   │   │   │   │   ├── getIntefaceNameParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getIntefaceNameParser_xdeIOS.rpl (68 lines)
│   │   │   │   │   └── getIntefaceNameParser_xdeIOS_XR.rpl (69 lines)
│   │   │   │   ├── getInterfaceNameXR/
│   │   │   │   │   ├── getInterfaceNameXR.par (56 lines)
│   │   │   │   │   ├── getInterfaceNameXRParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getInterfaceNameXRParser_xdeIOS_XR.rpl (61 lines)
│   │   │   │   │   └── getInterfaceNameXRParser_xdeIOS_XROutput.xsd (11 lines)
│   │   │   │   ├── getIpMask/
│   │   │   │   │   ├── Output.txt (9 lines)
│   │   │   │   │   ├── getIpMask.par (105 lines)
│   │   │   │   │   ├── getIpMaskParser_xdeIOS.rpl (49 lines)
│   │   │   │   │   └── getIpMaskXRParser_xdeIOS_XR.rpl (98 lines)
│   │   │   │   ├── getMPLSIntefaceName/
│   │   │   │   │   ├── InterfaceXEOutput (133 lines)
│   │   │   │   │   ├── getMPLSIntefaceName.par (104 lines)
│   │   │   │   │   ├── getMPLSIntefaceNameParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getMPLSIntefaceNameParser_xdeIOS.rpl (93 lines)
│   │   │   │   │   └── getMPLSIntefaceNameParser_xdeIOS_XR.rpl (93 lines)
│   │   │   │   ├── getMplsLabelRange/
│   │   │   │   │   ├── getMplsLabelRange.par (103 lines)
│   │   │   │   │   ├── getMplsLabelRangeParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getMplsLabelRangeParser_xdeIOS.rpl (68 lines)
│   │   │   │   │   └── getMplsLabelRangeXRParser_xdeIOS_XR.rpl (68 lines)
│   │   │   │   ├── igpSync/
│   │   │   │   │   ├── igpSync.par (55 lines)
│   │   │   │   │   ├── igpSyncParserOutput.xsd (6 lines)
│   │   │   │   │   └── igpSyncParser_xdeIOS.rpl (61 lines)
│   │   │   │   ├── ldpDetails/
│   │   │   │   │   ├── ldpDetails.par (104 lines)
│   │   │   │   │   ├── ldpDetailsParser_xdeIOS.rpl (190 lines)
│   │   │   │   │   ├── ldpDetailsParser_xdeIOS_XR.rpl (141 lines)
│   │   │   │   │   ├── ldpDiscoverySummary.txt (9 lines)
│   │   │   │   │   └── mplsLdpDiscoveryIOS.txt (7 lines)
│   │   │   │   ├── ldpNeighborDetails/
│   │   │   │   │   ├── ldpNeighbor.txt (43 lines)
│   │   │   │   │   ├── ldpNeighborDetails.par (102 lines)
│   │   │   │   │   ├── ldpNeighborDetailsParserOutput.xsd (17 lines)
│   │   │   │   │   ├── ldpNeighborDetailsParser_xdeIOS.rpl (357 lines)
│   │   │   │   │   └── ldpNeighborDetailsParser_xdeIOS_XR.rpl (200 lines)
│   │   │   │   ├── ldpParameters/
│   │   │   │   │   ├── ldpParameters.par (103 lines)
│   │   │   │   │   ├── ldpParametersParserOutput.xsd (6 lines)
│   │   │   │   │   ├── ldpParametersParser_xdeIOS.rpl (368 lines)
│   │   │   │   │   ├── ldpParametersXRParser_xdeIOS_XR.rpl (318 lines)
│   │   │   │   │   └── output.txt (20 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (1156 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (351 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.mef-qos-ME1200-inventory/
│   │   │   ├── evcPolicerDetails.xpa/
│   │   │   │   └── getMapPolicerDetails/
│   │   │   │       ├── getMapPolicerDetails.par (51 lines)
│   │   │   │       ├── getMapPolicerDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getMapPolicerDetailsParser_xdeME1200_OS.rpl (473 lines)
│   │   │   │       └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getEVCDetails/
│   │   │   │   ├── getEVCDetails.par (51 lines)
│   │   │   │   ├── getEVCDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getEVCDetailsParser_xdeME1200_OS.rpl (211 lines)
│   │   │   │   ├── getEVCDetailsParser_xdeME1200_OSOutput.xsd (28 lines)
│   │   │   │   ├── output1 (230 lines)
│   │   │   │   └── xmp-im-qos-module.xsd (30 lines)
│   │   │   ├── getEvcQosPolicymapPEPBinding/
│   │   │   │   ├── getEvcQosPolicymapPEPBinding.par (51 lines)
│   │   │   │   ├── getEvcQosPolicymapPEPBindingParserOutput.xsd (6 lines)
│   │   │   │   ├── getEvcQosPolicymapPEPBindingParser_xdeME1200_OS.rpl (185 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosClassMapDetails/
│   │   │   │   ├── getQosClassMapDetails.par (51 lines)
│   │   │   │   ├── getQosClassMapDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosClassMapDetailsParser_xdeME1200_OS.rpl (540 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosInterfaceDetails.xpa/
│   │   │   │   └── getInterfaceDetails/
│   │   │   │       ├── getQosInterface.par (51 lines)
│   │   │   │       ├── getQosInterfaceDetailsParser_ME1200_IOS.rpl (2668 lines)
│   │   │   │       └── xmp-im-qos-module.xsd (1076 lines)
│   │   │   ├── getQosPolicyMapDetails/
│   │   │   │   ├── getQosPolicyMapDetails.par (51 lines)
│   │   │   │   ├── getQosPolicyMapDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosPolicyMapDetailsParser_xdeME1200_OS.rpl (1139 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosPolicymapPEPBinding/
│   │   │   │   ├── getQosPolicymapPEPBinding.par (57 lines)
│   │   │   │   ├── getQosPolicymapPEPBindingParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosPolicymapPEPBindingParser_xdeME1200_OS.rpl (833 lines)
│   │   │   │   ├── output_interface (389 lines)
│   │   │   │   ├── output_storm (5 lines)
│   │   │   │   ├── output_wred (10 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosRedPreceedanceDetails/
│   │   │   │   ├── getQosRedPreceedanceDetails.par (54 lines)
│   │   │   │   ├── getQosRedPreceedanceDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosRedPreceedanceDetailsParser_xdeME1200_OS.rpl (988 lines)
│   │   │   │   └── xmp-im-qos-module.xsd (1073 lines)
│   │   │   ├── getQosStormPolicerDetails/
│   │   │   │   ├── getQosStormPolicerDetails.par (51 lines)
│   │   │   │   ├── getQosStormPolicerDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosStormPolicerDetailsParser_xdeME1200_OS.rpl (139 lines)
│   │   │   │   └── xmp-im-qos-module.xsd (1076 lines)
│   │   │   ├── getQosStormPolicingMapDetails/
│   │   │   │   ├── getQosStormPolicingMapDetails.par (51 lines)
│   │   │   │   ├── getQosStormPolicingMapDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosStormPolicingMapDetailsParser_xdeME1200_OS.rpl (171 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosWredMapDetails/
│   │   │   │   ├── getQosWredMapDetails.par (51 lines)
│   │   │   │   ├── getQosWredMapDetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getQosWredMapDetailsParser_xdeME1200_OS.rpl (173 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getQosConfigProcedure.xde (1230 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.config.xde.ospf-te-config/
│   │   │   ├── ospf_te_config.xpa/
│   │   │   │   ├── createOspfTrafficEng/
│   │   │   │   │   ├── createOspfTrafficEng.par (71 lines)
│   │   │   │   │   ├── ios.vtl (22 lines)
│   │   │   │   │   └── iosxr.vtl (26 lines)
│   │   │   │   ├── deleteOspfTrafficEng/
│   │   │   │   │   ├── deleteOspfTrafficEng.par (71 lines)
│   │   │   │   │   ├── ios.vtl (18 lines)
│   │   │   │   │   └── iosxr.vtl (25 lines)
│   │   │   │   └── testTrafficEngineering/
│   │   │   │       ├── testcreateOspfTrafficEng.xft (30 lines)
│   │   │   │       ├── testcreateOspfTrafficEngXR.xft (38 lines)
│   │   │   │       ├── testcreateOspfTrafficEngXR_WithoutLoopback.xft (33 lines)
│   │   │   │       ├── testdeleteOspfTrafficEng.xft (31 lines)
│   │   │   │       └── testdeleteOspfTrafficEngXR.xft (49 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ospfTeCreateProcedure.xde (14 lines)
│   │   │   ├── ospfTeDeleteProcedure.xde (14 lines)
│   │   │   ├── packageDescriptor.xml (13 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.port-mirroring-config/
│   │   │   ├── PortMirroring.xpa/
│   │   │   │   ├── portMirroringCreateAndUpdateWriter/
│   │   │   │   │   ├── portMirroringCreateAndUpdateWriter.par (40 lines)
│   │   │   │   │   └── portMirroringCreateIOS.vtl (160 lines)
│   │   │   │   └── portMirroringDeleteWriter/
│   │   │   │       ├── portDelete.vtl (35 lines)
│   │   │   │       └── portMirroringDeleteWriter.par (40 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ForceDeployer.vtl (5 lines)
│   │   │   ├── conf.xml (9 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   ├── portMirroringCreateProcedure.xde (38 lines)
│   │   │   ├── portMirroringDeleteProcedure.xde (19 lines)
│   │   │   ├── portMirroringUpdateProcedure.xde (46 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.ptp-config/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.config.xde/
│   │   │   │   │       └── ptp-config/
│   │   │   │   │           ├── pom.properties (5 lines)
│   │   │   │   │           └── pom.xml (39 lines)
│   │   │   │   └── MANIFEST.MF (6 lines)
│   │   │   ├── ptp.xpa/
│   │   │   │   ├── ptpCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (164 lines)
│   │   │   │   │   └── ptpCreateAndUpdateWriter.par (42 lines)
│   │   │   │   └── ptpDeleteWriter/
│   │   │   │       ├── ios.vtl (149 lines)
│   │   │   │       └── ptpDeleteWriter.par (42 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   ├── ptpCreateProcedure.xde (83 lines)
│   │   │   ├── ptpDeleteProcedure.xde (64 lines)
│   │   │   ├── ptpUpdateProcedure.xde (87 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── com.cisco.prime.config.xde.routing-isis-config/
│   │   │   ├── routing-isis-config.xpa/
│   │   │   │   ├── isisCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (172 lines)
│   │   │   │   │   ├── iosXR.vtl (169 lines)
│   │   │   │   │   ├── isisCreateAndUpdateWriter.par (28 lines)
│   │   │   │   │   └── temp.vtl (26 lines)
│   │   │   │   ├── isisDeleteWriter/
│   │   │   │   │   ├── ios.vtl (78 lines)
│   │   │   │   │   ├── iosXR.vtl (36 lines)
│   │   │   │   │   ├── iosXR_2.vtl (33 lines)
│   │   │   │   │   └── isisDeleteWriter.par (28 lines)
│   │   │   │   ├── tests/
│   │   │   │   │   ├── iosXE/
│   │   │   │   │   │   ├── createFirstIsisInterface_cktL1_L2_PTP_pri1_pri2.xft (107 lines)
│   │   │   │   │   │   ├── createIsisProcess.xft (57 lines)
│   │   │   │   │   │   └── updateIsisProcessSettings_net_and_istype.xft (72 lines)
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── addNewInterfaceWithOlds.xft (199 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_L2_PTP_noPri.xft (98 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_L2_PTP_pri1.xft (101 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_L2_PTP_pri1_pri2.xft (99 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_L2_PTP_pri2.xft (100 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_L2_noPTP_pri1_pri2.xft (98 lines)
│   │   │   │   │       ├── createFirstIsisInterface_cktL1_PTP_pri1_pri2.xft (99 lines)
│   │   │   │   │       ├── createIsisProcess.xft (57 lines)
│   │   │   │   │       ├── createIsisProcessWithoutNet.xft (56 lines)
│   │   │   │   │       ├── deleteIsisInterface_one_of_many_interfaces.xft (249 lines)
│   │   │   │   │       ├── deleteIsisInterface_only_one_that_existed.xft (94 lines)
│   │   │   │   │       ├── deleteIsisProcess.xft (45 lines)
│   │   │   │   │       ├── temp_deleteIsisInterface_only_one_that_existed.xft (96 lines)
│   │   │   │   │       ├── updateIsisInterface.xft (184 lines)
│   │   │   │   │       ├── updateIsisProcessSettings_from_noNet_to_net.xft (79 lines)
│   │   │   │   │       ├── updateIsisProcessSettings_net_and_istype.xft (81 lines)
│   │   │   │   │       └── updateIsisProcessSettings_noIstype_to_Istype.xft (79 lines)
│   │   │   │   ├── xmp-im-routing-module.xsd (4349 lines)
│   │   │   │   └── xmp-im-routing-module.xsd.bckp (3417 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── isisCreateProcedure.xde (53 lines)
│   │   │   ├── isisDeleteProcedure.xde (20 lines)
│   │   │   ├── isisUpdateProcedure.xde (70 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (30 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.segment-routing-config/
│   │   │   ├── affinity.xpa/
│   │   │   │   ├── affinityCreateAndUpdateWriter/
│   │   │   │   │   ├── affinityConfigCreateAndUpdateWriter.par (41 lines)
│   │   │   │   │   └── affinityConfigCreateAndUpdateWriter.vtl (50 lines)
│   │   │   │   └── affinityDeleteWriter/
│   │   │   │       ├── affinityDelete.vtl (42 lines)
│   │   │   │       └── affinityDeleteWriter.par (42 lines)
│   │   │   ├── onDemandPolicy.xpa/
│   │   │   │   ├── onDemandPolicyCreateAndUpdateWriter/
│   │   │   │   │   ├── onDemandPolicyConfigCreateAndUpdateWriter.par (43 lines)
│   │   │   │   │   └── onDemandPolicyConfigCreateAndUpdateWriter.vtl (95 lines)
│   │   │   │   └── onDemandPolicyDeleteWriter/
│   │   │   │       ├── onDemandPolicyDelete.vtl (51 lines)
│   │   │   │       └── onDemandPolicyDeleteWriter.par (40 lines)
│   │   │   ├── pcc.xpa/
│   │   │   │   ├── pccCreateAndUpdateWriter/
│   │   │   │   │   ├── pccConfigCreateAndUpdateWriter.par (41 lines)
│   │   │   │   │   └── pccConfigCreateAndUpdateWriter.vtl (72 lines)
│   │   │   │   └── pccDeleteWriter/
│   │   │   │       ├── pccDelete.vtl (11 lines)
│   │   │   │       └── pccDeleteWriter.par (42 lines)
│   │   │   ├── pceServer.xpa/
│   │   │   │   ├── pceServerCreateAndUpdateWriter/
│   │   │   │   │   ├── pceServerConfigCreateAndUpdateWriter.par (41 lines)
│   │   │   │   │   └── pceServerConfigCreateAndUpdateWriter.vtl (46 lines)
│   │   │   │   └── pceServerDeleteWriter/
│   │   │   │       ├── routingProcessDelete.vtl (41 lines)
│   │   │   │       └── routingProcessDeleteWriter.par (42 lines)
│   │   │   ├── routingProcess.xpa/
│   │   │   │   ├── routingProcessCreateAndUpdateWriter/
│   │   │   │   │   ├── routingProcessConfigCreateAndUpdateWriter.par (43 lines)
│   │   │   │   │   └── routingProcessConfigCreateAndUpdateWriter.vtl (135 lines)
│   │   │   │   └── routingProcessDeleteWriter/
│   │   │   │       ├── routingProcessDelete.vtl (41 lines)
│   │   │   │       └── routingProcessDeleteWriter.par (42 lines)
│   │   │   ├── segmentSettings.xpa/
│   │   │   │   ├── segmentSettingsCreateAndUpdateWriter/
│   │   │   │   │   ├── segmentSettingsConfigCreateAndUpdateWriter.par (43 lines)
│   │   │   │   │   └── segmentSettingsConfigCreateAndUpdateWriter.vtl (81 lines)
│   │   │   │   └── segmentSettingsDeleteWriter/
│   │   │   │       ├── segmentRoutingDelete.vtl (100 lines)
│   │   │   │       └── segmentRoutingDeleteWriter.par (42 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (3 lines)
│   │   │   ├── error.xml (4 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── segmentRoutingCreateProcedure.xde (115 lines)
│   │   │   ├── segmentRoutingDeleteProcedure.xde (65 lines)
│   │   │   ├── segmentRoutingUpdateProcedure.xde (300 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.serial-config/
│   │   │   ├── serial-config.xpa/
│   │   │   │   ├── rawSocketCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXE.vtl (260 lines)
│   │   │   │   │   └── rawsocketCreateAndUpdateWriter.par (46 lines)
│   │   │   │   ├── rawsocketDeleteWriter/
│   │   │   │   │   ├── iosXE.vtl (324 lines)
│   │   │   │   │   └── rawsocketDeleteWriter.par (46 lines)
│   │   │   │   ├── serialCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXR.vtl (156 lines)
│   │   │   │   │   └── serialCreateAndUpdateWriter.par (40 lines)
│   │   │   │   ├── serialDeleteWriter/
│   │   │   │   │   ├── iosXR.vtl (59 lines)
│   │   │   │   │   └── serialDeleteWriter.par (40 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (6 lines)
│   │   │   ├── error.xml (8 lines)
│   │   │   ├── isVersionNotSupported.xjs (29 lines)
│   │   │   ├── packageDescriptor.xml (17 lines)
│   │   │   ├── serialCreateProcedure.xde (77 lines)
│   │   │   ├── serialDeleteProcedure.xde (67 lines)
│   │   │   ├── serialUpdateProcedure.xde (43 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.snmpset-interface-adminstatus-writer/
│   │   │   ├── setIFAdminStatus/
│   │   │   │   ├── EthernetProtocolEndpointExtended.xml (1962 lines)
│   │   │   │   ├── EthernetSubInterface.xml (667 lines)
│   │   │   │   ├── setIFAdminStatus.par (44 lines)
│   │   │   │   └── setIFAdminStatus.snp (205 lines)
│   │   │   ├── .project (17 lines)
│   │   │   ├── ifAdminStatusCreateProcedure.xde (26 lines)
│   │   │   ├── ifAdminStatusUpdateProcedure.xde (82 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (29 lines)
│   │   ├── com.cisco.prime.config.xde.sonet-tdm-config/
│   │   │   ├── javaScriptFunctions/
│   │   │   │   └── getFormattedCli.xjs (14 lines)
│   │   │   ├── sonet-tdm-config.xpa/
│   │   │   │   ├── cemCreateAndUpdateWriter/
│   │   │   │   │   ├── cemCreateAndUpdateWriter.par (44 lines)
│   │   │   │   │   └── cemIOS.vtl (1933 lines)
│   │   │   │   └── cemDeleteWriter/
│   │   │   │       ├── cemDeleteWriter.par (64 lines)
│   │   │   │       └── cemIOS.vtl (104 lines)
│   │   │   ├── test/
│   │   │   │   ├── DS1/
│   │   │   │   │   ├── E1_AddDescription.xft (25 lines)
│   │   │   │   │   ├── E1_RemoveDescription.xft (25 lines)
│   │   │   │   │   ├── T1_AddDescription.xft (25 lines)
│   │   │   │   │   └── T1_RemoveDescription.xft (25 lines)
│   │   │   │   ├── DS3/
│   │   │   │   │   ├── E3_AddDescription.xft (25 lines)
│   │   │   │   │   ├── E3_RemoveDescription.xft (25 lines)
│   │   │   │   │   ├── T3_AddDescription.xft (25 lines)
│   │   │   │   │   └── T3_RemoveDescription.xft (25 lines)
│   │   │   │   └── OCx/
│   │   │   │       ├── SONET-ACR_AddDescription.xft (25 lines)
│   │   │   │       ├── SONET-ACR_RemoveDescription.xft (25 lines)
│   │   │   │       ├── SONET_AddDescription.xft (25 lines)
│   │   │   │       └── SONET_RemoveDescription.xft (25 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── cemCreateProcedure.xde (22 lines)
│   │   │   ├── cemDeleteProcedure.xde (20 lines)
│   │   │   ├── cemUpdateProcedure.xde (178 lines)
│   │   │   ├── error.xml (16 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.synce-config/
│   │   │   ├── synce.xpa/
│   │   │   │   ├── synceCreateAndUpdateWriter/
│   │   │   │   │   ├── ios-xr.vtl (945 lines)
│   │   │   │   │   ├── ios.vtl (283 lines)
│   │   │   │   │   └── synceCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── synceDeleteWriter/
│   │   │   │   │   ├── ios-xr.vtl (124 lines)
│   │   │   │   │   ├── ios.vtl (215 lines)
│   │   │   │   │   └── synceDeleteWriter.par (28 lines)
│   │   │   │   └── testFromEMS/
│   │   │   │       ├── iosXE/
│   │   │   │       │   ├── Output_IOS_XE.xml (85 lines)
│   │   │   │       │   ├── Output_IOS_XE_BitsFreq2M.xml (44 lines)
│   │   │   │       │   ├── Output_IOS_XE_BitsInf_E1_T1.xml (25 lines)
│   │   │   │       │   ├── Output_IOS_XE_BitsInf_E1_T1_Child.xml (44 lines)
│   │   │   │       │   ├── Output_IOS_XE_Diff.xml (85 lines)
│   │   │   │       │   ├── Output_IOS_XE_SSM.xml (929 lines)
│   │   │   │       │   ├── SyncEDelete.xft (445 lines)
│   │   │   │       │   ├── SyncE_BITS_FrequencyCreate.xft (79 lines)
│   │   │   │       │   ├── SyncE_BITS_FrequencyDelete.xft (76 lines)
│   │   │   │       │   ├── SyncE_BITS_FrequencyUpdate.xft (117 lines)
│   │   │   │       │   ├── SyncE_BITS_InterfaceCreate.xft (60 lines)
│   │   │   │       │   ├── SyncE_BITS_InterfaceDelete.xft (57 lines)
│   │   │   │       │   └── SyncE_BITS_InterfaceUpdate.xft (79 lines)
│   │   │   │       └── iosXR/
│   │   │   │           ├── OutputIOSXR.xml (84 lines)
│   │   │   │           ├── Output_IOS_XR_Bits_Freq.xml (45 lines)
│   │   │   │           ├── Output_IOS_XR_Bits_Inf_Child.xml (45 lines)
│   │   │   │           ├── Output_IOS_XR_Bits_Inf_Child_Update.xml (45 lines)
│   │   │   │           ├── Output_IOS_XR_Bits_Inf_Global.xml (26 lines)
│   │   │   │           ├── Sample.xml (46 lines)
│   │   │   │           ├── SyncECreate.xft (165 lines)
│   │   │   │           ├── SyncEUpdate.xft (220 lines)
│   │   │   │           ├── SyncE_BITSInterfaceCreate.xft (63 lines)
│   │   │   │           └── SyncE_BITSInterfaceUpdate.xft (101 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── getDeviceType.xde (32 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── synceCreateProcedure.xde (49 lines)
│   │   │   ├── synceDeleteProcedure.xde (61 lines)
│   │   │   ├── synceUpdateProcedure.xde (407 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.vcop-config/
│   │   │   ├── vcop.xpa/
│   │   │   │   ├── vcopCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (10 lines)
│   │   │   │   │   └── vcopCreateAndUpdateWriter.par (40 lines)
│   │   │   │   └── vcopDeleteWriter/
│   │   │   │       ├── ios.vtl (9 lines)
│   │   │   │       └── vcopDeleteWriter.par (40 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   ├── vcopCreateProcedure.xde (18 lines)
│   │   │   ├── vcopDeleteProcedure.xde (18 lines)
│   │   │   ├── vcopUpdateProcedure.xde (28 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.xde-cem-config-pg/
│   │   │   ├── META-INF/
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── protectiongroup.xpa/
│   │   │   │   ├── protectionGroupCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (114 lines)
│   │   │   │   │   └── protectionGroupCreateAndUpdateWriter.par (18 lines)
│   │   │   │   ├── protectionGroupDeleteWriter/
│   │   │   │   │   ├── ios.vtl (64 lines)
│   │   │   │   │   └── protectionGroupDeleteWriter.par (18 lines)
│   │   │   │   └── testFromEMS/
│   │   │   │       └── iosXE/
│   │   │   │           └── Output_IOS_XE.xml (1440 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   ├── protectionGroupCreateProcedure.xde (36 lines)
│   │   │   ├── protectionGroupDeleteProcedure.xde (31 lines)
│   │   │   ├── protectionGroupUpdateProcedure.xde (186 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.config.xde.xde-lag-config/
│   │   │   ├── xde-lag-config.xpa/
│   │   │   │   ├── lagCreateAndUpdateWriter/
│   │   │   │   │   ├── lagCreateAndUpdateWriter.par (30 lines)
│   │   │   │   │   ├── lag_IOSXR_velocityFile.vtl (71 lines)
│   │   │   │   │   └── lag_IOS_velocityFile.vtl (71 lines)
│   │   │   │   ├── lagCreateAndUpdateWritterXE/
│   │   │   │   │   ├── lagCreateAndUpdateWritterXE.par (18 lines)
│   │   │   │   │   └── velocityFile.vtl (71 lines)
│   │   │   │   ├── lagDeleteWriter/
│   │   │   │   │   ├── lagDeleteWriter.par (28 lines)
│   │   │   │   │   ├── lag_IOSXR_velocityFile.vtl (30 lines)
│   │   │   │   │   └── lag_IOS_velocityFile.vtl (30 lines)
│   │   │   │   └── xmp-im-link-aggregation-module.xsd (1101 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── lagCreateProcedure.xde (108 lines)
│   │   │   ├── lagDeleteProcedure.xde (40 lines)
│   │   │   ├── lagUpdateProcedure.xde (77 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.xde_MPLS_TE_FRR_config/
│   │   │   ├── mplste.xpa/
│   │   │   │   ├── mplsteCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (52 lines)
│   │   │   │   │   ├── iosXr.vtl (50 lines)
│   │   │   │   │   └── mplsteCreateAndUpdateWriter.par (71 lines)
│   │   │   │   └── mplsteDeleteWriter/
│   │   │   │       ├── ios.vtl (1 lines)
│   │   │   │       ├── iosXr.vtl (0 lines)
│   │   │   │       └── mplsteDeleteWriter.par (71 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── mplsteCreateProcedure.xde (30 lines)
│   │   │   ├── mplsteDeleteProcedure.xde (16 lines)
│   │   │   ├── mplsteUpdateProcedure.xde (111 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.config.xde.xmp-im-ethernet-oam-module-inventory/
│   │   │   ├── EoamDelayMeastSettings.xpa/
│   │   │   │   └── EoamDelayMeastSettings/
│   │   │   │       ├── EoamDelayMeastSettings.par (145 lines)
│   │   │   │       ├── EoamDelayMeastSettingsParser_xdeIOS.rpl (1188 lines)
│   │   │   │       ├── EoamDelayMeastSettingsParser_xdeIOS_XR.rpl (1644 lines)
│   │   │   │       ├── EoamDelayMeastSettingsParser_xdeIOS_XROutput.xsd (88 lines)
│   │   │   │       ├── EoamDelayMeastSettings_IOS.xslt (157 lines)
│   │   │   │       ├── EoamDelayMeastSettings_IOS_XR.xslt (206 lines)
│   │   │   │       ├── IOS_DelayMeast_TwoCommandsOutput.txt (70 lines)
│   │   │   │       ├── IOS_XR_output.txt (21 lines)
│   │   │   │       ├── IOS_XR_output2.txt (599 lines)
│   │   │   │       ├── IOS_output.txt (70 lines)
│   │   │   │       ├── IOS_output_2.txt (1353 lines)
│   │   │   │       ├── XR_DelayMeast_TwoCommandsOutput.txt (26 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (4247 lines)
│   │   │   ├── EoamLinkMonitorSettings.xpa/
│   │   │   │   ├── EoamEVCMapping/
│   │   │   │   │   ├── EoamEVCMapping.par (122 lines)
│   │   │   │   │   ├── EoamEVCMappingParser_xdeIOS.rpl (110 lines)
│   │   │   │   │   ├── EoamEVCMappingParser_xdeIOS_XR.rpl (97 lines)
│   │   │   │   │   └── ios_eoamEVCMapping_output.txt (506 lines)
│   │   │   │   ├── EoamLinkMonitorSettings/
│   │   │   │   │   ├── EoamLinkMonitorSettings.map (21 lines)
│   │   │   │   │   ├── EoamLinkMonitorSettings.par (109 lines)
│   │   │   │   │   ├── EoamLinkMonitorSettings_ios.map (22 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   │   ├── EoamLinkMonitorSettingsRow/
│   │   │   │   │   ├── EoamLinkMonitorSettingsRow.map (21 lines)
│   │   │   │   │   ├── EoamLinkMonitorSettingsRow.par (113 lines)
│   │   │   │   │   ├── EoamLinkMonitorSettingsRow_ios.map (22 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   │   ├── getIfIndex/
│   │   │   │   │   ├── getIfIndex.par (111 lines)
│   │   │   │   │   ├── getIfIndexOutput.xsd (18 lines)
│   │   │   │   │   ├── getIfIndexParser_xdeIOS.rpl (70 lines)
│   │   │   │   │   ├── getIfIndexParser_xdeIOS_XR.rpl (70 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (2 lines)
│   │   │   │   │   └── sampleDeviceOutputIOS_XR.txt (1 lines)
│   │   │   │   ├── snmpOutput.txt (11 lines)
│   │   │   │   ├── snmpOutput3.txt (10 lines)
│   │   │   │   ├── snmpOutput_ios.txt (110 lines)
│   │   │   │   └── snmpoutput2.txt (14 lines)
│   │   │   ├── EoamLossMeastSettings.xpa/
│   │   │   │   └── EoamLossMeastSettings/
│   │   │   │       ├── EoamLossMeastSettings.par (143 lines)
│   │   │   │       ├── EoamLossMeastSettingsParser_xdeIOS.rpl (752 lines)
│   │   │   │       ├── EoamLossMeastSettingsParser_xdeIOS_Output.xsd (70 lines)
│   │   │   │       ├── EoamLossMeastSettingsParser_xdeIOS_XR.rpl (1060 lines)
│   │   │   │       ├── EoamLossMeastSettingsParser_xdeIOS_XROutput.xsd (88 lines)
│   │   │   │       ├── EoamLossMeastSettings_IOS.xslt (101 lines)
│   │   │   │       ├── EoamLossMeastSettings_IOS_XR.xslt (217 lines)
│   │   │   │       ├── IOS_LossMeast_TwoCommandsOutput.txt (70 lines)
│   │   │   │       ├── IOS_XR_output.txt (23 lines)
│   │   │   │       ├── IOS_output.txt (135 lines)
│   │   │   │       ├── XR_LossMeast_TwoCommandsOutput.txt (28 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (4247 lines)
│   │   │   ├── EoamPmMeastInstanceSettings.xpa/
│   │   │   │   └── EoamPmMeastInstanceSettings/
│   │   │   │       ├── EoamPmMeastInst.par (160 lines)
│   │   │   │       ├── EoamPmMeastInstParser_xdeIOS.rpl (604 lines)
│   │   │   │       ├── EoamPmMeastInstParser_xdeIOS_Output.xsd (42 lines)
│   │   │   │       ├── EoamPmMeastInstParser_xdeIOS_XR.rpl (390 lines)
│   │   │   │       ├── EoamPmMeastInstParser_xdeIOS_XROutput.xsd (38 lines)
│   │   │   │       ├── EoamPmMeastInst_IOS.xslt (141 lines)
│   │   │   │       ├── EoamPmMeastInst_IOS_XR.xslt (207 lines)
│   │   │   │       ├── IOS_XR_output.txt (538 lines)
│   │   │   │       ├── IOS_output.txt (4579 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (4247 lines)
│   │   │   ├── EthMaintenanceDomainSettings.xpa/
│   │   │   │   ├── EthMaintDomainSettingsName/
│   │   │   │   │   ├── EthMaintDomainSettingsName.par (124 lines)
│   │   │   │   │   ├── EthMaintDomainSettingsNameParser_IOS.rpl (211 lines)
│   │   │   │   │   ├── EthMaintDomainSettingsNameParser_IOS_XR.rpl (211 lines)
│   │   │   │   │   ├── SampleOuputIOS.txt (30 lines)
│   │   │   │   │   ├── SampleOuputXR.txt (35 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (20 lines)
│   │   │   │   ├── EthMaintenanceDomainSettings/
│   │   │   │   │   ├── EthMaintenanceDomainSettings.map (135 lines)
│   │   │   │   │   ├── EthMaintenanceDomainSettings.par (56 lines)
│   │   │   │   │   ├── snmpOutput_XR.txt (38 lines)
│   │   │   │   │   ├── snmpOutput_ios.txt (104 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3181 lines)
│   │   │   │   ├── EthMaintenanceDomainSettingsRow/
│   │   │   │   │   ├── EthMaintenanceDomainSettingsRow.map (135 lines)
│   │   │   │   │   ├── EthMaintenanceDomainSettingsRow.par (60 lines)
│   │   │   │   │   ├── snmpOutput.txt (158 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3181 lines)
│   │   │   │   ├── GetHoldTime/
│   │   │   │   │   ├── GetHoldTime.par (38 lines)
│   │   │   │   │   ├── SampleDeviceOutput_IOS.txt (10 lines)
│   │   │   │   │   └── getholdParser_xdeIOS.rpl (45 lines)
│   │   │   │   ├── snmpOutput.txt (22 lines)
│   │   │   │   ├── snmpOutput1.txt (22 lines)
│   │   │   │   ├── snmpOutput2.txt (7 lines)
│   │   │   │   └── snmpOutput_ios.txt (7 lines)
│   │   │   ├── EthMaintenanceEntityGroupSettings.xpa/
│   │   │   │   ├── EthMaintenanceEntityGroupSettings/
│   │   │   │   │   ├── EthMaintenanceEntityGroupSettings.map (274 lines)
│   │   │   │   │   ├── EthMaintenanceEntityGroupSettings.par (27 lines)
│   │   │   │   │   ├── snmpOutput.txt (10 lines)
│   │   │   │   │   ├── snmpOutput1.txt (10 lines)
│   │   │   │   │   ├── snmpOutput2.txt (26 lines)
│   │   │   │   │   ├── snmpOutputLarge.txt (1791 lines)
│   │   │   │   │   ├── snmpOutputWithAllNameFormats.txt (121 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3183 lines)
│   │   │   │   ├── EthMaintenanceEntityGroupSettingsRow/
│   │   │   │   │   ├── EthMaintenanceEntityGroupSettingsRow.map (274 lines)
│   │   │   │   │   ├── EthMaintenanceEntityGroupSettingsRow.par (62 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3183 lines)
│   │   │   │   ├── GetBridgeDetails/
│   │   │   │   │   ├── EthMaintenanceEntityGroupSettings_ios.xslt (50 lines)
│   │   │   │   │   ├── GetBridgeDetails.par (136 lines)
│   │   │   │   │   ├── GetBridgeDetailsParser_xdeIOS.rpl (411 lines)
│   │   │   │   │   ├── GetBridgeDetailsParser_xdeIOS_XR.rpl (534 lines)
│   │   │   │   │   ├── SampleDeviceOutput_IOS.txt (67 lines)
│   │   │   │   │   ├── SampleDeviceOutput_IOSXR.txt (185 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (28 lines)
│   │   │   │   └── getTransformedNames/
│   │   │   │       └── getTransformedNames.xde (86 lines)
│   │   │   ├── EthMegEndPoint.xpa/
│   │   │   │   ├── EthMaintenancePoint/
│   │   │   │   │   ├── EthMaintenancePoint.par (145 lines)
│   │   │   │   │   ├── EthMaintenancePointParser.xsd (23 lines)
│   │   │   │   │   ├── EthMaintenancePointParser_xdeIOS.rpl (165 lines)
│   │   │   │   │   ├── EthMaintenancePointParser_xdeIOS_XR.rpl (163 lines)
│   │   │   │   │   ├── EthMaintenancePoint_IOS.xslt (34 lines)
│   │   │   │   │   ├── EthMaintenancePoint_IOSXR.xslt (60 lines)
│   │   │   │   │   ├── ios_ethmaintpoint_output.txt (58 lines)
│   │   │   │   │   └── iosxr_ethmaintpoint_output.txt (54 lines)
│   │   │   │   ├── EthMaintenancePointRemote/
│   │   │   │   │   ├── EthMaintenancePointRemote.par (120 lines)
│   │   │   │   │   ├── EthMaintenancePointRemoteParser.xsd (28 lines)
│   │   │   │   │   ├── EthMaintenancePointRemoteParser_xdeIOS_XR.rpl (134 lines)
│   │   │   │   │   ├── EthMaintenancePointRemote_IOSXR.xslt (60 lines)
│   │   │   │   │   ├── iosxr-ncs540-multiple-remotempid.txt (74 lines)
│   │   │   │   │   └── iosxr_ethmaintpoint_output.txt (82 lines)
│   │   │   │   ├── EthMegEndPoint/
│   │   │   │   │   ├── EthMegEndPoint.map (22 lines)
│   │   │   │   │   ├── EthMegEndPoint.par (29 lines)
│   │   │   │   │   ├── snmpOutput.txt (11 lines)
│   │   │   │   │   ├── snmpOutput1.txt (12 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   │   ├── EthMegEndPointRow/
│   │   │   │   │   ├── EthMegEndPointRow.map (22 lines)
│   │   │   │   │   └── EthMegEndPointRow.par (68 lines)
│   │   │   │   ├── getEthMaintenancePoint/
│   │   │   │   │   └── getEthMaintenancePoint.xde (177 lines)
│   │   │   │   ├── ifTableRow/
│   │   │   │   │   ├── ifTableRow.map (11 lines)
│   │   │   │   │   ├── ifTableRow.par (64 lines)
│   │   │   │   │   └── ifm-im-connectivity-ext-module.xsd (2957 lines)
│   │   │   │   └── snmpOutput.txt (51 lines)
│   │   │   ├── EthernetLmiPepSettings.xpa/
│   │   │   │   └── EthernetLmiPepSettings/
│   │   │   │       ├── EthernetLmiPepSettings.par (143 lines)
│   │   │   │       ├── EthernetLmiPepSettingsParser_xdeIOS.rpl (344 lines)
│   │   │   │       ├── EthernetLmiPepSettingsParser_xdeIOS_XR.rpl (316 lines)
│   │   │   │       ├── EthernetLmiPepSettings_ios.xslt (158 lines)
│   │   │   │       ├── EthernetLmiPepSettings_iosxr.xslt (154 lines)
│   │   │   │       ├── IOS-ELMI-Output (30 lines)
│   │   │   │       ├── XR-Elmi-Output (51 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3185 lines)
│   │   │   ├── tests/
│   │   │   │   ├── Ios-EoamDelayMeastSettings.xft (121 lines)
│   │   │   │   ├── Ios-EoamDelayMeastSettings2.xft (298 lines)
│   │   │   │   ├── Ios-EoamLinkMonitorSettings.xft (147 lines)
│   │   │   │   ├── Ios-EoamLossMeastSettings.xft (121 lines)
│   │   │   │   ├── Ios-EoamLossMeastSettings2.xft (123 lines)
│   │   │   │   ├── Ios-EoamPmMeastInstanceSettings.xft (342 lines)
│   │   │   │   ├── Ios-EthMaintenanceDomainSettings.xft (34 lines)
│   │   │   │   ├── Ios-EthMaintenanceEntityGroupSettings.xft (88 lines)
│   │   │   │   ├── Ios-EthernetLmiPepSettings.xft (286 lines)
│   │   │   │   ├── Ios-EthernetLmiPepSettings903.xft (334 lines)
│   │   │   │   ├── Ios-GetHoldTime.xft (80 lines)
│   │   │   │   ├── Ios-fullXdeProcedure.xft (4433 lines)
│   │   │   │   ├── IosFullProcedure.xft (2924 lines)
│   │   │   │   ├── NCS4K-EthMaintenanceEntityGroupSettings.xft (785 lines)
│   │   │   │   ├── NCS540-EoamPMMep_GI.xft (1591 lines)
│   │   │   │   ├── asr9k-DomainIdNullEoamPMMep_GI.xft (171 lines)
│   │   │   │   ├── asr9k-EoamDelayMeastSettings-new.xft (242 lines)
│   │   │   │   ├── asr9k-EoamDelayMeastSettings.xft (93 lines)
│   │   │   │   ├── asr9k-EoamLinkMonitorSettings.xft (43 lines)
│   │   │   │   ├── asr9k-EoamLossMeastSettings-new.xft (245 lines)
│   │   │   │   ├── asr9k-EoamLossMeastSettings.xft (94 lines)
│   │   │   │   ├── asr9k-EoamMeastDelaySettings_nopriority.xft (90 lines)
│   │   │   │   ├── asr9k-EoamPmMeastInstanceSettings.xft (171 lines)
│   │   │   │   ├── asr9k-EthMaintenanceDomainName.xft (127 lines)
│   │   │   │   ├── asr9k-EthMaintenanceDomainSettings.xft (44 lines)
│   │   │   │   ├── asr9k-EthMaintenanceEntityGroupSettings.xft (52 lines)
│   │   │   │   ├── asr9k-EthMegEndPoint.xft (44 lines)
│   │   │   │   ├── asr9k-EthernetLmiPepSettings.xft (285 lines)
│   │   │   │   ├── asr9k-EthernetLmiPepSettings2.xft (872 lines)
│   │   │   │   ├── asr9k-GetBridgeDetails.xft (156 lines)
│   │   │   │   ├── asr9k-GetHoldTimeEmpty.xft (24 lines)
│   │   │   │   ├── asr9k-WithoutAdminStatusXdeProcedure.xft (1245 lines)
│   │   │   │   ├── asr9k-fullXDE_DomainName.xft (619 lines)
│   │   │   │   ├── asr9k-fullXdeProcedure.xft (912 lines)
│   │   │   │   ├── asr9kMEGSettingsAllNameFormats.xft (327 lines)
│   │   │   │   ├── getEthMaintDomainSettingsRow.xft (33 lines)
│   │   │   │   ├── ios-EoamPmMepGI.xft (1491 lines)
│   │   │   │   ├── ios-fullXdeProcedure2.xft (8730 lines)
│   │   │   │   ├── ios-fullXdeProcedure3.xft (46258 lines)
│   │   │   │   ├── ios-fullXdeProcedure_GI.xft (1945 lines)
│   │   │   │   └── iosxr_FullProcedureGI.xft (2304 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── A_EthernetOAM.xde (1474 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.prime.inventory.LLDP_ME1200/
│   │   │   ├── neighborInfo.xpa/
│   │   │   │   ├── lldpNeighborInfo/
│   │   │   │   │   ├── lldpNeighborInfo.map (9 lines)
│   │   │   │   │   ├── lldpNeighborInfo.par (57 lines)
│   │   │   │   │   └── xmp-im-discovery-module.xsd (959 lines)
│   │   │   │   └── neighborAdrTypeCapability/
│   │   │   │       ├── neighborAdrTypeCapability.par (51 lines)
│   │   │   │       ├── neighborAdrTypeCapabilityParser_xdeME1200_OS.rpl (166 lines)
│   │   │   │       ├── output1.txt (35 lines)
│   │   │   │       ├── output2.txt (18 lines)
│   │   │   │       └── xmp-im-discovery-module.xsd (21 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (106 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.inventory.LLDP_topology_ME1200/
│   │   │   ├── linkLtp.xpa/
│   │   │   │   ├── getLocChassisId/
│   │   │   │   │   ├── getLocChassisId.par (53 lines)
│   │   │   │   │   ├── getLocChassisIdParser_xdeME1200_OS.rpl (50 lines)
│   │   │   │   │   └── xmp-im-discovery-module.xsd (17 lines)
│   │   │   │   └── linkOutput/
│   │   │   │       ├── linkOutput.par (51 lines)
│   │   │   │       ├── linkOutputParser_xdeME1200_OS.rpl (128 lines)
│   │   │   │       ├── output1.txt (35 lines)
│   │   │   │       ├── output2.txt (18 lines)
│   │   │   │       └── xmp-im-discovery-module.xsd (21 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── linkprocedure.xde (169 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.inventory.LLDP_topology_ME1200_persistance/
│   │   │   ├── linkLtp.xpa/
│   │   │   │   ├── getLinkDetails/
│   │   │   │   │   ├── getLinkDetails.par (51 lines)
│   │   │   │   │   ├── getLinkDetailsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getLinkDetailsParser_xdeME1200_OS.rpl (128 lines)
│   │   │   │   │   ├── output1.txt (35 lines)
│   │   │   │   │   └── prime-ethernet-resource-model.xsd (21 lines)
│   │   │   │   ├── getLtp/
│   │   │   │   │   ├── getLtp.map (12 lines)
│   │   │   │   │   ├── getLtp.par (57 lines)
│   │   │   │   │   ├── getLtpOutput.xsd (29 lines)
│   │   │   │   │   └── xmp-im-logical-resource-module.xsd (1180 lines)
│   │   │   │   └── getLtpDetails/
│   │   │   │       ├── getLtpDetails.map (9 lines)
│   │   │   │       ├── getLtpDetails.par (54 lines)
│   │   │   │       ├── getLtpDetailsOutput.xsd (45 lines)
│   │   │   │       └── xmp-im-logical-resource-module.xsd (1110 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── linkprocedure.xde (197 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.inventory.xde-eowyn5g-inventory/
│   │   │   ├── cisco_iosxe_getCardModuleDetails.xpa/
│   │   │   │   ├── No_Type_Output.txt (10 lines)
│   │   │   │   ├── celeborn_output.txt (23 lines)
│   │   │   │   ├── getCardModuleDetails.par (66 lines)
│   │   │   │   ├── getCardModuleDetailsParserOutput.xsd (690 lines)
│   │   │   │   ├── getCardModuleDetailsParser_xdeIOS.rpl (173 lines)
│   │   │   │   └── getCardModuleDetailsParser_xdeIOSOutput.xsd (27 lines)
│   │   │   ├── cisco_iosxe_getCelebornOpMode.xpa/
│   │   │   │   ├── getCelebornOpMode/
│   │   │   │   │   ├── CelebornBheem1OpMode.txt (7 lines)
│   │   │   │   │   ├── CelebornBheem2OpMode.txt (7 lines)
│   │   │   │   │   ├── device-capability-model.xsd (732 lines)
│   │   │   │   │   ├── getCelebornOpMode.par (53 lines)
│   │   │   │   │   └── getCelebornOpModeParser_xdeIOS.rpl (80 lines)
│   │   │   │   └── getSupportedSlotMode/
│   │   │   │       ├── SlotModeOutput_03.txt (15 lines)
│   │   │   │       ├── SlotModeOutput_04.txt (17 lines)
│   │   │   │       ├── SlotModeOutput_42_06.txt (17 lines)
│   │   │   │       ├── SlotModeOutput_42_10.txt (17 lines)
│   │   │   │       ├── SlotModeOutput_42_14.txt (17 lines)
│   │   │   │       ├── SlotModeOutput_42_15.txt (3 lines)
│   │   │   │       ├── device-capability-model.xsd (757 lines)
│   │   │   │       ├── getSupportedSlotMode.par (56 lines)
│   │   │   │       └── getSupportedSlotModeParser_xdeIOS.rpl (59 lines)
│   │   │   ├── cisco_iosxe_geteowyn5ginventory_cli.xpa/
│   │   │   │   ├── getEowyn5gCardMode/
│   │   │   │   │   ├── 10.104.120.41_Output.txt (6 lines)
│   │   │   │   │   ├── ShowPlatSoftChasfsr0brief_incOCX_Output.txt (3 lines)
│   │   │   │   │   ├── device-capability-model.xsd (648 lines)
│   │   │   │   │   ├── getEowyn5gCardMode.par (53 lines)
│   │   │   │   │   └── getEowyn5gCardModeParser_xdeIOS.rpl (71 lines)
│   │   │   │   └── getEowyn5gCardType/
│   │   │   │       ├── 10.104.120.167_output.txt (19 lines)
│   │   │   │       ├── 10.104.120.41_Output.txt (25 lines)
│   │   │   │       ├── 10.104.120.42_Oputput.txt (24 lines)
│   │   │   │       ├── Granular_41_Output.txt (4 lines)
│   │   │   │       ├── ShowPlatform_Output.txt (24 lines)
│   │   │   │       ├── device-capability-model.xsd (648 lines)
│   │   │   │       ├── getEowyn5gCardType.par (65 lines)
│   │   │   │       └── getEowyn5gCardTypeParser_xdeIOS.rpl (116 lines)
│   │   │   ├── getDenethorCardMode/
│   │   │   │   ├── 10.104.120.168_output.txt (2 lines)
│   │   │   │   ├── Denethor.txt (3 lines)
│   │   │   │   ├── getDenethorCardMode.par (63 lines)
│   │   │   │   ├── getDenethorCardModeParserOutput.xsd (6 lines)
│   │   │   │   ├── getDenethorCardModeParser_xdeIOS.rpl (114 lines)
│   │   │   │   └── getDenethorCardModeParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── tests/
│   │   │   │   └── IOS-XE/
│   │   │   │       ├── Eowyn5G_IOS_NCS42XX_Test_41.xft (93 lines)
│   │   │   │       └── Eowyn5G_IOS_NCS42XX_Test_42.xft (94 lines)
│   │   │   ├── xjsFunction/
│   │   │   │   ├── getDenethorMode.xjs (55 lines)
│   │   │   │   └── getSlotModeEnum.xjs (28 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (377 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.inventory.xde-lag-ME1200/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── xde-lag-ME1200/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (18 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── ether_interface.xpa/
│   │   │   │   └── getLAGInterfaces1/
│   │   │   │       ├── ME1200Lacp.txt (9 lines)
│   │   │   │       ├── getLAGInterfaces1.par (53 lines)
│   │   │   │       ├── getLAGInterfaces1Parser_xde.rpl (80 lines)
│   │   │   │       └── ifm-im-connectivity-ext-module.xsd (2957 lines)
│   │   │   ├── lag_interface1200.xpa/
│   │   │   │   └── getLAGInterfaces/
│   │   │   │       ├── ME1200Lacp.txt (8 lines)
│   │   │   │       ├── getLAGInterfaces.par (53 lines)
│   │   │   │       ├── getLAGInterfacesParser_xde.rpl (192 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (834 lines)
│   │   │   ├── lag_interface_static_1200.xpa/
│   │   │   │   └── getLAGInterfaces/
│   │   │   │       ├── ME1200Lacp.txt (4 lines)
│   │   │   │       ├── getLAGInterfaces.par (53 lines)
│   │   │   │       ├── getLAGInterfacesParser_xde.rpl (207 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (834 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── lagInventoryProcedure.xde (63 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.Vcop-inventory/
│   │   │   ├── getInterfaceName.xpa/
│   │   │   │   └── getInterfaceName/
│   │   │   │       ├── InterfaaceName_output (14 lines)
│   │   │   │       ├── device-capability-model.xsd (653 lines)
│   │   │   │       ├── getInterfaceName.par (28 lines)
│   │   │   │       ├── getInterfaceNameParserOutput.xsd (6 lines)
│   │   │   │       ├── getInterfaceNameParser_xdeIOS.rpl (79 lines)
│   │   │   │       └── getInterfaceNameParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── getSsfpdDetails.xpa/
│   │   │   │   └── getSsfpdDetails/
│   │   │   │       ├── VCOP_SSPFPD_output (27 lines)
│   │   │   │       ├── device-capability-model.xsd (722 lines)
│   │   │   │       ├── getSsfpdDetails.out.xml (0 lines)
│   │   │   │       ├── getSsfpdDetails.par (24 lines)
│   │   │   │       ├── getSsfpdDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getSsfpdDetailsParser_xdeIOS.rpl (99 lines)
│   │   │   │       └── getSsfpdDetailsParser_xdeIOSOutput.xsd (19 lines)
│   │   │   ├── getSuppInterfacelist.xpa/
│   │   │   │   └── getSuppInterfacelist/
│   │   │   │       ├── VCOP_SuppInter_output (60 lines)
│   │   │   │       ├── device-capability-model.xsd (722 lines)
│   │   │   │       ├── getSuppInterfacelist.par (24 lines)
│   │   │   │       ├── getSuppInterfacelistParserOutput.xsd (6 lines)
│   │   │   │       ├── getSuppInterfacelistParser_xdeIOS.rpl (80 lines)
│   │   │   │       └── getSuppInterfacelistParser_xdeIOSOutput.xsd (17 lines)
│   │   │   ├── getSupportedVCOPType.xpa/
│   │   │   │   └── getSupportedVCOPType/
│   │   │   │       ├── VCOP_ShowRun_Inv_output (8 lines)
│   │   │   │       ├── device-capability-model.xsd (722 lines)
│   │   │   │       ├── getSupportedVCOPType.out.xml (0 lines)
│   │   │   │       ├── getSupportedVCOPType.par (24 lines)
│   │   │   │       ├── getSupportedVCOPTypeParserOutput.xsd (6 lines)
│   │   │   │       ├── getSupportedVCOPTypeParser_xdeIOS.rpl (88 lines)
│   │   │   │       └── getSupportedVCOPTypeParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── getVCOPSfpDetails.xpa/
│   │   │   │   └── getVCOPSfpDetails/
│   │   │   │       ├── VCOP_ShowRun_Inv_output (8 lines)
│   │   │   │       ├── VCOP_ShowRun_Output (5 lines)
│   │   │   │       ├── device-capability-model.xsd (722 lines)
│   │   │   │       ├── getVCOPSfpDetails.par (29 lines)
│   │   │   │       ├── getVCOPSfpDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getVCOPSfpDetailsParser_xdeIOS.rpl (108 lines)
│   │   │   │       └── getVCOPSfpDetailsParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── xjsFunctions/
│   │   │   │   └── removeDuplicateObjects.xjs (74 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (563 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── com.cisco.prime.inventory.xde.ains-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── ains-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (39 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── transportState.xpa/
│   │   │   │   ├── getConfigurableIM/
│   │   │   │   │   ├── ASR907_IMListoutput (8 lines)
│   │   │   │   │   ├── ASR920_IMListoutput (15 lines)
│   │   │   │   │   ├── IMListoutput (29 lines)
│   │   │   │   │   ├── device-capability-model.xsd (685 lines)
│   │   │   │   │   ├── getConfigurableIM.par (59 lines)
│   │   │   │   │   ├── getConfigurableIMParserOutput.xsd (6 lines)
│   │   │   │   │   └── getConfigurableIMParser_xdeIOS.rpl (78 lines)
│   │   │   │   ├── getEntityDetails/
│   │   │   │   │   ├── getEntityDetails.map (11 lines)
│   │   │   │   │   ├── getEntityDetails.par (56 lines)
│   │   │   │   │   └── xmp-im-physical-resource-module.xsd (1030 lines)
│   │   │   │   └── getTransState/
│   │   │   │       ├── Output (21 lines)
│   │   │   │       ├── getTransState.par (53 lines)
│   │   │   │       ├── getTransStateParser_xdeIOS.rpl (489 lines)
│   │   │   │       ├── secState Output (11 lines)
│   │   │   │       └── xmp-im-physical-resource-module.xsd (1030 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (216 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.ains-port-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── ains-port-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (39 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── getAINSInterfaceState.xpa/
│   │   │   │   ├── getEntityDetails/
│   │   │   │   │   ├── getEntityDetails.par (54 lines)
│   │   │   │   │   ├── ios_xe (9 lines)
│   │   │   │   │   ├── parseAINSInterfaceState.rpl (46 lines)
│   │   │   │   │   └── xmp-im-connectivity-module.xsd (18 lines)
│   │   │   │   ├── getEntityDetailsGranular/
│   │   │   │   │   ├── getEntityDetails.par (57 lines)
│   │   │   │   │   ├── ios_xe (12 lines)
│   │   │   │   │   ├── parseAINSInterfaceStateGranular.rpl (165 lines)
│   │   │   │   │   └── xmp-im-connectivity-module.xsd (1304 lines)
│   │   │   │   ├── getSockTimeValueController/
│   │   │   │   │   ├── getEntityDetails.par (57 lines)
│   │   │   │   │   ├── ios_xe_controller (13 lines)
│   │   │   │   │   └── parseAINSInterfaceState.rpl (92 lines)
│   │   │   │   └── getSockTimeValueInterface/
│   │   │   │       ├── getEntityDetails.par (57 lines)
│   │   │   │       ├── ios_xe_interface (13 lines)
│   │   │   │       └── parseAINSInterfaceState.rpl (92 lines)
│   │   │   ├── javascript/
│   │   │   │   └── getAdminStatus.xjs (15 lines)
│   │   │   ├── test/
│   │   │   │   └── recordedTest.xft (1685 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (493 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.auth-key-chain-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── authentication-key-chain-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (21 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── authentication-key-chain-inventory/
│   │   │   │   ├── authentication-key-chain-inventory.par (99 lines)
│   │   │   │   ├── authentication-key-chain-inventoryParser_xdeIOS.rpl (230 lines)
│   │   │   │   ├── authentication-key-chain-inventoryParser_xdeIOS_XR.rpl (211 lines)
│   │   │   │   ├── xe_key_chain (13 lines)
│   │   │   │   ├── xmp-im-security-module.xsd (2304 lines)
│   │   │   │   └── xr_kaychain (9 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (28 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── com.cisco.prime.inventory.xde.bfd-template-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── bfd-template-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (21 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── bfd-template-inventory/
│   │   │   │   ├── bfd-template-inventory.par (111 lines)
│   │   │   │   ├── bfd-template-inventoryParser_xdeIOS.rpl (144 lines)
│   │   │   │   ├── bfd-template-inventoryParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   ├── bfd-template-inventoryParser_xdeIOS_XR.rpl (3 lines)
│   │   │   │   ├── getBFDTemplate.xde (83 lines)
│   │   │   │   ├── xe-bfd-template (74 lines)
│   │   │   │   ├── xmp-im-link-detect-module.xsd (485 lines)
│   │   │   │   └── xmp-im-mpls-te-module.xsd (1729 lines)
│   │   │   ├── .project (12 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── procedure.xde (55 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_hsrp_inventory/
│   │   │   ├── l3vpn-hsrp/
│   │   │   │   ├── XE-show archive log config all/
│   │   │   │   │   ├── XE-show archive log config all1.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all2.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_Delete_GroupAttribute.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_Pep.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_Pep1.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_delete_PepAttribute_.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_delete_manyGroup.txt (103 lines)
│   │   │   │   │   ├── XE-show archive log config all_delete_manyInterface.txt (103 lines)
│   │   │   │   │   └── show archive log config all.txt (103 lines)
│   │   │   │   ├── XR-show_config_commit_changes_last/
│   │   │   │   │   ├── XR-show_config_commit_changes_last.txt (20 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last2.txt (32 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_lastPEP1.txt (11 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_lastPEP2.txt (14 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_delete1.txt (15 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_deleteManyGroup.txt (14 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_delete_group.txt (13 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_delete_interface.txt (9 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_delete_many_PEP.txt (14 lines)
│   │   │   │   │   ├── XR-show_config_commit_changes_last_delete_many_interface.txt (10 lines)
│   │   │   │   │   └── outputXR.txt (60 lines)
│   │   │   │   ├── l3vpn-hsrp.par (90 lines)
│   │   │   │   ├── l3vpn-hsrpParserOutput.xsd (6 lines)
│   │   │   │   ├── l3vpn-hsrpParser_xdeIOS.rpl (340 lines)
│   │   │   │   ├── l3vpn-hsrpParser_xdeIOSOutput.xsd (26 lines)
│   │   │   │   ├── l3vpn-hsrpParser_xdeIOS_XR.rpl (352 lines)
│   │   │   │   └── l3vpn-hsrpParser_xdeIOS_XROutput.xsd (26 lines)
│   │   │   ├── l3vpnhsrpConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_ippep_inventory/
│   │   │   ├── l3vpn-ippep/
│   │   │   │   ├── interface_XE (8 lines)
│   │   │   │   ├── interface_XR (11 lines)
│   │   │   │   ├── l3vpnIPPepConfigChange.par (96 lines)
│   │   │   │   ├── l3vpnIpPepParserOutput.xsd (0 lines)
│   │   │   │   ├── updateInterfaceAddress_XE.rpl (170 lines)
│   │   │   │   └── updateInterfaceAddress_XR.rpl (110 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3vpnIPPepConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_ipsla_inventory/
│   │   │   ├── l3vpn-ipsla/
│   │   │   │   ├── l3vpn-ipsla.par (91 lines)
│   │   │   │   ├── l3vpn-ipslaParserOutput.xsd (6 lines)
│   │   │   │   ├── l3vpn-ipslaParser_xdeIOS.rpl (264 lines)
│   │   │   │   ├── l3vpn-ipslaParser_xdeIOSOutput.xsd (48 lines)
│   │   │   │   ├── l3vpn-ipslaParser_xdeIOSXR.rpl (421 lines)
│   │   │   │   ├── l3vpn-ipslaParser_xdeIOSXROutput.xsd (49 lines)
│   │   │   │   ├── show_archive_log_config_all.txt (64 lines)
│   │   │   │   └── show_config_commit_changes_last.txt (57 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3vpnIpslaConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_l3EnabledInterfaceSettings/
│   │   │   ├── l3EnabledInterfaceSettings/
│   │   │   │   ├── XR (52 lines)
│   │   │   │   ├── getConfChangel3InterfaceDetails.par (50 lines)
│   │   │   │   ├── getConfChangel3InterfaceDetailsParser_xdeIOS_XR.rpl (147 lines)
│   │   │   │   └── getConfChangel3InterfaceDetailsParser_xdeIOS_XROutput.xsd (37 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (21 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_ospf_inventory/
│   │   │   ├── l3vpn-ospf/
│   │   │   │   ├── XE-sh_config_commit_changes_last-Delete.txt (9 lines)
│   │   │   │   ├── XE-sh_config_commit_changes_last.txt (47 lines)
│   │   │   │   ├── XR-OSPFv3-ConfigChange.txt (20 lines)
│   │   │   │   ├── XR-OSPFv3-Delete.txt (10 lines)
│   │   │   │   ├── XR-sh_config_commit_changes_last-delete.txt (7 lines)
│   │   │   │   ├── l3vpn-ospf.par (91 lines)
│   │   │   │   ├── l3vpn-ospfParserOutput.xsd (6 lines)
│   │   │   │   ├── l3vpn-ospfParser_xdeIOS.rpl (488 lines)
│   │   │   │   ├── l3vpn-ospfParser_xdeIOSOutput.xsd (33 lines)
│   │   │   │   ├── l3vpn-ospfParser_xdeIOS_XR.rpl (685 lines)
│   │   │   │   ├── l3vpn-ospfParser_xdeIOS_XROutput.xsd (33 lines)
│   │   │   │   └── sh_config_commit_changes_last.txt (17 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3vpnOspfConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.l3vpn_config_change_routepolicy_inventory/
│   │   │   ├── l3vpn-routePolicy/
│   │   │   │   ├── l3vpn-routePolicy.par (90 lines)
│   │   │   │   ├── l3vpn-routePolicyParser_xdeIOS.rpl (123 lines)
│   │   │   │   ├── l3vpn-routePolicyParser_xdeIOS_XR.rpl (233 lines)
│   │   │   │   └── l3vpn-routePolicyParser_xdeIOS_XROutput.xsd (24 lines)
│   │   │   ├── l3vpnRoutePolicyProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.lspAttrList-inventory/
│   │   │   ├── lsp-attr-list-inventory/
│   │   │   │   ├── XEOutput.txt (27 lines)
│   │   │   │   ├── XROutput.txt (58 lines)
│   │   │   │   ├── lsp-attr-list-inventory.par (121 lines)
│   │   │   │   ├── lsp-attr-list-inventoryParser_xdeIOS.rpl (174 lines)
│   │   │   │   ├── lsp-attr-list-inventoryParser_xdeIOS_XR.rpl (122 lines)
│   │   │   │   └── xmp-im-mpls-te-module.xsd (23 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── procedure.xde (72 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.inventory.xde.port-mirroring-inventory/
│   │   │   ├── showSpanSession.xpa/
│   │   │   │   └── getMonitorSession/
│   │   │   │       ├── functionTest.xft (10 lines)
│   │   │   │       ├── getMonitorSession.par (63 lines)
│   │   │   │       ├── getMonitorSessionParser_xdeIOS.rpl (1339 lines)
│   │   │   │       └── xmp-im-monitor-module.xsd (966 lines)
│   │   │   ├── xJsFunctions/
│   │   │   │   └── getSeparateInterfaces.xjs (85 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (393 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.ptp-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── ptp-inventory/
│   │   │   │   │           ├── pom.properties (5 lines)
│   │   │   │   │           └── pom.xml (39 lines)
│   │   │   │   └── MANIFEST.MF (6 lines)
│   │   │   ├── PtpClock.xpa/
│   │   │   │   ├── getPortDetails/
│   │   │   │   │   ├── boundary (31 lines)
│   │   │   │   │   ├── getPortDetails.par (53 lines)
│   │   │   │   │   ├── getPortDetailsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getPortDetailsParser_xdeIOS.rpl (979 lines)
│   │   │   │   │   ├── getPortDetailsParser_xdeIOSOutput.xsd (22 lines)
│   │   │   │   │   ├── output_boundary_hybrid (172 lines)
│   │   │   │   │   ├── output_ordinary_master.txt (87 lines)
│   │   │   │   │   ├── output_ordinary_slave.txt (149 lines)
│   │   │   │   │   └── xmp-im-clock-module.xsd (2082 lines)
│   │   │   │   ├── getPortName/
│   │   │   │   │   ├── boundary (25 lines)
│   │   │   │   │   ├── getPortName.par (55 lines)
│   │   │   │   │   ├── getPortNameParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getPortNameParser_xdeIOS.rpl (196 lines)
│   │   │   │   │   ├── output_ordinary_master.txt (15 lines)
│   │   │   │   │   ├── output_ordinary_slave.txt (24 lines)
│   │   │   │   │   └── xmp-im-clock-module.xsd (2082 lines)
│   │   │   │   └── getPtpClock/
│   │   │   │       ├── Port Running detail (171 lines)
│   │   │   │       ├── TEST (97 lines)
│   │   │   │       ├── boundary_clock_3sources (135 lines)
│   │   │   │       ├── getPtpClock.par (71 lines)
│   │   │   │       ├── getPtpClockParserOutput.xsd (6 lines)
│   │   │   │       ├── getPtpClockParser_xdeIOS.rpl (2878 lines)
│   │   │   │       ├── ouputboundary (54 lines)
│   │   │   │       ├── output__redn_boundary.txt (172 lines)
│   │   │   │       ├── output__redn_ordinary_slave.txt (150 lines)
│   │   │   │       ├── output_boundary_hybrid (172 lines)
│   │   │   │       ├── output_ordinary_hybrid (148 lines)
│   │   │   │       ├── output_ordinary_master.txt (87 lines)
│   │   │   │       ├── output_ordinary_slave.txt (149 lines)
│   │   │   │       ├── outputmaster (92 lines)
│   │   │   │       └── xmp-im-clock-module.xsd (2023 lines)
│   │   │   ├── .project (30 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (208 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.sdr-inventory/
│   │   │   ├── getSdrName.xpa/
│   │   │   │   └── getSdrName/
│   │   │   │       ├── device-capability-model.xsd (680 lines)
│   │   │   │       ├── getSdrName.par (54 lines)
│   │   │   │       ├── getSdrNameParser_xdeIOS_XR.rpl (71 lines)
│   │   │   │       └── output.txt (29 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (56 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── com.cisco.prime.inventory.xde.serial-inventory/
│   │   │   ├── getGenricControllerPort/
│   │   │   │   ├── getGenricControllerPort.par (26 lines)
│   │   │   │   ├── getGenricControllerPortParserOutput.xsd (6 lines)
│   │   │   │   ├── getGenricControllerPortParser_xdeIOS.rpl (44 lines)
│   │   │   │   ├── getGenricControllerPortParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   └── output.txt (18 lines)
│   │   │   ├── getIfindex/
│   │   │   │   ├── D210.txt (295 lines)
│   │   │   │   ├── ME1200.txt (8208 lines)
│   │   │   │   ├── XR.txt (37 lines)
│   │   │   │   ├── asr9k (107 lines)
│   │   │   │   ├── getIfindex.par (289 lines)
│   │   │   │   ├── getIfindexParserOutput.xsd (6 lines)
│   │   │   │   ├── getIfindexParser_xdeIOS.rpl (102 lines)
│   │   │   │   ├── getIfindexParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   ├── getIfindexParser_xde_ME1200.rpl (111 lines)
│   │   │   │   ├── getIfindexParser_xde_Nexus.rpl (111 lines)
│   │   │   │   ├── getIfindexParser_xde_XR.rpl (93 lines)
│   │   │   │   ├── nexus.txt (66 lines)
│   │   │   │   ├── output.txt (158 lines)
│   │   │   │   └── output_109.txt (2394 lines)
│   │   │   ├── getInterfaceConfig/
│   │   │   │   ├── Output.txt (23 lines)
│   │   │   │   ├── getInterfaceConfig.par (52 lines)
│   │   │   │   ├── getInterfaceConfigParserOutput.xsd (6 lines)
│   │   │   │   ├── getInterfaceConfigParser_xdeIOS.rpl (286 lines)
│   │   │   │   └── getInterfaceConfigParser_xdeIOSOutput.xsd (22 lines)
│   │   │   ├── getRSClientStatusInfoForDevice/
│   │   │   │   ├── cli.output (5 lines)
│   │   │   │   ├── getRSClientStatusInfoForDevice.par (55 lines)
│   │   │   │   ├── getRSClientStatusInfoForDeviceParserOutput.xsd (6 lines)
│   │   │   │   ├── getRSClientStatusInfoForDeviceParser_xdeIOS.rpl (69 lines)
│   │   │   │   └── getRSClientStatusInfoForDeviceParser_xdeIOSOutput.xsd (11 lines)
│   │   │   ├── getRSVrfName/
│   │   │   │   ├── cli.out (5 lines)
│   │   │   │   ├── getRSVrfName.par (53 lines)
│   │   │   │   ├── getRSVrfNameParserOutput.xsd (6 lines)
│   │   │   │   ├── getRSVrfNameParser_xdeIOS.rpl (105 lines)
│   │   │   │   ├── getRSVrfNameParser_xdeIOSOutput.xsd (25 lines)
│   │   │   │   └── observation.txt (9 lines)
│   │   │   ├── getSerialControllerConfig/
│   │   │   │   ├── getSerialControllerConfig.par (57 lines)
│   │   │   │   ├── getSerialControllerConfigParserOutput.xsd (22 lines)
│   │   │   │   ├── getSerialControllerConfigParser_xdeIOS.rpl (321 lines)
│   │   │   │   ├── getSerialControllerConfigParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   ├── output1.txt (7 lines)
│   │   │   │   ├── output2.txt (9 lines)
│   │   │   │   ├── output3.txt (53 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (675 lines)
│   │   │   ├── getSerialLine/
│   │   │   │   ├── 17p01p01prd6_sessionCountSupport (30 lines)
│   │   │   │   ├── getSerialLine.par (64 lines)
│   │   │   │   ├── getSerialLineParserOutput.xsd (6 lines)
│   │   │   │   ├── getSerialLineParser_xdeIOS.rpl (1408 lines)
│   │   │   │   ├── getSerialLineParser_xdeIOSOutput.xsd (74 lines)
│   │   │   │   ├── output.txt (54 lines)
│   │   │   │   ├── output1.txt (54 lines)
│   │   │   │   ├── output2.txt (65 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (881 lines)
│   │   │   ├── getSerialPWEntities/
│   │   │   │   ├── Ouput_238.txt (31 lines)
│   │   │   │   ├── Output_179.txt (42 lines)
│   │   │   │   ├── Output_196 (29 lines)
│   │   │   │   ├── getSerialPWEntities.par (69 lines)
│   │   │   │   ├── getSerialPWEntitiesParserOutput.xsd (6 lines)
│   │   │   │   ├── getSerialPWEntitiesParser_xdeIOS.rpl (835 lines)
│   │   │   │   └── getSerialPWEntitiesParser_xdeIOSOutput.xsd (37 lines)
│   │   │   ├── getSerialPWPEP/
│   │   │   │   ├── getSerialPWPEP.par (84 lines)
│   │   │   │   ├── getSerialPWPEPParserOutput.xsd (6 lines)
│   │   │   │   ├── getSerialPWPEPParser_xdeIOS.rpl (426 lines)
│   │   │   │   ├── getSerialPWPEPParser_xdeIOSOutput.xsd (25 lines)
│   │   │   │   ├── output_1 (9 lines)
│   │   │   │   ├── output_2 (49 lines)
│   │   │   │   ├── output_3 (49 lines)
│   │   │   │   └── prime-resource-model.xsd (25 lines)
│   │   │   ├── javaScriptFunctions/
│   │   │   │   ├── constants.xct (30 lines)
│   │   │   │   ├── getClientStatusMap.xjs (78 lines)
│   │   │   │   ├── getInterfaceDetails.xjs (43 lines)
│   │   │   │   ├── getInterfaceNamebyIndex.xjs (38 lines)
│   │   │   │   ├── getRawSocketClient.xjs (128 lines)
│   │   │   │   ├── getRawSocketDetails.xjs (43 lines)
│   │   │   │   ├── getRawSocketServer.xjs (79 lines)
│   │   │   │   ├── getRawSocketSettings.xjs (79 lines)
│   │   │   │   ├── getSerialLineDetails.xjs (144 lines)
│   │   │   │   ├── getSerialPEP.xjs (119 lines)
│   │   │   │   └── getVRFDetailsMap.xjs (27 lines)
│   │   │   ├── test/
│   │   │   │   ├── ProcedureTest.xft (1410 lines)
│   │   │   │   ├── ProcedureWithParamsTest.xft (1093 lines)
│   │   │   │   ├── getGenricControllerPortTest.xft (63 lines)
│   │   │   │   ├── getInterfaceConfig.xft (2056 lines)
│   │   │   │   ├── getSerialLine.xft (86 lines)
│   │   │   │   ├── getSerialPWEntitiesTest.xft (53 lines)
│   │   │   │   ├── getVrfNameTest.xft (43 lines)
│   │   │   │   ├── rawSocketProcedureTest.xft (102 lines)
│   │   │   │   ├── rawSocketProcedureWithParamsTest.xft (112 lines)
│   │   │   │   ├── serialControllerProcedureTest.xft (1046 lines)
│   │   │   │   ├── serialControllerProcedureWithParamsTest.xft (811 lines)
│   │   │   │   ├── serialLineProcedureTest.xft (234 lines)
│   │   │   │   ├── serialLineProcedureWithParamsTestxft.xft (78 lines)
│   │   │   │   ├── serialPWPepProcedureTest.xft (212 lines)
│   │   │   │   ├── serialPWPepProcedureWithParamsTest.xft (103 lines)
│   │   │   │   ├── serialPWProcedureTest.xft (239 lines)
│   │   │   │   └── serialPWProcedureWithParamsTest.xft (112 lines)
│   │   │   ├── xde/
│   │   │   │   ├── rawSocketProcedure.xde (92 lines)
│   │   │   │   ├── serialControllerProcedure.xde (79 lines)
│   │   │   │   ├── serialLineProcedure.xde (74 lines)
│   │   │   │   ├── serialPWPepProcedure.xde (170 lines)
│   │   │   │   └── serialPWProcedure.xde (276 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (97 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.prime.inventory.xde.synce-inventory/
│   │   │   ├── getSyncEthClock.xpa/
│   │   │   │   ├── getPortParameter/
│   │   │   │   │   ├── getPortParameter.par (65 lines)
│   │   │   │   │   ├── getPortParameter_xdeIOSXR4K.rpl (220 lines)
│   │   │   │   │   └── xmp-im-clock-module.xsd (18 lines)
│   │   │   │   ├── getSyncEthClock/
│   │   │   │   │   ├── 184_cliOutput.txt (193 lines)
│   │   │   │   │   ├── CwWSyccliOutput.txt (124 lines)
│   │   │   │   │   ├── ExternalOutput.txt (124 lines)
│   │   │   │   │   ├── FourtyGigaGranular.txt (47 lines)
│   │   │   │   │   ├── FourtyGigaOutput.txt (76 lines)
│   │   │   │   │   ├── GranularIssue_Duplicate.txt (65 lines)
│   │   │   │   │   ├── Granular_output_Full_log.txt (67 lines)
│   │   │   │   │   ├── Granular_output_G10.txt (47 lines)
│   │   │   │   │   ├── HunGigaGranular.txt (47 lines)
│   │   │   │   │   ├── HundredGigaOutput.txt (122 lines)
│   │   │   │   │   ├── NCS4KOutputXRBITSIssue.txt (182 lines)
│   │   │   │   │   ├── Pepoutput.txt (53 lines)
│   │   │   │   │   ├── bitsshowoutput (165 lines)
│   │   │   │   │   ├── getSyncEthClock.par (187 lines)
│   │   │   │   │   ├── getSyncEthClockParser_xdeIOS.rpl (6906 lines)
│   │   │   │   │   ├── getSyncEthClockParser_xdeIOSXR.rpl (10280 lines)
│   │   │   │   │   ├── iox_xr_output_global_independent (38 lines)
│   │   │   │   │   ├── new output.txt (122 lines)
│   │   │   │   │   ├── newoutput.txt (124 lines)
│   │   │   │   │   ├── output.txt (220 lines)
│   │   │   │   │   ├── outputExtR0.txt (45 lines)
│   │   │   │   │   ├── outputExtR1.txt (45 lines)
│   │   │   │   │   ├── outputInterface.txt (48 lines)
│   │   │   │   │   ├── outputInterface1.txt (48 lines)
│   │   │   │   │   ├── output_HundredGiga_iox_xr (39 lines)
│   │   │   │   │   ├── output_HundredGiga_iox_xr_SSM_Dis (22 lines)
│   │   │   │   │   ├── output_HundredGiga_iox_xr_SSM_Ena (39 lines)
│   │   │   │   │   ├── outputglb.txt (18 lines)
│   │   │   │   │   ├── synce-inventory-xr-results (41 lines)
│   │   │   │   │   ├── synceethPepsettingsError.txt (170 lines)
│   │   │   │   │   ├── tengi.txt (48 lines)
│   │   │   │   │   ├── xmp-im-clock-module.xml (603 lines)
│   │   │   │   │   └── xmp-im-clock-module.xsd (278 lines)
│   │   │   │   ├── getSyncEthClock4K/
│   │   │   │   │   ├── getSyncEthClock.par (78 lines)
│   │   │   │   │   ├── getSyncEthClockParser_xdeIOSXR4K.rpl (11922 lines)
│   │   │   │   │   ├── xmp-im-clock-module.xml (603 lines)
│   │   │   │   │   └── xmp-im-clock-module.xsd (2043 lines)
│   │   │   │   └── getSyncEthClockBits/
│   │   │   │       ├── Input (2 lines)
│   │   │   │       ├── getSyncEthClockBits.par (57 lines)
│   │   │   │       ├── getSyncEthClockBitsParser_xdeIOS.rpl (99 lines)
│   │   │   │       └── xmp-im-clock-module.xsd (2043 lines)
│   │   │   ├── javascript/
│   │   │   │   ├── getLineBuildOutAssignValue.xjs (31 lines)
│   │   │   │   ├── getLineBuildOutConstantValue.xjs (38 lines)
│   │   │   │   ├── getLineCodeValue.xjs (79 lines)
│   │   │   │   └── getPortParameter.xjs (45 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (347 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-SegmentRouting-inventory/
│   │   │   ├── getLoopbackIP/
│   │   │   │   ├── LoopBackName_Output.txt (10 lines)
│   │   │   │   ├── LoopbackInterfaceXE.txt (7 lines)
│   │   │   │   ├── getLoopbackIP.par (107 lines)
│   │   │   │   ├── getLoopbackIPParser_xdeIOS.rpl (79 lines)
│   │   │   │   ├── getLoopbackIPParser_xdeIOSOutput.xsd (22 lines)
│   │   │   │   └── getLoopbackIPParser_xdeIOSXR.rpl (79 lines)
│   │   │   ├── getPcePeerState/
│   │   │   │   ├── XROutput_PendingState (5 lines)
│   │   │   │   ├── getPcePeerState.par (54 lines)
│   │   │   │   ├── getPcePeerStateParserOutput.xsd (6 lines)
│   │   │   │   ├── getPcePeerStateParser_xdeIOS_XR.rpl (70 lines)
│   │   │   │   └── getPcePeerStateParser_xdeIOS_XROutput.xsd (18 lines)
│   │   │   ├── getPceServerSettings/
│   │   │   │   ├── Output.txt (10 lines)
│   │   │   │   ├── getPceServerSettings.par (65 lines)
│   │   │   │   └── getPceServerSettingsParser_xdeIOS_XR.rpl (147 lines)
│   │   │   ├── getRoutingProcessName/
│   │   │   │   ├── LoopbackInterfaceDetail.txt (4 lines)
│   │   │   │   ├── getRoutingProcessName.par (58 lines)
│   │   │   │   ├── getRoutingProcessNameParser_xdeIOS.rpl (189 lines)
│   │   │   │   └── getRoutingProcessNameParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── getSegmentRoutingDetails/
│   │   │   │   ├── Output (64 lines)
│   │   │   │   ├── SR_IGP_and_LocalSID_XE.txt (43 lines)
│   │   │   │   ├── getSegmentRoutingDetails.par (132 lines)
│   │   │   │   ├── getSegmentRoutingDetailsParser_xdeIOS.rpl (664 lines)
│   │   │   │   ├── getSegmentRoutingDetailsParser_xdeIOSXR.rpl (1146 lines)
│   │   │   │   ├── output.txt (30 lines)
│   │   │   │   ├── output1.txt (24 lines)
│   │   │   │   ├── output2 (31 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (35 lines)
│   │   │   ├── getSegmentRoutingNeSettings/
│   │   │   │   ├── IOSXR (72 lines)
│   │   │   │   ├── PCE_SR_Output_XR.txt (88 lines)
│   │   │   │   ├── SR_NE_XE.txt (29 lines)
│   │   │   │   ├── getSegmentRoutingNeSettings.par (122 lines)
│   │   │   │   ├── getSegmentRoutingNeSettingsParserOutput.xsd (31 lines)
│   │   │   │   ├── getSegmentRoutingNeSettingsParser_xdeIOS.rpl (377 lines)
│   │   │   │   ├── getSegmentRoutingNeSettingsParser_xdeIOSXR.rpl (1094 lines)
│   │   │   │   ├── output.txt (3 lines)
│   │   │   │   ├── output2.txt (8 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (38 lines)
│   │   │   ├── getSegmentRoutingPrefixSidMapping/
│   │   │   │   ├── Output (279 lines)
│   │   │   │   ├── getSegmentRoutingPrefixSidMapping.par (103 lines)
│   │   │   │   ├── getSegmentRoutingPrefixSidMappingParserOutput.xsd (6 lines)
│   │   │   │   ├── getSegmentRoutingPrefixSidMappingParser_xdeIOS.rpl (189 lines)
│   │   │   │   ├── getSegmentRoutingPrefixSidMappingParser_xdeIOSXR.rpl (329 lines)
│   │   │   │   ├── output.txt (30 lines)
│   │   │   │   ├── output1.txt (24 lines)
│   │   │   │   ├── output2 (31 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (35 lines)
│   │   │   ├── javaScriptFunctions/
│   │   │   │   ├── setLocalSidDetails.xjs (35 lines)
│   │   │   │   ├── setLocalSidDetailsXE.xjs (69 lines)
│   │   │   │   ├── setPeerState.xjs (26 lines)
│   │   │   │   └── setStateSyncAddresses.xjs (41 lines)
│   │   │   ├── tests/
│   │   │   │   ├── IOS-XR-fullProcedure.xft (4918 lines)
│   │   │   │   ├── IOS-XR-getMPLSForwardingDetails.xft (275 lines)
│   │   │   │   ├── IOS-XR-getSegmentRoutingPolicySettings.xft (1848 lines)
│   │   │   │   └── IOS-XR-getSegmentRoutingSegmentList.xft (582 lines)
│   │   │   ├── xde/
│   │   │   │   ├── srXEGIProcedure.xde (97 lines)
│   │   │   │   └── srXRGIProcedure.xde (143 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (215 lines)
│   │   │   ├── xmp-im-mpls-module.xsd (2186 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-VSS-Redundancy-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── xde-VSS-Redundancy-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (41 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── getClusterControlPepSettings/
│   │   │   │   ├── getClusterControlPepSettings.par (53 lines)
│   │   │   │   ├── getClusterControlPepSettingsParserOutput.xsd (6 lines)
│   │   │   │   ├── getClusterControlPepSettingsParser_xdeIOS.rpl (84 lines)
│   │   │   │   ├── output_138.txt (93 lines)
│   │   │   │   ├── output_230.txt (74 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (684 lines)
│   │   │   ├── getClusterControlPepSettingsName/
│   │   │   │   ├── getClusterControlPepSettingsName.par (53 lines)
│   │   │   │   ├── getClusterControlPepSettingsNameParserOutput.xsd (6 lines)
│   │   │   │   ├── getClusterControlPepSettingsNameParser_xdeIOS.rpl (282 lines)
│   │   │   │   ├── getClusterControlPepSettingsNameParser_xdeIOSOutput.xsd (17 lines)
│   │   │   │   ├── output.txt (20 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (31 lines)
│   │   │   ├── getClusterIrlPepSettings/
│   │   │   │   ├── getClusterIrlPepSettings.par (53 lines)
│   │   │   │   ├── getClusterIrlPepSettingsParserOutput.xsd (6 lines)
│   │   │   │   ├── getClusterIrlPepSettingsParser_xdeIOS.rpl (110 lines)
│   │   │   │   ├── output_138.txt (93 lines)
│   │   │   │   ├── output_230.txt (74 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (684 lines)
│   │   │   ├── getClusterMember/
│   │   │   │   ├── getClusterMember.par (53 lines)
│   │   │   │   ├── getClusterMemberParserOutput.xsd (6 lines)
│   │   │   │   ├── getClusterMemberParser_xdeIOS.rpl (659 lines)
│   │   │   │   ├── output_138.txt (62 lines)
│   │   │   │   ├── output_230.txt (48 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (684 lines)
│   │   │   ├── getClusterSettings/
│   │   │   │   ├── getClusterSettings.par (53 lines)
│   │   │   │   ├── getClusterSettingsParserOutput.xsd (6 lines)
│   │   │   │   ├── getClusterSettingsParser_xdeIOS.rpl (88 lines)
│   │   │   │   ├── output_138.txt (8 lines)
│   │   │   │   ├── output_230.txt (8 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (684 lines)
│   │   │   ├── getMemberdetails/
│   │   │   │   ├── getMemberdetails.par (53 lines)
│   │   │   │   ├── getMemberdetailsParserOutput.xsd (6 lines)
│   │   │   │   ├── getMemberdetailsParser_xdeIOS.rpl (131 lines)
│   │   │   │   ├── output_138.txt (322 lines)
│   │   │   │   ├── output_230.txt (272 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (684 lines)
│   │   │   ├── getVslEndPointsSettings/
│   │   │   │   ├── getVslEndPointsSettings.par (56 lines)
│   │   │   │   ├── getVslEndPointsSettingsParserOutput.xsd (6 lines)
│   │   │   │   ├── getVslEndPointsSettingsParser_xdeIOS.rpl (140 lines)
│   │   │   │   ├── output_138.txt (117 lines)
│   │   │   │   ├── output_230.txt (99 lines)
│   │   │   │   └── xmp-im-switch-module.xsd (1822 lines)
│   │   │   ├── getVslInterfaces/
│   │   │   │   ├── getVslInterfaces.par (53 lines)
│   │   │   │   ├── getVslInterfacesParserOutput.xsd (6 lines)
│   │   │   │   ├── getVslInterfacesParser_xdeIOS.rpl (88 lines)
│   │   │   │   ├── getVslInterfacesParser_xdeIOSOutput.xsd (23 lines)
│   │   │   │   ├── output.txt (14 lines)
│   │   │   │   └── xmp-im-cluster-module.xsd (18 lines)
│   │   │   ├── vssRedundancy/
│   │   │   │   ├── output.txt (226 lines)
│   │   │   │   ├── vssRedundancy.par (70 lines)
│   │   │   │   ├── vssRedundancyParserOutput.xsd (1784 lines)
│   │   │   │   ├── vssRedundancyParser_xdeIOS.rpl (865 lines)
│   │   │   │   ├── vssRedundancyParser_xdeIOS2.rpl (982 lines)
│   │   │   │   └── xmp-im-switch-module.xsd (1837 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (732 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-cem-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── xde-cem-inventory/
│   │   │   │   │           ├── .project (17 lines)
│   │   │   │   │           ├── pom.properties (3 lines)
│   │   │   │   │           └── pom.xml (18 lines)
│   │   │   │   └── MANIFEST.MF (4 lines)
│   │   │   ├── XDE/
│   │   │   │   ├── C3794procedure.xde (212 lines)
│   │   │   │   ├── EandMprocedure.xde (51 lines)
│   │   │   │   ├── IOTRedirectHandler.xde (54 lines)
│   │   │   │   └── cemGIProcedure.xde (1667 lines)
│   │   │   ├── cisco-cem-C3794_Controller.xpa/
│   │   │   │   ├── getC3794LoopbackConfigsParser/
│   │   │   │   │   ├── getC3794LoopbackConfigs.par (68 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigsParser_xdeIOS.rpl (161 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigsParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   │   ├── output.txt (33 lines)
│   │   │   │   │   └── prime-optical-resource-model.xsd (11406 lines)
│   │   │   │   └── getInterfaceConfig/
│   │   │   │       ├── Output.txt (23 lines)
│   │   │   │       ├── getInterfaceConfig.par (53 lines)
│   │   │   │       ├── getInterfaceConfigParserOutput.xsd (6 lines)
│   │   │   │       ├── getInterfaceConfigParser_xdeIOS.rpl (286 lines)
│   │   │   │       └── getInterfaceConfigParser_xdeIOSOutput.xsd (19 lines)
│   │   │   ├── cisco-cem-EandM.xpa/
│   │   │   │   ├── getEMSlot/
│   │   │   │   │   ├── Output.txt (18 lines)
│   │   │   │   │   ├── getEMSlot.par (53 lines)
│   │   │   │   │   ├── getEMSlotParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getEMSlotParser_xdeIOS.rpl (43 lines)
│   │   │   │   │   └── getEMSlotParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   └── getEandMConfig/
│   │   │   │       ├── EM_Output1.txt (14 lines)
│   │   │   │       ├── getEandMConfig.par (56 lines)
│   │   │   │       ├── getEandMConfigParserOutput.xsd (6 lines)
│   │   │   │       ├── getEandMConfigParser_xdeIOS.rpl (487 lines)
│   │   │   │       └── getEandMConfigParser_xdeIOSOutput.xsd (30 lines)
│   │   │   ├── cisco-cem-acrdcr.xpa/
│   │   │   │   └── getACRDCRDetails/
│   │   │   │       ├── 22deviceoutput.txt (12 lines)
│   │   │   │       ├── 22latestoutput.txt (13 lines)
│   │   │   │       ├── 41Device.txt (15 lines)
│   │   │   │       ├── getACRDCRDetails.par (53 lines)
│   │   │   │       ├── getACRDCRDetailsParser_xdeIOS.rpl (1178 lines)
│   │   │   │       ├── latestoutput.txt (17 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (8230 lines)
│   │   │   │       └── xmp-im-clock-module.xsd (25 lines)
│   │   │   ├── cisco-cem-e1pep.xpa/
│   │   │   │   └── getE1Values/
│   │   │   │       ├── D160.txt (236 lines)
│   │   │   │       ├── E1.txt (577 lines)
│   │   │   │       ├── E1_Ctrl_Output.txt (2354 lines)
│   │   │   │       ├── getE1Values.par (70 lines)
│   │   │   │       ├── getE1ValuesParser_xdeIOS.rpl (786 lines)
│   │   │   │       ├── output46.txt (160 lines)
│   │   │   │       └── prime-optical-resource-model.xsd (8690 lines)
│   │   │   ├── cisco-cem-e3pep.xpa/
│   │   │   │   └── getE3Values/
│   │   │   │       ├── D42.txt (75 lines)
│   │   │   │       ├── D42_1.txt (913 lines)
│   │   │   │       ├── D42_E1_1.txt (436 lines)
│   │   │   │       ├── D42_E3_e1.txt (563 lines)
│   │   │   │       ├── D42_E3toE1.txt (773 lines)
│   │   │   │       ├── cablelength.txt (773 lines)
│   │   │   │       ├── cablelength2.txt (653 lines)
│   │   │   │       ├── e3.txt (18 lines)
│   │   │   │       ├── getE3Values.out.xml (0 lines)
│   │   │   │       ├── getE3Values.par (70 lines)
│   │   │   │       ├── getE3ValuesParser_xdeIOS.rpl (1590 lines)
│   │   │   │       ├── invalid32.txt (4 lines)
│   │   │   │       └── prime-optical-resource-model.xsd (49 lines)
│   │   │   ├── cisco-cem-genericcontrollerport.xpa/
│   │   │   │   ├── getCtrlRunConfigGranular/
│   │   │   │   │   ├── 184_E1Ctrl_Device_Output.txt (150 lines)
│   │   │   │   │   ├── 184_T1Ctrl_Device_Output.txt (656 lines)
│   │   │   │   │   ├── Running_Output.txt (3352 lines)
│   │   │   │   │   ├── getCtrlRunConfigGranular.par (63 lines)
│   │   │   │   │   ├── getCtrlRunConfigGranularParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getCtrlRunConfigGranularParser_xdeIOS.rpl (692 lines)
│   │   │   │   │   └── getCtrlRunConfigGranularParser_xdeIOSOutput.xsd (55 lines)
│   │   │   │   └── getMediaTypeInfo/
│   │   │   │       ├── 109.txt (2534 lines)
│   │   │   │       ├── 116.txt (2419 lines)
│   │   │   │       ├── 184_E1Ctrl_Device_Output.txt (150 lines)
│   │   │   │       ├── 184_T1Ctrl_Device_Output.txt (656 lines)
│   │   │   │       ├── 2.txt (6806 lines)
│   │   │   │       ├── 22Shutdown.txt (2097 lines)
│   │   │   │       ├── 32Shrun.txt (5124 lines)
│   │   │   │       ├── 32T3.txt (10 lines)
│   │   │   │       ├── 32_19.txt (7053 lines)
│   │   │   │       ├── 32_22.txt (7280 lines)
│   │   │   │       ├── 33.txt (2328 lines)
│   │   │   │       ├── 33_19.txt (7835 lines)
│   │   │   │       ├── 33_22.txt (7992 lines)
│   │   │   │       ├── 33_NewCli.txt (4754 lines)
│   │   │   │       ├── 41.txt (4168 lines)
│   │   │   │       ├── 41_TOH.txt (2564 lines)
│   │   │   │       ├── 46.txt (1573 lines)
│   │   │   │       ├── C3794 (1129 lines)
│   │   │   │       ├── D19_SDH_N1.txt (4845 lines)
│   │   │   │       ├── D19_SDH_New.txt (5107 lines)
│   │   │   │       ├── D19_SDH_mixed.txt (5360 lines)
│   │   │   │       ├── D32_16.6.6Vs_FC3.txt (9314 lines)
│   │   │   │       ├── D33_dummyMode.txt (3859 lines)
│   │   │   │       ├── D41_T3.txt (810 lines)
│   │   │   │       ├── D41_T3_Granular.txt (22 lines)
│   │   │   │       ├── D42V1681new1.txt (1743 lines)
│   │   │   │       ├── D42_16.8.1_E3.txt (3464 lines)
│   │   │   │       ├── D42_16.8.1_E3_LOP.txt (3470 lines)
│   │   │   │       ├── D42_16.8.1_exp.txt (3594 lines)
│   │   │   │       ├── D42_16.8.txt (4117 lines)
│   │   │   │       ├── D42_E3ToE1.txt (5517 lines)
│   │   │   │       ├── D42_SDHMixed_16.6.7_VS_fc2.txt (4751 lines)
│   │   │   │       ├── D58.txt (2201 lines)
│   │   │   │       ├── Device41.txt (1525 lines)
│   │   │   │       ├── Device53.txt (2174 lines)
│   │   │   │       ├── E3.txt (7 lines)
│   │   │   │       ├── E_Lop.txt (5514 lines)
│   │   │   │       ├── Lop_AU3_Mutlipe.txt (25 lines)
│   │   │   │       ├── Lop_AU4_Mutlipe.txt (55 lines)
│   │   │   │       ├── Running_Output.txt (3352 lines)
│   │   │   │       ├── SDH_136_1.txt (332 lines)
│   │   │   │       ├── SDH_160.txt (462 lines)
│   │   │   │       ├── Sdh136_2.txt (395 lines)
│   │   │   │       ├── SdhStm136.txt (312 lines)
│   │   │   │       ├── StsRange33.txt (3963 lines)
│   │   │   │       ├── cemgroup_32.txt (4680 lines)
│   │   │   │       ├── cemgroup_32_1.txt (4676 lines)
│   │   │   │       ├── cemgroup_33.txt (4572 lines)
│   │   │   │       ├── cliOutput.txt (2457 lines)
│   │   │   │       ├── d41.txt (3771 lines)
│   │   │   │       ├── getMediaTypeInfo.par (69 lines)
│   │   │   │       ├── getMediaTypeInfoParserOutput.xsd (283 lines)
│   │   │   │       ├── getMediaTypeInfoParser_TOH.xjs (59 lines)
│   │   │   │       ├── getMediaTypeInfoParser_xdeIOS.rpl (56036 lines)
│   │   │   │       ├── outpu32.txt (1726 lines)
│   │   │   │       ├── output.txt (1168 lines)
│   │   │   │       ├── output1.txt (22 lines)
│   │   │   │       ├── output109.txt (695 lines)
│   │   │   │       ├── output2.txt (18 lines)
│   │   │   │       ├── output22_running.txt (1545 lines)
│   │   │   │       ├── output24_latest.txt (1859 lines)
│   │   │   │       ├── output3.txt (818 lines)
│   │   │   │       ├── palawan.txt (954 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (7561 lines)
│   │   │   │       ├── run_config_lop.txt (2091 lines)
│   │   │   │       ├── runningconfig_21.txt (1112 lines)
│   │   │   │       ├── sonet_sdh_acr.txt (807 lines)
│   │   │   │       ├── sts1eVTG.txt (1733 lines)
│   │   │   │       ├── sts1e_allMode.txt (2330 lines)
│   │   │   │       └── t3run.txt (95 lines)
│   │   │   ├── cisco-cem-gettdmcemgrouppep.xpa/
│   │   │   │   └── gettdmcemgrouppep/
│   │   │   │       ├── 41.txt (553 lines)
│   │   │   │       ├── 42.txt (24 lines)
│   │   │   │       ├── CEP_22.txt (1393 lines)
│   │   │   │       ├── D41.txt (447 lines)
│   │   │   │       ├── Device 58.txt (481 lines)
│   │   │   │       ├── gettdmcemgrouppep.par (66 lines)
│   │   │   │       ├── gettdmcemgrouppepParser_xdeIOS.rpl (603 lines)
│   │   │   │       ├── output.txt (601 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (45 lines)
│   │   │   │       ├── sampleDeviceOutputIOS (96 lines)
│   │   │   │       └── timeslots_41.txt (553 lines)
│   │   │   ├── cisco-cem-pwpep.xpa/
│   │   │   │   ├── getPwPep/
│   │   │   │   │   ├── D168 (2871 lines)
│   │   │   │   │   ├── D21 (324 lines)
│   │   │   │   │   ├── D24.txt (18 lines)
│   │   │   │   │   ├── D42.txt (50 lines)
│   │   │   │   │   ├── D42_InCom.txt (14 lines)
│   │   │   │   │   ├── D_103_1 (166 lines)
│   │   │   │   │   ├── D_149_1 (178 lines)
│   │   │   │   │   ├── PwProtocolEndpoint_ios.xsd (38 lines)
│   │   │   │   │   ├── getPwPep.par (73 lines)
│   │   │   │   │   ├── getPwPepParser_xdeIOS.rpl (520 lines)
│   │   │   │   │   ├── out_184.txt (67 lines)
│   │   │   │   │   ├── output1.txt (64 lines)
│   │   │   │   │   ├── output2.txt (130 lines)
│   │   │   │   │   ├── prime-resource-model.xsd (25 lines)
│   │   │   │   │   ├── show l2vpn service xconnect all detail.txt (67 lines)
│   │   │   │   │   └── verizon.txt (24 lines)
│   │   │   │   └── getPwPepDescription/
│   │   │   │       ├── getPwPepDescription.par (57 lines)
│   │   │   │       ├── getPwPepDescriptionParserOutput.xsd (6 lines)
│   │   │   │       ├── getPwPepDescriptionParser_xdeIOS.rpl (42 lines)
│   │   │   │       ├── getPwPepDescriptionParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │       └── pse119.txt (9 lines)
│   │   │   ├── cisco-cem-sonethoploppep.xpa/
│   │   │   │   └── getSonet/
│   │   │   │       ├── 22_5.txt (8485 lines)
│   │   │   │       ├── 22_I1.txt (4502 lines)
│   │   │   │       ├── 33_CT3.txt (15264 lines)
│   │   │   │       ├── 33_LOP.txt (14184 lines)
│   │   │   │       ├── 33_NewCLI1.txt (10080 lines)
│   │   │   │       ├── Concat_new (1575 lines)
│   │   │   │       ├── D160Sonet.txt (1834 lines)
│   │   │   │       ├── D19(NCS42XX_show_controllers).txt (30868 lines)
│   │   │   │       ├── D19_STS_shutdown.txt (5655 lines)
│   │   │   │       ├── D19_STSnC.txt (5655 lines)
│   │   │   │       ├── D41_16.6.6.txt (28778 lines)
│   │   │   │       ├── D42 (12510 lines)
│   │   │   │       ├── D42_16.8.1_exp.txt (34930 lines)
│   │   │   │       ├── D42_16.8.1_loopback.txt (98022 lines)
│   │   │   │       ├── D42_Admin.txt (14251 lines)
│   │   │   │       ├── D42_Lop_shutdown.txt (3531 lines)
│   │   │   │       ├── D42_lattest3.txt (13658 lines)
│   │   │   │       ├── D42_m13.txt (81107 lines)
│   │   │   │       ├── Dev_133.txt (1391 lines)
│   │   │   │       ├── Dev_160_1.txt (998 lines)
│   │   │   │       ├── NCS42XX_SDH (830 lines)
│   │   │   │       ├── SDH_136.txt (1375 lines)
│   │   │   │       ├── SDH_46_2.txt (1280 lines)
│   │   │   │       ├── SONET_22_7.txt (2959 lines)
│   │   │   │       ├── Sdh136_4.txt (794 lines)
│   │   │   │       ├── Sonet@21.txt (604 lines)
│   │   │   │       ├── Sonet_Loopback1.txt (3452 lines)
│   │   │   │       ├── Sonet_loopback.txt (3445 lines)
│   │   │   │       ├── Sonet_loopback2.txt (3566 lines)
│   │   │   │       ├── Sonet_loopback3.txt (3541 lines)
│   │   │   │       ├── Sonet_loopback6.txt (3630 lines)
│   │   │   │       ├── VT-2.txt (2524 lines)
│   │   │   │       ├── VT15New.txt (35893 lines)
│   │   │   │       ├── dev_33.txt (15016 lines)
│   │   │   │       ├── getSonet.par (71 lines)
│   │   │   │       ├── getSonetParser_xdeIOS.rpl (8319 lines)
│   │   │   │       ├── getSonetParser_xdeIOSOutput.xsd (124 lines)
│   │   │   │       ├── output.txt (2399 lines)
│   │   │   │       ├── output46.txt (1513 lines)
│   │   │   │       ├── output_D42_4.txt (39510 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (6985 lines)
│   │   │   │       ├── run-config.txt (343 lines)
│   │   │   │       ├── sonet.txt (1468 lines)
│   │   │   │       ├── sonet1.txt (1403 lines)
│   │   │   │       ├── sonet2.txt (1415 lines)
│   │   │   │       ├── sonet3.txt (1948 lines)
│   │   │   │       ├── sonet4.txt (1948 lines)
│   │   │   │       ├── sonet5.txt (1949 lines)
│   │   │   │       ├── sonet6.txt (605 lines)
│   │   │   │       ├── sonet_21.txt (605 lines)
│   │   │   │       ├── sonet_22.txt (1538 lines)
│   │   │   │       ├── sonet_22_1.txt (2036 lines)
│   │   │   │       ├── sonet_22_2.txt (2398 lines)
│   │   │   │       ├── sonet_22_4.txt (2398 lines)
│   │   │   │       ├── sonet_22_5.txt (3146 lines)
│   │   │   │       ├── sonet_22_6.txt (2494 lines)
│   │   │   │       ├── sonet_VT2.txt (629 lines)
│   │   │   │       ├── sonet_output.txt (1467 lines)
│   │   │   │       └── sts1e_vtg.txt (1310 lines)
│   │   │   ├── cisco-cem-sonetprotectinaps.xpa/
│   │   │   │   ├── getLoopBackIP/
│   │   │   │   │   ├── 19_SDH_Output.txt (21 lines)
│   │   │   │   │   ├── 32.txt (20 lines)
│   │   │   │   │   ├── 41_APS_Output.txt (32 lines)
│   │   │   │   │   ├── D41.txt (38 lines)
│   │   │   │   │   ├── D42.txt (39 lines)
│   │   │   │   │   ├── aps.txt (32 lines)
│   │   │   │   │   ├── getLoopBackIP.par (53 lines)
│   │   │   │   │   ├── getLoopBackIPParser_xdeIOS.rpl (1006 lines)
│   │   │   │   │   ├── prime-optical-resource-model.xsd (47 lines)
│   │   │   │   │   └── revertiveoutput.txt (20 lines)
│   │   │   │   ├── getLoopbackName/
│   │   │   │   │   ├── LoopBackName_Output.txt (10 lines)
│   │   │   │   │   ├── LoopBack_19NameOutput.txt (5 lines)
│   │   │   │   │   ├── getLoopbackName.par (53 lines)
│   │   │   │   │   ├── getLoopbackNameParser_xdeIOS.rpl (89 lines)
│   │   │   │   │   └── getLoopbackNameParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   ├── getSonetAcrController/
│   │   │   │   │   ├── 1.txt (7335 lines)
│   │   │   │   │   ├── 32.txt (860 lines)
│   │   │   │   │   ├── D116ACR.txt (25898 lines)
│   │   │   │   │   ├── D116complete1.txt (49858 lines)
│   │   │   │   │   ├── D19.txt (48087 lines)
│   │   │   │   │   ├── D20_15.6(2)SP4.txt (235 lines)
│   │   │   │   │   ├── D41ACR1.txt (2898 lines)
│   │   │   │   │   ├── D41Acr.txt (4713 lines)
│   │   │   │   │   ├── D41TestImage1666vs1.txt (5052 lines)
│   │   │   │   │   ├── D41TestImage1666vs2.txt (5052 lines)
│   │   │   │   │   ├── D41_16.6.20180411 (3368 lines)
│   │   │   │   │   ├── D41_16.6.20180411_122955.txt (3369 lines)
│   │   │   │   │   ├── D42.txt (45020 lines)
│   │   │   │   │   ├── D42V1681output2.txt (3249 lines)
│   │   │   │   │   ├── D42_shutdown.txt (44738 lines)
│   │   │   │   │   ├── D42v1681output1.txt (4187 lines)
│   │   │   │   │   ├── STS12C (36 lines)
│   │   │   │   │   ├── getSonetAcrController.par (53 lines)
│   │   │   │   │   ├── getSonetAcrControllerParser_xdeIOS.rpl (3629 lines)
│   │   │   │   │   ├── getSonetAcrControllerParser_xdeIOSOutput.xsd (79 lines)
│   │   │   │   │   ├── output.txt (11781 lines)
│   │   │   │   │   └── prime-optical-resource-model.xsd (7804 lines)
│   │   │   │   └── getsonetprotectionaps/
│   │   │   │       ├── 32.txt (6 lines)
│   │   │   │       ├── 32_1.txt (6 lines)
│   │   │   │       ├── Controller_Width (4 lines)
│   │   │   │       ├── D42.txt (7 lines)
│   │   │   │       ├── getsonetprotectionaps.par (65 lines)
│   │   │   │       ├── getsonetprotectionapsParser_xdeIOS.rpl (46 lines)
│   │   │   │       ├── getsonetprotectionapsParser_xdeIOSOutput.out.xml (0 lines)
│   │   │   │       ├── getsonetprotectionapsParser_xdeIOSOutput.xsd (21 lines)
│   │   │   │       ├── output.txt (7 lines)
│   │   │   │       └── prime-optical-resource-model.xsd (6985 lines)
│   │   │   ├── cisco-cem-sonetprotectionupsr.xpa/
│   │   │   │   ├── getSonetProtectionUpsr/
│   │   │   │   │   ├── 32_new.txt (53 lines)
│   │   │   │   │   ├── 33_1.txt (12 lines)
│   │   │   │   │   ├── 33_2.txt (15 lines)
│   │   │   │   │   ├── 33_UpserDelete.txt (34 lines)
│   │   │   │   │   ├── 33_UpsrDelete.txt (35 lines)
│   │   │   │   │   ├── D27_SD (10 lines)
│   │   │   │   │   ├── D41.txt (16 lines)
│   │   │   │   │   ├── New_109 (6 lines)
│   │   │   │   │   ├── getSonetProtectionUpsr.par (63 lines)
│   │   │   │   │   ├── getSonetProtectionUpsrParser_xdeIOS.rpl (90 lines)
│   │   │   │   │   ├── getSonetProtectionUpsrParser_xdeIOSOutput.out.xml (0 lines)
│   │   │   │   │   ├── getSonetProtectionUpsrParser_xdeIOSOutput.xsd (23 lines)
│   │   │   │   │   ├── output_prtgrp.txt (9 lines)
│   │   │   │   │   └── prime-optical-resource-model.xsd (12504 lines)
│   │   │   │   └── getUpsrStatus/
│   │   │   │       ├── D41_shutdown.txt (5 lines)
│   │   │   │       ├── D42.txt (5 lines)
│   │   │   │       ├── getUpsrStatus.par (56 lines)
│   │   │   │       ├── getUpsrStatusParserOutput.xsd (6 lines)
│   │   │   │       ├── getUpsrStatusParser_xdeIOS.rpl (127 lines)
│   │   │   │       └── getUpsrStatusParser_xdeIOSOutput.xsd (19 lines)
│   │   │   ├── cisco-cem-sts1ehoploppep.xpa/
│   │   │   │   └── getSts1e/
│   │   │   │       ├── BERT.txt (342 lines)
│   │   │   │       ├── BertAllModes.txt (4319 lines)
│   │   │   │       ├── BertT3Mode.txt (344 lines)
│   │   │   │       ├── BertUnframed.txt (322 lines)
│   │   │   │       ├── bertVTG.txt (1157 lines)
│   │   │   │       ├── getSts1E.par (71 lines)
│   │   │   │       ├── getSts1EParser_xdeIOS.rpl (6491 lines)
│   │   │   │       ├── getSts1EParser_xdeIOSOutput.xsd (124 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (6985 lines)
│   │   │   │       ├── sts1ECT3.txt (613 lines)
│   │   │   │       ├── sts1eT3.txt (337 lines)
│   │   │   │       ├── sts1eUnframed (120 lines)
│   │   │   │       ├── sts1eVTG.txt (1277 lines)
│   │   │   │       └── sts1e_vtg.txt (1310 lines)
│   │   │   ├── cisco-cem-t1pep.xpa/
│   │   │   │   └── getT1Values/
│   │   │   │       ├── 184_Output.txt (2268 lines)
│   │   │   │       ├── AllLoopback.txt (865 lines)
│   │   │   │       ├── D42_16.8.1.txt (1489 lines)
│   │   │   │       ├── T1.txt (626 lines)
│   │   │   │       ├── T1_Ctrl_Output.txt (2315 lines)
│   │   │   │       ├── cablelength.txt (919 lines)
│   │   │   │       ├── cardProt.txt (2273 lines)
│   │   │   │       ├── getT1Values.out.xml (0 lines)
│   │   │   │       ├── getT1Values.par (69 lines)
│   │   │   │       ├── getT1ValuesParser_xdeIOS.rpl (1102 lines)
│   │   │   │       ├── output21_BertError.txt (898 lines)
│   │   │   │       └── prime-optical-resource-model.xsd (12804 lines)
│   │   │   ├── cisco-cem-t3pep.xpa/
│   │   │   │   └── getT3Values/
│   │   │   │       ├── 131.txt (844 lines)
│   │   │   │       ├── All_loopback.txt (1104 lines)
│   │   │   │       ├── Bert_33All.txt (2558 lines)
│   │   │   │       ├── Bert_all.txt (2570 lines)
│   │   │   │       ├── D41.txt (474 lines)
│   │   │   │       ├── D41_MBC.txt (4420 lines)
│   │   │   │       ├── D41_admin_down.txt (2730 lines)
│   │   │   │       ├── D42_16.8.1.txt (928 lines)
│   │   │   │       ├── D42_16.8.1_exp.txt (1755 lines)
│   │   │   │       ├── T3_admin.txt (2802 lines)
│   │   │   │       ├── cablelength.txt (4166 lines)
│   │   │   │       ├── cablelength2.txt (681 lines)
│   │   │   │       ├── channel_loopback.txt (2119 lines)
│   │   │   │       ├── getT3Values.out.out.xml (0 lines)
│   │   │   │       ├── getT3Values.out.xml (0 lines)
│   │   │   │       ├── getT3Values.par (71 lines)
│   │   │   │       ├── getT3ValuesParser_xdeIOS.rpl (3903 lines)
│   │   │   │       ├── getT3Values_xdeIOSOutput.xsd (85 lines)
│   │   │   │       ├── invalid32.txt (4 lines)
│   │   │   │       ├── loopback_109.txt (2650 lines)
│   │   │   │       ├── output32_T1_Bert.txt (1228 lines)
│   │   │   │       ├── output33.txt (1336 lines)
│   │   │   │       ├── prime-optical-resource-model.xml (1512 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (7865 lines)
│   │   │   │       └── t3.txt (218 lines)
│   │   │   ├── cisco-cem-tdmcemclasssettings.xpa/
│   │   │   │   └── gettdmcemclasssettings/
│   │   │   │       ├── 21.txt (25 lines)
│   │   │   │       ├── 22_1.txt (34 lines)
│   │   │   │       ├── 32.txt (42 lines)
│   │   │   │       ├── gettdmcemclasssettings.par (34 lines)
│   │   │   │       ├── gettdmcemclasssettingsParser_xdeIOS.rpl (353 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (7462 lines)
│   │   │   │       └── sampleDeviceOutputIOS (27 lines)
│   │   │   ├── cisco-cem-tdmcemp2pforwarder.xpa/
│   │   │   │   └── getTdmCemP2PForwarderDetails/
│   │   │   │       ├── D41.txt (9 lines)
│   │   │   │       ├── D42.txt (6 lines)
│   │   │   │       ├── getTdmCemP2PForwarderDetails.par (66 lines)
│   │   │   │       ├── getTdmCemP2PForwarderDetailsParser_xdeIOS.rpl (74 lines)
│   │   │   │       ├── output21.txt (7 lines)
│   │   │   │       └── prime-tdm-resource-model.xsd (21 lines)
│   │   │   ├── cisco-cem-tdmmdlsettings.xpa/
│   │   │   │   └── getTdmMdlSettings/
│   │   │   │       ├── getTdmMdlSettings.par (24 lines)
│   │   │   │       ├── getTdmMdlSettingsParser_xdeIOS.rpl (491 lines)
│   │   │   │       ├── output.txt (44 lines)
│   │   │   │       ├── output1.txt (217 lines)
│   │   │   │       ├── output2.txt (218 lines)
│   │   │   │       ├── prime-optical-resource-model.xsd (7457 lines)
│   │   │   │       └── t3.txt (497 lines)
│   │   │   ├── com-cisco-tdmcempwconprotocolendpoint.xpa/
│   │   │   │   └── getTdmCemPWConProtocolEndpoint/
│   │   │   │       ├── D24.txt (18 lines)
│   │   │   │       ├── D41_pw.txt (215 lines)
│   │   │   │       ├── D42_local.txt (295 lines)
│   │   │   │       ├── D42_pw.txt (15 lines)
│   │   │   │       ├── D_103_1 (166 lines)
│   │   │   │       ├── D_149_1 (178 lines)
│   │   │   │       ├── getTdmCemPWConProtocolEndpoint.rpl (932 lines)
│   │   │   │       ├── getTdmCemPWConProtocolEndpointIOSOutput.xsd (38 lines)
│   │   │   │       ├── out_184.txt (53 lines)
│   │   │   │       ├── output.txt (53 lines)
│   │   │   │       ├── output1.txt (64 lines)
│   │   │   │       ├── output2.txt (130 lines)
│   │   │   │       ├── output32.txt (304 lines)
│   │   │   │       ├── output4.txt (40 lines)
│   │   │   │       ├── prime-tdm-resource-model.xsd (228 lines)
│   │   │   │       ├── show l2vpn service xconnect all detail.txt (67 lines)
│   │   │   │       ├── tdmCemPWConProtocolEndpoint.par (76 lines)
│   │   │   │       └── verizon.txt (24 lines)
│   │   │   ├── getCardProtection/
│   │   │   │   ├── D42.txt (7 lines)
│   │   │   │   ├── cardprotection_19.txt (6 lines)
│   │   │   │   ├── getCardProtection.par (63 lines)
│   │   │   │   ├── getCardProtectionParserOutput.xsd (6 lines)
│   │   │   │   ├── getCardProtectionParser_xdeIOS.rpl (45 lines)
│   │   │   │   ├── getCardProtectionParser_xdeIOSOutput.xsd (20 lines)
│   │   │   │   └── xmp-im-logical-resource-module.xsd (1110 lines)
│   │   │   ├── getCardProtectionDetails/
│   │   │   │   ├── 19_Output.txt (10 lines)
│   │   │   │   ├── card-protectionDetails_output.txt (15 lines)
│   │   │   │   ├── getCardProtectionDetails.par (59 lines)
│   │   │   │   ├── getCardProtectionDetailsParserOutput.xsd (22 lines)
│   │   │   │   ├── getCardProtectionDetailsParser_xdeIOS.rpl (261 lines)
│   │   │   │   ├── lockout_output.txt (15 lines)
│   │   │   │   └── xmp-im-logical-resource-module.xsd (1265 lines)
│   │   │   ├── getCardProtectionRevertTime/
│   │   │   │   ├── CardProtectionRevertTime_output.txt (7 lines)
│   │   │   │   ├── getCardProtectionRevertTime.par (63 lines)
│   │   │   │   ├── getCardProtectionRevertTimeParserOutput.xsd (18 lines)
│   │   │   │   ├── getCardProtectionRevertTimeParser_xdeIOS.rpl (88 lines)
│   │   │   │   └── xmp-im-logical-resource-module.xsd (1110 lines)
│   │   │   ├── getCardType/
│   │   │   │   ├── Platform_41.txt (24 lines)
│   │   │   │   ├── getCardType.par (53 lines)
│   │   │   │   ├── getCardTypeParserOutput.xsd (6 lines)
│   │   │   │   ├── getCardTypeParser_xdeIOS.rpl (79 lines)
│   │   │   │   └── getCardTypeParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── getDenethorCardMode/
│   │   │   │   ├── Denethor.txt (3 lines)
│   │   │   │   ├── getDenethorCardMode.par (63 lines)
│   │   │   │   ├── getDenethorCardModeParserOutput.xsd (6 lines)
│   │   │   │   ├── getDenethorCardModeParser_xdeIOS.rpl (86 lines)
│   │   │   │   └── getDenethorCardModeParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── getIfindex/
│   │   │   │   ├── D210.txt (295 lines)
│   │   │   │   ├── ME1200.txt (8208 lines)
│   │   │   │   ├── XR.txt (37 lines)
│   │   │   │   ├── asr9k (107 lines)
│   │   │   │   ├── getIfindex.par (289 lines)
│   │   │   │   ├── getIfindexParserOutput.xsd (6 lines)
│   │   │   │   ├── getIfindexParser_xdeIOS.rpl (102 lines)
│   │   │   │   ├── getIfindexParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   ├── getIfindexParser_xde_ME1200.rpl (111 lines)
│   │   │   │   ├── getIfindexParser_xde_Nexus.rpl (111 lines)
│   │   │   │   ├── getIfindexParser_xde_XR.rpl (93 lines)
│   │   │   │   ├── nexus.txt (66 lines)
│   │   │   │   ├── output.txt (158 lines)
│   │   │   │   └── output_109.txt (2394 lines)
│   │   │   ├── getSDHLopForGI/
│   │   │   │   ├── getSDHLopForGI.par (56 lines)
│   │   │   │   ├── getSDHLopForGIParserOutput.xsd (6 lines)
│   │   │   │   ├── getSDHLopForGIParser_xdeIOS.rpl (2101 lines)
│   │   │   │   └── getSDHLopForGIParser_xdeIOSOutput.xsd (32 lines)
│   │   │   ├── javaScriptFunctions/
│   │   │   │   ├── constants.xct (30 lines)
│   │   │   │   ├── getACRDCR.xjs (379 lines)
│   │   │   │   ├── getACRGroupForController.xjs (23 lines)
│   │   │   │   ├── getACRPhysicalController.xjs (33 lines)
│   │   │   │   ├── getAPSAdminstrativeConfig.xjs (140 lines)
│   │   │   │   ├── getAccessInterfaceName.xjs (65 lines)
│   │   │   │   ├── getCardDataMap.xjs (32 lines)
│   │   │   │   ├── getCardProtectionMap.xjs (35 lines)
│   │   │   │   ├── getCemClassSettings.xjs (31 lines)
│   │   │   │   ├── getCemGroupPEP.xjs (275 lines)
│   │   │   │   ├── getCemGroupPEP_bkp.xjs (282 lines)
│   │   │   │   ├── getCpgNum.xjs (17 lines)
│   │   │   │   ├── getDenethorMode.xjs (38 lines)
│   │   │   │   ├── getE1BertSettings.xjs (17 lines)
│   │   │   │   ├── getE1Pep.xjs (83 lines)
│   │   │   │   ├── getE1PepWithCardProtection.xjs (58 lines)
│   │   │   │   ├── getE3BertSettings.xjs (17 lines)
│   │   │   │   ├── getE3Lop.xjs (67 lines)
│   │   │   │   ├── getE3LopRun.xjs (47 lines)
│   │   │   │   ├── getE3Pep.xjs (51 lines)
│   │   │   │   ├── getE3PepRun.xjs (27 lines)
│   │   │   │   ├── getE3PepWithCardProtection.xjs (57 lines)
│   │   │   │   ├── getEandMController.xjs (195 lines)
│   │   │   │   ├── getEandMData.xjs (36 lines)
│   │   │   │   ├── getGenericControllerPorts.xjs (40 lines)
│   │   │   │   ├── getInterfaceDetails.xjs (43 lines)
│   │   │   │   ├── getInterfaceNamebyIndex.xjs (45 lines)
│   │   │   │   ├── getLoopbackModeT1E1.xjs (63 lines)
│   │   │   │   ├── getMedia.xjs (30 lines)
│   │   │   │   ├── getPWConnections.xjs (72 lines)
│   │   │   │   ├── getPWIDRemotePeer.xjs (42 lines)
│   │   │   │   ├── getPwPep.xjs (59 lines)
│   │   │   │   ├── getRedundancySet.xjs (72 lines)
│   │   │   │   ├── getRedundancySetMember.xjs (53 lines)
│   │   │   │   ├── getSDHHopNameForGI.xjs (32 lines)
│   │   │   │   ├── getSTS1EHopPepWithCardProtection.xjs (71 lines)
│   │   │   │   ├── getSTS1ELopPepWithCardProtection.xjs (100 lines)
│   │   │   │   ├── getSTS1EPepWithCardProtection.xjs (62 lines)
│   │   │   │   ├── getSdhHop.xjs (102 lines)
│   │   │   │   ├── getSdhHopFromVirtualController.xjs (71 lines)
│   │   │   │   ├── getSdhHopIfIndexData.xjs (102 lines)
│   │   │   │   ├── getSdhHopRun.xjs (56 lines)
│   │   │   │   ├── getSdhLop.xjs (106 lines)
│   │   │   │   ├── getSdhLopFromVirtualController.xjs (67 lines)
│   │   │   │   ├── getSdhLopIfIndexData.xjs (74 lines)
│   │   │   │   ├── getSdhLopRun.xjs (73 lines)
│   │   │   │   ├── getSonet.xjs (51 lines)
│   │   │   │   ├── getSonetAcrStatus.xjs (101 lines)
│   │   │   │   ├── getSonetBertSettings.xjs (35 lines)
│   │   │   │   ├── getSonetHop.xjs (52 lines)
│   │   │   │   ├── getSonetHopAcr.xjs (87 lines)
│   │   │   │   ├── getSonetHopFromVirtualController.xjs (71 lines)
│   │   │   │   ├── getSonetHopIfIndexData.xjs (85 lines)
│   │   │   │   ├── getSonetHopRun.xjs (51 lines)
│   │   │   │   ├── getSonetLop.xjs (101 lines)
│   │   │   │   ├── getSonetLopAcr.xjs (81 lines)
│   │   │   │   ├── getSonetLopFromVirtualController.xjs (67 lines)
│   │   │   │   ├── getSonetLopIfIndexData.xjs (44 lines)
│   │   │   │   ├── getSonetLopRun.xjs (74 lines)
│   │   │   │   ├── getSonetMdlSettings.xjs (31 lines)
│   │   │   │   ├── getSonetProtection.xjs (290 lines)
│   │   │   │   ├── getSonetProtectionUPSR.xjs (384 lines)
│   │   │   │   ├── getSonetRun.xjs (90 lines)
│   │   │   │   ├── getSonetSDHAugMapping.xjs (54 lines)
│   │   │   │   ├── getSts1eLop.xjs (107 lines)
│   │   │   │   ├── getT1BertSettings.xjs (17 lines)
│   │   │   │   ├── getT1Pep.xjs (79 lines)
│   │   │   │   ├── getT1PepWithCardProtection.xjs (57 lines)
│   │   │   │   ├── getT3BertSettings.xjs (51 lines)
│   │   │   │   ├── getT3Lop.xjs (78 lines)
│   │   │   │   ├── getT3LopRun.xjs (42 lines)
│   │   │   │   ├── getT3MdlSettings.xjs (28 lines)
│   │   │   │   ├── getT3Pep.xjs (51 lines)
│   │   │   │   ├── getT3PepRun.xjs (27 lines)
│   │   │   │   ├── getT3PepWithCardProtection.xjs (58 lines)
│   │   │   │   ├── getTdmCemGroupPepMap.xjs (138 lines)
│   │   │   │   ├── getTdmP2P.xjs (111 lines)
│   │   │   │   ├── getTdmP2PForwarderLocalConnectStatus.xjs (64 lines)
│   │   │   │   └── getTimeslotsBundleValues.xjs (30 lines)
│   │   │   ├── javascript/
│   │   │   │   ├── getT3lop.xjs (33 lines)
│   │   │   │   ├── getTdmCemGroup.xjs (181 lines)
│   │   │   │   ├── getsonet.xjs (21 lines)
│   │   │   │   ├── getsonetHop.xjs (83 lines)
│   │   │   │   ├── getsonetHop1.xjs (83 lines)
│   │   │   │   ├── getsonetRun.xjs (68 lines)
│   │   │   │   ├── getsonetRunHop.xjs (137 lines)
│   │   │   │   ├── getsonetRunHopLop.xjs (103 lines)
│   │   │   │   └── getsonetRunHopLop1.xjs (108 lines)
│   │   │   ├── sdhconfiguration/
│   │   │   │   ├── 41_VC3_cliOutput.txt (3837 lines)
│   │   │   │   ├── D19.txt (28298 lines)
│   │   │   │   ├── D19_CS_LB.txt (48768 lines)
│   │   │   │   ├── D19_SDH.txt (14665 lines)
│   │   │   │   ├── D19_SDH_16.7.txt (41395 lines)
│   │   │   │   ├── D19_SDH_2.txt (52423 lines)
│   │   │   │   ├── D19_Sdh_admin.txt (43985 lines)
│   │   │   │   ├── D19_T3.txt (32468 lines)
│   │   │   │   ├── D19_mixed.txt (53563 lines)
│   │   │   │   ├── D210_16.6.1_fc3.txt (2429 lines)
│   │   │   │   ├── D210_16.7.1_fc6.txt (14040 lines)
│   │   │   │   ├── D41_SDH.txt (14683 lines)
│   │   │   │   ├── D42_16.8.1_fc1.txt (29219 lines)
│   │   │   │   ├── D42_16.8.1_fc3_1.txt (29265 lines)
│   │   │   │   ├── D42_SDHMixed_16.6.7_VS_fc2.txt (3276 lines)
│   │   │   │   ├── sdhconfiguration.out.xml (0 lines)
│   │   │   │   ├── sdhconfiguration.par (69 lines)
│   │   │   │   ├── sdhconfigurationParserOutput.xsd (6 lines)
│   │   │   │   ├── sdhconfigurationParser_xdeIOS.rpl (6161 lines)
│   │   │   │   ├── sdhconfigurationParser_xdeIOSOutput.xsd (89 lines)
│   │   │   │   └── showControllerSDHOutput.txt (105729 lines)
│   │   │   ├── test/
│   │   │   │   ├── C3794/
│   │   │   │   │   ├── C3794procedure.xft (272 lines)
│   │   │   │   │   ├── C3794procedureWithParams.xft (233 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigs1.xft (53 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigs2.xft (53 lines)
│   │   │   │   │   ├── getC3794LoopbackConfigs3.xft (53 lines)
│   │   │   │   │   └── getC3794LoopbackConfigsParser.xft (50 lines)
│   │   │   │   ├── EandM/
│   │   │   │   │   ├── EandMprocedure.xft (318 lines)
│   │   │   │   │   ├── EandMprocedureWithParamsxft.xft (333 lines)
│   │   │   │   │   ├── getEMSlot.xft (63 lines)
│   │   │   │   │   └── getEandMConfig.xft (46 lines)
│   │   │   │   ├── PwPepDescription/
│   │   │   │   │   └── getPwPepDescription.xft (31 lines)
│   │   │   │   ├── STS1E/
│   │   │   │   │   ├── BertSettingsTest.xft (1915 lines)
│   │   │   │   │   ├── BertSettingsUnframedTest.xft (1320 lines)
│   │   │   │   │   ├── BertSettingsvtTest.xft (2162 lines)
│   │   │   │   │   ├── STS1ECardProtectionCT3Lop.xft (14580 lines)
│   │   │   │   │   ├── STS1ECardProtectionControllerLevelClockSourceChange.xft (1362 lines)
│   │   │   │   │   ├── STS1ECardProtectionCt3HopMode.xft (14063 lines)
│   │   │   │   │   ├── STS1ECardProtectionEnable.xft (13034 lines)
│   │   │   │   │   ├── STS1ECardProtectionMediaTypeEnable.xft (1554 lines)
│   │   │   │   │   ├── STS1ECardProtectionMediatypeDisable.xft (2383 lines)
│   │   │   │   │   ├── STS1ECardProtectionNOMODE.xft (4092 lines)
│   │   │   │   │   ├── STS1ECardProtectionT3HopMode.xft (3862 lines)
│   │   │   │   │   ├── STS1ECardProtectionVT15HopMode.xft (14141 lines)
│   │   │   │   │   ├── STS1ECardProtectionVt15Lop.xft (57846 lines)
│   │   │   │   │   ├── STS1ELopCT3withCemGroup.xft (7635 lines)
│   │   │   │   │   ├── STS1ELopVt15WithCemGroup.xft (8214 lines)
│   │   │   │   │   ├── STS1EMediaType.xft (1424 lines)
│   │   │   │   │   ├── STS1EhopLevelTest.xft (1955 lines)
│   │   │   │   │   ├── STS1EhopT3withAttributes.xft (2336 lines)
│   │   │   │   │   ├── STS1EhopT3withcemGroup.xft (1891 lines)
│   │   │   │   │   ├── STS1EhopUnframedwithAttributes.xft (2247 lines)
│   │   │   │   │   ├── STS1EhopmodeUnframedWithCemGroup.xft (1870 lines)
│   │   │   │   │   ├── STS1ElopCT3withAttributes.xft (6795 lines)
│   │   │   │   │   ├── STS1ElopVT15withAttributesSet.xft (8600 lines)
│   │   │   │   │   ├── STS1EmodeCT3unconfigure.xft (4733 lines)
│   │   │   │   │   ├── STS1EmodeT3unconfigure.xft (2157 lines)
│   │   │   │   │   ├── STS1EmodeUNFRAMEDunconfigure.xft (2158 lines)
│   │   │   │   │   ├── STS1EmodeVT15unconfigure.xft (4761 lines)
│   │   │   │   │   └── sts1ePepInventory.xft (1078 lines)
│   │   │   │   ├── sonetAndSDH/
│   │   │   │   │   ├── addedDollarInMediaTypeInfoGI.xft (3674 lines)
│   │   │   │   │   ├── gettdmcemgrpPepTohTest.xft (136 lines)
│   │   │   │   │   ├── sdhAU3Inventory.xft (34340 lines)
│   │   │   │   │   ├── sdhAU4Inventory.xft (192575 lines)
│   │   │   │   │   ├── sdhLopGI.xft (3418 lines)
│   │   │   │   │   ├── sdhMSPProtectionGroupPepGI.xft (28846 lines)
│   │   │   │   │   ├── sdhMspWithMembersGI.xft (58722 lines)
│   │   │   │   │   ├── sdhMspWithoutMembersGI.xft (1637 lines)
│   │   │   │   │   ├── sdhPhysicalControllerGI.xft (58710 lines)
│   │   │   │   │   ├── sdhSNCPData.xft (3421 lines)
│   │   │   │   │   ├── sonetProtectionGroupPepGI.xft (1198 lines)
│   │   │   │   │   ├── tdmcempwconprotocolendpointtest.xft (50 lines)
│   │   │   │   │   └── virtualControllerWithoutActiveMember.xft (33628 lines)
│   │   │   │   └── updatedDescWhenAdminDownTest.xft (148 lines)
│   │   │   ├── updateDescWhenAdminDown/
│   │   │   │   ├── 19AdminDown.txt (13 lines)
│   │   │   │   ├── updateDescWhenAdminDown.par (56 lines)
│   │   │   │   ├── updateDescWhenAdminDown.xjs (36 lines)
│   │   │   │   ├── updateDescWhenAdminDownParserOutput.xsd (6 lines)
│   │   │   │   ├── updateDescWhenAdminDownParser_xdeIOS.rpl (69 lines)
│   │   │   │   └── updateDescWhenAdminDownParser_xdeIOSOutput.xsd (18 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ceminventoryprocedure11.xde (413 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── prime-optical-resource-model.xml (1675 lines)
│   │   │   ├── prime-optical-resource-model.xsd (8690 lines)
│   │   │   ├── testcases (113 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-ethernet-oam-module-inventory-ME1200/
│   │   │   ├── EoamLinkMonitorSettings.xpa/
│   │   │   │   └── EoamLinkMonitorSettings/
│   │   │   │       ├── EoamLinkMonitorSettings.par (54 lines)
│   │   │   │       ├── EoamLinkMonitorSettingsParserOutput.xsd (6 lines)
│   │   │   │       ├── EoamLinkMonitorSettingsParser_xdeME1200_OS.rpl (203 lines)
│   │   │   │       ├── ME1200output.txt (361 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3178 lines)
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.xmp.config.xde/
│   │   │   │   │       └── ethernet-oam-module-inventory/
│   │   │   │   │           ├── .project (17 lines)
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (41 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── getDetailsofEOAM.xpa/
│   │   │   │   ├── getConnectivity/
│   │   │   │   │   ├── connectivity.txt (7 lines)
│   │   │   │   │   ├── getConnectivity.par (52 lines)
│   │   │   │   │   ├── getConnectivityParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getConnectivityParser_xdeME1200_OS.rpl (53 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (20 lines)
│   │   │   │   ├── getMep/
│   │   │   │   │   ├── getMep.par (53 lines)
│   │   │   │   │   ├── getMepParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getMepParser_xdeME1200_OS.rpl (81 lines)
│   │   │   │   │   ├── getMepParser_xdeME1200_OSOutput.xsd (32 lines)
│   │   │   │   │   ├── mep_me1200.txt (13 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (32 lines)
│   │   │   │   └── getNameDetails/
│   │   │   │       ├── 163output.txt (184 lines)
│   │   │   │       ├── getNameDetails.par (51 lines)
│   │   │   │       ├── getNameDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getNameDetailsParser_xdeME1200_OS.rpl (188 lines)
│   │   │   │       ├── output.txt (260 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (20 lines)
│   │   │   ├── getEOAMDelayMeastSettings.xpa/
│   │   │   │   ├── getDM/
│   │   │   │   │   ├── DM.txt (136 lines)
│   │   │   │   │   ├── getDM.par (51 lines)
│   │   │   │   │   ├── getDMParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getDMParser_xdeME1200_OS.rpl (732 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (46 lines)
│   │   │   │   ├── getDMSettings/
│   │   │   │   │   ├── delaymeast.txt (31 lines)
│   │   │   │   │   ├── getDMSettings.par (52 lines)
│   │   │   │   │   ├── getDMSettingsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getDMSettingsParser_xdeME1200_OS.rpl (288 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (34 lines)
│   │   │   │   └── getDMTime/
│   │   │   │       ├── DMTimeoutput.txt (483 lines)
│   │   │   │       ├── getDMTime.par (51 lines)
│   │   │   │       ├── getDMTimeParser_xdeME1200_OS.rpl (131 lines)
│   │   │   │       ├── getDMTimeParser_xdeME1200_OSOutput.xsd (56 lines)
│   │   │   │       ├── newoutput.txt (483 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (56 lines)
│   │   │   ├── getEoamLossMeastSettings.xpa/
│   │   │   │   ├── getLM/
│   │   │   │   │   ├── getLM.par (53 lines)
│   │   │   │   │   ├── getLMParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getLMParser_xdeME1200_OS.rpl (106 lines)
│   │   │   │   │   ├── getLMParser_xdeME1200_OSOutput.xsd (27 lines)
│   │   │   │   │   ├── me1200.txt (264 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (27 lines)
│   │   │   │   ├── getLMSettings/
│   │   │   │   │   ├── getLMSettings.par (54 lines)
│   │   │   │   │   ├── getLMSettingsParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getLMSettingsParser_xdeME1200_OS.rpl (260 lines)
│   │   │   │   │   ├── getLMSettingsParser_xdeME1200_OSOutput.xsd (21 lines)
│   │   │   │   │   ├── lossmeast.txt (30 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (33 lines)
│   │   │   │   └── getLMTime/
│   │   │   │       ├── Time.txt (483 lines)
│   │   │   │       ├── getLMTime.par (53 lines)
│   │   │   │       ├── getLMTimeParserOutput.xsd (6 lines)
│   │   │   │       ├── getLMTimeParser_xdeME1200_OS.rpl (131 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (56 lines)
│   │   │   ├── getMepDetails_snmp/
│   │   │   │   ├── getMepDetails_snmp.map (72 lines)
│   │   │   │   ├── getMepDetails_snmp.par (54 lines)
│   │   │   │   ├── snmpOutput.xml (427 lines)
│   │   │   │   ├── snmpOutput1.xml (53 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (4388 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getSnmpMepDetails.xjs (69 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (853 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-hsrp-inventory/
│   │   │   ├── hsrp_cli.xpa/
│   │   │   │   ├── hsrp_Delay_IOS_cli/
│   │   │   │   │   ├── delayXE.txt (6 lines)
│   │   │   │   │   ├── hsrpPepVersion.ept (16 lines)
│   │   │   │   │   ├── hsrp_cli_IOS_delay.rpl (157 lines)
│   │   │   │   │   ├── hsrp_cli_XEdelay.par (65 lines)
│   │   │   │   │   └── xmp-im-router-redundancy-module.xsd (602 lines)
│   │   │   │   └── hsrp_cli/
│   │   │   │       ├── hsrpPepVersion.ept (16 lines)
│   │   │   │       ├── hsrp_cli.par (122 lines)
│   │   │   │       ├── hsrp_cli_IOS.rpl (437 lines)
│   │   │   │       ├── hsrp_cli_IOS_XR.rpl (755 lines)
│   │   │   │       ├── outputXE.txt (39 lines)
│   │   │   │       ├── outputXR.txt (60 lines)
│   │   │   │       └── xmp-im-router-redundancy-module.xsd (602 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xde-hsrp-inventory.xde (177 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-iosxe-SFP-inventory/
│   │   │   ├── SFP.xpa/
│   │   │   │   └── getSFP/
│   │   │   │       ├── getSFP.par (53 lines)
│   │   │   │       ├── getSFPParser_xdeIOS.rpl (147 lines)
│   │   │   │       ├── output.txt (55 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (21 lines)
│   │   │   ├── SFPParams.xpa/
│   │   │   │   └── getSFPParams/
│   │   │   │       ├── getSFPParams.par (27 lines)
│   │   │   │       ├── getSFPParamsParserOutput.xsd (6 lines)
│   │   │   │       ├── getSFPParamsParser_xdeIOS.rpl (345 lines)
│   │   │   │       ├── getSFPParamsParser_xdeIOSOutput.xsd (28 lines)
│   │   │   │       ├── sample_output.txt (202 lines)
│   │   │   │       └── xmp-im-physical-resource-module.xsd (890 lines)
│   │   │   ├── sensor/
│   │   │   │   ├── sensor.map (13 lines)
│   │   │   │   ├── sensor.par (62 lines)
│   │   │   │   ├── sensorOutput.xsd (51 lines)
│   │   │   │   └── xmp-im-sensor-module.xsd (242 lines)
│   │   │   ├── .project (30 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (120 lines)
│   │   │   └── xmpxde.xml (24 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l2vpn-pbb-evpn/
│   │   │   ├── cisco-getevpn.xpa/
│   │   │   │   └── getevpn/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (44 lines)
│   │   │   │       ├── getevpn.par (25 lines)
│   │   │   │       ├── getevpnParser_xdeIOS_XR.rpl (223 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   ├── cisco-getevpnbmacaddressentry.xpa/
│   │   │   │   └── evpnbmacaddressentry/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (32 lines)
│   │   │   │       ├── evpnbmacaddressentry.par (25 lines)
│   │   │   │       ├── evpnbmacaddressentryParser_xdeIOS_XR.rpl (140 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   ├── cisco-getevpnethsegmentpepsettings.xpa/
│   │   │   │   └── evpnethsegmentpepsettings/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (53 lines)
│   │   │   │       ├── getevpnethernetsegmentpepsettings.par (27 lines)
│   │   │   │       ├── getevpnethernetsegmentpepsettingsParser_xdeIOS_XR.rpl (447 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   ├── cisco-getexportbgproutetarget.xpa/
│   │   │   │   └── getexportbgproutetarget/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (44 lines)
│   │   │   │       ├── getexportbgproutetarget.par (25 lines)
│   │   │   │       ├── getexportbgproutetargetParser_xdeIOS_XR.rpl (106 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (424 lines)
│   │   │   ├── cisco-getimportbgproutetarget.xpa/
│   │   │   │   └── getimportbgproutetarget/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (44 lines)
│   │   │   │       ├── getimportbgproutetarget.par (25 lines)
│   │   │   │       ├── getimportbgproutetargetParser_xdeIOS_XR.rpl (106 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (424 lines)
│   │   │   ├── cisco-getpbbbbridgesettings.xpa/
│   │   │   │   ├── getpbbbbridgesettings/
│   │   │   │   │   ├── SampleDeviceOutputIOS_XR.txt (63 lines)
│   │   │   │   │   ├── getpbbbbridgesettings.par (25 lines)
│   │   │   │   │   ├── getpbbbbridgesettingsParser_xdeIOS_XR.rpl (118 lines)
│   │   │   │   │   └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   │   └── getpbbbridgeevpnid/
│   │   │   │       ├── getpbbbridgeevpnid.out.xml (0 lines)
│   │   │   │       ├── getpbbbridgeevpnid.par (29 lines)
│   │   │   │       ├── getpbbbridgeevpnidParser_xdeIOS_XR.rpl (72 lines)
│   │   │   │       ├── output.txt (7 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   ├── cisco-getpbbedgetocoredomain.xpa/
│   │   │   │   └── getpbbedgetocoredomain/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (68 lines)
│   │   │   │       ├── getpbbedgetocoredomain.par (27 lines)
│   │   │   │       ├── getpbbedgetocoredomainParser_xdeIOS_XR.rpl (42 lines)
│   │   │   │       └── getpbbedgetocoredomainParser_xdeIOS_XROutput.xsd (11 lines)
│   │   │   ├── cisco-getpbbibridgesettings.xpa/
│   │   │   │   └── getpbbibridgesettings/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (2456 lines)
│   │   │   │       ├── getpbbibridgesettings.par (25 lines)
│   │   │   │       ├── getpbbibridgesettingsParser_xdeIOS_XR.rpl (175 lines)
│   │   │   │       └── prime-carrier-ethernet-pbb-model.xsd (419 lines)
│   │   │   ├── test/
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_codeToedge_mapping.xft (72 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_evpn.xft (91 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_evpnBmacAddress.xft (55 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_evpnEthernetSettings.xft (211 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_evpnEthernetSettings_CSCur21385.xft (211 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_exportRouteTarget.xft.txt (91 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_importRouteTarget.xft.txt (91 lines)
│   │   │   │   ├── pbbevpn_ASR9001_XR_5.1.2_pbbBBridge.xft (121 lines)
│   │   │   │   └── pbbevpn_ASR9001_XR_5.1.2_pbbIBridge.xft (2149 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (93 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l3vpn-bgp-inventory/
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_bgp_getRouteDistribution.xpa/
│   │   │   │   └── getRouteDistribution/
│   │   │   │       ├── RouteDistribution_19.txt (30 lines)
│   │   │   │       ├── XEOutput.txt (23 lines)
│   │   │   │       ├── XROutput.txt (30 lines)
│   │   │   │       ├── distributeRouteTypesEnum.ept (46 lines)
│   │   │   │       ├── getRouteDistribution.par (113 lines)
│   │   │   │       ├── getRouteDistributionParser_xdeIOS.rpl (508 lines)
│   │   │   │       ├── getRouteDistributionParser_xdeIOS_XR.rpl (541 lines)
│   │   │   │       ├── output_asr903.txt (15 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_bgp_getRouteDistributionGi.xpa/
│   │   │   │   └── getRouteDistributionGi/
│   │   │   │       ├── RouteDistribution_19.txt (13 lines)
│   │   │   │       ├── distributeRouteTypesEnum.ept (46 lines)
│   │   │   │       ├── getRouteDistributionGi.par (113 lines)
│   │   │   │       ├── getRouteDistributionParser_xdeIOSGi.rpl (422 lines)
│   │   │   │       ├── getRouteDistributionParser_xdeIOS_XRGi.rpl (423 lines)
│   │   │   │       ├── output_asr903.txt (15 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_bgp_getaf_cli.xpa/
│   │   │   │   ├── getBgpAddressFamily/
│   │   │   │   │   ├── BgpAddressFamily_19.txt (40 lines)
│   │   │   │   │   ├── getBgpAddressFamily.par (155 lines)
│   │   │   │   │   ├── getBgpAddressFamilyParser_xdeIOS.rpl (119 lines)
│   │   │   │   │   ├── getBgpAddressFamilyParser_xdeIOS_XR.rpl (110 lines)
│   │   │   │   │   ├── getVrfParserOutput.xsd (20 lines)
│   │   │   │   │   ├── output_903.txt (6 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (3791 lines)
│   │   │   │   └── getBgpAddressFamilyVersion06/
│   │   │   │       ├── BgpAddressFamily_19.txt (40 lines)
│   │   │   │       ├── getBgpAddressFamilyParser_xdeIOS.rpl (119 lines)
│   │   │   │       ├── getBgpAddressFamilyParser_xdeIOS_XR.rpl (110 lines)
│   │   │   │       ├── getBgpAddressFamilyVersion06.par (155 lines)
│   │   │   │       ├── getVrfParserOutput.xsd (20 lines)
│   │   │   │       ├── output_903.txt (6 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (3791 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_bgp_getbgpneighbour_cli.xpa/
│   │   │   │   ├── getBgpNeighbourInfo_Cli/
│   │   │   │   │   ├── cliOutputIOSXR.txt (42 lines)
│   │   │   │   │   ├── cliOutputIOS_XR.txt (24 lines)
│   │   │   │   │   ├── cliOutput_XE.txt (28 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_Cli.par (112 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_CliParser_xdeIOS.rpl (262 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_CliParser_xdeIOS_XR.rpl (310 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (4079 lines)
│   │   │   │   └── getBgpNeighbourInfo_password_Cli/
│   │   │   │       ├── Password_XE (37 lines)
│   │   │   │       ├── Password_XR (21 lines)
│   │   │   │       ├── getBgpNeighbourInfo_password_Cli.par (114 lines)
│   │   │   │       ├── getBgpNeighbourInfo_password_CliParser_xdeIOS.rpl (202 lines)
│   │   │   │       ├── getBgpNeighbourInfo_password_CliParser_xdeIOS_XR.rpl (218 lines)
│   │   │   │       ├── output_asr903.txt (59 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_bgp_getvraf_ingress_egress.xpa/
│   │   │   │   └── getvraf_ingress_egress/
│   │   │   │       ├── RouteDistribution_19.txt (13 lines)
│   │   │   │       ├── getvraf_ingress_egress.par (65 lines)
│   │   │   │       ├── getvraf_ingress_egress.rpl (157 lines)
│   │   │   │       ├── output_asr903.txt (59 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_vrf_getvrfandvrfaf_cli.xpa/
│   │   │   │   └── getVrfAndNeighborAddressFamily/
│   │   │   │       ├── VrfAndNeighborAddressFamily_17.txt (160 lines)
│   │   │   │       ├── VrfAndNeighborAddressFamily_19.txt (69 lines)
│   │   │   │       ├── VrfAndNeighborAddressFamily_75.txt (239 lines)
│   │   │   │       ├── getVrfAndNeighborAddressFamily.par (127 lines)
│   │   │   │       ├── getVrfAndNeighborAddressFamilyParser_xdeIOS.rpl (444 lines)
│   │   │   │       ├── getVrfAndNeighborAddressFamilyParser_xdeIOS_XR.rpl (629 lines)
│   │   │   │       ├── localAsActionenumParseType-XR.ept (22 lines)
│   │   │   │       ├── localAsActionenumParseType.ept (28 lines)
│   │   │   │       ├── outputall_asr903.txt (171 lines)
│   │   │   │       ├── sample_asr903.txt (344 lines)
│   │   │   │       ├── sh_bgp_vrf_all_neighbors_detail.txt (125 lines)
│   │   │   │       ├── sh_bgp_vrf_all_summary.txt (56 lines)
│   │   │   │       ├── show_bgp_all_neighbors-IOS.txt (884 lines)
│   │   │   │       ├── show_bgp_vrf_all_neighbors_detail-IOS-XR.txt (173 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7084 lines)
│   │   │   ├── functionDefn/
│   │   │   │   └── yieldFuncion.xde (558 lines)
│   │   │   ├── test/
│   │   │   │   └── test.text (0 lines)
│   │   │   ├── tests/
│   │   │   │   └── testcases/
│   │   │   │       └── BGP/
│   │   │   │           ├── bgpInventory.xft (2366 lines)
│   │   │   │           ├── xftWithBgpNeighborInfo.xft (2021 lines)
│   │   │   │           └── xftWithBgpVrfSettings.xft (1183 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xde-l3vpn-bgp-inventory.xde (74 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l3vpn-mpbgp-inventory/
│   │   │   ├── cisco_iosxe_l3vpn_mpbgp_getAFxml.xpa/
│   │   │   │   └── bgpAF_XR/
│   │   │   │       ├── bgpAF_XR.par (99 lines)
│   │   │   │       ├── bgpAF_XRParserOutput.xsd (6 lines)
│   │   │   │       ├── bgpAF_XRParser_xdeIOS_XR.rpl (10094 lines)
│   │   │   │       ├── bgpAF_XRParser_xdeIOS_XROutput.xsd (100 lines)
│   │   │   │       ├── bgp_xr_run_config.txt (46 lines)
│   │   │   │       ├── lebeled_unicast.txt (75 lines)
│   │   │   │       ├── sho_run_9k.txt (1988 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7528 lines)
│   │   │   ├── cisco_iosxe_l3vpn_mpbgp_getbgplinkinfo.xpa/
│   │   │   │   └── getBgpLinkDetails/
│   │   │   │       ├── getBgpLinkDetails.par (103 lines)
│   │   │   │       ├── getBgpLinkDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getBgpLinkDetailsParser_xdeIOS.rpl (97 lines)
│   │   │   │       ├── getBgpLinkDetailsParser_xdeIOS_XR.rpl (111 lines)
│   │   │   │       ├── output.txt (7 lines)
│   │   │   │       ├── output1.txt (29 lines)
│   │   │   │       ├── output127.txt (6 lines)
│   │   │   │       ├── output85.txt (6 lines)
│   │   │   │       ├── output_linkstatus.txt (16 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (6011 lines)
│   │   │   ├── cisco_iosxe_l3vpn_mpbgp_getbgprunconfig.xpa/
│   │   │   │   ├── 10.104.120.85.txt (57 lines)
│   │   │   │   ├── 10.104.120.85_1.txt (61 lines)
│   │   │   │   ├── 167.txt (205 lines)
│   │   │   │   ├── 167_1.txt (184 lines)
│   │   │   │   ├── 167_granular (16 lines)
│   │   │   │   ├── 85.txt (63 lines)
│   │   │   │   ├── getBgpAFandNAF.par (55 lines)
│   │   │   │   ├── getBgpAFandNAFParser_xdeIOSOutput.xsd (48 lines)
│   │   │   │   ├── getBgpAFandNAF_xdeIOS.rpl (4056 lines)
│   │   │   │   ├── ipv6_mask.output.txt (32 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (7528 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_mpbgp_getmpbgpneighbour_snmp_cli.xpa/
│   │   │   │   ├── getBgpNeighbourInfo_Cli/
│   │   │   │   │   ├── LocalAsDeviceoutput.txt (21 lines)
│   │   │   │   │   ├── LocalAsxr.txt (22 lines)
│   │   │   │   │   ├── cliOutputIosIos.txt (12 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (12 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_Cli.par (125 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_CliParser_xdeIOS.rpl (286 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_CliParser_xdeIOS_XR.rpl (201 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (26 lines)
│   │   │   │   └── getBgpNeighbourInfo_Snmp/
│   │   │   │       ├── BgpNeighbourInfoSnmp.map (47 lines)
│   │   │   │       ├── getBgpNeighbourInfo_Snmp.par (69 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (3462 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_mpbgp_getmpbgpneighbourstateinfo_snmp.xpa/
│   │   │   │   └── getBgpNeighbourStateInfo/
│   │   │   │       ├── BgpNeighbourStateInfoSnmp.map (16 lines)
│   │   │   │       ├── getBgpNeighbourStateInfo.par (31 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (3347 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_mpbgp_getmpbgpneighbourstateinfo_snmp_cli.xpa/
│   │   │   │   ├── getBgpNeighborStateInfo_Cli_Ipv6/
│   │   │   │   │   ├── getBgpNeighborStateInfo_Cli_Ipv6.par (66 lines)
│   │   │   │   │   ├── getBgpNeighborStateInfo_Cli_Ipv6ParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getBgpNeighborStateInfo_Cli_Ipv6Parser_xdeIOS.rpl (90 lines)
│   │   │   │   │   ├── ipv6_output.txt (3 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (3457 lines)
│   │   │   │   ├── getBgpNeighborStateInfo_Snmp_new/
│   │   │   │   │   ├── getBgpNeighborStateInfo_Snmp_new.par (61 lines)
│   │   │   │   │   └── getBgpNeighborStateInfo_Snmp_newOutput.xsd (33 lines)
│   │   │   │   ├── getBgpNeighbourStateInfo_Cli/
│   │   │   │   │   ├── cliOutputIosIos.txt (4 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (8 lines)
│   │   │   │   │   ├── getBgpNeighStInfo_CliParser_IOS.rpl (90 lines)
│   │   │   │   │   ├── getBgpNeighStInfo_CliParser_IOS_XR.rpl (90 lines)
│   │   │   │   │   ├── getBgpNeighbourInfo_Cli.par (122 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (3457 lines)
│   │   │   │   └── getBgpNeighbourStateInfo_Snmp/
│   │   │   │       ├── BgpNeighbourStateInfoSnmp.map (16 lines)
│   │   │   │       ├── getBgpNeighbourStateInfo.par (31 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (3457 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_mpbgp_getmpbgpprocesssettings_snmp.xpa/
│   │   │   │   └── getBgpProcessSettings/
│   │   │   │       ├── BgpProcessSettingsSnmp.map (15 lines)
│   │   │   │       ├── getBgpProcessSettings.par (24 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (3457 lines)
│   │   │   ├── tests/
│   │   │   │   └── testcases/
│   │   │   │       ├── IOS-XE/
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfo_CliParser_IPV4_AddressFamily.xft (52 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfo_CliParser_IPV6_AddressFamily.xft (35 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfo_CliParser_LocalAS.xft (35 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_AdvertisementInterval.xft (94 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_BGPNeighborInventory.xft (91 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_BGPNeighbor_shutdown.xft (94 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_HoldTime.xft (91 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_KeepAlive.xft (91 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourInfosnmp_RemoteAS.xft (91 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourStateInfo_AdminStatus.xft (29 lines)
│   │   │   │       │   ├── eBGP_ME3600_15OS_getBgpNeighbourStateInfo_BGPConnectionState.xft (59 lines)
│   │   │   │       │   └── eBGP_ME3600_15OS_getBgpNeighbourStateInfo_BGPNeighborStateInfoInventory.xft (29 lines)
│   │   │   │       └── IOS-XR/
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfo_CliParser_IPV4_AddressFamily.xft (62 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfo_CliParser_IPV6_AddressFamily.xft (61 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_AdvertisementInterval.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_BGPNeighborInventory.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_BGPNeighbor_shutdown.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_HoldTime.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_KeepAlive.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourInfosnmp_RemoteAS.xft (160 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourStateInfo_AdminStatus.xft (39 lines)
│   │   │   │           ├── eBGP_ASR9006_520XR_getBgpNeighbourStateInfo_BGPConnectionstate.xft (59 lines)
│   │   │   │           └── eBGP_ASR9006_520XR_getBgpNeighbourStateInfo_BGPNeighborStateInfoInventory.xft (39 lines)
│   │   │   ├── xJsFunctions/
│   │   │   │   ├── getBgpAdditionalPaths.xjs (59 lines)
│   │   │   │   ├── getBgpAfSettings.xjs (58 lines)
│   │   │   │   ├── getBgpNeighAFJsFunc.xjs (170 lines)
│   │   │   │   ├── getBgpNeighInfoJsFunc.xjs (86 lines)
│   │   │   │   └── getBgpNetworkSettings.xjs (88 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (1259 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l3vpn-ospf-inventory/
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_ospf_cli.xpa/
│   │   │   │   └── cisco_iosxr_iosxe_l3vpn_ospf_cli/
│   │   │   │       ├── IOS_XR_Router_Ospf_config.txt (41 lines)
│   │   │   │       ├── XR-show_run_router_ospf_445566_vrf_VrfName.txt (16 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_cli.par (129 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_cliParserOutput.xsd (6 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_cliParser_xdeIOS.rpl (569 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_cliParser_xdeIOS_XR.rpl (899 lines)
│   │   │   │       ├── ospf_ios_xe.txt (9 lines)
│   │   │   │       ├── sh_ip_ospf_interface_xe.txt (12 lines)
│   │   │   │       ├── sh_running_config_router_ospf_xr.txt (60 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (8786 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceName_cli.xpa/
│   │   │   │   └── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCli/
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCli.par (110 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCliParserOutput.xsd (6 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCliParser_xdeIOS.rpl (113 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCliParser_xdeIOSOutput.xsd (21 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_interfaceNameCliParser_xdeIOS_XR.rpl (3 lines)
│   │   │   │       └── sh_ip_ospf_interface_xe.txt (12 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_ospfv3_cli.xpa/
│   │   │   │   └── cisco_iosxr_iosxe_l3vpn_ospfv3_cli/
│   │   │   │       ├── IOS_router_ospfv3_withAuth.txt (79 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospf_cliParserOutput.xsd (6 lines)
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospfv3_cli.par (131 lines)
│   │   │   │       ├── l3vpn_ospfv3_cliParser_xdeIOS_XR.rpl (909 lines)
│   │   │   │       ├── l3vpn_ospfv3_cliParser_xde_IOS.rpl (845 lines)
│   │   │   │       ├── sh_ip_ospf_interface_xe.txt (12 lines)
│   │   │   │       ├── sh_ospfv3_vrf_IOS.txt (73 lines)
│   │   │   │       ├── sh_running_config_router_ospf_xr.txt (23 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7655 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_ospfv3_interfaceName_cli.xpa/
│   │   │   │   └── cisco_iosxr_iosxe_l3vpn_ospfv3_interfaceNameCli/
│   │   │   │       ├── cisco_iosxr_iosxe_l3vpn_ospfv3_interfaceNameCli.par (110 lines)
│   │   │   │       ├── l3vpn_ospfv3_interfaceNameCliParserOutput.xsd (6 lines)
│   │   │   │       ├── l3vpn_ospfv3_interfaceNameCliParser_xdeIOS.rpl (113 lines)
│   │   │   │       ├── l3vpn_ospfv3_interfaceNameCliParser_xdeIOS_XR.rpl (3 lines)
│   │   │   │       └── sh_ip_ospf_interface_xe.txt (17 lines)
│   │   │   ├── functn/
│   │   │   │   └── l3vpnOspfInventoryCollector.xde (265 lines)
│   │   │   ├── getBfdXeCli.xpa/
│   │   │   │   └── getBfdXeCli/
│   │   │   │       ├── XE.txt (13 lines)
│   │   │   │       ├── getBfdXe.rpl (129 lines)
│   │   │   │       ├── getBfdXeCli.par (59 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (23 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xde-l3vpn-ospf-inventory.xde (78 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l3vpn-routepolicy-inventory/
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_vrf_getRoutePolicyMapEntry_cli.xpa/
│   │   │   │   └── getRoutePolicyMapEntry/
│   │   │   │       ├── XE.txt (9 lines)
│   │   │   │       ├── XR.txt (103 lines)
│   │   │   │       ├── getRoutePolicyMapEntry.par (121 lines)
│   │   │   │       ├── getRoutePolicyMapEntryIOS.rpl (117 lines)
│   │   │   │       ├── getRoutePolicyMapEntryIOS_XR.rpl (136 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (25 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_vrf_getRoutePolicySetExtComEntry_cli.xpa/
│   │   │   │   └── getRoutePolicySetExtComEntry/
│   │   │   │       ├── XE.txt (9 lines)
│   │   │   │       ├── XR.txt (38 lines)
│   │   │   │       ├── getRoutePolicySetExtComEntry.par (121 lines)
│   │   │   │       ├── getRoutePolicySetExtComEntry.rpl (105 lines)
│   │   │   │       ├── getRoutePolicySetExtComEntryIOS_XE.rpl (124 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (20 lines)
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_vrf_getRoutePolicy_cli.xpa/
│   │   │   │   └── getRoutePolicy/
│   │   │   │       ├── XRGI.txt (2 lines)
│   │   │   │       ├── XRNormalInv.txt (20 lines)
│   │   │   │       ├── asr903.txt (9 lines)
│   │   │   │       ├── asr903GI.txt (4 lines)
│   │   │   │       ├── getRoutePolicy.par (121 lines)
│   │   │   │       ├── getRoutePolicyParser_xdeIOS.rpl (52 lines)
│   │   │   │       ├── getRoutePolicyParser_xdeIOS_XR.rpl (105 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (8054 lines)
│   │   │   ├── function/
│   │   │   │   ├── routeMapSetAction.xde (82 lines)
│   │   │   │   └── routePolicySeq.xde (66 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xde_l3vpn_routepolicy_inventory.xde (271 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde-l3vpn-vrf-inventory/
│   │   │   ├── cisco_iosxr_iosxe_l3vpn_vrf_getvrfandvrfaf_cli.xpa/
│   │   │   │   └── getVrfAndVrfAddressFamily/
│   │   │   │       ├── IOSXR_TOTAL.txt (328 lines)
│   │   │   │       ├── associateVRFAndVPNID.xslt (87 lines)
│   │   │   │       ├── getVrfAndVrfAddressFamily.par (149 lines)
│   │   │   │       ├── getVrfAndVrfAddressFamilyParser_xdeIOS.rpl (1263 lines)
│   │   │   │       ├── getVrfAndVrfAddressFamilyParser_xdeIOS_XR.rpl (1282 lines)
│   │   │   │       ├── outputIOS_10_126_165_20.txt (84 lines)
│   │   │   │       ├── output_IOS_10_104_120_37.txt (18 lines)
│   │   │   │       ├── output_IOS_ASR903_10_126_165_24.txt (122 lines)
│   │   │   │       ├── output_XR_17.txt (159 lines)
│   │   │   │       ├── output_asr903.txt (741 lines)
│   │   │   │       ├── output_show_vrf_all_18.txt (513 lines)
│   │   │   │       ├── removeDuplicateForwardingDownstream.xslt (24 lines)
│   │   │   │       ├── removeEmptyTags.xslt (18 lines)
│   │   │   │       ├── show_running_config_XR.txt (62 lines)
│   │   │   │       ├── show_running_config_rd_xr.txt (17 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v1.txt (39 lines)
│   │   │   │       ├── showvrfdetail-output-106-XR52-v2.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v2.txt (122 lines)
│   │   │   │       ├── showvrfdetail-output-17-XR52-v3.txt (159 lines)
│   │   │   │       ├── showvrfdetail-output-17.XR52.txt (54 lines)
│   │   │   │       ├── showvrfdetail-output-173-ASR903-15.4.2S.txt (67 lines)
│   │   │   │       ├── showvrfdetail-output-178-ASR903-15.3.3S3.txt (196 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S-v2.txt (49 lines)
│   │   │   │       ├── showvrfdetail-output-20-ME3600x-15.3.3S.txt (47 lines)
│   │   │   │       ├── showvrfdetail-output-24-ASR903-15.4.3.S.txt (122 lines)
│   │   │   │       ├── testcaseIOS.txt (96 lines)
│   │   │   │       ├── xmp-im-vrf-module.out.xml (0 lines)
│   │   │   │       └── xmp-im-vrf-module.xsd (112 lines)
│   │   │   ├── test/
│   │   │   │   └── test.text (0 lines)
│   │   │   ├── tests/
│   │   │   │   └── testcases/
│   │   │   │       ├── PWHE-VRF/
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_AddFamilyIPV4Parameters.xft (415 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_AddFamilyIPV6Parameters.xft (543 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_AddfamilyIPV4RT.xft (495 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_AddfamilyIPV6RT.xft (543 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_ChangeRD.xft (443 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_ChangeVPNID.xft (443 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_Description.xft (443 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_Interfaces.xft (415 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_Inventory.xft (415 lines)
│   │   │   │       │   ├── PWHE-VRF_ASR9006_XR520_RDformats.xft (543 lines)
│   │   │   │       │   └── PWHE-VRF_ASR9006_XR520_VPNID.xft (443 lines)
│   │   │   │       └── VRF/
│   │   │   │           ├── VRF_ASR9006_XR520_AddFamilyIPV4Parameters.xft (415 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_AddFamilyIPV6Parameters.xft (543 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_AddfamilyIPV4RT.xft (495 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_AddfamilyIPV6RT.xft (543 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_ChangeRD.xft (443 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_ChangeVPNID.xft (443 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_Interfaces.xft (415 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_Inventory.xft (415 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_RDformats.xft (543 lines)
│   │   │   │           ├── VRF_ASR9006_XR520_VPNID.xft (475 lines)
│   │   │   │           ├── l3vpn_vrf_ASR9006_XR_165.17_Action_RouteTarget_ExportsOnly.xft (694 lines)
│   │   │   │           ├── l3vpn_vrf_ASR9006_XR_165.17_Action_RouteTarget_ImportsOnly.xft (370 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_Action_RouteTarget_ExportsOnly.xft (475 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_Action_RouteTarget_ImportsOnly.xft (476 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_IPv4AddressFamily.xft (423 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_IPv6AddressFamily.xft (345 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_for_description_with_RouteDistinguisher_tag.xft (550 lines)
│   │   │   │           ├── l3vpn_vrf_ASR903_XE_165.24_for_description_with_VPNID_tag.xft (550 lines)
│   │   │   │           └── l3vpn_vrf_ASR903_XE_165.24_for_description_with_VRF_tag.xft (549 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xde-l3vpn-vrf-inventory.xde (61 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.prime.inventory.xde.xde_MPLS_TE_FRR_Inventory/
│   │   │   ├── AutoBW.xpa/
│   │   │   │   └── getAutoBw/
│   │   │   │       ├── Output2 (33 lines)
│   │   │   │       ├── getAutoBw.par (53 lines)
│   │   │   │       ├── getAutoBwParser_xdeIOS.rpl (468 lines)
│   │   │   │       ├── output.txt (35 lines)
│   │   │   │       ├── output1.txt (28 lines)
│   │   │   │       └── xmp-im-mpls-te-module.xsd (26 lines)
│   │   │   ├── AutoBackUpTunnel.xpa/
│   │   │   │   └── getAutoBackupTunnel/
│   │   │   │       ├── getAutoBackupTunnel.par (55 lines)
│   │   │   │       ├── getAutoBackupTunnelParser_xdeIOS.rpl (128 lines)
│   │   │   │       ├── output.txt (12 lines)
│   │   │   │       └── xmp-im-mpls-te-module.xsd (21 lines)
│   │   │   ├── AutoBkupTunnelBWForXR.xpa/
│   │   │   │   └── getAutoBkupTunnelAndBwForXr/
│   │   │   │       ├── getAutoBkupTunnelAndBwForXr.par (62 lines)
│   │   │   │       ├── getAutoBkupTunnelAndBwForXrParserOutput.xsd (6 lines)
│   │   │   │       ├── getAutoBkupTunnelAndBwForXrParser_xdeIOS_XR.rpl (494 lines)
│   │   │   │       ├── output1.txt (77 lines)
│   │   │   │       ├── output2.txt (77 lines)
│   │   │   │       └── xmp-im-mpls-te-module.xsd (30 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (97 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.prime.xde.ipinterworking-inventory/
│   │   │   ├── getPWPep/
│   │   │   │   ├── cliOutput.txt (49 lines)
│   │   │   │   ├── getPWPep.par (73 lines)
│   │   │   │   ├── getPWPepParserOutput.xsd (6 lines)
│   │   │   │   ├── getPWPepParser_xdeIOS.rpl (266 lines)
│   │   │   │   ├── getPWPepParser_xdeIOSOutput.xsd (25 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (25 lines)
│   │   │   ├── getPWSegmentEndPointSettings/
│   │   │   │   ├── cliOutput.txt (110 lines)
│   │   │   │   ├── getPWSegmentEndPointSettings.par (53 lines)
│   │   │   │   ├── getPWSegmentEndPointSettingsParserOutput.xsd (6 lines)
│   │   │   │   ├── getPWSegmentEndPointSettingsParser_xdeIOS.rpl (96 lines)
│   │   │   │   ├── getPWSegmentEndPointSettingsParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   └── prime-resource-model.xsd (19 lines)
│   │   │   ├── getSerialEncapsulation/
│   │   │   │   ├── cliOutput.txt (509 lines)
│   │   │   │   ├── getSerialEncapsulation.par (53 lines)
│   │   │   │   ├── getSerialEncapsulationParserOutput.xsd (6 lines)
│   │   │   │   ├── getSerialEncapsulationParser_xdeIOS.rpl (174 lines)
│   │   │   │   ├── getSerialEncapsulationParser_xdeIOSOutput.xsd (18 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (21 lines)
│   │   │   ├── getSerialP2PForwarder/
│   │   │   │   ├── cliOutput.txt (49 lines)
│   │   │   │   ├── getSerialP2PForwarder.par (74 lines)
│   │   │   │   ├── getSerialP2PForwarderParserOutput.xsd (37 lines)
│   │   │   │   ├── getSerialP2PForwarderParser_xdeIOS.rpl (430 lines)
│   │   │   │   ├── getSerialP2PForwarderParser_xdeIOSOutput.xsd (37 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (37 lines)
│   │   │   ├── ipinterworking/
│   │   │   │   ├── cliOutput.txt (6 lines)
│   │   │   │   ├── ipinterworking.par (63 lines)
│   │   │   │   ├── ipinterworkingParserOutput.xsd (6 lines)
│   │   │   │   ├── ipinterworkingParser_xdeIOS.rpl (48 lines)
│   │   │   │   ├── ipinterworkingParser_xdeIOSOutput.xsd (24 lines)
│   │   │   │   └── prime-serial-resource-model.xsd (932 lines)
│   │   │   ├── .project (17 lines)
│   │   │   ├── getSerialPep.xjs (67 lines)
│   │   │   ├── getSerialPepConcatName.xjs (28 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (576 lines)
│   │   │   └── xmpxde.xml (24 lines)
│   │   ├── com.cisco.xmp.config.xde.ethernet-oam-cfm-domain/
│   │   │   ├── ethernet-oam-cfm-domain.xpa/
│   │   │   │   ├── cfmDomainCreateAndUpdateWriter/
│   │   │   │   │   ├── cfmDomainCreateAndUpdateWriter.par (38 lines)
│   │   │   │   │   ├── ios.vtl (127 lines)
│   │   │   │   │   ├── iosasr901.vtl (173 lines)
│   │   │   │   │   └── iosxr.vtl (91 lines)
│   │   │   │   ├── cfmDomainDeleteWriter/
│   │   │   │   │   ├── cfmDomainDeleteWriter.par (28 lines)
│   │   │   │   │   ├── ios.vtl (105 lines)
│   │   │   │   │   └── iosxr.vtl (65 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── ios/
│   │   │   │   │   │   ├── create/
│   │   │   │   │   │   │   ├── CreateAllCommands.xft (138 lines)
│   │   │   │   │   │   │   ├── CreateMultipleMp-Id.xft (138 lines)
│   │   │   │   │   │   │   ├── CreateMultipleServiceTest.xft (138 lines)
│   │   │   │   │   │   │   └── CreateSingleDomain.xft (32 lines)
│   │   │   │   │   │   └── delete/
│   │   │   │   │   │       ├── DeleteDomainTest.xft (32 lines)
│   │   │   │   │   │       ├── DeleteMp-idTest.xft (274 lines)
│   │   │   │   │   │       └── DeleteService.xft (67 lines)
│   │   │   │   │   └── iosxr/
│   │   │   │   │       ├── create/
│   │   │   │   │       │   ├── CreateAllCommands.xft (135 lines)
│   │   │   │   │       │   ├── CreateMultipleMp-Id.xft (135 lines)
│   │   │   │   │       │   ├── CreateMultipleServiceTest.xft (70 lines)
│   │   │   │   │       │   └── CreateSingleDomain.xft (31 lines)
│   │   │   │   │       └── delete/
│   │   │   │   │           ├── DeleteDomainTest.xft (61 lines)
│   │   │   │   │           ├── DeleteMp-idTest.xft (282 lines)
│   │   │   │   │           └── DeleteService.xft (70 lines)
│   │   │   │   └── xmp-im-ethernet-oam-module.xsd (2730 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── cfmDomainCreateProcedure.xde (11 lines)
│   │   │   ├── cfmDomainDeleteProcedure.xde (11 lines)
│   │   │   ├── cfmDomainUpdateProcedure.xde (209 lines)
│   │   │   ├── error.xml (8 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (30 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.ipsla-twamp-light-config/
│   │   │   ├── IpSlaTwampLight.xpa/
│   │   │   │   ├── iosXrTest/
│   │   │   │   │   ├── CreateSession_Timeout_functionTest.xft (46 lines)
│   │   │   │   │   ├── DeleteSession_functionTest.xft (40 lines)
│   │   │   │   │   └── createSession_functionTest.xft (45 lines)
│   │   │   │   ├── twampLightCreateAndUpdateWriter/
│   │   │   │   │   ├── twampLightCreateAndUpdateWriter.par (71 lines)
│   │   │   │   │   ├── twampLightCreateIOS.vtl (1 lines)
│   │   │   │   │   └── twampLightCreateIOSXR.vtl (22 lines)
│   │   │   │   └── twampLightDeleteWriter/
│   │   │   │       ├── twampLightDeleteIOS.vtl (1 lines)
│   │   │   │       ├── twampLightDeleteIOSXR.vtl (6 lines)
│   │   │   │       └── twampLightDeleteWriter.par (71 lines)
│   │   │   ├── .project (30 lines)
│   │   │   ├── error.xml (4 lines)
│   │   │   ├── ipslaTwampLightCreateProcedure.xde (21 lines)
│   │   │   ├── ipslaTwampLightDeleteProcedure.xde (19 lines)
│   │   │   ├── ipslaTwampLightUpdateProcedure.xde (50 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.l3link-ospf-config/
│   │   │   ├── ospf-config-XE.xpa/
│   │   │   │   ├── ospfCreateAndUpdateWriter_XE/
│   │   │   │   │   ├── createospfIOSXE.vtl (149 lines)
│   │   │   │   │   └── ospfCreateAndUpdateWriter_XE.par (42 lines)
│   │   │   │   ├── ospfDeleteWriter_XE/
│   │   │   │   │   ├── deleteospfIOSXE.vtl (0 lines)
│   │   │   │   │   └── ospfDeleteWriter_XE.par (18 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (4302 lines)
│   │   │   ├── ospf-config.xpa/
│   │   │   │   ├── ospfCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXR.vtl (140 lines)
│   │   │   │   │   └── ospfCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── ospfDeleteWriter/
│   │   │   │   │   ├── iosXR.vtl (0 lines)
│   │   │   │   │   └── ospfDeleteWriter.par (28 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (4302 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getDeviceType.xde (28 lines)
│   │   │   ├── ospfCreateProcedure.xde (34 lines)
│   │   │   ├── ospfDeleteProcedure.xde (34 lines)
│   │   │   ├── ospfUpdateProcedure.xde (48 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── trim_procedure.xde (35 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.xmp.config.xde.l3vpn-ip-pep/
│   │   │   ├── l3vpn-ip-pep.xpa/
│   │   │   │   ├── l3vpn-ip-pepCreateWriter/
│   │   │   │   │   ├── iosXR.vtl (23 lines)
│   │   │   │   │   └── l3vpn-ip-pepCreateWriter.par (19 lines)
│   │   │   │   ├── l3vpn_ip_pepDeleteWriter/
│   │   │   │   │   ├── iosXR.vtl (24 lines)
│   │   │   │   │   └── l3vpn_ip_pepDeleteWriter.par (19 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── createl3vpn-ip-pepProcessSettings.xft (52 lines)
│   │   │   │   │       └── deletel3vpn-ip-pepProcessSettings.xft (49 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── l3vpn-ip-pepCreateProcedure.xde (14 lines)
│   │   │   ├── l3vpn-ip-pepDeleteProcedure.xde (14 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.l3vpn-mpbgp-config/
│   │   │   ├── l3vpn-mpbgp-config.xpa/
│   │   │   │   ├── l3vpnMpbgpCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (419 lines)
│   │   │   │   │   ├── iosXR.vtl (443 lines)
│   │   │   │   │   └── l3vpnMpbgpCreateAndUpdateWriter.par (74 lines)
│   │   │   │   ├── l3vpnMpbgpDeleteWriter/
│   │   │   │   │   ├── ios.vtl (75 lines)
│   │   │   │   │   ├── iosXR.vtl (19 lines)
│   │   │   │   │   └── l3vpnMpbgpDeleteWriter.par (28 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── iosXE/
│   │   │   │   │   │   ├── createBgpNeighborInfo1.xft (94 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo2.xft (149 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo3.xft (203 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo4.xft (85 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo5.xft (140 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo6.xft (87 lines)
│   │   │   │   │   │   ├── createBgpNeighborInfo7.xft (92 lines)
│   │   │   │   │   │   ├── createBgpProcessSettings.xft (42 lines)
│   │   │   │   │   │   ├── deleteBgpNeighborInfo.xft (145 lines)
│   │   │   │   │   │   ├── deleteBgpProcessSettings.xft (40 lines)
│   │   │   │   │   │   ├── updateBgpNeighborInfo.xft (123 lines)
│   │   │   │   │   │   ├── updateBgpNeighborInfo1.xft (121 lines)
│   │   │   │   │   │   └── updateBgpProcessSettings.xft (62 lines)
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── CSCvo44109_BgpNetworkMask_with_NetworkRoutePolicyName.xft (577 lines)
│   │   │   │   │       ├── CSCvo44109_BgpNetworkMask_without_NetworkRoutePolicyName.xft (575 lines)
│   │   │   │   │       ├── createBgpNeighborInfo1.xft (94 lines)
│   │   │   │   │       ├── createBgpNeighborInfo2.xft (148 lines)
│   │   │   │   │       ├── createBgpNeighborInfo3.xft (202 lines)
│   │   │   │   │       ├── createBgpNeighborInfo4.xft (86 lines)
│   │   │   │   │       ├── createBgpProcessSettings.xft (43 lines)
│   │   │   │   │       ├── deleteBgpNeighborInfo.xft (148 lines)
│   │   │   │   │       ├── deleteBgpProcessSettings.xft (39 lines)
│   │   │   │   │       ├── updateBgpNeighborInfo.xft (123 lines)
│   │   │   │   │       └── updateBgpProcessSettings.xft (64 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── excludeAssociations.xml (21 lines)
│   │   │   ├── l3vpnMpbgpCreateProcedure.xde (115 lines)
│   │   │   ├── l3vpnMpbgpDeleteProcedure.xde (16 lines)
│   │   │   ├── l3vpnMpbgpUpdateProcedure.xde (201 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (30 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.l3vpn-qos-applyQosPolicy/
│   │   │   ├── xmp-im-policy-applications-module-applyQosPolicy.xpa/
│   │   │   │   ├── applyQosPolicyCreateAndUpdateWriter/
│   │   │   │   │   ├── applyQosPolicyCreateAndUpdateWriter.par (28 lines)
│   │   │   │   │   ├── ios.vtl (53 lines)
│   │   │   │   │   └── iosxr.vtl (24 lines)
│   │   │   │   ├── applyQosPolicyDeleteWriter/
│   │   │   │   │   ├── applyQosPolicyDeleteWriter.par (28 lines)
│   │   │   │   │   ├── ios.vtl (52 lines)
│   │   │   │   │   └── iosxr.vtl (22 lines)
│   │   │   │   ├── xmp-im-policy-applications-module.xml (36 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1482 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── applyQosPolicyCreateProcedure.xde (17 lines)
│   │   │   ├── applyQosPolicyDeleteProcedure.xde (11 lines)
│   │   │   ├── applyQosPolicyUpdateProcedure.xde (28 lines)
│   │   │   ├── excludeAssociations.xml (24 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.mef-qos-applyQosPolicy/
│   │   │   ├── xmp-im-policy-applications-module-applyQosPolicy.xpa/
│   │   │   │   ├── applyQosPolicyCreateAndUpdateWriter/
│   │   │   │   │   ├── ME1200.vtl (263 lines)
│   │   │   │   │   ├── applyQosPolicyCreateAndUpdateWriter.par (38 lines)
│   │   │   │   │   ├── ios.vtl (63 lines)
│   │   │   │   │   └── iosxr.vtl (29 lines)
│   │   │   │   ├── applyQosPolicyDeleteWriter/
│   │   │   │   │   ├── ME1200.vtl (66 lines)
│   │   │   │   │   ├── applyQosPolicyDeleteWriter.par (37 lines)
│   │   │   │   │   ├── ios.vtl (63 lines)
│   │   │   │   │   └── iosxr.vtl (28 lines)
│   │   │   │   ├── test/
│   │   │   │   │   ├── me1200/
│   │   │   │   │   │   ├── me1200-QoS_multi-QoS-PortLevel.xft (1593 lines)
│   │   │   │   │   │   ├── me1200-QoS_policerAction-Cir-KBPS.xft (193 lines)
│   │   │   │   │   │   └── me1200-QoS_policerAction-Cir-MBPS.xft (193 lines)
│   │   │   │   │   ├── Activate_ApplyQosPolicy_default_NMS.xft (48 lines)
│   │   │   │   │   ├── Activate_ApplyQosPolicy_default_NMS_Service_Instance.xft (50 lines)
│   │   │   │   │   └── Activate_ApplyQosPolicy_default_NMS_XR.xft (49 lines)
│   │   │   │   ├── xmp-im-policy-applications-module.xml (36 lines)
│   │   │   │   └── xmp-im-policy-applications-module.xsd (1482 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── applyQosPolicyCreateProcedure.xde (11 lines)
│   │   │   ├── applyQosPolicyDeleteProcedure.xde (11 lines)
│   │   │   ├── applyQosPolicyUpdateProcedure.xde (28 lines)
│   │   │   ├── error.xml (24 lines)
│   │   │   ├── excludeAssociations.xml (25 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.mef-qos-classMap/
│   │   │   ├── mef-qos-classMap.xpa/
│   │   │   │   ├── classMapCreateAndUpdateWriter/
│   │   │   │   │   ├── ME1200.vtl (0 lines)
│   │   │   │   │   ├── classMapCreateAndUpdateWriter.par (48 lines)
│   │   │   │   │   ├── ios.vtl (165 lines)
│   │   │   │   │   └── iosxr.vtl (117 lines)
│   │   │   │   ├── classMapDeleteWriter/
│   │   │   │   │   ├── ME1200.vtl (0 lines)
│   │   │   │   │   ├── classMapDeleteWriter.par (37 lines)
│   │   │   │   │   ├── ios.vtl (6 lines)
│   │   │   │   │   └── iosxr.vtl (6 lines)
│   │   │   │   ├── test/
│   │   │   │   │   ├── XFTUpdateProcedure/
│   │   │   │   │   │   ├── ClassMapDescriptionTest.xft (55 lines)
│   │   │   │   │   │   ├── UpdateAllClassCondition.xft (152 lines)
│   │   │   │   │   │   ├── UpdateCascadeCondition.xft (58 lines)
│   │   │   │   │   │   ├── UpdateClassName.xft (60 lines)
│   │   │   │   │   │   ├── UpdateCosValue.xft (114 lines)
│   │   │   │   │   │   ├── UpdateDeiValue.xft (81 lines)
│   │   │   │   │   │   ├── UpdateDscpValue.xft (85 lines)
│   │   │   │   │   │   ├── UpdateInnerCosValue.xft (115 lines)
│   │   │   │   │   │   ├── UpdatePrecedenceValue.xft (82 lines)
│   │   │   │   │   │   ├── UpdateProcedureACLTest.xft (63 lines)
│   │   │   │   │   │   ├── UpdateProcedureIOSACLTest.xft (62 lines)
│   │   │   │   │   │   ├── UpdateVLanCondition.xft (87 lines)
│   │   │   │   │   │   └── UpdateipDscpValue.xft (85 lines)
│   │   │   │   │   ├── XFTforIOS/
│   │   │   │   │   │   ├── AllClassMapConditionwithCascade.xft (100 lines)
│   │   │   │   │   │   ├── CascadeConditioning.xft (44 lines)
│   │   │   │   │   │   ├── ClassMapPacketLengthCondition.xft (80 lines)
│   │   │   │   │   │   ├── ClassMapVlanCondition.xft (67 lines)
│   │   │   │   │   │   ├── Class_MatchAny_MplsTopmost.xft (45 lines)
│   │   │   │   │   │   ├── IOSAclConditionTest.xft (43 lines)
│   │   │   │   │   │   ├── QosClassificationCos.xft (58 lines)
│   │   │   │   │   │   ├── QosClassificationDscp.xft (59 lines)
│   │   │   │   │   │   ├── QosClassificationDscpIpv4.xft (52 lines)
│   │   │   │   │   │   ├── QosClassificationInner_Cos.xft (58 lines)
│   │   │   │   │   │   ├── QosClassificationPrecedence.xft (56 lines)
│   │   │   │   │   │   └── QosClassification_Cos_Dscp_Precedence.xft (89 lines)
│   │   │   │   │   ├── XFTforXR/
│   │   │   │   │   │   ├── ACLConditiontestXR.xft (57 lines)
│   │   │   │   │   │   ├── AllClassConditionwithoutCascade.xft (96 lines)
│   │   │   │   │   │   ├── ClassMapVlanCondition.xft (67 lines)
│   │   │   │   │   │   ├── Class_MatchAll_Description.xft (46 lines)
│   │   │   │   │   │   ├── Class_MatchAny_MplsImposition.xft (49 lines)
│   │   │   │   │   │   ├── Class_MatchAny_MplsTopmost.xft (50 lines)
│   │   │   │   │   │   ├── QosClassificationCos.xft (58 lines)
│   │   │   │   │   │   ├── QosClassificationDei.xft (55 lines)
│   │   │   │   │   │   ├── QosClassificationDscp.xft (59 lines)
│   │   │   │   │   │   ├── QosClassificationInner_Cos.xft (58 lines)
│   │   │   │   │   │   ├── QosClassificationIpv4Dscp.xft (53 lines)
│   │   │   │   │   │   ├── QosClassificationIpv4Precedence.xft (56 lines)
│   │   │   │   │   │   ├── QosClassificationPrecedence.xft (57 lines)
│   │   │   │   │   │   └── QosClassification_Cos_Dscp_Precedence.xft (87 lines)
│   │   │   │   │   ├── Activate_QosClassMap_default_NMS.xft (76 lines)
│   │   │   │   │   ├── Activate_QosClassMap_default_NMS_XR.xft (79 lines)
│   │   │   │   │   └── DeleteProcedureTest.xft (28 lines)
│   │   │   │   ├── xmp-im-qos-module.xml (57 lines)
│   │   │   │   └── xmp-im-qos-module.xsd (846 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── classMapCreateProcedure.xde (11 lines)
│   │   │   ├── classMapDeleteProcedure.xde (11 lines)
│   │   │   ├── classMapUpdateProcedure.xde (53 lines)
│   │   │   ├── error.xml (5 lines)
│   │   │   ├── excludeAssociations.xml (25 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── trim_procedure.xde (30 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.xmp.config.xde.mef-qos-inventory/
│   │   │   ├── getClassMapAclConditions.xpa/
│   │   │   │   └── getClassMapAclCondition/
│   │   │   │       ├── aems-class-show-run-ISR-Output.txt (236 lines)
│   │   │   │       ├── aems-class-show-runOutput.txt (77 lines)
│   │   │   │       ├── getClassMapAclCondition-runParser_IOS.rpl (148 lines)
│   │   │   │       ├── getClassMapAclCondition-runParser_XR.rpl (148 lines)
│   │   │   │       ├── getClassMapAclCondition.par (113 lines)
│   │   │   │       ├── show-class-map-output.txt (37 lines)
│   │   │   │       ├── show-run-class-map-output_XR.txt (20 lines)
│   │   │   │       ├── show-running-output.txt (626 lines)
│   │   │   │       ├── test.txt (27 lines)
│   │   │   │       └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosActions.xpa/
│   │   │   │   └── getQosActions/
│   │   │   │       ├── 22.txt (32 lines)
│   │   │   │       ├── XR.txt (191 lines)
│   │   │   │       ├── getQosActions-runParser_IOS.rpl (7009 lines)
│   │   │   │       ├── getQosActions-runParser_XR.rpl (11755 lines)
│   │   │   │       ├── getQosActions.par (113 lines)
│   │   │   │       ├── policy-map_IOS.txt (77 lines)
│   │   │   │       ├── show-policy-map-output.txt (62 lines)
│   │   │   │       ├── show-run-policy-map-output_XR.txt (579 lines)
│   │   │   │       ├── show-running-output.txt (213 lines)
│   │   │   │       ├── test.txt (69 lines)
│   │   │   │       └── xmp-im-qos-module.xsd (1401 lines)
│   │   │   ├── getQosClassMaps.xpa/
│   │   │   │   └── getQosClassMaps/
│   │   │   │       ├── aems-class-show-run-ISR-Output.txt (236 lines)
│   │   │   │       ├── aems-class-show-runOutput.txt (77 lines)
│   │   │   │       ├── getQosClassMaps-runParser_IOS.rpl (1148 lines)
│   │   │   │       ├── getQosClassMaps-runParser_XR.rpl (820 lines)
│   │   │   │       ├── getQosClassMaps.par (123 lines)
│   │   │   │       ├── show-class-map-output.txt (37 lines)
│   │   │   │       ├── show-run-class-map-output_XR.txt (41 lines)
│   │   │   │       ├── show-running-output.txt (626 lines)
│   │   │   │       └── xmp-im-policy-applications-module.xsd (1666 lines)
│   │   │   ├── getQosConditions.xpa/
│   │   │   │   └── getQosConditions/
│   │   │   │       ├── getQosConditions-runParser_IOS.rpl (543 lines)
│   │   │   │       ├── getQosConditions-runParser_XR.rpl (772 lines)
│   │   │   │       ├── getQosConditions.par (113 lines)
│   │   │   │       ├── show-class-map-output.txt (30 lines)
│   │   │   │       ├── show-run-class-map-output_XR.txt (39 lines)
│   │   │   │       ├── show-running-output.txt (152 lines)
│   │   │   │       └── xmp-im-qos-module.xsd (1082 lines)
│   │   │   ├── getQosPolicyMapPepBindings.xpa/
│   │   │   │   └── getQosPolicyMapPepBindings/
│   │   │   │       ├── CemInterfaces.txt (84 lines)
│   │   │   │       ├── CemInterfaces_41.txt (23 lines)
│   │   │   │       ├── getQosPolicyMapPepBindings-runParser_IOS.rpl (241 lines)
│   │   │   │       ├── getQosPolicyMapPepBindings-runParser_XR.rpl (186 lines)
│   │   │   │       ├── getQosPolicyMapPepBindings.par (127 lines)
│   │   │   │       ├── show-policy-map-interface-output.txt (63 lines)
│   │   │   │       ├── show-policy-map-interface-si-output.txt (62 lines)
│   │   │   │       ├── show-run-policy-map-interface-output_XR.txt (94 lines)
│   │   │   │       ├── show-running-output.txt (629 lines)
│   │   │   │       └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── getQosPolicyMaps.xpa/
│   │   │   │   └── getQosPolicyMap/
│   │   │   │       ├── aems-policy-show-run-ISR-Output.txt (150 lines)
│   │   │   │       ├── aems-policy-show-runOutput.txt (69 lines)
│   │   │   │       ├── getQosPolicyMap-runParser_IOS.rpl (395 lines)
│   │   │   │       ├── getQosPolicyMap-runParser_XR.rpl (394 lines)
│   │   │   │       ├── getQosPolicyMap.par (113 lines)
│   │   │   │       ├── show-policy-map-output.txt (54 lines)
│   │   │   │       ├── show-run-policy-map-output_XR.txt (71 lines)
│   │   │   │       ├── show-running-output.txt (667 lines)
│   │   │   │       ├── test.txt (83 lines)
│   │   │   │       └── xmp-im-policy-applications-module.xsd (1552 lines)
│   │   │   ├── ignorePolicyServiceGroupName.xpa/
│   │   │   │   └── ignorePolicyServiceGroupName/
│   │   │   │       ├── Cli_input.txt (39 lines)
│   │   │   │       ├── ignorePolicyServiceGroupName.par (55 lines)
│   │   │   │       ├── ignorePolicyServiceGroupNameParser_xdeIOS.rpl (98 lines)
│   │   │   │       └── ignorePolicyServiceGroupNameParser_xdeIOSOutput.xsd (20 lines)
│   │   │   ├── patches/
│   │   │   │   ├── C3plClassMapHasConditions (24 lines)
│   │   │   │   └── QosPolicerColorAction (73 lines)
│   │   │   ├── test/
│   │   │   │   ├── ios/
│   │   │   │   │   ├── acl_conditions_ios.xft (112 lines)
│   │   │   │   │   ├── actions_dupburst_ios.xft (456 lines)
│   │   │   │   │   ├── actions_ios.xft (399 lines)
│   │   │   │   │   ├── classMaps_ios.xft (123 lines)
│   │   │   │   │   ├── conditions_ios.xft (141 lines)
│   │   │   │   │   ├── getQosActions_priority.xft (112 lines)
│   │   │   │   │   ├── global_pep_bindings_ios.xft (263 lines)
│   │   │   │   │   ├── pep_bindings_noefp_ios.xft (118 lines)
│   │   │   │   │   └── policyMaps_ios.xft (286 lines)
│   │   │   │   └── iosxr/
│   │   │   │       ├── QosConfigurationFull.xft (8563 lines)
│   │   │   │       ├── acl_conditions_iosxr.xft (72 lines)
│   │   │   │       ├── actions_iosxr.xft (1098 lines)
│   │   │   │       ├── actions_multiclass_iosxr.xft (142 lines)
│   │   │   │       ├── classMaps_iosxr.xft (126 lines)
│   │   │   │       ├── conditions_iosxr.xft (115 lines)
│   │   │   │       ├── global_pep_bindings_iosxr.xft (217 lines)
│   │   │   │       ├── policyMaps_iosxr.xft (321 lines)
│   │   │   │       └── qos_policymap_actions.xft (2431 lines)
│   │   │   ├── tests/
│   │   │   │   └── testcases/
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_cos.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_dei.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_dscptunnel.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_ecn.xft (78 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_frde.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_groupvalue.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_innercos.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_mplstopmost.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_precedence.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_precedencetunnel.xft (65 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosActions_priority.xft (75 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosClassMaps_innervlan.xft (303 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosClassMaps_mplstopmost.xft (69 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosClassMaps_vlanid.xft (303 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosConditions_discardclass.xft (68 lines)
│   │   │   │       ├── qos_ASR9001_XR520_getQosConditions_groupid.xft (68 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosActions_cos.xft (57 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosActions_groupvalue.xft (46 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosActions_mplstopmost.xft (46 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosActions_precendence.xft (46 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosClassMaps_innervlan.xft (171 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosClassMaps_mplstopmost.xft (169 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosClassMaps_vlanid.xft (171 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosConditions_discardclass.xft (247 lines)
│   │   │   │       ├── qos_ME3600_XE15.3(3)S_getQosConditions_groupid.xft (251 lines)
│   │   │   │       ├── qos_NCS4009_XR520_getQosActions_trafficclass.xft (79 lines)
│   │   │   │       └── qos_NCS4009_XR520_getQosConditions_trafficclass.xft (49 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getQosConfigProc.xde (337 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.xmp.config.xde.mef-qos-policyMap/
│   │   │   ├── mef-qos-policyMap.xpa/
│   │   │   │   ├── policyMap_CreateAndUpdateWriter/
│   │   │   │   │   ├── ME1200.vtl (172 lines)
│   │   │   │   │   ├── ios.vtl (869 lines)
│   │   │   │   │   ├── iosxe.vtl (936 lines)
│   │   │   │   │   ├── iosxr.vtl (831 lines)
│   │   │   │   │   └── policyMapCreateAndUpdateWriter.par (323 lines)
│   │   │   │   ├── policyMap_DeleteWriter/
│   │   │   │   │   ├── ME1200.vtl (0 lines)
│   │   │   │   │   ├── ios.vtl (65 lines)
│   │   │   │   │   ├── iosxr.vtl (35 lines)
│   │   │   │   │   └── policyMapDeleteWriter.par (37 lines)
│   │   │   │   ├── test/
│   │   │   │   │   ├── ASR907/
│   │   │   │   │   │   ├── ConformActionXFTforIOS/
│   │   │   │   │   │   │   ├── Confirm_action_ByPass_discard_class.xft (69 lines)
│   │   │   │   │   │   │   ├── Confirm_action_ByPass_l2_cos.xft (69 lines)
│   │   │   │   │   │   │   ├── Confirm_action_ByPass_mpls_exp.xft (69 lines)
│   │   │   │   │   │   │   └── Confirm_action_ByPass_mpls_exp_top_most.xft (69 lines)
│   │   │   │   │   │   ├── ExceedActionXFT/
│   │   │   │   │   │   │   ├── Exceed_action_ByPass_discard_class.xft (69 lines)
│   │   │   │   │   │   │   ├── Exceed_action_ByPass_l2_cos.xft (69 lines)
│   │   │   │   │   │   │   ├── Exceed_action_ByPass_mpls_exp.xft (69 lines)
│   │   │   │   │   │   │   └── Exceed_action_ByPass_mpls_exp_top_most.xft (69 lines)
│   │   │   │   │   │   ├── QosMarkingActionXFTforIOS/
│   │   │   │   │   │   │   ├── QosMarker_BypassFrFecnBecnTest.xft (60 lines)
│   │   │   │   │   │   │   ├── QosMarker_Bypass_Fr_de_bit.xft (59 lines)
│   │   │   │   │   │   │   └── QosMarker_Bypass_atn_clp_bit.xft (59 lines)
│   │   │   │   │   │   └── ViolateActionXFT/
│   │   │   │   │   │       ├── Violate_action_ByPass_discard_class.xft (69 lines)
│   │   │   │   │   │       ├── Violate_action_ByPass_l2_cos.xft (69 lines)
│   │   │   │   │   │       ├── Violate_action_ByPass_mpls_exp.xft (69 lines)
│   │   │   │   │   │       └── Violate_action_ByPass_mpls_exp_top_most.xft (69 lines)
│   │   │   │   │   ├── ConformActionXFTforXR/
│   │   │   │   │   │   ├── XFTforUpdateProcedureXR/
│   │   │   │   │   │   │   ├── ConformActionUpdateAtm-Clp.xft (115 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateCosandInnerCos.xft (143 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateDei.xft (123 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateDiscardClass.xft (127 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateDscpandPrecedence.xft (143 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateMplsExpTopmostandImposition.xft (146 lines)
│   │   │   │   │   │   │   ├── ConformActionUpdateQosGroup.xft (125 lines)
│   │   │   │   │   │   │   └── ConformActionUpdateTransmitandDrop.xft (138 lines)
│   │   │   │   │   │   ├──  ConformActiondDscpTunnelandPrecedenceTunnelTest.xft (82 lines)
│   │   │   │   │   │   ├── ConformActionCosandInnerCosTest.xft (80 lines)
│   │   │   │   │   │   ├── ConformActionDiscardClassandDeiTest.xft (80 lines)
│   │   │   │   │   │   ├── ConformActionDscpandPrecedenceTest.xft (80 lines)
│   │   │   │   │   │   ├── ConformActionMplsExpTopmostandImpositionTest.xft (83 lines)
│   │   │   │   │   │   ├── ConformActionTransmitandDropTest.xft (84 lines)
│   │   │   │   │   │   ├── ConformActiondAtm-ClpTest.xft (61 lines)
│   │   │   │   │   │   ├── ConformActiondDscpTunnelandPrecedenceTunnelTest.xft (82 lines)
│   │   │   │   │   │   └── ConformActiondQosGroupandFrDeTest.xft (80 lines)
│   │   │   │   │   ├── ExceedActionXFTforXR/
│   │   │   │   │   │   ├── XFTforUpdateProcedureXR/
│   │   │   │   │   │   │   ├── ExceedActionUpdateAtm-Clp.xft (125 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateCosandInnerCos.xft (169 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateDei.xft (123 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateDiscardClass.xft (122 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateDscpandPrecedence.xft (144 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateMplsExpTopmostandImposition.xft (168 lines)
│   │   │   │   │   │   │   ├── ExceedActionUpdateQosGroup.xft (122 lines)
│   │   │   │   │   │   │   └── ExceedActionUpdateTransmitandDrop.xft (140 lines)
│   │   │   │   │   │   ├── ExceedActionCosandInnerCosTest.xft (84 lines)
│   │   │   │   │   │   ├── ExceedActionDiscardClassandDeiTest.xft (83 lines)
│   │   │   │   │   │   ├── ExceedActionDscpandPrecedenceTest.xft (84 lines)
│   │   │   │   │   │   ├── ExceedActionMplsExpTopmostandImpositionTest.xft (84 lines)
│   │   │   │   │   │   ├── ExceedActionTransmitandDropTest.xft (81 lines)
│   │   │   │   │   │   ├── ExceedActiondAtm-ClpTest.xft (62 lines)
│   │   │   │   │   │   ├── ExceedActiondDscpTunnelandPrecedenceTunnelTest.xft (83 lines)
│   │   │   │   │   │   └── ExceedActiondQosGroupandFrDeTest.xft (83 lines)
│   │   │   │   │   ├── PolicerActionXFTforIOS&XR/
│   │   │   │   │   │   ├── PolicerAction.xft (245 lines)
│   │   │   │   │   │   └── PolicerActionXR.xft (92 lines)
│   │   │   │   │   ├── QosMarkingActionXFTforIOS/
│   │   │   │   │   │   ├── QosMarkingActionUpdateProcedureIOS/
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateCos.xft (112 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateDscp.xft (109 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdatePrecedence.xft (106 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateQos-Group.xft (113 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateCosInner.xft (109 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateDiscardClass.xft (107 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateFrameDiscardEligiblityTest.xft (95 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateIpDscpTunnelTest.xft (111 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateMplsImpositionTest.xft (110 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateMplsTopmostTest.xft (108 lines)
│   │   │   │   │   │   │   └── QosMarkerUpdatePrecdenceTunnelTest.xft (110 lines)
│   │   │   │   │   │   ├── QosMarkerAtm-ClpTest.xft (58 lines)
│   │   │   │   │   │   ├── QosMarkerCosInner.xft (150 lines)
│   │   │   │   │   │   ├── QosMarkerCosTest.xft (129 lines)
│   │   │   │   │   │   ├── QosMarkerDiscardClass.xft (133 lines)
│   │   │   │   │   │   ├── QosMarkerFrFecnBecnTest.xft (58 lines)
│   │   │   │   │   │   ├── QosMarkerImpositionTest.xft (136 lines)
│   │   │   │   │   │   ├── QosMarkerPrecdenceTest.xft (86 lines)
│   │   │   │   │   │   ├── QosMarkerQosGroupTest.xft (138 lines)
│   │   │   │   │   │   ├── QosMarkerSetIpDscpTest.xft (144 lines)
│   │   │   │   │   │   └── QosMarkerSetMplsTopmostTest.xft (127 lines)
│   │   │   │   │   ├── QosMarkingActionXFTforXR/
│   │   │   │   │   │   ├── QosMarkingActionUpdateProcedureXR/
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateCos.xft (141 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateDscp.xft (139 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdatePrecedence.xft (135 lines)
│   │   │   │   │   │   │   ├── QosMarkerActionUpdateQos-Group.xft (142 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateCosInner.xft (138 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateDeiBitTest.xft (127 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateDiscardClass.xft (136 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateFrameDiscardEligiblityTest.xft (126 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateIpDscpTunnelTest.xft (140 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateMplsImpositionTest.xft (139 lines)
│   │   │   │   │   │   │   ├── QosMarkerUpdateMplsTopmostTest.xft (137 lines)
│   │   │   │   │   │   │   └── QosMarkerUpdatePrecdenceTunnelTest.xft (139 lines)
│   │   │   │   │   │   ├── QosMarkerCosInner.xft (151 lines)
│   │   │   │   │   │   ├── QosMarkerCosTest.xft (131 lines)
│   │   │   │   │   │   ├── QosMarkerDeiTest.xft (60 lines)
│   │   │   │   │   │   ├── QosMarkerDiscardClass.xft (134 lines)
│   │   │   │   │   │   ├── QosMarkerImpositionTest.xft (138 lines)
│   │   │   │   │   │   ├── QosMarkerPrecdenceTest.xft (88 lines)
│   │   │   │   │   │   ├── QosMarkerQosGroupTest.xft (140 lines)
│   │   │   │   │   │   ├── QosMarkerSetIpDscpTest.xft (146 lines)
│   │   │   │   │   │   └── QosMarkerSetMplsTopmostTest.xft (129 lines)
│   │   │   │   │   ├── QosQueueingAction_IOS/
│   │   │   │   │   │   ├── Bandwidth_Create.xft (63 lines)
│   │   │   │   │   │   ├── Bandwidth_Update_Test.xft (100 lines)
│   │   │   │   │   │   ├── PriorityQueueEnabled_Create_Test.xft (73 lines)
│   │   │   │   │   │   ├── Priority_Update_Test.xft (94 lines)
│   │   │   │   │   │   ├── QueueLimit_Create.xft (63 lines)
│   │   │   │   │   │   ├── QueueLimit_Update_Test.xft (106 lines)
│   │   │   │   │   │   ├── UpdateProcedureTest_ClassMap.xft (96 lines)
│   │   │   │   │   │   └── UpdateProcedureTest_PolicyMap.xft (97 lines)
│   │   │   │   │   ├── QosQueueingAction_IOSXR/
│   │   │   │   │   │   ├── Bandwidth_Test_Create.xft (73 lines)
│   │   │   │   │   │   ├── PriorityLevel.xft (56 lines)
│   │   │   │   │   │   ├── QueueLimit_Test_Create.xft (68 lines)
│   │   │   │   │   │   ├── QueueingAction_Update_Test.xft (176 lines)
│   │   │   │   │   │   ├── UpdateProcedureTest_ClassMap.xft (113 lines)
│   │   │   │   │   │   └── UpdateProcedureTest_PolicyMap.xft (113 lines)
│   │   │   │   │   ├── QosRedActionXFTforIOS/
│   │   │   │   │   │   ├── QosRedPrecedenceUpdateProcedureIOS/
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateAtm_Clp.xft (105 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateCos.xft (102 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateDiscard-Class.xft (102 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateDscp.xft (102 lines)
│   │   │   │   │   │   │   └── QosRedPrecedenceActionUpdatePrecedence.xft (102 lines)
│   │   │   │   │   │   ├── QosRedActionECNTest.xft (48 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionAtm-ClpTest.xft (69 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionCosTest.xft (70 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDiscard-ClassTest.xft (71 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDscpTest.xft (71 lines)
│   │   │   │   │   │   └── QosRedPrecedenceActionPrecedenceTest.xft (71 lines)
│   │   │   │   │   ├── QosRedActionXFTforXR/
│   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateProcedureXR/
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateCos.xft (126 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateDei.xft (127 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateDiscard-Class.xft (126 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateDscp.xft (126 lines)
│   │   │   │   │   │   │   ├── QosRedPrecedenceActionUpdateMpls.xft (126 lines)
│   │   │   │   │   │   │   └── QosRedPrecedenceActionUpdatePrecedence.xft (126 lines)
│   │   │   │   │   │   ├── QosRedActionECNTest.xft (50 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionCosTest.xft (117 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDEITest.xft (116 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDefaultTest.xft (86 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDiscard-ClassTest.xft (117 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionDscpTest.xft (116 lines)
│   │   │   │   │   │   ├── QosRedPrecedenceActionMplsTest.xft (116 lines)
│   │   │   │   │   │   └── QosRedPrecedenceActionPrecedenceTest.xft (116 lines)
│   │   │   │   │   ├── QosTrafficShapingAction_IOS/
│   │   │   │   │   │   ├── LimitTypeAsAverageAndAdaptiveRateSet.xft (70 lines)
│   │   │   │   │   │   ├── LimitTypeAsAverage_Adaptive_Update_Test.xft (102 lines)
│   │   │   │   │   │   ├── LimitTypeAsAverage_Create_Test.xft (66 lines)
│   │   │   │   │   │   ├── LimitTypeAsAverage_Update_Test.xft (114 lines)
│   │   │   │   │   │   ├── LimitTypeAsFecnAdaptiveShapingEnabledTest.xft (59 lines)
│   │   │   │   │   │   ├── LimitTypeAsFrVoiceAdaptiveDeactivationTimeTest.xft (60 lines)
│   │   │   │   │   │   ├── LimitTypeAsFrVoiceAdaptiveShapingEnabledTest.xft (59 lines)
│   │   │   │   │   │   ├── LimitTypeAsPeak.xft (66 lines)
│   │   │   │   │   │   ├── LimitTypeAsPeakAndAdaptiveRateSet.xft (111 lines)
│   │   │   │   │   │   ├── LimitTypeAsPeak_Adaptive_Update_Test.xft (124 lines)
│   │   │   │   │   │   ├── LimitTypeAsPeak_Update_Test.xft (177 lines)
│   │   │   │   │   │   ├── LimitTypeAs_FecnAdaptive_Update_Test.xft (94 lines)
│   │   │   │   │   │   ├── LimitTypeAs_Fr-VoiceAdaptiveDeactivationTime_Update_Test.xft (98 lines)
│   │   │   │   │   │   ├── LimitTypeAs_Fr-VoiceAdaptive_Update_Test.xft (94 lines)
│   │   │   │   │   │   ├── UpdateProcedureTest_ClassMap.xft (96 lines)
│   │   │   │   │   │   └── UpdateProcedureTest_PolicyMap.xft (97 lines)
│   │   │   │   │   ├── QosTrafficShapingAction_IOSXR/
│   │   │   │   │   │   ├── QosTrafficShapingAction_Test_Create.xft (59 lines)
│   │   │   │   │   │   ├── ShapingAction_Update_Test.xft (115 lines)
│   │   │   │   │   │   ├── UpdateProcedureTest_ClassMap.xft (113 lines)
│   │   │   │   │   │   └── UpdateProcedureTest_PolicyMap.xft (113 lines)
│   │   │   │   │   ├── ViolateActionXFTforXR/
│   │   │   │   │   │   ├── XFTforUpdateProcedureXR/
│   │   │   │   │   │   │   ├── ViolateActionUpdateAtm-Clp.xft (125 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateCosandInnerCos.xft (167 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateDei.xft (124 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateDiscardClass.xft (122 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateDscpandPrecedence.xft (144 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateMplsExpTopmostandImposition.xft (171 lines)
│   │   │   │   │   │   │   ├── ViolateActionUpdateQosGroup.xft (125 lines)
│   │   │   │   │   │   │   └── ViolateActionUpdateTransmitandDrop.xft (141 lines)
│   │   │   │   │   │   ├── ViolateActionCosandInnerCosTest.xft (83 lines)
│   │   │   │   │   │   ├── ViolateActionDiscardClassandDeiTest.xft (82 lines)
│   │   │   │   │   │   ├── ViolateActionDscpandPrecedenceTest.xft (82 lines)
│   │   │   │   │   │   ├── ViolateActionMplsExpTopmostandImpositionTest.xft (84 lines)
│   │   │   │   │   │   ├── ViolateActionTransmitandDropTest.xft (84 lines)
│   │   │   │   │   │   ├── ViolateActiondAtm-ClpTest.xft (62 lines)
│   │   │   │   │   │   ├── ViolateActiondDscpTunnelandPrecedenceTunnelTest.xft (83 lines)
│   │   │   │   │   │   └── ViolateActiondQosGroupandFrDeTest.xft (85 lines)
│   │   │   │   │   ├── Activate_QosPolicyMap_default_NMS.xft (99 lines)
│   │   │   │   │   ├── Activate_QosPolicyMap_default_NMS_XR_Marker.xft (103 lines)
│   │   │   │   │   ├── Activate_QosPolicyMap_default_NMS_XR_Police.xft (100 lines)
│   │   │   │   │   └── Activate_QosPolicyMap_default_NMS_XR_Queuing.xft (94 lines)
│   │   │   │   ├── xmp-im-qos-module.xml (260 lines)
│   │   │   │   └── xmp-im-qos-module.xsd (846 lines)
│   │   │   ├── .project (24 lines)
│   │   │   ├── error.xml (15 lines)
│   │   │   ├── excludeAssociations.xml (25 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── policyMapCreateProcedure.xde (14 lines)
│   │   │   ├── policyMapDeleteProcedure.xde (14 lines)
│   │   │   ├── policyMapUpdateProcedure.xde (78 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.xmp.config.xde.ospf-config/
│   │   │   ├── ospf-config-XE.xpa/
│   │   │   │   ├── ospfCreateAndUpdateWriter_XE/
│   │   │   │   │   ├── createospfIOSXE.vtl (332 lines)
│   │   │   │   │   └── ospfCreateAndUpdateWriter_XE.par (42 lines)
│   │   │   │   ├── ospfDeleteWriter_XE/
│   │   │   │   │   ├── deleteospfIOSXE.vtl (87 lines)
│   │   │   │   │   └── ospfDeleteWriter_XE.par (18 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   └── iosXE/
│   │   │   │   │       ├── createOspfTeSettings.xft (135 lines)
│   │   │   │   │       └── deleteOspfTeSettings.xft (123 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (4302 lines)
│   │   │   ├── ospf-config.xpa/
│   │   │   │   ├── ospfCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXR.vtl (316 lines)
│   │   │   │   │   └── ospfCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── ospfDeleteWriter/
│   │   │   │   │   ├── iosXR.vtl (89 lines)
│   │   │   │   │   └── ospfDeleteWriter.par (28 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   └── iosXR/
│   │   │   │   │       ├── createOspfPepSettings.xft (176 lines)
│   │   │   │   │       ├── createOspfProcessSettings.xft (72 lines)
│   │   │   │   │       ├── deleteOspfProcessSettings.xft (68 lines)
│   │   │   │   │       ├── updateOspfPepSettings.xft (241 lines)
│   │   │   │   │       └── updateOspfProcessSettings.xft (130 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (4302 lines)
│   │   │   ├── .project (35 lines)
│   │   │   ├── getDeviceType.xde (28 lines)
│   │   │   ├── ospfCreateProcedure.xde (34 lines)
│   │   │   ├── ospfDeleteProcedure.xde (35 lines)
│   │   │   ├── ospfUpdateProcedure.xde (121 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   ├── trim_procedure.xde (35 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.prime-ethernet-resource-model-config/
│   │   │   ├── EthFlowPoint-config.xpa/
│   │   │   │   ├── EthFlowPoint_CreateAndUpdateWriter/
│   │   │   │   │   ├── EthFlowPoint_CreateAndUpdateWriter.par (363 lines)
│   │   │   │   │   ├── cat6500.vtl (83 lines)
│   │   │   │   │   ├── ios.vtl (115 lines)
│   │   │   │   │   ├── iosME1200.vtl (97 lines)
│   │   │   │   │   ├── iosxe.vtl (123 lines)
│   │   │   │   │   ├── iosxr.vtl (102 lines)
│   │   │   │   │   └── velocity_macros.vm (210 lines)
│   │   │   │   ├── EthFlowPoint_DeleteWriter/
│   │   │   │   │   ├── EthFlowPoint_DeleteWriter.par (50 lines)
│   │   │   │   │   ├── cat6500.vtl (29 lines)
│   │   │   │   │   ├── ios.vtl (54 lines)
│   │   │   │   │   ├── iosME1200.vtl (40 lines)
│   │   │   │   │   └── iosxr.vtl (35 lines)
│   │   │   │   ├── TestCases2EMS/
│   │   │   │   │   ├── IOS-XFT/
│   │   │   │   │   │   ├── Activate_EthFlowPoint_default.xft (218 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad.xft (197 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_cos_etype.xft (205 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_cos_secondTag_cos_etype.xft (209 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_cos_secondTag_etype.xft (210 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_second-dot1q.xft (206 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_secondTag_cos_etype.xft (208 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1ad_secondTag_etype.xft (206 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q.xft (193 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_Pop1.xft (197 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_Pop2.xft (193 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_Push1.xft (193 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_and_etypes.xft (209 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_cos_etypes.xft (206 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_cos_etypes_not_supported.xft (206 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_cos_secondTag_cos_etype.xft (212 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_cos_secondTag_etype.xft (210 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_secondTag_cos_etype.xft (212 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_dot1q_secondTag_etype.xft (206 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_default.xft (85 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_priority-tagged.xft (142 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged.xft (205 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged_and_dot1ad.xft (197 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged_and_dot1q.xft (197 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged_and_etypes.xft (192 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged_and_priority-tagged_and_dot1ad.xft (197 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_untagged_and_priority-tagged_and_dot1q.xft (197 lines)
│   │   │   │   │   │   └── Activate_EthFlowPoint_untagged_priority-tagged_dot1q_cos_etypes.xft (204 lines)
│   │   │   │   │   └── asr9k-XFT/
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_exact_with_translate22.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_priorityTagged.xft (187 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_priorityTagged_exact.xft (187 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_secondTag_exact_with_translate22.xft (53 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_untagged.xft (193 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1ad_with_translate22.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_secondTag_with_Push2_dot1ad.xft (53 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_secondTag_with_Push2_dot1q.xft (53 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Pop1.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Pop2.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Push1_dot1ad.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Push1_dot1q.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Push2_dot1ad.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_Push2_dot1q.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_translate11_dot1ad.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_translate11_dot1q.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_translate21.xft (53 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_exact_with_translate22.xft (52 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_priorityTagged.xft (187 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_priorityTagged_exact.xft (187 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_secondTag_exact_with_Push2_dot1ad.xft (53 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_dot1q_untagged.xft (193 lines)
│   │   │   │   │       └── Activate_EthFlowPoint_qinq.xft (53 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── L3VPN/
│   │   │   │   │   │   └── asr9k/
│   │   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_any.xft (140 lines)
│   │   │   │   │   │       ├── Cease_EthFlowPoint_L2VPN.xft (49 lines)
│   │   │   │   │   │       └── Cease_EthFlowPoint_L3VPN.xft (49 lines)
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── Activate_EFPSubinterface_asr903.xft (107 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_15.5(1)_TOBEREMOVED.xft (112 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr901_Etree.xft (89 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Eaccess_NNI_EVPL.xft (140 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Eaccess_UNI_EPL.xft (139 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Eaccess_UNI_EVPL.xft (138 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Elan.xft (95 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Etree.xft (88 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_default.xft (84 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1ad.xft (155 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1ad_dot1q.xft (111 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1q.xft (155 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1q_dot1q.xft (110 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_priority-tagged.xft (86 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged.xft (150 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_dot1q.xft (151 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_etypes.xft (137 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_priority-tagged.xft (86 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_priority-tagged_dot1q.xft (99 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_l2cp-15.5(1).xft (87 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_l2cp.xft (86 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_l2cp_multipoint.xft (86 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_rewrite.xft (152 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_rewrite_push_dot1ad_dot1q.xft (154 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_switchport.xft (135 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_uni_attrib.xft (150 lines)
│   │   │   │   │   │   ├── Activate_LocalSwitching_asr903.xft (128 lines)
│   │   │   │   │   │   ├── Cease_EthFlowPoint_service.xft (98 lines)
│   │   │   │   │   │   └── Cease_LocalSwitching_asr903.xft (48 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       ├── Activate_EFPSubinterface_asr9k.xft (108 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_Etree.xft (154 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Eaccess_NNI.xft (94 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Eaccess_UNI_EPL.xft (94 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Eaccess_UNI_EVPL.xft (94 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Elan.xft (94 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_l2cp_multipoint.xft (93 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_default.xft (82 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad.xft (139 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_any.xft (139 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_dot1q_exact.xft (149 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_exact.xft (141 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_multivlans.xft (142 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_priority_tagged.xft (132 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_untagged.xft (139 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_any.xft (139 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_dot1q_any.xft (149 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_dot1q_exact.xft (150 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_dot1q_multivlans.xft (152 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_exact.xft (142 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_multivlans_untagged.xft (142 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_priority_tagged.xft (132 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_priority_tagged_exact.xft (132 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_untagged.xft (139 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_untagged.xft (128 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_l2cp.xft (94 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_qinq.xft (104 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_rewrite.xft (140 lines)
│   │   │   │   │       └── Cease_asr9k.xft (48 lines)
│   │   │   │   ├── testFromNMS/
│   │   │   │   │   ├── asr903/
│   │   │   │   │   │   ├── Activate_EFPSubinterface_asr903.xft (76 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Elan.xft (75 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_asr903_Etree.xft (75 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_default.xft (54 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1ad_dot1q.xft (56 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1ad_multivlans.xft (55 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1q_dot1q.xft (56 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1q_multivlans.xft (55 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_dot1q_multivlans_rewrite_push.xft (60 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_priority-tagged.xft (56 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged.xft (55 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_etypes.xft (59 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_priority-tagged.xft (56 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_priority-tagged_dot1q.xft (56 lines)
│   │   │   │   │   │   ├── Activate_EthFlowPoint_encap_untagged_priority_tagged_dot1q_cos_etypes.xft (68 lines)
│   │   │   │   │   │   └── Activate_LocalSwitching_asr903.xft (97 lines)
│   │   │   │   │   └── asr9k/
│   │   │   │   │       ├── Activate_EFPSubinterface_asr9k.xft (76 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Elan.xft (73 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_asr9k_Etree.xft (74 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_default.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_dot1q_multivlans_exact.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_multivlans.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_priority-tagged_exact.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1ad_untagged.xft (67 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q.xft (67 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_dot1q.xft (68 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_dot1q_multivlans_exact.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_multivlans.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_priority-tagged_exact.xft (55 lines)
│   │   │   │   │       ├── Activate_EthFlowPoint_encap_dot1q_untagged.xft (67 lines)
│   │   │   │   │       └── Activate_EthFlowPoint_encap_untagged.xft (66 lines)
│   │   │   │   ├── prime-ethernet-resource-model.xml (58 lines)
│   │   │   │   └── prime-ethernet-resource-model.xsd (210 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── EthFlowPoint_CreateProcedure.xde (16 lines)
│   │   │   ├── EthFlowPoint_DeleteProcedure.xde (14 lines)
│   │   │   ├── EthFlowPoint_UpdateProcedure.xde (28 lines)
│   │   │   ├── error.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (27 lines)
│   │   │   ├── isRspInstalled.xde (84 lines)
│   │   │   ├── packageDescriptor.xml (15 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.xmp.config.xde.prime-resource-model-config-PwSegment/
│   │   │   ├── prime-resource-model-config-PwSegment.xpa/
│   │   │   │   ├── PwSegment_CreateAndUpdateWriter/
│   │   │   │   │   ├── PwSegment_CreateAndUpdateWriter.par (302 lines)
│   │   │   │   │   ├── ios.vtl (170 lines)
│   │   │   │   │   ├── iosGT15.6.vtl (337 lines)
│   │   │   │   │   ├── iosME-36x38x.vtl (224 lines)
│   │   │   │   │   ├── iosME-36x38xGT15.6.vtl (276 lines)
│   │   │   │   │   ├── iosxr.vtl (211 lines)
│   │   │   │   │   └── mtu_macro.vm (6 lines)
│   │   │   │   ├── PwSegment_DeleteWriter/
│   │   │   │   │   ├── PwSegment_DeleteWriter.par (228 lines)
│   │   │   │   │   ├── ios.vtl (140 lines)
│   │   │   │   │   ├── iosGT15.6.vtl (272 lines)
│   │   │   │   │   ├── iosME-36x38x.vtl (165 lines)
│   │   │   │   │   ├── iosME-36x38xGT15.6.vtl (205 lines)
│   │   │   │   │   └── iosxr.vtl (174 lines)
│   │   │   │   ├── testFromEMS/
│   │   │   │   │   ├── Activate_EFPSubinterface_asr903.xft (131 lines)
│   │   │   │   │   ├── Activate_EFPSubinterface_asr9k.xft (249 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_MTU_asrME-36x.xft (156 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_MTU_asrME-38x.xft (156 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asr903.xft (119 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asr903_15.6GT.xft (189 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asr9k.xft (90 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asrME-36x.xft (117 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asrME-38x.xft (117 lines)
│   │   │   │   │   ├── Activate_PwSegmentWithBackup.xft (161 lines)
│   │   │   │   │   ├── Activate_PwSegmentWithBackupWrongOrder.xft (211 lines)
│   │   │   │   │   ├── Activate_PwSegmentWithbackupWrongOrder_asr9k.xft (161 lines)
│   │   │   │   │   ├── Activate_PwSegmentWithbackup_asr9k.xft (161 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan.xft (132 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan_hub.xft (163 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan_vfi_defaultVcId.xft (131 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Etree.xft (167 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k.xft (111 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Elan.xft (113 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Elan_HVPLS.xft (167 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Elan_VPLS.xft (160 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Etree.xft (113 lines)
│   │   │   │   │   ├── Activate_PwSegment_asrME-36x_Elan.xft (127 lines)
│   │   │   │   │   ├── Activate_PwSegment_asrME-36x_Etree.xft (170 lines)
│   │   │   │   │   ├── Activate_PwSegment_asrME-36x_Etree_HVPLS_SVI.xft (203 lines)
│   │   │   │   │   ├── Activate_PwSegment_dot1q_pop_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_dot1q_push_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_dot1q_untagged_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_epl_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_epl_iosME_GT_5.6.xft (296 lines)
│   │   │   │   │   ├── Activate_PwSegment_epl_ios_GT_5.6.xft (168 lines)
│   │   │   │   │   ├── Activate_PwSegment_qinq_pop_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_qinq_push_asr903.xft (156 lines)
│   │   │   │   │   ├── Activate_PwSegment_qinq_untagged_asr903.xft (156 lines)
│   │   │   │   │   ├── Cease_LocalSwitching_asr9k.xft (118 lines)
│   │   │   │   │   ├── Cease_LocalSwitching_asrME-36x.xft (130 lines)
│   │   │   │   │   ├── Cease_LocalSwitching_asrME-38x.xft (129 lines)
│   │   │   │   │   ├── Cease_PwSegmentWithBackup.xft (203 lines)
│   │   │   │   │   ├── Cease_PwSegmentWithBackupWrongOrder.xft (203 lines)
│   │   │   │   │   ├── Cease_PwSegmentWithbackupWrongOrder_asr9k.xft (152 lines)
│   │   │   │   │   ├── Cease_PwSegmentWithbackup_asr9k.xft (152 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr903_Elan.xft (118 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr903_Elan_hub.xft (151 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr903_Elan_vfi_defaultVcId.xft (118 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr903_Eline.xft (154 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr903_Eline_GT_5.6.xft (156 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr9k_Elan.xft (102 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr9k_Elan_HVPLS.xft (152 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr9k_Elan_VPLS.xft (152 lines)
│   │   │   │   │   ├── Cease_PwSegment_asr9k_Eline.xft (104 lines)
│   │   │   │   │   ├── Cease_PwSegment_asrME-36x_ETree_hvpls_hub.xft (118 lines)
│   │   │   │   │   ├── Cease_PwSegment_service.xft (150 lines)
│   │   │   │   │   ├── PwSegment_asr903_Eline_GT_5.6_noInterfaceId.xft (156 lines)
│   │   │   │   │   └── cease_PwSegment_epl_ios_GT_5.6.xft (168 lines)
│   │   │   │   ├── testFromNMS/
│   │   │   │   │   ├── Activate_EFPSubinterface_asr903.xft (83 lines)
│   │   │   │   │   ├── Activate_EFPSubinterface_asr9k.xft (101 lines)
│   │   │   │   │   ├── Activate_LocalSwitching_asr9k.xft (62 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903.xft (83 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan.xft (82 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan_HVPLS.xft (102 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Elan_VPLS_defaultVcId.xft (84 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr903_Etree.xft (103 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k.xft (71 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Elan.xft (81 lines)
│   │   │   │   │   ├── Activate_PwSegment_asr9k_Elan_HVPLS.xft (102 lines)
│   │   │   │   │   └── Activate_PwSegment_asr9k_Etree.xft (77 lines)
│   │   │   │   └── prime-resource-model.xsd (265 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── PwSegment_CreateProcedure.xde (14 lines)
│   │   │   ├── PwSegment_DeleteProcedure.xde (14 lines)
│   │   │   ├── PwSegment_RollbackCreateProcedure.xde (11 lines)
│   │   │   ├── PwSegment_RollbackDeleteProcedure.xde (11 lines)
│   │   │   ├── PwSegment_RollbackUpdateProcedure.xde (12 lines)
│   │   │   ├── PwSegment_UpdateProcedure.xde (28 lines)
│   │   │   ├── conf.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (27 lines)
│   │   │   ├── packageDescriptor.xml (17 lines)
│   │   │   └── xmpxde.xml (23 lines)
│   │   ├── com.cisco.xmp.config.xde.rsvp/
│   │   │   ├── rsvp.xpa/
│   │   │   │   ├── rsvpCreateAndUpdateWriter/
│   │   │   │   │   ├── ios-xr.vtl (76 lines)
│   │   │   │   │   ├── ios.vtl (63 lines)
│   │   │   │   │   └── rsvpCreateAndUpdateWriter.par (32 lines)
│   │   │   │   ├── rsvpDeleteWriter/
│   │   │   │   │   ├── ios-xr.vtl (77 lines)
│   │   │   │   │   ├── ios.vtl (66 lines)
│   │   │   │   │   └── rsvpDeleteWriter.par (36 lines)
│   │   │   │   └── testFromEMS/
│   │   │   │       ├── iosXE/
│   │   │   │       │   ├── createRSVP_IOS.xft (88 lines)
│   │   │   │       │   ├── createRSVP_IOS_Bandwidthpercent.xft (37 lines)
│   │   │   │       │   ├── createRSVP_IOS_withoutBandwidthpercent.xft (38 lines)
│   │   │   │       │   ├── deleteRSVP_IOS.xft (92 lines)
│   │   │   │       │   └── updateRSVP_IOS.xft (98 lines)
│   │   │   │       └── iosXR/
│   │   │   │           ├── createRSVP_IOSXR_Bandwidthpercent.xft (38 lines)
│   │   │   │           ├── createRSVP_IOSXR_Bandwidthpercent_BC1enabled.xft (40 lines)
│   │   │   │           ├── createRSVP_IOSXR_Bandwidthpercent_PerFlowBitrate.xft (39 lines)
│   │   │   │           ├── createRSVP_IOSXR_Bandwidthpercent_subpool.xft (40 lines)
│   │   │   │           ├── createRSVP_IOS_XR.xft (126 lines)
│   │   │   │           ├── deleteRSVP_IOS_XR.xft (59 lines)
│   │   │   │           ├── deleteRSVP_IOS_XR_bandwidthInPercent.xft (59 lines)
│   │   │   │           ├── deleteRSVP_IOS_XR_bandwidth_BC1enabled.xft (59 lines)
│   │   │   │           ├── deleteRSVP_IOS_XR_bandwidth_BC1enabled_no_subpool.xft (59 lines)
│   │   │   │           └── updateRSVP_IOS_XR.xft (152 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   ├── rsvpCreateProcedure.xde (21 lines)
│   │   │   ├── rsvpDeleteProcedure.xde (18 lines)
│   │   │   ├── rsvpUpdateProcedure.xde (37 lines)
│   │   │   ├── trim_procedure.xde (31 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde-eoam-ipsla-config/
│   │   │   ├── IpSlaTwamp.xpa/
│   │   │   │   ├── twampCreateAndUpdateWriter/
│   │   │   │   │   ├── twampCreateAndUpdateWriter.par (71 lines)
│   │   │   │   │   ├── twampCreateIOS.vtl (28 lines)
│   │   │   │   │   └── twampCreateIOSXR.vtl (20 lines)
│   │   │   │   └── twampDeleteWriter/
│   │   │   │       ├── twampDeleteIOS.vtl (2 lines)
│   │   │   │       ├── twampDeleteIOSXR.vtl (2 lines)
│   │   │   │       └── twampDeleteWriter.par (71 lines)
│   │   │   ├── .project (30 lines)
│   │   │   ├── ipslaCreateProcedure.xde (20 lines)
│   │   │   ├── ipslaDeleteProcedure.xde (19 lines)
│   │   │   ├── ipslaUpdateProcedure.xde (55 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde-eoam-ipsla-inventory/
│   │   │   ├── IpReaction.xpa/
│   │   │   │   └── IpSlaReactionCli/
│   │   │   │       ├── IpSlaReactionCli.par (121 lines)
│   │   │   │       ├── IpSlaReaction_xdeIOS.rpl (1142 lines)
│   │   │   │       ├── IpSlaReaction_xdeIOS_XR.rpl (1156 lines)
│   │   │   │       ├── cliOutputIos.txt (13 lines)
│   │   │   │       ├── cliOutputIosXr.txt (16 lines)
│   │   │   │       ├── masterIpSlaConfigXR.txt (421 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3567 lines)
│   │   │   ├── IpSlaGroupSchedule.xpa/
│   │   │   │   ├── IpSlaGroupScheduleCli/
│   │   │   │   │   ├── IpSlaGroupScheduleCli.par (65 lines)
│   │   │   │   │   ├── IpSlaGroupScheduleCliParser_xdeIOS.rpl (108 lines)
│   │   │   │   │   ├── cliOutputIos.txt (79 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   │   └── IpSlaGroupScheduleSnmp/
│   │   │   │       ├── IpSlaGroupScheduleSnmp.map (28 lines)
│   │   │   │       ├── IpSlaGroupScheduleSnmp.par (33 lines)
│   │   │   │       ├── snmpOutputIos.txt (86 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   ├── IpSlaNrSettings.xpa/
│   │   │   │   └── IpSlaNrSettingsCli/
│   │   │   │       ├── IpSlaNrSettingsCli.par (42 lines)
│   │   │   │       ├── IpSlaNrSettingsCliParser_xdeIOS.rpl (158 lines)
│   │   │   │       ├── IpSlaNrSettingsCliParser_xdeIOS_XR.rpl (158 lines)
│   │   │   │       ├── cliOutputIos.txt (24 lines)
│   │   │   │       ├── cliOutputIosXr.txt (24 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   ├── IpSlaOperations.xpa/
│   │   │   │   ├── IpSlaOperationsCli/
│   │   │   │   │   ├── IpSlaOperationsCli.out.xml (0 lines)
│   │   │   │   │   ├── IpSlaOperationsCli.par (117 lines)
│   │   │   │   │   ├── IpSlaOperationsCliParser_xdeIOS.rpl (2343 lines)
│   │   │   │   │   ├── IpSlaOperationsCliParser_xdeIOS_XR.rpl (1192 lines)
│   │   │   │   │   ├── cliOutputIos.txt (286 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (238 lines)
│   │   │   │   │   ├── clioutput_ASR90X.txt (975 lines)
│   │   │   │   │   ├── enumParseType.ept (1552 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3351 lines)
│   │   │   │   └── IpSlaOperationsSnmp/
│   │   │   │       ├── IpSlaOperationsSnmp.map (93 lines)
│   │   │   │       ├── IpSlaOperationsSnmp.par (52 lines)
│   │   │   │       ├── snmpOutputIos.txt (281 lines)
│   │   │   │       ├── snmpOutputIosXr.txt (126 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3060 lines)
│   │   │   ├── IpSlaResponder.xpa/
│   │   │   │   └── IpSlaResponderCli/
│   │   │   │       ├── IpSlaResponderCli.par (110 lines)
│   │   │   │       ├── IpSlaResponderCliParser_xdeIOS.rpl (659 lines)
│   │   │   │       ├── IpSlaResponderCliParser_xdeIOS_XR.rpl (315 lines)
│   │   │   │       ├── cliOutputIos.txt (10 lines)
│   │   │   │       ├── cliOutputIosXr.txt (1 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   ├── IpSlaSimpleSchedule.xpa/
│   │   │   │   ├── IpSlaSimpleSchOperation/
│   │   │   │   │   ├── IpSlaSimpleSchOperation.par (66 lines)
│   │   │   │   │   ├── IpSlaSimpleScheduleCliParser_xdeIOS_XR.rpl (120 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (44 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   │   ├── IpSlaSimpleSchStatistics/
│   │   │   │   │   ├── IpSlaSimpleSchStatistics.par (66 lines)
│   │   │   │   │   ├── IpSlaSimpleScheduleCliParser_xdeIOS_XR.rpl (98 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (221 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   │   ├── IpSlaSimpleScheduleCli/
│   │   │   │   │   ├── IpSlaSimpleScheduleCli.par (119 lines)
│   │   │   │   │   ├── IpSlaSimpleScheduleCliParser_xdeIOS.rpl (314 lines)
│   │   │   │   │   ├── IpSlaSimpleScheduleCliParser_xdeIOS_XR.rpl (368 lines)
│   │   │   │   │   ├── cliOutputIos.txt (318 lines)
│   │   │   │   │   ├── cliOutputIosXr.txt (102 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   │   ├── IpSlaSimpleScheduleSnmp/
│   │   │   │   │   ├── IpSlaSimpleScheduleSnmp.map (25 lines)
│   │   │   │   │   ├── IpSlaSimpleScheduleSnmp.par (25 lines)
│   │   │   │   │   ├── snmpOutputIos.txt (82 lines)
│   │   │   │   │   ├── snmpOutputIosXr.txt (34 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   │   └── IpSlaSimpleScheduleStartXE/
│   │   │   │       ├── IpSlaSimpleScheduleStartXE.par (65 lines)
│   │   │   │       ├── IpSlaSimpleScheduleStartXE.rpl (117 lines)
│   │   │   │       ├── cliOutputIos.txt (5 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (3042 lines)
│   │   │   ├── IpSlaTwamp.xpa/
│   │   │   │   └── IpSlaTwampCli/
│   │   │   │       ├── IpSlaTwampCli.par (102 lines)
│   │   │   │       ├── IpSlaTwampCliParser_xdeIOS.rpl (226 lines)
│   │   │   │       ├── IpSlaTwampCliParser_xdeIOS_XR.rpl (228 lines)
│   │   │   │       ├── IpSlaTwampCliParser_xdeIOS_XROutput.xsd (20 lines)
│   │   │   │       ├── cliOutputIos.txt (20 lines)
│   │   │   │       ├── cliOutputIosXr.txt (17 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (22 lines)
│   │   │   ├── IpSlaTwampLight.xpa/
│   │   │   │   ├── IpSlaTwampLight/
│   │   │   │   │   ├── IpSlaTwampLight.par (54 lines)
│   │   │   │   │   ├── IpSlaTwampLightParser_xdeIOS_XR.rpl (213 lines)
│   │   │   │   │   ├── cliOutput_XR.txt (48 lines)
│   │   │   │   │   └── xmp-im-ethernet-oam-module.xsd (4270 lines)
│   │   │   │   └── ipSlaTwampLightProcedure.xde (51 lines)
│   │   │   ├── tests/
│   │   │   │   ├── IpSlaGroupScheduleCli_IOS_XE_ASR901.xft (201 lines)
│   │   │   │   ├── IpSlaNrSettingsCli_IOS_XE_901.xft (69 lines)
│   │   │   │   ├── IpSlaNrSettingsCli_IOS_XR_9006.xft (69 lines)
│   │   │   │   ├── IpSlaOperationsCli_IOS_XE_ASR901.xft (1023 lines)
│   │   │   │   ├── IpSlaOperationsCli_IOS_XE_ASR901_CSCur98455.xft (1023 lines)
│   │   │   │   ├── IpSlaOperationsCli_IOS_XE_ASR901_CSCur99011.xft (1023 lines)
│   │   │   │   ├── IpSlaOperationsCli_IOS_XR_ASR9006.xft (113 lines)
│   │   │   │   ├── IpSlaReaction_CLI_IOS_XE_ASR901.xft (35 lines)
│   │   │   │   ├── IpSlaResponderCli_IOS_XE_ASR901.xft (136 lines)
│   │   │   │   ├── IpSlaResponderCli_IOS_XR_ASR9006.xft (76 lines)
│   │   │   │   └── IpSlaSimpleScheduleCli_IOS_XE_ASR901.xft (850 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (338 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde-erps-g8032-inventory/
│   │   │   ├── cisco-g8032-nodesettings.xpa/
│   │   │   │   ├── getNodeSettings/
│   │   │   │   │   ├── getNodeSettings.par (44 lines)
│   │   │   │   │   ├── getNodeSettingsParser_xdeIOS_XR.rpl (72 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (12 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS_XR.txt (14 lines)
│   │   │   │   │   └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   │   └── getNodeTcnSettings/
│   │   │   │       ├── getNodeTcnSettings.par (46 lines)
│   │   │   │       ├── getNodeTcnSettingsParser_xdeIOS.rpl (93 lines)
│   │   │   │       ├── getNodeTcnSettingsParser_xdeIOS_XR.rpl (95 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (1 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (10 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringinstapsportsettings.xpa/
│   │   │   │   ├── getRingInstanceApsPortSettings/
│   │   │   │   │   ├── getRingInstanceApsPortSettings.par (65 lines)
│   │   │   │   │   ├── getRingInstanceApsPortSettingsParser_xdeIOS_XR.rpl (161 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (31 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS_XR.txt (35 lines)
│   │   │   │   │   └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   │   └── getRingInstanceApsUnresolvedPortSettings/
│   │   │   │       ├── PortSettingsParser_xdeIOS.rpl (182 lines)
│   │   │   │       ├── PortSettingsParser_xdeIOS_XR.rpl (168 lines)
│   │   │   │       ├── getRingInstanceApsUnresolvedPortSettings.par (63 lines)
│   │   │   │       ├── output_XE_24.txt (43 lines)
│   │   │   │       ├── output_XR17.txt (96 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringinstportsettings.xpa/
│   │   │   │   └── getRingInstancePortSettings/
│   │   │   │       ├── flagEnumParseType.ept (28 lines)
│   │   │   │       ├── getRingInstancePortSettings.par (63 lines)
│   │   │   │       ├── getRingInstancePortSettingsParser_xdeIOS_XR.rpl (275 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (31 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (34 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringinstsettings.xpa/
│   │   │   │   ├── getRingInstanceNodeSettings/
│   │   │   │   │   ├── getRingInstanceNodeSettings.par (61 lines)
│   │   │   │   │   ├── getRingInstanceNodeSettingsParser_xdeIOS_XR.rpl (252 lines)
│   │   │   │   │   ├── nodeState.ept (16 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS.txt (31 lines)
│   │   │   │   │   ├── sampleDeviceOutputIOS_XR.txt (42 lines)
│   │   │   │   │   └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   │   └── getRingInstanceSettings/
│   │   │   │       ├── getRingInstanceSettings.par (63 lines)
│   │   │   │       ├── getRingInstanceSettingsParser_xdeIOS.rpl (368 lines)
│   │   │   │       ├── getRingInstanceSettingsParser_xdeIOS_XR.rpl (330 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (26 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (53 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringportsetings.xpa/
│   │   │   │   └── getRingPortSettings/
│   │   │   │       ├── SampleDeviceOutputIOS_XR.txt (30 lines)
│   │   │   │       ├── getRingPortSettings.par (61 lines)
│   │   │   │       ├── getRingPortSettingsParser_xdeIOS.rpl (170 lines)
│   │   │   │       ├── getRingPortSettingsParser_xdeIOS_XR.rpl (194 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (25 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringprofile.xpa/
│   │   │   │   └── getProfileInformation/
│   │   │   │       ├── getProfileInformation.par (60 lines)
│   │   │   │       ├── getProfileInformationParser_xdeIOS_XR.rpl (180 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (5 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (7 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-g8032-ringsettings.xpa/
│   │   │   │   └── getRingSettings/
│   │   │   │       ├── getRingSettings.par (62 lines)
│   │   │   │       ├── getRingSettingsParser_xdeIOS.rpl (195 lines)
│   │   │   │       ├── getRingSettingsParser_xdeIOS_XR.rpl (195 lines)
│   │   │   │       ├── sampleDeviceOutputIOS.txt (25 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR.txt (30 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── tests/
│   │   │   │   ├── defects/
│   │   │   │   │   ├── CSCuq89294.xft (76 lines)
│   │   │   │   │   ├── CSCuq89297.xft (132 lines)
│   │   │   │   │   ├── CSCuq91755.xft (133 lines)
│   │   │   │   │   ├── CSCuq91806.xft (63 lines)
│   │   │   │   │   ├── CSCuq96286.xft (132 lines)
│   │   │   │   │   ├── CSCuq97715.xft (97 lines)
│   │   │   │   │   ├── CSCuq99867.xft (68 lines)
│   │   │   │   │   ├── CSCur00413_forcedSwitch.xft (63 lines)
│   │   │   │   │   ├── CSCur00413_manualSwitch.xft (63 lines)
│   │   │   │   │   └── CSCur02463.xft (172 lines)
│   │   │   │   └── testcases/
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstancePortSetting_forcedSwitch.xft (63 lines)
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstancePortSetting_manualSwitch.xft (63 lines)
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstancePort_IL.xft (63 lines)
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstancePort_nonRPL_fail.xft (63 lines)
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstanceSetting_forcedSwitch.xft (63 lines)
│   │   │   │       ├── g8032_ASR9001_XR512_ringInstanceSetting_manualSwitch.xft (63 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_nodeSetting.xft (51 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_nodeTcnSettings.xft (41 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringInstanceApsPortSettings.xft (97 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringInstanceNodeSettings.xft (97 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringInstancePortSettings.xft (97 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringInstanceSettings.xft (173 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringPortSettings.xft (172 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringProfile.xft (52 lines)
│   │   │   │       ├── g8032_ASR9006_XR520_ringSettings.xft (172 lines)
│   │   │   │       ├── g8032_ASR901_XE_15.4_ringInstanceNodeSetting_manualSwitch.xft (57 lines)
│   │   │   │       ├── g8032_ASR901_XE_15.4_ringInstancePortSetting_manualSwitch.xft (57 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_nodeSettings.xft (45 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_nodeTcnSettings.xft (23 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_ringApsPortSetting.xft (57 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_ringInstanceNodeSetting.xft (57 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_ringInstancePortSetting.xft (57 lines)
│   │   │   │       ├── g8032_ASR903_XE_15.4_ringInstanceSetting.xft (77 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringInstanceNodeSetting.xft (57 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringInstanceNodeSetting_forcedSwitch.xft (57 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringInstancePort_forcedSwitch.xft (57 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringInstanceSetting.xft (57 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringPortSetting.xft (56 lines)
│   │   │   │       ├── g8032_ME36000_XE_12.2_ringProfile.xft (36 lines)
│   │   │   │       └── g8032_ME36000_XE_12.2_ringSetting.xft (56 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (205 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde-l2vpn-pseudowire-headend-config/
│   │   │   ├── testfromEMS/
│   │   │   │   └── asr9k/
│   │   │   │       ├── Activate_pwheGenericInterface_asr9k.xft (27 lines)
│   │   │   │       ├── Activate_pwheInterface_asr9k.xft (40 lines)
│   │   │   │       ├── Cease_pwheGenericInterface_asr9k.xft (24 lines)
│   │   │   │       └── Cease_pwheInterface_asr9k.xft (35 lines)
│   │   │   ├── xde-PWHEInterface-config.xpa/
│   │   │   │   ├── PWHEInterfaceParametersCreateAndUpdateWriter/
│   │   │   │   │   ├── PWHEInterfaceParametersCreateAndUpdateWriter.par (18 lines)
│   │   │   │   │   └── cisco-iosxr-PWHEInterface-ConfigCmds.vtl (43 lines)
│   │   │   │   ├── PWHEInterfaceParametersDeleteWriter/
│   │   │   │   │   ├── PWHEInterfaceParametersDeleteWriter.par (18 lines)
│   │   │   │   │   └── cisco-iosxr-PWHEInterface-ConfigCmdsDelete.vtl (18 lines)
│   │   │   │   └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── PWHEInterfaceParametersCreateProcedure.xde (21 lines)
│   │   │   ├── PWHEInterfaceParametersDeleteProcedure.xde (22 lines)
│   │   │   ├── PWHEInterfaceParametersUpdateProcedure.xde (28 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde.iccp-inventory/
│   │   │   ├── cisco-iosxr-iccp-getgroupmember.xpa/
│   │   │   │   └── getGroupMemberDetails/
│   │   │   │       ├── getGroupMemberDetails.par (26 lines)
│   │   │   │       ├── getGroupMemberDetails.rpl (458 lines)
│   │   │   │       ├── show iccp group-2.txt (22 lines)
│   │   │   │       ├── show iccp group.txt (17 lines)
│   │   │   │       └── xmp-im-iccp-module.xsd (401 lines)
│   │   │   ├── cisco-iosxr-iccp-getlocalldpid.xpa/
│   │   │   │   └── getLocalLdpId/
│   │   │   │       ├── cisco-iosxr-local-ldp-id-output.txt (4 lines)
│   │   │   │       ├── getLocalLdpId.par (25 lines)
│   │   │   │       ├── getLocalLdpIdParser_xdeIOS_XR.rpl (43 lines)
│   │   │   │       └── getLocalLdpIdParser_xdeIOS_XROutput.xsd (11 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (99 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde.mlacp-inventory/
│   │   │   ├── bundle_pep_settings.xpa/
│   │   │   │   └── bundle_pep_settings/
│   │   │   │       ├── bundle_down_output.txt (30 lines)
│   │   │   │       ├── bundle_output.txt (100 lines)
│   │   │   │       ├── bundle_pep_settings.par (25 lines)
│   │   │   │       ├── bundle_pep_settingsParser_xdeIOS_XR.rpl (259 lines)
│   │   │   │       └── xmp-im-mlacp-module.xsd (420 lines)
│   │   │   ├── cisco-iosxr-mlcap-IccpGroupSettings.xpa/
│   │   │   │   └── getMlacpIccpGroupSettings/
│   │   │   │       ├── getMlacpIccpGroupSettings.par (25 lines)
│   │   │   │       ├── getMlacpIccpGroupSettingsParser_xdeIOS_XR.rpl (213 lines)
│   │   │   │       ├── output.txt (19 lines)
│   │   │   │       └── xmp-im-mlacp-module.xsd (568 lines)
│   │   │   ├── cisco-iosxr-pseudo-mlacp-geticcpsmdata.xpa/
│   │   │   │   ├── getICCPInfoForSM/
│   │   │   │   │   ├── getICCPInfoForSM.par (24 lines)
│   │   │   │   │   ├── getICCPInfoForSMParserOutput.xsd (6 lines)
│   │   │   │   │   ├── getICCPInfoForSMParser_xdeIOS_XR.rpl (164 lines)
│   │   │   │   │   ├── show iccp group.txt (17 lines)
│   │   │   │   │   └── xmp-im-mlacp-module.xsd (568 lines)
│   │   │   │   └── getPseudoMlacpDetails/
│   │   │   │       ├── getPseudoMlacpDetails.par (26 lines)
│   │   │   │       ├── getPseudoMlacpDetails.rpl (769 lines)
│   │   │   │       ├── getPseudoMlacpDetailsOutput.xsd (61 lines)
│   │   │   │       ├── show bundle.txt (66 lines)
│   │   │   │       ├── show l2vpn iccp-sm.txt (43 lines)
│   │   │   │       └── xmp-im-mlacp-module.xsd (568 lines)
│   │   │   ├── member_pep_settings.xpa/
│   │   │   │   └── member_pep/
│   │   │   │       ├── bundle_output.txt (100 lines)
│   │   │   │       ├── member_pep.par (25 lines)
│   │   │   │       ├── member_pepParser_xdeIOS_XR.rpl (99 lines)
│   │   │   │       └── xmp-im-mlacp-module.xsd (420 lines)
│   │   │   ├── tests/
│   │   │   │   ├── Mlacp_XR512_ASR9001_ICCPInfo.xft (50 lines)
│   │   │   │   ├── Mlacp_XR512_ASR9001_PseudoMlacp.xft (70 lines)
│   │   │   │   ├── Mlacp_XR520_ASR9006_ICCPInfo.xft (94 lines)
│   │   │   │   └── Mlacp_XR520_ASR9006_PseudoMlacp.xft (70 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (24 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.config.xde.xde_config_interface_Me1200/
│   │   │   ├── interfaceWriter-ME1200.xpa/
│   │   │   │   ├── interface_me1200_CreateAndUpdateWriter/
│   │   │   │   │   ├── interface_me1200_CreateAndUpdateWriter.par (40 lines)
│   │   │   │   │   └── iosME1200.vtl (171 lines)
│   │   │   │   └── interface_me1200_DeleteWriter/
│   │   │   │       ├── interface_me1200_DeleteWriter.par (40 lines)
│   │   │   │       └── iosME1200.vtl (0 lines)
│   │   │   ├── EthFlowPoint_CreateProcedure.xde (16 lines)
│   │   │   ├── EthFlowPoint_DeleteProcedure.xde (14 lines)
│   │   │   ├── EthFlowPoint_UpdateProcedure.xde (28 lines)
│   │   │   ├── conf.xml (9 lines)
│   │   │   ├── ifm-im-connectivity-ext-module.xsd (3525 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.xmp.inventory.xde-lacplag-link/
│   │   │   ├── cisco-iosxr-lacp-lag-link.xpa/
│   │   │   │   └── getLACPLinkData/
│   │   │   │       ├── getLACPLinkData.map (29 lines)
│   │   │   │       ├── getLACPLinkData.par (28 lines)
│   │   │   │       ├── getLACPLinkDataOutput.xsd (28 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (1050 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (165 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── com.cisco.xmp.inventory.xde.ip-prefixlist/
│   │   │   ├── getIpPrefixListStatistics.xpa/
│   │   │   │   └── getIpPrefixListStatistics/
│   │   │   │       ├── getIpPrefixListStatistics.par (24 lines)
│   │   │   │       ├── getIpPrefixListStatisticsParser_xdeIOS.rpl (146 lines)
│   │   │   │       ├── getIpPrefixListStatisticsParser_xdeIOSOutput.xsd (21 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7248 lines)
│   │   │   ├── getIpPrefixlist.xpa/
│   │   │   │   └── getIpPrefixlist/
│   │   │   │       ├── getIpPrefixlist.par (53 lines)
│   │   │   │       ├── getIpPrefixlistParser_xdeIOS.rpl (71 lines)
│   │   │   │       ├── output.txt (14 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7477 lines)
│   │   │   ├── getIpPrefixlistEntry.xpa/
│   │   │   │   └── getIpPrefixlistEntry/
│   │   │   │       ├── getIpPrefixlistEntry.par (68 lines)
│   │   │   │       ├── getIpPrefixlistEntryParser_xdeIOS.rpl (267 lines)
│   │   │   │       ├── output.txt (17 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7477 lines)
│   │   │   ├── getIpPrefixlistEntryGranular.xpa/
│   │   │   │   └── getIpPrefixlistEntryGranular/
│   │   │   │       ├── getIpPrefixlistEntryGranular.par (58 lines)
│   │   │   │       ├── getIpPrefixlistEntryGranularParserOutput.xsd (6 lines)
│   │   │   │       ├── getIpPrefixlistEntryGranularParser_xdeIOS.rpl (257 lines)
│   │   │   │       ├── output_granular.txt (2 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7477 lines)
│   │   │   ├── getIpPrefixlistGranular.xpa/
│   │   │   │   └── getIpPrefixlistGranular/
│   │   │   │       ├── getIpPrefixlistGranular.par (27 lines)
│   │   │   │       ├── getIpPrefixlistGranularParserOutput.xsd (6 lines)
│   │   │   │       ├── getIpPrefixlistGranularParser_xdeIOS.rpl (70 lines)
│   │   │   │       ├── output.txt (3 lines)
│   │   │   │       ├── output2.txt (5 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (18 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (221 lines)
│   │   │   └── xmpxde.xml (46 lines)
│   │   ├── com.cisco.xmp.inventory.xde.ipsla-twamp-light-inventory/
│   │   │   ├── IpSlaTwampLight_responder.xpa/
│   │   │   │   └── IpSlaTwampLight_responder/
│   │   │   │       ├── IpSlaTwampLightParser_xdeIOS_XR_responder.rpl (100 lines)
│   │   │   │       ├── IpSlaTwampLight_responder.par (59 lines)
│   │   │   │       ├── cliOutput_XR.txt (27 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (4285 lines)
│   │   │   ├── IpSlaTwampLight_session.xpa/
│   │   │   │   └── IpSlaTwampLight_session/
│   │   │   │       ├── IpSlaTwampLightParser_xdeIOS_XR_responder.rpl (213 lines)
│   │   │   │       ├── IpSlaTwampLight_session.par (62 lines)
│   │   │   │       ├── cliOutput_XR.txt (48 lines)
│   │   │   │       └── xmp-im-ethernet-oam-module.xsd (4285 lines)
│   │   │   ├── test/
│   │   │   │   └── IpslaTwampLight_session_functionTest.xft (169 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (59 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── com.cisco.xmp.inventory.xde.isis-inventory/
│   │   │   ├── isis-neighbor.xpa/
│   │   │   │   ├── getLocalIpByLocalInterface/
│   │   │   │   │   ├── getLocalIpByLocalInterface.par (113 lines)
│   │   │   │   │   ├── getLocal_xdeIOS.rpl (58 lines)
│   │   │   │   │   ├── getLocal_xdeIOS_XR.rpl (58 lines)
│   │   │   │   │   ├── iosInput.txt (1 lines)
│   │   │   │   │   ├── iosxrInput.txt (2 lines)
│   │   │   │   │   ├── show_ip_interface_brief_inc_localIsis.txt (2 lines)
│   │   │   │   │   ├── show_ip_interface_brief_inc_localisisXR.txt (2 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7628 lines)
│   │   │   │   ├── getLocalIpByLocalInterfaceIPV6/
│   │   │   │   │   ├── getLocalIpByLocalInterfaceIPV6.par (57 lines)
│   │   │   │   │   ├── getLocal_xdeIOS.rpl (70 lines)
│   │   │   │   │   ├── iosxeInput.txt (23 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   │   ├── getLocalIpByLocalInterfaceXRIPV6/
│   │   │   │   │   ├── getLocalIpByLocalInterfaceXRIPV6.par (58 lines)
│   │   │   │   │   ├── getLocal_xdeIOS_XR.rpl (70 lines)
│   │   │   │   │   ├── iosxrInput.txt (26 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   │   ├── isis-neighbor/
│   │   │   │   │   ├── iosInput.txt (17 lines)
│   │   │   │   │   ├── iosxrInput.txt (16 lines)
│   │   │   │   │   ├── iosxrInputipv6.txt (14 lines)
│   │   │   │   │   ├── isis-neighbor.par (119 lines)
│   │   │   │   │   ├── isis-neighborParser_xdeIOS.rpl (633 lines)
│   │   │   │   │   ├── isis-neighborParser_xdeIOS_XR.rpl (429 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (5163 lines)
│   │   │   │   ├── isis-neighbor-host/
│   │   │   │   │   ├── iosInput.txt (7 lines)
│   │   │   │   │   ├── iosxrInput.txt (9 lines)
│   │   │   │   │   ├── isis-neighbor-host.par (42 lines)
│   │   │   │   │   ├── isis-neighbor-hostParser_xdeIOS.rpl (126 lines)
│   │   │   │   │   ├── isis-neighbor-hostParser_xdeIOS_XR.rpl (119 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   │   ├── isis-protocol/
│   │   │   │   │   ├── iosInput.txt (76 lines)
│   │   │   │   │   ├── iosxrInput.txt (38 lines)
│   │   │   │   │   ├── isis-protocol.par (103 lines)
│   │   │   │   │   ├── isis-protocolParser_IOS.rpl (143 lines)
│   │   │   │   │   ├── isis-protocolParser_IOS_XR.rpl (143 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (20 lines)
│   │   │   │   └── isis-protocol-ltp/
│   │   │   │       ├── iosInput.txt (69 lines)
│   │   │   │       ├── iosxrInput.txt (60 lines)
│   │   │   │       ├── isis-protocol.par (103 lines)
│   │   │   │       ├── isis-protocolParser_IOS.rpl (185 lines)
│   │   │   │       ├── isis-protocolParser_IOS_XR.rpl (183 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (21 lines)
│   │   │   ├── isis-pep.xpa/
│   │   │   │   ├── isis-pep/
│   │   │   │   │   ├── iosInput.txt (55 lines)
│   │   │   │   │   ├── iosxeinputpassive (11 lines)
│   │   │   │   │   ├── iosxenonpassive (13 lines)
│   │   │   │   │   ├── iosxrInput.txt (49 lines)
│   │   │   │   │   ├── isis-pep.par (127 lines)
│   │   │   │   │   ├── isis-pep_xdeIOS.rpl (862 lines)
│   │   │   │   │   ├── isis-pep_xdeIOS_XR.rpl (359 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7648 lines)
│   │   │   │   └── isis-pep-xe-bfd/
│   │   │   │       ├── iosInput.txt (15 lines)
│   │   │   │       ├── isis-pep-xe-bfd.par (57 lines)
│   │   │   │       ├── isis-pep_xdeIOS.rpl (132 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (7648 lines)
│   │   │   ├── isis-process.xpa/
│   │   │   │   ├── isis-process/
│   │   │   │   │   ├── iosInput.txt (18 lines)
│   │   │   │   │   ├── isis-process.par (119 lines)
│   │   │   │   │   ├── isis-processParser_xdeIOS.rpl (309 lines)
│   │   │   │   │   ├── isis-processParser_xdeIOS_XR.rpl (296 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   │   └── isisProcess-dis/
│   │   │   │       └── isisProcess-dis/
│   │   │   │           ├── iosxrInput.txt (39 lines)
│   │   │   │           ├── isisProcess-dis.par (56 lines)
│   │   │   │           ├── isisProcess-dis_xdeIOS_XR.rpl (115 lines)
│   │   │   │           └── xmp-im-routing-module.xsd (7638 lines)
│   │   │   ├── javascript/
│   │   │   │   ├── getInterfaceFullNames.xjs (26 lines)
│   │   │   │   ├── getIsisPep.xjs (38 lines)
│   │   │   │   └── getIsisXEPepDetailsWithBfd.xjs (42 lines)
│   │   │   ├── test/
│   │   │   │   ├── Isis_Asr903_15.4_Interfaces.xft (956 lines)
│   │   │   │   ├── Isis_Asr903_15.4_Inventory.xft (823 lines)
│   │   │   │   ├── Isis_Asr903_15.4_Neighbors.xft (86 lines)
│   │   │   │   ├── Isis_Asr903_15.4_Process.xft (77 lines)
│   │   │   │   ├── Isis_Asr9k_5.3.1_Interfaces.xft (287 lines)
│   │   │   │   ├── Isis_Asr9k_5.3.1_Inventory.xft (2972 lines)
│   │   │   │   ├── Isis_Asr9k_5.3.1_Neighbors.xft (81 lines)
│   │   │   │   └── Isis_Asr9k_5.3.1_Process.xft (177 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (825 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.inventory.xde.rpd_l2tp/
│   │   │   ├── getCableRPDs/
│   │   │   │   ├── getCableRPDs.par (55 lines)
│   │   │   │   ├── getCableRPDsParserOutput.xsd (6 lines)
│   │   │   │   ├── getCableRPDsParser_xdeIOS.rpl (49 lines)
│   │   │   │   ├── getCableRPDsParser_xdeIOSOutput.xsd (22 lines)
│   │   │   │   └── output1.txt (6 lines)
│   │   │   ├── rtrvL2TPTunnels/
│   │   │   │   ├── output.txt (7 lines)
│   │   │   │   ├── rtrvL2TPTunnels.par (53 lines)
│   │   │   │   ├── rtrvL2TPTunnelsParserOutput.xsd (6 lines)
│   │   │   │   ├── rtrvL2TPTunnelsParser_xdeIOS.rpl (46 lines)
│   │   │   │   └── rtrvL2TPTunnelsParser_xdeIOSOutput.xsd (21 lines)
│   │   │   ├── show_rpd/
│   │   │   │   ├── cable_rpd_transform.par (47 lines)
│   │   │   │   └── transformRPDData.xslt (45 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   ├── prime-cable-resource-model.xsd (540 lines)
│   │   │   ├── procedure.xde (86 lines)
│   │   │   └── xmpxde.xml (35 lines)
│   │   ├── com.cisco.xmp.inventory.xde.xde-OSPF-inventory/
│   │   │   ├── distance.xpa/
│   │   │   │   └── getDistance/
│   │   │   │       ├── getDistance.par (36 lines)
│   │   │   │       ├── getDistanceParser_xdeIOS_XR.rpl (164 lines)
│   │   │   │       ├── output.txt (22 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospf-areaInfo.xpa/
│   │   │   │   └── getOspfAreaInfo/
│   │   │   │       ├── ASR9K_XR.txt (24 lines)
│   │   │   │       ├── ASR9XX_IOS.txt (6 lines)
│   │   │   │       ├── getOspfAreaInfo.par (141 lines)
│   │   │   │       ├── getOspfAreaInfo.rpl (184 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   ├── ospf-borderRouters.xpa/
│   │   │   │   └── getBorderRouter/
│   │   │   │       ├── getBorderRouter.par (56 lines)
│   │   │   │       ├── getBorderRouterParser_xdeIOS_XR.rpl (117 lines)
│   │   │   │       ├── output.txt (41 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospf-neighbor.xpa/
│   │   │   │   └── getOspfNeighbor/
│   │   │   │       ├── getOspfNeighbor.par (36 lines)
│   │   │   │       ├── getOspfNeighborParser_xdeIOS.rpl (347 lines)
│   │   │   │       ├── outputIOS.txt (4 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   ├── ospf-pepsettings.xpa/
│   │   │   │   ├── getLocalRouterIdByInterfaceName/
│   │   │   │   │   ├── getLocalRouterIdByInterfaceName.par (67 lines)
│   │   │   │   │   ├── getLocalRouterIdByInterfaceNameParser_xdeIOS.rpl (97 lines)
│   │   │   │   │   ├── getOspfPepSettingsParser_xdeIOSOutput.xsd (49 lines)
│   │   │   │   │   ├── output.txt (38 lines)
│   │   │   │   │   ├── output2.txt (148 lines)
│   │   │   │   │   └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   │   └── getOspfPepSettings/
│   │   │   │       ├── getOspfPepSettings.par (38 lines)
│   │   │   │       ├── getOspfPepSettingsParser_xdeIOS.rpl (532 lines)
│   │   │   │       ├── getOspfPepSettingsParser_xdeIOSOutput.xsd (49 lines)
│   │   │   │       ├── output.txt (38 lines)
│   │   │   │       ├── output2.txt (148 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   ├── ospf-proccesssettings.xpa/
│   │   │   │   └── getOspfProccessSettings/
│   │   │   │       ├── getOspfProccessSettings.par (73 lines)
│   │   │   │       ├── getOspfProccessSettingsParser_xdeIOS.rpl (321 lines)
│   │   │   │       ├── outputPrio (410 lines)
│   │   │   │       ├── output_iosxe.txt (38 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (34 lines)
│   │   │   ├── ospf-vrf.xpa/
│   │   │   │   └── getOSPFWithVRF/
│   │   │   │       ├── getOSPFWithVRF.par (54 lines)
│   │   │   │       ├── getOSPFWithVRFParserOutput.xsd (6 lines)
│   │   │   │       ├── getOSPFWithVRFParser_xdeIOS_XR.rpl (102 lines)
│   │   │   │       ├── output.txt (51 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (19 lines)
│   │   │   ├── ospfDownInterface.xpa/
│   │   │   │   └── getOspfDownInterface/
│   │   │   │       ├── getOspfDownInterface.par (66 lines)
│   │   │   │       ├── getOspfDownInterfaceParser_xdeIOS_XR.rpl (279 lines)
│   │   │   │       ├── output.txt (134 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospfGlobal.xpa/
│   │   │   │   └── getOspf/
│   │   │   │       ├── getOspf.out.xml (0 lines)
│   │   │   │       ├── getOspf.par (108 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospfGlobalv3.xpa/
│   │   │   │   └── getOspfv3/
│   │   │   │       ├── getOspfv3.par (91 lines)
│   │   │   │       ├── xmp-im-routing-module.xml (1077 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospfNeighborAndInterfaceDetails.xpa/
│   │   │   │   └── getOspfNeighborAndIntfDetails/
│   │   │   │       └── getOspfNeighborAndIntfDetails.par (80 lines)
│   │   │   ├── ospfV3InterfaceDetails.xpa/
│   │   │   │   └── getOspfv3InterfaceDetails/
│   │   │   │       ├── getOspfv3InterfaceDetails.par (36 lines)
│   │   │   │       ├── getOspfv3InterfaceDetailsParser_xdeIOS_XR.rpl (417 lines)
│   │   │   │       ├── output.txt (21 lines)
│   │   │   │       ├── output1.txt (22 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── ospfV3NeighborDetails.xpa/
│   │   │   │   └── getOspfv3NeighborDetails/
│   │   │   │       ├── getOspfv3NeighborDetails.par (37 lines)
│   │   │   │       ├── getOspfv3NeighborDetailsParser_xdeIOS_XR.rpl (156 lines)
│   │   │   │       ├── output.txt (17 lines)
│   │   │   │       ├── output1.txt (88 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (4108 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── Ospfprocedure.xde (2287 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── com.cisco.xmp.inventory.xde.xde-l2vpn-pseudowire-headend-inventory/
│   │   │   ├── cisco-pwhe-getgenericiflistinfo-cli.xpa/
│   │   │   │   └── getGenericIfList/
│   │   │   │       ├── SampledeviceoutputGenIfList.txt (20 lines)
│   │   │   │       ├── getGenericIfList.par (27 lines)
│   │   │   │       ├── getGenericIfListParser_xdeIOS_XR.rpl (70 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── cisco-pwhe-getpwheadendinfo-cli.xpa/
│   │   │   │   └── getPWHeadEndInfo/
│   │   │   │       ├── getPWHeadEndInfo.par (26 lines)
│   │   │   │       ├── getPWHeadEndInfoParser_xdeIOS_XR.rpl (127 lines)
│   │   │   │       ├── sampleDeviceOutputIOS_XR (41 lines)
│   │   │   │       └── xmp-im-carrier-ethernet-module.xsd (873 lines)
│   │   │   ├── test/
│   │   │   │   ├── PWHE_ASR9006_XR520_AllGenericInterfaceList.xft (73 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_AllInterfaceDownt.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_ChangeBandwidth.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_ChangeL2Overhead.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_ChangeMAC.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_ChangeMTU.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_Inventoryt.xft (273 lines)
│   │   │   │   ├── PWHE_ASR9006_XR520_PWHEInterfaceDown.xft (271 lines)
│   │   │   │   └── PWHE_ASR9006_XR520_WithBundleGenericInterface.xft (273 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── pwheinventoryprocedure.xde (22 lines)
│   │   │   └── xmpxde.xml (41 lines)
│   │   ├── com.cisco.xmp.inventrory.xde.xde-OSPF-inventory-IOS-XE/
│   │   │   ├── ospf-neighbor.xpa/
│   │   │   │   └── getOspfNeighbor/
│   │   │   │       ├── getOspfNeighbor.par (26 lines)
│   │   │   │       ├── getOspfNeighborParser_xdeIOS.rpl (140 lines)
│   │   │   │       ├── outputIOS.txt (4 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   ├── ospf-pepsettings.xpa/
│   │   │   │   └── getOspfPepSettings/
│   │   │   │       ├── getOspfPepSettings.par (26 lines)
│   │   │   │       ├── getOspfPepSettingsParser_xdeIOS.rpl (304 lines)
│   │   │   │       ├── getOspfPepSettingsParser_xdeIOSOutput.xsd (49 lines)
│   │   │   │       ├── output.txt (38 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (5173 lines)
│   │   │   ├── ospf-proccesssettings.xpa/
│   │   │   │   └── getOspfProccessSettings/
│   │   │   │       ├── getOspfProccessSettings.par (28 lines)
│   │   │   │       ├── getOspfProccessSettingsParser_xdeIOS.rpl (136 lines)
│   │   │   │       ├── output_iosxe.txt (38 lines)
│   │   │   │       └── xmp-im-routing-module.xsd (20 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (66 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ethernetFlowPoint_me1200_inventory/
│   │   │   ├── getEVCDetails/
│   │   │   │   ├── getEVCDetails.par (51 lines)
│   │   │   │   ├── getEVCDetailsParser_xdeME1200_OS.rpl (414 lines)
│   │   │   │   └── getEVCDetailsParser_xdeME1200_OSOutput.xsd (42 lines)
│   │   │   ├── getEntityMib/
│   │   │   │   ├── getEntityMib.map (11 lines)
│   │   │   │   ├── getEntityMib.par (59 lines)
│   │   │   │   └── getEntityMibOutput.xsd (29 lines)
│   │   │   ├── getInterfaceSatus/
│   │   │   │   ├── getInterfaceSatus.par (51 lines)
│   │   │   │   ├── getInterfaceSatusParserOutput.xsd (6 lines)
│   │   │   │   ├── getInterfaceSatusParser_xdeME1200_OS.rpl (48 lines)
│   │   │   │   └── getInterfaceSatusParser_xdeME1200_OSOutput.xsd (23 lines)
│   │   │   ├── getiftable/
│   │   │   │   ├── getiftable.map (20 lines)
│   │   │   │   ├── getiftable.par (67 lines)
│   │   │   │   ├── ifm-im-connectivity-ext-module.xsd (2957 lines)
│   │   │   │   ├── output.txt (2383 lines)
│   │   │   │   └── xmp-im-connectivity-module.xsd (663 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── getEFPMatchType.xjs (42 lines)
│   │   │   ├── getEthernetSubInterfaceAddAttr.xjs (78 lines)
│   │   │   ├── getInterfaceRangeAdditionalObject.xjs (99 lines)
│   │   │   ├── getVlanTagHandling.xjs (32 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (474 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── ethernet_interfaces_me1200/
│   │   │   ├── l2interface.xpa/
│   │   │   │   └── getiftable/
│   │   │   │       ├── getiftable.map (25 lines)
│   │   │   │       ├── getiftable.par (67 lines)
│   │   │   │       ├── ifm-im-connectivity-ext-module.xsd (2957 lines)
│   │   │   │       ├── output.txt (2383 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (663 lines)
│   │   │   ├── portGroup.xpa/
│   │   │   │   └── getPortGroup/
│   │   │   │       ├── getPortGroup.map (13 lines)
│   │   │   │       ├── getPortGroup.par (57 lines)
│   │   │   │       ├── ifm-im-connectivity-ext-module.xsd (2957 lines)
│   │   │   │       ├── output.txt (323 lines)
│   │   │   │       └── xmp-im-connectivity-module.xsd (663 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l2interface.xde (124 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── l3link-bgp-config/
│   │   │   ├── l3link-Bgp-config.xpa/
│   │   │   │   ├── l3linkBgpCreateAndUpdateWriter/
│   │   │   │   │   ├── iosXE.vtl (120 lines)
│   │   │   │   │   ├── iosXR.vtl (112 lines)
│   │   │   │   │   └── l3vpnBgpCreateAndUpdateWriter.par (71 lines)
│   │   │   │   ├── l3linkBgpDeleteWriter/
│   │   │   │   │   ├── iosXE.vtl (113 lines)
│   │   │   │   │   ├── iosXR.vtl (119 lines)
│   │   │   │   │   └── l3vpnBgpDeleteWriter.par (71 lines)
│   │   │   │   └── xmp-im-routing-module.xsd (3387 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── l3linkBgpCreateProcedure.xde (42 lines)
│   │   │   ├── l3linkBgpDeleteProcedure.xde (41 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── l3link-isis-config/
│   │   │   ├── routing-isis-config.xpa/
│   │   │   │   ├── isisCreateAndUpdateWriter/
│   │   │   │   │   ├── ios.vtl (118 lines)
│   │   │   │   │   ├── iosXR.vtl (131 lines)
│   │   │   │   │   └── isisCreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── isisDeleteWriter/
│   │   │   │   │   ├── ios.vtl (136 lines)
│   │   │   │   │   ├── iosXR.vtl (128 lines)
│   │   │   │   │   ├── iosXR_2.vtl (33 lines)
│   │   │   │   │   └── isisDeleteWriter.par (28 lines)
│   │   │   │   ├── xmp-im-routing-module.xsd (4349 lines)
│   │   │   │   └── xmp-im-routing-module.xsd.bckp (3417 lines)
│   │   │   ├── conf.xml (5 lines)
│   │   │   ├── isisCreateProcedure.xde (14 lines)
│   │   │   ├── isisDeleteProcedure.xde (20 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (20 lines)
│   │   ├── l3vpn_config_change_bgp_inventory/
│   │   │   ├── l3vpn-bgp/
│   │   │   │   ├── l3vpn-bgp.par (91 lines)
│   │   │   │   ├── l3vpn-bgpParserOutput.xsd (6 lines)
│   │   │   │   ├── l3vpn-bgpParser_xdeIOS.rpl (328 lines)
│   │   │   │   ├── l3vpn-bgpParser_xdeIOS_XR.rpl (590 lines)
│   │   │   │   ├── l3vpn-bgpParser_xdeIOS_XROutput.xsd (48 lines)
│   │   │   │   └── sh_config_commit_changes_last.txt (14 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3vpnBgpConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── l3vpn_config_change_vrf_inventory/
│   │   │   ├── l3vpn-vrf/
│   │   │   │   ├── l3vpn-vrf.par (91 lines)
│   │   │   │   ├── l3vpn-vrfParserOutput.xsd (6 lines)
│   │   │   │   ├── l3vpn-vrfParser_xdeIOS.rpl (541 lines)
│   │   │   │   ├── l3vpn-vrfParser_xdeIOSOutput.xsd (51 lines)
│   │   │   │   ├── l3vpn-vrfParser_xdeIOS_XR.rpl (1039 lines)
│   │   │   │   ├── l3vpn-vrfParser_xdeIOS_XROutput.xsd (50 lines)
│   │   │   │   ├── showArchieveForBDIChanges.txt (12 lines)
│   │   │   │   ├── show_archive_log_config_all.txt (1002 lines)
│   │   │   │   ├── show_config_commit_changes_last.txt (14 lines)
│   │   │   │   └── show_config_commit_changes_last1.txt (16 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── l3vpnVrfConfigChangeProcedure.xde (24 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ldp_config_change_ios_xde/
│   │   │   ├── get_ConfigChange_ldp_details.xpa/
│   │   │   │   ├── get_ConfigChange_ldp_details/
│   │   │   │   │   ├── get_ConfigChange_ldp_details.par (50 lines)
│   │   │   │   │   ├── get_ConfigChange_ldp_detailsParserOutput.xsd (39 lines)
│   │   │   │   │   └── get_ConfigChange_ldp_detailsParser_xdeIOS.rpl (270 lines)
│   │   │   │   └── config (16 lines)
│   │   │   ├── .project (30 lines)
│   │   │   ├── ldp_procedure.xde (22 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── ldp_config_change_iosxr_xde/
│   │   │   ├── get_ConfigChange_ldp_details.xpa/
│   │   │   │   ├── get_ConfigChange_ldp_details/
│   │   │   │   │   ├── get_ConfigChange_ldp_details.par (50 lines)
│   │   │   │   │   ├── get_ConfigChange_ldp_detailsParserOutput.xsd (38 lines)
│   │   │   │   │   └── get_ConfigChange_ldp_detailsParser_xdeIOSXR.rpl (206 lines)
│   │   │   │   └── config (18 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── ldp_procedure.xde (22 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (19 lines)
│   │   ├── lspAttrList_config_change/
│   │   │   ├── get_LspAttributeList_ConfigChange.xpa/
│   │   │   │   └── get_LspAttributeList_ConfigChange/
│   │   │   │       ├── XEOutput.txt (13 lines)
│   │   │   │       ├── XROutput.txt (10 lines)
│   │   │   │       ├── get_LspAttributeList_ConfigChange_details.par (91 lines)
│   │   │   │       ├── get_LspAttributeList_ConfigChange_details.xsd (23 lines)
│   │   │   │       ├── get_LspAttributeList_ConfigChange_details_IOS.rpl (60 lines)
│   │   │   │       └── get_LspAttributeList_ConfigChange_details_IOSXR.rpl (69 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── procedure.xde (22 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── mpls_config_change_ios_xde/
│   │   │   ├── get_ConfigChange_mplste_details.xpa/
│   │   │   │   ├── get_ConfigChange_mplste_details/
│   │   │   │   │   ├── ExplicitPath_IOS_XE (63 lines)
│   │   │   │   │   ├── ExplicitPath_IOS_XR (52 lines)
│   │   │   │   │   ├── get_ConfigChange_mplste_details.par (91 lines)
│   │   │   │   │   ├── get_ConfigChange_mplste_detailsParserOutput.xsd (59 lines)
│   │   │   │   │   ├── get_ConfigChange_mplste_detailsParser_xdeIOS.rpl (461 lines)
│   │   │   │   │   └── get_ConfigChange_mplste_detailsParser_xdeIOSXR.rpl (364 lines)
│   │   │   │   └── config (21 lines)
│   │   │   ├── mplste_procedure.xde (23 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── powerSupplyFanStatus_generic_inventory/
│   │   │   ├── fanStatus.xpa/
│   │   │   │   └── getFanStatus/
│   │   │   │       ├── getFanStatus.map (15 lines)
│   │   │   │       ├── getFanStatus.par (55 lines)
│   │   │   │       ├── output.txt (885 lines)
│   │   │   │       └── xmp-im-physical-resource-module.xsd (602 lines)
│   │   │   ├── powerSupply.xpa/
│   │   │   │   └── getPowerSupplyStatus/
│   │   │   │       ├── getPowerSupplyStatus.map (14 lines)
│   │   │   │       ├── getPowerSupplyStatus.par (55 lines)
│   │   │   │       ├── output.txt (885 lines)
│   │   │   │       └── xmp-im-physical-resource-module.xsd (602 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── powerSupplyFanStatus.xde (71 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── srpolicy_config_change/
│   │   │   ├── getSRPolicy.xpa/
│   │   │   │   └── getSRPolicy/
│   │   │   │       ├── ODNPolicyXE.txt (57 lines)
│   │   │   │       ├── getSRPolicy.par (90 lines)
│   │   │   │       ├── getSRPolicy.rpl (1453 lines)
│   │   │   │       ├── getSRPolicy.xsd (91 lines)
│   │   │   │       ├── getSRPolicyXE.rpl (1150 lines)
│   │   │   │       ├── odnPolicy.txt (60 lines)
│   │   │   │       ├── output.txt (80 lines)
│   │   │   │       └── outputXE.txt (72 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (22 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── vlan_me1200_inventory/
│   │   │   ├── VLANSwitchportSettings/
│   │   │   │   ├── VLANSwitchportSettings.par (53 lines)
│   │   │   │   ├── VLANSwitchportSettingsParser_xdeME1200_OS.rpl (134 lines)
│   │   │   │   ├── output_me1200 (271 lines)
│   │   │   │   └── xmp-im-vlan-module.xsd (28 lines)
│   │   │   ├── VLANTrunkingSettings/
│   │   │   │   ├── VLANTrunkingSettings.par (53 lines)
│   │   │   │   ├── VLANTrunkingSettingsParser_xdeME1200_OS.rpl (126 lines)
│   │   │   │   ├── output_me1200 (271 lines)
│   │   │   │   └── xmp-im-vlan-module.xsd (38 lines)
│   │   │   ├── getGVRPStatus/
│   │   │   │   ├── getGVRPStatus.par (51 lines)
│   │   │   │   ├── getGVRPStatusParser_xdeME1200_OS.rpl (103 lines)
│   │   │   │   ├── output1 (70 lines)
│   │   │   │   └── xmp-im-vlan-module.xsd (25 lines)
│   │   │   ├── getHybridVlanPortSettings/
│   │   │   │   ├── getHybridVlanPortSettings.par (53 lines)
│   │   │   │   ├── getHybridVlanPortSettingsParser_xdeME1200_OS.rpl (230 lines)
│   │   │   │   └── prime-ethernet-resource-model.xsd (30 lines)
│   │   │   ├── getInterfaceStatus/
│   │   │   │   ├── getInterfaceStatus.par (51 lines)
│   │   │   │   ├── getInterfaceStatusParser_xdeME1200_OS.rpl (49 lines)
│   │   │   │   ├── output1 (8 lines)
│   │   │   │   └── xmp-im-vlan-module.xsd (25 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── procedure.xde (145 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── xde-lag-asr9k_901_903/
│   │   │   ├── getIfSpeedXE/
│   │   │   │   ├── getIfSpeedXE.par (53 lines)
│   │   │   │   ├── getIfSpeedXEParserOutput.xsd (6 lines)
│   │   │   │   ├── getIfSpeedXEParser_xdeIOS.rpl (150 lines)
│   │   │   │   └── getIfSpeedXEParser_xdeIOSOutput.xsd (20 lines)
│   │   │   ├── getLagIndex.xpa/
│   │   │   │   └── getLagIndexes/
│   │   │   │       ├── ASR901.txt (3 lines)
│   │   │   │       ├── getIfindexParserOutput.xsd (18 lines)
│   │   │   │       ├── getLagIndex_xde.rpl (82 lines)
│   │   │   │       └── getLagIndexes.par (56 lines)
│   │   │   ├── getXELacpMemberPorts.xpa/
│   │   │   │   └── getXELacpMemberPorts/
│   │   │   │       ├── ASR901.txt (11 lines)
│   │   │   │       ├── getXELacpMemberPorts.par (56 lines)
│   │   │   │       ├── getXELacpMemberPorts.rpl (121 lines)
│   │   │   │       ├── getXELacpMemberPortsOutput.xsd (4 lines)
│   │   │   │       ├── getXELacpMemberPorts_ouput.xsd (18 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (834 lines)
│   │   │   ├── lag_interface.xpa/
│   │   │   │   └── getLAGInterfaces/
│   │   │   │       ├── ASR901.txt (22 lines)
│   │   │   │       ├── ASR902.txt (27 lines)
│   │   │   │       ├── ASR920.txt (25 lines)
│   │   │   │       ├── ASR920New.txt (36 lines)
│   │   │   │       ├── ASR9k.txt (455 lines)
│   │   │   │       ├── ASR9k_17.txt (151 lines)
│   │   │   │       ├── ASR9k_18.txt (1634 lines)
│   │   │   │       ├── ASR9k_new.txt (2908 lines)
│   │   │   │       ├── ASR9knew.txt (1439 lines)
│   │   │   │       ├── ME3600.txt (21 lines)
│   │   │   │       ├── ME3800.txt (25 lines)
│   │   │   │       ├── asr903.txt (33 lines)
│   │   │   │       ├── getLAGInterfaces.par (103 lines)
│   │   │   │       ├── getLAGInterfacesParser_xde.rpl (1734 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (834 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── lagInventoryProcedure.xde (134 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── xde-lag-me36_38/
│   │   │   ├── etherChannelCLI.xpa/
│   │   │   │   └── getetherChannelCLI/
│   │   │   │       ├── ME3600.txt (176 lines)
│   │   │   │       ├── getetherChannelCLI.par (24 lines)
│   │   │   │       ├── getetherChannelCLIParserOutput.xsd (6 lines)
│   │   │   │       ├── getetherChannelCLIParser_xdeIOS.rpl (775 lines)
│   │   │   │       ├── getetherChannelCLIParser_xdeIOSOutput.xsd (55 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (819 lines)
│   │   │   ├── interfaceControlMethod.xpa/
│   │   │   │   └── getControlMethod/
│   │   │   │       ├── ME3600.txt (21 lines)
│   │   │   │       ├── ME3800.txt (21 lines)
│   │   │   │       ├── getControlMethod.par (26 lines)
│   │   │   │       ├── getControlMethodParser_xde.rpl (155 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (819 lines)
│   │   │   ├── lag8023actordetail.xpa/
│   │   │   │   └── getActorDetails/
│   │   │   │       ├── 3800.txt (37 lines)
│   │   │   │       ├── getActorDetails.par (24 lines)
│   │   │   │       ├── getActorDetailsParserOutput.xsd (6 lines)
│   │   │   │       ├── getActorDetailsParser_xdeIOS.rpl (205 lines)
│   │   │   │       ├── getActorDetailsParser_xdeIOSOutput.xsd (29 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (819 lines)
│   │   │   ├── lag8023partnerdatail.xpa/
│   │   │   │   └── getPartnerdetail/
│   │   │   │       ├── ME3600.txt (37 lines)
│   │   │   │       ├── getPartnerdetail.par (24 lines)
│   │   │   │       ├── getPartnerdetailParserOutput.xsd (6 lines)
│   │   │   │       ├── getPartnerdetailParser_xdeIOS.rpl (242 lines)
│   │   │   │       └── getPartnerdetailParser_xdeIOSOutput.xsd (31 lines)
│   │   │   ├── lagBaseAggPort.xpa/
│   │   │   │   └── getLagBaseAggPort/
│   │   │   │       ├── getLagBaseAggPort.map (16 lines)
│   │   │   │       ├── getLagBaseAggPort.par (29 lines)
│   │   │   │       └── xmp-im-link-aggregation-module.xsd (819 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── linkaggregation.xde (429 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   ├── xmp-im-link-aggregation-module.xsd (809 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── xmp-im-global-bfd-config/
│   │   │   ├── global-bfd-config.xpa/
│   │   │   │   ├── globalbfd_CreateAndUpdateWriter/
│   │   │   │   │   ├── globalbfd_CreateAndUpdateWriter.par (40 lines)
│   │   │   │   │   └── iosxe.vtl (13 lines)
│   │   │   │   ├── globalbfd_DeleteWriter/
│   │   │   │   │   ├── globalbfd_DeleteWriter.par (40 lines)
│   │   │   │   │   └── iosxe.vtl (5 lines)
│   │   │   │   └── testFromNMS/
│   │   │   │       └── NCS42xx/
│   │   │   │           ├── NCS42xxConfig.xft (29 lines)
│   │   │   │           └── NCS42xxDelete.xft (24 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── global-bfd_CreateProcedure.xde (15 lines)
│   │   │   ├── global-bfd_DeleteProcedure.xde (15 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── xmp-im-mpls-te-module-config/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.config.xde/
│   │   │   │   │       └── xmp-im-mpls-te-module-config/
│   │   │   │   │           ├── pom.properties (5 lines)
│   │   │   │   │           └── pom.xml (57 lines)
│   │   │   │   └── MANIFEST.MF (6 lines)
│   │   │   ├── mpls-te-module-config.xpa/
│   │   │   │   ├── mplstetunnel_CreateAndUpdateWriter/
│   │   │   │   │   ├── iosxe.vtl (308 lines)
│   │   │   │   │   ├── iosxr.vtl (263 lines)
│   │   │   │   │   └── mplstetunnel_CreateAndUpdateWriter.par (74 lines)
│   │   │   │   ├── mplstetunnel_DeleteWriter/
│   │   │   │   │   ├── iosxe.vtl (112 lines)
│   │   │   │   │   ├── iosxr.vtl (144 lines)
│   │   │   │   │   └── mplstetunnel_DeleteWriter.par (28 lines)
│   │   │   │   └── testFromNMS/
│   │   │   │       ├── NCS42xx/
│   │   │   │       │   ├── ExplicitPath.xft (43 lines)
│   │   │   │       │   ├── ExplicitPathDelete.xft (200 lines)
│   │   │   │       │   ├── NCS42xxConfig.xft (38 lines)
│   │   │   │       │   └── NCS42xxDelete.xft (20 lines)
│   │   │   │       └── NCS4k/
│   │   │   │           ├── ExplicitPath.xft (195 lines)
│   │   │   │           ├── NCS4kConfig.xft (36 lines)
│   │   │   │           └── NCS4kDelete.xft (28 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── error.xml (4 lines)
│   │   │   ├── excludeAssociations.xml (6 lines)
│   │   │   ├── mpls-te-tunnel_CreateProcedure.xde (19 lines)
│   │   │   ├── mpls-te-tunnel_DeleteProcedure.xde (14 lines)
│   │   │   ├── packageDescriptor.xml (11 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── xmp-im-mpls-te-module-inventory/
│   │   │   ├── IFmib.xpa/
│   │   │   │   └── getIfTable/
│   │   │   │       ├── getIfTable.map (11 lines)
│   │   │   │       ├── getIfTable.par (54 lines)
│   │   │   │       ├── getIfTableOutput.xsd (32 lines)
│   │   │   │       └── snmpOutput.txt (122 lines)
│   │   │   ├── isis.xpa/
│   │   │   │   ├── getISISInterface/
│   │   │   │   │   ├── getISISInterface.par (153 lines)
│   │   │   │   │   ├── getMplsInterfaceParser_xdeIOS.rpl (832 lines)
│   │   │   │   │   ├── getMplsInterfaceParser_xdeIOSOutput.xsd (20 lines)
│   │   │   │   │   └── getMplsInterfaceParser_xdeIOS_XR.rpl (283 lines)
│   │   │   │   ├── getISISNeighborInfo/
│   │   │   │   │   ├── IsisNeighborIOS (3 lines)
│   │   │   │   │   ├── IsisNeighborXR (11 lines)
│   │   │   │   │   ├── getISISNeighborInfo.par (103 lines)
│   │   │   │   │   ├── getISISNeighborInfoParser_xdeIOS.rpl (60 lines)
│   │   │   │   │   ├── getISISNeighborInfoParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   │   └── getISISNeighborInfoParser_xdeIOS_XR.rpl (61 lines)
│   │   │   │   ├── getISISRouterId/
│   │   │   │   │   ├── ISISRouterId32XE (61 lines)
│   │   │   │   │   ├── ISISRouterIdXR (135 lines)
│   │   │   │   │   ├── getISISRouterId.par (53 lines)
│   │   │   │   │   ├── getISISRouterIdParserOutput.xsd (6 lines)
│   │   │   │   │   └── getISISRouterIdParser_xdeIOS.rpl (96 lines)
│   │   │   │   ├── getISSITeDetails/
│   │   │   │   │   ├── ISISRouterIdXE (42 lines)
│   │   │   │   │   ├── ISISRouterIdXR (50 lines)
│   │   │   │   │   ├── getISSITeDetails.par (99 lines)
│   │   │   │   │   ├── getISSITeDetailsParserOutput.xsd (19 lines)
│   │   │   │   │   ├── getISSITeDetailsParser_xdeIOS.rpl (125 lines)
│   │   │   │   │   ├── getISSITeDetailsParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   │   ├── getISSITeDetailsParser_xdeIOS_XR.rpl (124 lines)
│   │   │   │   │   ├── getISSITeDetailsParser_xdeIOS_XROutput.xsd (11 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1631 lines)
│   │   │   │   ├── isisLinkProcedure.xde (237 lines)
│   │   │   │   └── isisTeSettingsProcedure.xde (32 lines)
│   │   │   ├── mplsOspfProcessTeSettings.xpa/
│   │   │   │   ├── getLoopback/
│   │   │   │   │   ├── getLoopback.par (151 lines)
│   │   │   │   │   ├── getLoopbackParser_xdeIOS.rpl (56 lines)
│   │   │   │   │   ├── getLoopbackParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   │   └── getLoopbackParser_xdeIOS_XR.rpl (56 lines)
│   │   │   │   └── getOspfProcessId/
│   │   │   │       ├── getOspfProcessId.par (99 lines)
│   │   │   │       ├── getOspfProcessIdParser_xdeIOS.rpl (105 lines)
│   │   │   │       ├── getOspfProcessIdParser_xdeIOSOutput.xsd (18 lines)
│   │   │   │       └── getOspfProcessIdParser_xdeIOS_XR.rpl (105 lines)
│   │   │   ├── mplsProtocolEndpoint.xpa/
│   │   │   │   ├── getMplsLockOut/
│   │   │   │   │   ├── NCS4000_LockOut (570 lines)
│   │   │   │   │   ├── NCS4200_Lockout.txt (106 lines)
│   │   │   │   │   ├── getMplsLockOut.par (121 lines)
│   │   │   │   │   ├── getMplsLockOutParser_xdeIOS.rpl (265 lines)
│   │   │   │   │   ├── getMplsLockOutParser_xdeIOS_XR.rpl (141 lines)
│   │   │   │   │   └── xmp-im-mpls-module.xsd (328 lines)
│   │   │   │   └── getMplsPeP/
│   │   │   │       ├── getMplsPEP.map (33 lines)
│   │   │   │       ├── getMplsPeP.par (31 lines)
│   │   │   │       └── xmp-im-mpls-module.xsd (323 lines)
│   │   │   ├── mplsXEStandbyConfig.xpa/
│   │   │   │   └── getMplsXEStandbyConfig/
│   │   │   │       ├── 10.56.23.109-Standby-LSP-Output.txt (181 lines)
│   │   │   │       ├── 10.56.23.116-Standby-LSP-Output.txt (185 lines)
│   │   │   │       ├── 42xx_unidir_protection (26 lines)
│   │   │   │       ├── Standby.txt (273 lines)
│   │   │   │       ├── getMplsXEStandbyConfig.par (65 lines)
│   │   │   │       ├── getMplsXEStandbyConfigParser_xdeIOS.rpl (642 lines)
│   │   │   │       ├── protection-32.txt (135 lines)
│   │   │   │       └── xmp-im-mpls-te-module.xsd (1719 lines)
│   │   │   ├── test/
│   │   │   │   ├── isisInventory/
│   │   │   │   │   ├── getISISInterfaceXE.xft (35 lines)
│   │   │   │   │   ├── getISISInterfaceXR.xft (36 lines)
│   │   │   │   │   ├── getISISNeighborInfoXE.xft (28 lines)
│   │   │   │   │   ├── getISISNeighborInfoXR.xft (45 lines)
│   │   │   │   │   ├── getISISRouterIdXE.xft (384 lines)
│   │   │   │   │   ├── getISISRouterIdXR.xft (329 lines)
│   │   │   │   │   ├── getISSITeDetailsXE.xft (49 lines)
│   │   │   │   │   └── getISSITeDetailsXR.xft (50 lines)
│   │   │   │   ├── mplsModuleInventory/
│   │   │   │   │   ├── getMplsInterfaceXE.xft (30 lines)
│   │   │   │   │   ├── getMplsInterfaceXR.xft (31 lines)
│   │   │   │   │   ├── getMplsSystemIdXE.xft (45 lines)
│   │   │   │   │   ├── getMplsSystemIdXR.xft (58 lines)
│   │   │   │   │   ├── getMplsTrafficEngXE.xft (41 lines)
│   │   │   │   │   ├── getMplsTrafficEngXR.xft (84 lines)
│   │   │   │   │   ├── getXmp-im-mpls-moduleXE.xft (52 lines)
│   │   │   │   │   └── getXmp-im-mpls-moduleXR.xft (41 lines)
│   │   │   │   ├── mplsTEInventory/
│   │   │   │   │   ├── getDownTunnelSrcInfoXE.xft (63 lines)
│   │   │   │   │   ├── getDownTunnelSrcInfoXR-V6.3.2.xft (51 lines)
│   │   │   │   │   ├── getDownTunnelSrcInfoXR.xft (58 lines)
│   │   │   │   │   ├── getDownTunnelsDestInfoXE.xft (173 lines)
│   │   │   │   │   ├── getDownTunnelsDestInfoXR.xft (286 lines)
│   │   │   │   │   ├── getIfIndexTableDetail.xft (54 lines)
│   │   │   │   │   ├── getIfIndexTableXE.xft (98 lines)
│   │   │   │   │   ├── getIfIndexTableXR.xft (43 lines)
│   │   │   │   │   ├── getMplsLockOutXE.xft (202 lines)
│   │   │   │   │   ├── getMplsLockOutXR.xft (455 lines)
│   │   │   │   │   ├── getMplsPEPIfIndex.xft (33 lines)
│   │   │   │   │   ├── getMplsTeTunnelDestPOLspAttrXE.xft (38 lines)
│   │   │   │   │   ├── getMplsTeTunnelDestPOLspAttrXR.xft (80 lines)
│   │   │   │   │   ├── getMplsTeTunnelExplicitpathXE.xft (75 lines)
│   │   │   │   │   ├── getMplsTeTunnelExplicitpathXR.xft (109 lines)
│   │   │   │   │   ├── getMplsTeTunnelPEPInfoXE.xft (33 lines)
│   │   │   │   │   ├── getMplsTeTunnelPEPInfoXR.xft (32 lines)
│   │   │   │   │   ├── getMplsTeTunnelPEPStatusInfoXE.xft (79 lines)
│   │   │   │   │   ├── getMplsTeTunnelPEPStatusInfoXR.xft (87 lines)
│   │   │   │   │   ├── getMplsTeTunnelSettingsAvailableBandwidthInfo.xft (50 lines)
│   │   │   │   │   ├── getMplsTeTunnelSettingsXE.xft (76 lines)
│   │   │   │   │   ├── getMplsTeTunnelSettingsXR.xft (64 lines)
│   │   │   │   │   ├── getMplsXEStandbyConfig.xft (64 lines)
│   │   │   │   │   ├── getPEPStatusForNonDynamic.xft (143 lines)
│   │   │   │   │   ├── getXmp-im-mpls-te-moduleXE.xft (246 lines)
│   │   │   │   │   └── getXmp-im-mpls-te-moduleXR.xft (254 lines)
│   │   │   │   └── ospfInventory/
│   │   │   │       ├── getLoopbackXE.xft (46 lines)
│   │   │   │       ├── getLoopbackXR.xft (71 lines)
│   │   │   │       ├── getOspfProcessIdXE.xft (44 lines)
│   │   │   │       └── getOspfProcessIdXR.xft (57 lines)
│   │   │   ├── xmp-im-mpls-module-inventory.xpa/
│   │   │   │   └── xmp-im-mpls-module/
│   │   │   │       ├── asr907-mplsinterfaces.txt (73 lines)
│   │   │   │       ├── xmp-im-mpls-module.par (99 lines)
│   │   │   │       ├── xmp-im-mpls-module.xsd (323 lines)
│   │   │   │       ├── xmp-im-mpls-moduleParser_xdeIOS.rpl (318 lines)
│   │   │   │       └── xmp-im-mpls-moduleParser_xdeIOS_XR.rpl (362 lines)
│   │   │   ├── xmp-im-mpls-te-module-inventory.xpa/
│   │   │   │   ├── downTunnelSrcInfo/
│   │   │   │   │   ├── downTunnelSrcInfo.par (172 lines)
│   │   │   │   │   ├── downTunnelSrcInfoParser_xdeIOS.rpl (71 lines)
│   │   │   │   │   ├── downTunnelSrcInfoParser_xdeIOS_XR.rpl (71 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1321 lines)
│   │   │   │   ├── downTunnelsDestInfo/
│   │   │   │   │   ├── downTunnelsDestInfo.par (110 lines)
│   │   │   │   │   ├── downTunnelsDestInfoParser_xdeIOS.rpl (79 lines)
│   │   │   │   │   ├── downTunnelsDestInfoParser_xdeIOS_XR.rpl (80 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1321 lines)
│   │   │   │   ├── ifIndexTable/
│   │   │   │   │   ├── idIndexTable_IOS_XR_FULLConfig.txt (122 lines)
│   │   │   │   │   ├── ifIndexTable.par (105 lines)
│   │   │   │   │   ├── ifIndexTableParser_xdeIOS.rpl (197 lines)
│   │   │   │   │   ├── ifIndexTableParser_xdeIOS_XR.rpl (206 lines)
│   │   │   │   │   ├── ifIndexTableParser_xdeIOS_XROutput.xsd (64 lines)
│   │   │   │   │   ├── ifIndexTable_IOS.txt (25 lines)
│   │   │   │   │   ├── ifIndexTable_IOS_FullConfig.txt (49 lines)
│   │   │   │   │   ├── ifIndexTable_IOS_XR.txt (122 lines)
│   │   │   │   │   └── ifIndex_FULLIOS_XR.txt (134 lines)
│   │   │   │   ├── ifIndexTableDetail/
│   │   │   │   │   ├── ifIndexTableDetail.par (58 lines)
│   │   │   │   │   ├── ifIndexTableDetailParser_xdeIOS.rpl (90 lines)
│   │   │   │   │   └── ifIndexTableDetail_IOS.txt (14 lines)
│   │   │   │   ├── mplsPEPIfIndex/
│   │   │   │   │   ├── mplsPEPIfIndex.par (59 lines)
│   │   │   │   │   ├── mplsPEPIfIndexParser_xdeIOS.rpl (69 lines)
│   │   │   │   │   ├── mplsPEPIfIndexParser_xdeIOS_XR.rpl (3 lines)
│   │   │   │   │   ├── mplsPepIfindex_IOS.txt (1 lines)
│   │   │   │   │   └── xmp-im-mpls-module.xsd (169 lines)
│   │   │   │   ├── mplsTeTunnelDestPOLspAttr/
│   │   │   │   │   ├── mplsTeTunnelDestPOLspAttr.par (99 lines)
│   │   │   │   │   ├── mplsTeTunnelDestPOLspAttrParser_xdeIOS.rpl (175 lines)
│   │   │   │   │   ├── mplsTeTunnelDestPOLspAttrParser_xdeIOS_XR.rpl (103 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1690 lines)
│   │   │   │   ├── mplsTeTunnelExplicitpath/
│   │   │   │   │   ├── mplsTeTunnelExplicitpath.par (120 lines)
│   │   │   │   │   ├── mplsTeTunnelExplicitpathParser_xdeIOS.rpl (281 lines)
│   │   │   │   │   ├── mplsTeTunnelExplicitpathParser_xdeIOS_XR.rpl (280 lines)
│   │   │   │   │   ├── xmp-im-mpls-te-module.xsd (1676 lines)
│   │   │   │   │   └── xr_expathentry.txt (38 lines)
│   │   │   │   ├── mplsTeTunnelPEPInfo/
│   │   │   │   │   ├── ifIndexInfo_IOS.txt (2 lines)
│   │   │   │   │   ├── ifIndexInfo_IOS_FULLInv.txt (4 lines)
│   │   │   │   │   ├── ifIndexInfo_IOS_XR.txt (2 lines)
│   │   │   │   │   ├── ifIndexInfo_IOS_XR_FULLInv.txt (22 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPInfo.par (107 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPInfoParser_xdeIOS.rpl (69 lines)
│   │   │   │   │   └── mplsTeTunnelPEPInfoParser_xdeIOS_XR.rpl (69 lines)
│   │   │   │   ├── mplsTeTunnelPEPStatusForNonDynamic/
│   │   │   │   │   ├── mplsTeTunnelPEPStatusForNonDynamic.par (109 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPStatusForNonDynamicParser_xdeIOS_XR.rpl (770 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPStatusForNonDynamic_IOS_XR.txt (63 lines)
│   │   │   │   │   └── xmp-im-mpls-module.xsd (200 lines)
│   │   │   │   ├── mplsTeTunnelPEPStatusInfo/
│   │   │   │   │   ├── ifIndexStatusInfo_IOS.txt (29 lines)
│   │   │   │   │   ├── ifIndexStatusInfo_IOS_FullInv.txt (137 lines)
│   │   │   │   │   ├── ifIndexStatusInfo_IOS_XR.txt (18 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPStatusInfo.par (123 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPStatusInfoParser_xdeIOS.rpl (829 lines)
│   │   │   │   │   ├── mplsTeTunnelPEPStatusInfoParser_xdeIOS_XR.rpl (782 lines)
│   │   │   │   │   └── xmp-im-mpls-module.xsd (200 lines)
│   │   │   │   ├── mplsTeTunnelProtocolEndPointInfo/
│   │   │   │   │   ├── getMplsTeTunnelProtocolEndPointInfo.map (33 lines)
│   │   │   │   │   └── mplsTeTunnelProtocolEndPointInfo.par (125 lines)
│   │   │   │   ├── mplsTeTunnelSettings/
│   │   │   │   │   ├── mplsTeTunnelSettings.par (107 lines)
│   │   │   │   │   ├── mplsTeTunnelSettingsParser_xdeIOS.rpl (98 lines)
│   │   │   │   │   ├── mplsTeTunnelSettingsParser_xdeIOS_XR.rpl (98 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1326 lines)
│   │   │   │   ├── mplsTeTunnelSettingsAvailableBandwidthInfo/
│   │   │   │   │   ├── available-bandwidth (7 lines)
│   │   │   │   │   ├── mplsTeTunnelSettingsAvailableBandwidthInfo.par (103 lines)
│   │   │   │   │   ├── mplsTeTunnelSettingsAvailableBandwidthInfo_xdeIOS.rpl (99 lines)
│   │   │   │   │   └── mplsTeTunnelSettingsAvailableBandwidthInfo_xdeIOS_XR.rpl (71 lines)
│   │   │   │   ├── mplsTeTunnelSettingsConfigBandwidthInfo/
│   │   │   │   │   ├── getmplsTeTunnelSettingsConfigBandwidthInfo.par (57 lines)
│   │   │   │   │   ├── mplsTeTunnelSettingsConfigBandwidthInfo.map (14 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1711 lines)
│   │   │   │   ├── tunnelSrcInterfaceName/
│   │   │   │   │   ├── showRunningConfigXE.txt (213 lines)
│   │   │   │   │   ├── showRunningConfigXR.txt (61 lines)
│   │   │   │   │   ├── tunnelSrcInterfaceName.par (119 lines)
│   │   │   │   │   ├── tunnelSrcInterfaceNameParser_xdeIOS.rpl (113 lines)
│   │   │   │   │   ├── tunnelSrcInterfaceNameParser_xdeIOS_XR.rpl (113 lines)
│   │   │   │   │   └── xmp-im-mpls-te-module.xsd (1326 lines)
│   │   │   │   ├── xmp-im-mpls-te-module/
│   │   │   │   │   ├── 10.104.120.26-Standby-LSP.txt (636 lines)
│   │   │   │   │   ├── 10.56.23.109-Active-LSP-Tunnel-Config-Output.txt (895 lines)
│   │   │   │   │   ├── 10.56.23.109-Standby-LSP-Output.txt (181 lines)
│   │   │   │   │   ├── 10.56.23.116-Active-LSP-Tunnel-Config-Output.txt (823 lines)
│   │   │   │   │   ├── 10.56.23.116-Standby-LSP-Output.txt (185 lines)
│   │   │   │   │   ├── 42output.txt (453 lines)
│   │   │   │   │   ├── 42xx_unidir_head (47 lines)
│   │   │   │   │   ├── ASR9K-MplsTeTunnel-ShowOutput.txt (459 lines)
│   │   │   │   │   ├── ASR9K-MplsTeTunnel-v513_ShowOutput.txt (3435 lines)
│   │   │   │   │   ├── Auto-bw-NCS42xx.txt (68 lines)
│   │   │   │   │   ├── Auto-bw-NCS4k.txt (146 lines)
│   │   │   │   │   ├── IOSXE_Active_Lsp_Info.txt (161 lines)
│   │   │   │   │   ├── IOSXR_Current_StandBy_Lsp_Info.txt (273 lines)
│   │   │   │   │   ├── TETunnel-Mid.txt (429 lines)
│   │   │   │   │   ├── TETunnel-Tail.txt (546 lines)
│   │   │   │   │   ├── airtel_IOS_XRV9k.txt (319 lines)
│   │   │   │   │   ├── getMplsTeTunnelBFDSettings.xde (70 lines)
│   │   │   │   │   ├── getMplsTunnelPep.xde (277 lines)
│   │   │   │   │   ├── tunnelsDetail32.txt (505 lines)
│   │   │   │   │   ├── xeHead.txt (794 lines)
│   │   │   │   │   ├── xeMid.txt (343 lines)
│   │   │   │   │   ├── xeTail.txt (792 lines)
│   │   │   │   │   ├── xmp-im-mpls-te-module.par (162 lines)
│   │   │   │   │   ├── xmp-im-mpls-te-module.xsd (1791 lines)
│   │   │   │   │   ├── xmp-im-mpls-te-moduleParser_xdeIOS_XE.rpl (3569 lines)
│   │   │   │   │   ├── xmp-im-mpls-te-moduleParser_xdeIOS_XR.rpl (3409 lines)
│   │   │   │   │   ├── xrhead.txt (135 lines)
│   │   │   │   │   ├── xrmid.txt (100 lines)
│   │   │   │   │   └── xrtaiil.txt (87 lines)
│   │   │   │   └── featureInventoryProcedure.xde (1483 lines)
│   │   │   ├── xmp-im-mpls-topology-module-inventory.xpa/
│   │   │   │   ├── getBridgeDomain/
│   │   │   │   │   ├── getBridgeDomain.par (53 lines)
│   │   │   │   │   ├── getBridgeDomainParser_xdeIOS.rpl (54 lines)
│   │   │   │   │   └── getBridgeDomainParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │   ├── getCdpNeighbor/
│   │   │   │   │   ├── getCdpNeighbor.par (99 lines)
│   │   │   │   │   ├── getCdpNeighborParser_xdeIOS.rpl (83 lines)
│   │   │   │   │   ├── getCdpNeighborParser_xdeIOSOutput.xsd (18 lines)
│   │   │   │   │   └── getCdpNeighborParser_xdeIOS_XR.rpl (83 lines)
│   │   │   │   ├── getMplsInterface/
│   │   │   │   │   ├── getMplsInterface.par (151 lines)
│   │   │   │   │   ├── getMplsInterfaceParser_xdeIOS.rpl (244 lines)
│   │   │   │   │   ├── getMplsInterfaceParser_xdeIOSOutput.xsd (15 lines)
│   │   │   │   │   └── getMplsInterfaceParser_xdeIOS_XR.rpl (88 lines)
│   │   │   │   ├── getMplsSystemId/
│   │   │   │   │   ├── getMplsSystemId.par (99 lines)
│   │   │   │   │   ├── getMplsSystemIdParser_xdeIOS.rpl (64 lines)
│   │   │   │   │   ├── getMplsSystemIdParser_xdeIOSOutput.xsd (18 lines)
│   │   │   │   │   └── getMplsSystemIdParser_xdeIOS_XR.rpl (65 lines)
│   │   │   │   ├── getMplsTrafficEng/
│   │   │   │   │   ├── getMplsTrafficEng.par (103 lines)
│   │   │   │   │   ├── getMplsTrafficEngParser_xdeIOS.rpl (96 lines)
│   │   │   │   │   ├── getMplsTrafficEngParser_xdeIOSOutput.xsd (19 lines)
│   │   │   │   │   └── getMplsTrafficEngParser_xdeIOS_XR.rpl (137 lines)
│   │   │   │   └── getNeighbour/
│   │   │   │       ├── getNeighbour.par (103 lines)
│   │   │   │       ├── getNeighbourParser_xdeIOS.rpl (52 lines)
│   │   │   │       ├── getNeighbourParser_xdeIOSOutput.xsd (11 lines)
│   │   │   │       └── getNeighbourParser_xdeIOS_XR.rpl (52 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (12 lines)
│   │   │   ├── procedure.xde (133 lines)
│   │   │   └── xmpxde.xml (21 lines)
│   │   ├── xmp-im-mpls-te-tunnel-bfd-config/
│   │   │   ├── mpls-te-tunnel-bfd-config.xpa/
│   │   │   │   ├── mplstetunnelbfd_CreateAndUpdateWriter/
│   │   │   │   │   ├── iosxe.vtl (7 lines)
│   │   │   │   │   ├── iosxr.vtl (23 lines)
│   │   │   │   │   └── mplstetunnelbfd_CreateAndUpdateWriter.par (28 lines)
│   │   │   │   ├── mplstetunnelbfd_DeleteWriter/
│   │   │   │   │   ├── iosxe.vtl (7 lines)
│   │   │   │   │   ├── iosxr.vtl (6 lines)
│   │   │   │   │   └── mplstetunnelbfd_DeleteWriter.par (28 lines)
│   │   │   │   └── testFromNMS/
│   │   │   │       ├── NCS42xx/
│   │   │   │       │   ├── NCS42xxConfig.xft (44 lines)
│   │   │   │       │   └── NCS42xxDelete.xft (23 lines)
│   │   │   │       └── NCS4k/
│   │   │   │           ├── NCS4kConfig.xft (48 lines)
│   │   │   │           └── NCS4kDelete.xft (23 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── excludeAssociations.xml (18 lines)
│   │   │   ├── mpls-te-tunnel-bfd_CreateProcedure.xde (15 lines)
│   │   │   ├── mpls-te-tunnel-bfd_DeleteProcedure.xde (15 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (22 lines)
│   │   ├── xmp-im-mpls-te-tunnel-lspAttrList-config/
│   │   │   ├── mpls-te-tunnel-lspAttrList-config.xpa/
│   │   │   │   ├── mplstetunnellspAttrList_CreateAndUpdateWriter/
│   │   │   │   │   ├── iosxe.vtl (17 lines)
│   │   │   │   │   ├── iosxr.vtl (11 lines)
│   │   │   │   │   └── mplstetunnellspAttrList_CreateAndUpdateWriter.par (71 lines)
│   │   │   │   └── mplstetunnellspAttrList_DeleteWriter/
│   │   │   │       ├── iosxe.vtl (6 lines)
│   │   │   │       ├── iosxr.vtl (7 lines)
│   │   │   │       └── mplstetunnellspAttrList_DeleteWriter.par (71 lines)
│   │   │   ├── mpls-te-tunnel-lspAttrList_CreateProcedure.xde (15 lines)
│   │   │   ├── mpls-te-tunnel-lspAttrList_DeleteProcedure.xde (15 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── xmp-im-srte-module-config/
│   │   │   ├── SRTE-config.xpa/
│   │   │   │   ├── SRTE_CreateAndUpdateWriter/
│   │   │   │   │   ├── SRTE_CreateAndUpdateWriter.par (71 lines)
│   │   │   │   │   ├── iosxe.vtl (0 lines)
│   │   │   │   │   └── iosxr.vtl (190 lines)
│   │   │   │   ├── SRTE_DeleteWriter/
│   │   │   │   │   ├── SRTE_DeleteWriter.par (71 lines)
│   │   │   │   │   ├── iosxe.vtl (0 lines)
│   │   │   │   │   └── iosxr.vtl (159 lines)
│   │   │   │   └── testFromNMS/
│   │   │   │       └── NCS55xx/
│   │   │   │           ├── CreateSR_XR.xft (239 lines)
│   │   │   │           ├── CreateSR_XR_MandatoryFields.xft (108 lines)
│   │   │   │           ├── CreateSR_XR_SegmentList.xft (38 lines)
│   │   │   │           ├── Delete_XR_Policy.xft (84 lines)
│   │   │   │           └── Delete_XR_PolicyDetails.xft (155 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── SRTE_CreateProcedure.xde (20 lines)
│   │   │   ├── SRTE_DeleteProcedure.xde (20 lines)
│   │   │   ├── excludeAssociations.xml (4 lines)
│   │   │   ├── packageDescriptor.xml (10 lines)
│   │   │   └── xmpxde.xml (18 lines)
│   │   ├── xmp-im-srte-module-inventory/
│   │   │   ├── META-INF/
│   │   │   │   ├── maven/
│   │   │   │   │   └── com.cisco.prime.inventory.xde/
│   │   │   │   │       └── xmp-im-srte-module-inventory/
│   │   │   │   │           ├── pom.properties (4 lines)
│   │   │   │   │           └── pom.xml (18 lines)
│   │   │   │   └── MANIFEST.MF (5 lines)
│   │   │   ├── getSegmentRoutingOnDemandPolicy/
│   │   │   │   ├── getSegmentRoutingOnDemandPolicy.par (111 lines)
│   │   │   │   ├── getSegmentRoutingOnDemandPolicyParser_xdeIOS.rpl (1170 lines)
│   │   │   │   ├── getSegmentRoutingOnDemandPolicyParser_xdeIOSXR.rpl (1073 lines)
│   │   │   │   ├── getSegmentRoutingOnDemandPolicyParser_xdeIOS_XEOutput.xsd (66 lines)
│   │   │   │   ├── getSegmentRoutingOnDemandPolicyParser_xdeIOS_XROutput.xsd (63 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (2196 lines)
│   │   │   ├── getSegmentRoutingPolicySettings/
│   │   │   │   ├── DeviceOutput_XR_SidAlgorithm.txt (1527 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettings.par (213 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_IOS.xslt (648 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_IOS_XR.xslt (754 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_xdeIOS.rpl (1806 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_xdeIOS_XEOutput.xsd (157 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_xdeIOS_XR.rpl (1872 lines)
│   │   │   │   ├── getSegmentRoutingPolicySettingsParser_xdeIOS_XROutput.xsd (1057 lines)
│   │   │   │   ├── sampleDeviceOutput_XR.txt (513 lines)
│   │   │   │   ├── sampleOutput_XE.txt (919 lines)
│   │   │   │   └── sampleOutput_XR.txt (166 lines)
│   │   │   ├── getSegmentRoutingSegmentListSettings/
│   │   │   │   ├── getSegmentRoutingSegmentListSettings.par (112 lines)
│   │   │   │   ├── getSegmentRoutingSegmentListSettingsParser_xdeIOS.rpl (274 lines)
│   │   │   │   ├── getSegmentRoutingSegmentListSettingsParser_xdeIOS_XR.rpl (167 lines)
│   │   │   │   ├── getSegmentRoutingSegmentListSettingsParser_xdeIOS_XROutput.xsd (32 lines)
│   │   │   │   ├── sampleDeviceOutput_XR.txt (33 lines)
│   │   │   │   ├── segmentListSettings.xde (73 lines)
│   │   │   │   └── xmp-im-mpls-module.xsd (2196 lines)
│   │   │   ├── test/
│   │   │   │   ├── SegmentRoutingOnDemandPolicy/
│   │   │   │   │   ├── getSegmentRoutingOnDemandPolicy.xft (186 lines)
│   │   │   │   │   └── getSegmentRoutingOnDemandPolicyGI.xft (54 lines)
│   │   │   │   ├── SegmentRoutingPolicySettings/
│   │   │   │   │   └── getSegmentRoutingPolicySettings.xft (1650 lines)
│   │   │   │   ├── SegmentRoutingSegmentListSettings/
│   │   │   │   │   ├── getSegmentRoutingSegmentListSettings.xft (200 lines)
│   │   │   │   │   └── getSegmentRoutingSegmentListSettingsGI.xft (61 lines)
│   │   │   │   └── XE/
│   │   │   │       └── SegmentRoutingPolicySettings/
│   │   │   │           └── getSegmentRoutingPolicySettings.xft (939 lines)
│   │   │   ├── .project (29 lines)
│   │   │   ├── packageDescriptor.xml (14 lines)
│   │   │   ├── procedure.xde (427 lines)
│   │   │   └── xmpxde.xml (17 lines)
│   │   ├── .project (11 lines)
│   │   ├── pom.xml (780 lines)
│   │   ├── update.sh (260 lines)
│   │   └── update1.sh (60 lines)
│   ├── log_collection_tool/
│   │   ├── bin/
│   │   │   └── collectInventoryLogsScript.sh (53 lines)
│   │   ├── conf/
│   │   │   └── cepnm-inventory.properties (12 lines)
│   │   ├── assembly.xml (20 lines)
│   │   └── pom.xml (40 lines)
│   ├── logs/
│   │   ├── XFT_STATUS.txt (6310 lines)
│   │   └── XFTs_Without_Ownership.txt (1824 lines)
│   ├── mibs/
│   │   ├── files/
│   │   │   ├── CISCO-BGP4-MIB.my (2280 lines)
│   │   │   ├── CISCO-DOT3-OAM-MIB.mib (2134 lines)
│   │   │   ├── CISCO-ENTITY-SENSOR-MIB.my (874 lines)
│   │   │   ├── CISCO-ETHER-CFM-MIB.my (693 lines)
│   │   │   ├── CISCO-IETF-ISIS-MIB.my (3816 lines)
│   │   │   ├── CISCO-IETF-PW-ENET-MIB.my (510 lines)
│   │   │   ├── CISCO-IETF-PW-MIB.my (1369 lines)
│   │   │   ├── CISCO-IETF-PW-TC-MIB.my (182 lines)
│   │   │   ├── CISCO-QOS-PIB-MIB.my (2028 lines)
│   │   │   ├── CISCO-RTTMON-MIB.my (10604 lines)
│   │   │   ├── CISCO-RTTMON-TC-MIB.my (756 lines)
│   │   │   ├── CISCO-SMI.my (554 lines)
│   │   │   ├── CISCO-STACK-MIB.my (13255 lines)
│   │   │   ├── CISCO-TC.my (2435 lines)
│   │   │   ├── CISCO-VTP-MIB.my (6521 lines)
│   │   │   ├── IEEE8021-CFM-MIB.mib (3707 lines)
│   │   │   ├── IEEE8023-LAG-MIB.my (1399 lines)
│   │   │   ├── ISIS-MIB.my (4581 lines)
│   │   │   ├── LLDP-MIB.my (1987 lines)
│   │   │   ├── ME1200-IP-MIB.mib (4700 lines)
│   │   │   ├── ME1200-LLDP-MIB.mib (572 lines)
│   │   │   ├── ME1200-SMI.mib (43 lines)
│   │   │   └── Q-BRIDGE-MIB.my (1891 lines)
│   │   ├── assembly.xml (20 lines)
│   │   └── pom.xml (40 lines)
│   ├── .project (11 lines)
│   ├── pom.xml (56 lines)
│   └── xft_ownership_validation.sh (37 lines)
├── testautomation/
│   ├── xmp_device_package_test/
│   │   ├── testObjects/
│   │   │   ├── 1-create-customers.xml (6 lines)
│   │   │   └── 3-create-interfaces.xml (8 lines)
│   │   ├── packageDescriptor.xml (13 lines)
│   │   ├── runFeatureEMSXML.xde (36 lines)
│   │   └── runFeatureNMSXML.xde (38 lines)
│   └── pom.xml (972 lines)
├── .gitignore (68 lines)
├── CODEOWNERS (1 lines)
├── Jenkinsfile (81 lines)
└── pom.xml (107 lines)
```
