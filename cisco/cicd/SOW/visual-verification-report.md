# Visual Verification Report: SOW HTML Conversion

Comparing HTML screenshots against original PDF page by page.

---

## Pages 1-3

### Page 1 (Cover Page)

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Page border | Has decorative border/frame around entire page | No border | **YES - Missing page border** |
| Cisco logo | Dark/black colored bars and text | Cyan/teal colored (#049fd9) | **YES - Color differs** |
| "Cisco Systems" | Centered, black text | Centered, black text | OK |
| Title | Centered | Centered | OK |
| "SOW" | Centered, bold | Centered, bold | OK |
| Reference ID | Present | Present | OK |
| Prepared by | Present | Present | OK |
| Footer | Confidential, title, Page 1 of 12 | Same | OK |

**Issues Found:**
1. **Missing page border** - PDF has a thin rectangular border around the entire page content area. HTML has none.
2. **Logo color mismatch** - PDF logo appears black/dark gray. HTML logo is Cisco blue/cyan.

---

### Page 2

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| "SOW" header | Blue, centered | Blue, centered | OK |
| Title | Blue, centered | Blue, centered | OK |
| "General Information" header | Blue | Blue | OK |
| Field labels/values | Black text | Black text | OK |
| Timeline section | Blue header | Blue header | OK |
| Owner Information | Blue header | Blue header | OK |
| Custom Fields | Blue header | Blue header | OK |
| Vendor Information | Blue header | Blue header | OK |
| Vendor Fields | Blue header (empty) | Blue header (empty) | OK |
| Terms | Blue header (empty) | Blue header (empty) | OK |
| "1 General Information" | Blue header | Blue header | OK |
| "1.1 General Information" | Blue, smaller | Blue, smaller | OK |
| Body paragraphs | Black text, justified | Black text, justified | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 3

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Continuation paragraphs | Black text | Black text | OK |
| "2 Services and Work Product" | Blue header | Blue header | OK |
| "2.1 Services Objectives" | Blue header | Blue header | OK |
| "Organization background:" | Bold black | Bold black | OK |
| Body paragraphs | Black, justified | Black, justified | OK |
| "Outsourced:" | Bold black | Bold black | OK |
| "Impact/Benefit:" | Bold black | Bold black | OK |
| "Supplier management of resource:" | Bold black | Bold black | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

---

## Pages 4-6

### Page 4 (SLA Tables)

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| "2.2 Services & Service Levels" | Blue header | Blue header | OK |
| Body paragraphs | Black text, justified | Black text, justified | OK |
| Instruction text "[Include at least two SLAs...]" | Italicized | Italicized | OK |
| "Table 4.2.1 <Service Level Agreement 1>" | Bold, above table | Bold, above table | OK |
| SLA table 1 - left column labels | Bold | Bold | OK |
| SLA table 1 - right column values | Italic | Italic | OK |
| SLA table 1 - row count | 6 rows | 6 rows | OK |
| Table borders | Visible | Visible | OK |
| "Table 4.2.2 <Service Level Agreement 2>" | Bold, above table | Bold, above table | OK |
| SLA table 2 - first 3 rows | Present | Present | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 5

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| SLA table 2 continuation | Target, Frequency, Fee Adjustment rows | Same | OK |
| "2.3 Deliverables" | Blue header | Blue header | OK |
| "2.4 Acceptance of Deliverables" | Blue header | Blue header | OK |
| "[acceptance period]" in text | Italicized | Italicized | OK |
| "2.5 Resources" | Blue header | Blue header | OK |
| "2.4.1 Supplier Program Manager" | Bold BLACK (not blue) | Bold BLACK | OK |
| "2.4.2 Required Personnel" | Bold BLACK (not blue) | Bold BLACK | OK |
| Body paragraphs | Present | Present | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 6

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Continuation paragraph | Present | Present | OK |
| "2.6 Required Personnel & Other Resources" | Blue header | Blue header | OK |
| "[Note:...]" instruction | Present | Present | OK |
| "Required Personnel" label | Bold, above table | Bold, above table | OK |
| Required Personnel table | 3 columns, 4 empty rows | 3 columns, 4 empty rows | OK |
| "Other Resources" label | Bold, above table | Bold, above table | OK |
| Other Resources table | 2 columns, 4 empty rows | 2 columns, 4 empty rows | OK |
| "2.7 Place of Performance" | Blue header | Blue header | OK |
| Location/time info | Present | Present | OK |
| "3 Payment" | Blue header | Blue header | OK |
| "3.1 Payment" | Blue header | Blue header | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

---

## Pages 7-9 (Financials/Milestones)

### Page 7

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Text continuation (3.1 Payment) | Present | Present | OK |
| "Financials" | Blue header | Blue header | OK |
| "Fixed Bid" | Blue header | Blue header | OK |
| "Section Total (INR): Rs4,393,740.00" | Bold amount | Bold amount | OK |
| Milestone table header row | 6 columns: Name/Type/Start/End/Gross/Amount | Same | OK |
| Milestone 1 Name | "Develop AI solutions Phase 1 of 3 (66% of features complete) - 2025/11" | Same | OK |
| Milestone 1 Dates | 11/5/2025 - 11/30/2025 | Same | OK |
| Milestone 1 Amounts | Rs690,580.00 | Rs690,580.00 | OK |
| Description label | Italic | Italic | OK |
| Description content | Bullet list with responsibilities | Same | OK |
| Acceptance Criteria label | Italic | Italic | OK |
| Acceptance Criteria content | Bullet point text | Same | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 8

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| "release." (continuation) | Present | Present | OK |
| BAN row | "Outside Services - India Contractors-660619" | Same | OK |
| Milestone 2 header | Present | Present | OK |
| Milestone 2 Name | "...2025/12" | Same | OK |
| Milestone 2 End Date | 12/31/2026 (known quirk) | 12/31/2026 | OK - Preserved |
| Milestone 2 Amounts | Rs690,580.00 | Rs690,580.00 | OK |
| Description/Acceptance/BAN | Present | Present | OK |
| Milestone 3 header starts | "Develop AI solutions Phase 1 of 3 (66% of features complete) -" | Same (split across pages) | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 9

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Milestone 3 header continuation | "2026/01" | "2026/01" | OK |
| Milestone 3 Description | Full content | Full content | OK |
| Milestone 3 Acceptance Criteria | Present | Present | OK |
| Milestone 3 BAN | 660619 | 660619 | OK |
| Milestone 4 header | "Develop AI solutions Phase - 2026/02 - 670854" | Same | OK |
| Milestone 4 Dates | 2/1/2026 - 2/28/2026 | Same | OK |
| Milestone 4 Amounts | Rs774,000.00 | Rs774,000.00 | OK |
| Milestone 4 Description (partial) | Starts | Starts | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

---

## Pages 10-12

### Page 10

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Milestone 4 Description continuation | Bullet list | Bullet list | OK |
| Milestone 4 Acceptance Criteria | Bullet (•) on own line, then text | Same (anomaly preserved) | OK |
| Milestone 4 BAN | 670854 | 670854 | OK |
| Milestone 5 header | "Develop AI solutions Phase - 2026/03 - 670854" | Same | OK |
| Milestone 5 Dates | 3/1/2026 - 3/31/2026 | Same | OK |
| Milestone 5 Amounts | Rs774,000.00 | Rs774,000.00 | OK |
| Milestone 5 Description | Full content | Full content | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 11

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| Milestone 5 Acceptance Criteria | Bullet on own line, then text | Same (anomaly preserved) | OK |
| Milestone 5 BAN | 670854 | 670854 | OK |
| Milestone 6 header | "Develop AI solutions Phase - 2026/04 - 670854" | Same | OK |
| Milestone 6 Dates | 4/1/2026 - 4/30/2026 | Same | OK |
| Milestone 6 Amounts | Rs774,000.00 | Rs774,000.00 | OK |
| Milestone 6 Description | Full content | Full content | OK |
| Milestone 6 Acceptance Criteria | Bullet on own line, then text | Same | OK |
| Milestone 6 BAN | 670854 | 670854 | OK |
| Footer | Present | Present | OK |

**Issues Found:** None

---

### Page 12 (Final Page)

| Element | PDF | HTML | Issue? |
|---------|-----|------|--------|
| "Unit of Measure" | Blue header | Blue header | OK |
| "Section Total (INR): Rs0.00" | Bold amount | Bold amount | OK |
| Unit of Measure table | 6 columns, 1 empty row | Same | OK |
| "Totals" | Blue header | Blue header | OK |
| Total Amount (INR) | 4,393,740.00 | 4,393,740.00 | OK |
| Total Gross Amount (INR) | 4,393,740.00 | 4,393,740.00 | OK |
| Total Estimated Taxes | 0.00 | 0.00 | OK |
| Milestone totals (3 lines) | Present | Present | OK |
| Unit of Measure totals (3 lines) | Present | Present | OK |
| Resource Total | 0.00 | 0.00 | OK |
| "IN WITNESS WHEREOF..." | Present | Present | OK |
| Owner Signature block | Line + Date line | Line + Date line | OK |
| Owner Title | [insert title here] | [insert title here] | OK |
| Owner Name | Mahaveer Jinka | Mahaveer Jinka | OK |
| Vendor Signature block | Line + Date line | Line + Date line | OK |
| Vendor Title | [insert title here] | [insert title here] | OK |
| Vendor Name | Ashish Singh | Ashish Singh | OK |
| Footer | Page 12 of 12 | Page 12 of 12 | OK |

**Issues Found:** None

---

## Final Summary

### Total Visual Issues Found: 2

| Issue | Page | Severity | Description |
|-------|------|----------|-------------|
| 1 | Page 1 | Minor | **Missing page border** - PDF has a thin rectangular border/frame around the entire page content. HTML has no border. |
| 2 | Page 1 | Minor | **Logo color mismatch** - PDF Cisco logo is black/dark gray. HTML logo is cyan (#049fd9). |

### Verified as Correct

- All 12 pages present with correct content
- All section headers render in blue
- All tables render with visible borders
- SLA tables: bold labels, italic values
- Milestone tables: italic Description/Acceptance Criteria/BAN labels
- All numerical values match (dates, amounts, BAN codes)
- All known anomalies preserved (12/31/2026 date, bullet formatting, section numbering)
- Page footers present on all pages
- Signature block renders correctly

### Recommendation

**PASS with minor issues** - The HTML conversion is functionally complete and accurate. The two issues found are cosmetic and on the cover page only:

1. If page border is required, add CSS border to `.page` class
2. If black logo is required, change SVG fill color from `#049fd9` to `#000000`

