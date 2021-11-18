# Nextcord
from nextcord.embeds import Embed
from nextcord.ext import commands
from nextcord import Color

# Libraries
from random import choice, randint

# Database
from json import loads

with open('databases/db_lolchamps.json', encoding='utf-8') as db:
    data = db.read()
    champs = loads(data)

def rbColor():
    """Returns one of the main colors of RoboTito."""
    colors = [Color.from_rgb(255, 94, 43),
              Color.from_rgb(82, 92, 253),
              Color.from_rgb(72, 159, 181),
              Color.from_rgb(255, 134, 0)]
    return choice(colors)

def gets_name(name: str):
    for champ in champs:
        if name == champs[champ]['name']:
            return champ
        else:
            pass

def gets_role(role: str):
    final_role = str.lower(role)
    list = []
    for champ in champs:
        if champs[champ]['roles'][final_role] is True:
            list.append(champ)
    else:
        pass
    return choice(list)
    
def get_random(champs):
    index = len(champs)
    choice = randint(1, index)
    champion = champs[choice]
    return champion

def embeds(champ: str):
    index = champ
    e = Embed(
        color=rbColor()
    )
    e.set_author(
        name='League of Legends champions',
        url=champs[index]['lolpage'],
        icon_url='assets/lol_icon.png'
    )
    e.add_field(
        name=f"{champ[index]['name']}, {champ[index]['header']}",
        value=champ[index]['description'],
        inline=False
    )
    e.add_field(
        name='Items, runes and builds:',
        value=f"[OP.GG]({champs[index]['op.gg']})",
        inline=False
    )
    e.set_image(
        url=champs[index]['icon']
    )
    return e

# Commands
class Leagueoflegends(commands.Cog):
    def __init__(self, champ):
        self.champ: commands.Bot = champ

    @commands.command(
        aliases=['chname', 'champion']
        )
    async def championname(
        self, ctx: commands.Context, name: str):
        """Commands related to lol champs"""
        user = ctx.author
        champ = gets_name(name)
        if champ is not None:
            embeds(champ)
            await ctx.send(embed=embeds)
        else:
            e = Embed(
                color=user.color
            )
            e.add_field(
                name='There was a mistake',
                value="I couldn't recognize that champion,"
                      " please try again respecting capital"
                      " letters and symbols. The exact names"
                      " i use can be found at: https://las.op.gg/"
                      "champion/statistics"
            )
            await ctx.send(embed=e)


def setup(bot: commands.Bot):
    bot.add_cog(Leagueoflegends(bot))
