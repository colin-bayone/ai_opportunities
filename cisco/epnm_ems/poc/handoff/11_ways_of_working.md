# 11 — Ways of Working

**Purpose of this document:** How the engagement runs day to day. Escalation patterns, what to decide autonomously versus what to raise, how to document progress, and the working rhythm that has been established across the seven meetings leading up to this handoff.

---

## 1. The Working Model in One Sentence

BayOne works independently on Cisco hardware with Cisco-approved tools, driven by agent-based code exploration rather than calendar meetings, raising questions to Cisco only when the code genuinely does not answer them, and escalating scope or tooling questions through Colin before acting.

Every element of that sentence is sourced from specific commitments in the research library.

---

## 2. The Bandwidth Reality

The Cisco engineering team is on a critical release path for their own product. Guhan, Selva, and Praveen all stated in different meetings that the team cannot invest significant time in the POC. Selva in Set 02: "We would very well be that one party who would be keen on seeing this on one side, seeing a bit to be fielded. On the other side, we have to keep our critical platform." Selva in Set 03: Guhan's hard stop at 11:25 and his handoff to Selva reinforced that senior time is scarce.

What this means for the execution session:

- Meetings cost the team. Batch questions. Do not fragment attention across many small asks.
- Agent-driven exploration is the first move. Read the code. Use the research files. Use this handoff. Only after exhausting those should a question go to the team.
- When a question is necessary, make it high signal: specific, clearly framed, with enough context that the Cisco counterpart can answer without re-establishing the frame.

---

## 3. Escalation Routing

### Technical questions about a screen or behavior

1. Read the EPNM code. If the question is about what EPNM does today, the answer is there.
2. Read the EMS code. If the question is about what the new UX does or what the backend exposes, the answer is there.
3. Read the research library (`cisco/epnm_ems/research/`). If the question is about what the team said, the answer is there.
4. Read this handoff. If the question is about framing, scope, or approach, the answer is here.
5. If the question is still unresolved, raise to Colin with the work already done summarized in one or two sentences.
6. Colin decides whether the question needs to go to Cisco. If yes, Colin routes it to the relevant tech lead (Akhil for Inventory, Jenis for Fault Management, Ramkrishna for architecture, Ramesh for testing and infrastructure).

### Scope questions

Scope questions never route past Colin unilaterally. Scope questions go:

1. Raise to Colin.
2. Colin either decides (if the question is within what he has committed to) or raises to Selva (if the question touches a Cisco-side commitment).

### Access and provisioning

1. Raise to Colin.
2. Colin engages Selva and Neha.
3. Selva engages Akhil, Aadit, or Ramesh depending on the need.

### AI tooling or library questions

1. Raise to Colin.
2. Colin makes the call. If the question is material (new library, new tool), Colin routes to Selva or Ramesh.

### Backend change questions

1. Verify whether the classic view can solve the problem in Angular (adapter, service layer, component adjustment).
2. If a backend change is genuinely required, size it: narrow API touchup versus broader capability gap.
3. Raise to Colin with the sizing.
4. Colin routes to Selva. Selva decides.

---

## 4. Decision Authority

### Execution session decides without escalation

- Component-level implementation details: file organization within the proposed folder structure, component naming within the `*-classic` convention, method and property naming.
- Angular-idiomatic patterns for a given conversion (which Material component to use from the approved mapping, when to use signals versus BehaviorSubject, when to use `*ngIf` versus `@if`).
- Internal unit test design and coverage within the scope.
- Playwright agent implementation details for the functional equivalence verification.
- Code style and linting decisions within Cisco's conventions.
- Library choice within the already-approved package set in the environment.

### Execution session raises before acting

- Anything that contradicts Guhan's scope commitments from the 2026-03-25 reframe.
- Any backend change, even narrow.
- Any new tool, library, or service beyond the already-approved set.
- Any AD group or VM request that was not in the Set 07 action list.
- Customer-facing artifacts of any kind.
- The code-organization proposal (Colin owes it to Akhil).
- Anything that feels like scope creep.

### Colin decides, or Colin escalates

Colin is the gate for anything Cisco-facing. The execution session does not interact with Selva, Guhan, Venkat, or the tech leads directly without Colin's involvement.

---

## 5. Documentation and Progress Tracking

### Blockchain-style research library

The engagement folder uses an append-only research methodology (documented in `cisco/epnm_ems/research/00_methodology_2026-02-09.md`). New research documents are numbered chronologically and never edited after creation. Summary documents reference other documents in the same set.

For the execution session: do not modify any file in `cisco/epnm_ems/research/`. That library captures what was known at each point in the engagement's history. Edits to it break the historical record. If new source material arrives (a new meeting, a new email, a new discussion), it gets added as a new numbered set — not an edit to existing files.

### Where POC progress goes

New work products (progress notes, decision logs, artifacts produced by the execution session) should live under `cisco/epnm_ems/poc/` — the POC working folder. Subfolders for specific categories of artifact are fine; the handoff package in `cisco/epnm_ems/poc/handoff/` is the entry point.

