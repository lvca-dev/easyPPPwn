# easyPPPwn - PlayStation 4 PPPoE RCE
PPPwn is a kernel remote code execution exploit for PlayStation 4 up to FW 11.00. This is a proof-of-concept exploit for [CVE-2006-4304](https://hackerone.com/reports/2177925) that was reported responsibly to PlayStation.

Supported versions are:
- FW 11.00

The exploit prints `Hacked by Luca` on your PS4, Then GoldHen Gets Loaded!

## Requirements
- A computer with an Ethernet port
  - USB adapter also works
- Ethernet cable
- Linux
  - You can use VirtualBox to create a Linux VM with `Bridged Adapter` as network adapter to use the ethernet port in the VM.
- Python3 and gcc installed

## Usage
- Open Terminal and cd To easyPPPwn Then Copy Paste:
- pip install -r requirements.txt
- Then:
- Connect an LAN Cable From PC To PlayStation 4!
- Then:
- Open startme.py, then select ur interface.
- If not Set-up. Set-up An Lan Connection, Select Custom, On IP Select PPPOE, Then Just enter in Both things Something. every other setting is irrelevant! Just select what u think!
- Now Click Test Internet Connection!
- Thats it! If Failed, Simply Close, And Do The Same thing as before.
- Now Set-Up ur Real Internet Connection!
