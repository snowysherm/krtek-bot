import discord
import os
from discord import app_commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@client.event
async def on_ready():
    print('Ready!')


@client.event
async def on_message(message):
    if "test" in message.content.lower():
        await message.channel.send(f"<@!{238045757020569601}>")


@tree.command(name="stefan", description="Stefan Ping Command", guild=discord.Object(
    id=698964831671156907))
async def first_command(interaction):
    await interaction.response.send_message(f"<@!{245656082423218187}>")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=698964831671156907))
    print("Ready!")

client.run(DISCORD_TOKEN)
