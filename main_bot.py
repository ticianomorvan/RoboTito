import discord
import logging
import os
import tomli
from discord.ext import commands
from cog.functions.functions import Functions as f
from pretty_help import DefaultMenu, PrettyHelp

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

bot = commands.Bot(command_prefix=['rb!', 'rt!', 'r.'], case_insensitive=True,
                   intents=intents, help_command=None)

for filename in os.listdir('./cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'cog.{filename[:-3]}')

menu = DefaultMenu(page_left='⬅', page_right='➡', remove='🚫')
bot.help_command = PrettyHelp(color=f.rbColor(), menu=menu,
                              index_title='Comandos de RoboTito',
                              ending_note='Escribe r.help <comando>'
                              ' para más info. sobre algún comando.\nTambién'
                              ' puedes escribir r.help <categoría> para más'
                              ' info. de esa categoría.')


@bot.event
async def on_ready():
    print('Conectado como {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(
                                type=discord.ActivityType.watching,
                                name='RoboTito! | r.help'))

# Run

# You have to create an "config.toml" file at databases folder, with:
# "token": "your_bot_token"
# "api": "your_rapidapi_token"

with open('databases/config.toml', encoding='utf-8') as f:
    config_data = tomli.load(f)
    token = config_data['token']

bot.run(token)
