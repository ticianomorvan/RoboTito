import discord
from discord.ext import commands

import datetime

import random
# from random import randint


class Anime(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hug')
    async def abrazo(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        hug_dict = [
            'https://media1.tenor.com/images/1069921ddcf38ff722125c8f65401c28/'
            'tenor.gif',
            'https://media1.tenor.com/images/78d3f21a608a4ff0c8a09ec12ffe763d/'
            'tenor.gif',
            'https://media1.tenor.com/images/1d94b18b89f600cbb420cce85558b493/'
            'tenor.gif',
            'https://media1.tenor.com/images/e9d7da26f8b2adbb8aa99cfd48c58c3e/'
            'tenor.gif',
            'https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/'
            'tenor.gif',
            'https://media1.tenor.com/images/bb9c0c56769afa3b58b9efe5c7bcaafb/'
            'tenor.gif',
            'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/'
            'tenor.gif',
            'https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/'
            'tenor.gif',
            'https://media1.tenor.com/images/5ccc34d0e6f1dccba5b1c13f8539db77/'
            'tenor.gif',
            'https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/'
            'tenor.gif',
            'https://media1.tenor.com/images/4db088cfc73a5ee19968fda53be6b446/'
            'tenor.gif',
            'https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/'
            'tenor.gif',
            'https://media1.tenor.com/images/daffa3b7992a08767168614178cce7d6/'
            'tenor.gif',
            'https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/'
            'tenor.gif',
            'https://media1.tenor.com/images/c7efda563983124a76d319813155bd8e/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Abrazo!',
                value=f'{ctx.author.name} abraza a {member.name}',
            )
            hug_gif = random.choice(hug_dict)
            embed.set_image(
                url=hug_gif,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f'Oye, {ctx.author}, yo te abrazaría ¿sabes?, '
                'pero soy un robot.'
            )

    @commands.command(name='kiss')
    async def beso(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        kiss_dict = [
            'https://media1.tenor.com/images/503bb007a3c84b569153dcfaaf9df46a/'
            'tenor.gif',
            'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/'
            'tenor.gif',
            'https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/'
            'tenor.gif',
            'https://media1.tenor.com/images/f102a57842e7325873dd980327d39b39/'
            'tenor.gif',
            'https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/'
            'tenor.gif',
            'https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/'
            'tenor.gif',
            'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/'
            'tenor.gif',
            'https://media1.tenor.com/images/e76e640bbbd4161345f551bb42e6eb13/'
            'tenor.gif',
            'https://media1.tenor.com/images/02d9cae34993e48ab5bb27763d5ca2fa/'
            'tenor.gif',
            'https://media1.tenor.com/images/6f455ef36a0eb011a60fad110a44ce68/'
            'tenor.gif',
            'https://media1.tenor.com/images/a1f7d43752168b3c1dbdfb925bda8a33/'
            'tenor.gif',
            'https://media1.tenor.com/images/621ceac89636fc46ecaf81824f9fee0e/'
            'tenor.gif',
            'https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/'
            'tenor.gif',
            'https://media1.tenor.com/images/d0cd64030f383d56e7edc54a484d4b8d/'
            'tenor.gif',
            'https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/'
            'tenor.gif',
            'https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡El amor nace!',
                value=f'{ctx.author.name} besa a'
                      f' {member.name} con mucho amor.',
                inline=False
            )
            kiss_gif = random.choice(kiss_dict)
            embed.set_image(
                url=kiss_gif
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                'No creo que puedas besarte a ti mism@, a menos que...'
            )

    @commands.command(name='pat')
    async def caricia(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        pat_dict = [
            'https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/'
            'tenor.gif',
            'https://media1.tenor.com/images/e5fff7bc2fc641f8ed0cba92475ea741/'
            'tenor.gif',
            'https://media1.tenor.com/images/55df4c5fb33f3cd05b2f1ac417e050d9/'
            'tenor.gif',
            'https://media1.tenor.com/images/d9b480bcd392d05426ae6150e986bbf0/'
            'tenor.gif',
            'https://media1.tenor.com/images/90712ed3a99db973ec92383a3c6a8767/'
            'tenor.gif',
            'https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/'
            'tenor.gif',
            'https://media1.tenor.com/images/6151c42c94df654b1c7de2fdebaa6bd1/'
            'tenor.gif',
            'https://media1.tenor.com/images/f5176d4c5cbb776e85af5dcc5eea59be/'
            'tenor.gif',
            'https://media1.tenor.com/images/2b3ddd79058842ccb9c1fc6acea0bcaa/'
            'tenor.gif',
            'https://media1.tenor.com/images/daa885ec8a9cfa4107eb966df05ba260/'
            'tenor.gif',
            'https://media1.tenor.com/images/bfdeb9ec7f89aad86170d06fe4189bec/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Caricias para todos!',
                value=f'{ctx.author.name} acaricia a {member.name}',
                inline=False
            )
            pat_gif = random.choice(pat_dict)
            embed.set_image(
                url=pat_gif
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                'Creo que el amor propio es una parte '
                'importante que tener en cuenta.'
            )

    @commands.command(name='punch')
    async def golpear(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        punch_dict = [
            'https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/'
            'tenor.gif',
            'https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/'
            'tenor.gif',
            'https://media1.tenor.com/images/2e36b49b3d26d1e2fe014e5d4c1dbc75/'
            'tenor.gif',
            'https://media1.tenor.com/images/b111863f0714504a8ba22a0c68e78f32/'
            'tenor.gif',
            'https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/'
            'tenor.gif',
            'https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/'
            'tenor.gif',
            'https://media1.tenor.com/images/965fabbfcdc09ee0eb4d697e25509f34/'
            'tenor.gif',
            'https://media1.tenor.com/images/0654104d7eaeb87978733accfc575613/'
            'tenor.gif',
            'https://media1.tenor.com/images/d7c30e46a937aaade4d7bc20eb09339b/'
            'tenor.gif',
            'https://media1.tenor.com/images/99189c9eeb18be326a4d691c6ebd5888/'
            'tenor.gif',
            'https://media1.tenor.com/images/b11f32dd0cd96da2972fe1998a8f6286/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='¡Golpe rabioso!',
                value=f'{member.name} recibe una fuerte'
                      f' paliza de {ctx.author.name}',
                inline=False
            )
            punch_gif = random.choice(punch_dict)
            embed.set_image(
                url=punch_gif,
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send(
                'No es demasiado sano que te golpees a ti mismo.'
            )

    @commands.command(name='sleep')
    async def dormir(self, ctx, member: discord.Member = None):
        guild = ctx.guild
        sleep_dict = [
            'https://media1.tenor.com/images/bad0e118dc9e1f66f8baf9291112c989/'
            'tenor.gif',
            'https://media1.tenor.com/images/7175fe4b5e789b94b41a793e2fd4db3d/'
            'tenor.gif',
            'https://media1.tenor.com/images/1cdece239ec7d0fb33d2976d623f5e77/'
            'tenor.gif',
            'https://media1.tenor.com/images/b0daf8299389bf3fa4260a91690f0e12/'
            'tenor.gif',
            'https://media1.tenor.com/images/d599b5c2904739a35fbbf7ad30c506c5/'
            'tenor.gif',
            'https://media1.tenor.com/images/a7e8e8f9fd0a8784012d8f14b09da4a8/'
            'tenor.gif',
            'https://media1.tenor.com/images/81b39f20f9369290a0f3c8148427480e/'
            'tenor.gif',
            'https://media1.tenor.com/images/536666c6ed48d260e68ae067a5e7129c/'
            'tenor.gif',
            'https://media1.tenor.com/images/b190ed9c1cde30f00026433c8b5463ed/'
            'tenor.gif',
            'https://media1.tenor.com/images/766a25de69e36c91d06726ba3113b234/'
            'tenor.gif',
            'https://media1.tenor.com/images/6ced70626bc6ef8c47b49c6bd36a963c/'
            'tenor.gif',
        ]
        sleepw_dict = [
            'https://media1.tenor.com/images/18474dc6afa97cef50ad53cf84e37d08/'
            'tenor.gif',
            'https://media1.tenor.com/images/66c5a0d8405bea5d9bd99f406d844094/'
            'tenor.gif',
            'https://media1.tenor.com/images/8dd205d60e89ebcccb087820a47e2453/'
            'tenor.gif',
            'https://media1.tenor.com/images/bfacd94f66bdde64009f420277464e67/'
            'tenor.gif',
            'https://media1.tenor.com/images/18ab3dfa6a62a04d663eeee77fbdf901/'
            'tenor.gif',
            'https://media1.tenor.com/images/d2c429ba4072d427916287e1bb1e784a/'
            'tenor.gif',
            'https://media1.tenor.com/images/114361cbe30f6054fa204876295a6115/'
            'tenor.gif',
            'https://media1.tenor.com/images/e57ae19196e9ce618e21e0fd87985afc/'
            'tenor.gif',
            'https://media1.tenor.com/images/d3310176eb4f8ab65cd1bed917f5fba8/'
            'tenor.gif',
            'https://media1.tenor.com/images/d69811c67f629715448f8d1dbb2370f1/'
            'tenor.gif',
            'https://media1.tenor.com/images/4d3cce7fe44adc2ad944ecb6f02e98ba/'
            'tenor.gif',
        ]
        if member is not None:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Los tórtolos se acurrucan...',
                value=f'{ctx.author.name} y '
                      f'{member.name} se acuestan juntos...',
                inline=False,
            )
            sleepw_gif = random.choice(sleepw_dict)
            embed.set_image(
                url=sleepw_gif
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                color=discord.Color.blue(),
                timestamp=datetime.datetime.utcnow(),
            )
            embed.add_field(
                name='Alguien está con sueño...',
                value=f'{ctx.author.name} se va a dormir.',
                inline=False,
            )
            sleep_gif = random.choice(sleep_dict)
            embed.set_image(
                url=sleep_gif
            )
            embed.set_footer(
                text=guild,
                icon_url=guild.icon_url,
            )
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Anime(bot))
