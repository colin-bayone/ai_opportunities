# BayOne Document Design System
## Design Specifications for Professional HTML Documents

---

## Overview

This design system defines the visual language for BayOne's client-facing documents. The aesthetic is inspired by Big Four consulting deliverables: clean, modern, confident, and polished. Documents should feel premium without being flashy.

**Core Principles:**
- Clean over cluttered
- Confident use of whitespace
- Subtle gradients, not overwhelming
- Professional typography with clear hierarchy
- Consistency across all components
- Print-friendly by design

---

## Brand Colors

### Primary Palette

```css
:root {
  /* Core purples - primary brand identity */
  --purple-darkest: #2e1065;    /* Deep purple - cover backgrounds, summary tables */
  --purple-dark: #4c1d95;       /* Rich purple - gradient midpoint */
  --purple-mid: #5b21b6;        /* Solid purple - table headers, badges */
  --purple-bright: #6d28d9;     /* Vibrant purple - gradient endpoint */
  --purple-accent: #a855f7;     /* Light purple - section numbers, accents */
  --purple-glow: #e879f9;       /* Magenta/pink - cover label, logo accent */
  
  /* Neutrals */
  --primary: #0f172a;           /* Near-black - headings, strong text */
  --text: #334155;              /* Dark gray - body text */
  --text-light: #64748b;        /* Medium gray - secondary text, labels */
  --border: #e2e8f0;            /* Light gray - borders, dividers */
  --bg-subtle: #f8fafc;         /* Off-white - alternating rows, subtle backgrounds */
  --white: #ffffff;
}
```

### Gradient Definitions

**Cover/Hero Gradient:**
```css
background: linear-gradient(135deg, #2e1065 0%, #4c1d95 50%, #6d28d9 100%);
```

**Subtle Purple Tint (for cards, highlight boxes):**
```css
background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(168,85,247,0.08) 100%);
```

**Icon/Badge Gradient:**
```css
background: linear-gradient(135deg, #7c3aed, #a855f7);
```

---

## Typography

### Font Stack

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
```

Always import Inter from Google Fonts:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Type Scale

| Element | Size | Weight | Color | Line Height | Notes |
|---------|------|--------|-------|-------------|-------|
| Cover Title | 56px | 700 | white | 1.1 | Letter-spacing: -1px |
| Cover Subtitle | 22px | 300 | white (80% opacity) | 1.4 | |
| Section Heading (h2) | 32px | 700 | --primary | 1.2 | Letter-spacing: -0.5px |
| Subsection Heading (h3) | 20px | 600 | --primary | 1.3 | |
| Lead Paragraph | 18px | 400 | --text-light | 1.8 | First paragraph of sections |
| Body Text | 15px | 400 | --text | 1.7 | |
| Table Text | 14px | 400 | --text | 1.5 | |
| Table Header | 12px | 600 | white | 1.4 | Uppercase, letter-spacing: 0.5px |
| Section Number | 12px | 600 | --purple-accent | 1.2 | Uppercase, letter-spacing: 2px |
| Labels/Captions | 11-12px | 500-600 | --text-light | 1.4 | |

### Typography CSS

```css
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #334155;
  line-height: 1.7;
  font-size: 15px;
}

h2 {
  font-size: 32px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 24px;
  letter-spacing: -0.5px;
}

h3 {
  font-size: 20px;
  font-weight: 600;
  color: #0f172a;
  margin: 32px 0 16px;
}

p { margin-bottom: 16px; }

.lead {
  font-size: 18px;
  color: #64748b;
  line-height: 1.8;
  margin-bottom: 32px;
}

.section-number {
  font-size: 12px;
  font-weight: 600;
  color: #a855f7;
  letter-spacing: 2px;
  margin-bottom: 12px;
}
```

---

## Spacing System

Use consistent spacing based on an 8px grid:

| Token | Value | Usage |
|-------|-------|-------|
| xs | 8px | Tight spacing, inline gaps |
| sm | 12px | Between related items |
| md | 16px | Paragraph margins |
| lg | 24px | Section padding, card padding |
| xl | 32px | Between sections |
| 2xl | 48px | Major section breaks |
| 3xl | 64px | Container padding, section margins |
| 4xl | 80px | Cover page padding |

---

## Components

### Cover Page

The cover is full-viewport, deep purple gradient with subtle glow effects.

```css
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

/* Subtle diagonal glow */
.cover::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -20%;
  width: 80%;
  height: 200%;
  background: linear-gradient(135deg, rgba(168,85,247,0.15) 0%, rgba(236,72,153,0.1) 50%, transparent 70%);
  transform: rotate(-12deg);
}

/* Bottom-left radial glow */
.cover::after {
  content: '';
  position: absolute;
  bottom: -30%;
  left: -10%;
  width: 60%;
  height: 80%;
  background: radial-gradient(ellipse, rgba(147,51,234,0.2) 0%, transparent 70%);
  border-radius: 50%;
}

