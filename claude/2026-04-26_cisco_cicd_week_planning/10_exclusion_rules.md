# Exclusion Rules — What Stays Off Master Lists and Client-Visible Artifacts

Standing rules that govern what does NOT appear on master open-items lists, weekly trackers, deliverables, GitHub issues, or any artifact that could cross over to a client surface. These rules apply across the Cisco CI/CD engagement and any other engagement Colin is running.

---

## Rule 1 — No cross-engagement references in deliverables or trackers

Different client engagements stay separate. Names of other clients, names of other engagement leads, project codenames, methodology references that originated in a different client's project — none of these appear in this engagement's artifacts.

**Concrete examples:**
- Guhan Raman / his project / regression-protection template from his project does NOT get referenced in any Cisco CI/CD artifact, even when the technical pattern is reusable. The pattern can be applied; the source attribution stays internal-private.
- Sephora EDW Modernization, Lam Research IP protection, Ariat GCC, McGrath managed services, Tailored Brands QA, Zeblok partnership work — none of these get name-dropped in Cisco artifacts.
- BayOne-internal codenames, internal product nicknames, internal team conventions that are not shared with the client do not surface in client-readable surfaces.

**Why:** scope confusion, accidental disclosure of unrelated client work, register discipline, contractual confidentiality.

**Where this matters most often:** master open-items lists, weekly status one-pagers, deliverable HTML documents, GitHub issue bodies, joint chat messages.

## Rule 2 — No internal personnel observations on shared or client-visible artifacts

Internal observations about specific people — performance patterns, autonomy gaps, role critiques, political assessments — live in INTERNAL-ONLY files (Team Set 14a, 14b, 15 internal-only style) and do not appear on any master list, tracker, deliverable, or anything else that could cross over to a client.

**Concrete examples:**
- Mahaveer-as-procurement-listed-as-manager observation stays internal.
- Srikar autonomy-under-ambiguity diagnosis stays internal.
- Vaishali/Tanuja deliberate-hold-back-as-performative-theatrics framing stays internal.
- Cisco-side technical leadership critiques (Srinivas-runs-parallel-duplicate-projects, Nova-is-not-near-completion) stay internal.
- Engagement-origin yelling-match story stays internal.

**Why:** these are coaching-and-strategy frames, not facts that belong on operational tracking. Surfacing them on a tracker contaminates the tracker. Surfacing them on a client-readable surface burns trust and potentially ends engagements.

**Where this matters most often:** master open-items lists (Block B in file 02), weekly status one-pagers, GitHub issues, repo READMEs, joint chat content.

## Rule 3 — No "DELIVERED" or "SUPERSEDED with no remaining work" items on open-items lists

Open means open. Items that are fully completed in the form they were assigned, or that were overtaken by a later directive and have no remaining work, do not appear on a list called "open items."

**Why:** noise reduction. The list is for things that need attention.

**Note:** items resolved between the last meeting and the current one MAY appear with strikethrough on a Srinivas-facing weekly one-pager (per file 05a, A3). This is a different presentation rule for client communication continuity, not a master-list rule.

## Rule 4 — No internal politics on Cisco-visible repository content

Anything BayOne writes into a Cisco repository (CI/CD repo, SME-KB repo, future joint repos) does not contain BayOne-internal policy framing, BayOne-internal accountability framing, BayOne-internal team-coaching content, or anything that names BayOne's internal processes by name in a way that exposes them.

**Concrete example:** the BayOne Client Data Handling Policy is referenced ONLY by a one-line gate header on BayOne-internal issues, never named or excerpted in Cisco-visible artifacts. (Per file 05a, D4.)

**Why:** internal politics and process never surface on client systems.

---

## Operating note

This file is the source of truth for these rules. If a rule needs to be updated or added, edit this file. Do not rely on Claude's memory alone — Claude forgets, files persist.

Memory entries may also be saved as backup, but the file is canonical.
