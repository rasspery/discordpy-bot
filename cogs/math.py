import discord
from discord.ext import commands

class Mathematics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add", brief="[Add two numbers]", description="Add two numbers", aliases=["addition", "plus"])
    async def add(self, ctx, one: int = commands.parameter(default=1, description="1st operator"), two: int = commands.parameter(default=2, description="2nd operator")):
        await ctx.send(f"{one} + {two} = {one + two}")
    
    @commands.command(name="sub", brief="[Subtract two numbers]", description="Subtract two numbers", aliases=["subtract", "minus"])
    async def sub(self, ctx, one: int = commands.parameter(default=1, description="1st operator"), two: int = commands.parameter(default=2, description="2nd operator")):
        await ctx.send(f"{one} - {two} = {one - two}")

    @commands.command(name="mul", brief="[Multiply two numbers]", description="Multiply two numbers", aliases=["multiply"])
    async def mul(self, ctx, one: int = commands.parameter(default=1, description="1st operator"), two: int = commands.parameter(default=2, description="2nd operator")):
        await ctx.send(f"{one} * {two} = {one * two}")

    @commands.command(name="div", brief="[Divide two numbers]", description="Divide two numbers", aliases=["division"])
    async def div(self, ctx, one: int = commands.parameter(default=1, description="1st operator"), two: int = commands.parameter(default=2, description="2nd operator")):
        await ctx.send(f"{one} / {two} = {one / two}")

async def setup(bot):
    await bot.add_cog(Mathematics(bot))