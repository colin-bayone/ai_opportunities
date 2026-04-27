# 16 - Team Prep Call: Week Deliverables and Communication Strategy

**Source:** /cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/cicd-team-monday-pre-meeting_01_formatted.txt
**Source Date:** 2026-04-27 (Monday team pre-meeting, 15:15-15:45 PST, 75 minutes before the 1pm Srinivas sync)
**Document Set:** 16 (BayOne team prep call before the Monday Srinivas meeting)
**Pass:** Focused deep dive on Colin's framing of the week's scope and the GitHub plus chat communication infrastructure he is standing up

---

## Meeting framing and opening posture

- Colin opens by saying today will be "a quicker one for us, just because it's been the weekend, so nothing too crazy has happened."
- The agenda he sets: (1) walk through what the team will tell Srinivas Pitta on the 1pm call, (2) plan actions for the week.
- Colin's framing on Srinivas: "nothing's happened over the weekend for Srinivas" — i.e., no new directives or blocker resolutions came in over the weekend.
- Colin states he has already produced a one-pager for Srinivas describing what the team has to do for the coming week.

---

## PART A: Week's deliverables and scope

### A1. The one-pager and how Colin will deliver scope going forward

- Colin: "What I've done is I've put together kind of the one-pager for him as to what we had to do for this coming week."
- For today, Colin will present the items verbally.
- Going forward: "for our team, I'm going to be putting those in a GitHub repository. So you will want to keep an eye out for that."
- He will publish the items on BOTH BayOne GitHub and Cisco GitHub. Rationale and rules detailed in Part B below.

### A2. Top-line: this is "a pretty simple week" (Colin's framing)

- Colin: "Right now, for this week, it's a pretty simple week for us."
- The deliverables decompose into: (1) the CI/CD application deployment (the big Friday target), (2) Namita Mane's log analysis track (research, NOT a Friday deliverable), and (3) the cluster of blockers/clarifications that gate item 1 (ADS, language model access, WebEx bot deployment process).

### A3. The CI/CD application deployment — the big Friday target

Colin's exact phrasing: "number one is this CI/CD application deployment. What this is, is this is effectively a combination of two different things."

**Component 1 — Static FAQ from Srikar Madarapu's skill output (the static mapping):**
- Srikar's skill produced "a mapping of issues" by running over the historical data.
- Colin: "what Cerny Bus [Cisco] wants from this is an FAQ bot, effectively. So when someone asks a question in that chat, if that question has already been answered in the past, or if there's some deterministic easy answer for it, we would give that answer back."
- "Now the static part, the mapping is right there. So we have to think about how we want to do this. And that's something that's going to be one of the assignment issues to have ready for tomorrow."
- Time pressure: "we have to work kind of quick, because we only have until Friday to deliver this."

**Component 2 — Dynamic mapping via CAT MCP integration (the four tools):**
- Colin: "The second part of it is the more dynamic mapping, so to query using that Cat MCP integration. And that's essentially the dynamic mapping."
- "If there's an issue and we need to retrieve something that's from the cat MCP server using one of the four tools, it would be expected that whatever bot we create for WebEx is able to do that too."
- The WebEx bot must have BOTH: "the known mapping that we already come up with, as a kind of a static resource, and it would also have ability to access that cat MCP. So two sides, similar thing."
- Colin labels this "the big deployment target for the week."

**Srikar's update on CAT MCP investigation (from Friday):**
- Srikar: "I looked into that cat MCP on Friday, so I have to put a document on the chat." He looked into the MCP and it has "four other tools, 4 tools total."
- Critical gap Srikar identified: "usually in the chats we are getting like PR number, like PRID, we are not getting any cat ID for getting the details. So we have to have a like mapping table where we have cat ID and PRID mapping" — only then can the MCP be queried for the latest details of that PR and the bot can respond back.
- Srikar reports he created "a skill for issue responder and like MCP or like the cat MCP." He asks Colin to refer to the document on the BayOne IT CICD automation chat for the entire flow.
- Colin's call-to-action for Srikar: get this document committed to the branch before the 1pm call. (Confirmed done by end of meeting — see A6.)
- Colin proposes to use Codex with a playbook to put the CAT MCP through its paces: "are we even able to do the proper querying of cat using that MCP given how the issues come into the chat?"

