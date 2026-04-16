---
name: singularity
description: |
  Organizes consulting engagements from raw transcripts and context into structured research libraries, client deliverables, and pricing models.
  WHEN to use: new client opportunity, transcript processing, engagement prep, proposal creation, pricing model, discovery organization.
  WHEN NOT to use: internal project work, code implementation, non-consulting tasks.
user-invocable: true
argument-hint: [new|continue|process|deliver|price|discuss]
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python3:*), WebSearch, WebFetch, Task
hooks:
  Stop:
    - hooks:
        - type: "command"
          command: "python3 $CLAUDE_PROJECT_DIR/.claude/skills/singularity/scripts/singularity_stop.py"
          timeout: 10000
          statusMessage: "Verifying singularity workflow..."
---

# Singularity

Consulting engagement orchestrator. Processes meeting transcripts, emails, call preps, and internal debriefs into blockchain-style research libraries. Produces client-facing deliverables and pricing models. Replaces and supersedes sales-forge.

## Hard Rules

1. **Blockchain style.** Research documents are numbered chronologically and NEVER edited after creation. New understanding goes in new documents that reference earlier ones.
2. **Multi-pass processing.** Transcripts are read multiple times, each pass focused on one topic. This is the single most important processing rule. It exists for context clearing, exhaustive capture, better organization, and natural parallelization. Write after every read, not once at the end.
3. **Ask, do not assume.** Always propose file lists and get user approval before writing research docs or spawning agents. The user controls what gets created. Different meetings warrant different breakdowns.
4. **Agents write their own files.** Deep-dive and research agents write directly to the engagement folder. Use `mode: "bypassPermissions"`. Never fall back to writing in the main session if an agent fails. Report the failure and ask how to proceed.
5. **Max 5 questions per batch.** Never overwhelm the user. Ask follow-up questions in subsequent rounds. Prioritize questions that gate decisions or unblock progress. (Applies to written follow-ups during source processing. For interactive discussion, see Behavioral Rule B1 below — one question per turn.)
6. **Deliverables flow from research.** Client-facing documents are drafted from the research library, not from raw transcripts. The research library is the single source of truth.
7. **Everything is dated.** Every file in the engagement gets a date in its filename (YYYY-MM-DD). No exceptions. Date reflects the source material date, not the analysis date.
8. **No em dashes in deliverables.** Use commas, periods, or "and" instead. No individual names, no direct quotes, no contrastive framing ("It's not just X, it's Y"), no emojis, no contractions.
9. **Solution, never product.** BayOne builds custom, tailor-made solutions using proven methodology. Never position as an off-the-shelf product.
10. **Self-contained skill.** All reference files, templates, and assets live within `.claude/skills/singularity/`. No external dependencies. All reference files, templates, and company context live within `.claude/skills/singularity/`. All rationale, rules, and references must be inside this directory. Never cross-reference session folders, engagement folders, or external paths as authoritative sources from within the skill definition.

---

## Document Header Format

**Every research document must start with this header.** Agents must include it in all files they write.

```markdown
# <Set Number> - <Source Type>: <Topic>

**Source:** /<client_name>/<opportunity_name>/source/<filename>
**Source Date:** <date> (<context description>)
**Document Set:** <set number> (<description of what this set covers>)
**Pass:** <what this specific read was focused on>

---
```

Example:
```markdown
# 02 - Meeting: Technical Use Cases (Deep Dive)

**Source:** /lam_research/ip_protection/source/lam_meeting_3122026.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on use cases

---
```

---

## Mandatory Startup: Permission and Rules Check

**Every invocation, before ANY work, run these checks in order.**

1. Read `.claude/settings.local.json`
2. Verify `Write($CLAUDE_PROJECT_DIR/**)` exists in `permissions.allow`
3. Verify `WebSearch` exists in `permissions.allow`
4. If either is missing:
   - Tell the user: "Singularity requires agents to write files autonomously and research agents to search the web. I need to add `Write($CLAUDE_PROJECT_DIR/**)` and/or `WebSearch` to the permissions. May I do that?"
   - If approved, add the permission
   - If declined, explain the skill cannot function and stop
5. Read `.claude/skills/singularity/references/hard_rules.md`
6. If the file does not exist, stop and tell the user: "The behavioral hard rules file is missing. It must exist at `.claude/skills/singularity/references/hard_rules.md` for the skill to function."

---

## Invocation: "What are we doing today?"

When the user invokes `/singularity`, ask:

> **What are we doing today?**
> 1. **New engagement** - organize a new client opportunity from scratch
> 2. **Continue** - pick up where we left off on an existing engagement
> 3. **Process source** - add a new transcript, email, or document to an existing engagement
> 4. **Deliver** - draft a client-facing document
> 5. **Price** - build or refine a pricing model
> 6. **Discuss** - think through strategy or technical approach
> 7. **Present** - create a presentation deck from the research library
> 8. **Audit** - check if an engagement's structure is correct and propose fixes

If the user provides context that makes the intent obvious, skip this question and go directly to the right flow.

---

## Flow 1: New Engagement

**Questions to ask:**
1. What is the client name? (lowercase, underscores for folder name)
2. What is the opportunity name? (lowercase, underscores)
3. What source material do you have? (transcripts, emails, call preps, documents)
4. Do you want the full folder structure or a subset? (Default: all. Minimum: source + research.)

**Actions:**
1. Create `/<client_name>/<opportunity_name>/` with selected folders
2. Write `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` using the template at `.claude/skills/singularity/templates/methodology_template.md`. Fill in the client name and opportunity description.
3. Read `.claude/skills/singularity/references/bayone_team.md` for BayOne team context
4. If the engagement will involve team operations (standups, team syncs), offer to create a team sub-singularity: "This engagement will have team meetings. Should I create a `team/` sub-singularity now with its own source, research, and tracking folders?" If yes, create it using the pattern in `references/nested_singularity.md`.
5. Begin processing source material (proceed to Flow 3)

**Load references:** `.claude/skills/singularity/references/folder_structure.md`, `.claude/skills/singularity/references/blockchain_methodology.md`

**Full folder structure:**
```
/<client_name>/<opportunity_name>/
├── org_chart.md                    (living document, always current)
├── source/                         (raw files, NEVER modified)
├── research/                       (blockchain decomposition, append-only)
├── planning/                       (skill notes, glossary, session handoffs)
├── pricing/                        (pricing specs, corrections, workbooks)
├── deliverables/                   (client-facing docs, flat with dates)
├── presentations/                  (slide decks, materials)
├── decisions/                      (open questions, agreed decisions)
└── progress/                       (status tracking)
```

---

## Flow 2: Continue Engagement

**Questions to ask:**
1. Which engagement? (client/opportunity, or detect from context)

**Actions (read in this order):**
1. `/<client_name>/<opportunity_name>/planning/session_handoff_<date>.md` if exists (where last session left off)
2. `/<client_name>/<opportunity_name>/research/00_methodology_<date>.md` (the system)
3. `/<client_name>/<opportunity_name>/planning/skill_notes.md` if exists (accumulated do's/don'ts)
4. Summary docs in order from `/<client_name>/<opportunity_name>/research/` (01 summary, 02 summary, 02a summary, etc.)
5. `/<client_name>/<opportunity_name>/org_chart.md` (current people state)
6. Report current state and ask what to do next

**Load references:** `.claude/skills/singularity/references/session_continuity.md`

---

## Flow 3: Process Source Material

**Questions to ask:**
1. Which engagement? (if not already established)
2. What type of source? (transcript, call prep, email, debrief, other)
3. **Is this an internal team meeting or a client meeting?** If internal team meeting (standup, team sync, team-to-counterpart without the lead), route to the team sub-singularity instead of the main chain. If the sub-singularity does not yet exist, offer to create it using the nested_singularity methodology.
4. Is this a new event (new set number) or supplementary to a prior event (letter suffix like 02a)?

**Load references:** `.claude/skills/singularity/references/document_processing.md`, `.claude/skills/singularity/references/agent_architecture.md`, `.claude/skills/singularity/references/people_tracking.md`
**If team meeting:** Also load `.claude/skills/singularity/references/team_meeting_processing.md`, `.claude/skills/singularity/references/nested_singularity.md`, `.claude/skills/singularity/references/tracking_folder_pattern.md`

### Source File Organization

Before processing any source material, place it in the correct week/day folder structure:

1. Determine today's date (the upload date, NOT the source material date)
2. Calculate the Monday of the current week for the week folder name
3. Create `source/week_YYYY-MM-DD/day_YYYY-MM-DD/` if it doesn't exist
4. For team sub-singularities, also create a person subfolder: `source/week_YYYY-MM-DD/day_YYYY-MM-DD/<person>/`
5. Place the source file in the appropriate folder
6. If the `source/` folder has no `README.md`, create one explaining that week folders use Monday dates and day folders use the upload date (not the source material date)

