![Figure 6-4: Create Pool dialog box](figure-6-4-create-pool-dialog-box.png)

**Figure 6-4 (summary):** The "Create Pool" dialog box is shown. The Name field contains "Pool2". The "Data reduction" checkbox is checked. A warning message reads: "If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently."

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** → **GUI Preferences** → **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

![Figure 6-5: Advanced pool settings](figure-6-5-advanced-pool-settings.png)

**Figure 6-5 (summary):** The Settings menu is shown with the General tab selected. The "Advanced pool settings" option is checked (enabled), with the description "Allow extent size selection during pool creation."

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.