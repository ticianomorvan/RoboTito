import discord
from discord.ext import commands

import time

import datetime

import random
from random import randint

import json


class Comandos(
    commands.Cog,
    name='Variedad',
    description='Comandos que no entran en otra categoría.'
):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='8ball',
        description='¿Qué te responderá la bola ocho?'
    )
    async def eightball(self, ctx, *, args):

        with open('databases/db_8ball.json', encoding='utf8') as f:
            data = f.read()
            eball = json.loads(data)
            eightball = eball['eightball_responses']
            eightball_answer = random.choice(eightball)

        if args is not None:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='A tu pregunta de...',
                value=f'*"{args}"*',
                inline=False,
            )
            embed.add_field(
                name='La respuesta es:',
                value=eightball_answer,
                inline=False,
            )
            embed.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url,
            )
            await ctx.send(embed=embed)

    @commands.command(description='¡Llama a un usuario!')
    async def call(self, ctx, member=None):
        phone_numbers = [
            '0348-5154678',
            '2544-415-2547',
            '+14 15126784',
            '+97 15222747',
            '+11 55224978',
            '+34 51779522',
            '+21 47789521',
            '+378 55154449',
            '+4 411881264',
        ]
        pn_selected = random.choice(phone_numbers)
        if member is not None:
            message = await ctx.send('Conectando')
            time.sleep(0.5)
            await message.edit(content='Conectando.')
            time.sleep(0.5)
            await message.edit(content='Conectando..')
            time.sleep(0.5)
            await message.edit(content='Conectando...')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}.')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}..')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}...')
            time.sleep(0.5)
            await message.edit(content='*"Su"*')
            time.sleep(0.25)
            await message.edit(content='*"Su llamada al"*')
            time.sleep(0.25)
            await message.edit(content=f'*"Su llamada al {pn_selected}"*')
            time.sleep(0.25)
            await message.edit(content=f'*"Su llamada al {pn_selected} '
                                       'no recibió respuesta."*')
            time.sleep(1)
            await message.edit(content=f'{member} no contestó la llamada.')
        else:
            await ctx.send('¿A quién quieres llamar?')

    @commands.command(
        aliases=['probabilidad', 'prob'],
        description='Comprueba la probabilidad de que algo suceda.'
    )
    async def probability(self, ctx, *, args):

        if args is not None:
            probabilidad = randint(0, 100)
            embed = discord.Embed(
                colour=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='La probabilidad de...',
                value=f'*"{args}"*',
                inline=False,
            )
            embed.add_field(
                name='Es de un:',
                value=f'**{probabilidad}%**',
                inline=False,
            )
            embed.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send('Debes introducir una pregunta.')


def setup(bot):
    bot.add_cog(Comandos(bot))
