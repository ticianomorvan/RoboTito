import requests
import discord
from cog.functions.functions import Functions as f
from datetime import datetime
from discord.ext import commands


TOKEN = f.getToken()


def searchImage(query: str):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    querystring = {"q": query, "mkt": "es-AR", "count": "1"}
    headers = {
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers,
                                params=querystring)
    jsonResponse = response.json()
    return jsonResponse['value'][0]['contentUrl']


class ImageSearch(commands.Cog, name='Imágenes',
                  description='¡Obtén imágenes desde internet!'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='searchimg', aliases=['img', 'bing', 'imagen'],
                      help='Obtén una imagen desde el motor de búsqueda Bing.')
    async def searchImage(self, ctx, *, query: str):
        e = discord.Embed(
            color=discord.Color.from_rgb(f.rColor(), f.rColor(), f.rColor()),
            timestamp=datetime.utcnow(),
            description=f'**{query}**, enlace original:'
                        f' [aquí]({searchImage(query)})'
        )
        e.set_author(name='Imágenes de Bing',
                     icon_url='https://pluspng.com/img-png/'
                              'bing-logo-png-png-ico-512.png')
        e.set_image(url=searchImage(query))
        e.set_footer(text=f'Imagen pedida por {ctx.author.name}',
                     icon_url=ctx.guild.icon_url)

        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(ImageSearch(bot))
