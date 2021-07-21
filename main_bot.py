import discord
import logging
import tomli
from cog.helpers import rbColor
from discord.ext import commands

# Logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='robotito.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:'
                                       '%(name)s: %(message)s'))
logger.addHandler(handler)

# Start
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=['r.'], intents=intents, help_command=None)

initial_extensions = ['cog.error_handling',
                      'cog.information',
                      'cog.interaction',
                      'cog.leagueoflegends',
                      'cog.moderation',
                      'cog.utility',
                      'cog.variety']

for extension in initial_extensions:
    bot.load_extension(extension)


class MyHelp(commands.MinimalHelpCommand):
    async def send_bot_help(self, mapping):
        ctx = self.context
        embed = discord.Embed(title='Ayuda de RoboTito')
        embed.set_thumbnail(url=ctx.me.avatar_url)
        usable = 0

        for cog, bot_commands in mapping.items():
            if filtered_commands := await self.filter_commands(bot_commands):
                amount_commands = len(filtered_commands)
                usable += amount_commands
                if cog:
                    name = cog.qualified_name
                else:
                    name = "Varios"

                embed.add_field(name=f'{name}', value=f'**{amount_commands}** '
                                                      'comandos disponibles.')

        embed.description = f'**{len(bot.commands)}** comandos en total.'
        embed.color = rbColor()
        embed.set_footer(text='r.help <categoría> para más información.')
        await ctx.send(embed=embed)

    async def send_command_help(self, command):
        e = discord.Embed(color=rbColor(), description=command.help)
        e.set_author(name=f'Comandos - {command.name}',
                     url='https://ticiano-morvan.gitbook.io/spanish/comandos')
        aliases = command.aliases
        if aliases is not None:
            e.add_field(name="Aliases", value=", ".join(aliases),
                        inline=False)
        e.add_field(name='Uso',
                    value=f'`{self.get_command_signature(command)}`',
                    inline=False)
        e.set_footer(text='Argumentos: <requerido> [opcional]')
        channel = self.get_destination()
        await channel.send(embed=e)

    async def get_all_commands(self, commands):
        string = '```'
        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                string += f'{self.get_command_signature(command)}\n'

            return f'{string}```'

    async def send_cog_help(self, cog):
        e = discord.Embed(color=rbColor(), title=cog.qualified_name,
                          description=cog.description)
        e.add_field(name='Comandos',
                    value=await MyHelp.get_all_commands(
                        self, cog.get_commands()),
                    inline=False)

        e.set_footer(text='r.help <comando> para más información. '
                          '- <requerido> [opcional]')
        channel = self.get_destination()
        await channel.send(embed=e)


bot.help_command = MyHelp()


@bot.event
async def on_ready():
    print('Conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(
                                type=discord.ActivityType.watching,
                                name='RoboTito! | r.help'))


# Run

# You have to create an "config.toml" file at databases folder, with:
# token = "your_bot_token"
# rapidapi = "your_rapidapi_token"
# cuttly = "your_cuttly_token"

with open('databases/config.toml', encoding='utf-8') as config:
    config_data = tomli.load(config)
    token = config_data['token']

bot.run(token)
