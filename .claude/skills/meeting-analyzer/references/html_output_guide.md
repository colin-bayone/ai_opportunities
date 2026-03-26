# HTML Output Guide

Convert meeting analysis documents to polished, print-ready HTML following the BayOne design system.

---

## Contents

1. [Design System Overview](#design-system-overview)
2. [HTML Template Structure](#html-template-structure)
3. [Document-Specific Templates](#document-specific-templates)
4. [Complete CSS Reference](#complete-css-reference)

---

## Design System Overview

The BayOne design system creates clean, professional documents inspired by Big Four consulting deliverables. Key principles:

- **Clean over cluttered** - Ample whitespace
- **Purple brand palette** - Gradient covers, purple accents
- **Professional typography** - Inter font family
- **Print-optimized** - 8.5" x 11" ready
- **No emojis, no excessive bullets** - Prose-focused

### Brand Colors

```css
--purple-darkest: #2e1065;  /* Cover backgrounds */
--purple-dark: #4c1d95;     /* Gradient midpoint */
--purple-mid: #5b21b6;      /* Table headers */
--purple-bright: #6d28d9;   /* Gradient endpoint */
--purple-accent: #a855f7;   /* Section numbers */
--purple-glow: #e879f9;     /* Cover label, logo accent */
--primary: #0f172a;         /* Headings */
--text: #334155;            /* Body text */
--text-light: #64748b;      /* Secondary text */
--border: #e2e8f0;          /* Borders */
--bg-subtle: #f8fafc;       /* Alternating rows */
```

---

## HTML Template Structure

Every meeting document HTML follows this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title]</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* Full CSS - see Complete CSS Reference section */
  </style>
</head>
<body>
  <!-- Cover Page -->
  <div class="cover">
    <div class="cover-content">
      <div class="cover-label">[DOCUMENT TYPE]</div>
      <h1>[Meeting Title]</h1>
      <p class="cover-subtitle">[Meeting subtitle/context]</p>
      <div class="cover-meta">
        <div class="cover-meta-item">
          <label>Date</label>
          <span>[Meeting Date]</span>
        </div>
        <div class="cover-meta-item">
          <label>Location</label>
          <span>[Location]</span>
        </div>
        <div class="cover-meta-item">
          <label>Classification</label>
          <span>Internal</span>
        </div>
      </div>
    </div>
    <div class="logo">Bay<span>One</span> Solutions</div>
  </div>

  <!-- Content Container -->
  <div class="container">
    <!-- Sections go here -->

    <div class="footer">
      <div class="footer-logo">Bay<span>One</span> Solutions</div>
      <p>Internal Meeting Notes</p>
    </div>
  </div>
</body>
</html>
```

---

## Document-Specific Templates

### 1. Meeting Breakdown (00_meeting_breakdown.html)

**Cover label:** `MEETING SUMMARY`

**Sections to include:**

```html
<!-- Section: Participants -->
<div class="section">
  <div class="section-number">01</div>
  <h2>Participants</h2>
  <table>
    <tr>
      <th>Name</th>
      <th>Organization</th>
      <th>Role</th>
      <th>Scope in Meeting</th>
    </tr>
    <tr>
      <td><strong>[Name]</strong></td>
      <td>[Org]</td>
      <td>[Title]</td>
      <td>[What they covered]</td>
    </tr>
  </table>

  <!-- Transcription corrections note -->
  <div class="highlight-box">
    <p><strong>Transcription Note:</strong> Speech-to-text corrections applied: "[error]" → "[correction]"</p>
  </div>
</div>

<!-- Section: Discussion Topics -->
<div class="section">
  <div class="section-number">02</div>
  <h2>Discussion Topics</h2>

  <h3>[Topic Name]</h3>
  <p>[Discussion content as prose, not bullets]</p>

  <div class="highlight-box">
    <p><strong>Key Quote ([Speaker]):</strong> "[Verbatim quote]"</p>
  </div>
</div>

<!-- Section: Decisions -->
<div class="section">
  <div class="section-number">03</div>
  <h2>Decisions Made</h2>
  <table>
    <tr>
      <th>Decision</th>
      <th>Made By</th>
      <th>Context</th>
    </tr>
    <tr>
      <td>[Decision]</td>
      <td>[Person]</td>
      <td>[Why/context]</td>
    </tr>
  </table>
</div>

<!-- Section: Commitments -->
<div class="section">
  <div class="section-number">04</div>
  <h2>Commitments</h2>

  <h3>[Organization] Commitments</h3>
  <table>
    <tr>
      <th>Owner</th>
      <th>Commitment</th>
      <th>Timing</th>
    </tr>
    <tr>
      <td><strong>[Person]</strong></td>
      <td>[What they committed to]</td>
      <td>[When]</td>
    </tr>
  </table>
</div>

<!-- Section: Open Items -->
<div class="section">
  <div class="section-number">05</div>
  <h2>Open Items</h2>
  <table>
    <tr>
      <th>Item</th>
      <th>Owner</th>
      <th>Priority</th>
      <th>Notes</th>
    </tr>
    <tr>
      <td>[Item]</td>
      <td>[Person]</td>
      <td><span class="priority-high">High</span></td>
      <td>[Context]</td>
    </tr>
  </table>
</div>

<!-- Section: Key Insights -->
<div class="section">
  <div class="section-number">06</div>
  <h2>Key Insights</h2>
  <div class="insight-grid">
    <div class="insight-card">
      <h4>[Insight Title]</h4>
      <p>[Explanation of what this means]</p>
    </div>
  </div>
</div>
```

---

### 2. Speaker Notes (01_speaker_notes.html)

**Cover label:** `SPEAKER NOTES`

**Sections:**

```html
<!-- One section per speaker -->
<div class="section">
  <div class="section-number">01</div>
  <h2>[Speaker Name]</h2>
  <p class="lead">[Role] — Present for [duration/phases]</p>

  <h3>On [Topic]</h3>
  <div class="quote-block">
    <p>"[Verbatim quote]"</p>
  </div>

  <h3>Key Commitments</h3>
  <ul class="commitment-list">
    <li>[Commitment 1]</li>
    <li>[Commitment 2]</li>
  </ul>
</div>

<!-- Transcription Corrections Section -->
<div class="section">
  <div class="section-number">REFERENCE</div>
  <h2>Transcription Corrections</h2>
  <table>
    <tr>
      <th>Transcript Shows</th>
      <th>Actually Means</th>
    </tr>
    <tr>
      <td>[error]</td>
      <td>[correction]</td>
    </tr>
  </table>
</div>
```

---

### 3. Crossover Analysis (02_crossover_analysis.html)

**Cover label:** `CROSSOVER ANALYSIS`

**Sections:**

```html
<!-- Visual Relationship Diagram -->
<div class="section">
  <div class="section-number">01</div>
  <h2>Project Relationship</h2>

  <div class="relationship-diagram">
    <div class="project-box">
      <h4>[Project 1]</h4>
      <p>[Focus area]</p>
    </div>
    <div class="connector">↔</div>
    <div class="project-box">
      <h4>[Project 2]</h4>
      <p>[Focus area]</p>
    </div>
  </div>
</div>

<!-- Shared Challenges -->
<div class="section">
  <div class="section-number">02</div>
  <h2>Shared Challenges</h2>
  <table>
    <tr>
      <th>Challenge</th>
      <th>[Project 1]</th>
      <th>[Project 2]</th>
    </tr>
    <tr>
      <td>[Challenge]</td>
      <td>[How it manifests]</td>
      <td>[How it manifests]</td>
    </tr>
  </table>
</div>

<!-- Synergies -->
<div class="section">
  <div class="section-number">03</div>
  <h2>Potential Synergies</h2>
  <div class="synergy-grid">
    <div class="synergy-card">
      <h4>Build Once, Use Twice</h4>
      <table>
        <tr>
          <th>Component</th>
          <th>Build For</th>
          <th>Also Useful For</th>
        </tr>
      </table>
    </div>
  </div>
</div>
```

---

### 4. Sentiment & Relationship (03_sentiment_and_relationship.html)

**Cover label:** `SENTIMENT ANALYSIS`

**Sections:**

```html
<!-- Overall Tone -->
<div class="section">
  <div class="section-number">01</div>
  <h2>Overall Tone</h2>
  <div class="tone-summary">
    <div class="tone-badge positive">Collaborative</div>
    <div class="tone-badge positive">Optimistic</div>
  </div>
  <p class="lead">[Description of meeting energy]</p>
</div>

<!-- Per-Person Sentiment -->
<div class="section">
  <div class="section-number">02</div>
  <h2>[Person Name]</h2>
  <p class="lead">[Role]</p>

  <h3>[Sentiment Category]</h3>
  <p>[Interpretation]</p>
  <div class="quote-block">
    <p>"[Supporting quote]"</p>
    <span class="interpretation">Interpretation: [Analysis]</span>
  </div>
</div>

<!-- Relationship Indicators -->
<div class="section">
  <div class="section-number">03</div>
  <h2>Relationship Indicators</h2>

  <div class="indicators-grid">
    <div class="indicator-card">
      <h4>Trust Signals</h4>
      <ul>
        <li>[Signal]</li>
      </ul>
    </div>
    <div class="indicator-card">
      <h4>Interest Signals</h4>
      <ul>
        <li>[Signal]</li>
      </ul>
    </div>
    <div class="indicator-card">
      <h4>Investment Signals</h4>
      <ul>
        <li>[Signal]</li>
      </ul>
    </div>
  </div>
</div>

<!-- Meeting Comparison (if applicable) -->
<div class="section">
  <div class="section-number">04</div>
  <h2>Comparison to Previous Meetings</h2>
  <table>
    <tr>
      <th>Aspect</th>
      <th>Previous Meeting</th>
      <th>This Meeting</th>
    </tr>
    <tr>
      <td>Tone</td>
      <td>[Description]</td>
      <td>[Description]</td>
    </tr>
  </table>
</div>
```

---

## Complete CSS Reference

Include this complete CSS in every HTML document:

```css
:root {
  --primary: #0f172a;
  --accent: #a855f7;
  --purple-dark: #5b21b6;
  --text: #334155;
  --text-light: #64748b;
  --border: #e2e8f0;
  --bg-subtle: #f8fafc;
  --white: #ffffff;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  color: var(--text);
  line-height: 1.7;
  font-size: 15px;
  background: var(--white);
}

/* Cover Page */
.cover {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 80px;
  background: linear-gradient(135deg, #2e1065 0%, #4c1d95 50%, #6d28d9 100%);
  color: var(--white);
  position: relative;
  overflow: hidden;
}

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
  font-size: 48px;
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

.logo {
  position: absolute;
  bottom: 80px;
  right: 80px;
  font-size: 24px;
  font-weight: 700;
  color: var(--white);
  letter-spacing: -0.5px;
}

.logo span { color: #e879f9; }

/* Container & Sections */
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 80px 40px;
}

.section { margin-bottom: 44px; }

.section-number {
  display: inline-block;
  font-size: 13px;
  font-weight: 700;
  color: var(--purple-dark);
  letter-spacing: 2px;
  margin-bottom: 12px;
  padding: 6px 14px;
  background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(168,85,247,0.15) 100%);
  border-radius: 4px;
}

h2 {
  font-size: 28px;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 20px;
  letter-spacing: -0.5px;
}

h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--primary);
  margin: 28px 0 14px;
}

h4 {
  font-size: 15px;
  font-weight: 600;
  color: var(--primary);
  margin: 20px 0 10px;
}

p { margin-bottom: 16px; }

.lead {
  font-size: 17px;
  color: var(--text-light);
  line-height: 1.8;
  margin-bottom: 28px;
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 14px;
}

th {
  text-align: left;
  padding: 10px 14px;
  background: #5b21b6;
  color: var(--white);
  font-weight: 600;
  font-size: 11px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  border-right: 1px solid rgba(255,255,255,0.15);
}

th:last-child { border-right: none; }
th:first-child { border-radius: 8px 0 0 0; }
th:last-child { border-radius: 0 8px 0 0; }

td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  vertical-align: top;
}

