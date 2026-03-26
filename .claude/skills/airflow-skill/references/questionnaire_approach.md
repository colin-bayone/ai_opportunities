# Questionnaire Approach

**Date:** 2026-01-29
**Status:** DECIDED

---

## Context

Multiple agents in the Airflow skill use questionnaires to gather requirements and make decisions. This document establishes the standard approach for all questionnaire interactions.

---

## Core Principles

### 1. Always Include Open-Ended Override

Every question set must include an escape hatch for custom input.

**Pattern:**
```
"How should this DAG be scheduled?"

1. Daily at midnight (0 0 * * *)
2. Every 6 hours (0 */6 * * *)
3. Manual trigger only (no schedule)
4. **Other** - describe your needs

Which option, or describe something different?
```

**Never** present only closed options. Users may have requirements not captured by predefined choices.

---

### 2. Sequential Questions (No Pre-Generation)

Ask one question at a time. Wait for response before asking the next.

**Why:**
- Earlier answers often affect which questions are relevant
- Avoids overwhelming the user
- Prevents asking irrelevant questions based on assumptions

**Bad (pre-generated forking):**
```
Q1: Standalone or Django integration?
Q2a (if standalone): What tables do you need?
Q2b (if Django): Which apps have the models?
Q3a1 (if standalone, multiple tables): ...
Q3b2 (if Django, single app): ...
```

**Good (sequential):**
```
Agent: "Are you working standalone or integrating with Django?"
User: "Django integration"
Agent: "Got it. Which Django apps have the models you need?"
User: "candidates and jobs"
Agent: "Should I convert both apps, or just specific models?"
```

---

### 3. Allow Breaking Out Mid-Questionnaire

User can exit or change direction at any point.

**Pattern:**
```
Agent: "What's your scheduling requirement?"
User: "Actually, let me back up - I'm not sure this is the right approach"
Agent: "No problem. What are you thinking? Happy to discuss alternatives."
```

**Recognition triggers:**
- "Wait", "hold on", "actually"
- "Let me think", "I'm not sure"
- "Can we discuss", "what about"
- Any indication of uncertainty or direction change

**Response:** Pause questionnaire, engage conversationally, resume only when user is ready.

---

### 4. Summarize Before Proceeding

After completing a questionnaire section, summarize decisions before moving on.

**Pattern:**
```
Agent: "Before I generate the DAG, let me confirm:

- **Schedule:** Daily at 2 AM
- **Retries:** 3 attempts, 5 minute delay
- **Notifications:** Email on failure to data-team@company.com
- **Data models:** SQLAlchemy (standalone)

Does this match your intent? Anything to adjust?"
```

---

### 5. Explain Options When Needed

Don't assume user knows all concepts. Briefly explain options.

**Pattern:**
```
"How should sensors wait for conditions?

1. **Poke mode** - Holds a worker slot continuously (good for <60 sec waits)
2. **Reschedule mode** - Releases slot between checks (good for 1-10 min waits)
3. **Deferrable mode** - Uses triggerer process (best for long waits, saves resources)

Which approach fits your use case?"
```

---

### 6. Present Options, Not Recommendations

Let user decide. Don't push toward a particular choice.

**Bad:**
```
"You should definitely use TaskFlow API because it's the modern approach."
```

**Good:**
```
"Two main approaches:

1. **TaskFlow API** - Cleaner code, automatic XCom, good for Python logic
2. **Traditional operators** - More control, better for specialized operators

What's the nature of your tasks?"
```

---

## Questionnaire Sections by Agent

### Workflow Converter

**Section 1: Source Analysis**
- What's the source workflow? (script/cron/manual/Celery Beat)
- Where is it located? (file path or description)

**Section 2: Scheduling**
- How should DAG be scheduled?
- Options: cron, interval, manual, data-driven
- Always include "Other"

**Section 3: Error Handling**
- What should happen on failure?
- Options: retry, skip, fail DAG, different per task

**Section 4: Notifications**
- Who should be notified?
- Options: email, Slack, none
- On what events? (failure, success, retry)

**Section 5: Confirmation**
- Summarize all decisions
- Ask for adjustments

---

### DAG Builder

**Section 1: Codebase Discovery**
- Starting from scratch or existing codebase?
- If existing: What's the stack, or should I explore?
- Explore comprehensively or focus on specific paths?

**Section 2: Data Models**
- Does this DAG need database access?
- If yes: Standalone SQLAlchemy, Django converter, or Django ORM direct?

**Section 3: Task Structure**
- TaskFlow API or traditional operators?
- Parallel execution where possible?

---

### SQLAlchemy Model Builder

**Section 1: Context**
- New table or matching existing schema?
- What's the table for?

**Section 2: Structure**
- Proposed table name and columns
- Wait for approval before generating

---

### DAG Visualizer

**Section 1: Format**
- Which output format?
- Options: Mermaid, ASCII, Graphviz, Skeleton DAG
- Can generate multiple if requested

---

## User Decision Points (from PR Review Skill Pattern)

When presenting decisions, follow this pattern:

```markdown
"I found [finding description].

Here's what I see:
[detailed explanation]

Options:
1. [Option A] - [what it means]
2. [Option B] - [what it means]
3. [Option C] - [what it means]
4. **Other** - tell me what you're thinking

What would you like to do?"
```

**Then WAIT for response.** Never proceed until user responds.

---

## Recognition Patterns

### User Wants to Proceed
- Direct answer to question
- "Go ahead", "proceed", "yes"
- Selecting an option number

### User Wants More Info
- "What's the difference between..."
- "Can you explain..."
- "I'm not sure what X means"

### User Wants to Change Direction
- "Wait", "hold on", "actually"
- "Let me think about this"
- "Can we step back"
- Questions about alternatives

### User Is Done
- "That's all I need"
- "Good for now"
- Direct request to generate/proceed

---

## Summary

| Principle | Implementation |
|-----------|----------------|
| Open-ended override | Always include "Other" option |
| Sequential | One question at a time, wait for response |
| Breakout | Recognize uncertainty, pause, engage |
| Summarize | Confirm decisions before major steps |
| Explain | Brief context for technical options |
| Options not recommendations | Present choices, let user decide |
