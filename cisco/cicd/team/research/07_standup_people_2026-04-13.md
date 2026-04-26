# 07 - Standup: People and Dynamics

**Source:** /home/cmoore/programming/ai_opportunities/cisco/cicd/team/source/internal_team_meet_4-13-2026.txt
**Source Date:** 2026-04-13 (Monday team plan for the week)
**Document Set:** 07 (Internal BayOne team planning meeting following the April 10 Srinivas call)
**Pass:** People file, always first. Captures attendance, roles, engagement level, dynamics, and any new people introduced.

---

## Attendance

| Person | Title / Role | Engagement | Notes |
|--------|--------------|------------|-------|
| Colin Moore | Director of AI, BayOne (project lead) | Full | Ran the meeting. Kept the conversation moving across two parallel tracks (WebEx/transcription, build logs). Covered Srinivas debrief, tool access, architecture principles, and weekly deliverables. |
| Namita Ravikiran Mane | Agentic AI / Airflow Specialist, BayOne (on-site San Jose, build log track lead) | Full | Quiet but substantive. Confirmed ADS = Aurora Development Server (not Active Directory). Surfaced the CI versus CD distinction from the Friday call and said she would focus on the CD (nightly builds) gap. |
| Saurav Kumar Mishra | AI/ML Engineer, BayOne (offshore India, WebEx scraper and bot lead) | Full (most vocal offshore contributor) | Drove most of the technical depth in the call alongside Colin. Brought up Cisco IT flagging his Wall-E bot as non-compliant, the WebEx developer platform taxonomy (integrations, service apps, bots, agentic apps, OAuth), and cost-per-request scale math. Reused the Volley-bot Podman work as working proof. |
| Srikar Madarapu | AI Engineer, BayOne (on-site San Jose, WebEx scraper track lead) | Moderate | Clarified key facts when asked. Corrected Saurav on GitHub Desktop versus Docker Desktop install confusion. Confirmed Scribble is Naga-owned (not Justin-owned) and is a local script, not an integrated system. Shared A2G access state (granted but not visible, same as Saurav). |
| Vaishali Sonawane | BayOne (onboarding, log-side partner to Namita) | Silent observer | Single utterance in the meeting ("Thank you, everyone" at close). Colin opened the call confirming she was present and noted he had just finished a separate one-on-one with her. Still waiting on Cisco hardware, so she is scoped out of access requests this week. Paired with Namita on the log-side track. |

---

## Team Dynamics Observed

### Colin as project lead and senior engineer

Colin was clearly in the role of orchestrator and senior engineer. He ran the meeting, debriefed the Apr 10 Srinivas call, set the week's priorities, and walked through three substantial technical tutorials unprompted:

1. How to think about Podman versus Docker at Cisco, including the licensing backstory for why Cisco defaults to Podman.
2. What ADS machines actually are (Aurora Development Server, virtual machines likely running on something Proxmox-class, Linux so concurrent multi-user access is possible).
3. How to do proper A/B testing for the Scribble versus WebEx transcription comparison, framed as a three-tier decomposition: raw quality, glossary-augmented quality, then compute and scale cost.

Colin also set expectations about diplomatic framing when pushing back on Cisco-side work quality. He explicitly told the team not to call Naga's Scribble work junk in writing; instead, present current-state and proposed-state architecture diagrams and let technical stakeholders draw their own conclusions. He said literally, "you can't get your feathers ruffled if it's not really working for real yet."

### Saurav as the strongest offshore contributor

Saurav carried most of the technical back-and-forth. He brought in real observational data about the Cisco WebEx developer portal (the integrations, service apps, bots, agentic apps, OAuth taxonomy), flagged the compliance issue with his Wall-E bot being flagged by Cisco IT, and proposed a decoupled architecture (scraper, DB, MCP, then bot or app on top) before Colin arrived at the same framing. He also caught the economic logic about compute cost per transcript with characteristic bluntness: "if we can save like suppose 50 cents on each request, I suppose there will be millions coming in a month."

### Namita carrying the onboarding torch

Namita was the only person in the meeting who had actually gotten GitHub Enterprise access working. She followed the PDF she had shared with the team on Friday and said, "It's already there in the PDF document that I shared on Friday, so we have to follow the same steps. So that's all I did." Srikar and Saurav both said their A2G access shows "granted" but nothing is actually visible yet, and Namita explained the next step is to ping Justin to complete provisioning. Colin immediately assigned her the responsibility to teach the rest of the team the access procedure.

