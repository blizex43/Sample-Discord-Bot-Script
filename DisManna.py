# RAM: Discord Bot Project
# Author: [Your Name]
# Description: Discord bot with slash commands for data storage and control.

import discord
from discord.ext import commands
import json
import os
from ram_data_manager import DataManager  # Custom non-built-in module

# Load token from environment or hardcode for testing
TOKEN = os.getenv('DISCORD_BOT_TOKEN') or 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# --- Data Management --- #
data_manager = DataManager("ram_data.json")

# --- Classes --- #
class UserManager:
    def __init__(self):
        self.blacklist = data_manager.get_data("blacklist") or []

    def add_to_blacklist(self, user):
        if user not in self.blacklist:
            self.blacklist.append(user)
            data_manager.save_data("blacklist", self.blacklist)
            return True
        return False

    def is_blacklisted(self, user):
        return user in self.blacklist

class CommandHandler:
    def __init__(self, bot):
        self.bot = bot

    def build_embed(self, title, description, color=discord.Color.blue()):
        embed = discord.Embed(title=title, description=description, color=color)
        return embed

class RAM(UserManager):  # Subclass of UserManager
    def __init__(self, bot):
        super().__init__()
        self.handler = CommandHandler(bot)

    def get_embed_for_blacklist(self, user, success):
        if success:
            return self.handler.build_embed("Blacklist", f"{user} was added to blacklist.")
        else:
            return self.handler.build_embed("Blacklist", f"{user} is already blacklisted.", discord.Color.red())

ram = RAM(bot)

# --- Slash Command Functions --- #
@bot.command()
async def blacklist(ctx, user: str):
    """Adds a user to the blacklist"""
    try:
        success = ram.add_to_blacklist(user)
        embed = ram.get_embed_for_blacklist(user, success)
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def authcmd(ctx, key: str):
    """Authorize a key against stored valid tokens"""
    try:
        keys = data_manager.get_data("auth_keys") or []
        if key in keys:
            embed = ram.handler.build_embed("Authorization", "Access granted ✅")
        else:
            embed = ram.handler.build_embed("Authorization", "Invalid key ❌", discord.Color.red())
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

@bot.command()
async def update(ctx, field: str, value: str):
    """Update a field in config"""
    try:
        config = data_manager.get_data("config") or {}
        config[field] = value
        data_manager.save_data("config", config)
        embed = ram.handler.build_embed("Update", f"{field} updated to {value}")
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Loop through startup logs
@bot.event
async def on_ready():
    print("RAM is online!")
    for guild in bot.guilds:
        print(f"Connected to: {guild.name}")

# Run the bot
bot.run(TOKEN)
