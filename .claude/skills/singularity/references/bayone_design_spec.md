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
| Cover Subtitle | 20px | 300 | white (80% opacity) | 1.4 | Optional; omit for shorter covers |
| Section Heading (h2) | 32px | 700 | --primary | 1.2 | Letter-spacing: -0.5px |
| Subsection Heading (h3) | 20px | 600 | --primary | 1.3 | |
| Lead Paragraph | 18px | 400 | --text-light | 1.8 | First paragraph of sections |
| Body Text | 15px | 400 | --text | 1.7 | |
| h4 Subheading | 16px | 600 | --primary | — | margin: 24px 0 12px |
| Table Text | 14px | 400 | --text | 1.5 | |
| Table Header | 12px | 600 | white | 1.4 | Uppercase, letter-spacing: 0.5px |
| Section Number | 12px | 600 | --purple-accent | 1.2 | Uppercase, letter-spacing: 2px |
| Labels/Captions | 11-12px | 500-600 | --text-light | 1.4 | |

### Typography CSS

```css
/* Global reset — include in every document */
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: #334155;
  line-height: 1.7;
  font-size: 15px;
  background: #ffffff;
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

h4 {
  font-size: 16px;
  font-weight: 600;
  color: #0f172a;
  margin: 24px 0 12px;
}

p { margin-bottom: 16px; }

.lead {
  font-size: 18px;
  color: #64748b;
  line-height: 1.8;
  margin-bottom: 32px;
}

.section-number {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  color: #a855f7;
  letter-spacing: 2px;
  margin-bottom: 12px;
  padding: 6px 14px;
  background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(168,85,247,0.15) 100%);
  border-radius: 4px;
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
  font-size: 20px;
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

**Cover Label Convention:**

The `.cover-label` is a thematic label, NOT the literal document type. It should describe the category or value proposition of the document rather than naming the template type. Examples from gold standards:

| Document | Cover Label | NOT |
|----------|------------|-----|
| Problem Restatement | "Secure Knowledge Enablement" | "Problem Restatement" |
| Information Request | "Discovery" | "Information Request" |
| Preliminary Approach | "Preliminary Approach" | (this one is acceptable as-is) |
| POC Proposal | "Proof-of-Concept Proposal" | (this one is acceptable as-is) |
| Resource Plan | "Resource Plan" | (this one is acceptable as-is) |
| EDW Framework | "Working Session" | "EDW Framework" |

When the document type is self-explanatory and client-appropriate, using it directly is fine. When the document type is internal jargon (e.g., "Problem Restatement"), use a thematic label instead.

**Cover Variants:**

Covers may omit the subtitle when the title is self-sufficient. Demonstrated in information_request.html ("Next Steps and Discovery" with no subtitle) and preliminary_approach.html ("A Hybrid Architecture for Intelligent IP Protection" with no subtitle).

Cover meta items typically include 2-3 items. Common patterns:
- `Prepared For` / `Date` / `Author` (Cisco documents)
- `Prepared For` / `Prepared By` / `Date` (Lam Research documents)
- `Date` / `Program` (internal working sessions like the EDW framework)

Logo text may be "BayOne Solutions" (Cisco documents) or "BayOne" (Lam Research documents). Use whichever is appropriate for the client relationship.

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

/* Lists inside highlight boxes */
.highlight-box ol, .highlight-box ul {
  margin: 12px 0 0 20px;
  padding: 0;
}

.highlight-box li {
  margin-bottom: 8px;
  line-height: 1.6;
}
```

Highlight boxes frequently contain ordered or unordered lists (e.g., success criteria, key points). The list styles above ensure consistent spacing when lists appear inside the box. Demonstrated in poc_proposal_v5.html (success criteria) and information_request.html (document organization note).

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

/* Card internal styles */
.card h4 {
  margin-top: 0;
  color: #5b21b6;  /* --purple-mid */
}

.card ul {
  margin: 0 0 0 20px;
  padding: 0;
}

