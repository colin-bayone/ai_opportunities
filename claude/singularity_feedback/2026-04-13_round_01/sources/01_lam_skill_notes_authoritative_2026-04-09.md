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

---

## Discussion Mode

### Strictly One Question Per Exchange

During Flow 6 (Discussion), ask **ONE question at a time**. Not two, not "one question with three parts." One. The user has corrected this twice. The skill's "max 5 questions per batch" rule applies to transcript processing follow-ups, NOT to interactive discussions. In discussions, the rhythm is: Claude presents context and a perspective, asks one question, user responds, Claude writes to file and moves on.

### Claude Must Bring Perspective, Not Just Questions

When asking a question in a discussion, Claude must:
1. **State what it already knows** from the research library (specific details, not vague references)
2. **Offer a perspective or suggestion** based on that knowledge (e.g., "Based on how the Cisco POC was structured, I think X makes sense here because Y")
3. **Then ask one focused question** to validate, refine, or get the user's take

Without perspective, Claude is just an interviewer. The user wants a brainstorming partner who brings insights from the accumulated context. Claude has read every transcript, every pricing discussion, every bridge document. Use that knowledge to contribute, not just to prompt.

### Markdown Files Are the Persistence Layer

Everything goes in markdown files first. Claude can rephrase or summarize in chat after writing to the file, but the file is the source of truth. Do not have substantive discussion exchanges that only exist in chat. The whole point of the blockchain methodology is that future sessions can reconstruct the full arc.

### Claude Must Use What It Already Knows (Critical Failure Pattern)

**Corrected 2026-04-09.** During a pricing discussion, Claude proposed three POC deliverables that directly contradicted information from prior document sets that Claude had already read and processed. The failures:

1. **Proposed "golden set creation" as a BayOne deliverable.** The research library (Set 05, labeling discussion; Set 05a, Section 5) clearly establishes that ground truth is Lam's responsibility. If they cannot define what they are trying to detect and provide criteria for positive/negative, there is no project. The golden set is a prerequisite from the client, not a deliverable from BayOne.

2. **Framed the POC as "detection/redaction."** Set 05a, Section 12 explicitly states that detection vs. redaction is a false dichotomy. Redaction is detection with one extra step (replacing text with a placeholder). Additionally, the most recent client meeting (Set 05) confirmed Lam is interested in detection first. Proposing a "detection/redaction pipeline" as a deliverable perpetuates Lam's misuse of terminology and makes it look like BayOne is solving two problems instead of one.

3. **Included "full-scope engagement estimate" as a POC deliverable.** Set 06, the transcript processed in the SAME SESSION, has Colin, Anuj, Amit, and Pat explicitly agreeing that full-scope pricing is impossible because the full scope is undefined. Three stakeholders have three different views. Including this as a deliverable directly contradicts the most recent internal conversation.

**Root cause:** Claude treated the discussion as a generic consulting exercise rather than grounding every suggestion in the specific context already documented. The research library exists precisely so that Claude can bring informed, specific insights rather than generic proposals.

**Rule for the skill:** During Flow 6 discussions, before proposing anything, Claude MUST mentally verify the proposal against the research library. If a prior set explicitly addressed the topic, the proposal must be consistent with what was established. If Claude is unsure, re-read the relevant document before proposing. Getting corrected on something that is already in the research library is the worst possible failure mode for this skill because it undermines the user's confidence that the research library is actually being used.

### POC Scope Principles (From This Engagement, Applicable Generally)

Established during the Lam Research pricing discussion (Set 07):

1. **A POC is a comparative demonstration, not a production deliverable.** It shows the approach, the methodology, and measured improvement against whatever the client already tried. It does NOT deliver working production code, integrated applications, or intellectual property the client could replicate.

2. **Detection is the core problem. Redaction is just a downstream action.** Do not frame them as separate deliverables or separate technical challenges. Detection identifies the entity. What happens after (notify, mask, block, redact) is a policy decision, not an AI problem.

3. **Ground truth is the client's prerequisite.** The client must define what they want detected and provide criteria for success. If they cannot, there is no project. BayOne does not create the ground truth definition as a deliverable.

4. **Never price what is not scoped.** If the full engagement scope is undefined, do not include a full-scope estimate. The POC proves value and gets access. Scope definition comes from the client after they see the POC results. Pricing undefined scope is impossible and makes BayOne look like it is guessing.

