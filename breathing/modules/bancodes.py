import os
import re
from platform import python_version as kontol
from telethon import events, Button
from Messi.events import register
from Messi import telethn as tbot


PHOTO = "https://te.legra.ph/file/1c669652caf94443689ca.jpg"

@register(pattern=("/bancodes"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Shoushuke Komi** \n\n"
  TEXT += "🗡 **Here are bancodes for [Shoushuke](https://t.me/shoushuke_komi_bot)** \n\n"
  TEXT += f"🗡 **My Masters : [Primes Team](https://t.me/PrimesDivision)** \n\n"
  TEXT += f"🗡 **Abuse**  \n\n"
  TEXT += f"🗡 **Mass Add**  \n\n"
  TEXT += f"🗡 **Spambot**  \n\n"
  TEXT += f"🗡 **Raid Initiator**  \n\n"
  TEXT += f"🗡 **Raid Participant**  \n\n"
  TEXT += f"🗡 **NSFW spammer** \n\n"
  TEXT += f"🗡 **Refer to Slayer Bancodes for more info**  \n\n"
  TEXT += "**🔥 Thanks For Starting Me 🔥**"
  BUTTON = [[Button.url("Help", "https://t.me/shkushuke_komi_bot?start=help"), Button.url("My Headquarters", "https://t.me/Shoushuke_Support")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
