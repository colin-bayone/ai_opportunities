# 16 - Srinivas Sync: WebEx Agentic Proxy Long-Term Architecture Vision

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on Srinivas's CICD-app-as-single-pane-of-glass long-term vision, the WebEx-as-proxy architecture, the WebEx LLM access reality (Srinivas hedged, Colin confirmed agentic capability now exists), and the parallel two-team experiment framing

---

## 1. Why this section matters

This portion of the meeting (timestamps roughly 00:44:33 through 00:56:42) represents a material shift in scope. The prep deliverable Colin walked through (`weekly_status_2026-04-27_v3_table.md`) framed the engagement as a shared-backend chat assistant feeding two surfaces: the chat in the CI/CD application and the WebEx bot on the NX-OS CI pipeline. Both surfaces were treated as relatively coequal frontends sharing one backend.

Srinivas, in this segment, recasts that relationship. The CI/CD application, deployed on each user's own ADS server through DeepSight bring-your-own-compute, is the long-term single pane of glass for engineers. The WebEx bot is reframed as a near-term mitigation for users who already live in WebEx, and ultimately as a proxy / middleman that tunnels chat between the user's WebEx workspace and the user's own CI/CD application instance running on their own ADS server.

This was not in the prep deliverable. It opens a new architectural direction that BayOne is now expected to study, document, and prototype in parallel with another internal Cisco team that is already experimenting on the same pattern.

---

## 2. The two-product framing Srinivas opened with

The segment begins with Colin asking a clarifying question about whether something Srinivas asked Justin to do was tied to a different WebEx chat. Srinivas redirects with an explicit two-product framing.

**Direct quote (Srinivas):**
> "See, the end of the day, Webex you need to understand there are two products we are talking. Maybe we are interleaving that's why little confusion is there. One is the Webex interface. We are helping the user that if there is some issue. What is the problem, right? I mean, how they can resolve it through the MCP server behind the scene. So one thing, what you want to do is, to the Webex bot, can we attach an MCP? You need to first figure that out. Okay. If you cannot."

Decomposition of the two products:

1. **The WebEx interface (near-term mitigation surface).** Helps users who are already in WebEx resolve issues through MCP server queries running behind the scenes. This is the surface BayOne is deploying to on Friday (the static FAQ plus CAT MCP integration described in the prep deliverable).
2. **The CI/CD application (long-term destination).** The full front-end application for all engineers going forward. Single pane of glass, deployed per-user on each user's own ADS server via DeepSight, with role-based UI and full LLM and MCP integration.

Srinivas explicitly acknowledges that the conversation up to this point had been interleaving the two, which is why there had been confusion about which surface a given requirement applied to. The implicit instruction is that BayOne should keep these two products mentally separate going forward.

The first technical task he hands BayOne in this framing: figure out whether an MCP can be attached directly to the WebEx bot. If the answer is no, then the only path to MCP-backed assistance is the CI/CD application route, which makes the CI/CD application even more central.

---

## 3. Srinivas's hedge on WebEx LLM access ("minus six months knowledge, backdated")

Immediately after the two-product framing, Srinivas made a claim about WebEx's LLM capability and explicitly hedged it.

**Direct quote (Srinivas):**
> "The only way where those MCPs can be embedded is our CI / CD app on the the one that you are working on, the repo. Because WebEx board doesn't have LLM access. It is just a some kind of a query and just reply right, how the query comes in with a LLM and all they don't have the full LLM integration at least. As far as I understand, maybe you guys can maybe the, I mean minus six months knowledge okay back dated. So in the recent past, I don't know if AWS has provided some capability, but Either way, The CI CD app will be the full front end app for all the engineers going forward."

Three things to extract here:

1. **The claim:** WebEx bots do not have LLM access; they are query-and-reply only, without full LLM integration.
2. **The hedge:** Srinivas explicitly self-flagged his knowledge as "minus six months, backdated" and invited BayOne to correct him if a capability had landed in the recent past. ("AWS" in this passage is almost certainly a transcription artifact for "WebEx" given the context; flagging as ambiguous but treating as WebEx.)
3. **The fallback conclusion that survives either way:** Even if WebEx now has LLM integration, the CI/CD application is still the long-term destination. The hedge does not change the strategic direction; it only changes the near-term tactical options for what can run inside the WebEx bot itself.

