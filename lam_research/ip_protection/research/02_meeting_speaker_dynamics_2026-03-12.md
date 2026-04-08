# 02 - Meeting: Speaker Dynamics (Deep Dive)

**Source:** /lam_research/ip_protection/source/lam_discovery_call_2026-03-12.txt
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)
**Pass:** Focused deep dive on speaker dynamics, power structure, and meeting flow

---

## Executive Summary of Meeting Dynamics

This was Brad's meeting. He set the format, controlled the pace, established the rules of engagement, and redirected speakers when they strayed. Mikhail functioned as Brad's technical translator and whiteboard driver, executing the presentation while Brad managed the room. Colin delivered several moments that clearly landed (the 20%/ChatGPT diagnosis, the unified control plane concept) but also got redirected on an IAM tangent that earned a pointed "Is that clear, Colin?" from Brad. Pat contributed targeted, high-value questions on ingestion and ecosystem knowledge. The BayOne team's overall performance was solid but uneven -- Colin's best moments showed deep domain credibility, while his less disciplined moments triggered Brad's vendor scar tissue.

---

## 1. Pre-Meeting Setup and Format Control

### Brad Establishes the Physical and Conversational Space

The meeting opens with Brad already in motion, directing the room setup. He has decided in advance that this will be a whiteboard session, not a slides session, and he announces this decision, not proposes it:

> "We have slides, but we wanted to whiteboard to have an interactive discussion, because usually when you have stuff on slides and you want to draw an arrow or you want to do something, it's very difficult."

This is a significant format choice. A whiteboard session gives Brad and Mikhail physical control of the room -- they stand, they draw, they narrate what goes on the board. The BayOne team watches. It is a deliberate inversion of the typical vendor pitch dynamic where the seller presents and the buyer listens. Brad has designed this meeting so the buyer presents and the seller listens.

Brad then invites Pat to potentially join and "put your laptop at the screen," which gets a slightly amused response ("Well, I guess that's very innovative and creative. We do our best."). The early banter is loose and collegial -- this is not a tense room. But Brad is clearly the person deciding how the physical space operates.

### Mikhail as Whiteboard Driver

Mikhail has a specific slide or document he wants to find before starting: "I'm searching for one document that I have. I need like one minute for that. If I can't find it fast enough, we'll whiteboard."

This reveals that Mikhail has prepared structured content but is flexible about delivery format. When he cannot find the document quickly, he defaults to the whiteboard without friction. He is comfortable operating either way. This speaks to someone who knows the material cold and has internalized the structure well enough to reconstruct it from memory.

---

## 2. The Introductions: Establishing Credibility and Reading the Room

### Colin's Introduction: Enthusiasm and Domain Signaling

Colin's introduction is long and detailed. He covers:
- His background at Coherent (laser semiconductors, advanced materials)
- His career progression: process engineer to R&D engineer to chemical process engineer to AI leadership
- Founding and leading Coherent's AI Center of Excellence (50 members, global)
- Reporting directly to CEO and CIO
- Advisory role for legal, compliance, and cybersecurity teams
- ITAR, CMMC, DFARs experience (space and defense)
- Managing IP in China specifically

The introduction is strategically designed to signal domain credibility on exactly the problem Lam faces. Colin is saying: I have done this before, at a semiconductor company, with the same type of IP sensitivity. Key phrase:

> "So I was both lead for the AI Center of Excellence. I reported right to the CEO and CIO."

And the China reference is pointed:

> "One of the fun things that we had to navigate was doing things in China. So definitely managing IP, the exact same problem as I understand it right now, I think we have a good grip on."

Colin also front-loads his excitement, which is genuine but also runs a risk of coming across as presumptive:

> "I think the reason why I'm really excited today is because I think we have kind of a lot of alignment maybe between what I've done in the past and I think what I believe today is about. I won't say too much before I hear about it, but that's why I'm excited."

**Dynamic note:** Colin's intro runs longer than is typical for a discovery call where the buyer has explicitly said they want to present. He catches himself ("I won't say too much before I hear about it") but has already said quite a bit. This is the first indicator of a tendency toward verbosity that Brad will later correct.

### Mikhail's Introduction: Precise and Concise

Mikhail introduces himself in two sentences:

> "My name's Mikhail Kravenko. I'm a head of product in Brad's organization. So on the product management, I do IT design and the product order. So both ideation and execution part of the process."

