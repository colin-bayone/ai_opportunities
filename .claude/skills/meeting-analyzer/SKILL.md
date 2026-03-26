---
name: meeting-analyzer
description: |
  Analyzes meeting transcripts (speech-to-text) to produce comprehensive, organized notes with consistent structure.

  WHEN to use: User provides a meeting transcript and wants to summarize, analyze, or capture notes. Triggers include "process this meeting", "summarize the call", "create meeting notes", "analyze this transcript", or providing a transcript file path.

  WHEN NOT to use: General document summarization that isn't a meeting. Transcription services (this analyzes already-transcribed content). Quick single-question answers about a meeting.
---

# Meeting Analyzer

Analyze speech-to-text meeting transcripts and produce comprehensive, well-organized documentation.

---

## Hard Rules

1. **Always ask about transcription errors first** - Speech-to-text creates errors, especially for names and tools
2. **Create all 4 documents per meeting** - Never skip sentiment analysis or speaker notes
3. **Use Explore agent for context discovery** - Keep main context clean
4. **One meeting at a time** - Complete full analysis before moving to next
5. **Confirm folder structure before writing** - Ask if user created session folder already
6. **Never assume names** - When uncertain about a name (person, tool, product), ask for clarification
7. **Apply corrections globally** - Once a transcription error is identified, fix all instances
8. **Generate HTML for all documents** - Every markdown doc gets an HTML version

---

## Hook Enforcement

A Stop hook (`.claude/hooks/meeting-analyzer-workflow.py`) enforces the complete workflow.

**Opt-in:** The hook ONLY fires when the marker file `.meeting-analysis-active` exists in `claude/meeting-analyzer/`. Create this marker at skill start, remove on completion.

| Check | What It Verifies | How |
|-------|-----------------|-----|
| Context Discovery | `00_context_discovery.md` exists with content | File presence + >50 chars |
| Transcription Handling | `## Transcription` section header in breakdown | Regex match on heading |
| Required Documents | All doc types exist (pattern-matched) | `*_meeting_breakdown.md`, `*_speaker_notes.md`, `*_sentiment*.md` |
| HTML Generation | Every `.md` has a corresponding `.html` | File extension swap |

**This is not optional.** The hook ensures consistent, complete analysis every time.

---

## Workflow

### Phase 1: Session Setup

**Step 1.1: Create marker file (activates hook)**

```bash
mkdir -p claude/meeting-analyzer
touch claude/meeting-analyzer/.meeting-analysis-active
```

This marker tells the Stop hook to enforce the workflow. **Remove it when all meetings are complete.**

**Step 1.2: Create meeting folder**

```bash
mkdir -p claude/meeting-analyzer/meeting_<topic>_<date>
```

Naming: `meeting_kickoff_2026-02-17`, `meeting_regression_2026-02-17`, etc.

**Step 1.3: Confirm structure**

Expected structure:
```
claude/meeting-analyzer/
├── .meeting-analysis-active     # Marker file (remove when done)
├── meeting_<topic>_<date>/
│   ├── 00_context_discovery.md  # From Explore agent
│   ├── 01_meeting_breakdown.md
│   ├── 02_speaker_notes.md
│   ├── 03_crossover_analysis.md # (if applicable)
│   └── 04_sentiment_and_relationship.md
└── meeting_<topic2>_<date>/
    └── ...
```

---

### Phase 2: Context Discovery

**Step 2.1: Explore the project and write findings**

Before analyzing transcripts, spawn an Explore agent and **write findings to `00_context_discovery.md`**:

```
Task(subagent_type="Explore", prompt="Explore this project to understand:
1. What is this project about? (check CLAUDE.md, README, project/)
2. Who are the key people involved? (check existing documents)
3. What existing meetings or context exists? (check claude/*, documents/)
4. What tools, platforms, or systems are relevant?

Return a summary of key context that will help analyze meeting transcripts.")
```

**CRITICAL:** Write the Explore agent's findings to `00_context_discovery.md` in the meeting folder. The Stop hook checks this file exists with content.

```markdown
# Context Discovery

## Project Overview
[Summary from Explore agent]

## Key People
[Names and roles identified]

## Relevant Systems/Tools
[Platforms, tools, acronyms to watch for]
```

**Step 2.2: Ask clarifying questions based on context**

After exploration, if the project has existing context:
- Confirm key people names
- Confirm tool/platform names
- Ask about relationships to existing work

---

### Phase 3: Per-Meeting Analysis

For EACH meeting transcript:

**Step 3.1: Initial transcript review**

