# Critical Feedback on Recruiter Guides

**Reviewer:** Separate Claude session conducting quality review
**Date:** 2026-02-04
**Status:** Issues identified - review before continuing

---

## Summary

The work on recruiter guides has made progress but still has significant problems. Two guides were updated (Senior AI Solutions Engineer, Automation Engineer) but required multiple rounds of correction. Two guides (AI Engineer, Agentic AI Engineer) are pending and will need the same treatment.

This document details every issue found. Read it completely before making any changes.

---

## Current State

Two guides have been updated:
- `recruiter_guide_senior_ai_solutions_engineer.html` = 613 lines (updated)
- `recruiter_guide_automation_engineer.html` = 592 lines (updated)

Two guides are pending (not yet started per the one-at-a-time approach):
- `recruiter_guide_ai_engineer.html` = 181 lines (original state)
- `recruiter_guide_agentic_ai_engineer.html` = 192 lines (original state)

The pending guides still have their original problems:
- Emojis (checkmarks and X marks)
- No Teams transcription request
- No weak/good answer indicators on questions
- Flat search strings with no tiering
- AI pair programming buried in "strong signals" instead of must-haves
- "Target Backgrounds" with useless jargon tags

When you get to these guides, apply everything learned from the first two. Do not repeat the same mistakes.

---

## SEARCH STRINGS ARE UNUSABLE

### Agentic AI Engineer Current Search String

```
("agentic" OR "autonomous" OR "AI agent") AND ("LangGraph" OR "AutoGPT" OR "CrewAI" OR "function calling") AND Python
```

**Problems:**

1. **"AI agent" returns wrong results** - This phrase matches customer service agents, insurance agents, and real estate agents on LinkedIn. Noise.

2. **AutoGPT and BabyAGI are experimental projects** - These were viral experiments, not production-ready frameworks. Searching for them surfaces hobbyists, not production engineers. (Note: CrewAI and LangGraph are legitimate multi-agent frameworks and appropriate to include.)

3. **Missing CI/CD context** - This role builds SELF-HEALING SYSTEMS FOR JENKINS AND AIRFLOW. The search string would never surface someone who does that. Where is Jenkins? Where is Airflow? Where is "CI/CD" or "pipeline"?

4. **Demo builders vs production engineers** - Someone who made a CrewAI demo is not qualified for this role. Someone who built autonomous retry logic for Jenkins pipeline failures IS qualified. Framework-specific searches can surface relevant candidates, but recruiters need to verify production experience during screening.

### AI Engineer Current Search String

```
("chat interface" OR "chatbot" OR "conversational AI") AND ("LangChain" OR "OpenAI" OR "GPT") AND ("FastAPI" OR "Django" OR "Flask")
```

**Problems:**

1. **"chatbot" returns customer support bot builders** - Wrong talent pool. We need AI engineers who build intelligent interfaces, not people who configure Intercom or Drift.

2. **No tiering** - Where is Layer 1 (narrow), Layer 2 (broader), Layer 3 (widest net)? A recruiter needs options when the narrow search returns too few results.

3. **No AI pair programming filter** - This is a MUST-HAVE requirement that you keep forgetting. There should be a filter to add.

4. **No negative modifiers** - Should exclude `-recruiter -sales -"customer support"` to reduce noise.

---

## AI PAIR PROGRAMMING IS A MUST-HAVE, NOT A SIGNAL

Every single job description contains this exact text:

> "Proficiency with AI pair programming tools (Claude Code, Cursor, GitHub Copilot, or similar) is expected"

Yet in both untouched guides, you have this under "Strong Signals":

> "Uses AI coding tools daily (Claude Code, Cursor, Copilot)"

This is WRONG on two levels:

1. **It belongs in Must-Have Skills, not Strong Signals** - The JD says "expected," which means required.

2. **You're treating Copilot as equivalent to Claude Code/Cursor** - They are fundamentally different:

| Tool | Type | What It Does |
|------|------|--------------|
| GitHub Copilot | Autocomplete | Suggests the next line of code as you type |
| Claude Code | Agentic AI | Writes and edits entire files autonomously, runs commands, makes decisions |
| Cursor | Agentic AI | Same as above - autonomous code writing and editing |

Someone who only uses Copilot does NOT meet the bar for these roles. We need people comfortable with AI that takes autonomous action, not just autocomplete.

**Correct phrasing for Must-Have Skills:**

> **AI pair programming proficiency** - Actively uses Claude Code, Cursor, or similar agentic AI tools daily. Not just autocomplete (Copilot) - should be comfortable with AI that writes and edits code autonomously.

---

## TARGET BACKGROUNDS/COMPANIES ARE USELESS JARGON

### What You Wrote (Agentic AI Engineer)

```
Target Backgrounds:
- AI agent startups (Adept, Cognition)
- SRE teams at big tech
- Incident management (PagerDuty, Opsgenie)
- Workflow automation (Zapier, n8n, Temporal)
- AIOps platforms
- Robotics/control systems (transferable)
```

