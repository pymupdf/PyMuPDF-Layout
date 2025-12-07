15.ClickFinish to end the storage migration wizard, as shown in Figure 9-14.

Key information from the image:

*   **Title:** Storage Migration Wizard.
*   **SAN:** Data is being migrated to SAN.
*   **Action:** User should finalize action in management GUI to remove image-mode volume copies. Unzone/remove original storage system.
*   **Available Actions:** Back, Finish.

Figure 9-14 Migration is started

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

Start New Migration:
Actions:
Default
Contains
Filter

Volume Name: controller0_00000000...
Target Pool: Test Pool
Status: Online
Progress: 15%
UID: 600507680C9B80004800000000034

Figure 9-15 The ongoing Migration is listed in the Storage Migration window

- 16.If you want to check the progress by using the CLI, run the lsvdisksyncprogress command because the process is essentially a volume copy, as shown in Figure 9-16.

IBM_Storwize: ITSO-V7k: superuser>lsvdisksyncprogress
vdisk_id vdisk_name copy_id progress estimated_completion_time
26 controller0 0000000000000000 0 1 7 181016175637
IBM Storwize: ITSO-V7k: superuser>

Figure 9-16 Checking migration progress by using CLI

17.When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click Finalize, as shown in Figure 9-17 on page 400.

Chapter 9. Storage migration 399