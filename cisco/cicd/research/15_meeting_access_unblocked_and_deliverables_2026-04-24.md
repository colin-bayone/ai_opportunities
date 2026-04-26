# 15 - Meeting: Access Unblocked and Deliverables

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/source/week_2026-04-20/day_2026-04-24/srinivas_4-24-2026_formatted.txt
**Source Date:** 2026-04-24 (Friday afternoon Srinivas sync)
**Document Set:** 15 (Sixth Srinivas team meeting)
**Pass:** Focused deep dive on the one-page deliverable format, NX repo access unblock, CI/CD repo clarification, and next-Friday deployment target definition

---

## Overview

The Friday afternoon Srinivas sync on 2026-04-24 closed several access threads that had been blocking CAT MCP execution and locked in a clear, scoped definition of what BayOne is delivering by the end of the following week. The meeting opened with the one-page Friday deliverable BayOne had produced, "Open Items and Access," and that document set the agenda. Each item on the page received a resolution path or, in two cases, a direct unblock from Srinivas himself.

The single most consequential outcome was Srinivas committing to add BayOne user IDs to the NX repository lead-only group personally, bypassing the standard Cisco IT provisioning cycle. That commitment removes the last remaining blocker for CAT MCP execution and shifts the engagement's critical path off access provisioning and onto application build work. It also represents a meaningful trust signal: Srinivas is putting his own name behind BayOne's access to a controlled repository.

---

## One-Page Summary Slide Format Decision

Early in the meeting Srinivas surfaced a process expectation looking at the Friday "Open Items and Access" document on the screen.

Srinivas: "can we do one thing? Didn't create one last time also. I want one summary slide of one of the delivery rules for the next week. I don't want a very huge document, just only one."

He explained the intent: the summary should let him see the work in flight at a glance and serve as a weekly check on whether scope still matches the goal. "That way we know what are the tasks we are working on. And what is the next item delivery that we are marching towards? And then we can say, do we need to add one more item or not?" The document on screen was not the format he wanted as a recurring artifact. "Because I know this view is very hard. I can say, OK, what is the birthday view of the entire summary, right?"

Colin agreed. "I'll get a simple view for Monday." Srinivas confirmed: "Yeah, just a simple, make it simple, just one slider. And then we'll track where we are, what is the current status, and any new items that we are adding for the next week."

Friday's deliverable remains the detailed working document. Monday's deliverable becomes a single-page status that Srinivas uses as the standing weekly reference.

## Format Decision: GitHub Markdown with Mermaid

Colin proposed an implementation BayOne already uses internally. "Would it be OK with you if we did? Because we did this actually internally. We can have that in GitHub. They're just basically markdown files, mermaid charts if you need a graphic. That way you can actually see. We go over, we can see this."

Srinivas immediately endorsed it and pointed Colin to the right repository. "You can use the issues listed in the CI CD itself. You can add there also. You can use GitHub itself. That's how we do the other products."

Colin: "OK, perfect. Easy enough. Less work for me too, honestly. So that's great."

The Monday status deliverable lives as a GitHub markdown file inside the CI/CD repository. Mermaid charts are available when a graphic helps. Issues are tracked in the same repository's issues list, so a single location holds both the status snapshot and the working backlog. This aligns BayOne with the workflow Srinivas already uses for his other engineering products.

## NX Repository Access Unblock

The NX repository access item had been the critical-path blocker for CAT MCP execution coming out of Set 14. Colin had already obtained MCP-level access, but the deeper access needed to test commit approval tracking and run the CAT MCP against the live repository remained outstanding.

Colin raised it directly. "I think there's one for the NX repo access. This one on my end is resolved. I have access to the MCP, but it's to test out the MCP. I think it requires some commit approval tracking access on the NX repo." He started to lay out the constraints, then trailed off. "We don't have any kind of..."

Srinivas cut directly to the resolution.

