# Questions for Cisco: Clarification Needed to Progress

Based on the discovery call held December 15, 2025.

---

**Note:** The discovery call provided a good overview of the problem areas, but we do not yet have visibility into the scale, extent, or specifics of what this work touches. Without this information, we cannot provide meaningful estimates or timelines. The questions below are designed to close that gap.

---

## General / Cross-Cutting

1. What is the volume of PRs per day/week? How many developers are active? How many branches are maintained?

2. How many repositories does this apply to? Is the developer workflow consistent across repositories, or does it vary?

3. What baseline metrics exist today? (e.g., average PR merge time, failure rates by gate, PRs merged per week)

4. What quantitative improvement targets would define success for this engagement?

5. What is Cisco's timeline for an MVP? What capabilities would need to be included for an MVP to be considered successful?

---

## Unified Data Layer / Chat Interface

6. What APIs or data access points exist for CAT, DevX, Jenkins, Airflow, and Grafana? Is there existing documentation for these?

7. What log formats and data schemas are available from each system?

8. Can you provide examples of the data or logs from each system? (e.g., sample API responses, log files, dashboard exports)

9. Grafana dashboards already provide analytics on gate performance and PR times—what specific visibility is missing that Grafana doesn't provide today?

10. For the chat interface, what questions should it be able to answer? (e.g., "Where is my PR?" "Why did gate X fail?" "What PRs are blocked?")

---

## Developer Box Instrumentation

11. What specific data do you want captured from the local loop? (e.g., test names, pass/fail status, duration, coverage metrics)

12. How would this data be collected? Is there an expectation of an agent on developer machines, CI hooks, integration with pyATS, or another mechanism?

13. How much variation exists across teams in how local testing is done?

---

## AI Diagnosis for Gate Failures

14. What log data and failure outputs are available from Jenkins and Airflow jobs?

15. Are there common failure patterns that account for a large percentage of gate failures? (e.g., copyright check, build errors, static analysis)

16. What format would be most useful for diagnosis output—text summary, suggested code diff, link to relevant logs, something else?

---

## Coverage Tracking

17. CDT has been running for 2+ years and was described as "already solved"—what specific gaps exist, or what do you need beyond what CDT currently provides?

18. Is condition-level coverage tracking (vs. function-level) the goal, or is there something else?

19. Should coverage be tracked in the Developer Box, CI, or both?

---

## Self-Healing / Auto-Resume

20. What is the boundary between your internal AI code review project and the self-healing/auto-resume capabilities you're asking us to explore?

21. What types of failures would be acceptable to auto-correct without engineer approval? (e.g., copyright check failures vs. build failures)

22. Who defines and governs what actions AI can take autonomously vs. what requires human review? Is there an existing policy?

23. If no policy exists, would defining these governance criteria be part of our scope?

---

## Branch Health / CD Visibility

24. What specific information do release leads need that they don't have today?

25. Are there existing reports or dashboards for release leads, or would this be net new?

26. What does "automated follow-up identification" look like—notifications, assignments, escalations?

---

## AI and Infrastructure

27. For any AI-driven capabilities, should we bring our own LLM solutions and API keys, or will Cisco provide these?

28. Are there restrictions on what AI models or services can be used? (e.g., approved vendors, data residency requirements)

29. Where is the existing infrastructure hosted? (e.g., on-prem, cloud, hybrid) Specifically for Jenkins, Airflow, CAT, DevX, and Grafana.

30. Are there security, compliance, or network constraints we need to be aware of for any integration work?

---

## Process Request

31. We'd like to request a screen share or "day in the life" session to observe the workflow in practice for both a developer and a release lead.

While the high-level workflow has been described, the implementation appears to be highly customized. To accurately scope this work, we need a more detailed understanding of actual day-to-day activities—particularly where they deviate from a standard DevOps playbook. 
