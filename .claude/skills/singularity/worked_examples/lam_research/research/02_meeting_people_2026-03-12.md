# 02 - Meeting: People

**Source:** `source/lam_meeting_3122026.txt`
**Source Date:** 2026-03-12 (Discovery Call)
**Document Set:** 02 (Meeting Transcript)

---

## People Present on the Call

### Lam Research

**Bradley Estes ("Brad")** - Managing Director, Knowledge & Advanced Services
- Opened the call, set the agenda and ground rules
- Explicitly stated: "We don't want to have the discussion right now about, oh, I've got a technology solution that can solve that. We want a very clear understanding in what we're trying to solve."
- Owns the entire vertical: business case, product definition, ideation, execution. Has everything from business, program, product, to technical in his organization.
- Explicitly stated he would NOT be writing user stories or requirements himself if engagement proceeds - he has team members for that. Previous "pod" work was a pilot and not the standard mode of operation.
- Confirmed a follow-up meeting would bring in a broader set of folks (including Daniel and others).
- **Sentiment:** Controlled, deliberate, structured thinker. Kept the meeting focused when it drifted. Pushed back diplomatically when Colin's questions veered toward access management (a "third use case" Brad didn't want to introduce). Clearly the authority figure - Mikhail defers to him. Not interested in being sold to. Wants demonstrated understanding before solutions. Has been burned before ("we've heard it before").

**Mikhail Krivenko** - Head of Product in Brad's organization
- Led the whiteboard-style technical presentation of the two use cases
- Handles product management, IT design, and product order - both ideation and execution
- Technically informed but self-described as "not a technical audience" for deep infrastructure questions
- Could name the ML models tried (Transformers, SpaCy, Azure AI model) and describe results
- Corrected/redirected when discussion drifted from his two use cases
- Mentioned "Christian" as owning a specific slide he was looking for
- **Sentiment:** Pragmatic, detail-oriented, good communicator. Comfortable saying "I don't know what that means" when asked about Azure Foundry specifics. Very clear on distinguishing detection vs. redaction and why they're separate business cases. Focused on outcomes, not technology names.

**"Pat" / Pratik (likely Pratik Sharda from BayOne, but spoke as if on-site at Lam)**
- Referenced multiple times, asked to join and put laptop at screen
- Asked questions about identity/access management, data ingestion approaches
- Mentioned patterns seen "in the ecosystem" - positioned as having broader industry context
- **Note:** The transcript attribution is ambiguous. "Pat" may be Pratik Sharda from BayOne or a Lam employee. The conversational context (being asked to "join" and "put your laptop at the screen") suggests someone physically present but calling in.

**Christian** (mentioned, not present)
- Owns a specific slide/document that Mikhail was looking for at the start
- Part of the broader team

**Daniel** (mentioned, not present)
- Technical lead. Brad confirmed Daniel is on the same team working on this.
- "Daniel, program. Me [Mikhail], product."
- Will be brought into the follow-up meeting
- Brad described the org structure as: Daniel = technical, Mikhail = product, together they form scrum teams

**Monica** (mentioned briefly)
- Referenced by Brad: "you only met three people, but you know, Monica was blessed"
- Part of the broader team but not on this call

### BayOne Solutions

**Colin Moore** - Director of AI (referred to as "head of AI" in his own intro)
- Gave the opening intro covering Coherent Corp background, AI CoE, ITAR/CMMC/DFARS experience, China IP management
- Asked the technical probing questions: infrastructure stack, Azure Purview, AI Foundry, what's been tried
- Pushed the "unified control plane" concept for ingestion
- Made the point about 20% false positive being equivalent to out-of-the-box ChatGPT (fine-tuning didn't help)
- **Sentiment:** Engaged, technically sharp, but had to be redirected once by Mikhail when veering into access management territory. Brad and Mikhail kept him scoped. Good instincts on where the real problem is (ingestion > output).

**Pratik / "Pat"** - (See note above - may be the person referred to as Pat in transcript)
- Asked about ingestion, identity management, long-term scaling approaches

**Additional BayOne attendees** - Not clearly identified in transcript. Amit, Surej may have been present but did not speak or were not attributed.

## Key Relationship Dynamics Observed

1. **Brad controls the room.** He set the agenda, redirected when needed, and explicitly said "I want to make sure we're not introducing noise in our business case." Mikhail defers to him but is empowered to lead the technical presentation.

2. **Brad has been burned before.** Multiple signals: "we've heard it before," insistence on understanding before solutions, explicit statement that they want BayOne to "repeat back" the problem before proposing approaches. This is not a first rodeo.

3. **The org is self-contained.** Brad owns business, product, program, and technical. This is unusual and powerful - no cross-org politics to navigate for the initial engagement. The complexity comes later when branching to systems they don't own.

4. **Previous vendor friction.** Brad referenced "what we did last year" and "the pod working" as a pilot that was not standard. There was a prior engagement (possibly with BayOne or another vendor) that was structured differently. Brad is explicitly setting expectations that the next engagement will be more structured with his team doing the requirements work.

5. **Daniel is the gatekeeper to technical depth.** Brad and Mikhail handle the business/product framing. Technical deep dives require Daniel, who will be at the follow-up meeting.
