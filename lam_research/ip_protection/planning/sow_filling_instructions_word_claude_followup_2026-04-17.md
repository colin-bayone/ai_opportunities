# SOW Filling Instructions — Follow-Up: Inline All Referenced Content

**Engagement:** Lam Research IP Protection — Confidential Information Detection POC
**Status:** Follow-up to `sow_filling_instructions_word_claude_2026-04-17.md`. The prior spec has already been executed by the Word Claude session. This document instructs only the additional changes from this turn. Do not re-do prior work.
**Spec author:** Singularity skill session, 2026-04-17

---

## Why This Change

The prior spec's Section 1 ended with this sentence:

> The full scope, assumptions, exclusions, risk factors, and success criteria are as described in the Confidential Information Detection POC Proposal (April 2026) and the Engagement Pricing one-pager (April 2026), which are incorporated by reference into this SOW. In the event of any conflict between those documents and this SOW, this SOW controls.

Reason for change: incorporating external documents by reference forces Lam Legal to request, review, and reconcile those external documents alongside the SOW. This creates churn and delay. The fix is to inline all the referenced content directly into Section 1 so the SOW is fully self-contained. Lam Legal then reviews one document, not three.

---

## What To Do

In Section 1 (Services to be Provided), make two changes:

1. **DELETE** the "incorporated by reference" sentence (the verbatim text quoted above).
2. **ADD** the inline content below as new subsections within Section 1, placed AFTER the existing Phase 1 / Phase 2 deliverables paragraphs and BEFORE the existing "SOW-specific assumptions" subsection (which the prior spec already added).

Use bold subsection headers (e.g., **Success Criteria**, **Engagement Scope**, etc.) to organize the new content within Section 1. Match the formatting and indentation of the existing Section 1 content.

---

## Inline Content To Add

Add the following subsections to Section 1, in this order, immediately after the Phase 2 deliverables paragraph and before the "SOW-specific assumptions" subsection:

### Subsection: Success Criteria

Header: **Success Criteria**

This proof-of-concept will be considered successful if:

1. A baseline data assessment is completed, including data quality evaluation and determination of maximum achievable detection accuracy.
2. The detection approach is demonstrated against real Escalation Solver data for two entity types (customer name and fab identifier) across five free-text fields.
3. Detection performance is measured and reported using a defined evaluation protocol that can be repeated and built upon in subsequent phases.
4. The detection methodology is documented, showing how each layer of the approach contributes to accuracy improvement.
5. A clear path is documented for how the approach scales from proof-of-concept to a broader engagement.

---

### Subsection: Engagement Scope

Header: **Engagement Scope**

| Area | Detail |
| :--- | :--- |
| Application | Escalation Solver (five free-text fields, approximately 4,000 to 5,000 characters each). |
| Entity Types | Customer name and fab identifier. |
| Methodology | Layered detection approach: deterministic pattern matching, machine learning and natural language processing, and generative AI for contextual edge cases, applied sequentially. |
| Benchmarking | Detection performance measured against prior effort baseline as documented by Lam Research, using a defined, repeatable evaluation protocol. |

---

### Subsection: Detailed Approach

Header: **Detailed Approach**

The engagement is structured in two phases: a discovery phase to assess the data landscape and establish what is achievable, followed by a build phase to demonstrate the detection methodology against real data.

**Phase 1: Discovery and Data Assessment.** Approximately one week from data access. Contractor will conduct a systematic assessment of the available data, reference materials, and labeled examples to understand the detection landscape before any model development begins. Activities include:

- Data Quality Assessment: evaluation of the existing reference data (customer name lists, fab/location identifier lists, exclusion lists, and previously labeled examples) for completeness, consistency, and reliability. If contradictions exist within the reference data, for instance, content flagged as confidential in one context but present in approved documents elsewhere, Contractor will document these findings and their impact on achievable accuracy.
- Exploratory Data Analysis (EDA): statistical analysis to assess data separability between entity classes, evaluate the distribution and volume of content across the target fields, and determine the sample sufficiency of existing labeled data. The EDA produces a definitive assessment of what detection accuracy is achievable given the current data, rather than an estimate based on assumptions.
- Discovery Activities: identification of authoritative sources for detection criteria, mapping of the data access and validation workflow, and documentation of the specific detection targets and their variations. These findings carry forward as lasting artifacts that do not need to be repeated in a subsequent engagement.

