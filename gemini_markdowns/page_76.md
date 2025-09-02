![Figure 6-4: Create Pool dialog box](figure-6-4.png)

**Figure 6-4 (summary):** This dialog box titled "Create Pool" allows users to define a new storage pool. It features a "Name" field (pre-filled with "Pool2") and a "Data reduction" checkbox, which is enabled. Below this, an important warning advises that if physical capacity usage in a data reduction pool exceeds 85%, I/O performance might be affected, and 15% physical capacity is needed for efficient reclamation. The dialog includes "Cancel" and "Create" buttons.

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** → **GUI Preferences** → **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

![Figure 6-5: Advanced pool settings](figure-6-5.png)

**Figure 6-5 (summary):** This image displays the "General" preferences section within the system's GUI. On the left, a navigation panel shows options like Dashboard, Monitoring, Pools, Volumes, etc. The main content area shows various "General" settings: "Clear customization," "Default logout time" (set to 120 minutes), "Knowledge Center" URL, and "Refresh GUI cache." Crucially, the "Advanced pool settings" checkbox is enabled, accompanied by the text "Allow extent size selection during pool creation." Save and Reset buttons are visible at the top right.

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.