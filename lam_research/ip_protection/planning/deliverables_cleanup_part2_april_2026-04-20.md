# Deliverables Cleanup Assessment — Part 2: April 6 and April 9 Files

**Date:** 2026-04-20
**Pass:** Full read of April 6 and April 9 deliverables checked against current canonical engagement values
**Canonical source:** Engagement values as of 2026-04-20 (per session handoff and research library)

---

## File: discovery_followup_2026-04-06.html

**Role:** client-facing (delivered post April 6 discovery meeting, pre-scoping finalization)
**Matches .md/.html counterpart?** n/a (no .md counterpart in scope)
**Status:** MIXED — historically appropriate for its moment (pre-scoping), but several statements are now stale against the current engagement shape and should not be shared as if current.

### Discrepancies Found

1. **Lines 369-381 (Use Cases Under Discussion, Self-Help vs Escalation entry-points):**
   - Quote: "Two high-level use cases have been identified, both tied to the troubleshooting workflow: … Enabling Self-Help Search … Protecting Escalation Entry Points … These are broad, high-level use cases. The specific applications, data types, and workflows involved have not yet been fully defined."
   - Why stale: The POC has since been scoped specifically to the Escalation Solver application with five free-text fields and two entity types (customer name, fab identifier). The broader "two high-level use cases, not yet defined" framing is no longer current.
   - Severity: MEDIUM (framed as exploratory at the time, but presents a larger-than-current scope if read today).

2. **Lines 428-448 (Selecting the Proof of Concept Target):**
   - Quote: "To scope a meaningful proof of concept, we need to anchor on one specific application … Starting Point … If the prior work was tested against a specific application, that application may still be the right starting point. Alternatively, the team may have identified a different, more impactful target … Signals that can help identify the right target: Which application is the most critical to daily operations? Which one has the most active users? Which one is the largest and most mature?"
   - Why stale: The Escalation Solver has been selected as the POC target. This entire targeting exercise is closed.
   - Severity: MEDIUM (obsolete as current guidance, appropriate only as historical artifact).

3. **Lines 500-525 (Hybrid Detection Architecture):**
   - Quote: "Hybrid Detection Architecture … Deterministic Layer … AI Classification Layer … Enterprise tooling such as Microsoft Purview … Hosted on Azure AI Foundry …"
   - Why stale: Current canonical methodology is a **three-layer** sequential approach (deterministic → ML/NLP → Generative AI), not a two-layer (deterministic + AI classification) hybrid. Also, the earlier Purview/Azure AI Foundry tooling pitch has been dropped in favor of the layered methodology anchored on Lam Research infrastructure (Option A confirmed 2026-04-16).
   - Severity: HIGH (misrepresents the committed methodology; does not match the POC proposal or engagement pricing one-pager).

4. **Lines 524-526 (Common Data Plane hosted in Azure):**
   - Quote: "Both detection layers are unified through a common data plane hosted in Azure."
   - Why stale: POC execution environment is now Option A (Lam Research infrastructure) per Mikhail Krivenko email 2026-04-16. The Azure-hosted data plane framing no longer aligns with the agreed POC execution.
   - Severity: HIGH.

5. **Lines 528-556 (Why Azure):**
   - Quote: The entire "Why Azure" table and accompanying paragraph — "Azure is not the only option, but it is definitively the most scalable, maintainable, and cost-effective path."
   - Why stale: Not aligned with Option A (Lam Research infrastructure) selection. Whether or not Lam's environment is on Azure is separate; the "BayOne recommends Azure deployment model" framing is stale for this POC.
   - Severity: MEDIUM (may still be directionally useful for post-POC scaling discussion, but not as current POC positioning).

6. **Lines 562-564 (A Note on Infrastructure):**
   - Quote: "The recommended approach leverages Azure enterprise services for compliance, scalability, and IT manageability … If the team has direct access to Azure infrastructure, the deployment is straightforward. If the infrastructure landscape is more complex, BayOne can adapt the approach …"
   - Why stale: Infrastructure question is resolved — Option A (Lam Research environment) is confirmed for the POC.
   - Severity: MEDIUM.

7. **Lines 579-610 (Next Steps table):**
   - Quote: "Target application — To be identified … Prior work context — To be discussed … Representative data — To be provided … Scoped proposal — Pending inputs"
   - Why stale: All four items have since advanced — target is Escalation Solver, prior work context is documented (12 Presidio → 3 parallel models: spaCy, Flair, Azure AI), data access is in progress, and scoped proposal has been delivered (poc_proposal_2026-04-09.html and engagement_pricing_2026-04-09.html).
   - Severity: LOW (clearly a pre-scoping artifact; the staleness is obvious by date).

