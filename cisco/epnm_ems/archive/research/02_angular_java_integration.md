# Angular + Java Backend Integration: Technical Reference

**Purpose:** Internal reference for BayOne team understanding of EMS architecture patterns
**Date:** February 22, 2026

---

## Overview

Angular frontends communicate with Java backends (typically Spring Boot in microservices architectures) via REST APIs over HTTP. This is a well-established pattern for modern enterprise applications.

**Key characteristics:**
- Clear separation between frontend (Angular) and backend (Java)
- Stateless communication via REST
- JSON as the primary data format
- Backend handles business logic and persistence
- Frontend handles presentation and user interaction

---

## Architecture Pattern

### Traditional Monolith (EPNM Style)
```
Browser → Java Server (JSP/Servlets + Dojo) → Database
         [Single deployment unit]
```

### Microservices with Angular Frontend (EMS Style)
```
Browser → Angular SPA → API Gateway → Microservice A → Database A
                                   → Microservice B → Database B
                                   → Microservice C → Database C
```

In the EMS architecture:
- Angular runs entirely in the browser
- Each microservice exposes REST endpoints
- An API Gateway may aggregate/route requests
- Services communicate via REST or messaging

---

## Communication Pattern

### Angular Side: HTTP Client

Angular uses `HttpClient` from `@angular/common/http`:

```typescript
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class DeviceService {
  private apiUrl = '/api/devices';

  constructor(private http: HttpClient) {}

  getDevices(): Observable<Device[]> {
    return this.http.get<Device[]>(this.apiUrl);
  }

  getDevice(id: string): Observable<Device> {
    return this.http.get<Device>(`${this.apiUrl}/${id}`);
  }

  createDevice(device: Device): Observable<Device> {
    return this.http.post<Device>(this.apiUrl, device);
  }

  updateDevice(id: string, device: Device): Observable<Device> {
    return this.http.put<Device>(`${this.apiUrl}/${id}`, device);
  }

  deleteDevice(id: string): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
```

### Java Side: REST Controller

Spring Boot uses `@RestController`:

```java
@RestController
@RequestMapping("/api/devices")
@CrossOrigin(origins = "*")
public class DeviceController {

    @Autowired
    private DeviceService deviceService;

    @GetMapping
    public List<DeviceDTO> getAllDevices() {
        return deviceService.findAll();
    }

    @GetMapping("/{id}")
    public DeviceDTO getDevice(@PathVariable String id) {
        return deviceService.findById(id);
    }

    @PostMapping
    public DeviceDTO createDevice(@RequestBody DeviceDTO device) {
        return deviceService.create(device);
    }

    @PutMapping("/{id}")
    public DeviceDTO updateDevice(@PathVariable String id,
                                   @RequestBody DeviceDTO device) {
        return deviceService.update(id, device);
    }

    @DeleteMapping("/{id}")
    public void deleteDevice(@PathVariable String id) {
        deviceService.delete(id);
    }
}
```

---

## Key Concepts

### Data Transfer Objects (DTOs)

Backend domain models do not cross the wire directly. Instead, DTOs are used:

```java
// Domain model (stays on backend)
@Entity
public class Device {
    @Id private String id;
    private String name;
    private DeviceType type;
    @OneToMany private List<Port> ports;
    // ... complex relationships
}

// DTO (crosses the wire)
public class DeviceDTO {
    private String id;
    private String name;
    private String type;
    private int portCount;
    // ... flattened, serializable
}
```

**Relevance to conversion:** When converting EPNM screens, identify what data the UI needs and ensure corresponding DTOs exist in EMS microservices.

### CORS (Cross-Origin Resource Sharing)

When Angular runs on a different origin than the backend (common in development), CORS must be configured:

```java
@CrossOrigin(origins = "http://localhost:4200")
@RestController
public class MyController { ... }

// Or globally:
@Configuration
public class CorsConfig implements WebMvcConfigurer {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("*")
                .allowedMethods("GET", "POST", "PUT", "DELETE");
    }
}
```

### RxJS Observables

Angular uses RxJS for asynchronous operations:

