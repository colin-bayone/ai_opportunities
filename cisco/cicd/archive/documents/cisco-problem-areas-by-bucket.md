# Cisco CI/CD Pipeline: Problem Areas by Bucket

Based on the discovery call held December 15, 2025.

---

## Developer Box (Blue)

### No visibility into local loop / "black box"
Currently, there is no way for the organization to see what testing or validation happens before a PR is submitted. Srini stated: "We don't have visibility... we want to get the visibility and insights on what's happening at the local loop." They want to track anything that is scripted; only manual image loading would be excluded from tracking.

### No tracking of tests run before PR submission
The goal is end-to-end traceability—tracking test cases "from when it started all the way until it got merged" (Srini). Today this doesn't exist for the pre-PR phase.

### Unit test failures debugged manually
Developers debug test failures on their own without tooling assistance. The process involves manually loading an image on hardware and building a test topology based on the feature being changed.

### No coverage tracking for changed code
There's no way to verify that specific code changes were actually exercised by tests. Srini explained: "If I change a function foo... there is no easy way whether that particular condition has been touched through my validation." They want condition-level tracking, not just function-level—if a PR changes two `if` conditions, they want confirmation those specific conditions were hit.

---

## GitHub PR Validation (Green)

### Engineers don't know where PR is stuck or why
There's no unified view that tells a developer where in the 39-gate process their PR currently sits, or what action is needed.

### "Fire and forget" behavior with no consolidated status view
Engineers submit PRs and have no easy way to monitor progress. Divakar gave the example: an engineer pushing 5 bug fixes on different branches has no single view of status across all of them. The desired state is a table showing "these are the five PRs... this one is Green, this one has a build failure" so engineers can quickly act.

### Fragmented data sources with no unified interface
Information is scattered across multiple systems. Srini described: "We have one CAT tool... then we have a DevX platform that has some DB... and we have these Jenkins and Airflows that are running in silos." A user today cannot ask one system a single question and get a complete answer.

**Note:** Grafana dashboards already exist and provide analytics on gate performance, PR times, and anomalies. Yet Cisco describes a lack of visibility into PR status. This suggests the data exists but isn't consolidated or actionable in the way developers need it—or there's a gap between what Grafana shows vs. what developers actually need to see.

### No chat/conversational interface
There is no way to ask a natural language question like "Where is my PR?" and get an answer. Srini confirmed: "There is no chat enabled in this entire workflow... we'd like to have that."

### Manual triage of failures
When a gate fails, engineers must manually investigate the cause. The desired state is for AI to "triage the build failure automatically and come back with some information or maybe a possible code diff" to help the engineer fix it (Divakar).

### Self-healing / auto-resume desired
For failures that don't require human judgment, Cisco wants the system to take corrective action automatically. Srini stated: "If the user intervention is not required, technically the system should be able to correct itself and move on."

**Note:** Cisco mentioned they already have an internal AI code review project that "will go live soon" (Srini). Self-healing, auto-resume, and AI-assisted triage would likely fall under the same umbrella as AI code review. The boundary between what they're building internally vs. what they want from us is unclear.

### Coverage tracking incomplete
Even at the CI level, there's no confirmation that the specific code changes in a PR were actually tested. CDT (Context Driven Testing) exists and does a reverse lookup from function → test case, but tracking of whether coverage actually occurred for a given PR is incomplete.

**Note:** CDT has been live for 2+ years and Srini described it as "already solved." However, they also say they cannot confirm if specific code changes were exercised. This suggests either CDT has gaps they haven't articulated, or they want something beyond what CDT provides—this needs clarification.

---

## Existing Infrastructure (Context)

- **39 gates** including: build validation, static analysis, compiler warnings, sanities, bug severity, CDT, diff check, code review, control characters, copyright check
- **Jenkins** handles short/quick checks
- **Apache Airflow** handles longer-running jobs
- **CAT (Commit Approval Tool)** is a UI that manages which gates are enabled for each branch
- **Grafana dashboards** provide analytics on gate performance, PR times, and anomalies

---

## Official Build / CD (Red)

### Branch health visibility for release leads
Release leads managing a branch need a consolidated view of the branch's overall status. Anand mentioned that "a lot of things can be done at the branch level to make things simple," but specifics were not elaborated.

### Understanding failures at the branch level
When something goes wrong, release leads need to quickly understand the cause and who is responsible. Anand framed this as: "Why things went bad? Who should I go after?"

### Automatic corrections at branch level
Similar to the self-healing concept in PR validation, Cisco wants to explore what can be automatically corrected at the branch level without release lead intervention.
