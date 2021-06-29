import aiohttp
import discord
import cog.functions as f
from discord.ext import commands


TOKEN = f.get_api()


async def covid19_request(country: str):
    url = "https://covid-19-data.p.rapidapi.com/country"
    query = {"name": country}
    headers = {
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, params=query) as r:
            if r.status == 200:
                json_response = await r.json()
                return json_response
            else:
                return


class Covid19(commands.Cog, name='COVID-19',
              description='Información sobre el COVID-19'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(aliases=['cov19', 'c19'],
                      description='Obtén información sobre el estado de un'
                                  ' país frente al COVID-19')
    async def covid19(self, ctx, *, country: str):
        if not country:
            await ctx.send('Necesito que me digas el país del cual quieres'
                           ' conocer su información. **ATENCIÓN**: por'
                           ' motivos externos a RoboTito, necesito que'
                           ' escribas el nombre del país en inglés.')
        else:
            c19 = await covid19_request(country)
            e = discord.Embed(color=f.rbColor(),
                              title=f'COVID-19 >> {c19[0]["country"]}')
            e.add_field(name='Confirmados ⚠️',
                        value=format(c19[0]["confirmed"], ','),
                        inline=False)
            e.add_field(name='Recuperados ☑️',
                        value=format(c19[0]["recovered"], ','),
                        inline=False)
            e.add_field(name='Críticos ❗️',
                        value=format(c19[0]["critical"], ','), inline=False)
            e.add_field(name='Muertes ❌',
                        value=format(c19[0]["deaths"], ','), inline=False)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Covid19(bot))
