# Temp ADS Self-Deploy: The Bare-Minimum Floor

**Framing per Colin:** "We can at least go with the ADS machine that is temp, as that can be self-deployed and run with very minimal effort. At the bare minimum, the team should be able to do that. There's nothing getting them from doing that aside from their own free will, and we will have to set targets on that, as that would not be acceptable for this to not be done by Friday."

---

## What this is

The temporary ADS deployment is the floor. It is not the ceiling. The ceiling is the full Main Set 15 next-Friday target (CI/CD app on permanent ADS with CAT MCP, static FAQ, dynamic answers, WebEx bot, shared backend). The floor is what the team can deploy on the temporary ADS with the closest thing to zero external dependency available right now.

The floor is achievable but it is **not free of Cisco-side dependency**. The earlier framing of "no Cisco-side dependency" was wrong. Two Cisco-side items remain on the critical path even for the floor. They are tractable, but they are real, and the daily plan must treat them as risks. They are listed in the dependency section below.

## What Srinivas himself said about temp ADS on Friday Apr 24

Three Srinivas statements from the Friday Apr 24 transcript bear directly on what is and is not possible on temp ADS this week.

**Temp ADS is the explicit fallback for the next-Friday delivery, with Srinivas's blessing.** When Colin laid out the Mahaveer escalation, he said: "I don't want to miss a deliverable for next Friday to you. We're going to make sure it at least gets deployed on the temp ADS regardless." Srinivas accepted this without objection. Later Colin restated: "CSCD app, the thing that we are doing right now is we're bringing it up on the temp ADS, because we don't have a permanent ADS. So that's what we're doing for today." Srinivas's response acknowledged the path but immediately surfaced a constraint: "So that one, then again, you need to work your thumb for marketing your bundle, I mean, real bundles and whatnot. So there are some litigations out there, but you should solve the partner ADS, otherwise, it will get stuck." (Source: srinivas_4-24-2026_formatted.txt lines 183-187.)

The plain reading: temp ADS will run the demo, but Srinivas considers it stuck-prone. Permanent ADS is still the real target, and the floor demo on temp ADS is acceptable as a one-week interim only.

**WebEx bot on temp ADS needs only a Podman container.** Colin's exact framing on Friday: "we just need to get it on the ADS and we're in good shape. But even with the temp ADS, we'll be able to have this all deployed. It just needs, I believe, a Podman container to start." (Source: srinivas_4-24-2026_formatted.txt lines 322-326.) Note the hedging word "believe" — the team has tested the bot locally but has not yet pushed it through a Podman container against the temp ADS environment specifically. The deployment pattern is plausible; it is not yet proven on this specific machine.

**Temp ADS counts against Cisco's compute budget.** Colin asked directly: "the ADS machines that are temporary, do those count towards the compute that you have or are those kind of free game in the interim?" Srinivas: "They are not free. They are still built, except that they have like four weeks window or something." (Source: srinivas_4-24-2026_formatted.txt lines 127-132.) This is consequential. It means BayOne should not treat temp ADS as a sandbox for arbitrary experimentation. Anything heavy spun up on temp ADS draws from the same constrained pool that Srinivas described as already overcommitted ("for this project, or even for doing myself any R&D, I don't have any compute right now"). The two-mode pattern decided in the Friday meeting (on-demand pull + low-frequency dashboard refresh, no central poller) applies on temp ADS just as it applies on permanent ADS.

**Srinivas-side framing from the Wednesday Apr 22 MOM (srini_MOM.txt).** The Wednesday MOM did not address temp versus permanent ADS specifically, but it did set a priority that lands on the floor: "The priority will be on the deployment of this system, allowing users to begin utilizing it and providing feedback." That is Srinivas's stated value. The floor satisfies it; nothing else does. Anything not deployed by Friday is invisible to the priority Srinivas set on Wednesday.

## What "deployed on temp ADS" means at the floor

The minimum demonstration that satisfies the floor:

1. **WebEx bot running on temp ADS in a Podman container.** The bot itself is complete on the webex-skills branch per Main Set 15 status. Colin tested it locally. The remaining work: build the Podman image, push it to temp ADS, run it, validate that it can reach the WebEx API from inside the temp ADS network.
2. **CI/CD app shell running on temp ADS.** This is the part that needs the most clarification. The Friday meeting changed the plan here: Anupma's team is deploying the CI/CD app for BayOne, targeting Monday for a live environment. If that landing happens, BayOne consumes the app rather than standing it up. If it slips, the team falls back to standing up the app shell directly on temp ADS — which is heavier work and was not what either side planned for this week.
3. **Static FAQ entries served through the chat interface.** Static path only. The data exists ("the answers are already done in that way" — Srinivas, transcript line 491). The task is wiring the static answers into the CI/CD app chat backend.
4. **A demonstrable end-to-end loop on the temp ADS.** User opens chat, asks a question that has a static FAQ entry, gets the static answer back. Or user pings the WebEx bot in a test space and gets a response.

This is enough to show Srinivas on Friday that BayOne hit the deployment milestone in some form, even if the permanent ADS and full dynamic CAT MCP path are still pending.

## Why this matters strategically

The Friday May 1 conversation with Srinivas will compare what BayOne committed to deliver against what BayOne actually delivered. If permanent ADS is blocked through no fault of BayOne, the temp ADS deployment is the proof point that BayOne executed everything in its control. The framing for Srinivas is straightforward: the application is running, the bot is running, the static path works, the dynamic path is wired and waits only for the access provisioning to complete.

If BayOne does not have the temp ADS deployment running by Friday, there is no proof point. The conversation becomes a defense of why nothing landed in the engagement's first contract-renewal-window deployment. That is not acceptable.

## What is required to hit the floor

### Already done (per Main Set 15 status)
- WebEx bot complete on webex-skills branch (Apache eCharts, WebEx bot creation, NX-OS issue categorization, plus one fourth skill Colin needs to identify for the inventory)
- WebEx bot tested locally; Podman-container deployment pattern identified as the path
- Issue categorization skill complete on main CI/CD repo
- CAT MCP installed in VS Code with 4 tools identified, OAuth resolved
- NX repository lead-only access committed by Srinivas (pending Colin sending user IDs)

### Cisco-side dependencies that are NOT removed for the floor
These were previously listed as removed. They are not. Each is on the critical path for the floor.

- **Anupma's team CI/CD app deployment.** Srinivas committed Friday: "we will deploy the app for you... that will be live maybe by Monday and then you can be off." If Anupma's team does not land the CI/CD app instance by mid-week, BayOne either consumes a slipped environment or falls back to standing up the app directly on temp ADS. Status check Monday morning is the gating action.
- **CN-SJC-STANDALONE bundle request.** Colin requested it on the Friday call. Srinivas confirmed: "it will take like four to six hours or sometimes more." (Source: lines 188-191.) This bundle is needed before the temp ADS environment is fully usable for the deployment. If the request is pending more than 24 hours, escalate. This is also the second of the two remaining gates on the DCN Switching tenant blocker (per blockers.md row 1).
- **NX repository lead-only group add-in by Srinivas.** Required for dynamic CAT MCP path, not for the static FAQ floor. But Colin owes the user IDs to Srinivas immediately per the Friday commitment, and the floor framing to Srinivas on May 1 ("the dynamic path is wired and waits only for the access provisioning") only holds if BayOne sent the IDs and Srinivas had the chance to add them.

