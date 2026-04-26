# 08 - One-on-One: Architecture and Strategy

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/week_2026-04-14/day_2026-04-15/colin-saurav-1on1_2026-04-15_01.txt
**Source Date:** 2026-04-15 (38-minute Colin-Saurav one-on-one, Wednesday morning PDT)
**Document Set:** 08 (Colin-Saurav laptop blocker and Srinivas architecture coaching)
**Pass:** Focused deep dive on architecture strategy and technical discussion

---

## Overview

This one-on-one was originally scheduled as a quick check-in so Colin could coordinate with Saurav about the ongoing Cisco laptop blocker before Colin had to leave to meet his tax accountant. What it became, once the administrative items were handled, was the first substantive architecture coaching session of the engagement. With Saurav blocked on Cisco hardware but capable of doing pure architecture work on his BayOne machine, Colin reframed the week's deliverable priorities and, for the first time, articulated explicitly the three-slide framework he wants both tracks (WebEx and Logs) to use when presenting to Srinivas Pitta on Friday. Saurav extended that framework with technical proposals of his own: a service-app refactor of the WebEx bot, a blast-radius argument for scrape-once-per-space architecture, and an observation about the fundamental tension between Srinivas's self-service vision and a unified production service. The meeting also introduced Whisper (transcribed in the source as "Wispr") as a fallback rather than primary transcription tool, reframing the A/B-testing plan from Set 07. Finally, Colin handed off eight Mermaid.js reference files he had just added to the Singularity skill, intended to elevate the quality of the architecture diagrams Saurav will produce for Friday.

---

## 1. Colin's Three-Slide Architecture Framework

This meeting was the first time Colin articulated his three-slide framework for the Srinivas deliverable in full, explicit form. Prior sets (notably the Apr 13 team standup in Set 07) had introduced the component pieces (current state, gaps, recommended state), but Colin had not previously named them as a sequence or explained the rhetorical purpose of each slide. Here, he walked Saurav through the structure deliberately because he wants Saurav to lead the WebEx architecture document for Friday.

The first slide is the current state, framed explicitly as a proof-of-concept. Colin was direct about why this framing matters and about his willingness to defend it in the room. "So what we should do for architecture is we can phrase it as like maybe like the current state. And we can say things like POC," he told Saurav. "And phrase it like the current version is in like POC territory. So, you know, phrase that diplomatically. So, but basically do not make it sound like it is production if it is not production." Colin returned to the POC framing at the end of the meeting with explicit intent to fight for it: "Call it a POC and he is going to have to defend why it is production grade. You know, so I am ready to have that debate. Because he wanted us to do good work. I am like, okay, if you want me to do good work, let me do good work. But if you want us to do it your way and it is not good, I want you to know that I do not agree with it." This is the first time in the engagement that Colin has signaled an explicit willingness to have a direct architectural disagreement with Srinivas on the record.

The diplomatic phrasing Colin recommends for the current-state slide is the same language he used the day before with Justin Joseph: "this is a great foundation for us to build on." The construction is intentional. It does not criticize the existing work. It implies the opposite of what it says. "We are not saying, you know, one or two minor tweaks and it is production ready. I am being diplomatic in the sense that I am saying it is great for us to build on, which implies that there is a lot left to do."

The second slide is a transition slide covering gaps and considerations that Cisco should think about for production. Colin made clear that this slide is not about boiling the ocean or cataloging every possible concern, but about demonstrating that the considerations are intentional. "Making it clear that they are intentional and not just done, you know, because Claude said so, is the way to win the battle here. Basically what we are saying is I have thought about it more than you have thought about it." Colin was deliberate about expanding this beyond compute and scale: "You can say from a future scalability perspective, not just in terms of compute, not just in terms of engineering architecture, but also in terms of security, also in terms of, you know, privacy or in terms of, you know, X&Y&Z. You can bring those angles into it too." He cautioned against over-weighting: "You do not need to go like 10 slides on, you know, why this is bad, but definitely cover it."

The third slide is the recommended or proposed state. Colin emphasized that this state must be compatible with DeepSight as Cisco uses it, and that it can take whatever visual form makes sense for the content. "And then that the last screen is, and it does not have to be just one diagram. It could be several, it could be one, it could be whatever is appropriate, it could be per app, it does not really matter. But to say, here is what, you know, the recommended state would be, and here is why it is compatible with what we understand from DeepSight at this current moment."

