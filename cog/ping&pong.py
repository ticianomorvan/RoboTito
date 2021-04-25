import discord
from discord.ext import commands

import datetime

import json

import random


class PingPong(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def pingpong(self, ctx):
        guild = ctx.guild

        with open('databases/db_ping.json', 'r', encoding='utf8') as f:
            pong = json.load(f)

        with open('databases/db_gifs.json', 'r') as f:
            data = f.read()
            gif = json.loads(data)
            random_gif = random.choice(gif['pingpong'])

        try:
            with open('databases/db_ping.json', 'w', encoding='utf8') as w:
                if ctx.author.name != pong['cuser']:
                    pong['count'] = pong['count']+1
                    pong['user'] = pong['user']
                    pong['cuser'] = ctx.author.name
                    json.dump(pong, w, ensure_ascii=False)
                    count = pong['count']
                    user = pong['user']
                    cuser = pong['cuser']

                    embed = discord.Embed(
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.add_field(
                        name='¡Rebote!',
                        value=f'Hasta ahora, han habido {count} rebotes y '
                              f'el último en devolver la pelota fue {user}',
                        inline=False
                    )
                    embed.add_field(
                        name='¡Qué no sea el último!',
                        value=f'{cuser} es quien devolvió la pelota esta vez.'
                    )
                    embed.set_image(
                        url=random_gif,
                    )
                    embed.set_footer(
                        text=guild,
                        icon_url=guild.icon_url,
                    )
                    await ctx.send(embed=embed)

                elif ctx.author.name == pong['cuser']:
                    pong['count'] = pong['count']+1
                    pong['user'] = ctx.author.name
                    pong['cuser'] = pong['cuser']
                    json.dump(pong, w, ensure_ascii=False)
                    count = pong['count']
                    user = pong['user']
                    cuser = pong['cuser']

                    embed = discord.Embed(
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.add_field(
                        name='¡Rebote!',
                        value=f'Hasta ahora, han habido {count} rebotes y '
                              f'el último en devolver la pelota fue {user}',
                        inline=False
                    )
                    embed.add_field(
                        name='¡Qué no sea el último!',
                        value=f'{cuser} es quien devolvió la pelota esta vez.'
                    )
                    embed.set_image(
                        url=random_gif,
                    )
                    embed.set_footer(
                        text=guild,
                        icon_url=guild.icon_url,
                    )
                    await ctx.send(embed=embed)

                elif ctx.author.name != pong['user']:
                    pong['count'] = pong['count']+1
                    pong['user'] = pong['user']
                    pong['cuser'] = ctx.author.name
                    json.dump(pong, w, ensure_ascii=False)
                    count = pong['count']
                    user = pong['user']
                    cuser = pong['cuser']
                    await ctx.send(f'3 {count}, {user}, {cuser}')

                    embed = discord.Embed(
                        color=discord.Color.blue(),
                        timestamp=datetime.datetime.utcnow(),
                    )
                    embed.add_field(
                        name='¡Rebote!',
                        value=f'Hasta ahora, han habido {count} rebotes y '
                              f'el último en devolver la pelota fue {user}',
                        inline=False
                    )
                    embed.add_field(
                        name='¡Qué no sea el último!',
                        value=f'{cuser} es quien devolvió la pelota esta vez.'
                    )
                    embed.set_image(
                        url=random_gif,
                    )
                    embed.set_footer(
                        text=guild,
                        icon_url=guild.icon_url,
                    )
                    await ctx.send(embed=embed)

        except pong is None:
            return


def setup(bot):
    bot.add_cog(PingPong(bot))
