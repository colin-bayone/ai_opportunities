# Client Data Handling Policy Gate Status

**Source decision:** Team Set 15 decision discussion, action items #137 (Colin sends policy to team) and #138 (Namita signs and returns before resuming GitHub work).
**Status as of 2026-04-26 Sunday:** 3 of 6 signed copies received. Remaining signatures pending. Specific identities of signed/pending not noted here (privileged to Colin).

---

## What the policy is

The BayOne Client Data Handling Policy, effective 2026-04-20, issued by Colin Moore as Director of AI. The full signed document lives at `/home/cmoore/programming/ai_opportunities/bayone/processes/2026-04-20_client_data_handling_policy/client_data_handling_policy_2026-04-20.md`.

It is a **BayOne-wide policy** (not Cisco-specific) that applies to all BayOne personnel on any client engagement, contract, or SOW. It is a signed policy, not an acknowledgment, because the consequence ceiling is termination. It was created in direct response to the 2026-04-20 Cisco IT incident (Sets 06 through 06g) but is engagement-wide in scope going forward.

Colin introduced it to Namita in the Friday Apr 24 1:1 as the engagement-wide gating mechanism for resuming any client-data interaction. Mandatory for every team member including Colin himself: "I'm not immune to the policy either." (Source: Colin-Namita 1:1 transcript, 2026-04-24.)

## Who signs

Required signatures for the Cisco CI/CD engagement: Namita, Srikar, Saurav, Vaishali, Tanuja, Colin (six total).

- Confirmed signed (3 of 6): identities held by Colin
- Pending signatures (3 of 6): identities held by Colin

## What the policy actually covers (full scope from the signed document)

The current note had previously framed the policy as gating GitHub work specifically. The actual signed policy is substantially broader. The five rules:

1. **Rule 1 — Client Data Stays On Client Systems.** Any client-originated artifact (file, log, source code, document, screenshot, diagram, output, email, chat message, credential, configuration) remains on the client system. No AirDrop, USB, email-to-BayOne-account, upload to BayOne GitHub or any non-client cloud, screenshots into non-client tools, copy-paste into non-client chat or notes, or photographs of client screens with personal devices. Sharing client material with other BayOne personnel through BayOne channels is also prohibited even when both parties are on the engagement.
2. **Rule 2 — Team-Internal Communication On Client-Sanctioned Channels.** Any voice, video, chat, or file share between BayOne personnel about client work happens on the channel the client has sanctioned (typically client-tenant Teams, WebEx, Slack, or email). Not BayOne Teams, BayOne email, or personal messaging.
3. **Rule 3 — No Unsanctioned AI Tools On Client Data.** Approved AI tools are limited to those the client has sanctioned in writing or in published policy. The engagement lead communicates the approved list. No pasting client material into Claude, ChatGPT, Gemini, BayOne-hosted AI, or personal AI accounts unless explicitly sanctioned.
4. **Rule 4 — No Cross-Client Movement.** Material from one client engagement does not move to another. Techniques and general knowledge travel; artifacts do not.
5. **Rule 5 — When In Doubt, Stop And Ask.** If a workflow would require bending any rule, stop and ask the engagement lead before acting.

The policy includes a self-disclosure clause (material mitigating factor) and a single-strike consequence framing, with termination of employment with BayOne Solutions explicitly on the table for any violation.

## What the policy gates (Cisco CI/CD engagement specifically)

Per Colin's Friday 1:1 with Namita, the gate covers:

- Resuming any GitHub work (Namita's specific question, Colin's "yes with one condition" answer)
- Any client-data interaction by any team member on the Cisco engagement
- Any work that touches Cisco-owned source material, transcripts, code, configuration, or client systems

The hard rule, in Colin's words: "the only thing that's gating is just have that filled out and sent back before you continue and then you are free to go."

Note that Vaishali and Tanuja have an additional separate gate: they may be in observer mode (talk and listen) but cannot be assigned Cisco work until they receive their Cisco laptops, expected by next Friday. This is a Colin-imposed constraint layered on top of the policy gate, not a policy clause.

## Cisco-side framing alignment (from srini_MOM.txt 2026-04-22)

Srinivas's Wednesday MOM directive is that all team documentation, design, architecture, and source code be checked into the GitHub repository he is sharing. This is the Cisco-sanctioned channel for the engagement, which is consistent with Rule 1 (work stays on client systems) and Rule 2 (use client-sanctioned channels). The warning header on Monday GitHub issues should therefore be framed as a BayOne-internal contributor gate, not as a barrier to anything Cisco does on the issue. Srinivas, Justin, Anand, Mahaveer, and any Cisco engineer should never read the header as gating their own engagement with the issue.

## Working assumption for Monday Apr 27

