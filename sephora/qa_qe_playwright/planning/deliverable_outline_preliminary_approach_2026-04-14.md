# Deliverable Outline: Preliminary Approach

**Document:** preliminary_approach_2026-04-14
**Status:** Revision 2 planning (post Round 1 feedback)
**Last Updated:** 2026-04-14

---

## Cover Page

- **Cover label:** AGENTIC QUALITY ENGINEERING
- **Title:** "An Agentic Platform for Quality Engineering" (DECIDED)
- **Subtitle:** Preliminary approach for Sephora's Quality Engineering, Development, UI/UX, and Content Production teams
- **Meta:** Prepared For: Sephora / Prepared By: BayOne Solutions / Date: April 2026

## Table of Contents (NEW)

Simple, clean navigation. Lists all sections with names. Placed immediately after the cover page, before Section 01.

---

## Section 01: Problem Summary

**Purpose:** Demonstrate understanding of Sephora's situation without putting words in their mouth.

**Changes from draft:**
- Reframe the opening. Do NOT state that Sephora identified visual QE as a gap. Instead, frame as: organizations at this stage of QE maturity commonly encounter this challenge. Several teams were identified in conversation that would benefit from a more structured approach.
- Add a disclaimer early: this represents BayOne's understanding as of the conversations thus far. It may not represent the full picture and will be refined as more conversations happen.
- Keep the four consumer group cards (these were approved as "good").
- Keep the highlight box about common requirements.

**Content outline:**
1. Opening paragraph: industry-level framing (most organizations face this), not Sephora-specific claim
2. Disclaimer paragraph: this is BayOne's current understanding, subject to refinement
3. Brief context: AMP model, Selenium-to-Playwright migration, AI mandate, mid-2026 timeline
4. Four consumer group cards (two-col layout, same as draft)
5. Common requirements highlight box (same as draft)

---

## Section 02: Proposed Architecture

**Purpose:** Present BayOne's architectural recommendation as a synthesized, authoritative perspective.

**Changes from draft:**
- FULL REWRITE of the "Unified Backbone with Configurable Specificity" content. Must synthesize across:
  - Set 01: Colin's deterministic-first philosophy, state graph concept, CI/CD integration, agent evaluation framework, multi-model strategy, confidence/RLHF approach, observability, "system autonomy" not "autonomous systems," framework as growth bottleneck
  - Set 02: Exploratory flows and structured playbooks, review agent layer ("smart but lazy"), guardrails (non-destructive by default, sandbox escalation), traceability (action logs, SHA tags), Figma MCP connector, same tool for QE and marketing
  - Set 03 discussion: configurable specificity (settings, not structure), ecosystem not separate tools, deterministic playbooks (AI discovers, save, replay, tie to releases), human-in-the-loop as design feature, standard stack, Docker for isolation, Azure Container Apps for production
- REMOVE "Progressive Buildout" from this section (move to Section 05)
- REMOVE "Control Panel" as standalone subsection (fold relevant details into Section 03 Technical Foundation)
- The deterministic playbook engine content was good and stays
- Human-in-the-loop and confidence scoring content was good and stays

**Content outline:**
1. Lead paragraph: unified platform, one system, configurable
2. The architectural approach (REWRITE NEEDED, standalone content document required)
   - Deterministic foundation with agentic augmentation
   - How the platform serves four audiences through configuration, not separate implementations
   - The relationship between exploratory testing, playbook creation, and deterministic replay
   - How CI/CD integration and release mapping keep tests current
   - The review agent layer and human oversight model
   - Observability as a first-class architectural concern
3. Deterministic Playbook Engine (keep, minor refinements)
4. Human-in-the-Loop and Confidence Scoring (keep, minor refinements)

---

## Section 03: Technical Foundation

**Purpose:** Present the stack and production infrastructure with enough detail to be credible.

**Changes from draft:**
- Keep the core technology stack table (approved)
- Keep the deterministic-first design subsection (approved)
- Keep the multi-model strategy highlight box (approved)
- Keep the traceability and observability subsection (approved)
- Keep the production infrastructure table (approved)
- Keep the cost management highlight box (approved)
- Fold in relevant web application details (previously in Control Panel subsection) as a natural part of the stack table description. The Django/FastAPI row already exists; no separate callout needed.

**Content outline:**
1. Lead paragraph: battle-tested, conservative, maintainable
2. Core technology stack table
3. Deterministic-first design
4. Multi-model strategy highlight box
5. Traceability and observability
6. Production infrastructure table
7. Cost management highlight box

---

## Section 04: Engagement Models

**Purpose:** Present the three options clearly.

**Changes from draft:**
- Change layout from three-column to horizontal stacked cards (full-width, one per row)
- REMOVE the "Outcome-based, not headcount-based" highlight box entirely
- The outcome-based nature is already clear from the card descriptions; no separate callout needed

**Content outline:**
1. Lead paragraph: three models, first two are outcome/milestone/deliverable-based
2. Card: Fully Managed Delivery (full width)
3. Card: Variable Collaborative Delivery (full width)
4. Card: Staff Augmentation (full width, with note that BayOne does not recommend for this engagement)

---

## Section 05: Implementation Pathway

**Purpose:** Present sequencing options with appropriate caveats.

**Changes from draft:**
- Move "Progressive Buildout" content here from Section 02
- Keep the two starting point cards (rapid validation vs. broadest value)
- Keep the parallel execution subsection
- Keep the sequencing disclaimer highlight box
- Keep the additional collaboration note (re: Sephora's AI portal initiative)
- Consider whether progressive buildout should lead the section (framing the philosophy) with the specific starting points following

**Content outline:**
1. Lead paragraph: unified architecture supports multiple sequencing strategies
2. Progressive buildout philosophy (moved from Section 02)
3. Two-col cards: rapid validation starting point vs. broadest value starting point
4. Parallel execution subsection
5. Sequencing disclaimer highlight box
6. Additional collaboration note

---

## Section 06: Preliminary Framing

**Purpose:** Frame the document as preliminary, list what is needed to refine, close as a partner.

**Changes from draft:**
- No significant changes needed. This section was not flagged in feedback.

**Content outline:**
1. Lead paragraph: initial thinking, starting point for discussion
2. Requirements for refinement (bulleted list)
3. Continued partnership closing

---

## Outstanding Work Items

1. ~~**Title decision:**~~ RESOLVED. "An Agentic Platform for Quality Engineering"
2. **Architecture section rewrite:** Needs a standalone content document synthesizing across the full research library before editing the HTML
3. **All other changes** can be applied directly once the architecture content is ready

---

*This is a working document. Updated as revisions are planned and executed.*
