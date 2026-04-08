# Handoff: Malika Email Response

This document provides context from a parallel Claude session that worked on the Sephora scoping documents. Use this to correct the email draft.

---

## What's Being Sent

Both scoping documents are being attached to the email:
- Track A: Cognos MCP Demo (HTML)
- Track B: ETL/DataStage Demo (HTML)

The email should reflect that both are attached, not that one will be sent later after they choose.

---

## Corrections Needed

### 1. MCP Cannot Be Demonstrated

The email currently implies we can demonstrate MCP connectivity. We cannot.

**The reality:**
- We CAN build the MCP connector
- We CANNOT demonstrate or test it without access to their Cognos environment
- Cognos is a proprietary IBM product with no freely available Docker image or trial server
- For the demo, we work with exported Cognos report XML
- The MCP connector shows the architecture and would replace manual exports in production
- Live connectivity requires environment access from Sephora

**How to frame it:**
Put the ball in their court. If they want to see MCP working, they need to provide environment access. Based on the call discussion, this may not be feasible given their security constraints.

### 2. Track B Output Format Discrepancy

There is a conflict between what was said on the call and what Malika wrote:

- **Sergey (call):** YAML configuration files for the existing AggregationApplication framework, not new Scala code
- **Malika (email):** "Spark SQL / Scala" output

The email should ask them to clarify which output format is correct. This is important because they are fundamentally different deliverables.

### 3. Track B Output Language

The current draft says "generate Databricks-compatible output matching your YAML config and Scala framework" which is vague.

Based on Sergey's guidance on the call, the output should be YAML configs that work with their existing framework. They are not asking us to write new Scala code. Their developers write YAML configs and the framework handles the rest.

---

## Reference Files

If you need more context, these files exist in the session:

- `scoping/track_a_cognos_mcp_demo.md` - Track A details
- `scoping/track_b_etl_datastage_demo.md` - Track B details
- `scoping/track_a_cognos_mcp_demo.html` - Track A formatted doc (being attached)
- `scoping/track_b_etl_datastage_demo.html` - Track B formatted doc (being attached)
- `research/06_malika_email_breakdown.md` - Analysis of what Malika asked for
- `research/07_demo_feasibility_analysis.md` - What we have vs what's missing

---

## Questions

If you need clarification on anything from this session, ask. The parallel session has full context on:
- Meeting 4 transcript details
- Cognos Docker research (why we cannot spin up our own)
- The YAML vs Scala discrepancy
- What materials Sephora provided vs what's still missing
