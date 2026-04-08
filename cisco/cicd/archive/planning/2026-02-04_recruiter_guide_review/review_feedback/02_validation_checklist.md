# Recruiter Guide Validation Checklist

**Purpose:** Run through this checklist for EVERY recruiter guide before presenting it for review. If any item fails, fix it before proceeding.

**Usage:** Copy this checklist into your working notes and check off each item. Do not skip any section.

---

## Section 1: Document Structure

### Header and Introduction
- [ ] Document title clearly states the role name
- [ ] Subtitle includes: Location | Client-facing status | Focus area
- [ ] Teams transcription request appears at top in a note box
- [ ] Note box is friendly, not demanding ("Not required, but appreciated")

### Layout and Sections
- [ ] Two-column grid layout used throughout
- [ ] Top row: Must-Have Skills | Nice-to-Have Background
- [ ] Second row: Strong Signals | Warning Signs
- [ ] Full-width section: Screening Questions
- [ ] Full-width section: LinkedIn Search Strings
- [ ] Two-column section: Synonym Groups | Tech Stack Keywords
- [ ] Full-width section: What to Look for in Work History

### Formatting
- [ ] No emojis anywhere in the document (no checkmarks, X marks, or other symbols)
- [ ] Consistent heading hierarchy
- [ ] Print-friendly (fits 8.5" x 11" pages)
- [ ] Purple accent color from BayOne brand palette

---

## Section 2: Must-Have Skills

### Content Requirements
- [ ] Years of experience stated explicitly (e.g., "5+ years software engineering, 3+ years AI/ML")
- [ ] Each skill has a plain-language explanation underneath
- [ ] Explanations use no jargon, or jargon is explained in parentheses
- [ ] Skills align with the actual job description requirements

### AI Pair Programming (CRITICAL)
- [ ] "AI pair programming proficiency" is listed as a must-have
- [ ] Description explicitly distinguishes agentic tools from autocomplete
- [ ] Mentions Claude Code and Cursor by name
- [ ] States that Copilot alone is NOT sufficient
- [ ] Example wording: "Actively uses Claude Code, Cursor, or similar agentic AI tools daily. Not just autocomplete (Copilot) - should be comfortable with AI that writes and edits code autonomously"

### Plain Language Test
- [ ] Read each skill description aloud
- [ ] Ask: "Would a recruiter with zero tech background understand this?"
- [ ] If no, rewrite it

---

## Section 3: Nice-to-Have Background

### Content Requirements
- [ ] Clearly distinguished from Must-Haves (these are bonus, not requirements)
- [ ] Each item has a plain-language explanation
- [ ] Includes role-relevant technologies from the Cisco project context where applicable:
  - Airflow (workflow orchestration)
  - Jenkins (CI/CD)
  - Grafana (dashboards)
  - Bazel (build systems)
- [ ] No arbitrary company names or VC jargon

---

## Section 4: Strong Signals

### Content Requirements
- [ ] Each signal is observable by a non-technical recruiter
- [ ] Signals relate to either:
  - Work history patterns
  - Communication style
  - Enthusiasm indicators
  - Depth of experience markers
- [ ] "Enthusiastic about AI tools - can describe specific ways Claude Code or Cursor changed their workflow" is included
- [ ] No signals that require technical evaluation to assess

---

## Section 5: Warning Signs

### Content Requirements
- [ ] Each warning sign is observable by a non-technical recruiter
- [ ] "Doesn't use AI coding tools, or only uses basic autocomplete (Copilot alone)" is included
- [ ] "Vague about what they personally built vs. what their team built" is included
- [ ] Warning signs are behaviors or patterns, not technical deficiencies
- [ ] Plain language throughout

---

## Section 6: Screening Questions

### Structure Requirements
- [ ] Minimum 5 questions included
- [ ] Each question is a complete sentence ending in a question mark
- [ ] Questions are "canary style" - the shape of the answer reveals depth, not specific technical content

### Weak/Good Indicators (CRITICAL)
- [ ] Every single question has a WEAK ANSWER indicator
- [ ] Every single question has a GOOD ANSWER indicator
- [ ] Weak/Good indicators are 2-4 sentences each
- [ ] Indicators describe observable patterns, not technical correctness
- [ ] A recruiter can evaluate the answer without understanding the technology

### Required Questions
- [ ] At least one question about AI coding tools with weak/good indicators
- [ ] At least one question the recruiter can directly evaluate (e.g., "Explain [X] to me like I'm not technical")
- [ ] At least one behavioral/story question (e.g., "Tell me about a time...")

