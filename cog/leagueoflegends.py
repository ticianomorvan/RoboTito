import discord
import random
import json
from discord.ext import commands


with open('databases/db_lolchamps.json', encoding='utf-8') as f:
    data = f.read()
    champs = json.loads(data)


def champ(name=None, role=None):
    if role is not None:
        while True:
            index = random.randint(1, 14)
            champ = str(index)
            if champs[champ]['roles'][role] is True:
                e = discord.Embed(
                    color=discord.Color.blue(),
                )
                e.add_field(
                    name=f"{champs[champ]['name']},"
                         f" {champs[champ]['header']}.",
                    value=champs[champ]['description'],
                    inline=False
                )
                e.add_field(
                    name='Runas, objetos y builds:',
                    value=f"[OP.GG]({champs[champ]['op.gg']})",
                    inline=False
                )
                e.add_field(
                    name='Lore e información sobre el campeón.',
                    value=f"[League of Legends]({champs[champ]['lolpage']})",
                    inline=False
                )
                e.set_image(
                    url=champs[champ]['icon']
                )
                return e
            else:
                continue
    elif name is not None:
        while True:
            champIndex = random.randint(1, 14)
            champ = str(champIndex)
            if name == champs[champ]['name']:
                e = discord.Embed(
                    color=discord.Color.blue(),
                )
                e.add_field(
                    name=f"{champs[champ]['name']},"
                         f" {champs[champ]['header']}.",
                    value=champs[champ]['description'],
                    inline=False
                )
                e.add_field(
                    name='Runas, objetos y builds:',
                    value=f"[OP.GG]({champs[champ]['op.gg']})",
                    inline=False
                )
                e.add_field(
                    name='Lore e información sobre el campeón.',
                    value=f"[League of Legends]({champs[champ]['lolpage']})",
                    inline=False
                )
                e.set_image(
                    url=champs[champ]['icon']
                )
                return e
                break
            else:
                continue
    else:
        index = random.randint(1, 14)
        champ = str(index)
        e = discord.Embed(
            color=discord.Color.blue(),
        )
        e.add_field(
            name=f"{champs[champ]['name']}, {champs[champ]['header']}.",
            value=champs[champ]['description'],
            inline=False
        )
        e.add_field(
            name='Runas, objetos y builds:',
            value=f"[OP.GG]({champs[champ]['op.gg']})",
            inline=False
        )
        e.add_field(
            name='Lore e información sobre el campeón.',
            value=f"[League of Legends]({champs[champ]['lolpage']})",
            inline=False
        )
        e.set_image(
            url=champs[champ]['icon']
        )
        return e


class LeagueOfLegends(commands.Cog,
                      description='Comandos variados sobre '
                                  'League of Legends.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def champion(self, ctx, name=None):
        if name is not None:
            e = champ(name)
            await ctx.send(embed=e)
        else:
            await ctx.send('Introduce un nombre.')

    @commands.command()
    async def role(self, ctx, role=None, name=None):
        if role is not None:
            e = champ(name, role)
            await ctx.send(embed=e)
        else:
            await ctx.send('Introduce un rol.')

    @commands.command()
    async def random(self, ctx, role=None, name=None):
        e = champ(name, role)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))
