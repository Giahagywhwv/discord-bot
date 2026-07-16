import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN) 
