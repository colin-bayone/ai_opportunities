# 01 - Standup: Blockers, Dependencies, and Escalations

**Source:** /cisco/cicd/team/source/internal_standup_2026-04-10.txt
**Source Date:** 2026-04-10 (Friday standup, pre-Srinivas meeting)
**Document Set:** 01 (First team sub-singularity set)
**Pass:** Blockers, access status, political dynamics, escalation strategy

---

## 1. The Divakar Conflict (Log Build Analysis)

### What Happened

During the second meeting with Divakar and Justin, Divakar was initially resistant to engaging with the BayOne team. Namita reported directly: "Initially frankly speaking, he was not ready to talk because he said that this is kind of conflict because the work is already done by their team." Namita talked him through it by framing BayOne's role as collaborative ("we'll be working together to take this forward"), after which Divakar was willing to continue the discussion and share more information.

### Divakar's Position

- Divakar felt BayOne's assignment to the log build analysis work was a duplication of what his team (specifically Justin) had already built.
- He was not aware that Srinivas had directed BayOne to work on this.
- After Namita's de-escalation, Divakar indicated he expects Justin to remain involved -- not necessarily working alongside BayOne, but "aware of what is going on."

### Colin's Assessment

- Colin acknowledged the dynamic is common: "Everyone's always defensive when it comes to that."
- He noted the critical hierarchy: "Srinivas did ask us to work on it. And Srinivas does overrule Divakar."
- Colin assessed Justin's existing work as a POC, not a production system. The Python script extracts only a handful of errors (approximately 10-50), passes them to an LLM for summary and suggested fixes, then attempts to apply those fixes to the PR. Colin called this "POC mode" -- it does not work at scale.

### What Needs to Escalate to Srinivas

Colin provided explicit framing for the team to use in the Srinivas meeting:

> "Met with Divakar. Divakar didn't know we were working on this and felt that what we were doing was duplicating his own team's assigned work. So what should we do, Srinivas?"

Colin's coaching on how to present this:
- Raise it **early** in the Srinivas meeting, not buried at the end.
- Do **not** characterize it as a major problem -- present it factually and ask for direction.
- Do **not** mention that Namita talked Divakar around ("I wouldn't even give that information that after we talked about it with him, it sounded fine") because if Srinivas hears it was smoothed over, he may not act on it. Colin wants Srinivas to intervene now to prevent recurring friction.
- Frame the value proposition: "Divakar and his team, I appreciate what they did, but that was the POC. We're going to show you what production looks like."

---

## 2. The Naga Scope Confusion (Pulse and Scribble)

### What Happened

Srikar met with Naga, who walked through two tools he had built within the DeepSight repos:

- **Pulse:** A WebEx scraper that extracts/scrapes data from WebEx spaces. Built 2-3 months ago. No updates since. No clear downstream use case -- the data gets extracted but there is no defined next step.
- **Scribble:** An audio-to-text transcription tool using Whisper and Pannote. Last updated 1-2 weeks ago. Naga is still actively working on this. Positioned as "more robust and efficient" than the built-in WebEx transcription.

### The Core Problem: No End Goal

Naga could not articulate what the extracted data would be used for. Saurav put it bluntly: "What does it do for me? Scrape my messages and save it to the DB? Then what?" Srikar confirmed: "They haven't had any clear vision on where to go from there."

Additionally, Naga expanded the scope unprompted -- he suggested the tools should eventually extract data from emails, GitHub, Splunk, and other platforms. This contradicts Srinivas's directive, which scoped the work to WebEx messaging and meetings only.

### Colin's Assessment

- Colin diagnosed this as a pattern common in large organizations: someone senior (Srinivas) mentions something in passing, and a junior team member builds something without a proper project plan, objective, or scope definition. "Srinivas says, 'I want this.' So that guy says, 'OK, in my side time, I'm going to do this and Srinivas is going to really like me for it.' But he doesn't really have an objective or a plan."
- Colin challenged the need for Scribble specifically: WebEx already provides built-in meeting transcriptions via its API, so building a custom Whisper pipeline may be unnecessary cost and complexity unless there is a specific business justification (e.g., audio files from non-WebEx sources).
- Colin classified both Pulse and Scribble as POCs: "If it's used in production and people depend on it for business, then it's not a POC. Before that, POC."

### What Needs to Escalate to Srinivas

Two distinct questions for the Srinivas meeting:

1. **Scope clarification:** "Naga brought up his scope was [expanded to emails, GitHub, etc.] and he wasn't really clear. You had mentioned that you wanted us to focus on WebEx. Should we go forward with that as at least our immediate goal, and later once things are working, we can add on more? Or what would you like us to do?"

2. **Scribble justification:** "Why are we doing custom audio transcription when WebEx already has built-in transcription? If there are audio files outside of WebEx that need processing, that changes the equation. But if Cisco only uses WebEx, this may be unnecessary cost."

Colin coached the team to frame this diplomatically -- not calling out Naga's work as directionless, but presenting it as a scope alignment question for Srinivas to resolve.

