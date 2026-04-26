# 06b - Incident: Matt Healy / CSIRT Exchange Full Record

**Source:** /cisco/cicd/team/source/week_2026-04-20/day_2026-04-20/namita_matt_healy_it_security_transcript.txt
**Source Date:** 2026-04-20 (obtained by Colin during 7:30 PST prep call, is the full verbatim Namita–Matt chat)
**Document Set:** 06 (IT security incident — supplementary 06b, escalation detail)
**Pass:** Full exchange decomposition

---

## Summary

What was recorded in Set 06 as an IT Security flag is in fact a formal CSIRT investigation. Matt Healy identified himself as a Cisco Computer Security Incident Response Team Investigator and has escalated the matter to Cisco's GPS and Data Protection teams. The data scope on the investigation record is not four Python files — it is **26.77 GB in one zip and 80.7 GB overall**, because Cisco's monitoring captured the broader upload activity Namita attempted (the zipped log directory), not just the individually-shared source files. Namita's Cisco access has been suspended pending investigation. Matt explicitly refused Namita's offer to set up a joint meeting with Colin and Srinivas, stating Cisco's internal process takes precedence.

This is the most important artifact in Set 06. The Cisco-side posture revealed here is materially different from the one Set 06 was written under.

## Matt Healy — Revised Understanding

- **Actual title:** CSIRT Investigator (Computer Security Incident Response Team). Not generic IT Security.
- **Position in process:** Conducting the investigation. Not the decision-maker; GPS and Data Protection teams are the adjudicators.
- **Working style from transcript:**
  - Leads with the policy citation, then asks for specifics
  - Requires everything in writing ("he asked me to tell that in written")
  - Will suspend access mid-conversation to enforce cooperation ("if you do not cooperate I will be suspending your access")
  - Does not accept third-party intermediation — refused Namita's meeting-with-Colin-and-Srinivas suggestion outright
  - Treats minimization attempts as aggravating (pushed back hard when Namita said "just a couple of source code files")
  - Chains questions forward — got from "who" to "what" to "where airdropped" to "what else was on BayOne GitHub" in one continuous exchange
- **Quote on record:** "You've stated on the record as part of official CSIRT Investigation that the file 041526.zip (26.77Gb) only contains 4 python files. I am suspending your access to Cisco for the remainder of this investigation to protect Cisco's intellectual capital."

## The Cisco Scale On Record

