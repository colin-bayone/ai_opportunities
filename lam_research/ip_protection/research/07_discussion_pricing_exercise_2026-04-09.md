# 07 - Discussion: POC Pricing Exercise

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-09 (POC pricing exercise, continued from 07_discussion_pricing_scope)
**Document Set:** 07 (Pricing Discussion)
**Pass:** Pricing model construction

---

## Context

This continues the Set 07 discussion. The proposal structure is established (deliverables, timeline, success criteria, assumptions, risks, two-document format). Now working through the actual pricing number.

**Known inputs:**
- Colin at approximately 25% allocation for three weeks
- One India resource at 100% allocation for three weeks
- Three-week duration from access (one week discovery, two weeks build)
- POC runs on BayOne's environment
- $10K was a gut anchor, not a worked number
- Outcome-based pricing, no headcount disclosed to client

**Reference model:** Cisco EPNM/EMS pricing used the costing workbook with: base rates per resource, load factor (1.20x), risk reserve (25%), margin targets (40% hard floor compressed, 30% floor standard), and scenario modeling. The Cisco POC was $8,308 absorbed (zero cost to client), Colin solo for 80 hours. The Lam POC will NOT be free.

**Pricing workflow:** Per the Singularity pricing workflow, the questionnaire runs in batches. Starting with scope and team costs.

---

## Exchange 1: Team Costs

**Claude's perspective:**

From the Cisco pricing spec, the cost structure started with annual or hourly rates per resource, then applied a load factor (1.20x for benefits, overhead, etc.) to get loaded rates. For the Lam POC, we have two resources:

1. **Colin** at 25% allocation. From the Cisco workbook, Colin's rate was documented as a known input. For this POC, 25% of three weeks is roughly 30 hours (assuming ~40 hour weeks, 25% = 10 hours/week x 3 weeks). That's the time commitment, but the cost to BayOne depends on Colin's loaded rate. Since Colin is salaried, the internal cost is technically zero incremental if he's already on payroll, but the workbook accounts for it as an opportunity cost against other billable work.

2. **India resource** at 100% allocation. Three full weeks, roughly 120 hours. The rate for India-based resources was in the Cisco workbook as a significantly lower base than US-based resources.

The question that drives the pricing model is not what it costs BayOne internally (that determines margin), but what the deliverables are worth to Lam (that determines the price). From Set 04, Colin's philosophy: "How much is this worth to you?" not "Here's our hourly rate."

So the pricing exercise works backwards from value and forwards from cost, and the price lands somewhere that gives BayOne acceptable margin while staying within Lam's value perception.

For the cost side, I need the actual rates to run numbers. **What are the loaded rates for you and the India resource, or would you prefer to work with the ranges from the Cisco workbook as a starting point?**

**Colin's response:**

Use the Cisco workbook ranges. Colin as the US resource, mid-level offshore for the India resource. Calculate the POC costing.

---

## Exchange 2: POC Cost Model

**Claude's calculation:**

**Rates (from Cisco workbook, 1.20x load factor):**
- Colin: $180,000/yr base, $216,000/yr loaded, **$103.85/hr loaded**
- Offshore mid: $27.50/hr base, **$33.00/hr loaded**

**Duration:** 3 weeks = 15 working days = 120 available hours

**Hours by resource:**

| Resource | Allocation | Hours (3 weeks) | Loaded Rate | Cost |
|---|---|---|---|---|
| Colin | 25% | 30 hrs | $103.85/hr | $3,115.50 |
| Offshore mid | 100% | 120 hrs | $33.00/hr | $3,960.00 |
| **Personnel base cost** | | **150 hrs** | | **$7,075.50** |

**With risk reserve (25%, same as Cisco):**

| Line | Amount |
|---|---|
| Personnel base cost | $7,075.50 |
| Risk reserve (25%) | $1,768.88 |
| **Loaded cost** | **$8,844.38** |

**Margin analysis at various price points:**

| Price to Lam | Margin (on base) | Margin % (base) | Margin (on loaded) | Margin % (loaded) |
|---|---|---|---|---|
| $7,500 | $424.50 | 5.7% | -$1,344.38 | Below floor |
| $10,000 | $2,924.50 | 29.2% | $1,155.62 | 11.6% |
| $12,500 | $5,424.50 | 43.4% | $3,655.62 | 29.2% |
| $15,000 | $7,924.50 | 52.8% | $6,155.62 | 41.0% |
| $17,500 | $10,424.50 | 59.6% | $8,655.62 | 49.5% |
| $20,000 | $12,924.50 | 64.6% | $11,155.62 | 55.8% |

**Key observations:**

1. At the $10K gut anchor, base margin is 29.2%, which is just under the 30% floor from the Cisco model. On loaded cost (with risk reserve), margin drops to 11.6%. That is thin.

2. To hit the Cisco 30% floor on loaded cost, the price needs to be approximately $12,635. Rounding to $12,500 gets close (29.2% loaded margin).

3. At $15K, loaded margin is 41%, which is above the Cisco hard floor for compressed timelines (40%). This gives comfortable room.

