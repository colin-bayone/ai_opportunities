# Handoff: Build Slides 23-28 (Why BayOne & Close)

## Purpose

You are building five slides that form the closing section of the McGrath RFP response deck. These reinforce BayOne's differentiators, show breadth, and close strong.

**Your slides:**
- **Slide 23: BayOne's Advantage** (old slide 37, use Ariat 06) -- Competitive differentiators
- **Slide 24: Service Offerings** (old slide 05, use Ariat 04) -- 8 service lines
- **Slide 25: Make Tech Purple** (old slide 09, use Ariat 09) -- Diversity initiative
- **Slide 27: Summary** (old slide 29) -- 3 investment pillars
- **Slide 28: Closing** (old slide 45, use Ariat 19) -- #TheFutureWorksHere

Three of these (23, 24, 25) are Ariat crossover slides. The Ariat versions are better but need McGrath tailoring ("80% there" rule). The Summary and Closing are McGrath-specific.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck as HTML slides. You are one of three parallel build sessions. The other two are building slides 7-10 (solution/delivery) and slides 11-17 (quality/KPIs/case studies).

### Previously Built (Read for Quality Reference)
- `slides_output/slide_01_title.html`
- `slides_output/slide_04_section_divider.html`
- `slides_output/slide_05_scope_summary.html`
- `slides_output/slide_06a_transformation.html`
- `slides_output/slide_06b_ai_strategy.html`

### Build Lessons (READ THESE)
- `planning/04_slide_build_feedback.md`
- `handoffs/handoff_07_results.md`
- `planning/05_exec_summary_build_report.md`

### Key Rules
1. **Read gold standard slides first:** `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_*.html`, `slide_03_*.html`
2. **Proactively search `mcgrath/rfp_docs/`** for supporting detail where relevant.
3. **Compare output to gold standard before presenting.**
4. **No em dashes, no contrastive framing, no colloquial language.**
5. **No Playwright unless Colin explicitly asks.**
6. **Change ONLY what is requested.**
7. **Plan icons up front.**
8. **Always read PNGs AND content.md.** PNGs are source of truth.
9. **Remove WIP markers and internal annotations** without being asked.

### The "80% There" Rule
Ariat slides provide the design, structure, and ~80% of the content. You MUST tailor them for McGrath's context. Don't just copy-paste. Frame things in terms of managed services relevance where appropriate.

### Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700). Headlines 24-28px, Body 11-12px
- **Icons:** Font Awesome 6.5.1 CDN
- **Structure:** slide-header / slide-content / slide-footer
- **Layouts:** `claude/2026-03-03_ariat_slides/page_layouts/layout_*.html`
- **Components:** `claude/2026-03-03_ariat_slides/ui_catalog/`

### Crossover Analysis (Detailed Recommendations)
Read: `claude/2026-03-23_mcgrath_slides/research/06_ariat_crossover_detailed.md`
This has specific content-to-pull guidance for each Ariat crossover pair.

---

## Slide 23: BayOne's Advantage (Old 37, Use Ariat 06)

### Source
**Primary (Ariat 06):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_06/slide_06.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_06/content.md`

**Secondary (McGrath 37, for "Security First" item):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_37/slide_37.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_37/content.md`

### Content (from crossover analysis)
6-item icon grid:
1. **Customer Obsessed** -- Dedicated team provides white glove service and customized solutions
2. **Efficient & Scalable** -- Global expertise, nimble offerings, innovative technology
3. **Value-Driven Solutions** -- Efficient processes, automation, lower overhead, optimize cost without compromising quality
4. **Global Coverage** -- Rightshoring solutions; 24/7 follow-the-sun model across Americas, LATAM, APAC
5. **Great Talent** -- Highly-skilled, motivated, results-oriented talent pool
6. **#MakeTechPurple** -- Empowers women in tech, fostering innovation and boosting ROI

**McGrath adaptation:** Consider adding "Security First" (from McGrath 37) if it fits the layout. McGrath's environment (Oracle Fusion, financial data, integrations) likely values security. Could replace one item or expand to 7.

