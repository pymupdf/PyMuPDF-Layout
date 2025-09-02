15. Click **Finish** to end the storage migration wizard, as shown in Figure 9-14.

![Figure 9-14: Migration is started](figure-9-14.png)

**Figure 9-14 (summary):** This diagram illustrates the Storage Migration Wizard process. Data migration begins from a source system (represented by a single server rack) to multiple destination servers via a SAN (Storage Area Network). The accompanying text explains that after completion, the finalize action in the management GUI's Migration panel should be used to remove image-mode volume copies, then unzone and remove the original storage system.

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

![Figure 9-15: The ongoing Migration is listed in the Storage Migration window](figure-9-15.png)

**Figure 9-15 (summary):** This screenshot shows the "Storage Migration" window with a table of ongoing migrations. The table includes columns for "Volume Name", "Target Pool", "Status", "Progress", and "UID". One entry is visible: `controller0_000000000...` in `Test Pool`, showing `Online` status, `15%` progress, and a specific UID.

16. If you want to check the progress by using the CLI, run the `lsvdisksyncprogress` command because the process is essentially a volume copy, as shown in Figure 9-16.

![Figure 9-16: Checking migration progress by using CLI](figure-9-16.png)

**Figure 9-16 (summary):** This figure displays command-line output from the `lsvdisksyncprogress` command. The output shows details such as `vdisk_id`, `vdisk_name`, `copy_id`, `progress`, and `estimated_completion_time`. An example line shows `26 controller0 0000000000000000 0 1_7 181016175637`, indicating a progress of 7.

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click **Finalize**, as shown in Figure 9-17 on page 400.