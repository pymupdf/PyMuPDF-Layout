15. Click **Finish** to end the storage migration wizard, as shown in Figure 9-14.

    ![Figure 9-14: Migration is started](figure-9-14.png)

    **Figure 9-14 (summary):** The Storage Migration Wizard displays a completion message: "The data migration has begun. After it is completed use the finalize action in the Migration panel of the management GUI to remove the image-mode volume copies. Then unzone and remove the original storage system."

    The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

    ![Figure 9-15: The ongoing Migration is listed in the Storage Migration window](figure-9-15.png)

    **Figure 9-15 (summary):** The interface shows a table row with the following details:
    - **Volume Name:** `controller0_00000000...`
    - **Target Pool:** Test Pool
    - **Status:** Online (marked with a green check)
    - **Progress:** 15% (displayed as a blue progress bar)
    - **UID:** `600507680C9BB0004800000000000034`

16. If you want to check the progress by using the CLI, run the `lsvdisksyncprogress` command because the process is essentially a volume copy, as shown in Figure 9-16.

    ![Figure 9-16: Checking migration progress by using CLI](figure-9-16.png)

    ```text
    IBM_Storwize:ITSO-V7k:superuser>lsvdisksyncprogress
    vdisk_id vdisk_name                       copy_id progress estimated_completion_time
    26       controller0_0000000000000000     0       1        181016175637
    IBM_Storwize:ITSO-V7k:superuser>
    ```

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click **Finalize**, as shown in Figure 9-17 on page 400.