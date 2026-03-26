# McGrath RFP Excel Extraction - Handoff Document

**Date:** February 24, 2026
**Status:** Specific Requirements COMPLETE, remaining tabs TODO
**Workbook:** `McGrath RentCorp_Managed Services Provider RFP_02172026.xlsx`

---

## What Was Done

### Successfully Extracted
- **Specific Requirements** tab → `extracted/specific_requirements_clean.csv`
- 183 rows, 13 unique Solutions, clean Yes/No checkbox values

### Remaining Tabs to Extract
| Tab Name | Rows | Cols | Priority | Notes |
|----------|------|------|----------|-------|
| General Requirements | 141 | 16384* | HIGH | *Col count is Excel max - has wide merged cells |
| SLA | 60 | 6 | HIGH | Service level targets |
| KPI | 30 | 29 | HIGH | Performance metrics |
| RFP MGRC Overview | 75 | 8 | MEDIUM | Summary/intro text |
| Experience & Methodology | 220 | 6 | LOW | Response template |
| Corporate Response Form | 55 | 8 | LOW | Template |
| Pricing Here | 200 | 34 | MEDIUM | Pricing grid |
| Next Steps | 50 | 8 | MEDIUM | Timeline/process |
| MGRC Environment | 214 | 10 | SKIP | Embedded Visio - processed separately via screenshot |
| Vendor Q&A | 210 | 6 | SKIP | Just a template with example rows |

---

## Exact Workflow That Worked

### Step 1: Create scratchpad.py

All Python work MUST use a proper scratchpad file. **NEVER use inline Python, heredocs, or python -c commands.**

The scratchpad is at: `mcgrath/rfp_docs/scratchpad.py`

### Step 2: Scan Sheets First

Run the `scan_sheets()` function to understand dimensions:

```python
def scan_sheets():
    """Quick scan of all sheets - should be fast."""
    wb = load_workbook(FILE, read_only=True, data_only=True)
    for name in wb.sheetnames:
        ws = wb[name]
        print(f"{name:<30} {ws.max_row:<10} {ws.max_column:<10}")
    wb.close()
```

### Step 3: Debug Header Rows

The Excel has merged header rows at the top. You MUST find where actual data starts.

```python
def debug_first_rows():
    """Debug: show first 15 rows to find header row."""
    wb = load_workbook(FILE, read_only=True, data_only=True)
    ws = wb["YOUR_SHEET_NAME"]

    for row_num, row in enumerate(ws.iter_rows(min_row=1, max_row=15, min_col=1, max_col=5), start=1):
        values = [str(cell.value)[:40] if cell.value else "---" for cell in row]
        print(f"Row {row_num:2d}: {values}")
    wb.close()
```

**For Specific Requirements:**
- Headers were in Row 4
- Data started in Row 5
- Column B = Solution, Column C = Category, Column D = Requirements

### Step 4: Handle Merged Cells (Solution Column)

The Solution column only has a value in the first row of each group. You must propagate it down:

```python
current_solution = ""

for row in ws.iter_rows(min_row=5, min_col=2, max_col=12):
    values = [cell.value for cell in row]

    # Get solution (column B = index 0)
    solution = values[0]
    if solution:
        current_solution = clean_text(solution)  # Update when we see a new one

    # Use current_solution for all rows
    clean_row = [current_solution, ...]
```

### Step 5: Clean Text (Remove Newlines)

Excel cells can have embedded newlines that break CSV parsing:

```python
def clean_text(val):
    """Clean text value - replace newlines, strip whitespace."""
    if val is None:
        return ""
    text = str(val).strip()
    text = text.replace('\n', ' ').replace('\r', ' ')
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text
```

### Step 6: Convert Checkboxes

Checkbox columns show as Python `True`/`False`. Convert to "Yes"/"No":

```python
for i in range(3, 10):  # Checkbox columns
    val = values[i]
    if val is True:
        clean_row.append("Yes")
    elif val is False:
        clean_row.append("No")
    else:
        clean_row.append("")
```

