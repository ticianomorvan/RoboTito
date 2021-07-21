from discord import Embed
from discord.ext import commands
from discord.member import Member
from cog.helpers import gifs, strings, rbColor
from random import choice


class Helpers():
    def header(table):
        header = strings[table]
        return choice(header)

    def gif(table):
        return choice(gifs[table])

    def sentence(author, msg, member=None):
        if member is None:
            message = choice(strings[msg])
            result = author + message
            return result
        else:
            message = choice(strings[msg])
            result = author + message + member
            return result

    def get_embed(type: str, author, member=None):
        e = Embed(color=rbColor())
        if member is not None:
            e.add_field(name=Helpers.header(f'h_{type}'),
                        value=Helpers.sentence(
                            author, f'm_{type}', member))
        else:
            e.add_field(name=Helpers.header(f'h_{type}'),
                        value=Helpers.sentence(
                            author, f'm_{type}'))

        e.set_image(url=Helpers.gif(type))
        return e


class Interaction(commands.Cog, name='Interacción',
                  description='Comandos para interactuar'
                              ' usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'], help='Dale un abrazo a alguien.')
    async def hug(self, ctx, member: Member):
        e = Helpers.get_embed('hug', ctx.author.name, member.name)
        await ctx.send(embed=e)

    @commands.command(aliases=['beso'], help='Besa a alguien.')
    async def kiss(self, ctx, member: Member):
        e = Helpers.get_embed('kiss', ctx.author.name, member.name)
        await ctx.send(embed=e)

    @commands.command(aliases=['acariciar'], help='Acaricia a alguien.')
    async def pat(self, ctx, member: Member):
        e = Helpers.get_embed('pat', ctx.author.name, member.name)
        await ctx.send(embed=e)

    @commands.command(aliases=['golpear'], help='Golpea a alguien.')
    async def punch(self, ctx, member: Member):
        e = Helpers.get_embed('punch', ctx.author.name, member.name)
        await ctx.send(embed=e)

    @commands.command(aliases=['dormir'], help='Duerme con o sin alguien más.')
    async def sleep(self, ctx, member: Member = None):
        if member is None:
            e = Helpers.get_embed('sleep', ctx.author.name)
            await ctx.send(embed=e)
        elif member == ctx.author:
            await ctx.send('No te acuestes contigo mismo.')
        else:
            e = Helpers.get_embed('sleepw', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['matar'], help='Mata a alguien.')
    async def kill(self, ctx, member: Member):
        e = Helpers.get_embed('kill', ctx.author.name, member.name)
        await ctx.send(embed=e)

    @commands.command(aliases=['saludar', 'hi'],
                      help='Saluda a todo el mundo o a alguien especial.')
    async def greet(self, ctx, member: Member = None):
        if member == ctx.author:
            await ctx.send('Saluda a alguien más.')
        elif member is not None:
            e = Helpers.get_embed('greets', ctx.author.name, member.name)
            await ctx.send(embed=e)
        else:
            e = Helpers.get_embed('greet', ctx.author.name)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Interaction(bot))
