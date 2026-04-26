# SOW Filling Instructions: For Microsoft Word Claude Session

**Engagement:** Lam Research IP Protection — Confidential Information Detection POC
**MSA Reference:** BAYON-MAS-0013142 (effective June 12, 2018)
**Source Template:** The currently-loaded SOW in your Word session was previously used for "Sarthak Gupta Mar26" — a Data Engineer SOW for the unrelated "GCS Data Lake and Architecture" project. Your job is to overwrite the engagement-specific content with the new POC content while preserving the template's structural/legal scaffolding.
**Spec author:** Singularity skill session, 2026-04-17, working from the engagement research library at `/home/cmoore/programming/ai_opportunities/lam_research/ip_protection/`
**Audience:** Claude operating inside Microsoft Word, with the existing SOW .docx file open and editable.

---

## How To Use This Document

1. Read the entire spec end-to-end before making any edits. Several sections cross-reference each other.
2. Work top-to-bottom through "Section-by-Section Instructions." Each section tells you what's currently there, what to do, and provides exact replacement text where applicable.
3. After all section edits, run the "Verification Checks" at the end before saving the final file.
4. Flag any items in the "Items to Confirm with Colin" list back to the user before finalizing.

**Preserve all formatting:** font, sizes, indentation, numbering, underlining of section labels, BAYONE letterhead block, page footers ("Page X of 3"), and signature block layout. The template's visual identity is BayOne's standard; do not restyle.

---

## High-Level Summary of Changes

| Section | Change Type |
|---|---|
| Header / Letterhead | Keep as-is |
| Effective Date | Update from "Feb 1, 2026" to "May 1, 2026" |
| Section 1: Services to be Provided | Replace entirely (delete GCS Data Lake content, paste POC content) |
| Section 2: Acceptance Criteria | Keep template default (MSA Section 3) |
| Section 3: Fee Schedule | Replace table entirely (was T&M with hourly rates; now fixed-fee milestone table) |
| SOW Term (Page 2) | Replace dates with access-triggered language |
| Total Amount NTE (Page 2) | Update from $11,840 to $15,000 |
| Invoice Schedule (Page 2) | Update from "Monthly" to milestone-and-approval language |
| Section 4: Expenses | Keep as-is |
| Section 5: Equipment | Replace blanks with new language about Lam-IT-coordinated provisioning |
| Section 6: Background Technology Disclosure | Change from ☒ None to ☒ See immediately below; add 5-item high-level disclosure |
| Section 7: Third-Party Technology Disclosure | Change from ☒ None to ☒ See immediately below; add disclosure list |
| Section 8: Approved Subcontractors | Mark "None" — resource is full-time BayOne employee |
| Signature Block (BayOne column) | Fill: Anuj Sehgal, VP of Sales, BayOne Solutions Inc. |
| Signature Block (Lam column) | Leave blank for Lam to fill |

---

## Section-by-Section Instructions

### Header / Letterhead — KEEP AS-IS

**What's there:**
- BayOne logo
- "4637 Chabot Dr., Suite 200 / Pleasanton, CA 94588 / Phone: +1 888 537 8068 / Fax: +1 408 228 0753"
- "BayOne Solutions Inc."
- "STATEMENT OF WORK"
- "BAYONE-SOW"
- "Contract for Independent Contractor or Consultant Services"
- "[BAYON-MAS-0013142]"

**Action:** Do not modify. Confirm the letterhead appears on all three pages and is consistent.

---

### Effective Date Block — UPDATE

**What's there (verbatim, near the top of page 1):**

> This Statement of Work ("SOW") effective **Feb 1, 2026** ("Statement of Work Effective Date"), is by and between **Lam Research Corporation** ("Company") and **BayOne Solutions Inc.** ("Contractor") and made pursuant to that certain Contract for Independent Contractor or Consultant Services (BAYON-MAS-0013142), effective as of June 12, 2018 (the "Agreement"). Capitalized terms used herein without definition shall have the meanings ascribed to them in the Agreement.

