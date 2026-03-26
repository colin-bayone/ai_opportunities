# Web Security Best Practices

General web security patterns applicable across all web applications. Tech-stack-specific security is covered in separate docs.

## Input Validation

### User Input

- [ ] All user input validated on server side (never trust client validation alone)
- [ ] Whitelist validation preferred over blacklist
- [ ] Input length limits enforced
- [ ] Special characters validated or sanitized
- [ ] File uploads validated by content, not just extension
- [ ] JSON input validated against schema (`jsonschema` library)

### SQL Injection Prevention

- [ ] All database queries use parameterized queries (Django ORM or raw SQL with params)
- [ ] No string concatenation for SQL queries
- [ ] No user input directly in SQL statements
- [ ] ORM methods used correctly (avoid `raw()` when possible)
- [ ] `extra()` and `raw()` methods use parameter binding

### Command Injection Prevention

- [ ] No user input passed to shell commands
- [ ] If shell commands necessary, use subprocess with args list (not shell=True)
- [ ] User input sanitized before system calls
- [ ] Avoid `os.system()`, `eval()`, `exec()` with user input

## Output Encoding & XSS Prevention

### Template Auto-Escaping

- [ ] Django template auto-escaping enabled (default)
- [ ] `|safe` filter used only for trusted content
- [ ] HTML sanitization for user-generated HTML (django-markdownify)
- [ ] JavaScript context escaping when embedding data in `<script>`
- [ ] URL encoding for user data in URLs

### Content Security Policy

- [ ] CSP headers configured (if using custom CSP)
- [ ] Inline scripts avoided or use nonces
- [ ] External scripts from trusted CDNs only
- [ ] SRI (Subresource Integrity) for CDN assets

## Authentication Security

### Password Security

- [ ] Password hashing uses strong algorithm (Django default: PBKDF2)
- [ ] Passwords never logged or displayed
- [ ] Password reset tokens single-use and time-limited
- [ ] Password reset rate limited
- [ ] No password hints or security questions

### Multi-Factor Authentication

- [ ] MFA available for privileged accounts (Microsoft SSO provides MFA)
- [ ] MFA enforced for staff users
- [ ] Backup codes or recovery methods provided
- [ ] MFA bypass only with explicit admin approval and logging

### Session Security

- [ ] Session IDs cryptographically random
- [ ] Session regeneration after login
- [ ] Session timeout for inactive users
- [ ] Logout destroys session completely
- [ ] Concurrent session limits (if required)

## Authorization & Access Control

### Principle of Least Privilege

- [ ] Users granted minimum permissions needed
- [ ] Default deny: explicit permission required for access
- [ ] Permission checks at multiple layers (view, service, data)
- [ ] Admin privileges separated from regular user privileges

### Vertical Privilege Escalation Prevention

- [ ] User role checked before privileged operations
- [ ] No role/permission modifications via user input
- [ ] Admin functions separate from user functions
- [ ] Direct object reference attacks prevented

### Horizontal Privilege Escalation Prevention

- [ ] Object ownership verified before access
- [ ] Multi-tenancy boundaries enforced (client groups)
- [ ] URL parameter tampering prevented
- [ ] API endpoints filter by current user/tenant

## HTTPS & Transport Security

### TLS/SSL Configuration

- [ ] HTTPS enforced in production (`SECURE_SSL_REDIRECT=True`)
- [ ] HTTP Strict Transport Security (HSTS) enabled
- [ ] HSTS preload list inclusion considered
- [ ] TLS 1.2+ required (no SSL, TLS 1.0, TLS 1.1)
- [ ] Strong cipher suites configured

### Cookie Security

- [ ] Session cookies marked Secure in production
- [ ] Session cookies marked HttpOnly (prevent JS access)
- [ ] CSRF cookies marked Secure in production
- [ ] SameSite attribute set (Strict or Lax)
- [ ] Cookie expiration set appropriately

## CSRF Protection

### Django CSRF Middleware

- [ ] `CsrfViewMiddleware` enabled
- [ ] `{% csrf_token %}` in all forms
- [ ] AJAX requests include CSRF token (X-CSRFToken header)
- [ ] CSRF token validated on all state-changing requests
- [ ] CSRF exemption only for documented reasons (`@csrf_exempt`)

### HTMX CSRF

- [ ] HTMX requests include CSRF token
- [ ] CSRF token in meta tag for JavaScript access
- [ ] POST/PUT/DELETE requests always validated

## Clickjacking Protection

- [ ] X-Frame-Options header set (DENY or SAMEORIGIN)
- [ ] Frame embedding only allowed for trusted domains
- [ ] `XFrameOptionsMiddleware` enabled
- [ ] Iframes from untrusted sources rejected

## File Upload Security