Colin also explained why, even with Saurav owning the architecture deliverable, he intends to stay involved. "Being able to talk through architecture is half of the business of architecture. So, you know, and being able to talk through it means you have thought through it and have not just given what Claude gave you on the first pass." The thought-process-and-polish side is what Colin will help with, while Saurav does the heavier engineering reasoning.

---

## 2. Saurav's Architecture Refactor Proposal

Early in the architecture discussion, Saurav volunteered a proposal to restructure the WebEx tooling he already built. The current implementation is a bot (referred to in the engagement history as Wall-E or Volley). Saurav proposed breaking it apart into modular components. "So like currently it is as a bot, so should I change that as like a service app for like extraction and the bot for like make it modular kind of and build a MCP and that sort of it?"

Colin endorsed the direction immediately and enthusiastically. "Yeah. Yeah, that would be great. That would be great, because we can use that for a ton of different things." This endorsement is consistent with the decoupled architecture Saurav had proposed in Set 07 (scraper plus database plus MCP plus app or bot), but it is the first time Colin has agreed to retrofit the already-built WebEx bot into that pattern rather than simply applying the pattern to new work.

Saurav then extended the proposal with a security angle that had not appeared in any prior set in the research chain. Rather than scraping transcripts per user, his proposal was to scrape once at the space level and share the results across users. "Even if like you do not want to do like a single DB for suppose all the chats, all the transcripts, at least have it like at space level. So like it only scrapes one time for that space and all the users can use that one. So even if like in case of any attack, so the blast radius is only that group." This is the first time blast-radius language appears in the engagement. It introduces a concrete, defensible security argument for shared-storage architecture (it contains the damage surface if a tenant is compromised) that goes well beyond the compute-cost argument for deduplication.

Colin reinforced the broader point. "I would go like full pace with this too. The reason why I am setting this and the reason why I have transcription, if we can at least have this call as notes too, but even things like security, right? If you were trying to... access control." The access-control concern specifically is that, under the current architecture, any user can access whatever transcripts they want. "And that is not good. That is really not good."

---

## 3. Saurav's Self-Service-Architecture Observation

Saurav surfaced what may be the most important open question of the engagement: whether Srinivas is asking for a self-service POC pattern or a unified production service, and whether those two things can coexist. The observation came as Saurav was thinking out loud about why Naga is building Scribbler and Pulse as local scripts.

"I got an idea of like why they are building like [Scribbler] and everything else like this kind of scripting. So I think what Srinivas wanted something to be deployed on DeepSight so that like users can locally host it on a Podman container or something and then run those apps on their local. Okay, so that is why I think the Pulse and [Scribbler] are like kind of separate scripts which run locally."

Saurav then laid out the architectural tension this creates. "But that is, what do you call it? In one sense, it is good, it is modular, you can deploy it locally and everything else. But the other bad thing is like, if you want to deploy a chat bot or a scraper off using this architecture and no shared DB, then it is like you are scraping the same thing for like every person and duplicating that data into like different databases."

The resolution he proposed was a hybrid: some layers monolithic (the API, extraction, and storage layers), with the user-facing bots and agents modular and plug-and-play on top. "In which you have to get your transcripts out or download the audio files and scrape the messages and then push them to a separate location, suppose the DB or BLOB storage or any other container. And then that is like your, what do you call, fixed infra. And then based on those, you can select your own MCPs, like what data sources you want. Those can be like deployed locally and configurable. That what exactly type of bot you want to connect. Suppose you want your meeting transcript bot. So you take the data source of the transcript table, okay, and in the what you call in the bot you write your own prompt or we can provide like predefined prompts. So like you can custom like build your own use cases kind of that way that we have back end infra taken care of and these are some plug and play components you can just plug them and what you got it can solve different use cases for different users."

Saurav was explicit that this is a question for Srinivas, not a conclusion: "Clarity from his end, like what type of what do you call setup he wants, like is it okay to make some of it as like monolithic, like the API layers?" The architecture document on Friday needs to either propose an answer or surface this question to Srinivas directly.

---

## 4. Whisper as Fallback, Not Primary

Colin reframed the role of Whisper (transcribed in the source as "Wispr") in the engagement. Prior sets had treated Whisper as a candidate transcription engine to be evaluated head-to-head against WebEx native transcription through A/B testing. In this meeting, Colin introduced a new observation from his own use of WebEx transcripts that shifts Whisper's role from competitor to fallback.

"The one thing that I did notice, by the way, for [Whisper] is that a lot of the times there is some transcriptions that say the speaker was not talking clearly or was not talking in English and transcripts are not available." He identified accents and mumbling as likely causes. "I think it has to do with certain accents or even just the way that people talk, like some people mumble a little bit, but still, it is, you know, you would not want a fail-safe, which you could have, that would make sense then for [Whisper]."

