# 09 - Meeting: POC Status and Toggle Implementation

**Source:** /cisco/epnm_ems/source/guhan_selva-4-24-2026.txt
**Source Date:** 2026-04-24 (POC progress check-in with Guhan and Selva)
**Document Set:** 09 (Status check-in meeting)
**Pass:** Focused deep dive on POC conversion status and toggle implementation

---

## Headline Status

Colin opened the technical update with an unequivocal completion statement on the conversion work itself, framed against an ongoing solo sprint:

> "I just wanted to connect with both of you. I meant to do this earlier in the week, but I've been busy doing exactly what we're talking about here. So we've kind of been doing this solo, kind of to prove it out again the concept, but good news is we are right at the tail end of this. So we ended up doing a little bit more than we had originally anticipated."

The plain summary, in his words: **"conversion is ready, conversion is done. We are just doing our final tests."**

The only remaining gating item is Cisco-side access to the EPNM and EMS virtual machines so that BayOne can run a comparative validation against live reference systems before demo. Colin framed this as a self-imposed quality gate, not a Cisco-driven blocker:

> "The access item, the only one that I think you probably saw in the chat, what we're waiting on right now and what we'll talk about on Monday is the virtual machines that have the EPNM and EMS applications running. So we can do that comparative analysis on our end. That way we don't frankly embarrass ourselves before we come to you. If something's definitely missing or if something is not as expected, that'll let us actually test this out properly."

The agent workflow side of the test infrastructure is already in place:

> "We've got our agent workflow already good to go. So as soon as the team gives us access to the systems, we'll be in good shape so we can run our comparative test to make sure what we build with the toggle is exactly the same functionality on EPNM."

Later in the call Colin specified the test toolchain:

> "We have our whole agent[ic] test suite with Playwright that can do that, so that'll be quick whenever we get that access."

Selva and Guhan confirmed the access provisioning is targeted for Monday, with a likely demo slot of Wednesday — possibly slipping to Thursday once the code review with the India team is also factored in.

---

## What Has Been Built — Per-Screen Scope

The POC scope is narrow and consistent with prior planning: **inventory** and **fault management**. Colin described the runtime experience in concrete terms:

> "So whenever you get to the inventory or the fault management screens, there's now just a toggle at the top and you switch back and forth. That's it."

Everything outside those two screens is deliberately untouched in this POC. Colin's language for that boundary:

> "We kept everything exactly as it is in EMS. So we weren't trying to reinvent the wheel too much in the POC. We noted anything that were the caveats to it."

So the POC delivers two converted screens, a toggle at the top of each, and a documented set of caveats — not a comprehensive parallel UI.

---

## How the Toggle Works

Selva pressed for confirmation on the architecture of the toggle, specifically on backend behavior. The exchange is the cleanest statement of the design in the transcript:

> **Selva:** "So one thing, the POC, you have the classic view and then you have the current way to do the UI, right? So you switch back and forth."
> **Colin:** "Yes."
> **Selva:** "And then when you do that, it will still talk to the same backend. We're not spawning different backends, right?"
> **Colin:** "Absolutely. Absolutely. Identically the same. Yes."

Colin then described the implementation mechanics:

> "Yes, so in the system, the way that we have it right now, it's just a simple UI toggle. So that's really it... So whenever we deploy, that's all that happens. So whenever you get to the inventory or the fault management screens, there's now just a toggle at the top and you switch back and forth."

And the deployment-model description, which is the load-bearing technical claim of the entire POC design:

> "So simply just the JavaScript, and then all that happens is that we convert over to the new front end. So the back end never changes, of course, but it's just a different page that shows on the front end. So we kept all the Angular there. So it's just a bunch of packages in parallel. We actually tried as much as we could not to touch anything on the EMS side. Pretty much like a bolt-on seamless thing for you."

Key design points to extract from that:

- **Pure UI-layer change.** The toggle is a JavaScript switch; the backend is identical between modes — same APIs, same data, same services.
- **Angular preserved.** The existing EMS Angular stack is left in place. The classic UI is not a replacement of EMS; it is a sibling.
- **Parallel packages.** The classic UI ships as additional packages installed alongside the existing EMS packages. No rip-and-replace.
- **"Bolt-on seamless"** is the explicit phrase Colin used to characterize the integration footprint into EMS — minimally invasive, additive only.
- **No EMS-side changes attempted.** Colin emphasized "we actually tried as much as we could not to touch anything on the EMS side." The POC's correctness depends on this — it's why the toggle hits the same backend and why the comparison test is meaningful.

Guhan's response — "Super, super" — registered approval of this model.

---

## Where the Code Lives