**Action:** Replace `Feb 1, 2026` with `May 1, 2026`. Preserve bold formatting on the date and on "Lam Research Corporation" and "BayOne Solutions Inc." Leave everything else identical.

**Replacement text:**

> This Statement of Work ("SOW") effective **May 1, 2026** ("Statement of Work Effective Date"), is by and between **Lam Research Corporation** ("Company") and **BayOne Solutions Inc.** ("Contractor") and made pursuant to that certain Contract for Independent Contractor or Consultant Services (BAYON-MAS-0013142), effective as of June 12, 2018 (the "Agreement"). Capitalized terms used herein without definition shall have the meanings ascribed to them in the Agreement.

---

### Section 1: Services to be Provided — REPLACE ENTIRELY

**What's there (verbatim, the GCS Data Lake content to DELETE):**

> 1. **Services to be Provided** (underlined): Contractor shall render such services as may be necessary to complete in a professional manner the project described as follows:
>
>    **GCS Data Lake and Architecture**
>    Implement new customer requirements and features in our existing application.
>    Designs, develops, troubleshoots, and debugs software programs for enhancements and new products.
>    Develops software and tools in support of design, infrastructure, and technology platforms.
>    Determines hardware compatibility and/or influences hardware design.
>    Maintain existing code base and investigating problem areas.
>    Demonstrating solutions by providing documentation, flowcharts, and clear code
>    Work with cross functional teams throughout the organization

**Action:** Delete everything from "GCS Data Lake and Architecture" through "Work with cross functional teams throughout the organization." Replace with the new content below.

**Keep:** The numbered "1." with underlined "Services to be Provided" label. Keep the lead-in sentence "Contractor shall render such services as may be necessary to complete in a professional manner the project described as follows:" Keep the paragraph indentation pattern.

**Replacement content (paste under the lead-in sentence):**

> **Confidential Information Detection — Proof of Concept (Escalation Solver)**
>
> Contractor shall perform a three-week proof-of-concept engagement to demonstrate an improved detection methodology for customer-confidential information within the Escalation Solver application. The engagement is delivered in two phases: a Discovery and Data Assessment phase (Phase 1) and a Detection Build and Benchmarking phase (Phase 2).
>
> Services under this SOW are limited to the following scope:
>
> - Application in scope: Escalation Solver (five free-text fields, approximately 4,000 to 5,000 characters each).
> - Entity types in scope: customer name and fab identifier.
> - Duration: three weeks from the date BayOne receives all required access (environment access, data access, reference materials, equipment, and Lam Research SME availability).
>
> Phase 1 deliverables: an exploratory data analysis report including baseline data quality assessment, maximum achievable detection accuracy determination against the available reference data, and documentation of detection targets.
>
> Phase 2 deliverables: a working detection demonstration against real Escalation Solver data for the two in-scope entity types, benchmarking of detection performance against the prior effort baseline as documented by Lam Research, documentation of the layered detection methodology, and a scaling path for extending the approach to additional entity types, fields, and applications in subsequent engagements.
>
> The full scope, assumptions, exclusions, risk factors, and success criteria are as described in the Confidential Information Detection POC Proposal (April 2026) and the Engagement Pricing one-pager (April 2026), which are incorporated by reference into this SOW. In the event of any conflict between those documents and this SOW, this SOW controls.
>
> SOW-specific assumptions:
>
> - Lam Research provides Contractor with all required access (environment, data, reference materials, equipment) and Lam Research SME availability prior to the engagement start date. The three-week period of performance does not begin until all access is in place.
> - Engagement start date shall be no earlier than the week of May 4, 2026, to allow time for access provisioning, equipment delivery, internal Lam Research approvals, and any legal or procurement actions arising from this SOW.

**Formatting note:** Bold the project name line ("Confidential Information Detection — Proof of Concept (Escalation Solver)"). Use a bullet list (round bullets) for the three "scope limited to" items and the two "SOW-specific assumptions" items. The two phase deliverables are paragraphs, not bullets. Match the indentation level used in the rest of the section.

---

### Section 2: Acceptance Criteria — KEEP TEMPLATE DEFAULT

