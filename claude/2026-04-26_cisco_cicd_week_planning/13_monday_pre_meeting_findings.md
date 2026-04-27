# Monday Pre-Meeting Findings — Implications for Today's Srinivas Sync

**Source:** `cisco/cicd/team/source/week_2026-04-27/day_2026-04-27/cicd-team-monday-pre-meeting_01.txt`
**Date:** 2026-04-27 Monday morning (before the 1 PM Srinivas sync)
**Purpose:** Extract blockers and clarifications surfaced in the BayOne pre-meeting and propose Document A changes before the Srinivas sync.

---

## A. New blockers surfaced (not in v3 of the doc)

### A1. WebEx bot non-compliance email this morning

Saurav received an email today indicating the current bot is flagged as non-compliant. Mahaveer was on CC. The compliance criteria have not been shared with BayOne. The audit and approval timeline is not known.

**Implication:** The v3 row "Cisco IT registration approved" is FALSE. Registration is not approved; the bot is currently non-compliant. The row needs a substantive rewrite, and the compliance gap surfaces as a critical-path blocker.

### A2. WebEx bot deployment under individual user IDs is not viable

Saurav: "I deployed that from my saurmi at-rate Cisco ID... if tomorrow saurmi at-rate Cisco is down for some reason... that whole thing, the bot, the registry itself will be gone."

**Implication:** The bot needs a service account or centralized deployment ID owned by Cisco. This is a Cisco-side dependency BayOne cannot resolve unilaterally. Critical-path blocker.

### A3. WebEx bot deployment requires multiple Cisco-issued items beyond the container

Saurav enumerated: bot name, bot ID, access token, compliance audit and approval, channel-deployment registration, and the host environment (which loops back to the ADS dependency).

**Implication:** The current v3 framing of "Podman container build and LLM credential wiring are the remaining deployment steps" is incomplete and understates the gating items. Critical-path blocker.

### A4. CAT MCP querying needs a PR ID to CAT ID mapping

Srikar: chat issues arrive with PR IDs, the CAT MCP requires CAT IDs to query, so a mapping table is needed for the dynamic path to function end to end. Srikar built a placeholder skill structure (NxOS-Issue-Responder) with four tool placeholders and a CAT MCP placeholder that captures this design.

**Implication:** Whether the mapping exists on the Cisco side or BayOne is expected to construct it is currently unclear. Clarification needed from Srinivas.

### A5. Language model access path beyond DeepSight is unconfirmed

Colin in the pre-meeting: "Even if we spin up DeepSight, even if we get the ADS machine, do we then have language model access? Or what is the path to that? That is a critical thing because that gates pretty much every item on this sheet."

**Implication:** The v3 doc currently treats DeepSight credentials as the path to LLM access. The transcript surfaces that even with DeepSight in place, language model access is not confirmed. Critical-path blocker, needs explicit clarification today.

---

## B. Skills inventory update (delivered during the pre-meeting itself)

Srikar pushed two skills to the webex-skills branch during the call:

1. **NxOS-Issue-Categorizer** (already named in the prior inventory).
2. **NxOS-Issue-Responder** (NEW). Contains four tool placeholders and a CAT MCP placeholder. Carries the design for the PR ID to CAT ID mapping (per A4 above) and the dynamic-answer path.

Combined with the previously named WebEx-Bot-Builder and WebEx-Solution-Architect, the inventory is now four skills on the CI/CD repository.

**Implication:** The Skills row in v3 says three skills committed. Update to four. Inventory documentation this week now covers four skills.

---

## C. Repository destination working decision

Saurav and Colin landed a working approach: keep skills on the CI/CD repository / webex-skills branch during development; promote to the master skills repository only after testing and verification. Colin will frame this to Srinivas today.

**Implication:** This was on the prior session's open list as ambiguous. Working decision exists pending Srinivas confirmation. Belongs in the critical-path-clarifications section as a confirmation request, not in the general open items table.

---

## D. ADS situation reframed with sharper language

Colin's pre-meeting framing: "How the heck is Mahavir supposed to provision something of which he has none? So that's where I'm going to raise that today as, you know, that's on you guys. That's not on us anymore."

The Permanent ADS situation is not a BayOne work item; it is a Cisco-side resource constraint. The v3 doc captures this in the Open items table. The Critical path section can sharpen the ask: "Will Permanent ADS be available in the Friday window, or does the first deployment land on Temp ADS with Permanent ADS migration as a follow-on?"

