# 09 - SOW Template: Structural Decomposition

**Source:** /lam_research/ip_protection/source/lam_sow.pdf (extracted via pdf-extractor)
**Source Date:** 2026-04-17 (received from Lam procurement; template effective Feb 1, 2026 from prior use)
**Document Set:** 09 (Execution Kickoff: SOW template + Mikhail email signaling Lam moving to contract phase)
**Pass:** Section-by-section structural decomposition of the SOW template

---

## Overview

The document is a three-page Statement of Work ("SOW") template issued on BayOne Solutions Inc. letterhead. It is an addendum to a pre-existing Master Services Agreement ("Agreement") and is structured as eight numbered sections (Services to be Provided, Acceptance Criteria, Fee Schedule, Expenses, Equipment, Background Technology Disclosure, Third-Party Technology Disclosure, Approved Subcontractors), plus a header/letterhead block, a commercial/term block straddling pages 1 and 2, and a signature block on page 3.

The prior fill on record is an individual contractor SOW for "Sarthak Gupta Mar26" — a Data Engineer supporting the "GCS Data Lake and Architecture" project on a time-and-materials basis, Feb 1, 2026 through Mar 31, 2026, at $37/hour for 320 hours, Not to Exceed $11,840.00. That fill is used throughout this document as the example of how each field was populated previously.

The template mixes rendered checkboxes (both `☐` / `☒` filled glyphs and Markdown-style `- [ ]` / `- [x]` checklist items as extracted), underscored blank fields (`_________________`), and free-form prose areas. Several sections present mutually exclusive options (e.g., "None" vs. "See immediately below") rather than free text — filling the template is often a matter of selecting the correct option and then expanding on it if needed.

---

## Header / Letterhead (Pages 1, 2, 3)

The letterhead appears at the top of every page. Pages 2 and 3 repeat the address block but omit the second-line "BayOne Solutions Inc." company name that anchors page 1. Page 1 is the only page that carries the full title block.

### Letterhead Fields (all pages)

| Field | Value |
| :--- | :--- |
| Logo | `[BAYONE Logo]` (image placeholder on page 1; rendered as the word "BAYONE" on pages 2 and 3) |
| Street address | `4637 Chabot Dr., Suite 200` |
| City / State / ZIP | `Pleasanton, CA 94588` |
| Phone | `+1 888 537 8068` |
| Fax | `+1 408 228 0753` |

### Page 1 Title Block (after letterhead)

Following the address block, page 1 adds (in order):

1. `BayOne Solutions Inc.` (second-line company label)
2. `**STATEMENT OF WORK**` (bold, centered, treated as the document title)
3. `**BAYONE-SOW**` (bold document identifier / template code)
4. `Contract for Independent Contractor or Consultant Services` (descriptive subtitle)
5. `[BAYON-MAS-0013142]` (bracketed MSA identifier — the governing Master Services Agreement number)

### Preamble Paragraph

Immediately below the title block, an unnumbered preamble paragraph defines the parties and the governing agreement:

> This Statement of Work ("SOW") effective **Feb 1, 2026** ("Statement of Work Effective Date"), is by and between **Lam Research Corporation** ("Company") and **BayOne Solutions Inc.** ("Contractor") and made pursuant to that certain Contract for Independent Contractor or Consultant Services (BAYON-MAS-0013142), effective as of June 12, 2018 (the "Agreement"). Capitalized terms used herein without definition shall have the meanings ascribed to them in the Agreement.

Fillable elements in the preamble:

- **Statement of Work Effective Date** — bolded inline, prior fill: `Feb 1, 2026`
- **Company name** — bolded inline, fixed as `Lam Research Corporation`
- **Contractor name** — bolded inline, fixed as `BayOne Solutions Inc.`
- Governing agreement identifier — `BAYON-MAS-0013142`, effective `June 12, 2018`

