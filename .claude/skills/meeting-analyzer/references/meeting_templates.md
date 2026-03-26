# Meeting Document Templates

Reference templates for the 4 standard meeting analysis documents.

---

## Contents

1. [00_meeting_breakdown.md](#1-00_meeting_breakdownmd)
2. [01_speaker_notes.md](#2-01_speaker_notesmd)
3. [02_crossover_analysis.md](#3-02_crossover_analysismd)
4. [03_sentiment_and_relationship.md](#4-03_sentiment_and_relationshipmd)

---

## 1. 00_meeting_breakdown.md

**Purpose:** Comprehensive breakdown of the meeting - the primary reference document.

```markdown
# Meeting [N]: [Descriptive Title]

**Date:** [Date]
**Location:** [In-person/Remote, room/link if relevant]
**Duration:** ~[X] minutes
**Recording Status:** [Recorded/Not recorded]

---

## Participants

| Name | Organization | Role | Scope in Meeting |
|------|--------------|------|------------------|
| [Name] | [Org] | [Title] | [What they covered] |

**Context:** [Any relevant background on why this meeting happened, who was expected vs showed up, etc.]

**Transcription Note:** [List known transcription corrections, e.g., "Speech-to-text rendered 'Divakar' as 'the worker' throughout"]

---

## Meeting Structure

[Describe phases/flow of meeting]

1. **Phase 1:** [Description] (~X min)
2. **Phase 2:** [Description] (~X min)
3. **Phase 3:** [Description] (~X min)

---

## Discussion Topics (Chronological)

### 1. [Topic Name]

[Detailed discussion of this topic]

**Key Points:**
- Point 1
- Point 2

**Key Quote ([Speaker]):**
> "[Verbatim quote]"

### 2. [Topic Name]

[Continue for each major topic]

---

## Decisions Made

| Decision | Made By | Context |
|----------|---------|---------|
| [Decision] | [Person] | [Why/context] |

---

## Commitments Made

### [Organization 1] Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| [Person] | [What they committed to] | [When] |

### [Organization 2] Commitments

| Who | Commitment | Timing |
|-----|------------|--------|
| [Person] | [What they committed to] | [When] |

---

## Open Items / Next Steps

| Item | Owner | Priority | Notes |
|------|-------|----------|-------|
| [Item] | [Person] | [High/Medium/Low] | [Context] |

---

## Key Quotes

**[Speaker] on [topic]:**
> "[Quote]"

**[Speaker] on [topic]:**
> "[Quote]"

---

## Key Insights

1. **[Insight title]:** [Explanation of what this means]

2. **[Insight title]:** [Explanation]

---

## Clarifications Needed

1. [Question that remains unclear]
2. [Another question]

---

## Next Meeting

**What:** [Purpose]
**When:** [Date/timeframe]
**Who:** [Participants]
**Purpose:** [Goal]

---

## Files Referenced

- [File or document mentioned]
- [Another reference]
```

---

## 2. 01_speaker_notes.md

**Purpose:** Quick reference organized by speaker - who said what.

```markdown
# Speaker Notes: Meeting [N] ([Participants])

Quick reference for who said what and their areas of ownership.

---

## [Speaker 1 Name] ([Role])

**Present:** [Duration/phases when present]

### On [Topic 1]

> "[Verbatim quote]"

> "[Another quote]"

### On [Topic 2]

> "[Quote]"

### Key Commitments

- [Commitment 1]
- [Commitment 2]

---

## [Speaker 2 Name] ([Role])

**Present:** [Duration/phases]

### On [Topic 1]

> "[Quote]"

### On [Topic 2]

> "[Quote]"

### Key Commitments

- [Commitment]

---

## [Continue for each speaker]

---

## Transcription Corrections

| Transcript Shows | Actually Means |
|------------------|----------------|
| [Error] | [Correction] |
| [Error] | [Correction] |

---

## Quick Reference

| Speaker | Main Topics | Key Takeaway |
|---------|-------------|--------------|
| [Name] | [Topics] | [One-liner] |
| [Name] | [Topics] | [One-liner] |
```

---

## 3. 02_crossover_analysis.md

**Purpose:** Map connections to other work. Only create when there's meaningful crossover.

**When to use:**
- Multiple projects discussed that overlap
- Same patterns/solutions apply elsewhere
- People connections across teams/projects
- Potential scope expansion or synergies

```markdown
# Crossover Analysis: [Meeting Topic] ↔ [Related Work]

This document maps the connections between [this meeting's topic] and [other relevant work].

---

## The [Two/Multiple] Projects

### [Project 1 Name]
- **Focus:** [What it's about]
- **Scope:** [Boundaries]
- **Key People:** [Names]

### [Project 2 Name]
- **Focus:** [What it's about]
- **Scope:** [Boundaries]
- **Key People:** [Names]

---

## How They Relate

[Diagram if helpful - use ASCII art or describe visually]

```
┌─────────────────┐    ┌─────────────────┐
│   PROJECT 1     │───▶│   PROJECT 2     │
│                 │    │                 │
│  • Feature A    │    │  • Uses Feature │
│  • Feature B    │    │  • Overlaps on  │
└─────────────────┘    └─────────────────┘
```

**[Speaker] explained:**
> "[Quote about relationship]"

---

## Shared Challenges

| Challenge | Project 1 | Project 2 |
|-----------|-----------|-----------|
| [Challenge] | [How it manifests] | [How it manifests] |

---

## Shared Solution Patterns

### 1. [Pattern Name]

**For Project 1:**
- [How it applies]

**For Project 2:**
- [How it applies]

**[Speaker]'s Statement:**
> "[Quote about pattern]"

---

## People Connections

| Person | Project 1 Role | Project 2 Role | Connection |
|--------|----------------|----------------|------------|
| [Name] | [Role] | [Role] | [How they connect] |

---

## Potential Synergies

### Build Once, Use Multiple Times

| Component | Build For | Also Useful For |
|-----------|-----------|-----------------|
| [Component] | [Primary] | [Secondary] |

---

## Risk: Scope Creep

**Current Scope:**
- [What's in scope]
- [What's NOT in scope yet]

**[Related work] Asks:**
- [What they want that could creep]

**Recommendation:**
1. [Recommendation]
2. [Recommendation]

---

## Action Items from Crossover

| Action | Owner | Notes |
|--------|-------|-------|
| [Action] | [Person] | [Context] |

---

## Key Insight

[One paragraph summary of what this crossover means strategically]
```

---

## 4. 03_sentiment_and_relationship.md

**Purpose:** Capture tone, enthusiasm, and relationship-building moments.

```markdown
# Sentiment & Relationship Notes: Meeting [N] ([Participants])

Capturing tone, enthusiasm, and relationship-building moments from [meeting description].

---

## Overall Tone

**Meeting Energy:** [Description - e.g., "Warm, collaborative, optimistic"]

**Duration Note:** [Did it run long? Cut short? Why?]

---

## [Speaker 1 Name] ([Role])

### [Sentiment Category 1 - e.g., "Enthusiasm for Partnership"]

[Interpretation of their sentiment]

> "[Supporting quote]"

*Interpretation: [What this suggests about their mindset]*

### [Sentiment Category 2 - e.g., "Openness About Challenges"]

[Description]

> "[Quote]"

*Interpretation: [Analysis]*

### [Continue for relevant categories]

---

## [Speaker 2 Name] ([Role])

### [Sentiment Category]

[Same format]

---

## Relationship Indicators

### Trust Signals
- [Signal 1 - what they shared that shows trust]
- [Signal 2]

### Interest Signals
- [Signal 1 - what indicated genuine interest]
- [Signal 2]

### Investment Signals
- [Signal 1 - what showed commitment beyond minimum]
- [Signal 2]

### Cultural Fit Signals
- [Signal 1 - alignment on values/approach]
- [Signal 2]

---

## Key Quotes Capturing Sentiment

**[Speaker] on [topic]:**
> "[Quote that captures their sentiment]"

**[Speaker] on [topic]:**
> "[Quote]"

---

## Comparison to Previous Meetings

| Aspect | Previous Meeting | This Meeting |
|--------|------------------|--------------|
| **Tone** | [Description] | [Description] |
| **Data Shared** | [What they shared] | [What they shared] |
| **Commitment Level** | [Description] | [Description] |
| **Enthusiasm** | [Description] | [Description] |

---

## Summary

[2-3 sentence summary of relationship state and what it means]

Key takeaways:
- **[Aspect 1]:** [Assessment]
- **[Aspect 2]:** [Assessment]
- **[Aspect 3]:** [Assessment]
```

---

## Usage Notes

1. **Adapt templates to context** - Not every section applies to every meeting
2. **Remove empty sections** - Don't include headers with no content
3. **Add sections as needed** - These are starting points, not constraints
4. **Crossover analysis is optional** - Only create when genuinely relevant
5. **Sentiment analysis is NEVER optional** - Always capture tone and relationship signals
