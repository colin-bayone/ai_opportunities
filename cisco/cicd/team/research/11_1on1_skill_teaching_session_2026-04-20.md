# 11 - One-on-One: Skill Teaching Session and Drill-Down Context

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/week_2026-04-20/day_2026-04-20/srikar-and-colin-issues-breakdown-drilldown_01.txt
**Source Date:** 2026-04-20 (Monday morning Colin-Srikar 1:1, approximately 30 minutes, same day as the CSIRT incident)
**Document Set:** 11 (Colin-Srikar skill teaching session on nxos-issue-categorizer approach)
**Pass:** Focused deep dive on the teaching content and drill-down approach

---

## Session Framing

This was a one-on-one working session between Colin Moore and Srikar Madarapu on Monday morning, April 20, 2026. The recording is 1,102 utterances and roughly 30 minutes of working time. Colin and Srikar each contributed 276 utterances, an evenly balanced coaching dialogue. The meeting coincided with the early hours of the CSIRT incident cascade captured across Team Sets 06 through 06g, which surfaces inside this transcript only during the later policy-reminder segment.

The purpose was twofold. First, Colin wanted to walk Srikar through the approach for subclassifying the 708 bugs-and-errors category that Srinivas had requested during Main Set 12 and which had become Srikar's Wednesday deliverable (Team Set 10). Second, Colin used the session as a live teaching moment on the Claude Code skills methodology, the BayOne plugins repository, and how the nxos-issue-categorizer skill would handle the ambiguity problem.

## Opening: "No One Knows Everything"

Before showing any content on screen, Colin set an explicit psychological framing. He told Srikar, "no one knows everything. So if we talk about something and you don't feel, you know, confident in it, it's totally fine... There's new things every day, you can't. So if you don't, that's okay, I'll teach you. If you do, great."

Colin anchored the framing by referencing a prior bad experience with a senior colleague who had mocked him for not knowing every aspect of artificial intelligence. The tone was permission to admit unfamiliarity. This stands in contrast to the harsher retrospective tone Colin used in Team Set 10 (internal-only context, not shared with Srikar) where he commented that some current contractors "would not pass an interview with me." Inside this session, that frustration was entirely absent. The interaction was coaching, not evaluation.

## The Business Intelligence Framing

Before getting into the mechanics, Colin reframed the drill-down problem away from per-issue accuracy and toward bulk visualization. He drew on his former role running both artificial intelligence and business intelligence at his prior employer. He told Srikar, "what BI tells you is that, you know, you put numbers on a screen, and I'm not by any means, please don't take away from this that I'm saying to make up things. But the thing is, if information is presented well, people rarely question it."

He then applied this to the drill-down. "Even though things are a little bit ambiguous right now, I think the main point is not the, you know, per issue granularity of what specific categorization is this, but more like the bulk picture. Like as a whole, this is what Srinivas is trying to get at. He's trying to say, you know, most of the issues are because of this."

The practical consequence was permission to accept some ambiguity in individual categorization rows as long as the aggregate distribution was clear and defensible. Precision per row is not the deliverable; visualization legibility matters more than whether every message is perfectly labeled.

## The Skills Methodology Primer

Colin explained that skills originated at Anthropic for Claude but have become universal, with equivalent mechanisms in other environments including Codex. He described his own journey from skepticism to conviction. "I was honestly very skeptical of this before we started out with them. And then, you know, after I used for a while, I was like, oh my gosh, this is actually somewhat more useful than just about anything else that's come out so far, including MCP, because they are very, very flexible and they're very easy to make."

He crystallized the definition in one sentence: "at the end of the day, a skill is nothing more than a markdown file. That's it." This framing was the foundation for a later point about intellectual property portability that Colin wanted Srikar to internalize.

## Srikar's Familiarity Baseline

Colin asked Srikar directly about his comfort level with skills. Srikar self-assessed honestly: "I haven't used skills, but I've been going through like when I started like connecting with like Saurav and Team. So I was like going through all those. So I haven't like built anything on it, but I've been like going through like how we can create, like how we can use it."

He then raised an important constraint: "because we don't have like access to the cloud, like in the in our Cisco machine, but I have it here on my personal machine, so yeah, I can I can create one." This is the Cisco laptop restriction that had been discussed previously across Team Sets 07 through 09. Claude Code is not approved on Cisco hardware, which forces all skill-based experimentation onto personal laptops or pending BayOne-issued laptops. Srikar also confirmed, "I did not get the BayOne laptop yet. I'm using my personal laptop." The BayOne laptop for Srikar was still pending at the time of the session.

