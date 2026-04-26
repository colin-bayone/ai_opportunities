# 09 - SOW Template: Filling Strategy (Favorable + Defensible)

**Source:** /lam_research/ip_protection/source/lam_sow.pdf, plus deliverables/engagement_pricing_2026-04-09.html, plus deliverables/poc_proposal_2026-04-09.md
**Source Date:** 2026-04-17 (SOW arrival; engagement commitments dated 2026-04-09)
**Document Set:** 09 (Execution Kickoff)
**Pass:** Strategic positioning for filling each SOW section favorably and defensibly for BayOne

---

## Purpose of This Document

The Lam Research SOW template arrived pre-populated with filler text lifted from a prior engagement (a GCS Data Lake data engineer role at $37/hr for 320 hours). Sarthak's draft language is generic, time-and-materials oriented, and reveals hourly rates on the document face. It does not match what BayOne has committed to Lam in writing via the POC Proposal (2026-04-09) and Engagement Pricing one-pager (2026-04-09).

This document walks the SOW section by section and establishes, for each one:

- **Recommended content** (what actually goes in the SOW).
- **Why it's favorable** (protects BayOne margin, IP, scope boundaries, and follow-on pricing leverage).
- **Why it's defensible** (consistent with written commitments to Lam, with the MSA BAYON-MAS-0013142, and with procurement norms).
- **Alternative considered and rejected** (so the drafter knows the roads not taken).

The locked inputs for this exercise:

- **Pricing model: fixed-fee, deliverable-based. No hourly rates on the SOW.** Colin has explicitly directed that the rate columns in the template must not be used. The Fee Schedule table is being restructured to Phase / Deliverable / Fixed Fee summing to $15,000 NTE. This is not negotiable within this document.
- **Execution mode: Option A (Lam environment) confirmed by Mikhail on 2026-04-16.** Equipment and access sections should anticipate Lam-provided environment access.
- **Scope, deliverables, assumptions, exclusions: locked in the 2026-04-09 proposal and engagement pricing one-pager.** The SOW references those documents, it does not re-negotiate them.

---

## Header / Letterhead / Document Identifier

### Recommended content

- **Letterhead:** Keep the existing BayOne Pleasanton address block as-is (4637 Chabot Dr., Suite 200, Pleasanton, CA 94588). This SOW is BayOne's document on BayOne's paper, issued pursuant to the MSA between the two parties. The template arrived with BayOne letterhead correctly in place.
- **Document identifier "BAYONE-SOW":** Keep as-is. This is the boilerplate document type marker BayOne uses across clients.
- **MSA reference "[BAYON-MAS-0013142]":** Keep as-is. This is the master Contract for Independent Contractor or Consultant Services between Lam Research and BayOne, effective June 12, 2018. The template language "made pursuant to that certain Contract..." correctly incorporates the MSA, which is what gives the SOW its legal standing and its default terms for payment (Section 4), acceptance (Section 3), and capitalized-term definitions. Do not modify this block.
- **Effective Date:** **RECOMMEND 2026-04-24 (Friday of the signature week) or the date of BayOne countersignature, whichever is later.** The template shows "Feb 1, 2026" which is the placeholder Sarthak inherited from the prior SOW. That date is stale by more than two months and does not correspond to any actual event in this engagement.

### Why 2026-04-24 (or countersignature date)

