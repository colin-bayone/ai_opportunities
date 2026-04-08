# 01a - Call Prep: Discovery Strategy

**Source:** /cisco/epnm_ems/source/discovery_questions_call_prep_2026-02-20.md
**Source Date:** ~2026-02-18 (prepared between Feb 9 and Feb 20 meetings)
**Document Set:** 01a (Supplementary to Set 01, call prep for the Feb 20 discovery session)
**Pass:** Single pass, call prep analysis

---

## Purpose

This document captures BayOne's preparation for the February 20 discovery session with Guhan and Selva. It reveals what was understood after the Feb 9 meeting, what was unknown, and what strategy was planned for the next conversation.

## What BayOne Understood After Set 01

The call prep restated these takeaways from the Feb 9 meeting:

1. Cisco has a network management product that was modernized with a new UI
2. Major customers are asking for the original UI experience back
3. Reason: their systems are integrated with it, and operators are trained on it
4. Roughly 200 screen pages involved
5. Backend has changed, so reverting is not straightforward
6. Traditional approach (staffing up, 1-year timeline) does not fit the need
7. Cisco is exploring whether AI-assisted development could accelerate this

## What BayOne Did Not Know

The prep explicitly listed five unknowns:

1. The specific product or what the UIs look like
2. Whether this is web-based, thick client, or something else
3. What frameworks are involved
4. What "integrated" means in practice for these customers
5. How the backend changes affect UI compatibility

## Question Strategy

19 structured questions organized into five categories, with a priority table for time-limited scenarios.

### Category 1: Opening (Questions 1-3)
- "Please correct us" framing: walk us through the problem, did we capture the challenge correctly, what does "integrated" mean
- Strategy: let the client speak first, validate understanding before going deeper

### Category 2: Product Understanding (Questions 4-7)
- Web-based vs thick client, old framework, new framework, side-by-side access
- Strategy: establish the technical landscape

### Category 3: Technical Context (Questions 8-11)
- Missing functionality vs look/feel, backend changes preventing revert, complexity variation across screens, shared components vs independent
- Strategy: understand the conversion challenge depth

### Category 4: Available Resources (Questions 12-15)
- Source code access, design documentation, dev/test environment, point of contact
- Strategy: determine what BayOne would have to work with

### Category 5: POC Identification (Questions 16-19)
- Representative screens, self-contained candidate, success criteria, code sharing constraints
- Strategy: scope a proof of concept

### Priority Table (If Time Short)

| Priority | Questions |
|----------|-----------|
| Start Here | Walk us through the problem (#1) |
| Verify | Did we understand correctly? (#2) |
| Critical | What does "integrated" mean? (#3) |
| Critical | What are the frameworks? (#5, #6) |
| Critical | Can we access both UIs and code? (#7, #12) |
| POC | What is a good candidate screen? (#16, #17) |

## Retrospective Notes (What Actually Happened in Set 02)

Comparing this prep against Set 02 (the actual Feb 20 meeting):

- **"Please correct us" framing worked.** Guhan and Selva opened by reframing the problem in more precise terms than the prep assumed.
- **Unknowns 2-4 were answered.** Web-based (confirmed), Dojo/JavaScript to Angular (frameworks), "integrated" was clarified as operational dependency not API integration.
- **Most prepared questions were answered organically.** Colin noted in the meeting: "I did this before the meeting, so actually, I think a lot that's on here has already been answered."
- **The prep underestimated backend complexity.** The call prep assumed "backend has changed" but Set 02 revealed the vertical nature of the gaps (entire stack missing, not just UI).
- **No design documentation** was confirmed, validating the prep's question about it.

## Summary

This call prep demonstrates thorough preparation and a consultative approach. The "please correct us" strategy was effective: it positioned BayOne as listeners first, and the priority table shows focus on the most decision-relevant questions. The biggest gap in the prep was underestimating the vertical (full-stack) nature of the conversion work, which was only revealed during the actual meeting.
