import discord
from discord.ext import commands

import random

import time

import datetime


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ruletarusa', aliases=['rr'])
    async def ruletarusa(self, ctx, member: discord.Member = None):
        guild = ctx.guild

        if member is not None:
            await ctx.send(f'Desafiaste a {member.mention} a jugar a la '
                           'Ruleta Rusa, ¿aceptará?')

            def check_1(m):
                return m.author == member

            def check_2(m):
                return m.author == ctx.author

            confirm = await self.bot.wait_for(
                'message', check=check_1, timeout=60.0
            )
            if confirm.content == 'si':
                await ctx.send('¡Duelo iniciado!, '
                               f'{ctx.author.name} tu comienzas.')
                s1 = await self.bot.wait_for(
                    'message', check=check_2, timeout=60.0
                )
                if s1.content == 'probar':
                    death = random.randint(0, 3)
                    if death <= 2:
                        await ctx.send('Te salvaste, le toca a '
                                       f'{member.mention}')
                        s2 = await self.bot.wait_for(
                            'message', check=check_1, timeout=60.0
                        )
                        if s2.content == 'probar':
                            death_2 = random.randint(0, 2)
                            if death_2 <= 1:
                                await ctx.send(
                                    f'Por poco, {member.mention}. Te toca,'
                                    f' {ctx.author.mention}'
                                )
                                s3 = await self.bot.wait_for(
                                    'message', check=check_2, timeout=60.0
                                )
                                if s3.content == 'probar':
                                    death_3 = random.randint(0, 1)
                                    if death_3 == 0:
                                        await ctx.send(
                                            'La gracia divina te salva,'
                                            f' turno de {member.mention}'
                                        )
                                        s4 = await self.bot.wait_for(
                                            'message', check=check_1,
                                            timeout=60.0
                                        )
                                        if s4.content == 'probar':
                                            embed = discord.Embed(
                                                color=discord.Color.blue(),
                                                timestamp=datetime.datetime.
                                                utcnow(),
                                            )
                                            embed.add_field(
                                                name='MORISTE',
                                                value=f'{member.mention}'
                                            )
                                            embed.set_image(
                                                url='https://images.rapgenius.'
                                                'com/46bb57d90e7f3692014a769f2'
                                                'c3007cc.380x220x27.gif'
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
                                            name='MORISTE',
                                            value=f'{ctx.author.mention}'
                                        )
                                        embed.set_image(
                                            url='https://images.rapgenius.com/'
                                                '46bb57d90e7f3692014a769f2c300'
                                                '7cc.380x220x27.gif'
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
                                    name='MORISTE',
                                    value=f'{member.mention}'
                                )
                                embed.set_image(
                                    url='https://images.rapgenius.com/46bb57d'
                                        '90e7f3692014a769f2c3007cc.380x220x27'
                                        '.gif'
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
                            name='MORISTE',
                            value=f'{ctx.author.mention}'
                        )
                        embed.set_image(
                            url='https://images.rapgenius.com/46bb57d90e7f369'
                                '2014a769f2c3007cc.380x220x27.gif'
                        )
                        embed.set_footer(
                            text=guild,
                            icon_url=guild.icon_url,
                        )
                        await ctx.send(embed=embed)
        else:
            await ctx.send('¡Jugaré contigo!, tienes el primer turno.')

            def check(m):
                return m.author == ctx.author

            sh1 = await self.bot.wait_for(
                'message', check=check, timeout=60.0
            )
            if sh1.content == 'probar':
                death = random.randint(0, 3)
                if death <= 2:
                    await ctx.send('Te salvaste, me toca.')
                    death = random.randint(0, 2)
                    if death <= 1:
                        time.sleep(0.5)
                        await ctx.send('No es mi hora aún, tu turno.')
                        sh1 = await self.bot.wait_for(
                            'message', check=check, timeout=60.0
                        )
                        if sh1.content == 'probar':
                            death = random.randint(0, 1)
                            if death == 1:
                                await ctx.send('Una vez más, tienes suerte')
                                await ctx.send('Está bien, me toca.')
                                time.sleep(0.5)
                                await ctx.send('**MORÍ**, necesito '
                                               'reparaciones :pensive:')
                            else:
                                await ctx.send('**MORISTE**, '
                                               '¡los robots ganan!')
                        else:
                            await ctx.send('Deberías "probar" para jugar.')
                    else:
                        time.sleep(0.5)
                        await ctx.send('**MORÍ**, mis circuitos están '
                                       'muy dañados, alguien que me ayude :(')
                else:
                    await ctx.send('**MORISTE**, no merecías vivir :D')
            else:
                await ctx.send('Si quieres jugar, escribe "probar".')


def setup(bot):
    bot.add_cog(Fun(bot))