Colin laid out the source-control layout in straightforward terms:

> "All the code will be live on your GitHub. So I put everything, I believe, on the same... For each repository, there's a branch that is called a[n] [a]gentic UI conversion. So it's based on the develop branch for all of these, which is what Akhil told us in the chat. So we can rebase if we want to."

Decoded from transcription artifacts, this means:

- **Repository home:** Cisco's GitHub. Code is on Cisco's side, not held in a BayOne repo.
- **Branch name:** `agentic UI conversion` (transcript renders "Gentec UI conversion" — the agentic-workflow framing throughout the rest of the meeting confirms the intended name).
- **Branch base:** `develop` on each affected repository. This base was confirmed via Akhil in the team chat.
- **Multi-repo:** the same branch name is created on each repository touched by the conversion. Across the comprehensive mapping Colin described, **14 total repositories** were identified between EPNM and EMS, though not all are necessarily touched by the POC's per-screen scope.
- **Rebaseable:** Colin offered to rebase against `develop` on Cisco's request — meaning the work is intended to integrate cleanly back into Cisco's development flow, not sit as a fork.

---

## Auditability Architecture

Colin called out two specific affordances he built into the POC deliberately to make it reviewable by Cisco's team rather than just demonstrable. These were not requested up front; he architected them in:

**1. Commits attributed by individual.**

> "And just so you know, so we can make the demo. I mean, of course they can see everything. I actually put them in the commits that we did on the branch. I put them so specifically they could be audited by the team already. So that should make life a little bit easier."

The "them" here refers to the Cisco team members — Colin attributed commits to the relevant team members on the branch so that Cisco's own auditing and code-review processes could trace authorship in a way that maps to their organization.

**2. In-line decision rationale, human-authored.**

> "And any of the decisions that we had to make along the way, those are also documented with the rational[e] justification. So that's my human in the loop part, if you will. Any of those kind of decisions are rationales I put in myself. So those are not generated, those come from me directly."

This is significant: Colin draws an explicit line between AI-generated artifacts (the bulk of the conversion code and the ~250 mapping files) and human-authored decision rationales. The rationales are deliberately not LLM-generated — they are Colin's own writeups of why a particular choice was made when more than one path was available. This is the "human in the loop" he refers to, present in the audit trail itself.

The combined effect: a Cisco engineer reviewing the branches gets (a) commits that map to their own team for ownership semantics, and (b) the human reasoning for non-obvious decisions inline with the code, sourced from Colin rather than from generation.

---

## The Bookmarks Example — Caveat Handling

Colin used bookmarks as the concrete illustration of how the POC handles features that behave differently in EPNM vs. EMS:

> "I'll give a quick example. Bookmarks. Something that simple, a different concept in EPNM than it is in EMS. So what we did there is we said, we'll leave it alone for now, we'll leave it be. We'll port it exactly as it is in EMS. And if that is a gap, that's something that is more global scope that would impact pretty much every screen in EMS. So it's not possible to just do it within the scope of fault management inventory. But we have all that noted."

Several things to extract from this single example, which is being used as a stand-in for a class of decisions:

- Bookmarks behave differently between EPNM and EMS — at minimum a behavioral or conceptual gap, not just visual.
- The POC does **not** attempt to bridge that gap. The classic UI in the POC carries EMS bookmark behavior, not EPNM bookmark behavior.
- The reason is scope discipline: bookmarks are cross-screen / global. Fixing them properly would require touching screens outside the POC's inventory and fault-management scope, which would explode the surface area beyond what a POC can underwrite.
- The decision is documented as a noted caveat in the comprehensive gap analysis document Colin shared with the team.
- The same pattern likely applies to other globally-scoped UI concerns the conversion encounters.

This is a useful pattern to surface in any later proposal: the POC commits to in-scope screens being functionally faithful to EMS, and explicitly carries forward (without "fixing") any cross-cutting EMS behavior so that the POC doesn't quietly take on global-scope rework.

---

## Side Outcome: Comprehensive 14-Repo Mapping

What was originally test setup turned into a fuller artifact than expected, which Colin flagged as a bonus:

> "We are right now finalizing on the testing for the screens. So conversion is ready, conversion is done. We are just doing our final tests. So what we ended up doing by almost by accident, but it ended up working out, is we actually did a comprehensive mapping of the entire EPNM and EMS systems. So all 14 repositories between the two, we have the full absolute analysis of gaps that we found in the UI components and in the backend."

He went further on the mapping's depth:

> "We know everything in the front end, you know, what the correlation map is between feature A, feature B, or if there is a reverse direction, what that looks like, even down to the data elements there. So we have pretty much the full roadmap done already for the full scope here, which is pretty cool. That happened a lot faster than we thought it would. And that was actually a bigger chunk of the puzzle."

