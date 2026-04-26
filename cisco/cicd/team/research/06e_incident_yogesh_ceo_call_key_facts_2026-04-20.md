# 06e - Incident: Yogesh CEO Call

**Source:** /cisco/cicd/team/source/week_2026-04-20/day_2026-04-20/yogesh1_formatted.txt
**Source Date:** 2026-04-20 (Colin's briefing call to Yogesh, CEO of BayOne and Colin's direct superior)
**Document Set:** 06 (IT security incident — supplementary 06e, CEO briefing)
**Pass:** Key-facts extraction and authorization-gap identification
**Note:** Source is speech-to-text. Common corrections applied silently (Amital = Namita; Vashali/Vishali = Vaishali; Bonnie = unclear, likely "BayOne"; Suva = unclear proper name; Pradeep = unclear proper name).

---

## Summary

Colin briefed Yogesh on the full incident following the framing plan in `/cisco/cicd/team/planning/yogesh_call_framing_2026-04-20.md`. The briefing itself was delivered coherently and covered every material fact. Yogesh's response, however, did not match the gravity of the incident or the authorization asks Colin came in with. He defaulted to a "hear her out, no ill intent, people make mistakes" posture, declined to authorize the Keka incident report without Sonya's pre-clearance, and did not commit to any of the five authorizations Colin requested. This is a material alignment gap between Colin's engagement-level judgment and Yogesh's CEO-level posture that will need to be closed — likely by parallel pressure from Neha and Zahra, who have independently reached a more decisive conclusion (see 06f).

## What Colin Delivered

Colin covered the complete fact set as prepared in the framing doc:

- The four Python files shared BayOne-to-BayOne Teams on Cisco hardware
- The 80 GB figure on Cisco's CSIRT record
- The AirDrop workaround after Teams blocked the zip
- The BayOne GitHub upload
- The standing guidance violated: "Bay1 to Cisco okay; Cisco to Bay1 never; no downloads without approval"
- Rahul Bobbili's prior Tuesday guidance also violated
- Namita's over-disclosure to Matt Healy (CSIRT) without looping Colin in
- The Anand call and the Anand-as-GPS-POC commitment
- Namita access suspended, Vaishali signed NDA
- Colin's recommendation: final written warning + three-month probation + traffic monitoring + signed policy + accept any Cisco personnel decision

The briefing was clean, factually accurate, and in the logical order the framing doc called for.

## Yogesh's Response — And Why It Is Inadequate

Yogesh's substantive reactions, paraphrased from the transcript:

- "I hope Namita understands the severity of it." Reframes the issue as Namita's comprehension, not BayOne's response.
- On Vaishali's onboarding: "I requested for onboarding and the person is going through the process." Defensive about the hiring decision, which was not being questioned.
- "Namita, out of ignorance, did not know what to share and when to share. I apologize on Namita's behalf, but there was no ill intent by any means on this one." Directly offers a mitigating frame (ignorance, no ill intent) that neither Cisco nor BayOne's internal evidence supports — Colin had explicitly documented the repeated prior guidance that was disobeyed.
- "My assumption is have a one-on-one with her, without panicking her." Turns the recommended decisive action into a soft conversation. Colin's framing was "final warning + probation + escalation path," not "hear her out."
- "Hear her out. Hear her out. Read the body language and then maybe we can reconvene." Defers the decision to a later conversation based on subjective reads.
- "At times, these guys, because just sheer lack of experience, they do all those things. Maybe Bonnie [BayOne] can just take care of it." Minimizes the incident by attributing it to inexperience and suggests internal handling without clarity on what that means.
- On the Keka incident report: "I will check with Sonia on this. I know that she's out." Blocks Colin from filing the report today — makes it dependent on an HR person who is unavailable.
- On reading back: "I will tell you what she is for sure" — garbled/unclear in the transcript but reads as non-committal on all five authorization asks.

## Authorization Scorecard

