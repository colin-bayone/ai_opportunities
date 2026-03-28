# Kickoff: Sample Profile Slides (4 slides)

## Copy-paste the prompt below into a new Claude session

---

You are reformatting four sample profile slides for a McGrath RFP response deck. These are simple, text-heavy slides that need a clean, professional look in the BayOne design system. Retain ALL text exactly as written. Do not cut, summarize, or modify any content.

Each slide has the same structure: a title ("Sample Profiles - [Role]"), a summary paragraph with bold keywords, and a "Core Competencies" bulleted list.

## Source Slides

All at: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/`

| Slide | Title | Content File | PNG |
|-------|-------|-------------|-----|
| 40 | Oracle SCM Functional Lead (24+ years) | `slide_40/content.md` | `slide_40/slide_40.png` |
| 41 | Oracle Fusion Financials (11+ years) | `slide_41/content.md` | `slide_41/slide_41.png` |
| 42 | Salesforce Developer / CPQ Specialist (12+ years) | `slide_42/content.md` | `slide_42/slide_42.png` |
| 43 | MuleSoft Technical Lead (13+ years) | `slide_43/content.md` | `slide_43/slide_43.png` |

Read ALL four content.md files AND their PNGs before building.

## Design Approach

These are dense text slides. The goal is NOT to add visual complexity. The goal is to make dense text readable, professional, and consistent with the rest of the deck. Think clean typography, clear hierarchy, good spacing.

**Suggested layout per slide:**
- Title area: "Sample Profiles" as section label, role name as heading
- Summary: The paragraph text with bold keywords preserved. Could be in a slightly tinted card or just clean text with good line height.
- Core Competencies: Bulleted list with bold category labels. Consider a subtle left-accent bar or icon per bullet to break up the wall of text. A two-column layout for the competencies could help if there are 8+ bullets.

**Key design principles:**
- These should all look like siblings. Same layout, same spacing, same typography. Only the content changes.
- Don't over-design. A clean, readable profile is better than a flashy one with tiny text.
- Font sizes should be large enough to read comfortably. The originals cram everything in. Give the text room to breathe, even if it means the slide feels less dense.
- Use the purple accent system sparingly (accent bars, category label colors) but consistently.

## Design References

Read before building:
- Gold standard slides: `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html` (for card patterns and typography)
- Previously approved slides: browse `claude/2026-03-23_mcgrath_slides/slides_output/` -- especially `slide_05_scope_summary.html` for how dense content is handled with cards
- Build feedback: `claude/2026-03-23_mcgrath_slides/planning/04_slide_build_feedback.md`

## Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700)
- **Icons:** Font Awesome 6.5.1 if needed, but keep it simple
- **No em dashes.** No contrastive framing.
- **No Playwright unless Colin explicitly asks.**
- **Do NOT modify any text content.** Retain everything exactly as written in the source.

## Output
- `slides_output/slide_profile_oracle_scm.html`
- `slides_output/slide_profile_oracle_financials.html`
- `slides_output/slide_profile_salesforce.html`
- `slides_output/slide_profile_mulesoft.html`

Build one first, show the user, then replicate the pattern for the other three. When complete, tell the user what you built.
