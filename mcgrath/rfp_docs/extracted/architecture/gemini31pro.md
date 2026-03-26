# McGrath RentCorp - Future State Architecture Analysis

## 1. External Systems Inventory

Based on the visual legend (Blue = Synchronous, Amber = Asynchronous). Boxes with black or undefined outlines are noted as such.

| System Name | Logo/Icon? | Connected To | Integration Type (Legend) | Data Flow Description (if labeled) |
| --- | --- | --- | --- | --- |
| **Snowflake** | Yes | Tableau, Salesforce | Blue (Sync) | "Extract" (to Tableau), "Sync" (from Salesforce) |
| **Tableau** | Yes | Snowflake, Oracle SCM | Blue (Sync) | "Equipment Status" (from SCM) |
| **Rivery + SplashBI** | Yes | Snowflake, Salesforce | Blue (Sync) | "Sync" (to Salesforce) |
| **Xactly** | Yes | Salesforce | Amber (Async) | "Sales Compensation" |
| **Dun & Bradstreet** | Yes | Salesforce | None (Text only) | "Credit Check" |
| **DocuSign** | Yes | Salesforce | Blue (Sync) | "Contact Creation & Revision" |
| **Zilliant** | Yes | Salesforce | Amber (Async) | "Quote/Contract Information" |
| **Oracle Aconex** | Yes | Oracle SCM | Amber (Async) | N/A |
| **Emburse** | No | Oracle ERP (Payables) | Black Outline | N/A |
| **Corporate Travel Mgmt** | No | Oracle ERP (Payables) | Black Outline | N/A |
| **EHS** | No | Oracle ERP (Payables) | Black Outline | N/A |
| **OC Tanner** | No | Oracle ERP (Payables) | Black Outline | N/A |
| **Intellinum** | Yes | Oracle SCM | Blue (Sync) | "Scan & Labelling Solution", "Purchase Orders" |
| **Material Voucher** | No | Oracle SCM (Inventory) | Yellow Box | "Material Voucher (Java Application)" |
| **JONES** | Yes | Oracle SCM (Supplier Mgmt) | Black Outline | "COI - New Vendor Data", "COI - Compliance Status" |
| **Salesforce** | Yes | Oracle SCM, RecVue, Various | Blue (Sync) | "Project Creation", "Quote/Contract Information" |
| **Pardot** | No | Inside Salesforce | N/A | Sub-module of Salesforce |
| **Salesforce CPQ** | No | Inside Salesforce | N/A | Sub-module of Salesforce |
| **Hub of Customer Information** | Yes | Salesforce, Oracle | Orange Dashed | "Quotes & Contracts", "Quote Request & PO update Item Master" |
| **RecVue** | Yes | Oracle SCM/ERP, Salesforce | Blue (Sync) | "Quotes & Contracts" |
| **Oracle CRM On Demand** | Yes | Salesforce | None (Logo only) | "Customer Master" |
| **NexStar** | Yes | Oracle ERP | Blue (Sync) | N/A |
| **XE** | Yes | Oracle ERP | Blue (Sync) | N/A |
| **Avalara** | Yes | Oracle ERP, RecVue | Amber (Async) | N/A |
| **Billtrust** | Yes | Oracle ERP (Receivables) | Blue (Sync) | "Invoice PDFs" |
| **SnapPay** | Yes | Oracle ERP (Receivables) | Blue (Sync) | N/A |
| **Bank (APO)** | Yes | Oracle ERP (Cash Mgmt) | Blue (Sync) | "Bank & Bottom Line (APO)" |
| **ADP** | Yes | Oracle ERP (GL) | Blue (Sync) | N/A |
| **AD (Active Directory)** | No | Oracle Cloud EPM | Blue (Sync) | N/A |

## 2. Oracle Cloud Module Details

### Oracle Cloud SCM (Supply Chain Management)

* Demand & Supply
* Maintenance
* Inventory
* Procurement
* Order Management
* Product Data Hub
* Supplier Management
* Supplier Portal
* Install Base
* Maintenance Cloud
* Cost Management
* Employee Data

### Oracle Cloud ERP (Enterprise Resource Planning)

