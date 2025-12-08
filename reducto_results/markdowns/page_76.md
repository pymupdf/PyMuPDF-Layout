Key details from the "Create Pool" dialog box:

*   Pool Name: Pool2
*   Data reduction: Enabled
*   Warning: Physical capacity usage exceeding 85% in a data reduction pool may affect I/O performance. The system needs 15% of physical capacity available for efficient reclamation.
*   Options: Cancel, Create

Figure 6-4 Create Pool dialog box

Mark the Data Reduction check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking Settings → GUI Preferences → General and checking Advanced pool settings, as shown in Figure 6-5.

Key details from the image:

*   GUI shows Settings -> General
*   Default logout time is set to 120 minutes.
*   Knowledge Center URL is: http://www.ibm.com/support/knowledgecenter/STPVGU
*   Advanced pool settings are enabled, allowing extent size selection during pool creation.

Figure 6-5 Advanced pool settings

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

194 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1