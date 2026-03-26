# Help Center Architecture Reference

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         CONTENT FLOW                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Claude/AI ──writes──▶ Azure Blob Storage ◀──reads── Django App   │
│                         (docs container)              (viewer)      │
│                                                          │          │
│                                                          ▼          │
│                                                    Redis Cache      │
│                                                          │          │
│                                                          ▼          │
│                                                    Phoenix Theme    │
│                                                    (beautiful UI)   │
│                                                          │          │
│                                                          ▼          │
│                                                       Users         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Django App Structure

```
help_center/
├── __init__.py
├── apps.py
├── urls.py
├── views.py
├── services/
│   ├── __init__.py
│   ├── blob_reader.py       # Read markdown from Azure Blob
│   ├── markdown_renderer.py # Convert markdown to HTML
│   └── navigation.py        # Parse _nav.yaml, build nav
├── templates/
│   └── help_center/
│       ├── base.html        # Help center layout
│       ├── index.html       # Help center home
│       ├── article.html     # Single article view
│       └── components/
│           ├── header.html
│           ├── sidebar.html
│           ├── breadcrumb.html
│           └── toc.html
└── tests/
    └── ...
```

## Approved Libraries

| Library | Version | Purpose |
|---------|---------|---------|
| `markdown` | >= 3.10.0 | Markdown → HTML rendering |
| `pygments` | >= 2.19.2 | Code syntax highlighting |
| `django-storages[azure]` | 1.14.0 | Already installed |
| `azure-storage-blob` | 12.26.0 | Already installed |
| `pyyaml` | (check version) | Parse _nav.yaml |

## Blob Storage Structure

Container: `docs`

```
docs/
├── _nav.yaml                    # Navigation structure (AI-maintained)
├── index.md                     # Home page content
├── getting-started/
│   ├── index.md
│   ├── welcome.md
│   ├── first-day.md
│   └── quick-start.md
├── candidates/
│   ├── index.md
│   ├── search-basics.md
│   ├── filters.md
│   ├── saved-searches.md
│   └── profiles.md
├── jobs/
│   ├── index.md
│   ├── creating.md
│   ├── dashboard.md
│   └── matching.md
├── communication/
│   ├── index.md
│   ├── templates.md
│   ├── sending.md
│   └── history.md
├── calendar/
│   ├── index.md
│   ├── overview.md
│   └── scheduling.md
├── analytics/
│   ├── index.md
│   ├── dashboard.md
│   └── reports.md
├── tips/
│   ├── index.md
│   ├── sourcing.md
│   ├── shortcuts.md
│   └── power-user.md
└── faq/
    ├── index.md
    ├── common.md
    └── troubleshooting.md
```

## Service Implementations

### HelpCenterBlobReader

```python
from azure.storage.blob import BlobServiceClient
from django.conf import settings
from django.core.cache import cache
import yaml

class HelpCenterBlobReader:
    CONTAINER_NAME = "docs"
    CACHE_TTL = 300  # 5 minutes

    def __init__(self):
        self.client = BlobServiceClient(
            account_url=f"https://{settings.AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net",
            credential=settings.AZURE_STORAGE_ACCOUNT_KEY
        )
        self.container = self.client.get_container_client(self.CONTAINER_NAME)

    def get_navigation(self) -> dict:
        """Get navigation structure from _nav.yaml."""
        cache_key = "help_center:nav"
        nav = cache.get(cache_key)
        if nav is None:
            content = self._read_blob("_nav.yaml")
            nav = yaml.safe_load(content) if content else {'navigation': []}
            cache.set(cache_key, nav, self.CACHE_TTL)
        return nav

    def get_article(self, slug: str) -> str | None:
        """Get markdown content for an article."""
        cache_key = f"help_center:article:{slug}"
        content = cache.get(cache_key)
        if content is None:
            # Try slug.md first, then slug/index.md
            content = self._read_blob(f"{slug}.md")
            if not content:
                content = self._read_blob(f"{slug}/index.md")
            if content:
                cache.set(cache_key, content, self.CACHE_TTL)
        return content

    def _read_blob(self, path: str) -> str | None:
        try:
            blob = self.container.get_blob_client(path)
            return blob.download_blob().readall().decode('utf-8')
        except Exception as e:
            # Log error for debugging
            return None
```

