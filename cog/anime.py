import discord
from discord.ext import commands

import datetime

import random

import json

with open('databases/db_gifs.json') as f:
    data = f.read()
    gif = json.loads(data)


class Anime(commands.Cog,
            name='Interacción',
            description='Comandos para interactuar usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'],
                      description='Abraza a un usuario.')
    async def hug(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['hug'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Abrazo!',
                            value=f'**{ctx.author.name}** abraza a '
                                  f'**{member.name}**')
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            await ctx.send(f'Oye, {ctx.author.mention}, yo te abrazaría '
                           '¿sabes?, pero soy un robot.')

    @commands.command(aliases=['beso'],
                      description='Besa a un usuario.')
    async def kiss(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['kiss'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡El amor nace!',
                            value=f'**{ctx.author.name}** besa a '
                                  f'**{member.name}** con mucho amor.',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            await ctx.send('No creo que puedas besarte a ti mism@, '
                           'a menos que...')

    @commands.command(aliases=['acariciar'],
                      description='Acaricia a un usuario')
    async def pat(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['pat'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Caricias para todos!',
                            value=f'**{ctx.author.name}** acaricia a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            await ctx.send('Creo que el amor propio es una parte importante '
                           'que tener en cuenta.')

    @commands.command(aliases=['golpear'],
                      description='Golpea a un usuario.')
    async def punch(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['punch'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Golpe rabioso!',
                            value=f'**{member.name}** recibe una fuerte'
                                  f' paliza de **{ctx.author.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            await ctx.send('No es demasiado sano que te golpees a ti mismo.')

    @commands.command(aliases=['dormir'],
                      description='Dormir sol@ o con alguien.')
    async def sleep(self, ctx, member: discord.Member = None):

        if member is not None:
            choice = random.choice(gif['sleep'])

            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Los tórtolos se acurrucan...',
                            value=f'**{ctx.author.name}** y '
                                  f'**{member.name}** se acuestan juntos...',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            choice = random.choice(gif['sleepw'])

            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='Alguien está con sueño...',
                            value=f'**{ctx.author.name}** se va a dormir.',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['matar'],
                      description='Mata a un usuario.')
    async def kill(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['kill'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Hubo un asesinato en el servidor!',
                            value=f'**{ctx.author.name}** asesina a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            await ctx.send('La vida puede ser buena, como para que te mates.')

    @commands.command(aliases=['saludar', 'hi'],
                      description='Saluda a todos o a '
                                  'un usuario en específico.')
    async def greet(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['hi'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Buenas!',
                            value=f'**{ctx.author.name}** saluda a '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Buenas a todos!',
                            value=f'**{ctx.author.name}** saluda a todo mundo',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['bye', 'adios'],
                      description='Despide a un usuario o despídete.')
    async def goodbye(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['bye'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Adiós!',
                            value=f'**{ctx.author.name}** se despide de '
                                  f'**{member.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Sayonara!',
                            value=f'**{ctx.author.name}** se retira y '
                                  'saluda a todos',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['llorar'],
                      description='Lloras o alguien te hace llorar.')
    async def cry(self, ctx, member: discord.Member = None):
        choice = random.choice(gif['cry'])

        if member is not None:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Mira lo que hiciste!',
                            value=f'**{member.name}** hizo llorar a '
                                  f'**{ctx.author.name}**',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(color=discord.Color.blue(),
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name='¡Está llorando!',
                            value=f'**{ctx.author.name}** se comenzó a llorar',
                            inline=False)
            embed.set_image(url=choice)
            embed.set_footer(text=ctx.guild, icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Anime(bot))
