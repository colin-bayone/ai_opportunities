# 02e - Saurav Communication: Cisco Hardware Failure (Blocker)

**Source:** /cisco/cicd/team/source/week_2026-04-14/day_2026-04-16/saurav/saurav_email.txt
**Source Date:** 2026-04-15 (email sent 3:59 PM, from Saurav to Colin)
**Document Set:** 02e (supplementary to Set 02, individual team member communication)
**Pass:** Full decomposition of hardware failure incident, timeline, and impact

---

## Incident Summary

On April 14, 2026, Saurav's Cisco-issued MacBook failed to boot after a macOS software update. The device has not recovered despite multiple troubleshooting attempts. This is now a blocker for Task 1 (WebEx Space Scraper) and affects 10-12 days of concentrated development work that may need to be rebuilt from scratch.

**Ticket:** INC10796337
**Priority:** 5 — Standard (Saurav was unable to escalate through support channels)
**Status as of 4/15 3:59 PM:** Loaner laptop promised from Cisco Delhi office, no confirmation of pickup time or process

---

## Timeline

### April 14, 2026 (Monday)

- **Afternoon:** Saurav was working on WebEx integration (Wall-E/Volley development) when a macOS update notification appeared
- **Updated per Cisco mandatory training:** Cisco's own training advises updating immediately as updates may contain critical patches
- **Device did not come back online** after required restart. Has not booted since.
- **Independent troubleshooting:** Charging, forced restarts across different power states. All unsuccessful.
- **~7:20 PM IST:** Contacted Cisco IT support. Walked through same troubleshooting already completed. Asked to install WebEx on personal phone for case communication.
- **~11:00 PM IST:** Received automated case creation. Ticket INC10796337, Priority 5 (Standard), Assigned to: Unassigned.
- **Requested priority escalation.** Denied — agent said they cannot modify priority on a ticket belonging to another department.

### April 15, 2026 (Tuesday)

- **9:20 AM IST:** Ticket assigned to a support agent
- **3:30 PM IST:** First substantive communication from assigned agent — over 6 hours after assignment. Walked through same troubleshooting a third time.
- **Additional troubleshooting requested:** Plug USB-C cable into each of 3 ports individually, minimum 30 minutes each, attempt power-on after each.
- **~6:00 PM IST:** Saurav reported troubleshooting results. No response since.
- **Loaner laptop offered:** Agent indicated she would arrange a loaner (same model/make) from the Cisco Delhi office for next-day collection. Shared contact details of Delhi office service desk analyst.
- **Saurav proactively contacted Delhi office** with questions about collection time, process, and whether to bring faulty device. No response received.
- **3:59 PM IST:** Saurav sent this email to Colin documenting the full situation.

---

## Work at Risk

The failed MacBook contains approximately 10-12 days of concentrated development and research work:

1. **Wall-E/Volley prototype** — The working WebEx scraper bot that was demonstrated in the team space on 4/10. This is the most tangible deliverable from the entire team for Task 1.
2. **Exploratory research and technical investigation** — The research that informed the WebEx API integration design decisions.
3. **Environment setup and tooling configuration** — Cisco infrastructure-specific setup work.
4. **Reference documentation** — Project deliverable-related documentation.

Saurav states he is "treating this as lost and has begun planning to rebuild from scratch." The compounding effect on timeline is described as "immediate."

---

## Impact Assessment

### On Task 1 (WebEx Space Scraper)
- **Wall-E bot may need to be rebuilt.** If the laptop data is unrecoverable, the prototype that was deployed and demonstrated on 4/10 is gone. Saurav would need to recreate it from memory and any code that was pushed to remote repositories.
- **Open question:** Was the Wall-E code pushed to any remote repo (personal GitHub, Cisco internal GitHub, etc.)? If the code only existed on the local machine, it is lost. If it was pushed, only the local environment setup is lost.

### On Team Velocity
- **Saurav is working from his BayOne machine** but states "there is a hard limit on what can be done without the Cisco device." The Cisco machine has VPN access, Cisco-internal tools, and the development environment configured for Cisco infrastructure.
- **10-12 days of rebuild time** would push deliverables back significantly. With the April 30 contract renewal, this is a material risk.

### On Team Hardware Risk
- **Systemic risk:** Cisco support confirmed that contracted (red badge) employees receive refurbished hardware. All BayOne team members with Cisco MacBooks (Srikar, Namita, and the offshore team) have the same refurbished hardware and face the same failure risk.
- **Repair timeline:** Minimum 1 month, typically 2-3 months. Cisco may decline repair entirely on refurbished devices based on cost.

---

## Repair and Recovery Outlook

| Scenario | Likelihood | Impact |
|----------|-----------|--------|
| Loaner laptop received quickly, data recovered from failed device | Low (repair 1-3 months, device may not be repairable) | Minimal — back to full speed |
| Loaner laptop received quickly, data unrecoverable | Medium | 10-12 days rebuild; Wall-E may need recreation |
| Loaner laptop delayed | Medium (no confirmation yet, Delhi office unresponsive) | Extended period working from BayOne machine only |
| No loaner provided | Low | Severe impact; limited to BayOne machine indefinitely |

---

## Action Items for Colin

1. **Escalate the ticket priority.** Saurav was unable to escalate through support channels. Colin (or Srinivas) may have the standing to request escalation from Priority 5 to a higher priority given business impact.

2. **Confirm code backup status.** Critical question: was the Wall-E/Volley code pushed to any remote repository? If yes, the rebuild is the environment, not the code. If no, the prototype needs to be recreated.

3. **Alert the team about refurbished hardware risk.** All contractor devices are refurbished. Team members should be advised to push code to remote repos frequently and not rely on local-only storage.

4. **Consider requesting non-refurbished hardware.** Through Srinivas or Anand, request that the BayOne team receive standard (non-refurbished) hardware given the active project timeline.

5. **Track the loaner laptop status.** Saurav is waiting on confirmation from the Delhi office. If no response by end of 4/16, escalation is needed.

---

## Connection to Existing Blockers

This is a new high-severity blocker that compounds the existing access and hardware issues documented throughout Set 01 and Set 02:

- **Set 01 Action Item #7:** "Send BayOne laptops to Srikar and Namita" — Colin noted these "should have been done a month ago." Hardware logistics have been a persistent issue.
- **Set 01 Blocker:** "Colin does not have Cisco laptop yet" — hardware provisioning is a known bottleneck.
- **Set 02 Blocker:** Refurbished hardware is now confirmed as a systemic risk, not just a one-off inconvenience.

The hardware failure pattern across this engagement is escalating: slow provisioning → equipment not delivered → equipment delivered but refurbished → refurbished equipment fails → 1-3 month repair timeline. Each stage compounds the next.
