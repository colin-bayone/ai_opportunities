# SOC2 Compliance Considerations

SOC2-specific checks for PR reviews. These apply across all code changes regardless of tech stack.

## Audit Logging

### Immutable Audit Logs

- [ ] All audit log writes use `AuditedModel` base class or `AuditService`
- [ ] No code attempts to modify audit logs after creation
- [ ] No code attempts to delete audit logs
- [ ] Audit logs stored in `audit_logs_soc2` table (separate from application data)

### What Must Be Audited

- [ ] Authentication events (login, logout, failed attempts)
- [ ] Authorization failures (403 responses, permission denials)
- [ ] Model changes (create, update, delete) for sensitive data
- [ ] Management command execution (use `@audit_command` decorator)
- [ ] API access to sensitive endpoints
- [ ] File uploads/downloads of sensitive documents
- [ ] Configuration changes

### Audit Context Capture

- [ ] `AuditContextMiddleware` captures request context (user, IP, user agent, path)
- [ ] Thread-local storage preserves context across async operations
- [ ] X-Forwarded-For header properly parsed for real client IP
- [ ] All audit entries include timestamp with timezone

## Authentication & Authorization

### Authentication Security

- [ ] Staff users enforced to use Microsoft SSO (no password auth)
- [ ] External users can use email/password with email verification required
- [ ] Emergency admin password auth logs CRITICAL level alerts
- [ ] Rate limiting applied: 5 failed attempts in 15 minutes = 30 minute lockout
- [ ] All authentication attempts logged (success and failure)
- [ ] Failed login attempts include IP address and reason

### Session Management

- [ ] Staff session timeout enforced (default 30 minutes)
- [ ] Session timeout configurable via `STAFF_SESSION_TIMEOUT_MINUTES`
- [ ] Graceful logout with user-friendly message
- [ ] Session data validated for client group membership
- [ ] Secure session cookies in production (`SESSION_COOKIE_SECURE=True`)

### Authorization

- [ ] All permission denials logged via `AuditAccessDeniedMiddleware`
- [ ] Role-based access control enforced (`@role_required` decorator)
- [ ] Multi-tenancy isolation via `@filter_by_client_group`
- [ ] Service account authorization for Airflow endpoints (`IsAirflowServiceAccount`)
- [ ] Admin access restricted to staff users with SSO

## Data Privacy & Protection

### PII Handling

- [ ] All logs automatically scrubbed for PII (Presidio-based masking)
- [ ] PII masking enabled in production (`PII_MASKING_ENABLED=True`)
- [ ] Email addresses, phone numbers, IPs masked in logs
- [ ] Infrastructure secrets masked (Azure URLs, connection strings, API keys)
- [ ] No PII in error messages shown to users
- [ ] PII in database encrypted at rest (check model field encryption)

### File Upload Security

- [ ] Magika AI-based file validation (content-based, not extension-based)
- [ ] File size limits enforced (2MB job parser, 5MB resume parser, 10MB default)
- [ ] Allowed file types validated against whitelist (`FILE_ALLOWED_TYPES`)
- [ ] Empty files rejected
- [ ] File uploads stored in secure location with access controls

### Data Retention & Deletion

- [ ] User-initiated deletions are soft deletes (`STORAGE_DEFAULT_HARD_DELETE=False`)
- [ ] Auto cleanup uses hard deletes (`STORAGE_CLEANUP_HARD_DELETE=True`)
- [ ] Soft delete timestamps recorded
- [ ] Data retention policies documented in code
- [ ] GDPR compliance: user data export functionality exists
- [ ] GDPR compliance: user data deletion functionality exists

## Access Control

### Multi-Tenancy (Client Groups)

- [ ] `ClientGroupMiddleware` validates client group membership
- [ ] All queries filtered by client group (use `@filter_by_client_group`)
- [ ] No cross-tenant data leakage (check querysets)
- [ ] Client group context available in templates
- [ ] API endpoints enforce client group isolation

### Role-Based Access Control

- [ ] Roles checked via `@role_required` decorator
- [ ] Template permissions pre-computed (`navbar_permissions`)
- [ ] View-level permission checks enforced
- [ ] No permission checks bypassed in code
- [ ] Least privilege principle applied

## Security Headers & HTTPS

