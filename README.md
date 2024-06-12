<p><a target="_blank" href="https://app.eraser.io/workspace/NNvK2TSsAisLEufhr97Y" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

<h1 align="center"><a href="https://github.com/ronknight/get-saved-wifi-password">Get Saved WiFi Password</a></h1>
<h2 align="center">Saved WiFi Password Retriever</h2>
<h4 align="center">This Python script retrieves and displays the names and passwords of all saved WiFi profiles on a Windows machine.
</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/get-saved-wifi-password/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/get-saved-wifi-password/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a> •
  <a href="#script">Script</a> •
  <a href="#disclaimer">Disclaimer</a> •
  <a href="#diagrams">Diagrams</a> •
</p>

---

## Requirements
- Python 3.x
- Windows Operating System

## Usage
1. Save the `get_wifi.py`  script to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script using the following command:python get_wifi.py
The script will output the names and corresponding passwords of all saved WiFi profiles on your system.

## Script
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