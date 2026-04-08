# 08 - Research: EPNM Legacy Stack (Dojo, Oracle, Java Monolith)

**Source:** Web research
**Source Date:** 2026-04-07
**Document Set:** 08 (Technical Research)
**Pass:** EPNM legacy technology stack reference

---

## Purpose

This document provides a technical reference for the technologies that make up the EPNM (Evolved Programmable Network Manager) legacy stack. The goal is to equip BayOne's team with enough understanding of Dojo 1.x, Oracle persistence, Java monolith patterns, and SNMP/CLI data collection to effectively analyze and convert EPNM screens to Angular within the EMS (Element Management System) framework.

From the April 6, 2026 meeting (Set 07), Cisco's team confirmed:
- EPNM frontend: **Dojo (legacy version)**
- EPNM backend: **Java monolith with Oracle database**
- EPNM data collection: **SNMP and CLI (referred to as "ECLI") polling of network devices**
- EMS frontend: **Angular 21** with Harbor/Magnetic design system
- EMS backend: **Spring Boot + Go services with PostgreSQL**

The POC requires understanding how EPNM screens work (Dojo widgets, data fetching, rendering patterns) in order to rewrite them in Angular with identical look and feel, connected to the new EMS backend.

---

## 1. Dojo Toolkit 1.x -- Frontend Framework

### 1.1 What Dojo Is

Dojo Toolkit is a JavaScript framework that emerged in the mid-2000s. Unlike React or Angular, Dojo 1.x is a **toolkit** -- a collection of utilities, widgets, and patterns rather than an opinionated application framework. It provides its own module system, widget lifecycle, data abstraction layer, event handling, templating, theming, and AJAX communication.

Dojo 1.x is no longer actively developed. The last stable release is version 1.17.3. Dojo 2+ was a complete rewrite in TypeScript and bears little resemblance to 1.x. EPNM uses the legacy 1.x branch.

**Why this matters for conversion:** Every pattern in Dojo 1.x has a fundamentally different equivalent in Angular. There is no automated migration path. The conversion is a full rewrite guided by understanding what the Dojo code does, not a mechanical translation.

### 1.2 AMD Module System

Dojo 1.7+ uses the Asynchronous Module Definition (AMD) format for organizing code into modules. AMD was Dojo's answer to the lack of a native JavaScript module system (this was years before ES modules existed).

**How it looks in EPNM code:**

```javascript
// AMD module definition -- this is the pattern you will see everywhere in EPNM
define([
    "dojo/_base/declare",
    "dijit/_WidgetBase",
    "dijit/_TemplatedMixin",
    "dojo/text!./templates/DeviceList.html",
    "dojo/store/JsonRest",
    "dojo/topic"
], function(declare, _WidgetBase, _TemplatedMixin, template, JsonRest, topic) {

    return declare([_WidgetBase, _TemplatedMixin], {
        templateString: template,
        // ... widget implementation
    });
});
```

Key characteristics:
- **`define()`** declares a module with its dependencies listed as an array of string paths
- **`require()`** loads modules for execution without creating a new module
- Dependencies use **slash notation** (`dijit/form/Button`, not `dijit.form.Button`)
- The dependency array maps positionally to the callback function parameters
- Module paths map to filesystem paths relative to configured package roots
- The **`dojo/text!`** plugin loads text files (typically HTML templates) as strings

**Older EPNM code may use the legacy format** (pre-1.7):

```javascript
// Legacy (pre-AMD) -- you may encounter this in older parts of the codebase
dojo.provide("epnm.inventory.DeviceList");
dojo.require("dijit._Widget");
dojo.require("dijit._Templated");
```

The legacy loader operates synchronously. If EPNM mixes AMD and legacy patterns, it means the Dojo loader is running in compatibility mode, which forces synchronous loading for all modules.

**Angular equivalent:** ES module imports (`import { Component } from '@angular/core'`). The mapping is straightforward -- each AMD `define()` block becomes an ES module file with `import` statements.

### 1.3 Class System (dojo/_base/declare)

Dojo has its own class/inheritance system built before JavaScript had native classes. `dojo/_base/declare` provides:

- **Single inheritance** (first argument in the mixin array is the true superclass)
- **Multiple mixin support** using C3 superclass linearization (same algorithm Python uses for method resolution order)
- **`this.inherited(arguments)`** to call the parent class implementation (similar to `super()`)

```javascript
define([
    "dojo/_base/declare",
    "dijit/_WidgetBase",
    "dijit/_TemplatedMixin",
    "./_DeviceFilterMixin"
], function(declare, _WidgetBase, _TemplatedMixin, _DeviceFilterMixin) {

    // Multiple inheritance: _WidgetBase is the true superclass,
    // _TemplatedMixin and _DeviceFilterMixin are mixed in
    return declare([_WidgetBase, _TemplatedMixin, _DeviceFilterMixin], {

        name: "DeviceList",

        constructor: function(params) {
            // Called during instantiation
        },

        postCreate: function() {
            this.inherited(arguments); // Call parent's postCreate
            // Custom initialization here
        }
    });
});
```

**What to watch for in EPNM:** Custom mixins (prefixed with underscore by convention, like `_DeviceFilterMixin`) that add shared behavior across multiple widgets. These represent cross-cutting concerns that will need to be mapped to Angular services, directives, or base classes.

### 1.4 Widget Lifecycle (Dijit)

Dijit is Dojo's widget system. Every UI component in EPNM is a Dijit widget, and each widget follows a strict lifecycle. Understanding this lifecycle is essential for knowing where EPNM puts its initialization logic, DOM manipulation, and cleanup.

**Lifecycle methods in execution order:**

| Method | When it runs | What to look for |
|--------|-------------|------------------|
| `constructor()` | Object instantiation, before any DOM exists | Parameter initialization, default values |
| `postMixInProperties()` | After properties are mixed in, before DOM creation | Property computation, string assembly for templates |
| `buildRendering()` | Creates the DOM tree from the template | Usually handled by `_TemplatedMixin`; manual DOM creation if not using templates |
| `postCreate()` | **Most important.** After DOM exists but before it is placed in the document | Event binding, child widget references, data loading, store connections -- most logic lives here |
| `startup()` | After the widget and all children are in the DOM | Layout calculations, child widget startup, anything that needs measured dimensions |
| `destroy()` | Cleanup | Event listener removal, store disconnection, child widget destruction |

