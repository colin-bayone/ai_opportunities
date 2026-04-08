# Verification Task: SOW HTML Conversion

## Your Role

You are a verification reviewer. Your job is to compare an HTML conversion against the verified markdown source and original PDF to identify **any missing content, rendering issues, or discrepancies**. You are NOT fixing anything - only identifying issues.

---

## Source Documents (in order of authority)

1. **Original PDF:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building Nexus 9000 (switches).pdf`
2. **Verified Markdown:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches.md`
3. **Word Document:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW 33282 FY26Q3_Building Nexus 9000 (switches) product line _Bayone 2026-02-13.docx`

## Document to Verify

**HTML conversion:** `/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-Building-Nexus-9000-switches.html`

## Known Anomalies (Already Documented)

Review this file to understand what was intentionally preserved from the original:
`/home/cmoore/programming/cisco_projects/cicd/SOW/SOW-conversion-notes.md`

These anomalies were found in the original documents and preserved for fidelity. Do NOT flag these as issues.

---

## Your Task

### 1. Read All Documents
- Read the verified Markdown as your primary source
- Read the HTML conversion
- Cross-reference with original PDF for visual accuracy

### 2. Verify Content Fidelity

Check that ALL content from the markdown appears correctly in HTML:

**Text Content:**
- [ ] All paragraphs present and complete
- [ ] All section headers (1, 2, 2.1-2.7, 3, 3.1, Financials, etc.)
- [ ] All field labels and values
- [ ] Special text (bracketed notes, italicized instructions)

**Tables:**
- [ ] Table 4.2.1 (SLA 1) - 6 rows with bold labels, italic values
- [ ] Table 4.2.2 (SLA 2) - 6 rows with bold labels, italic values
- [ ] Required Personnel table - 3 columns, empty rows
- [ ] Other Resources table - 2 columns, empty rows
- [ ] 6 Milestone tables with Description/Acceptance Criteria/BAN
- [ ] Unit of Measure table - 6 columns, empty row

**Key Values:**
- [ ] Total Budget: Rs4,393,740.00
- [ ] Reference ID: 33282
- [ ] Milestone amounts: 3x Rs690,580.00, 3x Rs774,000.00
- [ ] BAN codes: 660619 (Nov-Jan), 670854 (Feb-Apr)
- [ ] December milestone end date: 12/31/2026 (preserved quirk)

**Visual Elements:**
- [ ] Cisco logo present (SVG or placeholder)
- [ ] Blue section headers (matching Cisco styling)
- [ ] Page footers with "Confidential", doc title, page number
- [ ] Signature block with lines for both parties

### 3. Verify Structure & Formatting

**Page Layout:**
- [ ] All 12 pages present with appropriate page breaks
- [ ] Content flows correctly at page boundaries
- [ ] Print styling works (@media print)

**Table Formatting:**
- [ ] Borders visible on all tables
- [ ] Column alignment correct
- [ ] Empty cells preserved (not collapsed)

**Typography:**
- [ ] Section headers in blue (Cisco blue ~#049fd9)
- [ ] Bold text where appropriate
- [ ] Italic text in SLA table values
- [ ] Instruction text in italics

### 4. Browser Testing (Optional but Recommended)

Open the HTML in a browser and verify:
- [ ] Document renders correctly
- [ ] No broken layouts
- [ ] Print preview shows correct page breaks
- [ ] All 12 pages visible in print preview

---

## Report Format

```markdown
# SOW HTML Conversion Verification Report

## Summary
[Overall assessment: PASS / ISSUES FOUND]

## Content Issues
[List any missing or incorrect content, or "None found"]

## Formatting Issues
[List any visual/structural problems, or "None found"]

## Table Issues
[List any table rendering problems, or "None found"]

## Page Layout Issues
[List any page break or layout problems, or "None found"]

## Verified Elements
[Checklist of what you confirmed as correct]

## Recommendation
[Ready for use / Needs revision]
```

---

## Important Notes

- The HTML should maintain 100% content fidelity with the verified markdown
- Visual styling should approximate the original Cisco PDF (professional, clean)
- All documented anomalies from the original should still be preserved
- DO NOT suggest improvements or design changes - only report issues