### Internal-only steps the team must execute this week
- Push WebEx bot to temp ADS via Podman container; validate WebEx API reachability from inside the temp ADS network
- Confirm or stand up CI/CD app shell on temp ADS (depending on Anupma's team timing)
- Wire static FAQ entries from existing answer data into the chat interface as the static-answer path
- Wire WebEx bot to share the same backend as the CI/CD app chat (service-application-platform pattern with pluggable frontends, per the Friday architectural decision)
- Implement user session identity in the dashboard so per-user PR filtering works (Friday architectural decision; lighter floor variant: confirm the CI/CD app already provides user session and document the contract)
- Test the end-to-end loop on temp ADS, capture screenshots or recording for Friday

### Not blocking the floor (can slip without missing the floor)
- DeepSight credentials (post-demo per Srinivas)
- Permanent ADS via Mahaveer
- Full dynamic CAT MCP execution against live NX repo (only gates the dynamic path; static path is the floor)
- Group API integration for manager roll-up views (Srinivas described it but it is a next-week item)
- All skills auto-discovery via ds agent init pattern (operational improvement, not floor-gating)
- MCP viewer app on DeepSight (announced as launching but not required for the floor)

## Technical steps glossed over in the prior version of this note

Three steps that previously read as one-line bullets but each carry a non-trivial risk surface:

**Podman image build for the WebEx bot.** "Push WebEx bot to temp ADS via Podman container" hides the actual sequence: write the Containerfile, declare runtime dependencies (Python version, WebEx SDK version, any native libs), set environment variables for the WebEx bot token (which is itself the subject of Cisco IT compliance from Set 07/08), build the image either locally or on temp ADS, push or load it onto temp ADS, run it, validate logs, validate WebEx API reachability from the temp ADS network. Each step can fail. The most likely failure modes are network egress restrictions on temp ADS that block the bot from reaching the WebEx API, and version mismatches between the local test environment and the RHEL8 temp ADS environment.

**Static FAQ data shape and routing.** "Wire static FAQ entries from existing answer data into the chat interface" requires the team to identify which answers Srinivas was referring to ("the answers are already done in that way... there are some environmental issues and whatnot that is already there in the answers by the user" — transcript lines 491-493), extract them into a data structure the chat backend can serve, and implement the routing logic that decides whether a user query goes to the static path or the dynamic CAT MCP path. The routing logic is the part that ties to the SAP backend pattern Srinivas described and is not a one-liner.

**Shared backend between CI/CD app chat and WebEx bot.** "Wire WebEx bot to share the same backend" requires the SAP-style backend to actually exist with two pluggable frontends. If the CI/CD app instance from Anupma's team arrives Monday with an existing backend, BayOne extends that backend. If it arrives without a backend BayOne can hook into, the team writes the backend itself, which is meaningful work for one week. Clarification with Anupma on Monday is the gating action.

## Friday May 1 deliverable framing for Srinivas

If the floor is hit but the ceiling is not:

> "The CI/CD app is running on temp ADS with the static FAQ path serving answers in the chat interface. The WebEx bot is running on temp ADS sharing the same backend. The dynamic CAT MCP path is wired and is gated only on the NX repository access that you committed to provision last Friday. As soon as that access lands, the dynamic path executes against the live repository and we move from temp ADS to permanent ADS the same week."

If the ceiling is hit:

> Standard Main Set 15 deliverable framing. CI/CD app on permanent ADS with full dynamic and static paths, WebEx bot on NX-OS CI pipeline.

## Targets

These dates assume Anupma's team CI/CD app instance lands by Monday end of day. If it slips, slide every subsequent date by the slip and revisit the Friday demo scope.

- **Monday Apr 27 (morning):** Status check on Anupma's team CI/CD app deployment. Confirm CN-SJC-STANDALONE bundle status. Send NX repo user IDs to Srinivas if not already done.
- **Monday Apr 27 (end of day):** Containerfile written for WebEx bot. Image builds locally. CI/CD app instance live (if Anupma's team hits Monday target) or fallback plan triggered.
- **Tuesday Apr 28:** WebEx bot Podman container running on temp ADS. WebEx API reachability validated from inside the temp ADS network. Static FAQ data extracted from existing answers and structured for the backend.
- **Wednesday Apr 29:** Static FAQ routing wired into the CI/CD app chat backend. End-to-end static-path loop working on temp ADS. Screenshots captured. NX repo access likely landed by now (Srinivas adding user IDs); dynamic CAT MCP path can begin wiring.
- **Thursday Apr 30:** Dry run of the Friday demo on temp ADS. Any gaps surfaced for the morning of Friday May 1. Dynamic CAT MCP path stubbed or live depending on access timing.
- **Friday May 1:** Demo to Srinivas. If permanent ADS is in place, demo there. If not, demo on temp ADS with the framing above.

## What "not acceptable" looks like

The Friday May 1 demo with no application running anywhere. Just a status update and apologies. This is the outcome to prevent.

## Question for Colin

The team can hit the floor but it is not dependency-free. The two Cisco-side items that remain (Anupma's team CI/CD app landing, CN-SJC-STANDALONE bundle) are tractable but warrant Monday-morning visibility. Confirm Friday May 1 dry-run on temp ADS as the hard deadline. Confirm whether the framing-to-Srinivas language above is the right diplomatic landing if the ceiling is not hit. Confirm whether the team should preemptively start the fallback (BayOne stands up the CI/CD app shell directly on temp ADS) on Monday afternoon if Anupma's team has not delivered by then, or whether to wait an additional 24 hours.
