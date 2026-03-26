This analysis provides a comprehensive extraction of the McGrath RentCorp Future State Architecture based on the provided diagram.

# McGrath RentCorp - Future State Architecture Analysis

## 1. External Systems Inventory

| System Name | Logo/Icon Present? | Connected To | Integration Type (Sync/Async) | Data Flow Description (if labeled) |
| --- | --- | --- | --- | --- |
| **Salesforce / Pardot / Salesforce CPQ** | Yes | SCM, ERP, CX, Xactly, D&B, Zilliant, Docusign, Recvue, Nexstar | **Synchronous** (Blue Outline) | Quotes & Contracts, Item Master, Credit Check, Sales Compensation |
| **Snowflake** | Yes | SplashBI / Rivery | **Asynchronous** (Amber Outline) | Extract |
| **Tableau** | Yes | Salesforce / SplashBI | **Asynchronous** (Amber Outline) | Equipment Status |
| **Rivery + SplashBI** | Yes | Snowflake, Tableau, Salesforce | **Asynchronous** (Amber Outline) | Sync |
| **Xactly** | Yes | Salesforce | **Asynchronous** (Amber Outline) | Sales Compensation |
| **Dun & Bradstreet** | Yes | Salesforce CPQ | **Synchronous** (Blue Outline) | Credit Check |
| **Docusign** | Yes | Salesforce CPQ | **Synchronous** (Blue Outline) | Contract Creation & Revision |
| **Zilliant** | Yes | Salesforce CPQ | **Synchronous** (Blue Outline) | Quote / Contract Information |
| **Oracle Aconex** | Yes | Oracle Cloud SCM | **Asynchronous** (Amber Outline) | Project Creation (unclear label) |
| **Recvue** | Yes | Salesforce, ERP, CX, Avalara, Billtrust | **Synchronous** (Blue Outline) | Revenue/Billing data flows |
| **Nexstar (Oracle CRM on Demand)** | Yes | Salesforce, ERP | **Synchronous** (Blue Outline) | Customer Master |
| **Avalara** | Yes | Recvue | **Synchronous** (Blue Outline) | Tax Calculation |
| **XE** | Yes | Oracle Cloud ERP | **Synchronous** (Blue Outline) | Currency/Exchange rates |
| **Billtrust** | Yes | Recvue | **Synchronous** (Blue Outline) | Invoice PDFs |
| **Snap Pay** | Yes | Bank | **Synchronous** (Blue Outline) | Payment Processing |
| **Bank** | Yes | ERP, Snap Pay, ADP | **Synchronous** (Blue Outline) | Bank & Statement (BAI2) |
| **ADP** | Yes | AD, Bank, ERP | **Asynchronous** (Amber Outline) | Payroll/HR Data |
| **AD (Active Directory)** | Yes | ADP, Oracle Cloud Applications | **Synchronous** (Blue Outline) | Identity Management |
| **Emburse** | Yes | Oracle Cloud ERP | **Synchronous** (Blue Outline) | Expense Data (INT 104) |
| **Corporate Travel Management** | Yes | Oracle Cloud ERP | **Synchronous** (Blue Outline) | Travel Data (INT 112) |
| **EHS** | Yes | Oracle Cloud ERP | **Synchronous** (Blue Outline) | Environmental Health & Safety (INT 106) |
| **OC Tanner** | Yes | Oracle Cloud ERP | **Synchronous** (Blue Outline) | Employee Recognition (INT 107) |
| **Intellinum** | Yes | Oracle Cloud SCM | **Synchronous** (Blue Outline) | Scan & Labeling, Purchase Orders |
| **Jones** | No (Text Only) | Oracle Cloud SCM | **Synchronous** (Blue Line) | COI - New Vendor / Compliance Status |
| **Material Voucher (Java Application)** | No (Text Only) | Oracle Cloud SCM | **Synchronous** (Blue Line) | Material Voucher data |

---

## 2. Oracle Cloud Module Details

### Oracle Cloud SCM

* Demand & Supply
* Inventory
* Procurement
* Supplier Management
* Supplier Portal
* Employee Data
* Install Base
* Order Management
* Maintenance Cloud
* Cost Management
* Maintenance
* Product Data Hub

### Oracle Cloud ERP

* General Ledger
* Project Management
* Fixed Assets
* Payables
* Receivables
* Advanced Collections
* Cash Management
* Reporting & Analytics

### Oracle Cloud CX

* Cloud Service
* Field Service Management

### Oracle Cloud EPM

* Enterprise Planning
* Account Reconciliation
* Narrative Reporting

---

## 3. Integration Map

