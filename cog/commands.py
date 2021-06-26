import discord
import random
from cog.functions.functions import Functions as f
from discord.ext import commands
from discord.member import Member


class Commands(commands.Cog,
               name='Variedad',
               description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['latency', 'latencia'],
                      help='Obtén el tiempo de respuesta del bot.')
    async def ping(self, ctx):
        latency = round(self.bot.latency)
        ms = latency / 100
        e = discord.Embed(color=f.rbColor())
        e.add_field(name='La latencia es de:', value=f'{ms} ms.')
        await ctx.send(embed=e)

    @commands.command(name='8ball', help='Pregúntale algo a la bola ocho.')
    async def eightball(self, ctx, *, args):
        if args is not None:
            e = discord.Embed(color=f.rbColor())
            e.add_field(name=f'**{f.get8Ball()}**', value=f'*"{args}"*')
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(aliases=['probabilidad', 'prob'],
                      help='¿Cuál es la probabilidad de...?')
    async def probability(self, ctx, *, args):
        if args is not None:
            probabilidad = random.randint(0, 100)
            e = discord.Embed(color=f.rbColor())
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
        penisSize = random.randint(0, 10000)

        if member is not None:
            e = discord.Embed(color=f.rbColor())
            e.add_field(
                name=f'El miembro reproductor de {member.name} mide:',
                value=f'**{penisSize}** {f.getPenis(penisSize)}.',
                inline=False)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=f.rbColor())
            e.add_field(
                name='Tu miembro reproductor mide:',
                value=f'**{penisSize}** {f.getPenis(penisSize)}.',
                inline=False)
            await ctx.send(embed=e)

    @commands.command(aliases=['amor', 'loving'],
                      help='¿Qué tan fuerte es el amor '
                           'entre tu y esa persona?')
    async def love(self, ctx, member: Member = None):
        loveProbability = random.randint(0, 100)

        if member is not None:
            e = discord.Embed(color=f.rbColor())
            e.add_field(name=f'El amor entre {member.name} y tu es del...',
                        value=f'**{loveProbability}%**,'
                              f' {f.getLove(loveProbability)}')
            e.set_image(url=f.getLoveGif(loveProbability))
            await ctx.send(embed=e)
        else:
            await ctx.send('Deberías mencionar a alguien.')


def setup(bot):
    bot.add_cog(Commands(bot))