- The session handoff establishes Brad's decision timing as "approximately April 17." Mikhail's email on 2026-04-16 confirms Option A, which implies internal alignment on the Lam side. A one-week pad from April 17 to April 24 absorbs Brad's signature routing, procurement review, and Sripriya's (or designated BayOne signer's) countersignature.
- **The Effective Date is symbolic, not operational.** It does not control the start of the POC clock. That clock is separately governed by the SOW Term clause, which we are tying to data and environment access (see SOW Term section below). Picking a slightly-future Effective Date avoids the appearance of back-dating while keeping the access-triggered start intact.

### Alternative considered: use the date the SOW is signed by both parties

- This is defensible and is how the template is usually executed in practice ("Executed the latest date below by the authorized representatives of the parties for the SOW Effective Date" is the concluding line on page 3).
- Rejected as the primary recommendation only because a specific date in the header provides a more concrete anchor for reference in follow-on correspondence and invoices. The template accepts either form; the primary recommendation and the alternative are effectively interchangeable.

### Alternative considered and rejected: leave Feb 1, 2026 in place

- Rejected outright. Back-dating a two-month-old Effective Date creates an audit trail problem, misrepresents when the engagement was formed, and could create timing ambiguity against the MSA's payment terms (30-day invoice cycle). Do not do this.

---

## Section 1: Services to be Provided

The template's arrived content is a seven-line description lifted from the GCS Data Lake engagement ("Implement new customer requirements and features in our existing application... Designs, develops, troubleshoots, and debugs software programs..."). This is generic staff-augmentation language for an open-ended data engineer role. It does not describe the Escalation Solver POC and, critically, it contains no scope boundaries.

### Recommended content

**Project name (first line, bolded):**

> **Confidential Information Detection - Proof of Concept (Escalation Solver)**

**Services description (paragraph form, replacing the seven-line filler):**

> Contractor shall perform a three-week proof-of-concept engagement to demonstrate an improved detection methodology for customer-confidential information within the Escalation Solver application. The engagement is delivered in two phases: a Discovery and Data Assessment phase (Phase 1) and a Detection Build and Benchmarking phase (Phase 2).
>
> Services under this SOW are limited to the following scope:
>
> - Application in scope: Escalation Solver (five free-text fields, approximately 4,000 to 5,000 characters each).
> - Entity types in scope: customer name and fab identifier.
> - Duration: three weeks from the date BayOne receives all required access (environment access, data access, reference materials, and SME availability).
>
> Phase 1 deliverables: an exploratory data analysis report including baseline data quality assessment, maximum achievable detection accuracy determination against the available reference data, and documentation of detection targets.
>
> Phase 2 deliverables: a working detection demonstration against real Escalation Solver data for the two in-scope entity types, benchmarking of detection performance against the prior effort baseline as documented by Lam Research, documentation of the layered detection methodology, and a scaling path for extending the approach to additional entity types, fields, and applications in subsequent engagements.
>
> The full scope, assumptions, exclusions, risk factors, and success criteria are as described in the Confidential Information Detection POC Proposal (April 2026) and the Engagement Pricing one-pager (April 2026), which are incorporated by reference into this SOW. In the event of any conflict between those documents and this SOW, this SOW controls.

### Why this is favorable

- **Bounded, not open-ended.** The template's filler language ("Implement new customer requirements and features... Maintain existing code base...") is unbounded in a way that suits a long-running staff augmentation role but is dangerous for a fixed-fee POC. Under that language, a client could reasonably argue that any "new customer requirement" during the three weeks is within scope. The recommended language enumerates the deliverables and caps the scope to five fields and two entity types.
- **Outcome language, not effort language.** "Demonstrate an improved detection methodology" and "exploratory data analysis report... working detection demonstration... scaling path" are deliverables BayOne owes at completion. There is no hour-based or staffing-based commitment in this language. This matches Colin's stated pricing philosophy (Set 06: "billed by outcome and by deliverable") and the Cisco precedent.
- **References the proposal and pricing doc, doesn't re-state them.** Pulling every assumption and exclusion into the SOW itself would quadruple the SOW length and create a second version of truth that may conflict with the originals. The incorporation-by-reference clause, plus the explicit priority clause ("in the event of any conflict, this SOW controls"), preserves the protections in the proposal while keeping the SOW tight.
- **Makes the three-week clock trigger explicit.** Embedding "from the date BayOne receives all required access" in the services description, not just the SOW Term, means any later scope debate can point to the services description itself as evidence that delayed access delays the engagement, not the fee.

### Why this is defensible

- The content is pulled from the POC Proposal (2026-04-09) and Engagement Pricing one-pager (2026-04-09), both of which Lam has had for a week. Nothing in this language is new to the Lam side.
- The two-phase structure matches the Milestone Payments table Lam has already seen ($6,000 Phase 1, $9,000 Phase 2).
- Incorporation of proposal and pricing documents by reference is standard contracting practice. The priority clause protects against document-conflict ambiguity.

### Alternative considered and rejected: keep Sarthak's filler language

- Rejected. The seven-line filler is time-and-materials language for operational support work. It does not describe the POC, and its open-endedness would undermine the fixed-fee structure.

### Alternative considered and rejected: fully restate all assumptions and exclusions in Section 1

- Rejected. The proposal has nine assumptions and five exclusions. Restating them in the SOW creates two places where the same language lives, which is a source of future conflict. The incorporation-by-reference approach is cleaner and industry-standard.

### Alternative considered and rejected: write "Services will be performed in accordance with the POC Proposal dated April 2026" with no elaboration

- Rejected. Too thin. Procurement reviewers expect Section 1 to describe the services on its face, not redirect immediately to an external document. The recommended approach gives enough detail for a procurement reviewer to understand what is being purchased without requiring them to open the proposal, while still pointing them to the proposal for the full assumptions and exclusions.

---

## Section 2: Acceptance Criteria

The template offers three options: "Not applicable," "See immediately below," or "Acceptance criteria shall be as set forth in Section 3 of the Agreement [MSA]."

### Recommended content

Select: **"Acceptance criteria shall be as set forth in Section 3 of the Agreement."**

Leave the "Additional sheets attached" checkbox unchecked.

### Why this is favorable

- **The MSA default is industry-typical.** Without reading the MSA verbatim, we can infer from standard contracting practice that Section 3 of a Contract for Independent Contractor Services contains a reasonable acceptance regime: Lam inspects deliverables within a defined window, raises written objections if any, and failing timely objection the deliverables are deemed accepted. This is favorable to BayOne.
- **Custom acceptance criteria are a trap.** If we listed the specific deliverables as acceptance items (the EDA report "must contain X, Y, Z"; the detection demonstration "must achieve N% accuracy"), we invite a procurement-driven checklist review where each item becomes a veto point. For a methodology POC where the ceiling of achievable accuracy is an output of the discovery phase (not an input), committing to a numeric acceptance threshold up front is a margin-kill scenario.
- **Avoids creating a Lam-side sign-off bottleneck.** Custom acceptance criteria typically require named sign-off by a specific Lam representative. Given the org structure (Brad owns, Mikhail drives, Daniel is a distractor, Orion controls data access), custom acceptance would create ambiguity about who signs off. The MSA's default leaves this to the companies, not named individuals, which is cleaner for invoicing.

### Why this is defensible

- The template explicitly offers this option and it is the most common selection in master-services-driven engagements.
- The POC Proposal's "Success Criteria" section already describes what a successful POC looks like (five bullets covering baseline assessment, demonstration against real data, measured performance, documented methodology, scaling path). These are reputational success criteria, not contractual ones. Keeping them out of the SOW acceptance clause preserves their rhetorical value without making them veto levers.

### Alternative considered and rejected: list the five Phase 1 and Phase 2 deliverables as acceptance items

- Rejected. Too rigid. Each deliverable becomes a sign-off gate, and Lam's acceptance timeline can stretch invoice collection. The per-milestone invoicing model (see Invoice schedule section below) already ties payment to delivery, which is sufficient commercial alignment.

### Alternative considered and rejected: select "Not applicable"

- Rejected. "Not applicable" looks odd for a deliverable-based engagement, invites procurement pushback, and loses the MSA's default protections. Always prefer the MSA reference over "Not applicable" unless the MSA default is genuinely inapplicable, which is not the case here.

---

## Section 3: Fee Schedule

This section is the most sensitive part of the template. The filler row shows "Data Engineer | 1 | 320 | $37/hr. | $11,840" — a textbook T&M row with role, quantity, hours, rate, and total. Colin has explicitly directed that **no hourly rates appear on the SOW**.

### Recommended content

Restructure the table header and rows. Replace the existing table with:

| Phase / Deliverable | Quantity | Fixed Fee |
| :--- | :--- | :--- |
| **Phase 1: Discovery and Data Assessment** — Exploratory data analysis report, baseline data quality assessment, maximum achievable detection accuracy determination | 1 | $6,000 |
| **Phase 2: Detection Build and Benchmarking** — Working detection demonstration, benchmarking against prior effort baseline, layered detection methodology documentation, scaling path | 1 | $9,000 |
| **Total (Not to Exceed)** | | **$15,000** |

Precede the table with the following sentence, replacing Sarthak's "This project will be implemented on a time and material basis and following are the hourly rate and estimated costs":

> This engagement is delivered on a fixed-fee, deliverable-based model. The following are the agreed deliverables and fixed fees:

### Row-by-row reasoning

- **Phase 1 / $6,000:** Matches the 40% milestone payment in the Engagement Pricing one-pager ($6,000 on EDA report delivery). The deliverable description is slightly compressed from the proposal but preserves the three substantive outputs (EDA, baseline assessment, maximum achievable accuracy).
- **Phase 2 / $9,000:** Matches the 60% milestone payment ($9,000 on detection build, benchmarking, methodology, scaling path delivery). All four Phase 2 deliverables are named on the SOW face, so there is no ambiguity about what triggers the milestone.
- **Total (Not to Exceed) / $15,000:** Matches the Total Amount (Not to Exceed) field on page 2, matches the engagement pricing one-pager, matches the proposal. The NTE framing is consistent with the template language on page 2.

### Why this is favorable

- **No hourly rate appears anywhere.** This is the single most important protection in this document. Once a rate appears on a signed SOW, it becomes the anchor for every follow-on pricing conversation. A $37/hr Data Engineer rate on a POC would cap BayOne's follow-on engagement pricing for the next several years at rates that make a full-scope engagement unprofitable. By keeping only fixed fees on the SOW, any follow-on engagement is priced against a completely new basis.
- **Quantity of "1" rather than hours.** The "Quantity" column is preserved (since it exists in the template), set to "1" meaning one deliverable bundle per row. This neutralizes the column without removing it, which would require more invasive template modification.
- **Levers for negotiation are deliverables, not headcount.** This mirrors the Cisco pricing structure Colin described in Set 06 ("if you want it to cost less, have less deliverables. It's that easy. But there's no lever to say we're gonna do this at a lower cost because we're going to do it with three people instead of four"). If Lam procurement pushes back on price, the only move is to reduce the deliverable count, which is a scope conversation BayOne can win.
- **No exposure of internal margin or cost structure.** The internal pricing (Set 06 and 08a) shows a loaded cost of roughly $10,808 and a 27.9% loaded margin at $15K. None of that math or structure is visible to Lam. They see only the output number.
- **Matches what Lam has already seen.** The Engagement Pricing one-pager shows a Milestone Payments table with $6,000 + $9,000 = $15,000. The SOW Fee Schedule is the contract expression of what Lam already reviewed and accepted in the one-pager. There is nothing to re-negotiate.

### Why this is defensible

- The template language on page 2 explicitly says "Total Amount (Not to Exceed)" as the reporting framing. Fixed-fee, NTE-capped engagements fit this framing cleanly.
- The MSA Section 4 (payment terms) will govern invoicing regardless of how the Fee Schedule is structured. Nothing in the restructured table conflicts with the MSA.
- Omitting hourly rate columns is not unusual for fixed-fee work. Procurement software and approval workflows handle both T&M and fixed-fee SOWs; the template's column structure is a convention, not a requirement.

### Alternative considered and rejected: keep T&M structure with blended hourly rate

- The template's structure preserved as Role / Quantity / Hours / Rate / Total, with e.g. "Engagement Team / 1 / 120 / $125/hr / $15,000."
- Rejected explicitly. Any hourly rate on a signed SOW becomes the anchor for follow-on work. A $125/hr blended rate on this POC would make a $500K full-scope engagement ($500K / $125 = 4,000 hours at one resource) appear to demand a lot of hours. Lam procurement would compare ratios. This is exactly the Cisco headcount trap Colin described in Set 06.

### Alternative considered and rejected: lump-sum single row with no phase split

- One row: "Proof of Concept Engagement / 1 / $15,000."
- Rejected. Removing the phase split removes the natural milestone for invoicing. Lam invoices BayOne against milestones per the engagement pricing one-pager (40% / 60%). Collapsing to one row forces either (a) invoice on completion only, which is a 3-week AR exposure for BayOne, or (b) invoice on a calendar schedule, which conflicts with the deliverable-based model. The two-row phase split is the right balance between SOW simplicity and commercial flexibility.

### Alternative considered and rejected: expose the percentage weights (40% / 60%) on the SOW

- Rejected. The milestone percentages appear on the Engagement Pricing one-pager, which is fine as a supplementary document. On the SOW itself, percentages invite a procurement question ("why 40/60 and not 50/50? what's the basis?") that dollar amounts do not. Dollar amounts are a commercial fact; percentages are a structure that demands justification.

---

## SOW Term (page 2 field)

The template shows "The period of performance of the Services shall commence on Feb 1, 2026 and end on Mar 31, 2026 ("SOW Term")." These dates are stale carryover from the prior engagement.

### Recommended content

> The period of performance of the Services shall commence on the date BayOne receives all required access (including Lam Research environment access, Escalation Solver data access, reference materials, and subject matter expert availability) and shall conclude three weeks thereafter, unless extended by mutual written agreement of the parties ("SOW Term").

### Why this is favorable

- **The three-week clock is tied to access, not calendar.** This is the single most important risk management decision in the engagement. Colin flagged in Set 06 the Cisco precedent: "Cisco signed a SOW. It took three entire calendar months to get the access to things." The session handoff flags the Orion team (Lam-side, controlling data access, on the critical COS project) as the primary execution risk. Anchoring the clock to a fixed calendar date would put BayOne on the hook for a three-week delivery from a date that Lam's internal dependencies may not support.
- **Mirrors the proposal and pricing language exactly.** The Engagement Pricing one-pager (Option A row) says "From the date BayOne has environment access, data access, and reference materials." The proposal's Assumptions section says "The three-week timeline begins from the date this access is provided." The SOW Term clause is a verbatim expression of those commitments.
- **Keeps the fee protected.** If the start date slips due to Orion dependencies or SME unavailability, the fee does not change and the delivery date rolls forward accordingly. Without this clause, a delayed start could create an awkward conversation about whether BayOne is past deadline.
- **"Unless extended by mutual written agreement" provides a clean extension mechanism.** If the engagement legitimately overruns (e.g., data quality issues surface in discovery that warrant a Phase 1 extension), the parties can extend in writing. No re-signing of the SOW required.

### Why this is defensible

- The proposal (sent April 10) and the engagement pricing one-pager both tie the three-week clock to access. Lam has not pushed back on this framing in over a week. Mikhail's April 16 email explicitly acknowledges the access-coordination requirement by asking what technologies Colin needs.
- Access-contingent start dates are standard for POC engagements at large enterprises where vendor access is non-trivial to provision. Procurement reviewers see this regularly.

### Alternative considered: dated range with explicit "subject to data access" clause

- Example formulation: "Commence on May 1, 2026 and conclude on May 22, 2026, subject to BayOne's receipt of required access as described in Section 1 and the POC Proposal dated April 2026. If such access is not provided by May 1, 2026, the SOW Term shifts by an equivalent number of business days."
- This is defensible and has the advantage of giving procurement a concrete date to reference in their tracking systems. However, it adds complexity and creates a second date-shift trigger (the slip provision) that could be the subject of interpretation disputes. The open-ended access-triggered formulation is cleaner.
- **Use this alternative if Lam procurement pushes back on the open-ended form.** It is a reasonable fallback that preserves the protection.

### Alternative considered and rejected: fixed calendar dates without access clause

- Example: "Commence on May 1, 2026 and end on May 22, 2026."
- Rejected. This is the Cisco mistake. Any delay in access provisioning becomes a BayOne breach problem rather than a Lam coordination problem.

### Reference: assumptions already protect us

- The POC Proposal's Assumptions section (items 1, 5, and 7) already establishes that the timeline is access-dependent, SME availability is required, and delays beyond BayOne's control extend the timeline. The SOW Term clause is the contractual expression of those assumptions.

---

## Total Amount (Not to Exceed) on Page 2

### Recommended content

> **$15,000.00**

### Why

- Matches the Engagement Pricing one-pager ($15,000).
- Matches the Fee Schedule Total row.
- Matches the POC Proposal investment section (revised in Set 08a from the original $10,000 to $15,000).
- Internally consistent across all documents Lam has seen.

### Alternative considered and rejected: round up or pad

- The internal pricing analysis (Set 08a) shows $15K at 27.9% loaded margin, slightly below the 30% internal floor. Padding to $17,500 would raise the margin to 38.2% loaded. Rejected: the $15K price is what Lam has seen, and Brad's scar tissue from prior vendors makes any upward adjustment at SOW stage a credibility risk. The right move is to honor the $15K commitment, accept the 27.9% margin (which is 39% if no risk reserve is consumed), and capture upside through follow-on engagement pricing.

---

## Invoice Schedule (Page 2)

The template shows "Invoice schedule: Monthly."

### Recommended content

> Invoice schedule: Per milestone completion, in accordance with Section 4 of the Agreement.

### Why this is favorable

- **Matches the deliverable-based commercial model.** Monthly invoicing is a T&M convention. A fixed-fee engagement with two phases should invoice against milestone completion.
- **Aligns with the 40% / 60% milestone structure Lam has already seen.** The Engagement Pricing one-pager's Milestone Payments table defines exactly when each invoice is triggered: Phase 1 completion ($6,000) and Phase 2 completion ($9,000).
- **Shortens AR cycle.** Under monthly invoicing, a three-week engagement would invoice twice (crossing a month boundary) or once (within one month), with the MSA's 30-day payment terms compounding the delay. Milestone invoicing allows the first invoice to go out the moment Phase 1 is accepted, which could be as early as week 1 of the engagement.

### Why this is defensible

- The template explicitly refers to MSA Section 4 ("Payment terms shall be subject to Section 4 of the MSA"), which governs invoice cadence. Changing "Monthly" to "Per milestone completion" is a customization of when invoices are issued, not a modification of when they are paid. The MSA's 30-day payment terms apply to either structure.
- Milestone-based invoicing is standard for fixed-fee POCs.

### Alternative considered and rejected: keep "Monthly"

- Rejected. Monthly invoicing is the default for the template but doesn't match the commercial model Lam accepted in the Engagement Pricing one-pager. Leaving it as Monthly creates document inconsistency: the one-pager shows Milestone Payments at 40% / 60%, while the SOW shows Monthly invoicing. When Lam AP tries to process the first invoice, they will look to the SOW for cadence, not the one-pager.

### Alternative considered and rejected: invoice on completion only

- Rejected. Three weeks of AR exposure for $15,000 is not a lot of capital, but it sets a precedent for follow-on engagements that would be material. Better to establish the milestone-based pattern now.

---

## Section 4: Expenses

The template's standard expense language is well-drafted and client-favorable (no reimbursement without prior written approval, reasonable expenses only, compliance with Lam's travel policy).

