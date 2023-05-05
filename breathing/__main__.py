from pyrogram import Client, filters

import os

import jikanpy

# Create a new Pyrogram client object and connect to the Telegram API

app = Client(

    "Obanai_iguru_bot",

    api_id=os.environ.get("API_ID"),

    api_hash=os.environ.get("API_HASH"),

    bot_token=os.environ.get("BOT_TOKEN")

)

# Create a new Jikan API client object

jikan = jikanpy.Jikan()

# Handle the /start command

@app.on_message(filters.command("start"))

def start_handler(client, message):

    client.send_message(message.chat.id, "Hello, I am Obanai iguru Bot!")

# Handle the /anime and /manga commands

@app.on_message(filters.command(["anime", "manga"]))

def anime_handler(client, message):

    query = message.text.split(" ", 1)[1]

    anime = jikan.search("anime", query)["results"][0]

    title = anime["title"]

    synopsis = anime["synopsis"]

    url = anime["url"]

    response = f"{title}\n\n{synopsis}\n\n{url}"

    client.send_message(message.chat.id, response)

# Run the bot

app.run()
