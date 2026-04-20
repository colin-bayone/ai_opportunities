# Handoff: Srinivas CI/CD Slides — Next Session

**Date:** 2026-04-16
**Prepared by:** Colin Moore + previous Claude session
**Status:** Primer HTML complete and approved by Colin. Slides not yet started.
**Target audience:** Next Claude session preparing slides for Srinivas meeting (April 17)

---

## 0. TL;DR for the Next Session

You are picking up an engagement where the team has just finished a substantial primer document for Srinivas Pitta (Director of Engineering, Cisco Cloud Networking Group, owns the DeepSight platform). The primer is at:

`/home/cmoore/programming/ai_opportunities/cisco/cicd/deliverables/srinivas_primer_2026-04-16.html`

Your job is to **build a slide deck based on the primer's content** that Colin will present to Srinivas. The deck must be created using the **Singularity skill** (Flow 7: Create Presentation). Slides go in the **team sub-singularity**, specifically in `cisco/cicd/team/presentations/`.

**Before you touch any slide file, you must:**
1. Read this entire handoff document
2. Read the primer HTML end to end
3. Read the April 10 Srinivas meeting research (Set 11 in the main chain)
4. Read the Singularity skill (SKILL.md) — you MUST follow its presentation flow
5. **Ask Colin what went wrong in the last slide session** — the previous session was structurally confusing and he wants the new deck organized differently

Do not start drafting slides until you have had that conversation with Colin. The previous session's failure mode is the single most important thing to understand before beginning.

---

## 1. What the Primer Covers (and Why)

The primer is a response to a direct request from Srinivas on April 15 at 8:21 PM. The request, verbatim:

> "Hey Colin, Following our discussion from last week, could you share what the team learned and any open questions you might have? I want to make sure tomorrow's meeting is as productive as possible."

The primer delivers:
- **What the team learned** (sections 01, 02, 04)
- **What the team proposes** (sections 03, 04 architecture)
- **What needs scope alignment** (section 05 — the Rui Guo / Naga situation)
- **Open questions** (section 06)
- **Access blockers** (section 07)

### Primer Sections (In Current Order)

| # | Section | Key Content |
|---|---------|-------------|
| 01 | Pain Point Analysis | 4,200+ messages scraped from NxOS CI workflow WebEx (318 members), categorized into 25 categories, response time statistics. Top finding: 66% of help requests go unanswered, bug/test failures wait 4-5 hours for first response. Three embedded charts. |
| 02 | Build Log Infrastructure | Discovery from Justin Joseph sessions (April 8 and 9). NFS path patterns for CI vs CD, 13 Bazel error log types, retention policies. Includes a detailed limitations table of the 7-component automation pipeline reviewed in PR #642. |
| 03 | Proposed Architecture | The corrected build log analysis pipeline (B1 Ingest → B2 Parse → B3 Classification Cascade with 3 tiers → B4 Remediate with human review gate → B5 Star Schema Storage → B6 MCP Serving Layer). Apache Airflow wraps the pipeline. Error Catalog Service replaces Namita's Bazel Docs Scraper. Embedded as `architecture_diagram.png`. 8 block-by-block notes follow. |
| 04 | WebEx Integration | Current state table (Pulse, Scribble, Wall-E all not deployed), vertical 6-layer proposed architecture diagram (inline HTML, not an image), Design Principles paragraph, 5 Open Design Questions as individual cards. |
| 05 | Scope Alignment Needed | The Rui Guo / Nexus T overlap and the Pulse/Scribble scope shift. Colin's view: this is the most important section. Names Rui and Naga directly. See section 4 below for why this was so hard to get right. |
| 06 | Open Questions | 4 technical questions: WebEx scope clarification, fix delivery preference, ML model data availability, batch vs realtime. |
| 07 | Access Items Requiring Action | 3 outstanding access blockers: DeepSight (4 weeks, no access), Pulse/Scribble repos, permanent ADS machine. Includes the Srinivas/Namita/Mahaveer chain from April 16. |

