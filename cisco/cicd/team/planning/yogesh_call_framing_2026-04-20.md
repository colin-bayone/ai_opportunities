# Yogesh Call Framing — 2026-04-20

**Caller:** Colin Moore (Director of AI, BayOne)
**Recipient:** Yogesh (CEO of BayOne, Colin's direct superior)
**Purpose:** Brief Yogesh on the Cisco CSIRT incident involving Namita, present BayOne's response posture, request authorization on personnel action and policy rollout, and align on commercial-relationship handling. This conversation happens before Zahra is looped in, so Yogesh hears it from Colin first.

**Channel:** Phone call (voice). Not email, not WebEx. This is a CEO conversation and requires tone, inflection, and real-time alignment.

**Timing:** Today, before end of business day.

---

## What Yogesh Needs From This Call

1. **An accurate picture of the incident** with the right weight — serious, but not catastrophic, and with executive-layer support already secured.
2. **Confidence that Colin has it in hand.** Yogesh should not have to rescue the situation; he should see that his engagement lead is driving.
3. **Alignment on personnel action.** Yogesh is CEO; personnel consequences above the engagement-lead level run through him and HR.
4. **Alignment on commercial-relationship posture.** If Cisco ends up terminating or narrowing the engagement, BayOne needs a unified response.
5. **A clean loop-in path for HR.** Rahul Bobbili already recommended looping Yogesh and HR together on the personnel action; this call is the start of that path.

---

## Opening (60 seconds)

> "Yogesh, I need to brief you on a serious incident with the Cisco engagement that happened Friday and came to our attention this morning. It is in hand — I have already done damage control with Anand Singh, the Cisco executive sponsor, and he is supportive — but it is serious enough that I need your authorization on a personnel action and on a policy rollout, and I want you to hear it from me before it reaches Zahra or anyone else."

This opening does four things:
- Establishes severity without panic
- Signals Colin is leading, not hiding
- Flags the two decisions he is seeking authorization on
- Protects Yogesh from being surprised by another BayOne source

---

## The Facts — In This Order

Do not lead with the 80.7 GB number. Lead with the act, then the scale, then the aggravation.

### 1. The core act

One of the BayOne team members on the Cisco engagement, Namita, shared four Python source files with another teammate, Vaishali, through BayOne-to-BayOne Microsoft Teams accounts on Namita's Cisco-issued laptop. That is a dual-policy violation — it violates both Cisco's access policies and BayOne's own client-data-handling standard.

### 2. The scale on the Cisco investigation record

Cisco's monitoring picked up 80.7 GB of upload activity, including a 26.77 GB zip of log files Namita also attempted to move but which was blocked. Cisco has the 80.7 GB figure on their investigation record regardless of what actually transferred.

### 3. The aggravating factors

This was not a one-off slip:

- Namita tried Teams, got blocked on the zip, then **AirDropped** a presentation document from her Cisco laptop to her BayOne laptop as a workaround
- She also uploaded a separate analysis PDF to **BayOne GitHub** on a different occasion
- She told Srikar (another teammate) to download Teams on his Cisco laptop — actively propagating the violation pattern
- She did all of this after Colin had given explicit, repeated, written-and-verbal guidance against exactly these actions
- Rahul Bobbili had also given her the same guidance earlier in the week
- When Cisco IT Security flagged her, she went directly to them and over-shared detail before notifying Colin, compounding the exposure

### 4. What Cisco is doing about it

- A CSIRT (Computer Security Incident Response Team) investigation is open
- Namita's Cisco access has been suspended
- The matter has been escalated to Cisco's GPS and Data Protection teams for disposition
- A formal finding will come back within one or two days based on the language the CSIRT investigator used

### 5. What Colin has already done

- Had Namita remove the BayOne GitHub upload this morning
- Instructed Vaishali to delete the four source files and confirm deletion
- Issued Namita a final written warning
- Conducted a damage-control call with Anand Singh (Cisco executive sponsor), who volunteered to be the Cisco-side POC for the GPS review and framed the incident as recoverable
- Drafted a BayOne-wide signed client data handling policy ready for rollout to the full Cisco team
- Aligned with Rahul Bobbili on procedural next steps

---

## The Verbal Explanation — What To Actually Say

This is the coherent paragraph-style explanation you can deliver directly, in order, during the call. It covers every material fact in a logical sequence, sounds like spoken English rather than a read-off briefing, and is designed to be delivered in roughly three to four minutes with natural pauses for Yogesh to interject. Use it as the core of the conversation after the 60-second opening. Adjust to your own cadence — it does not need to be delivered word-for-word.

---

> The short version is that one of the engineers on our Cisco engagement, Namita, committed a series of data-handling violations on Friday that have triggered a formal CSIRT investigation on the Cisco side. CSIRT is their Computer Security Incident Response Team. The investigation has been escalated to their GPS and Data Protection teams, and findings are expected in one to two days.
>
> What she actually did is layered, and I need to walk you through it so you have the full picture. Namita is on-site at Cisco as part of our team, with both a Cisco-issued laptop and her BayOne laptop, which is standard for all our contractors on this engagement. She was working with Vaishali, a new BayOne hire who had just signed her Cisco NDA and was in the middle of onboarding. Namita wanted to share some work-in-progress material with Vaishali to help her ramp up. She had four Python source files from a Cisco engineer named Justin that are directly related to our scope of work — they are part of the build log analysis track, no API keys, nothing proprietary in a dangerous sense, but they are Cisco source code. Instead of using WebEx, which is the approved channel for any Cisco-related sharing, she used Microsoft Teams. And not Cisco's Teams tenant — her BayOne Teams account talking to Vaishali's BayOne Teams account, with both accounts open on Namita's Cisco-issued laptop. That means those files crossed off Cisco hardware and into BayOne's cloud tenant. That is a dual-policy violation — it violates both Cisco's access policies and BayOne's own client-data-handling standards.
>
> That is just the first piece. She also tried to send a zip file of log data from the same Cisco systems over Teams — that zip was 26.77 GB. The Teams upload was blocked by Cisco's controls, but Cisco captured the attempt on their investigation record. Their total figure, counting everything their monitoring picked up across Teams, AirDrop, and other activity, is 80.7 GB. That is the headline number Cisco will use in any internal conversation about this, regardless of what actually transferred successfully.
>
> When Teams blocked the zip, she did not stop. She then AirDropped a presentation document from her Cisco laptop to her BayOne laptop as a workaround. Separately, on a different occasion, she had uploaded an analysis PDF she had been working on to BayOne GitHub. Cisco IT captured both of those activities as well.
>
> The most important aggravating factor is that none of this was a first-time guidance issue. From day one of the engagement I told the entire team, verbally on at least five occasions and in writing on the team chat, that content can go from BayOne to Cisco but never the other direction, and that nobody downloads anything without my direct approval. Rahul Bobbili gave her the same guidance earlier in the week specifically about Teams — he told her the purpose of having WebEx is defeated if we are using Teams, and that we should not be using it. She not only ignored that guidance herself — she told Srikar, another one of our engineers, to download Teams on his Cisco laptop too. His install attempt was blocked, so he is not personally flagged, but she was actively propagating the violation pattern to teammates.
>
> The way Cisco found out is that their CSIRT monitoring flagged the volume of upload activity coming off Namita's account. Their investigator, Matt Healy, contacted her directly on Friday. And this is where she made the situation materially worse. She did not loop me in. She just sent me a short message saying she had been flagged and she was handling it. Then she proceeded to have a long written exchange with Matt where she gave him far more detail than he had asked for — she named the files, confirmed the GitHub upload, confirmed the AirDrop, and effectively built his case for him. She did all of this without any framing or coaching from me, because I did not know the exchange was happening in real time. I only got the full picture this morning when she sent me the transcript.
>
> She is suspended from Cisco access pending the investigation outcome. Her account on BayOne GitHub is suspended. Her work on the engagement is paused. Srikar and Saurav can pick up the near-term deliverables.
>
> Here is the good news. Before I called you, I got on a call with Anand Singh, the Cisco executive sponsor for the engagement — the person who granted us the contract extension two weeks ago. He joined unexpectedly, which was a gift. I walked him through the core facts. I did not surface the 80.7 GB figure or the tenant-account specifics or the GitHub upload in that call — I kept the perimeter narrow but honest. What I shared was the four Python files, the Teams channel error, the fact that BayOne is taking this seriously at a policy level, and the fact that Vaishali is fully onboarded with an NDA. Anand's response was far better than I expected. He volunteered to be the Cisco-side point of contact for the GPS review. He accepted the Namita access suspension. He explicitly said this happens sometimes even with Cisco's own full-time employees, and that he would support BayOne through the review. His framing was that we should let their process play out and that he wants us to continue making progress on the engagement while it does. That is as supportive as it gets from the executive layer at Cisco.
>
> The one residual risk from the Anand call is that GPS may eventually brief him with the fuller picture, including the 80.7 GB figure and the GitHub upload. If that happens, my disclosure perimeter today will look thinner than it did in the moment. I have drafted a short follow-up WebEx message to him that would surface the GitHub upload proactively, framed as context for his POC role. I am not going to send it without aligning with you first.
>
> On the BayOne side, what I need to do now is formalize the response. First, I am recommending we issue Namita a final written warning combined with a three-month probation period, with traffic monitoring on her systems and a signed policy acknowledgment in her file. If she commits any further violation during probation, that is immediate termination. Second, I have drafted a BayOne-wide signed client data handling policy that applies to every engagement we run, not just Cisco. I want to roll that out this week, have every current team member on the Cisco engagement sign it, and make it a prerequisite for any future Cisco-related access. Third, if Cisco comes back and says they want Namita off the engagement, my position is we comply without resistance and offer Santhosh as her replacement. If Cisco goes further than that and wants the engagement paused or terminated entirely, we accept that decision. We do not push back on the CSIRT findings, we do not try to work around Anand, and we do not contest anything Cisco decides. That is the only posture that preserves our relationship for future engagements with them.
>
> Separately, Namita is on an H1B visa. If we end up terminating her, that path requires procedural care. I am going to loop Sonya in from HR after this call, formalize an incident report on Keka, and make sure everything runs through the right process. Rahul Bobbili already told me that is the path, and he is aligned.
>
> What I need from you is five things. First, your authorization on the personnel path — the final warning, probation, monitoring, and the escalation-to-termination condition. Second, your authorization to pull Sonya from HR in on this. Third, your authorization to roll out the signed policy across the full Cisco engagement team this week. Fourth, alignment on the Zahra loop-in — I plan to call her right after we hang up, unless you want to do that yourself. And fifth, alignment that we will accept whatever Cisco decides without contesting it, even if it costs us the engagement. I have it under control, but I need your cover on those five to move.

---

## Delivery Notes For The Script Above

- **Pace:** aim for three to four minutes, with natural pauses. If Yogesh interrupts, answer and return to the thread.
- **Tone:** factual-serious, not apologetic-serious. You did not do this, Namita did. You are briefing him, not confessing.
- **Physical delivery:** if possible, stand up for the call. It makes the voice more assertive and you will sound more in-control.
- **What to watch for:** if Yogesh goes quiet for a long stretch, keep going. If he interrupts with "how did this happen," go to the "none of this was a first-time guidance issue" paragraph and emphasize the defiance angle. If he asks about contract risk, go to the Anand paragraph and emphasize the supportive posture.
- **If he seems to underweight the incident:** add the line "Yogesh, the 80.7 GB figure is going to be on the Cisco investigation record. Even if nothing actually transferred, that number is what they will quote internally." That usually recalibrates.
- **If he seems to overweight it:** add the line "Anand volunteered to be the Cisco-side POC. That is an unusual amount of executive support on day one of an incident. I am not panicked about contract continuity at this point — I am focused on doing the right things procedurally so we are protected regardless of outcome."

---

## What Colin Is Recommending

### Personnel action on Namita

Preferred outcome (Colin's recommendation):

- **Final written warning** acknowledging the specific violations and naming termination as the consequence for any recurrence
- **Three-month probation** with traffic monitoring on her Cisco-issued systems and any BayOne systems she touches
- **Any further violation during probation triggers immediate dismissal**
- **Signed BayOne-wide client data handling policy** rolled out to her and the entire Cisco engagement team before any further Cisco access resumes
- Keep her on the project if Cisco permits; remove her from the project and potentially the company if Cisco requires it

Alternative outcomes if Cisco demands more:

- If Cisco demands her removal from the engagement but not termination, BayOne removes her and offers a replacement (Santhosh or other available consultant)
- If Cisco or the GPS findings point to something more severe (intentional exfiltration, etc.), BayOne proceeds to termination. H1B status requires procedural care; HR must drive that path.

Colin's own view: even a warning feels light. He would rather terminate than lose the Cisco contract over one person's carelessness. But the formal path needs Yogesh and HR co-signing, not a unilateral call from Colin.

### Policy rollout

- The drafted policy at `/bayone/processes/2026-04-20_client_data_handling_policy/client_data_handling_policy_2026-04-20.md` is a BayOne-wide signed document (not acknowledgment), with termination as the ceiling consequence
- Colin recommends running it by HR (Sonya) before distribution
- Every person on the Cisco engagement signs within 48 hours; no further Cisco access granted to new onboards without a signed copy on file
- This is defensible evidence of corrective action if Cisco asks what BayOne is doing structurally

### Commercial posture

- Zahra Syed needs to be looped in today after this call. Recommend Yogesh or Colin make that call, whichever Yogesh prefers.
- If Cisco terminates or narrows the engagement based on GPS findings, BayOne accepts without contesting
- If Cisco preserves the engagement but requires personnel changes, BayOne complies without resistance
- Under no circumstances does BayOne attempt to pressure Anand or Srinivas to influence the CSIRT findings

---

## What Colin Is Asking Yogesh To Authorize

1. **The personnel-action path** (final warning + probation + conditional continuation, with escalation to dismissal on any further violation or if Cisco requires it)
2. **HR engagement** — specifically, looping in Sonya (or whoever Yogesh designates) to drive the formal incident report on Keka and the H1B-aware path if dismissal becomes needed
3. **The BayOne-wide policy rollout** — authorization to distribute the signed policy to the full Cisco engagement team this week
4. **The Zahra loop-in sequencing** — who calls her, when
5. **Full acceptance posture with Cisco** — agreement that BayOne will not contest whatever GPS and Data Protection decide, even if it costs the engagement

---

## Questions Yogesh Will Likely Ask

Prepare clean answers for these before the call:

### "What is the contract risk?"

Answer: Low at the Srinivas/Anand layer — they are supportive. Real and independent at the GPS/Data Protection layer — their decision runs on Cisco's internal rails. Colin's best-case read: Cisco lets the engagement continue with Namita removed. Worst-case read: Cisco terminates. Expecting findings in one to two days.

### "Why did you not catch this earlier?"

Answer honestly: Colin had given the guidance verbally and in writing on multiple occasions. Namita actively defied it and did so in ways that were not visible to Colin until Cisco IT flagged it. BayOne does not currently have in-place monitoring on contractor laptops that would have detected large data movements. The policy rollout addresses the go-forward prevention; the lack of detection is a systems gap that BayOne may want to address separately.

### "What about the other team members?"

Answer: Every team member has both a BayOne laptop and a Cisco-issued laptop; the distinction is about behavior, not hardware access. Srikar is in the US, in person with Namita, and was directly exposed to her misguidance to install Teams on his Cisco laptop. Per current evidence he did not actually complete it, because the install was blocked, but he was close enough that under a different set of circumstances he could have been the one flagged. Saurav is in India, operates independently, and simply did not follow Namita's reasoning — so he is unexposed not because of hardware but because of judgment. Vaishali is in India, but has been in daily contact with Namita throughout her onboarding, so it is reasonable to assume she received the same misguidance Srikar did — she just happened to be the recipient of the Teams share rather than an originator of her own. She has signed the Cisco NDA, which limits her personal exposure. Askari is minimally engaged on the project and has no meaningful exposure. The signed policy rollout covers everyone; any new violations trigger the same consequences regardless of location or hardware.

### "Do we need lawyers?"

Answer: Recommend yes at the BayOne commercial-relationship layer. If Cisco moves toward contract termination or seeks damages, BayOne's contracts counsel should be engaged preemptively. If Namita is terminated, HR legal (H1B-aware) must be engaged on that path. These are two separate legal conversations and should run in parallel.

### "Is this going to cost us this client permanently?"

Answer: Probably not, based on Anand's posture today. Anand explicitly framed the incident as recoverable and cited precedent with Cisco's own employees. But the GPS findings could change the picture, and Colin will not know for one to two days. If findings are adverse enough, contract continuity is genuinely at risk, in which case BayOne's strategy shifts to preserving the relationship for future engagements.

### "What do you need from me?"

Answer: The five authorizations above. And availability to pick up the phone on short notice if GPS findings come in this week and BayOne needs to respond fast.

---

## What Colin Is Not Asking Yogesh To Do

- Intervene with Anand or Srinivas. The engagement-lead relationship is Colin's to run, and interference from the CEO layer would weaken rather than strengthen it.
- Make the personnel call unilaterally. Yogesh authorizes the path; HR drives the procedural execution.
- Speak to Cisco directly unless and until the situation escalates to a CEO-to-SVP conversation. That is not where we are today.

---

## Close (30 seconds)

> "That is the situation. I will put a written incident report on Keka and email today, I will loop in Sonya from HR and Zahra from commercial right after this call, and I will update you when the CSIRT findings come in. I expect that to be in one or two days. I know it is a lot, and I am sorry this happened on my engagement. I have it under control."

The close acknowledges the weight, takes ownership, commits to specific next steps with timing, and ends on confidence. Do not end on apology. Apology in the middle is fine; end on "I have it under control."

---

## What To Avoid In The Call

- **Do not volunteer the factual gap** about Namita telling Matt Healy that "my manager knows about" the GitHub upload. This is a narrow management corridor that does not need to be on Yogesh's radar unless the gap surfaces through Cisco.
- **Do not blame Rahul or any other BayOne person.** This was Namita's act. Rahul's prior guidance actually helps BayOne's defense.
- **Do not promise specific Cisco-side outcomes.** CSIRT is independent; Colin does not control it.
- **Do not use terms like "compliance" or "investigation" without specifying what kind.** "Cisco CSIRT investigation" is what this is. Saying "we are being investigated" is wrong and alarming.
- **Do not minimize.** Yogesh will notice. Name the 80.7 GB figure, name the multiple violations, name the aggravating pattern. He needs to feel the weight.

---

## After The Call

1. Send Yogesh a one-paragraph written summary on email within 30 minutes of the call. Subject line: "Cisco CSIRT Incident — Briefing Summary for Your Records."
2. Call Sonya (HR) next, brief her on the same facts, start the formal incident report process on Keka.
3. Call Zahra next, brief her on the same facts, align commercial posture.
4. Update `/cisco/cicd/team/research/` with a short entry capturing what Yogesh authorized and any follow-ups he requested.