### A4. Namita's log analysis track — explicitly NOT a Friday deliverable

- Colin: "separate from that is the log analysis stuff."
- Reference back to Friday: "for the log analysis side of the house, in Namita, we talked for a while on Friday about how to do that mapping for PR commit attribution and how to trace through that."
- Concrete cutoff: "the research for that should be finished up before the end of today so that we can move forward with that this week."
- Status framing: "as of right now, there's not a deliverable item for that this week. It is an ongoing piece of work that will help to boost the rest of the project."
- Re-allocation plan once the research wraps: "Once we get that done, I want to switch over to your energy helping on with this Cat MCP and bot deployment."

### A5. Blockers Colin will surface on the 1pm Srinivas call (gating items)

These are the items gating the Friday deliverable. Colin walks through each as a "blocker" to raise with Srinivas.

**Blocker 1 — Permanent ADS machine availability:**
- Colin has a call set up with Mahaveer Jinka later today. "We're going to get to the bottom of this one, and I'm going to just get Anand Singh in the loop, whatever the outcome is, because we're getting 30 different directions from Srinivas and none of it makes sense."
- Recap of contradictions: Srinivas told them to "put in the request for the ADS machine and then you'll just need a tenant. Did that. Never happened." Then Mahaveer was blamed (and "technically should have done that, or at least given clear direction"), but Mahaveer just sent back temp ADS instructions.
- Colin's revelation from Friday: "What's happening right now is they don't have any permanent ADS machines available. That was said by Srinivas on Friday. So how the heck is Mahaveer supposed to provision something of which he has none?"
- Colin's framing for the call: "that's on you guys. That's not on us anymore. Unless you are explicitly saying that that is something that we are able to resolve without actual intervention from Cisco IT." "If they're out of servers, that's an impossible deliverable."
- Fallback Colin will propose: work to a temporary ADS machine.
- Open question on temp ADS limits: Colin asked Srinivas about compute limits on temp ADS; Srinivas said yes there are limits. Colin's interpretation: "each part of the organization is allocated some level of compute across all temp ADS machines... when you're requesting a new machine and you go through those drop-downs, that probably is subtracting allocation from somewhere somehow." Implication: "we can't do anything super heavy on those ADS."
- Colin's hard ultimatum for the call: "if he says no, wait for the permanent, then I'm going to say it has to be ready by tomorrow [Tuesday] for the permanent ADS or else this is not possible to deliver this week. We can't even test it."

**Blocker 2 — Language model access / DeepSight cascade:**
- Setup: Rui Guo's bot used the Circuit API credentials. Srinivas flagged that as "improper in some way."
- Colin's read: "I think those credentials are really just for testing out different things. You know, they're probably very limited on how many tokens they have."
- The cascade Colin lays out: "he's the one that has to grant the language model access... In order to get the language model access, he needs a DeepSight instance. DeepSight instance needs an EDS [ADS] server. So it's a cascade."
- Concession Colin will propose: "do this with either a temp ADS machine, if DeepSight can get deployed on that, or just continue to use Circuit API and plan to switch it out whenever the time comes."
- The critical open question for the call: "even if we spin up DeepSight, even if we get the ADS machine, do we then have language model access? Or what is the path to that? That is a critical thing because that gates pretty much every item on this sheet. How is the AI team supposed to work without language models?"
- Colin's anti-Wednesday-surprise framing: "I don't want it to come to like Wednesday and he's like, so where are you guys at? And I'm like, hey, man, there's still blockers that we surfaced that you haven't addressed. And he's like, no, you haven't."