Srinivas: "There is some group there. I can add them. I can add them as lead only users. Give me the user ID, all the user ID's that need to be added. I'll add them."

Colin accepted on the spot. "Sure. I'll send it after the speed [meeting]." Srinivas: "Sure. Thank you."

This is the biggest strategic win of the meeting. The standard Cisco path for access to a controlled repository runs through IT provisioning workflows that have, in this engagement and in adjacent ones, taken weeks. Srinivas chose to skip that path entirely. He has the rights to add lead-only users to the group, and he is using those rights to bring BayOne in himself. That decision changes the engagement's risk profile in three ways.

First, it removes the last gating dependency for CAT MCP execution. With NX repository access in place, BayOne can run the CAT MCP against the live repository, observe commit approval tracking behavior, and validate the dynamic answer path. Second, it shifts the critical path. Until this meeting, progress was bounded by access provisioning. After this meeting, the bound is BayOne's application build velocity. Third, it is a trust signal. Srinivas is willing to put his own name on BayOne's presence in the lead-only group, which is a stronger endorsement than any procedural acknowledgment.

Colin's commitment to send the user IDs immediately after the meeting is the operational completion of this thread.

## CI/CD Repository Clarification

The second access item was a clarification. BayOne had received two repository pointers in earlier conversations and needed to know which was the correct destination for skill commits.

Colin: "We have this. This one is resolved at this point. We have the CICI [CI/CD] repository. We have one point of clarification. There's two different locations that you gave. One was the, it started with a K, if I'm not mistaken here."

Srinivas identified the second location. "This would be, this is SME-KB repo."

Colin: "Okay, got it. The other one is just the generic. So this one, all the skills, right? Whatever you're committing."

Srinivas confirmed and gave context. "Technically, what we did is we have an XPR. We'll maybe next week or something, we may announce it, but yeah, you can, for now you can, we'll re, we rework on the skills part. So, but ideally we want all the skills to be part of this repo. And then the app will pull it from here. So we are creating an MCP vault of this repo itself. And that piece is not ready. So, but we can refactor the code later on. So, you guys have to do whatever you have."

Colin: "Makes sense."

The decision: all skills go on the main CI/CD repository. SME-KB is a separate concern. The Cisco team is constructing an MCP vault on the main repository so that the CI/CD application can pull skills directly from it. That vault is not ready yet, but the destination is set, and any refactor happens later. BayOne keeps pushing skills to the main repository and does not branch into SME-KB.

The XPR reference is unclear and warrants follow-up. It may be an internal Cisco platform name that will be announced the following week. For now BayOne has enough direction to keep moving.

## Codex Admin Constraint and DS Agent Init Pattern

Colin floated a distribution mechanism that would have simplified rollout. "one thing, I don't know if you already have it set up, that you can do is all these skills can be auto-discovered in codecs [Codex]. So it's just one connection that you make. It's just a config.json file. Are you the admin for codecs [Codex]? By chance."

Srinivas declined and pointed elsewhere. "No, I'm not going to do it. Your manager is up there. So you have to... Yes, doctor will tell you this."

The Codex auto-discovery path is not available through this meeting. Srinivas described the alternative Cisco already uses. "once you do the products, we have a wrapper which doesn't init. And once you do the init, init will actually go and pull the skills from this and install as a part of the individual's thing." He restated it from the user's point of view. "the invention [intention] that's what the user will do they will do a deep site agent in it there's something called ds agent and when does the in it it will largely pull the skills and installs in there."

Each user runs a "ds agent init" command, which pulls the current skill set from the main CI/CD repository and installs the skills locally. Distribution is pull-based and per-user. BayOne does not need Codex admin involvement.

## Next-Friday Deployment Target Definition

The fourth item, and the one Colin explicitly wanted to lock down before leaving the meeting, was the definition of what "deployed by next Friday" means. Colin had not been in the Wednesday meeting where a target was first discussed.

