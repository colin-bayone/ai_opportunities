# Answers to File 05 Open Questions + Redirects

Colin's answers given verbatim 2026-04-26 evening, with context preserved. Some questions need to be re-asked in chat with proper context — those are flagged at the bottom.

---

## Block A — Srinivas Monday One-Pager

**A1.** Filename `weekly_status_<date>.md` is fine. (Colin: "stupid granular question.")

**A2.** Same-Friday first cut WAS NOT confirmed and WAS NOT sent. Did not have enough time. **Implication: the Monday version absorbs the same-Friday commitment plus the new week's content, and the spec must acknowledge the slip rather than gloss it.**

**A3.** Resolved items drop off immediately, OR are shown crossed off (strikethrough) if they were resolved between the last meeting and this one. Items that were already traversed in the last meeting do not need to appear at all. **Pattern: only show items that the audience hasn't already seen resolved in a meeting.**

**A4.** Plain markdown text and a simple table or column view as the primary representation. Mermaid is supplemental — a visual additive, not a replacement for the table. Both, not either-or.

**A5.** Drop the decision-prompt section entirely. Adding a "what else do you want?" prompt is redundant — Srinivas can add items in the meeting where the doc is presented; that is implied. Pattern correction: stop adding sections that re-state what's implied by meeting context.

**A6 (scope of "this week").** Apr 27 through May 1 (Mon-Fri). **Critical context Colin surfaced: Srinivas did not receive his weekly status update from the prior week (the same-Friday commitment that was not delivered). Therefore the team probably needs TWO one-pagers right now: (1) the missed prior-week status, and (2) the standard Monday one-pager for the upcoming week. Both should land Monday morning so Srinivas has continuity.**

**A7.** Regression protection workstream is OUT OF SCOPE for the BayOne CI/CD project. It can be mentioned as something to think about but is NOT a targeted item and does NOT get assigned this week. **Treatment: include in a "Future Goals" or similar box on the internal one-pager (helpful for our internal tracking even though Srinivas didn't ask for it). On the Srinivas-facing one-pager, treat per his framing of new items added — but do not commit to it as a deliverable.**

---

## Major structural insight from Block A answers

Colin made the structural correction explicit: **we need TWO documents, not one.**

1. **Internal BayOne document** — for our own bookkeeping. Tracks open items, dependencies, upstream work, future goals, internal positioning. Not visible to Cisco.
2. **Srinivas-facing one-pager** — built exactly to Srinivas's specification (his three explicit purposes plus the access status carry-forward). Lives in the Cisco CI/CD repo as GitHub markdown.

The two have different audiences, different scope, and different formatting. They cannot be one document.

---

## Block B — Master Open Items

**B1.** Fine for internal-doc structure, but missing things per the Block A answers — specifically, we need to logically separate the master list into:
- Internal-only bookkeeping document
- Srinivas-facing document built from exactly his asks

**B2.** Collapse. Each item lives in exactly one canonical section. No cross-listing.

**B3.** [REDIRECT — needs re-ask with proper context, same reason as B2.]

---

## Block C — Temp ADS Minimum Bar

**C1.** Friday May 1 is the hard deadline for either Temp ADS or Permanent ADS. Should be delivered earlier in the week ideally; Friday is the not-acceptable-to-miss deadline.

**C2.** Translation of the "ceiling not hit" jargon Colin called out: the actual question is **"Is it acceptable to Srinivas if the Friday May 1 deliverable runs only on Temp ADS rather than Permanent ADS?"** Answer: yes. Two requirements: (1) the deliverable must be clearly portable to Permanent ADS, (2) we need to clearly communicate that we are still working on getting the Permanent ADS sorted. Per Colin's read of the call, Srinivas is genuinely compute-constrained and may not deliver the Permanent ADS at all in the short term, so BayOne sets its own internal minimum on Temp ADS regardless of what Cisco does.

**C3.** Resolved by C2. The team proceeds with Temp ADS as the minimum BayOne-controlled bar. If Permanent ADS lands at any point, all goals shift to using it. No need to wait an additional 24 hours on the Anupma deployment — start the Temp ADS work in parallel.

**Vocabulary note for Claude:** Stop using "ceiling not hit" / "floor" / "ceiling" terminology. Colin doesn't use it and didn't introduce it. Use plain language: "Temp ADS only" vs "Permanent ADS by Friday."

---

## Block D — Policy Gate

**D1.** Not going to confirm the header text. Stop overexplaining and stop asking confirmation on header-level granularity. Too granular, waste of time.

**D2.** Same as D1.

**D3.** Create all issues with a pointed header. Exact text Colin gave: **"Do not begin on this work if you have not submitted the signed policy back to: it's as simple as that."** (Header text is set; do not propose alternatives.)

**D4.** Cisco-visible repository content NEVER references the BayOne policy by name and does NOT mention it. The issues will be assigned in a BayOne repository, OR potentially in both BayOne and Cisco repos — but the Cisco repository will NEVER contain policy-related content. Internal politics never surface on a client system, ever.

**D5.** Concern raised: if any issue contains MORE than just the header line at the top about not beginning work without the signed policy, that is inappropriate. **Confirm: BayOne issues contain ONLY the header line about the policy gate. No links to policy text, no policy excerpts, no scope description, no "what the policy covers" framing. Just the one-line gate header and the actual issue content.**

**D6.** Header alone is sufficient. **Asked 4 times — stop asking.** Pattern correction for Claude: do not re-ask the same question with marginally different framing in subsequent passes.

**Net guidance for Block D:** The proposed warning header was overengineered. The actual operating text is one line, sits at the top of every BayOne-internal issue, and is never named or referenced on any Cisco-visible surface. File 04 needs to be rewritten to reflect this much-simpler reality.

---

## Block E — Sequence and Ownership

**E1.** Monday one-pager first **AFTER** the prerequisite internal documents land. The prerequisite Colin specifically called out: an internal document that tracks all open items in relation to what Srinivas asked for this coming week, with dependencies and upstream items mapped. The current `02_master_open_items.md` is not that document — it is a comprehensive engagement-history list, not a week-targeted dependency-mapped tracker. **This internal week-targeted tracker is the missing prerequisite and must be built before any Srinivas-facing one-pager.**

**E2.** Yes — internal session-folder content stays on this machine and Cisco never sees it. The Singularity translation step happens on this machine side. Eventually BayOne writes handoff documents that are sent to the Cisco machine and used to create issues. Those handoff documents are clean of all BayOne internal commentary, framing, and politics. They are entirely appropriate for client-visible surfaces.

---

## Pattern corrections recorded for future Claude behavior

1. Stop overexplaining and overgranulating. Header-level confirmation requests are wasteful.
2. Stop re-asking the same question with marginally different framing.
3. Stop using jargon (ceiling/floor) that the user did not introduce.
4. When asking the user a question, give full context in the chat. Do not require flipping between files.
5. Two-document pattern is the rule, not the exception: internal-only + client-facing. They are always separate.
6. Internal politics, framing, and commentary never appear on client-visible surfaces.

---

## Re-ask queue

Three questions to be re-asked one at a time in chat with full context and Claude's perspective:

- **A5** — decision-prompt section in the Srinivas one-pager
- **B2** — cross-listing of items in multiple sections of the master list
- **B3** — Section F exclusions in the master list

Plus an implicit follow-up from Block E1: the prerequisite internal week-targeted tracker document needs to be discussed and scoped before the Monday one-pager can be drafted.
