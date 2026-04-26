# Confidential Information Detection
## Proof-of-Concept Proposal

**A Layered Detection Methodology for Domain-Specific Entity Identification**

**Prepared for:** Lam Research
**Date:** April 2026
**Author:** BayOne Solutions

---

## Executive Summary

BayOne Solutions proposes a three-week proof-of-concept engagement to demonstrate an improved detection methodology for confidential information within the Escalation Solver application.

This engagement will assess the current data landscape, establish the maximum achievable detection accuracy, and deliver a working detection approach benchmarked against prior efforts. The POC is scoped to five free-text fields and two entity types (customer name and fab identifier) within Escalation Solver.

The three-week engagement begins from the date BayOne receives access to the required data and reference materials. The data assessment, detection methodology, evaluation protocol, and detection targets established during the POC serve as the foundation for any subsequent engagement. This work does not need to be repeated.

---

## 01 Problem Statement

Lam Research manages escalation workflows containing customer-confidential information across multiple free-text fields. The current detection capability, developed over a prior 18-month effort using multiple Named Entity Recognition models in parallel, did not meet the operational thresholds required to enable cross-customer knowledge sharing.

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
**Deliverable:** EDA report with baseline accuracy assessment and maximum achievable accuracy

BayOne will conduct a systematic assessment of the available data, reference materials, and labeled examples to understand the detection landscape before any model development begins.

**Data Quality Assessment**

BayOne will evaluate the existing reference data (customer name lists, fab/location identifier lists, exclusion lists, and previously labeled examples) for completeness, consistency, and reliability. If contradictions exist within the reference data, BayOne will document these findings and their impact on achievable accuracy.

**Exploratory Data Analysis**

Using statistical analysis, BayOne will assess data separability between entity classes, evaluate the distribution and volume of content across the target fields, and determine the sample sufficiency of existing labeled data. The EDA produces a definitive assessment of what detection accuracy is achievable given the current data.

**Phase 1 Deliverables**

| Deliverable | Description |
|---|---|
| Data Quality Report | Assessment of reference data completeness, consistency, and contradictions with impact on achievable accuracy |
| Statistical Analysis | Data separability, class distribution, volume assessment, and sample sufficiency determination |
| Detection Target Map | Documented entity types, known variations, authoritative sources, and validation criteria |
| Accuracy Ceiling | Maximum achievable detection accuracy given data quality, determined through analysis rather than assumption |

### Phase 2: Detection Build and Benchmarking

**Duration:** Approximately two weeks following Phase 1
**Deliverable:** Working detection demonstration, methodology documentation, scaling path

BayOne will build and demonstrate the detection approach using a layered methodology. Rather than running multiple models in parallel and reconciling their outputs, this approach processes data through sequential layers of increasing capability:

1. **Deterministic layer:** Handles known patterns with high confidence and low computational cost
2. **Machine learning and NLP layer:** Addresses nuanced cases that deterministic matching cannot reach
3. **Generative AI layer:** Where required, provides contextual judgment on ambiguous cases

Each layer reduces the problem space for the next, resulting in higher cumulative accuracy and lower computational cost than any single approach operating independently.

BayOne will benchmark detection results against the prior effort baseline as documented by Lam Research, using a defined, repeatable evaluation protocol. The methodology documentation will explain how each layer contributes to accuracy improvement and how the approach extends to additional entity types, fields, and applications.

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
| 1 | Discovery and Data Assessment | Data quality evaluation, exploratory data analysis, baseline accuracy determination, detection target mapping |
| 2-3 | Detection Build and Benchmarking | Layered detection implementation, accuracy measurement, methodology documentation, scaling path |

The timeline begins upon receipt of the required data, reference materials, and access to a Lam Research subject matter expert. Some Phase 1 activities (initial consultation on detection targets and criteria) can proceed in parallel with data provisioning.

### Exclusions

