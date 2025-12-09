Key details from the "Create Pool" dialog box:

*   Pool Name: Pool2
*   Data Reduction: Enabled
*   Warning: I/O performance may be affected if the physical capacity usage of a data reduction pool exceeds 85%. The system requires 15% available capacity for efficient reclamation.

Figure 6-4 Create Pool dialog box

Mark the Data Reduction check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking Settings → GUI Preferences → General and checking Advanced pool settings, as shown in Figure 6-5.

The image shows the "General" settings page within a system interface. Key settings displayed are:

*   **Default logout time:** 120 minutes.
*   **Knowledge Center:** A URL is provided for the knowledge center.
*   **Advanced pool settings:** This setting is enabled to "Allow extent size selection during pool creation."

Figure 6-5 Advanced pool settings

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

194 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1