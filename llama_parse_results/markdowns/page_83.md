

182    Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1

The content of the welcome message is helpful when you need to notify users about some important information about the system, such as security warnings or a location description. To define and enable the welcome message by using the GUI, edit the text area with the message content and click **Save** (see Figure 5-80).

[Screenshot showing GUI interface with:
- Left sidebar with "Login" selected and "General" option below
- Main panel titled "Login Message" with subtitle "The login message will be displayed to anyone logging into the GUI or in a CLI session."
- Checkbox labeled "Login message:" with "Enabled" checked
- Text area containing "This is an ITSO-managed system. Unauthorized access is restricted."
- "Save" and "Reset" buttons in top right]

*Figure 5-80   Enabling login message*

The resulting log-in screen is shown in Figure 5-81.

[Screenshot showing dark login screen with:
- Title "Storwize V7000"
- Subtitle "Storage Management (ITSO_V7000G2_A)"
- "Username" input field
- "Password" input field
- "Sign In" button
- Red-outlined message box at bottom stating "This is an ITSO-managed system. Unauthorized access is restricted."]

*Figure 5-81   Welcome message in GUI*

The banner message also appears in the CLI login prompt window, as shown in Figure 5-82.

[Screenshot showing terminal window with:
```
10.18.228.64 - PuTTY
login as: ITSO_admin
This is an ITSO-managed system. Unauthorized access is restricted. Using keyboard-interactive authentication.
Password:
```
]

*Figure 5-82   Banner message in CLI*