The mapping covers both UI and backend (Guhan asked specifically; Colin confirmed "Both, yes"), and the artifact set is large — Colin estimated approximately 250 files. The files are stored on the GitHub branches alongside the conversion code:

> "We've also kept documented... I haven't been able to share as much with the team because I've been trying to sprint to the finish line here. But at least all of it is on the GitHub repositories for this too. So absolutely everything throughout this entire process for us is there."

The mapping inventory captures: feature-to-feature correlations in both directions; line-of-business metrics like exact volumes of Java, SQL, and XML across the codebases; UI gaps; feature/backend gaps; and data-source gaps. Colin's stated reason for going both directions — EPNM-to-EMS and EMS-to-EPNM — was to surface things that exist in EMS but not EPNM, behavioral differences, and microservice-vs-thick-client architectural deltas.

A specific number Colin called out for the backend gap count: **42 backend gaps**.

> "It's 42. If you want to know the number, 42 gaps for back-end."

This was offered when Guhan asked whether the team would be building back-end pieces against the gap analysis.

Coverage of DPM (the performance management functionality Guhan flagged as customer-critical) was confirmed **not** in the POC scope but **is** in the gap analysis:

> **Guhan:** "...DPM also. It's a key thing, right?... So we will see that is all part of the whatever you have generated or planning to. It's not in the POC, but..."
> **Colin:** "It's not part of the POC, you're right, but that's in the gap."

---

## Initial Data and Self-Sufficiency

Colin also flagged that he avoided pulling on the Cisco team for seed data:

> "I've tried to do as much as I can to not bother the team unless we actually really, really needed something. So even from that, if you're interested, all we did was we took that meeting recording that you shared and basically used the screenshots from that to precede [seed] the database. So we didn't even have to bother the team for that."

The POC's runtime database is seeded from screenshots extracted from a Cisco-shared meeting recording — not from a live data export.

---

## Live VM Offer

Colin offered to host a live instance Cisco-side if it would make playing with the POC easier:

> "If you wanted to make it live on an instance for a VM or something like that on your side, we could certainly do that. That way you can play with it yourself. But for the demo, we can have it pulled up, and maybe the team can tell us exactly what to do."

For the demo itself, the plan is for BayOne to drive — Colin will have EMS pulled up on his end (he confirmed earlier in the call: "we have EMS running on our end right now. I was able to get that pulled up. So we can show that.").

---

## What Is Not Yet Done

Concrete pending items at the time of this meeting (2026-04-24):

- **Final comparative tests** against live EPNM and live EMS — gated by Cisco-side VM access, expected to be provisioned Monday 2026-04-27. Playwright-based agentic test suite is ready to execute as soon as access lands.
- **Code review with the India team.** Guhan asked Colin to coordinate "designated coding" — interpreted from context as the decision-tagged commits / code-review pass — with Akhil's India team before the demo, so questions can be asked and answered while the team is awake. Colin agreed; this may push the demo from Wednesday to Thursday.
- **Demo itself.** Targeted for Wednesday 2026-04-29, possibly slipping to Thursday 2026-04-30 to accommodate the code review window. Time slot must work for East Coast, PST, and India simultaneously — meaning Pacific morning / India evening.
- **Rebase decision.** Colin offered to rebase the `agentic UI conversion` branches if Cisco wants; not yet executed.
- **Live VM-side hosting on Cisco side.** Offered, not yet requested.

What is **not** pending and is genuinely complete per Colin's framing:

- The conversion code itself for inventory and fault management screens.
- The toggle implementation and its wiring to the unchanged EMS backend.
- The comprehensive 14-repo mapping artifact set (~250 files).
- The 42-item backend gap analysis.
- Commit attribution by individual.
- Inline human-authored decision rationale documentation.
- Database seeding via meeting-recording screenshots.

---

## Tone and Confidence Markers

Guhan's framing at the close — "I mean, it's very comprehensive, really anxious and looking forward to the demo" — and his earlier "Super, super" response to the bolt-on description suggest the architectural choices are landing well. Selva's validation question on the shared backend was the only architectural pressure-test in the meeting and resolved cleanly on the first pass.

Colin's own pulse-check exchange near the end is worth preserving as a calibration:

> **Colin:** "Is it good or is it great? Not yet. Not yet. Just trying to pulse check."
> **Guhan:** "It's completely in the direction that we were looking. So that's why you would hear us say, ask like anything that's really surprised us already."

"Completely in the direction we were looking" with no surprises is the directional read going into the demo.
