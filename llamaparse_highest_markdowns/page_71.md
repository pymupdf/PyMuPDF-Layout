
By right-clicking and selecting **Properties**, you see detailed technical parameters, such as ID, state (online or offline), drive capacity, and the drive use, as shown in Figure 5-30.

**Figure 5-30 Canister information**

The figure shows a GUI interface with two main components:

1. **Rear View panel** (left side) showing:
   - Node Canister
   - iSCSI Port  
   - USB Port
   - Internal Components
   - Right-click context menu with options: Rename, Turn Identify On, Power Off Canister, Remove, Dependent Volumes, Properties

2. **Properties for Canister 1 dialog** (right side) displaying:

| Canister:           | Canister 1                                         |
| ------------------- | -------------------------------------------------- |
| Controller:         | 1                                                  |
| Configuration node: | Yes                                                |
| WWNN:               | 500507680B007610                                   |
| Memory:             | 32 GiB                                             |
| CPU:                | 10 core Intel(R) Xeon(R) CPU E5-2618L v4 @ 2.20GHz |
| FRU PN:             | 0000000                                            |
| FRU identity:       | 11S0000000Y00000000000                             |


In an environment with multiple IBM Storwize V7000 clusters, you can easily direct the onsite personnel or technician to the correct device by enabling the identification LED on the front pane. Click **Turn Identify On** in the menu that is shown in Figure 5-31.

**Figure 5-31 Identification LED**

The figure shows two Front View panels side by side with an arrow between them, demonstrating the before and after states of turning on the identification LED. The left panel shows the context menu with "Turn Identify On" option, and includes options for Drive and Dependent Volumes. The right panel shows the result after the LED has been activated.

Wait for confirmation from the technician that the device in the data center was correctly identified. In the GUI, you see a flashing light, which indicates that the Identify LED was turned on.

Chapter 5. Graphical user interface   149
