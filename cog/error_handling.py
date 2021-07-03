import discord
from cog.functions import rbColor
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

        else:
            e = discord.Embed(color=rbColor())
            e.add_field(name='Desgraciadamente, ha ocurrido un error.',
                        value='Las causas podrían ser algunas '
                              'de las siguientes:',
                        inline=False)
            e.add_field(name='1. Problemas con APIs',
                        value='Si estás tratando de utilizar un comando que'
                              ' hace uso de APIs (es decir, que busca'
                              ' información en internet) es probable que haya'
                              ' habido un error en la comunicación con dicha'
                              ' API y/o se haya llegado al límite'
                              ' de peticiones.',
                        inline=False)
            e.add_field(name='2. Errores del código inesperados',
                        value='Si bien hacemos numerosas pruebas antes de'
                              ' lanzar nuevas características o luego de'
                              ' arreglar errores, es cierto que podrían'
                              ' surgir nuevos problemas que todavía no'
                              ' hemos descubierto. De ser así, por favor,'
                              ' háznoslo saber a través de la creación'
                              ' de un *issue* en [Github](https://github.'
                              'com/Ti7oyan/RoboTito/issues).',
                        inline=False)
            e.add_field(name='3. Falta de ciertos permisos / configuraciones',
                        value='Ciertos comandos necesitan de permisos'
                              ' específicos para funcionar, por lo que es'
                              ' probable que estés careciendo de estos.\n'
                              'También existe la posibilidad de que algunas'
                              ' configuraciones no estén hechas correctamente,'
                              ' como la jerarquía de roles (el bot no puede'
                              ' modificar o realizar acciones sobre personas'
                              ' con roles superiores al suyo).',
                        inline=False)
            e.add_field(name='4. Otros',
                        value='No podemos estar seguros de todos los errores'
                              ' por los que el bot pasa durante su'
                              ' funcionamiento, por lo que sugerimos revisar'
                              ' la documentación oficial de RoboTito a través'
                              ' de este [enlace](https://ticiano-morvan.'
                              'gitbook.io/robotito/).',
                        inline=False)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Error(bot))
