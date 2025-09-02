# 15.Click Finish to end the storage migration wizard, as shown in Figure 9-14.

The image shows the Storage Migration Wizard interface with a diagram illustrating data migration from a server on the left through a SAN (Storage Area Network) to multiple servers on the right. The wizard indicates that data migration has begun and provides instructions to use the finalize action in the Migration panel after completion to remove image-mode volume copies and unzone the original storage system. At the bottom right, there are "Back" and "Finish" buttons to complete the wizard.

Figure 9-14 Migration is started

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

| Volume Name | Target Pool | Status | Progress | UID |
|---|---|---|---|---|
| controller0_000000000... | Test Pool | ✔ Online | 15% | 600507680C9B80004800000000000034 |

Figure 9-15 The ongoing Migration is listed in the Storage Migration window

16. If you want to check the progress by using the CLI, run the 1svdisksyncprogress command because the process is essentially a volume copy, as shown in Figure 9-16.

IBM_Storwize:ITSO-V7k:superuser>lsvdisksyncprogress
vdisk_id vdisk_name copy_id progress estimated_completion_time
26 controller0 000000000000000 0 1 7 181016175637
IBM_Storwize:ITSO-V7k:superuser>

Figure 9-16 Checking migration progress by using CLI

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click Finalize, as shown in Figure 9-17 on page 400.

Chapter 9. Storage migration 399

=