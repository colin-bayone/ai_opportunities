# Confidential Information Detection
## Proof-of-Concept Proposal

**Prepared for:** Lam Research
**Date:** April 2026
**Author:** BayOne Solutions

---

## Executive Summary

BayOne Solutions proposes a three-week proof-of-concept engagement to demonstrate an improved detection methodology for confidential information within the Escalation Solver application. This engagement will assess the current data landscape, establish the maximum achievable detection accuracy, and deliver a working detection approach benchmarked against prior efforts.

The POC is scoped to five free-text fields and two entity types (customer name and fab identifier) within Escalation Solver. The three-week engagement begins from the date BayOne receives access to the required data and reference materials.

---

## 01 Problem Statement

Lam Research manages escalation workflows containing customer-confidential information across multiple free-text fields. The current detection capability, developed over a prior 18-month effort using multiple Named Entity Recognition (NER) models in parallel, did not meet the operational thresholds required to enable cross-customer knowledge sharing.

The core challenge is domain-specific: standard NER models are trained on generic entity types (person names, organizations, locations) and have no concept of semiconductor-specific entities such as customer name variations, fab identifiers, or site-specific references with inconsistent formatting.

### Success Criteria

This proof-of-concept will be considered successful if:

1. A baseline data assessment is completed, including data quality evaluation and determination of maximum achievable detection accuracy
2. The detection approach is demonstrated against real Escalation Solver data for two entity types (customer name, fab identifier) across five free-text fields
3. Detection performance is measured and reported using a defined evaluation protocol that can be repeated and built upon in subsequent phases
4. The detection methodology is documented, showing how each layer of the approach contributes to accuracy improvement
5. A clear path is documented for how the approach scales from proof-of-concept to a broader engagement

---

## 02 Proposed Approach

The engagement is structured in two phases: a discovery phase to assess the data landscape and establish what is achievable, followed by a build phase to demonstrate the detection methodology against real data.

### Phase 1: Discovery and Data Assessment

**Duration:** Approximately one week from data access
**Deliverable:** Exploratory data analysis report with baseline accuracy assessment and maximum achievable accuracy determination

BayOne will conduct a systematic assessment of the available data, reference materials, and labeled examples to understand the detection landscape before any model development begins.

**Data Quality Assessment**

BayOne will evaluate the existing reference data (customer name lists, fab/location identifier lists, exclusion lists, and previously labeled examples) for completeness, consistency, and reliability. If contradictions exist within the reference data, for instance, content flagged as confidential in one context but present in approved documents elsewhere, BayOne will document these findings and their impact on achievable accuracy.

**Exploratory Data Analysis (EDA)**

Using statistical analysis, BayOne will assess data separability between entity classes, evaluate the distribution and volume of content across the target fields, and determine the sample sufficiency of existing labeled data. The EDA produces a definitive assessment of what detection accuracy is achievable given the current data, rather than an estimate based on assumptions.

**Discovery Activities**

During this phase, BayOne will also identify the authoritative sources for detection criteria, map the data access and validation workflow, and document the specific detection targets and their variations. These findings carry forward as lasting artifacts that do not need to be repeated in a subsequent engagement.

### Phase 2: Detection Build and Benchmarking

**Duration:** Approximately two weeks following Phase 1
**Deliverable:** Working detection demonstration with measured performance, methodology documentation, and scaling path

BayOne will build and demonstrate the detection approach using a layered methodology. Rather than running multiple models in parallel and reconciling their outputs, this approach processes data through sequential layers of increasing capability:

1. A deterministic layer handles known patterns with high confidence and low computational cost
2. A machine learning and natural language processing layer addresses nuanced cases that deterministic matching cannot reach
3. Where required, a generative AI layer provides contextual judgment on ambiguous cases

Each layer reduces the problem space for the next, resulting in higher cumulative accuracy and lower computational cost than any single approach operating independently.

BayOne will benchmark detection results against the prior effort baseline as documented by Lam Research, using a defined, repeatable evaluation protocol. The methodology documentation will explain how each layer contributes to accuracy improvement and how the approach would extend to additional entity types, fields, and applications.

---

## 03 Scope and Timeline

### POC Scope

- **Application:** Escalation Solver (five free-text fields, 4,000 to 5,000 characters each)
- **Entity types:** Customer name and fab identifier
- **Depth:** End-to-end detection demonstrated against real data with measured accuracy
- **Deliverables:** EDA report, working detection demonstration, methodology documentation, accuracy benchmarking, scaling path

### Timeline

**Total Duration:** Three weeks from data access