Colin: "The very last thing here was just I just wanted to get from you because I know I wasn't there on Wednesday. I just want to make sure that we have everything that you're expecting ready for you by Friday. So if that's the deployed WebEx bot, if that's just getting deep site online and getting something like the CICB [CI/CD] app deployed to it, I just wanted to confirm from you what was your expectation by the end of the week next week for that item."

Srinivas described the target in two parts. The first is the CI/CD application running with combined static and dynamic question handling.

Srinivas: "For the deep side, so first thing is we need to create a fat [FAQ] out of it given day [given the data]. The answers are already done in that way. So we need to first create a static fat [FAQ] least because not everything is dynamic. Dynamic part is in the cat recipe [CAT MCP]. Static part is there are some environmental issues and whatnot that is already there in the answers by the user. So we need to basically create a static for the static question answers and then for the dynamic part is part of the cat [CAT MCP] himself right."

The framework is hybrid. Static FAQ entries cover environmental issues and recurring user questions for which the answers are already known. Dynamic answers are handled by the CAT MCP, which queries the NX repository at request time. Both routes feed the same chat interface in the CI/CD application.

Srinivas described the end state. "assuming that your radius [admin] issues are resolved assuming this thing you should be able to bring up the CACD [CI/CD] app on your idea server [ADS] plug in the CAT MCP and these questions behind it so that the user asks a question in the chat box that I was showing you here that you should be able to get an answer for either dynamic or static, both. That is one part of it."

## WebEx Bot Deployment Target

The second part of the target moves the same backend behind a different frontend.

Srinivas: "The second part of it is... The bot itself, we need to work together and create a deep side bot that can be part of the NXEI [NX-OS CI] pipeline. The same information we should be able to, the user should be able to ask in the NXEI [NX-OS CI]. So that would be, the backend is common in the app. So if you can design the backend as an SAP [Service Application Platform], then technically we can plug in the UI and plug in as a part of the comp [component] itself. That way no work is related and we will just attach the LLM either through circuit for knowing how it but once we bring in deep secret you get the deep circuit credentials. You can use user credentials at that time and then basically get an answer."

Colin confirmed. "Okay, easy enough."

The architectural instruction is clear. The CI/CD application backend is built as a service-application-platform style backend with two pluggable frontends. The first is the chat box in the CI/CD application running on ADS. The second is a DeepSight-aware bot in the NX-OS CI WebEx space. Both frontends call the same backend, which routes questions to either the static FAQ path or the dynamic CAT MCP path. The LLM is initially attached through the circuit API with shared credentials, and migrates to per-user DeepSight credentials when DeepSight is issued.

## Path for LLM Credentialing

Colin acknowledged the open question around how shared credentials get distributed in the interim.

Colin: "Yeah, we had to look towards, maybe in the middle of the week, how to get that on the upper term."

Srinivas: "As I said, there are some... Yeah, if I give Kia [key], you need to..."

Colin: "Yeah, I will, we'll find out a bit. I'll have to think through how to get this key out of the stairs."

Srinivas: "Now, I'll give you an answer back on that quick."

The exchange leaves the LLM credentialing mechanism as a mid-week conversation. Colin owns the design of how a shared circuit key is distributed to BayOne developers without compromising it. Srinivas owns a quick answer back on the constraints from the Cisco side. The longer-term path is per-user DeepSight credentials, which removes the shared-key problem entirely once DeepSight is generally available.

## Access Summary at Close of Meeting

By the close of the meeting all four access and clarity items on the Friday document had a resolution path.

ADS access: in flight, with Mahaveer's escalation expected to resolve the same day. Colin: "we'll get that resolved today with my appeal."

NX repository access: fully resolved by Srinivas's offer. Colin had already secured MCP-level access. The lead-only group access that gates CAT MCP execution will be added by Srinivas himself once Colin sends the user IDs after the meeting.

CI/CD repository: clarified. The destination for all skills is the main CI/CD repository, not SME-KB. The MCP vault is being constructed on the main repository.

