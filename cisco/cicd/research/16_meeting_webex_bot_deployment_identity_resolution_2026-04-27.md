# 16 - Srinivas Sync: WebEx Bot Deployment Identity Resolution

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on the WebEx bot deployment identity decision (DSA Atlas / DSR Class generic user) and the form-filling handoff to Anupma; closes Blocker 3 of the prep deliverable at the identity level

---

## 1. Why this exchange happened

Colin entered the Monday sync with a prepped one-pager (weekly_status_2026-04-27_v3_table.md). Critical path blocker number three on that one-pager was "WebEx bot deployment infrastructure," which had a sub-caveat written as follows:

> Caveat on the deployment ID: BayOne can deploy the bot under one of our Cisco-issued user IDs to meet the Friday timeline. The proper pattern would be a service account or centralized deployment ID if one is available, since deployment under a personal user account ties the bot's lifecycle to that individual. Flagging as a caveat, not a blocker.

BayOne's prepared position was that a service account or centralized deployment ID is the right pattern, with a personal user ID as a fallback only to keep the Friday timeline. The team needed Cisco to either confirm a service account / centralized deployment ID was available, or accept the personal user ID fallback.

The exchange below resolves this at the identity level by landing on an existing generic user ID (DSA Atlas, also referred to as DSR Class) that Anupma will submit the bot deployment form under, on BayOne's behalf.

---

## 2. How Colin opened the issue

Colin walked through the prep one-pager top-to-bottom. When he arrived at the WebEx bot deployment row, he framed the situation as a prior attempt that had been blocked by Cisco IT's compliance gate:

> we did previously try to do the WebEx spot to play, And we tried to do it the same way we would if it was on an ADS machine on the temp ADS. Uh, what happened was that uh. I T had flagged it and said that there is an approval process for WebEx spots. So we went through, we filled out the form. You have to provide justification, clarification on the purpose and intent and you know functionality. Um. It got flagged to us. I think. Sorry, correct me if I'm wrong, That was just on last Friday or maybe even today. That, we finally got a response back from IT about the state of the bot, and that was. Do you. Have The case number?

Key facts Colin established:

- BayOne previously attempted to stand up the WebEx bot using the Temporary ADS approach (the same way they would deploy any application on an ADS machine).
- Cisco IT intercepted that attempt and informed BayOne that WebEx bot deployments are subject to a separate approval process.
- BayOne completed the WebEx bot approval form, providing justification, clarification on purpose, intent, and functionality.
- IT flagged the submission with a non-compliance response. The response was received "last Friday or maybe even today" (i.e., approximately April 24 or April 27).
- Colin had a case number for the existing IT ticket and offered to share it.

---

## 3. Srinivas's framing question: under whose user ID?

Srinivas immediately reframed the problem as a deployment identity question:

> So is it will it be deployed as a user ID one of your user ID? So we need to do it on behalf of you.

This is the key Cisco-side framing. Srinivas was not asking about the compliance criteria (the substance of why the bot was flagged) — he was asking about the identity under which the bot would run. The implicit position: WebEx bots in this Cisco environment are deployed under user IDs, and someone on the Cisco side would need to do that on BayOne's behalf if the bot is not to be tied to a BayOne contractor's personal ID.

---

## 4. Colin's response: service account preferred, but flexible on identity

Colin matched Srinivas's framing and surfaced BayOne's prepared position:

> we we were flagging it as it's probably best to deploy it as someone else just for continuity sake. Um, and usually for us we've done it as like a service account. But depending upon what the preference is here, we would just need to know what deployment ID we should use, and we can provide the case number for it too.

Three things Colin communicated here:

1. BayOne's preference is to deploy under a non-personal identity for continuity (so the bot's lifecycle does not depend on any one contractor remaining on the engagement).
2. BayOne's normal pattern in other engagements is a service account.
3. BayOne is flexible. They will use whatever deployment ID Cisco prefers, and they will hand over the existing case number to support the resubmission.

---

## 5. Srinivas turns to Anupma: can we create a generic user ID?

Srinivas turned to Anupma Sehgal (and briefly Justin Joseph) to ask about creating a generic user ID for the CICD engagement:

> So Anvoma, Can we create one or just in one of you create a like a generic user ID. Or the can we create like a like a. This will be a detailed.

The intent was to provision a fresh generic (i.e., service-account-style) user ID specifically for the CICD WebEx bot.

---

