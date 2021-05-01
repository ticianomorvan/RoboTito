import discord
from discord.ext import commands

import datetime

bot_icon = 'https://i.imgur.com/e4aMdPk.jpg'

readme_io = 'https://robotito.readme.io/reference#'


class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        guild = ctx.guild

        if isinstance(error, commands.BotMissingRole):
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f'{bot_icon}')
            embed.add_field(name='ERROR: #1',
                            value='No tengo los roles necesarios.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}botmissingrole)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #2',
                            value='No tengo los permisos necesarios.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}botmissingpermissions)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #3',
                            value='No pude encontrar ese comando.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}commandnotfound)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingAnyRole):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #4',
                            value='No pude encontrar ese comando.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}missinganyrole)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #5',
                            value='No tienes los permisos necesarios.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}missingpermissions)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #6',
                            value='Necesito más argumentos.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}missingrequiredargument)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRole):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #7',
                            value='No tienes los roles necesarios.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}missingrole)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #8',
                            value='No encontré al usuario.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}membernotfound)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.TooManyArguments):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #9',
                            value='Demasiados argumentos.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}toomanyarguments)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        elif isinstance(error, commands.NSFWChannelRequired):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_author(name='Reporte de errores:',
                             icon_url=f"{bot_icon}")
            embed.add_field(name='ERROR: #10',
                            value='Este comando funciona en canales NSFW.',
                            inline=False)
            embed.add_field(name='Para más información:',
                            value='[Visitá la documentación en readme.io]'
                                  f'({readme_io}nsfwchannelrequired)',
                            inline=False)
            embed.set_footer(text=guild, icon_url=guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('No encontré respuesta a eso, visitá la '
                           'documentación para más info. '
                           'https://robotito.readme.io')


def setup(bot):
    bot.add_cog(Error(bot))
