# Neha Follow-Up Email v6

---

Thanks for walking us through the Cognos workflow today. Understanding the difference between reports that use the Framework Model versus reports with embedded SQL was really helpful for scoping the demo.

For the demo, we'll take one of your Cognos reports and walk through the full conversion: parsing the report definition to understand what it's referencing, then producing output that maps to your Databricks environment. If the report uses the Framework Model, we'll show what needs to change to point it to Databricks. If it has embedded SQL, we'll show the conversion to Databricks-compatible SQL.

To put this together, we need two things from your side:
1. A Cognos report XML export from the Finance folder, the full export from Report Studio
2. The target Databricks schema, the catalog and table structure, so we can wire up the mapping on our end

Once we have those, we can get the demo on the calendar. Let me know if you have questions about what to export.

Best,
Neha
