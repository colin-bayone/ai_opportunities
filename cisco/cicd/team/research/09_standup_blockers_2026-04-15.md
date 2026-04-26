# 09 - Standup: Blockers, Dependencies, and Escalations

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/week_2026-04-14/day_2026-04-15/cisco-cicd-team-standup-wednesday-session_01.txt
**Source Date:** 2026-04-15 (Wednesday afternoon PDT / evening IST, 60-minute team standup)
**Document Set:** 09 (Wednesday team standup without Colin, Saurav leading)
**Pass:** Focused deep dive on blockers, dependencies, and escalations

---

## State of Blockers Entering Wednesday

The Wednesday afternoon team standup ran without Colin (he was on another call and would pick up the transcript later with Srikar and Namita). Saurav led the session and applied the escalation cadence established in Set 07: Wednesday is the latest day to surface blockers to Srinivas ahead of the Friday deliverable. Entering this meeting, the team carried three unresolved access blockers (DCN Switching tenant ID, DeepSight code-level GitHub access to the Pulse and Scribbler repos, Saurav's dead Cisco MacBook), and the Friday deliverable depth was already gated on the Pulse and Scribbler architectural visibility that those access grants would unlock. Over the course of the standup, the team also surfaced several new architectural and code-reality findings that shift what the Friday deliverable can honestly claim. Vaishali was present but effectively silent (one "no, not good" at the very end when Saurav prompted her by name).

## Access Blockers

| Blocker | Impact | Owner | Plan for Today | Escalation Path |
|---------|--------|-------|----------------|-----------------|
| DCN Switching tenant ID not reflecting in portal | Cannot select the tenant ID when creating a permanent ADS machine request; permanent ADS machine is blocked. Team is working from the temporary ADS (4-week lease) in the meantime. | Namita | Wait until Wednesday afternoon India time for the portal to reflect Mahaveer's approval. If still not reflected, re-ping Mahaveer and follow up with Anupma (who has not replied to prior ping). | Namita to discuss with Colin on the later-today 1:1; Colin then escalates to Srinivas. Namita: "obviously, we will tell Colin and, so maybe he can ask Srinivas or we can ask Srinivas something on those lines." |
| DeepSight code-level GitHub access (Pulse and Scribbler repos) | Cannot inspect Pulse implementation for Friday architecture diagram; cannot run A/B testing on Scribbler without Scribbler access. Gating Friday Srinivas deliverable depth. | Srikar | Srikar pinged Naga on Apr 14; Naga redirected him to Srinivas for approval. Colin also pinged Srinivas yesterday, no reply. Srikar to connect with Colin after this call so Colin can try Srinivas again. | Colin to Srinivas. Fallback: if repo access does not come through in time, ask Naga or Justin for a sample transcript file that has already been processed by Scribbler's Whisper model, which is sufficient for the A/B testing workaround (Issue 3.1). Saurav: "at least we ask for it and we can flag it that we asked and you never gave us access." |
| Saurav's Cisco MacBook dead since Tuesday evening | No access to GitHub repos, no access to Cisco subscriptions, only WebEx chat on phone. Podman container with the Wall-E bot is on the dead machine, so the bot cannot be demoed to Srinivas on Friday. Saurav's deliverable work is largely blocked; "most of the work is for Srikar and Namita" for today and tomorrow. | Saurav | Saurav in regular contact with Cisco tech support; hopeful a replacement laptop arrives Thursday Apr 16. Workaround: reachable via WebEx on phone and Teams on BayOne laptop. | Already escalated earlier Wednesday (Set 08 morning 1:1 with Colin): Colin forwarding Saurav's fact-driven email to Srinivas and Anand, with a BayOne-buys-Mac-under-SAL fallback if no resolution within one week. |

## Architectural Blockers

### Pulse and Scribbler Are Not Deployed Anywhere (Newly Clarified)

Srikar confirmed in this meeting what had only been suspected in Set 07: the Pulse and Scribbler repositories live under the DeepSight GitHub org, but neither has been deployed to the DeepSight platform, and no one is actually using either on DeepSight. Srikar: "they haven't deployed anything or they haven't been using anything on the deep side, so right now those two projects are in GitHub itself, like they haven't been like deployed." Saurav's reply: "Yeah, it is not deployed, so how can anyone use it?"

Saurav then walked the logic all the way through: Pulse is supposed to scrape everything and put it in a database. If Pulse were production, Cisco could hand BayOne a dataset and say "do exploratory data analysis on this table." The fact that Cisco is asking BayOne to build the scraper plus the analysis proves Pulse is not production. Saurav: "they should have already integrated that to the NX OS CICD group. Okay, they should not be asking us to do this job and then do exploratory data analysis, they can just share the details like this is the table or this is the database which has all the access and you can go ahead and do a EDA on this." This closes a live scope question about Pulse overlap with BayOne's Task 1 scraping work.

### Duplicate-Scraping Architecture (Saurav's Observation)

Saurav surfaced a structural problem with the DeepSight self-service model as currently understood: if every user runs Pulse locally, and every user is in the same team chat, the same chat data gets scraped into N separate databases (where N is the number of users in the team chat). Saurav: "If I am running it on my end and you are running or Namita and every all four of us are running the same thing, it will scrape it four time and save it in four DB." For the NX OS CICD team alone, that is four-plus duplicates of the same chat data in four-plus separate databases.

Srikar agreed immediately: "we have to like make it only once and then show it to all four." Saurav's proposed architecture response is a shared service layer: scrape once into a shared database, then use OAuth-token-backed MCP servers with row-level filtering so that each user only sees data for spaces and rooms they already have access to via their Cisco ID. This becomes the backbone of the architecture diagram deliverable for Friday: modular data sources, a shared ingestion and storage layer, MCP servers with OAuth token verification, and swappable consumer bots on top.

### DCN Tools Repo Agentic Hygiene Gaps (Newly Observed)

While Saurav still had laptop access earlier in the week, he inspected the DCN tools repo and found it running "bare bones":

- No agent.md file at the repo root (Codex would look for this as its memory file, equivalent to Claude's CLAUDE.md)
- No plugins, no prehooks, no skills defined
- No README
- A build_error_analysis.md file exists, but Namita pointed out it is under a prompt folder, not at the repo root. Saurav confirmed this is not serving the agent.md function: "that is totally different, right? Yeah, it should be named agent.md in case of using Codex to be run as like a memory for that."

Implication: the DCN tools team is running Codex without any of the modern agentic hygiene. This is a low-effort, high-output improvement opportunity BayOne can offer: add an agent.md file, add skills that teach the LLM how to read log files and use deterministic scripts, so the LLM has more of the picture rather than only the regex-extracted failed labels and BEP dependency graph excerpts.

### Retry-Mechanism Ambiguity (Unresolved After This Meeting)

The meeting surfaced a disagreement between Saurav's and Namita's reads of the DCN tools retry loop that was not resolved in the meeting and needs deeper inspection.

- **Saurav's read:** the tool applies the LLM's fix, runs the build, and if the build passes, captures the git diff and sends the diff to the user as notification. Essentially fix + build + diff.
- **Namita's read:** "no, I do not think they are fixing it. They are just sending it, right? I don't think they fix it." Namita: "I mean, it is sending the diff, so it is correcting it, it is correcting the error, but the build won't start on its own until the user" runs it. Essentially diff only.
- **Srikar's read:** aligned with Namita: "they are not like making any changes, changes in the code part, like just like identifying the issues and sending that."

Saurav's structural pushback: if the tool is not running the build and not applying anything, how can it tell whether its first-pass fix was correct, and how can the three-retry loop be a real retry? Saurav: "if it is not running the build or doing any kind of testing, okay, like not applying anything as you are saying, then how is it able to tell like if it was correct or not and then go for a retry?" He concluded the team needs eyes on the repo: "just confirm this if this is correct or not."

Either Saurav's read or Namita's read could be correct, or the truth could be a combination (Saurav: "it is a combination of both"). If Namita's read holds, then the "retry" is not iterative in any meaningful sense; the LLM sees its own first-pass output and reasons about it statically without any runtime feedback signal, which is architecturally weaker. Namita flagged as an open question whether the retry is happening at the LLM analysis stage or the log-fetch stage. Srikar noted this is a good question for Justin. [unclear in transcript whether the team will raise this with Justin on the upcoming code walkthrough call or will answer it internally from the code first.]

## CI vs CD Code Reality

This is the largest single substantive finding of the meeting, and it cuts against Justin Joseph's verbal claim that DCN tools "handles everything."

Namita performed a code-level review of the DCN tools repo and found:

- Logs are generated from two different places, and those locations are different: CD logs and CI logs (Bazel dev builds).
- The code is "mainly focused on the CD part. That is where, that is the location they are looking for the logs. They are not looking anything for CI."
- Namita asked Justin directly about this. Justin's claim: "no, it handles everything."
- Namita's assessment of Justin's claim: "as per his saying, it is kind of half true because it can handle CD part, not a problem. But the CI part how he's handling is if you give that log path manually through command line, then it is able to fetch it."
- So in practice: CD logs are fetched automatically via the coded log path. CI logs require the user to pass the log path manually through the command line for the tool to do its analysis.
- Nothing is in production. Justin said the handoff to production for the CD side would be "just one button click" to turn on the Airflow DAG, but as of now nothing is deployed to production.

This reinforces Colin's Set 07 observation about the 70/30 split: roughly 70% of Cisco verbal claims are accurate, 30% are misremembered or misstated. Justin's "handles everything" sits squarely in the 30%. The team now has the specific technical detail to back this up: CI auto-discovery is not implemented, manual log-path passing is the current workaround, and the claimed "one button click" path to production is CD-only.

This finding has two implications for the Friday deliverable:

1. BayOne's scope for Task 3 (build failure analysis) involves CI (Bazel dev builds) per the engagement charter. The existing DCN tools code does not actually cover CI auto-discovery, which means BayOne's work is genuinely incremental rather than duplicative.
2. The verbal-versus-code gap reinforces the Set 07 discipline that BayOne must verify every Cisco verbal claim at the code level before adopting it into the architecture. Namita's code review is the template.

## Hardware Blocker Update

Saurav's laptop remains dead since Tuesday evening. Saurav reported on the Cisco tech support call a systemic detail worth carrying into team-level risk: "all of us guys, the laptops which we had receiving, all of these are refurbished laptops." Saurav: "it is good that you did not get an issue, but yeah, do use them with care."

Counterpoint data during the meeting: Srikar updated his Mac mid-meeting and reported no issue. "I just updated my system, so yeah, I did not see any issue. It worked." This keeps the refurbished-laptop risk real but non-deterministic. Saurav, Namita, and Vaishali all remain on identical contractor refurbished hardware and carry the same latent risk. Colin's preemptive SAL-purchase contingency from Set 08 remains the right insurance policy at the team level.

Saurav also ruled out the Wall-E bot as the cause of his laptop failure when Srikar asked: "nope, nope, nope, like, because, like, it was running on a Podman container, okay, and Podman container itself is done." The Wall-E bot artifact is stranded on the dead machine along with the Podman container. Demo-to-Srinivas on Friday is now screen-share-only at best, with existing transcripts and outputs.

## Political Dynamics

### Integration-Not-Replacement Framing (Saurav Coaching the Team)

Saurav, unprompted and applying Colin's Set 07 coaching, explicitly guided the team on how to frame BayOne's architecture relative to Cisco's existing work: "we can incorporate that into our architecture as well, so that it does not look like that we are like just putting aside all the work they have done and coming up with something from totally from our end, rather than integrating their work and building upon that."

This is Colin's Set 07 diplomatic framing propagating into the team-level operating posture. The Pulse-not-in-production finding gives BayOne leverage to push a proper shared-service architecture, but that leverage has to be applied diplomatically; the presentation on Friday needs to read as "building upon Pulse and Scribbler" rather than "Pulse and Scribbler do not actually exist in production so we are replacing them." The architecture diagram Saurav drafted in Claude reflects this: Pulse and Scribbler appear as data sources that feed into the shared ingestion and storage layer, not as modules to be discarded.

### Data Flow Discipline

Saurav also reinforced Set 07 data-handling rules to Namita when she asked about transferring documents between machines: "always remember this is one way, never from Cisco to Baven, only from Baven to Cisco." And on Claude Code usage: "I don't think we are supposed to use that on what you call Cisco laptop, so yeah, keep that in mind." Namita: "yeah, yeah, definitely, definitely, yes." This keeps Claude Code confined to BayOne machines and makes the air-gap direction crisp: BayOne to Cisco yes, Cisco to BayOne no.

### Due Diligence Discipline

Saurav called out that even when Cisco counterparts say a tool works, BayOne must verify: "even if they say that, yeah, this is working fine, it can do 90, 99% of the work properly. Once we get like the repo access, we have to confirm. Did he say what he said? Is the tool doing like exactly what he said he is doing? Or is there like any kind of miscommunication here?" This is the Set 07 verify-before-trust discipline, now propagated into the team's operating norms.

## Changes Since Set 08 (Morning 1:1)

Set 08 was the Wednesday morning 1:1 between Colin and Saurav that set up the laptop escalation plan to Srinivas and Anand. Between Set 08 and this Wednesday afternoon team standup, the following blockers shifted:

- **Laptop escalation:** unchanged from Set 08. Saurav is still on phone-only WebEx and a BayOne laptop for Teams. Colin's forwarded escalation to Srinivas and Anand is in motion; no reply yet captured in this transcript. Saurav remains "hopeful" of a replacement tomorrow (Thursday Apr 16).
- **DCN Switching tenant ID:** no portal reflection yet; 48-plus hours since Mahaveer's approval. Namita added a plan: wait until Wednesday afternoon her time, then escalate to Colin for a Srinivas ask. Anupma still has not replied to Namita's earlier ping.
- **DeepSight code-level access (Pulse and Scribbler):** Srikar's Naga ping on Apr 14 was redirected to Srinivas. Colin's ping to Srinivas yesterday got no reply per Srikar. Still blocked, still gating Friday deliverable depth. Workaround identified: a single sample Scribbler-processed transcript file from Naga or Justin would unblock the A/B testing on Issue 3.1 even without repo access.
- **New findings (all surfaced in this meeting, not in Set 08):** Pulse and Scribbler are not deployed on DeepSight at all; DCN tools repo is missing agent.md, skills, plugins, README; Justin's "handles everything" claim is half true (CD-only auto-discovery, CI requires manual log path); the retry-mechanism reading disagreement between Saurav and Namita. All four are net-new material for Colin's later-today 1:1 with Namita and Srikar and for any Wednesday-evening escalation to Srinivas.

## Carry-Forward Items for Colin's Later-Today 1:1

The meeting closed with Saurav explicitly noting that Colin would pick up these items in the later-today 1:1 with Srikar and Namita. The items that matter for that handoff:

1. DCN Switching tenant ID portal reflection (Namita), escalate to Srinivas if still not reflected by Namita's Wednesday afternoon.
2. DeepSight code-level GitHub access for Pulse and Scribbler (Srikar), Colin to re-ping Srinivas; sample-transcript fallback if repo access does not materialize.
3. Pulse-not-in-production finding, needs diplomatic framing for Friday deliverable.
4. CI vs CD code-reality finding from Namita, strengthens BayOne's incremental-scope claim for Task 3.
5. Retry-mechanism read disagreement, needs deeper code dive before Friday; good question for Justin on the upcoming walkthrough call.
6. DCN tools agentic hygiene gaps (agent.md, skills, README), low-effort high-output addition that BayOne can contribute.
7. Saurav's laptop status, Thursday is the hoped-for replacement date; Friday demo now screen-share-only at best.
