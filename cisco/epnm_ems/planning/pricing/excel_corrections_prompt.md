# Corrective Feedback for Pricing Model Workbook

You have built an excellent workbook from the prototype spec. The following are additions and refinements. Do NOT remove or restructure any existing content. These are additive changes only.

---

## Change 1: Add Travel & Expenses Section

### On the Inputs tab

Add a new section below the existing parameters:

**Section: Travel & Expenses**

| Field | Default Value | Notes |
|---|---|---|
| Cost per Trip | $2,750 | Average: flights, hotel, meals, ground transport |
| Trips (July scenario) | 2 | Kickoff + final demo/acceptance |
| Trips (December scenario) | 4 | Kickoff + 2 periodic checkpoints + final demo/acceptance |
| Travel Destination | San Jose, CA | For reference only, not used in calculations |

Create named ranges: `CostPerTrip`, `JulyTrips`, `DecTrips`

### On each scenario tab (July, December, Discount)

Add a row below the personnel cost rows for Travel & Expenses:

- **July:** Travel total = `CostPerTrip * JulyTrips` (display as a single line item, not monthly)
- **December:** Travel total = `CostPerTrip * DecTrips`
- Add this to the Base Cost subtotal

The travel cost should appear in the Financial Summary as a separate line between personnel cost and the Base Cost total, like:

```
Personnel Cost:    $XXX,XXX
Travel & Expenses: $XX,XXX
Base Cost:         $XXX,XXX  (sum of personnel + travel)
Risk Reserve:      $XX,XXX
Loaded Cost:       $XXX,XXX
```

---

## Change 2: Add Hardware & Consumables Placeholder

### On the Inputs tab

Add to the Travel & Expenses section (or create a sibling section):

**Section: Hardware & Consumables**

| Field | Default Value | Notes |
|---|---|---|
| Monthly Tools & Subscriptions | $0 | Placeholder. Cisco provides hardware and AI licenses. |
| One-Time Equipment | $0 | Placeholder. Add if BayOne-side hardware needed. |

Create named ranges: `MonthlyTools`, `OneTimeEquipment`

### On each scenario tab

Add a row for Hardware & Consumables below Travel & Expenses:

- **Formula:** `OneTimeEquipment + (MonthlyTools * total_months_for_scenario)`
- Default will be $0 but the line item is present and configurable

Include in the Base Cost subtotal alongside personnel and travel.

The Financial Summary should now read:

```
Personnel Cost:         $XXX,XXX
Travel & Expenses:      $XX,XXX
Hardware & Consumables:  $X,XXX
Base Cost:              $XXX,XXX
Risk Reserve:           $XX,XXX
Loaded Cost:            $XXX,XXX
```

---

## Change 3: Per-Resource Utilization Percentages

### On the Inputs tab

Add a new column to the Personnel Rates table for **Allocation %**. This replaces the single "Colin Allocation %" parameter that currently exists as a standalone field.

The Personnel Rates table should now look like:

| Resource | Base | Load Factor | Loaded | Loaded Monthly | **Allocation %** | **Effective Monthly** |
|---|---|---|---|---|---|---|
| Colin Moore | $180,000 | 1.20 | $216,000 | $18,000 | 30% | =Loaded Monthly * Allocation |
| US Engineer A | $105,000 | 1.20 | $126,000 | $10,500 | 100% | =Loaded Monthly * Allocation |
| US Engineer B | $160,000 | 1.20 | $192,000 | $16,000 | 100% | =Loaded Monthly * Allocation |
| Offshore (low) | $20.00 | 1.20 | $24.00 | $4,152 | 100% | =Loaded Monthly * Allocation |
| Offshore (mid) | $27.50 | 1.20 | $33.00 | $5,720 | 100% | =Loaded Monthly * Allocation |
| Offshore (high) | $35.00 | 1.20 | $42.00 | $7,266 | 100% | =Loaded Monthly * Allocation |

Create named ranges for each Effective Monthly value. The Allocation % cells should be unlocked/editable so the user can adjust utilization per resource.

### On each scenario tab

Update all monthly cost formulas to use the **Effective Monthly** (which already factors in allocation) instead of multiplying by a separate allocation percentage. This means changing the allocation % on the Inputs tab automatically flows through to all scenarios.

**Remove** the standalone "Colin Allocation %" parameter from wherever it currently sits (it is now part of the Personnel Rates table).

