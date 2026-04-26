# Agent 04: Set 03 Deep Dives Extraction

**Source meeting:** guhan_selva-3-25-2026.txt (Set 03, 2026-03-25)
**Source files read:**
1. 03_meeting_scope_reframe_2026-03-25.md
2. 03_meeting_poc_planning_2026-03-25.md
3. 03_meeting_next_steps_2026-03-25.md

**Deliberately NOT read:** 03_meeting_july_timeline_and_costing_2026-03-25.md (commercial / timeline scope, excluded per assignment)

---

## 1. The Scope Reframe (the central event)

Source: 03_meeting_scope_reframe_2026-03-25.md

### 1.1 Prior understanding that Set 03 overturned

Before this meeting, Sets 01 (2026-02-09) and 02 (2026-02-20) had established that:

- The engagement was a conversion of missing EPNM functionality into EMS.
- Selva had described the missing functionality as "vertical": "If something was not brought in the frontend, the corresponding backend is also not working. The functionality, it doesn't exist. It's kind of doesn't exist like all the way down."
- Selva had also stated: "It's not a UI alone. There is a, along with it comes the backend logic. Only then this is more EMS element management domain."
- The POC was understood to focus on "missing reports" not yet ported to EMS.
- Guhan had framed the challenge as: "Can you take that experiment, provide a working code, show us the demo, taking some of the screens on the backend of the EPNM, run it in the EMS."
- Net effect: a full-stack vertical conversion of roughly 200 screens including UI rewrite (Dojo / JavaScript to Angular) and backend reimplementation in EMS microservices.

### 1.2 How Selva introduced the reframe

Selva prefaced the reframe with an acknowledgement that the earlier meetings had been unclear:

> "I wanted to, what I wanted to clarify is that is one thing, right? So today we have EMS screens and then we have the EPNM which is the old product. What we wanted to — like maybe this didn't come out as clear in the first meeting..."

He then introduced the two analogies that define the new scope.

### 1.3 The Outlook and banking application analogy (Selva)

> "We are looking at, you know, like how in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable. And then I want to switch to the new thing."

The pattern this analogy establishes:
- Product ships a new UX.
- Users receive a toggle to go back to the old experience.
- Over time, users adopt the new experience.
- Eventually the old experience is deprecated.

### 1.4 Guhan's extended banking / Outlook elaboration (personal anecdote)

> "So, a typical thing is your banking applications, right? Like, everyone does it. Those are all cloud applications. So they say, I'm used to doing this transfer here. I'm used to looking at a summary, and even Outlook. I'm used to doing certain things like layout. So when Outlook rolled out, I remember myself doing this. When I upgraded, I said, OK, I'm not going to use the new UI because I have 10 things to handle. I don't have time to handle your new UI thing right now. But gradually, when I got the time, I switched it and then saw, oh, this looks much nicer. And then over time I said this is my default view. That's what we want to do with the users."

Guhan's described adoption curve:
1. Upgrade forces new UI on the user.
2. User resists because they cannot afford the productivity hit.
3. User toggles back to the old view.
4. User gradually tries the new view on their own schedule.
5. User recognizes the new view is better.
6. New view becomes the default.

### 1.5 The core reframing statement: screens already exist (Selva)

> "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI. But obviously, it's been redesigned to adopt a new workflow, a new UX and everything."

This directly contradicts the Set 02 vertical / missing framing.

### 1.6 The marriage metaphor (Selva)

> "Take that UX and that experience, marry it with the backend that's already there in the system."

Decomposed:
- "That UX" = the EPNM-style classic workflow.
- "The backend that is already there" = the existing EMS backend, not to be rebuilt.
- "Marry it" = connect the classic UX presentation to the existing EMS backend services.

This is explicitly described as a UX overlay, not a conversion.

### 1.7 Explicit negation of missing functionality (Selva)

> "So in a sense, it's along the lines of what you've said, and we're not looking for missing functionalities, but we are looking for things that are there but gives us the same user [experience]."