### Recommended content

**Keep template default language verbatim.** No modifications.

### Why this is favorable (enough)

- **We are not anticipating reimbursable expenses.** The internal pricing (Set 08a) includes $2,500 in travel as a line item in BayOne's loaded cost, but that is internal cost that gets absorbed into the $15,000 fixed fee, not a pass-through expense billed to Lam. The POC is remote or hybrid; Colin may travel once or twice to Pleasanton or to the Lam site, but those costs are BayOne's to absorb as a business-development investment.
- **Zero-expense POC simplifies everything.** No travel approvals, no expense report submission against Lam's intranet policy, no 30-day post-completion expense tail. The entire engagement is one fee, two invoices.
- **The "absent prior written approval" language protects both sides.** If a legitimate expense does arise (e.g., Lam requests Colin travel to a specific fab for a specific meeting), the language provides the mechanism for Lam to approve it in writing and for BayOne to invoice it with the appropriate documentation.

### Why this is defensible

- Template default. Procurement will not review this section with any scrutiny because it is standard.

### Alternative considered and rejected: add a specific expense carve-out for Colin travel

- Rejected. Adding any named expense category invites procurement scrutiny and creates paperwork for small amounts. Better to absorb modest travel into the fixed fee and invoke the prior-written-approval clause only if something unusual arises.

