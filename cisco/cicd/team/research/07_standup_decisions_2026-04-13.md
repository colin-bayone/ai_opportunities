# 07 - Standup: Decisions and Rationale

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/internal_team_meet_4-13-2026.txt
**Source Date:** 2026-04-13 (Monday team plan for the week)
**Document Set:** 07 (Internal BayOne team planning meeting following the April 10 Srinivas Pitta call)
**Pass:** Focused deep dive on decisions made and rationale behind them

---

## Nature of Decisions in This Meeting

This was a Monday internal BayOne planning meeting in which Colin Moore set the operating framework for the rest of the week. Most decisions are Colin-as-lead setting direction, a smaller set are operational agreements (who teaches what, which day is the escalation cut-off), and a handful are strategic positioning choices around how to handle the gap between Cisco's existing exploratory work and BayOne's proposed architecture. The team generally aligned on the substance, with Saurav Kumar Mishra frequently validating the technical direction and Namita Ravikiran Mane contributing specific knowledge she had gathered from Justin at Cisco.

---

## Decisions

### 1. Focus exclusively on Bazel logs, ignore Gmake

- **What was decided**: The build-logs track (Namita and Vaishali) will work only on Bazel log output and will not attempt to process Gmake logs.
- **Rationale**: Srinivas Pitta explicitly confirmed this on the April 10 call. Colin noted, "with Basel, they only want us to focus on that. We can ignore Gmake. So that is one question that we finally have answered, which is good." This is one of the few questions that came back fully answered from that call.
- **Alternatives considered/rejected**: Dual-scope across both build systems. Rejected because Cisco's current-and-future direction is Bazel, and Gmake is in the legacy path they are actively moving away from. Namita checked in mid-meeting ("you are saying that we should look at Gmake logs as well right now, just for our understanding?") and Colin reaffirmed no, Gmake remains excluded.
- **Decided by**: Srinivas Pitta (Cisco), confirmed and restated by Colin as the operating rule for the team.

### 2. One shared Linux Aurora Development Server (ADS) for the team, not one per person

- **What was decided**: The team will request a single Linux Aurora Development Server (ADS) machine that multiple team members can access concurrently, rather than provisioning one per person.
- **Rationale**: Namita confirmed from Justin at Cisco that a single ADS machine supports simultaneous multi-user access. Colin added the technical reason: because ADS is Linux based (Red Hat Enterprise Linux 8 or Debian), concurrent user sessions work natively, unlike Windows virtual machines which tend to be single-session. Additionally, Imran on the Apr 10 call flagged that Cisco has a finite pool of Aurora Development Server compute across the whole organization, so subdividing wastes shared capacity.
- **Alternatives considered/rejected**: Per-person Aurora Development Servers (Saurav raised this as a question, worried about the classic VM contention pattern where "I'm working on something and Srikar wants to do his own thing"). Rejected because the Linux base removes the contention concern, and because Colin said, "As of right now, I would say no. Do not subdivide until there is a tactical production-related reason to do so."
- **Decided by**: Colin, informed by Namita's intel from Justin.

### 3. Docker Desktop is acceptable for local proof-of-concept work

- **What was decided**: Team members may install and use Docker Desktop locally on their Cisco machines for proof-of-concept work, even though Cisco's sanctioned container runtime is Podman.
- **Rationale**: Colin's reasoning was that Cisco uses Podman organization-wide because it is free and open source software, which avoids Docker licensing concerns at the enterprise scale. For local proof-of-concept work, that licensing concern does not apply. Colin: "they just use Podman because it is FOSS. So I think they are worried probably about licensing for Docker. For us, for things like POCs, it does not matter. So if you want to get Docker desktop and we want to use Docker locally, I think that is a smart way to unblock ourselves." Database access at Cisco is going to be challenging to provision, so local containerization is the pragmatic workaround.
- **Alternatives considered/rejected**: Podman only. Not rejected outright (Colin recommended the team also get Podman familiarity, and Saurav demonstrated he had already made Podman work with a Postgres 17 container pulled from a public AWS image registry), but Docker Desktop remains permitted alongside.
- **Decided by**: Colin.