This hedge is the opening for Colin's correction in the next beat.

---

## 4. Colin's correction: WebEx now supports agentic apps with LLM integration

Colin took the opening Srinivas offered and corrected the record on the current state of WebEx capability.

**Direct quote (Colin):**
> "Okay, and I think I. There's one thing, So I had the team kind of look into what the capability for WebEx looked like because there's there's a lot. And you probably know better than I do. It's a little bit fragmented for the documentation, so we've been trying to pull from everywhere and kind of get organized ourselves, so we know the capability. I think and sorry if you can correct me if I'm wrong here. I think we did find that they do now support. Um, agentic apps on Webex. So there is language model integrations now. Um. We we can share those docs, but I understood understood either way."

Key points:

- BayOne's team has already done a survey of current WebEx bot / app capability documentation.
- Colin flags that the documentation is fragmented across sources, which is why his confidence is qualified ("I think").
- The conclusion BayOne arrived at: WebEx now supports agentic apps and language model integrations are available.
- Colin offers to share the supporting documentation with Srinivas.
- Colin closes with "but I understood understood either way," acknowledging that even if the capability exists, Srinivas's strategic direction (CI/CD application as the long-term home) still holds.

Srinivas's response: "Okay, yeah, just take a look. So one one thing for example right let's say." He neither rejected nor over-fitted to the correction. He immediately pivoted to walking through how the CI/CD application would work, which is consistent with his "either way the CI/CD app is the destination" framing.

**Important note for BayOne's record:** This is the correction on the WebEx capability question. BayOne's prior internal understanding had this backwards. The current correct position is: WebEx does now support agentic apps with LLM integration. The supporting documentation will be shared with Srinivas as a follow-up.

---

## 5. The CI/CD application architecture, walked through live

Srinivas screen-shared the DeepSight CI/CD application as a live example of the architecture he was describing. The walkthrough started awkwardly (he initially opened the wrong application: "Oh, this does not have the chat unless I upload it. Okay. It's the wrong application. One second, I think this should be ready") and then he found the correct app.

### 5.1 Per-app chat with user-selected model

**Direct quote (Srinivas):**
> "Here, right when the user registered their Deepset application. Every app has their own chat. In your case, CACD will have its own chart. Okay, So of course in the chat we'll we'll pre cook some of these things. Uh even for you for the, but like a quick answers that user want, whatever it is right. But the idea is this, when the user asks a question, we are asking the user to pick whatever the model choice that you have. Right? What is offered on the Deepset platform. So we support Copilot Codex models, okay? And of course the circuit is also there. We'll also add cursor and other stuff later on. Let's ignore that piece."

Architectural points:

