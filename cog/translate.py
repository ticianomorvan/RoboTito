import discord
from discord.ext import commands

from translate import Translator

import datetime

import json

with open('databases/db_iso639-1.json') as f:
    data = f.read()
    lang = json.loads(data)
    languages = lang['languages']


class Translate(
    commands.Cog,
    name='Traductor',
    description='¡Traduce en más de 180 idiomas!'
):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='translate', aliases=['tr', 'tte'])
    async def traducir(self, ctx, extra=None):
        guild = ctx.guild

        if extra == 'help':
            embed = discord.Embed(
                title='Ayuda sobre las traducciones',
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.set_thumbnail(
                url='http://icons.iconarchive.com/icons/marcus-roberto/'
                    'google-play/512/Google-Translate-icon.png',
            )
            embed.add_field(
                name='Idiomas soportados',
                value='[Lista completa de idiomas soportados]'
                      '(https://es.wikipedia.org/wiki/ISO_639-1)',
                inline=False,
            )
            embed.add_field(
                name='Librería usada:',
                value='[Translate en Github]'
                      '(https://github.com/terryyin/translate-python)',
                inline=False,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send('¿Desde qué idioma quieres traducir?')

            def check1(m):
                return m.content in languages

            msg1 = await self.bot.wait_for(
                'message',
                check=check1,
            )
            await ctx.send('¡Bien! ahora, ¿a qué idioma quieres traducir?')
            msg2 = await self.bot.wait_for('message', check=check1)
            translator = Translator(
                from_lang=msg1.content,
                to_lang=msg2.content,
            )
            await ctx.send('Ya casi, ¿qué quieres traducir?')
            msg3 = await self.bot.wait_for(
                'message',
                check=lambda message: ctx.author == message.author,
            )
            translation = translator.translate(msg3.content)

            msg2_cont = msg2.content
            msg2_upper = msg2_cont.upper()

            embed = discord.Embed(
                title='¡Traducciones a la orden!',
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.set_thumbnail(
                url='http://icons.iconarchive.com/icons/marcus-roberto/'
                    'google-play/512/Google-Translate-icon.png',
            )
            embed.add_field(
                name='Traducción:',
                value=f'{translation} ({msg1.content} -> {msg2_upper})',
                inline=True,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

    @commands.command(name='fulltranslate', aliases=['ftr', 'ftte'])
    async def traducircompleto(self, ctx, fromlang, tolang, *, args):
        translator = Translator(from_lang=fromlang, to_lang=tolang)
        translation = translator.translate(args)
        await ctx.send(
            f'**{translation}** ({fromlang} -> {str.upper(tolang)})'
        )


def setup(bot):
    bot.add_cog(Translate(bot))
