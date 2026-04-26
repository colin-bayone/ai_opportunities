# WebEx Chat Findings — Cross-Reference Against the Plan

**Sources:** files 06 (BayOne internal) and 07 (BayOne + Cisco joint), through 2026-04-26 16:00 ET.
**Purpose:** Surface what the chats add, contradict, or clarify relative to the four working files (01-04) and the consolidated open questions (05). No file 01-04 edits — Colin is mid-review.

---

## A. Material clarifications (change how the plan should read)

### A1. NX repo access provisioner is Anupma, not Srinivas
File 02 section A4 and the Singularity Set 15 chain frame the NX repo unblock as "Srinivas committed to add user IDs himself." The joint chat shows the actual mechanism: Friday 5:21 PM, Srinivas wrote "pls post all email id's here so that **Anupma** can give access to NX repo to the team." Anupma confirmed "Will add" — but with a hard prerequisite: **"make sure to logon to the NX GitHub server at least once, so it's available to add to repo."** She pinged again at 7:13 PM Friday: "Please do the above, so I can add."

This is a real outstanding gate that the plan does not currently capture. The team has to log in to the NX GitHub server before Anupma can grant access. As of Sunday 4 PM ET, the chat does not show confirmation that all four team members have logged in. **This needs to be on the master open items list and on the Monday morning checklist.** Without it, the CAT MCP execution path stays gated even though the access commitment is in hand.

### A2. RHEL8 is confirmed as the ADS server type
Friday Apr 24 12:31 PM, Colin asked "do we know the proper server type for DeepSight of these?" Srikar: "RHEL8." This is operationally important for file 03 (temp ADS minimum bar) — any Podman image build needs to target RHEL8 compatibility. The temp ADS file already flags "RHEL8 version mismatch risk" as a watch item, and this confirms the target.

### A3. Saurav already has a circuit API token (as of Apr 23)
Saurav posted in team chat Thursday Apr 23 12:25 PM: "my circuit api token got approved." The token is real but **scope-limited per Srinivas's framing on the Friday call**: it is intended for Cisco personnel to try out AI tools at small scale, not for deployed production apps. It carries no production-grade usage allowance. Adequate for the PoC demo; not viable as the deployment-time LLM credential. The "API Enabler Bot" path Saurav documented (3 steps: visit URL, fill form, wait for bot ping) is a reusable pattern other team members can run on Monday to get their own scope-limited tokens.

**Srinivas is the gating factor for production-grade tokens, not the API Enabler Bot.** From the Friday transcript, Srinivas is currently struggling with this exact problem: he has no key revocation mechanism, no key lifecycle management, no rotation pattern in place. He has been operating with a single admin key and has not addressed the structural gap with his team. He flagged this and asked for knowledge leadership from BayOne (Colin offered three patterns: GitHub secrets, Azure Key Vault, Open Web UI; framed as "add to your list, not urgent" per Main Set 15 decision A12).

**This is not a BayOne gating factor for the next-Friday demo.** If Srinivas does not get a production-grade token mechanism in place by Friday May 1, the team proceeds with Saurav's circuit token (and any others granted via the API Enabler Bot path) for the demo. Srinivas cannot reasonably be upset about a gap he himself owns and that he himself flagged on Friday as a longer-term concern. BayOne cannot conjure a key vault or rotation system for him in a one-week window for a PoC demo; that is genuinely longer-term work and Srinivas acknowledged this on the call.

**Section A7 of the master open items should reflect:** (1) Saurav's existing token is sufficient for the PoC demo; (2) Other team members can self-serve scope-limited tokens via the API Enabler Bot Monday; (3) The mid-week Colin/Srinivas conversation on key distribution remains valuable but is no longer urgent for Friday May 1; (4) The longer-term key vault / rotation / lifecycle work is a Srinivas-side ask that BayOne can advise on but does not own as a deliverable.

### A4. Bazel dependency graph command is in hand from Justin (Apr 20)
Joint chat Monday Apr 20 1:47 PM, Divakar/Justin posted the working Bazel command:
```
bazel --output_user_root=../bazel_cache1 build //bzl-packages/core_64_n9000:compile_info_json_deps_graph
```
Output is a `.dot` structure at `bazel-bin/bzl-packages/core_64_n9000/compile_info_json_deps_graph`. This is the substrate for the PR-to-PR dependency mapping work (file 02 sections A10 and A15). The team has a working command they can execute as soon as NX repo login completes — does not need to wait for any further Cisco-side action.

### A5. Mahaveer ADS document received Friday Apr 24
"We received this document from Mahaveer" (Friday 12:11 PM, Srikar). The document is an ADS onboarding doc (filename surfaced separately as `onboarding_ADS_20251201_updated.pdf`, posted earlier on Apr 16 by Mahaveer per team chat). This is what the team is working off for the standalone ADS request. The team already followed the document's request flow — Srikar confirmed Friday 12:32 PM "Yes, We requested for standalone." So the request is in flight. **File 03 should treat the standalone bundle request as "already submitted Friday Apr 24" rather than "to be done."** The 4-6+ hour window Srinivas mentioned starts from the request submission, which means the bundle membership could land as early as Saturday or Sunday.

