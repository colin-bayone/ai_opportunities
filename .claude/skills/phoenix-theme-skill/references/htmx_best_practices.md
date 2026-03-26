# HTMX Best Practices

HTMX patterns for dynamic interactions with out-of-band swaps, events, and progressive enhancement.

## HTMX Overview

### What is HTMX
- [ ] Extend HTML with AJAX, WebSockets, and Server-Sent Events
- [ ] Partial page updates without full page reloads
- [ ] Progressive enhancement (works without JavaScript)
- [ ] Minimal client-side JavaScript needed
- [ ] Server-side rendering with dynamic updates

### When to Use HTMX
- [ ] Form submissions with inline validation
- [ ] Dynamic content loading (infinite scroll, lazy loading)
- [ ] Partial page updates (tabs, modals, accordions)
- [ ] Search with live results
- [ ] Progress indicators and status updates
- [ ] Content filtering and sorting

## HTMX Attributes

### Core Attributes

#### hx-get / hx-post / hx-put / hx-delete
```html
<!-- GET request -->
<button hx-get="/api/data" hx-target="#result">Load Data</button>

<!-- POST request -->
<form hx-post="/submit" hx-target="#response">
    <!-- form fields -->
</form>

<!-- DELETE request -->
<button hx-delete="/api/item/123" hx-target="#item-123" hx-swap="outerHTML">
    Delete
</button>
```