**What's there:**

> 2. **Acceptance Criteria** (underlined):
>
>    Not applicable.
>
>    See immediately below:
>
>    Acceptance criteria shall be as set forth in Section 3 of the Agreement.
>
>    ☐ Additional sheets attached.

**Action:** Leave the section structure unchanged. Confirm:
- "Acceptance criteria shall be as set forth in Section 3 of the Agreement" remains present (this is the operative default we want).
- The "Additional sheets attached" checkbox stays UNCHECKED.

**Note on the odd template formatting:** The template has both "Not applicable" and "See immediately below" as artifacts of a multi-option checkbox structure that didn't print cleanly. If your view shows checkboxes, ensure neither "Not applicable" nor "Additional sheets attached" is checked, and that the section relies on the MSA Section 3 default.

---

### Section 3: Fee Schedule — REPLACE TABLE ENTIRELY

**What's there (verbatim, to DELETE):**

> 3. **Fee Schedule.** This project will be implemented on a time and material basis and following are the hourly rate and estimated costs.
>
> | Role/Title | Quantity | Hours | Rate | Total Amount (Not to Exceed) |
> | :--- | :--- | :--- | :--- | :--- |
> | **Data Engineer** | 1 | 320 | $37/hr. | $11,840 |

**Action:** Replace BOTH the lead-in sentence ("This project will be implemented on a time and material basis...") AND the table. The new model is fixed-fee, deliverable-based — not T&M.

**Keep:** The numbered "3." with underlined "Fee Schedule" label.

**Replacement lead-in sentence:**

> This project will be implemented on a fixed-fee, deliverable-based basis. The total fee is allocated across the project phases and corresponding deliverables as set forth below.

**Replacement table** (replace the existing table cell-for-cell; preserve table style/borders):

| Phase / Deliverable | Quantity | Fixed Fee |
| :--- | :--- | :--- |
| **Phase 1 — Discovery and Data Assessment** (exploratory data analysis report including baseline data quality assessment, maximum achievable accuracy determination, and detection target documentation) | 1 | $6,000 |
| **Phase 2 — Detection Build and Benchmarking** (working detection demonstration, performance benchmarking against prior effort baseline, layered detection methodology documentation, and scaling path documentation) | 1 | $9,000 |
| **Total (Not to Exceed)** | | **$15,000** |

**Formatting notes:**
- The "Phase 1" and "Phase 2" labels in the first column should be bold.
- Drop the "Hours" and "Rate" columns from the original template — they do not apply to a fixed-fee model. The new table has three columns: Phase / Deliverable | Quantity | Fixed Fee.
- The "Total (Not to Exceed)" row spans the first two columns merged, with the dollar amount in the third column. Bold the total label and the total dollar amount.

---

### SOW Term Field (Page 2) — REPLACE WITH ACCESS-TRIGGERED LANGUAGE

**What's there (verbatim, near the top of page 2):**

> SOW Term: The period of performance of the Services shall commence on Feb 1, 2026 and end on Mar 31, 2026 ("SOW Term").

**Action:** Replace the sentence after "SOW Term:" entirely.

**Replacement text:**

> SOW Term: The period of performance of the Services shall commence on the date Contractor receives all required access (Lam Research environment access, Escalation Solver data, reference materials, equipment, and Lam Research SME availability), provided such access is in place no earlier than the week of May 4, 2026. The period shall conclude three (3) weeks following the access-in-place date, unless extended by mutual written agreement of the parties ("SOW Term").

**Why the change:** The original calendar date range does not match a POC whose start is gated by Lam-side access provisioning. The replacement language ties the start to access in place, matches what was committed in the Engagement Pricing one-pager (April 2026), and protects BayOne against access delays compressing the engagement.

---

### Total Amount (Not to Exceed) Line (Page 2) — UPDATE AMOUNT

**What's there (verbatim, page 2):**

> Total Amount (Not to Exceed): **$11,840.00**

**Action:** Replace `$11,840.00` with `$15,000.00`. Preserve the bold formatting on the dollar amount.

**Replacement text:**