.card li {
  margin-bottom: 8px;
  line-height: 1.5;
}

.card p {
  font-size: 14px;
  line-height: 1.6;
}

.card p:last-child { margin-bottom: 0; }
```

Cards frequently contain headings, lists, and paragraphs. The h4 heading uses `--purple-mid` to visually distinguish card titles from section headings. When cards are placed inside a `.two-col` grid, omit `margin: 24px 0` on `.card` since the grid handles spacing. Demonstrated across poc_proposal_v5.html (investment model), information_request.html (Priority 3 items), and preliminary_approach.html (hybrid architecture).

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
  font-size: 32px;
  font-weight: 700;
  color: #7c3aed;
  line-height: 1;
  margin-bottom: 8px;
}

.stat-label {
  font-size: 12px;
  color: #64748b;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
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

### Styled Lists

Body-content lists used outside of cards, highlight boxes, or other containers. The class name varies by document context (`.criteria-list`, `.content-list`, `.request-list`) but the styling is identical. Pick the name that fits the content.

```css
ul.criteria-list,
ul.content-list,
ul.request-list {
  margin: 0 0 0 20px;
  padding: 0;
}

ul.criteria-list li,
ul.content-list li,
ul.request-list li {
  margin-bottom: 10px;
  line-height: 1.6;
}
```

These lists typically use `<strong>` for lead-in labels on each item:
```html
<ul class="criteria-list">
  <li><strong>Represent</strong> the broader conversion challenge rather than edge cases</li>
  <li><strong>Are sufficiently self-contained</strong> to convert without extensive system dependencies</li>
</ul>
```

Demonstrated in poc_proposal_v5.html (criteria-list), problem_restatement.html (content-list), and information_request.html (request-list).

---

### Workflow Grid

Numbered step cards in a grid layout. Used to show sequential processes or workflows. Each step has a floating numbered badge that overlaps the card border.

```css
.workflow-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;  /* Use 1fr 1fr for two-column variant */
  gap: 20px;
  margin: 24px 0;
}

.workflow-step {
  background: #fff;
  border: 1px solid rgba(124,58,237,0.15);
  border-radius: 12px;
  padding: 20px 24px;
  position: relative;
}

.workflow-step-number {
  position: absolute;
  top: -12px;
  left: 20px;
  width: 24px;
  height: 24px;
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: #fff;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
}

.workflow-step h5 {
  font-size: 15px;
  font-weight: 600;
  color: #0f172a;
  margin: 0 0 8px 0;
}

.workflow-step p {
  font-size: 14px;
  margin: 0;
  color: #334155;
  line-height: 1.6;
}
```

**Usage example:**
```html
<div class="workflow-grid">
  <div class="workflow-step">
    <div class="workflow-step-number">1</div>
    <h5>Self-Help</h5>
    <p>The user searches knowledge bases and documentation to find an answer independently.</p>
  </div>
  <div class="workflow-step">
    <div class="workflow-step-number">2</div>
    <h5>Ask for Help</h5>
    <p>The user reaches out to a community of experts for guidance.</p>
  </div>
  <div class="workflow-step">
    <div class="workflow-step-number">3</div>
    <h5>Escalate</h5>
    <p>A structured troubleshooting process involving deeper analysis.</p>
  </div>
</div>
```

Column count is flexible: use three columns for 3 or 6 steps, two columns for 4 steps. Demonstrated in problem_restatement.html (3-col, 3 steps), preliminary_approach.html (3-col, 4 steps wrapping), and poc_proposal_v5.html (2-col, 4 steps).

---

### Phase Meta

Inline metadata row that appears below a phase heading. Displays key attributes (duration, deliverable, etc.) in a horizontal flex layout with a subtle purple tint background.

```css
.phase-meta {
  display: flex;
  gap: 48px;
  padding: 20px 24px;
  background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(168,85,247,0.08) 100%);
  border-radius: 8px;
  margin-bottom: 24px;
}