### Transcripts (Primary Use Case)

**Exact processing order:**

1. **Read prior context.** Latest summary in `/<client_name>/<opportunity_name>/research/` + `/<client_name>/<opportunity_name>/org_chart.md`. This ensures continuity and avoids re-discovery.
2. **Pass 1: People file.** Read the full transcript. Write the people document to `/<client_name>/<opportunity_name>/research/<set>_<type>_people_<date>.md`. Always the first file for transcript sets.
3. **Pass 1 continued: Topic map.** Identify major topics. Write topic map with proposed deep-dive files AND rationale for why each needs its own file. Present to user.
4. **Ask user.** Get approval on the file list. User may adjust, add, or remove files.
5. **Spawn parallel agents.** One agent per topic, ALL spawned in a single message for maximum parallelism. Each agent reads the full transcript with ONE topic focus and writes one file. See Agent Prompt Template below.
6. **Update org chart.** After all agents complete, update `/<client_name>/<opportunity_name>/org_chart.md` with everything learned.
7. **Bridge document.** If this is not the first set, write `/<client_name>/<opportunity_name>/research/<from>-<to>_changes_<date>.md`. See `.claude/skills/singularity/gold_standards/deliverables/bridge_document_example.md` for the gold standard format. Captures: hypotheses validated/invalidated/open, what we got wrong, what we got right, new information, questions answered.
8. **Summary document.** Always last. Short overview referencing all files in the set.
9. **Offer research.** If unfamiliar technologies or terms were encountered, offer to spawn research agents (see Web Research section).

### Agent Prompt Template

**Every deep-dive agent must receive this complete, self-contained prompt:**

```
You are writing a detailed decomposition document from a meeting transcript.
Read the transcript, then write one focused output file.

**Your focus:** [ONE SPECIFIC TOPIC - e.g., "Technical use cases and requirements"]

**Read this file:** /<client_name>/<opportunity_name>/source/<transcript_filename>

**Context from the topic map (so you know what to look for):**
[BULLET POINTS from the topic map for this specific topic]

**What to capture in exhaustive detail:**
- Quote or closely paraphrase key statements. Do not summarize. Decompose.
- Capture specific numbers, names, technical details, and claims.
- Note who said what when it matters for context.
- Flag open questions or unresolved points.

**IMPORTANT: Speech-to-text transcript quality.**
This transcript is speech-to-text and full of transcription errors. Use common sense:
- "concept-renade" = "confidential violation"
- "lamb GPT" = "LamGPT"
- "Spacey" = "SpaCy"
- "on pram" = "on-prem"
- "brass beam" = "Brad's team"
- "compiler" = "Copilot"
- "Gapsium" / "Kaptima" = "Capgemini"
Infer intended meaning from context. Do not take mangled words at face value.

**Write your output to:** /<client_name>/<opportunity_name>/research/<set>_<type>_<topic>_<date>.md

**Use this header format:**
# <Set Number> - <Source Type>: <Topic>

**Source:** /<client_name>/<opportunity_name>/source/<transcript_filename>
**Source Date:** <date> (<context>)
**Document Set:** <set number> (<description>)
**Pass:** Focused deep dive on <topic>

---
```

### Call Preps
Single or few passes. Propose file breakdown (situational context, discovery strategy, technical reference, people). Ask user. Write files.

### Internal Debriefs
Supplementary material using letter suffix (02a, 02b). Capture candid assessments honestly. Flag anything that must never appear in client-facing materials. Update org chart.

### Emails and Written Communications
Determine if new event or supplementary. Extract decisions, action items, new information. Usually fewer files than transcript sets.

### Working Discussions (User + Claude)
Conversation becomes a document set. Read prior context, propose discussion topics (max 5), user responds, write immediately after each exchange. Use "continued" files if discussion extends. Capture reasoning, not just conclusions. Distinguish hyperbole from commitments.

---

## Flow 4: Create Deliverable

**Questions to ask:**
1. Which engagement? (if not already established)
2. What type of deliverable?
   - Problem restatement (demonstrates understanding, no solutions)
   - Information request (prioritized asks, who can answer each)
   - Preliminary approach (initial direction, explicitly preliminary)
   - Formal proposal concise (scoped engagement with phases and pricing)
   - Formal proposal detailed (extended version with deeper technical sections)
   - Resource plan (staffing and team structure)
   - Follow-up email (markdown only, maintain momentum)