### A6. Anupma's 7:13 PM Friday ping is the most recent Cisco-side touchpoint
The joint chat ends with Anupma asking again for the team to log in to the NX GitHub server. Nothing from Srinivas, Justin, Divakar, or Anand after Friday evening. This is the last ball in BayOne's court before any Monday Cisco-side movement. Whoever has not logged in yet should do so before Monday morning to unblock Anupma.

## B. Things the chat surfaces that are NOT in any working file

### B1. Saurav's circuit-API-form prompt-hijack note (Apr 17)
Saurav speculated about prompt-hijacking the API Enabler Bot to bypass the form. This is internal-only context, not actionable, but reflects on team posture toward Cisco process friction. Does not change the plan; worth knowing for register awareness.

### B2. Wall-E bot operational then stranded (Apr 10 → ?)
Saurav added Wall-E bot to the team chat Apr 10 6:27 PM. Wall-E ran scrape, ping, help, and DB-status commands successfully on the team space the same evening. Action items tracker has item 102 "Wall-E bot stranded on dead Podman container." The chat confirms Wall-E was working initially. The stranding is post-Apr 10. This is consistent with the Set 14b catalog framing.

### B3. Apr 6 "PFA the overview of our upcoming tasks" (Colin)
Colin posted a planning overview to team chat after a call with Srinivas. The PDF is referenced by "PFA". This may be in the Singularity already as part of pre-Set-07 planning material. **Flag for confirmation: is this attachment processed?**

### B4. Apr 16 "Update from Naga" (Srikar)
Srikar shared an attached Naga update at 4:50 PM. Content not described in the chat text. May be the Pulse/Scribbler scope clarification or a separate update. **Flag for confirmation: is this attachment processed?**

### B5. Apr 17 Srinivas "impact graph high level design"
Srinivas attached an "impact graph high level design" document on Apr 17 2:32 PM in the joint chat: "Here is the impact graph high level design we did sometime back on the CD build. pls use this as reference and build on top of it working with Justin." This is a Cisco-side reference artifact (the prior CD build impact graph). **Flag for confirmation: is this attachment processed in the Singularity? It could be load-bearing for the build-track design.**

### B6. Mahaveer's onboarding_ADS_20251201_updated.pdf
Posted to team chat by Mahaveer directly (forwarded by Namita Apr 16 7:33 PM). This is the document the team is working off for permanent ADS provisioning. **Flag for confirmation: is this attachment processed?**

## C. Things the chat confirms that are already in the plan

- Pulse/Scribbler scope deferral and the Naga "modular tool" framing (team chat Apr 9-10)
- Two-track team structure (WebEx + Logs) being executed (multiple team chat exchanges)
- DCN Switching tenant/CN-SJC-STANDALONE bundle access blocker (joint chat Apr 16)
- Knowledge graph deferral language in Wednesday MOM is verbatim in team chat Apr 22
- CAT MCP server URL shared by Srinivas in joint chat Wednesday Apr 22 1:42 PM (matches Singularity)
- SME-KB URL shared Wednesday Apr 22 1:37 PM (matches Set 15 clarification — destination for skills is main CI/CD repo, not SME-KB)
- Friday Apr 24 NX repo email IDs posted by Srikar (colmoore@cisco.com, namane@cisco.com, srmadara@cisco.com, sauravmi@cisco.com) — confirms the four-person scope and the cisco.com email convention

## D. People-list confirmations (joint chat)

Confirmed participants in the BayOne CI-CD WG joint chat (created by Anand Singh 2/10/2026):
- **BayOne side:** Colin Moore, Srikar Madarapu, Namita Mane, Saurav Mishra, Zahra Syed (BayOne ops, also Rahul Bobbili mentioned in passing 3/25)
- **Cisco side:** Anand Singh, Divakar Rayapureddy, Srinivas Pitta, Shih-Ta Chi (added 3/26 by Anand for general onboarding), Neha Malhotra (added 3/31 by Zahra), Justin Joseph (added 4/20 by Divakar), Anupma Sehgal (added 4/17 by Srinivas)
- **No Vasanth.** Confirmed dictation noise from "Srinivas and Anand."
- Shih-Ta Chi and Neha Malhotra are Cisco-side onboarding/operations contacts who appeared early, were not flagged in the engagement org chart as ongoing collaborators. Worth a confirmation pass on whether either is still active.