**Blocker 3 — WebEx bot deployment process and identity / service account:**
- Saurav Kumar Mishra raises the issue first: "I don't think they want us to deploy the bot from our ID... I can code the back end of the bot, but the details which will where the bot will be hosted most likely should come from them."
- Saurav's continuity concern: "Suppose I deploy this model using my Saurav at the rate Cisco account and tomorrow I leave the organization or we are off to another project or somehow that account got suspended. I am on to a new account. That bot deployment is gone."
- Saurav: they need access token, bot name, bot ID. Back end can run in a Podman container, but "to deploy these things also like fall under their bed [bid]."
- Colin's response: "this is exactly what we should harp on today. Even if it ****** him off, at this point, it doesn't matter, because we're going to get dinged if we have a deliverable that we didn't speak up on."
- Colin: "I don't want to even get off that call until this is kind of clear and resolved by them... If he wants us to do it in like POC mode with personal, that's fine. But if he's expecting something productionalized, you know, with a zero day run, you know, lead time on it, that's crazy."
- Colin to team: "definitely don't feel shy to raise it up on the call, even if it makes things uncomfortable. I'm going to be right there too. I'm going to be blowing on the same trumpet because he needs to be fair with that. It doesn't make sense to ask someone to deploy something if you haven't given them literally anything to deploy with."

**Bot deployment specifics from Saurav (the architecture as he knows it):**
- "When it was on my local, it was in a Podman container which I can host normally, but when we are going to deploy it, I think he needs that on a permanent ADS machine, the back end one."
- "The front end part which is registered with WebEx, there we need to put in like the bot name, the bot ID, as well as the token."
- "These things are being put... into the .env file or however he wants to manage that."
- "I don't think they have a proper way to deploy it right now" (referring to API keys for the LLM as well).

**Bot registration / Cisco bot registry process:**
- Saurav: "everyone can deploy a bot. Whoever has like a Cisco ID and a VPN connected, he can go ahead and deploy his own bot."
- "The only thing after deploying the bot is get that bot registered with the Cisco bot registry. We have a form over there. You have to fill in the form with the details... I am deploying this bot, these are like what the bot is going to do, and this is from my ID."
- "Then they will audit and approve the whole bot... Plus, you have to also tell them on what channels and all of those details, like where exactly you want the bot to be deployed. And they will audit all those details, make sure that the bot is compliant. And then if everything passed, they will add you to that registry."
- Critical caveat (Saurav): "But it is still deployed from my ID, not from like an org level. So if tomorrow Saurav at the rate Cisco is down for some reason, like they have disconnected that after we are done with the project, that whole thing... the bot, the registry itself will be gone."
- New data point: Saurav got a mail today saying "your bot is not compliant." Mahaveer was on CC for that mail. Saurav forwarded the mail to Colin and shared the bot registration portal link in the group chat.
- Open question Saurav can't answer yet: when the audit happens, are they reviewing only the form submissions or actual code? Saurav: "That I'm not clear like, but yeah, because I did not submit for the audit yet. My system got down and I never ran the bot again."
- Colin's framing for the call: "if the bot's not compliant, there's no way for it to get deployed by Friday. And whenever we say compliant, there needs to be some kind of compliance to be compliant with. So they need to share that. So we can flag that as an item for Srinivas today."
- Colin's deliverable boundary statement: "it's not gated on us, it's gated on IT review. So on our end, we can say that ours will be ready, but we can't say deployed because deployment depends on things beyond us, which is that IT audit, review, and acceptance."
- Service account framing: "they need that service account. That's the best way to do that."
- Colin's plan for today: "I'll at least say that I'm going to try to register a bot on the portal. I'll say that's one of the pending items today. And I will flag that we need to talk about the ID under which it's deployed when we go today. I'll put that as one of the blockers."

### A6. Skills repository placement — the two-repo confusion (decision reached)

- Colin recalls Srinivas had directed skills to land in two different places on different occasions: once in the CICD repository, once on "one website... share it on that repo" (Saurav confirms).
- Colin's first instinct was: "let's put it on both and just call it a day... we can just take the exact same code. I know it's not correct to do."
- He notes the existing branch: "I think there is a branch called skills/webex. I think, Saurav, that's where all your skills are at." Colin will share the link in the WebEx chat and asks Srikar to put his skills there too.
- Saurav pushes back with a cleaner framing: "I was thinking like for the current use, we should keep them on like CICD. And once we have finalized and like tested them enough, then we can go to that other repo and posted there... that's why I did not add or else it would fall on our part to like maintain both of them."
- Colin agrees and adopts Saurav's framing: "Yes, actually, I like that framing. Let's keep that framing. We'll only put them on that repository for CICD in that branch. We don't have to worry about two places. I'm going to frame it to him exactly like that today. The finished skills that have been tested and verified will go into that master skills repo whenever they are fully done."
- End-of-meeting confirmation from Srikar: "I just added all the annex categorizer, as well as the issue responder skill, which has like other four, like 3 placeholders, and along with the one cat cat MCP." Colin confirms he sees all of them on the branch.
- Colin: "I'm going to add those in as some of the deliverables that are completed. I'm just going to frame them as completed."
- Saurav clarifies remaining work: "we have to like code the whole back end to make sure that everything inside the CICD as well as the skills are also taken into account for the bot. So in a way that is kind of still a deliverable for us for the end of the week. And for them it's like getting the bot details for the front end."

