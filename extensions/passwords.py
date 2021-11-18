# Nextcord
from operator import length_hint
import nextcord
from nextcord.ext import commands

# Randoms
import random

from nextcord.ext.commands.core import command

# Variables
Slower = 'abcdefghijklmnñopqrstuvwxyz'
Supper = 'ABCDEFGHIJKLMN;OPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+=-|'

#commands
class Passwords(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command(
        aliases=['pass', 'word']
    )
    async def password(self, args, ctx: commands.Context):
        if args == 'spanish' and 'Spanish':
            all=Slower + Supper + numbers + symbols
            length = 9
            password = "".join(random.sample(all,length))
            text = f'Your new password is: {password}'
            await ctx.send(text)
        elif args == 'english' and 'English':
            all=lower + upper + numbers + symbols
            length = 9
            password = "".join(random.sample(all,length))
            await ctx.send(password)
        elif args is None:
            arg = "Please i need a language to generate a passwors, use 'spanish' or 'english'."
            await ctx.send(arg)


def setup(bot: commands.Bot):
    bot.add_cog(Passwords(bot))