Confirmed participants in the BayOne-internal team chat:
- Colin Moore (cmoore@bayone.com and colmoore@cisco.com appearances)
- Namita Mane (namane@cisco.com)
- Srikar Madarapu (srmadara@cisco.com)
- Saurav Mishra (sauravmi@cisco.com)
- Askari Sayed (assayed@cisco.com) — chat presence ends Apr 2 2026, consistent with prior context that Askari left the project
- Wall-E bot (added Apr 10 by Saurav)
- Vaishali and Tanuja are not visible in this chat (they may be in a different team chat or only on the joint chat post-add)

## E. Implications for the open questions in file 05

- **Block A (Monday one-pager):** Question A2 (was the same-Friday first cut sent?) is still unanswered. Chat does not show Colin posting the one-pager into the joint chat Friday evening. If it was sent via direct message or email, fine; if not, the slip should be acknowledged.
- **Block B (master open items):** Section A4 should be revised to reflect the Anupma/login prerequisite chain. Section A7 should reflect Saurav's existing circuit token. New item for "Team logs in to NX GitHub server before Anupma can add" is missing.
- **Block C (temp ADS):** RHEL8 confirmation reduces the RHEL8 version mismatch risk to a verification step rather than an unknown. CN-SJC-STANDALONE bundle request was submitted Friday — the Sunday/Monday morning checkpoint is whether it landed.
- **Block D (policy gate):** Chat shows no policy distribution event in either chat through Sunday 4 PM ET. The 3-of-6-signed status from file 04 holds; the chat does not surface any additional signature confirmations.

## E2. Nova CI/CD AI Assistant — Srinivas's parallel internal project (INTERNAL ONLY)

The Cisco-side repository overview Srikar surfaced (`srikar_nova_cicd_assistant_repo_overview_2026-04-16.md`) describes a project called "Nova CI/CD AI Assistant" — a conversational AI assistant for Cisco CI/CD operations. Per Colin's framing:

- This is a Srinivas-led internal project that he has been claiming is near-complete for months. It is not actually near-complete and has been delayed repeatedly. Srinivas keeps saying "it's almost ready" without delivering.
- The project appears to be largely duplicate of what BayOne is building. Srinivas runs parallel duplicate workstreams that he does not manage well.
- Srinivas appears to have over-promised to his leadership on this project and is hedging his bet by also engaging BayOne for the same outcome.
- From what BayOne has seen, the Nova work is "AI tool vibe-coded" — simplistic, not production-ready, calling itself a production app when it isn't.
- BayOne's work remains the critical and primary path. Anything BayOne delivers will be substantially better.

**Operational implication:** Be aware of Nova. Do not treat it as competition or as a constraint on BayOne's deliverable. Do not refer to it in any client-facing artifact or in any joint chat content. If Srinivas references it, acknowledge politely and continue with BayOne's plan. Do not propose collaboration with Nova or alignment to its architecture; the architecture has not been demonstrated to merit alignment.

**Naming implication:** Do NOT use the "Nova" name in the Monday one-pager, GitHub issues, or any BayOne-owned artifact. The BayOne deliverable has its own framing (CI/CD app on ADS, CAT MCP, static FAQ + dynamic answers, WebEx bot, shared backend) that does not need to absorb a Cisco-side internal product name. Earlier suggestion to flag "Nova" as the official deliverable name is withdrawn.

This entire section is INTERNAL ONLY. No part of it surfaces in any client-readable channel.

## F. Attachments not visible in the chat exports (Colin omitted them)

The chat exports include text only, with `📎 file` markers in the Wall-E bot's transcript dump (team chat Apr 10) but no file content. Notable referenced attachments for cross-checking against Singularity processing:

1. Apr 6 Colin "PFA overview of upcoming tasks" — task plan PDF
2. Apr 9-10 Namita architecture screenshots/PDFs
3. Apr 15 Namita three architecture/log artifacts (current architecture, current architecture with limitations, log type mapping)
4. Apr 16 Namita "Initial draft of architecture"
5. Apr 16 Srikar 4231-message NXOS-CI-Workflow CSV (confirmed processed — basis of the 25-category taxonomy)
6. Apr 16 Srikar rule-based analysis charts
7. Apr 16 Srikar resolvable/unresolvable category charts and spreadsheets
8. Apr 16 Srikar "Update from Naga" — content unclear, **flag for processing confirmation**
9. Apr 16 Mahaveer `onboarding_ADS_20251201_updated.pdf` — **flag for processing confirmation; load-bearing for temp ADS work**
10. Apr 16 Srikar "brief overview of the CI-CD repository"
11. Apr 17 Srikar charts and spreadsheets
12. Apr 17 Srinivas (joint chat) "impact graph high level design" — **flag for processing confirmation; load-bearing for build-track**
13. Apr 24 Srikar "We received this document from Mahaveer" — same as #9 likely or related ADS doc
14. Apr 24 5:20 PM Srikar "Update on the cat mcp and issue responder skills"

Items 8, 9, and 12 are the highest-priority confirmation requests. The rest are likely covered by Set 09 architecture deliverables, Set 11-12 dashboard work, or are derivative of content already in the chain.
