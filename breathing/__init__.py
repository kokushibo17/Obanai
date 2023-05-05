from pyrogram import Client

import os

# Create a new Pyrogram client object and connect to the Telegram API

app = Client(

    "Obanai_iguru_bot",

    api_id=os.environ.get("API_ID"),

    api_hash=os.environ.get("API_HASH"),

    bot_token=os.environ.get("BOT_TOKEN")

)

if not os.path.exists("downloads"):

    os.makedirs("downloads")

if __name__ == '__main__':

    # Import the event handlers from the handlers.py file

    from handlers import *

    # Run the bot

    app.run()