**Output:** `slides_output/slide_23_bayone_advantage.html` (slide number 23)

---

## Slide 24: Service Offerings (Old 05, Use Ariat 04)

### Source
**Primary (Ariat 04):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_04/slide_04.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_04/content.md`

### Content (8 services with concise taglines)
1. **Artificial Intelligence** -- Unlock AI's potential to optimize, innovate, and transform your business
2. **Experience Design** -- Create seamless, user-centered experiences that inspire and drive results
3. **Application Modernization** -- Modernize legacy systems to boost efficiency, agility, and innovation
4. **Site Reliability Engineering** -- Ensure reliability, scalability, and performance with expert SRE solutions
5. **Tech & Biz Ops Support** -- Optimize, manage, and enhance your tech and business systems
6. **PMO Services** -- Align strategies, drive innovation, and execute projects with expert PMO solutions
7. **Quality Engineering** -- Elevate quality with precision, automation, and seamless user experiences
8. **Talent Solutions** -- Find top talent and build agile teams to power the future of your workforce

**Design:** 2x4 icon grid with gradient-colored circles and concise taglines.

**Output:** `slides_output/slide_24_service_offerings.html` (slide number 24)

---

## Slide 25: Make Tech Purple (Old 09, Use Ariat 09)

### Source
**Primary (Ariat 09):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_09/slide_09.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_09/content.md`

### Content
3-column layout:
1. **Community Cohorts** -- Provide women from underserved communities with months of technical training in AI and Software Engineering
2. **Girl Empowerment** -- Mentor middle/high school girls, offer apprenticeships, provide Girls Who Code scholarships
3. **BayOne Delivery** -- Female hires grew from 26% to 46% in four years via fair processes, "Rooney Rule," and AI-powered candidate sourcing

Include MakeTechPurple logo at bottom.

**Output:** `slides_output/slide_25_make_tech_purple.html` (slide number 25)

---

## Slide 27: Summary (Old Slide 29)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_29/slide_29.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_29/content.md`

### What It Is
Three investment/benefit pillars: (1) Vision (robust approach, knowledge management, talent retention), (2) BayOne Investment (shadow resources, transition funding, competitive pricing), (3) Productivity Benefits (multi-skilling, efficiency gains through AI). This is the penultimate slide, summing up the value proposition.

### Design Approach
Three-column or three-card layout. Each pillar gets a card with icon, title, and key points. Should feel like a confident summation. Consider using the `layout_quote_led.html` pattern or a clean 3-card horizontal layout.

**Output:** `slides_output/slide_27_summary.html` (slide number 27)

---

## Slide 28: Closing (Old 45, Use Ariat 19)

### Source
**Primary (Ariat 19):**
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_19/slide_19.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_19/content.md`

### What It Is
The final slide. Ariat version has a purple-tinted team photo across the top half, BayOne logo in the middle, and #TheFutureWorksHere at the bottom. Simple, professional.

### Design Note
The Ariat version uses a team photo which we don't have as an image file. Use the same approach as slide 01: substitute with a purple gradient visual treatment (abstract icons, gradient orbs, or similar). The slide 01 builder handled this well.

**Output:** `slides_output/slide_28_closing.html` (slide number 28)

---

## Output Files
- `slides_output/slide_23_bayone_advantage.html`
- `slides_output/slide_24_service_offerings.html`
- `slides_output/slide_25_make_tech_purple.html`
- `slides_output/slide_27_summary.html`
- `slides_output/slide_28_closing.html`

## Rules
All standard rules from Key Rules section. Additionally:
- You are one of three parallel sessions. Focus on YOUR slides.
- For Ariat crossover slides (23, 24, 25, 28): read the crossover analysis at `research/06_ariat_crossover_detailed.md` for specific content recommendations.
- Apply the "80% there" rule: Ariat content is the foundation, but tailor for McGrath.
- Write a results handoff when done at `handoffs/handoff_13_results.md`.
