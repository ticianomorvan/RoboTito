from cog.functions.functions import Functions as f
from discord.ext import commands
from discord.member import Member


class Interaction(commands.Cog, name='Interacción',
                  description='Comandos para interactuar'
                              ' usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'], help='Dale un abrazo a alguien.')
    async def hug(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(f.sameUser('abrazar a'))
        else:
            e = f.getEmbed('hug', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['beso'], help='Besa a alguien.')
    async def kiss(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(f.sameUser('besar a'))
        else:
            e = f.getEmbed('kiss', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['acariciar'], help='Acaricia a alguien.')
    async def pat(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(f.sameUser('acariciar a'))
        else:
            e = f.getEmbed('pat', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['golpear'], help='Golpea a alguien.')
    async def punch(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(f.sameUser('golpear a'))
        else:
            e = f.getEmbed('punch', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['dormir'], help='Duerme con o sin alguien más.')
    async def sleep(self, ctx, member: Member = None):
        if member is None:
            e = f.getEmbed('sleep', ctx.author.name)
            await ctx.send(embed=e)
        elif member == ctx.author:
            await ctx.send(f.sameUser('acostarte con'))
        else:
            e = f.getEmbed('sleepw', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(aliases=['matar'], help='Mata a alguien.')
    async def kill(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(f.sameUser('matar a'))
        else:
            e = f.getEmbed('kill', ctx.author.name, member.name)
            await ctx.send(embed=e)

    @commands.command(
        aliases=['saludar', 'hi'],
        help='Saluda a todo el mundo o a alguien especial.'
    )
    async def greet(self, ctx, member: Member = None):
        if member is None:
            e = f.getEmbed('greet', ctx.author.name,)
            await ctx.send(embed=e)
        elif member == ctx.author:
            await ctx.send(f.sameUser('saludar a'))
        else:
            e = f.getEmbed('greets', ctx.author.name, member.name)
            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Interaction(bot))
