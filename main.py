import discord
import os
import requests
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
async def clip(ctx):
    headers = {"Authorization": MEDAL_API}
    r = requests.get(
        "https://developers.medal.tv/v1/latest?userId=50766636&limit=1",
        headers=headers)
    response = r.json()
    await ctx.send(response["contentObjects"][0]["directClipUrl"])


@bot.command()
async def stefan(ctx, arg):
    count = 0
    while count < int(arg):
        await ctx.send(f"<@!{245656082423218187}>")
        count += 1


bot.run(DISCORD_TOKEN)
