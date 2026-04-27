# Handoff to Next Claude Session — Cisco CI/CD Weekly Status One-Pager

**Date prepared:** 2026-04-26 evening (Sunday)
**Reason for handoff:** Prior Claude session repeatedly failed to satisfy Colin's structural requirements for the Srinivas-facing weekly status one-pager despite multiple corrections. Specifically: conflated three different states in a single table column, then in the corrective version produced a "Delivered to date" table that mixed actual deliverables with access requests and architectural decisions that are not deliverables. Colin's patience is exhausted on this artifact and you are picking up cold. Read this entire file before doing anything.

---

## 1. The single most important thing

You are producing **one document** for Srinivas Pitta. He asked for it on the call Friday April 24, 2026. He had also asked for it Wednesday April 22 (item 6 of Srikar's MOM in `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srini_MOM.txt`: "One slide for next meeting on the open items and access").

**Vocabulary discipline.** Srinivas used the word "slide" interchangeably with "document." Colin has explicitly forbidden the word "slide" — it's a single-look document, format is GitHub markdown in the Cisco CI/CD repository per Colin's commitment on the Friday call. Do not use the word "slide" in chat with Colin or in any artifact. It is a markdown document.

The destination repository is Cisco-owned. It will be visible to Srinivas, Anupma, Justin, Anand, and any other Cisco engineer in the engagement. **Apply all four exclusion rules in `claude/2026-04-26_cisco_cicd_week_planning/10_exclusion_rules.md` strictly:** no cross-engagement references (no Guhan Raman), no internal personnel observations, no DELIVERED items on open lists in the wrong way, no internal politics, no BayOne policy mention.

---

## 2. What Srinivas asked for, in his own words

From the Friday Apr 24 transcript at `cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt`:

> "I want one summary slide of one of the delivery rules for the next week. I don't want a very huge document, just only one."

> "That way we know what are the tasks we are working on. And what is the next item delivery that we are marching towards."

> "Yeah, just a simple, make it simple, just one slider. And then we'll track where we are, what is the current status, and any new items that we are adding for the next week."

> "So that's a new item getting added. So that's why I need one border view. items while we are walking, the Lord and while we are riding, that will be much easier."
(transcript noise: "border view" = bird's-eye view; "Lord" = board)

From Wednesday Apr 22 MOM (`cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srini_MOM.txt`), Srikar item 6:

> "One slide for next meeting on the open items and access."

## 3. What Colin restated in chat (Sunday Apr 26 evening)

Colin restated the structural ask, addressing the prior session's failure to separate states:

- What was delivered so far
- What is going to be delivered this week
- Things that are in progress
- Things that are completed

These are FOUR distinct states. They MUST be separated. Do not blend them in a single column. Do not mix them in a single table. Do not put a "Status" column that mixes "complete," "in progress," and "not started" in adjacent rows.

## 4. Format decisions already locked

- GitHub markdown in `cisco/cicd/deliverables/` directory
- Filename pattern: `weekly_status_<date>.md` (Colin approved A1 in `05a_answers_and_redirects.md`)
- Mermaid charts allowed as supplemental visual; primary representation is plain markdown text and table view (Colin approved A4)
- Mermaid diagram and the future-state target paragraph go AT THE END (Colin's rule)
- Future-state language is FUTURE TENSE ("will be deployed"), not present tense
- No "Coverage" sub-line in the header
- No "(target for Friday May 1)" or similar parenthetical noise in headings
- No decision-prompt section soliciting Srinivas to add scope (Colin vetoed in A5 — "drop, reject, drop it entirely")
- Recent closures appear strikethrough only if resolved between the last meeting and this update
- New items added this week section is declarative, kept short

## 5. The prior session's specific failures (so you do not repeat them)

The prior session produced two attempted versions at:
- `cisco/cicd/deliverables/weekly_status_2026-04-27_v1_separate_sections.md`
- `cisco/cicd/deliverables/weekly_status_2026-04-27_v2_grouped_substables.md`

Colin rejected both with the following critique. Read it carefully:

> "You have something that says 'delivered to date', and it doesn't even call out exactly what is delivered. It's not even categorized."
>
> "You're trying to say three things are in progress this week. That is not true."
>
> "You said things delivered to date, which you somehow managed to mix access requests with things that have been delivered, which makes no fucking sense."
>
> "You said that deployment architecture is decided, which is: Not deliverable, Not true. Like repository destination clarified, how is that a deliverable?"
>
> "There have been plenty of other things that have been delivered that you could have called out, but you didn't."

**Three concrete classification errors the prior session made:**

1. **"Permanent ADS standalone provisioning request — Submitted Friday April 24"** was placed in "Delivered to date." A submitted request is not a deliverable. It is an access item.
2. **"CN-SJC-STANDALONE bundle membership request — Submitted Friday April 24"** was placed in "Delivered to date." Same error.
3. **"Deployment architecture decided"** and **"Repository destination clarified"** were placed in "Delivered to date." Architectural decisions and clarifications from a meeting are not deliverables. They are decisions or open-item resolutions.
4. **"Service Application Platform style backend — Architecture work underway"** was placed in "In progress this week." Architecture-work-underway is vague enough that Colin disputed whether it counts as in-progress this week. Be skeptical of bucket assignments that read as filler.

**The Delivered list also missed real deliverables Colin says exist.** The prior session pulled from the Set 15 summary's "Status of Main Workstreams" block but did not go deep enough into the engagement history to enumerate everything BayOne has actually shipped. You need to do this work properly — read across the team research chain (Sets 07 through 15), the team tracking files, and any artifacts in the deliverables and team source folders to build a real inventory of shipped work.

## 6. What you need to do, in order

### Step 1 — Read the source material before drafting anything

In this order:

1. `claude/2026-04-26_cisco_cicd_week_planning/10_exclusion_rules.md` — what NEVER appears on a Cisco-visible artifact
2. `claude/2026-04-26_cisco_cicd_week_planning/05a_answers_and_redirects.md` — Colin's answers to format and structural questions, including the four-state split, the future-tense rule, the no-decision-prompt rule, the closure-strikethrough rule
3. `cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt` — Friday Apr 24 Srinivas sync transcript, the source of truth for what Srinivas asked for
4. `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srini_MOM.txt` — Wednesday Apr 22 MOM, source of the open-items-and-access ask
5. `cisco/cicd/team/planning/internal_week_tracker_2026-04-27.md` — internal tracker with the dependency map for the week. **This is the upstream source for what is in progress and what is planned to start this week.** Do not reinvent these classifications; consume them from this file.
6. `cisco/cicd/team/research/14b_expectations_and_outstanding_actions_2026-04-24.md` — comprehensive 136-item delivery-state catalog with status categorizations. **Use this as the basis for the Delivered to date inventory.** Filter on items marked DELIVERED or DELIVERED (NARROW) and decide which belong on a Cisco-facing artifact.
7. `cisco/cicd/research/15_meeting_summary_2026-04-24.md` and the deep-dive files in the same folder — for the next-Friday target framing
8. `cisco/cicd/team/research/15_1on1_*.md` (excluding the INTERNAL ONLY leadership-ask file) — for engagement state context
9. `claude/2026-04-26_cisco_cicd_week_planning/08_chat_findings.md` — for material clarifications from chat content the Singularity may not yet capture (NX repo provisioning is via Anupma, login prerequisite, etc.)
10. The current rejected drafts at `weekly_status_2026-04-27.md`, `weekly_status_2026-04-27_v1_separate_sections.md`, `weekly_status_2026-04-27_v2_grouped_substables.md` to understand what Colin rejected and why

### Step 2 — Build a real inventory of what BayOne has actually delivered

This is where the prior session failed worst. Do this work properly.

A "deliverable" for the purposes of this artifact is a concrete artifact, code, or capability that BayOne has shipped that Srinivas could plausibly inspect or use. NOT:

- Access requests submitted (those go in "Open items and access")
- Architectural decisions made in meetings (those are decisions, not deliverables)
- Repository destinations clarified (that is an open-item resolution)
- Sign-off on a plan (planning is not delivery)

Examples of what likely DOES qualify (verify against actual research files before using):

- The 25+ category issue classification taxonomy from the 4,231-message NX-OS CI workflow scrape
- The eCharts dashboard built on top of that classification
- The WebEx bot complete on the webex-skills branch (Wall-E)
- The single-commit attribution working code
- The CAT MCP integration setup with four tools identified and OAuth resolved
- The Mermaid architecture diagrams for WebEx and logs tracks
- The Singularity-built prep documents and slide decks shared with Srinivas previously

For each candidate, verify it is real (file or repo evidence exists), it was shipped (not just discussed), and Srinivas would recognize it as a deliverable. Cite the source file or research entry that proves the deliverable exists.

### Step 3 — Categorize the deliverables

Colin's critique included "It's not even categorized." Group the deliverables by workstream so the list reads as organized work, not a flat dump. Likely groupings:

- **Build log / log analysis track** (Namita's primary domain)
- **WebEx and bot track** (Saurav's primary domain)
- **Issue categorization and dashboard** (Srikar's primary domain)
- **Architecture and integration design** (cross-cutting)
- **CAT MCP integration** (cross-cutting, Srikar lead this week)

Verify these groupings make sense against the actual deliverables you find. Do not impose a structure that does not match the work.

### Step 4 — Build the four state tables (or grouped equivalent)

The four states Colin restated:

1. **Delivered (cumulative across the engagement)** — categorized by workstream per Step 3
2. **In progress this week** — items currently mid-stream. Be honest about how many there really are. Do not pad.
3. **Planned to start this week** — items targeted to begin but not yet started
4. **Completed this week** — items shipped between the last Srinivas meeting (Apr 24) and the current update. These may also be the strikethrough closures.

States 2 and 3 should come from the internal week tracker at `cisco/cicd/team/planning/internal_week_tracker_2026-04-27.md`. Do not invent new categorizations of in-progress vs planned-to-start. Consume the tracker's classifications.

State 4 may overlap with the Recent Closures strikethrough section. Decide whether to fold them together or keep separate; ask Colin if uncertain.

### Step 5 — Build the supporting sections

These are largely already correct in the rejected drafts; you can adapt them. The supporting sections:

- **Open items and access** — table from Wednesday MOM directive 6. Same as in the rejected drafts; that part was not the failure.
- **Recent closures** — strikethrough items resolved between the last Srinivas meeting and the current update.
- **New items added this week** — declarative line. If no new BayOne scope, say so.
- **Future pipeline** — the May 1 target description in FUTURE TENSE plus the Mermaid diagram. Goes at the end.

### Step 6 — Apply final discipline

Before showing Colin:

- Read `10_exclusion_rules.md` again and audit every line of your draft against it
- Confirm no "slide" anywhere in your chat or document
- Confirm future tense for the future-pipeline paragraph
- Confirm no parenthetical filler in headings
- Confirm no "Coverage:" header sub-line
- Confirm Mermaid placement at the end
- Confirm no decision-prompt section
- Confirm em dashes are not used (BayOne deliverable rule)
- Confirm no individual names, no contractions, no contrastive framing
- Confirm tables use one consistent column structure (Item + one detail/status column)
- Confirm the Delivered table is genuinely categorized by workstream, not a flat dump
- Confirm every Delivered item is a real shippable artifact, not a meeting decision or an access request
- Confirm In Progress and Planned to Start come from the internal week tracker, not from your own invention

### Step 7 — Present to Colin

Show him ONE version, not two. The prior session offered two and was rejected on both because the underlying classification was wrong. Get the classification right, then present.

When you present, lead with: "I built the Delivered list from <list of source files you actually consulted>. Here is the categorization I used and why." Be ready to cite source files for every Delivered item. Colin will challenge bucket assignments; you need to defend them with evidence or accept correction quickly.

## 7. Files in the session folder, what they are

- `00_session_notes.md` — the working-session frame
- `01_srinivas_monday_onepager_spec.md` — the spec for this artifact, corrected for Wednesday MOM origin and GitHub markdown standard
- `02_master_open_items.md` — comprehensive engagement-history open items list (internal use only)
- `03_temp_ads_minimum_bar.md` — internal floor framing for the Friday demo
- `04_policy_gate_status.md` — BayOne Client Data Handling Policy state and the issue header text
- `05_open_questions_consolidated.md` — the original open questions document
- `05a_answers_and_redirects.md` — Colin's answers to those questions, plus pattern corrections
- `06_team_chat_internal_through_2026-04-26_1600.md` — BayOne internal team WebEx chat through Sunday 4 PM ET
- `07_group_chat_with_cisco_through_2026-04-26_1600.md` — BayOne + Cisco joint WebEx chat through same time
- `08_chat_findings.md` — material clarifications from the chats including Anupma-as-NX-provisioner, login prerequisite, RHEL8, Saurav circuit token, Nova-internal-project-not-our-concern internal positioning
- `09_attachments_placement_guide.md` — done; attachments already moved into Singularity source folders
- `10_exclusion_rules.md` — the four exclusion rules; canonical source of truth
- `HANDOFF_TO_NEXT_SESSION.md` — this file

## 8. Files outside the session folder you must consult

- `cisco/cicd/team/planning/internal_week_tracker_2026-04-27.md` — the internal week tracker built earlier this session; source for in-progress and planned-to-start items
- The three rejected weekly status drafts in `cisco/cicd/deliverables/` (do not delete; Colin will compare)
- The Singularity research chain at `cisco/cicd/research/` and `cisco/cicd/team/research/`
- The action items, decisions, blockers, cross-reference files at `cisco/cicd/team/tracking/` and `cisco/cicd/team/cross_reference.md`

## 9. Behavioral guardrails for working with Colin

These are accumulated from this session and from user memory. Internalize before engaging.

- **No filler questions.** Do not ask granular header-level confirmations. Think first, propose with rationale, accept correction quickly.
- **Do not re-ask the same question with marginally different framing.** Colin called this out three times this session.
- **Planning goes in files, not in chat.** If you are about to write a multi-paragraph plan in chat, write it to a file first.
- **Never put designs in chat.** Same rule.
- **Internal politics never on client surfaces.** Period.
- **No Guhan Raman or any other client reference** in any artifact for this engagement.
- **Cite sources.** When making any claim about what was decided, what was delivered, what is in progress, cite the file path and the quote.
- **Memories are unreliable; files persist.** Trust files over memory for any rule or decision.
- **Do not propose deleting a rationale or rules file** without verifying the rules persist elsewhere.
- **Two-document pattern is the rule, not the exception.** Internal-only and client-facing are always separate.
- **Drop the word "slide."** It is a one-look document.
- **Future tense for future-state descriptions.** Present tense reads as a false claim of completion.
- **No parenthetical filler in headings.** No "(target for Friday May 1)," no "(between last meeting and this update)."
- **Strict adherence to user-stated structure.** When Colin says four states, build four state tables. Do not consolidate them under your own judgment about visual simplicity.
- **Auto mode does not mean autonomous decision-making on style or structure.** It means execute approved direction without asking permission for routine action. Structural choices are NOT routine.
- **Reading is not optional.** When Colin says he gave you the transcript and the MOM, treat reading them in full as a precondition for proposing structure. The prior session's structural failures all trace back to insufficient source-reading.

## 10. Open items at handoff (status as of Sunday 2026-04-26 evening)

- The Srinivas-facing weekly status one-pager is rejected in all three current versions. Build a fresh one per Sections 6 and 7 above.
- The internal week tracker at `cisco/cicd/team/planning/internal_week_tracker_2026-04-27.md` was approved by Colin and does not need rework. Use it as a source.
- Three signed Client Data Handling Policy copies received as of Sunday 4 PM ET; three pending. Working assumption all six in by Monday morning.
- All chat content from both WebEx chats is captured in files 06 and 07; cross-referenced in file 08.
- Six attachments from the chat have been moved to the proper Singularity source folders. Work done.
- The three Cisco-side reference attachments (Mahaveer ADS PDF, Srinivas CD impact graph) have not yet been processed into the Singularity research chain. May warrant a 14c or 15b backfill set later this week. Not urgent.

## 11. The exact question to ask Colin first

When you start the next session, do not start drafting. Ask Colin one question:

> "Before I draft the weekly status one-pager, I want to confirm I have the right read on the Delivered category. Can I propose the categorized inventory of delivered work to you in chat first, with source citations for each item, before I put anything in the document?"

Get his approval on the inventory and categorization first. THEN draft the document. THEN present.

Do not produce two versions. Produce one, defend it, take correction, iterate.

## 12. End-of-handoff acknowledgment

Colin's exact words at end of session:

> "I am just failing to understand how this happened and how you're doing so poorly. In any case, you're fired."

Take the critique seriously. The prior session's failures were not edge cases; they were repeated structural errors despite multiple corrections. Read this handoff, read the source material, ask the gating question in Section 11, and proceed with discipline.