### 1.8 The forking metaphor (Guhan)

> "So it's the same thing. It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."

One-sentence summary: "It's just the look and feel."

### 1.9 Customer adoption, renewal revenue, and phase-out as the business rationale

Guhan on the customer adoption driver:

> "Our customers are asking that the operators are very used to a 10-year-old product. They can't just like that — one thing, they don't want to learn everything. They're asking us two or three, two releases or something, like a year, like a couple of releases or two or three. So we keep classic and the new."

Key points:
- Operators have a decade of EPNM muscle memory.
- Objection is to the entire new UX, not to specific missing features.
- Customers are asking for a transition period of roughly two or three release cycles (about a year).
- The word "classic" is introduced as the working label for the EPNM-style view.

Selva on renewal revenue:

> "This is one of the things, at least it's been in our minds, and then it's been top of my mind also, to improve the customer adoption. This is one of the challenges we are having. See, when it comes to renewal, we want the customers to go to this new product and the new thing. We don't want them to stick around with the older one."

Selva on phase-out:

> "We really want to phase out the old one and then go on the new one. That's where we're doing all the new things, cool things. We're not planning to sustain the old thing forever."

Guhan on end state:

> "And then over time we say okay we're going to take away your old view. This is the only view right now."

The four-phase lifecycle:
1. EMS has only the new UX (current state, causing customer resistance).
2. EMS gets a classic view toggle (the work being scoped).
3. Customers use classic view as a comfort bridge while learning the new UX.
4. Classic view is deprecated and removed; new UX is the only option.

### 1.10 What was ruled out: backend reimplementation (Guhan)

> "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work. If we write all the backend again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."

Guhan's four reasons:
1. Effort (a lot of work).
2. Maintenance burden (two backends to maintain).
3. Staffing (team is not resourced for dual backends).
4. Engineering judgment (not the right way to do it).

Guhan's definitive statement referring to Colin:

> "We are not trying to reboot the backend from older, right? That's not something what we want him to do."

Selva echoed this verbatim: "Guhan is absolutely right. We're not trying to reboot the backend from older, right? That's not something what we want him to do."

Guhan also raised footprint:

> "If you write, if you have two different backup, multiple backup services, it will also increase your footprint. You have to be cautious about it."

Footprint meaning deployment footprint (compute, memory, infrastructure) in customer environments.

### 1.11 The narrow exception: minor backend touchup for lens or filter differences (Selva)

> "One thing is, for example, in the older UI, we might have given him ability to look at things with a different lens. And we sometimes may or may not have that. Let's say that I am... A crude example is I'm showing a certain functionality with a broader lens. I'm showing everything. Whereas the newer thing is like filtering things out and showing it with a certain way. The converse may be true too. We may be doing the filtering in the older one. Now we are doing like a broader lens. So this means that there may be slight touchup to the backend to do that filtering."

The rule: no backend rewrite, but minor API-level adjustments (filter parameter added, query scope widened or narrowed) are expected and acceptable. Selva characterized this as "the kind of thing we expect."

### 1.12 Server-side risk: critical release path (Selva)

> "Any changes to the current server, because the current server is also getting updated. With no changes to the backend preferably, because any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."

Meaning:
- Cisco's backend is under active development for an upcoming release.
- A server-side regression could break both the new UI and the classic UI simultaneously.
- "No way to go either way" = no fallback if both break at once.

### 1.13 Colin's recognition of the change

> "This is actually in a good way. It changes the scope. It reduces it a little bit. Because I was thinking we were going to have to do the whole backend."

### 1.14 Selva's partial pushback on "scope reduced"

> "To me, I don't think it changes the scope that much. Whatever you have here still applies. For example, I told you this. Sometimes you may need to go touch the backend to do this particular API. Since we are not presenting a certain information in a certain way, I'm not having a corresponding backend API. So you may need to do that corresponding thing to make it happen. So which is similar to what you have mentioned here."

Colin's existing POC document discovery / exploration / tooling work still applies; the nature of the output has changed but the shape of the effort is comparable.

