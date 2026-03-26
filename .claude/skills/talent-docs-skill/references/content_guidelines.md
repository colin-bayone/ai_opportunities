# Content Writing Guidelines

## Target Audience

### Who We're Writing For

**Primary audience:**
- Recruiters (staffing agency and corporate)
- Hiring managers
- Account managers
- Sourcers
- HR coordinators

**What they have in common:**
- Non-technical background
- Busy, need quick answers
- Goal-oriented (fill positions, find candidates)
- May use TalentAI on mobile/tablet

**What they DON'T know:**
- Programming concepts
- Database terminology
- Technical architecture
- Developer jargon

### Who We're NOT Writing For

- Developers (they have code, CLAUDE.md, and inline docs)
- System administrators
- Technical support staff

## Voice & Tone

### Personality

Write like a **knowledgeable colleague** who:
- Genuinely wants to help
- Explains things clearly without condescension
- Uses everyday language
- Gets to the point

### Tone Guidelines

**DO:**
- Be friendly and approachable
- Use "you" to speak directly to the reader
- Be encouraging ("You can..." instead of "Users must...")
- Acknowledge that learning new software takes time

**DON'T:**
- Be robotic or formal
- Use passive voice ("The button should be clicked")
- Be condescending ("Simply click..." implies it's easy)
- Use technical jargon without explanation

### Examples

**Good:**
> "Click **Search** to find candidates matching your criteria. Results appear instantly as you type."

**Bad:**
> "The SearchView component processes GET requests and returns a filtered QuerySet based on form parameters."

**Good:**
> "If you're not seeing results, try removing some filters to broaden your search."

**Bad:**
> "Empty result sets may indicate overly restrictive filter parameters in the request payload."

## Article Structure

### Standard Article Template

```markdown
# [Task-Oriented Title]

[1-2 sentence overview: what this helps you do]

## [Section 1: Core Concept or Overview]

[Explanation with context]

## How to [Do the Thing]

1. [Step with **bolded UI element**]
2. [Next step]
3. [Verification step]

## Pro Tips

- **[Tip name]** - [Brief explanation]
- **[Another tip]** - [Brief explanation]

## Common Questions

**Q: [Question users ask]**
A: [Clear answer]

## Related Articles

- [Link to related article]
- [Link to another]
```

### Title Guidelines

**Good titles (task-oriented):**
- "Finding Candidates with Search"
- "Creating Your First Job Posting"
- "Setting Up Email Templates"
- "Understanding Your Analytics Dashboard"

**Bad titles (feature-oriented):**
- "The Search Feature"
- "Job Module Overview"
- "Email System"
- "Analytics"

### Section Guidelines

**Overview sections:**
- Maximum 2-3 sentences
- Answer "what is this?" and "why would I use it?"
- No technical details

**How-to sections:**
- Numbered steps (not bullets)
- One action per step
- Bold all UI elements: **Save**, **Cancel**, **Search**
- Include what they should see after each step

**Pro Tips sections:**
- 2-4 tips maximum
- Focus on time-savers and power-user features
- Each tip should provide clear value

## Formatting Standards

### UI Elements

Bold all interface elements:
- Buttons: **Save**, **Cancel**, **Submit**
- Menu items: **Candidates > Search**
- Field names: **First Name**, **Email**
- Tab names: **Details**, **Activity**, **Notes**

### Keyboard Shortcuts

Use code formatting:
- `Ctrl+K` - Open search
- `Ctrl+S` - Save
- `Esc` - Close modal

### Code/Technical Values

Use code formatting for:
- Keyboard shortcuts: `Ctrl+K`
- Specific values: `Active`, `Pending`
- File names (rare in user docs)

### Links

Use descriptive link text:
- Good: "Learn more about [using filters](/docs/candidates/filters/)"
- Bad: "Click [here](/docs/candidates/filters/)"

### Lists

**Use numbered lists for:**
- Sequential steps
- Prioritized items
- Processes with order

**Use bullet lists for:**
- Features/options (no order)
- Tips and notes
- Related items

### Callouts

Use sparingly for important information:

```markdown
> **Tip:** Save time by using keyboard shortcuts. Press `Ctrl+K` to open search from anywhere.

> **Note:** Changes are saved automatically. You don't need to click Save.

> **Important:** This action cannot be undone. Make sure you want to proceed.
```

## Content Types

### Getting Started Articles

**Purpose:** Onboard new users quickly
**Length:** 300-500 words
**Focus:** Essential first steps, quick wins

**Structure:**
1. Welcome message
2. What they'll accomplish
3. Step-by-step first task
4. What to explore next

### Feature Guides

**Purpose:** Explain how to use a feature
**Length:** 500-800 words
**Focus:** Complete workflow, practical examples

**Structure:**
1. What this feature does
2. How to access it
3. Step-by-step usage
4. Tips for success
5. Common questions

### Best Practices Articles

**Purpose:** Help users succeed with strategies
**Length:** 600-1000 words
**Focus:** Real-world advice, scenarios

**Structure:**
1. Why this matters
2. Key principles
3. Specific techniques
4. Examples/scenarios
5. Common mistakes to avoid

### FAQ Articles

**Purpose:** Quick answers to common questions
**Length:** Variable (question-based)
**Focus:** Direct answers, links to details

**Structure:**
- Questions as headings
- Concise answers (2-4 sentences)
- Links to full guides where relevant

### Troubleshooting Articles

**Purpose:** Solve specific problems
**Length:** 300-600 words
**Focus:** Problem → Solution

**Structure:**
1. Problem description (what users see)
2. Why it happens
3. How to fix it
4. How to prevent it

## Writing Process

### Before Writing

1. **Explore the feature** - Use it yourself, understand the workflow
2. **Identify user goals** - What are they trying to accomplish?
3. **Note pain points** - What might confuse them?
4. **Check existing content** - Any help text in the UI?

### While Writing

1. **Start with the user's goal** - Not the feature
2. **Write the steps** - Then add context
3. **Use real examples** - Recruiting scenarios
4. **Read aloud** - Does it sound natural?

### After Writing

1. **Check for jargon** - Replace or explain
2. **Verify accuracy** - Test the steps
3. **Add links** - Cross-reference related articles
4. **Review length** - Cut unnecessary content

## Common Mistakes to Avoid

### Jargon Creep

**Technical terms to avoid:**
- "Query" → "search"
- "Filter parameters" → "filters"
- "Submit" → "save" or "send"
- "Navigate to" → "go to"
- "Select" → "click" or "choose"
- "Instance" → (just describe the thing)
- "Entity" → (use the actual name: candidate, job)

### Over-Explaining

**Too much:**
> "The search feature allows you to find candidates in the database by entering keywords and applying various filter criteria to narrow down the results based on your specific requirements."

**Just right:**
> "Search helps you find candidates. Enter keywords and use filters to narrow results."

### Missing Context

**Bad:**
> "Click the Export button."

**Good:**
> "From the search results page, click **Export** in the top right corner."

### Assuming Knowledge

**Bad:**
> "Use Boolean operators to refine your search."

**Good:**
> "Combine search terms with AND, OR, or NOT to refine results. For example, 'Python AND Django' finds candidates with both skills."

## Quality Checklist

Before publishing, verify:

- [ ] Title is task-oriented
- [ ] Overview explains what and why (2-3 sentences)
- [ ] Steps are numbered and specific
- [ ] UI elements are bolded
- [ ] No unexplained jargon
- [ ] Examples use recruiting scenarios
- [ ] Links to related articles work
- [ ] Reads naturally when spoken aloud
- [ ] Answers the user's likely questions
- [ ] Tested the steps myself
