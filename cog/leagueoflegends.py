import discord
import random
import json
from cog.functions import rbColor
from discord.ext import commands


with open('databases/db_lolchamps.json', encoding='utf-8') as db:
    data = db.read()
    champs = json.loads(data)


def get_role(role: str):
    final_role = str.lower(role)
    list = []
    for champ in champs:
        if champs[champ]['roles'][final_role] is True:
            list.append(champ)
        else:
            pass

    choice = random.choice(list)
    return choice


def get_name(name: str):
    for champ in champs:
        if name == champs[champ]['name']:
            return champ
        else:
            pass


def get_random():
    index = len(champs)
    choice = random.randint(1, index)
    return choice


def create_embed(champ):
    index = str(champ)
    e = discord.Embed(color=rbColor())
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
        champ = get_name(name)
        if champ is not None:
            e = create_embed(champ)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.add_field(name='Hubo un error',
                        value='No pude reconocer a ese campeón, por'
                              ' favor, vuelve a intentarlo respetando'
                              ' mayúsculas y símbolos. Los nombres exactos'
                              ' que utlizo se encuentran en https://las.op.gg/'
                              'champion/statistics')
            await ctx.send(embed=e)

    @commands.command(aliases=['rol', 'role', 'chrole'],
                      help='Encuentra un campeón por su rol.')
    async def championrole(self, ctx, role: str):
        if role in ['top', 'jg', 'mid', 'adc', 'support']:
            champ = get_role(role)
            e = create_embed(champ)
            await ctx.send(embed=e)
        else:
            e = discord.Embed(color=rbColor())
            e.add_field(name='No reconocí ese rol.',
                        value=f'{role} no es un rol válido. Vuelve a'
                              ' intentarlo usando: **top**, **jg**,'
                              ' **mid**, **adc** o **support**.')
            await ctx.send(embed=e)

    @commands.command(aliases=['chrandom', 'caleatorio', 'chrand'],
                      help='Obtén un campeón aleatorio.')
    async def championrandom(self, ctx):
        champ = get_random()
        e = create_embed(champ)
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))
