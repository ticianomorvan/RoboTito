import json
from nextcord.ext import commands
from nextcord.flags import Intents


# Intents declaration
intents = Intents.all()

# Client declaration
client = commands.Bot(
    command_prefix='r!',
    description='Re-version of RoboTito.',
    intents=intents
)

client_extensions = [
    'extensions.information',
    'extensions.moderation',
    'extensions.passwords'
]

for extension in client_extensions:
    client.load_extension(extension)


@client.event
async def on_ready():
    print(f'Ready & Logged as {client.user}')


with open('config.json', 'r') as configuration_file:
    configuration = json.load(configuration_file)
    token = configuration['token']


client.run(token)
