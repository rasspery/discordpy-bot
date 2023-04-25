import discord
from discord.ext import commands
import config

prefix = config.PREFIX
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord.py")) # Add custom status in name="..."

    for cog_file in config.COGS_DIR.glob("*.py"):
        if cog_file.name != "__init__.py":
            await bot.load_extension(f"cogs.{cog_file.name[:-3]}")

@bot.command()
async def ping(ctx):
    """ Shows bot ping """
    await ctx.send(f"Bot Ping: {round(bot.latency * 1000)}ms")

bot.run(config.TOKEN)