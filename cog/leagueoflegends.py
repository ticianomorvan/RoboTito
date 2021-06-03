import discord
import random
import json
from discord.ext import commands


with open('databases/db_lolchamps.json', encoding='utf-8') as f:
    data = f.read()
    champs = json.loads(data)


def champRole(role):
    while True:
        index = random.randint(1, 14)
        champ = str(index)
        if champs[champ]['roles'][role] is True:
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
        else:
            continue


def champRandom():
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


def champName(name: str):
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


class LeagueOfLegends(commands.Cog,
                      description='Comandos variados sobre '
                                  'League of Legends.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rol', 'posición', 'carril', 'position'],
                      help='Elige un campeón aleatorio según su rol.')
    async def roleChamp(self, ctx, role: str):
        e = champRole(role)
        await ctx.send(embed=e)

    @commands.command(aliases=['randomchamp', 'champrandom', 'randchamp'],
                      help='Obtén un campeón aleatorio.')
    async def randomChamp(self, ctx):
        e = champRandom()
        await ctx.send(embed=e)

    @commands.command(aliases=['champname', 'champ', 'champion', 'campeón'],
                      help='Elige un campeón por su nombre.')
    async def nameChamp(self, ctx, name: str):
        e = champName(name)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))