### Example of Properly Formatted Question

```
"Describe an Airflow DAG you built. What did it do and why did you choose Airflow?"

WEAK ANSWER:
Can't describe a specific DAG. Gives vague answers like "it ran some jobs."
Doesn't know why Airflow was chosen over other options.

GOOD ANSWER:
Describes a specific workflow with details - what tasks ran, in what order,
what happened if something failed. Can explain why Airflow made sense for
that particular use case.
```

---

## Section 7: LinkedIn Search Strings

### Tiered Structure (CRITICAL)
- [ ] Layer 1 exists - labeled "Narrow" or "Start Here"
- [ ] Layer 2 exists - labeled "Broader Titles" or similar
- [ ] Layer 3 exists - labeled "Widest Net" or similar
- [ ] Clear instruction: "Start with Layer 1. If fewer than 20 results, try Layer 2..."

### Filter Add-ons
- [ ] Communication Filter exists (to add to any layer)
- [ ] AI Tools Filter exists (to add to any layer)
- [ ] Filters are clearly labeled as "Add to Any Layer"

### Search String Quality
- [ ] Multi-word phrases are in quotes (e.g., "AI engineer" not AI engineer)
- [ ] Boolean operators are uppercase (AND, OR, NOT)
- [ ] Parentheses group related terms correctly
- [ ] Negative modifiers included where appropriate (-recruiter, -sales, -manager)
- [ ] No hobbyist frameworks (AutoGPT, CrewAI, BabyAGI)
- [ ] AI Tools Filter includes: "Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI"

### Validation Test (CRITICAL)
- [ ] Copy Layer 1 search into LinkedIn Recruiter
- [ ] Verify results are relevant (not customer service agents, not recruiters, not sales)
- [ ] Verify result count is reasonable (not 0, not 50,000)
- [ ] If results are bad, fix the search string

---

## Section 8: Synonym Groups

### Content Requirements
- [ ] Groups are clearly labeled
- [ ] Each group explains WHY these terms are synonyms or related
- [ ] Include at minimum:
  - LLM Providers: (Claude OR Anthropic), (OpenAI OR GPT OR "GPT-4" OR ChatGPT)
  - Vector Databases: (pgvector OR Pinecone OR Qdrant OR Weaviate OR Milvus)
  - AI Coding Tools: ("Claude Code" OR Cursor OR "AI pair programming" OR "agentic AI")
- [ ] Role-specific synonyms included (e.g., orchestration tools for automation roles)

---

## Section 9: Tech Stack Keywords

### Structure
- [ ] Split into two tiers: Must-Have (Search for These) | Nice-to-Have (Bonus Points)
- [ ] Displayed as tags or chips for easy scanning

### Content
- [ ] Must-Have keywords align with Must-Have Skills section
- [ ] Nice-to-Have keywords align with Nice-to-Have Background section
- [ ] Claude Code and Cursor appear in Must-Have keywords
- [ ] Role-relevant Cisco technologies appear in Nice-to-Have where applicable

---

## Section 10: What to Look for in Work History

### Content Requirements
- [ ] NO arbitrary company names (no "Google", "Meta", "Anthropic")
- [ ] NO VC jargon (no "Series A-C", "pre-seed")
- [ ] Each item is actionable guidance a recruiter can use
- [ ] Each item has a brief explanation of WHY it matters

### Required Items
- [ ] Company size guidance (e.g., "100+ employees preferred")
- [ ] Type of work guidance (e.g., "Built X, not just used X")
- [ ] Team/collaboration guidance
- [ ] Role-specific context

### Example of Properly Formatted Item

```
**Company size 100+ employees preferred**
Large enough to have real production systems and team collaboration,
not just solo side projects
```

---

## Section 11: Final Review

### Complete Read-Through
- [ ] Read the entire document from top to bottom
- [ ] Read it as if you are a non-technical recruiter
- [ ] Flag any word or phrase that requires tech context to understand
- [ ] Either explain flagged items in parentheses or remove them

### Consistency Check
- [ ] All four recruiter guides follow the same structure
- [ ] Terminology is consistent across guides
- [ ] Formatting is consistent across guides

### Alignment Check
- [ ] Compare guide to the corresponding job description
- [ ] Verify Must-Have Skills match JD Required Qualifications
- [ ] Verify Nice-to-Have Background matches JD Preferred Qualifications
- [ ] Verify years of experience match JD requirements

---

## Checklist Complete

Only present the guide for review after ALL items above are checked. If any item cannot be checked, fix the issue first.
