from nextcord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def clean(self, ctx: commands.Context, amount=100):
        """Cleans a text channel by the given amount or 100 by default."""
        if not ctx.author.guild_permissions.manage_channels:
            await ctx.send('You **don\'t** have the needed'
                           ' permissions to do this!')
        elif amount > 100:
            await ctx.send('I can\'t delete more than 100 messages at once!')

        else:
            deleted_messages = await ctx.channel.purge(limit=amount)
            await ctx.channel.send(
                f'Successfully deleted 🗑️ **{len(deleted_messages)} messages**'
                f' in {ctx.channel.mention} by {ctx.author.mention}'
            )


def setup(bot: commands.Bot):
    bot.add_cog(Moderation(bot))