If this handoff document itself needs updating during the POC (because a risk materialized, an open question was resolved, or an item was added to the work list), update the relevant handoff doc with the new information and note the update date in a footer. Do not delete superseded content — add to it.

### Code documentation

Commit messages, code comments, PR descriptions, and in-code documentation must all read as standard Cisco engineering output. No references to AI, agents, prompts, models, or LangGraph in any customer-visible artifact. This is the customer-transparency principle in practice.

Internal BayOne documentation (progress notes in the POC folder) can reference the agent workflow freely. The distinction is whether the artifact will be seen by Cisco engineers reviewing code versus internal BayOne reference.

---

## 6. Communication Rhythm

### Default channel

The WebEx team space is the primary asynchronous channel. Once it is created, routine coordination, status, and low-urgency questions flow through it. High-urgency items still get raised in the recurring sync or via email.

### Recurring sync

A recurring sync with roughly the Set 07 attendee group is planned. Cadence and time slot were not agreed at the 2026-04-06 meeting. When it starts, it is the primary forum for:

- Progress updates.
- Decision points (scope clarifications, gap analysis findings that need Cisco direction).
- Questions that benefit from the full group being synchronously present.

### Email

Email is used for specific document handoffs (Akhil's code pointer email). The team space will likely replace email for most ongoing coordination once active.

### Escalation tempo

If the execution session raises a question to Colin and does not get a response within a working day, the normal pattern is a Neha nudge. Rahul described this explicitly in the 2026-04-06 meeting: "Sometimes he gets a little backlog and he just needs a little tiny internal nudge. So we'll make sure that any questions you guys have, Neha and me will make sure that, you know, you get a response back." The system is designed for Colin to not be the single point of failure.

---

## 7. How Progress Gets Reviewed

### Internal BayOne review

The execution session is responsible for demonstrating progress to Colin routinely. Colin is running the POC, and the execution session is a collaborator on that work. Running code, working demonstrations, and the internal test results are the currency of progress, not status reports.

### External Cisco review

Cisco visibility during the POC is scoped. Full dashboard visibility for the QA agent workflow is deferred to the full engagement. For the POC:

- The recurring sync (once established) provides the primary Cisco-facing visibility.
- The POC demonstration at closeout is the primary deliverable for Cisco.
- Colin coordinates any interim demo or preview that Selva asks for.

---

## 8. What "Good" Looks Like Day to Day

These are patterns from the transcripts that characterize effective execution on this engagement. They are guideposts, not rules.

- **Read code first.** Questions that the code answers should never reach the Cisco team. Colin: "We won't need much hand holding once we have access to the code base. We go and have exploration happen." The research library confirms this pattern is part of what Cisco has endorsed.
- **Batch questions.** If three related questions arise during a screen's analysis, resolve them in one ask, not three.
- **Treat the transcripts as authoritative for scope.** When in doubt about what was agreed, the research library is the source of truth. When the transcripts are ambiguous (speech-to-text errors on names, technical terms), defer to the screenshots for names and to the code for terms.
- **Preserve fidelity over elegance.** The classic view is not an opportunity to "improve" EPNM's behavior. Fidelity is the acceptance bar. If EPNM does something awkward, the classic view does the same awkward thing.
- **Flag narrow, solve narrow.** When a backend touchup is needed, it is a filter parameter, not a rewrite. When a library approval is needed, it is one library, not a batch.
- **Surface risks early.** If the gap analysis turns up something that could materially affect scope, raise it while it is small rather than letting it grow.
- **Keep the demo working.** The POC culminates in a demonstration. Progress toward a working demo is a better signal than progress against a backlog.

---

## 9. Customer Transparency (Re-stated as a Working Rule)

Customers never see the AI. This principle originates with Guhan in Set 01 and threads through Venkat's positioning in Set 05a. In practice:

- Commit messages: describe the change in standard engineering language.
- Code comments: describe what the code does, not how it was generated.
- PR descriptions: engineering intent and acceptance criteria.
- UI text: whatever EPNM says, the classic view says.
- Release notes: whatever Cisco product management writes.

Internal BayOne documentation can and should be honest about the agent workflow. The distinction is audience — Cisco engineers reviewing code, Cisco product management writing release notes, and Cisco customers reading UI text all see standard engineering output.

---

## 10. When the Execution Session Should Stop and Ask

The following should trigger a stop-and-ask rather than a proceed:

- A decision that feels like it should be unilateral but has non-trivial consequences if wrong.
- A tool or library need that was not anticipated in the approved set.
- A backend change that is larger than a narrow API touchup.
- A scope expansion that is being suggested from the Cisco side informally (during a casual exchange, an email, a sync). These should be captured and raised to Colin before being acted on.
- An AI compliance question about an activity that is not clearly covered by the existing rules.
- A pattern in the EPNM code that genuinely cannot be reproduced in Angular within the constraints (extremely rare, but possible).
- A realization that a work item may be materially larger than anticipated.

Stopping and asking is not a failure mode. It is the engagement model.
