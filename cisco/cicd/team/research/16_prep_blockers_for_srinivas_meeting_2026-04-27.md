# 16 - Team Prep Call: Blockers for the Srinivas Meeting

**Source:** /cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/cicd-team-monday-pre-meeting_01_formatted.txt
**Source Date:** 2026-04-27 (Monday team pre-meeting, 15:15-15:45 PST, 75 minutes before the 1pm Srinivas sync)
**Document Set:** 16 (BayOne team prep call before the Monday Srinivas meeting)
**Pass:** Focused deep dive on the four cascading blockers Colin will raise on the upcoming Cisco-side call

---

## Framing of the Meeting Itself

Colin opens by signaling this will be a quick prep session because "nothing too crazy has happened" over the weekend. He explicitly sets the agenda: "I want to go through quick what we're going to talk about to Srinivas for today." He has authored a one-pager describing what is expected for the coming week and intends to walk through it on the 1pm Srinivas Pitta call.

Colin frames the upcoming call's purpose around a single deliverable target: a CI/CD application deployment for Friday May 1. The deliverable has two halves:

1. **Static FAQ side** - A WebEx FAQ bot that answers questions already addressed in the past or where there is a deterministic easy answer. The static mapping (issue mapping) already exists from Srikar's skill output.
2. **Dynamic CAT MCP integration** - The bot must also query the CAT MCP server using one of the four tools when an incoming issue requires retrieving information not in the static map. Colin: "if there's an issue and we need to retrieve something that's from the cat MCP server using one of the four tools, it would be expected that whatever bot we create for WebEx is able to do that too."

Both pieces must be a deployed WebEx bot by Friday. Every blocker below traces to that gate.

Colin's tactical posture for the call is explicit: "be annoying. Be annoying." He commits to flagging unresolved blockers in the CI/CD WG chat at the start AND end of every day this week, telling the team "at minimum, there will be 10 messages from me this week in that CICD WG chat." Rationale: "I want this to be clear that this is not on us for a lot of these. These are just things that Srinivas is asking kind of, you know, loaded cannon not aiming anywhere, any particular direction."

Colin also references that Rui has already deployed a chatbot to WebEx, which proves there is a working process somewhere inside Cisco. He plans to use this as leverage: "clearly there is some process that can work. And the question then becomes, you know, how do we do the same?"

---

## Blocker 1: Permanent ADS Machine Unavailability

### (a) The Technical Gate
A permanent ADS (Application Deployment Service) machine is required to host the bot back end in production. Without it, the Friday deliverable cannot be tested or deployed to a stable environment. Saurav also notes later that the bot back end "I think he needs that on a like permanent ADS machine."

### (b) Colin's Rehearsed Framing
Colin reconstructs the chronology of contradictions from Srinivas Pitta:

- "On one hand, he said, you know, put in the request for the ADS machine and then you'll just need a tenant. Did that. Never happened."
- Then "Mahavir's to blame, which is technically true. He technically should have done that, or at least given clear direction. He just sends back the temp ADS instructions."
- Friday revelation: "What's happening right now is they don't have any permanent ADS machines available. That was said by Srinivas on Friday."

Colin's rehearsed line: "How the heck is Mahavir supposed to provision something of which he has none? So that's where I'm going to raise that today as, you know, that's on you guys. That's not on us anymore. Unless you are explicitly saying that that is something that we are able to resolve without actual intervention from Cisco IT. As far as that goes, there's no possible way for us to deploy on an ADS machine without Cisco itself provisioning one for us. And if they're out of servers, that's an impossible deliverable."

He plans to meet Mahaveer Jinka earlier in the day, then escalate to Anand Singh: "I'm going to just get it anand in the loop, whatever their outcome is."

### (c) Fallback Position
"My fallback for that is to say we will work to a temporary ADS machine."

Colin notes a related Srinivas confusion he will also clarify: he asked Srinivas if there is any limitation to temp ADS machines (e.g. compute). Srinivas said yes, but Colin finds this confusing because "anyone can request any temp ADS at any time, and it doesn't seem like it's linked to anything." Colin's working interpretation: "each part of the organization is allocated some level of compute across all temp ADS machines... when you're requesting a new machine and you go through those drop-downs, that probably is subtracting allocation from somewhere somehow." Practical implication: "we can't do anything super heavy on those ADS, but in any case, I think that's where the current state is."

### (d) What Colin Needs Srinivas to Commit To
A hard line tied to the Friday May 1 gate: "if he says no, wait for the permanent, then I'm going to say it has to be ready by tomorrow [Tuesday April 28] for the permanent ADS or else this is not possible to deliver this week. We can't even test it."

Specifically Colin needs:
- Acknowledgement that responsibility for permanent ADS provisioning is Cisco IT's, not BayOne's.
- Either a permanent ADS by tomorrow OR explicit approval to deploy to temp ADS for Friday.
- Clarification of "what our responsibility is and what Mahavir's and Srinivas's is" with respect to ADS provisioning.

