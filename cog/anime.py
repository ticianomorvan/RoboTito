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
        hug_dict = [
            'https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/'
            'tenor.gif',
            'https://media1.tenor.com/images/78d3f21a608a4ff0c8a09ec12ffe763d/'
            'tenor.gif',
            'https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/'
            'tenor.gif',
            'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/'
            'tenor.gif',
            'https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/'
            'tenor.gif',
            'https://media1.tenor.com/images/bb9c0c56769afa3b58b9efe5c7bcaafb/'
            'tenor.gif',
            'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/'
            'tenor.gif',
            'https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/'
            'tenor.gif',
            'https://media1.tenor.com/images/5ccc34d0e6f1dccba5b1c13f8539db77/'
            'tenor.gif',
            'https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/'
            'tenor.gif',
            'https://media1.tenor.com/images/4db088cfc73a5ee19968fda53be6b446/'
            'tenor.gif',
            'https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/'
            'tenor.gif',
            'https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/'
            'tenor.gif',
            'https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/'
            'tenor.gif',
            'https://media1.tenor.com/images/c7efda563983124a76d319813155bd8e/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Abrazo!',
                value=f'{ctx.author} abraza a {member.nick}',
            )
            hug_gif = random.choice(hug_dict)
            embed.set_image(
                url=hug_gif,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f'Oye, {ctx.author}, yo te abrazaría ¿sabes?, '
                'pero soy un robot.'
            )


def setup(bot):
    bot.add_cog(Anime(bot))
