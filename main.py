import json, subprocess, autoit, win32gui, pytesseract, pyautogui
from PIL import Image
from discord_webhook import DiscordWebhook, DiscordEmbed

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

with open("config.json", "r") as config:
    config = json.load(config)

raid_lobby_key = config['raid_lobby_key']
check_hog = config['check_hog']
check_sb = config['check_sb']
webhook_enabled = config['webhook_enabled']
webhookurl = config['webhook']
ping = config['webhook_ping']

if webhook_enabled == True:
    webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")

def Check():
    ScreenShot = pyautogui.screenshot(region=(700, 200, 550, 550))
    ScreenShot.save(r'Images/Drops.png')
    Drops = Image.open('Images/Drops.png')
    DroppedItems = pytesseract.image_to_string(Drops)
    if check_hog == True:
        if "Hogyoku Fragment" in DroppedItems:
            embed = DiscordEmbed(title=f"Hogyoku Fragment Found!", color=0x000000)
            webhook.add_embed(embed)
            webhook.execute()
            webhook.remove_embed(0)
            subprocess.call("taskkill /f /im RobloxPlayerBeta.exe", shell=True)
    if check_sb == True:
        if "Skill Box" in DroppedItems:
            embed = DiscordEmbed(title=f"Skillbox Found!", color=0x000000)
            webhook.add_embed(embed)
            webhook.execute()
            webhook.remove_embed(0)
            subprocess.call("taskkill /f /im RobloxPlayerBeta.exe", shell=True)

while True:
    win = win32gui.FindWindow(None, "Roblox")
    if win:
        if pyautogui.locateOnScreen('Images/JoinLobby.png'):
            x, y = pyautogui.locateCenterOnScreen('Images/JoinLobby.png')
            autoit.mouse_click("", x, y)
        s = pyautogui.screenshot()
        for x in range(s.width):
            for y in range(s.height):
                if s.getpixel((x, y)) == (58, 244, 64):
                    autoit.mouse_click("", x, y)
    Check()