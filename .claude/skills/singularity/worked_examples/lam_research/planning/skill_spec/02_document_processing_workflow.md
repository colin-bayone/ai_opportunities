# Document Processing Workflow

## Overview

This document describes how different types of source material are processed through the skill. The workflow changes depending on the source type, but the output always follows the blockchain methodology.

## Source Types

### Type 1: Meeting Transcripts (Primary Use Case)

Meeting transcripts are the most common and most complex source type. They require multi-pass reading and parallel agent execution.

**Processing Order:**

1. **Read prior context.** Before touching the transcript, read the previous set's summary document in `/<client_name>/<opportunity_name>/research/` and `/<client_name>/<opportunity_name>/org_chart.md`. This ensures continuity and avoids re-discovery of known information.

2. **Pass 1: People file.** Read the full transcript once. Write the people document (who was on the call, roles, titles, sentiment for each person). This is always the first file for a transcript set.

3. **Pass 1 continued: Topic map.** On the same or a second read, identify the major topics discussed. Write these as an outline/topic list. This becomes the roadmap for subsequent passes. Include a proposed list of detail files with rationale for why each needs its own file.

4. **Ask the user.** Present the proposed file list. Ask if they want to adjust, add, or remove files. The user controls what gets created.

5. **Pass 2+: Per-topic deep dives.** For each topic, read the transcript again focusing on that ONE topic. Write the documentation for that topic after that focused read. Then read again for the next topic. Write after every read, not once at the end.

   **Agent opportunity:** In the skill, each per-topic pass should be dispatched as a separate agent running in parallel. Each agent reads the full transcript with a specific topic focus and produces one output file. This is the natural parallelization point.

6. **Update org chart.** After all detail files are written, update `/<client_name>/<opportunity_name>/org_chart.md` with everything learned from the transcript.

7. **Bridge document.** If this is not the first set, write the bridge document capturing what changed between this set and the prior one (hypotheses validated/invalidated, new information, corrections).

8. **Summary document.** Always last. Short, high-level overview of everything in the set.

### Type 2: Call Prep Documents

Call prep documents are typically processed before the meeting they prepare for. They capture pre-meeting assumptions, hypotheses, strategy, and reference material.

**Processing Order:**

1. **Read the document.** Call preps are usually shorter and more structured than transcripts. A single read may be sufficient.

2. **Propose file breakdown.** Based on the content, propose how to split the document. Common splits:
   - Situational context (who the client is, what we know)
   - Discovery strategy (questions to ask, signals to listen for)
   - Technical reference (background research, stack details)
   - People (known contacts and their roles)

3. **Ask the user.** Confirm the file breakdown.

4. **Write the files.** Can be done sequentially or in parallel depending on complexity.

5. **Write the summary.** Last file for the set.

### Type 3: Internal Debriefs

Internal conversations (e.g., a sales debrief after a client meeting) are supplementary to the meeting they follow. They use the letter suffix convention (02a, 02b, etc.).

**Processing Order:**

1. **Read `/<client_name>/<opportunity_name>/org_chart.md` and the meeting summary** (in `/<client_name>/<opportunity_name>/research/`) that this debrief follows.

2. **Read the debrief transcript.**

3. **Propose file breakdown.** Common splits for internal debriefs:
   - People assessments (candid, internal views on client team)
   - Internal assessment (technical take, sales strategy, competitive intelligence)
   - Action items and next steps

4. **Ask the user.** Confirm the file breakdown.

5. **Write the files.** These are internal documents. Capture the tone honestly. Do not sanitize candid assessments, but do flag anything that should never appear in client-facing materials.

6. **Update `/<client_name>/<opportunity_name>/org_chart.md`** with any new people or updated assessments.

7. **Write the summary.** Last file for the set.

### Type 4: Working Discussions (User + Claude)

When the user wants to think through technical approach, strategy, or open questions with Claude, the conversation itself becomes a document set.

**Processing Order:**

1. **Read prior context.** Read the previous summary in `/<client_name>/<opportunity_name>/research/` and `/<client_name>/<opportunity_name>/org_chart.md`.

2. **Claude proposes discussion topics** based on what's known, what's open, and what needs decisions. Present as a batch of questions (max 5 per batch).

3. **User responds.**

4. **Write immediately.** After each exchange, write the discussed topics into a research file. Do not accumulate. Do not wait until the end.

5. **Continue the discussion.** Ask follow-up questions (max 5 per batch). Write after each exchange.

6. **Use "continued" files** if the discussion naturally extends beyond a single document. Each file should cover a coherent chunk of discussion.

7. **Write the summary** when the user indicates the discussion is complete.

**Special rules for discussions:**

- Capture the user's reasoning, not just conclusions. The "why" is as valuable as the "what."
- Flag open items explicitly. If the user says "this requires discovery" or "we need info from the sales team," that is an open item.
- Do not sanitize. Capture blunt assessments, strong opinions, and confidence claims honestly.
- Distinguish hyperbole from commitments. "I could do this in a day" is confidence in feasibility, not a timeline. Do not repeat it as a planning estimate.

