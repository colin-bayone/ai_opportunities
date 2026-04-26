# 09 - Meeting: Architectural Debt Observations

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on architectural debt observed during the mapping work

---

## Strategic Framing: A Distinct Value Lever

This document captures a category of findings that is qualitatively different from the gap analysis covered elsewhere in the research set. The two are easy to conflate, so the distinction matters and is the foundation of this entire document:

- **Gap analysis** answers the question: *what is missing from EMS that exists in EPNM?* It is an inventory of absences. It is what Cisco needs in order to reach feature parity. Forty-two backend gaps. UI gaps in both directions. Data source gaps. These are deliverables Cisco has explicitly asked for and that Selva confirmed will be taken to product management as the basis for customer commitments ("we got this covered, you can go promise the customers that they will get this functionality").
- **Architectural debt observations** answer a different question: *what is present in EMS but inconsistent, duplicative, or poorly structured?* It is an inventory of code-base patterns that already exist on the EMS side but were carried over from EPNM in a way that introduces or perpetuates inconsistency. It is not what Cisco *needs* — Cisco already has it running. It is what Cisco *could improve* while the conversion work is happening anyway, with marginal additional cost because the team is already in the code.

The gap analysis is a parity narrative. The architectural debt is a quality narrative. They produce two different scope-expansion conversations with two different stakeholder audiences. The gap conversation is with product management. The debt conversation is with engineering leadership.

This separation is the strategic point of this document. Conflating them weakens both stories.

---

## How Colin Discovered It: Observation, Not Hunting

A critical context note for how this finding should be framed in subsequent conversations: Colin did not set out to do an architectural review. He set out to do a UI conversion POC. The architectural debt was discovered as a byproduct of doing the mapping work end to end and being deep in the code himself.

From the transcript, the mapping was thorough enough that it produced incidental visibility:

- "We actually did a comprehensive mapping of the entire EPNM and EMS systems. So all 14 repositories between the two, we have the full absolute analysis of gaps that we found in the UI components and in the backend."
- "I felt good to kind of get to know the code base a little bit more myself."
- "I maxed out on the Cisco codec subscription pretty much every day this week."

When you read 14 repositories closely enough to map every UI component, every backend feature, every data element, and every correlation across the two systems, you cannot help but notice when the same problem is solved two different ways in two different places. The debt observations fell out of the mapping work. They were not the goal of it.

This matters for positioning. Colin is not pitching an architectural audit as a separate engagement. He is reporting findings he already has, that are already documented, that came out of work he was already doing. The credibility of the observations rests on the fact that he was not looking for them — he just had to wade through enough of the code base to see them.

This is also why the team was not involved in fixing them. The discovery and the decision to fix were never going to happen in the same engagement under POC scope. Colin saw the patterns, noted them, and held off.

---

## The Pattern: "Different Ways To Do The Same Thing"

The core observation Colin made in his own words:

> "I didn't want to bring this up for the POC, but I have it ready, even along like some architectural decisions, because there's even some, you know, we could see whatever things were getting ported over to EMS. There's some debt that it's carried over too. There's different ways to do the same thing."

The phrase that does the work here is **"different ways to do the same thing."** This is not a statement that EMS is missing something. It is a statement that EMS has the same thing implemented inconsistently — that the same conceptual operation is solved by two or more different code patterns in different places in the code base.

This is the textbook definition of architectural debt. Not bugs. Not missing features. Not performance problems. Just inconsistency in how a recurring problem is solved, which compounds over time as new code is written against whichever pattern the developer happened to find first.

Colin also made an important attribution point: this debt was not introduced by EMS. It was **"carried over"** from EPNM. EMS inherited the inconsistency from the legacy system. The act of porting did not introduce the debt; it propagated it. This framing is important because it positions the conversion engagement as the *natural moment* to address the debt — you are already touching every screen, the patterns are already on screen in front of the engineers, and the conversion forces a decision about how to implement the EMS equivalent. If you are going to make that decision anyway, you might as well make the consistent choice.

Stated as a principle: **a like-for-like port preserves debt. A thoughtful port has the option to retire it.** The POC was a like-for-like port by design. The full engagement does not have to be.

---

## Concrete Example One: Column Handling In Tables

Colin's first concrete example, given in the meeting:

> "For instance, even just looking at the way columns are handled in a table, something that's simple. We can even fix that along the way."

What Colin is describing — based on the framing as "simple" and as a recurring UI pattern — is that across the EMS code base, tables do not handle columns the same way from screen to screen. Different screens implement column rendering, sorting, sizing, visibility, persistence, or some subset of those concerns differently. The same UI primitive is solved by multiple component patterns.

Why this is the perfect example to lead with:

- **It is simple.** Tables are a foundational UI element. Every operations tool has them. The audience does not need a deep architectural background to understand the problem.
- **It is high-volume.** Tables appear on essentially every screen of a fault management or inventory system. The cost of inconsistency multiplies by the number of tables.
- **It is high-leverage to fix.** A consistent table component can be adopted incrementally and reduces the per-screen development time for the rest of the conversion.
- **It is observable from the outside.** End users feel inconsistent table behavior. Engineering teams feel inconsistent table code. So the fix has both a UX story and a code-quality story.

Colin chose this example deliberately. He did not lead with a deep backend pattern that would require half the call to set up. He led with the simplest possible example that anyone in the meeting could nod along to. That is a pattern worth preserving in subsequent positioning.

The example also implicitly carries the scope-expansion narrative: if column handling is inconsistent, what else is inconsistent? Modal dialogs? Form validation? Navigation patterns? Data loading states? Error messages? Colin did not enumerate these on the call, but the column example invites the question. The 250-file documentation set on GitHub presumably has more.

---

## Concrete Example Two: Bookmarks (Deferred-Decision Pattern)

The second example Colin gave is structurally different from the columns example. It illustrates a different kind of architectural decision — one Colin actively chose *not* to fix:

> "Bookmarks. something that simple, a different concept in EPNM than it is in EMS. So what we did there is we said, we'll leave it alone for now, we'll leave it be. We'll port it exactly as it is in EMS. And if that is a gap, that's something that is more global scope that would impact pretty much every screen in EMS. So it's not possible to just do it within the scope of fault management inventory. But we have all that noted. That's what was in that big dock that I shared with the team, just so they could get some eyes on what our constraints were with that."

Several things are worth pulling out from this passage:

**It is a conceptual mismatch, not an implementation inconsistency.** Unlike the columns example, where EMS has multiple ways to do the same thing, bookmarks are a case where EPNM and EMS treat the underlying *concept* differently. The behavior of a bookmark in EPNM is not the same behavior as a bookmark in EMS. So there is no clean conversion mapping; there is a decision about which concept wins.

**It is global, not local.** Bookmarks affect every screen, not just fault management inventory. So even if the POC team wanted to fix it, they could not — the fix would necessarily touch screens that are not in the POC scope. The conversion of fault management inventory cannot unilaterally redefine bookmarks for the whole product.

**Colin's chosen path: port exactly, document the constraint.** The POC does not try to solve the bookmarks question. It ports the EMS implementation as-is. The mismatch with EPNM behavior is recorded as a gap (or constraint) and surfaced to the team for a global decision later.

**This is a deferred-decision pattern, not a duck.** Colin is not avoiding the problem. He is documenting it, scoping it correctly (global, not local), and explicitly handing the decision to a stakeholder who has the authority and breadth to make it. This is the disciplined version of "we noticed this but did not fix it."

The bookmarks example is the answer to the question Cisco might ask — "well, why didn't you just fix the debt as you went?" — for things that genuinely cannot be fixed inside POC scope. Some debt is local and could be cleaned up screen-by-screen as conversion happens. Other debt is structural and requires a product-level decision. Colin demonstrated the discipline to tell the difference.

---

## Colin's Discipline: The Decision Not To Touch

The defining behavior captured in this transcript is what Colin chose *not* to do:

> "I didn't want to make that decision on a POC without the team involved, but with the team getting involved with us, that's a really easy way. We can make that go a lot quicker than not."

Colin had the technical capability to fix the column-handling inconsistency during the POC. He had access to the code, he had the agentic workflow running, and he had already converted the screens. He could have, while he was at it, normalized the column pattern across the screens he touched.

He did not. The reason is explicit: **architectural decisions belong to the team that owns the system.** A POC is a proof of capability, not a license to make permanent decisions about how Cisco's code base should be structured. Even if the change would clearly be an improvement, the choice of pattern, the rollout plan, the impact on other teams, and the regression risk are all things the EMS engineering team needs to weigh in on.

This is the kind of restraint that makes the observation credible. If Colin had silently made architectural changes during the POC, two things would happen, both bad:

1. The team would discover the changes during code review and lose trust that the POC actually represents what they think it represents.
2. Any future architectural conversation would have an immediate counter-argument: "you already changed things you shouldn't have."

By holding off, Colin gets to bring the debt observations to the team as findings, not as fait-accompli changes. The team can engage with them on their merits. The conversation is collaborative, not defensive.

The transcript also shows Colin reinforcing this discipline in another part of the conversation, on the broader principle of touching as little as possible:

> "We actually tried as much as we could not to touch anything on the EMS side. Pretty much like a bolt-on seamless thing for you."

The conversion-as-toggle approach (Angular packages running in parallel, JavaScript switch on the front end, no backend changes) is the same discipline at a different scale: prove the capability, change as little as possible, surface what you saw but did not change.

---

## The Future-Engagement Implication: Acceleration, Not Delay

The pivot in Colin's framing is important. He does not present the architectural debt as a complication, a risk, or extra scope that will slow things down. He presents it as an **accelerator**:

> "...with the team getting involved with us, that's a really easy way. We can make that go a lot quicker than not. So we can definitely accelerate the timeline even further with that in mind."

This is a deliberate inversion of the more common consulting frame. The default frame would be: "we found additional issues, here's the change order, here's the timeline extension." Colin's frame is: "we found additional issues, *and* fixing them while we are already doing the conversion is faster than the alternatives, so the scope expansion comes with a timeline acceleration."

The mechanism for the acceleration is the team-involvement piece. With the EMS engineering team in the loop, decisions about which pattern to standardize on can be made in real time as the conversion progresses. Without the team, the BayOne side has to either ask permission for every architectural choice (slow) or port debt as-is and create rework later (slower). With the team, the debt cleanup happens inline and the converted code base ends up cleaner than the source code base.

This framing has a second-order effect that is worth naming: it changes the nature of the engagement Cisco is contracting for. The POC is a UI conversion engagement. The full engagement, with debt cleanup folded in, is a *modernization* engagement. The deliverable is no longer "EMS with a new UI." It is "EMS with a new UI and a cleaner code base than it had before." That is a meaningfully different value proposition and a meaningfully different conversation with engineering leadership.

The narrative arc Colin is setting up:

- POC: prove the conversion capability without touching anything.
- Full conversion: convert all the screens, port debt as-is, deliver parity.
- Full conversion with debt cleanup (the upsell): convert all the screens, fix the inconsistencies as you go, deliver parity *and* improvement, faster than the alternatives because the team is already in the code.

The third option is the one Colin is positioning for. The transcript is the foundation of that positioning.

---

## The Documentation Discipline

A practical detail from the transcript that supports the credibility of the architectural debt findings: **everything is written down.**

> "But we have all that noted. That's what was in that big dock that I shared with the team, just so they could get some eyes on what our constraints were with that."

> "Any of the decisions that we had to make along the way, those are also documented with the rational justification. So that's my human in the loop part, if you will. Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly."

Two distinct artifacts are referenced:

1. **The big document** ("big doc") shared with the Cisco team. This document captures constraints encountered during the POC — specifically including cases like bookmarks where Colin chose not to fix the issue and wants the team to see what the constraint was and why.
2. **The commit-level rationales** on the GitHub branch. Colin attached his own (human-authored, not generated) reasoning to the commits where decisions had to be made. This means a code reviewer can see not just *what* was changed but *why* the change was made the way it was.

The agentic generation produced ~250 files of mapping output. Those are mostly machine-readable inputs to the next phase. But the architectural decisions, the constraints, and the deferred-decision rationales are explicitly human-authored. Colin called this out as his "human in the loop part." That distinction matters: the architectural debt observations are not LLM-generated commentary on the code base. They are Colin's own assessments, written in his own words, supported by the agentic mapping evidence.

When Cisco's team reviews the work, they will see:

- Mapping evidence (machine-generated, voluminous, supports the claims)
- Decision rationales on commits (human-authored, attached to the actual code changes)
- The big document (human-authored, summarizes constraints and deferred decisions)

This documentation pattern is what makes the architectural debt findings reusable in subsequent conversations. They are not a verbal observation from one meeting. They are written, commit-attached, and team-visible. Anyone who joins the conversation later — engineering leads, product managers, architects — can read the same source material and form their own view.

---

## Why This Is A Separate Scope-Expansion Narrative

To close the loop on the strategic framing at the top of this document: the architectural debt observations support a scope expansion that is structurally different from the gap analysis scope expansion.

**Gap analysis scope expansion** looks like this: "We found 42 backend gaps and additional UI gaps. To deliver parity with EPNM, the engagement needs to address these. Here is the scope and the timeline." The audience is product management. The decision criterion is customer commitments. The risk of saying no is that customers don't get features.

**Architectural debt scope expansion** looks like this: "While doing the conversion, we observed inconsistencies in the EMS code base that were carried over from EPNM. These can be addressed inline with the conversion work, with team involvement, faster than they could be addressed as a standalone cleanup. Here is the additional scope to fold in debt cleanup." The audience is engineering leadership. The decision criterion is long-term code-base health and team velocity. The risk of saying no is that the new EMS code base is no cleaner than the old EPNM code base, and the next engineer to touch it inherits the same problems.

These two narratives can be pursued independently. They can also be pursued together — the same engagement could deliver both gap closure and debt cleanup. But they are separate value levers, with separate stakeholders, separate decision criteria, and separate failure modes if ignored.

The strategic value of having both narratives well-developed is optionality. Depending on how the next conversation goes — what Cisco's priorities are, who is in the room, what budget is available — either narrative can be foregrounded. The gap analysis is the safer, more obvious sell. The architectural debt is the more sophisticated sell that demonstrates BayOne's ability to operate at the engineering-leadership altitude rather than just the feature-parity altitude.

Both belong in the post-demo conversation. This document is the foundation for the second one.
