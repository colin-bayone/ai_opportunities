# Excel Pricing Model Specification

**Purpose:** This document is a complete specification for building a professional Excel workbook that models three pricing scenarios for the Cisco EPNM-to-EMS UI Conversion engagement. It contains every input, formula, layout, and formatting instruction needed to build the workbook from scratch.

**Audience:** Claude (or any assistant) operating inside Excel. Follow this spec exactly.

---

## Workbook Structure

Create 6 tabs in this order:

1. **Inputs** -- All configurable parameters
2. **July Delivery** -- Scenario 1: compressed timeline, heavy parallelization
3. **December Delivery** -- Scenario 2: comfortable timeline, lean team
4. **Discount Analysis** -- Scenario 3: December timeline with price sensitivity
5. **Comparison** -- Side-by-side dashboard of all three scenarios
6. **Throughput** -- Screen conversion capacity model

---

## Tab 1: Inputs

### Layout

This sheet is the single source of truth. Every other tab references cells on this sheet. Use named ranges for all inputs to make formulas readable.

### Section A: Personnel Rates (starting at A1)

| | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | **Personnel Rates** | | | | |
| 2 | *Resource* | *Base Annual/Hourly* | *Load Factor* | *Loaded Annual/Hourly* | *Loaded Monthly* |
| 3 | Colin Moore (Director of AI) | $180,000 | 1.20 | =B3*C3 | =D3/12 |
| 4 | US Engineer A | $105,000 | 1.20 | =B4*C4 | =D4/12 |
| 5 | US Engineer B | $160,000 | 1.20 | =B5*C5 | =D5/12 |
| 6 | Offshore Engineer (low) | $20.00 | 1.20 | =B6*C6 | =D6*F$10 |
| 7 | Offshore Engineer (mid) | $27.50 | 1.20 | =B7*C7 | =D7*F$10 |
| 8 | Offshore Engineer (high) | $35.00 | 1.20 | =B8*C8 | =D8*F$10 |

| | F | |
|---|---|---|
| 10 | *Working Hours/Month* | 173.33 |

**Named Ranges:**
- `ColinMonthly` = E3
- `USEngAMonthly` = E4
- `USEngBMonthly` = E5
- `OffshoreMonthly` = E7 (use mid-range as default)
- `HoursPerMonth` = F10
- `LoadFactor` = C3 (same for all)

### Section B: Engagement Parameters (starting at A13)

| | A | B |
|---|---|---|
| 13 | **Engagement Parameters** | |
| 14 | Revenue | $500,000 |
| 15 | Total Screens | 250 |
| 16 | Hours per Screen (AI-assisted) | 8 |
| 17 | Total Conversion Hours | =B15*B16 |
| 18 | Risk Reserve % | 25% |
| 19 | Colin Allocation % | 30% |
| 20 | POC Hours (Colin, absorbed) | 80 |
| 21 | POC Cost | =B20*(ColinMonthly*12/2080) |

**Named Ranges:**
- `Revenue` = B14
- `TotalScreens` = B15
- `HoursPerScreen` = B16
- `TotalHours` = B17
- `RiskReserve` = B18
- `ColinAlloc` = B19
- `POCHours` = B20
- `POCCost` = B21

### Section C: Margin Thresholds (starting at A24)

| | A | B |
|---|---|---|
| 24 | **Margin Thresholds** | |
| 25 | July Target (ideal) | 40% |
| 26 | July Floor (do not budge) | 40% |
| 27 | December Target (ideal) | 40% |
| 28 | December Floor (minimum acceptable) | 30% |

**Named Ranges:**
- `JulyFloor` = B26
- `DecFloor` = B28

### Section D: Scenario Parameters (starting at A31)

| | A | B | C |
|---|---|---|---|
| 31 | **Scenario Staffing** | *July* | *December* |
| 32 | Offshore Engineers (factory) | 8 | 3 |
| 33 | Offshore Engineers (QA) | 8 | 3 |
| 34 | US Engineer Rate | USEngAMonthly | USEngAMonthly |
| 35 | US QA Allocation % | 100% | 50% |
| 36 | Dev Months (post-POC) | 2 | 6 |
| 37 | QA Months | 1 | 2 |
| 38 | Total Post-POC Months | =B36+B37 | =C36+C37 |

