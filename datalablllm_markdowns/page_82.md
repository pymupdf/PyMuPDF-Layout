## 15. Click **Finish** to end the storage migration wizard, as shown in Figure 9-14.

| Storage Migration Wizard |
|--------------------------|
|--------------------------|

The data migration has begun. After it is completed use the finalize action in the Migration panel of the management GUI to remove the image-mode volume copies. Then unzone and remove the original storage system.

| SAN  |        |
|------|--------|
| Back | Finish |

Figure 9-14 Migration is started

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

![](_page_0_Picture_4.jpeg)

Figure 9-15 The ongoing Migration is listed in the Storage Migration window

16.If you want to check the progress by using the CLI, run the lsvdisksyncprogress command because the process is essentially a volume copy, as shown in Figure 9-16.

![](_page_0_Figure_7.jpeg)

Figure 9-16 Checking migration progress by using CLI

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click **Finalize**, as shown in Figure 9-17 on page 400.