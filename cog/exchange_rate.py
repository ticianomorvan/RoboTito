import discord
import requests
from discord.ext import commands
from cog.functions.functions import Functions as f

TOKEN = f.getToken()


def exchangeRate(cFrom: str, cTo: str):
    url = f"https://exchangerate-api.p.rapidapi.com/rapid/latest/{cFrom}"
    headers = {
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "exchangerate-api.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    jsonResponse = response.json()
    return jsonResponse['rates'][cTo]


class ExchangeRate(commands.Cog, name='Conversión',
                   description='Convierte cantidades'
                               ' de dinero entre monedas.'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='exchange', aliases=['exch', 'convertir', 'conv'],
                      help='Convierte una cantidad de dinero'
                           ' entre dos monedas.')
    async def exchangeCommand(self, ctx, cFrom: str,
                              cTo: str, amount: int = None):
        fromCurrency = str.upper(cFrom)
        toCurrency = str.upper(cTo)
        exchange = float(exchangeRate(fromCurrency, toCurrency))

        if amount is not None:
            result = round(exchange * amount)
            e = discord.Embed(
                color=discord.Color.from_rgb(
                    f.rColor(), f.rColor(), f.rColor()),
                )
            e.set_author(
                name='Conversión de monedas',
                icon_url='https://cdn0.iconfinder.com/data/icons/'
                         'business-cool-vector-3/128/120-512.png',
                url='https://rapidapi.com/exchangerateapi/api/'
                    'exchangerate-api/'
            )
            e.add_field(
                name=f'La conversión de ${amount} {fromCurrency}'
                     f' a {toCurrency} es:',
                value=f'${result} {toCurrency}, a fecha de hoy.'
            )
            await ctx.send(embed=e)

        else:
            e = discord.Embed(
                color=discord.Color.from_rgb(
                    f.rColor(), f.rColor(), f.rColor()),
                )
            e.set_author(
                name='Tasa de cambio',
                icon_url='https://cdn0.iconfinder.com/data/icons/'
                         'business-cool-vector-3/128/120-512.png',
                url='https://rapidapi.com/exchangerateapi/api/'
                    'exchangerate-api/'
            )
            e.add_field(
                name=f'Por cada $1 {fromCurrency}, deberás pagar:',
                value=f'${exchange} {toCurrency}, a fecha de hoy.'
            )
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(ExchangeRate(bot))
