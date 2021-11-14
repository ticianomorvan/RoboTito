# Nextcord
import nextcord
from nextcord.ext import commands

# Helpers
from helpers.user import get_roles
from helpers.group import get_group_commands
from helpers.utility import datetime_parser, invite_expire, invite_uses

# Libraries
from random import choice


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    # User related commands.

    @commands.group(
        name='user',
        aliases=['us']
    )
    async def user(self, ctx: commands.Context):
        """Commands related to user's information."""
        if not ctx.invoked_subcommand:
            commands_embed = get_group_commands(self.bot, 'user')
            await ctx.send(embed=commands_embed)

    @user.command(
        name='profile',
        description='Retrieves user\'s information card.',
        aliases=['info']
    )
    async def profile(self, ctx: commands.Context,
                      member: nextcord.Member = None):
        """Retrieves user information"""
        user = ctx.author

        if member:
            user = member

        profile_embed = nextcord.Embed(title=user.name, color=user.color)

        profile_embed.set_thumbnail(url=user.default_avatar.url)

        if user.avatar is not None:
            profile_embed.set_thumbnail(url=user.avatar.url)

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
            name='🆔 ID:',
            value=f'{user.id}',
            inline=False
        )
        profile_embed.add_field(
            name='🔨 Roles:',
            value=f'{get_roles(user)}',
            inline=False
        )

        profile_embed.set_footer(
            text=f'Profile of {user.name}',
            icon_url=self.bot.user.avatar.url
        )
        await ctx.send(embed=profile_embed)

    @user.command(
        name='avatar',
        description='Returns your avatar or the given user\'s avatar.',
        aliases=['pic']
    )
    async def avatar(self, ctx: commands.Context,
                     member: nextcord.Member = None):
        """Returns an user avatar."""
        user = ctx.author

        if member:
            user = member

        avatar_embed = nextcord.Embed(
            title=user.name,
            color=user.color
        )

        avatar_embed.set_image(url=user.default_avatar.url)

        if user.avatar is not None:
            avatar_embed.set_image(url=user.avatar.url)

        avatar_embed.set_footer(
            text=f'hash: {hash(user.avatar)}',
            icon_url=self.bot.user.avatar.url
        )

        await ctx.send(embed=avatar_embed)

    # Guild / Server related commands.

    @commands.group(
        name='server',
        aliases=['sv']
    )
    async def server(self, ctx: commands.Context):
        """Commands related to server's information."""
        if not ctx.invoked_subcommand:
            commands_embed = get_group_commands(self.bot, 'server')
            await ctx.send(embed=commands_embed)

    @server.command(
        name='information',
        description='Returns server information.',
        aliases=['info']
    )
    async def information(self, ctx: commands.Context):
        """Returns an embed with server information."""
        server = ctx.guild
        server_embed = nextcord.Embed(
            title=server.name,
            color=ctx.author.color
        )

        server_embed.set_thumbnail(
            url=server.icon.url
        )

        if server.description:
            server_embed.add_field(
                name='📔 Description:',
                value=server.description,
                inline=False
            )

        server_embed.add_field(
            name='🧑‍🤝‍🧑 Members:',
            value=f'There are {server.member_count} members in the server!',
            inline=False
        )

        server_embed.add_field(
            name='👑 Owner:',
            value=f'This server is property of {server.owner.mention}!',
            inline=False
        )

        server_embed.add_field(
            name='📣 Channels:',
            value=f'There are {len(server.text_channels)} text channels'
                  f' and {len(server.voice_channels)} voice channels!',
            inline=False
        )

        server_embed.add_field(
            name='🔨 Roles:',
            value=f'There are {len(server.roles)}'
                  ' different roles in the server!',
            inline=False
        )

        if server.emojis:
            server_embed.add_field(
                name='😃 Emojis:',
                value='The server has a total of'
                      f' {len(server.emojis)} emojis!',
                inline=False
            )

        if server.stickers:
            server_embed.add_field(
                name='🖼️ Stickers:',
                value=f'There are {len(server.emojis)}'
                      ' stickers in the server!',
                inline=False
            )

        server_embed.set_footer(
            text=f'Requested by {ctx.author.name}',
            icon_url=self.bot.user.avatar.url
        )

        await ctx.send(embed=server_embed)

    @server.command(
        name='icon',
        description='Retrieves the server\'s icon.'
    )
    async def icon(self, ctx: commands.Context):
        """Returns the server icon."""
        server = ctx.guild
        server_embed = nextcord.Embed(
            title=f'{server.name}\'s icon',
            color=ctx.author.color
        )

        server_embed.set_image(
            url=server.icon.url
        )

        server_embed.set_footer(
            text=f'Requested by {ctx.author.name}',
            icon_url=self.bot.user.avatar.url
        )

        await ctx.send(embed=server_embed)

    @server.command(
        name='roles',
        description='Retrieves the server\'s roles.'
    )
    async def roles(self, ctx: commands.Context):
        server = ctx.guild
        if not ctx.author.guild_permissions.manage_roles:
            await ctx.send('You don\'t have the permissions to do that!')
        else:
            server_embed = nextcord.Embed(
                title=f'🔨 {server.name}\'s roles',
                color=ctx.author.color
            )

            all_server_roles = ''

            for role in reversed(server.roles):
                if role.name != '@everyone':
                    all_server_roles += f'<@&{role.id}> — '
                    all_server_roles += f'{len(role.members)} members.\n'

            server_embed.add_field(
                name='All roles:',
                value=all_server_roles,
                inline=False
            )

            server_embed.set_footer(
                text=f'Requested by {ctx.author.name}',
                icon_url=self.bot.user.avatar.url
            )

            await ctx.send(embed=server_embed)

    @server.command(
        name='bots',
        description='Returns all the bots that belongs to the server.'
    )
    async def bots(self, ctx: commands.Context):
        """Returns an embed with all bots in the server."""
        bots_embed = nextcord.Embed(
            title='🤖 Server\'s bots',
            color=ctx.author.color
        )

        bots_in_server = ''
        for bot in ctx.guild.bots:
            bots_in_server += f'- {bot.mention}\n'

        bots_embed.add_field(
            name='These are the bots that are in this server:',
            value=bots_in_server
        )

        bots_embed.set_footer(
            text=f'There is a total of {len(ctx.guild.bots)}'
                 ' bots in this server!',
            icon_url=self.bot.user.avatar.url
        )

        await ctx.send(embed=bots_embed)

    @server.command(
        name='users',
        description='Returns some users that belongs to the server.',
        aliases=['members']
    )
    async def users(self, ctx: commands.Context):
        """Returns an embed with some users that belongs to the server."""
        users_embed = nextcord.Embed(
            title='💁 People in this server',
            color=ctx.author
        )

        users_in_server = ctx.guild.humans
        users_in_list = ''
        max_users_in_list = 10

        if len(users_in_server) <= max_users_in_list:
            for user in users_in_server:
                users_in_list += f'- {user.name}\n'
        else:
            while max_users_in_list > 0:
                users_in_list += f'- {choice(users_in_server).name}\n'
                max_users_in_list -= 1

        users_embed.add_field(
            name='These are some people that are in the server:',
            value=users_in_list
        )

        users_embed.set_footer(
            text=f'There are {len(ctx.guild.humans)} humans in this server!',
            icon_url=self.bot.user.avatar.url
        )

        await ctx.send(embed=users_embed)

    @server.command(
        name='bans',
        description='Retrieves a list of the server\'s banned users.'
    )
    async def bans(self, ctx: commands.Context):
        """Returns an embed with the banned users from the server."""
        if not ctx.author.guild_permissions.ban_members:
            await ctx.send('You don\'t have permission to do this!')
        else:
            server = ctx.guild
            server_embed = nextcord.Embed(
                title=f'{server.name}\'s bans',
                color=ctx.author.color
            )

            server_embed.set_thumbnail(
                url=server.icon.url
            )

            all_server_bans = ''

            for ban in await server.bans():
                all_server_bans += f'{ban.user.name} — {ban.reason}\n'

            if not all_server_bans:
                server_embed.add_field(
                    name='There aren\'t any bans in the server.',
                    value='Maybe that\'s a good thing...'
                )
            else:
                server_embed.add_field(
                    name='All bans:',
                    value=all_server_bans
                )

            server_embed.set_footer(
                text=f'Requested by {ctx.author.name}',
                icon_url=self.bot.user.avatar.url
            )

            await ctx.send(embed=server_embed)

    @server.command(
        name='invitations',
        description='Retrieves all active invites.',
        aliases=['invites']
    )
    async def invitations(self, ctx: commands.Context):
        if not ctx.author.guild_permissions.create_instant_invite:
            await ctx.send('You don\'t have permission to do this!')
        else:
            server = ctx.guild
            server_embed = nextcord.Embed(
                title=f'{server.name}\'s invites',
                color=ctx.author.color
            )

            for invite in await server.invites():
                server_embed.add_field(
                    name=invite.code,
                    value=f'Created at: {datetime_parser(invite.created_at)}\n'
                          'Uses: '
                          f'{invite_uses(invite.uses, invite.max_uses)}\n'
                          f'Inviter: {invite.inviter.mention}\n'
                          f'Expires at: {invite_expire(invite.expires_at)}\n'
                          f'Channel: {invite.channel.mention}\n'
                          f'URL: {invite.url}',
                    inline=False
                )

            server_embed.set_footer(
                text=f'Requested by {ctx.author.name}',
                icon_url=self.bot.user.avatar.url
            )

            await ctx.send(embed=server_embed)


def setup(bot: commands.Bot):
    bot.add_cog(Information(bot))