.cover-content { position: relative; z-index: 1; max-width: 800px; }

.cover-label {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #e879f9;
  margin-bottom: 24px;
}

.cover h1 {
  font-size: 56px;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 24px;
  letter-spacing: -1px;
}

.cover-subtitle {
  font-size: 22px;
  font-weight: 300;
  color: rgba(255,255,255,0.8);
  margin-bottom: 48px;
  max-width: 600px;
}
```

**Cover Metadata Row:**
```css
.cover-meta {
  display: flex;
  gap: 48px;
  padding-top: 48px;
  border-top: 1px solid rgba(255,255,255,0.15);
}

.cover-meta-item label {
  display: block;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.5);
  margin-bottom: 8px;
}

.cover-meta-item span {
  font-size: 15px;
  font-weight: 500;
}
```

**Logo Placement:**
```css
.logo {
  position: absolute;
  bottom: 80px;
  right: 80px;
  font-size: 24px;
  font-weight: 700;
  color: #fff;
}

.logo span { color: #e879f9; }  /* "One" in BayOne */
```

---

### Tables

Tables have solid purple headers with subtle column separators.

```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 24px 0;
  font-size: 14px;
}

th {
  text-align: left;
  padding: 14px 16px;
  background: #5b21b6;
  color: #fff;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  border-right: 1px solid rgba(255,255,255,0.15);
}

th:last-child { border-right: none; }
th:first-child { border-radius: 8px 0 0 0; }
th:last-child { border-radius: 0 8px 0 0; }

td {
  padding: 14px 16px;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: top;
}

tr:last-child td { border-bottom: none; }
tr:nth-child(even) { background: #f8fafc; }
```

---

### Highlight Box

Used for key callouts, important notes, and executive summary points.

```css
.highlight-box {
  background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(168,85,247,0.08) 100%);
  border-left: 4px solid #a855f7;
  padding: 24px 28px;
  margin: 32px 0;
  border-radius: 0 8px 8px 0;
}

.highlight-box p:last-child { margin-bottom: 0; }
```

---

### Cards

Used for phases, timeline items, and grouped content.

```css
.card {
  background: #fff;
  border: 1px solid rgba(124,58,237,0.15);
  border-radius: 12px;
  padding: 28px;
  margin: 24px 0;
  box-shadow: 0 1px 3px rgba(124,58,237,0.06);
}
```

**Card with numbered badge (for phases):**
```css
.phase-number {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: #fff;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-weight: 700;
}
```

---

### Stat Cards

Used for key metrics and numbers.

```css
.stat-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* Adjust columns as needed */
  gap: 24px;
  margin: 32px 0;
}

.stat-card {
  background: linear-gradient(135deg, rgba(124,58,237,0.06) 0%, rgba(168,85,247,0.04) 100%);
  border: 1px solid rgba(124,58,237,0.1);
  padding: 24px;
  border-radius: 12px;
  text-align: center;
}

.stat-value {
  font-size: 36px;
  font-weight: 700;
  color: #7c3aed;
  line-height: 1;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 13px;
  color: #64748b;
  font-weight: 500;
}
```

---

### Table of Contents

```css
.toc {
  background: linear-gradient(135deg, rgba(124,58,237,0.04) 0%, rgba(168,85,247,0.06) 100%);
  border: 1px solid rgba(124,58,237,0.1);
  padding: 40px;
  border-radius: 12px;
  margin: 40px 0;
}

.toc h3 {
  margin-top: 0;
  margin-bottom: 24px;
  font-size: 14px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #64748b;
}

.toc-list {
  list-style: none;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 40px;
}

.toc-num {
  font-size: 12px;
  font-weight: 600;
  color: #a855f7;
  width: 24px;
}

.toc-link {
  color: #334155;
  text-decoration: none;
  font-weight: 500;
}
```

---

### Footer

```css
.footer {
  text-align: center;
  padding: 48px 40px;
  border-top: 1px solid #e2e8f0;
  margin-top: 64px;
}

.footer-logo {
  font-size: 20px;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 12px;
}

