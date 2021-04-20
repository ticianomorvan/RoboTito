import discord
from discord.ext import commands

import datetime

import random

import json

with open('databases/db_gifs.json') as f:
    data = f.read()
    gif = json.loads(data)


class Anime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def abrazo(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        choice = random.choice(gif['hug'])

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
        choice = random.choice(gif['kiss'])

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
        choice = random.choice(gif['pat'])

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
        choice = random.choice(gif['punch'])

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
            choice = random.choice(gif['sleep'])

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
            choice = random.choice(gif['sleepw'])

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

    @commands.command(name='kill')
    async def matar(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        choice = random.choice(gif['kill'])

        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Hubo un asesinato en el servidor!',
                value=f'{ctx.author.name} asesina a {member.name}',
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
                'Tocar a la mamá de tito nunca fue una opción '          
            )


def setup(bot):
    bot.add_cog(Anime(bot))