**Critical detail:** `postCreate()` is where the bulk of widget logic lives in most Dojo applications. When analyzing EPNM widgets to understand what they do, start with `postCreate()`.

**Angular equivalent mapping:**

| Dojo Lifecycle | Angular Lifecycle |
|---------------|-------------------|
| `constructor()` | `constructor()` |
| `postMixInProperties()` | Property initialization before `ngOnInit()` |
| `postCreate()` | `ngOnInit()` + `ngAfterViewInit()` |
| `startup()` | `ngAfterViewInit()` |
| `destroy()` | `ngOnDestroy()` |

### 1.5 Templating System

Dijit widgets use HTML template strings with special attributes for DOM binding. This is the mechanism that connects the widget's JavaScript logic to its rendered HTML.

**Template example (what you will see in EPNM `.html` template files):**

```html
<div class="deviceListContainer">
    <div data-dojo-attach-point="headerNode" class="deviceListHeader">
        <span data-dojo-attach-point="titleNode">${title}</span>
        <span data-dojo-attach-point="countNode"></span>
    </div>
    <div data-dojo-attach-point="gridNode" class="deviceGrid"></div>
    <button data-dojo-attach-event="onclick: _onRefresh"
            class="refreshButton">Refresh</button>
</div>
```

Key template features:
- **`data-dojo-attach-point="nodeName"`** -- Creates a reference on the widget instance: `this.gridNode` is the actual DOM element. This is how widgets find their own DOM nodes without using CSS selectors.
- **`data-dojo-attach-event="onclick: _onRefresh"`** -- Wires a DOM event directly to a widget method.
- **`${propertyName}`** -- Simple string substitution from widget properties (one-time, not reactive).
- **`_TemplatedMixin`** handles turning this template into DOM nodes during `buildRendering()`.
- **`_WidgetsInTemplateMixin`** -- If this mixin is included, the template can contain other Dijit widgets (using `data-dojo-type` inside the template). This creates widget composition/nesting.

**Angular equivalent:** Angular component templates with `@ViewChild` (for attach points), `(click)="onRefresh()"` (for attach events), and `{{ title }}` or `[innerText]="title"` (for property binding). The key difference: Angular's bindings are reactive; Dojo's `${}` substitution is one-time.

### 1.6 Declarative Markup (data-dojo-type)

Dojo allows widgets to be instantiated from HTML markup using the `dojo/parser`. This means you may find widget instantiation happening directly in HTML/JSP pages, not just in JavaScript.

```html
<!-- The parser scans the DOM and instantiates widgets from markup -->
<body class="claro">

    <div data-dojo-type="dijit/layout/BorderContainer" style="width:100%;height:100%">
        <div data-dojo-type="dijit/layout/ContentPane"
             data-dojo-props="region: 'top'"
             class="headerPane">
            <!-- Header content -->
        </div>
        <div data-dojo-type="epnm/inventory/DeviceList"
             data-dojo-props="autoLoad: true, pageSize: 50"
             data-dojo-attach-point="deviceListWidget">
        </div>
    </div>

    <script>
        require(["dojo/parser", "dojo/domReady!"], function(parser) {
            parser.parse();  // Scans DOM, instantiates all data-dojo-type widgets
        });
    </script>
</body>
```

Key attributes:
- **`data-dojo-type="module/path"`** -- Specifies the widget class to instantiate
- **`data-dojo-props="key: value, key2: value2"`** -- Widget constructor parameters as a JavaScript object literal (without outer braces)
- **`dojo/parser`** -- Scans the DOM, finds all `data-dojo-type` nodes, requires their modules, and instantiates them

**Why this matters:** EPNM pages likely use a combination of declarative (HTML-based) and programmatic (JavaScript-based) widget instantiation. When analyzing a page, you need to check both the HTML/JSP markup and the JavaScript for widget creation.

### 1.7 Data Stores

Dojo's data layer uses the `dojo/store` API, which abstracts data access behind a uniform interface. This is how EPNM widgets get their data from the Java backend.

**Core store types:**

```javascript
// In-memory store (client-side data)
var memoryStore = new Memory({
    data: [
        { id: 1, name: "Router-1", type: "Cisco ASR 9000" },
        { id: 2, name: "Switch-1", type: "Cisco Nexus 9000" }
    ]
});

// REST-backed store (server-side data via HTTP)
var restStore = new JsonRest({
    target: "/webacs/api/v4/data/Devices",  // Backend REST endpoint
    idProperty: "deviceId"
});

// Observable wrapper (enables widgets to react to data changes)
var observableStore = Observable(restStore);

// Cache wrapper (client-side cache in front of server store)
var cachedStore = Cache(restStore, Memory());
```

**The `dojo/store` API methods:**
- `get(id)` -- Fetch a single object by ID
- `query(queryParams, options)` -- Fetch a filtered, sorted, paginated collection
- `put(object)` -- Create or update an object
- `remove(id)` -- Delete an object
- `getIdentity(object)` -- Get the ID of an object

**How stores connect to widgets (especially grids):**

```javascript
// A dgrid configured with a store
var grid = new (declare([OnDemandGrid, Selection, ColumnResizer]))({
    store: observableStore,
    columns: {
        deviceName: "Device Name",
        ipAddress: "IP Address",
        deviceType: "Device Type",
        reachability: "Reachability"
    },
    sort: [{ property: "deviceName", descending: false }]
}, "gridNode");
grid.startup();
```

**What to watch for in EPNM:**
- **JsonRest stores** pointing at specific backend REST endpoints -- these tell you the API contract between frontend and backend
- **Custom store implementations** that extend the base stores with EPNM-specific logic (filtering, caching, polling)
- **Store composition** patterns: `Observable(Cache(JsonRest(...), Memory()))` -- multiple wrappers around a base store
- **Query parameter patterns** that map to the backend's expected query format

**Angular equivalent:** Angular `HttpClient` calls wrapped in services, with RxJS Observables for reactivity. The store URL targets tell you what REST endpoints the Angular service will need to call on the EMS backend.

### 1.8 Event Handling and Pub/Sub

Dojo uses two event systems: direct event handling (`dojo/on`) and a global publish/subscribe system (`dojo/topic`).

**Direct event handling:**

```javascript
// dojo/on -- binds events to specific DOM elements or widgets
require(["dojo/on"], function(on) {
    on(this.refreshButton, "click", function(evt) {
        // Handle click
    });
});
```

