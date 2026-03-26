# Meeting 4 - Commitments Made

## Overview

All commitments made during Meeting 4, organized by party, with owners, timelines, and tracking status.

---

## Sephora Commitments

### Commitment 1: Provide Cognos Report XML

| Field | Value |
|-------|-------|
| **What** | Provide one Cognos report XML definition from Finance track |
| **Owner** | Gariashi, coordinating with Vlad |
| **Timeline** | Not specified |
| **Status** | Pending |
| **Context** | "We need to work with Vlad to get that. We can pick one report from finance." |

**Notes:**
- Full XML definition preferred (not just SQL query)
- Report should be representative of common patterns
- Ideally a Framework Model report for simpler demo scope

---

### Commitment 2: Provide Databricks Schema Information

| Field | Value |
|-------|-------|
| **What** | Provide target Databricks catalog/schema information for mapping |
| **Owner** | Maher/Sergei (implied) |
| **Timeline** | Not specified |
| **Status** | Pending |
| **Context** | "We feed it the actual information about the catalog and schema. Assuming that we have the table that the SQL runs on, then it should work." |

**Notes:**
- Needed so agent can do the remapping without direct access
- Should include table names, column definitions, data types
- Does not require actual data, just structure

---

### Commitment 3: Consider DataStage Job for Demo (Optional)

| Field | Value |
|-------|-------|
| **What** | Potentially provide a simple DataStage job definition |
| **Owner** | Maher/Sergei |
| **Timeline** | Not specified |
| **Status** | Tentative |
| **Context** | Maher: "One of the DataStage... we probably can have a simple DataStage job that we can share." |

**Notes:**
- This is optional/additional scope
- Would demonstrate DataStage conversion capability
- Should be a simpler job to start

---

### Commitment 4: Internal Discussion on Demo Scope

| Field | Value |
|-------|-------|
| **What** | Regroup internally to determine what else would be helpful for demo |
| **Owner** | Andrew/Gariashi |
| **Timeline** | After this call |
| **Status** | Pending |
| **Context** | Andrew: "Maybe let's talk about it. As a team, we want to regroup and see what else would be helpful for us. And then we can get back to you." |

**Notes:**
- May result in additional requirements or scope changes
- Important to follow up on this

---

## BayOne Commitments

### Commitment 1: Build Demo with Provided Materials

| Field | Value |
|-------|-------|
| **What** | Build demo showing Cognos report lift-and-shift conversion |
| **Owner** | Colin Moore |
| **Timeline** | After receiving materials |
| **Status** | Pending (waiting on Sephora deliverables) |
| **Context** | "If we can get one of the Cognos reports, what we will be able to do is we can take that, build the MCP for it, make sure that we can A, connect to it, B, dissect it, and be able to get into it." |

**Demo scope agreed:**
1. Build MCP server for Cognos
2. Parse/dissect the report definition
3. Demonstrate remapping to Databricks structure
4. Do NOT require direct system access
5. Validation happens separately by Sephora

---

### Commitment 2: Help with Security Conversations (If Needed)

| Field | Value |
|-------|-------|
| **What** | Assist with IT/security team conversations when needed |
| **Owner** | Colin Moore |
| **Timeline** | As needed |
| **Status** | Standing offer |
| **Context** | "We do this all the time, so we're used to talking to IT and security teams to kind of tell them, no, we're not crazy. No, we're not going to hurt anything." |

---

### Commitment 3: Schedule Demo Session

| Field | Value |
|-------|-------|
| **What** | Set up time for demo after receiving materials |
| **Owner** | Neha |
| **Timeline** | After materials received |
| **Status** | Pending |
| **Context** | "Just waiting on those reports from you, and then we set up a time for that first level demo to showcase capabilities." |

---

## Commitments from Previous Meetings Still Outstanding

| Commitment | Original Meeting | Owner | Status |
|------------|------------------|-------|--------|
| Priority ranking of challenges | Meeting 3 | Sephora | Not mentioned (may be superseded) |
| Three-tier proposal | Meeting 2 | BayOne | Not discussed (may be superseded by demo-first approach) |

---

## Commitment Dependencies

```
Sephora: Provide Cognos XML + Databricks schema
    ↓
BayOne: Build MCP + Demo
    ↓
Both: Schedule demo session
    ↓
Demo delivery
    ↓
(Future) Discuss next steps / larger engagement
```

---

## Risk Factors

| Risk | Mitigation |
|------|------------|
| Sephora delays providing materials | Follow up proactively after 1 week |
| Report provided is too simple/complex | Request 2-3 options if possible |
| Databricks schema info insufficient | Clarify exact requirements upfront |
| Security blocks demo deployment later | Demo designed to not require direct access |
| Stakeholder availability for demo | Coordinate calendars early |

---

## Tracking Actions

### For BayOne (Immediate)

1. [ ] Send follow-up email summarizing commitments
2. [ ] Clarify exact Databricks schema info needed
3. [ ] Begin MCP server scaffolding for Cognos (can start without specific report)
4. [ ] Prepare for potential DataStage scope addition

### For BayOne (After Materials Received)

1. [ ] Review Cognos XML structure
2. [ ] Build report parsing capability
3. [ ] Create mapping logic to provided Databricks schema
4. [ ] Develop demo walkthrough script
5. [ ] Schedule demo session

### For Sephora

1. [ ] Select Finance report for demo
2. [ ] Export Cognos XML definition
3. [ ] Document relevant Databricks catalog/schema
4. [ ] (Optional) Select simple DataStage job
5. [ ] Internal discussion on additional demo needs
