import discord
import json
from datetime import datetime
from discord.ext import commands
from translate import Translator
from cog.functions.functions import Functions as f


def languageTranslate(language):
    with open('databases/db_languages.json', encoding='utf-8') as f:
        data = f.read()
        lang = json.loads(data)
        if language in lang:
            codename = lang[language]['codename']
            return codename
        else:
            pass


def languageEmbed(translation, fromlang, tolang, author, guildIcon):
    e = discord.Embed(
        title=translation,
        color=f.rbColor(),
        timestamp=datetime.utcnow()
    )
    e.add_field(
        name='Traducido:',
        value=f'**{fromlang}** >> **{tolang}**'
    )
    e.set_thumbnail(
        url='https://i.imgur.com/0o5ZKBl.png'
    )
    e.set_footer(
        text=author,
        icon_url=guildIcon
    )
    return e


class Translate(commands.Cog,
                name='Traductor',
                description='¡Traduce en más de 180 idiomas!'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['traducir'], help='¡Traduce oraciones!')
    async def translate(self, ctx, fromlang, tolang, *, args: str):
        fl = languageTranslate(str.lower(fromlang))
        if fl is None:
            await ctx.send(f'"{fromlang}" no es un idioma o'
                           ' no puedo reconocerlo.')
        else:
            tl = languageTranslate(str.lower(tolang))
            if tl is None:
                await ctx.send(f'"{tolang}" no es un idioma'
                               ' o no puedo reconocerlo.')
            else:
                translator = Translator(
                    from_lang=fl, to_lang=tl
                )

                translation = translator.translate(args)

                e = languageEmbed(
                    translation,
                    fromlang,
                    tolang,
                    ctx.author.name,
                    ctx.guild.icon_url
                )

                await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Translate(bot))
