# Sets 06 through 08a — Pricing and POC Proposal

**Sets:** 06 (internal pricing), 07 (pricing discussion), 08 (internal sync 2), 08a (pricing revision) — all 2026-04-09
**Deliverable Creation Date:** 2026-04-09
**Status:** Sent to Lam Research (except `internal_cost_breakdown` which is internal-only)
**Audience:** Mixed (see per-file notes)

---

## Purpose

This set contains the finalized POC proposal and pricing artifacts. These documents reflect the current engagement commitment as of 2026-04-20 and are the documents BayOne will reference when discussing scope, timeline, price, and methodology with Lam Research through the execution of the POC.

The POC commitment captured in this set:

- **Price:** $15,000 fixed-fee, outcome-based
- **Milestones:** 40% on Phase 1 Discovery complete ($6,000) / 60% on Phase 2 Build complete ($9,000)
- **Duration:** Three weeks from the date BayOne receives all required access
- **Start:** No earlier than the week of 2026-05-04 (per SOW-specific assumption in Set 09)
- **Scope:** Escalation Solver, five free-text fields, two entity types (customer name and fab identifier)
- **Methodology:** Three-layer sequential detection (deterministic → machine learning and NLP → generative AI)
- **Execution environment:** Option A (Lam Research environment), confirmed by Mikhail Krivenko on 2026-04-16 in Set 09

---

## Files in This Set

| File | Purpose | Audience |
|---|---|---|
| `engagement_pricing_2026-04-09.html` | Client-facing engagement-pricing one-pager; the canonical written commitment on price, milestones, and execution options | Client-facing |
| `poc_proposal_2026-04-09.md` / `.html` | Client-facing POC proposal; full narrative including problem statement, approach, scope, assumptions, risks, next steps | Client-facing |
| `pricing_breakdown_2026-04-09.html` | Client-facing pricing breakdown supporting the engagement pricing one-pager | Client-facing |
| `internal_cost_breakdown_2026-04-09.html` | **INTERNAL ONLY — do not share with Lam.** Contains BayOne-side cost, loaded rates, margin analysis, and commercial strategy | Internal |

---

## `.md` and `.html` Pairing

Only `poc_proposal_2026-04-09` has both `.md` and `.html` versions. The `.md` was updated on 2026-04-20 to mirror the content of the `.html`; before that date, the `.md` was a stale earlier-draft copy that showed $10,000 and an out-of-date assumption about BayOne infrastructure as the default execution environment. Both versions are now aligned on the current $15,000, three-week, three-layer, Option A-anticipating content.

The other three files in this set are HTML-only. Per Singularity deliverables convention, every client-facing HTML should have a matching markdown source. These missing pairs are known gaps:

- `engagement_pricing_2026-04-09.md` — missing
- `pricing_breakdown_2026-04-09.md` — missing
- `internal_cost_breakdown_2026-04-09.md` — missing (internal file; pairing convention still applies)

Creating the missing markdown sources is a remediation candidate for a future session.

---

## Relationship to Research Library

Research sources that fed these deliverables:

- **Set 06** (internal pricing call, 2026-04-09) — established the pricing and margin framework
- **Set 07** (pricing exercise discussion, 2026-04-09) — refined the commercial structure
- **Set 08** (internal sync 2, 2026-04-09) — final internal alignment on price and structure
- **Set 08a** (pricing revision discussion, 2026-04-09) — landed the $15,000 commitment and the milestone split

---

## Current Status vs. Later Evolution

These documents are the current engagement commitment. Set 09 (2026-04-16 to 2026-04-17) did not supersede them but did add two items that sit alongside:

1. **Option A (Lam Research environment) is confirmed.** The engagement-pricing one-pager presents Options A and B as equivalent alternatives at the same price; Mikhail's 2026-04-16 email confirmed Option A as Lam's preference. Neither document in this set has been reissued to reflect the confirmation because the price commitment did not change and Lam has the original already.
2. **SOW has been issued under MSA BAYON-MAS-0013142.** The SOW filling work happens in `../../planning/sow_filling_instructions_word_claude_*.md`. The SOW content is consistent with the commitments captured here.

For downstream work (SOW content, technology access coordination), refer to research Set 09 and the related planning documents.

---

## Handling Rule

These documents are the CURRENT state of the engagement's commercial commitment. They remain in place and in use. They are not edited retroactively unless Lam Research and BayOne jointly agree to a change, which would be captured in a new set with a bridge document in the research library.

The only edit made on 2026-04-20 was the `poc_proposal_2026-04-09.md` reconciliation to match its `.html` counterpart, which corrects a prior drift (the `.md` had never been updated from its $10,000 early-draft state). That edit is a pairing remediation, not a change to the current commercial commitment.
