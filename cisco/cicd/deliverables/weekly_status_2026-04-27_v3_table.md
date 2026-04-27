# Cisco CI/CD AI Engagement Weekly Status

**Week of April 27 to May 1, 2026**

---

## Current work

| Workstream | Status | Dependencies |
|---|---|---|
| CI/CD application on ADS | Cisco-side deployment in flight per Friday's discussion. BayOne fallback on Temp ADS ready. | Cisco platform team deployment. Temp ADS provisioning if fallback path. |
| Backend (Service Application Platform style, two pluggable frontends) | Architecture in flight. Backend designed to feed the chat in the CI/CD application and the WebEx bot on the NX-OS CI pipeline from one shared source. | None blocking. |
| Static FAQ wiring | Source corpus identified. Extraction starts this week. | Backend availability. |
| CAT MCP dynamic answer path | Installed. Four tools identified. OAuth resolved. Live execution begins after team sign-on completes. | Each BayOne team member completes first sign-on to the NX GitHub server. |
| WebEx bot deployment on the NX-OS CI pipeline | Bot built and validated locally. Cisco IT registration approved. Deployment to Temp ADS this week. Podman container build and LLM credential wiring are the remaining deployment steps. | ADS environment access. LLM credential path through DeepSight. |
| Skills on main CI/CD repository | Three skills committed: NxOS-Issue-Categorizer, WebEx-Bot-Builder, WebEx-Solution-Architect. Inventory documentation and ds agent init pattern validation this week. | None blocking. |
| Build dependency graph for commits and PRs | Current approach understood and documented from Justin last week. Deeper mapping framework being finalized and shared this week. | None blocking. |

---

## New items added this week

Regression protection framework. UI automation (Playwright-based) plus backend validation of the pipeline and business logic. Modular and adapter-based so the core is reusable across other Cisco applications. Framework derived from prior BayOne work, with an adapter layer built specifically for the CI/CD application.

---

## Open items and access

| Item | Status | Dependency or Unblock |
|---|---|---|
| NX repository lead-only access for the team | User identifiers posted last Friday. First sign-on to the NX GitHub server is the gating step before access can be granted. | Each BayOne team member completes first sign-on. |
| Permanent ADS provisioning | Standard onboarding request submitted Friday April 24. Escalation in flight. | Cisco access provisioning workflow. |
| CN-SJC-STANDALONE bundle membership | Submitted Friday April 24. In the standard provisioning window. | Cisco provisioning. |
| MCP viewer playground | Coming soon per the Cisco team. Will be used for external MCP validation before integration. | Cisco platform team launch. |
| DeepSight credentials | Issuance gated on the team operating from an ADS environment. | ADS environment access (Permanent or Temp). |
| Asynchronous unblocking via the engagement chat | Active. Either side may post blockers between meetings. | None. |

---

## Friday May 1 deployment target

This is the first deployment of the chat-based assistance in the CI/CD application, with a paired WebEx bot on the NX-OS CI pipeline. The initial release is a static and dynamic FAQ. Static entries cover environmental issues and recurring questions for which answers already exist. Dynamic answers come through the CAT MCP, which queries the NX repository at request time. Both surfaces share the same backend so users can ask the same questions from either the chat in the application or the WebEx bot.

This is a first pass, with incremental improvement to follow as the team uses it and as feedback from team usage and internal testing comes in.

The deployment is gated by two Cisco-side dependencies:

1. **ADS environment.** Deployment requires an ADS to run the application. If a Permanent ADS is not available in time, the first release will run on a Temp ADS as the interim path. ADS resource availability sits with the Cisco platform team.
2. **Language model API credentials.** Language model features require a DeepSight-provided API key. If the DeepSight key is not yet issued, the first release will run on the existing Circuit API key as an interim path, with known limitations until the DeepSight key is available.

Pre-deployment internal testing has been limited by these same access constraints. Validation will continue post-deployment as access is established and feedback comes in.

---

## Architecture overview

```mermaid
flowchart LR
    User1[User in CI/CD App Chat]
    User2[User in NX-OS CI WebEx]
    Backend[Shared Backend]
    Router{Routing}
    Static[Static FAQ]
    Dynamic[CAT MCP against NX repo]
    LLM[LLM]

    User1 --> Backend
    User2 --> Backend
    Backend --> Router
    Router --> Static
    Router --> Dynamic
    Static --> LLM
    Dynamic --> LLM
```

---

## Recent closures

Items resolved between the Friday April 24 sync and this update.

- ~~NX repository access path defined~~
- ~~CI/CD repository destination clarified between main and SME-KB~~
- ~~Deployment form decided~~
- ~~Friday May 1 deployment target defined~~
- ~~Monday weekly cadence and format decided~~