| Week | Phase | Activities |
|------|-------|------------|
| 1 | Discovery and Data Assessment | Data quality evaluation, EDA, baseline accuracy determination, detection target mapping |
| 2-3 | Detection Build and Benchmarking | Layered detection implementation, accuracy measurement, methodology documentation |

The timeline begins upon receipt of the required data, reference materials, and access to a Lam subject matter expert. Some Phase 1 activities (initial consultation on detection targets and criteria) can proceed in parallel with data provisioning.

### Exclusions

- **Additional entity types beyond customer name and fab identifier.** BayOne will document a scaling path for additional entity types, but the POC is bounded to two.
- **Additional applications beyond Escalation Solver.** The methodology is designed to extend across applications, but the POC is scoped to one.
- **Production integration.** POC deliverables demonstrate the approach against real data. Integration into the Escalation Solver application is a subsequent engagement activity.
- **Document and attachment scanning.** The POC is scoped to free-text fields within escalation tickets.
- **Ground truth remediation.** If the existing reference data contains significant quality issues, BayOne will document the findings and recommend a remediation path. Resolving data quality issues at scale is beyond the POC scope and would be addressed in a subsequent engagement.

---

## 04 Investment

| | |
|---|---|
| **Proof-of-Concept (This Proposal)** | **$10,000** |
| Duration | Three weeks from data access |
| Deliverables | EDA report, detection demonstration, methodology documentation, accuracy benchmarking, scaling path |
| Foundation | Data assessment, detection methodology, and evaluation protocol developed during this engagement carry forward to any subsequent engagement |

The data assessment, detection methodology, evaluation protocol, and detection targets established during the POC serve as the foundation for any subsequent engagement. This work does not need to be repeated.

---

## 05 Assumptions

- Lam Research provides access to Escalation Solver data, reference lists (customer names, fab/location identifiers, exclusion lists), and any previously labeled examples that informed the prior detection effort. The three-week timeline begins from the date this access is provided.
- Lam Research designates one or more subject matter experts who can define detection targets, validate detection results, and confirm what constitutes a true positive. Availability during the POC period is required.
- The detection scope is five free-text fields and two entity types (customer name, fab identifier). Requests beyond this scope are documented as candidates for a subsequent engagement.
- BayOne will assess the baseline accuracy of the existing reference data during the discovery phase. If the data contains contradictions or quality issues, the maximum achievable accuracy is bounded by the data quality. BayOne will report on findings and recommend refinements, but resolving data quality issues at scale is not within the POC scope.
- Data volume and scope are agreed during the discovery phase. The POC is designed for a representative data set. Processing at enterprise scale (hundreds of thousands of records) would require scope and timeline adjustment.
- The POC runs on BayOne infrastructure unless there is a specific requirement to operate within the Lam Research environment, in which case BayOne will need details about the existing environment and its availability.
- Lam Research manages internal coordination required to provide data access within a reasonable timeframe. BayOne cannot control internal team availability or scheduling.
- Lam Research provides timely feedback and validation during the POC period. If response times extend beyond an agreed window, the POC timeline extends accordingly.
- BayOne handles all Lam Research data in accordance with confidentiality requirements. Customer names are redacted from all BayOne-produced documents.
- This engagement does not include production integration into Escalation Solver or any other application.

---

## 06 Risk Factors

| Risk | Mitigation |
|------|------------|
| Data quality issues discovered during the assessment phase (contradictory, incomplete, or insufficient reference data) | The EDA deliverable documents findings formally. BayOne and Lam Research jointly determine whether to proceed with the build phase, adjust scope, or extend the engagement to address data quality. |
| Data access delays due to internal coordination | The three-week POC timeline does not begin until access is provided. BayOne cannot control internal scheduling. |
| Subject matter expert availability constraints compress the effective build window | Lam Research designates an SME with availability during the POC period. If response times extend beyond the agreed window, the timeline extends accordingly. |
| Data volume exceeds what the three-week POC can process | Volume and scope are agreed during the discovery phase before the build phase begins. |
| Scope requests beyond the agreed five fields and two entity types | POC scope is defined with explicit exclusions. Additional requests are documented as candidates for the subsequent engagement. |

---

## 07 Next Steps

- **Data provisioning:** Lam Research provides access to Escalation Solver data, reference lists, and labeled examples
- **SME designation:** Lam Research identifies the subject matter expert(s) available during the POC period
- **Kickoff:** Brief alignment on detection targets, success criteria, and communication cadence
- **Discovery start:** The three-week POC begins upon receipt of the required data and access

BayOne will deliver the discovery assessment within the first week of data access. The detection build and benchmarking will proceed in weeks two and three, with the final deliverables presented at the conclusion of the engagement.
