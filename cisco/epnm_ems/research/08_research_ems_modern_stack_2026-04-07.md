# 08 - Research: EMS Modern Stack (Angular, Spring Boot, Go, Postgres)

**Source:** Web research
**Source Date:** 2026-04-07
**Document Set:** 08 (Technical Research)
**Pass:** EMS modern technology stack reference

---

## Purpose

This document provides a practical technical reference for the EMS (Element Management System) technology stack, oriented toward building the classic view toggle UI. It covers the six core technologies confirmed in Set 07: Angular 21, Harbor/Magnetic design system, Spring Boot, Go services, PostgreSQL, and the microservices architecture that ties them together.

The audience is BayOne engineers ramping onto the codebase. Each section focuses on what matters for this engagement: building a EPNM-styled "classic view" UI layer within the existing EMS Angular application, connecting it to the existing Spring Boot / Go backend, reading from the existing Postgres database, and providing a toggle between classic and current (Magnetic) views.

---

## 1. Angular 21

### 1.1 Why This Matters for the Engagement

The entire EMS frontend is Angular 21. The classic UI is not a separate application -- it is a new set of Angular components that live within (or alongside) the existing EMS UI repository, share the same Angular runtime, and consume the same backend APIs. Understanding Angular 21's current architecture patterns is essential because the existing codebase uses them, and any new classic view code must follow the same patterns to be maintainable by Cisco's team.

### 1.2 Signals-First Architecture (The Biggest Shift from Older Angular)

Angular 21 completed the framework's transition to a signals-first, zoneless core. This is the single most important architectural change from earlier Angular versions.

**What signals are:** A signal is a reactive primitive that holds a value and notifies Angular when that value changes. Unlike RxJS Observables, signals are synchronous, have no subscription management, and are read by calling them as functions.

```typescript
// Creating and reading signals
import { signal, computed, effect } from '@angular/core';

// Writable signal
const count = signal(0);

// Read: call the signal as a function
console.log(count());  // 0

// Write: use .set() or .update()
count.set(5);
count.update(v => v + 1);

// Computed signal (derived, read-only)
const doubled = computed(() => count() * 2);

// Effect (side effect when dependencies change)
effect(() => {
  console.log(`Count is now: ${count()}`);
});
```

**Why this matters for classic view:** The existing EMS codebase likely uses signals throughout. New classic view components should follow the same pattern. There is no `.subscribe()`, no `ngOnInit` teardown logic, no `async` pipe needed for signal-based state.

### 1.3 Signal Components: input(), output(), model()

Angular 21 uses signal-based component communication as the standard. This replaces the older `@Input()` and `@Output()` decorators.

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
  // Signal input (read-only, set by parent)
  deviceId = input.required<string>();
  deviceName = input.required<string>();
  status = input<string>('unknown');

  // Signal output (event emitter)
  cardClicked = output<string>();
}
```

**Two-way binding with model():**

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
  // model() creates both input and output for two-way binding
  isClassicView = model(false);

  toggleView() {
    this.isClassicView.set(!this.isClassicView());
  }
}

// Parent usage: banana-in-a-box syntax
// <app-view-toggle [(isClassicView)]="showClassic" />
```

### 1.4 Standalone Components (No NgModules)

Angular 21 defaults to standalone components. There are no `NgModule` declarations. Each component declares its own imports directly.

```typescript
@Component({
  selector: 'app-alarm-list',
  standalone: true,
  imports: [CommonModule, FormsModule, AlarmRowComponent, FilterBarComponent],
  template: `...`
})
export class AlarmListComponent { }
```

**Relevance to classic view:** Classic view components will be standalone. They import what they need directly. No module registration ceremony.

### 1.5 Dependency Injection with inject()

The modern pattern uses the `inject()` function rather than constructor injection.

```typescript
@Component({ ... })
export class NetworkDevicesComponent {
  // Modern DI pattern
  private inventoryService = inject(InventoryService);
  private router = inject(Router);
  private activatedRoute = inject(ActivatedRoute);

  devices = signal<Device[]>([]);

  constructor() {
    // Load data
    this.inventoryService.getDevices().subscribe(data => {
      this.devices.set(data);
    });
  }
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

**For classic view:** Services are shared between classic and current views. Both views call the same `InventoryService`, `AlarmService`, etc. The classic view only changes how the data is rendered, not where it comes from.

### 1.6 RxJS Observables and HttpClient

While signals handle component state, HttpClient still returns Observables. The pattern is to convert HTTP responses to signals at the service or component level.

```typescript
@Injectable({ providedIn: 'root' })
export class AlarmService {
  private http = inject(HttpClient);

  getAlarms(params: AlarmFilterParams): Observable<PagedResponse<Alarm>> {
    return this.http.get<PagedResponse<Alarm>>('/api/v1/faults/alarms', {
      params: this.buildHttpParams(params)
    });
  }
}
```

**Interceptors** handle cross-cutting concerns. Angular 21 prefers functional interceptors:

```typescript
// auth.interceptor.ts
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const authToken = inject(AuthService).getToken();
  const authReq = req.clone({
    headers: req.headers.set('Authorization', `Bearer ${authToken}`)
  });
  return next(authReq);
};

// Error handling interceptor
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

### 1.7 Routing and Lazy Loading

Routes use `loadComponent` for lazy-loaded standalone components:

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