## 6. Anupma's pushback: existing generic user IDs already exist

Anupma's response steered Srinivas away from creating a new generic user ID and toward reusing one that already existed:

> We already have generic user. Like it's here. Like how to say, we already have one in D R settlers. We have uh, Yes, doc review, code review. So we do have three or four days.

Decoded against the established context, Anupma is saying:

- A generic user ID already exists in the relevant area (the speech-to-text rendered "D R settlers" — most likely a transcription artifact for the same generic user ID Srinivas later names "DSR class" / "DSA atlas").
- Existing generic user IDs cover use cases like "doc review" and "code review."
- There are roughly three or four such generic user IDs already provisioned (the transcript renders "three or four days" — a near-certain transcription error for "three or four IDs").

The implied argument: rather than spin up a brand-new generic user ID for this bot, lean on the inventory of generic IDs that already exists.

---

## 7. Srinivas's audit-trail counter-argument

Srinivas pushed back on the "reuse an existing generic ID" pattern with an audit-trail concern:

> Can We have separate DSCICD? That way, see the problem is if you overlay the same generic user ID. Then we don't have audit trail to say something happens. How do you know which of the three application caused the issue? Because you are using the same.

Srinivas's concern: if multiple applications all run under the same generic user ID, an incident under that identity is ambiguous — you cannot distinguish which of the three (or four) overlaid applications was the cause. He proposed a CICD-specific generic ID ("DSCICD") to keep the audit trail per-application.

He gave a concrete example a moment later:

> we have a specific uh what you call app name and specific purpose that drives the outcome, right. So I don't want to see if we can overlay is hard. For example, when the bug sentinel we are using DS Atlas. I would rather have a separate one, because if that guy is making some mistake, he's running the CI pipeline. And if that is making some mistake, I want to under fix that piece, not someone else. And some other because there is if they use the same generic user ID running in different pipelines. It's very hard to debug anything.

The example reveals two pieces of inventory:

- The bug sentinel application currently runs under the generic user ID "DS Atlas."
- The CI pipeline is the application Srinivas is worried about overlaying onto the same identity.

Srinivas's preference at this stage: separate generic user per application so that misbehavior can be attributed cleanly.

---

## 8. Anupma's pushback on proliferation

Anupma did not agree:

> having too many generic user IDs gets out of hands, right? Like then also it becomes confusing that which one you are using for what purpose.

Her counter-concern was operational: too many generic IDs creates its own confusion — knowing which ID corresponds to which purpose becomes harder, not easier, as the count grows.

She also flagged the provisioning cost:

> I would say creating is not difficult. We have done in the past, right? But getting all the generic user IDs like setup for everything. Is a like process, right? We have to make sure. Yes, and then getting any approvals needed for any groups. So we did set up the previous ones right consciously for this purpose.

Decoded:

- Creating a generic user ID is technically not hard.
- Setting one up "for everything" — i.e., getting it provisioned across all the systems and groups it needs access to, plus any required approvals — is a process, not a quick step.
- The previously created generic IDs were each set up "consciously for this purpose," meaning each existing generic ID was built deliberately for a specific use case and already has the right access plumbing.

The implication: standing up a new DSCICD-specific generic user ID would require running the full provisioning + approval process again, when an already-provisioned generic ID could be repurposed.

---

## 9. Srinivas concedes: app-name-based tracking is sufficient

Srinivas worked through the trade-off and conceded:

> So you're basically not sending me the same generic user ID, but since it is based on the application, we should be able to track it. For example, CACD you are saying. Yeah. Yeah. Okay, that makes sense. So then we have a DS Atlas. You can use that itself if you want. Yeah. I mean, if you think we can leverage that on purpose.

The reasoning he settled on:

- His original objection assumed that "same generic user ID across multiple applications" meant no per-application audit trail.
- Anupma's point reframed it: the audit trail does not need to come from the user ID. The applications themselves have distinct app names and distinct purposes. Per-application attribution can be done via the app name, not the identity.
- Therefore reusing the existing DS Atlas generic user ID is acceptable for the CICD WebEx bot.

Anupma reinforced the "save the form-filling burden for the future" angle:

> because you know that later on we'll have to get the for the codex, right? The generic user ID there. Also, we have to fill up a full big form, providing all the providing all these uh. Details. Justification and yeah.

Decoded: the Codex (Copilot Codex) deployment will itself require a generic user ID later, and that will involve another full form submission with full justification details. Burning cycles standing up a separate CICD-only generic user now would multiply that form-filling burden unnecessarily.

