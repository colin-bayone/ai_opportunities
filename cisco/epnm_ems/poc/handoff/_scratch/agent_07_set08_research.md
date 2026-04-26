# Agent 07 Extraction: Set 08 Technical Research

**Source set:** Set 08 (2026-04-07) Technical Research
**Source files:**
- `08_research_epnm_legacy_stack_2026-04-07.md`
- `08_research_ems_modern_stack_2026-04-07.md`
- `08_research_conversion_patterns_2026-04-07.md`

**Purpose:** Preserve the technical reference material assembled to guide the execution session that will build a classic view toggle for two EMS screens (Inventory and Fault Management) within Cisco Crosswork Network Controller.

---

## 1. EPNM Legacy Stack: What the Execution Session Will Encounter

Source: `08_research_epnm_legacy_stack_2026-04-07.md`

### 1.1 Confirmed facts (from Set 07, 2026-04-06)

- EPNM frontend: Dojo (legacy version, 1.x branch)
- EPNM backend: Java monolith with Oracle database
- EPNM data collection: SNMP and CLI (called "ECLI") polling of network devices
- EMS frontend: Angular 21 with Harbor/Magnetic design system
- EMS backend: Spring Boot plus Go services with PostgreSQL

The POC reuses the existing EMS backend. The classic UI is a presentation overlay that reads from the same EMS REST APIs.

### 1.2 Dojo Toolkit 1.x core concepts

Dojo 1.x is a toolkit rather than an opinionated framework. Last stable release is 1.17.3. Dojo 2 plus is a complete TypeScript rewrite with no resemblance to 1.x. EPNM uses the legacy 1.x branch. No automated migration path exists; the conversion is a full rewrite.

### 1.3 AMD module system

Dojo 1.7 plus uses Asynchronous Module Definition (AMD) via `define()` and `require()`.

Representative pattern the execution session will see:

```javascript
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
- `define()` declares a module; `require()` loads modules for execution
- Dependency paths use slash notation (`dijit/form/Button`)
- The dependency array maps positionally to callback parameters
- `dojo/text!` plugin loads text files (typically HTML templates) as strings

Older EPNM code may use legacy pre-AMD format (synchronous loader forces all modules to load synchronously):

```javascript
dojo.provide("epnm.inventory.DeviceList");
dojo.require("dijit._Widget");
dojo.require("dijit._Templated");
```

### 1.4 Class system (dojo/_base/declare)

- Single inheritance (first argument in mixin array is the true superclass)
- Multiple mixin support via C3 superclass linearization (Python-style MRO)
- `this.inherited(arguments)` to call the parent implementation (similar to `super()`)
- Custom mixins prefixed with underscore by convention (e.g., `_DeviceFilterMixin`)

### 1.5 Dijit widget lifecycle

Every UI component in EPNM is a Dijit widget. Execution order:

| Method | When it runs | What to look for |
|--------|-------------|------------------|
| `constructor()` | Object instantiation, before any DOM exists | Parameter initialization, default values |
| `postMixInProperties()` | After properties mixed in, before DOM creation | Property computation, string assembly |
| `buildRendering()` | Creates DOM tree from the template | Usually handled by `_TemplatedMixin` |
| `postCreate()` | **Most important.** After DOM exists but before placed in document | Event binding, child widget refs, data loading, store connections |
| `startup()` | After widget and all children in DOM | Layout calculations, child widget startup |
| `destroy()` | Cleanup | Event listener removal, store disconnection |

Most widget logic lives in `postCreate()`. Start analysis of any EPNM widget there.

### 1.6 Templating system

Dijit widgets use HTML template strings with special attributes:

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

- `data-dojo-attach-point="nodeName"` creates a reference on the widget instance (`this.gridNode`)
- `data-dojo-attach-event="onclick: _onRefresh"` wires a DOM event to a widget method
- `${propertyName}` substitutes widget properties (one-time, not reactive)
- `_TemplatedMixin` turns the template into DOM during `buildRendering()`
- `_WidgetsInTemplateMixin` enables nested Dijit widgets within templates

### 1.7 Declarative markup (data-dojo-type and dojo/parser)

Widgets can be instantiated from HTML markup. The execution session must check both HTML/JSP markup and JavaScript for widget creation.

```html
<div data-dojo-type="dijit/layout/BorderContainer" style="width:100%;height:100%">
    <div data-dojo-type="dijit/layout/ContentPane"
         data-dojo-props="region: 'top'"
         class="headerPane">
    </div>
    <div data-dojo-type="epnm/inventory/DeviceList"
         data-dojo-props="autoLoad: true, pageSize: 50"
         data-dojo-attach-point="deviceListWidget">
    </div>
</div>
<script>
    require(["dojo/parser", "dojo/domReady!"], function(parser) {
        parser.parse();
    });
</script>
```

Key attributes:
- `data-dojo-type="module/path"`
- `data-dojo-props="key: value, key2: value2"` (JS object literal without outer braces)

### 1.8 Data stores (dojo/store API)

Core store types:

```javascript
// In-memory store
var memoryStore = new Memory({ data: [ /* ... */ ] });

// REST-backed store
var restStore = new JsonRest({
    target: "/webacs/api/v4/data/Devices",
    idProperty: "deviceId"
});

// Observable wrapper
var observableStore = Observable(restStore);

// Cache wrapper
var cachedStore = Cache(restStore, Memory());
```

Store API methods: `get(id)`, `query(queryParams, options)`, `put(object)`, `remove(id)`, `getIdentity(object)`.

Store composition pattern to expect: `Observable(Cache(JsonRest(...), Memory()))`.

Store URL targets map directly to backend REST endpoints. Cataloging JsonRest store targets reveals the complete API contract between frontend and backend.

### 1.9 Event handling and pub/sub

Two event systems:

**Direct DOM events (dojo/on):**

```javascript
require(["dojo/on"], function(on) {
    on(this.refreshButton, "click", function(evt) { /* ... */ });
});
```

**Global pub/sub (dojo/topic):**

```javascript
// Publish
topic.publish("epnm/device/selected", { deviceId: 12345 });

