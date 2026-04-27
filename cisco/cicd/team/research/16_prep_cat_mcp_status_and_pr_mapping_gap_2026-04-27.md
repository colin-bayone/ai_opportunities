# 16 - Team Prep Call: CAT MCP Status and PR-to-CAT ID Mapping Gap

**Source:** /cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/cicd-team-monday-pre-meeting_01_formatted.txt
**Source Date:** 2026-04-27 (Monday team pre-meeting, 15:15-15:45 PST, 75 minutes before the 1pm Srinivas sync)
**Document Set:** 16 (BayOne team prep call before the Monday Srinivas meeting)
**Pass:** Focused deep dive on Srikar's CAT MCP research findings, the PR-to-CAT ID mapping gap, and the mid-call skill commits

---

## 1. Setup: Colin Frames the CAT MCP as One of the Two Halves of the Friday Deliverable

Before Srikar reports anything, Colin lays out the structure of the CI/CD application deployment that is due Friday. He explicitly splits it into two parts that the WebEx bot has to handle:

- **Static side (the FAQ/known-answer half).** Colin: "What Cerny Bus wants from this is an FAQ bot, effectively. So when someone asks a question in that chat, if that question has already been answered in the past, or if there's some deterministic easy answer for it. we would give that answer back. Now the static part, the mapping is right there." This is the output of the categorizer skill that has already run over the historical data.
- **Dynamic side (the live CAT MCP query half).** Colin: "The second part of it is the more dynamic mapping, so to query using that Cat MCP integration. And that's essentially the dynamic mapping. So if there's an issue and we need to retrieve something that's from the cat MCP server using one of the four tools, it would be expected that whatever bot we create for WebEx is able to do that too."
- The bot must combine both. Colin: "So it would have the known mapping that we already come up with. as a kind of a static resource, and it would also have ability to access that cat MCP. So two sides, similar thing. That's the big deployment target for the week."

Colin already cites "one of the four tools" of the CAT MCP. That number comes from Srikar's Friday research and is repeated when Srikar reports out below.

## 2. Colin Flags the Skill Deployment Problem and Recommends Codex with a Playbook for Further CAT MCP Investigation

Just before Srikar speaks, Colin pivots from Saurav's WebEx bot deployment concern to skills, and surfaces two problems with the current state of the categorizer plus the open question about what CAT MCP can actually do for the bot:

- **Skill deployment is immature.** Colin: "Skills, I understand there is a way to deploy. It's not really that mature, but there is something on deep side at least for it. But the problem once again comes deployment."
- **The categorizer covers history, not new traffic.** Colin: "for instance, for the skill categorizer, a skill that was built, that has run on all the historical stuff, but it does not cover any of the new stuff. Right, so if there's new issues that come in that aren't categorized, that can't work."
- **CAT MCP needs to be put through its paces, and Codex with a playbook is the recommended way to do that.** Colin: "And even if, you know, the issue comes in and you're trying to use Cat MCP, Cat MCP, if you, we're going to need to investigate that and really kind of put it through its paces here. And I recommend Codex to do that with a playbook."
- **The open technical question Colin poses out loud.** Colin: "Because are we even able to do the proper querying of cat using that MCP given how the issues come into the chat?" This is the exact gap that Srikar then steps into and answers.

## 3. Srikar's Friday CAT MCP Research: What the MCP Exposes

Srikar responds directly to Colin's "are we even able to do the proper querying" question by reporting what he found on Friday (2026-04-24).

- **He spent Friday on this.** Srikar: "Yeah, Colin, I, I, I looked into that cat MCP on Friday, so I have to put a document on the chat."
- **The MCP exposes four tools total.** Srikar: "what I did is, like, I looked into like MCP and it has like four other tools, 4 tools total." The "four other tools" phrasing is a transcription artifact; Srikar means the CAT MCP exposes exactly four tools.
- **He has documented this on the BayOne IT CICD automation chat, not in the repo.** Srikar: "I have to put a document on the chat." Later he confirms: "I just like I kept a document on the chat BayOne IT CICD automation, so I added like a status, like what what all is happening in that on the process, like how how how it works, so just a small document referring to ... On the entire flow." At the moment he speaks, this is a chat-side document only. It has not been pushed to the repo.