### 4. Diplomatic framing when presenting to Srinivas Pitta: preface any local-dev tooling choices

- **What was decided**: Whenever the team uses locally installed tooling (Docker Desktop, local containers, and so on) in anything shown to Srinivas Pitta, they will preface it with explicit framing that it is for local development to keep the team unblocked.
- **Rationale**: Colin, "as you can tell for Srinivas, just be, take some care to preface, you know, even for us internal, to preface him with, you know, hey, we are using this for local dev so we can keep moving." This avoids the appearance of going around Cisco's preferred tooling.
- **Alternatives considered/rejected**: Saying nothing and hoping it does not come up. Rejected implicitly because Cisco's internal tooling policies (Saurav described a nested web of bot-compliance policies he ran into) are sensitive and the team does not want to get flagged.
- **Decided by**: Colin.

### 5. Architecture approach for WebEx scraping: decoupled scraper + database + MCP + app / bot on top

- **What was decided**: The WebEx track will propose a layered architecture with a service-level scraper app, a database for scraped messages and files, a Model Context Protocol (MCP) layer on top of the database, and then any chat bots or agent apps built as consumers of that MCP layer.
- **Rationale**: Saurav proposed it first and Colin aligned: decoupling gives you a unified service layer that multiple downstream applications can share, reduces technical debt, and lets OAuth be scoped at the bot-to-data-access boundary rather than having the bot carry a god-mode token with access to all spaces and chats. Colin added the strategic framing, "That is a huge value that we can bring on this team, is we can basically say, effectively say like, without saying it out loud, pretend that you are in charge of this at Cisco." The architecture also has to handle open questions Cisco has not worked through (do you persist scraped files, do you track file IDs only, what happens if a user deletes a file after scrape).
- **Alternatives considered/rejected**: Building a bot that directly hits the WebEx APIs without a scraper or database layer. Rejected because it duplicates work across every new use case and creates data access governance problems at the bot token level.
- **Decided by**: Saurav proposed, Colin aligned, treated as consensus.

### 6. Do not take Cisco's statements about prior work at face value

- **What was decided**: When Cisco team members (Naga, Justin, or others) claim they have already built something, the team will not simply accept that and back off. They will insist on seeing the code and architecture before deciding whether BayOne's proposal duplicates it.
- **Rationale**: Colin's direct guidance, "even if they say that we have it, do not take that as the answer, right? So say, like, I need to understand it, I need to see it. Because very, very, very, very commonly do people say that stuff. And then you look and it is this hacked together thing." He also set a heuristic that verbal descriptions of Cisco's existing systems will be "about maybe 70 percent correct" with the remaining 30 percent being misremembered, misstated, or misrepresented.
- **Alternatives considered/rejected**: Taking Cisco's word and pivoting the BayOne scope. Rejected because it risks the team deferring to work that will not actually satisfy the use case.
- **Decided by**: Colin.

### 7. Scribbler versus WebEx transcription: three-tier A / B testing framework

- **What was decided**: The Scribbler (Whisper based) versus WebEx native transcription comparison will be structured as three evaluation tiers, not a single raw-quality bake-off:
  - Tier 1: Out-of-the-box Whisper versus out-of-the-box WebEx transcription, raw quality comparison.
  - Tier 2: Glossary-augmented quality. Instead of processing the transcript as a separate step, prompt-engineer the downstream AI consumer of the transcript by injecting a glossary of likely-misheard jargon and attendee names at the point the transcript is used. Measure whether the lower-accuracy WebEx transcript becomes as usable as Whisper once augmented.
  - Tier 3: Compute and scaling cost. Measure the compute resources Whisper requires, whether it runs concurrently or serially on a given host, and what the deployment footprint looks like if Cisco tries to use it organization wide.
