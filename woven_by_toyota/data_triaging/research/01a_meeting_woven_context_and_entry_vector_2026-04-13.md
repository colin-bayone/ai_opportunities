# 01a - Meeting: Woven Context and Entry Vector

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-23/woven_internal_sync_2026-04-13.txt
**Source Date:** 2026-04-13 (Internal BayOne sync between Colin Moore, Jesse Smith, and Pratik Sharda)
**Document Set:** 01 (Internal sync meeting)
**Pass:** Focused deep dive on Woven context and commercial entry vector

---

## 1. Company Context: Who Woven by Toyota Is

Pratik Sharda opens the substantive portion of the meeting by establishing the parent-subsidiary relationship and the strategic reason Woven exists. His framing is the primary source of company context in this transcript.

- Pratik states plainly: "the world's largest automaker currently as of today, which might change, is Toyota." He hedges the ranking as potentially unstable, which implicitly references the competitive pressure from next-generation electric automakers.
- He identifies Woven as the entity inside the Toyota organization that is attempting to close the technology gap with Tesla and other next-generation electric original equipment manufacturers. Although he does not use the phrase "autonomous vehicle subsidiary" in this portion, Jesse Smith earlier in the call anchors the identity by describing Woven as "Toyota's autonomous vehicle subsidiary."
- Pratik characterizes Toyota's competitive position as having "been left behind on some of this technology stack." He specifies the technology stack as "autonomous driving on the camera, ADAS systems and all."
- He acknowledges Toyota does have legitimate platforms of its own: "They have certain systems that they've developed well, platforms and all." The deficit he names is not in baseline automotive engineering but specifically in "this big push on the tech itself, which is software defined like automotive architecture."

The strategic thesis, paraphrased from Pratik: Woven is the Toyota organization designated to execute the catch-up play against Tesla and the next-generation electric automakers, and the vehicle for that catch-up is software-defined automotive architecture rather than mechanical platform work.

## 2. Technology Landscape Woven Sits In

Pratik provides enough technical context to sketch the environment in which the data triaging work takes place, although he is explicit that several specifics remain unknown to him.

- The domain stack he names explicitly: autonomous driving, camera systems, and Advanced Driver Assistance Systems.
- He describes the current operating mode inside Woven as active beta testing: "they are now beta testing a lot of their devices, their vehicles, platforms that they're doing."
- The data character that surfaces from this beta testing is described as fringe cases and manually added cases within the system: "there are a lot of, as you understand, cases that are fringe cases or cases that are manually added to the system and all of that."
- When Colin Moore asks what kind of data requires labeling, Pratik acknowledges the honest answer is that he does not know, but offers the assumption that it is "data of the driving paths" collected across "a variety of data attributes."
- He lists attribute categories from memory: "the visuals, how the anomalies of the vehicle is doing, what they, so all telemetry and all of those telemetry within the autonomous system, or they could have much more sensors that I'm not aware of."
- He characterizes the operational source of the data: "these are the operations guy, right, who are running these cars, they take them out, a lot of data is captured, transferred, so a lot of ingestion happens there."

Colin attempts to refine the technical framing by offering an engineering-language hypothesis: the team may not strictly be labeling in the AI sense and may instead be performing something closer to root cause analysis or "correlation kind of map" work, which he notes is still a subclass of labeling but would shift the solution posture. This hypothesis is not confirmed by the transcript. It is presented as the kind of clarification Colin would want to extract on the first customer call.

Pratik also flags a signal from the procurement conversation that shapes how BayOne should position: "they didn't even bring the AI word there. They were just talking about the problem statement they had." Pratik interprets this as an opening rather than a negative, stating his own judgment: "I thought knowing what I know a little bit, that we can do it together with the labeling and the AI part."

## 3. Commercial Origination Story

The origination of this opportunity is traced to a single in-person lunch. The details captured in the transcript are as follows.

- Pratik and Jesse had lunch "last Thursday" with "one of the procurement guys" at Woven. In the 2026-04-13 sync, "last Thursday" refers to 2026-04-09.
- The lunch was in person and Pratik could not take notes. He emphasizes this as a caveat on the fidelity of the context he is relaying: "this we didn't have, it was an in-person, so we were over lunch, so I couldn't even take notes on what I was being told."
- During the lunch, the procurement contact disclosed that an SOW was inbound. Jesse later clarifies the scale: the Statement of Work is effectively "a bulk SOW order" for "three to four people" joining the data triaging project.
- The procurement contact raised the problem statement without using the term AI. Pratik, drawing on his own read of the situation, brought AI into the conversation by proposing "both human and AI enabled labeling."
- The procurement contact who received the AI framing responded with interest: "the person there was very curious."
- A critical structural detail: the curious party at the table was not the owner of the work. Pratik clarifies, "It was not the person we met, but another person who is part of the team that runs the procurement and sourcing." The transcript therefore distinguishes between the lunch host and a second procurement or sourcing team member who became the champion for an introduction to the work owner.
- Pratik references past experience in the same pattern: Jesse remarks, "it feels like he's done this before with Rivian," suggesting Pratik has run a comparable autonomous-vehicle data triaging play at another electric automaker.

The commercial origination can therefore be summarized as: an in-person procurement lunch where the existence of an inbound SOW for three to four people was disclosed, where Pratik introduced an AI-plus-human labeling frame that was not part of Woven's original brief, and where a senior procurement or sourcing team member volunteered to make an introduction to the work owner.

