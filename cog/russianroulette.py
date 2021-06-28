import asyncio
import discord
import random
import json
from discord.member import Member
from discord.ext import commands
from cog.functions.functions import Functions as f


with open('databases/db_russianroulette.json', encoding='utf-8') as fi:
    data = fi.read()
    rr = json.loads(data)


def rr_death(winner, loser):
    e = discord.Embed(color=f.rbColor())
    e.add_field(name=random.choice(rr['death']),
                value=f'{loser} murió, es una pena. {winner} ganó esta ronda.',
                inline=False)
    e.set_image(url=f.gif('russianroulette'))
    return e


def rr_safe():
    return random.choice(rr['safe'])


rrAnswers = ['si', 'probar', 'intentar', 'try']


class RussianRoulette(commands.Cog,
                      name='Ruleta rusa',
                      description='Solo uno saldrá con vida.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rr', 'ruletarusa'],
                      help='Juega a la ruleta rusa.')
    async def russianroulette(self, ctx, member: Member = None):
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
    bot.add_cog(RussianRoulette(bot))