Srikar offered to lean on Saurav for peer support: "I can connect with Saurav also, like on understanding like skills in more detail." Saurav had been building skills over the prior weeks (Team Sets 07 through 09) and had taught Namita a folder-based Claude Code workflow. Colin's implicit model here is hub-and-spoke: Colin handles 1:1 deep teaching, Saurav provides peer reinforcement.

## BayOne Plugins and Skill-Forge Distribution

Colin pointed Srikar to the BayOne plugins repository, which he described as organizational plugins that any Claude Code user inside BayOne can install through the Claude Code sign-in flow. He emphasized that the installation process itself is self-documenting. "If you're ever not sure, just ask Cloud. Because Cloud is uniquely equipped to, you know, enable itself like that. So even in VS Code, it'll help you out. Now, once you invoke Cloud, you say like, hey, if I'm not sure how to install this plugins repo, just give it the link, say, how do I do this, follow the instructions."

He walked Srikar through the folder structure of the plugins repository, pointing out the core-tools subfolder and the skills underneath it. Of particular focus was skill-forge, which Colin contrasted with the default skill-creator shipped by Anthropic. "Skill Creator skill helps you to build skills... as if you're a high school student. Compared to Skill Forge, Skill Forge will help you create skills as if you're like the number one scientist at OpenAI. So they are night and day."

Colin also introduced a key operational feature of skill-forge: the skill self-updates. It rewrites its own markdown as new Claude Code features are released, removing the need for human maintenance of documentation currency.

## IP-Portability Insight

Colin offered an important framing about why these skills are shareable across Cisco without undermining BayOne's value. "These are universal across BayOne. We can bring these in for Cisco too. They're not really proprietary because what you'll see is at the end of the day, a skill is nothing more than a markdown file. That's it... by the time Cisco says, oh, this is really good, this is super awesome, I'll already have 30 versions that are better. So for me, it doesn't matter because they move very quickly."

The embedded principle: specific skill artifacts are not the moat. Methodology, pace of iteration, and the accumulated experience of building skills are the moat. This framing allowed Colin to be generous with IP in the Cisco context without compromising BayOne's competitive position.

## Live Walkthrough: Building the nxos-issue-categorizer

The bulk of the session was Colin sharing his screen and building the nxos-issue-categorizer skill live in Claude Code using skill-forge. Srikar attempted to follow along on his own machine using Cursor, but ran into setup friction. Rather than slow the session down, he asked Colin to just run through it on screen and offered to reference the recording later.

Colin walked through the skill-forge invocation, preflight checks, question flow, and architectural decisions. Key moments:

1. **Invocation discipline**. The user must see the explicit "use the skill, skill-forge" confirmation prompt. "This is critically important. If you do not see this, it is wrong. Do not allow Claude to say, I read the skill.md file and I know I understand the workflow even though the skill is not registered."

2. **Category count guidance**. When Srikar suggested specifying five or six initial categories, Colin pushed back: "Don't do that. The reason for that is that you don't know how many categories there are. So if you tell it five, it's going to force everything into 5 buckets."

3. **Single-threaded category discovery, agentic batch processing**. Colin kept initial category discovery as a single-threaded Claude session while allowing batch processing to happen agentically. "The first step is read the file at a high level and try to come up with categories. Now that step, is that agentic? No. As a hard rule, absolutely not, because you want consistency here... But once those categories are written, then you can process them in batches of 25 issues at a time."

4. **Thread integrity**. When Srikar raised the point that thread replies inherit context from parent messages, Colin had Claude codify it. The final design included a pre-processing step to build a thread map, identify root messages, and ensure children inherit the parent category.

5. **Hooks and subagents**. Hooks are for workflow enforcement. Agents without write permission are worse than useless. "If the agents don't have write permissions, they serve no functional purpose." Claude has a hard limit of seven parallel subagents.

6. **Stateful databases**. The skill persists results to SQLite and produces markdown artifacts for human review. The preflight check verifies the database exists before continuing.

By the end of the live build, the skill had generated its folder structure, SKILL.md file, supporting scripts, and a threadmap.json with approximately 2,000 root messages and 2,200 children across the 4,200-message CSV. Colin then demonstrated running the skill, correcting a batch-size issue on the fly, and showing the first categorization batch producing 17 categories rather than a prescribed number. The working repository is at /home/cmoore/programming/issue-categorizer-demo/ and contains the full skill, scripts, SQLite database, thread map, HTML report, and source CSV.