tr:last-child td { border-bottom: none; }
tr:nth-child(even) { background: var(--bg-subtle); }

/* Highlight Box */
.highlight-box {
  background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(168,85,247,0.08) 100%);
  border-left: 4px solid #a855f7;
  padding: 20px 24px;
  margin: 24px 0;
  border-radius: 0 8px 8px 0;
}

.highlight-box p:last-child { margin-bottom: 0; }

/* Quote Block */
.quote-block {
  background: var(--bg-subtle);
  border-left: 3px solid var(--accent);
  padding: 12px 16px;
  margin: 10px 0;
  border-radius: 0 8px 8px 0;
  font-style: italic;
}

.quote-block .interpretation {
  display: block;
  margin-top: 12px;
  font-style: normal;
  font-size: 13px;
  color: var(--text-light);
}

/* Priority Badges */
.priority-blocking {
  background: #fef2f2;
  color: #991b1b;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
}

.priority-high {
  background: #fef9c3;
  color: #854d0e;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
}

.priority-medium {
  background: #e0e7ff;
  color: #3730a3;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
  text-transform: uppercase;
}

/* Tone Badges */
.tone-summary {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
}

.tone-badge {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 500;
}

.tone-badge.positive {
  background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(168,85,247,0.15) 100%);
  color: var(--purple-dark);
}

