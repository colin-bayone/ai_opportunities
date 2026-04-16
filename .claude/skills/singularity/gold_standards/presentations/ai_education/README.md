# Gold Standard: AI Education Presentation

**Source:** Masterminds AI education deck
**Created:** 2026-03-31
**Purpose:** Gold standard for AI education and awareness presentations. A complete 25-slide deck covering AI fundamentals, failure modes, business applications, agentic AI, compliance, and practical guidance. Designed for non-technical executive audiences.

## Structure

The deck is organized into 6 sections with a prefix naming convention (`s0_` through `s6_`):

| Section | Slides | Topic |
|---------|--------|-------|
| s0 | `s0_00_title.html`, `s0_00_toc.html`, `s0_profile.html` | Opening: title, table of contents, presenter profile |
| s1 | `s1_01` through `s1_07` (7 slides) | What AI Actually Is: three branches, ML, computer vision, generative AI, ground truth, failure modes |
| s2 | `s2_01` through `s2_04` (4 slides) | Making AI Work: problem framing, 70/30 rule, what works, AI audit |
| s3 | `s3_01` through `s3_03` (3 slides) | Agentic AI: what it is, why it's not scary, what's possible today |
| s4 | `s4_01`, `s4_02` (2 slides) | Jobs and AI: replacement question, cost of waiting |
| s5 | `s5_01` through `s5_05` (5 slides) | Practical Guidance: compliance/PII, vendor pitch filtering, myth busting, business applications, getting started |
| s6 | `s6_01_closing.html` | Closing / Q&A |

## Resources

The `resources/` subfolder contains images referenced by the slides (logos, diagrams, photos, illustrations). These must stay alongside the HTML files for the slides to render correctly.

## Color Palette

This deck uses a **blue** color scheme (not BayOne purple). Variables: `--blue-darkest`, `--blue-dark`, `--blue-mid`, `--blue-bright`, `--blue-accent`, `--steel-light`, `--steel-glow`.

## Layout Patterns Demonstrated

This deck is the source for most of the layout examples in `layout_examples/`. Unique layouts include: dark full-bleed title, agenda card row, split panel profile, split panel concept, three-column cards, card grid with takeaway bar, and dark closing.

## How to Use

When building an AI education or awareness presentation, read through this deck to see how complex technical topics are broken down for non-technical audiences. Pay attention to the section flow, the progressive depth (simple concepts first, practical guidance last), and the use of concrete examples over abstract descriptions.
