| Create Pool                                                                                                                                                                                                                                                                 |  |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|
| Pool2<br>Name:<br>Data reduction:<br>Enable                                                                                                                                                                                                                                 |  |  |
| A<br>If the physical capacity usage of a data reduction pool exceeds<br>more than 85%, I/O performance can be affected. The system<br>needs 15% of physical capacity available in data reduction pools to<br>ensure that capacity reclamation can be performed efficiently. |  |  |
| Cancel<br>Create<br>3                                                                                                                                                                                                                                                       |  |  |

*Figure 6-4 Create Pool dialog box*

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** → **GUI Preferences** → **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

| $\boldsymbol{\mathcal{P}}$ | Dashboard     | Login   | General                                                                 |                                                                             | Reset<br>Save |
|----------------------------|---------------|---------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------|---------------|
| ₩                          | Monitoring    | General | Clear customization:<br>Default logout time (minutes, or 0 to disable): | Clear<br>120                                                                |               |
| ₩                          | Pools         |         | Knowledge Center:                                                       | http://www.ibm.com/support/knowledgecenter/STPVGU<br><b>Restore Default</b> |               |
| B                          | Volumes       |         | Refresh GUI cache:<br>Advanced pool settings:                           | Refresh<br>Allow extent size selection during<br>Enable<br>pool creation.   |               |
| 0                          | Hosts         |         |                                                                         |                                                                             |               |
| Ħ                          | Copy Services |         |                                                                         |                                                                             |               |
| $\mathcal{L}$              | Access        |         |                                                                         |                                                                             |               |
| భు                         | Settings      |         |                                                                         |                                                                             |               |

*Figure 6-5 Advanced pool settings*

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.