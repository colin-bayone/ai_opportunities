# Django Best Practices Checklist

This reference provides detailed Django best practices to check during PR reviews.

## Models

### Field Definitions

- [ ] ForeignKey/OneToOneField has `on_delete` parameter (required in Django 2.0+)
- [ ] Use appropriate `on_delete` options: CASCADE, PROTECT, SET_NULL, SET_DEFAULT
- [ ] CharField has appropriate `max_length`
- [ ] Use `blank=True` for optional form fields, `null=True` for optional database fields
- [ ] DateTimeField uses `auto_now` or `auto_now_add` for timestamps
- [ ] FileField/ImageField has `upload_to` parameter

### Model Methods

- [ ] `__str__` method defined for all models
- [ ] Custom model methods are in the right place (not in views)
- [ ] Property decorators used appropriately
- [ ] Class methods use `@classmethod` decorator
- [ ] Static methods use `@staticmethod` decorator

### Meta Options

- [ ] `ordering` defined for models that need consistent ordering
- [ ] `verbose_name` and `verbose_name_plural` set for admin
- [ ] `db_table` only used when necessary (legacy databases)
- [ ] Appropriate indexes defined
- [ ] `unique_together` or `constraints` used for uniqueness

## Views

### Class-Based Views (CBV)

- [ ] Using appropriate generic views (ListView, DetailView, CreateView, etc.)
- [ ] Overriding correct methods (get_queryset, get_context_data, etc.)
- [ ] Permission checks in place (LoginRequiredMixin, PermissionRequiredMixin)
- [ ] Form handling uses form_valid() and form_invalid()

### Function-Based Views (FBV)

- [ ] Appropriate HTTP method handling (@require_http_methods, @require_POST, etc.)
- [ ] Permission decorators applied (@login_required, @permission_required)
- [ ] Proper HttpResponse types returned

### Query Optimization

- [ ] select_related() used for foreign key lookups
- [ ] prefetch_related() used for reverse foreign keys and many-to-many
- [ ] No N+1 query problems
- [ ] Querysets filtered before iteration
- [ ] values() or values_list() used when only specific fields needed
- [ ] count() used instead of len(queryset)
- [ ] exists() used instead of bool(queryset)

## Forms

### Form Definition

- [ ] ModelForm used when possible instead of plain Form
- [ ] Meta.model and Meta.fields defined correctly
- [ ] Custom validation in clean() methods
- [ ] Field-specific validation in clean_<fieldname>() methods
- [ ] Widgets customized when needed

### Form Processing

- [ ] Forms properly validated before saving
- [ ] Error handling for invalid forms
- [ ] CSRF token present in templates
- [ ] File uploads handled securely

## URLs

### URL Patterns

- [ ] Name attribute used for all URLs
- [ ] Reverse() or {% url %} used instead of hardcoded URLs
- [ ] Namespacing used for app-specific URLs
- [ ] Path converters appropriate (<int:pk>, <slug:slug>, etc.)

## Templates

### Template Best Practices

- [ ] Template inheritance used properly
- [ ] Static files loaded with {% load static %}
- [ ] URL tags used: {% url 'name' %}
- [ ] CSRF token included in forms: {% csrf_token %}
- [ ] Template filters and tags used appropriately
- [ ] No business logic in templates

## Security

### Common Security Checks

- [ ] User input properly escaped in templates (automatic in Django)
- [ ] Raw SQL only used when necessary and with parameterized queries
- [ ] Sensitive data not logged or exposed
- [ ] File uploads validated and restricted
- [ ] Authentication and authorization enforced
- [ ] HTTPS enforced for sensitive operations
- [ ] Secret keys and credentials not in code

## Testing

### Test Coverage

- [ ] Models have tests for custom methods and properties
- [ ] Views have tests for success and error cases
- [ ] Forms have tests for validation
- [ ] URL routing tested
- [ ] Authentication/authorization tested
- [ ] Edge cases tested

### Test Quality

- [ ] Tests use Django TestCase or similar
- [ ] Fixtures used appropriately
- [ ] setUp() and tearDown() methods used properly
- [ ] Tests are independent and can run in any order
- [ ] Test names clearly describe what they test

## Migrations

### Migration Best Practices

- [ ] Migrations created with makemigrations
- [ ] Migration files reviewed for correctness
- [ ] Data migrations used for data changes
- [ ] RunPython used correctly in data migrations
- [ ] Migrations are reversible when possible
- [ ] Dependencies correctly specified
- [ ] No manual edits to migration files (unless necessary)

## Performance

### Query Performance

- [ ] Database indexes on frequently queried fields
- [ ] Avoid querying in loops
- [ ] Bulk operations used when appropriate (bulk_create, bulk_update)
- [ ] Database-level operations used instead of Python loops
- [ ] Pagination implemented for large datasets

### Caching

- [ ] Cache framework used appropriately
- [ ] Cache keys follow naming conventions
- [ ] Cache invalidation handled properly
- [ ] Querysets cached when beneficial

## Code Organization

### Project Structure

- [ ] Models in models.py (or models/ directory)
- [ ] Views in views.py (or views/ directory)
- [ ] Business logic in appropriate service modules
- [ ] Utilities in utils.py or helpers.py
- [ ] Signals in signals.py
- [ ] Management commands in management/commands/

### Code Quality

- [ ] DRY principle followed
- [ ] Functions/methods have single responsibility
- [ ] Imports organized (standard library, third-party, local)
- [ ] Docstrings for complex functions/classes
- [ ] Type hints used (Python 3.5+)
- [ ] Code follows PEP 8 style guide

## Common Anti-Patterns to Avoid

- [ ] **Fat Models**: Keep business logic in services, not models
- [ ] **Logic in Templates**: Move complex logic to views or template tags
- [ ] **Hardcoded URLs**: Always use reverse() or {% url %}
- [ ] **Query in Loops**: Use select_related()/prefetch_related()
- [ ] **Catching All Exceptions**: Catch specific exceptions
- [ ] **Using .get() without error handling**: Use try/except or get_object_or_404()
- [ ] **Mutable Default Arguments**: Don't use [] or {} as default values
- [ ] **Not Using get_absolute_url()**: Define this method on models