This is revealing. Mikhail defines himself relationally ("in Brad's organization") and functionally ("both ideation and execution"). He does not offer a career history or credentials. He lets his role speak for itself. The contrast with Colin's introduction is sharp.

### Brad's Introduction: Even More Concise

Brad gives one sentence:

> "And I run the knowledge management and event services organization, mostly supporting many different flavors of our support business group."

Then immediately pivots to the content: "So we will be using whiteboard." Brad has no interest in posturing. He has established his authority through format control, not through recitation of credentials. He is the most senior person in the room, and he knows everyone already knows that.

---

## 3. Brad's Opening Frame: The Rules of Engagement

### The "We've Heard It Before" Declaration

Brad's opening statement to the BayOne team is the single most important passage in the transcript for understanding the dynamics of this engagement. It must be decomposed carefully:

> "So today is all about sharing what we believe our, well, what our problem statement is. We can talk, I think, about what we tried to do and maybe what we learned and maybe what some of those results were and what we really want to be able to do."

Standard setup. But then:

> "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that."

This is a direct instruction to the BayOne team: do not pitch me. The phrasing "oh, I've got a technology solution that can solve that" is mimicry -- Brad is quoting back what vendors typically say, and doing so dismissively. He continues:

> "We want a very, because **we've heard it before**, we want people to be, we want the team to be able to report back to, or to repeat back to us, there's a very clear understanding in what we're trying to solve, right? And so that's critically important."

**"We've heard it before."** This is the vendor scar tissue statement. Brad has been through this with other vendors -- likely Capgemini, possibly others -- and they jumped to solutions too fast, probably made promises that did not land. Brad is inoculating against that by establishing an explicit rule: you will demonstrate understanding before you propose anything. He is testing the BayOne team's discipline. Can they listen first?

Brad then sets the incremental framing:

> "We're starting very, very small. And some of the things that I think we want to prove out, or we tried to prove out in our initial [effort], was just really about two attributes or two data fields, right? Because if you can't get those correct, and you can't redact or do whatever we're trying to do with those, you can't escape, right?"

This is Brad telling BayOne: do not come back with a grand architecture vision. Start with two fields. Prove you can do those. Then we talk about more.

### The Invitation to Ask Questions -- But with a Caveat

Brad then opens the floor:

> "Please, let's ask questions. If there's things that we're not saying, please inquire what those are, because there could be information that we didn't think about sharing that we want you to say, hey, what about this? What about that?"

But he adds:

> "Because it may be relevant or it may not be relevant. So it's better to ask those questions, seek that clarity, than to just take what we're feeding, so to speak."

Brad wants active listeners, not passive recipients. He is evaluating whether the BayOne team can demonstrate intellectual curiosity about the problem without jumping to solutions. This is the test he is running.

---

## 4. Mikhail's Presentation: The Technical Translator at Work

### The Whiteboard Structure

Mikhail takes over and builds a structured framework on the whiteboard: a troubleshooting workflow with three stages (self-help/search, ask-for-help/expert help, and escalation). He then maps two distinct IP protection use cases onto this workflow:

1. **Search/self-help use case:** How to produce meaningful search results while removing customer confidential information from the results
2. **Ask-for-help/escalation use case:** How to detect and prevent users from entering customer confidential information in their problem statements

Mikhail presents this with the clarity of someone who has thought about it extensively. He uses specific language:

> "So number one, let's talk about search. So when you're searching for things, there could be customer confidential information, the CI documents, and there could be other things that are located in this area where you might or might not have access to."

### Mikhail's Intellectual Honesty

One of the most striking dynamics in this meeting is Mikhail's willingness to admit the limits of his knowledge. When Colin asks about Azure AI Foundry and similar tools later in the call, Mikhail says plainly:

> "You're not talking to a technical audience here."

And:

> "Again, I don't know what that even means."

This is not false modesty. Mikhail is establishing a boundary: I know the product and business case cold, but I am not the person to discuss specific Azure services with. He does not pretend. He names specifics where he can ("We tried Transformers model, SpaCy, and... Azure AI model") and draws a clear line where his knowledge ends. This honesty is a strength -- it signals to BayOne that Mikhail will not nod along with something he does not understand, and that technical discussions will need to happen with Daniel's team.

### Brad and Mikhail as a Coordinated Unit