4. The base cost to BayOne is roughly $7K. Everything above that is margin and risk buffer. The question is what Lam perceives as reasonable for a three-week engagement that solves a problem they have been unable to fix in 18 months.

5. For context, Lam's prior effort consumed 18 months of internal engineering time across multiple people. Even at the most conservative estimate, that was hundreds of thousands of dollars of internal cost for 17% false positives. A $10-15K POC that demonstrates meaningful improvement is a fraction of what they have already spent.

**Colin's response:**

Colin revised his allocation to 10% (down from 25%) and asked to see updated numbers. Also established formatting rules for the internal document and expressed comfort at the $10K price point.

---

## Exchange 3: Revised Allocation and Internal Document

**Revised calculation at 10% Colin allocation:**

| Resource | Allocation | Hours (3 weeks) | Loaded Rate | Cost |
|---|---|---|---|---|
| Colin | 10% | 12 hrs | $103.85/hr | $1,246.20 |
| Offshore mid | 100% | 120 hrs | $33.00/hr | $3,960.00 |
| **Personnel base cost** | | **132 hrs** | | **$5,206.20** |

**With risk reserve (25%):**

| Line | Amount |
|---|---|
| Personnel base cost | $5,206.20 |
| Risk reserve (25%) | $1,301.55 |
| **Loaded cost** | **$6,507.75** |

**Revised margin analysis:**

| Price to Lam | Margin (on base) | Margin % (base) | Margin (on loaded) | Margin % (loaded) |
|---|---|---|---|---|
| $7,500 | $2,293.80 | 30.6% | $992.25 | 13.2% |
| $10,000 | $4,793.80 | 47.9% | $3,492.25 | 34.9% |
| $12,500 | $7,293.80 | 58.4% | $5,992.25 | 47.9% |
| $15,000 | $9,793.80 | 65.3% | $8,492.25 | 56.6% |

**Key change:** At 10% allocation, the $10K price point now gives 47.9% base margin and 34.9% loaded margin. That is above the 30% floor on loaded cost, which puts it in a healthy zone. The $10K gut anchor is actually well-justified at this allocation level.

**Claude's perspective on the $10K vs. $12.5K question:**

At 10% allocation, $10K gives nearly 48% base margin and 35% loaded margin. That is healthy for a POC whose primary value is access, not revenue. From Set 06, Colin's own argument was that even $3K margin on a $10K POC is "nice for personal, but not in the scope of the company" because the real value is the Lam ID and system access. At revised allocation, the margin is now $4,794 on base, which is even stronger than the original gut math.

The argument for $10K over $12.5K:
- Lower price reduces friction in Brad's approval process. Brad has vendor scar tissue (Set 02) and will scrutinize the number.
- The POC is a foot-in-the-door play. The real revenue comes from the full engagement, which is undefined but could be substantial given the scope confusion (multiple applications, internal + customer sites).
- $10K is a round number that signals "serious but not expensive." $12.5K is an odd number that invites the question "why not $10K?"
- At 35% loaded margin, BayOne is protected even if the risk reserve gets partially consumed.

The argument for $12.5K:
- Sets a higher anchor for the full engagement pricing. If the POC is $10K for three weeks, Lam might extrapolate that the full engagement should be proportionally cheap.
- 48% loaded margin gives more room for scope surprises.
- Brad wants to go into the weeds on pricing (Set 06, Anuj's observation). A higher number with clear justification may actually build more credibility than a suspiciously low one.

Colin's preference is $10K, and the math supports it at 10% allocation. The margin is healthy, the number is clean, and the strategic value of access outweighs optimizing POC margin.

**Internal document formatting rules (from Colin):**
- Colin's loaded rate is NOT shown. Only show his total cost for hours worked (i.e., $1,246.20 as a line item, not $103.85/hr x 12 hrs). His team does not need to know his salary.
- The India resource CAN be shown with both hourly rate and total.
- This document is internal only. It explains the price breakdown to the BayOne team (Anuj, Amit, Pat) so they understand the granularity.

**Colin's response:**

$10K confirmed as the final POC price.

---

## Final Pricing Summary

| Item | Value |
|---|---|
| **POC Price to Lam** | **$10,000** |
| Duration | 3 weeks from access (1 week discovery, 2 weeks build) |
| Personnel base cost | $5,206.20 |
| Risk reserve (25%) | $1,301.55 |
| Loaded cost | $6,507.75 |
| **Margin (base)** | **$4,793.80 (47.9%)** |
| **Margin (loaded)** | **$3,492.25 (34.9%)** |

**Team (internal only):**

| Resource | Allocation | Hours | Cost |
|---|---|---|---|
| Colin Moore | 10% | 12 hrs | $1,246.20 (shown as total only, no hourly rate) |
| Offshore mid | 100% | 120 hrs | $3,960.00 (shown with $33.00/hr loaded rate and total) |

**Internal document formatting:**
- Colin's line shows total cost only (not hourly rate, not salary)
- India resource shows hourly rate and total
- Document is internal only (BayOne team: Anuj, Amit, Pat)
- No version of this cost breakdown goes to Lam. Lam sees outcome-based deliverables and a total price.