The architectural conclusion was clean. "You could have [Whisper] as kind of the fallback for Cisco transcription. If the transcription is not available or fails, then use [Whisper] instead. That cuts down the, you know, the usage. That makes it make sense." The economic logic here is important: Whisper is more expensive (compute or API cost depending on deployment), so running it on every meeting would not pencil out. But running it only when WebEx native transcription fails amortizes the expensive option across the small fraction of cases where it is actually needed.

This reframes the three-tier A/B testing plan from Set 07. The goal is no longer to pick one winner between transcription engines. It is to use the cheap, always-on option (WebEx native) as the default path and reserve the expensive option (Whisper) for the failure cases. This is closer to a cascading-fallback architecture than a bake-off.

---

## 5. Unified-Layer Architecture Vision for DeepSight

The most ambitious architectural content in the meeting was Colin's articulation of what the "proposed state" slide should advocate for, and Saurav's immediate extension of it to Cisco's existing tools.

Colin described the target architecture as a unified-layer design built on top of DeepSight. "It is fairly simple. Like, let us say, like, you know, maybe like a unified space for MCP, a unified space for databases, a unified space for even like a service layer to access the resources." He contrasted this with the purely modular, distributed approach Cisco currently favors. "It is all fine and well when things are modular, but how do you scale that?" Saurav immediately picked up the thread: "Like an at-org level of like Cisco suppose 5000, 10,000 employees are going to use it. How are you going to scale that with compute?"

Colin then delivered a blunt assessment of the current state of Cisco's DeepSight ecosystem, which he has been exploring through the repositories. "Even just look at their repositories today. I mean, of course you cannot because you do not have your machine. But if you look at their repos today, it is just a dumpster fire. I mean, they have like 30 repositories that do not do anything. And what they are doing is they are like, for instance, for MCP, they are literally just copying and pasting the code and calling it modular. That is not modular. That is technical debt that is spiraling, you know, that they are not even aware of."

The key framing move that makes this pitch survivable for a Srinivas audience is that unified layers are not a retreat from modularity; they are a complement to it. "Proposing unified layers and single points of entry to things is a good approach. It is a production approach. And it is compatible still with DeepSight and that methodology that he wants things to be modular reusable, you are not creating a monolith, you are just creating a unified place for access and maintenance."

Saurav extended the vision directly to Cisco's existing tools. "If they really want like convert their [Pulse] into a service app which we can connect like on the service layer. Similarly, [Scribbler] also, we can have it one part where it is downloading and all at the service layer and where it is what you call converting the transcript as maybe a sub process and after that it is saving that to the DB and for like for more details just add an agent over there." The point was that the proposed architecture is not a replacement for what Naga has built. It is a home for it. "We are also thinking about how to bring what they have already built into the system."

Saurav did flag a dependency. He still does not have repository access to Pulse or Scribbler, and Namita has not yet reported DeepSight access either. "We will need more clarity on, like, how exactly is DeepSight and [...] Pulse and [Scribbler], everything is like structured and built. I don't know if they are able to access DeepSight and deploy something on their end. And if like Justin and Naga would be willing to provide the repo access of like [Scribbler] and this other tool. [...] Pulse, yeah, pulse." Colin took this as an action item for himself and said he would escalate it to Srinivas, noting that DeepSight access had been Srinivas's own action item from the prior Friday meeting and that he should not need to be reminded.

---

## 6. Mermaid.js Integration Into Singularity Skill

Colin used the last portion of the meeting to hand off eight Mermaid.js reference files he had just added to the Singularity skill. The handoff was not polished. "This is what I am adding into the Singularity skill. I am just going to give you the files because I do not have it ready. I will explain what is going on with it in a moment. Basically, I had to clean up the folder structure and I am like, that is a mess. I need to fix that and polish it up before I push it onto V2." But the content was substantive and directly relevant to the Friday deliverable.

Colin had used an agent to do a deep dive on every feature of Mermaid 11.2 and had assembled the results into eight linked HTML files. "So there is a total of, I think, 8 files that all link together. Now I am going to imagine that the URLs will be broken because they are probably pointing to my local path. But I would fix those with Claude real quick. It is just pointing the HTML files to each other." Saurav's action item, implicit in the handoff, is to use Claude to repath the local URLs so the tab-navigation works.

