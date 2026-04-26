# Incident Prep and Meeting Plan — 2026-04-20

**Purpose:** Questions Colin needs answered in the 7:30 PST prep call with Namita, plus how each answer should shape the 15-minute Srinivas + Anand meeting. Also covers the one-on-one tone with Namita and the internal team all-hands that follows.

**Known constraints:**

- Only 30 minutes with Namita before the Srinivas/Anand meeting
- The 15-minute duration of the Cisco meeting is mildly positive (they want to address and move on)
- Vaishali signed the Cisco NDA, which is the strongest legal mitigating factor
- Colin had previously and repeatedly issued verbal guidance against exactly this. The rules are also in both BayOne and Cisco access policies.
- The text exchange already delivered the final warning to Namita, so today is not about re-scolding her

---

## Uncertainty To Resolve Before Walking In

A key ambiguity from the text exchange: Namita wrote "via Cisco laptop" but Colin's read is that it may have been from the BayOne laptop, or that the Teams account used was BayOne-tenant. The hardware and the account are two separate questions, and both matter. Do not assume Namita's self-report is fully accurate on this point; she was rattled when writing it.

---

## Questions for Namita (30-minute prep)

Ordered by their impact on the Srinivas/Anand meeting. Get the first five answered no matter what; the rest if time allows. The single most important item is question 2 (verbatim Cisco communication) — if any tension exists between Namita's account to Cisco and the facts, the meeting strategy has to account for that before anything else.

### 1. Which device and which Teams account were used for the share?

- Was the Teams app on her Cisco-issued laptop, her BayOne laptop, or browser-based?
- Was the Teams account she was signed into the Cisco tenant or the BayOne tenant?
- Which tenant was Vaishali signed into? (If Vaishali has not been provisioned on the Cisco tenant yet, the share was necessarily cross-tenant, which is materially worse.)

**Why this matters for the Cisco meeting:** Intra-Cisco-tenant sharing is a policy violation but the files never left Cisco's environment. Cross-tenant sharing means Cisco source code is now in BayOne cloud storage, which is a different magnitude of incident and changes what corrective action Cisco will demand.

### 2. What exactly has Namita told Matt Healy and anyone else at Cisco, verbatim?

- Every message, email, and verbal statement Namita has made to Matt Healy since the flag. Ask for the actual words, screenshots of chat, or her best recall.
- Anything she has said to Justin, Divakar, Srinivas, or anyone else on the Cisco side about the incident.
- Anything she has committed to on Cisco's behalf (corrective actions, timelines, deletions).

**Why this matters:** Colin cannot walk into the Srinivas meeting having a different story than what Namita has already told Cisco IT. If Namita has understated, overstated, or speculated about anything, Colin needs to know before he opens his mouth. This is the single highest-priority alignment item before the meeting, alongside the GitHub PDF removal. Cisco will have a record of what Namita said; BayOne needs the same record.

### 3. Were there any secondary sensitivities in the four files?

The files are Justin's Python source for the WebEx scraper scope BayOne is already contracted to work on. So the payload is scope-aligned, not off-limits domain. That narrows the question to:

- Any credentials, API keys, tokens, connection strings, session cookies, or secrets embedded in those files?
- Any internal hostnames, internal URLs, private network paths, or SSH keys?
- Any comments or docstrings referencing things outside the scraper scope?

**Why this matters:** If any of those are present, it escalates the incident from "policy violation on scoped material" to "credential exposure" and obligates Colin to proactively request credential rotation in the Srinivas meeting. If none are present, the framing stays clean: wrong channel and wrong device, right scope.

### 4. Where are the four files now?

- On Vaishali's machine — which one, BayOne or Cisco-issued?
- In any Teams chat history, OneDrive, SharePoint, or other BayOne cloud location?
- Has Vaishali been instructed to delete them, and has she confirmed deletion?

**Why this matters:** "Deleted, confirmed" is the single most powerful sentence Colin can say in the Srinivas meeting. If the answer is still "we need to purge these after the meeting," that is a weaker position. Get deletion done before the meeting if possible.

### 5. Log_type_mapping.pdf on BayOne GitHub — current status

- Public or private repo? Organization or personal?
- Who has access (BayOne org members, anyone with link, world)?
- What does the PDF contain (Cisco log samples, internal paths, internal hostnames, proprietary error types)?
- Is it still there right now?

**Why this matters:** This is the only persistent artifact on a BayOne-controlled external system. If it is still live at meeting time, Cisco will justifiably see it as unresolved exposure. Removal should happen before the meeting. If it was public, also need to verify no GitHub forks or archives exist. This is the single highest-priority operational action from the prep call.

### 6. AirDropped presentation document — current status

- Where did it end up (BayOne laptop local disk, synced to BayOne OneDrive)?
- Is it still on the BayOne laptop?
- Does it contain anything beyond what was shown in the Friday presentation?

**Why this matters:** Same logic as Log_type_mapping.pdf but smaller radius. Purge before the meeting if it remains on BayOne hardware.

### 7. What has Matt Healy said to Namita, verbatim?

