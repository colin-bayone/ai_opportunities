# 02 - Meeting: Summary

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)

---

## What This Set Covers

Full decomposition of the BayOne-Lam Research discovery call on 2026-03-12. Seven detail files plus this summary:

| File | What It Covers |
|------|---------------|
| `02_meeting_people` | Who was on the call, roles, titles, sentiment for each person. Brad (room controller, decision maker), Mikhail (problem presenter, scope guardian), Colin (BayOne technical lead), Pat/Pratik (supporting voice). |
| `02_meeting_topic_map` | Pass 1 high-level topic identification. Nine topics mapped across the meeting. Proposed the five deep-dive files. |
| `02_meeting_technical_use_cases` | Exhaustive breakdown of the two use cases: (1) Self-help search via batch redaction, (2) Escalation entry via real-time detection. Includes the detection vs. redaction distinction, performance requirements, false positive tolerances, the over-restriction problem, the feedback loop vision, and edge cases (spelling variants, OCR, Teams transcripts, auditor fatigue). |
| `02_meeting_what_was_tried` | Every approach attempted: Transformers, SpaCy, Azure AI model (all ~20% false positive, fine-tuned to 17%), rule-based models (abandoned due to spelling variations), 1,000+ hour labeling exercise (paused for cost). Generative AI deliberately NOT tried. Colin's key assessment: 20% = out-of-the-box ChatGPT. |
| `02_meeting_infrastructure_and_access` | Infrastructure landscape: on-prem, cloud, LamGPT, Copilot, 6+ search systems, no unified data lake. IAM ~2 years in, "not super robust." Employee taxonomy (blue badge, contractors, LSPs, TRI, embargo). ASM limited scope. Customer segmentation at ticket level. Colin's unified control plane suggestion. |
| `02_meeting_business_opportunity` | Brad owns end-to-end. Wants rapid prototyping, evolutionary not revolutionary, technology agnostic. Previous "pod" model was a pilot, not standard. ROI = feedback loop (solve escalations -> feed back -> reduce costs). Must "repeat back" the problem before proposing solutions. No budget/timeline discussed. Transcript cuts off at "high value targets" answer. |
| `02_meeting_speaker_dynamics` | Brad as room controller (rules of engagement, redirections, "Is that clear, Colin?"). Mikhail as precise translator (framework-first, comfortable saying "I don't know"). Colin's hits (20%/ChatGPT, unified control plane) and misses (IAM drift, jargon). Trust-building and trust-eroding patterns. |

## The Core Problem

Lam Research occupies a unique position: they see production data from customers (TSMC, Samsung, Intel, Micron, SK Hynix) who are direct competitors. Cross-customer data contamination is existential. Their response has been blanket over-restriction, which kills productivity, siloes knowledge, and blocks AI training.

They need to solve two things:
1. **Batch redaction** of stored content so cross-customer knowledge can be searched safely
2. **Real-time detection** at data entry points to notify users of potential IP violations (sub-1% false positive, 2-5 second response)

Everything they've tried has failed: ML models hit 20% false positive (barely better than baseline ChatGPT), rule-based approaches can't handle spelling variation, and a labeling exercise was too expensive without proof of concept first.

## Key Takeaways for Next Steps

1. **BayOne must "repeat back" the problem.** Brad's explicit gate: demonstrate understanding before proposing solutions. The follow-up deliverable should be a problem decomposition, not a solution pitch.
2. **Two separate swim lanes.** Detection and redaction are separate business cases with different requirements. Don't jumble them.
3. **Start with two fields.** Customer name and file name are the MVP scope. If you can't get those right, nothing else matters.
4. **The transcript cuts off at the critical question.** Mikhail was answering "where should we focus first?" when the recording ended. This answer must be recovered.
5. **Connect Colin with Daniel** for technical depth before the follow-up meeting.
6. **Follow-up meeting format:** BayOne presents approaches (plural) with trade-offs. Broader Lam team (including Daniel) will attend. Q&A format, not a pitch.
7. **Avoid jargon.** Mikhail explicitly said "I don't know what that even means" when asked about Azure services. Use their language.
8. **Budget and timeline are unknown.** Neither was discussed. These need to be surfaced in follow-up.

## Hypotheses from Set 01 - Status

| Hypothesis | Status |
|---|---|
| "Failing guardrails" = Purview DLP misconfiguration | **Invalidated** -- it's a custom ML accuracy problem, not a Microsoft tools problem |
| OOTB SITs don't cover semiconductor IP | **Validated** (implicitly) -- they went straight to custom ML |
| Custom SIT configuration not implemented | **Superseded** -- they bypassed Microsoft detection entirely |
| Shadow AI is a bigger factor than admitted | **Open** -- not discussed in the meeting |

## State After This Set

BayOne has a thorough understanding of the problem statement. The next action is to demonstrate that understanding to Lam (the "repeat back" test), then present approaches with trade-offs in a follow-up meeting with the broader team. The missing "high value targets" answer from the transcript cutoff needs to be recovered. Colin needs to connect with Daniel for technical depth.
