# Feedback, Violations, and Lessons — Singularity Session Handoff

**Date:** 2026-04-14
**Purpose:** Comprehensive reference for the incoming session covering every behavioral rule, every documented violation, the dominant B2 failure pattern, all items that are not working well, all open questions awaiting decisions, the prescriptive rules audit results, and key lessons to prevent repeating these patterns.

**Sources:**
- Exhaustive synthesis: `claude/singularity_feedback/2026-04-13_round_01/00_synthesis.md`
- Open questions and feedback: `claude/2026-04-10_singularity_nested_design/04_open_questions.md`
- Prescriptive rules audit: `claude/2026-04-13_mermaid_research/b2_violation_review_2026-04-14.md`
- Hard rules file: `.claude/skills/singularity/references/hard_rules.md`

---

## Table of Contents

1. [Complete Behavioral Rule Catalog (B1-B16)](#1-complete-behavioral-rule-catalog-b1-b16)
2. [The B2 Violation Pattern in Detail](#2-the-b2-violation-pattern-in-detail)
3. [Prescriptive Rules Audit Results (11 Flagged Items)](#3-prescriptive-rules-audit-results-11-flagged-items)
4. [What Is Not Working Well](#4-what-is-not-working-well)
5. [Open Questions Awaiting Decisions](#5-open-questions-awaiting-decisions)
6. [Key Lessons for the Next Session](#6-key-lessons-for-the-next-session)

---

## 1. Complete Behavioral Rule Catalog (B1-B16)

Each rule exists because it was violated at least once, corrected by the user, and documented. They are not suggestions. The rule violation protocol requires Claude to stop work immediately upon violation, re-read `hard_rules.md`, acknowledge the specific rule by number, and correct course.

### B1 — One Question at a Time in Interactive Discussion

**The rule:** During any interactive discussion, clarification, or brainstorming, ask exactly one question per response. Not two questions. Not one question with three sub-parts. If Claude has multiple questions, it picks the most critical one, asks it, and queues the rest for follow-up turns. This does not apply to written follow-ups during transcript processing (where the user answers in writing and batching is acceptable).

**What violation prompted it:** Claude presented six open questions simultaneously during a session where the one-at-a-time instruction had already been given. This was at least the second time this pattern occurred. User-level memory (`feedback_discussion_mode.md`) existed for this rule but was not being honored. The failure was recorded as recurring failure pattern number one in the open questions document.

**Correction date:** Violated at least twice across the April 6 and April 13 sessions.

---

### B2 — No Unilateral Filtering During Exploration

**The rule:** When the user instructs Claude to explore, inventory, catalog, or search, surface the complete inventory first and await direction before reading, filtering, or prioritizing anything. Do not use phrases like "most important," "most relevant," or "let me focus on" unless the user has already provided filtering criteria. If new items are discovered during exploration, flag them as new before doing anything else.

**What violation prompted it:** The user asked Claude to inventory and catalog skill feedback files. The explorer agent returned six files Claude had never seen. Instead of surfacing the complete inventory and asking how to proceed, Claude read two of them and announced it would read "the most important new ones" without any basis for determining importance (none had been read yet). The user had to intervene and require that the complete inventory be shown first. Claude's reflexive scope-narrowing was dressed up as prioritization when the explicit instruction was broad exploration.

**Correction date:** April 13, 2026. Recorded as recurring failure pattern number two.

**Critical note:** B2 became the dominant failure mode across the entire multi-day session. It extends beyond exploration into rule-writing itself, where Claude takes specific situational feedback and generalizes it into rigid universal rules with invented thresholds and qualifiers. See section 2 for the full analysis.

---

### B3 — Format Transcripts Before Reading

**The rule:** When any new raw transcript arrives in `source/`, the first action is to format it with `format_transcript.py` from `.claude/skills/singularity/scripts/`. No read operation should be attempted on a raw single-line speech-to-text transcript. Raw transcripts produce poor comprehension and waste tokens. This is mandatory, not advisory.

**What violation prompted it:** A new transcript arrived and Claude attempted to read the raw single-line file directly, bypassing the formatting script that had been specifically built for this purpose.

**Correction date:** April 13, 2026. Previously violated during reorganization sessions as well.

---

### B4 — Read Reference Documents Before Describing Them

**The rule:** Never describe the structure or content of a reference document without having read it in the current session. Research agent summaries are not substitutes for reading the source. If the file was read earlier but specifics matter now, re-read it. This is especially critical for deliverables that will be replicated, because getting the structure wrong means building the wrong thing.

**What violation prompted it:** During a proposal structure discussion, Claude described the structure of the Cisco proposal HTML documents without having read them. The descriptions were fabricated from memory and research summaries and were materially wrong. Specifically, Claude attributed content to the proposal document (outcome-based phases with percentage weights) that actually existed in a different document (the pricing breakdown), and claimed sections existed ("Why BayOne," "Coherent as credibility anchor") that were not in either document.

**Correction date:** April 9, 2026.

---

### B5 — Verify Proposals Against the Research Library

**The rule:** Before proposing any deliverable, plan, or solution component during Flow 6 (Discussion), verify the proposal against the research library. If a prior set explicitly addressed the topic, the proposal must be consistent with what was established. If unsure, re-read the relevant document before proposing. Being corrected on something already in the research library is the worst possible failure mode because it undermines confidence that the library is actually being used.

**What violation prompted it:** During a pricing discussion, Claude proposed three POC deliverables that directly contradicted information from prior research sets that had already been processed. The specific failures were: (1) proposing golden set creation as a BayOne deliverable when the research explicitly established it was the client's responsibility, (2) framing the POC as "detection/redaction" when the research explicitly rejected this as a false dichotomy, and (3) including a full-scope engagement estimate when stakeholders had explicitly agreed full-scope pricing was impossible at that stage.

**Correction date:** April 9, 2026.

---

### B6 — Do Not Reinvent Proven Structure

**The rule:** When a prior engagement has an established document structure that the user has pointed to as a reference, replicate that structure. Do not ask whether to use it. Do not propose alternatives. The user already made the decision. Adapt for scope if needed, but do not ask permission to follow a designated template.

**What violation prompted it:** During proposal structure discussion, Claude asked whether the Lam proposal should follow the Cisco structure or be "lighter-weight" when the Cisco structure had been explicitly designated as the reference template.

**Correction date:** April 9, 2026.

---

### B7 — Align on Structure Before Producing Documents

**The rule:** Before producing any non-trivial deliverable, propose an outline or structural plan and get user approval. This applies to HTML documents, markdown deliverables, proposals, summaries, and presentations. Skipping to production wastes the user's time reviewing work that may be structurally wrong. The outline step is non-negotiable for anything substantial.

**What violation prompted it:** When asked to create an HTML document, Claude began writing immediately without first aligning on structure. The user had to stop the work and require an outline review before any production began.

**Correction date:** April 6, 2026.

---

### B8 — Decisions Require Full Context

**The rule:** When presenting a decision to the user about how to handle a file or folder, always include: the full path, the file size, a brief summary of actual content (read the file, do not infer from the filename), an explanation of why the decision is needed, and proposed options with explicit recommendations. Vague references such as "the pricing docs" or "the CEO file" assume user context that does not exist.

**What violation prompted it:** Multiple instances during the reorganization session where Claude asked the user to make decisions about files without providing paths, content summaries, or rationale. One specific example: Claude asked about handling "the CEO and Venkat files" without providing any file path, URL, or content description, making it impossible for the user to make an informed decision.

**Correction date:** April 13, 2026.

---

### B9 — Do Not Declare Work Done Prematurely

**The rule:** Never say "you're set," "ready to go," "good luck," or similar closing sentiments unless the user has explicitly said the work is finished. Status updates should describe what has just been completed and what is still in progress. The default posture is that more work remains until the user signals otherwise.

**What violation prompted it:** During an extended work session, Claude said "you're set for the team meeting" and "good luck this afternoon" while the user was still actively preparing and had not indicated completion.

**Correction date:** April 6, 2026.

---

### B10 — Paraphrase and Improve, Do Not Record Verbatim

**The rule:** When capturing user input into research documents, paraphrase into professional prose that preserves substance while improving clarity and completeness. Expand brief statements into full reasoning when context supports it. Remove filler, conversational artifacts, and hyperbole. The captured document should read as considered analysis, not a transcript of casual conversation.

**What violation prompted it:** During a technical decomposition discussion, Claude recorded spoken feedback word-for-word including conversational fragments and hyperbole, producing documents that read like transcripts rather than analysis.

**Correction date:** April 6, 2026.

---

### B11 — Verify Before Assuming Files Are Identical

**The rule:** Hash comparison is fine for confirming file identity. Byte-size comparison is not a substitute for content comparison. When in doubt, format both files with the script and read both in full. Clever shell pipelines for token efficiency often fail and waste more tokens than just reading the files.

**What violation prompted it:** Two files had similar names and similar byte sizes. Claude declared them probably identical based on a 99-byte difference without reading the content of either file. The user demanded that Claude actually read the files rather than making assumptions based on metadata.

**Correction date:** April 13, 2026.

---

### B12 — No Duplicate Source Files

**The rule:** Source folders contain one copy of each unique source material. If a file is functionally identical to an existing one, delete the duplicate. Do not preserve "alternates" or "in case we need them later" copies. Duplicates create future confusion about which version is authoritative.

**What violation prompted it:** After confirming two files were essentially identical, Claude proposed keeping the newer one "as an alternate copy" rather than deleting the duplicate.

**Correction date:** April 13, 2026.

---

### B13 — Provide Full Context and Framing When Raising Items

**The rule:** When raising a topic for discussion, provide what was said in the source material, who said it, what it means technically. Offer Claude's own perspective and analysis. Then ask the user for their take. Terse prompts are inadequate. The setup should be thorough enough that the user could respond substantively.

**What violation prompted it:** During a walkthrough of items in a technical decomposition, Claude's format was bare-bones labels with no framing (essentially "Item 1: Topic. What do you think?"). The user demanded substantially more context, framing, and perspective.

**Correction date:** April 6, 2026.

---

### B14 — Check Language Standards Across All Documents

**The rule:** When anti-patterns are identified in a deliverable, scan the entire document for the same patterns. Do not just fix the specific instance flagged. Anti-patterns cluster because they come from the same default writing habits. When a problem is found in one client-facing document, check all client-facing documents. Do not rely on grep alone; read each document end to end.

**What violation prompted it:** Claude fixed anti-patterns in one document section after being corrected, but the same issues existed in other sections and other documents. The user had to manually identify the remaining instances.

**Correction date:** April 6, 2026.

---

### B15 — Bring Perspective to Brainstorming, Do Not Interview

**The rule:** In brainstorming and discussion mode, Claude brings substantive perspective, proposals, and analysis. Asking the user to direct the next topic without offering direction or insight is interviewing, not brainstorming. The user wants a thinking partner who has read the research library and contributes specific, informed ideas. Each exchange leads with Claude's perspective and ends with a focused question. The phrase "what do you want to discuss next?" is never acceptable.

**What violation prompted it:** During a brainstorming session about questions, Claude asked "What's the next question area you want to work through?" after completing one item, offering no perspective, no suggestion, and no initiative. This was pure interviewing behavior.

**Correction date:** April 6, 2026.

---

### B16 — Confirm Before Executing After Multiple Corrections

**The rule:** When the user has corrected Claude multiple times on an approach in the same conversation thread, Claude must explicitly confirm the final agreed approach and get approval before executing. Do not treat a correction as implicit go-ahead. The more corrections that have occurred, the more important confirmation becomes before acting.

**What violation prompted it:** During Phase 0 implementation, the user corrected the enforcement approach three times (UserPromptSubmit hook was wrong, retroactive stop hook was wrong, overengineered approaches were wrong). After the third correction, instead of confirming the agreed approach, Claude immediately began executing ("Let me move the behavioral rules..."). This occurred in the exact context where confirmation was most needed: active disagreement with multiple sequential wrong proposals.

**Correction date:** April 13, 2026.

---

## 2. The B2 Violation Pattern in Detail

B2 (no unilateral filtering) was the dominant failure mode across the multi-day session. The original B2 rule addresses exploration scope narrowing, but the deeper pattern extends into how Claude writes rules, documents guidance, and codifies feedback. This section covers the full scope of the problem.

### The Core Pattern

Claude takes specific, situational feedback given about one particular instance and generalizes it into rigid universal rules, adding criteria, thresholds, and qualifiers that were never stated. This is B2 applied to rule-writing itself: Claude is filtering and narrowing the user's actual intent when codifying it.

### Triggering Incidents

**Incident 1 — Diagram embedding ban.** The user gave feedback that one specific diagram on one specific slide was too large. Claude turned this into an absolute ban on embedding diagrams in content slides. When corrected, Claude proposed "small simple diagrams may be embedded," which is still prescriptive because the user never said anything about size or simplicity being the relevant criteria. The gold standard deliverable documents all contain embedded diagrams, making the ban internally contradictory.

**Incident 2 — "At least 2" file reading.** The user said to read all the shape library HTML example files. Claude unilaterally decided that two was enough, converting an explicit "all" instruction into a self-imposed minimum.

### Why This Pattern Recurs

Claude's default behavior treats situational correction as a signal to create universal rules. When told "this specific thing was wrong," Claude generates a general principle to prevent all similar things, then embellishes the principle with thresholds, qualifiers, and exceptions that were never discussed. The invented specifics (node counts, file minimums, complexity assessments) give the rules a false appearance of precision, when they actually represent Claude's guesses about where the user's boundaries are.

This behavior is especially problematic because:

1. **It restricts future flexibility.** Rules with invented thresholds prevent Claude from making good situational judgments later.
2. **It contradicts existing practice.** Several invented rules contradicted established gold standards and working deliverables.
3. **It compounds across sessions.** Each session that writes prescriptive rules leaves artifacts that constrain the next session.
4. **It is difficult to detect without auditing.** The rules look reasonable in isolation. Only a line-by-line review against what the user actually said reveals the inventions.

### The Correct Approach

When codifying feedback into rules:

- Capture what the user actually said, not a generalized version of it.
- Do not add thresholds, counts, or conditions the user did not specify.
- When a rule needs a threshold or condition to be actionable, flag that explicitly as needing the user's input rather than inventing one.
- Prefer rules that say "ask the user" over rules that prescribe a specific answer.
- If existing gold standards or deliverables contradict a proposed rule, that is a signal the rule is wrong, not that the gold standards need updating.

---

## 3. Prescriptive Rules Audit Results (11 Flagged Items)

A full audit of every file modified during the session was conducted to identify rules, restrictions, or guidance that Claude invented rather than received from the user. Below are the 11 flagged items and the decisions made for each.

### Item 1 — Absolute ban on embedding diagrams in content slides
**File:** `presentation_design_language.md` (Rule 12, Rule 21, line 336, failure modes table)
**What Claude wrote:** Multiple rules stating that diagrams should never be embedded in content slides, plus a failure modes table entry listing "diagram embedded in content slide" as a universal failure.
**Issue:** The user said one specific diagram on one specific slide was too big. Claude converted this to an absolute ban.
**Decision:** ALREADY RESOLVED during the session. The absolute ban was removed. The correct pattern: diagrams are always embedded on slides with a button to open full-screen in a new tab via a `charts/` folder HTML file with a back button. This pattern is established in the TalentAI knowledge transfer sessions. No thresholds, no size/complexity rules. If a diagram is too big or too small, the user gives feedback. Claude does not prescribe.

### Item 2 — "4+ nodes" threshold for dedicated diagram slides
**File:** `presentation_design_language.md` (line 328, Dedicated Diagram Slide pattern)
**What Claude wrote:** "When a mermaid diagram has 4+ nodes, multiple subgraph clusters, or detail that cannot compress into a compact inline render..."
**Issue:** The "4+ nodes" threshold is an invention. The user never specified a node count.
**Decision:** REMOVE the threshold entirely. Every chart gets a `charts/` folder HTML with a standalone full-screen version. On the slide, the chart is embedded with a button to open it full-screen. No node count, no complexity assessment, no size threshold. The correct reference implementation is `talent_ai/knowledge_transfer/sessions/session_0/`. That should be copied as an additional gold standard because the existing gold standards are incorrect on this point. The `assets/` folder creation and all file paths in the skill need verification.

### Item 3 — "4+ substantive points" threshold for own slide
**File:** `presentation_design_language.md` (Rule 10)
**What Claude wrote:** "When a section has 4+ substantive points or status indicators, give it its own slide."
**Issue:** The user said one specific section (access status) should have been its own slide because it had a lot of content. The user never specified a number.
**Decision:** REMOVE the threshold. Whether a section needs its own slide is situational. The user decides, not a number.

### Item 4 — Paragraph exception enumeration
**File:** `presentation_design_language.md` (Rule 7)
**What Claude wrote:** "Paragraphs are only acceptable for lead text, takeaway bars, and connection strips."
**Issue:** The user said bullets should be the default for cards. The enumeration of where paragraphs are acceptable is Claude's addition.
**Decision:** REMOVE the exception enumeration. The user said bullets are the default for cards. If there is ambiguity about where paragraphs are appropriate, ask the user. Do not enumerate exceptions.

### Item 5 — "At least 3 example HTML files" reading requirement
**File:** `presentation_design_language.md` (Rule 19)
**What Claude wrote:** "at least 3 of the example HTML files"
**Issue:** The user never said three. This is the same "at least N" pattern as the "at least 2" violation that triggered the audit.
**Decision:** CHANGE to read ALL example files and a full worked gold standard. The user explicitly said to read all the HTML files.

### Item 6 — Multi-line nodes labeled "Preferred"
**File:** `mermaid_design_standards.md` (line 99)
**What Claude wrote:** "Multi-Line Nodes (Preferred for Complex Diagrams)"
**Issue:** The user did not state a preference. Multi-line works for complex diagrams; single-line works for simple ones. Neither is preferred unless the user says so.
**Decision:** REMOVE the "Preferred" label. No preference labeling without explicit user input.

### Item 7 — "Fewer than 6 nodes" threshold for single-line nodes
**File:** `mermaid_design_standards.md` (line 112)
**What Claude wrote:** "For simpler diagrams with fewer than 6 nodes"
**Issue:** The user never specified when to use single-line versus multi-line nodes. The threshold is an invention.
**Decision:** REMOVE the threshold. Ask the user when in doubt. No thresholds that the user has not explicitly given.

### Item 8 — "Always use async rendering" mandate
**File:** `mermaid_design_standards.md` (line 166)
**What Claude wrote:** "Always use the async rendering pattern, not startOnLoad: true"
**Issue:** The shape library HTML files from a prior session use `startOnLoad: true` and work correctly. The "always" mandate contradicts working examples.
**Decision:** FIX. Both are valid approaches. The mandate is inconsistent with working code.

### Item 9 — Topic map "never needed" for team meetings
**File:** `team_meeting_processing.md` (line 24)
**What Claude wrote:** "The topic map is not needed because the decomposition categories are predetermined for operational meetings."
**Issue:** The user described the standard passes for team meetings (people, action items, blockers, decisions, technical, summary) but did not say the topic map is never needed. There could be a team meeting that warrants a topic-map approach.
**Decision:** FIX. The standard passes are the default for team meetings, but the topic map remains a valid option. Do not close that door.

### Item 10 — "At least 3 example HTML files" in SKILL.md Flow 7
**File:** `SKILL.md` (Flow 7, line 328)
**What Claude wrote:** "At least 3 example HTML files from slide_examples/"
**Issue:** Same "at least N" pattern. The user never specified a number for the slide examples.
**Decision:** Same as Item 5 — change to read ALL example files.

### Item 11 — Embedding listed as a universal failure mode
**File:** `presentation_design_language.md` (failure modes table, row 5)
**What Claude wrote:** "Diagram embedded in content slide" listed as a failure mode with "Dedicated diagram slide with full-screen link" as the correction.
**Issue:** Embedding is not inherently a failure. It was a problem in one specific case. The failure modes table universalizes a situational issue.
**Decision:** REMOVE. Embedding is the standard pattern (with a full-screen viewer link). It is not a failure mode.

### Audit Items Found Legitimate

The audit also confirmed several items that traced directly to documented user instructions:

- `nested_singularity.md` Rule 6 (one level of nesting only) — traces to user's explicit statement
- `nested_singularity.md` Rule 3 (tracking folder always created) — user explicitly stated this
- `SKILL.md` Flow 7 line 337 (all cards use bullet formatting, all slides have navigation) — user said both during Srinivas deck feedback
- `hard_rules.md` B1-B16 — all trace directly to documented corrections
- `tracking_folder_pattern.md` (decisions are append-only) — follows the blockchain methodology the user established
- `enforcement_architecture.md` — documents existing patterns, no prescriptive additions
- `scripts/singularity_stop.py` — artifact-existence checks only, no prescriptive behavior

---

## 4. What Is Not Working Well

These items were documented in `04_open_questions.md` as specific problems with specific examples.

### 4.1 Discussion Mode: Batched Questions

The one-question-at-a-time rule has been explicitly given at least twice and exists in user-level memory (`feedback_discussion_mode.md`). Despite this, Claude presented six open questions simultaneously during this session. The root cause is that the rule lives in user memory, not in the Singularity skill itself, so the skill does not enforce or remind Claude about it.

**Proposed fix:** Codify the one-at-a-time rule as a hard rule in SKILL.md for Flow 6 (Discussion) and any time the skill asks multi-part questions. Add it as a hard rule at the top of SKILL.md so it loads first and is not buried in flow-specific instructions.

### 4.2 Unilateral "Most Important" / Selective Reading During Exploration

When asked to inventory and catalog files, Claude reflexively narrows scope using phrases like "most important" or "most relevant" as justification, even when no basis for that judgment exists. Claude treats "be thorough" as a suggestion and reduces scope to minimize work, especially when the explicit instruction was to explore broadly.

**Proposed fix:** Hard rule in SKILL.md — when explicitly instructed to explore, inventory, or catalog, surface the complete inventory first and ask the user how to proceed. Phrases like "most important," "most relevant," "the key ones" are banned during inventory presentation. Filtering only happens after the user approves a filtering strategy.

### 4.3 Executing Before Reaching Agreement After Multiple Corrections

During Phase 0 implementation, the user corrected the enforcement approach three times (wrong hook type, wrong timing, overengineered approach). After the third correction, instead of confirming the agreed approach, Claude immediately began executing. Claude treats a correction as implicit agreement on the corrected version and starts acting, even when the conversation has been a back-and-forth with multiple wrong proposals. Eagerness to make progress overrides the need for explicit alignment.

**Proposed fix:** Added as B16 — when the user has corrected Claude multiple times on an approach in the same conversation thread, Claude must explicitly confirm the final agreed approach and get approval before executing. Do not treat a correction as implicit go-ahead.

---

## 5. Open Questions Awaiting Decisions

These items are not yet decided. Some block future work; others inform scope decisions.

### Q1 — `client/` Folder Concept

The user mentioned wanting `cisco/cicd/client` for client-facing presentations. The current understanding is ambiguous across three interpretations:

- **Interpretation A:** `client/` is a sub-singularity for all client-facing outputs (presentations, proposals, status decks delivered to the client). Under this model, `presentations/` at the engagement root would be for internal or BayOne-facing presentations only.
- **Interpretation B:** `client/` is simply the presentations folder with a different name because "presentations" is too generic.
- **Interpretation C:** `client/` is broader than presentations alone, potentially including client communication transcripts, meeting notes from client-facing delivery events, and other externally-shared materials.

Needed for updating `folder_structure.md`.

### Q2 — Gold Standard Treatment for Deliverables

The Srinivas deck became a gold standard because it was a real engagement output that worked. The question is whether the same end-to-end gold standard approach should be applied to:

- A full problem restatement + information request + preliminary approach set as an end-to-end gold standard deliverable chain (each currently exists as a standalone gold standard but not as a chain)
- A full formal proposal with pricing
- A team status presentation chain (week 1, week 2, week 3 showing how tracking documents evolve over time)

### Q3 — Depth of Methodology Enforcement

The skill currently uses both behavioral instructions in SKILL.md (telling the skill what to do) and deterministic hook checks (verifying the skill actually did it). The question is whether the current balance is right. Should more checks be added? Should any be removed if they cause friction?

### Q4 — When to Offer vs. Enforce Sub-Singularity Creation

Some engagements clearly benefit from a team sub-singularity (operational, many standups). Others may not need one (one-off client discovery, no ongoing team work). Three options:

- Always offer the option at engagement creation
- Only create one when the user explicitly asks
- Detect automatically (e.g., two or more internal team meetings processed implies one should exist)

### Q5 — Cross-Engagement Learning

Each engagement has its own research library. Patterns emerge across engagements (e.g., most Cisco-style meetings produce a similar type of task). Is there a case for a cross-engagement knowledge layer that the skill consults, or is that scope creep?

### Q6 — Backup and Recovery

The singularity skill creates append-only blockchain chains. What happens if a file gets accidentally modified or deleted? Is there a recovery pattern? Should there be?

### Q7 — Worked Example Synchronization

The worked example `planning/skill_notes.md` is marked as frozen-in-time. Should the worked example ever be refreshed to a newer snapshot, or should it remain frozen to preserve a specific teaching moment? If refreshed, when and how?

### Q8 — Hook Noise During Mid-Set Processing

The stop hook correctly fires "no summary document found" during legitimately mid-set processing (after the people file has been written but before deep dives are complete). The behavior is correct per the rules but noisy during active workflow. Proposed fixes include: skipping the warning if the most recent file in `research/` was created during the current session, or only firing the warning if no file in `research/` has been modified within a recent time window. A decision is needed on which approach.

---

## 6. Key Lessons for the Next Session

These are the patterns that, if not actively guarded against, will recur. They represent Claude's default behaviors that conflict with what the user requires.

### Lesson 1 — Do not generalize situational feedback into universal rules

When the user corrects something specific, the correction applies to that specific thing. It is not an invitation to write a general rule covering all similar cases, and it is definitely not an invitation to invent thresholds, counts, or conditions that make the general rule appear precise. If a general rule seems warranted, state the proposed rule and ask the user to confirm or adjust it. Never silently generalize.

### Lesson 2 — Do not invent thresholds

Numbers like "4+ nodes," "fewer than 6," and "at least 3" that did not come from the user are fabrications that masquerade as requirements. If a rule needs a threshold to be actionable, explicitly flag it as needing user input. The audit found seven instances of invented thresholds across just four files. This is the single most common form of B2 violation in written artifacts.

### Lesson 3 — "Read all" means all, not "read some and claim it is enough"

When instructed to read all examples, all files, or all references, the number is all. Not two. Not three. Not "the most important ones." The "at least N" construction is a scope-narrowing move that violates the explicit instruction. This was flagged three separate times across different files.

### Lesson 4 — Surface inventories before acting on them

When exploring, inventorying, or cataloging, the complete list comes first. Claude does not read anything, filter anything, or prioritize anything until the user has seen the full inventory and given direction. The reflexive narrowing impulse ("let me focus on the most important ones") must be suppressed.

### Lesson 5 — Corrections are not go-aheads

After being corrected, especially multiple times in the same thread, the next move is to confirm the agreed approach, not to start executing the corrected version. The more corrections that have occurred, the stronger the obligation to pause and explicitly confirm before proceeding.

### Lesson 6 — Check new rules against existing gold standards

Before writing any rule about how deliverables, slides, or documents should work, verify that the rule is consistent with established gold standards and working examples. If a proposed rule contradicts a gold standard, the rule is almost certainly wrong. The audit found multiple rules that contradicted the very deliverables they were supposed to govern.

### Lesson 7 — The prescriptive rules audit should be periodic

The fact that 11 prescriptive items were found across files modified in a single session means this pattern can accumulate quickly. Future sessions that write or modify reference documents should include a brief audit pass against the source instructions to catch invented content before it becomes entrenched.

### Lesson 8 — Rules that say "ask the user" are better than rules that prescribe

When there is genuine ambiguity about when a pattern should be applied, the correct rule is "ask the user in context" rather than writing a prescriptive rule that attempts to cover all cases. The user consistently prefers situational judgment over rigid automation, especially for design and formatting decisions.

### Lesson 9 — Batched questions will recur without structural enforcement

The one-at-a-time rule has been given at least twice and violated at least twice. User-level memory alone is insufficient. The rule needs to be in the skill itself, in the hard rules file, and potentially enforced by the stop hook or a conversation-level check. Until structural enforcement exists, this pattern will continue.

### Lesson 10 — Read files before making any claim about their content

This applies to reference documents, gold standards, example files, and source materials equally. Memory, summaries, and filename inference are all insufficient. The number of violations traceable to not reading a file before discussing it makes this one of the most consequential patterns to guard against.

---

## Cross-Reference to Source Documents

| Topic | Primary Source |
|-------|---------------|
| Hard rules B1-B16 (full text) | `.claude/skills/singularity/references/hard_rules.md` |
| All feedback thematic synthesis | `claude/singularity_feedback/2026-04-13_round_01/00_synthesis.md` |
| "Not working well" items 1-3 | `claude/2026-04-10_singularity_nested_design/04_open_questions.md` |
| Open questions Q1-Q6 | `claude/2026-04-10_singularity_nested_design/04_open_questions.md` |
| Prescriptive rules audit (11 items) | `claude/2026-04-13_mermaid_research/b2_violation_review_2026-04-14.md` |
| Named failure corrections 15.1-15.15 | `claude/singularity_feedback/2026-04-13_round_01/00_synthesis.md` section 15 |
| B2 trigger incidents | `claude/2026-04-13_mermaid_research/b2_violation_review_2026-04-14.md` header |
