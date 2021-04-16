import discord
from discord.ext import commands

import datetime

bot_icon = 'https://i.imgur.com/e4aMdPk.jpg'


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info'])
    async def informacion(self, ctx):
        actual_guild = ctx.guild
        actual_guild_icon = ctx.guild.icon_url
        guilds = self.bot.guilds
        guilds_count = len(guilds)
        embed = discord.Embed(
            title='RoboTito',
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(name='Información sobre')
        embed.set_thumbnail(url=bot_icon)
        embed.add_field(
            name='Actualmente participo en:',
            value=f'{guilds_count} servidores.',
            inline=False
        )
        embed.add_field(
            name='¿Tienes dudas?',
            value='Consulta mi documentación en'
                  ' [readme.io](https://robotito.readme.io/)',
            inline=False
        )
        embed.set_footer(
            text=actual_guild,
            icon_url=actual_guild_icon
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['docs'])
    async def documentacion(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(
            name='Documentación de RoboTito',
            value='[Revisá la documentación en readme.io]'
                  '(https://robotito.readme.io)'
        )
        embed.set_image(url='https://i.imgur.com/eV8Uch6.png')
        embed.set_footer(text='Información de RoboTito')
        await ctx.send(embed=embed)

    @commands.command(aliases=['svinfo'])
    async def serverinfo(self, ctx):
        guild = ctx.guild
        members = guild.member_count
        owner = guild.owner
        creation = str(guild.created_at)[:10]
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(
            name=guild.name,
            icon_url=guild.icon_url
        )
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(
            name='Cantidad de usuarios:',
            value=members,
            inline=True
        )
        embed.add_field(
            name='El/La propietario/a del servidor es:',
            value=owner,
            inline=False
        )
        embed.add_field(
            name='El servidor se creó el:',
            value=creation,
            inline=False
        )
        embed.set_footer(text='Información de RoboTito')
        await ctx.send(embed=embed)

    @commands.command()
    async def myinfo(self, ctx):
        author = ctx.message.author
        nick = author.nick
        join_date = str(author.joined_at)[:10]
        creation_date = str(author.created_at)[:10]
        if nick is not None:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(
                name=author,
                icon_url=author.avatar_url
            )
            embed.set_thumbnail(url=author.avatar_url)
            embed.add_field(
                name='Nombre:',
                value=f'{author.name}',
                inline=False
            )
            embed.add_field(
                name='Apodo',
                value=author.nick,
                inline=False
            )
            embed.add_field(
                name='ID',
                value=author.id,
                inline=False
            )
            embed.add_field(
                name='Se unió el:',
                value=join_date,
                inline=False
            )
            embed.add_field(
                name='La cuenta se creó el:',
                value=creation_date,
                inline=False
            )
            embed.set_footer(text='Información de RoboTito')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(
                name=author,
                icon_url=author.avatar_url
            )
            embed.set_thumbnail(url=author.avatar_url)
            embed.add_field(
                name='Nombre:',
                value=f'{author.name}',
                inline=False
            )
            embed.add_field(name='ID', value=author.id, inline=False)
            embed.add_field(
                name='Se unió el:',
                value=join_date,
                inline=False
            )
            embed.add_field(
                name='La cuenta se creó el:',
                value=creation_date,
                inline=False
            )
            embed.set_footer(text='Información de RoboTito')
            await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        join_date = str(member.joined_at)[:10]
        creation_date = str(member.created_at)[:10]
        nick = member.nick
        if nick is not None:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(
                name=member.name,
                icon_url=member.avatar_url
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(
                name='Nombre:',
                value=f'{member.name}',
                inline=False
            )
            embed.add_field(
                name='Apodo',
                value=member.nick,
                inline=False
            )
            embed.add_field(
                name='ID',
                value=member.id,
                inline=False
            )
            embed.add_field(
                name='Se unió el:',
                value=join_date,
                inline=False
            )
            embed.add_field(
                name='La cuenta se creó el:',
                value=creation_date,
                inline=False
            )
            embed.set_footer(text='Información de RoboTito')
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.set_author(
                name=member.name,
                icon_url=member.avatar_url
            )
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(
                name='Nombre:',
                value=f'{member.name}',
                inline=False
            )
            embed.add_field(
                name='ID',
                value=member.id,
                inline=False
            )
            embed.add_field(
                name='Se unió el:',
                value=join_date,
                inline=False
            )
            embed.add_field(
                name='La cuenta se creó el:',
                value=creation_date,
                inline=False
            )
            embed.set_footer(text='Información de RoboTito')
            await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        help_embed = discord.Embed(
            title='¡Hola! sé que tratar conmigo puede ser un poco complicado, '
                  'pero vengo a hacerte la vida más fácil.',
            colour=discord.Colour.blue(),
            timestamp=datetime.datetime.utcnow()
        )
        help_embed.set_thumbnail(
            url=bot_icon
        )
        help_embed.add_field(
            name='Ayuda general:',
            value='Para una guía completa sobre RoboTito, visitá la '
            '[documentación oficial](https://robotito.readme.io)',
            inline=False
        )
        help_embed.add_field(
            name='Comandos:',
            value='Para obtener información sobre los comandos, '
                  'revisá el apartado de [Comandos]'
                  '(https://robotito.readme.io/reference#comandos-1)',
            inline=False
        )
        help_embed.add_field(
            name='Errores:',
            value='Para conocer los códigos de error, revisá el apartado de '
                  '[Errores]'
                  '(https://robotito.readme.io/reference#errores-1)',
            inline=False
        )
        help_embed.set_footer(
            text='Ayuda de RoboTito'
        )
        await ctx.send(embed=help_embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        if member is None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Avatar de:',
                value=ctx.author
            )
            embed.set_image(
                url=ctx.author.avatar_url
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Avatar de:',
                value=member.display_name
            )
            embed.set_image(
                url=member.avatar_url
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
