# 03 - Discussion: Final Clarifications

**Source:** Working discussion between Colin Moore and Claude
**Source Date:** 2026-03-20
**Document Set:** 03 (Technical Approach Discussion)
**Context:** Final Q&A round -- problem framing, sample requirements, and engagement positioning

---

## 1. Problem Restatement Strategy: Their Words, Then Our Reframe

### Document 1: Use Their Framing
Restate the problem using Mikhail's language and structure (two swim lanes, detection vs. redaction, self-help search vs. escalation entry). This demonstrates we listened.

### Document 2: Reframe from Authority
Show our approach, which naturally corrects the framing:

**The technical reality Lam is missing:** Detection is a necessary step for redaction. You cannot redact something if you haven't detected/identified it first. Redaction is simply an extra step after detection. They are separating things that are technically the same pipeline -- detect, then decide what to do (flag, reject, redact, quarantine). The fact that they frame these as separate business cases reveals they have no technical concept of how this actually works.

**How to handle this:** We don't take them to school. We don't say "you're wrong." We reframe based on our experience, coming from a position of authority where we've done this before. The approach document naturally shows a unified pipeline where detection feeds into action -- and the "two swim lanes" just become two modes of the same system (real-time at ingestion vs. batch on historical data).

---

## 2. Representative Sample: What We Actually Need

### What "Representative Sample" Means

A selection of documents (not one file type, not one file) that give us a view into what people are using the system for day-to-day. Must include:

- **Failure cases:** Documents that contain the kind of content that should be caught. We cannot detect things if we do not have examples of what to catch.
- **Known good examples:** Documents that are clean and should pass through without flagging. This is the gold standard.
- **Both are required.** We need the good and the bad to calibrate.

### It's Not Just Documents

The sample needs to reflect the actual data sources feeding the system:
- Documents (PDFs, Word docs, procedures)
- Emails or tickets
- Excel files
- SharePoint or OneDrive content
- Live queries to a database
- Anything else that could be a data source for the RAG system

Text pattern matching doesn't change between file types, but if the context or structure of documents is drastically different, we need to see what the things that should be caught look like in each context.

### If It's a Live Connection

For live data sources (databases, APIs), we either need:
1. An export of representative data, tagged by the Lam team as "this should be flagged" / "this is clean"
2. OR direct access to the data source plus access to an SME who can explain what should and should not be flagged

### The Dependency Chain

The answer to "what samples do we need" also depends on which use case / application is selected as the first one. The samples must come from that specific application's data sources. This is why naming the first application (Priority 1.1 from the open information needs) gates everything else.

### Do NOT Fixate on Timeline Claims

The "95%+ in a day" statement was hyperbole to illustrate that the problem is not as hard as Lam thinks. It is not a timeline commitment. Do not reference it in proposals, discussions, or planning documents.

---

## 3. The Control Plane Is a Project, Not a Product

### What It Is
A **custom build for Lam**, tailored to their environment, their data sources, and their specific needs. It is a consulting engagement: "we will come in, get this set up for you, and we're more than happy to provide long-term support and build off of this."

### What It Is NOT
- Not a product sitting in BayOne's back pocket ready to deploy
- Not an out-of-the-box solution
- Not a one-size-fits-all platform
- Not something we already have that magically solves any problem

### How to Describe It
- **Always call it a "solution," never a "product"**
- "A tailor-made solution using the same methodology and blueprint as has been applied at previous customers"
- Every client's environment is drastically different -- the methodology is reusable, the implementation is custom

### Prior Work as Credibility (Without Overpromising)
Colin has built similar architectures for:
- **Coherent Corp** -- massive global enterprise, many teams across finance, engineering, sales, service, manufacturing
- **A retail customer** -- Salesforce-based, completely different stack
- **An Oracle Cloud customer** -- different cloud, different use case

Each was custom. The pattern and expertise transfer; the code does not.

### Reusability Is Internal, Not Client-Facing
When Colin architects and builds this, he will build it to be reusable (good engineering practice). But that's an internal BayOne benefit -- it is never positioned to the client as "we have a pre-built thing."

The only scenario where it becomes product-like is if Lam wants BayOne to **maintain it long-term** -- managed service model. That's a conversation for later, not the proposal.

---

## 4. Scope Discipline: Stay Within Brad's Problem Statement

### What We Focus On
Solely the problem statement within Brad's team:
- Customer IP detection and protection across their document/knowledge systems
- The two use cases Mikhail presented (even though we'll reframe the approach)
- The ingestion pipeline, control plane, and historical data cleanup

### What We Mention Only in Passing
- "This architecture can naturally enable other AI activities once the immediate issue is solved"
- "If that is of interest strategically, we can discuss when the team is ready"
- Stop there. Do not elaborate. Do not list examples. Do not pitch growth.

### Why This Discipline Matters
Mikhail was dismissive of anything beyond the stated use cases. Brad explicitly said "we don't want to introduce noise in our business case." Colin got redirected on the call for exactly this kind of scope expansion. The proposal must not repeat that mistake.

The future potential is real and massive (Anuj's "boil the ocean" instinct is correct from a capability standpoint), but the presentation must be laser-focused on what was asked. Earn the right to expand later by delivering on the immediate ask first.
