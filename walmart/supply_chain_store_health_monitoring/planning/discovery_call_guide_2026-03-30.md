# Discovery Call Guide — Troy Ward, Walmart
## Colin's Eyes Only | March 30, 2026

---

## Pre-Call State

**What we know:**
- Troy Ward, Director of IT Operations in Supply Chain at Walmart
- His team manages: POS, self-checkout, payment systems, store networks, associate devices (handhelds/scanners), IoT/store infrastructure
- Heavy operational and support workload
- Primary challenge: health checks and early diagnostics for in-store machines, catching issues before they impact store performance
- Also interested in: predicting outages, real-time monitoring of all store tech systems
- Warm referral through someone Surej knows personally

**What Troy has been told (by Kanchan, verbally, nothing written):**
- BayOne has experience with multimodal AI and supervised fine-tuned models for predictive diagnostics
- "We can talk more deeply about how we did all of this"
- BayOne has been working on AI solutions focused on improving IT support and operations, especially around automating issue resolution, improving ticket quality, and enabling faster troubleshooting

**What Troy expects:** A conversation about experience with predictive diagnostics. NOT a demo or product showcase.

**What we do NOT know:**
- Whether Troy is connected to the Round 1 Walmart contact (Amit's deck)
- What health data his machines currently produce
- Whether there's an existing monitoring platform
- Whether this is proactive or reactive
- What the resolution path looks like after a predicted issue
- Who else he's talking to
- Timeline, budget, approval process

---

## The Hook

**DO NOT lead with Coherent.** "I built something similar at my last company" is resume-pitching. Troy hears that from every vendor.

**Lead with understanding of his world.** The credibility is in showing you've thought about his problem before he describes it. You understand the difference between predicting an outage and actually resolving one. You know that monitoring data maturity determines whether AI is even the right first step. You've thought about what happens when a self-checkout unit throws a warning at 2am in a store with no on-site tech.

**The Coherent story comes out when Troy asks "how do you know this?"** — not before. It becomes a natural proof point, not a pitch.

---

## Call Flow

### Phase 1: Surej Opens (2-3 min)
Referral warmth, relationship context. Surej should reset expectations early: "This is a conversation to understand your world and see if there's a fit." This neutralizes the meeting title.

### Phase 2: Colin Takes Over (60 seconds max)
Brief, domain-aware opening. Something like:

> "Troy, thanks for making time. I lead the AI practice at BayOne. When I heard your team is looking at health monitoring and early diagnostics for in-store systems, that immediately resonated with me. That pattern — distributed infrastructure, high uptime requirements, the need to catch issues before they reach the customer — is something I've spent a lot of time on. But every environment is different, and the specifics matter more than the pattern. So I'd really like to understand your world before we talk about anything else."

**What this does:** Establishes domain awareness without naming Coherent. Shows you've thought about the problem. Frames you as someone who listens before proposing. Hands control to Troy.

### Phase 3: Discovery (25-30 min)
Follow the themes on the screen-share doc. Let Troy talk. Your job is 30% talking, 70% listening.

### Phase 4: Close (3-5 min)
Summarize what you heard back to Troy. Propose a concrete next step. Let Surej handle the relationship close.

---

## Discovery Themes (Reference — the HTML doc covers these visually)

### Theme 1: Current State (START HERE)
Understanding what exists shapes everything. If there's telemetry and monitoring already flowing, the AI conversation is real. If it's reactive/manual, the first step is instrumentation, not AI.

- What does monitoring and alerting look like today?
- What health data do these machines produce? Telemetry, logs, error codes, heartbeat signals? Or is it mostly a black box until something breaks?
- Is there a system of record for incidents and tickets?
- What tools or vendors are already in the mix? Anything tried that fell short?
- Have you explored any AI/ML approaches before?

### Theme 2: The Problem
- Is this proactive (building toward something) or reactive (responding to active pain right now)?
- When a machine goes down today, how does your team find out?
- What's the typical time from "something is wrong" to "it's fixed"? Where does the most time get lost?
- Are certain systems more problematic than others?
- **The resolution mode question (your insight — use it):** "Here's something I think about a lot. Predicting an outage is one piece, but what happens after the prediction matters just as much. If we know a self-checkout unit is going to fail, what does the resolution path actually look like? Is there a tech dispatched to the store, a remote fix, a parts replacement? How does that whole chain work today?"
- What does downtime actually cost you? Not just dollars but operationally.

### Theme 3: What Success Looks Like
- If this is working a year from now, what does that look like?
- Specific metrics you're trying to move? MTTR, uptime %, incident volume?
- Is this primarily about reducing downtime, cost, or experience?

### Theme 4: Priority and Next Steps
- Where does this sit in terms of priority for your team right now?
- Is there a timeline or milestone driving this? Budget cycle, leadership mandate?
- What would a good next step look like from your perspective?
- (Only if flowing naturally) How does something like this get approved or funded on your side?

---

## Signals to Listen For

| Signal | What It Means |
|--------|---------------|
| **Data-rich environment** (telemetry, logs, existing monitoring) | AI conversation is real. Predictive models, anomaly detection, smarter alerting. Your Coherent experience maps directly. |
| **Data-poor environment** (reactive, no telemetry, manual) | First problem is instrumentation, not AI. Be honest. Don't sell AI where the foundation isn't there. |
| **Unclear resolution path** | Predicting outages is only half the value. If a prediction doesn't connect to a clear action, the value proposition changes. |
| **Specific vendors or platforms mentioned** | Tells you what's been tried, what failed, where the gaps are. Also whether he's shopping for a product or looking for help building something. |
| **Visual troubleshooting connection** | If techs are diagnosing hardware in stores visually, the Coherent case study is directly relevant. Bring it up naturally. |
| **Volunteered budget/timeline** | Bonus. Don't push for it. |

---

## The Coherent Case Study (Back Pocket)

**When to bring it up:** When Troy asks how you know this, when the conversation naturally connects to field techs diagnosing equipment, or when he describes a data-rich environment where predictive models would fit.

**How to frame it:** "I led a program at a previous organization that dealt with the exact same pattern. Global field service, 8,000+ pieces of complex equipment across 40 countries. We built a system where techs could diagnose faults faster using AI, cut resolution time in half, and significantly reduced unnecessary expert dispatches. Different industry, but the same core problem."

**Key numbers if asked:**
- 50-60% reduction in ticket resolution time
- First-pass fix rate: 71% to 91% (+28%)
- 50% reduction in expert call-outs
- ~$3.2M annual SLA penalty reduction
- 93% fault-classification accuracy
- Sub-2 second inference latency
- 15-week program, 12-person team

**NEVER position this as a BayOne product.** It is your experience. You can build something similar, tailored to Walmart's environment, but there is no off-the-shelf version.

---

## What NOT To Do

- Do not present a capability deck
- Do not promise anything. "Let me take this back and put some thinking together" is always right.
- Do not pretend BayOne has retail-specific experience. Be honest that the pattern is the same but the domain is new.
- Do not talk more than 30% of the time
- Do not ask binary build-vs-buy questions. Weave it into natural conversation about timeline and priorities.
- Do not bring up capacity constraints on the call. That's an internal issue.

---

## Capacity Note (Internal Only)

If this is real, BayOne doesn't have bandwidth for immediate new work. Colin's team is stretched. This is a leadership issue that has been raised for months. Do not let this affect the call. The call is about understanding Troy's world and determining fit. Capacity is solved after fit is established, not before.
