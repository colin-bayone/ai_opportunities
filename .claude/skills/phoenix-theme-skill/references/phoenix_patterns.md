# Phoenix Theme Patterns Reference

This is shared reference material for the Phoenix theme skill and its sub-agents.
All agents should reference this file for common patterns, anti-patterns, and troubleshooting.

## Phoenix Theme Quick Reference

**Version Lock:** v1.23.0
**Base URL:** https://prium.github.io/phoenix/v1.23.0/

### CRITICAL: Font Awesome Version

**Phoenix v1.23.0 uses Font Awesome 5, NOT Font Awesome 6.**

This affects icon class names. Common mistakes:

| FA6 (WRONG) | FA5 (CORRECT) |
|-------------|---------------|
| `fa-arrow-rotate-right` | `fa-redo` |
| `fa-box-archive` | `fa-archive` |
| `fa-trash-can` | `fa-trash` |
| `fa-pen-to-square` | `fa-edit` |
| `fa-floppy-disk` | `fa-save` |
| `fa-circle-xmark` | `fa-times-circle` |
| `fa-circle-check` | `fa-check-circle` |
| `fa-rotate` | `fa-sync` |

**Always verify icon names against FA5 documentation, not FA6.**

**Key Starting Points:**

| URL | Purpose |
|-----|---------|
| https://prium.github.io/phoenix/v1.23.0/widgets.html | Single most helpful - various widgets and UI elements |
| https://prium.github.io/phoenix/v1.23.0/modules/echarts/ | Apache ECharts (built into theme) |
| https://prium.github.io/phoenix/v1.23.0/modules/components/ | UI Components |
| https://prium.github.io/phoenix/v1.23.0/modules/forms/ | Form Components |
| https://prium.github.io/phoenix/v1.23.0/modules/tables/ | Table Components |

## Common Patterns

### Dashboard Layout

```html
{% extends "phoenix/layouts/dashboard.html" %}

{% block content %}
<div class="row g-3 mb-3">
  <!-- Stat Cards -->
  {% for stat in stats %}
  <div class="col-md-6 col-xl-3">
    {% include "components/stat_card.html" with stat=stat %}
  </div>
  {% endfor %}
</div>

<div class="row g-3">
  <!-- Main Chart -->
  <div class="col-xl-8">
    <div class="card h-100"
         hx-get="{% url 'dashboard_chart' %}"
         hx-trigger="load"
         hx-swap="innerHTML">
      <div class="card-body">Loading chart...</div>
    </div>
  </div>

  <!-- Activity Feed -->
  <div class="col-xl-4">
    {% include "components/activity_feed.html" %}
  </div>
</div>
{% endblock %}
```

### Card Component

```html
<div class="card mb-3">
  <div class="card-header bg-body-tertiary d-flex justify-content-between align-items-center">
    <h6 class="mb-0">{{ title }}</h6>
    <a href="{{ detail_url }}" class="btn btn-link btn-sm">View All</a>
  </div>
  <div class="card-body">
    {{ content }}
  </div>
</div>
```

### Card with Progress

```html
{% comment %}
Phoenix Theme: Card with Progress
Reference: https://prium.github.io/phoenix/v1.23.0/modules/components/card.html
{% endcomment %}

<div class="card mb-3" id="project-progress-card">
  <div class="card-header">
    <h6 class="mb-0">{{ title|default:"Project Progress" }}</h6>
  </div>
  <div class="card-body"
       hx-get="{% url 'project_progress' project.id %}"
       hx-trigger="load, every 30s"
       hx-swap="innerHTML">
    {% include "components/progress_bars.html" %}
  </div>
</div>
```

### Table with HTMX Sorting/Filtering

```html
<div id="table-container">
  <table class="table table-hover">
    <thead>
      <tr>
        <th hx-get="{% url 'table_data' %}?sort=name"
            hx-target="#table-body"
            hx-swap="innerHTML"
            class="cursor-pointer">
          Name <span class="sort-indicator"></span>
        </th>
        <!-- More headers -->
      </tr>
    </thead>
    <tbody id="table-body"
           hx-get="{% url 'table_data' %}"
           hx-trigger="load"
           hx-swap="innerHTML">
      <!-- Loaded via HTMX -->
    </tbody>
  </table>
</div>
```

### Stat Card

```html
<div class="card h-100">
  <div class="card-body">
    <div class="d-flex justify-content-between">
      <div>
        <h6 class="text-body-tertiary mb-2">{{ stat_label }}</h6>
        <h3 class="mb-0">{{ stat_value }}</h3>
      </div>
      <div class="bg-{{ stat_color|default:'primary' }}-subtle rounded-circle d-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">
        <i class="fas fa-{{ stat_icon }} text-{{ stat_color|default:'primary' }}"></i>
      </div>
    </div>
    {% if show_trend %}
    <p class="mb-0 mt-3">
      <span class="badge bg-{{ trend_color }}-subtle text-{{ trend_color }}">
        <i class="fas fa-caret-{{ trend_direction }}"></i> {{ trend_value }}
      </span>
      <span class="text-body-tertiary ms-2">{{ trend_label }}</span>
    </p>
    {% endif %}
  </div>
</div>
```

