# Handoff: Draft Executive Summary Content

## Purpose

You are a content strategist drafting the Executive Summary for a McGrath RFP response deck. This is NOT a slide-building task -- you are writing the **content** that will later be designed into an HTML slide by a different session.

The Executive Summary is the first substantive slide an evaluator reads (slide position #2, right after the title). It needs to hook McGrath immediately with a clear, compelling value proposition. The current version is a WIP todo list -- literally just bullet points of things someone needs to do. You're replacing that with real content.

## Context

### The Project
BayOne Solutions is responding to an RFP from McGrath RentCorp for managed services support. McGrath is undergoing a major transformation -- migrating from legacy systems (Nexstar) to Oracle Fusion, with 43+ integrations (likely 70-80 per insider intel), Salesforce, MuleSoft, and more. BayOne's key differentiator is AI-driven operations.

### Key Strategic Points (from Neha/Colin transcripts)
- AI playbook is BayOne's biggest differentiator: "The AI playbook is huge because that's one of the things they're looking at very carefully and that's our strength"
- BayOne should be positioned as a **niche AI-enabled solutions vendor**, NOT a staffing company
- Discovery-first approach: price to what the RFP says, but signal that discovery will refine the picture
- Mahesh (CIO-level reference) is actively supporting BayOne's bid
- Previous implementation by incumbent was ~$23M with ~200 people -- this is a large, complex engagement

### What the Deck's Narrative Arc Should Be
*"We understand your NextGen transformation challenge and we've built a solution around it. AI-driven operations are our core differentiator, and we'll prove it with a phased delivery backed by real metrics and real case studies. Here's what it costs, here's why we're worth it, let's get started."*

The exec summary should be the 30-second version of this story.

## Source Material (Read All of These)

### RFP Context
- **RFP overview:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/rfp_overview.csv`
- **General requirements:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/general_requirements.csv`
- **Specific requirements:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/specific_requirements.csv`
- **SLA definitions:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/sla.csv`
- **KPIs:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/kpi.csv`
- **Architecture:** `/home/cmoore/programming/cisco_projects/cicd/mcgrath/rfp_docs/final/architecture.md`

### Transcript Analysis (Strategic Context)
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/04_combined_transcript_analysis.md`

### Research Synthesis
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/planning/03_research_synthesis.md`

### What the Current Exec Summary Looks Like (The Bad Version)
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_11/content.md`
- Also read the PNG: `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_11/slide_11.png`

### Anti-Patterns (What NOT to Do)
- `/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/05_bad_slide_autopsy.md`

## Instructions (Follow This Order)

### Step 1: Research
Use parallel explore agents to read the RFP materials, transcript analysis, and research synthesis. Understand:
- What is McGrath buying? (managed services for Oracle Fusion, integrations, Salesforce, etc.)
- What's the scope? (in-scope vs out-of-scope services)
- What are the SLAs and KPIs they expect?
- What's the timeline? (Phase 1 onboarding May-July 2026, then ongoing)
- What makes BayOne different? (AI-driven operations, discovery-first approach)

### Step 2: Read the Bad Version
Look at slide 11's current content to understand what NOT to do. It's a WIP todo list, not an exec summary.

### Step 3: Draft the Executive Summary
Write your draft to:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/research/08_exec_summary_draft.md`

The exec summary should include:
1. **Opening hook** (2-3 sentences): Show you understand McGrath's transformation challenge. Reference the NextGen ecosystem, Oracle Fusion, the complexity of 43+ integrations. Don't be generic -- be specific to THEIR situation.
2. **Value proposition** (2-3 sentences): What BayOne brings. AI-driven operations as the differentiator. Phased delivery from discovery through steady state. Proven track record with Oracle Fusion implementations.
3. **Key proof points** (3-4 bullets or stats): Quick credibility hits. Could include: 13 years experience, 100+ customers, 95.7% SLA compliance (from Oracle HCM case study), specific tech stack relevance.
4. **Forward-looking statement** (1-2 sentences): Discovery-first approach, partnership mindset, continuous optimization through AI.

### Step 4: Write 2-3 Alternative Framings
Don't just write one version. Give Colin options:
- **Version A:** Lead with understanding of McGrath's challenge
- **Version B:** Lead with BayOne's AI differentiator
- **Version C:** Lead with proof/credibility (numbers-first approach)

### Step 5: Layout Suggestions
You're not building the slide, but suggest what kind of layout this content would work best with. Reference specific layouts from:
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-03_ariat_slides/page_layouts/`

## Rules
- Use parallel explore agents to read files efficiently
- Persist your work to files as you go
- Use simple `scratchpad.py` scripts if needed; never heredocs or `python -c`
- Do NOT modify any source files
- Do NOT finalize anything -- present options for Colin to choose from
- Be specific to McGrath. Generic "we deliver excellence" language is exactly what the anti-patterns warn against.
- Do NOT include any pricing or capacity numbers. Colin has explicitly said pricing/capacity is hands-off.
- Do NOT expose insider information (the 70-80 integration count). Use the RFP's stated numbers only.
