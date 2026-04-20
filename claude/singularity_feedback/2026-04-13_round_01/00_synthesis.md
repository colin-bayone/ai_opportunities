# Singularity Feedback Synthesis — Round 01

**Round date:** 2026-04-13
**Sources synthesized:** 8 files under `sources/` (see `00_index.md` for inventory)
**Intent:** Exhaustive thematic consolidation. Every distinct rule, pattern, failure mode, and insight from the source files is captured here, with source attribution. No filtering for "importance." Future sessions can use this as a single comprehensive reference.

---

## How This Document Is Organized

1. **Hard Rules (Non-Negotiable Skill Behavior)** — Rules the skill must enforce every invocation
2. **Discussion and Interaction Behavior** — How Claude engages with the user during skill work
3. **Transcript and Source Material Processing** — How the skill handles input files
4. **Research Library and Blockchain Methodology** — Core structural rules
5. **People Tracking** — Dual model for people information
6. **Folder Structure and Organization** — Where things go
7. **Document Quality and Writing Standards** — Output quality rules
8. **Agent Architecture and File Writing** — How agents are used
9. **Discussion Capture (User + Claude Sessions)** — Capturing working discussions
10. **Deliverable and Presentation Creation** — Client-facing output rules
11. **Presentation Design Language** — The slide generation system
12. **Nested Singularity (Sub-Singularity) Pattern** — New architectural concept
13. **Reorganization of Existing Engagements** — State-based reorganization
14. **Stop Hook and Enforcement** — Deterministic verification
15. **Critical Failure Patterns (Named Corrections)** — Specific documented failures with dates
16. **Open Questions and Unresolved Items** — Items awaiting Colin's decision
17. **Source Attribution Map** — Which source contributed which items

Source citations use the source file number: [S1] = `01_lam_skill_notes_authoritative_2026-04-09.md`, [S2] = `02_reorganization_session_skill_issues_2026-04-13.md`, etc. Per-file contents are in the `sources/` subfolder.

---

## 1. Hard Rules (Non-Negotiable Skill Behavior)

These are the rules that must be enforced every time the Singularity skill is invoked. They are candidates for placement at the top of SKILL.md as Hard Rules or for enforcement via stop hook.

### 1.1 One Question at a Time in Discussion [S1, S8]

During any interactive discussion, clarification, or brainstorming:

- Ask ONE question per response. Not two. Not "one question with three parts."
- Do not use "let me ask a few questions" or similar multi-question framing.
- If Claude has multiple questions, pick the most critical one, ask it, and queue the rest for follow-up turns.
- This supersedes the older "max 5 questions per batch" rule for interactive discussions (that rule still applies to transcript processing follow-ups where the user can answer in writing).
- User-level memory for this exists at `feedback_discussion_mode.md` but has not been reliably honored. Codification in the skill itself is required.

**Recorded violations:** At least twice during this session. Explicitly called out in source 08 as recurring failure pattern #1.

### 1.2 No Unilateral Filtering During Exploration [S8]

When the user instructs Claude to explore, inventory, catalog, or search:

- Surface the complete inventory first.
- Wait for the user to direct reading/prioritization.
- Do not use phrases like "most important," "most relevant," "the key ones," or "let me focus on" during inventory presentation unless the user has provided filtering criteria.
- If the exploration finds items Claude did not previously know about, explicitly flag them as new discoveries before doing anything else.

**Recorded violation:** Once this session. Explicitly called out in source 08 as recurring failure pattern #2.

### 1.3 Format Transcripts Before Reading Them [S2]

When a new raw transcript arrives in `source/`:

- First action is to format it with `format_transcript.py` from `.claude/skills/singularity/scripts/`.
- No Read operation should be attempted on a raw single-line speech-to-text transcript.
- This is mandatory, not advisory. Raw transcripts produce poor comprehension and waste tokens.

### 1.4 Read Reference Documents Before Describing Them [S1, 2026-04-09 correction]

When describing the structure or content of any reference document (gold standard, prior deliverable, example file, etc.):

- Read the file in the current session before making specific structural claims.
- Research agent summaries are NOT substitutes for reading the source.
- If the file has already been read earlier in the conversation but specifics matter, re-read it.
- Especially critical for deliverables that will be replicated — getting structure wrong means building the wrong thing.

### 1.5 Use What Is Already in the Research Library [S1, 2026-04-09 correction]

Before proposing any deliverable, plan, or solution component during Flow 6 (Discussion):

- Mentally verify the proposal against the research library.
- If a prior set explicitly addressed the topic, the proposal must be consistent with what was established.
- If unsure, re-read the relevant document before proposing.
- Being corrected on something already in the research library is the worst possible failure mode because it undermines confidence that the library is being used.

### 1.6 Do Not Reinvent Proven Structure [S1, 2026-04-09 correction]

When a prior engagement has an established document structure that the user has pointed to as a reference:

- Replicate that structure.
- Do not ask whether to use it.
- Do not propose alternatives.
- The user already made the decision. Adapt for scope if needed, but do not ask permission to follow a designated template.

### 1.7 Align on Structure Before Producing Documents [S1, 2026-04-06 correction]

Before producing any non-trivial deliverable:

- Propose an outline or structural plan.
- Get user approval.
- Iterate on structure if needed.
- Then produce the document.
- Skipping to production wastes the user's time reviewing work that may be structurally wrong.
- Non-negotiable for HTML documents, markdown deliverables, proposals, and summaries.

