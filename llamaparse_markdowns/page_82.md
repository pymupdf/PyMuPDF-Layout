
15. Click **Finish** to end the storage migration wizard, as shown in Figure 9-14.

| Storage Migration Wizard                                                                                                       | Storage Migration Wizard | Storage Migration Wizard                                                                                                                                                                                                     | Storage Migration Wizard | Storage Migration Wizard |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------ |
| \[Image of storage migration: one server on left, SAN in middle, three servers on right with arrows indicating data migration] |                          | The data migration has begun. After it is completed use the finalize action in the<br/>Migration panel of the management GUI to remove the image-mode volume copies.<br/>Then unzone and remove the original storage system. |                          |                          |
|                                                                                                                                |                          | Back Finish                                                                                                                                                                                                                  |                          |                          |


_Figure 9-14  Migration is started_

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

| Start New Migration \| Actions \| Default \| Contains \| Filter<br/>Volume Name | Start New Migration \| Actions \| Default \| Contains \| Filter<br/>Target Pool | Start New Migration \| Actions \| Default \| Contains \| Filter<br/>Status | Start New Migration \| Actions \| Default \| Contains \| Filter<br/>Progress | Start New Migration \| Actions \| Default \| Contains \| Filter<br/>UID | Start New Migration \| Actions \| Default \| Contains \| Filter |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------- |
| controller0\_0000000000000000                                                   | Test Pool                                                                       | ✔ Online                                                                   | 15%                                                                          | 600507680C9880004800000000000034                                        |                                                                 |


_Figure 9-15  The ongoing Migration is listed in the Storage Migration window_

16. If you want to check the progress by using the CLI, run the `lsvdisksyncprogress` command because the process is essentially a volume copy, as shown in Figure 9-16.

```bash
IBM_Storwize:ITSO-V7k:superuser> lsvdisksyncprogress
vdisk_id  vdisk_name           copy_id  progress  estimated_completion_time
26        controller0          0        1_7       181016175637
IBM_Storwize:ITSO-V7k:superuser>
```

_Figure 9-16  Checking migration progress by using CLI_

17. When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click **Finalize**, as shown in Figure 9-17 on page 400.
