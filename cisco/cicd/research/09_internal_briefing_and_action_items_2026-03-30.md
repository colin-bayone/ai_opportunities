# 09 - Internal Meeting: Briefing Content and Action Items

**Source:** /cisco/cicd/source/internal_team_meeting_2026-03-30.txt
**Source Date:** 2026-03-30 (Full team briefing)
**Document Set:** 09 (Internal team meeting — Colin, Saurav, Askari, Srikar)
**Pass:** What changed since Set 08, new technical discussion, and action items

---

## Source Context

This document captures what Colin communicated to the expanded team, how his framing has evolved since Set 08 (March 18), and what new technical or strategic content emerged. Most factual content about the engagement was captured in Sets 01-08. This document focuses on what is new or evolved.

---

## 1. How Colin's Framing Has Evolved Since Set 08

### Timeline and Urgency

In Set 08, Colin framed the April 30 date as a "renewal date" and said they needed to show progress. Twelve days later, he is more specific and more measured:

- He now states explicitly that Q1 will not be crammed into April: "that does not mean that we are going to slam everything into April 30th for that would be normally done in in three months. Not possible."
- But he balances this with urgency: "it also does not mean that we have until June 30th to show progress."
- He introduces the "heartbeat" concept: "even if it's small, even if it's just, you know, like let's call it a heartbeat rather than a finished product, that is the best." This is a shift from Set 08's more abstract "show progress" to a concrete philosophy — visible signs of life matter more than finished deliverables at this stage.
- He reveals that he intentionally designed Q1 to be light: "I'm not worried about this because I intentionally made Q1 light when we talk about discovery plus the two items." This is the first explicit acknowledgment that the Q1 scope was deliberately scoped to absorb delays.

### Baseline Measurement

Colin introduces a concept not present in Set 08 — the need for quantitative baselines before any solution work:

- "For any project, we need a baseline first so that we can show a tangible improvement."
- He lists specific metrics they need: PRs submitted per day/week, active developers at any given time, number of branches, number of repos in scope, average PR merge time.
- If Cisco does not know these numbers (and Colin expects they do not for most of them): "hard stop. Let's do some research and figure out what this is, because of course we can pull that the moment we have access to their GitHub."
- He frames this as enabling the success narrative: "we can show, you know, with our system in the mix, look, we gave you a 45% improvement."

### Architecture Flexibility

Colin is more explicit in this meeting about leaving architecture decisions open. In Set 08, he walked through the solution approach in detail. Here, he deliberately holds back:

- "You'll notice that I never mentioned a stack, a platform, anything."
- "I keep saying system, I keep saying very high level things, but I haven't used anything specific that is for us to think through and have discussions on this week itself."
- He frames this as deliberate: "there's very few decisions here that are set in stone. The only ones that are are because they are actual project constraints, not because they are design decisions made unilaterally by me."
- He introduces the YAGNI balance: "this is that balance between the, you know, Yagni principle and actual planning... don't put yourself at a, you know, disability by not addressing it whenever you are able to the first time, but also don't make it overcomplicated too early."

### Discovery as Structured Process

In Set 08, discovery was mentioned but not operationalized. In this meeting, Colin presents discovery as a set of specific meetings to be scheduled:

1. **Local developer workflow** — understanding what developers actually do day-to-day
2. **Branching and ownership** — including the need for a service account with read access to GitHub
3. **Airflow** — finding the actual owner (since Divakar turned out not to be the Airflow contact)
4. **Hosting** — how to deploy solutions on Cisco infrastructure, who to talk to, getting autonomy to deploy without ticketing
5. **AI access and DeepSight access** — tool standardization across the team, plus becoming experts on Srinivas's platform

Colin tells the team to prioritize discovery meetings in whatever order they become available: "Do them in the order that we get the discovery calls." He expects to schedule these across the next two weeks.

---

## 2. Questions Progress

Colin reveals that he has been working through a structured question list:

- **65 total questions** prepared.
- **Approximately 47 answered** (he says "over half" and later "I think we have 18 remaining"). He answered these during in-person time at Cisco — "I was able to go whenever I was there in person and kind of hammer them with all these."
- He will share two documents: the original question sheet and an updated version with answers.
- He wants the team to maintain a **live copy** (probably Excel) for deduplication: "anything that is not covered here that you would like to know during discovery, everyone here has freedom to add whatever you want. And what we will do is we will review them together at the end of the week before we send it over to Cisco."

This is a more structured approach to discovery than was evident in Set 08.

---

## 3. New Technical Discussion: Copilot and AI Code Review

The most substantive new technical discussion in this meeting centers on the quality and appropriateness of AI-generated code review suggestions in large codebases.

### The Trigger

Askari raises GitHub's recently launched AI agent platform, which "automatically verify and do all the sanity checks and generate the test cases." He asks whether they can build on top of it. Srikar follows up asking whether this happens before or after PR submission (Saurav explains: before PR = blue box/local, after PR = green box/GitHub).

### Colin's Analysis of Copilot Limitations

Colin pivots this into a practical warning about AI code review quality:

- **Scope problem.** "Copilot is not ideal. Even though yes, it does these things, it is fairly pedantic and it does not review things in the scope of a large repository. Use them in the scope of what was changed in that immediate PR."
- **Context-blind suggestions.** "Half of the things on copilot, if you don't take them in the context of the larger PR or excuse me, the larger code base, sometimes they can be completely wrong or pedantic suggestions."
- **Example given.** Colin points to a specific copilot suggestion about PR description quality — "it used the word debug dict and only some steps return it" — and calls it a "nightmare manager type thing" that is not worth fixing with a language model.
- **Risk assessment.** "It could also happen that their code base is extremely large, so these suggestions actually cause more problems than they solve."
- **Action required.** "Part of what we'll have to do on our side before we say anything or suggest anything is check performance and you know, check performance within the context of their code base." He frames this as "internal discovery" — testing before recommending.

### Cisco's Existing Internal AI Code Review Project

Colin reveals that Cisco has a separate internal team already working on AI code review:

- "They said that they have an internal AI code review project going on from a separate team that predates this engagement entirely."
- His assessment: "If it's anything like the other Cisco projects, then that means that this is probably 2 smart people that already have 30 day jobs going. I don't believe this is actually going to be a thing."
- His prediction: "I'm going to almost guarantee that that team does not have success with this. I have a good idea of what they're doing and how they're doing it. It's going to work for very small code bases only."
- **Strategic play:** "If we can get ownership of this, then we have very good business for a very long time, even far beyond this project." He plans to push Srinivas to make a decision: either let BayOne integrate the existing team's solution, or let BayOne take ownership. He wants to "force an issue" on this.

### Cisco Developer Tool Landscape

Colin provides first-hand observations from being on-site:

- Most Cisco developers have access to GitHub Copilot because they have GitHub Enterprise.
- "The overwhelming majority of devs do not have access to what we would consider like a proper agentic tool."
- "There are so many people still doing all of their code manually and then just using copilot at the end to say that they did to double check their work or to like help with you know, basic test generation for a single file scope."
- "A lot of their teams are not using AI tools today, which is part of the issue for them is just upscaling everyone."
- This gives BayOne an opportunity to "add some value in even when we talk about what we can integrate as a custom plugin for VS Code."

### VS Code Plugin Approach (Q4 Item, Mentioned Early)

Colin frames the eventual solution as lightweight: "I'm not saying recreate codecs or cloud code, but certainly we can give a very light version of that as a way to like triage bugs that happen or you know, gates that fail." He references open source libraries ("something like open code or something") and says: "our only responsibility for that and you'll see that is in Q4, so that is far down the pipeline for us." But he wants the team aware of it now so Q1 decisions do not conflict with Q4 needs.

---

## 4. CDT and 39 Gates Strategy (Expanded)

Colin revisits the CDT vs. 39 gates problem from Set 08 but with a more explicit strategic framing:

- He is asking questions he already knows the answers to: "Is there existing documentation on the 39 gates? I already know that there's not."
- His strategic intent: "My point here is to get them to realize that 39 is not needed." He is building a case through questions: if CDT is mature, why are there 39 additional gates? Either the gates address CDT deficiencies (meaning CDT is not mature) or the gates are unnecessary (meaning they should be eliminated).
- He frames this as a value-add: "we should absolve this, if at all possible, before we try to, you know, create a solution that has to integrate both. Because if one's, you know, just a Band-Aid, why not just do the surgery and and do the fix properly?"
- Saurav contributes: points out that even maintaining documentation for 39 gates plus CDT is overhead that "should not be there in any case." Colin agrees.

---

## 5. Singularity and Tooling

### Singularity Demonstrated

Colin gives the team its first direct look at the Singularity skill. Key points:

- He describes the blockchain-like knowledge chain: "Every single meeting we get more information and we refine what we already know... rather than keeping one live living document, we want to see the progression of those."
- He shows the numbered file structure: "the set of files named one is all here. Then there's this special file that's I call it as a bridge, then set of meetings #2."
- He explicitly says the files are not primarily for human reading: "these are not meant to be read by a human, although they're certainly human readable."
- He connects it to GitHub issues: "there is another skill that you'll see that I've put together for Cloud Code that can actually go and just simply create issues on GitHub."
- He frames the value proposition: "simply by talking about things, even in our technical discussions... we'll be able to pull out the technical bits and create them as issues."
- He references Saurav's existing experience: "Saurav, this is the same as what you're used to in Talent AI for Django Forge."

### Singularity Self-Reference

At the close of the meeting, Colin states: "I'll be feeding this transcript itself into that so you can all have that the meeting notes." This is the first explicit reference in the source material to Singularity being used on its own meeting transcripts — a self-referential application where the tool processes the meeting in which it was discussed.

### Jarvis Integration

Saurav suggests automating Singularity on a scheduler. Colin reveals the plan: "I have even better for you. So I have uh this can is gonna go on Jarvis." He explains: "Jarvis is the name for the code name for what we'll have for essentially automated meeting transcriptions. It's an Airflow based project that uses language models." The plan is to add a Webex transcript pipeline alongside the existing Teams transcript pipeline.

