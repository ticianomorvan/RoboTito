import asyncio

import discord
from discord.ext import commands

import datetime

import time

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


def header(table, index_id: int):
    index = random.randint(0, index_id)
    a_header = string[table][index]['header']
    return a_header


def message(table, index_id: int):
    index = random.randint(0, index_id)
    a_message = string[table][index]['message']
    return a_message


class Anime(commands.Cog,
            name='Interacción',
            description='Comandos para interactuar usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'],
                      description='Abraza a un usuario.')
    async def hug(self, ctx, member: discord.Member = None):
        g = ctx.guild
        a = ctx.author
        msg = message('message_hug', 9)

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name=header('header_hug', 9),
                            value=f'{a.name}{msg}{member.name}')
            embed.set_image(url=gif('hug'))
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send(f'Oye, {ctx.author.mention}, yo te abrazaría '
                           '¿sabes?, pero soy un robot.')

    @commands.command(aliases=['beso'],
                      description='Besa a un usuario.')
    async def kiss(self, ctx, member: discord.Member = None):
        g = ctx.guild
        a = ctx.author
        msg = message('message_kiss', 9)

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name=header('header_kiss', 9),
                            value=f'{a.name}{msg}{member.name}',
                            inline=False)
            embed.set_image(url=gif('kiss'))
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('No creo que puedas besarte a ti mism@, '
                           'a menos que...')

    @commands.command(aliases=['acariciar'],
                      description='Acaricia a un usuario')
    async def pat(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Caricias para todos!',
                            value=f'**{ctx.author.name}** acaricia a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=gif('pat'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('Creo que el amor propio es una parte importante '
                           'que tener en cuenta.')

    @commands.command(aliases=['golpear'],
                      description='Golpea a un usuario.')
    async def punch(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Golpe rabioso!',
                            value=f'**{member.name}** recibe una fuerte'
                                  f' paliza de **{ctx.author.name}**',
                            inline=False)
            embed.set_image(url=gif('punch'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('No es demasiado sano que te golpees a ti mismo.')

    @commands.command(aliases=['dormir'],
                      description='Dormir sol@ o con alguien.')
    async def sleep(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Los tórtolos se acurrucan...',
                            value=f'**{ctx.author.name}** y '
                                  f'**{member.name}** se acuestan juntos...',
                            inline=False)
            embed.set_image(url=gif('sleep'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Alguien está con sueño...',
                            value=f'**{ctx.author.name}** se va a dormir.',
                            inline=False)
            embed.set_image(url=gif('sleepw'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

    @commands.command(aliases=['matar'],
                      description='Mata a un usuario.')
    async def kill(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Hubo un asesinato en el servidor!',
                            value=f'**{ctx.author.name}** asesina a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=gif('kill'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            await ctx.send('La vida puede ser buena, como para que te mates.')

    @commands.command(aliases=['saludar', 'hi'],
                      description='Saluda a todos o a '
                                  'un usuario en específico.')
    async def greet(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Buenas!',
                            value=f'**{ctx.author.name}** saluda a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=gif('hi'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Buenas a todos!',
                            value=f'**{ctx.author.name}** saluda a todo mundo',
                            inline=False)
            embed.set_image(url=gif('hi'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

    @commands.command(aliases=['bye', 'adios'],
                      description='Despide a un usuario o despídete.')
    async def goodbye(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Adiós!',
                            value=f'**{ctx.author.name}** se despide de '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=gif('bye'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Sayonara!',
                            value=f'**{ctx.author.name}** se retira y '
                                  'saluda a todos',
                            inline=False)
            embed.set_image(url=gif('bye'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

    @commands.command(aliases=['llorar'],
                      description='Lloras o alguien te hace llorar.')
    async def cry(self, ctx, member: discord.Member = None):

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Mira lo que hiciste!',
                            value=f'**{member.name}** hizo llorar a '
                                  f'**{ctx.author.name}**',
                            inline=False)
            embed.set_image(url=gif('cry'))
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
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
        choice = random.randint(0, 9)
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

                    embed = discord.Embed(color=discord.Color.blue(),
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name='¡Los declaro esposos!',
                                    value=f'{ctx.author.name} y '
                                          f'{member.name} se casaron.',
                                    inline=False)
                    embed.set_image(url='attachment://image.gif')
                    embed.set_footer(text=ctx.guild,
                                     icon_url=ctx.guild.icon_url)

                    await ctx.send(embed=embed, file=file)

                elif answer.content == 'no':
                    await ctx.send(f'No es el fin del mundo, {member} no es '
                                   'la única persona en el mundo.')

                else:
                    await ctx.send('No reconocí esa respuesta.')


def setup(bot):
    bot.add_cog(Anime(bot))
