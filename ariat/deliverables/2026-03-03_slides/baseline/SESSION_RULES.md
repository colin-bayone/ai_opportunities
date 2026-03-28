# Session Rules - DO NOT VIOLATE

## Workflow
1. Make changes to a slide
2. Tell user what I did (brief)
3. WAIT for user feedback/approval
4. Only move to next slide after explicit "yes" or approval

## Screenshots
- Do NOT take screenshots for prototypes
- User will view HTML files directly in browser
- Only use screenshots when explicitly asked

## Prototypes
- Stay focused on the ask — no extra "comparison matrices" or additions
- Give REAL variety, not lazy variations of the same idea
- Think creatively, not just parameter tweaks

## Redundancy
- Watch for redundant labels (e.g., "Foundation" above "Technology Foundation")
- User is highly sensitive to this — called it out in original requirements

## Communication
- If user didn't ask for it, don't do it
- Don't suggest options that contradict the entire point (e.g., "no differentiation" when the whole task is to add differentiation)
- Remember context from earlier in the conversation

## When Corrected
- If corrected again, re-read this entire document before proceeding

---

## Mistakes Made This Session

1. **Took screenshots for prototypes after being told not to** — User said "no screenshots for prototypes" and I kept doing it anyway

2. **Added unwanted "Quick Comparison" section** — User never asked for it, wasted tokens and cluttered the prototype

3. **Lazy prototyping** — First prototype had 4 variations that were barely different from each other, not genuinely creative options

4. **Suggested "no differentiation" as an option** — The ENTIRE TASK was to add differentiation. This was stupid.

5. **Created wrong file when asked for specific file** — User said "show me prototype_card_styles.html with option F applied" and I created a new file (10_technology_foundation_v3.html) instead of editing the file they asked for

6. **Forgot the core problem** — The whole point was card differentiation with different colors. I kept forgetting this and producing undifferentiated designs.

7. **Redundant labeling** — Put "Foundation" above "Technology Foundation" after being told to watch for redundancy

8. **Not listening to explicit instructions** — Multiple instances of doing something other than exactly what was asked

---

## Reusable Patterns

### Differentiated Card Layout (Slide 10 style)
Use for grid layouts where cards need visual distinction. Each card gets:
- Colored icon (matching the card's accent color)
- Colored bullet points (matching the card's accent color)
- 3px bottom border (matching the card's accent color)

Color progression (dark to light):
1. #5B21B6
2. #6D28D9
3. #7C3AED
4. #8B5CF6
5. #A855F7
6. #C084FC

CSS pattern:
```css
.card:nth-child(1) { border-bottom: 3px solid #5B21B6; }
.card:nth-child(1) h3 i { color: #5B21B6; }
.card:nth-child(1) .list li::before { background: #5B21B6; }
```