> Total Amount (Not to Exceed): **$15,000.00**

**Cross-check:** This must equal the Fee Schedule table's total in Section 3.

---

### Invoice Schedule Line (Page 2) — UPDATE

**What's there (verbatim, page 2):**

> Invoice schedule: Monthly

**Action:** Replace with milestone-and-approval-gated language.

**Replacement text:**

> Invoice schedule: Per milestone completion, with each milestone invoice issued upon Lam Research's written approval of the corresponding milestone deliverable, in accordance with Section 4 of the Agreement.

**FLAG FOR COLIN:** The user instruction was "on receipt of POC approval." This replacement interprets that as per-milestone invoicing gated by Lam's approval of each milestone's deliverable, which preserves the 40/60 milestone payment structure already committed in the Engagement Pricing one-pager (April 2026). If the user's intent was instead a single invoice at end of POC for the full $15,000, the replacement text becomes: "A single invoice for the full Fixed Fee, issued upon Lam Research's written approval of the POC deliverables, in accordance with Section 4 of the Agreement." Confirm with the user before finalizing if there is any ambiguity.

---

### Payment Terms Note (Page 2) — KEEP AS-IS

**What's there:**

> "Payment terms shall be subject to Section 4 of the MSA."

**Action:** Leave unchanged.

**Also keep:** The template's parenthetical "(Company generally pays Contractors 30 days after Company receives and approves their invoice for completed work.)" remains as-is.

---

### Section 4: Expenses — KEEP AS-IS

**What's there:** Standard template language about no expense reimbursement absent prior written approval, scope-change clause, Company travel intranet website reference.

**Action:** Leave the entire section unchanged. We are not anticipating reimbursable expenses for this remote/hybrid POC.

---

### Section 5: Equipment — REPLACE WITH ACCESS-COORDINATED LANGUAGE

**What's there (verbatim):**

> 5. **Equipment**: Contractor will supply all its own equipment for this SOW, except for the following equipment which will be loaned to Contractor by Company for the duration of this SOW.
>
>    Equipment Type `_________________` Serial No. `_________________`
>
>    No license or other right is hereby granted in or to this equipment, except the right to use it in performing the services. Contractor agrees to return the equipment in good condition to Company promptly after termination of the SOW and, if it fails to do so, will pay Company the full manufacturer's suggested retail price for the equipment.

**Action:** Replace the entire body of Section 5 with the new language below. Keep the numbered "5." with underlined "Equipment" label.

**Replacement text:**

> 5. **Equipment**: Contractor will supply its own laptop and standard productivity tooling. Specific equipment to be loaned by Lam Research (such as a virtual machine, secure workstation, VPN tokens, or other equipment necessary for access to the Lam Research environment selected as the execution environment) shall be agreed between Contractor and Lam Research IT prior to the engagement start date. Equipment Type and Serial Number shall be documented at the time of delivery to Contractor. All loaned equipment must be in Contractor's possession or accessible to Contractor before the engagement start date.
>
> No license or other right is hereby granted in or to this equipment, except the right to use it in performing the services. Contractor agrees to return the equipment in good condition to Company promptly after termination of the SOW and, if it fails to do so, will pay Company the full manufacturer's suggested retail price for the equipment.

**Why the change:** Mikhail confirmed Option A (Lam environment) on 2026-04-16 as Lam's preferred execution mode. The replacement language anticipates Lam-provided equipment for environment access without locking specifics that have not been agreed yet. The "must be in Contractor's possession or accessible before the engagement start date" clause ties equipment delivery to the SOW Term gate, protecting BayOne against access delays.

---

### Section 6: Background Technology Disclosure — CHANGE TO "SEE BELOW" AND ADD DISCLOSURE LIST

**What's there:**

> 6. **Background Technology Disclosure**: The following is a complete list of all Background Technology:
>
>    - [x] None
>    - [ ] See immediately below:

**Action:** Change the checkbox state — uncheck "None" and check "See immediately below." Add the disclosure list below.

**Replacement text:**