The preamble formally incorporates the MSA by reference ("Capitalized terms ... shall have the meanings ascribed to them in the Agreement"). This means anywhere the template uses a capitalized defined term without defining it (e.g., "Services", "Background Technology", "Third-Party Technology"), the definition lives in the MSA.

---

## Section 1 — Services to be Provided

### Heading (as rendered)

`1.  **<u>Services to be Provided</u>**:` — numbered, bold, underlined heading followed by a colon.

### What the section asks for

Free-form prose describing the project scope. The lead-in verbatim: "Contractor shall render such services as may be necessary to complete in a professional manner the project described as follows:" — this framing positions the content that follows as the definition of "the project."

### Prior fill (Sarthak example)

A short project title on its own line, followed by a bulleted-but-unbulleted list of responsibility statements (each sentence on its own line):

> **GCS Data Lake and Architecture**
> Implement new customer requirements and features in our existing application.
> Designs, develops, troubleshoots, and debugs software programs for enhancements and new products.
> Develops software and tools in support of design, infrastructure, and technology platforms.
> Determines hardware compatibility and/or influences hardware design.
> Maintain existing code base and investigating problem areas.
> Demonstrating solutions by providing documentation, flowcharts, and clear code
> Work with cross functional teams throughout the organization

### Formatting conventions observed

- Project title is bold, on its own line.
- Responsibility lines follow, no bullet glyphs, no numbering, just paragraph-style line breaks.
- Mixed sentence-terminator discipline (some lines end in a period, some do not — e.g., "Demonstrating solutions by providing documentation, flowcharts, and clear code" has no trailing period).
- Mixed tense / voice: first-person imperative ("Implement...", "Maintain...") intermingled with third-person indicative ("Designs, develops, troubleshoots..."), reflecting that these lines were copy-pasted from a job-description source.
- No checkboxes in this section.
- No explicit word limit or page limit visible.

### Fillable elements

- Project title (bolded first line)
- Scope narrative (everything after the title, free-form)

---

## Section 2 — Acceptance Criteria

### Heading (as rendered)

`2.  **<u>Acceptance Criteria</u>**:` — numbered, bold, underlined heading followed by a colon.

### What the section asks for

Identifies how Services will be deemed accepted. The template presents three distinct lines (which, in the extracted markdown, appear to have been rendered as three separate blocks rather than as a multiple-choice cluster) plus a trailing checkbox:

| Line | Text as extracted | Apparent role |
| :--- | :--- | :--- |
| 1 | `Not applicable.` | First option — exempt this SOW from an acceptance-criteria clause |
| 2 | `See immediately below:` | Second option — expand with criteria inline |
| 3 | `Acceptance criteria shall be as set forth in Section 3 of the Agreement.` | Default / fallback — defer to MSA Section 3 |
| 4 | `☐ Additional sheets attached.` | Checkbox — indicates an attachment with additional criteria |

### Template artifact / oddity

In the source rendering the three options above are stacked as plain prose rather than as a set of radio-button-style selectable choices. There is no leading checkbox glyph on "Not applicable" or "See immediately below" in the prior fill — they appear as declarative sentences. The third line ("Acceptance criteria shall be as set forth in Section 3 of the Agreement") reads as a default fallback that remains applicable when neither of the preceding choices is actively asserted. The `☐ Additional sheets attached.` line is the only unambiguous checkbox in this block.

The prior fill (Sarthak) left the block as-is: all three prose options remained, the checkbox was left unchecked. This suggests the template is typically accepted as drafted (i.e., fall back to MSA Section 3), with the Section 2 block functioning more as boilerplate than as an active fill target.

### Fillable elements

- Implicit selection among the three prose options (by deletion or marking in the final signed version)
- `☐ Additional sheets attached.` checkbox
- Any inline criteria text that would follow "See immediately below:" if that option is chosen

---

## Section 3 — Fee Schedule

### Heading (as rendered)

`3.  **<u>Fee Schedule</u>**.` — numbered, bold, underlined heading followed by a period (not a colon, unlike Sections 1 and 2).

### What the section asks for

