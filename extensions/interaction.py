from nextcord.ext import commands
import random
import json
import nextcord as n
import helpers

with open('databases/db_gifs.json', mode='r', encoding='utf-8') as a:
    data = a.read()
    gifs = json.loads(data)

answer = ['Yes', 'No', 'maybye']

class Choice(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(
        aliases=['prob', 'choice']
    )
    async def probability(self, ctx: commands.Context, args):
        if args == 'probabilidad':
            value = random.randint(0, 100)
            await ctx.send(
                f'The probability is: {value}%'
            )
        else:
            result = random.choice(answer)
            await ctx.send(
                f'I say {result}'
            )

    @commands.command()
    async def hug(self, ctx: commands.Context, member: n.Member):
        e = helpers.HugEmbed(ctx.author.name, member.name, ctx.guild.name,
                             ctx.guild.icon.url)
        await ctx.send(embed=e)


def setup(bot: commands.Bot):
    bot.add_cog(Choice(bot))
