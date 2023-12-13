import discord
import os
import random
from medal import medal_api
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
activity = discord.Game(name='Ahoj!')
bot = commands.Bot(command_prefix='$', intents=intents, activity=activity)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@bot.command()
async def stefan(ctx, arg):
    count = 0
    while count < int(arg):
        await ctx.send(f"<@!{245656082423218187}>")
        count += 1


@bot.tree.command(name="ping", description="ping", guild=discord.Object(
    id=698964831671156907))
async def first_command(interaction, game: str = None):
    global response
    if game == "swtor":
        response = medal_api(165)
    elif game == "hunt":
        response = medal_api(947)
    elif not game:
        response = medal_api()

    length = len(response["contentObjects"])
    await interaction.response.send_message(response["contentObjects"][random.randint(0, int(length))]["directClipUrl"])


# Sync slash commands


@bot.command()
async def sync(ctx):
    if ctx.author.id == 418731919438643212:
        await bot.tree.sync(guild=discord.Object(id=698964831671156907))
        await ctx.send("Synced!")
    else:
        await ctx.send("No permission")


# Delete slash commands


@bot.command()
async def delete(ctx):
    if ctx.author.id == 418731919438643212:
        bot.tree.clear_commands(guild=None)
        await bot.tree.sync()
        await ctx.send('Commands deleted.')
    else:
        await ctx.send("No permission")


bot.run(DISCORD_TOKEN)
