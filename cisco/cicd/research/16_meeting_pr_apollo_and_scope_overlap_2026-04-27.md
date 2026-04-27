# 16 - Srinivas Sync: PR Apollo, Builder Triaging, and Scope Overlap

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on the discovery of Justin's PR Apollo MongoDB and the Builder Triaging tool, the resulting scope-overlap concern, and Srinivas's unawareness of both

---

## Executive summary

Mid-meeting, while Colin was walking through the BayOne plan to deploy a WebEx bot for the NX-OS CI workspace combining a static FAQ path with a dynamic CAT MCP path, Divakar Rayapureddy interrupted the flow to surface two pre-existing Cisco-internal artifacts that materially overlap with what BayOne is building:

1. **PR Apollo.** A Cisco-internal system already deployed (last week, around April 21 to April 24), built and operated by Justin Joseph, which captures all GitHub events for the NX CI repository into a MongoDB and is intended to back PR insights for engineers.
2. **Builder Triaging tool.** A separate Cisco-internal Justin Joseph build that is already in active production use by the client team and the kernel team, and has been the engine for the clang migration. Approximately 800 features have been processed through it. Cisco is "incorporating" it into the PR workflow so engineers can request that their PR be run through Builder Triaging and receive a possible-fix recommendation.

Srinivas was visibly unaware of both, despite Divakar having reportedly raised both in a prior weekly meeting (referred to as the "C was meeting" / "Shiva's meeting") on the previous Wednesday or Thursday. Srinivas explicitly said "this information is new to me also." Divakar followed up with a polite but pointed jab about Srinivas missing meetings, framed as "before we go technical, one request is if you can join the meeting." This is the first time in this engagement that the BayOne team has directly seen a coordination gap on the Cisco side surface in a meeting.

The substantive consequence: BayOne's planned dynamic answer path (CAT MCP integration plus the build dependency graph for commits and PRs) overlaps in part with what PR Apollo and the Builder Triaging tool already do. Srinivas reframed the meeting around his anti-duplication concern: "I want to make sure that the calling and teams' energy is utilized for the best, okay? Yes. And not duplicate the work. That we are doing versus they are doing." The agreed concrete next step is for Justin to create a generic read-only user ID against the PR Apollo MongoDB and share it with Colin's team so we can inspect what is already there before deciding whether to extend it or build the parallel BayOne capability.

This is the single most consequential surfacing of the day, and it directly affects the scope of the Friday May 1 deliverable.

---

## Artifact 1: PR Apollo

### What it is, in Divakar's words

Divakar (transcript line 314 onward, lightly de-mangled):

> "We have another one, right? I think I discussed this with you in Shiva's meeting time. The PR Apollo, where we have the entire database going in. I think we have the database available. I don't know if you wanted to deploy one more. We recently deployed one, and we are clicking [capturing] all the details, all the. Even ts [events] coming in from the GitHub and saving it into a MongoDB. Okay, and we can use that MongoDB to do other activities on top of it. Where you wanted to include one more."

Justin confirmed the scope:

> "This is for the CI work webex." (Line 332)
> "This is for CI." (Line 334, restated by Divakar)

And later, Justin reconfirmed and broadened (line 1006 onward):

> "And, then the GitHub data should also contain that I have. Like once we're, yeah I'll try to get you that GitHub or we just created a new data, a MongoDB like recently last week or something. So, that should also have that data as well. Okay. Um, any yeah, whatever the GitHub is posting, we should be collecting that now."

### Distilled facts

- **What it captures:** All GitHub events from the NX CI GitHub repository, persisted into a MongoDB. The phrase "whatever the GitHub is posting, we should be collecting that now" indicates broad event coverage, not a narrow slice.
- **Scope:** Specifically the CI WebEx / CI workflow repository. Justin explicitly narrowed it: "This is for the CI work webex" / "This is for CI."
- **Deployment status:** Recently deployed. Justin said the new MongoDB was created "last week or something," which on a 2026-04-27 reading lands sometime in the April 20 to April 24 window.
- **Owner:** Justin Joseph. Divakar deferred to Justin throughout this segment ("Jason, you have the data right for the company.").
- **Intent:** Back PR insights for engineers. Divakar's later quote: "if somebody come and say, 'Hey, show me all my PRs,' it will give them a table to say that these are the PRs, and this where it is stuck. And this where the problem is."
- **Discoverability layer planned:** Divakar floated layering an MCP server on top of the MongoDB so the data is queryable by tools: "We can create a MCP server on top of the data. We are already procuring it for you to be able to view the data and make some inferences on top of that."