.phase-meta-item {
  display: flex;
  flex-direction: column;
}

.phase-meta-item label {
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #64748b;
  margin-bottom: 4px;
}

.phase-meta-item span {
  font-size: 14px;
  font-weight: 500;
  color: #0f172a;
}
```

**Usage example:**
```html
<h3>Phase 1: Exploration and Onboarding</h3>
<div class="phase-meta">
  <div class="phase-meta-item">
    <label>Duration</label>
    <span>Approximately two weeks from code access</span>
  </div>
  <div class="phase-meta-item">
    <label>Deliverable</label>
    <span>Analysis document with categorized screens</span>
  </div>
</div>
```

Demonstrated in poc_proposal_v5.html and poc_proposal_v5_detailed.html (phase descriptions in proposals).

---

### Deliverable Grid

Two-column grid of small feature/deliverable cards. Lighter weight than `.card` -- uses `--bg-subtle` background and `--border` for a subdued appearance. Used to list outputs, deliverables, or feature categories.

```css
.deliverable-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin: 20px 0;
}

.deliverable-card {
  background: #f8fafc;  /* --bg-subtle */
  border: 1px solid #e2e8f0;  /* --border */
  border-radius: 8px;
  padding: 16px 20px;
}

.deliverable-card h5 {
  font-size: 14px;
  font-weight: 600;
  color: #5b21b6;  /* --purple-mid */
  margin: 0 0 6px 0;
}

.deliverable-card p {
  font-size: 13px;
  margin: 0;
  color: #334155;
  line-height: 1.5;
}
```

**Usage example:**
```html
<div class="deliverable-grid">
  <div class="deliverable-card">
    <h5>Screen Inventory</h5>
    <p>Categorization by type: dashboards, reports, configuration wizards</p>
  </div>
  <div class="deliverable-card">
    <h5>Dependency Graphs</h5>
    <p>Mapping which screens share backend services</p>
  </div>
</div>
```

Demonstrated in poc_proposal_v5.html and poc_proposal_v5_detailed.html (codebase analysis deliverables).

Note: The resource plan uses a similar but distinct component called `.deliverable-item` with the subtle purple gradient tint instead of flat `--bg-subtle`. See "Deliverable Item" in the Tier 2 components section.

---

### Priority Tiers

Tiered request containers used in information request documents. Each tier has a gradient badge indicating priority level and an audience tag indicating who should respond.

```css
.priority-tier {
  background: #fff;
  border: 1px solid rgba(124,58,237,0.15);
  border-radius: 12px;
  padding: 32px;
  margin: 32px 0;
  box-shadow: 0 1px 3px rgba(124,58,237,0.06);
}

.priority-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 8px;
}

.priority-badge {
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: #fff;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  white-space: nowrap;
}

