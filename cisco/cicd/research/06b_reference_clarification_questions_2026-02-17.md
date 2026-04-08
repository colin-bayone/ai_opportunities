# 06b - Reference: Clarification Questions

**Source:** /cisco/cicd/source/reference_clarification_questions_2026-02-17.md
**Source Date:** 2026-02-17 (prepared after Dec 15 discovery call, refined through Feb 17 discovery)
**Document Set:** 06b (Supplementary: Formal clarification questions for Cisco)
**Pass:** Inventory and status assessment

---

## Overview

This document contains 31 formal questions prepared by Colin for Cisco, organized by use case. The questions were drafted based on the December 15, 2025 discovery call and refined through subsequent meetings. They represent the structured gap analysis for the engagement.

## Question Status After Set 06

Based on the Feb 17 discovery meeting (Set 06), here is the status of each question:

### Answered or Partially Answered by Set 06

| # | Topic | Answer from Set 06 |
|---|-------|-------------------|
| 27 | AI models/APIs | DeepSight platform provides SDK and AI infrastructure. BayOne builds on top of it. |
| 29 | Infrastructure hosting | All on-prem: MySQL, MongoDB, Podman, Jenkins, ADS machines. VPN required. |
| 30 | Security/compliance constraints | VPN required, Cisco laptop or Cisco image, GitHub Enterprise training, read-only access to main repos. |

### Partially Addressed

| # | Topic | What We Know |
|---|-------|-------------|
| 6 | APIs for CAT, DevX, Jenkins, Airflow, Grafana | Jenkins access offered directly. Splunk is security-only. Others not yet addressed. |
| 14 | Log data from Jenkins/Airflow | Direct Jenkins log access confirmed. Airflow not yet explored (separate team). |
| 28 | AI model restrictions | DeepSight SDK implies Cisco-approved stack. Specifics not discussed. |

### Still Open (~25 questions)

Questions 1-5 (scale metrics, baseline metrics, success criteria, MVP timeline), 7-13, 15-26, and 31 remain unanswered. These represent the ~30 of 65 discovery questions still outstanding as noted in Set 06.

## Strategic Notes

1. **Question 31 (day-in-the-life session)** is particularly important and should be prioritized during the onboarding phase.
2. **Questions 1-5 (General/Cross-Cutting)** are prerequisites for any meaningful estimation or planning.
3. **Questions 20-23 (Self-Healing governance)** are deferred since Use Case E is not in initial scope.
4. **The DeepSight revelation (Set 06) reframes several questions.** Question 27 about "bringing our own LLM solutions" is now moot — DeepSight provides the AI infrastructure. Similarly, question 29 about hosting is largely answered.

## File Reference

The raw question document is preserved in source as `/cisco/cicd/source/reference_clarification_questions_2026-02-17.md`. This research file adds status tracking and context from subsequent sets.