- **041526.zip = 26.77 GB** (the log-directory zip Namita attempted to share to Vaishali via Teams; blocked from actually sending, but Matt has it on record that it existed and was attempted)
- **Total upload activity flagged: 80.7 GB** (this is Matt's figure, covering all activity their monitoring picked up, which likely includes AirDrop activity and additional files beyond the zip)
- **The four Python files named on record:** `analyze_and_fix_build.py`, `automated_bazel_workflow.py`, `automated_workflow.py`, `bzl_error_report.py` — all from `/DCN/tools`
- **Log_type_mapping.pdf** confirmed uploaded to BayOne-Solutions GitHub — Matt asked, Namita confirmed, "my manager knows about it" (i.e., Namita told Matt that Colin knew about the GitHub upload, which was not accurate at the time)

The operative fact: any Cisco-side narrative of this incident will use 80.7 GB as the headline number, not "four Python files." Colin must know this before any Cisco conversation.

## Violations Named By Matt (In Matt's Own Framing)

1. **Source code exfiltration via Teams** — "serious violation of Cisco's security policies that you have previously committed to following"
2. **Use of MS Teams for business in the first place** — "Even using MS teams for business as a violation of Cisco's data protection policies" (this is a separate, additional violation category)
3. **Sharing with a non-Cisco-ID individual** — "Doesn't matter if she's being on boarded. if she does not have a Cisco ID it is not okay for her to have any sister data"
4. **Upload of Cisco material outside Cisco network** — "Uploading source code outside of Ciscos network is probably the most egregious violation of Cisco's data protection policies"
5. **GitHub upload of Log_type_mapping.pdf** — captured as a separate data-protection concern
6. **The 26.77 GB / 80.7 GB total data flagged** — irrespective of what Namita intended to share

## Enforcement Actions Already Taken

- **Namita's Cisco access suspended** for the remainder of the investigation. Quote: "I am suspending your access to Cisco for the remainder of this investigation to protect Cisco's intellectual capital."
- **Do not delete anything** — Matt instructed Namita to preserve all artifacts for audit. This is not optional. Colin reinforced this in the prep call.
- **Escalation to GPS and Data Protection teams** — these teams, not Matt, will make the disposition decisions.
- **Internal Cisco process takes precedence** — Matt refused the joint-meeting-with-Colin-and-Srinivas suggestion, stating "Internal Cisco discussions of this incident will be conducted first. This is a serious matter, please stop ignoring my requests."

## What Namita Told Matt — Verbatim Record

This is the single most important input for Colin's posture in any Cisco meeting. Cisco's position will be built on what Namita said. Any divergence from this record creates additional credibility risk.

Key statements Namita made to Matt:

- "I was sending it to my colleague who is also part of Cisco project and we are working together. I got access to temp ADS machine. I will be careful from next time and won't do it again!"
- Named Vaishali Sonawane as the recipient
- Described her as "part of the new team, onboarding in process"
- Identified the four Python files by name
- When Matt pushed on the 26.77 GB zip: "Those are logs files for analysis for project. It's a new project. Only I had got access to it. And was responsible to share it with the team."
- Explained the AirDrop: "That was sample Bayone document we had prepared to share with the team. Was trying to transfer it to my bayone laptop."
- Named Colin and Srinivas by email when Matt asked which team
- On WebEx scraping: "Yes, that's our project. My teammate scrapped it. Srinivas knows about it."
- On GitHub upload: "Yes. As we are using it. My manager knows about it."
- Explicitly requested Matt not suspend her account, citing three-week access ramp; Matt declined

## What Cisco Now Believes (That Was Not In Set 06)

1. BayOne is working with a person (Vaishali) who does not have a Cisco ID and who has Cisco data in her possession. Matt treats this as the same class of violation regardless of NDA status.
2. There is a 26.77 GB zip of Cisco log data that was attempted to be moved to a BayOne account. Even though the move was blocked, Cisco's record shows the attempt and the volume.
3. BayOne is conducting WebEx scraping. Namita told Matt "Srinivas knows about it" — which is true per the engagement scope, but now this activity is formally known to Cisco IT Security, not just to the Srinivas/Anand layer.
4. BayOne has Cisco material on its GitHub (`Log_type_mapping.pdf`). Confirmed by Namita on the record.
5. BayOne's engagement lead ("my manager") allegedly knew about the GitHub upload before the incident was flagged. This is what Namita told Matt. Colin did not in fact know about it before the disclosure exchange; this creates a factual gap between what Cisco believes and what is true.

## Implications Colin Must Address

- **The 80.7 GB headline will land first.** Any conversation with Srinivas or Anand will start from a Cisco-side briefing that says "BayOne contractor moved 80.7 GB of Cisco data." Colin's opening must account for that number, not for "four Python files."
- **The Vaishali-without-Cisco-ID frame is a new argument surface.** Matt has placed this on the record as an independent violation. Even if the four files are scope-aligned, the recipient's lack of a Cisco ID is treated as a separate issue that the NDA does not resolve.
- **Matt has closed the back-channel path.** Colin cannot request a joint meeting with Matt to clarify. The investigation runs on Cisco's internal rails until GPS and Data Protection decide disposition.
- **"My manager knows about it" is a fact gap.** Namita told Matt that Colin knew about the GitHub upload. He did not. If this is surfaced by Cisco, Colin will need to correct the record without appearing to throw Namita under the bus — a narrow corridor.
- **WebEx scraping is now on the Cisco IT Security record.** This does not change its scope legitimacy, but it means any future conversation about it cannot be contained to the Srinivas layer.
