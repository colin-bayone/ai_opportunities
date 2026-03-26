# SOW HTML v2 - Round 2 Improvement Ideas

Working file: `SOW-Building-Nexus-9000-switches-v2.html`

Based on visual review of all 12 pages via Playwright screenshots.

---

## Proposed Improvements

### 1. Format Totals Section Like Page 2 Fields
**Location:** Page 12
**Current:** Totals are plain text paragraphs (Total Amount (INR): 4,393,740.00)
**Proposed:** Use the same field-label flexbox layout from page 2 for consistency
**Rationale:** Creates visual consistency between the metadata on page 2 and the summary totals on page 12

---

### 2. Style Inline Sub-headers Distinctly
**Location:** Page 3 (and similar throughout)
**Current:** Sub-headers like "Organization background:", "Outsourced:", "Impact/Benefit:" are just bold text
**Proposed:** Make these slightly larger (12pt vs 11pt) or add a subtle color to distinguish from body text
**Rationale:** Helps readers quickly scan for specific subsections within the content

---

### 3. Enhance Milestone Table Header Rows
**Location:** Pages 7-11
**Current:** The summary row (Name/Type/Start Date/End Date/Gross Amount/Amount) has light blue background like other table headers
**Proposed:** Consider making this row slightly more prominent - perhaps slightly darker background or bold text in all cells
**Rationale:** The milestone header rows are important summary data; they deserve more visual weight

---

### 4. Add Subtle Row Striping to Large Tables
**Location:** Pages 7-11 (Milestone description tables)
**Current:** All rows have white background
**Proposed:** Add very subtle alternating row colors (#fafafa on even rows) to the milestone detail tables
**Rationale:** The Description cells are dense with bullet points; alternating colors help track across long rows

---

### 5. Create Totals Summary Box
**Location:** Page 12
**Current:** Financial totals are plain text list
**Proposed:** Wrap the key totals in a subtle bordered box with light background to highlight them as the document's key figures
**Rationale:** The total amount is the most important financial figure; it should stand out

---

### 6. Reduce Whitespace After Empty Headers
**Location:** Page 2 ("Vendor Fields", "Terms")
**Current:** These section headers appear with significant whitespace below before the next section
**Proposed:** Reduce bottom margin when a section header has no content following it
**Rationale:** Tightens up the layout without removing the required headers

---

### 7. Standardize Description List Formatting
**Location:** Pages 7-11 (Milestone Description cells)
**Current:** Bullet points use mix of "- " prefix with some indentation inconsistency
**Proposed:** Ensure all bullet points have consistent indentation and spacing
**Rationale:** Cleaner, more professional appearance in the dense description text

---

### 8. Add Visual Weight to "Fixed Bid" Header
**Location:** Page 7
**Current:** "Fixed Bid" is a cyan subsection header like others
**Proposed:** Consider making this slightly larger or adding the section total more prominently below it
**Rationale:** This marks the start of the financial details section - an important transition point

---

## Review Order

Will present these one at a time:
1. Totals Section Formatting
2. Inline Sub-header Styling
3. Milestone Table Header Enhancement
4. Row Striping for Large Tables
5. Totals Summary Box
6. Empty Header Whitespace
7. Description List Formatting
8. Fixed Bid Header Enhancement

---

## Status Tracking

| # | Idea | Status |
|---|------|--------|
| 1 | Totals Section Formatting | **APPROVED** |
| 2 | Inline Sub-header Styling | **APPROVED** |
| 3 | Milestone Table Header Enhancement | **APPROVED** |
| 4 | Row Striping for Large Tables | **APPROVED** |
| 4a | Totals Section Spacing Fix | **APPROVED** |
| 5 | Totals Summary Box | **APPROVED** |
| 6 | Empty Header Whitespace | **APPROVED** |
| 7 | Description List Formatting | **APPROVED** |
| 8 | Fixed Bid Header Enhancement | **APPROVED** |
