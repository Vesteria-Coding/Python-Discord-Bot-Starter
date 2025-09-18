import os
import discord
import time as t
from discord import app_commands, Interaction, Embed

# Setup Credentials
BOT_TOKEN = 'Bot_Token_Here' # Replace With Bot Token

# Setup
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"Bot is ready. Logged in as {client.user} (ID: {client.user.id})")
    await tree.sync()
    for guild in client.guilds:
        print(f"Bot added to guild {guild.name} (ID: {guild.id})")
    print(f'Bot is in {len(client.guilds)} guilds')

# Commands
@tree.command(name="ping", description="sends ping of bot")
async def ping(interaction: discord.Interaction):
    latency = client.latency * 1000  # Convert to ms
    await interaction.response.send_message(f'Pong! `{latency:.2f}ms`', ephemeral=True)

client.run(BOT_TOKEN)
