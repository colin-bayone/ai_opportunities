# 16 - Srinivas Sync: CAT MCP PR-Mapping Resolution

**Source:** /cisco/cicd/source/week_2026-04-27/day_2026-04-27/srinivas_team_meeting_2026-04-27_formatted.txt
**Source Date:** 2026-04-27 (Monday Cisco-side Srinivas sync, 1pm PST, ~60 minutes)
**Document Set:** 16 (Main chain Cisco-side Srinivas meeting)
**Pass:** Focused deep dive on Anupma's resolution that the CAT cache request data already contains the PR mapping plus all related metadata, eliminating the need for BayOne to construct a separate mapping table; closes Blocker 4 of the prep deliverable

---

## 1. Why this exchange matters

This was the second of Colin's "two very last questions" before close, raised at roughly 39:46 in the transcript and resolved in roughly two minutes of dialogue with Anupma, with a complementary follow-up from Justin. It was small in airtime and large in consequence: it eliminated one of the five Critical path blockers and clarifications needed items from the prep deliverable (Blocker 4, "CAT MCP querying mechanism") and removed an entire workstream BayOne had been preparing to scope and build for the dynamic answer path by Friday.

Going into the meeting, BayOne was carrying an open architectural question: does the CAT MCP, as exposed to BayOne, accept PR IDs, or does BayOne need to construct a PR-to-CAT-ID mapping table to bridge the chat surface (where issues arrive with PR IDs) and the MCP surface (which Srikar's Friday research had concluded requires CAT IDs)? Anupma's answer reframed the question entirely. The mapping is not something BayOne needs to construct; the mapping plus a great deal of related metadata is already present in the CAT cache request that fires as a check on every PR.

## 2. The technical gap as BayOne understood it going into the meeting

The picture BayOne held at the start of the meeting, drawn from Srikar's preparation work over the prior week:

- Chat issues in the WebEx NX-OS CI space arrive with PR IDs. Engineers reference their PRs when they ask for help.
- The CAT MCP, as inspected by BayOne via the MCP tool surface, exposes four tools and appears to require a CAT ID as the primary key to query.
- A PR ID and a CAT ID are not the same identifier. The CAT system tracks CAT requests; the PR is the GitHub-side artifact.
- Without a bridge between the two, the dynamic answer path in the Friday deliverable (chat question with a PR ID, hand off to the CAT MCP, get back the state of the request) does not function end to end.
- The naive workaround Colin had identified was to enumerate branches associated with CAT IDs and back-derive the mapping. He flagged this in the meeting as imperfect: "the mapping between those technically we can get out by listing out related branches that are related to the cat IDs. That's not always perfect."

This gap was tracked in the prep deliverable as Critical path blockers and clarifications needed, item 4: "CAT MCP querying mechanism. Chat issues arrive with PR IDs. The CAT MCP requires CAT IDs to query. A PR-to-CAT mapping is required for the dynamic answer path to function end to end. Does this mapping exist on the Cisco side, or is BayOne expected to construct it as part of the integration?"

## 3. Colin's two-option framing of the question

Colin presented the question as a binary, leaving the decision with the Cisco side rather than presupposing an answer:

- Option A: Extend the CAT MCP itself with new functionality, so it accepts a PR ID directly and resolves to the underlying CAT request internally. This would put the work on the CAT MCP owners (Anupma's side), not on BayOne.
- Option B: Have BayOne work around the CAT MCP by constructing the PR-to-CAT mapping externally. The fallback Colin had in mind was the imperfect branch-enumeration approach.

The question as Colin posed it: "Do you the question really here is, do you want that CAD M C P to be extended with functionality? Or do you just want us to try to work kind of around it so that we can do that mapping between CAD ID to P R."

Anupma's answer was effectively neither A nor B. The capability already exists; BayOne was looking at the wrong layer.

## 4. Anupma's resolution

Anupma's response, in her words: "So cat ID should already have the PR mapping in it. Okay. Because have you have you maybe I can quickly. Here to show you how a cache request looks like and what all data it has."

She then walked the group through the actual CAT cache request data structure live on screen. The mechanism she described:

- Every PR in the NX GitHub repository has a Checks tab.
- One of the checks that fires on each PR is the CAT request creation check.
- That check produces a CAT cache request object. Anupma referred to this object variously as "cache request," "care request," and "character class," all of which the speech-to-text rendering should be read as the same data structure: the CAT cache request.
- The CAT cache request is the record that is dispatched per PR check and carries the full context of the request through the CAT system.

The fields she enumerated as present in that object:

- Branch (the GitHub branch the PR is built from)
- Submitter (the engineer who opened the PR)
- Bug ID (the linked defect tracker reference)
- SHA (the git commit hash; Anupma said "Shah" and "Shaw," both speech-to-text renderings of SHA)
- Sub-initiator
- CAT initiator (Anupma said "card initiator," speech-to-text rendering of CAT initiator)
- All the checks (the broader set of checks that ran against the PR)

Her summary statement, which is the load-bearing sentence for closing Blocker 4: "Single mapping to the PR as well as other information. That's branch. And as I said, right? Like the Shaw. And the sub- initiator, card initiator."

In other words, the CAT cache request carries a single mapping to the PR. Given a CAT cache request, the PR is unambiguously identified. Given a PR, the CAT cache request that was created against it is reachable through the PR's Checks tab. The bridge BayOne thought it would have to construct already exists, with a richer payload than the bare PR-to-CAT-ID mapping BayOne had in mind.

Colin's reaction in the moment: "Mhm. Okay, there's actually quite a bit. That's great." And on close of the exchange: "No, that's great. That's great. Okay, question answered. Thank you. That's really nice."

## 5. The access path Anupma described

Anupma gave a concrete, replicable path for a Cisco engineer (or BayOne with NX GitHub access) to inspect a CAT cache request:

1. Open any PR in the NX GitHub repository.
2. Go to the Checks tab on that PR.
3. Locate the CAT request creation check.
4. Open the CAT cache request data emitted by that check.
5. Inspect the fields directly.

Anupma's framing, important for tying this back to Friday's other unblocking: "Now that you have access to the NX GitHub, right? So you should be able to go there." This anchors the CAT MCP resolution to the NX GitHub access path that was unblocked on Friday April 24 (CN-SJC-STANDALONE bundle membership granted, Temp ADS connected and ready, NX repository sign-on the gating step before access can be granted per the prep deliverable Open items and access table).

The access path is therefore: NX GitHub access (already in motion as of Friday) -> any PR -> Checks tab -> CAT request creation check -> CAT cache request payload, with full PR-to-CAT mapping plus branch, submitter, bug ID, SHA, sub-initiator, CAT initiator, and all checks.

## 6. Justin's complementary contribution

Immediately after Anupma's walkthrough, Justin added a second, parallel data source: "And, then the GitHub data should also contain that I have. Like once we'reum yeah I'll try to get you that GitHub or we just created a new data, a MongoDB like recently last week or something. So, that should also have that data as well. Okay. Um, any yeah, whatever the GitHub is posting, we should be collecting that now."

Decoded:

- Justin's team recently stood up (last week, roughly mid-April) a new MongoDB that ingests GitHub events from the NX GitHub repository.
- Whatever GitHub posts as event payloads is being collected into that MongoDB now.
- The same PR-to-CAT mapping plus surrounding metadata that Anupma showed in the CAT cache request is also reachable through this MongoDB, since the CAT cache request fires as a check and check events are part of what GitHub posts.
- Justin offered to provide BayOne access to the MongoDB. Earlier in the meeting Diwakar and Srinivas had already discussed read-only access for BayOne engineers ("just in you have the data, so if we could give. Read only access to the engineers. Do you have any? Maybe you can create a generic user ID and give it to them."), with Justin saying he would check on that.

Justin's MongoDB therefore acts as a second, independent path to the same data. For implementation, this is useful because it gives BayOne a queryable backing store rather than requiring per-PR Checks-tab traversal.

## 7. The MCP-tools-versus-underlying-data distinction

Srikar's prep work over the previous week, reflected in his Set 16 prep call analysis, identified four tools exposed by the CAT MCP and concluded that the tool surface required CAT IDs. That conclusion was correct as a description of what BayOne saw via the MCP interface alone. Anupma's answer is not a contradiction of Srikar; it is a layer below it.

The distinction:

- MCP tools as exposed to BayOne: a set of named tool calls with documented input schemas. Whatever those tools require (CAT ID, in Srikar's reading) is a fact about the tool definitions.
- MCP underlying data via PR checks: the data that the CAT system itself produces and stores per PR check. This data is broader than what any single tool call exposes and includes the PR-to-CAT mapping by construction, because the CAT cache request is created in response to a PR.

Anupma's reference to the access path went through the GitHub Checks tab, not through an MCP tool call. Her phrasing "All the data should be available through the. MCP as well" suggests the data is in principle reachable via the MCP, but the demonstrated path she walked through was GitHub-side: PR -> Checks tab -> CAT request creation check -> cache request payload.

The practical implication for BayOne's Friday integration:

- Do not treat the four MCP tools as the only surface for CAT data.
- Treat the CAT cache request, accessible per PR through the Checks tab and also collected into Justin's MongoDB, as the authoritative joined record.
- Use either the GitHub Checks payload (Anupma's path) or Justin's MongoDB (Justin's path) as the source for the dynamic answer path.

This distinction is worth capturing precisely because it explains why Srikar was not wrong and why BayOne's plan-of-record going into the meeting (build a mapping table) was reasonable given what was visible. It also flags a research note for BayOne going forward: when an MCP appears to be missing capability, check whether the underlying system stores the data outside the MCP's tool surface before scoping a workaround.

## 8. Implication for the Friday May 1 deliverable

The dynamic answer path in the Friday deliverable was scoped in the prep deliverable as: chat question with a PR ID arrives -> dynamic answer path routes to the CAT MCP -> CAT MCP returns state -> answer composed. The hidden assumption was that BayOne would supply or construct the PR-to-CAT-ID translation either as a precomputed mapping table or as an at-request-time lookup.

After Anupma's resolution, that assumption is gone. The Friday plan can rely on either:

- Reading the CAT cache request from the PR's Checks tab on demand (Anupma's path). This is direct from GitHub, requires NX GitHub access, and gives the full payload including branch, submitter, bug ID, SHA, sub-initiator, CAT initiator, and all checks.
- Querying Justin's GitHub-events MongoDB for the corresponding records (Justin's path). This is more efficient at scale, gives the same fields, and uses a backing store rather than per-PR traversal. Requires read-only access, which is in motion.

Either path is sufficient for Friday. Neither requires BayOne to build a mapping table. The richer payload also enables capabilities BayOne had not been planning for the Friday surface, since branch, submitter, bug ID, SHA, and the broader checks list are all available in the same record. For example, a "where is my PR stuck" answer can include the SHA, the submitter for routing, the bug ID for cross-reference, and the check status, without additional lookups.

Colin's close on the exchange captures the architectural confirmation: "awesome because that'll really help us out for mapping between them. Just so we're sure, we're sure that we're sure. Let me put it that way for the dynamic requests."

## 9. Mapping to the prep deliverable

Critical path blockers and clarifications needed item 4 in the prep deliverable read:

> 4. CAT MCP querying mechanism. Chat issues arrive with PR IDs. The CAT MCP requires CAT IDs to query. A PR-to-CAT mapping is required for the dynamic answer path to function end to end.
>    - Does this mapping exist on the Cisco side, or is BayOne expected to construct it as part of the integration?

Status after the meeting: closed. The mapping exists on the Cisco side, embedded in the CAT cache request that fires as a check on each PR. Two access paths are confirmed:

- Anupma's path: NX GitHub PR -> Checks tab -> CAT request creation check -> CAT cache request payload.
- Justin's path: GitHub-events MongoDB recently stood up by Justin's team, which collects whatever GitHub is posting and therefore includes the CAT cache request data.

BayOne does not need to build a mapping table. BayOne does not need to ask for the CAT MCP to be extended. The two-option framing Colin offered (extend the MCP versus build a workaround) is moot.

This item should move from Critical path blockers and clarifications needed to Recent closures in the next iteration of the weekly status, alongside the other items already listed there (NX repository access path defined; CI/CD repository destination clarified; Deployment form decided; Friday May 1 deployment target defined; Monday weekly cadence and format decided; CN-SJC-STANDALONE bundle membership granted, Temp ADS connected and ready).

## 10. Dependencies that ride alongside this resolution

The resolution does not stand entirely on its own; it has two upstream dependencies that need to track to completion:

- NX GitHub access for BayOne team members. Anupma's "now that you have access" assumes first sign-on by each BayOne engineer is complete or imminent. The prep deliverable lists this as Open items and access, item 1: user identifiers posted Friday, first sign-on is the gating step before access can be granted. This needs to land for any team member who will be wiring or testing the dynamic answer path.
- Read-only access to Justin's MongoDB. Justin said in the meeting he would check on creating a generic user ID for BayOne. This is a parallel path; Anupma's GitHub path is sufficient on its own, but the MongoDB makes implementation cleaner and is the path that scales.

Neither dependency is a blocker for the Friday deliverable in the strict sense, since Anupma's GitHub Checks-tab path is available as soon as NX GitHub sign-on completes. Both are worth tracking so that the team picks the cleaner of the two paths for the production wiring rather than locking in the GitHub-traversal path by default.

## 11. Open follow-ups that are not blockers

- Validate that the field names Anupma listed are stable across all PR types. The fields enumerated (branch, submitter, bug ID, SHA, sub-initiator, CAT initiator, all checks) came from a single live example. Confirming the schema across a sample of PRs would be a low-cost first task for whoever wires the dynamic path.
- Confirm whether Justin's MongoDB stores the full CAT cache request payload as nested data or flattens it. The prep work Srikar did identified four MCP tools by name, and the field set Anupma listed is broader than what any one tool returned. The MongoDB schema needs a quick inspection so the dynamic answer path's queries can be written against the correct shape.
- Decide between Anupma's path and Justin's path for the production wiring. Anupma's path is direct from GitHub and requires no additional access beyond NX GitHub. Justin's path is queryable, scales better, and matches the pattern Diwakar described earlier in the meeting (PR Apollo, GitHub events into MongoDB, MCP server on top). For the Friday first pass either is acceptable; for the longer arc the MongoDB plus an MCP layer is the clearer fit, since Diwakar and Srinivas both pointed at that direction in the broader meeting discussion.
- Capture this resolution in the BayOne research log so the MCP-tools-versus-underlying-data distinction is preserved as a research note for the team. Future MCP integrations on this engagement may have the same shape (a thin MCP tool surface over a richer underlying data store), and the lesson generalizes.
