import discord
from discord.ext import commands
import config

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add role", brief="[Add a role]", description="Add a role to a mentioned user")
    @commands.has_any_role(config.MODERATOR)
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        member.add_roles(role)
        await ctx.send(f"Added <@&{role.id}> to <@{member.id}>")

    @commands.command(name="remove role", brief="[Remove a role]", description="Remove a role from a mentioned user")
    @commands.has_any_role(config.MODERATOR)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        member.remove_roles(role)
        await ctx.send(f"Removed <@&{role.id}> from <@{member.id}>")

async def setup(bot):
    await bot.add_cog(Moderator(bot))