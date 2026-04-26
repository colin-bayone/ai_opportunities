# SOW Filling Instructions — Follow-Up #3: Collapse SOW-Specific Assumptions Subsection

**Engagement:** Lam Research IP Protection — Confidential Information Detection POC
**Status:** Third follow-up. Prior specs (original + followup + followup2) have already been executed by the Word Claude session. This document instructs only the additional changes from this turn. Do not re-do prior work.
**Spec author:** Singularity skill session, 2026-04-17

---

## Why This Change

The prior specs left two assumptions-related constructs in Section 1: the main **Assumptions** subsection (11 items inlined from the proposal and engagement pricing one-pager) and a separate **SOW-specific assumptions** subsection at the end with two items. On review, the two SOW-specific items are either redundant with the main Assumptions list or belong inside it. Keeping a second "SOW-specific" subsection creates duplication, invites reader confusion about which list governs, and weakens the document.

The fix is to consolidate: keep one Assumptions list of 12 items, drop the separate SOW-specific subsection.

**The two SOW-specific items, analyzed:**

- Item 1 ("Lam Research provides Contractor with all required access... and Lam Research SME availability prior to the engagement start date. The three-week period of performance does not begin until all access is in place.") is redundant. Its content is already covered by main Assumption #1 (access provision triggers the three-week period), Assumption #2 (SME availability), and Assumption #7 (Lam manages internal coordination for access). No information is lost by removing it.
- Item 2 ("Engagement start date shall be no earlier than the week of May 4, 2026, to allow time for access provisioning, equipment delivery, internal Lam Research approvals, and any legal or procurement actions arising from this SOW") is unique. It is not in the proposal or pricing one-pager. It must be preserved.

---

## What To Do

Two edits, both within Section 1 (Services to be Provided).

### Edit 1: Add Assumption #12 to the Main Assumptions List

**LOCATE** the main **Assumptions** subsection within Section 1. It currently contains 11 numbered items (where item #6 was updated in Follow-Up #2 to remove the "options" framing).

**APPEND** a new item #12 immediately after item #11. The new item reads:

> 12. The engagement start date shall be no earlier than the week of May 4, 2026, to allow time for access provisioning, equipment delivery, internal Lam Research approvals, and any legal or procurement actions arising from this SOW.

Formatting: Match the numbered-list styling of items 1 through 11. Ensure the numbered list properly continues (Word's auto-numbering should handle this; if manual numbering is in use, confirm #12 is correctly rendered).

After this edit, the main Assumptions list has exactly 12 items.

---

### Edit 2: Delete the SOW-Specific Assumptions Subsection

**LOCATE** the subsection currently titled **SOW-specific assumptions** (or a similar variant such as "SOW-Specific Assumptions"). It sits at or near the end of Section 1 and contains exactly two bullet items:

> SOW-specific assumptions:
>
> - Lam Research provides Contractor with all required access (environment, data, reference materials, equipment) and Lam Research SME availability prior to the engagement start date. The three-week period of performance does not begin until all access is in place.
> - Engagement start date shall be no earlier than the week of May 4, 2026, to allow time for access provisioning, equipment delivery, internal Lam Research approvals, and any legal or procurement actions arising from this SOW.

**DELETE** the entire subsection: the "SOW-specific assumptions:" header/lead-in, both bullet items, and any surrounding formatting that was exclusive to this subsection. Leave no residue (no stray colon, no empty bullet, no orphan header).

---

## What NOT To Change

- The main **Assumptions** subsection's items #1 through #11 remain as they are. Do not rewrite them, renumber them, or re-order them.
- All other Section 1 subsections (Success Criteria, Engagement Scope, Detailed Approach, Timeline, Deliverables, Execution Environment, Exclusions, Risk Factors) are unaffected.
- All other Sections of the SOW (Effective Date, Sections 2 through 8, Signature Block) are unaffected.
- Page footers, letterhead, page numbering, and overall document structure are unaffected except for any minor shift from removing the two-bullet subsection. Update page footer "Page X of N" if total page count changes.

---

## Verification Checks (Run Before Saving)

- [ ] The subsection titled "SOW-specific assumptions" (or any variant of that title) is no longer present anywhere in the document.
- [ ] Neither of the two bullet items from the deleted subsection appears anywhere else in the document, except that the May 4 earliest start content now appears as main Assumptions item #12 with the exact wording specified above.
- [ ] The main Assumptions list in Section 1 contains exactly 12 numbered items. Count them.
- [ ] Main Assumptions item #12 reads as the new replacement text ("The engagement start date shall be no earlier than the week of May 4, 2026, to allow time for access provisioning, equipment delivery, internal Lam Research approvals, and any legal or procurement actions arising from this SOW.") — matching the exact text specified in Edit 1.
- [ ] Main Assumptions items #1 through #11 are unchanged from before this follow-up.
- [ ] No empty headers, stray colons, orphan bullets, or blank paragraphs remain where the SOW-specific assumptions subsection used to be.
- [ ] All other subsections of Section 1 retain their content from prior specs.
- [ ] Page footer numbering reflects any change in total page count.
- [ ] Saved as a new file. Suggested filename: `BAYON-MAS-0013142_Lam_Research_IP_Detection_POC_v4_2026-04-17.docx`.

---

## End of Follow-Up #3 Instructions

When complete, report back to Colin with:

1. New filename.
2. Final page count.
3. Confirmation that the "SOW-specific assumptions" subsection is removed.
4. Confirmation that the main Assumptions list now contains 12 items with the correct wording for item #12.
5. Any deviations from this spec.
