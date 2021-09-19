""" Module Imports """
# import discord as disc
from discord.ext import commands


class Misc(commands.Cog):
    """DigiBot Misc Features"""

    def __init__(self, client: commands.bot.Bot) -> None:
        """Constructor for Misc Cog"""
        self._client: commands.bot.Bot = client

    @commands.command()
    async def best_portfolio(self, ctx: commands.context.Context) -> None:
        """What is the best portfolio?"""
        await ctx.reply(content="IT!")

    @commands.command()
    async def best_bot(self, ctx: commands.context.Context) -> None:
        """What is the best bot?"""
        await ctx.reply(content="That's me, DigiBot!")

    @commands.command()
    async def axie(self, ctx: commands.context.Context) -> None:
        """Shameless plug"""
        await ctx.reply("https://github.com/axieax/")

    @commands.command()
    async def website(self, ctx: commands.context.Context) -> None:
        """DigiSoc website"""
        await ctx.reply("https://unswdigitalsociety.org/")

    @commands.command()
    async def discord(self, ctx: commands.context.Context) -> None:
        """DigiSoc Community Discord"""
        await ctx.reply("https://unswdigitalsociety.org/discord/")

    @commands.command()
    async def admin(self, ctx: commands.context.Context) -> None:
        """DigiSoc IT Admin Panel"""
        await ctx.reply("https://unswdigitalsociety.org/admin/")


def setup(client: commands.bot.Bot) -> None:
    client.add_cog(Misc(client))