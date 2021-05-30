import discord
from discord.ext import commands

from translate import Translator

import datetime

import json


def languageTranslate(language):
    with open('databases/iso639-1/db_languages.json', encoding='utf-8') as f:
        data = f.read()
        lang = json.loads(data)
        if language in lang:
            codename = lang[language]['codename']
            return codename
        else:
            pass


file = discord.File('images/Translate.png', filename='image.png')


class Translate(commands.Cog,
                name='Traductor',
                description='¡Traduce en más de 180 idiomas!'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='traducir')
    async def translate(self, ctx, fromlang, tolang, *, args: str):
        a = ctx.author
        g = ctx.guild

        if fromlang is not None:
            flstr = str.lower(fromlang)
            fl = languageTranslate(flstr)
            if tolang is not None:
                tlstr = str.lower(tolang)
                tl = languageTranslate(tlstr)
                if args is not None:
                    translator = Translator(
                        from_lang=fl, to_lang=tl
                    )

                    translation = translator.translate(args)

                    embed = discord.Embed(
                        title=translation,
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.add_field(
                        name='Traducido:',
                        value=f'{flstr} :arrow_right: {tlstr}',
                        inline=False
                    ),
                    embed.set_thumbnail(
                        url='attachment://image.png'
                    )
                    embed.set_footer(
                        text=a.name,
                        icon_url=g.icon_url
                    )

                    await ctx.send(embed=embed, file=file)


def setup(bot):
    bot.add_cog(Translate(bot))
