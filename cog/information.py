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
                      description='Obtén información del bot.')
    async def botinformation(self, ctx):
        g = ctx.guild
        gs = self.bot.guilds
        gs_count = len(gs)

        embed = discord.Embed(title='RoboTito',
                              color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.set_author(name='Información sobre')
        embed.set_thumbnail(url=bot_icon)
        embed.add_field(name='Actualmente participo en:',
                        value=f'{gs_count} servidores.',
                        inline=False)
        embed.add_field(name='¿Tienes dudas?',
                        value='Consulta mi documentación en'
                              ' [readme.io](https://robotito.readme.io/)',
                        inline=False)
        embed.set_footer(text=g, icon_url=g.icon_url)

        await ctx.send(embed=embed)

    @commands.command(name='documentation',
                      aliases=['docs', 'documentación'],
                      description='Accede a la documentación de RoboTito')
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
                      description='Obtén información del servidor.')
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
    async def userinformation(self, ctx, member=None):
        g = ctx.guild

        if member is not None:
            u = member
            u_joindate = str(u.joined_at)[:10]
            u_createdate = str(u.created_at)[:10]

            if member.nick is not None:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.set_author(name=u.name, icon_url=u.avatar_url)
                embed.set_thumbnail(url=u.avatar_url)
                embed.add_field(name='Nombre:',
                                value=u.name,
                                inline=False)
                embed.add_field(name='Apodo:',
                                value=f'"{u.nick}"',
                                inline=False)
                embed.add_field(name='ID:',
                                value=u.id,
                                inline=False)
                embed.add_field(name='Se unió el:',
                                value=u_joindate,
                                inline=False)
                embed.add_field(name='Cuenta creada el:',
                                value=u_createdate,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.set_author(name=u.name, icon_url=u.avatar_url)
                embed.set_thumbnail(url=u.avatar_url)
                embed.add_field(name='Nombre:',
                                value=u.name,
                                inline=False)
                embed.add_field(name='ID:',
                                value=u.id,
                                inline=False)
                embed.add_field(name='Se unió el:',
                                value=u_joindate,
                                inline=False)
                embed.add_field(name='Cuenta creada el:',
                                value=u_createdate,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

        else:
            author = ctx.author
            author_joindate = str(author.joined_at)[:10]
            author_createdate = str(author.created_at)[:10]

            if author.nick is not None:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.set_author(name=author.name, icon_url=author.avatar_url)
                embed.set_thumbnail(url=author.avatar_url)
                embed.add_field(name='Nombre:',
                                value=author.name,
                                inline=False)
                embed.add_field(name='Apodo:',
                                value=f'"{author.nick}"',
                                inline=False)
                embed.add_field(name='ID:',
                                value=author.id,
                                inline=False)
                embed.add_field(name='Se unió el:',
                                value=author_joindate,
                                inline=False)
                embed.add_field(name='Cuenta creada el:',
                                value=author_createdate,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.set_author(name=author.name, icon_url=author.avatar_url)
                embed.set_thumbnail(url=author.avatar_url)
                embed.add_field(name='Nombre:',
                                value=author.name,
                                inline=False)
                embed.add_field(name='ID:',
                                value=author.id,
                                inline=False)
                embed.add_field(name='Se unió el:',
                                value=author_joindate,
                                inline=False)
                embed.add_field(name='Cuenta creada el:',
                                value=author_createdate,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

    @commands.command(name='avatar',
                      aliases=['av', 'useravatar', 'usericon'],
                      description='Recupera la foto de perfil de un usuario.')
    async def useravatar(self, ctx, member=None):
        g = ctx.guild

        if member is not None:
            u = member

            if u.nick is not None:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.add_field(name='Avatar de:',
                                value=f'{u.name}, alias {u.nick}',
                                inline=False)
                embed.set_image(url=u.avatar_url)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.add_field(name='Avatar de:',
                                value=u.name,
                                inline=False)
                embed.set_image(url=u.avatar_url)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

        else:
            author = ctx.author

            if author.nick is not None:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.add_field(name='Avatar de:',
                                value=f'{author.name}, alias {author.nick}',
                                inline=False)
                embed.set_image(url=author.avatar_url)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.add_field(name='Avatar de:',
                                value=author.name,
                                inline=False)
                embed.set_image(url=author.avatar_url)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
