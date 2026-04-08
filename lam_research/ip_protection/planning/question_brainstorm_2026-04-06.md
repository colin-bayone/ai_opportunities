# Question Brainstorm: April 6 Lam Call

**Date:** 2026-04-06
**Status:** Working document, brainstorming in progress

---

## Context

This is a hybrid meeting (technical + business leadership). Lam requested it as a precursor before they answer BayOne's specific questions. Daniel Harrison is new to the conversation. Brad and Mikhail will also be present. This is a conversation, not an interrogation. It needs to flow naturally.

### New Intel from Pre-Call (April 6 morning)

- **CSBG vs. GIS:** Brad's team (CSBG) has the money and customer relationships. GIS (IT/engineering) has a new CIO who is bringing their own vendors. BayOne is losing business on the GIS side. Brad is funding this directly, bypassing GIS. Our positioning should empower Brad's team.
- **Pat is tactical wingman.** He backs Colin up when answers get vague. "My ultimate customer today is you [Colin]." This worked well last time.
- **Daniel may not know much about AI.** Pat: "I don't have a lot of high hopes." He's an engineering lead, not an AI person. Temper expectations for the technical autopsy.
- **Mikhail's real litmus test:** He gave 9 documents to the system, 7 had IP that failed to get detected. Concrete test case.
- **No pricing numbers today.** Team agreed. Sound responsive, plant the "what is this worth to you?" seed, but no figures until scope is defined.
- **Worst case outcome:** Lam says "just do a POC where you detect stuff and we'll feed it documents." That's a non-starter. They need to give us a specific business case.
- **Empowerment angle:** Position BayOne as empowering Brad's team so they don't need to depend on GIS. Brad has said "there is enough work and opportunity, all he wants to see is who is really capable."
- **Meeting format:** 1-2 icebreaker slides (recap + what we need today), then questions. Not a presentation.

---

## 1. Opening and Stage-Setting

Brad will likely frame why they're here. After introductions settle, our side sets the tone:

**Colin's opener:**
"Last time we met with Brad and Mikhail, they walked us through the two use cases and the challenge with false positives. We came away with a solid understanding of what you're trying to solve. What we'd love to do today is go deeper on the technical side, understand what's been tried, and get to a place where we can scope something specific for you."

This does three things:
- Acknowledges the prior meeting (continuity for Daniel's benefit, he wasn't there)
- Signals we're here to listen again, not pitch
- Sets the agenda as technical discovery

**Bridge to Daniel:**
"Daniel, I know you're closer to the technical implementation side. I'd love to hear your perspective on what's been attempted so far."

This invites Daniel to talk. Whatever he says becomes the natural springboard for the technical questions below. We follow HIS thread, not ours.

---

## 2. Prior Work / Technical Ground Plane

These questions live INSIDE Daniel's response to the opener, not as a pre-planned sequence. Ask them as natural follow-ups to whatever he shares.

