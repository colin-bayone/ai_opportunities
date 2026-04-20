# Singularity Skill Improvements Tracker

**Session:** 2026-04-10 (started), updated 2026-04-13
**Purpose:** Running list of all improvements, extensions, and new capabilities identified during this session that need to be integrated into the singularity skill. The goal: the singularity skill must be able to produce work at the same quality as what we just did for the Srinivas deck, on command, without substantial problems.

---

## Section A: Completed This Session (Skill Updated)

| # | Improvement | Status | Where |
|---|-----------|--------|-------|
| 1 | Flow 7: Present (presentation generation) added to SKILL.md | Done | SKILL.md invocation menu + flow section |
| 2 | Presentation design language spec created | Done | `references/presentation_design_language.md` |
| 3 | 7 example slide HTML files created | Done | `assets/slide_examples/` |
| 4 | Stop hook extended for presentation design reference verification | Done | `scripts/singularity_stop.py` |
| 5 | Sibling skills table updated (removed "Slide skill TBD") | Done | SKILL.md |
| 6 | Embedded diagram + full-screen viewer pattern added to design language spec | Done | `references/presentation_design_language.md` |
| 7 | Back button on full-screen chart pages | Done | `references/presentation_design_language.md` |

## Section B: Working Implementations Exist (Not Yet Codified in Skill)

These exist as real working files in the repo but the patterns are not documented in skill references yet. They serve as worked examples to extract from.

| # | Working Example | Current Location | Needs Codification In |
|---|----------------|------------------|----------------------|
| 8 | Full working Srinivas presentation (8 slides + chart) | `cisco/cicd/presentations/srinivas_status_2026-04-10/` | Gold standard in `assets/design/gold_standards/presentations/` |
| 9 | Team sub-singularity first instance | `cisco/cicd/team/` | Worked example in `references/worked_example_team/` |
| 10 | Mermaid ecosystem diagram | `cisco/cicd/presentations/srinivas_status_2026-04-10/charts/build_log_ecosystem.html` | Gold standard chart pattern |

## Section C: Pending Integration into SKILL.md / References

| # | Improvement | Description | Priority |
|---|-----------|-------------|----------|
| 11 | Nested singularity (sub-singularity) pattern | Full methodology in SKILL.md. Design doc at `claude/2026-04-10_singularity_nested_design/00_exploration_and_design.md`. Needs: new SKILL.md section, new reference file `references/nested_singularity.md`. | High |
| 12 | Team meeting processing methodology | Different standard passes than client meetings: people, action items, blockers, decisions, technical discussion, summary. Different from `document_processing.md` defaults. Needs: new reference file `references/team_meeting_processing.md` or section within nested_singularity.md. | High |
| 13 | Tracking folder as a concept | Living operational documents (action_items.md, blockers.md, decisions.md) updated after each meeting. Dual model: blockchain research + living tracking. | High |
| 14 | Cross-reference file pattern | Maps sub-singularity sets to parent sets and sibling sub-singularities. | Medium |
| 15 | Mermaid diagram as its own slide | When a diagram is too large for inline embed, give it a dedicated slide. Needs one sentence in design language spec plus a second chart-slide example. | Medium |
| 16 | `documents/` folder in sub-singularity | For HTML reports within sub-singularities. Must add to folder_structure reference. | Medium |
| 17 | `client/` folder concept | Colin mentioned `cisco/cicd/client` for client-facing presentations. Need clarification: is this a sub-singularity, an alias for presentations/, or something else? | Low |

## Section D: Lessons Learned From Srinivas Deck (Rules to Codify)

These are behavioral rules that emerged from feedback during slide generation. Each must be encoded explicitly in the design language spec or the Flow 7 instructions so the skill reproduces this quality on the first pass.

| # | Rule | Feedback Source | Where to Codify |
|---|------|----------------|-----------------|
| 18 | Bullet formatting (.items/.item) is the DEFAULT for all card bodies, not paragraphs | "The bullet formatting thing is needed on all of them, actually" | design language spec + Flow 7 rules |
| 19 | Navigation (prev/next/home) is MANDATORY on every slide in a multi-slide deck | "I think you're missing the JavaScript buttons from the slides" | design language spec + Flow 7 rules |
| 20 | Content must use SPECIFIC details from source material, not vague corporate language | "You didn't even talk about the items as you said. Overall, this is just okay" | Flow 7 rules |
| 21 | When a section (like access status) has substantive content, give it its own slide | "You did not cover the access still needed section well. That should be on its own page" | Flow 7 rules |
| 22 | Error on more slides rather than dense slides | "I thought you were doing seven... if you need to expand slides into multiple, that's fine by me" | Flow 7 rules |
| 23 | Slide deck proposal must be presented and approved BEFORE generation | "Does that look right before I generate?" workflow worked well | Flow 7 process (already partial) |
| 24 | No individual names in content; only on title/closing slide presenter credit | Was followed; needs to be explicit | design language spec rules |
| 25 | No direct quotes from any person | "Remember to not put quotes from people in any of the slides" | design language spec rules |
| 26 | Diplomatic framing: problems presented as "alignment needed," not as conflicts | "be very diplomatic with phrasing here" | Flow 7 rules |
| 27 | Architectural ideas framed as preliminary, not finalized plans | "we should not be too forthcoming with ideas and brainstorming just yet" | Flow 7 rules |
| 28 | Large diagrams go on their own slide, not crammed into content slides | "Now the other content is not having enough room on the page" | design language spec |
| 29 | After every substantive change, maintain a running improvements tracker in session folder | "I haven't seen you do any note-taking or edits" | Process rule (meta) |

## Section E: Gold Standard Strategy

The Srinivas deck is the first example of the new presentation design language actually working in a real engagement. Per Colin's direction, it should become a gold standard.

**Proposal:**
- Copy the final 8 slides + chart to `.claude/skills/singularity/assets/design/gold_standards/presentations/srinivas_status/`
- This complements the existing gold standards for problem_restatement.html, information_request.html, preliminary_approach.html, poc_proposal_v5.html
- The Flow 7 instructions should explicitly reference this gold standard like the deliverable flow references the problem_restatement gold standard
- Similarly, the team sub-singularity in `cisco/cicd/team/` should be copied as `.claude/skills/singularity/references/worked_example_team/` matching the pattern of `references/worked_example/` (Lam Research)

---

## Process Note

The original process rule that should have been followed from the start: after every substantive change or new pattern identified, update this tracker. This was not being done until feedback was given. Going forward, every new pattern or rule gets added here immediately so the final consolidation into the skill is mechanical, not reconstructive.
