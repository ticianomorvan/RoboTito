import discord
from discord.ext import commands

import time

import datetime


class Moderation(
    commands.Cog,
    name='Moderación',
    description='Herramientas útiles para moderadores.'
):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', aliases=['b'])
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

            else:
                await ctx.send(
                    'Ese usuario no se encuentra baneado.'
                )

    @commands.command(aliases=['c'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(self, ctx, amount=100):
        await ctx.send(
            '¿Estás segur@?'
        )

        def mod(m):
            return m.author == ctx.message.author

        confirm = await self.bot.wait_for(
            'message', check=mod, timeout=60.0
        )
        if confirm.content == 'si':
            try:
                message = await ctx.send('Preparando limpieza.')
                time.sleep(0.35)
                await message.edit(content='Preparando limpieza..')
                time.sleep(0.35)
                await message.edit(content='Preparando limpieza...')
                time.sleep(0.35)
                await message.edit(content='Ultimando detalles.')
                time.sleep(0.35)
                await message.edit(content='Ultimando detalles..')
                time.sleep(0.35)
                await message.edit(content='Ultimando detalles...')
                time.sleep(0.55)
                await ctx.channel.purge(limit=amount, bulk=True)
                time.sleep(1.15)
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.add_field(name='¡Limpieza a la orden!',
                                value=f'Borré {amount} mensajes '
                                      f'en el canal de {ctx.channel.name}')
                embed.set_image(url='https://media1.tenor.com/images/'
                                    '980fefd36ce46e30bb11e8861fa20633/'
                                    'tenor.gif')
                embed.set_footer(text='Limpieza de RoboTito')
                await ctx.send(embed=embed)

            except TimeoutError:
                await ctx.send(
                    'Se acabó el tiempo.'
                )

        elif confirm.content == 'no':
            await ctx.send(
                'Te dejo un rato para que lo pienses.'
            )

        else:
            await ctx.send(
                'No recibí ninguna respuesta.'
            )

    @commands.command(aliases=['fc'])
    @commands.has_guild_permissions(manage_messages=True)
    async def fastclean(self, ctx, amount=100):
        await ctx.send(
            '¿Estás segur@?'
        )

        def mod(m):
            return m.author == ctx.message.author

        confirm = await self.bot.wait_for(
            'message', check=mod, timeout=60.0
        )
        if confirm.content == 'si':
            try:
                await ctx.channel.purge(limit=amount, bulk=True)
                await ctx.send(f'Se borraron {amount} mensajes.')

            except TimeoutError:
                await ctx.send('Se acabó el tiempo.')

        elif confirm.content == 'no':
            await ctx.send(
                'Deberías asegurarte antes de tomar una decisión como esa.'
            )

        else:
            await ctx.send(
                'No recibí ninguna respuesta.'
            )


def setup(bot):
    bot.add_cog(Moderation(bot))
