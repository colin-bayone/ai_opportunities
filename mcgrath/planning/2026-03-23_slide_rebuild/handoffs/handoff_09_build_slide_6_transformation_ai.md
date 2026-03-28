# Handoff: Build Slide 6a + 6b (Transformation Journey + AI Strategy)

## Purpose

You are building the CENTERPIECE of the McGrath RFP response deck -- two connected slides that tell one story:

- **Slide 6a: Transformation Journey** -- McGrath's Today vs Tomorrow. Sets up the challenge and the vision.
- **Slide 6b: AI Strategy and Innovation** -- How BayOne's AI capabilities deliver the transformation. The differentiator.

These are the most important slides in the deck. Colin (Director of AI) personally owns this content. The AI story is BayOne's single biggest differentiator for this engagement -- the transcripts say: *"The AI playbook is huge because that's one of the things they're looking at very carefully and that's our strength."*

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. McGrath is undergoing a massive NextGen transformation -- migrating from legacy systems (Nexstar) to Oracle Fusion, with 43+ integrations, Salesforce CPQ, MuleSoft middleware, and more. BayOne's pitch is that AI-driven operations should be the FOUNDATION of managed services, not an afterthought.

### What Came Before
- Slides 1, 4, 5 are built and approved. Read them for quality reference:
  - `slides_output/slide_01_title.html`
  - `slides_output/slide_04_section_divider.html`
  - `slides_output/slide_05_scope_summary.html`
- Build feedback from sessions 1 and 2: `planning/04_slide_build_feedback.md` and `handoffs/handoff_07_results.md`

### Who You Can Ask
Tell the user if you have questions. This is Colin's slide -- he will want to be closely involved.

## Design System

### The Gold Standard (READ FIRST -- especially slide 01)
The AI Strategy gold standard is THE reference for slide 6b:
- **`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`** -- THIS IS YOUR PRIMARY REFERENCE for slide 6b
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_02_enterprise_ai_solutions.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_03_quality_engineering.html`

### Page Layout Templates
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/page_layouts/`

For slide 6a (Transformation), consider:
- `layout_problem_solution.html` -- Top = Today problems, Bottom = Tomorrow outcomes
- `layout_split_screen.html` -- Left = Today, Right = Tomorrow
- `layout_timeline_journey.html` -- 3 phases: Today -> Transformation -> Tomorrow

For slide 6b (AI Strategy), the gold standard HTML IS the layout. Replicate its card-based grid approach.

### UI Component Library
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/ui_catalog/`

### Core Design Rules
- **Canvas:** 16:10, max-width 1100px, white-to-light-purple gradient background, border-radius 12px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`. Neutrals: `#0f172a`, `#334155`, `#64748b`, `#e2e8f0`
- **Typography:** Inter (300-700). Headlines 24-28px, Lead 12-15px, Body 11-12px, Labels 10-11px uppercase
- **Icons:** Font Awesome 6.5.1 CDN. Icon boxes 36-48px with gradient backgrounds
- **Standard structure:** slide-header / slide-content / slide-footer
- **No em dashes in regular prose.** Use "with," commas, or other natural phrasing.

---

## Slide 6a: Transformation Journey

### The Story This Slide Tells
"McGrath, we understand your NextGen transformation. Here's where you are today, and here's where you're headed. The gap between these two states is what our managed services engagement addresses."

### Source Material

**Original McGrath slide 14:**
- PNG: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_14/slide_14.png`
- Content: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_14/content.md`

**RFP context (search these for McGrath-specific detail):**
- `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/architecture.md`
- `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/specific_requirements.csv`
- `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/rfp_overview.csv`

### Content Framework

**Title:** "Transformation Journey" (keep the original title -- it works)

**Lead text:** "NextGen is not just an Oracle Fusion migration -- it's a complete ecosystem overhaul spanning front-end CRM, back-end ERP, billing, tax, customer portal, and massive integration layer changes."

**Today State (5 pain points from the original, tailor to McGrath):**
- Customized environment
- Multiple integration layers
- Complex systems and processes
- Limited self-serve capabilities
- Limited scalability

**Transformation Levers (the bridge):**
- Simplify and Streamline
- Standardize
- Automate

**Tomorrow State (5 outcomes, tailor to McGrath):**
- Reduced total cost of ownership
- Industry standard processes
- Reduced cycle time with no-touch support
- Enriched customer self-service
- Faster time to market for new business

### What to Do
- Keep the Today -> Tomorrow narrative arc. It's a good concept.
- Make it McGrath-specific. Use parallel explore agents to search the RFP docs and architecture doc for specific systems, pain points, and goals. Don't just repeat generic bullets -- ground them in McGrath's actual environment (Oracle Fusion, Nexstar migration, MuleSoft integrations, Salesforce CPQ).
- The visual design should feel like a journey -- left-to-right flow, or top-to-bottom transformation.
- Remove the WIP marker.

### What NOT to Do
- Don't leave it generic. The original bullets could apply to any company. Make them McGrath's bullets.
- Don't include pricing or capacity numbers.

### Slide Number
06a (or 06 if you use one file)

---

## Slide 6b: AI Strategy and Innovation

### The Story This Slide Tells
"Here's HOW we get you from Today to Tomorrow. AI-driven operations across five domains. This is what makes BayOne different from every other managed services vendor."

This slide directly follows 6a. The evaluator should think: "Okay, I see the vision (6a). Now show me the engine (6b)."

