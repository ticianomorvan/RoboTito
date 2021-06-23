from cog.functions.functions import Functions as function
from discord.ext import commands
from discord.member import Member


class Anime(commands.Cog,
            name='Interacción',
            description='Comandos para interactuar usando gifs de anime.'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['abrazo'], help='Dale un abrazo a alguien.')
    async def hug(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(function.sameUser('abrazar a'))

        else:
            e = function.getEmbed(
                'hug',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['beso'], help='Besa a alguien.')
    async def kiss(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(function.sameUser('besar a'))

        else:
            e = function.getEmbed(
                'kiss',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )
            await ctx.send(embed=e)

    @commands.command(aliases=['acariciar'], help='Acaricia a alguien.')
    async def pat(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(function.sameUser('acariciar a'))

        else:
            e = function.getEmbed(
                'pat',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['golpear'], help='Golpea a alguien.')
    async def punch(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(function.sameUser('golpear a'))

        else:
            e = function.getEmbed(
                'punch',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['dormir'], help='Duerme con o sin alguien más.')
    async def sleep(self, ctx, member: Member = None):
        if member is None:
            e = function.getEmbed('sleep', ctx.author.name,
                                  ctx.guild.name, ctx.guild.icon_url)

            await ctx.send(embed=e)

        elif member == ctx.author:
            await ctx.send(function.sameUser('acostarte con'))

        else:
            e = function.getEmbed(
                'sleepw',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)

    @commands.command(aliases=['matar'], help='Mata a alguien.')
    async def kill(self, ctx, member: Member = None):
        if member is None or member == ctx.author:
            await ctx.send(function.sameUser('matar a'))

        else:
            e = function.getEmbed(
                'kill',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)

    @commands.command(
        aliases=['saludar', 'hi'],
        help='Saluda a todo el mundo o a alguien especial.'
    )
    async def greet(self, ctx, member: Member = None):
        if member is None:
            e = function.getEmbed(
                'greet',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
            )

            await ctx.send(embed=e)

        elif member == ctx.author:
            await ctx.send(function.sameUser('saludar a'))

        else:
            e = function.getEmbed(
                'greets',
                ctx.author.name,
                ctx.guild.name,
                ctx.guild.icon_url,
                member.name
            )

            await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Anime(bot))