3. What is the title and cover label? (Cover labels are thematic, NOT literal. "SECURE KNOWLEDGE ENABLEMENT" not "PROBLEM RESTATEMENT".)
4. Who is the audience? (VP level? Technical? Executive?)

**Process:**
1. Draft in markdown first in `/<client_name>/<opportunity_name>/deliverables/<name>_<date>.md`. User reviews substance before formatting.
2. Convert to HTML using BayOne design system. Read `.claude/skills/singularity/references/bayone_design_spec.md` for the complete design spec. Read the appropriate gold standard for structural reference (not fill-in-the-blanks).
3. Read `.claude/skills/singularity/references/bayone_team.md` for cover pages and "Why BayOne" sections.
4. Offer to run `/big4` for quality review before finalizing.
5. Iterate with user until approved.
6. Output HTML to `/<client_name>/<opportunity_name>/deliverables/<name>_<date>.html`.

**Load references:** `.claude/skills/singularity/references/deliverables_pipeline.md`, `.claude/skills/singularity/references/anti_patterns.md`, `.claude/skills/singularity/references/professional_standards.md`

**Gold standards** (read for style and structure):

| Type | Gold Standard |
|------|--------------|
| Problem restatement | `.claude/skills/singularity/gold_standards/deliverables/problem_restatement.html` |
| Information request | `.claude/skills/singularity/gold_standards/deliverables/information_request.html` |
| Preliminary approach | `.claude/skills/singularity/gold_standards/deliverables/preliminary_approach.html` |
| Proposal (concise) | `.claude/skills/singularity/gold_standards/deliverables/poc_proposal_v5.html` |
| Proposal (detailed) | `.claude/skills/singularity/gold_standards/deliverables/poc_proposal_v5_detailed.html` |
| Bridge document | `.claude/skills/singularity/gold_standards/deliverables/bridge_document_example.md` |

---

## Flow 5: Pricing

**When to offer:** After research is complete and scope is understood. Not before.

**Process:**
1. Run structured questionnaire in batches (scope/revenue, team/costs, timeline/scenarios, margin/risk, discount strategy). See `.claude/skills/singularity/references/pricing_workflow.md` for the full questionnaire.
2. Prototype numbers in the conversation first.
3. Build pricing spec markdown in `/<client_name>/<opportunity_name>/pricing/pricing_spec_<date>.md`. This file doubles as a prompt for Claude in Excel.
4. **Capture the pricing discussion as a research set.** The reasoning behind pricing decisions (margin targets, team composition choices, discount strategy) goes in `/<client_name>/<opportunity_name>/research/<set>_discussion_pricing_strategy_<date>.md`. The pricing spec in `pricing/` is the actionable output. The research doc is the record of how and why.
5. Reference the template at `.claude/skills/singularity/templates/ProjectCostingTemplate.xlsx` and the creation prompt at `.claude/skills/singularity/templates/excel_template_prompt.md`.
6. Write correction prompts as separate dated files in `/<client_name>/<opportunity_name>/pricing/` if iteration is needed.

**Load references:** `.claude/skills/singularity/references/pricing_workflow.md`

---

## Flow 6: Discussion

**When to proactively offer:** After 2+ document sets exist, proactively offer a strategy discussion. Say: "We have enough context to discuss BayOne's positioning for this engagement. Want to work through strategy before we draft deliverables?"

**Standard strategy questions (present as first batch):**
1. What does BayOne want from this engagement? (Staffing? Solutions? Advisory? Long-term relationship?)
2. What is our unique angle or credibility for this specific client?
3. Who has decision-making authority on the client side? Who influences but does not decide?
4. What are the explicit asks vs. implicit needs?
5. What is the competitive landscape? Who else is the client talking to?

**Process:**
1. Read prior context (latest summaries + org chart)
2. Propose discussion topics based on open threads from research
3. User responds
4. Write immediately after each exchange to `/<client_name>/<opportunity_name>/research/<set>_discussion_<topic>_<date>.md`. Do not accumulate.
5. Continue in batches of max 5 questions
6. Write summary when user indicates discussion is complete

**Special rules for discussions:**
- Ask ONE question per turn with perspective and context (see behavioral rule B1 in `references/hard_rules.md`). Do NOT batch multiple questions. The older "max 5 questions per batch" applies only to written transcript-processing follow-ups, not interactive discussions.
- Capture the user's reasoning, not just conclusions. The "why" is as valuable as the "what."
- Flag open items explicitly. If the user says "this requires discovery" or "we need info from the sales team," that is an open item.
- Do not sanitize. Capture blunt assessments, strong opinions, and confidence claims honestly.
- Distinguish hyperbole from commitments. "I could do this in a day" is confidence in feasibility, not a timeline commitment. Do not repeat it as a planning estimate.

