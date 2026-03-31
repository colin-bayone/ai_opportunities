# People Tracking System

## Dual System Design

People information is tracked in two places simultaneously. This is intentional and serves different purposes.

### 1. Per-Set People Documents (Blockchain Style)

Located in `/<client_name>/<opportunity_name>/research/`, these capture what was learned about people from a specific source event. They are append-only, like all research documents.

**Example:** `/<client_name>/<opportunity_name>/research/02_meeting_people_2026-03-12.md`

**What they capture:**
- Who was present (or mentioned) in that specific event
- Roles and titles as stated or observed
- Sentiment and behavioral observations from that event
- Relationship dynamics observed in that event
- New people introduced for the first time
- Candid assessments (for internal debriefs)

**Why they exist:** They preserve the historical record of when information was learned. If you want to know "what did we think about Brad after the first meeting vs. after the debrief," you read the Set 02 people doc and then the Set 02a people doc.

### 2. Living Org Chart (Always Current)

Located at `/<client_name>/<opportunity_name>/org_chart.md`, this always reflects the most current and complete understanding of all people across all events.

**What it contains:**
- Every person known to the engagement
- Their most current title, role, and relationship to the engagement
- A "Known Since" field indicating which set introduced them
- Sentiment notes that reflect the cumulative understanding
- A relationship map section at the bottom

**Why it exists:** It is the quick-reference truth. A new session reads the org chart and immediately knows who everyone is, what they do, and how they relate to each other. No need to read through every per-set people doc.

**This is the one exception to append-only.** The org chart IS updated over time because its purpose is to be a current-state reference, not a historical record.

## Org Chart Structure

```markdown
# [Engagement Name] - Org Chart

**Last Updated:** [date] (from document set [number])

---

## [Client Company Name]

### [Person Name] ("[Nickname]")
- **Title:** [Title]
- **Role in Engagement:** [Their role]
- **Ownership:** [What they own, if relevant]
- **Background:** [Career background if known]
- **Sentiment:** [Behavioral observations, communication style, trust signals]
- **Key Quote:** [One defining quote, if available]
- **Working Style:** [How they work, what they expect]
- **Known Since:** Set [number] ([source description])

### [Next Person]
...

---

## [BayOne Solutions / Our Company]

### [Person Name]
- **Title:** [Title]
- **Role in Engagement:** [Their role]
- **Relevant Experience:** [If applicable]
- **Meeting Performance:** [How they performed in the meeting, if applicable]
- **Known Since:** Set [number]

---

## Relationship Map

- **[Key relationship 1]**
- **[Key relationship 2]**
- **[Competitive landscape if known]**
- **[Next engagement point]**
```

## Workflow: Processing People Information

### Before Processing a New Set

1. Read `/<client_name>/<opportunity_name>/org_chart.md` to have full context on all known people.
2. Read the prior set's summary in `/<client_name>/<opportunity_name>/research/` for context on where we left off.

### During Processing

3. Create the per-set people document as the first file for transcript-based sets.
4. Capture everything specific to this event: who was there, what was observed, sentiment in this specific interaction.

### After All Set Files Are Written

5. Update `/<client_name>/<opportunity_name>/org_chart.md` with any new people, updated titles, new relationship information, or changed sentiment based on this set.
6. Update the "Last Updated" line in `/<client_name>/<opportunity_name>/org_chart.md` to reflect the current set.

## What to Capture About People

### For Client-Side People

| Field | What to Include |
|-------|----------------|
| Title | Official title as stated or discovered |
| Role in Engagement | What they do in the context of this initiative |
| Ownership | What they control (budget, decisions, systems, team) |
| Background | Career progression if known |
| Sentiment | Communication style, trust signals, red flags, behavioral patterns |
| Key Quote | One quote that captures their personality or priorities |
| Working Style | How they expect things to work (requirements, engagement model) |
| Relationship to Others | Who they defer to, who defers to them, tensions, alignments |

### For Internal People

| Field | What to Include |
|-------|----------------|
| Title | Official title |
| Role in Engagement | What they do in the context of this initiative |
| Relevant Experience | Why they are on this engagement |
| Meeting Performance | What landed well, what got redirected, strengths and weaknesses observed |
| Relationship to Others | Internal dynamics, who drives what |

### For People Mentioned but Not Met

| Field | What to Include |
|-------|----------------|
| Title | If known |
| Role | Expected role when they join |
| Context | How they were referenced and by whom |
| Significance | Why they matter to the engagement |

## Handling Candid Assessments

Internal debriefs often contain blunt, unfiltered opinions about client team members. These are valuable and should be captured honestly in the per-set people documents and reflected (more diplomatically) in the org chart.

**Rules:**
- Internal debrief people docs should preserve the tone and candor of the assessment
- The org chart should reflect the substance of the assessment without inflammatory language
- Flag any assessment that could be colored by ego friction or frustration (e.g., "Colin's assessment of Mikhail may be partly influenced by being redirected on the call")
- Never let internal candid assessments leak into client-facing deliverables

## Competitors and External Parties

Competitors, prior partners, and other external parties mentioned in meetings should be tracked in the org chart's relationship map section, not as individual entries. They are contextual, not stakeholders.

Example:
```markdown
## Relationship Map

- **Competitive landscape:** Deloitte and Capgemini are long-term embedded incumbents.
  Accenture was the prior partner who attempted the text classification work and failed.
```
