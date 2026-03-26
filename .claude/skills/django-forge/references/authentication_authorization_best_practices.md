# Authentication & Authorization Best Practices

Django authentication and authorization patterns based on your stack: django-allauth, Microsoft SSO, custom backends, and multi-tenancy.

## Custom Authentication Backend

### StaffSSOOnlyBackend Pattern
- [ ] `StaffSSOOnlyBackend` used instead of `ModelBackend`
- [ ] Staff users (`is_staff=True`) blocked from password authentication
- [ ] External users can use email/password authentication
- [ ] Emergency backdoor (`EMERGENCY_ADMIN_PASSWORD_AUTH`) logs CRITICAL alerts
- [ ] Backend returns `None` (not raising exception) when auth should be denied

### Rate Limiting in Backend
- [ ] Rate limiting implemented at backend level (5 failed attempts in 15 minutes)
- [ ] 30-minute lockout after threshold
- [ ] IP-based tracking using cache backend
- [ ] Failed attempts logged with IP address and username
- [ ] Rate limit keys namespaced properly (`auth_rate_limit:{ip}`)

### Backend authenticate() Method
- [ ] Returns `User` object on success
- [ ] Returns `None` on failure (never raises exception)
- [ ] Checks rate limiting before attempting authentication
- [ ] Validates user exists before checking password
- [ ] Enforces SSO-only policy for staff users
- [ ] Logs all authentication attempts

## django-allauth Configuration

### Account Adapters

#### NoNewUsersAccountAdapter
- [ ] Extends `DefaultAccountAdapter`
- [ ] Email verification required (`ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`)
- [ ] Internal employee emails blocked from signup (BayOne domain)
- [ ] Rate limiting applied (same as backend: 5/15min = 30min lockout)
- [ ] Clear error messages for blocked attempts
- [ ] Domain checking case-insensitive

#### AdminOrMicrosoftSocialAccountAdapter
- [ ] Extends `DefaultSocialAccountAdapter`
- [ ] Internal domains must use Microsoft SSO (no other social providers)
- [ ] External users blocked from Microsoft SSO
- [ ] Auto-connects social accounts to existing users by email
- [ ] Validates email domain before allowing connection
- [ ] Returns user object when auto-connecting

### allauth Settings
- [ ] `ACCOUNT_AUTHENTICATION_METHOD = 'email'` (not username)
- [ ] `ACCOUNT_EMAIL_REQUIRED = True`
- [ ] `ACCOUNT_USERNAME_REQUIRED = False`
- [ ] `ACCOUNT_EMAIL_VERIFICATION = 'mandatory'` for external users
- [ ] `SOCIALACCOUNT_AUTO_SIGNUP = True` (with domain validation)
- [ ] `SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'` (SSO pre-verified)
- [ ] Custom adapters registered in settings

### Microsoft Provider Configuration
- [ ] `SOCIALACCOUNT_PROVIDERS` includes Microsoft configuration
- [ ] `APP` section has client_id from Azure AD
- [ ] `SCOPE` includes `openid`, `email`, `profile`
- [ ] Tenant ID configured for organizational accounts
- [ ] Callback URL matches Azure AD app registration
- [ ] Provider enabled in Django admin

## Session Management

### Session Timeout Middleware

#### StaffSessionTimeoutMiddleware
- [ ] Extends `MiddlewareMixin`
- [ ] Only applies to staff users (`is_staff=True`)
- [ ] Timeout configurable via `STAFF_SESSION_TIMEOUT_MINUTES` (default 30)
- [ ] Updates `last_activity` timestamp in session on each request
- [ ] Graceful logout with user-friendly message
- [ ] Redirects to login page after timeout
- [ ] Does not affect external users

### Session Security Settings
- [ ] `SESSION_COOKIE_SECURE = True` in production
- [ ] `SESSION_COOKIE_HTTPONLY = True`
- [ ] `SESSION_COOKIE_SAMESITE = 'Strict'` in production
- [ ] `SESSION_ENGINE` configured (database or cache-backed)
- [ ] `SESSION_COOKIE_AGE` set appropriately
- [ ] Session data validated on each request

## Multi-Tenancy (Client Groups)

### ClientGroupMiddleware
- [ ] Validates client group membership for authenticated users
- [ ] Sets `request.client_group` from session
- [ ] Handles missing or invalid client group gracefully
- [ ] Logs client group changes
- [ ] Works with client group selector in UI
- [ ] Does not block anonymous users

### Client Group Filtering
- [ ] `@filter_by_client_group` decorator used on views returning querysets
- [ ] All model queries filtered by `client_group` field
- [ ] No direct queries without client group filter
- [ ] Related objects checked for client group membership
- [ ] Template context includes client group
- [ ] API endpoints enforce client group isolation

### Client Group Switching
- [ ] User can only switch to groups they're a member of
- [ ] Client group stored in session (`client_group_id`)
- [ ] Switching validated against user's `ClientGroupMembership`
- [ ] Session cleared and re-established on switch
- [ ] Audit log created on client group switch

## Role-Based Access Control

### Role Decorator
- [ ] `@role_required(role)` decorator used on views
- [ ] Role checked against user's role in current client group
- [ ] Returns 403 if user lacks required role
- [ ] Works with multi-tenancy (client group context)
- [ ] Logs access denials via `AuditAccessDeniedMiddleware`
- [ ] Clear error message for denied access

### Permission System
- [ ] Roles defined per client group (not global)
- [ ] User has different roles in different client groups
- [ ] Template permissions pre-computed in `navbar_permissions` context processor
- [ ] Permission checks at view level, not just template level
- [ ] Decorator-based permission checks preferred over manual checks