---

## Section 5: Equipment

The template offers a structure where Contractor supplies own equipment except for items loaned by Company (with Equipment Type and Serial No. blanks to fill).

### Recommended content

**Leave Equipment Type and Serial No. fields blank at SOW signing, with the language modified as follows:**

> Contractor will supply all its own equipment for this SOW, except for any equipment, virtual machine access, or credentialing that Company provisions to Contractor in support of Option A (Lam Research environment execution) as described in the POC Proposal and Engagement Pricing documents. Specific equipment, VM specifications, and access credentials will be documented through Lam Research IT provisioning and do not require amendment of this SOW.

### Why this is favorable

- **Anticipates Option A (Lam environment) without locking specifics.** Mikhail's April 16 email confirms Option A and asks Colin what technologies he needs. The specific technology stack (Azure VM? Windows workstation? SSH jump box? specific IDE licenses?) is a conversation with Daniel over the next days. Locking a specific "Equipment Type: Dell Latitude 5540 / Serial No. XXXX" into the SOW before that conversation forces a premature commitment.
- **Leaves the door open without requiring SOW amendment.** The modified language explicitly says specific items are documented through Lam IT provisioning, not the SOW. This means if Lam provisions a VM on April 28 and updates the credentials on May 5, neither event triggers an SOW amendment.
- **Preserves the standard return-in-good-condition clause.** The template's second paragraph ("No license or other right is hereby granted... Contractor agrees to return the equipment...") is kept unchanged. This protects Lam's equipment interest and is standard.

