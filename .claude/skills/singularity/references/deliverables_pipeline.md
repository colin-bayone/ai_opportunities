# Deliverables Pipeline

## Overview

Client-facing deliverables are drafted from the research library, not from raw transcripts. The research library is the single source of truth. Deliverables are stored flat in `/<client_name>/<opportunity_name>/deliverables/` with dates in filenames. No nested event subfolders.

## Deliverable Folder Structure

```
/<client_name>/<opportunity_name>/deliverables/
├── problem_restatement_2026-03-20.md       (markdown source)
├── problem_restatement_2026-03-20.html     (formatted client-facing version)
├── information_request_2026-03-20.md
├── information_request_2026-03-20.html
├── preliminary_approach_2026-03-22.md
├── preliminary_approach_2026-03-22.html
└── followup_email_2026-03-22.md
```

All deliverable files include dates in their filenames. There is no README or nested subfolder structure. The flat layout with dated filenames provides a clear timeline of what was delivered and when.

## Creating Deliverables

### Step 1: Identify What to Deliver

Based on the engagement state and user direction. The full catalog of deliverable types singularity can produce:

| Deliverable Type | Gold Standard | When to Use | Key Characteristics |
|---|---|---|---|
| Problem restatement | `.claude/skills/singularity/gold_standards/deliverables/problem_restatement.html` | After discovery, to demonstrate understanding before proposing solutions | Uses client's own framing. No solutions, no technology names, no individual names. Satisfies the "repeat back" requirement. |
| Information request | `.claude/skills/singularity/gold_standards/deliverables/information_request.html` | When specific information is needed from the client to proceed | Prioritized tiers (business team vs. technical team vs. working session). Specific, actionable asks. |
| Preliminary approach | `.claude/skills/singularity/gold_standards/deliverables/preliminary_approach.html` | Initial solution direction, before full scoping | Explicitly framed as preliminary. Reframes the problem from authority. Shows methodology without over-committing. |
| Formal proposal (concise) | `.claude/skills/singularity/gold_standards/deliverables/poc_proposal_v5.html` | Scoped engagement with pricing, timeline, and deliverables | Standard structure: Cover → Challenge → Approach → Capabilities → Engagement → Why BayOne → Next Steps. |
| Formal proposal (detailed) | `.claude/skills/singularity/gold_standards/deliverables/poc_proposal_v5_detailed.html` | Extended version with deeper technical justification | Same structure as concise but with expanded technical sections. Used when the audience is technical. |
| Follow-up email | (markdown only, no HTML) | After meetings, to maintain momentum and request next steps | Professional but warm. Not salesy. References attached documents. Single clear ask. |
| Resource plan | `.claude/skills/singularity/gold_standards/deliverables/resource_plan_for_cisco.html` | Staffing and team structure documents | Team composition, allocation, timeline visualization. |

The skill should reference the appropriate gold standard when creating each deliverable type. Gold standards are style and structure references, not fill-in-the-blanks templates. Deliverables are crafted from the research library, not templated.

### Step 2: Draft in Markdown

Always draft the content in markdown first. This allows the user to review and refine the substance before investing in formatting. The markdown version is the source of truth for content.

### Step 3: Convert to HTML

Use the BayOne design system for client-facing HTML documents:

**Design System Elements:**
- Purple gradient brand palette (#2e1065 to #6d28d9)
- Inter font family (Google Fonts)
- Full-page purple gradient cover with label, title, subtitle (optional), meta items, and BayOne logo
- Numbered sections (01, 02, 03...) using `.section-number` class
- `.lead` class for section intro paragraphs
- `.highlight-box` for callouts (purple gradient background, left border)
- Tables with purple header (#5b21b6), alternating row backgrounds
- `.two-col` grid for side-by-side `.card` components
- `.workflow-grid` for step visualizations
- Footer with BayOne logo
- Print styles for 8.5" x 11"

**Cover Page Meta Items:**
- Prepared For: [Client Name]
- Prepared By: BayOne Solutions
- Date: [Month Year]
- Status is optional (often omitted)

**Print Style Notes:**
- The cover page should have `page-break-after: always` and `height: 10in` so it gets its own page when printed
- Whether to include `page-break-inside: avoid` on content sections depends on the document. Ask the user if they want page breaks managed or content to flow freely.

**Template vs. Crafted:**

The `proposal_template.html` in `.claude/skills/singularity/templates/` is a **structural reference** showing standard section order and CSS patterns. It is NOT a fill-in-the-blanks template with `{{PLACEHOLDER}}` variables. Deliverables are written from the research library using the design spec (`.claude/skills/singularity/references/bayone_design_spec.md`) and gold standards (`.claude/skills/singularity/gold_standards/deliverables/`) as style guides. This produces engagement-specific documents that read naturally, not template-shaped output.

**Company Context:**

When writing deliverables that reference BayOne (cover pages, "Prepared By" metadata, "Why BayOne" sections, team descriptions), read `.claude/skills/singularity/references/bayone_team.md` for the current team directory.

### Step 4: Quality Review

Run the big4 skill (or equivalent quality checks) against the HTML:
- No em dashes anywhere
- No direct quotes or attribution to named individuals
- No contrastive framing ("It's not just X, it's Y")
- No emojis
- No contractions in formal sections
- No individual names
- Professional consulting tone appropriate for the audience
- Content faithful to the markdown source

### Step 5: Iterate with User

Present the draft for review. The user will have style adjustments, title changes, structural feedback, and content refinements. Iterate until approved.

## Client-Facing Content Rules

These rules apply to ALL client-facing deliverables:

### Absolute Rules (Never Violate)

1. **No em dashes.** Use commas, periods, "and," or parentheses instead.
2. **No direct quotes.** Never put quotation marks around something someone said. Paraphrase as organizational knowledge.
3. **No individual names.** Frame everything as "the team," "the organization," "Lam Research," or "BayOne." Never "Brad said" or "Mikhail mentioned."
4. **No contrastive framing.** Never "It's not just X, it's Y" or "This isn't about X, it's about Y." State what something IS directly.
5. **No emojis.** Zero, ever.
6. **No contractions.** "Does not" instead of "doesn't," "we are" instead of "we're."

### Tone Rules

7. **Never suggest the client is incompetent.** Even if the internal assessment is harsh. Frame gaps as opportunities: "prior approaches followed a common pattern that tends to be brittle in this type of environment."
8. **Do not question organizational authority in writing.** If Brad says he owns everything, the document accepts that.
9. **Come from a position of authority without arrogance.** "Based on BayOne's experience building similar solutions" is good. "Our unique and revolutionary approach" is bad.
10. **Call the solution a "solution," never a "product."** It is a custom, tailor-made engagement, not an off-the-shelf product.

### Scope Rules

11. **Stay within the stated problem.** Do not pitch future growth or expansion beyond a brief mention in passing.
12. **Preliminary work should be framed as preliminary.** "These are initial ideas informed by our experience. They require refinement through deeper discovery."
13. **Acknowledge what you do not know.** If specific information is needed before a recommendation can be finalized, say so explicitly.

## Deliverable Types and Their Characteristics

### Problem Restatement

**Purpose:** Demonstrate understanding. Satisfy the "repeat back" requirement.

**Contains:**
- The problem in the client's own framing and terminology
- Business context and why it matters
- Specific details that prove deep listening (exact metrics, specific examples cited in the meeting)
- No solutions, no technology names, no proposals

**Cover label example:** "SECURE KNOWLEDGE ENABLEMENT" (not "PROBLEM RESTATEMENT")

### Information Request

**Purpose:** Formally ask for what is needed to proceed.

**Contains:**
- Prioritized list of information needs
- Who can answer each item (business team vs. technical team)
- Specific, actionable asks (not vague)
- Next steps section as a call to action

**Cover label example:** "DISCOVERY" (not "INFORMATION REQUEST")

### Preliminary Approach

**Purpose:** Present initial thinking on the solution direction.

**Contains:**
- Brief problem summary (reference, not repeat)
- Observations on prior approaches (diplomatic)
- Proposed architecture and methodology
- Enterprise tools strategy
- What is needed to refine into a full proposal

**Framing:** Explicitly preliminary. "These ideas require refinement through deeper discovery."

### Follow-Up Emails

**Purpose:** Keep momentum. Request specific actions.

**Contains:**
- Thanks for the meeting
- Reference to attached documents
- The single most important ask (prioritized)
- Next step (usually: identify target application, then schedule technical session)
- Offer of flexibility on timing

**Tone:** Professional but warm. Not salesy.
