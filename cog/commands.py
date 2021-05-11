import discord
from discord.ext import commands

# import time

import datetime

import random

import json


def get_8ball():
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        ball8 = json.loads(data)
        return random.choice(ball8['ball8'])


def get_penis():
    with open('databases/db_commands.json', encoding='utf-8') as f:
        data = f.read()
        penis = json.loads(data)
        choice = random.choice(penis['penis_command'])
        return choice


class Commands(commands.Cog,
               name='Variedad',
               description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                      description='¿Qué te responderá la bola ocho?')
    async def eightball(self, ctx, *, args):

        if args is not None:
            embed = discord.Embed(colour=discord.Colour.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='A tu pregunta de...',
                            value=f'*"{args}"*',
                            inline=False)
            embed.add_field(name='La respuesta es:',
                            value=get_8ball(),
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
            probabilidad = random.randint(0, 100)
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

    @commands.command(name='penis',
                      aliases=['pene', 'penisize', 'tula'],
                      description='Conoce el tamaño de tu miembro.')
    async def penis(self, ctx, member: discord.Member = None):
        penis = get_penis()
        g = ctx.guild

        if member is not None:
            if penis == 'images/pikapenis.png':
                file = discord.File('images/pikapenis.png',
                                    filename='image.png')

                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.add_field(name='¡VOS NO TENÉS ESO AHÍ, ASQUEROS@!',
                                value='No tengo registro de una '
                                      'pija tan grande',
                                inline=False)
                embed.set_image(url='attachment://image.png')
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed, file=file)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f'Este es el miembro de {member.name}:',
                                value=penis,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)

        else:
            if penis == 'images/pikapenis.png':
                file = discord.File('images/pikapenis.png',
                                    filename='image.png')

                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.add_field(name='¡VOS NO TENÉS ESO AHÍ, ASQUEROS@!',
                                value='No tengo registro de una '
                                      'pija tan grande',
                                inline=False)
                embed.set_image(url='attachment://image.png')
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed, file=file)

            else:
                embed = discord.Embed(color=discord.Color.blue(),
                                      timestamp=datetime.datetime.utcnow())
                embed.add_field(name='Este es tu miembro:',
                                value=penis,
                                inline=False)
                embed.set_footer(text=g, icon_url=g.icon_url)

                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Commands(bot))