Throughout the presentation, Brad and Mikhail operate as a unit but with distinct roles:

- **Mikhail presents.** He builds the whiteboard, walks through the workflow, explains the technical details he knows.
- **Brad contextualizes and enforces.** He adds business context ("This is very costly"), redirects when conversations stray, and reframes when needed.

They finish each other's thoughts naturally. When Mikhail explains over-restriction, Brad jumps in:

> **Brad:** "Well, is it worth saying that our current mode of operation is we over restrict?"
> **Mikhail:** "100%, right?"

And then they volley:

> **Brad:** "True, but we're also knowing that we're limiting the productivity, the capability, because we don't share that much."
> **Mikhail:** "Exactly."

This back-and-forth is not rehearsed -- it is the product of people who have been working on this problem together and have aligned on the framing. They challenge each other in small ways ("Well, is it worth saying...") but always converge.

---

## 5. Colin's Interventions: Hits and Misses

### First Intervention: Unified Knowledge Base and Governance (Early, Mixed)

Colin's first substantive question comes after Mikhail's initial presentation of the search use case:

> "So two quick questions. I'll keep them short because I don't want to take the momentum here."

He asks about (1) whether there is a unified knowledge layer or if it is fragmented by application, and (2) how governance works today -- is this a broad concern or specific to the Q&A use case, and is there a shadow IT dimension?

These are good questions. The "I'll keep them short" preamble shows Colin is aware of the format rules Brad set. Mikhail engages with both questions substantively. The governance question draws out important information about the over-restriction philosophy.

**Dynamic note:** Colin's self-awareness about not taking momentum is genuine but he does not always maintain this discipline as the meeting progresses.

### The IAM Tangent: Colin's Biggest Miss

The most significant dynamic event in the meeting is the IAM (Identity Access Management) tangent. Colin asks about user identification:

> "Well, like for any of these scenarios, or at least the ones we're discussing here, these are all Lam internal, right? So is user identification part of the query, especially when we're inputting?"

Mikhail engages with this, and Brad adds context about the company's IAM program ("The company's working on getting to more of an IAM identity access management. And so that's an active program that's been going on probably for about two years.").

Colin continues pushing on this thread, talking about how user identification can help with detection -- identifying privileged users who warrant extra scrutiny on uploads. He gives a personal example:

> "I had a high level clearance whenever I was at Coherent. I had access to things that would, you know, make your eyes pop out. And if I uploaded something, I had some special scrutiny on me because they knew that where I was coming from, I had access to that highly classified, highly privileged information."

This is where Brad intervenes. Not harshly, but firmly:

> "I just want to caution against that."

And then, critically, Mikhail reframes what Colin was trying to say, redirecting the conversation back to the defined business cases. Brad has sensed that Colin is pulling the conversation into a third use case (access management/role-based filtering) that was not on the whiteboard and that Brad does not want mixed in with the two defined business cases.

**The "Is that clear, Colin?" Moment:**

After Brad's redirect and Mikhail's reframing, Brad asks directly:

> "Is that clear, Colin?"

This is not a genuine question about comprehension. It is a check -- Brad is making sure Colin has received the correction and will adjust. The phrasing is pointed. Brad does not say "Does that make sense?" or "Are we aligned?" He says "Is that clear?" -- which carries an undertone of "I need you to stay in the lane I've defined."

Colin responds: "Yes. All good."

And then immediately returns to the IAM thread with a justification:

> "The only reason I ask is for the purpose of ingestion to the system. Because, for instance, sometimes even if the knowledge is there, you have to segregate it because of different audiences at the compliance level."

Colin then gives the ITAR example from Coherent -- people mixed at a site, can't do site-level restrictions, need to check who is uploading what.

This is substantively valid but tactically poor. Brad just told him to stop, and Colin is explaining why his point is valid. Brad's response is to let it play out and then reassert:

> "But some of this is already built into our system. So that part is already there, but that's what's causing over restriction."

Translation: we know, we have it, it is not the problem we are here to solve today.

**Assessment:** Colin's IAM line of questioning was intellectually sound -- understanding user identity and privilege levels is genuinely relevant to detection accuracy. But Brad had explicitly framed the meeting around two specific business cases and did not want a third introduced. Colin read the room correctly the first time ("I'll keep them short") but lost that discipline on this thread. The ITAR example from Coherent, while credible, came across as Colin advocating for his point rather than receiving Brad's redirect.

