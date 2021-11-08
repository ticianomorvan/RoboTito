import nextcord
from nextcord.ext import commands
from helpers.user import get_roles
from helpers.client import github


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def profile(self, ctx: commands.Context,
                      member: nextcord.Member = None):
        """Retrieves user information"""
        if member is not None:
            user = member
        else:
            user = ctx.author

        profile_embed = nextcord.Embed(title=user.name, color=user.color)
        profile_embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.default_avatar.url,
            url=github
        )
        if user.avatar.url is not None:
            profile_embed.set_thumbnail(url=user.avatar.url)
        else:
            profile_embed.set_thumbnail(url=user.default_avatar.url)

        profile_embed.add_field(
            name='😎 Name:',
            value=user.name,
            inline=False
        )
        profile_embed.add_field(
            name='🤔 Nick:',
            value=user.nick,
            inline=False
        )
        profile_embed.add_field(
            name='📅 Account created:',
            value=f'{user.created_at.day}/{user.created_at.month}'
                  f'/{user.created_at.year}',
            inline=False
        )
        profile_embed.add_field(
            name='📅 Join date:',
            value=f'{user.joined_at.day}/{user.joined_at.month}'
                  f'/{user.joined_at.year}',
            inline=False
        )
        profile_embed.add_field(
            name='🪪 ID:',
            value=f'{user.id}',
            inline=False
        )
        profile_embed.add_field(
            name='🔨 Roles:',
            value=f'{get_roles(user)}',
            inline=False
        )
        await ctx.send(embed=profile_embed)

    @commands.command()
    async def avatar(self, ctx: commands.Context,
                     member: nextcord.Member = None):
        """Returns an user avatar."""
        if member is not None:
            user = member
        else:
            user = ctx.author

        avatar_embed = nextcord.Embed(
            title=user.name,
            color=user.color
        )
        avatar_embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.default_avatar.url,
            url=github
        )
        if user.avatar.url is not None:
            avatar_embed.set_image(
                url=user.avatar.url
            )
        else:
            avatar_embed.set_image(
                url=user.default_avatar.url
            )
        await ctx.send(embed=avatar_embed)


def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))
