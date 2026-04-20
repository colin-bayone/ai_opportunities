# Page 5

4.  Build metadata ( build number, status, ..) is stored in mySQL database.
    -   Below is the build portal screenshot

| Build No | Build Date | Expire By | LOC (Ins/Mod/Del) | Status/# Sanity | Comments |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ▶ **10.7(0)IDV9(0.205)**<br>(5bac722fc9e580f90448b2e7) | 04/08/2026 10:40 | 04/23/2026 14:56 | 9770 / 0 / 2286 | ✅ Pass | Build successful (divvenka) |
| ▶ **10.7(0)IDV9(0.204)**<br>(f1a36ff5acec9f3026eaf8867) | 04/07/2026 19:32 | 04/27/2026 23:30 | 3109 / 0 / 1671 | 🛂 Pass (42) | Codenet Label (psadhukh) |
| ▶ **10.7(0)IDV9(0.203)**<br>(dd01a4baf87491ea0da198df) | 04/07/2026 11:07 | 04/22/2026 14:52 | 38860 / 0 / 11639 | ✅ Pass (2) | Build successful (divvenka) |
| ▶ **10.7(0)IDV9(0.202)**<br>(442feb2f46d7328401594acf) | 04/06/2026 19:34 | 05/06/2026 23:16 | 33 / 0 / 36 | ✅ Pass (2) | QA Label (psadhukh) |
| ▶ **10.7(0)IDV9(0.201)**<br>(5efb3c5bbbbc515162b05fda) | 04/06/2026 15:21 | Tree Deleted | 1906387 / 0 / 689105 | ❗ Fail | Build failed (psadhukh) |

<br>

5.  Logs are stored on NFS accessible via ADS machines.

6.  Work by Justin
    a.  Wrote Python script that extracts errors and passes them to a large language model (LLM) for analysis.
    b.  The LLM suggests and applies code fixes automatically to a separate workspace.
    c.  After AI patching, a build verification step ensures the fixes resolve the errors.
    d.  There is potential to automate pull request creation for verified fixes to official builds.

7.  Jenkins jobs initiate builds, and logs are stored temporarily. Failed build logs remain accessible for a few days, while official nightly build logs are retained for years.

<br>
<br>
<br>
Cisco Confidential

---
*Source: Build_log_analysis_upadtes_04102026.pdf, Page 5 of 6*
