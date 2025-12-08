IBM Storwize: ITSO-V7k: superuser&gt;1svdisksyncproqress vdisk\_id vdisk\_ name

Start New Migration

: Actions - controllero 0000000000000000 0 1

26

Volume Name

Storage Migration Wizard copy\_id progress estimated completion\_time

Target Pool

IBM Storwize: ITSO-V7k: superuser&gt;l controller0\_000000000…. \_

Status

Test Pool

/ Online

Default

7

Progress

15%

Contains v

Filter

181016175637

UID

600507680C9B80004800000000000034

15.Click Finish to end the storage migration wizard, as shown in Figure 9-14.

The data migration has begun. After it is completed use the finalize action in the

Migration panel of the management GUI to remove the image-mode volume copies.

Then unzone and remove the original storage system.

Fire 0-14 Miaration ic ctarted

Figure 9-14   Migration is started

<!-- image -->

The end of the wizard is not the end of the migration task. You can find the progress of the migration in the Storage Migration window, as shown in Figure 9-15. The target storage pool and the progress of the volume copy synchronization is also displayed there.

Figure 9-15   The ongoing Migration is listed in the Storage Migration window

<!-- image -->

- 16.If you want to check the progress by using the CLI, run the lsvdisksyncprogress command because the process is essentially a volume copy, as shown in Figure 9-16.
- 17.When the migration completes, select all of the migrations that you want to finalize, right-click the selection, and click Finalize , as shown in Figure 9-17 on page 400.

Figure 9-16   Checking migration progress by using CLI

<!-- image -->