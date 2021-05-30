# import asyncio

import discord
from discord.ext import commands

from discord.member import Member

import datetime

import random

import json


with open('databases/db_str.json', encoding='utf8') as f:
    data = f.read()
    database = json.loads(data)


def get8Ball():
    return random.choice(database['ball8'])


def getPenis(number: int):
    if number > 1:
        return random.choice(database['penis'])
    elif number == 1:
        return random.choice(database['penis'])
    else:
        pass


def getLove(number: int):
    if number <= 45:
        return random.choice(database['love_low'])
    elif number >= 46 and number <= 75:
        return random.choice(database['love_medium'])
    else:
        return random.choice(database['love_high'])


def getLoveGif(number: int):
    with open('databases/db_gifs.json', encoding='utf-8') as f:
        gifData = f.read()
        gifDatabase = json.loads(gifData)
        if number >= 65:
            gif = random.choice(gifDatabase['love_high'])
            return gif
        else:
            gif = random.choice(gifDatabase['love_low'])
            return gif


color = discord.Color.blue()

time = datetime.datetime.utcnow()


class Commands(commands.Cog,
               name='Variedad',
               description='Comandos que no entran en otra categoría.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eightball(self, ctx, *, args):
        if args is not None:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name=f'**{get8Ball()}**',
                value=f'*"{args}"*'
            )
            embed.set_footer(
                text=ctx.author.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=embed)

        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(aliases=['probabilidad', 'prob'])
    async def probability(self, ctx, *, args):
        if args is not None:
            probabilidad = random.randint(0, 100)
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name='La probabilidad de...',
                value=f'"*{args}*"',
                inline=False
            )
            embed.add_field(
                name='Es de un...',
                value=f'**{probabilidad}%**',
                inline=False
            )
            embed.set_footer(
                text=ctx.author.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=embed)

        else:
            await ctx.send('Deberías preguntar algo.')

    @commands.command(name='penis', aliases=['pene', 'penisize', 'tula'])
    async def penis(self, ctx, member: Member = None):
        penisSize = random.randint(0, 10000)

        if member is not None:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name=f'El miembro reproductor de {member.name} mide:',
                value=f'**{penisSize}** {getPenis(penisSize)}.',
                inline=False
            )
            embed.set_footer(
                text=ctx.author.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name='Tu miembro reproductor mide:',
                value=f'**{penisSize}** {getPenis(penisSize)}.',
                inline=False
            )
            embed.set_footer(
                text=ctx.author.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=embed)

    @commands.command(aliases=['amor', 'loving'])
    async def love(self, ctx, member: Member = None):
        loveProbability = random.randint(0, 100)

        if member is not None:
            e = discord.Embed(
                    color=color,
                    timestamp=time
            )
            e.add_field(
                name=f'El amor entre {member.name} y tu es del...',
                value=f'**{loveProbability}%**, {getLove(loveProbability)}'
            )
            e.set_image(
                url=getLoveGif(loveProbability)
            ),
            e.set_footer(
                text=ctx.author.name,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        else:
            await ctx.send('Deberías mencionar a alguien.')


def setup(bot):
    bot.add_cog(Commands(bot))
