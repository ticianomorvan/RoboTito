import asyncio

import discord
from discord.ext import commands

from translate import Translator

import datetime

import json


with open('databases/iso639-1/db_iso639-C.json', encoding='utf-8') as f:
    data = f.read()
    lang = json.loads(data)


# Here i declare all the langcodes available on the ISO 639-1, for an 100%
# support of the standard.


def language(message):
    if message in lang['afar']:
        langcode = 'aa'
        return langcode
    elif message in lang['abkhazian']:
        langcode = 'ab'
        return langcode
    elif message in lang['avestan']:
        langcode = 'ae'
        return langcode
    elif message in lang['afrikaans']:
        langcode = 'af'
        return langcode
    elif message in lang['akan']:
        langcode = 'ak'
        return langcode
    elif message in lang['amharic']:
        langcode = 'am'
        return langcode
    elif message in lang['aragonese']:
        langcode = 'an'
        return langcode
    elif message in lang['arabic']:
        langcode = 'ar'
        return langcode
    elif message in lang['assamese']:
        langcode = 'as'
        return langcode
    elif message in lang['avaric']:
        langcode = 'av'
        return langcode
    elif message in lang['aymara']:
        langcode = 'ay'
        return langcode
    elif message in lang['azerbaijani']:
        langcode = 'az'
        return langcode
    elif message in lang['bashkir']:
        langcode = 'ba'
        return langcode
    elif message in lang['belarusian']:
        langcode = 'be'
        return langcode
    elif message in lang['bulgarian']:
        langcode = 'bg'
        return langcode
    elif message in lang['bihari']:
        langcode = 'bh'
        return langcode
    elif message in lang['bislama']:
        langcode = 'bi'
        return langcode
    elif message in lang['bambara']:
        langcode = 'bm'
        return langcode
    elif message in lang['bengali']:
        langcode = 'bn'
        return langcode
    elif message in lang['tibetan']:
        langcode = 'bo'
        return langcode
    elif message in lang['breton']:
        langcode = 'br'
        return langcode
    elif message in lang['bosnian']:
        langcode = 'bs'
        return langcode
    elif message in lang['catalan']:
        langcode = 'ca'
        return langcode
    elif message in lang['chechen']:
        langcode = 'ce'
        return langcode
    elif message in lang['chamorro']:
        langcode = 'ch'
        return langcode
    elif message in lang['corsican']:
        langcode = 'co'
        return langcode
    elif message in lang['cree']:
        langcode = 'cr'
        return langcode
    elif message in lang['czech']:
        langcode = 'cs'
        return langcode
    elif message in lang['churchslavic']:
        langcode = 'cu'
        return langcode
    elif message in lang['chuvash']:
        langcode = 'cv'
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
    elif message in lang['divehi']:
        langcode = 'dv'
        return langcode
    elif message in lang['dzongkha']:
        langcode = 'dz'
        return langcode
    elif message in lang['ewe']:
        langcode = 'ee'
        return langcode
    elif message in lang['greek']:
        langcode = 'el'
        return langcode
    elif message in lang['english']:
        langcode = 'en'
        return langcode
    elif message in lang['esperanto']:
        langcode = 'eo'
        return langcode
    elif message in lang['spanish']:
        langcode = 'es'
        return langcode
    elif message in lang['estonian']:
        langcode = 'et'
        return langcode
    elif message in lang['basque']:
        langcode = 'eu'
        return langcode
    elif message in lang['persian']:
        langcode = 'fa'
        return langcode
    elif message in lang['fulah']:
        langcode = 'ff'
        return langcode
    elif message in lang['finnish']:
        langcode = 'fi'
        return langcode
    elif message in lang['fijian']:
        langcode = 'fj'
        return langcode
    elif message in lang['faroese']:
        langcode = 'fo'
        return langcode
    elif message in lang['french']:
        langcode = 'fr'
        return langcode
    elif message in lang['westernfrisian']:
        langcode = 'fy'
        return langcode
    elif message in lang['irish']:
        langcode = 'ga'
        return langcode
    elif message in lang['gaelic']:
        langcode = 'gd'
        return langcode
    elif message in lang['galician']:
        langcode = 'gl'
        return langcode
    elif message in lang['guarani']:
        langcode = 'gn'
        return langcode
    elif message in lang['gujarati']:
        langcode = 'gu'
        return langcode
    elif message in lang['manx']:
        langcode = 'gv'
        return langcode
    elif message in lang['hausa']:
        langcode = 'ha'
        return langcode
    elif message in lang['hebrew']:
        langcode = 'he'
        return langcode
    elif message in lang['hindi']:
        langcode = 'hi'
        return langcode
    elif message in lang['hirimotu']:
        langcode = 'ho'
        return langcode
    elif message in lang['croatian']:
        langcode = 'hr'
        return langcode
    elif message in lang['haitian']:
        langcode = 'ht'
        return langcode
    elif message in lang['hungarian']:
        langcode = 'hu'
        return langcode
    elif message in lang['armenian']:
        langcode = 'hy'
        return langcode
    elif message in lang['herero']:
        langcode = 'hz'
        return langcode
    elif message in lang['interlingua']:
        langcode = 'ia'
        return langcode
    elif message in lang['indonesian']:
        langcode = 'id'
        return langcode
    elif message in lang['interlingue']:
        langcode = 'ie'
        return langcode
    elif message in lang['igbo']:
        langcode = 'ig'
        return langcode
    elif message in lang['sichuanyi']:
        langcode = 'ii'
        return langcode
    elif message in lang['inupiaq']:
        langcode = 'ik'
        return langcode
    elif message in lang['ido']:
        langcode = 'io'
        return langcode
    elif message in lang['icelandic']:
        langcode = 'is'
        return langcode
    elif message in lang['italian']:
        langcode = 'it'
        return langcode
    elif message in lang['inuktitut']:
        langcode = 'iu'
        return langcode
    elif message in lang['japanese']:
        langcode = 'ja'
        return langcode
    elif message in lang['javanese']:
        langcode = 'jv'
        return langcode
    elif message in lang['georgian']:
        langcode = 'ka'
        return langcode
    elif message in lang['kongo']:
        langcode = 'kg'
        return langcode
    elif message in lang['kikuyu']:
        langcode = 'ki'
        return langcode
    elif message in lang['kuanyama']:
        langcode = 'kj'
        return langcode
    elif message in lang['kazakh']:
        langcode = 'kk'
        return langcode
    elif message in lang['greenlandic']:
        langcode = 'kl'
        return langcode
    elif message in lang['centralkhmer']:
        langcode = 'km'
        return langcode
    elif message in lang['kannada']:
        langcode = 'kn'
        return langcode
    elif message in lang['korean']:
        langcode = 'ko'
        return langcode
    elif message in lang['kanuri']:
        langcode = 'kr'
        return langcode
    elif message in lang['kashmiri']:
        langcode = 'ks'
        return langcode
    elif message in lang['kurdish']:
        langcode = 'ku'
        return langcode
    elif message in lang['komi']:
        langcode = 'kv'
        return langcode
    elif message in lang['cornish']:
        langcode = 'kw'
        return langcode
    elif message in lang['latin']:
        langcode = 'la'
        return langcode
    elif message in lang['luxembourgish']:
        langcode = 'lb'
        return langcode
    elif message in lang['ganda']:
        langcode = 'lg'
        return langcode
    elif message in lang['limburgan']:
        langcode = 'li'
        return langcode
    elif message in lang['lingala']:
        langcode = 'ln'
        return langcode
    elif message in lang['lao']:
        langcode = 'lo'
        return langcode
    elif message in lang['lithuanian']:
        langcode = 'lt'
        return langcode
    elif message in lang['lubakatanga']:
        langcode = 'lu'
        return langcode
    elif message in lang['latvian']:
        langcode = 'lv'
        return langcode
    elif message in lang['malagasy']:
        langcode = 'mg'
        return langcode
    elif message in lang['marshallese']:
        langcode = 'mh'
        return langcode
    elif message in lang['maori']:
        langcode = 'mi'
        return langcode
    elif message in lang['macedonian']:
        langcode = 'mk'
        return langcode
    elif message in lang['malayalam']:
        langcode = 'ml'
        return langcode
    elif message in lang['mongolian']:
        langcode = 'mn'
        return langcode
    elif message in lang['marathi']:
        langcode = 'mr'
        return langcode
    elif message in lang['malay']:
        langcode = 'ms'
        return langcode
    elif message in lang['maltese']:
        langcode = 'mt'
        return langcode
    elif message in lang['burmese']:
        langcode = 'my'
        return langcode
    elif message in lang['nauru']:
        langcode = 'na'
        return langcode
    elif message in lang['norwegianbokmal']:
        langcode = 'nb'
        return langcode
    elif message in lang['northndebele']:
        langcode = 'nd'
        return langcode
    elif message in lang['nepali']:
        langcode = 'ne'
        return langcode
    elif message in lang['ndonga']:
        langcode = 'ng'
        return langcode
    elif message in lang['dutch']:
        langcode = 'nl'
        return langcode
    elif message in lang['norwegiannynorsk']:
        langcode = 'nn'
        return langcode
    elif message in lang['norwegian']:
        langcode = 'no'
        return langcode
    elif message in lang['southndebele']:
        langcode = 'nr'
        return langcode
    elif message in lang['navajo']:
        langcode = 'nv'
        return langcode
    elif message in lang['chichewa']:
        langcode = 'ny'
        return langcode
    elif message in lang['occitan']:
        langcode = 'oc'
        return langcode
    elif message in lang['ojibwa']:
        langcode = 'oj'
        return langcode
    elif message in lang['oromo']:
        langcode = 'om'
        return langcode
    elif message in lang['oriya']:
        langcode = 'or'
        return langcode
    elif message in lang['ossetian']:
        langcode = 'os'
        return langcode
    elif message in lang['punjabi']:
        langcode = 'pa'
        return langcode
    elif message in lang['pali']:
        langcode = 'pi'
        return langcode
    elif message in lang['polish']:
        langcode = 'pl'
        return langcode
    elif message in lang['pashto']:
        langcode = 'ps'
        return langcode
    elif message in lang['portuguese']:
        langcode = 'pt'
        return langcode
    elif message in lang['quechua']:
        langcode = 'qu'
        return langcode
    elif message in lang['romansh']:
        langcode = 'rm'
        return langcode
    elif message in lang['russian']:
        langcode = 'ru'
        return langcode
    elif message in lang['kinyarwanda']:
        langcode = 'rw'
        return langcode
    elif message in lang['sanskrit']:
        langcode = 'sa'
        return langcode
    elif message in lang['sardinian']:
        langcode = 'sc'
        return langcode
    elif message in lang['sindhi']:
        langcode = 'sd'
        return langcode
    elif message in lang['northernsami']:
        langcode = 'se'
        return langcode
    elif message in lang['sango']:
        langcode = 'sg'
        return langcode
    elif message in lang['sinhala']:
        langcode = 'si'
        return langcode
    elif message in lang['slovak']:
        langcode = 'sk'
        return langcode
    elif message in lang['slovenian']:
        langcode = 'sl'
        return langcode
    elif message in lang['samoan']:
        langcode = 'sm'
        return langcode
    elif message in lang['shona']:
        langcode = 'sn'
        return langcode
    elif message in lang['somali']:
        langcode = 'so'
        return langcode
    elif message in lang['albanian']:
        langcode = 'sq'
        return langcode
    elif message in lang['serbian']:
        langcode = 'sr'
        return langcode
    elif message in lang['swati']:
        langcode = 'ss'
        return langcode
    elif message in lang['southernsotho']:
        langcode = 'st'
        return langcode
    elif message in lang['sundanese']:
        langcode = 'su'
        return langcode
    elif message in lang['swedish']:
        langcode = 'sv'
        return langcode
    elif message in lang['swahili']:
        langcode = 'sw'
        return langcode
    elif message in lang['tamil']:
        langcode = 'ta'
        return langcode
    elif message in lang['telugu']:
        langcode = 'te'
        return langcode
    elif message in lang['tajik']:
        langcode = 'tg'
        return langcode
    elif message in lang['thai']:
        langcode = 'th'
        return langcode
    elif message in lang['tigrinya']:
        langcode = 'ti'
        return langcode
    elif message in lang['turkmen']:
        langcode = 'tk'
        return langcode
    elif message in lang['tagalog']:
        langcode = 'tl'
        return langcode
    elif message in lang['tswana']:
        langcode = 'tn'
        return langcode
    elif message in lang['tonga']:
        langcode = 'to'
        return langcode
    elif message in lang['turkish']:
        langcode = 'tr'
        return langcode
    elif message in lang['tsonga']:
        langcode = 'ts'
        return langcode
    elif message in lang['tatar']:
        langcode = 'tt'
        return langcode
    elif message in lang['twi']:
        langcode = 'tw'
        return langcode
    elif message in lang['tahitian']:
        langcode = 'ty'
        return langcode
    elif message in lang['uighur']:
        langcode = 'ug'
        return langcode
    elif message in lang['ukrainian']:
        langcode = 'uk'
        return langcode
    elif message in lang['urdu']:
        langcode = 'ur'
        return langcode
    elif message in lang['uzbek']:
        langcode = 'uz'
        return langcode
    elif message in lang['venda']:
        langcode = 've'
        return langcode
    elif message in lang['vietnamese']:
        langcode = 'vi'
        return langcode
    elif message in lang['volapuk']:
        langcode = 'vo'
        return langcode
    elif message in lang['walloon']:
        langcode = 'wa'
        return langcode
    elif message in lang['wolof']:
        langcode = 'wo'
        return langcode
    elif message in lang['xhosa']:
        langcode = 'xh'
        return langcode
    elif message in lang['yiddish']:
        langcode = 'yi'
        return langcode
    elif message in lang['yoruba']:
        langcode = 'yo'
        return langcode
    elif message in lang['zhuang']:
        langcode = 'za'
        return langcode
    elif message in lang['chinese']:
        langcode = 'zh'
        return langcode
    elif message in lang['zulu']:
        langcode = 'zu'
        return langcode
    else:
        pass


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
            embed.set_thumbnail(url='attachment://image.png')
            embed.add_field(name='El módulo de traducción funciona'
                                 ' del siguiente modo:',
                            value='En las dos primeras instancias deberás'
                                  ' especificar desde que y a que idioma'
                                  ' quieres traducir, dichos idiomas pueden'
                                  ' ser escritos de diversas formas (por'
                                  ' ej: Español, español, spanish, etc.).'
                                  ' Luego escribirás lo que quieras traducir'
                                  ' y ¡listo! tu traducción será mostrada.',
                            inline=False)
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
            await ctx.send('Te doy la bienvenida al módulo traductor de'
                           ' RoboTito, para comenzar, escribe el idioma desde'
                           ' el que quieres traducir. Para más información,'
                           ' escribe **r.tte help**.')

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

                if fromlang is None:
                    await ctx.send('No reconozco ese lenguaje.')

                else:
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

                        if tolang is None:
                            await ctx.send('No reconozco ese lenguaje.')

                        else:
                            translator = Translator(from_lang=fromlang,
                                                    to_lang=tolang)

                            await ctx.send('Ya casi, ¿qué quieres traducir?')

                            try:
                                msg3 = await self.bot.wait_for('message',
                                                               check=author,
                                                               timeout=60.0)

                            except asyncio.TimeoutError:
                                await ctx.send('Solicitud expirada.')

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


def setup(bot):
    bot.add_cog(Translate(bot))