By Monday morning all team members will have signed and returned the policy. This is a working assumption, not a confirmed status. The Monday GitHub issues will carry a warning header that defaults to the gate, in case any signature has not yet landed. The header reads as a standing operational artifact even after all signatures land, both because it scales to future team members joining the engagement and because it makes the BayOne policy structure visible inside a Cisco-readable surface without leaking incident detail.

## Warning header text for Monday GitHub issues (refined)

Proposed text to appear at the top of every BayOne-owned issue created in the Cisco CI/CD repository on Monday Apr 27 onward:

> **BayOne contributor gate.** Any BayOne Solutions team member contributing to this issue must have signed and returned the BayOne Client Data Handling Policy to Colin Moore before any work on this issue is started. The policy covers data movement between client and non-client systems, team-internal communication channels, AI tool use on client data, cross-client material handling, and the standing instruction to stop and ask when in doubt. If you have already signed and returned the policy, no further action is required. If you have not, contact Colin Moore directly. This gate applies only to BayOne contributors; it does not gate Cisco engineers, reviewers, or stakeholders engaging with this issue in their normal capacity.

Notes on the framing:
- Reads as standing operational language, not a one-time alert
- Anchors authority on Colin specifically and on BayOne specifically (clear that this is a BayOne-internal gate)
- Names the broad scope of the policy in one sentence so a reader gets why it matters beyond GitHub
- Explicitly excludes Cisco personnel from the gate, which removes any chance Srinivas, Justin, or Anand reads it as a BayOne-imposed constraint on Cisco
- Does not name individuals who have or have not signed
- Does not reference the IT incident that motivated the policy (no mention on a Cisco-visible repository)
- "BayOne contributor gate" as the heading reads as standing process language rather than as a temporary advisory

## Where the warning lives

Three placement options, all worth doing:

1. **Per-issue header.** The warning text above appears at the top of every new BayOne-owned issue. Boilerplate; same on every issue. Immediate enforcement mechanism.
2. **Repository README or CONTRIBUTING.md addition.** A standing one-paragraph note in the repository documentation that points to the policy and to Colin as the gate. Makes the policy structurally visible to anyone joining the repository.
3. **GitHub issue template (if the repo supports it).** If the Cisco CI/CD repo allows BayOne to define an issue template, the warning header becomes part of the template body so it cannot be forgotten on issue creation. This is the lowest-friction operational form of option 1.

Options 1 and 3 are equivalent in user-facing effect; option 3 is the implementation pattern that survives across creators. Option 2 is the structural backstop.

## Considerations not previously surfaced

- **Policy is broader than GitHub.** The current proposed header (and any prior framing) implied the policy is about GitHub specifically. It is not. The header text above now reflects the actual scope.
- **Cisco-side optics.** Cisco IT and Cisco engineers will see this header on every BayOne-owned issue. The framing must not invite the read that BayOne is operating under restriction; it must read as professional standing process. The "BayOne contributor gate" framing accomplishes this.
- **Consequence framing absent on purpose.** The actual policy lists termination as a consequence ceiling. The warning header does not surface this because the header is on a Cisco-visible surface and the consequence framing is BayOne-internal HR posture.
- **Self-disclosure clause not surfaced on purpose.** Same reason. Self-disclosure is a BayOne-internal mitigation lever, not a Cisco-readable concept.
- **Vaishali/Tanuja laptop gate is separate.** The header does not need to address this because they are not yet creating or working on Cisco issues.
- **Cisco's own published policy still governs where stricter.** The BayOne policy explicitly defers to stricter client policy where one exists. The header does not need to mention this; it is structurally implied.
- **Single-strike framing not surfaced.** Internal posture, not for the Cisco-visible surface.

## Open questions for Colin

1. Confirm the refined warning header text above is acceptable, or propose edits. Particular attention to whether the explicit "does not gate Cisco engineers" sentence is the right call, or whether it reads as overexplaining.
2. Confirm placement: per-issue header (option 1), repo documentation (option 2), and issue template (option 3) all together, or pick a subset.
3. Confirm what to do if Monday morning a signature is still missing: do not create issues for that person yet, or create issues with a more pointed header, or escalate to that person directly off the issue surface.
4. Confirm whether Cisco-visible repository content should reference the policy by full name ("BayOne Client Data Handling Policy") or by a shorter form ("BayOne contributor gate" / "BayOne data policy"). The header above uses the full name once.
5. Confirm whether the README/CONTRIBUTING addition (option 2) should link to the actual policy text on a BayOne-controlled surface, or whether the header itself is sufficient context without a link.
6. Confirm whether the policy framing surfaces in Monday's standup as a verbal reminder, or whether the header alone (with the assumption all signatures are in) is sufficient.