### Deliverables Folder Contents

All four of these files MUST stay co-located with the HTML for the images to render:

```
cisco/cicd/deliverables/
├── srinivas_primer_2026-04-16.html       # the primer
├── srinivas_primer_2026-04-16.md         # markdown source (older, don't edit)
├── architecture_diagram.png              # Section 03 — Build log pipeline (screenshot from Mermaid TB)
├── category_distribution.png             # Section 01 — Srikar's category breakdown
├── avg_response_time.png                 # Section 01 — Response time by category
├── weekly_trend.png                      # Section 01 — 3-year volume trend
├── proposed_architecture_mermaid_tb_2026-04-16.html   # Companion: standalone Mermaid TB version
├── proposed_architecture_mermaid_2026-04-16.html      # Companion: standalone Mermaid LR version
└── team_briefing_2026-04-06.html         # Previous deliverable sent to Srinivas (April 6)
```

---

## 2. The April 10 Srinivas Meeting (Critical Context)

**Read first:** `cisco/cicd/research/11_meeting_srinivas_guidance_2026-04-10.md`
**Source transcript:** `cisco/cicd/source/srinivas-and-team_4-10-2026_formatted.txt`

This was the meeting where Srinivas laid out his operating philosophy and the real problem statement. Several things he said should directly shape the slide structure:

### Srinivas's Operating Philosophy (His Words, Paraphrased)
1. **Fast iteration over perfection** — "I want to run as fast first. I don't want a perfect solution." He will push back on over-engineered plans.
2. **Build reusable pieces alongside the immediate solution** — Dual goal is non-negotiable.
3. **Come with recommendations, not questions alone** — "I support folks who come with suggestions and innovations. Once you know what the problem you're trying to solve, you don't have to depend on me how to solve it."
4. **The existing infrastructure is ready** — "It's not like you have to go build everything from scratch."
5. **Scope expansion is the reward for good work** — Good delivery leads to more projects.

### The Real Problem Statement (What Srinivas Actually Wants)
From the April 10 transcript, Srinivas's problem statement:

> "The PR goes through approximately 45 checks today... What failed we don't know... We need to look deep into the individual PR and say, okay, what is the issue, where did it start? What could be the issue? And how do we unblock?"

This is the overarching goal. All three tasks (WebEx scraping, build log analysis, meeting transcription) feed this. The primer includes a framing sentence connecting the work to this goal; make sure your slides do the same.

