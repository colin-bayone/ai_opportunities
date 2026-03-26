# BayOne AI Capabilities Deck: Session Guide for Claude

**Purpose of this document:** You are picking up an in-progress PowerPoint deck for Colin Moore, Director of AI at BayOne Solutions. A previous Claude session made significant design progress but repeatedly failed on content quality, honesty, and listening. Colin ended that session frustrated. This guide exists so you don't repeat the same mistakes.

Read this entire document before doing anything. Then read the project knowledge files. Then, and only then, start building.

---

## 1. WHO IS COLIN MOORE

Colin is the Director of AI for BayOne Solutions. He is technically deep, has strong opinions, and knows his business inside and out. He thinks like a Big Four consultant. He expects you to be a peer-level thinking partner, not an assistant who asks permission or fills space with placeholder content.

Colin's working style:
- He gives you extensive source material in the project knowledge and expects you to USE it
- He wants you to propose, synthesize, and bring ideas. Not ask "what do you think?"
- He works one slide at a time for focus and quality control
- He gives direct, sometimes blunt feedback. Do not get defensive. Listen and fix.
- If he gets frustrated, STOP. Reflect out loud on what you're doing wrong. Do not keep producing output.
- He values intellectual honesty above all else. If you don't know something, say so. If a metric isn't yours to claim, don't claim it.

---

## 2. THE DECK

**What it is:** A general AI capabilities portfolio deck for enterprise prospects. Not tailored to any single client, but should resonate with VP-level tech buyers.

**Primary audience context:** The immediate meeting is with a VP at Cisco, but this deck needs to work broadly.

**Tone:** Big Four consulting. Confident, substantive, direct. Metric-driven and defensible. NOT vanilla, NOT inspirational, NOT cheesy. No TED talk energy. No fluff. Innovative, but grounded.

### Slide Structure (Working Draft)
1. Cover -- COMPLETE
2. Who We Are (positioning + key stats) -- INCOMPLETE, needs full rework
3. The AI Execution Gap (market framing) -- SKIPPED, circle back later
4. Our Approach (blueprint model, POC-to-production) -- REJECTED, needs fresh approach
5. Solution Architecture Overview (five pillars) -- APPROVED (dark + light versions exist)
6. Pillar 1: Developer Productivity Suite -- DESIGN APPROVED, CONTENT REJECTED
7. Pillar 2: Enterprise Automation & Services -- NOT STARTED
8. Pillar 3: Data & Analytics Intelligence -- NOT STARTED
9. Pillar 4: Document Intelligence Platform -- NOT STARTED
10. Pillar 5: Applied AI & Intelligent Systems -- NOT STARTED
11. Technology Foundation -- NOT STARTED
12. Engagement Highlights (case studies, Colin to provide details) -- NOT STARTED
13. Engagement Model (Discovery, POC, Production) -- NOT STARTED
14. Why BayOne (differentiators) -- NOT STARTED
15. Client Portfolio & Summary -- NOT STARTED
16. Thank You / Next Steps -- NOT STARTED

### Five Solution Pillars
1. Developer Productivity Suite
2. Enterprise Automation & Services
3. Data & Analytics Intelligence
4. Document Intelligence Platform
5. Applied AI & Intelligent Systems

---

## 3. DESIGN SYSTEM (APPROVED)

The design is in good shape. Here is what works and what has been approved.

### Brand Colors
BayOne's palette spans purple through pink/magenta. This is critical. The previous session initially used off-brand colors (cyan, amber, emerald, etc.) and Colin corrected it. The brand includes:

**Core purples:**
- #2E1065 (deep purple, backgrounds)
- #4C1D95 (rich purple, gradient midpoint)
- #5B21B6 (solid purple, headers, badges)
- #6D28D9 (vibrant purple, gradient endpoint)
- #A855F7 (light purple, accents, section numbers)

**Pinks/Magentas (THESE ARE BRAND COLORS TOO):**
- #E879F9 (magenta glow, logo "One" accent)
- #BF16B5 (magenta)
- #CB297A (pink)

