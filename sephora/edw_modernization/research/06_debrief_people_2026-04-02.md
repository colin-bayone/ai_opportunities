# 06 - Debrief: People

**Source:** /sephora/edw_modernization/source/saurav_colin_demo_prep_2026-04-02.txt
**Source Date:** 2026-04-02 (Demo Prep Call)
**Document Set:** 06 (Saurav/Colin Demo Prep)
**Pass:** People identification

---

## On the Call

### Colin Moore (BayOne)
- **Tone:** Focused, energized, taking detailed notes while Saurav talked. Running the demo on his own machine to validate. Already thinking about demo flow and talking points. Practical about quota issues (requested 4-5X increase on Azure Foundry for Opus and Sonnet). Generous with praise ("No one will have any question that cannot be answered from this").
- **Key actions:** Pulled latest code, running poetry install, testing the full pipeline locally. Requested Azure quota increases. Planning to record the demo meeting. Offered to let Saurav skip if 3:30 AM is too late.

### Saurav Kumar Mishra (BayOne)
- **Tone:** Thorough, technically precise. Walked Colin through every single stage of the pipeline with detailed explanations of what each gate checks, what each parser does, how the retry loop works, and what the auto-fix feature does. Flagged known issues proactively (reject-and-retry DAG animation, zip download, rendering bug on advisory text, pipeline_runs table).
- **Key contributions:** Added execution log with live spinners and timers, AI review button, auto-fix feature ("like Claude Code for your pipeline"), highlight.js for code preview, knowledge base learning from approved patterns, multiple run history with clickable entries.
- **Availability:** May join the 3:30 AM demo call but not guaranteed. Will be available for at least 2.5 more hours after this call. Working on the pipeline_runs table creation fix.

---

## Sephora People Referenced

### Mani
- Colin met with Mani in person last week at Sephora HQ
- Told Colin that vendor selection must happen by end of month (April)
- Suggested BayOne leverage existing contractors/support people at Sephora for Cognos environment access

### "Yogesh"
- Colin has a meeting with Yogesh immediately after this call (unrelated to Sephora, likely Cisco)

---

## Key Dynamic

This is the final prep call. Both are confident. The pipeline works. The only concerns are performance (throttling from Azure quotas) and minor UI polish. Colin is transitioning from "reviewing Saurav's work" to "rehearsing how to present it."
