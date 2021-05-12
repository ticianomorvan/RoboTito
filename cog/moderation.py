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
    async def ban(self, ctx, member: discord.Member = None):

        def author(m):
            return ctx.author == m.author

        if member is None:
            await ctx.send('Por favor, menciona a quien quieres expulsar.')

        elif member.bot is True:
            await ctx.send('No deberías usar este comando para expulsar bots.')

        else:
            await ctx.send('¿Por qué motivo?')

            try:
                msg = await self.bot.wait_for('message',
                                              check=author,
                                              timeout=30.0)

            except asyncio.TimeoutError:
                await ctx.send('Debiste apurarte, por favor, '
                               'vuelve a introducir el comando.')

            else:
                if not msg.content:
                    await ctx.send('Por favor, dime la razón para expulsar'
                                   ' al usuario.')

                else:
                    await ctx.send('Bien, ¿deberían borrarse sus mensajes?')

                    try:
                        msg2 = await self.bot.wait_for('message',
                                                       check=author,
                                                       timeout=30.0)

                    except asyncio.TimeoutError:
                        await ctx.send('El tiempo se acabó, vuelve a '
                                       'introducir el comando.')

                    if not msg2.content:
                        await ctx.send('Debo saber si precisas borrar '
                                       'sus mensajes o no.')

                    else:
                        if msg2.content in ['no', 'No', 'NO']:
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

                        elif msg2.content == 'si':
                            await ctx.send('¿Los mensajes de cuántos días?'
                                           '(máximo 7)')

                            try:
                                msg3 = await self.bot.wait_for('message',
                                                               check=author,
                                                               timeout=30.0)

                            except asyncio.TimeoutError:
                                await ctx.send('Se acabó el tiempo.')

                            if not msg3.content:
                                await ctx.send('Necesito saber cuantos días '
                                               'de mensajes debo borrar.')

                            else:
                                if msg3.content <= 7:
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

                                else:
                                    await ctx.send('No puedo borrar mensajes '
                                                   'más allá de los 7 días.')

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
    async def unban(self, ctx, *, mm):

        if mm is not None:
            banned_users = await ctx.guild.bans()
            mm_name, mm_disc = mm.split('#')

            a = ctx.author
            g = ctx.guild
            d = datetime.datetime.utcnow()

            def author(m):
                return m.author == ctx.author

            await ctx.send('¿Es una decisión segura?')

            try:
                msg = await self.bot.wait_for('message',
                                              check=author,
                                              timeout=30.0)

            except asyncio.TimeoutError:
                await ctx.send('El tiempo se acabó, '
                               'vuelve a intentarlo.')

            else:
                if msg.content in ['Si', 'si', 'Yes', 'yes']:

                    for ban_entry in banned_users:
                        u = ban_entry.user

                        if (u.name, u.discriminator) == (mm_name, mm_disc):

                            await ctx.guild.unban(u)

                            embed = discord.Embed(title='Tribunal de Justicia',
                                                  description='Se revoca la '
                                                              'expulsión de:',
                                                  color=discord.Color.blue(),
                                                  timestamp=d)
                            embed.set_thumbnail(url=g.icon_url)
                            embed.add_field(name=f'{u.name}#'
                                                 f'{u.discriminator}',
                                            value='Ahora puede volver '
                                                  'al serivdor.')
                            embed.add_field(name='Orden tomada por:',
                                            value=a.name,
                                            inline=False)
                            embed.set_footer(text=a.name,
                                             icon_url=a.avatar_url)

                            await ctx.send(embed=embed)

                        else:
                            await ctx.send('Ese usuario no se '
                                           'encuentra baneado.')

                elif msg.content in ['no', 'No']:
                    await ctx.send('Mejor piensa más una decisión así.')

                else:
                    await ctx.send('Preferiría que me digas "si" o "no".')

        else:
            await ctx.send('Debes escribir el nombre del usuario '
                           'y su discriminador, por ejemplo: '
                           'RoboTito#1684')

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

    @commands.command(name='nick',
                      aliases=['changenick', 'apodo'],
                      description='Cambia el apodo de otra persona.')
    async def nick(self, ctx, member: discord.Member = None):

        def author(m):
            return m.author == ctx.author

        if ctx.message.author.guild_permissions.manage_nicknames:
            if member is not None:
                last_nick = member.nick

                await ctx.send(f'¿Qué apodo le quieres poner a {member.name}?')

                try:
                    nick = await self.bot.wait_for('message',
                                                   check=author,
                                                   timeout=30.0)

                except asyncio.TimeoutError:
                    await ctx.send('Tiempo expirado.')

                else:
                    if nick.content is not None:
                        await member.edit(nick=nick.content)
                        await ctx.send('¡Apodo cambiado correctamente! '
                                       f'Ahora el apodo de {member.name} es: '
                                       f'**{member.nick}**, '
                                       f'antes *{last_nick}*.')
                    else:
                        await ctx.send('Necesito saber que apodo '
                                       'le quieres poner.')

            else:
                await ctx.send('No puedo cambiar el apodo de un administrador '
                               'o moderador, en su lugar, cambia tu apodo a '
                               'través de la función de Discord.')

        else:
            if member is not None:
                await ctx.send('No tienes los permisos para cambiar '
                               'el apodo de alguien más.')

            else:
                await ctx.send('¿Qué apodo te quieres poner?')

                try:
                    nick = await self.bot.wait_for('message',
                                                   check=author,
                                                   timeout=30.0)

                except asyncio.TimeoutError:
                    await ctx.send('Tiempo expirado.')

                else:
                    if nick.content is not None:
                        await ctx.author.edit(nick=f'{nick.content}')
                        await ctx.send('¡Genial! ahora tu apodo es '
                                       f'**{ctx.author.nick}**, antes '
                                       f'{last_nick}')


def setup(bot):
    bot.add_cog(Moderation(bot))
