**To:** Daniel Harrison
**Cc:** Mikhail Krivenko; (optional) Anuj Sehgal, Pratik Sharda
**Subject:** Lam Research IP Detection POC: Technology Access Coordination

---

Hi Daniel,

Mikhail asked me to reach out to you to work through the technology access needs for the Lam Research IP Detection POC. Looking forward to working together on this.

The POC is structured as a three-week engagement, starting no earlier than the week of May 4, 2026, and executed in Lam's environment. Before the three-week clock starts, we need the access and tooling set up so the engagement begins with everything already in hand.

Here is the full list of what we need provisioned or confirmed from Lam's side. Some items may already be straightforward under Lam's standard contractor onboarding. Others may need conversations with the relevant system owners.

### Environment Access

- The ability to reach the files, data, systems, and locations where the work will happen. Whatever mechanism Lam uses to give outside consultants working access to the Escalation Solver data, reference materials, and the POC workspace is what we need opened up.
- Hardware acceptable to Lam's standards for us to perform the work on. Specifics to be agreed with Lam IT.
- Access to any artifacts still present in Azure from the prior 18-month effort. Code, notebooks, models, labeled data, evaluation scripts, retained outputs, or anything else the prior project left behind. Whatever survives, we can review and reuse what applies. This grounds the benchmark commitment against the prior baseline and saves meaningful time in Phase 1.

### Data Access

- Escalation Solver export: the five free-text fields, representative sample across ticket types (minimum approximately 1,000 tickets, ideal approximately 20,000)
- Customer name reference list (authoritative, with known variations)
- Fab and location identifier reference list (with known variations)
- Exclusion list (content or acronyms approved for general sharing)
- Lam acronyms list (approximately 3,000 items) with the authoritative source or owner
- Thumbs-up / thumbs-down feedback labels (approximately 1,000 items from the existing UI)
- Prior-effort baseline documentation: results, model selection history, target performance aims, baseline metrics
- Real false-positive examples from prior testing, if retained
- Any contractual or regulatory constraints on handling this data that we should know about upfront

### Source Control

- A GitHub or Azure DevOps repository on Lam's instance, whichever is preferred. We recommend persisting POC code inside Lam's environment alongside the data and artifacts.

### Generative AI Endpoint

- Access to Azure AI Foundry (ideal. It represents the future state, is the most scalable option, and is the most cost-effective path), or a comparable Lam-sanctioned language model endpoint.
- This needs to be an actual model endpoint, not generic access to a packaged tool. Microsoft Copilot and GitHub Copilot are not sufficient for this work. The methodology requires programmatic access to a language model for the generative AI layer of the detection pipeline.
- If Lam does not currently have a sanctioned endpoint provisioned, BayOne can support provisioning one as part of the POC setup.

### Containerization Tooling

- Lam's preferred containerization tooling (Docker, Podman, or other). We would like to know the standard on Lam's systems so our work fits your operational patterns.

### Identity and Accounts

- Two LAM ID accounts for BayOne consultants: Colin Moore (Director of AI) and one onshore BayOne engineer (name to follow).
- Confirmation that the existing BayOne and Lam NDA covers the POC scope, or that a supplemental is needed.

### Subject Matter Expert Coverage

The engagement needs SME coverage sufficient to fully satisfy the responsibilities below. It may be one person or several, and it must not be a partial fit. The SME function needs to be able to:

- Define detection targets (what specifically counts as a customer name, a fab identifier, and each of their accepted variations and edge cases)
- Adjudicate ambiguity (confirm true positive versus false positive when content is unclear, borderline, or context-dependent)
- Validate detection results (review a representative sample of Phase 2 output and confirm or correct the accuracy labels)
- Speak to the authoritative sources (know where the reference lists come from, how they are maintained, and who owns them)
- Anchor prior-effort context (understand what the prior 18-month detection effort was trying to do, what worked, what did not, and why)
- Be available during the POC window (responsive within an agreed turnaround during the three-week engagement, including Phase 2 validation cycles)

### Communication

- Lam's preferred channel for engagement communications (Slack, Teams, or other)

---

Could we set up a 30-minute working session to walk through these? I am flexible on timing and happy to work around your calendar. Happy to send a couple of time options, or you can send me yours.

If any items above are already straightforward under Lam's standard contractor onboarding, let me know and we can drop them from our tracking. My main concern is making sure nothing becomes a surprise blocker once the POC clock starts.

Best,
Colin Moore
Director of AI
BayOne Solutions