### Problems

1. **Adept and Cognition employees aren't looking at BayOne roles** - These are hot AI startups paying top dollar. Listing them as targets is fantasy.

2. **"AIOps platforms"** - Which ones? This means nothing actionable to a recruiter. Name them or don't mention them.

3. **"Robotics/control systems (transferable)"** - What? How does a robotics engineer transfer to CI/CD self-healing? This is a bizarre stretch that will confuse recruiters and waste their time.

4. **A non-technical recruiter cannot action any of this** - What is a recruiter supposed to DO with "SRE teams at big tech"? Search for "SRE Google"? This isn't guidance, it's vague hand-waving.

### What You Should Write Instead

```
What to Look for in Work History:

- **Company size 100+ employees** - Smaller companies don't have complex
  enough systems to need self-healing automation

- **Built autonomous systems that took real actions** - Not just analysis
  or recommendations, but systems that actually did things automatically

- **Production environment experience** - SRE, platform engineering,
  infrastructure, or DevOps teams where failures have real consequences

- **CI/CD or pipeline experience** - This role specifically automates
  pipeline failures, so prior CI/CD exposure is valuable
```

Plain language. Actionable. No jargon.

---

## QUESTIONS HAVE NO WEAK/GOOD INDICATORS

### Current Format (AI Engineer Guide)

```
Questions to Ask:
- "Describe an AI-powered feature you built that went to production."
- "How do you test AI features when outputs aren't deterministic?"
- "Have you built any chat interfaces? Walk me through the architecture."
- "What AI coding tools do you use and how do they fit into your workflow?"
```

A recruiter asks these questions. The candidate responds. How does the recruiter know if the answer is good or bad?

**They don't.** You gave them nothing to evaluate against.

### Required Format

```
"Describe an AI-powered feature you built that went to production."

WEAK ANSWER:
Vague description without specifics. Can't name the technologies used.
Describes a demo, prototype, or hackathon project rather than something
users relied on. Says "the team built it" without clarifying their
personal contribution.

GOOD ANSWER:
Specific feature with concrete details - what problem it solved, what
technologies they used, how many users or what scale. Clear ownership
of what THEY personally built versus what the broader team did. Can
explain why they made certain technical choices.
```

The recruiter doesn't need to understand the technology. They need to recognize the SHAPE of a good versus bad answer:
- Vague vs specific
- Team vs individual contribution
- Demo vs production
- Buzzwords vs reasoning

---

## MISSING PROJECT CONTEXT

This engagement is for Cisco's NX-OS CI/CD pipeline. The technology stack includes:

| Technology | What It Is | Relevance |
|------------|------------|-----------|
| Apache Airflow | Workflow orchestration | Core - schedules and runs pipeline tasks |
| Jenkins | CI/CD automation | Core - runs builds and tests |
| Bazel | Build system | Used for large codebase builds |
| pgvector | Vector database | PostgreSQL extension for embeddings |
| Grafana | Dashboards | Monitoring and visualization |
| pyATS | Test automation | Cisco's test framework |
| CAT | Commit Approval Tool | Internal Cisco gate management |
| DevX | Developer platform | Internal Cisco tooling |

Your recruiter guides barely mention any of this. A candidate who knows Airflow and Jenkins is MORE relevant than one who only knows generic LangChain patterns. This context should appear in:

- Nice-to-Have Background (familiarity with CI/CD tooling)
- Tech Stack Keywords (Airflow, Jenkins as bonus points)
- What to Look for in Work History (CI/CD or DevOps experience)

---

## IMMEDIATE ACTIONS REQUIRED

### Step 1: Perfect the First Two Guides

Focus on perfecting Senior AI Solutions Engineer and Automation Engineer first. They will be reviewed line by line before proceeding.

For both guides, verify:

- [ ] AI pair programming is in MUST-HAVES with the Copilot vs Claude Code/Cursor distinction
- [ ] Search strings are properly tiered (Layer 1/2/3)
- [ ] Search strings have been tested in LinkedIn and return relevant results
- [ ] All screening questions have weak/good answer indicators
- [ ] No arbitrary company lists remain (replaced with "What to Look for in Work History")
- [ ] No jargon without plain-language explanation
- [ ] Emojis removed entirely

### Step 2: Show Corrected Guides for Review

Present the corrected Senior AI Solutions Engineer and Automation Engineer guides. Do not proceed to the other two guides until these are approved.

### Step 3: Then Update Remaining Guides

When approved, apply everything learned to AI Engineer and Agentic AI Engineer. Use the validation checklist (see `02_validation_checklist.md`) before presenting them. Do not repeat the mistakes that required correction in the first two guides.

---

## Final Note

The pattern observed in this work: each critique is treated as an isolated fix rather than a systematic learning. When the AI pair programming issue was corrected on Automation Engineer, it should have immediately been checked and fixed on Senior AI Solutions Engineer. It wasn't - it required being told again.

When updating the remaining guides, apply ALL learnings from the first two simultaneously. Do not create new problems that were already solved.