## 4. The Core Technical Gap: Issues Arrive with PR IDs, but the CAT MCP Requires CAT IDs

This is the load-bearing finding of Srikar's research, and the precise reason a mapping table becomes a precondition for the dynamic query path.

- **What the chat actually delivers.** Srikar: "usually in the chats we are getting like PR number ... like PRID, we are not getting any cat ID for getting the details." The chat-side input the bot sees is a PR number (PR ID, also referred to as PRID). It does not include a CAT ID.
- **What the CAT MCP actually requires.** Implicit in Srikar's description: to retrieve the issue/PR details, you have to ping the MCP with a CAT ID. A PR ID alone cannot be used to query.
- **The gap, stated as a precondition.** Srikar: "So we have to have a like map mapping table where we have cat ID and PRID mapping and of where we can get the cat ID and we can ping the MCP using that and then we can. fetch the latest details of that particular PR and respond back."
- **Stated plainly:** the dynamic CAT MCP query path is gated on an external-to-MCP mapping resource that pairs every PR ID with its corresponding CAT ID. Without that table, the bot has nothing to feed the MCP. With it, the bot can resolve any PR ID it sees in chat to a CAT ID and proceed.

## 5. Srikar's Proposed Flow, and the Two Skills He Built Around It

Srikar does not stop at flagging the gap. He has already designed and built a flow that consumes the mapping table and routes the dynamic query end-to-end.

- **The flow, in Srikar's own words.** "we have a like map mapping table where we have cat ID and PRID mapping and of where we can get the cat ID and we can ping the MCP using that and then we can. fetch the latest details of that particular PR and respond back."
- **Decomposed step by step:**
  1. Bot receives a chat message containing a PR ID.
  2. Bot looks up the CAT ID corresponding to that PR ID in the mapping table.
  3. Bot pings the CAT MCP using that CAT ID, calling the appropriate tool from the four available.
  4. Bot receives the latest details of that PR back from the MCP.
  5. Bot responds back into the chat with the fetched details.
- **The skills Srikar built to embody this flow.** Srikar: "So I just like created a like skill for issue responder and like MCP or like the cat MCP." Two skills, paired:
  - The **issue responder** skill (the orchestrator that takes the PR ID, performs the lookup, and posts the response).
  - The **CAT MCP** skill (the wrapper that actually pings the CAT MCP using the resolved CAT ID).
- **He invites Colin to read the chat doc before the Srinivas call.** Srikar: "So if you can refer like a little bit on that document I think that way like ... We can move forward like if that is the right option."

## 6. Colin Asks Where the Skills Live, Srikar Confirms They Are Not Yet on the Branch

This is the moment that triggers the "push to the branch" instruction.

- Colin: "Got it, got it, got it. So one thing for that, so did you push that one to the... This goes yet on the branch or where did that one land up?"
- Srikar: "No. So, I can I can push it to the branch, so I just like I kept a document on the chat BayOne IT CICD automation, so I added like a status, like what what all is happening in that on the process, like how how how it works, so just a small document referring to ... On the entire flow."

The state at this moment: design is documented in the chat. Two skills have been built locally. Nothing has been pushed to the CICD repo yet.

## 7. Colin's Routing Decision: Repo Conflict, Then Saurav Reframes It Cleanly

Colin's first instinct is to put the skills in two places to hedge against Srinivas's contradictory prior instructions. Saurav pushes back with a cleaner framing that Colin then adopts.