Deployment form: resolved earlier in the meeting. The application uses on-demand pull at request time, plus a low-frequency dashboard refresh. There is no central poller.

Next-Friday target: defined precisely. Static FAQ plus dynamic CAT MCP behind a chat interface in the CI/CD application running on ADS. WebEx bot on the NX-OS CI pipeline sharing the same backend. LLM via circuit API initially, DeepSight credentials when issued.

## Meeting Close

The meeting ended on operational notes that confirmed the new working pattern.

Colin: "So I've got my actions, I took my notes throughout. So yeah, we're all good on it. I don't have to wait for the meeting. We can use the address space as a way to unblock each other."

Srinivas: "Yes, of course." "Have a good weekend."

Colin: "Yeah, you put it in the web space while you're waiting."

Srinivas: "Yes, I will do that now."

Srinivas closed by directing Anupma to handle a follow-up with Shyam on the DeepSight side. "Anboma [Anupma], please work with Shyam on the post poll thing on the deep side."

The exchange about the WebEx space confirms asynchronous unblocking is now accepted. BayOne does not need to wait for the next standing meeting to surface a blocker. This is a meaningful change in working cadence and reduces the cost of small blockers significantly.

## Strategic Reading

Three strategic shifts came out of this meeting.

The one-page deliverable format is now the engagement's weekly status pattern. Friday produces the detailed working document. Monday produces a single-page status that Srinivas uses as the standing weekly reference. GitHub markdown with Mermaid charts is the substrate, and the file lives in the CI/CD repository alongside the issues list.

The NX repository access unblock is the single most consequential outcome. It replaces a standard Cisco IT provisioning cycle with direct Srinivas action. CAT MCP execution can begin as soon as Srinivas runs the add. Beyond the operational effect, the unblock is a trust signal that reframes how Srinivas is engaging with BayOne.

The next-Friday target is now specifically defined and scoped. The CI/CD application runs on ADS. The CAT MCP is plugged into the backend. The static FAQ and the dynamic CAT MCP path both feed the chat user interface. The WebEx bot shares the same backend and is deployed on the NX-OS CI pipeline. The LLM runs through the circuit API at first and migrates to DeepSight credentials when DeepSight is issued. Every blocker except Mahaveer's ADS portal has a resolution path committed in this meeting.

## Forward Action Items

Colin sends user IDs to Srinivas immediately after the meeting so NX repository access can be added.

Colin produces the Monday summary as a GitHub markdown file in the CI/CD repository, with Mermaid charts where graphics help, and tracks open items as issues in the same repository.

BayOne pushes all skills to the main CI/CD repository. SME-KB is not the destination for skill commits.

Skill distribution to users runs through the ds agent init pattern. No Codex admin coordination is needed.

The CI/CD application backend is designed as a service-application-platform style backend with pluggable frontends. The chat user interface is one frontend. The WebEx bot on the NX-OS CI pipeline is the second. Both share the same backend and the same routing between static FAQ and dynamic CAT MCP answers.

The static FAQ covers environmental issues and recurring user questions. The dynamic CAT MCP path handles questions that require live lookups against the NX repository.

LLM integration runs through the circuit API initially. The mid-week conversation between Colin and Srinivas resolves how a shared circuit key is distributed to BayOne developers in the interim. The longer-term path is per-user DeepSight credentials.

Asynchronous unblocking through the WebEx space is an accepted pattern. Either side can post a blocker between meetings.

## Open Items to Track

The XPR reference is not yet clear. Srinivas indicated an announcement may come the following week. BayOne tracks the announcement and confirms implications for skill organization.

The shared circuit key distribution mechanism is open until the mid-week conversation. Colin owns the design. Srinivas owns the constraints from the Cisco side.

The Mahaveer ADS portal escalation closes the same day as the meeting and is the only remaining access item without a confirmed resolution at the close of the Srinivas sync.