A pricing table preceded by a single-sentence lead-in that identifies the commercial structure. Lead-in verbatim: "This project will be implemented on a time and material basis and following are the hourly rate and estimated costs."

The lead-in hard-codes the structure as **"time and material basis"** with **"hourly rate and estimated costs."** There is no alternate lead-in for a fixed-fee or milestone-based engagement visible in the template as extracted.

### Fee table structure

A five-column Markdown table:

| Column header | Example fill (Sarthak) |
| :--- | :--- |
| Role/Title | **Data Engineer** (bolded in the cell) |
| Quantity | 1 |
| Hours | 320 |
| Rate | $37/hr. |
| Total Amount (Not to Exceed) | $11,840 |

### Formatting conventions observed

- Single row in the prior fill; the table is structurally expandable to multiple rows (multiple roles) but was used with exactly one.
- "Rate" column uses the format `$N/hr.` (note trailing period after `hr`).
- "Total Amount (Not to Exceed)" column value is formatted without cents (`$11,840`), whereas the separate Total Amount line on page 2 uses cents (`$11,840.00`) — see page 2.
- Role/Title value is bolded; other cells are plain.

### Fillable elements

- Each row: Role/Title, Quantity, Hours, Rate, Total Amount (Not to Exceed)
- (Implicit) number of rows — the table can be extended

### End of page 1

Section 3 is the last section on page 1. Page 1 ends with three stacked `<br>` line breaks and the footer `Page 1 of 3`.

---

## Page 2 Commercial / Term Block (between Sections 3 and 4)

Before Section 4 begins, page 2 opens with a set of standalone commercial and term fields. These are not numbered as part of the Section 3 table — they appear as free-standing lines in the template, immediately under the page 2 letterhead.

### Fields in order of appearance

| Field (as rendered) | Prior fill | Notes |
| :--- | :--- | :--- |
| `Invoice schedule:` | `Monthly` | Inline value; no checkbox, free text |
| `"Payment terms shall be subject to Section 4 of the MSA."` | (fixed language, in quotation marks) | Defers payment terms to MSA Section 4 |
| `SOW Term: The period of performance of the Services shall commence on ___ and end on ___ ("SOW Term").` | Commence `Feb 1, 2026`, end `Mar 31, 2026` | Two inline date fields |
| `Total Amount (Not to Exceed):` | **`$11,840.00`** (bolded) | Distinct from the Fee Schedule table total on page 1; formatted with cents |
| Parenthetical payment-timing note | `(Company generally pays Contractors 30 days after Company receives and approves their invoice for completed work.)` | Fixed boilerplate; not a fillable field |

### Template artifact / oddity

- The **Total Amount (Not to Exceed)** appears *twice* in the document: once as the right-most column of the Fee Schedule table on page 1 (as `$11,840`) and once here on page 2 as its own labeled line (as `$11,840.00`). The page 2 instance uses cents; the page 1 table does not. Both must agree numerically when the template is filled.
- The **Invoice schedule** field has no multiple-choice options rendered in the extraction — it is a single free-text field. The prior fill simply says `Monthly`.
- The **Payment terms** line is a direct quotation (enclosed in double quotation marks) that re-incorporates MSA Section 4 by reference. It is not a fillable field; it is fixed language.
- The **SOW Term** uses prose-style date insertion ("commence on X and end on Y"), not a table or label-and-value format.

---

## Section 4 — Expenses

### Heading (as rendered)

`4. **Expenses**:` — numbered, bold heading followed by a colon. Note: unlike Sections 1, 2, and 3 where the heading uses `<u>...</u>` underline tags, Section 4's heading is bold-only (no underline).

### What the section asks for

A single dense paragraph of fixed contractual language governing expenses. No fillable fields. The clause asserts:

1. The fees above constitute the Contractor's entire remuneration.
2. Contractor will not be reimbursed for expenses absent prior written approval.
3. A material change in scope may trigger renegotiation by mutual written agreement.
4. Preapproved expenses are reimbursed only to the extent reasonable and subject to Company's travel policy.
5. Contractor is responsible for obtaining the then-current version of that policy before submitting a reimbursement request.

