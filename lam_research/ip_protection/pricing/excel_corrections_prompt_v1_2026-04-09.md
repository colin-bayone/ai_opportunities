# Correction Prompt v1: Lam Research POC Workbook

**Apply these changes to the Lam Research POC workbook. Do NOT restructure anything. These are targeted corrections only.**

---

## Change 1: Anonymize the Onshore Resource

### The Problem

The Personnel and POC tabs currently show "Colin Moore (Director of AI)" with his full salary and loaded rate. This workbook is shared with the internal BayOne team. Team members should not see a named individual's compensation attributed directly to them.

### The Fix

On every tab where this resource appears (Personnel, Project Inputs, POC, and any other tab that references the name):

| Old Label | New Label |
|---|---|
| Colin Moore (Director of AI) | Onshore Resource (Lead Level) |

- Replace the resource name everywhere it appears: row labels, section headers, cell comments, notes
- Do NOT change the rate values, formulas, allocation percentages, or hours. Only the label changes.
- The India resource label ("India Resource (Mid-Level)" or "Offshore Resource (Mid-Level)") stays as-is

### Verification

After the change:
- Search the entire workbook for "Colin" — should return zero results
- Search for "Director of AI" — should return zero results
- All formulas and calculated values should be unchanged
- The POC Financial Summary numbers should be identical to before the change