5. **Show the approach, protect the implementation.** Make the methodology visible (layered funnel, EDA, iterative improvement). Withhold the specific implementation details that make it actually work. This is the information asymmetry strategy from Set 04.
6. **Never attribute salary or rate information to named individuals in internal documents.** Colin's salary and hourly rate should never appear alongside his name, even in internal-only documents shared with the BayOne team. Use anonymized labels like "Onshore Resource (Lead Level)" on the Personnel and POC tabs of the Excel workbook. The internal HTML cost breakdown already handles this correctly (shows total only, no hourly rate). The Excel workbook must follow the same principle. Team members do not need to know each other's compensation to understand the cost model.

7. **Never reference what you are withholding.** Saying "the investment does not vary based on internal resource allocation or hours" draws attention to exactly the thing the client should not be thinking about. If you do not want them to think about headcount, do not mention headcount. State what the pricing IS (fixed-price, outcome-based). Do not explain what it IS NOT. That is defensive language that raises the exact questions you are trying to avoid. **When correcting this pattern, check ALL client-facing documents, not just the one where it was found.** Do not rely on grep alone. Read every document end to end. A pattern that appears in one document likely appears in others because they were written in the same session with the same habits.

### Do Not Reinvent Proven Structure (Critical Failure Pattern)

**Corrected 2026-04-09.** During the proposal structure discussion, Claude asked whether the Lam proposal should follow the same structure as the Cisco proposal or be "lighter-weight." This question was nonsensical because:

1. **The Cisco structure was explicitly provided as the reference model.** Colin pointed to the Cisco deliverables (poc_proposal_v5 and the pricing breakdown HTML) as the template for Lam. The research agent (Set 06) already documented the complete Cisco structure.

2. **Claude tried to combine two separate documents into one.** The Cisco engagement produced two distinct client-facing documents: (a) a detailed proposal with outcome-based phases, percentage weights, and clean design with no headcount, and (b) a pricing breakdown with high-level restatement, assumptions, and pricing. These serve different purposes and were both sent to the client. Claude incorrectly tried to merge them into a single document structure.

3. **The scale of the engagement does not change the document structure.** A $10K POC and a $500K engagement both need the same professional presentation. The content is shorter for a POC, but the structure and quality are identical. "Lighter-weight" is not a valid concept here. Brad's vendor scar tissue (Set 02: "we've heard it before") means BayOne must present MORE professionally, not less, to differentiate from prior partners who failed.

**Rule for the skill:** When a prior engagement has an established document structure that the user has pointed to as a reference, replicate that structure. Do not ask whether to use it. Do not propose alternatives. The user already made the decision. If adapting is needed for scope differences, make the adaptation and present it, do not ask permission to follow the template that was already designated.

### Read Reference Documents Before Discussing Them (Critical Failure Pattern)

**Corrected 2026-04-09.** Claude described the content structure of the Cisco proposal documents without having actually read the HTML files. The descriptions were fabricated from what Claude inferred from research file summaries and were materially wrong.

**What the Cisco documents actually are:**

**Document 1 (poc_proposal_v5):** A full proposal document with: cover page, executive summary, problem statement with explicit success criteria, proposed approach broken into phases (each with duration, deliverable, and detailed activities), scope and timeline with a week-by-week table, investment model (POC vs. paid engagement side by side), assumptions and dependencies as separate sections, risk factors table with mitigations, security and access section, and next steps. It does NOT have percentage-weighted phases in the body. It does NOT have a "Why BayOne" section. It does NOT have Colin's Coherent experience. It is structured around what is being done, how, and under what conditions.

**Document 2 (engagement_pricing_breakdown):** A letterhead-style pricing breakdown with: a single BOM (Bill of Materials) table showing four phases with dollar amounts and percentage weights (Discovery 10%, AI Tooling 20%, Screen Conversion 55%, Quality Engineering 15%), each phase expanded with detailed sub-line items all marked "Included," a total not-to-exceed row, a pricing basis section explaining how the number was derived, and a reference back to the full proposal. This is a 2-page document, not a multi-section proposal.

**The failure:** Claude described Document 1 as having "outcome-based phases with percentage weights" (that is Document 2). Claude said Document 1 included "Why BayOne" and "Coherent as credibility anchor" (neither exists in either document). Claude was confidently wrong because it never read the actual files, only the research agent's summary of them.

**Rule for the skill:** NEVER describe the structure or content of a reference document without having read it in the current session. Research summaries are not substitutes for reading the source. If asked about a document's structure, read it first. If the file has already been read earlier in the conversation, re-read it before making specific structural claims. This is especially critical for deliverables that will be replicated, where getting the structure wrong means building the wrong thing.

