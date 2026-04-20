# Internal Scoping Prep — Costing and Margin Analysis

**Source:** claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/internal_yikes_4152026_formatted.txt
**Date:** 2026-04-15 (internal BayOne meeting, pre-Anand call)

---

## The Core Costing Problem

Colin was never involved in the original pricing conversation. He was handed a number ($100K/quarter) and told to figure it out. He raised this issue multiple times when it happened. This is the root cause of the margin pressure: the price was set without consulting the person who would have to deliver against it.

### What Was Promised vs. What Exists

- **Promised to Cisco by RS:** Colin would be 100% involved in this project.
- **Reality:** Colin is not spending 100% of his time on this. He softened this in the proposal by saying he would be "heavily involved at the start" with utilization tapering off.
- **The margin impact:** If Colin's cost is loaded into the project at any meaningful allocation, the $100K/quarter math falls apart. Without Colin in the picture at $125K, the margin would be approximately 40%. With Colin at 25% allocation, the numbers jump significantly.

### Resource Rates Discussed

| Resource | Base Rate | Loaded | Location | Notes |
|----------|-----------|--------|----------|-------|
| Colin | Private | 25% allocation | Remote US (PA) | Rate kept private in meeting |
| Srikar | $73.50/hr | Already includes 5% load | Bay Area onsite | |
| Namita | $95/hr base | $140K salary, ~$95 loaded + visa costs | Bay Area onsite | |
| Saurav | $11.18/hr | + 30% offshore load | India | Colin pushing for raise, says he will leave |
| Vaishali | ~$15/hr est | + 30% offshore load | India | Not yet started |
| Tanuja | ~$15/hr est | + 30% offshore load | India | Not yet started |

### The Offshore Rate Debate

A significant portion of the meeting was spent arguing about whether to use actual payroll costs ($8-15/hr for offshore) or market replacement rates ($20-24/hr) for internal costing. Two conflicting perspectives:

1. **Colin's position:** Use actual payroll data (Paycom/Keka) as source of truth for internal costing. Present market rates to Cisco. These are two separate things. The team is conflating internal cost with external billing rate, which artificially depresses margin calculations.

2. **Others' position:** Use market replacement cost ($20/hr) as the internal rate because if those people leave, you would have to pay market rate for replacements. This is more conservative but makes the margin look worse than it is.

Colin pointed out that Askari (who backed out) had a loaded cost of ~$24/hr. The two replacements (Vaishali, Tanuja) combined are still less than what Askari alone was costing.

### The Numbers They Landed On

- **Q4 loaded cost (full team):** ~$159K
- **With 35% GM:** ~$216K
- **Q3 consumed (5 weeks, partial team):** ~$74K
- **Q3 revenue from Cisco:** $122K
- **Q3 surplus carry-forward:** ~$48K
- **Q4 ask from Cisco:** $168K ($216K minus $48K carry-forward)
- **Risk reserve:** Set to zero. Colin argued they cannot add risk reserve because the original $100K baseline was already too low. Adding 25% on top would make the ask look like 2.5x the original, which is indefensible.

### The Reverse Computation Check

Someone ran a sanity check using typical Cisco partner rates:
- Colin at $160/hr, 25% allocation, 500 hours = ~$20K
- Two onshore at $100/hr, 520 hours each = ~$104K
- Three offshore at $50/hr, 500 hours each = ~$78K
- Total: ~$203K

This roughly validates the $216K number, but the concern is that Cisco typically does not pay more than $25-30/hr for offshore resources. The onshore rates are close to what Cisco is used to.

---

## The Uncomfortable Truth Colin Surfaced

Colin said it bluntly in this meeting: RS told Cisco that Colin would be 100% on this project to get BayOne's foot in the door. That commitment was made without Colin's involvement in the pricing. Now the math does not work because:

1. Colin's loaded cost at even 25% allocation eats a meaningful chunk of a $100K quarter
2. The team was hired and staffed for a scope that assumed prerequisites were in place (they were not)
3. The actual work is simpler than expected ("soapbox derby car"), but access gates make velocity slow regardless of team size
4. Colin could do the whole project with one person if access were not the bottleneck

Colin's practical recommendation: $125K/quarter without his cost in the picture yields ~40% margin and is sustainable. The positioning to get more is to say Colin's involvement needs to stay higher longer due to Cisco's technical state.
