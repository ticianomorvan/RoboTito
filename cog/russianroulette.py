import asyncio
import discord
import random
import json
from discord.member import Member
from discord.ext import commands
from cog.functions.functions import Functions as function


with open('databases/db_russianroulette.json', encoding='utf-8') as f:
    data = f.read()
    rr = json.loads(data)


def rrDeath(winner, loser):
    e = discord.Embed(
        color=discord.Color.from_rgb(function.randomColor())
    )
    e.add_field(
        name=random.choice(rr['death']),
        value=f'{loser} murió, es una pena. {winner} ganó esta ronda.',
        inline=False
    )
    e.set_image(
        url=function.gif('russianroulette')
    )
    return e


def rrSafe():
    return random.choice(rr['safe'])


rrAnswers = ['Si', 'probar', 'Probar', 'intentar', 'Intentar']


class RussianRoulette(commands.Cog,
                      name='Ruleta rusa',
                      description='Solo uno saldrá con vida.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rr', 'ruletarusa'],
                      help='Juega a la ruleta rusa.')
    async def russianRoulette(self, ctx, member: Member = None):
        if member is not None:
            await ctx.send('¡Qué empiece el juego!, tu empiezas.')

            def member1(m):
                return m.author == ctx.author

            def member2(m):
                return m.author == member

            minusBullet = 6

            while True:
                try:
                    await ctx.send('Siguiente turno.')
                    minusBullet -= 1
                    bullet = random.randint(0, minusBullet)

                    m1msg = await self.bot.wait_for(
                        'message', check=member1, timeout=60.0
                    )

                except asyncio.TimeoutError:
                    await ctx.send('Se acabó el tiempo, no respondiste.')
                    break

                else:
                    if m1msg.content in rrAnswers and bullet == 0:
                        e = rrDeath(member.name, ctx.author.name)
                        await ctx.send(embed=e)
                        break
                    else:
                        await ctx.send(rrSafe())

                        try:
                            m2msg = await self.bot.wait_for(
                                'message', check=member2, timeout=60.0
                            )

                        except asyncio.TimeoutError:
                            await ctx.send('Se acabó el tiempo,'
                                           f' {member.name} no respondió.')
                            break

                        else:
                            if m2msg.content in rrAnswers and bullet == 0:
                                e = rrDeath(ctx.author.name, member.name)
                                await ctx.send(embed=e)
                                break
                            else:
                                await ctx.send(rrSafe())
                                continue


def setup(bot):
    bot.add_cog(RussianRoulette(bot))
