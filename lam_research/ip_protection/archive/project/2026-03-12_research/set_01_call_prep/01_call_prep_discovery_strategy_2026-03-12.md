# 01 - Call Prep: Discovery Strategy

**Source:** `source/lam_call_prep (1).txt`
**Source Date:** 2026-03-12 (prepared immediately before discovery call)
**Document Set:** 01 (Call Prep)

---

## Call Format

Per Bradley Estes' email, the call was structured as:
1. Lam presents their problem statement
2. Q&A session
3. BayOne goes away and comes back with a response/approach

This is a discovery call. The explicit strategy was: let them present, listen, ask smart questions that draw out information, demonstrate understanding of their world without making assumptions.

## Question Bank by Category

### Understanding the Failure
Priority: Start here. Don't assume what "failing" means.

- Walk through a specific example where guardrails didn't catch something expected
- When they say "failing" - false negatives (sensitive content getting through), false positives (blocking legitimate use), or both?
- How are they testing? Manual red teaming, automated adversarial testing, production monitoring?
- What does the 20% error rate specifically measure? How was that threshold determined?
- Are failures at the prompt level, response level, file uploads, or all?

### Understanding the Tool Stack
Priority: Validate assumptions about Sentinel vs. Purview confusion.

- Which specific tools are seeing failures? AI Foundry? Copilot? Something else?
- How are they doing content detection today? Purview DLP, Azure AI Content Safety, or something else?
- What custom Sensitive Information Types have been configured, if any?
- Detection approach: pattern-based (regex, keywords) or semantic (understanding context)?

### Understanding Their IP Taxonomy
Priority: Critical. Out-of-the-box patterns don't cover semiconductor IP.

- What categories of content are most concerning? Customer names, production volumes, process parameters, technical drawings - priority order?
- Examples of what "sensitive" looks like in their context - a sentence that should be blocked, a document type that shouldn't be uploaded
- Are customer names always sensitive, or only in certain contexts? (e.g., "TSMC" in public earnings discussion vs. "TSMC yield rate for Q4")

### Understanding Shadow AI
Priority: Industry data suggests this is likely bigger than admitted.

- Visibility into AI usage outside approved tools?
- Awareness of personal ChatGPT/Claude accounts, consumer AI tools?
- Browser extensions, meeting recording tools (Otter.ai), AI features in other SaaS?
- Developers using GitHub Copilot or unapproved AI APIs?

### Understanding Governance Structure
Priority: Determines who buys in and what's realistic.

- Who owns AI governance? Formal AI CoE or governance committee?
- Stakeholders: Legal, IT, CISO, business units?
- Approval process for new AI tools or use cases?
- Formal taxonomy or classification system for sensitive data?

### Understanding What's Been Tried
Priority: Don't duplicate failed work or propose ruled-out solutions.

- What's already configured in Purview, AI Foundry, or elsewhere?
- What worked? What didn't?
- Solutions evaluated and not pursued? Why not?

### Understanding the Vector
Priority: Different leakage vectors need different solutions.

- Primary concern: data going into AI via prompts/uploads, AI surfacing sensitive data from knowledge bases, or data leaving via AI-generated outputs?
- Is email exfiltration in scope, or specifically AI tools?

### Understanding Timeline & Success
Priority: Determines engagement scope.

- Timeline pressure? Blocking a specific initiative?
- Success criteria at 6 months? 12 months?
- Re-enable AI org-wide, or specific teams first?
- Preferred response format: written proposal, call, presentation?

### Closing
- What else should we understand?
- Who else should we talk to?
- What would you need to see to feel confident moving forward?

## Signals to Listen For

### Indicators: Configuration/Governance Gap (Consulting Opportunity)
- Confusion about which tool does what (Sentinel vs. Purview vs. Content Safety)
- No custom Sensitive Information Types configured
- No formal AI governance structure
- Shadow AI acknowledged but unquantified
- "We're not sure what Microsoft's tools can actually do"

### Indicators: Genuine Custom Build Requirement
- Custom SITs already configured and tuned, still insufficient
- Detection needs are semantic/contextual, not pattern-based
- Real-time intervention required, not just logging/alerting
- Specific failure modes that can't be addressed with configuration
