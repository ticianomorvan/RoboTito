# Nextcord
from nextcord.ext import commands

# Randoms
import random

# Variabless
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&'


# commands
class Passwords(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(
        aliases=['pass', 'word']
    )
    async def password(self, ctx: commands.Context):
        all = lower + upper + numbers + symbols
        length = 9
        password = "".join(random.sample(all, length))
        await ctx.send(
            f'This is your password: `{password}`,'
            " if you don't like it,"
            ' or if you want to make changes,'
            ' you can visit:'
            ' https://react-password-generator-'
            'seven.vercel.app/'
            '. This page was made by: Titoyan, who is my creator'
        )


def setup(bot: commands.Bot):
    bot.add_cog(Passwords(bot))
