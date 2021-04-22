import discord
from discord.ext import commands

import random

import json

with open('databases/db_champs.json') as f:
    data = f.read()
    lol = json.loads(data)

with open('databases/db_leagueoflegends.json') as f2:
    data2 = f2.read()
    lol_ch = json.loads(data2)


class Lol(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pj')
    async def elec(self, ctx):
        guild = ctx.guild
        choice = random.choice(lol['pj'])
        embed = discord.Embed(
                color=discord.Color.blue(),
        )
        embed.add_field(
            name='Tu campeón es...',
            value=f'**{ctx.author.name}** te tocó {choice}',
            inline=False
        )
        embed.set_footer(
            text=guild,
            icon_url=guild.icon_url,
        )
        await ctx.send(embed=embed)

    @commands.command(name='adc')
    async def elecc(self, ctx):
        guild = ctx.guild
        choice = random.choice(lol['adc'])
        embed = discord.Embed(
                color=discord.Color.blue(),
        )
        embed.add_field(
            name='Tu adc es...',
            value=f'**{ctx.author.name}** te tocó {choice}',
            inline=False
        )
        embed.set_footer(
            text=guild,
            icon_url=guild.icon_url,
        )
        await ctx.send(embed=embed)

    @commands.command(name='pk2')
    async def pk(self, ctx):
        guild = ctx.guild
        champ = random.randint(1, 155)
        embed = discord.Embed(
            color=discord.Color.blue()
        )
        embed.add_field(
            name='El campeón que escogí para ti es:',
            value=lol_ch['champions'][champ]['name']
        )
        embed.set_thumbnail(
            url=lol_ch['champions'][champ]['icon']
        )
        embed.set_footer(
            text=guild,
            icon_url=guild.icon_url
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Lol(bot))
