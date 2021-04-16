import discord
from discord.ext import commands

import datetime


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild

        # Guilds
        titogang = self.bot.get_guild(786392734377967676)
        neet = self.bot.get_guild(804077562087079936)

        # TitoGvng
        if guild == titogang:
            embed = discord.Embed(
                color=discord.Color.red(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='¡Te doy la bienvenida!',
                value='Tenemos mucha suerte de encontrate aquí,'
                      f'{member.mention}, '
                      '¡espero que te diviertas!'
            )
            embed.set_image(
                url='https://bestanimations.com/Nature/Water/'
                    'lake/lake-nature-animated-gif-7.gif'
            )
            embed.set_footer(text='Bienvenida de RoboTito')
            await self.bot.get_channel(786393328924098580).send(embed=embed)

        # NEET
        elif guild == neet:
            embed = discord.Embed(
                color=discord.Colour.from_rgb(202, 21, 180),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='¡𝑻𝒆 𝒅𝒂𝒎𝒐𝒔 𝒍𝒂 𝒃𝒊𝒆𝒏𝒗𝒆𝒏𝒊𝒅@!',
                value=f'𝑩𝒊𝒆𝒏𝒗𝒆𝒏𝒊𝒅@ {member.mention} 𝒂 '
                      f'{member.guild.name} 𝑹𝒆𝒄𝒖𝒆𝒓𝒅𝒂 𝒍𝒆𝒆𝒓 '
                      '𝒍𝒂𝒔 𝒓𝒆𝒈𝒍𝒂𝒔 𝒚 𝒔𝒆𝒓 𝒃𝒖𝒆𝒏𝒐 𝒄𝒐𝒏 𝒕𝒐𝒅𝒐𝒔 '
                      '𝒍𝒐𝒔 𝒑𝒖𝒕𝒐𝒔 𝒅𝒆 𝒆𝒔𝒕𝒆 𝒔𝒆𝒓𝒗𝒆𝒓'
            )
            embed.set_image(
                url='https://images-ext-2.discordapp.net/'
                    'external/Z-_ALisndUqmon'
                    'TIDdOi2MrkBNFgFsWU_'
                    'aZvGapnXgQ/https/p4.wallpaperbetter.com/'
                    'wallpaper/416/977/172/'
                    'anime-otaku-hd-wallpaper-preview.jpg'
            )
            embed.set_footer(text='Bienvenida de RoboTito')
            await self.bot.get_channel(815375493541003276).send(embed=embed)

        else:
            return


def setup(bot):
    bot.add_cog(Welcome(bot))