/* Insight/Indicator Cards */
.insight-grid, .indicators-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin: 24px 0;
}

.insight-card, .indicator-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
}

.insight-card h4, .indicator-card h4 {
  margin: 0 0 12px 0;
  font-size: 14px;
  color: var(--accent);
}

.indicator-card ul {
  margin: 0;
  padding-left: 20px;
  font-size: 14px;
}

.indicator-card li {
  margin-bottom: 6px;
}

/* Relationship Diagram */
.relationship-diagram {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  margin: 32px 0;
  padding: 32px;
  background: linear-gradient(135deg, rgba(124,58,237,0.04) 0%, rgba(168,85,247,0.06) 100%);
  border-radius: 12px;
}

.project-box {
  background: var(--white);
  border: 2px solid var(--border);
  border-radius: 8px;
  padding: 20px 28px;
  text-align: center;
  min-width: 200px;
}

.project-box h4 {
  margin: 0 0 8px 0;
  color: var(--primary);
}

.project-box p {
  margin: 0;
  font-size: 13px;
  color: var(--text-light);
}

.connector {
  font-size: 24px;
  color: var(--accent);
  font-weight: 700;
}

/* Footer */
.footer {
  text-align: center;
  padding: 48px 40px;
  border-top: 1px solid var(--border);
  margin-top: 64px;
}

