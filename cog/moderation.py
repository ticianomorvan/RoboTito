import asyncio

import discord
from discord.ext import commands

import time

import datetime


class Moderation(commands.Cog,
                 name='Moderación',
                 description='Herramientas útiles para moderadores.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'], description='Expulsión completa.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):

        if member is not None:
            await ctx.send('¿Por qué motivo?')

            def check(m):
                return ctx.author == m.author

            try:
                msg = await self.bot.wait_for('message',
                                              check=check,
                                              timeout=30.0)

            except asyncio.TimeoutError:
                await ctx.send('Debiste apurarte.')

            else:
                if msg.content is not None:
                    await ctx.send('Bien, ¿deberían borrarse su mensajes?')

                    try:
                        msg2 = await self.bot.wait_for('message',
                                                       check=check,
                                                       timeout=30.0)

                    except asyncio.TimeoutError:
                        await ctx.send('¿Necesitas más tiempo?')

                    else:
                        if msg2.content == 'si':
                            await ctx.send('¿Los mensajes de cuantos días?'
                                           '(máximo 7)')

                            try:
                                msg3 = await self.bot.wait_for('message',
                                                               check=check,
                                                               timeout=30.0)

                            except asyncio.TimeoutError:
                                await ctx.send('Se acabó el tiempo.')

                            else:
                                if msg3.content is not None:
                                    await member.ban(
                                        reason=msg.content,
                                        delete_message_days=msg3.content)
                                    embed = discord.Embed(
                                        title='Tribunal de justicia',
                                        description='Se expulsa a:',
                                        color=discord.Color.blue(),
                                        timestamp=datetime.datetime.utcnow())
                                    embed.set_thumbnail(url=ctx.guild.icon_url)
                                    embed.add_field(
                                        name=f'{member}',
                                        value=f'Por *"{msg.content}"*, '
                                              'borrándose sus mensajes hasta '
                                              f'{msg3.content} atrás.',
                                        inline=False)
                                    embed.add_field(name='Orden tomada por:',
                                                    value=ctx.author.name,
                                                    inline=False)
                                    embed.set_footer(
                                        text=ctx.guild,
                                        icon_url=ctx.guild.icon_url)
                                    await ctx.send(embed=embed)

                        elif msg2.content == 'no':
                            await member.ban(reason=msg.content)
                            embed = discord.Embed(
                                title='Tribunal de justicia',
                                description='Se expulsa a:',
                                color=discord.Color.blue(),
                                timestamp=datetime.datetime.utcnow())
                            embed.set_thumbnail(url=ctx.guild.icon_url)
                            embed.add_field(name=f'{member}',
                                            value=f'Por: **"{msg.content}"**',
                                            inline=False)
                            embed.add_field(name='Orden tomada por:',
                                            value=ctx.author.name,
                                            inline=False)
                            embed.set_footer(text=ctx.guild,
                                             icon_url=ctx.guild.icon_url)
                            await ctx.send(embed=embed)

                else:
                    await ctx.send('Deberías escribir "si" o "no".')

        else:
            await ctx.send('Debes mencionar a alguien.')

    @commands.command(aliases=['fb'], description='Expulsión rápida.')
    @commands.has_guild_permissions(ban_members=True)
    async def fastban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send('¿Es una decisión segura?')

        def check(m):
            return ctx.author == m.author

        try:
            msg = await self.bot.wait_for('message',
                                          check=check,
                                          timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send('Terminó el tiempo.')

        else:
            if msg.content == 'si':
                await member.ban(reason=reason)
                await ctx.send(f'{member} fue baneado por {reason}.')

            elif msg.content == 'no':
                await ctx.send('Mejor piensa bien una decisión como esa.')

            else:
                await ctx.send('Deberías escribir "si" o "no".')

    @commands.command(aliases=['ub'],
                      description='Revocar la expulsión a un usuario.')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name,
                                                   member_discriminator):
                await ctx.guild.unban(user)

                embed = discord.Embed(title='Tribunal de Justicia',
                                      description='Se revoca la expulsión de:',
                                      color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow)
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.add_field(name=f'{user.name}#{user.discriminator}',
                                value='Ahora puede volver al serivdor.')
                embed.add_field(name='Orden tomada por:',
                                value=ctx.author.name)
                embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

                await ctx.send(embed=embed)

            else:
                await ctx.send('Ese usuario no se encuentra baneado.')

    @commands.command(aliases=['c'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(self, ctx, amount=100):
        await ctx.send('¿Estás segur@?')

        def mod(m):
            return m.author == ctx.message.author

        try:
            confirm = await self.bot.wait_for('message',
                                              check=mod,
                                              timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send('El tiempo se acabó.')

        else:
            if confirm.content == 'si':
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

            elif confirm.content == 'no':
                await ctx.send('Te dejo un rato para que lo pienses.')

            else:
                await ctx.send('Deberías decir algo como "si" o "no".')

    @commands.command(aliases=['fc'])
    @commands.has_guild_permissions(manage_messages=True)
    async def fastclean(self, ctx, amount=100):
        await ctx.send('¿Estás segur@?')

        def mod(m):
            return m.author == ctx.message.author

        try:
            confirm = await self.bot.wait_for('message',
                                              check=mod,
                                              timeout=30.0)

        except asyncio.TimeoutError:
            await ctx.send('Se acabó el tiempo.')

        else:
            if confirm.content == 'si':
                await ctx.channel.purge(limit=amount, bulk=True)
                await ctx.send(f'Se borraron {amount} mensajes.')

            elif confirm.content == 'no':
                await ctx.send('Deberías asegurarte antes de tomar '
                               'una decisión como esa.')


def setup(bot):
    bot.add_cog(Moderation(bot))
