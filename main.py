import discord
import os
import requests
import random
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
activity = discord.Game(name='Ahoj!')
bot = commands.Bot(command_prefix='$', intents=intents, activity=activity)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MEDAL_API = os.getenv("MEDAL_API")


@bot.command()
async def clip(ctx, game=None):
    global response
    headers = {"Authorization": MEDAL_API}

    if game == "swtor":
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000&categoryId=165',
            headers=headers)
        response = r.json()
    elif game == "hunt":
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000&categoryId=947',
            headers=headers)
        response = r.json()
    elif not game:
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000',
            headers=headers)
        response = r.json()

    length = len(response["contentObjects"])
    await ctx.send(response["contentObjects"][random.randint(0, int(length))]["directClipUrl"])


@bot.command()
async def stefan(ctx, arg):
    count = 0
    while count < int(arg):
        await ctx.send(f"<@!{245656082423218187}>")
        count += 1


bot.run(DISCORD_TOKEN)
