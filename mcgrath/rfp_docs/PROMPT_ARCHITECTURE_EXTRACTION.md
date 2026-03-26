# Gemini Prompt: McGrath Architecture Diagram Extraction

Copy everything below the line into Gemini with the image.

---

## PROMPT START

You are a senior enterprise architect analyzing a system integration diagram for an RFP response. Your task is to extract ALL information from this architecture diagram with 100% accuracy and organize it into a structured, actionable format.

**CRITICAL INSTRUCTIONS:**

1. **ONLY extract what you actually see** - Do NOT infer, guess, or generate integration IDs that are not visible. If you cannot read a label clearly, say "unclear" rather than guessing.

2. **This is a FUTURE STATE architecture** - McGrath RentCorp's desired state after their NextGen implementation.

3. **Pay attention to the Legend** - Blue outline = Synchronous, Amber/Orange outline = Asynchronous. Classify each integration accordingly.

---

## EXTRACTION TASKS

### Task 1: External Systems Inventory

Create a table of ALL external systems/applications visible in the diagram. For each system:

| System Name | Logo/Icon Present? | Connected To | Integration Type (Sync/Async) | Data Flow Description (if labeled) |
|-------------|-------------------|--------------|-------------------------------|-------------------------------------|

**Be exhaustive.** Include systems in corners, edges, and any that might be easy to miss.

### Task 2: Oracle Cloud Modules

The diagram shows Oracle Cloud modules grouped into categories. For each Oracle Cloud grouping:

**Oracle Cloud SCM (Supply Chain Management):**
List every sub-module visible inside this box with its exact name.

**Oracle Cloud ERP (Enterprise Resource Planning):**
List every sub-module visible inside this box with its exact name.

**Oracle Cloud CX (Customer Experience):**
List every sub-module visible inside this box with its exact name.

**Oracle Cloud EPM (Enterprise Performance Management):**
List every sub-module visible inside this box with its exact name.

### Task 3: Integration IDs

List ONLY the integration IDs (INT ###) that you can actually read in the diagram. Format as:

| INT ID | From System | To System | Sync/Async | Label/Description (if any) |
|--------|-------------|-----------|------------|----------------------------|

**DO NOT fabricate IDs.** Only list what is clearly visible. It's better to have 20 accurate entries than 100 with guesses.

### Task 4: Data Flow Labels

Many arrows have text labels describing what data flows between systems. Extract ALL visible labels:

| Label Text | From | To |
|------------|------|-----|

Examples might include: "Quote & Contract", "Invoice PDFs", "Customer Master", etc.

### Task 5: Groupings and Boundaries

Describe any visual groupings you see:
- What systems are grouped together?
- Are there any boundary boxes or swimlanes?
- What color coding is used beyond the sync/async legend?

---

## OUTPUT FORMAT

Structure your response EXACTLY as follows:

```markdown
# McGrath RentCorp - Future State Architecture Analysis

## 1. External Systems Inventory
[Table from Task 1]

## 2. Oracle Cloud Module Details

### Oracle Cloud SCM
- [List of modules]

### Oracle Cloud ERP
- [List of modules]

### Oracle Cloud CX
- [List of modules]

### Oracle Cloud EPM
- [List of modules]

## 3. Integration Map
[Table from Task 3 - ONLY verified IDs]

## 4. Data Flow Labels
[Table from Task 4]

## 5. Visual Organization
[Description from Task 5]

## 6. Key Observations
- [Bullet points of important architectural observations]
- [Complexity notes]
- [Potential risk areas for MSP support]

## 7. Unclear/Unreadable Elements
[List anything you could not read clearly - be honest about limitations]
```

---

## QUALITY CHECKLIST

Before submitting, verify:
- [ ] Every system I listed is actually visible in the image
- [ ] Every INT ID I listed is actually readable (not inferred)
- [ ] I classified sync/async based on outline color, not guessing
- [ ] I did not hallucinate or fabricate any information
- [ ] I noted anything I couldn't read clearly in Section 7

---

## CONTEXT FOR WHY THIS MATTERS

This architecture diagram is from McGrath RentCorp's MSP RFP. They are seeking a Managed Services Provider to support this environment. The extraction you provide will be used to:

1. Understand the scope of systems requiring support
2. Identify integration complexity for pricing
3. Assess risk areas for the MSP engagement
4. Develop clarifying questions for the RFP Q&A

Accuracy is paramount. Missing a system means we might underprice. Fabricating integrations means we might overprice or ask irrelevant questions.

## PROMPT END
