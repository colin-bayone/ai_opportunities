# 16 - Srinivas Sync: LLM Access and CICD Deployment Path Clarification

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on the LLM access path and post-ADS CICD application deployment sequence Srinivas described, closing Blocker 2 of the prep deliverable

---

## 1. Why this thread exists in the meeting

Colin's prep deliverable for this week (`weekly_status_2026-04-27_v3_table.md`) listed five items on the critical path. Item 2 was the language model access path. The prep wording was:

> Language model access path. Language model features require credentials. Circuit API was indicated as not the appropriate production path. DeepSight credentials are gated on the team operating from an ADS environment. Even with ADS and DeepSight in place, the language model access path is not yet confirmed.
>
> What is the language model access path for the Friday deployment, and is interim Circuit API use acceptable until the production path is in place?

Colin walked Srinivas through this question on the call after the ADS provisioning thread had been resolved by Divakar Rayapureddy and Anand. Srinivas's response gave both the deployment sequence (how to bring the CICD application up on the Temporary ADS) and the language model access mechanism (DeepSight handles it automatically once credentials are registered on the website). That answer is what this document captures.

Colin's verbatim framing on the call:

> "This one is good on the number one for critical path blockers. Number two is on the language model access path. I think this one might get resolved once we have ADS and therefore DeepSight. The question was basically for Friday. Given that things that we have to do need a language model to work, currently we were using the incorrect Circuit API credential. Is that okay if we don't have other language model credentials available by Friday? That's that was the question. Not that that's permanent, but just as an interim."

---

## 2. Srinivas's answer in full (the core deployment + LLM sequence)

Srinivas answered with a single connected sequence. Reproduced verbatim from the transcript with transcription corrections applied (`AD server` / `ADS server`, `CICD app`, `DeepSight`, `circuit API`):

> "So one thing is, as soon as you get the ADS server, you need to build the CICD app and try to deploy on your ADS server and see if you can bring it up. Right, if that is there, then technically you should be able to. Just did you all register your credentials on the website already? Yes. Okay. Then technically it should work. Okay. If for whatever reason if you run into hiccups, then you can try with the circuit API itself. Yeah. But I want you guys to get familiar with bringing the app on the ADS server using DeepSight on the CICD app. That way, I know that you are comfortable basically."

This was followed immediately by the support commitment:

> "I asked the other team members who built the infrastructure to put some user guide into the CICD repo, so probably they'll try to do it like today, tomorrow or whenever. Okay, you can follow through. You'll see there will be some commits happening somewhere. So I asked them to do. And I asked them to basically deploy the Jenkins pipeline also for this. That way you don't have to struggle. How how how it is okay."

Then the .env follow-up from Colin and Srinivas's response:

> Colin: "And then the only remaining thing here was just because I think we were looking at the .env.example file. And I'm sure whenever this gets deployed, we were just wondering who the owner for that one would be, because this is where the AI credentials come into play."
>
> Srinivas: "No, that is on the DeepSight side. Will automatically take care. You don't have to worry. That is an example he has given. Okay, okay. As a how how do you put in?"
>
> Colin: "Okay, so so that's already handled whenever we have."
>
> Srinivas: "It's it's it should be."
>
> Colin: "Baked in already okay."
>
> Srinivas: "But uh, if you are that's what I am saying, if once you are stuck, we'll tell you how to move forward."

Then the existing-app validation tip:

> "One other way is once you get an ADS pick one of the existing app. And try to launch it and see if that works. Then you know that the other environment is all set."

That entire span (transcript timestamps 00:30:28 through 00:33:22) constitutes Srinivas's complete answer to Blocker 2. The remainder of this document decomposes that span step by step.

---

## 3. The deployment sequence Srinivas prescribed

Srinivas laid out the path as a linear sequence of steps that the BayOne team executes once the ADS server is in hand. Each step is captured below with what it means operationally for Friday.

### Step 1. Get the ADS server provisioned and accessible

Resolved earlier in the same meeting. Divakar Rayapureddy committed to:

- Leaving one of the previously procured machines available for the BayOne team to use immediately during this week (CN-SJC-STANDALONE Temp ADS, already connected and ready as of April 27 per recent commit history).
- Retiring four of the previously procured VMs and procuring two new 16 core / 32 GB / 100 GB local / no backup machines, mostly ready by Monday evening, possibly later in the week ("might be early. I cannot guarantee").
- Confirming bundle membership (CN-SJC-STANDALONE) on the new machines.

The Temporary ADS is the operative resource for this week. Permanent ADS provisioning is in flight as a parallel track but is not blocking Friday.

### Step 2. Build the CICD application

Srinivas's exact verb: "build the CICD app." This means clone the DeepSight CICD repository, build it locally on the ADS server. The application is the front end (chat in the application + the CICD UI surface) into which BayOne plugs the static FAQ wiring, the CAT MCP dynamic answer path, and ultimately the WebEx proxy interface Srinivas described later in the meeting.

### Step 3. Deploy the CICD application on the ADS server

Same verb pattern. "Deploy on your ADS server and see if you can bring it up." The deployment target is the ADS server itself. DeepSight allows "bring your own compute" (Srinivas's later demo phrasing), so the ADS server is attached as the host, and the CICD app is launched on top of it.

### Step 4. Confirm the application starts and the LLM access works end to end

Srinivas's verification check is the chat surface itself. Once the app is up on the ADS server with the developer's DeepSight credentials registered (see Step 5 below), opening the chat in the CICD app and selecting a model should work without any further credential configuration on the BayOne side.

### Step 5 (preflight, parallel to Step 1). Register credentials on the DeepSight website

Srinivas asked: "did you all register your credentials on the website already?" Colin confirmed: "Yes." Srinivas's response: "Okay. Then technically it should work."

This is the credential registration that gates DeepSight access. It is a per-user developer registration on the DeepSight website, not a separate step BayOne needs to repeat for the CICD app deployment. Because all four BayOne engineers have already completed it, the DeepSight + ADS + CICD app stack should pick up their LLM access automatically.

---

## 4. How the LLM access actually flows (Srinivas's later mental model)

In the deployment-walkthrough portion later in the meeting (around 00:49 onward), Srinivas demonstrated and described the LLM access flow on the chat surface:

> "Here, right when the user registered their DeepSight application. Every app has their own chat. In your case, CICD will have its own chat. Okay, so of course in the chat we'll pre cook some of these things. Even for you for the, but like a quick answers that user want, whatever it is right. But the idea is this, when the user asks a question, we are asking the user to pick whatever the model choice that you have. Right? What is offered on the DeepSight platform. So we support Copilot, Codex models, okay? And of course the circuit is also there. We'll also add cursor and other stuff later on."

Three points fall out of this:

1. **The chat is per-application.** The CICD application has its own chat surface. The user opens the chat and picks a model.
2. **Model menu available on DeepSight today:** Copilot, Codex. Circuit API is also present. Cursor and others are coming later.
3. **The user picks their own LLM at chat time using their own credentials.** "When he's chatting, he's using his own LLM access, right? His own credentials. What have we picked up? Of course, there's always a default."

This means the BayOne team does not need to provision a service-account LLM credential for the CICD application. The LLM credential follows the user, not the application. Each developer who opens the chat is using their own DeepSight-registered credentials, with the model picked from the available menu.

---

## 5. The .env.example question and DeepSight's automatic handling

Colin's specific concern from the prep deliverable was that the CICD repository's `.env.example` file referenced AI credentials. The natural interpretation was that someone needs to own those credentials, populate the real `.env`, and rotate them.

Srinivas's answer cuts that concern off cleanly: "That is on the DeepSight side. Will automatically take care. You don't have to worry. That is an example he has given."

Operational reading:

- The `.env.example` is illustrative. It shows the shape of the variables, not a credential ownership decision the BayOne team needs to make.
- DeepSight injects the LLM credential automatically when the application is launched on a DeepSight-registered ADS host.
- There is no separate AI-credential ownership decision to make for Friday.
- If the deployment runs into a credential problem in practice, Srinivas's escalation is direct: "if once you are stuck, we'll tell you how to move forward."

This collapses what looked like an unresolved ownership question into a non-issue, conditional on DeepSight behaving as Srinivas described.

---

## 6. The "use existing app first" validation suggestion

Right after the .env exchange, Srinivas added a smaller suggestion that is worth tracking as its own preflight step:

> "One other way is once you get an ADS pick one of the existing app. And try to launch it and see if that works. Then you know that the other environment is all set."

Operational reading:

- Before deploying the CICD application built by BayOne, take any existing DeepSight app already in the repo or already known to work and launch it on the ADS server.
- If the existing app launches cleanly, BayOne knows the ADS environment, the DeepSight host attachment, and the credential plumbing are all healthy.
- Then any subsequent failure on the CICD application deployment is isolatable to BayOne's build of the app, not to the environment.

This is a cheap-to-execute environment smoke test that should run before, or in parallel with, building the CICD app. It is not a blocker, but it shortens the debug loop materially if anything goes wrong on Friday.

---

## 7. The user guide and Jenkins pipeline support coming from Srinivas's other team

Srinivas committed two pieces of help from the team that built the underlying infrastructure:

1. **A user guide for the CICD repository.** "I asked the other team members who built the infrastructure to put some user guide into the CICD repo, so probably they'll try to do it like today, tomorrow or whenever."
2. **A deployed Jenkins pipeline for the CICD application.** "I asked them to basically deploy the Jenkins pipeline also for this. That way you don't have to struggle."

The signal Srinivas told BayOne to watch for is commits landing in the CICD repository: "you'll see there will be some commits happening somewhere."

Open questions on this commitment, none of which are blockers but all of which BayOne should track:

- **Timing.** "Today, tomorrow or whenever" is a soft window. If commits have not landed by midweek (Wednesday), BayOne should ask for a status check given the Friday deployment target.
- **Scope of the user guide.** Whether the guide will cover building, deploying, attaching the host, or all three was not specified. BayOne should be prepared to deploy from first principles using Srinivas's verbal walk-through and surface gaps to the documenting team as they hit them.
- **Jenkins pipeline coverage.** Whether the Jenkins pipeline will replace the manual build/deploy steps from Section 3 or will sit alongside them was not specified. BayOne can proceed with the manual path on Monday/Tuesday and pick up the pipeline once it is available.

---

## 8. The Circuit API interim fallback

Colin's original question was whether interim Circuit API use is acceptable for Friday if no other LLM credential path is in place. Srinivas's answer makes the question almost moot, but does not eliminate the fallback:

> "If for whatever reason if you run into hiccups, then you can try with the circuit API itself."

Reading:

- The expected path is the DeepSight-on-ADS path. That is what BayOne should target.
- Circuit API remains the explicit hiccup-recovery fallback if the DeepSight path does not come up in time for Friday.
- Srinivas did not condition the fallback on prior approval, did not flag it as policy-sensitive in this exchange, and did not give a deadline by which BayOne must switch off it. The earlier characterization in Colin's prep ("not the appropriate production path") still stands as a long-term constraint, but for this Friday's first deployment it is available.

The interim use of Circuit API for Friday is therefore acceptable, with the expectation that BayOne moves off it as soon as the DeepSight-on-ADS deployment is healthy.

---

## 9. Srinivas's escalation path if BayOne gets stuck

Two explicit escalation statements from Srinivas in this thread:

> "But if you're stuck or anything, just let us know. That way we can help you along the way." (00:23:16, in the wiki/scrape thread, but applies generally.)
>
> "If once you are stuck, we'll tell you how to move forward." (00:32:55, in the .env / LLM credential thread.)

Reading:

- Srinivas is committing to active unblocking. BayOne does not need to wait until the next Friday sync to surface a deployment problem.
- The asynchronous unblocking channel via the engagement WebEx space, already noted as active in Colin's prep deliverable, is the right place to flag a hiccup mid-week.
- The expected response time was not specified, but Srinivas's posture across the meeting was responsive within the workday.

---

## 10. Mapping back to Blocker 2 of the prep deliverable

Blocker 2 in `weekly_status_2026-04-27_v3_table.md` had one question:

> What is the language model access path for the Friday deployment, and is interim Circuit API use acceptable until the production path is in place?

Resolution from this meeting:

| Sub-question | Resolution from Srinivas |
|---|---|
| What is the language model access path for the Friday deployment? | DeepSight-on-ADS. The CICD application is built and deployed on the ADS server. DeepSight injects LLM credentials automatically based on the per-developer credential registration already completed on the DeepSight website. The user picks their model in the chat (Copilot, Codex, or Circuit API) at chat time. |
| Is interim Circuit API use acceptable until the production path is in place? | Yes, as an explicit hiccup fallback if the DeepSight-on-ADS path does not come up cleanly. Not the long-term path. |
| Who owns AI credentials in `.env.example`? | Non-issue. DeepSight handles `.env` automatically. The example file is illustrative. |
| Are DeepSight credentials gated on operating from an ADS environment? | Confirmed. Per-developer registration on the DeepSight website is the gating action and has been completed by all four BayOne engineers. The application then needs to run on a DeepSight-attached ADS host for the credentials to flow through. |

Blocker 2 is **resolved** for Friday's deployment, contingent on:

- The Temporary ADS being operational (resolved in this meeting under Blocker 1 / Permanent ADS thread).
- The user guide and/or Jenkins pipeline from Srinivas's other team landing in the CICD repository, or BayOne deploying from first principles using Srinivas's verbal sequence.
- DeepSight's automatic `.env` injection behaving as Srinivas described in practice.

---

## 11. Open questions remaining after this exchange

These did not get fully closed in this meeting and should be tracked into the Friday sync:

1. **Timing of the user guide and Jenkins pipeline commits.** Srinivas said "today, tomorrow or whenever." If nothing lands by Wednesday, BayOne should ask Srinivas for a status check.
2. **Scope of the user guide.** Whether it will cover the full sequence (build, deploy, host attachment, credential verification) or only some of it is unknown until the commits appear.
3. **Whether the existing-app smoke test from Section 6 is something BayOne should do explicitly before the CICD app deployment, or whether Srinivas treats it as optional.** Srinivas phrased it as one way; BayOne should treat it as a recommended preflight given the Friday deadline.
4. **The long-term migration off Circuit API.** Srinivas accepted Circuit API as a Friday fallback but the prep deliverable's earlier characterization (not the appropriate production path) still implies BayOne needs to migrate off it once the DeepSight-on-ADS path is healthy. The migration trigger and deadline are not yet specified.
5. **The WebEx-bot-to-ADS-app proxy pattern Srinivas described later in the meeting** (Sections 49-52 of the transcript, where the WebEx bot becomes a thin proxy that streams messages to and from the LLM-enabled CICD app on the developer's own ADS server) is a separate, longer-term workstream and is captured in a different decomposition document. It is not part of Blocker 2 closure for Friday, but it does mean the LLM access path described here also serves the future WebEx-bot architecture, since both surfaces share the same backend on the ADS-hosted CICD app.

---

## 12. Concrete operational sequence for the BayOne team this week

Synthesized from Srinivas's answer, in the order BayOne should execute:

1. Confirm the Temporary ADS server access for each engineer (in flight from Divakar Rayapureddy on Monday).
2. Confirm each engineer's DeepSight website credential registration is current (already done per Colin's confirmation).
3. (Optional, recommended.) Pick one existing DeepSight app and launch it on the ADS server to confirm the environment is healthy.
4. Watch the CICD repository for the user guide and Jenkins pipeline commits from Srinivas's infrastructure team. Pick those up as they land.
5. Build the CICD application on the ADS server.
6. Deploy the CICD application on the ADS server. Bring it up.
7. Open the chat in the CICD application. Pick a model from the DeepSight menu (Copilot, Codex, or Circuit API). Confirm the LLM access works end to end.
8. Wire the static FAQ path and the CAT MCP dynamic answer path into the chat surface (the Friday deliverable proper).
9. If anything in steps 5 through 7 fails, fall back to Circuit API for the Friday deliverable and surface the hiccup to Srinivas in the engagement WebEx space.

Friday deliverable target stands. Blocker 2 is closed.