* General Ledger
* Project Management
* Fixed Assets
* Payables
* Receivables
* Advanced Collections
* Cash Management
* Reporting & Analytics

### Oracle Cloud CX (Customer Experience)

* Cloud Service
* Field Service Management

### Oracle Cloud EPM (Enterprise Performance Management)

* Enterprise Planning
* Account Reconciliation
* Narrative Reporting

## 3. Integration Map

IDs are listed only where the number is legible.

| INT ID | From System/Module | To System/Module | Sync/Async |
| --- | --- | --- | --- |
| **INT104** | Emburse | Payables (ERP) | Sync (via line path) |
| **INT112** | Corporate Travel Mgmt | Payables (ERP) | Sync |
| **INT106** | EHS | Payables (ERP) | Sync |
| **INT107** | OC Tanner | Payables (ERP) | Sync |
| **INT200** | Intellinum | Inventory (SCM) | Sync |
| **INT016** | Material Voucher | Inventory (SCM) | Sync |
| **INT154** | Zilliant | Salesforce | Async (Amber System) |
| **INT125 C** | Oracle Aconex | Project Mgmt (ERP) | Async |
| **INT120** | Oracle Aconex | Project Mgmt (ERP) | Async |
| **INT201** | Demand & Supply | Maintenance | Internal SCM |
| **INT029** | Maintenance | Inventory | Internal SCM |
| **INT007** | Inventory | Cost Management | Internal SCM |
| **INT203** | Inventory | Cost Management | Internal SCM |
| **INT202** | Order Management | Receivables (ERP) | Internal |
| **INT124** | Cost Management | General Ledger (ERP) | Internal |
| **INT128** | General Ledger | Reporting & Analytics | Internal ERP |
| **INT139** | Fixed Assets | General Ledger | Internal ERP |
| **INT153** | Payables | General Ledger | Internal ERP |
| **INT069-B** | Payables | General Ledger | Internal ERP |
| **INT073** | Payables | General Ledger | Internal ERP |
| **INT102** | Receivables | General Ledger | Internal ERP |
| **INT132** | Advanced Collections | Receivables | Internal ERP |
| **INT101** | Cash Management | General Ledger | Internal ERP |
| **INT048** | Oracle Cloud EPM | General Ledger | Internal |
| **INT149** | AD | Oracle Cloud EPM | Sync |
| **INT108** | ADP | General Ledger | Sync |
| **INT110** | ADP | General Ledger | Sync |
| **INT053** | Bank (APO) | Cash Management | Sync |
| **INT013** | Bank (APO) | Cash Management | Sync |
| **INT060** | Bank (APO) | Cash Management | Sync |
| **INT126** | Bank (APO) | Cash Management | Sync |
| **INT032** | Billtrust | Receivables | Sync |
| **INT109-I** | Billtrust | Receivables | Sync |
| **INT109-II** | Billtrust | Receivables | Sync |
| **INT070** | Avalara | Receivables | Async |
| **INT163** | NexStar | Order Management | Sync |
| **INT161** | NexStar | Receivables | Sync |
| **INT066** | Field Service Mgmt | Payables | Internal |
| **INT076** | Avalara | RecVue | Async |
| **INT052** | RecVue | General Ledger | Sync |
| **INT020** | RecVue | Receivables | Sync |
| **INT019** | RecVue | Receivables | Sync |
| **INT021** | RecVue | Receivables | Sync |
| **INT030** | RecVue | Project Management | Sync |
| **INT150** | RecVue | Project Management | Sync |
| **INT152** | RecVue | Project Management | Sync |
| **INT100** | RecVue | Contract/Order? | Sync |
| **INT204** | RecVue | Contract/Order? | Sync |
| **INT055** | RecVue | Order Management | Sync |
| **INT117** | Salesforce | Product Data Hub | Sync |
| **INT119** | Salesforce | Product Data Hub | Sync |
| **INT122** | Salesforce | Product Data Hub | Sync |
| **INT116** | Salesforce | Product Data Hub | Sync |
| **INT121A** | Salesforce | Order Management | Sync |
| **INT121B** | Salesforce | Order Management | Sync |
| **INT121E** | Salesforce | Order Management | Sync |
| **INT155** | Salesforce | Order Management | Sync |

## 4. Data Flow Labels

