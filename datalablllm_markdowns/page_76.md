Create Pool

| Name:           | Pool2                                          |
|-----------------|------------------------------------------------|
| Data reduction: | <input checked="true" type="checkbox"/> Enable |

▲ If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently.
 

Cancel
CreateFigure 6-4 Create Pool dialog box

Mark the **Data Reduction** check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings**  $\rightarrow$ **GUI Preferences**  $\rightarrow$  **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

|  | Dashboard     |
|--|---------------|
|  | Monitoring    |
|  | Pools         |
|  | Volumes       |
|  | Hosts         |
|  | Copy Services |
|  | Access        |
|  | Settings      |

Login

|         | General |
|---------|---------|
| General |         |

| Clear customization:                            | <button>Clear</button>                                                                                            |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Default logout time (minutes, or 0 to disable): | 120                                                                                                               |
| Knowledge Center:                               | http://www.ibm.com/support/knowledgecenter/STPVGU <button>Restore Default</button>                                |
| Refresh GUI cache:                              | <button>Refresh</button>                                                                                          |
| Advanced pool settings:                         | <label><input checked="checked" type="checkbox"/>Enable</label> Allow extent size selection during pool creation. |

Save Reset*Figure 6-5 Advanced pool settings* 

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

 $\equiv$