> 6. **Background Technology Disclosure**: The following is a complete list of all Background Technology:
>
>    - [ ] None
>    - [x] See immediately below:
>
>    Contractor's pre-existing Background Technology brought to this engagement includes:
>
>    1. Layered detection methodology framework: Contractor's proprietary approach to entity detection that sequentially applies deterministic, statistical/machine learning, and generative AI techniques.
>    2. Evaluation protocol for entity-detection accuracy measurement and accuracy ceiling determination.
>    3. Exploratory data analysis methodology for entity-detection problems, including data quality assessment and reference data evaluation procedures.
>    4. Pre-existing scripts, pipeline templates, and tooling developed by Contractor in prior similar engagements.
>    5. Documentation templates and reporting frameworks used by Contractor across detection and redaction engagements.

**Formatting:** Use a numbered list (1 through 5). Each item is a single sentence. The phrase "Background Technology" is a defined term in the MSA, so capitalize as shown.

**Why this matters:** Disclosing Background Technology preserves Contractor (BayOne) ownership of these pre-existing assets when the MSA's IP assignment language transfers ownership of work product to Company (Lam). NOT disclosing leaves BayOne exposed to a future claim that the methodology was developed for Lam.

---

### Section 7: Third-Party Technology Disclosure — CHANGE TO "SEE BELOW" AND ADD LIST

**What's there (spans pages 2-3):**

> 7. ☐ Additional sheets attached.
>
>    Third-Party Technology Disclosure (underlined): The following is a complete list of all Third-Party Technology:
>
>    ☒ None
>
>    ☐ See immediately below:

**Action:** Uncheck "None"; check "See immediately below." Add the disclosure list below. Keep "Additional sheets attached" UNCHECKED (the list fits in the SOW body).

**Replacement text:**

> 7. ☐ Additional sheets attached.
>
>    **Third-Party Technology Disclosure**: The following is a complete list of all Third-Party Technology:
>
>    ☐ None
>
>    ☒ See immediately below:
>
>    Anticipated Third-Party Technology used during the engagement:
>
>    1. spaCy — open-source natural language processing library (MIT License).
>    2. Microsoft Presidio — open-source PII detection and redaction framework (MIT License).
>    3. scikit-learn — open-source machine learning library (BSD License).
>    4. HuggingFace Transformers and associated pre-trained models — open-source library (Apache 2.0 License); pre-trained models subject to model-specific licenses.
>    5. Standard Python data science libraries (pandas, numpy, and similar) — open-source licenses.
>    6. Microsoft Azure AI services — to the extent used within Lam Research's existing Azure tenancy under Lam Research's existing licensing.

**Formatting:** Numbered list 1 through 6. Each item is a single line.

**Why this matters:** Disclosing Third-Party Technology prevents later misrepresentation claims (Contractor representing third-party tools as Contractor IP) and clarifies which licenses govern which components of the deliverable.

---

### Section 8: Approved Subcontractors — MARK NONE

**What's there:**

> 8. **Approved Subcontractors**: The following subcontractors will be providing Services under this SOW. Company's approval of the list of subcontractors does not negate or waive any requirements and conditions regarding subcontractors set forth in the SOW.
>
>    Subcontractor: ___________________________ Statement of Services to be delegated to Subcontractor:
>    ----------------------------------- -----------------------------------

**Action:** Add a clear "None" indicator. The resource performing services under this SOW is a full-time onshore BayOne Solutions employee. No subcontractors will be used.

**Replacement text:**

> 8. **Approved Subcontractors**: No subcontractors will be providing Services under this SOW. All Services hereunder will be performed by employees of BayOne Solutions Inc.

**Action note:** Delete the blank "Subcontractor: ____" and "Statement of Services..." line and the dashed underlines beneath them. Replace with the single replacement sentence above.

---

### Signature Block (End of Page 3) — FILL BAYONE COLUMN, LEAVE LAM COLUMN BLANK

**What's there:**

> Executed the latest date below by the authorized representatives of the parties for the SOW Effective Date.
>
> | **Lam Research Corporation** | **BayOne Solutions Inc.** |
> | :--- | :--- |
> | By: | By: |
> | Name: | Name: |
> | Title: | Title: |
> | Date: | Date: |

