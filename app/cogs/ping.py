import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        # ctx: Context 
        await ctx.send("pong!")

    @commands.command()
    async def greet(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Hi!" + ctx.author.mention)
        else:
            await ctx.send("Hi!" + member.mention)


async def setup(bot):
    await bot.add_cog(Ping(bot))