/* Tier variants — progressively deeper purple */
.priority-badge.tier-2 {
  background: linear-gradient(135deg, #4c1d95, #7c3aed);
}

.priority-badge.tier-3 {
  background: linear-gradient(135deg, #2e1065, #4c1d95);
}

.priority-audience {
  display: inline-block;
  font-size: 12px;
  font-weight: 500;
  color: #64748b;
  padding: 4px 12px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
}

.priority-tier h3 {
  margin-top: 12px;
}
```

**Usage example:**
```html
<div class="priority-tier">
  <div class="priority-header">
    <span class="priority-badge">Priority 1</span>
    <span class="priority-audience">Business team can answer</span>
  </div>
  <!-- Ask cards go here -->
</div>

<div class="priority-tier">
  <div class="priority-header">
    <span class="priority-badge tier-2">Priority 2</span>
    <span class="priority-audience">Technical team needed</span>
  </div>
  <!-- Ask cards go here -->
</div>
```

Demonstrated in information_request.html (three priority tiers with nested ask cards).

---

### Ask Card

Content cards nested inside priority tiers. Each ask card represents a specific information request with context and a structured list of what is needed. Lighter than `.card` -- uses `--bg-subtle` background.

```css
.ask-card {
  background: #f8fafc;  /* --bg-subtle */
  border: 1px solid #e2e8f0;  /* --border */
  border-radius: 10px;
  padding: 24px 28px;
  margin: 20px 0;
}

.ask-card h4 {
  margin-top: 0;
  color: #5b21b6;  /* --purple-mid */
  font-size: 17px;
}

.ask-card p {
  font-size: 14px;
  line-height: 1.7;
}

.ask-card p:last-child { margin-bottom: 0; }

.ask-card ul {
  margin: 8px 0 0 20px;
  padding: 0;
}

.ask-card li {
  margin-bottom: 8px;
  line-height: 1.6;
  font-size: 14px;
}
```

Ask cards can also contain tables for structured data within a request item. Demonstrated in information_request.html (all priority tiers).

---

### Call-to-Action Box

A stronger variant of the highlight box, used for "what happens next" or closing action sections. Has a visible border on all sides (not just the left) and a stronger purple tint.

```css
.cta-box {
  background: linear-gradient(135deg, rgba(124,58,237,0.08) 0%, rgba(168,85,247,0.12) 100%);
  border: 2px solid rgba(124,58,237,0.2);
  border-radius: 12px;
  padding: 32px;
  margin: 32px 0;
}

.cta-box h3 {
  margin-top: 0;
  color: #5b21b6;  /* --purple-mid */
}

.cta-box p:last-child { margin-bottom: 0; }
```

**Usage example:**
```html
<div class="cta-box">
  <h3>What Happens Next</h3>
  <p>Once we receive the information outlined in Priority 1, we will be in a position to prepare a preliminary approach document.</p>
</div>
```

Use sparingly -- at most once per document, typically near the end. Demonstrated in information_request.html (Next Steps section).

---

### Quarter Card

Timeline/phase card with a badge, title, and optional cost indicator. Used for quarterly planning or phased engagement breakdowns.

```css
.quarter-card {
  background: #fff;
  border: 1px solid rgba(124,58,237,0.15);
  border-radius: 12px;
  padding: 28px;
  margin: 24px 0;
  box-shadow: 0 1px 3px rgba(124,58,237,0.06);
}

.quarter-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 20px;
}

.quarter-badge {
  background: linear-gradient(135deg, #7c3aed, #a855f7);
  color: #fff;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}

.quarter-title {
  font-size: 20px;
  font-weight: 600;
  color: #0f172a;
}

.quarter-cost {
  margin-left: auto;
  font-size: 18px;
  font-weight: 600;
  color: #7c3aed;
}
```

**Usage example:**
```html
<div class="quarter-card">
  <div class="quarter-header">
    <span class="quarter-badge">Q1</span>
    <span class="quarter-title">Foundation and Quick Wins</span>
    <span class="quarter-cost">$100K</span>
  </div>
  <!-- Content: tables, deliverable grids, team notes -->
</div>
```

Demonstrated in resource_plan_for_cisco.html (quarterly breakdown).

---

### Deliverable Item

A subtle variant of the deliverable card with a purple gradient tint background instead of flat `--bg-subtle`. Used within quarter cards or other container components.

```css
.deliverable-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin: 24px 0;
}

.deliverable-item {
  background: linear-gradient(135deg, rgba(124,58,237,0.04) 0%, rgba(168,85,247,0.06) 100%);
  border: 1px solid rgba(124,58,237,0.1);
  border-radius: 10px;
  padding: 20px;
}

.deliverable-item h4 {
  font-size: 14px;
  font-weight: 600;
  color: #0f172a;
  margin: 0 0 8px 0;
}

.deliverable-item p {
  font-size: 13px;
  color: #64748b;
  margin: 0;
  line-height: 1.5;
}
```

Demonstrated in resource_plan_for_cisco.html (quarterly deliverables within quarter cards).

---

### Team Note

Inline note used within cards to provide additional context about team composition or logistics. Subtle purple background with no border.

```css
.team-note {
  background: rgba(124,58,237,0.06);
  padding: 14px 18px;
  border-radius: 8px;
  font-size: 13px;
  color: #334155;
  margin-top: 16px;
}
```

Demonstrated in resource_plan_for_cisco.html (team composition notes within quarter cards).

---

### Summary Table

A wrapped table variant with rounded corners on the outer container. Used for final summary/recap tables that should stand out from inline tables.

```css
.summary-table {
  border-radius: 12px;
  overflow: hidden;
  margin: 32px 0;
  border: 1px solid #e2e8f0;
}

.summary-table th {
  background: #5b21b6;
}

.summary-table tr:nth-child(even) {
  background: #f8fafc;
}
```

The `overflow: hidden` combined with `border-radius` gives the entire table rounded corners, unlike regular tables where only the header corners are rounded. Demonstrated in resource_plan_for_cisco.html (final cost summary).

---

### System Grid

Grid of technology or system items displayed as centered cells. Used for listing tools, platforms, or systems in a compact visual layout.

```css
.system-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin: 20px 0;
}

.system-item {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 14px 16px;
  text-align: center;
}

.system-item strong {
  display: block;
  font-size: 13px;
  color: #0f172a;
  margin-bottom: 4px;
}

.system-item span {
  font-size: 11px;
  color: #64748b;
}
```

**Usage example:**
```html
<div class="system-grid">
  <div class="system-item">
    <strong>Jenkins</strong>
    <span>CI/CD orchestration</span>
  </div>
  <div class="system-item">
    <strong>Airflow</strong>
    <span>Workflow automation</span>
  </div>
</div>
```

Demonstrated in resource_plan_for_cisco.html (technology landscape).

---

### Org Chart

Organizational chart component for displaying team structure with connecting lines. Built with flex and grid layouts with CSS-drawn connector lines.

```css
.org-chart {
  margin: 32px 0;
  padding: 32px;
  background: linear-gradient(135deg, rgba(124,58,237,0.04) 0%, rgba(168,85,247,0.06) 100%);
  border-radius: 8px;
  position: relative;
}

.org-row {
  display: flex;
  justify-content: center;
  gap: 32px;
  margin-bottom: 24px;
}

.org-row:last-child { margin-bottom: 0; }

.org-box {
  background: #fff;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px 28px;
  text-align: center;
}

.org-box strong {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: #0f172a;
  margin-bottom: 4px;
}

.org-box span {
  font-size: 12px;
  color: #64748b;
}

/* Primary box (e.g., client name at top) */
.org-box.primary {
  background: #5b21b6;
  border-color: #5b21b6;
  padding: 20px 40px;
}

.org-box.primary strong {
  color: #fff;
  font-size: 16px;
}

/* Lead role box */
.org-box.lead {
  border-color: #a855f7;
}

/* Oversight/advisory role box */
.org-box.oversight {
  border-style: dashed;
  border-color: #64748b;
}
```

Org chart connector lines are document-specific (positions depend on the actual org structure) and should be implemented with `::before` and `::after` pseudo-elements as needed. Demonstrated in resource_plan_for_cisco.html (team structure).

---

### Dynamics Grid

Two-column grid of information cards with colored headings. Used for displaying team dynamics, operating principles, or categorical information.

```css
.dynamics-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin: 24px 0;
}

