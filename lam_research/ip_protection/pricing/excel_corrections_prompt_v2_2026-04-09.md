# Correction Prompt v2: Lam Research POC Workbook - Pricing Revision

**Apply these changes to the Lam Research POC workbook. These supersede any conflicting values from the original spec or v1 corrections. Do NOT restructure tabs or delete formulas. These are value and rate changes only.**

---

## Change 1: India Resource Rate Increase

### The Problem

The India resource is currently at $27.50/hr base ($33.00/hr loaded at 1.20x). This is below what BayOne charges for QA manual testers ($35-36/hr). AI work should be priced higher.

### The Fix

On the **Personnel** tab, update the India resource (currently labeled "India Resource (Mid-Level)" or "Offshore Resource (Mid-Level)"):

| Field | Old Value | New Value |
|---|---|---|
| Base Rate | $27.50/hr | $37.50/hr |
| Loaded Rate | $33.00/hr | $45.00/hr |
| Loaded Monthly | $5,720 | $7,800 (= $45.00 x 173.33) |

The load factor remains 1.20x. All downstream formulas on the POC tab should update automatically.

### Verification

- India resource loaded hourly: $45.00
- India resource POC cost (120 hrs): $5,400.00
- Total POC personnel base cost: $6,646.20

---

## Change 2: Add Travel Cost

### The Problem

No travel was budgeted. The team agreed Colin should be in person for at least one POC meeting.

### The Fix

On the **POC** tab, in Section C (POC Financial Summary), add a Travel line item between Personnel Base Cost and Risk Reserve:

| Line Item | Value | Notes |
|---|---|---|
| Total POC Personnel Cost | $6,646.20 | (auto-calculated from Section B) |
| **Travel** | **$2,500.00** | One in-person trip for POC demo/execution |
| Base Cost (Personnel + Travel) | $9,146.20 | = Personnel + Travel |
| Risk Reserve (25%) | $1,661.55 | = Personnel Cost x 25% (risk reserve is on personnel only, not travel) |
| Loaded Cost | $10,807.75 | = Base Cost + Risk Reserve |

If the POC tab does not have a travel line, add one. If it does, update the value from $0 to $2,500.

### Verification

- Base Cost (personnel + travel): $9,146.20
- Risk Reserve: $1,661.55
- Loaded Cost: $10,807.75

---

## Change 3: Update Billed Amount

### The Problem

The POC was priced at $10,000. With the revised cost basis, this is below loaded cost.

### The Fix

On the **POC** tab and **Project Inputs** tab, update:

| Field | Old Value | New Value |
|---|---|---|
| Billed Amount / POC Amount / Client Price | $10,000 | $15,000 |

### Verification After All Changes

| Check | Expected Value |
|---|---|
| Onshore Resource (Lead Level) loaded hourly | $103.85 |
| Onshore Resource POC hours | 12 |
| Onshore Resource POC cost | $1,246.20 |
| India Resource loaded hourly | $45.00 |
| India Resource POC hours | 120 |
| India Resource POC cost | $5,400.00 |
| Total POC personnel cost | $6,646.20 |
| Travel | $2,500.00 |
| Base cost (personnel + travel) | $9,146.20 |
| Risk reserve (25% on personnel) | $1,661.55 |
| Loaded cost | $10,807.75 |
| Billed amount | $15,000 |
| Net POC (revenue minus loaded) | $4,192.25 |
| Margin % (base + travel) | 39.0% |
| Margin % (loaded) | 27.9% |
| Above 30% floor (loaded)? | NO (but 39% on base+travel; risk reserve is buffer) |
