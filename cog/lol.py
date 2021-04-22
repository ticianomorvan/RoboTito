import discord
from discord.ext import commands

import random

import json

with open('databases/db_champs.json') as f:
    data = f.read()
    lol = json.loads(data)


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


def setup(bot):
    bot.add_cog(Lol(bot))
