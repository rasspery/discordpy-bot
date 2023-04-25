import discord
from discord.ext import commands
import config

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar", brief="[Fetch avatar]", description="Fetch a member's avatar", aliases=["av", "pfp"])
    async def avatar(self, ctx, member: discord.Member=None):
        member = ctx.author
        embed = discord.Embed(color=config.EMBED_COLOR)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar.url)
        embed.set_image(url=member.avatar.url)
        embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="userinfo", brief="[User Infomation]", description="Fetch a member's Information", aliases=["user", "whois"])
    async def userinfo(self, ctx, member: discord.Member=None):
        member = ctx.author
        embed = discord.Embed(color=config.EMBED_COLOR)
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=member.avatar.url)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Created At", value=discord.utils.format_dt(member.created_at), inline=False)
        embed.add_field(name="Joined At", value=discord.utils.format_dt(member.joined_at), inline=False)
        embed.add_field(name="Avatar URL", value=f"[1024x1024]({member.avatar.url})", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo", brief="[Server Infomation]", description="Fetch server's Information", aliases=["guild"])
    async def userinfo(self, ctx):
        guild = ctx.guild
        desc = ctx.guild.description
        if desc is None:
            desc = "None"
        embed = discord.Embed(color=config.EMBED_COLOR)
        embed.add_field(name="Owner", value=f"<@{guild.owner_id}>", inline=False)
        embed.add_field(name="Description", value=desc, inline=False)
        embed.add_field(name="ID", value=guild.id, inline=False)
        embed.add_field(name="Created At", value=discord.utils.format_dt(guild.created_at), inline=False)
        embed.add_field(name="Guild Icon URL", value=f"[1024x1024]({guild.icon.url})", inline=False)
        embed.set_thumbnail(url=guild.icon.url)
        embed.set_footer(text=f"Requested by: {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Information(bot))