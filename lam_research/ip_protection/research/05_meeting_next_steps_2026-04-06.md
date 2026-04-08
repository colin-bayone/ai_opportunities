# 05 - Meeting: Next Steps and POC Scope

**Source:** /lam_research/ip_protection/source/meeting_brad_mikhail_daniel_4-6-2026.txt
**Source Date:** 2026-04-06 (Follow-up Discovery Meeting)
**Document Set:** 05 (Follow-up Meeting with Daniel)
**Pass:** Focused deep dive on next steps, POC scope, and commitments

---

## 1. POC Confirmed: Escalation Solver, Same Data, Same Goals

The group confirmed that the POC will target the same application, the same data, and the same success criteria as Lam's prior internal attempt. Brad was explicit on this point:

> "I think it makes sense to do it on the same approach with the same stuff with the same goals so we can compare."

The application is **Escalation Solver**, a homegrown platform within GFSO (Global Field Service Operations). It handles field engineer escalation tickets, containing both structured and unstructured data across multiple text fields. The prior internal attempt selected five free-text fields and attempted to detect and redact two specific entity types (customer name, fab ID) within those fields.

Brad further noted that the original effort started as a redaction use case, and the detection use case evolved from it during that work. The data set and application support proving out both detection and redaction:

> "This actually will be able to use the same data to prove out both detection and redaction."

Pat asked whether Lam wanted to consider a different application or data source that might have emerged as a higher priority in the intervening 18 months. Brad's response was definitive: this is the simplest, most straightforward use case, they tried it internally and could not achieve the required accuracy, and there is no reason to increase complexity before proving the baseline.

Daniel reinforced this from an architecture perspective: if the architecture is designed to be scalable and extensible, proving additional use cases becomes an iteration exercise rather than a rebuild.

---

## 2. Proposal Timeline

The proposal timeline was negotiated in the final minutes of the meeting. The sequence:

1. **Colin's initial commitment:** "The fastest that I'm going to be able to get it is probably tomorrow. The longest that I'm going to need is Friday. But I would say, with all things good, unless a tree falls and hits my car on the way home, I'm going to shoot for tomorrow."
2. **Pat's recommendation:** Pat advised against rushing. "I think not to rush in the corner. My recommendation is Friday, if that's okay." The group agreed to target delivery within the current week (by Friday, April 10).
3. **Brad's review timeline:** Brad indicated he would review the following week. He stated: "Now I know Friday and Monday, so I will take a look at it." He confirmed that by the following week (before the following Friday), he would be able to provide a thumbs up or down or feedback. Pat paraphrased this as "by the following Friday, at least we get a thumbs up or down or anything," and Brad confirmed: "I think by next week, if only I had it on Friday, next week before I didn't be able to."

**Net timeline:** Proposal delivered by end of week (targeting Friday, April 10). Brad reviews the following week and provides a go/no-go decision, likely by Friday, April 17 at the latest.

---

## 3. SOW and Legal Process

Brad raised the SOW/legal process proactively, describing it as a known step in Lam's engagement process:

> "I anticipate, right, that there's gotta be an SOW put in place, because Lam loves to, well, they love to get to report, but I think that we put all things through when they go, right, make sure that there's like nothing in there that they don't think that we're going to trip over."

He characterized the process as generally smooth and fast, based on prior experience:

> "Usually everything goes pretty smoothly, right? Because we've been doing this, well, we've had other engagements in other areas so long it seems to just flow through with paperwork, right? But we still need to do that. That usually takes a week or so, right?"

Key details:
- Lam has existing engagement frameworks from prior BayOne engagements in other areas
- The SOW review process typically takes approximately one week
- Brad does not anticipate any issues, but the step cannot be skipped
- The SOW executes in parallel with or immediately after the proposal approval

Pat reinforced that BayOne has never asked for a "blind check" -- the proposal will contain clear, definitive scope and pricing so Lam knows exactly what they are approving before any SOW is signed.

---

## 4. POC Duration: Two Weeks from Data Access

Colin provided a two-week POC estimate with explicit caveats:

> "For POC, we usually aim for about a two-week turnaround, but that is contingent upon both having good access to the data. I usually say from the date that we have the access that we need, two weeks."

The two caveats:

1. **Data access:** The two-week clock starts from the date BayOne has the access it needs -- not from proposal approval, not from SOW execution, but from actual hands-on data access.
2. **Data quality:** Colin added a second condition: "Making sure that that data is not loaded up with landmines, which in this case it does not sound like it's going to be at all." Based on what was described in the meeting (five text fields, existing thumbs-up/thumbs-down data, approximately 1,000 labeled examples already available), Colin did not anticipate data quality issues but preserved the caveat.

Colin also noted that the timeline is tentative until hands-on data review: "Until we get hands-on data and things, I always say it's a tentative timeline."

---

## 5. POC Produces the Full-Scale Estimate

Colin highlighted a dual benefit of the POC that is strategically important:

> "The benefit of the POC is we can tell you what the full scale would look like too. So we'll have enough of an idea when we see POC. We can say at least for that whole application what that timeline could look like as well for a full scope engagement."

This means the POC is not just a technical validation exercise. It also produces the data-informed estimate for the full engagement. BayOne will have enough hands-on understanding of the data, the infrastructure, and the complexity to scope the complete Escalation Solver deployment and potentially the broader multi-application rollout.

---

## 6. The Orion Dependency

Mikhail flagged a critical dependency on a team member named Orion (or a team led by Orion) for data access:

> "The majority of this outside of Mikhail is Orion, so just FYI. They're working on COS, so it's not that the team is not capable, it's a small team working on a supercritical project."

Mikhail indicated he could handle some of the data access requirements himself but that certain items would require Orion's direct involvement, specifically on the data side. Brad's phrasing ("data side reactions") suggests Orion controls or manages the data retrieval infrastructure or the data custodianship for the Escalation Solver application.

Mikhail's self-assessment was that he could handle "some of it" but not all: "I should be able to do some of it, but some things will require Orion's attention."

The group did not attempt to resolve this in the meeting. Pat framed it as a communication and scheduling problem rather than a blocker: "We just need to know what is needed and then we can look at, okay, how do we make that manage?" Brad agreed that defining the specific access requirements clearly would allow them to work around Orion's COS project schedule.

This dependency is the most likely source of delay between SOW execution and the start of the two-week POC clock. Orion's team is on a "supercritical" project, which means data access requests may have to wait or be handled piecemeal by Mikhail where possible.

---

## 7. Daniel's Note on Internal Dependencies

Daniel raised the broader issue of dependencies on other teams within Lam:

> "Also just consideration when it comes to timelines if there are any dependencies on other teams within Lam."

Pat acknowledged this as a known pattern from prior engagements: "A lot of times you get into this like wall with other teams, especially data, like who are the custodians of a variety of things." Pat noted that much of the capability development can happen within the immediate team's scope, but data access often requires coordination with teams that have competing priorities.

This was reinforced by the Orion example immediately following. The implication is that BayOne should plan for potential delays in data access even after the SOW is signed, and should define exactly what access is needed as early as possible so Lam can begin internal coordination.

---

## 8. Brad's Request: Redact Customer Names from All BayOne Documents

Brad made a specific, unambiguous request regarding BayOne's own documents:

> "And even in the documents that I sent, remove the customer names, just multiple customers. They'll call out those specifically. And if these documents go broader, which they probably will at some point, we want to redact any specific customer names out of it."

This request applies to all BayOne-produced documents related to this engagement -- the proposal, any analysis or deliverables, presentations, and any materials that might circulate within Lam. Brad's concern is that documents will eventually be shared beyond the immediate working group, and specific customer names (which may appear in example data, case study references, or problem descriptions) must be replaced with generic references (e.g., "multiple customers," "Customer A/B/C," or simply redacted).

Colin acknowledged this immediately: "So easy first redaction project for us. Remove the customer names."

This is an action item for Colin to apply retroactively to any documents already shared and prospectively to all future deliverables.

---

## 9. Lam IDs and System Access for BayOne Team

Colin raised the question of system access for BayOne personnel:

