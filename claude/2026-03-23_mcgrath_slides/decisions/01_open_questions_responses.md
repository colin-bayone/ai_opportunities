# Open Questions & Responses

## Resolved

### Q1: Slide 31 (Case Study Title Card) -- QUESTION WITHDRAWN
**Original context:** Orchestrator incorrectly described slide 31 as a title-only card with no content. This was based on faulty PPTX extraction markdown that only captured the title.
**Reality (confirmed by reading PNG):** Slide 31 is a FULL case study slide with Business Scenario, Scope/Services/Technologies, Solution methodology (Oracle Soar), and Benefits (payroll processing reduced 12 days to 3 days, data accuracy 98.6%, 78% self-service adoption, payroll errors reduced 150-200 to 8-12 per cycle).
**Similarly, slide 30** was described as a section divider but is actually a full content slide with "IT Operations & Maintenance Service Expertise" (4 columns) and "Execution Readiness" (3 columns). Also has a "Check with Neha" note in red.
**Lesson:** The PPTX extractor's markdown (content.md) sometimes fails to capture table/grid content. **Workers MUST always read the PNG screenshots, not just content.md.** The images are the source of truth.
**Action:** Question withdrawn. Both slides are full content slides and stay as-is in the build list. Updated worker rules to mandate reading PNGs.

### Q2: Governance Gap
**Context:** Skipped slides 16 (Communication Model), 17 (Escalation Matrix), and 18 (Governance & Reporting) were badly executed, but the CONCEPT of showing governance structure is something RFP evaluators typically expect. The reordering session suggested creating one new, well-designed slide that combines communication + escalation + governance into a single clean design, placed in Section 3 (Delivery Approach).
**Colin's response:** "Document this idea, but save for later." Not doing it now.
**Action:** Idea documented. Parked for future consideration. Not included in build handoffs.

### Q3: Add Ariat 11 (Enterprise AI Solutions)?
**Context:** Ariat slide 11 shows AI-powered automation across 4 business functions (HR, Finance, Legal, Marketing). Has an HTML gold standard already built. No McGrath equivalent exists.
**Colin's response:** YES, add it. But tailor for McGrath and the RFP -- not leave as-is. "It's like 80% there but can be better."
**Action:** Added to build list. Builder must adapt content to McGrath's context (their Oracle Fusion environment, managed services scope, specific departments).

### Q4: Add Ariat 05 (Partnership Models)?
**Context:** Ariat slide 05 shows 4 engagement types: Managed Services, T&M, Fixed Capacity, Managed Projects. No McGrath equivalent. Bridges the gap between "here are our services" and "here's our solution for you."
**Colin's response:** YES, add it. But make relevant to the RFP. "80% there."
**Action:** Added to build list. Builder must frame engagement models in context of what McGrath is buying.

### Q5: Add Ariat 12 (Quality Engineering)?
**Context:** Ariat slide 12 shows 6 AI-powered QE capabilities with a chevron flow bar. Has an HTML gold standard. Strong technical depth.
**Colin's response:** YES, add it. But make relevant to the RFP. "80% there."
**Action:** Added to build list. Builder must connect QE capabilities to McGrath's testing/CI/CD needs.

### Q6: Closing Section Length / Tech Stack
**Context:** The reordering moved Tech Stack, Service Offerings, and Make Tech Purple from the intro to near the close. That made the closing section 6 slides long. Tech Stack (slide 04) is the weakest -- just a logo grid of ~40 technologies, identical across both decks, no differentiation value.
**Colin's response:** "We can kill tech stack. Good insight."
**Action:** Slide 04 (Technology Stack) moved to SKIP. Closing section is now 5 slides.

---

## Key Principle Captured
**"80% there"** -- When adding Ariat slides to the McGrath deck, they are NOT copy-paste. They provide the design, structure, and ~80% of the content, but must be tailored to McGrath's specific context and RFP requirements. Builders must adapt, not just replicate.

---

### Q7: Assumptions Content (Slide 20)
**Context:** Skipped slide 20 was awful (WIP markers, internal names visible), but the underlying content has legal/contractual value -- ticket volume baselines, complexity distribution, resource adjustment triggers, etc. Slide 47 (Prerequisites) covers related but different ground (access, SPOCs, documentation McGrath must provide). Both slides are dense.
**Colin's response:** Yes, the assumptions content matters. But can't do it lightly -- both slides are super dense. May need to deduplicate across 20 and 47 and produce two crisp slides that retain the important content. Colin must directly approve any content removals. This should be its own Claude session.
**Action:** Create a dedicated research/cleanup session to:
1. Read slides 20 and 47 in detail
2. Identify overlap and deduplicate
3. Propose two crisp slides (Prerequisites + Assumptions) with clear content
4. Present to Colin for approval before anything is removed
Slide 20 status changes from SKIP to "content being salvaged into a new Prerequisites & Assumptions pair."

### Q8: Overlap Between Risks (Slide 26) and Key Asks (Slide 28)
**Context:** Slides 26 (Risks Part 1) and 28 (Key Asks) share nearly identical content in their first two rows. "KT & Documentation Facilitation" appears as a risk in 26 and as an ask in 28. "Infrastructure Support" same pattern. In the new order, these slides are back-to-back (positions 18, 19, 20), making the repetition obvious and unprofessional.
**Colin's response:** Agrees repetition is not good. Should be cleaned up.
**Rationale:** An evaluator reading sequentially would hit the same points twice. The risks slide should frame what could go wrong; the asks slide should focus purely on what BayOne needs McGrath to provide. Overlapping content weakens both slides.
**Action:** When building slides 26 and 28, the worker should deduplicate. Key Asks (28) should be rewritten to focus on actionable requests WITHOUT restating the risk framing. Colin must approve the specific content changes before finalizing.

---

## All Questions Resolved

| Q | Topic | Status | Action |
|---|-------|--------|--------|
| 1 | Case Study Title Card (31) | WITHDRAWN -- slide has full content | No action needed |
| 2 | Governance Gap | Parked for later | Documented |
| 3 | Add Ariat 11 (Enterprise AI) | YES, tailor to McGrath (80%) | Added to build |
| 4 | Add Ariat 05 (Partnership Models) | YES, tailor to McGrath (80%) | Added to build |
| 5 | Add Ariat 12 (Quality Engineering) | YES, tailor to McGrath (80%) | Added to build |
| 6 | Tech Stack in closing | KILL IT | Slide 04 moved to SKIP |
| 7 | Assumptions (slide 20) | Salvage into 2 crisp slides | Own Claude session |
| 8 | Risks/Asks overlap (26+28) | Deduplicate | Builder cleans up, Colin approves |
