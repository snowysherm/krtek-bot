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


def medal_url(id=None):
    global r
    headers = {"Authorization": MEDAL_API}
    if id:
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000&categoryId={id}',
            headers=headers)
    elif not id:
        r = requests.get(
            f'https://developers.medal.tv/v1/latest?userId=50766636&limit=1000',
            headers=headers)

    return r.json()


@bot.command()
async def clip(ctx, game=None):
    global response
    if game == "swtor":
        response = medal_url(165)
    elif game == "hunt":
        response = medal_url(947)
    elif not game:
        response = medal_url()

    length = len(response["contentObjects"])
    await ctx.send(response["contentObjects"][random.randint(0, int(length))]["directClipUrl"])


@bot.command()
async def stefan(ctx, arg):
    count = 0
    while count < int(arg):
        await ctx.send(f"<@!{245656082423218187}>")
        count += 1


bot.run(DISCORD_TOKEN)