.footer-logo span { color: #a855f7; }

.footer p {
  font-size: 13px;
  color: #64748b;
  margin: 0;
}
```

---

## Layout

### Container

```css
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 80px 40px;
}
```

### Section Spacing

```css
.section { margin-bottom: 64px; }
```

### Two-Column Layout

```css
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin: 24px 0;
}
```

---

## Print Styles

Always include print optimization for 8.5" x 11" output.

```css
@media print {
  @page {
    size: 8.5in 11in;
    margin: 0.4in;
  }

  body { font-size: 9pt; line-height: 1.4; }

  .cover {
    min-height: 0;
    height: 10in;
    padding: 50px;
    page-break-after: always;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .cover h1 { font-size: 36pt; }
  .cover-subtitle { font-size: 14pt; }

  .container { padding: 0; max-width: 100%; }

  .section { margin-bottom: 20px; }

  h2 { font-size: 18pt; margin-bottom: 12px; }
  h3 { font-size: 12pt; margin: 16px 0 8px; }
  p { margin-bottom: 8px; }
  .lead { font-size: 11pt; margin-bottom: 16px; }

  table { font-size: 8pt; margin: 12px 0; }
  th, td { padding: 8px 10px; }

  /* Critical: preserve colors in print */
  th, .cover, .highlight-box, .stat-card, .summary-table {
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  /* ================================================
     PRINT PAGE BREAK CONTROL
     Prevents headers, tables, and sections from
     being split across pages
     ================================================ */

  /* Keep section numbers with their headings */
  .section-number {
    break-after: avoid;
    page-break-after: avoid;
  }

  /* Keep headings with following content */
  h1, h2, h3, h4, h5, h6 {
    break-after: avoid;
    page-break-after: avoid;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Prevent tables from splitting across pages */
  table {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Keep table headers with at least some rows */
  thead {
    display: table-header-group;
  }

  /* Prevent table rows from breaking */
  tr {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Keep cards, stat cards, and highlight boxes together */
  .card, .stat-card, .highlight-box, .phase-card {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Keep stat grids together when possible */
  .stat-grid {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Keep TOC together */
  .toc {
    break-inside: avoid;
    page-break-inside: avoid;
  }

  /* Keep sections from orphaning headers at page bottom */
  .section {
    break-inside: avoid-page;
  }

  /* Prevent widows and orphans in paragraphs */
  p {
    orphans: 3;
    widows: 3;
  }

  /* Keep lead paragraphs with their section headers */
  .lead {
    break-before: avoid;
    page-break-before: avoid;
  }
}
```

---

## Style Preferences

### Do:
- Use numbered section labels (01, 02, 03...)
- Use ample whitespace between sections
- Keep tables clean with rounded top corners
- Use subtle purple tints for backgrounds, not solid colors in body
- Lead each major section with a brief overview paragraph
- Use highlight boxes sparingly for key points
- Keep the cover simple and confident

### Don't:
- Use bullet points in prose—write in natural paragraphs
- Use emojis
- Use excessive bold text
- Use multiple colors beyond the purple palette
- Use busy patterns or textures
- Overuse gradients—solid purple for headers is cleaner
- Create visual "badges" unless truly necessary
- Make summary tables look different from regular tables

### General Writing Style:
- Confident but not arrogant
- Clear and direct
- Professional without being stiff
- Avoid jargon unless speaking to technical audience

---

## Document Structure (General)

While specific content varies, most documents follow this structure:

1. **Cover Page** — Title, subtitle, metadata (client, date, classification), logo
2. **Table of Contents** (optional for longer docs)
3. **Executive Summary / Overview** — Lead section with context
4. **Body Sections** — Numbered, each with h2 heading
5. **Summary** — Final table or recap
6. **Footer** — Logo and confidentiality note

---

## Quick Reference: Essential CSS Classes

| Class | Purpose |
|-------|---------|
| `.cover` | Full-page cover with gradient |
| `.cover-label` | Small uppercase label above title |
| `.cover-meta` | Metadata row (client, date, etc.) |
| `.logo` | Positioned logo element |
| `.container` | Max-width centered content area |
| `.section` | Wrapper for each major section |
| `.section-number` | Purple "01" style label |
| `.lead` | Larger intro paragraph |
| `.highlight-box` | Purple-left-border callout |
| `.stat-grid` / `.stat-card` | Metrics display |
| `.card` | Generic bordered card |
| `.toc` | Table of contents block |
| `.two-col` | Two-column grid |
| `.footer` | Centered footer with logo |

---

## HTML Template Skeleton

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title]</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* Include full CSS from this spec */
  </style>
</head>
<body>
  <div class="cover">
    <div class="cover-content">
      <div class="cover-label">[Document Type]</div>
      <h1>[Title]</h1>
      <p class="cover-subtitle">[Subtitle]</p>
      <div class="cover-meta">
        <div class="cover-meta-item">
          <label>Prepared For</label>
          <span>[Client]</span>
        </div>
        <div class="cover-meta-item">
          <label>Date</label>
          <span>[Date]</span>
        </div>
      </div>
    </div>
    <div class="logo">Bay<span>One</span> Solutions</div>
  </div>

  <div class="container">
    <div class="section">
      <div class="section-number">01</div>
      <h2>[Section Title]</h2>
      <p class="lead">[Overview paragraph]</p>
      <p>[Body content]</p>
    </div>
    
    <!-- Additional sections -->
    
    <div class="footer">
      <div class="footer-logo">Bay<span>One</span> Solutions</div>
      <p>Confidential — Prepared for [Client]</p>
    </div>
  </div>
</body>
</html>
```

---

*Design System v1.0 — BayOne Solutions*
