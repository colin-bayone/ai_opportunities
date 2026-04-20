# Excel POC Pricing Specification: Lam Research

**Purpose:** This document is a complete specification for adapting the BayOne Project Costing Template to model the Lam Research Confidential Information Detection POC. Open the template workbook (`ProjectCostingTemplate.xlsx`) and follow these instructions exactly.

**Audience:** Claude (or any assistant) operating inside Excel.

---

## What To Do

The template already has the full workbook structure (Instructions, Personnel, Project Inputs, POC, Scenarios, Throughput, Comparison/Charts). For this engagement, only the **Personnel**, **Project Inputs**, and **POC** tabs need to be populated. The Scenarios and Throughput tabs are not used because this is a POC-only engagement with no full-scale project to model yet.

---

## Tab: Personnel

### Update Personnel Rates

Clear the existing dummy data and enter:

| Resource | Working Location | Rate Type | Base Rate | Load Factor | Loaded Rate | Loaded Monthly |
|---|---|---|---|---|---|---|
| Colin Moore (Director of AI) | Onshore (US) | Annual | $180,000 | 1.20 | =Base*1.20 | =Loaded/12 |
| India Resource (Mid-Level) | Offshore (India) | Hourly | $27.50 | 1.20 | =Base*1.20 | =Loaded Hourly * HoursPerMonth |

**Constants:**
- Working Hours per Month: 173.33
- Load Factor: 1.20 (same for all resources)

**Expected calculated values:**
- Colin: Loaded Annual $216,000, Loaded Monthly $18,000
- India Resource: Loaded Hourly $33.00, Loaded Monthly $5,720 (at 173.33 hrs/mo)

---

## Tab: Project Inputs

### Section: Engagement Parameters

| Field | Value | Notes |
|---|---|---|
| Client | Lam Research | |
| Engagement | Confidential Information Detection POC | |
| Billing Model | Billed to Client | Not absorbed, not free |
| Billed Amount | $10,000 | Fixed price, outcome-based |

### Section: POC Parameters

| Field | Value | Notes |
|---|---|---|
| POC Duration (weeks) | 3 | One week discovery + two weeks build |
| POC Purpose | Detection methodology demonstration | |
| POC Billing | Billed to Client | |
| POC Amount | $10,000 | Same as engagement total (this IS the engagement) |

### Section: Margin Thresholds

| Field | Value |
|---|---|
| Target Margin | 40% |
| Floor Margin | 30% |

### Section: Risk Reserve

| Field | Value |
|---|---|
| Risk Reserve % | 25% |

---

## Tab: POC

This is the primary tab for this engagement. Adapt it to match the Lam POC structure.

### Section A: POC Overview

| Field | Value |
|---|---|
| Purpose | Confidential Information Detection: Demonstrate improved detection methodology for customer-confidential entities in Escalation Solver |
| Duration (weeks) | 3 |
| Billing Model | Billed to Client |
| Billed Amount (if applicable) | $10,000 |

### Section B: POC Team and Cost

| Resource | Working Location | Rate Type | Base Rate | Load Factor | Loaded Rate | Loaded Monthly | POC Allocation | Hours | Total Cost |
|---|---|---|---|---|---|---|---|---|---|
| Colin Moore (Director of AI) | Onshore (US) | Annual | $180,000 | 1.20 | $216,000 | $18,000 | 10% | 12 | =Loaded Hourly * Hours |
| India Resource (Mid-Level) | Offshore (India) | Hourly | $27.50 | 1.20 | $33.00 | $5,720 | 100% | 120 | =Loaded Hourly * Hours |

**Formulas and notes:**
- Colin's hours: 3 weeks * 40 hrs/week * 10% = 12 hours
- Colin's loaded hourly: $216,000 / 2,080 = $103.85/hr
- Colin's total cost: $103.85 * 12 = $1,246.20
- India resource hours: 3 weeks * 40 hrs/week * 100% = 120 hours
- India resource total cost: $33.00 * 120 = $3,960.00

### Section C: POC Financial Summary

| Line Item | Formula | Expected Value |
|---|---|---|
| Total POC Cost | Sum of all resource total costs | $5,206.20 |
| Billing Model | "Billed to Client" | |
| Billed Amount | From Section A | $10,000 |
| Risk Reserve (25%) | Total POC Cost * 25% | $1,301.55 |
| Loaded Cost | Total POC Cost + Risk Reserve | $6,507.75 |
| Net POC (Revenue minus Loaded) | Billed Amount - Loaded Cost | $3,492.25 |
| Margin on Base (%) | (Billed - Base) / Billed | 47.9% |
| Margin on Loaded (%) | (Billed - Loaded) / Billed | 34.9% |
| Above 30% Floor (loaded)? | IF(Margin Loaded >= 30%, "YES", "NO") | YES |