---

## 10. The decision

Srinivas summarized and committed:

> we have one generic user entity called DSR class. So can you tell what you guys have done? And maybe me or Anupama will fill it up. Will help you guys solve this problem.

And immediately after Colin agreed:

> Just let us know so that then we will deploy it as a DSA atlas itself as a generic use already.

> And maybe Anupama, can you help on that? I mean, fill up the form.

The decision, made jointly by Srinivas and Anupma:

- The WebEx bot will be deployed under the existing generic user ID, named in this conversation as both "DSR class" and "DSA atlas." Both names refer to the same generic user identity. The canonical form to use going forward is **DSA Atlas (also referred to as DSR Class)**, and Cisco-side confirmation of the exact spelling can come back through the engagement chat.
- No new generic user ID will be created for the CICD engagement. The Cisco audit-trail concern is resolved by application-name attribution rather than per-application identity separation.
- Srinivas or Anupma (Anupma confirmed) will fill out the WebEx bot deployment form on BayOne's behalf, submitting under the DSA Atlas generic user ID rather than under any BayOne contractor's personal Cisco-issued user ID.

---

## 11. The handoff

Anupma defined what BayOne needs to send for the form-filling step:

> Give us a case number and as well as the form that you filled, right? So we have the details.

Colin committed to send:

- The IT case number from the existing flagged submission.
- The WebEx bot deployment form Colin already filled under his personal Cisco-issued user ID, including all bot specifics (name, scopes, justification, purpose, intent, functionality).

Colin's commitment in his words:

> I'll give you all that so you can see exactly what we did, and it'll give all the bot specifics.

Anupma then explained the form-filling pattern she will follow:

> But if you see the steps that they already those steps right with your ID. So that we can repeat the same with the generic user ID and submit.

Decoded: she will replicate Colin's already-filled form, swapping the deploying identity from Colin's personal user ID to the DSA Atlas generic user ID, and submit. She also noted she may need Colin's help on specific form fields:

> for the form, and because I might need your help for the. The business justification part and the department and all those keys, right? So we can do it together.

The collaboration shape: Anupma drives the submission under the generic user ID. Colin supplies the prior submission as a template, plus subject matter input on business justification and department fields where Anupma is not the right author.

---

## 12. Colin's AI-generated business justification offer

Colin layered an additional offer on top of the handoff:

> if you want, I mean, too, we I'll put it this way: we're definitely not a stranger to those forms. So if you want, uh you know an AI generated business justification, let us know. We can help you there. If that's something that saves you some time. Yeah. Usually the people that are reviewing are also using AI, so we can kind of. We know how to do that.

Colin positioned this as a time-saver: BayOne's AI practice routinely generates business justifications for forms of this kind, and given that reviewers themselves use AI tools, BayOne can produce justification text shaped for that review pattern. Anupma's response circled back to wanting Colin's already-filled form first (so she has the literal precedent to work from), but did not decline the AI-generated justification offer.

---

## 13. Codex generic user ID — already flagged for the future

Anupma surfaced a forward-looking item that is not in scope this week but is on the radar:

> because you know that later on we'll have to get the for the codex, right? The generic user ID there. Also, we have to fill up a full big form, providing all the providing all these uh. Details. Justification and yeah.

Translation:

- The Codex (Copilot Codex) deployment, when it happens, will itself need a generic user ID.
- That generic user ID will require another full form submission with full justification.
- This is a known upcoming form-filling cycle that the team should plan for, separate from the WebEx bot form being submitted now.

This belongs in the engagement's forward-looking deployment-infrastructure tracker.

---

## 14. WebEx Bot Builder skill — process documentation commitment

Colin made a side commitment that turns the form-filling experience into a reusable asset:

> I think we finally found the policy. Ah, we'll we'll start documenting this too. It'll make it easier for us, but I think it'll help you too. Um, Just to have that ah even as part of the bot that we built like, for instance, one of the skills was Theum, the Webex BotBuilder scope. So we can put some of these references inside, So the next person that goes to make a bot already knows about all this stuff and can build it.

The commitment:

- BayOne has now found the underlying Cisco policy governing WebEx bot deployment.
- That policy, plus the form, plus the case-number trail, plus the generic-user-ID pattern landed on in this meeting, will be documented inside the existing **webex-bot-builder** skill (one of the eight skills currently committed on the `skills/webex` branch — see prep one-pager Skills currently committed section).
- The intended outcome: the next person on either side (BayOne or Cisco) who needs to deploy a WebEx bot in this environment has the full reference material baked into the skill, so they do not retrace the same discovery.

