'''import os
import re
import random

from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://telegra.ph/file/a815aeef7bbb7c22985ec.jpg"

@register(pattern=("Awake"))
async def awake(event):
  TEXT = f"""Hi {event.sender.first_name}, I'm shoushuke komi ."""\n
  TEXT += f"❄shoushuke Is Alive 🗿 **"\n\n
  TEXT += f"❄My Domain : (https://t.me/Knights_X_association/34)**"\n\n
  TEXT += f"❄ **Powered By: [Knights](https://t.me/Knights_X_association)**"\n\n
   Thanks For Adding Me Here ❤️ re ❤️ **"
  BUTTON = [[Button.url("Help", "https://t.me/shoushuke_komi_bot?start=help"), Button.url("Support", "https://t.me/shoushuke_support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
'''
