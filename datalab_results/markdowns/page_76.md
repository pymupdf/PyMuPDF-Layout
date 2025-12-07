

![Screenshot of the 'Create Pool' dialog box. The dialog shows fields for Name (Pool2) and Data reduction (checked, Enable). A warning message states: 'If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently.' Buttons include Cancel and Create.](2dfa6ac3edfe874f68aa0cbccaa42322_img.jpg)

Screenshot of the 'Create Pool' dialog box. The dialog shows fields for Name (Pool2) and Data reduction (checked, Enable). A warning message states: 'If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently.' Buttons include Cancel and Create.

Figure 6-4 Create Pool dialog box

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** → **GUI Preferences** → **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

![Screenshot of the 'Settings' menu, showing the 'General' tab selected. Under 'Advanced pool settings', the checkbox 'Allow extent size selection during pool creation' is checked. Other settings visible include Default logout time (120 minutes), Knowledge Center URL, and options to Clear, Refresh, and Restore Default.](390120de4fe440c42fea8154fcaad334_img.jpg)

Screenshot of the 'Settings' menu, showing the 'General' tab selected. Under 'Advanced pool settings', the checkbox 'Allow extent size selection during pool creation' is checked. Other settings visible include Default logout time (120 minutes), Knowledge Center URL, and options to Clear, Refresh, and Restore Default.

Figure 6-5 Advanced pool settings

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.