---

## 3. Access Status Matrix

| System | Status | Owner/Gatekeeper | Notes |
|---|---|---|---|
| **ADS Machines (temporary)** | Granted as of morning of 4/10 | Support/ticket system | 4-week temporary access for testing. Namita received confirmation just before the standup. Still needs to verify it actually works. |
| **ADS Machines (permanent)** | Blocked | Requires DCN Switching tenant | Namita can see the managecisco.com portal but the "DCN Switching" tenant is not available to the team. She contacted support, was directed to a chatbot, and has not received a response. She also raised a "bundle request" which was approved the morning of 4/10. Permanent ADS requires the tenant issue to be resolved first. |
| **GitHub repo (NX-OS)** | Granted as of morning of 4/10 | Group request via link Justin provided | Namita raised the request the night before; received approval email the morning of 4/10. Needs to verify actual access works. Once confirmed, she can review Justin's pull request containing the Python scripts and LLM workflow. |
| **NFS (log storage)** | Dependent on ADS access | Accessed through ADS machines | Logs are stored at a specific NFS location accessible only through ADS machines. No independent access path -- Namita asked Justin about alternatives (Kafka, other stores) and was told NFS via ADS is the only option. |
| **MySQL database (build metadata)** | Not yet requested | Justin's team | Namita has not raised a request for direct DB access. Current plan focuses on log files first. The build portal shows metadata (build number, date, status) but not actual logs. DB access may be needed later for build metadata correlation. |
| **DeepSight repos (Pulse, Scribble)** | Blocked -- needs Srinivas | Srinivas | Naga told Srikar that Srinivas is the right person to grant access to these two repos. This needs to be raised in the Srinivas meeting directly. |
| **DeepSight platform (ADS deployment)** | Blocked -- needs ADS first | ADS access prerequisite | Saurav noted that even running DeepSight requires ADS access, which creates a cascading dependency. |
| **Training courses** | Pending | Cisco training platform | Namita shared the training course link with the team. She raised an access request; no response yet. |
| **BayOne laptops** | Expected next week | BayOne IT (RIT) | Srikar and Namita still do not have BayOne-issued laptops. Colin noted they were supposed to have them over a month ago -- "RIT dropped the ball." Colin will follow up personally. Only needed for non-Cisco BayOne work. |
| **Cisco laptop (Colin)** | Not yet received | Cisco | Colin mentioned he has not yet received his Cisco laptop, which is why he had not seen Namita's document shared on Cisco systems. |

### Access Dependencies Chain

```
ADS Temporary (4 weeks) --> NFS Log Access --> Begin log analysis
     |
ADS Permanent requires: DCN Switching tenant (BLOCKED) + Bundle (approved)
     |
GitHub Access (granted) --> Justin's PR / Python scripts --> Understand existing workflow
     |
DeepSight Repos --> Needs Srinivas approval (escalate today)
     |
DeepSight Platform --> Needs ADS access first
```

### Key Access Concern

All access is **individual**, not team-wide. Saurav asked this directly and Namita confirmed: "It's individual access." This means every team member needs to raise their own requests for each system, multiplying the access burden significantly.

---

## 4. Political Dynamics and Colin's Coaching

### The Two Political Landmines

Colin identified two parallel situations that require careful handling:

1. **Divakar:** Feels his team's work is being duplicated. Defensive posture. Has direct control over access (ADS machines, system knowledge). Risk: if not managed, Divakar could become obstructionist on access and information sharing.

2. **Naga:** Not hostile, but operating without clear direction. Has expanded scope beyond what Srinivas assigned. Risk: if BayOne builds something that supersedes Naga's work without alignment, it creates the same type of conflict seen with Divakar.

### Colin's Coaching on Engineering Politics

Colin provided several specific pieces of guidance to the team:

**On presenting technical assessments diplomatically:**
- Do not say a system "needs rearchitected" unless you can speak deeply and specifically about why. Engineers will respond to reasoned, evidence-based critique but will get defensive at blanket dismissals.
- Preface assessments with caveats: "We'll need to investigate and see if it's compatible to be ready for production, or if a rearchitecture would be needed" -- this avoids premature judgment while still flagging the concern.
- Colin's own view: "My opinion, it's gonna need rearchitected, to be clear. I'm not saying it's not." But he counseled the team not to say this to Cisco until they have evidence.

**On framing existing work as POCs, not failures:**
- Use the word "POC" consistently. "We can keep calling them POCs because they are not finished mature projects. If people aren't using them, they're POCs."
- This reframes the conversation from "your work is bad" to "your work was a starting point, and we're here to take it to production."
- Specific language Colin modeled: "Divakar and his team, I appreciate what they did, but that was the POC. We're going to show you what production looks like."

**On using Srinivas as the decision-maker rather than fighting battles directly:**
- "A couple of these decisions we don't have to make ourselves, we can make with Srinivas in mind."
- When there is ambiguity or conflict, the approach is to present the situation factually and ask Srinivas to decide, rather than the BayOne team asserting their own position.
- This protects the team from being seen as adversarial while ensuring the right decisions get made through proper authority.

