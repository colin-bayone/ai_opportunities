# 02 - Team Chat: GitHub Training Access Saga (4/1 - 4/9)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/team_chat_1009AM.txt
**Source Date:** 2026-04-01 through 2026-04-09 (BayOne AI Team WebEx space)
**Document Set:** 02 (Team WebEx space chat log)
**Pass:** Focused deep dive on GitHub training access resolution

---

## Overview

What should have been a single-click training link turned into a nine-day odyssey spanning a deprecated platform, a VPN red herring, a Chrome/Duo workaround that did not work, a Cisco support call that revealed a silent platform migration, and finally a resolution that required a completely different URL, a different Cisco employee, and a group access request through a third portal. This is the most complete case study so far of the access friction pattern that defines the early weeks of this engagement.

---

## The Full Timeline

### Day 1: April 1, 2026 -- Link Shared

**9:16 AM** -- Colin (posting as colmoore@cisco.com, the "You" identity in the WebEx space) shares two training resources with the team:

1. **GitHub Training:** `https://learn.cisco.com/?courseID=COT00325705`
2. **DeepSight Atlas Training Video:** `https://cisco.webex.com/cisco/ldr.php?RCID=4450a31e35a93f8e14da79e99ba02ff8` (password: `JjDPKxG2`)

The DeepSight video link worked immediately. Srikar watched it the same day and posted an 8-point summary of the DeepSight Atlas platform by 6:59 PM, covering Triage, MCP Weaver, show tech processing capabilities, and the Runbook feature. No access issues reported for the DeepSight link.

The GitHub training link did not work. No one reported success on Day 1.

**7:06 PM** -- Colin (posting as cmoore@bayone.com) responds to Srikar's notes and adds: "All, I just talked with Srinivas and it looks like the issues that some of us are facing for the GitHub training are because we are trying to access it without being on the VPN."

Colin promised to verify this himself before advising the team. He suggested that the Cisco VPN, which is pre-installed by default and uses the same Duo authentication, should resolve the issue.

**Key detail:** Colin's VPN hypothesis came directly from a conversation with Srinivas, not from independent testing. This is the first misdirection -- the VPN turned out not to be the issue.

### Day 2: April 2, 2026 -- VPN Does Not Help

**9:39 AM** -- Askari Sayed posts: "hi Colin Moore / post using the vpn, i cannot access the github training"

This is Askari's only message in the entire 16-day chat log. He directly tested the VPN hypothesis and falsified it. The link was not an access-behind-VPN problem.

No response from Colin is visible in the chat on this date. The thread goes silent for four days.

### Day 6: April 6, 2026 -- Cisco Support Path

**8:54 PM** -- Colin (as cmoore@bayone.com) posts a new approach. Since the VPN did not resolve the issue, he directs the team to call Cisco Support:

> Phone: **+1-408-526-8888**
> Hours: Available 24/5, excluding specific holidays
> Process: Share your Cisco email ID; a support team member will screen share and help resolve or add a new authentication method to your account.

Colin set a deadline: "Please take time to get this resolved by the end of the day tomorrow."

**8:56 PM** -- In the same posting session, Colin shares an overview of upcoming tasks from a call with Srinivas, and reminds the team that discovery questions are due by Friday 4/10. The training access issue is being treated as a blocker that needs resolution before the team can productively engage with the GitHub-based NX-OS workflow.

### Day 7: April 7, 2026 -- Chrome Workaround Attempt, Platform Migration Discovered

This is the most eventful day in the saga. Three distinct troubleshooting approaches are tried and two fail.

**11:05 AM** -- Colin (as cmoore@bayone.com) posts what he believes is the solution, a Chrome/Duo workaround:

> 1. Open Finder and launch "Mac @ Cisco Self Service"
> 2. Search for Chrome and install Google Chrome
> 3. Open Chrome
> 4. Navigate to myduo.cisco.com and log in
> 5. In Chrome, select Touch ID authentication and save credentials
> 6. Navigate to the GitHub training URL using Chrome

Colin also noted that Safari could work if you sign in with a personal Apple ID, which enables additional authentication options. The core theory: Safari's default authentication flow was not presenting the right Duo options, and Chrome after a fresh Duo enrollment would.

**11:46 AM** -- Namita Mane tests the workaround and reports failure: "Thanks Colin! I tried the above steps yet unable to see the Github training! Anyone facing the same issue?"

**11:48 AM** -- Colin (as colmoore@cisco.com) asks Namita to confirm she is on VPN and using Chrome, and again references the support number (+1-408-526-8888) as the fallback.

**11:50 AM** -- Namita confirms: "Yes, VPN is connected."

At this point, the VPN + Chrome + Duo workaround is fully tested and confirmed non-functional. Namita takes initiative and calls Cisco Support herself.