- Exact wording of his concerns (not Namita's summary)
- What he has asked for or required
- Whether he has written anything formal (ticket number, email)
- Whether he has said who else is aware on the Cisco IT side

**Why this matters:** Know Cisco IT Security's current posture before walking in. If Matt has already communicated a corrective-action list, align to it. Do not contradict it in the meeting.

### 7. Has Justin been told, and what is his read?

- Did Justin find out through Matt, through Namita directly, or not yet?
- Is he upset with Namita personally or just concerned operationally?

**Why this matters:** Justin is Namita's operational partner on the build log track. If the personal relationship is damaged, that track stalls. Also Srinivas may or may not know Justin's reaction, and it may come up.

### 8. Was any AI assistance used on the shared files or airdropped content?

- Copilot, Cursor, Claude, or any other external AI tool
- Whether Namita pasted any Cisco source into an external AI tool at any point

**Why this matters:** If Cisco source crossed into a non-approved AI service, that is a separate disclosure issue that compounds the current one. Srinivas has previously noted Copilot and Cursor are approved at Cisco; anything else is not. Better to surface proactively if it happened.

### 9. What does Vaishali know about her own obligations?

- Does she understand Cisco NDA covers this?
- Has she deleted the files?
- Is she available today if Cisco asks for direct confirmation?

**Why this matters:** Cisco may want direct assurance from Vaishali, and because she signed the NDA directly, she is personally on the hook.

---

## Actions To Take Before Walking Into The Meeting

Based on the answers, complete the items below before the Srinivas/Anand call. These are the facts Colin wants in hand.

1. **Log_type_mapping.pdf removed from BayOne GitHub.** Namita does this herself during or immediately after the prep call. Confirm the repo is private or the file is deleted. If public, also request GitHub cache removal.
2. **Vaishali confirms deletion of the four source files.** From her machine, from any Teams message history she controls, from any OneDrive sync.
3. **AirDropped presentation document purged from BayOne laptop** if still present.
4. **Zahra looped in by text or quick call** so the BayOne commercial side knows this is live before the meeting.
5. **Scenario A or Scenario B determined.** Commit to one going into the meeting.
6. **Matt Healy's current asks written down verbatim.**

---

## The 15-Minute Srinivas and Anand Meeting

### Opening (Colin, first 2 minutes)

1. Acknowledge the incident directly. No softening. "We had a data-handling violation on our side on Friday. I want to own that with you up front."
2. Name the four items so they know we are aware of the full scope (do not wait for them to list them).
3. Present the corrective actions already completed (removal, deletion confirmations). Concrete beats apologetic.

### Middle (3 to 10 minutes, Q and A and context)

- Answer questions honestly. If they ask something unknown, say so and commit to follow-up.
- If Scenario A: frame the payload factually without minimizing the behavior. "The files were Python source related to our WebEx scraper scope, not credentials or sensitive IP. The sharing pattern was the violation, not the content."
- If Scenario B: lead with what was in the files, what has been done, and what BayOne recommends for credential rotation or further review. Offer to have Namita describe the facts directly if asked.
- Do not blame Namita by name. Take it as team leadership. They know who did it; the tone should be that Colin owns the team's behavior.

### Close (last 3 to 5 minutes)

- State the forward policy in one paragraph (see separate team policy doc). Do not improvise this; it must be the same language used with the internal team.
- Offer ongoing confirmation. "I will send Matt Healy written confirmation of all corrective actions by end of day."
- Do not ask for forgiveness. Ask what else they need.

### What to avoid

- Do not lead with "good intentions" or "in good faith." These are true but they are the weakest possible opening; they read as deflection. Save them for late in the meeting if relevant, framed as context not justification.
- Do not compare to what other vendors do, or to any past incident in their environment.
- Do not promise anything operational without a date attached.
- No em dashes, no jargon, no hedging language in the opening.

---

## The Namita One-On-One (Inside the Prep Call)

Colin has already delivered the final warning by text, so the 30-minute prep is tactical, not disciplinary. Posture:

- Open with the questions, not with the warning. She has already heard it.
- Keep her focused on facts; she is remorseful and may volunteer more than needed. Redirect to specifics.
- Do not coddle, but do signal that the relationship is intact as long as the pattern does not repeat. Her thoroughness, responsiveness, and ownership on this engagement are genuinely strong; the incident does not erase that and she should know Colin sees both.
- End by aligning on the exact talking points for the Srinivas meeting so there are no surprises.
- She should not speak first in the Srinivas meeting. Colin leads. She answers direct questions factually and briefly.

---

## The Internal Team All-Hands (After the Srinivas Meeting)

Separate session with the full BayOne team (Srikar, Saurav, Namita, Vaishali, Tanuja, Askari if reachable). See the separate team policy document for the substance. Timing and tone:

- Same day if possible, while the context is fresh and before the weekend gap
- Lead with the policy, not the incident. Mention the incident briefly as the reason for the reset; do not dwell. Namita has already been addressed privately and deserves not to be re-litigated publicly.
- Be explicit that this is single-strike going forward. No second final warnings.
- Invite questions at the end. Do not cut it short.

---

## Read-Out After The Meeting

Write a brief follow-up document to `team/research/` as set 06 continues:

- `06a_incident_srinivas_meeting_outcome_2026-04-20.md` — what Cisco asked for, what was agreed, remaining actions
- Update `team/tracking/action_items.md` and `team/tracking/blockers.md` accordingly

Matt Healy gets a written confirmation of actions by end of day. Copy Zahra on that message.
