import discord
from discord.ext import commands

from discord.member import Member

import datetime

import cog.functions.functions as functions

function = functions.Functions

color = discord.Color.blue()

time = datetime.datetime.utcnow()

noUser = 'Menciona a alguien más.'


class Anime(commands.Cog,
            name='Interacción',
            description='Comandos para interactuar usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'])
    async def hug(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            await ctx.send(noUser)

        elif member == a:
            await ctx.send(function.sameUser('abrazar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_hug'),
                value=function.sentence(a.name, 'm_hug', member.name),
            )
            e.set_image(
                url=function.gif('hug')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['beso'])
    async def kiss(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            await ctx.send(noUser)

        elif member == a:
            await ctx.send(function.sameUser('besar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_kiss'),
                value=function.sentence(a.name, 'm_kiss', member.name),
            )
            e.set_image(
                url=function.gif('kiss')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['acariciar'])
    async def pat(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            await ctx.send(noUser)

        elif member == a:
            await ctx.send(function.sameUser('acariciar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_pat'),
                value=function.sentence(a.name, 'm_pat', member.name),
            )
            e.set_image(
                url=function.gif('pat')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['golpear'])
    async def punch(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            await ctx.send(noUser)

        elif member == a:
            await ctx.send(function.sameUser('golpear a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_punch'),
                value=function.sentence(a.name, 'm_punch', member.name),
            )
            e.set_image(
                url=function.gif('punch')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['dormir'])
    async def sleep(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_sleep'),
                value=function.sentence(a.name, 'm_sleep'),
            )
            e.set_image(
                url=function.gif('sleep')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(function.function.sameUser('acostarte con'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_sleepw'),
                value=function.sentence(a.name, 'm_sleepw', member.name),
            )
            e.set_image(
                url=function.gif('sleepw')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['matar'])
    async def kill(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            await ctx.send(noUser)

        elif member == a:
            await ctx.send(function.sameUser('matar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_kill'),
                value=function.sentence(a.name, 'm_kill', member.name),
            )
            e.set_image(
                url=function.gif('kill')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['saludar', 'hi'])
    async def greet(self, ctx, member: Member = None):
        a = ctx.author

        if member is None:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_greet'),
                value=function.sentence(a.name, 'm_greet'),
            )
            e.set_image(
                url=function.gif('hi')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(function.sameUser('saludar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_greets'),
                value=function.sentence(a.name, 'm_greets', member.name),
            )
            e.set_image(
                url=function.gif('hi')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['bye', 'adios'],
                      description='Despide a un usuario o despídete.')
    async def goodbye(self, ctx, member: discord.Member = None):
        a = ctx.author

        if member is None:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=function.header('h_goodbye'),
                value=function.sentence(a.name, 'm_goodbye', member.name),
            )
            e.set_image(
                url=function.gif('bye')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(function.sameUser('despedir a'))

#        else:
#            e = discord.Embed(
#                color=color,
#                timestamp=time
#            )
#            e.add_field(
#                name=function.header('h_kill'),
#                value=sentence(a.name, 'm_kill', member.name),
#            )
#            e.set_image(
#                url=gif('kill')
#            )
#            e.set_footer(
#                text=ctx.guild,
#                icon_url=ctx.guild.icon_url
#            )
#
#            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Anime(bot))