Verbatim (opening): "The above fees constitute Contractor's entire remuneration for the services under this SOW. Contractor will not be reimbursed for any expenses incurred in connection with this SOW absent prior written approval of Company..."

### Fillable elements

None. The section is entirely boilerplate.

### Template artifact / oddity

The extracted text contains one minor typo preserved from source: `"a material increase or decrease in; the cost or time"` — an errant semicolon mid-clause. This appears in the template itself and is not an extraction artifact worth correcting in-place.

---

## Section 5 — Equipment

### Heading (as rendered)

`5. **Equipment**:` — numbered, bold, no underline, followed by a colon.

### What the section asks for

Two-part structure: (a) a prose lead-in stating that Contractor supplies its own equipment except as listed, and (b) two blank fields to list Company-loaned equipment.

### Lead-in verbatim

"Contractor will supply all its own equipment for this SOW, except for the following equipment which will be loaned to Contractor by Company for the duration of this SOW."

### Fillable fields

A single indented line with two inline blanks:

`Equipment Type _________________ Serial No. _________________`

Both blanks are rendered as underscore runs (about 17 underscores each). They are arranged side-by-side on a single line rather than as a table — only one equipment entry is structurally provided.

### Trailing fixed language

After the blanks, a fixed-language clause governs equipment return:

"No license or other right is hereby granted in or to this equipment, except the right to use it in performing the services. Contractor agrees to return the equipment in good condition to Company promptly after termination of the SOW and, if it fails to do so, will pay Company the full manufacturer's suggested retail price for the equipment."

### Template artifact / oddity

- Only one equipment row is provided. Listing multiple items requires either attaching a sheet (no "additional sheets attached" checkbox is provided for Section 5) or overflowing into the blanks with semicolon-separated entries.
- The prior fill (Sarthak) left both blanks empty — consistent with "Contractor supplies all its own equipment."

---

## Section 6 — Background Technology Disclosure

### Heading (as rendered)

`6. **Background Technology Disclosure**:` — numbered, bold, no underline, followed by a colon.

### What the section asks for

Requires the Contractor to list all "Background Technology" to be disclosed under the SOW. The capitalized term is a defined term from the MSA (not redefined inline here).

### Lead-in verbatim

"The following is a complete list of all Background Technology:"

### Checkbox options (as rendered)

Rendered in the extraction as Markdown-style checkboxes:

- `- [x] None`
- `- [ ] See immediately below:`

These are **mutually exclusive** options. In the prior fill (Sarthak), `None` is checked (`[x]`) and `See immediately below` is unchecked (`[ ]`).

### Fillable elements

- Checkbox choice between "None" and "See immediately below"
- If "See immediately below" is chosen, free-form list of Background Technology items

### End of page 2

After Section 6 the page ends with a run of stacked `<br>` tags (nine consecutive line breaks in the extraction) and the footer `Page 2 of 3`.

### Template artifact / oddity

Section 6 is **visually split across the page 2 / page 3 boundary in the template layout**, but the actual content of Section 6 ends cleanly at the checkbox pair on page 2. The empty lines that follow are intentional whitespace (reserved for the inline list if "See immediately below" is selected). The ambiguity at the top of page 3 involves Section 7, not Section 6 — see below.

---

## Section 7 — Third-Party Technology Disclosure

### Heading (as rendered)

`7. ☐ Additional sheets attached.`
`   <u>Third-Party Technology Disclosure</u>: The following is a complete list of all Third-Party Technology:`

### What the section asks for

Requires the Contractor to list all "Third-Party Technology" to be disclosed under the SOW. Like "Background Technology," this is a capitalized defined term from the MSA.

### Template artifact / oddity — the Section 7 layout confusion

This is the single strangest structural feature of the template:

- Page 3 **opens** with `7. ☐ Additional sheets attached.` — a checkbox presented as if it were the body of Section 7.
- Only **below** that checkbox does the underlined sub-heading appear: `<u>Third-Party Technology Disclosure</u>:`
- Then the lead-in sentence and its checkbox options follow.

The most likely interpretation is that `☐ Additional sheets attached.` belongs to Section 6 (Background Technology) and was visually pushed onto page 3 by the page break — mirroring the `☐ Additional sheets attached.` checkbox that appears at the bottom of Section 2. Under this reading, Section 7 effectively begins with its underlined sub-heading, not with the "Additional sheets attached" checkbox.

However, **as the template is laid out in the PDF**, the number `7.` is rendered immediately before the checkbox, making the checkbox structurally appear to be line 1 of Section 7. Subsequent items in Section 7 are presented indented under that number.

### Checkbox options for Third-Party Technology (as rendered)

Rendered using filled/empty Unicode glyphs rather than Markdown checklist syntax:

- `☒ None` (filled — selected in prior fill)
- `☐ See immediately below:` (empty)

### Additional blank line

Below the checkboxes, a long underscored blank appears:

`____________________________________`

Followed by the phrase: `Additional sheets attached.` (without a visible checkbox glyph before it in the extraction).

### Fillable elements

- Checkbox choice between `☒ None` and `☐ See immediately below:` (mutually exclusive)
- Free-form inline content after the blank line if "See immediately below" is chosen
- A second `Additional sheets attached.` annotation for attaching supplementary pages

### Template artifact / oddity — summary

- Section 7 **spans the page 2 / page 3 boundary** in layout terms (the visual grouping including the orphaned `Additional sheets attached.` checkbox from Section 6), even though its content is localized to page 3.
- The two disclosure sections (6 and 7) use **different checkbox rendering conventions** — Section 6 uses Markdown-style `- [x] / - [ ]`, Section 7 uses Unicode `☒ / ☐`. This is inconsistent template formatting preserved through extraction.
- The prior fill has `☒ None` selected for Section 7 (consistent with typical staff-augmentation SOWs that disclose no third-party technology).

---

## Section 8 — Approved Subcontractors

### Heading (as rendered)

`8. <u>Approved Subcontractors</u>:` — numbered, underlined, followed by a colon.

### What the section asks for

A list of subcontractors that will perform Services under the SOW, with the scope delegated to each.

### Lead-in verbatim

"The following subcontractors will be providing Services under this SOW. Company's approval of the list of subcontractors does not negate or waive any requirements and conditions regarding subcontractors set forth in the SOW."

### Fillable-field layout

Two parallel columns implemented in prose with non-breaking-space padding rather than as a table:

| Left column | Right column |
| :--- | :--- |
| `Subcontractor:` | `Statement of Services to be delegated to Subcontractor:` |
| `-------------------------------------------------` (blank line for name) | `-----------------------------------------------------------------------` (longer blank line for scope description) |

Only one row's worth of blanks is rendered. Additional subcontractors would need additional rows or attached sheets (no "Additional sheets attached" checkbox is provided for this section).

### Prior fill (Sarthak)

No subcontractors listed; both blanks empty.

### Fillable elements

- Subcontractor name (left blank)
- Statement of delegated Services (right blank)

---

## Execution / Signature Block

### Execution clause (above signature block)

Immediately after Section 8, a single sentence launches the signature block:

"Executed the latest date below by the authorized representatives of the parties for the SOW Effective Date."

This sentence is not numbered and is not part of Section 8; it functions as a standalone execution recital.

### Signature block layout

A two-column Markdown table, with Lam Research Corporation on the left and BayOne Solutions Inc. on the right. Each column has four fields:

| **Lam Research Corporation** | **BayOne Solutions Inc.** |
| :--- | :--- |
| By: | By: |
| Name: | Name: |
| Title: | Title: |
| Date: | Date: |

### Field semantics