### The 20%/ChatGPT Diagnosis: Colin's Biggest Hit

The best moment for Colin in the entire meeting comes when Mikhail reveals the results of their prior ML efforts:

> **Mikhail:** "We were hitting the rate of false positives of around 20% per ticket."

Colin's response:

> "I'll be honest, when I heard 20%... or 80% success rate, that's pretty much out-of-the-box ChatGPT. So probably, to be honest, the fine-tuning didn't do anything. It's equivalent to what you would get out-of-the-box with an untuned model at all."

Mikhail's reaction confirms this landed:

> "The fine-tuning actually went from 20% to 17% today, exactly. And that's why we paused it."

This is a moment of genuine alignment. Colin has just diagnosed their problem in one sentence -- the fine-tuning they invested in barely moved the needle from what a raw, untuned model would produce. Mikhail does not just confirm it; he adds the specific number (17%) and explains that this is precisely why they stopped. Colin's credibility jumps in this moment because he has demonstrated that he understands what happened technically without needing to see the implementation. He read the symptom (20% false positive rate) and correctly identified the disease (fine-tuning was not effectively specializing the model).

**Dynamic note:** Brad's silence during this exchange is significant. He does not jump in to contextualize or redirect. He lets the moment stand. This is Brad acknowledging that Colin has said something genuinely useful.

### The Unified Control Plane Concept: A Strong Close

Colin's other major contribution is the "unified control plane" concept:

> "There has to be commonality between these applications. The good thing with that is about 95% of a redaction application is identical. The only thing that really changes is maybe some strategy for ingestion, maybe the end use case is a little bit different, but the actual architecture fundamentally is relatively the same."

And:

> "You don't want to keep things so fragmented because you're going to end up trying to play whack-a-mole with this. I say that from experience."

Then the critical framing:

> "Even if information comes out, you shouldn't have to redact anything if this part actually worked. It's not possible. It can't create that from nothing. So it can make stuff up. That's a different topic altogether. But making sure that entry point is very robust, that is where the biggest bang for your buck is going to be here for sure."

This resonates because it aligns with what Mikhail has been presenting -- the distinction between detection at entry and redaction on output. Colin is reframing Mikhail's two business cases as two expressions of the same underlying architectural problem (lack of a unified control plane), which is exactly the kind of synthesis Brad wanted the BayOne team to demonstrate.

Brad's response is measured but positive: he does not push back on this framing.

---

## 6. Pat's Contributions: Targeted and Efficient

### Ingestion Questions

Pat asks the critical question about how data enters the system:

> "Doing it on ingestion, that's what I want to ask the question about, too. Because how do things actually get into the system? So I heard databases on one. Are users also uploading documents? Is this connected like an Oracle back-end for things like that?"

This is a precise, well-targeted question that draws out important information from Mikhail about the diversity of ingestion paths (procedures, Teams meeting transcripts auto-attached to tickets, user-entered problem statements, etc.).

### Ecosystem Knowledge

Pat demonstrates relevant ecosystem awareness:

> "It makes sense, and that's a good thing. It's common. It happens. Gen AI is so exciting. People love to do this. A lot of things spring up over years, even months."

And on redaction:

> "Redaction on the output tends to be, like you said, very heavy. Because first, you kind of have more of a classification problem first before you have an identification problem."

Pat is doing exactly what Brad asked for -- demonstrating understanding and contextualizing what Mikhail is describing within broader industry patterns. Pat's contributions are less frequent than Colin's but consistently on-target and never corrected.

### Pat's Role Relative to Colin

Pat functions as the quieter, steadier presence alongside Colin's higher-energy, higher-risk approach. When Colin gets redirected on IAM, Pat does not pile on or try to rescue. When Colin lands the 20%/ChatGPT diagnosis, Pat does not try to claim credit or add to it. Pat operates independently and seems aware of when to speak and when to let the room settle.

---

## 7. Brad's Room Management: Key Techniques

### Technique 1: The Time Check

When Colin is deep into the IAM discussion and the conversation is drifting, it is actually Mikhail who surfaces the time pressure, but on Brad's behalf:

> "So can I just add something just for time?"

This is a soft interrupt that resets the conversation. Brad does not have to be the one to say "we're running out of time" because Mikhail handles it.

