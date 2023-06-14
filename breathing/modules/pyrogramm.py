import json
import requests
from pyrogram import Client, filters
from pyrogram.types import Message, Chat
from pyrogram.types import ChatPermissions
from Messi import pbot

api_key = "SlayerApiKey-a3b216ec73c1016aa8332d4533c72d11d09abd0c" #Get it from @BlueXDBot by /token

url = "https://slayerapi2-0.herokuapp.com/records"
headers = {'API-KEY': api_key}

response = requests.get(url, headers=headers)
if response.status_code == 400: # bad request
    print("RESTARTING SLAYER SCANNER!!!!")
    response = requests.get(url, headers=headers)
    if response.status_code != 200: # unknown error
        print("SLAYER SCANNER FAILED TO START!!!")
elif response.status_code == 401: # not valid api key
    print("INVALID API KEY FOR SLAYER SCANNER!!!")
else:
    pass

SLAYER_DATABASE = {}
if response.status_code == 200: # SUCCESSFULL
    SLAYER_DATABASE = json.loads(response.text) # {user_id: [case_id, reason, bancode]}
    print("SLAYER SCANNER IS ONLINE!!!")

SCANNED_ID = [] # Your list of scanned user IDs
allkeys = SLAYER_DATABASE.keys()
for userid in allkeys:
    userid = int(userid)
    SCANNED_ID.append(userid)

scanned_users = {} # Keep track of the scanned users detected in each group
NOTICE_MSG = """
{} is banned globally as `{}`
Reason: `{}` |
Appeal By: @support
"""


@pbot.on_message(filters.group & filters.all)
async def scanning(client, message: Message):
    if message.from_user is None:
	    return
    if message.from_user.id in SCANNED_ID:
        chat_id = message.chat.id
        try:
            await client.ban_chat_member(chat_id, message.from_user.id)
            reasonn = SLAYER_DATABASE[str(message.from_user.id)][0] + " - "
            reasonn += SLAYER_DATABASE[str(message.from_user.id)][2]
            await message.reply_text(
                NOTICE_MSG.format(
                    message.from_user.mention(message.from_user.first_name),
                    SLAYER_DATABASE[str(message.from_user.id)][1],
                    reasonn
                )
            )
        except Exception as e:
            if chat_id in scanned_users and message.from_user.id in scanned_users[chat_id]:
                return
            if chat_id not in scanned_users:
                scanned_users[chat_id] = []
            scanned_users[chat_id].append(message.from_user.id)
            reasonn = SLAYER_DATABASE[str(message.from_user.id)][0] + " - "
            reasonn += SLAYER_DATABASE[str(message.from_user.id)][2]
            await message.reply_text(
                NOTICE_MSG.format(
                    message.from_user.mention(message.from_user.first_name),
                    SLAYER_DATABASE[str(message.from_user.id)][1],
                    reasonn
                )
            )
