import cog.functions.functions as functions
from discord.ext import commands
from translate import Translator


function = functions.Functions


class Translate(commands.Cog,
                name='Traductor',
                description='¡Traduce en más de 180 idiomas!'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['traducir'], help='¡Traduce oraciones!')
    async def translate(self, ctx, fromlang, tolang, *, args: str):
        fl = function.languageTranslate(str.lower(fromlang))
        if fl is None:
            await ctx.send(f'"{fromlang}" no es un idioma o'
                           ' no puedo reconocerlo.')
        else:
            tl = function.languageTranslate(str.lower(tolang))
            if tl is None:
                await ctx.send(f'"{tolang}" no es un idioma'
                               ' o no puedo reconocerlo.')
            else:
                translator = Translator(
                    from_lang=fl, to_lang=tl
                )

                translation = translator.translate(args)

                e = function.languageEmbed(
                    translation,
                    fromlang,
                    tolang,
                    ctx.author.name,
                    ctx.guild.icon_url
                )

                await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Translate(bot))