### Source Material

**PRIMARY: Ariat slide 10 + HTML Gold Standard**
- Gold standard HTML: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`
- Ariat 10 extract: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_10/content.md`
- Ariat 10 PNG: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/BayOne-Overview-Ariat-GCC---Feb-2026_COLIN_EDITS/slide_10/slide_10.png`

**DISCARD: McGrath slide 24**
The original McGrath slide 24 is Cisco-specific content (InstallBase, MACDs, SiteID, SN Alignment). It has NOTHING to do with McGrath. Do not use any content from it. The Ariat version replaces it entirely.

**Crossover analysis (detailed comparison):**
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/06_ariat_crossover_detailed.md` -- see "Pair 7: AI Enablement" section

**Transcript analysis (strategic context):**
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/04_combined_transcript_analysis.md`

### Content Framework (from Ariat 10 -- the "80% there" content)

**Title:** "AI Strategy and Innovation"
**Subtitle:** "Comprehensive AI capabilities across development, automation, data, and operations"

**Five AI capability domains (from Ariat, each with 3-4 items):**

1. **Developer Productivity**
   - AI Copilots trained on your codebase with context-aware suggestions
   - Intelligent Code Review that catches architectural issues, not just syntax errors
   - CI/CD Pipeline Intelligence that diagnoses failures and monitors branch health

2. **Enterprise Automation**
   - Intelligent Process Automation that handles exceptions and adapts to changing inputs
   - Enterprise App Integrations connecting Salesforce, ServiceNow, Jira, and more
   - Email and Document Automation with AI-powered intake and classification

3. **Data and Analytics**
   - Pipeline Engineering with Spark, Kafka, Airflow, Snowflake for real-time and batch processing
   - Predictive Analytics for forecasting and optimization with explainable outputs
   - Vector and Embedding Infrastructure powering RAG and AI applications

4. **Document Intelligence**
   - RAG Knowledge Systems with citations and source grounding
   - Intelligent Processing that extracts content from complex layouts
   - Document Generation for contracts, reports, and compliance documents
   - Multi-Modal Understanding across text, images, charts, and diagrams

5. **Agentic AI**
   - Agent Swarms with parallel execution, coordination, and dynamic task distribution
   - Multi-Agent Frameworks built on LangGraph, CrewAI, and Semantic Kernel
   - MCP and A2A Protocols for agent-to-tool and agent-to-agent communication
   - Reasoning and Planning with chain-of-thought execution and human-in-the-loop

### The "80% There" Rule
The Ariat content above is the foundation. But this is a McGrath proposal, not an Ariat one. You MUST tailor:
- Search `mcgrath/rfp_docs/` for specific McGrath systems and requirements
- Consider which of the 5 domains matter most for McGrath's managed services needs (Enterprise Automation and Data/Analytics are likely most relevant given Oracle Fusion + MuleSoft + 43+ integrations)
- Frame capabilities in terms of what they mean for McGrath's operations, not as abstract capabilities
- The Ariat version is industry-agnostic. Make it resonate with a managed services evaluator looking at Oracle Fusion support

### What NOT to Do
- Do NOT use any content from McGrath slide 24 (it's Cisco-specific garbage)
- Do NOT make indefensible AI claims. Every capability listed must be real and demonstrable. (The "Sarang lesson" from the transcripts: he pitched agentic AI for everything and got destroyed by Cisco's Imran.)
- Do NOT include pricing or capacity numbers
- Do NOT copy the Ariat content verbatim without McGrath tailoring

### Design Approach
- The HTML gold standard (`slide_01_ai_strategy_innovation.html`) IS the design. It uses a 3-2 card grid (3 top, 2 bottom), each card with icon + title + tagline + bullet items. Replicate this pattern.
- This slide should feel like a natural companion to 6a. If 6a is the "what" (transformation vision), 6b is the "how" (AI engine).

### Slide Number
06b (or 07 if you use separate numbering)

---

## The Connected Storyline

When an evaluator reads these two slides in sequence, they should think:

**6a:** "They understand our transformation. Today's pain points are real. Tomorrow's vision is exactly what we want. The path is simplify, standardize, automate."

**6b:** "And THIS is how they do it. Five AI capability domains. Real technology, not buzzwords. This is why BayOne is different."

The transition from 6a to 6b should feel inevitable -- not like two separate topics stapled together.

---

## Output

Write your HTML slides to:
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_06a_transformation.html`
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/slides_output/slide_06b_ai_strategy.html`

## Rules
1. Read the AI Strategy gold standard HTML slide FIRST -- this is your primary reference for 6b
2. Read all previously approved slides (01, 04, 05) for consistency
3. Read the build feedback docs for lessons learned
4. Read source PNGs for both original slides (14 and 24) -- but remember, slide 24 content is Cisco garbage
5. **Proactively search `mcgrath/rfp_docs/` for McGrath-specific detail** to enrich the content. Don't wait to be told.
6. Use parallel explore agents to read files efficiently
7. Visually compare your output to the gold standard before presenting
8. No em dashes in regular prose
9. Use simple `scratchpad.py` scripts if needed; never heredocs or `python -c`
10. Plan icons up front in a table before coding (learned from session 2)
11. Do NOT modify source files
12. Do NOT change Ariat content without user approval -- but DO propose McGrath-specific adaptations
13. Ask Colin about AI claims you're unsure about -- he's Director of AI and owns this content
