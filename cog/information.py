import discord
import json
from cog.functions import rbColor
from discord.guild import Guild
from discord.ext import commands


def month_name(month: int):
    """Returns the month name based in its order number."""
    with open('databases/db_str.json') as db:
        data = db.read()
        months = json.loads(data)
        selected_month = months['months'][month]
        return selected_month


class Member():
    """Member related information."""
    def creation(member: discord.Member):
        """Returns a sentence with the creation date of the user's account."""
        creation_date = str(member.created_at)[:10]
        year, month, day = creation_date.split('-')
        created_month = month_name(int(month))
        creation_sentence = 'Su cuenta se creó el día {} de {} del año {}.'
        member_created_at = creation_sentence.format(day, created_month, year)
        return member_created_at

    def joined(member: discord.Member):
        """Returns a sentence with the join date of the user to the server."""
        joined_date = str(member.joined_at)[:10]
        year, month, day = joined_date.split('-')
        joined_month = month_name(int(month))
        joined_sentence = 'Se unió el día {} de {} del año {}.'
        member_joined_at = joined_sentence.format(day, joined_month, year)
        return member_joined_at

    def roles(member: discord.Member):
        """Returns a string with all of the user's roles"""
        string = ' '
        roles = member.roles
        for role in roles:
            if role.name == '@everyone':
                string += ''
            else:
                string += f'<@&{role.id}> '

        return string

    def embed(member: discord.Member):
        """Returns an embed with information of the member."""
        e = discord.Embed(title=member.name, color=member.color)
        e.set_thumbnail(url=member.avatar_url)
        e.add_field(name='Color', value=member.color, inline=False)
        e.add_field(name='Rol más alto', value=member.top_role, inline=False)
        e.add_field(name='Creación', value=Member.creation(member),
                    inline=False)
        e.add_field(name='Llegada al servidor', value=Member.joined(member),
                    inline=False)
        e.add_field(name='Roles', value=Member.roles(member))
        return e


class Server():
    """Guild related information."""
    def guild_creation(guild: Guild):
        """Returns a sentence with the creation date of the guild."""
        creation_date = str(guild.created_at)[:10]
        year, month, day = creation_date.split('-')
        creation_month = month_name(int(month))
        creation_sentence = '{} de {} del año {}.'
        guild_created_at = creation_sentence.format(day, creation_month, year)
        return guild_created_at

    def guild_embed(guild: Guild):
        """Returns an embed with information about the guild."""
        e = discord.Embed(title=guild.name, color=rbColor())
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name='🚻 Miembros',
                    value=f'**{len(guild.members)}** miembros.')
        e.add_field(name='⚙ Categorías',
                    value=f'**{len(guild.categories)}** categorías.')
        e.add_field(name='📢 Canales',
                    value=f'**{len(guild.channels)}** canales en total.\n '
                          f'**{len(guild.text_channels)}** canales de texto.\n'
                          f' **{len(guild.voice_channels)}** canales de voz.')
        e.add_field(name='🤡 Emojis', value=f'**{len(guild.emojis)}** emojis.')
        e.add_field(name='🛡 Roles', value=f' **{len(guild.roles)}** roles.')
        e.add_field(name='🔧 Creación', value=Server.guild_creation(guild))
        e.add_field(name='🔗 Identificador', value=guild.id)
        e.add_field(name='🤴 Dueño/a del servidor',
                    value=f'**{guild.owner.mention}**')
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
                          color=rbColor())
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
        e = Server.guild_embed(ctx.guild)
        await ctx.send(embed=e)

    @commands.command(aliases=['usinfo', 'uinfo'],
                      help='Obtén información acerca de ti o alguien más.')
    async def userinfo(self, ctx, member: Member = None):
        if member is not None:
            e = Member.embed(member)
            await ctx.send(embed=e)
        else:
            e = Member.embed(ctx.author)
            await ctx.send(embed=e)

    @commands.command(aliases=['avatar', 'av'],
                      help='Obtén tu avatar o de alguien más.')
    async def useravatar(self, ctx, member: Member = None):
        if member is not None:
            e = discord.Embed(color=rbColor())
            e.set_author(name=member.name, icon_url=member.avatar_url)
            e.set_image(url=member.avatar_url)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            e.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Information(bot))
