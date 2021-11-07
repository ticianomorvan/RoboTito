import nextcord
from nextcord.ext import commands


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def profile(self, ctx: commands.Context,
                      user: nextcord.Member = None):
        """Retrieves user information"""
        if user is not None:
            profile_image = user.avatar.url
            profile_name = user.name
            profile_created_at = user.created_at
            profile_joined_at = user.joined_at
            profile_color = user.colour
            profile_id = user.id
            profile_roles = user.roles
            if user.nick is not None:
                profile_nick = user.nick
            else:
                profile_nick = 'Este usuario no tiene apodo.'
        else:
            profile_image = ctx.author.avatar.url
            profile_name = ctx.author.name
            profile_created_at = ctx.author.created_at
            profile_joined_at = ctx.author.joined_at
            profile_color = ctx.author.colour
            profile_id = ctx.author.id
            profile_roles = ctx.author.roles
            if ctx.author.nick is not None:
                profile_nick = ctx.author.nick
            else:
                profile_nick = 'No tienes apodo.'

        profile_embed = nextcord.Embed(title=profile_name, color=profile_color)
        profile_embed.set_author(
            name=self.bot.user.name,
            icon_url=self.bot.user.default_avatar.url
        )
        profile_embed.set_thumbnail(url=profile_image)
        profile_embed.add_field(
            name='Nombre:',
            value=profile_name,
            inline=False
        )
        profile_embed.add_field(
            name='Nick:',
            value=profile_nick,
            inline=False
        )
        profile_embed.add_field(
            name='Cuenta creada:',
            value=f'{profile_created_at.day}/{profile_created_at.month}'
                  f'/{profile_created_at.year}',
            inline=False
        )
        profile_embed.add_field(
            name='Se unió:',
            value=f'{profile_joined_at.day}/{profile_joined_at.month}'
                  f'/{profile_joined_at.year}',
            inline=False
        )
        profile_embed.add_field(
            name='ID:',
            value=f'{profile_id}',
            inline=False
        )
        profile_embed.add_field(
            name='Roles:',
            value=f'{profile_roles}',
            inline=False
        )
        await ctx.send(embed=profile_embed)


def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))