> "I don't know. I think everyone here but me has a Lam ID for things. But if we wanted to do things, that would also be something that would be a great thing to do early."

Colin framed this as something that would be helpful to initiate early in the process but did not push it as a hard requirement: "I won't force that. It's up to you if you want to continue with us after you see that proposal."

The implication is that Lam IDs or equivalent system access for BayOne team members would be needed for the POC (to access Escalation Solver data, to deploy to Azure environments, potentially to access the existing partially-decommissioned infrastructure from the prior project). No commitment was made on this in the meeting. It remains an open item that should be addressed during or immediately after SOW execution.

---

## 10. Data Access Through Existing Infrastructure

Mikhail disclosed that the infrastructure from the prior internal attempt has not been fully decommissioned:

> "From the last project, we've only partially spun down the old environment, so we still have access to it. Some of, I don't know if we stand on full envelope side of things, but Azure AI stuff is all up and running where actually we just disabled the hourly jobs and that's it. So that environment is fully out."

Additionally, Mikhail mentioned existing data retrieval jobs that could be re-enabled:

> "They have data, hourly data retrieval jobs that could get data out of the system."

This is significant for the POC timeline. It means:
- The Azure environment from the prior project still exists and can potentially be reused
- Data retrieval jobs already exist and only need to be re-enabled (they were disabled, not deleted)
- The infrastructure setup that would normally be a time-consuming precursor to a POC may already be substantially complete
- The primary barrier to data access may be permissions and Orion's availability rather than infrastructure buildout

---

## 11. Overall Engagement Sequence

Based on everything discussed, the end-to-end sequence from this meeting to POC completion is:

| Step | Owner | Duration | Notes |
|------|-------|----------|-------|
| 1. Proposal preparation | Colin (BayOne) | By Friday, April 10 | Pat recommended Friday rather than rushing |
| 2. Proposal review | Brad (Lam) | ~1 week (by April 17) | Brad reviews following week, provides go/no-go |
| 3. SOW/legal execution | Both parties | ~1 week | Lam has existing frameworks; Brad expects smooth process |
| 4. Data access provisioning | Mikhail, Orion (Lam) | Unknown | Orion on critical COS project; Mikhail can handle some items |
| 5. POC execution | Colin (BayOne) | ~2 weeks from data access | Contingent on data access and data quality |
| 6. Full-scope estimate | Colin (BayOne) | Delivered with POC results | POC informs the complete engagement estimate |

**Best-case timeline:** If the proposal is delivered Friday (April 10), approved by mid-following-week (April 15-16), SOW executes within a week (by April 23), and data access is granted promptly, the POC could complete by approximately May 7-9.

**Likely timeline:** The Orion dependency and SOW process introduce realistic delays. A more conservative estimate places POC completion in mid-to-late May.

**Critical path:** Data access is the gating item. The two-week POC clock does not start until BayOne has the access it needs, and that access depends on Orion's availability and Lam's internal prioritization.

---

## 12. Complete Commitment Register

| # | Commitment | Owner | Timeline | Status |
|---|-----------|-------|----------|--------|
| 1 | Deliver POC proposal | Colin (BayOne) | By Friday, April 10 | Open |
| 2 | Review proposal, provide go/no-go | Brad (Lam) | Following week (by ~April 17) | Pending #1 |
| 3 | Redact customer names from all BayOne documents | Colin (BayOne) | Immediate / ongoing | Open |
| 4 | Initiate SOW/legal process | Both parties | After proposal approval | Pending #2 |
| 5 | Define specific data access requirements | Colin (BayOne) | In proposal or immediately after | Open |
| 6 | Provision data access (re-enable retrieval jobs, grant access) | Mikhail / Orion (Lam) | After SOW | Pending #4 |
| 7 | Explore Lam ID / system access for BayOne team | Lam (Brad/Mikhail) | Early in process | Open, not firmly committed |
| 8 | Execute POC | Colin (BayOne) | ~2 weeks from data access | Pending #6 |
| 9 | Deliver full-scope engagement estimate | Colin (BayOne) | With POC results | Pending #8 |
| 10 | Share today's presentation/slides with Lam team | Colin (BayOne) | After meeting | Open |
