Dashboard

Create Pool

Login

General

Monitoring

Pools

Volumes

Name:

Pool2

Hosts

Data reduction: M Enable

Copy Services

A If the physical capacity usage of a data reduction pool exceeds

Access more than 85%, I/O performance can be affected. The system

Settings needs 15% of physical capacity available in data reduction pools to

ensure that capacity reclamation can be performed efficiently.

General

Clear customization:

Default logout time (minutes, or 0 to disable):

Knowledge Center:

Refresh GUI cache:

Advanced pool settings:

Clear

120

http://www.ibm.com/support/knowledgecenter/STPVGU

Refresh

• Enable 2)

Allow extent size selection during pool creation.

<!-- image -->

Fur 6-5 Advanced nool settinas

Figure 6-4   Create Pool dialog box

Mark the Data Reduction check box to create the Data Reduction Pool. Leaving it unmarked creates a standard storage pool.

A standard storage pool that is created by using the GUI has a default extent size of 1 GB. Data Reduction Pools have a default extent size of 4 GB. The size of the extent is selected at creation time and cannot be changed later.

If you want to specify a different extent size, you can enable this option by clicking Settings → GUI Preferences → General and checking Advanced pool settings , as shown in Figure 6-5.

Figure 6-5   Advanced pool settings

<!-- image -->

When advanced pool settings are enabled, you can additionally select an extent size at creation time, as shown in Figure 6-6 on page 195.

Restore Default

Save

Reset