**Note:** Daniel may not have deep AI knowledge (Pat's assessment). If he defers on the ML specifics, that's actually useful intel. Pivot to what he DOES know: the systems, the data, the workflows.

**Core questions (ask as the conversation allows):**
- "What system were the models running against? What data were you feeding them?"
- "Was this your internal team's work, or was this from the prior engagement?"
- "How did you construct the ground truth? Were documents hand-labeled, or were you working from known-flagged tickets?"
- "When something got flagged incorrectly, what was the pattern? Was it grabbing generic mentions of customer names in non-sensitive contexts, or was it something else?"
- "The fine-tuning moved it from 20% to 17%. What specifically changed in that iteration?"

**What these tell us:**
- Who built it (Accenture involvement without naming them)
- Daniel's personal proximity to the failure
- Whether they had a proper benchmark (we suspect they didn't)
- Whether the problem was model architecture, training data, or entity definition
- Daniel's actual AI knowledge level (critical for pricing leverage)

---

## 3. Application / Entry Point

Flows from Block 2. Once we know what system the models ran against:

- If a system is named: "Is that the same one you'd want us to focus on for a POC scope?"
- If it stays general: "For us to scope something concrete, can you point us to one application as the starting point for the same type of testing?"
- If they resist: "Even pointing us to the system that gave you the most pain would be a great place to start."

**Pat's role here:** If Mikhail or Brad stay vague again, Pat pushes: "To move forward and help you, we need to anchor on one specific system. Which one would give you the most value?"

**What we need about that application:**
- What does it do? What's its purpose?
- What audience does it serve?
- What data sources feed it?
- How does data get in (ingestion patterns)?
- What does the current restriction mechanism look like?
- Is it on Azure, on-prem, or hybrid?

---

## 4. Success Criteria

**Approach:** Do NOT throw around specific numbers (20%, sub-1%, 97% in 5 seconds). Those were off-the-cuff hand-waving. Let them define success in their own words.

**Core questions:**
- "What did you try before, and why was it not successful to you?"
- Follow-up: "What does success look like? What should the outcome have looked like in that case?"
- "Mikhail, last time you mentioned giving the system some documents and seeing what it caught. If we were to do something similar as a pilot, what would make you confident it's working?"

**Reference point:** Mikhail's concrete test: 9 documents, 7 with IP that failed detection. This is a real test case we can anchor to without throwing numbers around.

Let Daniel and the engineering lead answer this. Their definition of success will be more grounded than the aspirational numbers from the first call. We listen and calibrate from there.

---

## 5. Daniel-Specific (Technical Depth)

**If Daniel has AI knowledge:**
- "What was the MLOps setup? What infrastructure was this running on?"
- "Were you using any Azure AI services specifically, or was this custom model hosting?"
- "What did the training pipeline look like?"

**If Daniel defers on AI (more likely per Pat's assessment):**
- Pivot to what he knows: systems, data, workflows
- "Walk me through how a document gets into the knowledge base today."
- "What does the escalation ticketing system look like under the hood?"
- "What's the tech stack for the applications Brad's team owns?"
- This is equally valuable. Understanding the systems architecture is critical for scoping.

**Gauging Daniel's perception of difficulty:**
- Listen for whether he thinks this is solvable or if he's skeptical
- If skeptical: good for pricing leverage, validates BayOne's value
- If he thinks it's simple: different positioning needed

---

## 6. Business / Brad-Facing

**Empowerment positioning (from pre-call intel):**
- Frame everything as enabling Brad's team to own their technical destiny
- "We want to make sure your team has the capability to maintain and extend whatever we build together."
- Do NOT reference GIS or the CIO tension. Just position as empowering CSBG naturally.

**Scope and next steps:**
- "Based on what we learn today, we'd like to come back with a concrete, scoped proposal. What information do we still need to make that happen?"
- If they ask about cost: "The scope and complexity are driven by the information we get from your team. The more specific you can be, the quicker we can get you a quote and get started."
- Do NOT give numbers. Anuj handles any direct pricing questions.

**Long-term framing (light touch only):**
- "We see this as the starting point of a longer partnership, not a one-off project."
- Only if Brad or Pat opens that door. Do not push.

---

## 7. Competition / Positioning

**Do not ask directly.** Listen for signals:
- How much do they ask "what are others doing?" (If a lot: they're shopping. If not: we may be the only game.)
- Any references to other conversations or evaluations
- Urgency level (high urgency + no competition = strong position)

**If they ask what others are doing / off-the-shelf tools:**
- "We've looked at what's available. For standard PII (social security numbers, credit cards), there are off-the-shelf tools. For domain-specific IP like semiconductor customer names and fab identifiers, there's nothing off the shelf that works. That's why a custom approach is necessary."
- This positions BayOne as having done the homework without overselling.

**If prior partner work comes up:**
- Ask about the work, not the firm: "What was the goal of that effort? What was the approach?"
- Colin's insight from April 1: "Ask basic questions like 'what was the goal for this?' -- gives you credibility while taking it from the other guy."

---

## Parking Lot (Do Not Raise Today)

- Unified control plane architecture
- Ingestion-first philosophy
- Full hybrid architecture details
- Pricing numbers
- Headcount or hourly rates
- Anything that sounds like scope expansion beyond what Brad asked for

---

## Notes from Brainstorm

- The opener is NOT a question. It's stage-setting that gives Daniel context and invites him to talk.
- Let Daniel's response drive the conversation. Follow his thread.
- The technical questions are ammunition to deploy inside the conversation, not a checklist to march through.
- Colin corrected the approach: this is a fluid conversation, not a structured Q&A.
- Success criteria: do not use specific numbers from prior calls. Let them define success in their own words.
- Pat is the wingman. When answers get vague, he pushes for specifics.
- Daniel may not have AI depth. That's fine. Pivot to systems/data/workflows.
- Empowerment angle: position as enabling Brad's team, not as a vendor selling a product.
- No pricing today. Period. Sound responsive, plant "what is this worth to you?" seed, numbers come later.
