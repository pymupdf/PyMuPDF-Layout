

Chapter 9. Storage migration    399

15. Click **Finish** to end the storage migration wizard, as shown in Figure 9-14.

[Figure 9-14 shows a Storage Migration Wizard dialog window with the following content:]

**Storage Migration Wizard**

[Diagram showing a server on the left, connected via SAN (shown as an orange oval) to storage arrays on the right, with database cylinders in the middle]

The data migration has begun. After it is completed use the finalize action in the Migration panel of the management GUI to remove the image-mode volume copies. Then unzone and remove the original storage system.

[Two buttons at bottom right: "< Back" and "Finish"]

*Figure 9-14    Migration is started*

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

[Figure 9-15 shows a Storage Migration window with the following table:]

| Volume Name               | Target Pool | Status   | Progress | UID                              |
| ------------------------- | ----------- | -------- | -------- | -------------------------------- |
| controller0\_000000000... | Test Pool   | ✓ Online | 15%      | 600507680C9B80004800000000000034 |


*Figure 9-15    The ongoing Migration is listed in the Storage Migration window*

16. If you want to check the progress by using the CLI, run the `lsvdisksyncprogress` command because the process is essentially a volume copy, as shown in Figure 9-16.

```
IBM_Storwize:ITSO-V7k:superuser>lsvdisksyncprogress
vdisk_id vdisk_name                           copy_id progress estimated_completion_time
26       controller0_0000000000000000_0_1__   7        181016175637
IBM_Storwize:ITSO-V7k:superuser>
```

*Figure 9-16    Checking migration progress by using CLI*

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click **Finalize**, as shown in Figure 9-17 on page 400.