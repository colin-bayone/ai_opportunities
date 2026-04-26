# 01d - Meeting: Discovery Call Strategy

**Source:** /woven_by_toyota/data_triaging/source/week_2026-04-20/day_2026-04-23/woven_internal_sync_2026-04-13.txt
**Source Date:** 2026-04-13 (Internal BayOne sync between Colin Moore, Jesse Smith, and Pratik Sharda)
**Document Set:** 01 (Internal sync meeting)
**Pass:** Focused deep dive on how the Travis Millet discovery call should be run

---

## Purpose of the Call

The upcoming discovery call with Travis Millet at Woven by Toyota is intended to surface the problem statement in Travis's own words. The call is not positioned as a BayOne capabilities pitch, and it is not a show-and-tell. Pratik Sharda's original framing of the opportunity centered on labeling, with both human and AI-enabled approaches in play, but Colin Moore explicitly cautioned during this internal sync that BayOne should not walk in with a labeling-shaped solution before confirming that labeling is in fact what Travis needs. Colin's stated position is that BayOne needs to understand what the data looks like and what Travis wants to do with it before framing a solution.

The broader strategic purpose is to use this single window of access to accomplish two things simultaneously: gather enough technical specificity that BayOne can return with a focused, credible response, and demonstrate enough competence on the call itself that Travis is willing to grant additional time. Pratik emphasized that Travis has historically not given BayOne much time, so the team must treat this as a narrow opportunity and avoid exhausting it with generic capability statements.

## Sequencing Discipline: Listen First, Question Second, Solution Framing Only After Data Specifics Are Known

Colin presented three items mid-meeting, explicitly noting that they only make sense taken together rather than individually. In close paraphrase:

1. **Be on the call.** Colin wants to attend so he can ask the technical questions that will surface the actual nature of the work.
2. **Wait until after discovery before pitching.** Before the conversation shifts into any kind of show-and-tell mode, BayOne needs to understand what Travis wants to do with the data. Colin's concern is explicit: if BayOne frames the work as labeling and the actual problem is correlation or root cause analysis, the pitch misses the mark and BayOne loses credibility.
3. **Address the capacity concern separately.** If the work turns out to be true labeling, that creates a staffing problem that Colin has been trying to solve internally for five months. This is not a client-facing issue, but it determines whether BayOne can say yes now or has to stage the engagement. Colin wants the discovery call to give him enough information to know how hard he needs to push Yogesh and Surej for headcount.

The sequencing discipline that flows from items one and two is that nobody on the BayOne side should be anchoring on a specific solution shape during the call. Colin's hypothesis, shared during the sync, is that Woven likely has a traditional engineering or operations team looking at the data in a conventional sense, with what they would call root cause analysis or correlation between conditions and outcomes. Colin noted that correlation can still be framed as a subclass of labeling, but it is a different kind of labeling, and the specific framing changes the solution. The call must therefore surface which subclass applies before BayOne commits to any framing in front of Travis.

Colin summarized his first two items as follows, in close paraphrase: yes to being on the call, yes to getting the information, and yes to waiting until BayOne knows more details before pitching anything.

## Attendance Plan

The call will be virtual even though Travis Millet is local. The reason is that Jesse Smith will be on-site with Pratik Sharda at the Woven location on the day of the call, so the format is set by Jesse and Pratik's physical placement rather than by Travis's location.

Attendee roles:

- **Colin Moore (virtual):** Joins the call specifically to ask the technical discovery questions. Colin's role is to probe the data, the intended outcomes, and the shape of the problem so that BayOne can return with a focused response. Colin is the technical discovery driver on the call.
- **Jesse Smith (on-site, in person):** Physically present at Woven with Pratik. Jesse has limited depth on the data triaging subject matter and has said so directly, noting that Pratik can explain the problem better. Jesse's role is relationship continuity and account presence.
- **Pratik Sharda (on-site, supporting):** Physically present. Pratik carries the prior context of the lunch conversation with the senior procurement leader and is best positioned to explain the problem framing as BayOne currently understands it. Pratik also holds the relationship with the sponsor who is creating the Travis introduction.

Because Travis does not know Jesse and does not know BayOne, introductions on the call must establish who Jesse is and what BayOne does at a baseline level, without tipping the conversation into capabilities pitch mode.

## The Sponsor-Unlock Dynamic

The opening for this call exists because of a specific relationship dynamic. Pratik and Jesse had lunch on the prior Thursday with one of the senior procurement leaders at Woven. During that lunch, the procurement leader described the data triaging problem, mentioned that a Statement of Work was coming in, and suggested that BayOne might have something to offer. Critically, the procurement leader volunteered to introduce BayOne to Travis Millet or to set up a meeting.

Pratik's read, shared during the sync, is that this senior procurement leader is acting as the sponsor or coach for BayOne inside Woven. Without that sponsor, Travis Millet has historically not given BayOne much time. With the sponsor, there is a reasonable expectation that Travis will grant a window. The access is therefore entirely dependent on the sponsor's willingness to put BayOne in front of Travis, and the call should be treated as a sponsor-enabled window rather than a direct inbound opportunity.

This has two implications for how the call is run. First, BayOne should not squander the window with generic positioning, since the sponsor is spending relationship capital to create it. Second, performing well on this call reinforces the sponsor's decision to advocate for BayOne and opens the door to further introductions inside Woven.

## The Fallback Intake Call Path

Jesse Smith raised a distinct path that does not depend on Travis Millet granting time. The procurement side of Woven has an inbound Statement of Work for three to four people to work on the data triaging effort. That SOW will generate an intake call when it lands, and Jesse offered to bring Colin onto that intake call to listen in.

