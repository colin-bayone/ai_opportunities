# 05 - Team Prep Meeting: Meeting Structure and Presenter Assignments

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-17/cisco-cicd-friday-meet-and-sync_01_formatted.txt
**Source Date:** 2026-04-17 (Friday morning prep meeting for Srinivas afternoon meeting)
**Document Set:** 05 (Internal BayOne prep meeting)
**Pass:** Focused deep dive on meeting structure and presenter assignments

---

## Purpose of the Prep Meeting

Colin opened the internal prep meeting by establishing that the primary purpose of the session was to get ready for the Srinivas call scheduled to occur just under two hours later. He deliberately constrained the meeting duration — cutting it off earlier than the previous week's prep session — in order to give the team approximately one hour of lead time to review the slide deck before presenting. Colin explicitly noted this was a tighter turnaround than he wanted to repeat: while Singularity had been "good enough" the prior week to produce slides in fifteen minutes before the call, he did not want to operate that close to the wire again.

Colin also flagged that the Singularity-generated slides for this week's Srinivas meeting were in the middle of being produced during the prep meeting itself ("they're actually generating right now for me"). He planned to share them in the Teams chat immediately after wrapping the prep call, which would give the team roughly an hour to review their sections before the Srinivas meeting began.

## Explicit Contrast with the April 10 Meeting

Colin framed the entire structural approach for the April 17 meeting as a deliberate correction to what went wrong on April 10. In his own words, the April 10 meeting "kind of jumped all around because Srinivas just has a different way of doing the meetings." Colin had originally prepared slides for April 10 expecting to present through them sequentially and then take questions at the end, but Srinivas turned the session into an interactive, partner-style conversation. The consequence was that Colin ended up operating as an "interactive partner" rather than as a structured presenter, and the team did not get to deliver the material in the way it had been built.

The April 17 approach explicitly corrects for this. Rather than a single narrator with slides, Colin built a section-by-section agenda with named presenter assignments. Each teammate owns a specific section, presents it directly, and is expected to stand behind the content in front of Srinivas. Colin retains the opening, the scope-alignment section, and the access-items section, but the technical content is distributed across the team.

## Section-by-Section Agenda and Presenter Assignments

Colin walked through the agenda in the order it would be presented to Srinivas, pausing at each section to name the owner and describe the expectation. The sequencing below preserves Colin's own order.

### Opening

**Owner:** Colin

Colin handles the opening of the call as he always does. No further detail was provided on the opening itself during the prep.

### Section 1 — Pain Point Analysis

**Owner:** Srikar presents, with Colin framing

This is the section Srinivas specifically requested at the end of the April 10 meeting, so Colin wanted it covered first. Srikar built the script that produced the analysis and owns the data, the taxonomy, and the categorized charts. Colin's framing role is to introduce the work and provide context; Srikar's role is to walk through what the data shows.

Colin told Srikar directly that the work was excellent and that he should present it with confidence rather than oversimplifying it. Srinivas will almost certainly ask questions, and Srikar should be ready to explain the methodology without hedging.

Colin also previewed that the full set of images Srikar had produced would appear in the slides — the same visuals already captured in the document Colin had shared with Srinivas the prior evening.

Important scoping note Colin made explicit: the pain point analysis section covers **only** the pain point analysis. It does **not** touch WebEx integration, which is reserved for Section 4. Colin emphasized this because it would be tempting, mid-conversation, to jump ahead to the WebEx integration work when discussing the chat data, and he wanted the team to resist that pull and stay on the pain point framing at this point in the agenda.

#### Open subdivision action for Srikar

Colin asked Srikar whether the off-topic/general-chat bucket (approximately 1,200 messages, including links, attachments, thank-yous, good-mornings, and screenshots) could be subdivided further — specifically, whether messages containing a link or an attachment could be split out into a "follow-ups" bucket, leaving everything else as true general chat. Srikar confirmed this was possible but had not yet been done. Colin's ask: if Srikar could do it before the Srinivas meeting, Colin would incorporate the revised chart into the slides; if not, the team would simply explain the distinction verbally.

This is an open item at the time of the prep call. Whether the updated chart is ready in time for the meeting is uncertain.

### Section 2 — Build Log Infrastructure / Existing Automation

**Owner:** Namita

Namita presents the analysis of the existing build log pipeline at a high level. The content draws from her meetings with Justin and covers the pipeline structures, the error types, the file-per-build characteristics, and — importantly — the limitations Namita identified in the existing form of that pipeline.

Colin told Namita she did not need to exhaustively walk through every file or structure. The goal is a high-level orientation that leads directly into the proposed architecture discussion. The limitations, however, should be called out explicitly because they motivate why a new architecture is being proposed at all.

### Section 3 — Proposed Build Log Architecture

**Owner:** Namita

This section immediately follows Section 2 and stays with Namita because the proposed architecture builds directly on the existing-state analysis. Colin noted he made minor consistency changes to the diagram Namita originally produced, which he would walk her through before the meeting so she would not be surprised by a changed slide.