### Technique 2: The Explicit Redirect

Brad's most direct intervention is the "Is that clear, Colin?" moment discussed above. He also uses phrases like:

> "I just want to caution against that."

And:

> "I don't think that's like, that is a separate use case. That's a third case."

Brad does not let the BayOne team introduce scope he has not defined. He catches it immediately and names it explicitly.

### Technique 3: The Positive Reframe with Boundaries

When wrapping up and responding to Colin's unified control plane concept, Brad says:

> "We are open to any and all approaches by also understanding what are the trade offs and what are the outcomes that we can expect."

This is Brad acknowledging good input while reasserting his terms: show me trade-offs and outcomes, not just concepts. He follows with:

> "We're not expecting to be revolutionary and right out of it. Evolutionary is absolutely fine."

This is managing expectations in both directions -- signaling to BayOne that they should not overpromise, and signaling internally that incremental progress is acceptable.

### Technique 4: Managing the Follow-Up

Brad ends by establishing that this was a deliberately narrow meeting:

> "We just wanted to make sure we had focus on the problem, the kind of challenging, kind of so forth. So we had clarity around that. And then, yeah, in the follow up, we would have others here."

He is telling BayOne: this meeting was a test. If you pass, you get access to the broader team. The follow-up will include "a broader set of folks" including Daniel's technical team. But that access is gated on today's performance.

---

## 8. Key Tension and Alignment Moments (Chronological)

### Moment 1: Brad's Opening Rules (Tension - Preemptive)
**Signal:** Brad establishing "we've heard it before" before anyone has pitched anything. This is tension born from prior vendor experiences, directed at BayOne preemptively. It says: I assume you will do what every other vendor has done, and I am telling you not to.

### Moment 2: Colin's First Questions (Alignment - Mild)
**Signal:** Colin asks about unified knowledge layer and governance. These are on-target. Mikhail engages substantively. No correction from Brad. The room is in alignment.

### Moment 3: Mikhail's "Not Just LLMs" Clarification (Alignment - Important)
**Signal:** Mikhail says: "One thing I don't want us to limit is to just LLMs and generative AI." And: "We actually have not used generative AI to prove any use cases, not because of unstructured data, but because of unstructured output." This is Mikhail signaling technical sophistication -- he distinguishes between ML and generative AI, and explains why they chose ML (deterministic output) over LLMs (stochastic output). This is a test of whether BayOne hears the distinction.

### Moment 4: The IAM Tangent (Tension - Explicit)
**Signal:** Colin pushes into IAM territory. Brad and Mikhail redirect. "Is that clear, Colin?" is the most pointed moment in the meeting. Colin continues to justify. Brad lets it play out, then reasserts boundaries.

### Moment 5: The 20%/ChatGPT Diagnosis (Alignment - Strong)
**Signal:** Colin correctly diagnoses the failure mode of their prior ML efforts. Mikhail confirms with specifics (20% to 17%). Brad is silent, letting the moment land. This is the moment BayOne earns the most credibility.

### Moment 6: The Unified Control Plane (Alignment - Strong)
**Signal:** Colin synthesizes the two business cases into an architectural framing. No pushback from Brad or Mikhail. This concept resonates because it offers a perspective they have not heard before.

### Moment 7: Brad's "AI Is a Meaningless Word" (Tension - Philosophical)
**Signal:** Brad says: "I know AI is a very sexy word, but it's also a meaningless word, and not married to any specific AI technologies." This is Brad testing whether BayOne will chase the AI buzzword or actually engage with the problem. It is also Brad establishing that he is not impressed by AI branding.

### Moment 8: Brad on the Follow-Up Structure (Alignment - Gating)
**Signal:** Brad tells BayOne that the next meeting will include more people -- but only if this one goes well. The fact that he is describing the follow-up at all suggests BayOne has passed the test sufficiently to earn it.

---

## 9. Unspoken Signals and Structural Observations

### Brad Never Pitches Himself
Brad does not describe his accomplishments, his team's history, or his credentials. He lets his control of the room speak. This is a senior leader who does not need to establish credibility through words.

### Mikhail Defers to Brad on Business Decisions
On every business-level question (priorities, appetite for change, what is in scope, what is not), Mikhail either defers to Brad or confirms what Brad has already said. On technical and product details, Mikhail leads. The division is clean and practiced.