**Global pub/sub (topic):**

```javascript
// Publishing a message (from anywhere in the application)
require(["dojo/topic"], function(topic) {
    topic.publish("epnm/device/selected", { deviceId: 12345 });
});

// Subscribing to a message (from anywhere in the application)
require(["dojo/topic"], function(topic) {
    var handle = topic.subscribe("epnm/device/selected", function(data) {
        console.log("Device selected:", data.deviceId);
    });

    // Later: handle.remove() to unsubscribe
});
```

**Why pub/sub matters for understanding EPNM:** The topic system is how loosely-coupled widgets communicate. When a user selects a device in the inventory list, the list widget publishes a topic. The device details pane, the chassis view, and the fault panel all subscribe to that topic and update themselves. This pattern reveals the **implicit contracts** between UI components -- there is no explicit interface, just topic name strings.

**What to catalog when analyzing EPNM code:**
- All `topic.publish()` calls -- these are the messages a widget sends
- All `topic.subscribe()` calls -- these are the messages a widget listens for
- The topic name strings (e.g., `"epnm/device/selected"`) -- these form the application's internal event API
- The data payloads passed with each topic -- these define the contract

**Angular equivalent:** Angular services with RxJS Subjects/BehaviorSubjects, or NgRx/state management for complex cases. The pub/sub topic names become service method calls or action types.

### 1.9 Grids (dgrid / dojox DataGrid)

Data grids are likely the most important widget type in EPNM. The inventory list, fault list, and most tabular views are grid widgets. EPNM may use either the older `dojox/grid/DataGrid` or the newer `dgrid`.

**dojox/grid/DataGrid (older):**
- Monolithic grid widget with built-in features
- Uses the older `dojo/data` API (ItemFileReadStore, ItemFileWriteStore)
- Heavier, less modular

**dgrid (newer, recommended since Dojo 1.7):**
- Lightweight, modular grid built on `dojo/store`
- Features exposed as mixins: `Selection`, `ColumnResizer`, `Pagination`, `Editor`, `DnD`
- Much more flexible than DataGrid

```javascript
// dgrid with mixins composing features
define([
    "dgrid/OnDemandGrid",
    "dgrid/Selection",
    "dgrid/extensions/ColumnResizer",
    "dgrid/extensions/Pagination",
    "dojo/_base/declare"
], function(OnDemandGrid, Selection, ColumnResizer, Pagination, declare) {

    return declare([OnDemandGrid, Selection, ColumnResizer, Pagination], {
        columns: {
            deviceName: {
                label: "Device Name",
                sortable: true,
                renderCell: function(object, value, node) {
                    // Custom cell rendering
                    node.innerHTML = '<a href="#device/' + object.id + '">' + value + '</a>';
                }
            },
            ipAddress: { label: "IP Address" },
            reachability: {
                label: "Reachability",
                renderCell: function(object, value, node) {
                    node.className = value === "Reachable" ? "status-up" : "status-down";
                    node.textContent = value;
                }
            }
        },
        selectionMode: "single",
        minRowsPerPage: 25,
        maxRowsPerPage: 100
    });
});
```

**What matters for the POC:** The EPNM device list and fault list are almost certainly grid-based. Understanding the column definitions, custom cell renderers, sort behavior, pagination mode, and selection model will directly inform what the Angular replacement needs to implement. The Angular side will likely use a component like AG Grid, PrimeNG Table, or Angular Material's data table.

### 1.10 Layout Widgets

Dojo provides layout container widgets that manage how content is arranged on screen. These are likely used for the overall EPNM page structure.

Key layout widgets:
- **`dijit/layout/BorderContainer`** -- Divides the screen into regions (top, bottom, left, right, center) with resizable splitters
- **`dijit/layout/ContentPane`** -- A container that can load content, either static HTML or lazy-loaded from a URL
- **`dijit/layout/TabContainer`** -- Tabbed content areas
- **`dijit/layout/AccordionContainer`** -- Collapsible stacked panels

From the product walkthrough (Set 07), EPNM uses a layout with a left navigation panel, a main content area with tabbed views, and popup/overlay panels (like Interface 360). These are likely implemented using `BorderContainer` (or a custom layout) with `TabContainer` for the detail views.

### 1.11 Theming

Dijit ships four themes: **Claro** (the most recent), **Tundra**, **Nihilo**, and **Soria**. Themes are CSS files that style all Dijit widgets consistently.

**How theming works:**
1. Include the theme CSS: `<link rel="stylesheet" href="dijit/themes/claro/claro.css">`
2. Add the theme class to the `<body>`: `<body class="claro">`
3. All Dijit widgets inherit their styling from the theme CSS

EPNM likely uses either the Claro theme or a **custom theme** built on top of Claro. From the meeting transcript, the EPNM look is described as "blue and white" theming, which does not match Claro's default color scheme -- suggesting a customized theme.

Claro themes are built using **LESS CSS** with variables defined in `dijit/themes/claro/variables.less`. A custom EPNM theme would override these variables to produce the blue/white palette.

**What this means for the POC:** The Angular replacement must reproduce the EPNM "blue and white" visual treatment. This is purely a CSS/design task -- the EPNM theme CSS files (if accessible) can be analyzed to extract exact colors, spacing, and visual patterns.

### 1.12 AJAX Communication (dojo/request)

This is how EPNM widgets fetch data from the Java backend.

**Modern API (dojo 1.8+):**

```javascript
require(["dojo/request/xhr"], function(xhr) {
    xhr("/webacs/api/v4/data/Devices.json", {
        method: "GET",
        handleAs: "json",
        query: { .full: true, .maxResults: 50 }
    }).then(
        function(data) {
            // Success -- data is parsed JSON
            console.log("Devices:", data);
        },
        function(error) {
            // Error
            console.error("Failed:", error);
        }
    );
});
```

**Legacy API (pre-1.8, may still be present):**

```javascript
dojo.xhrGet({
    url: "/webacs/api/v4/data/Devices.json",
    handleAs: "json",
    load: function(data) { /* success */ },
    error: function(error) { /* failure */ }
});
```

**What to extract from EPNM code:** Every XHR call reveals a backend endpoint. Cataloging these gives you the complete API surface that the Angular replacement will need. The URL patterns, query parameters, HTTP methods, and response shapes define the contract.

---