---

## Flow 7: Create Presentation

**Questions to ask:**
1. Which engagement? (if not already established)
2. What is the presentation for? (client meeting, internal briefing, status update, executive review)
3. Who is the audience? (technical, executive, mixed)
4. What topics should it cover? (or: "pull from the research library")

**Mandatory pre-generation reading (hard gate):**

Before writing ANY HTML slide file, the skill MUST read:
1. `.claude/skills/singularity/references/presentation_design_language.md` (the design language spec — contains 21 rules, components, and common failure modes)
2. The layout examples index at `.claude/skills/singularity/layout_examples/README.md` and the layout HTML files
3. The gold standard deck README at `.claude/skills/singularity/gold_standards/presentations/team_status_update/README.md`

This is not optional. The stop hook verifies that presentation reference files exist. If generating slides via agents, each agent's prompt must instruct it to read the spec and at least one example before writing.

**Process:**
1. Read the design language spec, example slides, and gold standard README (mandatory, see above)
2. Read prior context from the research library (summaries, relevant detail files)
3. Propose a slide list with descriptions of what each slide covers and the layout approach in plain language (e.g., "dark definition bar introducing the concept, then two cards with bullet items below, plus a takeaway bar"). Get user approval before generating.
4. Generate slides. Each slide is a self-contained HTML file following the BayOne design language. All cards use bullet formatting (`.items`/`.item`). All slides have navigation (prev/next/home).
5. If a diagram is needed, read `.claude/skills/singularity/references/mermaid_design_standards.md` for color palettes and standards, `.claude/skills/singularity/references/mermaid_shape_library.md` for the quick-reference menu, and ALL of the shape library HTML examples at `.claude/skills/singularity/mermaid_shape_library/` (8 files). These HTML files are the best reference for what is possible — they demonstrate every shape, arrow, icon, styling option, and diagram type with live rendered examples. They are better than the gold standard for understanding capabilities. Read all of them. Propose a chart file in `charts/` and a dedicated diagram slide if the content warrants it.
6. Output to `/<client_name>/<opportunity_name>/presentations/<deck_name>_<date>/`
7. Offer to run `/big4` on the deck before finalizing.

**Load references:** `.claude/skills/singularity/references/presentation_design_language.md`, `.claude/skills/singularity/layout_examples/README.md` (index) and layout HTML files, `.claude/skills/singularity/gold_standards/presentations/team_status_update/README.md`

**The design language spec contains the full rules** (21 rules: 6 technical, 12 content, 3 process) and a common failure modes table. Read it. Do not rely on memory of what the rules are.

---

## Flow 8: Audit Engagement

**Questions to ask:**
1. Which engagement? (client/opportunity path)

**Mandatory pre-audit reading (hard gate):**

Before assessing ANYTHING about the engagement, the skill MUST read these files to understand the current spec. The skill definition is the sole source of truth. Do not assume what the structure should look like — read it.

1. `.claude/skills/singularity/SKILL.md` — structural rules, flows
2. `.claude/skills/singularity/references/folder_structure.md` — canonical folder structure, naming, week/day source organization
3. `.claude/skills/singularity/references/blockchain_methodology.md` — append-only rules, numbering, bridge documents
4. `.claude/skills/singularity/references/nested_singularity.md` — sub-singularity pattern (if sub-singularities are detected)
5. `.claude/skills/singularity/references/people_tracking.md` — dual people tracking system
6. `.claude/skills/singularity/references/health_check_methodology.md` — the full audit checklist and output format

**Process:**
1. Read all mandatory pre-audit files (above). This is non-negotiable.
2. Spawn explore agents to read the engagement deeply. Agents must actually read files, not infer from filenames. Cover: folder structure, source organization, research chain, document headers, people tracking, sub-singularities, deliverables, planning.
3. Compare findings against the skill spec. Every conformance or non-conformance must trace to a specific rule in the reference docs.
4. Write the health check report to `/<engagement>/planning/health_check_<date>.md` using the format in `references/health_check_methodology.md`.
5. If issues were found, write the remediation plan to `/<engagement>/planning/remediation_plan_<date>.md`.
6. Present the findings to the user. Do NOT execute any remediation actions without explicit user approval per action. Never move files without permission. Never delete files without permission.