// Subscribe
var handle = topic.subscribe("epnm/device/selected", function(data) {
    console.log("Device selected:", data.deviceId);
});
// handle.remove() to unsubscribe
```

Pub/sub creates implicit contracts between loosely-coupled widgets. When analyzing EPNM code, catalog:
- All `topic.publish()` calls (messages sent)
- All `topic.subscribe()` calls (messages listened for)
- Topic name strings (form the internal event API)
- Data payloads (define the contract)

### 1.10 Grids (dgrid / dojox DataGrid)

Data grids are likely the most important widget type in EPNM. Two variants:

- **dojox/grid/DataGrid** (older, monolithic, uses `dojo/data` API)
- **dgrid** (newer since Dojo 1.7, lightweight, modular, built on `dojo/store`)

Representative dgrid:

```javascript
var grid = new (declare([OnDemandGrid, Selection, ColumnResizer, Pagination]))({
    store: observableStore,
    columns: {
        deviceName: {
            label: "Device Name",
            sortable: true,
            renderCell: function(object, value, node) {
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
}, "gridNode");
grid.startup();
```

### 1.11 Layout widgets

- `dijit/layout/BorderContainer` (regions: top, bottom, left, right, center)
- `dijit/layout/ContentPane` (static or lazy-loaded content)
- `dijit/layout/TabContainer` (tabbed content)
- `dijit/layout/AccordionContainer` (stacked panels)

EPNM uses left navigation panel, main content with tabbed views, popup/overlay panels (like Interface 360).

### 1.12 Theming

Dijit ships Claro, Tundra, Nihilo, Soria themes. Theming pattern:

```html
<link rel="stylesheet" href="dijit/themes/claro/claro.css">
<body class="claro">
```

EPNM is described as "blue and white" which does not match Claro defaults, suggesting a customized theme (Claro themes built with LESS CSS, variables in `dijit/themes/claro/variables.less`).

### 1.13 AJAX communication

Modern API (dojo/request/xhr, dojo 1.8+):

```javascript
require(["dojo/request/xhr"], function(xhr) {
    xhr("/webacs/api/v4/data/Devices.json", {
        method: "GET",
        handleAs: "json",
        query: { .full: true, .maxResults: 50 }
    }).then(
        function(data) { /* success */ },
        function(error) { /* error */ }
    );
});
```

Legacy API (pre-1.8, may still be present):

```javascript
dojo.xhrGet({
    url: "/webacs/api/v4/data/Devices.json",
    handleAs: "json",
    load: function(data) { /* success */ },
    error: function(error) { /* failure */ }
});
```

URL patterns observed: `/webacs/api/v4/...` is the known EPNM REST API base path.

### 1.14 Oracle persistence patterns

Data flow:

```
Network Devices (routers, switches, optical gear)
    | SNMP polling, CLI commands
    v
Data Collection Services (Java)
    | Parse responses, normalize data
    v
Oracle Database
    | JDBC queries
    v
Java Application Layer
    | JSON responses
    v
Dojo Frontend
```

Oracle integration patterns in the Java monolith:
- Raw JDBC with `PreparedStatement`, `ResultSet`, manual mapping
- JPA / Hibernate ORM with `@Entity`, `@Table`, `@Column`, `@OneToMany`
- Stored procedures / PL/SQL via `CallableStatement` with OUT parameters
- Connection pooling via JNDI DataSource on application server (WildFly, Tomcat, WebLogic)

Oracle-specific features likely in use:
- Sequences (`.NEXTVAL`) for primary keys
- Materialized views (dashboard summaries, device counts, alarm rollups)
- PL/SQL packages (alarm correlation, inventory reconciliation, aggregation, bulk device ops)
- `CONNECT BY`, `DECODE()`, `ROWNUM`, `NVL()`, `DUAL`, `(+)` outer joins
- Partitioning by date on event logs, performance data, polling history

### 1.15 Java monolith architecture

EPNM is part of a codebase spanning 45 to 50 million lines across 6 to 8 products. Characteristics:

- Single deployable unit (WAR or EAR) on Java EE application server
- Nominally layered: Presentation / Service / Data Access / Infrastructure / Database
- Layer violations common in legacy code: servlets executing SQL, logic in JSPs, DAOs with business rules
- Tight coupling: shared database, shared application context, shared class hierarchies across domains (inventory, faults, topology, provisioning)

Frontend-to-backend integration patterns (likely present in EPNM):

1. REST APIs (most common post-2010): JAX-RS / Spring MVC controllers returning JSON, consumed by JsonRest stores
2. Servlets returning JSON or HTML fragments (older subsystems)
3. JSP pages with embedded data where Dojo enhances pre-rendered DOM

### 1.16 Implicit contracts warning

Legacy monoliths have implicit rather than explicit interfaces:
- No formal OpenAPI spec for internal endpoints
- Database schema is the cross-component interface
- Configuration scattered across database, property files, environment variables
- The "contract" is whatever the code happens to send or receive

### 1.17 SNMP and CLI data collection

SNMP operations used by EPNM:

| Operation | Purpose |
|-----------|---------|
| `GET` | Retrieve a single MIB object |
| `GETNEXT` | Retrieve next object in MIB tree |
| `GETBULK` | Retrieve multiple objects (v2c/v3) |
| `SET` | Modify a MIB object |
| `TRAP` / `INFORM` | Async notification from device |

Relevant MIBs:
- IF-MIB (interfaces: names, types, speeds, operational status, counters)
- ENTITY-MIB (physical inventory: chassis, slots, modules, fans, PSUs)
- CISCO-ENTITY-FRU-CONTROL-MIB (FRU info)
- SNMPv2-MIB (system info: hostname, sysDescr, uptime)
- CISCO-PROCESS-MIB (CPU)
- CISCO-MEMORY-POOL-MIB (memory)
- CISCO-CONFIG-MAN-MIB (config change notifications)

Java SNMP library: SNMP4J (open-source, pure Java, SNMPv1/v2c/v3).

CLI interaction: SSH (modern) or Telnet (legacy), typically via JSch library with expect-style pattern matching. Fragile: format varies by platform (IOS vs IOS-XR vs NX-OS) and software version.

End-to-end data flow from device to UI:

```
1. DISCOVERY: EPNM scans IP range -> SNMP GET sysDescr/sysName/sysObjectID
   -> identifies type/platform/version -> creates device record in Oracle
2. INVENTORY COLLECTION: scheduled polling -> SNMP WALK ENTITY-MIB,
   CLI "show inventory" -> parse -> store in Oracle (NETWORK_DEVICES,
   DEVICE_MODULES, DEVICE_INTERFACES)
3. STATUS MONITORING: frequent polling -> SNMP GET operational status
   -> update Oracle -> detect state changes
4. EVENT HANDLING: device sends SNMP trap -> trap listener -> alarm
   correlation engine -> store in Oracle ALARMS table -> notify UI
5. UI RENDERING: user opens Network Devices -> Dojo grid requests
   /webacs/api/v4/data/Devices -> Java REST API queries Oracle
   -> JSON response -> Dojo grid renders
```

### 1.18 Named risks for the execution session

From Section 6 of the legacy stack research:

1. **Undocumented behavior** in the 15-plus-year monolith. Sorting, filtering, data transformation quirks users rely on may not be obvious from UI alone.
2. **Custom widget complexity.** Extensive EPNM-specific Dijit widgets with accumulated conditional rendering, device-type special cases, browser workarounds.
3. **Pub/Sub dependency web.** The `dojo/topic` system creates an invisible dependency graph with no compile-time errors, no import chain, no visible connection in code structure. Must be mapped manually.
4. **Data shape mismatches.** EPNM REST API vs EMS REST API likely return different JSON structures. Field names, nesting, pagination format, error handling may differ. Angular replacement must either adapt to EMS shape or include an adapter layer.
5. **Oracle-to-PostgreSQL data gaps.** Some Oracle data may not have been carried over; part of the 10 to 20 percent functionality gap. If a field exists in EPNM UI but not in EMS backend, classic UI cannot display it.
6. **Device-type-specific logic.** Different parsing for IOS vs IOS-XR, different chassis layouts (ASR 9000 vs NCS 5500), different interface naming conventions per platform.

---

## 2. EMS Modern Stack: What the Execution Session Will Work In

Source: `08_research_ems_modern_stack_2026-04-07.md`

### 2.1 Angular 21 (signals-first, zoneless core)

Angular 21 completed the transition to signals-first, zoneless architecture. Zone.js is no longer included by default.

#### Signals (reactive primitives)

```typescript
import { signal, computed, effect } from '@angular/core';

const count = signal(0);
console.log(count());         // read by calling
count.set(5);
count.update(v => v + 1);

const doubled = computed(() => count() * 2);

effect(() => {
  console.log(`Count is now: ${count()}`);
});
```

Signals are synchronous, have no subscription management, are read by calling them as functions.

#### Signal-based component I/O: input(), output(), model()

Replaces `@Input()` / `@Output()` decorators.

```typescript
import { Component, input, output, model } from '@angular/core';

@Component({
  selector: 'app-device-card',
  standalone: true,
  template: `
    <div class="device-card" (click)="cardClicked.emit(deviceId())">
      <h3>{{ deviceName() }}</h3>
      <span>Status: {{ status() }}</span>
    </div>
  `
})
export class DeviceCardComponent {
  deviceId = input.required<string>();
  deviceName = input.required<string>();
  status = input<string>('unknown');
  cardClicked = output<string>();
}
```

Two-way binding with `model()`:

```typescript
@Component({
  selector: 'app-view-toggle',
  standalone: true,
  template: `
    <button (click)="toggleView()">
      {{ isClassicView() ? 'Switch to EMS' : 'Switch to Classic' }}
    </button>
  `
})
export class ViewToggleComponent {
  isClassicView = model(false);
  toggleView() {
    this.isClassicView.set(!this.isClassicView());
  }
}
// Parent: <app-view-toggle [(isClassicView)]="showClassic" />
```

#### Standalone components (no NgModules)

Angular 21 defaults to standalone. Components declare their own imports directly:

```typescript
@Component({
  selector: 'app-alarm-list',
  standalone: true,
  imports: [CommonModule, FormsModule, AlarmRowComponent, FilterBarComponent],
  template: `...`
})
export class AlarmListComponent { }
```

#### Dependency injection with inject()

```typescript
@Component({ ... })
export class NetworkDevicesComponent {
  private inventoryService = inject(InventoryService);
  private router = inject(Router);
  private activatedRoute = inject(ActivatedRoute);
  devices = signal<Device[]>([]);
}
```

Services are typically provided at root level:

```typescript
@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);
  getDevices(): Observable<Device[]> {
    return this.http.get<Device[]>('/api/v1/inventory/devices');
  }
}
```

#### RxJS and HttpClient

HttpClient still returns Observables. Convert to signals at service or component level. Functional interceptors are preferred:

```typescript
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = inject(AuthService).getToken();
  const authReq = req.clone({
    headers: req.headers.set('Authorization', `Bearer ${authToken}`)
  });
  return next(authReq);
};

export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      if (error.status === 401) {
        inject(Router).navigate(['/login']);
      }
      return throwError(() => error);
    })
  );
};
```

#### Routing and lazy loading

```typescript
export const routes: Routes = [
  {
    path: 'inventory',
    loadComponent: () => import('./pages/inventory/network-devices.component')
      .then(m => m.NetworkDevicesComponent),
    children: [
      {
        path: 'device/:id',
        loadComponent: () => import('./pages/inventory/device-detail.component')
          .then(m => m.DeviceDetailComponent)
      },
      {
        path: 'device/:id/360',
        loadComponent: () => import('./pages/inventory/device-360.component')
          .then(m => m.Device360Component)
      }
    ]
  },
  {
    path: 'faults',
    loadComponent: () => import('./pages/faults/alarm-list.component')
      .then(m => m.AlarmListComponent)
  }
];
```

Toggle options for classic view:
1. Route-level switching: `/classic/inventory` vs `/inventory`
2. Component-level switching: same route, parent component conditionally renders classic or modern child
3. Theme-level switching: same components, different CSS/template via directive (only works if layout differences are minor)

#### Change detection

Zoneless by default. Change detection triggered by signal changes, template events, async pipe emissions, router navigation. Components should use `ChangeDetectionStrategy.OnPush` with signals:

```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class DeviceListComponent {
  devices = signal<Device[]>([]);
}
```

#### Angular Material and theming

EMS uses Harbor/Magnetic rather than Material, but Material patterns are useful reference. Material supports design tokens and custom themes via SCSS:

```scss
@use '@angular/material' as mat;

$classic-theme: mat.define-theme((
  color: (
    theme-type: light,
    primary: mat.$blue-palette,
  )
));

.classic-view {
  @include mat.all-component-themes($classic-theme);
}
```

### 2.2 Harbor and Magnetic design system

From Set 07 (Akhil): "If you look at the Crosswork UI, we have a Magnetic design system. So it's a design system called Harbor and Magnetic design system you're using."

- **Magnetic** is Cisco's company-wide design system, originally built by the Meraki team, publicly introduced July 2022. Rolled out across Cisco networking and security products. Aims to unify UI patterns so IT professionals see familiar constructs between tools.
- **Harbor** appears to be the Crosswork-specific implementation layer or component library that applies Magnetic design principles to the Crosswork product family (including EMS). Likely relationship: Magnetic equals design spec/tokens; Harbor equals Angular component library for Crosswork.
- GitHub: `github.com/cisco-magnetic` (organization exists; most repositories may be private)
- Cited research driver: 50 percent of security breaches happen because users struggle with complex product UIs. Magnetic aims to simplify.
- "Adoption-ready UI Shell components" completed: header, navigation, layout primitives, common patterns.
- Scope includes interaction patterns, accessibility, UX conventions; not just visual styling.

Implications for classic view:
- Current EMS view: Magnetic design (Harbor components), modern layout.
- Classic EPNM view: blue and white theme, left-side navigation, EPNM-familiar layout.
- Default on login: classic (EPNM) view.
- Toggle: user switches to EMS (Magnetic) view.

Classic view likely needs its own CSS theme (blue/white palette), compatible but visually different components, theme isolation that does not collide with Magnetic CSS (ViewEncapsulation helps; global styles need careful management), left navigation swap (EPNM sidebar vs EMS top menu).

Open questions from Set 07 (still unresolved):
- Are Harbor and Magnetic two layers or distinct? (Likely: Magnetic equals tokens/spec; Harbor equals Crosswork component library.)
- Does Harbor expose theming APIs supporting multiple themes? If so, classic view could be a Harbor theme rather than separate components.
- Is Common UI built on Harbor? If so, can Common UI be reused with different styling?

### 2.3 Spring Boot backend

Confirmed from Set 07: "Mostly Spring Boot, yes" for the backend.

Spring Boot 3.x uses Jakarta EE 9 plus. All imports use `jakarta.*` prefix (not `javax.*`).

#### REST controller pattern

```java
@RestController
@RequestMapping("/api/v1/inventory")
public class DeviceController {
    private final DeviceService deviceService;
    public DeviceController(DeviceService deviceService) {
        this.deviceService = deviceService;
    }

