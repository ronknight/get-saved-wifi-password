<p><a target="_blank" href="https://app.eraser.io/workspace/NNvK2TSsAisLEufhr97Y" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

# Saved WiFi Password Retriever
This Python script retrieves and displays the names and passwords of all saved WiFi profiles on a Windows machine.

## Requirements
- Python 3.x
- Windows Operating System
## Usage
1. Save the `get_wifi.py`  script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script using the following command:python get_wifi.py
The script will output the names and corresponding passwords of all saved WiFi profiles on your system.

## How it Works
The script uses the `subprocess` module to run Windows commands (`netsh`) to retrieve information about the saved WiFi profiles. Here's a breakdown of the steps:

1. The `netsh wlan show profiles`  command is executed to get a list of all saved WiFi profile names.
2. For each profile name, the `netsh wlan show profile <name> key=clear`  command is executed to retrieve the password in plaintext.
3. The password is extracted from the command output using regular expressions.
4. The WiFi name and password are printed to the console.
Note that the script requires administrative privileges to run the `netsh` commands successfully.

## Disclaimer
This script is intended for educational purposes only. Accessing WiFi networks without proper authorization may be illegal in some jurisdictions. Use this script responsibly and only on networks where you have permission to do so.


<!-- eraser-additional-content -->
## Diagrams
<!-- eraser-additional-files -->
<a href="/README-Saved WiFi Password Retriever Flowchart-1.eraserdiagram" data-element-id="xR26Uj-gmo42uwCSuML4X"><img src="/.eraser/NNvK2TSsAisLEufhr97Y___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----1de9c6967c1928a58e723a7d02dce8ed-Saved-WiFi-Password-Retriever-Flowchart.png" alt="" data-element-id="xR26Uj-gmo42uwCSuML4X" /></a>
<!-- end-eraser-additional-files -->
<!-- end-eraser-additional-content -->
<!--- Eraser file: https://app.eraser.io/workspace/NNvK2TSsAisLEufhr97Y --->