# Design Spec Update: Handoff Document

**Purpose:** This document is a complete handoff for a new Claude session tasked with updating the BayOne Document Design System specification.

**Date:** 2026-03-28

---

## Your Mission

Update `/home/cmoore/programming/cisco_projects/cicd/specs/bayone-design-spec.md` to fully document every pattern, component, and convention used in BayOne's gold standard deliverables.

This is primarily an **append and correct** task. The existing spec is a good foundation but incomplete. Your job is to make it comprehensive by studying the gold standard HTML files and documenting every pattern they contain.

---

## Rules

1. **Do NOT rewrite from scratch.** The existing spec is the starting point. Add to it and correct it.
2. **Do NOT remove or change anything without user approval.** If you believe something in the current spec is wrong or outdated, flag it and ask. Do not silently change it.
3. **Do NOT make cosmetic or stylistic changes to the spec itself** unless directly relevant to documenting a pattern.
4. **Every addition must be grounded in a gold standard file.** Do not invent patterns. Document what exists.
5. **Cite which gold standard demonstrates each pattern** so the user can verify.

---

## Step 1: Read the Current Spec

Read the full design spec at:
```
/home/cmoore/programming/cisco_projects/cicd/specs/bayone-design-spec.md
```

Take notes on what it covers and what gaps you notice. Do not edit yet.

---

## Step 2: Study the Gold Standard Files

Read each file carefully. For each one, take notes on every CSS class, layout pattern, component type, and structural convention it uses. Pay attention to what the current spec does NOT document.

### Gold Standards (Tier 1 - Definitive)

These are the best examples of BayOne deliverables. They define what "correct" looks like.

| File | Type | Read It At |
|------|------|-----------|
| **POC Proposal (concise)** | Proposal | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/poc_proposal_v5.html` |
| **POC Proposal (detailed)** | Proposal (long form) | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-20_ui-conversion-discovery/poc_proposal_v5_detailed.html` |
| **Problem Restatement** | Understanding document | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-20_lam-research/deliverables/02_discovery_call_2026-03-12/problem_restatement.html` |
| **Information Request** | Request document | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-20_lam-research/deliverables/02_discovery_call_2026-03-12/information_request.html` |
| **Preliminary Approach** | Technical approach | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-20_lam-research/deliverables/02_discovery_call_2026-03-12/preliminary_approach.html` |

### Silver Standards (Tier 2 - Good Reference)

These are older but still demonstrate valid patterns. Use them to confirm patterns seen in the gold standards, but defer to gold when there is a conflict.

| File | Type | Read It At |
|------|------|-----------|
| **Resource Plan** | Planning document | `/home/cmoore/programming/cisco_projects/cicd/claude/2026-02-02_resource-planning/deliverables/resource_plan_for_cisco.html` |
| **EDW Framework** | Framework document | `/home/cmoore/programming/cisco_projects/cicd/claude/2025-02-25_big4_edw_framework/planning/03_edw_acceleration_framework_v2.html` |

---

## Step 3: Identify Gaps

After reading all files, compile a list of patterns that exist in the gold standards but are NOT documented in the current spec. Common gaps to look for:

### Component Patterns
- **Priority tiers** (`.priority-tier`, `.priority-badge`, `.priority-audience`) - used in information_request.html
- **Ask cards** (`.ask-card`) - used in information_request.html
- **Call-to-action boxes** (`.cta-box`) - used in information_request.html
- **Workflow grids** (`.workflow-grid`, `.workflow-step`, `.workflow-step-number`) - used in problem_restatement.html
- **Two-column card layouts** (`.two-col`, `.card`) - used across multiple docs
- **Stat cards and stat grids** - used in proposals
- **Phase cards with numbered progression** - used in proposals
- **Timeline components** - if present

### Structural Patterns
- **Cover page variants** (with/without subtitle, different meta item counts)
- **Section numbering** (PURPOSE vs 01, 02, 03...)
- **Lead paragraphs** (`.lead` class usage and when to use it)
- **Highlight box variants** (with lists, with bold labels, with plain text)
- **Table styling details** (header colors, alternating rows, border radius)
- **Footer variations**

### Print Styles
- **Cover page print behavior** (`page-break-after: always`, `height: 10in`)
- **Content flow options** (with vs without `page-break-inside: avoid`)
- **Print color adjustment** (`-webkit-print-color-adjust: exact`)
- **Font size reductions** for print

### Document Type Conventions
- **When to use which components** (e.g., priority tiers are for request documents, workflow grids are for process descriptions)
- **Cover page label conventions** (not the literal document type - e.g., "SECURE KNOWLEDGE ENABLEMENT" not "PROBLEM RESTATEMENT")
- **Standard section structures per document type**

---

## Step 4: Present Findings to User

Before editing the spec, present:

1. **What the spec currently covers** (brief summary)
2. **What is missing** (the gaps you identified, organized by category)
3. **What might need correction** (anything in the current spec that conflicts with the gold standards)
4. **Proposed additions** (what you plan to add, section by section)

Wait for user approval before making any changes.

---

## Step 5: Update the Spec

After user approval, update the spec. For each addition:

- Add it in the appropriate section (or create a new section if the category does not exist)
- Include the CSS for each component
- Include a usage example (HTML snippet)
- Note which gold standard file demonstrates it
- Follow the existing spec's formatting style

---

## Step 6: Verify

After updating, do a final pass:

1. Read the updated spec end to end
2. Confirm every component in every gold standard file is now documented
3. Confirm no existing content was removed without user approval
4. Present the final version to the user for review

---

## What NOT to Do

- Do not add components that do not exist in any gold standard file
- Do not change the brand colors (they are correct)
- Do not change the font family (Inter is correct)
- Do not reorganize the spec's existing structure unless the user asks
- Do not add emoji or decorative elements to the spec
- Do not generate new CSS patterns that are not grounded in existing files