## 2. Oracle Database -- Persistence Layer

### 2.1 Role in EPNM Architecture

Oracle is the persistence layer for all device data in EPNM. The data flow (confirmed in the April 6 meeting) is:

```
Network Devices (routers, switches, optical gear)
    |
    | SNMP polling, CLI commands
    v
Data Collection Services (Java)
    |
    | Parse responses, normalize data
    v
Oracle Database
    |
    | JDBC queries
    v
Java Application Layer (business logic, REST APIs)
    |
    | JSON responses
    v
Dojo Frontend (widgets, grids, charts)
```

Pradeep (Cisco engineering lead) described this pattern: "The information is collected, parsed, and there is a data model where the data is abstracted. And then the various applications -- when I say applications within the product -- you will have an inventory component, there will be a topology component, there will be a fault component, so on and so forth, service level component. All of them will consume that data from the database."

Colin confirmed the data access pattern: "This application reads from isn't necessarily the device directly, but instead this application reads from Oracle. Is that right?" The team responded: "In most of the cases, it won't directly go to the [device]. It reads from the database, correct."

### 2.2 How Java Applications Integrate with Oracle

Legacy Java applications typically use one or more of these integration patterns:

**JDBC (Java Database Connectivity) -- Direct SQL:**
The lowest-level approach. Java code executes SQL statements directly against Oracle using the Oracle JDBC driver (ojdbc).

```java
// Raw JDBC pattern -- common in older monoliths
Connection conn = dataSource.getConnection();
PreparedStatement stmt = conn.prepareStatement(
    "SELECT device_id, hostname, ip_address, device_type " +
    "FROM network_devices " +
    "WHERE reachability = ? AND device_type LIKE ?"
);
stmt.setString(1, "REACHABLE");
stmt.setString(2, "%ASR%");
ResultSet rs = stmt.executeQuery();

while (rs.next()) {
    Device device = new Device();
    device.setDeviceId(rs.getLong("device_id"));
    device.setHostname(rs.getString("hostname"));
    // ... manual mapping from ResultSet to Java objects
}
```

**JPA/Hibernate -- ORM (Object-Relational Mapping):**
Higher-level abstraction that maps Java classes to database tables. More likely in newer parts of the monolith, less likely in the oldest parts.

```java
@Entity
@Table(name = "NETWORK_DEVICES")
public class NetworkDevice {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "device_seq")
    @SequenceGenerator(name = "device_seq", sequenceName = "DEVICE_ID_SEQ")
    private Long deviceId;

    @Column(name = "HOSTNAME")
    private String hostname;

    @Column(name = "IP_ADDRESS")
    private String ipAddress;

    @OneToMany(mappedBy = "device", fetch = FetchType.LAZY)
    private List<DeviceInterface> interfaces;
}
```

**Stored Procedures / PL/SQL:**
Oracle-specific server-side logic. Common for complex data transformations, bulk operations, or performance-critical paths.

```java
// Calling an Oracle stored procedure from Java
CallableStatement cstmt = conn.prepareCall("{ call REFRESH_DEVICE_INVENTORY(?, ?) }");
cstmt.setLong(1, deviceId);
cstmt.registerOutParameter(2, Types.INTEGER);  // OUT parameter
cstmt.execute();
int result = cstmt.getInt(2);
```

**Connection Pooling:**
Enterprise Java applications use connection pools managed by the application server or a library like HikariCP. The Oracle JDBC driver provides `OracleDataSource` and `OracleConnectionPoolDataSource`. In a Java EE environment, the DataSource is typically configured via JNDI and managed by the application server (WebLogic, WildFly, etc.).

### 2.3 Oracle-Specific Features Likely Used in EPNM

A 15+ year old network management product built on Oracle will almost certainly use Oracle-specific features that create vendor lock-in. These features are relevant because EMS moved to PostgreSQL, meaning they had to be converted or replaced.

**Sequences:**
Oracle sequences generate unique IDs. Every device, interface, alarm, and event record likely uses a sequence-generated primary key.

```sql
CREATE SEQUENCE DEVICE_ID_SEQ START WITH 1 INCREMENT BY 1;
-- Used in INSERT: INSERT INTO NETWORK_DEVICES (DEVICE_ID, ...) VALUES (DEVICE_ID_SEQ.NEXTVAL, ...);
```

**Materialized Views:**
Pre-computed query results stored as physical tables. In a network management system, these would be used for dashboard summaries, device counts by type/status, alarm rollups, and performance aggregations.

```sql
CREATE MATERIALIZED VIEW MV_DEVICE_SUMMARY
REFRESH FAST ON COMMIT
AS SELECT device_type, reachability, COUNT(*) as device_count
   FROM NETWORK_DEVICES
   GROUP BY device_type, reachability;
```

Materialized views can refresh on commit (immediately), on demand, or on a schedule. For a network management system with constantly changing device status data, the refresh strategy directly affects how current the UI data is.

**PL/SQL Packages and Stored Procedures:**
Server-side business logic. In NMS applications, common uses include:
- Alarm correlation and deduplication
- Inventory reconciliation after device polling
- Performance data aggregation and rollup
- Bulk device operations (discovery, rediscovery)
- Data cleanup and archival

**Oracle-Specific SQL:**
- `CONNECT BY` for hierarchical queries (device containment trees)
- `DECODE()` function (conditional logic in SQL)
- `ROWNUM` for pagination (pre-12c; later versions use `FETCH FIRST n ROWS`)
- `NVL()` instead of standard `COALESCE()`
- `DUAL` table for computed expressions
- `(+)` syntax for outer joins (legacy; modern ANSI join syntax may also be used)

**Partitioning:**
Large tables (event logs, performance data, polling history) are likely partitioned by date for manageability and query performance.

### 2.4 Why Oracle Matters for the POC

For the POC itself, Oracle is not directly relevant -- the POC reuses the existing EMS backend (Spring Boot + PostgreSQL). However, understanding the Oracle data model helps when:
- Comparing what data EPNM screens show vs. what the EMS backend currently exposes
- Understanding the 10-20% functionality gap between EPNM and EMS
- Analyzing how EPNM's REST endpoints transform Oracle data for frontend consumption (this informs what the Angular code expects to receive)

---

## 3. Java Monolith Architecture

### 3.1 Characteristics of a 15+ Year Java Monolith

