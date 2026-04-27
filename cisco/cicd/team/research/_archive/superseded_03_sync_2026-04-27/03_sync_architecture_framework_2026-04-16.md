# 03 - Team Sync: Architecture Framework

**Source:** /claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/cisco-team-sync_4-16-2026.txt.txt
**Source Date:** 2026-04-16 (Wednesday team sync)
**Document Set:** 03 (Third team sub-singularity set)
**Pass:** Focused deep dive on architecture framework, technical design, and security considerations

---

## 1. The Three-Part Architecture Framework

### 1.1 Namita's Question That Triggered the Framework

Namita raised the question directly at [00:31:18]: "Yesterday we were discussing about the architecture. So do we need one single architecture or we create two or three separate architectures?"

Colin responded that it depends, then laid out a three-part framework that structures how the team should think about architecture documentation for any application in the Cisco CI/CD ecosystem. This was not an abstract exercise -- Colin explicitly tied each part to credibility, defensibility, and the team's ability to present recommendations to Srinivas.

### 1.2 Part One: Current State Architecture

Colin defined the first architecture layer as "the current state architecture of a given system." He stated this is "important to have either from something that you can defend, for instance, like a meeting transcript or direct from the source person who wrote this, not just, you know, like what Srinivas does in meetings and kind of hand waving."

He specified two acceptable evidence bases for current state:
1. Defensible sourcing from the person who actually built the system (not secondhand accounts)
2. Direct access to the repository to "really see how it works in the first place" and "grounding that architecture of the current state in code"

He warned explicitly: "That's very, very important to not guess on the architecture, because if we're wrong there, that's a credibility loss for us."

Colin characterized this layer as "eyes wide open. That's, this is what it is right now, for better or for worse. It could be good, it could be bad, who knows?"

He then gave the Pulse application as a concrete example of what the current state would reveal. From everything the team knows, "there is not a unified layer for a database" in that application. Every person who runs it to "scrape transcripts from WebEx" creates "duplicate work and duplicate processing" because "everything's deployed as like standalone." He instructed the team not to just accept his characterization but to "confirm and understand it" by asking people like Naga or Justin directly: "When this gets deployed, what's the plan? Is the plan for this to get deployed to everyone exactly as this is, so that everyone's running their own scraper? Or, you know, what's the ultimate plan here?"

He framed the investigative posture: "You basically want to have it so that you are being a detective and you're getting all the details and you have full visibility."

### 1.3 Part Two: Problems and Recommendations

Colin described the second layer as "really not a diagram at all. It's kind of, here's the problem with this from a scaling perspective, from a cost perspective, from a security perspective."

He continued with the Pulse example to illustrate. The core problem: transcripts are constant regardless of source. "A transcript is a transcript. So if they are WebEx transcripts, for instance, that are being scraped, if they're WebEx chats that are being scraped, if they are coming from Wispr, it does not matter. They are all referring to the same thing. So if it's processed, it should be processed once and stored and referenced. Otherwise, you're just duplicating databases, you're duplicating compute, you're duplicating for language models that are summarizing those meetings."

He called this out as architecturally unacceptable: "From an architecture perspective, that's a terrible approach to AI." He gave an analogy: "Even for this meeting transcript, if I said, hey, everyone, each of you go and generate the same meeting notes, and it had no personalization, no customization, it was just the same prompt for the same meeting transcript. Sure, there will be slight variations, but it's duplicate. It's wasteful."

Colin said the team does not have to call out the problems in accusatory language: "We don't have to call out and say your process is bad, but we're effectively saying that without saying it."

He also flagged the hosting dimension, referencing the previous Friday meeting with Imperma about ADS machine management: "She was trying to say, oh, ADS machines, you know, compute, blah, blah, blah. It's a problem to manage that. Well, how are they going to do that at scale for people that want to use this if it's deployed in that way? They essentially do need to have one unified layer to do this."

### 1.4 Part Three: Future State Map

Colin defined the third layer as "the future state map that would be our ideal state based upon our own recommendations."