### 1.15 "Direction from the top" executive pressure (Selva)

> "Because you can always see where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently. And I think we have to. So that's why the AI, your expertise needed."

Leadership is pushing away from the one-person-per-screen model toward an AI-accelerated approach.

---

## 2. POC Planning Details

Source: 03_meeting_poc_planning_2026-03-25.md (primary) and 03_meeting_scope_reframe_2026-03-25.md

### 2.1 Target screens: Faults and Inventory

> Guhan: "Like the fault and I think, is it inventory or?"
> Selva: "It's inventory, yeah."

Guhan explained the selection:

> "So, these are very common applications that customer usually go to."

Established facts:
- The POC targets two to three screens.
- The confirmed candidates are Faults (fault management) and Inventory.
- A third screen was implied ("two to three") but not named; it will likely be identified in the upcoming India team session.
- Selection logic is customer usage frequency, not technical complexity.

Full product scope (cited by Colin during the meeting): "There's, I think in total 200, 250 screens, or workflow screens that will have you going."

### 2.2 Local-per-screen toggle for POC (Selva)

> "For the toggle, as I said, let's not worry too much about the UX. There is a separate UX team. We didn't want to involve them here. So this is like we can keep it simple and say we will do local toggle. By that what I mean is, let's say a fault screen for example, right? That's the one I want to give you. You want to take in this new product and you want to give an equivalent classic experience. We'll just add a toggle to that very same page and say once you toggle it gives me the classic."

POC implementation rules:
- Toggle is per-screen, embedded in the existing EMS screen.
- No UX team involvement for POC.
- Keep it simple; the goal is illustration of the concept, not a polished UX.

### 2.3 Global toggle is the product-level future (Selva)

> "But when we finally do the product, we may do it somewhere globally in the user setting or somewhere where they say, and then the whole experience is going to be classic. So that we'll worry about later."

Reinforced:

> "Now, let's say we're going to pick three screens. We're going to have a local toggle on each one — one, each one, another — to keep it simple. Because you're just illustrating the idea."

Phasing:

| Phase | Toggle Type | Scope | Purpose |
|-------|-------------|-------|---------|
| POC (now) | Local, per-screen | 2-3 screens | Illustrate the concept |
| Product (later) | Global, user settings | All screens | Customer-facing feature |

### 2.4 Exponential decay / front-loading (Colin)

Colin's framing:

> "This does grow exponentially. So when it starts out, I think we'd said it would just be me working on this for the POC, but it's still fine. That is the slowest it will ever be."

> "So it takes time to, there's that initial inertia just to get everything set up, learn the initial quirks of the system. Everything after that is kind of a multiplier for the speed. We'll still be able to scope that up perfectly, but don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just... kind of that initial front loading of getting everything set up, understanding everything, discoveries wrapped in there too."

Selva asked for confirmation:

> Selva: "On your earlier comment, I didn't quite catch, are you saying that initially it takes more time and then the subsequent ones will be even faster?"
> Colin: "Yes, yes, by far. So typically what we see, and this is the first, it's almost like this exponential decay cycle truly, even the time-wise, the first time is us, first of all, understanding the problem. So there's that kind of onboarding period for us."

Specific claims:
1. Initial inertia: environment setup, codebase understanding, architecture mapping, agent development, pattern establishment — work that is not repeated for later screens.
2. Multiplier effect: each subsequent screen leverages the infrastructure and patterns built earlier.
3. Three weeks for the POC does NOT equal one week per screen. Colin explicitly warned against this linear extrapolation.
4. Exponential decay: per-screen time decays exponentially, approaching a steady-state rate.

Efficiency mechanism (Colin):

> "We're very good at that. So we won't need much hand holding once we have access to the code base. We go and have exploration happen. Even on this, I said we kind of build our own kind of map of the application. So we understand a lot more without having to ask SMEs. So we try to make that as painless as it can be. The only time we'll ask questions is if things contradict each other or things aren't in alignment or logically speaking."

