

**Figure 6-4** Create Pool dialog box

Create Pool                                                                    ×

Name:            Pool2

Data reduction:  ☑ Enable

> ⚠ If the physical capacity usage of a data reduction pool exceeds more than 85%, I/O performance can be affected. The system needs 15% of physical capacity available in data reduction pools to ensure that capacity reclamation can be performed efficiently.

                                                    Cancel        Create

Mark the **Data Reduction** check box to create the **Data Reduction Pool**. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking **Settings** → **GUI Preferences** → **General** and checking **Advanced pool settings**, as shown in Figure 6-5.

**Figure 6-5** Advanced pool settings

| 🖥 Dashboard<br/>📊 Monitoring<br/>💾 Pools<br/>📁 Volumes<br/>🖥 Hosts<br/>📋 Copy Services<br/>🔐 Access<br/>⚙ Settings | Login General Save Reset<br/><br/>General Clear customization: Clear 120<br/>Default logout time (minutes, or 0 to disable):<br/>Knowledge Center: http\://www\.ibm.com/support/knowledgecenter/STPVGU Restore Default<br/>Refresh GUI cache: Refresh<br/>Advanced pool settings: ☑ Enable Allow extent size selection during pool creation. |
| ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

194    Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1
