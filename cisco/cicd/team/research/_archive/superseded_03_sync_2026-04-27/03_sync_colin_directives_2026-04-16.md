# 03 - Team Sync: Colin's Standing Directives

**Source:** /claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/cisco-team-sync_4-16-2026.txt.txt
**Source Date:** 2026-04-16 (Wednesday team sync)
**Document Set:** 03 (Third team sub-singularity set)
**Pass:** Focused deep dive on Colin's standing operating instructions to the team

---

## Directive 1: Be Verbose in Team Meetings Because Transcripts Feed Singularity

**Where in transcript:** Lines 36 (timestamp 00:02:10)

**Colin's exact language:** "Keep in mind for everyone, I'm using this, I'll use this meeting transcript to help me to generate some of the files that I'm going to be sending up to Srinivas. So keep that in mind. It's okay to be verbose right now. Like I, we'll get into this. In general, it'll become more and more normal. It's weird. It's like, like I said in the last time, it's like we're prompt engineering live on a call. So it's good to share detail. It's good to be specific. Don't feel like you're talking too much. It's all for Cloud."

**Rationale:** The meeting transcript is not just a record -- it is a direct input to the Singularity skill, which will process it into structured deliverables for Srinivas. The more detail the team provides verbally, the better the downstream outputs. Colin frames this explicitly as "prompt engineering live on a call."

**Relationship to Set 01:** This is a new directive not present in Set 01. The briefing document (03_briefing_engagement_rules_2026-04-07.md) established meeting recording as important ("worth their weight in gold") but did not instruct the team to be deliberately verbose. This directive adds a behavioral instruction on top of the recording policy: not just capture meetings, but speak in a way that maximizes the value of the transcript for automated processing.

---

## Directive 2: Do Not Feel Like You Are Complaining -- Report All Blockers Fully and Transparently

**Where in transcript:** Lines 52 (00:05:47), Lines 228 (00:22:10)

**Colin's exact language (first instance):** "Don't feel like you're complaining. Just be completely, you know, straightforward about it."

**Colin's exact language (second instance):** "No matter what it is, big or small, do not feel like you're complaining. I'm just getting all the things documented for today."

