# Kickoff: Screenshot Export Pipeline

## Copy-paste the prompt below into a new Claude session

---

You are building a tooling pipeline to export HTML slides as high-resolution PNGs for PowerPoint assembly. This is a scripting task, not a design task.

**Start by reading this handoff document thoroughly:**
`/home/cmoore/programming/cisco_projects/cicd/claude/2026-03-23_mcgrath_slides/handoffs/handoff_18_screenshot_export.md`

Your job:
1. Copy all final HTML slides from `slides_output/` to `slides_export/`
2. Strip presentation chrome (header, footer, border-radius, background) from each copy
3. Write a Playwright screenshot script at 3840x2400 (4K, 16:10)
4. Test on 2-3 diverse slides first and show the user
5. Run full batch once approved

Use simple Python scripts (`scratchpad.py` style). Work on COPIES only -- never modify originals in `slides_output/`.

Output to `slides_export/` and `slides_export/pngs/`. Write results handoff at `handoffs/handoff_18_results.md`.