### Where this overlaps with BayOne's plan

BayOne's Friday May 1 deliverable plan (per the v3 status table) commits to:

- Wiring a "dynamic answer path" through CAT MCP to query the NX repository at request time, surfaced through the WebEx bot and the CI/CD application chat.
- Building a "build dependency graph for commits and PRs" using deeper Git-native mapping.

PR Apollo overlaps both. It is already capturing GitHub events into a queryable store, and an MCP layer is planned for it. The CAT MCP path remains complementary (CAT MCP queries the NX repository's care-request system), but if PR Apollo is supposed to be the canonical "show me my PRs and where they are stuck" layer, then BayOne's PR-centric pieces and any PR-state querying we build into the dynamic path need to consume from PR Apollo rather than build a parallel store.

---

## Artifact 2: Builder Triaging tool

### What it is, in Divakar's words

Divakar (line 384 onward, de-mangled from "bidder triaging"):

> "And we are incorporating the builder triaging, right? We have just enrolled the builder triaging, which is being used for the clang migration. It's being used for different different projects. That one we are incorporating into the PR as well. So the engineers can go click on it and say, 'Hey, I want my PR to go through this builder or triaging.' Bring in that information back to the user and tell them, 'This is the possible fix for you.'"

And the volume datapoint (line 396 onward):

> "We have given it for the client team and kernel team as well, which is which email team [likely 'image team' or a specific team name; flag uncertain] is already actively using it for all their conversions. They converted about eight hundred features. They put it through the tool."

### Distilled facts

- **What it does:** Takes a build (or a PR's build) and returns a possible-fix recommendation. Effectively a triage assistant that can be invoked against a candidate PR.
- **Owner / developer:** Justin Joseph. Divakar's later attribution is explicit: "developed by Justin was also discussed previous week."
- **Adoption inside Cisco:**
  - Client team: in active production use.
  - Kernel team: in active production use.
  - Clang migration: it is the engine being used for the clang migration effort.
  - One of those teams ("email team" in the transcript, almost certainly a transcription error for "image team" or another specific team name; flag uncertain) has put approximately **800 features through the tool** for their conversions. This is a real production volume datapoint, not a demo.
- **Status with respect to the PR workflow:** Cisco is currently incorporating it into the PR workflow itself, exposing it as a click-to-invoke action where an engineer can route their own PR through it.
- **Output intent:** The tool returns a "possible fix." Srinivas immediately constrained the framing: "Don't go to the fix yet. I think I think." Divakar held the line: "We are giving a possible fix because that's being applied also for the official build." The unresolved point is whether the bot surfaces the proposed fix verbatim or simply points the user at it.

### Where this overlaps with BayOne's plan

BayOne's plan for the Friday deliverable includes a dynamic answer path that, for PR-stuck cases, would help the user understand where the PR is stuck and what to do about it. Builder Triaging is, in essence, the existing Cisco answer for the "what to do about it" half of that question for a specific class of failures. The natural design is for the bot to invoke Builder Triaging when the question is in its domain rather than have BayOne reimplement a fix-recommendation layer.

The 800-features datapoint is also independently useful: it means there is a substantial corpus of triage runs that could inform the static-answer FAQ wiring, by mining recurring patterns in what the tool has already recommended.

---

## Srinivas's unawareness, on the record

When Divakar surfaced PR Apollo (line 326), Srinivas's first response was:

> "Okay, but Justin was not telling us. I didn't know. So maybe Justin is not aware."

Justin then confirmed he was the owner. Srinivas's follow-up (line 340 onward) is a small but telling moment of disorientation:

> "Yeah. I'm not uh so I think sorry for having use this. Rohit since you are missing some meetings there is a confusion okay. Two things are there."

(The "Rohit" token is almost certainly a transcription error. In context it reads either as a self-correction "sorry, I'm having to use this" / "sorry I'm" or as Srinivas addressing a third party. We have no other evidence of a "Rohit" in this engagement; flag as a likely speech-to-text artifact rather than a real person.)

After Divakar laid out the full picture of PR Apollo plus Builder Triaging plus the 800-feature volume, Srinivas was explicit (line 400):

> "Okay, so okay, I think there is a disconnect. Okay. Okay, so I've actually first of all this information is new to me also. So I don't know that we had it. But we wanted to know two things."

Two things to register here:

1. The C-S-E-D leader did not know that one of his own team's tools was already in production with 800 features run through it for the clang migration.
2. He said so on the record, in front of the BayOne team. He did not try to paper over it. That is a positive signal about how he handles being caught off guard, and it is consistent with his anti-duplication framing that follows.

---

## Divakar's polite jab

Immediately after Srinivas's "this information is new to me also," Divakar pushed back, gently but without softening the substance (line 405):

> "But one, one okay. Before we go technical, one request is if you can join the meeting. It is easy for all of us. I am one. I think that I mentioned it. There are times where we are actually losing. I am not able to join all the meetings, but I do whenever I have a time, definitely will come. But, we can we can discuss offline if you wanted to come over or i i try to discuss this one in the C was meeting. You are also there in that meeting, So I am assuming you are getting all the information there because PR Apollo was discussed last week. We also discussed. Imran was mentioning about the bidder, triaging and other things, which developed by Justin was also discussed previous week. So I'm hoping you are up to date on that one, but yeah, we can discuss. Maybe I need a discussion. No worries. No worries."

What this carries:

- **Clear, polite jab:** "if you can join the meeting. It is easy for all of us." Divakar opens by softening with "before we go technical, one request" but the request itself is unambiguous: Srinivas has been missing meetings.
- **Self-deprecating cover:** "I am not able to join all the meetings, but I do whenever I have a time." Divakar gives Srinivas a face-saving frame, but the next sentence reasserts the point.
- **The factual escalation:** Divakar names the specific meeting series ("the C was meeting" / "Shiva's meeting"), confirms Srinivas was on the invite list ("you are also there in that meeting"), and lists the agenda items that were already covered there: PR Apollo and Builder Triaging, the latter raised by Imran and developed by Justin, both discussed "previous week."
- **The apology that isn't quite an apology:** "Maybe I need a discussion. No worries. No worries." Divakar walks himself back at the end so the meeting can move on without escalating, but the substantive point is on the table for everyone in the room.

This is the first time in this engagement that we have seen an internal Cisco coordination gap surface visibly in front of BayOne. It is worth noting, but not worth amplifying back into Cisco-visible material. Internal use only.

---

## Names to add to the engagement landscape

### Imran (no last name yet)

Divakar's quote: "Imran was mentioning about the bidder, triaging and other things, which developed by Justin was also discussed previous week."

Reading: Imran is a real Cisco engineer who was present in the prior week's "C was meeting" / "Shiva's meeting" and who raised Builder Triaging in that forum. He is meaningful enough to the C-S-E-D conversation that Divakar names him spontaneously while pushing back on Srinivas. We do not yet have his last name, role, team, or relationship to the engagement.

**Action:** Add Imran to the watch list for the engagement org chart. He is likely an internal Cisco engineer adjacent to the PR / build infrastructure space and may surface again as a counterpart on the dynamic answer path. Do not add him to any client-visible artifact until we have a full name and a confirmed role.

### Rohit (uncertain, likely transcription artifact)

Srinivas's "Rohit since you are missing some meetings there is a confusion okay" reads more naturally as either a self-correction ("sorry, I'm having to use this. Sorry I'm... since...") or a misheard token. We have no other reference to a Rohit in this engagement. Flag as uncertain; do not propagate.

---

## The "C was meeting" / "Shiva's meeting" timeline

Divakar refers to a specific Cisco-internal meeting series multiple times in the segment, with three different transcript renderings:

- "Shiva's meeting" (twice)
- "the C was meeting"

Reading: this is one meeting series, not two. The most plausible canonical name is "C-S-E-D meeting" (since C-S-E-D is the umbrella under which PR, Builder Triaging, and PR Apollo all live, per Srinivas's framing earlier in the same conversation: "C S E D contains the build. The PR, correct, and also the build infrastructure all three pieces."). "Shiva's meeting" might be a separate, related meeting hosted by someone named Shiva (potentially a Cisco architect or director not yet in our org map), or it could be a different rendering of the same meeting series. Flag as ambiguous; do not commit to a single interpretation yet.

**When PR Apollo and Builder Triaging were discussed there, without Srinivas present:**

Divakar said the previous week. Divakar's exact phrasing: "Last week on Thursday, not Thursday or Wednesday" and later "PR Apollo was discussed last week. We also discussed. Imran was mentioning about the bidder, triaging and other things, which developed by Justin was also discussed previous week."

So: the meeting in question was on **Wednesday April 22 or Thursday April 23, 2026**, the week before this Monday sync. PR Apollo and Builder Triaging were both on that agenda. Srinivas was on the invite ("you are also there in that meeting") but did not attend or did not retain the content.

---

## The scope-overlap concern, distilled

Putting it all together, the substantive overlap is:

| BayOne planned capability (Friday May 1) | Pre-existing Cisco artifact | Overlap reading |
|---|---|---|
| WebEx bot static FAQ wired to nx-os-issue-categorizer | NX-OS wiki articles already authored on GitHub | Complementary; the wiki is the source of truth Srinivas wants the static FAQ to derive from. No conflict; existing direction holds. |
| WebEx bot dynamic answer path through CAT MCP, querying NX repo at request time | CAT MCP itself is from Anupma Sehgal's side and is the intended dynamic source for care-request data; not an overlap per se. PR Apollo is the overlap risk because it independently captures PR-relevant GitHub events into MongoDB. | Partial overlap. CAT MCP gives PR-to-care-request mapping (Anupma demonstrated that all care-request data including the linked PR, branch, submitter, bug ID, SHA, and checks is available through the CAT MCP). PR Apollo gives PR event history. The two are complementary if and only if BayOne consumes both rather than recreating PR event history. |
| Build dependency graph for commits and PRs (Git-native deeper mapping) | PR Apollo (event-level mapping for PR state) plus Builder Triaging (fix-recommendation engine) | Highest overlap risk. If PR Apollo's MongoDB already has the GitHub event graph, BayOne should consume it rather than build a parallel mapping. |
| Future fix-recommendation logic on the dynamic path | Builder Triaging tool, already production-grade with 800 features run through it | Direct overlap. Anything BayOne builds that recommends a fix for a stuck PR should call Builder Triaging, not reimplement triage. |

Srinivas's framing of the resolution lens (line 423):

> "I want to make sure that the calling and teams' energy is utilized for the best, okay? Yes. And not duplicate the work. That we are doing versus they are doing. Number one, I agree. So. And at the same time, all these tools has to be coming together, so that From the user point of view, we are actually improving the experience. Number one, number two. Through the AI, we are hoping that we will move fast. That's the essential goal: productivity improvement."

Two operating principles fall out of that:

1. **Anti-duplication.** Where Cisco already has it built, BayOne should consume rather than rebuild.
2. **Single-pane integration.** All the tools (PR Apollo, CAT MCP, Builder Triaging, WebEx bot, CI/CD application chat) need to "come together" from the user's point of view. The user does not see four different tools; the user sees one assistant that knows about their PR.

Both principles are favorable to BayOne in the sense that they keep us focused on integration value rather than asking us to build duplicative infrastructure. They are unfavorable in the sense that the Friday deliverable's dynamic-path scope is now contingent on access to PR Apollo and on understanding what Builder Triaging exposes.

---

## Concrete next step (agreed in the meeting)

Justin will create a generic read-only user ID against the PR Apollo MongoDB and share it with Colin's team.

Divakar's prompt (line 488):

> "And just in you have the data, so if we could give. Read only access to the engineers. Do you have any? Maybe you can create a generic user ID and give it to them."

Justin's answer (line 493):

> "Okay. Oh, yeah. I'll check on that."

Srinivas's framing of why we need this (line 485):

> "You want to know what is its capability right now because you have an experiment, right? So that when we design the end-to-end workflow We have it."

Justin's later reconfirmation, including the broader GitHub data scope (line 1006 onward):

> "And, then the GitHub data should also contain that I have. Like once we're, yeah I'll try to get you that GitHub or we just created a new data, a MongoDB like recently last week or something. So, that should also have that data as well. Okay. Um, any yeah, whatever the GitHub is posting, we should be collecting that now."

So the deliverable from Justin is two things, possibly bundled:

1. Read-only credentials (a generic user ID) for the existing PR Apollo MongoDB.
2. Confirmation of what GitHub events are being captured and the schema.

There is no committed timeline. Justin said "I'll check on that" without a date.

---

## What the BayOne team needs to verify before Friday May 1

These are open questions that resolution of (or commitment around) before Friday's deployment would meaningfully reduce duplication risk:

1. **Does the PR Apollo MongoDB already contain enough state to back the dynamic answer path?** Specifically, can a user ask "where is my PR stuck?" and get a useful answer purely from PR Apollo's event history, with CAT MCP layered on for care-request semantics? If yes, BayOne's dynamic-path skill calls PR Apollo first, then enriches with CAT MCP. If no, BayOne adds what is missing on top.
2. **Should BayOne build the MCP layer on top of PR Apollo, or is Cisco already going to do that?** Divakar said "We are already procuring it [an MCP server on top of PR Apollo data] for you." That phrasing reads as Cisco committing to deliver the MCP, not asking BayOne to build it. Confirm.
3. **What is the call interface to Builder Triaging?** If it is being incorporated into the PR workflow as a clickable action ("the engineers can go click on it and say, 'Hey, I want my PR to go through this builder or triaging'"), is there an API or MCP we can call from the bot, or only a UI integration? If only UI, how does the bot return a fix recommendation today without invoking it programmatically?
4. **Is the planned BayOne build dependency graph for commits and PRs additive to PR Apollo, or duplicative?** Worth a direct read of Justin's MongoDB schema before Friday. The build dependency graph framing in BayOne's status table is "deeper mapping framework" beyond pattern matching, so there may be a real additive piece. We should be able to articulate it precisely after seeing what PR Apollo already has.
5. **Does Anupma's CAT MCP already give us the PR-to-CAT mapping such that no additional mapping work is needed?** Anupma's live demo in the same meeting (lines 956 onward) showed that the care-request data includes the linked PR, branch, submitter, bug ID, SHA, and checks, all available through the MCP. That answers item 4 in the v3 status table favorably; the mapping does exist. Worth re-noting because it removes one BayOne-side mapping concern entirely.

The pragmatic Friday-deliverable read: BayOne can keep moving on the static FAQ path, the WebEx bot scaffolding, and the CAT MCP integration as planned, because none of those duplicate PR Apollo or Builder Triaging. The risk concentrates on the build dependency graph and on any "show me my PRs" / "where is my PR stuck" framing. Where possible for Friday, BayOne should defer those framings or scope them to delegating to PR Apollo and Builder Triaging once read access lands.

---

## Internal-only observations

The following are for BayOne planning use, not for any Cisco-visible artifact:

- The fact that Srinivas did not know about a tool his own team built and that has 800 features run through it is a meaningful internal coordination signal. It explains some of the thrash we have been managing on the BayOne side. If Srinivas does not always have current state on his own team's artifacts going into our weekly syncs, then the right BayOne posture is to keep surfacing what Justin and Divakar tell us back to Srinivas explicitly in writing, so the asymmetry shrinks rather than grows.
- Divakar's polite jab is also a leadership tell. Divakar feels comfortable raising the missing-meetings issue directly in front of the BayOne team. That is a reasonable proxy for "Divakar has standing inside C-S-E-D" and means Divakar is a substantive ally for the BayOne integration story, not just a procurement contact. This reinforces our prior reading.
- Justin remained quiet for most of the segment and answered with the minimum needed ("This is for the CI work webex" / "Okay. Oh, yeah. I'll check on that"). That is consistent with prior reads of Justin as competent and reserved, but it also means BayOne should be careful to follow up on the "I'll check on that" in writing rather than assume the read-only access will arrive on its own.
- The "client team and kernel team and clang migration with 800 features through it" datapoint is genuinely useful sales material for future BayOne pursuits adjacent to this one (Cisco's broader build infrastructure modernization). Not for current Cisco-visible work; capture it for the BayOne portfolio catalog when this engagement closes.
