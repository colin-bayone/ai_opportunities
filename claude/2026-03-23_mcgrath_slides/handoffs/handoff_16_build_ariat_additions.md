# Handoff: Build 3 New Ariat Addition Slides

## Purpose

You are building three NEW slides being added to the McGrath deck from the Ariat source deck. These don't replace existing McGrath slides -- they fill gaps identified during research.

**Your slides:**
- **NEW: Partnership Models** (from Ariat slide 05) -- 4 engagement types
- **NEW: Enterprise AI Solutions** (from Ariat slide 11) -- AI across HR/Finance/Legal/Marketing. HAS HTML GOLD STANDARD.
- **NEW: Quality Engineering** (from Ariat slide 12) -- 6 AI-powered QE capabilities. HAS HTML GOLD STANDARD.

### The "80% There" Rule
All three slides use Ariat content as the foundation but MUST be tailored for McGrath's managed services context. Don't just copy-paste. Frame capabilities in terms of what they mean for McGrath's Oracle Fusion, Salesforce, MuleSoft environment.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. You are one of three parallel sessions in the final build wave. Others are building slides 18-20 (risks/asks) and slides 21-22 (commercial/prerequisites).

### Previously Built
Browse `slides_output/` -- 20+ completed slides. Read especially:
- `slide_06b_ai_strategy.html` -- The AI strategy slide, same visual language for the AI additions
- `slide_05_scope_summary.html` -- Good card density reference

### Key Rules
1. **Read gold standard slides first** -- especially slides 02 and 03, which ARE the templates for Enterprise AI and Quality Engineering
2. **Proactively search `mcgrath/rfp_docs/`** for McGrath-specific detail to weave in
3. **No em dashes.** No contrastive framing ("not X"). No colloquial language.
4. **No Playwright unless Colin explicitly asks.**
5. **Plan icons up front.** No duplicates within a slide.
6. **Compare to gold standard before presenting.**

### Crossover Analysis
Read: `claude/2026-03-23_mcgrath_slides/research/06_ariat_crossover_detailed.md`
See sections on Ariat 05, 11, 12 for specific content recommendations and McGrath adaptation guidance.

### Design System
Standard BayOne design system. 16:10 canvas, max-width 1100px, purple gradient palette, Inter font, Font Awesome icons.

---

## NEW Slide: Partnership Models (From Ariat 05)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_05/slide_05.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_05/content.md`

### Content (4 engagement models)
1. **Managed Services** -- End-to-end service delivery with SLAs, billed as a fixed monthly fee
2. **Time & Material (T&M)** -- Flexible engagement where billing is based on actual hours worked
3. **Fixed Capacity** -- Pre-allocated team at a fixed cost, ensuring consistent resource availability
4. **Managed Projects** -- Fixed-price delivery with defined scope, budget, and milestones

### McGrath Tailoring
- Frame in context of what McGrath is buying (managed services is the primary model)
- Could highlight Managed Services as the recommended model for this engagement
- The other models show flexibility for future work

### Placement
This goes in the closing section, between Service Offerings and Make Tech Purple. Exact slide number TBD by orchestrator.

**Output:** `slides_output/slide_new_partnership_models.html`

---

## NEW Slide: Enterprise AI Solutions (From Ariat 11)

### Source
**PRIMARY: HTML Gold Standard**
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_02_enterprise_ai_solutions.html`

**Ariat 11 extract:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_11/slide_11.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_11/content.md`

### Content (AI across 4 business functions)
1. **Human Resources** -- Recruiting Automation, Onboarding Workflows, Policy Q&A Assistants, Workforce Analytics
2. **Finance** -- Expense Processing, Invoice Automation, Financial Reporting, Forecasting & Anomaly Detection
3. **Legal** -- Contract Review, Contract Lifecycle Management, Compliance Monitoring, Legal Knowledge Search
4. **Marketing** -- Content Generation, Personalization Engines, Campaign Automation, Marketing Analytics

### McGrath Tailoring
- Frame capabilities for McGrath's operational context
- Finance is highly relevant (Oracle Fusion ERP, Avalara tax, RecVue billing)
- HR is relevant (Oracle Fusion HCM is a key module)
- Legal/Marketing may need lighter tailoring
- This follows the AI Strategy slide (6b) -- position as "vertical applications" of the horizontal AI capabilities

### Placement
Goes in Section 2 (The Solution), after the AI Strategy slide. Exact position TBD.

**Output:** `slides_output/slide_new_enterprise_ai.html`

---

## NEW Slide: Quality Engineering (From Ariat 12)

### Source
**PRIMARY: HTML Gold Standard**
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_03_quality_engineering.html`

**Ariat 12 extract:**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_12/slide_12.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_12/content.md`

### Content (6 AI-powered QE capabilities)
1. **Test Case Clustering** -- Group similar tests by structure and dependencies
2. **Intelligent Routing** -- Governance-driven playbook for routing decisions
3. **Root Cause Analysis** -- Failure correlation distinguishing primary from cascading symptoms
4. **Agentic Diagnosis** -- AI deep dives into codebase to diagnose and troubleshoot
5. **Visibility Dashboard** -- Single pane of glass across build and deployment stack
6. **Automated Testing** -- Playwright UI/UX testing with coverage tracking and regression analysis

### McGrath Tailoring
- Frame for McGrath's quarterly Oracle Fusion patches (regression testing is critical)
- Integration troubleshooting across 50+ integrations benefits from root cause analysis
- Visibility dashboard relevant for monitoring MuleSoft/OIC integration health
- Test clustering relevant for Oracle Fusion quarterly release testing

### Placement
Goes in Section 2, after the Enterprise AI Solutions slide. Creates a 3-slide AI showcase: Strategy > Solutions > Quality Engineering.

**Output:** `slides_output/slide_new_quality_engineering.html`

---

## Output Files
- `slides_output/slide_new_partnership_models.html`
- `slides_output/slide_new_enterprise_ai.html`
- `slides_output/slide_new_quality_engineering.html`

Write a results handoff at `handoffs/handoff_16_results.md` when done.