This converts a one-time blocker resolution into ongoing engagement value.

---

## 15. What this resolves on the prep one-pager

Mapped against Critical path blockers and clarifications needed item 3 ("WebEx bot deployment infrastructure") in weekly_status_2026-04-27_v3_table.md:

| Sub-item from prep one-pager | Status after this exchange |
|---|---|
| Caveat on the deployment ID (service account / centralized deployment ID preferred over personal user ID) | **Resolved.** Bot will deploy under DSA Atlas generic user ID, owned by Cisco-side, not under any BayOne personal user ID. Anupma submits the form. |
| WebEx bot compliance criteria question (the substance of why the original submission was flagged) | **Still pending.** This exchange did not surface the actual compliance criteria text from Cisco IT. The path to obtain it remains: BayOne sends Anupma the case number and the existing form; Cisco-side review of what IT flagged is implicit in Anupma's resubmission, but no compliance criteria document has been promised or shared. |
| Friday expectation for the WebEx bot given audit and approval timing | **Still pending.** Approval turnaround was previously more than a week. Resubmission timing now depends on Anupma getting the case number and form from Colin, then submitting under DSA Atlas. Friday delivery of the deployed bot remains gated on Cisco IT approval timing, which is outside BayOne's control. |

In one sentence: **the identity question is resolved (DSA Atlas generic user); the compliance question and the approval-timing question remain open and depend on Cisco IT's response cycle.**

---

## 16. Action items captured from this exchange

| # | Owner | Action | Due / Trigger |
|---|---|---|---|
| 1 | Colin (BayOne) | Send Anupma the IT case number for the original flagged WebEx bot submission | ASAP this week |
| 2 | Colin (BayOne) | Send Anupma the completed WebEx bot deployment form Colin originally submitted under his personal Cisco-issued user ID, including all bot specifics (name, scopes, justification, purpose, intent, functionality) | ASAP this week |
| 3 | Anupma (Cisco) | Replicate Colin's submission with DSA Atlas (DSR Class) as the deploying identity and submit the WebEx bot deployment form on BayOne's behalf | After receiving items 1 and 2 from Colin |
| 4 | Colin (BayOne) | Optionally provide an AI-generated business justification for Anupma's submission to save her time | If Anupma signals she wants it |
| 5 | Anupma + Colin | Co-fill the business justification, department, and similar fields where Colin's input is needed | During Anupma's form preparation |
| 6 | Colin (BayOne) | Document the WebEx bot deployment policy, form contents, case-number trail, and generic-user-ID pattern inside the webex-bot-builder skill on the `skills/webex` branch of the DeepSight CICD repository | This week and ongoing |
| 7 | Cisco-side (forward-looking) | Plan for a separate, similarly large form submission to provision a generic user ID for the Codex (Copilot Codex) deployment when that work begins | Tracked as upcoming, not this week |
| 8 | Cisco-side | Provide the actual WebEx bot compliance criteria text that flagged the original submission, so the resubmission addresses the underlying non-compliance and not just the identity question | Still open |

---

## 17. Glossary of names used in this exchange

The transcript renders the same generic user ID under multiple variants. They all refer to one identity:

| Transcript rendering | Canonical |
|---|---|
| "D R settlers" | DSA Atlas / DSR Class (same generic user ID) |
| "DS Atlas" | DSA Atlas / DSR Class (same generic user ID) |
| "DSA atlas" | DSA Atlas / DSR Class (same generic user ID) |
| "DSR class" | DSA Atlas / DSR Class (same generic user ID) |

Recommended canonical form for downstream documents: **DSA Atlas (also referred to as DSR Class)**. Cisco-side spelling confirmation can come through the engagement chat as part of the case-number / form handoff in action item 1.

Other generic user IDs Anupma named or referenced as already existing:

- Doc review (existing generic user ID, separate from DSA Atlas)
- Code review (existing generic user ID, separate from DSA Atlas)
- The bug sentinel application currently runs under DSA Atlas (per Srinivas)
- "Three or four" total generic user IDs in inventory (per Anupma)

The CICD WebEx bot will overlay onto DSA Atlas alongside the bug sentinel, with per-application attribution coming from the app name rather than from a separate identity.