- **Rationale**: Colin's reasoning was that raw transcription accuracy is not the real question. The real question is which transcript is more usable as input to downstream AI, and whether any quality advantage Whisper might have is worth the compute and scaling cost Cisco would have to absorb to host it on-premises across the organization. He gave the concrete example, "if I told you that with Whisper, I could get 10 percent better transcripts, and it costs 20,000 dollars a month, are you going versus free for the other one with WebEx transcription? You are going to say, you know, that is great, but 10 percent does not justify 240,000 dollars a year."
- **Alternatives considered/rejected**: One-tier raw-quality comparison only. Rejected as insufficient because it ignores the production economics and the AI-downstream usability question.
- **Decided by**: Colin, with Saurav contributing the initial A / B testing framing.

### 8. Data model for build logs: star schema, SHA-hash keyed, with Model Context Protocol tool for on-the-fly git queries

- **What was decided**: The build-logs data layer will be a star schema relational design, keyed on Git SHA hashes and similar identifiers, rather than a NoSQL or JSON-document store. Backward traceability from a build back to originating pull requests and commits will be served through a Model Context Protocol (MCP) tool that issues git queries on demand, rather than by persisting the full lineage data in the database.
- **Rationale**: Colin, "this is one where realistically it should be a star schema. And I mean, that is the easiest possible way also to enable downstream agentic AI. I would not do it as like a JSON format with NoSQL." The follow-on insight was that because MCP can retrieve information on demand, the team does not need to persist everything. Store the SHA hash and the minimum identifiers, then rely on live git queries, either through the git command-line interface or through a git Model Context Protocol server, for anything that can be reconstructed from git itself.
- **Alternatives considered/rejected**: NoSQL / JSON-document store. Rejected because it makes relational queries and agentic AI lookups harder. Also rejected: storing all commit and pull-request lineage data redundantly in the database when git itself is the source of truth and MCP can query it live.
- **Decided by**: Colin, with Namita accepting the direction for her data-model planning work.

### 9. Weekly deliverable structure: architecture diagram plus presentation per team, generated with Singularity

- **What was decided**: Each of the two tracks (WebEx and build logs) will be responsible every week for producing an architecture diagram and a presentation for that week's meeting with Srinivas Pitta, generated using the Singularity tool. Colin will train each team on how to use Singularity so the deliverables are not manually assembled.
- **Rationale**: Colin observed from the Apr 10 Srinivas Pitta call that the call was chaotic because attendees kept jumping between topics, and that having pre-staged slides (game plan for the meeting, architecture diagrams, proposal vs current state) would have helped cut through the jumping. Framing for the team, "no one is going to be wasting hours in PowerPoint here. We do not do that." Colin noted he generated the Apr 10 deck in the 15 minutes before the call using Singularity and there was no negative feedback on the output from Srinivas.
- **Alternatives considered/rejected**: Manually built slides. Rejected because it is slow and does not scale to a weekly cadence across two tracks.
- **Decided by**: Colin.

### 10. Team continuity: both members of each track learn the Singularity workflow

- **What was decided**: Both people on each two-person team will be trained on Singularity so that either can produce the weekly architecture-and-presentation deliverable. No team should have a single-point-of-failure owner for the weekly output.
- **Rationale**: Colin, "we will make sure that both people on each team know how to do this for continuity. You know, sometimes people get sick, sometimes people go on vacation. You do not want things to stop working just because one person is not there."
- **Alternatives considered/rejected**: Designating a single owner per team for slide generation. Rejected on continuity grounds.
- **Decided by**: Colin.

### 11. Team responsibility split: two two-person tracks, Colin meets with each separately on architecture

- **What was decided**: The team is organized as two tracks:
  - WebEx / scraping / transcription: Srikar Madarapu and Saurav Kumar Mishra
  - Build logs: Namita Ravikiran Mane and Vaishali Sonawane
  - Colin will hold a separate architecture meeting with each track this week.
