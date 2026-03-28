# Corrective Feedback v3: Editable Working Hours Per Month

Apply this after all prior changes. Do NOT remove or restructure any existing content. This is one additive change.

---

## Change: Make Working Hours Per Month Editable

### Current State

Working Hours per Month is hardcoded at 173.33. This value only affects resources with Rate Type = "Hourly" (their Loaded Monthly formula is `Loaded Hourly × Working Hours per Month`). Resources with Rate Type = "Annual" are unaffected (their formula is `Loaded Annual / 12`).

The 173.33 represents theoretical maximum capacity (52 weeks × 40 hours / 12 months). Some companies prefer 160 or 168 to account for holidays, PTO, and realistic availability.

### What to Change

1. Find the cell containing the 173.33 value on the Inputs tab (it should already exist, possibly with a named range `HoursPerMonth`).

2. Make sure that cell is:
   - **Editable** (not locked, not embedded inside a formula elsewhere)
   - **Light yellow background** (#fef9c3) to match other editable input cells
   - Has a **cell comment** or adjacent note in a smaller font: *"Standard: 173.33 (52w × 40h / 12). Adjust to 160-168 for realistic availability after holidays/PTO."*

3. Confirm the Loaded Monthly formula for Hourly resources references this cell (not a hardcoded 173.33). The formula should be:
   ```
   =IF(RateType="Annual", LoadedRate/12, LoadedRate * HoursPerMonth)
   ```
   where `HoursPerMonth` points to the editable cell.

### Verification

1. Change Working Hours from 173.33 to 160. Every Hourly resource's Loaded Monthly should drop (e.g., offshore mid at $33/hr goes from $5,720 to $5,280).
2. Every Annual resource's Loaded Monthly should stay exactly the same.
3. All downstream calculations (Effective Monthly, scenario tabs, comparison, discount analysis) should update automatically.
4. Change it back to 173.33 and confirm all values return to their original amounts.