### Colin's Coherent References
Colin references Coherent at least three times (the intro, the ITAR example, the China IP management). This is his primary credibility asset and he uses it heavily. The risk is that too many references to past experience can start to feel like the consultant is talking about themselves rather than the client.

### The "Daniel" Reveal
Late in the meeting, the team structure becomes clearer. Brad reveals that Daniel is the technical lead and that in a future engagement, "it's not going to be like Capgemini working because that was a pilot." This is the most explicit reference to the prior vendor experience (Capgemini). The fact that Brad names it directly and calls it a "pilot" and "not a standard mode of operation" suggests that the Capgemini engagement was suboptimal from Brad's perspective -- either too disconnected from Brad's team or structured in a way that did not work.

### Brad's Final Gating Statement
Brad's last substantive statement is about the engagement model:

> "Initially for this it's all... I want to be really clear like, if we decide to go there, it's not going to be me writing user stories and requirements. I'm going to have somebody as part of my team. Your team is going to be working with -- it's not going to be like Capgemini working, because that was a pilot. That was the only reason. That's not a standard mode of operation."

This is Brad establishing what a real engagement would look like (embedded, working with his team, not operating as an isolated external unit). The Capgemini comparison is the clearest expression of vendor scar tissue in the transcript -- Brad is saying "that is what bad looks like; do not repeat it."

---

## 10. BayOne Team Performance Assessment

### Colin Moore
| Category | Assessment |
|---|---|
| **Domain credibility** | Strong. The Coherent background, semiconductor industry knowledge, and ITAR/CMMC/DFARs experience are directly relevant and clearly genuine. |
| **Technical diagnosis** | Excellent in moments. The 20%/ChatGPT insight was the single most valuable BayOne contribution. The unified control plane concept was strong synthesis. |
| **Listening discipline** | Inconsistent. Opened well ("I'll keep them short"), lost discipline on the IAM tangent, received the redirect but pushed back before accepting it. |
| **Verbosity** | Above optimal. Introduction was longer than necessary. The IAM thread ran longer than the room wanted. Multiple contributions could have been 40% shorter. |
| **Reading the room** | Mixed. Correctly identified the 20% false positive as a diagnostic opportunity. Did not correctly read Brad's desire to limit scope on the IAM discussion. |
| **Overall** | Net positive. The hits were genuine and memorable. The misses were correctable and did not damage credibility permanently. Brad's "Is that clear?" was a warning, not a dismissal. |

### Pat
| Category | Assessment |
|---|---|
| **Questioning** | Precise and targeted. Ingestion question drew out critical information. Ecosystem observations were on-point. |
| **Discipline** | High. Spoke less frequently but every contribution was relevant and well-timed. |
| **Technical framing** | Strong. "Classification problem before identification problem" showed genuine understanding of the ML pipeline. |
| **Room awareness** | Excellent. Never overextended, never corrected, never redirected. |
| **Overall** | Quiet strength. Did not dominate but added real value at every intervention point. |

---

## 11. Power Structure Summary

```
Brad (Director level, owns everything)
  |
  |--- Room controller, business decision-maker, gatekeeper for next steps
  |--- Sets scope, redirects when scope is violated
  |--- Carries vendor scar tissue from Capgemini and possibly others
  |--- Tests BayOne with "we've heard it before" framing
  |
  +-- Mikhail (Head of Product, reports to Brad)
        |
        |--- Technical translator, whiteboard driver
        |--- Presents the structured problem framework
        |--- Honest about knowledge limits ("I don't know what that even means")
        |--- Defers to Brad on business decisions, leads on product/technical details
        |
        +-- Daniel (Technical lead, referenced but not present)
              |--- Will be involved in follow-up if engagement proceeds
              |--- Brad's signal: "it's not going to be me writing user stories"
```

**BayOne side:**
- Colin leads, carries the domain credibility, takes the most risk, gets the most reward and the most correction
- Pat supports, asks precise questions, provides ecosystem context, never corrected

**Key dynamic:** Brad and Mikhail function as a single decision-making unit with complementary roles. Colin needs to understand that both of them need to be satisfied -- Brad on discipline and approach, Mikhail on technical credibility and product fit. The 20%/ChatGPT moment satisfied Mikhail; the unified control plane concept satisfied both. The IAM tangent concerned Brad. The net outcome: BayOne earned the follow-up meeting, but Brad is watching.