### 2.5 Parallelizable workflow (Colin)

> "So in terms of that, I think from a resource perspective, if we said, but there's I think in total 200, 250 screens, or workflow screens that will have you going, something like that. Now, I'll say this is a very parallelizable workflow."

> "So once the foundation is there, once those agents are there, it's really just a matter of having people on our side to continue to run this and be the quality checkers."

> "For instance, for me it's like I would have a person dedicated to just the QA/QE agents, you know, and I would have a person doing this subset of screens, doing that batch, moving on to the next. I can get more done with more people in parallel."

Parallel stream model:

| Stream | Focus | Personnel |
|--------|-------|-----------|
| QA / QE agents | Build and run automated verification agents | 1 dedicated person |
| Screen batch A | Convert a subset of screens using established patterns | 1 person |
| Screen batch B | Convert another subset of screens | 1 person |
| Additional batches | Further subsets | Additional people |

### 2.6 Automated QA / QE agents (Colin)

> "There are going to be extra steps that we can throw into after the POC is done, which is kind of automated QA/QE for it. That doesn't have to replace, but instead to complement the existing QA/QE process."

> "So for instance, even if we wanted to set up like a user persona, train an agent to go and know the old interface and then say, you know, try this on the new interface, make sure that everything is matching. We can do that."

Selva: "That would be great too."

Colin added:

> "We can even have an agent try this out on a classic content and then say this is matching with what was the experience. And we can do that from a number of different echos too."

(The word "echos" is a likely speech-to-text error for "angles" or "vectors" — multiple perspectives: different user roles, different data states, different workflows.)

Customer-specific workflow testing:

> "So like even for instance if there's a customer that uses a certain subset of screens or does a workflow..."

Tool: Playwright. Colin stated: "We use Playwright."

### 2.7 Classic versus new UI matching as the acceptance test (Guhan)

> "We will say hey old way of doing this for example like faults right and then now you're doing new way of doing that and then switch and then say do some actions here, do some actions here and then final test will be to show the same thing comes up everywhere."

The acceptance test flow:
1. Start on the faults screen in the new EMS view.
2. Perform some actions (view, filter, interact).
3. Toggle to the classic view.
4. Perform the same actions in the classic view.
5. Verify the results are consistent in both views.

This is functional equivalence testing — both views produce the same outcomes because they share the same backend.

### 2.8 Venn diagram approach to feature mapping (Colin)

Selva asked:

> "How will you figure out things like, I mean, I'm able to do a certain functionality in this new UI, and then that functionality is not even, it was there or not even there in the previous one, you'd be able to figure out and analyze between how?"

Colin:

> "So that's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about, as you said. But for the start out, we would essentially not know. So we'd have to map that out."

> "We like to do that because it actually makes our life easier. So rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore. And that helps us ask the right questions, so it's a lot more efficient."

Meaning:
- One circle = EPNM functionality. Other circle = EMS functionality. Overlap = functionality shared by both.
- Target is a perfect circle overlap for the areas customers care about.
- 100 percent functional parity across every historical EPNM capability is not required; customer-relevant parity is.
- The mapping does not yet exist. Neither BayOne nor Cisco has a comprehensive EPNM-to-EMS feature map. Building it is a discovery deliverable, driven by agent-based codebase exploration rather than calendar meetings.

### 2.9 Azure Foundry reference (Colin, demonstrated during the meeting)

Colin screen-shared Azure Foundry during the call:

> "Like, for instance, this is Azure Foundry. This has a toggle to show the old version versus the new version. New version, you can see a completely different UI flow. But old version... you'll see that old version looks much different."

Guhan's confirming response: "Thank you. So it's the same thing. It's essentially forking the UI. So back-end is kind of consistent between the two. It's just the look and feel."

The Azure Foundry example served as a concrete visual anchor for the toggle pattern and an architectural confirmation that Guhan and Colin were aligned.

### 2.10 Diversity versus priority in screen ordering (Colin)

