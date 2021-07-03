import aiohttp
import discord
import random
from cog.functions import rbColor, get_api
from discord.ext import commands


TOKEN = get_api()


async def search_image(query: str):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    querystring = {"q": query, "mkt": "es-AR", "count": "30"}
    headers = {
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers,
                               params=querystring) as r:
            if r.status == 200:
                json_response = await r.json()
                index = random.randint(0, 30)
                return json_response['value'][index]['contentUrl']
            else:
                return


class ImageSearch(commands.Cog, name='Imágenes',
                  description='¡Obtén imágenes desde internet!'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(aliases=['img', 'bing', 'imagen'],
                      help='Obtén una imagen desde el motor de búsqueda Bing.')
    async def searchimage(self, ctx, *, query: str):
        if not query:
            await ctx.send('Tienes que buscar algo.')
        else:
            e = discord.Embed(
                color=rbColor(),
                description=f'**{query}**, enlace original:'
                            f' [aquí]({await search_image(query)})'
            )
            e.set_author(name='Imágenes de Bing',
                         icon_url='https://pluspng.com/img-png/'
                                  'bing-logo-png-png-ico-512.png')
            e.set_image(url=await search_image(query))
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(ImageSearch(bot))
