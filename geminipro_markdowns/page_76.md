![Figure 6-4: Create Pool dialog box](figure-6-4.png)

**Figure 6-4 (summary):** A dialog box titled "Create Pool" is displayed. It contains a "Name" field with "Pool2" entered. Below that, a "Data reduction" checkbox is checked with the label "Enable". A warning message indicates that if a data reduction pool's physical capacity usage exceeds 85%, I/O performance can be affected. At the bottom are "Cancel" and "Create" buttons.

***

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings → GUI Preferences → General** and checking **Advanced pool settings**, as shown in Figure 6-5.

![Figure 6-5: Advanced pool settings](figure-6-5.png)

**Figure 6-5 (summary):** The "General" settings screen of the GUI is shown. In the "Advanced pool settings" section, a checkbox labeled "Enable" is checked. The description next to it reads "Allow extent size selection during pool creation."

***

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.