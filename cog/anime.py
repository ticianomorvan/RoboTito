import asyncio

import discord
from discord.ext import commands

from discord.member import Member

import datetime

import random

import json


def gif(database):
    with open('databases/db_gifs.json') as f:
        data = f.read()
        gif = json.loads(data)
        return random.choice(gif[database])


def open_str():
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        string = json.loads(data)
        return string


string = open_str()


def header(table):
    header = string[table]
    return random.choice(header)


def sentence(author, msg, member=None):
    if member is None:
        message = random.choice(string[msg])
        result = author + message
        return result
    else:
        message = random.choice(string[msg])
        result = author + message + member
        return result


def sameUser(activity):
    message = 'Trata de ' + activity + ' alguien más.'
    return message


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
            await ctx.send(sameUser('abrazar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_hug'),
                value=sentence(a.name, 'm_hug', member.name),
            )
            e.set_image(
                url=gif('hug')
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
            await ctx.send(sameUser('besar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_kiss'),
                value=sentence(a.name, 'm_kiss', member.name),
            )
            e.set_image(
                url=gif('kiss')
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
            await ctx.send(sameUser('acariciar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_pat'),
                value=sentence(a.name, 'm_pat', member.name),
            )
            e.set_image(
                url=gif('pat')
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
            await ctx.send(sameUser('golpear a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_punch'),
                value=sentence(a.name, 'm_punch', member.name),
            )
            e.set_image(
                url=gif('punch')
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
                name=header('h_sleep'),
                value=sentence(a.name, 'm_sleep'),
            )
            e.set_image(
                url=gif('sleep')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(sameUser('acostarte con'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_sleepw'),
                value=sentence(a.name, 'm_sleepw', member.name),
            )
            e.set_image(
                url=gif('sleepw')
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
            await ctx.send(sameUser('matar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_kill'),
                value=sentence(a.name, 'm_kill', member.name),
            )
            e.set_image(
                url=gif('kill')
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
                name=header('h_greet'),
                value=sentence(a.name, 'm_greet'),
            )
            e.set_image(
                url=gif('hi')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(sameUser('saludar a'))

        else:
            e = discord.Embed(
                color=color,
                timestamp=time
            )
            e.add_field(
                name=header('h_greets'),
                value=sentence(a.name, 'm_greets', member.name),
            )
            e.set_image(
                url=gif('hi')
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
                name=header('h_goodbye'),
                value=sentence(a.name, 'm_goodbye', member.name),
            )
            e.set_image(
                url=gif('bye')
            )
            e.set_footer(
                text=ctx.guild,
                icon_url=ctx.guild.icon_url
            )

            await ctx.send(embed=e)

        elif member == a:
            await ctx.send(sameUser('despedir a'))

#        else:
#            e = discord.Embed(
#                color=color,
#                timestamp=time
#            )
#            e.add_field(
#                name=header('h_kill'),
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

    @commands.command(aliases=['llorar'],
                      description='Lloras o alguien te hace llorar.')
    async def cry(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=color,
                                  timestamp=time)
            embed.add_field(name='¡Mira lo que hiciste!',
                            value=f'**{member.name}** hizo llorar a '
                                  f'**{ctx.author.name}**',
                            inline=False)
            embed.set_image(url=gif('cry'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=color,
                                  timestamp=time)
            embed.add_field(name='¡Está llorando!',
                            value=f'**{ctx.author.name}** comenzó a llorar',
                            inline=False)
            embed.set_image(url=gif('cry'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

# This command uses local files to work. For organization purposes,
# i don't included them on the files that i push.
# Anyway, i'm gonna work on another database system.

    @commands.command(name='propose',
                      aliases=['proponer', 'casar', 'proposal'],
                      description='Te casas con un usuario.')
    async def marry_propose(self, ctx, member: discord.Member = None):
        choice = random.randint(0)
        file = discord.File(f'images/gifs/marry/{choice}.gif',
                            filename='image.gif')

        if member.bot is True:
            await ctx.send('No puedes casarte con un robot.')

        elif member is None:
            await ctx.send('No puedes casarte contigo mism@... creo.')

        else:
            await ctx.send(f'Le propusiste matrimonio a {member.name}, '
                           '¡tiene 25 segundos para responder!')

            def author(m):
                return m.author == ctx.message.author

            def couple(m):
                return m.author == member

            try:
                answer = await self.bot.wait_for('message',
                                                 check=couple,
                                                 timeout=25.0)
            except asyncio.TimeoutError:
                await ctx.send(f'{member.name} no respondió, '
                               'inténtalo después.')

            else:
                if answer.content == 'si':
                    await ctx.send('Por el poder que se me ha conferido...')
                    time.sleep(1.5)

                    embed = discord.Embed(
                        color=color,
                        timestamp=time
                    )
                    embed.add_field(
                        name='¡Los declaro esposos!',
                        value=f'{ctx.author.name} y '
                              f'{member.name} se casaron.',
                        inline=False
                    )
                    embed.set_image(url='attachment://image.gif')
                    embed.set_footer(
                        text=ctx.guild,
                        icon_url=ctx.guild.icon_url
                    )

                    await ctx.send(embed=embed, file=file)

                elif answer.content == 'no':
                    await ctx.send(f'No es el fin del mundo, {member} no es '
                                   'la única persona en el mundo.')

                else:
                    await ctx.send('No reconocí esa respuesta.')


def setup(bot):
    bot.add_cog(Anime(bot))