The pre-meeting also surfaced a hard line: if Permanent ADS is the requirement, it must be ready by tomorrow or the deliverable is not feasible this week. That hard line goes in the internal record, not on the Cisco-facing doc, but it informs the Critical path section's framing.

---

## E. Build dependency graph timing

The pre-meeting confirmed that Namita's research on the new mapping framework should finish today. The dependency graph deliverable itself is not a Friday deliverable; it is ongoing work that will boost the rest of the project. Once research finishes, Namita pivots to help with CAT MCP wiring and bot deployment.

**Implication:** No change needed to Document A. The current row reads correctly. The pivot of Namita's time is an internal allocation decision and stays internal.

---

## F. Proposed Document A changes

### F1. New section: Critical path blockers and clarifications needed

Placement: between Current work and Open items and access. Visible early because urgent. Direct, factual, not finger-pointing. Each item names what we need from the Cisco side.

```
## Critical path blockers and clarifications needed

The items below are on the critical path for Friday's first deployment. Each needs clarification or unblocking from the Cisco side so the team can complete the work in the available window.

1. **Permanent ADS availability.** Permanent ADS resources were noted as currently constrained on the Cisco side on April 24. Clarification requested: will Permanent ADS be available within the Friday window, or does the first deployment land on Temp ADS with Permanent ADS migration as a follow-on?

2. **Language model access path.** Language model features require credentials. Circuit API was indicated as not the appropriate production path. DeepSight credentials are gated on the team operating from an ADS environment. Even with ADS and DeepSight in place, the language model access path is not yet confirmed. Clarification requested: what is the language model access path for the Friday deployment, and is interim Circuit API use acceptable until the production path is in place?

3. **WebEx bot deployment infrastructure.** The bot backend is built. Deployment requires items that sit with Cisco: a service account or centralized deployment ID (deployment under an individual user account creates continuity risk if a team member rolls off), the bot name and bot ID, the access token, the WebEx bot compliance criteria, and the IT audit and approval. An email this morning indicated the current bot is flagged as non-compliant. Clarification requested: the compliance criteria, the audit and approval timeline, and the Cisco-side ID under which the deployed bot will run.

4. **CAT MCP querying mechanism.** Chat issues arrive with PR IDs. The CAT MCP requires CAT IDs to query. A PR-to-CAT mapping is required for the dynamic answer path to function end to end. Clarification requested: does this mapping exist on the Cisco side, or is BayOne expected to construct it as part of the integration?

5. **Skills repository destination.** Earlier guidance pointed to two destinations (the main CI/CD repository and the master skills repository). Working approach is to keep skills on the CI/CD repository during development and promote to the master skills repository after testing and verification. Confirmation requested.
```

### F2. WebEx bot row in Current work — rewrite

Current (incorrect):

> Bot built and validated locally. Cisco IT registration approved. Deployment to Temp ADS this week. Podman container build and LLM credential wiring are the remaining deployment steps.

Proposed replacement:

> Bot backend built and validated locally. Deployment requires a Cisco-side service account or centralized deployment ID, bot name and bot ID, access token, WebEx bot compliance criteria, IT audit and approval (current bot was flagged as non-compliant April 27), the ADS environment, and language model access. See Critical path blockers and clarifications needed.

Dependencies cell stays as: ADS environment access. LLM credential path through DeepSight. (Or expanded to: ADS environment access. LLM credential path. Cisco-side deployment infrastructure for the bot.)

### F3. Skills row in Current work — update count

Current:

> Three skills committed: NxOS-Issue-Categorizer, WebEx-Bot-Builder, WebEx-Solution-Architect.

Proposed:

> Four skills committed: NxOS-Issue-Categorizer, NxOS-Issue-Responder, WebEx-Bot-Builder, WebEx-Solution-Architect.

### F4. Optional: tighten Static FAQ wiring row

Could add reference to the categorizer skill's static mapping output being the source for the FAQ. Current wording is acceptable; no change required unless Colin wants tighter framing.

---

## G. Items NOT for Document A (kept internal)

- Internal frustration framing ("loaded cannon not aiming anywhere")
- "Be deliberately annoying" communication strategy
- Hard line on Permanent ADS by tomorrow or deliverable infeasible
- Specific named individuals on the Cisco side (Mahaveer, Anand, etc.) on a Cisco-visible artifact
- Internal allocation decisions (Namita pivoting to CAT MCP support after research finishes)
- Cisco-internal political observations (Srinivas's organizational disorganization)

These stay in the team meeting transcript and the internal week tracker. They do not surface on Document A.