Namita also added the single most precise technical clarification of the meeting, correcting the common-misread ADS acronym:

> Aurora Development Server. So it's not the Active Directory server.

She drew out from the Apr 10 call the distinction between the CI track (Basel dev builds, which she has visibility into) and the CD track (nightly builds, which Justin has not shown her). She committed to closing the CD gap this week.

### Srikar as the on-site clarifier

Srikar was not the loudest voice in the meeting but contributed precise corrections at key moments. Two specific instances:

1. On the Scribble tool ownership: Colin was unsure whether Naga or Justin handled Scribble. Srikar confirmed, "This is with Naga Colin."
2. On the Scribble tool state: Late in the meeting, Srikar clarified that Scribble is not deployed or integrated with any system. It is a local Python script that runs Wispr on an audio file. This single statement shifted Colin's framing from "they have a working tool" to "they have a POC that is nowhere near production," which set up the diplomatic architecture-diagram approach Colin then coached the team on.

### Vaishali as quiet observer

Vaishali said nothing substantive during the meeting. Colin acknowledged her by name at the open and closed, and noted he had just had a one-on-one with her. She is still waiting on Cisco hardware, which means the Codex and Copilot access requests do not apply to her this week. Her work is scoped to pair with Namita on the build-log side once her hardware arrives. No sentiment signal either way can be drawn from a single-utterance meeting. Her engagement level will become readable in later sets.

### Team structure formalized

The meeting explicitly divided the BayOne team into two tracks:

- **WebEx scraping and transcription track:** Srikar (lead on-site) and Saurav (offshore counterpart). Colin will meet with them separately on architecture.
- **Build logs track:** Namita (lead on-site) and Vaishali (offshore partner). Colin will meet with them separately on architecture.

Colin confirmed he will handle the master Srinivas meetings but said each track should start generating its own presentations using the Singularity tool going forward, so that track-level visibility does not depend on Colin personally.

---

## New People Introduced

No new people were introduced in this meeting.

Two notes on people already on the org chart:

1. **Vaishali's first team-meeting appearance was 2026-04-13, not 2026-04-17.** The org chart currently references her onboarding as Apr 17 based on the Friday Sync. This meeting confirms she was already present and observing on Apr 13. The org chart should be updated to reflect this earlier first-team-contact date.
2. **Tanuja Raj was not in this meeting.** She first appeared in the Friday Sync (Apr 17). No update required to her entry.

---

## External parties referenced but not present

- **Srinivas Pitta** (Cisco Director of Engineering, AI lead): referenced throughout. The entire meeting was partly a debrief of his Apr 10 call, and several action items this week are framed around what to send him and when to escalate to him.
- **Justin Joseph** (Cisco build infrastructure owner): referenced as the next-step provisioning contact for A2G access and as the source for CD nightly build visibility. Also referenced as someone who is on the Cisco side of future scribble-versus-WebEx meeting-transcript comparison testing.
- **Nagabhushan ("Naga")** (Cisco, Pulse and Scribble owner): referenced as the actual owner of Scribble. Colin and Saurav agreed the team needs to connect with Naga directly to understand whether the WebEx-side work overlaps with what BayOne is being asked to build.
- **Imran** (Cisco stakeholder on the Apr 10 call): referenced as the person who raised the ADS-machine subdivision concern and then went quiet when Colin brought up auto-scaling, which Colin read as Imran not having thought in those terms before.
- **Anupma** (Cisco, CAT database / DevEx): referenced indirectly as "An Purma" in the Apr 10 call context. She raised the finite-ADS-compute point.

---

## Sentiment summary

No sentiment shifts from existing org-chart entries. Vaishali is a new data point with insufficient signal. Namita's credibility as a technically serious contributor is reinforced by her correct acronym call on ADS, her successful GitHub access, and her clear articulation of the CI versus CD gap. Saurav's reputation as the strongest offshore contributor is reinforced by the quality of his architectural thinking in this meeting.

---

## Files in this set (planned)

- `07_standup_people_2026-04-13.md` — this file
- `07_standup_action_items_2026-04-13.md` — parallel agent
- `07_standup_blockers_2026-04-13.md` — parallel agent
- `07_standup_decisions_2026-04-13.md` — parallel agent
- `07_standup_technical_discussion_2026-04-13.md` — parallel agent
- `07_standup_summary_2026-04-13.md` — last, main session
- Bridge: `06g-07_changes_2026-04-13.md` — retroactive gap-fill bridge
