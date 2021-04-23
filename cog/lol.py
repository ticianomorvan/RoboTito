import discord
from discord.ext import commands

import datetime

import random

import json

with open('databases/db_leagueoflegends.json') as f2:
    data2 = f2.read()
    lol_ch = json.loads(data2)


class Lol(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='champpick', aliases=['chpick', 'champick'])
    async def championpick(self, ctx, *, args):
        guild = ctx.guild
        select = random.randint(1, 155)
        champ_name = lol_ch['champions'][select]['name']
        champ_header = lol_ch['champions'][select]['header']
        champ_square = lol_ch['champions'][select]['icon']
        champ_ugg = lol_ch['champions'][select]['u.gg']
        champ_page = lol_ch['champions'][select]['lol']

        if args == 'jg':
            jungler_id = random.randint(1, 155)
            for role in lol_ch['champions']:
                jungler = lol_ch['champions'][jungler_id]['role']
                if str(jungler) == 'jg':
                    await ctx.send(lol_ch['champions'][jungler_id]['name'])
                else:
                    await ctx.send('no')

        elif args == 'random':
            embed = discord.Embed(
                title=champ_name,
                description=champ_header,
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.set_thumbnail(
                url=champ_square
            )
            embed.add_field(
                name='Builds, hechizos y estadísticas:',
                value=f'[Sitio oficial de u.gg]({champ_ugg})',
                inline=False
            )
            embed.add_field(
                name='Más información sobre el campeón:',
                value='[Página oficial de League Of Legends]'
                      f'({champ_page})',
                inline=False,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Lol(bot))