.dynamics-card {
  background: #f8fafc;
  border-radius: 8px;
  padding: 24px;
}

.dynamics-card h4 {
  font-size: 14px;
  font-weight: 600;
  color: #a855f7;  /* --purple-accent */
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0 0 12px 0;
}

.dynamics-card p {
  font-size: 14px;
  color: #334155;
  margin: 0;
  line-height: 1.6;
}
```

Demonstrated in resource_plan_for_cisco.html (team dynamics section).

---

### Idea Card

Content card for presenting ideas, capabilities, or feature descriptions. Similar to `.card` but includes a box-shadow and uses `--purple-mid` for the heading. Best for lists of discrete concepts where each needs its own container.

```css
.idea-card {
  background: #fff;
  border: 1px solid rgba(124,58,237,0.15);
  border-radius: 12px;
  padding: 28px;
  margin: 24px 0;
  box-shadow: 0 1px 3px rgba(124,58,237,0.06);
}

.idea-card h4 {
  margin-top: 0;
  color: #5b21b6;  /* --purple-mid */
}

.idea-card p {
  margin-bottom: 0;
  color: #334155;
}
```

Demonstrated in 03_edw_acceleration_framework_v2.html (AI acceleration ideas).

---

### Challenge Item

Simple heading-plus-paragraph pattern for listing challenges, risks, or issues. No container or border -- relies on the heading color for visual grouping.

```css
.challenge-item {
  margin-bottom: 24px;
}

