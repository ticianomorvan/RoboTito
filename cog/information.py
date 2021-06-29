import discord
import json
import cog.functions as f
from discord.member import Member
from discord.guild import Guild
from discord.ext import commands


def monthName(month: int):
    with open('databases/db_str.json') as db:
        data = db.read()
        months = json.loads(data)
        selectMonth = months['months'][month]
        return selectMonth


def memberCreation(member: Member):
    mCreationFull = str(member.created_at)[:10]
    year, month, day = mCreationFull.split('-')
    cMonth = monthName(int(month))
    mCreation = f'Su cuenta se creó el día {day} de {cMonth} del año {year}.'
    return mCreation


def memberJoined(member: Member):
    mJoinFull = str(member.joined_at)[:10]
    year, month, day = mJoinFull.split('-')
    jMonth = monthName(int(month))
    mJoin = f'Se unió el día {day} de {jMonth} del año {year}.'
    return mJoin


def memberRoles(member: Member):
    string = ' '
    for role in member.roles:
        string += f'{role} - '

    return string


def memberEmbed(member: Member):
    e = discord.Embed(title=member.name, color=member.color)
    e.set_thumbnail(url=member.avatar_url)
    e.add_field(name='Color', value=member.color, inline=False)
    e.add_field(name='Rol más alto', value=member.top_role, inline=False)
    e.add_field(name='Creación', value=memberCreation(member), inline=False)
    e.add_field(name='Llegada al servidor', value=memberJoined(member),
                inline=False)
    e.add_field(name='Roles', value=memberRoles(member))
    return e


def guildCreation(guild: Guild):
    gCreationFull = str(guild.created_at)[:10]
    year, month, day = gCreationFull.split('-')
    cMonth = monthName(int(month))
    gCreation = f'El servidor se creó el día {day} de {cMonth} del año {year}.'
    return gCreation


def guildEmbed(guild: Guild):
    e = discord.Embed(title=guild.name, color=f.rbColor())
    e.set_thumbnail(url=guild.icon_url)
    e.add_field(name='Miembros',
                value='El servidor cuenta con '
                      f'**{len(guild.members)}** miembros.',
                inline=False)
    e.add_field(name='Categorías',
                value='El servidor cuenta con'
                      f' **{len(guild.categories)}** categorías.',
                inline=False)
    e.add_field(name='Canales',
                value=f'Existen **{len(guild.channels)}** canales en total,'
                      f' **{len(guild.text_channels)}** canales de texto y'
                      f' **{len(guild.voice_channels)}** canales de voz.',
                inline=False)
    e.add_field(name='Emojis',
                value='El servidor cuenta con '
                      f'**{len(guild.emojis)}** emojis.',
                inline=False)
    e.add_field(name='Roles',
                value='Este servidor cuenta con'
                      f' **{len(guild.roles)}** roles.',
                inline=False)
    e.add_field(name='Creación',
                value=guildCreation(guild),
                inline=False)
    e.add_field(name='Identificador', value=guild.id, inline=False)
    e.add_field(name='Dueño/a del servidor',
                value=f'**{guild.owner}**, ID: {guild.owner_id}',
                inline=False)
    return e


class Information(commands.Cog,
                  name='Información',
                  description='Obtén información sobre el bot, '
                              'el servidor o un usuario.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['binfo'],
                      help='Obtén información sobre el bot.')
    async def botinfo(self, ctx):
        app = await self.bot.application_info()
        prefix = self.bot.command_prefix
        users = len(self.bot.users)
        e = discord.Embed(description='**RoboTito** es un bot centrado en la'
                                      ' facilidad de uso, la variedad de'
                                      ' comandos y la diferenciación de sí'
                                      ' mismo por sobre otros utilizando'
                                      ' funcionalidades innovadoras o pocas'
                                      ' veces vistas.',
                          color=f.rbColor())
        e.set_author(name='RoboTito - Documentación',
                     url='https://ticiano-morvan.gitbook.io/robotito/')
        e.set_thumbnail(url=app.icon_url)
        e.add_field(name='Servidores',
                    value='Participo en un total de:'
                          f' **{len(self.bot.guilds)}** servidores.',
                    inline=False)
        e.add_field(name='Creador',
                    value=f'Fui creado por: **{app.owner}**',
                    inline=False)
        e.add_field(name='Prefijos',
                    value=f'Mis prefijos son: **{prefix[0]}**, **{prefix[1]}**'
                          f' y **{prefix[2]}**',
                    inline=False)
        e.add_field(name='Usuarios',
                    value=f'Puedo ver a un total de **{users}** usuarios entre'
                          ' todos los servidores en los que participo.',
                    inline=False)
        e.add_field(name='Invitación',
                    value='Puedes invitarme a tu servidor a través de este'
                          ' [link](https://discord.com/api/oauth2/authorize?'
                          'client_id=820819824669491210&permissions=8'
                          '&scope=bot)',
                    inline=False)
        await ctx.send(embed=e)

    @commands.command(aliases=['svinfo'],
                      help='Obtén información sobre este servidor.')
    async def serverinfo(self, ctx):
        e = guildEmbed(ctx.guild)
        await ctx.send(embed=e)

    @commands.command(aliases=['usinfo', 'uinfo'],
                      help='Obtén información acerca de ti o alguien más.')
    async def userinfo(self, ctx, member: Member = None):
        if member is not None:
            e = memberEmbed(member)
            await ctx.send(embed=e)
        else:
            e = memberEmbed(ctx.author)
            await ctx.send(embed=e)

    @commands.command(aliases=['avatar', 'av'],
                      help='Obtén tu avatar o de alguien más.')
    async def useravatar(self, ctx, member: Member = None):
        if member is not None:
            e = discord.Embed(color=f.rbColor())
            e.set_author(name=member.name, icon_url=member.avatar_url)
            e.set_image(url=member.avatar_url)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=f.rbColor())
            e.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            e.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Information(bot))