### Recommendation

**ARCHIVE AS HISTORICAL** — This was an April 6 conversation artifact delivered before pricing and scope were locked. It served its purpose. It should not be updated to current state (that would erase its historical value and confuse with the later canonical documents). Mark as superseded by poc_proposal_2026-04-09.html + engagement_pricing_2026-04-09.html and move to a historical/archive subfolder, or simply leave in place with a note at the top of the file indicating it is superseded.

---

## File: engagement_pricing_2026-04-09.html

**Role:** client-facing (CANONICAL pricing one-pager — Lam has this)
**Matches .md/.html counterpart?** n/a (no .md counterpart)
**Status:** MIXED — core commercials are CURRENT and correct, but the Option A/B framing is now stale since Mikhail Krivenko confirmed Option A on 2026-04-16.

### Discrepancies Found

1. **Line 190 (Assumptions):**
   - Quote: "Execution environment (Lam Research infrastructure or BayOne infrastructure) agreed upon before the engagement begins, as described in the Execution Options section of this document"
   - Why stale: Option A (Lam Research infrastructure) was confirmed by Mikhail Krivenko on 2026-04-16. This assumption is now crystallized; the parenthetical choice is no longer open.
   - Severity: MEDIUM (still technically accurate since agreement was reached, but reads as if choice is pending).

2. **Lines 224-266 (Execution Options section, the Option A vs Option B comparison table):**
   - Quote: The entire Execution Options table and its trailing paragraphs describing both options as live alternatives — "Option A (Recommended): All work is performed within the Lam Research environment … Option B: BayOne performs the work on its own infrastructure using data provided by Lam Research under the existing confidentiality agreement."
   - Why stale: Option B is no longer live. Presenting it as an equivalent alternative (even with Option A marked "Recommended") is inconsistent with the 2026-04-16 Mikhail Krivenko confirmation.
   - Severity: MEDIUM-HIGH. This one-pager is the canonical client-facing pricing. If it is resent or referenced now, Lam could reasonably re-open the Option B question. However, because this was the version Lam saw before confirming Option A, it is historically correct as delivered — the staleness is only a forward-looking concern.

3. **Line 265 (Constraint note):**
   - Quote: "The three-week POC timeline begins from the date all required access and data are in place, regardless of which option is selected."
   - Why stale: "Regardless of which option is selected" is stale; option is selected.
   - Severity: LOW.

4. **Line 271 (Pricing Basis):**
   - Quote: "Pricing is the same for both execution options."
   - Why stale: Tied to the Option A/B framing that is no longer live.
   - Severity: LOW.

5. **Start date context (not present in file):**
   - No mention of "no earlier than week of May 4, 2026." This is the current canonical start-date floor. Its absence is not a discrepancy per se (the doc says "from the date BayOne has environment access, data access, and reference materials"), but if the doc is refreshed, add it.
   - Severity: LOW.

### Notes on what is CURRENT and correct

- Price: $15,000 fixed-fee, outcome-based (lines 259-260, 271) — CORRECT
- Milestone split 40/60 = $6,000/$9,000 (lines 297-304) — CORRECT
- Scope: Escalation Solver, 5 free-text fields, 4,000-5,000 characters each, customer name and fab identifier (lines 166-172, 185, 188) — CORRECT
- Three-week duration from access-in-place (line 265) — CORRECT
- Sequential layered methodology (deterministic → ML/NLP → Generative AI) (line 175) — CORRECT
- Seven committed deliverables (lines 277-285) — CORRECT (matches canonical list)
- No BayOne signatory listed in this document (Anuj Sehgal is the SOW signatory per canonical; this one-pager does not claim otherwise, so no conflict here)

### Recommendation

**KEEP AS-IS (as the delivered artifact)** — This is the document Lam has. Do not edit the delivered copy. For any future reissue or companion SOW, update to reflect Option A as confirmed and drop the comparison framing. If Colin wants a "current state" pricing one-pager to circulate internally or to attach to the SOW, create a new dated version (e.g., engagement_pricing_2026-04-20.html) that presents Option A as the confirmed environment without the Option B comparison.

---

## File: poc_proposal_2026-04-09.html

