import aiohttp
import discord
from discord.ext import commands
from cog.functions.functions import Functions as f


TOKEN = f.getToken()


class Covid19(commands.Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='covid19', aliases=['cov19', 'c19'],
                      description='Obtén información sobre el estado de un'
                                  ' país frente al COVID-19')
    async def covid19_command(self, ctx, *, country: str):
        url = "https://covid-19-data.p.rapidapi.com/country"
        query = {"name": country}
        headers = {
            'x-rapidapi-key': TOKEN,
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
            }

        async with aiohttp.ClientSession() as session:
            async with session.get(url=url,
                                   headers=headers, params=query) as response:
                if response.status == 200:
                    jsonResponse = await response.json()
                    countryName = jsonResponse[0]['country']
                    confirmedCases = jsonResponse[0]['confirmed']
                    recoveredCases = jsonResponse[0]['recovered']
                    criticalCases = jsonResponse[0]['critical']
                    deaths = jsonResponse[0]['deaths']

                    e = discord.Embed(color=f.rbColor(),
                                      title=f'COVID-19 >> {countryName}')
                    e.add_field(name='Confirmados ⚠️',
                                value=format(confirmedCases, ','),
                                inline=False)
                    e.add_field(name='Recuperados ☑️',
                                value=format(recoveredCases, ','),
                                inline=False)
                    e.add_field(name='Críticos ❗️',
                                value=format(criticalCases, ','), inline=False)
                    e.add_field(name='Muertes ❌',
                                value=format(deaths, ','), inline=False)
                    await ctx.send(embed=e)

                else:
                    await ctx.send('Hubo un problema en la comunicación'
                                   ' con la API.')


def setup(bot):
    bot.add_cog(Covid19(bot))