### 1.8 Decisions Require Context, Not Just Names [S2]

When asking the user to decide about handling a file or folder:

- Include full path
- Include file size
- Include brief content summary (read the file — do not infer from filename)
- Explain why the decision is needed
- List proposed options with explicit recommendations

Vague references ("the pricing docs," "the CEO file") assume user context they do not have.

### 1.9 Do Not Declare Work Done Prematurely [S1, 2026-04-06 correction]

Closing language is reserved:

- Never say "you're set," "ready to go," "good luck," or similar unless the user has explicitly said the work is finished.
- Status updates describe what has just been completed and what is still in progress.
- Default posture: more work remains until the user signals otherwise.

### 1.10 Paraphrase and Improve Feedback, Do Not Record Verbatim [S1, 2026-04-06 correction]

When capturing user input into research documents:

- Paraphrase into professional prose.
- Preserve substance; improve clarity and completeness.
- Expand brief statements into full reasoning when context supports it.
- Remove filler, conversational artifacts, and hyperbole.
- Captured documents read as considered analysis, not conversation transcripts.

### 1.11 Verify Before Assuming Files Are Identical [S2]

When comparing two source files:

- Hash comparison is fine for confirming identity.
- Byte-size comparison is NOT a substitute for content comparison.
- Clever shell pipelines (diff + fold) often fail and waste more tokens than just reading both files.
- When in doubt, format both with the script and read both in full.

### 1.12 Never Keep Duplicate Source Files As Alternates [S2]

- Source folders contain ONE copy of each unique source material.
- If a file is functionally identical to an existing one, delete the duplicate.
- Do not preserve "alternates" or "in case we need them later."
- Duplicates create future confusion about which version is authoritative.

### 1.13 Provide Full Context and Framing When Raising Items [S1, 2026-04-06 correction]

When raising a topic for discussion:

- Provide what was said in the source material, who said it, what it means technically.
- Offer Claude's own perspective and analysis.
- Then ask the user for their take.
- Terse prompts ("Item X: Topic. What do you think?") are inadequate.
- Setup should be thorough enough that the user could respond substantively even without Claude's perspective, but Claude's perspective is always included.

### 1.14 Check Language Standards for Every Document, Not Just the Flagged One [S1, 2026-04-06 correction]

When anti-patterns are identified in a deliverable:

- Scan the entire document for the same patterns.
- Do not just fix the specific instance flagged.
- Anti-patterns cluster because they come from the same default habits.
- Finding one means others are likely present.
- When a problem is found in one client-facing document, check all client-facing documents, not just the one flagged. Do not rely on grep alone — read every document end to end.

### 1.15 Bring Perspective to Brainstorming, Do Not Interview [S1, 2026-04-06 correction]

In brainstorming and discussion mode:

- Claude brings substantive perspective, proposals, and analysis.
- Asking the user to direct the next topic without offering direction or insight is interviewing, not brainstorming.
- The user wants a thinking partner who has read the research library and contributes specific, informed ideas.
- Each exchange leads with Claude's perspective and ends with a focused question — never with "what do you want to discuss next?"

---

## 2. Discussion and Interaction Behavior

### 2.1 The Three-Step Pattern for Asking Questions in Discussion [S1]

When asking a question in a discussion, Claude must:

1. State what it already knows from the research library (specific details, not vague references).
2. Offer a perspective or suggestion based on that knowledge (e.g., "Based on how the Cisco POC was structured, I think X makes sense here because Y").
3. Then ask one focused question to validate, refine, or get the user's take.

Without perspective, Claude is just an interviewer. Claude has read every transcript, every pricing discussion, every bridge document — use that knowledge to contribute, not just to prompt.

### 2.2 Markdown Files Are the Persistence Layer [S1]

- Everything goes in markdown files first.
- Claude can rephrase or summarize in chat after writing to the file, but the file is the source of truth.
- Do not have substantive discussion exchanges that only exist in chat.
- The whole point of the blockchain methodology is that future sessions can reconstruct the full arc.

### 2.3 Write After Each Exchange [S1]

- If the user gives a long answer covering 5 topics, write those into the research docs immediately.
- Do not accumulate and dump at the end.

### 2.4 Internal vs External Language [S1]

- Capture everything honestly in internal research docs.
- Flag anything that should never appear in client-facing materials.
- Examples of internal-only: assessments of client competence, frustration with client's technical approach, competitive intelligence about prior partners.

### 2.5 Capture Reasoning, Not Just Conclusions [S1]

- The "why" behind a technical decision is as valuable as the decision itself for future sessions.

### 2.6 Flag Open Items Explicitly [S1]

- If the user says "this requires discovery" or "we need info from the sales team," that is an open item to track.

### 2.7 Do Not Sanitize [S1]

- If the user is blunt about a client's capability gaps or makes strong claims, capture that.
- It is part of the honest record.

### 2.8 Distinguish Hyperbole from Commitments [S1]

- When the user says something like "I could do this in a day," that is confidence in feasibility, not a timeline.
- Do NOT repeat it as a planning estimate, reference it in proposals, or fixate on it as a deliverable timeline.
- Capture the sentiment, not the literal claim.

### 2.9 Use "Continued" Files When Discussions Extend [S1]

- If a discussion naturally extends beyond a single document, use "continued" files.
- Each file should cover a coherent chunk.

---

## 3. Transcript and Source Material Processing

### 3.1 Speech-to-Text Quality [S1]