Read the transcript and identify:
- Likely transcription errors (names, tools, acronyms)
- Number of speakers
- Meeting type (kickoff, status, discovery, etc.)

**Step 3.2: Transcription error clarification**

Present suspected errors and ask for corrections:

> "I noticed some likely transcription errors:
> - 'the worker' appears frequently - is this a person's name?
> - 'basil' mentioned in build context - could this be 'Bazel'?
> - 'Java' in a non-programming context - could this be a person?
>
> Please confirm or correct these, and I'll fix them throughout."

**IMPORTANT:** Create a correction table and apply fixes globally before analysis.

**Step 3.3: Generate the required documents**

See `.claude/skills/meeting-analyzer/references/meeting_templates.md` for complete templates.

| Doc | File | Purpose |
|-----|------|---------|
| 1 | `01_meeting_breakdown.md` | Comprehensive breakdown: participants, topics, decisions, commitments, open items, key quotes |
| 2 | `02_speaker_notes.md` | Quick reference by speaker with verbatim quotes |
| 3 | `03_crossover_analysis.md` | Connections to other work (if applicable - ask user) |
| 4 | `04_sentiment_and_relationship.md` | Tone, enthusiasm, trust signals, relationship indicators |

Note: `00_context_discovery.md` was created in Phase 2. Numbering may vary if crossover is skipped.

**CRITICAL:** The meeting breakdown MUST contain a `## Transcription` section header. This can document corrections made, or note that no errors were found:

```markdown
## Transcription

No significant transcription errors were identified in this recording.
```

or:

```markdown
## Transcription

The following corrections were applied throughout this document:
| Original | Corrected |
|----------|-----------|
| "the worker" | Divakar |
| "basil" | Bazel |
```

**Step 3.5: Confirm and summarize**

After creating all documents, summarize:
- Key findings from this meeting
- Major decisions made
- Open items requiring follow-up
- Notable sentiment highlights

Ask: "Ready for the next meeting, or would you like to refine anything?"

---

### Phase 4: HTML Generation (Required)

After creating markdown documents, generate HTML versions. A Stop hook enforces this - completion will be blocked until all HTML files exist.

**Step 4.1: Generate HTML for each document**

For each markdown document created, generate a corresponding HTML version:

| Markdown | HTML |
|----------|------|
| `00_context_discovery.md` | `00_context_discovery.html` |
| `01_meeting_breakdown.md` | `01_meeting_breakdown.html` |
| `02_speaker_notes.md` | `02_speaker_notes.html` |
| `03_crossover_analysis.md` | `03_crossover_analysis.html` |
| `04_sentiment_and_relationship.md` | `04_sentiment_and_relationship.html` |

**Step 4.2: Apply BayOne design system**

See `.claude/skills/meeting-analyzer/references/html_output_guide.md` for:
- Complete HTML template structure
- CSS styling (purple gradient brand, Inter font)
- Document-specific templates for each meeting doc type
- Print-optimized formatting

**Key HTML elements:**
- Cover page with gradient background and meeting title
- Numbered sections (01, 02, 03...)
- Tables with purple headers
- Quote blocks with left border styling
- Footer with document metadata
- Print styles for 8.5" x 11" output

**Step 4.3: Place HTML files**

Save HTML files alongside their markdown counterparts in the meeting folder:

```
claude/meeting-analyzer/meeting_<topic>_<date>/
├── 00_context_discovery.md
├── 00_context_discovery.html
├── 01_meeting_breakdown.md
├── 01_meeting_breakdown.html
├── 02_speaker_notes.md
├── 02_speaker_notes.html
├── 03_crossover_analysis.md      # (if applicable)
├── 03_crossover_analysis.html
├── 04_sentiment_and_relationship.md
└── 04_sentiment_and_relationship.html
```

**Step 4.4: Remove marker file (workflow complete)**

```bash
rm claude/meeting-analyzer/.meeting-analysis-active
```

This deactivates the Stop hook for future sessions.

---

## Transcription Error Handling

Speech-to-text transcripts ALWAYS have errors. Common patterns:

| Pattern | Likely Cause | Example |
|---------|--------------|---------|
| "the worker" or similar | Person's name phonetically similar | "the worker" → "Divakar" |
| Random food/plant names in technical context | Tool/platform name | "basil" → "Bazel" |
| Wrong programming language as name | Person's name | "Java" → "Zahra" |
| "total less" or nonsense phrases | Proper noun | "total less" → "Atlas" |
| Inconsistent capitalization of same term | Product/tool name | "deep sight" → "DeepSight" |