### Tool Standardization

Colin is explicit about tool alignment across the team:

- He will not accept "just GitHub Copilot" as the team's AI tool: "That's not AI to me anymore. Anyway, that's just auto complete."
- He wants the team on the same tool platform: "if everyone wants to use cursor and Cisco provides it, no problem. It's just a matter of making sure that the overwhelming majority of everyone is on the same page."
- His concern is interoperability: "if someone creates a skill for cloud code and then you know everyone's doing great except that one poor guy with cursor who is not able to access that skill."

---

## 6. GitHub Actions Rejection (Reiterated)

Colin restates the GitHub Actions rejection from Set 08, now with slightly more context:

- "I pushed them to use GitHub Actions for all of this. I said this would GitHub Actions is going to solve about 80% of the total problem right from the start."
- The rejection is political: "a senior most person on the team told the team for many years that they don't need GitHub actions and suddenly, you know, now that it's fully mature and able to do this, they would have basically have to admit, hey, I wasted our time for two years developing a parallel system for no reason."
- Colin frames his acceptance pragmatically: "there's not a hill to die on for us."

---

## 7. Sales Training Absence

Colin reveals he was offline the prior week due to a mandatory sales training: "there was a sales training last week where essentially they for all purposes, made us put our phones in a metal box and said you can't touch them for a week." This explains any gap in communication between the March 18 meeting and this March 30 meeting. He frames his return with urgency: "I'm finally back EST. This is my number one priority to get this project on the road and ready to go."

---

## 8. Action Items

### For the Entire Team — This Week

1. **Complete the GitHub Enterprise training.** Colin will share the training link via a Webex channel. Each team member must notify Colin upon completion so he can report to Srinivas. Colin's implicit instruction about effort level: "I have no way to know how much or how little you pay attention to that training. And I have no requirements from my side... if it's a three hour training that you are sitting there for every minute of the three hours and I have no way of knowing otherwise." He also notes the training might contain developer standards worth capturing.

2. **Review the discovery questions.** Colin will share the original 65-question sheet and an updated version with approximately 47 answers. The team should read the answered questions to understand what is known, review the 18 remaining questions, and add any new questions they want answered during discovery.

3. **Study DeepSight.** Review the Srinivas webinar recording (nearly 2 hours, downloadable VTT transcript). Colin will share the link and password via the Cisco Webex chat. He suggests using Claude for Q&A against the transcript rather than watching the full video. The team should also note any deficiencies — but only flag them to Srinivas after thorough understanding.

4. **Start thinking about Q1 architecture.** Specifically for the developer box (pre-PR visibility and tracking) and branch health dashboard. No stack decisions yet — Colin wants this to be collaborative engineering discussion.

### For Srikar and Namita (On-Site)

5. **Be available for discovery meetings.** Colin will schedule meetings with Cisco counterparts across five areas (local dev workflow, branching/ownership, Airflow, hosting, AI/DeepSight access). On-site team members will attend in person. When the offshore team cannot attend due to time zones, transcripts will serve as the record.

6. **Route questions from offshore team.** Saurav and Askari will send questions; Srikar (and eventually Namita) will get them answered in person.

### For Srikar Specifically

7. **Get BayOne hardware.** Meet Rahul Bobbili on March 31 or April 1 to receive the BayOne laptop and set up the BayOne email account.

### For Colin

8. **Set up Webex channel** for the team using Cisco IDs. Share the GitHub Enterprise training link there.
9. **Share discovery question documents** — both the original and updated versions.
10. **Share the DeepSight webinar link and password** via the Webex channel.
11. **Schedule discovery meetings** with Cisco counterparts across the five areas.
12. **Set up a Claude project** for the team to do collaborative Q&A on DeepSight materials: "we'll set up a project for it. So we'll try to do kind of like a just even in Cloud desktop."
13. **Process this meeting transcript through Singularity** — explicitly stated: "I'll be feeding this transcript itself into that so you can all have that the meeting notes."
14. **Adjust meeting times** going forward to 11:00 AM EST / 8:00 AM PST to accommodate Srikar.

### Meeting Cadence

- **Immediate:** Meet again tomorrow (March 31), shorter session.
- **This week:** Meet "a couple of times this week" to build momentum.
- **Ongoing:** Three meetings per week minimum (Monday/Wednesday/Friday or Monday/Wednesday/Thursday, depending on India time zone impact). Plus ad hoc sub-team meetings as needed.
- **Formal structure** for meetings and specific responsibilities to be established once Cisco's expectations are clarified: "We will establish all of that once we have the clarity from Cisco's team as to what their expectation is."

---

## 9. Anand's Two-Week Plan Request

Not explicitly discussed in this meeting. Set 07a documented Anand's March 27 message requesting a two-week plan within a few days. Colin does not reference this request to the team, though his urgency about showing progress and his plan to schedule discovery meetings this week may be his response to it. The team is not made aware of the specific leadership ask.
