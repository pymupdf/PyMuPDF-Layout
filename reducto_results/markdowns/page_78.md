2. The import mappings window opens. Select the source host from which you want to import the volume mappings. As shown in Figure 8-39, we select the host ITSO-VMHOST-01 and click Import.

- Title: Import Mappings
- Field: Select Source Host: [dropdown] — value shown: "ITSO-VMHOST-"
- Dropdown appears focused/outlined
- Close icon (X) at top-right
- Action buttons: "Cancel" and "Import"

Figure 8-39 import volume mappings source host selection

3. After the task completes, verify that the mappings are as expected from the Hostsmenu (see Figure 8-26 on page 346), right-click the target host, and select Properties . Then, click the Mapped Volumes tab and verify that the required volumes were mapped to the new host (see Figure 8-37 on page 353).

## Renaming a host

To rename a host, complete the following steps:

1. Select the host, and then right-click and select Rename (see Figure 8-40).

The image shows a software interface with a table and a context menu. The table displays host information. The context menu opened from the "Actions" button, shows options such as "Rename...", "Assign to Host Cluster...", etc.

| Name            | Host Type | # of Ports | Host Mappings | Host Cluster ID | Host Cluster Nam II! |
|-----------------|-----------|------------|---------------|-----------------|----------------------|
| ITSO-VMHOST-01  | Generic   | 2          | No            |                 |                      |
| ITSO-VMHOST-02  | Generic   | 2          | No            |                 |                      |


Figure 8-40 Rename a host

354 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1