    @GetMapping("/devices")
    public ResponseEntity<Page<DeviceDTO>> getDevices(
            @RequestParam(required = false) String hostname,
            @RequestParam(required = false) String deviceType,
            Pageable pageable) {
        Page<DeviceDTO> devices = deviceService.getDevices(hostname, deviceType, pageable);
        return ResponseEntity.ok(devices);
    }

    @GetMapping("/devices/{id}")
    public ResponseEntity<DeviceDetailDTO> getDevice(@PathVariable Long id) {
        return ResponseEntity.ok(deviceService.getDeviceById(id));
    }

    @GetMapping("/devices/{id}/360")
    public ResponseEntity<Device360DTO> getDevice360(@PathVariable Long id) {
        return ResponseEntity.ok(deviceService.getDevice360(id));
    }
}
```

Classic view should not require new REST endpoints. If the classic view needs data shaped differently, the reshaping should happen in the Angular service layer (adapters), not by creating new backend endpoints.

#### Service layer pattern

```java
@Service
public class DeviceService {
    private final DeviceRepository deviceRepository;
    private final DeviceMapper deviceMapper;

    public Page<DeviceDTO> getDevices(String hostname, String deviceType, Pageable pageable) {
        Page<DeviceEntity> entities;
        if (hostname != null || deviceType != null) {
            entities = deviceRepository.findByFilters(hostname, deviceType, pageable);
        } else {
            entities = deviceRepository.findAll(pageable);
        }
        return entities.map(deviceMapper::toDTO);
    }
}
```

#### DTO pattern

Entities separated from API responses:

```java
@Entity
@Table(name = "network_devices")
public class DeviceEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "device_seq")
    @SequenceGenerator(name = "device_seq", sequenceName = "network_devices_id_seq")
    private Long id;
    @Column(name = "hostname") private String hostname;
    @Column(name = "ip_address") private String ipAddress;
    @Column(name = "device_type") private String deviceType;
    @Column(name = "software_version") private String softwareVersion;
    @Column(name = "last_polled_at") private Instant lastPolledAt;
}

public record DeviceDTO(
    Long id, String hostname, String ipAddress, String deviceType,
    String softwareVersion, String lastPolledAt
) {}
```

#### JPA repository pattern

```java
public interface DeviceRepository extends JpaRepository<DeviceEntity, Long> {
    @Query("SELECT d FROM DeviceEntity d WHERE " +
           "(:hostname IS NULL OR d.hostname LIKE %:hostname%) AND " +
           "(:deviceType IS NULL OR d.deviceType = :deviceType)")
    Page<DeviceEntity> findByFilters(
        @Param("hostname") String hostname,
        @Param("deviceType") String deviceType,
        Pageable pageable
    );
    Optional<DeviceEntity> findByIpAddress(String ipAddress);
}
```

#### Pagination

Spring Data JPA uses `Pageable`. Query parameters auto-parsed: `?page=0&size=20&sort=severity,desc`. Response includes `content`, `totalElements`, `totalPages`, `number`, `size`, `sort`.

Classic view EPNM table views must pass `page`, `size`, `sort` parameters to existing endpoints.

#### Global exception handling

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(
            new ErrorResponse(HttpStatus.NOT_FOUND.value(), ex.getMessage(), Instant.now())
        );
    }
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericError(Exception ex) {
        log.error("Unexpected error", ex);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(
            new ErrorResponse(HttpStatus.INTERNAL_SERVER_ERROR.value(),
                "Internal server error", Instant.now())
        );
    }
}
public record ErrorResponse(int status, String message, Instant timestamp) {}
```

Spring Boot 3.4 with virtual threads: 3.3x throughput vs platform threads, P99 drops from 85ms to 18ms under heavy load.

### 2.4 Go services

From Set 07 (Pradeep): "There are areas, at least on the device management side, and there are Go services running at the back end."

Go is used for specific backend services, primarily device management. Polyglot microservices pattern: Spring Boot for majority; Go for performance-sensitive device management.

Why Go:
- Concurrency via goroutines handles thousands of concurrent device connections efficiently
- First-class gNMI (gRPC Network Management Interface) support; OpenConfig reference at `github.com/openconfig/gnmi` is Go
- Excellent protobuf support for gRPC/gNMI
- Single static binary deployment
- Low memory footprint

Go in Cisco ecosystem: pipeline-gnmi (Model-Driven Telemetry collector supporting IOS XR, IOS XE, NX-OS), Netflix gnmi-gateway, Telegraf plugins for Cisco (IOS XR 6.5.1 plus, NX-OS 9.3 plus, IOS XE 16.12 plus).

Go and Spring Boot coexistence:
1. REST APIs (HTTP/JSON): simplest; most likely in EMS
2. gRPC (Protocol Buffers): higher-performance, type-safe cross-language
3. Message queues (Kafka, RabbitMQ): async
4. Shared database: tighter coupling, less preferred

Typical Go REST pattern:

```go
package main
import (
    "encoding/json"
    "net/http"
    "github.com/gorilla/mux"
)
type DeviceStatus struct {
    DeviceID    string `json:"device_id"`
    Hostname    string `json:"hostname"`
    Reachable   bool   `json:"reachable"`
    LastContact string `json:"last_contact"`
}
func getDeviceStatus(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    deviceID := vars["id"]
    status, err := pollDevice(deviceID)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(status)
}
func main() {
    r := mux.NewRouter()
    r.HandleFunc("/api/v1/devices/{id}/status", getDeviceStatus).Methods("GET")
    http.ListenAndServe(":8080", r)
}
```

Classic view typically does not interact with Go directly. Flow:

```
Angular -> Spring Boot (REST) -> Go service (internal API or gRPC) -> gNMI/SNMP/CLI -> Devices
```

Open questions: which EMS endpoints are Go vs Spring Boot; do Go services have direct frontend endpoints; is gRPC used for inter-service communication.

### 2.5 PostgreSQL (replacing Oracle)

From Set 07: "There's Postgres in the new product. We've gotten rid of Oracle dependency."

Classic view connects to the same Postgres as current EMS view; no Oracle connection.

#### Data type mapping

| Oracle | PostgreSQL | Notes |
|--------|-----------|-------|
| `VARCHAR2(n)` | `VARCHAR(n)` or `TEXT` | Postgres TEXT has no length limit |
| `NUMBER` | `NUMERIC`, `INTEGER`, `BIGINT` | Use most specific type |
| `DATE` | `TIMESTAMP` or `TIMESTAMPTZ` | Oracle DATE includes time; Postgres DATE does not |
| `CLOB` | `TEXT` | |
| `BLOB` | `BYTEA` | Binary |
| `RAW` | `BYTEA` | Binary |
| `SEQUENCE.NEXTVAL` | `nextval('sequence_name')` | Function syntax |

#### Date/time (critical)

Oracle `SYSDATE` returns server OS timezone; value does not change with session timezone. Postgres `now()`/`current_timestamp` returns session timezone. Postgres stores `TIMESTAMPTZ` as UTC internally, converts on display.

```sql
-- Oracle
SELECT SYSDATE FROM DUAL;
-- PostgreSQL
SELECT now();
SELECT now() AT TIME ZONE 'UTC';
SELECT clock_timestamp();
```

#### Primary keys

```java
@Id
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "device_seq")
@SequenceGenerator(name = "device_seq", sequenceName = "network_devices_id_seq",
                   allocationSize = 50)
private Long id;
```

`SEQUENCE` preferred over `IDENTITY` for Postgres (supports batch insert optimization via ID pre-fetching).

#### Function mapping

| Oracle | PostgreSQL |
|--------|-----------|
| `NVL(a, b)` | `COALESCE(a, b)` (accepts multiple args) |
| `DECODE(x, a, b, c)` | `CASE WHEN x = a THEN b ELSE c END` |
| `ROWNUM` | `LIMIT`/`OFFSET` or window `ROW_NUMBER()` |
| `SYSDATE` | `now()` or `current_timestamp` |
| `TO_DATE('...', 'fmt')` | `TO_DATE('...', 'fmt')` (format strings differ slightly) |
| `\|\|` | `\|\|` (same) |
| `SUBSTR(s, start, len)` | `SUBSTRING(s FROM start FOR len)` |

#### Packages and stored procedures

- Oracle packages to Postgres schemas
- Oracle procedures to Postgres procedures (`CREATE PROCEDURE`, supports transaction control)
- Oracle functions to Postgres functions (`CREATE FUNCTION`, single transaction)
- PL/SQL to PL/pgSQL (similar syntax; exception handling, loop bounds, variable scope differ)

PL/pgSQL differences:
- No global variables (use `SET`/custom GUC parameters)
- Functions run within a single transaction (no COMMIT/ROLLBACK inside functions)
- `RAISE` replaces `DBMS_OUTPUT.PUT_LINE`
- Integer `FOR` with `REVERSE` swaps bounds

#### Spring Boot + PostgreSQL config

```yaml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/ems_db
    username: ems_user
    password: ${DB_PASSWORD}
    driver-class-name: org.postgresql.Driver
  jpa:
    database-platform: org.hibernate.dialect.PostgreSQLDialect
    hibernate:
      ddl-auto: validate
    properties:
      hibernate:
        default_schema: ems
        jdbc:
          batch_size: 50
        order_inserts: true
        order_updates: true
```

### 2.6 Microservices architecture

EMS architecture overview:

```
Client Browser (Angular SPA: Infra UI -> Common UI -> EMS UI)
        |
        v REST/HTTP
API Gateway / Ingress (routing, auth, rate limiting)
        |
    +---+---+
    |       |
    v       v
Spring Boot   Go Services
(Inventory,   (Device
Faults, SIM)  Management)
    |       |
    v       v
PostgreSQL (shared or per-service)
    |
    v (SNMP, CLI, NETCONF, gNMI)
Network Devices
```

#### Shell app pattern (three-layer frontend)

| Layer | Repository | Purpose |
|-------|-----------|---------|
| Infra UI | Infra UI Repo | Shell app: header, top nav, infrastructure components. Outermost layer. |
| Common UI | Common UI Repo | Shared component library: cards, tables, design system widgets (Harbor/Magnetic). |
| EMS UI | EMS UI Repo | Feature pages: inventory views, fault management, SIM, device details. |

