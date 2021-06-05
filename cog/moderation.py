import asyncio
from discord.member import Member
from discord.ext import commands


async def sleep(seconds):
    time = float(seconds)
    await asyncio.sleep(time)


class Moderation(commands.Cog,
                 name='Moderación',
                 description='Herramientas útiles para moderadores.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'], help='Expulsa a un usuario.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: Member, reason=None):
        if reason is not None:
            await member.ban(reason=reason)
            await ctx.send(
                f'**{member.name}** fue expulsado del servidor '
                f'por "{reason}"'
            )
            await member.send(
                f'Fuiste expulsado de {ctx.guild.name} por {reason}.'
            )
        else:
            await member.ban()
            await ctx.send(
                f'**{member.name}** fue expulsado del servidor.'
            )
            await member.send(
                f'Fuiste expulsado de {ctx.guild.name}.'
            )

    @commands.command(
        aliases=['ub'], help='Permite el regreso de un usuario expulsado.'
    )
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
                    await ctx.send('Ese usuario no se '
                                   'encuentra baneado.')

        else:
            await ctx.send('Debes escribir el nombre del usuario'
                           'y su discriminador, por ejemplo:'
                           ' **RoboTito#1684**')

    @commands.command(
        aliases=['c'], help='Borra mensajes en un canal específico.'
    )
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

    @commands.command(
        name='nick', aliases=['apodo'],
        help='Cambia tu apodo o el de otro usuario.'
    )
    async def nick(self, ctx, nick: str, member: Member = None):
        if ctx.author.guild_permissions.manage_nicknames is True:
            if member is not None:
                await member.edit(nick=nick)
            else:
                await ctx.send('No puedo cambiar el apodo de alguien'
                               ' con un rol superior al mio.')
        else:
            await ctx.author.edit(nick=nick)


def setup(bot):
    bot.add_cog(Moderation(bot))
