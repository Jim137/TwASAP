import csv
import os
import sys

import discord
from discord.ext import commands

from TwASAP.twitter import get_status

token = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    with open("id.csv", "r") as f:
        reader = csv.reader(filter(lambda row: row[0] != "#", f))
        for row in reader:
            Twitter_user_ID = row[0]
            Discord_channel_ID = int(row[1])
            status = get_status([Twitter_user_ID])
            if status is not None:
                channel = bot.get_channel(Discord_channel_ID)
                send = status["full_text"] + "\n\n"
                try:
                    for media in status["extended_entities"]["media"]:
                        send += media["media_url"] + "\n"
                except KeyError:
                    pass
                await channel.send(send)
    await bot.close()


bot.run(token)
sys.exit(0)
