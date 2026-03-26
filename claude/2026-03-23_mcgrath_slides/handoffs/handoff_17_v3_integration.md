# Handoff: V3 Deck Integration (New Slides + Content Updates)

## Purpose

A newer, better version of the McGrath proposal deck (v3) has been produced in parallel. You are integrating 10 slides from it: building 4 genuinely new slides, and working with Colin to update 6 existing slides with better v3 content.

**This session requires close collaboration with Colin. Do NOT make content changes automatically. Present options and get explicit approval for every change.**

## The V3 Source Deck
**Base path:** `claude/2026-03-19_pptx_extractor_skill/source/MGRC Managed Services Proposal v3 2/`
Each slide: `slide_NN/content.md`, `slide_NN/slide_NN.png`

## Detailed Mapping
Full analysis at: `claude/2026-03-23_mcgrath_slides/research/10_mgrc_v3_mapping.md`

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. 23+ slides are already built as HTML in `slides_output/`. This session integrates better content from a v3 PPTX that was developed in parallel.

### Previously Built (Read for Quality + Content Reference)
Browse `slides_output/` -- read all existing slides so you understand what's already built.

### Key Rules
1. **Read gold standard slides first:** `claude/2026-03-03_ariat_slides/foundational/slide_01_*.html`, `slide_02_*.html`, `slide_03_*.html`
2. **Colin is in the loop for EVERY content change.** Present v3 content alongside existing content and let him decide.
3. **No em dashes.** No contrastive framing. No colloquial language.
4. **No Playwright unless Colin explicitly asks.**
5. **Change ONLY what is approved.**
6. **Always read PNGs AND content.md.** PNGs are source of truth.
7. **Plan icons up front.**
8. **Proactively search `mcgrath/rfp_docs/`** for supporting detail.

### Design System
Standard BayOne design system. 16:10 canvas, max-width 1100px, purple gradient palette, Inter font, Font Awesome 6.5.1 icons. Match the visual quality of existing slides in `slides_output/`.

---

## PART 1: Build 4 New Slides

### Follow This Order for Part 1

### NEW: "Our Understanding" Section Divider (v3 Slide 4)

**Source:**
- Content: `MGRC Managed Services Proposal v3 2/slide_04/content.md`
- PNG: `MGRC Managed Services Proposal v3 2/slide_04/slide_04.png`

**What It Is:** Section divider titled "Our Understanding" with subtitle "McGrath RentCorp's NextGen Transformation & Support Requirements." Introduces the understanding/scope block.

**Design:** Match the style of our existing section divider (`slides_output/slide_04_section_divider.html`) which uses a dark purple gradient. Same visual treatment, different title.

**Placement:** Goes before the architecture and scope slides. This replaces our current "Our Solution" divider as the first section break, OR sits before it as a new section.

**Output:** `slides_output/slide_new_our_understanding_divider.html`

---

### NEW: NextGen Ecosystem Architecture (v3 Slide 5)

**Source:**
- Content: `MGRC Managed Services Proposal v3 2/slide_05/content.md`
- PNG: `MGRC Managed Services Proposal v3 2/slide_05/slide_05.png`

**What It Is:** Comprehensive architecture diagram. Header: "12-13 connected systems, 70+ integrations, Complete ecosystem overhaul." Shows:
- **Top layer:** Salesforce CRM/CPQ/CLM (280 users), Oracle Fusion ERP (Finance/SCM/Procurement/O2C), RecVue (Billing)
- **Integration layer:** MuleSoft (~32 APIs), OIC (~16 flows), ~5% retry/failure rate
- **Support layer:** Avalara, Customer Hub (PCI), NexSTAR (legacy), Snowflake, Oracle BI, Azure DevOps
- **Infrastructure:** 5 SQL Servers + 7 Oracle ATP + OCI + Azure | SOX/PCI/NIST | July 2026 MVP

**Design challenge:** This is an architecture diagram. Consider a layered card layout with connection indicators between layers. The gold standard card patterns can work if you think of each layer as a row of cards with flow arrows between rows. Or use a custom layout that shows the system hierarchy clearly.

**This is one of the most important new slides.** It shows McGrath that BayOne understands their entire technical landscape.

**Output:** `slides_output/slide_new_architecture.html`

---

### NEW: 13 Solution Towers (v3 Slide 6)

**Source:**
- Content: `MGRC Managed Services Proposal v3 2/slide_06/content.md`
- PNG: `MGRC Managed Services Proposal v3 2/slide_06/slide_06.png`

**What It Is:** Detailed table showing all 13 solution areas BayOne will cover:
1. Oracle Fusion (+FSM, EPBCS, ARCS) -- Bid
2. Salesforce (CRM, CPQ, CLM) -- Bid
3. Oracle Integration Cloud (OIC) -- Bid
4. MuleSoft -- Bid
5. RecVue -- Bid*
6. Oracle Cloud Infrastructure (OCI) -- Bid
7. Oracle BI Tools (FRS, OTBI, BIP) -- Bid
8. Snowflake / Rivery / SplashBI / Tableau -- Bid*
9. Avalara -- Bid
10. NexSTAR (Custom Legacy ERP) -- Bid*
11. SQL Server / Oracle ATP Databases -- Bid
12. Customer Hub (nopCommerce) -- Bid*
13. Azure DevOps -- Bid

