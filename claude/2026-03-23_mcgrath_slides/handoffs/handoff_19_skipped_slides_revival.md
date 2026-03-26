# Handoff: Revived Skipped Slides + Updated Case Studies + Commercials

## Purpose

You are building slides from the latest PPTX version of the McGrath deck. This includes:

1. **ONE new combined slide:** Location Footprint + Proposed Coverage, reimagined as a unified global coverage story
2. **Updated Commercials slide** (slide 29 from latest PPTX)
3. **Four updated Case Studies** (slides 34-37 from latest PPTX) -- these may replace or update existing HTML versions

**The combined slide (item 1) is the creative challenge. The rest are build-from-source tasks.**

## Source Deck
**Base path:** `claude/2026-03-19_pptx_extractor_skill/source/WIP_PC_Managed_Services_Support_Proposal_0322 2/`

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. 25+ slides are already built as HTML. The Location Footprint and Proposed Coverage slides were originally SKIP (flagged as bad). Colin now wants them revived and combined into one beautiful slide.

### Why These Were Originally Skipped
Read the autopsy report for context on what was wrong with the originals:
`claude/2026-03-23_mcgrath_slides/research/05_bad_slide_autopsy.md`

- **Location Footprint (old slide 06):** "Generic filler. Every staffing company has a 'look how global we are' map slide." Reinforced staffing perception.
- **Proposed Coverage (old slide 19):** "Cramped and overloaded. Two visualizations jammed onto one slide. Incomplete offshore roles. Standard onshore/offshore split."

The key insight: individually these slides are generic filler. COMBINED with a clear purpose ("here's our global team and exactly when they're available for McGrath"), they tell a useful story.

### Previously Built
Browse `slides_output/` for quality and design consistency reference.

### Key Rules
1. **Read gold standard slides first**
2. **No em dashes.** No contrastive framing. No colloquial language.
3. **No Playwright unless Colin explicitly asks.**
4. **Change ONLY what is approved.** For the combined slide, present your design concept and ask Colin before finalizing.
5. **Always read PNGs AND content.md.**
6. **Plan icons up front.**
7. **Pricing is HANDS OFF.** Build commercials slide faithfully.

### Design System
Standard BayOne: 16:10 canvas, max-width 1100px, purple gradient palette, Inter font, Font Awesome 6.5.1.

---

## SLIDE A: Combined Global Coverage (Location + Coverage) -- THE CREATIVE CHALLENGE

### Source Material

**Location Footprint (latest PPTX slide 5):**
- Content: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_05/content.md`
- PNG: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_05/slide_05.png`

**Proposed Coverage (latest PPTX slide 18):**
- Content: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_18/content.md`
- PNG: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_18/slide_18.png`

### Content to Combine

**From Location (slide 5):**
- North America: On and nearshore model, English/Spanish/Portuguese
- LATAM: Nearshore model, BCP strategies
- APJC (India): Support hub, offshoring, multiple languages
- Also: USA, Canada, Philippines, Costa Rica, India locations

**From Coverage (slide 18):**
- India Team: 8PM-5AM PST on-call
- US Team: 5AM-5PM PST primary, 5PM-8PM PST on-call
- Onsite team (Functional SMEs): Critical incidents, user collaboration, governance
- Offshore team (Technical Support Engineers): Ticket resolution, documentation, monitoring
- Key stat: 100% governance/SMEs/engagement during 5am-5pm PST, 80% engineers during same window

### The Reimagined Purpose
This is NOT a "look how global we are" slide (that's what killed the original). This is a **"here's how we guarantee McGrath 24/7 coverage"** slide. The locations are relevant BECAUSE they enable the coverage model. The coverage schedule is compelling BECAUSE you can see where the teams are.

Design concept directions (not prescriptive -- bring your creativity):
- Left: simplified region indicators (not a generic world map). Right: coverage timeline showing who's on when
- Or: a horizontal timeline across the top with coverage blocks, team cards below showing locations + roles
- Or: a split layout -- "Your Daytime Team" (US, onsite SMEs) and "Your Overnight Team" (India, offshore engineers) with coverage hours for each

**The anti-pattern to avoid:** Don't make this look like a staffing company's global map. Make it look like a purpose-built coverage model for McGrath's specific needs.

**Present your concept to Colin before building the full slide.** Describe the layout and ask for feedback.

**Output:** `slides_output/slide_new_global_coverage.html`

---

## SLIDE B: Managed Service Commercials (Latest PPTX Slide 29)

### Source
- Content: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_29/content.md`
- PNG: `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_29/slide_29.png`

### What It Is
Pricing breakdown: Phase 1 $738,400, Year 1 $4,867,200, Year 2 $3,889,600 (20% savings), Year 3 $2,828,800 (27% savings). Total: $12,344,800. Plus key callouts.

### Rules
- **HANDS OFF.** Build the visual design, preserve ALL pricing content exactly as written.
- Do not modify, round, reformat, or annotate any numbers.
- Check if Session E already built `slide_21_commercials.html`. If so, compare the content -- if identical, this may be unnecessary. If the latest version has different numbers or callouts, build this as a replacement.

**Output:** `slides_output/slide_new_commercials.html` (or update existing if content differs)

---

## SLIDES C-F: Four Case Studies (Latest PPTX Slides 34-37)

### Why Rebuild These
Session B already built case study slides (14-17) from the original PPTX. The latest version may have updated content. Compare and build replacements if the content is materially better.

### Slide 34: Oracle Fusion HCM Implementation
**Source:** `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_34/`
**Existing:** `slides_output/slide_14_case_study_hcm_impl.html`
**Key content:** Oracle Soar methodology, payroll 12 days to 3 days, 98.6% accuracy, 78% self-service adoption

### Slide 35: Oracle Fusion HCM Managed Services
**Source:** `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_35/`
**Existing:** `slides_output/slide_15_case_study_hcm_managed.html`
**Key content:** 95.7% SLA, 100% P1, zero payroll failures, 99.8% uptime, 87% CSAT. NEW: payroll processing 4.5 hrs to 1.8 hrs

### Slide 36: Oracle Fusion ERP Reporting
**Source:** `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_36/`
**Existing:** `slides_output/slide_16_case_study_erp_reporting.html`
**Key content:** 25+ BIP reports, 40% manual reduction, technical architecture flow

### Slide 37: Oracle EBS Support
**Source:** `WIP_PC_Managed_Services_Support_Proposal_0322 2/slide_37/`
**Existing:** `slides_output/slide_17_case_study_ebs_support.html`
**Key content:** 12+ year partnership, 30+ global sites, M&A migrations, export compliance

### Approach for All Four
1. Read the latest PPTX content AND the existing HTML slide
2. Compare content side-by-side
3. If the latest version has materially better/more content, rebuild from the latest
4. If they're essentially identical, keep the existing HTML
5. **Present your comparison to Colin** for each case study and let him decide whether to rebuild

**Outputs:** `slides_output/slide_new_case_study_34.html` through `slide_new_case_study_37.html` (only if rebuilding)

---

## Output Files
- `slides_output/slide_new_global_coverage.html` (the combined slide -- always build this)
- `slides_output/slide_new_commercials.html` (if content differs from existing)
- `slides_output/slide_new_case_study_34.html` through `37.html` (only if rebuilding)

## Write results handoff at `handoffs/handoff_19_results.md` when done.
