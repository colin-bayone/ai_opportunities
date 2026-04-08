# SOW Conversion Notes

**Source:** `SOW-Building Nexus 9000 (switches).pdf`
**Output:** `SOW-Building-Nexus-9000-switches.md`
**Conversion Date:** 2026-02-13
**Converted By:** Claude Code (Opus 4.5)

---

## Purpose

This document catalogs anomalies, quirks, and potential errors found in the original PDF that were **intentionally preserved** in the markdown conversion to maintain perfect fidelity. These items are documented here so they can be reviewed and addressed separately if needed.

---

## Preserved Anomalies

### 1. December 2025 Milestone End Date

**Location:** Page 8, Financials section, second milestone table

**Issue:** The end date for "Develop AI solutions Phase 1 of 3 (66% of features complete) - 2025/12" shows:
- Start Date: `12/1/2025`
- End Date: `12/31/2026` (likely should be `12/31/2025`)

**Why preserved:** This appears in both the PDF and Word document. It may be a typo (2026 instead of 2025), but we cannot assume intent. Preserved as-is for fidelity.

---

### 2. Section Numbering Sequence Error

**Location:** Pages 5-6

**Issue:** Subsections 2.4.1 and 2.4.2 appear AFTER Section 2.5:
```
2.4 Acceptance of Deliverables
2.5 Resources
2.4.1 Supplier Program Manager    <-- Out of sequence
2.4.2 Required Personnel          <-- Out of sequence
2.6 Required Personnel & Other Resources
```

**Why preserved:** This numbering sequence exists in the original document. It may be intentional (2.4.1/2.4.2 as sub-items under 2.5 Resources despite the numbering) or an error. Preserved as-is.

---

### 3. Double-Dash Formatting in Descriptions

**Location:** Pages 7-11, all milestone Description fields

**Issue:** One bullet point reads `- -Porting the test plan to the new test bed` with a space between two dashes.

**Why preserved:** This formatting appears consistently across all six milestone descriptions in the original. May be a copy/paste artifact or intentional formatting. Preserved as-is.

---

### 4. Inconsistent Bullet Point Formatting in Descriptions

**Location:** Pages 7-11, milestone Description fields

**Issue:** The bullet list in descriptions has inconsistent formatting:
- Some items start with `- ` (dash space)
- Some items start with `-` (dash only, no space)

Example from original:
```
- Build data pipeline for the given problem
- Design, Develop AI models
- Test and deploy the solutions in production
- Raise defects in bug reporting tool and fix them.
...
- -Porting the test plan to the new test bed
-Executing the test plan for maintenance releases...
-Automating test cases
```

**Why preserved:** Reflects the original document exactly.

---

### 5. Acceptance Criteria Bullet Formatting (Later Milestones)

**Location:** Pages 10-11, milestones for Feb, Mar, Apr 2026

**Issue:** In these milestones, the Acceptance Criteria shows the bullet point `•` on its own line, followed by the text on the next line (as opposed to earlier milestones where the bullet and text are on the same line).

**Why preserved:** This is how it appears in the original PDF rendering.

---

### 6. Trailing Space in "Project "

**Location:** Page 3, Section 1.1

**Issue:** The text reads: `...within the C-Worker connect associated "Project " and remains...`

There is a space before the closing quotation mark after "Project".

**Why preserved:** Appears in original. May be intentional (placeholder) or formatting artifact.

---

### 7. Empty Tables

**Location:** Page 6 and Page 12

**Issue:** The following tables are empty with no data rows:
- Required Personnel table (3 columns, no data)
- Other Resources table (2 columns, no data)
- Unit of Measure table (6 columns, no data)

**Why preserved:** These are intentionally empty in the original document (template placeholders).

---

## Elements Not Representable in Markdown

| Element | Location | Handling |
|---------|----------|----------|
| Cisco logo | Page 1 | `[LOGO: Cisco logo - stylized "CISCO" text with bridge-like bars above]` |
| Blue/colored header text | Throughout | Converted to markdown headers (##, ###, ####) |
| Signature lines | Page 12 | Represented with underscores: `_________________________________` |
| Table borders | Throughout | Standard markdown table syntax |
| Page-specific whitespace/margins | Throughout | Not preserved; content-only conversion |

---

## Verification Checklist

For reviewers verifying this conversion:

- [ ] All 12 pages present with content
- [ ] All section headers (1, 2, 2.1-2.7, 3, 3.1, Financials, etc.)
- [ ] Both SLA tables (4.2.1 and 4.2.2) complete
- [ ] All 6 milestone deliverables with Description/Acceptance Criteria/BAN
- [ ] All numerical values (amounts, dates, codes)
- [ ] Signature block with both parties
- [ ] Totals section with all line items