- **Additional entity types beyond customer name and fab identifier.** BayOne will document a scaling path for additional entity types, but the POC is bounded to two.
- **Additional applications beyond Escalation Solver.** The methodology is designed to extend across applications, but the POC is scoped to one.
- **Production integration.** POC deliverables demonstrate the approach against real data. Integration into the Escalation Solver application is a subsequent engagement activity.
- **Document and attachment scanning.** The POC is scoped to free-text fields within escalation tickets.
- **Ground truth remediation.** If the existing reference data contains significant quality issues, BayOne will document the findings and recommend a remediation path. Resolving data quality issues at scale is beyond the POC scope.

---

## 04 Investment

### Proof-of-Concept (This Proposal)

- **Investment:** $15,000
- **Duration:** Three weeks from data access
- **Deliverables:** EDA report, detection demonstration, methodology documentation, accuracy benchmarking, scaling path

### Subsequent Engagement (Upon Approval)

- **Model:** Outcome-based engagement
- **Scope:** Determined collaboratively based on POC findings and Lam Research priorities
- **Foundation:** All POC methodology and analysis transfers directly

The data assessment, detection methodology, evaluation protocol, and detection targets established during the POC serve as the foundation for any subsequent engagement. This work does not need to be repeated.

---

## 05 Assumptions and Dependencies

### Assumptions

- Lam Research provides access to Escalation Solver data, reference lists (customer names, fab/location identifiers, exclusion lists), and any previously labeled examples that informed the prior detection effort
- Lam Research designates one or more subject matter experts available during the POC period who can define detection targets, validate detection results, and confirm what constitutes a true positive
- Detection scope is five free-text fields and two entity types (customer name, fab identifier); additional scope is documented for a subsequent engagement
- Baseline accuracy of existing reference data is assessed during discovery; maximum achievable accuracy is bounded by data quality
- Data volume and scope are agreed during discovery; the POC is designed for a representative data set
- The execution environment (Lam Research infrastructure or BayOne infrastructure) is agreed upon before the engagement begins, as described in the Engagement Pricing document
- Lam Research provides timely feedback and validation during the POC period. Once the engagement is underway, if cumulative project delays beyond BayOne's control exceed 50% of the remaining engagement duration, both parties will formally review engagement terms through a change request process, which may include timeline adjustment, scope adjustment, or additional investment.
- BayOne handles all data in accordance with confidentiality requirements; customer names are redacted from all BayOne-produced documents
- Lam Research provides documentation of prior detection effort results and target performance aims to serve as a benchmark

### Dependencies

- Data access provisioning (Escalation Solver data, reference materials, and labeled examples)
- Subject matter expert availability during the POC period
- Lam Research internal coordination for data access within a reasonable timeframe
- Execution environment provisioning (VM or equivalent for Option A, data export for Option B)

---

## 06 Risk Factors

| Risk | Mitigation |
|------|------------|
| Data quality issues discovered during assessment (contradictory, incomplete, or insufficient reference data) | EDA deliverable documents findings formally; joint decision to proceed, adjust scope, or extend engagement |
| Data access delays due to internal coordination | Three-week timeline does not begin until access is provided |
| Subject matter expert availability constraints | SME designated with availability during POC; cumulative delays beyond 50% of remaining engagement duration trigger a formal change request process |
| Data volume exceeds three-week POC capacity | Volume and scope agreed during discovery before build phase begins |
| Scope requests beyond agreed five fields and two entity types | Scope defined with explicit exclusions; additional requests documented for subsequent engagement |

---

## 07 Next Steps

- **Data provisioning:** Lam Research provides access to Escalation Solver data, reference lists, and labeled examples
- **SME designation:** Lam Research identifies the subject matter expert(s) available during the POC period
- **Kickoff:** Brief alignment on detection targets, success criteria, and communication cadence
- **Discovery start:** The three-week POC begins upon receipt of the required data and access

BayOne will deliver the discovery assessment within the first week of data access. The detection build and benchmarking will proceed in weeks two and three, with the final deliverables presented at the conclusion of the engagement.

---

**BayOne Solutions** — Confidential, Prepared for Lam Research