### Type 4a: Strategy Discussion (Proactive Offering)

After the research library has 2+ document sets, the skill should proactively offer a strategy discussion. This is a specific variant of the working discussion focused on engagement positioning.

**Standard Strategy Questions (present as a batch):**

1. What does BayOne want from this engagement? (Staffing? Solutions? Advisory? Long-term relationship?)
2. What is BayOne's unique angle or credibility for this specific client?
3. Who has decision-making authority on the client side? Who influences but does not decide?
4. What are the client's explicit asks vs. implicit needs? (What they said they want vs. what they actually need)
5. What is the competitive landscape? Who else is the client talking to?

**Output:** Captured as a standard discussion set in `/<client_name>/<opportunity_name>/research/`. The positioning decisions feed directly into deliverable creation.

**When to offer:** After processing a discovery call or initial meeting transcript, when the research library has enough context to have a meaningful strategy conversation. The skill should say: "We have enough context to discuss BayOne's positioning for this engagement. Want to work through strategy before we draft deliverables?"

### Type 5: Emails and Written Communications

Emails, Slack messages, or other written communications can be processed as their own set or as supplementary material to a meeting.

**Processing Order:**

1. Determine if this is its own event (new set number) or supplementary (letter suffix).
2. Read the content.
3. Extract key information: decisions made, action items, new information, changes to prior understanding.
4. Write appropriate files (often fewer and shorter than transcript-based sets).
5. Update `/<client_name>/<opportunity_name>/org_chart.md` if needed.
6. Write summary.

## Multi-Pass Reading: Why It Matters

The multi-pass approach is the single most important processing rule. It exists because:

- **Context clearing.** Each pass starts fresh with one focus. The agent reads the entire transcript but only attends to one topic. This prevents the "everything blurs together" problem.
- **Exhaustive capture.** Details that would be missed in a single sweep get caught because the agent is looking for one specific thing.
- **Better organization.** Each file is written with focused intent after a focused read, producing tighter, more purposeful documents.
- **Natural parallelization.** Each per-topic pass is independent, making it ideal for parallel agent execution.

## Web Research During Source Processing

When processing any source material, the skill should watch for unfamiliar technologies, companies, domain-specific terms, or claims that need verification. When detected:

1. **Flag to the user.** "I noticed references to Microsoft Purview, Azure AI Foundry, and SpaCy NER. Want me to spawn research agents to investigate these in parallel?"
2. **Spawn parallel research agents** if the user approves. Each agent researches one topic and writes its findings to `/<client_name>/<opportunity_name>/research/<set>_research_<topic>_<date>.md`.
3. **Update the glossary** if one exists at `/<client_name>/<opportunity_name>/planning/glossary_<date>.md`. If the engagement involves heavy domain-specific terminology and no glossary exists yet, offer to create one.
4. **Incorporate findings** into subsequent research docs and deliverables.

Research agents run in parallel with deep-dive agents when possible. For example, while 5 deep-dive agents are processing a transcript by topic, 3 research agents can simultaneously investigate unfamiliar technologies mentioned in that transcript.

See `05_agent_architecture.md` for full research agent details (prompts, file paths, quality standards).

## Glossary (Optional)

Located at `/<client_name>/<opportunity_name>/planning/glossary_<date>.md`. Created when the engagement involves unfamiliar technology or domain-specific terminology.

**When to create:**
- The skill encounters 3+ terms that need definition during source processing
- The user asks for one
- The engagement spans a domain BayOne has not worked in before

**How it works:**
- Research agents populate it during source processing
- It is a living document (editable, not append-only)
- New terms are added as they are discovered in subsequent document sets
- Definitions include what it is, how it relates to the engagement, and source

## Question Batching

When asking the user follow-up questions during a discussion:

- **Maximum 5 questions per batch.** More than 5 overwhelms the user and leads to thin answers.
- If you have more questions, ask them in subsequent rounds after the first batch is answered.
- Prioritize questions that gate decisions or unblock progress.

## Source Material Quality

Transcripts are almost always speech-to-text and will be full of transcription errors: misspelled names, garbled technical terms, sentence fragments, speaker misattribution. The skill (and all agents) must apply common sense when reading them.

Examples of common transcription errors:
- "concept-renade" = "confidential violation"
- "lamb GPT" = "LamGPT"
- "Spacey" = "SpaCy"
- "on pram" = "on-prem"
- "kills that guy" = "builds that out"
- "brass beam" = "Brad's team"
- "compiler" = "Copilot"
- "Gapsium" / "Kaptima" = "Capgemini"

Do not take mangled words at face value. Infer the intended meaning from context. The skill should instruct all spawned agents to apply this same interpretation.