He said this could take two forms:
1. Per-application future state
2. A "master grand vision for how all these things tie together to remove duplicates"

On the master vision, Colin stated: "I think that's what all of Cisco right now is lacking, a master grand vision for how all these things tie together to remove duplicates." He acknowledged the difficulty: "For that, you really have to do some deep dive digging into that. You have to zoom out as much as you can and look for abstraction and similarities. It is a tough thing to do."

He gave a litmus test: "How many applications would benefit from one singular place to retrieve meeting transcripts? If there is more than a few, make it a common module and an architecture diagram for a master plan and show the inheritance up the chain from the other apps."

He preemptively addressed the objection that unification equals monolith: "Sometimes people perceive unification as creating a monolith and they say, oh my gosh, I hate this. They're wrong. That is the wrong assumption to go with. What we are showing is that you can modularize it, unify it, and still have great flexibility with microservices if you do this. You just are having common modules instead of duplicating the work."

On the master plan, Colin noted the coordination challenge: "If everyone does their own spin on it, we're going to jumble over each other. But that's one where we'll all have to work together on." His recommended method: "The easiest way to do it is get on a call, talk through it in great detail like this, and then we'll use that singularity skill like I've been talking to pull it together."

### 1.5 Proactive Recommendations Over Reactive Requirements

Colin emphasized that the team should not wait for Srinivas to hand them requirements. He stated: "What I want is for us to go with the already thought out recommendation for those requirements." He said to "go in with that kind of thinking. You know, we will ultimately go with what they tell us to do, but you know what? Here are my suggestions and here's my rationale."

He described the desired posture: "Rather than him saying, you know, you know, give the requirements, we will go to him and say, here is our recommendation. We are the experts here. Here's our recommendation for you on how to proceed."

He returned to this point later, saying the team adds the most value by solving universal problems rather than waiting for instructions: "I can tell you he's not going to, you know, really care too much about what we're doing if we're just waiting to say, you know, what's the requirements, what to do. He wants people to come and fix this mess for sure."

---

## 2. Dual Entry Points for Log Analysis

### 2.1 Namita's Ingestion Question

Namita asked at [00:46:03]: "So when we design the process, do we directly start from the NFS location and grab what's the problem or grab the logs and work on it or we are using directly from Webex?" She proposed: "My idea was we are directly grabbing from NFS location."

### 2.2 Colin's Response: Two Complementary Systems

Colin praised the question but reframed it from either/or to both/and. He called out the key insight: "Why should it have to come from a user manually mentioning a problem in order to address it. We already have the logs. I don't need to wait. I can have a watchdog and observer look at those NFS and look out for these. And probably users are only flagging things that they notice."

He then laid out two entry points:

**Entry Point 1: Background NFS Watcher (Proactive)**
"Number one is the logs, and that should be first and foremost, and as a background service." He elaborated: "We have those log files. We have them real time for whenever those builds happen. We don't need to wait for a human to say what the error is. Essentially, the human's almost acting like a language model that's saying, whenever you notice, write a summary of what's going on."

**Entry Point 2: Manual WebEx Reports (Reactive)**
"The second entry point could be a manual one. So we can say that we can have both flows." For this entry point, when a human reports in WebEx chat, the system "should reference what we have in NFS to see if we're already in the process of addressing it or have already addressed it. And to make sure if we have already addressed it, that our fix took care of what the user was saying too, to make sure that we didn't miss any detail."

Colin also identified a third scenario that makes the WebEx entry point essential: "If it's a runtime bug that the build didn't fail on and there is no error log there. If it's a runtime bug that the user is noting, that's when we will have to go through and, you know, see what we should do at that point."

He concluded: "I think I see them as two systems that work hand in hand with each other and need to have kind of a contract between the two, more so than, you know, one or the other."

---

## 3. Batch vs. Real-Time Processing

### 3.1 Namita's Question

