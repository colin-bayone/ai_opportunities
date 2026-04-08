# 01 - Call Prep: Discovery Strategy

**Source:** /lam_research/ip_protection/source/lam_call_prep_2026-03-12.txt
**Source Date:** 2026-03-12 (Pre-discovery call preparation document)
**Document Set:** 01 (Call Prep)
**Pass:** Discovery strategy and question bank

---

## Overall Approach

Listen first. Let Lam present. Ask smart questions that draw out information. Demonstrate understanding of their world without making assumptions. Do not present hypotheses as fact. Validate through questions.

## Question Bank by Category

### 1. Understanding the Failure (Start Here)

The prep explicitly prioritizes this category first. Do not assume what "failing" means.

- Walk through a specific example where guardrails did not catch something expected
- When you say "failing," false negatives (sensitive content getting through), false positives (blocking legitimate use), or both?
- How are you testing? Manual red teaming, automated adversarial testing, production monitoring?
- What does the 20% error rate specifically measure? How was the threshold determined?
- Are failures at the prompt level (user input), response level (AI output), file uploads, or all?

### 2. Understanding the Tool Stack

Validate assumptions about their architecture rather than stating them.

- Which specific tools show failures? AI Foundry? Copilot? Something else?
- How is content detection done today? Purview DLP, Azure AI Content Safety, or something else?
- What custom Sensitive Information Types have been configured, if any?
- Detection method: patterns (regex, keywords) or semantics (understanding context)?

### 3. Understanding Their IP Taxonomy

Critical because out-of-the-box patterns do not cover semiconductor IP.

- What categories of content are most concerning? Customer names, production volumes, process parameters, technical drawings. All equal, or priority order?
- Examples of what "sensitive" looks like in their context. A sentence that should be blocked, a document type that should not be uploaded.
- Are customer names always sensitive, or only in certain contexts? ("TSMC" in a public earnings discussion vs. "TSMC yield rate for Q4")

### 4. Understanding Shadow AI

Industry data suggests this is likely a bigger factor than admitted.

- Visibility into AI usage outside approved tools?
- Personal ChatGPT accounts, personal Claude accounts, consumer AI tools?
- Browser extensions, meeting recording tools (Otter.ai), AI features in other SaaS?
- Developer concern: GitHub Copilot, unapproved AI APIs?

### 5. Understanding Governance Structure

Determines who needs to buy in and what is realistic.

- Who owns AI governance at Lam? Formal AI CoE or governance committee?
- Stakeholders: Legal, IT, CISO, business units?
- Approval process for new AI tools or use cases?
- Formal taxonomy or classification system for sensitive data?

### 6. Understanding What Has Been Tried

Do not duplicate work or propose something already ruled out.

- What has been configured in Purview, AI Foundry, or elsewhere?
- What worked? What did not?
- Solutions evaluated and decided against? Why?

### 7. Understanding the Vector

Different leakage vectors require different solutions.

- Primary concern: data going INTO AI tools (prompts/uploads), AI surfacing sensitive data from knowledge bases (responses), data leaving via AI-generated outputs?
- Is email exfiltration in scope, or specifically AI tools?

### 8. Understanding Timeline and Success

Determines engagement scope.

- Timeline pressure? Blocking a specific initiative?
- Success criteria at 6 months? 12 months?
- Re-enable AI org-wide or specific teams first?
- Best format for response: written proposal, another call, presentation?

## Closing Questions

- What else should we understand before coming back with an approach?
- Who else should we be talking to?
- What would you need to see from us to feel confident moving forward?

## Signals to Listen For

### Indicators of a Configuration/Governance Gap (Consulting Opportunity)
- Confusion about which tool does what (Sentinel vs. Purview vs. Content Safety)
- No custom Sensitive Information Types configured
- No formal AI governance structure
- Shadow AI usage acknowledged but unquantified
- "We're not sure what Microsoft's tools can actually do"

### Indicators of a Genuine Custom Build Requirement
- Custom SITs already configured and tuned, still insufficient
- Detection needs are semantic/contextual, not pattern-based
- Real-time intervention required, not just logging/alerting
- Specific failure modes that cannot be addressed with configuration
