# Deliverables Cleanup Assessment — Part 1: March 12 Files

**Date:** 2026-04-20
**Pass:** Full read of March 12 deliverables checked against current canonical engagement values
**Canonical source:** Engagement values as of 2026-04-20 (per session handoff and research library)

---

## Framing note on the March 12 file set

All seven files in this part are pre-scoping artifacts produced 2026-03-20 from the 2026-03-12 discovery call. They are EXPECTED to contain pre-scoping language (scope questions still open, approach preliminary, architecture aspirational). The canonical check here is not "does this match the POC SOW" (it predates the SOW), but:

1. Any factual claim that was wrong even at time of writing, or
2. Any statement that now reads as actively misleading given what has crystallized (e.g., scope is now customer name + fab identifier, not customer name + file name; execution is now in Lam's environment, not BayOne-hosted; methodology is layered sequential, not "hybrid two-layer"), and
3. Any .md vs .html drift.

---

## File: problem_restatement_2026-03-12.md

**Role:** Client-facing (source markdown; HTML counterpart is the rendered deliverable)
**Matches .md/.html counterpart?** Partial — HTML drops the phrasing "customer names (direct mentions in text)" and restructures the sensitive-info list into a table, removes the explicit "if we over-redact less than we currently restrict" quoted phrasing from prose into a boxed callout, and softens one Use Case 1 opening sentence. Substance materially aligned; the initial scope statement "customer name and file name" is identical in both.
**Status:** MIXED (valid as historical discovery artifact; contains now-wrong initial-scope statement that sits in the active deliverables folder)

### Discrepancies Found

1. **Line 4, "Date: 2026-03-20"** — Date discrepancy between filename (`_2026-03-12`) and header date (`2026-03-20`). Consistent drift across all three .md files in this set; not a staleness issue per se, but worth noting that the filename reflects the discovery-call date while the header reflects the document-prep date. **Severity: LOW** (naming convention issue, not a factual one).

2. **Line 49, "...may include customer names, fab identifiers, or other sensitive information."** — In context this reads as a general list of what escalation content might contain, which is accurate. Not flagged. (Included for reader clarity: the document does acknowledge fab identifiers as sensitive; the "initial scope" statement below is the one that's now inverted.)

3. **Line 83, "The initial target scope is narrow: customer name and file name. If detection and redaction cannot be made reliable for these two fields, there is no basis for expanding to harder cases."** — STALE. Current canonical scope is **customer name and fab identifier** as the two entity types. "File name" was an early-discovery shorthand but the POC as scoped targets customer names + fab identifiers across five free-text fields in the Escalation Solver application. A reader coming to this document today would be misled about what BayOne agreed to detect. **Severity: HIGH** (misrepresents current scope, and this is a client-facing doc in the deliverables folder).

4. **Line 183, "The initial proof of concept scope is narrow: demonstrate reliable detection and handling of customer names and file names."** — STALE. Same issue as #3, repeated in the Desired Outcome section. **Severity: HIGH**.

5. **Line 104, "Detection only, no redaction at this stage. The system identifies and flags; it does not modify content."** — This framing is specific to Use Case 2 (the real-time entry notification) and was accurate framing for the discovery understanding. However, as of the POC as scoped, the engagement is narrower still — detection demonstration only on the Escalation Solver, and the "two use cases" framing has been collapsed into a single application POC. Not strictly wrong, but the Use Case 1 / Use Case 2 framing throughout this file is no longer the operative structure of the engagement. **Severity: MEDIUM** (framing drift).

6. **Line 124-135, Machine Learning Models section** — Describes three models as "Transformers-based model, SpaCy, an Azure AI model." Canonical now is **spaCy, Flair, and an Azure AI model**, narrowed from an originally larger set of ~12 Presidio models. The "Transformers-based model" label was how it was understood from the first call, but subsequent sessions clarified the Flair identity and the Presidio lineage. **Severity: MEDIUM** (factually imprecise about Lam's prior work; defensible at time of writing; no longer accurate).

7. **Line 125, "Three models were trained using an MLOps pipeline deployed on Azure Cloud"** — The MLOps-pipeline framing is accurate; the framing that misses context is that these three were narrowed from ~12 Presidio models originally. Not wrong, but incomplete versus what BayOne now knows. **Severity: LOW**.

8. **Line 146, "Generative AI approaches have not been attempted."** — Still current as a claim about Lam's prior work per canonical. **Not stale.**

9. **Lines 79-80, Fab identifiers listed among sensitive info, but not called out as one of the initial POC targets** — At line 83 the initial target is stated as "customer name and file name," excluding fab identifiers from the narrow scope. This is the central drift in the document. **See #3. Severity: HIGH**.

### Recommendation

ARCHIVE AS HISTORICAL — Move this file (with its .html counterpart) to a `deliverables/archive/` or `deliverables/discovery_march_2026/` subfolder and add a short README noting these artifacts predate the scoped POC and should not be used as a source of truth on scope or methodology. Alternative: UPDATE IN PLACE to correct the two "customer names and file names" lines to "customer names and fab identifiers" with a header note that this was the March 12 discovery understanding. The archive path is cleaner because multiple framings in this doc (Use Case 1 / Use Case 2 split, Transformers model label) have moved on.

---

## File: problem_restatement_2026-03-12.html

**Role:** Client-facing rendered deliverable
**Matches .md/.html counterpart?** Partial — see .md entry above. Substance aligned; rendered version omits the Use Case 2 "False positive sensitivity is critical" sub-bullet content from the characteristics list (moves it into a highlight-box), drops the "big brother" phrasing, and reshapes the what-has-been-tried narrative into a table. Line 540 substitutes "one customer's context... a different customer's problem" for the .md's "Samsung context may be entirely applicable to an Intel problem" — a stylistic softening of named customers, arguably an improvement, but a drift between versions.
**Status:** MIXED — same staleness as .md counterpart.

### Discrepancies Found

1. **Line 444, "Date: March 2026"** — Cover page shows "March 2026" where .md shows "2026-03-20." Minor inconsistency; both are historically accurate for a March 20 production date. **Severity: LOW**.

2. **Line 586, "The initial target scope is narrow: customer name and file name."** — STALE. Same as discrepancy #3 in the .md file. **Severity: HIGH**.

3. **Line 731 (inside highlight-box), "Demonstrate reliable detection and handling of customer names and file names."** — STALE. Same as discrepancy #4 in the .md file. **Severity: HIGH**.

4. **Line 540, "A solution that originated in one customer's context may be entirely applicable to a different customer's problem"** — Drifts from the .md's "A solution that originated in a Samsung context may be entirely applicable to an Intel problem." Not staleness; .md ↔ .html drift. Arguably the HTML version is an improvement (less risky to name competitor customers in a client-facing deliverable), but the two versions should match. **Severity: LOW** (consistency).

5. **Lines 642-655, Machine Learning Models table** — Lists "Transformers-based model, SpaCy, Azure AI model." Same issue as .md #6. Canonical prior models are now known to be spaCy, Flair, Azure AI, narrowed from ~12 Presidio. **Severity: MEDIUM**.

6. **Line 710, "Enforced at the customer level in the ticketing system. Employees assigned to one customer see only that customer's tickets. Cross-visibility is blocked."** — .md version (line 167) names specific customers ("Lam employees assigned to Micron see Micron tickets; those assigned to Samsung see Samsung tickets"); HTML generalizes. Consistency drift but HTML softening is defensible. **Severity: LOW**.

### Recommendation

ARCHIVE AS HISTORICAL — move with the .md.

---

## File: preliminary_approach_2026-03-12.md

**Role:** Client-facing (source markdown for rendered HTML deliverable)
**Matches .md/.html counterpart?** Partial — HTML drops one paragraph from section 2 ("Additionally, the separation between detection and redaction..."), turning it into a highlight callout; drops section 4 workflow into a visual step-grid; otherwise substance-aligned.
**Status:** MIXED — high framing drift from current methodology, though explicitly labeled "preliminary."

### Discrepancies Found

1. **Line 19, "Prior attempts using custom ML models (Transformers, SpaCy, Azure AI) produced false positive rates around 20%"** — STALE. Canonical model list is now spaCy, Flair, Azure AI (narrowed from ~12 Presidio). "Transformers" is a mislabel. **Severity: MEDIUM**.

2. **Entire section 3 ("Proposed Approach: Hybrid Architecture"), lines 33-59** — Presents a **two-layer hybrid** (Deterministic + AI-based classification). Current canonical methodology is a **three-layer sequential** approach: deterministic → ML/NLP → Generative AI. The March 12 document collapses ML/NLP and Generative AI into a single "AI-based classification layer" and positions it as parallel-ish to the deterministic layer rather than as sequential escalation. The word "hybrid" is also now off-brand for how BayOne is describing the approach. **Severity: HIGH** — any Lam reader returning to this document will form a wrong mental model of what BayOne is doing.

3. **Line 58, "Deterministic matching gives a false positive rate of zero on known patterns. AI classification handles the contextual gray areas."** — Implies two layers, parallel operation. Canonical is three layers, sequential. **Severity: HIGH** (same as #2).

4. **Section 4 ("Ingestion-First Architecture"), lines 63-81** — Entire section frames the solution as an ingestion-time pipeline that blocks or cleans content as it enters the system. The current POC is a **detection demonstration on an existing corpus** inside Lam's environment; there is no ingestion pipeline component, no real-time gating, no architecture commitment of this shape. This was legitimate preliminary thinking at discovery; it is now misleading about what BayOne is delivering. **Severity: HIGH**.

5. **Section 5 ("Unified Data Plane"), lines 85-103** — Describes a unified data plane built on Azure-native services, centralized ingestion pipeline, credential/access management, etc. None of this is in the POC scope. This is entirely forward-looking architecture framing that has not been committed. **Severity: HIGH** — in a deliverables folder, this reads like a commitment.

6. **Line 97, "The recommended starting point is Azure-native services (Blob Storage for documents, a vector database for search embeddings, Azure AI Foundry for AI model hosting)"** — Now inverted by Option A election on 2026-04-16. BayOne will execute **in Lam's environment**, not on Azure-native BayOne infrastructure. The Azure-first framing is stale. **Severity: HIGH**.

7. **Section 6 ("Historical Data Cleanup"), lines 107-123** — Describes an application-by-application historical cleanup approach. The POC is a single-application detection demonstration on the Escalation Solver; there is no historical cleanup commitment. **Severity: MEDIUM** (preliminary section, but still presents as an approach).

8. **Section 7 ("Enterprise Tools Strategy") — Microsoft Purview, Azure AI Foundry, lines 127-141** — Recommends Purview and Azure AI Foundry as foundations. Not part of the POC. **Severity: MEDIUM** (preliminary framing, but branded as recommendation).

9. **Line 137, "Even applications that are hosted on-premises can leverage Azure AI Foundry APIs for processing, decoupling the AI compute from the application deployment model."** — Directly contradicts the Option A election where execution is in Lam's environment, not split across Lam-on-prem + Azure-hosted AI. **Severity: MEDIUM**.

10. **Line 151, "Identification of the first target application for the proof of concept"** — Now resolved: Escalation Solver. Fine to remain as a historical "what we needed next" item; not stale in context. **Severity: LOW** (intended preliminary).

11. **No mention anywhere of price, timeline, or duration** — this is correct for a March 12 pre-scoping doc; not a drift. **Not flagged**.

### Recommendation

ARCHIVE AS HISTORICAL — The entire approach document has been superseded. The POC is not a hybrid two-layer ingestion pipeline on Azure; it is a three-layer sequential detection demonstration in Lam's environment. Leaving this in the active deliverables folder is actively misleading. Archive with a clear README indicating it is superseded by the research library's methodology document(s) and the POC SOW.

---

## File: preliminary_approach_2026-03-12.html

**Role:** Client-facing rendered deliverable
**Matches .md/.html counterpart?** Yes, substantively — minor rendering differences (tables vs prose, callouts vs inline) but no content drift beyond the .md.
**Status:** STALE — same issues as .md.

### Discrepancies Found

1. **Line 449, "Prior attempts using custom ML models (Transformers, SpaCy, Azure AI)"** — Same as .md #1. **Severity: MEDIUM**.

2. **Lines 465-493, Hybrid Architecture section with two-card layout (Deterministic Layer / AI Classification Layer)** — Same as .md #2 and #3. Presents two-layer parallel, not three-layer sequential. **Severity: HIGH**.

3. **Lines 496-532, Ingestion-First Architecture section** — Same as .md #4. Depicts an ingestion pipeline that is not what BayOne is delivering. **Severity: HIGH**.

4. **Lines 534-571, Unified Data Plane section** — Same as .md #5. **Severity: HIGH**.

5. **Line 566, "Azure-native services (Blob Storage for documents, a vector database for search embeddings, Azure AI Foundry for AI model hosting)"** — Same as .md #6. Inverted by Option A election. **Severity: HIGH**.

6. **Lines 573-593, Historical Data Cleanup section** — Same as .md #7. **Severity: MEDIUM**.

7. **Lines 595-624, Enterprise Tools Strategy** — Same as .md #8. **Severity: MEDIUM**.

8. **Line 614, "Applications hosted on-premises can leverage Azure AI Foundry APIs for processing, decoupling the AI compute from the application deployment model"** — Same as .md #9. Directly contradicts Option A. **Severity: MEDIUM**.

9. **Line 435, "Date: March 2026"** — Consistency with filename `_2026-03-12`; minor. **Severity: LOW**.

### Recommendation

ARCHIVE AS HISTORICAL — move with the .md. This is the rendered PDF-class deliverable and is even more consequential than the .md if it ends up in a client inbox.

---

## File: information_request_2026-03-12.md

**Role:** Client-facing (source markdown)
**Matches .md/.html counterpart?** No — see details below. HTML version has meaningful structural and content drift from the .md.
**Status:** MIXED — expected pre-scoping info request; contains one factual claim that is now inverted.

### Discrepancies Found

1. **Line 4, "Date: 2026-03-20"** — Header vs filename date drift. **Severity: LOW**.

2. **Line 56, "During the discovery session, the team described customer names and file names as the initial target fields."** — STALE as a factual claim today, and also worth noting: even at time of writing this was an imperfect reflection of the discovery — fab identifiers were discussed as a sensitive category. The current canonical initial scope is customer names + fab identifiers. **Severity: HIGH** if anyone reads this doc today as a source of truth; the doc was asking Lam to confirm, so as a historical request-for-confirmation it's defensible, but a read-today interpretation would mislead. Critical because the sibling documents (problem_restatement) embed this same error and propagate it.

3. **Line 67, "We understand that multiple ML-based approaches have been tried (Transformers, SpaCy, an Azure AI model)"** — Stale model label. Canonical: spaCy, Flair, Azure AI. **Severity: MEDIUM**.

4. **Entire document structure** — This is an information request that was largely answered by the April 6 discovery session and subsequent exchanges. As a historical artifact it is internally consistent; as an active deliverable it is obsolete because the information requested has been gathered. **Severity: MEDIUM** (whole-document obsolescence, not line-level staleness).

5. **HTML counterpart has meaningful divergence** — In the .md, Priority 1 contains only "1.1 Identify One Application" and Priority 2 contains "2.1 Representative Data Samples" through "2.6 The 2-5 Seconds Requirement." The HTML restructures Priority 1 to include **both** "1.1 Identify One Application" AND "1.2 Representative Data Samples" — and then repeats "2.1 Representative Data Samples" inside Priority 2 with the same content. This is a **duplicated ask** in the HTML that does not exist in the .md. See HTML entry below for details. **Severity: MEDIUM** (.md/.html consistency issue).

### Recommendation

ARCHIVE AS HISTORICAL — The questions have been answered; the document's purpose is served. Move to an archive subfolder alongside the other March 12 artifacts.

---

## File: information_request_2026-03-12.html

**Role:** Client-facing rendered deliverable
**Matches .md/.html counterpart?** NO — partial duplication issue (see below). Substance largely aligned on questions asked, but the HTML has a structural difference that looks like a generation error or an intentional edit that wasn't back-ported to .md.
**Status:** MIXED.

### Discrepancies Found

1. **Line 485, "Date: March 2026"** — Consistency with .md date. **Severity: LOW**.

2. **Lines 521-546 (Priority 1) vs Lines 562-572 (Priority 2.1)** — "Representative Data Samples" appears **twice**: once as Priority 1 item 1.2 and once as Priority 2 item 2.1, with nearly identical text. The .md only has this in Priority 2 (as 2.1). This is a duplication that needs one copy removed. **Severity: MEDIUM** (structural issue; client-facing).

3. **Line 576, "During the discovery session, the team described customer names and file names as the initial target fields."** — STALE, same as .md #2. **Severity: HIGH**.

4. **Line 588, "multiple ML-based approaches have been tried (Transformers, SpaCy, an Azure AI model)"** — Same stale model label as .md #3. **Severity: MEDIUM**.

5. **Lines 697-712, Summary table of priorities and responders** — This summary table is present in the HTML but not in the .md. Not staleness; .md/.html drift. **Severity: LOW**.

6. **Lines 697-712, Priority "3" in the summary table is the working session** — Consistent with Priority 3 section; fine.

### Recommendation

ARCHIVE AS HISTORICAL — move with the .md. If kept active for any reason, the duplicated 1.2/2.1 section needs to be reconciled and the "customer names and file names" line needs correction.

---

## File: followup_email_draft_2026-03-12.md

**Role:** Internal draft (email to be sent by Colin to Brad/Mikhail; never sent in this exact form given subsequent session cadence)
**Matches .md/.html counterpart?** N/A (no HTML counterpart)
**Status:** MIXED — accurate for its moment, obsolete as a live artifact.

### Discrepancies Found

1. **Line 3, "To: Bradley Estes, Mikhail Krivenko"** — Bradley Estes is consistent with "Brad Estes" elsewhere; Brad's full name in canonical is "Brad Estes, Managing Director." The email draft does not include titles, which is fine for an email draft. **Not flagged**.

2. **Line 4, "From: Colin Moore"** — Consistent with canonical (Director of AI, BayOne). **Not flagged**.

3. **Line 15-18, "I have attached two documents for your review: 1. Balancing IP Protection with Productivity at Scale ... 2. Next Steps and Discovery"** — Attachments reference the two client-facing deliverables in this set. Both are now being recommended for archival; if the email were sent today it would be attaching superseded material. **Severity: MEDIUM** (cascading obsolescence — the email is only as current as what it attaches).

4. **Line 20, "...the most important first step is identifying the specific application or system that would serve as the starting point for an initial proof of concept."** — This ask has since been answered (Escalation Solver selected). **Severity: MEDIUM** (obsolete as an ask).

5. **Line 22, "Based on our conversation, we have a clear sense of the methodology and can speak to the approach at a high level"** — At time of writing this was accurate; today BayOne has a fully articulated methodology and a priced, scoped POC. Not a factual error, just dated framing. **Severity: LOW**.

6. **Line 24, "...we will be in a position to fully scope the engagement and deliver a formal proposal."** — This has happened; the POC is scoped and priced. Email is superseded by actual events. **Severity: MEDIUM** (whole-document obsolescence).

7. **No pricing, no timeline, no Anuj reference** — Appropriate for a March 12 pre-scoping email. Not flagged.

### Recommendation

ARCHIVE AS HISTORICAL — This is a draft that was not sent (or that has been superseded by actual communication with Brad and Mikhail). Move to the same archive location as the other March 12 artifacts. No value in keeping it in active `deliverables/`.

---

## Summary

| File | Status | Recommendation |
| --- | --- | --- |
| problem_restatement_2026-03-12.md | MIXED | ARCHIVE AS HISTORICAL |
| problem_restatement_2026-03-12.html | MIXED | ARCHIVE AS HISTORICAL |
| preliminary_approach_2026-03-12.md | STALE | ARCHIVE AS HISTORICAL |
| preliminary_approach_2026-03-12.html | STALE | ARCHIVE AS HISTORICAL |
| information_request_2026-03-12.md | MIXED | ARCHIVE AS HISTORICAL |
| information_request_2026-03-12.html | MIXED | ARCHIVE AS HISTORICAL |
| followup_email_draft_2026-03-12.md | MIXED | ARCHIVE AS HISTORICAL |

**Observations across the file set:**

Four cross-file patterns stand out.

**(1) Initial-scope error is propagated consistently.** Every March 12 document that talks about the narrow starting scope describes it as "customer names and file names." The canonical scope as negotiated and committed is customer names and fab identifiers. This is the single most load-bearing staleness pattern in the set because it sits in client-facing language in the deliverables folder. The error is consistent (not a typo in one place) and appears at least five times across the three client-facing deliverable pairs. Even at time of writing this was an imperfect capture — fab identifiers were discussed in discovery as a sensitive category and are listed as sensitive info in the problem restatement, but the initial-scope statement excludes them and names file names instead. That March 12 formulation never should have been the scope anchor, and it is definitively not the scope today.

**(2) Prior-effort model list uses the early "Transformers" label.** All four documents that reference prior ML work cite the three models as "Transformers, SpaCy, Azure AI." Canonical now is spaCy, Flair, and an Azure AI model, narrowed from an originally larger Presidio-based set (~12 models). The "Transformers" label was an honest misread from the first discovery call and has since been corrected. In isolation, each occurrence is a medium-severity factual slip; collectively it suggests that any downstream doc citing the March 12 artifacts as a source would inherit the error.

**(3) The preliminary_approach pair is the most actively misleading.** It presents a two-layer hybrid (deterministic + AI) architecture, an ingestion-first pipeline, a unified data plane on Azure-native services, an application-by-application historical cleanup program, and recommendations for Microsoft Purview and Azure AI Foundry — **none** of which is what BayOne is delivering. The current POC is a three-layer sequential detection demonstration (deterministic → ML/NLP → GenAI) on existing Escalation Solver data, running **in Lam's environment** (Option A, elected 2026-04-16), with none of the unified-data-plane or ingestion-pipeline framing committed. Every section 3 onward in the preliminary_approach document drifts from current reality. This pair should be archived with a clear "superseded" marker; leaving it in `deliverables/` invites a Lam reader to assume BayOne is committing to an Azure-hosted, ingestion-first, unified-data-plane architecture.

**(4) .md ↔ .html drift is present in two of three pairs.** The problem_restatement pair has minor stylistic drift (named competitor customers in .md, generalized in .html; some prose vs. table differences). The information_request pair has a structural duplication in the HTML — "Representative Data Samples" appears as both 1.2 and 2.1 in the HTML while only existing as 2.1 in the .md. That's a real defect that was never reconciled. The preliminary_approach pair is clean on .md/.html consistency.

**Net recommendation for the set:** All seven files should be moved to a `deliverables/archive/discovery_march_2026/` subfolder (or similar), with a short README noting that these are March 12 discovery artifacts, that they predate the April 6 scoping session and the Option A election of April 16, and that the current source of truth for methodology and scope is the POC SOW and the research library. None of these files should be edited in place to "fix" them — the simpler and safer move is to move them out of the active `deliverables/` namespace so they cannot be mistaken for current commitments. If Colin wants a March 20 snapshot preserved for narrative/history purposes, archival achieves that without the drift risk.