| INT ID | From System | To System | Sync/Async | Label/Description (if any) |
| --- | --- | --- | --- | --- |
| **INT 104** | Emburse | ERP | Sync | Expense Integration |
| **INT 112** | Corp Travel Mgmt | ERP | Sync | Travel Integration |
| **INT 106** | EHS | ERP | Sync | Health & Safety Integration |
| **INT 107** | OC Tanner | ERP | Sync | Rewards Integration |
| **INT 209** | Salesforce CPQ | SCM (Demand & Supply) | Sync | Unlabeled |
| **INT 117** | Salesforce CPQ | ERP (Receivables/Payables) | Sync | Multiple flows (117, 121B, 121E, 116) |
| **INT 154** | Salesforce | Xactly | Async | Sales Compensation |
| **INT 126 C** | Salesforce | ERP | Sync | Unlabeled |
| **INT 120** | Salesforce | ERP | Sync | Unlabeled |
| **INT 200** | Intellinum | SCM | Sync | Scan & Labeling |
| **INT 102** | SCM | ERP | Sync | Internal Oracle Cloud flow |
| **INT 121** | ERP (Internal) | Reporting & Analytics | Sync | Internal ERP flow |
| **INT 131** | ERP (Internal) | Reporting & Analytics | Sync | Internal ERP flow |
| **INT 132** | ERP (Internal) | Reporting & Analytics | Sync | Internal ERP flow |
| **INT 122** | SCM | ERP | Sync | Unlabeled |
| **INT 124** | SCM | ERP | Sync | Unlabeled |
| **INT 155** | SCM | ERP | Sync | Unlabeled |
| **INT 023** | SCM | ERP | Sync | Unlabeled |
| **INT 022** | SCM | ERP | Sync | Unlabeled |
| **INT 110** | ADP | AD | Async | Identity Sync |
| **INT 109** | ADP | ERP | Async | Payroll/HR Integration |
| **INT 105** | ADP | Bank | Async | Direct Deposit/Funding |
| **INT 128** | Billtrust | Recvue | Sync | Invoice PDFs |
| **INT 151** | Avalara | Recvue | Sync | Tax Integration |
| **INT 113** | Recvue | ERP | Sync | Revenue/Billing Integration |
| **INT 048** | EPM | ERP | Sync | Planning/Financial Close |

---

## 4. Data Flow Labels

| Label Text | From | To |
| --- | --- | --- |
| **Sales Compensation** | Salesforce | Xactly |
| **Credit Check** | D&B | Salesforce CPQ |
| **Contract Creation & Revision** | Salesforce CPQ | Docusign |
| **Quote/Contract Information** | Zilliant | Salesforce CPQ |
| **Scan & Labeling Solution** | Intellinum | Oracle Cloud SCM |
| **Purchase Orders** | Intellinum | Oracle Cloud SCM |
| **Material Voucher (Java Application)** | Java App | Oracle Cloud SCM |
| **COI - New Vendor Data** | Jones | SCM (Supplier Management) |
| **COI - Compliance Status** | Jones | SCM (Supplier Management) |
| **Animated PO Creation** | SCM (Order Management) | Product Data Hub |
| **Project Creation** | Oracle Aconex | SCM (Maintenance) |
| **Customer Master** | Salesforce | Nexstar (Oracle CRM on Demand) |
| **Quotes & Contracts** | Salesforce | Nexstar (Oracle CRM on Demand) |
| **Quote Request & PO update** | Salesforce | Nexstar (Oracle CRM on Demand) |
| **Item Master** | Salesforce | Nexstar (Oracle CRM on Demand) |
| **Invoice PDFs** | Billtrust | Salesforce |
| **Bank & Statement (BAI2)** | Bank | ERP (Cash Management) |
| **Equipment Status** | Tableau | Salesforce |
| **Extract** | Snowflake | Tableau |
| **Sync** | Rivery + SplashBI | Snowflake / Salesforce |

---

## 5. Visual Organization

* **Primary Container:** A large, light-red shaded box encompasses the entire **Oracle Cloud Applications** suite.
* **Functional Groupings:** Inside the Oracle container, modules are grouped into colored sub-boxes:
* **Tan:** Oracle Cloud SCM (Largest footprint)
* **Green:** Oracle Cloud ERP (Central financial hub)
* **Blue:** Oracle Cloud CX
* **Pink:** Oracle Cloud EPM


* **Directional Flow:** The diagram generally flows from Customer/Front-end (Top/Left) to Financials/Back-end (Center) to Reporting/Analytics (Top/Right).
* **External Periphery:** High-level analytics and sales tools are at the top; HR/Payroll/Banking are on the right; specific SCM edge-cases (Jones, Intellinum) are on the left.

---

## 6. Key Observations

* **Salesforce as the Front-End Hub:** Salesforce (including CPQ and Pardot) acts as the primary "Front Office," handling complex quoting and contracting before passing data to Oracle.
* **High Synchronous Dependency:** The vast majority of integrations are Blue (Synchronous). This indicates a "Real-Time" enterprise requirement where system downtime in one area (like Recvue or Avalara) could immediately halt business processes.
* **Hybrid Oracle Strategy:** The presence of **Nexstar (Oracle CRM on Demand)** alongside **Salesforce** and **Oracle Cloud CX** suggests a complex migration or a multi-CRM strategy for different business units.
* **Recvue for Billing Complexity:** The use of Recvue between Salesforce and Oracle ERP suggests high-volume or highly complex subscription/usage-based billing that standard Oracle ERP modules might not be handling.
* **Support Risk:** The density of "INT" IDs between SCM and ERP (INT 122, 124, 155, 023, 022) indicates a highly customized or complex "Lead-to-Cash" and "Procure-to-Pay" landscape.

---

## 7. Unclear/Unreadable Elements

* **INT IDs on Bank lines:** There is a cluster of IDs (including 152, 117, 114, 115, 120) near Snap Pay and the Bank that are very small and overlap, making exact "From/To" mapping difficult for those specific lines.
* **Project Creation Label:** The line from Oracle Aconex to SCM is labeled, but the text "Project Creation" is partially obscured by the boundary line.
* **Salesforce CPQ to ERP line (INT 117/121):** There are 4-5 IDs listed on a single line path, making it unclear if these are separate sub-processes or sequence steps.
* **SplashBI Connection:** The line between SplashBI and Snowflake is labeled "Sync," but the arrow direction is bi-directional and very small.

Would you like me to draft a set of clarifying questions for the RFP based on these identified complexities?