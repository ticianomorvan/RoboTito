import asyncio
import discord
import cog.functions as f
from discord.member import Member
from discord.ext import commands
from discord.guild import Guild


async def sleep(seconds):
    time = float(seconds)
    await asyncio.sleep(time)


def guild_embed(guild: Guild, action, member: Member, aReason=None):
    if aReason is not None:
        e = discord.Embed(color=f.rbColor())
        e.set_author(name=guild.name, icon_url=guild.name)
        e.set_thumbnail(url=member.avatar_url)
        e.add_field(name=f'**{member.name}** fue {action}',
                    value=f'Con el motivo de "{aReason}".')
        return e
    else:
        e = discord.Embed(color=f.rbColor())
        e.set_author(name=guild.name, icon_url=guild.name)
        e.set_thumbnail(url=member.avatar_url)
        e.add_field(name=f'**{member.name}** fue {action}',
                    value='Sin motivos especificados.')
        return e


def user_embed(guild: Guild, action, aReason=None):
    if aReason is not None:
        e = discord.Embed(color=f.rbColor())
        e.set_author(name=guild.name, icon_url=guild.icon_url)
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name=f'Fuiste {action} de **{guild.name}**',
                    value=f'Con el motivo de "{aReason}".')
        return e
    else:
        e = discord.Embed(color=f.rbColor())
        e.set_author(name=guild.name, icon_url=guild.icon_url)
        e.set_thumbnail(url=guild.icon_url)
        e.add_field(name=f'Fuiste {action} de **{guild.name}**',
                    value='Sin motivos especificados.')
        return e


class Moderation(commands.Cog,
                 name='Moderación',
                 description='Herramientas útiles para moderadores.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'],
                      help='Prohibe el reingreso al servidor a un usuario.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: Member, reason=None):
        if reason is not None:
            await member.ban(reason=reason)
            gE = guild_embed(ctx.guild, 'vetado', member, reason)
            await ctx.send(embed=gE)

            uE = user_embed(ctx.guild, 'vetado', reason)
            await member.send(embed=uE)

        else:
            await member.ban()
            gE = guild_embed(ctx.guild, 'vetado', member)
            await ctx.send(embed=gE)

            uE = user_embed(ctx.guild, 'vetado')
            await member.send(embed=uE)

    @commands.command(aliases=['k'], help='Expulsa a un usuario.')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: Member, reason=None):
        if reason is not None:
            await member.kick(reason=reason)
            gE = guild_embed(ctx.guild, 'expulsado', member, reason)
            await ctx.send(embed=gE)

            uE = user_embed(ctx.guild, 'expulsado', reason)
            await member.send(embed=uE)

        else:
            await member.kick(reason=reason)
            gE = guild_embed(ctx.guild, 'expulsado', member)
            await ctx.send(embed=gE)

            uE = user_embed(ctx.guild, 'expulsado',)
            await member.send(embed=uE)

    @commands.command(aliases=['ub'],
                      help='Permite el regreso de un usuario vetado.')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, *, mm):
        if mm is not None:
            banned_users = await ctx.guild.bans()
            mm_name, mm_disc = mm.split('#')

            for ban_entry in banned_users:
                u = ban_entry.user
                if (u.name, u.discriminator) == (mm_name, mm_disc):
                    await ctx.guild.unban(u)
                    await ctx.send(f'**{mm}** ya puede volver al servidor.')
                else:
                    await ctx.send('Ese usuario no se encuentra baneado.')
        else:
            await ctx.send('Debes escribir el nombre del usuario'
                           ' y su discriminador, por ejemplo:'
                           ' **RoboTito#1684**')

    @commands.command(aliases=['c'],
                      help='Borra mensajes en un canal específico.')
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(self, ctx, amount=100):
        if amount > 100:
            await ctx.send('Solo puedo borrar 100 mensajes o menos que'
                           ' hayan sido enviados dentro de los últimos'
                           ' catorce días.', delete_after=5.0)
        else:
            await ctx.channel.purge(limit=amount)
            await sleep(1)
            await ctx.send(f'Borrados **{amount}** mensajes en'
                           f' {ctx.channel.mention} por {ctx.author.name}.')

    @commands.command(name='nick', aliases=['apodo'],
                      help='Cambia tu apodo o el de otro usuario.')
    async def nick(self, ctx, *, nick: str, member: Member = None):
        if member is not None:
            if ctx.author.guild_permissions.manage_nicknames is True:
                await member.edit(nick=nick)
            else:
                await ctx.send('No tienes los permisos necesarios.')
        else:
            await ctx.author.edit(nick=nick)


def setup(bot):
    bot.add_cog(Moderation(bot))