### A7. Final integration piece — the WebEx delivery mechanism itself

Colin's summary of what makes the application work:
1. The ADS machine
2. The language model
3. The connection to the MCP
4. The static mapping of issues for the static FAQ
5. The WebEx integration (the actual delivery mechanism)

Colin: "All those things working independently, it's still not an application. It has to be deployed somewhere somehow."

Open question Colin will pose: "What do we need to do to deploy a WebEx bot? Are we able to use something local? Whenever he says deployed, this is where I need kind of some feedback from all of you as to, you know, if we wanted to deploy a WebEx bot on Podman."

This rolls directly into Saurav's deployment specifics captured in A5 / Blocker 3.

---

## PART B: GitHub issue tracking infrastructure

### B1. Two repositories, by design

- Colin will publish weekly deliverables and tracking issues on BOTH BayOne GitHub and Cisco GitHub.
- "BayOne GitHub is just meant to be a read-only tracker. So that's where you can put in anything that, you know, it's not for code to go. Do not try to commit any code to it."
- Purpose of BayOne GitHub: "It's just a way to communicate the issues to everyone and stay on track here. You can put in comments, you can put in questions on that one to the issues that you're assigned."

### B2. Rationale for two repos (the separation principle)

- Colin: "The reason why I'm doing both is not to confuse everyone, but just so that there's a clear separation for Cisco. Because there's some things that obviously you don't want to have visible to them that you might have a question about from an issue perspective or feedback we might have."
- Internally tracked vs. Cisco-visible: BayOne GitHub holds the questions/feedback the team does not want visible to Cisco; Cisco GitHub holds the assigned-work view.

### B3. The hard rule (engagement rule reminder)

- Colin: "Remember, don't access BayOne GitHub from the Cisco laptop. That's one of the rules."
- Allowed access surfaces for BayOne GitHub: phone, BayOne laptop. NOT Cisco laptop.
- "The equivalent issue will be there on the Cisco repo."

### B4. Cisco-side repo setup (today's action)

- Colin: "I'll be setting up a repository for the team or using one of the existing ones so that we can assign the work."
- Purpose: "so that we have a clear path as to what progress is being made throughout the week and clear deliverables and timelines for it."
- Timing: "I'll be putting that on today."

### B5. Markdown deliverables live on the GitHub page

- Colin's closing action: "what I'm going to do is I'm going to update this sheet based upon everything we talked about now. I'll share this with everyone. I'm going to put it on the GitHub page itself. So these markdown files, just so that we can keep track of them, will be available on the GitHub page itself."
- Use on the 1pm call: "That's what we'll go through on the call to keep it nice and simple."
- Implication for Srinivas: he can track the one-pager and the blocker tracking directly on the GitHub page rather than in chat or email.

---

## PART C: "Be annoying" communication cadence

### C1. The strategy in Colin's words

- "Basically, I just want us to be as proactive as possible. At this point, my advice is to be annoying. Be annoying."
- Channel: "in the chat, I'm going to just keep on raising things." (The CICD WG / working group chat.)
- Citation of Srinivas's own stated preference: "he said repeatedly that, you know, if anything comes up as a blocker, surface it early and often in the chat. I'm going to do exactly that."

### C2. The cadence — start of day and end of day

- "Every start of the day, I'm going to flag these if they're not resolved. At the end of every day, I'm going to flag them again if they're not resolved."
- Volume target: "at minimum, there will be 10 messages from me this week in that CICD WG chat that everyone can see."