- **Rationale**: The two tracks are sufficiently independent (different data sources, different Cisco stakeholders, different architectures) that combining architecture conversations wastes time. Keeping them separate also lets Colin tailor the depth and content to each track's specific questions.
- **Alternatives considered/rejected**: One combined all-hands architecture meeting. Rejected implicitly because the tracks have little architectural overlap.
- **Decided by**: Colin.

### 12. Escalation cadence: Wednesdays are the latest day in the week to flag access blockers to Srinivas Pitta

- **What was decided**: If any team member is still blocked on access (Aurora Development Server, GitHub, DeepSight, Scribbler, Codex / Copilot, and so on) after Tuesday's check-in, Wednesday is the latest day to escalate to Srinivas Pitta.
- **Rationale**: Srinivas Pitta explicitly asked on the Apr 10 call for early escalation, because he wants the chance to unblock access issues before they compound through the rest of the week. Colin, "Wednesdays will be the latest day in the week where we are going to flag still existing problems up to Srinivas. He was asking for earlier in the week, he wants to know if there is problems so that he can help."
- **Alternatives considered/rejected**: Waiting until the Friday Srinivas Pitta call to raise blockers. Rejected because it leaves Thursday and Friday burned on the same blocker.
- **Decided by**: Colin, based on Srinivas Pitta's stated preference.

### 13. Diplomatic framing of Cisco's existing Scribbler work: show current state versus proposed state, do not call it junk

- **What was decided**: When presenting to Srinivas Pitta about the gap between Cisco's current Scribbler implementation (which Srikar learned from Naga is essentially a local Python script that runs Whisper on the engineer's own machine with no service-level integration) and BayOne's proposed architecture, the team will present a current-state architecture diagram side-by-side with a proposed-state architecture diagram and allow the technical audience to draw their own conclusions about the gaps.
- **Rationale**: Colin, "for us, what I mean by diplomatic is capture that. Say, here is what we can see for the current state without saying that this is, you know, complete junk. Here is why this will not work. Here is what our proposal is to do this better at scale." He also said, "simply show it as a diagram and say, here is how it works today, here is what we suggest it works in the future, because it will naturally come out as to what the shortcomings are to any logical person that is technical." Colin's direct diagnosis of Cisco's Scribbler effort, reserved for the internal team only, "effectively what Cisco has done is they have created a solution without an actual use case, which is another way of saying I messed around at work and got paid to do it."
- **Alternatives considered/rejected**: Directly calling out the shortcomings of Scribbler verbally in the meeting with Srinivas Pitta. Rejected because it creates an argument dynamic and damages the working relationship with Naga and others who built it.
- **Decided by**: Colin.

### 14. Namita Ravikiran Mane will teach the team the GitHub Enterprise access procedure

- **What was decided**: Namita, who was the only team member who successfully completed GitHub Enterprise access at Cisco (via the A2G group plus a Justin ping), will teach the rest of the team the procedure using the PDF she shared on Friday.
- **Rationale**: She is the only one who got through. Everyone else who tried has been stuck at "access granted" with nothing visible. Colin, "I have to give you that job for the rest of the team. Teach all of us how to, you know, get that access. We have all been trying. We have not been successful. You are the only person that has had success there."
- **Alternatives considered/rejected**: Having each team member individually figure out the procedure with Justin. Rejected as inefficient when one person already has a working recipe.
- **Decided by**: Colin, deferring to Namita's existing knowledge.

### 15. Do not mention Claude Code to Srinivas Pitta

- **What was decided**: Team members will not reference Claude Code in any Cisco-facing meeting. Colin has it installed personally on his Cisco machine and uses it, but the rest of the team is blocked on Codex or Copilot access and will work without AI tooling rather than say out loud that they are using Claude Code.
- **Rationale**: Cisco's sanctioned AI tooling for internal engineering is Codex and Copilot, and they are still gating access behind the mandatory training. Colin, "technically no one knows if you are, if you are not using Cloud Code. I mean, I have mine personally installed on the Cisco machine. So just do not say a word about that in a meeting, and I will not know any better. No one will know any better." Saurav confirmed he was being careful on his end because the documents he generates with AI assistance are recognizable as AI-generated.
- **Alternatives considered/rejected**: Waiting for sanctioned Cisco AI tools only. Not rejected for the team broadly (they are effectively waiting), but Colin personally opted to use Claude Code covertly in the interim.
- **Decided by**: Colin, for his own usage, with guidance to the team to keep it off the record.