Namita raised the batch vs. real-time question at [00:46:09]: "We also need to decide, are we going to do batch processing or we are going to do real-time processing?" She argued for real-time on CI: "If some problems comes in PR, the user PR, I think it should be kind of like a real time because quickly, the patch should be generated, right? It should not take one or two days to get answer to it. Otherwise, the user himself can fix it."

### 3.2 Colin's Three-Option Menu

Colin laid out three processing modes with their trade-offs:

1. **Real-time / Streaming:** "Streaming or real time is going to get you quicker resolution for sure."
2. **Batch:** "You could do batch to save on cost and optimize that, especially if it's a heavy language model burden at the expense of not having things resolve as quickly."
3. **Polling Middle Ground:** "You could also have a middle ground where it is, you know, on some set frequency as a polling thing, like something with airflow, check every 5 minutes or check every half hour."

He characterized the polling option as "kind of the best of both worlds in a sense, depending upon preference."

His recommended approach to Srinivas: "What I would do for Srinivas is say, hey, here's the menu. Pick from the menu. Which one is closest to your vision? Or are we completely off?"

### 3.3 Saurav's CI/CD Split (Post-Colin Discussion)

After Colin left the first time, Saurav added a practical distinction at [01:14:50]: "For the CI things, correct, for CI it is from the developer end. So those should be like real time because developer is anyways sitting there and waiting for the build to run. For the CD part, we can have that one batched because that has like a lot of batches running together at nightly bits, correct? That's the CD part, so that can be as batched."

---

## 4. Security Discussion

### 4.1 Access Control and Authorization Gaps

Colin introduced the security topic at [00:37:45]: "From security perspective, two big things. Security means both access control authorization, but it also means making sure bad things don't happen whenever they absolutely shouldn't."

**Org-Level Token Problem:**
Colin raised the issue of org-level access tokens for meetings: "Remember, we're talking about org-level access tokens to meetings. How do you gatekeep that?" He proposed a scenario: "What if I was to say, whoever the CEO of Cisco is, I want to read all of his meetings. Is there access control properly scoped in these existing apps?"

He drew the line between POC and production: "Even if they do work as a POC, that's what separates POC from production. Because if there's a way to use, you know, some generic token, and the only thing that gates it is, you know, strictly an API key and no other system, that's a bad system."

He stated the fundamental vulnerability: "API keys can leak and API keys can be shared. So you can't guarantee who can access what."

**Saurav's Correction: API Key vs. Access Token:**
Saurav corrected the terminology at [00:38:43]: "So it's for like WebEx scraping and accessing, it's not an API key, it's an access token. Okay, so just for clarification there."

**Saurav's Defense of Cisco's Current Design:**
Saurav offered a counterpoint at [00:39:12]: "Maybe they have built it like intentionally bad. So the way they have currently built it, it does solve the problem of this like chat leaking because everyone is scraping their own chats and doing their own work. So even if I want Colin's chat, I cannot get if I was not in that meeting."

He acknowledged the trade-off: "But still, it's duplication of work, so that's like the whole point there."

**Colin's Reframe:**
Colin responded by naming the design trade-off explicitly: "Rather than, you know, solving it from an authorization authentication standpoint, they're choosing to solve it by simply having scope to access tokens, which is going to cause that duplication. When in reality, the more efficient solution would be to have properly gated org level tokens for a given probably a team."

He suggested the tokens could be "attached to particular meetings" and noted they said they can have "up to 40 different chats" (40 spaces).

### 4.2 No Guardrails on AI Fixes

Colin raised this concern earlier in the meeting at [00:28:44] when discussing Rui Guo's NexusT agent and other existing tools: "Cisco doesn't really seem to care too much about guardrails. Or even, you know, authorization. That's true in both Justin and Joseph as well as this guy's stuff. Again, they can do what they want to do, but I'm like, I have no clue why they're letting AI just randomly edit source code for production."

### 4.3 WebEx Chat Tampering Scenario

