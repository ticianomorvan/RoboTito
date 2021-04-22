import discord
from discord.ext import commands

import random

import time

import json

import datetime


with open('databases/db_phrases.json') as d:
    rrd = d.read()
    rrdata = json.loads(rrd)
    rrdeath = random.choice(rrdata['rr_death'])
    rrsafe = random.choice(rrdata['rr_safe'])
    rrbdeath = random.choice(rrdata['rr.bot_death'])
    rrbsafe = random.choice(rrdata['rr.bot_safe'])


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ruletarusa', aliases=['rr'])
    async def ruletarusa(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        author = ctx.author.name
        gif = ('https://images.rapgenius.com/'
               '46bb57d90e7f3692014a769f2c3007cc.380x220x27.gif')

        if member is not None:
            await ctx.send(f'Desafiaste a {member.name} a jugar a la '
                           'Ruleta Rusa, ¿aceptará?')

            def msg_member(m):
                return m.author == member

            def msg_author(m):
                return m.author == ctx.author

            confirm = await self.bot.wait_for(
                'message', check=msg_member, timeout=60.0
            )
            if confirm.content == 'si':
                await ctx.send('¡Duelo iniciado!, '
                               f'{author} tu comienzas.')
                s = await self.bot.wait_for(
                    'message', check=msg_author, timeout=60.0
                )
                if s.content == 'probar':
                    death = random.randint(0, 3)
                    if death <= 2:
                        await ctx.send(str(rrsafe))
                        time.sleep(1)
                        await ctx.send(f'Tu sigues, {member.name}')
                        s = await self.bot.wait_for(
                            'message', check=msg_member, timeout=60.0
                        )
                        if s.content == 'probar':
                            death = random.randint(0, 2)
                            if death <= 1:
                                await ctx.send(str(rrsafe))
                                time.sleep(1)
                                await ctx.send(f'Tu sigues, {author}')
                                s = await self.bot.wait_for(
                                    'message', check=msg_author, timeout=60.0
                                )
                                if s.content == 'probar':
                                    death = random.randint(0, 1)
                                    if death == 0:
                                        await ctx.send(str(rrsafe))
                                        time.sleep(1)
                                        await ctx.send('Te toca, '
                                                       f'{member.name}')
                                        s = await self.bot.wait_for(
                                            'message', check=msg_member,
                                            timeout=60.0
                                        )
                                        if s.content == 'probar':
                                            embed = discord.Embed(
                                                color=discord.Color.blue(),
                                                timestamp=datetime.datetime.
                                                utcnow(),
                                            )
                                            embed.add_field(
                                                name=f'Moriste, {member.name}',
                                                value=str(rrdeath)
                                            )
                                            embed.set_image(
                                                url=gif
                                            )
                                            embed.set_footer(
                                                text=guild,
                                                icon_url=guild.icon_url,
                                            )
                                            await ctx.send(embed=embed)

                                    else:
                                        embed = discord.Embed(
                                            color=discord.Color.blue(),
                                            timestamp=datetime.datetime.
                                            utcnow(),
                                        )
                                        embed.add_field(
                                            name=f'Moriste, {author}',
                                            value=str(rrdeath)
                                        )
                                        embed.set_image(
                                            url=gif
                                        )
                                        embed.set_footer(
                                            text=guild,
                                            icon_url=guild.icon_url,
                                        )
                                        await ctx.send(embed=embed)

                                else:
                                    await ctx.send('Utiliza la palabra '
                                                   'correcta la próxima vez.')

                            else:
                                embed = discord.Embed(
                                    color=discord.Color.blue(),
                                    timestamp=datetime.datetime.utcnow(),
                                )
                                embed.add_field(
                                    name=f'Moriste, {member.name}',
                                    value=str(rrdeath)
                                )
                                embed.set_image(
                                    url=gif
                                )
                                embed.set_footer(
                                    text=guild,
                                    icon_url=guild.icon_url,
                                )
                                await ctx.send(embed=embed)
                        else:
                            await ctx.send('No, no creo que esa sea '
                                           'la palabra que buscas.')
                    else:
                        embed = discord.Embed(
                            color=discord.Color.blue(),
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.add_field(
                            name=f'Moriste, {ctx.author.name}',
                            value=str(rrdeath)
                        )
                        embed.set_image(
                            url=gif
                        )
                        embed.set_footer(
                            text=guild,
                            icon_url=guild.icon_url,
                        )
                        await ctx.send(embed=embed)
                else:
                    await ctx.send('Esa no es la palabra clave.')
            else:
                await ctx.send('¿No juegas?, que decepción.')
        else:
            await ctx.send('¡Jugaré contigo!, tienes el primer turno.')

            def check(m):
                return m.author == ctx.author

            s = await self.bot.wait_for(
                'message', check=check, timeout=60.0
            )
            if s.content == 'probar':
                death = random.randint(0, 3)
                if death <= 2:
                    await ctx.send(str(rrsafe))
                    time.sleep(0.5)
                    await ctx.send('Está bien, me toca.')
                    death = random.randint(0, 2)
                    if death <= 1:
                        time.sleep(1)
                        await ctx.send(str(rrbsafe))
                        s = await self.bot.wait_for(
                            'message', check=check, timeout=60.0
                        )
                        if s.content == 'probar':
                            death = random.randint(0, 1)
                            if death == 1:
                                await ctx.send(str(rrsafe))
                                time.sleep(1.5)
                                await ctx.send('Está bien, me toca.')
                                time.sleep(1.5)
                                embed = discord.Embed(
                                    color=discord.Color.blue(),
                                    timestamp=datetime.datetime.utcnow(),
                                )
                                embed.add_field(
                                    name='Morí.',
                                    value=str(rrbdeath),
                                    inline=False,
                                )
                                embed.set_image(
                                    url=gif
                                )
                                embed.set_footer(
                                    text=guild,
                                    icon_url=guild.icon_url,
                                )
                                await ctx.send(embed=embed)
                            else:
                                time.sleep(1.5)
                                embed = discord.Embed(
                                    color=discord.Color.blue(),
                                    timestamp=datetime.datetime.utcnow(),
                                )
                                embed.add_field(
                                    name=f'Moriste, {author}',
                                    value=str(rrdeath),
                                    inline=False,
                                )
                                embed.set_image(
                                    url=gif
                                )
                                embed.set_footer(
                                    text=guild,
                                    icon_url=guild.icon_url,
                                )
                                await ctx.send(embed=embed)
                        else:
                            await ctx.send('Deberías "probar" para jugar.')
                    else:
                        time.sleep(1.5)
                        embed = discord.Embed(
                            color=discord.Color.blue(),
                            timestamp=datetime.datetime.utcnow(),
                        )
                        embed.add_field(
                            name='Morí',
                            value=str(rrbdeath),
                            inline=False,
                        )
                        embed.set_image(
                            url=gif
                        )
                        embed.set_footer(
                            text=guild,
                            icon_url=guild.icon_url,
                        )
                        await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.add_field(
                        name=f'Moriste, {author}',
                        value=str(rrdeath),
                        inline=False
                    )
                    embed.set_image(
                        url=gif
                    )
                    embed.set_footer(
                        text=guild,
                        icon_url=guild.icon_url,
                    )
                    await ctx.send(embed=embed)
            else:
                await ctx.send('Si quieres jugar, escribe "probar".')


def setup(bot):
    bot.add_cog(Fun(bot))