**Role:** client-facing (CANONICAL POC proposal — went to Lam)
**Matches .md/.html counterpart?** NO — substantively different from poc_proposal_2026-04-09.md. The .html is the sent version at $15,000; the .md is a stale draft at $10,000 with different assumption wording (see next file section).
**Status:** MIXED — core content is CURRENT; some references to the Option A/B framing and to the companion Engagement Pricing document's two-option structure are now stale.

### Discrepancies Found

1. **Line 636 (Assumptions):**
   - Quote: "The execution environment (Lam Research infrastructure or BayOne infrastructure) is agreed upon before the engagement begins, as described in the Engagement Pricing document"
   - Why stale: Option A is confirmed as of 2026-04-16. Framing still presents the environment as pending agreement.
   - Severity: MEDIUM.

2. **Line 647 (Dependencies):**
   - Quote: "Execution environment provisioning (VM or equivalent for Option A, data export for Option B)"
   - Why stale: Only Option A is live. The "data export for Option B" clause is no longer relevant.
   - Severity: MEDIUM.

3. **BayOne signatory not named in proposal (expected):**
   - Anuj Sehgal, VP of Sales, is the SOW signatory per canonical. This POC proposal does not include a signature block — consistent with it being a proposal rather than a contract. Not a discrepancy.
   - Severity: n/a.

4. **Start date context (not present):**
   - As with the pricing one-pager, no mention of "no earlier than week of May 4, 2026." Absence is acceptable because the proposal defers start to "data access received," but if refreshed, include.
   - Severity: LOW.

5. **Line 473 (Problem Statement):**
   - Quote: "developed over a prior 18-month effort using multiple Named Entity Recognition models in parallel"
   - Why OK: This is correct directionally. Canonical detail is 3 parallel models (spaCy, Flair, Azure AI), narrowed down from an original 12 Presidio models. The proposal generalizes to "multiple NER models in parallel," which is accurate if non-specific.
   - Severity: n/a (not a discrepancy; noted only for completeness).

### Notes on what is CURRENT and correct

- Three-week duration (executive summary, scope, and timeline) — CORRECT
- Five free-text fields, 4,000-5,000 characters each — CORRECT (line 563)
- Two entity types: customer name and fab identifier — CORRECT
- Sequential layered methodology with three layers (deterministic → ML/NLP → Generative AI) (lines 544-552) — CORRECT
- $15,000 investment (line 608) — CORRECT
- Success criteria (five items, matching canonical deliverables shape) — CORRECT
- Outcome-based engagement framing — CORRECT

### Recommendation

**KEEP AS-IS (as the delivered artifact).** This is the proposal Lam has. If a post-signature refresh is produced (e.g., to attach to the SOW), update the two Option A/B references noted above. Otherwise leave in place.

---

## File: poc_proposal_2026-04-09.md

**Role:** DRAFT (stale — never sent; superseded by the .html version which went to Lam)
**Matches .md/.html counterpart?** NO — substantively different. Stale on price and execution-environment assumption.
**Status:** STALE

### Discrepancies Found

1. **Line 110 (Investment table):**
   - Quote: "| **Proof-of-Concept (This Proposal)** | **$10,000** |"
   - Why stale: Canonical price is **$15,000**, not $10,000. The .html version that Lam received says $15,000. This .md is a pre-increase draft.
   - Severity: HIGH (misrepresents current commercial commitment by $5,000).

2. **Line 126 (Assumptions bullet):**
   - Quote: "The POC runs on BayOne infrastructure unless there is a specific requirement to operate within the Lam Research environment, in which case BayOne will need details about the existing environment and its availability."
   - Why stale: This is the pre-Option-A default framing. Option A (Lam Research infrastructure) was confirmed by Mikhail Krivenko on 2026-04-16. Also, this text does not match the .html version's assumption wording (which instead points to the Engagement Pricing document and the Execution Options section).
   - Severity: HIGH (directly inverts the now-confirmed execution environment).

3. **Line 128 (Assumptions bullet about timeline extension):**
   - Quote: "Lam Research provides timely feedback and validation during the POC period. If response times extend beyond an agreed window, the POC timeline extends accordingly."
   - Why stale: The canonical/.html version uses the more formal "50% of remaining engagement duration" change-request trigger language. This .md uses the older softer language.
   - Severity: MEDIUM.

4. **No Option A / Option B framing at all, no Execution Options section:**
   - Why stale: The .html and the companion engagement_pricing one-pager both carry Option A/B framing (which is itself now being retired due to the 2026-04-16 confirmation). This .md was written before that framing was introduced, which is why it falls back to "BayOne infrastructure by default."
   - Severity: HIGH at a draft-level; the draft as a whole represents a prior state of the proposal.

