# Project Costing Template -- Excel Workbook Specification

Build a professional, reusable Excel workbook that BayOne Solutions uses for pricing outcome-based consulting engagements. This is a **template with sample data**, not a live project. The sample data demonstrates how the sheet works. Users will clear the sample data and enter their own project details.

---

## Workbook Structure

Create 7 tabs in this order:

1. **Instructions** -- How to use this workbook
2. **Inputs** -- All configurable parameters
3. **Scenario A** -- First delivery scenario (shorter timeline, more resources)
4. **Scenario B** -- Second delivery scenario (longer timeline, fewer resources)
5. **Discount Analysis** -- Price sensitivity for the longer-timeline scenario
6. **Comparison** -- Side-by-side dashboard
7. **Throughput** -- Delivery capacity model

---

## Tab 1: Instructions

This tab explains the workbook to someone who has never seen it before. Use clean formatting (no heavy styling, just clear text with headers).

### Content

```
PROJECT COSTING WORKBOOK
BayOne Solutions -- Outcome-Based Engagement Pricing

PURPOSE
This workbook models the internal cost of delivering an outcome-based consulting engagement.
It helps you determine whether a quoted price supports your target margin at a given team
structure and timeline.

It models two delivery scenarios (shorter vs. longer timeline) and a discount sensitivity
analysis for the longer-timeline option.

HOW TO USE
1. Start on the INPUTS tab. Fill in your project details, personnel rates, and scenario parameters.
2. The SCENARIO A and SCENARIO B tabs auto-calculate based on your inputs.
3. Use the DISCOUNT ANALYSIS tab to see how much room you have to negotiate on price.
4. The COMPARISON tab gives you a side-by-side view of all scenarios.
5. The THROUGHPUT tab validates whether your team can actually deliver the scope in the timeline.

KEY CONCEPTS

  Allocation %
  This is a COST ALLOCATION mechanism, not a productivity measure. If a person is 50% allocated,
  it means 50% of their cost is charged to this project. The other 50% is charged elsewhere.
  The person still works full-time. Allocation splits cost across projects.

  Rate Type (Annual vs. Hourly)
  Each resource is either salaried (Annual) or contracted (Hourly). This determines how the
  Loaded Monthly cost is calculated:
    - Annual: Loaded Annual / 12
    - Hourly: Loaded Hourly × Working Hours per Month

  Risk Reserve
  A percentage buffer added on top of base cost to account for scope creep, technical complexity,
  and unknowns. This is not a guaranteed spend. It sits inside the gross margin as protection.
  If nothing goes wrong, the risk reserve becomes additional margin.

  Stabilization & Acceptance
  The final phase of each scenario. This is NOT a separate QA phase. Development is agile and
  testing happens throughout. This buffer covers production-level validation after client
  integration, bug fixes, stakeholder demos, and final acceptance.

  Base Cost vs. Loaded Cost
    - Base Cost = Personnel + Travel + Hardware/Consumables (what you expect to spend)
    - Loaded Cost = Base Cost + Risk Reserve (worst-case budget)
    - Margin on Base = best case (if risk doesn't materialize)
    - Margin on Loaded = worst case (if full risk reserve is consumed)

EDITABLE FIELDS
  Cells with a LIGHT YELLOW background are user-editable inputs.
  All other cells contain formulas. Do not overwrite formula cells.

ADDING RESOURCES
  To add a new resource, insert a row in the Personnel Rates table on the Inputs tab.
  Set the Rate Type to Annual or Hourly. The formulas will handle the rest.
  Then add a corresponding row on each Scenario tab.

SAMPLE DATA
  This workbook ships with sample data for a fictional engagement. Clear the sample data
  on the Inputs tab and replace with your project details. All scenario tabs will update
  automatically.
```