Infra UI owns bootstrap, authentication, layout frame. Common UI likely consumed as npm package or linked library. EMS UI registers routes and feature components within the shell. Classic view code lives in EMS UI (or new repo), registers its own routes or variant components within the same shell.

#### Service boundaries

- Inventory Service: devices, details, 360, chassis view
- Fault/Alarm Service: alarms, events, syslogs, correlated alarms
- Device Management Service: device communication, polling, config (likely Go)
- Topology Service: topology maps
- Software Image Management (SIM): images, upgrade management
- User/Auth Service

#### Service discovery (Kubernetes)

Crosswork uses Kubernetes:
- Services expose pods via stable DNS (`inventory-service.ems.svc.cluster.local`)
- CoreDNS resolves service names to pod IPs
- No external service registry
- Ingress controllers (often Envoy) route external traffic

```yaml
device-management:
  service:
    url: ${DEVICE_MGMT_URL:http://device-management-service:8080}
```

Containerization confirmed by Crosswork architecture docs. Health: Healthy / Degraded / Down. System health aggregates service health.

Classic view is purely a frontend concern:
1. No new backend services needed
2. Same auth flow (handled by Infra UI shell)
3. Same API gateway
4. Toggle state storage options: frontend-only (localStorage), user preference API, URL-based
5. Classic view components must be part of EMS UI bundle; lazy loading important

### 2.7 Priority summary

| Priority | Technology | Focus |
|----------|-----------|-------|
| Critical | Angular 21 | Signals, standalone components, inject(), lazy loading, OnPush. Patterns the codebase uses. |
| Critical | Harbor/Magnetic | Understanding existing component library for coexistence. Theme isolation strategy. |
| Important | Spring Boot | REST controller patterns and DTO shapes. API contract the classic view consumes. No new backend code. |
| Important | PostgreSQL | Data types, timestamp handling, NULL behavior. |
| Contextual | Go services | Know they exist for device management. Classic view calls Spring Boot; Spring Boot calls Go internally. |
| Contextual | Microservices architecture | Shell app pattern (Infra UI -> Common UI -> EMS UI). Classic view lives in or alongside EMS UI. |

---

## 3. Conversion Pattern Reference

Source: `08_research_conversion_patterns_2026-04-07.md`

### 3.1 Complete Dojo-to-Angular widget mapping table

From Section 1.5 of the conversion patterns research:

| Dojo Widget | Angular Equivalent | Notes |
|---|---|---|
| `dojox/grid/DataGrid` | `mat-table` + `MatSort` + `MatPaginator` | Main table widget |
| `dgrid/Grid` | `mat-table` | Newer Dojo grid, same mapping |
| `dijit/Dialog` | `MatDialog.open()` | Device 360 dialogs, confirmations |
| `dijit/TooltipDialog` | `MatMenu` or `cdkOverlayOrigin` | Popup panels like Device 360 |
| `dijit/Tree` | `MatTree` / `CdkTree` | Chassis trees, nav menus |
| `dijit/form/TextBox` | `<input matInput>` + `FormControl` | |
| `dijit/form/ValidationTextBox` | `FormControl` + `Validators` | Validators replace regex property |
| `dijit/form/FilteringSelect` | `<mat-select>` or `<mat-autocomplete>` | Autocomplete for type-ahead |
| `dijit/form/ComboBox` | `<mat-autocomplete>` + free text | Allows non-listed values |
| `dijit/form/Select` | `<mat-select>` | Simple dropdown |
| `dijit/form/CheckBox` | `<mat-checkbox>` | Use with formControlName |
| `dijit/form/RadioButton` | `<mat-radio-group>` + `<mat-radio-button>` | Wrap in FormControl |
| `dijit/form/NumberSpinner` | `<input matInput type="number">` | Step buttons manual |
| `dijit/form/DateTextBox` | `<mat-datepicker>` | MatDatepickerModule |
| `dijit/form/Button` | `<button mat-button>` or `<button mat-raised-button>` | Style variants via mat- prefix |
| `dijit/ProgressBar` | `<mat-progress-bar>` | determinate, indeterminate, buffer |
| `dijit/TabContainer` | `<mat-tab-group>` + `<mat-tab>` | Device 360 tabs |
| `dijit/layout/ContentPane` | Angular component with `<ng-content>` | Content projection |
| `dijit/layout/BorderContainer` | CSS Grid or Flexbox | No direct widget |
| `dijit/layout/AccordionContainer` | `<mat-accordion>` + `<mat-expansion-panel>` | Collapsible sections |
| `dijit/Toolbar` | `<mat-toolbar>` | Action bar above tables |
| `dijit/Menu` / `dijit/MenuItem` | `<mat-menu>` + `<mat-menu-item>` | Context, action menus |
| `dijit/Tooltip` | `matTooltip` directive | Inline tooltip |
| `dojox/widget/Toaster` | `MatSnackBar` | Toast notifications |

### 3.2 DataGrid conversion example

Dojo DataGrid:

```javascript
var store = new ItemFileWriteStore({
  data: {
    identifier: "id",
    items: [ { id: 1, hostname: "router-01", ipAddress: "10.0.0.1", status: "Managed", deviceType: "Cisco ASR 9000" } ]
  }
});
var layout = [
  { field: "hostname", name: "Device Name", width: "200px" },
  { field: "ipAddress", name: "IP Address", width: "150px" },
  { field: "status", name: "Status", width: "100px" },
  { field: "deviceType", name: "Device Type", width: "auto",
    formatter: function(value) {
      return "<span class='device-type'>" + value + "</span>";
    }
  }
];
var grid = new DataGrid({
  store: store,
  structure: layout,
  rowSelector: "20px",
  clientSort: true,
  query: { hostname: "*" }
}, "gridDiv");
grid.startup();
```

Angular Material Table equivalent:

```typescript
@Component({
  selector: 'app-network-devices-classic',
  standalone: true,
  imports: [MatTableModule, MatSortModule, MatPaginatorModule],
  templateUrl: './network-devices-classic.component.html',
  styleUrls: ['./network-devices-classic.component.scss']
})
export class NetworkDevicesClassicComponent implements OnInit {
  private inventoryService = inject(InventoryService);
  displayedColumns: string[] = ['hostname', 'ipAddress', 'status', 'deviceType'];
  dataSource = new MatTableDataSource<NetworkDevice>();
  @ViewChild(MatSort) sort!: MatSort;
  @ViewChild(MatPaginator) paginator!: MatPaginator;

  ngOnInit(): void {
    this.inventoryService.getNetworkDevices().subscribe(devices => {
      this.dataSource.data = devices;
    });
  }
  ngAfterViewInit(): void {
    this.dataSource.sort = this.sort;
    this.dataSource.paginator = this.paginator;
  }
}
```

```html
<div class="epnm-table-container">
  <table mat-table [dataSource]="dataSource" matSort class="epnm-data-grid">
    <ng-container matColumnDef="hostname">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Device Name</th>
      <td mat-cell *matCellDef="let device">
        <a class="epnm-device-link" (click)="openDeviceDetails(device)">
          {{ device.hostname }}
        </a>
      </td>
    </ng-container>
    <ng-container matColumnDef="ipAddress">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>IP Address</th>
      <td mat-cell *matCellDef="let device">{{ device.ipAddress }}</td>
    </ng-container>
    <ng-container matColumnDef="status">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Status</th>
      <td mat-cell *matCellDef="let device">
        <span [class]="'epnm-status epnm-status--' + device.status.toLowerCase()">
          {{ device.status }}
        </span>
      </td>
    </ng-container>
    <ng-container matColumnDef="deviceType">
      <th mat-header-cell *matHeaderCellDef mat-sort-header>Device Type</th>
      <td mat-cell *matCellDef="let device">
        <span class="epnm-device-type">{{ device.deviceType }}</span>
      </td>
    </ng-container>
    <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
    <tr mat-row *matRowDef="let row; columns: displayedColumns;"
        (click)="selectDevice(row)"
        [class.selected]="selectedDevice === row">
    </tr>
  </table>
  <mat-paginator [pageSizeOptions]="[25, 50, 100]" showFirstLastButtons>
  </mat-paginator>
</div>
```

Mapping notes:
- Dojo `structure` array to `matColumnDef` definitions
- Dojo `formatter` function to Angular template expressions within `*matCellDef`
- Dojo `store` to `MatTableDataSource`
- Dojo `clientSort: true` to `matSort` directive + ViewChild
- Dojo `rowSelector` to `(click)` on `mat-row`
- Dojo `query` to service-level filtering or `dataSource.filter`

### 3.3 Dialog conversion example

Dojo Dialog:

```javascript
var device360Dialog = new Dialog({
  title: "Device 360 - router-01",
  content: "<div id='device360Content'></div>",
  style: "width: 800px; height: 600px;",
  onHide: function() { /* cleanup */ }
});
device360Dialog.set("content", buildDevice360Content(deviceData));
device360Dialog.show();
```

Angular Material Dialog:

```typescript
@Component({
  selector: 'app-device-360-classic',
  standalone: true,
  imports: [MatDialogModule],
  templateUrl: './device-360-classic.component.html',
  styleUrls: ['./device-360-classic.component.scss']
})
export class Device360ClassicComponent {
  private dialogRef = inject(MatDialogRef<Device360ClassicComponent>);
  data: { device: NetworkDevice } = inject(MAT_DIALOG_DATA);
  activeTab = 'alarms';
  close(): void { this.dialogRef.close(); }
  openInterface360(interfaceData: any): void {
    // Nested dialog pattern mirrors EPNM "360 inside 360"
  }
}

// Parent:
export class NetworkDevicesClassicComponent {
  private dialog = inject(MatDialog);
  openDevice360(device: NetworkDevice): void {
    this.dialog.open(Device360ClassicComponent, {
      data: { device },
      width: '800px',
      height: '600px',
      panelClass: 'epnm-dialog-container'
    });
  }
}
```

Mapping notes:
- `new Dialog({ content: ... })` to `MatDialog.open(ComponentClass, config)`
- `dialog.show()` returns `MatDialogRef`
- `dialog.set("content", html)` to Angular template rendering in dialog component
- `onHide` callback to `MatDialogRef.afterClosed().subscribe()`
- Nested dialogs supported via injected MatDialog from within dialog component
- `panelClass` applies EPNM CSS without affecting global theme

### 3.4 Tree conversion example

Dojo Tree uses `Memory` store with `getChildren`, `ObjectStoreModel` with `mayHaveChildren`, and `Tree` widget. Angular equivalent uses `MatTreeFlattener` + `MatTreeFlatDataSource` + `FlatTreeControl`:

```typescript
interface ChassisNode {
  id: string;
  name: string;
  type: 'chassis' | 'module' | 'port';
  children?: ChassisNode[];
}
interface FlatChassisNode {
  expandable: boolean;
  name: string;
  type: string;
  level: number;
}

@Component({
  selector: 'app-chassis-tree-classic',
  standalone: true,
  imports: [MatTreeModule, MatIconModule, MatButtonModule],
  template: `
    <mat-tree [dataSource]="dataSource" [treeControl]="treeControl" class="epnm-tree">
      <mat-tree-node *matTreeNodeDef="let node" matTreeNodePadding>
        <button mat-icon-button disabled></button>
        <span class="epnm-tree-node epnm-tree-node--{{node.type}}"
              (click)="selectNode(node)">
          {{ node.name }}
        </span>
      </mat-tree-node>
      <mat-tree-node *matTreeNodeDef="let node; when: hasChild" matTreeNodePadding>
        <button mat-icon-button matTreeNodeToggle>
          <mat-icon>
            {{ treeControl.isExpanded(node) ? 'expand_more' : 'chevron_right' }}
          </mat-icon>
        </button>
        <span class="epnm-tree-node epnm-tree-node--{{node.type}}"
              (click)="selectNode(node)">
          {{ node.name }}
        </span>
      </mat-tree-node>
    </mat-tree>
  `
})
export class ChassisTreeClassicComponent implements OnInit {
  private transformer = (node: ChassisNode, level: number): FlatChassisNode => ({
    expandable: !!node.children && node.children.length > 0,
    name: node.name,
    type: node.type,
    level: level,
  });
  treeControl = new FlatTreeControl<FlatChassisNode>(
    node => node.level, node => node.expandable
  );
  treeFlattener = new MatTreeFlattener(
    this.transformer,
    node => node.level,
    node => node.expandable,
    node => node.children
  );
  dataSource = new MatTreeFlatDataSource(this.treeControl, this.treeFlattener);
  hasChild = (_: number, node: FlatChassisNode) => node.expandable;
}
```

Mapping notes:
- Dojo `Memory` store with `getChildren` to Angular nested data structure with `children`
- Dojo `ObjectStoreModel` to `MatTreeFlattener` + `MatTreeFlatDataSource`
- Dojo `mayHaveChildren` to Angular `hasChild` function
- Dojo `onClick` to `(click)` binding
- Dojo `tree.startup()` handled automatically by Angular data binding

### 3.5 Form widget conversion

Dojo form widgets (`TextBox`, `FilteringSelect`, `CheckBox`, `NumberSpinner`) map to Angular Reactive Forms with `FormControl`/`FormGroup`/`FormBuilder`:

```typescript
@Component({
  selector: 'app-add-device-classic',
  standalone: true,
  imports: [
    ReactiveFormsModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatCheckboxModule, MatStepperModule
  ],
})
export class AddDeviceClassicComponent implements OnInit {
  private fb = inject(FormBuilder);
  deviceInfoForm!: FormGroup;
  credentialsForm!: FormGroup;
  deviceTypes = [
    { id: 'asr9k', name: 'Cisco ASR 9000' },
    { id: 'nexus9k', name: 'Cisco Nexus 9000' },
    { id: 'ncs5500', name: 'Cisco NCS 5500' }
  ];

  ngOnInit(): void {
    this.deviceInfoForm = this.fb.group({
      ipAddress: ['', [Validators.required, this.ipAddressValidator]],
      deviceType: ['', Validators.required]
    });
    this.credentialsForm = this.fb.group({
      snmpEnabled: [true],
      snmpCommunity: [''],
      telnetEnabled: [false],
      telnetUsername: [''],
      telnetPassword: [''],
      httpEnabled: [false]
    });
    // Reactive valueChanges replaces Dojo onChange
    this.credentialsForm.get('snmpEnabled')!.valueChanges.subscribe(enabled => {
      const snmpCommunity = this.credentialsForm.get('snmpCommunity')!;
      if (enabled) {
        snmpCommunity.setValidators(Validators.required);
      } else {
        snmpCommunity.clearValidators();
      }
      snmpCommunity.updateValueAndValidity();
    });
  }
  private ipAddressValidator(control: any) {
    const ipRegex = /^(\d{1,3}\.){3}\d{1,3}$/;
    return ipRegex.test(control.value) ? null : { invalidIP: true };
  }
}
```

Mapping notes:
- `TextBox` to `<input matInput>` + `formControlName`
- `FilteringSelect` + `store` to `<mat-select>` + `<mat-option>` loop (or `mat-autocomplete` for type-ahead)
- `CheckBox` + `onChange` to `formControlName` + `valueChanges.subscribe()`
- `required: true` to `Validators.required`
- `intermediateChanges` to `valueChanges` Observable (emits every keystroke)
- Wizard to `<mat-stepper>` with `linear` mode
- `placeHolder` to `placeholder` attribute or `<mat-label>`

### 3.6 AMD to ES6 module mapping

| AMD Pattern | ES6/Angular Equivalent |
|---|---|
| `define(["dep1", "dep2"], function(dep1, dep2) { ... })` | `import { dep1 } from 'dep1'; import { dep2 } from 'dep2';` |
| `require(["module"], function(Module) { ... })` | `import { Module } from './module';` or dynamic `import('./module')` |
| `dojo/_base/declare("ClassName", [Base1, Base2], { ... })` | `class ClassName extends Base1 implements Interface2 { ... }` |
| `dojo/text!./template.html` | `templateUrl: './template.html'` in `@Component` |
| `dojo/i18n!./nls/strings` | `@ngx-translate` or built-in `$localize` |
| `return declare(...)` | `export class ...` or `export default class ...` |
| `this.inherited(arguments)` | `super.methodName()` |
| Dependencies via `define()` callback args | Services via `inject()` or constructor DI |

Automated tool: `amd-to-es6` npm package performs mechanical AMD to ES6 transformation but does not handle Dojo-specific patterns (`declare()`, `this.inherited()`, Dijit lifecycle).

```bash
npm install -g amd-to-es6
amd-to-es6 src/legacy/NetworkDevicesView.js
```

### 3.7 Data binding translation (Dojo watch to Angular signals/observables)

| Dojo Pattern | Angular Equivalent | When to Use |
|---|---|---|
| `widget.get("prop")` | `this.prop` or `this.prop()` (signal) | Reading state |
| `widget.set("prop", value)` | `this.prop = value` or `this.prop.set(value)` | Setting state |
| `widget.watch("prop", callback)` | `effect(() => { ... })` (signal) or `ngOnChanges()` | Reacting to property changes |
| `_setFooAttr(value)` custom setter | `set` accessor, or `effect()` with side effects | Custom on-change logic |
| Template substitution `${prop}` | `{{ prop }}` interpolation or `[attr]="prop"` | Rendering values |
| `data-dojo-attach-point` | `@ViewChild()` / `#templateRef` | DOM element references |
| `data-dojo-attach-event` | `(event)="handler()"` | Binding DOM events |

Example patterns:

```typescript
// Signal-based inputs (Angular 17+, preferred for Angular 21)
@Component({
  template: `
    <span class="device-name">{{ deviceName() }}</span>
    <span [class.online]="isOnline()">{{ isOnline() ? 'Online' : 'Offline' }}</span>
  `
})
export class DeviceWidgetComponent {
  deviceName = input.required<string>();
  isOnline = input<boolean>(true);
  statusChange = output<boolean>();
  constructor() {
    effect(() => {
      console.log('isOnline changed to:', this.isOnline());
    });
  }
}

// model() for two-way binding
@Component({
  template: `
    <input [ngModel]="filterText()" (ngModelChange)="filterText.set($event)">
  `
})
export class DeviceFilterComponent {
  filterText = model<string>('');
}
```

### 3.8 Event handling translation (pub/sub to RxJS)

| Dojo Pattern | Angular Equivalent | Scope |
|---|---|---|
| `dojo/topic.publish` / `topic.subscribe` | Shared service with `Subject` | Cross-component |
| `dojo/on(domNode, event, handler)` | `(event)="handler()"` template binding | Single component DOM |
| `widget.emit("customEvent", data)` | `@Output() customEvent = new EventEmitter()` | Child to parent |
| `dojo/aspect.after(obj, method, callback)` | RxJS `tap()` in pipe, or HTTP interceptor | Method interception |
| `dojo/Evented` base class | Service extending `Subject` | Event-emitting objects |
| Parent calling child method directly | `@ViewChild(ChildComponent)` | Parent to child (imperative) |
| Shared data store | Service with `BehaviorSubject` | Cross-component state |

Shared service example replacing `dojo/topic`:

```typescript
export interface DeviceSelectedEvent {
  deviceId: string;
  ip: string;
}

@Injectable({ providedIn: 'root' })
export class EventBusService {
  private deviceSelected$ = new Subject<DeviceSelectedEvent>();
  private alarmAcknowledged$ = new Subject<string>();

  emitDeviceSelected(event: DeviceSelectedEvent): void {
    this.deviceSelected$.next(event);
  }
  onDeviceSelected(): Observable<DeviceSelectedEvent> {
    return this.deviceSelected$.asObservable();
  }
  emitAlarmAcknowledged(alarmId: string): void {
    this.alarmAcknowledged$.next(alarmId);
  }
  onAlarmAcknowledged(): Observable<string> {
    return this.alarmAcknowledged$.asObservable();
  }
}

// Publisher
export class NetworkDevicesClassicComponent {
  private eventBus = inject(EventBusService);
  selectDevice(device: NetworkDevice): void {
    this.eventBus.emitDeviceSelected({
      deviceId: device.id,
      ip: device.ipAddress
    });
  }
}

// Subscriber
export class DeviceDetailPanelComponent implements OnInit, OnDestroy {
  private eventBus = inject(EventBusService);
  private destroy$ = new Subject<void>();
  ngOnInit(): void {
    this.eventBus.onDeviceSelected()
      .pipe(takeUntil(this.destroy$))
      .subscribe(event => this.loadDeviceDetails(event.deviceId));
  }
  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

HTTP interceptor replaces `dojo/aspect` for method interception patterns:

```typescript
@Injectable()
export class TimestampInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (req.method === 'PUT' || req.method === 'POST') {
      const modified = req.clone({
        body: { ...req.body, lastModified: new Date().toISOString() }
      });
      return next.handle(modified);
    }
    return next.handle(req);
  }
}
```

### 3.9 Lifecycle hook translation

| Dojo Lifecycle | Angular Lifecycle | When / Purpose |
|---|---|---|
| `constructor(params)` | `constructor()` | Object creation, DI. Avoid side effects in Angular. |
| `postMixInProperties()` | `ngOnChanges()` (first call) or field initializers | Compute derived properties from inputs before rendering |
| `buildRendering()` | (handled by template compiler) | DOM creation, no Angular equivalent |
| `postCreate()` | **`ngOnInit()`** | Primary initialization. Main mapping. Most postCreate code moves here. |
| `startup()` | **`ngAfterViewInit()`** | DOM-dependent init. Measure DOM, init third-party libs, access ViewChild refs. |
| `destroy()` | **`ngOnDestroy()`** | Cleanup. Unsubscribe. Use `takeUntil(this.destroy$)` pattern or `DestroyRef`. |
| `resize()` (dijit layout) | `@HostListener('window:resize')` or `ResizeObserver` | Resize handling |

Concrete full-lifecycle conversion example (AlarmPanel):

Dojo:

```javascript
define([
  "dojo/_base/declare",
  "dijit/_WidgetBase",
  "dijit/_TemplatedMixin",
  "dojo/on",
  "dojo/topic",
  "dojo/store/JsonRest",
  "dojo/text!./templates/AlarmPanel.html"
], function(declare, _WidgetBase, _TemplatedMixin, on, topic, JsonRest, template) {
  return declare("epnm.alarms.AlarmPanel", [_WidgetBase, _TemplatedMixin], {
    templateString: template,
    deviceId: null,
    refreshInterval: 30000,
    postMixInProperties: function() {
      this.inherited(arguments);
      this._alarmStore = new JsonRest({ target: "/api/v1/alarms" });
    },
    postCreate: function() {
      this.inherited(arguments);
      this._loadAlarms();
      this._topicHandle = topic.subscribe("device/selected", function(data) {
        this.set("deviceId", data.deviceId);
        this._loadAlarms();
      }.bind(this));
    },
    startup: function() {
      this.inherited(arguments);
      this._resizeGrid();
      this._timer = setInterval(this._loadAlarms.bind(this), this.refreshInterval);
    },
    _loadAlarms: function() {
      if (!this.deviceId) return;
      this._alarmStore.query({ deviceId: this.deviceId }).then(function(alarms) {
        this._renderAlarms(alarms);
      }.bind(this));
    },
    destroy: function() {
      if (this._topicHandle) this._topicHandle.remove();
      if (this._timer) clearInterval(this._timer);
      this.inherited(arguments);
    }
  });
});
```

Angular equivalent:

```typescript
import { Component, OnInit, AfterViewInit, OnDestroy, input, inject } from '@angular/core';
import { Subject, interval, switchMap, takeUntil, filter } from 'rxjs';

@Component({
  selector: 'app-alarm-panel-classic',
  standalone: true,
  imports: [/* material modules */],
  templateUrl: './alarm-panel-classic.component.html',
  styleUrls: ['./alarm-panel-classic.component.scss']
})
export class AlarmPanelClassicComponent implements OnInit, AfterViewInit, OnDestroy {
  private alarmService = inject(AlarmService);
  private eventBus = inject(EventBusService);
  private destroy$ = new Subject<void>();
  deviceId: string | null = null;
  refreshInterval = 30000;
  alarms: Alarm[] = [];

  ngOnInit(): void {
    this.loadAlarms();
    this.eventBus.onDeviceSelected()
      .pipe(takeUntil(this.destroy$))
      .subscribe(event => {
        this.deviceId = event.deviceId;
        this.loadAlarms();
      });
    interval(this.refreshInterval)
      .pipe(
        filter(() => this.deviceId !== null),
        switchMap(() => this.alarmService.getAlarms(this.deviceId!)),
        takeUntil(this.destroy$)
      )
      .subscribe(alarms => { this.alarms = alarms; });
  }

  ngAfterViewInit(): void { this.resizeGrid(); }

  private loadAlarms(): void {
    if (!this.deviceId) return;
    this.alarmService.getAlarms(this.deviceId)
      .pipe(takeUntil(this.destroy$))
      .subscribe(alarms => { this.alarms = alarms; });
  }

  private resizeGrid(): void { /* DOM-dependent calcs */ }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }
}
```

### 3.10 State management translation (stores to services)

| Dojo Store | Angular Equivalent | Purpose |
|---|---|---|
| `dojo/store/Memory` | Service with `BehaviorSubject<T[]>` | Client-side in-memory data |
| `dojo/store/JsonRest` | Service with `HttpClient` | Server-side REST data access |
| `dojo/store/Cache` | Service with `BehaviorSubject` + `HttpClient` + cache logic | Caching layer over server data |
| `dojo/store/Observable` | `BehaviorSubject` (inherently observable) | Change notifications on mutations |
| `store.query(filter)` | `HttpClient.get(url, { params })` or `BehaviorSubject.pipe(map(filter))` | Query/filter |
| `store.get(id)` | `HttpClient.get(url/id)` or `BehaviorSubject.value.find()` | Single item |
| `store.put(item)` | `HttpClient.put()` + `BehaviorSubject.next()` | Update |
| `store.add(item)` | `HttpClient.post()` + `BehaviorSubject.next()` | Create |
| `store.remove(id)` | `HttpClient.delete()` + `BehaviorSubject.next()` | Delete |

Memory store to in-memory state service:

```typescript
@Injectable({ providedIn: 'root' })
export class DeviceStateService {
  private devices$ = new BehaviorSubject<NetworkDevice[]>([
    { id: 1, name: 'router-01', status: 'online' },
    { id: 2, name: 'switch-01', status: 'offline' }
  ]);
  getDevices(): Observable<NetworkDevice[]> { return this.devices$.asObservable(); }
  getDevice(id: number): NetworkDevice | undefined {
    return this.devices$.value.find(d => d.id === id);
  }
  queryDevices(filter: Partial<NetworkDevice>): Observable<NetworkDevice[]> {
    return this.devices$.pipe(
      map(devices => devices.filter(d =>
        Object.entries(filter).every(([key, val]) =>
          d[key as keyof NetworkDevice] === val
        )
      ))
    );
  }
  updateDevice(device: NetworkDevice): void {
    const current = this.devices$.value;
    const index = current.findIndex(d => d.id === device.id);
    if (index >= 0) {
      current[index] = device;
      this.devices$.next([...current]);
    }
  }
  addDevice(device: NetworkDevice): void {
    this.devices$.next([...this.devices$.value, device]);
  }
  removeDevice(id: number): void {
    this.devices$.next(this.devices$.value.filter(d => d.id !== id));
  }
}
```

JsonRest store to HttpClient service:

```typescript
@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);
  // NOTE: This calls the EMS REST API, NOT the old EPNM API.
  // The EMS API endpoints serve the same data from PostgreSQL.
  private baseUrl = '/api/ems/v1/devices';
  getNetworkDevices(filters?: Record<string, string>): Observable<NetworkDevice[]> {
    let params = new HttpParams();
    if (filters) {
      Object.entries(filters).forEach(([key, value]) => {
        params = params.set(key, value);
      });
    }
    return this.http.get<NetworkDevice[]>(this.baseUrl, { params });
  }
  getDevice(id: number): Observable<NetworkDevice> {
    return this.http.get<NetworkDevice>(`${this.baseUrl}/${id}`);
  }
  updateDevice(device: NetworkDevice): Observable<NetworkDevice> {
    return this.http.put<NetworkDevice>(`${this.baseUrl}/${device.id}`, device);
  }
  addDevice(device: Omit<NetworkDevice, 'id'>): Observable<NetworkDevice> {
    return this.http.post<NetworkDevice>(this.baseUrl, device);
  }
  removeDevice(id: number): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`);
  }
}
```

Cache store (Memory + JsonRest combination):

```typescript
@Injectable({ providedIn: 'root' })
export class CachedInventoryService {
  private http = inject(HttpClient);
  private cache$ = new BehaviorSubject<NetworkDevice[] | null>(null);
  private baseUrl = '/api/ems/v1/devices';
  getNetworkDevices(): Observable<NetworkDevice[]> {
    if (this.cache$.value) {
      return of(this.cache$.value);
    }
    return this.http.get<NetworkDevice[]>(this.baseUrl).pipe(
      tap(devices => this.cache$.next(devices))
    );
  }
  updateDevice(device: NetworkDevice): Observable<NetworkDevice> {
    return this.http.put<NetworkDevice>(`${this.baseUrl}/${device.id}`, device).pipe(
      tap(() => this.cache$.next(null))
    );
  }
}
```

Observable store maps naturally to `BehaviorSubject` subscription, which auto-notifies subscribers on value changes.

---

## 4. Theme Toggle Architecture

Source: `08_research_conversion_patterns_2026-04-07.md` Section 7

### 4.1 The requirement

From Set 07 (Akhil): "The default, once I log into the Crosswork UI, the default will be showing the EPNM theme. Basically the left menu and the other area should be the EPNM current feel should be shown instead of Magnetic."

Two visual modes coexist in same Angular application:
1. **Classic (EPNM):** blue/white color scheme, legacy layout, left navigation panel, Dojo-era visual density
2. **Modern (EMS/Magnetic):** Harbor/Magnetic design system, current Crosswork UI look

### 4.2 CSS custom properties architecture

Theme toggle uses CSS custom properties on document root. Instant switching, no reload.

EPNM classic palette:

```scss
// styles/themes/_epnm-classic.scss
:root[data-theme="classic"] {
  --theme-primary: #003366;           // EPNM dark blue
  --theme-primary-light: #0066cc;     // EPNM medium blue
  --theme-primary-dark: #002244;      // EPNM navy
  --theme-accent: #4a90d9;            // EPNM accent blue
  --theme-background: #ffffff;
  --theme-surface: #f5f7fa;
  --theme-surface-alt: #e8ecf1;
  --theme-text-primary: #333333;
  --theme-text-secondary: #666666;
  --theme-border: #cccccc;
  --theme-header-bg: #003366;
  --theme-header-text: #ffffff;
  --theme-nav-bg: #f0f2f5;
  --theme-nav-hover: #e0e4ea;
  --theme-nav-active: #d0d6e0;
  --theme-table-header-bg: #003366;
  --theme-table-header-text: #ffffff;
  --theme-table-row-hover: #e8f0fe;
  --theme-status-online: #28a745;
  --theme-status-offline: #dc3545;
  --theme-status-warning: #ffc107;
  --theme-nav-width: 240px;
  --theme-header-height: 48px;
  --theme-font-family: 'Segoe UI', Arial, sans-serif;
  --theme-font-size-base: 13px;
  --theme-border-radius: 2px;
  --theme-spacing-unit: 4px;
}
```