### Other Key Items from April 10
- Srinivas said "scraping is just a one day job" — the value is in the pain point analysis, not the scraper itself
- Srinivas said "Airflow is too early" — design first, Airflow comes at productionalization (but Namita's architecture still shows Airflow wrapping the pipeline because that's the right long-term answer)
- Srinivas endorsed Claude Code and Codex as the team's primary tools
- Twice-weekly meeting cadence was established
- The Nexus T agent was NOT discussed in the April 10 meeting (the team only discovered Rui Guo's work afterward)

---

## 3. How the Primer Was Built

### The Full Workflow

1. **Research library was built using the Singularity skill.** Over multiple sessions, transcripts and documents were processed into blockchain-style research files in `cisco/cicd/research/` (main chain) and `cisco/cicd/team/research/` (team sub-singularity).

2. **Team sub-singularity has Sets 01-04** covering:
   - Set 01: April 10 internal standup
   - Set 02: Team WebEx chat (April 1-16) + supplementary files (02a-02e) for individual team member deliverables
   - Set 03: April 7 internal team briefing (coaching session, substantive content only)
   - Set 04: April 16 team sync (the day of the primer) + supplementary files (04a-04g) for Srikar's analysis, Namita's architectures, Saurav's architecture and clarifications, and Saurav's hardware failure email

3. **Main research chain has Sets up to 11** (April 10 Srinivas meeting).

4. **Primer outline was drafted first** as markdown at `cisco/cicd/planning/srinivas_prep_outline_2026-04-16.md`. Colin reviewed and approved the structure.

5. **Markdown draft was written to** `cisco/cicd/deliverables/srinivas_primer_2026-04-16.md`. Colin reviewed substance before HTML conversion.

6. **HTML was built using an agent** with the BayOne design spec from `.claude/skills/singularity/references/bayone_design_spec.md` as the reference. The agent also studied the existing `team_briefing_2026-04-06.html` for style consistency.

7. **Big4 skill was run** on the HTML. It identified 3 factual corrections (the "actionable messages" count was wrong; the blocker response time needed a sample size note; the summary needed a connection to Srinivas's PR-unblocking goal). All three were applied.

8. **Multiple rounds of revision with Colin** followed. See section 4 for the specific issues.

### Specific Data Sources for Each Section

| Section | Primary Source(s) | Notes |
|---------|-------------------|-------|
| 01 Pain Point | `team/source/week_2026-04-14/day_2026-04-16/srikar/new/` (9 files) | Charts are from Srikar's categorization work. CSV data sources are in the same folder. |
| 02 Build Log | `team/research/02a_namita_build_log_analysis_updates_2026-04-10.md`, `02b_namita_log_type_mapping_2026-04-16.md`, `02c_namita_build_architecture_diagrams_2026-04-16.md` | Source documents in `team/source/week_2026-04-14/day_2026-04-16/namita/` |
| 03 Proposed Architecture | `deliverables/proposed_architecture_mermaid_tb_2026-04-16.html` (the screenshot `architecture_diagram.png` was taken from the rendered Mermaid output); original was Namita's SVG at `team/source/week_2026-04-14/day_2026-04-16/namita/Proposed Build Log Analysis Architecture — Blocks 1–7.html`. See section 5 of this handoff for architectural corrections. |
| 04 WebEx Integration | `team/research/02d_srikar_webex_recording_extraction_2026-04-16.md`, `04f_saurav_webex_architecture_2026-04-16.md`. Vertical architecture was rebuilt inline (HTML/CSS) from Saurav's original horizontal design at `team/source/week_2026-04-14/day_2026-04-16/saurav/webex_architecture_light 1.html`. Design questions from `saurav/webex_arch_clarifications.md`. |
| 05 Scope Alignment | `team/research/04_sync_rui_guo_nexus_t_2026-04-16.md`, `04d_srikar_nxos_chat_analysis_2026-04-16.md` (includes the Naga screenshot where Naga told Srikar the scope had shifted). |
| 06 Open Questions | Distilled from across Set 04 architecture discussions. |
| 07 Access Items | `team/tracking/blockers.md` + the April 16 Srinivas/Namita/Mahaveer exchange that Colin shared verbally. |

### Architectural Corrections (Do Not Regress)

The architecture in Section 03 has been corrected from Namita's original. The HANDOFF from the Mermaid rebuild session is at:

`claude/2026-04-16_cisco_architecture_mermaid_rebuild/HANDOFF.md`

**Read this file before discussing the architecture with Colin.** Key corrections that must not be regressed:

- B2 Parse is deterministic only. No NLP. No summarization. Namita's original had NLP in B2; this was pushed into the LLM tier (T3) where it belongs.
- The tier cascade is mutually exclusive. Each error is caught at exactly one tier. Don't reintroduce the "race condition" framing.
- Error Catalog Service replaced the "Bazel Docs Scraper." It has three sources: Bazel release catalogs, historical Cisco logs, and promoted approved fixes (feedback loop).
- The feedback loop is `B4 approved fix → CATALOG` — novel errors that get human-approved fixes get promoted into the Tier 1 catalog.
- MySQL and B6 shapes (cylinder and hexagon) must not be changed.

---

## 4. Problems, Challenges, Pitfalls — Things That Went Wrong

This section is crucial. Read it carefully. Many of these are Claude-level mistakes that Colin had to correct. Do not repeat them.

### Process Mistakes (Claude violating the Singularity workflow)

1. **Skipping the topic map approval step.** When processing a new source, the Singularity skill REQUIRES proposing a topic map with rationale and getting Colin's approval before spawning deep-dive agents. Claude at one point tried to write a "single consolidated research file" without the topic map approval step, and Colin stopped the session and threatened to fire Claude. **You must follow Singularity Flow 7 exactly for the slides: read the mandatory references, propose a slide list with layout descriptions in plain language, get Colin's approval, THEN generate.**

2. **Asking Colin "what topics do you want me to propose?"** — This is wrong. Claude's job is to identify the topics and propose them. Colin approves, adjusts, adds, or removes. Do not defer the decision back to him.

3. **Proposing to "pivot immediately" without approval.** Claude tried to skip from processing source material straight to building the prep document. Colin stopped this. The workflow is the workflow.

### Content Mistakes (Language and Framing)

1. **Passive/defensive language.** Claude wrote "the team is proceeding with architecture design but is not committing to implementation that could conflict with or duplicate existing work." Colin: "That is not the right language to use. It's basically like we need clarification as to what our role is." The correction: ask direct questions about whether to build on, collaborate, or work separately. Be direct, not hedgy.

2. **Missing the Rui Guo / Naga issue entirely from early drafts.** Colin was clear from the start that the scope overlap needed its own section. Claude kept putting it as a single bullet in Open Questions. Colin: "Claude, what the hell are you thinking... Honestly, in both sections, you should mention Rui and Naga both. Naga pretty much blew Srikar off. You need to raise that up."

3. **Using internal characterizations in client-facing text.** Claude wrote things like "the team is ready to move in whatever direction is confirmed and can adapt quickly once the boundaries are established" — Colin pushed back on overly corporate/defensive language. Use direct language framed as collaborative: "we'd like to understand X so we can focus our effort where it adds the most value."

4. **"What We Learned" as a title.** Colin flagged this as weak: "the Big Four skill should have flagged that." The title was changed to "CI/CD Pipeline Intelligence: Progress and Open Items." Avoid vague/generic titles.

### Formatting Mistakes

1. **Badges placed inconsistently.** Some architectural badges were top-right corner labels ("modular"), others were inline pill badges ("WebEx API", "Per-user auth"). Colin: "Be consistent. The badges should give some value." The fix: use top-right badges only for meaningful architectural labels; fold everything else into the description text.

2. **Stripping sub-items from source diagrams.** When rebuilding Saurav's WebEx architecture, Claude simplified the box contents too much, removing the detailed sub-items that Saurav had. Colin: "Why did you do that?" The fix: preserve Saurav's original level of detail.

3. **Questions crammed into a single card.** Claude put 5 design questions into one "Open Design Decisions" card as a single paragraph. Colin: "The formatting sucks. They're not even formatted. They're just all cluttered together." The fix: each question in its own card with clear label, context, and the actual question.

4. **Bold-on-bold competing for attention.** When Colin said "make the question itself bold," Claude made both the label AND the question bold. Colin: "It's kind of competing for attention. I wish there was more vertical space." The fix: label in bold (600 weight), context in regular, question in medium weight (500) with a subtle purple accent color.

5. **Print layout issues.** The Mermaid diagram and Saurav's vertical architecture both broke across pages. Colin got frustrated: "Quit trying to do that fancy shit. This is so easy. Put the diagram on the fucking page." Eventually the Mermaid diagram was replaced with a static screenshot (`architecture_diagram.png`). **For slides, page size is constrained — do not create content that overflows a single slide.**

### Positive Feedback (What Colin Liked)

1. After multiple rounds of scope-alignment revisions: "Makes sense."
2. After the individual question cards were split with proper spacing: Colin approved the layout.
3. After the Mermaid diagram was replaced with the static image: "This finally looks great."
4. After the Big4 review surfaced the factual errors: Colin approved all three corrections without pushback.
5. Colin liked that the primer directly names Rui and Naga (after the corrections) rather than dancing around it.

### Colin's Specific Working Style (Important)

- Colin uses a dictation tool. Garbled names and terms in his messages are transcription errors; match against known context first before asking.
- Colin wants you to **do the thing** when the next step is obvious. Don't describe and wait for confirmation on trivial steps. But for non-trivial decisions, propose and wait.
- Colin hates filler questions (obvious exclusions, self-evident clarifications). Think first, then propose.
- Never make unilateral decisions. When instructions can't be followed exactly, STOP and ask Colin. Never silently adjust.
- Never skip any part of the Singularity workflow.
- Planning goes in files, not in chat. Write designs/plans/specs to markdown files before discussing.

---

## 5. The Last Session With Srinivas Didn't Go Great

**Colin's words:** "The last session did not go great because we didn't have detail on certain things, and the structure was a little bit confusing, convoluted, and it wasn't clear. He wants to have something more organized."

**This is the most important thing for you to understand.** The previous slide session produced a deck that felt disorganized to Srinivas. The exact failure mode is not documented — you need to ask Colin.

**Before you start drafting slides:** Have a conversation with Colin about what went wrong. Ask specifically:
- Which topics felt underdeveloped or where was there not enough detail?
- Which parts of the structure were confusing?
- What was the order of sections and why did it feel disorganized?
- What would a well-organized version look like to Srinivas?
- Is there specific content Srinivas asked about that wasn't covered?

Do not start drafting until you have clarity from Colin on what he wants different this time.

---

## 6. Where the Slides Should Go

**Slides go in the team sub-singularity:**

`cisco/cicd/team/presentations/<deck_name>_<date>/`

Each slide is a self-contained HTML file following the BayOne presentation design language. Navigation (prev/next/home) on every slide.

### Mandatory Reads Before Generating Any Slide

Per Singularity Flow 7 (this is a hard gate):

1. `.claude/skills/singularity/references/presentation_design_language.md` — 21 rules, components, and common failure modes
2. `.claude/skills/singularity/layout_examples/README.md` and the layout HTML files
3. `.claude/skills/singularity/gold_standards/presentations/team_status_update/README.md`

If diagrams are needed on any slide:

4. `.claude/skills/singularity/references/mermaid_design_standards.md`
5. `.claude/skills/singularity/references/mermaid_shape_library.md`
6. All 8 HTML example files at `.claude/skills/singularity/mermaid_shape_library/`

**The Stop hook verifies these files were read. Skipping this step will fail.**

### Singularity Flow 7 Summary

1. Read the design language spec, layout examples, and gold standard README
2. Read prior context from the research library (you should read all of Set 04 and Set 11)
3. **Propose a slide list** with descriptions of what each slide covers and the layout approach in plain language (e.g., "dark definition bar introducing the concept, then two cards with bullet items below, plus a takeaway bar")
4. **Get Colin's approval before generating anything**
5. Generate slides. Each slide is self-contained HTML. All cards use bullet formatting (`.items`/`.item`). All slides have navigation.
6. Output to `cisco/cicd/team/presentations/<deck_name>_<date>/`
7. Offer to run `/big4` on the deck before finalizing

### Content for the Deck

The deck should present the primer content, reorganized based on Colin's feedback about what went wrong last time. At minimum, the deck needs to cover:

- The pain point analysis findings (charts embedded)
- The build log infrastructure understanding
- The proposed architecture (use the `architecture_diagram.png` image)
- The WebEx integration work
- The Rui/Naga scope alignment (neutrally named)
- The access items blocking progress

**But the order and emphasis should come from the conversation with Colin.** The primer structure may not be the right slide structure.

### What to Avoid

- Do not include internal team dynamics
- Do not include tool attribution strategy (Claude vs Copilot)
- Do not include the Saurav hardware failure
- Do not include internal escalation framing
- Do not include pricing/financial discussion
- Do not include unresolved internal architecture debates (skills approach, the "$1M question")
- Do not use "what we learned" as a title or section header
- Do not use em dashes in any rendered text
- Do not use individual team member names (frame as "the team")
- Do not use direct quotes

---

## 7. Org Chart Key Names (For Reference, Not Inclusion in Slides)

| Name | Role | Relevance |
|------|------|-----------|
| Srinivas Pitta | Director of Engineering / AI Lead, Cisco CNG | The audience |
| Anand Singh | Senior Director, Cisco CNG | Srinivas's boss, budget authority |
| Justin Joseph | Engineer, Build Infrastructure, Cisco | Owns existing build automation (PR #642) |
| Divakar Rayapureddy | Engineering Lead, Cisco | Access provisioning |
| Rui Guo | Engineer (Arun's team), Cisco | Built Nexus T — scope overlap concern |
| Nagabhushan Bangalore Nanjaiah ("Naga") | Engineer (Srinivas's team), Cisco | Built Pulse and Scribble — scope shifted per his 4/16 message |
| Mahaveer Jinka | Procurement + Infrastructure access | Granted the DCN Switching tenant |
| Colin Moore | Director of AI, BayOne | Project lead (you report to him) |
| Namita Mane | On-site engineer, BayOne | Build log track lead, authored Section 02/03 source |
| Srikar Madarapu | On-site engineer, BayOne | WebEx track, NxOS chat analysis |
| Saurav Kumar Mishra | Offshore engineer, BayOne | Wall-E bot, WebEx architecture |
| Vaishali Sonawane | Offshore, BayOne | New, no hardware yet |

---

## 8. Complete File Inventory (What Exists)

### The Primer (Your Reference)
- `cisco/cicd/deliverables/srinivas_primer_2026-04-16.html` — the final HTML
- `cisco/cicd/deliverables/srinivas_primer_2026-04-16.md` — markdown draft
- `cisco/cicd/deliverables/architecture_diagram.png` — build log architecture
- `cisco/cicd/deliverables/category_distribution.png` — pain point chart 1
- `cisco/cicd/deliverables/avg_response_time.png` — pain point chart 2
- `cisco/cicd/deliverables/weekly_trend.png` — pain point chart 3
- `cisco/cicd/deliverables/team_briefing_2026-04-06.html` — previous Srinivas deliverable (reference for style)

### Research Library (Team Sub-Singularity)
- `cisco/cicd/team/research/00_methodology_2026-04-10.md` — methodology doc
- `cisco/cicd/team/research/01_*` — Set 01, April 10 standup (5 files)
- `cisco/cicd/team/research/02_chat_*` — Set 02, April 1-16 team chat (6 files)
- `cisco/cicd/team/research/02a_namita_build_log_analysis_updates_2026-04-10.md`
- `cisco/cicd/team/research/02b_namita_log_type_mapping_2026-04-16.md`
- `cisco/cicd/team/research/02c_namita_build_architecture_diagrams_2026-04-16.md`
- `cisco/cicd/team/research/02d_srikar_webex_recording_extraction_2026-04-16.md`
- `cisco/cicd/team/research/02e_saurav_hardware_failure_email_2026-04-15.md`
- `cisco/cicd/team/research/03_briefing_*` — Set 03, April 7 team briefing (4 files)
- `cisco/cicd/team/research/04_sync_*` — Set 04, April 16 team sync (7 files)
- `cisco/cicd/team/research/04d_srikar_nxos_chat_analysis_2026-04-16.md`
- `cisco/cicd/team/research/04e_namita_proposed_architecture_2026-04-16.md`
- `cisco/cicd/team/research/04f_saurav_webex_architecture_2026-04-16.md`
- `cisco/cicd/team/research/01-02_changes_2026-04-16.md` — bridge between Sets 1 and 2
- `cisco/cicd/team/research/03-04_changes_2026-04-16.md` — bridge between Sets 3 and 4

### Research Library (Main Chain)
- `cisco/cicd/research/11_meeting_people_2026-04-10.md`
- `cisco/cicd/research/11_meeting_srinivas_guidance_2026-04-10.md` — **READ THIS FIRST**
- `cisco/cicd/research/11_meeting_summary_2026-04-10.md`

### Source Materials
- `cisco/cicd/source/srinivas-and-team_4-10-2026_formatted.txt` — the April 10 meeting transcript (formatted)
- `cisco/cicd/source/srinivas-and-team_4-10-2026.txt` — original single-line version
- `cisco/cicd/team/source/2026-04-16/cisco-team-sync_01.txt` — April 16 team sync transcript
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/team_chat_1009AM.txt` — team WebEx chat April 1-16
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/namita/` — Namita's 5 files
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/srikar/WEBEX_REC_EXTRACTION.md`
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/srikar/new/` — 9 files, Srikar's NxOS chat analysis
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/saurav/saurav_email.txt` — hardware failure email
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/saurav/webex_arch_clarifications.md`
- `cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/saurav/webex_architecture_light 1.html`

### Tracking Files
- `cisco/cicd/team/tracking/action_items.md` — 38 action items across sets
- `cisco/cicd/team/tracking/blockers.md` — active and resolved blockers
- `cisco/cicd/team/tracking/decisions.md` — 13 decisions logged
- `cisco/cicd/org_chart.md` — living org chart

### Planning
- `cisco/cicd/planning/srinivas_prep_outline_2026-04-16.md` — the outline that shaped the primer
- `cisco/cicd/planning/proposed_architecture_review_2026-04-16.md` — architectural review that led to the Mermaid rebuild
- `cisco/cicd/planning/srinivas_slides_handoff_2026-04-16.md` — this document

### Mermaid Architecture Rebuild Session
- `claude/2026-04-16_cisco_architecture_mermaid_rebuild/HANDOFF.md` — full history of architectural corrections

### Big4 Session
- `claude/2026-04-16_big4_srinivas_primer/` — Big4 quality review artifacts

---

## 9. Your First Moves

1. **Read this entire document.**
2. **Read the primer HTML** at `cisco/cicd/deliverables/srinivas_primer_2026-04-16.html`.
3. **Read Set 11** at `cisco/cicd/research/11_meeting_srinivas_guidance_2026-04-10.md`.
4. **Read the Mermaid rebuild HANDOFF** at `claude/2026-04-16_cisco_architecture_mermaid_rebuild/HANDOFF.md`.
5. **Read the Singularity SKILL.md** at `.claude/skills/singularity/SKILL.md` (especially Flow 7: Create Presentation).
6. **Read the mandatory presentation references** listed in section 6 of this handoff.
7. **Have the "what went wrong last time" conversation with Colin.** Do not start drafting until you have clarity. Ask specifically about:
   - Structural issues in the previous deck
   - Topics that felt underdeveloped
   - What Srinivas wanted that wasn't there
   - What "organized" looks like to Colin this time
8. **Propose a slide list with layouts in plain language.** Wait for approval.
9. **Generate slides one by one**, with navigation, following the BayOne presentation design language.
10. **Offer to run /big4** before finalizing.

---

## 10. Final Reminders

- Slides go in `cisco/cicd/team/presentations/` — this is the team sub-singularity.
- Use the Singularity skill. Flow 7. Do not skip phases.
- Ask Colin what went wrong last time. That is the single most important input.
- The primer content is approved. Don't re-litigate it. Reorganize for presentation flow.
- Never make unilateral decisions. Propose, wait, execute.
- The meeting is tomorrow (April 17). Time pressure is real but skipping steps will cost more time than following the workflow.
