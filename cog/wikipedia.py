import discord
from discord.ext import commands

import wikipedia

import datetime

wikipedia.set_lang('es')


class WikipediaBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search', aliases=['buscar', 'query'])
    async def search(self, ctx, *, args):
        guild = ctx.guild
        wiki_result = wikipedia.search(args, results=5)
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow(),
            title='Encontré esto:',
            description=f'{wiki_result}'
        )
        embed.set_footer(
            text=guild,
            icon_url=guild.icon_url
        )
        await ctx.send(embed=embed)

    @commands.command(name='summary', aliases=['resumen', 'res', 'summ'])
    async def summary(self, ctx, *, args):
        guild = ctx.guild
        wiki_summary = wikipedia.summary(args, sentences=2)
        wiki_page = wikipedia.page(args)
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow(),
            title='Aquí está tu resumen:',
            description=f'{wiki_summary}'
        )
        embed.add_field(
            name='Enlace',
            value=f'{wiki_page.url}',
            inline=False
        )
        embed.set_footer(
            text=guild,
            icon_url=guild.icon_url
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(WikipediaBot(bot))
