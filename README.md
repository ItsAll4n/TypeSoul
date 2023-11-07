# Type://Soul Auto Raid

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation:
1) First download the latest version of the program.
2) Extract the files to a folder of your choice.
3) Ensure "Pytesseract" is installed. https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
4) Copy the "C:\Program Files\Tesseract-OCR" folder into the folder your extracted the program into.
5) Ensure "AutoIt" is Installed. https://www.autoitscript.com/cgi-bin/getfile.pl?autoit3/autoit-v3-setup.zip

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Config guide:

Default config.json file:
```json
{
    "wait_time": 1,
    "check_hog": false,
    "check_sb": false,
    "webhook_enabled": false,
    "webhook_ping": "<@1234567890987654>",
    "webhook": "https://discord.com/api/webhooks/xxxxxxxx/xxxxxxxxxxxxxx"
}
```

### wait_time:
How often you want it to check for items/buttons.

### check_hog:
Whether or not it should check for "Hogyoku Fragments" or not.

### check_sb:
Whether or not it should check for "Skill Box" or not.

### webhook_enabled:
Whether it should send a webhook to Discord or not.

### webhook_ping:
Who the webhook should ping.

### webhook:
If you set webhook_enabled to "True" input your webhook into here to it can actually send it to you
