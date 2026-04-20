An analysis of the provided page image is presented in three sections: Markdown Content, ASCII Layout, and Visual Elements.

## Markdown Content

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

## ASCII Layout

```
+-------------------------------------------------------------------------------------------------+
| [Numbered List Item 4: Build metadata...]                                                       |
|                                                                                                 |
|   +-----------------------------------------------------------------------------------------+   |
|   |                                                                                         |   |
|   |                                [Screenshot: Build Portal Table]                         |   |
|   |                                                                                         |   |
|   +-----------------------------------------------------------------------------------------+   |
|                                                                                                 |
| [Numbered List Item 5: Logs are stored on NFS...]                                               |
|                                                                                                 |
|   +-----------------------------------------------------------------------------------------+   |
|   |                                                                                         |   |
|   |                                                                                         |   |
|   |                                [Screenshot: Terminal Window]                            |   |
|   |                                                                                         |   |
|   |                                                                                         |   |
|   |                                                                                         |   |
|   +-----------------------------------------------------------------------------------------+   |
|                                                                                                 |
| [Numbered List Item 6: Work by Justin]                                                          |
|   [Sub-list items a, b, c, d]                                                                   |
|                                                                                                 |
| [Numbered List Item 7: Jenkins jobs...]                                                         |
|                                                                                                 |
|                                                                                                 |
|                                                                                                 |
|                                                                         [Footer: Cisco Conf.]   |
+-------------------------------------------------------------------------------------------------+
```

## Visual Elements

There are two screenshots on this page.

1.  **Build Portal Screenshot**
    -   **Type**: Screenshot of a web-based table.
    -   **Position on page**: Top-center, located under heading 4.
    -   **Description**: This is a table from a build portal, showing the status of five recent software builds. The table has six columns: "Build No", "Build Date", "Expire By", "LOC (Ins/Mod/Del)", "Status/# Sanity", and "Comments". The status column uses icons: a green checkmark for "Pass", a blue checkmark for "Pass" with a number, and a red circle with an exclamation mark for "Fail". Four builds have passed and one has failed.
    -   **Text Content**: The complete text content of the table is transcribed in the Markdown section above.

2.  **Terminal Screenshot**
    -   **Type**: Screenshot of a command-line interface (CLI) or terminal window.
    -   **Position on page**: Center, located under heading 5.
    -   **Description**: The screenshot shows a user, `justijos`, interacting with a Linux/Unix-like system via a terminal. The user navigates through directories and lists their contents to access build logs. The image is split into multiple panes, showing different commands and outputs. The user lists directories, changes into the `nexus/logs` directory, and then into a specific build log directory (`COV_10_6_2_IMG9_0_229`). Inside this directory, a wide variety of log files, JSON files, and other build artifacts are listed.
    -   **Text Content (Partial Transcription)**:
        -   **User and Host**: `justijos@sjc-ads-6791`
        -   **Commands shown**: `cd nexus/`, `ls`, `cd logs/`, `cd COV_10_6_2_IMG9_0_229`, `ls -altr error.log*`
        -   **File/Directory names visible**: `eng`, `nexus`, `build`, `logs`, `config.files`, `all_image_compare.log`, `build.log.html`, `cbuild_sanity_submission.log`, `commits.dir`, `error.log.images^final^bazel^linecardimages`, `error.log.images^final^nxos64`, `standalone_compiler_warnings.json`, `post_build_activities.log`.