- **Colin's initial both-places instruction.** "I think it's, and Saurav, correct me if I'm wrong, I think that there is also kind of a conflict there because he had us try to drop skills in two different places. You know, on one meeting he had said, put them in that CICD repository." Saurav adds: "And they also have like one website where he said like share it on that repo." Colin: "Okay, so let's put it on both and just call it a day."
- **The branch path.** Colin: "I think there is a branch called skills slash WebEx. I think, Saurav, that's where all your skills are at." Saurav confirms. Colin: "I'll put that link in the WebEx chat right now so you can see where it is. Srikar. And then you can put your skills on there."
- **Saurav's reframing, which Colin accepts.** Saurav: "I was also in the same thing, like I was thinking like for the current use, we should keep them on like CICD. And once we have finalized and like tested them enough, then we can go to that other repo and posted there. So that's why I did not add or else it would fall on our part to like maintain both of them." Colin: "Yes, actually, I like that framing. Let's keep that framing. We'll only put them on that repository for CICD in that branch. We don't have to worry about two places. I'm going to frame it to him exactly like that today. The finished skills that have been tested and verified will go into that master skills repo whenever they are fully done."
- **Net rule for the week:** unfinished or in-test skills live on `skills/webex` in the CICD repo. The separate master skills repo is reserved for fully tested, finalized skills. Srikar's CAT-MCP-related skills are in the unfinished bucket, so they go on `skills/webex`.

## 8. Mid-Call Confirmation: Srikar Pushes the Three Skills During the Meeting

About 12 minutes after Colin asked him to push, Colin closes the meeting with an immediate-action ask, and Srikar reports that the push has just happened.

- **Colin's direction at meeting close.** "So in the meantime, immediate actions, number one, Srikar, get yours, skill committed to that branch of that repository."
- **Srikar's confirmation, in real time.** Srikar: "Yeah, I... I just did Colin, yeah. I just added all the an annex categorizer, as well as the issue responder scale, so which has like other four, like 3 placeholders, and with along with the one cat cat MCP."
  - Decoded: "an annex categorizer" is the **issue categorizer skill** (the NX-OS issue categorizer; "an annex" is a speech-to-text mangling of "nxos" or "an NX-OS"). "Issue responder scale" is the **issue responder skill**. "Cat cat MCP" is the **CAT MCP skill**. "Like other four, like 3 placeholders" reads as Srikar saying the issue responder skill ships with four pieces inside it, three of which are placeholders, alongside the one CAT MCP skill.