- Transcripts are almost always speech-to-text.
- They will be full of errors: misspelled names, garbled technical terms, sentence fragments, speaker misattribution.
- Agents must apply common-sense interpretation.

**Examples from Lam engagement:**
- "concept-renade" = "confidential violation"
- "lamb GPT" = "LamGPT"
- "Spacey" = "SpaCy"
- "on pram" = "on-prem"
- "kills that guy" = "builds that out"
- "brass beam" = "Brad's team"

### 3.2 Multi-Pass Reading (Critical Processing Rule) [S1]

Do NOT read a transcript once and try to produce everything from a single pass.

1. **Pass 1 — High-level overview.** Read the entire transcript. Identify major topics. Write these down as an outline/topic list. This becomes the roadmap.
2. **Pass 2+ — Per-topic deep dives.** Read again focusing on ONE topic at a time. Write the documentation after that focused read. Then read again for the next topic.
3. **Write after every read, not once at the end.**
4. **Agent opportunity.** Each per-topic pass can be dispatched as a separate agent for parallelization.

**Why multi-pass:**
- Clears context between topics so each gets full attention
- Prevents the "everything blurs together" problem of single-pass
- Produces better-organized output because each file is written with focused intent
- Catches details that would be missed in a single sweep

### 3.3 Standard Processing Order for Transcripts [S1]