> "And the more diversity of the screens that we encounter, it's a good way for us to even plan what screens. Because there's the priority order, but there's also the diversity order. Diversity order helps us cover all the edge cases that we might miss with agents. So it can be more intelligent with this."

Two selection criteria:
- Priority order (Guhan's criterion): screens that customers use most — Faults, Inventory.
- Diversity order (Colin's criterion): screens covering the widest range of UI patterns (table, detail / form, topology / graph) so agents learn more edge cases early.

Colin raised this as a planning consideration, not as a challenge to Guhan's selection.

### 2.11 Colin's confidence statement

Selva pressure-tested:

> "What is your confidence level with respect to this quote-unquote, the same experience for customer, what they want? Without bugs and maybe we still have to release it with quality and it's going to be product of product. It's not a prototype. Eventually it will be product, right?"

Colin: "Very high. Very high."

Qualified with:

> "I think one of the goals that I would have for this depends upon how comfortable everyone is. I know there's other initiatives at Cisco to go to what we'd say is like 100% AI generated code. This is a very good one where maybe not at first can we say that because at first we're going to need to pass a manual oversight of this."

> "Once we have a pattern established, this starts to take off. And that's the momentum that comes with these agentic workflows. Once you get those early kinks worked out, I won't be the guy that sits here and tells you it's going to be perfect on day one. It never is. But every iteration of this, it's a very iterative process, gets better."

---

## 3. Scope Boundary Clarifications

Sources: 03_meeting_scope_reframe_2026-03-25.md and 03_meeting_poc_planning_2026-03-25.md

Hard constraints on the POC, pulled directly from Selva and Guhan statements:

### 3.1 Backend is not to be rewritten (Guhan, emphatic)

> "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work. If we write all the backend again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."

> "We are not trying to reboot the backend from older, right? That's not something what we want him to do."

### 3.2 Target screens already exist in EMS (Selva)

> "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI."

Scope is not porting missing functionality. Scope is adding a classic view overlay to existing screens.

### 3.3 No missing-functionality work (Selva)

> "We're not looking for missing functionalities, but we are looking for things that are there but gives us the same user [experience]."

### 3.4 Backend changes only at API-level touchup scale (Selva)

> "There may be slight touchup to the backend to do that filtering. That's the kind of thing we expect."

Acceptable: adding a filter parameter, changing a query scope to present data at a different lens.
Not acceptable: reimplementing services, recreating backend logic.

### 3.5 Server-side changes carry release-path risk (Selva)

> "Any changes to the current server, because the current server is also getting updated. With no changes to the backend preferably, because any service change we have — we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."

The backend is under active development by Cisco and is in the critical release path. Regressions could break both the new UI and the classic UI with no fallback.

### 3.6 Footprint constraint on dual backends (Guhan)

> "If you write, if you have two different backup, multiple backup services, it will also increase your footprint. You have to be cautious about it."

Deployment footprint in customer environments is a real constraint.

### 3.7 UX team ownership sits outside POC (Selva)

> "For the toggle, as I said, let's not worry too much about the UX. Finally, of course, we'll take the blessing of the UX. There is a separate UX team. We didn't want to involve them here so this is like we can keep it simple and say we will do local toggle."

UX ownership of the final design rests with Cisco's separate UX team. For POC purposes, the UX team is explicitly not involved. The POC is a functional demonstration, not a UX deliverable.

### 3.8 POC toggle scope: local-per-screen only (Selva)

> "Let's not worry too much about the UX... we will do local toggle... just add a toggle to that very same page and say once you toggle it gives me the classic."

Global or user-settings-level toggle is explicitly deferred to the product phase, not part of the POC.

### 3.9 POC must be production-quality code (Selva)

> "It's going to be product of product. It's not a prototype. Eventually it will be product, right?"

(Likely "part of the product.") The POC output, while proof-of-concept in form, must be production-grade since the classic view toggle will ship to customers.

### 3.10 Functional equivalence is the acceptance bar (Guhan)

> "Final test will be to show the same thing comes up everywhere."

Both views must produce identical outcomes because they share the same backend.

---

## 4. Next Steps Committed in Set 03

Source: 03_meeting_next_steps_2026-03-25.md

### 4.1 Colin to amend the POC document

Selva: "And if you want to amend this document for that UI thing, you can do that."

Colin agreed. The POC document (written under the Set 01 / 02 framing) needs to be revised to reflect:
- Classic view toggle concept rather than missing-functionality porting.
- Local toggle per screen for POC.
- Faults and Inventory as target screens.
- Backend remains untouched (minor API adjustments as exceptions).
- Parallelizable post-POC scaling model.

Selva described the "running thread" that stays constant:

> "This document, that's the running thread you want to be, because in a sense it's bringing in screens and tying it with the backend thread. It doesn't change. But the slight twist to that is, it's an existing thing. And then we'll also show you how it exists in the old product."

### 4.2 Selva to schedule the India team session

> "The next step will be, I'll get the domain experts on this. And then we will set up a session with you to go over specific things we want."

> "Expect something early next week."

> "I'll work with the team in India and give you the next two days, and then I'll get back to you with a meeting sometime next week."

Timing:
- Next two days (March 26-27): Selva coordinates with India team.
- Week of March 30: target for the actual walkthrough session.
- Subject to India team availability.

Selva on the session's coverage:

> "Now the specifics of which screen are we going to do. What is the outcome here? And then what is the equivalent of that in the old product? How do you get to the code of the old product? How do you get to the code of the new? And then we give you access to both."

Session count is undetermined: "maybe I don't know, like you'll need one session or another couple of sessions to do that."

Selva will attend at least the intro:

> "At least for the intro and setting up the right context, I'll be there."

The team is India-based:

> Selva: "I'm expecting that the team will be in India, by the way, Colin."
> Colin: "Yes. No problem."

### 4.3 Selva to create a WebEx space

> "I will create a space between you, me and Colin on WebEx and then we can decide. Other folks there and then we can decide on our time and then we can schedule."

Initial members: Selva, Colin, Rahul. Others can be added. This is the primary ongoing coordination channel.

### 4.4 Local San Jose resource for Colin's first week

> "I also wanted to like reconfirm with Kuhan of anyone local from San Jose. I have a few people in mind or at least one, right? That can give you the overall overview and everything, right? So that really, at least for the first week, you have someone to, if you have anything or bounce off something."

- Purpose: rapid back-and-forth during initial ramp-up, particularly first week.
- Selva has candidates.
- Requires Guhan's sign-off (raised after Guhan had left the meeting).

### 4.5 Colin to finish Cisco onboarding

Colin announced receipt of Cisco hardware: "You'll be happy to know I finally got my Cisco hardware."

Guhan: "May the first code you write is for us."

Colin had the laptop in hand as of March 24. Setup was partial as of the meeting ("I got it set up late last night. I haven't gotten signed into everything").

Colin also stated: "I have been onboarded, I have Cisco ID, taking all the trainings today itself, so I'll have access to everything."

Guhan confirmed: "He's completely onboarded."

### 4.6 Access to both old and new codebases

Selva committed to providing code access as part of the walkthrough: "How do you get to the code of the old product? How do you get to the code of the new? And then we give you access to both."

### 4.7 Critical-path items before active POC work

1. Colin completes Cisco laptop setup and sign-in (in progress, near-immediate).
2. Colin completes application-specific trainings (in progress).
3. Selva creates WebEx space (committed).
4. Selva schedules India team walkthrough (target: week of March 30).
5. Walkthrough session occurs — screens, EPNM equivalents, code access covered.
6. Code access granted for both EPNM and EMS.
7. Local San Jose resource confirmed (not a hard blocker).

Expected timing for active POC work to begin: end of week of March 30 or beginning of week of April 6.

### 4.8 Action item table (from source)

| # | Action Item | Owner | Timeline |
|---|-------------|-------|----------|
| 1 | Amend POC document to reflect classic UI toggle framing | Colin | Near-term |
| 2 | Create WebEx space for Selva, Colin, and Rahul | Selva | Immediate |
| 3 | Coordinate with India team to prepare for walkthrough | Selva | March 26-27 |
| 4 | Schedule team walkthrough with India domain experts | Selva | Week of March 30 |
| 5 | Confirm local San Jose resource with Guhan | Selva | Near-term |
| 6 | Complete Cisco application-specific trainings | Colin | Day of and following |
| 7 | Finish signing into Cisco systems on new laptop | Colin | Immediate |

---

## 5. Key People Dynamics

Source: 03_meeting_next_steps_2026-03-25.md (primary) and both other files

### 5.1 Guhan's hard stop and handoff to Selva

Guhan opened with his time constraint: "11:25, I need to bail out. Salva can continue."

On reaching the hard stop: "I think I have to have a host stop at Selva. I hope you can. Maybe you can capture these things, the high level. This is the one that we'll chat with."

Guhan offered to stay briefly for Rahul: "And Rahul, if you have any other questions, right? I mean, I'm here to answer a few moments and then we'll probably look for the next one."

After Guhan's departure, Selva took operational ownership of logistics, scheduling, local-resource coordination, and WebEx space creation.

### 5.2 Operational ownership map

- Guhan: strategic framing, scope direction, executive-level decisions. Involvement going forward is limited; he has delegated operational coordination.
- Selva: operational coordination of the POC — scheduling, team walkthrough, WebEx space, local San Jose resource, code access, ongoing technical liaison. Will attend at least the intro of the India team session.
- Rahul: included in the WebEx space; present on this call. Specific ongoing role not explicitly defined.
- Venkat: referenced by Selva as being the push behind July delivery ("direction from the top"). Not present. Alignment between Venkat's expectations and the reframed scope is an open question flagged in the source.
- Colin: amends POC document, completes application trainings, runs discovery and POC execution once access is granted.

### 5.3 Venkat referenced (not present)

Referenced by Selva in the "direction from the top" context. Venkat is understood to be pushing for July delivery. It is not known whether Venkat is aware of or aligned with the reframed scope versus the earlier full-stack framing.

### 5.4 Rahul joining partway through

Rahul was on the call. Selva explicitly included him in the planned WebEx space. A second voice (likely Rahul) confirmed Colin's onboarding: "Yeah, he's done. He's done with it."

### 5.5 Informal end-of-meeting discussion

After Guhan departed and the formal agenda wrapped, an informal exchange between Colin and Rahul included:
- A status-update message Colin was drafting or reading about having his Cisco hardware and pending application trainings.
- A building reference: "This is building 22?" — "No, we're in building 20, but we can meet them in building 22."
- A garbled reference to a message (possibly deleted) from someone sounding like "Cerny" saying "another team is working on this." Not resolved in-meeting, potentially worth follow-up.
- A suggestion of an impromptu meeting using the remaining time slot.

---

## 6. Verbatim Statements That Shape Scope

These are the statements the execution session must not contradict. Each is attributed and paraphrased close to verbatim.

### 6.1 Selva statements

- "Maybe this didn't come out as clear in the first meeting."
- "We are looking at, you know, like how in Outlook and some of the banking applications, when you change your flow or when you come up with a new UX, they give you the option to toggle and say, I want to continue with the old workflow until I'm comfortable."
- "The areas that we are going to pick are areas that already exist in the new EMS. So it's not like it is not there. It's got a backend. It's got a UI."
- "Take that UX and that experience, marry it with the backend that's already there in the system."
- "We're not looking for missing functionalities, but we are looking for things that are there but gives us the same user [experience]."
- "There may be slight touchup to the backend to do that filtering. That's the kind of thing we expect."
- "Any changes to the current server, because the current server is also getting updated... we are in the critical release path, which is basically it can cause now we will have a non-usable or a buggy new UI under classic UI. So we will not have any way now to go either way."
- "We will do local toggle by that what I mean is let's say a faults screen for example... we'll just add a toggle to that very same page and say once you toggle it gives me the classic."
- "When we finally do the product, we may do it somewhere globally in the user setting."
- "Now, let's say we're going to pick three screens. We're going to have a local toggle on each one — one, each one, another — to keep it simple. Because you're just illustrating the idea."
- "This is one of the challenges we are having. See, when it comes to renewal, we want the customers to go to this new product and the new thing. We don't want them to stick around with the older one."
- "We really want to phase out the old one and then go on the new one."
- "We are being asked to think differently. And I think we have to. So that's why the AI, your expertise needed."
- "It's inventory, yeah." (confirming inventory as the second POC screen)
- "And if you want to amend this document for that UI thing, you can do that."
- "I'll get the domain experts on this. And then we will set up a session with you to go over specific things we want."
- "I'm expecting that the team will be in India, by the way, Colin."
- "I will create a space between you, me and Colin on WebEx."
- "To me, I don't think it changes the scope that much. Whatever you have here still applies."

### 6.2 Guhan statements

- "Our customers are asking that the operators are very used to a 10-year-old product. They can't just like that — one thing, they don't want to learn everything."
- "So we keep classic and the new."
- "It's essentially forking the UI. So backend is kind of consistent between the two. It's just the look and feel."
- "And we don't want to rewrite the backend services. So that can keep me honest. Because that's a lot of work. If we write all the backend again, then we have to maintain two different versions. We're not staffed. It's not the right way to do it."
- "We are not trying to reboot the backend from older, right? That's not something what we want him to do."
- "If you write, if you have two different backup, multiple backup services, it will also increase your footprint."
- "And then over time we say okay we're going to take away your old view. This is the only view right now."
- "Right now just for demonstrating POC let's say we pick two to three screens... for example like faults."
- "These are very common applications that customer usually go to."
- "Final test will be to show the same thing comes up everywhere."
- "Where we are getting direction from the top is 10 screens, now there are 10 people. We are being asked to think differently."
- "What is your confidence level that we can do this automated AI way without having to burn lots of resources?"
- "11:25, I need to bail out. Salva can continue."
- "May the first code you write is for us."

### 6.3 Colin statements

- "This is actually in a good way. It changes the scope. It reduces it a little bit. Because I was thinking we were going to have to do the whole backend."
- "Very high. Very high." (confidence)
- "I won't be the guy that sits here and tells you it's going to be perfect on day one. It never is. But every iteration of this, it's a very iterative process, gets better."
- "Once we have a pattern established, this starts to take off. And that's the momentum that comes with these agentic workflows."
- "This does grow exponentially... That is the slowest it will ever be."
- "Don't think if I say like it'll take us three weeks to do this, that that's three weeks for three screens, because that's just kind of that initial front loading."
- "It's almost like this exponential decay cycle truly, even the time-wise."
- "So that's what I call almost like a Venn diagram. And our goal would be a perfect circle overlap, at least for the areas that the customers care about."
- "Rather than trying to set up all these calendar meetings with the team and bogging everyone down, now with agents, we just go and explore."
- "There's the priority order, but there's also the diversity order. Diversity order helps us cover all the edge cases that we might miss with agents."
- "This is a very parallelizable workflow. So once the foundation is there, once those agents are there, it's really just a matter of having people on our side to continue to run this and be the quality checkers."
- "I would have a person dedicated to just the QA/QE agents... and I would have a person doing this subset of screens, doing that batch, moving on to the next."
- "Automated QA/QE for it. That doesn't have to replace, but instead to complement the existing QA/QE process."
- "Set up like a user persona, train an agent to go and know the old interface and then say, try this on the new interface, make sure that everything is matching."
- "We use Playwright."
- "This is Azure Foundry. This has a toggle to show the old version versus the new version."
- "Two or three representative screens are fully covered, converted."
- "There's, I think in total 200, 250 screens, or workflow screens that will have you going."
- "You'll be happy to know I finally got my Cisco hardware."
- "At least I have been onboarded, I have Cisco ID, taking all the trainings today itself, so I'll have access to everything."
