# Corrective Feedback v2: Rate Type Column

This is an additional correction on top of the v1 corrections prompt. Apply this AFTER the v1 changes. Do NOT remove or restructure any existing content.

---

## Change 5: Add Rate Type Column to Personnel Rates Table

### The Problem

Column B (Base Annual/Hourly) mixes two units: annual salaries for US resources and hourly rates for offshore resources. The formula that calculates Loaded Monthly is different for each, but nothing on the sheet indicates which formula to use. This breaks if someone adds a new resource without knowing which path to follow (e.g., a US contractor at $75/hr would get the wrong result if the formula assumes annual).

### The Fix

Add a **Rate Type** column to the Personnel Rates table on the Inputs tab. This column drives the Loaded Monthly calculation via a conditional formula.

### Updated Personnel Rates Table

| Resource | **Rate Type** | Base Rate | Load Factor | Loaded Rate | **Loaded Monthly** | Allocation % | Effective Monthly |
|---|---|---|---|---|---|---|---|
| Colin Moore | Annual | $180,000 | 1.20 | =Base*Load | *(formula below)* | 30% | =LoadedMonthly*Alloc |
| US Engineer A | Annual | $105,000 | 1.20 | =Base*Load | *(formula below)* | 100% | =LoadedMonthly*Alloc |
| US Engineer B | Annual | $160,000 | 1.20 | =Base*Load | *(formula below)* | 100% | =LoadedMonthly*Alloc |
| Offshore (low) | Hourly | $20.00 | 1.20 | =Base*Load | *(formula below)* | 100% | =LoadedMonthly*Alloc |
| Offshore (mid) | Hourly | $27.50 | 1.20 | =Base*Load | *(formula below)* | 100% | =LoadedMonthly*Alloc |
| Offshore (high) | Hourly | $35.00 | 1.20 | =Base*Load | *(formula below)* | 100% | =LoadedMonthly*Alloc |

### Rate Type Column

- **Cell format:** Data validation dropdown with two options: `Annual` and `Hourly`
- **Column position:** Insert as the SECOND column (after Resource name, before Base Rate). This way someone reading left-to-right sees the resource, then immediately knows how to interpret the base rate number.
- **Styling:** Light yellow background (#fef9c3) to match the Allocation % column (both are user-editable configuration fields)

### Loaded Monthly Formula

The Loaded Monthly column uses a conditional formula based on Rate Type:

```
=IF(RateType="Annual", LoadedRate/12, LoadedRate*HoursPerMonth)
```

Where:
- `RateType` = the Rate Type cell for that row
- `LoadedRate` = the Loaded Rate cell for that row (Base × Load Factor)
- `HoursPerMonth` = 173.33 (the named range from the Inputs tab)

Spelled out:
- **If Annual:** Loaded Annual / 12 = Loaded Monthly
- **If Hourly:** Loaded Hourly × 173.33 = Loaded Monthly

### Example Calculations (to verify)

| Resource | Rate Type | Base | Loaded | Loaded Monthly |
|---|---|---|---|---|
| Colin | Annual | $180,000 | $216,000 | $216,000 / 12 = **$18,000** |
| US Eng A | Annual | $105,000 | $126,000 | $126,000 / 12 = **$10,500** |
| Offshore (mid) | Hourly | $27.50 | $33.00 | $33.00 × 173.33 = **$5,720** |

These should match the existing values. The change is in HOW they are calculated, not WHAT the result is.

### Why This Matters for the Template

When this workbook is reused for other engagements:
- A US contractor at $75/hr can be entered with Rate Type = "Hourly" and the formula works correctly
- A salaried offshore team lead at $85,000/yr can be entered with Rate Type = "Annual" and it works correctly
- No one has to understand or modify the formula; they just pick Annual or Hourly from the dropdown

### Column Header Label

Label the column **"Rate Type"** with a subtitle or cell comment: *"Annual = yearly salary, Hourly = per-hour rate. Drives the Loaded Monthly calculation."*

---

## Validation After This Change

1. All existing Loaded Monthly values remain identical (this is a formula change, not a result change)
2. The dropdown shows exactly two options: Annual, Hourly
3. Changing a US resource from "Annual" to "Hourly" dramatically changes their Loaded Monthly (this confirms the formula is working -- change it back after testing)
4. All downstream calculations (scenario tabs, comparison, discount analysis) still pull correct values
5. The Effective Monthly column still works (it multiplies Loaded Monthly by Allocation %)