Colin gave a vivid scenario to illustrate the security risk of using WebEx chat as the source of truth for bug reports at [00:44:17]: "What if I was a bad guy and I said, delete everything in an XOS? And then I delete my comment or I change it to a :). But the language model pipeline that they built already processes that and goes in. I'm being a little bit facetious here, but goes and deletes everything. And then there's no possible trace back to me to say that I was what caused it, because I've changed it out and edited my comment as a :)."

### 4.4 Authorization Check on Triage

Colin identified a missing authorization layer at [00:49:09]: "You have to have some identity for any kind of auto triage. You have to have some identity as to who they should be sent to." He gave an example: "If I am in the WebEx chat and I say, huge issue, blah, blah, blah, blah, blah, but I'm an intern. Should we have? At that point, let's say that I'm an intern and I don't even have write access to the repo. But you know who does? The agent."

He stated the gap clearly: "There's not anything right now in place in the Webex chat that says this user is authorized to do this action on this repository. There's not a check that I'm aware of there."

---

## 5. Unified Data Layer Argument

### 5.1 Colin's Core Argument

Colin built the unified data layer argument through the Pulse example. The problem: per-user deployment means every person running the application creates duplicate processing. "Every person that runs that to go and scrape transcripts from WebEx... that is going to create duplicate work and duplicate processing as if someone were to do it, you know, with their own deployment from DeepSight."

His principle: "If it's processed, it should be processed once and stored and referenced."

### 5.2 Saurav's Downstream MCP Impact

Saurav extended Colin's argument at [00:35:41] to downstream tooling: "For downstream processing also, if we are not having like a unified data layer for all of those things, we cannot like constantly build like good MCPs or tools to access the database as like a data source. So it breaks like the whole pipeline we can build for automations."

This is a significant point because it connects the data layer unification argument to MCP (Model Context Protocol) architecture. Without a unified data layer, every MCP or tool built on top has to handle its own data retrieval, which fragments the tooling ecosystem and prevents reuse.

### 5.3 Microservices Done Wrong

Colin articulated the architectural anti-pattern at [00:36:45]: "They have all these capabilities duplicated and locked inside of individual apps, whenever there should be a more modular, reusable approach to this. If they truly want to go microservices, they should do it right. Microservice does not mean isolation. That's how they're going with it right now."

He specified what the correct approach looks like: "There should be one tools repository with all these tools in there. So if you want to do a WebEx scraper for chats or for transcripts, do that in one place. If you're going to write MCPs that are usable across apps and between apps, don't just simply copy folders over into a new Git repository. Put them in one place, save one source of truth to manage and maintain."

### 5.4 Chat Liveness Problem

Colin raised a specific data freshness issue at [00:41:46]: "There's a little bit of a liveness to chats. Meetings are kind of static because once a meeting happens, it's not like the meeting changes. But for a chat, you can't say that the chat I retrieved at one point in time and it's going to be the same tomorrow because anyone can respond on any comment thread at any time."

He proposed the solution: "This should be stateful, but it should be able to refresh on some loop. That's perfect territory for Airflow, for instance, to point it at a message, scrape the text, stored in a database, link to the attachments or process the attachments through some pipeline, whatever that pipeline is, or however many tools we need beyond the point."

### 5.5 Saurav's File Processing Concern

Saurav raised an additional data processing gap at [00:40:29]: "People are sending in files, photos, images, Excel sheets, everything else. So what are they doing with this currently and what are their plans for this?" He argued for "a single orchestrator or a single tool we should build which should do all of these for like everything. So the conversion task and pre-processing and all of those things."

He also flagged the cost dimension: "Even if I can save like 10 tokens on a request, that's like over a month a lot of tokens saved."

---

## 6. GitHub Issues vs. WebEx Chat Traceability

### 6.1 Colin's Argument

Colin made a pointed argument against using WebEx chat for bug tracking at [00:43:24]. He cited a specific example from the NxOS CI workflow chat where Sitaria wrote: "Hi, the ULS sanity from my PR fails even before running. We run outside the same issue."

