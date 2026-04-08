# 07 - Chat: Blocker Analysis

**Source:** /cisco/cicd/source/webex_group_chat_2026-02-10.txt
**Source Date:** 2026-02-10 to 2026-03-31
**Document Set:** 07 (External communications record)
**Pass:** Access blockers, delays, and what has/hasn't moved

---

## Blocker 1: SOW Procurement

**Status at end of record:** Resolved

| Date | Event |
|------|-------|
| Pre-Feb 10 | SOW already pending. Engagement created before SOW is approved. |
| Mar 3 | Zahra: "still working on getting the SOW approved for the US where Colin is on. It's pending approved on Cisco side." Working with Mahvir and Vidya. "Told this should be fully approved this week." |
| Mar 13 | Colin: "The procurement delay on the SOW is fully resolved. That was the single blocker." |

**Duration:** Unknown start to Mar 13 resolution. At minimum 31 days from group creation to resolution. Zahra attributed the delay entirely to Cisco-side procurement and offshore team availability.

**Impact:** This was positioned as the reason nothing else could start. Colin's Mar 13 message calls it "the single blocker." However, SOW resolution did not actually unblock the access items — those remained stuck for an additional 18+ days through end of record.

---

## Blocker 2: Hardware

**Status at end of record:** Resolved (Colin has hardware; India team status unclear)

| Date | Event |
|------|-------|
| Mar 13 | Colin: "India team are picking up their equipment by 3/16, and the onshore team, myself included, have hardware in transit for mid next week delivery." |
| Mar 25 | Colin: "I now have my Cisco hardware in hand and have finished the setup and completion." |
| Mar 26 | Zahra: "Colin is all set up as of yesterday. He has the laptop and Webex up and running." |

**Duration:** Hardware arrived to Colin between Mar 18-25. India team pickup was scheduled for Mar 16.

**Impact:** Hardware was a prerequisite for access items. Once Colin had it, he immediately posted the access list again. Hardware is resolved, but everything downstream of it is not.

---

## Blocker 3: Access Items — The Identical List

This is the central finding. Colin posted an access needs list on **Mar 13** and again on **Mar 25**. The lists are nearly identical, meaning no visible progress on any item in 12 days.

### Mar 13 List

> - GitHub Enterprise training, the 3-4 hour prerequisite before repo access can be granted
> - ADS Linux machine provisioning so we can check out and build code
> - VPN setup and network access
> - DeepSight platform repo access and integration onboarding with Srini's team

### Mar 25 List

> - GitHub Enterprise training, the 3-4 hour prerequisite before repo access can be granted
> - ADS Linux machine provisioning so we can check out and build code
> - VPN setup and network access
> - DeepSight platform repo access and integration onboarding with Srini's team
> - If different from DeepSight access, some discussion with Srinivas on AI tool access/ assignment so we are using Cisco-provided endpoints and subscriptions from day 1

**What changed:** One item added (AI tool access). Four items carried over verbatim. No indication any of the original four have started, are in progress, or have been assigned to anyone.

### Individual Access Item Status