### MarkdownRenderer

```python
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

class MarkdownRenderer:
    def __init__(self):
        self.md = markdown.Markdown(
            extensions=[
                'tables',
                'fenced_code',
                TocExtension(
                    permalink=True,
                    permalink_class='anchor-link',
                    toc_depth=3,
                ),
                CodeHiliteExtension(
                    css_class='highlight',
                    guess_lang=False,
                ),
                'sane_lists',
            ],
            output_format='html5'
        )

    def render(self, content: str) -> dict:
        self.md.reset()  # Reset state for reuse
        html = self.md.convert(content)
        toc = getattr(self.md, 'toc', '')
        return {
            'html': html,
            'toc': toc,
        }
```

### Navigation Service

```python
def get_navigation_context(nav_data: dict, current_slug: str = None) -> dict:
    """Process navigation data, marking active items."""
    navigation = nav_data.get('navigation', [])
    for section in navigation:
        section['active'] = False
        for child in section.get('children', []):
            child['active'] = child.get('slug') == current_slug
            if child['active']:
                section['active'] = True
    return {'navigation': navigation}

def build_breadcrumbs(nav_data: dict, slug: str) -> list:
    """Build breadcrumb trail for given slug."""
    breadcrumbs = []
    parts = slug.split('/')

    for section in nav_data.get('navigation', []):
        if slug.startswith(section.get('slug', '')):
            breadcrumbs.append({
                'title': section['title'],
                'slug': section['slug']
            })
            for child in section.get('children', []):
                if child.get('slug') == slug:
                    breadcrumbs.append({
                        'title': child['title'],
                        'slug': child['slug']
                    })
                    break
            break

    return breadcrumbs
```

## Views

```python
from django.shortcuts import render
from django.http import Http404
from .services.blob_reader import HelpCenterBlobReader
from .services.markdown_renderer import MarkdownRenderer
from .services.navigation import get_navigation_context, build_breadcrumbs

blob_reader = HelpCenterBlobReader()
renderer = MarkdownRenderer()

def index(request):
    """Help center home page."""
    nav = blob_reader.get_navigation()
    content = blob_reader.get_article("index")
    rendered = renderer.render(content) if content else {'html': '', 'toc': ''}

    return render(request, 'help_center/index.html', {
        **get_navigation_context(nav),
        'content': rendered['html'],
    })

def article(request, slug):
    """Display a single help article."""
    nav = blob_reader.get_navigation()
    content = blob_reader.get_article(slug)

    if not content:
        raise Http404("Article not found")

    rendered = renderer.render(content)

    return render(request, 'help_center/article.html', {
        **get_navigation_context(nav, slug),
        'content': rendered['html'],
        'toc': rendered['toc'],
        'slug': slug,
        'breadcrumbs': build_breadcrumbs(nav, slug),
    })
```

## Caching Strategy

| Item | Cache Key | TTL | Invalidation |
|------|-----------|-----|--------------|
| Navigation | `help_center:nav` | 5 min | Manual or on sync |
| Article content | `help_center:article:{slug}` | 5 min | Manual or on sync |

For production, consider 15-30 min TTLs since docs change infrequently.

## Template CSS Variables

```css
:root {
    --docs-sidebar-width: 280px;
    --docs-toc-width: 220px;
    --docs-content-max-width: 800px;
    --docs-header-height: 56px;
}
```

## TalentAI Branding

```css
/* Purple-to-pink gradient */
.docs-brand-name .text-accent {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.btn-bayone {
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
    color: #ffffff;
    border: none;
    box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
}

/* Gradient accents throughout */
/* - Category card icons */
/* - TOC active indicator */
/* - Callout tip borders */
/* - Search focus state */
```