Colin stated: "This should 100% be a GitHub issue as a bug report." He noted the response pattern -- "I will take a look and this is for 622. I've put a workaround. Okay, thanks. What was the other issue?" -- and said: "There's no traceability to this. This is not the way efficient teams run with GitHub."

He proposed a pipeline solution: "We could certainly have a part of the pipeline, not to just diagnose and triage, but also to get this properly tracked in GitHub. So that whenever you do have a PR, you can have some traceability to it, instead of saying that, oh, I think this WebEx chat, that by the way, someone can edit at any time, is linked back to this."

### 6.2 Saurav's Extended Loop (Post-Colin Section)

After Colin left the first time, Saurav extended this into a full feedback loop at [01:38:05]: After an error is encountered, "sends to an LLM for a fix. Okay, if it fixes it, okay, good. If it does not fix it, create an issue on the GitHub and also send a message on WebEx." He proposed GitHub as the source of truth: "GitHub is good source of truth for us. We can always track all the commits, the PRs created, and whenever the issue is being created, have the agent created with the skill so that it adds all like the details of from where the build was taken and what exactly was the error kind of an audit trail."

He also proposed a cross-referencing check for incoming WebEx messages: "If anyone else is pinging on the WebEx channel, check if there is an issue related to it. Okay, if it is related, is it the exact issue or not? Is it talking about the same thing? Have we already fixed it? Is it in the pipeline? If we have fixed it, give an update on the WebEx, if we have not fixed it, it's still in the pipeline given update to the user."

Saurav argued the developer experience is better through GitHub: "Even if like the developer does not want or because in Webex there is simple message and you have to change from VS Code or your coding environment to the Webex channel to see your response or ask something. Instead, you are already on terminal. You can use git commands or GH repo or ask Claude or Codex or Claude to pull out these details directly from the GitHub."

---

## 7. No Documentation Exists at Cisco

### 7.1 The Discovery

Srikar reported at [00:55:18]: "We reached out to Justin yesterday. I think Namita our message to Justin for the like architectural diagram for the existing one. Yeah, Justin mentioned like they don't have any of the such kind." When asked about tooling: "We asked like they use like Miro or anything. They said like just the PowerPoint. They use for architecture diagrams and all."

### 7.2 Colin's Auto-Documentation Proposal

Colin immediately identified this as both a problem and an opportunity at [00:55:46]: "That's even a problem. One thing to flag, documentation, and not just documentation like markdown files, but documentation of architecture. That's something that we can do pretty darn easily. We can build a skill or some plugin for them that'll go and auto document architecture every time there's a code change."

He stated the proactive posture: "This is what I mean. Don't wait for Srinivas to tell us that. If you have a good idea, let's propose it."

Saurav immediately picked up on the implementation mechanism at [00:56:21]: "We can let like the hooks run at like commit or when the PR is being created. Just let the hook run or if you want to be really safe after the build has completed."

Colin reinforced the effort argument: "Sometimes people hear that and say, yeah, yeah, yeah, we don't need that right now. But it takes all of half an hour. It's not that big of a deal, especially because they already have Copilot Enterprise. They could already have been doing this this whole time."

---

## 8. Namita's 7-Block Pipeline Diagram

### 8.1 The Diagram Blocks

After Colin left for the Yogesh/Rahul meeting, Namita shared her screen and walked through a pipeline diagram with 7 blocks. She described the structure at [01:14:31]: "So you see this blocks one to seven, right?"

The blocks as discussed:
1. **NFS Ingestion** -- where batch vs. real-time decision lives
2. **Parsing/Chunking** -- log preprocessing
3. **Tier 1: Rule-based error detection** -- regex patterns, deterministic matching (no AI)
4. **Tier 2: Specialized ML/NLP models** -- classification and issue typing
5. **Tier 3: LLM analysis** -- complex root cause analysis and fix suggestion
6. **Structured Storage** -- metadata, build diffs, resolution tracking (new addition, Cisco does not currently have this)
7. **Auto Fix and PR** -- patch generation and delivery mechanism

### 8.2 Team Discussion on the Diagram

