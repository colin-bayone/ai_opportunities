# Skill Notes: Code Meeting Decomposition

Running collection of do's, don'ts, and wisdom gathered during the Lam Research decomposition exercise. These notes will inform the creation of a new skill to replace the existing meeting-analyzer skill.

---

## Structure & Organization

- **Don't use a single massive file.** Break decomposition into purposeful groupings that have distinct reasons to exist separately - but don't go so granular that you have a file per paragraph. Each file should have a clear reason to be its own thing.

- **Include dates in filenames.** When the date of the source material is known, append it (e.g., `01_call_prep_situational_context_2026-03-12.md`). This makes chronological ordering unambiguous even outside the numbering system.

- **Document the methodology up front.** The very first document (00) should explain the decomposition approach and why it was chosen, so that any future reader or Claude session understands the rules before reading the content.

- **Every document set needs a summary.** The summary is the last file written for each set. It's short and high-level - its job is to let a future Claude session understand the set without reading every file. This is critical because the number and type of detail files will vary per set.

- **Track people in two places.** A per-meeting blockchain-style people document captures what was learned about people from that specific event. A living org chart at the session root is always current. The blockchain version preserves history; the org chart is the quick-reference truth.

- **Read prior context before processing new material.** Before decomposing a new document, read the previous summary and the current org chart. This ensures continuity and avoids re-discovery of known information. The skill should enforce this as a step.

- **Bridge documents go at the end.** Don't try to write what changed between document sets while you're still processing them. Bridge documents are retrospective and are written after both sets exist.

---

## Philosophy

- **The system should be self-describing.** A new Claude session with zero context should be able to read the methodology doc, then the summaries in order, and reconstruct the full state of the engagement. No tribal knowledge required.

- **Living documents are the exception, not the rule.** Almost everything is append-only. The org chart is a deliberate exception because its purpose is to be a current-state reference, not a historical record. The history is preserved in the per-set people documents.

---

## Numbering Convention: Supplementary Material

When supplementary material is tied to the same event as an existing document set (e.g., an internal debrief immediately after a meeting, a follow-up email the same day), use a **letter suffix** rather than a new number. For example:

- `02_meeting_*` = the meeting itself
- `02a_debrief_*` = internal debrief after the same meeting
- `02b_followup_email_*` = a follow-up email about the same meeting

This keeps it clear that the supplementary material is event-adjacent, not a new chronological step. The same blockchain rules apply: no editing prior documents.

### Numbering Is Purely Chronological

There is nothing special about what number a set gets. 01 is not always "call prep," 02 is not always "a meeting," 03 is not always "a discussion." The number reflects when in the project timeline the material was created or processed. A set could be a meeting transcript, a call prep doc, an internal discussion with Claude, an email chain, or anything else. The type of content determines the file names within the set, not the set number.

---

## Source Material Quality

**Transcripts are almost always speech-to-text.** They will be full of transcription errors -- misspelled names, garbled technical terms, sentence fragments, speaker misattribution. Use common sense when reading them. Don't take mangled words at face value; infer the intended meaning from context. Examples from this engagement:

- "concept-renade" = "confidential violation"
- "lamb GPT" = "LamGPT"
- "Spacey" = "SpaCy"
- "on pram" = "on-prem"
- "kills that guy" = "builds that out" (or similar)
- "brass beam" = "Brad's team"

The skill should instruct agents to apply this same common-sense interpretation when processing transcripts.

---

## Transcript Processing

### Standard Files (Every Transcript)

- **People file** - One file per transcript. Who was on the call, roles, titles, sentiment. Always created.
- **Summary** - Always last. Short, high-level overview of everything.
- **"What Changed" bridge document** - Also always last, written after all other docs for the set are done.

### Variable Files (Ask the User)

Beyond the people file, the set of detail files is NOT fixed. Different meetings will warrant different breakdowns. The skill should **ask the user** what files to create beyond the standard ones. Some common candidates:
- Technical deep dive breakdown (by topic)
- Business opportunity and specific notes
- Meeting breakdown and speaker notes
- Action items / next steps
- Hypothesis validation (what was confirmed/invalidated from prior sets)

The user knows what matters. Ask, don't assume.

### Discussion Sessions (User + Claude)

