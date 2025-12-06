2. The import mappings window opens. Select the source host from which you want to import the volume mappings. As shown in Figure 8-39, we select the host ITSO-VMHOST-01 and click Import.

The image shows a dialog box labeled "Import Mappings". It includes a dropdown menu labeled "Select Source Host", with the current selection being "ITSO-VMHOST-". There are "Cancel" and "Import" buttons.

Figure 8-39 import volume mappings source host selection

3. After the task completes, verify that the mappings are as expected from the Hostsmenu (see Figure 8-26 on page 346), right-click the target host, and select Properties . Then, click the Mapped Volumes tab and verify that the required volumes were mapped to the new host (see Figure 8-37 on page 353).

## Renaming a host

To rename a host, complete the following steps:

1. Select the host, and then right-click and select Rename (see Figure 8-40).

| Name             | Host Type | # of Ports | Host Mappings | Host Cluster ID | Host Cluster Name |
|------------------|-----------|------------|---------------|-----------------|-------------------|
| ITSO-VMHOST-01   | Generic   | 2          | No            | —               | —                 |
| ITSO-VMHOST-02   | Generic   | 2          | No            | —               | —                 |

Visible UI elements:
- Top controls: Add Host button, Actions (dropdown), filter controls (Default / Contains / Filter textbox).
- Bottom status: "Showing 2 hosts" (partial).

Actions menu (visible items, top → bottom):
- Rename...
- Assign to Host Cluster...
- Remove from Host Cluster...
- Modify Volume Mappings...
- Duplicate Volume Mappings...
- Import Volume Mappings...
- Modify Type...
- Edit Throttle...
- View All Throttles...
- Remove Private Mappings...
- Remove
- Properties

Figure 8-40 Rename a host

354 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1