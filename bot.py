import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import discord
from discord.ext import commands


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SUPERBIRILLO BOT online")

    def log_message(self, format, *args):
        return


def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"SUPERBIRILLO BOT online come {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("📌 SUPERBIRILLO BOT è online!")


TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN non configurato")


threading.Thread(target=run_health_server, daemon=True).start()

bot.run(TOKEN)