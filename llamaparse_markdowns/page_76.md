

| **Create Pool**                                                                                                                                                                                                                                                     |             |        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------ |
| Name:                                                                                                                                                                                                                                                               | Pool2       |        |
| Data reduction:                                                                                                                                                                                                                                                     | \[x] Enable |        |
| **⚠** If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently. |             |        |
|                                                                                                                                                                                                                                                                     | Cancel      | Create |


> *Figure 6-4  Create Pool dialog box*

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings → GUI Preferences → General** and checking **Advanced pool settings**, as shown in Figure 6-5.

| **Dashboard**<br/>Monitoring<br/>Pools<br/>Volumes<br/>Hosts<br/>Copy Services<br/>Access<br/>**Settings** | **Login**   |                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------- |
|                                                                                                            | **General** | Clear customization:<br/>Clear                                                                 |
|                                                                                                            |             | Default logout time (minutes, or 0 to disable):<br/>120                                        |
|                                                                                                            |             | Knowledge Center:<br/>http\://www\.ibm.com/support/knowledgecenter/STPVGU<br/>Restore Default  |
|                                                                                                            |             | Refresh GUI cache:<br/>Refresh                                                                 |
|                                                                                                            |             | Advanced pool settings:<br/>\[x] Enable<br/>*Allow extent size selection during pool creation* |
|                                                                                                            | Save Reset  |                                                                                                |


> *Figure 6-5  Advanced pool settings*

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.