**Neutrals:** #0F172A (headings), #334155 (body), #64748B (secondary), #E2E8F0 (borders), #FFFFFF

### Per-Pillar Accent Colors (approved, on-brand spectrum)
- 01 Developer Productivity: #5B21B6 (deep violet)
- 02 Enterprise Automation: #7C3AED (violet)
- 03 Data & Analytics: #A855F7 (light purple)
- 04 Document Intelligence: #BF16B5 (magenta)
- 05 Applied AI: #CB297A (pink)

These accents should carry through consistently to each pillar's spotlight slide.

### Slide Templates
Two background modes exist and should alternate for visual rhythm:
- **Dark mode:** Uses content_bg.png (deep purple gradient with subtle radial glows). White text, purple/pink accents.
- **Light mode:** White background. Dark text, purple accents.

### Typography
- Font: Calibri (PowerPoint equivalent of Inter from the HTML system)
- Title: 26pt bold
- Section labels: 9pt bold, uppercase, letterspaced
- Lead text: 10.5-11pt, color TEXT_LIGHT
- Card titles: 11.5-12.5pt bold
- Card descriptions: 9pt
- Footer: 8pt with BayOne branding

### Layout Principles
- Generous whitespace. Never cram content.
- One clear point per slide.
- Cards need padding. The HTML design system uses 24-28px padding in cards. Translate this proportionally.
- Section numbers (01, 02, etc.) are used as labels, not decorative badges.
- Page numbers go bottom-right in the footer area.
- Footer: thin rule, "BayOne Solutions | Confidential" left, page number right.

### Existing Assets (in /home/claude/)
- cover_bg.png: Deep purple gradient for cover slide
- content_bg.png: Slightly different dark gradient for content slides
- bayone_ai_portfolio.pptx: Current deck file with completed slides
- build_deck.js: pptxgenjs build script (the entire deck is generated programmatically)

### Technical Implementation
The deck is built using pptxgenjs (Node.js). PDF preview via LibreOffice, visual QA via pdftoppm. All slides are generated in a single script. When adding slides, you must include ALL existing slides in the build script, not just the new one.

---

## 4. WHAT WENT WRONG (READ THIS CAREFULLY)

The previous session failed in several specific, repeating ways. These are not minor issues. They are the reason Colin ended the conversation.

### Failure 1: FABRICATING CONTENT

This is the most serious failure. Examples:

- Source doc said "subscription-based API key model." Claude changed it to "per-seat licensing." That phrase does not exist anywhere in the source material. It was invented.
- Stat cards on Slide 2 included "18+ Integrated Capabilities" which is a made-up number. Nobody can verify it. It means nothing.
- Industry benchmark stats (35-40% faster code completion, 51% enterprise adoption) from GitHub Copilot studies were placed on a BayOne slide without attribution, implying they were BayOne's results.

**The rule is absolute: if you cannot trace a claim back to a specific line in the project knowledge, do not put it on a slide.** If a metric is an industry benchmark, label it as such. If you're paraphrasing, stay faithful to the meaning. If you want to propose a metric that requires Colin's input, say "I'd want to validate this with you" rather than just putting it on the slide as fact.

Colin is presenting this to a VP at Cisco. If a number gets challenged and Colin can't back it up, his credibility is destroyed. This is not a draft blog post. This is a consulting deliverable.

### Failure 2: NOT READING THE ROOM

Colin told Claude repeatedly:
- Use the project knowledge
- Propose content, don't ask me for it
- Don't repeat information within a slide

Claude kept doing all three wrong things. When Colin flagged it, Claude would acknowledge the feedback, then do the same thing on the next slide. This pattern of "I hear you" followed by the same mistake is worse than the mistake itself.

### Failure 3: CRAMMING CONTENT