5. **Line 12 (Executive Summary):**
   - Quote: "BayOne Solutions proposes a three-week proof-of-concept engagement …"
   - Why OK: Duration is correct and matches canonical.
   - Severity: n/a.

6. **No milestone payment structure:**
   - The .md investment section lists a single $10,000 line and four descriptive rows. No 40/60 milestone split. The canonical 40/60 ($6,000/$9,000) structure is absent.
   - Severity: HIGH (missing the milestone commitment that is now canonical).

### Recommendation

**DELETE** (with Colin's explicit sign-off) or at minimum **ARCHIVE AS HISTORICAL** with a prominent DRAFT / SUPERSEDED header added to line 1. Per canonical feedback ("Never make unilateral decisions"), I recommend flagging this for Colin's deletion decision rather than deleting outright. The file is a stale $10,000 draft that contains the inverted execution-environment default. It presents real risk if someone opens it thinking it reflects the current commitment.

---

## File: internal_cost_breakdown_2026-04-09.html

**Role:** internal (marked "Do Not Share With Client" — internal accounting artifact)
**Matches .md/.html counterpart?** n/a (no .md counterpart)
**Status:** MIXED — internal figures are current-looking but one line drifts from the Option A confirmation.

### Discrepancies Found

1. **Line 155 (Engagement Summary table, Environment row):**
   - Quote: "BayOne infrastructure (unless Lam requires otherwise)"
   - Why stale: Option A (Lam Research infrastructure) was confirmed 2026-04-16. Internal execution environment assumption should now read "Lam Research infrastructure (confirmed per Mikhail Krivenko 2026-04-16)."
   - Severity: MEDIUM (internal doc, not seen by client, but drives internal cost planning — affects infrastructure line and possibly travel/VM-access assumptions).

2. **Line 217-222 (Cost Buildup — Infrastructure row at $0):**
   - Quote: "Infrastructure | $0.00 | BayOne environment; minimal compute"
   - Why stale: Under Option A, BayOne is operating in Lam Research's environment. Infrastructure cost to BayOne remains effectively zero for the POC (Lam provides the VM), which is actually still consistent with $0 — but the NOTE "BayOne environment; minimal compute" is inverted. Should read "Lam environment; compute provided by Lam."
   - Severity: LOW (the dollar figure is still correct; only the explanatory note drifts).

3. **Line 263 (Margin Analysis note):**
   - Quote: "The travel investment supports Anuj's recommendation for in-person presence during the POC, which strengthens the relationship with Brad's team."
   - Why OK: Brad Estes as decision-maker / Managing Director is canonically correct. Anuj (Sehgal) is correctly identified as sales leadership. No staleness.
   - Severity: n/a.

4. **Line 270 (Strategic Context):**
   - Quote: "Brad (Managing Director, decision-maker) reviews the proposal and is expected to provide a decision within one week of receipt."
   - Why stale: The "expected to provide a decision within one week of receipt" timing assumption may be outdated depending on where we are in the April 9 → April 20 timeline. Check against actual signoff status; if Lam has already confirmed Option A on April 16, the decision loop has substantively progressed.
   - Severity: LOW (internal context, aging prediction).

5. **Line 173 (Personnel Cost table, Colin's line):**
   - Quote: "Colin Moore (Director of AI)"
   - Why OK: Title is correct per canonical.
   - Severity: n/a.

### Notes on what is CURRENT and correct

- Client price $15,000 fixed, outcome-based (line 147) — CORRECT
- Duration: three weeks (one discovery, two build) (line 151) — CORRECT
- Colin as Director of AI — CORRECT
- Brad as Managing Director / decision-maker — CORRECT
- Anuj as commercial owner (implied) — CORRECT

### Recommendation

**UPDATE IN PLACE** — Two small edits on the Environment row (line 155) and the Infrastructure note (line 223) to align with Option A confirmation. This is a live internal accounting artifact; keeping it accurate matters for internal planning. Do NOT delete (it is a financial/margin record). The updates are cosmetic but useful.

---

## File: pricing_breakdown_2026-04-09.html

**Role:** client-facing (no "internal" marking; references the Engagement Pricing document and POC Proposal as companion documents, which implies this is in the client-deliverable bundle)
**Matches .md/.html counterpart?** n/a (no .md counterpart)
**Status:** MIXED — phase-level BOM, totals, and milestone splits are CURRENT; one reference to "execution options" is now stale.

### Discrepancies Found

1. **Line 221 (Pricing Basis):**
   - Quote: "Pricing is the same for both execution options (Lam Research environment or BayOne environment) as described in the Engagement Pricing document."
   - Why stale: Option A is confirmed; both-options framing is obsolete.
   - Severity: MEDIUM.

2. **Line 234 (Reference):**
   - Quote: "This document supplements the Confidential Information Detection POC Proposal and Engagement Pricing documents dated April 2026. Success criteria, proposed approach, execution options, assumptions, exclusions, risk factors, and terms are detailed in those documents."
   - Why stale: The phrase "execution options" ties this doc to a now-stale framing.
   - Severity: LOW.

### Notes on what is CURRENT and correct

- Phase 1 at $6,000 (40%) and Phase 2 at $9,000 (60%) — CORRECT and aligned to canonical milestone split
- Total $15,000 fixed price — CORRECT
- Three-layer sequential methodology (deterministic, ML/NLP, Generative AI) represented across Phase 2 line items (lines 181-191) — CORRECT
- Scope: two entity types (customer name, fab identifier), five free-text fields, Escalation Solver — CORRECT
- Exclusions list matches canonical — CORRECT
- References EDA report, benchmarking, evaluation protocol, methodology documentation, scaling path, reference-data refinement recommendations — matches canonical 7-deliverable list

### Recommendation

**KEEP AS-IS (as the delivered artifact)** OR **UPDATE IN PLACE** if this is going to continue to be circulated post-confirmation. If part of the final SOW package, update line 221 to drop the two-options framing and line 234 to remove "execution options" from the list of topics covered in companion documents. If this is the delivered artifact Lam already has, leave in place and produce a refreshed version only if a new dated circulation is planned.

---

## Summary

| File | Status | Recommendation |
| --- | --- | --- |
| discovery_followup_2026-04-06.html | MIXED | ARCHIVE AS HISTORICAL |
| engagement_pricing_2026-04-09.html | MIXED | KEEP AS-IS (delivered); new dated version if refresh needed |
| poc_proposal_2026-04-09.html | MIXED | KEEP AS-IS (delivered); update two Option A/B lines only if refreshed |
| poc_proposal_2026-04-09.md | STALE | NEEDS DISCUSSION — recommend DELETE or ARCHIVE with prominent DRAFT/SUPERSEDED header |
| internal_cost_breakdown_2026-04-09.html | MIXED | UPDATE IN PLACE (two small edits to Environment row and Infrastructure note) |
| pricing_breakdown_2026-04-09.html | MIXED | KEEP AS-IS (delivered); update two lines only if refreshed |

**Observations across the file set:**

There are two distinct staleness patterns across this set. The first is the **poc_proposal .md versus .html divergence**: the .md is a clear pre-increase, pre-Option-framing draft at $10,000 with the inverted "BayOne infrastructure by default" assumption. It does not match the .html that went to Lam. Anyone opening the .md thinking it reflects current commitment will be off by $5,000 and wrong about where the work happens. This is the single highest-risk staleness finding in the set and should be resolved by either deletion (with Colin's sign-off) or a prominent DRAFT/SUPERSEDED header.

The second pattern is the **April 16 Option A confirmation** that has not yet been back-propagated to the April 9 client-facing documents (pricing one-pager, POC proposal, pricing breakdown). All three still present Option A and Option B as live alternatives and the environment as pending agreement. For the versions Lam already received, this is acceptable — the documents were correct as of the moment they were delivered. But if any of these are reissued, attached to the SOW, or referenced as "current state," the Option A/B comparison framing needs to be retired. Recommend generating refreshed 2026-04-20 (or SOW-attachment-dated) versions of the pricing one-pager and pricing breakdown that present Option A as the confirmed execution environment, without the comparison.

The **discovery_followup_2026-04-06.html** is a different case: it is historically appropriate (pre-scoping), but if someone uses it today as a "BayOne's methodology and approach" reference, they will get the wrong two-layer architecture (deterministic + AI classification, with Azure Purview / AI Foundry as the recommended tooling) rather than the canonical three-layer sequential methodology. This is a HIGH-severity methodology drift in a document that some might still reach for. Archive it with a supersession marker.

The **internal_cost_breakdown** is almost entirely correct — the margin numbers and personnel costs still reflect the $15,000 price point. The two minor drifts (Environment row and Infrastructure note) are easily fixed in place and the file should be kept as an internal accounting record regardless.
