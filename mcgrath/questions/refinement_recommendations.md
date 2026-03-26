# Question Refinement Recommendations

**Date:** February 20, 2026
**Analyzed by:** Session D

---

## Executive Summary

The 20-question catalog is generally well-constructed with clear strategic purpose. **14 questions require no changes or only minor wordsmithing**, while **6 questions need refinement** to improve neutrality, reduce sensitivity exposure, or sharpen clarity. The most significant improvements target the medium-sensitivity questions (Q8, Q9, Q18, Q19), which currently reveal more strategic intent than necessary. One consolidation opportunity exists (Q18 + Q19).

---

## Questions Requiring No Changes

**Q1, Q5, Q6, Q7, Q11, Q12, Q14, Q15, Q17** — These are clear, professionally worded, and reveal nothing strategic. Standard MSP scoping questions that any sophisticated bidder would ask.

| Question | Why It's Good |
|----------|---------------|
| Q1 | Specific, data-driven, essential for pricing |
| Q5 | Shows technical depth without revealing strategy |
| Q6 | Smart catch on the OCI hours hint; neutrally framed |
| Q7 | Standard evaluation weighting question |
| Q11 | Technical scoping for after-hours support |
| Q12 | Governance maturity question; reveals nothing |
| Q14 | Standard tooling clarification |
| Q15 | Responsible technical due diligence |
| Q17 | Every vendor asks about budget |

---

## Questions with Minor Refinements

### Q2: Current FTE Count

**Original:** What is the current FTE count (internal and external/contractor) supporting each application area today? How many of these resources are expected to transition to the MSP, remain at MGRC, or depart during the onboarding period?

**Refined:** What is the current FTE count (internal and contractor) supporting each application area? Are any of these resources expected to transition to the MSP as part of the onboarding process?

**Changes:**
- Removed "external" (redundant with "contractor")
- Simplified the three-way split question to focus on what matters: will we absorb anyone?
- The "remain at MGRC or depart" scenarios are MGRC's business; we only need to know about potential rebadging

**Impact:** Efficiency, Clarity

---

### Q3: KT Period Resource Availability

**Original:** For the Knowledge Transfer phase (May 18 – July 6), will MGRC's current support resources remain fully available to shadow and co-work with MSP staff during the entire transition period, or is there an expected ramp-down schedule for current resources?

**Refined:** During the Knowledge Transfer phase (May 18 – July 6), will current support resources remain available to work alongside MSP staff, or is a ramp-down schedule anticipated?

**Changes:**
- "shadow and co-work" → "work alongside" (simpler)
- Removed "fully" (binary question, yes or no)
- "current resources" rather than "MGRC's current support resources" (tighter)

**Impact:** Efficiency

---

### Q4: Phased Go-Live Approach

**Original:** Is MGRC open to a phased go-live approach where application areas are transitioned in priority waves (e.g., Salesforce and integrations first, then Oracle Fusion, then BI/data platforms) rather than a single go-live date of July 6 for all areas?

**Refined:** Is MGRC open to a phased go-live approach where application areas transition in priority waves, rather than a single July 6 go-live for all areas?

**Changes:**
- Removed the specific example sequence "(e.g., Salesforce and integrations first, then Oracle Fusion, then BI/data platforms)"
- The example sequence reveals our thinking about complexity/priority ordering, which competitors could interpret

**Impact:** Neutrality

---

### Q10: Dedicated vs Pooled Resources

**Original:** For US business hours support (5 AM – 5 PM PST), does MGRC require dedicated named resources assigned exclusively to MGRC for each application area, or is a shared/pooled resource model with guaranteed response SLAs acceptable?

**Refined:** For US business hours support, does MGRC require dedicated named resources for each application area, or is a pooled model with guaranteed response SLAs acceptable?

**Changes:**
- Removed "(5 AM – 5 PM PST)" — this is in the RFP; no need to repeat
- "shared/pooled" → "pooled" (redundant)
- "assigned exclusively to MGRC" — implied by "dedicated"

**Impact:** Efficiency

---

### Q13: Oracle Fusion Volumes

**Original:** For Oracle Fusion day-to-day operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, PO/invoice processing, and service requests? Are there seasonal peaks (quarter-end, year-end) that require surge staffing?

