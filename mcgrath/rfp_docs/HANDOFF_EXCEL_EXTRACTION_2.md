# McGrath RFP Excel Extraction - Session 2 Handoff

**Date:** February 24, 2026
**Status:** ALL TABS COMPLETE

---

## Completed This Session

### High-Priority Tabs

| Tab | Output File | Rows | Structure |
|-----|-------------|------|-----------|
| General Requirements | `general_requirements_clean.csv` | 102 | Hierarchical: 16 sections, 86 requirements |
| SLA | `sla_clean.csv` | 9 | Matrix: categories x priority levels (P1-P4) |
| KPI | `kpi_clean.csv` | 9 | Simple table: KPI name + measurement method |

### Medium-Priority Tabs

| Tab | Output File | Rows | Structure |
|-----|-------------|------|-----------|
| RFP MGRC Overview | `rfp_overview.csv` | 48 | Prose/narrative with section headers |
| Pricing Here | `pricing_template.csv` | 14 | Template structure (empty - vendors fill in) |
| Next Steps | `next_steps.csv` | 17 | Process instructions and attachments list |

### Low-Priority Tabs

| Tab | Output File | Rows | Structure |
|-----|-------------|------|-----------|
| Experience & Methodology | `experience_methodology.csv` | 17 | 2 sections, 15 questions |
| Corporate Response Form | `corporate_response_form.csv` | 42 | Company profile questionnaire |

### Functions Added to scratchpad.py

```python
def clean_text(val)                      # Moved to module level for reuse
def extract_general_requirements_clean() # Hierarchical with section tracking
def extract_sla_clean()                  # Matrix format, rows 3-11
def extract_kpi_clean()                  # Simple 2-column table
def extract_overview_clean()             # Prose content from column B
def extract_pricing_template()           # Template structure with headers
def extract_next_steps_clean()           # Process instructions
def extract_experience_methodology()     # Questionnaire format
def extract_corporate_response()         # Company profile questionnaire
```

---

## All Extracted Files (Final)

```
mcgrath/rfp_docs/extracted/
├── specific_requirements_clean.csv   # 183 rows, 13 solutions (Session 1)
├── general_requirements_clean.csv    # 102 rows, 16 sections
├── sla_clean.csv                     # 9 rows, P1-P4 matrix
├── kpi_clean.csv                     # 9 rows, 8 KPIs
├── rfp_overview.csv                  # 48 rows, company info & intro
├── pricing_template.csv              # 14 rows, template structure
├── next_steps.csv                    # 17 rows, process & attachments
├── experience_methodology.csv        # 17 rows, 2 sections questionnaire
├── corporate_response_form.csv       # 42 rows, company profile template
└── architecture/                     # Screenshots (processed separately)
```

---

## Data Structures by Tab

### General Requirements
- **Columns:** Section, Number, Requirement, Type, MSP Response
- **Type values:** "Section Header" (whole numbers like 1, 2, 3) or "Requirement" (decimals like 1.1, 1.2)
- **Section propagation:** Requirements inherit section name from preceding header

### SLA
- **Columns:** Service Level Category, P1 (Critical), P2 (High), P3 (Medium), P4 (Low)
- **Categories:** Situation, Impacting Who, Affecting What, Customer Facing/Revenue Generation, Work Arounds, Expected Response, Measurements, Service Level Objective

### KPI
- **Columns:** KPI, How to Measure
- **8 KPIs:** Average resolution time, First contact resolution rate, Opened/closed ratio, SLA compliance rate, Response Time, MTTR, SLA Compliance %, Resource Utilization Rate

---

## Skipped Tabs

| Tab Name | Reason |
|----------|--------|
| MGRC Environment | Embedded Visio diagram - processed separately via screenshots |
| Vendor Q&A | Empty template with example rows only |

---

## How to Run Extractions

```bash
cd mcgrath/rfp_docs
python3 scratchpad.py
```

Change which function runs in the `if __name__ == "__main__":` block.

---

## Key Patterns Established

1. **Debug first** - Always run `debug_first_rows(sheet_name, max_cols)` before writing extraction code
2. **Limit columns** - Use `max_col` parameter to avoid 16384 phantom columns
3. **Clean text** - Use `clean_text()` to strip newlines and collapse whitespace
4. **Handle merged cells** - Track current section/solution and propagate to child rows
5. **Skip empty rows** - Check `if not any(values): continue`
6. **read_only=True, data_only=True** - Required flags for this workbook

---

## Quick Reference: Most Useful Files for RFP Response

| For This Task | Use This File |
|---------------|---------------|
| Answer specific technical requirements | `specific_requirements_clean.csv` |
| Answer general capability questions | `general_requirements_clean.csv` |
| Define SLA commitments | `sla_clean.csv` |
| Define KPI/metrics | `kpi_clean.csv` |
| Understand company context | `rfp_overview.csv` |
| Structure pricing response | `pricing_template.csv` |
| Understand submission process | `next_steps.csv` |
