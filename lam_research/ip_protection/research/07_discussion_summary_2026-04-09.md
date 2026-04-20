# 07 - Discussion: Summary

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-04-09 (POC pricing and scope brainstorm)
**Document Set:** 07 (Pricing Discussion)
**Pass:** Summary

---

## Overview

Document Set 07 captures a working discussion between Colin Moore and Claude on April 9, 2026, to define the complete POC proposal for the Lam Research IP Protection engagement. The discussion covered deliverables, timeline, success criteria, assumptions, risks, document structure, and pricing. Two files: `07_discussion_pricing_scope_2026-04-09.md` (10 exchanges covering structure) and `07_discussion_pricing_exercise_2026-04-09.md` (3 exchanges working through the costing model).

## Files in This Set

1. **07_discussion_pricing_scope_2026-04-09.md** - Ten exchanges covering: POC deliverables (comparative detection demonstration, EDA report, methodology documentation, accuracy report), timeline (three weeks from access), success criteria (five, no accuracy commitment before discovery), twelve assumptions, five risks with mitigations, and the two-document proposal structure (same as Cisco EPNM/EMS).

2. **07_discussion_pricing_exercise_2026-04-09.md** - Three exchanges working through the costing model using Cisco workbook rates. Colin at 10% allocation ($103.85/hr loaded), one mid-level offshore resource at 100% ($33.00/hr loaded). Base personnel cost: $5,206.20. With 25% risk reserve: $6,507.75 loaded. Final price: $10,000. Base margin: 47.9%. Loaded margin: 34.9%.

## Key Decisions

### Deliverables
- The POC is a comparative detection demonstration, not a production application or IP transfer
- Detection only, not redaction (redaction is just detection with a downstream action)
- EDA report as a formal engineering document (discovery week output)
- No accuracy commitment before seeing data. BayOne reports maximum achievable accuracy after discovery.
- No full-scope engagement estimate (scope is undefined, must come from Lam)
- Ground truth definition is Lam's prerequisite, not a BayOne deliverable

### Timeline
- Three weeks from access: one week discovery, two weeks build
- Full POC timer starts from access, not just the build timer
- "Access" means the data, reference lists, labeled examples, and all information available to the prior effort

### Pricing
- $10,000 outcome-based, no headcount disclosed
- Internal cost: Colin 12 hrs ($1,246.20) + offshore mid 120 hrs ($3,960.00) = $5,206.20 base
- 25% risk reserve: $1,301.55
- Loaded cost: $6,507.75
- Base margin: 47.9%, loaded margin: 34.9%
- Internal document shows Colin as total only (no hourly rate), India resource with hourly and total

### Proposal Structure
- Two documents, same structure as Cisco EPNM/EMS engagement
- Document 1 (POC proposal): cover page, executive summary, problem statement with five success criteria, proposed approach in two phases, scope and timeline, assumptions (12), risks (5), next steps
- Document 2 (pricing breakdown): letterhead BOM table with phases, sub-line items, $10,000 total, pricing basis

### Success Criteria
1. Baseline data assessment completed with data quality evaluation and maximum achievable accuracy determination
2. Detection approach demonstrated against real Escalation Solver data for two entity types across five fields
3. Detection performance measured and reported using a defined evaluation protocol that can be repeated and built upon
4. Documented approach showing the layered detection methodology and how each layer contributes
5. Clear path documented for how the approach scales from POC to full engagement

### Assumptions (12)
1. Data access is the starting gate (three-week clock starts from access)
2. Baseline data quality bounds accuracy (discovery assesses, if contradictory must be addressed first)
3. Detection scope: five free-text fields, two entity types (customer name, fab ID)
4. No production integration
5. Lam provides a subject matter expert to define goalposts and validate results
6. POC runs on BayOne's environment unless critical need for Lam infrastructure
7. Lam manages internal coordination for data access within reasonable timeframe
8. Data volume and scope defined upfront (2,000 vs. 500,000 is a different exercise)
9. Confidentiality and data handling per requirements, customer names redacted from BayOne documents
10. Lam provides existing reference data (entity lists, exclusion lists, labeled examples), not prior code
11. Timely feedback and validation from Lam during POC period
12. Ground truth data quality is Lam's responsibility; BayOne reports on refinement needs but does not fix ground truth within POC scope

### Risks (5)
1. Data quality issues discovered during EDA
2. Data access delays due to Lam internal coordination
3. SME availability constraints compress build window
4. Data volume exceeds three-week POC capacity
5. Scope creep beyond agreed five fields / two entity types

## Corrections During This Discussion

Three significant corrections were made during this discussion, all documented in `planning/skill_notes.md`:

1. **Proposed deliverables contradicted the research library.** Golden set creation (Lam's responsibility), detection/redaction framing (false dichotomy per Set 05a), and full-scope estimate (explicitly ruled out in Set 06) were all proposed incorrectly.

2. **Tried to combine two documents into one.** The Cisco engagement produced two distinct documents. Claude questioned whether to follow this structure instead of replicating it.

3. **Described document structures without reading the source HTML.** Claude fabricated content descriptions (percentage-weighted phases, "Why BayOne" section) that did not exist in the actual Cisco documents.

## State After This Set

The proposal is fully defined: deliverables, timeline, success criteria, assumptions, risks, pricing, and document structure. Ready to produce:
- Document 1: Lam POC proposal (HTML, BayOne design spec)
- Document 2: Pricing breakdown (HTML, letterhead format)
- Internal document: Cost breakdown for BayOne team