Colin flagged this section as one Srinivas will probe heavily — architecture diagrams draw deep engineering scrutiny from him. Colin committed to helping Namita in real time during the meeting if questions got difficult, but the primary voice is hers.

### Section 4 — WebEx Integration and Open Design Questions

The WebEx section is split across multiple owners because it contains several distinct workstreams.

**Chat scraping status and architecture:** Saurav primary, Srikar backup.

Saurav owns the chat scraping work and has the full trace of the current state. Colin already knows Saurav's laptop has been unreliable, so he flagged the possibility that Saurav would not be able to screen-share or present cleanly. Colin told Saurav: if he cannot present, he should signal that in advance, and Colin or Srikar will handle the section instead. Colin's strong preference is that Saurav presents directly if at all possible.

The chat-scraping coverage is compact — one slide describing current state and deployment approach.

**Meeting recording extraction and the owner-only API constraint:** Srikar

Srikar owns what was found out about the WebEx meeting recording extraction endpoint and specifically the owner-only constraint that limits who can pull recordings via the API. Colin called this out as a significant early decision point — not a small detail — because the owner-only limitation materially shapes what is and is not possible downstream.

**WebEx architecture diagram:** Saurav

The architecture diagram Saurav produced for the WebEx integration is presented by Saurav. Again, same fallback protocol applies if his laptop fails.

**Open design questions for this section:** team collective

Each open question is attached to a section owner, who is expected to come with a recommendation. More on this in the tactical guidance section below.

### Scope Alignment — Nexus T, Pulse / Scribble

**Owner:** Colin

Colin keeps the scope-alignment section because it is politically sensitive and deals directly with the contractual scope boundary. He described it as "a more political one for sure," and wants to own it rather than hand it off.

This section covers the question of whether BayOne's work overlaps with work already underway by other Cisco teams — specifically Rui's Nexus T work and Naga's Pulse/Scribble/Scribbler work. Colin's goal in this section is to force Srinivas to clarify whether BayOne is supposed to work with those teams, alongside them, or on a completely different project.

Srikar is expected to chime in during the Pulse/Scribble portion because he has been the one interfacing with Naga. Colin asked Srikar directly for his read on Naga and whether the current state of Pulse/Scribble/Scribbler makes sense; Srikar provided context that informed Colin's approach.

### Access Items and Decisions

**Owner:** Colin

Colin owns the access-items section. The central item is the permanent ADS machine / DeepSite access block. Namita's recent discovery efforts and her raised ticket for a tenant ID are inputs Colin will cite, but he is the one framing it to Srinivas. The section ends with a forced decision point: if access cannot be unblocked, what deployment approach should the team pursue in the interim?

Colin said he would draw a firm line on this during the meeting, making clear that BayOne has followed the protocol, that the protocol itself is broken, that Colin has personally followed up with Srinivas three times in the week, and that there is no realistic path to develop or test without the access being granted.

### Open Items for Discussion

**Owner:** Colin leads, team chimes in on topic

At the end of the agenda, Colin listed all remaining open questions and designed the section so teammates are pulled in as the relevant topic surfaces. This is not a single-person section; it is a deliberate discussion block where each person speaks to their own open questions when those come up.

## Tactical Guidance Colin Gave the Team on Srinivas's Behavior

Colin spent a meaningful portion of the prep meeting coaching the team on how Srinivas operates and how to hold the room when he engages. The specific guidance falls into several clear principles.

### "Architecture is an engineer's chew toy"

Colin's own framing was that Srinivas is an engineer and engineers "love to go deep into architecture and start gnawing on the bone." Any time an architecture diagram is on screen, the team should assume Srinivas will want to dissect it. Presenters must be prepared to justify every decision visible on the diagram — box selection, arrow direction, ordering, choice of technology, anything.

The practical consequence: whoever puts up an architecture slide must own it fully and cannot hand it off mid-discussion.

### Confidence is non-negotiable when a decision has already been made

Colin was direct: "The worst thing that you can do is sound unconfident about a decision made, or like you're not sure." If the team is presenting a decision that has already been landed on, the team must present it as landed. Hedging, softening, or sounding tentative about a concluded decision is the single worst posture to take with Srinivas.

This does not mean every decision must be defended to the death (see star schema guidance below), but anything being presented as the team's position must be delivered with conviction.

### Every open question must come with a recommendation and a justification

Srinivas does not want open questions dropped in his lap as raw questions. He wants the team's proposed answer. Colin's formulation of the pattern was essentially: "with these assumptions, here's what I would give, here's why this is where I'd go — but you tell me what you want."

Each open question on the deck needs three things:
1. The assumptions the team is operating under
2. The team's recommended answer
3. The reasoning that supports that recommendation

The question itself is useful, but it cannot stand alone. And just like architecture decisions, the team must be able to justify and stand behind whatever recommendation they offer.

### Tell architecture as a linear story, even when the flow is parallel

Colin gave an explicit storytelling directive for presenting any architecture diagram: "Start at the beginning, go through each box, give the detail that you think is needed, make it a linear flow, even if it's a parallel flow."

