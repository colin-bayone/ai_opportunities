# Audit Logging Best Practices

Immutable audit logging patterns for SOC2 compliance using AuditService and signal handlers.

## Core Audit Principles

### Immutability Requirements
- [ ] Audit logs CANNOT be modified after creation (enforced at model level)
- [ ] Audit logs CANNOT be deleted (SOC2 requirement)
- [ ] `AuditedModel` base class prevents updates to audit fields
- [ ] Database constraints enforce immutability
- [ ] Separate table: `audit_logs_soc2`

### What Must Be Audited
- [ ] Authentication events (login, logout, failed attempts)
- [ ] Authorization failures (403s, permission denials)
- [ ] Model changes for sensitive data (create, update, delete)
- [ ] Management command execution
- [ ] API access to sensitive endpoints
- [ ] File uploads/downloads of sensitive documents
- [ ] Configuration changes
- [ ] Client group switches

## AuditService Usage

### Direct Audit Logging
**Check in PR**:
- [ ] Use `AuditService.log()` for manual audit entries
- [ ] Include action type, user, and details
- [ ] Details dictionary serializable to JSON
- [ ] No PII in audit details (use IDs, not values)
- [ ] Timestamp automatic (UTC)
- [ ] Context captured from `AuditContextMiddleware`

### Audit Context
**Check in PR**:
- [ ] Context captured in thread-local storage
- [ ] Available fields: user, IP, user_agent, request_path
- [ ] X-Forwarded-For properly parsed for real IP
- [ ] Context cleared after request completes
- [ ] Fallback values if context unavailable

## Signal Handlers

### Authentication Signals
**Auto-logged via Django signals**:
- [ ] `user_logged_in` → Login audit
- [ ] `user_logged_out` → Logout audit  
- [ ] `user_login_failed` → Failed login audit
- [ ] Signal handlers in `signals.py`
- [ ] Handlers connected in `AppConfig.ready()`

### Model Change Signals
**Check in PR**:
- [ ] `post_save` signal for create/update
- [ ] `post_delete` signal for delete
- [ ] Only sensitive models audited (not all models)
- [ ] Signal handlers differentiate create vs update
- [ ] Include old vs new values for updates
- [ ] Use `update_fields` to identify what changed

## AuditedModel Base Class

### Inheritance Pattern
**Check in PR**:
- [ ] Models inherit from `AuditedModel` for auto-audit
- [ ] Automatic logging on save() and delete()
- [ ] Override `get_audit_details()` for custom info
- [ ] Specify `audit_fields` to track specific fields
- [ ] Works with client group filtering

### What to Audit with AuditedModel
- [ ] User data models
- [ ] Financial transaction models
- [ ] Configuration models
- [ ] Access control models
- [ ] Document/file models
- [ ] NOT: Session data, temporary data, cache entries

## Decorators

### @audit_command
**Check in PR**:
- [ ] Applied to management commands
- [ ] Automatically logs: command name, args, duration, success/failure
- [ ] Exception details logged on failure
- [ ] User context (if command run by specific user)
- [ ] Timestamp and duration recorded

### Custom Audit Decorators
**Check in PR**:
- [ ] Function-level audit decorators for sensitive operations
- [ ] Log function name, args (sanitized), result status
- [ ] Don't log sensitive args (passwords, tokens)
- [ ] Exception handling doesn't suppress errors
- [ ] Performance impact minimal

## Audit Log Structure

### Required Fields
- [ ] Action type (login, create, update, delete, etc.)
- [ ] Timestamp (UTC, with timezone)
- [ ] User (user ID, not full user object)
- [ ] IP address
- [ ] User agent
- [ ] Request path
- [ ] Details (JSON field with context)

### Details Field Content
- [ ] Model name and object ID
- [ ] Changed fields (before/after values for updates)
- [ ] Action result (success/failure)
- [ ] Error message if failed
- [ ] No PII unless necessary for audit trail
- [ ] Structured data (not free-form text)

## Query and Reporting

### Audit Log Queries
**Check in PR**:
- [ ] Queries by user, action type, date range
- [ ] Indexes on commonly queried fields (user, timestamp, action)
- [ ] Pagination for large result sets
- [ ] Export functionality for compliance reports
- [ ] Read-only access for non-admins

