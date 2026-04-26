# Technology Access Request List — Lam Research IP Protection POC

**Date:** 2026-04-20 (revised)
**Purpose:** The specific access BayOne needs Lam to provision for the POC to begin. This is the distilled answer to Mikhail Krivenko's 2026-04-16 question: "What specific technologies would you need access to?"
**Scope note:** This list only contains items that Lam must set up, grant, or provide. Items that are obvious for any engineering work (runtimes, package managers, IDEs, model weight downloads) are not included because they are not things Lam needs to provision. Narrower provisioning items will be raised with Daniel Harrison as they surface.

---

## 1. Environment Access

- **The ability to reach the files, data, systems, and locations where the work lives.** Whatever mechanism Lam uses to give outside consultants working access to the Escalation Solver data, reference materials, and the POC workspace — that mechanism needs to be opened up to BayOne. This is the foundational ask.
- Hardware acceptable to Lam's standards for BayOne to perform the work on. Specifics to be agreed with Lam IT.
- **Access to any artifacts still present in Azure from the prior 18-month effort** — code, notebooks, models, labeled data, evaluation scripts, retained outputs, or anything else the prior project left behind. We will review whatever survives and reuse what applies. This grounds the benchmark commitment against the prior baseline and saves meaningful time in Phase 1.

---

## 2. Data Access

- Escalation Solver export: the five free-text fields, representative sample across ticket types (minimum ~1,000 tickets; ideal ~20,000)
- Customer name reference list (authoritative, with known variations)
- Fab / location identifier reference list (with known variations: Fab 11, F11, Micro 11, FAP 11, FAP-11, etc.)
- Exclusion list (content or acronyms approved for general sharing)
- Lam acronyms list (~3,000 items) with the authoritative source / owner
- Thumbs-up / thumbs-down feedback labels (~1,000 items from the existing UI)
- Prior-effort baseline documentation: results, model selection history, target performance aims, baseline metrics (21% / 17% false-positive rate, ~90% accuracy)
- Real false-positive examples from prior testing, if retained
- Any contractual or regulatory constraints on handling this data that BayOne needs to know about upfront

---

## 3. Source Control

- Provisioning of a **GitHub or Azure DevOps** repo on Lam's instance, whichever is preferred. BayOne recommends persisting POC code inside Lam's environment alongside the data and artifacts.

---

## 4. Generative AI Endpoint

- Access to **Azure AI Foundry** (ideal — it represents the true future state, is the most scalable option, and is the most cost-effective path), or a comparable Lam-sanctioned language model endpoint.
- This must be an **actual model endpoint**, not generic access to a packaged tool. **Microsoft Copilot and GitHub Copilot are not sufficient** for this work — the methodology requires programmatic access to a language model for the generative AI layer of the detection pipeline.
- If Lam does not currently have a sanctioned endpoint provisioned, BayOne can support Lam in provisioning one as part of the POC setup.

---

## 5. Containerization Tooling

- Lam's preferred containerization tooling — **Docker, Podman, or other**. We would like to know the standard on Lam's systems so that POC work fits Lam's operational patterns rather than introducing something Lam would have to accommodate.

---

## 6. Identity / Accounts

- Two LAM ID accounts for BayOne consultants:
  - Colin Moore (Director of AI, BayOne Solutions)
  - One onshore BayOne engineer (name to follow)
- Confirmation in passing that the existing BayOne–Lam NDA covers the POC scope, or that a supplemental is needed.

---

## 7. Subject Matter Expert Coverage

The engagement needs SME coverage sufficient to fully satisfy the following responsibilities. It may be one person who does all of it, or several people who collectively cover it. It must not be a partial fit — any gap directly affects the Phase 1 Detection Target Map deliverable and the Phase 2 validation results.

The SME function must be able to:

- **Define detection targets** — what specifically counts as a customer name, a fab identifier, and each of their accepted variations and edge cases.
- **Adjudicate ambiguity** — confirm what constitutes a true positive vs. a false positive when the content is unclear, borderline, or context-dependent.
- **Validate detection results** — review a representative sample of BayOne's Phase 2 output and confirm or correct the accuracy labels.
- **Speak to the authoritative sources** — know where the reference lists (customer names, fab identifiers, acronyms, exclusion list) come from, how they are maintained, and who owns them.
- **Anchor prior-effort context** — understand what the prior 18-month detection effort was trying to do, what worked, what did not, and why the baseline metrics landed where they did.
- **Be available during the POC window** — responsive within an agreed turnaround during the three-week engagement, including during the Phase 2 validation cycles.

---

## 8. Communication

- Lam's preference for engagement communications — Slack, Teams, or other.
