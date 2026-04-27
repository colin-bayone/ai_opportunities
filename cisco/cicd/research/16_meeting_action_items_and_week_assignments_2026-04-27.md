# 16 - Srinivas Sync: Action Items and Week Assignments

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on the actionable outputs of the meeting: deliverable document updates, BayOne technical work, Cisco-side commitments, per-team-member assignment proposals for the GitHub issue tracker Colin is standing up, and the four-blocker resolution status

---

## Purpose of this document

The Set 16 team prep call earlier today announced that GitHub issue tracking by team member starts this week. The Srinivas sync that followed both resolved the four blockers Colin came in with and introduced new directions and new commitments. This file is the operational output: every concrete item that needs to land on the GitHub tracker, against an owner, during the week of April 27 to May 1.

Items are organized into:

1. Deliverable document updates Colin owes (the prep one-pager)
2. BayOne technical work for the week
3. Cisco-side commitments and owners
4. Proposed per-BayOne-team-member GitHub issue assignments
5. Four-blocker resolution status going into the rest of the week
6. New items Set 16 introduces that were not in the prep deliverable
7. What goes into the next deliverable update

---

## 1. Deliverable document updates (the prep one-pager)

Srinivas had specific feedback on the format and content of the prep document Colin walked through. These are the edits Colin owes before the next sync.

### 1.1 Format change: nest sub-items under a single top-level bullet

Srinivas: "When you arrange that table, make sure that there will be one top level item. All the sub items will be part of that only. A single bullet... That way we know how many main items we are working versus minor items."

Colin: "Okay, yeah, no problem. I'll do that. Ironically, I actually had it that way. I just flattened it out. I didn't know if it would be too much, so I'll fix that."

**Action:** Re-nest each main work item with its sub-items as bullet children rather than flattened sibling rows. The deliverable should make the count of main items immediately countable at a glance.

**Owner:** Colin
**Target:** Tuesday or Wednesday update of the same deliverable

### 1.2 Add a "what is accomplished" section

Srinivas: "We can also add what is accomplished as well."

Colin: "Yes, of course... I'll add in that, you know, what we've accomplished, what we've delivered section as well."

**Action:** Add an explicit "Accomplished" or "Delivered" section to the prep one-pager. The "Recent closures" section already serves this in part, but Srinivas wants accomplishment language attached as its own section, framed around what BayOne has delivered (not just what items have been resolved on the Cisco-supply side).

**Owner:** Colin
**Target:** Tuesday or Wednesday update

### 1.3 Skills currently committed section

Already present in the deliverable file (`weekly_status_2026-04-27_v3_table.md`), listing all eight skills currently committed on the `skills/webex` branch of the DeepSight CI/CD repository. No additional action required other than to keep this current as more skills land.

**Owner:** Colin
**Target:** Maintain ongoing

### 1.4 Send Srinivas the dashboard link with the breakdown chart

Srinivas: "So Colin, can you send the link to this? We'll take a look."

Colin: "Of course."

**Action:** Send the dashboard link directly to Srinivas (one-to-one or in the WebEx working space). Confirm that the link surfaces the chart Colin demonstrated where the NX-OS chat questions are broken down by category and resolution status (resolved, ambiguous, unanswered).

**Owner:** Colin
**Target:** Today or Tuesday morning at the latest

### 1.5 Build and send the static-vs-dynamic intersection analysis

Srinivas asked for a further breakdown of the chart: of the unanswered questions, how many are static (deterministic, fixable from a wiki) versus dynamic (require a live database lookup against PR or job state)? He wants to glance at it to identify the highest-pain category to attack first.

Srinivas: "How many are static, meaning that information that is like what is consistent... versus depends on the dynamic information... that way we know that okay these things can be now solved through the DB."

Colin: "Do you still want that six months constraint? I actually I can just make it a toggle for you."

Srinivas: "Yeah, we just I want we want to just glance it. So that way we know where the pain points are."