### Step 7: Skip Empty Rows

Check that the row has actual content (like a Category value):

```python
category = values[1]
if not category:
    continue  # Skip rows without category
```

---

## Problems Encountered and How They Were Fixed

### Problem 1: Script Hanging
**Symptom:** `process_excel.py` skill script ran for 5+ minutes without finishing.
**Cause:** Embedded Visio object and complex formatting in MGRC Environment tab.
**Fix:** Use direct openpyxl with `read_only=True, data_only=True`. Don't use the skill script for this workbook.

### Problem 2: Missing First Solution (Salesforce)
**Symptom:** First 6 rows had empty Solution column.
**Cause:** Started extracting at row 11 instead of row 5.
**Fix:** Used `debug_first_rows()` to find actual header row (row 4), then started at row 5.

### Problem 3: CSV Parsing Errors
**Symptom:** `cut` command showed fragments of text as "Solutions".
**Cause:** Embedded newlines in cells broke CSV row boundaries.
**Fix:** Added `clean_text()` function to replace `\n` and `\r` with spaces.

### Problem 4: Column Count 16384
**Symptom:** General Requirements shows 16384 columns.
**Cause:** Excel's max column count - likely has a merged cell or conditional formatting extending to the right.
**Fix:** Use `max_col=20` (or appropriate limit) when iterating rows.

---

## Current scratchpad.py State

The scratchpad has these functions:
- `scan_sheets()` - Quick dimension scan
- `extract_sheet_to_csv(sheet_name, max_cols)` - Raw extraction
- `extract_specific_requirements_clean()` - Cleaned extraction with all fixes
- `debug_first_rows()` - Header row finder

To run: `cd mcgrath/rfp_docs && python3 scratchpad.py`

Change which function runs in the `if __name__ == "__main__":` block.

---

## Your Task: Extract Remaining Tabs

### Priority 1: General Requirements

1. Add `debug_first_rows()` call for "General Requirements" sheet
2. Find where headers are and where data starts
3. Identify column structure (likely different from Specific Requirements)
4. Create `extract_general_requirements_clean()` function
5. Handle merged cells and newlines same as before
6. Use `max_col=20` to avoid the 16384 issue
7. Output to `extracted/general_requirements_clean.csv`

### Priority 2: SLA Tab

1. Debug first rows to find structure
2. Likely a simpler table format
3. Extract to `extracted/sla.csv`

### Priority 3: KPI Tab

1. Debug first rows
2. 29 columns suggests a wide table
3. Extract to `extracted/kpi.csv`

### Lower Priority: Other Tabs

- RFP MGRC Overview, Pricing Here, Next Steps
- Use same debug → extract pattern
- Output to `extracted/<tab_name>.csv`

---

## Output Location

All extracted CSVs go to: `mcgrath/rfp_docs/extracted/`

Current contents:
- `specific_requirements.csv` (raw, 188 rows)
- `specific_requirements_clean.csv` (cleaned, 183 rows) ← **USE THIS ONE**

---

## Key Reminders

1. **ALWAYS use scratchpad.py** - no inline Python ever
2. **read_only=True, data_only=True** - required for this workbook
3. **Debug first rows** before writing extraction code
4. **Propagate merged cell values** down to child rows
5. **Clean newlines** from text cells
6. **Limit max_col** if column count looks wrong
7. **Skip the MGRC Environment tab** - it's just an embedded Visio, processed separately

---

## Files Reference

```
mcgrath/rfp_docs/
├── McGrath RentCorp_Managed Services Provider RFP_02172026.xlsx  # Source
├── scratchpad.py                                                   # Extraction scripts
├── HANDOFF_EXCEL_EXTRACTION.md                                    # This file
└── extracted/
    ├── specific_requirements.csv                                  # Raw (don't use)
    └── specific_requirements_clean.csv                            # Clean (USE THIS)
```
