# Deep Research Plan for Ariat Slides

**Created:** 2026-03-04
**Status:** IN PROGRESS

---

## Objective

Create topic-focused research documents with extracted facts, quotes, case studies, and online research to inform 2-3 AI capability slides for Ariat.

---

## Topics and Research Sources

### Topic 1: AI for Managed Testing
**Why:** Ariat's primary pain point. Lots of manual testers, want AI transformation.

**Codebase Sources:**
- [ ] `sephora/` - 8 AI acceleration ideas, pattern detection, batch processing
- [ ] `new_context_2-2-2026/rahul2.txt` - Testing/QA case study (16-person team, 4,000+ test cases)
- [ ] `big4_edw_framework/` - Framework for AI-accelerated work
- [ ] `claude/2026-02-20_ui-conversion-discovery/` - AI-assisted development, Playwright visual testing
- [ ] `cisco-meeting-summaries/` - Graph topology approach for test relationships

**Online Research:**
- [ ] Current state of AI in testing/QA (2026)
- [ ] Real company examples and case studies
- [ ] Specific tools and approaches
- [ ] Quantified outcomes

**Output:** `research/topic_1_ai_testing.md`

---

### Topic 2: Enterprise AI for Back-Office Functions (HR/Finance/Legal/Marketing)
**Why:** Ariat is scaling these departments. Need to show AI applicability across functions.

**Codebase Sources:**
- [ ] `new_context_2-2-2026/rahul2.txt` - General AI strategy discussion
- [ ] `capabilities_deck/` - Existing AI capability positioning

**Online Research:**
- [ ] AI for HR: recruiting automation, onboarding, policy Q&A, performance management
- [ ] AI for Finance: expense processing, reporting, anomaly detection, forecasting
- [ ] AI for Legal: contract review, compliance monitoring, document search
- [ ] AI for Marketing: content generation, campaign analysis, personalization
- [ ] Real company examples for each domain

**Output:** `research/topic_2_enterprise_ai_backoffice.md`

---

### Topic 3: AI for Culture & Skill Development
**Why:** CEO explicitly wants to understand how AI can grow skills and build culture.

**Codebase Sources:**
- [ ] `new_context_2-2-2026/` - Engagement philosophy, team building content

**Online Research:**
- [ ] AI for upskilling and reskilling programs
- [ ] AI for culture transformation and organizational change
- [ ] AI for onboarding and knowledge transfer
- [ ] AI for maintaining culture across geographies
- [ ] Real company examples

**User Input (Later):**
- [ ] Coherent insights from Colin (to be provided at end)

**Output:** `research/topic_3_ai_culture_skills.md`

---

### Topic 4: General AI Capabilities Overview
**Why:** Broad positioning of what BayOne can do with AI.

**Codebase Sources:**
- [ ] `capabilities_deck/slides/` - 13 existing capability slides (extract actual content)
- [ ] `sephora/deliverables/01_ai_acceleration_proposal.html` - Production AI proposal
- [ ] `specs/bayone-design-spec.md` - Design system for output formatting

**Online Research:**
- [ ] Current enterprise AI landscape (2026)
- [ ] Key capability categories and how they're being positioned

**Output:** `research/topic_4_general_ai_capabilities.md`

---

## Research Waves

### Wave 1: Topic 1 Codebase Research (AI for Testing) - COMPLETE
- [x] Agent 1: Deep read of `sephora/` - extract all testing-relevant AI capabilities, quotes, patterns
- [x] Agent 2: Deep read of `new_context_2-2-2026/rahul2.txt` - extract Testing/QA case study details
- [x] Agent 3: Deep read of `big4_edw_framework/` - extract framework and acceleration ideas
- [x] Agent 4: Deep read of `cisco-meeting-summaries/` - extract graph topology and testing approaches

**Output:** `topic_1_ai_testing.md` (550+ lines) with codebase findings

---