.challenge-item h4 {
  color: #5b21b6;  /* --purple-mid */
  margin-bottom: 8px;
}

.challenge-item p {
  margin-bottom: 0;
}
```

Demonstrated in 03_edw_acceleration_framework_v2.html (key challenges section).

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

  .cover h1 { font-size: 32pt; }
  .cover-subtitle { font-size: 13pt; }

  /* Reposition cover meta and logo for print */
  .cover-meta { padding-top: 32px; gap: 32px; }
  .logo { position: relative; bottom: auto; right: auto; margin-top: 32px; }

  .container { padding: 0; max-width: 100%; }

  .section { margin-bottom: 20px; }

  h2 { font-size: 14pt; margin-bottom: 10px; page-break-after: avoid; }
  h3 { font-size: 11pt; margin: 14px 0 8px; page-break-after: avoid; }
  h4 { font-size: 10pt; margin: 10px 0 6px; page-break-after: avoid; }
  p { margin-bottom: 6px; }
  .lead { font-size: 10pt; margin-bottom: 14px; }

  table { font-size: 8pt; margin: 10px 0; }
  th, td { padding: 6px 8px; }

  /* Critical: preserve colors in print */
  th, .cover, .highlight-box, .stat-card, .summary-table,
  .priority-badge, .cta-box, .workflow-step-number, .quarter-badge {
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
  .card, .stat-card, .highlight-box, .phase-card,
  .idea-card, .ask-card, .priority-tier, .quarter-card {
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

  /* ================================================
     PRINT SIZE REDUCTIONS FOR COMPONENTS
     ================================================ */

  .highlight-box {
    padding: 12px 16px;
    margin: 14px 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .two-col { gap: 16px; }
  .card { padding: 16px; }

  .workflow-grid { gap: 12px; }
  .workflow-step { padding: 12px 16px; }

  .phase-meta { padding: 10px 14px; margin-bottom: 16px; }

  .deliverable-grid { gap: 10px; }
  .deliverable-card { padding: 10px 14px; }
  .deliverable-item { padding: 12px; }

  .priority-tier { padding: 16px; margin: 14px 0; }
  .ask-card { padding: 12px 16px; margin: 10px 0; }

  .cta-box {
    padding: 16px;
    margin: 14px 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .quarter-card { padding: 16px; margin: 12px 0; }

  .stat-grid { gap: 12px; margin: 20px 0; }
  .stat-card { padding: 14px; }
  .stat-value { font-size: 20pt; }
  .stat-label { font-size: 8pt; }

  .system-grid { gap: 8px; }
  .system-item { padding: 10px; }

  .dynamics-grid { page-break-inside: avoid; }
  .org-chart { page-break-inside: avoid; }

  .footer { margin-top: 20px; padding: 16px; }
}
```

---

## Style Preferences

### Do:
- Use numbered section labels (01, 02, 03...) or word labels (PURPOSE, EXECUTIVE SUMMARY) for lead sections
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