- **By:** — signature line (handwritten or e-signed)
- **Name:** — printed name of the signer
- **Title:** — signer's job title
- **Date:** — date of signing (this is the "latest date below" referenced in the execution clause; the effective date remains the Feb 1, 2026 SOW Effective Date from the preamble)

### Prior fill (Sarthak)

All signature fields are blank in the template as received; the signed executed copy would fill these with actual signatures, names, titles, and dates.

### End of page 3

Below the signature block, page 3 ends with eight stacked `<br>` tags and the footer `Page 3 of 3`.

---

## Page / Footer Conventions

### Page footers

Every page ends with the plain-text footer `Page X of 3` (where X is 1, 2, or 3). No running headers beyond the repeated letterhead.

### Page counts

- **Page 1 of 3** — Title block, preamble, Sections 1, 2, 3 (Fee Schedule table)
- **Page 2 of 3** — Commercial/term block (Invoice schedule, payment terms reference, SOW Term, Total Amount NTE, payment-timing boilerplate), Section 4 (Expenses), Section 5 (Equipment), Section 6 (Background Technology Disclosure checkbox pair)
- **Page 3 of 3** — Section 7 (Third-Party Technology Disclosure) including the orphaned `Additional sheets attached.` checkbox that likely belongs to Section 6, Section 8 (Approved Subcontractors), Execution clause, Signature block

### Document identifiers (summary)

| Identifier | Value | Location |
| :--- | :--- | :--- |
| Document title | `STATEMENT OF WORK` | Page 1 title block |
| Template code | `BAYONE-SOW` | Page 1 title block |
| MSA identifier | `BAYON-MAS-0013142` | Page 1 title block + preamble |
| MSA effective date | `June 12, 2018` | Page 1 preamble |
| This SOW effective date | `Feb 1, 2026` (prior fill) | Page 1 preamble + quoted as "Statement of Work Effective Date" |
| SOW Term dates | `Feb 1, 2026` to `Mar 31, 2026` (prior fill) | Page 2 commercial block |
| Total Amount NTE (table) | `$11,840` (prior fill) | Page 1 Fee Schedule table |
| Total Amount NTE (callout) | `$11,840.00` (prior fill) | Page 2 commercial block |

### Cross-references to the MSA

The template defers to MSA clauses in three places:

1. **Preamble** — capitalized terms without inline definition take their meaning from the MSA.
2. **Section 2 (Acceptance Criteria), default line** — "Acceptance criteria shall be as set forth in Section 3 of the Agreement."
3. **Page 2 commercial block, payment terms line** — "Payment terms shall be subject to Section 4 of the MSA." (note this line says "MSA" rather than "Agreement", though both refer to the same document — BAYON-MAS-0013142).

### Formatting / style inventory

- Section headings 1, 2, 3 use `**<u>...</u>**` (bold + underline); sections 4, 5, 6 use `**...**` (bold only); section 8 uses `<u>...</u>` (underline only). Section 7's heading appears underlined but is partially obscured by the orphaned checkbox layout.
- Two different checkbox rendering conventions coexist: Markdown `- [x] / - [ ]` (Section 6) and Unicode `☒ / ☐` (Sections 2, 7, and the orphaned checkbox).
- Currency uses `$N,NNN` in tables and `$N,NNN.NN` in the Total Amount callout.
- Rate uses format `$N/hr.` with a trailing period.
- Blank fields are rendered as underscore runs of varying length (approximately 17 underscores for Equipment Type / Serial No., approximately 36 underscores for the Third-Party Technology free-form line, and much longer runs using non-breaking space padding plus dashes for the Subcontractor columns).

---

## Summary of Fillable vs. Fixed Elements

### Fillable elements (per section)

