# 07 - Standup: Blockers, Dependencies, and Escalations

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/internal_team_meet_4-13-2026.txt
**Source Date:** 2026-04-13 (Monday team plan for the week)
**Document Set:** 07 (Internal BayOne team planning meeting following the April 10 Srinivas call)
**Pass:** Focused deep dive on blockers, dependencies, escalations, and political dynamics

---

## State of Blockers Entering the Week of April 13

The BayOne team entered the week of April 13 still gated on most of the access and tooling that would make meaningful Cisco-side engineering possible. The Friday April 10 call with Srinivas Pitta had clarified scope on two points (Bazel-only, not Gmake; parallel build of WebEx transcription through Scribbler is permitted rather than required to depend on Pulse), but it had also surfaced that several of the access problems the team assumed would resolve after the first round of requests had not. As of Monday morning:

- Namita was the only team member with functional GitHub Enterprise (A2G) visibility sufficient to see Justin's code. Everyone else who had received an A2G grant was seeing "access granted" but no repositories visible.
- Saurav's Wall-E bot had been flagged by Cisco IT as non-compliant under the internal bot policy.
- No one on the team had confirmed access to DeepSight, nor to the Pulse or Scribbler repositories.
- Vaishali was still without Cisco hardware and was explicitly excluded from this week's tool requests.
- The team had decided, informally, to continue using Claude Code covertly on Cisco machines because Codex and Copilot access had not yet been granted.

Colin's framing at the start of the meeting was that Monday was the day to raise access requests, Tuesday was the day to verify and to assign GitHub tasks to specific owners, and Wednesday was the latest possible day to flag any still-blocking items to Srinivas so he had time in the week to unblock them.

---

## Access Blockers