**Notes to display below the financial summary:**
- "POC costs are the actual personnel cost to BayOne."
- "Risk reserve is a 25% buffer on base cost for scope variance."
- "Net POC shows profit after risk reserve. If risk reserve is not consumed, effective margin rises to 47.9%."

### Section D: POC Deliverables Detail

List the following deliverables:

1. Exploratory data analysis report (EDA)
2. Data quality assessment with accuracy ceiling determination
3. Working detection demonstration
4. Detection benchmarking against prior effort baseline
5. Evaluation protocol documentation
6. Methodology documentation (layered detection approach)
7. Scaling path for additional entity types, fields, and applications
8. Reference data refinement recommendations

---

## Formatting

Follow the existing template formatting conventions:

- Section headers: Bold, dark purple background (#2e1065), white text
- Sub-headers: Bold, light purple background (#ede9fe), dark text
- Input cells (yellow background): POC Allocation %, Billed Amount, Duration
- Calculated cells (no background or light gray): all formula-driven fields
- Currency: Accounting format, 2 decimal places for hourly, 0 for totals and monthly
- Percentages: 1 decimal place
- Conditional formatting on margin %: green if >= 40%, amber if 30-39.9%, red if < 30%
- "YES"/"NO" cells: green/red conditional formatting

---

## Clearing the Template: Dummy Data Removal

The template ships with dummy data (Acme Corp, 120 screens, $350K, etc.) across all tabs. This data MUST be cleared so the workbook does not appear to contain full engagement decisions that have not been made. However, formulas and tab structure must be preserved for future use when the full engagement is scoped.

### Instructions for Clearing

**General principle:** Clear the VALUES in input cells (yellow-highlighted cells, data entry fields) but do NOT delete rows, columns, or formulas. Formula cells will automatically show $0, 0%, or blank once their input dependencies are cleared. This is the correct behavior.

### Tab: Instructions
- Update the engagement name from the dummy client to "Lam Research - Confidential Information Detection"
- Update the date to April 2026

### Tab: Personnel
- **Clear all dummy resource rows** (Acme Corp resources)
- **Replace with** the two Lam POC resources (Colin Moore and India Resource) as specified in the Personnel section above
- Keep the table structure, headers, and formulas intact

### Tab: Project Inputs
- **Clear all full-engagement parameters:** revenue, total deliverables/screens, hours per deliverable, full engagement duration, scenario staffing numbers, travel parameters, hardware/consumables
- **Populate only** the POC-related fields and engagement identification as specified in the Project Inputs section above
- For any full-engagement fields that cannot be blanked without breaking formulas, enter 0 as the value
- The section headers and structure remain in place

### Tab: POC
- **Clear all dummy POC data** (Acme Corp POC content)
- **Populate with** the Lam POC data as specified in the POC section above
- This is the primary working tab for this engagement

### Tab: Scenarios
- **Clear all input values** (staffing numbers, durations, resource assignments) by setting them to 0 or blank
- **Do NOT delete any rows, columns, or formulas.** Formula cells will show $0 or 0%, which is correct.
- **Add a note in cell A1** (merged across columns, yellow background, bold): "PENDING: Full engagement scope not yet defined. This tab will be populated after POC completion and scope agreement with Lam Research."

### Tab: Throughput
- **Clear all input values** by setting them to 0 or blank
- **Preserve all formulas and structure**
- **Add the same pending note in cell A1** as the Scenarios tab

### Tab: Comparison/Charts
- **Clear all input values** by setting them to 0 or blank
- **Preserve all formulas and structure.** Charts will display empty or zero, which is correct.
- **Add the same pending note in cell A1** as the Scenarios tab

### Why This Approach

- The workbook remains a single, complete artifact that tracks the full engagement lifecycle from POC through full scope
- When the full engagement is scoped after the POC, the same workbook is used by populating the Scenarios, Throughput, and Comparison tabs with real data
- No formulas need to be rebuilt because the structure was preserved
- Anyone opening the workbook sees clearly which tabs are active (Personnel, Project Inputs, POC) and which are pending (Scenarios, Throughput, Comparison)

---

## Validation Checklist

After populating, verify these values:

| Check | Expected |
|---|---|
| Colin loaded monthly | $18,000 |
| Colin loaded hourly | $103.85 |
| Colin POC hours | 12 |
| Colin POC cost | $1,246.20 |
| India loaded hourly | $33.00 |
| India loaded monthly | $5,720 |
| India POC hours | 120 |
| India POC cost | $3,960.00 |
| Total POC base cost | $5,206.20 |
| Risk reserve (25%) | $1,301.55 |
| Loaded cost | $6,507.75 |
| Billed amount | $10,000 |
| Net POC (on loaded) | $3,492.25 |
| Margin % (base) | 47.9% |
| Margin % (loaded) | 34.9% |
| Above 30% floor? | YES |