### 16. This week's primary deliverable is documentation

- **What was decided**: For the week of Apr 13, the primary written deliverable for both tracks is documentation (current-state understanding, proposed architecture, data model, log map) rather than code or a running demo.
- **Rationale**: Colin's read of both Deepak and Srinivas Pitta is that they want to see a concrete plan. "That is the very common thread between Deepak and Srinivas. They want to see how are you guys going to do this. Like we have talked about it for a while, we have met, we have gathered info, what are we going to do about it?" Documentation is also the deliverable that is least blocked on Cisco-side access provisioning, since it can be produced on BayOne hardware.
- **Alternatives considered/rejected**: Jumping straight into code or proof-of-concept demos. Rejected because too many access blockers remain and because the Cisco stakeholders are asking for a plan, not a demo.
- **Decided by**: Colin.

### 17. Build-logs observation period: sample real logs, structure them in folders, automate collection if possible

- **What was decided**: Namita and Vaishali will establish an observation period for Bazel build logs:
  - Capture samples of both passing and failing logs from the dev environment.
  - Structure them in a simple folder hierarchy capturing date, build type (nightly production vs user build), and whether the build passed or failed. At Saurav's suggestion, also capture the user or commit attribution so commit-level traceability can be tested against real data.
  - Automate the daily collection via a script rather than manually downloading files. This will likely run against the Network File System (NFS) store where Cisco persists build logs.
  - Push Justin for access to main-branch (production) build logs, not just the dev environment's passing logs.
- **Rationale**: Colin's guidance was that a single log sample is never representative ("the outlier that is weird from all the other ones that are ever going to be sampled"), so the team needs multiple samples across multiple builds to see consistency, schema drift, whether the log file is one composite text file or many individual logs per application, and what varies day to day. Manual daily download is a tax that compounds over the length of the engagement, so automation up front is worth the investment.
- **Alternatives considered/rejected**: Manual daily downloads with no automation. Rejected as not scalable. Also rejected: working only from a single sample Justin provides.
- **Decided by**: Colin, with Saurav adding the commit-level attribution requirement.

---

## Items deferred to the next day or to individual meetings

- GitHub issue assignment at the project level: deferred to Tuesday, gated on all team members completing BayOne GitHub account creation.
- Architecture deep dives: deferred to separate per-track meetings with Colin later in the week.
- Singularity training for the teams: scheduled for later the same day for Srikar and Namita, with others to follow.
- Scribbler access: deferred pending DeepSight access, which Colin will escalate to Srinivas Pitta in his post-meeting summary. As an interim, Saurav suggested asking Naga for the Scribbler transcript of the Apr 10 call itself so the team can at least see output quality without full tool access.

---

## Cross-cutting themes in Colin's decision-making

Three themes run across the decisions above:

1. **Unblock locally, escalate for access formally.** Docker Desktop locally, Claude Code personally, scripted log collection, all accept the reality that Cisco's access provisioning is slow and the team cannot afford to sit idle waiting for it.
2. **Take ownership of architecture even when not asked.** Multiple decisions (the decoupled WebEx scraper architecture, the star-schema data model, the three-tier A / B testing framework, the current-state-vs-proposed-state framing) reflect Colin's position that Cisco has not done the architectural thinking themselves and that BayOne's value is doing it for them, diplomatically.
3. **Present, do not argue.** The diplomatic framing decisions (items 4, 6, 13, 15) all come back to the same principle: present facts and diagrams, let the technical audience reach their own conclusions, avoid direct confrontation with Cisco's prior work.
