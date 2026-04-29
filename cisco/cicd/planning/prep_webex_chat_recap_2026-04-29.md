# Prep recap: WebEx engagement chat since the Monday Srinivas sync

**For:** Wednesday 2026-04-29 Srinivas meeting
**Source:** `/cisco/cicd/source/week_2026-04-27/day_2026-04-27/webex_chat_post_monday_sync_2026-04-27.txt` plus the Realm portal screenshot at `/cisco/cicd/source/week_2026-04-27/day_2026-04-27/03_33_24.jpg`
**Span:** Monday Apr 27, 2:44 PM through Tuesday Apr 28, 6:39 PM PST

---

## What landed cleanly

**Provisioning was fast.** Divakar provided two ADS machines within hours of the 1pm Monday sync closing.

- `divvenka-qa-1` and `divvenka-qa-2`
- 16 cores, 31 GB RAM, on the `CN-SJC-STANDALONE` bundle
- Spec confirmed live by Divakar via `lscpu` and `free -h`
- Matches the Monday commitment exactly

Srinivas thanked Divakar at 4:41 PM Monday. Anand checked in at Tue 12:35 AM ("Colin did it work?"), continuing the working-meeting-level engagement pattern from Monday.

## What is now blocked

**Access to the provisioned machines is gated by REALM bundle membership and the unblock path is opaque.**

- Tue 9:29 AM: Colin tried the connection and was blocked by REALM. The host is gated by two bundles: `INS-SW-BUILD` and `CN-SJC-STANDALONE`.
- Tue 9:35 AM: Colin submitted a Request Access via `realm.cisco.com`. The portal returned "An email has been sent to bundle owners."
- Tue 4:47 PM: Srikar hit the same wall. Was confused about whether the `srikarmadarapu@divvenka-qa-1` prompt asking for "your UNIX password" wanted CEC, his AD password, or something else. Re-submitted at Divakar's prompting.
- Tue 6:39 PM: Srikar received the actual approval-path email. Membership is gated through `oneaccess.cisco.com` (group `CN-ACI-HOSTBUNDLE-GROUP-ACCESS`) or through `myid-groups.cisco.com` (groups `DEVXADS-GROUP`, `NGDEVX-DEV`, `WIT-REALM-GROUP`).

The Realm portal screenshot adds the missing piece. Divakar's own Bundle User view shows zero pending host approvals across all three queues (host, storage, storage permissions). The approval is not happening at the host-bundle level. It is happening through user-group membership in two adjacent Cisco identity systems, and whoever owns those groups has not been named to the team.

## Read for today's meeting

This is the same pattern as the Mahaveer ADS situation, at a different layer. Cisco delivered the infrastructure cleanly. Cisco's access provisioning is opaque, the documented unblock path (Realm Request Access portal, "email to bundle owners") is not the actual unblock path, and the actual unblock path is gated by a person nobody on BayOne has been told about.

The team has been blocked on usable ADS access for 24 hours and counting as of the start of today's meeting.

## Concrete asks Colin can frame for Srinivas

- Name the owner of `CN-ACI-HOSTBUNDLE-GROUP-ACCESS` on `oneaccess.cisco.com`
- Name the owner of `DEVXADS-GROUP`, `NGDEVX-DEV`, and `WIT-REALM-GROUP` on `myid-groups.cisco.com`
- Get those user-group memberships approved today so the team can use the ADS that was provisioned Monday

The "we have the machines, we cannot use them" framing keeps the focus on Cisco-side ownership. Colin can also flag that Srikar already lost most of Tuesday on this and the team's Friday deliverable timeline is being eaten by access provisioning, not by code.