### C3. The strategic intent — "not on us"

- Colin: "Because I want this to be clear that this is not on us for a lot of these. These are just things that Srinivas is asking kind of, you know, loaded cannon not aiming anywhere, any particular direction."
- Tied directly to the deliverable boundary work in Part A5: separating what BayOne can deliver (back end, skills, integration code) from what is gated by Cisco IT (ADS provisioning, language model access, bot registry approval, service account).
- This is the paper trail. The visible chat messages demonstrate that BayOne flagged the gating items in real time, so when Friday arrives without a fully-deployed bot, the cause is documented in chat and not attributable to BayOne.

### C4. The Rui Guo precedent (the "process clearly works" lever)

- Colin: "the big thing here is that with Rui, his own chat bot that he made for WebEx, they already have one. So clearly there is some process that can work. And the question then becomes, you know, how do we do the same?"
- This is the reference point Colin will use to argue the deployment path is not theoretical — Rui Guo already walked it. The question is purely how BayOne replicates it without the same internal-Cisco identity that Rui has.

### C5. Why this matters now (renewal-window stakes)

- Although the renewal window is not named explicitly in this transcript segment, the entire posture is consistent with it: Colin is willing to make Srinivas uncomfortable on the call ("Even if it ****** him off, at this point, it doesn't matter") because the worse outcome is "we're going to get dinged if we have a deliverable that we didn't speak up on."
- The cadence (10+ messages, start-of-day and end-of-day blocker flags) is specifically engineered to make sure that at the end of the week, the unresolved items are visibly Cisco's, not BayOne's.

---

## Open questions and unresolved points carried into the 1pm Srinivas call

1. Permanent ADS: do they actually have one to give? If not, is temp ADS acceptable as the deploy target? If permanent, can it be ready by Tuesday end-of-day or Friday is at risk?
2. Language model access path: even with DeepSight on an ADS, does the team get LLM access? Until then, is Circuit API allowed as a stopgap?
3. WebEx bot deployment identity: who owns the bot's deploying ID? Is there a service account, or is the expectation that a BayOne contractor's personal Cisco ID will host a "production" bot?
4. Cisco bot compliance criteria: what does "not compliant" mean? Where is the compliance specification documented?
5. Skills repo placement: confirm with Srinivas that during-development skills live in the CICD repo (skills/webex branch) and only finished/tested skills migrate to the master skills repo.
6. CAT MCP querying: can the four MCP tools actually be queried correctly given that chat events surface PR IDs but not CAT IDs? The PR-ID-to-CAT-ID mapping table is a prerequisite Srikar has flagged.

---

## Immediate actions assigned during this prep call

- Srikar Madarapu: get the issue responder skill and CAT MCP skill committed to the skills/webex branch before the 1pm call. (Confirmed done by end of meeting — categorizer, issue responder with three placeholders, plus CAT MCP skill all on the branch.)
- Saurav Kumar Mishra: forward the "bot not compliant" mail to Colin and share the Cisco bot registration portal link in the group chat. (Confirmed done during the meeting.)
- Colin Moore: meet with Mahaveer Jinka later today to get to the bottom of the ADS contradictions and loop Anand Singh in on the outcome.
- Colin Moore: stand up the team's Cisco-side repository today and the parallel BayOne read-only tracker; publish the updated one-pager as a markdown file on the GitHub page; share the link to the team.
- Colin Moore: try to register a bot on the Cisco bot portal himself today as a pending item to discuss on the call.
- Colin Moore: drive the 1pm call to resolution on the WebEx bot deployment ID question — "I don't want to even get off that call until this is kind of clear and resolved by them."

---

## Meeting close

- Colin: "There's a meeting coming up in 15 minutes that I need to jump off for." (Implies this prep call ran ~15:15-15:45 PST window with a 1pm Srinivas sync to follow approximately 75-90 minutes later.)
- Colin closes: "we'll wrap up now, and I'll see you all in just shy of an hour and 15 minutes."
- Attendees on the call: Colin Moore, Saurav Kumar Mishra, Srikar Madarapu, Namita Ravikiran Mane.
