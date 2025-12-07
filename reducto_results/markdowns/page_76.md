Key information from the "Create Pool" dialog box:

*   **Name:** Pool2
*   **Data reduction:** Enabled
*   **Warning:** I/O performance may be affected if the physical capacity usage of a data reduction pool exceeds 85%. The system needs 15% of physical capacity available.
*   **Buttons:** Cancel, Create

Figure 6-4 Create Pool dialog box

Mark the Data Reduction check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking Settings → GUI Preferences → General and checking Advanced pool settings, as shown in Figure 6-5.

Key details from the GUI screenshot:

*   **Section**: Settings -> General
*   **Clear customization**: Option to clear customization settings.
*   **Default Logout Time**: 120 minutes
*   **Knowledge Center**: URL points to IBM Knowledge Center.
*   **Advanced pool settings**: Allow extent size selection during pool creation. This setting is enabled.
*   **Save** and **Reset** buttons are present.

Figure 6-5 Advanced pool settings

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

194 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1