.footer-logo {
  font-size: 20px;
  font-weight: 700;
  color: var(--primary);
  margin-bottom: 12px;
}

.footer-logo span { color: #a855f7; }

.footer p {
  font-size: 13px;
  color: var(--text-light);
  margin: 0;
}

/* Print Styles */
@media print {
  @page {
    size: 8.5in 11in;
    margin: 0.5in;
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

  .container { padding: 0; max-width: 100%; }

  .section {
    margin-bottom: 24px;
    page-break-inside: avoid;
  }

  h2 { font-size: 14pt; margin-bottom: 10px; page-break-after: avoid; }
  h3 { font-size: 11pt; margin: 14px 0 8px; page-break-after: avoid; }
  p { margin-bottom: 6px; }
  .lead { font-size: 10pt; margin-bottom: 14px; }

  table {
    font-size: 8pt;
    margin: 10px 0;
    page-break-inside: avoid;
  }

  th, td {
    padding: 6px 8px;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .highlight-box, .quote-block {
    padding: 12px 16px;
    margin: 14px 0;
    page-break-inside: avoid;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }

  .insight-grid, .indicators-grid {
    gap: 12px;
  }

  .footer {
    margin-top: 20px;
    padding: 16px;
  }
}
```

---

## Usage Instructions

When generating HTML output:

1. **Create the markdown first** - Complete analysis before HTML conversion
2. **Use the template structure** - Follow the section patterns above
3. **Write in prose** - Convert bullet points to paragraphs
4. **Preserve all quotes** - Use `.quote-block` for verbatim quotes
5. **Include transcription notes** - Use `.highlight-box` at the top
6. **Use appropriate cover label** - Match to document type

### Cover Labels by Document Type

| Document | Cover Label |
|----------|-------------|
| Meeting Breakdown | `MEETING SUMMARY` |
| Speaker Notes | `SPEAKER NOTES` |
| Crossover Analysis | `CROSSOVER ANALYSIS` |
| Sentiment & Relationship | `SENTIMENT ANALYSIS` |

### File Naming

HTML files go alongside their markdown counterparts:

```
meeting1_anand_srini_divakar/
├── 00_meeting_breakdown.md
├── 00_meeting_breakdown.html    # HTML version
├── 01_speaker_notes.md
├── 01_speaker_notes.html        # HTML version
└── ...
```