Magnetic palette:

```scss
// styles/themes/_ems-magnetic.scss
:root[data-theme="magnetic"] {
  --theme-primary: #049fd9;
  --theme-primary-light: #3eb8e5;
  --theme-primary-dark: #037baa;
  --theme-accent: #6abf4b;
  --theme-background: #1a1a2e;
  --theme-surface: #222240;
  --theme-surface-alt: #2a2a48;
  --theme-text-primary: #ffffff;
  --theme-text-secondary: #b0b0c0;
  --theme-border: #3a3a5c;
  --theme-header-bg: #111128;
  --theme-header-text: #ffffff;
  --theme-nav-bg: #1a1a2e;
  --theme-nav-hover: #2a2a48;
  --theme-nav-active: #3a3a5c;
  --theme-table-header-bg: #222240;
  --theme-table-header-text: #ffffff;
  --theme-table-row-hover: #2a2a48;
  --theme-status-online: #6abf4b;
  --theme-status-offline: #e74c3c;
  --theme-status-warning: #f5a623;
  --theme-nav-width: 280px;
  --theme-header-height: 56px;
  --theme-font-family: 'CiscoSans', 'Helvetica Neue', sans-serif;
  --theme-font-size-base: 14px;
  --theme-border-radius: 8px;
  --theme-spacing-unit: 8px;
}
```

Component styles reference theme variables:

```scss
.epnm-data-grid {
  font-family: var(--theme-font-family);
  font-size: var(--theme-font-size-base);
  border: 1px solid var(--theme-border);
  border-radius: var(--theme-border-radius);
  th {
    background-color: var(--theme-table-header-bg);
    color: var(--theme-table-header-text);
    padding: calc(var(--theme-spacing-unit) * 2);
  }
  td {
    padding: calc(var(--theme-spacing-unit) * 2);
    border-bottom: 1px solid var(--theme-border);
    color: var(--theme-text-primary);
  }
  tr:hover { background-color: var(--theme-table-row-hover); }
}

.epnm-left-nav {
  width: var(--theme-nav-width);
  background-color: var(--theme-nav-bg);
  font-family: var(--theme-font-family);
  .nav-item {
    padding: calc(var(--theme-spacing-unit) * 2) calc(var(--theme-spacing-unit) * 3);
    color: var(--theme-text-primary);
    &:hover { background-color: var(--theme-nav-hover); }
    &.active {
      background-color: var(--theme-nav-active);
      border-left: 3px solid var(--theme-primary);
    }
  }
}
```

### 4.3 ThemeService pattern

```typescript
// theme.service.ts
import { Injectable, signal, effect } from '@angular/core';

export type ThemeMode = 'classic' | 'magnetic';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  readonly currentTheme = signal<ThemeMode>('classic');  // EPNM classic is default

  constructor() {
    const saved = localStorage.getItem('epnm-theme') as ThemeMode | null;
    if (saved) {
      this.currentTheme.set(saved);
    }
    effect(() => {
      const theme = this.currentTheme();
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('epnm-theme', theme);
    });
  }

  toggle(): void {
    this.currentTheme.update(current =>
      current === 'classic' ? 'magnetic' : 'classic'
    );
  }

  isClassic(): boolean {
    return this.currentTheme() === 'classic';
  }
}
```

### 4.4 Toggle component (lives in the shell app header)

