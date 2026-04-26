# 05 - Team Prep Meeting: Pulse, Scribble Naming Resolution and Naga's Position

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-17/cisco-cicd-friday-meet-and-sync_01_formatted.txt
**Source Date:** 2026-04-17 (Friday morning prep meeting for Srinivas afternoon meeting)
**Document Set:** 05 (Internal BayOne prep meeting)
**Pass:** Focused deep dive on the Pulse and Scribble naming, Naga's stance, and Colin's pushback

---

## 1. Summary

During the Friday internal prep meeting, the BayOne team finally resolved a tangled mess of naming around two applications owned by Naga's team that have been orbiting the CI/CD scope. Colin had been carrying an incorrect mental model for weeks, and Srikar corrected it on this call. The team also surfaced, for the first time in unambiguous terms, Naga's position that his projects are separate from the CI/CD engagement and should not overlap. Colin pushed back strategically on that stance, arguing both procedurally (Naga does not have the authority to unilaterally declare something out of scope) and architecturally (separation contradicts Srinivas's explicit modularity directive). Saurav closed the section by raising a broader scope-drift concern that the pattern of new tools and new projects keeps appearing with no stable boundary.

---

## 2. The Naming Tangle: Three Names, Two Tools

Until this meeting, the team had been loosely using four different names (Pulse, Scribble, Scribbler, Scrubber) to refer to what turned out to be two applications. The resolution reached on this call:

### 2.1 Pulse

- **What it is:** The WebEx scraping tool.
- **Current implementation:** At present, Pulse is scoped to WebEx scraping only.
- **Long-term trajectory:** Naga's team has broader ambitions for Pulse that extend well beyond WebEx scraping. The WebEx scraping capability is described more as a foundational building block of Pulse rather than the final product vision.
- **Ownership:** Naga is the current owner and is running it on an independent trajectory.

### 2.2 Scribble / Scribbler / Scrubber

- **What it is:** The audio transcription tool (the functional counterpart to what Colin previously assumed was Pulse's role).
- **Three names, one tool:**
  - **Scribble** - the name the BayOne team originally received.
  - **Scribbler** - the name Naga later provided as an update. Per Srikar, **Scribbler is the final, official name.**
  - **Scrubber** - the name that appears on GitHub, inside the team's code/repo naming conventions.
- Srikar confirmed that Scribble and Scribbler refer to the same thing, and that Scrubber is the GitHub-side artifact of the same project rather than a separate tool.

### 2.3 Colin's Prior Misunderstanding

Colin entered the meeting believing that **Pulse** was the transcription tool (the "whisper" one, as he framed it). Srikar corrected him directly: Pulse is web scraping, not transcription. Colin acknowledged the confusion openly and characterized the naming situation as a genuine mess, noting with some irritation that the underlying name is not even a good one and has now been reused in three variations. This correction reset the team's shared vocabulary for the rest of the conversation and for the upcoming Srinivas meeting.

### 2.4 Access Status

As of this meeting, BayOne has access to **none** of these repositories. Not Pulse, not Scribble/Scribbler, not the Scrubber GitHub presence. Srikar noted that Naga neither provided access to the rebuild nor shared the links directly; any access would have had to route through Srinivas.

---

## 3. Naga's Position (via Srikar)

Srikar met with Naga in person earlier in the week. Based on that interaction and Naga's most recent message, Srikar summarized Naga's position for the team:

- Naga considers the two projects (Pulse and Scribble/Scribbler) to be operating independently of the CI/CD work.
- Naga intends for both projects to continue moving separately, on their own trajectories, with their own roadmaps.
- Naga does not believe there is meaningful overlap between his work and the CI/CD engagement that BayOne is delivering.
- The practical consequence Naga is signaling: he does not see any integration requirement, collaboration requirement, or shared-scope obligation with BayOne's CI/CD deliverables.

Srikar's read was that Naga is not necessarily being difficult, but his stated position effectively walls his work off from BayOne's scope.

---

## 4. Colin's Pushback

Colin's response was that Naga's stance cannot stand on its own, and the pushback had two distinct legs.

### 4.1 Authority: Naga Is Not the Decision-Maker Here

Colin was explicit that whether Naga's projects overlap with BayOne's scope is **not Naga's decision to make unilaterally**. If Naga has been informed of the full scope of BayOne's CI/CD engagement and is making an informed judgment that his work does not touch it, that is one conversation. If he has not been briefed on BayOne's scope (which Colin suspects is the case), then his declaration that there is no overlap is not credible because he lacks the information to make that call. The scope-overlap question is one that needs to be settled by Srinivas, not by Naga.

### 4.2 Architecture: Separation Contradicts Srinivas's Modularity Directive

The second leg of the pushback is architectural. Srinivas has given BayOne an explicit directive to build things in a modular, reusable fashion. Pulse's WebEx scraping function and BayOne's CI/CD WebEx scraping requirements are directly adjacent work. If Pulse is walled off as a separate project, then either:

- BayOne duplicates WebEx scraping effort that Naga's team is also building, which is the exact anti-pattern Srinivas told BayOne to avoid, or
- Naga builds WebEx scraping with no awareness of how BayOne will need to consume it, and the two implementations diverge in ways that will require rework later.

Colin's framing is that **Pulse and Scribble should not be treated as standalone product projects. They should be treated as infrastructure-level components that are reusable across projects.** Under that framing, the question is not "do these projects overlap" but "how should these shared building blocks be factored so that CI/CD, Pulse, and Scribble can all draw from them." That is the conversation Naga is preemptively closing by declaring separation.

### 4.3 Pulse Is the Primary Overlap, Scribble Is a Separate Conversation

Colin drew a clear distinction between the two tools in terms of their relevance to the immediate engagement. **Pulse is the primary overlap** because WebEx scraping is directly in BayOne's CI/CD scope. The Scribble (transcription) piece was not meaningfully discussed this week because Naga did not respond on it and did not provide access to the rebuild. Scribble will need its own conversation at some later point, but it is not the pressing item. The Srinivas meeting should focus on Pulse.

---

## 5. Distinction from the Nexus T WebEx Integration

During this same section of the meeting, Srikar surfaced a related but distinct overlap that needs to be kept mentally separate from the Pulse question:

- The Nexus T repository that Srinivas gave BayOne access to (Rui's codebase) contains its own WebEx component.
- That component performs outbound WebEx actions: pushing notifications, creating channels, creating rooms, creating meetings.
- These are WebEx **write** actions originating from the CI/CD side.
- This is distinct from Pulse, which is a WebEx **read/scrape** capability originating from Naga's side.

Both touch WebEx, but they are different directions of integration and different overlap patterns. Pulse is the overlap being negotiated in the Naga conversation. The Nexus T WebEx push integration is a different overlap pattern, addressed in the Nexus T / Rui research file.

---

## 6. Saurav's Scope-Drift Concern

After the Pulse and Scribble conversation was effectively resolved, Saurav raised a broader concern that changed the tenor of the section. Paraphrased:

> Naga's team has a pattern of standing up multiple repos and projects in parallel, and they keep layering on new ones. When BayOne first engaged, this CI/CD project was not even in the conversation. The knowledge graph work only surfaced inside the last two weeks. What Saurav wants to avoid is a future pattern where, at any given moment, someone new arrives with yet another tool and says "work on this one instead, and drop the others."

Critical points about this intervention:

- Saurav is flagging a **pattern**, not an isolated incident. The shifting-scope dynamic has happened more than once already, and he is projecting it forward.
- The concern is about the absence of a stable boundary. BayOne does not currently have a durable definition of what is in scope versus what is adjacent Cisco-internal work.
- This is a sustainability concern: if scope keeps moving, the engagement cannot be delivered against a fixed target, and the team cannot know when any specific piece of work is done.

This concern triggered Colin's explicit commercial response about scope, deliverables, change requests, and contract mechanics. That commercial response is documented in a separate research file and is not duplicated here. The important linkage to capture for this file: **Saurav's scope-drift concern is what prompted Colin to move from the Pulse/Scribble-specific discussion into the broader commercial framing of the engagement.**

---

## 7. The Broader Pattern

Stepping back from the specific Pulse and Scribble tangle, the section as a whole reveals a consistent pattern that BayOne needs to respond to:

- Naga's team keeps producing new tools and new repos with shifting names.
- Those tools have ambiguous relationships to BayOne's contracted scope.
- The tools' owners independently declare whether those tools overlap with BayOne's work.
- BayOne has access to none of the relevant repositories.
- There is no single authoritative scope document that establishes what is in and what is out.

The Pulse/Scribble conversation is the acute instance. The pattern is the underlying disease. The Srinivas meeting needs to settle both.

---

## 8. Implications for Slide 05 (Scope Alignment)

Slide 05 of the Srinivas deck is the scope alignment slide, and Colin committed to owning this section of the meeting himself. The Pulse/Scribble material in this document shapes that slide in the following specific ways:

1. **Frame the overlap, do not argue it.** Present Pulse as the primary WebEx overlap with BayOne's CI/CD scope, and do so factually. The argument against separation is implicit in the framing and does not need to be made aggressively on the slide itself.

2. **Use the "infrastructure-level components" language.** The slide should explicitly position Pulse and Scribble as reusable infrastructure components rather than standalone projects. This aligns Colin's pushback directly to Srinivas's own modularity directive, so it lands as agreement rather than pushback.

3. **Name the ambiguity explicitly.** The naming tangle (Pulse vs Scribble vs Scribbler vs Scrubber) should be acknowledged on the slide or in speaker notes. This is a low-cost way to signal that BayOne has done the diligence to untangle the vocabulary, and it implicitly demonstrates that the owning team has not communicated clearly.

4. **Flag the access gap.** The slide must call out that BayOne has no access to any of these repositories. This turns an internal friction point into a visible, unblockable item that Srinivas owns.

5. **Ask, do not tell.** The slide should pose the question to Srinivas: do these components get pulled into the CI/CD architecture as shared infrastructure, does BayOne work alongside Naga's team, or does BayOne build a parallel capability. Frame BayOne's recommendation, but let Srinivas make the call.

6. **Separate Pulse from Scribble visually.** Treat Pulse as the active discussion item. Flag Scribble as a parallel open question that cannot be closed this week because Naga has not provided access or responded. Do not try to resolve both in the same slide; that invites conflation.

7. **Separate Pulse from the Nexus T WebEx push.** These are different overlap patterns. On the scope alignment slide, it is worth making clear that WebEx overlap exists in two directions (inbound scraping via Pulse, outbound push via Nexus T's existing WebEx component) so that the architectural conversation downstream is precise.

8. **Do not present the commercial framing on this slide.** That thread (triggered by Saurav's concern) belongs in its own framing, handled verbally, not in the scope alignment slide itself. Slide 05 is about technical scope boundaries; the commercial escalation is a separate lever.