**Action:** Add a static-vs-dynamic toggle to the existing breakdown chart, scoped by default to the last six months. "Static" defined per Srinivas: the question can be answered from a wiki without referencing any database (e.g., "how do I commit my code?"). "Dynamic" defined as: the question requires looking up runtime state (PR ID, job ID, build ID) against an actual database (CAT MCP, Justin's PR Apollo MongoDB, or similar).

**Owner:** Colin (with Srikar on the data side, since the categorizer feeds it)
**Target:** Tuesday or Wednesday for first cut

### 1.6 Send the WebEx bot case number and the form Colin already filled

Anupma: "Give us a case number and as well as the form that you filled, right? So we have the details."

Colin: "Sure, sure. And I can give you. Yeah, I'll give you all that so you can see exactly what we did, and it'll give all the bot specifics."

**Action:** Send Anupma the case number from the previous WebEx bot submission plus a copy of the form Colin filled out under his own ID. This becomes the template for the resubmission under DSA Atlas (also referenced as DSR Class) generic user ID.

Colin also offered an AI-generated business justification: "We're definitely not a stranger to those forms. So if you want, you know, an AI generated business justification, let us know. We can help you there."

**Owner:** Colin
**Target:** Today or Tuesday

---

## 2. BayOne technical work for the week

These are the technical work items the BayOne team owes between now and Friday May 1. Each is a candidate GitHub issue under the tracker Colin is standing up.

### 2.1 Build the static-vs-dynamic breakdown chart (last 6 months)

Already covered in 1.5 above. Implementation work belongs to the technical track even though Colin owns the deliverable side.

### 2.2 Validate the ADS environment by launching an existing app

Once the permanent ADS is provisioned (today or tomorrow per Divakar), the team picks an existing app from the Cisco team and tries to launch it on the new ADS. The point is to confirm the environment is correctly set up before BayOne starts deploying its own work onto it.

Srinivas: "One other way is once you get an ADS, pick one of the existing app and try to, let's say, launch it and see if that works. Then you know that okay, the other environment is all set."

**Owner:** Saurav and Srikar paired (since both will need ADS for their own deliverables)
**Target:** Same day ADS lands

### 2.3 Build the CICD app deployment on ADS

Srinivas: "As soon as you get the ADS server, you need to build the CICD app and try to deploy on your ADS server and see if you can bring it up."

This is the prerequisite step before any of the static FAQ wiring or dynamic CAT MCP integration can be tested end to end. The user guide and Jenkins pipeline are being committed by Srinivas's other team to the CICD repo today or tomorrow (see 3.5 below) precisely so this work does not require BayOne to figure out the deployment from scratch.

**Owner:** Srikar and Saurav
**Target:** Within 24 hours of ADS provisioning

### 2.4 Wait for and consume the user guide and Jenkins pipeline commits

Srinivas: "I asked the other team members who built the infrastructure to put some user guide into the CICD repo, so probably they'll try to do it like today, tomorrow or whenever. You can follow through. You'll see there will be some commits happening somewhere. So I asked them to do. And I asked them to basically deploy the Jenkins pipeline also for this."

**Action:** Watch the CICD repo for incoming commits from the other Cisco team this week. Pull and use them when they land. If not landed by Wednesday, flag in the WebEx working space.

**Owner:** Srikar (skills track lead)
**Target:** Pull within 24 hours of commit landing; flag if not landed by Wednesday

### 2.5 Scrape the NX-OS wiki for static FAQ source content

This is the new direction Srinivas introduced (replacing the prior framing where the chat itself was the static FAQ source). The wiki is the source of truth; the chat is the surface.

Srinivas: "For the webex spaces, the static information, what we are looking at is already part of the wiki pages created inside the GitHub NX website... we'll scrape that and we'll put it as part of static."

Divakar will share the wiki link in the WebEx space (see 3.3 below). Once shared, BayOne scrapes the wiki and uses it as the source for the static-answer skill.

Colin: "We won't commit to that for Friday just because we don't have eyes on it yet."
Srinivas: "Yeah, that's fine."

**Owner:** Srikar
**Target:** Best effort by Friday; if blocked, document the gap and propose a Tuesday-of-next-week target

### 2.6 Build the chat-to-wiki feedback loop

Colin proposed this and Srinivas accepted. When the chat surfaces a static fix that is not in the wiki, the system proposes the addition to the wiki as a GitHub issue (assuming the wiki is GitHub Pages backed, which the team will verify when the link lands). Human review gates the actual wiki update.

Colin: "If there's some chat that has a fix that is, you know, a static fix that is not surfaced in the wiki, at least propose to the wiki. I don't know what format it's in, but if it's GitHub Pages, we could even just propose it as an issue, so it can still have some human review before it gets added to the wiki."

Srinivas: "The existing questions, if you can answer it, then the feedback loop. You are right."

**Owner:** Srikar
**Target:** After wiki access lands; nice-to-have for Friday, must-have for the following week

### 2.7 Get read-only access to Justin's GitHub-event MongoDB

Justin's MongoDB stores GitHub events scraped from the NX repo. Srinivas asked Justin for a generic read-only user ID so the BayOne team can evaluate the existing data and decide whether to integrate or to build something parallel.

Srinivas: "Justin, you have the data, so if we could give read-only access to the engineers. Do you have any? Maybe you can create a generic user ID and give it to them."

Justin: "Okay. Oh, yeah. I'll check on that."

**Action on BayOne side:** Once Justin shares the credential, evaluate the schema, the freshness, and the coverage. Determine whether the planned PR-mapping work overlaps with what is already in this database. Report back to Srinivas with findings.

**Owner:** Colin to receive the credential and route; Namita is the candidate to evaluate (her log work wraps today, she pivots into dynamic answer support)
**Target:** Within 48 hours of receiving access

### 2.8 Coordinate with Anupma on the WebEx bot deployment form under DSA Atlas

Already covered in 1.6 above on the deliverable-update side. The technical-side action: Saurav rebuilds the bot to meet whatever compliance criteria arrive (still pending, see 5.3), then Anupma submits the form under DSA Atlas using Colin's prior submission as the template.

Srinivas: "And maybe Anupma, can you help on that? I mean, fill up the form."
Anupma: "Yeah, I will see what he shares right when he shares the details. But I might need your help for the business justification part and the department and all those keys, right? So we can do it together."

**Owner:** Saurav (rebuild) plus Colin (business justification copy) plus Anupma (form submission)
**Target:** Resubmission Wednesday once compliance criteria are in hand

### 2.9 Document the WebEx Bot Builder skill with all IT and policy references

Colin: "I think we finally found the policy. We'll start documenting this too. It'll make it easier for us, but I think it'll help you too. Just to have that even as part of the bot that we built like, for instance, one of the skills was the WebEx Bot Builder scope. So we can put some of these references inside, so the next person that goes to make a bot already knows about all this stuff and can build it."

**Action:** Update the `webex-bot-builder` skill on the `skills/webex` branch with the policy references, the case number from the prior submission, the compliance criteria once received, and the form template. The next bot builder should not have to rediscover the entire chain.

**Owner:** Srikar (skill author) with Saurav contributing the deployment specifics
**Target:** Friday May 1; this is part of the production-grade definition for the skill

### 2.10 Research the WebEx agentic-app capability and the proxy pattern

Srinivas introduced a long-term architectural direction during the meeting: a WebEx bot acting as a proxy to the user's CICD app running on their own ADS server. The user chats with the bot in WebEx; the bot relays messages to the user's CICD app on ADS; the app uses the user's LLM credentials and MCP backends; responses stream back to the bot and the user's WebEx space. Effectively a remote-control pattern over WebEx.

Srinivas: "When I chat through my WebEx on my phone, I should be able to send the same message to my app running on my ADS server. That essentially means if I run a webex agent on this app also, whenever this app is launched, I should be able to send a message from my workspace to my own ADS server, which has access to all LLM, everything running."

Colin: "So it's essentially like a proxy connection."
Srinivas: "It's a proxy exactly."

Colin volunteered that the team had already started looking into the WebEx agentic capability and that WebEx now supports agentic apps with language model integrations.

**Action:** Pull together everything BayOne has found on the WebEx agentic-app capability. Share the documentation references with Srinivas. Sketch the proxy architecture and identify what would be required to build it (the WebEx agent on the bot side, the listening endpoint on the ADS-app side, the message routing, and authentication).

**Owner:** Srikar (skill ownership) with Saurav (bot architecture) and Colin (share-out to Srinivas)
**Target:** Best effort this week as research; not a Friday deliverable

### 2.11 Look into Claude Code's "remote control" pattern for analog

Colin: "I don't think it's there yet for Codex. I know that it's there for Claude Code because we do this at BayOne. But there's something now for Claude Code that's essentially called remote control that does exactly this natively."

(Transcript renders "Claude Code" as "Cloud Code." Same thing.)

**Action:** Document the Claude Code remote-control pattern as a reference architecture. Note where the Codex roadmap may eventually catch up. Share the pattern with Srinivas as a forward-looking benchmark.

**Owner:** Colin
**Target:** This week, low priority

### 2.12 Coordinate with Justin on the Basel MCP timeline

Justin is working on a Basel (BSL) MCP. Srinivas asked Justin to find out the timeline today.

Srinivas: "Justin, when do we have this Basel MCP? Are we working on it like to build?"
Justin: "Yes, yeah, we're working on a few of them... I can uh, I'll get more. I'll find out today."

Srinivas (to Colin): "Colin, can you talk to Justin and get the other PR... we'll find out what is there actually."

**Action:** Colin chases Justin for the Basel MCP status and surfaces the answer to Srinivas. The Basel scope is deferred for this week, but the Basel MCP is the gating piece for extending the bot to Basel after CICD/NX-OS work is complete (see 6.4 below).

**Owner:** Colin
**Target:** End of day Monday or Tuesday morning

---

## 3. Cisco-side commitments

These are commitments Cisco-side participants made during the meeting. Each needs tracking on the GitHub tracker so the BayOne team can flag if they slip and so Friday's deliverable risk is appropriately attributed.

### 3.1 Divakar: retire 4-5 underused VMs and procure 2 new ADS machines

Divakar: "I think we procured about four or five different VMs last time. Can I retire them?... Retire them and I'll procure a couple of additional machines for the engineers here."

Specs: 16-core CPU, 32 GB RAM (the maximum Divakar can provision), 100 GB local storage, no backup.

**Owner:** Divakar
**Target:** New machines today or this week; "by today evening mostly other things are to be taken care of. So it will take a day or probably we'll see. It might be early. I cannot guarantee."

### 3.2 Divakar: leave one CN-SJC-STANDALONE bundle machine available immediately

Divakar: "I am leaving one machine for you. You can use that machine for next one week. When the other machines come up, I'll give it to you, but I've got to leave the one machine for you."

This is the immediate-use fallback while the new procurement runs. The team is unblocked starting today on the existing CN-SJC-STANDALONE bundle machine.

**Owner:** Divakar
**Target:** Today (already in motion)

### 3.3 Divakar: share the NX-OS wiki link in the WebEx space

Divakar: "I just send you that link as well... I will do. There is a nice wiki."

This is the single-source-of-truth wiki Srinivas wants the static FAQ scraped from. Without the link, BayOne cannot start the wiki scrape (see 2.5 above).

**Owner:** Divakar
**Target:** Today

### 3.4 Anand: verify CN-SJC-STANDALONE bundle membership for the team

Divakar: "Make sure that they're part of our bundle, CN-SJC-STANDALONE bundle. That one I think is already part of as far as you know. Just (Anand) can help with that one."

**Owner:** Anand
**Target:** Today

### 3.5 Srinivas: ask the other team to commit user guide to the CICD repo

Already referenced in 2.4. Srinivas committed to the ask in the meeting. The other team commits the user guide to the CICD repo today or tomorrow.

**Owner:** Srinivas (to make the ask) and the other team (to deliver)
**Target:** Today or Tuesday

### 3.6 Srinivas: ask the other team to deploy the Jenkins pipeline

Same pattern as 3.5. Srinivas committed to ask the other team to deploy the Jenkins pipeline so the BayOne team does not have to figure out deployment from scratch.

**Owner:** Srinivas (to make the ask) and the other team (to deliver)
**Target:** This week

### 3.7 Justin: create a read-only generic user ID for the GitHub-event MongoDB

Already referenced in 2.7.

**Owner:** Justin
**Target:** This week ("Okay. Oh, yeah. I'll check on that.")

### 3.8 Justin: find out the Basel MCP timeline today

Already referenced in 2.12.

**Owner:** Justin
**Target:** Today

### 3.9 Anupma: fill the WebEx bot deployment form under DSA Atlas

Already referenced in 1.6 and 2.8. Anupma owns the form submission once Colin sends the case number, the prior form, and (with Colin's help) the business justification, and once Saurav has rebuilt the bot to compliance criteria.

**Owner:** Anupma
**Target:** Wednesday resubmission target

---

## 4. Per-BayOne-team-member assignment proposals

These are the proposed GitHub issue assignments for the tracker Colin is standing up. Grounded in the two-track structure the prep call established: Srikar on skills/WebEx, Saurav on bot, Namita on logs (transitioning to dynamic answer path), Colin on coordination.

### 4.1 Colin (coordination, deliverable, external interfaces)

- Update the prep one-pager: nest sub-items under top-level bullets, add the accomplished section (1.1, 1.2)
- Send Srinivas the dashboard link with the breakdown chart (1.4)
- Build and send the static-vs-dynamic intersection analysis with toggle (1.5, 2.1)
- Send Anupma the WebEx bot case number, prior form, and AI-generated business justification (1.6, 2.8)
- Coordinate with Justin on the Basel MCP timeline (2.12)
- Coordinate with Justin on the GitHub-event MongoDB read-only access (2.7)
- Share BayOne's findings on the WebEx agentic capability with Srinivas (2.10)
- Document the Claude Code remote-control pattern as reference (2.11)
- Stand up the GitHub issue tracker (announced on the prep call this morning)
- Maintain the "be annoying" cadence in the WebEx working space (committed on the prep call)

### 4.2 Srikar (skills track, static FAQ wiring, WebEx agentic research)

- Pull the user guide and Jenkins pipeline commits from the CICD repo when the other team lands them (2.4)
- Build the CICD app deployment on ADS once permanent ADS is up (2.3)
- Validate the ADS environment by launching an existing Cisco app (2.2; paired with Saurav)
- Scrape the NX-OS wiki for static FAQ source content once Divakar shares the link (2.5)
- Build the chat-to-wiki feedback loop (propose chat-found static answers as GitHub issues against the wiki) (2.6)
- Document the WebEx Bot Builder skill with policy references, case number, compliance criteria, and form template (2.9)
- Research the WebEx agentic-app capability and sketch the proxy architecture (2.10)
- Continue maintenance on the existing eight skills on the `skills/webex` branch
- Static-vs-dynamic categorization on the unanswered chat questions (data side of 1.5 and 2.1)

### 4.3 Saurav (WebEx track, bot rebuild, deployment)

- Rebuild the WebEx bot to meet compliance criteria once received (gating on Cisco-side criteria delivery, see 5.3)
- Resubmit the bot under DSA Atlas with Anupma; provide bot specifics for the form (2.8)
- Validate the ADS environment by launching an existing Cisco app (2.2; paired with Srikar)
- Build the CICD app deployment on ADS once permanent ADS is up (2.3; paired with Srikar)
- Assist with the WebEx agentic / proxy pattern research given his bot expertise (2.10)
- Contribute deployment specifics to the WebEx Bot Builder skill documentation (2.9)

### 4.4 Namita (logs track wrapping; pivot to dynamic answer path)

- Wrap up the PR commit attribution research today (carryover from Set 16 prep call commitment)
- Pivot to the CAT MCP / dynamic answer path support
- Once Justin's MongoDB read-only access lands, evaluate schema, freshness, coverage; report on overlap between BayOne's planned PR-mapping work and the existing PR Apollo data (2.7)
- Help Srikar with the static-vs-dynamic categorization data slice (1.5, 2.1) if capacity allows

### 4.5 General team

- Use the `skills/webex` branch on the CICD repo as the working location for skills in development (closed in Set 16; promote to SME KB only when production-grade)
- File issues against the new GitHub tracker for any blocker that arises from the Cisco side; chase via the WebEx working space
- Maintain the start-of-day and end-of-day cadence in the WebEx working space (paper trail discipline)

---

## 5. Four-blocker resolution status going into the rest of the week

Status of each of the four (now five) blockers Colin came in with from the prep deliverable, after the Srinivas sync.

### 5.1 Blocker 1: Permanent ADS availability — RESOLVED today/tomorrow

Divakar committed to retire 4-5 underused VMs and procure 2 new 16-core/32GB ADS machines. One existing CN-SJC-STANDALONE bundle machine is left available for the team to use immediately starting today. The new procurement is targeted for "today evening mostly... it will take a day or probably we'll see."

**Status:** Resolved. Immediate-use machine available today; new ADS machines today or tomorrow. Risk: Divakar's "I cannot guarantee" caveat.

**Path forward:** Saurav and Srikar pick the machine up today, validate the environment by launching an existing app, then start CICD app deployment.

### 5.2 Blocker 2: Language model access path — PATH CLARIFIED

Srinivas confirmed the path: ADS provisions the machine, DeepSight runs on top of ADS, users register their credentials on the DeepSight platform, and the platform handles the `.env` file automatically. No manual credential management.

Models available on DeepSight: Copilot, Codex. Cursor and others to be added later.

Srinivas: "That is on the DeepSight. Will automatically take care. You don't have to worry. That is an example he has given... if once you are stuck, we'll tell you how to move forward."

**Status:** Resolved at the architectural level. Operational confirmation pending the actual ADS provisioning and DeepSight deployment.

**Path forward:** Once ADS is up, deploy DeepSight, register team member credentials on the platform, deploy the CICD app, confirm `.env` handling works as described. If stuck, escalate to Srinivas.

### 5.3 Blocker 3: WebEx bot deployment infrastructure — IDENTITY RESOLVED, COMPLIANCE CRITERIA STILL OPEN

Two sub-blockers were tracked in the prep deliverable. They resolve at different rates.

#### 5.3.1 Identity: RESOLVED

Srinivas asked Anupma whether to create a CICD-specific generic user ID. Anupma argued for reuse of the existing DSA Atlas (also referred to as DSR Class) generic user ID since (a) creating new generic user IDs requires a separate approval process, and (b) the application name is sufficient for audit-trail purposes when overlaid on a shared generic user ID.

Srinivas: "We have one generic user entity called DSR Class. So can you tell what you guys have done? And maybe me or Anupma will fill it up."

The bot will deploy under the DSA Atlas generic user ID.

**Status:** Resolved.

#### 5.3.2 Compliance criteria: STILL OPEN

The compliance non-compliance email arrived this morning (April 27) from IT. The email flagged the bot as non-compliant but did not provide the criteria. BayOne cannot rebuild the bot to meet criteria it has not received.

**Status:** Still open. Resubmission expected Wednesday once criteria are in hand.

**Path forward:**
- Cisco IT to provide compliance criteria (path not specified in the meeting; presumably back through Mahaveer Jinka who was on CC for the original case)
- Saurav rebuilds the bot to meet criteria once received
- Colin sends Anupma the case number, prior form, and AI-generated business justification
- Anupma submits the form under DSA Atlas (Wednesday target)
- Audit and approval window is outside BayOne control; prior turnaround was over a week, so Friday May 1 deployment of the bot is at structural risk independent of BayOne's work

### 5.4 Blocker 4: CAT MCP querying / PR-to-CAT mapping — RESOLVED

Anupma walked Colin through a live cache request page. The cache request structure already contains the PR mapping plus rich metadata: branch, submitter, bug ID, SHA, all the checks. Plus Justin confirmed the new MongoDB they recently created captures the same GitHub events.

Anupma: "Cat ID should already have the PR mapping in it... All the data should be available through the MCP as well."

Colin: "No, that's great. That's great. Okay, question answered. Thank you. That's really nice."

**Status:** Resolved. The mapping exists and is queryable via the existing cache request infrastructure.

**Path forward:** No further mapping work required. The dynamic-answer skill can use the existing CAT MCP plus the cache request data without BayOne building a custom mapping table.

### 5.5 Blocker 5: Skills repository destination — CONFIRMED

Colin presented the working approach (CICD repo `skills/webex` branch during dev, promote to SME KB once production grade) that the team agreed on in the prep call.

Srinivas: "For now keep it here, and whenever you see okay some skills are ready, then it could be deployed by anyone. Then put it to the SME KB."

**Status:** Confirmed.

**Path forward:** Continue committing to `skills/webex` during development. Define a "production grade" gate (likely: documented, tested, deployed at least once in CICD context). Promote individual skills to SME KB as they pass the gate.

---

## 6. New items Set 16 introduces (not in the prep deliverable)

These directions did not exist in the prep one-pager. The next deliverable update needs to incorporate them.

### 6.1 PR Apollo and Justin's MongoDB

Divakar surfaced this mid-meeting: "We have another one, right? I think I discussed this with you in Shiva's meeting time. The PR Apollo, where we have the entire database going in. I think we have the database available."

Justin's GitHub-event MongoDB stores everything from the GitHub events feed and is intended to drive PR insights for engineers ("show me all my PRs," with stuck-state, possible fixes, builder triaging integration).

**Implication for BayOne:** Need to evaluate whether the planned PR-mapping work overlaps. Read-only access from Justin is the gating step (see 2.7).

### 6.2 Builder Triaging tool

Divakar: "We are incorporating the builder triaging, right? We have just enrolled the builder triaging, which is being used for the clang migration. It's being used for different different projects. That one we are incorporating into the PR as well... they converted about 800 features. They put it through the tool."

**Implication for BayOne:** Same overlap question as PR Apollo. The Builder Triaging tool is providing possible-fix suggestions based on official builds and historical migration data. BayOne's chat-based assistance work needs to coordinate rather than duplicate.

### 6.3 WebEx agentic proxy long-term architecture

The proxy pattern Srinivas described in section 2.10 is a new long-term architectural direction. Not a Friday deliverable; a research direction. The bot becomes a proxy to the user's CICD app on their own ADS server, with the user's LLM credentials and MCP backends doing the heavy lifting.

**Implication for BayOne:** Add this as a research workstream. Sketch the architecture, document the WebEx agentic-app capability, identify any gaps versus the Claude Code remote-control pattern.

### 6.4 Basel scope deferred; Basel MCP pending

Srinivas: "What we can do is let them finish this week. They have that to be deployed for CICD workflow. And once that end-to-end is done, we can just replicate for the other services."

Basel (BSL) is deferred for this week. After CICD/NX-OS deployment lands, the bot pattern extends to the Basel team's WebEx space (350 engineers per Divakar). The Basel MCP (Justin's work, 2.12) is the gating piece for that extension.

### 6.5 Wiki as static FAQ source

This changes the data source for the static FAQ workstream. Previously, the prep one-pager framed the static FAQ as derived from the chat itself via the categorizer skill. Set 16 reframes it: the wiki is the source of truth, the chat is the surface, the categorizer feeds an intersection analysis (which questions are answered in the wiki versus which are not), and the chat-to-wiki feedback loop closes the gap.

### 6.6 Last-six-months data slice constraint

Anupma: "I would suggest like do it for last six months, because anything previously, like lot of things were changing. So... get data for all of it."

The breakdown chart and the static-vs-dynamic intersection analysis should default to a six-month window. Colin agreed and committed to making it a toggle.

---

## 7. What goes into the next deliverable update

The next deliverable update (Tuesday prep, or Wednesday update, or the Friday wrap depending on cadence chosen) needs to reflect the following.

### 7.1 Format change

Re-nest sub-items under single top-level bullets per Srinivas's request (1.1).

### 7.2 New "Accomplished" section

Frame BayOne's deliverables to date as accomplishments alongside the Recent closures section (1.2).

### 7.3 Recent closures additions

- Permanent ADS provisioning resolved (immediate-use machine plus 2 new ADS machines in flight)
- Language model access path clarified (ADS to DeepSight to user-registered credentials, automatic `.env`, Copilot and Codex available)
- CAT MCP PR mapping resolved (cache request structure has the mapping plus rich metadata)
- WebEx bot deployment identity resolved (DSA Atlas / DSR Class generic user ID)
- Skills repository destination confirmed (CICD `skills/webex` during dev, SME KB on production grade)
- NX-OS wiki identified as static FAQ source of truth

### 7.4 Open items remaining

- WebEx bot compliance criteria from Cisco IT (Wednesday resubmission target)
- New ADS machines fully provisioned (Divakar tracking)
- User guide and Jenkins pipeline commits in CICD repo from Srinivas's other team
- Justin's MongoDB read-only access
- Justin's Basel MCP timeline
- Divakar's NX-OS wiki link in the WebEx space

### 7.5 New directions

- PR Apollo and Justin's MongoDB (overlap evaluation pending)
- Builder Triaging tool (overlap evaluation pending)
- WebEx agentic proxy architecture as long-term direction
- Basel extension deferred until CICD/NX-OS lands; Basel MCP gating
- Chat-to-wiki feedback loop as a near-term workstream
- Last-six-months data slice constraint applied to dashboards

### 7.6 Skills currently committed

Maintain the existing list of eight skills on `skills/webex`. Add any new skills as they land.

### 7.7 Friday May 1 deployment target

Confirm that the target remains intact: the CICD app composition (static FAQ wiring plus dynamic CAT MCP integration) deploys via the WebEx bot (subject to bot compliance approval, which is the principal residual risk to the Friday timeline).

---

## Cross-references

- Prep deliverable Colin walked through: `cisco/cicd/deliverables/weekly_status_2026-04-27_v3_table.md`
- Set 16 team prep call summary: `cisco/cicd/team/research/16_summary_2026-04-27.md`
- Prep call blocker rehearsal: `cisco/cicd/team/research/16_prep_blockers_for_srinivas_meeting_2026-04-27.md`
- Prep call week deliverables and communication strategy: `cisco/cicd/team/research/16_prep_week_deliverables_and_communication_strategy_2026-04-27.md`
- Prep call skills repository decision: `cisco/cicd/team/research/16_prep_skills_repository_decision_2026-04-27.md`
- Prep call CAT MCP status: `cisco/cicd/team/research/16_prep_cat_mcp_status_and_pr_mapping_gap_2026-04-27.md`
