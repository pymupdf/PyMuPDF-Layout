The content of the welcome message is helpful when you need to notify users about some important information about the system, such as security warnings or a location description. To define and enable the welcome message by using the GUI, edit the text area with the message content and click Save (see Figure 5-80).

![Figure 5-80: Enabling login message](figure-5-80.png)

**Figure 5-80 (summary):** The "Login Message" configuration panel in the GUI. It displays a checkbox marked "Enabled" and a text field containing the warning: "This is an ITSO-managed system. Unauthorized access is restricted." Buttons for "Save" and "Reset" are located at the top right.

The resulting log-in screen is shown in Figure 5-81.

![Figure 5-81: Welcome message in GUI](figure-5-81.png)

**Figure 5-81 (summary):** The Storwize V7000 login interface. It shows fields for Username and Password. A red oval highlights the text displayed at the bottom of the panel: "This is an ITSO-managed system. Unauthorized access is restricted."

The banner message also appears in the CLI login prompt window, as shown in Figure 5-82.

![Figure 5-82: Banner message in CLI](figure-5-82.png)

**Figure 5-82 (summary):** A PuTTY terminal window displaying the CLI login sequence. The text reads:
```text
10.18.228.64 - PuTTY
login as: ITSO_admin
This is an ITSO-managed system. Unauthorized access is restricted. Using keyboard-interactive authentication.
Password:
```