from asyncio import sleep
from random import sample
from nextcord import Embed
from nextcord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(
        name='password',
        description='Generate a secure password.',
        aliases=['pass']
    )
    async def password(self, ctx: commands.Context, length=16):
        """Generates a random password."""
        password_lower = 'abcdefghijklmnopqrstuvwxyz'
        password_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        password_numbers = '0123456789'
        password_characters = password_lower + password_upper + password_numbers
        password_result = ''.join(sample(password_characters, int(length)))

        if int(length) < 8 or int(length) > 16:
            message = await ctx.send('A password shorter than 8 characters is insecure.'
                                     ' In the other hand, a password longer than 16'
                                     ' characters is sometimes disallowed, so keep that in mind. ')
            await sleep(10)
            await message.delete()
        else:
            password_embed = Embed(
                title='🔐 Password generator',
                color=ctx.author.color
            )
            password_embed.add_field(
                name=password_result,
                value='This is your password!'
            )

            await ctx.send(embed=password_embed)


def setup(bot: commands.Bot):
    bot.add_cog(Utility(bot))
