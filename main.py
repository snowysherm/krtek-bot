import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
activity = discord.Game(name='Ahoj!')
client = discord.Client(activity=activity, intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@client.event
async def on_message(message):
    if "hey" in message.content.lower():
        await message.channel.send(f"<@!{1}>")


@bot.command()
async def test(ctx, arg):
    count = 0
    while count >= arg + 1:
        await ctx.send("123")


client.run(DISCORD_TOKEN)
