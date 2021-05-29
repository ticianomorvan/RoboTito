import asyncio

import discord
from discord.ext import commands

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
    index = random.randint(0, 9)
    a_header = string[table][index]['header']
    return a_header


def message(table):
    index = random.randint(0, 9)
    a_message = string[table][index]['message']
    return a_message


color = discord.Color.blue()

time = datetime.datetime.utcnow()


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
        msg = message('message_hug')

        if member is None:
            await ctx.send('Me gustaría que abraces a alguien.')

        else:
            if member == a:
                await ctx.send('Bueno, si puedes abrazarte a ti mismo,'
                               ' pero... preferiría que lo'
                               ' hagas con alguien más.')

            elif member == self.bot.user:
                await ctx.send('Nadie... nadie... me había querido'
                               ' abrazar nunca :(')

            elif member.bot is True:
                await ctx.send('No sé que tan sano sea abrazar a'
                               ' programas informáticos.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_hug'),
                    value=f'**{a.name}**{msg}**{member.name}**'
                )
                embed.set_image(url=gif('hug'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['beso'],
                      description='Besa a un usuario.')
    async def kiss(self, ctx, member: discord.Member = None):
        g = ctx.guild
        a = ctx.author
        msg = message('message_kiss')

        if member is None:
            await ctx.send('Menciona a quien quieras besar.')

        else:
            if member == a:
                await ctx.send('Deberías buscar a alguien más para besar.')

            elif member == self.bot.user:
                await ctx.send('Yo... yo... :flushed: ')

            elif member.bot is True:
                await ctx.send('Fuera de lo lógico, no creo que sea'
                               ' físicamente posible que beses a un software.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_kiss'),
                    value=f'**{a.name}**{msg}**{member.name}**'
                )
                embed.set_image(url=gif('kiss'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['acariciar'],
                      description='Acaricia a un usuario')
    async def pat(self, ctx, member: discord.Member = None):
        g = ctx.guild
        a = ctx.author
        msg = message('message_pat')

        if member is None:
            await ctx.send('Menciona a quien quieras abrazar.')

        else:
            if member == a:
                await ctx.send('Es lindo que tengas afecto propio, pero sería'
                               ' lindo que acaricies a alguien más.')

            elif member == self.bot.user:
                await ctx.send('No... no estaría mal un'
                               ' poco de cariño para mi...')

            elif member.bot is True:
                await ctx.send('Podrías... ¿acariciar'
                               ' la computadora?, no lo sé.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_pat'),
                    value=f'**{a.name}**{msg}**{member.name}**'
                )
                embed.set_image(url=gif('pat'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['golpear'],
                      description='Golpea a un usuario.')
    async def punch(self, ctx, member: discord.Member = None):
        g = ctx.guild
        a = ctx.author
        msg = message('message_punch')

        if member is None:
            await ctx.send('Menciona a quien quieras golpear...'
                           ' aunque no sea muy lindo.')

        else:
            if member == a:
                await ctx.send('No deberías golpearte, no es sano.')

            elif member == self.bot.user:
                await ctx.send('¿Qué te hice yo como para que me golpees?')

            elif member.bot is True:
                await ctx.send('Todos los programas tienen errores,'
                               ' no les tengas bronca.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_punch'),
                    value=f'**{a.name}**{msg}**{member.name}**'
                )
                embed.set_image(url=gif('punch'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['dormir'],
                      description='Dormir sol@ o con alguien.')
    async def sleep(self, ctx, member: discord.Member = None):
        a = ctx.author
        g = ctx.guild
        msg = message('message_sleep')
        msgw = message('message_sleepw')

        if member is None:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name=header('header_sleep'),
                value=f'**{a.name}**{msg}'
            )
            embed.set_image(url=gif('sleep'))
            embed.set_footer(text=g, icon_url=g.icon_url)

            await ctx.send(embed=embed)

        else:
            if member == a:
                await ctx.send('No hagas tus propios clones, en'
                               ' cualquier caso, acuéstate con alguien más.')

            elif member == self.bot.user:
                await ctx.send('No... no podemos... lo siento :(')

            elif member.bot is True:
                await ctx.send('Podrías acostarte con la computadora,'
                               ' aunque no creo que sea muy normal.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_sleepw'),
                    value=f'**{a.name}**{msgw}**{member.name}**'
                )
                embed.set_image(url=gif('sleepw'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['matar'],
                      description='Mata a un usuario.')
    async def kill(self, ctx, member: discord.Member = None):
        a = ctx.author
        g = ctx.guild
        msg = message('message_kill')

        if member is None:
            await ctx.send('Menciona a alguien, aunque ya estás en '
                           'la lista negra.')

        else:
            if member == a:
                await ctx.send('No deberías hacerlo, seguramente mucha '
                               'gente te quiere :<')

            elif member == self.bot.user:
                await ctx.send('¡Por favor! tengo hijos, espos... bueno,'
                               ' en realidad no tengo mucho...'
                               ' ¡pero no me mates!')

            elif member.bot is True:
                await ctx.send('Creo que hay mejores formas de apagar un bot.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_kill'),
                    value=f'**{a.name}**{msg}**{member.name}**'
                )
                embed.set_image(url=gif('kill'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['saludar', 'hi'],
                      description='Saluda a todos o a '
                                  'un usuario en específico.')
    async def greet(self, ctx, member: discord.Member = None):
        a = ctx.author
        g = ctx.guild
        msg = message('message_greet')
        msgs = message('message_greets')

        if member is None:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(
                name=header('header_greet'),
                value=f'**{a.name}**{msg}'
            )
            embed.set_image(url=gif('hi'))
            embed.set_footer(
                text=g,
                icon_url=g.icon_url
            )

            await ctx.send(embed=embed)

        else:
            if member == a:
                await ctx.send('Podrías estar padeciendo algún'
                               ' trastorno mental, o simplemente'
                               ' tener mucho (demasiado) amor propio.')

            elif member == self.bot.user:
                await ctx.send(f'Gracias, **{a.name}**, aprecio tu saludo :)')

            elif member.bot is True:
                await ctx.send(f'**{member.name}** no puede hablar contigo'
                               ' porque es un robot pero te dice gracias :D')

            elif member is not None:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(
                    name=header('header_greets'),
                    value=f'**{a.name}**{msgs}**{member.name}**'
                )
                embed.set_image(url=gif('hi'))
                embed.set_footer(
                    text=g,
                    icon_url=g.icon_url
                )

                await ctx.send(embed=embed)

    @commands.command(aliases=['bye', 'adios'],
                      description='Despide a un usuario o despídete.')
    async def goodbye(self, ctx, member: discord.Member = None):
        a = ctx.author
        g = ctx.guild

        if member is None:
            embed = discord.Embed(
                color=color,
                timestamp=time
            )
            embed.add_field(name='¡Sayonara!',
                            value=f'**{ctx.author.name}** se retira y '
                                  'saluda a todos',
                            inline=False)
            embed.set_image(url=gif('bye'))
            embed.set_footer(
                text=g,
                icon_url=g.icon_url
            )

            await ctx.send(embed=embed)

        else:
            if member == a:
                await ctx.send('No creo que tengas que auto-despedirte.')

            elif member == self.bot.user:
                await ctx.send(f'¡Adiós {a.name}')

            elif member.bot is True:
                await ctx.send(f'No creo que {member.name} te salude, digo,'
                               ' es un robot.')

            else:
                embed = discord.Embed(
                    color=color,
                    timestamp=time
                )
                embed.add_field(name='¡Adiós!',
                                value=f'**{ctx.author.name}** se despide de '
                                      f'**{member.name}**',
                                inline=False)
                embed.set_image(url=gif('bye'))
                embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)

                await ctx.send(embed=embed)

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