- Every DeepSight-registered application gets its own chat surface.
- The CI/CD application will have its own chat tab.
- The chat will be pre-seeded ("pre-cooked") with quick answers for common user requests. (BayOne's static FAQ work fits naturally as one source of pre-seeded content.)
- The user picks which language model to use per-question from a list of models offered on the DeepSight platform.
- Models supported today: Copilot, Codex, Circuit. ("co-pilot codex" in the transcript is the speech-to-text rendering of "Copilot, Codex" as two separate model options.)
- Models on the future roadmap: Cursor, and "other stuff later on."
- For this conversation Srinivas explicitly de-scopes the model-list discussion ("Let's ignore that piece") and uses Copilot / Codex as the example for the rest of the walkthrough.

### 5.2 Single pane of glass for CI/CD, with role-based views

**Direct quote (Srinivas):**
> "If I pick a co-pilot codex model, I can ask a question here. Now I want to, and this will be a single what you call. pane of glass for the CA series. Let's say if you use a CA series app, there may be some static or dynamic, we'll create some graphs. Or based on the role of the engineer, like engineer manager, release lead, probably will have different pains here. But from the user point of view, There'll be a user clickable tab where user can get glance information, or he can also chat dynamically with the data because that will pull in the MCP information and do whatever he wants."

Architectural points:

- The CI/CD application is the single pane of glass for the CI/CD pipeline experience.
- The application surfaces both static and dynamic graphs (visualizations) above and beyond the chat.
- The application is role-aware. Different roles get different views ("pains" / panes):
  - Engineer
  - Manager
  - Release lead
- Each role probably gets a different pane configuration. Srinivas hedged with "probably," which suggests the role-based UI is a design intent rather than a fully scoped requirement.
- From the user's perspective there are two interaction modes inside the app:
  1. A clickable tab for at-a-glance information (graphs, status views).
  2. A dynamic chat against the underlying data, which pulls in MCP information and executes whatever the user asks.

### 5.3 Bring-your-own-compute via DeepSight, deployed on each user's own ADS server

**Direct quote (Srinivas):**
> "Now this is right now deployed on my AD server. Because DeepSIEM allows to bring your own compute. So I attached my host on the deep side, which is my AD server, and I launched this app on my. On my A D server, right."

Architectural points:

- DeepSight supports bring-your-own-compute. A user attaches their own host to the DeepSight platform and DeepSight launches the application on that host.
- Srinivas's instance of the CI/CD application is currently running on his own ADS server, which he attached to DeepSight as his compute.
- The implication for engagement design: the long-term deployment model is per-user, not centralized. Each engineer runs their own instance of the CI/CD application on their own ADS server, attached to DeepSight as their compute.
- This is the same ADS pattern BayOne has been blocked on for the engagement (the team's Permanent ADS request from April 14 referenced in the prep deliverable). The engagement's ADS dependency is therefore not just an environment-availability issue. It is the same compute pattern that the long-term per-user architecture relies on.

### 5.4 Per-user-credential model

**Direct quote (Srinivas):**
> "But now assume that, and now when he's chatting, he's using his own LLM access, right? His own credentials. What have we picked up? Of course, there's always a default."

Architectural points:

- Each user authenticates against the language model with their own credentials. This is consistent with Srinivas's note in section 5.1 that the user picks the model for each question; the credential follows the user's selection.
- There is a default option if the user does not pick. Srinivas did not specify what the default is, but the implication is that the platform handles the fallback transparently.
- This is a meaningful design point for BayOne's WebEx-side work: any proxy architecture has to carry the user's identity / credential context end to end so the right LLM is invoked under the right account.

### 5.5 The MCPs the chat hooks into

**Direct quote (Srinivas):**
> "And this chart has, we are hope we hope that assume that we hook this chart. To both static and dynamic data, Meaning the the NXOS SAN - IT MCP, that is there that is there as a part of CACD. The whatever the PR data that Justin is going to give you, and the CATMCP everything is hooked up behind it. Okay, assume that. That means user is able to, through a single chat, this thing he should be able to say, 'Hey where is my PR stuck?' Okay. Can you unstuck through this or whatever? He can use some actions: get status or whatever thing."

MCPs and data sources hooked up behind the CI/CD application chat:

| Source | Type | Notes |
|---|---|---|
| NX-OS sanity MCP | Static and dynamic | Already part of the CI/CD application stack. (Transcribed as "NXOS SAN - IT MCP," which is the NX-OS sanity MCP per project context.) |
| PR data MongoDB | Dynamic | The PR data Justin's team has been collecting from GitHub events into MongoDB. To be exposed to BayOne via read-only access through a generic user ID per the earlier portion of the same meeting. |
| CAT MCP | Dynamic | The Cisco internal MCP that surfaces CAT request data including PR mapping, branch, submitter, and bug ID, per Anupma's walkthrough earlier in the meeting. |

The user experience at the chat layer collapses these into a single conversation. Sample user intents Srinivas called out:

- "Where is my PR stuck?" (status query, dynamic)
- "Can you unstuck through this?" (action query, dynamic)
- "Get status" (action call against the underlying tools)

---

## 6. The proxy / middleman architecture between WebEx and the CI/CD application

Having walked through the CI/CD application as the destination, Srinivas pivoted to the cross-product question: how does a user interact with their own CI/CD application from their phone, when they are not at their laptop? His answer is the proxy architecture.

### 6.1 The full statement of the proxy vision

**Direct quote (Srinivas):**
> "Now I'm on my phone or a web page. Ideally, when I chat through my WebEx. On my phone, I should be able to send the same message to my app running on my A D S server. That essentially means if I run a webex agent on this app also. Whenever this app is launched, I should be able to send a message from my workspace. To my own, what you call, uh, ADS server. Which has access to all alarm everything running."

> "Right, and what are the response you get from this chat? You should be able to again stream back to my webex space. That essentially mean me and my application running on AD. Server are part of one bot space, like a unique thing. I'm not saying it is a Requirement of government, but I am saying eventually we will get there. So while you are studying the web accelerator, because you are saying you are documenting studying right. I'm just telling you this will be one more requirement where, how can a user. From the Webex space, chat with his own what you call application. which is running on his own AD server."

Architectural decomposition:

1. **Initiator:** The user, on their phone (or any web page), inside their WebEx workspace.
2. **Inbound leg:** The user sends a chat message in WebEx. That message has to be relayed to the user's own CI/CD application running on the user's own ADS server.
3. **Per-app WebEx agent:** Each launched instance of the CI/CD application also runs a WebEx agent component. The application is therefore both a chat client (consuming MCPs and LLM) and a WebEx-aware listener (receiving relayed messages from the user's WebEx space).
4. **Backend execution:** The user's CI/CD application receives the relayed message, executes the chat against the LLM and MCPs the user is authorized for, and produces a response.
5. **Outbound leg:** The response streams back from the user's application to the user's WebEx space.
6. **Identity model:** The user and the user's application instance are part of one shared bot space, like a unique two-party channel. The bot is essentially a private bridge unique to that user-application pair.

Srinivas explicitly noted "I'm not saying it is a Requirement of government, but I am saying eventually we will get there." Read in context, "government" appears to be a transcription rendering of "go-now-ment" / "right now"; the intent is clearly "this is not a today requirement, but it is a direction we will reach." It is a forward-looking design constraint that BayOne should bake into the WebEx capability study, not a Friday deliverable.

The phrase "while you are studying the web accelerator, because you are saying you are documenting studying" ties this back to BayOne's documentation work on WebEx capability. Srinivas is asking BayOne to fold the proxy use case into the same study.

### 6.2 Colin's clarifying summary and Srinivas's confirmation

**Direct quote (Colin):**
> "Right, so it's essentially like a proxy connection."

**Direct quote (Srinivas):**
> "It's a proxy exactly, and they are just chatting with each other and getting a response. I'm the middleman basically. Understood, yeah."

This is the canonical name for the pattern in the conversation: the proxy connection. Srinivas confirmed Colin's framing verbatim, explicitly calling himself the middleman. The user is the human in the middle, and the WebEx bot is the proxy carrier between WebEx and the user's CI/CD application instance.

### 6.3 Why LLM in the WebEx bot is not required under this pattern

**Direct quote (Srinivas):**
> "You got that thing right, because this will have access to LLM when I in the WebEx bot. I mean, in the bot, I don't need access LLM. But there is a central. It is like a like a remote. Host right, and you are just chatting with the remote host. And that guy is doing all the heavy lifting and just getting the response. So we should have a Ubox agent here running, which is calling the API. Backend API get the answer and streaming back to the user."

Architectural conclusion: under the proxy pattern, the WebEx bot itself does not need LLM access. The LLM access lives in the CI/CD application running on the user's ADS server. The WebEx bot is a thin relay. It calls the application's backend API, retrieves the response, and streams it back to the user's WebEx space.

This reconciles Srinivas's earlier hedge about WebEx LLM access (section 3) with Colin's correction (section 4): even if WebEx now supports agentic apps with LLM integration, the proxy pattern does not depend on it. The pattern works whether or not the bot has its own LLM.

"Ubox agent" in the transcript is the WebEx bot agent (transcription artifact).

---

## 7. The on-the-go user experience

Srinivas closed the architectural sketch by grounding it in the user value proposition.

**Direct quote (Srinivas):**
> "It's you got the requirement. That means essentially, what we are telling is that. You are able to now debug your PR issues on the go. Meaning you don't have to sit in front of your laptop... You raise a PR, you go get on the train or a bus, then you monitor your PR on the Webex page on your phone. And you can take actions, whatever you want to do. That's the idea."

User journey decomposition:

1. Engineer raises a PR at their desk.
2. Engineer leaves the laptop, gets on the train or bus.
3. Engineer continues to monitor the PR through their WebEx app on their phone.
4. Through the proxy, the WebEx phone surface routes through to the engineer's own CI/CD application instance on their own ADS server.
5. The engineer can take actions on their PR from the phone, not just observe state.

The strategic value is that engineering productivity is no longer tied to laptop time. PR debugging becomes asynchronous and mobile.

---

## 8. Cloud Code = Claude Code: the BayOne analog Colin referenced

Colin connected the requirement to BayOne's own internal practice using a parallel from the BayOne tooling stack. The transcript renders "Claude Code" as "Cloud Code" throughout this exchange.

**Direct quote (Colin):**
> "Yes, yes. Let let me look into it and and I'll also share. I I don't think it's there yet for Codex. I know that it's there for Cloud Code because we do this at Bay One. But there's something now for cloud code that's essentially called remote control that does exactly this natively. I'm wondering if that's going to be on the roadmap for Codex. So this could be even easier in the future. That does not mean that it circumvents what you're saying at all. But, that means that at least I don't know if people have ah like the chat G P T apps on their phone for for Cisco. But there might eventually be a native interface there, just to flag that to you. But it doesn't exist today."

Decomposition:

- "Cloud Code" in the transcript is **Claude Code**, the Anthropic CLI / agent tooling that BayOne uses internally. Treat every transcript reference to "Cloud Code" or "cloud code" in this exchange as Claude Code.
- Claude Code has a feature, in this exchange called "remote control," that natively does the same proxy / remote-host chat pattern Srinivas just described. BayOne uses this internally at BayOne ("we do this at Bay One").
- The same capability does not exist today for Codex (the OpenAI agent tooling that DeepSight surfaces as one of its model options).
- Colin speculated that the Codex roadmap may eventually include this natively, in which case the integration becomes much easier.
- Colin also noted that he does not know whether Cisco engineers have the ChatGPT mobile app deployed on their phones, but if they did and if Codex shipped a native equivalent of Claude Code's remote control, there might eventually be a native phone interface for the same workflow.
- Important caveat Colin added: this analog does not replace what Srinivas is asking for. The proxy requirement still stands. The Claude Code reference is provided as a nearby existing pattern to study, not as a substitute deliverable.

**Srinivas's response (direct quote):**
> "That's okay. When all that comes, we'll move to that interface. But for now. I want to be able to engineers to use their Cobalt's interface on their mobile. To chat to their what you call service running on their Redis server. It's like one to one."

Decomposition:

- Srinivas explicitly accepts that if and when native interfaces (Codex on phone, ChatGPT app, Claude Code remote control on Cisco devices) become available, Cisco will move to those interfaces.
- Until then, the requirement stands: engineers should use their **Codex** interface (transcribed as "Cobalt's") on their mobile to chat to their **CI/CD application service** running on their own **ADS server** (transcribed as "Redis server").
- The interaction model is one-to-one between the engineer and their own application instance.

---

## 9. Strategic angle: business-user enablement

Colin folded a strategic upside into the discussion before Srinivas closed the segment.

**Direct quote (Colin):**
> "Yes, and and from my angle, just from a strategic standpoint, it's good because if you do this, you're also enabling business users too. If people don't agree."

Decomposition:

- The proxy pattern's value is not limited to engineers. Business users (non-engineering Cisco staff) gain the same on-the-go access pattern.
- This positions the work as a platform-level capability rather than a CI/CD-only feature.
- The trailing fragment "If people don't agree" is incomplete in the transcript and reads like the start of a follow-on thought that did not finish; record the strategic point as the load-bearing content.

This is consistent with Colin's broader engagement strategy: anchor BayOne's work as platform infrastructure that has reach beyond the immediate CI/CD use case.

---

## 10. The two-team parallel experiment framing

Srinivas closed the segment by revealing that BayOne is not the only team being asked to crack this pattern.

**Direct quote (Srinivas):**
> "Basically it's on the go. I want to enable DeepSet on the go. And we are experimenting since you are also studying. I am giving the same requirement to you. So which our two teams are working in parallel. Whichever teams come first, we'll take it. The solutions."

Decomposition:

- Strategic objective: enable DeepSight on the go.
- Another Cisco-internal team is already experimenting on the same proxy pattern in other applications.
- Srinivas is now giving the same requirement to BayOne, in parallel.
- The two teams are independent. There is no coordination requirement called out.
- The selection rule is explicit and competitive: whichever team produces a working solution first, Srinivas will take that solution as the path forward.

This is a soft race. The other team has a head start (they were already experimenting). BayOne enters with the WebEx capability research already underway (per Colin's correction in section 4) and with prior experience with the analogous Claude Code remote control pattern (per section 8).

**Direct quote (Colin):**
> "We'll sprint fast then."

Decomposition:

- Colin commits BayOne to fast pace in response to the parallel-team framing.
- This is a verbal commitment, not a written one. It does not specify a timeline or deliverable beyond pace.
- It signals to Srinivas that BayOne understands the competitive dynamic and is willing to play.

---

## 11. BayOne's research and documentation actions out of this segment

The segment created a set of research and documentation obligations for BayOne. They are not all explicitly enumerated by Srinivas, but they fall out of the conversation.

| Action | Driver |
|---|---|
| Confirm and share the WebEx agentic-apps and language-model-integration documentation with Srinivas. | Colin offered: "We we can share those docs." Srinivas accepted: "Okay, yeah, just take a look." |
| Continue the WebEx capability study (the "web accelerator" study Srinivas referenced) and explicitly fold the proxy use case into it. | Srinivas: "while you are studying the web accelerator, because you are saying you are documenting studying right. I'm just telling you this will be one more requirement." |
| Investigate whether an MCP can be attached directly to the WebEx bot. | Srinivas: "to the Webex bot, can we attach an MCP? You need to first figure that out. Okay. If you cannot." |
| Document the proxy pattern: WebEx bot relays user messages from WebEx to the user's CI/CD application instance on the user's ADS server, application executes against LLM and MCPs under the user's credentials, response streams back to the user's WebEx space. | Falls out of section 6. |
| Track Codex roadmap for a native equivalent of Claude Code's remote control feature, since that would simplify or replace part of the proxy stack. | Colin's commitment: "Let let me look into it and and I'll also share." |
| Sprint fast against the other Cisco-internal team running the same experiment in parallel. | Colin: "We'll sprint fast then." |

---

## 12. How this changes the engagement scope versus the prep deliverable

The prep deliverable Colin walked through framed the engagement as:

- One backend.
- Two coequal frontends: chat in the CI/CD application and the WebEx bot on the NX-OS CI pipeline.
- Friday deliverable: static FAQ wiring plus CAT MCP integration into both surfaces, sharing the backend.

After this segment, the engagement has the additional dimension of:

- The CI/CD application is **not** a coequal frontend with the WebEx bot. It is the long-term destination, deployed per-user on each user's own ADS server via DeepSight bring-your-own-compute.
- The WebEx bot in the long term becomes a thin proxy relaying user messages between the user's WebEx workspace and the user's own CI/CD application instance. The bot does not need to host LLM or MCP access itself in this model.
- The Friday deliverable scope (static FAQ plus CAT MCP into the WebEx bot on the NX-OS CI pipeline) does not change. It is positioned as near-term mitigation for users already in WebEx.
- A new research and documentation track is now expected, in parallel with the Friday deliverable, covering:
  - The proxy pattern (WebEx bot to user's ADS-hosted CI/CD application).
  - Whether an MCP can attach directly to a WebEx bot.
  - The current state of WebEx agentic-app and LLM-integration capability.
  - Roadmap implications from Codex potentially shipping a Claude-Code-style remote control.
- BayOne is competing in parallel with another Cisco-internal team on this research and prototyping track. Whichever team produces a working solution first wins the path forward.

This is the new architectural direction that was not in the prep deliverable. It should be reflected in the next iteration of the weekly status and in any forward-looking architecture documents BayOne produces.

---

## 13. Open questions to track

The segment leaves a set of open questions that should be carried forward:

1. **Can an MCP attach directly to a WebEx bot, given the current state of WebEx agentic-app capability?** Srinivas asked BayOne to figure this out. The answer determines whether MCPs can run inside the bot, or whether the proxy pattern is the only path to MCP-backed assistance.
2. **What is the WebEx agentic-app feature surface today?** BayOne's research says agentic apps and LLM integrations are now supported. The detailed capability surface (tool calling, streaming, identity propagation, persistent state) needs to be documented.
3. **What does the per-user ADS deployment of the CI/CD application look like operationally?** Each engineer has their own ADS server attached as DeepSight compute, running their own application instance, holding their own LLM credentials. The provisioning, credential, and lifecycle pattern at scale needs to be understood.
4. **How does identity flow end to end through the proxy?** The user is in WebEx on a phone. The bot relays into the user's own application instance. The application invokes the LLM under the user's credentials. The full identity propagation chain needs to be traced.
5. **What is the other Cisco-internal team's progress on the proxy pattern, and is there a coordination point?** Srinivas framed the two teams as parallel and competitive. There may still be value in a periodic compare-notes touchpoint to avoid duplicated dead-ends.
6. **Will Codex ship a native remote-control equivalent of Claude Code's, and on what timeline?** This is a roadmap-watching item. If it lands, it changes the long-term architecture.
7. **Do Cisco engineers have ChatGPT or equivalent mobile apps deployed?** Colin flagged this as unknown. The answer affects whether a native client surface is even possible as an end state.

---

## 14. Summary

The CI/CD application, deployed per-user on each engineer's own ADS server through DeepSight bring-your-own-compute, is Srinivas's long-term single pane of glass for the CI/CD pipeline experience. It hosts a per-app chat with user-selected models (Copilot, Codex, Circuit today; Cursor and others later), per-user credentials, role-based UI for engineers, managers, and release leads, and direct access to the NX-OS sanity MCP, the PR data MongoDB, and the CAT MCP.

The WebEx bot in the long term becomes a proxy. The user, on their phone, chats inside their WebEx workspace. The bot relays the message to the user's own CI/CD application on their own ADS server. The application executes the chat against the LLM and MCPs under the user's credentials. The response streams back to the user's WebEx space. The user and the application share a unique two-party bot space. The bot itself does not need LLM access; the application does.

Srinivas hedged on whether WebEx supports LLM integration, calling his own knowledge "minus six months, backdated." Colin corrected the record: BayOne's research finds that WebEx now supports agentic apps with language model integration. The supporting documentation will be shared. Either way, Srinivas's strategic direction stands; the CI/CD application is the destination.

Colin referenced Claude Code's "remote control" feature as the BayOne analog of the pattern. Cisco does not have a native equivalent for Codex today, but if it ships, the long-term architecture becomes simpler.

Two Cisco-internal teams are now running parallel experiments on the proxy pattern: another team that started earlier, and BayOne starting now. Srinivas will take whichever team's solution lands first. Colin committed BayOne to sprint fast.

This is a new architectural direction not captured in the Monday prep deliverable. BayOne's deliverables for the week should continue to focus on the Friday static FAQ plus CAT MCP work for the WebEx bot on the NX-OS CI pipeline, while a parallel research track on the proxy pattern, the WebEx agentic-app capability surface, and direct MCP attachment to WebEx bots is opened immediately.