#### hx-target
- [ ] Specify element to update with response
- [ ] Use CSS selectors (#id, .class, etc.)
- [ ] Use `this` for the triggering element
- [ ] Use `closest` to find ancestor
- [ ] Use `next` or `previous` for siblings

```html
<!-- Target by ID -->
<button hx-get="/data" hx-target="#content">Load</button>

<!-- Target self -->
<div hx-get="/refresh" hx-target="this">Click to refresh</div>

<!-- Target closest parent -->
<button hx-get="/update" hx-target="closest .card">Update Card</button>
```

#### hx-swap
- [ ] `innerHTML` - Replace inner content (default)
- [ ] `outerHTML` - Replace entire element
- [ ] `beforebegin` - Insert before element
- [ ] `afterbegin` - Insert at start of element
- [ ] `beforeend` - Insert at end of element
- [ ] `afterend` - Insert after element
- [ ] `delete` - Remove element
- [ ] `none` - Don't swap (use for side effects)

```html
<!-- Replace inner HTML -->
<div hx-get="/content" hx-swap="innerHTML"></div>

<!-- Replace entire element -->
<div hx-get="/widget" hx-swap="outerHTML"></div>

<!-- Append to end -->
<div id="list" hx-get="/next-items" hx-swap="beforeend" hx-target="#list">
    Load More
</div>
```

#### hx-trigger
- [ ] `click` - On click (default for buttons)
- [ ] `change` - On input change
- [ ] `keyup` - On key release
- [ ] `submit` - On form submit
- [ ] `load` - On page load
- [ ] `revealed` - When element scrolled into view
- [ ] Custom events

```html
<!-- Trigger on change with delay -->
<input type="search" 
       hx-get="/search" 
       hx-trigger="keyup changed delay:500ms"
       hx-target="#results">

<!-- Trigger on scroll into view -->
<div hx-get="/load-more" 
     hx-trigger="revealed" 
     hx-target="#content" 
     hx-swap="beforeend">
    Loading...
</div>

<!-- Trigger every 5 seconds -->
<div hx-get="/status" 
     hx-trigger="every 5s" 
     hx-target="this">
    Status
</div>
```

### UI Feedback Attributes

#### hx-indicator
```html
<!-- Show spinner during request -->
<button hx-get="/data" hx-indicator="#spinner">
    Load Data
</button>
<div id="spinner" class="htmx-indicator">
    <span class="spinner-border"></span>
</div>
```

#### hx-disabled-elt
```html
<!-- Disable button during request -->
<button hx-post="/submit" 
        hx-disabled-elt="this"
        hx-target="#result">
    Submit
</button>

<!-- Disable multiple elements -->
<form hx-post="/submit" hx-disabled-elt="find button, find input">
    <!-- form fields -->
</form>
```

### Advanced Attributes

#### hx-vals
```html
<!-- Add extra parameters -->
<button hx-post="/action" 
        hx-vals='{"extra": "value"}'>
    Submit
</button>

<!-- Dynamic values with JavaScript -->
<button hx-post="/action" 
        hx-vals='js:{timestamp: Date.now()}'>
    Submit
</button>
```

#### hx-headers
```html
<!-- Add custom headers -->
<div hx-get="/data" 
     hx-headers='{"X-Custom-Header": "value"}'>
</div>
```

#### hx-include
```html
<!-- Include other form fields in request -->
<input name="search" hx-get="/search" hx-include="#filters">
<div id="filters">
    <input name="category">
    <input name="date">
</div>
```

## Out-of-Band (OOB) Swaps

### What are OOB Swaps
- [ ] Update multiple page regions from single response
- [ ] Server returns multiple fragments
- [ ] Each fragment targets different element
- [ ] All swaps happen simultaneously

### OOB Swap Syntax
```html
<!-- In server response -->
<!-- Primary content (goes to hx-target) -->
<div id="main-content">
    Updated main content
</div>

<!-- OOB swaps (go to their own IDs) -->
<div id="notification" hx-swap-oob="true">
    Success message!
</div>

<div id="counter" hx-swap-oob="innerHTML">
    New count: 42
</div>

<div id="old-element" hx-swap-oob="delete">
    <!-- This element will be removed -->
</div>
```

### OOB Swap Patterns

#### Success Messages
```python
# Django view
def submit_form(request):
    # Process form
    success = process_data(request.POST)
    
    # Return main content + success message
    return render(request, 'partials/form_result.html', {
        'result': result,
        'show_success': success
    })
```

```html
<!-- form_result.html -->
<div id="form-result">
    <!-- Main result content -->
    {{ result }}
</div>

{% if show_success %}
<div id="success-message" hx-swap-oob="true" class="alert alert-success">
    Form submitted successfully!
</div>
{% endif %}
```

#### Counter Updates
```html
<!-- Server returns both main content and updated counter -->
<div id="item-list">
    <!-- Updated item list -->
</div>

<div id="item-count" hx-swap-oob="innerHTML">
    Total items: {{ count }}
</div>
```

#### Error Handling
```html
<!-- Server returns error in OOB swap -->
<div id="main-content">
    <!-- Original content (not updated) -->
</div>

<div id="error-container" hx-swap-oob="true" class="alert alert-danger">
    An error occurred: {{ error_message }}
</div>
```

## Django Integration

### URL Patterns
```python
# urls.py
urlpatterns = [
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<int:pk>/update/', views.item_update, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
]
```

### Django Views for HTMX

#### Detecting HTMX Requests
```python
def my_view(request):
    is_htmx = request.headers.get('HX-Request') == 'true'
    
    if is_htmx:
        # Return partial template
        return render(request, 'partials/content.html', context)
    else:
        # Return full page
        return render(request, 'full_page.html', context)
```

#### Form Submission
```python
from django.http import HttpResponse

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            
            # Return new item + success message
            return render(request, 'partials/item.html', {
                'item': item,
                'show_success': True
            })
        else:
            # Return form with errors
            return render(request, 'partials/form.html', {
                'form': form
            })
    
    # GET request
    form = ItemForm()
    return render(request, 'partials/form.html', {'form': form})
```

#### Inline Editing
```python
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Return updated item display (not form)
            return render(request, 'partials/item_display.html', {
                'item': item
            })
        else:
            # Return form with errors
            return render(request, 'partials/item_form.html', {
                'item': item,
                'form': form
            })
    
    # GET request - show edit form
    form = ItemForm(instance=item)
    return render(request, 'partials/item_form.html', {
        'item': item,
        'form': form
    })
```

#### Delete with Confirmation
```python
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'DELETE':
        item.delete()
        # Return empty response (hx-swap="delete" will remove element)
        return HttpResponse(status=200)
    
    # GET request - show confirmation modal
    return render(request, 'partials/delete_confirm.html', {
        'item': item
    })
```

### Template Partials

#### Partial Template Structure
```
templates/
├── base.html
├── items/
│   ├── list.html                  # Full page
│   └── partials/
│       ├── item.html              # Single item display
│       ├── item_form.html         # Edit form
│       ├── item_list.html         # List of items
│       └── delete_confirm.html    # Confirmation modal
```

#### Item Display Partial
```html
<!-- partials/item.html -->
<div id="item-{{ item.id }}" class="card mb-2">
    <div class="card-body">
        <h5>{{ item.title }}</h5>
        <p>{{ item.description }}</p>
        
        <button hx-get="{% url 'item_update' item.id %}"
                hx-target="#item-{{ item.id }}"
                hx-swap="outerHTML"
                class="btn btn-sm btn-primary">
            Edit
        </button>
        
        <button hx-delete="{% url 'item_delete' item.id %}"
                hx-target="#item-{{ item.id }}"
                hx-swap="outerHTML"
                hx-confirm="Are you sure?"
                class="btn btn-sm btn-danger">
            Delete
        </button>
    </div>
</div>

{% if show_success %}
<div id="success-message" hx-swap-oob="true" class="alert alert-success">
    Item saved successfully!
</div>
{% endif %}
```

#### Form Partial
```html
<!-- partials/item_form.html -->
<div id="item-{{ item.id }}" class="card mb-2">
    <div class="card-body">
        <form hx-post="{% url 'item_update' item.id %}"
              hx-target="#item-{{ item.id }}"
              hx-swap="outerHTML">
            {% csrf_token %}
            
            {{ form.as_p }}
            
            <button type="submit" class="btn btn-primary">
                Save
            </button>
            <button type="button"
                    hx-get="{% url 'item_detail' item.id %}"
                    hx-target="#item-{{ item.id }}"
                    hx-swap="outerHTML"
                    class="btn btn-secondary">
                Cancel
            </button>
        </form>
    </div>
</div>
```

## CSRF Protection

### Including CSRF Token
```html
<!-- In all POST/PUT/DELETE requests -->
<form hx-post="/submit">
    {% csrf_token %}
    <!-- form fields -->
</form>

<!-- Or in meta tag for JavaScript access -->
<meta name="csrf-token" content="{{ csrf_token }}">
```

### JavaScript CSRF Configuration
```javascript
// Set CSRF token for all HTMX requests
document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = getCookie('csrftoken');
});

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
```

## HTMX Events

### Listening to HTMX Events
```javascript
// After content swapped
document.body.addEventListener('htmx:afterSwap', (event) => {
    // Re-initialize plugins
    feather.replace();  // Feather icons
    
    // Initialize MathJax
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
});

// Before request
document.body.addEventListener('htmx:beforeRequest', (event) => {
    console.log('Making request to:', event.detail.pathInfo.requestPath);
});

// After request
document.body.addEventListener('htmx:afterRequest', (event) => {
    if (event.detail.successful) {
        console.log('Request succeeded');
    } else {
        console.error('Request failed');
    }
});
```

### Custom Events
```javascript
// Trigger custom event
document.body.addEventListener('itemUpdated', (event) => {
    console.log('Item updated:', event.detail);
    // Refresh related content
});

// Server can trigger client-side events via HX-Trigger header
```

### Server-Triggered Events
```python
# Django view
from django.http import HttpResponse

def item_update(request, pk):
    # Update item
    item.save()
    
    # Trigger client-side event
    response = render(request, 'partials/item.html', {'item': item})
    response['HX-Trigger'] = 'itemUpdated'
    return response
```

```javascript
// Client-side event listener
document.body.addEventListener('itemUpdated', () => {
    // Refresh item list
    htmx.trigger('#item-list', 'refresh');
});
```

## Common Patterns

### Infinite Scroll
```html
<div id="items">
    {% for item in items %}
        {% include 'partials/item.html' %}
    {% endfor %}
</div>

{% if has_more %}
<div hx-get="{% url 'items' %}?page={{ next_page }}"
     hx-trigger="revealed"
     hx-swap="afterend"
     hx-target="this">
    <div class="text-center">
        <div class="spinner-border"></div>
    </div>
</div>
{% endif %}
```

### Live Search
```html
<input type="search"
       name="q"
       hx-get="{% url 'search' %}"
       hx-trigger="keyup changed delay:500ms"
       hx-target="#search-results"
       placeholder="Search...">

<div id="search-results">
    <!-- Results appear here -->
</div>
```

### Tabs
```html
<ul class="nav nav-tabs">
    <li class="nav-item">
        <a class="nav-link active"
           hx-get="{% url 'tab_content' tab='overview' %}"
           hx-target="#tab-content">
            Overview
        </a>
    </li>
    <li class="nav-item">
        <a class="nav-link"
           hx-get="{% url 'tab_content' tab='details' %}"
           hx-target="#tab-content">
            Details
        </a>
    </li>
</ul>

<div id="tab-content">
    <!-- Tab content loads here -->
</div>
```

### Modal Loading
```html
<!-- Trigger modal -->
<button hx-get="{% url 'item_details' item.id %}"
        hx-target="#modal-content"
        data-bs-toggle="modal"
        data-bs-target="#detailModal">
    View Details
</button>

<!-- Modal structure -->
<div class="modal" id="detailModal">
    <div class="modal-dialog">
        <div class="modal-content" id="modal-content">
            <!-- Content loads here -->
        </div>
    </div>
</div>
```

### Progress Indicator
```html
<!-- Progress bar that updates via polling -->
<div id="progress-container">
    <div class="progress">
        <div class="progress-bar"
             role="progressbar"
             style="width: {{ progress }}%"
             hx-get="{% url 'task_progress' task_id %}"
             hx-trigger="every 1s"
             hx-target="closest #progress-container"
             hx-swap="outerHTML">
            {{ progress }}%
        </div>
    </div>
</div>
```

### Dependent Dropdowns
```html
<select name="category"
        hx-get="{% url 'subcategories' %}"
        hx-target="#subcategory-select"
        hx-include="[name='category']">
    <option value="">Select category</option>
    {% for cat in categories %}
        <option value="{{ cat.id }}">{{ cat.name }}</option>
    {% endfor %}
</select>

<div id="subcategory-select">
    <!-- Subcategories load here -->
</div>
```

## Performance Optimization

### Request Debouncing
```html
<!-- Wait 500ms after user stops typing -->
<input hx-get="/search" 
       hx-trigger="keyup changed delay:500ms">
```

### Partial Updates Only
- [ ] Return only HTML that changed
- [ ] Use OOB swaps for multiple regions
- [ ] Avoid returning entire page
- [ ] Target specific elements

### Caching
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 5)  # 5 minutes
def partial_view(request):
    # Expensive operation
    return render(request, 'partial.html', context)