This is a separate route to discovery. Even if Travis does not give BayOne time directly, the intake call for the three to four person SOW provides another venue to extract information. The people who join that intake call will have operational insights into what the data triaging work actually involves, and Colin noted that the moment BayOne has people on the ground, they will have all kinds of insights that can be pulled out.

Pratik's stated preference is to pursue both paths. The direct Travis call is the higher leverage opportunity because it allows BayOne to position the larger AI-enabled play before procurement exhausts its budget on a pure staffing engagement. The intake call is the secondary path and is useful regardless of whether the Travis call happens. Pratik was explicit that if procurement runs with the staffing-only approach and burns their budget there, the AI opportunity narrows, which is why getting Colin in front of Travis early is important.

## Specific Questions Colin Plans to Ask Travis

Colin articulated the specific discovery questions he intends to bring to the call. Each serves a distinct purpose in narrowing the solution framing.

1. **What kind of data is it?** Colin wants to know whether this is logs, telemetry, sensor output, or something generated by a running vehicle system. Pratik's working assumption is that the data includes driving path data, visuals, vehicle anomaly data, telemetry from the autonomous system, and potentially additional sensor data, but Pratik was honest that he does not actually know the full scope. This question matters because the data type determines which BayOne techniques are applicable and which are not.

2. **What do they want to do with it?** Colin wants to distinguish among categorization, classification, correlation, and root cause analysis. Pratik had framed the original opportunity as labeling, but Colin noted that if it turns out to be correlation or root cause analysis, labeling is the wrong framing. This question matters because it determines whether BayOne pitches a labeling engagement, a correlation and analysis engagement, or a hybrid.

3. **What outcomes are they after?** Colin wants to understand the downstream purpose of the work. The assumption is that Woven is trying to make its autonomous systems better by acting on reported cases, but the specific outcome Travis is optimizing for is not known. This question matters because it surfaces whether BayOne should propose a faster version of what Woven is already doing, a different methodology, or a hybrid approach with AI and human in the loop.

Colin noted that once he can get into the engineering language with Travis, the conversation will move quickly, because this is familiar territory for Colin. The questions are designed to work together: the data shape, the intended operation on the data, and the outcome sought are the three variables that determine the solution space.

## The Risk of Pitching Too Early

Colin was explicit about the downside of framing the work prematurely. His words, in close paraphrase: what would be a bad thing is if BayOne thinks it is labeling and goes in with a particular kind of labeling, and misses the mark with the client. The failure mode is not just a lost deal. It is a loss of credibility with Travis, who has historically not given BayOne much time to begin with.

The reasoning chain Colin laid out is worth preserving. Pratik's read from the lunch was that the Woven team did not use the word AI and did not use the word tagging or triaging in the way BayOne would. They described an operational problem. Pratik inferred an AI-plus-labeling shape from that description because that is the shape he is familiar with. Colin's counter-point is that an operations team with this kind of data is likely framing the problem as correlation or root cause analysis in traditional engineering terms, which means labeling as a pitch would land wrong even if the underlying techniques overlap.

The practical consequence is that the call must stay in question-asking mode for longer than would be comfortable in a typical sales conversation. Only after the data, operation, and outcome are pinned down should BayOne offer a framing, and even then the offer should be tentative and focused rather than a full capabilities pitch.

## Relationship-Building Considerations

Jesse Smith noted directly that Travis Millet does not know who Jesse is, and he does not think Travis knows who BayOne is either. Whatever prior interaction has occurred has been through the procurement side rather than through Travis's organization. This means the call is as much a credibility-establishing event as it is an information-gathering event.

Two considerations follow from this. First, Colin's technical questions need to demonstrate competence quickly. The questions themselves signal that BayOne understands the space, which builds credibility independent of any pitch. Second, Jesse's on-site presence with Pratik serves a relationship function that cannot be accomplished virtually. Being physically at Woven alongside the sponsor and the in-person introduction to Travis, if it happens in person for Jesse and Pratik while Colin joins virtually, reinforces that BayOne is a local, engaged partner rather than a remote vendor.

The longer-term relationship objective, stated by Pratik, is that even if this specific opportunity does not convert, performing well on the call opens additional doors inside Woven. Pratik framed this as a three-month map item that is worth pursuing on its own terms and that is also expected to open adjacent conversations about AI across Woven.

## Open Questions Specific to This Topic

The following questions remain unresolved as of the 2026-04-13 internal sync and should be clarified before or during the call:

- **Is the call confirmed with Travis Millet, and if so, when?** As of the sync, the sponsor had offered to introduce BayOne to Travis, but the meeting had not been scheduled. Pratik said the team was hoping to set it up during the week of 2026-04-13, but Travis's availability and his willingness to grant the time were not yet confirmed.
- **Has Travis's openness to AI as a framing been validated?** The lunch conversation did not include the word AI. Pratik inferred the AI angle independently. It is not known whether Travis himself is open to an AI-enabled framing or whether his team is committed to a traditional engineering approach.
- **What is the specific data type, volume, and velocity?** This is the first question on Colin's list and will be resolved on the call, but it is open going in.
- **Is the work closer to labeling, correlation, classification, or root cause analysis?** This is the second question on Colin's list and is the single most important framing variable for the BayOne response.
- **What is the expected budget envelope on the procurement side for the three to four person SOW?** Pratik noted that if procurement commits the budget to a pure staffing engagement, the AI opportunity narrows. The actual budget figure is not yet known.
- **Will Travis grant a follow-up meeting, or is this single window the only shot?** The answer determines whether the call must carry both discovery and initial framing, or whether discovery can be done cleanly with framing deferred to a second session.
- **Who else on Travis's team should BayOne expect to meet or eventually engage?** Pratik described Travis as responsible for the data triaging effort but did not identify other stakeholders in that organization. Surfacing the team structure is a secondary discovery objective for the call.
