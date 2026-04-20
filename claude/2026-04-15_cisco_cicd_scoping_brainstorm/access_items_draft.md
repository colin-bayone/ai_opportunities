# Outstanding Access Items — Draft for Colin's Review

**Source:** Team sub-singularity (Set 01, April 10), blockers tracker, session handoff, org chart, and Colin's April 15 updates.

**Purpose:** Colin to review and update current status before team meeting. Items marked with "?" need Colin to confirm whether they have been resolved since April 10.

---

## Items from Team Tracking + Research (as of April 10, updated with April 15 context where known)

| # | System/Item | Status as of Apr 10 | Apr 15 Update (if known) | Who Controls It |
|---|-------------|---------------------|--------------------------|-----------------|
| 1 | **Permanent ADS server** | Blocked. DCN Switching tenant not available in managecisco.com. Chatbot support contacted, no response. Temporary 4-week access granted Apr 10 (expires ~May 8). | Still pending per Colin's email draft. Temp machine is a stopgap only. | Cisco support / tenant provisioning |
| 2 | **DeepSight platform access** | Blocked. Team cannot see apps running on DeepSight or deploy to it. Depends on ADS access. | Colin raised this with Srinivas on Apr 15. Srinivas acknowledged and said he asked current team to wrap up compose files for production. | Srinivas |
| 3 | **DeepSight CI/CD repo** | Not discussed Apr 10. | Srinivas shared `https://wwwin-github.cisco.com/DeepSight/ci-cd` on Apr 15. Said team should be able to take over once compose files are done. | Srinivas |
| 4 | **Pulse and Scribble repos** | Blocked. Naga said Srinivas must grant access. | ? (Was this raised in the Apr 11 Srinivas meeting?) | Srinivas |
| 5 | **GitHub Enterprise write access** | Read access granted Apr 10 (A2G group). No write access. | ? (Colin mentioned "GitHub Enterprise read access" was just received, possibly referring to the ci-cd repo on Apr 15) | Divakar / GitHub admin |
| 6 | **NFS log storage** | Dependent on ADS access. Logs at `/auto/ins-bld-tools/branches/nx_main/nexus/togs/`. Only accessible through ADS machines. | Should be accessible via temporary ADS. Needs verification. | Accessed through ADS |
| 7 | **MySQL database (build metadata)** | Not yet requested as of Apr 10. Team focused on logs first. | ? | Justin's team |
| 8 | **CAT databases (Cassandra)** | Anupma (DevEx) guarded about exposing. Redirected discussion offline in Apr 2-3 meeting. | ? | Anupma Sehgal (DevEx) |
| 9 | **Cisco training courses** | Permission denied. Request raised with support, no response. | ? | Cisco training platform |
| 10 | **VPN access** | Was listed as a need in early onboarding. | ? (Presumably resolved since team is working, but confirm) | Cisco IT |
| 11 | **Airflow access / SME identification** | Airflow SME still not identified. Divakar said he has nothing to do with Airflow. | Still unknown as of Apr 15. | Unknown |
| 12 | **Individual access problem** | All access is individual, not team-wide. Each person must request separately for every system. Multiplies onboarding time. | Ongoing structural issue. | Cisco process |
| 13 | **Saurav's Cisco laptop** | Working as of Apr 10. | Bricked Apr 14 after mandatory update. Loaner picked up Apr 16 (heavily used M1, non-functional keys, sticky residue). Two weeks of work lost. | Cisco IT |
| 14 | **Colin's Cisco laptop** | Listed as "not yet received" in Apr 10 standup. | Colin had it by late March per session handoff. Unclear if this was resolved by Apr 10 or if it is a different device. | Cisco IT |
| 15 | **BayOne laptops for Srikar and Namita** | Not received. Overdue by 1+ month. Colin escalating to BayOne IT. | ? | BayOne IT (RIT) |

---

## Notes for Colin

- Items 1, 2, 4, 6, 11, and 12 are the ones that most directly block delivery and would be strongest in the email to Anand/Srinivas.
- Item 12 (individual access) is the structural problem that makes everything else worse. Every new team member multiplies every other access item.
- The Saurav laptop (item 13) is already covered in the email body. The list should focus on systemic access items, not one-off hardware.
- Some of these may have been resolved in the Apr 11 Srinivas meeting or the Apr 15 conversations. Colin's team meeting this morning will clarify current state.