```

### Lazy Loading
```html
<!-- Load content when scrolled into view -->
<div hx-get="/lazy-content"
     hx-trigger="revealed"
     hx-swap="outerHTML">
    Loading...
</div>
```

## Error Handling

### Client-Side Error Handling
```javascript
document.body.addEventListener('htmx:responseError', (event) => {
    console.error('Request failed:', event.detail.xhr.status);
    
    // Show error message
    showError('Something went wrong. Please try again.');
});

document.body.addEventListener('htmx:sendError', (event) => {
    console.error('Network error');
    showError('Network error. Please check your connection.');
});
```

### Server-Side Error Responses
```python
def my_view(request):
    try:
        # Process request
        result = process_data(request.POST)
        return render(request, 'partials/success.html', {'result': result})
    except Exception as e:
        # Return error partial
        return render(request, 'partials/error.html', {
            'error': str(e)
        }, status=400)
```

```html
<!-- partials/error.html -->
<div id="error-container" hx-swap-oob="true" class="alert alert-danger">
    <strong>Error:</strong> {{ error }}
</div>
```

## Testing

### Testing HTMX Views
```python
from django.test import TestCase, Client

class HTMXViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_htmx_request(self):
        # Simulate HTMX request
        response = self.client.get(
            '/items/',
            HTTP_HX_REQUEST='true'
        )
        
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/items.html')
    
    def test_non_htmx_request(self):
        # Regular request
        response = self.client.get('/items/')
        
        # Check full page rendered
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/list.html')
```

## Best Practices

### Progressive Enhancement
- [ ] Pages work without JavaScript
- [ ] HTMX enhances existing functionality
- [ ] Fallback for disabled JavaScript
- [ ] Forms submit normally without HTMX

### Accessibility
- [ ] ARIA live regions for dynamic updates
- [ ] Focus management after swaps
- [ ] Keyboard navigation works
- [ ] Screen reader announcements

```html
<!-- ARIA live region -->
<div id="status" aria-live="polite" aria-atomic="true">
    <!-- Status updates announced to screen readers -->
</div>
```

### SEO Considerations
- [ ] Important content in initial HTML
- [ ] Progressive enhancement for dynamic content
- [ ] Use proper semantic HTML
- [ ] Server-side rendering for crawlers

### Security
- [ ] CSRF protection on all POST/PUT/DELETE
- [ ] Validate user permissions server-side
- [ ] Sanitize user input
- [ ] No sensitive data in HTML attributes

## Troubleshooting

### HTMX Not Working
- Check browser console for errors
- Verify HTMX library loaded
- Check network tab for requests
- Verify CSRF token included

### Content Not Updating
- Check `hx-target` selector is correct
- Verify response HTML structure
- Check `hx-swap` mode appropriate
- Review server response in network tab

### OOB Swaps Not Working
- Verify `hx-swap-oob="true"` attribute
- Check target element IDs match
- Ensure elements exist in DOM
- Review server response HTML

## Cross-Reference

Related docs:
- `django_templates_best_practices.md` - Template structure
- `channels_websockets_best_practices.md` - Real-time updates
- `web_security_best_practices.md` - CSRF protection
- `django_best_practices.md` - View patterns
