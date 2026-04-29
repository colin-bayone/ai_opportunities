# Prep recap: Srikar's status going into the Wednesday Srinivas meeting

**For:** Wednesday 2026-04-29 Srinivas meeting
**Source folder:** `/cisco/cicd/team/source/week_2026-04-27/day_2026-04-29/srikar/`
**Files captured:**
- `github.txt` — GitHub comments from issues 14 and 15
- `srikar.txt` — same content as github.txt (slight overlap)
- `image.png` — SSH terminal screenshot showing the REALM access wall on `divvenka-qa-1`

---

## What Srikar reports

**Issue 14 (CAT MCP / data path):** Justin shared a working MongoDB endpoint URL: `http://sjc-ads-20375:9000/db/chatbot_ai/github_pr_status?key=pr_number&value=88861&type=N`. The endpoint returns the status of a PR with all checks (42 in the example). Srikar's read: based on this, an MCP server can be created on top of Justin's MongoDB and made available for our use. This is a concrete unblock on the dynamic answer data path question; Justin delivered.

**Issue 15 (static answers):** Srikar did not produce the analysis deliverable. Instead he built a new `wiki-issue-responder` skill on the `skills/webex` branch with three CLI scripts (`sync_wiki.py`, `build_wiki_index.py`, `query_wiki.py`) plus updates to `issue-response-router` to add wiki-routing logic, regex-based PR/CAT/job identifier detection, and a `has_dynamic_identifiers()` helper to separate static from dynamic requests. Substantive work, but not the deliverable on the issue.

Colin called this out in the issue thread two hours before this prep recap was written:
> "This is good progress, @srmadara! However, remember that we have an analysis deliverable for this issue, not a skill. The analysis deliverable is due today as specified above. The skills are definitely useful, but they don't negate the specific deliverables listed in the issue. Please connect with me on this one ASAP."

Followed by:
> "That analysis is a chart, just like we did the HTML for Apache ECharts."

The deliverable is the static-vs-dynamic breakdown chart from the Monday meeting (the analysis Srinivas asked for). The chart is what should land today, not the wiki responder skill.

## Access blocker (separate from issue 15)

The screenshot shows Srikar's SSH attempt to `divvenka-qa-1`. Same REALM wall as Colin: the host is locked behind `INS-SW-BUILD` and `CN-SJC-STANDALONE` bundles. Per the WebEx engagement chat, Srikar re-submitted the access request Tuesday evening and got the user-groups email pointing him to `oneaccess.cisco.com` and `myid-groups.cisco.com`. As of this prep document Srikar has not confirmed access has resolved.

## Read for today's meeting

Two distinct threads on Srikar's status:

1. **The data path question is in better shape.** Justin's MongoDB endpoint works and the MCP layer on top is now a concrete next step. This is a real unblock for the CAT MCP integration issue.

2. **The analysis deliverable for issue 15 is off-track.** Srikar built skills instead of the chart. Colin has already flagged this in the issue thread and asked Srikar to connect ASAP. Today's meeting is the natural forcing function for landing the chart.

## Concrete asks for the team meeting

- Confirm Srikar has access to the ADS machines (or that his user-group membership is in motion)
- Bring the static-vs-dynamic chart to landing for today; the wiki responder skill is parallel work, not the deliverable
- Acknowledge Justin's MongoDB unblock; thread that into the CAT MCP integration work