**Refined:** For Oracle Fusion operations, can MGRC provide approximate monthly volumes for period-close activities, journal entries, and PO/invoice processing? Are there seasonal peaks that require surge capacity?

**Changes:**
- "day-to-day operations" → "operations" (tighter)
- Removed "service requests" — Q1 already covers ticket volumes
- "(quarter-end, year-end)" removed — they know what seasonal peaks means
- "surge staffing" → "surge capacity" (more neutral; doesn't presume staffing model)

**Impact:** Efficiency, Clarity

---

### Q16: PCI Compliance Scope

**Original:** For the Customer Hub (nopCommerce), can MGRC confirm the current PCI compliance scope (SAQ type), frequency of penetration testing, and whether the MSP will be expected to maintain PCI certification on behalf of MGRC or support MGRC's own PCI audit process?

**Refined:** For the Customer Hub (nopCommerce), can MGRC clarify the current PCI compliance scope (SAQ type), penetration testing frequency, and the MSP's expected role in PCI compliance activities?

**Changes:**
- "confirm" → "clarify" (we're not confirming assumptions)
- "whether the MSP will be expected to maintain PCI certification on behalf of MGRC or support MGRC's own PCI audit process" is wordy — replaced with the neutral "MSP's expected role in PCI compliance activities"
- Original phrasing reveals concern about accountability exposure

**Impact:** Neutrality, Efficiency

---

### Q20: RACI Finalization Timing

**Original:** For items designated as 'Shared Responsibility,' will the RACI and responsibility splits be finalized before contract execution, or will they be defined during the Phase 1 onboarding period? How will scope disputes in shared areas be resolved?

**Refined:** For items designated as 'Shared Responsibility,' will the RACI be finalized before contract execution or during Phase 1 onboarding?

**Changes:**
- Removed "How will scope disputes in shared areas be resolved?" — This is a reasonable question but asking it pre-award signals we anticipate disputes, which isn't a good look. Address dispute resolution during contract negotiation if shortlisted.
- "responsibility splits" is redundant with RACI

**Impact:** Positioning, Neutrality

---

## Questions with Significant Refinements

### Q8: Multi-MSP vs Single Provider

**Original:** Is MGRC open to awarding the MSP engagement to more than one provider with complementary specializations (e.g., one MSP for Salesforce/CRM ecosystem and another for Oracle ERP/infrastructure), or is the strong preference for a single provider across all solution areas?

**Refined:** Does MGRC have a preference between a single MSP provider across all solution areas versus multiple providers with complementary coverage?

**Changes:**
- Removed the example "(e.g., one MSP for Salesforce/CRM ecosystem and another for Oracle ERP/infrastructure)" — this reveals exactly which split we're considering
- Changed framing from "Is MGRC open to..." (reveals we want this) to "Does MGRC have a preference between..." (neutral inquiry)
- "complementary specializations" → "complementary coverage" (less specific)

**Impact:** Neutrality (HIGH PRIORITY)
**Risk Note:** Original wording flagged as medium-sensitivity. Refinement reduces signal that BayOne may not bid full scope independently.

---

### Q9: Incumbent Advantage Weighting

**Original:** For vendors who currently have resources supporting MGRC operations, how will demonstrated institutional knowledge, existing relationships, and reduced transition risk be weighted in the evaluation?

**Refined:** How will the evaluation account for a vendor's existing familiarity with MGRC operations and systems?

**Changes:**
- The original question is essentially a neon sign saying "WE ARE THE INCUMBENT, PLEASE WEIGH THIS IN OUR FAVOR"
- Refinement asks the same question but without the heavy-handed framing
- Removed "demonstrated institutional knowledge, existing relationships, and reduced transition risk" — too specific, too much coaching
- Changed from "vendors who currently have resources" (us) to "a vendor's existing familiarity" (anyone, technically)

**Impact:** Neutrality, Positioning (HIGH PRIORITY)
**Risk Note:** Original was flagged as medium-sensitivity and "aggressive competitive move." Refinement significantly reduces the telegraph while still getting useful information. Competitors will still understand the question, but it's more professionally neutral.

---

### Q18: Hybrid Pricing Model

**Original:** For pricing flexibility, is MGRC open to a hybrid model combining a fixed monthly retainer for core operational support with a flexible/variable pool of hours for enhancement, transformation, and project work? Or does MGRC prefer fully fixed pricing?

**Refined:** Is MGRC open to pricing models that combine fixed operational support with variable capacity for enhancement and project work?

**Changes:**
- Removed "fixed monthly retainer" (too specific about our structure)
- Removed "flexible/variable pool of hours" (reveals our preferred mechanism)
- "Or does MGRC prefer fully fixed pricing?" deleted — the binary choice reveals we don't want fully fixed
- New phrasing asks about model openness without prescribing the structure

**Impact:** Neutrality (HIGH PRIORITY)
**Risk Note:** Original flagged medium-sensitivity. Refinement asks the same strategic question while revealing less about BayOne's preferred commercial structure.

---

### Q19: Multi-Year Pricing Model

**Original:** For the multi-year pricing (Years 1–3), does MGRC expect flat pricing across all years, or is a ramp model acceptable where Year 1 pricing reflects onboarding investment with normalized pricing in Years 2–3?

**Refined:** For multi-year pricing, does MGRC expect flat pricing across Years 1–3, or are escalating/de-escalating structures acceptable?

**Changes:**
- Removed "where Year 1 pricing reflects onboarding investment with normalized pricing in Years 2–3" — this describes our exact strategy (aggressive Year 1, normalize later)
- "ramp model" replaced with "escalating/de-escalating structures" — technically broader, covers both directions, reveals less
- Shorter, cleaner

**Impact:** Neutrality (HIGH PRIORITY)
**Risk Note:** Original flagged medium-sensitivity for revealing Year 1 aggressive pricing strategy. Refinement maintains the question's value while obscuring intent.

---

## Questions to Consider Removing

**None recommended for removal.** All 20 questions have clear strategic or scoping purpose. Even Q9 (incumbent advantage), despite being the most openly competitive, provides legitimate value if the refined version is used.

---

## Consolidation Opportunities

| Questions | Combined Version | Benefit |
|-----------|-----------------|---------|
| Q18 + Q19 | "For pricing structure, is MGRC open to models that combine fixed and variable components, and are escalating or de-escalating multi-year structures acceptable?" | Reduces question count; both relate to pricing flexibility; combined question is still clear and answerable |

**Recommendation:** Consider consolidating Q18 + Q19 if MGRC has a limit on question count. If no limit, keeping them separate is fine — they address distinct aspects (model type vs. year-over-year trajectory).

---

## Positioning Enhancements

The refined questions collectively position BayOne as:

1. **Sophisticated but not presumptuous** — Technical questions (Q5, Q15, Q16) show depth without lecturing
2. **Pragmatic risk managers** — Transition and phasing questions (Q3, Q4, Q20) show maturity without anxiety
3. **Flexible partners** — Pricing questions (Q18, Q19 refined) signal flexibility without tipping our hand
4. **Professional neutrality** — Refined Q8 and Q9 remove the "insider advantage" signaling that could alienate evaluators who value fairness

**Subtle positioning maintained:**
- Q3 and Q4 still signal we're thinking about transition risk (desirable)
- Q5 still demonstrates integration complexity understanding
- Q13 still shows ERP operations expertise

---

## Summary of Recommended Changes

| Question | Action | Priority |
|----------|--------|----------|
| Q1 | No change | — |
| Q2 | Minor refinement | Low |
| Q3 | Minor refinement | Low |
| Q4 | Minor refinement | Medium |
| Q5 | No change | — |
| Q6 | No change | — |
| Q7 | No change | — |
| Q8 | **Significant refinement** | **High** |
| Q9 | **Significant refinement** | **High** |
| Q10 | Minor refinement | Low |
| Q11 | No change | — |
| Q12 | No change | — |
| Q13 | Minor refinement | Low |
| Q14 | No change | — |
| Q15 | No change | — |
| Q16 | Minor refinement | Medium |
| Q17 | No change | — |
| Q18 | **Significant refinement** | **High** |
| Q19 | **Significant refinement** | **High** |
| Q20 | Minor refinement | Medium |

---

## Final Notes

The four high-priority refinements (Q8, Q9, Q18, Q19) address the medium-sensitivity flags in the original catalog. These changes preserve the strategic intent while significantly reducing the competitive intelligence leak to other bidders.

All refinements follow the principle: **ask neutral questions that any sophisticated MSP might ask, while internally knowing exactly why we're asking.**
