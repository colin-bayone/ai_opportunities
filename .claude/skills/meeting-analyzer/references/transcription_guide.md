# Transcription Error Guide

Common patterns in speech-to-text transcripts and strategies for identifying/correcting them.

---

## Contents

1. [Common Error Patterns](#common-error-patterns)
2. [Detection Strategies](#detection-strategies)
3. [Clarification Dialogue Examples](#clarification-dialogue-examples)
4. [Correction Application](#correction-application)

---

## Common Error Patterns

### 1. Names Rendered as Common Words

**Pattern:** Person's name sounds like an English word or phrase.

| Transcription Error | Likely Actual Name | Clue |
|--------------------|-------------------|------|
| "the worker" | Divakar | Repeated in contexts where a person should be |
| "Java" / "Gerard" / "Jarra" | Zahra | Used in greetings, non-programming context |
| "sue knee" / "shriney" | Srinivas/Srini | Indian name, tech context |
| "a run" / "around" | Arun | Director/VP context |
| "rom" / "rama" | Rama | Manager context |
| "call in" / "calling" | Colin | Repeated as speaker attribution |
| "new leash" / "Nilesha" | Nilesha | Leadership mention |
| "milesh" / "my lash" | Milesh | Management context |

### 2. Technical Terms Misheard

**Pattern:** Technical tools/platforms rendered as similar-sounding words.

| Transcription Error | Likely Actual Term | Clue |
|--------------------|-------------------|------|
| "basil" / "bezel" | Bazel | Build system context |
| "total less" / "at last" | Atlas | Platform/infrastructure context |
| "deep site" / "deep sight" | DeepSight | AI platform context |
| "air flow" | Airflow | CI/CD, orchestration context |
| "jenkins" (usually correct) | Jenkins | CI/CD context |
| "pod man" | Podman | Container context |
| "jira" (usually correct) | Jira | Issue tracking context |
| "get hub" / "git hub" | GitHub | Code repository context |
| "splunk" (usually correct) | Splunk | Logging context |

### 3. Acronyms Expanded or Mangled

**Pattern:** Acronyms spelled out phonetically or misheard entirely.

| Transcription Error | Likely Actual Term | Clue |
|--------------------|-------------------|------|
| "and XOS" / "nexus" | NX-OS | Cisco operating system |
| "S D N" / "sedan" | SDN | Software-defined networking |
| "M C P" | MCP | Model Context Protocol |
| "L C P" | LCP (or MCP) | Verify with context |
| "a p i" | API | Common, usually clear |
| "c i c d" / "see I see dee" | CI/CD | Continuous integration |
| "S R T" | SRT | Selective Regression Testing |
| "D D T S" | DDTS | Bug tracking system |
| "cack" / "cat" | CAT/CAC | Commit Approval Tool |

### 4. Company/Organization Names

**Pattern:** Organization names phonetically rendered.

| Transcription Error | Likely Actual Term | Context |
|--------------------|-------------------|---------|
| "bay one" / "be one" | BayOne | Consulting company |
| "Cisco" (usually correct) | Cisco | Usually fine |
| "red hat" (usually correct) | Red Hat | Linux/container context |
| "anthropic" (usually correct) | Anthropic | AI context |

### 5. Indian English Patterns

**Pattern:** Indian English pronunciations and cadence affect transcription.

Common patterns:
- Dropped articles: "the" may be added where not spoken
- "Right" used as confirmation: May appear as "write" or "rite"
- "Actually" frequently used: Usually transcribed correctly
- "Basically" frequently used: Usually transcribed correctly
- Numbers may be spelled out unexpectedly

### 6. Context Switching Errors

**Pattern:** When speakers switch topics, transcription often lags.

Signs:
- Sentence suddenly doesn't make grammatical sense
- Topic seems to jump without transition
- Quote attribution seems wrong

Strategy: Read surrounding context and reassign if needed.

---

## Detection Strategies

### Strategy 1: Frequency Analysis

If a nonsensical phrase appears 5+ times, it's likely a mistranscribed proper noun.

**Example:**
- "the worker" appears 12 times → Probably a person's name
- "basil" appears in build context 6 times → Probably "Bazel"

### Strategy 2: Context Mismatch

When a word doesn't fit the context:
- "Java" in a greeting → Probably a person (Zahra)
- "basil" in CI/CD discussion → Probably Bazel
- "total less" as a platform → Probably Atlas

### Strategy 3: Phonetic Similarity

Sound out the error and consider alternatives:
- "the worker" → sounds like "Divakar"
- "sue knee" → sounds like "Srini"
- "Nilesha" → sounds like "Nilesha" (sometimes correct!)

### Strategy 4: Role/Position Clues

When someone is referred to by title then name:
- "The director, [garbled]" → Look for director names
- "Our manager, [garbled]" → Look for manager names
- "AI guy, [garbled]" → Person responsible for AI

### Strategy 5: Meeting Context

Use meeting metadata:
- If you know participants, match unknown names to known list
- If you know the topic, technical terms should align
- If you know the organization, use their terminology

---

## Clarification Dialogue Examples

### Example 1: Simple Name Clarification

**Claude:**
> I noticed "the worker" appears 12 times in the transcript, often in positions where a person's name should be. Is this possibly "Divakar" or another name?

**User:** Yes, that's Divakar - our engineering lead.

**Claude:** Thanks! I'll fix all 12 instances of "the worker" → "Divakar" throughout.

---

### Example 2: Multiple Corrections Needed

**Claude:**
> Before I analyze this transcript, I noticed several likely transcription errors:
>
> **People (uncertain):**
> - "the worker" (12 occurrences) - Is this "Divakar"?
> - "Java" in greetings (3 occurrences) - Could this be "Zahra"?
> - "sue knee" (8 occurrences) - Is this "Srinivas" or "Srini"?
>
> **Technical terms (uncertain):**
> - "basil" in build context (6 occurrences) - Is this "Bazel"?
> - "total less" as a platform name (4 occurrences) - Could this be "Atlas"?
>
> Please confirm or correct these.

**User:**
- the worker = Divakar, correct
- Java = Zahra, correct
- sue knee = Srinivas, we call him Srini
- basil = Bazel (Google's build system)
- total less = DeepSight Atlas (two words)

**Claude:**
Perfect! Here's my correction table:

| Error | Correction | Count |
|-------|------------|-------|
| the worker | Divakar | 12 |
| Java | Zahra | 3 |
| sue knee | Srinivas (Srini) | 8 |
| basil | Bazel | 6 |
| total less | DeepSight Atlas | 4 |

I'll apply these throughout before analysis.

---

### Example 3: Uncertain - Asking for Help

**Claude:**
> I'm not sure about some names in this transcript. Could you help identify:
>
> 1. Who is "new leash" or "Nilesha" - a person or something else?
> 2. Is "rom" referring to "Rama" or "ROM" (the memory type)?
> 3. "cack retooling" - is this "CAC" (an acronym) or something else?

---

## Correction Application

### Step 1: Build Correction Table

Always document corrections before applying:

```markdown
## Transcription Corrections

| Transcript Shows | Actually Means | Count | Confidence |
|------------------|----------------|-------|------------|
| the worker | Divakar | 12 | Confirmed by user |
| basil | Bazel | 6 | Confirmed by user |
| Java | Zahra | 3 | Confirmed by user |
```

### Step 2: Apply Globally

When creating documents, use the corrected versions everywhere. Never leave uncorrected errors.

### Step 3: Include Correction Note

At the top of `00_meeting_breakdown.md`, include:

```markdown
**Transcription Note:** Speech-to-text rendered "Divakar" as "the worker" throughout, "Bazel" as "basil", and "Zahra" as "Java". These have been corrected below.
```

### Step 4: Preserve Original for Context

If a quote is significant and the error adds context, you can note it:

> "basil [Bazel] is giving us problems"

But usually, just use the corrected version.

---

## When NOT to Correct

1. **If genuinely uncertain** - Ask first
2. **If it might be intentional** - Some teams use nicknames
3. **If the context is ambiguous** - Two valid interpretations
4. **If the speaker actually said it wrong** - Quote accurately if they misspoke

When in doubt, ask the user.
