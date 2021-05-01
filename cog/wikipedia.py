import discord
from discord.ext import commands

import wikipedia

import wikipediaapi

import datetime

wikipedia.set_lang('es')

wiki = wikipediaapi.Wikipedia('es')


class WikipediaBot(
    commands.Cog,
    name='Wikipedia',
    description='Obtén la información que necesitas de Wikipedia.'
):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search', aliases=['buscar', 'query'])
    async def wiki_query(self, ctx, *, args):
        wiki_result = wikipedia.search(args, results=5)
        file = discord.File('images/Wikipedia.png')

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow(),
        )
        embed.set_thumbnail(
            url='attachment://Wikipedia.png',
        )
        embed.add_field(
            name='Estos fueron los resultados de tu búsqueda:',
            value=wiki_result,
            inline=False
        )
        embed.set_footer(
            text=ctx.guild,
            icon_url=ctx.guild.icon_url
        )
        await ctx.send(embed=embed, file=file)

    @commands.command(name='summary', aliases=['resumen', 'summ'])
    async def wiki_summary(self, ctx, *, args):
        wiki_page = wiki.page(args)
        split = wiki_page.summary.split('.')
        sentences = split[0] + '.' + split[1] + '.' + split[2] + '.'
        file = discord.File('images/Wikipedia.png')

        if wiki_page.exists() is True:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.set_thumbnail(
                url='attachment://Wikipedia.png'
            )
            embed.add_field(
                name=wiki_page.title,
                value=sentences,
                inline=False,
            )
            embed.add_field(
                name='Para visitar el artículo original visita:',
                value=f'[{wiki_page.title} en Wikipedia]'
                      f'({wiki_page.canonicalurl})'
            )
            embed.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url,
            )
            await ctx.send(embed=embed, file=file)

        else:
            await ctx.send('Esa página no existe, por favor, '
                           'inténtalo de nuevo.')


def setup(bot):
    bot.add_cog(WikipediaBot(bot))
