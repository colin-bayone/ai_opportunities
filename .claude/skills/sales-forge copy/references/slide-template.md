# Slide Template Guide

Structure and patterns for generating BayOne slide decks.

## Key Concept: Two Rendering Modes

### HTML View (Browser)
- Decorative container with gradient background
- Centered slide with border/shadow
- Navigation-friendly

### PDF View (Export)
- Full-bleed, no decorative container
- Slide content fills the page
- Print-optimized

## Slide Types

### 1. Cover Slide

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Deck Title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .cover {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px;
      background: linear-gradient(135deg, #2e1065 0%, #4c1d95 50%, #6d28d9 100%);
      color: #fff;
      position: relative;
      overflow: hidden;
    }

    /* Glow effects - same as proposal */
    .cover::before { /* diagonal glow */ }
    .cover::after { /* radial glow */ }

    .cover-content { position: relative; z-index: 1; max-width: 800px; }
    .cover-label { /* same as proposal */ }
    .cover h1 { font-size: 56px; /* ... */ }
    .cover-subtitle { /* ... */ }
    .cover-meta { /* ... */ }
    .logo { /* bottom right */ }

    @media print {
      @page { size: 11in 8.5in; margin: 0; }  /* Landscape */
      .cover {
        min-height: 0;
        height: 8.5in;
        width: 11in;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
    }
  </style>
</head>
<body>
  <div class="cover">
    <!-- Same structure as proposal cover -->
  </div>
</body>
</html>
```

### 2. Content Slide

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Same head setup -->
  <style>
    .slide {
      min-height: 100vh;
      padding: 60px 80px;
      display: flex;
      flex-direction: column;
    }

    .slide-header {
      margin-bottom: 40px;
    }

    .slide-number {
      font-size: 12px;
      font-weight: 600;
      color: #a855f7;
      letter-spacing: 2px;
      margin-bottom: 12px;
    }

    .slide h1 {
      font-size: 36px;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.5px;
    }

    .slide-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }

    .slide-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 20px;
      border-top: 1px solid #e2e8f0;
      font-size: 12px;
      color: #64748b;
    }

    .slide-footer .logo {
      font-weight: 700;
      color: #0f172a;
    }
    .slide-footer .logo span { color: #a855f7; }

    @media print {
      @page { size: 11in 8.5in; margin: 0; }
      .slide {
        min-height: 0;
        height: 8.5in;
        width: 11in;
        padding: 40px 60px;
      }
    }
  </style>
</head>
<body>
  <div class="slide">
    <div class="slide-header">
      <div class="slide-number">02</div>
      <h1>{Slide Title}</h1>
    </div>

    <div class="slide-content">
      <!-- Slide-specific content -->
    </div>

    <div class="slide-footer">
      <span class="logo">Bay<span>One</span> Solutions</span>
      <span>Confidential</span>
    </div>
  </div>
</body>
</html>
```

### 3. Stats Slide

```html
<div class="slide-content">
  <div class="stat-grid-4">
    <div class="stat-card-large">
      <div class="stat-value">6,000</div>
      <div class="stat-label">Reports to Migrate</div>
    </div>
    <!-- More stats -->
  </div>
</div>
```

### 4. Two-Column Slide

```html
<div class="slide-content">
  <div class="two-col">
    <div class="col">
      <h3>{Left Title}</h3>
      <p>{Content}</p>
    </div>
    <div class="col">
      <h3>{Right Title}</h3>
      <p>{Content}</p>
    </div>
  </div>
</div>
```

### 5. Quote/Highlight Slide

```html
<div class="slide-content">
  <div class="quote-block">
    <p class="quote">"{Important quote from the client}"</p>
    <p class="attribution">- {Name}, {Title}</p>
  </div>
</div>
```

## File Organization

```
deliverables/slides/
├── 01_cover.html
├── 02_the_challenge.html
├── 03_key_stats.html
├── 04_our_approach.html
├── 05_capabilities.html
├── 06_engagement_phases.html
├── 07_why_bayone.html
├── 08_next_steps.html
└── logos/              # Client/tech logos if needed
```

## Slide Deck Conventions

- **One HTML = One Slide**
- **Landscape orientation** for presentation
- **Numbered filenames** for order
- **Consistent header/footer** across slides
- **Minimal text** - slides are visual, not documents

## Common Slide Types by Purpose

| Type | When to Use |
|------|-------------|
| Cover | Opening slide with title |
| Stats | Key numbers that grab attention |
| Problem | Frame the challenge |
| Approach | High-level methodology |
| Capabilities | What we do (table or icons) |
| Phases | Engagement timeline (cards) |
| Team | Key people (if relevant) |
| Clients | Logo wall (credibility) |
| Why Us | Differentiators |
| Next Steps | Call to action |