| Label Text | From | To |
| --- | --- | --- |
| **Sync** | Snowflake | Salesforce |
| **Extract** | Snowflake | Tableau |
| **Equipment Status** | Tableau | Oracle SCM (Maintenance) |
| **Sales Compensation** | Xactly | Salesforce |
| **Credit Check** | Dun & Bradstreet | Salesforce |
| **Contact Creation & Revision** | DocuSign | Salesforce |
| **Quote/Contract Information** | Zilliant | Salesforce |
| **Quote/Contract Information** | Salesforce | Order Management (SCM) |
| **Project Creation** | Salesforce | Project Management (ERP) |
| **Quotes & Contracts** | Salesforce | RecVue |
| **Customer Master** | Oracle CRM On Demand | Salesforce |
| **Quote Request & PO update Item Master** | Hub of Customer Info | Salesforce/Oracle |
| **Invoice PDFs** | Billtrust | Receivables |
| **Bank & Bottom Line (APO)** | Bank | Cash Management |
| **Scan & Labelling Solution** | Intellinum | Oracle SCM |
| **Purchase Orders** | Intellinum | Oracle SCM |
| **COI - New Vendor Data** | JONES | Supplier Management |
| **COI - Compliance Status** | JONES | Supplier Management |
| **Automated PO Creation** | Order Management | Procurement |

## 5. Visual Organization

* **Central Architecture:** The core is "Oracle Cloud Applications," a large container broken into four vertical/functional swimlanes: SCM, ERP, CX, and EPM.
* **Color Coding (Boxes):**
* **Blue Outline:** Indicates Synchronous systems (e.g., Salesforce, RecVue, Banks).
* **Amber Outline:** Indicates Asynchronous systems (e.g., Avalara, Aconex).
* **Teal/Green Fill:** Used for the internal Oracle modules.


* **Integration Density:**
* **High Density:** Between Salesforce and Oracle SCM (Product Data Hub/Order Management).
* **High Density:** Between RecVue and Oracle ERP (Receivables/Projects).


* **Logical Grouping:**
* **Financials/Banking:** Grouped on the right side connecting to ERP.
* **Sales/CRM:** Grouped at the top connecting to SCM and RecVue.
* **HR/Identity:** Far right (ADP, AD).
* **Operations/Field:** Left side (Intellinum, Jones) connecting to SCM.



## 6. Key Observations

* **RecVue Complexity:** RecVue is a major integration hub, not just a peripheral system. It has at least 9 distinct integration points (INTs) connecting to both Project Management and Receivables, indicating it likely handles complex billing/revenue recognition logic outside of standard Oracle ERP.
* **Salesforce as Front-End:** Salesforce is heavily integrated with Oracle SCM (specifically Product Data Hub and Order Management), suggesting a "Quote-to-Cash" flow where Salesforce handles the quote and Oracle/RecVue handles the execution and billing.
* **Custom Java App:** There is a "Material Voucher (Java Application)" connected to Inventory. This implies legacy debt or a custom solution that the MSP may need to support or interface with.
* **Multiple Sync Protocols:** The architecture relies heavily on Synchronous (Blue) connections, which imposes stricter uptime and latency requirements on the MSP than an asynchronous batch-based architecture.
* **Master Data Management:** There is a specific icon "Hub of Customer Information" with an orange dashed line, suggesting a logical master data layer for customer attributes spanning Salesforce and Oracle.

## 7. Unclear/Unreadable Elements

* **INT IDs near Billtrust:** Specifically `INT109-B` and `INT109-NB` (or similar) are difficult to read with 100% certainty.
* **INT IDs inside RecVue:** The cluster of IDs (`INT020`, `INT019`, `INT021`) is very tight; directionality is clear, but exact number confirmation is difficult.
* **Hub of Customer Information:** The text "Hub of Customer Information" is accompanied by an icon and an orange dashed line connecting to a generic "Hub" icon near Salesforce. The exact technology or system hosting this "Hub" is not explicitly named (e.g., is it Informatica? Oracle MDM? Just a logical concept?).
* **"Material Voucher":** The label says "Material Voucher (Java Application)" but does not give a system name (e.g., is it hosted on OCI? On-prem?).