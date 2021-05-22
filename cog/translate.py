import asyncio

import discord
from discord.ext import commands

from translate import Translator

import datetime

import json

# Remaking in progress

with open('databases/iso639-1/db_iso639-1.json', encoding='utf-8') as f:
    data = f.read()
    lang = json.loads(data)

with open('databases/db_ttlocales.json') as f2:
    data2 = f2.read()
    locales = json.loads(data2)


def language(message):
    if message in lang['afrikaans']:
        langcode = 'af'
        return langcode
    elif message in lang['arabic']:
        langcode = 'ar'
        return langcode
    elif message in lang['belarusian']:
        langcode = 'be'
        return langcode
    elif message in lang['bulgarian']:
        langcode = 'bg'
        return langcode
    elif message in lang['bosnian']:
        langcode = 'bs'
        return langcode
    elif message in lang['catalan']:
        langcode = 'ca'
        return langcode
    elif message in lang['czech']:
        langcode = 'cs'
        return langcode
    elif message in lang['welsh']:
        langcode = 'cy'
        return langcode
    elif message in lang['danish']:
        langcode = 'da'
        return langcode
    elif message in lang['german']:
        langcode = 'de'
        return langcode
    elif message in lang['greek']:
        langcode = 'el'
        return langcode
    elif message in lang['english']:
        langcode = 'en'
        return langcode
    else:
        if message in locales['languages']:
            return message


class Translate(commands.Cog,
                name='Traductor',
                description='¡Traduce en más de 180 idiomas!'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='translate',
                      aliases=['tr', 'tte'],
                      description='Traduce paso a paso.')
    async def translate_normal(self, ctx, extra=None):
        file = discord.File('images/Translate.png', filename='image.png')

        if extra == 'help':
            embed = discord.Embed(title='Ayuda sobre las traducciones',
                                  color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url='attachment://Translate.png')
            embed.add_field(name='Idiomas soportados',
                            value='[Lista completa de idiomas soportados]'
                                  '(https://es.wikipedia.org/wiki/ISO_639-1)',
                            inline=False)
            embed.add_field(name='Librería usada:',
                            value='[Translate en Github]'
                                  '(https://github.com/terryyin/'
                                  'translate-python)',
                            inline=False)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed, file=file)

        else:
            await ctx.send('¿Desde qué idioma quieres traducir?')

            def author(m):
                return m.author == ctx.message.author

            try:
                msg1 = await self.bot.wait_for('message',
                                               check=author,
                                               timeout=60.0)

            except asyncio.TimeoutError:
                await ctx.send('Tiempo expirado.')

            else:
                fromlang = language(msg1.content)
                await ctx.send('¡Bien! ahora, ¿a qué idioma quieres '
                               'traducir?')

                try:
                    msg2 = await self.bot.wait_for('message',
                                                   check=author,
                                                   timeout=60.0)

                except asyncio.TimeoutError:
                    await ctx.send('Tiempo expirado.')

                else:
                    tolang = language(msg2.content)
                    translator = Translator(from_lang=fromlang,
                                            to_lang=tolang)

                    await ctx.send('Ya casi, ¿qué quieres traducir?')

                    try:
                        msg3 = await self.bot.wait_for('message',
                                                       check=author,
                                                       timeout=60.0)

                    except asyncio.TimeoutError:
                        await ctx.send('Solicitud expirada.')

                    except not msg3.content:
                        await ctx.send('No escribiste nada.')

                    else:
                        translation = translator.translate(
                            msg3.content
                        )
                        tolangUpper = tolang.upper()

                        embed = discord.Embed(
                            title='¡Traducciones a la orden!',
                            color=discord.Color.blue(),
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.set_thumbnail(
                            url='attachment://image.png')
                        embed.add_field(name='Traducción:',
                                        value=f'{translation}'
                                              f' ({fromlang}'
                                              f' -> {tolangUpper})',
                                        inline=True)
                        embed.set_footer(text=ctx.guild,
                                         icon_url=ctx.guild.icon_url)

                        await ctx.send(embed=embed, file=file)

    @commands.command(name='fulltranslate',
                      aliases=['ftr', 'ftte'],
                      description='Traduce con una sola línea.')
    async def translate_full(self, ctx, fromlang, tolang, *, args):
        translator = Translator(from_lang=fromlang, to_lang=tolang)
        translation = translator.translate(args)
        await ctx.send(f'**{translation}** ({fromlang}'
                       f' -> {str.upper(tolang)})')


def setup(bot):
    bot.add_cog(Translate(bot))
