# Namita Discrepancy Response — Draft 2026-04-20

**Context:** Namita has sent two messages today after the morning prep call and Colin's written response. She is now telling Colin that only her GitHub access was revoked and that she still has temp ADS access, and she is asking about the upcoming Srinivas presentation. She appears to not understand that she is effectively sidelined pending the CSIRT outcome. Additionally, the discrepancy between what she told Colin in the prep call (approximately 26 GB) and what Matt Healy has on the CSIRT record (80.7 GB) remains unresolved and is material.

**Goal of this message:**

1. Get the exact contents and size of what she attempted to share, reconciled between her account (26 GB) and Cisco's record (80.7 GB).
2. Reset her operating posture. She should not be continuing to write code, plan presentations, or engage with Cisco work while under investigation.
3. Do both with an unambiguous tone. Colin's earlier message was appropriately firm. This follow-up should be firmer because the evidence since then has gotten worse, not better.

**Tone:** Direct, factual, no cushion. Not cruel, but no reassurance either. She has had her cushion.

---

## Your Original Draft

> I need to understand one discrepancy that is not clear right now regarding the situation with IT.
>
> You told me you originally tried to share four Python files, and then there was the matter of the log files, which seemed very large. I am trying to understand what the actual file size is. You said you believed it was 26 GB, but Cisco flagged it as 80 GB.
>
> I want to understand what the discrepancy is. In any case, even if it is the lower number, I want to know exactly what was in the folder (the zip folder you tried to share) because 20+ GB does not make much sense for log files in a zip file; that is absolutely massive. What exactly was in those files?

This is the right content but it is softer than it needs to be and it leaves two concrete things unasked: (1) specifically what she selected as the contents of the zip, and (2) what she intends to do with her remaining access while the investigation is open.

---

## Refined Version (Recommended)

> Namita, I need two things from you before we go any further.
>
> First, there is a material discrepancy between what you told me in our call this morning and what Cisco has on their investigation record. You said the zip was approximately 26 GB. Cisco logged the upload activity at 80 GB. Both numbers are implausibly large for five days of log files, so I need a precise accounting. Tell me exactly what directory you selected for the zip, how many individual log files it contained, and what their average size was. If you cannot reconstruct this from memory, look at your shell history, your local file system, or whatever you still have access to. I need the answer in writing today. I cannot represent you to Cisco or to BayOne leadership if my numbers do not match theirs, and right now they do not.
>
> Second, you mentioned that your GitHub access was revoked but that you still have temp ADS access, and you asked about the Srinivas presentation today. Stop. You are not presenting to Srinivas today. You are not continuing any Cisco work until the CSIRT investigation is closed and BayOne has completed its internal review. That is not a punishment — it is the only posture that is defensible to Cisco. Any continued activity on your side while this is open, even activity you believe is innocuous, gets logged as more data for them to review and further widens our exposure.
>
> Practically, that means: do not open any Cisco-related files, do not run code against Cisco infrastructure, do not respond to anything from Cisco IT or anyone else at Cisco without me. If anyone at Cisco messages you about the incident, forward it to me on BayOne Teams and wait for my direction before replying. If anyone at Cisco messages you about regular project work, forward it to me too. I will decide how to handle each case.
>
> I understand this is uncomfortable. The discomfort is appropriate given what happened. Focus on giving me the file-contents answer above today; everything else waits.

## Why This Version

- **Opens with "I need two things"** — frames the message as a directive, not a discussion. No apology prefix.
- **The discrepancy ask is sharpened.** Original said "what exactly was in those files" — too open-ended. Refined version asks for directory selection, count, average size, and tells her where to look (shell history, file system). Makes evasion harder.
- **"I cannot represent you" is the load-bearing sentence.** Explains why the discrepancy matters without making the request feel arbitrary. She should feel that her position depends on cooperating with the accounting request.
- **The second paragraph is the hardest new content.** Addresses her "only GitHub is revoked, I can keep going" assumption directly and shuts it down. Names the Srinivas presentation question and kills it immediately.
- **"Not a punishment — it is the only posture defensible to Cisco"** — reframes the stop-working directive as protective, not punitive. Removes the grievance angle she might otherwise take.
- **The practical instructions are concrete.** Do not open files, do not run code, do not respond to Cisco. Forward everything to Colin. No ambiguity.
- **The close acknowledges discomfort without softening.** "The discomfort is appropriate." Does not apologize for the discomfort. Redirects her to the only productive action: get him the file answer.

## What The Refined Version Deliberately Does Not Do

- Does not use the word "mistake." Mistake language is the framing Yogesh used and that Colin rejected in the Neha/Zahra call. This is more serious than a mistake.
- Does not mention the 80.7 GB as a specific threat. Cisco has it; she knows it exists; Colin does not need to wave it at her.
- Does not preview the probation, written warning, or termination-conditional policy. Those are authorizations Colin does not yet have from Yogesh; discussing them with Namita before they are authorized would be premature and would give her a ground to resist.
- Does not answer her Srinivas-presentation question with a process ("I will present instead" or "we will reschedule"). Just shuts down her participation. The process can be decided after.
- Does not thank her for anything. There is nothing to thank her for in this exchange.
- Does not use the phrase "moving forward" or anything similar. She does not get a promise of forward motion right now.

## Tone Calibration Notes

The message sits one notch harder than the earlier morning response, which is appropriate. The earlier response covered the incident facts and issued a final warning. This response is a tactical follow-up issued after:

- The Matt Healy transcript revealed the picture is worse than Namita disclosed
- The 80.7 GB number landed on the Cisco record
- Namita has been messaging Colin today as if only her GitHub access matters
- Yogesh failed to back a stronger response, making Colin's engagement-level discipline the only available lever

If she reacts with additional apology or defensive explanation, do not engage. Reply with one line: "I need the file-contents answer today. We can discuss the rest when I have that."

## Sending Channel

BayOne Teams, same thread as her incoming messages. Not WebEx. Not email. Not Cisco Teams — that channel should not be used for anything related to the incident.

## After Sending

- If she answers the file-contents question completely within a few hours, document it as a short note in a `06g_incident_file_contents_reconciliation_2026-04-20.md` research entry.
- If she does not answer or provides an evasive answer, that is itself signal and Colin's personnel recommendation hardens further.
- Regardless of her answer, update `/cisco/cicd/team/tracking/` if and when Colin decides to track these at the team level — currently, per the earlier correction in this session, all incident items stay within the 06 set and do not pollute the team operational trackers.

## If You Want It Shorter

The minimum viable version, stripped to the essentials:

> Namita, two things.
>
> One. The size of the zip you tried to share. You said 26 GB. Cisco has it at 80 GB. Tell me exactly what directory you selected, how many files it contained, and their average size. In writing, today.
>
> Two. You are not presenting to Srinivas today and you are not continuing any Cisco work until the CSIRT investigation is closed. If anyone at Cisco messages you about anything, forward it to me on BayOne Teams and wait for my direction. No exceptions.
>
> Focus on the file-contents answer today. Everything else waits.

This short version has the same content but less cushion. Use it if you want the directive to land harder and you are comfortable with a colder tone.
