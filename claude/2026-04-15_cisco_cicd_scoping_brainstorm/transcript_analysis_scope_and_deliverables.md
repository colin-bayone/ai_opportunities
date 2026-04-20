# Internal Scoping Prep — Scope Creep and Deliverable Risk

**Source:** claude/2026-04-15_cisco_cicd_scoping_brainstorm/source/internal_yikes_4152026_formatted.txt
**Date:** 2026-04-15 (internal BayOne meeting, pre-Anand call)

---

## The Scope Problem (Colin's Road Analogy)

Colin described the scope creep with this analogy: "Your contract is to go deliver a package down the road five miles. And we say, yeah, sounds good boss. And then they say, great, by the way, the road doesn't exist yet. So you're going to build that too."

### What Was Agreed

Six deliverables (A-F) spread across four quarters, built on the assumption that Srinivas's team had existing infrastructure (DeepSight apps, MCPs, databases) that BayOne would build on top of.

### What Actually Happened

When BayOne finally got access, none of the prerequisites were built. DeepSight CI/CD app is still not deployed as of April 15. Srinivas changed the scope from the six agreed items to three smaller, more granular tasks that are precursors to the original six. These are related work, not unrelated, but they are work that Cisco said was already done.

### The Defensibility Problem

Colin explicitly flagged this risk: if Cisco procurement comes after BayOne and says "you committed to six things and they are not done," BayOne has no defense. The scope change was verbal, driven by Srinivas, and does not appear to be documented in any formal change request.

Colin's specific language: "There's no way to make that defensible if procurement comes after us and says, hey, you said you do these six things, they're not done. We're stuck."

### What Colin Wants from the Anand Meeting

Two options to present:
1. Re-scope based on what reality is at Cisco (not what they want reality to be)
2. Agree to adjust deliverables to align with what Srinivas is actually directing BayOne to do

Either way, there needs to be a documented agreement that the A-F items are not the current measuring stick.

### Current Delivery Status

- First three Srinivas-directed deliverables: one delivering end of this week (April 18), remaining two end of next week (April 25)
- This is accelerated and both Srinivas and Anand are aware
- The original A-F items have not been started because the prerequisites do not exist

### The Cisco Culture Problem

Colin described Srinivas's team as "fairly toxic in terms of how they approach problems." Specific behaviors:
- "You're just not resourceful enough"
- "You should just figure it out because we're all building a giant platform"
- Scripts on someone's laptop being positioned to Anand as production-deployed solutions
- Anand is likely not aware of the actual state of his own team's projects

This is distinct from other Cisco teams Colin works with (e.g., the EPNM/EMS engagement does not have this dynamic).

---

## Timeline of Delays (All Cisco-Caused)

| Period | Duration | Cause |
|--------|----------|-------|
| Jan-Feb 2026 | ~2 months | SOW procurement delays |
| Mar 2026 | ~1 month | Hardware provisioning |
| Late Mar-Apr 2026 | Ongoing | Access provisioning (no process, whack-a-mole) |
| Apr 15 | New | Saurav's laptop died, IT says 2-month replacement |

Total time lost to Cisco-caused delays: approximately 3 months out of a 3-month quarter.