---

## Blocker 2: LLM Access Cascade

### (a) The Technical Gate
The bot must call a language model to answer non-static questions. The path to LLM access has been described by Srinivas as a cascade: ADS machine -> DeepSight instance -> language model access granted by Srinivas. Without an LLM, the AI deliverables cannot function. Colin: "How is the AI team supposed to work without language models?"

### (b) Colin's Rehearsed Framing
The team had been using Circuit API credentials to test LLM calls. Srinivas Pitta flagged this on Friday as "improper in some way." Colin's read: "I think those credentials are really just for testing out different things. You know, they're probably very limited on how many tokens they have, et cetera."

Colin builds the cascade out loud so he can confront Srinivas with it directly: "however, he's the one that has to grant the language model access, which you can see where this is going. In order to get the language model access, he needs a deep set instance. Deep set instance needs an EDS server. So it's a cascade."

He explicitly does not want this dragged into Wednesday: "I don't want it to come to like Wednesday. And he's like, so where are you guys at? And I'm like, hey, man, there's still blockers that we surfaced that you haven't addressed. And he's like, no, you haven't."

### (c) Fallback Position
Colin proposes a two-track fallback: "a concession we're going to have to make is to do this with either a temp ADS machine, if DeepSight can get deployed on that, or just continue to use Circuit API and plan to switch it out whenever the time comes."

### (d) What Colin Needs Srinivas to Commit To
The critical question Colin will force at the meeting (verbatim): "even if we spin up DeepSight, even if we get the ADS machine, do we then have language model access? Or what is the path to that? That is a critical thing because that gates pretty much every item on this sheet."

He also needs explicit permission for the interim: "Unless we're allowed to use the circuit API stuff in the meantime. Language models are a language model at the end of the day."

Open questions to resolve today:
- Is DeepSight deployable on a temp ADS, or strictly permanent?
- Even with DeepSight deployed, is LLM access automatic or a separate Srinivas grant?
- Is Circuit API approved as an interim LLM source until the proper path is online?

---

## Blocker 3: WebEx Bot Deployment ID and Service Account

### (a) The Technical Gate
A WebEx bot, regardless of where its back end is hosted, needs a registered identity in Cisco's WebEx bot registry. Today, the bot Saurav built is registered to his personal Cisco ID. Saurav lays out the failure mode: "Suppose I deploy this model using my Cisco MI, sorry, Saurav MI at the rate Cisco. account and tomorrow I leave the organization or we are off to another project or somehow that account got suspended. I am on to a new account. That bot deployment is gone."

The deployment process as Saurav describes it:
- Anyone with a Cisco ID and VPN can technically deploy a bot.
- After deployment, the bot must be registered with the Cisco bot registry via a form. The form captures bot purpose, deploying ID, target channels, etc.
- Cisco IT then audits and approves. Once approved, the bot is added to the registry.
- However, the registry entry remains tied to the personal ID, "not like from. Like my ID as in Cisco's my ID, but at a personal level, not like an org level."
- If the personal ID is later disabled (project end, departure), "the registry itself will be gone."

Saurav also flags the front-end vs back-end split: back end (the container running the bot logic) "I can host normally" in a Podman container, but front-end registration with WebEx requires a bot name, bot ID, and access token, which "after we have those, we put those into the .env file or however he wants to manage that."

### (b) Colin's Rehearsed Framing
Colin amplifies Saurav's point and commits to escalating it on the call: "Even if it ****** him off, at this point, it doesn't matter, because we're going to get dinged if we have a deliverable that we didn't speak up on... today on the call, I don't want to even get off that call until this is kind of clear and resolved by them."

Colin's framing distinguishes POC from production: "If he wants us to do it in like POC mode with personal, that's fine. But if he's expecting something productionalized, you know, with a zero day run, you know, lead time on it, that's crazy."

He commits to backing Saurav up vocally on the call: "I'm going to be right there too. I'm going to be blowing on the same trumpet because he needs to be fair with that. It doesn't make sense to ask someone to deploy something if you haven't given them literally anything to deploy with."

Saurav's framing of the ask, which Colin endorses: "it should not be on me or else even for like anyone of our team, even if we want to deploy it personally, it should either be like Srinivas's bot deployment or someone else."

### (c) Fallback Position
- POC mode acceptable if Cisco only wants a proof of concept on personal ID. "If he wants us to do it in like POC mode with personal, that's fine."
- Colin will "at least say that I'm going to try to register a bot on the portal. I'll say that's one of the pending items today."
- Production fallback ask: a Cisco service account, "Srinivas's bot deployment or someone else" - i.e. the bot is owned by an organizational identity that survives personnel turnover.

### (d) What Colin Needs Srinivas to Commit To
- Acknowledgement that bot deployment ID is a Cisco-side responsibility, not BayOne's.
- A documented process or organizational ID (service account) under which the production bot will live.
- "Effectively they need that service account. That's the best way to do that."
- Clarity on whether Srinivas wants POC behavior or productionalized behavior.

