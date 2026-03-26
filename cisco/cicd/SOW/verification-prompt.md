# Verification Task: SOW PDF-to-Markdown Conversion

## Your Role

You are a verification reviewer. Your job is to compare a markdown conversion against the original source documents and identify **any missing content, errors, or discrepancies**. You are NOT fixing anything - only identifying issues.

---

## Source Documents (in order of authority)

1. **Original PDF:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building Nexus 9000 (switches).pdf`
2. **Word Document:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW 33282 FY26Q3_Building Nexus 9000 (switches) product line _Bayone 2026-02-13.docx`
3. **Text extraction (for reference):** `/home/cmoore/programming/cisco_projects/cicd/SOW/pdf-copied-text.txt`

## Document to Verify

**Markdown conversion:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches.md`

## Known Anomalies (Already Documented)

Review this file to understand what was intentionally preserved from the original:
`/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-conversion-notes.md`

These anomalies were found in the original documents and preserved for fidelity. Do NOT flag these as issues unless you find they were transcribed incorrectly.

---

## Your Task

### 1. Read All Documents
- Read the PDF and/or Word document as your source of truth
- Read the markdown conversion
- Read the conversion notes to understand known quirks

### 2. Perform Page-by-Page Verification

For each of the 12 pages, verify:
- All text content is present
- All tables have correct structure and content
- All numerical values (amounts, dates, reference numbers) are accurate
- All section headers and numbering are correct
- Page breaks are marked appropriately

### 3. Check Specific Elements

**Headers & Structure:**
- [ ] Cover page (Title, Reference ID, Prepared by)
- [ ] General Information section (Currency, Budget, Location, etc.)
- [ ] Timeline section
- [ ] Owner Information section
- [ ] Vendor Information section
- [ ] Sections 1 through 3 with all subsections
- [ ] Financials section

**Tables:**
- [ ] Table 4.2.1 (SLA 1) - 6 rows
- [ ] Table 4.2.2 (SLA 2) - 6 rows
- [ ] Required Personnel table - 3 columns
- [ ] Other Resources table - 2 columns
- [ ] 6 Milestone tables in Fixed Bid section
- [ ] Unit of Measure table - 6 columns

**Key Values to Verify:**
- [ ] Total Budget: Rs4,393,740.00
- [ ] Reference ID: 33282
- [ ] Start Date: 11/5/2025
- [ ] End Date: 4/30/2026
- [ ] Cost Center: DCN-Switching-India-123023191
- [ ] Milestone amounts: 3x Rs690,580.00, 3x Rs774,000.00
- [ ] BAN codes: 660619 (Nov-Jan), 670854 (Feb-Apr)

**Signature Block:**
- [ ] Owner: Mahaveer Jinka
- [ ] Vendor: Ashish Singh
- [ ] Both signature lines present

### 4. Report Your Findings

Create a verification report with:

**A. Missing Content** - Any text, tables, or elements present in the source but missing from the markdown

**B. Incorrect Content** - Any values, text, or structure that differs from the source

**C. Structural Issues** - Problems with page break placement, table formatting, or document organization

**D. Confirmation** - Elements you verified as correct

---

## Important Notes

- **DO NOT** suggest corrections or improvements
- **DO NOT** flag items already documented in the conversion notes as issues (unless transcribed wrong)
- **DO** flag any content that is missing or incorrect
- **DO** be thorough - this is a legal/contractual document where accuracy matters
- **DO** note the specific page and section for any issues found

The goal is 100% fidelity to the original. Even "errors" in the original should be preserved exactly as they appear.

---

## Output Format

Please structure your report as:

```markdown
# SOW Conversion Verification Report

## Summary
[Overall assessment: PASS / ISSUES FOUND]

## Missing Content
[List any content in source but missing from MD, or "None found"]

## Incorrect Content
[List any discrepancies, or "None found"]

## Structural Issues
[List any formatting/organization problems, or "None found"]

## Verified Elements
[Checklist of what you confirmed as correct]

## Recommendation
[Ready for use / Needs revision]
```
