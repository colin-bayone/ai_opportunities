# Handoff: Build Slides 18-20 (Risks & Key Asks)

## Purpose

You are building three slides covering risk management and engagement asks. These sit between the case studies and the commercial section.

**Your slides:**
- **Slide 18: Risks & Mitigation Part 1** (old slide 26) -- 5 risks with mitigations
- **Slide 19: Risks & Mitigation Part 2** (old slide 27) -- 3 risks with mitigations
- **Slide 20: Key Asks** (old slide 28) -- What BayOne needs from McGrath

### CRITICAL: Deduplication Required for Slide 20
Slides 18 (Risks Part 1) and 20 (Key Asks) share nearly identical content in their first two rows. "KT & Documentation Facilitation" appears as a risk in 18 and as an ask in 20. "Infrastructure Support" same pattern. In the new order these are back-to-back, making repetition obvious.

**Slide 20 (Key Asks) must be rewritten to focus purely on what BayOne needs McGrath to provide, WITHOUT restating the risk framing from slide 18.** Present the deduplicated version to Colin for approval before finalizing.

## Context

### The Project
BayOne Solutions is rebuilding a McGrath RentCorp RFP response deck. You are one of three parallel sessions in the final build wave. Others are building slides 21-22 (commercial) and 3 new Ariat additions.

### Previously Built (Read for Quality Reference)
Browse `slides_output/` -- there are 20+ completed slides. Read at least slide_05 (scope cards) and slide_06a (transformation) for design consistency.

### Key Rules
1. **Read gold standard slides first:** `claude/2026-03-03_ariat_slides/foundational/slide_01_ai_strategy_innovation.html`, `slide_02_*.html`, `slide_03_*.html`
2. **No em dashes.** No contrastive framing. No colloquial language.
3. **No Playwright unless Colin explicitly asks.**
4. **Change ONLY what is requested.** For the dedup work, present changes for approval.
5. **Always read PNGs AND content.md.** PNGs are source of truth.
6. **Remove WIP markers and internal annotations.**
7. **Plan icons up front.**

### Design System
- **Canvas:** 16:10, max-width 1100px
- **Colors:** `#2e1065` -> `#4c1d95` -> `#5b21b6` -> `#6d28d9` -> `#a855f7` -> `#e879f9`
- **Typography:** Inter (300-700). Headlines 24-28px, Body 11-12px
- **Icons:** Font Awesome 6.5.1 CDN
- **Structure:** slide-header / slide-content / slide-footer

---

## Slide 18: Risks & Mitigation Part 1 (Old Slide 26)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_26/slide_26.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_26/content.md`

### What It Is
5 risks with mitigations. Status: Final. This is solid content. Design it as a clean risk table or card layout. Each risk has: Risk description, Mitigation strategy.

**Build faithfully.** Content is marked Final and should not be modified.

**Output:** `slides_output/slide_18_risks_part1.html` (slide number 18)

---

## Slide 19: Risks & Mitigation Part 2 (Old Slide 27)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_27/slide_27.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_27/content.md`

### What It Is
3 additional risks: geopolitical changes, information sharing by incumbent, knowledge gap from attrition. Status: Final. Same design pattern as slide 18 for consistency.

**Build faithfully.** Content is marked Final.

**Output:** `slides_output/slide_19_risks_part2.html` (slide number 19)

---

## Slide 20: Key Asks (Old Slide 28)

### Source
- PNG: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_28/slide_28.png`
- Content: `claude/2026-03-19_pptx_extractor_skill/source/WIP_Managed_Services_Support_Proposal/slide_28/content.md`

### What It Is
4 asks from McGrath: KT & documentation facilitation, Infrastructure support, Timely information sharing, Sign-offs & approvals. Status: Final.

### DEDUPLICATION WORK
The first two asks (KT facilitation, Infrastructure support) overlap heavily with risks in slide 18. Since these slides are now back-to-back (positions 18, 19, 20), the repetition is obvious.

**Your job:**
1. Read both slide 26 (risks) and slide 28 (asks) content carefully
2. Identify the specific overlapping content
3. Rewrite slide 20 to focus purely on WHAT BayOne needs McGrath to provide (actionable requests), WITHOUT restating the risk framing
4. **Present the original and rewritten versions to Colin for approval before finalizing**

The risk slides frame "what could go wrong." The asks slide should frame "what we need from you to succeed." Different angles, no duplication.

**Output:** `slides_output/slide_20_key_asks.html` (slide number 20)

---

## Output Files
- `slides_output/slide_18_risks_part1.html`
- `slides_output/slide_19_risks_part2.html`
- `slides_output/slide_20_key_asks.html`

Write a results handoff at `handoffs/handoff_14_results.md` when done.
