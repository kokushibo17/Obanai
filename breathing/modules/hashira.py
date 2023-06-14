from Messi import dispatcher

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

NETWORK_USERNAME = "Hashira_Association"
PHOTO = "https://telegra.ph/file/7fd7e49b876d5ba43cb37.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "Hashira_Association":
    def hashira(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [𝐇𝐀𝐒𝐇𝐈𝐑𝐀  𝐀𝐒𝐒𝐎𝐂𝐈𝐀𝐓𝐈𝐎𝐍](https://t.me/Hashira_Association),
𝐇𝐀𝐒𝐇𝐈𝐑𝐀  𝐀𝐒𝐒𝐎𝐂𝐈𝐀𝐓𝐈𝐎𝐍 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙂𝙤 𝙩𝙝𝙧𝙤𝙪𝙜𝙝 𝙩𝙝𝙚 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙖𝙣𝙙 𝙟𝙤𝙞𝙣 𝙩𝙝𝙚 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮, 𝙞𝙛 𝙞𝙩 𝙙𝙧𝙖𝙬𝙨 𝙮𝙤𝙪𝙧 𝙖𝙩𝙩𝙚𝙣𝙩𝙞𝙤𝙣.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="𝐇𝐀𝐒𝐇𝐈𝐑𝐀  𝐀𝐒𝐒𝐎𝐂𝐈𝐀𝐓𝐈𝐎𝐍", url="https://t.me/Hashira_Association")],
                    [
                    InlineKeyboardButton(text=" ᴜꜱᴇʀ ᴛᴀɢ ", url="https://t.me/Hashira_Association/19"),
                    InlineKeyboardButton(text=" ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ] ", url="https://t.me/omegaruby")
                    ],
                ]
            ),
        )


    hashira_handler = CommandHandler(("hashira", "network", "net"), hashira, run_async = True)
    dispatcher.add_handler(hashira_handler)

    __help__ = """
    ──「@Hashira_Association」──                         
    
    ❂ /net: Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "Hashira_Association"
