import discord
from discord.ext import commands

# import time

import datetime

import random
from random import randint

import json


class Commands(commands.Cog,
               name='Variedad',
               description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      description='¿Qué te responderá la bola ocho?')
    async def eightball(self, ctx, *, args):

        with open('databases/db_8ball.json', encoding='utf8') as f:
            data = f.read()
            eball = json.loads(data)
            eightball = eball['eightball_responses']
            eightball_answer = random.choice(eightball)

        if args is not None:
            embed = discord.Embed(colour=discord.Colour.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='A tu pregunta de...',
                            value=f'*"{args}"*',
                            inline=False)
            embed.add_field(name='La respuesta es:',
                            value=eightball_answer,
                            inline=False)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(aliases=['probabilidad', 'prob'],
                      description='Comprueba la probabilidad de '
                                  'que algo suceda.')
    async def probability(self, ctx, *, args):

        if args is not None:
            probabilidad = randint(0, 100)
            embed = discord.Embed(colour=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='La probabilidad de...',
                            value=f'*"{args}"*',
                            inline=False)
            embed.add_field(name='Es de un:',
                            value=f'**{probabilidad}%**',
                            inline=False)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('Debes introducir una pregunta.')


def setup(bot):
    bot.add_cog(Commands(bot))
