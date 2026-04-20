## Markdown Content
iii. This PR has the changes for the AI triage tool https://wwwwin-github.cisco.com/DCN/tools/pull/642
iv. 

**4. Training course**
    a. Link - https://cisco.edcast.com/insights/ECL-529e2871-ff1f-4c2b-8855-608fa4269ba8
    b. Status - Error: You do not have permission to access this Content. Please reach out to Administrator. - Raised a request with support.

**5. Build portal**
    a. Link - https://wwwwin-ins-sw-web.cisco.com/node/branch/build

**6. Appstore**
    a. Link - https://appstore.cisco.com/

**7. DeepSight**
    a. Link - https://deepsight.cisco.com/

**Meetings**

1. Build log analysis intro with Justin (04/08/2026)
   a. webexteams://im?space=8fcc5f70-2dcc-11f1-a1fc-a98bb153865a&message=7726afb0-3453-11f1-bacb-858bcec24e03
2. Build log analysis with Divakar and Justin (04/09/2026)
   a. webexteams://im?space=8fcc5f70-2dcc-11f1-a1fc-a98bb153865a&message=c45958f0-3494-11f1-a96b-8f3ce65ee974

**Build log analysis understanding after call with Justin**

1. There are official nightly builds and user builds, with logs stored on NFS accessible via ADS machines. (NFS location: /auto/ins-bld-tools/branches/nx_main/nexus/togs/)
2. The official builds primarily use two branches, NX main and NX dev, with different build systems (Gmake and Bazel respectively)
3. Uses two build automation tools:
   a. Gmake
      i. Used to build nx_main repo.
      ii. Moving away from Gmake to Bazel
      iii. Old repos are built using Gmake
   b. Bazel
      i. Used to build nx_dev repo.

Cisco Confidential

## ASCII Layout
```
+------------------------------------------------------------------------------+
|                                                                              |
| [OUTLINE/LIST CONTENT]                                                       |
|                                                                              |
| iii. This PR has the changes for the AI triage tool...                       |
| iv.                                                                          |
|                                                                              |
| 4. Training course                                                           |
|    a. Link - ...                                                             |
|    b. Status - Error: ...                                                    |
|                                                                              |
| 5. Build portal                                                              |
|    a. Link - ...                                                             |
|                                                                              |
| 6. Appstore                                                                  |
|    a. Link - ...                                                             |
|                                                                              |
| 7. DeepSight                                                                 |
|    a. Link - ...                                                             |
|                                                                              |
| [HEADING: Meetings]                                                          |
|                                                                              |
| 1. Build log analysis intro with Justin...                                   |
|    a. webexteams://...                                                       |
| 2. Build log analysis with Divakar and Justin...                             |
|    a. webexteams://...                                                       |
|                                                                              |
| [HEADING: Build log analysis understanding after call with Justin]           |
|                                                                              |
| 1. There are official nightly builds and user builds...                      |
| 2. The official builds primarily use two branches...                         |
| 3. Uses two build automation tools:                                          |
|    a. Gmake                                                                  |
|       i. Used to build...                                                    |
|       ...                                                                    |
|                                                                              |
|                                                                              |
|                                                                              |
|                                                      [FOOTER]                |
|                                                      Cisco Confidential      |
+------------------------------------------------------------------------------+
```

## Visual Elements
There are no visual elements such as images, charts, diagrams, or logos on this page. The entire page consists of structured text.