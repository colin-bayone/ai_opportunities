# McGrath RentCorp - Desired State Architecture Summary

**Source:** MGRC Environment tab (embedded Visio), extracted from screenshot
**Type:** Future State Integration Architecture

---

## Legend

| Outline Color | Meaning |
|---------------|---------|
| Blue | Synchronous integration |
| Amber/Orange | Asynchronous integration |

---

## Core Oracle Cloud Modules

### Oracle Cloud SCM (Supply Chain Management)
- Demand & Supply
- Maintenance
- Inventory
- Procurement
- Order Management
- Install Base
- Maintenance Cloud
- Cost Management
- Product Data Hub
- Supplier Management
- Supplier Portal

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

## External Systems & Integrations

### CRM & Sales
| System | Integration Type | Purpose |
|--------|------------------|---------|
| Salesforce | Sync/Async | CRM, CPQ, CLM |
| Pardot | Sync | Marketing automation |
| DocuSign | Async | Contract creation & revision |
| Xactly | Sync | Sales compensation |
| Zilliant | Async | Quote contract information |
| Dun & Bradstreet | Sync | D&B data |
| Oracle CRM on Demand | Async | Legacy CRM |

### Financial & Billing
| System | Integration Type | Purpose |
|--------|------------------|---------|
| RecVue+ | Async | Revenue management |
| Avalara | Async | Tax calculation |
| Billtrust | Async | Invoice PDFs, Pay Bills |
| SnapPay | Async | Payments |
| Bank | Async | Bank & Debit/Credit Line (APO) |

### Data & Analytics
| System | Integration Type | Purpose |
|--------|------------------|---------|
| Snowflake | Extract | Data warehouse |
| Tableau | Sync | Equipment setup, BI |
| Rivery | Sync | ETL/Data pipeline |
| SplashBI | Sync | BI reporting |

### HR & Operations
| System | Integration Type | Purpose |
|--------|------------------|---------|
| ADP | Async | Payroll/HR |
| AD (Active Directory) | Sync | Identity management |
| Emburse | Async | Expense management |
| Corporate Travel Management | Async | Travel |
| EHS | Async | Environment, Health, Safety |
| OC Tanner | Async | Employee recognition |

### Supply Chain & Vendors
| System | Integration Type | Purpose |
|--------|------------------|---------|
| Intellinum | Async | Scan & labeling, SO/GO, Purchase Orders |
| JONES | Async | OCI - New Vendor Data, Compliance Status |
| Oracle Aconex | Async | Project management |

### Custom Applications
| System | Purpose |
|--------|---------|
| Material Voucher Issue (Application) | Internal voucher system |
| Nextiva | Communication |

---

## Key Integration Flows

### Quote-to-Cash
1. Salesforce (CPQ) → DocuSign (contracts) → Oracle ERP (billing)
2. Zilliant → Quote Contract Information → Salesforce
3. RecVue+ → Oracle ERP (Receivables)

### Procure-to-Pay
1. Oracle SCM (Procurement) → Supplier Portal → Suppliers
2. JONES → OCI Vendor Data → Oracle SCM
3. Oracle ERP (Payables) → Bank

### Financial Close
1. Oracle ERP (GL, Receivables, Payables) → Oracle EPM (Enterprise Planning)
2. Oracle EPM (Account Reconciliation) → Narrative Reporting

### Data & Reporting
1. Oracle Cloud → Snowflake (Extract)
2. Snowflake → Tableau / SplashBI

---

## Integration ID Ranges (Visible in Diagram)

| Range | Oracle Module |
|-------|---------------|
| INT 1xx | External system integrations |
| INT 2xx | Oracle Cloud SCM modules |
| INT 3xx | Oracle Cloud ERP modules |
| INT 4xx | Oracle Cloud CX modules |
| INT 5xx | Oracle Cloud EPM modules |

---

## Complexity Assessment

**High Complexity Areas:**
- Salesforce integration (CPQ, CLM, multiple connected systems)
- Oracle Fusion suite (SCM, ERP, CX, EPM - all interconnected)
- Financial integrations (RecVue, Avalara, Billtrust, Bank)

**Medium Complexity:**
- Data pipeline (Snowflake, Rivery, Tableau)
- HR/Operations (ADP, Emburse, etc.)

**Lower Complexity:**
- Single-purpose integrations (OC Tanner, EHS, Corporate Travel)

---

## Notes for RFP Response

1. **This is FUTURE STATE** - not current state
2. Integration volume is significant (50+ integrations visible)
3. Mix of synchronous and asynchronous patterns
4. Heavy Oracle Cloud footprint (SCM, ERP, CX, EPM)
5. Multiple third-party systems requiring ongoing support
6. NextGen Release 1 mentioned - indicates active development/migration