### Formatting
- Title "PROJECT COSTING WORKBOOK" in 16pt bold
- "BayOne Solutions" subtitle in 12pt, purple text (#5b21b6)
- Section headers (PURPOSE, HOW TO USE, etc.) in 12pt bold
- Body text in 11pt Calibri, comfortable line spacing
- No borders, no cell coloring -- clean document-style layout
- Column A width: 100+
- Print-friendly: fits on 1-2 pages

---

## Tab 2: Inputs

### Section A: Project Details (starting at A1)

| | A | B |
|---|---|---|
| 1 | **Project Details** | |
| 2 | Project Name | Acme Corp Platform Migration |
| 3 | Client | Acme Corporation |
| 4 | Engagement Type | Legacy Platform Conversion |
| 5 | Deliverable | 120 screens, full-stack (UI + backend) |
| 6 | Pricing Model | Outcome-based, fixed price |

*These are reference fields only. Not used in calculations.*

### Section B: Personnel Rates (starting at A9)

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 9 | **Personnel Rates** | | | | | | | |
| 10 | *Resource* | *Rate Type* | *Base Rate* | *Load Factor* | *Loaded Rate* | *Loaded Monthly* | *Allocation %* | *Effective Monthly* |
| 11 | Project Lead | Annual | $150,000 | 1.20 | =C11*D11 | =IF(B11="Annual",E11/12,E11*HoursPerMonth) | 25% | =F11*G11 |
| 12 | Senior Engineer (US) | Annual | $120,000 | 1.20 | =C12*D12 | =IF(B12="Annual",E12/12,E12*HoursPerMonth) | 100% | =F12*G12 |
| 13 | Offshore Engineer 1 | Hourly | $30.00 | 1.20 | =C13*D13 | =IF(B13="Annual",E13/12,E13*HoursPerMonth) | 100% | =F13*G13 |
| 14 | Offshore Engineer 2 | Hourly | $25.00 | 1.20 | =C14*D14 | =IF(B14="Annual",E14/12,E14*HoursPerMonth) | 100% | =F14*G14 |
| 15 | Offshore Engineer 3 | Hourly | $28.00 | 1.20 | =C15*D15 | =IF(B15="Annual",E15/12,E15*HoursPerMonth) | 100% | =F15*G15 |

**Named Ranges:**
- `HoursPerMonth` = B20
- `Revenue` = B24
- `TotalScreens` = B25 (or equivalent deliverable units)
- `RiskReserve` = B28

**Column formatting:**
- Rate Type (col B): Data validation dropdown: `Annual`, `Hourly`. Light yellow background (#fef9c3).
- Base Rate (col C): Accounting format. Light yellow background.
- Load Factor (col D): Number, 2 decimals. Light yellow background.
- Loaded Rate (col E): Accounting format. Light gray background (calculated).
- Loaded Monthly (col F): Accounting format. Light gray background (calculated).
- Allocation % (col G): Percentage, 0 decimals. Light yellow background.
- Effective Monthly (col H): Accounting format. Light gray background (calculated).

### Section C: Constants (starting at A18)

| | A | B |
|---|---|---|
| 18 | **Constants** | |
| 19 | Load Factor (default) | 1.20 |
| 20 | Working Hours per Month | 173.33 |

Cell B20: Light yellow background. Cell comment: *"Standard: 173.33 (52w × 40h / 12). Adjust to 160-168 for realistic availability after holidays/PTO."*

### Section D: Engagement Parameters (starting at A23)

| | A | B |
|---|---|---|
| 23 | **Engagement Parameters** | |
| 24 | Revenue | $350,000 |
| 25 | Total Deliverable Units (screens, modules, etc.) | 120 |
| 26 | Hours per Unit (estimated, with tooling) | 10 |
| 27 | Total Delivery Hours | =B25*B26 |
| 28 | Risk Reserve % | 25% |
| 29 | POC Duration (months) | 1 |
| 30 | POC Resource | Project Lead |
| 31 | POC Hours | 60 |
| 32 | POC Cost (absorbed) | =B31*(Inputs!F11*12/2080) |

All cells in column B with user-entered values: light yellow background.

### Section E: Travel & Expenses (starting at A35)

| | A | B |
|---|---|---|
| 35 | **Travel & Expenses** | |
| 36 | Cost per Trip | $2,500 |
| 37 | Trips (Scenario A) | 2 |
| 38 | Trips (Scenario B) | 3 |
| 39 | Travel Destination | Client HQ |

### Section F: Hardware & Consumables (starting at A42)

| | A | B |
|---|---|---|
| 42 | **Hardware & Consumables** | |
| 43 | Monthly Tools & Subscriptions | $0 |
| 44 | One-Time Equipment | $0 |

### Section G: Margin Thresholds (starting at A47)

| | A | B |
|---|---|---|
| 47 | **Margin Thresholds** | |
| 48 | Scenario A Target (ideal) | 40% |
| 49 | Scenario A Floor | 40% |
| 50 | Scenario B Target (ideal) | 40% |
| 51 | Scenario B Floor (minimum acceptable) | 30% |

### Section H: Scenario Parameters (starting at A54)

| | A | B | C |
|---|---|---|---|
| 54 | **Scenario Parameters** | *Scenario A* | *Scenario B* |
| 55 | Scenario Label | Q3 Delivery | Q4 Delivery |
| 56 | Offshore Engineers (dev phase) | 5 | 2 |
| 57 | Offshore Engineers (stabilization) | 4 | 2 |
| 58 | Dev Months (post-POC) | 2 | 5 |
| 59 | Stabilization & Acceptance Months | 1 | 2 |
| 60 | Total Post-POC Months | =B58+B59 | =C58+C59 |

---

## Tab 3: Scenario A

### Title Row
Row 1: "Scenario A: [Scenario A Label from Inputs] -- [Scenario A description]" merged, bold, dark purple bg (#2e1065), white text, 14pt.

Row 2: Subtitle with timeline description in gray italic.

### Section A: Monthly Cost Breakdown (starting at row 4)

Create columns for each month of the scenario. POC month + Dev months + Stabilization months.

For the sample data (Scenario A = 1 POC + 2 dev + 1 stabilization = 4 months):

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 4 | *Resource* | *Month 1 (POC)* | *Month 2* | *Month 3* | *Month 4 (Stab.)* | *Total* |
| 5 | Project Lead | =POCCost | =EffMonthly_Lead | =EffMonthly_Lead | =EffMonthly_Lead | =SUM |
| 6 | Senior Engineer (US) | 0 | =EffMonthly_USEng | =EffMonthly_USEng | =EffMonthly_USEng | =SUM |
| 7 | Offshore (dev) | 0 | =EffMonthly_Off × ScA_OffDev | =same | 0 | =SUM |
| 8 | Offshore (stab.) | 0 | 0 | 0 | =EffMonthly_Off × ScA_OffStab | =SUM |
| 9 | **Personnel Total** | =SUM(B5:B8) | =SUM | =SUM | =SUM | =SUM(F5:F8) |
| 10 | **Cumulative** | =B9 | =B10+C9 | =C10+D9 | =D10+E9 | |

*Note: Offshore rows use the Effective Monthly for the offshore resource multiplied by the number of engineers from the Inputs tab. If multiple offshore resources exist at different rates, either use an average or create separate rows per resource.*

### Section B: Financial Summary (starting at A13)

| | A | B |
|---|---|---|
| 13 | **Financial Summary** | |
| 14 | Revenue | =Revenue |
| 15 | Personnel Cost | =F9 |
| 16 | Travel & Expenses | =CostPerTrip * ScA_Trips |
| 17 | Hardware & Consumables | =OneTimeEquipment + (MonthlyTools * ScA_TotalMonths) |
| 18 | **Base Cost** | =SUM(B15:B17) |
| 19 | Risk Reserve | =B18 * RiskReserve |
| 20 | **Loaded Cost** | =B18+B19 |
| 21 | | |
| 22 | Margin on Loaded Cost ($) | =B14-B20 |
| 23 | **Margin on Loaded Cost (%)** | =B22/B14 |
| 24 | Margin on Base Cost ($) | =B14-B18 |
| 25 | **Margin on Base Cost (%)** | =B24/B14 |
| 26 | | |
| 27 | Above Floor? (loaded) | =IF(B23>=ScA_Floor,"YES","NO") |
| 28 | Above Floor? (base) | =IF(B25>=ScA_Floor,"YES","NO") |

### Section C: Per-Unit Economics (starting at A31)

| | A | B |
|---|---|---|
| 31 | **Per-Unit Economics** | |
| 32 | Cost per Unit (base) | =B18/TotalUnits |
| 33 | Cost per Unit (loaded) | =B20/TotalUnits |
| 34 | Revenue per Unit | =B14/TotalUnits |
| 35 | Margin per Unit | =B34-B33 |

### Section D: Staffing Summary (starting at A38)

| | A | B |
|---|---|---|
| 38 | **Staffing Summary** | |
| 39 | Total Duration (months) | =1+ScA_TotalPostPOC |
| 40 | Peak Headcount | (count of active resources at peak) |
| 41 | Peak Monthly Burn | =MAX of monthly totals |
| 42 | Avg Monthly Burn | =F9/B39 |

---

## Tab 4: Scenario B

Identical structure to Scenario A, but referencing Scenario B parameters from Inputs.

For the sample data (Scenario B = 1 POC + 5 dev + 2 stabilization = 8 months), the monthly breakdown has 8 columns instead of 4.

US Engineer allocation during stabilization: use 50% of their Effective Monthly (configurable).

---

## Tab 5: Discount Analysis

### Title: "Discount Sensitivity -- Scenario B Timeline Only"

### Section A: Cost Reference

| | A | B | C |
|---|---|---|---|
| 3 | *Base Cost (from Scenario B):* | ='Scenario B'!B18 | |
| 4 | *Loaded Cost (from Scenario B):* | ='Scenario B'!B20 | |

### Section B: Discount Table (starting at row 6)

| | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 6 | *Price* | *Discount %* | *Margin $ (loaded)* | *Margin % (loaded)* | *Margin $ (base)* | *Margin % (base)* | *Verdict* |
| 7 | =Revenue | 0% | =A7-$B$4 | =C7/A7 | =A7-$B$3 | =E7/A7 | =IF(D7>=ScB_Floor,"SAFE","BELOW FLOOR") |
| 8 | =Revenue*0.95 | 5% | ... | ... | ... | ... | ... |
| 9 | =Revenue*0.90 | 10% | ... | ... | ... | ... | ... |
| 10 | =Revenue*0.85 | 15% | ... | ... | ... | ... | ... |
| 11 | =Revenue*0.80 | 20% | ... | ... | ... | ... | ... |
| 12 | =Revenue*0.75 | 25% | ... | ... | ... | ... | ... |
| 13 | =Revenue*0.70 | 30% | ... | ... | ... | ... | ... |

### Section C: Floor Price Calculation

| | A | B |
|---|---|---|
| 16 | **Floor Prices** | |
| 17 | Floor at margin target (loaded) | =LoadedCost/(1-ScB_Floor) |
| 18 | Max discount % (loaded) | =1-(B17/Revenue) |
| 19 | Floor at margin target (base) | =BaseCost/(1-ScB_Floor) |
| 20 | Max discount % (base) | =1-(B19/Revenue) |

### Conditional formatting on discount table
- Margin % (loaded) >= 40%: green text, green row background (#dcfce7)
- 30-39.9%: amber text, yellow row (#fef9c3)
- < 30%: red text, red row (#fee2e2)
- Verdict column: "SAFE" = green, "BELOW FLOOR" = red bold

---

## Tab 6: Comparison

### Title: "Scenario Comparison Dashboard"

Side-by-side table pulling from Scenario A, Scenario B, and Discount Analysis:

| Metric | Scenario A | Scenario B | Discount (floor) |
|---|---|---|---|
| Revenue | (from A) | (from B) | (from Discount floor) |
| Base Cost | | | |
| Risk Reserve | | | |
| Loaded Cost | | | |
| Margin % (loaded) | | | |
| Margin % (base) | | | |
| Duration | | | |
| Peak Headcount | | | |
| Cost per Unit | | | |
| Revenue per Unit | | | |
| Avg Monthly Burn | | | |
| Above Floor? | | | |

### Column header colors
- Scenario A: medium purple (#7c3aed), white text
- Scenario B: dark blue (#1e40af), white text
- Discount: dark amber (#92400e), white text

---

## Tab 7: Throughput

### Capacity validation for each scenario.

| | A | B |
|---|---|---|
| 3 | Total Deliverable Units | =TotalUnits |
| 4 | Hours per Unit | =HoursPerUnit |
| 5 | Total Hours Needed | =TotalHours |

### Per-scenario capacity table

For each scenario, calculate:
- Engineers × HoursPerMonth × Dev Months = Total Available Hours
- Total Available Hours / Hours per Unit = Screens Possible
- Utilization % = Screens Needed / Screens Possible

Color the utilization cell: green (<80%), yellow (80-95%), red (>95%).

---

## Global Formatting Rules

### Colors (BayOne Brand Palette)

| Use | Hex |
|---|---|
| Dark purple (tab titles, main headers) | #2e1065 |
| Medium purple (section headers) | #5b21b6 |
| Light purple (accent/summary rows) | #ede9fe |
| Very light purple | #f5f3ff |
| Editable cells background | #fef9c3 (light yellow) |
| Calculated cells background | #f1f5f9 (light gray) |
| Green (positive/pass) | #dcfce7 |
| Red (negative/fail) | #fee2e2 |
| Yellow (caution) | #fef9c3 |
| Border color | #e2e8f0 |

### Typography
- Font: Calibri (or Aptos)
- Tab titles: 14pt bold, dark purple bg, white text
- Section headers: 12pt bold, medium purple bg, white text
- Column headers: 11pt bold, light purple bg
- Data: 11pt regular
- Notes: 10pt italic gray

### Number Formats
- Currency (large): Accounting, 0 decimals
- Currency (hourly): Accounting, 2 decimals
- Percentages: 1 decimal place
- Headcount/months: Number, 0 decimals

### Print Setup
- All tabs: Landscape
- Fit to 1 page wide
- Header: "BayOne Solutions -- Confidential" (left), tab name (center)
- Footer: Page number (right)
- Margins: 0.5" all sides

### Cell Protection
- Light yellow cells: unlocked (user-editable)
- All other cells: locked (formulas)
- Sheet protection ON with password "" (empty -- protection is a safety net, not security)

### Data Validation
- Rate Type column: dropdown list `Annual, Hourly`
- Allocation % column: 0% to 100%
- Risk Reserve: 0% to 50%
- Load Factor: 1.00 to 2.00

---

## Sample Data Summary (For Validation)

These are the expected outputs from the sample data above. Use them to verify the workbook is calculating correctly.

### Inputs
- Revenue: $350,000
- Units: 120 screens at 10 hrs each = 1,200 total hours
- Risk Reserve: 25%
- Project Lead: $150K annual, 1.20 load, 25% allocated = $3,750/mo effective
- US Engineer: $120K annual, 1.20 load, 100% allocated = $12,000/mo effective
- Offshore 1: $30/hr, 1.20 load, 100% = $36/hr loaded × 173.33 = $6,240/mo effective
- Offshore 2: $25/hr, 1.20 load, 100% = $30/hr loaded × 173.33 = $5,200/mo effective
- Offshore 3: $28/hr, 1.20 load, 100% = $33.60/hr loaded × 173.33 = $5,824/mo effective
- Travel: $2,500/trip, 2 trips (A), 3 trips (B)
- Hardware: $0

### Scenario A (3 months post-POC: 2 dev + 1 stab, 5 offshore dev, 4 offshore stab)
- POC cost: ~$5,192 (60 hrs × $86.54/hr loaded for lead)
- Month 2-3 personnel: Lead $3,750 + US $12,000 + 5 offshore (use avg ~$5,755) $28,775 = $44,525/mo × 2 = $89,050
- Month 4 (stab): Lead $3,750 + US $12,000 + 4 offshore avg $23,020 = $38,770
- Personnel total: ~$5,192 + $89,050 + $38,770 = ~$133,012
- Travel: $5,000
- Hardware: $0
- Base cost: ~$138,012
- Risk reserve (25%): ~$34,503
- Loaded cost: ~$172,515
- Margin (loaded): ~50.7%

### Scenario B (7 months post-POC: 5 dev + 2 stab, 2 offshore)
- POC: ~$5,192
- Months 2-6 (dev): Lead $3,750 + US $12,000 + 2 offshore avg $11,510 = $27,260/mo × 5 = $136,300
- Months 7-8 (stab): Lead $3,750 + US $6,000 (50%) + 2 offshore $11,510 = $21,260/mo × 2 = $42,520
- Personnel total: ~$184,012
- Travel: $7,500
- Base: ~$191,512
- Risk (25%): ~$47,878
- Loaded: ~$239,390
- Margin (loaded): ~31.6%

*Note: These are approximate. Minor rounding differences are expected. The workbook should match within $100.*