One valid document set type is a working discussion between the user and Claude to think through technical approach, strategy, or open questions. These get their own set number and are captured as they happen (write after each exchange, not at the end). The skill should support this as a mode.

### Question Batching

When asking the user follow-up questions during a discussion, **max 5 questions per batch.** More than 5 overwhelms the user and leads to thin answers. If you have more questions, ask them in subsequent rounds after the first batch is answered.

### Multi-Pass Reading (Critical)

Do NOT read a transcript once and try to produce everything from a single pass. This is the most important processing rule:

1. **Pass 1 - High-level overview.** Read the entire transcript. Identify the major topics discussed. Write these down as an outline/topic list. This becomes the roadmap for subsequent passes.

2. **Pass 2+ - Per-topic deep dives.** Read the transcript again focusing on ONE topic at a time. Write the documentation for that topic after that focused read. Then read again for the next topic.

3. **Write after every read, not once at the end.** Documentation is updated/created after each pass, not accumulated and dumped at the end. This ensures granular, accurate capture and clears context between topics.

4. **Agent opportunity.** In the skill, each per-topic pass could be dispatched as a separate agent. This is a natural parallelization point - each agent reads the transcript with a specific focus and produces one document.

### Agent File Writing

**UPDATE (2026-03-20, later session):** The agent write permission issue is RESOLVED. With `"Write($CLAUDE_PROJECT_DIR/claude/**)"` in `permissions.allow` in `.claude/settings.local.json`, agents can write files fully autonomously -- no user approval prompt required. All 5 deep-dive agents wrote their files without any user interaction. This was confirmed working with `mode: "bypassPermissions"` on the agent spawns.

Previous session (same date, earlier) reported this only worked in "semi-auto mode" requiring user clicks. That is no longer the case. The permission rule is sufficient for full autonomy.

**The skill should:**
- Pre-configure the Write permission in settings as part of skill setup (e.g., `"Write($CLAUDE_PROJECT_DIR/claude/**)"`)
- Agents write files directly -- no user approval needed
- NOT fall back to main-session sequential writing as a workaround
- NOT attempt to extract agent output from temp files with scripts

### Why Multi-Pass

- Clears context between topics so each gets full attention
- Prevents the "everything blurs together" problem of single-pass processing
- Produces better-organized output because each file is written with focused intent
- Catches details that would be missed in a single sweep

### Processing Order for Transcripts

1. People file first (who's there, what do we know)
2. High-level topic overview (pass 1)
3. Per-topic deep dives (passes 2+, one topic per pass, write after each)
4. Any additional requested files (business opportunity, speaker notes, etc.)
5. "What Changed" bridge document (last)
6. Summary (very last)

---

## Research Agents

Part of the skill should support launching research agents to look up external information in the context of the problem statement. Examples:
- Researching Azure AI Foundry capabilities for RAG architectures
- Researching Microsoft Purview custom Sensitive Information Types
- Validating technical claims from the meeting against current documentation

The user may ask for this at any point during the discussion. Research agents can also be used to re-explore existing decomposition docs for specific details (e.g., "find all mentions of Azure services across all 02 files"). This is encouraged -- going back to source material to verify or discover is always fine.

---

## Discussion Capture

When capturing a working discussion (user + Claude):
- **Write after each exchange, not at the end.** If the user gives a long answer covering 5 topics, write those into the 03 docs immediately. Don't accumulate.
- **Use "continued" files** if the discussion naturally extends beyond a single document. Each file should cover a coherent chunk of discussion.
- **Capture the user's reasoning, not just conclusions.** The "why" behind a technical decision is as valuable as the decision itself for future sessions.
- **Flag open items explicitly.** If the user says "this requires discovery" or "we need info from the sales team," that's an open item that should be tracked.
- **Don't sanitize.** If the user is blunt about a client's capability gaps or makes strong claims ("I could do this in a day"), capture that. It's part of the honest record.
- **Distinguish hyperbole from commitments.** When the user says something like "I could do this in a day," that's an expression of confidence in feasibility, not a timeline. Do NOT repeat it as a planning estimate, reference it in proposals, or fixate on it as a deliverable timeline. Capture the sentiment, not the literal claim.
- **Internal vs. external language.** Capture everything honestly in the research docs (internal), but flag anything that should never appear in client-facing materials. Examples: assessments of client competence, frustration with client's technical approach, competitive intelligence about prior partners.