**When in doubt, ASK.** A 30-second clarification saves hours of confusion.

See `.claude/skills/meeting-analyzer/references/transcription_guide.md` for detailed patterns.

---

## Document Quality Standards

### 00_context_discovery.md
- Project overview from Explore agent
- Key people with roles
- Relevant systems, tools, acronyms
- Must have >50 characters of content (hook enforces this)

### 01_meeting_breakdown.md
- Include all participants with roles
- **MUST include `## Transcription` section** (hook enforces this)
- Chronological discussion flow
- Link decisions to who made them
- Cross-reference to project documents when relevant
- Key quotes with attribution

### 02_speaker_notes.md
- Organized by speaker
- Include verbatim quotes (cleaned of obvious transcription errors)
- Note topics each person owned
- Highlight commitments made by each person

### 03_crossover_analysis.md (when applicable)
- Map connections between this meeting's content and other work
- Identify shared challenges, patterns, or opportunities
- Note people connections across projects
- Flag potential synergies or conflicts

### 04_sentiment_and_relationship.md
- Overall meeting tone/energy
- Per-person sentiment analysis with supporting quotes
- Trust signals (what did they share that shows trust?)
- Interest signals (what indicated genuine interest?)
- Relationship quality indicators
- Comparison to previous meetings if applicable

---

## Example Clarification Dialogue

**User provides transcript**

**Claude:**
> I've done an initial read of the transcript. Before I create the full analysis, I noticed some likely transcription errors:
>
> **People (uncertain):**
> - "the worker" appears 12 times - Is this "Divakar" or another name?
> - "Java" mentioned in greetings context - Could this be "Zahra"?
>
> **Tools/Platforms (uncertain):**
> - "basil" in build system context - Is this "Bazel"?
> - "total less" seems like a platform name - Could this be "Atlas"?
>
> Please confirm or correct these so I can apply fixes throughout.

**User confirms/corrects**

**Claude applies corrections, then proceeds with full analysis**

---

## References

- `.claude/skills/meeting-analyzer/references/meeting_templates.md` - Full templates for all 4 document types
- `.claude/skills/meeting-analyzer/references/transcription_guide.md` - Common transcription error patterns
- `.claude/skills/meeting-analyzer/references/html_output_guide.md` - BayOne design system HTML templates and CSS
- `.claude/hooks/meeting-analyzer-workflow.py` - Stop hook enforcing workflow compliance

---

## Partial Workflow Execution

Users can invoke specific phases of the workflow on demand. This is useful when:
- Markdown documents already exist and only HTML generation is needed
- Re-running a specific phase after corrections
- Testing individual workflow components

### Supported Partial Commands

| User Request | Phase Executed | Requirements |
|--------------|----------------|--------------|
| "generate HTML for meeting docs" | Phase 4 only | Markdown files must exist |
| "analyze this transcript" | Phase 3 only | Session folder must exist |
| "create session folder" | Phase 1 only | None |
| "explore project context" | Phase 2 only | None |

### Examples

**HTML Only:**
> "Generate HTML versions for the meeting documents in `claude/meeting-analyzer/`"
>
> Claude: Finds all `.md` files, generates corresponding `.html` using BayOne design system.

**Re-analyze Single Meeting:**
> "Re-analyze the transcript for meeting_kickoff_2026-02-17 with the corrected names"
>
> Claude: Runs Phase 3 for that meeting only, regenerates all docs + HTML.

**Add Missing Crossover Analysis:**
> "Create crossover analysis for meeting_kickoff - I forgot to mention the connections"
>
> Claude: Creates `03_crossover_analysis.md` and `.html` for that meeting.

### Hook Behavior in Partial Mode

The Stop hook checks for **completed state** at conversation end. When running partial workflows:
- Hook only fires if `.meeting-analysis-active` marker exists
- If starting from existing documents, the hook verifies all required outputs exist
- Missing documents from earlier phases will still trigger the hook
- Remove marker file to bypass hook when doing partial work on legacy folders

---

## Notes

- This skill is **portable** - works for any project with meeting transcripts
- Assumes transcripts are **already transcribed** (speech-to-text output)
- Uses **dedicated folder** `claude/meeting-analyzer/` for all output
- Uses **marker file** `.meeting-analysis-active` to activate/deactivate hook enforcement
- Uses **Explore agents** to gather project context (writes to `00_context_discovery.md`)
- Generates **polished HTML versions** using BayOne design system (required)
- **Remove marker file** when all meetings are complete to deactivate hook
