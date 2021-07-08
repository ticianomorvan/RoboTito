import discord
import json
import tomli
import wikipedia
import wikipediaapi
import asyncio
from aiohttp import ClientSession
from random import randint
from discord.ext import commands
from cog.functions import rbColor
from translate import Translator
from datetime import datetime, timedelta, timezone

timezone_icon = '''
https://cdn.discordapp.com/avatars/447266583459528715/bc6d8794326ef2fd57690a852eefde1b.png?size=512
'''


class Utility(commands.Cog, name='Utilidad',
              description='Comandos útiles y variados.'):

    def __init__(self, bot):
        self.bot = bot

    def open_config():
        with open('databases/config.toml', encoding='utf-8') as f:
            config_data = tomli.load(f)
            return config_data

    def get_rapidapi():
        """Returns the token for RapidApi related commands."""
        config = Utility.open_config()
        token = config['rapidapi']
        return token

    def get_cuttly():
        """Returns the token for URL shortener."""
        config = Utility.open_config()
        token = config['cuttly']
        return token

    # APIs Commands

    @commands.command(aliases=['cov19'],
                      help='Información sobre el COVID-19 en un país.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def covid19(self, ctx, *, country: str):

        async def covid19_request(country: str):
            """Returns information about a desired country."""

            url = "https://covid-19-data.p.rapidapi.com/country"
            query = {"name": country}
            headers = {'x-rapidapi-key': Utility.get_rapidapi(),
                       'x-rapidapi-host': "covid-19-data.p.rapidapi.com"}

            async with ClientSession() as session:
                async with session.get(url=url, headers=headers,
                                       params=query) as r:
                    if r.status == 200:
                        json_response = await r.json()
                        return json_response
                    else:
                        return

        if not country:
            await ctx.send('Necesito que me digas el país del cual quieres'
                           ' conocer su información. **ATENCIÓN**: por'
                           ' motivos externos a RoboTito, necesito que'
                           ' escribas el nombre del país en inglés.')
        else:
            c19 = await covid19_request(country)
            e = discord.Embed(color=rbColor(),
                              title=f'COVID-19: {c19[0]["country"]}')
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

    @commands.command(aliases=['exch', 'convertir', 'conv'],
                      help='Convierte una cantidad de dinero'
                           ' entre dos monedas.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def exchange(self, ctx, currency_from: str,
                       currency_to: str, amount: int = None):

        async def exchangeRate(cFrom: str, cTo: str):
            u = f'https://exchangerate-api.p.rapidapi.com/rapid/latest/{cFrom}'
            headers = {'x-rapidapi-key': Utility.get_rapidapi(),
                       'x-rapidapi-host': "exchangerate-api.p.rapidapi.com"}
            async with ClientSession() as session:
                async with session.get(url=u, headers=headers) as r:
                    if r.status == 200:
                        json_response = await r.json()
                        return json_response['rates'][cTo]
                    else:
                        return

        fromCurrency = str.upper(currency_from)
        toCurrency = str.upper(currency_to)
        exchange = float(await exchangeRate(fromCurrency, toCurrency))

        if amount is not None:
            result = round(exchange * amount)
            e = discord.Embed(color=rbColor())
            e.set_author(name='Conversión de monedas',
                         icon_url='https://cdn0.iconfinder.com/data/icons/'
                                  'business-cool-vector-3/128/120-512.png',
                         url='https://rapidapi.com/exchangerateapi/api/'
                             'exchangerate-api/')
            e.add_field(name=f'La conversión de ${amount} {fromCurrency}'
                             f' a {toCurrency} es:',
                        value=f'${result} {toCurrency}, a fecha de hoy.')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.set_author(name='Tasa de cambio',
                         icon_url='https://cdn0.iconfinder.com/data/icons/'
                                  'business-cool-vector-3/128/120-512.png',
                         url='https://rapidapi.com/exchangerateapi/api/'
                             'exchangerate-api/')
            e.add_field(name=f'Por cada $1 {fromCurrency}, deberás pagar:',
                        value=f'${exchange} {toCurrency}, a fecha de hoy.')
            await ctx.send(embed=e)

    @commands.command(aliases=['img', 'bing', 'imagen'],
                      help='Obtén una imagen desde el motor de búsqueda Bing.')
    @commands.cooldown(1, 2.5, commands.BucketType.user)
    async def searchimage(self, ctx, *, query: str):

        async def search_image(query: str):
            url = "https://bing-image-search1.p.rapidapi.com/images/search"
            querystring = {"q": query, "mkt": "es-AR", "count": "30"}
            headers = {
                'x-rapidapi-key': Utility.get_rapidapi(),
                'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
                }
            async with ClientSession() as session:
                async with session.get(url=url, headers=headers,
                                       params=querystring) as r:
                    if r.status == 200:
                        json_response = await r.json()
                        index = randint(0, 30)
                        return json_response['value'][index]['contentUrl']
                    else:
                        return

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

    @commands.command(name='urlshortener', aliases=['acortador', 'urlshort'],
                      help='Acorta URLs')
    @commands.cooldown(1, 7.5, commands.BucketType.user)
    async def url_shortener(self, ctx, *, url):

        async def shortener_api(request: str):
            key = Utility.get_cuttly()
            url = request
            api_url = f'https://cutt.ly/api/api.php?key={key}&short={url}'
            async with ClientSession() as session:
                async with session.post(url=api_url) as r:
                    if r.status == 200:
                        json_response = await r.json()
                        return json_response
                    else:
                        pass

        link = await shortener_api(url)
        e = discord.Embed(color=rbColor())
        e.add_field(name=link['url']['title'], value=link['url']['shortLink'])
        await ctx.send(embed=e)

    # Translate

    @commands.command(aliases=['traducir', 'tte'],
                      help='¡Traduce oraciones!')
    @commands.cooldown(1, 3.5, commands.BucketType.user)
    async def translate(self, ctx, fromlang, tolang, *, args: str):

        file = discord.File('assets/github_512x512.png', 'image.png')

        def language_translate(language):
            with open('databases/db_languages.json', encoding='utf-8') as f:
                data = f.read()
                lang = json.loads(data)
                if language in lang:
                    codename = lang[language]['codename']
                    return codename
                else:
                    pass

        def language_embed(word, translation, fromlang, tolang):
            e = discord.Embed(title=translation,
                              description=f'La traducción de "{word}" del '
                                          f'**{fromlang}** al **{tolang}**'
                                          f' es {translation}.',
                              color=rbColor())
            e.set_footer(text='translate-python, por Terry Yin',
                         icon_url='attachment://image.png')
            return e

        fl = language_translate(str.lower(fromlang))
        if fl is None:
            await ctx.send(f'"{fromlang}" no es un idioma o'
                           ' no puedo reconocerlo.')
        else:
            tl = language_translate(str.lower(tolang))
            if tl is None:
                await ctx.send(f'"{tolang}" no es un idioma'
                               ' o no puedo reconocerlo.')
            else:
                translator = Translator(from_lang=fl, to_lang=tl)
                translation = translator.translate(args)
                e = language_embed(args, translation, fromlang, tolang)
                await ctx.send(embed=e, file=file)

    # Wikipedia

    @commands.command(name='wikipedia',
                      aliases=['wiki', 'buscar', 'search'],
                      help='Realiza una búsqueda en Wikipedia.')
    async def wikipedia_search(self, ctx, *, args):

        wikipedia.set_lang('es')

        wiki = wikipediaapi.Wikipedia('es')

        wiki_logo = """
        https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Wikipedia_svg_logo.svg/1200px-Wikipedia_svg_logo.svg.png
        """

        def get_summary(page):
            p = page.summary.split('.')
            sentences = f'{p[0]}. {p[1]}. {p[2]}. {p[3]}. {p[4]}.'
            return sentences

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

    # Time

    def get_local_time(hours):
        time = str(datetime.now(timezone(timedelta(hours=hours))))[10:][:6]
        return time

    @commands.command(aliases=['utc', 'greenwich'],
                      help='Conoce la hora (del meridiano de Greenwich)')
    async def utctime(self, ctx):
        e = discord.Embed(title=f'Son las{str(datetime.utcnow())[10:][:6]}'
                                ' (UTC)',
                          color=rbColor())
        e.set_author(name='Tiempo del meridiano de Greenwich',
                     url='https://time.is/es/UTC',
                     icon_url=timezone_icon)
        await ctx.send(embed=e)

    @commands.command(aliases=['tiempodelbot', 'bothour'],
                      help='Conoce la hora de la región del bot.')
    async def bottime(self, ctx):
        e = discord.Embed(title=f'Son las{str(datetime.now())[10:][:6]}',
                          color=rbColor())
        e.set_author(name='Tiempo de la zona horaria del bot',
                     icon_url=timezone_icon)
        await ctx.send(embed=e)

    @commands.command(aliases=['tiempolocal', 'local'],
                      help='Conoce la hora de tu zona horaria.')
    async def localtime(self, ctx, hours: int = None):
        if not hours:
            await ctx.send('Para averiguar la hora de tu zona horaria,'
                           ' ingresá la cantidad de horas de diferencia'
                           ' con el tiempo del meridiano de Greenwich.'
                           ' Por ejemplo, para Argentina (UTC -3)'
                           ' ingresá `-3` después del comando.')
        else:
            e = discord.Embed(title=f'Son las{Utility.get_local_time(hours)}',
                              color=rbColor())
            e.set_author(name='Tiempo de tu zona horaria',
                         icon_url=timezone_icon)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Utility(bot))