| Section | Fillable elements |
| :--- | :--- |
| Preamble | SOW Effective Date |
| 1. Services to be Provided | Project title (bold), scope narrative (free prose) |
| 2. Acceptance Criteria | Implicit choice among three prose options; `☐ Additional sheets attached.` checkbox; inline criteria text if expanded |
| 3. Fee Schedule | Each row of the five-column table (Role/Title, Quantity, Hours, Rate, Total) |
| Page 2 commercial block | Invoice schedule (free text); SOW Term commence date; SOW Term end date; Total Amount (Not to Exceed) |
| 4. Expenses | (none — fixed boilerplate) |
| 5. Equipment | Equipment Type; Serial No. (one pair of blanks) |
| 6. Background Technology Disclosure | Checkbox: `None` vs. `See immediately below`; inline list if expanded |
| 7. Third-Party Technology Disclosure | Checkbox: `☒ None` vs. `☐ See immediately below`; inline blank line; `Additional sheets attached.` annotation |
| 8. Approved Subcontractors | Subcontractor name; Statement of delegated Services |
| Signature block | By / Name / Title / Date for both Lam Research Corporation and BayOne Solutions Inc. |

### Fixed (boilerplate) elements

- Letterhead block (all pages)
- Title block on page 1 (`STATEMENT OF WORK`, `BAYONE-SOW`, subtitle, `[BAYON-MAS-0013142]`)
- Preamble prose (except the three inline bolded fields: effective date, Company, Contractor)
- Section 1 lead-in ("Contractor shall render such services...")
- Section 2 fallback line ("Acceptance criteria shall be as set forth in Section 3 of the Agreement.")
- Section 3 lead-in ("This project will be implemented on a time and material basis...")
- Page 2 payment-terms quotation ("Payment terms shall be subject to Section 4 of the MSA.")
- Page 2 parenthetical payment-timing note ("Company generally pays Contractors 30 days...")
- Section 4 expenses paragraph (entire)
- Section 5 equipment lead-in and trailing return clause
- Section 6 / 7 lead-in sentences ("The following is a complete list of all ...Technology:")
- Section 8 lead-in ("The following subcontractors will be providing Services...")
- Execution clause ("Executed the latest date below by the authorized representatives...")
- Page footers (`Page X of 3`)

---

## Notable Template Artifacts (Recap)

1. **Acceptance Criteria (Section 2) is presented as three stacked prose lines** rather than as selectable options, with only the `☐ Additional sheets attached.` line rendered as an explicit checkbox. The fallback ("Section 3 of the Agreement") appears to be the default state.

2. **Total Amount (Not to Exceed) appears twice** — once in the page 1 Fee Schedule table (without cents) and once as a standalone labeled line on page 2 (with cents). Both must agree.

3. **The Section 6 / Section 7 boundary is visually confused** — an `Additional sheets attached.` checkbox opens page 3 immediately beneath the `7.` number, though its content pairing likely belongs to Section 6 from the bottom of page 2. The two disclosure sections also use different checkbox glyph conventions.

4. **Equipment (Section 5) provides only one Equipment Type / Serial No. blank pair** with no mechanism (e.g., no "Additional sheets attached" checkbox) for listing multiple items.

5. **Approved Subcontractors (Section 8) uses non-breaking-space-padded prose columns** rather than a true table, and provides only one row of blanks.

6. **Heading formatting is inconsistent across sections** — Sections 1/2/3 are bold+underlined, Sections 4/5/6 are bold-only, Section 8 is underline-only. Section 7's heading is partially obscured by the orphaned Section-6 checkbox that landed at the top of page 3.

7. **Section 3's lead-in hard-codes a time-and-materials commercial structure** ("This project will be implemented on a time and material basis and following are the hourly rate and estimated costs."). The Fee Schedule table columns (Role / Quantity / Hours / Rate / Total NTE) mirror this T&M assumption. There is no visible template-provided alternate lead-in or table structure for fixed-fee, milestone-based, or outcome-based engagements.

8. **Minor typographical artifact in Section 4**: "a material increase or decrease in; the cost or time" contains a stray semicolon preserved from the source.

9. **The SOW defers three distinct subjects to the MSA**: capitalized-term definitions (preamble), acceptance criteria (Section 2 fallback / MSA Section 3), and payment terms (page 2 / MSA Section 4).
