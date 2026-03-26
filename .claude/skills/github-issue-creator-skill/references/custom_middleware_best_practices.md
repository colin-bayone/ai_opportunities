# Custom Middleware Best Practices

Patterns for custom middleware based on your middleware stack (15 middleware components).

## Middleware Order

### Critical Order Requirements
- [ ] SecurityMiddleware first (Django core security)
- [ ] WhiteNoiseMiddleware after Security (static file serving)
- [ ] SessionMiddleware before Auth (session needed for auth)
- [ ] AuthenticationMiddleware before custom auth middleware
- [ ] CSRF after Session (needs session)
- [ ] Custom middleware placed strategically based on dependencies
- [ ] XFrameOptionsMiddleware near end (response processing)

### Your Middleware Stack Order
1. SecurityMiddleware
2. WhiteNoiseMiddleware
3. SessionMiddleware
4. CommonMiddleware
5. CsrfViewMiddleware
6. AuthenticationMiddleware
7. MessageMiddleware
8. StaffSessionTimeoutMiddleware (custom)
9. AuditContextMiddleware (custom)
10. XFrameOptionsMiddleware
11. AccountMiddleware (allauth)
12. PulsecheckMiddleware (custom)
13. MetricsMiddleware (custom)
14. ClientGroupMiddleware (custom)
15. AuditAccessDeniedMiddleware (custom)

## Custom Middleware Patterns

### StaffSessionTimeoutMiddleware
**Purpose**: Auto-logout staff after 30 mins inactivity

**Check in PR**:
- [ ] Only applies to staff users (`is_staff=True`)
- [ ] Timeout configurable via `STAFF_SESSION_TIMEOUT_MINUTES`
- [ ] Updates `last_activity` timestamp in session on each request
- [ ] Graceful logout with message (no abrupt redirect)
- [ ] Does NOT affect external users
- [ ] Uses `process_request()` method
- [ ] Clears session on timeout

### AuditContextMiddleware
**Purpose**: Capture request context for audit logging

**Check in PR**:
- [ ] Uses thread-local storage to store context
- [ ] Captures: user, IP (X-Forwarded-For aware), user agent, path, timestamp
- [ ] Context available to audit service throughout request
- [ ] Context cleared after request completes (process_response)
- [ ] Handles anonymous users gracefully
- [ ] Real client IP extracted (handles proxies)

### PulsecheckMiddleware
**Purpose**: Request tracking and logging

**Check in PR**:
- [ ] Generates unique request ID
- [ ] Logs request start and completion
- [ ] Times request duration
- [ ] Auto-severity by status code (5xx=ERROR, 4xx=WARNING)
- [ ] Adds request ID to logs for tracing
- [ ] Performance metrics collected
- [ ] Thread-local context for request tracking

### MetricsMiddleware
**Purpose**: Performance metrics collection

**Check in PR**:
- [ ] Tracks request times (last 1000 requests)
- [ ] Counts errors by status code
- [ ] Endpoint statistics collected
- [ ] Minimal performance impact
- [ ] Thread-safe data structures
- [ ] Metrics accessible via dedicated endpoint
- [ ] No PII in metrics

### ClientGroupMiddleware
**Purpose**: Multi-tenancy client group handling

**Check in PR**:
- [ ] Validates client group from session
- [ ] Sets `request.client_group` for views
- [ ] Handles missing/invalid client group gracefully
- [ ] Does not block anonymous users
- [ ] Logs client group context switches
- [ ] Client group required for authenticated users
- [ ] Session validation

### AuditAccessDeniedMiddleware
**Purpose**: Log 403s and permission denials

**Check in PR**:
- [ ] Checks response status in `process_response()`
- [ ] Logs all 403 responses with context
- [ ] Captures user, path, and reason
- [ ] Creates audit log entry
- [ ] Does not modify response
- [ ] Handles exceptions gracefully

## Middleware Development Patterns

### MiddlewareMixin Pattern
- [ ] Extend `django.utils.deprecation.MiddlewareMixin`
- [ ] Use `process_request()` for pre-view processing
- [ ] Use `process_response()` for post-view processing
- [ ] Use `process_exception()` for exception handling
- [ ] Return `None` to continue, return response to short-circuit

