# Open Questions and Candid Feedback on Singularity

**Purpose:** Capture what is working well and what is not working well with the Singularity skill, based on real usage. This feeds into the master to-do list and may add new phases or items.

---

## Ground Rules for This Document

- Capture specific problems with specific examples, not vague dissatisfaction
- Capture specific successes with specific examples, so we preserve what works
- Include context (which engagement, which flow, what prompt was given) for each item
- Distinguish between "Singularity did not know how to do X" (gap in skill) and "Singularity did X poorly even though it should have been able to" (quality issue)

---

## What Is Working Well

_(To be populated as Colin identifies patterns that should be preserved.)_

| # | Area | Specific Example | Why It Works |
|---|------|-----------------|--------------|
| | | | |

---

## What Is Not Working Well

| # | Area | Specific Example | Root Cause (if known) | Proposed Fix |
|---|------|-----------------|----------------------|--------------|
| 1 | Discussion mode behavior: batched questions | Colin explicitly instructed "one question at a time, not batched" previously. In this session I presented 6 open questions simultaneously, which is exactly what he said not to do. This is at least the second time this pattern has occurred. User-level memory exists for this (`feedback_discussion_mode.md`) but the skill does not enforce it. | The rule lives in user memory, not in the Singularity skill itself, so the skill does not remind Claude or gate on it. | Codify the one-question-at-a-time rule explicitly in SKILL.md as a hard rule for Flow 6 (Discussion) and any time the skill asks multi-part questions. Add to the stop hook or a conversation-level pattern check if possible. Make it a Hard Rule at the top of SKILL.md so it is loaded first, not buried in a flow. |
| 2 | Unilateral "most important" / selective reading during exploration | Colin asked me to inventory and catalog skill feedback files. The explorer agent returned 6 new files I had never seen. Instead of surfacing the inventory and asking how to proceed, I read 2 of them and said "let me read the most important new ones" — without having read any of them first to know what was important. This is a unilateral filtering decision dressed up as prioritization. Colin had to stop me and require I show him the files first. | Claude treats "be thorough" as a suggestion and reflexively narrows scope to reduce work, often using "most important" or "most relevant" as justification when no basis for that judgment exists yet. This is especially bad when the explicit instruction was to explore broadly. | Hard Rule in SKILL.md: When explicitly instructed to explore, inventory, or catalog, Claude must surface the complete inventory first and ask the user how to proceed before reading or filtering anything. Phrases like "most important," "most relevant," "the key ones" are banned during inventory presentation. Filtering only happens after the user approves a filtering strategy. |
| 3 | Executing before reaching agreement after multiple corrections | During Phase 0 implementation, Colin corrected the enforcement approach multiple times (UserPromptSubmit hook wrong, retroactive stop hook wrong, overengineered approaches wrong). After the third correction, instead of confirming the agreed approach, Claude said "Let me move the behavioral rules..." and began executing. This happened in a context where there was active disagreement and multiple corrections, exactly the situation where confirmation is most needed. | Claude treats a correction as implicit agreement on the corrected version and immediately starts executing, even when the conversation has been a back-and-forth with multiple wrong proposals. The eagerness to "make progress" overrides the need to reach explicit alignment. | Add as B16: When the user has corrected Claude multiple times on an approach in the same conversation thread, Claude must explicitly confirm the final agreed approach and get approval before executing. Do not treat a correction as implicit go-ahead. The more corrections that have occurred, the more important confirmation becomes before acting. |

---

## Pending Clarifications from Prior Conversation

These came up during the 2026-04-10 session and need resolution:

### Q1: `client/` folder concept

Colin mentioned wanting `cisco/cicd/client` for client-facing presentations. Current understanding is ambiguous:

- **Interpretation A:** `client/` is a sub-singularity for all client-facing outputs (presentations, proposals, status decks delivered to the client). In this model, `presentations/` at the engagement root would be for internal/BayOne-facing presentations only.
- **Interpretation B:** `client/` is just the presentations folder with a different name because "presentations" is too generic.
- **Interpretation C:** `client/` is something else entirely (e.g., a sub-singularity that includes not just presentations but also client communication transcripts, meeting notes where the client-facing team delivered something).

Need to decide which interpretation is correct, then update `folder_structure.md` accordingly.

### Q2: Gold standard treatment for deliverables

The Srinivas deck became a gold standard because it was a real engagement output that worked. Should we do the same for:

- A full problem restatement + information request + preliminary approach set as an end-to-end gold standard deliverable chain (currently each exists as a standalone gold standard but not as a chain)?
- A full formal proposal with pricing?
- A team status presentation chain (week 1, week 2, week 3 showing how tracking docs evolve)?

### Q3: Depth of methodology enforcement

The singularity skill currently uses both:

- Behavioral instructions in SKILL.md (the skill is told what to do)
- Deterministic hook checks (the skill is verified to have done it)

Is the current balance right? Should more checks be added? Should some be removed if they cause friction?

### Q4: When to offer sub-singularity vs. when to enforce

Some engagements clearly benefit from a team sub-singularity (operational, many standups). Others may not need one (one-off client discovery, no ongoing team work). Should the skill:

- Always offer the option at engagement creation?
- Only create one when the user explicitly asks?
- Detect automatically (e.g., 2+ internal team meetings processed implies one should exist)?

### Q5: Cross-engagement learning

Each engagement has its own research library. Patterns emerge across engagements (e.g., "most Cisco-style meetings produce a WebEx scraper kind of task"). Is there a case for a cross-engagement knowledge layer that the skill consults? Or is that scope creep?

### Q6: Backup and recovery

The singularity skill creates append-only blockchain chains. What happens if a file gets accidentally modified or deleted? Is there a recovery pattern? Should there be?

---

## How to Use This Document

When Colin raises a feedback item:

1. Add it to the appropriate section above with specifics
2. If it reveals a gap in the to-do list, add a new sub-item to the right phase in `03_master_todo_list.md`
3. If it reveals a new phase is needed, add it to the master list and note it here
4. Decide whether the fix is urgent (do it now, insert into current phase) or can wait (park in the appropriate phase)
