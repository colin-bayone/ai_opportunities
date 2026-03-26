# 03 - Discussion: Open Information Needs

**Source:** Working discussion between Colin Moore and Claude, informed by all prior document sets
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Consolidated list of everything we still need from Lam, organized by who needs to get it

---

## Priority 1: What the Sales Team Must Get (No Technical Call Required)

These are things Pat/Pradeep and Anuj should be able to extract from Brad or Mikhail without needing Daniel.

### 1.1 The Critical Missing Piece: Name One Application
- Name one specific RAG-like application (the highest-impact one)
- Describe what it does
- What documents or data sources feed it
- **This gates everything.** Without this, we cannot scope a POC, estimate costs, or write a proposal.
- Colin asked this on the call and was told it was "too technical." It is not. It is a business question.

### 1.2 Data Volume Estimates
- How many documents are ingested per day/week?
- How many tickets are created per day?
- How many search queries per day?
- How many users across all systems?
- Needed for: architecture decisions, cost estimation, scale planning

### 1.3 Verify Brad's Authority
- Brad says he owns everything end-to-end. Does he actually have IT decision-making authority?
- How do IT and cybersecurity factor in? Do they have veto power?
- Who controls infrastructure decisions (cloud services, data residency)?
- We cannot afford to build a proposal assuming Brad can greenlight everything and then discover IT or security has to approve.

### 1.4 Budget and Timeline
- What budget range is Lam working with?
- The 1,000 man-hours comment suggests they have no cost framework -- we need to understand expectations
- Timeline for first pilot/POC?
- Who has final approval on spend?

### 1.5 Azure Environment
- What Azure services is Lam currently paying for?
- This determines whether Purview, AI Foundry, AI Search, etc. are immediately available or require new procurement

---

## Priority 2: What Requires the Daniel Technical Call

These require someone who can answer "what Azure services are you using" without saying "I don't know what that means."

### 2.1 Prior Technical Work (Full Autopsy)

| Question | Why We Need It |
|----------|---------------|
| What specific model architectures were tried? (Exact versions, configurations) | To understand if the approach was fundamentally wrong or just poorly executed |
| Who did the work? Internal team, Accenture, or both? | To assess the skill level that was applied |
| What was the golden standard / ground truth? | To understand if they even had a proper benchmark |
| What was the testing methodology? How were false positives calculated? | To determine if the 20% number is even measured correctly |
| What was the test dataset -- size, composition, labeling? | To understand if the data was sufficient |
| How is the current system deployed? | To understand what infrastructure exists |
| What does the end-to-end pipeline look like today? | To understand what we're replacing vs. building from scratch |

### 2.2 Accenture's Involvement (Critical Context)

| Question | Why We Need It |
|----------|---------------|
| What deliverables did Accenture produce? | To understand what exists vs. what was abandoned |
| How was the problem statement given to Accenture? | Was it well-scoped or vague? If vague, we risk the same outcome |
| Did Lam provide Accenture enough information to succeed? | We need to avoid the same trap if the problem is client-side |
| Why was the Accenture engagement ended? | Success, failure, budget, relationship, or something else? |

### 2.3 Top Applications (Technical Level)

| Question | Why We Need It |
|----------|---------------|
| Top 3 most important RAG-like applications, described technically | Scoping the control plane and prioritizing migration |
| What systems do they touch? (Databases, APIs, etc.) | Architecture planning |
| What data sources feed each? | Understanding data overlap (Colin's hypothesis: they share sources) |
| Are they truly unique or variations of the same pattern? | Validates the "one project reused many times" theory |
| Which has the highest business impact if fixed? | POC selection |

### 2.4 Organizational Reality Check

| Question | Why We Need It |
|----------|---------------|
| What is the actual technical governance structure? | Brad's version may not match reality |
| Does IT/cybersecurity have veto power? | Proposal risk |
| Who controls infrastructure decisions? | Cloud, data residency, service selection |

### 2.5 The "2-5 Seconds" Clarification
- Is the 2-5 second requirement for upload completion, RAG readiness, or real-time detection notification?
- This fundamentally changes the architecture if it's for instant RAG readiness vs. just upload acknowledgment

---

## Priority 3: What Requires Document Samples or Hands-On Access

These are needed for the POC itself, not for proposal writing.

### 3.1 Representative Documents
- A sample document of the type they're worried about (even sanitized)
- A sample support ticket with the kind of customer information that gets flagged
- Examples of the specific entities that need detection (customer names, fab IDs, site identifiers)

### 3.2 Test Data for Validation
- Real false positive examples from their prior model testing
- A small labeled dataset to benchmark against
- The specific "7th ticket with a violation" Brad mentioned -- what did that actually look like?

### 3.3 System Access
- API documentation for their ingestion endpoints
- Access to a non-production environment (if pilot approved)
- Prior model training artifacts from the Accenture/internal effort

### 3.4 Governance Documentation
- Written policies for customer confidential information handling
- Customer contractual requirements around data segregation
- Current ACL/role definitions in their systems

---

## Sequencing

| Step | Action | Owner | Gate |
|------|--------|-------|------|
| 1 | Email Pat with Priority 1 asks (especially 1.1) | Anuj + Colin | None |
| 2 | Get Priority 1 responses | Pat/Anuj | Lam responsiveness |
| 3 | Schedule Daniel technical call | Anuj/Pat | Priority 1 answered |
| 4 | Daniel call: extract Priority 2 | Colin | Call scheduled |
| 5 | Request Priority 3 items | Colin via Pat | Pilot/POC greenlit |
| 6 | Build POC | Colin | Priority 3 items received |
