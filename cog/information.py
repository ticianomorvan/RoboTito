import discord
import datetime
import json
from discord.member import Member
from discord.ext import commands


bot_icon = 'https://i.imgur.com/e4aMdPk.jpg'

color = discord.Color.blue()

time = datetime.datetime.utcnow()


def embedUser(
    uName, uIcon, uColor, cDay, cMonth, cYear, jDay, jMonth, jYear,
        uTop_role):
    e = discord.Embed(
        color=uColor,
        time=time
    )
    e.set_author(
        name=uName
    )
    e.set_thumbnail(
        url=uIcon
    )
    e.add_field(
        name='Color',
        value=uColor,
        inline=False
    )
    e.add_field(
        name='Rol más alto',
        value=uTop_role,
        inline=False
    )
    e.add_field(
        name='Su cuenta se creó el día',
        value=f'{cDay} de {cMonth} del año {cYear}.',
        inline=False
    )
    e.add_field(
        name='Se unió a este servidor el día',
        value=f'{jDay} de {jMonth} del año {jYear}.',
        inline=False
    )
    return e


def monthName(month: int):
    with open('databases/db_str.json') as f:
        data = f.read()
        months = json.loads(data)
        selectMonth = months['months'][month]
        return selectMonth


class Information(commands.Cog,
                  name='Información',
                  description='Obtén información sobre el bot, '
                              'el servidor o un usuario.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info', 'información', 'botinfo'],
                      help='Obtén información del bot.')
    async def botInfo(self, ctx):
        gs = self.bot.guilds
        gs_count = len(gs)

        embed = discord.Embed(
            color=color,
            timestamp=time
        )
        embed.set_author(
            name='RoboTito',
            url='https://att-inc.github.io/RoboTito',
            icon_url=bot_icon
        )
        embed.set_thumbnail(
            url=bot_icon
        )
        embed.add_field(
            name='Actualmente participo en:',
            value=f'{gs_count} servidores.',
            inline=False
        )
        embed.add_field(
            name='Para invitarme a un servidor:',
            value='Usá este [link](https://discord.com/api/oauth2/'
                  'authorize?client_id=820819824669491210&permiss'
                  'ions=8&scope=bot)',
            inline=False
        )
        embed.add_field(
            name='Mi código fuente está en:',
            value='[RoboTito, por ATT-Inc]'
                  '(https://github.com/Ti7oyan/RoboTito)',
            inline=False
        )
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['svinfo', 'infosv'],
                      help='Obtén información del servidor.')
    async def serverInfo(self, ctx):
        guildCreation = str(ctx.guild.created_at)[:10]
        gYear, gMonth, gDay = guildCreation.split('-')
        month = monthName(int(gMonth))

        embed = discord.Embed(
            color=color
        )
        embed.set_author(
            name=f'{ctx.guild.name}, de {ctx.guild.owner}.',
            icon_url=ctx.guild.icon_url
        )
        embed.set_thumbnail(
            url=ctx.guild.icon_url
        )
        embed.add_field(
            name='Cuenta con un total de',
            value=f'{ctx.guild.member_count} usuarios.',
            inline=False,
        ),
        embed.add_field(
            name='El servidor se creó el día',
            value=f'{gDay} de {month} del año {gYear}.',
            inline=False,
        )
        embed.add_field(
            name='Existen en total',
            value=f'{len(ctx.guild.channels)} canales'
                  f' y {len(ctx.guild.categories)} categorías.',
            inline=False
        )
        embed.add_field(
            name='Cuenta con',
            value=f'{len(ctx.guild.emojis)} emojis en total.',
            inline=False
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['servericon', 'svicon', 'guildicon', 'gicon'],
                      help='Obtén el ícono del servidor.')
    async def serverIcon(self, ctx):
        e = discord.Embed(
            color=color,
            timestamp=time
        )
        e.set_author(
            name=ctx.guild.name,
            icon_url=ctx.guild.icon_url
        )
        e.set_image(
            url=ctx.guild.icon_url
        )
        e.set_footer(
            text=ctx.author.name,
            icon_url=ctx.author.avatar_url
        )

        await ctx.send(embed=e)

    @commands.command(aliases=['userinfo', 'infodelusuario', 'uinfo'],
                      help='Obtén información del usuario.')
    async def userInfo(self, ctx, member: Member = None):
        if member is not None:
            memberCreation = str(member.created_at)[:10]
            cYear, cMonth, cDay = memberCreation.split('-')
            crMonth = monthName(int(cMonth))

            memberJoined = str(member.joined_at)[:10]
            jYear, jMonth, jDay = memberJoined.split('-')
            joMonth = monthName(int(jMonth))

            e = embedUser(
                member.name, member.avatar_url, member.color, cDay, crMonth,
                cYear, jDay, joMonth, jYear, member.top_role)

            await ctx.send(embed=e)

        else:
            authorCreation = str(ctx.author.created_at)[:10]
            cYear, cMonth, cDay = authorCreation.split('-')
            crMonth = monthName(int(cMonth))

            authorJoined = str(ctx.author.joined_at)[:10]
            jYear, jMonth, jDay = authorJoined.split('-')
            joMonth = monthName(int(jMonth))

            e = embedUser(
                ctx.author.name, ctx.author.avatar_url, ctx.author.color, cDay,
                crMonth, cYear, jDay, joMonth, jYear, ctx.author.top_role)

            await ctx.send(embed=e)

    @commands.command(aliases=['av', 'avatar', 'useravatar', 'usericon'],
                      help='Obtén la foto de perfil de un usuario.')
    async def userAvatar(self, ctx, member: Member = None):
        if member is not None:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.set_author(
                name=member.name,
                icon_url=member.avatar_url
            )
            e.set_image(
                url=member.avatar_url
            )
            e.set_footer(
                text=ctx.guild.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.set_author(
                name=ctx.author.name,
                icon_url=ctx.author.avatar_url
            )
            e.set_image(
                url=ctx.author.avatar_url
            )
            e.set_footer(
                text=ctx.guild.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Information(bot))
