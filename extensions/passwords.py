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
    async def password(self, ctx: commands.Context, length = 12):
        if not length in range(8, 16):
            all = lower + upper + numbers + symbols
            password = "".join(random.sample(all, length))
            await ctx.send(
                f'This is your password: `{password}`.'
            )
        else:
            all = lower + upper + numbers + symbols
            password = "".join(random.sample(all, length))
            await ctx.send(
                f'This is your password: `{password}`.'
            )


def setup(bot: commands.Bot):
    bot.add_cog(Passwords(bot))
