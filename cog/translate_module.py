import discord
import json
from cog.functions import rbColor
from discord.ext import commands
from translate import Translator


def language_translate(language):
    with open('databases/db_languages.json', encoding='utf-8') as f:
        data = f.read()
        lang = json.loads(data)
        if language in lang:
            codename = lang[language]['codename']
            return codename
        else:
            pass


def language_embed(translation, fromlang, tolang):
    e = discord.Embed(title=translation, color=rbColor())
    e.add_field(name='Traducido:', value=f'**{fromlang}** >> **{tolang}**')
    e.set_thumbnail(url='https://i.imgur.com/0o5ZKBl.png')
    return e


class Translate(commands.Cog,
                name='Traductor',
                description='¡Traduce en más de 180 idiomas!'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['traducir'], help='¡Traduce oraciones!')
    async def translate(self, ctx, fromlang, tolang, *, args: str):
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
                e = language_embed(translation, fromlang, tolang)
                await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Translate(bot))