```typescript
// In component
this.deviceService.getDevices().subscribe({
  next: (devices) => this.devices = devices,
  error: (err) => this.handleError(err),
  complete: () => console.log('Done')
});

// Or with async pipe in template
<div *ngFor="let device of devices$ | async">
  {{ device.name }}
</div>
```

**Relevance to conversion:** Dojo's callback-based async patterns (Deferreds, Promises) map to RxJS Observables in Angular.

---

## API Gateway Pattern (Microservices)

In microservices architectures, an API Gateway often sits between the frontend and services:

```
Angular → API Gateway → Service A
                     → Service B
                     → Service C
```

**Benefits:**
- Single entry point for frontend
- Authentication/authorization at gateway
- Request aggregation (one frontend call = multiple service calls)
- Rate limiting, caching

**Relevance to conversion:** A single EPNM screen might call one monolithic endpoint. The EMS equivalent might require the API Gateway to orchestrate calls to multiple microservices.

---

## Authentication Patterns

### Session-Based (Traditional)
- Server maintains session state
- Cookie-based authentication
- Less common in modern SPAs

### Token-Based (JWT)
- Stateless authentication
- Token stored in browser (localStorage or memory)
- Included in HTTP headers: `Authorization: Bearer <token>`

```typescript
// Angular HTTP Interceptor for adding token
@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler) {
    const token = this.authService.getToken();
    if (token) {
      req = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` }
      });
    }
    return next.handle(req);
  }
}
```

### Backend for Frontend (BFF) Pattern
- Recommended for OAuth2/OIDC
- Session managed on server-side gateway
- More secure for SPAs

---

## Error Handling

### Angular Side
```typescript
this.http.get<Device[]>(this.apiUrl).pipe(
  catchError((error: HttpErrorResponse) => {
    if (error.status === 404) {
      return of([]); // Return empty array
    }
    return throwError(() => new Error('Something went wrong'));
  })
);
```

### Java Side
```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse("NOT_FOUND", ex.getMessage()));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneral(Exception ex) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR)
            .body(new ErrorResponse("ERROR", "An error occurred"));
    }
}
```

---

## Pagination Pattern

### Request
```
GET /api/devices?page=0&size=20&sort=name,asc
```

### Spring Data Response
```java
@GetMapping
public Page<DeviceDTO> getDevices(Pageable pageable) {
    return deviceService.findAll(pageable);
}
```

### Angular Material Table Integration
```typescript
// Data source connects to paginator
this.dataSource.paginator = this.paginator;

loadDevices(page: number, size: number) {
  this.deviceService.getDevices(page, size)
    .subscribe(response => {
      this.dataSource.data = response.content;
      this.totalElements = response.totalElements;
    });
}
```

**Relevance to conversion:** Dojo DataGrids with server-side paging need to map to Angular Material Tables with pagination that calls Spring Data paginated endpoints.

---

## Key Conversion Considerations

### From EPNM to EMS

1. **Service boundaries** - One EPNM endpoint might become multiple EMS microservice calls

2. **Data shape** - EPNM backend might return data shaped for Dojo widgets; EMS DTOs may differ

3. **API contracts** - EMS has explicit REST contracts; EPNM may have implicit ones

4. **State management** - EPNM might maintain server-side state; EMS is likely stateless

5. **Error handling** - Different error response formats between systems

### Questions to Ask

- Does an equivalent EMS endpoint exist for this EPNM functionality?
- If not, which microservice should own this data?
- What DTOs need to be created or extended?
- How does authentication work in EMS?
- Is there an API Gateway aggregating calls?

---

## Sources

- [Baeldung: Spring Boot and Angular](https://www.baeldung.com/spring-boot-angular-web)
- [Angular University: Spring MVC and Angular Stack](https://blog.angular-university.io/developing-a-modern-java-8-web-app-with-spring-mvc-and-angularjs/)
- [Java Guides: Angular + Spring Boot REST Tutorial](https://www.javaguides.net/2021/01/angular-spring-boot-rest-api-example.html)
- [Microservices.io: API Gateway Pattern](https://microservices.io/patterns/apigateway.html)
- [Baeldung: OAuth2 BFF with Spring Cloud Gateway](https://www.baeldung.com/spring-cloud-gateway-bff-oauth2)
