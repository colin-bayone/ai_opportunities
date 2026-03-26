# PII Detection & Masking - Review Checklist

Review checklist for PII handling in code. Focus on verifying proper detection and masking patterns, regardless of implementation approach.

## PII Detection in Code

### Logging & Output
- [ ] No PII written to application logs
- [ ] No PII in error messages shown to users
- [ ] No PII in debug output
- [ ] No PII in exception stack traces
- [ ] No PII in metrics or monitoring data
- [ ] Console.log or print statements don't expose PII

### Database Storage
- [ ] PII fields identified in models
- [ ] Encryption applied to sensitive PII fields (if required)
- [ ] Database queries don't log PII parameters
- [ ] Database connection strings don't contain PII
- [ ] Migration scripts don't expose PII in logs

### API Responses
- [ ] API responses don't include unnecessary PII
- [ ] PII filtered based on user permissions
- [ ] Audit logs capture PII access without storing full PII
- [ ] Error responses don't leak PII from failed operations

### File Handling
- [ ] Uploaded files with PII processed securely
- [ ] PII removed from temporary files after processing
- [ ] File paths don't contain PII
- [ ] Log messages about files don't expose PII content

## Common PII Types to Check

### Personal Identifiers
- [ ] Full names not logged unnecessarily
- [ ] Email addresses masked in logs
- [ ] Phone numbers masked in logs
- [ ] Social Security Numbers never logged
- [ ] Government ID numbers never logged
- [ ] IP addresses masked where required

### Financial Information
- [ ] Credit card numbers never logged
- [ ] Bank account numbers never logged
- [ ] Financial transaction details appropriately masked
- [ ] Payment tokens not exposed in logs

### Health Information
- [ ] Medical records not logged
- [ ] Health conditions not exposed
- [ ] Prescriptions not logged
- [ ] HIPAA compliance maintained (if applicable)

### Authentication Credentials
- [ ] Passwords never logged (even hashed)
- [ ] API keys masked in logs
- [ ] OAuth tokens not logged
- [ ] Session IDs not logged in full

## Infrastructure Secrets

### Azure & Cloud Credentials
- [ ] Azure Storage URLs masked in logs
- [ ] Blob Storage SAS tokens not logged
- [ ] Azure connection strings masked
- [ ] Service principal credentials not exposed
- [ ] Managed identity tokens not logged

### Database Credentials
- [ ] Database passwords not in code
- [ ] Connection strings masked in logs
- [ ] PostgreSQL connection URLs masked
- [ ] Redis passwords not exposed

### Third-Party API Keys
- [ ] OpenAI API keys not logged
- [ ] Service API keys masked
- [ ] Webhook secrets not exposed
- [ ] Integration tokens secured

## Masking Patterns

### What to Look For
- [ ] Consistent masking approach across codebase
- [ ] Masking applied before logging, not after
- [ ] Masking doesn't break legitimate use cases
- [ ] Masked values clearly identified (e.g., `<EMAIL_ADDRESS>`, `***`)
- [ ] Masking preserves data types for debugging (e.g., email → email format)

### Common Masking Mistakes
- [ ] Partial masking that's reversible (e.g., `jo**@example.com`)
- [ ] Masking applied inconsistently
- [ ] Logging full value then attempting to mask later
- [ ] Regular expressions that miss edge cases
- [ ] Masking disabled in development (should always be on)

## Configuration & Settings

### Environment Variables
- [ ] PII masking enabled in all environments
- [ ] Masking configuration not bypassable in production
- [ ] Settings for masking level (if configurable)
- [ ] No "debug mode" that disables masking

### Feature Flags
- [ ] PII masking cannot be disabled via feature flag in production
- [ ] Audit logging when masking configuration changes
- [ ] Emergency access documented and logged

## Code Review Patterns

### New Logging Statements
- [ ] All new log statements reviewed for PII
- [ ] Structured logging used (easier to mask)
- [ ] Log levels appropriate (DEBUG might have more data)
- [ ] Exception handlers don't log full exception with PII

### Database Queries
- [ ] Query parameters logged safely
- [ ] ORM query debugging doesn't expose PII
- [ ] Raw SQL queries reviewed for PII in logs
- [ ] Query results not logged with full PII

### External API Calls
- [ ] API request logs don't include PII in URLs
- [ ] Request bodies with PII not logged
- [ ] Response bodies with PII not logged fully
- [ ] API errors don't expose PII

### Testing
- [ ] Test data doesn't use real PII
- [ ] Test logs don't expose PII
- [ ] Test fixtures use fake/synthetic PII
- [ ] Integration tests mask PII appropriately

## Audit & Compliance

### Access Logging
- [ ] PII access logged (who accessed what, when)
- [ ] Audit logs don't store full PII values
- [ ] Audit trail preserved for compliance
- [ ] Unusual PII access patterns flagged

### Data Minimization
- [ ] Only necessary PII collected
- [ ] PII retention periods defined
- [ ] PII deleted per retention policy
- [ ] Data exports exclude unnecessary PII

### User Rights
- [ ] Users can export their PII (GDPR)
- [ ] Users can delete their PII (right to be forgotten)
- [ ] PII export includes all user data
- [ ] PII deletion is thorough (not just soft delete)

## Common Anti-Patterns

Verify these DON'T exist in the PR:
- [ ] String formatting with PII in log messages: `logger.info(f"User email: {email}")`
- [ ] Exception messages containing PII: `raise ValueError(f"Invalid email: {user.email}")`
- [ ] Debug prints left in code: `print(user.ssn)`
- [ ] Conditional masking based on environment: `if DEBUG: log(email)`
- [ ] PII in URL parameters: `/api/user/search?email=user@example.com`
- [ ] PII in git commit messages
- [ ] Test assertions with real PII
- [ ] Documentation examples with real PII

## Questions to Ask During Review

1. **Could this log statement expose PII?** Check all logger calls in the diff
2. **Does this error message include user data?** Check exception messages
3. **Are database queries logged with parameters?** Check ORM/SQL logging
4. **Do external API calls log request/response?** Check HTTP client usage
5. **Are file paths or names based on PII?** Check file operations
6. **Could this debug code expose PII?** Check temporary debugging code
7. **Do test cases use realistic-looking PII?** Could be confused for real data
8. **Is PII minimized?** Could less data achieve same goal?

## Integration Points to Review

### Forms & User Input
- [ ] Form validation errors don't echo PII
- [ ] Form data not logged on submission
- [ ] AJAX requests don't log PII payloads

### Background Jobs
- [ ] Celery task arguments don't contain PII (use IDs instead)
- [ ] Job logs don't expose PII
- [ ] Failed job logs mask PII

### WebSockets
- [ ] WebSocket messages with PII not logged
- [ ] Real-time updates don't expose other users' PII
- [ ] Connection logs don't include PII

### Monitoring & Metrics
- [ ] Performance metrics don't include PII
- [ ] Error tracking (Sentry, etc.) masks PII
- [ ] Health check endpoints don't expose PII
- [ ] Status pages don't show PII

## Documentation Requirements

- [ ] PII fields documented in model docstrings
- [ ] Masking approach documented for team
- [ ] Examples in docs use fake/synthetic PII
- [ ] API docs show masked examples
- [ ] README doesn't contain real PII

## Cross-Reference

Related docs:
- `soc2_considerations.md` - Compliance logging requirements
- `web_security_best_practices.md` - General security patterns
- `audit_logging_best_practices.md` - What to log vs. what to mask
- `ai_ml_integration_best_practices.md` - PII in ML contexts
