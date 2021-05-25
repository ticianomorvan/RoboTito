import asyncio

import discord
from discord.ext import commands

import datetime


async def sleep(seconds):
    time = float(seconds)
    await asyncio.sleep(time)

color = discord.Color.blue()

timestamp = datetime.datetime.utcnow()

answersYes = ['si', 'Si', 'SI', 'yes', 'Yes', 'YES', 'por supuesto', 'lo es']

answersNo = ['no', 'No', 'NO', 'no lo es', 'la verdad no']


class Moderation(commands.Cog,
                 name='Moderación',
                 description='Herramientas útiles para moderadores.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['b'], description='Expulsión completa.')
    async def ban(self, ctx, member: discord.Member = None):
        a = ctx.author
        g = ctx.guild

        def author(m):
            return m.author == a

        if a.guild_permissions.ban_members is True:

            if member is None:
                await ctx.send('Por favor, menciona a'
                               ' quien quieres expulsar.')

            elif member.bot is True:
                await ctx.send('No deberías usar este comando'
                               ' para expulsar bots.')

            else:
                await ctx.send('¿Estás segur@?')

                try:
                    secure = await self.bot.wait_for('message',
                                                     check=author,
                                                     timeout=30.0)

                except asyncio.TimeoutError:
                    await ctx.send('El tiempo terminó')

                else:
                    if secure.content in answersYes:

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
                                await ctx.send('Por favor, dime la razón para'
                                               ' expulsar al usuario.')

                            else:
                                await member.ban(reason=msg.content)
                                embed = discord.Embed(title='Tribunal '
                                                            'de justicia',
                                                      description='Se expulsa'
                                                                  ' a:',
                                                      color=color,
                                                      timestamp=timestamp)
                                embed.set_thumbnail(url=g.icon_url)
                                embed.add_field(name=f'{member}',
                                                value='Por: '
                                                      f'**"{msg.content}"**',
                                                inline=False)
                                embed.add_field(name='Orden tomada por:',
                                                value=a.name,
                                                inline=False)
                                embed.set_footer(text=a.name,
                                                 icon_url=g.icon_url)

                                await ctx.send(embed=embed)

                    elif secure.content in answersNo:
                        await ctx.send('Piensa más una decisión como esa.')

                    else:
                        await ctx.send('No entendí tu respuesta,'
                                       ' escribe cosas como "si" o "no".')

        else:
            await ctx.send('Debería reportarte por eso,'
                           ' pero no lo intentes de nuevo.')

    @commands.command(aliases=['fb'], description='Expulsión rápida.')
    async def fastban(self, ctx, member: discord.Member, *, reason=None):
        a = ctx.author

        if a.guild_permissions.ban_members is True:

            def author(m):
                return m.author == a

            await ctx.send('¿Es una decisión segura?')

            try:
                msg = await self.bot.wait_for('message',
                                              check=author,
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
    async def clean(self, ctx, amount=100):
        g = ctx.guild
        a = ctx.author

        if a.guild_permissions.manage_messages is True:

            await ctx.send('¿Estás segur@?')

            def author(m):
                return m.author == a

            try:
                confirm = await self.bot.wait_for('message',
                                                  check=author,
                                                  timeout=30.0)

            except asyncio.TimeoutError:
                await ctx.send('El tiempo se acabó.')

            else:
                if confirm.content in ['si', 'Si', 'SI', 'yes', 'Yes', 'YES']:

                    # Editing the bot message

                    message = await ctx.send('Preparando limpieza.')
                    await sleep(0.5)
                    await message.edit(content='Preparando limpieza..')
                    await sleep(0.5)
                    await message.edit(content='Preparando limpieza...')
                    await sleep(0.5)
                    await message.edit(content='Ultimando detalles.')
                    await sleep(0.5)
                    await message.edit(content='Ultimando detalles..')
                    await sleep(0.5)
                    await message.edit(content='Ultimando detalles...')
                    await sleep(1)
                    await ctx.channel.purge(limit=amount, bulk=True)
                    await sleep(1.25)

                    embed = discord.Embed(color=discord.Color.blue(),
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name='¡Limpieza a la orden!',
                                    value=f'Borré {amount} mensajes '
                                          f'en el canal de {ctx.channel.name}')
                    embed.set_image(url='https://media1.tenor.com/images/'
                                        '980fefd36ce46e30bb11e8861fa20633/'
                                        'tenor.gif')
                    embed.set_footer(text=a.name, icon_url=g.icon_url)

                    await ctx.send(embed=embed)

                elif confirm.content in ['no', 'No', 'NO']:
                    await ctx.send('Te dejo un rato para que lo pienses.')

                else:
                    await ctx.send('Deberías decir algo como "si" o "no".')
        else:
            await ctx.send('No tenés los permisos necesarios para hacer esto.')

    @commands.command(aliases=['fc'], description='Borrá mensajes rápidamente')
    async def fastclean(self, ctx, amount=100):
        a = ctx.author

        if a.guild_permissions.manage_messages is True:

            await ctx.send('¿Estás segur@?')

            def author(m):
                return m.author == ctx.message.author

            try:
                confirm = await self.bot.wait_for('message',
                                                  check=author,
                                                  timeout=30.0)

            except asyncio.TimeoutError:
                await ctx.send('Se acabó el tiempo.')

            else:
                if confirm.content in ['si', 'Si', 'SI', 'yes', 'Yes', 'YES']:
                    await ctx.channel.purge(limit=amount, bulk=True)
                    await ctx.send(f'{amount} mensajes fueron borrados'
                                   f' por {a.name}')

                elif confirm.content in ['no', 'No', 'NO']:
                    await ctx.send('Deberías asegurarte antes de tomar '
                                   'una decisión como esa.')

        else:
            await ctx.send('No tenés los permisos para hacer eso.')

    @commands.command(name='nick',
                      aliases=['changenick', 'apodo'],
                      description='Cambia el apodo de otra persona.')
    async def nick(self, ctx, member: discord.Member = None):
        a = ctx.author

        def author(m):
            return m.author == a

        if a.guild_permissions.manage_nicknames is True:
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
                await ctx.send('Lo siento, no puedo cambiar el apodo de un'
                               ' administrador o moderador, en su lugar,'
                               ' cambia tu apodo a través de la función'
                               ' de Discord.')

        else:
            if member is not None:
                await ctx.send('No tienes los permisos para cambiar '
                               'el apodo de alguien más.')

            else:
                last_nick = ctx.author.nick

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
