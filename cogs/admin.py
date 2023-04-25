import discord
from discord.ext import commands
import config

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick", brief="[Kick a member]", description="Kick a member from server")
    @commands.has_any_role(config.ADMIN)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None):
        if member is not None:
            await member.kick()
            await ctx.send(f"✅ Kicked {member.name}")
        else:
            await ctx.send("Mention a user to kick!")

    @commands.command(name="ban", brief="[Ban a member]", description="Ban a member from server")
    @commands.has_any_role(config.ADMIN)
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member=None):
        if member is not None:
            await member.ban()
            await ctx.send(f"✅ Banned {member.name}")
        else:
            await ctx.send("Mention a user to ban!")

async def setup(bot):
    await bot.add_cog(Admin(bot))