- **What was pushed to `skills/webex` during the call:**
  1. Issue categorizer skill (the NX-OS issue categorizer, previously run on historicals).
  2. Issue responder skill (with three placeholder sub-pieces inside it, per Srikar's count).
  3. CAT MCP skill (the wrapper for the four-tool CAT MCP, paired with the issue responder).
- **Colin verifies on screen and accepts.** Colin: "Ohh, great, great, great. Oh, great, great, great. Yep, I see all of them on there now. That's great. So I'm going to add those in as some of the deliverables that are completed. I'm just going to frame them as completed. It's fine."

## 9. Built-vs-Stub: Colin Asks, Srikar Does Not Answer Explicitly

Colin needs to know what to call "done" versus "promised this week" when he frames things to Srinivas.

- Colin's exact ask: "But we'll say that, are there any ones that are like explicitly just like stubs that aren't built at all? Because I can phrase those as things we'll deliver this week."
- **Srikar does not answer the stub question.** The transcript has no Srikar reply to this question. The implicit answer is in his own earlier sentence: the issue responder skill has "3 placeholders" inside its four-piece structure. So at minimum three components inside the issue responder are stubs. The CAT MCP skill and the issue categorizer are described as built; the issue responder is built as a shell with three placeholder sub-components.
- **Colin will frame the lot as completed deliverables to Srinivas anyway,** and back-fill the stub framing only if needed: "I'm just going to frame them as completed. It's fine."

## 10. Saurav's Adjacent Comment: Back-End Integration Is Still a Friday Deliverable

Saurav steps in to make sure Colin does not over-credit the team on the back of Srikar's push. The skills are pushed, but the back end that wires them into the bot is not.

- Saurav: "So in a way like we have to like code the whole back end to make sure that everything inside the CICD as well as the skills are also taken into account for the bot. So in a way that is kind of still a deliverable for us for the end of the week. And for them it's like getting the. Bot details for like the front end."
- **Decomposition of Saurav's point:**
  - BayOne side: code the back end of the bot so that everything in the CICD repo plus the skills (categorizer, issue responder, CAT MCP) are wired into the bot's runtime. Friday is the deadline.
  - Cisco/IT side: provide the bot front-end registration details (bot name, bot ID, access token) that Saurav described earlier in the call. Without those, even a fully wired back end cannot deploy as a registered WebEx bot.
- **Colin acknowledges and folds it into the Monday-call framing.** Colin: "Right. ... Back. Yeah, so what I'm going to do is I'm going to update this sheet based upon everything we talked about now. I'll share this with everyone. I'm going to put it on the GitHub page itself."

## 11. Open Technical Questions Surfaced by Srikar's Findings

These are the questions Srikar's research opens up that the team has not yet resolved. They map directly into things Colin will need to either answer internally or raise with Srinivas.

- **Mapping table source of truth.** Srikar identified that a CAT-ID-to-PR-ID mapping table is a precondition for the dynamic path, but the call did not establish where the table comes from. Two candidates:
  1. Cisco-side: an existing CAT-to-PR mapping that Cisco can hand BayOne (a database, an export, an API).
  2. BayOne-built: the team derives the mapping themselves, possibly from CAT exports plus PR metadata, possibly via the categorizer's existing dataset.
  This must be resolved before the dynamic path is testable.
- **Whether the four CAT MCP tools are sufficient to support proper querying given how issues come into chat.** This is Colin's earlier framing ("are we even able to do the proper querying of cat using that MCP given how the issues come into the chat?"). Srikar's response answers part of it (yes, given a mapping table) but does not enumerate the four tools or confirm that one of them performs the by-CAT-ID detail fetch the proposed flow assumes. Codex with a playbook is Colin's recommended path to put the MCP through its paces and answer this fully.
- **Is a static-only fallback acceptable for Friday?** Given that the dynamic path depends on a mapping table that may not be available by Friday, the implicit fallback is to ship the static FAQ side (categorizer-driven) and represent the dynamic CAT MCP path as built but pending mapping. The call did not explicitly choose this fallback.
- **Stub coverage in the issue responder skill.** Three of the four pieces inside the issue responder are placeholders. Which three, what they are placeholders for, and which is the one non-placeholder piece are not stated in this transcript. Colin would need this detail to honestly differentiate "completed" from "stubbed" when speaking to Srinivas.
- **Skill deployment mechanism on `skills/webex`.** Colin notes "I don't know if we have push permissions or whatever on that" at the moment he sends the link. Srikar's mid-call push proves the team does have write access to the branch, which retroactively answers that question, but the broader question of the deployment mechanism for skills (Colin: "It's not really that mature, but there is something on deep side at least for it") remains open.

## 12. Status of Srikar's Items at End of Call

- CAT MCP investigation: **complete for Friday's scope.** Four-tool surface area enumerated; PR-vs-CAT-ID gap identified; mapping table identified as the unblocker.
- Chat-side status document on BayOne IT CICD automation: **published before this call.**
- Issue categorizer skill on `skills/webex`: **pushed during this call.**
- Issue responder skill on `skills/webex`: **pushed during this call** (shell with three placeholder sub-components plus one built piece, per Srikar's count).
- CAT MCP skill on `skills/webex`: **pushed during this call** (paired with issue responder, embodies the PR-ID-to-CAT-ID-to-MCP-call flow).
- PR-to-CAT-ID mapping table: **not built, not sourced. Open precondition for the dynamic path.**
- Back-end integration tying skills + CICD repo into the WebEx bot runtime: **not done; Saurav owns; due end of week.**
- Codex-with-playbook deeper investigation of CAT MCP capabilities: **recommended by Colin, not yet started.**