### Common Roles
- [ ] Roles consistently named across application
- [ ] Role hierarchy documented (if applicable)
- [ ] Default role assigned on user creation
- [ ] Role changes audited

## Audit Middleware

### AuditContextMiddleware
- [ ] Captures request context in thread-local storage
- [ ] Sets user, IP address, user agent, request path
- [ ] Handles X-Forwarded-For for real client IP
- [ ] Context available to audit service
- [ ] Context cleared after request completes
- [ ] Works with async views

### AuditAccessDeniedMiddleware
- [ ] Logs all 403 responses
- [ ] Captures user, path, and reason
- [ ] Placed after authentication middleware
- [ ] Does not block request processing
- [ ] Creates audit log entry for permission denial

## Authentication Views

### Login Views
- [ ] Admin login uses custom template with SSO button
- [ ] External user login uses allauth views
- [ ] Password reset rate limited
- [ ] Email verification rate limited
- [ ] Clear error messages for all failure scenarios
- [ ] Redirect to intended page after login

### SSO Flow
- [ ] Microsoft SSO button in login template
- [ ] Initiates OAuth flow via allauth
- [ ] Handles OAuth callback
- [ ] Creates or updates user account
- [ ] Links to existing account by email if found
- [ ] Sets appropriate session data

### Logout
- [ ] Clears session completely
- [ ] Creates audit log entry
- [ ] Redirects to login page
- [ ] Handles CSRF token properly
- [ ] POST-only logout (no GET logout links)

## Rate Limiting Implementation

### Cache-Based Rate Limiting
- [ ] Uses Redis in production, in-memory cache in dev
- [ ] Rate limit keys include IP address
- [ ] Counter incremented on each attempt
- [ ] Counter expires after time window
- [ ] Lockout key set when threshold reached
- [ ] Lockout key has its own expiration

### Rate Limit Patterns
```python
# Check rate limit
cache_key = f"auth_rate_limit:{ip}"
attempts = cache.get(cache_key, 0)
if attempts >= MAX_ATTEMPTS:
    # Check if lockout period expired
    lockout_key = f"auth_lockout:{ip}"
    if cache.get(lockout_key):
        return None  # Still locked out
    else:
        cache.delete(cache_key)  # Reset counter

# Increment counter
cache.set(cache_key, attempts + 1, timeout=WINDOW_SECONDS)
```

### Rate Limit Testing
- [ ] Rate limits tested in unit tests
- [ ] Lockout behavior verified
- [ ] Counter expiration tested
- [ ] Multiple IPs tested independently

## Security Best Practices

### Password Security
- [ ] Staff users cannot set passwords (SSO-only)
- [ ] External user passwords validated (Django's password validators)
- [ ] Password reset tokens single-use
- [ ] Password reset emails rate limited
- [ ] Passwords never logged
- [ ] Emergency admin password usage logs CRITICAL

### Token Security
- [ ] OAuth tokens stored securely (allauth handles this)
- [ ] Tokens refreshed appropriately
- [ ] Expired tokens handled gracefully
- [ ] Token validation on each request
- [ ] No tokens in URLs or logs

### Email Verification
- [ ] Verification emails rate limited
- [ ] Verification tokens single-use
- [ ] Verification tokens time-limited
- [ ] Clear instructions in verification email
- [ ] Resend verification available but rate limited

## Testing Authentication

### Unit Tests
- [ ] Test staff user blocked from password auth
- [ ] Test external user can use password auth
- [ ] Test rate limiting (success and lockout)
- [ ] Test session timeout
- [ ] Test SSO flow (mock OAuth)
- [ ] Test client group validation
- [ ] Test role-based access control

### Integration Tests
- [ ] Test complete login flow (password and SSO)
- [ ] Test logout and session clearing
- [ ] Test client group switching
- [ ] Test permission denials
- [ ] Test audit logging for auth events

## Common Patterns

### Checking if User is Staff SSO User
```python
if user.is_staff and not settings.EMERGENCY_ADMIN_PASSWORD_AUTH:
    # Block password authentication
    return None
```

### Getting Client Group from Session
```python
client_group_id = request.session.get('client_group_id')
if client_group_id:
    try:
        client_group = ClientGroup.objects.get(id=client_group_id)
    except ClientGroup.DoesNotExist:
        # Handle invalid client group
        pass
```

### Role-Based View Protection
```python
@login_required
@role_required('admin')
def admin_view(request):
    # Only users with 'admin' role in current client group can access
    pass
```

### Filtering by Client Group
```python
@filter_by_client_group
def my_view(request):
    # Queryset will automatically filter by request.client_group
    objects = MyModel.objects.all()  # Auto-filtered
    return render(request, 'template.html', {'objects': objects})
```

## Troubleshooting

### "Password authentication not allowed"
- User is staff and trying password auth → Expected, use SSO
- Check `EMERGENCY_ADMIN_PASSWORD_AUTH` setting if needed

### Rate limit not resetting
- Check cache backend configuration
- Verify timeout values are correct
- Check if lockout key persists beyond window

### SSO not connecting to existing account
- Check email match between SSO and existing user
- Verify `AdminOrMicrosoftSocialAccountAdapter.pre_social_login()` logic
- Check domain validation

### Session timeout not working
- Verify `StaffSessionTimeoutMiddleware` in middleware stack
- Check `STAFF_SESSION_TIMEOUT_MINUTES` setting
- Ensure middleware is after `AuthenticationMiddleware`

## Cross-Reference

Related docs:
- `soc2_considerations.md` - Audit logging requirements
- `web_security_best_practices.md` - General auth security
- `redis_best_practices.md` - Cache backend for rate limiting
- `custom_middleware_best_practices.md` - Middleware patterns
