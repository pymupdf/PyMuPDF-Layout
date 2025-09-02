
2. The import mappings window opens. Select the source host from which you want to import the volume mappings. As shown in Figure 8-39, we select the host ITSO-VMHOST-01 and click Import.

**Import Mappings** ×

Select Source Host: ITSO-VMHOST- [dropdown arrow]

[Cancel] [Import]

Figure 8-39 import volume mappings source host selection

3. After the task completes, verify that the mappings are as expected from the Hosts menu (see Figure 8-26 on page 346), right-click the target host, and select Properties. Then, click the Mapped Volumes tab and verify that the required volumes were mapped to the new host (see Figure 8-37 on page 353).

## Renaming a host

To rename a host, complete the following steps:

1. Select the host, and then right-click and select Rename (see Figure 8-40).

| ⊕ Add Host            | Actions ▼                    |           | Default ▼  | Contains ▼    | Filter            |
| --------------------- | ---------------------------- | --------- | ---------- | ------------- | ----------------- |
| Name                  | Rename...                    | Host Type | # of Ports | Host Mappings | Host Cluster ID   |
|                       | Assign to Host Cluster...    |           |            |               | Host Cluster Name |
| ITSO-VMHOST-01        | Remove from Host Cluster...  | Generic   | 2          | No            |                   |
| ITSO-VMHOST-02        | Modify Volume Mappings...    | Generic   | 2          | No            |                   |
|                       | Duplicate Volume Mappings... |           |            |               |                   |
|                       | Import Volume Mappings...    |           |            |               |                   |
|                       | Modify Type...               |           |            |               |                   |
|                       | Edit Throttle...             |           |            |               |                   |
|                       | View All Throttles...        |           |            |               |                   |
|                       | Remove Private Mappings...   |           |            |               |                   |
|                       | Remove                       |           |            |               |                   |
| Showing 2 hosts \| Se | Properties                   |           |            |               |                   |


Figure 8-40 Rename a host

354    Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1