### Production Security Headers

- [ ] All security headers only enabled when `IS_PRODUCTION=True`
- [ ] `IS_PRODUCTION` requires both `DEBUG=False` AND `ENVIRONMENT=production`
- [ ] HTTPS redirect enabled (`SECURE_SSL_REDIRECT=True`)
- [ ] HSTS enabled with 1-year max-age
- [ ] Content security headers enabled (XSS filter, content type nosniff)
- [ ] X-Frame-Options set to DENY (clickjacking protection)
- [ ] Secure cookies in production (`SECURE=True`, `HTTPONLY=True`, `SAMESITE=Strict`)

### Subresource Integrity (SRI)

- [ ] SRI enabled in production (`ENABLE_SRI=IS_PRODUCTION`)
- [ ] CDN assets include integrity hashes
- [ ] SRI hashes cached in dedicated Redis DB
- [ ] CORS configured for CDN assets (`crossorigin="anonymous"`)
- [ ] SRI cannot be disabled in production

## Rate Limiting

### Authentication Rate Limiting

- [ ] Login attempts: 5 failed in 15 minutes = 30 minute lockout
- [ ] Rate limiting tracked by IP address
- [ ] Rate limit cache backend configured (Redis in production)
- [ ] Rate limits applied at both backend and adapter levels

### API Rate Limiting

- [ ] DRF throttling configured (`DEFAULT_THROTTLE_RATES`)
- [ ] Authenticated users: 1000 requests/hour
- [ ] Service-specific rate limits (extraction service: 20 uploads/min)
- [ ] Bulk operations have separate limits (20 bulk requests/min)
- [ ] Rate limit exceeded errors logged

### Brute Force Protection

- [ ] All authentication endpoints rate limited
- [ ] Account lockout after threshold
- [ ] Lockout duration enforced
- [ ] Failed attempts logged with context

## Monitoring & Alerting

### Performance Monitoring

- [ ] `MetricsMiddleware` collects request metrics
- [ ] Request timing tracked (last 1000 requests)
- [ ] Error counts by status code tracked
- [ ] System metrics collected (CPU, memory, threads)
- [ ] Monitoring endpoints secured (DEBUG or auth required)

### Logging & Diagnostics

- [ ] `PulsecheckMiddleware` generates unique request IDs
- [ ] Request/response timing logged
- [ ] Auto-severity by status code (5xx=ERROR, 4xx=WARNING)
- [ ] Sensitive data automatically masked in logs
- [ ] No credentials or API keys in logs
- [ ] File paths masked in production logs

### Error Tracking

- [ ] All 5xx errors logged with full context
- [ ] All 4xx errors logged with user context
- [ ] Permission denials audited
- [ ] Unusual activity patterns logged

## Third-Party Integrations

### Azure Services

- [ ] Azure credentials stored in environment variables (never in code)
- [ ] Azure API calls use secure protocols (HTTPS)
- [ ] Azure service authentication uses managed identities where possible
- [ ] Azure Blob Storage URLs masked in logs
- [ ] Azure OpenAI API keys secured

### External APIs

- [ ] API keys stored in environment variables
- [ ] API calls over HTTPS only
- [ ] API rate limits respected
- [ ] API errors logged without exposing keys
- [ ] Third-party libraries kept up-to-date

## Incident Response

### Security Event Logging

- [ ] Critical security events log at CRITICAL level
- [ ] Emergency admin password usage logs CRITICAL alert
- [ ] Rate limit violations logged
- [ ] Permission denials logged with context
- [ ] Authentication failures logged with IP and user agent

### Audit Trail Completeness

- [ ] Sufficient detail for post-incident investigation
- [ ] Timestamps include timezone information
- [ ] User actions traceable across audit logs
- [ ] No gaps in audit log coverage
- [ ] Audit logs queryable by date range, user, action type

## Code Review Checklist Summary

For SOC2 compliance, verify:

1. All sensitive operations are audited
2. Audit logs are immutable and complete
3. Authentication uses SSO with rate limiting
4. PII is masked in all logs
5. Files validated with Magika (content-based)
6. Multi-tenancy isolation enforced
7. Security headers enabled in production
8. Rate limiting prevents abuse
9. No credentials in code or logs
10. Monitoring captures security events
