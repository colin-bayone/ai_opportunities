# Django Templates Best Practices

Template patterns for your stack: Django templates, Phoenix Admin Theme, Bootstrap 5, custom inclusion tags, and HTMX integration.

## Template Organization

### File Structure
- [ ] Templates in app-specific directories: `templates/[app_name]/`
- [ ] Shared components in `templates/components/`
- [ ] Reusable partials in `templates/partials/`
- [ ] Custom error pages in `templates/errors/` (400, 403, 404, 500)
- [ ] No templates in root `templates/` directory (use subdirectories)

### Base Templates
- [ ] `main_base.html` for authenticated app layout (sidebar, navbar, breadcrumbs)
- [ ] `auth_base.html` for authentication pages (split-screen design)
- [ ] `base.html` for simple fallback layout
- [ ] App-specific base templates extend from appropriate base
- [ ] No duplicate layout code across templates

## Template Inheritance

### Proper Inheritance Chain
- [ ] Child templates extend from appropriate base: `{% extends "main_base.html" %}`
- [ ] Block structure consistent across inheritance chain
- [ ] `{% block title %}` defined in child templates
- [ ] `{% block content %}` contains page-specific content
- [ ] Optional blocks used for customization (e.g., `extra_css`, `extra_js`)

### Block Usage
- [ ] Standard blocks: `title`, `content`, `extra_css`, `extra_js`
- [ ] `{{ block.super }}` used when extending parent block content
- [ ] Blocks not deeply nested (max 2-3 levels)
- [ ] Empty blocks removed (no `{% block %}{% endblock %}` with nothing)

## Custom Template Tags

### Inclusion Tag Usage
- [ ] Use inclusion tags for reusable components
- [ ] Component templates in `templates/components/`
- [ ] Tag parameters have sensible defaults
- [ ] Documentation for required vs optional parameters
- [ ] Tags loaded at template top: `{% load auth_components %}`

### Your Custom Tags
- [ ] `{% admin_login_form %}` - Admin login with password/SSO
- [ ] `{% auth_divider %}` - "or" divider with lines
- [ ] `{% auth_messages %}` - Flash message display
- [ ] `{% main_navigation %}` - Top horizontal navbar
- [ ] `{% vertical_navigation %}` - Sidebar navigation
- [ ] `{% reusable_modal %}` - Bootstrap modal wrapper
- [ ] `{% reusable_table %}` - Data table component
- [ ] `{% reusable_card %}` - Card container
- [ ] `{% cdn_asset 'path' %}` - CDN URL generation
- [ ] `{% cdn_script 'name' %}` - Script with SRI
- [ ] `{% cdn_link 'name' %}` - Link with SRI

### Tag Parameters
- [ ] Required parameters always provided
- [ ] Optional parameters have clear defaults
- [ ] Boolean parameters use proper syntax: `show_footer=True`
- [ ] CSS classes passed as strings: `css_class="mb-3"`
- [ ] No hardcoded values that should be parameters

## Template Syntax

### Django Template Language
- [ ] Proper syntax: `{{ variable }}`, `{% tag %}`
- [ ] No raw Python in templates (use template filters/tags)
- [ ] Whitespace control used: `{%- tag -%}` when needed
- [ ] Comments use `{# comment #}` not HTML comments for logic
- [ ] No template syntax in JavaScript (use data attributes)

### Variable Access
- [ ] Use dot notation: `{{ user.username }}`
- [ ] Check for None/empty: `{% if variable %}`
- [ ] Use `|default` filter for fallbacks: `{{ value|default:"N/A" }}`
- [ ] No complex logic in templates (move to view/context processor)

### Template Filters
- [ ] Built-in filters used correctly: `{{ date|date:"Y-m-d" }}`
- [ ] Custom filters loaded: `{% load custom_filters %}`
- [ ] Chained filters: `{{ text|truncatewords:50|capfirst }}`
- [ ] No filter overuse (move complex formatting to view)

## Static Files

### Static File Loading
- [ ] `{% load static %}` at template top (after extends)
- [ ] Static files referenced: `{% static 'path/to/file.css' %}`
- [ ] No hardcoded `/static/` paths
- [ ] CDN assets use `{% cdn_asset %}` tag
- [ ] Conditional loading based on environment (dev vs prod)

### CSS and JavaScript
- [ ] CSS in `{% block extra_css %}` or head
- [ ] JavaScript in `{% block extra_js %}` or before `</body>`
- [ ] Async/defer attributes on non-critical scripts
- [ ] No inline styles (use CSS classes)
- [ ] Minimal inline JavaScript (prefer external files)