## Deterministic Early, AI When It Makes Sense

Near the end of the session, Colin articulated his core methodological principle. "You can make these reliable by using deterministic early... Deterministic early, AI when it makes sense. That's the mantra. Don't use it too early. Don't use it too late."

Colin contrasted this with a former colleague who spoke about "the power of ChatGPT" as if any language model could solve any task at any scale. "There is no magic wand that ChatGPT, Claude, Gemini, anything has that makes it universally omnipotent towards any task... you can't just give Claude a thousand-page PDF and expect it to generate a good summary."

The walkthrough makes the deterministic-early principle operational. CSV parsing, thread mapping, batch construction, and category persistence are all deterministic. The language model is applied only where the ambiguity of user-written issue descriptions genuinely requires semantic reasoning, and even then within tightly controlled batch boundaries.

## CSIRT Policy Reminder Embedded in the Session

Mid-session, while waiting for the skill to generate, Colin pivoted to the Namita incident. He walked Srikar through what had happened: Microsoft Teams installed on a Cisco laptop against instructions, Cisco source code sent to a non-Cisco email, an 80-gigabyte zip file shared through the wrong channel, and an AirDrop attempt that escalated the situation. Colin was clear that Srikar had done nothing wrong but wanted every team member to hear the rules directly.

The rules: do not install Teams on a Cisco laptop, use WebEx only for file transfer, share Cisco materials only to cisco.com addresses, do not work around Cisco IT blocks, escalate to Colin when unsure. Srikar confirmed he had been following these rules and was keeping Cisco and BayOne work separate on his personal laptop.

## Handoff for Wednesday

Colin's stated goal was to give Srikar enough context and tooling to complete the Wednesday deliverable. The intended handoff model was that Colin would share the full skill repository and let the skill run to completion in the background on his own machine. Once finished, Colin would share the resulting SQLite database with Srikar, who would then only need to build the visualization layer on top. "You'll get from me the actual just SQLite database. And then at that point, you know, you'll be able to do any kind of visuals very easily because it's already in database format."

Colin was explicit that visualization and sense-making were still Srikar's to own. "I'm not trying to say your work for Wednesday is done. You know, you still have to worry about the visualization. You still have to worry about, you know, making sense of it and checking the output here." He suggested matplotlib or any similar library, and pointed Srikar to talent.bayone.com for pulling transcripts through the singularity skill as a next experiment.

## Retrospective Context

This session is notable in light of what followed. Per Team Set 13 (April 22), Colin reported that Srikar produced zero progress in the 36 hours after this meeting, and Colin ended up building the full categorization deliverable himself. The finished artifact Colin described in Team Set 13 matches the architecture designed in this session: deterministic preprocessing, LLM categorization with traceability, 78 final categories, SQLite backend, HTML eCharts reports with weekly, monthly, and daily views plus a race chart and drill-down popups, the issues.dat filename rename to evade Cisco file scanning, and the 16,749-line thread-map JSON.

The coaching appears to have been well-received in the moment. Srikar said, "I had like a couple of questions. I think this session like clear all those doubts I had." The execution gap does not diminish what Colin taught, but it does set up the pattern observation captured in Team Set 13: coaching-heavy handoffs do not always produce output when execution capability is uneven.

## Cross-References

- **Team Set 07**: BayOne plugins first introduced conceptually, Cisco laptop Claude Code rule established
- **Team Set 08**: Mermaid reference HTML files shared with the team, referenced here as resources inside the plugins repository
- **Team Set 09**: Saurav's folder-based Claude Code workflow demo to Namita, peer teaching pattern being replicated with Srikar here
- **Team Set 10**: Wednesday deliverable assigned to Srikar, internal-only skeptical commentary about contractor capability
- **Team Set 13 (April 22, retrospective)**: Srikar non-progress after this session, Colin built the full nxos-issue-categorizer artifact himself
- **Main Set 12**: Srinivas's original ask for top-5 subclassification that drove this session
- **Main Set 13**: Pulse and Scribbler deferred, common-issues categorizer becomes the Wednesday priority
- **Working repository**: /home/cmoore/programming/issue-categorizer-demo/ contains the complete nxos-issue-categorizer skill, supporting scripts, SQLite database, thread map, HTML report, and source CSV that Colin built during and after this session
