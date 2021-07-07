import random
import json
import discord


def open_str():
    """Opens the string's database."""
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        string = json.loads(data)
        return string


string = open_str()


def rbColor():
    """Returns one of the main colors of RoboTito."""
    colors = [discord.Color.from_rgb(255, 94, 43),
              discord.Color.from_rgb(82, 92, 253),
              discord.Color.from_rgb(72, 159, 181),
              discord.Color.from_rgb(255, 134, 0)
              ]
    return random.choice(colors)

# Functions used in cog/anime.py


def gif(table):
    """Returns an random gif from the given table."""
    with open('databases/db_gifs.json') as f:
        data = f.read()
        gif = json.loads(data)
        return random.choice(gif[table])


def header(table):
    """Returns the "header" (main sentence) for interaction commands."""
    header = open_str()[table]
    return random.choice(header)


def sentence(author, msg, member=None):
    """Returns the message that will show in interaction commands."""
    if member is None:
        message = random.choice(string[msg])
        result = author + message
        return result
    else:
        message = random.choice(string[msg])
        result = author + message + member
        return result


# Functions used in cog/commands.py


def get_8ball():
    """Returns a random response for 8ball command."""
    return random.choice(string['ball8'])


def get_penis(number: int):
    """Returns a random measure unit for penis commands."""
    if number >= 1:
        return random.choice(string['penis'])
    else:
        pass


def get_love(number: int):
    """Returns a random phrase for love command, based on the rate."""
    if number >= 75:
        return random.choice(string['love_high'])
    elif number >= 45:
        return random.choice(string['love_medium'])
    else:
        return random.choice(string['love_low'])


def get_love_gif(number: int):
    """Returns a random gif for love command, based on the rate."""
    with open('databases/db_gifs.json', encoding='utf-8') as f:
        gifData = f.read()
        gifstring = json.loads(gifData)
        if number >= 65:
            gif = random.choice(gifstring['love_high'])
            return gif
        else:
            gif = random.choice(gifstring['love_low'])
            return gif