## 4. Introduction Path to Travis Millet

The identity of the work owner and the mechanics of the planned introduction are described with reasonable specificity, but with several open items.

- The work owner's name is Travis Millet. Pratik initially misremembers it as "Troy," then corrects with "So he said Travis is the one, not Troy." Jesse supplies the surname: "Travis Millet."
- Travis is described as responsible for the data triaging work and for "have these cases reported and acted upon better."
- The procurement sponsor, described by Pratik as "the actually sponsor itself or the coach that we have is a senior like leader on the procurement," committed to make the introduction. Pratik states the sponsor "is going to introduce us or maybe set up a meeting with Travis."
- Jesse notes that historical traction with Travis has been limited: "we have not got a lot of traction from him, but given this time, the actually sponsor itself or the coach that we have is a senior like leader on the procurement, so he may put us in front."
- Jesse also flags that Travis does not yet know BayOne: "I don't think he knows who I am or he don't think he knows who BayOne is for that part."
- The planned meeting format is virtual. Jesse notes that although Travis appears to be local, "We'll keep it virtual."
- Timing: Pratik is targeting the current week if possible: "most likely this week, if not, whenever Travis is available, whenever they're comfortable."
- A secondary introduction route is available. Jesse proposes that even if the dedicated discovery call with Travis does not materialize quickly, Colin can be brought onto the intake call that will accompany the three-to-four-person SOW: "once the SOW or I guess the work proposal comes in for the three, four people to come on and we do an intake call, we could even bring you on that intake call to listen in."
- Pratik explicitly endorses the dual-path approach: "the goal is to get both."

## 5. Forward-Looking Commercial Framing

Pratik uses the closing section of the call to frame this engagement as a foothold rather than a one-off transaction. Several statements in the transcript establish that framing.

- The three-month horizon: "I can already see in the next three month map, this is something we should definitely put it as one of the things we can get and at least explore."
- The doors-multiply thesis: "even if we don't get this one, I'm assuming with that we'll see a lot more conversations opening up in Woven for the AI."
- The welcome to a new customer relationship: "I wanted to welcome you to the Woven customer as well while we are at other customers."
- The hybrid-first positioning rationale: Pratik anticipates Woven's default approach may be "classical, older, obsolete," and proposes a hybrid play where BayOne offers to take the AI-leaning piece alongside the traditional labeling work. In his words: "we can do a hybrid where we are not saying just do it with AI, we are saying do it together. You can give us this piece as well while we work on this AI part of it and which could be a longer term solution for them."
- The budget-preemption rationale for Colin attending early: "if they go that route, they might exhaust the budget and all of that, right? Because they might be running with some number. So I want to have that play because I am very sure that there is play for AI in this space." Pratik is expressing concern that if the SOW for three to four staff is consumed without an AI-shaped conversation happening in parallel, the overall Woven AI budget could close before BayOne has positioned itself.
- The competence-display rationale: "Giving that value to this team and the team on the procurement and others shows the competence we have as an organization. And not only that, it also shows there are a lot of other doors that we have not even seen yet. They will show us and maybe open for us."

Taken together, Pratik frames the upcoming Travis meeting as the visible tip of a much larger intended account penetration. The three-to-four-person SOW is described as in-scope business to win, but the strategic intent is explicitly to use the procurement sponsor's goodwill to generate further introductions inside Woven over the following three months.

## 6. Open Questions Specific to This Topic

The following items are unresolved in the transcript and should be tracked as open questions relating specifically to Woven company context and the commercial entry vector.

- **Identity of the procurement sponsor.** The transcript never names the procurement lunch host or the secondary procurement or sourcing team member who volunteered the introduction to Travis. Both are referred to only by role.
- **Reporting relationship between the procurement sponsor and Travis Millet.** Pratik describes the sponsor as "a senior like leader on the procurement," but the transcript does not clarify whether Travis reports into procurement, reports into an engineering or autonomy organization, or sits in a separate business unit that procurement supports.
- **Travis Millet's exact title and organizational placement.** He is described as responsible for the data triaging work, but his function, team name, and level are not specified.
- **The Woven team name that owns the data.** Pratik gestures at it ("one of the teams, which Jesse will give the name") and then neither party names the team on the call. Only Travis's name surfaces.
- **The actual nature of the data to be triaged.** Pratik is explicit that he does not know whether it is driving-path telemetry, camera or vision data, anomaly logs, sensor output, or some combination.
- **Whether Woven intends classical labeling, correlation and root cause analysis, or something else.** Colin's hypothesis that the work may be more correlation-driven than labeling-driven is unvalidated.
- **The procurement sponsor's incentive structure.** It is unclear why the sponsor has chosen to champion BayOne internally. Pratik refers to him as a "sponsor" and "coach" without describing how that relationship was established beyond the Thursday lunch.
- **Whether prior BayOne work has been performed inside Woven.** Jesse's remark that Travis does not know BayOne suggests limited or no prior footprint, but this is not stated definitively.
- **The budget envelope behind the three-to-four-person SOW.** Pratik references the risk that Woven "might exhaust the budget" pursuing the classical path, but no budget figure or range is disclosed in the transcript.
- **Whether the introduction to Travis will be made in the current week or deferred.** Pratik targets the current week but concedes the timing is at Travis's discretion.
- **Whether the procurement sponsor's promised future introductions are generic goodwill or tied to specific known initiatives inside Woven.** Pratik predicts doors will open, but does not cite any named second or third opportunity inside Woven.
