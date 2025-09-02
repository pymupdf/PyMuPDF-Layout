The image shows a "Create Pool" dialog box with a name field containing "Pool2" and a checked "Enable" option for data reduction. There is a warning message explaining that if physical capacity usage exceeds 85%, I/O performance may be affected, and the system requires 15% available capacity for efficient reclamation. The dialog includes Cancel and Create buttons at the bottom.

Figure 6-4 Create Pool dialog box

Mark the Data Reduction check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking Settings →
GUI Preferences → General and checking Advanced pool settings, as shown in
Figure 6-5.

| Setting | Value / Action |
| :--- | :--- |
| Clear customization | `Clear` button |
| Default logout time (minutes, or 0 to disable) | `120` |
| Knowledge Center | `http://www.ibm.com/support/knowledgecenter/STPVGU` and `Restore Default` button |
| Refresh GUI cache | `Refresh` button |
| Advanced pool settings | `Enable` checkbox is checked. (Tooltip: "Allow extent size selection during pool creation.") |

Figure 6-5 Advanced pool settings

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

194

Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1

=