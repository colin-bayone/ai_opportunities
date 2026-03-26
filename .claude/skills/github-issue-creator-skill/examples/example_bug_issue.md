# Issue: Prevent External Users from Being Promoted to Internal Status

**Dependencies:** None  
**Estimated Complexity:** Medium - Security enforcement across multiple layers

---

## Bug Description

External users can potentially be promoted to internal status through Django admin or database manipulation. This violates the fundamental business rule that external users must remain external permanently.

**Impact:**
- **Users Affected:** All external users and system integrity
- **Business Impact:** Unauthorized access to internal BayOne data, compliance violations
- **Severity Explanation:** High - Privilege escalation vulnerability

**Current Behavior:**
External users can have their status changed, email domains modified, or Microsoft accounts linked.

**Expected Behavior:**
Once classified as external, a user must permanently remain external with no path to internal status.

---

## Current State

**Technical Explanation:**
No enforcement at model, admin, or database level prevents external → internal transitions.

**Affected Components:**
- `core/accounts/models.py` - User/UserProfile models
- `core/accounts/admin.py` - Django admin configuration
- `core/accounts/adapters.py` - django-allauth adapters

**Root Cause:**
Missing validation and constraints to enforce user classification immutability.

**Why It's a Bug:**
Violates access control principles and creates security vulnerability.

---

## Technical Approach

### Implementation Strategy

Enforce immutability at three levels:
1. **Model-level:** Validation in `clean()` and database constraints
2. **Admin-level:** Read-only fields and save validation
3. **Social-auth-level:** Block Microsoft account linking for external users

**Pattern to Use:**
```python
# Model validation pattern
def clean(self):
    if self.pk:  # Existing record
        old = UserProfile.objects.get(pk=self.pk)
        if old.is_external_user and not self.is_external_user:
            raise ValidationError("External users cannot become internal")
```

### Best Practices References

This fix should follow:
- [ ] `authentication_authorization_best_practices.md` - User classification
- [ ] `soc2_considerations.md` - Access control enforcement
- [ ] `django_best_practices.md` - Model validation

**Think about:**
- Should we allow ANY field changes for external users?
- How to handle edge cases (data corrections)?

---

## Tasks

### 1. Add Model-Level Enforcement

**File:** `core/accounts/models.py`

Add validation to UserProfile model.

**Pattern:**
```python
class UserProfile(models.Model):
    is_external_user = models.BooleanField(default=True)
    
    def clean(self):
        # Check if trying to change external → internal
        # Raise ValidationError if prohibited
        # Validate email domain consistency
        pass
    
    class Meta:
        constraints = [
            # CheckConstraint for email/status consistency
        ]
```

**Think about:**
- What if admin needs to correct a misclassification?
- How to document legitimate edge cases?

---

### 2. Enforce in Django Admin

**File:** `core/accounts/admin.py`

Make classification fields read-only, validate in save_model.

**Pattern:**
```python
class UserProfileAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing existing
            return ['is_external_user', 'registration_method']
        return []
    
    def save_model(self, request, obj, form, change):
        # Validate no status changes
        # Show error message if attempted
        # Don't save if invalid
        pass
```

---

### 3. Block Social Account Linking

**File:** `core/accounts/adapters.py`

Prevent external users from linking Microsoft accounts.

**Pattern:**
```python
def pre_social_login(self, request, sociallogin):
    # Check if existing external user
    # If trying to link Microsoft account → block
    # Return error with clear message
    pass
```

---

### 4. Add Verification Command

**Create:** `core/accounts/management/commands/verify_user_classification.py`

Audit tool to check user classifications.

**Pattern:**
```python
class Command(BaseCommand):
    def handle(self, *args, **options):
        # For each user:
        #   Check email domain vs is_external_user
        #   Check social accounts vs classification
        #   Report inconsistencies
        pass
```

---

## Testing

### Manual Testing Flow

1. Create external user via email signup
2. Attempt to change is_external_user in admin → Should fail
3. Attempt to change email to @bayone.com → Should fail
4. Attempt to link Microsoft account → Should fail
5. Verify error messages are clear

### Edge Cases

- External user with BayOne email (data error)
- Staff user without Microsoft account
- User with multiple social accounts

### Django Shell Testing

```python
python manage.py shell
>>> profile = UserProfile.objects.get(user__email='external@example.com')
>>> profile.is_external_user = False
>>> profile.save()  # Should raise ValidationError
```

---

## Acceptance Criteria

**Functionality:**
- [ ] Model validation prevents external → internal
- [ ] Admin interface blocks status changes
- [ ] Email domain changes blocked for external users
- [ ] Social account linking blocked for external users
- [ ] Clear error messages for all blocked operations

**Code Quality:**
- [ ] Follows Django model validation patterns
- [ ] Database constraints added
- [ ] Admin customizations follow `django_best_practices.md`

**Testing:**
- [ ] Unit tests for model validation
- [ ] Integration tests for admin
- [ ] Tests for social auth blocking
- [ ] Edge cases covered

**Compliance:**
- [ ] Audit logging for attempted status changes
- [ ] Documentation updated with classification rules
- [ ] Follows `soc2_considerations.md` - Access Control

---

## Notes

### Using Claude Code Effectively

**For Model Validation:**
Ask Claude Code to help implement the validation pattern with proper exception handling and clear error messages.

**For Admin Customization:**
Claude Code can help structure the admin class with proper readonly logic and save validation.

**For Testing:**
Use Claude Code to generate comprehensive test cases covering all enforcement points.

### Django Patterns Reference

**Model Validation:**
Use `clean()` method for complex validation. Call in `save()` to ensure validation runs. Add database constraints for additional safety layer.

**Admin Customization:**
Override `get_readonly_fields()` for conditional readonly. Use `save_model()` for validation that shows user-friendly errors.

**Signal Handlers:**
Consider pre_save signal for User model email changes. Prevents end-run around UserProfile validation.

### Common Pitfalls

1. **Only enforcing in one place:** Need enforcement at model, admin, AND social auth levels
2. **Forgetting database constraints:** Add CHECK constraints for belt-and-suspenders approach
3. **Poor error messages:** Users need to understand WHY operation blocked
4. **Missing edge cases:** Test with existing bad data

### Security Considerations

**Attack Vectors Prevented:**
- Direct admin manipulation
- Database updates bypassing ORM
- Social account exploitation
- Email domain manipulation

**Defense in Depth:**
Multiple layers ensure no single bypass point.

### Migration Strategy

**Developer Actions:**
1. Add fields to UserProfile model
2. Create migration locally
3. Test migration on Docker postgres
4. **Ask Colin to review changes**
5. **Colin runs migration on main**

**Data Migration:**
May need to audit existing users and fix classifications before adding constraints.

---

## Related Issues

- Related to authentication implementation
- Related to Microsoft SSO configuration
- Blocks any features assuming user classification immutability

---

## Additional Context

This is HIGH PRIORITY security issue. External → internal promotion would bypass:
- Microsoft SSO requirement
- Access controls
- Audit logging assumptions
- Multi-tenancy boundaries