### Wave 2: Topic 1 Remaining + Topic 2 Codebase - COMPLETE
- [x] Agent 1: Deep read of `claude/2026-02-20_ui-conversion-discovery/` - AI-assisted dev patterns
- [x] Agent 2: Deep read of `capabilities_deck/` for Topic 2 - existing AI positioning
- [x] Agent 3: Deep read of `new_context_2-2-2026/rahul2.txt` for Topic 2 - **GAP: No relevant back-office content found**
- [x] Agent 4: Online research - AI for Testing (current state, tools, case studies)

**Output:** `wave_2_raw/` (4 files) + `topic_1_ai_testing.md` (COMPLETE) + `topic_2_enterprise_ai_backoffice.md` (started, needs Wave 3)

---

### Wave 3: Topic 2 Online Research - COMPLETE
- [x] Agent 1: Online research - AI for HR (400+ lines)
- [x] Agent 2: Online research - AI for Finance (370+ lines)
- [x] Agent 3: Online research - AI for Legal (400+ lines)
- [x] Agent 4: Online research - AI for Marketing (400+ lines)

**Output:** `wave_3_raw/` (4 files) + `topic_2_enterprise_ai_backoffice.md` (COMPLETE, 600+ lines)

---

### Wave 4: Topic 3 Research - COMPLETE
- [x] Agent 1: Deep read of `new_context_2-2-2026/` - engagement philosophy, team building (350+ lines)
- [x] Agent 2: Online research - AI for upskilling and reskilling (500+ lines)
- [x] Agent 3: Online research - AI for culture transformation (600+ lines)
- [x] Agent 4: Online research - AI for onboarding and knowledge transfer (600+ lines)

**Output:** `wave_4_raw/` (4 files) + `topic_3_ai_culture_skills.md` (COMPLETE, 500+ lines, pending Coherent insights)

---

### Wave 5: Topic 4 Research - COMPLETE
- [x] Agent 1: Deep read of `capabilities_deck/slides/` - all 13 slides extracted (500+ lines)
- [x] Agent 2: Deep read of `sephora/deliverables/01_ai_acceleration_proposal.html` - proposal patterns (300+ lines)
- [x] Agent 3: Read `specs/bayone-design-spec.md` - design requirements (150+ lines)
- [x] Agent 4: Online research - enterprise AI landscape 2026 (1,200+ lines)

**Output:** `wave_5_raw/` (4 files) + `topic_4_general_ai_capabilities.md` (COMPLETE, 500+ lines)

---

## Output Document Standards

Each topic document must contain:
1. **Extracted facts and quotes** - Direct content from source files with file paths
2. **Specific capabilities** - Concrete examples, not generic descriptions
3. **Case study details** - Numbers, outcomes, team sizes, timelines
4. **Patterns applicable to Ariat** - Explicitly called out
5. **Online research findings** - With source URLs
6. **Target length:** 500+ lines of substantive content per document

---

## Progress Tracking

| Wave | Status | Output |
|------|--------|--------|
| Wave 1 | **COMPLETE** | `wave_1_raw/` (4 files) + `topic_1_ai_testing.md` (550+ lines) |
| Wave 2 | **COMPLETE** | `wave_2_raw/` (4 files) + `topic_1_ai_testing.md` (COMPLETE) + `topic_2_enterprise_ai_backoffice.md` (started) |
| Wave 3 | **COMPLETE** | `wave_3_raw/` (4 files) + `topic_2_enterprise_ai_backoffice.md` (COMPLETE, 600+ lines) |
| Wave 4 | **COMPLETE** | `wave_4_raw/` (4 files) + `topic_3_ai_culture_skills.md` (COMPLETE, 500+ lines, pending Coherent) |
| Wave 5 | **COMPLETE** | `wave_5_raw/` (4 files) + `topic_4_general_ai_capabilities.md` (COMPLETE, 500+ lines) |

---

## Final Deliverables

- [ ] `research/topic_1_ai_testing.md`
- [ ] `research/topic_2_enterprise_ai_backoffice.md`
- [ ] `research/topic_3_ai_culture_skills.md`
- [ ] `research/topic_4_general_ai_capabilities.md`
