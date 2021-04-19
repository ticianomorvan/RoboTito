import discord
from discord.ext import commands

import datetime

import random
# from random import randint


class Anime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def abrazo(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        with open('databases/hug_db.txt') as f:
            line = f.readlines()
            choice = random.choice(line)

        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Abrazo!',
                value=f'{ctx.author.name} abraza a {member.name}',
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send(
                f'Oye, {ctx.author.mention}, yo te abrazaría ¿sabes?, '
                'pero soy un robot.'
            )

    @commands.command(name='kiss')
    async def beso(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        with open('databases/kiss_db.txt') as f:
            line = f.readlines()
            choice = random.choice(line)

        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡El amor nace!',
                value=f'{ctx.author.name} besa a'
                      f' {member.name} con mucho amor.',
                inline=False
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send(
                'No creo que puedas besarte a ti mism@, a menos que...'
            )

    @commands.command(name='pat')
    async def caricia(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        with open('databases/pat_db.txt') as f:
            line = f.readlines()
            choice = random.choice(line)

        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Caricias para todos!',
                value=f'{ctx.author.name} acaricia a {member.name}',
                inline=False
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send(
                'Creo que el amor propio es una parte '
                'importante que tener en cuenta.'
            )

    @commands.command(name='punch')
    async def golpear(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        with open('databases/punch_db.txt') as f:
            line = f.readlines()
            choice = random.choice(line)

        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Golpe rabioso!',
                value=f'{member.name} recibe una fuerte'
                      f' paliza de {ctx.author.name}',
                inline=False
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send(
                'No es demasiado sano que te golpees a ti mismo.'
            )

    @commands.command(name='sleep')
    async def dormir(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        if member is not None:
            with open('databases/sleepw_db.txt') as f:
                line = f.readlines()
                choice = random.choice(line)

            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Los tórtolos se acurrucan...',
                value=f'{ctx.author.name} y '
                      f'{member.name} se acuestan juntos...',
                inline=False,
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            with open('databases/sleep_db.txt') as f:
                line = f.readlines()
                choice = random.choice(line)

            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Alguien está con sueño...',
                value=f'{ctx.author.name} se va a dormir.',
                inline=False,
            )
            embed.set_image(
                url=choice
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Anime(bot))
