# 01 - Call Prep: Summary

**Source:** `source/lam_call_prep (1).txt`
**Source Date:** 2026-03-12
**Document Set:** 01 (Call Prep)

---

## What This Set Covers

Pre-call preparation for BayOne's discovery call with Lam Research on 2026-03-12. Four detail files:

| File | What It Covers |
|------|---------------|
| `01_call_prep_situational_context` | Who Lam is ($17B+ semiconductor equipment company), why IP protection is existential (customers are competitors who share production data with Lam), what we knew going in (Azure stack, guardrails "failing," all AI pulled back, 20% error rate target), and four working hypotheses to validate |
| `01_call_prep_discovery_strategy` | Call format (Lam presents, Q&A, BayOne responds later), question bank organized by 8 categories, and signals to listen for that distinguish a consulting/configuration opportunity from a custom build requirement |
| `01_call_prep_technical_reference` | Reference material on the Microsoft stack (Sentinel vs. Purview vs. Content Safety), shadow AI industry statistics, AI governance maturity model, and guardrail testing concepts |
| `01_call_prep_people` | Known information about Bradley Estes (decision maker), Mikhail Krivenko (presenting), Daniel (technical lead, not yet met), and BayOne team members |

## Key Hypotheses Going Into the Call

1. "Failing guardrails" likely means Purview DLP misconfiguration, not Sentinel (Sentinel can't block content)
2. Microsoft's out-of-the-box Sensitive Information Types don't cover semiconductor IP
3. Custom SIT configuration probably not fully implemented
4. Shadow AI likely a bigger factor than Lam is admitting

## Open Questions for the Call

- What does "20% error rate" actually measure? False positives, false negatives, or combined?
- Which tools specifically are failing? What have they configured?
- What does "sensitive" look like in their context?
- Who owns AI governance? Is there formal structure?
- What's the timeline and success criteria?

## State After This Set

We have a well-prepared game plan but have not yet heard from Lam directly. Everything above is BayOne's pre-call interpretation. Document set 02 (the meeting transcript) will show what actually happened on the call.