---

## Blocker 4: Bot Compliance Email Received Today

### (a) The Technical Gate
Saurav received an email TODAY (April 27) saying his existing bot was flagged non-compliant. Mahaveer Jinka is on CC. The email arrived during the prep call: "actually I just got a mail today also that your bot is not compliant. Let me just check in that mail." Saurav forwards it to Colin during the call and shares the bot registration portal link in the team group.

This collides directly with the Friday May 1 gate. Colin: "if the bot's not compliant, there's no way for it to get deployed by Friday."

### (b) Colin's Rehearsed Framing
Colin's framing turns the lack of documented compliance criteria into a Cisco-side responsibility: "whenever we say compliant, there needs to be some kind of a, you know, some compliance to be compliant with. So they need to share that. So we can flag that as an item for Srinivas today."

He also positions the audit/review as outside BayOne's control: "for us, we need to say it's not gated on us, it's gated on IT review. So on our end, we can say that ours will be ready, but we can't say deployed because deployment depends on things beyond us, which is that IT audit, review, and acceptance."

Colin reads the situation as Srinivas himself not understanding the process: "because it's clear that he doesn't know this either."

When Colin asked Saurav whether the audit reviews submitted form details or actual code, Saurav's answer was "That I'm not clear like, but yeah, because I did not submit for the audit yet. My that system got down and on this like I never ran the bot again." So even the BayOne side does not yet know what artifacts are reviewed.

### (c) Fallback Position
- BayOne's end-of-week posture will be "ours will be ready" - i.e. code complete, registration form submitted - but not "deployed," because deployment is gated on IT audit/review/acceptance which BayOne does not control.
- Saurav can resubmit for audit to start the clock if Colin asks: "if you want me to do it, I can like go through the process of audit and we can also had that ready by, like, the next meeting."

### (d) What Colin Needs Srinivas to Commit To
- Cisco must produce documented compliance criteria for any "compliant" determination to be meaningful. "There needs to be some kind of a, you know, some compliance to be compliant with."
- Acknowledgement that Friday "deployed" is a Cisco-controlled outcome, not a BayOne-controlled one, since IT audit and acceptance sit between code-complete and deployed.
- Formal acceptance that Saurav's bot non-compliance flag from today will be addressed via documented criteria, not opaque rejection.

---

## How the Four Blockers Interlock Against the Friday May 1 Gate

Colin lays out the dependency chain explicitly near the end of the call: "we have the ADS machine we need. We have the language model we need. We have the need to connect to the MCP. We have the need to have the static mapping of issues for the static FAQ. The final thing that makes all of this work is there has to be that WebEx integration. All those things working independently, it's still not an application. It has to be deployed somewhere somehow."

The cascade against Friday:

1. **No permanent ADS** -> nothing to host the production bot back end. Fallback: temp ADS, if Srinivas approves and if compute allocation allows.
2. **No LLM access** -> bot cannot answer non-static questions. LLM access requires DeepSight, which requires an ADS, so Blocker 1 cascades into Blocker 2. Fallback: keep using Circuit API in the interim, if Srinivas approves.
3. **No service account / org-level bot ownership** -> bot registry entry tied to Saurav's personal ID, evaporates if his account is disabled. Fallback: POC mode on personal ID for Friday, with productionalization deferred.
4. **No documented compliance criteria** -> bot cannot pass the IT audit needed for deployed status. Fallback: BayOne delivers "ready" not "deployed," and pushes IT review onto Cisco's side of the line.

Colin's core meta-framing for the entire 1pm call: "this is not on us for a lot of these." Each blocker, if unresolved, gets attributed to a specific Cisco-side owner (Mahaveer for ADS provisioning, Srinivas for LLM access, IT for service account and bot compliance criteria), with BayOne's posture explicitly defensive against being "dinged if we have a deliverable that we didn't speak up on."

---

## Open Questions Still Live Going Into the 1pm

- Does requesting a temp ADS subtract from a shared org compute allocation, and does that limit what the team can deploy on it? (Colin's working interpretation is yes, but he wants Srinivas to confirm.)
- Can DeepSight be deployed on a temp ADS, or strictly a permanent ADS?
- If both ADS and DeepSight are in place, is LLM access automatic, or does Srinivas grant it as a separate step?
- Does the Cisco bot audit review only the registration form's contents, or does it inspect actual bot code? (Saurav does not know; he never reached the audit stage before his system went down.)
- What are Cisco's documented compliance criteria for a WebEx bot? (Today's non-compliance email did not specify them.)
- Where exactly should skills live - the CI/CD repository or the centralized skills repo (the "KDE skills" branch)? Saurav's working approach, which Colin endorses for the call: keep them only in CI/CD until tested and verified, then promote finished skills to the master skills repo. Colin will frame this to Srinivas exactly that way.
- Does the team have push permissions on the skills/WebEx branch where current skills live? Colin notes uncertainty: "I don't know if we have push permissions or whatever on that."