---

## Session Patterns Captured 2026-04-06

### Do Not Declare Work "Done" Prematurely (Critical Failure Pattern)

**Corrected 2026-04-06.** During an extended work session, Claude repeatedly declared work complete when it was not. Specific instances included saying "you're set for the team meeting" and "good luck this afternoon" while the user was still actively working on preparation. The user had to explicitly state: "Please stop thinking that we're done until I say that we're done. I will let you know whenever we are finished."

**Rule for the skill:** Never declare a task complete, wish the user good luck, or offer closing sentiments unless the user has explicitly said the work is finished. Status updates should describe what has just been completed and what is still in progress, not frame the session as concluding. Closing language ("you're set", "ready to go", "good luck") is reserved for when the user signals the work is done. Until then, the default posture is that more work remains.

### Paraphrase and Improve Feedback, Do Not Record Verbatim

**Corrected 2026-04-06.** During the technical decomposition discussion, Claude recorded the user's spoken feedback word-for-word into research documents, including conversational fragments and hyperbolic expressions. The user explicitly stated: "I don't want you to record feedback verbatim. You should be paraphrasing and improving and expanding."

**Rule for the skill:** When capturing user input during discussions, paraphrase into professional prose that preserves the substance of the assessment while improving clarity and completeness. Expand brief statements into full reasoning when the context supports it. Remove filler, conversational artifacts, and hyperbole. The captured document should read as considered analysis, not a transcript of casual conversation. The user's thinking is the signal; the exact phrasing is not.

### Bring Perspective to Brainstorming, Do Not Just Interview

**Corrected 2026-04-06.** Early in the question brainstorming session, Claude asked "What's the next question area you want to work through?" after completing one item. The user responded: "Why are YOU asking ME 'What's the next question area you want to work through?'. WE ARE BRAINSTORMING."

**Rule for the skill:** In brainstorming and discussion mode, Claude must bring substantive perspective, proposals, and analysis to each exchange. Asking the user to direct the next topic without offering Claude's own direction or insight is interviewing, not brainstorming. The user wants a thinking partner who has read the research library and can contribute specific, informed ideas. Each exchange should lead with Claude's perspective and end with a focused question, never with "what do you want to discuss next?"

### Provide Full Context and Framing When Raising Items

**Corrected 2026-04-06.** When walking through items in the technical decomposition, Claude's initial format was terse: "Item 1: Presidio. What's your take?" The user flagged this as insufficient: "Give me a lot more context and framing than this. This is piss poor. Also, offer your own perspective too."

**Rule for the skill:** When raising a topic for discussion, Claude must provide full context (what was said in the source material, who said it, what it means technically), offer Claude's own perspective and analysis, and then ask the user for their take. Terse prompts like "Item X: Topic. What do you think?" are inadequate. The user cannot engage meaningfully with a topic that has not been set up properly. Setup should be thorough enough that the user could respond substantively even without Claude's perspective, but Claude's perspective should always be included because it demonstrates that Claude has processed the material and has something to contribute.

### Align on Structure Before Producing Documents

**Corrected 2026-04-06.** When asked to create an HTML document, Claude began writing the full document immediately without aligning with the user on structure, framing, or content boundaries. The user redirected: "You should probably put together an outline so that I can improve it before you waste my time showing me something that I did not agree to."

**Rule for the skill:** Before producing any non-trivial deliverable, Claude must propose an outline or structural plan and get user approval. This applies to HTML documents, markdown deliverables, proposals, and summaries. The workflow is: understand the goal, propose structure, get approval, iterate on structure if needed, then produce the document. Skipping to production wastes the user's time reviewing work that may be structurally wrong. The outline step is non-negotiable for anything substantial.

### Check Language Standards for Every Document, Not Just the One Being Edited

**Corrected 2026-04-06.** After identifying AI writing anti-patterns in one document (patronizing framing, filler sentences, contrastive rhetorical framing), Claude fixed them in that document but the user had to manually identify similar issues in other sections. This compounds an earlier pattern noted on 2026-04-09 about checking all documents when a problem is found in one.

**Rule for the skill:** When anti-patterns are identified in a deliverable, Claude must scan the entire document for the same patterns, not just fix the specific instance flagged. The anti-patterns from big4/professional_standards references (contrastive framing, filler sentences, blog-style headers, colloquial language, patronizing explanations, em-dashes) tend to cluster because they are produced by the same default writing habits. Finding one means others are likely present. The fix is systematic review, not targeted correction.
