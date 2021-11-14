# Nextcord
from nextcord.embeds import Embed
from nextcord.ext import commands

# Libraries
from random import choice, randint

# Database
from json import loads

with open('databases/db_lolchamps.json', encoding='utf-8') as db:
    data = db.read()
    champs = loads(data)


# Functions
# def gets_name(name: str):
#    for champ in champs:
#        if name == champs[champ]['name']:
#            return champ
#        else:
#            pass
#
#
# def gets_random():

def embeds(ctx: commands.Context, champ):
    index = str(champ)
    user = ctx.author
    e = Embed(
        color=user.color
    )
    e.set_author(
        name='League of Legends champions',
        url=champs[index]['lolpage'],
        icon_url='assets/lol_icon.png'
    )
    e.add_field(
        name=f"{champs[index]['name']}, {champs[index]['header']}",
        value=champs[index]['description'],
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

    def get_name(self):
        return self.champ['name']

    def gets_role(role: str):
        final_role = str.lower(role)
        list = []
        for champ in champs:
            if champs[champ]['roles'][final_role] is True:
                list.append(champ)
        else:
            pass
        return choice(list)

    def get_random(self, champs):
        index = len(champs)
        choice = randint(1, index)
        champion = champs[choice]
        return champion

    def get_lolpage(self):
        return self.champ['lolpage']

    def get_description(self):
        return self.champ['description']
    
    def get_header(self):
        return self.champ['header']

    def embeds(self, champ, ctx: commands.Context):
        index = champ()
        user = ctx.author
        e = Embed(
            color=user.color
        )
        e.set_author(
            name='League of Legends champions',
            url=champs[index]['lolpage'],
            icon_url='assets/lol_icon.png'
        )
        e.add_field(
            name=f"{self.champ['name']}, {self.champ['header']}",
            value=self.champ['description']
        )

#
#    @commands.command(
#        aliases=['chname', 'champion']
#        )
#    async def championname(self, ctx: commands.Context, *, name: str):
#        """Commands related to lol champs"""
#        user = ctx.author
#        champ = gets_name(name)
#        if champ is not None:
#            embeds()
#            await ctx.send(embed=embeds)
#        else:
#            e = Embed(
#                color=user.color
#            )
#            e.add_field(
#                name='There was a mistake',
#                value="I couldn't recognize that champion,"
#                      " please try again respecting capital"
#                      " letters and symbols. The exact names"
#                      " i use can be found at https://las.op.gg/"
#                      "champion/statistics"
#            )
#            await ctx.send(embed=e)


def setup(bot: commands.Bot):
    bot.add_cog(Leagueoflegends(bot))
