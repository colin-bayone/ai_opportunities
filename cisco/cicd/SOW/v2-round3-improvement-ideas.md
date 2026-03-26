# SOW HTML v2 - Round 3 Improvement Ideas

Working file: `SOW-Building-Nexus-9000-switches-v2.html`

Based on fresh screenshots after Round 2 changes.

---

## Critical Fixes

### 1. Fix Inconsistent Bullet Formatting (Page 10 top)
**Location:** Milestone table - "Develop AI solutions Phase - 2026/02" Description cell
**Current:** Uses "- " dashes instead of proper `<ul><li>` bullets like other milestones
**Problem:** Inconsistent with other milestone descriptions that use bullet points
**Fix:** Convert this Description cell to use proper HTML list like the others

---

### 2. Prevent Tables from Splitting Across Pages
**Location:** Throughout document (pages 4-5, 7-8, 8-9, 9-10, 10-11)
**Current:** Milestone tables and SLA tables split across page boundaries
**Proposed:** Add CSS per the BayOne design spec:
```css
table {
    break-inside: avoid;
    page-break-inside: avoid;
}
tr {
    break-inside: avoid;
    page-break-inside: avoid;
}
```
**Rationale:** Tables should never split - this is a fundamental print layout rule

---

### 3. Keep Section Headers with Content
**Location:** Throughout document
**Current:** Headers may end up at bottom of page with content on next page
**Proposed:** Add CSS:
```css
h1, h2, h3, h4, h5, h6 {
    break-after: avoid;
    page-break-after: avoid;
}
```
**Rationale:** Orphaned headers look unprofessional

---

## Review Order

1. Fix inconsistent bullets (Page 10)
2. Prevent table splitting
3. Keep headers with content

---

## Status Tracking

| # | Idea | Status |
|---|------|--------|
| 1 | Fix Inconsistent Bullets (Page 10) | **APPROVED** |
| 2 | Prevent Table Splitting | **APPROVED** |
| 3 | Keep Headers with Content | **APPROVED** |