**Phase 2: Detection Build and Benchmarking.** Approximately two weeks following Phase 1. Contractor will build and demonstrate the detection approach using a layered methodology. Rather than running multiple models in parallel and reconciling their outputs, this approach processes data through sequential layers of increasing capability:

1. A deterministic layer handles known patterns with high confidence and low computational cost.
2. A machine learning and natural language processing layer addresses nuanced cases that deterministic matching cannot reach.
3. Where required, a generative AI layer provides contextual judgment on ambiguous cases.

Each layer reduces the problem space for the next, resulting in higher cumulative accuracy and lower computational cost than any single approach operating independently. Contractor will benchmark detection results against the prior effort baseline as documented by Lam Research, using a defined, repeatable evaluation protocol. The methodology documentation will explain how each layer contributes to accuracy improvement and how the approach would extend to additional entity types, fields, and applications.

---

### Subsection: Timeline

Header: **Timeline**

Total Duration: three weeks from the date all required access is in place.

| Week | Phase | Activities |
| :--- | :--- | :--- |
| 1 | Discovery and Data Assessment | Data quality evaluation, exploratory data analysis, baseline accuracy determination, detection target mapping. |
| 2-3 | Detection Build and Benchmarking | Layered detection implementation, accuracy measurement, methodology documentation, scaling path documentation. |

The timeline begins upon receipt of the required data, reference materials, equipment, environment access, and Lam Research subject matter expert availability. Some Phase 1 activities (initial consultation on detection targets and criteria) can proceed in parallel with data provisioning where practical.

---

### Subsection: Deliverables

Header: **Deliverables**

Contractor will deliver the following items during the engagement:

1. Exploratory data analysis report including baseline data quality assessment, maximum achievable accuracy determination, and documentation of detection targets.
2. Working detection demonstration against real Escalation Solver data for customer name and fab identifier across the five in-scope free-text fields.
3. Detection performance benchmarked against prior effort baseline as documented by Lam Research.
4. Defined, repeatable evaluation protocol that carries forward to subsequent phases.
5. Documented layered detection methodology showing the contribution of each approach layer.
6. Scaling path documenting how the approach extends to additional entity types, fields, and applications in subsequent engagements.
7. Recommendations for reference data refinement where applicable.

---

### Subsection: Execution Options

Header: **Execution Options**

Lam Research has confirmed Option A (Lam Research environment) as the elected execution mode. Both options are documented below for completeness.

| Element | Option A: Lam Research Environment (elected) | Option B: BayOne Environment |
| :--- | :--- | :--- |
| Execution Environment | Lam Research infrastructure. | BayOne Solutions infrastructure. |
| Data Handling | Data remains within Lam Research systems at all times. | Data provided to Contractor under the existing confidentiality agreement. |
| Access Requirements | Contractor requires environment access (such as a virtual machine or equivalent) and access to Escalation Solver data and reference materials. | Lam Research provides data export and reference materials to Contractor. |
| Timeline Start | From the date Contractor has environment access, data access, equipment, and reference materials. | From the date Contractor receives the data export and reference materials. |
| Project Leadership | Director of AI, BayOne Solutions. | Director of AI, BayOne Solutions. |

The three-week period of performance begins from the date all required access and materials are in place, regardless of which option is in effect.

---

### Subsection: Assumptions

Header: **Assumptions**

This SOW is based on the following assumptions:

1. Lam Research provides Contractor with access to Escalation Solver data, reference lists (customer names, fab/location identifiers, exclusion lists), and any previously labeled examples that informed the prior detection effort. The three-week period of performance begins from the date all required access is provided.
2. Lam Research designates one or more subject matter experts available during the POC period to define detection targets, validate detection results, and confirm what constitutes a true positive.
3. The detection scope is five free-text fields and two entity types (customer name and fab identifier). Requests beyond this scope are documented as candidates for a subsequent engagement and may be subject to a formal change request process with adjusted pricing.
4. Contractor will assess the baseline accuracy of the existing reference data during the discovery phase. If the data contains contradictions or quality issues, the maximum achievable accuracy is bounded by the data quality. Contractor will report on findings and recommend refinements, but resolving data quality issues at scale is not within the POC scope.
5. Data volume and scope are agreed during the discovery phase. The POC is designed for a representative data set. Processing at enterprise scale (hundreds of thousands of records) would require scope and timeline adjustment.
6. The execution environment (Lam Research infrastructure or BayOne infrastructure) is agreed upon before the engagement begins, as described in the Execution Options subsection. Lam Research has elected Option A (Lam Research environment).
7. Lam Research manages internal coordination required to provide data, equipment, and environment access within a reasonable timeframe. Contractor cannot control internal team availability or scheduling.
8. Lam Research provides timely feedback and validation during the POC period. Once the engagement is underway, if cumulative project delays beyond Contractor's control exceed 50% of the remaining engagement duration, both parties will formally review engagement terms through a change request process.
9. Contractor handles all Lam Research data in accordance with confidentiality requirements. Customer names are redacted from all Contractor-produced documents.
10. Lam Research provides documentation of prior detection effort results and target performance aims to serve as a benchmark for the engagement.
11. This engagement does not include production integration into Escalation Solver or any other application.

---

### Subsection: Exclusions

Header: **Exclusions**

The following items are explicitly excluded from this SOW:

1. Additional entity types beyond customer name and fab identifier. Contractor will document a scaling path for additional entity types, but this POC is bounded to two.
2. Additional applications beyond Escalation Solver. The methodology is designed to extend across applications, but this POC is scoped to one.
3. Production integration. POC deliverables demonstrate the approach against real data. Integration into the Escalation Solver application is a subsequent engagement activity.
4. Document and attachment scanning. This POC is scoped to free-text fields within escalation tickets.
5. Ground truth remediation at scale. If the existing reference data contains significant quality issues, Contractor will document the findings and recommend a remediation path. Resolving data quality issues at scale is beyond this POC scope and would be addressed in a subsequent engagement.

Material changes to assumptions, scope, or deliverables, or requests beyond stated exclusions, may require a formal change request with adjusted pricing.

---

### Subsection: Risk Factors

Header: **Risk Factors**

The following risks have been identified along with their respective mitigations:

| Risk | Mitigation |
| :--- | :--- |
| Data quality issues discovered during the assessment phase (contradictory, incomplete, or insufficient reference data). | The exploratory data analysis deliverable documents findings formally. Contractor and Lam Research jointly determine whether to proceed with the build phase, adjust scope, or extend the engagement to address data quality. |
| Data, equipment, or environment access delays due to internal coordination. | The three-week period of performance does not begin until access is provided. Contractor cannot control internal scheduling. |
| Subject matter expert availability constraints compress the effective build window. | Lam Research designates a subject matter expert with availability during the POC period. If response times extend beyond the agreed window, the timeline extends accordingly. |
| Data volume exceeds what the three-week POC can process. | Volume and scope are agreed during the discovery phase before the build phase begins. |
| Scope requests beyond the agreed five fields and two entity types. | POC scope is defined with explicit exclusions. Additional requests are documented as candidates for the subsequent engagement and may be subject to a formal change request process. |

---

## Placement Within Section 1

The order of content within Section 1 should be:

1. (Already in doc) Project name and three-week POC description paragraph.
2. (Already in doc) Three-bullet "Services under this SOW are limited to the following scope" list.
3. (Already in doc) Phase 1 deliverables paragraph.
4. (Already in doc) Phase 2 deliverables paragraph.
5. **NEW: Success Criteria subsection.**
6. **NEW: Engagement Scope subsection (with table).**
7. **NEW: Detailed Approach subsection.**
8. **NEW: Timeline subsection (with table).**
9. **NEW: Deliverables subsection.**
10. **NEW: Execution Options subsection (with table).**
11. **NEW: Assumptions subsection.**
12. **NEW: Exclusions subsection.**
13. **NEW: Risk Factors subsection (with table).**
14. (Already in doc) "SOW-specific assumptions" subsection — KEEP this even though there is some overlap with the new Assumptions subsection. The SOW-specific assumptions are purpose-built for the SOW timing/access gates and are worth retaining as a distinct callout. If you find they are redundant after the new Assumptions subsection is in place, merge them into the Assumptions subsection by appending the two SOW-specific items as items 12 and 13 of the consolidated list. Do not silently drop them.
15. **DELETE: the "incorporated by reference" sentence that previously closed Section 1.**

---

## Page Layout Impact

This change will materially increase the length of Section 1. The SOW will likely grow from 3 pages to 5-7 pages. Update page footers accordingly ("Page X of N" where N is the new total). Confirm:

- Letterhead block remains at the top of every page.
- Page footer numbering is correct for the new total page count.
- Section numbering (1 through 8) and Signature Block remain in their correct locations.
- Section 2 (Acceptance Criteria) starts on a new logical break, not mid-paragraph.

If the document grows substantially (8+ pages), flag back to Colin before saving — that may indicate the new content was duplicated rather than added cleanly.

---

## Verification Checks (Run Before Saving)

- [ ] The "incorporated by reference" sentence is fully removed from Section 1.
- [ ] All nine new subsections (Success Criteria through Risk Factors) appear in the listed order within Section 1.
- [ ] No content was dropped from the source POC proposal or engagement pricing one-pager (success criteria 1-5, engagement scope 4 rows, both phase descriptions, timeline 2 rows, 7 deliverables, 2 execution options, 11 assumptions, 5 exclusions, 5 risk factors). Count each list against the spec.
- [ ] No external document is incorporated by reference anywhere in Section 1.
- [ ] Bold subsection headers are visually distinct from body paragraphs but match the existing Section 1 paragraph styling (do not introduce new fonts or colors).
- [ ] The Engagement Scope, Timeline, Execution Options, and Risk Factors tables render cleanly without column overflow or broken rows.
- [ ] Section 3 (Fee Schedule) is unchanged from the prior spec ($6K + $9K = $15K NTE table).
- [ ] All other sections (Effective Date, Section 2, Section 4 through Section 8, Signature Block) are unchanged from the prior spec.
- [ ] Updated page footer numbering reflects the new total page count.
- [ ] Saved as a new file (do not overwrite prior version). Suggested filename: `BAYON-MAS-0013142_Lam_Research_IP_Detection_POC_v2_2026-04-17.docx`.

---

## Source Documents Used For This Spec (For Audit Trail Only)

The inline content above was extracted from these client-facing documents that Lam has already received:

- POC Proposal: `/lam_research/ip_protection/deliverables/poc_proposal_2026-04-09.md` (Sections 01 Problem Statement / Success Criteria, 02 Proposed Approach, 03 Scope and Timeline, 05 Assumptions, 06 Risk Factors).
- Engagement Pricing one-pager: `/lam_research/ip_protection/deliverables/engagement_pricing_2026-04-09.html` (Engagement Scope table, Assumptions, Exclusions, Execution Options, Included in This Engagement).

Where the two source documents had overlapping content with slightly different wording, the more recent or more complete wording was used. Nothing was simplified or dropped.

---

## End of Follow-Up Instructions

When complete, report back to Colin with:

1. New filename.
2. Final page count.
3. Confirmation that the "incorporated by reference" sentence is removed.
4. Confirmation that all nine new subsections are in place.
5. Any deviations from this spec.
