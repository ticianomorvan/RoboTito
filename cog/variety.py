import json
import asyncio
from discord import Embed
from cog.helpers import rbColor, strings, gifs
from cog.interaction import Helpers
from discord.ext import commands
from discord.member import Member
from random import choice, randint


class VarietyHelp():
    def get_8ball():
        return choice(strings['ball8'])

    def get_penis(number: int):
        return choice(strings['penis'])

    def get_love(number: int):
        if number >= 75:
            return choice(strings['love_high'])
        elif number >= 45:
            return choice(strings['love_medium'])
        else:
            return choice(strings['love_low'])

    def get_love_gif(number: int):
        if number >= 75:
            gif = choice(gifs['love_high'])
        else:
            gif = choice(gifs['love_low'])

        return gif


with open('databases/db_russianroulette.json', encoding='utf-8') as rr_file:
    data = rr_file.read()
    rr = json.loads(data)


class RussianRoulette():
    def rr_death(winner, loser):
        e = Embed(color=rbColor())
        e.add_field(name=choice(rr['death']),
                    value=f'{loser} murió, es una pena.'
                          f' {winner} ganó esta ronda.',
                    inline=False)
        e.set_image(url=Helpers.gif('russianroulette'))
        return e

    def rr_safe():
        return choice(rr['safe'])


class Variety(commands.Cog,
              name='Variedad',
              description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latency', 'latencia'],
                      help='Obtén el tiempo de respuesta del bot.')
    async def ping(self, ctx):
        latency = str(self.bot.latency)
        e = Embed(color=rbColor())
        e.add_field(name='La latencia es de:', value=f'{latency[:4]} ms.')
        await ctx.send(embed=e)

    @commands.command(name='8ball', help='Pregúntale algo a la bola ocho.')
    async def eightball(self, ctx, *, args):
        if args is not None:
            e = Embed(color=rbColor())
            e.add_field(name=f'**{VarietyHelp.get_8ball()}**',
                        value=f'*"{args}"*')
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(aliases=['probabilidad', 'prob'],
                      help='¿Cuál es la probabilidad de...?')
    async def probability(self, ctx, *, args):
        if args is not None:
            probability = randint(0, 100)
            e = Embed(color=rbColor())
            e.add_field(name='La probabilidad de...', value=f'"*{args}*"',
                        inline=False)
            e.add_field(name='Es de un...', value=f'**{probability}%**',
                        inline=False)
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(name='penis', aliases=['pene', 'penisize', 'tula'],
                      help='¿Cuánto mide tu aparato?')
    async def penis(self, ctx, member: Member = None):
        penis_size = randint(0, 100)
        e = Embed(color=rbColor())

        if member is not None:
            e.add_field(name=f'El miembro reproductor de {member.name} mide:',
                        value=f'**{penis_size}**'
                              f' {VarietyHelp.get_penis(penis_size)}.',
                        inline=False)
        else:
            e = Embed(color=rbColor())
            e.add_field(name='Tu miembro reproductor mide:',
                        value=f'**{penis_size}**'
                              f' {VarietyHelp.get_penis(penis_size)}.',
                        inline=False)

        await ctx.send(embed=e)

    @commands.command(aliases=['gaymeter', 'gayperc', 'gaylevel'],
                      help='Conoce tu porcentaje de homosexualidad.')
    async def gay(self, ctx, member: Member = None):
        gay_percentage = randint(0, 100)
        e = Embed(color=rbColor())

        if member is not None:
            e.add_field(name='Según mis cálculos...',
                        value=f'{member.name} es un **{gay_percentage}%**'
                              ' homosexual :rainbow_flag:')
        else:
            e = Embed(color=rbColor())
            e.add_field(name='Según mis cálculos...',
                        value=f'Sos un **{gay_percentage}%**'
                              ' homosexual :rainbow_flag:')

        await ctx.send(embed=e)

    @commands.command(aliases=['amor', 'loving'],
                      help='¿Qué tan fuerte es el amor '
                           'entre tu y esa persona?')
    async def love(self, ctx, member: Member = None):
        love_probability = randint(0, 100)

        if member is not None:
            e = Embed(color=rbColor())
            e.add_field(name=f'El amor entre {member.name} y tú es del...',
                        value=f'**{love_probability}%**,'
                              f' {VarietyHelp.get_love(love_probability)}')
            e.set_image(url=VarietyHelp.get_love_gif(love_probability))
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías mencionar a alguien.')

    @commands.command(aliases=['rr', 'ruletarusa'],
                      help='Juega a la ruleta rusa.')
    async def russianroulette(self, ctx, member: Member = None):
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
                    bullet = randint(0, minusBullet)

                    m1msg = await self.bot.wait_for(
                        'message', check=member1, timeout=60.0
                    )
                    m1msgStr = str.lower(m1msg.content)

                except asyncio.TimeoutError:
                    await ctx.send('Se acabó el tiempo, no respondiste.')
                    break

                else:
                    if m1msgStr in rrAnswers and bullet == 0:
                        e = RussianRoulette.rr_death(
                            member.name, ctx.author.name)
                        await ctx.send(embed=e)
                        break
                    else:
                        minusBullet -= 1
                        await ctx.send(RussianRoulette.rr_safe())
                        await asyncio.sleep(1)
                        await ctx.send(f'Te toca, {member.name}.')

                        try:
                            bullet = randint(0, minusBullet)

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
                                e = RussianRoulette.rr_death(
                                    ctx.author.name, member.name)
                                await ctx.send(embed=e)
                                break
                            else:
                                minusBullet -= 1
                                await ctx.send(RussianRoulette.rr_safe())
                                await asyncio.sleep(1)
                                await ctx.send(f'Te toca, {ctx.author.name}.')
                                continue

        else:
            await ctx.send('Jugaría contigo, pero si perdiera,'
                           ' ¿quién haría mi trabajo?')


def setup(bot):
    bot.add_cog(Variety(bot))