**Named Ranges:**
- `JulyOffshore` = B32
- `JulyQAOffshore` = B33
- `DecOffshore` = C32
- `DecQAOffshore` = C33
- `JulyDevMonths` = B36
- `JulyQAMonths` = B37
- `DecDevMonths` = C36
- `DecQAMonths` = C37

### Formatting for Inputs Tab

- Header row (row 1, 13, 24, 31): Bold, dark purple background (#2e1065), white text, font size 13
- Sub-headers (row 2, etc.): Bold, light purple background (#ede9fe), dark text, font size 11
- Data cells: Regular weight, font size 11
- Currency cells: Accounting format, 0 decimal places for annual/monthly, 2 decimals for hourly
- Percentage cells: Percentage format, 0 decimal places
- All borders: Thin light gray (#e2e8f0)
- Column widths: A=35, B=18, C=12, D=18, E=18, F=18
- Font: Calibri or Aptos throughout

---

## Tab 2: July Delivery

### Section A: Monthly Cost Breakdown (starting at A1)

Title row: "Scenario 1: July Delivery -- Compressed Timeline" in row 1, merged across columns, bold, dark purple bg, white text, font 14.

Subtitle row 2: "April POC --> May-Jun Factory --> Jul QA/Acceptance" in gray italic.

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 4 | *Resource* | *April (POC)* | *May* | *Jun* | *Jul (QA)* | *Total* |
| 5 | Colin Moore | =POCCost | =ColinMonthly*ColinAlloc | =ColinMonthly*ColinAlloc | =ColinMonthly*ColinAlloc | =SUM(B5:E5) |
| 6 | US Engineer A | 0 | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly | =SUM(B6:E6) |
| 7 | Offshore (factory) | 0 | =OffshoreMonthly*JulyOffshore | =OffshoreMonthly*JulyOffshore | 0 | =SUM(B7:E7) |
| 8 | Offshore (QA) | 0 | 0 | 0 | =OffshoreMonthly*JulyQAOffshore | =SUM(B8:E8) |
| 9 | **Monthly Total** | =SUM(B5:B8) | =SUM(C5:C8) | =SUM(D5:D8) | =SUM(E5:E8) | =SUM(F5:F8) |
| 10 | **Cumulative** | =B9 | =B10+C9 | =C10+D9 | =D10+E9 | |

### Section B: Financial Summary (starting at A13)

| | A | B |
|---|---|---|
| 13 | **Financial Summary** | |
| 14 | Revenue | =Revenue |
| 15 | Base Cost | =F9 |
| 16 | Risk Reserve (25%) | =B15*RiskReserve |
| 17 | **Loaded Cost** | =B15+B16 |
| 18 | | |
| 19 | Margin on Loaded Cost ($) | =B14-B17 |
| 20 | **Margin on Loaded Cost (%)** | =B19/B14 |
| 21 | Margin on Base Cost ($) | =B14-B15 |
| 22 | **Margin on Base Cost (%)** | =B21/B14 |
| 23 | | |
| 24 | Above 40% Floor (loaded)? | =IF(B20>=JulyFloor,"YES","NO") |
| 25 | Above 40% Floor (base)? | =IF(B22>=JulyFloor,"YES","NO") |

### Section C: Per-Screen Economics (starting at A28)

| | A | B |
|---|---|---|
| 28 | **Per-Screen Economics** | |
| 29 | Cost per Screen (base) | =B15/TotalScreens |
| 30 | Cost per Screen (loaded) | =B17/TotalScreens |
| 31 | Revenue per Screen | =B14/TotalScreens |
| 32 | Margin per Screen | =B31-B30 |

### Section D: Staffing Summary (starting at A35)

| | A | B |
|---|---|---|
| 35 | **Staffing Summary** | |
| 36 | Duration (total months) | 4 |
| 37 | Peak Headcount | =1+1+JulyOffshore |
| 38 | Peak Monthly Burn | =MAX(B9:E9) |
| 39 | Avg Monthly Burn | =F9/4 |

### Formatting for July Tab

- Section headers: Bold, medium purple background (#5b21b6), white text
- Total/summary rows: Bold, light purple background (#f5f3ff)
- "YES" cells: Green background (#dcfce7), green text
- "NO" cells: Red background (#fee2e2), red text
- Margin % cells: Percentage format, 1 decimal
- Currency cells: Accounting format, 0 decimals
- Alternating row shading on the monthly breakdown: white / very light gray (#f8fafc)

---

## Tab 3: December Delivery

### Identical structure to July tab but with December parameters.

Title: "Scenario 2: December Delivery -- Comfortable Timeline"
Subtitle: "April POC --> May-Oct Development --> Nov-Dec QA/Acceptance"

| | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | *Resource* | *Apr* | *May* | *Jun* | *Jul* | *Aug* | *Sep* | *Oct* | *Nov* | *Dec* | *Total* |
| 5 | Colin | =POCCost | =ColinMonthly*ColinAlloc | (same for Jun-Dec) | ... | ... | ... | ... | ... | ... | =SUM(B5:J5) |
| 6 | US Eng A | 0 | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly | =USEngAMonthly*0.5 | =USEngAMonthly*0.5 | =SUM(B6:J6) |
| 7 | Offshore | 0 | =OffshoreMonthly*DecOffshore | (same for Jun-Oct) | ... | ... | ... | ... | =OffshoreMonthly*DecQAOffshore | =OffshoreMonthly*DecQAOffshore | =SUM(B7:J7) |
| 8 | **Monthly** | =SUM(B5:B7) | =SUM(C5:C7) | ... | ... | ... | ... | ... | ... | ... | =SUM(K5:K7) |
| 9 | **Cumulative** | =B8 | =B9+C8 | ... | ... | ... | ... | ... | ... | ... | |

Financial Summary, Per-Screen Economics, and Staffing Summary sections follow the same structure as July tab but referencing December values.

- Duration: 9 months
- Peak Headcount: =1+1+DecOffshore
- Margin floor check uses DecFloor (30%)

---

## Tab 4: Discount Analysis

### Title: "Scenario 3: Discount Sensitivity -- December Timeline Only"

### Section A: Discount Table (starting at A4)

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 3 | *December base cost:* | =('December Delivery'!B15) | *Loaded cost:* | =('December Delivery'!B17) | | |
| 4 | | | | | | |
| 5 | *Price* | *Discount %* | *Margin $ (loaded)* | *Margin % (loaded)* | *Margin $ (base)* | *Margin % (base)* |
| 6 | $500,000 | =1-(A6/Revenue) | =A6-$D$3 | =C6/A6 | =A6-$B$3 | =E6/A6 |
| 7 | $475,000 | (same pattern) | | | | |
| 8 | $468,000 | | | | | |
| 9 | $450,000 | | | | | |
| 10 | $425,000 | | | | | |
| 11 | $400,000 | | | | | |
| 12 | $375,000 | | | | | |
| 13 | $358,000 | | | | | |
| 14 | $350,000 | | | | | |

### Section B: Floor Price Calculation (starting at A17)

| | A | B |
|---|---|---|
| 17 | **Floor Price Calculations** | |
| 18 | Floor at 30% margin (loaded cost) | =$D$3/(1-DecFloor) |
| 19 | Max discount from $500K (loaded) | =1-(B18/Revenue) |
| 20 | Floor at 30% margin (base cost) | =$B$3/(1-DecFloor) |
| 21 | Max discount from $500K (base) | =1-(B20/Revenue) |

### Section C: Negotiation Rules (starting at A24)

| | A |
|---|---|
| 24 | **Negotiation Rules** |
| 25 | 1. July delivery: NO discount. 40% floor is non-negotiable. Speed is the premium. |
| 26 | 2. December at up to 6% discount: safe on loaded cost margin. |
| 27 | 3. December at 6-25% discount: viable only if risk reserve is treated as buffer inside margin. |
| 28 | 4. Below $375K: walk away or reduce scope. |
| 29 | 5. Counter-offer if they push hard: reduce screens (150 instead of 250) at discounted price. |

### Formatting for Discount Tab

- Rows where margin % (loaded) drops below 30%: entire row gets light red background (#fee2e2)
- Rows where margin % (loaded) is 30-40%: light yellow background (#fef9c3)
- Rows where margin % (loaded) is above 40%: light green background (#dcfce7)
- Conditional formatting on column D (margin % loaded):
  - >= 40%: green text, bold
  - 30-39.9%: orange text
  - < 30%: red text, bold
- The negotiation rules section: light gray background, italic text, no borders

---

## Tab 5: Comparison

### Title: "Scenario Comparison Dashboard"

### Section A: Side-by-Side (starting at A3)

| | A | B | C | D |
|---|---|---|---|---|
| 3 | *Metric* | *July (Sc. 1)* | *December (Sc. 2)* | *Discount (Sc. 3)* |
| 4 | Revenue | ='July Delivery'!B14 | ='December Delivery'!B14 | ='Discount Analysis'!B18 |
| 5 | Base Cost | ='July Delivery'!B15 | ='December Delivery'!B15 | ='December Delivery'!B15 |
| 6 | Risk Reserve | ='July Delivery'!B16 | ='December Delivery'!B16 | ='December Delivery'!B16 |
| 7 | Loaded Cost | ='July Delivery'!B17 | ='December Delivery'!B17 | ='December Delivery'!B17 |
| 8 | **Margin $ (loaded)** | ='July Delivery'!B19 | ='December Delivery'!B19 | =D4-D7 |
| 9 | **Margin % (loaded)** | ='July Delivery'!B20 | ='December Delivery'!B20 | =D8/D4 |
| 10 | Margin $ (base) | ='July Delivery'!B21 | ='December Delivery'!B21 | =D4-D5 |
| 11 | Margin % (base) | ='July Delivery'!B22 | ='December Delivery'!B22 | =D10/D4 |
| 12 | Duration (months) | 4 | 9 | 9 |
| 13 | Peak Offshore | =JulyOffshore | =DecOffshore | =DecOffshore |
| 14 | Peak Headcount | ='July Delivery'!B37 | ='December Delivery'!B37 | ='December Delivery'!B37 |
| 15 | Cost per Screen | ='July Delivery'!B30 | ='December Delivery'!B30 | =D7/TotalScreens |
| 16 | Revenue per Screen | ='July Delivery'!B31 | ='December Delivery'!B31 | =D4/TotalScreens |
| 17 | Monthly Burn (avg) | ='July Delivery'!B39 | ='December Delivery'!B39 | ='December Delivery'!B39 |
| 18 | Above Floor? | ='July Delivery'!B24 | ='December Delivery'!B24 | =IF(D9>=DecFloor,"YES","NO") |

### Section B: Key Insights (starting at A21)

| | A |
|---|---|
| 21 | **Key Insights** |
| 22 | July is most profitable: shorter timeline = less onshore overhead despite more offshore engineers. |
| 23 | December has ~$69K more onshore cost (Colin + US paid for 5 additional months). |
| 24 | Total offshore cost is identical in both scenarios (same total engineer-months). |
| 25 | Never discount July. Compressed timeline IS the premium. |
| 26 | Maximum safe discount on December: ~6% on loaded cost, ~25% on base cost. |

### Formatting for Comparison Tab

- Column headers (B3:D3): each scenario gets a distinct color
  - July: medium purple (#7c3aed) background, white text
  - December: dark blue (#1e40af) background, white text
  - Discount: dark amber (#92400e) background, white text
- Margin % rows (9, 11): bold, font size 12
- "YES"/"NO" cells: green/red conditional formatting as before
- Key insights: light gray background, italic

---

## Tab 6: Throughput

### Title: "Screen Conversion Throughput Model"

### Section A: Inputs (starting at A3)

| | A | B |
|---|---|---|
| 3 | Total Screens | =TotalScreens |
| 4 | Hours per Screen | =HoursPerScreen |
| 5 | Total Hours Needed | =TotalHours |
| 6 | Hours per Engineer per Month | =HoursPerMonth |

### Section B: July Throughput (starting at A9)

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 9 | **July Throughput** | *Apr* | *May* | *Jun* | *Jul* | *Total* |
| 10 | Engineers | 1 | =JulyOffshore+1 | =JulyOffshore+1 | 0 | |
| 11 | Available Hours | =B10*$B$6 | =C10*$B$6 | =D10*$B$6 | 0 | =SUM(B11:E11) |
| 12 | Screens Possible | =B11/$B$4 | =C11/$B$4 | =D11/$B$4 | 0 | =SUM(B12:E12) |
| 13 | Utilization Needed | | | | | =B5/F11 |

*Note: Row 10 April shows 1 (Colin during POC). May-Jun shows offshore + US engineer. Jul is 0 (QA, not new conversions).*

### Section C: December Throughput (starting at A16)

| | A | B | C-H (May-Oct) | I-J (Nov-Dec) | K |
|---|---|---|---|---|---|
| 16 | **December Throughput** | *Apr* | *May* ... *Oct* | *Nov* ... *Dec* | *Total* |
| 17 | Engineers | 1 | =DecOffshore+1 (each month) | 0 | |
| 18 | Available Hours | =B17*$B$6 | =C17*$B$6 ... | 0 | =SUM(...) |
| 19 | Screens Possible | =B18/$B$4 | ... | 0 | =SUM(...) |
| 20 | Utilization Needed | | | | =B5/K18 |

### Section D: Capacity Summary (starting at A23)

| | A | B | C |
|---|---|---|---|
| 23 | **Capacity Summary** | *July* | *December* |
| 24 | Total Capacity (screens) | =from B12 total | =from B19 total |
| 25 | Screens Needed | =TotalScreens | =TotalScreens |
| 26 | Utilization % | =B25/B24 | =C25/C24 |
| 27 | Headroom (extra screens) | =B24-B25 | =C24-C25 |

### Formatting for Throughput Tab

- Use a horizontal bar chart or data bars in the Screens Possible row to visualize throughput by month
- Utilization % cell: conditional formatting (green if under 80%, yellow 80-95%, red over 95%)
- Clean, minimal layout matching the other tabs

---

## Global Formatting Rules

### Colors (BayOne Brand Palette)

| Use | Color | Hex |
|---|---|---|
| Dark purple (headers) | Deep violet | #2e1065 |
| Medium purple (section headers) | Purple | #5b21b6 |
| Light purple (accent rows) | Soft violet | #ede9fe |
| Very light purple (subtle bg) | Near-white violet | #f5f3ff |
| Green (positive/pass) | Light green | #dcfce7 |
| Red (negative/fail) | Light red | #fee2e2 |
| Yellow (caution) | Light yellow | #fef9c3 |
| Border color | Light gray | #e2e8f0 |
| Text primary | Dark slate | #334155 |
| Text secondary | Medium slate | #64748b |

### Typography

- Font: Calibri (or Aptos if available)
- Tab titles: 14pt, bold, dark purple bg, white text
- Section headers: 12pt, bold, medium purple bg, white text
- Column headers: 11pt, bold, light purple bg
- Data: 11pt, regular
- Notes/insights: 10pt, italic, gray text

### Number Formats

- Currency: Accounting, 0 decimal places (e.g., $193,288)
- Hourly rates: Accounting, 2 decimal places (e.g., $27.50)
- Percentages: Percentage, 1 decimal place (e.g., 51.7%)
- Headcount: Number, 0 decimal places
- Months: Number, 0 decimal places

### Print Setup

- All tabs: Landscape orientation
- Fit to 1 page wide
- Header: "BayOne Solutions -- Confidential" left-aligned, "EPNM-to-EMS Pricing Model" center
- Footer: Page number right-aligned
- Margins: 0.5" all sides

### Conditional Formatting (apply globally where applicable)

- Margin % >= 40%: bold green text (#16a34a)
- Margin % 30-39.9%: bold amber text (#d97706)
- Margin % < 30%: bold red text (#dc2626), light red background
- "YES" cells: green bg (#dcfce7), dark green text
- "NO" cells: red bg (#fee2e2), dark red text

---

## Validation Checklist

After building, verify these values match the prototype:

| Check | Expected |
|---|---|
| July base cost | $193,288 |
| July loaded cost | $241,610 |
| July margin (loaded) | 51.7% |
| July margin (base) | 61.3% |
| December base cost | $262,288 |
| December loaded cost | $327,860 |
| December margin (loaded) | 34.4% |
| December margin (base) | 47.5% |
| December floor price (loaded, 30%) | ~$468,371 |
| December floor price (base, 30%) | ~$374,697 |
| POC cost | ~$8,308 |
| Colin monthly loaded | $18,000 |
| US Eng A monthly loaded | $10,500 |
| Offshore monthly loaded (mid) | ~$5,720 |

---

## Notes for the Builder

1. All financial cells on Scenarios 2-6 should reference the Inputs tab. If someone changes a rate on the Inputs tab, all scenarios should update automatically.
2. Do NOT hardcode any number that appears on the Inputs tab. Use named ranges.
3. The discount table on Tab 4 can have hardcoded price values in column A (those are the scenarios being tested), but all calculations reference the Inputs and December tabs.
4. Lock/protect the Inputs tab structure but leave the value cells editable so the user can run what-if scenarios.
5. Add data validation dropdowns where appropriate (e.g., offshore rate selection: low/mid/high).
6. Freeze panes: row 4 (below headers) on all scenario tabs so headers stay visible when scrolling.