**Action:**

- **Lam Research Corporation column:** Leave all four lines (By, Name, Title, Date) BLANK. Lam will fill these.
- **BayOne Solutions Inc. column:** Fill Name and Title. Leave By (signature line) and Date BLANK for Anuj's wet signature.

**Replacement text for the BayOne column:**

> | | **BayOne Solutions Inc.** |
> | :--- | :--- |
> | | By: |
> | | Name: Anuj Sehgal |
> | | Title: VP of Sales |
> | | Date: |

**Note:** The "By:" line is for the signature itself. Leave blank for Anuj's wet/electronic signature. The "Date:" line is for the signature date — leave blank, Anuj fills at signing time.

---

## Page Layout and Footer Verification

The original template is exactly **3 pages**. After your edits, confirm:

- **Page 1** ends with the Fee Schedule table and footer "Page 1 of 3."
- **Page 2** contains the SOW Term, Total Amount NTE, Invoice schedule, Payment Terms note, Section 4 (Expenses), Section 5 (Equipment), and the start of Section 6 (Background Tech). Footer: "Page 2 of 3."
- **Page 3** contains the rest of Section 6 (if it spilled), Section 7 (Third-Party Tech), Section 8 (Subcontractors), and the Signature Block. Footer: "Page 3 of 3."
- **Letterhead block** (BayOne Pleasanton address) appears at the top of all three pages.

If the new content has caused page reflow such that you are now at 4 pages or 2 pages, adjust paragraph spacing or list compactness to restore 3 pages. Do NOT shrink fonts or drop required content to fit. If 3 pages is genuinely impossible without dropping content, flag it back to the user.

---

## Verification Checks (Run Before Saving)

Walk through this checklist after all edits are made.

### Content Consistency

- [ ] All instances of "Sarthak Gupta" removed (probably none in template body, but search to confirm).
- [ ] All instances of "GCS Data Lake" or "Data Lake" removed.
- [ ] All instances of "Data Engineer" removed (was the prior role title).
- [ ] All instances of "$11,840" replaced with "$15,000" (check both Section 3 table and Page 2 Total Amount line).
- [ ] All instances of "$37/hr" or any other hourly rate removed.
- [ ] All instances of "Feb 1, 2026" updated (Effective Date → "May 1, 2026"; SOW Term → access-triggered language with no calendar date).
- [ ] All instances of "Mar 31, 2026" removed (was the prior end date).
- [ ] All instances of "320 hours" or any specific hour count removed.
- [ ] All instances of "time and material basis" replaced with "fixed-fee, deliverable-based basis" in the Section 3 lead-in.
- [ ] All instances of "Monthly" (in Invoice schedule context) replaced with the milestone-and-approval language.

### Section Integrity

- [ ] Section 1 (Services) contains the new POC services description, scope boundaries, phase deliverables, and SOW-specific assumptions paragraphs.
- [ ] Section 2 (Acceptance Criteria) is unchanged from template default.
- [ ] Section 3 (Fee Schedule) table has three columns (Phase/Deliverable | Quantity | Fixed Fee) with two phase rows and a Total NTE row.
- [ ] Section 4 (Expenses) is unchanged from template default.
- [ ] Section 5 (Equipment) has the new Lam-IT-coordinated provisioning language and the access-before-start clause.
- [ ] Section 6 (Background Technology) has "None" UNCHECKED and "See immediately below" CHECKED, with a 5-item numbered list.
- [ ] Section 7 (Third-Party Technology) has "None" UNCHECKED and "See immediately below" CHECKED, with a 6-item numbered list.
- [ ] Section 8 (Approved Subcontractors) has the single sentence "No subcontractors will be providing Services under this SOW. All Services hereunder will be performed by employees of BayOne Solutions Inc."
- [ ] Signature Block has Anuj Sehgal as Name and VP of Sales as Title in the BayOne column. By and Date lines blank in BayOne column. All four lines blank in Lam column.

### Formatting