## Forms

### Form Rendering
- [ ] Use django-bootstrap5: `{% bootstrap_form form %}`
- [ ] CSRF token in all forms: `{% csrf_token %}`
- [ ] Form errors displayed: `{% bootstrap_form_errors form %}`
- [ ] Field help text shown
- [ ] Required fields marked visually

### Form Attributes
- [ ] `method="post"` for state-changing operations
- [ ] `enctype="multipart/form-data"` for file uploads
- [ ] Form action specified or defaults to current URL
- [ ] `novalidate` used if custom validation needed
- [ ] Accessible labels: `<label for="id_field">` or django-bootstrap5

### HTMX Forms
- [ ] HTMX attributes on form or submit button
- [ ] `hx-post` or `hx-get` with URL
- [ ] `hx-target` specifies swap target
- [ ] `hx-swap` defines swap strategy (innerHTML, outerHTML, etc.)
- [ ] `hx-disabled-elt` prevents double submit
- [ ] CSRF token included (HTMX automatically includes it)

## HTMX Integration

### HTMX Attributes
- [ ] Valid HTMX attributes: `hx-get`, `hx-post`, `hx-put`, `hx-delete`
- [ ] Target specified: `hx-target="#container"`
- [ ] Swap strategy: `hx-swap="innerHTML"` (or outerHTML, beforeend, etc.)
- [ ] Trigger configured: `hx-trigger="click"` (or custom events)
- [ ] Loading states: `hx-indicator="#spinner"`

### HTMX Partials
- [ ] Partial templates return only fragment (no full page)
- [ ] Partials in `templates/partials/` directory
- [ ] Out-of-band swaps use `hx-swap-oob="true"`
- [ ] Multiple OOB elements have unique IDs
- [ ] Error responses also return partial HTML

### HTMX Events
- [ ] JavaScript listens for HTMX events when needed
- [ ] `htmx:afterSwap` - Re-initialize plugins (Feather icons, MathJax)
- [ ] `htmx:beforeRequest` - Show loading states
- [ ] `htmx:afterRequest` - Clear loading states
- [ ] Custom events dispatched when appropriate

## Phoenix Theme Integration

### Theme Classes
- [ ] Use Phoenix CSS classes: `.card`, `.btn`, `.form-control`
- [ ] Bootstrap 5 utility classes: `.mb-3`, `.d-flex`, `.justify-content-between`
- [ ] Phoenix components: `.navbar`, `.sidebar`, `.breadcrumb`
- [ ] No conflicting custom CSS that breaks theme
- [ ] Responsive classes: `.d-none`, `.d-md-block`

### Theme Compatibility
- [ ] Light/dark mode classes if using theme switcher
- [ ] Phoenix-compatible color variables
- [ ] No hardcoded colors (use CSS variables or theme classes)
- [ ] Icons use Feather Icons (primary) or FontAwesome (secondary)

## Accessibility

### ARIA Attributes
- [ ] `aria-label` on icon-only buttons
- [ ] `aria-labelledby` links label to element
- [ ] `aria-describedby` links description to element
- [ ] `aria-expanded` on collapsible elements
- [ ] `aria-hidden="true"` on decorative icons
- [ ] `aria-current="page"` on active navigation

### Semantic HTML
- [ ] Use semantic tags: `<nav>`, `<main>`, `<article>`, `<section>`
- [ ] Heading hierarchy correct (h1 → h2 → h3)
- [ ] Form labels associated with inputs
- [ ] Button elements for actions (not `<a>` styled as button)
- [ ] Link elements for navigation (not `<button>` with href)

### Keyboard Navigation
- [ ] Tab order logical
- [ ] Focus visible on interactive elements
- [ ] Skip links present (Phoenix default)
- [ ] No keyboard traps
- [ ] Enter/Space work on custom interactive elements

## Security

### XSS Prevention
- [ ] Auto-escaping enabled (Django default)
- [ ] `|safe` filter used sparingly and only on trusted content
- [ ] `|escape` used when needed
- [ ] User input always escaped in templates
- [ ] JavaScript context escaping: `{{ value|escapejs }}`

### CSRF Protection
- [ ] `{% csrf_token %}` in all POST forms
- [ ] No CSRF token in GET forms
- [ ] HTMX automatically includes CSRF token
- [ ] AJAX requests include CSRF token from meta tag

