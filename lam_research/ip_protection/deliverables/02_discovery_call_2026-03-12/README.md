# Set 02 — Discovery Call Deliverables

**Set:** 02 (Discovery Call, 2026-03-12)
**Deliverable Creation Date:** 2026-03-20
**Status:** Sent to Lam Research
**Audience:** Client-facing

---

## Purpose

These are the four client-facing artifacts produced after BayOne's initial discovery call with Lam Research on 2026-03-12. They were drafted collaboratively during the March 20 discussion (research Sets 02, 02a, and 03) and delivered to Brad Estes and Mikhail Krivenko shortly after.

The purpose of this set was to demonstrate BayOne's understanding of the problem before proposing any solution, request the specific information needed to scope an engagement, and offer a preliminary direction for discussion.

---

## Files in This Set

| File | Purpose |
|---|---|
| `problem_restatement_2026-03-12.md` / `.html` | BayOne's restatement of the problem as heard during discovery, intended to confirm alignment before any solution work |
| `preliminary_approach_2026-03-12.md` / `.html` | Initial BayOne thinking on how to address the challenge, framed as early direction for discussion rather than a committed plan |
| `information_request_2026-03-12.md` / `.html` | Prioritized list of questions BayOne needed answered to move from understanding to scoping |
| `followup_email_draft_2026-03-12.md` | Cover email to Brad and Mikhail accompanying the three attached documents |

---

## Relationship to Research Library

Research sources that fed these deliverables:

- **Set 01** (call prep, 2026-03-12)
- **Set 02** (discovery meeting transcript, 2026-03-12)
- **Set 02a** (internal debrief, 2026-03-12)
- **Set 03** (working discussion, 2026-03-20, where the deliverables were drafted collaboratively)

---

## Important Context: These Are an Earlier State of Understanding

The understanding reflected in these documents represents what BayOne knew as of 2026-03-20, immediately after the discovery call. Subsequent events substantially evolved the engagement:

- **Set 05** (2026-04-06 second client meeting) refined the target scope from "customer names and file names" to **customer names and fab identifiers** and identified Escalation Solver as the target application. It also revealed that Lam's prior ML work used spaCy, Flair, and Azure AI (narrowed from 12 Presidio models with parallel reconciliation), not just "Transformers, spaCy, and an Azure AI model" as stated in these documents.
- **Sets 06 through 08a** (2026-04-09) crystallized commercial terms into a fixed-fee, outcome-based POC at $15,000, three weeks from data access, with 40/60 milestone payments. The methodology committed became the three-layer sequential detection approach (deterministic → ML/NLP → Generative AI), which is more specific than the "hybrid deterministic + AI classification" framing in `preliminary_approach`.
- **Set 09** (2026-04-16 to 2026-04-17) confirmed Option A (Lam Research environment) as the execution mode and opened the contract phase with the SOW under MSA BAYON-MAS-0013142.

These documents are NOT to be edited. Per the Singularity blockchain methodology, they represent BayOne's understanding at a specific point in the engagement timeline and are preserved as part of the historical record. Their value is in showing the evolution of thinking, not in being current.

For the current engagement commitment, refer to `../06_pricing_and_proposal_2026-04-09/`.

---

## Known Drift Between `.md` and `.html`

The `.md` and `.html` versions in this set are largely mirrors of each other, but a discrepancy audit on 2026-04-20 found:

- `information_request_2026-03-12.html` contains a duplicated "Representative Data Samples" section (appears as both 1.2 and 2.1) that is not present in the `.md` version.
- `problem_restatement_2026-03-12.html` softens some named customer examples compared to the `.md` version.

These drifts exist in the historical record as-is. They are flagged here for transparency. Because these documents represent an earlier state, they are not to be reconciled or edited.
