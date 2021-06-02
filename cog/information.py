import discord
from discord.ext import commands

import datetime

bot_icon = 'https://i.imgur.com/e4aMdPk.jpg'


class Information(commands.Cog,
                  name='Información',
                  description='Obtén información sobre el bot, '
                              'el servidor o un usuario.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='information',
                      aliases=['info', 'información', 'botinfo'],
                      help='Obtén información del bot.')
    async def botinformation(self, ctx):
        g = ctx.guild
        gs = self.bot.guilds
        gs_count = len(gs)

        embed = discord.Embed(color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=bot_icon)
        embed.add_field(name='RoboTito',
                        value='Información sobre mi.',
                        inline=False)
        embed.add_field(name='Actualmente participo en:',
                        value=f'{gs_count} servidores.',
                        inline=False)
        embed.add_field(name='¿Tienes dudas?',
                        value='Consulta mi documentación en'
                              ' [readme.io](https://robotito.readme.io/)',
                        inline=False)
        embed.add_field(name='Mi código fuente está en:',
                        value='[RoboTito, por ATT-Inc]'
                              '(https://github.com/ATT-Inc/RoboTito)',
                        inline=False)
        embed.add_field(name='Para invitarme a un servidor:',
                        value='Usá este [link](https://discord.com/api/oauth2/'
                              'authorize?client_id=820819824669491210&permiss'
                              'ions=8&scope=bot)',
                        inline=False)
        embed.set_footer(text=g, icon_url=g.icon_url)

        await ctx.send(embed=embed)

    @commands.command(name='documentation',
                      aliases=['docs', 'documentación'],
                      help='Accede a la documentación de RoboTito')
    async def botdocumentation(self, ctx):
        g = ctx.guild

        embed = discord.Embed(color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=bot_icon)
        embed.add_field(name='Documentación de RoboTito',
                        value='[Revisá la documentación en readme.io]'
                              '(https://robotito.readme.io)')
        embed.set_footer(text=g, icon_url=g.icon_url)

        await ctx.send(embed=embed)

    @commands.command(name='serverinfo',
                      aliases=['svinfo', 'infosv', 'infodelserver'],
                      help='Obtén información del servidor.')
    async def serverinformation(self, ctx):
        g = ctx.guild
        members = g.member_count
        owner = g.owner
        creation = str(g.created_at)[:10]

        embed = discord.Embed(color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_author(name=g.name, icon_url=g.icon_url)
        embed.set_thumbnail(url=g.icon_url)
        embed.add_field(name='Cantidad de usuarios:',
                        value=members,
                        inline=True)
        embed.add_field(name='El/La propietario/a del servidor es:',
                        value=owner,
                        inline=False)
        embed.add_field(name='El servidor se creó el:',
                        value=creation,
                        inline=False)
        embed.set_footer(text=ctx.author.name,
                         icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(name='userinfo',
                      aliases=['usinfo', 'infodelusuario', 'uinfo'],
                      description='Obtén información del usuario.')
    async def userinformation(self, ctx, member: discord.Member = None):
        g = ctx.guild

        if member is None:
            author = ctx.author

            if author.nick is not None:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=author.avatar_url)
                embed.add_field(name=author.name,
                                value=author.nick,
                                inline=False)
                embed.add_field(name=author.color,
                                value='Color',
                                inline=False)
                embed.add_field(name=author.top_role,
                                value='Rol más alto',
                                inline=False)
                embed.add_field(name=str(author.created_at)[:10],
                                value='Su cuenta se creó el día',
                                inline=False)
                embed.add_field(name=str(author.joined_at)[:10],
                                value='Se unió al servidor el día',
                                inline=False)
                embed.add_field(name='No',
                                value='¿Es un bot?',
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=author.avatar_url)
                embed.add_field(name=author.name,
                                value=f'#{author.discriminator}',
                                inline=False)
                embed.add_field(name=author.color,
                                value='Color',
                                inline=False)
                embed.add_field(name=author.top_role,
                                value='Rol más alto',
                                inline=False)
                embed.add_field(name=str(author.created_at)[:10],
                                value='Su cuenta se creó el día',
                                inline=False)
                embed.add_field(name=str(author.joined_at)[:10],
                                value='Se unió al servidor el día',
                                inline=False)
                embed.add_field(name='No',
                                value='¿Es un bot?',
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

        if member.bot is True:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name=member.name,
                            value=member.nick,
                            inline=False)
            embed.add_field(name=member.color,
                            value='Color',
                            inline=False)
            embed.add_field(name=member.top_role,
                            value='Rol más alto',
                            inline=False)
            embed.add_field(name=str(member.created_at)[:10],
                            value='Su cuenta se creó el día',
                            inline=False)
            embed.add_field(name=str(member.joined_at)[:10],
                            value='Se unió al servidor el día',
                            inline=False)
            embed.add_field(name='Sí',
                            value='¿Es un bot?',
                            inline=False)
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed)

        elif member.bot is False:

            if member is not None:

                if member.nick is not None:
                    embed = discord.Embed(color=discord.Color.blue(),
                                          timestamp=datetime.datetime.utcnow())
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name=member.name,
                                    value=member.nick,
                                    inline=False)
                    embed.add_field(name=member.color,
                                    value='Color',
                                    inline=False)
                    embed.add_field(name=member.top_role,
                                    value='Rol más alto',
                                    inline=False)
                    embed.add_field(name=str(member.created_at)[:10],
                                    value='Su cuenta se creó el día',
                                    inline=False)
                    embed.add_field(name=str(member.joined_at)[:10],
                                    value='Se unió al servidor el día',
                                    inline=False)
                    embed.add_field(name='No',
                                    value='¿Es un bot?',
                                    inline=False)
                    embed.set_footer(text=g, icon_url=g.icon_url)

                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(color=discord.Color.blue(),
                                          timestamp=datetime.datetime.utcnow())
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name=member.name,
                                    value=f'#{member.discriminator}',
                                    inline=False)
                    embed.add_field(name=member.color,
                                    value='Color',
                                    inline=False)
                    embed.add_field(name=member.top_role,
                                    value='Rol más alto',
                                    inline=False)
                    embed.add_field(name=str(member.created_at)[:10],
                                    value='Su cuenta se creó el día',
                                    inline=False)
                    embed.add_field(name=str(member.joined_at)[:10],
                                    value='Se unió al servidor el día',
                                    inline=False)
                    embed.add_field(name='No',
                                    value='¿Es un bot?',
                                    inline=False)
                    embed.set_footer(text=g, icon_url=g.icon_url)

                    await ctx.send(embed=embed)

    @commands.command(name='avatar',
                      aliases=['av', 'useravatar', 'usericon'],
                      help='Recupera la foto de perfil de un usuario.')
    async def useravatar(self, ctx, member: discord.Member = None):
        g = ctx.guild

        if member is None:
            author = ctx.author

            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name=author.name,
                            value=author.nick)
            embed.set_image(url=author.avatar_url)
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name=member.name,
                            value=member.nick)
            embed.set_image(url=member.avatar_url)
            embed.set_footer(text=g, icon_url=g.icon_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