### Why this is defensible

- The language aligns with the proposal's Option A assumption ("BayOne requires environment access (VM or equivalent) and access to Escalation Solver data and reference materials before the three-week timeline begins").
- Deferring specific equipment specification to IT provisioning is standard for IT-provisioned engagements at large enterprises.

### Alternative considered: leave Equipment Type and Serial No. blanks blank with standard template language unchanged

- This is simpler and is what the template literally offers. It is defensible as-is because the second paragraph ("Contractor will supply all its own equipment... except for the following equipment which will be loaned...") naturally accommodates either scenario: if nothing is loaned, no blanks are filled; if something is loaned, Lam IT fills the blanks at provisioning time.
- **This alternative is acceptable if Colin prefers minimal template modification.** The recommended approach is slightly more explicit about the Option A scenario, but the template default is not wrong here.

### Alternative considered and rejected: mark Section 5 "Not Applicable" or "N/A"

- Rejected. Option A requires Lam-provisioned access. Marking Equipment as N/A contradicts that. Also creates a paperwork ambiguity if Lam later loans a physical item (a token, a workstation for on-site work).

### Alternative considered and rejected: specify the equipment now

- Example: "Equipment Type: Azure VM (Windows Server 2022, 4 vCPU, 16GB RAM) / Serial No.: Lam Research Azure Subscription ID XXXX."
- Rejected. Premature specification. Mikhail's email is asking what we need, which means nothing has been provisioned yet. Any specific equipment statement in the SOW today is a guess.

---

## Section 6: Background Technology Disclosure

**This is the most IP-protective section of the entire SOW for BayOne.** The template's default is "☒ None / ☐ See immediately below:" which would forfeit BayOne's Background Technology protections under the MSA.

The MSA's typical IP regime (standard across consulting MSAs): work product created specifically for the client under the SOW is owned by the client. Background Technology — meaning pre-existing IP that BayOne brings into the engagement — remains BayOne's, but only if it is disclosed on the SOW. **Disclosure on the SOW is the only mechanism that prevents Lam from later claiming ownership over methodology and tooling BayOne developed before the engagement and uses again after it.**

### Recommended content