| Item | First Mentioned | Owner/Path | Status at Mar 31 |
|------|----------------|------------|-------------------|
| GitHub Enterprise training | Feb 17 (Divakar sent link) | Divakar sent the training URL. Completion is a prerequisite for repo access. | Unknown if anyone has completed the 3-4 hour training. Colin lists it as still needed on Mar 25. |
| ADS Linux machine provisioning | Mar 13 (Colin's list) | Divakar noted as knowing this process. Colin flagged "can take a bit to work through." | No progress visible. Divakar was absent. |
| VPN setup and network access | Mar 13 (Colin's list) | Standard Cisco onboarding item. | No progress visible. |
| DeepSight platform repo access | Mar 13 (Colin's list) | Requires Srinivas's team. | No progress visible. Srinivas silent in chat since Feb 17. |
| AI tool access/assignment | Mar 25 (new addition) | Srinivas. | Just raised. No response. |

---

## Blocker 4: Divakar's Absence

**Status at end of record:** Divakar returned Mar 27, offered to meet starting Monday (Mar 30)

Divakar is the single point of contact for onboarding mechanics — he added Colin to the space, he sent the GitHub training link, and Colin identified him (in the Mar 13 message) as the person who knows ADS provisioning.

| Date | Event |
|------|-------|
| Feb 17 | Last substantive contribution (adds Colin, shares GitHub link) |
| Mar 26 | Anand asks: "Divakar - if you are back today, can you please help?" — implies known absence |
| Mar 27 | Divakar: "I am back today onwards, I can meet starting Monday" |

**Duration of absence:** At minimum Mar 18 to Mar 27 (10 days). Possibly longer — no messages from him between Feb 17 and Mar 27 (38 days of silence in the chat).

**Impact:** The access items that require Divakar (GitHub repo access post-training, ADS provisioning) could not progress while he was out. No backup or delegate was identified. Anand's addition of Shih-Ta Chi on Mar 26 is an explicit workaround for Divakar's absence.

---

## Blocker 5: Shih-Ta Chi — Unknown Quantity

**Status at end of record:** Added to group, no messages from them

| Date | Event |
|------|-------|
| Mar 26 | Anand adds Shih-Ta Chi: "Adding Shih-Ta in my team, who can get someone to help on general onboarding." |
| Mar 26 | Colin: "Great! I will message Shih-Ta" |

Shih-Ta is described as someone who "can get someone to help" — not as the person who will directly help. This is a referral chain, not a direct unblock. No messages from Shih-Ta appear in the chat record.

---

## Unresolved Technical Items

### Rui's CI/CD Deliverable Handoff

| Date | Event |
|------|-------|
| Mar 25 | Colin: "I believe that Srini had mentioned that there was a team that was working on a CI/CD deliverable that would be wrapping up around now and being deployed on DeepSight-- I believe the idea was that we would use that as a starting point and build off of it. If that is still the case, we would need to connect to that team as well!" |

**Status:** Raised by Colin. No response or acknowledgment in chat. "I believe" phrasing suggests this was discussed verbally (likely in the Feb 17 discovery session, per Set 06) but never confirmed in writing. The handoff team is unnamed and unconnected.

### Airflow SME Identification

| Date | Event |
|------|-------|
| Mar 25 | Colin: "we would also want to identify the Airflow owner/ SME so we can start building with DeepSight and have all the tool access needed to tie it into the broader CI/CD lifecycle." |

**Status:** Raised by Colin. No response in chat. Airflow integration is part of the CI/CD pipeline work, and without an SME identified, the team cannot begin design work on that component.

### IC-Level Discovery Meetings

| Date | Event |
|------|-------|
| Mar 25 | Colin: "we are finally ready for the IC-level discovery meetings, starting with understanding more deeply the local developer box life cycle from the viewpoint of a local developer." |

**Status:** Requested by Colin. No scheduling or response in chat. These meetings require Cisco ICs to participate — none have been identified or connected.

---

## Summary of Blocker Movement

| Blocker | Feb 10 | Mar 3 | Mar 13 | Mar 25 | Mar 31 |
|---------|--------|-------|--------|--------|--------|
| SOW | Pending | Pending, "this week" | **Resolved** | Resolved | Resolved |
| Hardware | Not started | Not discussed | In transit | **Resolved** (Colin) | Resolved |
| GitHub training | Link shared Feb 17 | Not discussed | Listed as needed | Listed as needed | No change |
| ADS provisioning | Not started | Not discussed | Listed as needed | Listed as needed | No change |
| VPN | Not started | Not discussed | Listed as needed | Listed as needed | No change |
| DeepSight access | URL shared Feb 17 | Not discussed | Listed as needed | Listed as needed | No change |
| Divakar available | Present Feb 17 | Silent | Silent | Silent | **Back Mar 27** |
| Rui handoff | Not raised | Not raised | Not raised | Raised | No response |
| Airflow SME | Not raised | Not raised | Not raised | Raised | No response |

The pattern: procurement and hardware blockers eventually resolved through normal process. Every blocker that requires a Cisco person to take action (access provisioning, team connections, SME identification) has not moved.
