import discord
import random
from datetime import datetime
from discord.member import Member
from discord.ext import commands

# This commands are mostly for use in a private server, but you can use some
# of the ideas that are here.


def polentaLevels(percentage: int):
    if percentage == 0:
        phrases = [
            'estoy orgulloso de ti.',
            'no esperaría menos de alguien como tu.',
            'fiel al sistema, me enorgulleces.',
            'me hacés llorar, estoy orgulloso.',
            'te criaron bien, demasiado bien.'
        ]
        return random.choice(phrases)
    elif percentage <= 40:
        phrases = [
            'hay cosas sobre las que tenemos que trabajar, pero vas bien.',
            'has empezado a transformarte, pero tranquilicémonos, podemos'
            ' arreglarlo.',
            'es bastante poco aún, podemos hacer algo para mejorarlo.',
            'aún no aceptaste lo suficiente la polenta, tenemos tiempo.',
            'por favor, no te acerques a focos de infección.'
        ]
        return random.choice(phrases)
    elif percentage <= 70:
        phrases = [
            'no te queda mucho tiempo, tenemos que apresuranos.',
            'la polenta está tapando tus arterias, hay que tomar medidas.',
            'debemos actuar **ya**, antes de que avance aún más.',
            'no quiero que te perdamos, debemos empezar a actuar.',
            'no tenemos mucho tiempo, hay que ponernos manos a la obra.'
        ]
        return random.choice(phrases)
    elif percentage <= 99:
        phrases = [
            'no hay mucho que podamos hacer, la polenta reemplazó cada'
            ' gota de tu sangre.',
            'el nivel de polenta en tu sangre es altísimo, lo sentimos.',
            'esto pasa cuando votan asado y terminan comiendo polenta,'
            ' odio este país.',
            'no podemos ayudarte, la polenta tomó completamente tu cuerpo.',
            'esperamos que hayas vivido una buena vida, porque llegaste'
            ' hasta acá.'
        ]
        return random.choice(phrases)
    else:
        return """**SOS POLENTAMAN Y VENÍS A LLENAR DE POLENTA CADA
               ESTÓMAGO ARGENTINO**"""


def polentaEmbed(percentage, phrase, guildIcon, guildName, user=None):
    if user is not None:
        e = discord.Embed(
            title='Polentómetro',
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        e.add_field(
            name=f'El nivel de polenta en sangre de {user} es de:',
            value=f'**{percentage}%**, {phrase}'
        )
        e.set_image(url='https://img.itdg.com.br/tdg/images/blog/uploads/'
                        '2017/12/polenta.jpg')
        e.set_footer(text=guildName, icon_url=guildIcon)
        return e
    else:
        e = discord.Embed(
            title='Polentómetro',
            color=discord.Color.blue(),
            timestamp=datetime.utcnow()
        )
        e.add_field(
            name='Tu nivel de polenta en sangre es de:',
            value=f'**{percentage}%**, {phrase}'
        )
        e.set_image(url='https://img.itdg.com.br/tdg/images/blog/uploads/'
                        '2017/12/polenta.jpg')
        e.set_footer(text=guildName, icon_url=guildIcon)
        return e


class ExtraCommands(commands.Cog, name='Extra', description='Comandos extra.'):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name='polenta', aliases=['polentalvl', 'polenta%'],
                      help='¿De qué es tu polenta?')
    async def polentaLevel(self, ctx, member: Member = None):
        if member is not None:
            polLevel = random.randint(0, 100)
            polPhrase = polentaLevels(polLevel)
            polEmbed = polentaEmbed(polLevel, polPhrase, ctx.guild.icon_url,
                                    ctx.guild.name, member.name)
            await ctx.send(embed=polEmbed)
        else:
            polLevel = random.randint(0, 100)
            polPhrase = polentaLevels(polLevel)
            polEmbed = polentaEmbed(polLevel, polPhrase, ctx.guild.icon_url,
                                    ctx.guild.name)
            await ctx.send(embed=polEmbed)


def setup(bot):
    bot.add_cog(ExtraCommands(bot))