| Blocker | Impact | Owner | Escalation path | Status |
|---------|--------|-------|-----------------|--------|
| Codex access on Cisco machines | No approved AI coding assistant; team is covertly using Claude Code and self-censoring in meetings | Each individual with Cisco hardware (Srikar, Saurav, Namita) | Srinivas via appstore.cisco.com workflow; Colin will push for Codex minimum | Ongoing. Request to be submitted this week. Saurav has not submitted because he has not received Copilot or Codex yet and is avoiding AI-generated artifacts that would reveal usage. |
| GitHub Copilot access | Same as above | Team | appstore.cisco.com request | Ongoing. Request to be submitted this week. |
| GitHub Enterprise (A2G) effective access beyond the grant | Grant arrives but no repositories are visible; second step requires pinging Justin after the A2G grant to receive actual repo visibility | Saurav and Srikar (Namita has completed both steps) | Justin, then Srinivas | Partial. Namita resolved via the PDF instruction she had shared Friday. Saurav and Srikar both saw "access granted" but see no repos. Next step: ping Justin per Namita's walkthrough. |
| Aurora Development Server (ADS) permanent provisioning | Temporary ADS in place for 4-week lease; need to clarify whether one shared ADS serves the whole team (Linux/RHEL allows concurrent sessions) or whether each track needs its own | Namita for logs track; Srikar and Saurav for WebEx track | Justin confirmed single ADS is fine for multi-user Linux; Colin confirmed this depends on OS | Partial. Justin has told Namita a single shared ADS works. Concurrency confirmed viable if the machine is RHEL or Debian based (not Windows). Permanent bundle still pending. |
| DeepSight platform access | Cannot access the DeepSight environment that Srinivas himself owns. Without DeepSight there is no access to Scribbler (Naga's Whisper tool) and no ability to do the A/B test against WebEx transcription | Whole team; Colin owns escalation | Srinivas; Colin to re-ping with the post-meeting summary | Ongoing. Colin committed in this meeting to ping Srinivas again with the Friday meeting summary, framing the ask as "we need Scribbler access to do the A/B test, and that should come through DeepSight in the same stroke." |
| Scribbler repository access on DeepSight | Without the repo we cannot see whether Scribbler is production, a POC, or a local Python script; cannot A/B test against WebEx transcription | Srikar (lead for WebEx/transcription track) | Srinivas (explicitly committed to unblock), then Naga directly | Ongoing. Srinivas said on Friday he would unblock. Colin will continue to push. |
| Pulse repository access | Cannot evaluate whether Naga and Justin have already built the WebEx scraping layer the team is proposing; creates scope duplication risk | Srikar | Srinivas, Naga, Justin | Ongoing. Same gate as Scribbler. |
| Docker Desktop on Cisco machines | Requires a Cisco IT admin-level approval (macOS/Windows admin permission required); Podman is available without access request but Docker Desktop is behind an access flow | Saurav identified; all team members with Cisco hardware | Cisco IT admin; route via Srinivas if blocked | New this week. Colin's guidance is to request it and to frame the ask to Srinivas as "local dev to unblock ourselves" so that it does not read as going around IT. |
| Codex/Copilot as an interim AI coding tool | Saurav is deliberately not using either because of the bot compliance issue and because he has not received access; Claude Code is being used covertly | Colin for escalation path | Srinivas | Ongoing. Colin will keep pushing on Srinivas for "minimum Codex" given that Codex, although not as good as Claude Code, is "way better than Copilot." |

---

## Compliance Blockers

Saurav raised a compliance issue that surfaced after he deployed his Wall-E bot prototype on Cisco infrastructure. The Cisco IT team sent him an email flagging the bot as non-compliant and directing him to a nested set of policy documents (bot policy referencing internet policy referencing two or three additional policies). Two specific rules emerged from his reading of the policies:

1. **Bot registration.** Any bot deployed on Cisco must be registered with the organization and submitted for thorough review. This is a formal pre-deployment step, not a post-hoc notification.
2. **Group size rule (<100 users).** When the bot is under development, the group it operates within must be fewer than 100 users and more than two users. This directly conflicts with the Cisco NX-OS group, which has more than 300 users. Saurav flagged this as something that Cisco would have to adjust for its own internal use cases (the rule cannot be honored as written if the target group is more than 100 users).

**Implications the team needs to carry into architecture:**

- The OAuth model Saurav proposed (surface only data the end user has access to; do not surface everything using the bot's own token) is the right defensive posture. Bot tokens have broad access to chats and spaces, and Saurav flagged that using the bot's own token rather than the user's OAuth would risk leaking data across channels the user should not see.
- The service-layer design (scraper -> database -> MCP -> consumer apps or bots) is compatible with the compliance constraints only if OAuth passthrough is enforced at the MCP boundary.
- Before the team presents this to Srinivas, Colin's guidance was to frame it as: "I can show you this, but there is some policy around bots. Help me navigate that." The tone is to push the policy question back to Cisco rather than absorb it.

---

## Knowledge Blockers

The team does not yet have the ground-truth information needed to commit to a log-processing architecture for the CI/CD track. Specifically:

- **CI versus CD log structure is not yet known.** Namita has access to Bazel logs in the dev environment, which represent the CI pipeline Justin has shown her. The CD process (nightly builds) is a different pipeline that Justin has not walked her through. Srinivas on Friday framed the overall project as covering both. Namita committed in this meeting to get information on the CD side this week.
- **Composite versus individual log files is unknown.** Colin's specific concern: the log file for a nightly build could be a single large text file that blends output from multiple applications, or it could be a collection of individual per-application log files. The downstream processing strategy (parsing, chunking, MCP tool design) depends entirely on this. The team cannot design the architecture diagram for Friday without eyes on actual log samples.
- **Log storage location and access pattern is unclear.** Justin indicated logs are on an NFS (network file system) server. Whether the team can get read-only NFS access (which would allow local Airflow-driven downloads over VPN) or whether access is gated to portal downloads is not yet confirmed.
- **Traceability from build to commit is not captured at Cisco today.** Srinivas stated on Friday that the current pipeline does not carry commit-level traceability. Colin noted this was actively harder to achieve than to skip, and flagged it as a design target for Namita's data model work (star schema, SHA hash as the key, lineage computed on demand through MCP rather than persisted).
- **Sample quality is not trustworthy.** Colin's guidance: any log sample Justin hands over should be treated as suspect. "Anytime you have someone who is not an AI person give you a sample of data, you can 100% guarantee it is not going to be a good sample." The team needs its own sampling window, not a curated file from Justin.
- **No visibility into the nightly build cadence yet.** Namita noted the dev environment had no recent failures in the past four days, so the team has only passing logs to work with. A longer observation window is required to see variation.
- **WebEx scraping scope is not documented on Cisco's side.** Saurav explicitly flagged that WebEx offers integrations, service apps, bots, Agentic apps, and OAuth flows, and that the team does not yet know which surface Naga and Justin are building against or whether they have already provisioned bot registrations and access tokens.
- **Scribbler runtime model is unclear.** Srikar clarified in this meeting that Scribbler is not wired to any Cisco meeting system. It runs locally, requires the user to provide an audio file, and is not a deployed service. This is knowledge the team did not have entering the week, and it materially changes how to present the A/B test.

---

## Scope and Duplication Risk Blockers

Two scope-overlap risks were discussed in detail:

**1. Naga's Scribbler overlaps with BayOne's proposed WebEx transcription work.**
Srikar confirmed that Scribbler is from Naga, not from Justin, and that it is not connected to any Cisco meeting system. It is a local Python script that wraps Whisper. Saurav initially suggested the team grab Friday's meeting transcript from Scribbler so the A/B test could start without repo access, but Srikar then clarified that Scribbler has no configuration for any meeting and can only be run locally against a pre-downloaded audio file. This means:

- There is no running Scribbler output to borrow from.
- The A/B test requires first getting Scribbler to run (requires DeepSight access, repo access, and possibly API keys which Saurav has not seen documented anywhere).
- The team cannot yet confirm what Scribbler's end state is supposed to be. Srinivas indicated on Friday that Scribbler and the WebEx MCP/transcription work can proceed in parallel and do not need to depend on each other, but that parallelism only holds if both sides are real; if Scribbler is a 50-line local Python script then there is not really a parallel track, there is a POC and a proposed production system.

**2. Pulse may duplicate the WebEx scraping architecture Saurav is proposing.**
Saurav's architectural proposal (decouple scraping from consumer bots by building a scraper -> database -> MCP -> app or bot stack) may already be partially built by Naga or Justin under the name Pulse. Saurav's concern, in his own words: "if this is something they have already done, they completed, he would be like, why are you duplicating the work?" Colin's specific guidance on how to handle this:

- Confirm with Naga and Justin what is built.
- Do not accept a verbal confirmation that it exists. Ask to see it. Colin: "even if they say that we have it, do not take that as the answer. Say, like, I need to understand it, I need to see it. Because very, very, very, very commonly people say that stuff, and then you look and it is this hacked together thing."
- Whether what they have is good or bad, the move is the same: record the meeting, then generate an architecture diagram showing what they have. If it is bad, generate a second architecture diagram showing BayOne's proposed alternative and present them side by side. Do not verbally critique the existing work.

**3. Duplicated processing at runtime.**
Colin flagged a third scope risk that is not about team politics but about compute waste: if Srikar builds a WebEx-meetings-to-transcripts app using Whisper and Saurav builds a separate app that also needs transcripts, and both spin up their own DeepSight pods to process the same meeting audio, Cisco is paying twice for the same compute. This is the argument for the unified service-layer approach and will be part of what the team raises to Srinivas as an architectural consideration.

---

## Hardware Blocker

Vaishali still does not have Cisco hardware. Colin explicitly excluded her from this week's tool requests: "Vaishali, do not worry. You are still waiting on hardware, so just ignore this part." She is not named in any of the appstore.cisco.com requests (Codex, Copilot, Podman, Docker Desktop, A2G) that the rest of the team is submitting this week.

**Implications:**

- Vaishali's log-processing work is gated on Namita sharing downloaded log samples. Colin's explicit framing: once Namita has NFS access and can pull logs locally, "Vaishali can work kind of async with you, Namita, to help to process those and transfer."
- Vaishali can still contribute to the architecture document and the presentation deliverables this week because those are BayOne-machine deliverables, not Cisco-machine deliverables.
- There is no explicit escalation path called out in this meeting for the hardware delay itself; it is outside the scope of what Srinivas is asked to resolve and is implicitly a BayOne operations issue.

---

## Tool Usage Blockers

**Covert Claude Code use.**
Colin stated plainly that he has Claude Code installed on his Cisco machine and intends to keep using it: "technically no one knows if you are or are not using Cloud Code. I mean, I have mine personally installed on the Cisco machine. So just do not say a word about that in a meeting, and I will not know any better. No one will know any better." The guidance to the team:

- If you have Claude Code installed, use it, but never say the name in a meeting with Srinivas or any other Cisco stakeholder.
- Saurav explicitly chose not to install Claude Code for now because the documents it generates have a structure that reads as AI-generated, which would reveal usage in the absence of an approved tool. He is waiting on Copilot or Codex access.
- Colin: "Just be very careful then."

**Codex and Copilot access pending.**
Both requests are to be submitted this week through appstore.cisco.com by each team member with Cisco hardware. Colin will push Srinivas for "minimum Codex" as the acceptable approved tool. Copilot is considered the fallback, and Colin described Codex as "not as good as Cloud Code, but at least it is way better than Copilot."

**Podman is available without a request.**
Saurav confirmed Podman does not require an access request and can be downloaded directly from the redirect link. Podman is tightly integrated with the DeepSight/ADS deployment flow, which is why it is pre-approved. Docker Desktop is not, because of licensing implications.

**Docker Desktop preferred for local POC work.**
Colin's position is that for POC work, Docker Desktop is worth the access-request friction because the team can spin up arbitrary services locally (databases in particular) to unblock themselves without waiting on Cisco-managed infrastructure. Colin specifically cited "you can already tell from that meeting that database access is going to be challenging" as the reason to have local container capability.

---

## Political and Diplomatic Dynamics

The central political dynamic this week is how to raise the Scribbler-is-a-toy-POC framing to Srinivas without putting Naga on the defensive or appearing to dismiss existing Cisco work.

**Colin's core guidance on Scribbler specifically:**

- Capture the current state of Scribbler as a diagram. Do not characterize it in words as "literally just essentially a Python script that runs Whisper ... probably 50 lines of code at most." That framing is for internal BayOne use only.
- Capture what is missing around it: no observer backend, no WebEx meeting discovery, no audio pipe, no deployment, no integration. Those are architectural components, not insults.
- Present the current-state diagram and a proposed future-state diagram side by side. "Simply show it as a diagram and say, here is how it works today, here is what we suggest it works in the future, because it will naturally come out as to what the shortcomings are to any logical person that is technical."
- Do not argue about whether Naga's work is good. "You will get into an argument if you do that."

**The "you can't get your feathers ruffled" principle.**
Colin's central permission structure for the team to propose a re-architecture is that Scribbler is not yet in production. Paraphrasing his formulation: you cannot get your feathers ruffled over having your work re-architected if the work is not really working for real yet. The exact phrasing was that if Scribbler is not fully matured, "that gives us a way to put ourselves inside of it and insert and say, we are going to do this a better way, a different way, without really ruffling feathers, because you can't get your feathers ruffled if it is not really working for real yet." The team should lean on this as the diplomatic opening, framing BayOne's re-architecture as an extension of what Naga started rather than a replacement.

**The "solution without a use case" characterization.**
Internally, Colin named what he sees happening at Cisco: "what Cisco has done is they have created a solution without an actual use case, which is another way of saying I messed around at work and got paid to do it." This is explicitly an internal BayOne framing and must not leak into any external-facing document or meeting. The external framing is always a diagram of the current state and a diagram of the proposed state, with the conclusion left for the Cisco stakeholders to draw themselves.

**The "let smart people come to their own conclusions" rule.**
Colin's broader technique for dealing with Cisco stakeholders when the existing work is weak: "present the facts plainly on their face and let smart people come to their own conclusions." Do not call out the gaps explicitly; show the architecture and the logical questions will surface on their own (for example, "my computer restarted, is it running?" or "am I really going to pull the same meeting transcript down and he is going to process it on his side and I am going to process it on my side?").

**Budget pressure as a Cisco stakeholder motivator.**
Colin briefed the team on Cisco VP bonus dynamics: VPs get a material bonus for staying at or under budget, which is why Imran and others push back hard on anything that sounds like it expands compute footprint. When the team presents architecture, cost-of-compute framing (for example, "Whisper is 10% more accurate but costs $240K a year") is the lever that will actually move a Cisco VP, not quality framing alone.

**Verbal information is 70% accurate.**
Colin's explicit rule on what Naga, Justin, and other Cisco stakeholders tell the team: assume "whatever they tell you verbally will be about maybe 70% correct, and then 30% they will either have misremembered, misstated, or misrepresented per the database, not intentionally, but you know, something that is in their eyes works this way, does it actually work that way in the code?" Verbal answers are fine to work with in the short term, but every verbal claim must be verified against the code or the repo before it goes into a BayOne deliverable.

---

## Escalation Cadence

**The Wednesday rule.**
Colin set Wednesday as the latest day of the week on which the team will flag still-blocking access issues to Srinivas. Colin's exact framing: "Wednesdays will be the latest day in the week where we are going to flag still existing problems up to Srinivas. So even for tomorrow, try to do, you know, for instance, like on Namita's sheet, follow those instructions. If you are still blocked after tomorrow, that is when you can tell me and I will raise it up to Srinivas as early escalation."

The mechanics:

- Monday: raise access requests with Cisco IT (appstore.cisco.com, A2G, etc.).
- Tuesday: verify whether the access worked; follow Namita's PDF-documented "ping Justin after A2G" step for GitHub.
- Wednesday: anything still blocked is flagged to Colin; Colin escalates to Srinivas.
- Thursday to Friday: Srinivas has time in the week to actually unblock.

**Srinivas's stated preference.**
Colin noted that Srinivas himself asked for earlier-in-the-week escalation: "he was asking for earlier in the week, he wants to know if there is problems so that he can help." The Wednesday cutoff is designed to respect that preference rather than surfacing issues on Friday when Srinivas no longer has time to act.

**Escalation levels above Srinivas.**
Not explicitly discussed in this meeting, but carried forward from prior context: Anand Singh is one level above Srinivas as the Cisco exec sponsor. The team did not discuss escalating to Anand in this meeting; the April 13 framing is that Srinivas is the active escalation point for the week.

---

## Summary of Blocker Changes Since the Friday April 10 Call

Because the team's own numbered sets begin on April 10 (Set 01 team) and the prior Srinivas call is the April 10 "Set 11 main" reference, the correct chronological frame for "what changed" is Friday April 10 to Monday April 13 (over the weekend).

**New blockers discovered over the weekend and this meeting:**

- Cisco IT flagged Saurav's Wall-E bot as non-compliant. Bot registration and the <100-user rule are new compliance gates that did not exist in the team's model at end of Friday.
- A2G grant does not equal repo visibility. This was discovered Monday morning. Saurav and Srikar both see "access granted" but no repos. Namita found the second step (ping Justin post-grant) documented in the PDF she shared Friday; the rest of the team did not work through the PDF over the weekend.
- Scribbler is confirmed to be a local-only Python script with no system integration. Srikar delivered this clarification in this meeting. Before this, the team's working assumption was that Scribbler might be a running Cisco service that the BayOne team would need to integrate with or test against. It is now understood to be a POC.
- Docker Desktop was identified as an admin-gated tool on Cisco machines, while Podman is not. This was not discussed on April 10.
- CI versus CD log pipeline distinction. Namita raised this in this meeting: Justin has walked her through the CI Bazel log flow, but has not walked her through the CD nightly build flow. Srinivas on Friday framed the project as covering both, so there is now an explicit knowledge gap to close this week.
- Concurrency model of ADS machines was clarified (Linux allows concurrent users; Windows does not). This was not known on Friday and answers Saurav's direct question about whether the team needs multiple ADS machines.

**Resolved since Friday:**

- Bazel versus Gmake scope question. Srinivas confirmed on Friday that Gmake is out of scope; only Bazel logs need to be processed. This carried into Monday as a settled decision.
- Scribbler and WebEx MCP parallelism. Srinivas confirmed on Friday that Scribbler and the WebEx/transcription work can proceed in parallel and do not need to depend on each other. This remains in effect.
- Namita has functional GitHub access and can see Justin's Python script and PR history. This happened Monday morning.
- Namita has ADS access (temporary lease) and can see past Bazel logs in dev. Monday morning.

**Still open from Friday, unchanged:**

- DeepSight access for the team. Srinivas committed on Friday to unblock; Colin committed in this meeting to re-ping with the post-meeting summary and to frame Scribbler access as the lever.
- Pulse and Scribbler repo access. Same gate as DeepSight.
- Codex and Copilot access. Requests to be submitted this week through appstore.cisco.com.
- Vaishali's hardware. Not discussed in any detail; still outside the Srinivas escalation scope.
- GitHub Enterprise repo set-up for BayOne's own internal documentation at Cisco. Colin noted the team needs its own Cisco-side GitHub repo to collectively pull together documentation and reproducible code-exploration agents, and that he would keep bugging for this.

---

## Forward-Looking Items That Will Become Blockers if Not Addressed

- **No Cisco-side BayOne documentation repo exists yet.** Without one, any code-exploration work the team does (the "deep dive onto an existing repository" pattern Colin described, whether automated through a Claude Code skill or done manually) is siloed on individual machines and cannot be shared across the team. Colin flagged this as something he will continue to push on but it is not yet a named access request.
- **No approved path for BayOne to use Claude Code.** The covert-use decision is pragmatic but fragile. If any Cisco stakeholder sees a deliverable that reads as AI-generated without an approved tool behind it, the team loses credibility. Saurav's self-censorship (refusing to install Claude Code until Codex or Copilot approval arrives) is the conservative read of this risk.
- **No observation window on real logs.** Until the team has multiple days of real log snapshots, the Friday architecture deliverable Colin plans to give Srinivas will be based on inference rather than on data. This is acknowledged but not yet mitigated; the mitigation plan is "even if the logs are all passing, take a sampling so we have a library of known log files."
- **No documented path for bot compliance registration.** Saurav read the policies and did not find a clean registration workflow; the implicit plan is to push the policy question back to Srinivas rather than absorb it. If Srinivas does not help navigate, the Wall-E bot cannot move past prototype.

[unclear in transcript] The exact identity of "Imperma" or "An Purma" (the Cisco person Colin attributes the "finite pool of ADS compute" comment to) is ambiguous in the transcript. The topic map identifies this person as Anupma (CAT DB). Treat the attribution in this document as the Cisco stakeholder who raised the ADS compute-pool constraint on the Friday call, pending confirmation of the exact name.
