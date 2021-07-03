import asyncio
import discord
from cog.functions import rbColor
from discord.ext import commands


async def sleep(seconds):
    time = float(seconds)
    await asyncio.sleep(time)


class Messages():
    def guild(guild: discord.Guild, member: discord.Member,
              action, moderator: discord.Member, reason=None):
        e = discord.Embed(color=rbColor())
        e.set_author(name=guild.name, icon_url=guild.icon_url)
        e.set_thumbnail(url=member.avatar_url)
        if reason is not None:
            e.add_field(name=f'{member.name} fue {action}.',
                        value=f'Por "{reason}".')
        else:
            e.add_field(name=f'{member.name} fue {action}.',
                        value='Sin motivos especificados.')

        e.add_field(name='Moderador a cargo:',
                    value=moderator.name,
                    inline=False)
        return e

    def user(guild: discord.Guild, action, moderator: discord.Member,
             reason=None):
        e = discord.Embed(color=rbColor())
        e.set_author(name=guild.name, icon_url=guild.icon_url)
        e.set_thumbnail(url=guild.icon_url)
        if reason is not None:
            e.add_field(name=f'Fuiste {action} de {guild.name}.',
                        value=f'Debido a "{reason}".')
        else:
            e.add_field(name=f'Fuiste {action} de {guild.name}.',
                        value='Sin motivos especificados.')

        e.add_field(name='Moderador a cargo',
                    value=moderator.name,
                    inline=False)
        return e


class Moderation(commands.Cog,
                 name='Moderación',
                 description='Herramientas útiles para moderadores.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'],
                      help='Prohibe el reingreso al servidor a un usuario.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Embed, *, reason=None):
        if reason is not None:
            await member.ban(reason=reason)
            guild_embed = Messages.guild(ctx.guild, member, 'vetado',
                                         ctx.author, reason)
            await ctx.send(embed=guild_embed)

            user_embed = Messages.user(ctx.guild, 'vetado',
                                       ctx.author, reason)
            await member.send(embed=user_embed)

        else:
            await member.ban()
            guild_embed = Messages.guild(ctx.guild, member, 'vetado',
                                         ctx.author)
            await ctx.send(embed=guild_embed)

            user_embed = Messages.user(ctx.guild, 'vetado',
                                       ctx.author)
            await member.send(embed=user_embed)

    @commands.command(aliases=['k'], help='Expulsa a un usuario.')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if reason is not None:
            await member.kick(reason=reason)
            guild_embed = Messages.guild(ctx.guild, member, 'expulsado',
                                         ctx.author, reason)
            await ctx.send(embed=guild_embed)

            user_embed = Messages.user(ctx.guild, 'expulsado',
                                       ctx.author, reason)
            await member.send(embed=user_embed)

        else:
            await member.kick()
            guild_embed = Messages.guild(ctx.guild, member, 'expulsado',
                                         ctx.author)
            await ctx.send(embed=guild_embed)

            user_embed = Messages.user(ctx.guild, 'expulsado',
                                       ctx.author)
            await member.send(embed=user_embed)

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
    async def nick(self, ctx, *, nick: str, member: discord.Member = None):
        if member is not None:
            if ctx.author.guild_permissions.manage_nicknames is True:
                await member.edit(nick=nick)
            else:
                await ctx.send('No tienes los permisos necesarios.')
        else:
            await ctx.author.edit(nick=nick)


def setup(bot):
    bot.add_cog(Moderation(bot))
