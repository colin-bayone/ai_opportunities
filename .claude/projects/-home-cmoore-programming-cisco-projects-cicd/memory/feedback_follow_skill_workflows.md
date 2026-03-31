---
name: Follow skill workflows exactly
description: When a skill like skill-forge defines a mandatory workflow, follow it step by step - never skip to generating output
type: feedback
---

When a skill defines a mandatory workflow (like skill-forge's Step 0 → Step 1 → Step 2 → Step 3 sequence), follow it EXACTLY. Do not skip steps even if you think you have enough information to jump ahead.

**Why:** In the singularity skill build session (2026-03-28), skill-forge was invoked but its entire workflow was skipped. Jumped straight to generating files. The resulting skill had 4 critical gaps, 11 important gaps, and 11 minor gaps that the questionnaire and planning steps would have caught. User explicitly said this wasted their time.

**How to apply:** When a skill is loaded that has numbered phases, gates, or mandatory steps, follow them in order. Even if the user has provided comprehensive specs, the workflow exists to ensure nothing is missed. The planning step (Step 2) is especially important - it forces you to think through what's needed before generating anything.
