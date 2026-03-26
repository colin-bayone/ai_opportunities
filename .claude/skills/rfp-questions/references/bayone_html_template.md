# BayOne HTML Template Reference

This document provides the HTML/CSS template for generating professional RFP question documents following the BayOne design system.

---

## Design Principles

- **Purple gradient brand palette:** #2e1065 to #6d28d9
- **Inter font family** (loaded from Google Fonts)
- **Numbered sections** with badges (01, 02, 03...)
- **No emojis** in professional documents
- **Print-optimized** for 8.5" x 11" paper

---

## Complete HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{CLIENT_NAME}} - RFP Clarifying Questions</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* === CSS Variables === */
    :root {
      --primary: #0f172a;
      --accent: #a855f7;
      --purple-dark: #5b21b6;
      --purple-darker: #4c1d95;
      --purple-darkest: #2e1065;
      --text: #334155;
      --text-light: #64748b;
      --border: #e2e8f0;
      --bg-subtle: #f8fafc;
      --white: #ffffff;
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
    }

    /* === Reset === */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    /* === Base === */
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text);
      line-height: 1.5;
      font-size: 14px;
      background: var(--white);
    }

    /* === Cover Page === */
    .cover {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px;
      background: linear-gradient(135deg,
        var(--purple-darkest) 0%,
        var(--purple-darker) 50%,
        var(--purple-dark) 100%
      );
      color: var(--white);
    }

    .cover-label {
      font-size: 12px;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #e879f9;
      margin-bottom: 24px;
    }

    .cover h1 {
      font-size: 44px;
      font-weight: 700;
      margin-bottom: 24px;
      line-height: 1.2;
    }

    .cover-subtitle {
      font-size: 20px;
      color: rgba(255, 255, 255, 0.8);
      margin-bottom: 48px;
    }

    .cover-meta {
      display: flex;
      gap: 48px;
      padding-top: 48px;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
    }

    .cover-meta-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .cover-meta-item label {
      font-size: 11px;
      color: rgba(255, 255, 255, 0.5);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .cover-meta-item span {
      font-size: 15px;
      font-weight: 500;
    }

    /* === Container === */
    .container {
      max-width: 1000px;
      margin: 0 auto;
      padding: 48px 40px;
    }

    /* === Summary Grid === */
    .summary-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 40px;
    }

    .summary-stat {
      text-align: center;
      padding: 20px;
      background: linear-gradient(135deg,
        rgba(124, 58, 237, 0.06),
        rgba(168, 85, 247, 0.04)
      );
      border-radius: 8px;
    }

    .summary-stat .value {
      font-size: 28px;
      font-weight: 700;
      color: #7c3aed;
    }

    .summary-stat .label {
      font-size: 11px;
      color: var(--text-light);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 4px;
    }

    /* === Section Header === */
    .section-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 32px 0 16px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--purple-dark);
    }

    .section-num {
      font-size: 11px;
      font-weight: 700;
      color: white;
      background: var(--purple-dark);
      padding: 4px 10px;
      border-radius: 4px;
    }

    .section-title {
      font-size: 18px;
      font-weight: 700;
    }

    /* === Question Table === */
    .q-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      margin-bottom: 24px;
    }

    .q-table th {
      text-align: left;
      padding: 8px 10px;
      background: var(--purple-dark);
      color: white !important;
      font-size: 10px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .q-table td {
      padding: 10px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }

    .q-table tr:nth-child(even) {
      background: var(--bg-subtle);
    }

    .q-table tr:hover {
      background: rgba(124, 58, 237, 0.04);
    }

    /* === Question Number === */
    .q-num {
      font-weight: 600;
      color: var(--accent);
      white-space: nowrap;
    }

    /* === Badges === */
    .badge {
      display: inline-block;
      padding: 2px 6px;
      border-radius: 3px;
      font-size: 9px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .badge-original {
      background: #e0e7ff;
      color: #3730a3;
    }

    .badge-revised {
      background: #fef3c7;
      color: #92400e;
    }

    .badge-new {
      background: #d1fae5;
      color: #065f46;
    }

    .badge-removed {
      background: #fee2e2;
      color: #991b1b;
    }

    /* === Revision Note === */
    .revision-note {
      display: block;
      margin-top: 8px;
      padding: 8px 10px;
      background: #fef3c7;
      border-left: 3px solid #f59e0b;
      font-size: 11px;
      color: #92400e;
    }

    .revision-note strong {
      display: block;
      margin-bottom: 4px;
    }

    /* === Risk Flag === */
    .risk-flag {
      display: block;
      margin-top: 8px;
      padding: 8px 10px;
      background: #fee2e2;
      border-left: 3px solid #ef4444;
      font-size: 11px;
      color: #991b1b;
    }

    /* === Footer === */
    .footer {
      text-align: center;
      padding: 32px;
      border-top: 1px solid var(--border);
      margin-top: 40px;
    }

    .footer-brand {
      font-size: 18px;
      font-weight: 700;
    }

    .footer-brand span {
      color: var(--accent);
    }

    .footer-confidential {
      font-size: 12px;
      color: var(--text-light);
      margin-top: 8px;
    }

    /* === Print Styles === */
    @media print {
      @page {
        size: 8.5in 11in;
        margin: 0.4in;
      }

      .cover {
        height: 10in;
        page-break-after: always;
      }

      .section-header {
        page-break-after: avoid;
      }

      .q-table {
        page-break-inside: auto;
      }

      .q-table tr {
        page-break-inside: avoid;
        page-break-after: auto;
      }

      .footer {
        page-break-before: avoid;
      }
    }
  </style>
</head>
<body>
  <!-- Cover Page -->
  <div class="cover">
    <div class="cover-content">
      <div class="cover-label">RFP Clarifying Questions</div>
      <h1>{{CLIENT_NAME}}<br>{{RFP_NAME}}</h1>
      <p class="cover-subtitle">{{QUESTION_COUNT}} questions for Q&A submission</p>
      <div class="cover-meta">
        <div class="cover-meta-item">
          <label>Prepared For</label>
          <span>{{CLIENT_NAME}}</span>
        </div>
        <div class="cover-meta-item">
          <label>Submitted By</label>
          <span>BayOne Solutions</span>
        </div>
        <div class="cover-meta-item">
          <label>Date</label>
          <span>{{DATE}}</span>
        </div>
        <div class="cover-meta-item">
          <label>Version</label>
          <span>Final</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Content -->
  <div class="container">
    <!-- Summary Statistics -->
    <div class="summary-grid">
      <div class="summary-stat">
        <div class="value">{{QUESTION_COUNT}}</div>
        <div class="label">Total Questions</div>
      </div>
      <div class="summary-stat">
        <div class="value">{{ORIGINAL_COUNT}}</div>
        <div class="label">Original</div>
      </div>
      <div class="summary-stat">
        <div class="value">{{REVISED_COUNT}}</div>
        <div class="label">Revised</div>
      </div>
      <div class="summary-stat">
        <div class="value">{{NEW_COUNT}}</div>
        <div class="label">New</div>
      </div>
    </div>

    <!-- Section Template (repeat for each category) -->
    <div class="section-header">
      <span class="section-num">01</span>
      <span class="section-title">{{SECTION_NAME}}</span>
    </div>

    <table class="q-table">
      <thead>
        <tr>
          <th style="width: 40px;">#</th>
          <th style="width: 70px;">Type</th>
          <th style="width: 40%;">Question</th>
          <th style="width: 15%;">RFP Reference</th>
          <th style="width: 30%;">Justification</th>
        </tr>
      </thead>
      <tbody>
        <!-- Question Row Template -->
        <tr>
          <td class="q-num">{{Q_NUM}}</td>
          <td><span class="badge badge-{{Q_TYPE_LOWER}}">{{Q_TYPE}}</span></td>
          <td>
            {{Q_TEXT}}
            <!-- If revised, include original -->
            <span class="revision-note">
              <strong>Original question:</strong>
              {{Q_ORIGINAL_TEXT}}
            </span>
          </td>
          <td style="font-size: 12px;">{{Q_RFP_REF}}</td>
          <td style="font-size: 12px;">{{Q_JUSTIFICATION}}</td>
        </tr>
      </tbody>
    </table>

    <!-- Footer -->
    <div class="footer">
      <div class="footer-brand">Bay<span>One</span> Solutions</div>
      <p class="footer-confidential">Confidential</p>
    </div>
  </div>
</body>
</html>
```

---

## Template Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{CLIENT_NAME}}` | Client/company name | McGrath RentCorp |
| `{{RFP_NAME}}` | RFP name/title | MSP RFP 2026 |
| `{{DATE}}` | Document date | February 23, 2026 |
| `{{QUESTION_COUNT}}` | Total questions | 36 |
| `{{ORIGINAL_COUNT}}` | Unchanged questions | 16 |
| `{{REVISED_COUNT}}` | Modified questions | 3 |
| `{{NEW_COUNT}}` | New questions | 17 |
| `{{SECTION_NAME}}` | Category name | Scope & Transition Planning |
| `{{Q_NUM}}` | Question number | 1 |
| `{{Q_TYPE}}` | Question type | Original / Revised / New |
| `{{Q_TYPE_LOWER}}` | Lowercase type for CSS | original / revised / new |
| `{{Q_TEXT}}` | Question text | Can MGRC provide... |
| `{{Q_ORIGINAL_TEXT}}` | Original text (for revised) | Is MGRC open to... |
| `{{Q_RFP_REF}}` | RFP section reference | MGRC Environment |
| `{{Q_JUSTIFICATION}}` | Why we ask | Critical for cost modeling... |

---

## Badge Types

| Type | Background | Text Color | Usage |
|------|------------|------------|-------|
| Original | #e0e7ff (blue) | #3730a3 | Unchanged from source |
| Revised | #fef3c7 (yellow) | #92400e | Modified from source |
| New | #d1fae5 (green) | #065f46 | Added during gap analysis |
| Removed | #fee2e2 (red) | #991b1b | Excluded (if shown) |

---

## Print Considerations

- Cover page is exactly 10 inches tall for proper page break
- Questions avoid breaking mid-row
- Section headers stay with content
- 0.4 inch margins for 8.5" x 11" paper
- Font sizes optimized for print readability

---

## Usage Notes

1. **Load Inter font** - Required for brand consistency
2. **No emojis** - Use text labels and badges instead
3. **Revision notes** - Always show full original text
4. **Print preview** - Test before final distribution
5. **CSS variables** - Adjust colors at `:root` if needed
