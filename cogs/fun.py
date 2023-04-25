import discord
import random
from discord.ext import commands
import config

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="slap", brief="[Slap a member]", description="Slap a member from server")
    async def slap(self, ctx, member: discord.Member = None):
        if member is not None:
            slap_gifs = random.choice(config.SLAP_GIFS)
            embed = discord.Embed(description=f"{ctx.author.mention} slaps {member.mention}", color=config.EMBED_COLOR)
            embed.set_image(url=slap_gifs)
            await ctx.send(embed=embed)
        else:
            ctx.send("Mention a user to slap!")
    
    @commands.command(name="punch", brief="[Punch a member]", description="Punch a member from server")
    async def punch(self, ctx, member: discord.Member = None):
        if member is not None:
            punch_gifs = random.choice(config.PUNCH_GIFS)
            embed = discord.Embed(description=f"{ctx.author.mention} punches {member.mention}", color=config.EMBED_COLOR)
            embed.set_image(url=punch_gifs)
            await ctx.send(embed=embed)
        else:
            ctx.send("Mention a user to punch!")

    @commands.command(name="kill", brief="[Kill a member(virtually)]", description="Kill a member(virtually) from server")
    async def kill(self, ctx, member: discord.Member = None):
        if member is not None:
            kill_gifs = random.choice(config.KILL_GIFS)
            embed = discord.Embed(description=f"{ctx.author.mention} kills {member.mention}(virtually)", color=config.EMBED_COLOR)
            embed.set_image(url=kill_gifs)
            await ctx.send(embed=embed)
        else:
            ctx.send("Mention a user to kill virtually!")

async def setup(bot):
    await bot.add_cog(Fun(bot))