### HTMX Loading Pattern

```html
<div id="{{ container_id }}"
     hx-get="{% url 'partial_view_name' %}"
     hx-trigger="load, every 30s"
     hx-swap="innerHTML">
  <div class="text-center py-4">
    <div class="spinner-border text-primary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>
</div>
```

### OOB Swap Pattern (update multiple elements)

```html
{# Main response #}
<div id="main-content">
  Updated main content
</div>

{# OOB updates - these swap into their targets regardless of hx-target #}
<div id="notification-count" hx-swap-oob="true">
  <span class="badge bg-danger">{{ new_count }}</span>
</div>

<div id="last-updated" hx-swap-oob="true">
  Updated: {{ now|date:"H:i" }}
</div>
```

## Anti-Patterns to Avoid

### DO NOT:

1. **Create custom components** - Always find the Phoenix equivalent
2. **Use Ajax/fetch** - Use HTMX instead
3. **Write custom CSS for layout** - Use Bootstrap utilities from Phoenix
4. **Build custom JavaScript widgets** - Find Phoenix/Bootstrap equivalent
5. **Deviate from Phoenix color scheme** - Use theme variables
6. **Create custom form controls** - Use Phoenix form components
7. **Build custom modals** - Use Bootstrap modal from Phoenix

### Bad Examples:

```html
{# BAD: Custom JavaScript #}
<script>
  fetch('/api/data').then(...)  {# NEVER DO THIS #}
</script>

{# GOOD: HTMX #}
<div hx-get="{% url 'data' %}" hx-trigger="load">Loading...</div>
```

```html
{# BAD: Inline styles for layout #}
<div style="display: flex; gap: 20px;">

{# GOOD: Bootstrap classes #}
<div class="d-flex gap-3">
```

```html
{# BAD: Custom component class #}
<div class="my-custom-card">

{# GOOD: Phoenix card #}
<div class="card">
```

### If Something "Doesn't Exist" in Phoenix:

1. Check the widgets page thoroughly: https://prium.github.io/phoenix/v1.23.0/widgets.html
2. Search the catalog for similar components
3. Consider combining multiple Phoenix components
4. Ask user to reconsider the requirement to fit Phoenix

**Never say "Phoenix doesn't have this, let me create it custom."**

## Django Template Requirements

### CRITICAL: Never Use Hash-Bang Placeholder Links

When generating Django templates, **always use real Django URLs**, not `#` placeholders.

```html
{# BAD: Placeholder links #}
<a href="#">Drafts</a>
<a href="#">Spam</a>
<a href="#">Trash</a>

{# GOOD: Real Django URLs #}
<a href="{% url 'communications:drafts' %}">Drafts</a>
<a href="{% url 'communications:spam' %}">Spam</a>
<a href="{% url 'communications:trash' %}">Trash</a>
```

If a URL route doesn't exist yet, either:
1. Create the URL pattern in urls.py
2. Use a reasonable placeholder that indicates the intended route: `{% comment %}TODO: Create drafts view{% endcomment %}`
3. Ask the user which URL pattern to use

**Never assume `#` is acceptable** - it creates broken navigation.

### Email/List Item Links Must Go to Detail Views

When creating list pages (email inbox, candidate list, etc.), ensure clickable items link to their detail pages:

```html
{# BAD: Links back to the same list page #}
<a href="{% url 'communications:inbox' %}">{{ email.subject }}</a>

{# GOOD: Links to detail page with ID #}
<a href="{% url 'communications:email_detail' pk=email.id %}">{{ email.subject }}</a>
```

### Static Asset Paths

In this project, Phoenix assets use the `phoenix/` prefix:

```html
{# Project convention #}
{% static 'phoenix/assets/img/team/60.webp' %}
```

Verify the project's static file structure before using asset paths.

## Accessibility Requirements

### MANDATORY: Alt Text on Images

Every `<img>` tag MUST have meaningful alt text:

```html
{# BAD: Empty alt text #}
<img src="{% static 'phoenix/assets/img/team/60.webp' %}" alt="" />

{# GOOD: Descriptive alt text #}
<img src="{% static 'phoenix/assets/img/team/60.webp' %}" alt="Jessica Ball" />
```

For avatars, use the person's name. For decorative images only, use `alt=""` with `role="presentation"`.

### Icon-Only Buttons Need aria-label

```html
{# BAD: No accessibility label #}
<button class="btn p-0"><span class="fas fa-archive"></span></button>

{# GOOD: Screen reader accessible #}
<button class="btn p-0" aria-label="Archive email">
    <span class="fas fa-archive"></span>
</button>
```

### Avatar Initials Must Match Name

When using initials-based avatars, the initial must match the person's name:

```html
{# BAD: Wrong initial for "Max Williamson" #}
<div class="avatar-name rounded-circle"><span>R</span></div>

{# GOOD: Correct initial #}
<div class="avatar-name rounded-circle"><span>M</span></div>
```

## Template Generator Output Guidelines

When generating Django templates:

1. **Be concise** - Avoid excessive comments; document non-obvious patterns only
2. **Use real URLs** - Never use `#` placeholders
3. **Include accessibility** - Alt text, aria-labels, proper semantic HTML
4. **Match Phoenix exactly** - Copy class names precisely from the reference
5. **Verify FA version** - Double-check icon names against FA5
6. **Test links** - Ensure all links go to appropriate destination pages

## Mockup-to-Phoenix Mapping

Common visual elements and their Phoenix equivalents:

| Mockup Element | Phoenix Component | Reference |
|----------------|-------------------|-----------|
| Sidebar nav | Navbar Vertical | modules/components/navbar-vertical.html |
| Top navigation | Navbar Top | modules/components/navbar-top.html |
| Metrics/stats cards | Stat Widgets | widgets.html |
| Data table | Advanced Tables | modules/tables/advance-tables.html |
| Line/bar/pie chart | ECharts | modules/echarts/*.html |
| Form inputs | Form Controls | modules/forms/basic/*.html |
| Date picker | Advanced Forms | modules/forms/advance/date-picker.html |
| Modal dialog | Modal | modules/components/modal.html |
| Dropdown menu | Dropdown | modules/components/dropdowns.html |
| Tabs | Nav Tabs | modules/components/navs-and-tabs.html |
| Alerts/notifications | Alerts | modules/components/alerts.html |
| Progress indicators | Progress | modules/components/progress-bar.html |
| Badges/labels | Badges | modules/components/badges.html |
| Buttons | Buttons | modules/components/buttons.html |
| Cards | Cards | modules/components/card.html |

## Page Structure Recommendation

For a typical dashboard:

```
├── base.html (Phoenix base template)
│   ├── navbar-vertical (sidebar)
│   ├── navbar-top (header)
│   └── main content area
│       ├── Row 1: Stat cards (col-md-6 col-xl-3 × 4)
│       ├── Row 2: Chart (col-xl-8) + Activity (col-xl-4)
│       └── Row 3: Data table (full width)
```

## Troubleshooting

### Can't Find Component

1. Search by multiple terms: `catalog.search_tags('button', 'action', 'primary')`
2. Check the widgets page (most comprehensive)
3. Look in related categories (buttons might be in components OR forms)
4. Check subcategories: `catalog.list_subcategories('components')`

### HTMX Integration Issues

Reference `htmx_best_practices.md` for:
- Proper trigger patterns
- Target selection
- OOB swap usage
- Integration with Django views

### Layout Problems

1. Start from Phoenix dashboard template
2. Use Bootstrap grid system (row/col classes)
3. Reference existing layouts in apps category
4. Check utilities for spacing (margins, padding)

## Regenerating the Catalog

If the Phoenix theme is updated or catalog needs refresh:

```bash
# Crawl the site and generate new catalog
poetry run python claude/2025-12-16_phoenix-theme-skill/scripts/01_crawl_phoenix_site.py

# Generate markdown summaries
poetry run python claude/2025-12-16_phoenix-theme-skill/scripts/03_generate_markdown_summaries.py
```

## Catalog Query Examples

```python
from scripts.query_catalog import PhoenixCatalog
catalog = PhoenixCatalog()

# Search by category
charts = catalog.by_category('charts')
forms = catalog.by_category('forms')

# Search by tags
tables = catalog.search_tags('table', 'data', 'grid')

# Search by text across title, description, components
results = catalog.search_text('progress bar')

# Get specific page
page = catalog.get_page_by_path('modules/components/progress-bar.html')
```

## Verifying Work with Screenshots

### IMPORTANT: Use Authenticated Screenshots

When verifying UI work, **always use authenticated screenshots** because most pages require login. Unauthenticated screenshots will just show the login page.

The screenshot tool supports dev auth bypass (Issue #815) for local development:

```bash
# Screenshot an authenticated page (RECOMMENDED)
poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py \
    --url http://localhost:8000/candidates/search/ \
    --email cmoore@bayone.com \
    /tmp/screenshot.png

# Screenshot with full page capture
poetry run python .claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py \
    --url http://localhost:8000/home/ \
    --email user@bayone.com \
    --full-page
```

### Requirements for Authenticated Screenshots

1. **Local dev server running**: `poetry run python run.py local`
2. **DEV_AUTH_ENABLED=True** in `.env.local`
3. **Valid user email** that exists in the database

### When to Use Unauthenticated Screenshots

Use unauthenticated screenshots only for:
- Static HTML demo files (not served by Django)
- Public pages that don't require login
- Testing that login/authentication works correctly

### Screenshot Tool Reference

Location: `.claude/skills/phoenix-theme-skill/scripts/05_screenshot_html.py`

See `docs/authentication.md` (Issue #815 section) for full documentation on the dev auth system.