**Rationale:** Colin is building a comprehensive blocker inventory for an email to Anand (Srinivas's boss) and Srinivas. He needs the unvarnished truth, not a filtered version where the team self-censors to avoid seeming negative. He repeats this directive nearly word-for-word to two different team members (Srikar and Namita), indicating it is a standing behavioral norm, not a one-time instruction.

**Relationship to Set 01:** The briefing document established "proactive outreach" and "self-sufficiency" as expectations, but did not explicitly address the psychological barrier of team members feeling like they are complaining when reporting blockers. This directive removes that barrier by name.

---

## Directive 3: Never Mention Claude to Cisco -- Say Copilot Instead

**Where in transcript:** Lines 665-675 (01:02:04 through 01:02:52)

**Colin's exact language:** "I'm going to tell him we did it with Copilot. And for Namita, for instance, what you built, I'm telling him we did it with Copilot."

**Followed by the explicit rule:** "Just the only rule is never mention Claude. I will handle the rest. So when in doubt, co-pilot."

**Rationale:** Colin frames this as a compliance and optics issue. Saurav raised a concern that Cisco might ask how the team was able to scrape WebEx chats without deploying a bot or connector, and that this "might come as like compliance or something." Colin's response is to absorb that risk himself: "Let me be the shield for all of you with that, because I'm quite good at this." He acknowledges the awkwardness ("don't get the wrong idea about me, everyone. I'm not just trying to be sneaky") but is clear that the directive is absolute. If Cisco asks how something was done, the answer is Copilot. Colin will handle any follow-up questions or explanations.

**Relationship to Set 01:** This is a new directive not present in Set 01. The briefing document discussed Copilot Enterprise as Cisco's existing tooling and the MCP strategy, but never addressed the need to obscure Claude usage. This directive introduces a standing operational security rule for all client-facing communications.

---

## Directive 4: Propose Solutions, Do Not Ask for Requirements

**Where in transcript:** Lines 547-568 (00:50:16 through 00:51:39)

**Colin's exact language:** "What I want is for us to go with the already thought out recommendation for those requirements."

**Expanded:** "Go in with that kind of thinking. You know, we will ultimately go with what they tell us to do, but you know what? Here are my suggestions and here's my rationale. Here's what I would do if this is important."

**The menu model:** "What I would do for Srinivas is say, hey, here's the menu. Pick from the menu. Which one is closest to your vision? Or are we completely off?"

**The framing of expertise:** "Rather than him saying, you know, you know, give the requirements, we will go to him and say, here is our recommendation. We are the experts here. Here's our recommendation for you on how to proceed."

**Rationale:** Colin distinguishes between two modes of engagement: (a) asking Srinivas "what do you want?" and waiting for requirements, versus (b) arriving with a fully formed recommendation and asking Srinivas to confirm, modify, or reject it. He is explicit that mode (b) is the only acceptable approach. The rationale is both about positioning ("we are the experts here") and about reading Srinivas correctly: "I can tell you he's not going to, you know, really care too much about what we're doing if we're just waiting to say, you know, what's the requirements, what to do."

**The specific example:** Colin walks through batch vs. real-time vs. polling as three processing modes, lays out the trade-offs for each, and says the team should present these as a menu with rationale. Srinivas picks from the menu. The team does not ask Srinivas which one to build.

**Relationship to Set 01:** Set 01 established "understand before solutioning" as Rule 3, which could be misread as "wait for requirements." This directive clarifies the distinction: understand the problem first (Rule 3), then come with a recommendation (Directive 4). The team should never be in a position of saying "tell us what to build." They should always be in a position of saying "here is what we think you should build, based on our understanding."

---

## Directive 5: Proactively Suggest Improvements -- Do Not Wait for Srinivas to Ask

**Where in transcript:** Lines 615-633 (00:55:46 through 00:56:55)

**Context:** Srikar and Namita reported that Justin Joseph and Cisco's team do not have architecture documentation -- not even Mermaid diagrams, just PowerPoint. Colin's response is immediate.

**Colin's exact language:** "That's something that we can do pretty darn easily. You know, we can build a skill or, you know, some plugin for them that'll go and auto document architecture every time there's a code change. This is what I mean. Don't wait for Srinivas to tell us that. If you have a good idea, let's propose it."

**The distinction Colin draws:** "This is the difference between waiting for him to tell us what to do and us saying, look, I see this as a gap. I've got an easy solution for you. Let's go and do this. And this is why you need it, because you don't have this right now."

**Handling the pushback:** Colin anticipates Srinivas might dismiss the suggestion by saying "yeah, yeah, yeah, we don't need that right now," and preempts it: "But it takes all of half an hour. You know, it's not that big of a deal, especially because they already have Copilot Enterprise. They could already have been doing this this whole time."

**Rationale:** The team's value is not just in executing assigned tasks. It is in seeing gaps that Cisco's own team does not see (or does not act on) and proposing solutions. Colin frames this as the mechanism for growing the engagement: "That's where we add the most value to him."

**Relationship to Set 01:** Set 01 established the financial incentive structure (fast, high-quality delivery leads to more work, contract extension, greater headcount). This directive operationalizes that by telling the team that proactive suggestions are a specific behavior that drives the growth mechanism. It is not enough to do assigned work well; the team must also identify and propose unassigned work.

---

## Directive 6: Frame Existing Cisco Work as POCs, Not Failures

**Where in transcript:** Lines 272-296 (00:26:10 through 00:29:48)

**Colin's exact language:** "It's good work for sure, but at the same time, it's not quite, you know, anything beyond what you could just do natively with, you know, Cloud Code or even Codex. You know, you could still get these things out. It's just a matter of having the UI for it."

**And:** "Hopefully to all of you, I don't sound like I'm like, you know, why did he do this? There's no jealousy here. It's just, you know, I don't like to do duplicate work."

**The diplomatic framing (regarding Rui Guo's NexusT agent):** Colin characterizes these as POCs -- proof of concept experiments -- rather than failures or bad work. He acknowledges they function ("they are building these things") while noting they lack production qualities. He uses the language "quick POCs" and aligns with Saurav's characterization of it as a "hackathon."

**Where this applies to the team's communication:** Colin models a specific communication pattern. When discussing existing Cisco tools with Cisco stakeholders, the team should: (a) acknowledge the work, (b) characterize it as a POC or exploration, (c) identify what separates it from production-grade, and (d) position the team's work as the production-grade evolution. This is not about criticizing Justin or Rui -- it is about framing the gap that BayOne fills.

**Colin's exact framing of the gap:** "I don't think those are really getting resolved" and "we're effectively saying that without saying it" (referring to the problem with Cisco's current processes, line 408). The team should present observations and recommendations, not accusations.

**Relationship to Set 01:** Not explicitly present in Set 01. Set 01 covered the partnership dynamic with Srinivas and the financial incentive, but did not provide guidance on how to talk about existing Cisco work. This directive fills that gap with a specific diplomatic framework.

---

## Directive 7: Confirm Architecture Claims with Code or Defensible Sources Before Presenting

**Where in transcript:** Lines 322-328 (00:31:49 through 00:32:26)

**Colin's exact language:** "That is important to have either from something that you can defend, for instance, like a meeting transcript or direct from the source person who wrote this, not just, you know, like what Srinivas does in meetings and kind of hand waving. Or number 2, having access to the repository to really see how it works in the first place and grounding that architecture of the current state in code."

**The warning:** "So that's very, very important to not guess on the architecture, because if we're wrong there, that's a credibility loss for us."

**What counts as defensible:** Colin enumerates exactly two categories of defensible sources: (1) written artifacts such as meeting transcripts or direct written statements from the person who built the system, and (2) the actual code in the repository. He explicitly excludes verbal hand-waving in meetings (he calls out "what Srinivas does in meetings and kind of hand waving" as insufficient).

**The verification process Colin prescribes:** "Don't just take what I just said and run with it. Confirm and understand it. And you can even ask the questions to say, even to people like Naga or to Justin, you know, when this gets deployed, what's the plan?" (lines 352-353). Colin instructs the team to independently verify even his own claims, not just take his word for it.

**Rationale:** Credibility is the engagement's most fragile asset. Presenting an architecture diagram that turns out to be wrong undermines the team's expert positioning. Colin would rather the team present less and be correct than present more and be wrong.

**Relationship to Set 01:** Set 01's Rule 3 ("Understand Before Solutioning") is the philosophical parent of this directive. But Rule 3 was about process sequence (understand first, then solution). This directive is about evidentiary standards -- what counts as "understanding" is not "someone told us in a meeting" but "we confirmed it against code or a defensible written source."

---

## Directive 8: Do Not Say "Rearchitecture" Unless You Can Speak Deeply About Why

**Where in transcript:** This is referenced in the topic map but expressed indirectly throughout the architecture discussion (lines 317-593). Colin's behavior throughout the architecture framework section models this principle rather than stating it as a single quotable directive.

**The modeling behavior:** Colin spends the entire architecture discussion (roughly 30 minutes of transcript) meticulously building the case for why Cisco's current approach has problems. He does not once use the word "rearchitecture" or propose a wholesale replacement. Instead, he walks through:

1. Current state architecture per application (what it actually is, confirmed against code or defensible sources)
2. Problems with the current state (scalability, cost, security, duplication)
3. Specific recommendations for improvement with rationale
4. Future state map based on those recommendations

**The implicit instruction:** By spending this much time building the case step-by-step, Colin is demonstrating that the team should never shortcut to "this needs to be rearchitected" without being able to articulate the full chain: what the current state is, what specifically is wrong, why it matters, and what the alternative looks like. The word "rearchitecture" carries weight and triggers defensiveness in clients. It should only be used when the team can defend every element of that claim.

**Key supporting quote (line 408):** "We don't have to call out and say your process is bad, but we're effectively saying that without saying it." Colin is explicit that the team should communicate the substance of a needed rearchitecture without using the loaded term.

**Relationship to Set 01:** Not present in Set 01. This is a new communication standard for how the team talks about architectural change at Cisco.

---

## Directive 9: Don't Devalue Skills Because They Are Markdown Files -- All Code Is Text

**Where in transcript:** Lines 1291-1297 (02:02:02 through 02:02:44)

**Context:** Saurav raised a concern about whether they could justify asking for significant money for a skills-based system, saying: "Even the idea itself, as well as at the face of it, it is just an dot MD file. But a lot goes behind it."

**Colin's exact language:** "Even though skills are markdown files, at the end of the day, all code is just text, you know? So it's the same thing. So don't devalue it just because it's a markdown. You know, that's still substantial work that goes in. And if skills were that easy to do, then everyone would do them. But you can already see that people aren't that good."

**Rationale:** Colin is addressing both an internal confidence issue and a client-facing positioning concern. Internally, the team should not view their own skill work as "less than" because the artifact is a markdown file rather than compiled code. The engineering effort, domain knowledge, workflow design, hook implementation, and iterative refinement that goes into a well-built skill is substantial. Externally, when presenting to Cisco, the team needs to be confident in the value of what they are proposing, not apologetic about the format.

**Relationship to Set 01:** Not present in Set 01. This directive addresses a specific psychological barrier that emerged during this meeting's conversation about the skills-based architecture proposal. It establishes a standing mindset correction: the format of the artifact does not determine its value.

---

## Directive 10: Present Ideas Fully Formed with Examples Before Proposing to Srinivas

**Where in transcript:** Lines 1302-1323 (02:02:46 through 02:05:35)

**Colin's exact language:** "We're going to have to have an example of it working, ready to go. Not a full pace one either, like a smaller scale example ready to go to show him, here's what we can do."

**The full checklist Colin provides:** "Number one, have that idea fully formed, build out. Here's how this would work. Here's how people would use it. Here's how it would be maintained. Here's all the things you can do with it. Here's how it complements your system. Here's an example of what we're talking about. And if you want us to proceed with this, that is our recommendation. Here's why."

**Rationale:** This builds on Directive 4 (propose solutions, don't ask for requirements) but adds a higher bar. For significant proposals (like the skills-based autonomous agent system), the team should not just propose the idea verbally. They should arrive with: (a) a fully articulated concept, (b) a working small-scale example, (c) a deployment/distribution plan (how would developers actually use it?), (d) a maintenance story, and (e) a clear recommendation with rationale.

**Colin's anticipation of Srinivas's reaction:** "He's going to hear that and say it sounds too good to be true. We know otherwise." Colin recognizes that the skills-based approach will seem implausibly simple to Srinivas, which is exactly why the team needs a working example -- to convert skepticism into understanding.

**Relationship to Set 01:** Set 01 established the financial incentive for fast, high-quality delivery. This directive adds a quality standard for proposals: do not bring half-formed ideas to Srinivas. Bring finished concepts with proof.

---

## Directive 11: Colin Will Be the Shield on Compliance and Tooling Questions

**Where in transcript:** Lines 665-675 (01:02:04 through 01:02:52)

**Colin's exact language:** "Let me be the shield for all of you with that, because I'm quite good at this."

**And:** "Don't feel like, you know, you have to dance around that."

**How this works in practice:** If Cisco asks how something was accomplished, the team's only responsibility is to not mention Claude. Colin will handle all follow-up explanations. The team does not need to prepare cover stories, worry about compliance questions, or navigate technical explanations about tooling. Colin explicitly takes ownership of that risk.

**Rationale:** Colin recognizes that the team members are in a vulnerable position -- they are on-site at Cisco, working with Cisco colleagues daily, and may face direct questions about their methods. By establishing himself as the single point of explanation, he removes the burden from individual team members and prevents inconsistent stories.

**Relationship to Set 01:** Not present in Set 01. This is a new role definition where Colin explicitly assigns himself the function of compliance shield. It is paired with Directive 3 (never mention Claude) but is a distinct directive about organizational responsibility.

---

## Directive 12: Use the Architecture Framework -- Current State, Problems/Recommendations, Future State

**Where in transcript:** Lines 317-593 (00:31:32 through 00:54:31)

**Colin's framework, synthesized from a long discussion:**

**Diagram 1 -- Current State:** The actual architecture of a given application, as it exists today, grounded in code or defensible sources. Not speculative. Not based on verbal hand-waving. This is "eyes wide open" (line 333).

**Diagram 2 -- Problems and Recommendations:** A non-diagram analysis that identifies: scalability problems, cost problems, security problems, duplication problems, and other architectural deficiencies. For each problem, a recommendation with rationale. Colin walks through several examples:
- No unified data layer means duplicate processing across users (scalability/cost)
- Standalone deployment means each user runs their own instance (hosting/management)
- Capabilities duplicated and locked inside individual apps instead of modular, reusable modules (extensibility)
- No proper access control beyond scoped tokens (security)
- No architecture documentation (documentation)
- No observability or tracing for AI agent actions (auditability)

**Diagram 3 -- Future State:** The team's ideal architecture based on their own recommendations. This can exist at two levels: (a) per-application future state, and (b) a master grand vision showing how all applications tie together to remove duplicates. Colin calls the master plan "much harder" and says it requires collaborative work across the team.

**The abstraction principle Colin teaches:** "How many applications would benefit from one singular place to retrieve meeting transcripts? If there is more than a few, make it a common module and an architecture diagram for a master plan and show the inheritance up the chain from the other apps." (line 589)

**The monolith misconception Colin preempts:** "Sometimes people perceive unification as creating a monolith and they say, oh my gosh, I hate this. They're wrong. That is the wrong assumption to go with. What we are showing is that you can modularize it, unify it, and still have great flexibility with microservices if you do this. You just are having common modules instead of duplicating the work." (line 589)

**Relationship to Set 01:** Set 01 established Rule 3 (understand before solutioning) and discussed the inverted pyramid / 4-tier approach. This directive extends those into a specific three-part architecture framework that the team should use for all Cisco-facing architecture work. It operationalizes the understanding-first principle into a repeatable structure.

---

## Directive 13: Think of Existing Cisco Tools as Two Complementary Entry Points, Not Competing Systems

**Where in transcript:** Lines 505-521 (00:47:37 through 00:49:07)

**Colin's exact language:** "I think I see them as two systems that work hand in hand with each other and need to have kind of a contract between the two, more so than, you know, one or the other."

**The two entry points:** (1) NFS log files as a background, proactive monitoring service, and (2) WebEx chat messages as a manual, reactive reporting channel. Colin's position is that these are not alternatives to choose between -- they are complementary.

**How they interact:** The background NFS process should run first and continuously. If a human reports an issue in WebEx chat, the system should cross-reference against what NFS monitoring has already identified: "It should reference what we have in NFS to see if we're already in the process of addressing it or have already addressed it. And to make sure if we have already addressed it, that our fix took care of what the user was saying too, to make sure that we didn't miss any detail." (line 515)

**The third case:** Colin identifies a gap neither system covers: "If it's a runtime bug that the build didn't fail on and there is no error log there." This is where WebEx-reported issues have unique value -- users notice things that logs do not capture.

**Rationale:** The team should not frame recommendations as "use NFS" or "use WebEx" but as a unified system with defined contracts between the two input channels. This prevents the false dichotomy that Namita initially raised (batch vs. real-time, NFS vs. WebEx) and replaces it with a systems-thinking approach.

**Relationship to Set 01:** Set 01's Rule 1 (everything modular and reusable) is the parent principle. This directive applies that principle to the specific question of how to architect the ingestion layer for Cisco's CI/CD monitoring system.

---

## Directive 14: The Golden Rule -- Never Let AI Decide If Something Is Complex

**Where in transcript:** Lines 1271 (01:58:26)

**Colin's exact language:** "But the golden rule, we never let AI decide if something's complex or not. That's the golden rule, you know, because it is not a good assessor of what that is."

**Context:** This comes at the end of a long discussion about human-in-the-loop vs. autonomous bug fixing. Colin walks through severity, criticality, and complexity as three dimensions of a bug, and explains that each has different implications for whether AI should auto-resolve.

**The framework Colin establishes:**
- **Severity:** Is this functionally breaking?
- **Criticality:** Does it affect other people's work?
- **Complexity:** Is this a one-liner fix or a full rewrite?

**Colin's position:** Humans must be the ones to determine whether a bug is complex enough to warrant AI intervention, not AI itself. AI should not self-assess its ability to handle a problem. This is a standing engineering principle, not a one-time instruction.

**Supporting example:** "If I say, oh, hey, Claude, my problem is that this app was written in, you know, Angular and not in Django. You know, that's not exactly a small fix. Like, that's a massive thing, and that's not something that should be auto-resolved by any AI model." (lines 1267-1271)

**Relationship to Set 01:** Set 01's Rule 2 (optimize before complexifying / 4-tier approach) established that the team should not default to LLMs for everything. This directive extends that principle into the specific domain of AI-driven bug resolution by establishing that complexity assessment itself must remain a human function.

---

## Directive 15: Meetings Are Not Wasted -- Nothing Is Lost

**Where in transcript:** Lines 1351-1352 (02:06:34)

**Colin's exact language:** "And you'll see whenever we talk Singularity, why these meetings exactly like this are perfect. So it's a big, big thing. And nothing is wasted. We'll put it that way."

**Rationale:** This reinforces Directive 1 (be verbose) but adds a motivational dimension. Colin is telling the team that the time they spend in these meetings -- even the parts that feel like rambling or tangential discussion -- is all captured and processed by Singularity into structured outputs. The team should not feel like meeting time is unproductive. It is, in Colin's framing, the primary input mechanism for the system that generates their deliverables.

**Relationship to Set 01:** Set 01 established meeting recordings as "worth their weight in gold." This directive extends that from a tactical instruction (record meetings) to a philosophical stance (meeting time is never wasted because it feeds the system).

---

## Summary: How Set 03 Directives Build On and Extend Set 01

| Set 01 Foundation | Set 03 Extension |
|---|---|
| Rule 1: Everything modular and reusable | Directive 13: Apply modularity to the NFS/WebEx dual-entry-point architecture specifically |
| Rule 2: Optimize before complexifying (4-tier) | Directive 14: The golden rule -- AI never assesses its own complexity |
| Rule 3: Understand before solutioning | Directive 4: Understand first, then propose solutions (not ask for requirements); Directive 7: "Understanding" requires code or defensible sources, not verbal hand-waving |
| Meeting recordings are "worth their weight in gold" | Directive 1: Be verbose because transcripts are processed by Singularity; Directive 15: Nothing is wasted |
| Proactive outreach / self-sufficiency | Directive 2: Remove the psychological barrier -- do not feel like you are complaining; Directive 5: Proactively suggest improvements Srinivas did not ask for |
| Financial incentive (fast + high quality = more work) | Directive 10: Present ideas fully formed with examples before proposing; Directive 6: Frame existing work as POCs to position BayOne's production-grade alternative |
| *Not in Set 01* | Directive 3: Never mention Claude -- say Copilot; Directive 11: Colin is the compliance shield |
| *Not in Set 01* | Directive 8: Do not say "rearchitecture" without deep backing |
| *Not in Set 01* | Directive 9: Don't devalue skills because they are markdown files |
| *Not in Set 01* | Directive 12: Use the three-part architecture framework (current/problems/future) |

---

## New Directives Not Present in Set 01

The following directives from this meeting have no direct parent in Set 01 and represent new standing instructions:

1. **Directive 3** -- Never mention Claude to Cisco; say Copilot instead
2. **Directive 8** -- Do not say "rearchitecture" unless you can speak deeply about why
3. **Directive 9** -- Don't devalue skills because they are markdown files; all code is text
4. **Directive 11** -- Colin will be the shield on compliance and tooling questions
5. **Directive 12** -- Use the three-part architecture framework for all Cisco-facing work

These five new directives reflect the engagement maturing from its initial briefing phase (Set 01, where rules were abstract and preparatory) into active execution (Set 03, where the team is encountering real situations that require specific behavioral guidance).
