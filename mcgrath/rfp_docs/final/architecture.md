# McGrath RentCorp - Future State Architecture (Verified)

**Source:** MGRC Environment tab - embedded Visio diagram
**Verified:** February 24, 2026 (human + AI review)
**Type:** Future State Integration Architecture (Post-NextGen Implementation)

---

## Legend

| Outline Color | Meaning |
|---------------|---------|
| Blue | Synchronous integration |
| Amber/Orange | Asynchronous integration |

---

## Oracle Cloud Application Suite

The core of the architecture is Oracle Cloud Applications, organized into four major functional areas:

### Oracle Cloud SCM (Supply Chain Management)
- Demand & Supply
- Maintenance
- Inventory
- Procurement
- Order Management
- Product Data Hub
- Supplier Management
- Supplier Portal
- Install Base
- Maintenance Cloud
- Cost Management
- Employee Data

### Oracle Cloud ERP (Enterprise Resource Planning)
- General Ledger
- Project Management
- Fixed Assets
- Payables
- Receivables
- Advanced Collections
- Cash Management
- Reporting & Analytics

### Oracle Cloud CX (Customer Experience)
- Cloud Service
- Field Service Management

### Oracle Cloud EPM (Enterprise Performance Management)
- Enterprise Planning
- Account Reconciliation
- Narrative Reporting

---

## External Systems by Functional Area

### CRM & Sales (Top Center)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **Salesforce** (contains Pardot, Salesforce CPQ) | Synchronous | Quote/Contract, Customer Master, Item Master |
| **Xactly** | Asynchronous | Sales Compensation |
| **Dun & Bradstreet** | Synchronous | Credit Check |
| **DocuSign** | Synchronous | Contract Creation & Revision |
| **Zilliant** | Asynchronous | Quote/Contract Information |
| **Oracle CRM on Demand** | - | Customer Master (legacy CRM) |
| **Nextstar** | - | Adjacent to Oracle CRM on Demand |

### Revenue & Billing (Center)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **RecVue** | Synchronous | Quotes & Contracts, Revenue/Billing to ERP |
| **Avalara** | Synchronous | Tax Calculation |
| **Billtrust** | Synchronous | Invoice PDFs |

### Banking & Payments (Right Side)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **Bank** | Synchronous | Bank & Debit/Credit Line (APO), BAI2 Statements |
| **SnapPay** | Synchronous | Payment Processing |
| **XE** | Synchronous | Currency/Exchange Rates |

### Data & Analytics (Top)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **Snowflake** | - | Extract (data warehouse) |
| **Tableau** | - | Equipment Status, BI visualization |
| **Rivery + SplashBI** | - | Sync, ETL/Data pipeline |

### HR & Identity (Right Side)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **ADP** | Asynchronous | Payroll/HR Data |
| **AD (Active Directory)** | Synchronous | Identity Management |

### Expense & Travel (Top Left - connecting to Payables)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **Emburse** | Synchronous | Expense Management |
| **Corporate Travel Management** | Synchronous | Travel Expenses |
| **EHS** | Synchronous | Environment, Health & Safety |
| **OC Tanner** | Synchronous | Employee Recognition |

### Supply Chain & Vendors (Left Side - connecting to SCM)

| System | Integration Type | Key Data Flows |
|--------|------------------|----------------|
| **Intellinum** | Synchronous | Scan & Labeling, Purchase Orders |
| **JONES** | Synchronous | COI - New Vendor Data, COI - Compliance Status |
| **Oracle Aconex** | Asynchronous | Project Creation |

### Custom/Legacy Applications

| System | Type | Notes |
|--------|------|-------|
| **Material Voucher** | Java Application | Custom app connecting to Inventory - potential legacy risk |

---

## Key Integration Patterns

### Quote-to-Cash Flow
```
Salesforce CPQ → DocuSign (contracts) → RecVue (billing) → Oracle ERP (Receivables)
                                                        ↓
Zilliant → Quote/Contract Info → Salesforce       Billtrust (Invoice PDFs)
```

### Procure-to-Pay Flow
```
JONES (Vendor Compliance) → Supplier Management → Procurement
                                                       ↓
Intellinum (Scan/Label) → Inventory → Order Management → Automated PO Creation
```

### Financial Close Flow
```
Oracle ERP (GL, AR, AP) → Oracle EPM (Enterprise Planning)
                                    ↓
                         Account Reconciliation → Narrative Reporting
```

### Data & Analytics Flow
```
Oracle Cloud → Snowflake (Extract) → Tableau / SplashBI
                    ↑
              Rivery (ETL)
```

---

## Complexity Assessment for MSP Support

### High Complexity (Requires Deep Expertise)

1. **Salesforce ↔ Oracle Integration**
   - Dense integration cluster with multiple data flows
   - CPQ, CLM, and standard CRM all interconnected
   - Customer Master, Item Master, Quote/Contract synchronization

2. **RecVue Billing Hub**
   - Sits between Salesforce and Oracle ERP
   - Handles complex revenue recognition/subscription billing
   - Multiple integration points to Receivables, Projects, GL

3. **Oracle Fusion Suite (SCM + ERP + CX + EPM)**
   - All four clouds interconnected
   - Internal module-to-module integrations
   - "Automated PO Creation" between Order Management and Procurement

### Medium Complexity

4. **Banking/Payment Cluster**
   - Bank, SnapPay, Billtrust all connected
   - BAI2 format for bank statements
   - APO (Accounts Payable Outsourcing?) integration

5. **Data Pipeline**
   - Snowflake as central warehouse
   - Multiple BI tools (Tableau, SplashBI)
   - Rivery for ETL orchestration

### Lower Complexity (Standard Integrations)

6. **HR/Payroll** - ADP → Oracle ERP
7. **Expense Management** - Emburse, Corporate Travel → Payables
8. **Tax** - Avalara → RecVue/ERP
9. **Identity** - AD → Oracle Cloud

### Risk Areas for MSP

| Risk | Description |
|------|-------------|
| **Legacy Java App** | Material Voucher application - custom code, unknown hosting |
| **Multi-CRM** | Oracle CRM on Demand + Nextstar + Salesforce suggests migration complexity |
| **Sync-Heavy** | Majority synchronous integrations = high uptime requirements |
| **RecVue Dependency** | If RecVue fails, billing/revenue recognition stops |
| **Integration Density** | 50+ integration points visible - high change management burden |

---

## Questions for RFP Clarification

Based on this architecture, key questions for McGrath:

1. **Material Voucher App**: Where is this hosted? Who supports it? Is it in scope for MSP?

2. **Oracle CRM on Demand / Nextstar**: Are these being retired, or will MSP need to support all three CRM platforms?

3. **RecVue**: Is this managed by McGrath, a third party, or in scope for MSP? What's the SLA?

4. **Integration Monitoring**: Is there existing middleware/iPaaS (MuleSoft, Boomi, OIC) or are these point-to-point?

5. **Snowflake/Analytics**: Who owns the data pipeline? Is Rivery managed separately?

6. **Banking Integrations**: Are bank connections through a treasury management system or direct?

---

## Document History

| Date | Version | Notes |
|------|---------|-------|
| 2026-02-24 | 1.0 | Initial extraction via Gemini 3.1 Pro and Gemini 3 Thinking |
| 2026-02-24 | 1.1 | Human verification of key elements, synthesis of both AI outputs |

---

*This document represents McGrath RentCorp's FUTURE STATE architecture after NextGen implementation, not current state.*
