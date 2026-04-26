# Consolidated Open Questions for Colin

All questions across the four working files, gathered in one place for batch review. Source file in parentheses. Answer in any format you like; the session folder gets updated from your answers and then we move to drafting actual artifacts.

---

## Block A: Srinivas Monday One-Pager (file 01)

**A1.** Confirm `weekly_status_<date>.md` as the filename, or align to whatever convention the existing CI/CD repo already uses for `.md` documents (Srinivas's other-products workflow may have a pattern worth matching).

**A2.** Confirm the same-Friday first cut Colin promised on Apr 24 was actually sent. If not, the Monday version absorbs that commitment and the spec should note the slip.

**A3.** Confirm the open-access-items section is appropriate even after items resolve, or whether resolved items should drop off immediately.

**A4.** Confirm Mermaid is appropriate for the next-Friday target diagram or whether plain markdown text is sufficient. Srinivas's "birthday view" / "border view" phrasing favors keeping the Mermaid.

**A5.** Confirm the decision-prompt section is appropriate or whether it reads as soliciting scope creep.

**A6.** Confirm scope of "this week" is Monday Apr 27 through Friday May 1 (the contract-renewal demo Friday).

**A7.** Confirm whether the regression-protection workstream gets its own GitHub issue this week or rolls into the next-Friday target as a stretch item.

## Block B: Master Open Items (file 02)

**B1.** Confirm the seven-section structure (A Srinivas Set 15 asks, B engagement history, C Main 15 forward items, C2 Wednesday MOM items, D decision-needed, D2 items implied by Sets 13 and 14, E temp ADS floor pointer, F excluded) is what you want, or restructure before anything translates downstream.

**B2.** Confirm the deliberate cross-listing of items in multiple sections (NX repo access in A4 and B1; Friday May 1 deployment in A2 and E; multi-MCP orchestration in A18 and C2; issue categorization productionization in A17 and B2) is the right call, or collapse to a single canonical location per item.

**B3.** Confirm Section F exclusions are right (cross-engagement template references, all DELIVERED items, SUPERSEDED items with no remaining work, internal-only personnel observations).

## Block C: Temp ADS Minimum Bar (file 03)

**C1.** Confirm Friday May 1 dry-run on temp ADS as the hard deadline.

**C2.** Confirm the framing-to-Srinivas language for the ceiling-not-hit case is the right diplomatic landing ("application is running, bot is running, static path works, dynamic path is wired and waits only for the access provisioning to complete").

**C3.** Confirm whether the team should preemptively start the fallback (BayOne stands up the CI/CD app shell directly on temp ADS) on Monday afternoon if Anupma's team has not delivered by then, or whether to wait an additional 24 hours.

## Block D: Policy Gate (file 04)

**D1.** Confirm the refined "BayOne contributor gate" header text is acceptable, or propose edits. Specifically: whether the explicit "does not gate Cisco engineers" sentence is right, or reads as overexplaining.

**D2.** Confirm placement: per-issue header (option 1), repo documentation (option 2), and GitHub issue template (option 3) all together, or pick a subset.

**D3.** Confirm what to do if Monday morning a signature is still missing: do not create issues for that person yet, or create issues with a more pointed header, or escalate directly off the issue surface.

**D4.** Confirm whether Cisco-visible repository content should reference the policy by full name ("BayOne Client Data Handling Policy") or by a shorter form ("BayOne contributor gate" / "BayOne data policy").

**D5.** Confirm whether the README/CONTRIBUTING addition (option 2) should link to the actual policy text on a BayOne-controlled surface, or whether the header alone is sufficient.

**D6.** Confirm whether the policy framing surfaces in Monday's standup as a verbal reminder, or whether the header alone (with the assumption all signatures are in) is sufficient.

## Block E: Sequence and ownership of next deliverables

**E1.** Once these blocks are answered, the four real artifacts to draft are:
- The Monday one-pager (markdown for the CI/CD repo)
- GitHub issue templates with the contributor gate header
- Per-person assignment from the master list
- Daily target tracker for the temp ADS floor

Confirm sequence (which first), and whether any of these should be parallel-drafted by sub-agents the way the corrective pass just was.

**E2.** Confirm whether the four working session files need to translate into Singularity research entries at any point, or whether they stay as session-local and only the final artifacts go to the chain (or to client-visible repos).
