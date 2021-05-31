import random

import json

from discord.ext import commands


def open_str():
    with open('databases/db_str.json', encoding='utf8') as f:
        data = f.read()
        string = json.loads(data)
        return string


string = open_str()


class Functions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Functions used in cog/anime.py

    def gif(string):
        with open('databases/db_gifs.json') as f:
            data = f.read()
            gif = json.loads(data)
            return random.choice(gif[string])

    def header(table):
        header = string[table]
        return random.choice(header)

    def sentence(author, msg, member=None):
        if member is None:
            message = random.choice(string[msg])
            result = author + message
            return result
        else:
            message = random.choice(string[msg])
            result = author + message + member
            return result

    def sameUser(activity):
        message = 'Trata de ' + activity + ' alguien más.'
        return message

    # Functions used in cog/commands.py

    def get8Ball():
        return random.choice(string['ball8'])

    def getPenis(number: int):
        if number > 1:
            return random.choice(string['penis'])
        elif number == 1:
            return random.choice(string['penis'])
        else:
            pass

    def getLove(number: int):
        if number >= 75:
            return random.choice(string['love_high'])
        elif number >= 45:
            return random.choice(string['love_medium'])
        else:
            return random.choice(string['love_low'])

    def getLoveGif(number: int):
        with open('databases/db_gifs.json', encoding='utf-8') as f:
            gifData = f.read()
            gifstring = json.loads(gifData)
            if number >= 65:
                gif = random.choice(gifstring['love_high'])
                return gif
            else:
                gif = random.choice(gifstring['love_low'])
                return gif


def setup(bot):
    bot.add_cog(Functions(bot))