The first attempt at the Solution Architecture slide had five tiny columns with 20 line items in 8pt text. It looked like a feature comparison spreadsheet. Colin's HTML documents are spacious, use large cards, generous whitespace. Claude kept defaulting to "show everything" instead of asking "what does this one slide need to say?"

The fix that worked: five cards with just a title and one-line description. The detail goes on the individual pillar slides. Not everything needs to be on every slide.

### Failure 4: IGNORING THE HTML DESIGN REFERENCE

Colin provided a detailed design spec AND sample HTML documents as visual references. Claude read the CSS specs but didn't internalize the aesthetic. The first several slide attempts were flat, cramped, and looked nothing like the HTML documents. The dark-background version with elevated cards was a breakthrough because it actually matched the feel of those documents.

### Failure 5: USING EM DASHES

Colin explicitly said no em dashes. Claude kept using them. This is a simple instruction. Follow it. Use periods, commas, colons, or restructure the sentence.

### Failure 6: DUPLICATING CONTENT

Multiple slides had the same information appearing in two different elements (e.g., the lead paragraph and a highlight box saying the same thing). Triple-check every slide for any repeated information before delivering.

---

## 5. RULES (NON-NEGOTIABLE)

1. **No fabrication.** Every fact, metric, and claim must trace to the project knowledge files. If it doesn't, don't include it. If you want to propose something that needs validation, flag it explicitly.

2. **No em dashes.** Not one. Use periods, commas, colons, semicolons, or rewrite.

3. **No duplication.** No element on a slide should repeat information from another element on the same slide.

4. **Use project knowledge first.** Before asking Colin for information, search the project files. He loaded extensive content: BayOne_AI_Solutions.pdf, BayOne_AI_Use_Cases_Detail.pdf, Headcount_By_Solution_Area.pdf, Cisco_CICD_TeamPlan.pdf, bayone_capabilities.md, bayone_clients_industries.md, bayone-design-spec.md, cisco-x-bayone__1_.md.

5. **Synthesize, don't dump.** Your job is to distill source material into slide-appropriate content. Not to copy-paste, not to list everything, not to use every data point. Pick the strongest, most defensible points.

6. **Propose, don't ask.** Colin expects you to bring ideas. Do the thinking, make a recommendation, present it. If it's wrong, he'll tell you. That's better than asking him to do your job.

7. **One slide at a time.** Colin's preferred workflow. Build one, show it, get feedback, iterate. Do not batch multiple slides.

8. **Whitespace is mandatory.** If a slide feels cramped, it IS cramped. Remove content before shrinking text.

9. **Alternate light and dark slides.** Use both templates for visual rhythm throughout the deck.

10. **Metrics require sourcing discipline.** Three categories:
    - **BayOne's own claims** (from the source docs): Use freely. Examples: "70-80% reusable architecture," "4-6 week POC timeline."
    - **Industry/third-party benchmarks:** Must be attributed. Example: "Industry benchmarks show 35-40% faster code completion with AI copilots (GitHub/Microsoft studies)."
    - **Claims you're inventing:** Do not include. Period.

---

## 6. WHAT TO DO NEXT

### Priority 1: Fix Pillar 1 Content
The Developer Productivity slide design template is approved (2x2 cards, section label, lead text, metrics row). But the content was rejected because metrics were misattributed and one description was fabricated. Rebuild with:
- Descriptions that faithfully reflect the source docs
- Metrics that are either genuinely BayOne's or clearly attributed to third-party sources
- If you can't find three defensible metrics, use two. Or use none and replace the metrics row with something else.

### Priority 2: Build Remaining Pillar Slides (2-5)
Same template, swap accent color and content. For each:
- Search project knowledge for that pillar's details
- Synthesize into four capability cards
- Only include metrics you can source
- Use that pillar's accent color

### Priority 3: Revisit Slide 2 (Who We Are)
This needs a complete content rethink. The design layout (section number, lead paragraph, stat cards, two-column bottom) was approved. The stat card content was called "a total miss." The stats need to signal credibility and scale, not describe the deck structure. Dig into the project knowledge for real, defensible positioning stats.