EPNM is part of a codebase that spans 45-50 million lines across 6-8 products (per Guhan in the February 9 meeting). This is a textbook legacy Java monolith. Based on the product's age and description, EPNM likely exhibits these common patterns:

**Single deployable unit:** The entire application (UI serving, business logic, data access, device communication, scheduling) deploys as one artifact -- typically a WAR or EAR file deployed to a Java EE application server.

**Layered architecture (nominally):** Most Java monoliths of this era follow a layered pattern, but with significant bleeding between layers over 15+ years of development:

```
+------------------------------------------------------------------+
|  Presentation Layer (Dojo widgets served via servlets/JSP)       |
+------------------------------------------------------------------+
|  Service Layer (business logic, REST endpoints)                  |
+------------------------------------------------------------------+
|  Data Access Layer (DAO/Repository pattern, JDBC/Hibernate)      |
+------------------------------------------------------------------+
|  Infrastructure Layer (SNMP, CLI, scheduling, caching)           |
+------------------------------------------------------------------+
|  Oracle Database                                                 |
+------------------------------------------------------------------+
```

In practice, layers in old monoliths are often violated:
- Servlets that directly execute SQL
- Business logic embedded in JSP pages
- Data access objects that contain business rules
- UI-specific data transformations in the service layer

**Tight coupling:** Business domains (inventory, faults, topology, provisioning) share the same database, the same application context, and often the same class hierarchies. A change to the device data model can ripple through inventory, fault correlation, topology rendering, and provisioning workflows.

### 3.2 How Dojo Frontends Talk to Java Backends

This is the most important integration point for the POC. The Dojo frontend needs to get data from the Java backend. In EPNM, this likely uses one or more of these patterns:

**Pattern 1: REST APIs (most likely for newer parts)**

The most common pattern in post-2010 Java web applications. The backend exposes REST endpoints that return JSON, and the Dojo frontend fetches data via XHR.

```java
// Java side: JAX-RS or Spring MVC REST controller
@Path("/api/v4/data/Devices")
public class DeviceResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getDevices(
        @QueryParam(".full") boolean full,
        @QueryParam(".maxResults") int maxResults,
        @QueryParam(".firstResult") int firstResult
    ) {
        List<Device> devices = deviceService.findDevices(full, maxResults, firstResult);
        return Response.ok(devices).build();
    }
}
```

```javascript
// Dojo side: JsonRest store pointing at the REST endpoint
var deviceStore = new JsonRest({
    target: "/webacs/api/v4/data/Devices",
    idProperty: "deviceId"
});
```

EPNM has documented REST APIs (Cisco provides API documentation for EPNM). The URL pattern `/webacs/api/` is the known EPNM REST API base path.

**Pattern 2: Servlets returning JSON or HTML fragments**

Older parts of the application may use plain servlets instead of REST frameworks:

```java
// Java side: raw servlet
public class DeviceServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
        throws IOException {
        String deviceId = req.getParameter("deviceId");
        Device device = deviceDAO.findById(Long.parseLong(deviceId));

        resp.setContentType("application/json");
        resp.getWriter().write(objectMapper.writeValueAsString(device));
    }
}
```

**Pattern 3: JSP pages with embedded data**

The oldest pattern: JSP pages that render HTML with data baked in, and Dojo widgets that operate on that pre-rendered DOM:

```jsp
<%-- JSP page that renders device data into HTML, then Dojo enhances it --%>
<table data-dojo-type="dojox/grid/DataGrid"
       data-dojo-props="structure: deviceGridLayout">
    <% for (Device d : devices) { %>
    <tr>
        <td><%= d.getHostname() %></td>
        <td><%= d.getIpAddress() %></td>
    </tr>
    <% } %>
</table>
```