### Thread-Local Storage
- [ ] Use for request-scoped data (audit context, request ID)
- [ ] Initialize in `process_request()`
- [ ] Clear in `process_response()` or `process_exception()`
- [ ] Handle missing data gracefully
- [ ] Thread-safe operations

### Performance Considerations
- [ ] Minimal processing in middleware (runs on every request)
- [ ] Avoid database queries in middleware when possible
- [ ] Use caching for expensive lookups
- [ ] Profile middleware impact
- [ ] Consider async support if using ASGI

## Common Patterns to Check

### Session Access
- [ ] Session available after `SessionMiddleware`
- [ ] Check session exists before accessing
- [ ] Handle expired/invalid sessions
- [ ] Update session with `request.session.save()` if modified

### User Context
- [ ] User available after `AuthenticationMiddleware`
- [ ] Check `request.user.is_authenticated`
- [ ] Handle anonymous users appropriately
- [ ] Don't assume user is staff

### Response Modification
- [ ] Only modify response if necessary
- [ ] Preserve original response when possible
- [ ] Set appropriate headers
- [ ] Don't break streaming responses

### Exception Handling
- [ ] Implement `process_exception()` for error handling
- [ ] Log exceptions with context
- [ ] Don't suppress exceptions unless intentional
- [ ] Return appropriate error response

## Testing Custom Middleware

### Unit Tests
- [ ] Test middleware in isolation
- [ ] Mock request/response objects
- [ ] Test all code paths (authenticated, anonymous, errors)
- [ ] Test middleware with different settings
- [ ] Verify thread-local cleanup

### Integration Tests
- [ ] Test middleware in request/response cycle
- [ ] Test interaction with other middleware
- [ ] Test order-dependent behavior
- [ ] Verify session/user context available

## Security Considerations

### Input Validation
- [ ] Validate session data before use
- [ ] Sanitize user input from headers
- [ ] Handle missing/malicious data gracefully
- [ ] Don't trust client-provided data

### Information Disclosure
- [ ] Don't expose sensitive data in middleware logs
- [ ] PII masked in logging middleware
- [ ] Error messages don't leak system info
- [ ] Stack traces not shown to users

### Authentication/Authorization
- [ ] Don't bypass auth checks
- [ ] Validate permissions appropriately
- [ ] Handle unauthorized access correctly
- [ ] Audit security-relevant actions

## Common Issues to Check

### Middleware Not Running
- [ ] Verify middleware in `MIDDLEWARE` setting
- [ ] Check order in middleware list
- [ ] Verify middleware class path correct
- [ ] Check for exceptions in middleware init

### Session Issues
- [ ] Session accessed before `SessionMiddleware`
- [ ] Session not saved after modification
- [ ] Session data type incompatible
- [ ] Session timeout conflicts

### Request Context Issues
- [ ] Thread-local not cleared (memory leak)
- [ ] Context accessed before initialization
- [ ] Context not available in async
- [ ] Race conditions in multi-threaded environments

### Performance Issues
- [ ] Database queries in middleware (N+1 problem)
- [ ] Expensive operations on every request
- [ ] Unnecessary processing for static files
- [ ] Memory leaks from uncleaned state

## Async Middleware Considerations

### ASGI Support
- [ ] Middleware works with both WSGI and ASGI
- [ ] `async def` methods for async support
- [ ] `sync_to_async` for blocking operations
- [ ] Thread-local alternatives for async (contextvars)

### Channels Compatibility
- [ ] Middleware doesn't break WebSocket connections
- [ ] Request handling differs for WS vs HTTP
- [ ] Channel-specific middleware if needed
- [ ] Context available in consumers

## Monitoring Custom Middleware

### Performance Metrics
- [ ] Track middleware execution time
- [ ] Monitor memory usage
- [ ] Count exceptions raised
- [ ] Alert on degraded performance

### Logging
- [ ] Log middleware initialization
- [ ] Log configuration changes
- [ ] Debug logs for development
- [ ] Error logs for production issues

## Cross-Reference

Related docs:
- `authentication_authorization_best_practices.md` - Auth middleware patterns
- `audit_logging_best_practices.md` - AuditContext usage
- `performance_monitoring_best_practices.md` - Metrics collection
- `soc2_considerations.md` - Audit requirements
- `django_best_practices.md` - General Django patterns