1. People file first (who's there, what do we know)
2. High-level topic overview (pass 1)
3. Per-topic deep dives (passes 2+, one topic per pass, write after each)
4. Any additional requested files (business opportunity, speaker notes, etc.)
5. "What Changed" bridge document (last)
6. Summary (very last)

### 3.4 Standard Files Per Set [S1]

**Always created:**
- People file (for transcript-based sets)
- Summary (last file)
- Bridge / "What Changed" document (also written last, retrospective between two existing sets)

**Variable files (ask the user):**
- Technical deep dive breakdown (by topic)
- Business opportunity and specific notes
- Meeting breakdown and speaker notes
- Action items / next steps
- Hypothesis validation (confirmed/invalidated from prior sets)

The user knows what matters. Ask, do not assume.

### 3.5 Source File Integrity [S2]

- Source folders contain ONE copy of each unique file.
- No duplicates, no alternates, no backups.
- If unsure whether two files are the same, format both and read both in full.

---

## 4. Research Library and Blockchain Methodology

### 4.1 Blockchain Rules [S1]

- Research documents are append-only.
- Once written, never edit.
- New understanding goes in new documents that reference earlier ones.
- The org chart is the only living document (deliberate exception, because it is a current-state reference).

### 4.2 Numbering Is Purely Chronological [S1]

- There is nothing special about what number a set gets.
- 01 is not always "call prep," 02 is not always "a meeting," 03 is not always "a discussion."
- The number reflects when in the project timeline the material was created or processed.
- Content type determines filenames within the set, not the set number.

### 4.3 Supplementary Material Uses Letter Suffixes [S1]

When supplementary material is tied to the same event as an existing set:

- `02_meeting_*` = the meeting itself
- `02a_debrief_*` = internal debrief after the same meeting
- `02b_followup_email_*` = a follow-up email about the same meeting

This keeps it clear that supplementary material is event-adjacent, not a new chronological step. Same blockchain rules apply.

### 4.4 Filename Convention [S1]

- Include dates in filenames when the source date is known.
- Example: `01_call_prep_situational_context_2026-03-12.md`
- Makes chronological ordering unambiguous even outside the numbering system.

### 4.5 Methodology Doc Is Always First [S1]

- Every engagement starts with `00_methodology_<date>.md`.
- Explains the decomposition approach and why it was chosen.
- Any future reader (human or Claude) can read it and understand the rules before reading content.

### 4.6 Summary Is Always Last [S1]

- Every document set ends with a summary.
- Short, high-level, references all files in the set.
- Lets a future session understand the set without reading every file.

### 4.7 Bridge Documents Are Retrospective [S1]

- Do not try to write "what changed between two sets" while still processing them.
- Written after both sets exist.
- Captures: hypotheses validated/invalidated/open, what we got wrong, what we got right, new information, questions answered.

### 4.8 Read Prior Context Before Processing New Material [S1]

- Before decomposing a new document, read:
  1. The previous summary
  2. The current org chart
- Ensures continuity and avoids re-discovery of known information.
- The skill should enforce this as a step.

### 4.9 The System Is Self-Describing [S1]

- A new Claude session with zero context should be able to read the methodology doc, then summaries in order, and reconstruct full engagement state.
- No tribal knowledge required.

### 4.10 Don't Use a Single Massive File [S1]

- Break decomposition into purposeful groupings with distinct reasons to exist separately.
- Do not go so granular that there's a file per paragraph.
- Each file needs a clear reason to be its own thing.

---

## 5. People Tracking

### 5.1 Dual Model [S1]

Track people in two places:

1. **Per-meeting blockchain-style people document.** Captures what was learned about people from that specific event. Immutable.
2. **Living org chart at the session root.** Always current. Quick-reference truth.

The blockchain version preserves history; the org chart is for quick reference.

---

## 6. Folder Structure and Organization

### 6.1 Core Engagement Structure [S1, S2]

```
/<client_name>/<opportunity_name>/
├── org_chart.md
├── source/
├── research/
├── planning/
├── pricing/
├── deliverables/
├── presentations/
├── decisions/
└── progress/
```

### 6.2 Distinctions Between Deliverables, Presentations, and Planning [S2]

The working rule settled on during the 2026-04-13 reorganization session:

- **deliverables/** = Client-facing documents (multi-page, narrative, sent to client or shared internally as polished artifacts).
- **presentations/** = Slide decks (individual slides meant to be presented or walked through).
- **planning/** = Internal-only documents (meeting summaries for BayOne use, prep notes, session handoffs).

### 6.3 Flow 4 (Create Deliverable) Should Ask Client-Facing vs Internal [S2]

- Currently the skill assumes everything in deliverables/ is client-facing.
- The flow should ask and route accordingly.
- Internal-only documents should be in planning/, not deliverables/.

---

## 7. Document Quality and Writing Standards

### 7.1 Absolute Rules for Client-Facing Content

These apply to all client-facing deliverables (captured across sources):

- No em dashes. Use commas, periods, "and," or parentheses.
- No direct quotes. Never put quotation marks around something someone said. Paraphrase as organizational knowledge.
- No individual names. Frame as "the team," "the organization," "[Client]," or "BayOne."
- No contrastive framing. Never "It's not just X, it's Y" or "This isn't about X, it's about Y." State what something IS directly.
- No emojis. Zero, ever.
- No contractions. "Does not" instead of "doesn't," "we are" instead of "we're."

### 7.2 Tone Rules

- Never suggest the client is incompetent, even if internal assessment is harsh. Frame gaps as opportunities.
- Do not question organizational authority in writing.
- Come from a position of authority without arrogance.
- Call the solution a "solution," never a "product." Custom, tailor-made engagement, not off-the-shelf.

### 7.3 Scope Rules

- Stay within the stated problem.
- Preliminary work should be framed as preliminary.
- Acknowledge what you do not know.

### 7.4 Paraphrase Feedback, Do Not Record Verbatim [S1, 2026-04-06 correction]

Covered in §1.10.

### 7.5 Check Language Standards Across All Documents [S1, 2026-04-06 correction]

Covered in §1.14.

### 7.6 Salary / Rate Anonymization [S1]

- Never attribute salary or rate information to named individuals in internal documents.
- Use anonymized labels like "Onshore Resource (Lead Level)" on the Personnel and POC tabs.
- Team members do not need to know each other's compensation to understand the cost model.

### 7.7 Never Reference What You Are Withholding [S1]

- Saying "the investment does not vary based on internal resource allocation" draws attention to exactly the thing the client should not be thinking about.
- State what the pricing IS (fixed-price, outcome-based). Do not explain what it IS NOT.
- Defensive language raises the exact questions you are trying to avoid.

---

## 8. Agent Architecture and File Writing

### 8.1 Agent Write Permission Is Resolved [S1, 2026-03-20 update]

- With `"Write($CLAUDE_PROJECT_DIR/claude/**)"` in `permissions.allow` in `.claude/settings.local.json`, agents can write files fully autonomously.
- No user approval prompt required.
- Confirmed working with `mode: "bypassPermissions"` on agent spawns.
- The earlier "semi-auto mode" limitation is no longer the case.

### 8.2 Agent Behavior Rules [S1]

- Agents write files directly.
- Do NOT fall back to main-session sequential writing as a workaround.
- Do NOT attempt to extract agent output from temp files with scripts.
- The skill should pre-configure the Write permission as part of skill setup.

### 8.3 When to Use Agents [S1]

- Per-topic deep dives during transcript processing. Natural parallelization point.
- Research lookups for external information (Azure AI Foundry capabilities, Microsoft Purview, etc.).
- Re-exploration of existing research docs for specific details (e.g., "find all mentions of Azure services across all 02 files").

### 8.4 Research Agents as First-Class [S1]

- Research agents look up external information in context of the problem.
- The user may ask for this at any point.
- Can also re-explore existing decomposition docs.
- Going back to source material to verify or discover is always encouraged.

---

## 9. Discussion Capture (User + Claude Sessions)

### 9.1 Discussion Sessions Are a Valid Set Type [S1]

- One valid document set type is a working discussion between user and Claude to think through technical approach, strategy, or open questions.
- These get their own set number.
- Captured as they happen — write after each exchange, not at the end.
- The skill should support this as a mode.

### 9.2 Capture Rules for Discussions [S1]

Covered across §1.10, §2.2, §2.3, §2.4, §2.5, §2.6, §2.7, §2.8, §2.9 above.

---

## 10. Deliverable and Presentation Creation

### 10.1 Draft in Markdown First [from existing skill references, reinforced across sources]

- Always draft content in markdown first.
- User reviews substance before formatting.
- Markdown is the source of truth for content.

### 10.2 Convert to HTML Using Design System [from existing skill]

- Use BayOne design system for client-facing HTML.
- Reference the appropriate gold standard for style and structure.

### 10.3 Template vs Crafted [from existing skill]

- Gold standards are structural references, not fill-in-the-blanks templates.
- Deliverables are written from the research library using the design spec and gold standards as style guides.
- Engagement-specific, not template-shaped.

### 10.4 Slide Deck Proposal Before Generation [S6, S7]

- When creating a presentation, propose the slide list with descriptions of what each covers and the layout approach.
- Get user approval before generating HTML.
- These are not rigid template IDs — describe the layout in plain language.

---

## 11. Presentation Design Language

### 11.1 Design Language, Not Rigid Templates [S5]

- The presentation design language defines palette, typography, components, rules — not a closed set of layouts.
- Example slides in `assets/slide_examples/` are patterns to draw inspiration from.
- Layouts can be combined or new arrangements created that follow the design language.
- A well-designed slide that does not match any example exactly but follows the palette, typography, and component patterns is better than content forced into an ill-fitting layout.

### 11.2 Shared Foundation [S5]

- Font: Inter (Google Fonts), weights 300-700
- Icons: Font Awesome 6.5.1 (CDN)
- Aspect ratio: 16:10 (`aspect-ratio: 16 / 10`, max-width 1100px)
- Border radius: 12px (slide), 10px (cards), 7-8px (icon badges)
- Page background: `#e6e8eb`
- Standard shadow on slide container

### 11.3 Color Palette [S5]

```
--blue-darkest: #0c1929
--blue-dark: #15293e
--blue-mid: #1e3a5f
--blue-bright: #2563eb
--blue-accent: #3b82f6
--steel-light: #64748b
--steel-glow: #94a3b8
--primary: #0f172a
--text: #334155
--text-light: #64748b
--border: #e2e8f0
```

### 11.4 Gradient Progression System [S5]

Five-position progression for sequential cards/icons:

1. `#0c1929 -> #1e3a5f` (darkest, anchoring)
2. `#1e3a5f -> #2563eb` (dark to bright)
3. `#2563eb -> #3b82f6` (bright to accent)
4. `#3b82f6 -> #4f93f7` (accent to light)
5. `#4f93f7 -> #64748b` (light to steel)

Used when there are 3+ sequential peer elements.

### 11.5 Reusable Components [S5]

- Standard slide header (logo + context label)
- Footer bar (3px gradient strip)
- Card (icon + title + description, left or top accent bar)
- Definition bar (full-width dark gradient strip at content top)
- Takeaway bar (dark gradient strip at content bottom)
- Connection strip (takeaway bar variant used inside panels)
- Question block (wrong/right variants for argument slides)
- Bullet item pattern (`.items` / `.item` with blue-accent dot + bold lead + description)
- Slide navigation (prev/next/home, bottom-left, fixed)
- Embedded diagram with full-screen viewer link
- Standalone chart page with back button

### 11.6 Example Layout Patterns [S5]

Demonstrated in the example HTML files:

- Dark full-bleed (title, closing)
- Split panel (left explanation + right detail)
- Definition bar + content area
- Card grid (full width)
- Agenda / navigation row

### 11.7 Rules Codified From Srinivas Deck Experience [S6]

These emerged as lessons learned and must be in the design language spec:

- Bullet formatting (`.items` / `.item`) is the DEFAULT for all card bodies, not paragraph text.
- Navigation (prev/next/home) is MANDATORY on every slide in a multi-slide deck. First slide has prev disabled. Last slide has next disabled. Home always points to slide 00.
- When a section (access status, etc.) has 4+ substantive points, give it its own slide.
- Large diagrams go on their own dedicated slide, not embedded within content slides.
- No individual names in slide content. Presenter credit only on title and closing slides.
- No direct quotes from any person.
- Diplomatic framing: problems are "alignment needed" or "items for discussion," not conflicts.
- Architectural ideas are framed as preliminary or exploratory, not as finalized plans, unless confirmed.
- Content must use specific details from source material. Vague corporate language is a failure mode.
- Error on more slides rather than dense slides.
- No images or external media. Font Awesome icons only.
- Self-contained HTML per slide. Inline styles. CDN links for fonts and icons only.
- Content must fit without scrolling. Split into multiple slides if needed.

### 11.8 Mandatory Pre-Generation Reading [S5]

Before generating any HTML slide:

1. Read `presentation_design_language.md`.
2. Read at least 3 example HTML files from `assets/slide_examples/`.
3. (Planned) Read the Srinivas deck gold standard.

Enforced by stop hook verifying the reference files exist.

### 11.9 Embedded Diagram + Full-Screen Viewer Pattern [S5, S6]

For mermaid.js diagrams on slides:

- Slide embeds a compact inline render.
- Link "Open full-screen diagram" opens a standalone file in `charts/` subfolder in a new tab.
- Standalone chart file has a back button using `history.back()`.
- When diagram has 4+ nodes or multiple subgraphs, give the diagram its own dedicated slide rather than embedding.
- Reference implementation at `talent_ai/knowledge_transfer/sessions/session_0/` and in the Srinivas deck.

### 11.10 Slide File Naming [S5]

```
<deck_name>_<date>/
├── 00_title.html
├── 01_<descriptive_name>.html
├── 02_<descriptive_name>.html
├── ...
├── NN_closing.html
└── charts/
    └── <chart_name>.html
```

---

## 12. Nested Singularity (Sub-Singularity) Pattern

### 12.1 Concept [S4]

A sub-singularity is a self-contained singularity instance nested within a parent singularity. It has its own source, research, and numbering chain. Follows the same blockchain methodology but with processing focus tailored to its purpose.

### 12.2 When to Use [S4]

When an engagement has a distinct track of activity that:

- Has its own source materials
- Follows its own timeline
- Is supplementary to the main engagement narrative
- Could overwhelm the main chain if mixed in

Examples beyond team meetings:

- Parallel workstream within the same engagement (infrastructure vs application)
- Vendor evaluation research
- Training or onboarding materials processing
- Sub-team's independent discovery meetings
- Compliance or legal review track

### 12.3 Template [S4]

```
<sub_singularity_name>/
├── source/                  (raw input files, never modified)
├── research/                (blockchain chain, own numbering, append-only)
│   ├── 00_methodology_<date>.md
│   ├── 01_*
│   └── ...
├── tracking/                (living operational documents, always created)
├── documents/               (formatted outputs: HTML, reports, etc.)
├── planning/                (session handoffs, notes)
└── cross_reference.md       (maps to parent and sibling sub-singularities)
```

### 12.4 Rules [S4]

1. Each sub-singularity has its own independent numbering chain.
2. Blockchain methodology applies within each sub-singularity.
3. `cross_reference.md` is living.
4. Parent's `org_chart.md` is the single people reference.
5. Sub-singularities are peers, not nested further. One level only.
6. Each sub-singularity is self-contained for processing.
7. Convergence flows upward. Findings enter the parent chain as new sets when relevant.
8. Sub-singularity naming is descriptive and flat (`team/`, `team_cisco_syncs/`, `vendor_eval/`).
9. `tracking/` folder is always created.
10. `documents/` folder is standard.

### 12.5 Team Meeting Processing (First Instance) [S4, S6]

Standard passes for team meetings:

1. People and dynamics (first file, always)
2. Action items and assignments (including status of prior-set items)
3. Blockers, dependencies, escalations
4. Decisions made and rationale
5. Technical discussion (only when substantive technical content exists)
6. Summary (last file, always)

Differences from client-meeting processing:

- Topic map replaced with standard passes
- Post-processing: update `tracking/` files
- Living documents: multiple in `tracking/` folder
- Cross-reference updated after each set

### 12.6 Tracking Folder Dual Model [S4]

- `tracking/action_items.md` — open, completed, blocked items with status and source references
- `tracking/blockers.md` — active and resolved blockers with status and escalation path
- `tracking/decisions.md` — numbered log with rationale and source references

Dual model: research chain is the audit trail (immutable), tracking is the operational dashboard (living).

### 12.7 Cross-Reference File Format [S4]

```markdown
# Cross Reference: <Sub-Singularity> <> Main Chain

## By Team Meeting Set
| Team Set | Date | Main Chain Sets | Notes |
| ...      | ...  | ...             | ...   |

## By Topic Thread
| Thread | Team Sets | Main Sets | Status |
| ...    | ...       | ...       | ...    |
```

### 12.8 How to Add a New Sub-Singularity [S4]

1. Propose the sub-singularity name, purpose, and expected content.
2. Create the folder structure using the template.
3. Write `research/00_methodology_<date>.md`.
4. Create `cross_reference.md` with initial mapping.
5. Begin processing source materials.

### 12.9 Emerging Ideas (Not Yet Built) [S4]

- Master aggregation across sub-singularities (roll-up view of all tracking/ folders)
- Sub-singularity templates by type (operational, discovery, research, compliance)
- Automatic cross-referencing by topic overlap detection

---

## 13. Reorganization of Existing Engagements

### 13.1 Four Engagement States [S2]

- **State A: Never touched** — Raw folder with transcripts, notes, deliverables, no Singularity structure
- **State B: Partially done** — Some Singularity structure exists but content is incomplete or mixed
- **State C: Fully done, needs validation** — Complete Singularity structure but may have gaps or new content
- **State D: Multi-project folder** — Client folder containing multiple engagement subfolders

### 13.2 Four-Phase Approach [S2]

1. Explore and map (always first — inventory, identify projects, determine state)
2. Archive and structure (State A and D cleanup)
3. Process source materials (State A and B)
4. Validate (State B and C)

### 13.3 State C Validation Checklist [S2]

12-item checklist exists in `.claude/skills/singularity/references/reorganization_guide.md`. Applied to sephora/edw_modernization (10/12 pass) and lam_research/ip_protection (10/12 pass). Same two failures in both: empty pricing folder and missing session handoff.

### 13.4 Reorganization Is Not Greenfield [S2]

- The skill was originally built for greenfield engagements.
- Did not have guidance for reorganizing folders with partial structure, mixed content, or content needing to be archived vs integrated.
- `reorganization_guide.md` was created to address this.
- Should be officially incorporated as a new flow in SKILL.md ("Reorganize an existing engagement folder"), with detection of existing folder state routing to the appropriate flow.

### 13.5 Archive With Care [S2]

Before archiving any folder during cleanup:

- Run a comparison agent that identifies:
  - Source materials already captured in the active project
  - Source materials that are unique and need to be moved into the active project
  - Derived analysis that is superseded by the active research library
- Archive only what is fully accounted for.
- Naive "move to archive" can lose unique content.

Example: during sephora reorganization, 124 files of pre-Singularity analysis existed. 16 unique items (stakeholder dossiers, relationship analysis, action tracking) needed to be preserved before archiving.

### 13.6 Split Reorganization Into Validate vs Process Phases [S2]

Most common reorganization pattern: project mostly-Singularity with gaps (missing session handoff, unformatted source files, empty pricing, source files added since last processing). For these, full reprocessing is wasteful. Targeted gap-filling is right.

Validation checklist could become a runnable script, not just a reference.

---

## 14. Stop Hook and Enforcement

### 14.1 Current Checks [S2, S6]

The stop hook currently verifies:

- Methodology doc exists in `research/`
- Org chart exists (if research has started)
- Summary docs exist (if research files beyond methodology exist)
- Presentation design references exist (if presentation HTML is present)

### 14.2 Hook Noise During Mid-Set Processing [S2]

- Stop hook fires "no summary document found" during legitimately mid-set processing (after people file, before deep dives complete).
- Correct behavior per the rule but noisy during workflow.
- Proposed fixes:
  - Skip warning if most recent file in `research/` is dated within current session
  - Only fire warning if no file in `research/` has been modified within some recent window

### 14.3 Proposed Additional Checks [S6, S7]

- If sub-singularity folders exist, verify `references/nested_singularity.md` exists (once it exists)
- If presentation HTML exists, verify the Srinivas gold standard exists (once copied)
- If `charts/` subfolder exists, verify each chart file has a back button element
- If presentation HTML cards contain paragraphs instead of `.items` pattern AND exceed N words, flag as potential paragraph-in-card violation

---

## 15. Critical Failure Patterns (Named Corrections with Dates)

These are documented failures with specific dates and corrections. Each should be treated as a named anti-pattern the skill must prevent.

### 15.1 Claude Proposes Things Contradicting Research Library (2026-04-09) [S1]

**Context:** Pricing discussion. Claude proposed three POC deliverables that directly contradicted information from prior sets already read and processed.

**Specific failures:**
1. Proposed "golden set creation" as a BayOne deliverable when research explicitly established it was Lam's responsibility.
2. Framed the POC as "detection/redaction" when research explicitly rejected this as a false dichotomy.
3. Included "full-scope engagement estimate" when research explicitly documented stakeholders agreeing full-scope pricing was impossible.

**Rule:** Before proposing anything in Flow 6, verify against the research library. See §1.5.

### 15.2 Claude Describes Reference Docs Without Reading (2026-04-09) [S1]

**Context:** Proposal structure discussion. Claude described the structure of the Cisco proposal documents without having read the HTML files. Descriptions were fabricated from research summaries and were materially wrong.

**Specific failures:**
- Described the proposal document as having "outcome-based phases with percentage weights" — those were in the pricing breakdown document, not the proposal.
- Claimed the proposal included "Why BayOne" and "Coherent as credibility anchor" — neither existed in either document.

**Rule:** Read reference documents before describing them. See §1.4.

### 15.3 Claude Asks Whether to Follow a Designated Template (2026-04-09) [S1]

**Context:** Proposal structure discussion. Claude asked whether the Lam proposal should follow the Cisco structure or be "lighter-weight" — when the Cisco structure had been explicitly designated as the reference.

**Rule:** Do not reinvent proven structure. See §1.6.

### 15.4 Claude Declares Work Done Prematurely (2026-04-06) [S1]

**Context:** Extended work session. Claude said "you're set for the team meeting" and "good luck this afternoon" while the user was still actively preparing.

**User correction:** "Please stop thinking that we're done until I say that we're done. I will let you know whenever we are finished."

**Rule:** Closing language reserved for user signal. See §1.9.

### 15.5 Claude Records Feedback Verbatim (2026-04-06) [S1]

**Context:** Technical decomposition discussion. Claude recorded spoken feedback word-for-word including conversational fragments and hyperbole.

**User correction:** "I don't want you to record feedback verbatim. You should be paraphrasing and improving and expanding."

**Rule:** Paraphrase and improve. See §1.10.

### 15.6 Claude Interviews Instead of Brainstorming (2026-04-06) [S1]

**Context:** Question brainstorming session. Claude asked "What's the next question area you want to work through?" after completing one item.

**User correction:** "Why are YOU asking ME 'What's the next question area you want to work through?'. WE ARE BRAINSTORMING."

**Rule:** Bring perspective, not just questions. See §1.15.

### 15.7 Claude Provides Terse Prompts Without Framing (2026-04-06) [S1]

**Context:** Walking through items in technical decomposition. Claude's initial format: "Item 1: Presidio. What's your take?"

**User correction:** "Give me a lot more context and framing than this. This is piss poor. Also, offer your own perspective too."

**Rule:** Full context and framing. See §1.13.

### 15.8 Claude Skips to Production Without Outline Alignment (2026-04-06) [S1]

**Context:** Asked to create an HTML document, Claude began writing immediately without aligning on structure.

**User correction:** "You should probably put together an outline so that I can improve it before you waste my time showing me something that I did not agree to."

**Rule:** Align on structure before producing. See §1.7.

### 15.9 Claude Fixes Anti-Patterns in One Doc But Not Others (2026-04-06) [S1]

**Context:** Anti-patterns identified in one document. Claude fixed them in that document, but user had to manually identify same issues in other sections.

**Rule:** Scan all documents systematically. See §1.14.

### 15.10 Claude Reads Raw Transcript Without Formatting (2026-04-13) [S2]

**Context:** New transcript arrived. Claude tried to read the raw single-line file directly.

**User correction:** "Did you just try to read a single line transcript without running it through the script that we put together?"

**Rule:** Format transcripts before reading. See §1.3.

### 15.11 Claude Assumes Files Are Identical Based on Byte Size (2026-04-13) [S2]

**Context:** Two files with similar names and same byte size. Claude assumed they were duplicates based on "99 bytes different — probably trivial."

**User correction:** "You can't just read and say that it's 99 bytes bigger and therefore it's trivial. You need to actually see what's actually different there."

Followed by: "Just read the fucking files; they're not that long; it's not that hard."

**Rule:** Verify before assuming. See §1.11.

### 15.12 Claude Proposes Keeping Duplicate "Alternates" (2026-04-13) [S2]

**Context:** After confirming two files were essentially identical, Claude proposed keeping the new one "as an alternate copy."

**User correction:** "I specifically said no, do not keep two versions of the same file as an alternate."

**Rule:** No duplicates. See §1.12.

### 15.13 Claude Asks User to Decide About Files Without Showing Context (2026-04-13) [S2]

**Context:** Multiple times. Example: "What about the CEO and Venkat files?"

**User correction:** "I have no idea what they are because you just said 'CEO and backend files'. You didn't tell me a path or a URL, and you didn't tell me what content was contained inside."

**Rule:** Decisions need context. See §1.8.

### 15.14 Claude Presents Batched Questions in Discussion (at least twice, through this session) [S8]

**Context:** Colin previously instructed one question at a time. Claude presented 6 questions simultaneously in this session.

**Rule:** One question at a time. See §1.1. User-level memory exists but the skill does not enforce it.

### 15.15 Claude Performs Unilateral Filtering During Exploration (this session) [S8]

**Context:** Colin asked for inventory. Explorer returned 6 new files. Claude read 2 and said "let me read the most important new ones" without having read any to know what was important.

**Rule:** No unilateral filtering during exploration. See §1.2.

---

## 16. Open Questions and Unresolved Items

These items are not yet decided and block or inform future work.

### 16.1 `client/` Folder Concept [S8]

Colin mentioned wanting `cisco/cicd/client` for client-facing presentations. Three possible interpretations:

- **A:** `client/` is a sub-singularity for all client-facing outputs.
- **B:** `client/` is an alias for presentations/ with a more intuitive name.
- **C:** `client/` is something more — transcripts, notes, and presentations from client-facing delivery events.

Unresolved. Needed for `folder_structure.md` update.

### 16.2 Gold Standard Treatment for Deliverables [S8]

Should the end-to-end gold standard approach applied to the Srinivas deck also be applied to:

- Problem restatement + information request + preliminary approach as a chain?
- Formal proposal with pricing?
- Team status presentation chain showing how tracking docs evolve?

### 16.3 Depth of Methodology Enforcement [S8]

Balance of:
- Behavioral instructions in SKILL.md
- Deterministic hook checks

Is current balance right? Should more checks be added? Should any be removed if they cause friction?

### 16.4 When to Offer vs Enforce Sub-Singularity Creation [S8]

- Always offer at engagement creation?
- Only when explicitly asked?
- Detect automatically (e.g., 2+ internal team meetings processed implies one should exist)?

### 16.5 Cross-Engagement Learning [S8]

Patterns emerge across engagements. Is there a case for a cross-engagement knowledge layer the skill consults, or is that scope creep?

### 16.6 Backup and Recovery [S8]

Blockchain chains are append-only. If a file is accidentally modified or deleted, is there a recovery pattern? Should there be?

### 16.7 Worked Example skill_notes.md Synchronization [this synthesis]

The worked_example/planning/skill_notes.md is now marked as frozen-in-time. Question: should the worked example ever be refreshed to a newer snapshot, or should it remain frozen to preserve a specific teaching moment? If refreshed, when and how?

### 16.8 Hook Noise During Mid-Set Processing [S2]

Stop hook correctly fires during mid-set processing but is noisy. Proposed fixes listed in §14.2. Decision on which approach.

---

## 17. Source Attribution Map

Every item in sections 1-16 is traceable to one or more of these source files. This map lets future sessions validate by going back to originals.

| Source Tag | File | Key Contributions |
|------------|------|-------------------|
| S1 | `01_lam_skill_notes_authoritative_2026-04-09.md` | Full methodology: structure, philosophy, numbering, source quality, transcript processing, research agents, discussion capture, discussion mode rules, POC scope principles, plus 2026-04-06 and 2026-04-09 named failure corrections |
| S2 | `02_reorganization_session_skill_issues_2026-04-13.md` | Source material handling, decision presentation, reorganization-specific patterns (four states, four phases), hook noise, archive-with-care, validate-vs-process |
| S3 | `03_stale_snapshot_skill_notes_2026-03-20.md` | Subset of S1 — preserved for historical completeness. No unique content not in S1. |
| S4 | `04_nested_design_exploration_2026-04-10.md` | Sub-singularity concept, template, rules, team meeting processing, tracking folder dual model, cross-reference format, emerging ideas |
| S5 | `05_slide_format_spec_2026-04-10.md` | Presentation design language: palette, gradient progression, components, example patterns, rules, embedded diagram pattern, mandatory pre-generation reading |
| S6 | `06_improvements_tracker_2026-04-13.md` | Completed items, working implementations not yet codified, pending integrations, lessons learned from Srinivas deck (bullets default, nav mandatory, etc.), gold standard strategy |
| S7 | `07_master_todo_list_2026-04-13.md` | Five-phase execution plan, cross-cutting process rules, success criteria |
| S8 | `08_open_questions_2026-04-13.md` | Two recurring failure patterns (batched questions, unilateral filtering), six pending clarifications |

---

## 18. What This Synthesis Does Not Include

For honesty, items intentionally out of scope:

- Feedback about other skills (skill-forge, meeting-analyzer, rfp-questions) — see their respective future feedback catalogs
- `.claude/skills/singularity/references/anti_patterns.md` — already in the skill as a reference
- Gold standards themselves — they live in `assets/design/gold_standards/`
- The actual SKILL.md content — separate from feedback; synthesis informs updates to it but does not replicate it

---

## 19. Next Logical Steps After This Synthesis

In dependency order:

1. Review this synthesis for anything missed.
2. Decide on the open questions in §16.
3. Execute the master to-do list (`07_master_todo_list_2026-04-13.md`).
4. Write a new round of feedback (`2026-XX-XX_round_02`) after the next substantive engagement work with Singularity.
