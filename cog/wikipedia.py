import discord
import wikipedia
import wikipediaapi
import asyncio
from cog.functions import rbColor
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

    @commands.command(name='wikipedia',
                      aliases=['wiki', 'buscar', 'search'],
                      help='Realiza una búsqueda en Wikipedia.')
    async def wikipedia_search(self, ctx, *, args):
        result = wikipedia.search(args, results=10)
        embed = discord.Embed(color=rbColor())
        embed.set_thumbnail(url=wiki_logo)
        embed.add_field(name='Estos fueron los resultados de tu búsqueda:',
                        value=f'1. **{result[0]}**\n2. **{result[1]}**\n'
                              f'3. **{result[2]}**\n4. **{result[3]}**\n'
                              f'5. **{result[4]}**\n6. **{result[5]}**\n'
                              f'7. **{result[6]}**\n8. **{result[7]}**\n'
                              f'9. **{result[8]}**\n10. **{result[9]}**',
                        inline=False)
        embed.set_footer(text='Escribe el número correspondiente'
                              'al artículo que deseas obtener.')
        await ctx.send(embed=embed)

        def is_author(m):
            return m.author == ctx.author

        try:
            selected_page = await self.bot.wait_for('message', check=is_author,
                                                    timeout=45.0)
        except asyncio.TimeoutError:
            await ctx.send('Tu petición expiró.')

        else:
            index = int(selected_page.content) - 1
            page = wiki.page(result[index])
            e = discord.Embed(color=rbColor(), title=page.title,
                              description=get_summary(page))
            e.set_author(name=f'{page.title} en Wikipedia',
                         url=page.canonicalurl)
            e.set_thumbnail(url=wiki_logo)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(WikipediaBot(bot))