**What matters for the POC:** The REST API pattern (Pattern 1) is what the POC will work with. The EMS backend already exposes REST APIs for the Angular frontend. The task is mapping what data the EPNM UI shows (which came from EPNM's REST endpoints or servlets) to what the EMS backend currently provides. Mismatches in data shape, field naming, or available fields represent the gap that may need backend work.

### 3.3 Application Server

Java monoliths of this era run on a Java EE application server. For Cisco products, the likely candidates are:
- **WildFly** (formerly JBoss) -- Cisco Prime Service Catalog uses WildFly, and there is precedent in the Cisco product family
- **Apache Tomcat** -- Common for servlet-based applications without full Java EE requirements
- **Oracle WebLogic** -- Used by some Cisco products historically

The application server provides:
- JNDI DataSource management (database connection pooling)
- Servlet container (HTTP request handling)
- Security (authentication, authorization, session management)
- Deployment infrastructure

### 3.4 Implicit Contracts in Monoliths

A critical characteristic of legacy monoliths is that interfaces between components are often implicit rather than explicit. In EPNM, this manifests as:

**Frontend-backend contracts:**
- The Dojo code expects specific JSON shapes from specific URL paths
- There is no formal API specification (OpenAPI/Swagger) for most internal endpoints
- The "contract" is whatever the current code happens to send/receive

**Cross-component contracts:**
- One Java component writes to a database table; another reads from it
- The database schema is the implicit interface
- No formal event system between Java components -- they share state through the database

**Configuration contracts:**
- Behavior controlled by database-stored configuration, property files, or environment variables
- These are rarely documented and usually discovered through code inspection

**Why this matters:** When the EPNM UI expects a specific JSON response shape, and the EMS backend provides a different shape for the same data, the Angular replacement needs to handle the translation. The POC will need to document these differences.

---

## 4. SNMP and CLI for Network Device Management

### 4.1 How EPNM Collects Device Data

EPNM is a Network Management System (NMS). Its core function is to discover, inventory, monitor, and manage network devices. It does this through two primary protocols:

**SNMP (Simple Network Management Protocol):**
- The standard protocol for network device monitoring
- EPNM polls devices periodically to collect inventory and status data
- Devices send traps (unsolicited notifications) to EPNM when events occur

**CLI (Command Line Interface) via SSH/Telnet:**
- Direct command execution on device operating systems (IOS, IOS-XR, NX-OS)
- Used for configuration retrieval, show commands, and device provisioning
- Referred to as "ECLI" in the EPNM meeting transcripts

### 4.2 SNMP Architecture

SNMP has three core components:

**NMS (Network Management Station):** EPNM acts as the NMS. It initiates SNMP requests to devices and receives SNMP traps from devices.

**SNMP Agent:** Software running on each managed device (router, switch, etc.) that responds to SNMP requests and sends traps.

**MIB (Management Information Base):** A hierarchical database of manageable objects. Each object has an OID (Object Identifier) -- a dotted numeric address that identifies a specific piece of data.

**SNMP Operations used by EPNM:**

| Operation | Purpose | Example |
|-----------|---------|---------|
| `GET` | Retrieve a single MIB object | Get hostname: `.1.3.6.1.2.1.1.5.0` |
| `GETNEXT` | Retrieve the next object in the MIB tree | Walk through interface table |
| `GETBULK` | Retrieve multiple objects efficiently (SNMPv2c/v3) | Bulk poll all interfaces |
| `SET` | Modify a MIB object on the device | Change admin status of an interface |
| `TRAP` / `INFORM` | Asynchronous notification from device | Link down, config change, threshold exceeded |

**MIB Walk (SNMP Walk):**
An SNMP walk iterates through a MIB subtree using repeated GETNEXT (or GETBULK) requests. This is how EPNM discovers what interfaces, modules, and configurations exist on a device. For example, walking the ifTable (`.1.3.6.1.2.1.2.2`) returns all interface entries with their names, types, speeds, and operational states.

**Common MIBs relevant to EPNM:**
- **IF-MIB** (interfaces) -- Interface names, types, speeds, operational status, traffic counters
- **ENTITY-MIB** (physical inventory) -- Chassis, slots, modules, fans, power supplies
- **CISCO-ENTITY-FRU-CONTROL-MIB** -- Cisco-specific field-replaceable unit information
- **SNMPv2-MIB** (system info) -- Hostname, sysDescr, uptime, contact, location
- **CISCO-PROCESS-MIB** -- CPU utilization
- **CISCO-MEMORY-POOL-MIB** -- Memory utilization
- **CISCO-CONFIG-MAN-MIB** -- Configuration change notifications

### 4.3 Java SNMP Libraries

EPNM's data collection services are written in Java. The primary Java SNMP library is **SNMP4J** -- an open-source, Apache-licensed, pure Java library supporting SNMPv1, v2c, and v3.

```java
// Conceptual example: SNMP GET using SNMP4J
Snmp snmp = new Snmp(new DefaultUdpTransportMapping());
snmp.listen();

CommunityTarget target = new CommunityTarget();
target.setCommunity(new OctetString("public"));
target.setAddress(GenericAddress.parse("udp:192.168.1.1/161"));
target.setVersion(SnmpConstants.version2c);

PDU pdu = new PDU();
pdu.add(new VariableBinding(new OID(".1.3.6.1.2.1.1.5.0"))); // sysName
pdu.setType(PDU.GET);

ResponseEvent response = snmp.send(pdu, target);
if (response.getResponse() != null) {
    String hostname = response.getResponse().get(0).getVariable().toString();
}
```

For trap handling, SNMP4J implements a `CommandResponder` interface that processes incoming notifications:

```java
// Conceptual: trap listener
snmp.addCommandResponder(new CommandResponder() {
    @Override
    public void processPdu(CommandResponderEvent event) {
        PDU pdu = event.getPDU();
        // Process trap -- extract OIDs, variable bindings
        // Store alarm in Oracle, update device status
    }
});
```

### 4.4 CLI-Based Device Interaction

For data that is not available via SNMP, or for device configuration and provisioning, EPNM connects to devices via SSH (or legacy Telnet) and executes CLI commands.

**Common patterns:**
- Execute `show` commands and parse the text output (screen scraping)
- Push configuration changes via `configure terminal` mode
- Manage device credentials and connection sessions

**In Java, CLI interaction typically uses:**
- **JSch** (Java Secure Channel) -- SSH library for establishing connections
- **Expect-style pattern matching** -- Send a command, wait for a prompt pattern, parse the output
- Custom parsers for each device type and command output format

```java
// Conceptual: CLI interaction via SSH
Session session = jsch.getSession("admin", "192.168.1.1", 22);
session.connect();
Channel channel = session.openChannel("shell");

// Send command
outputStream.write("show inventory\n".getBytes());

// Read output until prompt is detected
String output = readUntilPrompt(inputStream, "Router#");

// Parse the text output into structured data
List<InventoryItem> items = InventoryParser.parse(output);
```

**Why CLI parsing is fragile:**
- Output format varies by device platform (IOS vs. IOS-XR vs. NX-OS)
- Output format varies by software version
- Parsing relies on text patterns (regex, string matching) that can break with minor output changes
- This is the "screen scraping" problem -- a known pain point in network management

### 4.5 Data Flow: From Device to UI

Putting it all together, here is how a device's data gets from the network to the EPNM UI:

```
1. DISCOVERY
   EPNM scans an IP range or receives a device list
   -> SNMP GET sysDescr, sysName, sysObjectID
   -> Identifies device type, platform, software version
   -> Creates device record in Oracle

2. INVENTORY COLLECTION
   Scheduled polling job runs (e.g., every 24 hours)
   -> SNMP WALK of ENTITY-MIB (chassis, modules, ports)
   -> CLI "show inventory" for serial numbers, PIDs
   -> Parse responses into structured Java objects
   -> Store/update in Oracle (NETWORK_DEVICES, DEVICE_MODULES,
      DEVICE_INTERFACES tables)

3. STATUS MONITORING
   Frequent polling (e.g., every 5 minutes)
   -> SNMP GET interface operational status, counters
   -> Update Oracle with current status
   -> Detect state changes (up->down, threshold exceeded)

4. EVENT HANDLING
   Device sends SNMP trap
   -> EPNM trap listener receives and processes
   -> Alarm correlation engine determines severity, deduplication
   -> Store alarm in Oracle (ALARMS table)
   -> Notify UI (likely via polling or WebSocket)

5. UI RENDERING
   User opens Network Devices page
   -> Dojo grid widget requests /webacs/api/v4/data/Devices
   -> Java REST API queries Oracle
   -> Returns JSON with device list
   -> Dojo grid renders the table
```

### 4.6 What This Means for the POC

The POC does not involve SNMP or CLI -- the data collection layer stays as-is. But understanding the data flow matters because:

1. **The data shape is determined by what SNMP/CLI collects.** The fields shown in EPNM's inventory screens (hostname, IP, device type, serial number, module details, interface counters) originate from specific SNMP MIBs and CLI commands. The EMS backend collects the same data via the same protocols and stores it in PostgreSQL.

2. **The 10-20% gap may be in data collection, not just UI.** If certain SNMP MIBs or CLI commands are not implemented in the EMS data collection layer, the data simply will not be in PostgreSQL, and the classic UI will have nothing to show.

3. **Chassis views depend on device-type-specific knowledge.** The ChassisView component (from the ChassisView repo) renders physical device images. This requires knowing the physical layout of each device model -- information that comes from device-specific MIB data and pre-built device image assets.

---

## 5. Putting It All Together: Anatomy of an EPNM Screen

Here is a composite picture of what an EPNM inventory screen likely looks like in code, based on the technology patterns documented above. This is not actual EPNM code -- it is a representative example based on the stack.

### 5.1 The Page (JSP or HTML)

```html
<!-- Served by Java servlet or as static HTML -->
<div data-dojo-type="dijit/layout/BorderContainer" style="width:100%;height:100%">

    <!-- Left nav panel -->
    <div data-dojo-type="dijit/layout/ContentPane"
         data-dojo-props="region:'left', splitter:true"
         style="width:250px">
        <div data-dojo-type="epnm/nav/TreeMenu"
             data-dojo-props="selectedItem:'networkDevices'">
        </div>
    </div>

    <!-- Main content area -->
    <div data-dojo-type="dijit/layout/ContentPane"
         data-dojo-props="region:'center'">
        <div data-dojo-type="epnm/inventory/DeviceListPage"></div>
    </div>
</div>
```

### 5.2 The Widget (JavaScript AMD module)

```javascript
define([
    "dojo/_base/declare",
    "dijit/_WidgetBase",
    "dijit/_TemplatedMixin",
    "dojo/text!./templates/DeviceListPage.html",
    "dojo/store/JsonRest",
    "dojo/store/Observable",
    "dojo/topic",
    "dgrid/OnDemandGrid",
    "dgrid/Selection"
], function(declare, _WidgetBase, _TemplatedMixin, template,
            JsonRest, Observable, topic, OnDemandGrid, Selection) {

    return declare([_WidgetBase, _TemplatedMixin], {
        templateString: template,
        baseClass: "epnmDeviceListPage",

        postCreate: function() {
            this.inherited(arguments);

            // Create the data store (connects to Java REST API)
            this.deviceStore = Observable(new JsonRest({
                target: "/webacs/api/v4/data/Devices",
                idProperty: "deviceId"
            }));

            // Create the grid
            this.grid = new (declare([OnDemandGrid, Selection]))({
                store: this.deviceStore,
                columns: {
                    hostName: { label: "Device Name", sortable: true },
                    ipAddress: { label: "IP Address" },
                    productType: { label: "Device Type" },
                    reachability: { label: "Reachability" },
                    softwareVersion: { label: "Software Version" }
                },
                selectionMode: "single"
            }, this.gridNode);  // gridNode is a data-dojo-attach-point

            // Wire up selection to publish device selection event
            this.grid.on("dgrid-select", function(event) {
                var device = event.rows[0].data;
                topic.publish("epnm/device/selected", device);
            });
        },

        startup: function() {
            this.inherited(arguments);
            this.grid.startup();  // Grid needs startup after DOM placement
        },

        destroy: function() {
            this.grid.destroy();
            this.inherited(arguments);
        }
    });
});
```

### 5.3 The Java Backend (REST endpoint)

```java
@Path("/data/Devices")
public class DeviceResource {

    @Inject
    private DeviceService deviceService;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Response getDevices(
        @QueryParam(".full") @DefaultValue("false") boolean full,
        @QueryParam(".maxResults") @DefaultValue("50") int maxResults,
        @QueryParam(".firstResult") @DefaultValue("0") int firstResult,
        @QueryParam(".sort") String sortField
    ) {
        DeviceQuery query = new DeviceQuery(full, maxResults, firstResult, sortField);
        DeviceListResult result = deviceService.findDevices(query);

        // Returns JSON like:
        // { "queryResponse": { "@count": 1234, "entity": [ { ... }, { ... } ] } }
        return Response.ok(result).build();
    }
}
```

### 5.4 What the Angular Replacement Needs

For each EPNM screen, the conversion requires:
1. **Identify the data source** -- What REST endpoint does the Dojo store point to?
2. **Map to EMS equivalent** -- Does the EMS backend have an equivalent endpoint? What is the response shape?
3. **Translate the grid/widget configuration** -- Column definitions, sort behavior, pagination, selection mode, custom cell renderers
4. **Replicate event contracts** -- What topics does this widget publish/subscribe? Map these to Angular service calls
5. **Match the visual design** -- Extract CSS classes, colors, spacing from the Dojo theme and EPNM-specific styles
6. **Handle the toggle** -- The Angular component must support switching between EPNM-classic and EMS-modern themes

---

## 6. Key Risks and Conversion Challenges

### 6.1 Undocumented Behavior

In a 15+ year monolith, significant behavior lives in code that has no documentation. Quirks in sorting, filtering, or data transformation that users rely on may not be obvious from the UI alone -- they are embedded in the Dojo widget code, the Java service layer, or even Oracle stored procedures.

### 6.2 Custom Widget Complexity

EPNM likely has extensive custom Dijit widgets built on top of the base toolkit. These widgets may have accumulated complex behavior over many years -- conditional rendering, special cases for specific device types, workarounds for browser-specific issues. Each custom widget needs analysis before it can be rewritten.

### 6.3 Pub/Sub Dependency Web

The `dojo/topic` pub/sub system creates an invisible dependency graph. Widget A publishes "epnm/device/selected"; widgets B, C, and D subscribe to it. Removing or changing widget A's publication breaks B, C, and D with no compile-time error, no import chain, and no visible connection in the code structure. This must be mapped manually.

### 6.4 Data Shape Mismatches

The EPNM REST API and EMS REST API likely return different JSON structures for the same conceptual data. Field names, nesting, pagination format, and error handling may all differ. The Angular replacement must either:
- Adapt to the EMS API shape directly (changing the UI expectations), or
- Include an adapter/transformation layer that maps EMS responses to the shape the classic UI expects

### 6.5 Oracle-to-PostgreSQL Data Gaps

Some data that exists in Oracle (EPNM) may not have been carried over to PostgreSQL (EMS). This is part of the 10-20% functionality gap mentioned in the meetings. If a field is shown in an EPNM screen but the EMS backend does not provide it, the classic UI cannot display it regardless of how well the frontend is converted.

### 6.6 Device-Type-Specific Logic

Network management products contain extensive device-type-specific logic -- different parsing for IOS vs. IOS-XR, different chassis layouts for ASR 9000 vs. NCS 5500, different interface naming conventions per platform. This logic is embedded throughout the stack and will need to be handled in the conversion.

---

## Sources

### Dojo Toolkit References
- [Introduction to AMD Modules](https://dojotoolkit.org/documentation/tutorials/1.10/modules/)
- [The Dojo Loader](https://dojotoolkit.org/reference-guide/1.10/loader/amd.html)
- [Understanding _WidgetBase](https://dojotoolkit.org/documentation/tutorials/1.10/understanding_widgetbase/)
- [Dojo Widget Lifecycle](https://justinchmura.com/2015/02/28/dojo-widget-lifecycle/)
- [Creating Template-based Widgets](https://dojotoolkit.org/documentation/tutorials/1.10/templated/)
- [dijit/_TemplatedMixin](https://dojotoolkit.org/reference-guide/1.9/dijit/_TemplatedMixin.html)
- [dojo/_base/declare](https://dojotoolkit.org/reference-guide/1.9/dojo/_base/declare.html)
- [Using Declarative Syntax](https://dojotoolkit.org/documentation/tutorials/1.10/declarative/index.html)
- [dojo/parser](https://dojotoolkit.org/reference-guide/1.10/dojo/parser.html)
- [dojo/store](https://dojotoolkit.org/reference-guide/1.10/dojo/store.html)
- [Dojo Object Store Tutorial](https://dojotoolkit.org/documentation/tutorials/1.10/intro_dojo_store/)
- [dojo/store/Observable](https://dojotoolkit.org/reference-guide/1.9/dojo/store/Observable.html)
- [dojo/topic](https://dojotoolkit.org/reference-guide/1.9/dojo/topic.html)
- [Using Pub Sub with Dojo](https://davidwalsh.name/dojo-pub-sub)
- [Themes and Theming](https://dojotoolkit.org/reference-guide/1.6/dijit/themes.html)
- [dgrid (dojo1-dgrid)](https://github.com/dojo/dojo1-dgrid)
- [Working with the Grid](https://dojotoolkit.org/documentation/tutorials/1.10/working_grid/index.html)
- [Ajax with dojo/request](https://dojotoolkit.org/documentation/tutorials/1.10/ajax/)
- [dojo/request/xhr](https://dojotoolkit.org/reference-guide/1.10/dojo/request/xhr.html)
- [Dojo Object Stores (SitePen)](https://www.sitepen.com/blog/dojo-object-stores)

### Dojo Migration References
- [Dojo 1.x to 2.0 Migration Guide](https://dojotoolkit.org/reference-guide/1.9/releasenotes/migration-2.0.html)
- [Integrate ReactJS into a Legacy Dojo Application (IBM)](https://developer.ibm.com/articles/migrating-existing-legacy-application-in-dojo-to-react-step-by-step-guide/)
- [Using React Instead of Dijit with Dojo (10Clouds)](https://10clouds.com/blog/web/using-react-instead-of-dijit-with-dojo-toolkit/)
- [Upgrading from Dojo to React (Medium)](https://medium.com/mendix/upgrading-from-dojo-to-react-cfc6f9a17f66)
- [Mixing Dojo Widgets and Angular 2 Components (SitePen)](https://www.sitepen.com/blog/dojo-mixing-dojo-widgets-and-angular-2-components)

### Oracle Database References
- [Oracle Materialized Views](https://oracle-base.com/articles/misc/materialized-views)
- [Basic Materialized Views (Oracle Docs)](https://docs.oracle.com/database/122/DWHSG/basic-materialized-views.htm)
- [Calling Oracle Stored Procedures from Hibernate](https://vladmihalcea.com/how-to-call-oracle-stored-procedures-and-functions-from-hibernate/)
- [JPA Stored Procedures (Baeldung)](https://www.baeldung.com/jpa-stored-procedures)
- [JDBC Connection Pooling](https://docs.oracle.com/cd/B10501_01/java.920/a96654/connpoca.htm)
- [DataSource Objects and Connection Pools (Java EE 7)](https://docs.oracle.com/javaee/7/tutorial/resource-creation002.htm)
- [Oracle Exit Strategy -- Vendor Lock-In](https://newtglobal.com/cloud-migration-services/oracle-exit-strategy/)
- [Oracle Synonyms Migration (AWS)](https://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/chap-oracle-aurora-mysql.special.synonyms.html)

### Java Monolith References
- [From Monoliths to Microliths (Wipro)](https://wiprotechblogs.medium.com/from-monoliths-to-microliths-navigating-the-evolution-of-legacy-java-applications-5799c3a441fb)
- [How to Modernize a Legacy Java Monolith (Curotec)](https://www.curotec.com/insights/modernize-java-monolith-to-microservices/)
- [Enterprise Java Migration 2026](https://www.legacyleap.ai/blog/java-migration-guide/)
- [Breaking Down Monoliths (Java Code Geeks)](https://www.javacodegeeks.com/2025/10/breaking-down-monoliths-strategies-to-refactor-legacy-java-into-microservices.html)

### SNMP and Network Management References
- [SNMP (Wikipedia)](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol)
- [SNMP (NetworkAcademy)](https://www.networkacademy.io/ccna/network-services/simple-network-management-protocol-snmp)
- [SNMP Walk (SolarWinds)](https://www.solarwinds.com/resources/it-glossary/snmp-walk)
- [SNMP4J](https://www.snmp4j.org/)
- [Java and SNMP (O'Reilly)](https://www.oreilly.com/library/view/essential-snmp-2nd/0596008406/ch14.html)
- [Screen Scraping for Network Automation (ipSpace)](https://blog.ipspace.net/kb/CiscoAutomation/050-scraping/)

### Cisco EPNM References
- [Cisco EPNM Data Sheet](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/evolved-programmable-network-epn-manager/datasheet-c78-733928.html)
- [EPNM DevNet](https://developer.cisco.com/site/epnm/)
- [EPNM REST API Documentation](https://www.cisco.com/c/en/us/support/cloud-systems-management/evolved-programmable-network-epn-manager/products-programming-reference-guides-list.html)
