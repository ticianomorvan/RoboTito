import discord
import random
import json
import cog.functions as f
from discord.ext import commands


with open('databases/db_lolchamps.json', encoding='utf-8') as db:
    data = db.read()
    champs = json.loads(data)


def Role(role):
    while True:
        roleIndex = random.randint(1, 85)
        roleChamp = str(roleIndex)
        if champs[roleChamp]['roles'][role] is True:
            return roleChamp
        else:
            continue


def Name(name):
    while True:
        nameIndex = random.randint(1, 85)
        nameChamp = str(nameIndex)
        if name == champs[nameChamp]['name']:
            return nameChamp
        else:
            continue


def Random():
    randomIndex = random.randint(1, 85)
    randomChamp = str(randomIndex)
    return randomChamp


def Embed(index: str):
    e = discord.Embed(color=f.rbColor())
    e.set_author(name='Campeón de League of Legends',
                 url=champs[index]['lolpage'],
                 icon_url='https://img1.wikia.nocookie.net/'
                          '__cb20150402234343/leagueoflegends/images/1/12/'
                          'League_of_Legends_Icon.png')
    e.add_field(name=f"{champs[index]['name']}, {champs[index]['header']}",
                value=champs[index]['description'],
                inline=False)
    e.add_field(name='Objetos, runas y builds:',
                value=f"[OP.GG]({champs[index]['op.gg']})",
                inline=False)
    e.set_image(url=champs[index]['icon'])
    return e


class LeagueOfLegends(commands.Cog,
                      description='Comandos variados sobre '
                                  'League of Legends.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['chname', 'champion', 'campeón'],
                      help='Encuentra un campeón por su nombre.')
    async def championname(self, ctx, *, name: str):
        champ = Name(name)
        e = Embed(champ)
        await ctx.send(embed=e)

    @commands.command(aliases=['rol', 'role', 'chrole'],
                      help='Encuentra un campeón por su rol.')
    async def championrole(self, ctx, role: str = None):
        if role is not None:
            champ = Role(role)
            e = Embed(champ)
            await ctx.send(embed=e)

        else:
            await ctx.send('Debes introducir un rol, con las siguientes'
                           ' posibilidades: `top, jg, mid, adc, support`')

    @commands.command(aliases=['chrandom', 'caleatorio', 'chrand'],
                      help='Obtén un campeón aleatorio.')
    async def championrandom(self, ctx):
        champ = Random()
        e = Embed(champ)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))