1. **Cover Page** — Title, subtitle (optional), metadata (client, date, classification), logo
2. **Table of Contents** (optional for longer docs)
3. **Executive Summary / Overview** — Lead section with context
4. **Body Sections** — Numbered, each with h2 heading
5. **Summary** — Final table or recap
6. **Footer** — Logo and confidentiality note

### Section Numbering Conventions

The first section may use a word label instead of a number to signal its role:
- `PURPOSE` — Used when the first section explains why the document exists (problem_restatement.html)
- `EXECUTIVE SUMMARY` — Used for proposals and plans (poc_proposal_v5.html)
- `01` — Used when the document jumps directly into content (preliminary_approach.html)

Subsequent sections always use zero-padded numbers: `01`, `02`, `03`, etc. If the first section uses a word label, the second section starts at `01`.

### Document Type Component Conventions

Different document types tend to use different component sets:

| Document Type | Typical Components |
|--------------|-------------------|
| **Proposal** | Phase meta, deliverable grids, workflow steps, two-col cards, highlight boxes with success criteria |
| **Understanding/Restatement** | Workflow grids, tables, highlight boxes, content lists |
| **Information Request** | Priority tiers, ask cards, CTA box, tables within ask cards |
| **Technical Approach** | Workflow grids, two-col cards, tables, highlight boxes |
| **Resource Plan** | Quarter cards, stat grids, org charts, deliverable items, summary tables |
| **Framework/Working Session** | Idea cards, challenge items, tables |

---

## Quick Reference: Essential CSS Classes

### Core Layout & Structure
| Class | Purpose |
|-------|---------|
| `.cover` | Full-page cover with gradient |
| `.cover-label` | Small uppercase thematic label above title |
| `.cover-meta` | Metadata row (client, date, etc.) |
| `.logo` | Positioned logo element |
| `.container` | Max-width centered content area |
| `.section` | Wrapper for each major section |
| `.section-number` | Purple pill-badge section label (01, PURPOSE, etc.) |
| `.lead` | Larger intro paragraph |
| `.footer` | Centered footer with logo |
| `.two-col` | Two-column grid |
| `.toc` | Table of contents block |

### Content Components
| Class | Purpose |
|-------|---------|
| `.highlight-box` | Purple-left-border callout (supports lists) |
| `.cta-box` | Stronger callout with full border (end-of-doc actions) |
| `.card` | Generic bordered card (used in two-col layouts) |
| `.idea-card` | Card with box-shadow for ideas/capabilities |
| `.stat-grid` / `.stat-card` | Metrics display |
| `.criteria-list` / `.content-list` | Styled body-content lists |

### Process & Timeline Components
| Class | Purpose |
|-------|---------|
| `.workflow-grid` / `.workflow-step` | Numbered step cards in grid |
| `.workflow-step-number` | Floating numbered badge on workflow step |
| `.phase-meta` | Inline phase attributes (duration, deliverable) |
| `.deliverable-grid` / `.deliverable-card` | Grid of deliverable feature cards |
| `.deliverable-item` | Purple-tint variant of deliverable card |
| `.quarter-card` / `.quarter-badge` | Timeline card with badge and cost |

### Request & Priority Components
| Class | Purpose |
|-------|---------|
| `.priority-tier` | Priority-level container |
| `.priority-badge` / `.tier-2` / `.tier-3` | Gradient priority badges |
| `.priority-audience` | Audience tag (who should answer) |
| `.ask-card` | Information request card within priority tier |

### Specialized Components
| Class | Purpose |
|-------|---------|
| `.summary-table` | Rounded-corner table wrapper |
| `.system-grid` / `.system-item` | Technology/system display grid |
| `.org-chart` / `.org-box` | Organizational chart |
| `.dynamics-grid` / `.dynamics-card` | Two-col info cards with colored headings |
| `.challenge-item` | Simple h4 + p challenge/risk listing |
| `.team-note` | Inline note within cards |

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
      <div class="cover-label">[Thematic Label]</div>
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

*Design System v2.0 — BayOne Solutions*