**For classic view toggle:** The toggle likely needs a route guard or a top-level conditional that loads either the classic or current component for the same path. Options include:

1. **Route-level switching:** Different routes for `/classic/inventory` vs `/inventory`
2. **Component-level switching:** Same route, parent component conditionally renders classic or current child
3. **Theme-level switching:** Same components, different CSS/template via directive (only works if layout differences are minor)

### 1.8 Change Detection: Zoneless + OnPush

Angular 21 runs **zoneless by default** -- Zone.js is no longer included. Change detection is triggered by:

- Signal value changes (the primary mechanism)
- Template events (click, input, etc.)
- Async pipe emissions
- Router navigation

OnPush change detection strategy remains important: it limits how far up the component tree Angular checks. Combined with signals, this gives fine-grained DOM updates.

```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush,
  // ...
})
export class DeviceListComponent {
  devices = signal<Device[]>([]);
  // Only this component's template re-renders when devices changes
}
```

**For classic view:** All new components should use `OnPush` change detection and signals for state. This matches the existing EMS codebase patterns.

### 1.9 Angular Material

Angular Material provides pre-built UI components (tables, forms, buttons, dialogs, etc.) that follow Material Design 3. The EMS codebase uses Harbor/Magnetic instead, but Angular Material's patterns are useful reference since Harbor/Magnetic components likely follow similar APIs.

