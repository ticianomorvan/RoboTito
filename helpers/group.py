import nextcord
from nextcord.ext import commands


def get_group_commands(bot: commands.Bot, group: str):
    """Returns an embed with the commands in a group"""
    group_commands_embed = nextcord.Embed(
        title=f'{group.capitalize()}\'s commands',
        color=bot.user.color
    )

    group_commands = 0

    for command in bot.walk_commands():
        if str(command.parent) == group:
            group_commands_embed.add_field(
                name=command.name,
                value=f'{command.description}',
                inline=False
            )

            group_commands += 1

    group_commands_embed.set_footer(
        text=f'This group has {group_commands} commands! |'
             f' Use {bot.command_prefix}help for more information.',
        icon_url=bot.user.avatar.url
    )

    return group_commands_embed
