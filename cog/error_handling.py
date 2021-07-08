import discord
from cog.functions import rbColor
from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        e = discord.Embed(color=rbColor())

        if isinstance(error, commands.CommandNotFound):
            e.add_field(name='Comando erróneo',
                        value='No pude encontrar ese comando,'
                              ' por lo que puede que no exista,'
                              ' esté deshabilitado o lo hayas escrito mal.')
            await ctx.send(embed=e)

        elif isinstance(error, commands.MissingPermissions):
            e.add_field(name='No tienes los permisos necesarios',
                        value='Te faltan los permisos requeridos'
                              ' para usar este comando.')
            await ctx.send(embed=e)

        elif isinstance(error, commands.MissingRequiredArgument):
            e.add_field(name='Necesito más argumentos',
                        value='Escribe `r.help <comando>`'
                              ' para más información.')
            await ctx.send(embed=e)

        elif isinstance(error, commands.MemberNotFound):
            e.add_field(name='Usuario no encontrado',
                        value='Inténtalo otra vez, trata de mencionar'
                              ' al correcto.')
            await ctx.send(embed=e)

        elif isinstance(error, commands.CommandOnCooldown):
            e.add_field(name='¡Comando en enfriamiento!',
                        value='Por favor, reinténtalo en '
                              f'**{error.retry_after:.2f}** segundos.')
            await ctx.send(embed=e)

        else:
            e.add_field(name='Hubo un error inesperado.',
                        value='Si bien no pudimos detectar el error exacto,'
                              ' puedes obtener más información en la'
                              ' documentación. Usá `r.docs` para ir a ella.')
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Error(bot))