**Saurav on restructuring:** He suggested grouping blocks into logical containers: "These first two steps, correct? Ingestion and parsing, chunking. Make it like a big one box, then these two small boxes inside that." Similarly for the three routing tiers: "Put it in a big box, single box and inside these three."

**Saurav on Tier 1:** Recommended referencing Bazel docs to create "this rule-based error detection, what you call repo or whatever we want to create over there, regex patterns."

**Saurav on Tier 2:** Flagged practicality: "We obviously are not going to train it. You have to confirm from them, do they have like this kind of data set? Because for like our timeline, it is not very practical to like create the data set and then do all the steps, then train and inferencing and everything else."

**Saurav on Tier 3 / Block 5:** Stated: "Most likely they do not want a singular LLM call. They want to do it in the same way they are doing for their current one... asking the Codex and passing it the whole workspace. So here it's either Codex or Claude instead of like agent instead of models."

**Saurav on Block 6 (Storage):** Recommended Postgres over SQL: "When a local Postgres can always be used... for an agentic perspective, the performance of Postgres is much better... we will also get like option to add in more extensions on this, like PG vector or age." Namita confirmed: "Right now they don't have this block 6 at all in their system. So block 6 is something that we'll be adding completely new."

**Srikar on observability:** At [01:29:00], Srikar raised the need for LLM observability: "When we are like using the LLMs here, like we need to also like show them like which, let's say like there are some errors, like how the LLM is performing, like a little bit of observability like on what steps the LLM is taking. Something like similar to LangSmith." Namita confirmed: "He is not evaluating. But he's not evaluating. That's the thing. I mean, there are ways to do it, but right now they don't have."

**Saurav's feedback loop addition:** At [01:25:53], Saurav proposed adding arrows back into the tier system: "After we have done a fix, correctly, that was approved by the user and they have applied it. We can add that back to the rule based. Now we have one error and one particular fix that works for it. So something like that. Getting my point. So the system itself takes back feedback, the correct responses into them."

---

## 9. Human-in-the-Loop vs. Autonomous Fix Application

### 9.1 The Cisco Requirement

Saurav stated from the Friday meeting at [01:51:52]: "From what I remember on Friday, they said that they want the developer who is raising that PR to be the person who is closing that PR. Like the agent can go review the bug, create a fix, but it must not apply that fix."

Namita noted a discrepancy: Justin's team wanted to create a new PR with the fix, while Srinivas's team seemed to want just a notification. She said at [01:19:05]: "There was a discussion with them that they wanted to create a new PR. So maybe with Srinivas, we can just confirm."

### 9.2 Colin's Bug Classification Framework

When Colin returned, Saurav asked whether to pitch full autonomy. Colin responded with a classification framework at [01:53:52]:

- **Severity:** "Is this something that's actively functional breaking?"
- **Criticality:** "Even if it's functional breaking, fine, but does it matter to other people? Have you affected other people's work as a result of what you did?"
- **Complexity:** "Is this just a quick, you know, one-liner fix? You missed a parentheses, you missed a semicolon, or is this something that, you know, you completely screwed up the entire class and you got a full rewrite?"

He stated: "Those have different implications for automation."

### 9.3 Colin's Two Recommendations

**Recommendation 1: Human-in-the-loop with faster detection.**
"Humans with an HIL system, human in the loop system, will have to be there at first. How I would build this is have that HIL system so that you can still go with the pattern that they described, but you can cut out the middleman of a human being needing to report that issue. But you can still automatically send it to the human as soon as you note that that happened. So it's at least faster, even though it's not fully autonomous."

**Recommendation 2: Graduated autonomy based on confidence scoring.**
"For full auto mode, you have to clearly define the guardrails. Easiest way to define the guardrails is to categorize past actions and what the outcome of those was." He specified: "Not Claude's interpretation or Codex or Gemini's interpretation of anything, but that exact scenario, if it has come up in the past and it has been resolved successfully in the past and is still correct in context, that lends itself to being more able or more permissible for auto resolution."