## Performance

### Template Efficiency
- [ ] No queries in templates (pass data from view)
- [ ] `select_related`/`prefetch_related` used in view
- [ ] Template fragments cached: `{% cache %}`
- [ ] Expensive operations moved to view or context processor
- [ ] No template loops over large datasets

### Asset Loading
- [ ] Critical CSS inline or in head
- [ ] Non-critical CSS with `media="print"` then JS switches to `all`
- [ ] Scripts at end of body or with `async`/`defer`
- [ ] No duplicate asset loading
- [ ] CDN assets for libraries (Bootstrap, icons, etc.)

## Navigation

### Active State
- [ ] Active page highlighted in navigation
- [ ] Use `request.resolver_match.url_name` to check active
- [ ] Template tag handles active state logic
- [ ] No hardcoded active classes

### Breadcrumbs
- [ ] Breadcrumbs auto-generated from URL structure
- [ ] Override breadcrumbs in template block when needed
- [ ] Breadcrumb trail logical and helpful
- [ ] Current page not a link in breadcrumbs

## MathJax Support

### MathJax Configuration
- [ ] MathJax script loaded when needed (not on every page)
- [ ] Configuration: inline `$...$` and display `$$...$$`
- [ ] Re-render after HTMX swaps: `MathJax.typeset()`
- [ ] Content with math wrapped appropriately

## Icons

### Feather Icons (Primary)
- [ ] Icons use `data-feather="icon-name"` attribute
- [ ] `feather.replace()` called after DOM ready
- [ ] Re-initialize after HTMX swaps
- [ ] Icon size controlled with `width` and `height` attributes
- [ ] Accessible label or `aria-hidden="true"` if decorative

### FontAwesome (Secondary)
- [ ] Use for brand icons: Microsoft, GitHub, etc.
- [ ] Class-based: `<i class="fa-brands fa-microsoft"></i>`
- [ ] No conflicts with Feather icons

## Component Patterns

### Cards
- [ ] Use `{% reusable_card %}` tag or Phoenix card classes
- [ ] Card header optional but consistent
- [ ] Card body contains main content
- [ ] Card footer for actions

### Modals
- [ ] Use `{% reusable_modal %}` tag or Bootstrap modal markup
- [ ] Modal ID unique on page
- [ ] Modal title descriptive
- [ ] Accessible (focus trap, ESC to close)
- [ ] HTMX can load modal content dynamically

### Tables
- [ ] Use `{% reusable_table %}` tag or responsive table markup
- [ ] Tables wrapped in `.table-responsive` for horizontal scroll
- [ ] Column headers descriptive
- [ ] Empty state shown when no data
- [ ] Pagination for large datasets

## Error Handling

### Error Templates
- [ ] Custom templates for 400, 403, 404, 500 errors
- [ ] Error message clear and helpful
- [ ] Navigation available (back to home, etc.)
- [ ] No debug info in production error pages
- [ ] Styled consistently with site theme

### User Feedback
- [ ] Django messages framework used: `{% bootstrap_messages %}`
- [ ] Message types: success, info, warning, error
- [ ] Messages dismissible
- [ ] Toast notifications for non-blocking feedback
- [ ] Loading states during AJAX operations

## Testing Considerations

### Template Testing
- [ ] Test templates render without errors
- [ ] Test context data appears correctly
- [ ] Test template tags with various inputs
- [ ] Test accessibility with automated tools
- [ ] Test responsive behavior at different breakpoints

## Common Issues to Check

### Missing Blocks
- [ ] Child template defines all required blocks
- [ ] No undefined blocks referenced

### URL Reversal
- [ ] Use `{% url 'name' %}` not hardcoded paths
- [ ] URL names exist and correct
- [ ] Parameters passed to parameterized URLs

### Template Tag Loading
- [ ] Template tags loaded before use
- [ ] No missing `{% load %}` statements
- [ ] Tags loaded in correct order

### HTMX Targets
- [ ] Target elements exist on page
- [ ] Target IDs unique
- [ ] Swap strategy appropriate for target

### Form Issues
- [ ] CSRF token present
- [ ] Form method correct (GET vs POST)
- [ ] Required fields marked
- [ ] Validation errors displayed

## Cross-Reference

Related docs:
- `htmx_best_practices.md` - HTMX patterns and usage
- `cdn_sri_best_practices.md` - CDN asset loading
- `web_security_best_practices.md` - XSS prevention
- `django_best_practices.md` - General Django patterns