```typescript
// theme-toggle.component.ts
@Component({
  selector: 'app-theme-toggle',
  standalone: true,
  imports: [MatSlideToggleModule],
  template: `
    <div class="theme-toggle-container">
      <span class="theme-label">Classic</span>
      <mat-slide-toggle
        [checked]="themeService.currentTheme() === 'magnetic'"
        (change)="themeService.toggle()"
        color="primary">
      </mat-slide-toggle>
      <span class="theme-label">Modern</span>
    </div>
  `,
  styles: [`
    .theme-toggle-container {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .theme-label {
      font-size: 12px;
      color: var(--theme-header-text);
    }
  `]
})
export class ThemeToggleComponent {
  themeService = inject(ThemeService);
}
```

### 4.5 Conditional component rendering

For screens with fundamentally different layouts:

```typescript
@Component({
  selector: 'app-inventory-view',
  standalone: true,
  imports: [NetworkDevicesClassicComponent, NetworkDevicesModernComponent],
  template: `
    @if (themeService.currentTheme() === 'classic') {
      <app-network-devices-classic />
    } @else {
      <app-network-devices-modern />
    }
  `
})
export class InventoryViewComponent {
  themeService = inject(ThemeService);
}
```

### 4.6 Theming decision matrix

| Scenario | Approach |
|---|---|
| Same layout, different colors/fonts | CSS custom properties only; single component |
| Same layout, minor structural differences | CSS custom properties + conditional `@if` blocks in template |
| Fundamentally different layouts | Two separate components; container switches based on theme |
| Navigation structure differs | Two navigation components; shell app switches between them |
| Third-party components (Magnetic library) | `panelClass` or `::ng-deep` with theme-scoped selectors to override Magnetic defaults in classic mode |

---

## 5. API Integration Approach

Source: `08_research_conversion_patterns_2026-04-07.md` Section 8

### 5.1 Architecture

Classic view does NOT call the old EPNM backend. It calls the same EMS REST APIs that the modern Magnetic UI calls. Difference is purely in presentation.

```
                    +-------------------+
                    |  EMS REST APIs    |
                    |  (Spring Boot/Go) |
                    |  (PostgreSQL)     |
                    +--------+----------+
                             |
                    +--------v----------+
                    |  Angular Services |
                    |  (HttpClient)     |
                    +---+----------+----+
                        |          |
              +---------+--+  +----+---------+
              | Classic    |  | Modern       |
              | Components |  | Components   |
              | (EPNM UX)  |  | (Magnetic UX)|
              +------------+  +--------------+
```

### 5.2 Shared service pattern

Both classic and modern views share the same Angular service layer. Service handles API; components handle presentation.

```typescript
// services/inventory.service.ts (shared)
export interface DeviceApiResponse {
  id: number;
  hostname: string;
  ipAddress: string;
  managementStatus: string;   // "MANAGED" | "UNMANAGED" | "MAINTENANCE"
  deviceFamily: string;       // "CISCO_ASR_9000" | "CISCO_NEXUS_9000" etc.
  softwareVersion: string;
  lastInventoryCollection: string;
  chassisSerialNumber: string;
  location: {
    site: string;
    building: string;
    floor: string;
  };
}

@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);
  private baseUrl = '/api/ems/v1/inventory/devices';

  getNetworkDevices(params?: {
    deviceFamily?: string;
    status?: string;
    site?: string;
    page?: number;
    pageSize?: number;
    sortBy?: string;
    sortOrder?: 'asc' | 'desc';
  }): Observable<DeviceApiResponse[]> {
    let httpParams = new HttpParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined) {
          httpParams = httpParams.set(key, String(value));
        }
      });
    }
    return this.http.get<DeviceApiResponse[]>(this.baseUrl, { params: httpParams });
  }

  getDeviceDetails(deviceId: number): Observable<DeviceApiResponse> {
    return this.http.get<DeviceApiResponse>(`${this.baseUrl}/${deviceId}`);
  }

  getDevice360(deviceId: number): Observable<Device360Response> {
    return this.http.get<Device360Response>(`${this.baseUrl}/${deviceId}/360`);
  }

  getChassisView(deviceId: number): Observable<ChassisViewResponse> {
    return this.http.get<ChassisViewResponse>(`${this.baseUrl}/${deviceId}/chassis`);
  }
}
```

### 5.3 Display adapter for classic view

Data transformation happens in classic view components or optional adapter services, NOT in the shared base service:

```typescript
// classic/adapters/epnm-display.adapter.ts
export class EpnmDisplayAdapter {
  // EMS "MANAGED"/"UNMANAGED"/"MAINTENANCE" to EPNM "Managed"/"Unmanaged"/"In Maintenance"
  static formatStatus(emsStatus: string): string {
    const statusMap: Record<string, string> = {
      'MANAGED': 'Managed',
      'UNMANAGED': 'Unmanaged',
      'MAINTENANCE': 'In Maintenance',
      'PARTIALLY_MANAGED': 'Partially Managed'
    };
    return statusMap[emsStatus] || emsStatus;
  }

  // EMS "CISCO_ASR_9000" to EPNM "Cisco ASR 9000 Series"
  static formatDeviceFamily(emsFamily: string): string {
    const familyMap: Record<string, string> = {
      'CISCO_ASR_9000': 'Cisco ASR 9000 Series',
      'CISCO_NEXUS_9000': 'Cisco Nexus 9000 Series',
      'CISCO_NCS_5500': 'Cisco NCS 5500 Series',
      'CISCO_NCS_540': 'Cisco NCS 540 Series'
    };
    return familyMap[emsFamily] || emsFamily.replace(/_/g, ' ');
  }

  // EMS ISO 8601 to EPNM "Mar 25, 2026 14:30:22 PDT"
  static formatTimestamp(isoTimestamp: string): string {
    const date = new Date(isoTimestamp);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      timeZoneName: 'short'
    });
  }
}
```

Usage:

```typescript
export class NetworkDevicesClassicComponent implements OnInit {
  private inventoryService = inject(InventoryService);
  displayDevices: ClassicDeviceRow[] = [];

  ngOnInit(): void {
    this.inventoryService.getNetworkDevices().subscribe(apiDevices => {
      this.displayDevices = apiDevices.map(device => ({
        id: device.id,
        hostname: device.hostname,
        ipAddress: device.ipAddress,
        status: EpnmDisplayAdapter.formatStatus(device.managementStatus),
        deviceType: EpnmDisplayAdapter.formatDeviceFamily(device.deviceFamily),
        softwareVersion: device.softwareVersion,
        lastCollected: EpnmDisplayAdapter.formatTimestamp(device.lastInventoryCollection),
        location: `${device.location.site} / ${device.location.building}`
      }));
    });
  }
}
```

### 5.4 API response gaps to watch for

| EPNM Feature | EMS API Expectation | Gap Risk |
|---|---|---|
| Device count in left filter panel | API must return faceted counts by device type, location | Check if EMS API supports aggregation queries |
| Chassis view images | Bundled as application assets in EMS (confirmed) | Low risk -- already available |
| Device 360 alarm count badge | API must return alarm count per device | Check if EMS device endpoint includes alarm summary |
| Export device (CSV) | API must support export format or client-side generation | Check if EMS has export endpoint |
| Bulk import (CSV) | API must accept multipart file upload | Check if EMS has import endpoint |
| OEM commands execution | API must support command dispatch to devices | Likely in the ~20% gap -- verify |
| Scheduling (maintain/managed state) | API must support scheduled state transitions | May need new backend endpoints |

---

## 6. Shell App Integration Considerations

Source: `08_research_conversion_patterns_2026-04-07.md` Section 9

### 6.1 Current EMS shell architecture

```
Infra UI (Shell App - outermost)
  |-- Header bar, top navigation, login
  |-- Common UI (shared component library)
  |     |-- Cards, tables, design system widgets
  |     |-- Harbor/Magnetic component implementations
  |
  |-- EMS UI (feature pages - loaded into shell content area)
        |-- Inventory views
        |-- Fault management views
        |-- Software image management
```

### 6.2 Where the toggle lives

Theme toggle button lives in the **Infra UI shell header** (persistent, always visible). Controls global theme state that all nested layers respond to.

```typescript
// app-header.component.ts (existing shell header -- add toggle)
import { ThemeToggleComponent } from './theme-toggle/theme-toggle.component';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [ThemeToggleComponent, /* existing imports */],
  template: `
    <header class="shell-header">
      <div class="header-left">
        <img src="assets/cisco-logo.svg" class="logo" />
        <span class="product-name">Crosswork Network Controller</span>
      </div>
      <div class="header-center">
        <!-- existing navigation -->
      </div>
      <div class="header-right">
        <!-- NEW: Theme toggle added here -->
        <app-theme-toggle />
        <!-- existing user menu, settings, etc. -->
      </div>
    </header>
  `
})
export class AppHeaderComponent { }
```

### 6.3 Classic view routing strategy

**Option A (recommended for POC): Dual routes with container component**

```typescript
const routes: Routes = [
  {
    path: 'inventory/network-devices',
    component: InventoryViewComponent,  // container switches based on theme
    children: []
  },
  {
    path: 'faults/alarms',
    component: FaultViewComponent,      // container switches based on theme
    children: []
  }
];
```

URL stays the same regardless of theme. Container component uses `ThemeService` signal to decide which inner component to render.

**Option B: Route guards with theme-aware loading**

```typescript
export const classicViewGuard: CanMatchFn = () => {
  return inject(ThemeService).currentTheme() === 'classic';
};
export const modernViewGuard: CanMatchFn = () => {
  return inject(ThemeService).currentTheme() === 'magnetic';
};

const routes: Routes = [
  {
    path: 'inventory/network-devices',
    canMatch: [classicViewGuard],
    loadComponent: () => import('./classic/network-devices-classic.component')
      .then(m => m.NetworkDevicesClassicComponent)
  },
  {
    path: 'inventory/network-devices',
    canMatch: [modernViewGuard],
    loadComponent: () => import('./modern/network-devices-modern.component')
      .then(m => m.NetworkDevicesModernComponent)
  }
];
```

Recommendation (from research): Option A is simpler for POC; avoids route re-evaluation on toggle. Option B fits better if the team already uses `canMatch` patterns.

### 6.4 Classic view folder structure

Proposed organization within EMS UI repository:

```
ems-ui/
  src/
    app/
      classic/                          # <-- NEW: All classic view code
        components/
          network-devices-classic/
            network-devices-classic.component.ts
            network-devices-classic.component.html
            network-devices-classic.component.scss
          device-360-classic/
            device-360-classic.component.ts
            device-360-classic.component.html
            device-360-classic.component.scss
          device-details-classic/
            device-details-classic.component.ts
            device-details-classic.component.html
            device-details-classic.component.scss
          chassis-view-classic/
            chassis-view-classic.component.ts
            chassis-view-classic.component.html
            chassis-view-classic.component.scss
          alarm-list-classic/
            alarm-list-classic.component.ts
            alarm-list-classic.component.html
            alarm-list-classic.component.scss
        adapters/
          epnm-display.adapter.ts       # Data transformation
        styles/
          _epnm-classic.scss            # EPNM theme variables
          _epnm-components.scss         # EPNM component overrides
          _epnm-layout.scss             # Left-nav + content layout
        shared/
          epnm-left-nav/                # Classic left navigation
          epnm-toolbar/                 # Classic toolbar
          epnm-filter-panel/            # Left-side filtering panel
      modern/                           # Existing Magnetic/Harbor components
        components/
          ...
      shared/                           # Shared between classic and modern
        services/
          inventory.service.ts          # API calls (shared)
          alarm.service.ts              # API calls (shared)
          theme.service.ts              # Theme toggle state
          event-bus.service.ts          # Cross-component events
        models/
          network-device.model.ts
          alarm.model.ts
          device-360.model.ts
        containers/
          inventory-view.component.ts   # Switches classic/modern
          fault-view.component.ts       # Switches classic/modern
```

### 6.5 Common UI reuse policy

1. Reuse Common UI structural components where they can be themed via CSS custom properties (card containers, layout grids)
2. Do NOT reuse Common UI components tightly coupled to Magnetic (Magnetic-specific button styles, Harbor typography)
3. Create classic-specific wrapper components using same data patterns but EPNM styling

Example: If Common UI has `<cx-data-table>` heavily styled with Magnetic tokens, classic view should use `<mat-table>` directly with EPNM styling rather than override the Common UI component.

### 6.6 Build integration

Classic view code must be part of EMS build pipeline (confirmed requirement from Set 07: "It has to be part of the new EMS build"). Classic components must be importable from EMS UI module:

```typescript
const routes: Routes = [
  {
    path: 'inventory',
    loadChildren: () => import('./classic/classic.routes')
      .then(m => m.CLASSIC_ROUTES)
  }
];
```

Classic view ships in the same build artifact as modern EMS UI. No separate deployment.

---

## 7. Named Conversion Risks and Pitfalls

Consolidated from all three research files.

### 7.1 From legacy stack research (Section 6)

1. **Undocumented behavior** in 15-plus-year monolith. Quirks in sorting, filtering, data transformation embedded in widget code, service layer, or Oracle stored procedures.
2. **Custom widget complexity.** EPNM custom Dijit widgets with accumulated conditional rendering, device-type special cases, browser workarounds.
3. **Pub/Sub dependency web.** `dojo/topic` creates invisible dependency graph. No compile-time errors, no import chain, no visible structural connection. Must be mapped manually.
4. **Data shape mismatches.** EPNM vs EMS REST APIs likely return different JSON structures (field names, nesting, pagination format, error handling). Angular must adapt or use adapter layer.
5. **Oracle-to-PostgreSQL data gaps.** 10 to 20 percent functionality gap. If a field is in EPNM UI but not in EMS backend, classic UI cannot display it.
6. **Device-type-specific logic.** IOS vs IOS-XR vs NX-OS parsing differences, chassis layout differences by model, interface naming conventions.

### 7.2 From modern stack research

- Harbor/Magnetic relationship still open question: are they one system or distinct; does Harbor expose theming APIs; is Common UI built on Harbor
- Go service integration unclear: which endpoints are Go vs Spring Boot; direct frontend calls vs Spring Boot intermediary; gRPC vs REST between services
- Postgres timezone behavior differs from Oracle SYSDATE: classic view must handle UTC storage conversion for display
- Postgres NULL handling: Postgres distinguishes empty string from NULL (Oracle treats empty as NULL); queries ported from EPNM may behave differently

### 7.3 From conversion patterns research (Section 8.4)

| EPNM Feature | Gap Risk |
|---|---|
| Device count in left filter panel | Check if EMS API supports aggregation |
| Device 360 alarm count badge | Check if EMS device endpoint includes alarm summary |
| Export device (CSV) | Check if EMS has export endpoint |
| Bulk import (CSV) | Check if EMS has import endpoint (multipart upload) |
| OEM commands execution | Likely in the ~20% gap; verify |
| Scheduling (maintain/managed state) | May need new backend endpoints |

### 7.4 From modern stack Priority summary and routing implications

- Toggle state persistence decision: localStorage vs user preference API vs URL-based (each has tradeoffs for cross-device persistence and discoverability)
- Bundle size: classic view adds to EMS UI bundle; lazy loading important so classic components only load when selected
- Automated AMD-to-ES6 tool (`amd-to-es6`) handles mechanical transformation only; does not handle Dojo-specific patterns (`declare()`, `this.inherited()`, Dijit lifecycle)

---

## 8. Per-Screen Migration Checklist

Source: `08_research_conversion_patterns_2026-04-07.md` Section 10 (preserved verbatim)

For each EPNM screen being converted, follow this checklist.

### Step 1: Analyze the EPNM Screen

- [ ] Identify all Dojo widgets used (DataGrid, Dialog, Tree, form widgets)
- [ ] Document the data flow (what API/store does it call?)
- [ ] Map the layout structure (BorderContainer, ContentPane, TabContainer)
- [ ] Note all user interactions (click handlers, context menus, keyboard shortcuts)
- [ ] Capture the visual design (colors, fonts, spacing, borders)

### Step 2: Identify the EMS API Endpoints

- [ ] Find the equivalent EMS REST API for each data source
- [ ] Compare the EPNM data fields with EMS API response fields
- [ ] Document any gaps (fields present in EPNM but absent from EMS API)
- [ ] Note any data format differences requiring adapter transformation

### Step 3: Create the Angular Component

- [ ] Map Dojo widgets to Angular Material components (Section 1)
- [ ] Convert AMD modules to ES6 imports (Section 2)
- [ ] Replace Dojo data binding with Angular binding patterns (Section 3)
- [ ] Replace Dojo event handling with Angular patterns (Section 4)
- [ ] Map lifecycle methods (Section 5)
- [ ] Create/reuse Angular services for state management (Section 6)

### Step 4: Apply EPNM Theming

- [ ] Use CSS custom properties for theme-responsive styling (Section 7)
- [ ] Apply EPNM-specific class names for structural differences
- [ ] Test that the component renders correctly in both classic and modern themes

### Step 5: Integrate with Shell App

- [ ] Add component to the appropriate routing configuration
- [ ] Wire up the theme-switching container component (Section 9.3)
- [ ] Verify component renders within the Infra UI shell
- [ ] Test toggle between classic and modern views

---

## End of extraction