| Colin's Ask | Yogesh's Response |
|---|---|
| Authorize final warning + probation + monitoring path | Deferred. "Hear her out first." |
| Authorize pulling Sonya in from HR | Deferred. "I will check with Sonia." Colin cannot file on Keka yet. |
| Authorize signed policy rollout to the full Cisco team this week | Not discussed affirmatively. Colin signaled his intent ("I'll make a written one that says, and everyone's going to be forced to sign it first") but Yogesh did not explicitly authorize. |
| Align on Zahra loop-in sequencing | Not addressed. |
| Align on full-acceptance posture with Cisco (accept any outcome) | Not explicitly agreed. Yogesh's tone was optimism about Anand, not acceptance readiness. |

Net result: **zero of five authorizations granted.** Yogesh's posture preserves Colin's ability to continue damage control but does not give Colin the procedural backing he came in to secure.

## Yogesh's Framing Where It Is Useful

Not all of Yogesh's response was obstructive. Two items are usable:

1. On Anand: "The good part is that you've already beaten Anand." He validated that the executive-layer damage control was correct and sufficient at that layer.
2. On Srinivas: "It depends upon how much he reads into what their cybersec tells him." Implicit agreement that the GPS/Data Protection layer is the real risk, not Srinivas directly.

## The Gap Between Colin's Judgment and Yogesh's Posture

Colin's view of the incident, as stated in the call and consistent with his framing doc:

- Repeated prior guidance + active propagation to teammates + over-disclosure to Cisco IT = not a "mistake out of ignorance"
- The 80 GB figure and the AirDrop circumvention show carelessness of an intolerable degree for a paid engineer on a client engagement
- "No company on this earth would ever think it was okay to send 80 GBs of files, legitimate or not"
- "Even if I was to send them to Suva, I would hope that Pradeep would call me out on it" — Colin invokes peer-accountability to underline the seriousness

Yogesh's view, as stated in the call:

- Ignorance and inexperience
- No ill intent
- Hear her out, read body language, reconvene
- BayOne can handle internally without escalation

This is not a factual disagreement — Yogesh is not contesting any of the facts. It is an interpretive and procedural disagreement. Colin sees the facts as requiring decisive personnel action. Yogesh sees them as requiring a conversation.

## Implications

1. **Colin cannot unilaterally issue a written warning on Keka without Sonya-Yogesh pre-clearance.** This is an HR procedural block that prevents Colin from closing out the formal record today.
2. **Colin's position with Cisco requires decisive posture BayOne does not yet have.** If Cisco (via GPS) asks what BayOne has done, Colin cannot yet point to filed documentation or authorized personnel action — he can only point to verbal warnings and a drafted policy.
3. **Parallel pressure is needed.** Colin alone has not moved Yogesh. Independent outreach from Neha and Zahra, both of whom have reached a harder conclusion (see 06f), is the most promising path.
4. **Colin's personal position is solidifying toward immediate removal regardless.** Language in the call: "I'm just going to ice her out from the team is how that's going to go. Because I can't trust someone like that on a client engagement." This is stronger than the framing doc's baseline recommendation.
5. **The signed policy rollout becomes the primary corrective-action artifact Colin can move on without Yogesh's explicit authorization.** The policy as drafted is Colin's authority as engagement lead; Yogesh has not blocked it even if he has not affirmatively authorized it.

## Forward Actions From This Call

- **Colin:** Continues damage control, holds the Srinivas message line already sent, handles the weekly Srinivas call.
- **Colin:** Does not file on Keka until Sonya is reachable. Does proceed with the signed policy draft rollout planning.
- **Neha and Zahra (from 06f):** Will independently call Yogesh to apply pressure toward a faster decision.
- **Zahra:** Will talk to Venkat for additional Cisco-internal guidance on GPS handling.
- **Open item:** If Sonya is unreachable through the end of today, Colin needs a contingency for filing the Keka report on Tuesday without further delay.
