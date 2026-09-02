import os
import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"SUPERBIRILLO BOT online come {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 SUPERBIRILLO BOT è online!")

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN non configurato")

bot.run(TOKEN)