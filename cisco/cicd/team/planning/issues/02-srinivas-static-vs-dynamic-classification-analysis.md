# Issue: NX-OS issue categorizer: classify unanswered questions as static or dynamic and add a six-month time window

**Repository:** https://wwwin-github.cisco.com/DeepSight/ci-cd
**Branch:** `skills/webex`
**Working folder:** `nxos-issue-categorizer/` (the skill is already on this branch; this issue extends it)
**Dependencies:** None blocking. The existing skill, database, and HTML report are sufficient inputs.

---

## Description

Srinivas asked for this analysis directly during the Monday Cisco-side sync. He redefined "static" and "dynamic" on the call and then asked the team to apply that distinction to the unanswered chat questions over the last six months. His exact framing: a question is **static** if it can be answered without consulting any database (for example, "how do I commit my code"), and **dynamic** if it requires looking up the state of a specific PR or build at the moment of asking (for example, "where is my PR stuck"). His goal is pain-point prioritization. Once the unanswered set is split into static versus dynamic, he can see which categories have the highest volume of well-known answers nobody is surfacing (low-hanging fruit for the wiki and the static FAQ path) and which have the highest volume of lookup-required questions (high-leverage targets for the dynamic answer path through CAT MCP and Justin's MongoDB).

The deliverable is the existing `nxos-issue-categorizer` dashboard, extended with a static-versus-dynamic dimension on each issue and a six-month time window that filters every chart in the report. The chart link goes back to Srinivas as the deliverable confirmation. The dashboard is already mature: 1,756 categorized issues across 78 categories, three years of data, ECharts-rendered HTML report with the data inlined as a JavaScript constant. This issue extends the skill rather than rebuilding it.

The classification dimension does not exist in the current schema. Resolution status is the only label today (`resolved`, `unanswered`, `ambiguous`, `NULL`). The static-versus-dynamic distinction is net new and has to be applied to every relevant issue, with priority on the unanswered subset since that is what Srinivas wants to see.

## Technical Approach

The current skill produces output through this path:

```
Webex CSV
    |
    v
import_csv.py -> raw_messages
    |
    v
thread_mapper.py -> root messages + threads
    |
    v
[per-batch agent run] -> batches/batch_NNN_categorized.md
    |
    v
merge_issues.py -> issues table
    |
    v
export_html.py -> report_weekly.html
```

This issue adds the static-versus-dynamic dimension at the issue level and a date-window filter at the report level. The cleanest approach extends the schema, the agent prompt, the merge step, and the HTML export. Sketch:

```
issues table
  + answer_type TEXT CHECK(answer_type IN ('static','dynamic',NULL))
  + index on (resolution_status, answer_type)

agent prompt (SKILL.md)
  + add the classification rule to the per-thread analysis
  + extend the YAML output format to include answer_type
  + use Srinivas's exact framing in the prompt so the
    classification is reproducible

merge_issues.py
  + parse answer_type from the batch markdown into SQLite

verify_batch.py
  + validate answer_type is in {'static','dynamic'} or absent

export_html.py
  + new chart: unanswered breakdown by static vs dynamic,
    grouped by top-level category (this is the chart for Srinivas)
  + new toggle: six-month vs all-time, applied to every chart
    via a single date filter at the data layer
  + new metric card: unanswered-static count, unanswered-dynamic
    count, both for the active window
```

The classification can run in two passes if needed. First pass: re-run the existing agent over batches with the extended prompt to populate `answer_type` for newly categorized issues. Second pass: a backfill agent run that reads each existing issue (its root message, replies, and `solution_pattern`) and assigns `answer_type` without re-categorizing. Decide which pass shape fits your timeline.

## Tasks

1. **Extend the schema.** On `skills/webex` under `nxos-issue-categorizer/`, add the `answer_type` column to the `issues` table in `init_db.py`. Add the supporting index. Commit and push directly to `skills/webex`. Push daily as the work progresses.

2. **Update the categorization prompt and validation.** Extend the agent prompt in `SKILL.md` (the per-thread analysis section) to include Srinivas's exact static-versus-dynamic definition. Extend the YAML output format to include `answer_type`. Update `verify_batch.py` to validate the new field. Update `merge_issues.py` to parse and store it.

3. **Backfill `answer_type` for existing issues.** Run a backfill agent over the existing 1,756 categorized issues (or at minimum the unanswered subset, which is the priority for Srinivas). The backfill reads the root message text and any thread replies and assigns `answer_type`. Capture the prompt and the run output in `nxos-issue-categorizer/backfill/` so the run is reproducible. The unanswered set is roughly 436 explicit unanswered rows plus the relevant slice of the 653 NULL rows; check whether the NULL rows need re-classification or can be left out.

4. **Add the six-month window toggle to the report.** In `export_html.py`, add a date-window filter applied at the data layer so every chart respects the active window. Default the report to the last six months. Include a UI control on the page that toggles between six-month and all-time views without regenerating the file. The toggle changes which slice of the inlined `DATA` constant is rendered.

5. **Add the static-versus-dynamic breakdown chart.** Add a new section to the report titled "Unanswered: static vs dynamic" that shows the breakdown grouped by top-level category. Use ECharts (matching the rest of the report). Add the per-window metric cards for unanswered-static and unanswered-dynamic counts. The chart should make it obvious where the highest pain points sit so Srinivas can use it to prioritize.

6. **Generate the report and send the link to Colin.** Regenerate `report_weekly.html`, verify the new section renders against real data, verify the six-month toggle changes every chart, and send Colin the link so he can forward to Srinivas with the deliverable framing.

## Testing

**Set up:**
- Branch `skills/webex` checked out locally
- Existing `output/issues.db` accessible (3.3 MB, 1,756 issues)
- Existing `output/report_weekly.html` as the visual baseline

**Functional flow:**
1. Apply the schema migration; verify `answer_type` exists with the expected values
2. Run the backfill agent on a sample of 50 unanswered issues; spot-check ten of them by hand to confirm Srinivas's definition is being applied correctly (a "how do I commit" question is static; a "where is my PR stuck" question is dynamic)
3. Generate the report and load it in a browser
4. Toggle the six-month switch; verify every chart updates (trend, heatmap, treemap, monthly composition, calendar, bubble, bar race, the new static-vs-dynamic chart)
5. Click into the new "Unanswered: static vs dynamic" chart; verify the per-category breakdown is consistent with the underlying database query

**Edge cases:**
- A question that is partly static and partly dynamic ("what is the rule for X, and is my PR Y meeting it?"). Decide your tie-breaker rule and document it in the prompt.
- A question whose resolution status is `ambiguous`. Should it be classified, or left out of the unanswered chart?
- The `NULL` resolution status rows (653 of them). Decide whether they get backfilled or skipped.
- The six-month window for an empty period (no messages in the last six months for a small category).

**Reproducibility:**
- The backfill prompt and run output live under `nxos-issue-categorizer/backfill/` so the classification can be re-run if Srinivas asks for adjustments later.

## Acceptance Criteria

**Functionality:**
- [ ] `issues` table has the `answer_type` column with values from {`static`, `dynamic`, NULL}
- [ ] All unanswered issues have `answer_type` populated (or are explicitly excluded with documented reasoning)
- [ ] Report has a six-month versus all-time toggle that affects every chart
- [ ] Report has a new "Unanswered: static vs dynamic" chart grouped by top-level category
- [ ] Report has metric cards for unanswered-static count and unanswered-dynamic count in the active window
- [ ] Default view is six-month

**Code quality:**
- [ ] Schema change is in `init_db.py` and validated by `verify_batch.py`
- [ ] Agent prompt in `SKILL.md` uses Srinivas's exact static-versus-dynamic framing
- [ ] Backfill prompt and output are reproducible from artifacts in `nxos-issue-categorizer/backfill/`
- [ ] No hard-coded category-to-classification mappings; the agent classifies per issue
- [ ] Commits land on `skills/webex` daily as the work progresses

**Visibility:**
- [ ] All work is on `skills/webex` and visible to Cisco
- [ ] The engagement chat has the link to the latest commit and the report file path per the 24-hour update cadence
- [ ] Colin has the report link to forward to Srinivas

## Notes

### Working folder and branch

All code lands on https://wwwin-github.cisco.com/DeepSight/ci-cd/tree/skills/webex under `nxos-issue-categorizer/`. The skill is already on this branch; this issue extends it rather than starting fresh. Commit and push early so progress is visible; push daily as the work progresses.

### Why this issue is the next logical step

Srinivas asked for this analysis during the Monday sync as input to his pain-point prioritization. The static-versus-dynamic split tells the team which categories are static-dominated (those answers belong on the wiki and feed the static answer path) versus dynamic-dominated (those need the CAT MCP plus Justin's MongoDB integration to answer at all). Without this analysis, downstream wiki-extraction work and dynamic-path work are uninformed. With it, every subsequent issue has a clear ordering by Srinivas's own pain-point ranking.

### Using Codex effectively

The prompt below is a starting point. You own your Codex sessions; expand, contract, or rewrite this prompt as you learn the actual shape of the data and refine the classification logic. Move with velocity; Codex is the accelerator on the schema work, the agent prompt updates, the backfill run, and the ECharts work. Treat this as guidance only.

```
Start here:

I am extending an existing Claude Code skill called nxos-issue-categorizer
on the skills/webex branch of the DeepSight CI/CD repo. The skill ingests
Webex chat messages, categorizes them via an LLM agent, and produces an
HTML dashboard from a SQLite database.

Reference the skill at:
- SKILL.md (the agent prompt is in the per-thread analysis section)
- scripts/init_db.py (schema)
- scripts/merge_issues.py (parsing batch outputs into SQLite)
- scripts/verify_batch.py (validation)
- scripts/export_html.py (generates report_weekly.html with ECharts)
- output/issues.db (1,756 categorized issues, 78 categories, 3 years
  of data; 436 explicit unanswered, 653 NULL, 481 resolved, 186
  ambiguous)
- output/report_weekly.html (575 KB single-file dashboard with data
  inlined as a JS constant)

I need to add two things:

1. A new dimension on each issue: answer_type in {static, dynamic}.
   Definition (from the Cisco AI Lead):
     - static: the answer does not require any database lookup, and
       is well-known (example: "how do I commit my code")
     - dynamic: the answer requires looking up the state of a specific
       PR or build at the moment of asking (example: "where is my PR
       stuck")

2. A six-month time window toggle on the report. Default to six
   months. Toggle to all-time. Every chart respects the active window.

Help me:
- Plan the minimal schema change for answer_type (column + index)
- Update the agent prompt in SKILL.md to use the definition above
  exactly, including Srinivas's exact phrasing
- Update verify_batch.py and merge_issues.py to handle the new field
- Write a backfill prompt that reads existing issues from issues.db
  and assigns answer_type without re-categorizing
- Add a date-window filter at the data layer of export_html.py and a
  UI toggle that swaps which slice of the inlined data renders
- Add a new "Unanswered: static vs dynamic" ECharts chart grouped by
  top-level category, plus the per-window metric cards

Use the skills/webex branch as the working location. Commit and push
early. Push daily. Capture the backfill prompt and output under
nxos-issue-categorizer/backfill/ for reproducibility.
```

Refine that prompt as you go. Switch to a sharper version once the schema is in and you are iterating on the agent classification.

### Coordination

- **Colin (BayOne):** owns sending the report link to Srinivas. Send him the link as soon as the chart renders against backfilled data.
- **Anupma (Cisco):** if any classification edge cases require domain interpretation (Cisco-specific tooling questions where the static-versus-dynamic call is not obvious), her PR-Checks-tab knowledge from the Monday sync makes her a useful Cisco-side check-in.
- **24-hour update cadence:** push commits daily and update the engagement chat with progress.

### Common pitfalls

- Re-categorizing existing issues from scratch instead of layering the new dimension on top. The existing categories and resolution status are correct; only `answer_type` is being added.
- Hard-coding category-to-classification mappings ("anything in the Workflow category is static"). The agent should classify per issue; some Workflow questions need a DB lookup, some do not.
- Filtering at the chart level instead of the data layer. The toggle changes which slice of `DATA` renders; doing it per chart leads to drift between charts.
- Letting the backfill run skip the high-volume "NULL" resolution status rows without thinking about whether they should be classified. Decide explicitly and document the choice.
- Treating "six months" as a hard-coded constant. Make the window value parameterized so the toggle UI can drive it.

### What this issue does NOT cover

- Wiring static answers from the wiki into the bot's static answer path. Separate workstream.
- Dynamic answer path data layer (CAT MCP versus MongoDB). Separate issue.
- Bot deployment, compliance, registration. Separate workstream.

This issue is a pure analysis-and-visualization deliverable for Srinivas. It informs every wiring issue that comes after it.
