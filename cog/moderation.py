import discord
from discord.ext import commands

import datetime


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', aliases=['ban'])
    @commands.has_guild_permissions(ban_members=True)
    async def banear(self, ctx, member: discord.Member = None, *, reason=None):
        guild = ctx.guild

        if member is not None:
            await ctx.send('¿Por qué motivo?')

            def check(m):
                return ctx.author == m.author

            msg = await self.bot.wait_for(
                'message', check=check, timeout=60.0
            )
            await ctx.send('Bien, ¿deberían borrarse su mensajes?')
            msg2 = await self.bot.wait_for(
                'message', check=check, timeout=60.0
            )

            if msg2.content == 'si':
                await ctx.send('¿Los mensajes de cuantos días? (máximo 7)')
                msg3 = await self.bot.wait_for(
                    'message',
                    check=check,
                    timeout=60.0,
                )
                await member.ban(
                    reason=msg.content,
                    delete_message_days=msg3.content,
                )
                embed = discord.Embed(
                    title='Tribunal de justicia',
                    description='Se expulsa a:',
                    color=discord.Color.blue(),
                    timestamp=datetime.datetime.utcnow(),
                )
                embed.set_thumbnail(
                    url=guild.icon_url
                )
                embed.add_field(
                    name=f'{member}',
                    value=f'Por *"{msg.content}"*, borrándose sus'
                          f' mensajes hasta {msg3.content} atrás.',
                    inline=False
                )
                embed.add_field(
                    name='Orden tomada por:',
                    value=ctx.author.name,
                    inline=False
                )
                embed.set_footer(
                    text=guild,
                    icon_url=guild.icon_url,
                )
                await ctx.send(embed=embed)

            elif msg2.content == 'no':
                await member.ban(reason=msg.content)
                embed = discord.Embed(
                    title='Tribunal de justicia',
                    description='Se expulsa a:',
                    color=discord.Color.blue(),
                    timestamp=datetime.datetime.utcnow(),
                )
                embed.set_thumbnail(
                    url=guild.icon_url
                )
                embed.add_field(
                    name=f'{member}',
                    value=f'Por: **"{msg.content}"**',
                    inline=False
                )
                embed.add_field(
                    name='Orden tomada por:',
                    value=ctx.author.name,
                    inline=False
                )
                embed.set_footer(
                    text=guild,
                    icon_url=guild.icon_url,
                )
                await ctx.send(embed=embed)

            else:
                await ctx.send('Deberías escribir "si" o "no".')

        else:
            await ctx.send('Debes mencionar a alguien.')

    @commands.command(name='fastban', aliases=['fb'])
    @commands.has_guild_permissions(ban_members=True)
    async def banearapido(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send('¿Es una decisión segura?')

        def check(m):
            return ctx.author == m.author

        msg = await self.bot.wait_for(
            'message', check=check, timeout=60.0
        )
        if msg.content == 'si':
            await member.ban(reason=reason)
            await ctx.send(f'{member} fue baneado por {reason}.')

        elif msg.content == 'no':
            await ctx.send('Mejor piensa bien una decisión como esa.')

        else:
            await ctx.send('Deberías escribir "si" o "no".')

    @commands.command(name='unban', aliases=['ub'])
    @commands.has_guild_permissions(ban_members=True)
    async def desbanear(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.name}#{user.discriminator} '
                               'fue desbaneado.')


def setup(bot):
    bot.add_cog(Moderation(bot))