### Retention Policy
- [ ] Define retention period (7 years for SOC2)
- [ ] Archive old logs (don't delete)
- [ ] Compressed storage for archives
- [ ] Restore procedure documented
- [ ] Compliance with regulatory requirements

## Client Group Context

### Multi-Tenancy Audit
**Check in PR**:
- [ ] Client group ID included in audit logs
- [ ] Audit logs filtered by client group for isolation
- [ ] Cross-tenant access attempts logged
- [ ] Client group switches logged
- [ ] Admin access logs visible across tenants

## API Access Auditing

### DRF Integration
**Check in PR**:
- [ ] Sensitive API endpoints log access
- [ ] Include: endpoint, method, response status, payload size
- [ ] Rate limit violations logged
- [ ] Authentication failures logged
- [ ] Service account usage logged separately

## Management Command Auditing

### Command Execution
**Check in PR**:
- [ ] All management commands use `@audit_command` decorator
- [ ] Scheduled commands (Celery Beat) audited
- [ ] Manual command runs audited with user context
- [ ] Command output not logged (only success/failure)
- [ ] Long-running commands show duration

## Performance Considerations

### Async Audit Logging
**Check in PR**:
- [ ] Heavy audit operations use Celery for async
- [ ] Critical operations log synchronously (auth events)
- [ ] Batch inserts for bulk operations
- [ ] Audit log writes don't block user requests
- [ ] Transaction context preserved

### Database Impact
**Check in PR**:
- [ ] Audit table indexed appropriately
- [ ] Partition audit table by date (optional, for large scale)
- [ ] Separate database connection for audits (optional)
- [ ] Monitor audit table size
- [ ] Alert on audit write failures

## Testing Audit Logging

### Unit Tests
**Check in PR**:
- [ ] Test audit log creation
- [ ] Test signal handlers trigger correctly
- [ ] Test `AuditedModel` base class
- [ ] Test decorator functionality
- [ ] Verify immutability enforcement

### Integration Tests
**Check in PR**:
- [ ] Test full request cycle audit
- [ ] Test context capture from middleware
- [ ] Test client group isolation
- [ ] Verify no audit log leaks between tests
- [ ] Test audit query performance

## Security and Compliance

### Access Control
**Check in PR**:
- [ ] Audit logs read-only for most users
- [ ] Admin-only access to full audit trail
- [ ] Client group filtering enforced
- [ ] Export permissions verified
- [ ] API access to audits secured

### PII Handling
**Check in PR**:
- [ ] PII masked in audit details where possible
- [ ] Audit logs follow data retention policies
- [ ] Export includes necessary PII only
- [ ] GDPR considerations documented
- [ ] User deletion doesn't delete audit trail (anonymize instead)

## Common Patterns to Check

### Authentication Event Audit
- [ ] Login/logout logged with IP and user agent
- [ ] Failed attempts include reason
- [ ] Rate limit lockouts logged
- [ ] SSO vs password auth differentiated
- [ ] Session timeout events logged

### Model Change Audit
- [ ] Create: log model name, ID, creator
- [ ] Update: log changed fields with old/new values
- [ ] Delete: log model name, ID, deleter (soft delete preferred)
- [ ] Bulk operations log summary (count, affected IDs)

### Permission Denial Audit
- [ ] 403 responses logged via `AuditAccessDeniedMiddleware`
- [ ] Include attempted action and resource
- [ ] User context and client group
- [ ] Permission check failures (not just HTTP 403s)

### File Operation Audit
- [ ] Uploads: filename, size, uploader, client group
- [ ] Downloads: filename, downloader, client group
- [ ] Deletions: filename, deleter, reason
- [ ] Access denials: attempted file, user, reason

## Monitoring and Alerting

### Audit System Health
**Check in PR**:
- [ ] Monitor audit write success rate
- [ ] Alert on audit write failures
- [ ] Track audit log growth rate
- [ ] Monitor query performance
- [ ] Alert on suspicious patterns (mass deletions, failed access)

### Compliance Reporting
**Check in PR**:
- [ ] Regular audit reports generated
- [ ] Anomaly detection (unusual activity)
- [ ] Failed access attempts summarized
- [ ] User activity reports available
- [ ] Export format compliance-ready

## Troubleshooting

### Audit Logs Not Creating
- Check signal handlers connected
- Verify `AuditContextMiddleware` in middleware stack
- Check database permissions
- Verify model inherits from `AuditedModel`
- Check for exceptions in audit code

### Missing Context in Audits
- Verify middleware order (AuditContext before views)
- Check thread-local storage setup
- Verify context cleared properly
- Check async/sync compatibility

### Performance Issues
- Check audit table size and indexes
- Consider async audit logging for heavy operations
- Partition audit table if very large
- Review batch insert patterns
- Monitor database connection pool

## Cross-Reference

Related docs:
- `soc2_considerations.md` - SOC2 requirements
- `custom_middleware_best_practices.md` - AuditContextMiddleware
- `authentication_authorization_best_practices.md` - Auth event auditing
- `django_best_practices.md` - Signal handlers, model patterns
- `performance_monitoring_best_practices.md` - Monitoring audit system