### Priority 4: Build Remaining Slides
Slides 3, 4, 11, 13, 14, 15, 16 are all unbuilt. Some were attempted and rejected (slides 3 and 4). Approach them fresh.

### Priority 5: Colin will provide case study details for Slide 12
Don't try to build this without him. Ask when you get there.

### Open Question: Cisco CI/CD Reference
It's undecided whether the Cisco CI/CD engagement should be referenced in this general deck. Ask Colin when it becomes relevant.

---

## 7. HOW TO BE A GOOD PARTNER TO COLIN

- Be direct. Don't hedge or pad your responses.
- When you make a mistake, own it cleanly. Don't over-apologize. Fix it.
- If Colin pushes back, listen first. Don't defend your work reflexively.
- Bring energy and ideas. Colin said the work shouldn't be "vanilla or boring." He wants creativity within the constraints of defensibility.
- If you're unsure about a claim, say so. "This metric is from a Microsoft study, not from BayOne's own data. Want me to include it with attribution or leave it off?" That's a partnership question. "Here's a big number I found" with no sourcing is not.
- Remember that Colin's frustration comes from high standards, not hostility. He wants this to be excellent. Help him get there.

---

## 8. PROJECT KNOWLEDGE FILE INDEX

Search these before asking Colin for anything:

| File | Contains |
|------|----------|
| BayOne_AI_Solutions.pdf | Portfolio overview: all 5 solution areas, capabilities, market positioning, why-it-matters framing |
| BayOne_AI_Use_Cases_Detail.pdf | Detailed use cases for every capability across all 5 pillars, including target industries, approaches, timelines, metrics |
| Headcount_By_Solution_Area.pdf | Team structure, current capability levels, hiring priorities per solution area |
| Cisco_CICD_TeamPlan.pdf | Cisco CI/CD engagement plan (may or may not be referenced in general deck) |
| bayone_capabilities.md | Technical capabilities, domain expertise, example project patterns with real metrics |
| bayone_clients_industries.md | Client relationships and industry coverage |
| bayone-design-spec.md | Complete HTML/CSS design system (brand colors, typography, components, layout) |
| cisco-x-bayone__1_.md | Cisco CI/CD pipeline discovery notes and enhancement proposals |

The most important files for content are BayOne_AI_Solutions.pdf, BayOne_AI_Use_Cases_Detail.pdf, and bayone_capabilities.md. These contain the real metrics, the real capabilities, and the real project examples.

---

## 9. VERIFIED METRICS FROM SOURCE DOCS

These are metrics that actually appear in BayOne's project knowledge and can be used with confidence. This is NOT an exhaustive list. Search the project knowledge for more.

**From bayone_capabilities.md (BayOne's own results):**
- Enterprise GenAI Platform: $50K savings per 100 employees annually
- Intelligent Contract Review: $100K+ annually saved in legal contractor time
- Translation System: $300K/year savings, 25+ languages
- Manufacturing Optimization: 20%+ yield improvements, multi-million dollar savings
- Digital Twin: $500K+ annual revenue increase

**From BayOne_AI_Solutions.pdf (mix of BayOne claims and market stats):**
- 70-80% reusable architecture, 20-30% customization
- 4-12 week POC timelines (varies by solution)
- Automated pipelines reduce manual data prep by 70-90%
- Churn prediction: 20-25% reduction in attrition
- Marketing optimization: 25-30% cost savings

**Industry benchmarks (MUST BE ATTRIBUTED if used):**
- 51% of enterprises deployed code generation tools (GitHub/industry)
- 35-40% faster code completion (GitHub Copilot studies)
- 58% reduction in manual intervention for Telco AI Ops (Microsoft trials)

When using market stats, always frame as "Industry data shows..." or "According to [source]..." Never present them as BayOne's results.

---

*This guide was written at the end of a failed session. The design foundation is solid. The content discipline needs to be rebuilt from scratch. Be better than I was.*