Key theming capability: Angular Material supports design tokens and custom themes via SCSS. The classic view will need its own theme (EPNM's blue-and-white palette) that can coexist with the Magnetic theme.

```scss
// Example: defining a custom theme
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

### 1.10 Key Differences from Dojo (What EPNM Engineers Should Know)

| Concept | Dojo (EPNM) | Angular 21 (EMS) |
|---------|-------------|-------------------|
| Component model | Widgets (`dijit/_WidgetBase`) | Standalone components with decorators |
| Data binding | Manual / one-way | Signals (reactive, automatic) |
| Templating | JS functions or HTML templates | Inline HTML templates with Angular directives |
| Dependency injection | Manual or AMD modules | Built-in DI with `inject()` function |
| Routing | Manual or `dojo/router` | Built-in `@angular/router` with lazy loading |
| Module system | AMD (`define`/`require`) | ES6 modules (`import`/`export`) |
| Change detection | Manual DOM updates | Automatic via signals + zoneless scheduler |
| State management | Store pattern or manual | Signals + injectable services |
| HTTP requests | `dojo/request` | `HttpClient` returning Observables |
| CSS scoping | Global CSS | Component-scoped CSS (ViewEncapsulation) |
| Type safety | JavaScript (no types) | TypeScript (full type checking) |
| Build system | Dojo build tool | Angular CLI (esbuild-based in v21) |
| Lifecycle | `postCreate`, `startup`, `destroy` | `ngOnInit`, `ngOnDestroy` (or `afterNextRender`, `DestroyRef`) |

---

## 2. Harbor / Magnetic Design System

### 2.1 What We Know

From Set 07 (Akhil): "If you look at the Crosswork UI, we have a Magnetic design system. So it's a design system called Harbor and Magnetic design system you're using."

**Magnetic** is Cisco's company-wide design system. It was originally built by the Meraki team, publicly introduced in July 2022, and is being rolled out across all Cisco networking and security products. It provides a unified visual language so IT professionals see familiar patterns as they move between Cisco tools.

**Harbor** appears to be the Crosswork-specific implementation layer or component library that applies Magnetic design principles to the Crosswork product family (including EMS). The relationship is likely: Magnetic = design spec/tokens, Harbor = Angular component library for Crosswork.

### 2.2 Public Information about Magnetic

- **GitHub presence:** `github.com/cisco-magnetic` -- the organization exists but most repositories may be private or internal.
- **Design philosophy:** Reduce UI complexity in network management tools. Cisco cited research that 50% of security breaches happen because users struggle with complex product UIs. Magnetic aims to simplify.
- **Visual language:** Clean, modern design. Consistent across devices and services. The EMS current view uses Magnetic styling.
- **Component scope:** "Adoption-ready UI Shell components" have been completed. These include header, navigation, layout primitives, and common patterns.
- **Not just cosmetic:** Magnetic includes interaction patterns, accessibility standards, and UX conventions, not just visual styling.

### 2.3 Implications for Classic View Toggle

The classic view must provide a different visual experience from Magnetic. Based on Set 07:

- **Current EMS view:** Magnetic design system (Harbor components), modern layout
- **Classic EPNM view:** "Blue and white" theme, left-side navigation menu, EPNM-familiar layout
- **Default on login:** Classic (EPNM) view
- **Toggle:** User can switch to EMS (Magnetic) view

This means the classic view likely needs:

1. **Its own CSS theme** -- Blue/white palette, EPNM-like typography and spacing
2. **Compatible but visually different components** -- Same data, different presentation. Could reuse Harbor component APIs with different styling, or could use separate simpler components.
3. **Theme isolation** -- Classic and Magnetic CSS must not conflict. Angular's ViewEncapsulation helps, but global styles (header, nav shell) need careful management.
4. **Left navigation menu** -- EPNM uses a left sidebar navigation. EMS/Magnetic uses a top menu. The classic view needs to swap the navigation paradigm.

### 2.4 Open Questions (From Set 07, Still Open)

- Are Harbor and Magnetic two layers of one system, or distinct? (Likely: Magnetic = design tokens/spec, Harbor = Crosswork component library)
- Does Harbor expose theming APIs that support multiple themes? If so, classic view might be implementable as a Harbor theme rather than separate components.
- Is Common UI (the shared repo) built on Harbor? If so, can classic view components reuse Common UI with different styling?

---

## 3. Spring Boot

### 3.1 Role in EMS

Spring Boot is the primary backend framework for EMS. It provides the REST API layer that the Angular frontend calls to get inventory data, alarm data, device details, and other information. From Set 07: "Mostly Spring Boot, yes" for the backend.

### 3.2 Current Spring Boot (3.x on Jakarta EE)

Spring Boot 3.x is built on Jakarta EE 9+. All persistence, validation, and servlet imports use the `jakarta` package prefix (not `javax`). This is relevant if reading legacy code or documentation that still references `javax`.

```java
// Spring Boot 3.x uses jakarta, not javax
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.validation.constraints.NotNull;
```

### 3.3 REST Controller Pattern

The standard pattern for EMS API endpoints:

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
        DeviceDetailDTO device = deviceService.getDeviceById(id);
        return ResponseEntity.ok(device);
    }

    @GetMapping("/devices/{id}/360")
    public ResponseEntity<Device360DTO> getDevice360(@PathVariable Long id) {
        Device360DTO device360 = deviceService.getDevice360(id);
        return ResponseEntity.ok(device360);
    }
}
```

**For classic view:** The classic view should not require new REST endpoints in most cases. It consumes the same APIs as the current EMS view. The data is identical; only the frontend rendering changes. If the classic view needs data shaped differently (e.g., flattened tables instead of card-based layouts), that reshaping should happen in the Angular service layer, not by creating new backend endpoints.

### 3.4 Service Layer Pattern

The service layer sits between controllers and repositories. It contains business logic, validation, and DTO mapping.

```java
@Service
public class DeviceService {

    private final DeviceRepository deviceRepository;
    private final DeviceMapper deviceMapper;

    public DeviceService(DeviceRepository deviceRepository, DeviceMapper deviceMapper) {
        this.deviceRepository = deviceRepository;
        this.deviceMapper = deviceMapper;
    }

    public Page<DeviceDTO> getDevices(String hostname, String deviceType, Pageable pageable) {
        Page<DeviceEntity> entities;
        if (hostname != null || deviceType != null) {
            entities = deviceRepository.findByFilters(hostname, deviceType, pageable);
        } else {
            entities = deviceRepository.findAll(pageable);
        }
        return entities.map(deviceMapper::toDTO);
    }

    public DeviceDetailDTO getDeviceById(Long id) {
        DeviceEntity entity = deviceRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("Device", id));
        return deviceMapper.toDetailDTO(entity);
    }
}
```

### 3.5 DTO Pattern

DTOs (Data Transfer Objects) separate the database entity model from the API response model. This is standard in Spring Boot applications.

```java
// Entity (database model) -- internal, never exposed directly
@Entity
@Table(name = "network_devices")
public class DeviceEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "device_seq")
    @SequenceGenerator(name = "device_seq", sequenceName = "network_devices_id_seq")
    private Long id;

    @Column(name = "hostname")
    private String hostname;

    @Column(name = "ip_address")
    private String ipAddress;

    @Column(name = "device_type")
    private String deviceType;

    @Column(name = "software_version")
    private String softwareVersion;

    @Column(name = "last_polled_at")
    private Instant lastPolledAt;

    // getters, setters
}

// DTO (API response model) -- exposed to frontend
public record DeviceDTO(
    Long id,
    String hostname,
    String ipAddress,
    String deviceType,
    String softwareVersion,
    String lastPolledAt  // formatted string, not Instant
) {}
```

**For classic view:** DTOs define the data contract between frontend and backend. The classic view Angular components will receive these same DTO shapes. Understanding the DTO structure tells you what fields are available for display.

### 3.6 JPA/Hibernate with PostgreSQL

Spring Data JPA abstracts the database layer. Repository interfaces extend `JpaRepository`:

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

### 3.7 Pagination

Spring Data JPA handles pagination automatically through `Pageable`:

```java
// Controller receives pagination params automatically
@GetMapping("/alarms")
public ResponseEntity<Page<AlarmDTO>> getAlarms(Pageable pageable) {
    // Spring auto-parses: ?page=0&size=20&sort=severity,desc
    return ResponseEntity.ok(alarmService.getAlarms(pageable));
}
```

The `Page` response includes metadata:

```json
{
  "content": [...],
  "totalElements": 1523,
  "totalPages": 77,
  "number": 0,
  "size": 20,
  "sort": { "sorted": true, "direction": "DESC", "property": "severity" }
}
```

**For classic view:** The EPNM table views (network devices, alarms) use pagination. The classic view components need to pass `page`, `size`, and `sort` query parameters to the existing API endpoints, which already support `Pageable`.

### 3.8 Error Handling

Global exception handling uses `@RestControllerAdvice`:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        ErrorResponse error = new ErrorResponse(
            HttpStatus.NOT_FOUND.value(),
            ex.getMessage(),
            Instant.now()
        );
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGenericError(Exception ex) {
        log.error("Unexpected error", ex);
        ErrorResponse error = new ErrorResponse(
            HttpStatus.INTERNAL_SERVER_ERROR.value(),
            "Internal server error",
            Instant.now()
        );
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}

public record ErrorResponse(int status, String message, Instant timestamp) {}
```

**For classic view:** Error handling in the Angular layer should expect these structured error responses. The classic view should display errors in an EPNM-appropriate style (likely simpler error banners vs. Magnetic's styled error components).

### 3.9 Performance Note

Spring Boot 3.4 with virtual threads delivers 3.3x more throughput than the same application with platform threads, with P99 latency dropping from 85ms to 18ms under heavy load. The EMS backend may or may not use virtual threads, but it is a capability of the current framework.

---

## 4. Go Services

### 4.1 Role in EMS

From Set 07 (Pradeep): "There are areas, at least on the device management side, and there are Go services running at the back end."

Go is used for specific backend services in EMS, primarily in the device management area. This is a polyglot microservices pattern: Spring Boot handles the majority of the backend, while Go handles performance-sensitive device management operations.

### 4.2 Why Go for Device Management

Go is well-suited for network device management because of:

- **Concurrency model:** Go's goroutines handle thousands of concurrent device connections efficiently without the thread-per-connection overhead of traditional Java.
- **gNMI (gRPC Network Management Interface):** Go has first-class support for gNMI, the OpenConfig-standard protocol for device telemetry and configuration. The reference implementation at `github.com/openconfig/gnmi` is in Go.
- **Protocol Buffers:** Go has excellent protobuf support, which is central to gRPC/gNMI communication with network devices.
- **Binary deployment:** Go compiles to a single static binary, which simplifies containerization.
- **Low memory footprint:** Important when running many service instances for large device fleets.

### 4.3 Go in the Cisco Ecosystem

Cisco has significant Go usage in the network management space:

- **pipeline-gnmi:** A Go-based Model-Driven Telemetry (MDT) collector with gNMI support, supporting IOS XR, IOS XE, and NX-OS.
- **Netflix's gnmi-gateway:** Built in Go specifically because of Go's first-class protobuf support and existing reference code for gNMI.
- **Telegraf plugins:** Go-based telemetry plugins for Cisco devices (IOS XR 6.5.1+, NX-OS 9.3+, IOS XE 16.12+).

### 4.4 Go and Spring Boot Coexistence

In a polyglot microservices architecture, Go and Spring Boot services communicate through:

1. **REST APIs (HTTP/JSON):** Simplest approach. Go services expose REST endpoints that Spring Boot services call, or vice versa. This is the most likely pattern in EMS.
2. **gRPC (Protocol Buffers):** Higher-performance option. Both Go and Spring Boot have mature gRPC support. gRPC's protobuf schema generates client/server code for both languages, ensuring type-safe communication.
3. **Message queues:** Services communicate asynchronously through Kafka, RabbitMQ, or similar. Go and Spring Boot each consume/produce messages independently.
4. **Shared database:** Both can read from the same PostgreSQL database, though this creates tighter coupling and is generally less preferred.

### 4.5 Typical Go REST API Structure

```go
// Simplified example of a Go device management service
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

### 4.6 Implications for Classic View

The classic view frontend will not interact with Go services directly in most cases. The typical flow is:

```
Angular frontend
    |
    v (REST API call)
Spring Boot service
    |
    v (internal API or gRPC call)
Go device management service
    |
    v (gNMI, SNMP, CLI)
Network devices
```

The Angular classic view components call the Spring Boot API layer. Spring Boot orchestrates calls to Go services internally. The frontend is shielded from the polyglot backend. However, if some API endpoints are served directly by Go services (without a Spring Boot intermediary), the classic view Angular services need to know the correct base URLs.

### 4.7 Open Questions

- Which specific EMS API endpoints are served by Go vs. Spring Boot?
- Do Go services have their own REST endpoints that the frontend calls directly, or does everything go through Spring Boot?
- Is gRPC used for inter-service communication between Spring Boot and Go, or is it REST?

---

## 5. PostgreSQL (Replacing Oracle)

### 5.1 Context

From Set 07 (team): "There's Postgres in the new product. We've gotten rid of Oracle dependency."

EMS uses PostgreSQL. EPNM used Oracle. The ~80% backend reimplementation includes the database migration. The classic view connects to the same Postgres database as the current EMS view -- there is no Oracle connection in the classic view.

### 5.2 Key Differences: Oracle vs. PostgreSQL

Understanding these differences matters when reading code that was ported from the EPNM Oracle codebase, or when Cisco engineers describe behavior using Oracle terminology.

#### Data Types

| Oracle | PostgreSQL | Notes |
|--------|-----------|-------|
| `VARCHAR2(n)` | `VARCHAR(n)` or `TEXT` | Postgres `TEXT` has no length limit and no performance penalty |
| `NUMBER` | `NUMERIC`, `INTEGER`, `BIGINT` | Use the most specific type available |
| `DATE` | `TIMESTAMP` or `TIMESTAMPTZ` | Oracle `DATE` includes time; Postgres `DATE` does not |
| `CLOB` | `TEXT` | Postgres `TEXT` handles large strings natively |
| `BLOB` | `BYTEA` | Binary data |
| `RAW` | `BYTEA` | Binary data |
| `SEQUENCE.NEXTVAL` | `nextval('sequence_name')` | Function syntax, not object property |

#### Date/Time Handling (Critical Difference)

Oracle's `SYSDATE` returns the database server's OS timezone, and this value does not change even if the session timezone is modified.

PostgreSQL's `now()` / `current_timestamp` returns values in the session's timezone. PostgreSQL stores `TIMESTAMPTZ` values internally as UTC and converts to the session timezone on display.

```sql
-- Oracle
SELECT SYSDATE FROM DUAL;  -- Always server OS time

-- PostgreSQL
SELECT now();              -- Session timezone
SELECT now() AT TIME ZONE 'UTC';  -- Explicit UTC
SELECT clock_timestamp();  -- Wall-clock time (changes within a statement)
```

**For the classic view:** If EPNM displayed times in a specific format tied to Oracle's `SYSDATE` behavior, the classic view must account for Postgres timestamps being UTC-based. The Angular frontend should handle timezone display formatting consistently.

#### Sequences and Primary Keys

Oracle uses sequences with `.NEXTVAL`. PostgreSQL uses `nextval()` function syntax. In Spring Boot / JPA, the recommended strategy for PostgreSQL is `GenerationType.SEQUENCE`:

```java
@Id
@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "device_seq")
@SequenceGenerator(name = "device_seq", sequenceName = "network_devices_id_seq",
                   allocationSize = 50)
private Long id;
```

`SEQUENCE` is preferred over `IDENTITY` for PostgreSQL because it supports batch insert optimization (pre-fetching IDs, reducing database round-trips).

#### Built-in Function Mapping

| Oracle | PostgreSQL | Notes |
|--------|-----------|-------|
| `NVL(a, b)` | `COALESCE(a, b)` | `COALESCE` accepts multiple arguments |
| `DECODE(x, a, b, c)` | `CASE WHEN x = a THEN b ELSE c END` | Standard SQL |
| `ROWNUM` | `LIMIT` / `OFFSET` | Or use window functions with `ROW_NUMBER()` |
| `SYSDATE` | `now()` or `current_timestamp` | See timezone caveat above |
| `TO_DATE('...', 'fmt')` | `TO_DATE('...', 'fmt')` | Similar but format strings differ slightly |
| `||` (string concat) | `||` (string concat) | Same syntax |
| `SUBSTR(s, start, len)` | `SUBSTRING(s FROM start FOR len)` | Different syntax |

#### Packages and Stored Procedures

Oracle uses PL/SQL packages to group related procedures and functions. PostgreSQL has no package concept. The common migration patterns:

- **Oracle packages -> PostgreSQL schemas** -- Use schemas to group related functions
- **Oracle procedures -> PostgreSQL procedures** -- `CREATE PROCEDURE` (supports transaction control)
- **Oracle functions -> PostgreSQL functions** -- `CREATE FUNCTION` (runs in a single transaction)
- **PL/SQL -> PL/pgSQL** -- Very similar syntax, but exception handling, loop bounds, and variable scope differ

Key PL/pgSQL differences:
- No global variables (use `SET` / custom GUC parameters for session-scoped state)
- Functions run within a single transaction (no `COMMIT` / `ROLLBACK` inside functions; use procedures instead)
- `RAISE` replaces `DBMS_OUTPUT.PUT_LINE` and custom exception handling
- Integer `FOR` loops with `REVERSE` swap the bounds compared to PL/SQL

### 5.3 Spring Boot + PostgreSQL Integration

In `application.yml` (or `application.properties`):

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
      ddl-auto: validate  # never use 'update' or 'create' in production
    properties:
      hibernate:
        default_schema: ems
        jdbc:
          batch_size: 50
        order_inserts: true
        order_updates: true
```

### 5.4 Implications for Classic View

The classic view does not interact with the database directly. It calls REST APIs that call Spring Boot services that call JPA repositories that query Postgres. However, understanding the database layer matters for:

1. **Data shape:** Knowing what's in the database tells you what data is available for display
2. **Performance:** Complex EPNM views that relied on Oracle-specific features (materialized views, analytic functions) may behave differently on Postgres
3. **Time zones:** Classic view time display must account for Postgres UTC storage
4. **NULL handling:** If EPNM code relied on Oracle's treatment of empty strings as NULL, the same queries on Postgres behave differently (Postgres distinguishes empty string from NULL)

---

## 6. Microservices Architecture

### 6.1 EMS Architecture Overview

From Set 07, the EMS architecture follows a microservices pattern within the Crosswork Network Controller platform:

```
+---------------------------------------------------------------+
|  Client Browser                                                |
|  Angular SPA (Infra UI shell -> Common UI -> EMS UI)          |
+---------------------------------------------------------------+
              |
              | REST / HTTP
              v
+---------------------------------------------------------------+
|  API Gateway / Ingress                                        |
|  (Routing, auth, rate limiting)                               |
+---------------------------------------------------------------+
              |
    +---------+---------+
    |                   |
    v                   v
+-------------+   +-------------+
| Spring Boot |   | Go Services |
| Services    |   | (Device     |
| (Inventory, |   |  Management)|
|  Faults,    |   |             |
|  SIM, etc.) |   |             |
+------+------+   +------+------+
       |                  |
       v                  v
+---------------------------------------------------------------+
|  PostgreSQL                                                   |
|  (Shared database or per-service databases)                   |
+---------------------------------------------------------------+
              |
              | (SNMP, CLI, NETCONF, gNMI)
              v
+---------------------------------------------------------------+
|  Network Devices (routers, switches, optical transport)       |
+---------------------------------------------------------------+
```

### 6.2 The Shell App Pattern (Frontend Microservices)

The three-layer frontend architecture described in Set 07 is a form of micro-frontend pattern:

| Layer | Repository | Purpose |
|-------|-----------|---------|
| **Infra UI** | Infra UI Repo | Shell application: header, top nav, infrastructure components. Outermost layer. |
| **Common UI** | Common UI Repo | Shared component library: cards, tables, design system widgets (Harbor/Magnetic). Consumed by all feature modules. |
| **EMS UI** | EMS UI Repo | Feature pages: inventory views, fault management, software image management, device details. |

This pattern means:

- **Infra UI** owns the application bootstrap, authentication, and layout frame
- **Common UI** is likely consumed as an npm package or linked library
- **EMS UI** registers routes and feature components within the shell
- The **classic view** code would live in EMS UI (or a new repo), registering its own routes or variant components within the same shell

### 6.3 Service Boundaries

In a microservices architecture like EMS, each service owns a specific domain:

- **Inventory Service** -- Network devices, device details, device 360, chassis view
- **Fault/Alarm Service** -- Alarms, events, syslogs, correlated alarms
- **Device Management Service** -- Device communication, polling, configuration (likely Go)
- **Topology Service** -- Network topology maps and relationships
- **Software Image Management (SIM)** -- Software images, upgrade management
- **User/Auth Service** -- User management, authentication, authorization

Each service has its own API contract. The Angular frontend calls specific service APIs for specific data.

### 6.4 API Contracts and Inter-Service Communication

**Frontend to backend:** REST/HTTP with JSON payloads. Standard Spring Boot `@RestController` endpoints.

**Service to service:** Multiple options observed in Cisco-scale deployments:

1. **Synchronous REST** -- Service A calls Service B's REST API directly. Simple but creates coupling.
2. **gRPC** -- Higher-performance synchronous communication. Likely used between Spring Boot and Go services. Protocol Buffers provide schema enforcement across languages.
3. **Message-based (async)** -- Events published to a message bus (Kafka, RabbitMQ). Used for operations that don't need immediate response (e.g., device status change triggers alarm evaluation).

### 6.5 Service Discovery

In a Kubernetes environment (which Crosswork uses), service discovery is handled by Kubernetes itself:

- **Kubernetes Services** expose pods behind stable DNS names (e.g., `inventory-service.ems.svc.cluster.local`)
- **CoreDNS** resolves service names to pod IPs
- **No external service registry needed** -- Kubernetes manages registration automatically
- **Ingress controllers** (often Envoy-based) route external traffic to the correct service

Spring Boot services in Kubernetes configure their URLs via environment variables or ConfigMaps:

```yaml
# application.yml
device-management:
  service:
    url: ${DEVICE_MGMT_URL:http://device-management-service:8080}
```

### 6.6 Containerization

EMS services are containerized (confirmed by the Crosswork architecture documentation):

- Each microservice runs in its own container
- Kubernetes orchestrates deployment, scaling, and health monitoring
- The Crosswork Infrastructure platform provides the cluster architecture
- Health checks: services report Healthy, Degraded, or Down status
- System health = aggregate of all service health states

### 6.7 Implications for Classic View

The classic view is purely a frontend concern in the microservices architecture. It does not add new microservices to the backend. Key implications:

1. **No new backend services needed:** Classic view components call existing API endpoints. The service boundaries and API contracts are already defined.
2. **Same authentication:** Classic view uses the same auth flow as current EMS view (handled by Infra UI shell app).
3. **Same API gateway:** Classic view requests go through the same ingress/gateway.
4. **Toggle state management:** The toggle (classic vs. current view) needs a storage mechanism:
   - **Option A: Frontend-only (localStorage)** -- Simplest, but doesn't persist across devices/browsers
   - **Option B: User preference API** -- Store in backend as user setting. Requires a small API endpoint (likely exists already for other user preferences).
   - **Option C: URL-based** -- Different URL paths for classic vs. current. Most discoverable and debuggable.
5. **Build pipeline:** Classic view components must be built and deployed as part of the EMS UI bundle. They add to the bundle size, so lazy loading is important -- classic view components should only load when the user selects classic mode.

---

## 7. Cross-Cutting Patterns for Classic View Implementation

### 7.1 The Toggle Architecture (Synthesis)

Combining all the technology research, here is how the classic view toggle likely needs to work across the stack:

```
User clicks toggle button
    |
    v
Toggle component updates state
(signal: isClassicView.set(true))
    |
    +---> Persist preference (localStorage or user preference API)
    |
    v
Router or conditional rendering switches view
    |
    +--> Classic components load (lazy-loaded Angular standalone components)
    |    - Use EPNM blue/white theme CSS
    |    - Render EPNM-style layouts (left nav, tables, device views)
    |    - Call SAME backend API services as current view
    |
    +--> OR current components load (existing EMS/Magnetic components)
         - Use Harbor/Magnetic theme CSS
         - Render current layouts (top nav, cards, modern device views)
         - Call SAME backend API services
```

### 7.2 Shared Services, Different Components

The service layer in Angular should be view-agnostic:

```typescript
// Shared service -- used by both classic and current views
@Injectable({ providedIn: 'root' })
export class InventoryService {
  private http = inject(HttpClient);

  getDevices(params: DeviceFilterParams): Observable<PagedResponse<DeviceDTO>> {
    return this.http.get<PagedResponse<DeviceDTO>>('/api/v1/inventory/devices', {
      params: this.toHttpParams(params)
    });
  }
}

// Classic view component -- EPNM-style table layout
@Component({
  selector: 'app-classic-device-list',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="epnm-table-container">
      <table class="epnm-data-table">
        <thead>
          <tr>
            <th (click)="sort('hostname')">Host Name</th>
            <th (click)="sort('ipAddress')">IP Address</th>
            <th (click)="sort('deviceType')">Device Type</th>
            <th (click)="sort('reachability')">Reachability</th>
          </tr>
        </thead>
        <tbody>
          @for (device of devices(); track device.id) {
            <tr (click)="openDevice(device.id)">
              <td>{{ device.hostname }}</td>
              <td>{{ device.ipAddress }}</td>
              <td>{{ device.deviceType }}</td>
              <td>{{ device.reachability }}</td>
            </tr>
          }
        </tbody>
      </table>
      <app-classic-paginator
        [currentPage]="currentPage()"
        [totalPages]="totalPages()"
        (pageChange)="onPageChange($event)" />
    </div>
  `
})
export class ClassicDeviceListComponent {
  private inventoryService = inject(InventoryService);

  devices = signal<DeviceDTO[]>([]);
  currentPage = signal(0);
  totalPages = signal(0);

  // ... loads data from same InventoryService
}
```

### 7.3 Theme Coexistence

The classic view needs its own CSS theme that doesn't conflict with Magnetic:

```scss
// classic-theme.scss
// EPNM color palette
:root .classic-view {
  --epnm-primary: #003366;       // EPNM navy blue
  --epnm-secondary: #0066cc;     // EPNM accent blue
  --epnm-bg: #f5f7fa;            // Light gray background
  --epnm-surface: #ffffff;       // White cards/panels
  --epnm-text: #333333;          // Dark text
  --epnm-border: #d0d5dd;        // Light gray borders
  --epnm-header-bg: #003366;     // Navy header
  --epnm-header-text: #ffffff;   // White header text
  --epnm-nav-bg: #e8ecf1;        // Light nav sidebar
  --epnm-nav-active: #0066cc;    // Active nav item
}

.classic-view {
  // Override Magnetic navigation with EPNM left sidebar
  .app-nav {
    position: fixed;
    left: 0;
    top: var(--header-height);
    width: 240px;
    height: calc(100vh - var(--header-height));
    background: var(--epnm-nav-bg);
  }

  .app-content {
    margin-left: 240px;
  }

  // EPNM-style data tables
  .epnm-data-table {
    width: 100%;
    border-collapse: collapse;

    th {
      background: var(--epnm-primary);
      color: var(--epnm-header-text);
      padding: 8px 12px;
      text-align: left;
      cursor: pointer;
    }

    td {
      padding: 8px 12px;
      border-bottom: 1px solid var(--epnm-border);
    }

    tr:hover {
      background: #e8f0fe;
    }
  }
}
```

### 7.4 Data Flow Summary

For any screen in the classic view, the data flow is:

```
1. Angular classic component initializes
2. Component calls shared Angular service (e.g., InventoryService)
3. Service makes HTTP GET to Spring Boot REST controller
4. Controller calls service layer
5. Service calls JPA repository
6. Repository queries PostgreSQL
7. Data flows back: Postgres -> JPA entity -> DTO -> JSON response
8. Angular service receives Observable<DTO>
9. Classic component converts to signal and renders in EPNM-style template
```

No step in this flow changes between classic and current views except step 9 (the rendering).

---

## 8. Summary: What Matters Most for the Classic View POC

| Priority | Technology | What to Focus On |
|----------|-----------|-----------------|
| **Critical** | Angular 21 | Signals, standalone components, `inject()`, lazy loading, `OnPush` change detection. These are the patterns the codebase uses. |
| **Critical** | Harbor/Magnetic | Understanding the existing component library so classic view can coexist without conflict. Theme isolation strategy. |
| **Important** | Spring Boot | REST controller patterns and DTO shapes -- this is the API contract the classic view consumes. No new backend code expected. |
| **Important** | PostgreSQL | Data types, timestamp handling, and NULL behavior -- affects how data appears in classic view. |
| **Contextual** | Go services | Know they exist for device management. Classic view likely calls Spring Boot, which calls Go internally. |
| **Contextual** | Microservices architecture | Know the shell app pattern (Infra UI -> Common UI -> EMS UI). Classic view code lives in or alongside EMS UI. |

The core work is Angular: building standalone components with signal-based state management, consuming existing services, applying EPNM-style CSS theming, and integrating with the shell app's routing and navigation. The backend is already built. The database is already populated. The classic view is a frontend exercise that reuses everything below the Angular component layer.

---

## Sources

### Angular 21
- [Angular v21 Release](https://angular.dev/events/v21)
- [What's New in Angular 21](https://www.angulararchitects.io/blog/whats-new-in-angular-21-signal-forms-zone-less-vitest-angular-aria-cli-with-mcp-server/)
- [Angular Signals: Complete Guide](https://blog.angular-university.io/angular-signals/)
- [Angular Signal Components: input, output](https://blog.angular-university.io/angular-signal-components/)
- [Angular Signals in Practice (2026)](https://dev.to/cristiansifuentes/angular-signals-in-practice-a-scientific-production-minded-guide-2026-56jb)
- [State Management with Angular Signals](https://www.telerik.com/blogs/practical-guide-state-management-using-angular-services-signals)
- [Angular Dependency Injection Overview](https://angular.dev/guide/di)
- [Angular Zoneless Change Detection](https://angular.dev/guide/zoneless)
- [Change Detection: Zones and Signals](https://blog.lunatech.com/posts/2025-11-05-change-detection-strategies-in-angular-zones-and-signals)
- [Lazy Loading Standalone Components](https://angular.dev/reference/migrations/route-lazy-loading)
- [Angular HTTP Interceptors](https://angular.dev/guide/http/interceptors)
- [Angular Material Theming](https://material.angular.dev/guide/theming)

### Cisco Magnetic Design System
- [Magnetic Design System GitHub](https://github.com/cisco-magnetic)
- [Cisco Unifying GUIs with Magnetic (The Register)](https://www.theregister.com/2022/12/07/cisco_magnetic_consistent_security_ui/)
- [Design as a Differentiator: One Year at Cisco](https://security.design/blog/design-as-a-differentiator-one-year-at-cisco)
- [Cisco Crosswork Network Controller Data Sheet](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/crosswork-network-automation/datasheet-c78-743456.html)
- [Crosswork Network Controller UI Overview](https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/crosswork-network-controller/5-0/Solution-Workflow-Guide/bk-crosswork-network-controller-5-0-solution-workflow-guide/m-ui-overview.html)

### Spring Boot
- [Spring Boot + Spring Data JPA + PostgreSQL](https://mkyong.com/spring-boot/spring-boot-spring-data-jpa-postgresql/)
- [Spring Boot REST API Guide (2026)](https://tech-insider.org/spring-boot-tutorial-rest-api-java-2026/)
- [DTOs with Spring Boot](https://bell-sw.com/blog/ultimate-guide-to-using-dtos-with-spring-boot/)
- [Service Layer Pattern in Java](https://foojay.io/today/service-layer-pattern-in-java-with-spring-boot/)
- [Spring Boot Global Exception Handling](https://josealopez.dev/en/blog/spring-boot-global-exception-handling)
- [Pagination and Sorting with Spring Data JPA (Baeldung)](https://www.baeldung.com/spring-data-jpa-pagination-sorting)
- [Spring Cloud Gateway](https://www.baeldung.com/spring-cloud-gateway)

### Go Services
- [Network Automation with Go](https://nleiva.medium.com/network-automation-with-go-96341507a369)
- [Cisco pipeline-gnmi (Go)](https://github.com/cisco-ie/pipeline-gnmi)
- [OpenConfig gNMI Reference (Go)](https://github.com/openconfig/gnmi)
- [Netflix gnmi-gateway in Go](https://netflixtechblog.com/simple-streaming-telemetry-27447416e68f)
- [Cisco Data Center Telemetry with gNMI](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-744191.html)
- [Go Microservices Guide (Cortex)](https://www.cortex.io/post/golang-microservices)

### PostgreSQL / Oracle Migration
- [Oracle to PostgreSQL: PL/SQL vs PL/pgSQL](https://stormatics.tech/blogs/transitioning-from-oracle-to-postgresql-pl-sql-vs-pl-pgsql)
- [PostgreSQL Docs: Porting from Oracle PL/SQL](https://www.postgresql.org/docs/current/plpgsql-porting.html)
- [Complete Oracle to PostgreSQL Migration Guide (EDB)](https://www.enterprisedb.com/blog/the-complete-oracle-to-postgresql-migration-guide-tutorial-move-convert-database-oracle-alternative)
- [Oracle to Postgres Conversion (PostgreSQL Wiki)](https://wiki.postgresql.org/wiki/Oracle_to_Postgres_Conversion)
- [SYSDATE Oracle to PostgreSQL (AWS)](https://aws.amazon.com/blogs/database/converting-the-sysdate-function-from-oracle-to-postgresql/)
- [PostgreSQL Sequence with Hibernate (Vlad Mihalcea)](https://vladmihalcea.com/postgresql-serial-column-hibernate-identity/)

### Microservices Architecture
- [Crosswork Network Controller APIs (Cisco DevNet)](https://developer.cisco.com/docs/crosswork/network-controller/)
- [Kubernetes for Microservices: Best Practices](https://dev.to/rubixkube/kubernetes-for-microservices-best-practices-and-patterns-2440)
- [API Gateway and Service Discovery](https://api7.ai/blog/api-gateway-and-service-discovery)
- [Tracing Polyglot Microservices](https://oneuptime.com/blog/post/2026-02-06-trace-polyglot-microservices-architecture/view)

### Dojo to Angular Comparison
- [AngularJS vs Dojo (StackShare)](https://stackshare.io/stackups/angularjs-vs-dojo)
- [Mixing Dojo Widgets and Angular Components (SitePen)](https://www.sitepen.com/blog/dojo-mixing-dojo-widgets-and-angular-2-components)
