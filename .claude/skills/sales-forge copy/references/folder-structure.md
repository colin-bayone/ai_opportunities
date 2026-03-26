# Engagement Folder Structure

Standard folder structure for sales engagement documentation.

## Directory Layout

```
{client-name}/
├── 00_index.md              # Navigation hub with quick links
│
├── context/                 # Source materials (user provides)
│   ├── email1.txt
│   ├── transcript.txt
│   └── additional*/         # Numbered folders for batches
│       └── *.txt
│
├── project/                 # Current state documents
│   ├── 00_project_overview.md    # What, why, scope
│   ├── 01_glossary.md            # Key terms explained
│   ├── 02_pain_points.md         # Problems and opportunities
│   ├── 03_scope_and_scale.md     # Quantified metrics
│   └── 04_engagement_timeline.md # History and milestones
│
├── planning/                # Strategy and approach
│   ├── 00_bayone_positioning.md  # How we position ourselves
│   └── 01_open_questions.md      # Gaps to fill
│
├── stakeholders/            # People and relationships
│   └── 00_people_directory.md    # Names, roles, org chart
│
├── research/                # Investigation materials
│   └── *.md                      # Research findings
│
└── deliverables/            # Final outputs
    ├── 01_proposal.html
    ├── 01_proposal.pdf
    └── slides/                   # For decks
        ├── 01_cover.html
        ├── 02_problem.html
        └── ...
```

## File Naming Conventions

- **Snake case** with two-digit prefixes: `00_initial.md`, `01_next.md`
- **Context folders**: `additional1/`, `additional2/` for batches
- **Deliverables**: Numbered by version or order

## Document Purposes

| Document | Purpose |
|----------|---------|
| `00_index.md` | Navigation hub, key numbers at a glance |
| `00_project_overview.md` | Executive summary of the opportunity |
| `01_glossary.md` | Define unfamiliar terms for anyone reading |
| `02_pain_points.md` | Client's problems + our opportunity analysis |
| `03_scope_and_scale.md` | Quantified metrics (reports, users, timeline) |
| `04_engagement_timeline.md` | Chronological record of interactions |
| `00_bayone_positioning.md` | How we differentiate, approach strategy |
| `01_open_questions.md` | Information gaps, questions to ask |
| `00_people_directory.md` | Stakeholder map with roles and preferences |

## Cross-References

Each document should reference related documents at the bottom:

```markdown
---

## Related Documents

- [Project Overview](../project/00_project_overview.md)
- [Pain Points](../project/02_pain_points.md)
```

## Index Template

```markdown
# {Client Name} - Documentation Index

*Last updated: {date}*

## Quick Links

### Core Understanding
- [Project Overview](project/00_project_overview.md)
- [Key Terms & Glossary](project/01_glossary.md)
- [Scope and Scale](project/03_scope_and_scale.md)

### Problem Analysis
- [Pain Points & Opportunities](project/02_pain_points.md)

### People
- [Stakeholder Directory](stakeholders/00_people_directory.md)

### Strategy
- [BayOne Positioning](planning/00_bayone_positioning.md)
- [Open Questions](planning/01_open_questions.md)

### Timeline
- [Engagement History](project/04_engagement_timeline.md)

## Key Numbers

| Metric | Value |
|--------|-------|
| ... | ... |

## Key People

**{Client}:**
- Name - Role

**BayOne:**
- Colin Moore - Director of AI
```
