import discord
import json
import random
import asyncio
from cog.functions import (rbColor, gif, get_8ball,
                           get_love_gif, get_love, get_penis)
from cog.information import Member as m
from discord.ext import commands
from discord.member import Member


class Variety(commands.Cog,
              name='Variedad',
              description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latency', 'latencia'],
                      help='Obtén el tiempo de respuesta del bot.')
    async def ping(self, ctx):
        latency = round(self.bot.latency)
        ms = latency / 100
        e = discord.Embed(color=rbColor())
        e.add_field(name='La latencia es de:', value=f'{ms} ms.')
        await ctx.send(embed=e)

    @commands.command(name='8ball', help='Pregúntale algo a la bola ocho.')
    async def eightball(self, ctx, *, args):
        if args is not None:
            e = discord.Embed(color=rbColor())
            e.add_field(name=f'**{get_8ball()}**', value=f'*"{args}"*')
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(aliases=['probabilidad', 'prob'],
                      help='¿Cuál es la probabilidad de...?')
    async def probability(self, ctx, *, args):
        if args is not None:
            probabilidad = random.randint(0, 100)
            e = discord.Embed(color=rbColor())
            e.add_field(name='La probabilidad de...', value=f'"*{args}*"',
                        inline=False)
            e.add_field(name='Es de un...', value=f'**{probabilidad}%**',
                        inline=False)
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(name='penis', aliases=['pene', 'penisize', 'tula'],
                      help='¿Cuánto mide tu aparato?')
    async def penis(self, ctx, member: Member = None):
        penisSize = random.randint(0, 100)

        if member is not None:
            e = discord.Embed(color=rbColor())
            e.add_field(
                name=f'El miembro reproductor de {member.name} mide:',
                value=f'**{penisSize}** {get_penis(penisSize)}.',
                inline=False)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.add_field(
                name='Tu miembro reproductor mide:',
                value=f'**{penisSize}** {get_penis(penisSize)}.',
                inline=False)
            await ctx.send(embed=e)

    @commands.command(aliases=['gaymeter', 'gayperc', 'gaylevel'],
                      help='Conoce tu porcentaje de homosexualidad.')
    async def gay(self, ctx, member: Member = None):
        gay_percentage = random.randint(0, 100)
        if member is not None:
            e = discord.Embed(color=rbColor())
            e.add_field(name='Según mis cálculos...',
                        value=f'{member.name} es un **{gay_percentage}%**'
                              ' homosexual :rainbow_flag:')
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.add_field(name='Según mis cálculos...',
                        value=f'Sos un **{gay_percentage}%**'
                              ' homosexual :rainbow_flag:')
            await ctx.send(embed=e)

    @commands.command(aliases=['amor', 'loving'],
                      help='¿Qué tan fuerte es el amor '
                           'entre tu y esa persona?')
    async def love(self, ctx, member: Member = None):
        loveProbability = random.randint(0, 100)

        if member is not None:
            e = discord.Embed(color=rbColor())
            e.add_field(name=f'El amor entre {member.name} y tú es del...',
                        value=f'**{loveProbability}%**,'
                              f' {get_love(loveProbability)}')
            e.set_image(url=get_love_gif(loveProbability))
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías mencionar a alguien.')

    @commands.command(aliases=['ruser', 'ualeatorio'],
                      help='Obtén información de un usuario aleatorio.')
    async def randomuser(self, ctx):
        member = random.choice(ctx.guild.members)
        e = m.embed(member)
        await ctx.send(embed=e)

    @commands.command(aliases=['rr', 'ruletarusa'],
                      help='Juega a la ruleta rusa.')
    async def russianroulette(self, ctx, member: Member = None):

        with open('databases/db_russianroulette.json', encoding='utf-8') as fi:
            data = fi.read()
            rr = json.loads(data)

        def rr_death(winner, loser):
            e = discord.Embed(color=rbColor())
            e.add_field(name=random.choice(rr['death']),
                        value=f'{loser} murió, es una pena.'
                              f' {winner} ganó esta ronda.',
                        inline=False)
            e.set_image(url=gif('russianroulette'))
            return e

        def rr_safe():
            return random.choice(rr['safe'])

        rrAnswers = ['si', 'probar', 'intentar', 'try']

        if member is not None:
            await ctx.send('¡Qué empiece el juego!, tu empiezas.')

            def member1(m):
                return m.author == ctx.author

            def member2(m):
                return m.author == member

            minusBullet = 6

            while True:
                try:
                    bullet = random.randint(0, minusBullet)

                    m1msg = await self.bot.wait_for(
                        'message', check=member1, timeout=60.0
                    )
                    m1msgStr = str.lower(m1msg.content)

                except asyncio.TimeoutError:
                    await ctx.send('Se acabó el tiempo, no respondiste.')
                    break

                else:
                    if m1msgStr in rrAnswers and bullet == 0:
                        e = rr_death(member.name, ctx.author.name)
                        await ctx.send(embed=e)
                        break
                    else:
                        minusBullet -= 1
                        await ctx.send(rr_safe())
                        await asyncio.sleep(1)
                        await ctx.send(f'Te toca, {member.name}.')

                        try:
                            bullet = random.randint(0, minusBullet)

                            m2msg = await self.bot.wait_for(
                                'message', check=member2, timeout=60.0
                            )
                            m2msgStr = str.lower(m2msg.content)

                        except asyncio.TimeoutError:
                            await ctx.send('Se acabó el tiempo,'
                                           f' {member.name} no respondió.')
                            break

                        else:
                            if m2msgStr in rrAnswers and bullet == 0:
                                e = rr_death(ctx.author.name, member.name)
                                await ctx.send(embed=e)
                                break
                            else:
                                minusBullet -= 1
                                await ctx.send(rr_safe())
                                await asyncio.sleep(1)
                                await ctx.send(f'Te toca, {ctx.author.name}.')
                                continue

        else:
            await ctx.send('Jugaría contigo, pero si perdiera,'
                           ' ¿quién haría mi trabajo?')


def setup(bot):
    bot.add_cog(Variety(bot))
