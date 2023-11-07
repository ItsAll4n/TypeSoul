import json, subprocess, win32gui, pytesseract, pyautogui, win32com.client, os, time
from PIL import Image
from discord_webhook import DiscordWebhook, DiscordEmbed

autoit = win32com.client.Dispatch("AutoItX3.Control")

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'

os.system(f'title AutoRaid ^')

with open("config.json", "r") as config:
    config = json.load(config)

sleep_timer = config['wait_time']
check_hog = config['check_hog']
check_sb = config['check_sb']
webhook_enabled = config['webhook_enabled']
webhookurl = config['webhook']
ping = config['webhook_ping']

if webhook_enabled == True:
    webhook = DiscordWebhook(url=webhookurl, content=f"{ping}")

def Webhook(title):
    if webhook_enabled == True:
        embed = DiscordEmbed(title=f"{title}", color=0x000000)
        webhook.add_embed(embed)
        webhook.execute()
        webhook.remove_embed(0)
    subprocess.call("taskkill /f /im RobloxPlayerBeta.exe", shell=True)

def Check():
    ScreenShot = pyautogui.screenshot(region=(700, 200, 550, 550))
    ScreenShot.save(r'Drops.png')
    Drops = Image.open('Drops.png')
    DroppedItems = pytesseract.image_to_string(Drops)
    if check_hog == True:
        if "Hogyoku Fragment" in DroppedItems:
            Webhook("Fragment Found!")
    if check_sb == True:
        if "Skill Box" in DroppedItems:
            Webhook("Skillbox Found!")

while True:
    win = win32gui.FindWindow(None, "Roblox")
    if win:
        time.sleep(sleep_timer)
        if pyautogui.locateOnScreen('JoinLobby.png'):
            x, y = pyautogui.locateCenterOnScreen('JoinLobby.png')
            autoit.MouseClick("", x, y)
        s = pyautogui.screenshot()
        for x in range(s.width):
            for y in range(s.height):
                if s.getpixel((x, y)) == (58, 244, 64):
                    autoit.MouseClick("", x, y)
        Check()
