The content of the welcome message is helpful when you need to notify users about some important information about the system, such as security warnings or a location description. To define and enable the welcome message by using the GUI, edit the text area with the message content and click Save(see Figure 5-80).

| Field | Value |
|---|---|
| Page / Section | Login → General |
| Panel Title | Login Message |
| Description | The login message will be displayed to anyone logging into the GUI or in a CLI session. |
| Login message enabled | Enabled (checkbox checked) |
| Message text | "This is an ITSO-managed system. Unauthorized access is restricted." |
| Buttons | Save, Reset

Figure 5-80 Enabling login message

The resulting log-in screen is shown in Figure 5-81.

The image shows a login screen for Storwize V7000 Storage Management. The screen has fields for "Username" and "Password", a "Sign In" button, and a message stating "This is an ITSO-managed system. Unauthorized access is restricted.". The system is identified as (ITSO_V7000G2_A).

Figure 5-81 Welcome message in GUI

The banner message also appears in the CLI login prompt window, as shown in Figure 5-82.

10.18.228.64 - PuTTY

login as: ITSO_admin
This is an ITSO-managed system. Unauthorized access is restricted. Using keyboar
d-interactive authentication.
Password:

Figure 5-82 Banner message in CLI

182 Implementing the IBM Storwize V7000 with IBM Spectrum Virtualize V8.2.1