**Load references:** `.claude/skills/singularity/references/health_check_methodology.md`, `.claude/skills/singularity/references/folder_structure.md`, `.claude/skills/singularity/references/blockchain_methodology.md`

---

## Engagement Inventory

The stop hook automatically regenerates the engagement inventory after every skill invocation. The inventory script at `.claude/skills/singularity/scripts/generate_inventory.py` produces tree-view markdown files in `<engagement>/inventory/`:

- `master_map.md` — complete tree of every file
- `markdown_inventory.md` — all `.md` files only
- `non_markdown_inventory.md` — all non-`.md` files
- `folder_descriptions.md` — folders with descriptions and last-updated dates
- `sub_<name>.md` — one per sub-singularity (auto-detected)

This is fully automated. The inventory is a current-state snapshot that overwrites on each run. See `references/inventory_design.md` for design assumptions.

---

## Sub-Singularities

Sub-singularities are self-contained mini-singularities nested within an engagement for parallel tracks that would overwhelm the main research chain. The most common use case is team meeting processing (internal standups, team-to-counterpart syncs), but the pattern is general-purpose.

**When to create one:** When the engagement has a distinct track of activity with its own source materials, own timeline, and content that is supplementary to (not part of) the main engagement narrative. See `references/nested_singularity.md` for the full pattern, rules, and folder template.

**When invoked:**
1. Load `references/nested_singularity.md` for the pattern and rules
2. If processing a team meeting, also load `references/team_meeting_processing.md` for the standard passes
3. If the sub-singularity has a `tracking/` folder, also load `references/tracking_folder_pattern.md` for update rules

**Key rules:**
- Each sub-singularity has its own independent numbering chain (01, 02, 03...)
- The parent's `org_chart.md` is the single people reference (update it from sub-singularity people files)
- The `tracking/` folder is always created (living documents: action_items.md, blockers.md, decisions.md)
- The `cross_reference.md` file maps sub-singularity sets to parent sets when content overlaps
- One level of nesting only (no sub-sub-singularities)

**Worked example:** `worked_examples/cisco_team/`

---

## Sibling Skills

| Skill | When to Use | How to Offer |
|-------|------------|--------------|
| `/big4` | After drafting any deliverable or presentation | "Want me to run a quality review on this before finalizing?" |
| `/pptx-extractor` | User provides .pptx source material | "This is a PowerPoint file. I can use the pptx-extractor to pull the content into markdown before processing. Want me to do that?" |
| `/pdf-extractor` | User provides .pdf source material | "This is a PDF. I can extract the content to markdown first. Want me to do that?" |

---

## Web Research

When unfamiliar technologies, companies, or terms are encountered during any phase:

1. **Flag to the user.** "I noticed references to Microsoft Purview, Azure AI Foundry, and SpaCy NER. Want me to spawn research agents to investigate these in parallel?"
2. **If approved, spawn parallel research agents.** Each agent investigates one topic using WebSearch and writes findings directly to `/<client_name>/<opportunity_name>/research/<set>_research_<topic>_<date>.md`.
3. **Update glossary** if one exists at `/<client_name>/<opportunity_name>/planning/glossary_<date>.md`.

**When to offer a glossary:** If the engagement involves 3+ unfamiliar terms, or spans a domain BayOne has not worked in before, offer to create one.

---

## Glossary (Optional)

Located at `/<client_name>/<opportunity_name>/planning/glossary_<date>.md`. Living document (editable, not append-only). Research agents populate it during source processing. New terms added as discovered in subsequent sets.

---

## Cross-Session Artifacts

Singularity creates markdown documents that serve as prompts for other Claude sessions:
- **Pricing specs** in `/<client_name>/<opportunity_name>/pricing/` become prompts for Claude in Excel
- **Correction prompts** in `/<client_name>/<opportunity_name>/pricing/` capture iterative feedback for Excel sessions
- **Design spec update handoffs** in `/<client_name>/<opportunity_name>/planning/` guide other sessions on updating shared assets

These are part of the engagement record and should have clear, dated filenames.

---

## Worked Example

`.claude/skills/singularity/worked_examples/lam_research/` contains the complete Lam Research engagement showing every document set, bridge document, org chart, and deliverable produced by this methodology. Read through it to see what good output looks like end-to-end.

---

## Stop Hook (Skill-Scoped)

The Stop hook is defined in this skill's frontmatter. It only fires when singularity is active, not on every session. It verifies engagement artifacts exist using the Proof via Artifact pattern. The script lives at `.claude/skills/singularity/scripts/singularity_stop.py`.