Uncheck "None." Check "See immediately below:" Then fill in the disclosure:

> The following is a list of Background Technology that BayOne Solutions brings into this engagement and that remains BayOne's intellectual property:
>
> 1. **Layered detection methodology framework.** BayOne's approach of sequencing deterministic pattern matching, machine learning and natural language processing, and generative AI methods in a hierarchical filter to improve cumulative detection accuracy at lower computational cost than parallel approaches. This methodology was developed by BayOne prior to this engagement.
>
> 2. **Exploratory data analysis framework for entity-detection problems.** BayOne's structured approach to assessing data separability between entity classes, evaluating distribution and volume across target fields, determining sample sufficiency, and establishing maximum achievable accuracy bounded by reference data quality. This framework was developed by BayOne prior to this engagement.
>
> 3. **Evaluation protocol templates and accuracy ceiling determination methodology.** BayOne's templates and procedures for defining repeatable, measurable evaluation protocols for entity-detection engagements, including the methodology for determining the maximum achievable accuracy given a defined reference data set. These templates were developed by BayOne prior to this engagement.
>
> 4. **Reusable pipeline components and script templates.** BayOne's library of script templates, pipeline configurations, and wrapper components used across entity-detection and confidentiality-detection engagements, including integration patterns for open-source NLP libraries (see Section 7). These components were developed by BayOne prior to this engagement.
>
> 5. **BayOne consulting methodology artifacts.** BayOne's engagement management, deliverable structures, and presentation templates (including but not limited to discovery assessment formats, methodology documentation formats, and scaling-path documentation formats). These artifacts were developed by BayOne prior to this engagement.

### Why this is favorable

- **Protects the methodology from claim by Lam.** If BayOne does not disclose the layered detection methodology as Background Technology, Lam could argue (years from now, in a licensing dispute or in a situation where BayOne uses the same methodology for a competitor) that the methodology was developed "under the SOW" and is therefore Lam's. Disclosure preempts that argument.
- **Specifically contrasts with Lam's prior approach.** The engagement's entire differentiator is the layered approach versus Mikhail's prior parallel-NER-model approach. Claiming the layered approach as BayOne Background Technology is what makes this an IP-protected engagement rather than generic consulting work.
- **Protects the EDA framework.** The EDA framework and accuracy-ceiling methodology are core differentiators. Without disclosure, Lam could argue these are "work product" (because they are applied during the engagement) rather than pre-existing tooling.
- **Protects script templates and pipeline components.** Even if Colin's actual implementation is "a generic Python script" (Set 06, Colin's internal framing), the templates and patterns BayOne applies are pre-existing and reusable. Disclosure keeps them reusable.
- **Protects consulting artifacts.** Discovery formats, methodology documentation formats, scaling-path documentation formats are BayOne's engagement IP. Without disclosure, a client could argue that the specific format adopted for this engagement is their property.

### Why this is defensible

- The MSA (standard consulting MSA boilerplate) almost certainly contains a Background Technology carve-out that requires disclosure. Reading the MSA would confirm the exact mechanism, but the disclosure-or-forfeit structure is near-universal.
- The recommended disclosure is at medium specificity — enough to identify the IP without giving Lam a detailed technical blueprint. This is the right altitude for a procurement-reviewed document.
- Disclosure here is not the same as "sharing the code." BayOne discloses the existence and nature of Background Technology, not the source code or detailed implementation.

### Why the medium-specificity level

There is a trade-off in how specific the disclosure should be:

- **Too vague** ("BayOne's proprietary methodology and tooling") fails the disclosure-or-forfeit test. A future dispute might argue that the disclosure was too generic to actually identify the Background Technology, and therefore failed.
- **Too detailed** (full architecture diagrams, specific library names for the pipeline, specific prompt templates) tips Lam off to exactly what the IP is worth and invites scrutiny of whether the disclosure covers the actual work product. Also creates a roadmap for a technical reader to understand BayOne's IP without engaging BayOne.
- **Medium specificity** — name the capability, state that it pre-existed the engagement, decline to specify the implementation — is the right altitude. The recommended disclosures above hit this altitude.

### Alternative considered and rejected: check "None" (the template default)

- Rejected explicitly. This is the critical IP trap. Marking None on the SOW is equivalent to agreeing that BayOne has no pre-existing IP being brought into the engagement. This is both factually wrong and legally catastrophic for follow-on revenue from the same methodology.

### Alternative considered and rejected: check "See immediately below" with just "BayOne's proprietary detection methodology and consulting artifacts"

- Rejected as too vague. A single-sentence disclosure does not itemize the specific capabilities and may not survive a specificity challenge.

### Alternative considered and rejected: full technical specification of each item

- Rejected as too detailed. For example, explicitly naming "our fine-tuned transformer model trained on N tokens of semiconductor-domain text" would be both more than procurement needs and more information about BayOne's internal capabilities than Lam needs. Medium specificity is the target.

---

## Section 7: Third-Party Technology Disclosure

The template default is "☒ None / ☐ See immediately below." Default is wrong here for the same structural reason as Section 6, but the analysis differs.

### Recommended content

Uncheck "None." Check "See immediately below:" Then fill in:

> The following is a list of Third-Party Technology that may be used in the performance of this SOW:
>
> 1. **SpaCy** — open-source natural language processing library. Licensed under MIT License.
> 2. **Microsoft Presidio** — open-source personally identifiable information detection framework. Licensed under MIT License.
> 3. **Open-source Python libraries and supporting tooling** — including but not limited to standard NLP, data processing, and evaluation libraries used in implementation. Each is used under its respective open-source license.
> 4. **Microsoft Azure AI services** (if accessed within the Lam Research environment under Option A execution) — used under Lam Research's existing Azure subscription and license terms. No additional licensing obligation is created under this SOW.
> 5. **Cloud-hosted AI models and API services** as required for the generative AI layer of the detection methodology, used under each provider's standard terms of service.