The contents Colin walked through covered shapes, text formatting (including Font Awesome and Feather icons), class definitions for reusable styling ("so that code does not start to get scrawling"), subgraphs (box-in-a-box), and diagram types. He called the diagram-types file the most important. "This has the most useful stuff for any kind of architecture or planning, like even here for classes, if you wanted to share like database models and, you know, relationships." Beyond class diagrams, the reference covers Gantt charts, pie charts, mind maps, milestone trackers, and git graphs.

The reason the reference files matter for Friday is specific. "Claude tends to default to something incredibly simplistic." Even with Mermaid understanding in its training data, Claude defaults to flow charts. The reference library gives Saurav (or Claude, via Saurav) a catalog to point to. "You could look at this and say, you know what, I would like to visualize it like this. Here, go to this file for a reference on to how to do that." Colin also included four markdown reference files covering the comprehensive shape library and SVG scaling for Claude-friendly document embedding.

One known limitation Colin flagged: "Some of these things, if you notice they get cut off, just know that that is a JavaScript issue. All you have to do is pad the container that it is in. So it is just a padding thing." Trivial to fix at render time, not a blocker for use.

---

## 7. Critical Assessment of Current Cisco Work

Interleaved with the architecture coaching was a shared, increasingly direct critical assessment of what Cisco's internal tools actually are versus what they are claimed to be. Near the end of the meeting, Saurav offered a clean test case for the Pulse claim.

"If it was like production grade, now I have like a very good question for them. They are saying like Pulse is ready and running, correct? It is a scraper. So they should already have integrated that on like an NX-OS chat and already have the data in the DB, correct? [...] Then they should not have asked to like, what do you call it, go ahead and build the scraper as well as the bot and then do the analysis. They should have like shared just the data like here is all the scraped data and you do an analysis on this." Colin agreed immediately: "Right, exactly, exactly."

The implication is significant. If Pulse were actually production, the BayOne scope of work would look different (it would begin with analysis on the existing scraped data, not with scraping). The fact that BayOne has been asked to build the scraper, bot, and analysis from scratch is evidence that Pulse is also in POC territory, not production. This aligns with the three-slide framework: Pulse and Scribbler and the BayOne-built WebEx bot are all POCs, and the proposed-state slide is about how all of them fit together into something that could become production.

Colin and Saurav also share a working heuristic about how much of what Cisco says verbally is reliable. "Even there is a guy that had an app hosted. So even for them in production right now, they are still, you know, really in POC mode." The implicit rule is that verbal production claims should be treated as approximately seventy percent correct and thirty percent misremembered or misstated, and the architecture document should not take Cisco's self-description at face value.

---

## 8. Saurav's Delivery Responsibility While Laptop Is Down

The administrative frame of the meeting was the laptop blocker. The first fifteen minutes were spent on documentation logistics: Colin asked Saurav to send him a factual written account of the IT support interaction, with the ticket number included and with a bolded note about the two-month repair timeline, so that Colin could escalate to Srinivas and Anand. Colin was willing to purchase a Mac under the BayOne statement of work rather than wait. "If it is going to take any longer than a week here, we are going to get behind. At this point, can I take it into my control and just buy the laptop under the SAL because your IT is incompetent?"

The operationally important decision that came out of the laptop conversation, however, was the reassignment of Saurav's near-term responsibilities to work that does not require Cisco hardware. "I am going to shift a couple of responsibilities on to you that you can do without Cisco hardware." Architecture documents and diagrams are doable on BayOne hardware; repository exploration and any work touching the Cisco internal environment are not.

Specifically, Saurav will lead the WebEx architecture deliverable for Friday. He has what he needs to do it. "At least you have the WebEx chats. So what we can do is grab the, and you will have a way to grab the transcripts anyway from what you had built. So we can get those, start to get some architecture put together for Srinivas." The WebEx scraper Saurav built previously can still produce transcripts; the chat history is accessible; the architecture work is primarily thinking and diagramming, which does not require the Cisco loaner laptop. Colin noted a political nuance: "I do not want Srikar and Namita Vaishali to know that because they are going to say, hey, why am I not involved there? And I am like, because you guys have laptops number one and number two, I want you to keep going on here, especially the two that are in person." The reassignment is real, but quiet.

The immediate asks for Saurav before Friday are therefore: write up the factual laptop account for Colin to escalate; on today's team meeting, collect status from the rest of the team since Colin will miss most of it due to tax appointments; receive the eight Mermaid reference files and use Claude to repath them; and begin the three-slide WebEx architecture document with POC framing, a gaps slide that expands beyond compute into security, privacy, and access control, and a proposed-state slide built around unified layers over DeepSight that accommodates Pulse and Scribbler as service apps.

---
