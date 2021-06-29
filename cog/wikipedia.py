import discord
import wikipedia
import wikipediaapi
import cog.functions as f
from discord.ext import commands


wikipedia.set_lang('es')

wiki = wikipediaapi.Wikipedia('es')

wiki_logo = """
https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/1200px-Wikipedia_svg_logo.svg.png
"""


def get_summary(page):
    split = page.summary.split('.')
    sentences = f'{split[0]}. {split[1]}. {split[2]}. {split[3]}. {split[4]}.'
    return sentences


class WikipediaBot(commands.Cog,
                   name='Wikipedia',
                   description='Obtén la información que '
                               'necesitas de Wikipedia.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='search',
                      aliases=['buscar', 'query'],
                      help='Realiza una búsqueda en Wikipedia.')
    async def wiki_query(self, ctx, *, args):
        result = wikipedia.search(args, results=10)
        embed = discord.Embed(color=f.rbColor())
        embed.set_thumbnail(url=wiki_logo)
        embed.add_field(name='Estos fueron los resultados de tu búsqueda:',
                        value=f'1. **{result[0]}**\n2. **{result[1]}**\n'
                              f'3. **{result[2]}**\n4. **{result[3]}**\n'
                              f'5. **{result[4]}**\n6. **{result[5]}**\n'
                              f'7. **{result[6]}**\n8. **{result[7]}**\n'
                              f'9. **{result[8]}**\n10. **{result[9]}**',
                        inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='summary',
                      aliases=['resumen', 'summ'],
                      help='Obtén el resumen de algún artículo.')
    async def wiki_summary(self, ctx, *, args):
        wiki_page = wiki.page(args)

        if wiki_page.exists() is True:
            embed = discord.Embed(color=f.rbColor(), title=wiki_page.title,
                                  description=get_summary(wiki_page))
            embed.set_author(name=f'{wiki_page.title} en Wikipedia',
                             url=wiki_page.canonicalurl)
            embed.set_thumbnail(url=wiki_logo)
            await ctx.send(embed=embed)

        else:
            await ctx.send('Esa página no existe, por favor, '
                           'inténtalo de nuevo.')


def setup(bot):
    bot.add_cog(WikipediaBot(bot))