**Important:** The offshore allocation % applies per engineer. If Allocation is 90%, each offshore engineer's monthly cost is $5,720 * 90% = $5,148. Multiply that by the number of engineers for the total offshore line.

---

## Change 4: Reframe "QA Months" as "Stabilization & Acceptance"

### Everywhere "QA" appears as a phase label

Replace with **"Stabilization & Acceptance"**. This phase represents:
- Production-level testing after Cisco integrates the converted screens
- Validation that everything works as expected in Cisco's environment
- Bug fixes and refinements based on integration findings
- Building stakeholder trust in the deliverables
- Final acceptance and handoff

This is NOT a separate QA phase. Development follows an agile cycle where testing happens throughout. The stabilization period is a safety net and acceptance buffer after the core conversion work is complete.

### Specific label changes

| Old Label | New Label |
|---|---|
| "Jul (QA)" | "Jul (Stabilization & Acceptance)" |
| "Nov-Dec (QA)" | "Nov-Dec (Stabilization & Acceptance)" |
| "QA Months" on Inputs tab | "Stabilization & Acceptance Months" |
| Any column headers with "QA" | Replace with "Stab. & Acceptance" (abbreviated for column width) |
| Phase subtitles | Update to reflect: "...May-Jun Factory --> Jul Stabilization & Acceptance" |

### On the Inputs tab

Rename the field from "QA Months" to "Stabilization & Acceptance Months" in the Scenario Parameters section.

---

## Formatting Notes

- New sections (Travel, Hardware) should match existing section styling: bold headers with purple background, same font and border treatment
- The Allocation % column should have a light yellow background (#fef9c3) to visually signal "this is editable/configurable"
- Effective Monthly column can have a light gray background to show it is calculated
- Travel and Hardware rows on scenario tabs should use the same alternating row styling as personnel rows
- If the Financial Summary section needs to be taller to fit the new line items, extend it downward (do not compress existing rows)

---

## Change 5: Make Working Hours Per Month Editable

### The Problem

Working Hours per Month is hardcoded at 173.33 (2,080 hrs/yr / 12). This value only affects hourly (offshore) resources -- it determines their monthly cost. For annual/salaried resources, monthly cost is simply Annual / 12 regardless of hours. The 173.33 represents theoretical maximum capacity (52 weeks × 40 hrs). Some companies use 160 or 168 to account for holidays and PTO.

### The Fix

Make Working Hours per Month an editable input cell on the Inputs tab, not a hardcoded value. It remains a single global setting (not per-resource).

### On the Inputs tab

The Working Hours per Month field should:
- Be in the existing Constants/Parameters section
- Default to 173.33
- Have a light yellow background (#fef9c3) to signal it is editable
- Have a cell comment or adjacent note: *"Standard: 173.33 (52w × 40h / 12). Adjust to 160-168 for realistic availability after holidays/PTO."*
- Have the named range `HoursPerMonth` (likely already exists -- just ensure the cell is editable, not hardcoded in formulas)

### How It Connects

- The Loaded Monthly formula for hourly resources uses this value: `LoadedHourly × HoursPerMonth`
- Changing it from 173.33 to 160 reduces each offshore engineer's monthly cost (e.g., $33/hr × 160 = $5,280 vs. $33/hr × 173.33 = $5,720)
- This flows through Allocation % → Effective Monthly → all scenario tabs automatically
- Annual/salaried resources are unaffected (their formula is `LoadedAnnual / 12`)

### Important

This is a **company-level** setting, not a project-level one. It represents BayOne's standard for how many hours an hourly contractor generates per month. It should be the same across all projects using this template.

---

## Validation After Changes

After applying these changes, verify:

1. Changing Colin's Allocation % on Inputs updates all scenario tabs automatically
2. Changing US Engineer A's Allocation % updates all scenario tabs automatically
3. Changing offshore Allocation % updates all scenario tabs (per-engineer cost changes, multiplied by headcount)
4. Travel costs appear in Base Cost on all scenario tabs
5. Hardware & Consumables row exists (at $0 default) and is additive to Base Cost
6. No scenario tab still says "QA" anywhere
7. The Comparison dashboard still pulls correct values after all changes
8. Discount Analysis still calculates correctly with the updated Base Cost
9. Margin percentages shift slightly due to travel cost addition (this is expected and correct)
10. Working Hours per Month cell is editable (not hardcoded) and changing it updates all hourly resource monthly costs
11. Changing Working Hours does NOT affect annual/salaried resource costs