### Upload Validation

- [ ] File size limits enforced
- [ ] File type validation by content (magic bytes, not extension)
- [ ] Filename sanitization (remove path traversal characters)
- [ ] Upload directory outside web root
- [ ] Uploaded files served with correct Content-Type
- [ ] Executable files rejected or stored securely

### File Storage

- [ ] Uploaded files stored with restricted permissions
- [ ] Uploaded files accessed via application (not direct URL)
- [ ] Temporary files cleaned up
- [ ] Storage quota enforced per user/tenant
- [ ] Cloud storage (Azure Blob) uses access controls

## API Security

### REST API

- [ ] Authentication required for all non-public endpoints
- [ ] Token-based auth with secure token generation
- [ ] API rate limiting enforced
- [ ] Input validation on all API endpoints
- [ ] Consistent error responses (no info disclosure)

### API Versioning

- [ ] URL path versioning used (e.g., `/api/v1/`)
- [ ] Deprecated versions documented
- [ ] Breaking changes in new versions only
- [ ] Old versions sunset with notice

### WebSocket Security

- [ ] WebSocket authentication enforced (Channels)
- [ ] Origin checking for WebSocket connections
- [ ] Message validation on all incoming messages
- [ ] Rate limiting on WebSocket messages
- [ ] Secure WebSocket (wss://) in production

## Error Handling & Information Disclosure

### Error Messages

- [ ] Generic error messages for users (no technical details)
- [ ] Detailed errors logged server-side only
- [ ] Stack traces never shown to users in production
- [ ] Debug mode disabled in production (`DEBUG=False`)
- [ ] Custom error pages (400, 403, 404, 500)

### Information Leakage Prevention

- [ ] No sensitive data in URLs (use POST for sensitive data)
- [ ] No sensitive data in error messages
- [ ] Server headers minimized (no version info)
- [ ] No directory listings
- [ ] No source code exposure

## Dependency Management

### Third-Party Libraries

- [ ] Dependencies pinned to specific versions
- [ ] Dependencies regularly updated for security patches
- [ ] Vulnerability scanning (Dependabot, Snyk, etc.)
- [ ] Unused dependencies removed
- [ ] License compliance checked

### Supply Chain Security

- [ ] Dependencies from trusted sources (PyPI, npm)
- [ ] Package integrity verified (checksums)
- [ ] Private packages hosted securely
- [ ] Dependency confusion attacks prevented

## Logging & Monitoring

### Security Logging

- [ ] Authentication events logged
- [ ] Authorization failures logged
- [ ] Input validation failures logged
- [ ] Rate limit violations logged
- [ ] Security-relevant errors logged

### Log Security

- [ ] Logs do not contain passwords or tokens
- [ ] Logs do not contain PII (or PII is masked)
- [ ] Logs stored securely with access controls
- [ ] Log integrity protected (append-only)
- [ ] Logs retained per compliance requirements

## Rate Limiting & DoS Prevention

### Application-Level Rate Limiting

- [ ] Login attempts rate limited (per IP and per user)
- [ ] API endpoints rate limited (per user)
- [ ] File upload rate limited
- [ ] Resource-intensive operations rate limited
- [ ] Rate limit headers returned (X-RateLimit-*)

### Infrastructure-Level Protection

- [ ] CDN/WAF configured (Azure Front Door)
- [ ] Connection limits enforced
- [ ] Request size limits enforced
- [ ] Timeout configurations set

## Secure Development Practices

### Code Review

- [ ] Security considerations in PR review checklist
- [ ] Secrets never committed to version control
- [ ] `.env` files in `.gitignore`
- [ ] Security-sensitive changes reviewed by security expert
- [ ] Automated security scanning in CI/CD

### Configuration Management

- [ ] Secrets in environment variables (django-environ)
- [ ] Different configs for dev/staging/prod
- [ ] Secure defaults (fail secure)
- [ ] Configuration changes audited
- [ ] Secret rotation procedures documented

## Common Vulnerability Checklist

Verify PR does not introduce:

- [ ] SQL injection vulnerabilities
- [ ] Cross-Site Scripting (XSS)
- [ ] Cross-Site Request Forgery (CSRF)
- [ ] Authentication bypass
- [ ] Authorization bypass
- [ ] Insecure direct object references
- [ ] Security misconfiguration
- [ ] Sensitive data exposure
- [ ] XML External Entities (XXE)
- [ ] Broken access control
- [ ] Using components with known vulnerabilities
- [ ] Insufficient logging & monitoring
- [ ] Server-Side Request Forgery (SSRF)
- [ ] Deserialization vulnerabilities
- [ ] Path traversal
- [ ] Open redirects
- [ ] Race conditions
- [ ] Business logic flaws
