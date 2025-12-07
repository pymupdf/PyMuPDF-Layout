

194    Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1

**Figure 6-4** *Create Pool dialog box*

[Dialog box showing:
- Title: "Create Pool" with × close button
- Name field containing "Pool2"
- Data reduction checkbox (checked) with "Enable" label
- Warning icon with text: "If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently."
- Information icon at bottom left
- "Cancel" and "Create" buttons at bottom right]

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** ⇒ **GUI Preferences** ⇒ **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

[Screenshot showing settings interface with:
- Left sidebar menu including: Dashboard, Monitoring, Pools, Volumes, Hosts, Copy Services, Access, Settings
- Main panel showing "General" tab with:
  - Clear customization section with "Clear" button
  - Default logout time field showing "120"
  - Knowledge Center URL: http://www.ibm.com/support/knowledgecenter/STPVGU with "Restore Default" button
  - Refresh GUI cache section with "Refresh" button
  - Advanced pool settings checkbox (checked) with text "Allow extent size selection during pool creation."
- "Save" and "Reset" buttons in top right]

**Figure 6-5** *Advanced pool settings*

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.