**On showing production thinking to build credibility:**
- Colin specifically called out the approach of questioning unnecessary costs (e.g., custom Whisper transcription when WebEx API already provides transcripts) as "showing production thinking."
- The framing: "I'm not saying no, I'm just saying you tell me. Do you want me to use this Scribble thing or do you want me to pull the existing transcripts? It's going to be cheaper for you."

---

## 5. Srinivas Meeting Agenda (Planned Escalations)

Based on the standup discussion, the following items were identified for the Srinivas meeting (~30 minutes after standup ended):

### Must-Raise Items

1. **Divakar conflict disclosure.** Present early in the meeting. Factual framing, ask for direction. Do not minimize or suggest it was resolved.

2. **Naga scope clarification.** Confirm that WebEx is the immediate focus per Srinivas's original directive. Ask whether expanded scope (email, GitHub, etc.) is desired or premature.

3. **Scribble vs. WebEx API question.** Ask Srinivas whether custom audio transcription is needed when WebEx provides built-in transcripts, or if there are non-WebEx audio sources that justify it.

4. **DeepSight repo access.** Naga directed Srikar to get repo access from Srinivas. Raise this directly.

5. **Gmake vs. Bazel scope decision.** Divakar recommended focusing only on Bazel. Confirm with Srinivas. Optionally mention that Gmake-to-Bazel conversion (code modernization) is also something BayOne could assist with.

### Information-Sharing Items

6. **Namita's progress report.** High-level overview of meetings with Justin and Divakar, access status, and findings about the build systems and log architecture. Namita had a prepared document; Colin was considering converting it into a presentation using internal tools but was uncertain about the 28-minute time constraint.

7. **Saurav's WebEx bot demo.** Working prototype scraping WebEx space messages into a Postgres database via WebEx SDK, webhook, and bot framework. Already functional with message categorization (human vs. bot), room-level scraping, and permission controls. Colin anticipated Srinivas would ask: (a) how was it built, (b) was it API or MCP-based, (c) what is the plan beyond exploration.

8. **Emerging use cases.** Build queue optimization (200 builds in queue, manual prioritization, 3-4 day processing delays), silent build failures (builds expected at 1.5 hours running to 6+ hours without notification), and automated build retry from WebEx thread analysis.

### Items to Hold for Later

- Detailed architecture proposals (need log access first to validate assumptions)
- Rearchitecture recommendations for Pulse/Scribble (need repo access to assess properly)
- Training course status (low priority relative to access blockers)

---

## 6. Technical Blockers Summary

| Blocker | Type | Severity | Resolution Path |
|---|---|---|---|
| No log access (ADS/NFS) | Access | High | Temporary ADS granted 4/10 -- needs verification. Permanent ADS blocked on DCN tenant. |
| DeepSight repo access | Access | High | Requires Srinivas approval -- escalate today. |
| Divakar perceives conflict/duplication | Political | High | Escalate to Srinivas for alignment -- today. |
| Naga scope undefined | Organizational | Medium | Ask Srinivas to confirm WebEx-only scope -- today. |
| Individual access model | Organizational | Medium | Each team member must request access separately. Multiplies onboarding time. |
| No Cisco laptop for Colin | Access | Medium | Colin cannot access documents shared on Cisco systems. |
| No BayOne laptops for Srikar/Namita | Access | Low | Colin escalating to BayOne IT. Not blocking Cisco work. |
| Training course access | Access | Low | Request pending, no response. |
| MySQL DB access not requested | Access | Low | Not yet needed -- log analysis is the priority. |
| Scribble may be unnecessary work | Technical | Low | Pending Srinivas's answer on WebEx API vs. custom transcription. |

---

## 7. Team Assignments and Status

| Person | Current Focus | Status |
|---|---|---|
| **Namita** | Log build analysis track -- meetings with Justin and Divakar, access requests, understanding existing Python/LLM workflow | Multiple access requests in flight. GitHub access and temporary ADS granted morning of 4/10. Needs to verify both work, then review Justin's PR and examine actual logs. |
| **Srikar** | Pulse/Scribble track -- meeting with Naga, understanding DeepSight integration, WebEx scraping scope | Met with Naga. Needs DeepSight repo access from Srinivas. Scope unclear -- awaiting Srinivas clarification. |
| **Saurav** | WebEx exploration and bot development -- built working prototype scraping WebEx messages into Postgres | Functional demo ready. WebEx SDK, bot framework, webhook, and Postgres backend operational. Exploring WebEx agents and MCP integration capabilities. |
| **Vaishali** | Onboarding -- following along, early preliminary work completed | Colin noted she has completed "some early work" that gives her a head start. Full deep-dive onboarding session planned for Monday. |
| **Colin** | Project leadership, Srinivas relationship management, meeting prep, political navigation | Preparing for Srinivas meeting. Planning to create presentations using internal tooling. Working on getting team added to the Srinivas call. Also noted a new person will be joining the project. |
