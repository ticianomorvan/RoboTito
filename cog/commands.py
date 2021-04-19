import discord
from discord.ext import commands

import time

import datetime

import random
from random import randint


class Comandos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.counter = 0

# Ping & Pong
    @commands.command()
    async def ping(self, ctx):
        self.counter += 1
        if self.counter >= 0:
            embed = discord.Embed(title='Pong!',
                                  colour=discord.Colour.blue())
            embed.add_field(name='¡Devuelve el rebote!',
                            value='Cantidad de rebotes '
                            f'hasta ahora: **{self.counter}**',
                            inline=True)
            embed.set_footer(text='RoboTito')
            await ctx.send(embed=embed)
        elif self.counter >= 100:
            embed = discord.Embed(title='Pong furioso!',
                                  colour=discord.Colour.blue())
            embed.add_field(name='¡Rebote relámpago!',
                            value='El partido se complica, la pelota rebotó '
                            f'hasta ahora: **{self.counter}** veces.',
                            inline=True)
            embed.set_footer(text='RoboTito')
            await ctx.send(embed=embed)

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Eso fue inesperado, tu ganas.')

# Clean & Fastclean
    @commands.command(aliases=['c'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clean(self, ctx, amount=100):
        message = await ctx.send('Preparando limpieza.')
        time.sleep(0.35)
        await message.edit(content='Preparando limpieza..')
        time.sleep(0.35)
        await message.edit(content='Preparando limpieza...')
        time.sleep(0.35)
        await message.edit(content='Ultimando detalles.')
        time.sleep(0.35)
        await message.edit(content='Ultimando detalles..')
        time.sleep(0.35)
        await message.edit(content='Ultimando detalles...')
        time.sleep(0.55)
        await ctx.channel.purge(limit=amount, bulk=True)
        time.sleep(1.15)
        embed = discord.Embed(color=discord.Color.blue(),
                              timestamp=datetime.datetime.utcnow())
        embed.add_field(name='¡Limpieza a la orden!',
                        value=f'Borré {amount} mensajes '
                              f'en el canal de {ctx.channel.name}')
        embed.set_image(url='https://media1.tenor.com/images/'
                            '980fefd36ce46e30bb11e8861fa20633/tenor.gif')
        embed.set_footer(text='Limpieza de RoboTito')
        await ctx.send(embed=embed)

    @commands.command(aliases=['fc'])
    @commands.has_guild_permissions(manage_messages=True)
    async def fastclean(self, ctx, amount=100):
        await ctx.channel.purge(limit=amount, bulk=True)
        await ctx.send(f'Se borraron {amount} mensajes.')

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, args):
        guild = ctx.guild
        answers = ('Si.',
                   'Quizá, quien sabe.',
                   'Definitivamente.',
                   'Definitivamente **no**.',
                   'Absolutamente.',
                   'En el mejor de los casos, si.',
                   'Esperemos que no.',
                   'Recenle a quien sea para que eso no pase.',
                   'No.',
                   'Bajo ningún término.',
                   'De ninguna manera.',
                   'Probablemente, no.',
                   'Hay muchas probabilidades de que suceda.',
                   'No estoy seguro...',
                   'No sé que responder a eso :(',
                   'Por mi parte, ojalá.',
                   'Si lo quieres mucho, sucederá',
                   'Hay esperanzas, pocas, pero hay.',
                   '¿Para qué mentirte?',
                   'No veo por que no.',
                   'Lo siento, pero no.',
                   'Quizás, quizás no, no lo sé',
                   )
        if args is not None:
            answers_result = random.choice(answers)
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='A tu pregunta de...',
                value=f'*"{args}"*',
                inline=False,
            )
            embed.add_field(
                name='La respuesta es:',
                value=f'{answers_result}',
                inline=False,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

    @commands.command(aliases=['saludar'])
    async def greet(self, ctx, member=None):
        guild = ctx.guild
        if member is None:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Hola!',
                value=f'Te saludo, {ctx.author.name}',
            )
            embed.set_image(
                url='https://media1.tenor.com/images/'
                    '79f33c2f524cbfed4ef6896b39e67663/tenor.gif'
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        elif member is not None:
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='Alguien está saludándote...',
                value=f'{ctx.author.name} te saluda, {member}'
            )
            embed.set_image(
                url='https://media1.tenor.com/images/'
                    '056c584d9335fcabf080ca43e583e3c4/tenor.gif'
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            pass

    @commands.command(aliases=['llamar'])
    async def call(self, ctx, member=None):
        phone_numbers = [
            '0348-5154678',
            '2544-415-2547',
            '+14 15126784',
            '+97 15222747',
            '+11 55224978',
            '+34 51779522',
            '+21 47789521',
            '+378 55154449',
            '+4 411881264',
        ]
        pn_selected = random.choice(phone_numbers)
        if member is not None:
            message = await ctx.send('Conectando')
            time.sleep(0.5)
            await message.edit(content='Conectando.')
            time.sleep(0.5)
            await message.edit(content='Conectando..')
            time.sleep(0.5)
            await message.edit(content='Conectando...')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}.')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}..')
            time.sleep(0.5)
            await message.edit(content=f'Llamando a {member}...')
            time.sleep(0.5)
            await message.edit(content='*"Su"*')
            time.sleep(0.25)
            await message.edit(content='*"Su llamada al"*')
            time.sleep(0.25)
            await message.edit(content=f'*"Su llamada al {pn_selected}"*')
            time.sleep(0.25)
            await message.edit(content=f'*"Su llamada al {pn_selected} '
                                       'no recibió respuesta."*')
            time.sleep(1)
            await message.edit(content=f'{member} no contestó la llamada.')
        else:
            await ctx.send('¿A quién quieres llamar?')

    @commands.command(aliases=['prob'])
    async def probabilidad(self, ctx, *, args):
        guild = ctx.guild
        if args is not None:
            probabilidad = randint(0, 100)
            embed = discord.Embed(
                colour=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='La probabilidad de...',
                value=f'*"{args}"*',
                inline=False
            )
            embed.add_field(
                name='Es de un:',
                value=f'**{probabilidad}%**',
                inline=False
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)

        else:
            await ctx.send('Debes introducir una pregunta.')


def setup(bot):
    bot.add_cog(Comandos(bot))
