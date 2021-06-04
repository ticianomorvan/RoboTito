from discord.ext import commands


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            await ctx.send('No pude encontrar ese comando,'
                           ' por lo que puede que no exista,'
                           ' esté deshabilitado o lo hayas escrito mal.')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('No tienes los permisos necesarios.')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Necesito más argumentos para ejecutar ese'
                           ' comando, escribe `r.help <comando>` para'
                           ' más información.')

        elif isinstance(error, commands.MissingRole):
            await ctx.send('No tienes el o los permisos necesarios para'
                           ' ejecutar ese comando.')

        elif isinstance(error, commands.MemberNotFound):
            await ctx.send('No pude encontrar a ese usuario.')

        elif isinstance(error, commands.TooManyArguments):
            await ctx.send('Escribiste demasiados argumentos.')


def setup(bot):
    bot.add_cog(Error(bot))