He proposed: "Let humans be your confidence score. If this problem is a known one that Cloud can resolve perfectly, great. Have that as a playbook, have that as a reference. We can do that as infrastructure. And for those ones, specifically, have someone with some power, some intimate knowledge of the system, review those and approve or deny that those can be done automatically."

### 9.4 The Golden Rule

Colin stated a non-negotiable principle at [01:58:26]: "The golden rule, we never let AI decide if something's complex or not. That's the golden rule, you know, because it is not a good assessor of what that is."

### 9.5 Critical Bug Escalation Scenario

Colin raised an edge case at [01:57:07]: "Let's say that I have a critical bug that's not allowing anyone to do anything in the app. It's completely blocked. You might as well let AI do it because you don't want to have to wait. Like, let's say that over 24 hours pass. Do you want to let that sit or do you want to have the reminder or do you want to escalate it up to another person? We have to think about that framework and propose it to Srinivas."

He also critiqued Justin's approach: "The worst thing people do here is kind of, unfortunately, like how Justin did, and say, hey, Claude, you've got, you know, what, three tries to try to fix this. And as long as it compiles, we're going to say it's good. If it fails to compile, we'll say it's bad. There's a lot to unpack there."

Saurav added: "Technically, it's only one try to fix it, because then the error itself is different."

---

## 10. Skills-Based Architecture Proposal

### 10.1 Saurav's Autonomous Agent Pitch

After Colin left the first time, Saurav proposed an alternative architecture at [01:19:56] that bypasses the traditional ML pipeline entirely. Rather than deploying separate ML models and rule-based systems in blocks, he proposed: "Subdivide these into how to read the bazel log, how to read the other structured log... all kind of those things can be categorized in five or six different skills. Load all of those skills into the agent. In the agent.md, write only the instruction that you have to use these skills."

He described the skill architecture: "Inside a skill, what you have is first the normal description of the skill, then you have different steps, so you can define a particular workflow, how exactly the LLM should work. You can also add different assets or different scripts if you want to run it deterministically. Then in addition to those scripts, you also have post and prehooks."

He proposed adversarial validation: "Suppose Codex and Claude both are working in what you call instinct, so Codex does the fixes. And for critique, we have codex or the other way around."

### 10.2 Colin's Response on Skills

When Colin returned, he engaged with the skills idea. He stated at [02:04:23]: "What's missing from their deep site, yeah, they've got MCP all day long, but they don't have skills. So it's probably safe to assume that they don't have much detailed understanding of that."

He identified the work needed to make this pitch: "Number one, have that idea fully formed, build out. Here's how this would work. Here's how people would use it. Here's how it would be maintained. Here's all the things you can do with it. Here's how it complements your system. Here's an example of what we're talking about. And if you want us to proceed with this, that is our recommendation."

He also identified the deployment question that needs answering: "How would a developer set that up? Like, is that going to be a plugin? You know, is that going to be in their VS Code? Are we going to have to write a VS Code plugin ourselves, et cetera? Like, how does that manifest?"

### 10.3 Saurav's Meta-Agent Concept

Saurav described a self-improving system at [01:59:12]: "Just create good skills, meta skill which can make the skill better based on like the results. Have it have deterministic vertical outcomes, keep like kind of a scorecard. And yep, one meta agent which looks at the scorecard, updates the skill." He also proposed background learning: "Even if you don't have like any errors in your system or any builds running. It can just like the back end agent can just go ahead, look up what are like the previous errors, how exactly they fix them, then go ahead and update your skill or your database."

---

## 11. Saurav's Observation on the Original CICD Diagram

Saurav connected the discussion back to the original project framing at [00:57:13]: "If you remember the CICD diagram which they shared with us, the blue box and the other boxes, correct? And they said that they do not have clear visibility into the CICD pipeline. If they are really doing this on a what you call WebEx chat and in this manner, so obviously they don't have and I think this is also the problem they want us to solve."

Colin agreed and tied it to the value proposition: "That's where we add the most value to him."
