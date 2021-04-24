# import discord
from discord.ext import commands

# import datetime

import json


class PingPong(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pingpo')
    async def pingpong(self, ctx):
        # guild = ctx.guild

        with open('databases/db_ping.json', 'r', encoding='utf8') as f:
            pong = json.load(f)
        try:
            with open('databases/db_ping.json', 'w', encoding='utf8') as w:
                pong['count'] = pong['count']+1
                json.dump(pong, w, ensure_ascii=False)

                await ctx.send(pong['count'])
        except pong['count'] not in pong:
            with open('databases/db_ping.json', 'w', encoding='utf8') as w:
                pong = {}
                pong['count'] = 0
                json.dump(
                    pong, w, ensure_ascii=False, sort_keys=True, indent=4)


def setup(bot):
    bot.add_cog(PingPong(bot))