### Why this is favorable

- **Prevents Lam from later claiming that BayOne represented open-source tools as proprietary.** If the Phase 2 deliverable shows detection outputs from SpaCy or Presidio, disclosure on the SOW confirms these are third-party tools, not BayOne's IP.
- **Lam already knows these tools.** Mikhail explicitly named Presidio in Set 05 as a tool used in the prior effort. SpaCy ("Spacey" in the speech-to-text) was also discussed. This disclosure does not reveal anything competitively sensitive.
- **Protects against license cross-contamination claims.** If Lam's procurement or legal team later asks "did you use any open-source software with GPL or AGPL licensing that could taint our codebase?" the disclosure explicitly names the permissively-licensed tools used.
- **The Azure services clause protects the Option A execution mode.** If Colin uses Azure OpenAI or Azure AI Language within Lam's tenant, those services are under Lam's license, not BayOne's responsibility to procure. The disclosure makes this explicit.

### Why this is defensible

- Every item listed is either already disclosed in Mikhail's prior conversations, is an obvious open-source choice for this problem space, or is a service provisioned through Lam's own account. Nothing is sensitive or contestable.
- Medium specificity again: named tools, standard licenses, no technical implementation details.

### Alternative considered and rejected: check "None"

- Rejected. If any third-party tool appears in the deliverables, a "None" disclosure was false. This is a quiet but real liability. Disclose and be done with it.

### Alternative considered and rejected: list every possible library by version

- Rejected. Over-specification is unnecessary and creates amendment burden if a library version changes mid-engagement.

---

## Section 8: Approved Subcontractors

### Recommended content

**Decision needed from Colin.** See "Open Decisions for User" section at end of document.

If subcontractor is used:

> **Subcontractor:** [Firm Name — one of Pratik Sharda's, Amit Grover's, or Anuj Sehgal's partner organizations that supplies the India-based AI/ML engineer]
>
> **Statement of Services to be delegated to Subcontractor:**
> Detection methodology implementation, data analysis execution, and pipeline development under BayOne Solutions' supervision and direction. All deliverables to Lam Research are issued under BayOne Solutions' name and responsibility.

If no subcontractor is used (India resource is a direct BayOne employee):

> **Subcontractor:** None.

### Why this is favorable

- **If a subcontractor firm is used, it must be disclosed and approved.** The MSA almost certainly makes unapproved subcontracting a breach. The internal pricing (Set 08a) assumes an "India Resource (Mid-Level)" at $45/hr loaded cost for 120 hours. Whether that resource is a BayOne employee or a subcontractor is a question Colin must confirm with Anuj and Amit. The BayOne partner structure (Pratik, Amit, Anuj operate through affiliated entities) suggests the India resource may flow through one of those entities.
- **The supervision clause protects BayOne's deliverable responsibility.** The Statement of Services explicitly states deliverables are BayOne's responsibility, and the subcontractor works under BayOne's supervision. This preserves the single-throat-to-choke model Lam expects.
- **Naming the scope of subcontracted services limits it.** If the delegated scope is narrow ("methodology implementation under supervision"), Lam cannot later claim that BayOne's consulting role was substantially subcontracted.

### Why this is defensible

- The template explicitly requires this disclosure. Failing to disclose a subcontractor when one is used is a material breach risk.
- Subcontracting to offshore resources is industry-standard. Lam has prior BayOne-managed offshore engagements (Philippines team on knowledge management per Daniel's background in the org chart).

### Why this is a decision Colin must make

Two scenarios and the user needs to confirm which applies:

1. **The India resource is a direct BayOne employee.** Mark "None" for subcontractor. No disclosure required.
2. **The India resource is supplied through a BayOne partner firm (Pratik, Amit, or Anuj's affiliated entity).** Mark the partner firm as subcontractor. Disclosure required.

The org chart and the internal pricing document do not resolve this definitively. Set 06 references "Colin's team" and "our partners" somewhat interchangeably. This is a question for Colin, Anuj, and Amit.

### Alternative considered and rejected: mark "None" without confirming

- Rejected explicitly. If the India resource is actually a subcontractor and BayOne marks None, this is a misrepresentation that could surface during any Lam audit of the engagement. Low probability, but not zero, and the cost of getting it wrong is disproportionate.

### Alternative considered and rejected: mark a named subcontractor without confirming

- Rejected. Naming a partner firm on the SOW creates contractual privity implications between that firm and Lam. This must not happen without the partner firm's awareness and consent.

---

## Signature Block

### Recommended content

**Lam Research Corporation column:**

Leave all four fields (By / Name / Title / Date) blank for Lam procurement to complete. Do not pre-populate. The signing party for Lam is typically a procurement or legal officer, not the technical sponsor. Brad Estes, Mikhail Krivenko, and Daniel Harrison are unlikely to be the Lam-side signer on an MSA-governed SOW at a company the size of Lam Research.

**BayOne Solutions Inc. column:**

**Decision needed from Colin.** See "Open Decisions for User" section. The natural candidates are:

1. **Sripriya (CTO, Colin's direct report chain per skill_notes and org chart).** Given Sripriya is Colin's boss and the CTO, she is the likely authorized signer for technical-scope SOWs under $X threshold.
2. **Anuj Sehgal (VP of Sales).** As the commercial owner of the deal, Anuj may be the BayOne convention for sales-originated SOWs.
3. **Another BayOne officer per internal signature authority matrix.**

This depends on BayOne's internal signing authority matrix, which is not captured in the engagement documents. Colin should confirm with Sripriya or the BayOne back-office.

### Why

- Leaving the Lam column blank is correct. Do not attempt to pre-populate Brad/Mikhail/Daniel because they are not the signers.
- Determining the BayOne signer is a procedural question BayOne handles internally, not a strategic positioning question.

### Alternative considered and rejected: pre-populate Brad Estes as Lam signer

- Rejected. Brad is the technical sponsor and decision-maker but almost certainly not the authorized SOW signer at Lam's size. Pre-populating him would be presumptuous and would be corrected by Lam procurement anyway.

### Alternative considered and rejected: pre-populate Colin as BayOne signer

- Rejected unless Colin is in fact the authorized signer. Colin is the Director of AI and technical lead. Sripriya as CTO is the more likely signer for a CTO-reporting engagement.

---

## Open Decisions for User

The following decisions cannot be made from the research library alone and require Colin's input before the SOW is drafted:

### 1. Effective Date

**Question:** Do you want 2026-04-24 (a specific forward date) or leave blank for whichever party signs last to date the document?

**Recommendation:** 2026-04-24. Provides a concrete anchor for future reference without back-dating.

**Impact of getting it wrong:** Minor. The Effective Date is symbolic; the SOW Term clause (access-triggered) governs operational dates.

### 2. Subcontractor Disclosure

**Question:** Is the India-based AI/ML engineer a BayOne employee or a subcontractor flowing through a partner firm (one of Pratik's, Amit's, or Anuj's entities)?

**Recommendation:** Confirm with Anuj and Amit before SOW finalization. The internal pricing document's "India Resource (Mid-Level) at $45/hr" framing suggests subcontractor, but is not definitive.

**Impact of getting it wrong:** Material. Unapproved subcontracting is typically an MSA breach. Must be resolved before signing.

### 3. Background Technology Specificity Level

**Question:** The recommended disclosure lists five items at medium specificity. Do you want to (a) accept the recommendation, (b) compress to fewer items, or (c) expand with additional items (e.g., specific detection models, specific prompt templates)?

**Recommendation:** Accept the five-item medium-specificity disclosure. It protects the methodology IP without exposing implementation details.

**Impact of getting it wrong:** Too vague risks failing the disclosure-or-forfeit test. Too specific tips off Lam to IP value. Medium specificity is the target.

### 4. Equipment Section Approach

**Question:** Do you want (a) the recommended Option A-anticipating language (leaves specific items to Lam IT provisioning), (b) the template default unchanged (with blanks left empty), or (c) specific equipment named now?

**Recommendation:** (a) Option A-anticipating language. Flexible, anticipates Mikhail's provisioning without locking specifics.

**Impact of getting it wrong:** Minor. The template default (b) is also acceptable.

### 5. Authorized BayOne Signatory

**Question:** Who is the authorized BayOne signer for a $15,000 SOW under MSA BAYON-MAS-0013142?

**Recommendation:** Confirm with Sripriya (CTO) or the BayOne back-office. Likely Sripriya; possibly Anuj as commercial owner.

**Impact of getting it wrong:** Procedural. Wrong signer means SOW has to be re-signed. Catch before sending to Lam.

### 6. Invoice Schedule Language

**Question:** The recommendation replaces "Monthly" with "Per milestone completion." Confirm this aligns with BayOne AR preferences and Lam's typical procurement expectations.

**Recommendation:** Per milestone completion, matching the 40/60 structure Lam has already seen in the Engagement Pricing one-pager.

**Impact of getting it wrong:** AR cycle misalignment. If BayOne AR expects monthly invoicing regardless of deliverable cadence, need to surface that conflict.

---

## Summary of Section-by-Section Recommendations

| Section | Template Default | Recommended Content |
| :--- | :--- | :--- |
| Effective Date | Feb 1, 2026 (stale) | 2026-04-24 (or countersignature date) |
| Services | GCS Data Lake filler | POC-specific deliverable-bounded language, incorporating proposal by reference |
| Acceptance Criteria | Three options offered | MSA Section 3 default |
| Fee Schedule | T&M with hourly rates | Two-row fixed-fee table: Phase 1 $6K + Phase 2 $9K = $15K NTE |
| SOW Term | Feb 1 - Mar 31, 2026 (stale) | Three weeks from access provisioning, access-triggered |
| Total Amount (NTE) | $11,840 | $15,000 |
| Invoice Schedule | Monthly | Per milestone completion |
| Section 4 Expenses | Template standard | Keep verbatim |
| Section 5 Equipment | Blanks for loaned items | Option A-anticipating language, specifics deferred to IT provisioning |
| Section 6 Background Technology | None | See immediately below (five-item medium-specificity disclosure) |
| Section 7 Third-Party Technology | None | See immediately below (named open-source and Azure services) |
| Section 8 Subcontractors | Blanks | Decision needed — confirm India resource status |
| Signature Block | Blanks | Leave Lam column blank; BayOne signer decision needed |

---

## Next Steps for the Drafter

The drafter of the actual SOW deliverable should:

1. Take this document as the section-by-section playbook.
2. Resolve the six Open Decisions with Colin before starting the draft.
3. Produce the filled SOW as both a markdown document (for version control) and as a formatted document suitable for countersignature (PDF or Word, following BayOne letterhead format).
4. Route the draft through Colin for technical review, then through Sripriya (or designated signer) for signature authority review, before issuing to Lam.
5. Flag to Colin any place where the MSA's actual Section 3 (Acceptance) or Section 4 (Payment) language conflicts with the recommended SOW language. The recommendations in this document are based on standard MSA boilerplate; the actual MSA should be read before final SOW drafting.
