# Handoff: Build Slides 11-17 (Quality, KPIs, Proof Section)

## Purpose

You are building seven slides covering the end of the Delivery section and the entire Proof section of the McGrath RFP response deck.

**Your slides:**
- **Slide 11: Service Quality Audit Process** (old slide 23) -- Quality improvement cycle
- **Slide 12: Measurement By Metrics** (old slide 46) -- 10 KPIs table
- **Slide 13: Why BayOne?** (old slide 30) -- IT Ops expertise + Execution readiness
- **Slide 14: Case Study -- Oracle HCM Implementation** (old slide 31) -- Full case study
- **Slide 15: Case Study 1 -- Oracle Fusion HCM Managed Services** (old slide 32) -- 95.7% SLA
- **Slide 16: Case Study 2 -- Oracle ERP Reporting** (old slide 33) -- 40% manual effort reduction
- **Slide 17: Case Study 3 -- Oracle EBS Support** (old slide 34) -- 12+ year partnership

The case studies (14-17) share a structure. Build one well, then replicate the pattern for the remaining three.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck as HTML slides. You are one of three parallel build sessions. The other two are building slides 7-10 (solution/delivery) and slides 23-28 (closing section).

### Previously Built (Read for Quality Reference)
- `slides_output/slide_01_title.html`
- `slides_output/slide_04_section_divider.html`
- `slides_output/slide_05_scope_summary.html` -- Good card-based density reference
- `slides_output/slide_06a_transformation.html`
- `slides_output/slide_06b_ai_strategy.html`

### Build Lessons (READ THESE)
- `planning/04_slide_build_feedback.md`
- `handoffs/handoff_07_results.md`
- `planning/05_exec_summary_build_report.md`

### Key Rules
1. **Read gold standard slides first:** `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_*.html`, `slide_03_*.html`
2. **Proactively search `mcgrath/rfp_docs/`** for supporting detail.
3. **Compare output to gold standard before presenting.**
4. **No em dashes, no contrastive framing, no colloquial language.**
5. **No Playwright unless Colin explicitly asks.**
6. **Change ONLY what is requested.**
7. **Plan icons up front.** No duplicates within a slide.
8. **Always read PNGs AND content.md.** PNGs are source of truth.
9. **Remove WIP markers, internal annotations** without being asked.

### Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700). Headlines 24-28px, Body 11-12px
- **Icons:** Font Awesome 6.5.1 CDN
- **Structure:** slide-header / slide-content / slide-footer
- **Layouts:** `claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`
- **Components:** `claude/2026-03-03_ariat_slides/ui_catalog/`

---

## Slide 11: Service Quality Audit Process (Old Slide 23)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_23/slide_23.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_23/content.md`

### What It Is
Three sections: On-boarding phase, Steady State phase (with L0-L3 flowchart), and Value Adds (AI/automation). Shows a continuous quality improvement cycle: review -> gaps -> RCA -> update KB/process.

### Design Approach
Process flow slide. The chevron pattern from gold standard slide 03 could work for the phases. The key is showing the continuous improvement loop clearly.

**Output:** `slides_output/slide_11_quality_audit.html` (slide number 11)

---

## Slide 12: Measurement By Metrics (Old Slide 46)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_46/slide_46.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_46/content.md`

### What It Is
10 KPIs across categories: Incident Management (MTTR, case age, hops, backlog, FCR, automation %), Standard Processes (playbook adoption, knowledge repo), Problem Management (incidents eliminated), Customer Experience (CSAT). Structured as a table.

### Design Approach
Data-dense KPI slide. Consider `layout_two_column_detail_rows.html` or a card-per-category layout. The categories (Incident, Standard Processes, Problem, Customer) provide natural groupings. Make the metrics feel measurable and specific, not generic.

**Output:** `slides_output/slide_12_kpi_metrics.html` (slide number 12)

---

## Slide 13: Why BayOne? (Old Slide 30)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_30/slide_30.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_30/content.md`

### CRITICAL: The content.md was re-extracted but the PNG is still source of truth.
The PNG shows two sections: "IT Operations & Maintenance Service Expertise" (4 columns: prior Cisco experience, data/analytics projects, IB experts, experience with other customers) and "Execution Readiness" (3 columns: 100% readiness, CAM Academy, competitive pricing). Also has a red "Check with Neha" annotation.

### Design Approach
This slide opens the Proof section. Two clear content blocks. Consider a split or two-row layout with distinct visual treatment for each section. **Remove the "Check with Neha" annotation** (internal).

**Note:** Some content references Cisco (prior Cisco IB experience, CAM Academy). This content may need McGrath-tailoring. Flag anything Cisco-specific for Colin's review rather than changing it yourself.

**Output:** `slides_output/slide_13_why_bayone.html` (slide number 13)

---

## Slides 14-17: Case Studies

### Shared Design Approach
All four case studies should share a consistent card/layout pattern. Build slide 14 or 15 first as the template, get feedback, then replicate for the others. Each case study has: Business Scenario, Scope/Services/Technologies, Solution, and Benefits.

### Slide 14: Oracle Fusion HCM Implementation (Old Slide 31)

**Source:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_31/slide_31.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_31/content.md`

**CRITICAL:** Content.md was re-extracted. Read BOTH md and PNG.

**Key metrics:** Payroll processing 12 days to 3 days, data accuracy 98.6%, 78% self-service adoption, payroll errors 150-200 reduced to 8-12 per cycle. Oracle Soar methodology.

**Output:** `slides_output/slide_14_case_study_hcm_impl.html` (slide number 14)

### Slide 15: Oracle Fusion HCM Managed Services (Old Slide 32)

**Source:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_32/slide_32.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_32/content.md`

**Key metrics:** 95.7% SLA compliance, 100% P1 adherence, zero payroll failures, 99.8% uptime, 87% CSAT.

**Output:** `slides_output/slide_15_case_study_hcm_managed.html` (slide number 15)

### Slide 16: Oracle ERP Reporting (Old Slide 33)

**Source:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_33/slide_33.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_33/content.md`

**Key metrics:** 25+ BIP reports, 40% manual effort reduction, automated reporting across business units.

**Output:** `slides_output/slide_16_case_study_erp_reporting.html` (slide number 16)

### Slide 17: Oracle EBS Support (Old Slide 34)

**Source:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_34/slide_34.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_34/content.md`

**Key metrics:** 12+ year partnership, M&A data migration, export compliance.

**Output:** `slides_output/slide_17_case_study_ebs_support.html` (slide number 17)

---

## Output Files
- `slides_output/slide_11_quality_audit.html`
- `slides_output/slide_12_kpi_metrics.html`
- `slides_output/slide_13_why_bayone.html`
- `slides_output/slide_14_case_study_hcm_impl.html`
- `slides_output/slide_15_case_study_hcm_managed.html`
- `slides_output/slide_16_case_study_erp_reporting.html`
- `slides_output/slide_17_case_study_ebs_support.html`

## Rules
All standard rules from Key Rules section. Additionally:
- You are one of three parallel sessions. Focus on YOUR slides.
- Build one case study as the template, get feedback, replicate for the rest.
- Flag Cisco-specific content in slide 13 for Colin's review.
- Write a results handoff when done at `handoffs/handoff_12_results.md`.