The point is to avoid jumping around the diagram. Even when the actual execution has parallel paths, the narrative needs to walk the listener from start to end in a single coherent thread. This mirrors what went wrong on April 10 — the jumping-around dynamic is exactly the failure mode to avoid in architectural storytelling specifically.

### Srinivas's engineering bias: simple first, cheapest first

Colin flagged this as his single biggest point of engineering alignment with Srinivas personally: **simple first, least expensive first — in both compute terms and cost terms.** This is why the classification cascade leads with regex, then escalates to ML/NLP, then escalates to language models only for what the earlier tiers cannot resolve.

The warning Colin gave: "If you start out with something that is more complex than regex as a first line, he's going to be very dismissive." The team needs to lead with the cheapest, simplest layer in any architecture presented, and frame any more expensive tier as a fallback that handles what the cheap tier misses, with a feedback loop to push more volume down-cascade over time.

### Star schema posture: don't die on that hill

Colin anticipated Srinivas might push back on the star schema representation of the database layer. The prepared posture: "this is a recommendation based on our experience, not the end state. Don't die on that hill."

Colin expanded this with a broader observation that everyone has strong opinions about databases when they have not actually run production databases. Team A wants MongoDB and JSON for everything; Team B wants dimensional modeling; Team C creates a new table every time a requirement appears. If Srinivas pushes, the team should simply acknowledge that the star schema is an initial recommendation and agree to align to whatever storage architecture Cisco prefers.

This is specifically contrasted with the confidence-on-decisions guidance above. On items that are genuinely the team's recommendation based on experience, not a foundational decision, flexibility is the right posture. The distinction matters: confidence on what has been decided, humility on what has been recommended.

## Handling Pending Decisions: the "make-or-find" framing

Colin gave a specific pattern for how to present pending decisions to Srinivas — items like ML model training data where the team needs something and does not yet know if it exists on Cisco's side.

The framing is: **"Does it already exist, or do we need to make it for you? We'll make it if we need to — no problem."**

Colin's example was training data for an ML model. Rather than presenting this as a blocker, the team phrases it as a routine check: if Cisco already has labeled data, great; if not, BayOne will produce it. Colin specifically noted that what Srikar had already assembled was "90% of the way there" for training purposes, so the lift on BayOne's side is genuinely small. The phrasing is meant to communicate that either outcome is low-friction and that Srinivas does not need to worry about the item becoming a bottleneck.

This pattern should be applied consistently across every pending decision, not just ML training data.

## Saurav-to-Srikar Backup Arrangement

Saurav's laptop issues were ongoing as of the prep call. He had managed to join the prep meeting itself, but Colin was not confident Saurav would be able to screen-share or present cleanly during the Srinivas call.

The arrangement Colin set up:

- Saurav is the primary presenter for both the chat-scraping section and the WebEx architecture diagram.
- Srikar is the named backup for both.
- Colin asked Srikar and Saurav to get on a short sync in the interval between the prep meeting and the Srinivas meeting to transfer enough knowledge that Srikar can cover the material if Saurav's equipment fails mid-call.
- Colin explicitly noted he himself cannot be the backup for these sections because he has to drive the slide deck. He can talk through the material extemporaneously if absolutely necessary, but Srikar is the preferred fallback.

Srikar agreed in the meeting to sync with Saurav.

## Sequencing Summary

For quick reference, the full presenter sequence as Colin built it:

1. Opening — Colin
2. Pain point analysis — Srikar (Colin frames)
3. Build log infrastructure / existing automation — Namita
4. Proposed build log architecture — Namita
5. WebEx integration:
   - Chat scraping status and architecture — Saurav (Srikar backup)
   - Meeting recording extraction and owner-only API constraint — Srikar
   - WebEx architecture diagram — Saurav (Srikar backup)
6. Open design questions — team collective, each owner presents their question with a recommendation
7. Scope alignment (Nexus T, Pulse/Scribble) — Colin (Srikar chimes in on Pulse/Scribble specifics)
8. Access items and decisions — Colin
9. Open items for discussion — Colin leads, team chimes in as their topics surface

## Open Items and Ambiguities

Flagging items that were genuinely uncertain at the time of the prep meeting:

- **Srikar's chart subdivision.** Whether the follow-ups-vs-general-chat split would be ready in time for the slide deck was explicitly left open. Srikar committed to attempting it and sharing the updated chart if he could finish in the window. If not, the team would explain the distinction verbally during Section 1. This affects Colin's slide content and is a real uncertainty for the meeting.
- **Saurav's laptop reliability.** Saurav was present on the prep call but the underlying equipment issue had not been resolved. The backup arrangement is in place specifically because the risk is live, not theoretical.
- **Vaishali and Tanuja attendance.** Colin made clear that attendance at the Srinivas meeting was optional for both — they had only just been onboarded, the meeting would land near midnight IST on a Friday, and the transcript and recording would be shared regardless. This is a team-composition note rather than a content item.
- **Slide availability timing.** The Singularity-generated slides were being produced live during the prep meeting. Colin committed to sharing them in Teams chat as soon as they were ready and expected the team to have roughly an hour with them before the Srinivas call. Any real preparation time for individual presenters is compressed into that window.