- [ ] Section labels (1 through 8) retain underline formatting.
- [ ] Phase 1 and Phase 2 labels in Section 3 table are bold.
- [ ] Total Amount NTE on Page 2 ($15,000.00) is bold.
- [ ] Lam Research Corporation and BayOne Solutions Inc. names retain bold throughout.
- [ ] All bullet lists are formatted consistently (round bullets in Section 1; numbered lists 1-N in Sections 6 and 7).
- [ ] Letterhead block intact and identical on all three pages.
- [ ] Footer "Page X of 3" present on each page.

### Math Cross-Check

- [ ] Section 3 table: Phase 1 ($6,000) + Phase 2 ($9,000) = $15,000.
- [ ] Page 2 Total Amount NTE ($15,000.00) matches Section 3 table total.

### Final Save

- [ ] Save as a new file. Suggested filename: `BAYON-MAS-0013142_Lam_Research_IP_Detection_POC_2026-04-17.docx`
- [ ] Do NOT overwrite the original Sarthak Gupta SOW file. Keep both files for reference.

---

## Items to Confirm with Colin Before Sending to Lam

These are flagged for explicit confirmation before the SOW is countersigned by Anuj and sent to Lam procurement:

1. **Invoice schedule interpretation.** The replacement text uses milestone-and-approval-gated language preserving the 40/60 split from the Engagement Pricing one-pager. Confirm this matches the user's intent (vs. a single invoice at end of POC). See FLAG FOR COLIN under Invoice Schedule above.

2. **Effective Date specificity.** The recommended Effective Date is May 1, 2026. Confirm this works with internal BayOne and Lam procurement timing. If procurement signature is expected later (mid-May), update to the actual countersignature date.

3. **Anuj's title at BayOne.** Recommended title is "VP of Sales" based on the engagement org chart. Confirm Anuj's official SOW signature title is exactly that and not (for example) "Vice President of Sales" or another formal variant.

4. **Background Technology disclosure level.** The 5-item disclosure is written at medium-but-high-level specificity per user instruction. Confirm the wording does not over-reveal proprietary methodology details. The current wording names the methodology categories (deterministic / statistical-ML / generative AI sequencing) and asset types (templates, scripts, frameworks) without revealing specific techniques, models, or trade-secret implementations.

5. **Third-Party Technology completeness.** The 6-item list anticipates the typical NLP and Azure AI stack. If the team plans to use a tool not listed (e.g., a specific commercial library, a particular fine-tuned model, or an LLM API outside Lam's Azure tenancy), add it before sending.

6. **Equipment section.** The new language defers specifics to "Contractor and Lam Research IT" coordination. Confirm Daniel Harrison (Lam tech access counterpart per Mikhail's 2026-04-16 email) is the right interface, and that the access-before-start clause is consistent with what Colin will negotiate in that workstream.

---

## Reference Documents (For Context Only — Do Not Modify)

These documents in the engagement research library informed this spec. The Word Claude session does not need to read them, but Colin may reference them during review:

- POC Proposal: `/lam_research/ip_protection/deliverables/poc_proposal_2026-04-09.md`
- Engagement Pricing one-pager: `/lam_research/ip_protection/deliverables/engagement_pricing_2026-04-09.html`
- SOW template structural decomposition: `/lam_research/ip_protection/research/09_execution_kickoff_sow_template_structure_2026-04-17.md`
- SOW filling strategy (this spec was derived from): `/lam_research/ip_protection/research/09_execution_kickoff_sow_filling_strategy_2026-04-17.md`
- Mikhail email decomposition + tech access workstream: `/lam_research/ip_protection/research/09_execution_kickoff_mikhail_signal_and_tech_access_2026-04-16.md`
- Org chart: `/lam_research/ip_protection/org_chart.md`

---

## End of Instructions

When all edits are complete, all verification checks pass, and the file is saved with a new name, report back to Colin with:

1. The new filename.
2. Confirmation that page count is 3.
3. Any of the "Items to Confirm with Colin" that you were unable to resolve and need user input on.
4. Any places where you had to deviate from this spec (with reason).