**12:42 PM** -- Namita returns with a critical discovery from Cisco Support:

> "Support message: Please noted that learn.cisco.com is migrated to new platform -- skillstudio.cisco.com. You need to login from skillstudio.cisco.com and then only you can access the course."

This is the first time anyone on the team learns that learn.cisco.com has been migrated. The original training link was pointing to a deprecated platform. The VPN, Chrome, and Duo troubleshooting were all irrelevant -- the URL itself was the problem.

**12:43 PM** -- Namita immediately follows up with the logical next question: "Do we have a corresponding course in skillstudio? I am unable to locate NX Github course on skillstudio.cisco.com"

The course ID from the original link (`COT00325705`) does not resolve on the new platform. The migration was not a simple URL swap -- the course either has a different identifier on skillstudio.cisco.com, or was not migrated at all.

**2:05 PM** -- Colin (as cmoore@bayone.com), apparently not having seen Namita's 12:42 PM discovery about the platform migration, asks if she is using the complete URL with the courseID parameter, not just the base learn.cisco.com domain.

**2:21 PM** -- Namita confirms: "Yes, tried the complete link."

**2:23 PM** -- Colin (as cmoore@bayone.com) acknowledges Namita's finding and escalates: "I just connected with Srinivas; it looks like you are correct and the link is pointing to a now deprecated training. I am getting the correct link from Srinivas and Divakar right now and will share shortly."

The thread goes silent again. Srinivas and Divakar apparently did not have the correct link readily available.

### Day 9: April 9, 2026 -- Resolution Through Justin

Two days after Colin escalated to Srinivas and Divakar, the resolution comes through a different person entirely.

**4:34 PM** -- Namita shares a meeting (visible as a WebEx meeting share message). This appears to be the call with Justin, Naga, and Divakar that both Namita and Srikar participated in.

**7:30 PM** -- Namita posts the correct training course link, obtained from Justin:

> `https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8`

**7:31 PM** -- Namita immediately notes: "However, I don't have access to it. I will call support and check."

Even with the correct URL, access is not automatically granted.

**7:31 PM** -- Namita shares the access mechanism Justin provided:

> "Justin mentioned: For the nx github you have to request access to **A2G_group** @ **https://oneaccess.cisco.com**"

**7:35 PM** -- Colin (as colmoore@cisco.com) acknowledges the breakthrough: "Great work, Namita! Team, please review the transcript from the call with Justin, and let's see if we can figure out how to get access to the A2G_group as Namita shared above."

---

## Complete URL and Access Method Inventory

### URLs Attempted

| URL | Platform | Status | Outcome |
|-----|----------|--------|---------|
| `https://learn.cisco.com/?courseID=COT00325705` | learn.cisco.com (deprecated) | Dead link | Platform migrated to skillstudio.cisco.com. Course ID does not resolve. |
| `https://skillstudio.cisco.com` | skillstudio.cisco.com | New platform | NX GitHub course could not be located by searching. No known course ID mapping from the old platform. |
| `https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8` | edcast.com | Correct link | Provided by Justin on 4/9. Requires A2G_group membership to access. |
| `https://oneaccess.cisco.com` | oneaccess.cisco.com | Access portal | Where to request A2G_group membership. |

### Authentication Methods Attempted

| Method | Who Tested | Date | Result |
|--------|-----------|------|--------|
| Direct link (no VPN) | Multiple team members | 4/1 | Failed |
| Link with Cisco VPN connected | Askari | 4/2 | Failed |
| Chrome via Mac @ Cisco Self Service + Duo enrollment + VPN | Namita | 4/7 | Failed |
| Calling Cisco Support (+1-408-526-8888) | Namita | 4/7 | Revealed platform migration but did not grant access |
| A2G_group request via oneaccess.cisco.com | Pending | 4/9+ | Identified as the correct path by Justin |

### Support and Contact Information Gathered

| Resource | Detail |
|----------|--------|
| Cisco Support Phone | +1-408-526-8888 (24/5, excluding specific holidays) |
| Cisco Support Process | Share Cisco email ID, support will screen share to resolve |
| A2G_group access request | https://oneaccess.cisco.com |
| Correct training URL | https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8 |

---

## The DeepSight Training: The Control Case

The DeepSight Atlas training video was shared on the same day (4/1) as the GitHub training link and experienced zero access problems:

- **URL:** `https://cisco.webex.com/cisco/ldr.php?RCID=4450a31e35a93f8e14da79e99ba02ff8`
- **Password:** `JjDPKxG2`
- **Hosted on:** WebEx (Cisco's own platform, already authenticated via team membership)
- **Result:** Srikar watched it the same evening and posted detailed notes.

The difference: the DeepSight video was a WebEx recording link, which the team already had authentication for by virtue of being in the Cisco WebEx space. The GitHub training was hosted on an internal learning platform that had been silently deprecated and migrated, with the course not properly transferred to the new platform, and access gated behind a group membership that no one on the team had.

---

## What Actually Happened: The Platform Migration

Cisco's internal learning management system underwent a migration during or before the engagement:

1. **learn.cisco.com** was the original platform hosting the NX-OS GitHub training (course ID: COT00325705).
2. **learn.cisco.com migrated to skillstudio.cisco.com.** Cisco Support confirmed this directly to Namita on 4/7.
3. **The specific NX-OS GitHub course was not findable on skillstudio.cisco.com.** Namita searched and could not locate a corresponding course.
4. **The actual training content ended up on edcast.com** (a third platform), under a completely different URL scheme using an ECL identifier rather than a COT course ID.
5. **Access to the edcast.com content requires membership in A2G_group**, which must be requested through oneaccess.cisco.com -- a fourth platform.

The team was troubleshooting authentication (VPN, Duo, Chrome) when the actual problem was that the content had moved to a different platform entirely. No amount of correct authentication would have made the original link work.

---

## Who Did What

### Colin Moore
- Shared the original (deprecated) link on 4/1
- Relayed the VPN hypothesis from Srinivas on 4/1 (incorrect)
- Shared the Cisco Support phone number on 4/6
- Discovered and shared the Chrome/Duo workaround on 4/7 (did not resolve the issue)
- Escalated to Srinivas and Divakar on 4/7 after Namita confirmed the link was deprecated
- Did not have the correct link as of 4/7; Srinivas and Divakar also did not have it readily

### Namita Mane
- Tested the Chrome/Duo workaround on 4/7 (failed)
- Called Cisco Support independently on 4/7 (discovered the platform migration)
- Reported the skillstudio.cisco.com migration to the team on 4/7
- Identified that the course could not be found on skillstudio.cisco.com on 4/7
- Obtained the correct edcast.com link from Justin on 4/9
- Obtained the A2G_group access path from Justin on 4/9
- Tested the correct link and confirmed she still lacked access on 4/9

### Askari Sayed
- Tested the VPN hypothesis on 4/2 and falsified it. This is his only visible contribution in the entire chat log.

### Srikar Madarapu
- Not directly involved in the training troubleshooting, but his same-day success with the DeepSight training video provides the contrast case.

### Srinivas (Cisco manager, not in the team space)
- Suggested the VPN hypothesis to Colin on 4/1 (incorrect)
- Was escalated to on 4/7 when the link was confirmed deprecated
- Did not produce the correct link; it ultimately came from Justin

### Justin (Cisco team member)
- Provided the correct edcast.com training link to Namita on 4/9
- Provided the A2G_group access mechanism on 4/9
- Was the only person in the entire chain who knew where the training actually lived

---

## Operational Lessons

### 1. Cisco's Internal Platforms Are Fragmented and Actively Migrating

The resolution of this single training link involved **four distinct Cisco platforms** (learn.cisco.com, skillstudio.cisco.com, cisco.edcast.com, oneaccess.cisco.com) and **two different course identification schemes** (COT and ECL). No single person on the Cisco side -- not Srinivas, not Divakar -- had the correct information until Justin was consulted directly. This fragmentation is not unique to the training link; it is a systemic characteristic of working inside Cisco.

### 2. VPN Is the Default Cisco Explanation for Everything

Srinivas's initial response to the access issue was "try VPN." This turned out to be completely wrong -- the content had moved to a different URL. The VPN hypothesis cost the team at least a day (4/1 to 4/2) before Askari falsified it. In a large enterprise, "are you on VPN?" is the reflexive first-tier support response, and it must be tested quickly and discarded when it does not work, rather than treated as the likely answer.

### 3. Namita's Independent Initiative Was the Breakthrough

The resolution came because Namita did not wait for instructions. She independently called Cisco Support (after Colin suggested it), independently discovered the platform migration, independently pursued the correct link through Justin, and independently reported the A2G_group access mechanism. Without her initiative, the team would still be waiting for Srinivas and Divakar to produce the correct link.

### 4. The Original Link Provider Did Not Know It Was Deprecated

Colin shared the learn.cisco.com link from Srinivas (or from materials Srinivas provided). Neither Colin nor Srinivas knew the link was deprecated at the time it was shared. This is a common pattern in large organizations: links persist in documentation, wikis, and email threads long after the underlying resource has moved. The lesson is that any Cisco-provided link to internal tooling should be verified by actually attempting access before distributing it to the team.

### 5. Access Is Always Multi-Layered

Even after finding the correct URL, Namita could not access it. The training required A2G_group membership, which required a separate request through oneaccess.cisco.com. This is consistent with the access pattern documented in the Set 01 blockers analysis: every system at Cisco requires its own request, approval, and often a group membership. There is no single "onboard a contractor" process that grants access to all necessary resources.

### 6. The Working Link Provides a Template

The DeepSight training video worked immediately because it was hosted on WebEx, which the team already had access to. For future resource sharing, hosting on platforms the team already authenticates to (WebEx, shared drives they can already reach) avoids the access labyrinth entirely. When that is not possible, the person sharing the link should verify it works from a contractor account before distributing it.

---

## Timeline Summary Table

| Date | Time | Who | Action | Result |
|------|------|-----|--------|--------|
| 4/1 | 9:16 AM | Colin | Shares learn.cisco.com training link | Link does not work for team |
| 4/1 | 9:17 AM | Colin | Shares DeepSight Atlas video link | Works immediately |
| 4/1 | 6:59 PM | Srikar | Posts DeepSight training notes | Confirms DeepSight link works fine |
| 4/1 | 7:06 PM | Colin | Relays VPN hypothesis from Srinivas | Team directed to try VPN |
| 4/2 | 9:39 AM | Askari | Reports VPN does not help | VPN hypothesis falsified |
| 4/6 | 8:54 PM | Colin | Posts Cisco Support number (+1-408-526-8888) | Provides escalation path |
| 4/7 | 11:05 AM | Colin | Posts Chrome/Duo workaround via Mac @ Cisco Self Service | New approach shared |
| 4/7 | 11:46 AM | Namita | Tests Chrome workaround, reports failure | Workaround does not work |
| 4/7 | 11:48 AM | Colin | Asks Namita to confirm VPN + Chrome | Troubleshooting continues |
| 4/7 | 11:50 AM | Namita | Confirms VPN connected, Chrome used | All known approaches exhausted |
| 4/7 | 12:42 PM | Namita | Reports Cisco Support finding: learn.cisco.com migrated to skillstudio.cisco.com | Root cause identified |
| 4/7 | 12:43 PM | Namita | Reports NX GitHub course not found on skillstudio.cisco.com | Correct link still unknown |
| 4/7 | 2:05 PM | Colin | Asks if full URL was used (not just base domain) | Checking for user error |
| 4/7 | 2:21 PM | Namita | Confirms full URL was used | User error ruled out |
| 4/7 | 2:23 PM | Colin | Confirms link deprecated, escalates to Srinivas and Divakar | Awaiting correct link |
| 4/9 | 4:34 PM | Namita | Meeting with Justin/Naga/Divakar | Context for link discovery |
| 4/9 | 7:30 PM | Namita | Shares correct link from Justin (cisco.edcast.com) | Correct URL obtained |
| 4/9 | 7:31 PM | Namita | Reports she cannot access the edcast link | Access still blocked |
| 4/9 | 7:31 PM | Namita | Shares A2G_group requirement via oneaccess.cisco.com | Access mechanism identified |
| 4/9 | 7:35 PM | Colin | Acknowledges, directs team to pursue A2G_group access | Action item for team |

---

## Connection to Broader Access Friction Pattern

This saga is one instance of a pattern that repeats across every system the team needs. The Set 01 blockers analysis documented nine separate access-related items (ADS machines, GitHub repos, NFS, MySQL, DeepSight repos, DeepSight platform, training courses, BayOne laptops, and Colin's Cisco laptop). The training access issue demonstrates the pattern in miniature:

1. **A link or resource is provided by a Cisco manager.** (4/1: learn.cisco.com link from Srinivas)
2. **It does not work, and the initial diagnosis is wrong.** (4/1: "try VPN")
3. **Multiple troubleshooting attempts consume days.** (4/2 through 4/7: VPN, Chrome, Duo, support calls)
4. **The real issue is structural, not technical.** (Platform migration, not authentication)
5. **Resolution requires finding the right person at Cisco.** (Justin, not Srinivas or Divakar)
6. **Even with the right information, another access gate appears.** (A2G_group membership required)
7. **Access is individual, not team-wide.** (Each person must request A2G_group separately)

This is the friction tax on every new system. The training saga consumed nine calendar days for what should have been a zero-friction onboarding step. When multiplied across all the systems the team needs access to, this pattern is the single largest constraint on the engagement's velocity.

---

## Open Items as of 4/9

1. **A2G_group access:** No team member has confirmed successful enrollment in A2G_group via oneaccess.cisco.com.
2. **Training completion:** No team member has confirmed watching the NX-OS GitHub training video on edcast.com.
3. **Whether all team members have the correct link:** Colin directed the team to pursue A2G_group access on 4/9, but individual confirmation of access is pending.

**Note:** By 4/15, Srikar reported receiving access to the CI/CD team on Cisco's internal GitHub (`https://wwwin-github.cisco.com/orgs/DeepSight/teams/ci-cd`), which is the actual repository access (distinct from the training video). The training video access status remains unconfirmed in the chat log.
