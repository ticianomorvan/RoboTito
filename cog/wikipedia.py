import discord
from discord.ext import commands

import wikipedia

import wikipediaapi

import datetime

# Wikipedia language and some useful variables.

wikipedia.set_lang('es')

wiki = wikipediaapi.Wikipedia('es')

color = discord.Color.blue()

time = datetime.datetime.utcnow()

file = discord.File('images/Wikipedia.png', filename='image.png')


class WikipediaBot(commands.Cog,
                   name='Wikipedia',
                   description='Obtén la información que '
                               'necesitas de Wikipedia.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search',
                      aliases=['buscar', 'query'],
                      description='Realiza una búsqueda en Wikipedia.')
    async def wiki_query(self, ctx, *, args):
        g = ctx.guild
        wiki_result = wikipedia.search(args, results=5)

        embed = discord.Embed(color=color,
                              timestamp=color)
        embed.set_thumbnail(url='attachment://image.png')
        embed.add_field(name='Estos fueron los resultados de tu búsqueda:',
                        value=wiki_result,
                        inline=False)
        embed.set_footer(text=g, icon_url=g.icon_url)

        await ctx.send(embed=embed, file=file)

    @commands.command(name='summary',
                      aliases=['resumen', 'summ'],
                      description='Obtén el resumen de algún artículo.')
    async def wiki_summary(self, ctx, *, args):
        g = ctx.guild
        wiki_page = wiki.page(args)
        split = wiki_page.summary.split('.')
        sentences = split[0] + '.' + split[1] + '.' + split[2] + '.'

        if wiki_page.exists() is True:
            embed = discord.Embed(color=color,
                                  timestamp=time)
            embed.set_thumbnail(url='attachment://image.png')
            embed.add_field(name=wiki_page.title,
                            value=sentences,
                            inline=False)
            embed.add_field(name='Para visitar el artículo original visita:',
                            value=f'[{wiki_page.title} en Wikipedia]'
                                  f'({wiki_page.canonicalurl})')
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed, file=file)

        else:
            await ctx.send('Esa página no existe, por favor, '
                           'inténtalo de nuevo.')


def setup(bot):
    bot.add_cog(WikipediaBot(bot))