Legend: Bid = Full coverage | Bid* = Specialist staffing refined during Phase 1

**Design:** Consider a numbered card grid or a styled table. Each tower should feel distinct and show its scope clearly. The Bid vs Bid* distinction matters.

**Output:** `slides_output/slide_new_13_towers.html`

---

### NEW: "Proposed Solution" Section Divider (v3 Slide 8)

**Source:**
- Content: `MGRC Managed Services Proposal v3 2/slide_08/content.md`
- PNG: `MGRC Managed Services Proposal v3 2/slide_08/slide_08.png`

**What It Is:** Section divider titled "Proposed Solution" with subtitle "Support Model, Governance Framework & Transition Approach."

**Design:** Same dark gradient treatment as our other section dividers.

**Output:** `slides_output/slide_new_proposed_solution_divider.html`

---

## PART 2: Content Updates (Colin Decides Each One)

**For each of the following, present the v3 content alongside the existing slide content and ask Colin what to keep, merge, or replace. Do these one at a time. Do NOT batch them.**

### Update 1: "43+" to "70+" Everywhere

**What:** All previously built slides reference "43+ integrations." The v3 deck uses "70+" and Colin has approved this change.

**Action:** Search all HTML files in `slides_output/` for "43" and update to "70+" where it refers to integration count. Present the list of files and specific changes for Colin to confirm before editing.

---

### Update 2: Exec Summary (v3 Slide 2 vs Our Versions A/B)

**v3 content highlights:**
- 5 embedded resources already at MGRC, zero-risk transition
- $300-500K KT savings eliminated
- 4 value pillars: Embedded Advantage, Governance-Led MSP, Post Go-Live Focus, Full Stack Coverage
- 3-year cost optimization (20% Y2, 27% Y3)

**Existing:** `slides_output/slide_02_exec_summary_version_a.html` and `version_b.html`

**Ask Colin:** Build a new version D from v3 content? Hybrid v3 claims with existing narrative framing? Replace entirely?

---

### Update 3: Scope Summary (v3 Slide 7 vs Our Slide 5)

**v3 additions over our existing:**
- 70+ integrations (vs 50+)
- Mentions FreshService as ticketing tool
- Expanded out-of-scope: adds Infrastructure/network operations, L0/L1 triage retained by McGrath
- SLA compliance timeline: "baselines established in Phase 1; compliance from Jan 2027"

**Existing:** `slides_output/slide_05_scope_summary.html`

**Ask Colin:** Update existing with v3 additions? Or does the new 13 Solution Towers slide make our scope summary redundant?

---

### Update 4: Transformation Journey (v3 Slide 9 vs Our Slide 6a)

**v3 additions:**
- New Today item: "Manual quarterly patch testing"
- New Tomorrow item: "Automated patch testing"

**Existing:** `slides_output/slide_06a_transformation.html`

**Ask Colin:** Add these two items to the existing slide?

---

### Update 5: KPI Metrics (v3 Slide 20 vs Our Slide 12)

**v3 differences:**
- Adds "Enhancement defect leakage" under Quality
- Adds "Schedule variance" under Time
- Explicit phased timeline: Phase 1 define, Phase 2 baseline, Jan 2027+ compliance

**Existing:** `slides_output/slide_12_kpi_metrics.html` (if built by Session B)

**Ask Colin:** Update with v3 additions?

---

### Update 6: Assumptions (v3 Slide 21 vs Our Cleanup Plan)

**v3 content:** Clean 10-point assumptions list. Includes:
- MuleSoft→OIC migration note (pricing reflects post-migration)
- COLA applicable per contract terms
- 3rd-party vendor coordination (Oracle, Salesforce, RecVue, Avalara)
- ±10% deviation triggers change request

**This solves our prerequisites/assumptions cleanup problem.** If Session E hasn't built slide 22 yet, we can use v3 slide 21 directly. If Session E already built it, compare and pick the better version.

**Ask Colin:** Use v3 assumptions as-is? Combine with prerequisites?

---

### Update 7: Risks (v3 Slide 22 vs Our Slides 18+19)

**v3 content:** 7 consolidated risks in one slide (vs our 8 across two). References "BayOne embedded at MGRC" and "rebadging critical resources with approval."

**Existing:** `slides_output/slide_18_risks_part1.html` and `slide_19_risks_part2.html` (if built by Session D)

**Ask Colin:** Replace two risk slides with one consolidated v3 version? Keep our two slides?

---

## Output Files

### New slides:
- `slides_output/slide_new_our_understanding_divider.html`
- `slides_output/slide_new_architecture.html`
- `slides_output/slide_new_13_towers.html`
- `slides_output/slide_new_proposed_solution_divider.html`

### Updated slides (pending Colin decisions):
- Various files in `slides_output/` -- changes applied only after Colin approves each one

## Write results handoff at `handoffs/handoff_17_results.md` when done.
