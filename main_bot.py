import discord
from discord.ext import commands

import logging

import os

import json

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(
    filename='robotito.log',
    encoding='utf-8',
    mode='w',
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s')
)
logger.addHandler(handler)

# Inicio
intents = discord.Intents.all()

intents.members = True

bot = commands.Bot(command_prefix=['rb!', 'rt!', 'r.'],
                   intents=intents)

for filename in os.listdir('./cog'):
    if filename.endswith('.py'):
        bot.load_extension(f'cog.{filename[:-3]}')


@bot.event
async def on_ready():
    print('Conectado como {0.user}'.format(bot))
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name='robotito.readme.io'
        )
    )

# Token
with open('databases/db_bot.json') as f:
    token_data = f.read()
    token = json.loads(token_data)
bot.run(token['token'])
