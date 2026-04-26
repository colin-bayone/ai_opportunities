# Srinivas Monday One-Pager Specification

**Primary sources:**
- `cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt` (Friday Apr 24 Srinivas sync, Main Set 15 transcript)
- `cisco/cicd/team/source/week_2026-04-20/day_2026-04-24/srini_MOM.txt` (combined MOMs from the Wednesday Apr 22 Srinivas meeting — item #6 is the **first** request for this artifact, plus Namita's parallel build-track MOM with the GitHub repo mandate)

**Anchor research files:**
- `cisco/cicd/research/15_meeting_access_unblocked_and_deliverables_2026-04-24.md`
- `cisco/cicd/research/15_meeting_summary_2026-04-24.md`

---

## Critical context the prior version of this spec missed

The Monday one-pager is **not a new ask from Friday**. Srinivas asked for it the prior Wednesday Apr 22 (a meeting Colin missed for a Toyota VP call). Item 6 of Srikar's MOM from that meeting reads, verbatim:

> "One slide for next meeting on the open items and access."
> — Srikar Madarapu, MOM 2026-04-22 (`srini_MOM.txt`)

Friday's "Open Items and Access" HTML document was Colin's response to that Wednesday request. When Srinivas saw it on screen Friday, he reacted with "Didn't create one last time also" — meaning the Wednesday ask had already gone unfulfilled once, and Friday's HTML deliverable, while it served the meeting, was still not the form he wanted as the recurring artifact.

This changes the framing. The Monday deliverable is not a fresh request; it is the third attempt to satisfy a standing request that Srinivas first issued Wednesday Apr 22 and then refined Friday Apr 24. Missing Monday again is not an option.

The Wednesday MOM also contains a parallel, related instruction from Namita's build-track session with Srinivas the same day:

> "Srinivas will be sharing a Github repo that we need to use for all documentation / code changes — All the learning / document (in .md format), design, architecture and source code must be checked in the repo."
> — Namita Mane, MOM 2026-04-22 (`srini_MOM.txt`)

This establishes — three days before the Friday meeting — that Srinivas had already designated GitHub markdown as the documentation standard for the engagement. Colin's Friday proposal of "GitHub markdown with Mermaid" was therefore not a novel idea Srinivas accepted on the spot; it aligned BayOne to a standard Srinivas had already set. That makes the Monday format decision essentially settled, not negotiable.

---

## What Srinivas explicitly asked for (Friday Apr 24)

His exact words:

> "can we do one thing? Didn't create one last time also. I want one summary slide of one of the delivery rules for the next week. I don't want a very huge document, just only one."

His stated intent — three explicit purposes:

> "That way we know what are the tasks we are working on. And what is the next item delivery that we are marching towards? And then we can say, do we need to add one more item or not?"

His framing of the Friday HTML on the screen:

> "Because I know this view is very hard. I can say, OK, what is the birthday view of the entire summary, right?"

("birthday view" = bird's-eye view, dictation slip)

> "Catch what the team is working on."

Colin's commitment:

> "OK, I'll get a simple view for Monday."

Srinivas confirming:

> "Yeah, just a simple, make it simple, just one slider. And then we'll track where we are, what is the current status, and any new items that we are adding for the next week."

Srinivas re-emphasized the bird's-eye purpose later when authorizing the regression-protection workstream as a new scope item:

> "So that's a new item getting added. So that's why I need one border [bird's-eye] view. items while we are walking, the Lord [board] and while we are riding, that will be much easier."

Two things to draw from that second quote. First, Srinivas explicitly tied the one-pager to scope-change tracking — when something gets added (like regression protection), it has to land on the board so he can see it without re-reading transcripts. Second, his phrasing "while we are walking ... and while we are riding" reinforces that the artifact is for at-a-glance use during day-to-day work, not for set-piece review meetings.

## Format decision (Friday Apr 24, ratifying the Wednesday Apr 22 standard)

Colin proposed:

> "Would it be OK with you if we did? Because we did this actually internally. We can have that in GitHub. They're just basically markdown files, mermaid charts if you need a graphic. That way you can actually see. We go over, we can see this."

Srinivas immediately endorsed and pointed Colin at the right repository:

> "You can use the issues listed in the CI CD itself. You can add there also. You can use GitHub itself. That's how we do the other products."

Colin:

> "OK, perfect. Easy enough. Less work for me too, honestly. So that's great."

Decisions ratified:

- **GitHub markdown file** in the **main Cisco CI/CD repository** (the same repo the Wednesday Apr 22 MOM designated for all `.md` documentation, design, architecture, and source code)
- **Mermaid charts** when a graphic helps
- **Working items tracked as GitHub issues in the same CI/CD repository's issues list**

This means the Monday artifact is **not** a slide deck and **not** an HTML document like Friday's deliverable. It is a markdown file in the CI/CD repo, with linked GitHub issues for working items, and Mermaid only where it earns its keep. It also aligns BayOne with the workflow Srinivas already uses for other engineering products at Cisco — Srinivas's "That's how we do the other products" quote.

Colin further committed to deliver the first version the same day as the Friday meeting, not on Monday:

> "Yes, yes, I can do that. I'll actually, why don't I do this? Even after this meeting, I'll get that prepped for you today itself. I'll get that sent over so you at least have it today, and then we'll continuously update that. We'll keep it simple, we'll keep it straightforward, so it's not this big wall of text I'll add to your review."

This is a commitment to a same-Friday first-cut plus continuous update, separate from the Monday baseline. The Monday version becomes the standing weekly reference; the same-Friday version is the bridge.

## Five explicit content requirements (combined Wednesday + Friday)

From the Wednesday Apr 22 MOM (Srikar, item 6): the artifact tracks **open items and access**.

From Friday Apr 24 (Srinivas's three purposes plus tracking elements):

1. **What tasks are we working on** (current in-flight)
2. **What is the next item delivery we are marching towards** (the next-Friday target)
3. **Do we need to add one more item or not** (decision prompt)
4. **Where we are / current status** against each tracked task
5. **New items being added for the next week** (especially when Srinivas adds scope, e.g., regression protection)

The five together are non-negotiable. The Wednesday open-items-and-access framing means access status (ADS, NX repo, CI/CD repo, DeepSight, MCP viewer) belongs on the page even after items resolve, at least until they are stably closed.

## What Friday's deliverable was vs what Monday's becomes

- **Friday "Open Items and Access" HTML document** served its purpose for the meeting and is the detailed working format. Srinivas does not want it as the recurring artifact.
- **Monday becomes the standing weekly artifact.** Single page. GitHub markdown. Lives in the Cisco CI/CD repository. Mermaid where it earns its keep. Working items as GitHub issues in the same repo.
- **Same-Friday bridge version** (Colin's commitment to deliver the first cut Friday evening Apr 24) seeds the Monday baseline so Srinivas has continuous visibility over the weekend.

## Proposed structure for the Monday one-pager

Single markdown file in the main Cisco CI/CD repository. Suggested filename: `weekly_status_2026-04-27.md` (or whatever Srinivas's existing repo naming convention dictates — confirm against the repo before writing).

### Header

- Date range covered (Apr 27 to May 1)
- One-sentence framing of the next-Friday target locked in Main Set 15
- Link back to the prior week's status file once the pattern is established

### Section 1: Where we are heading (the next-Friday target)

The deployment target Srinivas locked down on Apr 24:

- CI/CD application running on ADS (permanent if Mahaveer access resolves; temporary ADS as fallback)
- CAT MCP plugged into the backend
- Static FAQ entries for environmental issues plus dynamic answers via CAT MCP
- Both routes feed the same chat user interface in the CI/CD application
- WebEx bot deployed on the NX-OS CI pipeline sharing the same backend (Service Application Platform style backend with pluggable frontends)
- LLM via circuit API initially; per-user DeepSight credentials when issued

A simple Mermaid diagram showing two-frontend, one-backend, two-routing-paths is the visual that earns its keep here. This is the only place a graphic is clearly worth it; everything else can be plain markdown.

### Section 2: What we are working on this week (current tasks)

Each item links to a GitHub issue in the CI/CD repo issues list. One line per item. Owner. Status (not started, in progress, blocked, done). Target completion within the week.

This list comes from the master open items in `02_master_open_items.md` filtered to what is achievable this week and aligned to the next-Friday target.

### Section 3: Open access items and their status

Carries the Wednesday Apr 22 "open items and access" framing forward. Even when items resolve, they stay listed for one cycle so Srinivas can see the closure trajectory.

- ADS access (Mahaveer escalation status; permanent vs temporary fallback)
- NX repository lead-only group (Srinivas to add user IDs personally; Colin sent IDs Friday)
- CI/CD repository (resolved — main repo confirmed as destination, not SME-KB)
- DeepSight credentials (pending product demo)
- MCP viewer app (coming soon as playground for external MCP testing)

### Section 4: New items being added this week

Anything that was not on the Friday Open Items document but is being added now. Each linked to a new GitHub issue. The current example is the regression-protection workstream (Playwright UI automation plus backend validation, modular adapter pattern) that Srinivas added at the end of the Friday meeting.

### Section 5: Decision prompt for Srinivas

The explicit "do we need to add one more item or not" question Srinivas asked for. Concise. One or two specific candidates if BayOne sees them. Otherwise: "Nothing new from our side this week. Anything from yours we should add."

## What does NOT go on the one-pager

- Internal team accountability content (Team Set 14a, 14b, 15 internal-only material)
- Person-by-person performance characterizations
- Cisco IT incident detail beyond what is operationally relevant
- Mahaveer or any other Cisco-side individual diagnostic
- Pricing or commercial framing
- Methodology overhead (how the BayOne AI practice does research, etc.)
- Wall-of-text narrative — Srinivas was explicit: "I don't want a very huge document, just only one."

## Open questions for Colin

1. Confirm `weekly_status_<date>.md` as the filename, or align to whatever convention the existing CI/CD repo already uses for `.md` documents (Srinivas's other-products workflow may have a pattern worth matching)
2. Confirm the same-Friday first cut Colin promised on Apr 24 was actually sent. If not, the Monday version absorbs that commitment and the spec should note the slip
3. Confirm the open-access-items section (Section 3) is appropriate even after items resolve, or whether resolved items should drop off immediately
4. Confirm Mermaid is appropriate for the next-Friday target diagram or whether plain markdown text is sufficient — Srinivas's use of "birthday view" / "border view" suggests he values the at-a-glance picture, which favors keeping the Mermaid
5. Confirm the decision-prompt section is appropriate or whether it reads as soliciting scope creep
6. Confirm scope of "this week" is Monday Apr 27 through Friday May 1 (the contract-renewal demo Friday)
7. Confirm whether the regression-protection workstream gets its own GitHub issue this week or rolls into the next-Friday target as a stretch item
