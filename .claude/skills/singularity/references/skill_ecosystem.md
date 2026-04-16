# Skill Ecosystem and Integration

## Singularity's Role

Singularity is the **engagement orchestrator**. It owns the full lifecycle from raw source material through structured research to client-facing output. It does not need to do everything itself. It knows about sibling skills and invokes them when appropriate.

## Sibling Skills

### Skills Singularity Can Invoke

| Skill | What It Does | When Singularity Uses It |
|-------|-------------|--------------------------|
| `big4` | Polishes documents to Big Four consulting quality. Catches AI anti-patterns, tone issues, formatting violations. | After drafting any client-facing deliverable in `/<client_name>/<opportunity_name>/deliverables/`. Run before finalizing. |
| `pptx-extractor` | Extracts PowerPoint slides to markdown using Gemini Vision. Handles screenshot-heavy decks. | When the user provides a `.pptx` file as source material in `/<client_name>/<opportunity_name>/source/`. Extract content before processing into research docs. |
| `pdf-extractor` | Extracts PDF pages to markdown using Gemini Vision. Handles scanned and image-heavy PDFs. | When the user provides a `.pdf` file as source material in `/<client_name>/<opportunity_name>/source/`. Extract content before processing into research docs. |
| Slide skill (TBD) | Generates BayOne-branded HTML slide decks from content. | When the user needs a presentation created from research or deliverable content. Output goes to `/<client_name>/<opportunity_name>/presentations/`. |

### How Invocation Works

Singularity does not call these skills silently. When source material requires extraction or a deliverable needs polishing, the skill should:

1. Recognize the file type or workflow step
2. Tell the user: "This is a .pptx file. I can use the pptx-extractor skill to pull the content into markdown before processing. Want me to do that?"
3. Invoke the sibling skill
4. Take the output and continue the singularity workflow

For big4 specifically, the skill should offer to run it on any deliverable before the user sends it to a client. This is not automatic. Ask first.

### Skills That Singularity Replaces

| Skill | Disposition |
|-------|-------------|
| `sales-forge` | **Absorbed into singularity.** All of sales-forge's capabilities (context gathering, strategy development, deliverable creation, PDF export) are covered by singularity's workflow. Sales-forge's unique assets (proposal template, slide templates, html_to_pdf.py, slide format reference) are incorporated into singularity's assets. |

## Shared Company Context

### Location: `.claude/skills/singularity/references/`

Company-level context lives in `.claude/skills/singularity/references/`. Updates happen when the user provides new information.

### Key Files

| File | Purpose | Updated By |
|------|---------|-----------|
| `bayone_team.md` | BayOne team directory. Names, titles, roles, expertise, contact info. Living document that grows as the team changes. | Any skill or session when the user mentions team changes |

### `bayone_team.md` Structure

```markdown
# BayOne Solutions - Team Directory

**Last Updated:** <date>

---

## Leadership

### Rahul
- **Title:** President
- **Role:** Executive sponsor, client relationships, strategic direction
- **Engagement involvement:** Reviews proposals and pricing, relationship owner for key accounts

### Colin Moore
- **Title:** Director of AI
- **Role:** Technical lead, AI architecture, engagement delivery, sales engineering
- **Expertise:** Data science, AI engineering, full-stack development, Claude Code
- **Engagement involvement:** Leads discovery, architects solutions, reviews all deliverables

### Zahra
- **Title:** Director, Strategic Accounts
- **Role:** Sales leadership, account management, client development
- **Engagement involvement:** Initial outreach, relationship management, commercial terms

---

## Delivery

### Amit
- **Title:** Delivery Lead
- **Role:** Engagement delivery management, offshore team coordination
- **Engagement involvement:** Staffing, resource allocation, delivery oversight

### [Future team members added here as they join]

---

## Technical Team

### [Engineers, data scientists, etc. added as they join engagements]

---

## Notes

- This file is referenced by multiple skills (singularity, slide generation, etc.)
- Update it whenever team composition changes
- Do not include sensitive compensation data here (that belongs in pricing models)
```

### How Skills Reference Company Context

Any skill that needs company context reads from `.claude/skills/singularity/references/`:

```
Read .claude/skills/singularity/references/bayone_team.md for the current team directory.
```

Singularity references these when:
- Writing the org chart for an engagement (BayOne side of the org chart pulls from `.claude/skills/singularity/references/bayone_team.md`)
- Drafting deliverables that reference "BayOne will..." or "The BayOne team..."
- Populating cover pages with "Prepared By" metadata
- Building pricing models (team names and roles)

## Asset Consolidation from Sales-Forge

The following assets move from `.claude/skills/sales-forge/` into `.claude/skills/singularity/`:

| From Sales-Forge | To Singularity | Notes |
|-----------------|----------------|-------|
| `assets/templates/proposal-template.html` | `.claude/skills/singularity/templates/proposal_template.html` | The HTML shell with placeholder variables |
| `assets/templates/slide-cover-template.html` | Slide skill (TBD) | Moves to the slide generation skill, not singularity |
| `assets/templates/slide-content-template.html` | Slide skill (TBD) | Moves to the slide generation skill, not singularity |
| `references/bayone-design-spec.md` | `.claude/skills/singularity/references/bayone_design_spec.md` | Own copy, to be updated with gold standards |
| `references/slide-format.md` | Slide skill (TBD) | Moves to the slide generation skill |
| `scripts/html_to_pdf.py` | `.claude/skills/singularity/scripts/html_to_pdf.py` | PDF conversion utility. Also copy to slide skill. |

## Design System Update

The current `bayone_design_spec.md` is outdated. It does not reflect all the patterns established in the gold standard deliverables from the Lam Research engagement.

### Gold Standard References

The following files serve as the definitive examples of what BayOne deliverables should look like. They are included in `.claude/skills/singularity/gold_standards/deliverables/`:

| File | What It Demonstrates |
|------|---------------------|
| `problem_restatement.html` | Full cover page, numbered sections, highlight boxes, tables, workflow grids, two-column cards, footer, print styles |
| `information_request.html` | Priority tiers with badges, ask cards, call-to-action boxes, audience labels |
| `preliminary_approach.html` | Technical content presentation, architecture descriptions, enterprise tools framing |

### Design Spec: Updated to v2.0 (2026-03-28)

The design spec at `/home/cmoore/programming/cisco_projects/cicd/specs/bayone-design-spec.md` has been updated to v2.0 by a parallel Claude session. It is now comprehensive and covers all patterns from the gold standards.

**What was updated:**

- **4 corrections:** `.section-number` pill style, cover subtitle size, `.stat-value` size, `.stat-label` formatting
- **18 new components added:** Workflow grids, priority tiers, ask cards, CTA boxes, quarter cards, org charts, dynamics grids, phase meta, deliverable grids, summary tables, system grids, styled lists, team notes, idea cards, challenge items, deliverable items
- **3 existing components expanded:** Highlight box (list styles), cards (internal styles), h4 heading
- **5 structural additions:** Global reset, cover label conventions (thematic vs literal), cover variants, section numbering conventions, document type component conventions table
- **Print styles updated** to match gold standards
- **Quick reference reorganized** into categorized tables (Core, Content, Process/Timeline, Request/Priority, Specialized)

The spec in the skill at `.claude/skills/singularity/references/bayone_design_spec.md` should be a copy of this updated v2.0 file.
